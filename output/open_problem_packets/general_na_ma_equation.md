# Extending the non-Archimedean Monge--Ampère equation

Map the exact frontier of existence and uniqueness for finite-energy
non-Archimedean Monge--Ampère equations beyond the original BFJ setting.
Include as a separate exact axis Pille--Schneider, arXiv:2209.04879v2,
Remark 4.4: \(\mathcal E^1(X,L)\) is definable over an arbitrary complete
non-Archimedean field, but extension of the Monge--Ampère operator to that
class is unclear in general.  The dedicated packet
ps23_arbitrary_field_e1_ma.md gives this question without bundling it with
the other axes.
Separate the following axes:

1. residue characteristic zero versus positive characteristic;
2. smooth versus normal, unibranch, or arbitrary projective varieties;
3. discrete versus general nontrivial valuations;
4. ample line bundles versus big and nef or arbitrary big classes;
5. measures supported on the skeleton/divisorial locus versus arbitrary
   finite-energy Radon measures;
6. algebraizable versus general analytic spaces.

First survey the precise primary theorems of BFJ, Boucksom--Jonsson,
Burgos Gil--Gubler--Jell--Künnemann--Martin,
Gubler--Jell--Künnemann--Martin, Fang--Gubler--Künnemann, and later work
available by 14 August 2026.  Keep their different signatures separate: the
2019 equal-characteristic result retains geometric-origin and resolution
hypotheses, while the 2025 mixed-characteristic result retains projective
resolution and embedded-resolution hypotheses. Then try to remove each
remaining hypothesis using envelopes, alterations, universal
homeomorphisms, capacity, and variational compactness.

Use the exact source boundary.  BFJ Theorem A assumes a complete discretely
valued field with residue characteristic zero, a smooth projective
algebraizable variety, an ample line bundle, and a measure of the correct
mass supported on one snc dual complex.  Gubler--Jell--Künnemann--Martin
Theorem 1.5 is an equal-characteristic positive result for spaces of
geometric origin from a \(d\)-dimensional family over a perfect field of
characteristic \(p>0\), and retains resolution and embedded resolution in
dimension \(d+n\); the stated unconditional case is a smooth projective
surface of geometric origin from a one-dimensional family.
Fang--Gubler--Künnemann Theorem 1.2, in the December 2025 version supplied in
the reference pack, treats the complete discretely valued mixed-characteristic
case under projective resolution and embedded-resolution hypotheses.  Each
of these theorems produces the continuous semipositive solution, unique up
to additive constant (equivalently, metric scaling), for a correctly
normalized skeleton-supported measure.  None of these cited statements by
itself treats arbitrary finite-energy measures, singular varieties, general
valuations, or nonalgebraizable analytic spaces.

Also record the dimension-one boundary separately: Gubler--Jell--Künnemann--
Martin Theorem 1.1 proves continuity of the semipositive envelope for an
ample line bundle on a smooth projective curve over any complete
non-Archimedean field, and the ensuing curve argument gives a continuous
solution for a correctly normalized measure supported on the skeleton of a
strictly semistable model.  This curve case is not subject to the
positive-characteristic resolution hypotheses of Theorem 1.5.

The three attached primary papers are the source base for the theorem
signatures just listed.  Any additional theorem attributed to the other works
named in the survey must be accompanied by, and checked against, its exact
primary statement; do not fill a missing signature from memory or from a
secondary survey.

Every proposed extension must prove:

- a well-defined full-mass finite-energy class;
- upper semicontinuity and compactness sufficient for the direct method;
- differentiability or a valid substitute;
- comparison and uniqueness;
- correct total-mass normalization and base-change behavior.

Do not bundle distinct unresolved axes into one theorem. If an existing
publication already closes an axis, classify it as known rather than new. If
a proof uses resolution or multiplier ideals, retain the characteristic
hypothesis.

Do not use skeletal regularity as an implicit compactness theorem.
Boucksom--Jonsson, *Non-Archimedean Green's functions and Zariski
decompositions* (2024), Theorems A--B, give two negative boundaries: a
divisorial Green function need not be rational PL/model, and a finite atomic
Monge--Ampère solution supported on a dual complex need not factor through
the retraction of any snc model.  These are resolved obstructions, not open
questions.
