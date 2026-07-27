# Game Index

The index is the corpus-wide lookup table. Its complete signatures are derived
from game front matter and use the
[canonical comparison rules](../../docs/ARCHITECTURE.md#genome-signature).
Detailed prose belongs only in the relevant game analyses.

| ID | Game | Genome signature `(ACT; SYS; CON; INF; OBJ; TIM)` | Family | Analysis status | Primary combination | Reviewed |
|---|---|---|---|---|---|---|
| `GAME-0001` | [2048](0-9/2048.md) | `ACT-001; SYS-001,SYS-002,SYS-003,SYS-004; CON-001,CON-002,CON-003; INF-001,INF-002; OBJ-001,OBJ-002,OBJ-003; TIM-001` | Slide-and-merge | `reviewed` | [`COMB-0001`](../combinations/COMB-0001.md) | 2026-07-27 |

## Stable path shards

New files use a lower-case slug and one non-semantic shard:

- `0-9/`
- `a-f/`
- `g-l/`
- `m-r/`
- `s-z/`

Shards prevent a 1000-file directory without coupling paths to a taxonomy that
may later change.
