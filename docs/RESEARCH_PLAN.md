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

1. FreeCell
2. Sudoku
3. Sokoban
4. Nonogram
5. Water Sort
6. Royal Match
7. Chess
8. Threes
9. Flow Free
10. Pipe Mania
11. Baba Is You
12. Mini Metro
13. Balatro
14. Into the Breach
15. Dorfromantik
16. Peg Solitaire

The pool is coverage backlog, not a commitment or a novelty claim. The
operational analysis workflow lives only in
[`CONTRIBUTING.md`](../CONTRIBUTING.md).

## Immediate next task

Analyse Tetris next.

- Claim status: `Hypothesis`
- Evidence quality: `Limited`
- Confidence: `Medium`
- Reason: it introduces continuous forced gravity, real-time input, locking,
  line clearing and terminal stack pressure, unlike all completed genomes.
- Model test: determine whether player-controlled transformation during
  automatic time-driven motion separates cleanly into Action, System Behaviour,
  Constraint and Time genes.

This is the highest-information next subject under current evidence. Reassess
after `GAME-0004`.
