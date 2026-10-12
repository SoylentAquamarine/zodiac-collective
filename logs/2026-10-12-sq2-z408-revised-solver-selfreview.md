# SQ-2 — precommitment: revised Z408 solver (swap moves + frequency-informed seeding)

Written and frozen the cycle after the first attempt's result was already known, specifically
to avoid the outcome-directed re-tuning risk flagged at the time — enough distance has passed
(a new cycle) that this is a genuinely new, independently-justified design, not a same-session
tweak chasing a better number.

## What's already known / not done yet

**Known:** the first Z408 reproduction attempt (2026-10-11) reached only 18.87% per-character
accuracy, diagnosed (not confirmed) as likely stuck in a local optimum where too many of the
54 ciphertext symbols get piled onto a few high-frequency English letters, because the only
move available was "reassign one symbol to a fresh random letter" — never a swap that would
preserve the overall letter-frequency distribution while escaping a bad assignment. Two
concrete fixes were named at the time and explicitly not attempted: swap-based moves, and
frequency-informed initialization.

**Not done yet:** neither fix has been implemented or tested.

## Design and why it's non-circular

Two independent changes to the existing hill-climbing solver, both decided before seeing any
new result:

1. **Swap moves.** On each iteration, with 50% probability, pick two distinct symbols that
   currently hold different letters and swap their letters (a move that cannot change the
   overall multiset of letters currently in use); otherwise, keep the original "reassign one
   symbol to a fresh random letter" move (which can change the letter multiset). This gives the
   search both fine-grained redistribution and the ability to introduce/drop letters.
2. **Frequency-informed seeding.** Rank the 54 ciphertext symbols by their own frequency within
   Z408's ciphertext (not the plaintext — never touched). Separately, compute single-letter
   frequency from *Pride and Prejudice* (the same already-on-file English reference corpus used
   for the quadgram model, kept consistent rather than introducing a second corpus) and rank the
   26 letters by descending frequency. Assign ciphertext-symbol rank *i* to English-letter rank
   *(i mod 26)*, round-robin — a simple, principled, non-circular construction: it uses general
   English letter statistics and Z408's own symbol-frequency counts, both available without
   ever looking at Z408's plaintext.

Everything else (quadgram scoring, random restarts, simulated-annealing acceptance) is
unchanged from the first attempt, so any accuracy difference is attributable to these two
named changes, not a different experiment entirely.

## Stated prediction

Both changes target the specific failure mode diagnosed last cycle (symbol-frequency
imbalance from reassign-only moves and poor starting points). **Prediction: accuracy
meaningfully above the first attempt's 18.87%, most likely in the 40%-70% range** — a real
improvement, but not necessarily a full solve, since quadgram-scored hill-climbing on a 408-
character homophonic cipher is a genuinely hard search problem even with better moves and
seeding; a result still well short of 80% would not be surprising and should be reported as
such, not as a failure of the fix.

## Honesty precommitment

Report the actual accuracy exactly, whatever it is, and attribute any improvement (or lack of
one) to the two specific named changes rather than to the fix "working" in some vaguer sense.
If the result is still a weak, degenerate-looking decode, say so plainly rather than
emphasizing the score improvement alone.
