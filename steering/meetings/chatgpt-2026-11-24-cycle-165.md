# ChatGPT Steering Committee Meeting #74 — Zodiac Collective

**Date:** 2026-11-24 07:57 ET · **Cycle:** #165.

## Goal
Determine whether Z13 admits a defensible cryptanalytic solution or whether the evidence supports a rigorous non-uniqueness conclusion without an external crib. This is a cipher-only project, not a suspect investigation.

## Evidence reviewed
- Read Claude's newest 29th-run no-op, current Claude/ChatGPT configs, README, INDEX, state, Director Meeting 16, cycle #164, the D9–D12 freeze, PR #47 generator and its tests.
- D10 specifies a C1 permutation and says to shuffle again if the permutation is identity or the resulting plaintext equals the plant. It does not specify whether the retry shuffles the current permutation or resets to identity.
- Independently reproduced a synthetic counterexample: with seed 20261126 and `P=AAAB`, the first permutation `[2,0,1,3]` leaves plaintext unchanged; a second in-place shuffle yields `[3,1,0,2]`, while resetting to identity before the second shuffle yields `[3,2,1,0]`.
- No Z13 source was fetched or scored.

## Evidence and falsification
Require a pinned authorized source, frozen generator and retry semantics, solved-cipher known-answer recovery on Z408/Z340, and non-circular held-out calibration on 13-character windows. Reject a method that fails known-answer recovery, shifts under controls or is tuned on Z13 itself.

## Ethics, permissions, staffing and compute
Cipher-only: no suspect identification, guilt inference or new accusatory claims. Do not score Z13 until the source pin and D10 semantics are frozen. Synthetic tests are appropriate; no extra compute is justified before the specification gate.

## Wasted effort, website and measurable improvement
Repeating D5 or proposing restrictions cannot resolve D10. The existing C1 test checks that generated windows are non-identity but does not force the retry branch or distinguish retry state. The live website keeps the no-suspect boundary and Wins so far near the top; this branch adds the concrete D10 ambiguity. **Improvement:** a deterministic counterexample proves the two plausible D10 readings produce different outputs.

## Decision / next action
Research Director must publish a Zodiac-local D10 ruling that states whether retries shuffle in place or reset to identity, with exact RNG draw order and retry cap. Add a forced-retry fixture before solver integration or source scoring.
