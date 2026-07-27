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

Read the full [gene admission rules](knowledge/genes/README.md).

## How knowledge is added

```text
Source-backed observations
          ↓
Full game decomposition
          ↓
Typed genome with stable gene IDs
          ↓
Full-corpus signature scan
          ↓
Verified combination or research lead
          ↓
Novelty research, only when justified
```

Every new game is checked against the complete indexed corpus. Exact matches
are recorded centrally; only the nearest decision-relevant neighbours receive
long prose comparisons. This avoids duplicating hundreds of pairwise tables as
the corpus grows.

## Evidence model

Claim status and evidence strength are separate.

### Claim status

- `Observation` — a directly recorded fact.
- `Hypothesis` — a falsifiable proposed explanation or prediction.
- `Pattern` — a recurring relationship supported by multiple observations.
- `Strong Pattern` — a pattern reproduced across mechanically distinct
  families with counterexamples actively checked.
- `Confirmed` — a bounded claim independently verified within its stated scope.

### Evidence quality

- `Direct`
- `Corroborated`
- `Limited`
- `Conflicting`

Each claim also receives `Low`, `Medium` or `High` confidence. The project does
not use `Law`; no current evidence justifies universal mechanical laws.

See [Evidence Model](docs/EVIDENCE_MODEL.md) for promotion and downgrade rules.

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
[architecture document](docs/ARCHITECTURE.md) explains how this remains usable
at 100, 500 and 1000 game analyses.

## Analyse a new game

1. Read the [mission](docs/MISSION.md),
   [research principles](docs/RESEARCH_PRINCIPLES.md) and
   [evidence model](docs/EVIDENCE_MODEL.md).
2. Check the [game index](knowledge/games/INDEX.md), gene registries and
   combination index.
3. Choose a game that adds mechanical diversity rather than a near-duplicate of
   the most recent subject.
4. Copy the [game-analysis template](templates/GAME_ANALYSIS_TEMPLATE.md).
5. Prefer original rules, source code, direct play and primary historical
   records.
6. Encode the genome with existing IDs; propose new genes only with boundaries
   and evidence.
7. Scan the full corpus for exact matches and document the closest neighbours.
8. Update indexes, combinations, taxonomy proposals and the public research
   log.

The current completed corpus begins with
[`GAME-0001` — 2048](knowledge/games/0-9/2048.md). Rubik's Cube is next because
it provides a high-distance test of reversible permutation, orientation and
reachability.

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
- Active genes: baseline genes evidenced by `GAME-0001`
- Verified combinations: `COMB-0001`
- Novelty claims: none
- Prototyping: not started

See the adaptive [research plan](docs/RESEARCH_PLAN.md) and
[v1 roadmap](ROADMAP.md).

## Public scope

Only structured research is versioned. Personal notes, local logs, credentials,
raw idea dumps and unfinished scratch work remain excluded.

Puzzle Genome Atlas is available under the [MIT License](LICENSE). Participation
is governed by the [Code of Conduct](CODE_OF_CONDUCT.md).
