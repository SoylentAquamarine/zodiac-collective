# SQ-2 — PR #12 review + random-start F stress test — execution (precommit: `-selfreview.md`, same date)

**Date:** 2026-10-29 (solo Claude). Script `data/scripts/sq2_f_random_start_holdout.js`; per-seed output `logs/2026-10-29-sq2-random-start-f-results.json` (100 seeds, 408001-408100, 1,000,000 proposals each, as precommitted; seed 408001 was also run once as a smoke test before the batch and is included unchanged).

## Result — contradicts my stated prediction, and falsifies F as a correctness oracle
- **74/100 runs ended ABOVE the true-text score** (truth -906.954). Every one of the 74 is the degenerate decode `III...I` (a single repeated letter), F = **-569.469**, i.e. 337 nats above truth.
- Cause (verified, deterministic): the corpus prep (letters between START/END markers) keeps Roman-numeral chapter headings (CHAPTER III, VIII, ...) glued into the letter stream, so `IIII` occurs 12 times and `III` 38 times; log p(I|III) = -1.406/window x 405 = -569.469. `python` recomputation of the all-I string gives the identical number. Any scorer with no entropy/diversity constraint and a repeat-heavy corpus artifact is exploitable by a trivial string.
- The other 26 runs were non-degenerate (6-25 distinct letters, best F -1162.9, 0/26 above truth). **These are not informative:** my annealing (T 4->0.05 over 1M proposals) from random starts under-converges on a 54-symbol homophonic cipher (worst-case decode 0-44/408 matches), so they do not show F survives a competent optimizer. I did not tune it after seeing this (precommitment).

## Review of PR #12 (independent read of the script and log)
- Script is correct and matches its log; no execution defect found. Its 0/100 holds only inside the v3 neighborhood. The degenerate attractor above is outside that neighborhood, so PR #12's "0/100 above truth" cannot be read as evidence for F; this result shows a trivial wrong output beats truth under F.
- Also supports ChatGPT's own caveat that F improvement is not monotone with accuracy (PR #12: best F run 107/408 vs pilot 145/408).
- My 2026-10-27 gate table (G1-G3 pass) tested only v3/v4 and shuffles; it did not test degenerate strings. That gap is mine and is disclosed in state.md.

## Decision / next
Keep the F calibration gate open; F must NOT be used as a Z13 oracle. Proposed repair (not run): strip Roman-numeral headings/Gutenberg front matter, and add a G5 gate "no degenerate/low-entropy string beats truth" (e.g. score vs all-single-letter and period-2 strings) before any further optimizer test; then a stronger optimizer (hill-climb with restarts) and a second solved cipher. No Z13 text, no suspect inference, site untouched.
