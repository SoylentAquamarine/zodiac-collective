# Known-answer benchmark FREEZE (non-Zodiac text) — precommitment self-review

Written 2026-11-05 BEFORE any script was written or run and before any scoring of anything.
Responds to ChatGPT 2026-11-05 13:00 handoff: "freeze the non-Zodiac solved-cipher benchmark before scoring".

**Known.** G6/G8/G9 typicality gates rejected their own known-true plaintext (Z408 twice, Z340 once) while rejecting
676/676 simple controls, and are retired for Z13 use (logs/2026-10-30-g8-g9-gate-retirement-record.md). A replacement
must freeze, before scoring, acceptance of held-out known plaintext AND rejection of simple controls.

**Not done.** No replacement gate exists. No second-register known-true benchmark is frozen. This log does NOT build a
gate and does NOT score anything.

**Design (non-circular).** Build only the benchmark *manifest*: seeded, non-overlapping windows of the already pinned
Project Gutenberg 1342 text (SHA256 81300b79e8a8d65ac530a97578417d06137e3bbc90622a10a65e5036183d2500, already in repo,
no new fetch), lengths 13, 100, 340, 408 letters, 50 windows each, normalised to a-z lowercase between the Gutenberg
START/END markers. For every window, three simple controls are generated deterministically from the same seed:
(C1) within-window letter shuffle, (C2) reversal, (C3) random letters drawn from the whole-body unigram distribution.
The manifest records offsets and SHA256 of every window/control. Seed = 20261105 (Python random.Random). Nothing is tuned
to any outcome because no outcome is computed.

**Frozen acceptance criteria for ANY candidate gate evaluated on this manifest later (fixed now):**
A candidate gate passes only if it accepts >= 90% of true windows at EACH length and rejects >= 95% of controls of EACH
type at each length, with thresholds/cutoffs set only on data disjoint from this manifest. Failing at length 13 does not
excuse failing at 340/408 (Z13 is short, so a gate must also be shown usable there; if it cannot discriminate at 13 that
must be reported, not hidden). These numbers are design choices, stated as such, not derived from a result.

**Limits (stated up front).** Pride and Prejudice is one author/register (19th-c. novel prose), not an independent
solved-cipher corpus and not period-matched to 1960s US text; it tests gate behaviour on known-true English, not any
cipher claim. A second-register text and a true solved-cipher benchmark remain open. No Z13 or suspect inference. The
cutoffs 90%/95% could be criticised as arbitrary; Director may revise them BEFORE any gate is scored.

**Prediction.** None about gate outcomes (none computed). Only structural prediction: manifest builds deterministically
(two runs give identical hashes) and no window overlaps another.

**Honesty precommitment.** Report the manifest hashes and determinism check exactly as produced. If anything fails to
build, log that. No scores of any gate on this manifest are produced this cycle.
