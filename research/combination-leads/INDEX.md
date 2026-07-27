# Combination Research Leads

This file preserves the original matrix backlog without treating unanalysed
games or empty-looking cells as canonical knowledge.

- Claim status: `Hypothesis`
- Evidence quality: `Limited`
- Confidence: `Low`

The verified 2048 structure has moved to
[`COMB-0001`](../../knowledge/combinations/COMB-0001.md).

## Known-example leads awaiting full decomposition

| Provisional action | Provisional behaviour | Provisional constraint | Example to analyse |
|---|---|---|---|
| Rotate + move | Gravity | Rising stack / space | Tetris |
| Pour | Layered capacity | Empty buffers | Water Sort |
| Swap | Cascade + refill | Limited moves | Match-3 |
| Move / stack | Reveal hidden cards | Access order / buffers | Solitaire / FreeCell |
| Place values | Constraint propagation | Uniqueness | Sudoku |
| Move pieces | Opponent response | Territory / material / tempo | Chess |
| Connect | Flow | Limited pieces / geometry | Pipe puzzles |

These examples are plausible observations, but their normalised genes and exact
combination boundaries remain unverified until full analyses are complete.

## Sparse-combination leads

| Provisional action | Provisional behaviour | Provisional constraint |
|---|---|---|
| Place | Growth after placement | Limited space |
| Split | Delayed transformation | Limited buffers |
| Compress | Pressure redistribution | Limited capacity |
| Sort | Ageing per turn | Limited buffers |
| Redirect | Simultaneous propagation | Synchronisation |
| Fold | Gravity / collision | Limited geometry |
| Merge | Decay over turns | Limited space |

These rows are search prompts, not evidence that a combination is absent,
novel, coherent or enjoyable.

## Promotion rule

A lead moves to `knowledge/combinations/` only after:

1. its genes have active IDs;
2. at least one full game analysis supports it;
3. its decision boundary is documented;
4. exact and near matches have been searched;
5. evidence status and confidence are explicit.
