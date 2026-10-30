# G8 second-text known-answer diagnostic — precommit

**Written before any score on GITenberg 1661 was computed, 2026-10-29 UTC.** ChatGPT exploratory diagnostic for Claude review; no Z13 or suspect inference.

## Selection and source
The source was named in the 18:07 UTC ChatGPT handoff before Z408 scoring: *The Adventures of Sherlock Holmes* (Arthur Conan Doyle), GITenberg `The-Adventures-of-Sherlock-Holmes_1661`, commit `7e5dd2703fbf503c004063e96ab7c61262375e5f`, path `1661.txt`, Git blob `70349ec04e577406123e9d89af4863cd610ccc1e`. It was selected as a crime-fiction collection by the author of the previously tried ebook 2852; ebook 2852 was already scored and is excluded as a fresh blind comparator. GITenberg's pinned README calls the book public domain; preserve the Gutenberg license notices when obtaining it. Do not redistribute the full text in this PR.

## Frozen cleaning and evaluation
1. Read the exact pinned 1661 text; abort on Git blob mismatch. Slice from the first exact `To Sherlock Holmes she is always THE woman.` through but excluding the first subsequent exact `End of the Project Gutenberg EBook`. This drops boilerplate and the table of contents. Split lines; drop lines matching `/^\\s*ADVENTURE [IVXLC]+\\. .*$/` or `/^\\s*[IVXLC]+\\.\\s*$/`; join with newline. Uppercase and retain ASCII A–Z only. Report the retained-letter count and any empty-marker error.
2. Use G6's exact order-4 add-0.5 scorer: first 70% of letters for training, remaining 30% split into disjoint 408-letter calibration windows, dropping the remainder. Score = mean log probability over 405 transitions. Letter entropy is Shannon bits over 26 counts. Cutoffs are P1/P99 of calibration window score and entropy separately, using G6's nearest-rank-by-rounded-index function. A candidate passes only when inside both bands.
3. Evaluate known true 408-letter Z408 plaintext and all 676 G6 constant/period-2 controls, reporting both axes, accepted count/IDs and calibration window count. The frozen gate passes only if truth is accepted and all 676 controls are rejected. Report P5/P95 and 60/40 sensitivity regardless of primary outcome. Never tune thresholds using truth. The truth string is the same repository file used in G6; verify it normalizes to length 408.
4. Compare results with G6's Pride & Prejudice failure as a corpus-sensitivity diagnostic. No optimizer, Z13 reading, source-language claim, or second solved-cipher validation follows from this single alternate corpus.

**Prediction:** Different register and a larger corpus may improve the truth score, but the text still may reject truth or admit a degenerate. Report failure as failure. A second solved-cipher holdout remains required before any Z13 use.
