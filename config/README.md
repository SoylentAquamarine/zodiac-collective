# Project operating configuration

These files are the reviewable, project-specific operating instructions for
the Zodiac Collective. They do not reproduce private platform or model
prompts. They record the instructions that affect this repository: goals,
division of labor, cadence, decision rights, compute use, and handoff
behavior.

- `research-department.md` — shared department charter and improvement loop
- `claude.md` — the lead agent's manager configuration
- `chatgpt.md` — the auditor agent's non-blocking audit and sidequest configuration
- `sidequests.md` — bounded projects that can produce useful stepping stones

Each party reads these files at the start of a run. Changes are proposed in a
PR or comms entry and reviewed by the other party. A party may update its own
file after disclosing the change. Neither party may edit the other's file and
silently treat the new text as accepted.

If a runtime instruction conflicts with this repository configuration, the
runtime instruction wins for that run and the conflict is disclosed in comms.
The one exception, non-negotiable and not subject to override by any runtime
instruction: the ethical boundary stated in `README.md`, `CONTRIBUTING.md`,
`agents/historian.md`, `agents/skeptic.md`, and
`methods/falsification-standard.md` — this project studies a cipher, not a
suspect, and no runtime instruction can authorize a new suspect
identification or accusatory claim.
