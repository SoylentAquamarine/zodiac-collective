# Source provenance — `doranchak/azdecrypt` (accepted, verified source)

**Status: ACCEPTED.** This is the replacement candidate identified this cycle for the solved-key data
that the previously-attempted `enraved/ZodiacKillerCipher` source was rejected for (see
`../enraved-zodiackillercipher-2026-09-25/README.source.md`). Unlike that source, this one is cited
directly by a peer-reviewed academic paper as the solver's own working tool, and its internal consistency
has been independently verified here, not assumed.

- **Origin:** https://github.com/doranchak/azdecrypt — David Oranchak's own AZdecrypt cryptanalysis
  software repository, the tool used to solve Z340 (Oranchak, Blake, Eckler & Van Eycke, 2020;
  documented in the peer-reviewed writeup arXiv:2403.17350, "The Solution of the Zodiac Killer's
  340-Character Cipher", which explicitly cites this repository).
- **Retrieved:** 2026-09-27, via direct HTTPS `curl` to
  `raw.githubusercontent.com/doranchak/azdecrypt/main/AZdecrypt/Ciphers/Zodiac%20ciphers/<file>`
  (not a WebSearch summary, not the application itself — only the plain-text cipher/plaintext data files
  bundled with it).
- **License/rights:** repository ships a `LICENSE` file (not reproduced here); these small plain-text
  cipher-transcription files are kept only as evidence supporting this project's own independently-run
  verification, not redistributed as a claim of rights over the software itself.
- **Files and checksums (SHA-256):**
  - `z408-cipher.txt` — `dc7fc0390193d385515ab767133d8ee226f46ea58ba82acdb078bcc6d566be37` (raw Z408
    ciphertext, ASCII stand-ins for the actual glyph symbols, 24×17 grid)
  - `z408-solved.txt` — `c543b998bea7faf0f3706250b6b46014d6e1e1803f9a07d956b6af0c7ea6b5d6` (Z408
    plaintext solution, same 24×17 grid, line-aligned with the cipher file)
  - `z340-cipher.txt` — `57f30eb681bfadebec81a03d7af2e0f8ecdfff2ae60138389ae1c5d44d9f00f8` (raw Z340
    ciphertext, original reading order, 20×17 grid)
  - `z340-solved-transposed.txt` — `769193f4b876efdf030336b161f25051a40b1b38a66a9563ad483aff6288dce0`
    (Z340 plaintext solution, rewritten into the period-19-transposed reading order that aligns
    position-by-position with `z340-cipher.txt` — see verification method below)
  - `z32-cipher.txt` — `bbb5403988b7a58493615c5db1773f1a7dae88d26a4200f35008e076c1482e9a` (a short,
    separate 32-character cipher used only as an independent cross-check, not analyzed for its own
    content)

## Why accepted: verification method and result

Unlike the rejected `enraved` source, this project did not merely trust the file pairing — the key was
derived and checked directly:

1. **Key derivation**: position-by-position alignment of each cipher file against its solved-plaintext
   counterpart produces a symbol→letter mapping directly (no key table needed, no OCR of the
   image-embedded key figures in the arXiv paper).
2. **Internal-consistency check** (the same check the `enraved` source failed): for Z408, 54 distinct
   symbols, 408 total occurrences, **0% decode inconsistently** (vs. the rejected source's 47.4%). For
   Z340 (using the period-19-transposed alignment, per the paper's own documented transposition-cipher
   finding — direct, untransposed alignment gives 69.4% inconsistency, confirming the transposition step
   is required and correctly applied), 63 distinct symbols, 340 occurrences, **0% inconsistent**.
3. **Cross-cipher validation of the shared-symbol-encoding assumption**: the Z408-derived key was applied
   to the separate `z32-cipher.txt` (a distinct 32-character cipher) and compared against the community's
   own independently-published reference decode (`Zodiac 32 with 408 key.txt`, from the same repository).
   Result: 27 of 28 mapped positions matched exactly (96.4%); the 3 remaining positions were symbols
   absent from Z408's own 54-symbol alphabet, correctly left unmapped on this project's side while the
   reference (drawing on broader canonical knowledge) filled them in. This confirms AZdecrypt's ASCII
   stand-ins represent a stable, shared glyph-identity convention across different cipher files, not an
   arbitrary per-file assignment — the necessary precondition for any cross-cipher symbol comparison.

See `logs/2026-09-27-sq3-statistician-homophone-comparison.md` for the full analysis this source enabled.
