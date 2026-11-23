# Result — D4 seed-collision check + C1/C2/C3 addendum (ChatGPT #154)

Precommit: `logs/2026-11-23-a6-addendum-c1-c3-rng-precommit.md`, written before any code was run.

## Seed enumeration (python3, stdlib `random`; w = 0..999, D4 as frozen)
- 2,001 seeds collide, in exactly the three predicted families:
  - (A5 window-selection, window-0 restart 0) × 1
  - (split, restart 7) × 1000 (every window)
  - (C3 letters, restart 11) × 1000 (every window)
- No cross-window collisions.
- `Random(s)` constructed twice with the same s gives identical draws (checked).
- **Prediction CONFIRMED.** Under D4 as written, restarts 7 and 11 of every window would replay the cipher-construction draws, which contradicts D2's independence intent.
- Proposed schedule (restarts at +100+r; C1 at +13): **0 collisions** over w < 1000, including the A5 seed.

## Decision
Issued `logs/2026-11-23-a6-addendum-d9-d12-freeze.md`, SHA-256 `f69e8b753f07d59c8159f71b959efd323674e7f17eb43c7c389f0710c34109ce`. It pins the 2026-11-18 freeze at `84214972df42ba149c7d8bfe08a93791deab98b938824570d6b3bf1f96768a41`, as of today.
- D9: restart offset moved to +100+r.
- D10: C1 is a joint plaintext/ciphertext index permutation from Random(+13).
- D11: C2 is the joint reversal.
- D12: C3 is drawn by rejection sampling to feasibility, then split, assignment and labelling continue on the C3 stream.
Split (+7) and C3 (+11) are unchanged, so the D5/D6/D7 fixtures (58/58 per ChatGPT #152/#153) remain valid.

## Not done
No production runner, nothing scored, no source fetched; the source pin is still unfilled. The addendum is design-only and cipher-only, with no suspect inference.
