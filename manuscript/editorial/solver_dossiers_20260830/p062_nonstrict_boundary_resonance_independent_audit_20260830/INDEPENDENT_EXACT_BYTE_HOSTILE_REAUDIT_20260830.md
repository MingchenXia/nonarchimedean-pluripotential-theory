# Independent exact-byte hostile re-audit

Date: 2026-08-30

## Verdict

**PASS: zero critical errors and zero proof gaps.**

This report audits only the corrected final freeze identified below. The
earlier statement freeze was discarded without being relied on. The audit
was performed independently of the author-side hostile self-audit. No file
in the frozen dossier and no live-manuscript file was edited.

The first proposition is a valid counterexample to the unrestricted
arbitrary-radius endpoint-polycylinder classification when the Hessian
current is required to vanish only on the absolute analytic interior. The
second proposition is a valid scalar-stable repair, conditional exactly on
the upstairs current equation stated there and on the already verified
strict-v4 theorem.

This independent verdict is not a production-verification receipt and does
not by itself authorize live-book integration.

## Exact-byte identity

The dossier's SHA256SUMS manifest validates without error. The principal
and compile identities are:

| File | SHA-256 |
|---|---|
| p062_nonstrict_boundary_resonance_statement_20260830.tex | 27ff3ad7a6174b8b38d5890d8c891681edf416f02e2538017db22edf372c1ed8 |
| p062_nonstrict_boundary_resonance_proof_20260830.tex | 15ff9b3a28b63c1e3f37c104f27e30e77431f389ec694a1d3f3823232ef1f125 |
| p062_nonstrict_boundary_resonance_minimal_compile_20260830.tex | 321633edef236554af6e196865f1c749ec5ed8cbac562dca56de6f6e56785605 |
| p062_nonstrict_boundary_resonance_minimal_compile_20260830.pdf | eb3e14de9c7ee80ba81dcda002588e61ba44c69299bacfeea5c34efc317f0280 |
| EXACT_BYTE_RELEASE.md | 278d6ae579241a00772f5bc2f96e6bac0e82c4a0ea212720e11c7a3b82db0913 |
| SHA256SUMS | c62908add097974a5f639e13b2709ac4bdeea7ff5b08771ffc28785dca62006b |

The invoked strict-v4 principal statement has SHA-256
56ffaad6c42e0a14c56279e263d326120ce03f6ae132d8261deee56ff9ca7663.

## Counterexample audit

1. **Radius and geometric hypotheses.** If
   \(R\notin\sqrt{|K^\times|}\), then also
   \(R^{-1}\notin\sqrt{|K^\times|}\). For a discretely valued field with
   \(|K^\times|=|\ell|^{\mathbf Z}\), its divisible closure is
   \(|\ell|^{\mathbf Q}\), so \(R=|\ell|^{\sqrt 2}\) is a valid example.
   The generalized Tate algebra of the displayed bidisc is a domain of
   dimension two, so the bidisc is good and pure two-dimensional. It is
   genuinely non-strict: the spectral radius of \(T\) is \(R\), attained at
   the corresponding Gauss point, whereas spectral radii in a reduced strict
   affinoid algebra lie in \(\sqrt{|K^\times|}\).

2. **Nonemptiness and relative openness of the tube.** The morphism
   \(U\mapsto(U,U^{-1})\) is the analytic closed immersion of the hyperbola
   \(TS=1\). The \(R\)-Gauss point of
   \((\mathbf G_{\mathrm m,K})^{\mathrm{an}}\) maps into the two reciprocal
   closed discs and satisfies \(TS-1=0\). Thus \(W\ne\varnothing\). Since
   \(x\mapsto|TS-1|(x)\) is continuous, its inverse image of \([0,1)\) is
   relatively open in \(P\).

3. **Coordinate equalities and Gauss restriction.** For \(x\in W\), the
   inequality \(|TS-1|<1\) implies \(|TS|=1\). Together with
   \(|T|\leq R\) and \(|S|\leq R^{-1}\), this forces equality in both
   coordinate bounds. If two nonzero terms of a polynomial in \(T\) had
   equal weighted norm at \(R\), then a nonzero integral power of \(R\)
   would lie in \(|K^\times|\), contrary to the hypothesis. Hence every
   polynomial has a unique dominant term, and the first-coordinate
   restriction of \(x\) is exactly the \(R\)-Gauss seminorm.

4. **Absolute-interior argument.** Berkovich Proposition 1.5.5(i)--(ii),
   applied to the analytic domain
   \(P\subset(\mathbf A^2_K)^{\mathrm{an}}\) and the boundaryless affine
   plane, identifies \(\operatorname{Int}(P)\) with the ordinary
   topological interior of \(P\) in the affine plane. If
   \(x\in W\cap\operatorname{Int}(P)\), an ambient open neighbourhood
   \(O\subset P\) would exist. The coordinate projection is smooth, so
   Berkovich Corollary 3.7.4 makes \(\pi_T(O)\) an open neighbourhood of
   \(\eta_R\) contained in \(\{|T|\leq R\}\). This is impossible because
   \(a\mapsto\eta_a\) is continuous (each polynomial Gauss norm is
   continuous in \(a\)) and \(\eta_a\to\eta_R\) with \(a>R\). Therefore
   \(W\cap\operatorname{Int}(P)=\varnothing\).

5. **Cutoff, support, and current.** The maximum of the two displayed
   continuous functions is continuous. Its nonzero locus is
   \(\{|TS-1|<c\}\), so continuity gives
   \(\operatorname{supp}(h_c)\subseteq\{|TS-1|\leq c\}\subset W\) because
   \(c<1\). Thus \(h_c\) is identically zero on the open analytic space
   \(\operatorname{Int}(P)\). By locality, its integration current
   restricts to the zero current there, and hence
   \(\mathrm d'\mathrm d''[h_c]=0\) there. At the hyperbola Gauss point its
   value is one, while at \((0,0)\) its value is zero; it is nonconstant.

These checks establish every assertion of the first proposition and show
that the failed positive statement already fails on a pure two-dimensional
product of two closed non-strict discs.

## Scalar-stable repair audit

1. Base change commutes with the displayed disc and annulus domains and
   with their finite products. Because every defining radius is in
   \(|L^\times|\), \(P_L\) lies in the exact scope of the strict-v4 endpoint
   theorem. The theorem is applied only to the explicitly assumed equation
   on the full absolute interior \(\operatorname{Int}(P_L)\); no ascent of
   currents from \(\operatorname{Int}(P)\) is asserted.

2. CLD Section 11.1.9 states that the scalar-extension projection is
   surjective. A lift \(x_L\) restricts to the seminorm \(x\), so every
   coordinate absolute value is preserved. The affine identity obtained
   upstairs therefore descends pointwise to all of \(P\), without
   descending a current.

3. Uniqueness is valid. Set all disc coordinates to zero and vary the
   annulus Gauss radii through the nonempty open logarithmic box. The
   functions \(1,\log|S_1|,\ldots,\log|S_q|\) are linearly independent on
   this box. For \(q=0\), nonemptiness of the product gives uniqueness of
   the constant.

4. A complete strictifying extension exists for any finite radius list:
   equip a rational-function field with the corresponding multivariate
   Gauss absolute value and complete it. The new variables retain exactly
   the prescribed absolute values. This construction does not supply the
   upstairs current equation, which remains the substantive additional
   hypothesis.

The final sentence of the repaired statement is also sound: if the
counterexample's pullback equation held on the full interior of a
strictifying extension, the repaired proposition would force the
nonconstant cutoff to be constant.

## Source and build checks

- Berkovich source inspected:
  /private/tmp/Berkovich1993_Etale.pdf, SHA-256
  bd864c89ed8b6e8f27a90f459837221549db75afa75554ab51414e17771066af.
  Proposition 1.5.5(i)--(ii) and Corollary 3.7.4 have the directions used.
- CLD source inspected: /private/tmp/CLD25.txt, SHA-256
  021be260392de1f3240858d4c775da86653518dfab4fd9c4c21a2406081b6c7e.
  Section 11.1.9 states surjectivity of scalar extension.
- An exact-byte scratch copy was compiled twice with
  latexmk -pdf -interaction=nonstopmode -halt-on-error. The rebuilt
  five-page PDF has SHA-256
  f1dd4d9e40dc14dd5ebacdf08f8e07a9fab99e8dadc8f937ecd8a94a43d3b861.
  Its five pages were rendered at 160 dpi and visually inspected. The
  rendered PNG hashes agree page-for-page with independent renders of the
  frozen PDF, so the PDF-byte difference is nonvisual build metadata.
- The final log has no TeX error, undefined reference, undefined citation,
  or multiply-defined label. Its sole overfull box is the documented
  inherited 0.74893 pt line in the strict-v4 dependency; the new statement
  and proof add none. Visual inspection found no clipping, overlap,
  malformed glyph, broken display, or unreadable reference.

## Fail-closed scope

The audit confirms exactly the negative arbitrary-radius result and the
positive scalar-stable replacement. It does **not** classify all radius
tuples for which the downstairs equation ascends, prove equality of
interiors after arbitrary complete scalar extension, or extend the result
to nonproduct germs. Those questions remain outside these exact bytes.

Critical errors: **0**. Proof gaps: **0**.
