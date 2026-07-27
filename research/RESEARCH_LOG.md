# Public Research Log

This log records concise, structured results that change the public Puzzle
Genome Atlas corpus. Local notes and personal observations are intentionally
excluded.

## 2026-07-27 — Research foundation

- Established the mission, layered mechanics taxonomy, combination matrix and
  evidence-first process.
- Adopted the original evidence ladder; it was superseded by the three-field
  evidence model during the architecture review below.
- Added mandatory genome comparison, negative-result reporting and auditable taxonomy-change proposals.
- Replaced fixed game order with an adaptive maximum-information-gain plan.

## 2026-07-27 — 2048 baseline decomposition

- Added the first full game analysis, now located at
  [`GAME-0001`](../knowledge/games/0-9/2048.md).
- Corrected the core classification from player-commanded merge to global directional slide with automatic ordered collision merging and random spawn.
- Identified maneuverable empty space as the primary scarce strategic resource.
- Recorded 2048 as the baseline genome; no novelty claim can be made against an empty prior corpus.
- Selected Rubik's Cube as the next analysis for expected structural distance.

## 2026-07-27 — Public research release

- Added public governance, contribution and licensing files.
- Separated structured public research from ignored local notes and logs.
- Added the first-version research roadmap and directory-level publication rules.
- Published the reviewed corpus, now available as
  [`puzzle-genome-atlas`](https://github.com/chernysh-denis/puzzle-genome-atlas).

## 2026-07-27 — Final architecture revision

- Renamed the public project to Puzzle Genome Atlas.
- Separated method (`docs/`), canonical knowledge (`knowledge/`) and active
  investigation (`research/`).
- Added stable IDs for games, genes and combinations.
- Replaced undefined taxonomy lists with an active gene registry plus preserved
  candidate vocabulary.
- Replaced the single evidence ladder with claim status, evidence quality and
  confidence.
- Added non-semantic game-path shards and central combination records to avoid
  quadratic pairwise prose at 100–1000 analyses.
- Recorded the change in `TAXONOMY_CHANGE_001` and `ADR-001`.

## 2026-07-28 — Final methodology normalisation

- Formalised exact and near genome comparison, separated combinations from full
  genomes, consolidated status definitions and aligned validation with the
  documented method.
- Recorded the scope as an amendment to
  [`ADR-001`](../docs/architecture-decisions/ADR-001-scalable-knowledge-architecture.md).
- No game evidence, gene ID or novelty conclusion changed.

## 2026-07-28 — Rubik's Cube architecture stress test

- Added the complete sourced
  [`GAME-0002`](../knowledge/games/m-r/rubiks-cube.md) decomposition.
- Reused `CON-001` and `INF-001`; admitted five bounded genes for direct layer
  rotation, invariant-constrained reachability, primitive reversibility,
  configuration reconstruction and self-paced sequential action.
- Registered `COMB-0002` as a proper subset of the seven-gene genome.
- Found no System Behaviour gene and no failure of the six-type model.
- Compared the full signature with `GAME-0001`: two shared typed genes and
  structural Jaccard score `2 / 19 = 0.105263`.
- Selected Minesweeper next for maximum expected information gain, chiefly to
  test hidden state and randomness-at-setup boundaries.
