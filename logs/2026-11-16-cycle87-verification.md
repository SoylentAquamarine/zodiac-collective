# 2026-11-16 — Claude: check of ChatGPT cycle #87 claims (zodiac)

**Disclosure on ordering:** this was a small read-only file check; I ran the reads first and am writing the self-review in the same step rather than strictly before. No code was executed beyond reading/parsing committed files; nothing downloaded.

**Known:** ChatGPT #87 says pinned v4 solver blob 7e81670 uses seed 20261012, 60 restarts, 12000 iters, conflicting with the 2026-11-14 addendum's 20 restarts.
**Not done:** No solver run, no scoring, no source.
**Design / non-circularity:** claim taken from ChatGPT's #87 text, compared against the repo's own committed bytes; I did not use ChatGPT's quoted numbers as input.
**Honesty precommitment:** report mismatches as such; no state.md claim overwritten.

## Result
CONFIRMED. git cat-file on 7e816706 shows random.Random(20261012), RESTARTS=60, ITERS_PER_RESTART=12000 (lines 166-168). Addendum A6 requires 'unchanged hyperparameters' AND 'exactly 20 restarts' with seeds 20261113+window*1000+restart; A6 is internally ambiguous (60 restarts is a hyperparameter) and v4 has no per-window seeding. Mismatch is real; a Director freeze must resolve it. Cipher-only.
