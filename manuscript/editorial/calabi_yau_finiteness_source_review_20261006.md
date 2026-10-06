# Calabi–Yau finiteness framework: primary-source review

**Research-only source audit; no mathematical result is admitted to the
book by this record.** The baseline is `3e7958e2e6c481e97bd9bbf87ab0d87fcf4119cc`,
matching `origin/work` after fetching both tracked branches. The controlling
source is Truong Dinh Dat, *A Pluripotential-Theoretic Approach to Finiteness
of Polarized Calabi–Yau Manifolds*,
[arXiv:2610.00361v1](https://arxiv.org/abs/2610.00361v1). It was submitted
30 September 2026 at 05:45:38 UTC and first announced in October. No later
version or journal edition is used here.

All 1,951 extracted text lines, including the proofs and bibliography,
were read in four complete ranges. All 34 actual PDF pages were displayed
in seventeen contact sheets and read. The final reading record is
`source_material/calabi_yau_finiteness_20261006/full_reading_v1_20261006.json`.
The earlier acquisition and progress records keep their historical flags.
The accompanying [manifest](calabi_yau_finiteness_source_review_manifest_20261006.json)
records the source hashes, actual-page reading and preservation checks.

The abstract on actual page 1, introduction on 2–3 and discussion on 33
explicitly describe a framework with unresolved capacity–perimeter and
metric-to-embedding steps. This is not an unconditional solution of
Calabi–Yau finiteness. Definition 2.1 on 3–4 uses smooth projectivity,
`c_1(M)=0` and an ample polarization, without a simply connectedness
assumption; elliptic curves and abelian varieties belong to that scope.
The source uses `ddc = i partial partialbar`, rather than the book's
`i partial partialbar/(2 pi)`. Its capacity volume is `integral omega^n`.
Early polarization classes are written `c_1(L)`, whereas Section 7 uses
`2 pi c_1(L)` for the curvature form. These conventions must be fixed
before transporting quantitative constants.

## Capacity estimates: what is actually assumed

Theorem 3.1 and its proof occupy actual pages 6–8. Assumption (iv), although
called local, already asserts for **every Borel set** K in M that

\[
 \operatorname{Vol}_\omega(K)
 \le C_0\operatorname{Cap}_{m,\omega}(K)^\tau,
 \qquad 1<\tau<\frac{n}{n-m}.
\]

The displayed conclusion is the same estimate with constants C and alpha.
It follows directly with C=C_0 and alpha=tau. Thus the conditional
statement is valid, but it does not derive this uniform estimate from
Calabi–Yau or polarization data. The coordinate-cover assertion in the
proof's globalization step is unnecessary for that literal conclusion;
uniform coordinate control has not been supplied by that step.

Theorem 4.1 and proof occupy 9–13. The stated estimate supplies one fixed
exponent tau>1 and assumes p>n/m. On page 10 the proof sets
q_H=p/(p-1), needs delta=tau/q_H>1, and then selects a new tau. The
displayed assumptions do not supply an estimate for that newly selected
exponent. For n=3, m=1, p=4 and the admissible fixed tau=11/10,
delta=33/40<1. The argument needs tau>p/(p-1), or volume–capacity
estimates for suitable exponents approaching n/(n-m). This identifies a
missing proof input; it does not provide a counterexample to the proposed
uniform solution estimate.

There is also a direct error in the truncation on page 11. For t>s it is
printed as

\[
 v_{s,t}=\max\left\{\frac{u+t}{t-s},-1\right\},
\]

and is asserted to equal -1 on A_t={u<-t}. At the value
u=-t-(t-s)/2 it instead equals -1/2. This is a check of the displayed
formula, not an example of a Hessian solution violating Theorem 4.1.
The global background-form scaling and step-size range in the subsequent
capacity comparison also need justification. The standard extinction
lemma under its own strong iteration hypothesis is not refuted here.

The separate Sobolev-cutoff proof of noncollapse in Theorem 4.6 on 13–15
uses the correct small-to-large Bishop–Gromov inequality. Its uniform
Sobolev bound remains an explicit assumption. Neither bounded potentials
alone nor the Calabi–Yau condition alone supplies that assumption.

## Diameter: a valid qualitative implication, an invalid printed constant

Theorem 5.1 on actual pages 16–17 assumes a total volume upper bound V_0
and noncollapse at every point for every radius up to r_0. On a connected
compact manifold these assumptions do imply a diameter bound. The
printed proof, however, reverses Bishop–Gromov: for R>r_0 and Ricci>=0
the volume ratio at R is at most the ratio at r_0. The proof uses the
opposite inequality and obtains the constant

\[
 D_{\rm printed}=\max\{2r_0,\,2(V_0/\kappa)^{1/(2n)}\}.
\]

An elementary flat model checks that this particular constant is false.
Let E_T=C/(T Z+i T^{-1} Z), T>=1, with the Euclidean metric and
omega=dx wedge dy. It has area one, Ricci zero and a degree-one ample
polarization. Its injectivity radius is 1/(2T). With r_0=1/(4T), every
ball of radius at most r_0 has area pi r^2, so V_0=1 and kappa=pi satisfy
the assumptions. Its diameter is

\[
 \operatorname{diam}(E_T)=\tfrac12\sqrt{T^2+T^{-2}}.
\]

At T=4 this is sqrt(257)/8, approximately 2.0039, whereas the printed
constant is 2/sqrt(pi), approximately 1.1284. The example addresses the
printed quantitative constant only. Allowing a genuine dependence on
r_0 restores the usual qualitative statement.

For completeness, the standard packing argument explains that distinction
without any Ricci hypothesis. Put d=2n and take points spaced r_0 along
a minimizing geodesic of length L. Their open balls of radius r_0/2 are
disjoint, and there are floor(L/r_0)+1 of them. Each has volume at least
kappa(r_0/2)^d. Hence a safe bound is

\[
 L\le\frac{2^d V_0}{\kappa r_0^{d-1}}.
\]

This ordinary consequence of packing is an explanation of the preserved
qualitative implication, not a new theorem or a book result.

## Regularity and compactness retain their additional data

Theorem 5.2 and proof on actual pages 17–19 require uniform background
geometry, positive density bounds and derivative bounds. The printed
derivative bookkeeping needs further review: the second-order step uses
the C^2 norm of log F and later steps invoke Hölder and higher derivative
data. Ricci-flatness could supply additional local information, so this
record does **not** declare the theorem false. Its argument is not used
as a source of curvature estimates from capacity control alone.

Theorem 6.1 on 19–22 separately assumes diameter, noncollapse and all
curvature derivative bounds. Those are the familiar strong inputs for
smooth Cheeger–Gromov compactness; the parallel complex structures can
then be passed to a subsequential limit. The paper has not obtained all
these hypotheses from its initial polarization data.

## Bergman estimates: supremum does not commute with the sum

Lemma 7.1 on actual pages 22–24 assumes the pointwise bound
rho_q(x)=sum_alpha |s_alpha(x)|^2<=C_B for an L^2-orthonormal basis.
It concludes sum_alpha ||s_alpha||_infinity^2<=C_B. Page 23 explicitly
acknowledges that the hypothesis does not generally imply this conclusion;
page 24 then imposes an additional uniform section estimate absent from
the statement.

The failure of the printed conclusion is visible on P^1 with O(1), q=1,
the standard Fubini–Study Hermitian metric and
omega=i partial partialbar log(1+|z|^2). Here integral omega=2 pi, as
required by the lemma's curvature convention. The sections
s_0=1/sqrt(pi), s_1=z/sqrt(pi) form an L^2-orthonormal basis, and

\[
 |s_0|^2=\frac{1}{\pi(1+|z|^2)},\qquad
 |s_1|^2=\frac{|z|^2}{\pi(1+|z|^2)},\qquad
 \rho_1\equiv\frac1\pi.
\]

Each squared supremum is 1/pi, so their sum is 2/pi, exceeding the
admissible choice C_B=1/pi. Lemma 7.1 concerns polarized compact Kähler
manifolds, so this test is within its stated scope, even though P^1 is
not Calabi–Yau. The pointwise estimate does imply each individual
supremum bound and the sum bound (N+1)C_B. Moreover, integration gives
h^0(L^q)=integral rho_q dV<=C_B Vol(M); a uniform volume bound can
therefore bound the dimension without interchanging a sum and supremum.

## Degree does not bound arbitrary projective schemes

Lemma 8.1 on actual pages 29–31, anticipated in Section 2.6 on 5–6,
covers arbitrary projective schemes of fixed dimension n in P^N and
degree at most D. That signature is too broad. Let X_r in P^2 be the
disjoint union of a line and r distinct reduced points off the line.
For all r it has dimension one and degree one, but

\[
 P_{X_r}(k)=k+1+r.
\]

Thus its Hilbert polynomials are not a finite set for n=1, N=2 and D=1.
Its sheaf section dimension is h^0(O_{X_r}(k))=k+1+r for k>=0,
whereas the degree-zero piece of its homogeneous coordinate ring has
dimension one. The proof on page 29 identifies these two Hilbert
functions in all degrees; that identification needs eventual comparison,
not an automatic equality in the small degrees used on page 30.
Degree controls the top coefficient and does not control the number of
lower-dimensional components in this general scheme category.

This example does not address the usual boundedness statement for
smooth pure-dimensional projective varieties. Theorem 7.3 on 25–28 and
Theorem 8.2 on 31–32 use smooth varieties and retain a fixed very ample
power, ambient dimension and degree. An appropriately scoped reduced
variety boundedness input can replace the overstrong Lemma 8.1. The
metric-to-uniform-embedding step has still not been supplied.

## Topological finiteness needs a smooth base or a stratification

Theorem 8.3 on actual pages 32–33 already assumes finitely many Hilbert
polynomials. The locus in a Hilbert scheme whose fibers are smooth need
not itself be a smooth base. Consequently Ehresmann's theorem for maps
of manifolds cannot be applied directly to each connected component of
that possibly singular locus as written on page 33. A finite
stratification into smooth algebraic strata, followed by the proper
smooth family on each stratum, supplies the usual argument. This is a
proof qualification; the familiar topological-finiteness consequence of
algebraic boundedness is not refuted.

## Admission boundary and continuing work

This review separates missing hypotheses, false printed formulas and
overbroad intermediate statements from valid conditional implications.
It neither disproves the proposed research programme nor supplies a
Calabi–Yau finiteness theorem. The simple models above are ordinary
checks of the source's printed formulations; they are not promoted to
new result typography, an original priority claim, a production-verifier
receipt or a solved canonical book problem. No independent model call
was made for this record.

The 425 active book inputs, 46 earlier frozen research-integration
manifests, current book/review/source exports, native open-problem
catalogue, inventory and inactive toric candidate remain byte-preserved.
The existing 4,361-page checked edition is still the current book.
No new TeX build or whole-book rereading is claimed for this source-only
checkpoint. Continue the related primary-source search, emphasizing
explicit hypotheses and usable, independently checked results.
