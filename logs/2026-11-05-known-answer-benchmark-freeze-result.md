# Known-answer benchmark freeze — result (follows precommitment of the same date)

Built with `data/scripts/known_answer_benchmark_manifest.py` (python3 -I) on the pinned GITenberg 1342 file (SHA256 verified in-script).
Output `data/derived/known-answer-benchmark-manifest.json`, SHA256 `73eedd4166f7443670d65aec3ac0514df7aaa3a70340b87c0df2ab355dfac3d0`.

- 200 items (50 each at 13/100/340/408 letters) over a 563,924-letter normalised body; every item has SHA256 for the true window and controls C1 shuffle, C2 reverse, C3 unigram-random.
- Determinism: second run byte-identical (cmp). Overlap check: 0 overlapping windows of 200. Both structural predictions held.
- No gate was scored. Frozen acceptance criteria (>=90% true accepted per length; >=95% each control rejected per length; cutoffs set only on data disjoint from the manifest) stand as written in the precommitment; Director may revise them before any scoring.
- Plaintext windows are not committed (only offsets+hashes); they regenerate from the pinned text.
- Still open: a second-register text and a true solved-cipher benchmark; same-author caveat from G8/G9 is NOT fixed by this (single novel register). No Z13/suspect inference.
