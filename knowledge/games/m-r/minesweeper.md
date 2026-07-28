---
game_id: GAME-0003
slug: minesweeper
game_title: Minesweeper
analysis_status: reviewed
reviewed: 2026-07-28
combination_ids:
  - COMB-0003
gene_ids:
  action:
    - ACT-003
    - ACT-004
  system:
    - SYS-005
  constraint:
    - CON-001
    - CON-006
  information:
    - INF-003
    - INF-004
  objective:
    - OBJ-005
  time:
    - TIM-001
---

# Game: Minesweeper

## Analysis scope

- Version / ruleset: an untimed classic rectangular Minesweeper round with a
  fixed minefield selected during setup, single-cell reveal, reversible flags,
  exact eight-neighbour clues and automatic expansion from zero clues.
- Included: the common deduction loop documented by Microsoft, GNOME and KDE
  and formalised in Minesweeper research.
- Excluded: Adventure and Daily Challenge modes, XP, achievements, paid
  features, high-score timing, auto-chording, guaranteed no-guess generation,
  first-click-safe relocation, lives, hints and non-square topologies.
- Direct-play status: not conducted. Rules were triangulated from official
  documentation, a contemporary Windows guide and academic formalisations.

The setup samples one of many possible fields, but the field is fixed before
the analysed decision loop. This scope decision is necessary because modern
implementations disagree about first-click safety and when generation occurs.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `MINE-001` | The player reveals covered cells and may mark suspected mines with reversible flags | Confirmed | Corroborated | High | P1–P4 |
| `MINE-002` | Within the scoped round, mine locations are fixed hidden current state rather than future random events | Confirmed | Corroborated | High | P2, P4, A3, A4 |
| `MINE-003` | A revealed safe cell gives the exact count of mines in its eight-cell neighbourhood | Confirmed | Corroborated | High | P2, P4, A1, A3 |
| `MINE-004` | Revealing a zero clue automatically expands its connected blank region and numbered boundary | Confirmed | Corroborated | High | P4, A3 |
| `MINE-005` | A flag is an unverified player hypothesis that protects its cell from ordinary reveal | Confirmed | Corroborated | High | P3, P4 |
| `MINE-006` | Revealing a mine ends the attempt; revealing every non-mine cell completes it | Confirmed | Corroborated | High | P1, P2, P4, A3 |
| `MINE-007` | Play alternates exact constraint deduction with probabilistic choice when several hidden assignments remain consistent | Pattern | Corroborated | Medium | P2, A2–A4 |
| `MINE-008` | Complexity results for generalised or offline formulations do not establish the difficulty of every fixed preset board | Confirmed | Corroborated | High | A1–A3 |
| `MINE-009` | Microsoft's version appeared in 1990 and became a standard Windows 3.1 inclusion in 1992 | Confirmed | Corroborated | High | H1–H3 |
| `MINE-010` | Human performance in a Minesweeper variant is affected by subproblem order and externalised intermediate results | Observation | Direct | Medium | A5 |
| `MINE-011` | The six-type Atlas model distinguishes setup randomness, fixed hidden state and reveal-time resolution without a taxonomy change | Observation | Corroborated | Medium | MINE-001–MINE-007 |

## Basic data

- Release / origin: Robert Donner and Curt Johnson wrote Microsoft's version,
  which appeared in the 1990 Microsoft Entertainment Pack and was bundled with
  Windows 3.1 in 1992. Earlier minefield games existed, but the reviewed
  evidence does not establish one uncontested direct design lineage.
- Platform or physical form: originally a mouse-controlled desktop grid;
  subsequently reproduced across operating systems and devices.
- Puzzle family: hidden-state spatial deduction with terminal hazards.
- Primary and official sources:
  - **[P1] Microsoft/Xbox:** [Microsoft Minesweeper](https://www.xbox.com/en-US/games/store/microsoft-minesweeper/9WZDNCRFHWCN),
    whose Classic Mode description states the clear-without-triggering goal and
    flag action. Modern metagame modes are outside scope.
  - **[P2] GNOME:** [Mines game rules](https://help.gnome.org/gnome-mines/rules.html),
    documenting covered cells, exact adjacent counts, mine failure and
    completion by uncovering every non-mine tile.
  - **[P3] GNOME:** [flag rules](https://help.gnome.org/gnome-mines/flags.html),
    documenting unverified flags, question flags and protection from reveal.
  - **[P4] KDE:** [KMines handbook](https://docs.kde.org/trunk_kf6/en/kmines/kmines/kmines.pdf),
    documenting reveal, flags, eight-cell adjacency, automatic blank expansion,
    mine failure and the mine counter.
- Historical sources:
  - **[H1]** Richard Cobbett,
    ["The most successful game ever: a history of Minesweeper"](https://www.techradar.com/news/gaming/the-most-successful-game-ever-a-history-of-minesweeper-596504),
    TechRadar, 2009.
  - **[H2]** Kris Jamsa,
    [*The Concise Guide to Microsoft Windows 3.1*](https://vtda.org/books/Computing/OperatingSystems/ConciseGuideWindows3.1_KrisJamsa.pdf),
    1992, contemporary documentation of reveal, clue and flag controls.
  - **[H3]** MobyGames,
    [*Minesweeper* release record](https://www.mobygames.com/game/4828/minesweeper/),
    recording the 1990 Microsoft release and Curt Johnson credit.
- Academic and mathematical sources:
  - **[A1]** Richard Kaye,
    ["Minesweeper is NP-complete"](https://doi.org/10.1007/BF03025367),
    *The Mathematical Intelligencer* 22(2), 2000.
  - **[A2]** Allan Scott, Ulrike Stege and Iris van Rooij,
    ["Minesweeper May Not Be NP-Complete but Is Hard Nonetheless"](https://doi.org/10.1007/s00283-011-9256-x),
    *The Mathematical Intelligencer* 33(4), 2011.
  - **[A3]** Michiel de Bondt,
    ["The computational complexity of Minesweeper"](https://arxiv.org/abs/1204.4659),
    2012.
  - **[A4]** Chain Tsuan Liu et al.,
    ["A solver of single-agent stochastic puzzle: A case study with Minesweeper"](https://doi.org/10.1016/j.knosys.2022.108630),
    *Knowledge-Based Systems* 246, 2022.
  - **[A5]** Samuel J. Cheyette et al.,
    ["Decompose, Deduce, and Dispose: A Memory-Limited Metacognitive Model of Human Problem Solving"](https://www.bramleylab.ppls.ed.ac.uk/publication/2025-01-01_cheyette2025decompose/),
    *Proceedings of the 47th Annual Meeting of the Cognitive Science Society*,
    2025.
- Claim IDs: `MINE-001`–`MINE-010`.

## Mechanical decomposition

### Action Genes

- Existing gene IDs: none.
- `ACT-003` — select concealed cell for reveal. The player chooses one covered
  cell whose fixed content will become visible.
- `ACT-004` — toggle protective hypothesis marker. A flag records a suspected
  mine, may be wrong, can be removed and prevents an ordinary reveal while
  present.
- Candidate genes: none. Chording is excluded from the scoped ruleset because
  it batches otherwise available reveals and varies across implementations.
- Parameters: pointer/touch input, rectangular target geometry, flag/question
  cycle and first-action safety policy.
- Claim IDs: `MINE-001`, `MINE-005`.

`ACT-004` is not merely a parameter of reveal: it is a separate reversible
command, changes which cells accept reveal input and externalises a hypothesis
without disclosing the underlying state.

### System Behaviour Genes

- `SYS-005` — zero-clue region expansion. A revealed safe cell with no adjacent
  mines triggers automatic reveal through its connected zero region and the
  numbered boundary around that region.
- Revealing the one selected cell is the commanded result of `ACT-003`, not a
  separate automatic behaviour. Only propagation beyond that target enters
  `SYS-005`.
- Random mine placement belongs to setup in this scope. The system does not
  resample or relocate hidden content after each decision.
- Resolution order: reveal selected cell; if it is a mine, terminate; if its
  clue is zero, complete recursive expansion; then accept the next input.
- Parameters: eight-neighbour topology, connected-region rule and expansion
  boundary.
- Claim IDs: `MINE-002`, `MINE-004`, `MINE-006`.

`SYS-004` does not apply. Randomness selected the current hidden field before
the loop; it is not a future outcome chosen after a player action.

### Constraint Genes

- `CON-001` — fixed occupancy capacity. Board dimensions define a finite,
  unchanging set of cells.
- `CON-006` — terminal hazard exposure. Revealing one mined cell immediately
  ends the attempt.
- The mine count and board topology constrain all consistent hidden
  assignments. They are parameters of this genome rather than independent
  genes.
- Scarce strategic resources: safe information-bearing frontier cells and the
  remaining tolerance for uncertainty. There is no recoverable life resource
  in the scoped round.
- Claim IDs: `MINE-002`, `MINE-003`, `MINE-006`, `MINE-007`.

### Information Genes

- `INF-003` — fixed concealed current state. Mine locations are already part of
  the current board but cannot be inspected directly.
- `INF-004` — exact local aggregate clue. Each revealed safe cell reports the
  number of mines among up to eight adjacent cells.
- `INF-001` is absent because decision-relevant mine locations remain
  inaccessible. `INF-002` is absent because no in-play future random event
  waits to be selected.
- Parameters: known total mine count, mine-placement prior, neighbourhood,
  permanent reveal and any first-action conditioning.
- Claim IDs: `MINE-002`, `MINE-003`, `MINE-007`.

The displayed total mine count narrows the possible hidden assignments. It is
currently a parameter of `INF-003`; this game alone does not establish that
global-count knowledge is a reusable gene separate from fixed concealed state.

### Objective Genes

- `OBJ-005` — reveal every non-hazard position.
- Correct flags are useful but not sufficient: the core completion test is that
  every safe cell is exposed. No score or target value is part of this scoped
  objective.
- Success: all non-mine cells revealed.
- Evaluation: binary completion; optional time records are excluded.
- Failure: any mine revealed before completion.
- Claim IDs: `MINE-006`.

### Time Genes

- `TIM-001` — discrete turn with automatic resolution. The player supplies one
  reveal or marker input; any zero-region expansion finishes before the next
  input.
- The player may think indefinitely between actions. A continuously displayed
  completion timer evaluates speed but does not advance the minefield and is
  excluded from the untimed unit.
- Parameters: input granularity and optional external completion timer.
- Claim IDs: `MINE-004`, `MINE-006`.

## Reproducible transitions

These cases assume one fixed mine layout. `■` is covered, `⚑` is a player flag
and numbers are revealed clues.

| Before | Action | Deterministic resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Covered safe cell beside two mines | Reveal it | Show `2` | Exact local clue, not mine identity | `MINE-003` |
| Covered safe cell beside no mines | Reveal it | Reveal its zero region and numbered boundary | Automatic propagation | `MINE-004` |
| Covered mined cell | Reveal it | Expose mine and end attempt | Terminal hazard | `MINE-006` |
| Covered safe cell | Flag it, then attempt reveal | Marker appears; reveal is blocked | Marker is protective but unverified | `MINE-005` |
| Revealed `1` with one adjacent covered cell | Infer, then flag that cell | Under every consistent assignment it is a mine | Local exact deduction | `MINE-003` |
| Two symmetric covered cells constrained to contain one mine | Reveal either | One is safe and one is fatal, with no clue distinguishing them | Irreducible choice under current information | `MINE-007` |

An incorrect flag does not change any clue and does not itself lose the game.
It records a false hypothesis that can later cause an unsafe bulk or manual
reveal if the player reasons from it as though confirmed.

## Strategic and experiential structure

- Local decision: translate each visible number into an equality over adjacent
  hidden cells.
- Basic deterministic rules: if a clue's remaining mine count is zero, all
  other covered neighbours are safe; if it equals the number of remaining
  covered neighbours, all are mines.
- Medium-term planning: combine overlapping clue neighbourhoods, subtract
  subset constraints, flag forced mines and choose reveals that expose the most
  useful frontier.
- Long-term structure: decompose the visible frontier into coupled constraint
  components, use the known global mine count to relate frontier and
  non-frontier cells, and minimise risk when no forced move remains.
- Common heuristics: expand zero regions early, prefer certain reveals over
  guesses, avoid treating flags as system-confirmed facts, and compare complete
  consistent assignments rather than isolated clue ratios.
- Failure attribution: a logically unsafe reveal or incorrect assumed flag is
  often traceable. Attribution weakens when all remaining moves have non-zero
  hazard probability, because a loss can follow the best available choice.
- Player-trust factors: clues are exact and the hidden layout does not change
  after evidence is shown. Randomly relocating mines during the solve would
  break the deduction contract and is outside scope.
- Claim IDs: `MINE-003`, `MINE-005`, `MINE-007`, `MINE-010`.

The Cognitive Science study used a Minesweeper variant, not this exact
ruleset. It supports the bounded observation that subproblem ordering and
externalised intermediate results can matter; it does not justify a universal
claim about all Minesweeper players.

## Replay and variation

- What changes between sessions: the initial hidden mine arrangement.
- Randomness or procedural generation: a field is sampled at setup under fixed
  dimensions and mine count, then remains deterministic during the round.
- Multiple viable strategies: different safe frontiers may be explored first;
  when no forced reveal exists, probability models can choose different
  minimum-risk or maximum-information cells.
- Typical replay motive: solve a fresh field, improve deduction fluency or,
  in timed variants, reduce completion time.
- Solvability caveat: random classic boards can contain states in which several
  mine assignments remain consistent and no risk-free reveal exists. “No
  guessing” generators are a distinct variant.
- Claim IDs: `MINE-002`, `MINE-007`, `MINE-008`.

## Adjacent systems and history

- Direct predecessors: early minefield and grid-deduction games predate the
  Microsoft release, but the reviewed historical accounts conflict on direct
  lineage; no single predecessor is asserted here.
- Variants: first-click-safe generation, guaranteed-solvable/no-guess boards,
  chord and auto-chord controls, triangular or hexagonal neighbourhoods,
  competitive timers, lives, hints, multiplayer and Microsoft's Adventure
  mode.
- Similar games: Nonogram and Sudoku also expose constraints over hidden or
  unknown values, but their clue topology, action consequences and failure
  rules require separate decompositions.
- Important mathematical difference: Kaye's consistency construction and later
  complexity models are generalised decision problems. Scott, Stege and van
  Rooij refine what “playing Minesweeper” means, while de Bondt studies
  probabilistic play and other topologies. None proves that every standard
  beginner board is hard.
- Claim IDs: `MINE-008`, `MINE-009`.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-003`, `ACT-004` | input method, flag cycle, first-click policy |
| System Behaviour | `SYS-005` | neighbourhood and expansion stopping rule |
| Constraint | `CON-001`, `CON-006` | dimensions, mine count |
| Information | `INF-003`, `INF-004` | setup prior, known total, clue topology |
| Objective | `OBJ-005` | safe-cell completion rule |
| Time | `TIM-001` | optional external timer excluded |

Canonical signature:

`ACT-003,ACT-004; SYS-005; CON-001,CON-006; INF-003,INF-004; OBJ-005; TIM-001`

## Corpus comparison

- Indexed games scanned: `GAME-0001`, `GAME-0002`.
- Indexed combinations scanned: `COMB-0001`, `COMB-0002`.
- Exact genome matches: none.
- Shared with `GAME-0001`: `CON-001`, `TIM-001`.
- Structural similarity to `GAME-0001`: intersection `2`, union `21`,
  `2 / 21 = 0.095238`.
- Shared with `GAME-0002`: `CON-001`.
- Structural similarity to `GAME-0002`: intersection `1`, union `15`,
  `1 / 15 = 0.066667`.
- Near match: `GAME-0001`, the unique positive maximum among non-exact indexed
  games.
- Supported existing combination subsets: none. Neither `COMB-0001` nor
  `COMB-0002` is a subset of this genome.
- New combination: `COMB-0003`, whose six genes are a proper subset of this
  nine-gene genome.
- Scan date: 2026-07-28.

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0001` — 2048 | `CON-001`, `TIM-001` | 2048 shows current state and selects a new random outcome after each move; Minesweeper fixes hidden state at setup and reveals exact local evidence about it | Near, `0.095238` |
| `GAME-0002` — Rubik's Cube | `CON-001` | Rubik's Cube is fully inspectable and structurally reversible; Minesweeper is partially observable and one hazard reveal is terminal | Non-near, `0.066667` |

- New genes: `ACT-003`, `ACT-004`, `SYS-005`, `CON-006`, `INF-003`,
  `INF-004`, `OBJ-005`.
- Classification result: `New gene`.
- Evidence and reasoning: each new gene answers a distinct typed question,
  defines an exclusion boundary and cannot be represented by a value of an
  existing gene. Board dimensions, mine count, neighbourhood and setup policy
  remain parameters.

## Taxonomy impact

- Registry changes: seven bounded genes added; `CON-001` and `TIM-001` reused.
- Taxonomy-change record: none. The six types represent the complete scoped
  rules without distortion.
- Candidate terms affected: reveal, protective marking, propagation, hidden
  information, local clues and clear-safe-state now have bounded mappings.
- `INF-003` is the concrete exclusion case promised by `GAME-0002`: unlike
  sequential inspection of a cube, mine locations cannot be inspected before
  acting.
- Setup randomness and fixed concealed state remain distinct. `SYS-004` would
  misclassify a predetermined hidden mine as a future random outcome.
- The visible total mine count remains an `INF-003` parameter for now. A future
  game that changes decisions solely by revealing or hiding the total would be
  evidence to reconsider this boundary.
- First-click-safe generation is deliberately deferred. Implementations differ
  between pre-generated relocation and generation conditioned on the first
  click; a separate scoped variant is needed before deciding whether it adds
  `SYS-004`.
- Claim IDs: `MINE-011`.

## Negative results

None. Minesweeper confirms rather than rejects the prior `INF-001` boundary and
does not invalidate a concrete gene distinction, combination or novelty claim.
No separate negative-result record is required.

## Delta summary

## Нові факти

- [Confirmed | Corroborated | High] Minesweeper's in-play uncertainty concerns a
  fixed concealed state, not repeated random future events (`MINE-002`).
- [Confirmed | Corroborated | High] Exact local counts turn reveals into
  constraints over neighbouring hidden cells (`MINE-003`).
- [Pattern | Corroborated | Medium] Some consistent states require
  probabilistic choice after deterministic deductions are exhausted
  (`MINE-007`).

## Нові гени

- [Observation | Corroborated | High] `ACT-003`, `ACT-004`, `SYS-005`,
  `CON-006`, `INF-003`, `INF-004` and `OBJ-005`.
- [Observation | Corroborated | High] `CON-001` and `TIM-001` are reused.

## Нові комбінації

- [Confirmed | Corroborated | High] `COMB-0003` — safe-cell deduction from
  fixed hidden hazards and exact local counts.

## Зміни таксономії

- [Observation | Corroborated | Medium] Змін таксономії немає. Minesweeper
  supplies the first concrete hidden-current-state boundary without requiring a
  seventh gene type.

## Нові питання

- TODO: analyse a first-click-safe implementation as its own ruleset before
  classifying conditional setup generation. It is deferred because the classic
  sources do not specify one uniform policy.
- TODO: test known versus unknown global hazard count in another game before
  promoting it from an `INF-003` parameter. One subject cannot establish a
  reusable boundary.
- TODO: compare optional flags with a system where player annotations have no
  protective input effect. This is required to test the exclusion boundary of
  `ACT-004`.

## Наступна рекомендована гра

- [Hypothesis | Limited | Medium] `GAME-0004` — Tetris.
- Optimisation criterion: maximise expected structural distance and test the
  least-covered time/system interaction.
- Expected information gain: continuous forced gravity, real-time input,
  player-controlled transformation during automatic motion, locking, line
  clearing and terminal stack pressure.
- Backlog impact: Tetris moves from the coverage pool to the immediate task;
  displaced subjects retain their relative order.

## Чому саме вона

- [Hypothesis | Limited | Medium] Tetris is farther from the three completed
  decision loops than another static deduction puzzle. It directly tests
  whether automatic time-driven movement and player action can be separated
  without duplicating genes or treating speed as a parameter of turn-based
  play.
