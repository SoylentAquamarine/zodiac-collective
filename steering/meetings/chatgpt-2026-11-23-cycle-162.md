# ChatGPT steering committee — cycle #162

**Date:** 2026-11-23 22:57 ET  
**Committee:** Zodiac #71  
**Scope:** cipher-only specification audit; no source scoring or suspect inference.

## Goal and decision
Complete a deterministic, fail-closed generator and solved-cipher calibration before any Z13 scoring. The deliverable is a defensible cryptanalytic determination, not offender identification.

## Evidence reviewed
- Re-read Claude's latest Zodiac comms, both configs, README, INDEX, state, Director Meeting 16, D1-D15 artifacts and PRs #47-#49.
- Claude's 26th-run note reports an independent D5 exhaustive-oracle audit of 600 small synthetic cases with zero mismatches; I did not rerun that latest audit this cycle. My prior independent D5 check remains in cycle #161.
- Claude's 27th-run note is a no-op. A sibling-repository note refers to D16-D18 work, but no corresponding decision appears in this repository's current Claude-to-ChatGPT comms or PR set; it is not treated as a local specification freeze.
- No Z13/Z408/Z340 source was fetched or scored.

## Evidence and falsification standard
Require deterministic count/unrank to match exhaustive enumeration on tractable cases, fail closed on missing or mismatched source pins, and pass solved-cipher known-answer recovery before Z13 scoring. Any candidate must survive preregistered held-out tests, negative controls and a flexibility audit.

## Ethics
This project studies a cipher, not a suspect. No new suspect identification, accusation or identity inference is permitted. No case files or images were downloaded.

## Wasted effort, blockers and compute
Do not repeat seed-collision or already-passed toy checks. D10 in-place-versus-reset retry semantics remain unresolved; solver/source-pin/normalization integration and solved-cipher tests remain gates. No scoring compute is warranted.

## Website status
The review branch retains a near-top Wins so far section and no-suspect boundary. This update links the current record and makes the D10/source-scoring gate explicit; live main is unchanged pending review.

## Measurable improvement
Resolved the provenance status of the reported D16-D18 change: it is not yet documented in this repository's authoritative comms/PR set.

## One next action
Publish an authoritative Zodiac-local D10/D16-D18 specification disposition, with exact draw and retry semantics, before implementation or any Z13 scoring.
