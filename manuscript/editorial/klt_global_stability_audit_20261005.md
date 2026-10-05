# Global klt continuity and big-class stability — 5 October 2026

This checkpoint admits identified external results in Chapter 68 and Appendix L.
It imports the global adapted-measure continuity, analytic/divisorial alpha and
delta identities, and strict subcritical existence from Darvas–Zhang,
arXiv:2608.23505v2, revised 13 September 2026. It does not admit an original
result or claim an independent production-model receipt. The repository's
verification protocol expressly separates such imports from original results.

## Controlling primary files and reading scope

- Darvas–Zhang klt v2: 33 pages, 474658 bytes, SHA-256
  `c79f474903068d25d1ca3092f1afb27ff9f6f069333b61bfc2a705f3c0b02d7a`.
  All 1754 extracted Python-split lines and all 33 actual PDF pages were read.
  The original acquisition record is immutable; current reading is recorded
  separately in the ignored source cache.
- Darvas–Zhang twisted KE v4, arXiv:2208.08324v4, revised 28 April 2024:
  35 pages, SHA-256
  `9b99c2311d7302d80766297e6f8602f36ddde721947f41d0789fa7fe6a983602`.
  All 2146 extracted lines, including references, were read for this checkpoint.
  Actual pages 4, 5, 7, 8, 9, 16–24 and 27 were inspected (15 pages).
  The earlier selected-reading record from the big-ray checkpoint is unchanged.
  Publication metadata recorded by arXiv does not identify acquired publisher bytes.
- BEGZ, arXiv:0812.3674v2, revised 9 September 2010: reused primary PDF,
  actual pages 3, 40 and 43, with selected extracted ranges 68–115,
  1945–2010 and 2107–2169. This is not a new full-paper reading.
  The version has its own citation key; published `BEGZ10` is not silently
  used to authenticate a different version's numbered locator.

The actual-page manifests are `/tmp/darvas_zhang_klt_primary_20261005/manifest.json`,
`/tmp/klt_dependencies_selected_20261005/manifest.json`, and
`/tmp/klt_smooth_variation_selected_20261005/manifest.json`.
The second manifest also records 17 selected pages of a local dependency
that is not admitted in this checkpoint. There are 68 actual primary pages
in total, including those research-only pages; global admitted dependencies
account for 51 of these pages. Flags record actual inspection, not rendering alone.

## Exact signatures and source locators

1. Klt v2 Theorem 1.1, proved using Proposition 5.2: connected normal analytic
   klt real pair, effective boundary, real-Cartier log canonical divisor,
   smooth formal metric and its adapted measure, pure dimension n >= 1.
   PSH convergence is local L1 for embedded Kähler volume. Integrability at
   lambda on a neighborhood of K implies strict openness and exponential
   L1 continuity on a possibly smaller neighborhood. The theorem retains
   the strict larger exponent t < c_mu,K[u].
2. Klt v2 Theorems 1.2 and 1.3: compact normal Kähler klt pair, big smooth
   (1,1) representative, quasi-psh twist with integrable exponential and
   probability-normalized twisted measure. Alpha is uniform over sup-zero
   PSH potentials; analytic delta is uniform over E1 after subtracting the
   volume-normalized Monge–Ampère energy. Divisorial numerators are
   A_X,Delta(E) minus the twist's generic Lelong number. Denominators are
   the big threshold tau and expected order S = integral(volume)/V.
3. Smooth DZ v4 Theorems 1.4/4.1 and 1.5/4.7: sublinear finite-energy
   subgeodesic rays, tame probability measure, lambda below the complex
   singularity exponent of V_theta. The radial Ding formula is a liminf,
   with the Legendre integrability threshold and radial energy. Section 7.2
   of klt v2 transfers this to the adapted measure on a resolution. No
   convexity of the Ding functional is asserted or assumed by this formula.
4. Klt v2 Proposition 7.2 and Theorem 7.3: endpoint segments with lengths
   tending to infinity, fixed background curvature, local product L1 limit,
   Legendre transforms at fixed tau < 0. If Ding is unbounded below at
   lambda < delta, the exponential integrals of the limit dual are infinite
   for -1 < tau < 0. Maximalization gives a nontrivial geodesic ray. Its
   negative slopes at eta in (lambda, delta) contradict the known radial
   semistability threshold. The positive increment is retained; the chapter
   does not use a literal reading allowing negative epsilon.
5. Klt v2 Lemma 7.4: eta > lambda > 0 and
   0 < a < min(lambda, alpha). The coefficients in the Hölder inequality
   have positive denominators and the energy coefficient has negative sign.
   Sup-zero finite-energy potentials satisfy -I = d1(V_theta,u). Boundedness
   below at eta < delta therefore gives coercivity at lambda.
6. Klt v2 Corollary 7.5 and smooth DZ v4 Proposition 5.2: coercive Ding,
   L1 continuity of its exponential part, and finite-energy variational
   minimization. Continuous obstacle variations give MA(u)/V equal to the
   normalized exponential probability measure. Adding
   (log integral(exp(-lambda u) dmu_psi) - log V)/lambda to u gives the
   unnormalized equation. No additive shift changes the current.
7. BEGZ v2 Theorem B/4.1: full mass in a big class on a smooth compact
   Kähler manifold, density in L^(1+epsilon), minimal singularities. This
   estimate is applied on the resolution as in the new klt source. Its
   capacity iteration is checked on actual page 43; boundedness on all of
   X is not substituted for minimal singularities in a merely big class.

## Why resolution alone does not suffice

The pullback of an adapted measure has SNC discrepancy factors with a_i > -1.
The local proof obtains bounds by smooth regular slices, L2 extension,
quantitative division and normal holomorphic estimates. General
exp(chi-psi) weights on a resolution do not enjoy this continuity.
The use of fixed curvature bounds for u + psi/lambda is essential when
applying the local theorem to quasi-psh potentials. No unrestricted
quasi-psh sequence with varying lower curvature is imported.

The uniform larger-exponent bound produces uniform integrability at lambda.
Local L1 convergence for Kähler volume gives convergence in measure for the
absolutely continuous adapted measure; Vitali then supplies exponential L1
convergence. The theorem's assumption is not adapted-measure L1 convergence
of the potentials themselves.

## Normalization and proof boundaries

The klt and smooth DZ sources use ddc = i partial partial-bar / (2pi), as
in the book. Generic divisorial Lelong coefficients of log|z|^2 equal one.
Energy is divided by V, the twist measure has unit mass, and MA is explicitly
nonpluripolar in the global equation. No factor-two change of additive
potentials is needed here, unlike the previous Xiao construction.

The missing factor two in the smooth v4 rooftop-distance display on page 7
is excluded. The book uses I(u)+I(v)-2I(P(u,v)). The unrestricted increasing
quasi-psh wording in Theorem 2.2 is not used beyond the fixed-curvature
applications. The endpoint in Lemma 3.12 can be identically minus infinity;
its literal endpoint positivity argument is not copied. Proposition 5.2's
proof has D^1/D^lambda and equation-number slips; its displayed variational
identity, with the correct lambda and normalized mass, controls the chapter.
The auxiliary Proposition 3.6 background-form slip and extra thermodynamic
argument of Proposition 5.4 are outside the present proof route.

The conclusions are existence for 0 < lambda < delta and minimal
singularities. Delta > 1 is sufficient at lambda = 1. The chapter does not
assert endpoint existence, necessity, uniqueness, an all-category YTD
biconditional, spectral pushforward, or convergence of minimizing directions.
The general non-Archimedean Siu and envelope proof boundaries stay explicit.

## Local dependency audit retained outside active TeX

The klt paper's Section 8 and Corollary 1.7 concern an isolated log terminal
singularity, a strongly pseudoconvex neighborhood with rK trivial, a flat
adapted probability measure and ordinary Cegrell MA retaining polar mass.
They are not part of this global import.

Guedj–Trusiani's arXiv:2306.07900v1 (39 pages; SHA-256
`66404e8705acbbaac799ebe4495e55aa18b74dd5f4fc51b63415e3fef63d9f87`)
was compared by a selected introduction reading only. It does not contain
the published Proposition 5.8. A direct publisher download returned HTTP 403;
the institutional archived published-format file was acquired instead from
https://research.chalmers.se/publication/547970/file/547970_Fulltext.pdf.
It has 44 PDF pages including two institutional cover pages, 947555 bytes,
SHA-256 `82521b158a23b0a0e1f8b782383520a9206e9a78d2a170af43174abdd3dcf472`.
Printed metadata are Compositio Mathematica 161 (2025), 714–755,
DOI 10.1112/S0010437X24007619, with an appendix by Boucksom.
No byte comparison with an unacquired publisher download is claimed.

Selected published text ranges and 17 actual pages were read, including
Definition 2.6, Proposition 2.7, Proposition 3.14, Theorem 4.5, Theorem 5.1,
Definition 5.5, Proposition 5.8, Lemma 5.9, the existence proof and Appendix A.
This is not a claim to have read all 2752 extracted lines. The klt source's
Corollary 1.7 cites “Theorems C and 3.5”; the published upper bound is
Theorem 4.5, while published 3.5 is an energy lemma. In the old arXiv edition
Theorem 3.5 is an upper bound. These editions must not be mixed.

Further work is needed to audit Lemma 5.9's transition from the asymptotic
order of one valuation ideal to a comparison with the full PSH singularity
across other divisors. The single order formula (5.9), by itself, does not
supply that implication. This is a proof-dependency question, not a
counterexample to Proposition 5.8. Appendix A supplies a separate nef
b-divisor comparison route and a locally-bounded-away-from-p formula; its
literal log-sum generator normalization must also be reconciled with the
main text's log-sum-of-squares convention before copying a formula.
The printed root/ideal infimum in Proposition 5.8's proof requires
volhat^(1/n) = inf_I lct(I) e(I)^(1/n), rather than the raw unrooted product.
The appendix's complex-current Siu decomposition is distinct from BJ22's
non-Archimedean changing-coefficient argument. No general BJ repair follows.

A local integration must retain the larger-domain obstacle extension in the
klt proof: closure(Omega) must be compactly contained in Omega-prime before
applying continuity. A sharp critical MT exponent is not a nonexistence
theorem for KE solutions above it. These checks remain future work.

## Preservation and release verification

Only Chapter 68 and Appendix L change among the 425 active TeX inputs.
Their existing formal environments and proofs are byte preserved; no new
formal result environment is created. Seven displayed equation tags are
68.23e–68.23k; nine labels are added across the chapter and provenance.
Two version-specific bibliography entries are added; the existing smooth
v4 note now covers all its numbered locators, without changing source version.
All 108 protected inputs, 42 complete inventory statuses, the native
catalogue source/PDF, and earlier frozen manifests/releases are preserved.

Fresh compilation, source/reference, inventory, bibliography, index and
PDF-navigation checks and actual release-page inspections are recorded in
the matching integration manifest, source closure and artifact record.
No fresh isolated archive compilation or whole-book rereading is claimed
by this scoped integration checkpoint. Work continues with the unresolved
local dependency checks and related primary literature.
