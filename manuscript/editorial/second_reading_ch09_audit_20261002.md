# Chapter 9: second reading audit

Date: 2 October 2026. The complete original 3,251-line source,
`parts/part2/ch09_superforms.tex`, was read continuously from beginning to
end. It has no active input fragments. The revised source has 3,271 lines,
preserves all 65 labels and 80 formal environments, and leaves 71 formal
environments byte-identical. Nine environments change. The complete diff
and edited contexts were rechecked.

The orientation now separates affinity of transition maps, which ensures
commutation with the differentials, from the lattice condition imposing
integrality. The algebraic pullback by a nonlinear smooth map preserves
bidegrees, wedge products and the block involution, although it need not
commute with the differentials. The smooth section spaces are distinguished
from their finite-dimensional constant fibres: the one-variable table gives
module ranks and the two-variable table gives fibre dimensions. The
zero-dimensional exception is explicit. The basic smooth form algebra is
distinguished from continuous Hessian coefficients of C2 potentials and from
the limited distributional criterion later in the chapter.

The complementary pairing warning now computes the actual unnormalized
sign, (-1)^{p(n-p)} c_n = c_p c_{n-p}, which can be negative. The normalized
expansions supply the two missing factors and give prefactor one. The factor
c_p belongs to every grouped rank-one generator, equivalently to its whole
sum; inserting it per term does not double it, but inserting it a second
time does. The affine pullback proof distinguishes decomposable coefficient
arrays for vectors from those for covectors before using the exterior power
of the linear map on its test vectors. The numerical wedge examples and the
two six-by-six cone examples remain unchanged.

The product warning now explains the strongly positive test required for
weak positivity, and separates the pointwise product of positive Hessians
from constructing products of currents. Complex positivity terminology is
tied to Demailly's stated convention rather than declared universal. The
rank-one example assumes a smooth one-variable function and concludes
vanishing of the smooth top-degree density, without inferring mass on
singular tropical strata. Local convexity becomes global convexity by
restriction to segments on a convex domain; a maximum principle does not
create global convex coordinates on an arbitrary tropical space. The
nonaffine diffeomorphism example has the correct source and target intervals.
Log-sum-exp supplies a local chartwise smoothing ingredient, with gluing
requiring its own argument.

The radial mollification proposition and its proof remain unchanged. The
uncentred-kernel counterexample still gives x-epsilon m, showing failure of
domination and of monotonicity. Its explanation no longer claims evenness
is necessary: for a zero-barycentre probability kernel,
g_x(t) = integral f(x-ty) rho(y) dy is convex, and Jensen gives
g_x(t) >= g_x(0). For 0 <= s < t, convexity gives
g_x(s) <= (1-s/t)g_x(0)+(s/t)g_x(t) <= g_x(t).
Thus zero barycentre already supplies both properties. Conversely,
domination for every affine function forces the barycentre to be zero.
This is a direct classical consequence, not a new research result.

The distributional convexity proof passes the inequality to its possibly
minus-infinite limit only for 0 < s < 1; endpoint identities do not form
zero times minus infinity. The smooth approximation corollary retains its
domains U_epsilon. Its explanatory interface now distinguishes the generated
psh sheaf from first-stage approachability using Chapter 16's precise
hierarchy, and does not infer locally uniform convergence from decreasing
convergence for singular potentials. Polyhedral curvature products retain
their stated product hypotheses. The closing dictionary records signed
transposition by (-1)^{pq}, local versus global convexity, and affine pullback
versus invertible change of variables. The source notes agree with the actual
order and the limited distributional content of the chapter.

These are classical algebra, proof, example and scope repairs. Existing
published import locators and prior source evidence are reused for unchanged
results. No fresh primary-source retrieval, new original research claim,
independent verifier verdict or solved open-problem status is claimed.
Semantic, dependency, delimiter and structural checks replace the unavailable
legacy scoped writer.

The full book builds to 4,174 pages and 19,478,544 bytes, with zero TeX errors,
LaTeX/package warnings, overfull boxes, unresolved references or citations,
and rerun requests. There are 866 nonfatal underfull boxes. All Chapter 9
physical pages 373--420 and seams 372/421 were visually inspected in thirteen
contact sheets. The blank final verso is normal. No clipping, collision or
detached heading was found. Post-render references pass for 425 active files
and 12,564 unique labels. The open-problem inventory remains 42 atoms in
twelve families, with tiers (0,3,7,15,17). Exact hashes and scope checks are in
[the manifest](second_reading_ch09_manifest_20261002.json).

The selected review PDF is
`/workspace/book-completion-drafts/second-reading/Ch09_Review_2026-10-02.pdf`.
Chapter 9 passes this reading gate. Chapter 10's fresh source reading has
reached line 1,440, with no edits yet; its gate remains open. The complete-book
goal continues in the cloud.
