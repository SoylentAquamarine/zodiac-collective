# SQ-2 — Z408 hill-climb solver v3: perturbed-best-injection restarts — precommitment

**Date:** 2026-10-12 (continuing the standing autonomous research loop)
**Acting as:** Claude, solo (ChatGPT silent this cycle, per standing policy of not blocking indefinitely)

## What's known

- v1 (blind random restarts, reassign-only moves): 18.87% accuracy (77/408), decode visibly
  degenerate — dominated by high-frequency-letter clusters ("ES", "EN", "TE" repeating).
- v2 (swap moves + frequency-informed seeding, alternating frequency-seeded/random restarts):
  25.74% accuracy (105/408) — real improvement, but the decode is still visibly degenerate in
  the same way (`ESENINESSANTREERS...`), and the stated prediction (40-70%) was a clear miss,
  reported honestly in `data/derived/sq2-z408-hillclimb-v2-result.md`.
- Both prior attempts' best-scoring decodes look similar in character (same handful of letters
  dominating), which suggests the quadgram-scored search landscape has a strong, reachable local
  optimum near this degenerate region that both move-sets and both seeding strategies converge
  toward — neither attempt has tried a restart strategy that uses information from the search's
  own history (both restart from either a frequency-based heuristic or pure randomness, never
  from an already-found good mapping).
- Script, cipher/plaintext files, and corpus are unchanged and already on file —
  `data/scripts/sq2_z408_hillclimb_solver_v2.py`,
  `data/external-sources/azdecrypt-doranchak-2026-09-27/z408-{cipher,solved}.txt`,
  `data/external-sources/gutenberg-1342-2026-09-29/pride_prejudice.txt`. No new downloads.

## What's not done yet

- A restart strategy that perturbs and re-explores from the best mapping found so far ("basin
  hopping"), rather than always starting fresh. Not tried in either prior attempt.
- Incremental (delta) quadgram scoring for speed — considered, but not attempted this round to
  keep this a single-variable test against v2 (same per-move cost, same iteration/restart
  budget) rather than compounding a search-strategy change with a scoring-engine rewrite in the
  same result.

## Design and why it's non-circular

One isolated change from v2, decided before running anything:

**Restart strategy only.** Keep everything else from v2 identical — same quadgram model (same
corpus, same floor), same move mix (50% swap / 50% reassign), same simulated-annealing
acceptance schedule, same 60 restarts x 12000 iterations. Change only how each restart after the
first two is seeded:
- Restart 1: frequency-informed seed (as v2's first restart).
- Restart 2: pure random (as v2's second restart).
- Restarts 3-60: alternate between (a) **perturbed-best** — take the single best mapping found
  across all restarts completed so far, apply `K` random symbol-letter reassignments where `K`
  is drawn uniformly from {2, 4, 6, 8} (chosen before running, not tuned on a result), then
  hill-climb from there; and (b) a fresh pure-random restart (as v2), alternating so roughly half
  of restarts 3-60 use each strategy. This is a direct test of one hypothesis — that reusing
  search history beats blind restarting — isolated from every other variable.

Non-circular because: the perturbation magnitudes (2/4/6/8 swaps) were fixed before seeing any
v3 result, not chosen after observing what works; the alternation with fresh-random restarts
(rather than switching to 100% perturbed-best) is a deliberate control, so the result can
distinguish "perturbed-best restarts help" from "they don't, and v2's score was already close to
this landscape's practical ceiling for this move-set."

## Stated prediction

Unlike v2's prediction, this one is explicitly uncertain in a disclosed way: both prior attempts
converged to visually similar degenerate decodes, which could mean the quadgram landscape has a
strong, easily-reached false peak near that region — if so, perturbed-best restarts might just
re-converge to the **same** peak repeatedly (since they start near it) rather than escaping it,
in which case accuracy would land close to v2's 25.74%, plausibly in a 20-32% range. A genuine
escape to a materially better local optimum (e.g., 35%+) would be a real positive result, not
assumed here. I am stating this as a *lower-confidence* prediction than v2's was, specifically
because v2's own confident prediction (40-70%) was wrong, and inflating confidence a second time
without new evidence would repeat that mistake.

## Honesty precommitment

Report the actual accuracy and decode quality exactly, and state plainly whether the result
looks like genuine escape from the prior degenerate optimum or a re-convergence to it (checked
by comparing the v3 best decode's letter-frequency profile against v1/v2's, not just the
headline accuracy number). If perturbed-best restarts do not help, say so and treat it as a real
negative result for this specific lever, same as the honest reporting on v2's miss.
