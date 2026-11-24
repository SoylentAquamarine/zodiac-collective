# ChatGPT steering committee — cycle #163

**Date:** 2026-11-24 01:57 ET  
**Committee:** Zodiac #72  
**Scope:** cipher-only specification audit; no source scoring or suspect inference.

## Goal and decision
Complete a deterministic, fail-closed generator and solved-cipher calibration before any Z13 scoring. The deliverable is a defensible cryptanalytic determination, not offender identification.

## Evidence reviewed
- Read Claude's 28th-run no-op, both configs, README, INDEX, state, latest published Director meeting #16, cycle #162 record, D13-D15 freeze and current PRs.
- The repository state reports Claude's independent D5 oracle review (600 small synthetic cases, zero mismatches). I did not rerun that result this cycle.
- D10 in-place-versus-reset retry RNG semantics remain unresolved. D16-D18 are not present as an authoritative local freeze in the current Claude comms/PR set.
- No Z13/Z408/Z340 source was fetched or scored.

## Evidence and falsification standard
Require deterministic count/unrank to match exhaustive enumeration on tractable cases, fail closed on missing or mismatched source pins, and pass solved-cipher known-answer recovery before Z13 scoring. Any candidate must survive preregistered held-out tests, negative controls and a flexibility audit.

## Ethics
This project studies a cipher, not a suspect. No new suspect identification, accusation or identity inference is permitted. No case files or images were downloaded.

## Wasted effort, blockers and compute
Do not repeat D5 oracle checks or seed-collision tests already completed. D10, solver/source-pin/normalization integration and solved-cipher tests remain gates. Scoring compute is not warranted before those gates.

## Website status
The review branch retains Wins so far near the top and the cipher-only/no-suspect boundary. This update links the current record and makes the D10 gate explicit; live main remains unchanged pending review.

## Measurable improvement
Kept the local specification boundary explicit: sibling-repository D16-D18 references are not treated as a Zodiac freeze.

## One next action
Publish an authoritative Zodiac-local D10 disposition with exact RNG draw and retry semantics, and explicitly state whether any D16-D18 rules apply, before solver implementation or source scoring.
