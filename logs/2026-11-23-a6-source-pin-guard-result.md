# Result: A6 production-runner source-pin guard audit — 2026-11-23

Precommit: \`logs/2026-11-23-a6-source-pin-guard-precommit.md\` (committed before the formal rerun). Scope remains cipher-only; no source retrieval, no solver run and no scoring.

## Finding and correction

The prior production entry point accepted \`pin=None\` and proceeded without assertion 5. When a pin tuple was supplied, the old helper only searched the pin text for a caller-supplied hash string; it did not calculate SHA-256 from the loaded normalized text.

The revised code:
- separates \`generate_manifest()\` for explicitly synthetic fixture tests from production \`run()\`;
- makes \`run()\` abort when the source-pin path is absent;
- requires a \`normalized_text_sha256: <64 lowercase hex>\` field;
- restricts the supplied normalized string to non-empty A–Z;
- computes SHA-256 from the actual loaded normalized-text bytes and compares it with the pinned value.

The pin-file field is an interface contract for the future source pin. It does not itself establish source provenance, public-domain status or user authorization; those remain separate mandatory checks.

## Formal local test result

The updated generator/test implementation was exercised on synthetic text only (20,000 letters generated with \`Random(1)\`, six-letter skewed alphabet; not a source and not natural language).

**17/17 checks passed**, including:
- D5 hand cases and N=0;
- deterministic byte-identical manifests;
- 30 synthetic length-13 windows and plant/C1/C2/C3 multiplicity properties;
- 2,001 duplicate instances in the D4 reference schedule over w=0..999;
- zero collisions in the D9 schedule across 23,001 seed instances (1,000 windows plus the register-selection stream);
- production entry abort without a pin;
- rejection of a mismatched normalized-text hash;
- acceptance of a matching synthetic pin for the generator-only entry point.

Synthetic manifest SHA-256: \`1fc162b7576e0496ba71a5d03b1146d19a52e90341f6d528bfb2ab082972eac1\`.

The branch's updated script and test files were fetched back from GitHub after publication.

## Explicitly unresolved

- This is still a **length-13 generator half**, not the full D14 13/34/100 pipeline.
- D5 enumeration at lengths 34 and 100 still needs a count/unrank implementation that preserves the frozen lexicographic order, or a Director ruling.
- D10's in-place versus reset-before-re-shuffle wording remains open; the implementation was not changed.
- Text normalization, exact second-register source and source pin remain open.
- Solver integration, assertions 1–2 and solved-cipher known-answer tests are not implemented.

No real source was read, fetched or scored. No Z13 result and no suspect inference.
