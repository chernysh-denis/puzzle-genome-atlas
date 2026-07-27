# Constraint Genes

## CON-001 — Fixed occupancy capacity

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: the playable state has a fixed finite number of occupancy
  positions.
- Includes: the 16 cells of the standard 2048 board.
- Excludes: a move limit or timer; a board that expands during play.
- Parameters: capacity and topology.
- Evidence: [2048 decomposition](../games/0-9/2048.md).
- Novelty: not assessed; this is part of the baseline genome.

## CON-002 — Equality merge compatibility

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: only elements with equal current values may merge.
- Includes: `2 + 2`, `4 + 4` and the corresponding higher powers in 2048.
- Excludes: adjacency without merging; asymmetric compatibility rules.
- Evidence: [2048 decomposition](../games/0-9/2048.md).
- Novelty: not assessed; this is part of the baseline genome.

## CON-003 — Single merge participation per resolution

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: an element created by a merge cannot merge again during the same
  automatic resolution.
- Includes: `[2, 2, 2, 2]` resolving to `[4, 4]`, not `[8]`.
- Excludes: restrictions that apply across multiple turns.
- Evidence: [2048 decomposition](../games/0-9/2048.md).
- Novelty: not assessed; this is part of the baseline genome.
