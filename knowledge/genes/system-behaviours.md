# System Behaviour Genes

## SYS-001 — Directional line compression

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: after a direction is chosen, movable elements automatically
  travel as far as permitted along parallel lines.
- Includes: deterministic maximal translation to a boundary or blocker.
- Excludes: the player's directional choice; gravity acting without a
  direction selected each turn.
- Evidence: [2048 decomposition](../games/0-9/2048.md).
- Novelty: not assessed; this is part of the baseline genome.

## SYS-002 — Collision-triggered compatible merge

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: compatible elements that collide during automatic resolution are
  replaced by one transformed element.
- Includes: equality-based numeric doubling in 2048.
- Excludes: a player directly selecting two objects to combine.
- Parameters: compatibility relation, output transform, resolution order.
- Evidence: [2048 decomposition](../games/0-9/2048.md).
- Novelty: not assessed; this is part of the baseline genome.

## SYS-003 — Element spawn after valid action

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: a new element is inserted after an action changes the state.
- Includes: the post-move tile insertion in 2048.
- Excludes: initial setup; deterministic refill; spawn after an invalid input.
- Parameters: trigger, element type and available positions.
- Evidence: [2048 decomposition](../games/0-9/2048.md).
- Novelty: not assessed; this is part of the baseline genome.

## SYS-004 — Random outcome selection

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: the system selects an outcome from more than one possible result
  according to a probability process.
- Includes: selecting the spawned tile's value and empty position in 2048.
- Excludes: hidden but predetermined outcomes; player-selected uncertainty.
- Parameters: outcome set and probability distribution.
- Evidence: [2048 decomposition](../games/0-9/2048.md).
- Novelty: not assessed; this is part of the baseline genome.

## SYS-005 — Zero-clue region expansion

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: revealing a safe position with zero adjacent hazards
  automatically reveals its connected zero-valued region and the region's
  numbered boundary before the next player input.
- Includes: classic Minesweeper blank-area expansion.
- Excludes: the player's initially selected reveal; a player-commanded chord;
  random placement of hazards during setup.
- Parameters: neighbourhood topology, connectivity and expansion stopping rule.
- Evidence: [Minesweeper decomposition](../games/m-r/minesweeper.md).
- Novelty: not assessed.
