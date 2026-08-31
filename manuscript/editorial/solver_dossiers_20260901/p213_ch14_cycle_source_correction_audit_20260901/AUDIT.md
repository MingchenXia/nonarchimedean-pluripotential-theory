# Chapter 14 cycle-current source correction audit

Date: 1 September 2026.
Auditor and correction author: /root/p082_independent_reaudit.
Classification: KNOWN SOURCE ONLY. No new theorem, no P21.3 claim, no production-verified status.

## 1. Verdict and bounded scope

The two requested passages require correction. The underlying identity delta_Y=delta_[Y] is exactly CLD Proposition 16.6.3 and remains valid in the stated scope; its manuscript proof is not the proof in that source and contains an invalid excision. The line-cycle example confuses the test degree of an integration current with that of a measure and suppresses the actual calibrated rays.

The audit covers the complete example labelled ex:ch14-line-cycles and the immediately following theorem/proof labelled thm:current-fundamental-cycle, with only their necessary current-degree, star and calibrated-degree dependencies. No whole-chapter approval is implied. The replacement preserves both labels and the theorem statement verbatim, supplies the source's actual proof, and repairs a further cycle-versus-Dirac confusion inside the same example.

Only the new dossier was written. The live chapter, all earlier frozen packets, bibliography, inventory, Git state and production services were untouched.

The runtime context available to this agent does not provide independently verifiable model-identifier/reasoning-effort metadata. Accordingly this report does not attest a sol/xhigh execution or satisfy any external model-identity gate by assertion.

## 2. Exact manuscript input

Read-only live source:
 /Users/mingchen/Projects/Yethlas/nonarchimedean_pluripotential_theory/manuscript/parts/part2/ch14_currents.tex

At the audited read it contained 160088 bytes and had SHA-256
 4dc28ea36f841d71ff6f082a6e458d8c9fec3d150c802f241d5430c37dc9a1c7.

The target was approximately lines 2550--2618 at that revision. Exact blocks are preserved in original_target.tex, from the beginning of the line-cycle example through the end of the fundamental-cycle proof. The necessary star description, Dirac example and truncated-potential example are preserved in original_star_context.tex. The original theorem statement is checked byte-for-byte against the proposed statement.

The whole live file is mutable context, not a promise that later authorized book edits must preserve its hash. The frozen local excerpts and the source PDF/text pins make this audit independently reproducible.

## 3. Findings in the line-cycle example

### 3.1 The purported mass is ill-typed

CLD 7.1.1 defines a current of bidimension (p,q) as a continuous functional on compactly supported forms of type (p,q). For a curve, its integration current delta_X has bidimension (1,1), or bidegree (0,0), and
\[
                    \langle\delta_X,\alpha\rangle=\int_X\alpha
                    \quad(\alpha\in A_c^{1,1}).
\]
The constant function 1 has type (0,0). Therefore the expression described as delta_X's mass against the constant test form is not a defined pairing. By contrast a zero-cycle current has bidimension (0,0), is a measure, and can be evaluated on 1 when the underlying space is compact.

The equality delta_X=[1] does not change this conclusion: [1] means the current associated to the smooth function 1 by integration against a complementary top-degree test form. It does NOT mean evaluation of delta_X on 1.

A scalar mass for a positive bidegree-(0,0) current requires an appropriate chosen top-degree test form; there is no intrinsic total-length interpretation supplied by its notation alone.

### 3.2 The actual trivially valued line has calibrated real rays

CLD 6.7.3 explicitly realizes the star with branches [-infinity,0], indexed by P^1(k), as the analytification of P^1 over an algebraically closed trivially valued field. Each branch is calibrated by the one-dimensional lattice volume. This is also already the manuscript's own star description in sec:ch14-line-examples.

Choose one branch, its coordinate t=log|T-b|, and a nonzero nonnegative smooth chi with compact support in (-infinity,0). The form
\[
                    \alpha=\chi(t)\,\mathrm d't\wedge\mathrm d''t
\]
extends by zero to a smooth compactly supported form on the whole star: its support stays away from the common center and the rigid endpoint. Its integral is the strictly positive ordinary integral of chi with respect to t. Hence delta_X is certainly not zero.

This directly tests the integration current on its CORRECT degree of form. A one-point auxiliary/model skeleton does not carry every test form of the analytic space and cannot be substituted for the full calibrated star. The correction does not need to deny that a particular coarser model can have a one-point skeleton; it denies the claimed inference about integration.

### 3.3 Two Dirac currents in the same example are not analytic cycle currents

The final paragraph calls delta_p1 minus delta_eta a difference of two cycle currents. Neither point is rigid: p1 is the interior point of a real branch with t=-1, while eta is the generic trivial seminorm. They do define legitimate point-mass currents of bidimension (0,0), but not analytic zero-cycles on this line.

The truncated-potential formula is still correct and is preserved. Its sign can be checked directly on a smooth test f:
\[
 \int_{-\infty}^{-1}(-1)f_b''(t)\,\mathrm d t
   +\int_{-1}^{0}t f_b''(t)\,\mathrm d t
                  =f(p_1)-f(\eta).
\]
The endpoint terms at minus infinity vanish because f is constant there. This confirms the positive atom at p1 and negative atom at eta, but supplies no algebraic-cycle interpretation of these atoms.

The replacement distinguishes this identity from the untruncated Poincare--Lelong formula for the analytic zero/pole divisor of a meromorphic function.

### 3.4 Local finiteness on this compact space is ordinary finiteness

For analytic zero-cycles on compact X, the locally finite family of nonzero point coefficients is finite: take a finite subcover of neighborhoods meeting only finitely many such points. No special smooth-star lemma is needed to prove finiteness against a test. The replacement makes this direct reason explicit and gives the legitimate zero-cycle pairing with 1.

## 4. Findings in the fundamental-cycle proof

### 4.1 A generically nonreduced component cannot be deleted as dimension-lowering

The manuscript proposes deleting loci where an irreducible component is not generically reduced and asserts that the removed set has dimension less than r. If Y has generic multiplicity m>1 on a component, its nonreduced generic structure occupies that whole component. Deleting it removes dimension r, not a lower-dimensional exceptional set.

A basic example is the doubled affine line cut out by U^2=0 in the analytic affine plane with coordinates (T,U). It is pure one-dimensional with generic local algebra K(T)[epsilon]/(epsilon^2), of length 2. The generic multiplicity is 2 along its entire reduced line. Deleting the generic nonreduced component discards exactly the component whose coefficient the theorem must retain.

If the manuscript phrase instead referred literally to the already reduced components Y_j of Y_red, those components are reduced by definition and the phrase supplies no usable locus. Neither reading yields the claimed argument.

### 4.2 The correct deleted set consists only of component intersections

CLD 16.6.3 takes the Zariski open where a point belongs to exactly one irreducible component. It does NOT delete the locus of generic nonreducedness. Pairwise intersections of distinct pure r-dimensional components have dimension less than r.

The needed support fact is the stronger ambient assertion CLD 15.2.1(b): the SUPPORT of a top-degree form avoids a lower-dimensional analytic closed set. Merely saying that the restricted form on that set is zero would not by itself justify deleting the set from an arbitrary integration problem. The replacement cites and uses the actual support statement.

This removes the intersections and leaves disjoint OPEN subspaces with their possibly NONREDUCED induced structure.

### 4.3 The source uses calibrated degree 1/m, not a graded-length slogan

CLD 13.3.4--13.3.7 defines the calibrated degree using normalized Artinian lengths. For the finite reduction immersion of a generically multiplicity-m component, it is
\[
                  \frac{\operatorname{length}_A(A_{\mathrm{red}})}
                       {\operatorname{length}_A(A)}
                   =\frac1m.
\]
The numerator is 1, since the reduction of an Artinian local ring is its residue field. Ordinary finite-flat degree is not being substituted here: a reduction immersion is generally not flat.

CLD 15.4.3 then gives the finite-map integration formula. Applied to the reduction immersion nu:V_red -> V, it yields
\[
                      \int_{V_{\mathrm{red}}}\nu^*\omega
                               =\frac1m\int_V\omega.
\]
Thus integration on V is m times integration on its reduction. Summing the disjoint open pieces produces the fundamental-cycle identity.

The printed CLD proof cites exactly Propositions 15.4.3 and 13.3.7 and displays exactly this inverse factor. It contains no blanket statement that length is unchanged by a graded reduction. The manuscript's claimed graded-length principle is undefined as written, unproved, and incorrectly attributed to this proposition. This audit does not replace it with another unsupported assertion about all possible graded norms; the correction uses the source's calibrated-degree argument.

### 4.4 Locally finite components, not globally finitely many components

The original proof writes Y_1,...,Y_s although the theorem is not restricted to compact Y. The corrected proof allows a locally finite family, and every sum becomes finite after fixing a compactly supported test form. The disjoint open pieces meeting that support each inherit compact support for the restricted test.

No narrowing to a reduced, irreducible, good-reduction, projective or geometrically connected Y is introduced. The equality itself also needs no new boundaryless hypothesis; boundarylessness is used separately for closedness of integration currents.

## 5. Exact known-source interface

| Primary source | Exact scope/use in the correction |
|---|---|
| CLD 7.1.1, printed p.155 | Bidimension (p,q) acts on A_c^(p,q); bidegree is complementary to the analytic dimension. |
| CLD 6.7.3, printed p.152 | Trivially valued algebraically closed P^1 is the calibrated star; smooth compact tests on a branch interior are legitimate. |
| CLD 16.6.1--16.6.2, printed p.459 | Integration currents of closed analytic subspaces and locally finite analytic cycles. |
| CLD 16.6.3, printed p.459 | The unchanged theorem delta_Y=delta_[Y] and its component-open/reduction-immersion proof. |
| CLD 15.2.1(b), printed p.423 | Ambient SUPPORT avoidance for a lower-dimensional analytic closed subset. |
| CLD 13.3.4--13.3.7, printed pp.379--380 | Calibrated degree of reduction is the reciprocal generic multiplicity, including nonreduced targets. |
| CLD 15.4.1--15.4.3, printed pp.425--426 | Finite-map Radon-measure/integration formula for locally integrable top forms, valid for the finite reduction immersion. |

Exact source version: Chambert-Loir--Ducros, Formes differentielles reelles et courants sur les espaces de Berkovich, arXiv:1204.6277v2, 25 July 2025, 608 pages. The [official version record](https://arxiv.org/abs/1204.6277v2) was checked on 2026-09-01.

Local PDF: /private/tmp/CLD25.pdf, 4659053 bytes, SHA-256
 5690f999523017d184ab751bb55857ab1637b197d1186ad4fd2edba7e1bda719.

Local extracted text: /private/tmp/CLD25.txt, 2150944 bytes, SHA-256
 021be260392de1f3240858d4c775da86653518dfab4fd9c4c21a2406081b6c7e.

Relevant text ranges read in full: 7540--7735, 19180--19312, 21524--21583, 21635--21762 and 23315--23410. The complete relevant PDF pages 152, 380, 423, 426 and 459 were rendered and visually inspected, especially the inverse factor on pp.380/459 and the support statement on p.423. No missing symbol or PDF-extraction ambiguity remained. The original PDF was neither edited nor re-exported.

The PDF skill was used for that read-only visual verification. No new PDF is a requested deliverable.

## 6. Replacement and checks

proposed_replacement.tex contains the COMPLETE replacement example plus COMPLETE replacement theorem/proof, not just editing instructions. Both existing labels and the original equation reference eq:appJ-cld-pl are preserved; the latter now correctly refers only to the untruncated Poincare--Lelong formula. The theorem statement is byte-identical to the target statement. No additional theorem is invented.

The check script verifies:

- all pinned primary-source bytes;
- exact original-target extraction if the live chapter remains at its audited revision;
- preservation of both labels and the original theorem statement;
- balanced TeX environments and braces, and all controls except LF/TAB;
- the existing source labels used by the replacement and the CLD25 bibliography key;
- every frozen manifest/checksum entry.

No full-book compilation or production validation is claimed. The replacement uses existing book macros and references; the referenced chapter labels and bibliography key were checked directly. A later ordinary book build after authorized integration remains the appropriate final layout test. Finite string/structure checks are not represented as a mathematical proof.

The original passages fail the source/mathematical audit for the reasons above. The replacement is the auditor's authored known-source repair, not a separately independently reviewed repair. Its proof follows the complete original CLD argument with the degree and support steps made explicit.

## 7. Adjacent risk recorded, not expanded into this task

The immediately PRECEDING example ex:ch14-skeleton-current also defines a measure by testing functions and calls it bidimension (1,1), then identifies it with the whole Tate-curve integration current. That is the same degree warning and cannot be used to justify the repaired line example. It was encountered in the necessary surrounding read and reported to root, but no replacement of that third example is included here and no full audit of its attached-tree assertions is claimed.

The bounded correction does not rely on that example, on the recent research rigidity packets, or on a production receipt.
