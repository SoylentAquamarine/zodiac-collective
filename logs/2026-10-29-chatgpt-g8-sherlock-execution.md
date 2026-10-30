# G8 second-text known-answer diagnostic — execution

**Date:** 2026-10-29 UTC. **Status:** ChatGPT exploratory second-corpus test, following the separately committed [precommit](2026-10-29-chatgpt-g8-sherlock-precommit.md). Not independently reproduced by Claude; no Z13 reading or suspect inference.

## Inputs and reproducibility
- Corpus: [GITenberg 1661.txt](https://github.com/GITenberg/The-Adventures-of-Sherlock-Holmes_1661/blob/7e5dd2703fbf503c004063e96ab7c61262375e5f/1661.txt), commit `7e5dd2703fbf503c004063e96ab7c61262375e5f`, Git blob `70349ec04e577406123e9d89af4863cd610ccc1e`. The source README calls the book public domain; Gutenberg redistribution terms still apply. Full source not copied into this PR.
- Truth: repository `data/external-sources/azdecrypt-doranchak-2026-09-27/z408-solved.txt`, Git blob `5185e41ee50e46d70c326c7ef6a2ce8508d36828` at test time.
- Runner: `data/scripts/chatgpt_g8_sherlock_typicality.js`. From repository root, obtain the exact pinned source and run `node data/scripts/chatgpt_g8_sherlock_typicality.js /path/to/1661.txt`. The runner aborts on a source Git-blob mismatch or non-408-letter truth. The `G6` JSON key retains the reused gate name; here it reports the G8 second-text verdict.
- ChatGPT first calculated the frozen formula through the connector, then reran the committed Node runner locally with both exact Git-blob inputs. The Node output matched the first calculation for retained length, cutoffs, truth score/entropy, control counts, and verdicts. Node v24.22.1; source and truth Git blobs checked with `git hash-object`. This is same-agent implementation checking, not an independent third-party replication.
- Exact machine-readable output: `logs/2026-10-29-chatgpt-g8-sherlock-results.json`.

## Result
The precommitted cleaning retained **431,195 letters**. The primary 70/30 split supplied **317** disjoint calibration windows. The P1 score cutoff was **−2.1685** nats/transition; true Z408 scored **−2.3157**, so truth failed the score axis by **0.1472**. Its entropy **4.1557 bits** passed the entropy band **[4.0072, 4.2183]**. All **676** constant/period-2 controls were rejected; 674 failed both axes and two failed entropy only. The declared gate therefore **fails** because it rejects the known correct text. The P5/P95 and 60/40 sensitivity runs also fail. Twenty seeded letter shuffles of truth all failed the score axis; all passed the entropy axis.

The result extends the G6 failure to one preselected Doyle collection under the same model architecture. It does **not** show that every corpus fails, explain the cause of the Z408 score deficit, validate a repaired gate, or support any Z13 candidate. Do not widen cutoffs after seeing truth. A separately selected solved-cipher holdout remains missing before any use on Z13.
