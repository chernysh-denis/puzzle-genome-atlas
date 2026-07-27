# Gene Registry

A **gene** is the smallest decision-relevant mechanical component that the
knowledge base can currently distinguish and reuse across puzzle analyses.

A word is not a gene merely because it sounds mechanical. Every active gene
requires:

1. a stable type-specific ID;
2. a canonical name;
3. an operational definition;
4. inclusion and exclusion boundaries;
5. evidence and at least one analysed example;
6. lifecycle, claim-status, evidence-quality and confidence fields.

## Gene types

| Prefix | Type | Question answered |
|---|---|---|
| `ACT` | Action Gene | What does the player directly command? |
| `SYS` | System Behaviour Gene | What state transition resolves automatically? |
| `CON` | Constraint Gene | What limits legal or useful action? |
| `INF` | Information Gene | What can the player know, and when? |
| `OBJ` | Objective Gene | What state or measurement is pursued? |
| `TIM` | Time Gene | How are actions and resolution scheduled? |

These six types are the current model, not a protected truth. A seventh type may
be proposed only when repeated evidence cannot be represented without systematic
distortion. Use the taxonomy-change process; do not create an ad hoc category in
a game file.

## Registries

- [Action Genes](actions.md)
- [System Behaviour Genes](system-behaviours.md)
- [Constraint Genes](constraints.md)
- [Information Genes](information.md)
- [Objective Genes](objectives.md)
- [Time Genes](time.md)
- [Candidate terms inherited from the original taxonomy](CANDIDATE_TERMS.md)

## Lifecycle

- `Candidate` — vocabulary awaiting definition or evidence; not a gene yet.
- `Active` — accepted for genome encoding.
- `Deprecated` — retained for compatibility but replaced.
- `Merged` — found to be synonymous with another gene.
- `Split` — found to contain multiple decision-relevant genes.

Lifecycle is separate from claim status. `Active` means usable in the registry;
it does not mean novel or universally valid.
