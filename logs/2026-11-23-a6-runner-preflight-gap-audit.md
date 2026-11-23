# A6 runner preflight gap audit — 2026-11-23

## Scope

Read, without editing, the frozen A6 operational freeze, its precommit, the Z13 planted-recovery protocol freeze, the pre-score addendum, the D5/D6/D7 fixture code and the latest runner-gaps record.

## Frozen details confirmed

- D1: 20 independent restarts per ciphertext, 12,000 iterations each.
- D2: restart 0 uses the frequency seed; restarts 1–19 use independent random mappings and fresh per-restart RNGs, not perturbations of a prior best.
- D3: the 50% swap/reassign move is part of the frozen move set.
- D4: per-window split RNG, C3-letter RNG and per-restart solver RNG are specified.
- D5/D6: feasible split enumeration/order and seeded occurrence assignment are frozen.
- D7: C3 uses the pinned source register's unigram distribution and the paired window's class structure.
- D8: deduplicate plaintexts, retain each duplicate's best score, rank by score with lexicographic tie-breaking and report ties.

## Two implementation questions that are not explicit in the freeze

1. **C1 shuffle RNG:** C1 must shuffle the plaintext, but D4 does not explicitly name a C1 shuffle seed or draw order. Reusing the per-window split RNG after D5/D6 is plausible, but is not stated.
2. **C3 class assignment:** D7 says to use the same class structure as the paired window. It does not explicitly say how to assign that class-size vector to the new C3 random-letter counts. Reapplying D5/D6 with the split RNG is plausible, but is not stated.

These are specification gaps, not license to invent seeds. Do not edit the frozen A6 files or score a production source until the Research Director records a dated addendum resolving them.

## Separate source/permission gate

The second-register source-pin file is still unfilled. No exact source URL, public-domain determination, user authorization reference or source hash was available. No second-register source was fetched and no A6 scoring was run.

## Decision

The runner remains unimplemented and pre-score. The next action is a Director-owned addendum for the two control-generation details; after that, implement the runner with fixture tests and an explicit fail-closed source-pin gate. No suspect inference is authorized.
