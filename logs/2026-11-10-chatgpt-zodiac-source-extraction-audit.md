# Independent source-extraction audit of the frozen Zodiac manifests

**Date:** 2026-11-10 06:56 UTC  
**Scope:** independent source and substring verification for the frozen cutoff-development and known-answer benchmark manifests. No gate was scored, no Z13 candidate was evaluated, and no suspect inference is made.

## Pinned inputs

- Stored source: `data/external-sources/gutenberg-1342-2026-09-29/pride_prejudice.txt`
- GitHub blob SHA: `9c37e59d9a9162a21368f00aa4da250218dbfc01`
- Independently computed raw-file SHA256: `81300b79e8a8d65ac530a97578417d06137e3bbc90622a10a65e5036183d2500`
- Cutoff-development manifest blob: `1d3e89659161dffaab66330dab546d8866d7312b`; raw JSON SHA256: `35fd46194c528b20a72dbbf5d730e959d48f5c9dc514b19a4573ce2564b12b5a`
- Known-answer benchmark manifest blob: `2bbf9500387d0d97a0b83b7ce2be1bc2c969ad61`; raw JSON SHA256: `73eedd4166f7443670d65aec3ac0514df7aaa3a70340b87c0df2ab355dfac3d0`

## Independent method

A separate JavaScript implementation (not either repository Python manifest generator) extracted the text between the exact Project Gutenberg 1342 start/end markers, lowercased it, and retained ASCII `a-z`. It then recomputed SHA256 over each manifest's `body[offset:offset+len]` substring and over each reversed substring.

## Results

- Raw source SHA256 matches the source pin exactly.
- Normalized body length: **563,924 letters**, matching both manifests.
- Windows checked: **400** (200 development + 200 benchmark).
- True-window SHA256 mismatches: **0/400**.
- Reverse-control SHA256 mismatches: **0/400**.
- Distinct true-window hashes: **200/200** in each manifest.
- Minimum development-to-benchmark gap: **1,032 letters**, exceeding the frozen 1,000-letter buffer.
- Cutoff-development manifest SHA256 matches the frozen execution record exactly.

## Limits and interpretation

This closes the source-substring verification gap explicitly left open by the earlier PR #16 structural audit. It does **not** independently regenerate Python's seeded shuffle or unigram-random controls, rebuild either manifest from its generator, verify the upstream GITenberg commit, or score any calibration gate. Both manifests use disjoint offsets from the same book, so they are not independent samples of English. No plaintext, decipherment, or suspect claim follows.

## One next action

The Research Director should review this source-extraction audit alongside PR #16 before authorizing any scoring; preserve the frozen cutoffs and the single-book/register limitation.
