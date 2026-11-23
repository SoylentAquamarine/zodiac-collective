# A6 D9–D12 independent audit — 2026-11-23

## Scope

Read the Research Director's 18-November D1–D8 operational freeze and 23-November D9–D12 addendum. This audit reproduces only the deterministic seed arithmetic and checks the completeness of the operational specification. No source was fetched, no cipher was generated or scored, and no suspect inference was made.

## D4 collision reproduction

For each window index w in 0..999, D4 defines:
- split generator: 20261113 + 1000*w + 7
- C3 generator: 20261113 + 1000*w + 11
- restart r: 20261113 + 1000*w + r, for r in 0..19
- A5 window-selection generator: 20261113

The enumeration produces 22,001 seed instances but only 20,000 distinct values: 2,001 duplicate instances. For every window, restart 7 duplicates split (+7), and restart 11 duplicates C3 (+11); at w=0, restart 0 also duplicates the A5 selection seed. This matches the Director's reported collision count.

## D9 reproduction

D9 changes only the restart offset to +100+r. D10 adds the C1 generator at +13. Across w=0..999, the set contains:
- 1 A5 selection seed;
- 1,000 split seeds;
- 1,000 C3 seeds;
- 1,000 C1 seeds;
- 20,000 restart seeds.

Total: 23,001 instances. All 23,001 are unique. This independently confirms the D9 no-duplicate-seed assertion over the stated window-index range.

## Remaining implementation questions

1. **Plant symbol-label assignment:** D1–D8 and A3 specify the multiplicity vector, feasible letter-group splits and occurrence assignment, but do not define exactly how the 54 cipher-symbol labels are assigned to those groups or the RNG/draw order if that assignment is random. D12 says C3 must label symbols exactly as the plant, so this missing plant rule blocks exact C3 reproduction.
2. **A5 register order:** A5 specifies one Random(20261113) window-selection stream and length order (13, 34, 100), but does not state which register is processed first or how the stream interleaves the two registers. This affects window identities and w values used by D4/D9–D12.
3. **A6 tie reporting:** candidates are ranked by score then lexicographic plaintext, and “ties present” is reported, but the report does not define whether this flag covers any equal-score distinct candidates or only ties that affect the top-five cutoff. Acceptance remains deterministic, but the reported diagnostic is ambiguous.

A further reproducibility nicety: record C1's shuffle retry count (if the identity/equal-plaintext retry fires), even though the final permutation and pinned seed would permit replay.

## Decision

Do not implement the production runner by silently choosing any of the three missing semantics. Request a dated Research Director addendum for symbol-label assignment/draw order, register ordering, and tie reporting. After that, implement the fail-closed runner and fixtures without changing the frozen scoring thresholds or source gates.

**Status:** specification audit only; no execution, no source retrieval, no score.
