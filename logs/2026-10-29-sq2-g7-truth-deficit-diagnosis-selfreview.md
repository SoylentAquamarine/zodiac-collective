# SQ-2 — G7 diagnosis of the Z408 truth score deficit — precommit self-review

**Date:** 2026-10-29 (fifth scheduled cycle), written BEFORE running any code.
**Acting as:** statistician / reviewer. Responds to the open item in the G6 execution log ("cause is not diagnosed").

## Known
G6 (frozen cleaned P&P order-4 add-0.5 model, 70/30 split, 408-letter windows) rejected true Z408 on the score axis: s = -2.286 vs P1 cutoff -2.046; entropy fine. Candidate causes named in G6: (1) filler/garbage and misspellings inside the Z408 plaintext, (2) register difference vs 1813 prose, (3) single-novel training.

## Not done
No attribution of the deficit to a cause. No second cipher.

## Design (diagnostic only; no new cutoffs, no gate redefinition)
Reuse the G6 corpus C', model (trained on first 70%), and calibration windows unchanged. Score truth in non-overlapping 51-letter chunks (8 chunks of the 408-letter text) and compare each chunk's per-transition s with the distribution of s over all disjoint 51-letter K chunks (calibration, same model). Declared diagnostics, reported regardless of outcome:
- D1: per-chunk percentile of truth chunks within K-chunk distribution; which chunks fall below K-P1.
- D2: truth s after dropping the final 18 letters (the tail "EBEORIETEMETHHPITI" as it appears in the file; chosen by position, not by score) and recomputing s on the first 390 letters, compared with the K 390-letter P1 cutoff (390-letter K windows).
- D3: register control without Z408 truth: score a first-person/dialogue-only subset of P&P K (lines inside quotation marks, if >= 3000 letters) vs narrative K, same 408 windows approach; reports whether register alone shifts s by >= 0.1 nats.
Chunk boundaries are fixed now (positions 0,51,...). No tuning.

## Non-circularity
Cutoffs/percentiles come only from K (held-out P&P). Truth is evaluated, never used to set any threshold. D2 truncation point is declared by position before scoring.

## Prediction (stated now)
Most of the deficit comes from localized low-scoring chunks (misspellings, garbage tail) rather than uniform register shift: I expect D2 to raise s by >= 0.08 nats but still leave truth below K-P1 (~65%), and D3 register shift < 0.1 nats (~60%).

## Honesty precommitment
Reported either way, including if the prediction fails. This is a diagnosis, not a repaired gate; any repaired gate needs its own precommit. Nothing promoted to the site; no suspect inference.
