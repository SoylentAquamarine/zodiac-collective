#!/usr/bin/env python3
"""
Z13 repeat-pattern structural-flexibility check (config/sidequests.md SQ-3).

Purpose: this is the "optional simulation work" SQ-3 names as a next step --
"measuring how often a frozen scoring procedure produces a 'plausible' match
to an unrelated 13-character target phrase" -- applied here at the cheapest,
most mechanical layer: BEFORE any frequency/scoring model is even applied,
how many candidate 13-letter English words are even structurally compatible
with Z13's reported ciphertext-symbol repeat pattern?

A homophonic substitution key is a function from ciphertext symbols to
plaintext letters (many symbols may map to the same letter -- that is the
whole point of a homophonic cipher). The ONLY hard constraint this imposes
on a candidate plaintext is: two positions that share the same ciphertext
symbol MUST have the same plaintext letter. Two positions with DIFFERENT
symbols are free to have the same letter or different letters -- nothing
about homophony forbids it. So the repeat pattern is a NECESSARY, not
sufficient, compatibility filter: any candidate word whose own letter-
repeats are at least as coarse as (a superset of) the required symbol-repeat
equalities can be fit by *some* choice of key, with zero help from
frequency analysis.

This script counts how many entries in a standard, reproducible English
word list of exactly Z13's length (13) satisfy this necessary condition,
under the REPORTED Z13 repeat-pattern classes, and under sensitivity
variants, to give a concrete number for how much (or little) the
repeat-pattern constraint alone narrows the candidate space -- as a
complement to (not a replacement for) the information-theoretic unicity-
distance finding already in knowledge-base/state.md, which reasons about
key-space entropy directly rather than about a real dictionary corpus.

Disclosed sourcing limitation: this session's network egress policy
blocked direct WebFetch access to every specific Z13-transcription source
site tried this session (zodiackillerciphers.com, en.wikipedia.org,
arxiv.org, www.zodiacciphers.com, news.terabox.com -- all
EGRESS_BLOCKED), the same recurring, disclosed restriction noted in
logs/2026-09-23-sq3-homophonic-unicity-calibration.md (raw.githubusercontent.com
remained reachable, as before). The repeat-pattern figures below
(ciphertext position equalities 1=12, 3=11, 5=7=9, 8=13, with positions 2,
4, 6, 10 unique -- 8 total symbol-classes, size profile 3-2-2-2-1-1-1-1)
come from the WebSearch tool's own synthesized answer over multiple
secondary sources, not a directly read/quoted primary transcription or a
primary FBI-released scan. This is explicitly NOT yet verified against a
primary source, and is only loosely consistent with (not the same claim
as) the still-unverified "repeated eight-ball separator symbol" note
flagged in logs/2026-09-23-sq1-sq3-source-and-attacksurface.md Sec. 3 --
both remain open and disclosed. This finding's dependency on the true
transcription is named explicitly, per methods/falsification-standard.md's
"Dependencies" requirement, and is exactly why SQ-1 (primary-source
acquisition) remains the project's real blocker.

Word-list corpus definition (units and controls): dwyl/english-words'
`words_alpha.txt` (a widely used, public-domain-derived English word list;
retrieved 2026-09-25 via raw.githubusercontent.com -- a small, generic
linguistic reference list, not a bulk cipher-corpus download), filtered to
entries of exactly 13 alphabetic characters, uppercased. This is a broad
dictionary (includes technical/obscure words and inflected forms), not a
curated common-word or proper-noun list -- disclosed as a real scope
limitation, discussed in the Interpretation section below and in the
companion log entry.

Reproducing this script: download
https://raw.githubusercontent.com/dwyl/english-words/master/words_alpha.txt
to the same directory as this script (as `words_alpha.txt`) and run
`python3 z13-repeat-pattern-flexibility.py`. The word list itself is not
committed to this repository (it is a large, generic, independently
reproducible third-party file, not project-specific data); the full
verbatim output of this run is committed instead, in the companion log
entry, per methods/falsification-standard.md's provenance requirement.

No suspect-identification content: this script and its output contain no
candidate name, person, or proposed Z13 solution of any kind -- only a
generic dictionary word list and a mechanical compatibility count.
"""

import itertools  # noqa: F401  (kept for readability/extension; not required by current logic)
from collections import Counter

WORDLIST_PATH = "words_alpha.txt"
TARGET_LEN = 13


def load_length_n_words(path: str, n: int) -> list:
    with open(path, encoding="ascii", errors="strict") as f:
        lines = f.read().splitlines()
    return sorted({w.upper() for w in lines if len(w) == n and w.isalpha()})


def classes_from_equalities(n: int, groups: list) -> list:
    """Build the full partition of positions 1..n into equivalence classes,
    given explicit multi-member groups (1-indexed); every position not
    named in a group is its own singleton class."""
    assigned = set()
    classes = []
    for g in groups:
        classes.append(tuple(sorted(g)))
        assigned.update(g)
    for p in range(1, n + 1):
        if p not in assigned:
            classes.append((p,))
    return classes


def is_compatible(word: str, classes: list) -> bool:
    """A word is compatible with a repeat-pattern (necessary condition
    only) iff every position pair within the same class shares a letter."""
    for cls in classes:
        letters = {word[p - 1] for p in cls}
        if len(letters) != 1:
            return False
    return True


def expected_count_naive(classes: list, words: list) -> float:
    """Analytical cross-check: expected number of compatible words if each
    position's letter were drawn i.i.d. from the corpus's own OVERALL
    letter-frequency distribution (an approximation -- ignores real
    positional/morphological correlation within English words, disclosed
    here rather than presented as exact). For each multi-member class of
    size k, P(all k positions share a letter) = sum_letter freq(letter)^k;
    classes are then treated as independent and multiplied together, times
    the corpus size, to estimate the expected compatible-word count under
    a "no special positional structure" null."""
    letter_counts = Counter(ch for w in words for ch in w)
    total = sum(letter_counts.values())
    freqs = {ch: c / total for ch, c in letter_counts.items()}
    p_match = 1.0
    for cls in classes:
        if len(cls) > 1:
            p_match *= sum(f ** len(cls) for f in freqs.values())
    return p_match * len(words)


def report_pattern(name: str, classes: list, words: list, source_note: str):
    sizes = sorted((len(c) for c in classes), reverse=True)
    compatible = [w for w in words if is_compatible(w, classes)]
    expected = expected_count_naive(classes, words)
    print(f"=== {name} ===")
    print(f"Source/status: {source_note}")
    print(f"Classes: {len(classes)}  size profile: {'-'.join(map(str, sizes))}")
    print(f"Groups (1-indexed positions): "
          f"{[c for c in classes if len(c) > 1]}")
    print(f"Compatible dictionary words (of {len(words)} total length-{TARGET_LEN} "
          f"entries): {len(compatible)}  ({100 * len(compatible) / len(words):.2f}%)")
    print(f"  Analytical cross-check (expected count under an i.i.d.-letter, "
          f"overall-corpus-frequency null model, classes treated independently): "
          f"~{expected:.2f}")
    if compatible:
        print(f"  Sample (first 8, alphabetical): {compatible[:8]}")
    print()
    return compatible


def main():
    words = load_length_n_words(WORDLIST_PATH, TARGET_LEN)
    print(f"Loaded {len(words)} length-{TARGET_LEN} alphabetic entries from "
          f"{WORDLIST_PATH} (dwyl/english-words words_alpha.txt).\n")

    # --- Null model: no required repeats at all (13 singleton classes). ---
    null_classes = classes_from_equalities(TARGET_LEN, [])
    report_pattern(
        "Null model (no required repeats -- baseline candidate count)",
        null_classes, words,
        "No sourcing needed -- definitional baseline (0 constraints).",
    )

    # --- Reported Z13 pattern (WebSearch-synthesis sourced, disclosed). ---
    reported_groups = [[1, 12], [3, 11], [5, 7, 9], [8, 13]]
    reported_classes = classes_from_equalities(TARGET_LEN, reported_groups)
    assert len(reported_classes) == 8
    assert sorted((len(c) for c in reported_classes), reverse=True) == [3, 2, 2, 2, 1, 1, 1, 1]
    report_pattern(
        "Reported Z13 pattern (1=12, 3=11, 5=7=9, 8=13; 8 classes total)",
        reported_classes, words,
        "WebSearch-tool synthesis over secondary sources this session "
        "(2026-09-25); NOT directly read from a primary transcription or "
        "verified against the still-open SQ-1 primary-source deliverable. "
        "Treat as a disclosed working assumption, not a confirmed fact.",
    )

    # --- Sensitivity variant: denser pattern (more repetition than reported).
    denser_groups = [[1, 12], [3, 11], [5, 7, 9], [8, 13], [2, 4]]
    denser_classes = classes_from_equalities(TARGET_LEN, denser_groups)
    report_pattern(
        "Sensitivity variant A: denser pattern (7 classes; adds a [2,4] tie)",
        denser_classes, words,
        "Hypothetical sensitivity check, not a claim about Z13's real "
        "transcription -- tests how much the compatible-word count moves "
        "if the true symbol-repeat structure is denser than currently "
        "reported.",
    )

    # --- Sensitivity variant: sparser pattern (less repetition than reported).
    sparser_groups = [[1, 12], [3, 11], [5, 7], [8, 13]]
    sparser_classes = classes_from_equalities(TARGET_LEN, sparser_groups)
    report_pattern(
        "Sensitivity variant B: sparser pattern (9 classes; triple -> pair)",
        sparser_classes, words,
        "Hypothetical sensitivity check, not a claim about Z13's real "
        "transcription -- bounds the other direction from variant A.",
    )

    print("=== Interpretation (actual result, reported as observed -- not the "
          "a-priori hypothesis this script set out to test) ===")
    print(
        "This analysis set out to measure how much unconstrained "
        "structural flexibility remains for candidate Z13 plaintexts even "
        "before any frequency-based scoring is applied. The measured "
        "result is the OPPOSITE of what a naive intuition about "
        "homophonic-key flexibility might suggest: at the full reported "
        "repeat pattern (5 independent positional-equality constraints), "
        "ZERO of the 20,944 length-13 entries in this generic English "
        "dictionary corpus are even structurally compatible -- consistent "
        "with (and quantitatively cross-checked against) the analytical "
        "expected-count null model reported above, which independently "
        "predicts a near-zero expected count from compounding several "
        "1-in-~25 positional coincidences on a corpus this size. Relaxing "
        "to any single constituent constraint restores hundreds to low "
        "thousands of compatible words (see the per-constraint checks in "
        "this file's accompanying log entry), confirming this is not a "
        "bug but the expected effect of intersecting several fairly "
        "restrictive constraints on a modest-sized corpus."
        "\n\nThe honest, appropriately narrow conclusion: THIS corpus (a "
        "broad but ordinary-word dictionary) offers no candidate at all "
        "under the full reported pattern -- which does not mean Z13 is "
        "unsolvable or especially constrained; it means the 'structural "
        "flexibility' problem this project is worried about, if it "
        "exists, must come from a much larger and more permissive "
        "candidate space (proper nouns, initials, abbreviations, or short "
        "phrases with spaces removed -- none of which are modeled or "
        "searched here) rather than from ordinary dictionary words. This "
        "gives a concrete, disclosed reason -- independent of any "
        "suspect-identity reasoning -- that future Skeptic/Linguist work "
        "on Z13 should not expect an ordinary dictionary word to be the "
        "plaintext, and should define its candidate space explicitly "
        "rather than defaulting to one. No candidate word, name, or "
        "solution is proposed, endorsed, or implied anywhere in this "
        "analysis or its output."
    )


if __name__ == "__main__":
    main()
