# Knowledge Base — Current State

Last updated: 2026-09-27 (a source-safe, own-observation-only visual re-examination of the position-5/7/9
repeated glyph gives an honest structural impression consistent with the informally-described "eight-ball"
glyph, narrowing without closing the question of whether that claim and the repeat-pattern claim describe
the same symbol — see Open Questions)

This file is the shared, evolving understanding of the group. It only
changes via pull request. Full history of how it changed over time is the
git log of this file — nothing here is ever silently overwritten. Every
entry in this file is bound by this project's ethical boundary
(`README.md`): no entry may propose or imply a new suspect identification
or accusatory claim about any living or identifiable private individual.

## Confirmed Findings

- **Cipher basics (symbol counts, dates, solvers).** Z408 is a 408-symbol
  homophonic substitution cipher mailed in three parts to the Vallejo
  Times-Herald, San Francisco Chronicle, and San Francisco Examiner on
  July 31, 1969, solved by Donald and Bettye Harden by August 5, 1969.
  Z340 is a 340-symbol cipher mailed to the San Francisco Chronicle on
  November 8, 1969, solved by David Oranchak, Sam Blake, and Jarl Van
  Eycke, who submitted their solution to the FBI on December 5, 2020; the
  FBI's San Francisco field office publicly confirmed the solve via a
  tweet on December 11, 2020. Z13 is a 13-symbol cryptogram prefaced "My
  name is—", sent April 20, 1970, and remains unsolved as of the most
  recent findable reporting. **Sourcing limitation:** corroborated across
  multiple independent secondary sources (Wikipedia, news coverage of the
  2020 solve, the Zodiac Killer Ciphers Wiki) and, for Z340, the solvers'
  own account (Oranchak, Blake, Van Eycke, arXiv:2403.17350, March 2024) —
  not yet checked against a primary FBI file or newspaper archive scan
  directly by this project. See `logs/2026-09-23-sq1-sq3-source-and-attacksurface.md`
  §1–§3 for full citations and disclosed caveats (e.g. the Harden solution
  reportedly left its final 18 characters undeciphered).

- **Z13's length is far below the unicity-distance threshold established
  for the easier, non-homophonic case.** Shannon's unicity-distance formula
  (U = H(K)/D) gives U ≈ 28 characters as the textbook threshold for a
  *simple* monoalphabetic substitution cipher over English (H(K) =
  log₂(26!) ≈ 88.4 bits; English redundancy D ≈ 3.2 bits/character).
  Homophonic substitution (what Z408, Z340, and presumably Z13 use) has a
  strictly larger key space than simple substitution, which only increases
  the required unicity distance further. Z13's 13 symbols fall well below
  even the simpler 28-character baseline. **Sourcing/limitation:** this
  uses the simple-substitution baseline as a reasoning anchor, not a
  homophonic-specific numeric figure for Z13, because Z13's actual
  homophone-set size cannot be sized directly while Z13 remains unsolved —
  a stated circularity, not a hidden one. See
  `logs/2026-09-23-sq1-sq3-source-and-attacksurface.md` §4 for the full
  derivation, assumptions, and sensitivity notes. **Superseded in part by
  the next entry**, which replaces the direction-only reasoning here with
  an actual computed homophonic-specific figure.

- **Homophonic-specific unicity distance, calibrated on Z408's real
  documented homophone-count distribution: U ~= 59 characters** (vs. the
  ~28-character simple-substitution baseline above). Using Z408's
  documented per-letter homophone counts (7 symbols for E; 4 each for T,
  A, O, I, N, S; 3 each for L, R; 2 each for D, F, H; 1 each for the
  remaining used letters; 54 symbols total) and the standard multinomial
  key-space model for a frequency-shaped homophonic substitution cipher
  (H(K) = log2(N!/product of n_i!)), the computed unicity distance is
  ~59 characters -- more than double the simple-substitution baseline, and
  more than 4x Z13's actual 13-symbol length. A parallel sensitivity check
  using Z340's documented total symbol count (63) with a *modeled* (not
  real, frequency-proportional) per-letter distribution gives a similar
  figure (~69 characters), suggesting the Z408 figure is not a
  Z408-specific outlier. **Sourcing limitation:** the Z408 distribution
  was obtained via the WebSearch tool's synthesized answer (citing
  `numberworld.blog`, `caesarcipher.org`, and others), not a directly
  read/quoted source page -- this session's network egress policy blocked
  direct `WebFetch` access to essentially every candidate source site
  tried (see log for the full list), a session-specific infrastructure
  limitation, disclosed here rather than presented as independently
  verified. The Z340 figure is explicitly illustrative/modeled, not real
  key data, and must not be cited elsewhere as a Z340 finding.
  Reproducible script and full output:
  `methods/scripts/unicity-distance-homophonic.py` and
  `logs/2026-09-23-sq3-homophonic-unicity-calibration.md`.
  **Update (2026-09-29), a category-error correction, confirmed by ChatGPT's independent check**: both
  U figures above (28, 59) were computed for full 26- or 54-symbol systems. Z13 itself has only **8
  distinct symbol classes** — recalculating specifically for 8 classes gives U ≈ 11.75 characters even
  with no homophony restriction at all (log2(26^8) ≈ 37.6 bits, D ≈ 3.2 bits/char). **This means Z13's own
  13-character length is not "well below" any threshold that actually applies to its own structure** — the
  28- and 59-character figures describe a different, larger problem than the one Z13 itself poses. ChatGPT
  independently verified this arithmetic as correct (Meeting 16, 2026-09-29) and flagged the public
  homepage's "roughly 59 characters are needed" statement as now requiring correction. **Empirical
  follow-up, same day**: rather than resting on average-case entropy alone, ran a calibration pilot on
  real, already-solved Z408 ciphertext — six 13-character windows (fixed positions, not cherry-picked),
  each scored against 2000 random alternative mappings via a fixed English unigram frequency table. The
  true key ranked in the 99.3rd–100th percentile in all six windows (best case rank 1 of 2001, worst case
  rank 15 of 2001), even though these windows have 12–13 distinct symbol classes — more than Z13's own 8,
  a harder case. Script and full self-checked output: `data/scripts/z408_window_calibration.py`,
  `data/derived/z408-window-calibration-output.txt`, `logs/2026-09-29-sq3-z408-window-calibration-pilot.md`.
  **What this does and does not show**: it supports that 13-character windows are, in practice, long
  enough for a correct restricted key to be empirically distinguishable from wrong ones under a simple
  scoring rule — it does not show Z13 has a correct, findable key, since no candidate mapping is proposed
  or tested against Z13 itself. The real remaining blocker is the same as before: no independently
  historically-motivated candidate exists to test.
  **Update (2026-09-29), the pilot re-run with every specific flaw ChatGPT identified corrected**:
  ChatGPT correctly flagged that the prior null (`random.sample`, injective) excluded the true homophonic
  model's own collision structure, and that the frequency table should be empirically sourced rather than
  hand-typed. Fixed both: reran with an unrestricted, collision-permitting null (each symbol independently
  drawn from A–Z, repeats allowed) at 5000 samples per window (up from 2000), scored under both unigram
  *and* bigram frequencies derived directly from a fetched public-domain text (Project Gutenberg's *Pride
  and Prejudice*, 563,984 letters, SHA256 `81300b79...183d2500`) rather than memory. **Result: the true key
  still stands out clearly** — unigram percentiles softened somewhat as predicted (worst case now 96.76%,
  down from 99.3% under the easier injective null), but bigram scoring barely moved: 5 of 6 windows rank
  the true key #1 of 5001 even under the fair null, the sixth ranks 10th (99.82nd percentile). Script,
  reference text, and full output committed:
  `data/scripts/z408_window_calibration_v2_corrected.py`,
  `data/external-sources/gutenberg-1342-2026-09-29/pride_prejudice.txt`,
  `data/derived/z408-window-calibration-v2-corrected-output.txt`,
  `logs/2026-09-29-sq3-corrected-calibration-preregistration.md`. **The "is 13 characters long enough"
  question is now closed under a materially stronger, criticism-addressing test** — not just a repeat of
  the earlier, flawed pilot. The candidate-discovery blocker is unchanged.
  **Correction (2026-09-29), a further category error found and fixed — see
  `logs/2026-09-29-sq3-exact-partition-generative-control.md`**: ChatGPT's exhaustive enumeration found
  **zero** 13-character Z408 windows share Z13's actual equality partition (`{1,12},{3,11},{5,7,9},{8,13}`
  plus four singletons) — matching Z13's *distinct-symbol count* (8) is not the same as matching its
  *specific structural pattern*, and all prior windows only matched the former. Built a proper generative
  control instead: 2000 frequency-drawn ("true-like") vs. 2000 uniform-drawn ("wrong") 13-character strings,
  both respecting Z13's exact partition by construction, scored under the same empirical unigram table
  (bigram scoring deliberately not used here, since independently-drawn per-class letters have no real
  sequential structure for bigram scoring to meaningfully test). **Result: real but weaker separation than
  previously claimed** — only 1.05% of wrong draws score at or above the median true-like score, but the
  two distributions' ranges genuinely overlap at the tails. **This revises, without reversing, the prior
  conclusion**: 13 characters under Z13's actual structure carries a real statistical signal, not the
  near-total separation the earlier (structurally mismatched) pilots suggested. The practical implication:
  any future Z13 scoring attempt needs real sequential structure (genuine candidate phrases, not
  independently-drawn letters) to approach the stronger separation the bigram-scored Z408 pilots showed.
  **Update (2026-10-04), the "find a natural phrase" path is now ruled out at much higher confidence — see
  `logs/2026-10-04-sq3-natural-phrase-search-negative-result.md`**: while scoping ChatGPT's "planted-recovery
  experiment" (a real candidate phrase, encoded under Z13's exact partition, ranked for recovery against a
  pool), exhaustively scanned all 563,972 possible 13-character windows in the committed *Pride and
  Prejudice* reference text for one that naturally satisfies Z13's exact equality pattern. **Zero
  matches** — a ~1,383x larger search than the earlier Z408-based check (396 windows), still finding
  nothing. This confirms, at much higher confidence, that Z13's specific repeat structure is genuinely rare
  in real English at this length, not an artifact of Z408 being too short a corpus. Consequence: the
  planted-recovery experiment's phrase must be deliberately constructed to fit the partition, not found by
  search — a real design constraint for the next step, not a minor detail.
  **Update (2026-10-05), a second independent check on a genuinely different real text — see
  `logs/2026-10-05-sq3-z340-natural-phrase-search.md`**: reran the identical exhaustive-scan predicate
  against Z340's own solved plaintext (already sourced, hash-verified at run time against the project's
  provenance record) — 328 possible windows, **zero matches**, consistent with the Pride-and-Prejudice
  result. Explicitly disclosed as carrying far less statistical weight on its own (zero-of-328 vs.
  zero-of-563,972), but it rules out the possibility that the original null result was an artifact specific
  to one author's prose style, since Z340's plaintext shares no text with either Z408 or Pride and
  Prejudice.
  **Update (2026-10-04), the planted-recovery experiment run, 20 trials — see
  `logs/2026-10-04-sq3-bigram-chain-phrase-construction.md`**: rather than hand-picking a real phrase
  (which would reintroduce researcher discretion), constructed "true" sequences mechanically via a bigram
  Markov chain over the already-committed empirical bigram table, respecting Z13's exact partition by
  forcing repeat positions to copy their class's already-drawn letter. Ran 20 independent trials (fixed
  seed `20261004`), each scored against 2000 unrestricted alternatives under both unigram and bigram
  tables. **Bigram scoring wins decisively and consistently**: mean percentile 98.66 (range 95.40–100.00)
  vs. unigram's mean 95.63 (range 85.71–100.00) — bigram's *worst* trial (95.40%) beats unigram's *median*
  comfortably, and far exceeds unigram's own worst trial (85.71%). This is a materially more robust result
  than the earlier single-instance rankings, now backed by a real 20-trial distribution. **Still does not
  show Z13 has a recoverable answer** — only that length and structure are not inherent obstacles if a
  correct scoring approach existed. The candidate-discovery blocker is unchanged.

  **Update, later cycle — sourcing tier upgraded, one apparent discrepancy caught and resolved:**
  WebFetch access that was blocked worked this cycle. Directly fetched `zodiackillerciphers.com/408/key.html`
  first, which appeared to show a *different* distribution (T=5, A=5, I=5, O=5, N=4, S=6 distinct
  symbols) — but that page's own table conflated plaintext letter-occurrence counts with a
  separately-labeled "distinct symbols" column that doesn't hold up under its own totals. Cross-checked
  against the wiki's dedicated `Homophone_sequences` page instead (which explicitly tabulates
  distinct-symbol counts per letter, with the actual symbol characters listed): E=7, T=4, A=4, O=4,
  I=4, N=4, S=4, L=3, R=3, D=2, F=2, H=2 — an **exact match** to the distribution already used in the
  unicity-distance calculation above. This upgrades the sourcing from pure WebSearch-synthesis to two
  directly-fetched pages, with the apparent conflict traced to the first page's own table structure,
  not a real discrepancy in the underlying key. One minor, disclosed loose end: this second page's own
  stated total ("55 total symbol assignments") is off by one from the previously-recorded total of 54 —
  not reconciled, small enough to not affect the unicity-distance calculation's conclusion either way.

- **Z13 repeat-pattern structural-flexibility check: zero of 20,944
  generic length-13 English dictionary words are structurally compatible
  with Z13's reported ciphertext symbol-repeat pattern (position
  equalities 1=12, 3=11, 5=7=9, 8=13).** This is a mechanical, necessary-
  condition check (a valid homophonic key requires positions sharing a
  ciphertext symbol to share a plaintext letter; it imposes no other
  constraint), not a scoring/plausibility judgment. The zero result was
  cross-checked against an analytical expected-count null model (~0.03
  expected matches under an i.i.d.-letter approximation, consistent with
  observing zero) and confirmed not to be an implementation error via
  per-constraint counts in the hundreds to low thousands. **Sourcing
  limitation:** the repeat-pattern input itself is WebSearch-synthesis
  sourced (not a directly read primary transcription — the same disclosed
  network-egress restriction as the entry above blocked every specific
  source site tried this session too), and is a distinct, not yet
  cross-checked, claim from the separate "repeated eight-ball separator"
  note in Open Questions below. **Scope limitation, stated plainly:** this
  result is about a generic ~21,000-word ordinary-English-word corpus
  only; it says nothing about proper nouns, initials, or short phrases,
  which "My name is—" suggests may be the actually relevant candidate
  space, and must not be read as evidence for or against Z13's solvability
  either way. Reproducible script and full output:
  `methods/scripts/z13-repeat-pattern-flexibility.py` and
  `logs/2026-09-25-sq3-z13-repeat-pattern-flexibility.md`.

  **Update, later cycle — sourcing tier upgraded, pattern independently confirmed:** WebFetch access
  that was blocked in prior sessions worked this cycle for `zodiackillerciphers.com` (a
  dedicated, community-maintained cipher-research wiki, not WebSearch's own synthesis). Directly
  fetched its "Unsolved 13-character 'My name is' cipher" page, which gives an explicit ASCII
  transcription — `AENz0K0M0[NAM` — sourced by the page itself to "a scan dated April 20, 1970,
  from the San Francisco Chronicle showing the original cipher letter." Checked this transcription's
  own position-equalities directly (1-indexed): position 1 (`A`) = position 12 (`A`); position 3
  (`N`) = position 11 (`N`); positions 5, 7, 9 (`0`, `0`, `0`) all equal; position 8 (`M`) = position
  13 (`M`) — an exact match to the repeat pattern (1=12, 3=11, 5=7=9, 8=13) this project's
  dictionary-flexibility check already used, previously sourced only from WebSearch's own synthesis.
  **This upgrades the repeat-pattern input from WebSearch-synthesis tier to a directly-fetched,
  explicitly-cited-to-a-primary-scan source** — it does not yet mean this project has independently
  viewed the 1970 SF Chronicle scan itself (that remains the actual primary-source gate this
  project's own standard requires before treating any Z13 reading as settled), but it is a real,
  disclosed tier upgrade, and it independently reproduces the exact repeat structure rather than
  merely repeating the same unverified claim from a different aggregator.
- **The Statistician's own direct check is now done: Z408 and Z340 do not share a reusable homophone
  convention** (`logs/2026-09-27-sq3-statistician-homophone-comparison.md`,
  `data/external-sources/azdecrypt-doranchak-2026-09-27/`; resolves the provisional finding in Open
  Questions below). Derived both ciphers' solved keys directly (not read from a table) by aligning each
  cipher's raw transcription against its solved plaintext, sourced from David Oranchak's own AZdecrypt
  repository (cited by the peer-reviewed arXiv:2403.17350) — a credible replacement for the previously-
  rejected `enraved` source. Both derived keys pass a 0%-inconsistency internal check (vs. the rejected
  source's 47.4%), and the shared-symbol-encoding assumption needed to compare them was independently
  verified (not assumed) via a third cipher cross-check, 96.4% exact match. **Result: of 47 symbols shared
  between the two ciphers' alphabets, only 5 (10.6%) decode to the same letter in both** — confirming the
  earlier single-source estimate ("about five") at direct-data tier. No suspect-related content was read
  or cited anywhere in this process. **Open**: a formal chance-level baseline for this count has not been
  computed, so "no reusable convention" is currently a qualitative, not quantitative, conclusion.
  **Correction (2026-09-27), not a silent revision — the chance baseline has now been computed, and it
  complicates this finding**: `logs/2026-09-27-sq3-homophone-chance-baseline-selfreview.md`,
  `methods/scripts/homophone_chance_baseline.py`,
  `data/derived/homophone-chance-baseline-report.md`. A 10,000-shuffle permutation test (fixing Z408's 47
  relevant letters, randomly reshuffling Z340's own 47 letters, preserving Z340's real per-symbol letter
  distribution) gives a null mean of **2.68 coincidences** — *lower* than the observed 5, not higher.
  **P(null ≥ 5) = 0.126 — not remotely significant, and in the opposite direction from what would
  strengthen "no reusable convention."** The precise, corrected statement: the observed 5-of-47 overlap is
  statistically indistinguishable from two independently-constructed keys' chance overlap, and if anything
  mildly *exceeds* the naive chance mean rather than falling short of it. **This does not newly support a
  shared convention** (5 is still a small absolute count, and the result is nowhere near significant in
  either direction) — but the earlier framing's implicit suggestion that 5 was unusually *low* is not
  supported. The correct summary is that this specific measure is simply uninformative about whether the
  two ciphers share a convention, not that it demonstrates they don't. The bullet above is left as
  originally written per this project's no-silent-overwrite discipline; this correction supersedes its
  interpretive framing, not its raw count (5 of 47 remains accurate).

## Active Hypotheses

_(none yet)_

## Rejected Hypotheses

_(none yet — bootstrap state. As the Historian catalogues prior public
Z13 solution claims (`config/sidequests.md` SQ-4), refuted or unconfirmed
ones will be logged here with the specific reason, so they are not
re-proposed without new evidence.)_

## Open Questions

- What is the best-available, most complete, rights-clear, checksummed
  primary-source transcription/image set of Z13, Z408, and Z340 to adopt
  as this project's canonical `/data/` source? See `config/sidequests.md`
  SQ-1 — this blocks everything else.
- Given Z13's length (13 symbols), is a statistically defensible,
  crib-free solution possible at all — and if not, what would even count
  as sufficient defensible evidence for a claimed solution (an internal
  crib, cross-letter corroboration, etc.)? See SQ-3. This is the central
  open question this project must formally answer before any solution
  attempt, not resolve by default toward "it's solvable" just because
  Z408 and Z340 were. **Update (2026-09-23):** now grounded in an actual
  computed homophonic-specific unicity distance (~59 characters,
  calibrated on Z408's real documented homophone-count distribution — see
  Confirmed Findings above and
  `logs/2026-09-23-sq3-homophonic-unicity-calibration.md`) rather than only
  the simple-substitution baseline. This strengthens, but does not by
  itself close, the "likely not solvable crib-free" position — Z13's own
  homophone-set size is still unknown, and the calibration's sourcing tier
  (WebSearch synthesis, not a directly read primary table, per this
  session's disclosed network-access limitation) still needs independent
  recheck. **Update (2026-09-25):** one candidate directly-fetched
  re-derivation (a third-party GitHub repo's claimed Z408 symbol sequence)
  was tested against a basic internal-consistency requirement for a
  homophonic cipher and **failed** (47% of checked symbol occurrences
  decoded to more than one letter) — rejected, not adopted; the
  WebSearch-sourcing-tier caveat above therefore still stands unchanged.
  See `logs/2026-09-25-sq3-z408-source-verification-attempt.md` and
  `methods/scripts/verify-z408-source-enraved.py`. Kept open.
- What is Z13's actual, primary-source-verified symbol-repeat pattern
  (which of the 13 positions share a ciphertext symbol)? Two distinct,
  mutually unverified WebSearch/secondary-sourced claims are currently on
  record and must not be conflated: (1) a "repeated eight-ball symbol
  acting as a separator" (see prior entry below, from
  `logs/2026-09-23-sq1-sq3-source-and-attacksurface.md` §3), and (2) an
  8-class pattern with equalities 1=12, 3=11, 5=7=9, 8=13 (see Confirmed
  Findings above, from
  `logs/2026-09-25-sq3-z13-repeat-pattern-flexibility.md`). **Update, later
  cycle**: claim (2) has now been independently confirmed against a
  directly-fetched source (`zodiackillerciphers.com`, citing an April 20,
  1970 San Francisco Chronicle scan) — see the Confirmed Finding above. This
  narrows, but does not fully close, the question: it is still not this
  project's own direct view of the primary 1970 scan, and claim (1) (the
  "repeated eight-ball separator") remains wholly unchecked against either
  source. The primary-scan-direct-view gate for full closure remains open.
  **Update (2026-09-27): the primary-scan-direct-view gate is now closed for claim (2).** Located and
  directly viewed (not OCR'd, not AI-summarized — visually inspected after local upscaling) a genuine,
  dated, provenance-clear, public-domain extraction of the actual Z13 cipher glyphs from the 1970 letter,
  sourced via Wikimedia Commons (`data/external-sources/wikimedia-z13-name-cipher-2026-09-27/README.source.md`;
  full method and a disclosed first-read correction: `logs/2026-09-27-sq3-z13-primary-source-direct-view.md`).
  **Confirms exactly**: position 1 = position 12 (`A`=`A`); position 3 = position 11 (`N`=`N`); positions
  5, 7, and 9 all share one repeated glyph (a circled pinwheel/segmented symbol, distinct from position 4's
  circled crosshair symbol and position 10's hook shape); position 8 = position 13 (`M`=`M`) — an exact
  match to claim (2)'s pattern, now confirmed at the strongest tier available without institutional archive
  access, not merely against a secondary transcription. **Claim (1) (the "repeated eight-ball separator")
  remains unaddressed by this specific check** — not evaluated against this image, still open. No
  suspect-related content was read or cited anywhere in this process.
  **Attempted, later cycle, deliberately not pursued further**: searched for
  a purely structural source on the "eight ball as separator" claim. Found
  a real, checkable structural detail (an "eight ball" glyph reportedly at
  position 5, among others, in the 13-symbol cipher — potentially the same
  symbol already identified via `AENz0K0M0[NAM`'s repeated `0` at positions
  5/7/9 in the repeat-pattern confirmation above, which would mean these two
  "distinct" claims may in fact describe the same underlying fact from two
  research framings, not two competing structural claims) — but every
  candidate source surfaced for it also carried suspect-identification
  content, which this project's absolute ethical boundary (cipher only,
  never a suspect) prohibits repeating, citing, or building on. **Declined
  to pursue or cite those sources further this cycle.**
  **Update (2026-09-27), addressed without touching any external source at all**: now that this project
  has its own direct view of the primary Z13 image (see the repeat-pattern confirmation above), the
  position-5/7/9 repeated glyph itself was re-examined at very high magnification (no web search, no
  external claim consulted — a pure visual self-comparison of already-legitimately-sourced material).
  **Structural observation, disclosed as a judgment call, not a confirmed identity**: the glyph is a mostly
  dark/filled circle with irregular light-colored internal gaps — visually consistent with a colloquial
  "eight-ball"-style description (a solid ball marking with lighter internal detail), though no canonical
  reference image for what other sources specifically mean by "eight ball" was consulted, deliberately, to
  avoid the suspect-tainted sources already declined above. **This is compatible with, but does not prove,
  the hypothesis floated earlier** that the "eight-ball separator" claim and the "position 5=7=9 repeated
  glyph" claim describe the same underlying symbol from two different research framings. Reported as an
  honest structural impression, not a definitive match — the two claims are not hereby merged into one, but
  the plausibility of them being the same fact is now somewhat better supported by independent, source-safe
  observation than before. **A fully independent, source-external confirmation** (an authoritative
  reference discussing the "eight-ball" glyph's position/frequency without any suspect content attached)
  still has not been located and remains open — this update narrows the question via this project's own
  visual judgment alone, it does not close it.
- Do the Zodiac's two solved ciphers (Z408, Z340) share homophone-
  assignment conventions that could narrow Z13's search space in a
  principled, non-arbitrary way? Needs the Statistician's comparative
  analysis against verified solved mappings, not assumption. **Provisional
  finding (2026-09-23, single secondary source — Cipher Mysteries — not
  yet independently rechecked against the solved keys directly):** only
  about five symbol-to-letter assignments coincide between the two solved
  ciphers despite visually similar symbol styles, suggesting no simple,
  directly reusable convention currently exists. Kept open pending the
  Statistician's own direct check. See
  `logs/2026-09-23-sq1-sq3-source-and-attacksurface.md` §5.
  **Update (2026-09-27): a credible replacement candidate source for the actual solved-key data has been
  identified, but the direct check itself is still not done.** This repo's only previously-attempted
  solved-key source (`data/external-sources/enraved-zodiackillercipher-2026-09-25/`) is already marked
  REJECTED for a documented internal-consistency failure (47.4% of checked symbol occurrences decode
  inconsistently). Directly fetched and locally text-extracted (via `pypdf`, downloaded with `curl`) the
  peer-reviewed/arXiv Z340 solution paper (Oranchak et al., arXiv:2403.17350, "The Solution of the Zodiac
  Killer's 340-Character Cipher") -- purely cipher-methodology content, no suspect material read or cited.
  It contains "Figure 4: Z408 substitution key" and a comparable Z340 key figure, but **both are embedded
  as images, not extractable as text** by the tooling used this cycle -- the actual symbol-to-letter
  mappings could not be pulled from this PDF directly. The paper does cite the solver's own working
  repository, `github.com/doranchak/azdecrypt`, as the tool that produced the Z340 solution -- a much more
  authoritative candidate source for the actual key data than the rejected `enraved` repo, since it is
  cited directly by the peer-reviewed paper rather than an unattributed third-party reimplementation.
  **Not yet checked**: whether that repository's own data files contain the solved keys in a
  directly-parseable (non-image) form. This is the concrete next step, not the comparison itself.
  **Resolved, same day**: that repository's data files did contain directly-parseable solved
  cipher/plaintext pairs — the comparison has now been run. See the new Confirmed Findings bullet above
  and `logs/2026-09-27-sq3-statistician-homophone-comparison.md` for the full result (5 of 47 shared
  symbols coincide, confirming the prior provisional estimate).
- What is the actual, current evidentiary status of the various publicly
  claimed Z13 solutions, and does any survive this project's own
  falsification standard? See SQ-4. Cataloging prior claims is read-only
  research into already-public material — see the ethical boundary in
  `README.md` for what this project will and will not do with this
  catalog.
