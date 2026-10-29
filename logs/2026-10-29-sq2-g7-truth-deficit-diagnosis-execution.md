# SQ-2 — G7 Z408 truth-deficit diagnosis — execution

**Date:** 2026-10-29 (fifth scheduled cycle). Precommit `logs/2026-10-29-sq2-g7-truth-deficit-diagnosis-selfreview.md` committed before running. Script `data/scripts/sq2_g7_truth_deficit_diagnosis.js`; output `logs/2026-10-29-sq2-g7-results.json`. Same model/corpus/70-30 split as G6.

## Results
- **D1 (8 truth chunks of 51 letters vs 51-letter held-out P&P chunks):** every chunk has s between -2.11 and -2.57 against a K median far higher; all 8 sit at or below the 8.2th percentile of K chunks, 7/8 at or below the 4th percentile, and 3/8 (chunks 2, 4, 7) fall below the K-P1 cutoff (-2.321). The deficit is spread across the whole text, not confined to one region.
- **D2 (drop final 18 letters `EBEORIETEMETHHPITI`):** s rises only from -2.286 to -2.230 (+0.056 nats), still below the 390-letter K-P1 (-2.037) and below every K 390-letter window (percentile 0). The known garbage tail explains about a fifth of the 0.24-nat gap, no more.
- **D3 (register control, P&P only):** quoted speech scores 0.088 nats lower than narrative (mean -1.856 vs -1.768), i.e. register moves s by under 0.1, but truth is ~0.43 below the all-K window mean (-1.82), so register as measured by quoted-vs-narrative P&P cannot account for most of it.

## Prediction check
Predicted most of the deficit is localized (misspellings/tail) rather than uniform; D2 gain >= 0.08 (65%): **wrong** (+0.056), and D1 shows a diffuse deficit, so the "localized" half is contradicted. Predicted register shift < 0.1: correct (0.088), though close to the line.

## Interpretation (scoped)
What is established: truth's low score is broad, not a single-region artifact; the garbage tail and a quoted-speech register shift together account for well under half of the gap. What is NOT established: the remaining cause. Untested candidates: lexical/topic mismatch (killing, slaves, paradise vs. 1813 courtship vocabulary), spelling errors scattered through the text, and single-novel training size. A repaired gate would need training text chosen without Z408 truth and a new precommit. No claim about Z13. No suspect inference. Nothing promoted to the site.
