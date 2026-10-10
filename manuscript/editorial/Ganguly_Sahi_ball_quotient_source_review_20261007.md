# Finite ball quotients and singular Stein spaces: exact-source review

Date: 7 October 2026. Baseline and explicitly fetched `origin/work`:
`1d2fa1186eb729cdd533e05818f4143509b9670f`; fetched `origin/main`:
`00957114db21b627e97369563032ceda9cea09c7`.

Ganguly--Sahi arXiv:2607.14621v1 removes the abelian and dimension-two
restrictions from the non-Einstein theorem for nontrivial finite sphere-free
ball quotients. Its singular Stein consequence retains isolated normal
singularities, a compact smooth strongly pseudoconvex boundary and an
algebraic CR realization. The general singular Cheng--Huang--Xiao conjecture
without the algebraic CR hypothesis remains a separate problem.

The complete eleven-page controlling paper was read as complete text with
matching images in six individually displayed sheets. Thirty-three further
exact-source/page pairs were read in eighteen displayed sheets. The total
is **44 source/page pairs on 24 sheets**, all fresh, across five PDFs:
one complete main reading and four partial dependency readings. This is
an attributed source/convention audit with elementary exact diagnostics,
not an independent model receipt or complete external proof-chain certificate.

The source-only checkpoint preserves the checked 4,476-page book, both
bibliographies, index, canonical inventory and native catalogue/editor.
An attributed Appendix H continuation and provenance note can follow after
its own compilation and matching-page review.

## Controlling files and selection scopes

| Primary source | Actual pages read | PDF SHA-256 |
| --- | --- | --- |
| Ganguly--Sahi 2607.14621v1, submitted 16 July 2026, 06:37:15 UTC | 1--11, complete | `7f5bbbe23c8a554f0853cdf85bf839b71dfe1b4872cd50432617e03ab04c994d` |
| Ebenfelt--Xiao--Xu, OUP 2021 advance publication, numbered 1--31, DOI 10.1093/imrn/rnab120, NSF public repository copy | 1--12 of 31 | `76dd41f516837ef1fba45c85a5c257472ac93290412fd6e4982df4e34ac10de4` |
| Huang--Li, official Rutgers to-appear author copy, 23 pages | 1--4 and 13--20; twelve pages | `7193e74420bd2056eb254f332143715c534e0d5dab74be1fbe0c09788395cc4d` |
| Ganguly--Sinha 2210.12323v3, revised 11 September 2024, 23:43:36 UTC | 1--4 of 17 | `e898cbc68d2b04e0dcaafe838d49da7318371c18798ced66ef0958f3c0b918f1` |
| Huang, *Isolated Complex Singularities and Their CR Links*, official Rutgers author copy, 13 pages | 1--5 of 13 | `8d2091c33ca08b0b8b7d22ea96993892f6fb1693c3cf47e2ba69862223126028` |

EXX's controlling file is the advance layout downloaded 3 July 2021.
The later IMRN 2022(19), 15240--15270 citation is bibliographically related,
but its printed page locators are not transferred to this file. Huang--Li's
author copy has 23 pages, distinct from CAG 31(7), 1669--1692. The attempted
old publisher URL redirects to the journal homepage and does not authenticate
an article PDF. The arXiv metadata independently records the related journal
edition. Ganguly--Sinha's exact v3 is distinct from the 2026 Michigan layout
cited by the main paper; only v3 locators control the present selection.
Huang's author copy is distinct from the ten-page 2006 journal layout.

Acquisition layout texts are preserved unchanged. Images control conjugation
marks on group determinants, transpose matrices and second variables; several
such bars are lost in the layout extraction. That loss is not a source error.
The queued main acquisition preceded this audit and was only acquisition;
its full reading is recorded here. No successful frozen record is overwritten.

## Scoped source records

**GS01 — The singular Stein theorem.** Main Theorem 1.2, actual page 2,
requires dimension N at least two, normality, isolated singularities, compact
smooth strongly pseudoconvex boundary and CR equivalence to an algebraic CR
manifold in a complex Euclidean space. Its ball characterization is not
asserted for arbitrary smooth or real-analytic CR boundaries.

**GS02 — The group action.** Theorem 1.3 and the definition on main page 2
use a finite unitary subgroup whose nonidentity elements have no eigenvalue
one. The action is free on the sphere and punctured ball; every group element
fixes the origin. In dimension at least two, a nontrivial such quotient has
an isolated origin singularity. It is not an everywhere free quotient.

**GS03 — Intrinsic Bergman space.** EXX Section 2.1, actual pages 4--5,
and Huang--Li pages 2--4 use L2 holomorphic top forms on the regular locus.
For the group projection, coefficient functions satisfy
f(gamma z) det(gamma)=f(z). Untwisted invariant scalar functions give a
different space. Fixed volume-normalization constants do not change the metric.

**GS04 — Covering transformation and averaging.** EXX Theorem 2.3,
actual page 6, assumes a regular finite m-sheeted holomorphic covering with
deck group of size m, outside specified analytic subsets. Its formula is a
sum of pulled-back kernel forms. Huang--Li Lemma 5.1, pages 15--16, instead
has the averaged projection kernel. The quotient pullback differs from that
average by |Gamma|. This distinction matters for a determinant identity's
constant, even though multiplying a potential coefficient by a positive
constant leaves its logarithmic metric unchanged.

**GS05 — Conjugate group.** Main Proposition 2.1, pages 3--4, defines
the conjugate group explicitly. The canonical pullback in EXX (4.1) and
the second-variable Jacobian introduce conjugated determinants/matrices.
After complexification, the main potential is phi_Gamma=sum det(gamma)
(1-z^T gamma w)^(-N-1), and the quotient criterion uses the conjugate group.
Replacing Gamma by its conjugate preserves all group hypotheses.

**GS06 — The Einstein constant.** EXX Lemma 4.2 and its proof, pages
11--12, extend the pluriharmonic factor over the puncture by Hartogs, use
the identity summand's uniform boundary asymptotics and apply maximum modulus
to a nowhere-zero holomorphic exponential and its reciprocal. This forces
the source Einstein constant -1 and determinant factor (N+1)^N. This is a
ball-quotient argument, not a statement about every Kähler--Einstein metric.

**GS07 — Bordered determinant.** Main (2.1)--(2.3), pages 3--4, use
the (N+1)-by-(N+1) bordered matrix M(phi). Its determinant divided by
phi^(N+1) is det(partial-barpartial log phi). The necessary rational identity
is F=det M(phi)-(N+1)^N phi^(N+2)=0. This kernel determinant differs from
the positive-defining-function Fefferman determinant convention used earlier
in Appendix H; its sign is not silently transferred.

**GS08 — Complexification.** Main Theorem 2.2 implies Theorem 1.3 on
page 4 because the anti-diagonal (z,bar z) is maximally totally real.
A rational identity vanishing there on an open set vanishes identically.
The polar divisors and selected complex points need not lie on a physical
diagonal inside the ball. A complex pole can contradict the required rational
identity without producing a singularity of the physical interior kernel.

**GS09 — Identity-summand inverse.** Main Lemma 3.1 and its proof,
pages 4--5, use E=I+h^(-1)wz^T, E^(-1)=I-wz^T and det E=h^(-1).
The inverse is (N+2)h^(N+1)A0-h^(N+2)A with the displayed orientation.
Independent-variable and complex rational fixtures check the inverse and
determinant; neither a transposed inverse nor a real-only fixture controls it.

**GS10 — A nonempty restriction set.** Main Lemma 3.2, page 5, proves
h=1-z^T w irreducible by Gauss's lemma. Each nonidentity divisor cuts a
proper closed subset of the identity divisor; finitely many such subsets
cannot cover that irreducible variety. H_Gamma is the complement of those
other divisors, not an intersection where every group summand has a pole.

**GS11 — First valuation.** Main Proposition 3.3, pages 5--6, cancels
the determinant and binomial linear terms. It gives
h^(N(N+2))F/(N+1)^N=-G_Gamma+h^N(R-S), with R,S regular on H_Gamma.
The exponent N(N+2), the minus sign and the remaining positive power of h
are retained. It is enough to show the restriction of G_Gamma is nonzero.

**GS12 — The unitary affine-combination argument.** Main Lemma 4.2,
page 7, sets S=I-eta, invertible by the sphere-free assumption. If
S^(-1)(I-delta) were scalar, delta=(1-mu)I+mu eta. Distinct eigenvalues
of the nonscalar unitary eta, together with one, would lie on two circles.
The circles must coincide, forcing mu=1. This uses unitarity and the missing
eigenvalue one; it is not an arbitrary finite-linear-group argument.

**GS13 — The selected pair and curve.** Main Lemmas 4.1--4.2,
pages 6--7, choose a row outside finitely many eigenvector subspaces and a
vector in its kernel outside finitely many smaller kernels. Dimension
N-1 at least one is essential. The resulting point lies on precisely
H_I and H_eta; the curve w+epsilon u stays on H_I and avoids all other
divisors for sufficiently small nonzero epsilon.

**GS14 — Second valuation.** Main Proposition 4.3, pages 7--8, obtains
the coefficient det(eta)(N+2)(1-z^T eta^2 w) for a pole of order N+3.
A nonscalar sphere-free unitary eta cannot have eta^2=I, because such an
involution would be -I. Thus eta^2 is neither I nor eta and the coefficient
is nonzero by the selected-point construction. A nonabelian Q8 fixture
isolates the pair and gives coefficient eight; finite fixtures are not
a substitute for the general proof.

**GS15 — Scalar cyclic group.** Appendix A, page 9, identifies a
nontrivial finite scalar group with all ell-th roots of unity. The determinant
weight is lambda^N. The potential is a one-variable rational f(s), s=z^T w.
Replacing the weight by one changes the root-of-unity filter and the proof.

**GS16 — A zero away from the poles.** Appendix A, pages 9--10,
writes f=P/(1-s^ell)^(N+1). Individual summands have genuine poles, so
P does not vanish at those denominator roots. The first nonzero infinity
root sum gives degree P=N(ell-1); the origin order is at most ell-1.
N at least two forces a nonzero root b away from the poles. This is
the dimension restriction in the scalar argument.

**GS17 — The scalar pole.** Main Lemma A.1 and Proposition A.2,
pages 9--10, give det M(f)=(f')^(N-1)[ff'+s(ff''-(f')^2)]. If f has
order r at b, F/f^(N+2) has a pole of order N+r+1 and nonzero coefficient
-b r^N/u(b). No simple-zero assumption is imposed. Exact ell=2 fixtures
in dimensions two and three check both the numerator roots and coefficients.

**GS18 — Dimension one.** Main page 2 and Huang--Li Proposition 5.6,
page 20, retain the disk exception. A finite centered disk quotient is
smooth; its branched pullback can degenerate at zero without a quotient
singularity. The scalar dimension-one rational F vanishes identically,
and degree P equals the possible origin order. Neither the higher-dimensional
singularity statement nor the scalar zero argument extends to this case.

**GS19 — Earlier results and current scope.** EXX Theorem 1.4,
actual page 3, is the abelian theorem in arbitrary dimension at least two.
Ganguly--Sinha v3 Theorems 1--2, pages 1--2, allow nonabelian groups in
dimension two. The current main paper removes both restrictions without
using the finite sphere-free group classification. This is source-scoped
comparison, not an exhaustive intervening-literature or priority audit.
The earlier classification/combinatorial proofs are not read completely here.

**GS20 — Global Stein reduction.** Huang--Li Theorem 1.1, page 3,
gives spherical boundary from the Bergman--Einstein assumption. Corollary
4.2, page 14, supplies the algebraic-CR finite-quotient reduction; EXX
Section 3, pages 7--8, records the related boundary covering and interior
extension steps. Original localization, algebraicity, holomorphic continuation
and extension proofs retain their independent hypotheses and unread scopes.

**GS21 — Algebraic versus analytic boundary.** Huang's survey author
copy Theorem 3.1 and Corollaries 3.2--3.3, pages 3--4, record the algebraic
spherical uniformization argument, with original Huang/Huang--Ji inputs.
Compactness is retained from the surrounding context; the isolated Corollary
3.3 wording does not itself repeat it. The survey attributes real-analytic
spherical examples with infinite fundamental group to Burns--Shnider.
Those examples are not asserted to have Einstein Bergman metrics. Failure
of the boundary-only finite-quotient step does not disprove the Einstein
conjecture without algebraicity.

**GS22 — Finite-type consequences.** Main Corollaries 4.4--4.5,
page 8, import separate localization/asymptotic papers. The dimension-two
case and the N at least three case have different hypotheses. The latter
requires finite D'Angelo 1-type and h-extendibility at every weakly
pseudoconvex boundary point. These full external proof chains, including
the cited unpublished 2026 work, are not certified by this selection.

**GS23 — Huang--Li ancillary formulas.** In the controlling author
copy, (4.6) on page 14 reverses the smooth correction's sign relative to
(4.5); the weaker order used in (4.7) is unchanged. Lemma 5.2's proof on
page 17 wrongly assigns unit modulus to the quotient map's Jacobian.
The correct kernel pullback includes its Jacobian square, whose logarithm
is pluriharmonic off the branch. Equation (5.12) on page 18 writes the
opposite Ricci sign before using the standard negative Einstein constant.
Example 5.5's dimension-three kernel is correct, but its displayed
two-by-two calculation and page-20 value 20 do not give the full
three-dimensional determinant; that determinant grows as 20/s. Its corrected
non-Einstein conclusion survives. Equation (5.22)'s first double sum drops
1/ell, while the closed disk kernel and subsequent Einstein equation are
correct. These literal auxiliary defects do not refute the main GS theorem.

**GS24 — Other ancillary boundaries and final assessment.**
Ganguly--Sinha v3 page 3 prints f composed gamma=gamma in an invariance
sentence; top-form pullback and twisted coefficients give the correct
dictionary. Its unrestricted negative-Einstein-constant sentence on page 2
must be limited to the Bergman setting. Huang's survey page 3 gives the
quadratic cone cover with two variables but calls its source boundary
the three-ball, and its ambient/intrinsic dimension letters conflict.
The tangent-tube argument on pages 4--5 infers sphericity from local CR
homogeneity and has an incorrect all-directions quadratic coefficient in
base dimension at least two. That ancillary example is not imported or
certified here. The one-dimensional fiber square-root calculation is separate.
None of these findings is a counterexample to the main finite-quotient result.
The fully read main argument is unrefuted by this scoped convention audit
and its elementary diagnostics, with external proof inputs explicitly retained.

## Exact diagnostics and preservation

The exact-diagnostics record retains twenty elementary checks: bordered
inverses/determinants, radial Schur identities, nonabelian Q8 group/point/pole
fixtures, scalar roots, the disk exception, quotient Jacobian, Ricci sign,
full versus principal determinant, root-sum normalization, smooth-term sign,
tangent-tube quadratic coefficients and the elementary flat-metric boundary.
These finite examples and direct identities are not an arbitrary-group proof
certificate or a new mathematical result.

The first diagnostic attempt was interrupted during prolonged exact symbolic
evaluation, before any final certificate. V2 passed its first six checks but
was interrupted during a prolonged rational trace-sum calculation. Both helpers
and interruption records are preserved; no source-mathematics failure is
inferred. A distinct v3 attempt clears denominator powers before polynomial
determinants and evaluates the finite pole sum through individual polynomial
trace numerators. The exact identities and selected point are unchanged.

The main reading record has SHA-256
`68a55fc680cd4304b9ba417e5a5126a0878ad7407ee571a8c6723df10405c009`;
dependency reading record:
`a4c466eea6f91b19ffe426a8e3fe62ef25527496634f06157b7a9cded2403b99`.
The successful v3 exact-diagnostics record has SHA-256
`251ed4da0759e6e8762b657a5966585cd2160a2a97715e30056b7bece7449880`.
The immutable source manifest includes the exact diagnostics, acquisition
records, all matching image/text hashes and preparation/freeze helper sources.

All 425 active inputs, 108 protected inputs, both bibliographies, generated
book/index, 102 prior frozen manifests and 175 prior exports retain their
bytes. All 42 canonical atoms and status tiers 0/3/7/15/17 remain unchanged.
The open native catalogue source/PDF and editor are preserved. No original
theorem, independent model call, production receipt, Xean run, general
BJ22 Theorem 6.21 Siu/envelope repair or historical receipt extension is added.

Fetch both branch refs explicitly, push normally to work and update the
existing draft PR 2. Integrate an attributed Appendix H continuation,
Chapter 68 connection and Appendix L provenance only after this source
checkpoint; compile and read the matching final book pages before publishing
that integration. Continue recent primary research and incoming author progress.
