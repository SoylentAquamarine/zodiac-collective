# PR #10 revised paragraph review (2026-10-27)

Precommitment: read-only check. Compare each factual claim in PR #10's added paragraph (head 847fa6a) against committed repo logs; no code run, no fetches. Honesty: report any mismatch, including wording that overstates.

Result:
- "matched just 42 of 408 known letters" -> logs/2026-10-21-sq2-z408-v4-unigram-penalty-execution.md line 6: 10.29% (42/408). Matches.
- "Claude independently reproduced all 16 reported scores" -> logs/2026-10-26-sq2-pr11-second-corpus-reproduction-execution.md. Matches.
- "wrong output ranks above the real message at every tested order" -> orders 1-4, both corpus preparations. Matches.
- Caveat: "latest output" = v4, which is the lowest-accuracy of v1-v4 (v3 30.64% was best); wording is accurate but a reader could infer the solver family is that bad. Optional clarification only.
- No suspect content; the paragraph says it is a method check, not a Z13 reading.

Disposition: accurate; PR left unmerged for the user's decision.
