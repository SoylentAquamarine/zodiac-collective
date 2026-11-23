# Precommit: A6 runner, generator half (length-13 windows) — 2026-11-23, scheduled cycle 22
Written BEFORE any code is run. Cipher-only; no suspect inference. No source fetched; no scoring; no solver run.

## Known
D1–D15 and A1–A8 are frozen. ChatGPT #151–#157 each name the production runner as the next action. D5 fixtures (58/58) exist.

## Not done
No production code exists. Source pin is UNFILLED, so the runner cannot run on real text, and this cycle does not try.

## Design
Build `data/scripts/a6_runner_generator.py`: window selection (D14), feasible-split enumeration (D5), occurrence assignment (D6), plant/C1/C2/C3 construction (D10–D12), symbol labelling (D13), manifest, and fail-closed assertions 3, 6, 8, 9, 11, 12, 13. Scope is length-13 windows (A3 vector [3,2,2,2,1,1,1,1]), where exhaustive enumeration is feasible. The solver and scoring are NOT touched. Source-pin assertion 5 is implemented as an abort when no pin file exists.
Non-circular: the tests use a SYNTHETIC letter string from Random(1) (explicitly not a source, not natural language), and test properties the frozen text states (multiplicity vector, seed uniqueness, determinism, joint permutation/reversal), not anything derived from the generator's own output.
Known-answer tests: reuse the committed D5 hand values; add hand-checkable cases for D10/D11.

## Prediction
Gaps will show up when D5–D15 are turned into code (the spec has been ambiguous on each previous pass). Expected candidates: length 34/100 enumeration infeasible by brute force (D5 says "enumerate"), and C3 D12 rejection cap behaviour on short feasible sets.

## Honesty precommitment
Any ambiguity found is reported as an open item for the Director addendum, not silently resolved. If a freeze rule is unimplementable as written, I say so rather than patch it. Nothing here is a Z13 result.
