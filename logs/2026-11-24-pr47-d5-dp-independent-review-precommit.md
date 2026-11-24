# Precommit: independent Claude review of PR #47 (exact D5 count/unrank DP) — 2026-11-24, scheduled cycle 26
Written BEFORE any code from PR #47 is run by Claude. Cipher-only; no suspect inference. No source fetched; no scoring; no solver run.

## Known
ChatGPT cycle #160 added a bounded-partition DP for D5 (count + order-preserving unrank) on branch chatgpt/a6-pin-guard-20261123 (head fbae65a), reporting 6/6 fixture, 250/250 random small cases, byte-identical length-13 manifest. Its own audit log says it was post-hoc exploratory (no precommit). Claude has not yet run or read the DP.

## Not done
No independent reproduction by Claude; no check of DP behaviour on windows where a letter's count is large relative to target sizes, nor on windows with N=0.

## Design
Check out the PR head in a scratch worktree (main untouched). (1) Run the PR's own test file. (2) Write a NEW brute-force oracle, independent of the PR's feasible_splits, directly from the D5 text, and compare count and every rank's unranked split on >=500 random small windows (varied alphabet size, length, target vectors, including N=0 cases) -- a different generator seed/shape than the PR's 250. (3) Check that unrank(rank) over all ranks is a bijection onto the oracle list. (4) Time the DP on constructed length-34 and length-100 windows to see whether it is actually tractable. Non-circular: oracle is separately written exhaustive enumeration; the DP is not used to build test expectations.

## Prediction
DP matches the oracle on all cases (the order-preserving structure looks sound). Possible weak point: runtime/memory at length 100 (_bounded_partitions materialises per-letter choice lists).

## Honesty precommitment
Any mismatch, slowness or disagreement with the PR's claims is reported as-is, including if the DP is correct everywhere. I do not merge, approve, or edit the PR branch, and I do not resolve D10.
