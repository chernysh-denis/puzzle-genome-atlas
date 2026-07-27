# Combination Registry

A combination record identifies a verified interaction between genes. It is not
an empty matrix cell, a game pitch or a novelty claim.

The canonical definition is in
[`docs/ARCHITECTURE.md`](../../docs/ARCHITECTURE.md#canonical-vocabulary). In
particular, a combination gene set is a proper subset of each supporting game
genome; it must not duplicate a full genome.

Each record requires:

- a stable `COMB-xxxx` ID;
- a gene set containing at least two IDs from at least two types;
- at least one analysed game;
- decision-structure notes;
- a match boundary and explicit novelty conclusion;
- evidence and confidence.

The [index](INDEX.md) supports corpus-wide subset scanning. Exact and near
genome matching uses the separate game index. Exploratory combinations remain in
[`research/combination-leads/`](../../research/combination-leads/) until they
are supported by a complete analysis.
