# G8 (PR #13) independent reproduction — execution

**Date:** 2026-10-30 UTC. Follows [self-review](2026-10-30-g8-pr13-independent-reproduction-selfreview.md) (written before any run). Runner: `data/scripts/claude_g8_independent_repro.py` (Python, written from the precommit prose; run `python3 -I … /path/to/1661.txt` from repo root). Output: `2026-10-30-g8-pr13-independent-reproduction-results.json`.

## Result: exact reproduction (prediction confirmed)
- Pinned 1661.txt fetched at commit 7e5dd27…; `git hash-object` = 70349ec04e577406123e9d89af4863cd610ccc1e (matches). Text not committed.
- Retained letters **431,195**; 317 windows (60/40: 422). Cutoffs match PR #13 to ≤1e-15 (only float-summation noise in the last digit): sLo -2.1685238, sHi -1.7996990, hLo 4.0071984, hHi 4.2183430.
- True Z408: score **-2.3156902** (fails score axis), entropy **4.15567** bits (passes). 60/40 truth score -2.3260706.
- Controls: 0 of 676 accepted; 674 fail both axes, 2 pass the score band but fail entropy (matches PR #13: "entropy only"). 20 seeded shuffles of truth: 0 typical.
- P5/P95 and 60/40 sensitivities: FAIL, matching PR #13.
- Precommit-vs-runner fidelity: the JS runner's cleaning regexes, slice markers, 405-transition mean, add-0.5/+13 smoothing, rounded-index percentile and window tiling all agree with the precommit text. One cosmetic note: the JSON key `G6` is a reused name for the G8 verdict (already disclosed by ChatGPT).

## Caveats
My implementation is independent in code but not blind: I read the runner while reviewing. Shuffle seeds differ from PR #13's (mulberry32), but both give 0/20, so only the qualitative result is comparable. This confirms arithmetic only: it does not explain the diffuse truth-score deficit, show other corpora fail, or supply the missing second solved-cipher holdout. No Z13 reading, no suspect inference, no cutoff changes. Recommendation: PR #13 can be promoted as a verified negative result; any repair of the gate needs a new precommit, not a cutoff tweak.
