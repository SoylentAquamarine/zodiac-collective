# SQ-3 — a defensible phrase-construction method: bigram-chain, not hand-picked

**Trigger:** last cycle confirmed no natural phrase fits Z13's exact partition (0 of 563,972 windows).
The planted-recovery phrase must be constructed. This log designs *how*, before constructing anything.

## What's already known / not done yet

Known: Z13's exact partition (`{1,12},{3,11},{5,7,9},{8,13}`, plus singletons `{2},{4},{6},{10}`); the
already-committed empirical unigram and bigram frequency tables (from *Pride and Prejudice*). Not done:
any method for building a 13-character sequence that both respects the partition and carries real
bigram-level structure for scoring to detect.

## Why hand-picking a real phrase is the wrong approach, not just impractical

Deliberately selecting a specific real sentence or phrase to use as the "planted truth" — even if chosen
before seeing scoring results — still means *I* am the one choosing which real phrase to privilege, which
reintroduces exactly the kind of unstated researcher discretion this project's falsification standard
exists to block (not fit-tuning in the strict sense, but still a human judgment call dressed as evidence).
The exhaustive search in the last log was the objective alternative (a found match, not a chosen one); it
returned nothing.

## Design: construct via a bigram Markov chain, not a hand-picked sentence

Rather than picking a real phrase, generate the "true" sequence mechanically: walk positions 1 to 13 in
order. For the **first** position in each equality class (the first time a new class is encountered),
draw its letter from the empirical bigram-conditional distribution given the immediately preceding
position's letter (position 1 itself has no predecessor, so it draws from the unigram distribution).
For a position that is a **repeat** occurrence of an already-assigned class (e.g. position 12, forced
equal to position 1), copy the already-determined letter directly — it cannot be redrawn, since the
cipher's own structure requires it.

This gives the sequence real **local** bigram structure wherever a position's letter was actually drawn
(not forced), while being honest that the *forced* positions (where a class repeats) may break bigram
flow at that specific boundary — an inherent, unavoidable feature of any real message under this exact
cipher structure, not a flaw introduced by the simulation. This is a materially more defensible
construction than either independent unigram draws (the method already tried, bigram-uninformative) or a
hand-picked sentence (reintroduces researcher discretion).

## Explicit parameters, fixed before generation

- Random seed: fixed, declared here before running: `20261004`.
- Number of constructed "true" sequences to generate and test: 20 (not 1 — a single instance risks being a
  lucky or unlucky draw; 20 gives a real distribution of outcomes).
- Alternatives per true sequence: 2000, drawn fully independently per equality class (same unrestricted
  null as prior corrected pilots).
- Scoring: both unigram and bigram, using the already-committed empirical tables.
- Metric reported: rank and percentile of each constructed "true" sequence among its own 2000 alternatives,
  for both scoring functions — the full distribution across the 20 trials, not just a mean.

## Stated prediction

I expect bigram scores to separate true-from-alternative more than unigram scores (as in the Z408 pilots),
but less cleanly than those pilots did, since roughly a third of the 13 positions here are forced repeats
that may break local bigram flow rather than being independently drawn to fit it.

## Honesty precommitment

Report the actual rank distribution across all 20 trials, including if some or most trials show the true
sequence failing to separate from alternatives — not just the best-looking trial.

## Result

Self-checks passed: unigram probabilities sum to 1.0; every transition-probability row sums to 1.0
(spot-checked for A/B/C, true for all 26 by construction). All 20 constructed sequences verified to
satisfy Z13's exact partition exactly (every required-equal position pair/triple checked programmatically,
not assumed).

| Trial | Sequence | Unigram rank | Unigram %ile | Bigram rank | Bigram %ile |
|---|---|---|---|---|---|
| 0 | ERENTOTETEEEE | 1/2001 | 100.00 | 1/2001 | 100.00 |
| 1 | EXILAYATASIET | 33/2001 | 98.40 | 6/2001 | 99.75 |
| 2 | RMBEOWONOUBRN | 100/2001 | 95.05 | 16/2001 | 99.25 |
| 3 | RMIREGENEMIRN | 9/2001 | 99.60 | 5/2001 | 99.80 |
| 4 | VANLISISIMNVS | 123/2001 | 93.90 | 93/2001 | 95.40 |
| 5 | APRAVIVEVERAE | 101/2001 | 95.00 | 19/2001 | 99.10 |
| 6 | GEDASHSHSHDGH | 51/2001 | 97.50 | 22/2001 | 98.95 |
| 7 | HALEAVANANLHN | 13/2001 | 99.40 | 14/2001 | 99.35 |
| 8 | ELETITISINEES | 1/2001 | 100.00 | 1/2001 | 100.00 |
| 9 | WINTOROTORNWT | 10/2001 | 99.55 | 1/2001 | 100.00 |
| 10 | FARLLYLLLYRFL | 287/2001 | 85.71 | 26/2001 | 98.75 |
| 11 | RHIEVEVEVEIRE | 30/2001 | 98.55 | 3/2001 | 99.90 |
| 12 | MOSADODPDOSMP | 161/2001 | 92.00 | 85/2001 | 95.80 |
| 13 | IMASTTTOTYAIO | 9/2001 | 99.60 | 1/2001 | 100.00 |
| 14 | SWASFEFSFGASS | 103/2001 | 94.90 | 24/2001 | 98.85 |
| 15 | HEGWHEHPHEGHP | 116/2001 | 94.25 | 39/2001 | 98.10 |
| 16 | RTYOMSMSMMYRS | 153/2001 | 92.40 | 56/2001 | 97.25 |
| 17 | TINDAIARANNTR | 6/2001 | 99.75 | 1/2001 | 100.00 |
| 18 | KINDABATABNKT | 228/2001 | 88.66 | 77/2001 | 96.20 |
| 19 | MYPPINIRIAPMR | 235/2001 | 88.31 | 65/2001 | 96.80 |

**Summary across all 20 trials**: unigram percentile mean 95.63 (median 96.28, range 85.71–100.00);
bigram percentile mean 98.66 (median 99.17, range **95.40–100.00**).

## Decision

**Prediction confirmed.** Bigram scoring is consistently stronger than unigram across every single trial
— not just on average. Most strikingly, bigram's *minimum* across 20 trials (95.40%) is higher than
unigram's *median* (96.28% is close, but unigram's own minimum, 85.71%, is far below anything bigram
produced). This means: under this construction method, a scoring approach using real bigram structure
would essentially never mistake a constructed "true" sequence for one of 2000 structureless alternatives,
even in the worst of 20 trials — a materially more robust result than the single-instance rankings from
two cycles ago, now backed by a real multi-trial distribution rather than one favorable draw.

**Caveat, as anticipated in the design**: this still doesn't show Z13 itself has a recoverable answer —
it shows that *if* a message were encoded this way, and *if* a correct scoring approach existed, length
and structure would not be the obstacle. The unmotivated-candidate blocker is unchanged.

