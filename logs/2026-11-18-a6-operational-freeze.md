# A6 OPERATIONAL FREEZE (Research Director, design-only) — dated 2026-11-18
Adopts, as BINDING, the eight decisions below, to be applied on top of `2026-11-14-z13-pre-score-addendum-freeze.md` (A1-A8, not edited) before any planted or Z13 scoring. No code run, no source fetched, nothing scored. Cipher-only; no suspect inference. Responds to ChatGPT #103-#106 ("Director publishes dated, hash-pinned A6 freeze resolving all eight decisions and naming the source").

## Crosswalk (9 raw items -> 8 decisions)
| Decision | Raw items folded in | Binding rule |
|---|---|---|
| D1 Restart count | cycle-88 #1 (v4 60 vs A6 20) | Exactly 20 restarts per ciphertext; ITERS_PER_RESTART=12000 and all other v4 hyperparameters retained. |
| D2 Restart independence/history | cycle-88 #4 | Restarts are independent fresh runs; restart 0 frequency-seeded, restarts 1-19 random-initialised; v4's perturb-best-so-far is DROPPED. No state crosses restarts. |
| D3 Move set | cycle-88 #3 | v4 move set kept: 50% swap / 50% reassign. ("swap-based" in A6 means this v4 move set.) |
| D4 RNG schedule | cycle-88 #2 (shared vs per-restart seeds) + cycle-90 #3 (A5 stream vs A6 seeds) — one decision | Random(20261113) is used ONLY for window selection (A5). Everything else uses per-window generators: split = Random(20261113+w*1000+7); C3 letters = Random(20261113+w*1000+11); solver restart r = Random(20261113+w*1000+r). w = window_index in draw order. |
| D5 Feasible-split enumeration | cycle-90 #1 | Enumerate feasible splits in lexicographic order of the tuple (group size per distinct letter, letters in order of first occurrence); choose index rng.randrange(N) from the split generator. |
| D6 Occurrence assignment | cycle-90 #2 | Within a letter, occurrences are assigned to groups by seeded shuffle of the occurrence-index list (split generator, continuing its stream after D5), groups taken in descending size. |
| D7 C3 control | cycle-90 #4 | C3 = len(window) letters drawn i.i.d. from unigram letter frequencies of the window's own plaintext source register over the pinned source text, using the C3 generator's .choices over letters in alphabetical order; same class structure as the paired window. |
| D8 Duplicate plaintexts | cycle-90 #5 | Candidates deduplicated by plaintext string before ranking; best score among duplicates retained; ties broken by lexicographic plaintext (A6); report "ties present". |

## Second-register source (UNFILLED — gate)
No source is named, because none is authorized. The runner MUST abort unless a separate dated `source-pin` file exists giving (a) exact file/URL, (b) SHA-256, (c) explicit user authorization reference, (d) confirmation it is not Gutenberg 1342 and is public-domain. Naming one here without authorization would be fabricating a gate pass.

## Fail-closed runner assertions (must pass before the first planted score)
1. Constants: RESTARTS==20, ITERS==12000, swap prob 0.5, no call of perturb_mapping on a prior-restart mapping.
2. Exactly one Random() construction per (window, restart) plus the two per-window generators (+7, +11) and one window-selection stream; no module-level shared RNG used in solving.
3. Z13-class multiplicity vector of every length-13 plant == [3,2,2,2,1,1,1,1] (A3).
4. Window disjointness / buffer asserts per A5; n=100 windows per length per register (A2).
5. Source-pin file present and SHA-256 of the loaded text matches it.
6. Determinism check: two runs of the generator with identical inputs produce byte-identical ciphertext manifests.
7. Unit fixtures for D5/D6/D7 (tiny hand-computed cases) written and passing BEFORE any score.

## Pinned inputs (SHA-256, computed 2026-11-18; the freeze file's own hash is recorded in comms/state because a file cannot contain its own hash)
- data/scripts/sq2_z408_hillclimb_solver_v4.py = debb2ec643b7922858795cb96f5d1f9308899fc19ecd1b06bea901f78e6d96d9 (git blob 7e816706009e6272e9ea74433353bd54385de9f1)
- logs/2026-11-13-z13-planted-recovery-protocol-freeze.md = b58ede1802d958f6b1764b9d016aca77e43790c453af7af1b625faa0e6e69338
- logs/2026-11-14-z13-pre-score-addendum-freeze.md = e14a7b74ec7eb102894104a58401bddfbc9c40208b9b75c72b4f1e38b84d4633
- logs/2026-11-16-cycle88-a6-static-check-result.md = b1fe5b1961bb7955285c0343b812dc9d79ca87d6d70edef776ff35c2822a69dd
- logs/2026-11-16-cycle90-a6-runner-gaps-result.md = 17f209861ca98c634ee97c9da8a80e05024db78cc1b8e68a3f5800d67ba48b71

## Status / honesty
Prediction in A8 unchanged (length 13 fails; 34/100 pass). Untested caveat: dropping v4's perturb-best-so-far (D2) changes solver behaviour relative to the v4 results already reported; its effect is unmeasured and will be reported, not assumed negligible. Any later change to D1-D8 requires a new dated freeze; this file is not edited. Execution stays blocked on the source-pin gate; compute is not the bottleneck.
