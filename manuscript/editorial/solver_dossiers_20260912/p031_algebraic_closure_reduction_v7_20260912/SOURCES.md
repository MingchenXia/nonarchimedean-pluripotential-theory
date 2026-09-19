# Source and dependency ledger

Date: 19 September 2026

## Gubler--Rabinoff

Walter Gubler and Joseph Rabinoff, *Classically psh and pluriharmonic
functions on Berkovich spaces*, arXiv:2506.13548v2.

- Section 2.9 states that analytic scalar projection is continuous,
  topologically closed, and surjective.
- Section 2.11(5) states the needed compatibility of relative interiors
  with analytic scalar extension.
- Proposition 4.2(5) states that a function is classically psh if and only
  if its pullback along an analytic scalar extension is classically psh.
- In the proof of Proposition 3.5(9), the authors explicitly invoke
  Berkovich Corollary 1.3.6 to say that scalar projection from the completion
  of an algebraic closure is open on a strict affinoid curve.

The repository-pinned v2 PDF has SHA-256
`83ca9a19394f44bb2e4e1aa316de95938f311acd53a00fe250fa0f605184b726`.

## Berkovich

Vladimir G. Berkovich, *Spectral Theory and Analytic Geometry over
Non-Archimedean Fields*, Mathematical Surveys and Monographs 33, American
Mathematical Society, 1990, Corollary 1.3.6.

The cited corollary gives the completed-algebraic-closure quotient theorem
from which openness follows.  The exact locator and quotient formulation
were corroborated by Mehmeti, Proposition 1.1.44, and by the proof of
Hrushovski--Loeser--Poonen, Theorem 8.1.  The proof uses the openness
consequence also stated explicitly in the pinned Gubler--Rabinoff source.

## Live dependencies

The only book-local inputs are
`lem:p031-open-pullback-usc` and
`thm:p031-affine-ground-field-perron`.  Both were integrated and validated
in the immediately preceding P03.1 affine Perron version.  No quarantined
v5 or v6 result is used.  No novelty or priority claim is made.
