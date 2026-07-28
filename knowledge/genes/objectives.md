# Objective Genes

## OBJ-001 — Reach target value

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: produce an element whose value meets a declared threshold.
- Includes: creating the 2048 tile in the original 2048 ruleset.
- Excludes: maximising an unbounded score without a target-state threshold.
- Parameters: target value.
- Evidence: [2048 decomposition](../games/0-9/2048.md).
- Novelty: not assessed; this is part of the baseline genome.

## OBJ-002 — Maximise accumulated score

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: increase an unbounded or session-bounded numerical evaluation.
- Includes: increasing 2048's accumulated merge score.
- Excludes: reaching one fixed threshold as the only objective.
- Evidence: [2048 decomposition](../games/0-9/2048.md).
- Novelty: not assessed; this is part of the baseline genome.

## OBJ-003 — Preserve move availability

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: avoid a state in which no legal state-changing action remains.
- Includes: survival as an implicit continuing objective.
- Excludes: maximising score independently of terminal mobility.
- Evidence: [2048 decomposition](../games/0-9/2048.md).
- Novelty: not assessed; this is part of the baseline genome.

## OBJ-004 — Reconstruct specified configuration

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: transform the existing components into a declared target
  arrangement.
- Includes: restoring a Rubik's Cube so that each face has one colour relative
  to its fixed centres.
- Excludes: reaching a scalar value; maximising score; merely keeping another
  action available.
- Parameters: target equivalence, permitted whole-object orientations and
  alignment tolerance.
- Evidence: [Rubik's Cube decomposition](../games/m-r/rubiks-cube.md).
- Novelty: not assessed.

## OBJ-005 — Reveal every non-hazard position

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: expose every safe position while leaving all hazardous positions
  unexposed.
- Includes: completing a classic Minesweeper board without detonating a mine.
- Excludes: merely placing markers on every suspected hazard; clearing all
  pieces from a board; maximising score without completing the safe set.
- Parameters: whether correct markers are also required and the number of safe
  positions.
- Evidence: [Minesweeper decomposition](../games/m-r/minesweeper.md).
- Novelty: not assessed.
