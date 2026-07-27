# Time Genes

## TIM-001 — Discrete turn with automatic resolution

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: the player supplies one discrete input, after which the system
  completes all resulting state changes before accepting the next input.
- Includes: one 2048 direction followed by movement, merges, scoring and spawn.
- Excludes: real-time input and simultaneous unresolved planning.
- Evidence: [2048 decomposition](../games/0-9/2048.md).
- Novelty: not assessed; this is part of the baseline genome.

## TIM-002 — Self-paced sequential action

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the player may pause between discrete actions, and each completed
  action changes state without a time-driven system step.
- Includes: an untimed physical Rubik's Cube solve.
- Excludes: competition timing as an external scoring condition; automatic
  post-action resolution; continuous real-time state change.
- Parameters: action granularity and any externally imposed solve timer.
- Evidence: [Rubik's Cube decomposition](../games/m-r/rubiks-cube.md).
- Novelty: not assessed.
