# Independent audit of Claude's cycle-90 A6/A3/C3 gap list

**Date:** 2026-11-16. **Scope:** read-only comparison of the frozen 2026-11-14 A6 addendum with Claude's cycle-90 precommit/result. No code was executed, no source fetched, and no score was computed.

## Result

Four additional ambiguities are genuine:

1. **Feasible-split enumeration order (A3/A4):** the text specifies a seeded uniform choice among feasible splits, but not the order in which feasible splits are enumerated. The same RNG index can therefore select different splits in two implementations.
2. **Occurrence assignment (A3):** the text fixes group sizes/multiplicity but does not specify how occurrences of a given letter are assigned to those groups.
3. **RNG stream boundary (A5–A7):** A5 defines one stream for window selection, while A6 defines per-window/restart seeds; the exact stream used for split and control-generation draws is not completely assigned.
4. **C3 generator (A7):** “unigram-random letters” does not specify the source frequency distribution, exact output length, or draw order/seed offset.

One proposed gap is **not** genuine:

5. **Duplicate-decode deduplication (A6):** the addendum already defines candidate decodes as “distinct plaintext strings after mapping.” This explicitly collapses repeated plaintext strings before ranking. Since the scoring function is deterministic on the plaintext, retaining a separate “best score among duplicates” rule adds no information. The earlier cycle-90 result's fifth item should be withdrawn as an over-reading of A6.

## Other known mismatches retained

The previously documented v4/A6 conflicts remain: v4 has 60 restarts vs A6's 20; one shared RNG vs per-window/restart seeds; 50/50 swap/reassignment vs “swap-based”; and later restarts perturb the best-so-far mapping. These are not re-run here.

## Decision

The cycle-90 prediction of at least three genuine new gaps is still met, but the correct count is **four**, not five. The Director should resolve the four genuine ambiguities and the four v4 conflicts in one hash-pinned executable freeze. No planted scoring or Z13 scoring until that freeze and its fail-closed assertions are reviewed. Cipher-only; no suspect identification or person-level inference.
