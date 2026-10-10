# Griffiths positivity and the sign of the top Chern form

Date: 7 October 2026. Baseline and fetched `origin/work`:
`195c73e64abfdd9c66d7f8c27c544c2ea101e5fc`; fetched `origin/main`:
`00957114db21b627e97369563032ceda9cea09c7`.

Yun-Heng Du, *Griffiths positivity does not imply positivity of the top
Chern form*, exact arXiv:2610.05931v1, submitted 5 October 2026,
07:48:50 UTC, constructs for every rank r at least nine a smooth
Griffiths-positive metric on O(1)^{direct sum r} over complex projective
r-space with a negative top Chern form on a nonempty open subset.
All fourteen actual main-paper pages and fifty-four selected dependency
pages were read as complete selected text with matching images:
68 distinct exact-source/page pairs in 35 sheets, two complete PDFs
and four partial selections. Twenty-four scoped records and twenty-one
exact elementary diagnostics keep pointwise Chern--Weil representatives,
cohomological classes and numerical positivity distinct.

The main construction is unrefuted by this review. This is an attributed
source audit, not a complete external proof-chain certificate, a new
original theorem, an independent model review, a production receipt or
a canonical problem solution. Adjacent dependency formula issues below
do not constitute counterexamples to Du's main theorem.

## Exact sources and actual reading

Cached sources are under
`source_material/Du_Griffiths_Chern_sources_20261007/`.

| Exact acquired file | Actual pages read | PDF SHA-256 |
| --- | --- | --- |
| Du 2610.05931v1, 14 pages | All 1--14 | `d3e98a87a87e813211826ba355fd1855c7e5c5a3060c9742cac989083207bc37` |
| Finski, JLMS 106(2) (2022), 1539--1579; DOI 10.1112/jlms.12605, author-linked publisher PDF, 41 pages | 1--5, 7--12, 17--21, 24; seventeen pages | `b38dac8563dfa7ef56c98ff2b79a0756d2ed5c7532d46324860ca469af93559c` |
| Caracciolo--Sokal--Sportiello, Advances in Applied Mathematics 50 (2013), 474--594; DOI 10.1016/j.aam.2012.12.001, published PDF, 121 pages | 1--4, 17--19; seven pages | `66288d97f5f8e93358f3900fd38594da0999ce867fe551bc320fd39ebeb73eea` |
| Hall quant-ph/0607035v1, 5 July 2006, 13:02:59 UTC, 16 pages | 1, 8--10; four pages | `11a9382a5be449f2e0fa4ca1fa3a492a32ba3842fe5778e2d300c0b259bba319` |
| Wan 2601.10424v2, 20 January 2026, 08:44:14 UTC, 16 pages | All 1--16 | `0a0ab4a05b0442b9fc0009957f761b5c3f14898c3ac820f97816ff8f9a30288d` |
| Idel 1609.06349v1, 20 September 2016, 20:41:04 UTC, 101 pages | 1, 4, 55--56, 59--60, 97--98, 100--101; ten pages | `93ab59982cf5ab90d87c688d4ca5927da7955b3b8b17a4041fb292af5a81c673` |

Finski actual page 1 is printed 1539; CSS actual page 1 is printed 474.
Hall's returned v1 has a printed 17 July 2018 typesetting date in
addition to its 5 July 2006 arXiv stamp. Its preprint title is
*Constructions of indecomposable positive maps based on a new criterion
for indecomposability*, distinct from the journal title cited by Du.
Theorem 4 was located and read in this exact v1 rather than assumed
to have the journal's numbering. Hall's journal edition was not read.
Only Du and Wan are fully read; no claim covers the other files' unread
pages. Finski's form-pushforward and full stronger-positivity proof
chains, Griffiths' original c2 proof, Fagioli's semipositive inputs,
Güler's signed Segre theorem and the original Gurvits proof remain
external inputs. Reading Idel's selected review is not reading all
of Gurvits' original paper.

Main reading SHA-256:
`713d11e6039ccca5ccb577bed7061d873904134ce00228ef3ac8e99382d120c4`.
Dependency reading SHA-256:
`5efd7f9bf08263871cf91fbea1937b5f429cdcaf496c5bd54193f873bd2e356d`.

## Scoped records

**DS01 — Version and provenance.** Main locators belong to the exact
October v1. Published Finski and CSS layouts and exact Hall, Wan and
Idel arXiv versions retain separate identities. Acquisition and scouting
are not actual proof reading. Every claimed selected text and matching
image was displayed before setting the reading flags.

**DS02 — The metric, the class and the number.** Theorem 1.1 changes a
particular smooth metric, not the holomorphic bundle or its Chern class.
For E=O(1)^{direct sum r} on projective r-space, c(E)=(1+H)^r and
the top Chern number is one. A representative negative on a small open
set is consistent with that positive integral. It does not refute
Fulton--Lazarsfeld numerical positivity or the existence of a different
positive representative.

**DS03 — Normalization and volume.** Main actual 1--4 uses
Omega=(i/(2pi))R and det(I+s Omega)=sum c_q s^q. For square Phi,
F_n(Phi)=det(partial_Y) det(Phi(Y)), and the local metric
h=I-2pi Phi(zz*) has top Chern form F_n(Phi) dV_n at the origin,
where dV_n is the product of i dz_j wedge dbar z_j. Its real-coordinate
coefficient is 2^n. No sign or factorial is suppressed when comparing
the determinant pairing with a normalized mixed discriminant.

**DS04 — Positivity dictionary.** Griffiths positivity tests
v*R(u,bar u)v for nonzero tangent and fibre vectors. Complex-linear
PSD-preserving maps preserve adjoints; a spectral decomposition reduces
PSD positivity to rank-one input. Strict positivity means positive
definite output for every nonzero PSD input. The ordinary positive-map
convention in Hall allows semidefinite output; Finski/Wan explicitly
distinguish it from strict positivity.

**DS05 — Bilinear apolar pairing.** Main actual 4--6 defines f(partial)g,
without conjugating coefficients of f. The Gaussian expression uses
f(conjugate coordinates)g(coordinates). It agrees with conjugate(det G)
only because determinant coefficients are real. Bars were checked in
the images. The factorial monomial moments and different-degree
vanishing are checked exactly; no missing-conjugation criticism is made.

**DS06 — Gaussian transfer.** Multiplication in the second argument
transfers to constant-coefficient differentiation in the first.
Gaussian integration by parts differentiates the holomorphic factor;
the antiholomorphic factor is not holomorphically differentiated.
These elementary rules, not a stochastic numerical fit, control the
final weighted determinant calculation.

**DS07 — Breuer--Hall positivity.** Main actual 7 defines
B_6(S)=tr(S)I-S-J S^T J*, with J=[0,I;-I,0]. For a rank-one S=ww*,
q=J conjugate(w) is orthogonal to w and has the same norm. B_6(ww*)
is the norm-squared multiple of the projection onto their common
orthogonal complement. PSD spectral decomposition completes the
positive-map proof. Hall v1 actual 8--9, Theorem 4, gives exactly
this argument. Indecomposability is not needed for Du's conclusion.

**DS08 — Adjacent Hall slips.** Hall v1 actual 9's Lemma 3 proof
asserts that a general complex skew-symmetric matrix is normal; an
exact complex fixture disproves that assertion. The odd-dimension
obstruction instead follows immediately from det M=det(-M^T).
Equation (29) literally repeats the same ket-bra in both terms and
therefore gives zero. Neither auxiliary passage is copied: Du's
explicit real J is unitary and skew, and the read Theorem 4 projection
argument remains valid. These are not counterexamples to that theorem.

**DS09 — The nine-dimensional map.** Partition the input into 3-by-3
blocks X,W,V,Y,Z and four ignored corner blocks. Du uses
Phi_t=diag(diag(Z,Z^T)+t B_6([X,W;V,Y]), X+Y^T), t>=0.
Transpose is complex-linear and preserves PSD Hermitian matrices.
For a PSD input the principal blocks and B_6 are PSD, so Phi_t is
PSD-preserving. Ignored blocks are not secretly identified with zero
before the determinant differential operator is considered.

**DS10 — Block determinant.** With A=X+Y^T, R=tr(A)I-A,
K=W^T-W=[k], L=V^T-V=[l] in the source's skew convention,
det Phi_t=det A [det(Z+tR)+t^2 k^T(Z+tR)l]^2.
The invertible Schur-complement calculation uses transpose-sensitive
skew covariance, then extends polynomially to singular matrices.
Both a nonsymmetric invertible fixture and a singular fixture check
the complete polynomial in t; those fixtures supplement the read
general proof rather than replacing it.

**DS11 — Ordinary Cayley constants.** CSS Theorem 2.1, actual 4/printed
477, and its elementary proof actual 17--19/printed 490--492 use all
n^2 independent matrix entries. At n=3, det(partial)(det M)^2=24det M;
all nine entry-weighted identities give 8M_ij. The symmetric-matrix
half-derivative convention is a different theorem. These constants
and the translated cubic-square identity are checked as exact polynomials.

**DS12 — Differential orders.** Main actual 9--10 uses ignored corner
variables to reduce det(partial_Y) to the 6-block and 3-block operators.
After the three Z derivatives, degree considerations permit Z=0.
The result is t^3 det A[24det R+16k^T Rl]. In A,k,l variables
the remaining operator is (D+Lop)^2. The signs of derivatives in W,V
must follow the source skew convention.

**DS13 — The vanishing contribution.** det R=tr A e2(A)-det A,
and D of each of these two terms is six, so D det R=0.
Apolar transfer and Cayley yield D^2(det A det R)=0.
This is also checked directly in the full nine-variable polynomial.
No positivity conclusion is inferred from this cancellation alone.

**DS14 — The negative contribution.** All 81 exact weighted covariances
equal 8 times the identity in the nine entry coordinates.
The weighted trace-square moment is 24 and Frobenius-square moment
is 72, giving -48. The remaining differential coefficient has factor
32. Consequently F_9(Phi_t)=-1536 t^3. The separate zero and negative
terms were checked directly without Monte Carlo sampling.

**DS15 — Strict perturbation.** Phi_1 is only PSD-preserving.
Adding eta tr(Y)I makes every nonzero PSD input positive definite.
F_n is a real polynomial in eta, so the strict negative coefficient
persists for sufficiently small positive eta. The optional explicit
rank-nine coefficient budget assumes coefficient bound one; it is a
termwise estimate, not a full arbitrary-rank expansion.

**DS16 — Higher ranks.** For r>9 append the scalar diagonal inputs
y_10,10,...,y_r,r, then add eta tr(Y)I_r. At eta=0 the differential
operator factorizes and the coefficient stays -1536; ignored cross
variables contribute no spurious permutation terms. A small positive
eta gives strict positivity and a negative coefficient separately for
each finite r. No rank-uniform perturbation size is asserted.

**DS17 — Local metric realization.** Du's explicitly normalized negative
quadratic jet gives h(0)=I, first jets zero and
R_ij(0)=2pi Phi(E_ij). Finski Proposition 2.10 and the complete rank-one
dictionary Proposition 2.11 were read on actual 11--12. Finski's
printed plus-jet formula (2.20) is not copied: in the convention fixed
by its (2.1) and by Du, the scalar h=1+d|z|^2 has curvature -d at zero,
whereas h=1-2pi d|z|^2 has normalized curvature d. The existential
local realization is obtained by the correctly normalized jet; this
does not disprove the existential statement.

**DS18 — Global patching hypotheses.** Main actual 12--13 compares
h_0=I/(1+|z|^2) with h_1=I-2pi Lambda(zz*) for a strictly positive
Lambda. Their first jets vanish at zero; the entire affine segment
has a uniformly positive metric and uniformly negative mixed Hessian
on a sufficiently small closed ball. This local Hessian fact is
proved from the common jets and compactness, not from a general
convexity assertion for the space of Griffiths-positive metrics.

**DS19 — Logarithmic cutoff.** H=h_1-h_0 is O(s), its first derivative
is O(sqrt s), and the log cutoff has first derivative O(1/(L sqrt s))
and second derivative O(1/(L s)). All cross-Hessian errors are O(1/L).
For sufficiently large fixed L, -h_u,bar u stays positive; the quadratic
first-derivative curvature term is nonnegative. The metric agrees
with h_1 on a smaller ball and the Fubini--Study direct sum outside
the prescribed neighborhood. Negative top Chern value at the origin
persists on an open set by continuity.

**DS20 — What Finski's equivalence imports.** The universal positive-map
question and universal Griffiths Schur question are equivalent in
Theorem 1.3. Its read actual-page-20 proof uses the form-pushforward
Theorem 3.2, whose full technical proof was not read here. This universal
equivalence is not an equivalence for every fixed rank's entire Schur
family. Stronger Nakano/dual-Nakano Schur positivity is an attributed
Theorem 1.1 input, not a new derivation from this partial reading.

**DS21 — The three-dimensional positive result.** Wan v2 Theorem 0.3
and 2.11 assume a strictly positive map and normalize sum B_ii=3I,
tr B_ij=3delta_ij by exact invertible scaling. The dual test matrix
C(xi)=(xi*B_ij xi) is positive with trace three. Its sphere moments
have denominators 12 and 60; Phi=average(10det C+27-12sigma_2 C).
Schur's sorted-eigenvalue rearrangement makes the integrand at least
det C>0. A complete two-parameter complex unitary/transposed-unitary/
trace family verifies the averaging identity and F_3=6Phi exactly.
The source's Lemma 2.6 proof has an extra projector prefactor in an
intermediate line; its final moment statement has the correct constant.

**DS22 — Scaling and principal compression.** Idel Theorem 1.2 supplies
the positivity-improving exact scaling input, without assuming complete
positivity. Selected later pages distinguish exact scaling from generic
approximate scaling. Printed equation (79) has an extra outer inverse;
the correct stationarity is H*(H(C)^-1)=C^-1. Adjacent strict-convexity
calculations and approximate-scaling sign slips are not imported.
For strict maps the familiar uniform bound H(X)>=a tr(X)I directly
gives compact determinant-one capacity sublevels. Wan's arbitrary-rank
c3 conclusion is treated by pointwise principal compression and plane
restriction. Its blanket subbundle-preservation wording is not used:
the positive ambient metric exp(-|z|^2)I_2 induces negative curvature
on the local subline spanned by (1,2z) at zero. Normal jets or the
algebraic principal blocks supply the required pointwise interface.

**DS23 — Remaining rank question.** Du's final paragraph asks for the
smallest rank admitting the negative top Chern representative. The
read rank-two and rank-three top-degree positive results and rank-nine
negative example leave ranks four through eight as source-scoped
candidate ranks. This is not an exhaustive audit of all intervening
literature or a new canonical problem atom. Wan's rank-four residual
trace term obstructs the naive three-dimensional integral method;
it is not itself a negative example in rank four.

**DS24 — Integration boundary.** Appendix H can contrast positive scalar
(1,1)-products with smooth higher-rank Chern--Weil representatives,
and Chapter 17 can connect that distinction to its line-bundle metric
discussion. No non-Archimedean higher Chern construction, singular
metric product, new envelope theorem or BJ22 Siu/closure repair follows.
Canonical problem statuses and the native open-problem catalogue remain
unchanged. Any new original rank result would require the prescribed
independent model and production gate, neither invoked here.

## Diagnostics, workflow corrections and preservation

The thirteen main exact diagnostics DC01--DC13 have immutable SHA-256
`24a5126a484c19f571245a9965de67923f744435b605e8239cd3dc8e89336e69`.
The eight dependency/interface diagnostics DD01--DD08 have SHA-256
`bc00d1e8fbcdcb290fd1201d7698dbeee60e34b995dac927c333fedf78c50f52`.
All twenty-one pass. They are elementary diagnostics of formulas and
interfaces, not complete theorem certificates.

The failed main v1 diagnostic used raw symbolic equality on complex
expressions; v2 simplifies expressions before equality. Its failure
record and helper are retained, not relabeled as a source error.
A scouting text extraction inadvertently reused four acquired text
paths. The original deterministic pdftotext bytes were restored only
after equality with their original acquisition hashes; scouting copies
were retained under distinct names. Source PDFs and all actual reading
texts/images were unaffected. The immutable correction record has
SHA-256 `fbdffb1142b7cfd394c67aca9b90f8eb6f0c33692343f443fe0d0739c93ee866`.

This source-only checkpoint preserves all 425 active TeX inputs,
108 protected inputs, both bibliographies, the generated 4,463-page
book and index, 98 prior frozen manifests and 169 prior exports.
The native catalogue source/PDF and open editor are preserved.
No original theorem, model call, production receipt, Xean run,
canonical-status change or BJ22 closure repair is added. Both GitHub
branch references were explicitly fetched; publication uses an ordinary
push to `work` and a scoped update to the existing draft PR.
