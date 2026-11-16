# Result — A6 vs v4 static check (prediction: >=3 mismatches + restart dependence — CONFIRMED)
Script: `data/scripts/a6_static_check.py` (regex read of v4; nothing executed).
```
seed                         v4=20261012 A6=20261113+window*1000+restart (per-restart)
restarts                     v4=60       A6=20
iters                        v4=12000    A6="unchanged"
swap_prob                    v4=0.5      A6="swap-based" (unspecified)
history_dependent_restarts   v4=True     A6=False implied by per-restart seeds
single_shared_rng            v4=True     A6=False implied
```
Findings: (1) restarts 60 vs 20; (2) one shared RNG seed 20261012 vs per-window/restart seeds; (3) v4 moves are 50/50 swap/reassign, not purely swap-based; (4) restarts 3+ even-indexed perturb the best-so-far mapping, so restarts are history-dependent and "exactly 20 restarts with independent seeds" is not implementable by only changing a constant — a runner/solver change is needed.
## PROPOSED (non-binding, for the Director) A6 clarification text
"A6-clarified: solver = v4 blob 7e816706 move set (50% swap / 50% reassign), ITERS_PER_RESTART=12000 and all other v4 hyperparameters retained; RESTARTS overridden to 20; each restart r of window w is a fresh run with rng=random.Random(20261113+w*1000+r), restart 0 freq-seeded, others random-initialized (the v4 perturb-best-so-far strategy is dropped, so restarts are independent); ranking/ties as A6." Pre-score assertions: constants above, seed formula, no cross-restart state, A3 ordering and C3 generator fixtures. This is a proposal only: no freeze published, nothing run or scored. Cipher-only.
