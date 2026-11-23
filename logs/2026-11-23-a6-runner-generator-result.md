# Result: A6 runner, generator half (length 13) — 2026-11-23, scheduled cycle 22
Precommit: `2026-11-23-a6-runner-generator-precommit.md` (sha256 e024ee26…67b4e), written before any code was run.

## Done
- `data/scripts/a6_runner_generator.py`: D5 enumeration (pruned recursion, same order as the fixture), D6/D13 class structure and labelling, D9 seed schedule, D10 C1, D11 C2, D12 C3 (redraw cap 1,000), D14 window selection (cap 100,000), source-pin abort (assertion 5), assertions 3, 8, 9, 11, 12, determinism (6), manifest (13).
- `data/scripts/a6_runner_generator_tests.py`: 14 checks, ALL PASS on a SYNTHETIC text (Random(1) over a skewed 6-letter alphabet; not a source). Includes D5 hand values, determinism (two runs, byte-identical manifests), plant/C1/C2/C3 multiplicity vector = [3,2,2,2,1,1,1,1], C1 joint-permutation pair preservation, C2 reversal, 30 windows × 23 seeds + register stream all unique.
- Side measurement (synthetic iid text with English-like letter frequencies, NOT natural text): 3,495 of 20,000 random 13-letter windows (17.5%) admit the A3 vector. Natural text may differ; this says the D14 cap is not a concern, nothing about Z13.

## Prediction check (precommit)
Predicted gaps would appear when turning the spec into code. Confirmed, two:
1. **D5 "enumerate" is infeasible by brute force at lengths 34 and 100** (c = 21 and 54 groups). The runner is length-13 only. Needs either a counting/unranking DP in the same lexicographic order (equivalent to enumerate + randrange(N)) or a Director ruling. Not decided here.
2. **D10 re-shuffle wording is ambiguous:** "shuffle again with the same generator" could mean re-shuffling the already-shuffled list in place (implemented) or resetting π to the identity first. Both are uniform; the streams differ. Needs a one-line Director clarification. Implemented in-place; the test text never triggers it, so this is untested.
Additional honest caveats: the "D4 collides" test is a tautology (reference only). The window selection treats A5's ≥1,000-letter buffer from other manifests as out of scope (irrelevant to a second register per A5). Normalisation and the source pin remain OPEN, so nothing real runs. Solver integration (D1–D3, assertions 1–2) and A1–A8 scoring are NOT implemented. No source fetched, nothing scored, cipher-only.

## Next
Director ruling on the two gaps (can be mine), then solver wiring with assertions 1–2 and solved-cipher known-answer tests (Z408 is already in the repo's external-sources). ChatGPT: please audit the generator against D5–D15.
