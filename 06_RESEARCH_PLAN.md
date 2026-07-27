# Research Plan

## Phase 1 — Build the catalogue

1. Expand elementary actions to 40–60 well-defined operations.
2. Expand system behaviours to 25–40.
3. Expand constraints to 20–30.
4. Merge synonyms and document distinctions.
5. Add representative games and evidence.

## Phase 2 — Decompose known games

Coverage pool; this is not a fixed analysis order:

1. 2048
2. Water Sort
3. Royal Match
4. Solitaire / FreeCell
5. Tetris
6. Chess
7. Sudoku
8. Minesweeper
9. Sokoban
10. Nonogram
11. Threes
12. Flow Free
13. Pipe Mania
14. Baba Is You
15. Mini Metro
16. Balatro
17. Into the Breach
18. Dorfromantik
19. Peg Solitaire
20. Rubik's Cube

For each, identify actions, automatic response, constraints, information model, objective, strategic depth, heuristics, replay variation, failure attribution and adjacent games.

After each decomposition, normalise its mechanical genome and compare it with every game already present in `research/games/`. Record whether it contains a new gene, a new combination of known genes or a full structural match. State explicitly when there are no new genes.

Do not select the next game by list position. Select the game with the highest expected mechanical distance from the most recently analysed game and the largest expected coverage gain for the whole corpus. The recommendation must name the missing layers or contrasts it is expected to add.

After every completed analysis, audit this plan against the enlarged corpus:

- `Plan status: optimal under current evidence` — state why the current next step still dominates plausible alternatives.
- `Plan status: not optimal` — immediately provide a replacement sequence, optimisation criterion, expected information gain and the items returned to the coverage backlog.

The plan is a falsifiable working schedule, not an instruction to continue after its assumptions stop holding.

## Phase 3 — Populate combinations

- Record known combinations.
- Search market and historical catalogues.
- Mark confidence explicitly.
- Identify sparse combinations, not merely empty-looking cells.

## Phase 4 — Candidate filtering

Advance only when the combination is not a reskin, has no obvious established equivalent, is simple to explain, readable, state-rich and prototypable.

## Immediate next task

Analyse Rubik's Cube next. Relative to 2048 it replaces global compression, collision merging, random spawning and scarce empty cells with deterministic reversible layer rotation, permutation constraints, fixed occupancy and state reconstruction. This is expected to increase Atlas diversity more than another spawn-and-space or sorting puzzle.

Plan status: optimal under current evidence. Rubik's Cube currently supplies a larger expected contrast with the sole analysed genome than Water Sort, match-3, Threes or another grid-based spawning system. This status must be reassessed after the Rubik's Cube decomposition.

Progress:

1. 2048 — completed: `research/games/2048.md`
2. Rubik's Cube — next
3. Water Sort — coverage backlog
4. Royal Match — coverage backlog
5. Solitaire / FreeCell — coverage backlog
6. Tetris — coverage backlog
