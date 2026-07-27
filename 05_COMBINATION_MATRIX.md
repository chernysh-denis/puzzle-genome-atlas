# Combination Matrix

Each candidate is recorded as:

`Action + System behaviour + Constraint -> known examples / uncertainty`

## Genome comparison protocol

A game's **mechanical genome** is its normalised set of:

- player-action genes;
- automatic-system-behaviour genes;
- constraint genes;
- information-model genes;
- time-model genes;
- objective/evaluation genes.

The **core structural combination** used for match classification is:

`Player action + automatic system behaviour + constraint + information model`

After every game analysis:

1. Compare each normalised gene with the taxonomy and all earlier game decompositions.
2. Compare the core structural combination with every earlier game and this matrix.
3. Record one primary result:
   - `New gene` — at least one evidenced decision-relevant gene is absent from prior analysed games and the taxonomy. List it and explain the distinction.
   - `New combination of known genes` — every gene is already known, but the core combination is not present in an earlier analysed game.
   - `Full structural match` — the core combination already exists; differences are theme, interface, content or parameter tuning rather than decision structure.
4. Always include an explicit `New genes: none` when applicable.

Classification precedence is `New gene` → `New combination of known genes` → `Full structural match`. A synonym, reskin or changed number is not a new gene. An apparent new gene remains `Unverified` until supported by direct mechanics evidence and checked against the existing corpus.

The first completed game is recorded as `Baseline`; an empty comparison set is not evidence of novelty. All subsequent games must use one of the three classifications above.

| Action | System behaviour | Constraint | Example | Status |
|---|---|---|---|---|
| Global directional slide | Ordered collision/merge + random spawn after valid move | 16-cell board space / no spawn preview | 2048 | Established |
| Rotate + move | Gravity | Rising stack / space | Tetris | Established |
| Pour | Layered capacity | Empty buffers | Water Sort | Established |
| Swap | Cascade + refill | Limited moves | Match-3 | Established |
| Move / stack | Reveal hidden cards | Access order / buffers | Solitaire / FreeCell | Established |
| Place values | Constraint propagation | Uniqueness | Sudoku | Established |
| Move pieces | Opponent response | Territory / material / tempo | Chess | Established |
| Connect | Flow | Limited pieces / geometry | Pipe puzzles | Established |
| Place | Growth after placement | Limited space | Needs research | Unverified |
| Split | Delayed transformation | Limited buffers | Needs research | Unverified |
| Compress | Pressure redistribution | Limited capacity | Needs research | Unverified |
| Sort | Ageing per turn | Limited buffers | Needs research | Unverified |
| Redirect | Simultaneous propagation | Synchronisation | Needs research | Unverified |
| Fold | Gravity / collision | Limited geometry | Needs research | Unverified |
| Merge | Decay over turns | Limited space | Needs research | Unverified |

## Status values

- Established
- Known but niche
- Possible overlap
- Unverified
- Apparently empty
- Rejected
- Candidate for prototype

An apparently empty cell may only receive that status after explicit novelty research.
