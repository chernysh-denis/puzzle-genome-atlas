# Information Genes

## INF-001 — Fully visible current state

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: every decision-relevant element of the current board is visible
  before the player acts.
- Includes: the complete tile layout and values on the standard 2048 board; all
  Rubik's Cube stickers, inspectable by changing viewpoint before a move.
- Excludes: knowledge of future random events.
- Parameters: simultaneous display versus sequential inspection.
- Evidence: [2048 decomposition](../games/0-9/2048.md) and
  [Rubik's Cube decomposition](../games/m-r/rubiks-cube.md).
- Novelty: not assessed.

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

## INF-003 — Fixed concealed current state

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: decision-relevant contents already exist in the current state but
  remain inaccessible until an information-revealing action occurs.
- Includes: fixed mine locations under covered Minesweeper cells.
- Excludes: a future random event not yet selected; an inspectable element that
  is merely offscreen; information the player once saw and forgot.
- Parameters: setup distribution, known global content count, first-action
  conditioning and reveal permanence.
- Evidence: [Minesweeper decomposition](../games/m-r/minesweeper.md).
- Novelty: not assessed.

## INF-004 — Exact local aggregate clue

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: a revealed safe position reports the exact aggregate count of
  concealed hazards in its fixed local neighbourhood.
- Includes: Minesweeper clues from 0 through 8 on a square grid.
- Excludes: approximate hints; the global remaining-hazard count alone; direct
  identification of which neighbouring position is hazardous.
- Parameters: neighbourhood topology, clue range and display convention.
- Evidence: [Minesweeper decomposition](../games/m-r/minesweeper.md).
- Novelty: not assessed.
