# Research Plan

This document owns subject selection. Release gates and corpus-size targets
belong only in [`ROADMAP.md`](../ROADMAP.md).

The plan is adaptive. Coverage targets are not a fixed sequence.

## Selection rule

Choose the next subject for expected information gain:

1. prefer mechanical distance from the completed corpus;
2. cover gene types and boundaries that remain weakly tested;
3. avoid consecutive close relatives when a higher-information subject exists;
4. preserve displaced subjects in the coverage pool;
5. reassess after every completed analysis.

This selection rule decides order; it does not claim that the chosen game or
its mechanics are novel.

## Coverage pool

The current task is listed separately below.

1. Minesweeper
2. Tetris
3. FreeCell
4. Sudoku
5. Sokoban
6. Nonogram
7. Water Sort
8. Royal Match
9. Chess
10. Threes
11. Flow Free
12. Pipe Mania
13. Baba Is You
14. Mini Metro
15. Balatro
16. Into the Breach
17. Dorfromantik
18. Peg Solitaire

The pool is coverage backlog, not a commitment or a novelty claim. The
operational analysis workflow lives only in
[`CONTRIBUTING.md`](../CONTRIBUTING.md).

## Immediate next task

Analyse Rubik's Cube next.

- Claim status: `Hypothesis`
- Evidence quality: `Limited`
- Confidence: `Medium`
- Reason: it replaces 2048's stochastic spawning and capacity economy with
  deterministic reversible transformations, permutation/orientation constraints
  and state reconstruction.
- Model test: determine whether permutation, orientation and reachability fit
  the current six gene types without distortion.

This is the highest-information next subject under current evidence. Reassess
after `GAME-0002`.
