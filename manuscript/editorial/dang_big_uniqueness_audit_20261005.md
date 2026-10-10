# Big-class stability, small-parameter uniqueness and local continuity

This checkpoint continues the cloud-only book task from `b780e43` on
`work`. It adds an identified September source to Chapter 68 and a
version-specific entry to Appendix L. The native open-problem catalogue
is unchanged. The global klt release and all older frozen records remain
immutable.

## Mathematical admission

The principal source is Dang–Zhang–Zhou, *Uniqueness and Stability of
Monge–Ampère Potentials in Big Cohomology Classes*,
[arXiv:2609.00810v1](https://arxiv.org/abs/2609.00810v1), submitted
1 September 2026, manuscript dated 2 September 2026. Its 21-page PDF has
SHA-256 `043857474c003da0d68aa8d0c666256aa06b415de8bbd371ce11a51cbb9e4ff9`.
The full 1,265-line Python `splitlines` extraction, including references,
was read, and all 21 actual PDF pages were inspected. Acquisition flags
remain their historical snapshots; mutable reading progress records the
subsequent reading. No publisher identity is claimed for this preprint.

The chapter admits the following fixed-geometry smooth complex results.

- Theorem 3.2, restricted to power `L^q` densities, controls the bounded
  difference of two supremum-normalized minimally singular potentials by
  the `L^(nq)` norm of the difference of the density roots. The right-hand
  densities have unit mass and a common `L^q` bound; `q>1`.
- The sufficiently small parameter conclusion of Theorem 3.3 is recovered
  from this estimate, uniform Skoda integrability and ordinary full-mass
  solvability. The chapter displays the two direct formal calculations
  below. It makes no original-result or priority claim.
- Theorem D of Demailly–Dinew–Guedj–Pham–Kołodziej–Zeriahi supplies local
  Hölder regularity on the ample locus once the actual solution density
  has an `L^q` bound. Its domain includes arbitrary big classes.
- Theorem 4.1 and the proof of Theorem 1.2 supply logarithmic continuity
  for `L^1(log L)^a`, `a>n`, with the explicit hypothesis
  `V_theta - M_0 <= phi <= V_theta` retained. The entropy-only deduction
  of minimal singularities through an unacquired auxiliary preprint is
  outside this import.

The ambient space is a connected smooth compact Kähler manifold of
dimension `n>=1`; the class is big with positive volume. A fixed smooth
probability volume, fixed geometry and nonnegative probability densities
are used. Zeros of a density are allowed. General normal klt spaces,
zero volume, noncompact domains, all positive parameters and global
boundedness in a merely big class are not asserted.

## Two proof adjustments

The actual formulas on pages 11–12 were checked, not inferred from the
abstract or extraction alone.

1. **Weighted contraction.** The printed uniqueness proof takes a global
   supremum of exponential differences. A minimal potential can be
   unbounded in a big class, so that intermediate quantity need not be
   finite. Instead fix `1<q<p`, put `r'=p/(p-q)`, and impose
   `q lambda r' <= alpha`, where normalized psh potentials have a uniform
   `exp(-alpha w)` integral. Hölder gives a uniform `L^q` bound for
   `exp(-lambda w)F`. For supremum-zero potentials, their normalizing
   integrals `Z_w` are at least one. If their finite comparison norm is
   `S`, then `|log Z_u - log Z_v| <= lambda S` exactly. An almost-everywhere
   exponential difference estimate inside `L^(nq)` gives
   `S <= (4 C_q B^(1/n)/n) lambda S`. All constants are uniform over the
   two solutions. A strict smaller parameter bound forces `S=0`, and
   mass fixes the remaining additive constant. Pole values are never
   subtracted or used in a pointwise supremum of exponentials.
2. **Convex normalization for existence.** The printed fixed-point
   paragraph calls the supremum-zero psh slice convex. In general it is
   not: on a compact manifold take a nonconstant smooth function `h` with
   range `[0,1]` and a Kähler form; for sufficiently small positive `e`,
   `-e h` and `-e(1-h)` are psh relative to that form and each has supremum
   zero, but their midpoint is the constant `-e/2`. The chapter uses the
   integral-zero psh slice, which is compact and convex in `L^1` and has
   uniformly bounded suprema. Choose `1<q<q_1<p` and a stricter parameter
   bound for uniform `L^(q_1)` densities. Normalizing integrals have a
   uniform positive lower bound. Higher integrability makes the
   probability densities continuous in `L^q` under `L^1` convergence of
   the inputs. Solve the ordinary normalized full-mass equation using
   BEGZ Theorems A–B, then normalize its output by integral. Theorem 3.2
   and `|a^(1/n)-b^(1/n)|^n <= |a-b|` give continuity of this self-map.
   Schauder gives a fixed point; an explicit additive shift solves the
   negative-exponent equation. The image has minimal singularities.

These are direct formal consequences of checked imported inputs under
the repository's Rethlas protocol, not original general results promoted
without a production receipt. No independent model call or receipt is
claimed. Neither adjustment is a counterexample to Theorem 3.3.

The auxiliary density in the proof of Theorem 3.1 on actual page 8 is
printed with an unpowered root difference. That auxiliary proof is
excluded: the chapter uses Theorem 3.2 and ordinary full-mass solvability
for both existence and uniqueness. In the latter theorem's extrapolated
envelope, the obstacle is `V_theta` plus a bounded function and thus has
a psh minorant. Contact comparison ensures absolute continuity before
using its density; full mass and the mixed inequality give the required
contact point outside the polar set. The source's broad Orlicz theorem
is not imported wholesale.

## Normalizations and dependency checks

The principal source uses `ddc_s=i partial partialbar`; the book uses
`ddc_b=i partial partialbar/(2 pi)`. If the book's volume is `V`, put
`c=V^(-1/n)`, `Theta=c theta`, `U=c u/(2 pi)`. Then the source current is
`c` times the book current and has volume one; its Monge–Ampère measure
is exactly the book's mass-normalized measure. The parameter becomes
`lambda_s=2 pi V^(1/n) lambda_b`. Difference norms and stability constants
are scaled accordingly. A constant scaling of the reference Kähler
volume realizes the smooth probability volume; the distance scaling
only changes constants for small positive distances. No class-varying
uniformity or identification of parameter units is claimed.

Four additional primary files were acquired and read **selectively**.
Their complete texts were not read in this checkpoint.

- Darvas–Di Nezza–Lu, arXiv:2303.11584v2, revised 3 October 2023:
  Theorem 2.7, Lemma 2.9 and Lemma 3.5, actual pages 14–17 and 23.
  SHA-256 `e72213a3154bff5cab1a41f9651568201f8ead79beb662925884e58994c19fd0`.
  This is an arXiv version, separate from the existing published survey.
- Demailly et al., JEMS 16 (2014), 619–647, DOI 10.4171/JEMS/442:
  publisher PDF, Theorem D and Section 6, actual pages 4 and 23–25
  (printed 622 and 641–643).
  SHA-256 `f5079b46b1acf68362ef61fa49f08118701fef1b738ab4e25dfd9de500e10257`.
- Lu–Phung–Tô, AIF 71 (2021), 2019–2045, DOI 10.5802/aif.3436:
  publisher PDF, Lemma 4.4, actual pages 23–25 (printed 2040–2042).
  SHA-256 `e6c1b8836680c79973176b7bac3ce78e8d28a42692ebe86cc395a93f7f4f66eb`.
  This lemma treats a global bounded Hermitian power modulus.
- Zeriahi, arXiv:2007.08399v1, submitted 16 July 2020:
  condition (3.1), Lemma 3.3 and its proof, actual pages 9–12.
  SHA-256 `8c55994b7b24f944cb5070669e2af5e7f2d995367b115934e30281d65e4ab16f`.
  The interior lemma applies to a logarithmic modulus after restricting
  to small scales; no regularity at a domain boundary is inferred.

The new dependency contact sheet manifest records 16 actual page views;
together with the principal paper this gives 37 fresh primary page views.
The already acquired BEGZ v2 Theorems A–B on actual page 3 were reused
from the preceding global check; no fresh complete BEGZ reading or new
actual page view is claimed here.

In the logarithmic regularization argument, shifting the analytic
strictly positive barrier down ensures that it lies below all relevant
regularized obstacles. Its curvature does not change. This justifies
the positive-part `L^1` comparison printed on actual page 16. The
average-to-oscillation step uses nested compact subsets inside the ample
locus. Small positive distances avoid the singular expressions at
distance one. A logarithmic modulus is not promoted to a power modulus;
the Hölder statement comes from the separate `L^q` theorem.

## Preserved research boundaries

No forty-two-atom status is changed. The Boucksom–Jonsson Theorem 6.21
proof issue remains a proof-boundary statement with critical division
explicitly additional; no theorem counterexample or general repair is
claimed. Normal/non-nef envelope closure, initial spectral pushforward,
the quantization assumptions A2–A4 and minimizing-direction convergence
retain their existing status. The separate Guedj–Trusiani local Cegrell
dependency audit remains pending, including its single-valuation to full
singularity comparison and logarithmic generator normalization.

The double-logarithmic result, Ricci convention, entropy-only minimal
singularity estimate and all-parameter uniqueness are outside this
checkpoint. Frozen source caches and prior published checkpoint records
are not reinterpreted as full readings or independent receipts.

## Final cloud verification and release

The matching final build has 4,311 pages, 20,053,398 bytes and SHA-256
`a3caf7fa81fe7088ee6b522c620fedbb8af62fa21d76ee7335bac7df91b1dea1`.
Its 425-input reference closure has 12,671 unique labels and 326 cited
keys out of 621 bibliography keys. Bibliography, index and navigation
checks pass; there are no TeX errors, unresolved references, missing
glyphs, package/PDF warnings, rerun requests or overfull boxes. Underfull
boxes remain 954. All 108 protected inputs and the 423 unedited active
TeX inputs are byte preserved. The inventory check passes with 42 atoms
in 12 families and tiers 0/3/7/15/17.

Eighteen matching final-book pages were checked, including every new
chapter/provenance page, contents entries, an adjacent appendix boundary,
the index opening and all five new bibliography entries. Sixteen final
page rasters are byte identical to the previously actually displayed
and inspected sheets; the changed two-page sheet was displayed again
after protecting the proper name “Hölder” from bibliography lowercasing.
The manifest distinguishes image reuse from a new display. The matching
18-page review has SHA-256
`d51fc9366032e5e3fbd2068a743178738fd27bfd7eb36abd8d87089b88a69a68`.
This is selected release verification, not another complete book reading.

The first build's long inline norm pair was replaced by equivalent prose
to remove one overfull line. The second build's new bibliography title
was corrected after its actual page inspection; the mathematical text
did not change. Historical diagnostic outputs are not the final release.
The new full PDF, matching review and source archive are recorded in
the new integration manifest and artifact record. The archive retains
all 425 active inputs and verifies every archived byte against the
workspace, without claiming an isolated archive compilation. Earlier
frozen manifests and exported artifacts remain byte preserved.

Two follow-up primary files have been acquired with versions checked on
arXiv: Dang–Zhang–Zhou arXiv:2608.19600v1 and Lu–Phung
arXiv:2501.18281v1. Only the first 230 extracted lines of the former
have been read; the latter has not yet been read. Neither is imported
in this checkpoint. The uniform-estimate proof, energy exponents and
constant dependencies are the next reading targets.
