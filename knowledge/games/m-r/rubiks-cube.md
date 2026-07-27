---
game_id: GAME-0002
slug: rubiks-cube
game_title: "Rubik’s Cube"
analysis_status: reviewed
reviewed: 2026-07-28
combination_ids:
  - COMB-0002
gene_ids:
  action:
    - ACT-002
  system: []
  constraint:
    - CON-001
    - CON-004
    - CON-005
  information:
    - INF-001
  objective:
    - OBJ-004
  time:
    - TIM-002
---

# Game: Rubik's Cube

## Analysis scope

The unit is the standard untimed physical 3 × 3 Rubik's Cube: a legal scrambled
state must be restored by face-layer turns. Scrambling is setup, not an action
inside the solve. Speedcubing timers, blindfold rules, fewest-moves scoring,
picture-cube orientation and larger or smaller cubes are variants, not parts of
this genome.

Sections inherit status, evidence quality and confidence from the claim ledger.
Unlabelled statements are descriptive scope, source citations or deductions
whose inputs are explicitly identified.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `CUBE-001` | A solve directly turns face layers and ends with one colour per aligned face | Confirmed | Corroborated | High | P1, P2, P3, A1 |
| `CUBE-002` | A completed face turn has no automatic system-resolution step | Observation | Corroborated | High | P2, P3, A1 |
| `CUBE-003` | State separates corner/edge permutation from orientation and legal states obey three global invariants | Confirmed | Corroborated | High | A1, M1 |
| `CUBE-004` | Every primitive face turn has an exact legal inverse | Confirmed | Corroborated | High | P2, M1, M2 |
| `CUBE-005` | The reachable state space is about 4.3 × 10^19 and its face-turn-metric diameter is 20 | Confirmed | Corroborated | High | A1, A2 |
| `CUBE-006` | Common human methods use ordered algorithms that preserve previously solved substructures | Pattern | Corroborated | Medium | P1, A1 |
| `CUBE-007` | The current physical state is inspectable before action, with no hidden in-play random event | Observation | Corroborated | High | P1, P2, A1 |
| `CUBE-008` | The base puzzle is self-paced; competition timing is a separable variant rule | Observation | Corroborated | High | P1, P2, P3 |
| `CUBE-009` | Novices can acquire a multistep solution procedure, but broad cognitive claims require bounded samples | Observation | Direct | Medium | A4 |
| `CUBE-010` | The six-type Atlas model represents this unit without a taxonomy change | Observation | Corroborated | Medium | CUBE-001–CUBE-008 |

## Basic data

- Origin: Ernő Rubik made the first working cube in 1974 while investigating
  three-dimensional movement; the patented mechanism keeps the elements
  together while allowing layers to rotate.
- Platform: mechanical 3 × 3 × 3 twisty puzzle.
- Puzzle family: deterministic permutation-and-orientation reconstruction.
- Goal: restore the scrambled cube so that every aligned face has a single
  colour; whole-cube orientation does not change solvedness.
- Sources:
  - **[P1] Official solution material:** Rubik's,
    [3 × 3 solution guide](https://www.rubiks.com/solution-guides), including
    the cross, corners, middle layer and final-layer orientation/position steps.
  - **[P2] Official competition rules:** World Cube Association,
    [Regulations, Articles 10 and 12](https://www.worldcubeassociation.org/regulations/),
    for solved state, face-turn notation, inverses, half turns and cube
    rotations. Competition-only conditions are used to delimit variants.
  - **[P3] Primary mechanical description:** Ernő Rubik,
    [US Patent 4,378,116](https://patents.google.com/patent/US4378116A/en),
    filed from the Hungarian invention, describing coupled 3 × 3 layer
    rotations and reconstruction of a predetermined order.
  - **[H1] Historical/design account:** Smithsonian Magazine,
    ["A Brief History of the Rubik's Cube"](https://www.smithsonianmag.com/innovation/brief-history-rubiks-cube-180975911/),
    on Rubik's 1974 prototype and exploration of three-dimensional movement.
  - **[A1] Search and state representation:** Richard E. Korf,
    ["Finding Optimal Solutions to Rubik's Cube Using Pattern Databases"](https://cdn.aaai.org/AAAI/1997/AAAI97-109.pdf),
    AAAI 1997.
  - **[A2] Diameter:** Tomas Rokicki, Herbert Kociemba, Morley Davidson and
    John Dethridge,
    ["The Diameter of the Rubik's Cube Group Is Twenty"](https://doi.org/10.1137/120867366),
    *SIAM Journal on Discrete Mathematics* 27(2), 2013.
  - **[M1] Reachability theorem:** Jamie Mulholland,
    [Cubology notes and the Fundamental Theorem of Cubology](https://www.sfu.ca/~jtmulhol/math302/puzzles-rc-cubology.html),
    Simon Fraser University.
  - **[M2] Group formulation:** Alex Chuang,
    ["Group Theory and the Rubik's Cube"](https://math.uchicago.edu/~may/REU2021/REUPapers/Chuang%2CAlex.pdf),
    University of Chicago REU, 2021.
  - **[A3] Large-state single-goal solver study:** Forest Agostinelli et al.,
    ["Solving the Rubik's Cube with deep reinforcement learning and search"](https://doi.org/10.1038/s42256-019-0070-z),
    *Nature Machine Intelligence* 1, 2019.
  - **[A4] Human skill acquisition:** Elizabeth J. Meinz et al.,
    ["The Relationship between Intelligence and Complex Skill Acquisition"](https://doi.org/10.3390/jintelligence11010018),
    *Journal of Intelligence* 11(1), 2023.
- Claim IDs: `CUBE-001`, `CUBE-005`, `CUBE-008`, `CUBE-009`.

## Mechanical decomposition

### Action Genes

- `ACT-002` — direct layer rotation.
- The player chooses one outer layer and turns it by 90° clockwise, 90°
  counter-clockwise or 180°. Standard notation names the six outer faces
  `F`, `B`, `R`, `L`, `U` and `D`; a prime denotes the inverse quarter turn.
- The action is coupled: one input changes the positions and/or orientations of
  several edge and corner cubies together.
- A whole-cube `x`, `y` or `z` rotation changes viewpoint/reference frame, not
  puzzle state under the WCA definition, so it is not another state-changing
  Action Gene.

Parameters: 3 × 3 size, six selectable outer layers, permitted turn angles,
notation and chosen move metric. `Permutation`, `orientation`, `cubie` and
`algorithm` describe state or composed actions; none is an additional gene.

Claim IDs: `CUBE-001`, `CUBE-004`.

### System Behaviour Genes

- None.
- The core mechanism physically constrains a directly commanded layer turn but
  does not autonomously move, spawn, merge, randomise or resolve state after the
  player completes that turn.
- A scrambling procedure changes the initial condition before the analysed
  solve. Treating scramble generation as in-play system behaviour would mix
  setup with the decision loop.

Claim IDs: `CUBE-002`.

### Constraint Genes

- `CON-001` — fixed occupancy capacity. The movable state has 8 corner cubies
  and 12 edge cubies in fixed classes of positions; the 6 centres supply a
  reference frame.
- `CON-004` — invariant-constrained reachability. A representable arrangement
  is reachable by legal turns only when corner and edge permutation parities
  agree, total corner orientation is 0 modulo 3, and total edge orientation is
  0 modulo 2.
- `CON-005` — primitive action reversibility. Every face turn has an allowed
  inverse, and a half turn is self-inverse.
- Physical piece type is preserved: legal turns do not put an edge into a
  corner position or vice versa.

Parameters: corner/edge counts, position graph, permutation coordinates,
orientation coordinates and the three invariant equations. These values
instantiate `CON-004`; splitting each coordinate or equation into a gene would
mistake a mathematical representation for an independently reusable mechanic.

Claim IDs: `CUBE-003`, `CUBE-004`.

### Information Genes

- `INF-001` — fully visible current state.
- All decision-relevant stickers can be inspected before a move by changing the
  cube's viewpoint. They are not necessarily visible simultaneously; that is a
  visibility parameter, not hidden state.
- Once a current state and face turn are fixed, the next state is deterministic.
  There is no preview queue because there is no in-play random future event.

Parameters: sequential inspection rather than simultaneous display, physical
viewpoint and optional notation/recording aids. Blindfold solving is excluded
because it deliberately changes the information condition.

Claim IDs: `CUBE-007`.

### Objective Genes

- `OBJ-004` — reconstruct specified configuration.
- The target is an equivalence class under whole-cube orientation: every face
  is a single colour and the physical parts are aligned. It is not a scalar
  threshold or an instruction to maximise score.
- The untimed base puzzle has no terminal loss state. A poor move can increase
  remaining distance, but another legal sequence can always undo it.

Parameters: colour scheme, target equivalence under whole-cube rotation and
physical alignment tolerance.

Claim IDs: `CUBE-001`, `CUBE-004`.

### Time Genes

- `TIM-002` — self-paced sequential action.
- Face turns are discrete and ordered. State does not advance while the player
  waits, and no automatic system phase follows a completed turn.
- WCA inspection limits and solve timers are competition-layer parameters or
  variant rules, not properties of the base unit.

Parameters: primitive move granularity and an optional external timer.

Claim IDs: `CUBE-008`.

## Reproducible transitions

The following checks use standard face-turn notation and hold from every legal
starting state `s`:

| Test | Transition | Expected result | Boundary demonstrated |
|---|---|---|---|
| Exact inverse | `s → R → R'` | returns to `s` | `CON-005` |
| Quarter-turn order | `s → R → R → R → R` | returns to `s` | finite action parameter |
| Non-commutation | solved `→ R U` versus solved `→ U R` | different states | ordered composition matters |
| Single corner twist | disassemble, twist one corner, reassemble | no legal face-turn sequence solves it | `CON-004`, corner sum |
| Single edge flip | disassemble, flip one edge, reassemble | no legal face-turn sequence solves it | `CON-004`, edge sum |
| Two-piece swap | disassemble, swap only two corners | no legal face-turn sequence solves it | `CON-004`, parity |

The last three are mathematical boundary cases, not legal scrambles. They show
why fixed occupancy alone cannot explain the reachable state space.

Claim IDs: `CUBE-003`, `CUBE-004`.

## Strategic and experiential structure

- A face turn is locally simple but globally coupled: it typically moves eight
  movable cubies, so improving one substructure can disrupt another.
- The official beginner method decomposes the solve into cross, first-layer
  corners, middle-layer edges, and final-layer orientation and permutation.
  Korf similarly describes conventional methods as sequences of
  macro-operators that place cubies without destroying previously solved ones.
- The scarce strategic asset is preserved solved structure, not board capacity
  or time. Algorithms, commutators and conjugate-like setup/restore sequences
  control collateral change.
- Exact reversibility prevents irreversible mechanical failure but does not
  make error attribution trivial. In a long memorised sequence, the present
  state is visible while the location of an earlier execution error may not be.
- The sampled novice study supports learnability of a multistep procedure; it
  does not establish a universal intelligence requirement or one unique human
  solution structure.

Claim IDs: `CUBE-006`, `CUBE-009`.

## Replay and variation

- Different legal scrambles create different start states in a large but finite
  reachable space. After setup, identical move sequences from identical states
  are deterministic.
- Many solution paths reach the same target. Human methods optimise different
  costs: learnability, recognition burden, execution speed or move count.
- Under the face-turn metric, every legal position is at most 20 moves from
  solved. This optimal diameter does not imply that typical beginner solutions
  use at most 20 moves; the metric and solver objective must be stated.
- Replay in the base puzzle comes from new start states and improving procedure,
  not random in-play events, score accumulation or content progression.

Claim IDs: `CUBE-005`, `CUBE-006`.

## Adjacent systems and history

- The patent and historical account make the mechanical design central: the
  puzzle had to permit three-dimensional coupled motion while remaining one
  physical object.
- Officially supported 2 × 2, 4 × 4, Picture Cube and other variants alter
  dimensions, centres, target orientation or notation; they should receive
  separate units if analysed.
- Blindfolded solving changes observability. Speed solving and fewest-moves
  competition add time or move-evaluation objectives. None should be silently
  folded into `GAME-0002`.
- The mathematical state is naturally a group action on cubie arrangements.
  That vocabulary explains invariants and inverses, but “group” is not itself a
  mechanic gene.

Claim IDs: `CUBE-001`, `CUBE-003`, `CUBE-004`, `CUBE-008`.

## Normalised genome

- Action: `ACT-002`
- System Behaviour: none
- Constraint: `CON-001`, `CON-004`, `CON-005`
- Information: `INF-001`
- Objective: `OBJ-004`
- Time: `TIM-002`

Canonical signature:

`ACT-002; ; CON-001,CON-004,CON-005; INF-001; OBJ-004; TIM-002`

The empty System Behaviour component is intentional. The signature records a
complete classification across all six types; completeness does not require at
least one gene in every set.

## Corpus comparison

Corpus scanned: all other reviewed games in the index (`GAME-0001`) and all
previously registered combinations (`COMB-0001`).

- Exact matches: none. Equality fails in Action, System Behaviour, Constraint,
  Information, Objective and Time sets.
- Shared genes with `GAME-0001`: `CON-001`, `INF-001`.
- Rubik's Cube-only genes: `ACT-002`, `CON-004`, `CON-005`, `OBJ-004`,
  `TIM-002`.
- 2048-only genes: `ACT-001`, `SYS-001`–`SYS-004`, `CON-002`, `CON-003`,
  `INF-002`, `OBJ-001`–`OBJ-003`, `TIM-001`.
- Flattened typed-pair intersection size: 2.
- Union size: 19.
- Structural Jaccard score: `2 / 19 = 0.105263`.
- Formal near matches: `GAME-0001`, because it is the only indexed non-exact
  comparison with a positive score and therefore attains the current maximum.
  The low score is reported explicitly; “near” is corpus-relative and does not
  claim perceptual similarity.
- Existing combination support: `COMB-0001` is not a subset of this genome.
- New verified combination: `COMB-0002`, whose five-gene set is a proper subset
  of this seven-gene genome.
- Classification: `New gene`.

Mechanically, 2048 has globally coupled agency followed by irreversible,
stochastic system resolution; Rubik's Cube has locally selected but coupled
direct transformations, exact inverses and no autonomous response. Both expose
the current state, but only 2048 hides a random future event. 2048 manages
capacity and survival under accumulating randomness; Rubik's Cube navigates a
deterministic reachability group toward one configuration through composed
algorithms.

## Taxonomy impact

- The six gene types are sufficient for this unit. No taxonomy-change proposal
  is warranted.
- `Permutation` and `orientation` are state coordinates and parameters of
  `CON-004`, not genes.
- `Algorithm` is a sequence of actions and a strategy object, not a gene.
- Primitive reversibility is `CON-005`, not an angle parameter of `ACT-002`,
  because it constrains the transition graph across every action and excludes
  otherwise similar inputs followed by irreversible system effects. Inverse
  notation and action granularity remain parameters.
- The physical mechanism constrains player action; it is not autonomous System
  Behaviour.
- `INF-001` accommodates sequential inspection because all state remains
  inspectable before action. This boundary should be retested on a genuinely
  hidden-information game; no definition is broadened here.
- Exact and near matching are mathematically executable. The one-game prior
  corpus exposes the intended limitation of relative near matching, not a
  contradiction.
- `COMB-0002` demonstrates that a meaningful combination can omit
  decision-relevant genes and remain a proper subset of the full genome.

Claim IDs: `CUBE-010`.

## Negative results

None. Rubik's Cube did not reject a prior concrete Atlas claim, and the planned
six-type model test succeeded. Under the negative-result rules, absence of a
taxonomy failure does not require a separate negative-result record.

## Delta summary

## Нові факти

- The base 3 × 3 puzzle is deterministic during play, fully inspectable,
  self-paced and exactly reversible.
- Its legal state space is restricted by permutation parity and orientation
  invariants; fixed piece count is insufficient to describe legality.
- The face-turn-metric diameter is 20, while common human solution procedures
  deliberately trade move optimality for learnable preserved subgoals.

## Нові гени

- `ACT-002` — direct layer rotation.
- `CON-004` — invariant-constrained reachability.
- `CON-005` — primitive action reversibility.
- `OBJ-004` — reconstruct specified configuration.
- `TIM-002` — self-paced sequential action.

No System Behaviour gene was added. The remaining relevant properties reuse
`CON-001` and `INF-001`.

## Нові комбінації

- `COMB-0002` — reversible layer rotation under reachability invariants:
  `ACT-002 + CON-004 + CON-005 + OBJ-004 + TIM-002`.

## Зміни таксономії

- None. New bounded genes extend the existing six registries without changing
  their types, ID scheme, signature or matching rules.

## Нові питання

- TODO: retest whether sequential physical inspection remains inside `INF-001`
  when `GAME-0003` introduces genuinely hidden state. It is deliberately
  deferred because Rubik's Cube has no inaccessible decision-relevant state and
  therefore supplies no failure case.
- TODO: seek a second independent game for `CON-004` and `COMB-0002` before
  making a cross-family reuse claim. One analysed game establishes boundaries,
  not prevalence or novelty.
- TODO: compare direct structural reversibility with interface-level undo in a
  future subject. They are excluded from one another here, but this game cannot
  demonstrate both sides empirically.

## Наступна рекомендована гра

`GAME-0003` — Minesweeper.

## Чому саме вона

Minesweeper has the highest expected information gain in the current pool
because it introduces inaccessible latent state, information-revealing actions,
deduction under uncertainty and an irreversible hazard. It directly retests
the `INF-001` boundary and separates randomness in setup from randomness during
play, while remaining mechanically distant from both 2048 and Rubik's Cube.
