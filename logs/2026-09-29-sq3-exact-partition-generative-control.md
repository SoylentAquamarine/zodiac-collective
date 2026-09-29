# SQ-3 — a properly-scoped control respecting Z13's exact equality partition

**Trigger:** ChatGPT's exhaustive-enumeration finding: zero 13-character windows in Z408's real ciphertext
share either an 8-distinct-class count or Z13's specific equality partition. This confirms a real category
error in both prior calibration pilots — matching Z13's *distinct symbol count* is not the same as matching
its *specific structural pattern* (which exact positions are forced equal to which others), and the latter
is what actually determines how constrained the decoding problem is.

## What's already known / not done yet

Known: Z13's own documented repeat pattern is `{1,12}, {3,11}, {5,7,9}, {8,13}`, plus four singleton
positions `{2}, {4}, {6}, {10}` — 8 classes total, confirmed already on file. Not done: any calibration
test that actually respects this exact partition rather than just an unordered class count.

## Why a natural-text match isn't the right approach here

Finding a real 13-character English window where positions 1&12 share a letter, 3&11 share a letter,
5&7&9 all share a letter, and 8&13 share a letter is a genuinely rare coincidence in natural text (zero
found in all of Z408 by ChatGPT's exhaustive check) — waiting for one to appear "in the wild" is not a
practical or well-justified strategy.

## Design: a generative control, not a natural-occurrence search

For each of many trials: build a 13-character decoding respecting Z13's exact partition by drawing **one
independent letter per equality class** (8 draws total, not 13) from the empirically-derived unigram
frequency table (the same one from the prior corrected pilot, sourced from *Pride and Prejudice*), then
expand each class's letter to all of its positions. This produces a candidate that has *realistic
per-letter frequency* by construction, respecting the exact structural constraint, without requiring the
letter sequence to be an actual English word or phrase.

**Scoring**: unigram frequency only, not bigram. Bigram scoring requires real sequential English
structure, which this generative approach does not and cannot claim to produce (the letters are drawn
independently per class, not from real running text) — using bigram scoring here would test something the
design doesn't actually construct, and I want to avoid repeating the kind of scope mismatch this whole log
exists to correct. This is an honest limitation of the generative approach, not a workaround.

**Trials and alternatives**: draw 2000 "true" candidates this way (representing plausible realistic
decodings under the exact partition). For each, generate 2000 random alternative decodings that also
respect the same partition (one independent *uniform* random letter per class, not frequency-weighted —
representing an arbitrary wrong guess), and score both under the unigram table. Compare the distribution
of "true" (frequency-drawn) scores against the distribution of "wrong" (uniform-drawn) scores directly,
rather than ranking a single instance — this avoids needing one specific true answer to test against,
since none exists for this synthetic construction.

## Stated prediction

I predict the frequency-drawn distribution will score measurably higher on average than the uniform-drawn
distribution (since frequency-weighted draws are more likely to select common, high-log-probability
letters), but I do not have a confident prediction for how much separation exists, or whether the
distributions overlap enough that a single realistic instance couldn't be reliably distinguished from an
unlucky wrong guess — that overlap question is the real content of this test.

## Honesty precommitment

Report the actual distributions and their separation (or lack of it) exactly as produced, including if
they overlap substantially enough to undermine the "13 characters is enough" claim from prior cycles.

## Result

Self-checks passed: unigram probabilities sum to exactly 1.0; the partition covers all 13 positions
exactly once (no gaps, no double-counting). 2000 frequency-drawn ("true-like") and 2000 uniform-drawn
("wrong") 13-character strings generated, both respecting Z13's exact partition by construction.

```
Frequency-drawn ("true-like") scores: mean = -37.618, stdev = 3.330
Uniform-drawn ("wrong") scores:       mean = -49.763, stdev = 6.659
Median true-like score: -37.159
Fraction of wrong-draws scoring >= median true-like score: 0.0105 (1.05%)
True-like score range: -53.853 to -29.787
Wrong score range:     -78.804 to -33.873
```

**Real separation exists, but it is not the near-total separation the earlier (structurally mismatched)
pilots showed.** Only 1.05% of wrong draws score at or above the median true-like score — still a strong
signal — but the two distributions' ranges genuinely overlap (the weakest true-like draws, down to
-53.85, score worse than the strongest wrong draws, up to -33.87). This is an honestly weaker, more
nuanced result than the prior single-instance percentile rankings, which is expected: this is a
distributional comparison under the *exact* structural constraint Z13 actually has, not a best-case
single-window ranking under a looser, non-matching structure.

## Decision

Under Z13's own exact equality partition, unigram frequency alone still provides real, usable
discrimination between realistic and arbitrary decodings — but with genuine overlap at the tails, not the
near-certainty the earlier flawed comparisons suggested. Bigram scoring was not attempted here, since this
generative construction (independent per-class draws) does not produce real sequential structure and
using bigram scoring on it would repeat the same kind of scope mismatch this experiment exists to correct.
**Revised, more honest conclusion**: 13 characters under Z13's actual structure carries a real but
imperfect statistical signal — not the near-decisive separation claimed two cycles ago. This softens, but
does not reverse, the "length itself is not the blocker" conclusion; it does sharpen the caveat that any
future scoring attempt against Z13 needs real sequential (not just per-letter) structure — likely via
finding or constructing genuine multi-word candidate text, not independently-drawn letters — to get
closer to the separation strength the bigram-scored Z408 pilots showed.
