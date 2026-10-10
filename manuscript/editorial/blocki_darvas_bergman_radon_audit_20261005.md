# Błocki–Darvas: Bergman measures and bounded curvature

Controlling baseline: work commit `1cad11421309e14922b8d543d6c17628d7593214`.
This is an ordinary primary-source import of identified known results,
with explicit normalization and scope. It is not a new general theorem,
production-model receipt, proof of assumptions A2–A4 or repair of the
general Boucksom–Jonsson Siu/envelope argument.

## 1. Acquired and actually read source

The controlling text is arXiv:2602.03111v1, submitted 3 February 2026,
*Sharp C^{1,bar1} estimates in Kähler quantization and non-pluripolar
Radon measures*, by Zbigniew Błocki and Tamás Darvas. The arXiv PDF
and the PDF currently linked from Błocki's author publication page both
have 18 pages, 622,246 bytes and SHA-256
`81c8907fa05b5e8f92ec907b62c917f40b7971f98f12a5496fcbe1f1f74d95d3`.
Their complete bytes were compared and are identical. This authenticates
these two acquired files, without assigning a publisher version,
publication date or identity to any other file.

All 1,147 Python-split extracted lines, including references, were read
in four consecutive ranges: 1–285, 286–560, 561–845 and 846–1,147.
All eighteen actual PDF pages were then rendered and inspected in nine
contact sheets. Only successful actual image views count. Immutable
initial acquisition records retain their initial unread flags; the
separate reading-progress record records the subsequent work.

The primary cache is `source_material/blocki_darvas_radon_20261005/`.
Its discovery web record pins the arXiv metadata, author page and primary
HTML/PDF links; these do not replace the cloud PDF reading or inspections.
The actual-page manifest is
`/tmp/blocki_darvas_radon_primary_20261005/manifest.json`.

## 2. Exact imported signatures

Chapter 68 uses a compact smooth complex polarized manifold of positive
dimension, an ample line bundle L and a smooth positive reference h.
It uses only sufficiently large very ample tensor degrees. With the
book's ddc=i/(2pi) partial partial-bar, omega=-ddc log h and
V=integral omega^n, the logarithmic potential phi satisfies
omega_phi=omega+ddc phi. Its Hilbert norm is the integral of
|s|_h^2 exp(-k phi) omega^n on the entire H0(X,L^k).

For the measure theorem phi lies in the full-mass class E(X,omega).
Full mass gives zero Lelong numbers, hence exponential integrability
at every fixed degree. The cited known convergence is stated in exact
probability normalization:

    beta_k(phi) = K_k(phi) exp(-k phi) omega^n / N_k,
    integral beta_k(phi) = 1,
    beta_k(phi) --> MA_omega(phi) / V weakly.

The controlling anchors are Theorems 1.4 and 5.4 (actual pages 4 and
16). No finite-energy hypothesis is inserted. The prescribed-measure
form first solves MA_omega(phi_nu)=V nu for a nonpluripolar probability
nu, using the source's identified complex full-mass Calabi–Yau input.
It does not assume that nu has a density or that phi_nu has finite energy.

The separate regularity theorem, Theorem 1.1 (actual page 2), requires
bounded Laplacian/Levi coefficients and the current inequalities
0<a omega<=omega_phi<=A omega. The bounds have lower coefficient
a^(n+1)/(C(1+A^n)), upper coefficient C(1+A^(n+1))/a^n and
degree threshold C/a. C depends only on the fixed polarized background.
Its convergence is C^{1,alpha} for alpha strictly between zero and one.
Bounded Laplacian is distinguished from bounded all-real second
derivatives, and the C^{1,1} norm endpoint is not asserted.

## 3. Normalization independent of a raw factorial convention

The source uses i partial partial-bar; its background form is
Omega=2pi omega with the **same** logarithmic potential phi and the
same exp(-k phi). One does not divide the logarithmic potential by
2pi while retaining the same Hermitian metric. A constant rescaling
dV -> c dV rescales an orthonormal section basis by c^(-1/2), hence
K -> c^(-1) K and P -> P-k^(-1)log c. The product K exp(-k phi)dV
and beta_k are unchanged, as are the curvature forms. This is a direct
finite-dimensional calculation, not an asymptotic comparison of
uninspected versions.

The probability normalization is integral-one at every nonzero section
degree. It therefore does not use the source's literal raw factor
(2pi)^n/k^n or its displayed raw dimension/volume identification on
actual page 13. In the book's ordinary wedge/intersection convention,
Riemann–Roch is N_k/k^n -> V/n!, not V. With Omega=2pi omega,
the raw source-looking prefactor has total mass (2pi)^n N_k/k^n,
which tends to integral Omega^n/n! when powers are ordinary wedges.
Such a literal formula cannot be copied with raw top wedges as its
target measure in dimension at least two. A divided top-volume
convention can account for a scalar; the chapter avoids that ambiguity
by stating only the canonical probability form of the known theorem.

The elementary projective calibration is already visible on P2 with
L=O(1): N_k=(k+1)(k+2)/2 and V=1. The raw k^(-2) section-density
mass tends to 1/2, whereas N_k^(-1) normalization gives mass one in
every degree. On P3 the corresponding leading factor is 1/6. These
are exact normalization checks, not independent certificates of the
analytic convergence theorem or assertions that its intended
probability conclusion fails. The active text introduces no original
counterexample heading and makes no priority claim.

## 4. Proof dependencies and what they establish

Theorem 1.2 (actual page 3) proves local evaluation/first-jet estimates
on a bounded pseudoconvex domain. Upper kernel bounds use spherical
Jensen and bounded Laplacian; first-jet upper bounds use Lemma 3.1.
The lower bounds use Theorem 3.2's sharp transversal jet extension
(pages 9–12). Theorem 3.6 (page 12) transfers these through Lemma 2.3
(pages 6–7) to the compact polarized case. The evaluation-to-jet ratio
is the Fubini–Study curvature, and gives Theorem 1.1.

Theorem 2.4 (page 7) is the quantum comparison principle. Its proof
uses ordering of Hilbert norms, equality of the finite-level total
masses and the maximum potential; it does not rely on plurifine
locality of the weighted Bergman density. Proposition 5.2 (page 15)
compares degree k at phi to degree 2k at phi/2 using a smooth-reference
peak section. Proposition 5.1 (pages 14–15) supplies the lower bound
for a strictly positive current. Proposition 5.3 (pages 15–16) combines
these with P(alpha phi), alpha>1, to obtain small asymptotic quantum
mass on sufficiently deep sublevel sets. Theorem 5.4 then reduces to
the finite-energy Theorem 4.3 using bounded truncations and equality
of the limiting masses.

In the finite-energy step, Proposition 4.2 (page 13) supplies the
perturbed energy convergence. The derivative statement (31) and
concavity sandwich on page 14 give weak convergence; the argument
does not differentiate an arbitrary pointwise-convergent family
without the concavity bounds. The full text and dependencies within
this controlling file were checked. References to other papers are
identified imported inputs, without a new claim to have fully reread
every cited dependency or independently certified the whole analytic
theorem. Existing source-checked complex energy/Calabi–Yau conventions
are retained.

## 5. Literal auxiliary clauses excluded from copying

- Actual page 1 says the Bergman potential is a smooth Kähler
  potential at all k>=1. An ample L need not even have nonzero,
  basepoint-free sections at every small degree. The book uses only
  sufficiently large very ample k, and lets the constant in the
  regularity threshold absorb that background threshold.
- The source calls the quantum measures smooth on page 4. The
  factor exp(-k phi) need not be smooth for singular phi; the chapter
  says integrable density, while retaining a smooth kernel and
  Fubini–Study form for large k. The weighted measure is not the
  top Monge–Ampère wedge of that form.
- The local jet extremal formula on page 3 prints f(0)=0 at a
  general evaluated point z. Its proof on page 9 uses f(z)=0
  before translating to the origin. The chapter/audit uses vanishing
  at the evaluated point and does not import the literal origin clause.
- The auxiliary calculation in Lemma 2.2 on page 6 omits log before
  the section sum and shifts basis indices e0/e1/e2. The chapter uses
  P=k^(-1)log K and the usual logarithmic Fubini–Study curvature;
  it does not copy that displayed differentiation or index arithmetic.
- Page 13 prints I(phi)=+infinity after extending energy by an
  infimum over bounded majorants. In the usual energy convention the
  unbounded-below value is minus infinity. The chapter uses its
  existing energy conventions and only the cited E1/full-mass
  signatures, without copying the printed sign.
- The raw factorial convention is treated separately in section 3;
  no source-looking raw mass constant is imported.

These exclusions identify auxiliary literal clauses. They do not
claim a refutation of the intended known main statements, a repaired
original general proof, a verifier verdict or a conclusion about any
unacquired later version.

## 6. Research directions and separation from existing open atoms

The inspected version proposes decoupling the upper/lower Bergman
curvature bounds, controlling higher derivatives from diagonal kernels,
and sufficiency of I-good type for partial-kernel measure convergence.
These are attributed questions of the February source. This record
does not assert that no later paper has advanced them, declare them
new active problem atoms or change any current status from literature
silence. The author-hosted and arXiv files currently inspected agree.

Weak convergence of measures on X does not imply convergence of a
pointwise initial-velocity pushforward, empirical spectral laws,
minimizing directions or a compatible family of Chow minimizers.
Curvature bounds require a>0 and do not supply a uniform bound on a
degenerate weak-geodesic slice. The complex polarized construction
does not give a nonprojective quantization, a merely big partial-kernel
theorem or a non-Archimedean Siu division argument. A2–A4 and the
general envelope/Siu boundary retain their existing status.

## 7. Preservation and release boundary

The matching source/build/navigation manifest pins the changed
Chapter 68 subsection, Appendix L entry and one bibliography addition.
All previous formal environments/proofs in those TeX files and all
108 protected Appendix M–N inputs are retained byte for byte. The
42 complete problem status rows, catalogue source/PDF and all prior
frozen manuscript exports/manifests are preserved. No original general
result or independent model receipt is admitted. Four tags continue
the existing in-chapter sequence as 68.23a–68.23d before 68.24.

The final cloud build has 4,298 pages, 314 cited references and 12,642
unique source labels. It has no TeX errors, package/PDF warnings,
unresolved references, rerun requests, missing glyphs or overfull boxes.
Its 954 underfull diagnostics match the previous release. Bibliography
and index processing have no warnings or rejected entries. All 21,574
named destinations, 46,483 internal links, 2,477 outline entries and
numerical index destinations pass their checks. Sixteen actual pages
of this final PDF were inspected, covering the full new subsection,
adjacent arguments, both TOC entries, the provenance entry, reference
and final-page boundaries. The matching review extract contains those
same pages. This is a targeted release review, not a renewed full-book
rereading. The source export is byte-checked against the workspace and
includes the complete 425-input closure; a fresh isolated archive
compilation is not claimed.
