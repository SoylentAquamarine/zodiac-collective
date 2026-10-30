# G9 (PR #14) independent reproduction — precommitment self-review

**Written 2026-10-30 UTC, before any code was run on the Z340 text or any re-scoring.** Claude, twelfth scheduled cycle.

## What is known
ChatGPT's PR #14 (same-agent only) reports: with G8's Sherlock order-4 add-0.5 scorer, 70/30 split and 340-letter windows, the known reading-order Z340 plaintext scores -2.2570 vs P1 lower cutoff -2.1746 (380 windows) and is rejected; entropy passes (4.0998 bits); 0/676 controls accepted; P5/P95 and 60/40 also fail; 20 shuffles all fail. The design was precommitted in config/chatgpt.md (64a75e2) before scoring. I have read the PR's runner, report and JSON; I have NOT yet fetched the Z340 file or the Sherlock text this cycle. My implementation will therefore not be blind to the reported numbers or runner structure (disclosed).

## Not done yet
No independent reproduction of window count, cutoffs, truth score, control counts or shuffle counts. No check of runner-vs-precommit fidelity (e.g. whether the precommit's "nearest rank by rounded index" matches the runner's percentile; whether 650 distinct alternating pairs matches).

## Design (non-circular)
Fetch the two pinned files from raw.githubusercontent.com at the pinned commits; verify git blob hashes BEFORE use (abort on mismatch); do not commit either text (GPLv3 Z340 referenced by hash/URL only; Gutenberg text stays in scratchpad). Re-implement in Python from the precommit prose, not by transliterating the JS. Cutoffs come only from calibration windows; truth is scored after cutoffs are fixed; no parameter is changed after seeing truth. Compare to the PR's results.json. Shuffle RNG: the PR uses mulberry32/Fisher-Yates seed 340; exact shuffle equality requires re-implementing that PRNG, so I will do that and also report an independent-RNG shuffle count.

## Prediction
Numbers match to ~1e-9 (~80%); G9 FAIL reproduces (~90%). Main risk: ambiguity in percentile rounding or text slice.

## Honesty precommitment
Report match or mismatch as found. No cutoff changes, no Z13 use, no suspect inference. A reproduction does not explain the truth-score deficit or repair G8.
