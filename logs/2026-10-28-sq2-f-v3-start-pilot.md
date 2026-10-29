# SQ-2 — exploratory F-objective Z408 search from the frozen wrong v3 mapping

**Date:** 2026-10-28 UTC. **Status:** ChatGPT exploratory diagnostic for review, not a solved-cipher validation or Z13 result. The test design was stated in the ChatGPT conversation before execution, but no repository precommit file was written. Do not describe it as a preregistered experiment.

## Inputs and fixed method

- Cipher: `data/external-sources/azdecrypt-doranchak-2026-09-27/z408-cipher.txt`, GitHub blob `7dfc1c66c472903783bb7c6d0bb99faaac63b705`.
- Known plaintext (opened only after the search loop): `data/external-sources/azdecrypt-doranchak-2026-09-27/z408-solved.txt`, blob `5185e41ee50e46d70c326c7ef6a2ce8508d36828`.
- Corpus: `data/external-sources/gutenberg-1342-2026-09-29/pride_prejudice.txt`, blob `9c37e59d9a9162a21368f00aa4da250218dbfc01`; letters between the START/END markers, A–Z only (563,955 letters).
- Initial wrong decode: `data/derived/sq2-z408-hillclimb-v3-result.md`, blob `f6034efd9f2c295bbbd013c138ef1c315d3c54be`. Each of 54 cipher symbols maps consistently to a letter.
- Frozen score F is Claude's order-4, add-0.5 Lidstone conditional score: sum of natural logs of `(quadgram_count+0.5)/(trigram_context_count+13)` over 405 windows. The exact script is `data/scripts/sq2_f_v3_start_pilot.js`.
- One seeded search: xorshift32 seed 20261028, start at v3's symbol mapping, maximum 100,000 proposals and 60 seconds, 50% two-symbol assignment swaps and 50% single-symbol reassignments, annealing temperature `4*0.9999^t`. This executed 97139 score evaluations within 5801 ms. This is one bounded search, not a search-budget sweep.

## Observed output

| Text | F score (nats) | Known-plaintext match |
|---|---:|---:|
| Original v3 wrong decode | -993.884 | 125/408 (from Claude's committed v3 record) |
| Best F-optimized wrong decode in this pilot | -967.308 | 145/408 (35.54%) |
| True Z408 text, evaluated after search | -906.954 | 408/408 |

The search raised v3's F score by 26.576 nats and its match count by 20. The best wrong decode still trails the true text by 60.354 nats. This establishes only that this particular start, move set, seed and budget did not find a wrong output above truth. It does not show that F is robust to stronger optimizers, other starts, another corpus, or a second solved cipher. No Z13 text or suspect was tested.

## Output decode

```
ESENENESSISTMEEMSEHESEADIETEWNORASHFANETITRERENASTHERNESSESTNESSTEREINTHEFERNEDTHESAAWERESENTHIREATHERTERTAEESARESENESSTENESSWERETHENTTIRENRETHEROATTHRESSESTERMINERSEETIDERESHETTERTHENTITTESTEEARNESNWEFNNETHATERSTHEHENTMERTOFITEATHEENHEREHEEINESSHENEHERSENMERESESITSHESSTHEIHERENESSESNESSHESEREREDSAREWENESSSETTEREEEARENEREHESEANEEEANESSTRETODSEEHENSENTTOMRESESSISTESTENDSEREWFERREAFTERSENEIHEEREETIRETHHMETI
```

## Decision

Keep the F calibration gate open. A stronger search protocol and a second solved-cipher holdout are needed before this objective can support Z13 work. Preserve the earlier finding that the floor-smoothed quadgram scorer and orders 1–3 fail the frozen wrong-output control; this exploratory result does not reverse it. The public site's current wording remains unchanged.

## Separate executable rerun (2026-10-28)

ChatGPT fetched the script and all four pinned text inputs from GitHub into a clean scratch tree and ran `node data/scripts/sq2_f_v3_start_pilot.js` from its root. The process exited 0 and reproduced exactly: 97,139 evaluated proposals; initial score −993.8836502912634; best score −967.3081290690794; truth score −906.9540631004104; 145/408 matches; and the complete decode printed above. Wall time was 158 ms on this host and is not a frozen result. This is a separate execution of the same code and inputs, not an independent algorithm or adversarial review; Claude's reproduction remains open.

## Exploratory 100-seed extension (2026-10-29 UTC)

To test sensitivity to random initialization, ChatGPT ran the **same v3 start, objective F, move set, 100,000-proposal cap, and 60-second cap** with xorshift32 seeds 20261028 through 20261127 inclusive (100 searches). The runner `data/scripts/sq2_f_v3_start_multiseed.js` differs from the pilot only by reading the seed from argv and reporting it; SHA-256 `0ada695fa0e288c0b138f871ef931609f40de3604ba90d37c305ca757025e343`. Run from repo root with `node data/scripts/sq2_f_v3_start_multiseed.js 20261028`; the batch loops over the stated integer range. Full per-seed JSON, including every decode, is `logs/2026-10-29-sq2-f-v3-multiseed-results.json`, SHA-256 `114a2512b1be3cf76a1cc4a92e2231ee1df14f0f33f9eaf71552624b21c14084`. The four input blobs and corpus extraction are identical to the pilot above.

Across 9,714,637 evaluated proposals, mean best F score was −979.625 nats. The highest F score was **−965.4434552183326** at seed 20261039 (107/408 known-text characters), 58.489 nats below the true-text score −906.9540631004104. No seed found an output at or above truth; the lowest best score stayed at the initial −993.884. The best F score here has *lower* character accuracy than the original single-seed pilot (107/408 versus 145/408), illustrating that score improvement is not a monotone reading improvement.

This seed range and batch were chosen after inspecting the single-seed pilot; the test is exploratory, with no preregistration, no new start mapping or move family, and no second solved cipher. A hundred starts from the same wrong mapping do not validate F or a Z13 interpretation. A different optimizer or holdout could still falsify F. No website claim is promoted.
