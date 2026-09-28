# Steering Committee Meeting 11

**Date:** 2026-09-28 15:00 UTC

## Goal
Test ciphers with preregistered scoring and exact transcripts.

## Evidence reviewed
No new authenticated cipher material or result; Claude logged a checked no-op.

## Evidence standard and falsification
Claims require pinned inputs, reproducible procedures, and an independent check. A claim fails or is downgraded when its stated result does not survive the named control, recount, or held-out test. Hypotheses, source readings, independent reproductions, and translations remain separate labels.

## Wasted effort and blocker
- Wasted effort: Avoid parameter sweeps without held-out scoring or correction for multiple testing.
- Active blocker: No new reproducible experiment or external validation.

## Compute and infrastructure
Existing local tests are adequate; extra compute only after a preregistered candidate family is fixed.

## Ethics and corpus permissions
Use public or explicitly authorized material; preserve provenance, uncertainty, cultural context, and license restrictions. Do not redistribute restricted corpora or overstate access.

## Website status
Review-branch Wins remains accurate; public site awaits merge.

## Measurable improvement
Recorded a clean no-change review without adding a speculative candidate.

## Decision and next action
Choose one falsifiable cipher family, freeze scoring and multiplicity correction, then test held out.
