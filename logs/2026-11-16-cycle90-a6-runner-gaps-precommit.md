# Precommit — cycle #90 response: enumerate remaining A6/A3/C3 under-specification (spec-only)
Written BEFORE the text-reading step below; nothing is executed, scored, or fetched.
- Known: ChatGPT #90 confirmed the v4-vs-A6 mismatches (60 vs 20 restarts, shared vs per-restart seeds, 50/50 swap/reassign vs "swap-based", history-dependent perturbation). My cycle-88 non-binding clarification already covers all four.
- Not done: A3 says "seeded uniform random choice among feasible splits" without fixing the enumeration order the RNG indexes into; A7 names C3 "unigram-random letters" without a source distribution, length rule, or RNG draw order. These are the remaining items in #90's "complete runner" ask not covered by my clarification.
- Design: read-only grep of the committed A-series freeze text for each ambiguity; list each as (ambiguity, why two implementers could differ, proposed fixing sentence). Non-circular: the proposal fixes procedure only and uses no planted or Z13 score, no data.
- Prediction: at least 3 distinct under-specified points remain beyond the four already clarified.
- Honesty: proposal is non-binding; only the Research Director can publish a freeze. If fewer than 3 gaps are found I report that. Cipher-only; no suspect inference.
