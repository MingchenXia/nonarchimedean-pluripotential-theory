# P08.1 global smooth-psh counterexample: integration audit — 25 September 2026

## Baseline and scope

Baseline commit: `9ae9b25f9b465ba25c412eb0e7a815ac57e42eb9` on `main`, synchronized with
the designated GitHub origin. The author supplied the three-page PDF
`global-smooth-psh-counterexample.pdf`, SHA-256
`682eec5c367f9cd5d81427173a540b8c87b844ca7803c776344bd21eb117944a`.
The original is preserved byte for byte under
`manuscript/author_sources_20260925/`.

The manuscript answers the literal first question of CLD Remark 17.8.10:
a continuous metric with locally ordinary CLD-psh weights on a projective
non-Archimedean variety need not be a uniform limit of globally ordinary
smooth psh metrics. Chapter 17 adapts the complete proof. Chapter 72 retains
the old semantic label on a historical remark and retires P08.1. The active
inventory changes from 43 atoms in 13 formal environments, tiers
`(0,3,8,15,17)`, to **42 atoms in 12 environments**, tiers
**`(0,3,7,15,17)`**.

This result does not concern ample-class envelope continuity. It is stronger
than the existing Tate example, which separates smooth global psh
approximation from rational-model approximation but already has a smooth
psh metric. It is independent of the P08.2 formal-twistor counterexample to
the separate parlinear/global-dpsh extension.

## Proof audit

The example uses the constant elliptic curve `y^2=x^3-x` over `C((t))`, a
transcendental point `P`, and the non-torsion degree-zero bundle `O(P-O)`.
The constant smooth model supplies a nef integral model metric. Its weight
in the canonical rational frame is `r_P` on the residual `P`-disc, `-r_O`
on the residual `O`-disc and zero in every other residual direction.

For an ordinary smooth function near the good-reduction point, the local
moment presentation and reduction of analytic units show that its outgoing
slope divisor is a finite real linear combination of principal divisors.
For a smooth psh metric on `O(D)`, positivity tested on a cutoff inside each
residual disc gives coefficientwise `a_R <= d_R`. Both slope divisors have
degree zero, so equality holds. The integral divisor `D` therefore lies in
the real span of finitely many integral principal divisors. Row reduction
over the rationals gives rational coefficients and clearing denominators
makes a positive multiple of `D` principal. Thus every such degree-zero
class is torsion.

Conversely, a torsion divisor class has a globally smooth pluriharmonic
metric by taking a rational root of the absolute value of a principal
function. The chosen point `P` is non-torsion because all torsion points of
the elliptic curve have algebraic coordinates while its x-coordinate is
transcendental.

Local pshness at the good-reduction point is constructive. For
`R_n=(n+1)P`, choose `f_n` with divisor
`(n+1)P-nO-R_n`. The functions `-(1/n)log|f_n|` are smoothed only inside
the residual `R_n`-disc by a fixed convex cutoff. Their Hessians are
nonnegative, and on a fixed neighborhood their sup-norm error is at most
`max(a,2)/n`. This proves ordinary local smooth-psh approximation without
producing a single global smooth psh metric on the bundle.

The first review checked every sign in the three residual directions, the
compact support of the cutoff, the integration-by-parts limit, degree-zero
coefficient comparison, rational row reduction, the elliptic divisor
identity and the uniform error. The second review reread the adapted proof
against the preserved PDF and rechecked its scope against the existing
positive-degree and Tate results.

## Primary-source audit and correction

- [Chambert--Loir--Ducros, revision of 25 July 2025](https://webusers.imj-prg.fr/~antoine.chambert-loir/publications/papers/fdceb-20250725.pdf):
  Definition 8.1.7 and Propositions 8.1.9 and 8.1.11 give the continuous psh
  uniform-closure statements; Lemma 8.1.10 supplies a decreasing subsequence
  after vanishing constant shifts; Proposition 8.3.1(a) identifies psh
  functions with positive Hessian currents in the required direction;
  Proposition 15.1.1(b) and Corollary 15.1.2 give ordinary local moment
  presentations; Theorem 15.7.1 supplies the analytic tropical structure;
  Definitions 17.8.1 and 17.8.5 and Remark 17.8.10 give the metric notions
  and the literal question. The exact PDF pages were inspected directly.
- The supplied citation to Stacks Tag 0DSV is incorrect: that tag is an
  example about a smooth positive-dimensional automorphism group, not the
  degree-one Picard identification of a genus-one curve. The book adaptation
  does not use the tag. Riemann--Roch and the chord-and-tangent divisor law
  give the required identification directly.

No authorship, priority or publication status absent from the supplied PDF
is invented. The supplied original, the local integration review and any
model-verifier response have separate provenance.

## Repository cleanup

At the author's instruction, the tracked root directory
`author_source_repairs/` is removed. It contained four repair-working files
for the partial-Okounkov-body source. The historical receipt retains its
dated locator, and the frozen 24 August source archive is not rewritten.
Git history continues to preserve the removed directory.

## Validation

The frozen statement, proof, primary-source extracts and review scope were
sent to the local Rethlas endpoint with `gpt-6-astra` at `xhigh`. The
service-allocated run is `20260925T000718Z_60d573d3ec8e`. Its HTTP 200
response returns `correct`, with zero critical errors and zero gaps; the
sequential run recorded 17 statement checks and 12 reference checks. The
exact request, response, safe headers, receipt and checksum ledger are
preserved with the packet. The request and response SHA-256 values are
`4aae29650932e850dca3aba6166dd34b6eaf06a4043efca0ce45783078da3bb7`
and
`410e27b751324b85d5ecd22729213070c152878578448966e699bae050929e9b`.

The final source checks cover 397 build inputs and 11,828 unique labels,
with no missing input, multiply defined label, dangling reference or
per-file structural failure. The inventory checker passes with 42 active
atoms in 12 formal environments and tiers `(0,3,7,15,17)`. Its six unit
tests pass. The scoped Mingchen audit of the new fragment has zero errors
and one reviewed warning that the exact 25 July 2025 CLD revision is still
represented by its preprint entry.

The full build produces `book.pdf` with 4,066 pages and 19,360,315 bytes,
SHA-256
`f4ee97a51249628f44b940258218bce3ea2f19dada6bf533c8aedb04885fa7be`.
The final log has no unresolved reference or citation, rerun request,
horizontal overflow or vertical overflow. The 13 inherited duplicate
Chapter 70 equation destinations are unchanged. Physical PDF pages
1128--1135, 3836--3839, 4043--4045 and 4063--4065 were rendered and
visually inspected, covering the Chapter 17 proof, Chapter 72 retirement,
provenance entry and bibliography record; no clipping, collision or broken
line was found.

The source archive checksum passes, and its preserved PDF has the same
SHA-256 as the supplied file in `Downloads`. `git diff --check`, the
inventory check, reference check, unit tests and scoped style audit were
rerun after the final textual edits.
