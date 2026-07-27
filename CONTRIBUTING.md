# Contributing to Puzzle Genome Atlas

Puzzle Genome Atlas accepts evidence-backed knowledge. It does not accept raw
game concepts or unsupported novelty claims.

## Useful contributions

- a complete decomposition of a mechanically diverse puzzle;
- primary, historical or reproducible evidence;
- a counterexample or status downgrade;
- a gene-boundary correction;
- a verified structural combination;
- a structured negative result.

## Before starting

1. Read the [mission](docs/MISSION.md),
   [research principles](docs/RESEARCH_PRINCIPLES.md),
   [evidence model](docs/EVIDENCE_MODEL.md) and
   [architecture](docs/ARCHITECTURE.md).
2. Search the [game index](knowledge/games/INDEX.md), gene registry,
   combination index and taxonomy changes.
3. Open an issue describing the proposed subject and expected coverage gain.
4. Prefer a mechanically distant subject over a close relative of the most
   recent analysis.

## Game-analysis workflow

1. Reserve the next `GAME-xxxx` ID.
2. Choose the stable path shard from the lower-case game slug.
3. Copy
   [`templates/GAME_ANALYSIS_TEMPLATE.md`](templates/GAME_ANALYSIS_TEMPLATE.md).
4. Prefer original rules, source code, physical artefacts, patents, creator
   records, direct play and peer-reviewed work.
5. Separate Action, System Behaviour, Constraint, Information, Objective and
   Time Genes.
6. Use existing gene IDs whenever their boundaries fit.
7. Scan the complete game and combination indexes for exact signatures.
8. Compare only the nearest structural neighbours in detailed prose.
9. State one result: `New gene`, `New combination of known genes` or
   `Full structural match`.
10. Write `New genes: none` when applicable.
11. Update all affected indexes and records.
12. Audit the next subject and update the public research log.

## Claim requirements

Every substantive claim must expose:

- claim status;
- evidence quality;
- confidence;
- sources or reproduced evidence.

Use inline notation or a claim ledger as defined in
[`docs/EVIDENCE_MODEL.md`](docs/EVIDENCE_MODEL.md). Do not use `Law`.

## Adding or changing genes

A candidate term becomes an active gene only when it has:

- a stable type-specific ID;
- an operational definition;
- inclusion and exclusion boundaries;
- evidence and an analysed example;
- lifecycle and claim metadata.

Do not silently correct a classification. Create the next numbered file under
`research/taxonomy-changes/` from the
[taxonomy-change template](templates/TAXONOMY_CHANGE_TEMPLATE.md).

## Source quality

Prefer sources in this order when available:

1. original implementation, official rules or physical artefact;
2. creator documentation or contemporary historical record;
3. peer-reviewed academic work;
4. reputable secondary analysis;
5. community material, explicitly labelled.

Direct evidence does not eliminate uncertainty. Record conflicts and scope.

## Pull-request checklist

- [ ] The contribution adds evidence, a counterexample or a new comparison.
- [ ] Stable IDs and paths follow the architecture.
- [ ] Every substantive claim has status, evidence quality and confidence.
- [ ] Primary sources are linked where available.
- [ ] The complete indexed corpus was scanned.
- [ ] Exact matches and closest neighbours are identified.
- [ ] `New genes: none` is written when applicable.
- [ ] Gene, game and combination indexes are updated.
- [ ] Any classification correction has a taxonomy-change record.
- [ ] Required final research-summary headings are present.
- [ ] No private notes, credentials, raw ideas or unrelated files are included.

## Style

Use compact, precise prose. Define boundaries instead of multiplying synonyms.
Preserve previous conclusions and explain revisions.

By participating, you agree to follow the [Code of Conduct](CODE_OF_CONDUCT.md).
