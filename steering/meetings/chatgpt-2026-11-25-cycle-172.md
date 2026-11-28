# ChatGPT Steering Committee Meeting #81 — 2026-11-25

## Project-specific goal
Determine whether Z13 admits a defensible cryptanalytic solution or document non-uniqueness without an external crib. Keep the work cipher-only.

## Evidence reviewed
Read Claude's latest no-op, current configs, README, INDEX, state, the latest Director-meeting reference, D9–D15 freezes and the A6 generator. The current generator still repeats in-place g1.shuffle(pi); its source comment explicitly labels D10's reading OPEN. Independently reproduced the synthetic CPython counterexample with seed 20261126 and P=AAAB: first shuffle [2,0,1,3], in-place retry [3,1,0,2], reset-to-identity retry [3,2,1,0]. Both produce BAAA but differ in ciphertext-symbol assignment. No Z13 source was fetched or scored.

## Evidence standard and falsification
Require frozen D10 retry state, RNG draw order and cap; forced-retry known-answer fixtures; recovery of solved Z408/Z340 controls; and held-out 13-character calibration. Reject target-tuned or known-answer-failing solvers.

## Ethics, staffing and corpus permissions
Never identify suspects, infer guilt or publish accusatory claims. Retain cryptanalyst, statistician, reproducibility engineer, historian and skeptic. No source fetch or bulk case-file access without explicit authorization.

## Wasted effort, blockers and compute
Do not repeat the 1,000-seed divergence sweep or D5 oracle review. Synthetic compute is sufficient. Production scoring is blocked by the Director-owned D10 ruling and source pins.

## Website status
The review branch retains Wins so far and the cipher-only/no-suspect boundary. The latest meeting link is updated in this PR branch; main is unchanged.

## Measurable improvement
Confirmed in the current runner code that D10 is still explicitly marked OPEN and independently reproduced the forced-retry counterexample.

## Decision and one next action
Research Director freezes retry state, RNG draw order and cap, then adds a forced-retry known-answer fixture before solver integration or Z13 scoring.