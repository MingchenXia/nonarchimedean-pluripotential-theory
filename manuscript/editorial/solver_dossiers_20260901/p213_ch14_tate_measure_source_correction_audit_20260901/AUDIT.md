# Chapter 14 Tate-skeleton measure: known-source correction audit

Date: 2026-09-01. Auditor and replacement author: /root/p082_independent_reaudit.
Status: original example FAIL; complete known-source replacement supplied for independent parent review. No new theorem, production submission, production verification, or live edit.

## 1. Exact bounded scope and provenance

The sole target is ex:ch14-skeleton-current in
/Users/mingchen/Projects/Yethlas/nonarchimedean_pluripotential_theory/manuscript/parts/part2/ch14_currents.tex.
The exact original example is saved as original_target.tex, with source-context and primary-source hashes in INPUT_PINS.json.

This is a NEW sibling packet. The frozen preceding cycle/fundamental-cycle correction packet is not modified. The replacement retains the historical label. The original Tate block contains no equation references; its empty eqref list is preserved and checked. Correct existing references to the Tate quotient and lattice measure are retained; references invoked to justify the false current identification are deliberately removed.

The original source passage was independently diagnosed. The proposed replacement is authored by this auditor and is not described as having received a second independent audit. Parent requested this separate complete example and will review it. Runtime context does not independently certify a model-name/reasoning-effort gate such as sol/xhigh; no such metadata certification is claimed.

## 2. Errors requiring correction

(1) The displayed functional f -> integral_Sigma f ds acts on compactly supported smooth (0,0)-forms. By the definition of a current in CLD 7.1.1, its bidimension is (0,0), and on a curve its bidegree is (1,1). The original assigns the opposite degrees.

(2) The whole-curve integration current delta_E acts on (1,1)-forms. It is the current [1] associated with a locally integrable function, not evaluation of a measure at the test function 1. The equation delta_Sigma=delta_E is ill-typed under the original displayed definition of delta_Sigma. Compactness makes 1 a permissible FUNCTION test for the measure; it does not change its form degree.

(3) The assertion that every top-degree form on E is carried by the canonical circular skeleton is false. The replacement gives an original-K explicit open-disc/annulus form disjoint from that circle with positive integral. No algebraic closure, residue-field restriction, alteration, or current base change is involved.

(4) Writing delta_Sigma=tau^* has no defined meaning in the stated equality, and the displayed identity for tau-invariant functions proves no current pullback theorem. The repaired identity is the elementary measure identity obtained from tau o i=id, valid for every continuous ambient function.

(5) The final comparison between q and q^2 and unchanged full-space topology is removed. Its truth in any broader category is not needed here, and no all-fields whole-space homeomorphism assertion has been established or is supplied.

## 3. Complete mathematical verification of the replacement

### 3.1 Scope and quotient skeleton

K is complete and nontrivially valued, and q belongs to K with 0<|q|<1. E is the split Tate elliptic curve, given by its actual analytic quotient. This does not require algebraic closure, discrete valuation, characteristic zero, or assumptions on the residue field.

CLD 19.2.1--19.2.2 explicitly places the uniformization in the split setting and describes the skeleton as the quotient of the split-torus skeleton by the lattice. In this example the good-reduction factor is a point, the torus is G_m and the lattice is q^Z. The seminorm formula for eta_s gives the shift s -> s+ell directly. It also gives a continuous embedding of R/ell Z into E and the usual retraction: evaluate -log|T| modulo ell and then take its Gauss point class. These formulas are compatible with every q-translate.

The sign convention s=-log|T| is opposite to any positive-log convention in the source; the lattice LENGTH measure is unsigned, so this changes no normalization. Translations preserve ds. A fundamental interval has length ell, with its two endpoints identified and with no endpoint atoms.

### 3.2 Radon measure and current

The circle is compact Hausdorff and ds is its finite positive length measure. Its inclusion in the separated proper analytic curve is continuous, so its ordinary measure pushforward is a finite Radon measure. It is not an analytic inclusion of a one-dimensional analytic subspace, and no analytic pushforward theorem is being invoked for this inclusion.

For a smooth test function f, absolute value of its pairing is bounded by ell times its supremum norm. On every fixed compact chart datum this is the C^0 continuity estimate; hence it defines an order-zero current. This reproduces precisely CLD 7.2.8(a). Its bidimension is determined by the test degree and its bidegree follows from n=1 in CLD 7.1.1. Since E is compact, f=1 is allowed and the pairing is ell.

The full integration current delta_E instead has bidimension (1,1) by the definition of analytic integration. CLD 7.2.10 with u=1 gives the same current degree and continuity statement. None of these assertions identifies these two differently graded objects.

### 3.3 Actual-source off-circle test

Set B={|T-1|<1}. The ultrametric inequality gives |T|=1 on all actual analytic points of B. Distinct q-translates have distinct constant |T|, so they are disjoint. The quotient by the discontinuous lattice is a local analytic isomorphism; its restriction to B is injective, open and an analytic isomorphism onto its image. This uses the original analytic quotient, not a statement about a Cartesian point set.

Every standard Gauss point eta_s satisfies |T-1|=max(exp(-s),1), including s=0, where there is no cancellation in the Gauss norm. Consequently B misses the entire standard torus skeleton; its image misses the quotient skeleton since every translate of a Gauss point is again a Gauss point.

The coordinate z=T-1 identifies B with an open unit disc over K. For any real 0<r<R<1, its punctured annulus r<|z|<R exists over K; generalized radii require no field extension. A smooth coefficient chi supported compactly inside (-log R,-log r) produces the displayed ordinary smooth (1,1)-form. Its support is contained in a closed subannulus strictly inside the open annulus. That closed subannulus is an affinoid domain and compact; its quotient image is compact and contained in the ordinary open image of B. The form therefore extends smoothly by zero; no unsupported G-open extension is used.

On that annulus z is an actual analytic coordinate. The corresponding moment is an isomorphism onto a standard annulus, so its canonical top-cell calibration has degree and lattice index 1. In dimension one d'u wedge d''u has positive sign. The definition of calibrated integration is thus exactly the ordinary integral of chi du, which is strictly positive. The form is zero near every point of the fixed circle, since its compact support is disjoint from that closed circle. This disproves the claimed universal fixed-skeleton carrier, without requiring any general current-rigidity result.

## 4. Primary-source ledger

Primary source: A. Chambert-Loir and A. Ducros, Formes differentielles reelles et courants sur les espaces de Berkovich, arXiv:1204.6277v2, 25 July 2025, local /private/tmp/CLD25.pdf and /private/tmp/CLD25.txt. Exact hashes are in INPUT_PINS.json and the manifest. The PDF has 608 pages; printed page numbers used below agree with PDF page positions in the inspected sections.

| Source | Exact use | Scope / limitation |
| --- | --- | --- |
| CLD 7.1.1 (definition of a current), printed p155 | Bidimension is the bidegree of the test forms; D^{p,q}=D_{n-p,n-q} | No choice of skeleton reverses this convention. |
| CLD Proposition 7.2.8, pp161--162 | A positive Radon measure gives a positive current of bidimension (0,0), order zero | Applied to an already constructed finite measure, not used to manufacture an analytic current pullback. |
| CLD Corollary 7.2.10, p163 | A locally integrable function defines a current on top-degree test forms | u=1 gives the whole-space integration current, not a measure paired with the function 1. |
| CLD paragraphs 19.2.1--19.2.2, pp551--552 | Split uniformization and quotient skeleton / retraction | Already split Tate case; no extension of scalars required. |
| CLD paragraph 12.1.2, p329 | Actual Gauss seminorm on Laurent polynomials over the original field | Gives the shift and the no-cancellation assertion at s=0. |
| CLD paragraph 14.5.2 and Proposition 14.5.3, pp410--411 | A coordinate isomorphism has calibration degree 1; standard torus lattice normalization | Used only for the explicit standard one-dimensional annulus. |
| CLD Proposition 15.1.1(b), pp421--422 | Ordinary smooth forms arise from analytic moments on ordinary opens | The z-coordinate construction is already such an ordinary chart. |
| Current book ex:trop-tate-curve, def:ch11-lattice-measure, ex:ch14-forms-and-measures | Existing compatible normalization and references | Read as dependencies; not asserted to make every form descend to one fixed circle. |

The genuine primary pages 155, 161, 162, 163, 329, 411, 421, 422, 551 and 552 are rendered and visually inspected, including the complete current definition, measure proof, Gauss formula, calibration proposition, ordinary-moment representation and split-skeleton statements. The previous bounded cycle audit inspected the independent fundamental-cycle sources. The present statement does not rely on its new replacement as a theorem.

## 5. Structural checks and handoff

proposed_replacement.tex is the COMPLETE replacement example, retaining ex:ch14-skeleton-current. It uses existing roman differential and exponential macros. INPUT_PINS.json records the exact original excerpt and relevant source files. check_packet.mjs checks source bytes, unchanged labels/equation-reference list, actual reference labels, balanced environments/braces, all authored control bytes, and all final manifest and checksum entries.

No full-book compilation is claimed here. No live book, old frozen packet, bibliography, production endpoint or Git state was modified. Parent's authorized integration and ordinary book build are the remaining layout checks. The final manuscript correction is an application of established definitions and calibrated integration, not a new mathematical theorem.
