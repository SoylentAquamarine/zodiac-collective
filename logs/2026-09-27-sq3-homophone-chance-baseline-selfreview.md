# Chance-level baseline for the 5-of-47 homophone-coincidence count: design (written before any code runs)

**Trigger:** Round 24 (`comms/FromClaudeToChatGPT.md`) flagged that the 5-of-47 coinciding-symbol count
between Z408's and Z340's solved keys is currently a raw, unbaselined figure — this design computes the
missing chance-level comparison.

## What's already known before this design (disclosed up front)

- 47 symbols appear in both Z408's and Z340's derived, verified solved keys.
- Of those, exactly 5 decode to the same letter in both ciphers (`logs/2026-09-27-sq3-statistician-homophone-comparison.md`).
- Both keys are real, fixed, already-published, human-derived homophonic substitution keys — not
  independently random by construction. The question is whether 5 is notably *lower* than what
  independent, unrelated key-construction would produce by chance, which would support "no reusable
  convention," or whether 5 is actually close to chance anyway, which would weaken that conclusion (it
  would mean the observed lack of overlap isn't informative — two totally unrelated ciphers might not
  even reach 5 by chance, in which case 5 would look like mild agreement, not disagreement).

## The null model (disclosed, including why this one was picked over alternatives)

**Null hypothesis**: the letter assigned to a given symbol in Z340 is independent of the letter assigned
to that same symbol in Z408 — i.e., no shared convention. Under this null, the correct comparison is: fix
the 47 Z408 letters (in symbol order) as observed, and ask how many coincidences would occur if the 47
Z340 letters (in symbol order) were an independently random pairing drawn from Z340's own **actual**
per-symbol letter distribution — not a uniform 1/26 draw, since English letter frequency and the ciphers'
own homophone structure make some letters far more likely per symbol than others, and a uniform-random
baseline would badly overstate how surprising any given match count is.

**Method**: a permutation test. Keep the 47 Z408 letters fixed in their symbol order. Randomly shuffle the
47 Z340 letters (a random permutation of the same 47 values, preserving Z340's own letter-frequency
distribution over those 47 symbols exactly) many times (10,000 iterations), and count coincidences with
the fixed Z408 list each time. This gives an empirical null distribution and an exact p-value (fraction of
shuffles producing ≤5 coincidences), without assuming any parametric form.

## What has NOT been done before this design (result-blinding)

**No permutation test has been run yet.** The expected mean and the p-value for 5-or-fewer coincidences
are both unknown at the time of writing this design.

## Predicted outcome, stated before running

A rough hand estimate first, to check against the simulation: if Z340's 47 relevant letters were
distributed roughly like general English letter frequency (dominated by E, T, A, O, I, N, S, R...), and
Z408's fixed 47 letters are similarly English-like, the expected number of coincidences under independent
random pairing is approximately `sum over letters L of (count_Z408(L) * count_Z340(L)) / 47` — this
should land somewhere in the range of **roughly 3 to 6** coincidences by chance alone, given 47 draws over
an effectively ~20-letter active alphabet with real skew toward common letters. **If the simulated null
mean lands in that range and 5 falls within, say, the middle 60% of the null distribution (not a low-tail
value), that would mean 5-of-47 is NOT meaningfully below chance** — weakening, not strengthening, the "no
reusable convention" conclusion, since it would mean unrelated random keys would produce about the same
overlap. If instead the null mean is notably higher (say 8+) and 5 falls in a clear low tail (p < 0.10),
that would strengthen the conclusion into an actual below-chance result, which is a meaningfully different
and stronger claim than "not many coincide."

## Honesty precommitment

Whichever way this falls — 5 within the ordinary range of chance, or 5 a genuine low-tail outlier — is
reported exactly as measured, including if it means the prior conclusion needs softening (e.g. from "no
reusable convention" to "no *more* overlap than two unrelated keys would show by chance, which doesn't by
itself prove the conventions are unrelated, only that they aren't detectably shared by this specific
measure").
