# A6 PRE-SCORE ADDENDUM D9–D12 (Research Director, design-only) — dated 2026-11-23
Applies on top of `2026-11-18-a6-operational-freeze.md` (D1–D8, not edited) and `2026-11-14-z13-pre-score-addendum-freeze.md` (A1–A8, not edited). Nothing has been scored and no source fetched. The second-register source pin is still UNFILLED, so execution stays blocked. Cipher-only; no suspect inference. Precommit: `2026-11-23-a6-addendum-c1-c3-rng-precommit.md`. Evidence: `2026-11-23-a6-addendum-c1-c3-rng-result.md`.

Unchanged: A1–A8 pass/fail thresholds, k = 5, window counts, the scoring model, the A8 prediction, D1–D3, D5–D8 semantics, and the split (+7) and C3 (+11) offsets. The committed D5/D6/D7 fixtures therefore stay valid.

| ID | Supersedes / fills | Binding rule |
|---|---|---|
| D9 Restart seed offset | Restart part of D4 only. Collision found: split (+7) ≡ restart 7, C3 (+11) ≡ restart 11, A5 Random(20261113) ≡ window-0 restart 0. That is 2,001 duplicate seeds over w < 1000, with identical CPython streams. | Solver restart r uses Random(20261113 + w*1000 + 100 + r), r = 0..19. The rest of D4 is unchanged. Assertion: the set of all generator seeds constructed in a run has no duplicates (the runner aborts otherwise). |
| D10 C1 shuffle | Gap in A1 control (C1), not covered by D4 | C1 generator = Random(20261113 + w*1000 + 13). π = list(range(n)); C1gen.shuffle(π) (one call, nothing drawn before it). C1 plaintext[i] = P[π[i]] and C1 ciphertext[i] = C[π[i]], where (P, C) is the planted window's plaintext/ciphertext. Class counts, multiplicities and the symbol↔letter key are identical to the plant by construction. If π is the identity (or C1 plaintext == P), shuffle again with the same generator, up to 100 times, then abort. |
| D11 C2 reversal | Gap: C2 occurrence assignment unspecified | C2 plaintext = reversed(P); C2 ciphertext = reversed(C). Deterministic, no RNG. Multiplicities identical. If P is a palindrome, report "C2 degenerate" for that window; it is not redrawn. |
| D12 C3 class assignment | Ambiguity in D7 ("same class structure") | Using the C3 generator (+11) only: (a) draw L = C3gen.choices(alphabet, weights, k = n) per D7; (b) enumerate feasible splits of L against the paired plant's multiplicity vector (for length 13, the A3 vector [3,2,2,2,1,1,1,1]) in D5 order. If N = 0, redraw (a) on the same stream, up to 1,000 draws, then abort fail-closed for the whole run. (c) Choose the split with C3gen.randrange(N), then do occurrence assignment per D6 and symbol labelling exactly as for the plant, all continuing on C3gen. Record the redraw count per window. Disclosed bias: this conditions C3 on letter profiles compatible with the class vector. That conditioning is what "same class structure" requires, so it is accepted, not hidden. |

## Added fail-closed assertions (on top of the freeze's 1–7)
8. No duplicate generator seed in the run (D9).
9. For C1, C2 and C3: sorted class-multiplicity vector == the paired plant's.
10. Per-window manifest records C1 π, the C3 redraw count and C3's split index, and is included in the byte-identical determinism check (assertion 6).

## Status / honesty
Design-only. D9 changes solver randomness relative to D4-as-written. Since nothing was ever run under D4, nothing reported is affected. The untested caveat about D2's perturb-drop is unchanged. A later change to D9–D12 requires a new dated freeze; this file is not edited. The next blocker is still the production runner, and after it the source-pin gate.
