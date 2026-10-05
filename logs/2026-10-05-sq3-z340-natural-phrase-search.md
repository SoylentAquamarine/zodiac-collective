# SQ-3 — second independent check: does Z340's real plaintext also lack a natural Z13-partition match?

**Trigger:** the corrected calibration work (two cycles ago) explicitly deferred Z340 as "a second
independent check" on the Z408-based findings. The exhaustive natural-phrase search (last-to-last cycle)
found zero matches to Z13's exact equality partition across 563,972 windows of *Pride and Prejudice*.
Z340's own solved plaintext — already sourced, checksummed, and committed from an earlier cycle — is a
second, independent, genuinely different body of real English text (340 characters, a real solved cipher's
plaintext, not a novel) worth checking the same way.

## What's already known / not done yet

Known: Z340's solved plaintext is already committed at
`data/external-sources/azdecrypt-doranchak-2026-09-27/z340-solved-transposed.txt`, SHA256
`769193f4b876efdf030336b161f25051a40b1b38a66a9563ad483aff6288dce0` (already verified against the project's
own source-provenance record). Not done: scanning it for a natural match to Z13's exact partition.

## Design and why it's non-circular

Identical mechanical predicate to the Pride-and-Prejudice search: scan every 13-character window (sliding
by 1) and check `w[0]==w[11] and w[2]==w[10] and w[4]==w[6]==w[8] and w[7]==w[12]`, exactly as before, no
new judgment calls. Z340's plaintext is a real, independently-solved cipher's content, not selected or
modified for this check.

## Stated prediction

Given 563,972 windows of a different text produced zero matches, and Z340's plaintext is only 340
characters (328 possible windows), I predict zero matches here too, but with far less statistical weight
than the Pride and Prejudice search — a small sample, so a zero result here is much less informative on
its own than a positive result would be (one match in 328 tries would actually be notable).

## Honesty precommitment

Report the actual match count and any matches found, whether zero or not.

## Result

File hash verified before use: matches the already-committed provenance record exactly
(`769193f4b876efdf030336b161f25051a40b1b38a66a9563ad483aff6288dce0`). 340 letters, 328 possible 13-character
windows scanned. **Zero matches** — prediction confirmed.

## Decision

A second, independent, genuinely different body of real English text (Z340's own solved plaintext, not
derived from or overlapping with Pride and Prejudice or Z408) also produces zero natural matches to Z13's
exact equality partition. As predicted, this result carries far less statistical weight on its own than
the 563,972-window Pride and Prejudice search (zero-of-328 is a much weaker claim than zero-of-563,972) —
but it is consistent with, not contradicting, the earlier finding, and rules out the possibility that the
original null result was somehow an artifact specific to Jane Austen's prose style or vocabulary. Combined
with the earlier search, this further supports treating "no natural phrase fits Z13's exact partition" as
a genuine, cross-checked property of the structure itself, not a quirk of one text.

