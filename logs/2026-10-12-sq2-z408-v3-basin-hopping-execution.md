# SQ-2 — Z408 hill-climb solver v3: perturbed-best-injection restarts — execution

**Date:** 2026-10-12
**Design/prediction frozen first:** `logs/2026-10-12-sq2-z408-v3-basin-hopping-selfreview.md`
**Script:** `data/scripts/sq2_z408_hillclimb_solver_v3.py`
**Full result:** `data/derived/sq2-z408-hillclimb-v3-result.md`

## What was run

Same quadgram model, corpus, move mix (50% swap / 50% reassign), annealing schedule, and
restart/iteration budget (60 restarts x 12000 iterations) as v2. Only the restart-seeding
strategy changed: restarts 3-60 alternate between a fresh random restart (as v2) and a
perturbed-best restart that starts from the single best mapping found so far, with
`K in {2,4,6,8}` (randomly chosen per restart, fixed set decided in advance) symbol-letter
reassignments applied first.

## Result

**Accuracy: 0.3064 (125/408)** — a real improvement over both v1 (0.1887) and v2 (0.2574), and
squarely inside the disclosed-uncertain 20-32% range stated in the precommitment, not the more
optimistic "genuine escape" outcome (35%+) that was also named as possible but not assumed.

**The decode is still visibly degenerate, confirming the "same peak" reading over the "genuine
escape" reading.** The best decode's top-5 letter frequencies are E:0.368, T:0.154, R:0.142,
H:0.130, S:0.123 — E alone covers 36.8% of the decoded text (real English averages ~12.7%), an
even more extreme concentration than v1/v2 showed qualitatively. Per-restart score logging
confirms this directly: perturbed-best restarts' mean best-score and plain-random restarts'
mean best-score (both recorded in the result file) are close to each other, not showing
perturbed-best restarts reliably finding a distinctly better region — consistent with
perturbation-sized moves (2-8 symbol reassignments out of 54) staying within the same basin
most of the time rather than escaping it.

## Interpretation

This is a real, if modest, accuracy gain, but **the precommitment's "re-convergence to the same
degenerate peak" hypothesis is the better-supported reading of what happened**, not "perturbed-
best restarts found a genuinely different, better-structured solution." The quadgram-scored
landscape for this cipher appears to have a strong, broad, easily-reached local-optimum region
centered on heavy E/T/R/H/S overloading that three different restart/seeding strategies (blind
random, frequency-informed, and now perturbed-best) all gravitate toward. Escaping it would
likely need either a fundamentally different move operator (one that actively penalizes extreme
single-letter concentration, not just quadgram likelihood) or a different objective entirely —
neither attempted here.

## Honesty check against precommitment

The stated prediction (20-32% range, with an explicit disclosed possibility of 35%+ "genuine
escape") is met by the actual 30.64% result, landing in the predicted range. Checked the
decode's letter-frequency profile against v1/v2 as precommitted, rather than reporting only the
headline accuracy number — this is what revealed the "same peak" interpretation rather than
"the fix worked." Reporting this as a real but limited improvement, not a breakthrough.

## Proposed next step (not attempted here)

A move operator or auxiliary scoring term that directly penalizes single-letter overconcentration
(e.g., a soft cap or divergence penalty against the reference corpus's own unigram distribution,
added to the quadgram score) is the most direct way to test whether this specific degenerate
basin is avoidable at all with this general search framework — a distinct design, needing its
own fresh precommitment.
