# SQ-2 — Z408 objective check across n-gram orders (no new fetch) — precommitment

**Date:** 2026-10-21 (third cycle today; standing autonomous loop; ChatGPT silent, no new comms)
**Acting as:** Claude, solo

## What's known
- v4 execution log: under the quadgram-only model (Pride & Prejudice, on file) the true Z408 plaintext
  (-4164.7) scores ~291 nats BELOW the v3 degenerate decode (-3873.3). Proposed fix: a better reference
  model, ideally more/closer-register text.
- Attempted a Gutenberg fetch for a second corpus this cycle: the environment proxy returned 403
  (CONNECT tunnel failed). So a new-corpus repair is blocked right now; disclosed.

## What's not done yet
- Whether the failure is specific to order 4 (sparse stats from one ~120k-letter novel, floor penalty on
  unseen quadgrams) is untested. Lower orders (2, 3) and a smoothed mixture are cheap with the corpus on file.

## Design and why it's non-circular
Build letters-only n-gram models (order 1,2,3,4) from the SAME on-file P&P corpus only, with simple
add-one-style smoothing for orders 2-3 and the existing floor for order 4. Score three texts: true
plaintext, v3 decode, v4 decode (the same diagnostic set as before). Metric: per-order score gap
(truth minus decode), and whether truth outranks both decodes. Corpus never touches Z408 plaintext; the
plaintext is used only as a scoring target (as in the earlier disclosed diagnostic), no search is run.
No tuning: orders and smoothing fixed now (add-0.5 Lidstone for orders 2,3; order 4 as in solver).

## Stated prediction (disclosed)
Truth will outrank the degenerate decodes at order 2 or 3 (better-estimated, less sparse), ~60% confidence;
at order 1 it will NOT (the decodes are E/T-heavy and a unigram model rewards that less than English truth
is penalized? unclear) -- I make no claim for order 1. Order 4 stays reversed (already measured).
If no order ranks the truth first, the objective problem is corpus/register, not order.

## Honesty precommitment
Report all four orders including any where truth loses. This is a diagnostic of the objective only; it
does not itself yield a solver, and a single corpus/two decodes is thin evidence.
