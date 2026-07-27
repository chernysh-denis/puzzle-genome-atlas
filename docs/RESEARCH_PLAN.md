# Research Plan

The plan is adaptive. Coverage targets are not a fixed sequence.

## Phase 1 — Establish the baseline model

- [x] Define six provisional gene types.
- [x] Separate accepted genes from candidate vocabulary.
- [x] Add stable IDs for genes, games and combinations.
- [x] Complete `GAME-0001` — 2048.
- [x] Record `COMB-0001` as the baseline combination.
- [ ] Test the model against a mechanically distant second family.

## Phase 2 — Build a diverse reference corpus

Coverage pool:

1. Rubik's Cube
2. Minesweeper
3. Tetris
4. FreeCell
5. Sudoku
6. Sokoban
7. Nonogram
8. Water Sort
9. Royal Match
10. Chess
11. Threes
12. Flow Free
13. Pipe Mania
14. Baba Is You
15. Mini Metro
16. Balatro
17. Into the Breach
18. Dorfromantik
19. Peg Solitaire

For every new game:

1. create a complete source-backed decomposition;
2. encode its genome with stable IDs;
3. scan the complete game and combination indexes;
4. record every exact structural match;
5. compare the nearest structural neighbours in detail;
6. add or revise genes only through the registry rules;
7. update verified combinations and research leads;
8. report negative results explicitly;
9. audit the next subject for expected information gain.

## Phase 3 — Normalise the registry

- Define and evidence candidate terms before promotion.
- Merge synonyms without reusing stable IDs.
- Test the boundaries between gene parameters and distinct genes.
- Test whether the six-type model survives multiple puzzle families.
- Record every classification change under `research/taxonomy-changes/`.

## Phase 4 — Map combinations

- Keep verified structures under `knowledge/combinations/`.
- Keep unsupported possibilities under `research/combination-leads/`.
- Attach evidence, confidence and analysed examples to each verified record.
- Identify sparse regions without calling them novel.

## Phase 5 — Gap and novelty research

- Search commercial, historical, academic, mechanical and experimental
  sources.
- Publish counterexamples and rejected novelty claims.
- Advance only combinations whose decision structure remains distinct.
- Do not prototype before a dedicated novelty review.

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

Plan status: `optimal under current evidence`. Reassess after `GAME-0002`.
