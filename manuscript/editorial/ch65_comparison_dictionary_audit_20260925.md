# Chapter 65 comparison-dictionary audit, 25 September 2026

## Scope

This pass starts from commit
`4b7932fa1cc6d17c6a98203e4b3e550eefee15c1` and completes the concluding
comparison dictionary in Chapter 65. It does not change the Chapter 72
inventory and does not claim a new independent-agent or model-verifier
verdict.

The new three-column dictionary records the exact input, canonical output,
and reverse condition or information loss for six passages:

1. normal relatively ample test configurations to finitely generated
   rational filtrations and rational PL metrics;
2. arbitrary standing filtrations to Fubini--Study functions, closed maximal
   test curves, and weak geodesic rays;
3. finitely generated rational projective filtrations to the analytic-square
   equality and normalization-invariant closed rays;
4. filtrations to the probability spectral DH measure and the mass-$V$
   test-curve DH measure, including the terminal atom;
5. closed filtration test curves to Legendre rays and the exact
   energy/first-moment identity; and
6. smooth test-configuration rays to the BHJ functional slopes under their
   stated hypotheses.

The character translation and the norm/squared-norm factor-two conversion
are separated explicitly. The final row was tightened on a second
mathematical pass: outside the smooth test-configuration setting, Chapter 65
extends only the energy identity to bounded filtration rays; every other
functional requires a separate extension theorem.

## Strict boundaries

The old four-item warning list is replaced by six precise boundaries. A
general filtration need not reconstruct a finite-type test configuration;
the big-class maximal envelope is removed only on the strict interior; the
Bergman result is an upper-semicontinuous tail-envelope limit rather than
smooth convergence; the DXZ--BJ arrow is neither an arbitrary compact
Kahler nor an MP comparison; an order isomorphism of psh cones does not
identify their Monge--Ampere operators; and saturation or graded integral
closure preserves the asymptotic objects without preserving finite weights,
base ideals, Bergman potentials, or uniformity on the whole time half-line.

## Source and style audit

The source note now gives pinpoint locators for BHJ17, BJ22, BC11, RWN14,
DXZ23, BHJ19, and the BHJ19 erratum. In particular, BJ22 Theorem 4.22 and
Corollary 4.23 are named for divisorial determination and extension to all
semivaluations. No quarantined BHJ19 Section 5 result is used.

The chapter's remaining inline `\\(...\\)` delimiters were normalized to the
book's dollar-delimiter convention, the optional non-historical remark title
was removed in favor of a semantic label, and the projective-line section
heading now uses a valid `\\texorpdfstring` math branch. The scoped Mingchen
audit reports zero errors and four reviewed convention warnings: the
established `chap:`, two `warn:`, and one `tab:` semantic label prefixes are
not in the audit script's narrower allowlist.

## Release gates

- `editorial/tools/refcheck.py`: 397 inputs, zero missing inputs, 11,831
  labels, zero duplicates, zero dangling references, and clean per-file
  structure.
- `editorial/tools/check_open_problem_inventory.py`: pass, with 42 active
  atoms in 12 Chapter 72 environments and tier totals `(0,3,7,15,17)`.
- `git diff --check`: clean.
- Full `latexmk` build: success, 4,068 pages and 19,372,336 bytes.
- Log audit: no unresolved reference or citation, multiply-defined label,
  rerun request, missing input, or horizontal or vertical overfull box.
- Rendered inspection: physical PDF pages 3,539--3,542 (printed pages
  3,471--3,474) were checked. The dictionary begins on printed page 3,471,
  the table fits without clipping on page 3,472, Section 65.13 begins only
  after the table on page 3,473, and the source note continues cleanly on
  page 3,474.

This is a mathematical, source, and presentation audit of the existing
Chapter 65 comparison chain. It retires no open-problem atom and creates no
new verifier or independent-agent claim.
