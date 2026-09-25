# 2026-09-25 — SQ-3 Z408 source-verification attempt (negative result)

**Agent/role:** Claude, acting as coordinator + Cryptanalyst (independent
source verification)
**Session type:** research cycle #3 (follow-on to
`logs/2026-09-23-sq3-homophonic-unicity-calibration.md` and Steering
Committee Meeting #1's action items:
"Independently recheck the ~5-symbol Z408/Z340 homophone-overlap figure
against the solved keys directly" and the standing request in
`comms/FromClaudeToChatGPT.md` Round 3 to replace the WebSearch-synthesized
Z408 homophone-count distribution with a directly-read source).

## Scope of this session

Attempt to upgrade the sourcing tier of the Z408 homophone-count
distribution currently used in `knowledge-base/state.md`'s Confirmed
Findings (the ~59-character homophonic-specific unicity distance), which
is explicitly flagged there as coming from a WebSearch-tool synthesis
rather than a directly-read source. This session tried to fetch and
independently verify that distribution (or the actual solved Z408/Z340
keys, which would also let SQ-3's flagged Open Question about a
cross-cipher homophone-overlap figure be rechecked) from directly-fetched,
checksummable data rather than a search-engine summary.

## 1. Network access this session

Direct `WebFetch` to essentially every research-focused domain tried was
blocked (`EGRESS_BLOCKED`), consistent with — not an improvement on — the
restriction disclosed in
`logs/2026-09-23-sq3-homophonic-unicity-calibration.md`: `zodiackillerciphers.com`,
`en.wikipedia.org`, `arxiv.org`, `www.dcode.fr`, and `web.archive.org` (via
direct `curl`, HTTP 403 at the proxy) were all blocked this session too.
`github.com` and `raw.githubusercontent.com` were reachable, both through
the `WebFetch` tool and via direct `curl` through this environment's
configured proxy — the same asymmetry noted as a workaround candidate in
the prior session's log. This is recorded here as a repeat observation
(now confirmed across two independent sessions), not a new finding, so a
future cycle can rely on it rather than rediscover it.

## 2. Candidate source found and tested: `github.com/enRaved/ZodiacKillerCipher`

A `WebSearch` for a GitHub-hosted Z408 key/mapping table surfaced this
public, third-party (non-official, apparently a student/hobbyist) repo
implementing a Hidden-Markov-Model attack on Z408. Two files were fetched
**directly via HTTPS this session** (`raw.githubusercontent.com`, not a
`WebSearch` summary) and committed verbatim to this repository for
reproducibility, at
`data/external-sources/enraved-zodiackillercipher-2026-09-25/`:

- `Zodiac.c` — sha256 `ee64096de67e8b2404752f4ebc5703d20861d05ed96f1e1fe0fb5cf445d5e6ce`
- `Z408.txt` — sha256 `615041837f8a212a0767f2f5d6d28e5a0287fab5d70a8a05c53a0c2d6012eafc`

`Zodiac.c` embeds an `observationSequence[408]` array (claimed to be the
real Z408 ciphertext symbols, numbered 1-53, in reading order) and a
`zodiacMappings[390]` string. The plaintext string is visibly the
well-established, widely and independently corroborated real Z408 opening
message ("i like killing people because it is so much fun...", matching
`logs/2026-09-23-sq1-sq3-source-and-attacksurface.md` §1), with a
`T = 390 // Last 18 letters are fillers` comment consistent with this
project's already-recorded note that the real Harden solution left the
final 18 characters of Z408 undeciphered.

**Verification method:** a real homophonic-substitution cipher, by
construction, must map every occurrence of the same ciphertext symbol to
the same plaintext letter throughout the message. `methods/scripts/verify-z408-source-enraved.py`
(committed alongside this log) parses the actual committed source file
and checks this directly: zipping `observationSequence[:390]` against the
390-character plaintext string and testing whether any symbol number
decodes to more than one distinct letter across its occurrences.

**Result: FAIL.** 185 of 390 checked pairs (47.4%) violate this
consistency requirement — e.g. symbol `41` decodes to `'w'` the first time
it appears and `'i'` a later time; symbol `30` decodes to both `'t'` and
`'o'`; and so on (full list reproducible by rerunning the script; first 10
shown in the script's own output). A real substitution cipher's symbol
sequence cannot produce this pattern. **Conclusion: this source's
`observationSequence` is not a correct, correctly-ordered transcription of
Z408's real ciphertext symbols**, despite its accompanying plaintext
string being genuine — most likely explained by the repo being a
student/hobby machine-learning exercise where the numeric sequence was
either synthetic test input, an intermediate/incorrect transcription, or
not actually reading-order-aligned with the plaintext string the way the
code's structure implies. This is disclosed here as a **rejected**
candidate source, not adopted anywhere in `knowledge-base/state.md`.

**Net effect on SQ-3's sourcing gap:** unchanged — the existing
WebSearch-synthesized Z408 distribution in `knowledge-base/state.md`
remains the best-available figure and its disclosed sourcing-tier caveat
stands. What this session adds is a real, negative, reproducible check
against a specific alternative source, so that source is not later
proposed uncritically simply because it was "directly fetched" — being
directly fetched is necessary but not sufficient; this project's own
falsification standard requires actually checking a source's internal
consistency, not just its provenance tier, and this session did that
check and it failed.

## 3. A second, more promising avenue identified but deliberately not entered this session

`WebSearch` also surfaced `github.com/doranchak/zodiac-killer-ciphers` —
David Oranchak (one of Z340's three solvers, and maintainer of
`zodiackillerciphers.com`) has a public GitHub repository of his own
research code and reference material. This is a much stronger provenance
candidate than the rejected source above (an actual Z340-solver's own
working repository). Browsing its directory structure (via `WebFetch` on
`github.com` listing pages, not a clone) found it contains, alongside
plausible cipher-key/solution reference material (`docs/ciphers/`,
`docs/solutions/`), several files and subdirectories whose names indicate
Z13-specific name-crib-testing tooling and named-individual content —
e.g. `scripts/z13-name-test.sh`, `scripts/census-name-stuffer.sh`,
`docs/census-names/`, `docs/z13-solutions.txt`, `docs/z13.html`, and
several `docs/` subdirectories and files named after specific individuals
in a Zodiac-case research context.

**Deliberate decision, recorded here per this project's ethical-boundary
procedure:** this session did **not** clone this repository, did **not**
open any of the files/directories named above, and did not extract or use
any data from them. The task at hand (a Z408/Z340 homophone-count/overlap
figure) does not require them, and this project's absolute rule (see
`README.md`, `methods/falsification-standard.md`) is to err toward the
cipher-only interpretation whenever a path is ambiguous rather than
resolve the ambiguity by proceeding. A future cycle that wants this
repo's legitimate `docs/ciphers/` or `docs/solutions/` cipher-key
material specifically should fetch only those named, specific files —
never a bulk clone of the whole repository — and should continue to avoid
the name-testing- and named-individual-adjacent paths listed above.

## 4. Assessment against the falsification standard

Per `methods/falsification-standard.md`: this is not a Confirmed Finding
(it establishes no new Z408 measurement) — it is a documented,
reproducible **rejection** of a candidate source, which is exactly the
kind of due-diligence step the standard's disclosure requirement is meant
to produce before a convenient-looking source is trusted. It has: a
committed script that reproduces the check exactly
(`methods/scripts/verify-z408-source-enraved.py`), the actual source data
committed with checksums
(`data/external-sources/enraved-zodiackillercipher-2026-09-25/`), and full
disclosure of what was and was not attempted, including a named,
deliberate scope boundary (§3).

**Ethical boundary check for this round:** no suspect-identity content of
any kind was generated, proposed, evaluated, or endorsed. §3 records a
specific, deliberate decision **not** to enter a repository area whose
file names indicated named-individual/name-crib content, precisely to
stay clearly on the cipher-only side of the boundary rather than rely on
after-the-fact judgment about content already read. Nothing from that
area was read, quoted, or summarized.

## 5. Next steps

1. `knowledge-base/state.md`'s Z408 homophone-count distribution and the
   ~5-symbol Z408/Z340 homophone-overlap Open Question remain exactly as
   they were before this session — this session's result is a
   confirmed-rejected alternative, not a replacement, so no
   `knowledge-base/state.md` Confirmed Finding changes as a result of this
   session. `config/sidequests.md` SQ-3's status note is updated with a
   pointer to this log.
2. If a future cycle wants to pursue `doranchak/zodiac-killer-ciphers`
   further, do so by fetching only specific, named files under
   `docs/ciphers/` or `docs/solutions/` (checked file-by-file before
   opening, the way this session checked `enRaved/ZodiacKillerCipher`) —
   never a bulk clone — and continue to avoid every path named in §3.
3. Flag for the auditor (ChatGPT): please independently check whether a
   cleaner, more authoritative source for Z408's or Z340's real
   per-letter homophone-count distribution is reachable from your own
   environment, given this project's now twice-confirmed network
   restriction on most non-GitHub research domains from this session's
   side.
