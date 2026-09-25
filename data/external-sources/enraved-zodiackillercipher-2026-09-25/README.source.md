# Source provenance — `enRaved/ZodiacKillerCipher` (rejected source)

**Status: REJECTED.** These files are kept for reproducibility of a
negative verification result, not as trusted reference data. See
`logs/2026-09-25-sq3-z408-source-verification-attempt.md` and
`methods/scripts/verify-z408-source-enraved.py` for the full check and
its result.

- **Origin:** https://github.com/enRaved/ZodiacKillerCipher — a public,
  third-party (non-official) repository implementing a Hidden-Markov-Model
  attack on the Z408 cipher.
- **Retrieved:** 2026-09-25, via direct HTTPS `curl` to
  `raw.githubusercontent.com/enRaved/ZodiacKillerCipher/master/<file>`
  (not a WebSearch summary).
- **License/rights:** repository has no explicit license file identified
  at retrieval time; these two small source files are kept here only as
  evidence supporting this project's own reproducible rejection of them
  as a data source, not redistributed as reference material.
- **Files and checksums (SHA-256):**
  - `Zodiac.c` — `ee64096de67e8b2404752f4ebc5703d20861d05ed96f1e1fe0fb5cf445d5e6ce`
  - `Z408.txt` — `615041837f8a212a0767f2f5d6d28e5a0287fab5d70a8a05c53a0c2d6012eafc`
- **Why rejected:** the embedded `observationSequence` array fails a basic
  internal-consistency check for a homophonic substitution cipher (47.4%
  of checked symbol occurrences decode to a different letter than an
  earlier occurrence of the same symbol) — see the script and log for the
  full derivation. **Do not use this source's derived homophone counts,
  key, or symbol numbering anywhere in `knowledge-base/state.md`.**
