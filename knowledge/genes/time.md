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
