# Constraint Genes

## CON-001 — Fixed occupancy capacity

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the playable state has a fixed finite number of occupancy
  positions.
- Includes: the 16 cells of the standard 2048 board; the fixed corner and edge
  positions of the standard 3 × 3 Rubik's Cube; the fixed cells of a
  Minesweeper board.
- Excludes: a move limit or timer; a board that expands during play.
- Parameters: capacity and topology.
- Evidence: [2048 decomposition](../games/0-9/2048.md) and
  [Rubik's Cube decomposition](../games/m-r/rubiks-cube.md), and
  [Minesweeper decomposition](../games/m-r/minesweeper.md).
- Novelty: not assessed.

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

## CON-004 — Invariant-constrained reachability

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: legal actions preserve global invariants, so only a proper subset
  of otherwise representable component arrangements is reachable.
- Includes: Rubik's Cube parity agreement, total corner-twist and total
  edge-flip constraints.
- Excludes: capacity alone; a local collision rule; a target that is difficult
  but not structurally unreachable.
- Parameters: component classes, permutation representation, orientation
  coordinates and invariant equations.
- Evidence: [Rubik's Cube decomposition](../games/m-r/rubiks-cube.md).
- Novelty: not assessed.

## CON-005 — Primitive action reversibility

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: every primitive legal state-changing action has a legal inverse
  that restores the immediately preceding state without a random or irreversible
  side effect.
- Includes: a Rubik's Cube face turn followed by the opposite turn.
- Excludes: undo supplied as an interface convenience; a move followed by an
  automatic random spawn; recoverability only through a restart.
- Parameters: inverse notation and primitive-action granularity.
- Evidence: [Rubik's Cube decomposition](../games/m-r/rubiks-cube.md).
- Novelty: not assessed.

## CON-006 — Terminal hazard exposure

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: exposing any concealed hazard immediately ends the current
  attempt before the completion objective is met.
- Includes: detonating a mine by revealing its Minesweeper cell.
- Excludes: an incorrect marker by itself; a recoverable damage or lives system;
  random setup that does not expose a hazard.
- Parameters: hazard count, any first-action safety exception and terminal
  feedback.
- Evidence: [Minesweeper decomposition](../games/m-r/minesweeper.md).
- Novelty: not assessed.
