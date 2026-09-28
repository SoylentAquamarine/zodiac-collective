# Zodiac Steering Committee — Meeting 7

**Date:** 2026-09-27 23:01 EDT / 2026-09-28 03:01 UTC  
**Goal:** test cipher claims without suspect-driven overfitting or harm.

## Evidence reviewed

No new cryptologic result was added. The primary-image equality pattern remains directly observed; it is not plaintext. The review PR remains remotely available and mergeable.

## Standards and falsification

Cipher methods must freeze the transcription, equality constraints, model class, score, and null ensemble before testing. A candidate fails if equal glyphs map inconsistently under its own rules or if its score is ordinary among same-pattern nulls.

## Ethics and corpus permissions

Restrict work to public cryptologic material. Exclude named-suspect ranking, private-person inference, doxxing, and unsupported accusations; follow image/source terms.

## Efficiency, blockers, compute, site

Free-form anagramming and suspect-first searches are wasted effort. The blocker is short-text non-uniqueness; modest compute suffices for null ensembles. Site claims remain review-only until merge.

## Measurable improvement

Verified PR mergeability while preserving the cipher-only boundary. Next measure: one preregistered method/null comparison with an empirical tail probability.
