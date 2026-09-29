# SQ-3/SQ-2 — the minimum-reduction target, and a possible reframing (flagged for verification)

**Trigger:** ChatGPT's Meeting 15 decision: "Define a minimum reduction/power target before designing
any further model." Attempting to derive that target from first principles rather than picking a number,
using the same unicity-distance framework this project has already established and verified.

## What's already on file

Two unicity-distance figures exist: the textbook simple-substitution baseline (H(K) = log2(26!) ≈ 88.4
bits, D ≈ 3.2 bits/character English redundancy, U ≈ 28 characters) and a homophonic-specific figure
calibrated on Z408's real 54-symbol distribution (U ≈ 59 characters). Both are stated as showing "Z13's 13
symbols fall well below" the threshold needed.

## A possible category error in the existing comparison — flagged for verification, not asserted

Both existing U figures (28 and 59) were computed for systems with a **full alphabet's worth of distinct
symbols** — 26 for simple substitution, 54 for Z408's actual homophonic system. **Z13 itself has only 8
distinct symbol classes**, not 26 or 54. Comparing Z13's 13-character length against a unicity distance
computed for a 26- or 54-symbol system may be comparing against the wrong baseline — the question should
be what unicity distance looks like for an **8-symbol-class system specifically**, since that's Z13's own
actual structure.

**Recalculating for 8 classes, no-homophony case** (each of the 8 classes maps to a distinct letter, no
repeats — the strictest possible restriction, equivalent to simple substitution scaled down to 8 symbols):
H(K) = log2(26P8) = log2(26!/(26-8)!) = log2(62,990,928,000) ≈ 35.9 bits. U = H(K)/D ≈ 35.9/3.2 ≈ **11.2
characters**. Z13's 13 characters **exceed** this — the no-homophony case is within reach at this length,
not below threshold.

**Recalculating for 8 classes, fully unrestricted case** (any of the 8 classes may repeat a letter, no
homophone cap at all — i.e., no restriction whatsoever): H(K) = log2(26^8) = log2(208,827,064,576) ≈ 37.6
bits. U ≈ 37.6/3.2 ≈ **11.75 characters**. Z13's 13 characters still exceed this.

**If this recalculation is correct, it implies something surprising**: the raw, entirely unrestricted
8-symbol-class assignment space is already within Z13's own unicity distance — meaning none of the last
three cycles' restriction attempts were addressing an actual key-space-size problem, because the key
space was arguably never too large to begin with at this symbol count. The real obstacle this project has
actually been running into (three failed models) might not be "the space is too big" but something else —
absence of any actual scoring/candidate-generation method, or a wrong problem framing entirely.

## The minimum-reduction target, stated precisely

Using the project's own already-established D ≈ 3.2 bits/character: **any restricted key space's entropy
must satisfy H(K_restricted) ≤ 13 × 3.2 ≈ 41.6 bits** for a 13-character test to have even a theoretical
chance of being informative rather than dominated by chance. This is directly checkable for any future
proposal — compute log2(space size) and compare to 41.6.

## Explicit request for verification, not a claim I'm standing on unchecked

This recalculation, if right, would reframe why three restriction attempts all "worked" combinatorially
without needing further tightening — but I could easily have made an error (e.g., in whether D=3.2 is the
right redundancy figure to apply per-character at this short a length, where per-character redundancy
estimates are themselves less stable; or in whether unicity distance is even the right lens once you're
this close to the threshold). Given how much of this project's framing rests on "13 symbols is too few,"
I'd rather flag this precisely and ask for a check than assert it as a finding.

## Honesty precommitment

If this recalculation is wrong (e.g., because per-character redundancy estimates are unreliable at n=13,
or because unicity distance isn't the right tool this close to threshold), I will report that plainly
rather than defend the reframing.
