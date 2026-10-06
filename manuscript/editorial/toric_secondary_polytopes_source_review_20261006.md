# Toric instability and secondary polytopes: full source review

**Research-only checkpoint.** The controlling source is Chi Li, Li Sheng
and Yi Yao, *K-unstable Toric Varieties and Secondary Polytopes*,
[arXiv:2610.05179v1](https://arxiv.org/abs/2610.05179v1), submitted
4 October 2026 at 12:41:11 UTC and announced on 6 October.
The baseline is `9830d067f78b1496874594e477db59f4d306bdaa`.
All **49 actual PDF pages**, complete extracted text, proofs, Appendices
A--B, references and final author page were read and displayed in
25 sheets. The arXiv comments advertise 46 pages; actual file pagination
controls this review. No main-theorem admission, complete repaired proof,
canonical-status change or production verification receipt is made here.

The PDF has 843,655 bytes and SHA-256
`63215db3cddf557280dad21555cba0b1eb191130ed618b24c24cd8bd409b1a69`.
The full-reading record is
`source_material/toric_secondary_polytopes_full_review_20261006/full_reading_v1_20261006.json`,
SHA-256 `5e9e3517b0a1114f32a72da018a56ce033835690e6205e75ac7c92845c21f22e`.
The [manifest](toric_secondary_polytopes_source_review_manifest_20261006.json)
embeds the source, reading, exact substitutions and preservation evidence.
Historical acquisition/preparation flags retain their original values.

## Claimed results and their scope

The finite part treats a full-dimensional marked polytope `(Q,A)`,
where `A` is a finite point configuration spanning `Q`. It uses the
normalized GKZ vector whose coordinate at `u` is the sum of the volumes
of incident simplices divided by `(n+1) vol(Q)`. Its coordinates sum to
one. The secondary polytope `Sigma(A)` is the convex hull of these
vectors. Triangulations may omit marked points. The shortest vector
`sigma_A` is the unique Euclidean projection of zero onto `Sigma(A)`;
it is convex on the marked configuration and positive at every node.
The finite algorithms concern this exact compact polytope, rather than
an a priori compact space of all non-Archimedean metrics.

For a lattice polytope `P`, use lattice Lebesgue measure `dx`, lattice
facet measure `d sigma`, volume `V_P`, and
`Sbar = vol(boundary P)/V_P`. The continuum density `Theta` is concave.
Theorem 1 on page 2, proved on pages 26--29, strengthens its known
existence to continuity on the closed polytope, bounded subgradients
of `-Theta`, and a globally concave extension of `Theta`.
The optimal convex function need not be rational piecewise affine.
The source's proposed example on page 25 is numerical evidence, not a
verified explicit optimal density. Its Alexandrov Monge--Ampere-zero
assertion on page 29 uses Li--Zhou with a stated removal of a smoothness
condition; that external proof has not been freshly checked here.

Theorem 50 on pages 29--30 identifies the minimizer of

`Psi_k(eta) = (1/(2 k^n)) sum_{P_k} eta^2
             + (2/k^(n-1)) (sum_{P_k} eta - k^n integral_P eta)`

as `psi_k = 2 V_P k^(n+1) sigma_k^vee - 2 k`.
Theorem 4 on page 5, proved on pages 37--39, gives `psi_k -> -Theta`
in `L^2(P)` and locally uniformly in the interior **for Delzant `P`**,
with convergence of the minimum values and relative Mabuchi values.
It does not assert automatic uniform convergence on the closed polytope.
For a general lattice polytope, the stated closed-polytope convergence
criterion retains the additional `C^0` precompactness assumption.
Corollary 5 detects relative K-instability at sufficiently large levels
in the Delzant setting; no uniform effective threshold is supplied.
The Calabi-flow consequence retains long-time existence as a premise.

## Normalizations and finite proof structure

1. `C(P)` in this source consists of **convex** functions continuous on
   the closed polytope. The larger `C_1` class permits corner singularities
   but requires continuity on the interior and facet interiors, finite
   boundary integral and, when used, finite `L^2` norm.
2. A test `f` gives jumping numbers `chi_f(s_{u,k}) = -k f(u)` on
   page 8. Toric energy is `-V_P^-1 integral_P F_phi^*` on page 12.
   The convex-envelope sign, factor `k`, volume denominator and
   centering must be retained together.
3. Projection away from constants and projection away from all affine
   functions are different. The affine projection of every GKZ vector
   is the same `ell_A`. The valid finite criteria are
   `1/|A| in Sigma(A)` for Chow semistability and
   `ell_A in Sigma(A)` for relative Chow semistability. The shortest
   vector, rather than only its affine projection, determines instability.
4. Lemma 32 on page 20 is the ordinary closest-point inequality
   `<sigma_A, g-sigma_A> >= 0`. The support-function formula then
   identifies the minimizing ray with `sigma_A-1/|A|`; the jumping
   numbers have the opposite sign. The source's Euclidean test-vector
   quotient and normalized spectral quotient differ by the positive
   factor `sqrt(|A|)/k`. Their minimizing rays agree, but their
   numerical minima cannot be identified without this factor.
5. Pages 21--22 prove convexity and positivity of `sigma_A` by its
   convex envelope and the nearest-point inequality. They do not require
   a secondary-polytope vertex to be the minimizer. The relevant
   subdivision comes from the smallest face containing the minimizer.
6. Appendix B on pages 45--46 uses
   `delta(rho) = ||rho||^2 - min_{g in Sigma(A)} <rho,g>`.
   For `rho in Sigma(A)`, `delta >= 0` and
   `||rho-sigma_A|| <= sqrt(2 delta)`. A regular triangulation refining
   the lower subdivision supplies the linear oracle. The iterative
   quadratic program has a numerical stage and a separate exact
   rational certificate. Exact rational arithmetic requires rational
   input coordinates; the general marked-polytope definition allows
   real coordinates. The linked sGKZ program was not downloaded or run.

The continuum functional is
`Psi(eta) = (1/2) integral_P eta^2 + integral_boundary eta`, with raw
integrals. Its unique convex minimizer is `-Theta` by the displayed
variational inequality and Cauchy--Schwarz/Young. The finite functional
uses a different level-dependent center from Yao's `1/|P_k|` convention.
Writing `r_k=|P_k|/(V_P k^n)` and `s_k=2k(r_k-1)`, the relation is
`eta_k-s_k/r_k=psi_k`. The resulting constant correction in Remark 51
is consistent; it must not be silently discarded at finite level.

## Main convergence and Appendix A

The rough lattice bound on pages 30--31 works on general lattice
polytopes. The fine bound on pages 32--34 uses unimodular orthant
coordinates at vertices of a Delzant polytope, barycentric hat
functions and a partition of unity. It produces the `2^-codimension`
node weights and lower-order boundary errors. Its boundary estimate
controls normalized minimizing sequences. Compactness, the affine
moment projection and mixed lattice inner products then identify
every subsequential limit with the unique minimizer of `Psi`.
Norm convergence gives strong `L^2` convergence. The continuous recovery
test `-Theta` uses Theorem 1 and the lattice expansion in Appendix A.
This proof structure was read; the full external chain is not certified.

Remark 60 on pages 39--40 supplies a non-Delzant obstruction to the
**fine estimate**: on `conv((0,0),(1,0),(1,m))`, `m>=4`, the convex
test `max(1-kx_1,0)` has only one nonzero grid value but
`k^2 integral_P phi = m/6`. This is not a counterexample to the main
`L^2` convergence theorem in its Delzant scope, or to a separately
proved singular toric convergence theorem.

Appendix A on pages 40--45 proves the first boundary correction for
convex continuous tests converging uniformly on the closed polytope.
Its fixed-test form has remainder `o(k^(n-1))` in the raw lattice sum.
It does not extend the formula to all continuous tests. A common
continuity modulus handles boundary cells; smooth approximation and
the smooth lattice expansion identify their half-boundary contribution.
Convex symmetric differences control the interior error, and a sum
along lattice chains telescopes to boundary terms. Delzant geometry
is not needed for this Appendix A statement. The pairing diagram on
page 43 is explicitly heuristic and is not used as the proof.

## Selected primary dependencies: 19 actual pages

All selected passages were read and displayed in ten sheets. Neither
dependency paper is claimed read in full.

| Controlling edition | Actual PDF pages | Checked passage |
| --- | --- | --- |
| Székelyhidi, *Optimal test-configurations for toric varieties*, `0709.2687v1`, 17 September 2007, 19:16:33 UTC; 24 actual pages | 1--3, 6--11 | Theorem 4, Propositions 5--6 and 8, Lemma 7, and the complete displayed Section 3 proof of the optimal convex direction and its variational characterization |
| Tate, *Asymptotic Euler--Maclaurin formula over lattice polytopes*, `0908.3073v5`, 1 May 2010, 02:41:35 UTC; 35 actual pages | 1--4, 26--29, 32--33 | Smooth lattice expansion, rational-cone reduction, Theorem 5.1 and its displayed proof, and the complete displayed proof of Corollary 5.5's half-boundary coefficient |

The selected-reading record is
`source_material/toric_secondary_polytopes_dependencies_20261006/selected_reading_v1_20261006.json`,
SHA-256 `2f420581931249e293759b0253b64861eeb6b3a6c18d0410a60dfff9fc0842b4`.
The exact [Székelyhidi](https://arxiv.org/pdf/0709.2687v1) and
[Tate](https://arxiv.org/pdf/0908.3073v5) PDFs control the locators.
Tate's Corollary 5.6 continues on unselected page 34; its full proof
is not claimed read. Donaldson's compactness proof, the unimodular-cone
expansion and Berline--Vergne antecedents remain outside this fresh
selected reading. Tate states Corollary 5.5 for Delzant polytopes;
Theorem 5.1 has the broader smooth lattice-polytope signature.

The preceding Yao v1 reading is reused from the
[maximal-destabilizer audit](maximal_destabilizer_integration_audit_20261005.md):
all 43 extracted pages were read there, with fourteen selected primary
PDF pages and seven dependency PDF pages displayed. It is not described
as a fresh complete PDF reading. The BJ weighted YTD preprint was
rechecked against official version metadata and its cached first page:
the full title *On the Yau--Tian--Donaldson conjecture for weighted cscK
metrics* agrees with the existing bibliography; a shortened running
header does not require a title change.

## Literal formula defects: exact substitutions

These diagnostics concern printed assertions in v1. They do not assert
that a corrected main theorem is false or supply an independently
verified new theorem. Exact `Fraction` arithmetic reproduces the values.

1. **Theorem 29, page 19: an extra equivalence is false.** Let
   `Q=[-1,1]`, `A={-1,-1/10,0,1/10,1}` and `f(x)=|x|`.
   Symmetry gives `ell_A=1/5`: its total mass is one and its first
   moment is the continuous barycenter zero. But the discrete average
   of `f` is `11/25`, while its volume-normalized integral is `1/2`.
   Thus the printed Chow weight is `-3/50`. The affine condition
   `ell_A=1/|A|` is not sufficient. The valid membership condition
   `1/|A| in Sigma(A)` and Theorem 2's correct shortest-vector criterion
   are distinct from this faulty extra clause. This marked configuration
   need not be the full grid `P_k` to fall within Theorem 29(1).
2. **Proposition 55, pages 34--35: the level qualifier is missing.**
   For `P=[0,1]`, `k=1`, `x_0=1/2` and normalized
   `phi(x)=|x-1/2|`, both node values equal `1/2` and their affine
   projection is constant `1/2`. The printed lattice norm squared is
   `1/2` and the affine residual norm is zero. Therefore no constant
   can give the asserted inequality at this level. The displayed
   contradiction proof uses `k -> infinity`; a sufficiently-large-level
   qualifier is required. This finite-level defect does not refute
   the asymptotic main convergence assertion.
3. **Page 12: the supernorm expansion omits its remainder.** For
   `P=[0,1]`, `f(x)=x^4` and `k=2`, the actual normalized energy is
   `-17/48`, while the two printed terms give `-7/20`, differing by
   `-1/240`. The asymptotic display must retain `o(1/k)` rather than
   serve as an exact finite-level identity.

The diagnostic record is
`source_material/toric_secondary_polytopes_full_review_20261006/literal_formula_diagnostics_v1_20261006.json`,
SHA-256 `b5b9aab92085bfdc84a7fd0a9b4ef20e43ed2d7ff382b81c2bf5950052b3d042`.

## Preservation and next directions

Only README and the research programme change among the 5,032 tracked
baseline files; the other 5,030 retain their bytes. All 425 active inputs,
108 protected inputs, 56 prior frozen manifests (52 integration and four
source-only records), 112 exported artifacts, the checked 4,386-page
book, all generated book files and the open native catalogue retain
their bytes. Inventory and whitespace gates pass. No unchanged-book
rebuild, fresh book-page review, native compilation or archive compilation
is claimed. All 42 canonical problem statuses and the general Siu/closure
boundary retain their scope.

The next book candidate is the finite closest-point argument with its
correct membership criterion, separate affine projection and exact gap
certificate. The continuum regularity and convergence admission needs
a scoped review of Donaldson compactness and the remaining primary
dependencies; the Alexandrov assertion needs Li--Zhou. Piecewise-affinity,
non-Delzant quantization and effective instability thresholds are source
research directions, not newly solved canonical problems. Recent Hermitian
Monge--Ampere and Hessian papers `2610.06473v1` and `2610.06719v1` have
only been identified from primary metadata and remain unread candidates.
