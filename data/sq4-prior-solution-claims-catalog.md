# SQ-4 — Prior claimed Z13 solutions catalog (cipher-only half)

Per this sidequest's own scope split: publicly claimed **Z13 solutions** (what the ciphertext is claimed
to decode to, and the cryptologic evidence for/against) are catalogued here. **Named-suspect theories are
explicitly and deliberately excluded from this file and from this pass** — the standing project-level
instruction under which this cycle's work was done states that half "has been deliberately left unstarted
pending explicit confirmation, not attempted solo," on top of this repository's own README/CONTRIBUTING
boundary against producing new accusatory content. Several real, publicly documented claimed solutions
double as named-suspect theories (the proposed plaintext is or contains a candidate suspect's name); those
are named here only generically (proposer, date, existence of a critique) with the specific claimed name
withheld, pending that explicit confirmation.

## Claim 1 — "ALFRED E. NEUMAN" (Craig P. Bauer)

**Proposer:** Craig P. Bauer, cryptographer and cipher historian (author of a published book on the Zodiac
ciphers). **Claimed plaintext:** "ALFRED E. NEUMAN" — the Mad Magazine mascot, not a real individual.
**Claimed structural evidence:** Bauer's own stated argument is that Z13's first three cipher symbols
decode to "AEN," matching Neuman's initials. **Rationale offered:** fits the killer's documented taunting
tone (naming a fictional joke mascot as "my name"), not a suspect-identification claim at all.

**Evidentiary status, disclosed plainly**: not universally accepted. Z13's extreme shortness (13
characters) is repeatedly cited across sources as the central structural problem — too short for
frequency analysis to independently verify any proposed key, meaning the claim cannot be confirmed or
ruled out by statistical means alone, only by checking its own internal consistency (e.g., against the
repeat-structure constraints noted in Claim 3 below, not yet done for this specific claim by this
project). No independent reproduction attempted by this project this cycle — recorded as a citable claim,
not relied upon.

**Sourcing tier**: search-synthesis tier (History.com article by Bauer himself, via WebSearch) — not yet
directly fetched as a primary document.

## Claim 2 — A 2021 claim using the Z340 solve's key (proposer publicly named, claimed to name a suspect)

A French amateur codebreaker publicly claimed in early 2021 to have extended the key used in the
FBI-confirmed December 2020 Z340 solution to Z13, with the claimed plaintext reported as identifying a
suspect. **Per this catalog's own stated scope boundary above, the specific claimed name is deliberately
not recorded here.** What is recorded: the claim exists, is widely publicly reported (e.g. Fox News, New
York Times coverage), and drew mixed expert reaction — Z340 co-solver David Oranchak was reported
skeptical; cryptographer Rémi Géraud was reported as characterizing the method as involving "arbitrary
choices"; two other named cryptographers were reported as more sympathetic to the method's soundness.
Oranchak is also reported making the broader methodological point that it is "practically impossible to
determine" which of the many (reportedly "hundreds") of proposed Z13/Z32 solutions is correct, given the
cipher's shortness — the same structural problem noted in Claim 1.

**Sourcing tier**: search-synthesis tier only this cycle.

## Claim 3 — A structural falsification method: Z13's own repeat-position constraints

Independent of any specific proposed plaintext, a documented critique (dated 2026-02, responding to a
different, also-not-named-here 2025/2026 candidate-name claim) states four repeat-position equality
constraints that **any** one-symbol-one-letter substitution solution to Z13 must satisfy, since they
follow directly from the ciphertext's own observed symbol-repeat pattern, not from any candidate plaintext:
**position 1 = position 12, position 3 = position 11, position 8 = position 13, and positions 5, 7, and 9
must all decode to the same letter.** The critique's conclusion in that specific case was that the tested
candidate name failed these constraints under the standard one-symbol-one-letter model (the critique
explicitly scoped its own claim to that model, not ruling out a non-standard encoding).

**Cross-check against this project's own existing Confirmed Finding**: `knowledge-base/state.md` already
has this exact pattern on record, at a stronger sourcing tier (directly fetched from `zodiackillerciphers.com`,
citing the original April 20, 1970 San Francisco Chronicle scan — see
`logs/2026-09-25-sq3-z13-repeat-pattern-flexibility.md`) — positions 1=12, 3=11, 5=7=9, 8=13. Today's
search-synthesis-tier source states the identical equalities independently. This is not new structural
information for this project; it's an independent secondary corroboration of an already-stronger-tier
finding, recorded here specifically because it shows the rule being actively used by an outside critic to
falsify a real 2025/2026 candidate claim — a concrete demonstration of this project's own planned
flexibility-testing approach already happening in the wild, worth knowing about even though the rule
itself isn't new.

**Sourcing tier**: search-synthesis tier for this specific application; the underlying repeat-pattern rule
itself is already a directly-fetched-tier Confirmed Finding (see above).

## Honest bottom line

Three real, citable claims now on file, none independently verified by this project. Claim 3's
repeat-position rule was already a directly-fetched-tier Confirmed Finding before this cycle; what's new
is seeing it actively applied by an outside critic against a real candidate claim, worth having on file as
a demonstration of the project's own planned falsification approach, not as new structural knowledge.
Claim 1 ("ALFRED E. NEUMAN") is the one genuinely new, independently checkable, non-suspect candidate this
project now has on record — applying Claim 3's rule to it is a concrete, fully cipher-only next step once
SQ-1's canonical transcription exists. Two claims (2 and the 2025/2026 one referenced for Claim 3) involve
a named-suspect dimension this project is not evaluating this cycle — recorded only generically, per the
standing scope decision stated above, pending explicit user confirmation to catalog that half properly.
