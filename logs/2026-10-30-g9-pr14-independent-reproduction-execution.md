# G9 (PR #14) independent reproduction — execution

**2026-10-30 UTC.** Precommitted self-review: `logs/2026-10-30-g9-pr14-independent-reproduction-selfreview.md` (written before any code ran).

Pinned inputs fetched from raw.githubusercontent.com and hash-verified before use: Sherlock 1661.txt (GITenberg commit 7e5dd27…, blob 70349ec… — match; note a first guess at the repo name 404'd, the correct repo is `The-Adventures-of-Sherlock-Holmes_1661`), Z340 reading-order solved text (doranchak/azdecrypt 3f3e1f1…, blob 74aa9b7… — match). Neither text is committed.

Python re-implementation (`data/scripts/g9_z340_independent_reproduction.py`, from the precommit prose, numpy; mulberry32 shuffle ported). Output: `logs/2026-10-30-g9-pr14-independent-reproduction-results.json`.

## Result: exact reproduction
- 431,195 cleaned letters; 380 windows (70/30), 507 (60/40) — match.
- Primary cutoffs sLo -2.1746166250, sHi -1.7887568984, hLo 3.98184, hHi 4.22584 — match to ~1e-14.
- Z340 score -2.2570356879 (< sLo, fails), entropy 4.0998113841 (passes). P5/P95 and 60/40 also fail (-2.2727789417 vs -2.1964793429).
- 0/676 controls accepted in all three settings; 20 seeded shuffles: 0 typical, 0 score-OK, 20 entropy-OK — match. G9 = FAIL.

Prediction (match ~80%, FAIL ~90%): confirmed. Fidelity: the runner's percentile rule (round-half-up index) and cleaning matched the precommit prose; no ambiguity found. Caveat (disclosed): not blind to the runner structure.

## Interpretation (limited)
The typicality filter rejects a second, shorter known-true Zodiac plaintext on the score axis, with truth at -2.257 vs cutoff -2.175 (deficit ~0.08 nats, smaller than Z408's ~0.15). The Sherlock-trained gate therefore cannot validate/accept known Zodiac text; it is not usable on Z13. Same author/case, so this is not an independent-register test and does not diagnose the cause (abbreviations/misspellings/register remain candidates). No suspect inference.
