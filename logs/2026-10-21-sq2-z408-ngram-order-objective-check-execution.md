# SQ-2 — Z408 objective check across n-gram orders — execution

Precommitment: `logs/2026-10-21-sq2-z408-ngram-order-objective-check-selfreview.md`.
Script: `data/scripts/sq2_z408_ngram_order_objective_check.py`; output: `data/derived/sq2-z408-ngram-order-objective-check-output.txt`.

| order | truth | v3 decode | v4 decode | best |
|---|---|---|---|---|
| 1 | -1200.6 | -997.7 | -1014.6 | v3 |
| 2 | -1060.5 | -902.1 | -973.0 | v3 |
| 3 | -975.0 | -934.6 | -1016.1 | v3 |
| 4 | -4164.7 | -3873.3 | -4114.3 | v3 |

## Result
**The stated prediction was wrong: the truth outranks the v3 degenerate decode at NO order.** The gap
shrinks monotonically-ish with order up to 3 (order 1: 203 nats, order 2: 158, order 3: 40.4), and truth
beats the v4 decode at order 3 (by 41 nats) but not at orders 1, 2 or 4. So the objective failure is not
simply an artefact of sparse order-4 statistics; the order-3 near-miss suggests a closer-register corpus
might flip it, but this run does not show that. Corpus is the on-file P&P (563,984 letters; the v4 log's
"~120k" guess in my precommitment was an under-estimate).

## Caveats
Order 4 uses the solver's own joint-count floor model while orders 1-3 use Lidstone-0.5 conditional
probabilities, so scores are not comparable ACROSS orders, only within an order. Two decodes, one corpus,
one text; known plaintext used only as a scoring target. A second-corpus fetch (Gutenberg #2852) was
attempted and blocked by the environment proxy (403), so register repair remains untested.

## Proposed next step
Order-3 gap (40 nats) is small: try a closer-register corpus when fetch access exists (or a user-supplied
small text), verified by the same truth-vs-decode comparison before any search.
