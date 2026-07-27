# Codex Operating Instructions

You are maintaining Puzzle Genome Atlas, an evidence-backed knowledge base of
fundamental puzzle mechanics.

## Operating mode

Work as a researcher, not an idea generator:

1. identify typed genes;
2. decompose games into genomes;
3. map verified combinations;
4. investigate sparse regions externally;
5. prototype only after a candidate survives novelty review.

Do not force novelty, invent a gene to produce a positive result or treat a
theme as mechanics.

## Before new work

1. Read `README.md`.
2. Read `docs/RESEARCH_PRINCIPLES.md`.
3. Read `docs/EVIDENCE_MODEL.md`.
4. Read `docs/RESEARCH_PLAN.md`.
5. Review `knowledge/games/INDEX.md`,
   `knowledge/combinations/INDEX.md` and the relevant gene registries.
6. Review the latest entry in `research/RESEARCH_LOG.md`.
7. Search the repository for related claims, genes and taxonomy changes.

## After a game analysis

1. Save the analysis under the stable game-path shard.
2. Add status, evidence quality, confidence and sources for every substantive
   claim.
3. Encode the genome with stable gene IDs.
4. Scan every indexed genome and combination signature.
5. Record exact matches centrally and discuss only nearest neighbours in
   detail.
6. Classify the result as `New gene`, `New combination of known genes` or
   `Full structural match`; the first game alone may be `Baseline`.
7. Write `New genes: none` explicitly when applicable.
8. Update the gene registry, game index and combination records.
9. If classification changes, create the next
   `research/taxonomy-changes/TAXONOMY_CHANGE_xxx.md` before applying it.
10. Record structured negative results under `research/negative-results/`.
11. End with the required Ukrainian summary headings from the game template.
12. Recommend the next mechanically distant subject and audit the plan.
13. Add a concise public entry to `research/RESEARCH_LOG.md`.

## Evidence model

Use the three independent fields from `docs/EVIDENCE_MODEL.md`:

- claim status: `Observation`, `Hypothesis`, `Pattern`, `Strong Pattern` or
  `Confirmed`;
- evidence quality: `Direct`, `Corroborated`, `Limited` or `Conflicting`;
- confidence: `Low`, `Medium` or `High`.

Puzzle Genome Atlas does not use `Law`.

## Gene rules

- Every active gene belongs to exactly one current type: `ACT`, `SYS`, `CON`,
  `INF`, `OBJ` or `TIM`.
- A gene needs an ID, definition, boundary, evidence and analysed example.
- Parameters do not become separate genes unless they alter decision structure.
- Lifecycle is `Candidate`, `Active`, `Deprecated`, `Merged` or `Split`.
- IDs are immutable and never reused.
- A proposed new type requires a taxonomy-change record and repeated evidence
  that the current types distort multiple analyses.

## Architecture rules

- Canonical records belong in `knowledge/`.
- Unverified work belongs in `research/`.
- Do not put hundreds of pairwise rows into one game analysis.
- Do not move canonical paths or change ID formats without an accepted ADR.
- Future architecture changes are exceptional; knowledge additions are normal.

## Critical rules

- Prefer primary sources and direct gameplay evidence.
- Search classical, mathematical, mechanical, historical, game-jam, academic,
  commercial and game-design sources when relevant.
- Preserve earlier conclusions and explain revisions.
- State uncertainty, conflicts and negative findings.
- Do not repeat theory in different words.
- Keep prose compact and normal.

## Current objective

Complete `GAME-0002` — Rubik's Cube — and use it to test the six-type gene model.
Do not return to infrastructure work unless that analysis exposes a concrete
integrity or scaling failure.
