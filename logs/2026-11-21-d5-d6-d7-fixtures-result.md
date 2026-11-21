# Result — D5/D6/D7 fixtures (2026-11-21); precommit `2026-11-21-d5-d6-d7-fixtures-precommit.md`
Hand-value file `2026-11-21-d5-d6-d7-fixtures.md` (SHA-256 bbb2a5cb...e66e9e) was fixed and hashed BEFORE `data/scripts/d5_d6_d7_fixture_check.py` existed. All checks PASS (F5-1 N=2 ordered; F5-2 N=1; F5-3 N=0; F6 structural invariants and determinism; F7 forced "BBBB" for 100 seeds, length/alphabet). Prediction (all reproduce) held.
Machine-computed, NOT hand-computed: seed 20261113 gives F6 A-groups [[1],[0]] and C3 "BCBCAAAA" (len 8, weights 1/2/3); these pin stdlib `random` behaviour only.
## Disclosed findings
1. D5 tuple representation is ambiguous in the A6 text; I fixed one reading (per-letter descending partitions, lexicographic tuple order). The Director must confirm or re-freeze; the fixtures are valid only under that reading.
2. D6 "occurrence-index list" is ambiguous (positions within the window vs index within the letter's occurrences). The fixture file says relative; the checker returns window positions (B group [2,3]). Not a numeric conflict in the passing checks but must be pinned.
3. F5-3 (N=0) shows the runner needs an explicit infeasible-split abort path; A6 does not say what happens.
4. Fixtures are spec-level: no runner exists, so assertion 7 is NOT yet discharged for the real runner. Source-pin gate unchanged (UNFILLED); no scoring, no Z13 reading, cipher-only.
