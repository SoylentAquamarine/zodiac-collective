# Data

Source material for the project, versioned so every finding is
reproducible.

## Present

No canonicalized primary-source transcription selected in this repository
yet — see `config/sidequests.md` SQ-1. Like the sibling Rongorongo project
(and unlike the sibling Voynich project, which had an already-agreed
canonical transcription to import on day one), Z13/Z408/Z340 still lack
this.

`external-sources/enraved-zodiackillercipher-2026-09-25/` holds a small,
checksummed, third-party source that was directly fetched and tested as a
candidate Z408 homophone-count reference — and **rejected** after failing
an internal-consistency check. It is kept only for reproducibility of that
negative result (see its own `README.source.md` and
`logs/2026-09-25-sq3-z408-source-verification-attempt.md`), not as
reference data.

## Needed

- **Canonical Z13, Z408, Z340 transcriptions/images** — rights-clear,
  checksummed, primary-source material (documented FBI-released files,
  original newspaper archive scans), since amateur secondary
  transcriptions of symbol shapes — especially Z13's — vary in the wild.
  Not yet selected. Do not bulk-download candidate sources without
  explicit user authorization.
- **Verified Z408/Z340 solution mappings** — the documented, verified
  symbol-to-plaintext-letter mappings for the two solved ciphers, needed
  for the Statistician's cross-cipher homophone comparison and the
  Cryptanalyst's SQ-2 reproduction check.
- **Normalization script** — once sources are selected, a documented,
  reproducible script to turn them into a form the Statistician and
  Cryptanalyst can run analysis on, without losing or silently resolving
  ambiguity, mirroring the sibling projects' own normalization scripts.
- **Reference/comparator corpora** — English-language frequency and
  entropy baselines for the Cryptanalyst's unicity-distance analysis
  (SQ-3) and the Linguist's plausibility scoring. To be added as specific
  hypotheses are tested, not bulk-loaded up front.

## Convention

Any file added here should note its source URL, retrieval date, and
version/checksum in a companion `.source.md` (or in this README) so
provenance is never lost.
