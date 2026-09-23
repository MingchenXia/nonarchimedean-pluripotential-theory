# Chapter 59 log discrepancy and its normalization

Date: 23 September 2026.
Baseline: `c52fda4eb4f29114f509b67e83815f5f85f56e98`.
Scope: Section 59.5 only. The standing X is a connected compact Kahler
manifold, and the existing cofinal system consists of projective snc models.

## Mathematical reconstruction

The old cone formula omitted the requirement that a log-smooth boundary
contain the exceptional locus. The new local logarithmic-Jacobian lemma
proves 1+ord_G(K_Z/Y) >= ord_G(mu*B): a pulled-back logarithmic top form
has at most one surviving du/u factor. With the required boundary, the
relative canonical divisor is supported on it. Stratum blowups preserve
K+B, giving the rational monomial formula. The Jacobian inequality gives
the divisorial retraction bound. Ideal-valued continuity of lifts, the
finite stratum-ideal embedding and rational approximation then prove the
real formula, its independence and monotonicity between presentations.
The zero cone is included. The proof uses analytic ideal characters,
not an unjustified global algebraic function field.

An explicit counterexample explains the missing hypothesis: after blowing
up the origin of P2, the strict transforms of y=0 and y=x^2 are transverse,
but omit the exceptional divisor. Their rays have discrepancy 1 each,
whereas the (1,1) valuation at their intersection has discrepancy 3.

For a central fiber sum b_i E_i, the affine model discrepancy is
sum (1+k_i)w_i, with value (1+k_i)/b_i at its normalized vertex. Distinct
normalized vertical primes are separated on a common model by the PL
function of one prime; this establishes independence of the prescription
under restriction. The Jacobian lemma gives 1+k_i >= b_i, so every model
function is at least 1. Canonical transitivity computes the nonnegative
difference on a domination explicitly. Common-model comparison recovers
divisorial values, and rational density on each fixed complex proves
A_tot composed with i_X = a_X, including irrational points. The supremum
is lower semicontinuous.

Reduced discrepancy is A_tot-1. Its model restrictions are the nonnegative
continuous PL functions associated to K_model/T+B_red-model_0; they increase
to the reduced function. This supplies the precise identity already used
in Chapters 60 and 61. Those chapters are unchanged. Gauss comparison is
proved for every positive rational multiple r ord_F, on the correct
domains: A_T(sigma(v))=A_X(v)+1 and A_X^NA(v)=A_X(v). The trivial
valuation and dim X=0 are explicit.

The P1 example with weights (2,3)/3 has central multiplicity 3, relative
canonical coefficient 4, total discrepancy 5/3 and reduced discrepancy
2/3. Repeated point blowups principalize I_p+(t^N), with last vertex
N ord_p; their ideal values locate the retraction of the character
supported at p at that vertex. Its reduced discrepancy is consequently
infinite. No assertion about every proper-support character is inferred.
The entropy warning uses addition by 1, never subtraction of two infinite
integrals, to distinguish the total and reduced conventions.

## Exact source checks

- Jonsson--Mustata, published article at
  [Numdam](https://www.numdam.org/item/10.5802/aif.2746.pdf):
  Lemma 1.5(i), pp. 2156--2157; Definition 3.2, p. 2168;
  Proposition 5.1 and the inequality in Lemma 5.3, pp. 2179--2181.
  PDF physical pages 13, 25, 36, 37 and 38 were visually checked;
  physical page 14 was read as text. PDF SHA-256:
  `b0360dbfeb5b19601500e3ed03e8b186f4ac84b6c771a2a300fe25efa0d5fb57`.
- Mesquita-Piccione, exact
  [arXiv:2409.06221v2](https://arxiv.org/html/2409.06221v2):
  Section 3.2, equations (3.2.3)--(3.2.4), Remark 3.2.1, pp. 31--32;
  Definition 6.2.1, p. 51. All three PDF pages were visually checked.
  SHA-256 `9eb2ea7686a5962ebc11c5eacd23b0cb3dcb081e27ac48292933f291fc82cb23`.
  Fresh publisher-access attempts failed. These locators belong to the
  exact author version, not to a newly checked published MP24 PDF.
- Mesquita-Piccione--Witt Nystrom, exact
  [arXiv:2509.09442v1](https://arxiv.org/html/2509.09442v1),
  Section 2.4.1 and Definition 2.4.1: checked in HTML for the normalized
  total discrepancy and entropy integral of A_tot-1. No PDF review is claimed.

## Second pass and validation

After the first successful full build and visual review, the complete
statement-to-proof and source pass rechecked finite ideal coordinates,
rational realization, canonical signs, exceptional support, the cone zero,
central multiplicities, irrational extension, and the infinite example.
It clarified the nonempty boundary strata used for continuity, made the
curve principalization explicit, and repaired infinite-entropy wording.
The final typesetting pass kept the domination computation together and
incorporated the short Gauss calculation into its paragraph.

Final complete build: **3,961 pages, 18,839,044 bytes**. Reference audit:
389 inputs, 11,585 unique labels, zero missing inputs, duplicate labels or
dangling references. Final log: no unresolved references/citations,
multiply-defined labels, or horizontal/vertical overflow. Existing underfull
and class warnings remain. Strict changed-block audit: zero errors/warnings;
with bibliography: zero errors and two reviewed exact-arXiv warnings.
Whole-chapter bibliography-aware style audit: 120 errors and 8 warnings
(legacy 117 inline delimiters, 2 missing example labels, 1 compound-surname
bibliography-label error; 3 preprints, chapter-label prefix, 4 optional titles).
This is not a clean whole-chapter style claim. Inventory: 46 atoms, 14
environments, tiers (0,5,8,16,17). `git diff --check` passes.

The final changed pages and boundaries, physical 3329--3335, were rendered
and inspected after compilation. A premature read while the PDF was being
written was discarded; the completed PDF and final rendering pass succeed.
Final chapter SHA-256: `f36abb1303731cfa8e8a7a6a8c2a0c2469daa601a76b4c3d2546f8cb82db461a`.
Final live PDF SHA-256: `32896ea13e5be43fe1a44b44f5b65f7f4f0641f82c2838cfb4741be484934239`.

Everything before and after Section 59.5 retains its baseline bytes,
including the projective comparison, later examples and source note.
Chapters 58, 60 and 61, bibliography, supplied CURVE_PSH.tex, frozen packets,
verifier receipts and dated releases are untouched. This is a source
reconstruction with a local two-pass review, not an independent-agent or
production-verifier receipt. It closes no research atom. The later
author-supplied P12.1 integration is a separate unit.
