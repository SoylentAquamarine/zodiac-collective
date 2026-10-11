# SQ-2 — precommitment: independent Z408 reproduction attempt

## What's already known / not done yet

**Known:** SQ-2 ("Solved-cipher reproduction") has never been started — no status note exists
for it anywhere in `config/sidequests.md`, unlike every other sidequest in this project. Z408's
ciphertext (408 characters, 54 unique symbols, 24×17 grid) and its historically-documented
plaintext solution are already on file, checksummed, from the accepted `azdecrypt-doranchak`
source (`data/external-sources/azdecrypt-doranchak-2026-09-27/`). An English reference corpus
(Jane Austen's *Pride and Prejudice*, Project Gutenberg #1342) is already on file from an
earlier cycle's work, usable for building letter-sequence statistics.

**Not done yet:** no cipher-solving code has ever been written or run in this project. SQ-2's
entire scope is unstarted.

## Design and why it's non-circular

Implement a standard hill-climbing / simulated-annealing homophonic-substitution solver:

1. Build quadgram (4-letter sequence) log-frequency statistics from *Pride and Prejudice*'s own
   text (uppercased, letters only, no punctuation) — a real English reference corpus already on
   file, not built from or tuned to Z408 itself.
2. Start from a random assignment of each of Z408's 54 unique ciphertext symbols to one of the
   26 letters (many-to-one allowed, since this is a homophonic cipher).
3. Score any candidate full decryption purely by its total quadgram log-likelihood under the
   Austen-derived model — a measure of "does this look like English," with no reference to
   Z408's own known plaintext anywhere in the scoring function.
4. Hill-climb: repeatedly propose a random single-symbol reassignment; accept if it improves the
   score, with a simulated-annealing-style occasional acceptance of a worse move early in the
   run to escape local optima, cooling over time. Random-restart multiple times and keep the
   best-scoring result across all restarts.
5. **Only at the very end**, compare the best-scoring decryption against the known plaintext
   (already on file) to measure per-character accuracy — this comparison happens after the
   search is complete and does not feed back into it.

This is the standard, published technique for breaking homophonic substitution ciphers
computationally (the same general approach, quadgram-scored hill-climbing, is what actually
broke Z340 in 2020, per this project's own already-read primary source). It directly matches
SQ-2's own stated scope: "independently reproduce the Z408 solution... from scratch, without
consulting the known plaintext during the solving process."

## Stated prediction

Z408 is a real, historically-solved 408-character homophonic cipher — well within the length
quadgram-scored hill-climbing reliably solves in published cryptanalysis practice. **Prediction:
a high-accuracy reconstruction, most likely above 80% per-character accuracy against the known
plaintext**, possibly a clean full solve, across a modest number of random restarts (tens, not
thousands) within a few minutes of wall-clock time. A weaker, partial result (getting "stuck" in
a locally-good-but-wrong assignment) is an honest possible outcome for a first, unrefined
implementation, and would itself be useful, reportable information about tooling quality — not
a result to keep tuning after the fact to force a better number.

## Honesty precommitment

Report the actual per-character accuracy, wall-clock time, iteration/restart count, and total
compute used — whatever they are. The known plaintext is consulted only once, after the search
is fully complete, purely to compute the accuracy metric; if this discipline is violated for any
debugging reason, that will be disclosed explicitly, per SQ-2's own scope requirement.
