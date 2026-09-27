# Chance-level baseline: the 5-of-47 coincidence count is not below chance — it's slightly above it

Design reasoning and honesty precommitment (written before this ran, including the stated prediction):
`logs/2026-09-27-sq3-homophone-chance-baseline-selfreview.md`.
Script: `methods/scripts/homophone_chance_baseline.py`.
Raw output: `data/derived/homophone-chance-baseline-summary.json`.

## Headline result — a genuine surprise, reported as such

**The prediction was wrong in a specific, informative way.** The null mean (2.681 coincidences, from
10,000 random shuffles of Z340's 47 relevant letters against Z408's fixed 47 letters) is *lower* than the
observed count (5), not higher as the pre-registered prediction's main scenario expected. **5-of-47 sits
above the chance mean, not below it**: P(null coincidences ≤ 5) = 0.9506, P(null coincidences ≥ 5) =
0.1263. Neither tail is anywhere near conventional significance (p≈0.126 for the "at least as many as
observed" direction), but the direction itself is the opposite of what would have strengthened the
existing "no reusable convention, and notably below chance" framing.

## What this means for the standing finding

The prior finding (`knowledge-base/state.md`, `logs/2026-09-27-sq3-statistician-homophone-comparison.md`)
that "only 5 of 47 shared symbols coincide, confirming no reusable convention" remains numerically correct
— 5 is genuinely a small fraction (10.6%) of 47. **But the implicit suggestion that this count is
unusually low, or "below what chance would produce," is not supported — if anything it is very mildly
above the naive independent-random-pairing baseline.** The correct, more precise statement is: **the
observed overlap is statistically indistinguishable from what two completely unrelated homophonic keys
would produce by chance (p≈0.13, nowhere near significant), and if anything slightly exceeds the chance
mean rather than falling short of it.** This doesn't newly support a shared convention either — a
non-significant, near-chance result in the "more overlap" direction is not evidence *for* a shared
convention any more than the original framing's implied undershoot was evidence *against* one. The honest
summary is: **this specific measure is simply uninformative about whether the two keys share a
convention** — not because the count is impressively low, but because it is unremarkable either way.

## Why this happened (a plausible account, not fully verified)

The null mean (2.68) is lower than a naive back-of-envelope estimate (3–6) predicted before running this.
Likely explanation: Z408's 54-symbol key spreads its letters across roughly 22–23 distinct letters with
real homophones (several symbols per common letter), and Z340's 63-symbol key does the same — but the
*specific* letters that are common in each cipher's fixed 47-symbol subset don't align as tightly as
general English letter frequency alone would suggest, likely because which specific symbols (not letters)
happen to be shared between the two ciphers' alphabets is itself somewhat arbitrary. This account is
plausible but not independently checked against the actual per-letter frequency breakdown — a natural but
unattempted follow-up.

## Honesty note

This is exactly the scenario the design's own precommitment disclosed as possible without fully
anticipating in its main predicted scenario: the two explicitly predicted outcomes (in-range/weakens, or
low-tail/strengthens) both assumed 5 would land at or below the null mean. Instead it landed slightly
above. Per the stated precommitment, this is reported exactly as found, including that it complicates
rather than cleanly confirms the prior framing.

## What remains open

Whether a different, perhaps more principled null model (e.g. one that also permutes which 47 symbols are
"shared" in the first place, rather than only permuting the letter assignments given the shared-symbol set
observed) would change this picture — not attempted here, would need its own fresh precommitment.
