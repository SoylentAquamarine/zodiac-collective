# Independent D5/D6/D7 fixture reproduction — 2026-11-22

**Source script:** `data/scripts/d5_d6_d7_fixture_check.py`  
**Source blob:** `4a12f803427cdc61afd0decf2ed261824a4a99be`  
**Reference result:** `logs/2026-11-21-d5-d6-d7-fixtures-result.md`

## Checks reproduced
- F5-1: exactly two feasible partitions and the frozen lexicographic order — PASS.
- F5-2: exactly one feasible split — PASS.
- F5-3: infeasible split returns an empty set — PASS.
- F6: occurrence assignment preserves the occurrence set for seeds 0–49; the three named hand checks, single-group assignment and determinism check pass — PASS.
- F7: a forced-B unigram distribution yields only BBBB for 100 seeds; generated strings preserve length and alphabet — PASS.

All 11 named assertions passed. The 50-seed property check is additional to those named assertions.

## Boundary
This is an independent reimplementation of the committed fixture logic, not execution of a production A6 runner. The A6 freeze remains design-only; the source-pin gate is unfilled, no planted or Z13 scoring occurred, and no suspect inference is permitted. The N=0 fail-closed behavior must be implemented in the real runner, not inferred from this toy helper.
