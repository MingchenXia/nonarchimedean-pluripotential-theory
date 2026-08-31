# P14.3 independent source and dependency ledger

Reviewer: p082_independent_reaudit. Date: 2026-08-31. This ledger accompanies INDEPENDENT_EXACT_BYTE_AUDIT.md, not a production receipt.

## Frozen mathematical sources

| Source | Exact local path | SHA-256 |
| --- | --- | --- |
| MP, arXiv:2409.06221v2, 18 September 2025 | /private/tmp/mp24.pdf | 9eb2ea7686a5962ebc11c5eacd23b0cb3dcb081e27ac48292933f291fc82cb23 |
| Same MP version, layout text | /private/tmp/mp24.txt | 0445ccf2c4474b6576a8053d0c7c038ffbd72c2ab27bb3d5704b90dd0e5beb62 |
| DXZ, arXiv:2302.02541v3, 17 July 2024 | /private/tmp/dxz23.pdf | 7fede7c413e396008217a4a4c9638776dbdd7cacff90fdd463bf5ae48220246c |
| Same DXZ version, layout text | /private/tmp/dxz23.txt | 7d5a061d240096139e6302c2b4da2e9c125a8839730fc90909c1488baa446244 |

These are arXiv-version locators, not unverified published-version pagination.

## Exact source interfaces checked

| Source/locator directly read | Interface | Hypothesis or limitation preserved |
| --- | --- | --- |
| MP Sections 1.2--1.3, Definition 1.3.1, pp.7--9 | Ideal-semiring spectrum, pointwise topology, functorial pullback | Compact Hausdorff spectrum includes infinite ideal values; the review also checks the closed-product argument directly |
| MP Lemma 2.1.1 and Definition 2.1.2, pp.11--12 | Coherent prime central ideal is the sum/maximal member of all positive-valued ideals | Actual centre need not be a point or equal a chosen SNC stratum |
| MP Proposition 2.1.6; Remark 2.3.2, pp.12--15 | Birational invariance of valuations and rational divisorial valuations | Valuation-only bijectivity is not asserted on all semivaluations; the new lift uses compactness and density |
| MP Definition 2.3.1, p.15 | Rational nonnegative divisorial multiples | Trivial valuation explicitly included |
| MP Section 2.3.1, Proposition 2.3.4 and Remark 2.3.5, pp.16--17; Appendix B | SNC monomial construction, independence on a connected stratum, rational divisorial realization | Tangential coordinates have weight zero; global ideal evaluation is not pointwise vanishing of coefficients |
| MP Theorem 2.3.6 and its stated proof strategy, pp.18--27 | Ordinary divisorial density | Used only to prove surjectivity of a modification on spectra; no ordered-density theorem is attributed to MP |
| MP Section 2.4, pp.18--19; Section 3.1.1 | Gauss flag-ideal formula and normalized test-configuration simplex | Unnormalized SNC cones on models of X are not confused with the simplex sum b_i w_i=1 on models of X times P1 |
| MP Definition 4.3.1, p.39; Theorem 4.3.8, p.42 | USC of MP potentials and comparison with an arbitrary USC function from divisorial inequalities | The background is Kahler; the comparator need not be MP psh |
| MP Section 5 standing hypotheses and (5.1.1), pp.44--46 | Kahler ray convention s=-log|z| and divisorial Lelong definition | Ordinary-norm potentials and Lelong denominator must be matched |
| MP Theorems 5.1.4, 5.1.7, Section 5.2 and Lemma 5.3.1, pp.46--48 | Ray extension, maximal finite-energy ray correspondence, finite-energy DXZ comparison, value at the trivial valuation | Not a correspondence of unrestricted singular cones |
| DXZ Section 3.4, (43), Theorem 3.17, pp.23--24 | Finite-energy objects are represented by unperturbed test curves; ray correspondence | The subsection explicitly resets to compact Kahler and big class; the audited class is Kahler |
| DXZ Section 3.1, (23)--(25), Proposition 3.1, p.15 | Divisorial ideal/Lelong and Gauss-Legendre formulas | Printed under projectivity; the local full-scope analytic ingredient is checked separately below |

The candidate imports the stated published-source results; this audit is not a fresh reconstruction of every proof in MP's pluripotential theory. In particular no production acceptance of MP's entire text or the live book is asserted.

## Analytic principalization

Primary: Edward Bierstone and Pierre D. Milman, *Canonical desingularization in characteristic zero by blowing up the maximum strata of a local invariant*, [arXiv:alg-geom/9508005v2](https://arxiv.org/abs/alg-geom/9508005v2), 16 August 1995; the published article is Inventiones Mathematicae 128 (1997), 207--302.

The [primary arXiv PDF](https://arxiv.org/pdf/alg-geom/9508005) currently contains the 30-page introductory portion, not the complete published article. Its class list (0.2)(2), p.3, explicitly includes complex analytic spaces. Remark 1.8 and Theorem 1.10, pp.6--7, state finite smooth-centre principalization of a finite-type ideal on quasi-compact M, with normal-crossing total transform. The surrounding convention and algorithm distinguish global finite blowups in the compact case from locally finite constructions in the noncompact case. These exact statements were read through the primary web PDF. Theorem 1.10 is a more precise locator for the classical input than an unspecific reference to Section 13. No claim of having read the omitted full proof or an invented simultaneous-principalization theorem is made. Simultaneous treatment follows by principalizing a finite product, as checked in the audit.

Compact Kahlerness under the smooth-centre blowups is classical; the audit includes the relevant relative-positive-curvature argument. A search located Blanchard's original paper, but its PDF was unavailable to the web reader. It is not listed as a directly read source theorem.

## Nonprojective divisorial comparison interface

Primary: Tamás Darvas and Mingchen Xia, *The closures of test configurations and algebraic singularity types*, Advances in Mathematics 397 (2022), 108198, [university-hosted version-of-record PDF](https://research.chalmers.se/publication/528300/file/528300_Fulltext.pdf), [DOI](https://doi.org/10.1016/j.aim.2022.108198).

Published Lemma 3.14, printed p.39, explicitly assumes only a complex manifold and a nonempty family of nonpositive psh functions. Its proof uses Choquet reduction, finite maxima and semicontinuity of Lelong numbers. It supplies the local supremum/Lelong interchange used in the divisorial Gauss-Legendre calculation. The preceding Proposition 3.13 has the paper's projective setting and is not itself quoted as a nonprojective theorem. The audit spells out the local potential/linear shift and generic-divisor passage needed to justify the Kahler interface. This is a source-precision clarification of the existing finite-energy correspondence, not a new all-point comparison input.

The integer multiplier-ideal/Lelong asymptotic and perturbation invariance are the exact interfaces already recorded in frozen Chapter 71 and frozen P14.2: ordinary/squared-norm conversion is applied to the potential and its logarithmic denominator together. Published DX22 Proposition 2.18(ii), in the arbitrary compact-Kahler Section 2.4, is the ideal-preservation input. The P14.3 proof uses equality of ideals, not only equality of their divisorial values, when choosing a perturbation component.

## Conditional predecessor and manuscript interface

All following paths have root `/private/tmp/nappt_p071_20260827`.

| Input | SHA-256 | Use |
| --- | --- | --- |
| manuscript/editorial/solver_dossiers_20260831/p142_raw_transform_usc_research_20260831/statement.tex | 488868dc2b2d1d62b23864970f8bf36acc0a6c7c85d27eaf66e6a9ed7120c949 | USC of the literal raw formula on all semivaluations; reread in full |
| Same P14.2 directory, proof.tex | bf991c724e138626fbd8fcd4fc6f613d7979f3bf75a3614c569a1ff3c7d21e21 | Monotone-level finite-grid argument and exact perturbation interface; reread in full |
| Same P14.2 directory, MANIFEST.json | c677e7a289d9b957d2269cb7b68da4dfcfa89faa4a761a15e8fd8b6dc65e5a87 | Exact predecessor binding; production remains pending |
| manuscript/parts/part6/ch71_pseudoeffective_mp_dxz.tex | c6bc0fb2d6813ed2ca4c6c37df4a7b75ef733a0cae62d97400df78fe087327e2 | Ideal formula, norm convention, finite-energy theorem at (71.39)--(71.40); not whole-chapter endorsement |
| manuscript/parts/part6/ch72_major_open_problems.tex | 6e671da09d50cc7becd553d319a0cbce0fe6c3622ac77a491550411a32c69b8c | Frozen context/preservation only; no retirement or live status change |

## Visual and access record

The PDF skill was used for read-only source QA. Complete MP PDF pages 11, 12, 16, 17, 42, 46, 47, 48 and DXZ pages 15, 23, 24 were locally rendered and visually inspected. They confirm the central-ideal construction, tangent/transverse distinction, rational-weight clause, comparison direction, finite-energy boundary and displayed normalizations. No typesetting inference substitutes for the mathematical checks.

BM and DX22 relevant primary statements were read through the web PDF text. A DX22 web screenshot returned a cache miss. Ordinary shell retrieval of both source PDFs failed at DNS resolution and was not retried or escalated; no local copy/hash or successful visual QA for those two PDFs is claimed. The candidate has only a five-page draft-mode TeX check and no PDF, as stated in its own validation record.

All authored audit artifacts are isolated. No source/candidate/live edits, production calls, approval-gate workaround, novelty claim, or change of open-problem status occurred.
