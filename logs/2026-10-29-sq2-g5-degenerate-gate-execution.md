# SQ-2 — G5 degenerate-string gate — execution (precommit: `-selfreview.md`, same date, committed before running)

Script `data/scripts/sq2_g5_degenerate_gate.js`; output `logs/2026-10-29-sq2-g5-results.json`. 676 degenerate strings (26 constant + 650 period-2), length 408, scored with frozen F and cleaned-corpus F' (rule as precommitted; residue check: 0 "CHAPTER", 0 "Illustration"; C' = 536,581 letters vs 563,955).

## Result
| scorer | truth | strings above truth | which | G5 |
|---|---|---|---|---|
| F (frozen) | -906.954 | 5 | I (-569.5), ID, DI, WE, EW | FAIL |
| F' (cleaned) | -908.923 | 4 | ID (-862.2), DI, WE, EW | FAIL |

- Reproduces ChatGPT's 06:00 UTC finding exactly (all-I, ID, DI, WE, EW above truth) and shows it is a complete count over all 676 strings.
- Cleaning removes the constant-string attractor (all-I is no longer above truth under F'), confirming that artifact was corpus-prep, but the four period-2 offenders survive with a margin of 46.7 nats.
- My prediction (F' passes G5 with 0 above truth) was **wrong**.

## Post-hoc diagnostic (labelled post-hoc, not part of the gate)
In C', `IDID` occurs 29x, `DIDI` 19x, `WEWE` 20x (from "I did ...", "we ...we"-type phrasing), so these alternations are real English statistics, not prep artifacts. A bare order-4 likelihood summed over 405 windows rewards repetition of a few high-probability windows; truth is penalised by writer misspellings and by being diverse text.

## Decision / next
G5 stays FAILED for both F and F'; neither may be used as a correctness oracle for a decode or for Z13. Cleaning alone is insufficient. Proposed repair (not run, to be precommitted separately): do not rank by raw likelihood; instead require a decode to have per-letter score and letter-entropy inside the range seen for 408-letter windows of real English (use corpus windows as null), i.e. a typicality gate, and re-run G5 on that; then second solved cipher. No Z13 text, no suspect inference, site untouched.
