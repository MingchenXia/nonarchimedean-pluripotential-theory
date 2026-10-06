# Boundary mass, the Hölder subsolution erratum and interior oscillations

Four exact primary PDFs have now been read completely, including proofs,
references and publisher matter. All 77 physical pages were displayed
in 39 sheets. Four Zeriahi pages were previously read from the identical
hashed file and were reread here: this checkpoint adds 73 fresh physical
pages, comprising 68 research pages and five publisher pages. It is a
source review, with no active TeX or original mathematical admission.

## Editions and actual reading

| Source | Controlling edition | Actual PDF pages |
| --- | --- | --- |
| Amel Benali and Ahmed Zeriahi, *Erratum to “The Hölder continuous subsolution theorem for complex Hessian equations”* | [JEP 8 (2021), 779–789](https://doi.org/10.5802/jep.157), published online 22 March 2021 | All 12: publisher cover 1, research 2–12; sheets 01–06 |
| Ngoc Cuong Nguyen, *On the Hölder continuous subsolution problem for the complex Monge–Ampère equation, II* | [APDE 13(2) (2020), 435–453](https://doi.org/10.2140/apde.2020.13.435) | All 22: cover 1, research 2–20, publisher matter 21–22; sheets 07–17 |
| Ahmed Zeriahi, *Remarks on the modulus of continuity of subharmonic functions* | [2007.08399v1](https://arxiv.org/abs/2007.08399v1); arXiv v1 metadata: 16 July 2020, 15:20:28 UTC | All 15; sheets 18–25; pages 9–12 match the earlier reading |
| Amel Benali and Ahmed Zeriahi, *The Hölder continuous subsolution theorem for complex Hessian equations* | [JEP 7 (2020), 981–1007](https://doi.org/10.5802/jep.133), published online 16 July 2020; read with its explicit erratum | All 28: cover 1, research 2–28; sheets 26–39 |

The PDF SHA-256 values in table order are:

```
1ef038b5d22de71df875ad28c2140c8ba9c54dd41c8f3cfe937e8fe043d1321e
c3b57a3b4eaa0b3f2abbae6085d54c21e6226bc34005edcfa6be471e149d1a5d
8c55994b7b24f944cb5070669e2af5e7f2d995367b115934e30281d65e4ab16f
791646c992aa972d1bd12a75ccb7910ab40ac153ba9b77d0364303c033c59e74
```

Their complete extracted-text SHA-256 values are:

```
12bce93022d8fdbfc1d7d7c361af13519bd9a0e64b3897865c27168a3b83e9ad
cb77264838689b6b28c25ceba62ba36da7f7e8296af0dcd28c5fd879ce8fabde
acc3644d90635d62149726476eed4eb4adf75de5b93a586ec66ddd0bad309831
8fc65c500cd4b9c199044a8c90586a7cdb8253d5906fb82d280f0de08eb9f7de
```

Zeriahi's acquired PDF internally prints “Date: November 27, 2024” on
actual page 1, while the arXiv primary metadata identifies the only
listed v1 submission as July 2020. These are different facts. This audit
does not invent a 2024 submission or revision, and pins the bytes actually
read. The earlier Chapter 68 source selection was actual pages 9–12 of
this same PDF, not a reading of the entire paper. The original BZ journal
metadata download returned HTTP 503; its PDF was obtained successfully,
and the publication metadata was inspected through the primary web page.
All four PDF acquisitions succeeded.

## Nguyen: boundary localization without finite total mass

Theorems A and B are on a bounded strictly pseudoconvex domain. A
Hölder continuous psh subsolution vanishes on the boundary and dominates
the prescribed positive measure by its Monge–Ampère measure. Continuous
boundary data give a continuous solution; Hölder boundary data give a
Hölder solution. The measure and subsolution need not have finite total
mass on the open domain. Remark 1.1 uses −(−rho)^alpha, 0<alpha<1,
to illustrate infinite mass near the boundary.

The upper homogeneous Monge–Ampère envelope psi and lower subsolution
psi+phi bound u and agree with its boundary values. Their Hölder
differences give the collar error before any global gluing. One may
decrease the common exponent to accommodate the boundary envelope;
the original boundary exponent is not silently retained.

The extension phi_epsilon=max(phi−epsilon,A rho/epsilon) agrees with
phi−epsilon on a defining-function collar. Lemma 4.3 controls mixed
mass on interior collars by negative powers of epsilon. For Corollary
4.6, normalize the extension:

```
epsilon phi_epsilon=max(epsilon phi−epsilon^2,A rho).
```

This family has uniformly bounded Hölder and supremum norms for
0<epsilon≤1. Proposition 3.1 applied to the normalized family explains
the uniform exponential capacity constants; undoing the n-homogeneity
gives the epsilon^{-n} prefactor. The unnormalized coarse C/epsilon
norm bounds alone would not establish that uniformity.

Proposition 4.7 and Theorem 4.9 compare functions agreeing outside an
interior collar. They retain the comparison norms and separate ordinary
L1 error from measure-weighted L1 error. Lemma 4.10 uses the correctly
buffered Jensen estimate, with the mean error on Omega_{2delta} and
the Laplacian mass on Omega_delta. Bounded subharmonicity gives local
trace mass O(delta^{-1}); an O(delta) collar-volume error completes the
ordinary L1 estimate. This is different from assuming finite total
Laplacian mass and obtaining an O(delta^2) estimate.

The final displayed optimization has the form

```
sup(hat(u)_delta−u) ≤ C epsilon^alpha
                      + C delta^(alpha2 alpha3)/epsilon^(2n+1),
epsilon=delta^(alpha2 alpha3/(2n+1+alpha)).
```

It supplies a positive modulus only with the preceding stability,
weighted transfer and boundary-barrier inputs. Corollary C assumes the
Hölder psh subsolution on a neighborhood of the closed domain. That
extra hypothesis supports the larger-domain construction and finite
mass there. The maximal homogeneous Monge–Ampère extension is not
generally pluriharmonic, despite that word on actual page 19.

The statement that a general continuous subsolution problem was open
is historical to 2020. The already integrated Guedj–Lu continuous
domination result must be taken into account; this review adds no
canonical open problem from the old introductory sentence.

## What the BZ erratum actually corrects

The erratum explicitly identifies an incomplete proof of original
Lemma 4.2 for general nonzero Hölder boundary values and a wrong exponent
used at the end of the original Theorem B proof. Its Theorem B' retains
finite prescribed total mass and a zero-boundary subsolution in
E_m^0 intersected with C^alpha of the closed domain, 0<alpha<1.
E_m^0 includes finite total Hessian mass of that subsolution. Neither
finiteness assumption is deleted when this theorem is cited.

For C1,1 boundary data, Lemma 2.1 constructs a smooth m-subharmonic
boundary extension and a zero-boundary solution, then uses Cegrell
inequalities to control global mixed mass. For arbitrary Hölder data,
Lemma 2.2 instead works with (u−v)^m and applies the Błocki inequality
repeatedly. Taking an mth root explains its smaller transfer exponent.
The general-boundary proof uses local trace mass, rather than a global
Laplacian bound inferred solely from finite Hessian mass.

This separates three situations: finite-mass Hessian subsolution with
smooth boundary extension; finite-mass subsolution with only Hölder
boundary values; and the infinite-total-mass local Monge–Ampère theorem
of Nguyen. The later intermediate-Hessian infinite-mass extension in
Kołodziej–Nguyen v2 remains a separate source with its previously
recorded normalization and proof gates.

The erratum's printed quantitative exponents are not certified here.
There is an additional rooted-capacity issue in the proposition that
the erratum imports, described below. Its qualitative positive-exponent
mechanism can be explained without admitting those exact numerical
exponents or claiming a complete corrected quantitative proof.

## A shrinking collar is not a fixed interior compact set

Zeriahi's literal Lemma 3.3 on actual page 10 asserts a uniform oscillation
bound for x in Omega_{Bdelta}, for one fixed B and every small delta,
from a radial-mean error bound without boundary control. The following
elementary harmonic diagnostic disproves that uniform assertion.

On the unit disk, let u(z)=Im log(1−z), using the analytic branch since
Re(1−z)>0. It is bounded harmonic, so every positive radial average
equals u. For any fixed B>1 choose a>B, x_delta=1−a delta and
y_delta=x_delta−i delta/2. For sufficiently small delta both points
are in the disk, x_delta lies in Omega_{Bdelta}, and

```
|y_delta−x_delta|<delta,
u(y_delta)−u(x_delta)=atan(1/(2a))>0.
```

The oscillation cannot be bounded by a constant times a modulus tending
to zero uniformly on those shrinking collars. This also tests the
boundary-free collar formulation in the introduction and Corollary
2.3. It is not a counterexample to Theorem 3.2 with its explicit boundary
modulus, or to a fixed-compact consequence of the nested-ball argument.

On actual pages 11–12 the recurrence compares oscillations at delta
and (A+1)delta. It can be iterated only while the larger balls fit in
the domain. For E compactly contained in Omega, choose a positive
starting radius below a fixed multiple of dist(E,boundary). Boundedness
then controls the initial oscillation divided by the modulus at that
radius. The resulting constant is uniform on E and may depend on that
buffer. This is the scope needed by Chapter 68's ample-locus logarithmic
estimate. The existing logarithmic conclusion is not refuted; its prose
will make this positive buffer and starting radius explicit.

The real-dimension modulus condition is (2N/A) kappa(At)/kappa(t)<1
at sufficiently small scales. Powers with exponent strictly between
zero and one, and kappa(t)=|log t|^{-gamma}, satisfy it for suitable A.
This argument does not assert the Lipschitz endpoint. Positive averaging
kernels with the needed annular mass are used. On a Hermitian chart,
adding a quadratic background must dominate the metric: beta≤omega≤C
beta requires C beta, rather than beta alone.

## Fourteen diagnostics and their limits

The separate hashed diagnostic record preserves fourteen checks, four
in the modulus note, five in the BZ pair and five in Nguyen or their
shared prerequisites. Their scopes are as follows.

1. **Uniform shrinking-collar modulus:** the bounded harmonic model
   above refutes the literal boundary-free assertion. The fixed-compact
   consequence and the theorem with boundary control are distinct.
2. **Jensen regions:** Lemma 2.4 of the modulus note and Lemma 2.3 of
   the BZ original use the same Omega_delta for the mean error and
   Laplacian mass. On the unit disk take
   u=max(Re z−(1−delta/2),0). Its Laplacian support lies outside
   Omega_delta, but the radius-delta mean is strictly positive at
   x=1−1.1 delta in Omega_delta. The correct buffer is Omega_{2delta}
   against mass on Omega_delta. Erratum (3.4), written over all Omega,
   also requires its domain of regularization and collar treatment.
3. **Hermitian background order:** adding beta need not make an
   omega-psh potential subharmonic when beta≤omega. Add C beta≥omega.
4. **Poisson negative part:** multiplying a kernel lower bound by a
   negative integrand gives a positive error defect, not the printed
   negative one. The mean relation controls the negative part and
   allows a corrected dimensional bound; no suitably constanted full
   Poisson lemma is refuted.
5. **Weighted Hölder:** the factor in erratum (2.11) must use the
   total mixed measure, not unweighted domain volume. E_m^0 supplies
   finite mixed mass; the missing factor is absorbed in a properly
   stated subsolution-dependent constant.
6. **Wedge and mass bookkeeping:** the erratum's A'/B' displays need
   beta^{n−k−1}, and the power-difference induction carries R^m before
   its mth root. Dropping a nonnegative energy term proves an upper
   bound for the signed remainder, not its printed absolute bound.
7. **Rooted capacity stability:** in original Proposition 2.20, write
   c(s)=capacity({u<v−s}). From t^m c(s+t)≤A c(s)^tau and f=c^{1/m},
   the extinction scale is proportional to c(0)^{(tau−1)/m}. Actual
   page 15 instead writes c(0)^{tau−1}; it also prints f(t) where the
   recurrence requires f(s). With c(0)≤C epsilon^{−m−1}e, retaining
   the root gives the optimizing power
   (tau−1)/(m+(m+1)(tau−1)), rather than the printed
   (tau−1)/(1+(m+1)(tau−1)). For m=2,tau=2 these are 1/5 and 1/4.
   The erratum's quantitative chain still cites this proposition.
   This checks the derivation, not a counterexample to the theorem's
   quantitative conclusion. A correctly rooted positive-exponent
   recursion supports the qualitative route.
8. **Capacity range and branches:** writing volume≤C capacity^{1+r},
   Dinew–Kołodziej's range is 0<r<m/(n−m). The original twice prints
   1<r<m/(n−m), which is empty when n≥2m. Theorem A keeps two powers;
   large-capacity handling uses a normalized bounded test potential,
   not reversal of the order of powers at capacity≥1.
9. **Boundary-dependent mixed mass:** the original invokes inequalities
   stated for E_m^0 on nonzero-boundary potentials. The erratum supplies
   the C1,1 extension argument and a separate power-difference argument
   for general boundary data. A global trace bound is not silently used
   in that general case.
10. **Regularization remainder:** ddc phi=ddc phi_t−ddc(phi_t−phi).
    Nguyen (3.16),(4.38) and the BZ original's decomposition print a
    plus. Later absolute remainder bounds are compatible with a repair.
11. **Collar barrier sign:** Nguyen (4.11) needs −phi(z)+phi(boundary).
    Absolute Hölder differences restore its final collar estimate.
12. **Uniform capacity constants:** the normalized epsilon phi_epsilon
    family above clears the objection that the exponential constant
    would have to deteriorate with the coarse C/epsilon norm bound.
13. **Maximal versus pluriharmonic:** vanishing Monge–Ampère determinant
    does not imply pluriharmonicity in dimension at least two. Keep
    the neighborhood hypothesis and homogeneous envelope in Corollary C.
14. **Boundary and historical scope:** Nguyen has actual boundary
    barriers despite allowing infinite total mass; Zeriahi's global
    theorem retains boundary control. The 2020 open-problem description
    is not automatically a current open problem.

The harmonic and Jensen models, the weighted-factor model and the
rooted-power calculation were explicitly evaluated. These are elementary
diagnostics of literal formulas. They are not original theorem admissions,
independent production-model verification, or certification of a complete
external repaired proof. No counterexample to the main qualitative
Nguyen or BZ Hölder theorem is claimed.

## Next integration and preservation

The useful next book change is a scoped explanation of boundary barriers,
local trace mass and fixed interior buffers, together with a clarification
of the existing logarithmic mean-to-oscillation paragraph. The numeric
BZ exponent remains outside the admitted account. The non-spectral
structural chain, infinite-mass intermediate-Hessian quantitative chain,
original Kołodziej 2002 iteration PDF and published GKZ edition retain
their specific earlier gates.

The 4,398-page book and fourteen generated files, all 425 active inputs,
108 protected inputs, 71 preceding frozen manifests, 124 preceding
exports, the native open catalogue and all canonical statuses are
preserved. No unchanged-book rebuild, fresh book-PDF review, native
editor change or native compilation is claimed. Main and work were
fetched with explicit remote-tracking refspecs; no incoming author
commit was present at this baseline. Publication remains on work.
