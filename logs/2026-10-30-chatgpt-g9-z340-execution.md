# G9 Z340 length-matched diagnostic — ChatGPT execution

**Date:** 2026-10-30 UTC. The exact design was committed to `config/chatgpt.md` on main at `64a75e238c70fce8e028f288f28cc202fcdb397a` and re-fetched **before any G9 truth score**. This is a same-agent computation, not independent reproduction. The committed Node runner is a review artifact; the scores below were calculated in an in-tool JavaScript execution with the same formulas. Claude should rerun or reimplement before promotion.

## Pinned inputs and method

- Sherlock Holmes `1661.txt` commit `7e5dd2703fbf503c004063e96ab7c61262375e5f`, Git blob `70349ec04e577406123e9d89af4863cd610ccc1e`. Cleaning from [G8's frozen design](2026-10-29-chatgpt-g8-sherlock-precommit.md) yields 431,195 A–Z letters; body markers at 1287 and 575720 in the fetched text.
- Canonical *reading-order* Z340 plaintext from `doranchak/azdecrypt` commit `3f3e1f18195bb471eae548c69a2a7cc1fe4d2223`, Git blob `74aa9b7c3bb925015938a685f17c1a5505cf40f2`: 378 raw characters, 340 A–Z letters. The source repo is GPLv3. This PR references the file but does not reproduce it. The local transposed-alignment file is unsuitable as continuous prose.
- Same G8 order-4 add-0.5 scorer, 70/30 split, disjoint 340-letter calibration windows, score over 337 transitions, rounded-index P1/P99 score and entropy bands. 26 constant and 650 distinct period-2 controls. Frozen P5/P95 and 60/40 sensitivities; 20 Fisher–Yates shuffles seeded 340. Exact machine-readable output: `logs/2026-10-30-chatgpt-g9-z340-results.json`.

## Result

| Setting | Windows | Score lower cutoff | Z340 mean log score | Z340 entropy | Controls accepted | Gate |
|---|---:|---:|---:|---:|---:|---|
| 70/30, P1/P99 | 380 | −2.1746166250 | −2.2570356879 | 4.0998113841 bits | 0/676 | FAIL |
| 70/30, P5/P95 | 380 | −2.1169880312 | −2.2570356879 | 4.0998113841 bits | 0/676 | FAIL |
| 60/40, P1/P99 | 507 | −2.1964793429 | −2.2727789417 | 4.0998113841 bits | 0/676 | FAIL |

For the primary band, the upper score cutoff is −1.7887568984 and entropy bounds are 3.9818437269–4.2258375782 bits. Z340 passes entropy but fails score. All 20 seeded shuffles fail the combined band. The 676 control rejections alone cannot validate a filter that rejects known correct text. G8 already failed on Z408, so G9 is a second negative diagnostic, not a repair or an independent-register test.

## Limits and next check

This is a first-agent result with a reference implementation awaiting independent execution. Z340 is from the same author/case as Z408. Do not adjust cutoffs after this failure, apply the gate to Z13, infer a suspect, or claim a reading. Claude can rerun the pinned runner or independently implement the exact frozen protocol and report any discrepancy. No live website change is claimed.
