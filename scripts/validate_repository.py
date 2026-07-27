#!/usr/bin/env python3
"""Validate Puzzle Genome Atlas records without third-party dependencies."""

from __future__ import annotations

import re
import sys
from collections import Counter
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
EXCLUDED_PARTS = {".git", "logs", "private"}
GENE_TYPES = {
    "action": "ACT",
    "system": "SYS",
    "constraint": "CON",
    "information": "INF",
    "objective": "OBJ",
    "time": "TIM",
}

GENE_ID = re.compile(r"\b(?:ACT|SYS|CON|INF|OBJ|TIM)-\d{3}\b")
GENE_HEADING = re.compile(
    r"^## ((?:ACT|SYS|CON|INF|OBJ|TIM)-\d{3})\b", re.MULTILINE
)
GAME_ID = re.compile(r"\bGAME-\d{4}\b")
COMBINATION_HEADING = re.compile(r"^# (COMB-\d{4})\b", re.MULTILINE)
MARKDOWN_LINK = re.compile(r"\[[^\]]*\]\(([^)]+)\)")

CLAIM_STATUSES = {
    "Observation",
    "Hypothesis",
    "Pattern",
    "Strong Pattern",
    "Confirmed",
}
EVIDENCE_QUALITIES = {"Direct", "Corroborated", "Limited", "Conflicting"}
CONFIDENCE_LEVELS = {"Low", "Medium", "High"}
GENE_LIFECYCLES = {"Active", "Deprecated", "Merged", "Split"}
ANALYSIS_STATUSES = {"draft", "reviewed"}
PROPOSAL_STATUSES = {"Proposed", "Accepted", "Rejected", "Superseded"}


@dataclass
class Game:
    genes_by_type: dict[str, set[str]]
    combinations: set[str]
    status: str

    @property
    def genes(self) -> set[str]:
        return set().union(*self.genes_by_type.values())


@dataclass
class Combination:
    genes: set[str]
    games: set[str]


def fail(errors: list[str], path: Path | str, message: str) -> None:
    label = path.relative_to(ROOT) if isinstance(path, Path) else path
    errors.append(f"{label}: {message}")


def markdown_files() -> list[Path]:
    return [
        path
        for path in ROOT.rglob("*.md")
        if not EXCLUDED_PARTS.intersection(path.relative_to(ROOT).parts)
    ]


def scalar(text: str, name: str) -> str | None:
    match = re.search(
        rf"^{re.escape(name)}:\s*[\"']?([^\"'\n]+?)[\"']?\s*$",
        text,
        re.MULTILINE,
    )
    return match.group(1).strip() if match else None


def record_field(text: str, name: str) -> str | None:
    match = re.search(
        rf"^- {re.escape(name)}:\s*`?([^`\n]+?)`?\s*$", text, re.MULTILINE
    )
    return match.group(1).strip() if match else None


def list_values(text: str, name: str, indent: int) -> list[str]:
    spaces = " " * indent
    match = re.search(
        rf"^{spaces}{re.escape(name)}:\s*(?:\[\])?[ \t]*\n"
        rf"((?:{spaces}  - [^\n]+\n)*)",
        text,
        re.MULTILINE,
    )
    if not match:
        return []
    return [
        line.split("-", 1)[1].strip()
        for line in match.group(1).splitlines()
    ]


def section(text: str, heading: str) -> str:
    match = re.search(
        rf"^## {re.escape(heading)}\s*$\n(.*?)(?=^## |\Z)",
        text,
        re.MULTILINE | re.DOTALL,
    )
    return match.group(1) if match else ""


def heading_block(text: str, heading: str) -> str:
    match = re.search(
        rf"^## {re.escape(heading)}\b.*?\n(.*?)(?=^## |\Z)",
        text,
        re.MULTILINE | re.DOTALL,
    )
    return match.group(1) if match else ""


def check_controlled(
    text: str,
    path: Path,
    fields: tuple[tuple[str, set[str]], ...],
    errors: list[str],
) -> None:
    for name, allowed in fields:
        value = record_field(text, name)
        if value not in allowed:
            fail(
                errors,
                path,
                f"{name} must be one of {', '.join(sorted(allowed))}; "
                f"found {value!r}",
            )


def validate_links(files: list[Path], errors: list[str]) -> None:
    for path in files:
        text = path.read_text(encoding="utf-8")
        for raw in MARKDOWN_LINK.findall(text):
            target = raw.removeprefix("<").removesuffix(">")
            if target.startswith(("http://", "https://", "mailto:", "#")):
                continue
            local = target.split("#", 1)[0]
            if local and not (path.parent / local).resolve().exists():
                fail(errors, path, f"broken local link {raw}")


def gene_definitions(
    files: list[Path], errors: list[str]
) -> dict[str, Path]:
    found = [
        (identifier, path)
        for path in files
        for identifier in GENE_HEADING.findall(path.read_text(encoding="utf-8"))
    ]
    for identifier, count in Counter(item[0] for item in found).items():
        if count > 1:
            fail(errors, identifier, f"defined {count} times")
    return {identifier: path for identifier, path in found}


def validate_genes(genes: dict[str, Path], errors: list[str]) -> None:
    controlled = (
        ("Lifecycle", GENE_LIFECYCLES),
        ("Claim status", CLAIM_STATUSES),
        ("Evidence quality", EVIDENCE_QUALITIES),
        ("Confidence", CONFIDENCE_LEVELS),
    )
    for identifier, path in genes.items():
        block = heading_block(path.read_text(encoding="utf-8"), identifier)
        check_controlled(block, path, controlled, errors)
        for name in ("Definition", "Includes", "Excludes", "Evidence"):
            if not re.search(rf"^- {name}:\s*\S", block, re.MULTILINE):
                fail(errors, path, f"{identifier} lacks {name}")


def shard(slug: str) -> str:
    first = slug[:1].lower()
    if first.isdigit():
        return "0-9"
    return next(
        (
            name
            for name in ("a-f", "g-l", "m-r", "s-z")
            if name[0] <= first <= name[2]
        ),
        "",
    )


def validate_claim_ledger(text: str, path: Path, errors: list[str]) -> None:
    for line in section(text, "Claim ledger").splitlines():
        if not re.match(r"^\| `?C[^|]+", line):
            continue
        cells = [cell.strip().strip("`") for cell in line.strip("|").split("|")]
        if len(cells) < 6:
            fail(errors, path, "malformed claim-ledger row")
            continue
        checks = (
            (cells[2], CLAIM_STATUSES, "claim status"),
            (cells[3], EVIDENCE_QUALITIES, "evidence quality"),
            (cells[4], CONFIDENCE_LEVELS, "confidence"),
        )
        for value, allowed, label in checks:
            if value not in allowed:
                fail(errors, path, f"invalid {label} {value}")
        if not cells[5]:
            fail(errors, path, "claim lacks sources")


def parse_games(errors: list[str]) -> dict[str, Game]:
    games: dict[str, Game] = {}
    for path in (ROOT / "knowledge/games").glob("*/*.md"):
        text = path.read_text(encoding="utf-8")
        identifier = scalar(text, "game_id")
        if not identifier or not re.fullmatch(r"GAME-\d{4}", identifier):
            fail(errors, path, "missing or invalid game_id")
            continue
        if identifier in games:
            fail(errors, identifier, "defined more than once")
            continue

        required = ("slug", "game_title", "analysis_status", "reviewed")
        values = {name: scalar(text, name) for name in required}
        for name, value in values.items():
            if not value:
                fail(errors, path, f"missing {name}")

        status = values["analysis_status"] or ""
        if status not in ANALYSIS_STATUSES:
            fail(errors, path, f"invalid analysis_status {status!r}")
        slug_value = values["slug"] or ""
        if path.stem != slug_value or path.parent.name != shard(slug_value):
            fail(errors, path, "slug, filename and shard do not agree")

        genes_by_type: dict[str, set[str]] = {}
        seen: set[str] = set()
        for type_name, prefix in GENE_TYPES.items():
            if not re.search(
                rf"^  {type_name}:\s*(?:\[\])?\s*$", text, re.MULTILINE
            ):
                fail(errors, path, f"missing gene type {type_name}")
            raw = list_values(text, type_name, 2)
            if len(raw) != len(set(raw)):
                fail(errors, path, f"duplicate ID in {type_name}")
            genes_by_type[type_name] = set(raw)
            for gene in raw:
                if not re.fullmatch(rf"{prefix}-\d{{3}}", gene):
                    fail(errors, path, f"{gene} is in the wrong type")
                if gene in seen:
                    fail(errors, path, f"duplicate gene {gene}")
                seen.add(gene)

        game = Game(
            genes_by_type=genes_by_type,
            combinations=set(list_values(text, "combination_ids", 0)),
            status=status,
        )
        if not game.genes:
            fail(errors, path, "genome must contain a gene")
        games[identifier] = game
        validate_claim_ledger(text, path, errors)
    return games


def parse_combinations(errors: list[str]) -> dict[str, Combination]:
    records: dict[str, Combination] = {}
    controlled = (
        ("Claim status", CLAIM_STATUSES),
        ("Evidence quality", EVIDENCE_QUALITIES),
        ("Confidence", CONFIDENCE_LEVELS),
    )
    for path in (ROOT / "knowledge/combinations").glob("COMB-*.md"):
        text = path.read_text(encoding="utf-8")
        match = COMBINATION_HEADING.search(text)
        if not match:
            fail(errors, path, "missing combination ID")
            continue
        identifier = match.group(1)
        if identifier in records:
            fail(errors, identifier, "defined more than once")
            continue
        check_controlled(text, path, controlled, errors)
        records[identifier] = Combination(
            genes=set(GENE_ID.findall(section(text, "Combination gene set"))),
            games=set(GAME_ID.findall(section(text, "Analysed games"))),
        )
    return records


def validate_relations(
    files: list[Path],
    genes: dict[str, Path],
    games: dict[str, Game],
    combinations: dict[str, Combination],
    errors: list[str],
) -> None:
    referenced = {
        identifier
        for path in files
        for identifier in GENE_ID.findall(path.read_text(encoding="utf-8"))
    }
    for identifier in sorted(referenced - genes.keys()):
        fail(errors, identifier, "referenced but not defined")

    for game_id, game in games.items():
        for identifier in sorted(game.genes - genes.keys()):
            fail(errors, game_id, f"undefined gene {identifier}")
        for identifier in sorted(game.combinations - combinations.keys()):
            fail(errors, game_id, f"undefined combination {identifier}")

    for combination_id, combination in combinations.items():
        types = {gene.split("-", 1)[0] for gene in combination.genes}
        if len(combination.genes) < 2 or len(types) < 2:
            fail(errors, combination_id, "requires two genes from two types")
        for identifier in sorted(combination.genes - genes.keys()):
            fail(errors, combination_id, f"undefined gene {identifier}")
        for game_id in sorted(combination.games - games.keys()):
            fail(errors, combination_id, f"undefined game {game_id}")
        for game_id in combination.games & games.keys():
            game = games[game_id]
            if not combination.genes < game.genes:
                fail(errors, combination_id, f"not a proper subset of {game_id}")
            if combination_id not in game.combinations:
                fail(errors, combination_id, f"{game_id} lacks reciprocal link")

    for game_id, game in games.items():
        for combination_id in game.combinations & combinations.keys():
            if game_id not in combinations[combination_id].games:
                fail(errors, game_id, f"{combination_id} lacks reciprocal link")


def table_row(text: str, identifier: str) -> str:
    return next(
        (
            line
            for line in text.splitlines()
            if line.startswith("|") and identifier in line
        ),
        "",
    )


def signature(game: Game) -> str:
    return "; ".join(
        ",".join(sorted(game.genes_by_type[type_name]))
        for type_name in GENE_TYPES
    )


def validate_indexes(
    games: dict[str, Game],
    combinations: dict[str, Combination],
    errors: list[str],
) -> None:
    game_index = (ROOT / "knowledge/games/INDEX.md").read_text(encoding="utf-8")
    for identifier, game in games.items():
        row = table_row(game_index, identifier)
        expected_combinations = set(re.findall(r"\bCOMB-\d{4}\b", row))
        if not row:
            fail(errors, identifier, "missing from game index")
        elif f"`{signature(game)}`" not in row:
            fail(errors, identifier, "index signature differs from front matter")
        elif expected_combinations != game.combinations:
            fail(errors, identifier, "index combinations differ from front matter")
        elif f"`{game.status}`" not in row:
            fail(errors, identifier, "index analysis status differs")

    combination_index = (
        ROOT / "knowledge/combinations/INDEX.md"
    ).read_text(encoding="utf-8")
    for identifier, combination in combinations.items():
        row = table_row(combination_index, identifier)
        if not row:
            fail(errors, identifier, "missing from combination index")
        elif set(GENE_ID.findall(row)) != combination.genes:
            fail(errors, identifier, "index gene set differs from record")
        elif set(GAME_ID.findall(row)) != combination.games:
            fail(errors, identifier, "index games differ from record")


def validate_taxonomy_changes(errors: list[str]) -> None:
    controlled = (
        ("Proposal status", PROPOSAL_STATUSES),
        ("Claim status", CLAIM_STATUSES),
        ("Evidence quality", EVIDENCE_QUALITIES),
        ("Confidence", CONFIDENCE_LEVELS),
    )
    seen: set[str] = set()
    directory = ROOT / "research/taxonomy-changes"
    for path in directory.glob("TAXONOMY_CHANGE_*.md"):
        match = re.fullmatch(r"TAXONOMY_CHANGE_(\d{3})\.md", path.name)
        if not match:
            fail(errors, path, "invalid taxonomy filename")
            continue
        identifier = match.group(1)
        if identifier in seen:
            fail(errors, identifier, "duplicate taxonomy change")
        seen.add(identifier)
        text = path.read_text(encoding="utf-8")
        if not re.search(rf"^# Taxonomy Change {identifier}\b", text, re.MULTILINE):
            fail(errors, path, "heading does not match filename")
        check_controlled(text, path, controlled, errors)


def main() -> int:
    errors: list[str] = []
    files = markdown_files()
    validate_links(files, errors)
    genes = gene_definitions(files, errors)
    validate_genes(genes, errors)
    games = parse_games(errors)
    combinations = parse_combinations(errors)
    validate_relations(files, genes, games, combinations, errors)
    validate_indexes(games, combinations, errors)
    validate_taxonomy_changes(errors)

    if errors:
        print("Repository validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print(
        "Repository validation passed: "
        f"{len(files)} Markdown files, {len(genes)} genes, "
        f"{len(games)} games, {len(combinations)} combinations."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
