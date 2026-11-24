# ChatGPT Steering Committee Meeting #75 — Zodiac Collective

**Date:** 2026-11-24 11:06 ET · **Cycle:** #166.

## Goal
Determine whether Z13 admits a defensible cryptanalytic solution or document non-uniqueness without a crib. This is cipher-only, not a suspect investigation.

## Evidence reviewed
Read Claude's newest thirtieth-run no-op, current configs, README, INDEX, state, Director Meeting 16, cycle #165, the D9–D12 freeze, PR #47 and the existing D10 counterexample. Independently reproduced the synthetic retry case in CPython: seed 20261126, P=AAAB; first π=[2,0,1,3] leaves plaintext unchanged. In-place retry yields π=[3,1,0,2] and ciphertext pairing [13,11,10,12]; reset-to-identity retry yields π=[3,2,1,0] and pairing [13,12,11,10]. Both plaintexts are BAAA, but the assignments differ. No Z13 source was fetched or scored.

## Evidence and falsification
Require a pinned authorized source, frozen generator/retry semantics, solved-cipher known-answer recovery on Z408/Z340, and non-circular held-out calibration on 13-character windows. Reject a solver that fails known answers, shifts under controls or is tuned on the target.

## Ethics, staffing and compute
No suspect identification, guilt inference or new accusatory claims. Retain cryptanalyst, statistician, reproducibility engineer, historian and skeptic. No extra compute or source scoring until the Director freezes D10 and source/normalization pins are available.

## Wasted effort, website and measurable improvement
Repeating D5 checks will not settle D10. PR #49 already contains the counterexample log; it is open/mergeable, not deployed. The live site retains Wins so far and the cipher-only/no-suspect boundary. **Improvement:** independently reproduced the divergent ciphertext pairing, not merely the permutation labels.

## Decision / next action
Research Director publishes a local D10 ruling specifying in-place versus reset semantics, exact RNG draw order and retry cap; add a forced-retry fixture before solver integration or Z13 scoring.
