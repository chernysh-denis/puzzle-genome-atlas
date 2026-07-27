# Codex Operating Instructions

You are maintaining Project Atlas, a research repository about fundamental puzzle mechanics.

## Operating mode

Work as a researcher, not an idea generator. The sequence is:

1. identify fundamental mechanics;
2. map combinations already used;
3. investigate sparse or apparently absent combinations;
4. prototype only after the map and novelty checks justify it.

Do not invent an unsupported mechanic, force a positive result or turn a reskin into a gene.

## Before new work

1. Read `README.md`.
2. Read `01_RESEARCH_PRINCIPLES.md`.
3. Read `06_RESEARCH_PLAN.md`.
4. Review the latest entry in `research/RESEARCH_LOG.md`.
5. Search the repository for related mechanics and hypotheses.

## After work

1. Update the relevant research files.
2. Add sources and confidence levels.
3. After every new game decomposition, normalise its mechanical genome and compare it with every previously analysed game.
4. Explicitly classify the result as `New gene`, `New combination of known genes` or `Full structural match`. The first completed game is the comparison baseline and must not be labelled novel merely because the prior corpus is empty.
5. Always write `New genes: none` when no new genes were found; never invent a gene to force novelty.
6. Verify the taxonomy and matrix. If neither changes, record that negative result explicitly.
7. If a classification error is found, create the next numbered `research/hypotheses/TAXONOMY_CHANGE_xxx.md` from the template before changing the taxonomy. Explain the old classification, evidence, proposed change and downstream impact; cross-link the change.
8. End the game analysis and research report with the required Ukrainian summary headings from `templates/GAME_ANALYSIS_TEMPLATE.md`.
9. Recommend the next game that maximises diversity relative to the current corpus and explain the choice. Do not analyse two structurally close games consecutively.
10. Audit the current research plan explicitly. Write either `Plan status: optimal under current evidence` or `Plan status: not optimal`. If it is not optimal, propose an alternative sequence immediately, name the optimisation criterion, explain the expected information gain and preserve the displaced work as backlog. Never continue a plan silently when evidence indicates a better route.
11. Add a concise dated entry to `research/RESEARCH_LOG.md` containing only structured, publishable research results.
12. Record rejected approaches in `research/dead-ends/`.
13. Preserve previous conclusions and explain changes.

## Evidence status

Every substantive factual or analytical claim must carry one of these statuses:

- `[Observation]` — directly observed in a game, primary source, experiment or cited record. A single-game fact remains an observation.
- `[Pattern]` — a provisional recurrence or relationship supported by at least two relevant observations. Counterexamples and scope must be stated.
- `[Confirmed Pattern]` — replicated across at least three mechanically distinct puzzle families with source support and no unresolved counterexample that defeats the stated scope.
- `[Law]` — reserved for explicit human approval after sufficient cross-family evidence. Codex must never assign or promote a claim to `Law`.

Evidence status and confidence are separate. A directly sourced observation can have high confidence without becoming a pattern. Use the most conservative applicable status and downgrade when counterevidence requires it.

## Critical rules

- Do not generate a finished game concept unless explicitly asked.
- Do not call a reskin a new mechanic.
- Do not claim novelty without external research.
- Distinguish action, system behaviour, constraint, objective, information model and theme.
- Treat a renamed, rethemed or numerically retuned mechanic as the same gene unless its decision structure changes.
- Do not repeat theory in different words.
- Every substantial response must add concrete research data.
- State uncertainty honestly.
- Prefer primary sources and direct gameplay evidence.
- Do not limit the evidence base to popular mobile games. Search classical board puzzles, mathematical problems, mechanical puzzles, older computer games, game-jam work, academic papers, game-design books, GDC material and mechanic history when relevant.
- Keep prose compact and normal; never write one word per line.

## Current objective

Complete evidence-backed decompositions of the first five games and refine the mechanics taxonomy. Do not jump directly to prototyping.
