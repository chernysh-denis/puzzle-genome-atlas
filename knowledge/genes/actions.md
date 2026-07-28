# Action Genes

## ACT-001 — Global directional slide

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the player selects a direction and attempts to translate every
  movable element along that direction.
- Includes: one input globally coupled across multiple rows or columns.
- Excludes: selecting one element and moving it independently; automatic
  compression after the direction has been chosen.
- Parameters: direction set, affected topology, movement distance.
- Evidence: [2048 decomposition](../games/0-9/2048.md).
- Novelty: not assessed; this is part of the baseline genome.

## ACT-002 — Direct layer rotation

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the player directly selects a coupled layer of elements and
  rotates that layer as one rigid action.
- Includes: an outer face-layer turn of a standard 3 × 3 Rubik's Cube.
- Excludes: rotating the whole object only to change viewpoint; rotating one
  element independently; an automatic rotation caused by another action.
- Parameters: available axes, selectable layers, permitted turn angles and move
  metric.
- Evidence: [Rubik's Cube decomposition](../games/m-r/rubiks-cube.md).
- Novelty: not assessed.

## ACT-003 — Select concealed cell for reveal

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the player selects one concealed position and commands its fixed
  underlying content to be exposed.
- Includes: uncovering one covered Minesweeper cell.
- Excludes: automatically exposed neighbouring cells; selecting already visible
  information; generating new random content after the selection.
- Parameters: input method, target geometry and first-selection protection.
- Evidence: [Minesweeper decomposition](../games/m-r/minesweeper.md).
- Novelty: not assessed.

## ACT-004 — Toggle protective hypothesis marker

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the player marks or unmarks a concealed position as a suspected
  hazard without verifying its content, and the marker blocks ordinary reveal
  while present.
- Includes: flagging and unflagging a covered Minesweeper cell.
- Excludes: a system-confirmed hazard; a cosmetic note with no input effect;
  automatically revealing unmarked neighbours.
- Parameters: marker cycle, question-mark state, reveal protection and whether
  markers enable a bulk-reveal command.
- Evidence: [Minesweeper decomposition](../games/m-r/minesweeper.md).
- Novelty: not assessed.
