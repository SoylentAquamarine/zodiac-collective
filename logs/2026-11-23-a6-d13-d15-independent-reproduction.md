# A6 D13–D15 independent reproduction — 2026-11-23

## Scope
Read Claude's D13–D15 pre-score addendum and precommit, plus the D1–D8 freeze, D9–D12 addendum, and the committed D5/D6/D7 fixture script. No source was fetched, no cipher generated or scored, and no suspect inference was made.

## Independent checks
- Re-ran the committed D5/D6/D7 fixture logic in CPython 3.13.5: **58/58 assertions passed**.
- Independently enumerated the D9–D10 generator seed schedule for window indices 0–999: 23,001 seed instances, 23,001 unique values, zero collisions.
- Read D13: confirms the fixture's D5 tuple ordering and D6 window-position indices; symbol labels are sampled without replacement as the final draw on the plant/C3 stream.
- Read D14: one register, accepted-window order 13 then 34 then 100, one start-position draw per candidate, zero-buffer overlap rejection, 100,000-candidate cap, accepted indices 0–299.
- Read D15: tie flags are exact-float descriptive diagnostics (internal ranks 1–5; boundary rank ≥6 equals rank 5) and do not affect acceptance.

## Remaining gates
- The second-register source pin is still unfilled. Exact text normalization and normalized-text SHA-256 remain open until that source is named and authorized.
- No production A6 runner exists yet. The 58/58 checks are fixture-level, not runner assertions 1–13 and not solved-cipher known-answer tests.
- No source retrieval, planted run, score, calibration result, or Z13 inference is claimed.

## Decision
The Director-owned D13–D15 specification is now readable and consistent with the existing fixture interpretation. Next: implement the fail-closed production runner and solved-cipher known-answer tests; keep source retrieval/scoring blocked until the exact public-domain second-register source, normalization, hash and user authorization are pinned. No suspect inference.
