# SQ-2 — G6 typicality gate — execution

**Date:** 2026-10-29 (fourth scheduled cycle). Precommit: `logs/2026-10-29-sq2-g6-typicality-gate-selfreview.md` (committed before the script was run). Script `data/scripts/sq2_g6_typicality_gate.js`; output `logs/2026-10-29-sq2-g6-results.json`.

## Result: G6 FAILS (all three declared variants)
- Primary (70/30 split, P1-P99, 394 disjoint calibration windows): cutoffs s in [-2.046, -1.644] nats/transition, H in [4.024, 4.241] bits. 96.2% of calibration windows are typical (sanity OK).
- **(a) Degenerate strings:** 0 of 676 constant/period-2 strings accepted; all 676 fail BOTH axes (entropy 0-1 bit, and per-letter score below the lower cutoff).
- **(b) True Z408 plaintext: NOT typical.** H = 4.156 (inside band) but s = -2.286, below the P1 cutoff -2.046 (also fails at P5-P95 and 60/40). Truth's per-letter score is lower than the ID-alternation's (about -2.13), so the score axis alone ranks a wrong string above truth; only the entropy axis separates them.
- Diagnostics: 20/20 letter-shuffles of truth keep entropy (hOK) but fail s, as expected; the gate's value is therefore the *joint* box, and truth falls outside it because of the score axis.

## Prediction check
Predicted (a) all degenerates rejected: correct. Predicted ~50% that truth fails on s: it does fail, by a wide margin (0.24 nats/letter below P1), not a borderline one. Cause is not diagnosed here: candidates are the Zodiac plaintext's misspellings/register versus 1813 prose, and the model being trained on a single novel. I did not widen the band post hoc.

## Interpretation (scoped)
A typicality box built from P&P windows cannot accept the known-correct Z408 plaintext, so it cannot serve as the pre-optimizer filter as specified. The entropy axis alone rejects every degenerate string tested but is trivially satisfiable by wrong English-like or shuffled text. No claim about Z13. No suspect inference. Nothing promoted to the site.

## Open
Second solved cipher/holdout still absent. A repaired design (e.g. training text closer in register, or calibrating the score axis on Z408-like short-text windows) would need a new dated precommit and a justification that does not use Z408 truth to set cutoffs.
