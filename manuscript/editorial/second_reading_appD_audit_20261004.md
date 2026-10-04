# Appendix D second-reading audit — 4 October 2026

All 936 original lines of *Convex analysis and Legendre duality* were freshly
read, including all proofs and examples. There are no direct inputs. The
revision has 944 lines. Appendix D closes the ordered gate; Appendix E is
active and all 669 original lines have already been freshly read.

## Repairs and mathematical review

The sphere and facet formulas now use an auxiliary Euclidean structure on
M whose volume measure is the lattice-normalized Lebesgue measure, and the
dual structure on N. This makes their unit normals and area measures
compatible with the mixed-volume normalization.

The final support-current theorem and proof now restrict the Lorentzian
signature assertion to smooth strictly convex fixed bodies. The inequality
for arbitrary convex bodies follows by Hausdorff limits. A point among
the fixed bodies in dimension at least three makes the limiting bilinear
form zero, so an unrestricted signature assertion would be false. Exactly
the final theorem and proof change; the other 37 formal environments remain
byte-identical. The mixed-current identity itself is unchanged.

The rereading checks the proper closed-convex hypotheses, affine-minorant
separation including a vertical separating hyperplane, Fenchel equality,
the one-break concave inversion, and the distinction between scalar duality
and analytic envelope realization. Mixed-volume polynomial coefficients,
Hausdorff continuity, positivity and monotonicity retain finite-dimensional
scope. The Alexandrov Monge–Ampere convention has no factorial; the current
power carries n!, and the mixed-current measure divided by n! equals the
mixed volume times the Dirac mass at zero. Subgradient images are measurable;
almost-everywhere differentiability of the conjugate also handles
lower-dimensional bodies. Compact/open Portmanteau estimates justify local
weak convergence. Probability normalization requires positive finite mass;
signed moments are treated by their positive and negative parts.

## Primary-source evidence

The pinned Berndtsson arXiv 2501.02896v3 PDF (6 August 2026, 93 pages) was
freshly checked at physical pages 1, 17–18, 21–28 and 50–59: 21 selected
pages, all 1,029 extracted text lines, and all six source contacts. Its SHA-256
is `d2cb950659b15eb2223ee6cebf7034c6169346277c79a5fb4bd0adbb6a4da034`.
The selected interfaces are Theorem 4.2 and Remark 4.3 (convex Bedford–Taylor
products), Theorem 5.1 (mass and monotonicity), Section 6 (support functions,
Dirac mass and polarization), Section 7 (partial-dilation convention),
Theorems 12.3 and 12.5 (Lorentzian signature and linear algebra), and the
selected Section 13 kernel/solvability argument. The current normalization
and the source's partial dilation are explicitly translated to the book's
Lagerberg conventions.

These are selected-page checks, not a whole-paper reading. Earlier mass,
PDE and deformation inputs remain imports; the source's final deformation
argument is presented as a sketch. Page 59 only begins the alternative
Gromov proof. The freshly read internal interfaces are Chapter 7 lines
2183–2226 and Chapter 14 lines 2140–2205. Classical Rockafellar, Schneider
and Evans–Gariepy locators remain previously identified foundational inputs,
without a new whole-book source review. The historical 18,225 D–F
illustration checks were not rerun and are not a D-only total.

## Source and rendered gates

Baseline commit: `44e6f54526551a3c931b3591ebc0564b8ecb665c`.
Original SHA-256:
`e709ffdebf3312f8a0fd6cce17aa30ff163403df2ed36ff0b6ff5bd3ff157b29`.
Revised SHA-256:
`d7f2191ee0e4c90705d4100dfa9f1a5f9934dd4b450b1f457cdb894f5ae95f1d`.
All 65 labels and their order, 39 formal environments and thirty tagged
display labels are preserved. Existing inline delimiter syntax is retained
(342 pairs). No unlabelled numbered object, double-dollar display or
placeholder was found.

The new full build has 4,236 pages, 19,735,004 bytes and SHA-256
`0aa144bfef9cdd64da4149eb77abc8d0586cd1cfe3d9d5f78f6faa1ac240a066`.
TeX errors, package warnings, overfull boxes, unresolved references/citations
and rerun requests are zero; 953 inherited bookwide underfull boxes remain.
All fourteen appendix pages 3849–3862 and seams 3848/3863 were actually
viewed in four contacts. The terminal page and the preceding recto separator
are intentional blanks; the revised statements and formulas fit.

Post-render references are clean across 425 active files and 12,569 labels.
The unchanged inventory passes at 42 atoms in twelve families, with tier
totals 0/3/7/15/17. Six checker regression tests passed in the new complete
build. No new independent verifier verdict, exhaustive literature search
or open-problem solution is claimed.

Review PDF: `/workspace/book-completion-drafts/second-reading/AppD_Review_2026-10-04.pdf`.
The whole-book goal continues through E–N and front matter before new research.
