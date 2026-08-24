# Rethlas verification protocol for new mathematical results

This protocol applies to every mathematical statement first proved in this
book.  Imported results, definitions, explanatory reformulations, and direct
formal consequences that are explicitly identified as such remain subject to
the ordinary mathematical and source audits, but are not described as new
results.

No candidate may be promoted to `theorem`, `proposition`, `lemma`, or
`corollary` status until its verification record contains all of the following.

Result headings are numbered but unnamed by default.  A parenthetical name is
permitted only when the cited literature already uses that name for the result
(for example, the Fenchel--Moreau theorem).  Descriptive phrases invented for
this book belong in the prose immediately before the statement, not in the
theorem heading.  In particular, Rethlas verification never licenses the book
to coin a conventional name.

1. **Exact signature.**  State the ambient category, all separation,
   compactness, positivity, regularity, characteristic, dimension, and
   finiteness hypotheses, as well as every normalization.
2. **Natural-framework test.**  Decide which restrictions are essential and
   which can be removed.  Test at least the relevant singular/non-normal,
   positive- or mixed-characteristic, zero-volume or zero-mass,
   nonmetrizable/net, and nonprojective/Kähler boundaries.
3. **Independent proof.**  Give a complete proof independent of the prose
   proposed for the chapter.  Every imported input must have a primary-source
   anchor with its original hypotheses.
4. **Adversarial audit.**  A separate `gpt-5.6-sol` verifier at `xhigh`
   reasoning effort must search for circularity, reversed inequalities,
   missing compactness or measurability, illicit sequential arguments,
   undefined infinite arithmetic, and normalization or sign errors.
5. **Counterexample search.**  Test the statement on curves, toric or
   polyhedral models, reducible or non-unibranch spaces when meaningful, and
   the appropriate zero-dimensional or zero-volume boundary.  Record failed
   proof routes as well as actual counterexamples.
6. **Novelty separation.**  Search the current primary literature.  Distinguish
   a genuinely new theorem from a known theorem, a strengthened formulation,
   a conditional reduction, and a worked special case.  The book makes no
   priority claim without external confirmation.
7. **Rethlas receipt.**  Preserve the problem digest, proof digest, model and
   reasoning settings, verifier findings, repairs, final verdict, and date.
   The only promotable verdict is `VERIFIED`.
8. **Independent integration audit.**  After insertion, recheck the displayed
   theorem, proof, downstream uses, provenance ledger, research-question
   ledger, index, and cross-references against the verified receipt.

## Primary-source locator firewall

Rethlas is used here as a mathematical proof auditor.  Its verdict does not,
by itself, authenticate a theorem number, proposition number, page number,
edition, version, or other bibliographic locator.  Every load-bearing locator
must therefore be checked separately against the controlling primary-source
file and the edition or version actually cited by the book.  Search snippets,
secondary citations, a different edition, and model recollection do not settle
that check.

A primary-source inspection may show that a verifier's locator objection was
a false positive.  It may then clear the locator and justify a new
source-attested submission.  It cannot change the status of the earlier run:
a run on stale bytes, or a run whose final verdict is `wrong`, remains a
diagnostic artifact and never becomes a receipt by editorial reinterpretation.
Conversely, a mathematically favorable verdict cannot rescue a locator that
the controlling source disproves.

Promotion therefore requires all three of the following, simultaneously:

1. the submitted statement and proof are the exact current bytes used in the
   book, or are a source-aware composite whose live components are proved
   byte-identical to those current bytes;
2. every load-bearing bibliographic locator has primary-source clearance in
   the controlling edition or version; and
3. the production verifier returns a final `correct` verdict for that exact
   submission, with no critical error and no gap.

The 24 August 2026 Xia, Cao, and Schneider audits are controlling examples.
The Xia source locators were checked against the supplied book PDF before the
two exact-current Chapter 55 submissions.  Cao's relevant statement is
Proposition 4.4 on physical page 19 of the archived arXiv PDF, not a
nonexistent Proposition 4.3; the earlier contrary Rethlas run is retained only
as a diagnostic, and a fresh source-attested run supplies the receipt.
Schneider's second expanded edition places the John theorem at Theorem
10.12.2 and the Blaschke selection theorem at Theorem 1.8.7; locators from a
different edition were not allowed to control the live citation.

The remaining verdicts have fixed meanings:

- `CONDITIONAL`: the argument is correct only after adding an explicitly
  displayed hypothesis or importing an unresolved input;
- `DISPROVED`: a counterexample to the proposed statement has been verified;
- `OPEN`: neither proof nor counterexample survived verification;
- `RETRACTED`: an earlier internal candidate failed a later audit and must not
  be used downstream.

The research summary must report all five verdicts.  Failed candidates are
mathematical information, but they never appear in theorem typography.
