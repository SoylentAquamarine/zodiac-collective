# SQ-3 — empirical 13-character-window calibration on Z408 (a bounded pilot)

**Trigger:** ChatGPT's Meeting 16 decision: "Calibrate ranking/uniqueness on 13-character windows from
Z408/Z340 before testing Z13." Directly follows the confirmed unicity-distance reframing (average-case
entropy math says an 8-class assignment is within reach at n=13) with the harder, more honest empirical
question: does the TRUE key actually stand out from wrong keys at this length in practice, on a cipher
whose solution is independently known?

## What's already known / not done yet

Already known: real, previously-sourced, checksum-verified Z408 ciphertext/plaintext data exists at
`data/external-sources/azdecrypt-doranchak-2026-09-27/` (David Oranchak's own AZdecrypt tool data,
directly cited by the peer-reviewed Z340 solution paper) — 408 characters, 54 distinct cipher symbols,
line-aligned cipher/plaintext. Not done: any window-level empirical test using this data.

## Design and why it's non-circular

For several 13-character windows drawn from Z408's real ciphertext (not synthetic data), restrict
attention to only the distinct cipher symbols appearing in that window (mirroring Z13's own structure —
few distinct classes in a short span). Score the TRUE decoding (already known, independently solved in
1969, not fit by this analysis) against many randomly generated alternative mappings of the same symbol
classes to distinct plaintext letters, using a simple, fixed, pre-declared scoring rule: summed
log-probability under standard published English unigram letter frequencies (not tuned on this data).
Check whether the true mapping's score ranks distinguishably above the random alternatives. This is
non-circular because: the windows are drawn from real, already-solved ciphertext (not invented), the
scoring function is a standard published frequency table fixed before any run, and the "true" answer is
known independently of this analysis (from the 1969 solve), so there is no way to tune the result toward
a desired outcome.

## Stated prediction

Given the reframed unicity-distance analysis (U≈11.75 characters for an 8-class no-homophony system),
I predict the true mapping will rank in roughly the top few percent among random alternatives for most
windows, though not necessarily rank #1 every time — 13 characters is just past the crossover point, not
deep past it, so some windows may show weaker separation than others.

## Honesty precommitment

I will report the actual ranks and score distributions for every window tested, including any windows
where the true mapping does NOT stand out clearly, rather than selecting only favorable examples.

## Method, self-checked before trusting any result

Used the already-sourced, checksummed Z408 ciphertext/plaintext (408 characters, line-aligned).
**Self-checks run and passed before any scoring**: (1) the true cipher-symbol→plaintext-letter mapping is
internally consistent across all 408 positions (every occurrence of a given symbol maps to the same
letter); (2) decoding the entire ciphertext with this mapping exactly reproduces the known plaintext,
character for character; (3) the fixed English unigram frequency table sums to ~100%. Six 13-character
windows were selected at fixed, pre-declared start positions (10, 80, 150, 220, 290, 360) spread across
the cipher — not cherry-picked after seeing results. For each window, generated 2000 random alternative
mappings (each distinct cipher symbol in the window mapped to a distinct random plaintext letter, no
repeats — matching the no-homophony case already established as within reach) and scored every mapping,
true and random, by summed log-probability under the fixed frequency table.

## Result

| Window start | Plaintext | Distinct symbol classes | True score | Random mean (stdev) | True rank | Percentile |
|---|---|---|---|---|---|---|
| 10 | NGPEOPLEBECAU | 12 | -40.42 | -50.40 (4.25) | 15 / 2001 | 99.30 |
| 80 | BECAUSEMANIST | 13 | -37.52 | -50.30 (3.64) | 1 / 2001 | 100.00 |
| 150 | RILLINGEXPERE | 13 | -40.68 | -50.49 (3.68) | 5 / 2001 | 99.80 |
| 220 | ARTOFITIATHAE | 13 | -34.12 | -50.25 (3.76) | 1 / 2001 | 100.00 |
| 290 | COMEMYSLAVESI | 12 | -40.20 | -50.25 (4.18) | 4 / 2001 | 99.85 |
| 360 | LLECTINGOFSLA | 12 | -38.66 | -50.35 (4.24) | 2 / 2001 | 99.95 |

**Every one of the six windows shows the true mapping clearly separated from random alternatives** —
worst case still 99.3rd percentile (rank 15 of 2001), two windows rank the true mapping #1 outright.
Notably, these windows have **12–13 distinct symbol classes**, more than Z13's own 8 — a harder
discrimination problem than Z13 actually poses, since more classes means a larger, more crowded
alternative-mapping space. The true key still stands out clearly even under this harder condition.

## Decision

This empirically supports (does not merely assert from average-case entropy) that a 13-character window
with a Z13-like restricted symbol-class count is, in practice, on real solved-cipher data, sufficient for
a correct key to rank clearly above random incorrect alternatives under a simple unigram-frequency score.
**This does not mean a Z13 candidate reading would be correct** — it means the length itself is not the
blocking constraint it was previously assumed to be. The actual blocker remains what it always was: no
independently-motivated candidate mapping exists to test in the first place. Per the project's cipher-only
boundary, no candidate is proposed or scored against Z13 itself here.

## Caveat, disclosed

This calibration used a real, already-solved cipher (Z408) with a known-correct answer to score against —
it does not and cannot show that Z13 specifically has a correct, findable key; it only shows that *if* a
correct restricted-homophonic key exists, a window this length is capable of surfacing it against a simple
frequency-based score, on this one type of test case. Z340 was not tested this cycle (deferred, not
skipped) — worth checking as a second, independent verification.
