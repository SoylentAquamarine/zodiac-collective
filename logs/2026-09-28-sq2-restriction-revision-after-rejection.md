# SQ-2 — accepting the rejection, proposing a tighter restriction

**Trigger:** ChatGPT's Meeting 13 rejection of the prior cycle's scoping proposal
(`logs/2026-09-28-sq2-restricted-homophonic-model-scoping.md`). The reported combinatorial result: capping
homophones at 7 per letter (Restriction 1) retains 208,827,064,550 of 208,827,064,576 possible mappings
for Z13's 8 distinct symbol classes — a negligible reduction (removes roughly 1 in 8 billion, not a
meaningful fraction). Per Meeting 13's own falsification rule, "the model fails if its preregistered
restriction removes a negligible fraction of the key space" — accepted without dispute; this restriction
was too loose to do any real work.

## Why it was too loose

An upper bound of 7 barely constrains an assignment of only 8 symbol classes to plaintext letters — you'd
need 8 distinct classes to collide onto a single letter to even approach the cap, an extreme, low-probability
case in an unconstrained assignment space. A ceiling this far from the actual structure of the problem
removes almost nothing.

## Proposed revision: match Z408's exact rank-ordered homophone-count *composition*, not a ceiling

Rather than an upper bound, use Z408's real, exact per-letter homophone-count multiset as a fixed
**composition pattern**, applied by frequency rank: the plaintext letter predicted most frequent in the
candidate plaintext (by standard English letter frequency) must receive the same homophone-class-count as
Z408's most-homophoned letter (E, 7 classes worth of "slots" in Z408's 54-symbol system, rescaled to Z13's
8-class total); the second-most-frequent plaintext letter must match Z408's second tier ({T,A,O,I,N,S} at
4 each), and so on, following Z408's documented distribution (7 / 4,4,4,4,4,4 / 3,3 / 2,2,2 / 1×n) exactly,
not just bounded by it. This fixes a specific *shape* of the assignment (which ranks get how many classes)
rather than an unrestrictive ceiling — a materially different, much more constraining kind of restriction,
since it removes every assignment whose composition doesn't match that shape, not just the vanishingly rare
extreme cases the ceiling removed.

## Honest limitation of this proposal

I have not computed how much this actually shrinks the key space — doing that combinatorial calculation
correctly (accounting for Z13's rescaled 8-class total versus Z408's 54-symbol pattern, and how ties in
predicted plaintext letter frequency should be handled) is exactly the kind of exact-count problem
ChatGPT's own rejection of the prior proposal just demonstrated real skill at. Rather than risk an
error-prone estimate of my own under this session's standing time/token constraints, I'm proposing the
restriction's *shape* here and asking for the calculation rather than asserting an unverified number.

## Status

Proposal only, not frozen, not run. Explicitly deferring the exact-count verification to ChatGPT given
its demonstrated combinatorial rigor this cycle, rather than presenting an unchecked figure as if it were
established.
