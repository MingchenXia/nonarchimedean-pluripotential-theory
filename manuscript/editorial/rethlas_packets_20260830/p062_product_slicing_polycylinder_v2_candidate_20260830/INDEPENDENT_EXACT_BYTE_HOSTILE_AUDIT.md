# Independent exact-byte hostile audit of P06.2 v2

Date: 30 August 2026

Auditor role: independent, fail-closed mathematical review.  I did not
participate in assembling the v2 proof, did not use the author self-audit as
evidence, did not call Rethlas, and did not edit either frozen mathematical
file or any live-book file.  Every uncertainty was to be counted as a gap.

## Exact target identity

The bytes reviewed were:

| target | independently recomputed SHA-256 |
|---|---|
| `p062_product_slicing_polycylinder_v2_statement_20260830.tex` | `147612fc96ddb973f5dd2df7ccc3da38798e3f3df46b462cd38b6cfaa9f1167b` |
| `p062_product_slicing_polycylinder_v2_proof_20260830.tex` | `e146c0eec6372995f881a3db054719969575515a913474a14d073ec17010627d` |

These are exactly the hashes assigned for this audit.  The failed-v1
production response, SHA-256
`9658be614a25bc74788023c4c83bfec07f054a93b265d895d1d5e66a4779e490`,
was reread only to identify its two objections; its verdict was not
transferred to v2.

The primary CLD statements were checked against the locally materialized
2025 source bytes (PDF SHA-256
`5690f999523017d184ab751bb55857ab1637b197d1186ad4fd2edba7e1bda719`;
text extraction SHA-256
`021be260392de1f3240858d4c775da86653518dfab4fd9c4c21a2406081b6c7e`).
The already verified finite-trace, arbitrary-field disc, and
rational-centred trace dependencies were also read in their
dependency-closed exact materialization.  This receipt audits how v2 uses
those dependencies; it does not replace their earlier verification
receipts.

## Fail-closed findings

### A. Exact extension of an arbitrary fibre test

1. **PASS -- the ambient and fibre completed residue fields are the same.**
   In affinoid coordinates `A -> C`, a point of
   `M(C completed_tensor_A H(x))` over the ambient point `y` evaluates in
   `H_Y(y)`.  The image of `C` already has fraction field dense in
   `H_Y(y)` by the definition of the ambient completed residue field.  The
   canonical image of `H(x)`, obtained by completing the image of `A`, is
   contained in that closure.  Hence adjoining `H(x)` in the fibre algebra
   neither enlarges nor shrinks the completed fraction field.  Thus the
   fibre point has completed residue field canonically equal to `H_Y(y)`.
   This argument applies to nonrigid `x` and nonrigid `y`.

2. **PASS -- the density used is the correct ambient density.**  The
   product `Y_0=U_0 x_K Z` is good and topologically separated.  CLD
   Section 11.1.10 therefore makes it almost good and gives the dense
   embedding `kappa_{Y_0}(y) -> H_{Y_0}(y)`.  The proof does not substitute
   `kappa(x)` for this ambient local residue field, which was one source of
   danger in v1.

3. **PASS -- strict approximation gives literal norm equality.**  Every
   fibre moment is a unit, so its value at `y` is nonzero.  Density permits
   an ambient residue class `c` with `|c-f(y)|<|f(y)|`.  A representative
   ambient germ `g` has nonzero residue and is consequently a unit.  After
   restricting to the fibre, continuity preserves the strict inequality
   on a neighbourhood; the ultrametric inequality then gives the exact
   identity `|g|=|f|` there.  This is equality, not asymptotic
   approximation.

4. **PASS -- the local smooth representatives restrict exactly.**  CLD
   Corollary 15.1.2 represents the given ordinary smooth function locally
   as a smooth real function of finitely many logarithmic norms of fibre
   units.  At the central point the lifted ambient units have exactly the
   same norm vector; continuity allows the ambient neighbourhood to be
   shrunk into the domain of the same real smooth function.  The resulting
   ambient `Phi_y` therefore restricts literally to `varphi`, with no need
   to lift an analytic function itself and no overlap cocycle to solve.

5. **PASS -- the ambient partition is in the cited scope.**  The fibre is
   closed over the Hausdorff base point and `supp(varphi)` is compact, hence
   it is a compact closed subset of the Hausdorff total space.  The finitely
   many ordinary ambient moment neighbourhoods cover it.  CLD Corollary
   15.2.9 applies to precisely such a compact closed set in a locally
   holomorphically separated analytic space and supplies nonnegative smooth
   functions, each with compact support contained in its assigned
   neighbourhood, whose sum is one near the compact set.

6. **PASS -- zero extension, exact gluing, and relative support close.**
   Since `supp(theta_i)` is compactly contained in `W_i`,
   `theta_i Phi_i` is zero on a neighbourhood of the complement and extends
   smoothly by zero.  At a fibre point, every nonzero summand uses a local
   lift equal to `varphi`; on `supp(varphi)` the weights sum to one, while
   off that support `varphi=0`.  Hence the glued restriction equals
   `varphi` at every fibre point.  Its support lies in a finite union of
   compact supports.  A compact subset maps properly to the Hausdorff
   affinoid base, giving the required `U`-proper support.  The ambient
   neighbourhoods may be chosen over the ordinary interior of the
   affinoid neighbourhood of `x`, so the later compactly supported test is
   also a legitimate test for the current on the original product.

**Conclusion for failed-v1 gap 1:** closed.  The v2 argument constructs the
required exact ambient extension for every compactly supported ordinary
CLD-smooth fibre test; it does not assume a restriction or pullback of an
arbitrary current.

### B. Continuous-multiplier slicing

7. **PASS -- positive decomposition and uniform control.**
   `tau=d'd''Phi` is a compactly supported symmetric `(1,1)`-form.  CLD
   Proposition 6.5.2(b) applies on the almost-good total space and writes it
   as the difference of compactly supported positive forms.  Their
   restrictions to the one-dimensional fibres remain positive.  For the
   flat, boundaryless, pure-relative-dimension-one product projection, CLD
   Theorem 16.3.3(d) makes both fibre masses continuous, hence bounded on
   the compact base under consideration.  The displayed estimate therefore
   proves uniform convergence of the fibre integrals.

8. **PASS -- the Fubini limit is legal on both sides.**  CLD smooth
   functions approximate the continuous multiplier uniformly near the
   fixed compact support (equivalently, first insert the compact smooth
   cutoff of Corollary 15.2.5 and apply Theorem 15.2.6).  Each smooth
   product has relative top degree and support compact over the base, so
   Theorem 16.5.4 and Corollary 16.5.5 apply.  The positive decomposition
   controls the fibre side uniformly; on the total-space side uniform
   convergence against the fixed compactly supported signed top-degree
   Radon measure gives the limit.  No continuous coefficient is falsely
   declared tropical-smooth.

9. **PASS -- bidegrees and the current pairing match.**  If
   `m=dim B`, then `Phi pi^*alpha` has bidegree `(m,m)`, the test degree for
   a `(1,1)`-current on the `(m+1)`-dimensional product.  Since `alpha` has
   top bidegree on the base, both of its differentials vanish, so every
   horizontal and mixed Leibniz term vanishes and only
   `d'd''Phi wedge pi^*alpha` remains.  The sign convention is immaterial
   because the resulting pairing is zero.

10. **PASS -- vanishing of the fibre integral function follows.**  A
    strict base is very rich by CLD Theorem 16.4.4(b), and CLD Corollary
    7.3.12 makes the map from continuous functions to `(0,0)`-currents
    injective.  Thus the continuous fibre integral `G` vanishes.  At `x`,
    smooth restriction commutes with `d'` and `d''`, and the exact identity
    `Phi|_{X_x}=varphi` gives the desired fibre current equation.  This
    covers arbitrary, not merely rigid, base points.

### C. The annulus reduction and one-variable scope

11. **PASS -- the polynomial tube is correct.**  For a rigid annulus point
    with minimal polynomial `P` and `s=|T(y)|`, uniqueness of the extended
    absolute value gives `|c_i|<=s^(d-i)` and the nonzero constant term has
    norm `s^d`.  If `|T|<s`, the constant term strictly dominates; if
    `|T|>s`, the leading term strictly dominates.  Therefore
    `{|P|<s^d}` is contained in `{|T|=s}`.  It is the inverse image of the
    strict target disc under the monic polynomial map, hence the map is
    finite flat of full degree `d` by the free basis
    `1,T,...,T^(d-1)`.

12. **PASS -- the endpoint Gauss fibre and trace limit retain all degree.**
    At radius `s`, the initial polynomial has degree `d`, including when
    lower terms tie.  The rational-function extension generated by `U`
    over that generated by `in_s(P)(U)` has degree `d`, including its
    inseparable part.  The graded fundamental inequality and the total
    finite-flat degree leave a single Gauss point of local degree `d`.
    Finiteness/properness and that singleton fibre give a target
    neighbourhood whose whole inverse image lies in a chosen relatively
    compact annulus neighbourhood.  Continuity of the verified finite trace
    as the interior Gauss points tend to the boundary therefore identifies
    `d h(y)` with `d h(eta_s)`.

13. **PASS -- rigid density is used only where valid.**  A standard strict
    open annulus is locally covered by strict affinoids, on which rigid
    points are dense.  The rigid-to-skeleton identity, radial affinity, and
    continuity then determine the function at all analytic points.  No
    density of `K`-rational points is asserted.

### D. Canonical multivariate Gauss endpoint

14. **PASS -- finite Laurent sums are order independent.**  A
    one-coordinate Gauss replacement takes the maximum over that exponent.
    For a finite Laurent sum, iterating in any order gives
    `max_nu |a_nu| product_j s_j^(nu_j)` because finite nested maxima
    commute.  At an intermediate stage the coefficients are evaluated in
    the appropriate completed residue field of the remaining base point;
    its one-variable Gauss extension uses the same maximum, and isometric
    completion changes none of the finitely many coefficient norms.

15. **PASS -- Laurent completion is justified.**  Around a fixed interior
    radius vector, choose a compact closed subpolyannulus.  Its analytic
    algebra is the Banach completion of the Laurent polynomials, including
    for generalized real radii.  Every analytic point is a bounded
    multiplicative seminorm and is continuous for this Banach norm.
    Equality on the dense Laurent subalgebra thus extends to every
    convergent Laurent series.  Equal seminorms on this affinoid algebra
    determine the same analytic point.

16. **PASS -- the endpoint is canonical and continuous.**  The common
    seminorm is exactly the standard multivariate Gauss seminorm, so all
    orders end at `sigma(s)`.  On a compact logarithmic subrectangle,
    evaluation of a Laurent polynomial at `sigma(s)` is the maximum of
    finitely many continuous monomials.  Uniform Banach approximation
    passes continuity to every analytic function.  Since the Berkovich
    topology is initial for these evaluations, the Gauss section is
    continuous.

17. **PASS -- nonrigid coordinate fibres and the factorization are
    covered.**  The slicing proposition applies over each successive base
    point with its complete residue field.  The one-dimensional annulus
    result over that field preserves the value of `h` when the coordinate
    is replaced by its same-radius Gauss point.  The preceding canonical
    endpoint calculation therefore gives
    `h(z)=h(sigma(|S_1(z)|,...,|S_q(z)|))` for arbitrary `z`, proving the
    continuous factorization through tropicalization.  Disc coordinates
    are first removed by the verified arbitrary-field disc theorem; the
    zero sections in different disc factors commute.

**Conclusion for failed-v1 gap 2:** closed.  V2 proves the endpoint,
order independence, Banach/Laurent passage, and continuity needed for the
factorization rather than merely asserting iterative replacement.

### E. Joint affinity, endpoints, and stated conclusions

18. **PASS -- the final distributional test has the right support and
    degree.**  A compactly supported positive top form in the disc factors
    and the pullback of a compactly supported `(q-1,q-1)` Lagerberg form
    give a compactly supported `(p+q-1,p+q-1)` test.  Top degree kills the
    derivatives of the disc form.  Weight-one split-torus integration and
    Fubini reduce the current equation to `d'd''[phi]=0`; the strictly
    positive disc mass cancels.  The resulting vanishing of every
    distributional Hessian entry makes `phi` affine by local convolution,
    overlap compatibility, and continuity.

19. **PASS -- quantifiers, endpoint variants, and regularity conclusions
    agree with the proof.**  The argument includes `p=0`, `q=0`, arbitrary
    nonnegative dimensions, and arbitrary complete residue fields.  The
    absolute analytic interior of each stated closed or half-closed
    standard factor is the corresponding open factor and is dense; the
    affine formula extends uniquely by continuity.  Real affine
    combinations of logarithms of analytic units are ordinary CLD-smooth
    with zero Hessian.  The cited Gubler--Jell--Rabinoff equivalence then
    gives weak smoothness and harmonicity, while the explicit unit-log
    expression gives classical pluriharmonicity.  The proof does not claim
    current pullback under arbitrary scalar extension or a result for
    general non-product analytic germs.

## Independent compilation

The minimal wrapper was compiled out of tree with three `pdflatex` passes
via `latexmk -pdf -interaction=nonstopmode -halt-on-error`.  Exit code was
zero.  The final log had no undefined reference, undefined citation,
overfull/underfull box, or other LaTeX warning.  The independently produced
eight-page PDF had SHA-256
`dedf6785fd73230d2369205bd5c714e86549b8e0f220b91859190cd3ee160adb`.
The different PDF hash from the author-side build is expected from PDF
build metadata; the target TeX hashes remained unchanged after compilation.

## Verdict

**PASS: zero critical errors and zero unresolved proof gaps.**

In particular, both gaps reported against v1 are genuinely closed in the
exact v2 bytes identified above.  This independent receipt is not a
production verification: the packet must remain quarantined until the
dependency-closed exact bytes receive a fresh production Rethlas verdict.
