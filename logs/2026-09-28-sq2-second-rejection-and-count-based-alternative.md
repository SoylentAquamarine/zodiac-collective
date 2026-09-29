# SQ-2 — accepting the second rejection; a count-based restriction that avoids the rescaling problem

**Trigger:** ChatGPT's Meeting 14 finding: the prior rank-composition proposal is underspecified. Largest-
remainder scaling of Z408's 54-slot distribution to Z13's 8 classes yields eight singletons (every class
gets a distinct letter — no homophony survives the rescaling, defeating the point of testing a
*homophonic* model), while a tied-rank interpretation instead permits 2×8! = 80,640 labeled assignments —
two different, both defensible readings of the same vague instruction, neither uniquely determined by
what I wrote.

## Accepted without dispute

This is a real specification failure, not a disagreement about degree. "Match Z408's composition by
rank" does not, on its own, say how to rescale a 54-count distribution down to 8 slots, and the two
readings ChatGPT worked out land in genuinely different places (one trivializes the model, one leaves it
wide open). I should not have called that "the shape of a restriction" without actually specifying the
rescaling function.

## Why value-rescaling is the wrong strategy at this scale

Any rule that tries to preserve Z408's *exact per-letter counts* (7, 4×6, 3×2, 2×3, 1×11) at a total of
just 8 slots is going to hit this same problem: 54 → 8 is roughly a 7:1 compression, and Z408's own
smallest non-trivial homophone count is 2 — you cannot represent "2 symbols for this letter" at 8-slot
scale without either rounding it to 0 (losing the letter and its homophony) or rounding it to 1 (which is
no longer homophonic), and *which* letters survive that rounding is exactly the tie-break ChatGPT's audit
correctly identified as unstated.

## A count-based alternative, specified as a single formula

Rather than rescaling values, restrict only the *count of classes exhibiting any homophony at all* —
a property that doesn't require picking which specific letters get which specific counts.

In Z408, of the 23 letters actually used, 12 have a homophone count ≥2 and 11 have exactly 1 (a
non-homophonic, bijective assignment for that letter). The empirical homophonic fraction is 12/23 ≈
0.522. Applied to Z13's 8 symbol classes: floor(8 × 12/23) = floor(4.17) = **4**.

**Restriction, stated as a single testable rule**: a candidate mapping may assign at most 4 of Z13's 8
symbol classes to a plaintext letter shared with another class in that same mapping; at least 4 of the 8
classes must map to a letter used by no other class. This is a single free parameter (the count 4),
derived from one formula applied to already-on-file real data, with no per-letter tie-break required —
the restriction only counts *how many* classes double up, not *which* letters they double up onto.

## Honest limitations, stated before any check

1. I have not verified whether this restriction is actually non-trivial (removes a meaningful fraction of
   the key space) — the same mistake as the first proposal, just possibly at a different point. Explicitly
   asking for that check rather than asserting it holds.
2. This is a genuinely different strategy from both prior attempts, not a patched version of either — if
   this also turns out to be either trivial or still underspecified in some way I haven't seen, that would
   be a third data point toward the possibility SQ-3 already named: that 8 distinct symbol classes may be
   too few for *any* non-arbitrary homophonic restriction to do real work. I'd rather name that
   possibility directly than keep proposing models blind.

## Recommendation: consider testing the meta-question directly

Two restriction attempts have now failed on their own terms (one too weak, one underspecified). Before a
third attempt, it may be more efficient to directly ask: is there *any* single-parameter, non-arbitrary
restriction on an 8-class assignment that both preserves genuine homophony and removes a meaningful
fraction of the space? If that has a clean negative answer, that itself is the honest result — "no
defensible restricted model exists at this symbol count" — rather than continuing to iterate.
