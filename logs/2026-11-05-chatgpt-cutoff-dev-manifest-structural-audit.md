# Independent structural audit: cutoff-development manifest

**Date:** 2026-11-05 18:52 UTC  
**Scope:** arithmetic and interval checks over the two committed JSON manifests only. This did not reconstruct Project Gutenberg text, regenerate windows or controls, or verify that recorded hashes correspond to source substrings.

## Inputs

- `data/derived/cutoff-dev-set-manifest.json`
- `data/derived/known-answer-benchmark-manifest.json`

## Recomputed checks

- Cutoff-development manifest SHA256: `35fd46194c528b20a72dbbf5d730e959d48f5c9dc514b19a4573ce2564b12b5a` (matches the execution record).
- 200 items total: exactly 50 each at lengths 13, 100, 340 and 408.
- All offsets and lengths are in range of the declared 563,924-letter body.
- Indices are exactly 0–49 at every length.
- Zero overlaps among the 200 development intervals, checked globally across lengths.
- Minimum non-overlap gap among development intervals: 3 letters. No buffer was precommitted for dev-to-dev intervals, only non-overlap.
- Zero development-versus-benchmark violations of the precommitted 1,000-letter buffer.
- Recomputed minimum development-versus-benchmark gap: 1,032 letters.
- All 800 recorded SHA256 fields are distinct and syntactically valid lowercase 64-hex strings.
- Source SHA256 and body-length pins agree between the two manifests.

## Interpretation

The committed manifests satisfy their stated structural separation rules. This independently checks manifest geometry and file identity, not source extraction, deterministic generation, content hashes, scoring performance, English-register independence, cipher validity, Z13, or any suspect attribution.
