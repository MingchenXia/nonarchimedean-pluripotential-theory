# Final-chapters source audit, 22 August 2026

**24 August release addendum.**  Availability statements below describe the
22 August snapshot only.  Xia's positive-volume Conjecture 8.8 formula is now
supported by repaired-proof review and two exact-current Chapter 55 production
runs, `20260824T054849Z_57635bfa07f4` and
`20260824T061508Z_17bf73c6b37c`, both final `correct`, zero critical errors,
and zero gaps.  This does not close the Chapter 72 zero-volume environment:
Conjecture 5.29, auxiliary-potential independence, zero-volume geometry, and
the transcendental, singular-variety, and attainment extensions remain open.
The source is an unpublished author-supplied work in progress, not a published
or priority claim.  The failed MP--DXZ packet and the standalone MP reduced
entropy-slope reconstruction retain their recorded non-promoted status.

## Scope and exact inventory

**23 August correction.**  The 22 August count included a purported
\(P\)-valued trace-refinement problem.  The supplied complete trace chapter
already proves that trace depends only on the input \(\mathcal I\)-class and
is unique as an output \(P\)-class.  That environment has been removed.
Wu's source-stated affine-cone comparison/image problem has been added in its
place.  The current counts below supersede the original 22 August inventory.

This audit covers printed Chapters 71--72:

- parts/part6/ch71_pseudoeffective_mp_dxz.tex;
- parts/part6/ch72_major_open_problems.tex.

Chapter 72 contains exactly 21 problem environments. Chapter 71 contains
the separate projective-rational full-MP-cone problem. Thus the book-wide
inventory is exactly 22. Every environment retains a genuinely open residual
scope. At the whole-environment level the count is:

| resolved | disproved | conditional | genuinely open |
|---:|---:|---:|---:|
| 0 | 0 | 0 | 22 |

Resolved, disproved, and conditional subclaims inside those environments are
boundary results, not additional active problems.

## Primary-source delta since 15 August

The only status-changing revision found among the version-sensitive sources
in the open-problem manifest was Antonio Trusiani,
arXiv:2605.30063v2, submitted 17 August 2026. Version 2:

- retains Theorems A--B and Corollaries A--B;
- retains the claimed smooth polarized projective automorphism-relative YTD
  theorem and special Fujita/entropy regularization;
- explicitly records the consequent projective maximal-ray entropy-slope
  equality;
- adds Theorem C for the weighted-relative smooth polarized correspondence,
  including the log-concave weighted-extremal consequence;
- adds an appendix by Sébastien Boucksom proving the entropy approximation
  over \(k((t))\) in the non-Archimedean formalism.

These are recorded as dated preprint claims, not promoted as new book
theorems. OP-19 remains open only in its compact-Kähler, singular,
hybrid-continuity, bounded-support, and direct-algebraic-proof residual
scopes.

The primary-source version pages checked through the cutoff also confirm:
DXZ arXiv:2302.02541v3; Xia arXiv:2312.17150v3; MPWN
arXiv:2509.09442v1; Boucksom--Jonsson arXiv:2509.15016v1;
Darvas--Zhang arXiv:2509.15173v2; Pille--Schneider
arXiv:2209.04879v2; Gubler--Rabinoff arXiv:2503.05513v1 and
arXiv:2506.13548v2; and BMPS arXiv:2603.08664v1. No revision of those
sources changed a Chapter 72 status by 22 August 2026.

## MP--DXZ--BJ scope firewall

The strongest source-backed projective comparison is:

1. DXZ Theorem 3.14: for a smooth projective manifold and a
   pseudoeffective \(\mathbf Q\)-line bundle \(L\), the full DXZ space is
   bijective and order-isomorphic to \(\operatorname{PSH}(L^{\mathrm{an}})\).
2. Xia, formula (3.8) and Theorem 3.12: in that
   \(\mathbf Q\)-line-bundle setting the comparison is literally the raw
   multiplier-ideal formula on every semivaluation.
3. DXZ Remark 3.15: the canonical identification extends, by two stated
   inverse-limit identifications, to pseudoeffective real Néron--Severi
   classes.
4. MP Section 5.2 and Remark 5.2.1: the MP--DXZ comparison is proved in
   finite energy; removal of the energy assumption is more delicate.

Accordingly, the book now asserts the literal all-semivaluation raw formula
only for \(\mathbf Q\)-line-bundle classes and the source-stated
directed-limit identification for real Néron--Severi classes. It does not
identify the full MP cone with the DXZ/BJ cone. It does not create an MP
cone for a non-nef class, and it does not replace \(P\)-equivalence with
\(\mathcal I\)-equivalence.

## Verification status and blocker

No new manuscript theorem was promoted in this audit. The historical exact
packet open_problems/mp_pseff_chapter_exact has two negative verifier
verdicts and no valid production receipt. The candidate-only 15 August
trace and filtration analyses also remain unpromoted.

At 22 August 2026 the configured Rethlas launcher remains unavailable
because the account usage cap reports a reset on 27 August 2026. Therefore
any statement not already imported from the exact primary-source anchors or
covered by an existing valid receipt remains pending/open.

## Final-chapters slice

The dedicated driver `tmp/pdfs/part6_ch71_ch72_slice.tex` compiles printed
Chapters 71--72 against the book preamble. The final run on 22 August 2026
produced `part6_ch71_ch72_slice.pdf` (76 pages, 609854 bytes), SHA-256
`6477602bd58c6344f9a2ccfb3cfa0756c1879ecdf60499723b35b51327e01d08`.
The log contains no undefined citation, undefined reference, multiply-defined
label, LaTeX error, undefined control sequence, or fatal error. It retains one
3.0 pt overfull display box and one harmless underfull table-cell warning.
