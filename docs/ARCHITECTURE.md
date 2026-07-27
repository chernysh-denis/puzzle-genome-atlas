# Repository Architecture

Puzzle Genome Atlas separates accepted knowledge from active investigation.
That boundary is the main scaling rule.

## Top-level structure

```text
docs/        Method, governance, evidence model and research plan
knowledge/   Canonical genes, game genomes and verified combinations
research/    Leads, taxonomy proposals, candidates and negative results
templates/   Required contribution formats
scripts/     Repository-integrity validation
```

Root files are limited to public orientation and project governance.

## Stable identifiers

- Games: `GAME-xxxx`
- Genes: `ACT-xxx`, `SYS-xxx`, `CON-xxx`, `INF-xxx`, `OBJ-xxx`, `TIM-xxx`
- Combinations: `COMB-xxxx`
- Taxonomy changes: `TAXONOMY_CHANGE_xxx`

IDs are never reused. Renames change labels, not identifiers.

## Game-file scaling

Game analyses use stable alphabetical path shards:

```text
knowledge/games/0-9/
knowledge/games/a-f/
knowledge/games/g-l/
knowledge/games/m-r/
knowledge/games/s-z/
```

The shard is non-semantic, so a change in puzzle family never moves a file.

## Comparison scaling

Every new genome is still checked against the full corpus, but the result is
not copied as hundreds of prose rows into the new analysis.

1. Scan stable gene and combination signatures in the corpus indexes.
2. Record every exact structural match.
3. Describe only the closest decision-relevant neighbours in detail.
4. Put shared combination knowledge in one `COMB-xxxx` record.

This preserves exhaustive matching while avoiding quadratic narrative
duplication.

## Expected scale

| Corpus size | Architecture response |
|---|---|
| 100 games | Markdown indexes and path shards remain sufficient. |
| 500 games | Generate indexes and validation reports from stable front matter; paths do not change. |
| 1000 games | Add search or database views as derived interfaces; Markdown records and IDs remain canonical. |

Automation may be added without relocating knowledge records.

## Integrity checks

`scripts/validate_repository.py` verifies local Markdown links, stable-ID
uniqueness, gene references and index coverage. Continuous integration also
runs Markdown lint. These checks protect the canonical paths and IDs without
introducing a database or build system.

## Architecture change policy

This revision is intended to be the last broad relocation. Future structural
changes require:

1. a concrete scaling or integrity failure;
2. an architecture decision record in `docs/architecture-decisions/`;
3. a migration plan with link validation;
4. preservation of stable IDs and Git history.

Adding genes, analyses, combinations or validators is normal knowledge work and
does not count as an architecture change.
