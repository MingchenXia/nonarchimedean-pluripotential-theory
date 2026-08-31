# Revised1 exact-byte addendum: connectedness scope and display split

31 August 2026. Independent auditor: p213_skeletal_hostile.
Read together with ORIGINAL_INDEPENDENT_AUDIT.md in this directory.

## Revised1 verdict

No remaining mathematical gap was found in the exact revised1 uniqueness
proof within its stated original-BFJ continuous-curve scope. The new
source-scope paragraph explicitly resolves the original proof's Ch05
geometric-connectedness citation mismatch. The second change is only a
line-breaking adjustment to one previously authored energy definition.

This is independent acceptance of the bounded revised uniqueness
argument and exact revision isolation, NOT production verification and
NOT independent acceptance of the weighted-energy baseline authored by
this auditor.

## Exact revised bytes

Directory:
p081_ch28_curve_uniqueness_snc_repair_20260831/revised1 under the common
solver_dossiers_20260831 directory.

- uniqueness_proof.tex, 4414 bytes, SHA256
  493acabe01f2a9dad1028cb8d4a3fa0d85a2f7a88c1fcaa9eb55b08e4bd19e2c.
- patched/ch28_finite_energy_measures.tex, 177787 bytes, SHA256
  d302fc06208ded647cbb4ef3c63c425e54c5382f2ad25cb8ba9bb68a5f8d9315.
- scope_addendum.tex, 497 bytes, SHA256
  d263f6205a3aafb6e23e62751eaa7606b8c3ed974118a913e5a6cd5f3a98e9a2.
- dirichlet_display.tex, 245 bytes, SHA256
  0290744fbacd6b65695f268f7f6685b23fa9da8d755c1c49b970dcb6ac9b9a88.
- chapter.patch, 31899 bytes, SHA256
  1282ff32d331c796af22ccf1fbfb822359c474534521ce0eb86c402ed0b99c8f.
- MANIFEST.json, 3042 bytes, SHA256
  03825f39efb9b1ed0e7f8faa1dea207801919ba611a8206fc44d561f161d8115.

All ten revised1 manifest entries were independently size-checked and
rehashed with zero mismatches. The eight original entries still match.

## Primary-source and connectedness check

The primary [BFJ preprint, arXiv:1201.0187v2](https://arxiv.org/pdf/1201.0187v2)
was independently opened on 31 August 2026. Section 2.4 (printed page 9)
assumes ordinary connectedness. Corollary 2.4 (page 11) proves divisorial
density; Corollary 3.2 (page 12) gives the SNC inverse-limit description;
Corollary 3.17 (page 19) identifies rational skeletal points as divisorial
and realizes them on higher models. The complete relevant statements and
their short proofs were read. Section 1.1 also supplies SNC domination
in its characteristic-zero model framework.

That checks the primary citation in revised proof lines 82--89. Ch05's
extra geometric-connectedness convention need not be imported.
Its cofinality proof was separately reread: common normal projective
domination and the stated relative characteristic-zero resolution input
use smoothness, not geometric connectedness. The primary source and this
algebraic argument cover precisely the ordinary-connectedness case of
Ch28. This audit does not independently reprove the resolution theorem.

Earlier use of the model-function vertex formula also creates no
geometric-connectedness restriction: ord_E(D)/b_E is its local definition,
and real linearity gives the stated formula component by component.

## Exact two-change check

The complete original/revised proof diff and complete original/revised
full-chapter diff were read. An independent in-memory reconstruction
confirmed exactly two changes:

1. The 497-byte scope paragraph is inserted immediately before the final
   end of the uniqueness proof. All earlier proof lines are preserved.
2. The D_Gamma/L/L_R equation gains an aligned environment and a line break.
   Its mathematical tokens, after removing only alignment/spacing syntax,
   are unchanged. No edge weight, exponent, inequality, sign, numerical
   constant, definition domain, or label changes.

The proposed complete chapter is exactly that reconstruction; its patch
against the recorded live chapter is byte-exact and passes git apply
--check without application. All 170 existing chapter labels survive,
with only the model-test label added by the original proof repair.
The author assembly scripts were inspected, never executed, because they
write frozen author artifacts.

The live source remains at SHA256
1bb59ce13a77fb7c6a2153f77e20eae7a340d84e727f2a76bb314c10c14b56a5.
No production call, live integration, or independent full-book compile
was performed. The author's build observations are not substituted for
validation of these exact revised bytes. The full copied chapter includes
the earlier energy patch, so the two cumulative chapter patches must not
both be applied.
