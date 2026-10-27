# SQ-2 — frozen score spec + gate table — execution

Precommitment: `logs/2026-10-27-sq2-frozen-score-spec-gate-selfreview.md` (written before running). Script `data/scripts/sq2_frozen_score_spec_gate.py`; output `data/derived/sq2-frozen-score-spec-gate-output.txt`. Post-hoc sensitivity (labeled as such, not part of the frozen spec): `data/derived/sq2-frozen-score-spec-gate-posthoc-output.txt`.

## Gate table (frozen formula F: order-4, add-0.5 Lidstone, Pride & Prejudice marker-bounded corpus, 563,955 letters)

| Gate | Result | Detail |
|---|---|---|
| G1 truth > v3 and v4 | **PASS** | truth -907.0, v3 -993.9, v4 -1077.8 nats (per letter -2.223 / -2.436 / -2.642) |
| G2 truth wins >=3 of 4 fixed 102-letter windows vs v3 | **PASS (4/4)** | windows: -212.7/-229.3, -222.7/-246.5, -227.8/-236.4, -232.6/-265.5 |
| G3 truth beats 20 seeded letter-shuffles | **PASS (20/20)** | seed 408 |
| G4 costliest truth quadgrams (diagnostic) | n/a | 25 truth quadgrams unseen in corpus (v3: 24); costliest are the writer's irregularities: THAE, EMOA, IKEK, FEEB, FORR... |

## Prediction check
My stated prediction (G1 and G2 FAIL, G3 pass, G4 misspelling-driven) was **wrong** on G1 and G2: they pass. G3 and the G4 reading held.

## Post-hoc sensitivity (not frozen, labeled)
Same corpus: order 1-3 Lidstone still favor v3 (truth -1200.6/-1060.6/-975.0 vs v3 -997.7/-902.1/-934.6); the solver's own quadgram model (0.01/total floor) on this corpus also favors v3 (-4164.7 vs -3873.3), while order-4 Lidstone favors truth. So the earlier order-4 failure is largely a smoothing-floor effect (25 unseen quadgrams each punished by the flat floor), not evidence that quadgram statistics cannot rank the true text first. Orders 1-3 failing is a separate unresolved matter (v3 is optimized to English-like low-order statistics; truth carries the writer's irregular spellings).

## Caveats (important)
- One corpus, one cipher, one formula; v3/v4 were produced under the floor-quadgram model, not F, so they are not adversarial to F. A fair known-answer test needs wrong decodes produced by a search against F, which means new solver compute — NOT done and not recommended yet.
- The held-out gate here is within-Z408 windows only. No second solved cipher plaintext in readable order is on file (`z340-solved-transposed.txt` is in cipher order; Z32 unsolved), so ChatGPT's "held-out solved-cipher" gate is NOT satisfied; marked open.
- Does not read or constrain Z13; no suspect inference.

## Disposition
Gate G1/G2/G3 pass under F, so the prior "failed scoring control" verdict should be scoped to the repo's floor-smoothed quadgram objective and to orders 1-3, not to order-4 Lidstone. Recommended next step (unclaimed): decide whether to run ONE solver search against F on Z408 (known answer) as the final gate before any Z13 work; needs ChatGPT/user agreement given the "no solver compute before a passing control" rule — this spec passes the control, but the held-out-cipher gate is still open.
