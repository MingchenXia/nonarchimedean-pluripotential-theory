# Audit: P12 reduced excellent curve links

Date: 11 September 2026

## Result

PASS.  The live manuscript now proves four sharply delimited results for
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
3. `prop:p126-curve-conductor-principal-realization` proves that every
   sufficiently deep integral vector of normalization-branch orders is cut
   out by one downstairs nonzerodivisor generating an m-primary principal
   ideal.
4. `thm:p122-curve-principal-ideal-envelope` identifies the resulting
   profiles with the strictly negative rational orthant, their uniform
   closure with the nonpositive real orthant, and the raw finite-link
   obstacle envelope with pointwise truncation by zero.

The reducible node, irreducible node, and cusp examples check support,
branch multiplicity, and the necessity of compatible ideal normalization.

## Hostile review

Independent GPT-6 Astra hostile review first passed the link and finite-map
packet, and then separately passed the proposed conductor and ideal-profile
extension.  The latter review checked the product normalization case,
existence and exact branch orders of a generator downstairs, regularity and
primaryness, both monotone approximation directions, the zero-coordinate
obstruction, and equality of the raw and closed-family envelopes.  Its
required explicit proof details and boundary wording were incorporated
before a final exact-live review of the integrated bytes, which returned
PASS with no mandatory correction.  That review was bound to SHA-256
`73eb8ce87542` for `CONDUCTOR_IDEALS.tex`, `c1b1aeb6431f` for the Chapter 70
integration, `2280affa9cd1` for Chapter 72, `8dc951f34e1b` for the inventory,
and `d4aaf135cf3b4` for Appendix L.

The retained scope firewalls are essential:

- branches are indexed by maximal ideals of the normalization above the
  closed point, not merely by minimal primes;
- finite-map restriction need not be surjective;
- decreasing primary-ideal approximation is asserted only for strictly
  negative profiles and starts only after the conductor threshold;
- the raw principal-ideal envelope is a supremum and need not be attained;
- the computed ideal-profile closure is not identified with an independently
  constructed singular psh or nef cone, and no intersection product,
  Monge--Ampere operator, energy, or higher-dimensional theorem is inferred.

Accordingly P12.1, P12.2, P12.3, and P12.6 are narrowed but remain active.

## Mechanical verification

- `git diff --check`: PASS.
- Open-problem inventory: PASS, 48 active atoms in 14 formal problem
  environments; tier totals T2=5, T3=9, T4=17, T5=17.
- Full `latexmk` build: PASS, 3644-page `book.pdf`.
- Final `book.log`: no undefined reference, undefined citation,
  multiply-defined-label, or rerun warning matched.

Primary-source claims and links are recorded in `SOURCES.md`; exact proof
packet hashes are recorded in `SHA256SUMS`.
