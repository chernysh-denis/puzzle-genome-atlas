# Puzzle Genome Atlas

**Puzzle Genome Atlas is an open knowledge base for the fundamental,
reusable mechanics of puzzles.**

It is not a game catalogue, genre database or collection of ideas. It
decomposes puzzles into typed mechanical **genes**, records verified
combinations and investigates areas that may be underexplored.

## Why this exists

Genres and themes describe products, not decision structures. Two games can
look unrelated while using the same mechanical structure; two visually similar
games can ask the player to reason in fundamentally different ways.

Puzzle Genome Atlas asks:

1. What are the smallest reusable mechanical components of a puzzle?
2. Which combinations of those components already exist?
3. Which apparent gaps survive historical and external research?

The project maps before it invents. Prototypes begin only after the knowledge
base can support a defensible novelty investigation.

## The gene model

A gene is a bounded, evidence-backed unit of mechanics. It must have a stable
ID, operational definition, inclusion and exclusion boundaries, sources and an
analysed example.

| Type | Prefix | Meaning |
|---|---|---|
| Action Gene | `ACT` | What the player directly commands |
| System Behaviour Gene | `SYS` | What the system resolves automatically |
| Constraint Gene | `CON` | What limits legal or useful action |
| Information Gene | `INF` | What can be known, and when |
| Objective Gene | `OBJ` | What state or measurement is pursued |
| Time Gene | `TIM` | How actions and resolution are scheduled |

An attractive verb is not automatically a gene. Undefined vocabulary remains
a candidate term until evidence gives it a stable boundary. If the six-type
model proves inadequate, the project will propose a documented taxonomy change
instead of forcing evidence into the wrong category.

The terms **gene**, **parameter**, **genome**, **genome signature** and
**combination** have distinct canonical meanings. Exact and near matches are
defined mathematically, not by prose judgement.

Read the [canonical vocabulary and comparison
rules](docs/ARCHITECTURE.md#canonical-vocabulary) and the
[gene admission rules](knowledge/genes/README.md).

## How knowledge is added

```text
Source-backed observations
          ↓
Full game decomposition
          ↓
Typed genome with stable gene IDs
          ↓
Canonical full-corpus signature comparison
          ↓
Verified combination or research lead
          ↓
Novelty research, only when justified
```

Every new game is checked against the complete indexed corpus. Exact matches
are recorded centrally; only the mathematically selected near matches receive
long prose comparisons. This avoids duplicating pairwise tables as the corpus
grows.

## Evidence model

Every substantive claim separates three questions: what kind of claim it is,
how strong its evidence is and how likely it is to change. Gene lifecycle and
document workflow never replace claim assessment.

The [Evidence Model](docs/EVIDENCE_MODEL.md) is the single canonical definition
of statuses, evidence quality, confidence and promotion rules.

## Repository map

| Path | Purpose |
|---|---|
| [`docs/`](docs/ARCHITECTURE.md) | Mission, method, evidence model and research plan |
| [`knowledge/genes/`](knowledge/genes/README.md) | Canonical typed gene registry |
| [`knowledge/games/`](knowledge/games/INDEX.md) | Evidence-backed game genomes |
| [`knowledge/combinations/`](knowledge/combinations/INDEX.md) | Verified structural combinations |
| [`research/`](research/RESEARCH_LOG.md) | Leads, taxonomy proposals, candidates and negative results |
| [`templates/`](templates/GAME_ANALYSIS_TEMPLATE.md) | Required contribution formats |
| [`scripts/`](scripts/validate_repository.py) | Dependency-free integrity validation |

Canonical knowledge and open investigation are intentionally separate. The
[architecture document](docs/ARCHITECTURE.md) defines canonical records,
signatures and comparison rules.

## Analyse a new game

The operational workflow is maintained once in
[CONTRIBUTING.md](CONTRIBUTING.md). It points to the required template,
comparison formula, evidence rules and registries.

The current corpus contains
[`GAME-0001` — 2048](knowledge/games/0-9/2048.md) and
[`GAME-0002` — Rubik's Cube](knowledge/games/m-r/rubiks-cube.md). The adaptive
[research plan](docs/RESEARCH_PLAN.md) owns the next-subject decision.

## Add new knowledge

Contributions may add:

- a complete game decomposition;
- primary or historical evidence;
- a counterexample;
- a gene-boundary correction;
- a verified combination;
- a structured negative result.

Do not submit raw ideas, reskins or unsupported novelty claims. Start with
[CONTRIBUTING.md](CONTRIBUTING.md) and use the relevant template.

## Project status

- Stage: taxonomy and evidence collection
- Active genes: bounded genes evidenced by `GAME-0001` and `GAME-0002`
- Verified combinations: `COMB-0001`, `COMB-0002`
- Novelty claims: none
- Prototyping: not started

See the adaptive [research plan](docs/RESEARCH_PLAN.md) and
[v1 roadmap](ROADMAP.md).

## Public scope

Only structured research is versioned. Personal notes, local logs, credentials,
raw idea dumps and unfinished scratch work remain excluded.

Puzzle Genome Atlas is available under the [MIT License](LICENSE). Participation
is governed by the [Code of Conduct](CODE_OF_CONDUCT.md).
