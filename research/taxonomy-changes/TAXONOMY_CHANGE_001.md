# Taxonomy Change 001: Typed gene registry

## Status

- Proposal status: `Accepted`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Date: 2026-07-27
- Trigger: final pre-growth architecture review

## Current classification

- Historical model: six prose lists in a pre-public
  `04_MECHANICS_TAXONOMY.md`.
- Original rationale: separate actions, system behaviours, constraints,
  objectives, information and time.
- Matrix impact: prose terms were used directly in combination rows.

The pre-public file is intentionally not part of the canonical repository. The
relevant old classification is preserved in this record so the decision does
not depend on an unavailable document.

## Detected problem

The six layers are useful, but the lists treat undefined words as if they were
already reusable genes. They lack stable IDs, boundaries, lifecycle and
evidence. The same word can also occupy different roles: `merge` may be a
player action in one game and automatic collision resolution in another.

This is a classification integrity problem, not a naming preference.

## Evidence

- The [2048 analysis](../../knowledge/games/0-9/2048.md) required a correction
  from player-commanded merge to player-commanded slide plus automatic merge.
- The old matrix marked several games `Established` without complete analyses
  or source records.
- No evidence currently requires a seventh gene type.
- Counterpoint: stable IDs add process cost for the first few games. The cost is
  accepted because retrofitting IDs after hundreds of analyses is riskier.

## Change

- Preserve the six types: Action, System Behaviour, Constraint, Information,
  Objective and Time.
- Replace undefined taxonomy entries with a candidate-term inventory.
- Admit a term to the active registry only after it has an operational
  definition, boundaries, evidence and an analysed example.
- Assign immutable type-specific IDs to active genes.
- Separate gene lifecycle from claim status, evidence quality and confidence.
- Move unsupported combination rows to research leads.

## What does not change

- No candidate term is deleted.
- No novelty claim is created.
- The 2048 mechanical conclusions remain intact.
- Theme and presentation remain outside the gene model.

## Impact

- Genes added: only baseline genes evidenced by `GAME-0001`.
- Genes removed: none; undefined vocabulary remains as candidate terms.
- Matrix: `COMB-0001` becomes the sole verified baseline combination.
- Earlier analysis: 2048 gains stable IDs and a claim ledger.
- Novelty claims: none affected because none existed.

## Test result — 2026-07-28

[`GAME-0002` — Rubik's Cube](../../knowledge/games/m-r/rubiks-cube.md)
represented permutation and orientation as state parameters under
`CON-004`, not as new types. Direct layer rotation, global reachability
invariants, primitive reversibility, reconstruction objective and self-paced
time fit the existing registries. Its System Behaviour set is validly empty.

The six-type model, genome signature, proper-subset combination rule and
exact/near comparison all remained executable. No concrete failure case was
found, so this accepted change needs no follow-up proposal.

## Decision

- Decision: `Accepted`
- Rationale: required for auditable comparison at 100–1000 game analyses.
- Architecture reference:
  [`ADR-001`](../../docs/architecture-decisions/ADR-001-scalable-knowledge-architecture.md).
