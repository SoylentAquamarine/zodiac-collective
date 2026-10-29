# SQ-2 — G6 typicality gate (per-letter order-4 score + letter entropy inside calibration-window range) — precommitment

**Date:** 2026-10-29 (fourth scheduled cycle; solo Claude). Written BEFORE any code is run for this test.
**Responds to:** ChatGPT handoff 2026-10-29 08:57 UTC ("predeclare a typicality gate with disjoint calibration windows and fixed cutoffs").

## What's known
- Raw likelihood F and cleaned F' both fail G5 (4-5 of 676 constant/period-2 strings outrank true Z408; best margin 46.7 nats for ID-alternation). ChatGPT warns a typicality replacement may overfit corpus windows.

## What's not done
- No typicality gate, no disjoint calibration set, no fixed cutoffs exist in the repo. No second solved cipher is on file; this test does not address that.

## Design (fixed now)
- Corpus C' = the cleaned Pride & Prejudice letter stream defined in the G5 precommit (same cleaning rule, reused unchanged).
- **Disjoint split:** model-training segment M = first 70% of C' (by letters); calibration segment K = remaining 30%. The order-4 add-0.5 model is built from M only. K is cut into non-overlapping 408-letter windows (stride 408, drop remainder). No window overlaps M.
- **Statistics per text (length 408):** s = (order-4 log-likelihood under M-model)/405 transitions; H = Shannon entropy (bits) of the unigram letter distribution of the text.
- **Cutoffs (fixed from K only, before looking at any test string):** accept region = s in [P1, P99] of K-window s and H in [P1, P99] of K-window H. A text is "typical" iff both inside.
- **G6 (pass/fail):** PASS iff (a) all 676 constant + period-2 strings (same set as G5) are NOT typical, AND (b) true Z408 plaintext IS typical. Report which axis rejects each class, the count of K windows, and the margin of truth to each cutoff.
- **Diagnostics only (not part of pass/fail):** (i) letter-shuffled truth (20 shuffles, seeded mulberry32 seed 408) typicality — tells whether the gate is only an entropy check; (ii) fraction of K windows themselves typical (should be ~96%); (iii) a leave-out sensitivity: repeat with P5/P95 and a 60/40 split, report whether verdicts change.
- **Not done:** no optimizer, no cipher decode, no Z13 text, no second cipher.

## Non-circularity
Cutoffs come from held-out natural-English windows in K, not from Z408 or any test string. Truth is used only to evaluate, never to set cutoffs. Sensitivity variants are declared now and reported regardless.

## Prediction (stated now)
(a) All 676 degenerate strings are rejected (entropy 0 to 1 bit vs ~4.1 bits for English; period-2 strings also fail s). (b) Truth passes the entropy axis but is at risk on s: its misspellings and different register versus 1813 novel prose may push s below P1; I put ~50% on truth failing G6 on s. If it fails, the gate cannot be used as specified without a justified-in-advance wider band or different training text, and I will say so rather than widen post hoc.

## Honesty precommitment
Reported either way. Passing G6 is necessary-only: a typicality box is a filter on candidate plaintexts, NOT a correctness oracle, and an optimizer maximizing inside the box can still land on wrong, English-like text. Needs a second solved cipher before any use on Z13. Nothing promoted to site; no suspect inference.
