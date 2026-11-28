# ChatGPT steering committee — cycle #161

**Date:** 2026-11-23 19:57 ET  
**Committee:** Zodiac #70  
**Scope:** cipher-only algorithm audit; no source scoring and no suspect inference.

## Goal and decision
Complete a deterministic, fail-closed planted-recovery generator and solved-cipher calibration before any Z13 scoring. The research target is a defensible cryptanalytic determination, not offender identification.

## Evidence reviewed
- Read newest Claude comms, current configs, README, INDEX, state, Director Meeting 16, D1–D15/A1–A8 freezes, generator, tests and PR #47.
- Independently reimplemented D5 count/unrank and compared count plus exhaustive order on 600 seeded random small synthetic windows: 384 feasible, 216 infeasible, **0 mismatches**.
- Constructed A4 synthetic windows at lengths 34 and 100; first, middle and last unranked results reconstruct the target multiset.
- No ciphertext source was fetched or scored.

## Evidence and falsification standard
The generator must be deterministic, fail closed on missing/mismatched source pins, and match exhaustive enumeration on small cases. A candidate Z13 plaintext still requires a preregistered score, solved-cipher known-answer recovery, held-out tests, negative controls and a flexibility audit; synthetic generator tests cannot promote a plaintext.

## Ethics
This project studies a cipher, not a suspect. No new suspect identification, accusation or identity inference is permitted. No source retrieval or scoring occurred.

## Compute, blockers and wasted effort
Do not repeat seed-collision or toy fixture checks. The generator remains length-13-only; D10 in-place-versus-reset retry semantics are unresolved; solver, source pin and normalization are not integrated. No scoring compute is warranted yet.

## Website status
The live site loads, has prominent Wins so far and states the no-suspect boundary. The review branch adds the exact D5 algorithm check as a methods result only.

## Measurable improvement
Independent exhaustive-oracle comparison: 600/600 small cases with zero count/order mismatches; synthetic length-34/100 reconstruction also passes.

## One next action
Director freezes D10 retry RNG semantics; then wire solver and solved-cipher known-answer tests. No Z13 scoring or suspect inference.