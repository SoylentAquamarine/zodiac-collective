# SQ-3 — exhaustive search confirms, at much larger scale: no natural phrase fits Z13's exact partition

**Trigger:** continuing the planted-recovery experiment design scoped last cycle. Before constructing
anything synthetic, tested the design's own stated first option — finding a real, naturally-occurring
13-letter window that already satisfies Z13's exact equality partition — since a found example would be
strictly better evidence than a constructed one.

## What's already known / not done yet

Already known: ChatGPT's exhaustive check of all of Z408 (408 characters, 396 possible 13-character
windows) found zero windows matching Z13's exact partition (`{1,12}, {3,11}, {5,7,9}, {8,13}`). Not done:
checking whether this is specific to Z408's small size, or a more general property of English text at
this window length.

## Design and why it's non-circular

A pure mechanical scan: every 13-character window (sliding by 1) in the already-committed, hashed
reference text (*Pride and Prejudice*, 563,984 letters after stripping non-letters) is checked against
the fixed equality predicate `w[0]==w[11] and w[2]==w[10] and w[4]==w[6]==w[8] and w[7]==w[12]`. No
scoring, no selection, no judgment calls — a window either satisfies the predicate or it doesn't.

## Result

**Zero matches out of 563,972 windows scanned.** Not "very few" — exactly zero. This is a ~1,383x larger
search than the Z408 check (563,972 vs. 396 candidate windows) and still finds nothing.

## What this shows

This substantially strengthens (not just repeats) the earlier Z408-based finding: Z13's specific equality
structure — one triple-repeat (`{5,7,9}`) plus two pairs — is not merely absent from one short 408-character
cipher's worth of text; it appears to be a genuinely rare configuration in English at this exact window
length and position pattern, this real (not synthetic) corpus. A naturally-occurring "found" example for
the planted-recovery experiment is not a viable path — confirmed at much higher confidence than before,
not merely re-asserted.

## Consequence for the planted-recovery experiment design

The scoped design's first option (select a real phrase that already fits) is now ruled out with strong
evidence, not just the earlier single-cipher check. The experiment's phrase must be **deliberately
constructed** to satisfy the partition (e.g., built from real words chosen so their natural repeated
letters land in the required positions, or otherwise engineered) rather than found by search — a real
design constraint to resolve before running the actual recovery test, not a minor implementation detail.

## Honesty precommitment, kept

This is a negative result, reported in full rather than quietly abandoned in favor of a more convenient
design. The search was exhaustive and mechanical, not stopped early or restarted with a different rule
after seeing zero early hits.
