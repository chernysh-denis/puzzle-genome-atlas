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
- full-corpus signature scan;
- nearest structural neighbours;
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

## Next

- `GAME-0002` — Rubik's Cube

Use the [game-analysis template](../../templates/GAME_ANALYSIS_TEMPLATE.md) and
follow [CONTRIBUTING.md](../../CONTRIBUTING.md).
