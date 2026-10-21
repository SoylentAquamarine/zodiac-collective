# SQ-2 — Z408 solver v4 (unigram-KL penalty) — execution

Precommitment: `logs/2026-10-21-sq2-z408-v4-unigram-penalty-selfreview.md` (written before any code ran).
Script: `data/scripts/sq2_z408_hillclimb_solver_v4.py`; result: `data/derived/sq2-z408-hillclimb-v4-result.md`.

## Result: **10.29% accuracy (42/408)** — worse than v1 (18.87%), v2 (25.74%), v3 (30.64%)
Stated prediction (35-60% likely, ~35% chance of 25-35%) was **wrong, and below even the low
end of the disclosed range**. The penalty did what it was designed to do on its narrow target —
top letter E fell from 36.8% (v3) to 28.4%, top-5 now E .284, T .194, S .142, N .083, R .066 — but
E is still >2x English's ~12.7% and the decode remains degenerate ("ESONENETSASESHTHTO...").
Accuracy fell, so reducing single-letter overconcentration was not the binding lever.

## Post-hoc diagnostic (NOT precommitted; disclosed as exploratory)
`data/scripts/sq2_z408_objective_vs_search_diagnostic.py` scores the true plaintext vs the v3/v4
decodes (known plaintext used only for this diagnostic, after all runs):

| text | quadgram-only | v4 objective |
|---|---|---|
| true plaintext | -4164.7 | -4190.1 |
| v3 decode | -3873.3 | -4161.6 |
| v4 decode | -4114.3 | -4285.7 |

Two separable findings:
1. **Objective failure (v1-v3):** under the quadgram-only objective the degenerate v3 decode scores
   ~291 nats *higher* than the true plaintext, so more/better search under that objective would not
   find the answer. Even with the unigram penalty, v3's decode (-4161.6) still outscores the truth
   (-4190.1). Plausible contributors (not isolated): a single-novel 1813 corpus is a poor
   model for Z408's text (misspellings like "PARADICE", "EXPERENCE"), and quadgram stats over ~700 repeated
   E/T/R/H/S words are cheap to score highly.
2. **Search failure (v4 specifically):** v4's found score (-4285.7) is below both v3's decode and the
   truth under its own objective, so v4's search did not even reach the best point of its own
   landscape; the penalty rescaled the objective while the annealing temperature (4.0, tuned
   implicitly for quadgram-only deltas) was left unchanged, plausibly causing the chain to stick (best score
   unchanged from restart ~41 on). Temperature interaction was not tested.

## Caveats
Single run, single lambda, single seed; the diagnostic uses one decode per version. The
"objective failure" claim rests on the true plaintext's own score being lower — robust to search
noise, but dependent on the specific corpus/model.

## Proposed next step (needs fresh precommitment)
Fix the objective before the search: a larger/closer-register reference corpus or a word-level
model (more than one novel; period-appropriate text) so the truth outscores degenerate decodes —
verified first by the same truth-vs-decode score comparison, *before* spending search budget. Adding
further corpus sources needs checking the standing no-bulk-download rule (small public-domain texts
only, individually fetched).
