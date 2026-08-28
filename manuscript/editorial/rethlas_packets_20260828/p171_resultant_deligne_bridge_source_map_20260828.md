# P17.1 relative-resultant and metric bridge: source map

Date: 28 August 2026

Status: editorial source map only.  It contains no new theorem and authorizes
no live integration.  Every proposed bridge below requires an exact statement,
proof, and production Rethlas verification before use in the monograph.

## Objective

Pille--Schneider Question 4.9 asks for continuity of fibrewise mixed
Monge--Ampere measures in a Banach-family setting.  The first attempted global
candidate was rejected and remains excluded.  The independently verified
weighted Philippon--Gauss lemma supplies one analytic input only.  The remaining
route must separate three logically different constructions:

1. an algebraic relative mixed-resultant line and section;
2. a fibrewise identification with the classical resultant of the fundamental
   cycle;
3. an isometry between the resultant metric and the relevant mixed
   Chow/Deligne metric.

No one of these steps may be silently substituted for another.

## Ducrot: the algebraic line and section

The primary-source audit located the following anchors.

- The introduction of Ducrot's preprint, paragraph 0.6, explicitly permits an
  arbitrary projective relative scheme of relative dimension `n`; purity and
  reducedness are not imposed.
- The published Theorem 4.2 corresponds to the preprint's Main Theorem 5.3.
- Proposition 6.1.1 and Lemmas 6.3.1--6.3.6 construct the `q=1` line-valued
  resultant, prove its base-change behaviour, extend across the relevant depth
  locus, and identify its codimension-one incidence divisor.

These results support a relative resultant line and section in their stated
scope.  They do **not** say that the section vanishes whenever arbitrary
sections have any common zero.

### Codimension-one firewall

Take

`X = P^1 x P^1`, `n = 2`,

and take all three linear systems from `pr_1^* O(1)`.  The common-zero locus in
the coefficient space is the small diagonal of codimension two, while the
resultant section is a unit.  Thus a correct statement must retain Ducrot's
depth-at-most-one formulation, or the equivalent essentiality criterion in
the D'Andrea--Krick--Sombra cycle language.  A blanket common-zero vanishing
claim is false.

### Proposed extension that is still new

The desired family theorem uses arbitrary finite locally free basepoint-free
systems, not only complete sufficiently positive systems.  The source audit
suggests replacing each complete space of sections by the given bundle
`E_{i,s}`.  At each associated point the bad coefficients form a proper linear
subspace; the rank-at-least-two depth argument should then be unchanged, while
rank one gives a canonical unit.  This is a plausible proof plan, not yet a
theorem.

For extension from Noetherian approximations to an arbitrary base, the source
map records Stacks Project tags `01ZM`, `01ZR`, `0B8W`, `05LY`, `0D4R`, `0B91`,
and `05IN` as the likely approximation, descent, and common-refinement inputs.
Their exact hypotheses must be checked against the final packet.

## Fibrewise comparison with the cycle resultant

The expected fibre statement identifies Ducrot's section with the
D'Andrea--Krick--Sombra multiprojective resultant of

`phi_* [X_s]_n`,

including generic lengths on nonreduced components.  This comparison is not
supplied automatically by the existence of either construction.  It needs a
separate proof, with normalization fixed by the rank-one/unit case and with
essentiality treated componentwise.  Until that proof is verified, the two
resultants must not be declared equal.

## Chen--Moriwaki: fixed-field metric comparison

The primary-source audit records the following usable scope.

- Section 3.9, Theorem 3.9.7 gives the fixed-field mixed Chow/Deligne isometry
  for closed immersions and allows arbitrary ultrametric norms; no strictness
  or value-group restriction is needed there.
- Definition 1.6.4 treats a general projective scheme through its
  top-dimensional fundamental cycle with generic lengths.
- Proposition 3.6.2 gives the corresponding componentwise linearity of local
  heights.
- For a diagonal norm with logarithmic weights, the epsilon tensor and
  symmetric norms reduce exactly to the weighted maximum coefficient norm.

The closed-immersion hypothesis is a genuine gap for the intended
basepoint-free quotient systems.  Passing to a graph or Segre embedding does
not by itself preserve the required comparison.  The minimal new statement
should replace the closed immersion by a basepoint-free quotient and repeat
the incidence/projective-bundle calculation.  This statement requires its own
Rethlas packet.

Two further scalar-field steps remain separate:

1. at a trivially valued fibre, extend to the completion of the relevant
   function field and then prove descent of the isometry;
2. on an Archimedean fibre with a powered absolute value, prove the precise
   scaling formula rather than importing the ordinary-norm statement without
   adjustment.

Boucksom--Eriksson Proposition 8.3(iv), Theorem 8.16, and Appendix A.22 are
candidate uniqueness/base-change inputs for the first step.  Their exact use
has not yet been verified.

## Verification order

The next production packets should be deliberately modular.

1. Relative `q=1` resultant for finite locally free basepoint-free systems,
   retaining the codimension-one/essentiality hypothesis.
2. Fibrewise equality with the D'Andrea--Krick--Sombra resultant of the
   top-dimensional fundamental cycle.
3. Chen--Moriwaki comparison for a basepoint-free quotient, first over one
   complete non-Archimedean field.
4. Trivial-valuation base change and descent.
5. Archimedean powered-norm scaling.
6. Only then assemble the Banach-family continuity argument and test whether
   it reaches the full literal scope of Question 4.9.

Failure of any packet leaves P17.1 open and must be recorded rather than
replaced by a stronger unproved assertion.
