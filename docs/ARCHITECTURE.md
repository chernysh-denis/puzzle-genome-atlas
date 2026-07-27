# Repository Architecture

Puzzle Genome Atlas separates accepted knowledge from active investigation.
That boundary is the main scaling rule.

## Canonical vocabulary

These definitions are normative throughout the repository.

- A **gene** is one typed, bounded, decision-relevant mechanic represented by
  an immutable ID. Its admission rules live in
  [`knowledge/genes/README.md`](../knowledge/genes/README.md).
- A **parameter** is a value inside one gene, such as board capacity or
  direction set. It refines an instance of that gene but is not a gene and has
  no stable ID. If a parameter repeatedly changes decision structure enough to
  make one gene boundary misleading, that is evidence for a taxonomy change.
- A **genome** is the complete set of active gene IDs assigned to one scoped
  game or ruleset, partitioned into the six gene types. Parameters and source
  notes belong to the analysis but not to the signature defined below.
- A **genome signature** is the canonical, parameter-free representation of a
  genome used for corpus comparison.
- A **combination** is a verified interaction among two or more genes from at
  least two types. Its gene set must be a proper subset of every supporting
  game's genome signature. A combination captures a reusable decision
  structure; it is not another name for a game or its full genome.

Presentation, theme, platform, family labels and release metadata are outside
the genome signature.

## Genome signature

Let the six ordered gene types be

```text
T = (ACT, SYS, CON, INF, OBJ, TIM)
```

For a scoped game `g`, let `G_t(g)` be the finite set of active gene IDs of type
`t`. Its signature is the ordered tuple

```text
S(g) = (G_ACT(g), G_SYS(g), G_CON(g), G_INF(g), G_OBJ(g), G_TIM(g))
```

Each set is deduplicated and rendered in ascending ID order. The `gene_ids`
front matter of a game record is the canonical stored form; index signatures
are derived lookup copies and must contain the same IDs.

Parameters are deliberately excluded. Therefore an exact match means “the same
structure at the current gene resolution”, not identical numbers, board
geometry, presentation or implementation.

### Exact match

Games `a` and `b` are an exact genome match if and only if

```text
S(a) = S(b)
```

Equivalently, `G_t(a) = G_t(b)` for all six types.

### Near match

Flatten the signature into typed pairs:

```text
U(g) = {(t, id) | t in T and id in G_t(g)}
```

Define Jaccard similarity over the complete typed gene sets:

```text
sim(a, b) = |U(a) ∩ U(b)| / |U(a) ∪ U(b)|
```

Every valid genome contains at least one gene, so the denominator is non-zero.
This formula does not award similarity for two games merely lacking the same
gene type and introduces no untested type weights.

For a new game `a`, its **near matches** are all non-exact indexed games with a
positive score equal to the maximum non-exact `sim(a, x)` in the corpus. Ties
are retained. If every non-exact score is zero, there is no near match.

The score selects records for detailed comparison; it is not evidence that two
games feel alike or that their shared structure is novel. Parameters explain
decision-relevant differences after the mathematical scan.

## Top-level structure

```text
docs/        Method, governance, evidence model and research plan
knowledge/   Canonical genes, game genomes and verified combinations
research/    Leads, taxonomy proposals, candidates and negative results
templates/   Required contribution formats
scripts/     Repository-integrity validation
```

Root files are limited to public orientation and project governance.

## Stable identifiers

- Games: `GAME-xxxx`
- Genes: `ACT-xxx`, `SYS-xxx`, `CON-xxx`, `INF-xxx`, `OBJ-xxx`, `TIM-xxx`
- Combinations: `COMB-xxxx`
- Taxonomy changes: `TAXONOMY_CHANGE_xxx`

IDs are never reused. Renames change labels, not identifiers.

## Game-file scaling

Game analyses use stable alphabetical path shards:

```text
knowledge/games/0-9/
knowledge/games/a-f/
knowledge/games/g-l/
knowledge/games/m-r/
knowledge/games/s-z/
```

The shard is non-semantic, so a change in puzzle family never moves a file.

## Comparison scaling

Every new genome is still checked against the full corpus, but the result is
not copied as hundreds of prose rows into the new analysis.

1. Compare the complete game signatures in the game index using the rules
   above.
2. Test whether each verified combination's gene set is a subset of the new
   signature.
3. Record every exact match and every mathematically selected near match.
4. Describe only those near matches in detailed prose.
5. Put shared combination knowledge in one `COMB-xxxx` record.

This preserves exhaustive matching while avoiding quadratic narrative
duplication.

## Integrity checks

`scripts/validate_repository.py` verifies local Markdown links, stable-ID
uniqueness, controlled metadata values, gene boundaries, game front matter,
type-correct gene references, path shards, combination subsets and index
signature equality. Continuous integration also runs Markdown lint.

TODO: automatic claim-to-prose coverage is intentionally deferred. Determining
whether arbitrary prose contains a substantive claim requires human judgement;
the validator checks claim-ledger field values, while review checks whether the
ledger is complete. Do not add heuristic prose classification until repeated
review failures justify it.

TODO: parameter schemas, generated indexes and a separate multi-maintainer
governance document are deferred. The one-game corpus has not exposed a
parameter-boundary failure, manual indexes remain readable and decisions still
have one maintainer. Add each mechanism only after its stated condition changes.

## Architecture change policy

This revision is intended to be the last broad relocation. Future structural
changes require:

1. a concrete scaling or integrity failure;
2. an architecture decision record in `docs/architecture-decisions/`;
3. a migration plan with link validation;
4. preservation of stable IDs and Git history.

Adding genes, analyses, combinations or validators is normal knowledge work and
does not count as an architecture change.
