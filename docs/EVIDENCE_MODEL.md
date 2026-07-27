# Evidence Model

Every substantive claim in Puzzle Genome Atlas must expose three independent
fields:

1. claim status;
2. evidence quality;
3. confidence.

The old single ladder mixed different questions. A hypothesis is a kind of
claim, while corroboration is a property of its evidence. Keeping them separate
prevents a sourced fact about one game from being mistaken for a cross-family
pattern.

## Claim status

### Observation

A directly recorded fact about one artefact, game, source, event or experiment.

Examples:

- behaviour reproduced from source code;
- a transition observed through direct play;
- a dated statement by a game's creator.

### Hypothesis

A falsifiable proposed explanation, relationship or prediction that has not met
the threshold for a pattern.

Every hypothesis must state what evidence could weaken or reject it.

### Pattern

A recurring, scoped relationship supported by at least two independent relevant
observations. Two close clones do not normally count as independent families.

Known counterexamples and the claimed scope must be stated.

### Strong Pattern

A pattern reproduced across at least three mechanically distinct puzzle
families, supported by sources and tested against plausible counterexamples.

The numeric threshold is a minimum review trigger, not automatic promotion.

### Confirmed

A bounded claim independently verified within its stated scope. This status is
appropriate for exact rules or historical facts with direct and corroborating
evidence.

`Confirmed` does not mean universal. Cross-family generalisations normally
remain `Pattern` or `Strong Pattern`.

## Evidence quality

- `Direct` — primary artefact, source code, official rules or reproduced test.
- `Corroborated` — supported by multiple independent sources or methods.
- `Limited` — relevant evidence exists but is narrow, indirect or incomplete.
- `Conflicting` — credible sources or observations disagree.

## Confidence

- `High` — unlikely to change without new contradictory evidence.
- `Medium` — useful but materially uncertain.
- `Low` — preliminary, weakly supported or sensitive to assumptions.

Confidence never promotes claim status by itself.

## Required notation

Short claims may use:

`[Status | Evidence quality | Confidence]`

Long analyses may define a claim ledger with stable local IDs and let sections
inherit those labels. Any exception must be explicit; unlabelled generalisations
are not acceptable.

## Promotion and downgrade

- `Observation → Confirmed` requires independent verification of the bounded
  claim.
- `Hypothesis → Pattern` requires repeated independent observations.
- `Pattern → Strong Pattern` requires cross-family replication and an explicit
  counterexample search.
- Any status may be downgraded when evidence conflicts or scope was overstated.

Puzzle Genome Atlas does not use `Law`. No current evidence justifies a universal
law of puzzle mechanics, and no contributor or agent may introduce the status
without a separate governance decision.
