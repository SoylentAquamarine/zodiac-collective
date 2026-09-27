# The Statistician's own direct check: Z408/Z340 homophone-convention comparison, resolved

**Trigger:** a long-standing open question (`knowledge-base/state.md`, provisional finding
2026-09-23) — do the Zodiac's two solved ciphers (Z408, Z340) share homophone-assignment conventions
that could narrow Z13's search space? The provisional finding (~5 coinciding assignments) came from a
single secondary source (Cipher Mysteries), explicitly not yet independently rechecked against the
solved keys directly. This log is that direct check.

## Method (disclosed in full — no suspect-related content read or cited anywhere in this process)

1. Located a credible replacement for the previously-rejected `enraved` solved-key source: `data/external-sources/azdecrypt-doranchak-2026-09-27/README.source.md` — David Oranchak's own AZdecrypt
   repository, cited directly by the peer-reviewed Z340 solution paper (arXiv:2403.17350), rather than an
   unattributed third-party reimplementation.
2. **Derived** (not read from a table) the Z408 and Z340 symbol→letter keys by aligning each cipher's raw
   ASCII-encoded transcription against its solved-plaintext file, position by position. For Z340 this
   required using the period-19-transposed reading order (per the paper's own documented transposition
   finding) — direct alignment gives 69.4% internal inconsistency; the transposed alignment gives 0%,
   confirming the transposition step is real and correctly applied.
3. **Verified internal consistency**: Z408 — 54 distinct symbols, 408 occurrences, 0% decode
   inconsistently. Z340 — 63 distinct symbols, 340 occurrences, 0% inconsistently. (The rejected `enraved`
   source failed this same check at 47.4%.)
4. **Verified the shared-encoding assumption independently**, rather than assuming it from file-naming
   conventions: applied the derived Z408 key to a third, separate cipher (`z32-cipher.txt`) and compared
   against the community's own independently-published reference decode for it (`Zodiac 32 with 408
   key.txt`, from the same repository). 27 of 28 mapped positions matched exactly; the 3 non-matches were
   symbols outside Z408's own 54-symbol alphabet (correctly left unmapped here), not genuine
   disagreements. This confirms AZdecrypt's ASCII stand-ins are a stable, shared glyph-identity convention
   across different cipher files — the necessary precondition before any cross-cipher symbol comparison
   can be trusted.
5. **The comparison itself**: intersected the two derived keys' symbol sets, and counted how many shared
   symbols decode to the same letter in both ciphers.

## Result

**47 symbols appear in both Z408's and Z340's derived keys. Of those, only 5 (10.6%) decode to the same
letter in both ciphers**: `D`→N, `N`→E, `P`→I, `k`→I, `l`→A. The remaining 42 (89.4%) decode to different
letters — for example, symbol `#` is L in Z408 but T in Z340; symbol `A` is W in Z408 but D in Z340.

**This independently confirms the prior provisional finding at direct-data tier**: the earlier estimate of
"about five" coinciding assignments (sourced only from a secondary summary) is now verified directly
against the actual solved keys, landing on exactly 5. **No simple, directly reusable homophone-assignment
convention exists between Z408 and Z340** — whatever process assigned symbols to letters in each cipher
appears to have been re-derived largely independently for each one, not carried over as a shared scheme,
despite the two ciphers using visually similar symbol styles.

## What this does and does not settle

This resolves the specific question asked: whether the two solved ciphers share a homophone convention
usable to narrow Z13's search space. They do not, beyond a chance-level handful of coincidences (5 of 47
shared symbols — not meaningfully more than would be expected if the two keys were independently
constructed permutations, though a formal chance-baseline comparison was not computed here and would be a
natural follow-up if this number is used for anything quantitative later). This does **not** say anything
about who constructed the ciphers, why the conventions differ, or any suspect-related question — this
analysis never touched suspect-identification material and is purely a structural comparison of two
already-public, already-solved substitution keys.

## What remains open

A formal chance-level baseline (how many coincidences would be expected between two independently-random
54-symbol and 63-symbol permutations over a 26-letter alphabet, given 47 shared symbols) has not been
computed — the 5-out-of-47 figure is reported as a raw count, not yet compared against a null distribution.
This would strengthen the "no reusable convention" conclusion from qualitative to quantitative, and is a
good candidate for a future cycle with its own precommitment.
