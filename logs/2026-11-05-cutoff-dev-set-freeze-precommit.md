# Disjoint cutoff-development set FREEZE (non-Zodiac text) — precommitment self-review

Written 2026-11-05 (cycle ~18:00 UTC) BEFORE the script was written or run. Responds to ChatGPT 2026-11-05 16:00 handoff:
"freeze a disjoint cutoff-development set before scoring this manifest" (and "do not tune thresholds before a disjoint cutoff set exists").

**Known.** The 200-item benchmark manifest (seed 20261105, pinned GITenberg 1342, SHA256 81300b79...) is frozen and unscored.
Its acceptance criteria (>=90% true accepted, >=95% each control rejected, per length) require any gate's cutoffs to be set
only on data disjoint from that manifest. Director confirmation of the 90/95 criteria is still pending.

**Not done.** No cutoff set exists; no gate is designed; nothing is scored. This log builds ONLY a second manifest (hashes + offsets).

**Design (non-circular).** Same pinned source, same normalisation, lengths 13/100/340/408, 50 windows each, different seed
(20261106). Each dev window must (i) not overlap any benchmark window and (ii) not overlap any other dev window, and (iii) sit
at least 1000 letters from every benchmark window (a buffer so neighbouring-text correlation is reduced; the buffer size is a
design choice, not derived from a result). Controls C1 shuffle / C2 reverse / C3 unigram-random as before. Only offsets and
SHA256 are recorded. The script reads the benchmark manifest offsets, so the benchmark file is not modified.

**Prediction.** Structural only: deterministic rebuild (identical hashes on two runs), 0 overlaps within dev, 0 overlaps/buffer
violations against the benchmark. No outcome of any gate is predicted because none is computed.

**Limits (stated up front).** Same single book, so dev and benchmark share author, register and vocabulary; disjoint offsets do
not make them independent samples of English. A second-register text and a true solved-cipher benchmark remain open. A cutoff
fit here is only evidence about this register.

**Honesty precommitment.** Report hashes and checks exactly as produced; if a check fails, log the failure. No gate scoring.
