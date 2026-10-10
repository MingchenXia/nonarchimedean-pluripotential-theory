# Direct gradient estimates, quantitative subsolutions and Green potentials

Date: 6 October 2026. Baseline: `c5ec3c5ce41b8afb9ef1cc910d3a584e9911f814`.
This is a source-review checkpoint. Active TeX, the checked 4,394-page
book, the native catalogue and all 42 canonical problem statuses are
preserved. No original theorem or complete external proof repair is
admitted. The accompanying
[manifest](Guo_Song_direct_gradient_source_review_manifest_20261006.json)
records exact editions, reading scopes, diagnostics and preservation.

## Exact sources and actual reading

Read and individually displayed all 28 actual pages of Bin Guo--Jian
Song, *Stability and gradient estimates for fully nonlinear elliptic
equations on hermitian manifolds*,
[arXiv:2609.39726v1](https://arxiv.org/abs/2609.39726v1), submitted
30 September 2026 at 13:36:58 UTC. Current metadata lists only v1.
The PDF has 551,155 bytes and SHA-256
`f16b733e920504b82a67b6c61774cf74e12a5e0fd61317ea1d7ea7300ac7573a`;
the layout text has SHA-256
`aa80d583df78c3deda9505a22dc6c527c22ec6cfba37ad49b4ea5fe33307339d`.
All proofs, references and final matter were read in fourteen sheets.
The font-type extraction warning is recorded; the selected pages were
also displayed. Source normalization is `i partial bar-partial`, so the
book's `ddc=i partial bar-partial/(2 pi)` requires multiplying the source
potential by `2 pi`.

Read and displayed another forty fresh dependency pages in twenty-one
sheets, without claiming complete readings of these three papers:

- Guo--Phong, *On L-infinity estimates for fully nonlinear partial
  differential equations*, [2204.12549v3](https://arxiv.org/abs/2204.12549v3),
  submitted 28 February 2023 at 03:45:55 UTC: actual pages 1--4 and
  9--19, fifteen pages of a thirty-two-page PDF. This includes Theorem 1,
  Corollary 1, the entire local-estimate argument and their proofs on
  compact Hermitian manifolds. PDF 298,187 bytes, SHA-256
  `985bdc1a7f39b0229072534afafa697babbf76eed34381745723abf7568dbd6f`;
  text `45301818eec04ddf517a9734a9e6cd71132f73d548ce8b9c25a4a931413e9ed8`.
  Current metadata confirms v3. No reading of the distinct Annals
  publication PDF is claimed.
- Székelyhidi, *Fully non-linear elliptic equations on compact Hermitian
  manifolds*, [1501.02762v3](https://arxiv.org/abs/1501.02762v3): eight
  fresh actual pages 3--10, including Propositions 5--6 and their printed
  arguments. Reuse the precise acquisition in the earlier Fang dependency
  review: PDF SHA-256
  `0b8a8f819c99eda19c8041d3a02d6e2202a5f99a3958d79041cd4758b4d3b3dd`.
  Earlier pages 1--2 and 11--28 remain separately frozen. The cumulative
  selection is therefore 1--28 of thirty-four pages; pages 29--34 remain
  unread. The published journal PDF is not claimed read.
- Dong--Zhang, *Second order estimates for equations with sums of Hessian
  operators on Hermitian manifolds*,
  [2603.19045v1](https://arxiv.org/abs/2603.19045v1), submitted
  19 March 2026 at 15:41:19 UTC: actual pages 1--17 of twenty-four,
  including the full printed Lemma 3.2 argument and its algebraic
  preliminaries. PDF 347,110 bytes, SHA-256
  `c133961581ce3f6755fe155569cfe37badb091463c3eb8ac94baedc88e9ba5e8`;
  text `152fefd8e6a9b0096d800c1bb9a3a791173ff4b49812e6455f49f05cb46fb826`.
  Current metadata lists only v1. The main Hessian-estimate argument on
  pages 18--22 and references on 23--24 are not read here.

This checkpoint has 68 fresh physical pages and 35 displayed sheets.
The previously fully read Guo--Phong 2401.11572v1, fourteen pages,
supplies the quantitative-subsolution zeroth-order input. Previously
selected Székelyhidi and Tosatti--Wang--Weinkove--Yang readings remain
separate, with their recorded partial scopes. Guo--Song reference [1]
is Cheng--Xu **2501.17016v1**, not the different 2406.00953v2 read for
Xu's paper. Only current metadata of 2501.17016 was checked here; no
proof or viscosity-existence result from it is imported.

## The direct gradient statement and its data

Fix a compact Hermitian manifold of complex dimension at least two, a
smooth real background form chi, and the spectral operator
`F(A_u)=f(lambda(A_u))`, with `A_u=omega^(-1)(chi+i partial bar-partial u)`.
The background need not be positive or closed. The cone is open,
convex and symmetric, with `Gamma_n subset Gamma subset Gamma_1`.
The function is smooth, symmetric, elliptic and concave in the cone,
continuous on its closure, positive inside and zero on its boundary,
and grows to infinity on each admissible ray. Degree-one homogeneity
and a fixed lower bound on `det DF` are not assumptions of the direct
gradient theorem.

Fix **one smooth admissible subsolution** underline-u. For
`f_infinity,i(mu)=lim_(t to infinity) f(mu+t e_i)` and their minimum,
assume a common positive gap
`f_infinity(lambda(A_underline-u)) >= h(x)+delta_0`, with
`0<h<=H_0` for every solution in the family. Ordinary pointwise
C-subsolution existence, without common quantitative data, is weaker.
Normalize each smooth given solution by `inf u=0`. Theorem 1.1 gives
a gradient bound for densities with `norm gradient h<=H_1`, depending
on the fixed geometry, operator, subsolution and common gap, H_0 and
H_1. The bound is independent of `inf h`. It is an a priori theorem
for given smooth solutions, not an existence theorem for arbitrary
right-hand sides or a bounded weak-solution regularity theorem.

The density is prescribed as a function of x. Neither an exponential
penalty with a diverging parameter nor a density containing uncontrolled
derivatives of a varying auxiliary potential automatically satisfies
these family hypotheses. Thus this theorem does not, by itself, close
the earlier Xu/Fang weak auxiliary estimates.

## Common radius, auxiliary mass and stability

Lemma 2.1 and Remark 2.2 first obtain common positive r and finite R.
Shifting the subsolution spectrum down by r remains admissible, and
positive matrix increments P with a bounded value of F have `P<=R Id`.
The capped continuous majorant for h retains a uniform gap. Lemma 2.3
converts this into the delta/R data used by Guo--Phong's quantitative
subsolution theorem. Lemma 2.4 applies that theorem after shifting the
background by the fixed underline-u. It consequently controls the
oscillation using fixed common radii, not by replacing the radius
dependence with an Lp-only claim. The earlier radius objection to Xu's
citation therefore does not apply to this fixed-gap setup.

Lemma 2.5 concerns a fixed Hermitian metric alpha and smooth positive
auxiliary densities rho with average one, `rho>=a_0` and a uniform
Lq bound for q>1. For
`(alpha+i partial bar-partial psi)^n=c rho alpha^n`, normalized by
`sup psi=0`, the maximum of psi gives `c<=1/a_0`. A uniform Lq bound
on c rho controls every fixed logarithmic entropy exponent p>n.
Guo--Phong Theorem 1 then bounds psi, and their Corollary 1 supplies a
positive lower bound on the total Monge--Ampère mass, hence on c.
Keep c: general Hermitian geometry does not identify that mass with
the original metric's volume. The local auxiliary proof also uses
the cited exponential-integrability theorem; no new original proof
of that external theorem is claimed.

The trace lower bound and a fixed invariant Gauduchon adjoint measure
give a uniform W^(1,2) bound on normalized solutions, hence L1
precompactness by Rellich. This does not assume a gradient estimate.
Proposition 2.8 establishes
`norm(u_1-u_2)_infinity <= C(norm(h_1-h_2)_infinity+norm(u_1-u_2)_L1)`.
In its proof, the uniform auxiliary bounds for densities of baseline
at least one half and L2 norm squared at most four are fixed first.
Then fix kappa small, M large, and only afterwards epsilon_0 small.
The high-value set has volume at most `(16/7) epsilon_0`; the auxiliary
density `b+M zeta` has average one,
`b>=1-M(16/7)epsilon_0>=1/2` and second moment at most
`2+2 M^2(16/7)epsilon_0<=4`. Its peak is large enough to contradict
the matrix radius at the comparison maximum. The constants are not
chosen in a circle involving an uncontrolled peak.

For equicontinuous density families, Arzelà--Ascoli and this stability
bound turn L1 subsequences into uniform Cauchy subsequences. Lemma 2.9
gives C0 precompactness before derivative estimates.

## Comparison gradients and the stronger second-order conclusions

Proposition 3.1 fixes a proximity eta before choosing any comparison
function v. For every smooth admissible v with
`norm(u-v)_infinity<=eta`, it gives
`norm gradient u<=C(1+norm gradient v squared)`.
The constants do not depend on the derivatives of v or its distance
to the cone boundary. The proof uses the subsolution/linearization
alternative, the positive trace of DF, Chern commutation, and a
weighted gradient square. Pure Chern second derivatives need not be
symmetric. Torsion errors involve mixed derivatives and are absorbed
with retained positive square terms. The density derivative is
controlled by H_1.

For small values of h, admissibility of the fixed subsolution directly
gives the favorable linearized gap. For values of h bounded away
from zero, Lemma 3.2 invokes Székelyhidi Proposition 6 with the common
delta/R data and a compact interval of levels. That proposition is a
known literature input; the literal issue in its printed preliminary
cone construction below is not a counterexample to its statement.
An independent proof repair or complete verification of that external
construction is not claimed in this checkpoint.

Theorem 1.1 argues by contradiction: a uniformly convergent subsequence
has one fixed smooth member v within eta of all sufficiently late
members. Its finite gradient, inserted in Proposition 3.1, contradicts
divergence of those gradients. This avoids using an unknown a priori
gradient bound for v. The argument supplies a data-dependent bound,
without claiming an explicit formula for its value.

Corollary 1.2 adds a positive lower density bound and uniform C2 density
control. Székelyhidi's second-order estimate can then use the gradient
bound. Bounded eigenvalues and `f>=h_->0` remain in a compact subset
of the cone, so the complex Evans--Krylov theorem and a fixed-metric
Schauder estimate give a full C^(2,alpha) bound. The constants are not
claimed uniform as h_- tends to zero. Varying subsolutions need common
smooth norms and radii as well as gaps.

## Green potentials: retain three independent operator hypotheses

Theorem 1.3 is a different argument: omega is Kähler, chi is closed,
`Gamma subset Gamma_2`, the density has a positive lower bound and
controlled C2 norm of its logarithm, and conditions (6.2)--(6.4) are
imposed separately. These are trace growth of DF on large-trace level
strips, normalized ellipticity when the smallest eigenvalue is a
fixed negative fraction of the trace, and a refined sesquilinear
concavity inequality near the nonnegative cone. Concavity alone is
not condition (6.4).

Normalize the linearization by its trace. The fixed subsolution gives
a barrier on the large-trace region and a uniform bound for the
Dirichlet Green occupation integral. The real ABP exponent is 1/(2n).
Its use is localized to the set with normalized ellipticity; uniform
ellipticity on the whole varying region is not assumed. A fixed
Gauduchon adjoint trace integral bounds that set's volume. C0
precompactness and comparison with one fixed smooth potential then
make its Green integral of the gradient square small without an
a priori gradient estimate. The final weighted largest-eigenvalue
inequality contradicts its interior maximum through a boundary
supremum estimate. The kernel is for a possibly nonsymmetric operator;
symmetry or convergence of the varying Green kernels is not used.

For the root Hessian operator, differentiating `sigma_k=f^k` converts
Dong--Zhang's sesquilinear equation (3.2) into (6.4), with the squared
derivative coefficient `2k-(k-1)=k+1`. The large-eigenvalue threshold
and fixed positive level strip are retained. This conversion is
algebraically checked. However, the printed final step of Dong--Zhang's
proof needs further review, and its earlier real-case claims cite
other papers not read here. No unconditional certification of that
root/sum application or the entire external dependency chain is
claimed. Guo--Song's general theorem explicitly assumes (6.4), so
a defect in a cited verification of that hypothesis does not refute
the theorem under its stated hypotheses.

## Four literal diagnostics and four cleared objections

The frozen exact diagnostic record distinguishes:

1. Székelyhidi's printed Proposition 5 cone construction: take
   `f=lambda_1+lambda_2`, level four, mu zero, delta one quarter and
   R ten. The shifted level section lies in B_R, and v=(2,2) belongs
   to the printed A_delta. Every w in the printed C_v has sum zero,
   so C_v cannot contain the positive orthant as the proof claims.
   This diagnoses that construction, not the known quantitative
   alternative or Guo--Song's main theorem.
2. Dong--Zhang's displayed cone characterization by *all* multi-indices
   includes a repeated-coordinate second derivative of sigma_2,
   which is identically zero. Strict derivative positivity needs
   square-free indices. This does not invalidate the intended cone
   fact used later.
3. Dong--Zhang equation (3.1) prints bilinear squares for complex xi.
   At `lambda=(R,1/R,0)`, extra root y=0, fixed sigma_2=1 and
   `xi=(i,0,0)`, its left side is `-2/R^2`, smaller than the right
   side `-(1-gamma)/R^2`. R can be arbitrarily large. Equation (3.2)
   has the required conjugates and modulus squares; that correctly
   formulated inequality is not refuted by this check.
4. After (3.38), the text chooses its last remainder negative and
   concludes the lower bound with that term removed. Such a deduction
   does not follow from the displayed lower bound. The check does
   not construct an eigenvalue counterexample to Lemma 3.2 or certify
   a complete repair.

The root conversion coefficient is correct. Fixing M before shrinking
epsilon_0 clears a possible instability objection to the auxiliary
density argument. The harmonic-mean example really has `det DF`
tending to zero, consistent with the direct method not assuming a
universal determinant lower bound. Choosing eta before a fixed v
clears a possible circularity objection to the comparison gradient.
No diagnostic here refutes a main Guo--Song theorem. Original results,
independent production-model calls and verification receipts are zero.

## Preservation and continuation

The baseline has 5,057 tracked files, 425 active source inputs, 108
protected inputs, 66 prior frozen manifests (55 integration and eleven
separate source-review records) and 121 prior frozen exports. Preserve
all active and protected hashes, all earlier records and exports, the
checked book and generated files, and the open native catalogue.
Only this audit, its manifest, README and the progress programme are
written in the tracked repository. Inventory and whitespace checks
are run; there is no repeated build or PDF-review claim for unchanged
book sources, and no native compile or editor change.

Next explain the fixed common-gap route in Chapter 68 with its
prescribed-density scope and imported quantitative alternative kept
explicit. Keep the broader weak auxiliary and Green-hypothesis
verification gates separate. Continue reading the omitted dependency
proofs and recent related papers before enlarging conclusions. Fetch
both main and work before each remote checkpoint, incorporate incoming
author progress when present, and push work without force.
