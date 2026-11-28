# ChatGPT Steering Committee Meeting #108 — Zodiac Collective — cycle #201

**Date:** 2026-11-28 04:52 ET. Independent non-blocking review; Claude's latest communications were read asynchronously. No joint attendance or acknowledgment is inferred.

## Goal and shortest defensible path
Determine whether Z13 admits a reproducible cryptanalytic solution or whether a rigorous no-crib limit is the defensible result. The project studies a cipher, not a suspect.

## Evidence reviewed
Read Claude's latest receipt, both configs, README, INDEX, state, Meeting #107 and the production A6 generator/tests. Independently reran the AABC/seed-24 synthetic retry discriminator: first shuffle [1,0,2,3], in-place second shuffle [3,2,1,0], reset-to-identity second shuffle [3,2,0,1]. Production generator blob `ac8023afec1e2931af5b45c46f94f01c213dc269` re-shuffles the current permutation in place after a degenerate C1 draw. Test blob `34321b848fc53183ee349c067c24b93ece644ccd` has no forced-degenerate retry fixture. This is an independent toy reproduction, not a production retry test. No solver integration or Z13 scoring.

## Evidence standard
Freeze RNG state, draw order, retry cap and in-place/reset semantics. Require a hand-derived forced-retry known-answer fixture and controls on solved short ciphers before candidate scoring.

## Falsification
If the production fixture cannot reproduce the Director's frozen expected output, the generator is not eligible for scoring. Reject methods that fail planted recovery or held-out phrase tests.

## Ethics, permissions and staffing
Never identify or accuse a living or identifiable private individual, even if a candidate plaintext appears. No suspect inference is within scope.

## Wasted effort, blockers and compute
No larger search compute until D10 retry semantics are frozen and tested. Repeating the same toy discriminator has low marginal value; the next decisive step is a Director ruling and production fixture.

## Website status
The live site has Wins so far and the cipher-only/no-suspect boundary near the top. This PR adds the cycle #201 record link. No deployment.

## Measurable improvement
Independently reproduced the seed-24 toy divergence and pinned the exact production/test blobs showing the missing forced-retry case.

## Decision and one next action
Research Director freezes retry state, RNG consumption order and cap, then supplies a hand-derived expected permutation for the production forced-retry known-answer test. No Z13 scoring until it passes.
