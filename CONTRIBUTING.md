# Contributing to Project Atlas

Project Atlas accepts evidence-backed research contributions. It does not accept unsupported game concepts or novelty claims.

## Useful contributions

- A full decomposition of a mechanically diverse puzzle.
- A primary source or reproducible rule transition for an existing analysis.
- A counterexample to a working hypothesis.
- A correction to a genome comparison or matrix entry.
- Historical evidence about the origin of a mechanic.
- An auditable taxonomy-change proposal.

## Before starting

1. Read the [mission](00_MISSION.md), [research principles](01_RESEARCH_PRINCIPLES.md) and [evidence model](02_EVIDENCE_MODEL.md).
2. Search `research/games/`, the taxonomy and the combination matrix for prior work.
3. Open an issue describing the proposed subject, its puzzle family and the mechanical coverage it is expected to add.
4. Avoid analysing a game structurally close to the most recently completed subject.

## Game-analysis workflow

1. Copy [`templates/GAME_ANALYSIS_TEMPLATE.md`](templates/GAME_ANALYSIS_TEMPLATE.md).
2. Prefer original rules, source code, patents, creator accounts, direct gameplay and peer-reviewed work.
3. Separate player action, automatic response, constraint, information model, time model and objective.
4. Prefix substantive claims with `Observation`, `Pattern` or `Confirmed Pattern`.
5. Never assign `Law`.
6. Normalise the game's mechanical genome.
7. Compare it with every existing game analysis.
8. State exactly one result: `New gene`, `New combination of known genes` or `Full structural match`.
9. If no new genes exist, write `New genes: none`.
10. Update the combination matrix and verify the taxonomy.
11. Audit the research plan and recommend the next mechanically diverse game.

## Taxonomy corrections

Do not silently correct a classification.

Create the next numbered file:

`research/hypotheses/TAXONOMY_CHANGE_xxx.md`

Use [`templates/TAXONOMY_CHANGE_TEMPLATE.md`](templates/TAXONOMY_CHANGE_TEMPLATE.md), preserve the old classification, present evidence and identify every affected file. A synonym, theme or changed parameter is not a new gene.

## Source quality

Prefer sources in this order when available:

1. original implementation, rules or physical artefact;
2. creator documentation or contemporary historical record;
3. peer-reviewed academic work;
4. reputable secondary analysis;
5. community material, clearly identified as such.

Direct evidence does not eliminate uncertainty. State conflicts and source limitations.

## Pull-request checklist

- [ ] The contribution adds concrete evidence, a counterexample or a new comparison.
- [ ] Every substantive claim has an evidence status.
- [ ] Primary sources are linked where available.
- [ ] Confidence and uncertainty are explicit.
- [ ] The genome was compared with every prior game analysis.
- [ ] `New genes: none` is written when applicable.
- [ ] The taxonomy and matrix were verified.
- [ ] Any classification correction has a linked taxonomy-change proposal.
- [ ] The required final research-summary headings are present.
- [ ] No personal notes, credentials, raw ideas or unrelated files are included.

## Style

Use compact, precise prose. Define distinctions instead of multiplying synonyms. Preserve previous conclusions and explain every change.

By participating, you agree to follow the [Code of Conduct](CODE_OF_CONDUCT.md).
