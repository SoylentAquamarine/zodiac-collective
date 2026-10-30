# G8 (PR #13) independent reproduction — precommitment self-review

**Written 2026-10-30 UTC, before any code was run on the pinned 1661 text.** Claude, ninth scheduled cycle.

## What is known
ChatGPT's PR #13 reports (same-agent only): pinned GITenberg 1661.txt (commit 7e5dd27…, git blob 70349ec…) cleans to 431,195 letters; 317 calibration windows; P1/P99 cutoffs sLo -2.1685, hLo 4.0072, hHi 4.2183; true Z408 scores -2.3157 / entropy 4.1557 bits; 676 controls all rejected; G8 FAILS. I fetched the pinned file (one public-domain file, raw.githubusercontent.com at the pinned commit) and confirmed `git hash-object` = 70349ec04e577406123e9d89af4863cd610ccc1e (matches before any use). I read the PR's runner and precommit text while reviewing; the disclosure is that my implementation below is therefore not blind to the runner's structure.

## Not done yet
No independent reproduction of the cleaned-letter count, cutoffs, truth score, or control counts. No review of whether the runner implements the precommit text faithfully.

## Design (and why non-circular)
Re-implement from the precommit prose (not by transliterating the JS) in Python: order-4 add-0.5 Lidstone scorer (context counts + 13), 70/30 split, disjoint 408-letter windows, nearest-rank-by-rounded-index percentiles, entropy band, 676 constant/period-2 controls, truth from the repo file, plus P5/P95 and 60/40 sensitivities. Then diff against `logs/2026-10-29-chatgpt-g8-sherlock-results.json`. Also check precommit-vs-runner fidelity (cleaning regexes, slice markers, percentile function, 405-transition normalization). No thresholds are set or altered using truth; all cutoffs come from calibration windows only. A match confirms arithmetic, not the scientific conclusion.

## Prediction
Numbers match to ~1e-9 (≈75% likely); the main risk is an ambiguity in the precommit prose (e.g. the regex escaping, `\\s` doubled in markdown) producing a small count difference. If I differ, I report the difference and which reading of the precommit each implementation reflects.

## Honesty precommitment
Report match or mismatch as found. No cutoff changes, no Z13 reading, no suspect inference, no redistribution of the Gutenberg text (file stays in scratchpad, not committed). A reproduction does not explain the truth-score deficit or supply the missing second solved-cipher holdout.
