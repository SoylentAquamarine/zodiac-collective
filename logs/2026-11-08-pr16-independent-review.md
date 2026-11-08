# Claude review of PR #16 (ChatGPT structural audit of the cutoff-development manifest), 2026-11-08

**Process disclosure.** The check was a short read-only recomputation; I ran it before writing this file, so this record is written post hoc rather than as a precommitment. The design was fixed by the PR's own list of checks (I reproduced each, with my own code, from the two committed manifests only): no source text fetched, no gate scored, cipher-only, no person implicated. Prediction (stated informally beforehand): all PR claims reproduce.

**Result: every checked claim in PR #16 reproduced.**
- SHA256 of `cutoff-dev-set-manifest.json` = `35fd4619...12b5a` (matches).
- 200 dev items, 50 each at lengths 13/100/340/408; idx exactly 0-49 per length; all intervals within the 563,924-letter body.
- 0 dev-dev overlaps, minimum gap 3 letters; dev-vs-benchmark minimum gap 1,032 (>= 1,000 buffer).
- Hash fields: 1,600 across both manifests (800 dev + 800 benchmark), all distinct lowercase 64-hex. (The PR states 800 for the dev manifest; consistent.)
- Source SHA256 and body length agree between manifests.

**Not checked (same limits as the PR):** source extraction, hash-to-substring correspondence, deterministic regeneration. Recommendation: PR #16 is accurate and hedged; I recommend merge. I did not merge (Director decision). No frozen score was run.
