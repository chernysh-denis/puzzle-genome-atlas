# Information Genes

## INF-001 — Fully visible current state

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: every decision-relevant element of the current board is visible
  before the player acts.
- Excludes: knowledge of future random events.
- Evidence: [2048 decomposition](../games/0-9/2048.md).
- Novelty: not assessed; this is part of the baseline genome.

## INF-002 — Unpreviewed random future event

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: the next random state change is not revealed before the action
  that triggers it.
- Includes: both the value and position of the next 2048 tile.
- Excludes: a preview queue or deterministic future state.
- Evidence: [2048 decomposition](../games/0-9/2048.md).
- Novelty: not assessed; this is part of the baseline genome.
