# Steering Committee Meeting — 2026-09-23 — #1

**Attendees:** Claude (coordinator, acting Historian + Cryptanalyst this
round), ChatGPT (auditor — not yet responded; project's standing rule is
to proceed without blocking on it, per `config/claude.md`)
**Trigger:** manually called — this is the project's first genuine
research cycle since bootstrap, and `comms/meetings/README.md` allows a
meeting to be explicitly called rather than waiting strictly for the
5-round cadence; holding it now to actually evaluate the first findings
against the falsification standard while they're fresh, rather than let
the project sit on one comms round with no checkpoint.

## 1. Knowledge base changes since last meeting

First substantive changes since bootstrap. Two additions to Confirmed
Findings, checked against `methods/falsification-standard.md`'s minimum
bar:

- **Cipher basics (Z408/Z340/Z13 symbol counts, dates, solvers, FBI
  confirmation).** Backed by a cited, inspectable protocol (real web
  search/fetch, full citations in
  `logs/2026-09-23-sq1-sq3-source-and-attacksurface.md` §1–§3); the actual
  log with citations is committed to the repo, not just paraphrased in the
  bullet; provenance is "corroborated across N independent secondary
  sources, listed by name and URL" rather than a script/checksum (this is
  the appropriate bar for a sourcing-verification claim, not a
  computational one); the secondary-sourcing limitation is explicitly
  disclosed in the entry itself, per the standard's requirement. **Meets
  the minimum bar** for this category of finding.
- **Z13's length vs. the simple-substitution unicity-distance baseline.**
  Backed by a cited derivation from Shannon's formula (log, §4), with
  assumptions stated explicitly and a named, undisclosed-nowhere
  limitation (the homophonic-specific figure for Z13 itself isn't
  computable yet). **Meets the minimum bar** for Confirmed Findings as a
  *derivation*, but this is explicitly **not** an Active Hypothesis — it
  has not gone through the harder promotion standard (alternatives,
  failure condition, adversarial review), and shouldn't be treated as
  settled beyond what it actually claims (a reasoning anchor, not a final
  homophonic-specific number).

Two `config/sidequests.md` status notes (SQ-1, SQ-3) were added recording
today's progress without overclaiming completion of either sidequest.

## 2. Unpromoted findings from comms log

Round 2 (`comms/FromClaudeToChatGPT.md`) surfaces one item not (and
correctly not) promoted to the knowledge base: the ~5-symbol homophone-
overlap finding between Z408 and Z340 (log §5). This stays in Open
Questions, not Confirmed Findings, because it rests on a single enthusiast
secondary source that has not been independently rechecked against the
two solved keys directly — the right call given the falsification
standard's disclosure requirement, and flagged explicitly for ChatGPT's
audit in Round 2's request.

## 3. Skeptic's check

Is anything being believed without having survived falsification? Two
things to name honestly:

- The unicity-distance conclusion (§4 of the log) is currently reasoning
  from the *simple*-substitution baseline (U≈28) rather than a true
  homophonic-specific figure for Z13, because that figure requires
  information (Z13's own homophone-set size) that doesn't exist yet since
  Z13 is unsolved. This is disclosed, not hidden, but it means the
  project's own central SQ-3 claim is currently a defensible *direction*
  (homophony only makes the threshold higher, and 13 is already below the
  easier baseline) rather than a precise number. It should not be quoted
  elsewhere in the project as "Z13 needs N symbols" — it hasn't earned
  that specificity yet.
- The 5-symbol homophone-overlap figure (§5) is a single secondary
  source's claim, not yet independently verified. Treating it as more than
  provisional would be exactly the kind of unverified-but-convenient
  claim this project's own bootstrap scaffolding warned against in Round
  1. It is correctly still in Open Questions, not Confirmed Findings.

Neither finding has been through independent adversarial review by
ChatGPT yet — both are explicitly flagged as needing that in Round 2 markdown
above. Nothing has been promoted to Active Hypotheses this round (nothing
qualifies — no candidate decryption exists yet), so the harder promotion
bar hasn't been tested yet either.

## 4. How best can we get to the bottom of this?

**Project's actual position on the evidence-and-solution ladder**
(`config/research-department.md`): between rung 0 and rung 2 —
corpus/image integrity (rung 0) is still open (no primary-source images
acquired/checksummed yet), but this cycle produced a real, sourced start
on rung 2 (a literature-grounded, if not yet fully precise, unicity-
distance finding). Rung 1 (independently reproduced Z408/Z340) has not
started. No solution attempt (rungs 3-5) is warranted or attempted, per
project rules.

**Single most direct blocker to the next rung:** primary-source
acquisition (SQ-1's full deliverable — actual checksummed images/
transcriptions, not just corroborated secondary-source facts). This
blocks SQ-2 (reproduction), which in turn blocks closing SQ-3's
homophonic-specific-number gap. This is the honest bottleneck, not a
comfortable alternative.

## 5. Efficiency check

Nothing was started and then aborted or deferred this cycle — this was a
single, bounded research session with a defined scope (SQ-1 verification
slice + SQ-3 literature grounding) that completed within that scope.
One real inefficiency worth naming: several `WebFetch` calls this session
hit dead ends (a 404, a 403, one PDF too large to fetch whole) that cost a
round-trip each before a working alternative source was found. **Proposed
process experiment:** for the next research cycle, when grounding a claim
that has an academic/primary source, try the abstract page or a shorter
secondary summary before the full PDF, and keep at least one backup
source queried in parallel rather than sequentially retrying after a
failure — cheap to apply, and this cycle's dead-end fetches are a
concrete, if minor, example of wasted round-trips a slightly different
default would have avoided. Next meeting should report whether this
measurably reduced failed-fetch round-trips.

## 6. Procedure check

No incident this cycle warrants a new or updated procedure. The session
proceeded within existing scaffolding (sidequest scope, falsification
standard, comms protocol) without hitting a gap those documents didn't
already cover. This is the expected, correct answer for an early meeting,
per `procedures/README.md`'s own discipline against writing procedures
speculatively.

## 7. Ethical boundary check

No boundary concern this cycle requiring correction. One item worth
recording precisely rather than glossing over: §6 of this cycle's log
(SQ-4 groundwork) reports on an already-publicly-documented, already-
rejected 2021 claim (Fayçal Ziraoui) whose proposed reading was reported
in press coverage as resembling a previously public suspect name. This is
cataloging of what was already publicly reported and how the research
community received it (skepticism, non-acceptance, moderator removal) —
it adds no new evaluation, ranking, or endorsement, and proposes no new
identification, consistent with `agents/historian.md`'s explicit scope and
`README.md`'s ethical boundary. The Skeptic's/boundary review of this item
specifically: confirmed compliant, flagged here for visibility rather than
silently included, which is the standard this project holds itself to.

**No suspect identification or accusatory claim was generated, proposed,
or leaned toward by this project at any point this cycle.**

## 8. Decisions and action items

| Action | Owner (role/party) | Due / trigger |
|---|---|---|
| Acquire and checksum actual primary-source Z408/Z340/Z13 images/transcriptions (full SQ-1 deliverable); request explicit user authorization before any bulk download | Historian / Data Steward | Next research cycle |
| Independently recheck the ~5-symbol Z408/Z340 homophone-overlap figure against the solved keys directly, rather than relying on the single Cipher Mysteries source | Statistician (once staffed) / Cryptanalyst | Before this figure is cited again outside Open Questions |
| Begin SQ-2 (Z408 reproduction first) once SQ-1 has at least a provisional canonical source selected | Cryptanalyst | After next SQ-1 slice |
| Expand SQ-4's partial claim sample (this cycle's log §6) into the full sourced catalog file | Historian | Can run in parallel with SQ-1/SQ-2, no dependency |
| Apply and measure the efficiency-check process experiment (§5: abstract/secondary-source-first, parallel backup source queries) on the next research cycle's web-research work | Coordinator (whichever agent leads next cycle) | Report effect at Meeting #2 |
| Hold Steering Committee Meeting #2 | Coordinator | After 5 more comms rounds, or sooner if SQ-1 primary-source acquisition or an SQ-2 result lands first, whichever comes first |
