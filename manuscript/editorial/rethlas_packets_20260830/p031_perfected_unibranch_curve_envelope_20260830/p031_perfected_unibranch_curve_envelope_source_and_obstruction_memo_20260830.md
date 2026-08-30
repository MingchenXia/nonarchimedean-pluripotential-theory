# P03.1 perfected-unibranch curve envelope: source and obstruction memo

Date: 30 August 2026

Status: **quarantined research candidate; not independently audited; not
submitted to Rethlas; not integrated into the live book; P03.1 remains
active**.

## Exact target and frozen book inputs

P03.1 asks for hypotheses under which upper-semicontinuous regularization
of every local Fubini--Study/semipositive-real-PL obstacle envelope is
classically psh.  The live atom is broader than curves and broader than
perfect fields.

| input | SHA-256 |
|---|---|
| manuscript/parts/part2/ch15_poincare_lelong.tex | ca439119d083b03a5feb5b8fce285daab512b58dbfaab20c460c5be7795b6566 |
| manuscript/parts/part4/ch37_envelope_statement.tex | 0caf68cdcaffb1741385617371cf90ba26a098786551335ed9d17880a8b35a4e |
| manuscript/parts/part4/ch45_envelope_consequences.tex | 882b390955a9cfb1b6d85dd18931d88ef1cda1153d9e8cf40fc6a7b127f125cd |
| manuscript/parts/part6/ch72_major_open_problems.tex | 8bcc3f7c54ce2568c395448e95ae29266f2f24a57e6ee2feafd9e986192d30e0 |
| manuscript/editorial/open_problem_atomic_inventory_20260824.md | ead74f25b7dd7e2e41915ea3361daba43c93f421dcf00d3ee99d4a8d81fbdd1e |
| output/open_problem_packets/local_fs_envelope.md | 26702c2f512e7029f7b19271517682060b5c8fbe1d8bb1160cd344895b1a5275 |

The nodal counterexample in Chapter 15 is not contradicted: its
normalization has two points over the node, so the central bijectivity
hypothesis of the candidate fails.

## Candidate obtained

The packet proves a stronger family statement in dimension one.

1. On any separated rig-smooth strict analytic curve, the usc
   regularization of the supremum of an arbitrary locally-upper-bounded
   family of classically psh functions is classically psh.
2. For an arbitrary complete nontrivially valued field, perfect the field
   in positive characteristic, reduce the base-changed curve, and normalize.
   If this canonical normalization is bijective on Berkovich points, the
   same conclusion descends to the original curve.
3. Therefore the local FS/semipositive-real-PL obstacle envelope is
   classically psh on this class of curves for every usc obstacle, including
   at relative-boundary points.
4. Over a perfect field this includes every normal strict analytic curve
   and every reduced analytically unibranch strict analytic curve in the
   explicit sense that its normalization has one point over every point.

The proof is Perron comparison rather than a Choquet or sequential
argument.  Given a harmonic majorant on the finite boundary of a strict
affinoid subdomain, every competitor lies below it by Thuillier's defining
comparison property.  Their raw supremum therefore lies below it; usc
regularization preserves the inequality at interior points because the
majorant is continuous.  Gubler--Rabinoff's boundary-extension theorem
retains the relative boundary.  Homeomorphism of the perfecting,
reduction, and unibranch-normalization maps then makes usc regularization
commute with pullback, while scalar-extension equivalence and
finite-surjective descent bring classical psh-ness back down.

Exact candidate files:

- p031_perfected_unibranch_curve_envelope_statement_20260830.tex;
- p031_perfected_unibranch_curve_envelope_proof_20260830.tex;
- p031_perfected_unibranch_curve_envelope_compile_20260830.tex;
- p031_perfected_unibranch_curve_envelope_compile_20260830.pdf.

No theorem, lemma, or corollary has been given an optional conventional
name.

## Primary-source ledger

Frozen source:

- Walter Gubler and Joseph Rabinoff, *Classically psh and pluriharmonic
  functions on Berkovich spaces*, arXiv:2506.13548v2, 17 September 2025;
- local packet copy:
  sources/Gubler_Rabinoff_2506.13548v2.pdf;
- SHA-256:
  83ca9a19394f44bb2e4e1aa316de95938f311acd53a00fe250fa0f605184b726.

Exact source inputs:

- Sections 3.3--3.4.1: Thuillier comparison and its agreement with the new
  subharmonicity on smooth strict curves;
- Proposition 3.5(3): extension from the relative interior to the boundary;
- Proposition 3.5(8): finite-surjective descent on curves;
- Lemma 3.7: completed-perfect-closure scalar extension is a
  boundary-preserving homeomorphism;
- Lemma 3.8: reduction is a boundary-preserving homeomorphism;
- Lemma 3.9(1),(4): the normalization over a perfect field is rig-smooth
  and is a topological quotient;
- Section 4.1.2: classical psh equals subharmonic on analytic curves;
- Proposition 4.2(1)--(3),(5),(6): sheaf/log/max calculus, scalar extension,
  pullback, and finite-surjective descent;
- Theorem 4.3: semipositive real PL equals classically psh;
- Section 2.11(3),(4): on an analytic domain of a boundaryless separated
  curve, the complement of the absolute relative boundary is the
  topological interior.

The proof does not use Theorem 6.5.  That theorem requires the pointwise
limit itself to be usc and therefore does not by itself justify replacing a
raw supremum by its usc regularization.

## Firewall from the global trivially valued theorem

The supplied unibranch envelope theorem in Chapters 37--45 concerns
Boucksom--Jonsson psh functions on the whole analytification of an integral
projective variety over an algebraically closed **trivially valued** field.
Its hard input is the global envelope property on the normalization, and
its descent uses projective psh reflection through a finite universal
homeomorphism.

None of those assertions supplies the candidate above:

- the current competitors are local FS or semipositive real-PL functions
  over a generally nontrivially valued field;
- the analytic domain can have relative boundary and need not be proper or
  algebraizable;
- local FS/PL reflection through an arbitrary finite normalization is not a
  consequence of BJ reflection;
- the present proof instead uses one-dimensional harmonic comparison and
  the independently sourced Gubler--Rabinoff scalar/finite descent
  statements.

Thus the global projective theorem is used only as motivation and as a
scope firewall, never as a proof input.

## Why this does not yet retire P03.1

Let \(\mathcal F\) be a locally upper-bounded family of classically psh
functions on a higher-dimensional analytic space \(X\), put
\(s=\sup_{\phi\in\mathcal F}\phi\), and let \(u=s^*\).  For a curve test
\(\gamma:C\to X_{K'}\), one always has
\[
 \left(\sup_{\phi\in\mathcal F}\phi\circ\pi\circ\gamma\right)^*
 \leq
 u\circ\pi\circ\gamma .
\]
The inequality can be strict because neighborhoods inside the curve are
not cofinal among neighborhoods in \(X\).  Equality would make the
right-hand side subharmonic by the rig-smooth curve lemma, but normality or
unibranchness of \(X\) does not presently provide that equality.  In
dimension at least two a nonconstant analytic curve is normally not open,
so the homeomorphism argument used for curve normalization has no analogue.

A complete higher-dimensional proof therefore still needs one of:

1. a transversal barrier theorem forcing usc regularization to commute
   with every scalar-extended analytic-curve pullback;
2. a local model-envelope theorem plus gluing that proves the same
   statement without assuming it;
3. a capacity/removability theorem showing that the possible strict
   inequality is harmless for subharmonic pullback.

No such result was found in the frozen primary sources or in the supplied
global integration.  No normal or unibranch higher-dimensional
counterexample was found in this pass.  Mere normality over an imperfect
field is also not promoted: the candidate uses the explicit bijectivity of
the normalization after completed perfecting and reduction.

P03.1 must therefore remain one active atom even if this curve candidate
passes independent and production verification.  P03.2 (CLD-v2 psh) and
P03.3 (continuity for continuous obstacles) are not claimed.

## Adversarial checks

- The obstacle takes no \(+\infty\) value, so upper semicontinuity makes it
  locally bounded above; this really bounds the whole competitor family.
- The empty competitor family is treated separately and gives
  \(-\infty\).
- No sequence is extracted from an uncountable family.
- No closure of real-PL functions under a coefficient-sensitive maximum is
  used.
- Relative-boundary points are not discarded.
- Scalar extension, reduction, normalization, and descent are separate
  steps; no direct descent through the infinite perfect-closure extension
  is asserted.
- The candidate concludes only classical psh-ness, not CLD-v2 psh-ness or
  continuity.
- The nodal example fails the exact normalization-bijectivity hypothesis.

## Skill-scope audit

The envelope-unique-continuation-firewall skill was inspected because of
the word “envelope.”  Its input contract requires a holomorphic section
vanishing in an exterior region and propagation around a compact obstacle
and singular tube.  P03.1 has no such section, zero set, exterior vanishing
region, or identity-theorem step.  The skill is therefore a **non-trigger**
for the proof.  Its general warning about confusing distinct envelope
operations was retained in the BJ/local firewall above; none of its
holomorphic-zero mechanism was imported.

## Required next gate

Before any live integration:

1. perform an independent exact-byte mathematical audit, especially of the
   rig-smooth/relative-boundary passage and the reduction descent;
2. freeze statement and proof hashes;
3. submit those exact bytes, with the source PDF and this dependency ledger,
   to production Rethlas using gpt-5.6-sol at xhigh;
4. integrate only if the verdict is final/correct with zero critical errors
   and zero gaps.
