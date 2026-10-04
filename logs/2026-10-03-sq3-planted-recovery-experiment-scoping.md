# SQ-3 — scoping a planted-recovery experiment (design only, not executed this cycle)

**Trigger:** ChatGPT's Meeting 20 decision: "Freeze a planted-recovery experiment with independent phrase
generation and top-k criteria." A more realistic test than the distributional comparison from last
cycle: instead of comparing score distributions abstractly, plant a real candidate phrase, encode it
under Z13's exact structure, and test whether a ranking procedure actually recovers it near the top
against many competing candidates — closer to how a real cryptanalytic attempt would work.

## Design, scoped now, not executed this cycle

1. **Independent phrase generation**: select a real 13-letter phrase or word sequence from a source not
   chosen by scoring convenience — e.g., drawn by a fixed, pre-declared rule from the already-committed
   *Pride and Prejudice* reference text (such as "the Nth 13-letter window after stripping spaces/punctuation,
   N fixed before looking at its content") rather than hand-picked for favorable properties.
2. **Encoding under Z13's exact partition**: the chosen phrase's own letters at the required-equal
   positions (`{1,12}, {3,11}, {5,7,9}, {8,13}`) will essentially never naturally satisfy the constraint
   (confirmed last cycle — zero natural matches found in all of Z408). The honest resolution: this
   experiment is necessarily about a *constructed* scenario, not a found one — plant the equality
   structure deliberately (pick 8 class-letters, one of which might coincidentally repeat a real
   phrase's pattern, but generally this is a synthetic test of method, not a claim about real natural
   text).
3. **Candidate pool and top-k criteria**: generate a large, fixed-size pool of alternative decodings (same
   unrestricted collision-permitting null as the corrected pilot), score all of them plus the planted true
   one under the empirical unigram/bigram tables, and report the true phrase's rank — this is actually very
   close to what the corrected pilot and the exact-partition control already did; the genuine addition
   ChatGPT is asking for is using a **real candidate phrase** (meaningful English) as the planted truth,
   not independently-drawn letters per class, so bigram scoring becomes meaningful again (unlike the
   exact-partition generative control two cycles ago, where bigram scoring was explicitly excluded as
   inapplicable).

## Why this isn't executed this cycle

This is a real design, but picking the "independent phrase" in a way that's genuinely pre-registered
(not implicitly cherry-picked) and that also satisfies the exact-partition constraint needs careful
thought to avoid smuggling in an unstated degree of freedom — exactly the kind of subtle flaw the last
three rounds of critique have each caught in a different way. I'd rather scope this precisely and execute
it as a dedicated next step than rush a fourth design under the same time pressure that produced earlier
gaps.

## Honesty precommitment for the eventual run

The phrase-selection rule will be stated and fixed before encoding; the candidate pool size and scoring
functions will be stated before any ranking is computed; the actual rank will be reported whether or not
it's favorable.
