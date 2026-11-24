# Result: independent Claude review of PR #47 (exact D5 DP) — 2026-11-24
Precommit: `logs/2026-11-24-pr47-d5-dp-independent-review-precommit.md` (committed and pushed before any PR code was run). Cipher-only; synthetic only; no source, no scoring.

## What was run (PR head fbae65a, scratch worktree; main and the PR branch untouched)
1. PR's own test file: ALL PASS, manifest SHA-256 1fc162b7…2eac1 (matches ChatGPT's reported hash).
2. New independent exhaustive oracle (written from the D5 text, not reusing `feasible_splits`), 600 random windows (alphabet 1–5, length 2–11, targets either derived from a real split or a random partition of L): 503 with N>0, 97 with N=0. Count equal on all 600; every rank's unranked split equal to the oracle's i-th element on all 503 N>0 cases; `unrank(N)` raised IndexError each time. **0 mismatches.**
3. Constructed synthetic A4 windows: length 100 (26 letters) N = 1,910,868, count and unrank instantaneous, unranked split has the target multiset. Length 34 (17 letters): **N = 1**, so it is a weak test of ordering (only one feasible split); it checks tractability, not rank ordering.

## Prediction check
Predicted DP matches oracle (confirmed). Predicted possible runtime/memory weakness at length 100 — **not observed** on this constructed window; but the window is one constructed shape, not a natural-text window, so this is not a worst-case bound.

## Caveats (disclosed)
- The oracle is feasible only for small windows, so order-preservation is verified up to length 11; lengths 34/100 rely on the DP's structure (same code path) plus multiset checks, not exhaustive comparison.
- Length-34 constructed case has N=1 — it does not exercise multi-rank ordering.
- PR's `log 2026-11-23-a6-d5-dp-audit.md` is post-hoc by its own statement; this review is the first precommitted check of the DP.
- D10 (in-place vs reset re-shuffle) is untouched and still needs a Director ruling. No approval/merge action is taken by Claude.
