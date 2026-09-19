# Live primary-source ledger

Date: 19 September 2026

## Gubler--Jell--Rabinoff

Walter Gubler, Philipp Jell, and Joseph Rabinoff, *Forms on Berkovich
spaces based on harmonic tropicalizations*, Bulletin de la Société
Mathématique de France 154 (2026), no. 1.

- Official PDF:
  `https://smf.emath.fr/system/files/filepdf/GUBLER_JELL_RABINOFF.pdf`
- Pinned SHA-256:
  `acf1c49e853f5f126e02d694eacd4bea0cf018ab5d396830aa09d17b72d2884c`
- Book key: `GJR26`.

Claims checked against the PDF:

- Section 5.2(7): finite minima and maxima preserve Z-PL and Q-PL functions.
- Example 5.3: over a field with additive value group Q, the real-PL function
  `pi log|t| + 1` has a maximum with zero whose tropical bend is at the
  irrational point `1/pi`, so that maximum is not real PL.
- Proposition 5.11: for a finite flat surjection of good strict analytic
  spaces and a divisible coefficient group, a function on the base is PL if
  and only if its pullback is PL.
- Proposition 7.6(1'): semipositivity pulls back, and reflects through a
  proper surjection.
- Definition 7.8 and Section 7.9: LFS functions are semipositive real-PL
  functions with a local finite-unit description; the proof of Proposition
  7.10 explicitly uses stability of LFS functions under maximum.

## Gubler--Rabinoff

Walter Gubler and Joseph Rabinoff, *Classically psh and pluriharmonic
functions on Berkovich spaces*, arXiv:2506.13548v2.

- Versioned PDF: `https://arxiv.org/pdf/2506.13548v2`
- Pinned SHA-256:
  `83ca9a19394f44bb2e4e1aa316de95938f311acd53a00fe250fa0f605184b726`
- Book key: `GR25Classical`.

Claims checked against the PDF:

- Proposition 4.2(2),(3): logarithms of analytic functions are classically
  psh; the class is a nonnegative cone and is stable under maximum.
- Theorem 4.3: over a nontrivially valued field, a real-PL function on a good
  strict analytic space is semipositive if and only if it is classically psh.

## Claim separation

The published GJR source supplies PL descent, semipositivity functoriality,
the LFS local calculus, and the real-slope counterexample.  The arXiv v2
source is used only for classical-psh closure and the semipositive/classical-
psh equivalence.  Neither source is cited for an LFS descent theorem, a scalar
orbit presentation, or envelope regularity.
