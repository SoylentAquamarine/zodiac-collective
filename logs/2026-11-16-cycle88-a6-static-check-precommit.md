# 2026-11-16 — Claude: static A6-vs-v4 consistency check (precommit)

**Known:** ChatGPT #88: A6 says "swap-based ... unchanged hyperparameters ... exactly 20 restarts ... per-window/restart seeds" but v4 has seed 20261012, 60 restarts, 12000 iters, 50/50 swap/reassign. I confirmed constants in #87 check.
**Not done:** no runner, no solver run, no planted trial, no Z13 score, no second-register source.
**Design / non-circularity:** a read-only script parses v4 source text (regex only, never executes/imports it) and prints each A6 requirement vs the v4 value. Additionally inspect whether restarts are independent (v4 restarts >=3 perturb best-so-far, which would make per-restart seeds not independently reproducible). Takes only committed bytes as input.
**Prediction:** >=3 mismatches (restarts, seed schedule, move mix wording) plus a restart-dependence finding. **Honesty precommitment:** report if fewer; I only *propose* an A6 clarification text for the Director — it is not a freeze and changes nothing. Cipher-only; no suspect inference.
