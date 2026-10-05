# Complex geodesic distances and initial-velocity regularity

Date: 5 October 2026. Baseline work commit: `151282a340bd8f378916fbe3e6efe0fbca8da29b`.

## Admission and verification scope

Chapter 68 receives a short account of known complex finite-energy metric geometry, with a separate regularity hypothesis for the initial-velocity formula. Appendix L records the exact version and normalization. There is no new theorem environment, solution of a live atom, Finski counterexample verdict, Siu repair, general envelope repair, independent production-model call or receipt. Yao assumptions A2–A4 retain their previous scope. In particular, no topology for A4 or compatible sequence of finite Chow optimizers has been supplied.

The controlling source is Prakhar Gupta, *Complete Geodesic Metrics in Big Classes*, arXiv:2401.01688v1, submitted 3 January 2024 at 11:46:14 UTC. The current arXiv metadata lists this version only. Its 33-page PDF was acquired over HTTP 200 at 15:18:59.352424 UTC on 5 October; 491,817 bytes; SHA-256 `c6672f61245b9f6b88849e347192ad1c097e188332fc2144d1ea9819375557eb`.

All 2,116 Python `splitlines()` lines of the layout extraction were read in nine contiguous ranges: 1–240, 241–480, 481–720, 721–960, 961–1200, 1201–1440, 1441–1680, 1681–1920 and 1921–2116. This includes the references. Twenty-one actual PDF pages were viewed: 2, 5–7, 9–10, 15–24, 26 and 28–31. Their eleven image sheets and reading progress are pinned by the release manifest. Full extracted-text reading is not a fresh independent proof certificate for every antecedent cited by the source.

The DOI registry confirms the published work as *Transactions of the American Mathematical Society* 378(6) (2025), 4129–4172, DOI `10.1090/tran/9360`. Its online date in the registry is 19 March 2025. Both the version-of-record and accepted-manuscript PDF URLs supplied by that registry returned HTTP 403; their public `/journals/` aliases also returned HTTP 403. The DOI landing page could not be retrieved. These are source-access failures, not LaTeX compilation failures. No published text was obtained, no published/arXiv equivalence is asserted, and no diagnosis below is claimed to persist in the published version. The new `Gupta24GeodesicV1` entry keeps all numbered locators explicitly attached to the acquired initial version; the existing published `Gup24` entry is preserved.

## The source statements actually used

The setting is a compact Kähler manifold and a smooth closed real (1,1)-form theta in a big class. The energy spaces have full nonpluripolar mass `V = vol({theta}) > 0` and finite p-energy relative to `V_theta = P_theta(0)`, with `1 <= p < infinity`.

1. Section 4 defines the distance first for envelopes of regular obstacles. On actual page 16 the class `H_theta` consists of `P_theta(f)` for obstacles of bounded-Laplacian regularity `C^{1,bar 1}`. A C2 obstacle is a safe special case of this class. Definition 4.10 on page 21 extends the distance by decreasing approximation from these regular envelopes.
2. Lemma 4.12 on page 22 compares the *p-th power* of the distance to the unrooted integral `I_p(u,v) = integral |u-v|^p (theta_u^n + theta_v^n)`. The proof's last line drops that power typographically; the statement, the preceding comparison and Definition 4.10 determine the intended units.
3. Theorem 5.1 on page 22 gives completeness. It uses the comparison with I_p and the earlier complete I_p topology.
4. Lemma 5.3 on page 23 gives `d_p(u0,u1)^p = integral |dot u_{0+}|^p theta_{u0}^n` when the *fixed initial endpoint* is in `H_theta`, and the other endpoint is in `E^p`. Its proof decreases the other endpoint, bounds its initial derivatives against a shifted comparison geodesic, and passes to the integral. Keeping the initial endpoint fixed is essential to that argument.
5. Theorem 5.4 on page 23 says that weak geodesics between arbitrary `E^p` endpoints are metric geodesics. The regular-endpoint case uses Lemma 5.3. The general case passes to limits of *distances* using Lemma 5.2. It does not remove the initial-endpoint hypothesis from Lemma 5.3.
6. Theorem 8.3 on pages 30–31 gives the uniform-convexity inequality; only its p=2 quadratic inequality is imported. It makes the complete complex E2 space CAT(0). The printed second p-range has inconsistencies, so no general quantitative p>2 formula is copied.

The paper's regularity mechanism is visible before Lemma 5.3. Theorem 2.3 and Corollary 2.5, pages 5–6, localize the Monge–Ampère measure on regular obstacle contact sets. Theorem 2.8, pages 6–7, then compares endpoint velocity integrals for regular obstacle envelopes. Lemma 2.22, page 10, uses this identity with affine energy. Theorem 4.5, pages 18–19, works with nested contact sets and velocities against one common regular obstacle measure; Theorems 4.6 and 4.7, pages 19–20, remove the order assumption while retaining the regular obstacles. These are stronger inputs than convergence of potentials alone.

Theorem 3.11, page 15, treats regular relative envelopes with an analytic singularity type and explicitly stresses finite entropy after resolving the singularities. It cites Di Nezza–Lu's finite-entropy result, not a formula for an arbitrary continuous initial weight. The source's prescribed analytic-type metric statements have their own standing setting; the book's new subsection uses only the full-mass minimal reference class and does not claim arbitrary prescribed-singularity extensions.

## Normalization in the book

The source's distance uses unnormalized Monge–Ampère mass. The book denotes that distance by `d_p^G` locally and sets

    d_p^C = V^(-1/p) d_p^G,
    I_p^C(u,v) = V^(-1) integral |u-v|^p (theta_u^n + theta_v^n).

Thus `(d_p^C)^p` compares to `I_p^C`, and the initial-velocity integral is divided by V. We allow a constant depending on n and p without claiming a new uniform-in-p estimate. All metrics refer to *additive complex potentials* whose curvature is `theta + ddc u`; no identification with an arbitrary non-Archimedean metric or radial clock is made.

The uniform-convergence observation is a direct formal consequence: for bounded full-mass endpoints with `sup_X |u_j-u| <= delta_j`, `I_p^C(u_j,u) <= 2 delta_j^p`, hence `d_p^C(u_j,u) <= (2 C_{n,p})^(1/p) delta_j`. Boundedness makes these literal pointwise differences finite. This uses the whole I_p comparison, not an initial-velocity formula for the limit. It is an ordinary consequence of a known source result and does not require an original-general-result promotion.

For p=2, dividing the source's quadratic metric inequality by V preserves every term and gives the displayed CAT(0) inequality. It supplies metric convexity once the geometric comparison and convergence problem are specified. It does not establish equicoercivity, existence of compatible graded minimizers, A3 uniformly on minimizing sequences, or A4.

## Research-only continuation of the toric initial-point diagnostic

This section strengthens the preceding frozen Finski diagnostic using the just-read known I_p comparison. It is **not** inserted as a theorem or source-counterexample verdict in the book, and it has no independent production receipt. The original Finski audit and manifest are not edited retrospectively.

On P1 with O(1), write `r = log|z|` and use the Fubini–Study norm weight

    Phi_FS(r) = (1/2) log(1 + exp(2r)).

Set `Phi_0(r) = max(0,r)`. For n>=1 let `eta_n = 1/(n+1)` and

    Phi_n(r) = (1-eta_n)/(2n) log(1+exp(2nr))
               + eta_n/2 log(1+exp(2r)).

These are global smooth positive Hermitian norm weights, because the first term is the kth-root norm of the smooth metric with local squared expression `1+|z|^(2n)` and the positive Fubini–Study component supplies strictly positive curvature at both poles. Their transition at infinity has the correct degree-one logarithmic term. The elementary log-sum inequalities give, for every real r,

    0 <= Phi_n(r)-Phi_0(r)
       <= epsilon_n := (1-eta_n) log(2)/(2n) + eta_n log(2)/2,

with epsilon_n tending to zero. This estimate is uniform even on the two affine charts of P1.

To express these in the book's *squared additive potential* convention, set

    u_n,t = 2(Phi_n(r+t) - Phi_FS(r)),
    u_0,t = 2(max(0,r+t) - Phi_FS(r)),       t>=0.

The reference form is omega_FS, normalized to mass one. The potential at the two poles has its global continuous extension. The initial limit measure is normalized angular measure on the unit circle, where r=0. In a fixed segment `[0,T]`, the local joint weight is the convex function `2 Phi_n(r+T tau)` in the real spatial logarithm and time coordinate. Its Hessian has rank at most one; the associated bounded joint psh metric has zero homogeneous Monge–Ampère measure. Equivalently, its toric Legendre transform is `2(Phi_n^*(x)-T tau x)`, linear in time. This identifies it with the weak geodesic of its endpoints. The corner limit has the same Legendre description; the prior audit gives the elementary homogeneous-Monge–Ampère and chart checks.

For each fixed t, the uniform estimate gives `sup|u_n,t-u_0,t| <= 2 epsilon_n`. Every endpoint is bounded and has full mass one, so the known comparison gives `d_p^C(u_n,t,u_0,t) <= 2(2 C_{1,p})^(1/p) epsilon_n`. This also holds uniformly in t in a bounded segment. The triangle inequality therefore passes distances between the smooth endpoints to the distances between their corner limits.

Write `a_n(r) = Phi_n'(r)`. Strict convexity makes it a strictly increasing bijection from R onto `(0,1)`. The normalized curvature measure has radial expression `da_n(r)` and uniform angle. For the segment parameter tau in `[0,1]`, the initial squared-potential velocity is `2T a_n(r)`. Thus every smooth initial-velocity distribution is exactly uniform on `[0,2T]`, and Gupta's regular initial-endpoint formula gives

    d_p^C(u_n,0,u_n,T)^p = integral_0^1 (2T x)^p dx
                          = (2T)^p/(p+1).

Distance convergence therefore gives the exact candidate computation

    d_p^C(u_0,0,u_0,T) = 2T/(p+1)^(1/p).

In contrast, on the initial corner circle r=0, the right derivative of `2 max(0,r+T tau)` is `2T`. The pushforward of the initial curvature measure by that *literal pointwise right derivative* is the atom `delta_(2T)`, and its p-th absolute moment is `(2T)^p`. For T>0 these are different for every finite p>=1. In particular the p=1 distance is T, matching the affine energy slope computed in the preceding audit, whereas the initial derivative integral would be 2T.

This is compatible with every imported Gupta result: the corner potential is not a regular C2 obstacle envelope. Indeed its curvature is a measure on a circle; the regular obstacle contact-set identity would instead make it absolutely continuous with respect to smooth volume. The smooth metric distances and their limits coexist with failure of the derivative/curvature-pushforward passage. The argument targets a literal arbitrary-continuous-endpoint formula; it does not refute metric geodesicity, completeness, smooth positive quantization, or any of the Gupta statements imported above.

No finite checker is claimed to certify this analytic construction. The earlier exact checker supplies only its own recorded finite moment and energy tests. A production verdict, any priority claim, and promotion to an original general result remain absent.

## Literal initial-version diagnostics excluded from import

The actual pages confirm that several inconsistencies are printed in the initial PDF and are not solely extraction artifacts:

- Theorem 2.19, page 9, prints `d_p` against an unrooted p-th moment; Theorem 3.11, page 15, and Lemma 5.3, page 23, have the correct p-th power. The book uses the latter units.
- Lemma 4.12, page 22, has the correct power in its statement and drops it at the end of its proof. This is not used as a degree-one scaling identity.
- Several second inequalities in the uniform-convexity displays print `p<=2` where the surrounding complementary p-range is inconsistent. Only the correct overlapping p=2 case is imported; no corrected all-p theorem is independently promoted here.
- Theorem 6.2, page 26, invokes a pointwise inequality `|dot w_0| <= |w_1-w_0|`. Convexity by itself does not give an absolute pointwise derivative bound from endpoint differences. For bounded global endpoint difference C, the subgeodesic barriers `w_0-Ct` and `w_1-C(1-t)`, together with the convex upper bound, give the required global speed bound C. For that source's regular envelope endpoints, envelope monotonicity bounds C uniformly by the sup-norm differences of its obstacles; rooftop monotonicity supplies the intermediate bound. This elementary bounded-endpoint argument suffices for its domination step, without importing the printed pointwise inequality.
- Theorem 7.4's final contraction estimate on page 29 uses `d_p(u1^j,u0)` where the triangle argument requires `d_p(u1^j,u1)`. The surrounding limits show the intended endpoint, but no literal mismatched comparison is copied.
- Corollary 8.5, page 31, introduces a constant C(p) in prose but omits it from its inequality, and has an incomplete endpoint label. The book does not use that printed quantitative estimate. Theorem 8.3's p=2 inequality is the controlling metric-convexity input.
- The minor repeated endpoint labels in the affine energy discussion, and the limits labelled `t -> infinity` in the page 28 initial-velocity calculation, are not independently enlarged into claims about failure of the main distance construction.

These observations neither acquire the published version nor assert that its theorem is false. The known complex metric statements are imported in their stated scope, with the regular endpoint formula and source normalization kept explicit. The larger joint-measure convergence problem remains a research direction.

## Release validation

The release manifest records the complete 425-input source closure, old theorem/proof block preservation in Chapter 68 and Appendix L, the 108 protected analytic inputs, all 42 complete open-problem statuses, the unchanged standalone catalogue, reference and inventory checks, the fresh whole-book LaTeX build and PDF navigation/index checks. Prior frozen exports and research manifests remain immutable. This checkpoint uses the cloud environment only and does not invoke Xean or a subscription runtime.
