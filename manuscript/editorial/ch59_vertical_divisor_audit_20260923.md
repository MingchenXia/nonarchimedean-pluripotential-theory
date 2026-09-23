# Chapter 59 invariant vertical-divisor audit

Date: 23 September 2026.
Baseline: `bc0fae8e00ad7a8fe1a997bc9bae91e8102dabfd`.
Scope: the model definition, normalized vertical restriction and divisorial
comparison in Section 59.4, ending before the PL/vertical-Cartier proposition.
The standing base X is a connected compact Kahler manifold.

## Findings

The map called restriction was described as restriction along the inclusion
of a fiber. Its actual definition uses pullback under the projection to X.
A valuation factoring through t=0 would give t infinite value, incompatible
with the vertical normalization w(t)=1.

The proof cited BHJ Theorem 4.8 for a general local divisorial restriction
assertion. In the published paper, that theorem identifies Rees valuations
in the deformation to the normal cone. The general restriction calculation
is Lemma 4.1; the test-configuration comparison is Theorem 4.6 and its
realization step is Lemma 4.7. The manuscript's claim that discreteness and
w(t)=1 alone justified passage to excellent analytic local rings did not
supply the necessary dimension argument.

The forward construction took place on Y x P1 for a modification Y of X.
The composite to X x P1 is generally nontrivial off the central fiber.
Transporting the divisor therefore needs a separate construction of a model
of X. The former account mentioned this transport, but did not explicitly
verify the support of every center or the resulting model conditions.

## Reconstruction and mathematical checks

The projection and its composite with the model morphism are now explicit.
Connectedness of C* gives invariance of each central-fiber component, and
the multiplicity b_E remains the normalization factor.

The new local lemma works over a regular excellent local C-algebra A.
For a divisorial valuation w over A[t] with w(t)>0, write v=w|Frac(A).
If v is nontrivial with center p of height h, the center of w is (p,t),
of height h+1. The birational dimension formula gives residual transcendence
degree h for w over kappa(p). Residues algebraically independent over
kappa(v) lift to elements algebraically independent over Frac(A), so the
residue extension from v to w has transcendence degree at most one.
The value group of v is a nonzero subgroup of the discrete cyclic group
of w. Abhyankar's inequality forces residual transcendence degree h-1.
The regular excellent version of Jonsson--Mustata Proposition 3.7 and
Remark 3.9 then makes v divisorial. Its scalar is rational. No finite
generation of Frac(A) over C is assumed; invariance is not needed for
this local restriction lemma.

The projective model is algebraized over a germ of X, retaining its map
to P1 over A. Its birationality gives the field Frac(A)(t). Divisor orders
are compared componentwise in that germ. A global irreducible analytic
center is not assumed to have an irreducible germ. Factoring the generic
order of a nonzero ideal and applying the identity theorem on the smooth
prime E proves equality of the local and global orders. The zero ideal
has infinite value in both descriptions; the unit has order zero.

The center-blowup termination argument is supplied explicitly. Normalize
the group to Z. In a local ring at the center, choose a maximal-ideal
generator of least positive value. In its blowup chart, dividing numerator
and denominator by that generator decreases the denominator's value by a
positive integer. Any prescribed fraction in the divisorial DVR eventually
belongs to a center local ring. The DVR is essentially of finite type, so
finitely many such fractions suffice; the localization denominators have
value zero and are already units. This proves finite termination, also
with intermediate normalizations. A center already of codimension one
needs no additional extraction.

The blowups use global reduced center ideals, obtained from proper images
on common resolutions. At the generic point of the selected local branch,
the other branches disappear from the localized ideal. Thus the local
center-ring calculation applies to the global sequence. The existing
Bingener dimension comparison makes the terminal irreducible center a
global divisor. The normalized restriction is q ord_F, with q=e/b_E for
a positive integer e. It is not silently replaced by the primitive order.

For the converse, primitive weights (k,m) along F x {0} on Y x P1 give
an invariant prime order with values k on a local equation of F and m
on t, using the previously checked ordinary-blowup construction. A second
extraction starts directly on X x P1. Its centers are invariant and
contained in t=0. All maps are therefore isomorphisms off that fiber.
Projectivity gives the Kahler property, and torsion-freeness over the
local DVR of P1 gives flatness. Equivariant resolution preserves the
order and the multiplicity m. The product model supplies the trivial
valuation, including when dim X=0.

The example on P1 computes b_E=3 and r(v_E)=(2/3) ord_p for weights (2,3).
The global ideal I_p^3 and the local flag ideal (u^3,t^2) both have
normalized value 2. The product of Bl_p P2 with P1 demonstrates the
noncentral-fiber obstruction addressed by the second extraction.

## Primary sources

- Boucksom--Hisamoto--Jonsson, *Uniform K-stability, Duistermaat--Heckman
  measures and singularities of pairs*, Ann. Inst. Fourier 67 (2017),
  no. 2, 743--841, [published DOI 10.5802/aif.3096](https://www.numdam.org/articles/10.5802/aif.3096/).
  Checked Section 1.3, equation (1.3), and Lemmas 4.1--4.2, 4.5, 4.7,
  Theorems 4.6 and 4.8, pp. 782--785. Physical PDF pages 41--44 were
  rendered and inspected. The finite-type-over-a-field scope is explicit
  in the paper, so the local-ring argument is written out rather than
  attributed directly to that theorem. PDF SHA-256:
  `edfd3b1506b49cf42ae85014d731bd9d86af5ed248134397cd562fba70c6f60e`.
- Jonsson--Mustata, *Valuations and asymptotic invariants for sequences
  of ideals*, Ann. Inst. Fourier 62 (2012), no. 6, 2145--2209,
  [published DOI 10.5802/aif.2746](https://www.numdam.org/articles/10.5802/aif.2746/).
  Checked Section 1.1, p. 2152 (excellence of convergent power series),
  and Section 3.2, pp. 2171--2173, including equation (3.4), Proposition
  3.7 and Remark 3.9. Physical pages 9, 29 and 30 were rendered and
  inspected. The framework includes regular excellent schemes over Q.
  PDF SHA-256: `b0360dbfeb5b19601500e3ed03e8b186f4ac84b6c771a2a300fe25efa0d5fb57`.
- Mesquita-Piccione, [arXiv:2409.06221v2](https://arxiv.org/abs/2409.06221v2),
  18 September 2025, Section 2.5, pp. 20--25: Remark 2.5.2, Theorem 2.5.5,
  Lemma 2.5.9 and Propositions 2.5.10--2.5.11. Physical pages 20 and
  22--25 were rendered and inspected. The reconstruction retains the
  rational factors in the divisor comparisons and treats germ branches
  explicitly. PDF SHA-256:
  `9eb2ea7686a5962ebc11c5eacd23b0cb3dcb081e27ac48292933f291fc82cb23`.
  The exact author-version locators are cited as MPTropicalV2. The
  publisher-access limit recorded in the preceding audits remains; no
  claim is made that these locators were checked in the publisher PDF.

All existing bibliography entries are unchanged. The bibliography-aware
style audit's one arXiv-only warning for MPTropicalV2 was reviewed against
this exact-version policy. The strict audit of the entire changed TeX block
has zero errors and zero warnings.

## Second pass and validation

The first compilation exposed a missing display terminator; it was fixed
before the first successful complete build. After that build and inspection
of physical pages 3318--3323, the second mathematical pass rechecked both
inclusions, the residue-field calculation, finite termination, branch
localization, preservation of the primitive order, and all model conditions.
It made birationality of the algebraized map and compatibility of proper
images explicit, wrote q=e/b_E, used the global point ideal in the example,
and included the zero ideal. The first dimension identity was placed inline
to avoid separating its introductory sentence from a display across pages.
The final build and rendered-page review were repeated after these changes.

The final complete build has 3,953 pages and 18,799,924 bytes. The input
check passes for 389 TeX files and 11,581 unique labels, with no missing
inputs, duplicate labels or dangling references. The final log has no
unresolved references or citations and no horizontal or vertical overflow.
Pre-existing underfull-box and class warnings remain. Final physical pages
3318--3323 (printed 3250--3255) were inspected. Compilation is not a
mathematical verifier. `git diff --check` passes.

Chapter 59 outside this unit, Chapter 58 and the bibliography match the
baseline byte for byte. The supplied CURVE_PSH.tex is unchanged. The
inventory remains 46 active atoms in 14 formal environments, tiers
`(0,5,8,16,17)`. Frozen proofs, author sources, production-verifier receipts
and dated releases are preserved. The live PDF is ignored and is not a new
release. No independent-agent audit, production-verifier pass, new research
theorem or atom closure is claimed.

Final SHA-256:

- Chapter 59: `991080fd39ebb0980e8666ec8dfc9f6310319e0193f80f4cce4e909646a9550c`.
- Unchanged bibliography: `f77736549ed82a38bc6db488b2527629b2cb2ebf5b47475f3c94e08e0e068219`.
- Generated live PDF: `a58fba65450dcba39113c6d537cfde8d2f5b52d3839e2afc8998a1f2448e4d05`.
- Supplied and restored CURVE_PSH.tex: `9142aac73c5af7e4e715b3313def5ed56fae4e63e1ac8a53d0419df7d2194be9`.

Next: audit the PL/vertical-Cartier correspondence, including rational
denominators, fractional flag ideals, the Gauss evaluation on ideals of
X x P1, and generation on a dominating model before using density.
