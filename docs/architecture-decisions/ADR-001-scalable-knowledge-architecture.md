# ADR-001 — Scalable knowledge architecture

- Status: `Accepted`
- Date: 2026-07-27
- Decision owner: Puzzle Genome Atlas maintainer

## Context

The initial repository successfully captured one game analysis, but it mixed
canonical knowledge, working vocabulary and research leads. A flat game
directory and a full pairwise table inside every future analysis would become
hard to navigate and would duplicate roughly 500,000 comparison pairs at 1000
games.

## Decision

- Separate `docs/`, `knowledge/`, `research/` and `templates/`.
- Give games, genes and combinations stable IDs.
- Shard game files by non-semantic slug ranges.
- Keep full-corpus exact and near matching in the game index.
- Scan combination records as proper-subset interactions, not game signatures.
- Limit detailed prose comparisons to mathematically selected near matches.
- Treat undefined taxonomy vocabulary as candidate terms, not accepted genes.
- Keep the six current gene types until evidence justifies a typed extension.
- Validate links, stable IDs, gene references and index coverage in continuous
  integration.

## Consequences

- New contributors can distinguish accepted knowledge from open investigation.
- Future automation can parse stable IDs without another path migration.
- Some manual index maintenance remains until generation tools are justified.
- The architecture adds several small registry files, but avoids a later
  high-risk migration of hundreds of analyses.

## Amendment — 2026-07-28

The final pre-corpus review formalised the genome signature and Jaccard
near-match rule, restricted combinations to proper subsets of supporting
genomes, consolidated status definitions and made index consistency
machine-validated. It did not add a new record type or change any stable ID.
