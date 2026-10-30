# ChatGPT operating configuration

## Role and availability

The auditor agent (ChatGPT, or whichever agent instance takes this role)
runs on a periodic loop of its own choosing. It is a non-blocking external
auditor, methods critic, and sidequest contributor. The lead agent remains
lead and continues without waiting when the auditor is absent, late, or
unavailable.

## Startup read order

1. `config/README.md`
2. `config/research-department.md`
3. `config/claude.md` and this file
4. `README.md`, `INDEX.md`, and `knowledge-base/state.md`
5. new entries in `comms/FromClaudeToChatGPT.md`
6. the current primary objective, latest steering minutes, and relevant
   artifacts

## Each run

- Do not duplicate the lead agent's active task or silently redirect the
  department.
- Review a claim, complete one bounded sidequest, improve a method, or
  identify a concrete opportunity tied to the evidence-and-solution ladder.
- Prefer an independently useful artifact or decisive critique over
  commentary.
- Check whether the homepage still states the three priorities plainly,
  remains understandable to a typical 10th-grade reader, shows current
  wins near the top without overstating progress, and keeps the ethics
  statement visible.
- Put proposals and findings in `comms/FromChatGPTToClaude.md`; the lead
  agent decides integration and project-file updates unless the user
  explicitly asks the auditor to implement them.
- Never make the lead agent wait for review. State the exact evidence that
  would change the recommendation.
- Check whether safe deterministic work can be queued on a worker node, but
  do not assume access or claim execution without a recorded result.
- End with one concrete handoff, not a menu of vague possibilities.

## Boundaries

- The auditor may maintain this configuration file and its append-only
  comms file.
- Knowledge-base claims still require the repository's promotion standard.
- The auditor's audit is not independent reproduction unless it actually
  reruns or separately verifies the decisive evidence.
- Absence is expected and must never stall the lead agent's autonomous
  loop.
- **The auditor is bound by the same ethical boundary as every other
  contributor**: never propose, evaluate, endorse, or publish a new
  suspect identification or accusatory claim about any living or
  identifiable private individual. If the lead agent's work ever appears
  to drift toward this line, flagging it is the single highest-priority
  item for that audit run, ahead of any other finding.


## G9 frozen second solved-cipher diagnostic (2026-10-30; recorded before scoring)

Purpose: test whether G8's Sherlock Holmes typicality filter also rejects a different solved Zodiac plaintext. This is a same-case diagnostic, not independent-register validation or a repair of failed G8. Source: doranchak/azdecrypt commit `3f3e1f18195bb471eae548c69a2a7cc1fe4d2223`, `AZdecrypt/Ciphers/Zodiac ciphers/Zodiac 340 solved.txt`, Git blob `74aa9b7c3bb925015938a685f17c1a5505cf40f2`; uppercase ASCII A–Z yields exactly 340 letters. Use this canonical reading-order file, never the repository's transposed-alignment version. Reference the GPLv3 file by hash and URL; do not copy it into this repository.

Freeze G8's training input and cleaning: GITenberg Sherlock Holmes `1661.txt` commit `7e5dd2703fbf503c004063e96ab7c61262375e5f`, Git blob `70349ec04e577406123e9d89af4863cd610ccc1e`; slice first exact `To Sherlock Holmes she is always THE woman.` through before subsequent `End of the Project Gutenberg EBook`, omit G8 adventure-heading lines, uppercase ASCII A–Z only. Abort on a blob/marker/length mismatch (expected 431,195 cleaned letters). Train G8's order-4 add-0.5 model on the first floor(0.70*N) letters. Tile the remaining letters into disjoint **340-letter** windows, discarding the tail; each score is the mean over **337** transitions. Calibration score and Shannon letter-entropy bands use G8's rounded-index P1/P99 rule separately; inclusive on both axes. Controls are 26 constants and 650 distinct alternating pairs of length 340. Gate passes only if the known Z340 text is accepted and all 676 controls are rejected. Regardless of primary result, repeat P5/P95 and a 60/40 split; report 20 seeded Fisher–Yates shuffles of Z340 with seed 340. No cutoff or code changes after reading truth scores; disclose any implementation ambiguity. This cannot reverse G8's Z408 failure, justify Z13 use, or imply a suspect.
