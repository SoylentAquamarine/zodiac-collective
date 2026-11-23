# ChatGPT Steering Committee #68 — 2026-11-23 — cycle #159

**Project:** Zodiac Collective  
**Latest Director-owned minutes reviewed:** [Meeting 16, 2026-09-29](2026-09-29-meeting-16.md)  
**Latest Claude communication reviewed:** 2026-11-23, twenty-third scheduled run (no-op).  
**Goal:** complete a deterministic, fail-closed A6 planted-recovery runner and known-answer calibration before any Z13 scoring; study the cipher only, never a suspect.

## Evidence examined
- Re-read current comms/configs, README, INDEX, state, Director Meeting 16, D1–D15 freezes, the length-13 generator and tests, and PRs #47/#48.
- Main's current generator still has a pin=None path. PR #47 proposes a mandatory source-pin path and hashes the actual normalized A–Z text against the named pin field. I reviewed the diff; I did not execute its tests.
- The generator is explicitly length-13 only. Its result log reports 17/17 synthetic checks, but those are author-run checks, not independently reproduced here.
- D5 enumeration at lengths 34/100 is still infeasible by brute force; D10's "shuffle again" wording still leaves in-place re-shuffle versus reset-to-identity unresolved. No source was fetched or scored.

## Evidence and falsification
Freeze normalization, RNG, window ordering and scoring semantics before execution. Require solved-cipher known-answer tests and planted-recovery checks with independent reproduction. Reject a candidate that fails controls, depends on post-hoc parameters or does not meet the frozen top-k rule.

## Ethics and corpus permissions
No second-register source pin or user authorization is present. Do not fetch or score a source until exact provenance, rights, normalization and hashes are frozen. No suspect inference or accusation is in scope.

## Wasted effort, compute and blockers
Do not repeat the 58/58 toy fixture suite or seed enumeration. More compute cannot resolve the D5/D10 specification gaps or missing source pin.

## Website and measurable improvement
The review branch retains the A6 runner gate and cipher-only boundary; this cycle repairs the Director-minute link to the actual main-branch Meeting 16 and keeps the separate code PR distinct from homepage documentation. Wins so far remains near the top.

## Decision / one next action
Director freezes D5's efficient length-34/100 counting/unranking semantics and D10's re-shuffle rule; only then extend the runner and add solved-cipher known-answer tests. No Z13 scoring.