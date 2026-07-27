# Project Atlas

**Project Atlas is an open research project that maps the fundamental mechanics of puzzle games.**

Its goal is not to invent a game prematurely. Atlas decomposes existing puzzles into comparable mechanical genes, maps combinations that already exist, and only then investigates combinations that may be genuinely underexplored.

## The problem

Puzzle games are usually catalogued by genre, theme, platform or popularity. Those labels do not answer the questions Atlas is built around:

1. What fundamental player actions, system behaviours and constraints exist?
2. Which combinations of those mechanics have already been used?
3. Which combinations are absent, rare or poorly studied?

Atlas treats novelty as a research claim, not a creative adjective. A new theme, interface or numerical tuning is not a new mechanic.

## How Atlas differs from a game catalogue

| Conventional catalogue | Project Atlas |
|---|---|
| Groups games by genre or presentation | Decomposes games into normalised mechanical genes |
| Describes what a game looks like | Records player actions, system responses, constraints, information, time and objectives |
| Lists similar titles | Compares every new game with every previously analysed genome |
| May call an unusual theme novel | Requires external evidence before any novelty claim |
| Focuses on successful or popular releases | Includes classical, mathematical, mechanical, historical, academic and experimental puzzles |

## The Atlas method

Each game analysis separates six layers:

1. **Player actions** — what the player directly commands.
2. **System behaviours** — what resolves automatically.
3. **Constraints** — what limits access, capacity, sequence or choice.
4. **Information model** — what is visible, hidden, random or previewed.
5. **Time model** — how actions and resolution are scheduled.
6. **Objectives and evaluation** — what counts as progress, success or failure.

Claims use a conservative evidence ladder:

`Observation → Pattern → Confirmed Pattern → Law`

Codex and contributors may not assign `Law`; that status requires explicit human review after broad cross-family evidence.

After every decomposition, Atlas reports one genome result:

- `New gene`
- `New combination of known genes`
- `Full structural match`

If no new gene was found, the analysis must state that directly.

## Current status

Atlas is in **Stage 1: taxonomy and evidence collection**.

- First completed decomposition: [2048](research/games/2048.md)
- Current next subject: Rubik's Cube, selected for maximum expected mechanical distance from 2048
- Prototyping: not started
- Novelty claims: none

See the [research plan](06_RESEARCH_PLAN.md) for the adaptive analysis queue and the [v1 roadmap](ROADMAP.md) for release criteria.

## Start reading

- [Mission and boundaries](00_MISSION.md)
- [Research principles](01_RESEARCH_PRINCIPLES.md)
- [Evidence model](02_EVIDENCE_MODEL.md)
- [Working hypotheses](03_WORKING_HYPOTHESES.md)
- [Mechanics taxonomy](04_MECHANICS_TAXONOMY.md)
- [Combination matrix](05_COMBINATION_MATRIX.md)
- [Research plan](06_RESEARCH_PLAN.md)
- [Public research log](research/RESEARCH_LOG.md)
- [Game analyses](research/games/README.md)

## Contributing

Contributions are welcome from puzzle players, designers, historians and researchers.

The shortest useful contribution path is:

1. Open an issue proposing a mechanically diverse puzzle or a correction.
2. Prefer primary sources, direct gameplay evidence and reproducible rule transitions.
3. Use the appropriate file in [`templates/`](templates/).
4. Compare a new game with every existing analysis and update the matrix.

Do not submit raw game ideas, reskins or unsupported novelty claims. Read [CONTRIBUTING.md](CONTRIBUTING.md) for the research workflow and review checklist.

## Public research scope

This repository publishes structured research materials only. Personal notes, local logs, credentials, raw idea dumps and unfinished scratch work are excluded from version control.

## License and conduct

Research text and repository materials are available under the [MIT License](LICENSE). Participation is governed by the [Code of Conduct](CODE_OF_CONDUCT.md).
