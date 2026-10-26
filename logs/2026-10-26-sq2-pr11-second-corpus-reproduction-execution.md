# SQ-2 — independent reproduction of PR #11 — execution

Precommitment: `logs/2026-10-26-sq2-pr11-second-corpus-reproduction-selfreview.md` (written before running). Script: `data/scripts/sq2_z408_second_corpus_reproduction.py`; output `data/derived/sq2-pr11-second-corpus-reproduction-output.txt`.

**Result:** pinned corpus blob hash verified (0d8e53fc...); every score in ChatGPT's PR #11 table reproduces exactly to one decimal (whole file 260,898 letters; marker-bounded 245,714). Order 3 gap -27.1 / -31.5, order 4 -273.8 / -279.1. Truth loses to the wrong v3 decode at all four orders on both preparations. Prediction held.

**Meaning:** the earlier finding that the failure is not corpus-specific is strengthened: a second, closer-register-ish (late-Victorian crime fiction) corpus does not repair the objective. Still one corpus and one cipher; says nothing about Z13, and no suspect inference.

**Dispositions:** PR #11 accepted as independently reproduced (left unmerged: log lives on its branch; merging is the user's call). PR #10 (public-site calibration note): its statements check against the repo (v4 = 42/408 per `logs/2026-10-21-sq2-z408-v4-unigram-penalty-execution.md`; scoring ranks wrong output above truth), but it edits the public site, so left for the user. Agree with the proposed next step: freeze a score design and pass/fail gate (truth must outrank frozen wrong decodes plus held-out controls) before any more solver search.
