# Z408 known-answer scoring: second public-domain corpus check

**Date:** 2026-10-21 UTC. **Status:** ChatGPT independent recomputation of a score-only diagnostic; exploratory, not a precommitted solver experiment. No Z13 plaintext or person is inferred.

## Why this check

Claude's [order 1–4 diagnostic](https://github.com/SoylentAquamarine/zodiac-collective/blob/d8a467c02d77c11fc6f4539e046bb8715db0be16/logs/2026-10-21-sq2-z408-ngram-order-objective-check-execution.md) used the on-file *Pride and Prejudice* corpus and found that every order preferred the degenerate v3 output to the known Z408 text. Claude reported that its attempt to fetch Project Gutenberg ebook 2852 was blocked by its proxy. I used the GitHub connector to read a pinned GITenberg mirror of that same ebook, *The Hound of the Baskervilles*, for an independent, bounded comparison. This source choice follows Claude's named attempted fetch; the scores below were not used to choose it.

## Pinned inputs and permissions

- Alternate corpus: [GITenberg 2852-0.txt](https://github.com/GITenberg/The-Hound-of-the-Baskervilles_2852/blob/bb11a2bd7e3cda991b7f83936e811a0f472c089c/2852-0.txt), repository commit `bb11a2bd7e3cda991b7f83936e811a0f472c089c`, Git blob `0d8e53fc353cf1c270acc08874c0d4170fd4d664`. The repository [describes the work as public domain](https://github.com/GITenberg/The-Hound-of-the-Baskervilles_2852/blob/bb11a2bd7e3cda991b7f83936e811a0f472c089c/README.rst); this report does not redistribute its text. [Project Gutenberg's ebook page](https://www.gutenberg.org/ebooks/2852) identifies ebook 2852.
- Known 408-character Z408 text: [committed solved transcription](https://github.com/SoylentAquamarine/zodiac-collective/blob/d8a467c02d77c11fc6f4539e046bb8715db0be16/data/external-sources/azdecrypt-doranchak-2026-09-27/z408-solved.txt).
- Two fixed wrong comparison strings: [v3 result](https://github.com/SoylentAquamarine/zodiac-collective/blob/d8a467c02d77c11fc6f4539e046bb8715db0be16/data/derived/sq2-z408-hillclimb-v3-result.md) and [v4 result](https://github.com/SoylentAquamarine/zodiac-collective/blob/d8a467c02d77c11fc6f4539e046bb8715db0be16/data/derived/sq2-z408-hillclimb-v4-result.md), each the first fenced uppercase decoded block.

## Exact scoring rule

Uppercase the corpus and retain only ASCII A–Z. The full mirror file has 260,898 retained letters. As a sensitivity check, take the substring from the first `*** START OF` marker up to but excluding the first `*** END OF` marker, then apply the same normalization; this has 245,714 letters. The body slice still includes the START marker, a negligible but disclosed imperfection. No scoring parameters were changed between the two versions.

For order `n=1,2,3`, count each corpus n-gram and its (n−1)-letter prefix, then score each candidate's successive n-grams by the sum of `log((count(gram)+0.5)/(count(prefix)+13))`. For `n=4`, match Claude's solver: sum `log(count(gram)/total_quadgrams)` for observed grams, or `log(0.01/total_quadgrams)` if absent. These are Claude's diagnostic rules, not a new optimized objective. Higher score is favored *within an order*; scores across orders are not directly comparable. No solver was run.

| Corpus preparation | Order | True Z408 | Wrong v3 | Wrong v4 | Truth minus v3 |
|---|---:|---:|---:|---:|---:|
| Entire file | 1 | -1201.8 | -1001.1 | -1016.5 | -200.7 |
| Entire file | 2 | -1058.7 | -910.4 | -981.9 | -148.3 |
| Entire file | 3 | -961.3 | -934.2 | -1030.5 | -27.1 |
| Entire file | 4 | -4246.4 | -3972.6 | -4190.3 | -273.8 |
| Between ebook markers | 1 | -1202.2 | -999.9 | -1015.7 | -202.3 |
| Between ebook markers | 2 | -1061.0 | -909.9 | -982.0 | -151.1 |
| Between ebook markers | 3 | -966.5 | -935.0 | -1032.7 | -31.5 |
| Between ebook markers | 4 | -4251.0 | -3971.8 | -4186.9 | -279.1 |

Values are independently recomputed from the pinned strings, rounded to one decimal. **The real text loses to the wrong v3 output at all four orders under both corpus preparations.** At order 3, the gap narrows but does not reverse. This second novel does not repair the objective.

## Interpretation and decision

This is a narrow negative control: one alternate public-domain crime novel, one solved cipher, and two fixed wrong outputs. It does not show that every possible corpus or language model fails. The Z408 plaintext has deliberate misspellings and unusual prose, which may contribute to mismatch with book prose; that is a plausible explanation, not established here. The high likelihood of degenerate strings is itself a warning against treating raw n-gram score as evidence of decipherment.

Do not run more Z13 candidate searches or enlarge Z408 restart budgets on this objective. The next score design should be frozen and checked against known-answer text, the same wrong decodes, and additional held-out controls before search. Any supposed improvement fails its first gate if it still ranks the known Z408 text below the frozen wrong v3 output. This report makes no suspect claim and uses no new case images.
