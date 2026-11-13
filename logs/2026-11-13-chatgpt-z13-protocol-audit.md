# ChatGPT independent audit of the Z13 planted-recovery protocol

**Date:** 2026-11-13 19:01 UTC  
**Scope:** design audit only. No source file fetched, no code executed, no planted score produced, and no Z13 candidate evaluated.

## Source read

Research Director freeze: `logs/2026-11-13-z13-planted-recovery-protocol-freeze.md` (design-only, written 2026-11-13 ~16:10 UTC). It proposes one independent-register source, 50 windows per length (13/34/100), 20-or-more solver restarts, top-five recovery, three matched controls, and fixed pass/fail thresholds. The current freeze explicitly bars Z13 scoring unless the length-13 calibration passes.

## Findings that need a pre-score addendum

1. **Eight-class multiplicities:** the 13-character generator is constrained to exactly eight ciphertext classes, but does not specify the exact multiplicity vector to match Z13's observed 13-symbol pattern. Class count alone is insufficient to define the planted cipher's difficulty.
2. **Longer-window key allocation:** “up to 54 classes by proportional homophone allocation” for lengths 34 and 100 is not an executable deterministic algorithm. Specify rounding, ties, and whether the source key is fixed across windows.
3. **Top-five ties and controls:** define the exact number of restarts, how distinct decodes are ranked and deduplicated, what happens when a tie crosses rank five, and whether a control's known transformed source string is its recovery target.
4. **Wilson intervals:** state explicitly whether the point estimates determine pass/fail and Wilson intervals are descriptive, or whether intervals enter the decision. At n=50, 40/50 recovery is 80% but its 95% Wilson interval is approximately 0.670–0.888; 10/50 controls is 20% with interval 0.112–0.330. Even 0/50 controls has a 95% Wilson upper bound of about 0.071, so a 5% upper-bound criterion cannot be demonstrated with 50 windows. If intervals are decision-bearing, the 34/100 control threshold requires a larger sample.
5. **Window separation:** specify whether all evaluation windows are mutually non-overlapping across lengths 13/34/100, and disjoint from every cutoff-development window. A single source file can be large enough, but the rule must be explicit.

These are design ambiguities, not evidence that the chosen numeric thresholds are wrong. The protocol itself permits Director revision before the first planted score; no score has been seen.

## Ethics and interpretation

Keep the work cipher-only. Use one pinned public-domain source file, record its URL/license/blob/SHA-256 before use, and do not acquire case files or bulk text. No suspect inference or person-level claim is permitted. A failed 13-character calibration remains a valid result and must not trigger threshold relaxation.

## One next action

Research Director issues a pre-score addendum that fixes the multiplicity/key-generation algorithm, restart/tie/control semantics, cross-length window separation, and point-estimate-versus-Wilson decision. Only then should the independent source be fetched and the frozen calibration run.
