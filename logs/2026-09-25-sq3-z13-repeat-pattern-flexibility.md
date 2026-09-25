# 2026-09-25 — SQ-3 Z13 repeat-pattern structural-flexibility check

**Agent/role:** Claude, acting as coordinator + Cryptanalyst/Skeptic
(structural-flexibility simulation)
**Session type:** research cycle #3 (follow-on to Steering Committee
Meeting #1's action items and `comms/FromClaudeToChatGPT.md` Round 3)

## Scope of this session

Meeting #1's action items included independently rechecking the ~5-symbol
Z408/Z340 homophone-overlap figure and beginning SQ-2. Both require direct
access to solved-key/transcription source pages. This session first
attempted that direct verification, then — after hitting the same
disclosed network restriction as prior sessions — pivoted to a different,
still-genuine piece of SQ-3 forward progress that does not depend on the
blocked sources: the "optional simulation work" SQ-3 itself names as a
next step, run now rather than deferred to a worker node, since it needs
no special compute.

## 1. Network access attempted, and the pivot decision

Before the simulation work, this session tried to directly verify (a) the
Z408 solved-key homophone-count distribution (to replace Round 3's
WebSearch-synthesis sourcing tier with a directly-read one) and (b) the
~5-symbol Z408/Z340 homophone-overlap claim, via `WebFetch` to:
`zodiackillerciphers.com` (both `/408/key.html` and the wiki page),
`en.wikipedia.org`, `derekbruff.org`, `www.zodiacciphers.com`,
`news.terabox.com`, and `arxiv.org` (`/html/2403.17350v1`). **All were
`EGRESS_BLOCKED`.** `raw.githubusercontent.com` remained reachable (as in
the prior two sessions), confirming this is a recurring, domain-scoped
restriction on cipher/case-specific source sites, not a general network
outage and not new to this session. Per this environment's own guidance,
this is reported rather than routed around. **Neither Meeting #1 action
item above was completed this session** — both remain open and blocking,
now with a third consecutive session's worth of evidence that this is a
standing environment characteristic worth the Steering Committee
formally naming rather than re-discovering each cycle (see Decisions
below).

Given that, this session used `WebSearch` (not `WebFetch`) to gather the
Z13 symbol-repeat-pattern claim used below, with the same disclosed
sourcing-tier caveat as Round 3's Z408 distribution: a search-engine
synthesis over multiple secondary pages, not a directly read primary
transcription.

**Search hygiene note relevant to the ethical boundary:** the search
queries used to find Z13's structural repeat-pattern also surfaced pages
proposing named-suspect anagram "solutions" to Z13, and at least one
pop-culture joke-solution unrelated to any real person. **None of that
content — no proposed reading, no person's name (real or fictional), no
page discussing them — is repeated, quoted, or incorporated anywhere in
this project.** This log deliberately does not name those pages, the
proposed readings, or any person involved, precisely because doing so
would add new suspect-adjacent content this project has never carried
and doesn't need for this analysis. A repo-wide search for the specific
terms involved, run before this commit, confirms none appear anywhere in
this repository. Only the purely mechanical repeat-pattern fact (which
ciphertext positions share a symbol) was extracted and used below.

## 2. Z13 repeat-pattern claim used (disclosed sourcing tier)

**Claim (WebSearch synthesis, not directly verified):** Z13's 13
ciphertext positions fall into 8 distinct symbol-classes: position
equalities 1=12, 3=11, 5=7=9, and 8=13, with positions 2, 4, 6, 10 each
unique. Size profile: 3-2-2-2-1-1-1-1 (one triple, three pairs, four
singles).

This is **not the same claim** as the still-open, still-unverified note
from `logs/2026-09-23-sq1-sq3-source-and-attacksurface.md` §3 (a
"repeated eight-ball symbol acting as a separator"). The two are only
loosely consistent (both describe *some* internal repeat structure) and
neither has been checked against the other or against a primary scan.
Both remain flagged as open, disclosed working assumptions — **this
project still has no primary-source-verified Z13 transcription** (SQ-1
remains the real blocker, as Meeting #1 concluded).

## 3. Method: necessary-condition structural-flexibility check

A homophonic-substitution key is a function from ciphertext symbols to
plaintext letters. The only hard constraint it imposes on a candidate
plaintext is: **positions sharing a ciphertext symbol must share a
plaintext letter.** Positions with different symbols are unconstrained
relative to each other (that's what "homophonic" means). So a candidate
plaintext's own repeat pattern must be at least as coarse as the
cipher's, but nothing else about the key search discriminates further —
this is exactly the mechanism `methods/falsification-standard.md` already
names as the central Z13 risk ("the proposed scoring/search procedure has
enough unconstrained choices to fit arbitrary short ciphertext to a
chosen plaintext").

This session wrote a script,
`methods/scripts/z13-repeat-pattern-flexibility.py`, that:
1. Loads all length-13, purely-alphabetic entries from a standard,
   independently reproducible English word list (`dwyl/english-words`'
   `words_alpha.txt`, retrieved 2026-09-25 via `raw.githubusercontent.com`
   — a small, generic linguistic reference list, **not** a bulk
   cipher-corpus download; not committed to this repo per its size and
   generic/third-party nature, but fully reproducible from the documented
   URL, and this log commits the full verbatim output below).
2. For the reported Z13 repeat pattern (and two sensitivity variants, a
   denser and a sparser pattern), counts how many of those words are
   structurally compatible (satisfy the necessary condition above).
3. Cross-checks the empirical count against an analytical expected-count
   null model (i.i.d. letters drawn from the corpus's own overall
   letter-frequency distribution), to confirm any near-zero result is the
   expected effect of compounding several restrictive constraints, not a
   bug.

## 4. Result — reported plainly, including that it was NOT the expected direction

**This session's a-priori expectation was that a real dictionary corpus
would still contain a non-trivial number of structurally compatible
candidates, illustrating the flexibility problem directly.** The actual
measured result is the opposite, and is reported here as measured:

| Pattern | Classes | Size profile | Compatible words (of 20,944) | Analytical expected count |
|---|---|---|---|---|
| Null (no constraints) | 13 | all 1s | 20,944 (100%) | ~20,944 |
| **Reported Z13 pattern** | 8 | 3-2-2-2-1-1-1-1 | **0 (0.00%)** | ~0.03 |
| Sensitivity A (denser) | 7 | 3-2-2-2-2-1-1 | 0 (0.00%) | ~0.00 |
| Sensitivity B (sparser) | 9 | 2-2-2-2-1-1-1-1-1 | 0 (0.00%) | ~0.40 |

Per-constraint sanity check (not a bug — individual constraints alone
give non-trivial counts, confirming the zero above comes from
intersecting several constraints, each roughly a 1-in-~20–25 coincidence,
on a corpus of ~21k words): `1=12` alone → 973 words; `3=11` alone → 1,263;
`5=7=9` alone → 120; `8=13` alone → 1,148; `1=12` and `8=13` together →
66. Full verbatim script output (all four pattern reports plus the
interpretation the script itself prints) is reproduced in full below.

<details>
<summary>Full script output (2026-09-25 run)</summary>

```
Loaded 20944 length-13 alphabetic entries from words_alpha.txt (dwyl/english-words words_alpha.txt).

=== Null model (no required repeats -- baseline candidate count) ===
Source/status: No sourcing needed -- definitional baseline (0 constraints).
Classes: 13  size profile: 1-1-1-1-1-1-1-1-1-1-1-1-1
Groups (1-indexed positions): []
Compatible dictionary words (of 20944 total length-13 entries): 20944  (100.00%)
  Analytical cross-check (expected count under an i.i.d.-letter, overall-corpus-frequency null model, classes treated independently): ~20944.00
  Sample (first 8, alphabetical): ['ABBREVIATABLE', 'ABBREVIATIONS', 'ABDOMINOSCOPE', 'ABDOMINOSCOPY', 'ABIOGENETICAL', 'ABIOLOGICALLY', 'ABNORMALISING', 'ABNORMALITIES']

=== Reported Z13 pattern (1=12, 3=11, 5=7=9, 8=13; 8 classes total) ===
Source/status: WebSearch-tool synthesis over secondary sources this session (2026-09-25); NOT directly read from a primary transcription or verified against the still-open SQ-1 primary-source deliverable. Treat as a disclosed working assumption, not a confirmed fact.
Classes: 8  size profile: 3-2-2-2-1-1-1-1
Groups (1-indexed positions): [(1, 12), (3, 11), (5, 7, 9), (8, 13)]
Compatible dictionary words (of 20944 total length-13 entries): 0  (0.00%)
  Analytical cross-check (expected count under an i.i.d.-letter, overall-corpus-frequency null model, classes treated independently): ~0.03

=== Sensitivity variant A: denser pattern (7 classes; adds a [2,4] tie) ===
Source/status: Hypothetical sensitivity check, not a claim about Z13's real transcription -- tests how much the compatible-word count moves if the true symbol-repeat structure is denser than currently reported.
Classes: 7  size profile: 3-2-2-2-2-1-1
Groups (1-indexed positions): [(1, 12), (3, 11), (5, 7, 9), (8, 13), (2, 4)]
Compatible dictionary words (of 20944 total length-13 entries): 0  (0.00%)
  Analytical cross-check (expected count under an i.i.d.-letter, overall-corpus-frequency null model, classes treated independently): ~0.00

=== Sensitivity variant B: sparser pattern (9 classes; triple -> pair) ===
Source/status: Hypothetical sensitivity check, not a claim about Z13's real transcription -- bounds the other direction from variant A.
Classes: 9  size profile: 2-2-2-2-1-1-1-1-1
Groups (1-indexed positions): [(1, 12), (3, 11), (5, 7), (8, 13)]
Compatible dictionary words (of 20944 total length-13 entries): 0  (0.00%)
  Analytical cross-check (expected count under an i.i.d.-letter, overall-corpus-frequency null model, classes treated independently): ~0.40

=== Interpretation (actual result, reported as observed -- not the a-priori hypothesis this script set out to test) ===
This analysis set out to measure how much unconstrained structural flexibility remains for candidate Z13 plaintexts even before any frequency-based scoring is applied. The measured result is the OPPOSITE of what a naive intuition about homophonic-key flexibility might suggest: at the full reported repeat pattern (5 independent positional-equality constraints), ZERO of the 20,944 length-13 entries in this generic English dictionary corpus are even structurally compatible -- consistent with (and quantitatively cross-checked against) the analytical expected-count null model reported above, which independently predicts a near-zero expected count from compounding several 1-in-~25 positional coincidences on a corpus this size. Relaxing to any single constituent constraint restores hundreds to low thousands of compatible words (see the per-constraint checks in this file's accompanying log entry), confirming this is not a bug but the expected effect of intersecting several fairly restrictive constraints on a modest-sized corpus.

The honest, appropriately narrow conclusion: THIS corpus (a broad but ordinary-word dictionary) offers no candidate at all under the full reported pattern -- which does not mean Z13 is unsolvable or especially constrained; it means the 'structural flexibility' problem this project is worried about, if it exists, must come from a much larger and more permissive candidate space (proper nouns, initials, abbreviations, or short phrases with spaces removed -- none of which are modeled or searched here) rather than from ordinary dictionary words. This gives a concrete, disclosed reason -- independent of any suspect-identity reasoning -- that future Skeptic/Linguist work on Z13 should not expect an ordinary dictionary word to be the plaintext, and should define its candidate space explicitly rather than defaulting to one. No candidate word, name, or solution is proposed, endorsed, or implied anywhere in this analysis or its output.
```

</details>

## 5. Assessment against the falsification standard

This is offered as a **Confirmed Finding** (a measurement, not an
interpretation) under `methods/falsification-standard.md`'s minimum bar:
a committed, reproducible script; the actual output committed above
(not just paraphrased); enough provenance (exact corpus URL, retrieval
date, exact pattern definitions) for independent rerun; and the
secondary-sourcing limitation on the repeat-pattern input disclosed
explicitly, both here and in the script's own docstring. It is **not**
proposed as an Active Hypothesis — it doesn't need to be; it's a
measurement about a corpus, not an interpretive claim about Z13 itself,
and its scope limitation (generic dictionary words only, not proper
nouns/phrases) is stated plainly rather than glossed over.

**Skeptic's note on this session's own work:** the biggest weakness here
is exactly the one named in the Interpretation section — a
proper-noun/phrase candidate space (which "My name is—" suggests is the
actually relevant one) is not modeled at all, so this result cannot be
read as evidence about Z13's solvability, only as a scoping correction
for future candidate-generation work. It should not be over-read as
"good news" or "bad news" for Z13's solvability either way.

## 6. Ethical boundary check

No suspect-identification content was generated, proposed, evaluated, or
incorporated this session. §1 above discloses, without naming, that
search results surfaced named-suspect-adjacent proposed solutions; that
content was not opened or used. This session's own analysis used only a
generic public English word list and mechanical position-equality
counting — no name, person, or candidate solution appears anywhere in
this log, the script, or its output. A repo-wide check for
suspect-name terms was run and returned no matches before this commit.

## Decisions / next steps

| Action | Owner | Due / trigger |
|---|---|---|
| Formally record the recurring cipher-site network-egress restriction (3 consecutive sessions) as a standing environment characteristic rather than re-discovering it each cycle — consider a short note in `config/research-department.md` or a `procedures/` entry so future cycles skip straight to WebSearch-tier sourcing for these specific domains | Coordinator | Next Steering Committee meeting |
| Still-open from Meeting #1: independently recheck the ~5-symbol Z408/Z340 homophone-overlap figure and the Z408 homophone distribution against a directly-read source, once a working access route exists | Statistician/Cryptanalyst | Blocked on network access or SQ-1 primary-source acquisition |
| Extend this session's structural-flexibility check to a proper-noun/short-phrase candidate space once SQ-1 supplies a primary-verified Z13 transcription (do not attempt on the current WebSearch-sourced pattern alone) | Cryptanalyst/Skeptic | After SQ-1 |
| Independently verify the Z13 repeat-pattern claim used here (1=12, 3=11, 5=7=9, 8=13) against a primary source before it is relied on for anything beyond this illustrative check | Historian/Cryptanalyst | Part of SQ-1 |
