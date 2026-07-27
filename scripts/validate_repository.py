#!/usr/bin/env python3
"""Validate Puzzle Genome Atlas records without third-party dependencies."""

from __future__ import annotations

import re
import sys
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
EXCLUDED_PARTS = {".git", "logs", "private"}
GENE_ID = re.compile(r"\b(?:ACT|SYS|CON|INF|OBJ|TIM)-\d{3}\b")
GENE_DEFINITION = re.compile(
    r"^## ((?:ACT|SYS|CON|INF|OBJ|TIM)-\d{3})\b", re.MULTILINE
)
GAME_FRONT_MATTER = re.compile(r"^game_id:\s*(GAME-\d{4})\s*$", re.MULTILINE)
COMBINATION_HEADING = re.compile(r"^# (COMB-\d{4})\b", re.MULTILINE)
MARKDOWN_LINK = re.compile(r"\[[^\]]*\]\(([^)]+)\)")


def markdown_files() -> list[Path]:
    return [
        path
        for path in ROOT.rglob("*.md")
        if not EXCLUDED_PARTS.intersection(path.relative_to(ROOT).parts)
    ]


def fail(errors: list[str], message: str) -> None:
    errors.append(message)


def validate_links(files: list[Path], errors: list[str]) -> None:
    for path in files:
        text = path.read_text(encoding="utf-8")
        for raw_target in MARKDOWN_LINK.findall(text):
            target = raw_target.removeprefix("<").removesuffix(">")
            if target.startswith(("http://", "https://", "mailto:", "#")):
                continue
            relative_target = target.split("#", 1)[0]
            if not relative_target:
                continue
            resolved = (path.parent / relative_target).resolve()
            if not resolved.exists():
                fail(
                    errors,
                    f"{path.relative_to(ROOT)}: broken local link {raw_target}",
                )


def definitions(
    files: list[Path], pattern: re.Pattern[str], errors: list[str], label: str
) -> dict[str, Path]:
    occurrences: list[tuple[str, Path]] = []
    for path in files:
        text = path.read_text(encoding="utf-8")
        occurrences.extend((identifier, path) for identifier in pattern.findall(text))

    counts = Counter(identifier for identifier, _ in occurrences)
    for identifier, count in sorted(counts.items()):
        if count > 1:
            fail(errors, f"{label} {identifier} is defined {count} times")

    return {identifier: path for identifier, path in occurrences}


def validate_gene_references(
    files: list[Path], gene_definitions: dict[str, Path], errors: list[str]
) -> None:
    referenced: set[str] = set()
    for path in files:
        referenced.update(GENE_ID.findall(path.read_text(encoding="utf-8")))
    for identifier in sorted(referenced - gene_definitions.keys()):
        fail(errors, f"gene {identifier} is referenced but not defined")


def validate_index(
    definitions_by_id: dict[str, Path],
    index_path: Path,
    errors: list[str],
    label: str,
) -> None:
    index_text = index_path.read_text(encoding="utf-8")
    for identifier in sorted(definitions_by_id):
        if identifier not in index_text:
            fail(errors, f"{label} {identifier} is missing from {index_path.name}")


def main() -> int:
    errors: list[str] = []
    files = markdown_files()

    validate_links(files, errors)
    genes = definitions(files, GENE_DEFINITION, errors, "gene")

    game_files = list((ROOT / "knowledge/games").glob("*/*.md"))
    games = definitions(game_files, GAME_FRONT_MATTER, errors, "game")

    combination_files = list((ROOT / "knowledge/combinations").glob("COMB-*.md"))
    combinations = definitions(
        combination_files, COMBINATION_HEADING, errors, "combination"
    )

    validate_gene_references(files, genes, errors)
    validate_index(
        games, ROOT / "knowledge/games/INDEX.md", errors, "game"
    )
    validate_index(
        combinations,
        ROOT / "knowledge/combinations/INDEX.md",
        errors,
        "combination",
    )

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
