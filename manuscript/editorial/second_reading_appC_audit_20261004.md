# Appendix C second-reading audit — 4 October 2026

All 790 original lines of *Multiplier ideals and test ideals* were freshly
read, including every proof, example and dependency entry. There are no
direct inputs. The revised source has 794 lines. Appendix C closes the
ordered rereading gate; Appendix D is active and its 936 source lines have
been freshly read, with primary checks continuing.

## Repairs and mathematical review

The asymptotic multiplier-ideal definition and uniform-generation theorem
now specify a **nonzero** graded sequence. Without that condition the
definition's family of nonzero indices could be empty, and its maximum
would be undefined. The analytic strong-openness proof now explains the
local reduction from a quasi-psh weight to its psh part: the smooth summand
contributes locally bounded factors to both original and scaled weights.
Exactly these two environments and one proof change; the other 38 formal
environments remain byte-identical.

The squared analytic weight matches the algebraic exponent and Boucksom's
Lp convention with p = 2 and weight phi/2. The one-pole example checks the
floor at integer exponents. The resolution formula separates degree-zero
birational transformation from local vanishing; the ordinary valuative
criterion uses full-support divisorial valuations on a smooth base.
Subadditivity cites the ideal Variant 2.5, extends rational to real
exponents by preserving finitely many floors, and spreads finite-type data
before field extension. Geometric Skoda retains characteristic zero.

The graded-order limit uses the nonzero-index additive semigroup and finite
residue-class estimates. The parity example explains why supported
semivaluations require a divisibility-net convention. Asymptotic ideals
use noetherian stabilization at common multiples. The graded multiplier
estimate is one-sided; no unproved supported valuative criterion replaces
the stabilized maximum.

Frobenius roots and real-exponent test ideals retain regular F-finite
domains and the ceil(t p^e) convention. The Cartier discrepancy estimate
uses Canton v3 Definition 3.3, equation (3.3.1) and Proposition 4.1 only
in the stated smooth, algebraically closed geometric scope. Real-exponent
test Skoda is proved by the root-coefficient and pigeonhole computation;
BMS 2.25 is the exact identity, while HY 2.1 is a related containment.
Fixed-twist generation imports the Chapter 40 relative proof. Its residual
coefficient ranges over a finite set for each fixed m and stabilization
index q; the Serre threshold may depend on them while the twist does not.
Chapter 40's proof and finishing paragraph were freshly checked here.
HY comparison remains one fixed rational-exponent datum after spreading
and excluding primes, without uniform equality for all graded sequences.
The concluding ideal-function comparison keeps its sign reversal,
divisibility nets and supported infinite values.

## Primary-source evidence

Nine pinned PDFs were checked at all 36 selected physical pages. All selected
extracted text was freshly read and all thirteen source contacts were actually
viewed. Eight sources reuse cached PDFs with matching historical hashes; the
Guan–Zhou witness was newly acquired and title checked.

| Source | Physical pages | Checked interface |
| --- | --- | --- |
| BMS, math/0607660v2 | 1, 3–7, 12–13 | Regular F-finite scope; roots 2.2/2.5/2.7; real-exponent 2.9; subadditivity 2.11(4); exact Skoda 2.25 and complete displayed proof |
| Mustata | 6–10 | Trace convention; asymptotic stabilization and 3.1; 3.3 discrepancy example; 4.1 statement and proof beginning |
| Canton v3 | 14–16, 22–23 | Definition 3.3 and (3.3.1); Proposition 4.1 and complete selected proof; algebraically closed geometric scope |
| Schwede–Tucker | 19–23 | Rounding conventions, Skoda and containment references; test-ideal subadditivity |
| HY, math/0211008v1 | 1, 10, 32–33 | Title; 2.1 containment; 6.8 fixed rational-exponent comparison and selected proof sketch |
| BJ, published | 84–86 | Uniform-generation input in the complete displayed proof of 5.20 |
| DEL | 11–12 | Product/restriction deduction and ideal Variant 2.5 |
| Boucksom | 36, 47 | Analytic coherence 9.3/10.20 and Lp normalization |
| Guan–Zhou, 1403.7247v1 | 1–2 | Title, squared-weight definition and Theorem 1.1 statement across the page boundary |

The GZ witness is the identified arXiv v1 for the bibliography's Inventiones
entry; identity with its published PDF is not claimed. A guessed identifier
returned an unrelated cosmology paper, which was excluded after title checking
and is not mathematical evidence. Classical PAG2, log resolution and other
earlier foundations remain explicit imports. The selected Mustata and GZ
pages do not constitute a fresh full-proof or whole-paper review. Exact
PDF/text/image pins and exclusions are in the manifest. The historical
29,513 A–C illustration checks were not rerun and are not a C-only total.

## Source and rendered gates

Baseline commit: `44e6f54526551a3c931b3591ebc0564b8ecb665c`.
Original SHA-256:
`15151fc6eea24ebc60c29025dbb3a1f5614d9d0dc3f5b2d6a28b2fed5af8c2db`.
Revised SHA-256:
`d07c59dc54a117970dbb5ff5b8fa36e64d6346e8c97fed00bd71eb48be1d447b`.
All 69 labels and their order, 41 formal environments and thirty tagged display
labels are preserved. The environments comprise twelve assertions, thirteen
proofs (including the separate stabilization proof), six definitions, seven
remarks and three examples. Existing inline delimiter syntax is retained
(245 pairs). No unlabelled numbered object, double-dollar display or
placeholder was found.

The new full build has 4,236 pages, 19,734,507 bytes and SHA-256
`71fcbfcf73890e9ec8524ef8480d778010e4566337c13a575e53e89f9d2ff883`.
TeX errors, package warnings, overfull boxes, unresolved references/citations
and rerun requests are zero; 953 inherited bookwide underfull boxes remain.
The initial package-path preflight failed before compilation; the successful
run explicitly used the existing /workspace/.texlive tree, without installation.
All twelve appendix physical pages 3837–3848 and seams 3836/3849 were actually
viewed in four contact sheets. The terminal page is an intentional blank.
Revised prose, the nonzero conditions and both comparison tables fit; no
new layout defect was found.

Post-render references are clean across 425 active files and 12,569 labels.
The unchanged inventory passes at 42 atoms in twelve families, with tiers
0/3/7/15/17. Six checker regression tests passed in the new complete build.
No new independent verifier verdict, exhaustive literature search or
open-problem solution is claimed.

Review PDF: `/workspace/book-completion-drafts/second-reading/AppC_Review_2026-10-04.pdf`.
The whole-book goal continues through D–N and front matter before new research.
