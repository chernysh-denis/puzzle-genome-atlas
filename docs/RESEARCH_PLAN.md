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

1. Tetris
2. FreeCell
3. Sudoku
4. Sokoban
5. Nonogram
6. Water Sort
7. Royal Match
8. Chess
9. Threes
10. Flow Free
11. Pipe Mania
12. Baba Is You
13. Mini Metro
14. Balatro
15. Into the Breach
16. Dorfromantik
17. Peg Solitaire

The pool is coverage backlog, not a commitment or a novelty claim. The
operational analysis workflow lives only in
[`CONTRIBUTING.md`](../CONTRIBUTING.md).

## Immediate next task

Analyse Minesweeper next.

- Claim status: `Hypothesis`
- Evidence quality: `Limited`
- Confidence: `Medium`
- Reason: it introduces inaccessible latent state, information-revealing
  actions, deduction under uncertainty and an irreversible hazard, unlike both
  completed genomes.
- Model test: retest the `INF-001` boundary and distinguish randomness in setup
  from randomness during the decision loop without inventing information genes
  prematurely.

This is the highest-information next subject under current evidence. Reassess
after `GAME-0003`.
