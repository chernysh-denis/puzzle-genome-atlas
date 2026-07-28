# Game Genomes

Each game file contains a complete evidence-backed decomposition and a typed
genome. The [index](INDEX.md) is the canonical corpus lookup.

## Required contents

- stable `GAME-xxxx` ID and path slug;
- sources and claim ledger;
- player actions and automatic behaviours;
- constraints, information, objectives and time;
- strategy, replay, failure and adjacent systems;
- active gene IDs;
- full-corpus comparison using the
  [canonical signature rules](../../docs/ARCHITECTURE.md#genome-signature);
- mathematically selected near matches;
- combination result and explicit negative findings.

## Path rule

Use one non-semantic slug shard:

- `0-9/`
- `a-f/`
- `g-l/`
- `m-r/`
- `s-z/`

Do not organise canonical files by puzzle family. Family classifications may
change; stable paths should not.

## Completed

- [`GAME-0001` — 2048](0-9/2048.md)
- [`GAME-0002` — Rubik's Cube](m-r/rubiks-cube.md)
- [`GAME-0003` — Minesweeper](m-r/minesweeper.md)

Use the [game-analysis template](../../templates/GAME_ANALYSIS_TEMPLATE.md) and
follow [CONTRIBUTING.md](../../CONTRIBUTING.md). The
[research plan](../../docs/RESEARCH_PLAN.md) owns subject selection.
