# Audit: P12 reduced excellent curve links

Date: 11 September 2026

## Result

PASS.  The live manuscript now proves two link-level results for
one-dimensional reduced Nagata Noetherian local rings, hence for reduced
excellent local complex curve germs:

1. `thm:p121-reduced-nagata-curve-link` classifies the normalized link as
   the finite discrete set of maximal ideals of the normalization above the
   closed point.  An m-primary ideal fixes the scale on each branch, and
   changing that ideal obeys the stated exact cocycle.
2. `prop:p126-finite-reduced-curve-link` gives restriction under arbitrary
   finite local homomorphisms in this class.  On each branch the
   ramification index multiplies both the order and the extended-ideal
   denominator, so it cancels after normalization.

The reducible node, irreducible node, and cusp examples check support,
branch multiplicity, and the necessity of compatible ideal normalization.

## Hostile review

An independent GPT-6 Astra exact-live hostile review returned PASS with no
mandatory correction.  It specifically checked possible failures from
nonequidimensional components, noninjective finite maps, branch indexing,
DVR domination of real valuations, primary extension, ramification,
topology, and the three examples.  Three optional clarifications proposed
by the reviewer were incorporated; the reviewer then reconfirmed PASS on
the final proof bytes.

The retained scope firewalls are essential:

- branches are indexed by maximal ideals of the normalization above the
  closed point, not merely by minimal primes;
- finite-map restriction need not be surjective;
- no conductor descent, singular psh class, envelope, intersection product,
  Monge--Ampere, energy, or higher-dimensional theorem is inferred.

Accordingly P12.1 and P12.6 are narrowed but remain active.

## Mechanical verification

- `git diff --check`: PASS.
- Open-problem inventory: PASS, 48 active atoms in 14 formal problem
  environments; tier totals T2=5, T3=9, T4=17, T5=17.
- Full `latexmk` build: PASS, 3630-page `book.pdf`.
- Final `book.log`: no undefined reference, undefined citation,
  multiply-defined-label, or rerun warning matched.

Primary-source claims and links are recorded in `SOURCES.md`; exact proof
packet hashes are recorded in `SHA256SUMS`.
