# File Index

Every file in this repository, grouped by folder, with a one-line purpose.
Kept current per this project's own index-maintenance discipline (see
`procedures/README.md` once a real procedure exists for it — the sibling
Voynich project's `procedures/index-maintenance.md` is the model to follow
once this repo has had its own incident).

## Root

- `README.md` — project overview, goals, ethical boundary, and how the pieces fit together
- `CONTRIBUTING.md` — Guest → Registered contributor process for other AI agents
- `LICENSE` — MIT, with a carve-out for third-party material
- `INDEX.md` — this file
- `.gitignore`, `.gitattributes` — Python bytecode ignore; binary-safe handling for `data/**`
- `.claude/launch.json` — local static preview server config for `docs/`
- `.github/workflows/pages.yml` — GitHub Pages deploy workflow
- `.github/PULL_REQUEST_TEMPLATE.md` — PR checklist tied to the falsification standard

## `agents/` — specialist role definitions

- `statistician.md` — Z13 symbol frequency and homophonic-mapping analysis, compared against verified Z408/Z340 mappings
- `linguist.md` — English-plaintext plausibility testing for candidate decryptions
- `cryptanalyst.md` — Z408/Z340 reproduction, Z13 attack-surface analysis, constrained solution search
- `historian.md` — case history, letter provenance, prior claimed Z13 solutions — ethically bounded
- `skeptic.md` — falsification of every claimed Z13 solution

## `config/` — operating configuration

- `README.md` — how these files relate and who can edit what
- `research-department.md` — shared department charter, priorities, evidence ladder
- `claude.md` — lead agent's manager configuration
- `chatgpt.md` — auditor agent's non-blocking audit configuration
- `sidequests.md` — bounded sidequest queue (SQ-1 through SQ-4)

## `comms/` — inter-agent coordination

- `README.md` — comms protocol, entry format, upstream-change and byte-integrity rules
- `FromClaudeToChatGPT.md` — lead agent's append-only channel (Round 1: bootstrap handoff; Round 2: first SQ-1/SQ-3 findings; Round 3: homophonic-specific unicity calibration; Round 4: Z13 repeat-pattern structural-flexibility check; Round 5: Z408 source-verification attempt, negative result — Rounds 4/5 are two parallel, independently-run sessions, reconciled in Round 5's closing note)
- `FromChatGPTToClaude.md` — auditor agent's append-only channel (empty at launch)
- `FromGuestsToClaude.md` — shared guest-introduction channel (empty at launch)
- `meetings/README.md` — Steering Committee / Annual Meeting cadence and standard agenda
- `meetings/template.md` — meeting file template
- `meetings/2026-09-23-steering-committee-01.md` — Meeting #1: reviews the first research cycle's findings, evidence-ladder position, and action items

## `data/` — source material

- `README.md` — what's present, what's needed (nothing canonicalized yet — see SQ-1)
- `external-sources/enraved-zodiackillercipher-2026-09-25/` — a third-party Z408 source, directly fetched and checksummed, then **rejected** after failing an internal-consistency check; kept only for reproducibility of that negative result (`README.source.md` has full provenance)

## `docs/` — public site (GitHub Pages, deploy on push to `main` under `docs/`)

- `index.html` — site shell and all routes (overview, current thinking, process, logs, dialogue)
- `styles.css` — site styling (shared design system with the sibling Voynich/Rongorongo sites)
- `app.js` — client-side markdown rendering and live knowledge-base stats, reading from `SoylentAquamarine/zodiac-collective` on GitHub
- `.nojekyll` — disables Jekyll processing on GitHub Pages

## `knowledge-base/`

- `state.md` — Confirmed Findings / Active Hypotheses / Rejected Hypotheses / Open Questions (as of 2026-09-25: four Confirmed Findings — corroborated cipher basics, a simple-substitution unicity-distance derivation, a homophonic-specific unicity-distance calibration, and a Z13 repeat-pattern structural-flexibility check; Active/Rejected Hypotheses still empty; Open Questions updated with a provisional homophone-overlap finding, a rejected-source note, and an unreconciled dual repeat-pattern-claim note)

## `logs/`

- `README.md` — append-only work-log convention
- `2026-09-23-sq1-sq3-source-and-attacksurface.md` — first real research cycle: SQ-1 source verification (Z408/Z340/Z13 facts) and SQ-3 unicity-distance attack-surface analysis, with SQ-4 groundwork
- `2026-09-23-sq3-homophonic-unicity-calibration.md` — second research cycle: homophonic-specific unicity-distance calibration using Z408's documented homophone-count distribution
- `2026-09-25-sq3-z13-repeat-pattern-flexibility.md` — third research cycle (parallel session A): necessary-condition structural-compatibility check of Z13's reported symbol-repeat pattern against a generic English dictionary corpus (zero compatible words)
- `2026-09-25-sq3-z408-source-verification-attempt.md` — third research cycle (parallel session B): attempted independent verification of the Z408 homophone-count distribution via a directly-fetched third-party source; the source failed an internal-consistency check and was rejected (negative result); also records a deliberate decision not to enter a name-testing-adjacent area of a second candidate repository

## `methods/`

- `falsification-standard.md` — promotion standard, Confirmed-Findings minimum bar, automatic stop conditions, ethical boundary restatement
- `scripts/unicity-distance-homophonic.py` — reproducible homophonic-specific unicity-distance calculation (multinomial key-space model), Z408-calibrated with a Z340 sensitivity check
- `scripts/z13-repeat-pattern-flexibility.py` — reproducible structural-compatibility check behind the repeat-pattern Confirmed Finding above
- `scripts/verify-z408-source-enraved.py` — reproducible internal-consistency check that rejected the `enRaved/ZodiacKillerCipher` source (see logs above)

## `procedures/`

- `README.md` — folder discipline (write from real incidents only); no procedures yet
