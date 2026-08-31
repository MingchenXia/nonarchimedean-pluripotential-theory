# Source matrix for the exact Chapter 20/21 repair review

Date: 2026-08-31. Reviewer: /root/p082_independent_reaudit.
Scope and non-fresh provenance are in ORIGINAL_REVISION_AUDIT.md.

## Primary version

Boucksom--Favre--Jonsson, Singular semipositive metrics in non-Archimedean
geometry; published citation BFJ16, Journal of Algebraic Geometry 25(1)
(2016), 77--139, DOI https://doi.org/10.1090/jag/656.

The exact inspected primary source is the 49-page arXiv PDF retrieved
from https://arxiv.org/pdf/1201.0187. Its margin states 1201.0187v2,
21 January 2014; its internal title-page date states 22 October 2018.
All source locators below refer to this version, not assumed journal
pagination. Mathematical statements, proofs and coefficient conventions
were inspected directly, not inferred from the citation key alone.

- PDF: /private/tmp/BFJ_singular_1201.0187_audit_20260831.pdf
  SHA256 8b684713055b9147de0d3379ad925c58f031bafe10a77e769a2791cdaa128270.
- pdftotext -layout extraction:
  /private/tmp/BFJ_singular_1201.0187_audit_20260831.txt
  SHA256 df3fa71656240742234907514956389d2f2533e20bb89cd877bd235a922e5f1f.

Primary PDF pages 10,15,16,23,24,25,33 were directly visually checked in
the preceding diagnostic audit against these identical source bytes.
This review reread the relevant exact local text; it did not claim a new
visual inspection of an assembled chapter PDF.

| Primary source | Interface used | Scope restriction / check |
| --- | --- | --- |
| Sections 1.1 and 2.4, pp. 6 and 9 | Complete DVR, residue characteristic zero; smooth connected projective generic fibre | No algebraically closed valued field is required |
| Definition 1.3, p. 7 | Finite-dimensional relative real numerical classes, closed nef cone | Theta remains real |
| Lemma 1.4 and Corollary 1.5, pp. 7--8 | Ample real generic bundle admits an ample extension on sufficiently high models | Fresh extension on the final model, not ampleness of an arbitrary pullback |
| Definition 2.1, p. 10 | D(X)=D_Q, with separately named D_Z and D_R | No real vector-lattice convention |
| Proposition 2.2, pp. 10--11 | Ideal representation and rational/integral model maximum membership | Establish membership before closedness arguments |
| Monomial formulas (3.2)--(3.4), pp. 14--15; Proposition 3.12 and Corollary 3.13 first assertion, pp. 15--16 | Rational cuts on the fixed unit edge via integral exponents and ideal logarithms | Bare piecewise affineness is insufficient; no use of the printed converse in Corollary 3.13 |
| Proposition 5.2, p. 23, with proof | Positive representative on a cofinal set of common models | Requires ample generic theta; proof constructs a real vertical divisor |
| Definition 5.5 and Lemma 5.6, pp. 23--24 | Rational theta-nef models; generated twisted ideal gives nefness | Theta can be arbitrary real; line bundle after denominator clearing is genuine |
| Lemma 5.7, p. 24 | Relative-nef model functions approximated by normalized ideal logarithms | Exact locator replacing inherited Lemma 5.3 citation |
| Proposition 5.8, pp. 24--25 | Rational convexity and finite maximum stability, arbitrary real theta | No ample generic hypothesis; open ample cone is used on the auxiliary fixed model |
| Proposition 5.9, p. 25 | Face convexity and retraction inequality for rational models | Real case supplied by fixed-form density under ample generic hypothesis |
| Definition 7.1 and Proposition 7.4, pp. 32--33 | Full PSH via skeletal uniform closure; real convexity and maxima | Full PSH maximum is not D_R maximum closure |

## Book-side interfaces read directly

The exact chapter hashes and parent path are recorded in the original
report and the author's manifest. These additional interfaces were read
in context, not merely checked for label existence.

| Book interface | Review |
| --- | --- |
| eq:ch20-model-functions | Finite real span of rational vertical Cartier functions, not uniform/max closure |
| eq:ch20-sign and eq:ch20-ddc-constant | Positive divisor functions; special-fibre divisor gives constant one and zero differential |
| lem:ch20-special-fibre-test | Nef plus ample and finite-dimensional numerical spaces; stale denial of openness noted separately |
| prop:ch20-semipositive-well-defined | Nefness preserves and reflects through domination; supports fixed-model limit |
| prop:ch20-positive-representative | Cofinal common determination with ample correction |
| prop:skeleton-model-pa in manuscript/parts/part1/ch05_skeleta.tex | Rational piecewise affine restriction; direct primary monomial argument additionally checks the required rational cuts |
| def:ch21-bfj-psh and eq:ch21-hypotheses | Real approximation convention and ample generic reference class |
| lem:ch21-model-skeletal-properties | Changed real approximation paragraph only; distinct curve retraction work excluded |
| thm:ch21-stability maximum clause | Uniform rational replacement at exactly theta1, then rational max |
| thm:ch20-model-envelope items 2--8 | Retain semipositive reference only; no rational-family reference-change shortcut |

Additional read inputs:

- manuscript/parts/part1/ch05_skeleta.tex:
  76c47909486f66289199e54369ecb5ba0c8bc4018efa205f534d1e44e25d318d.
- manuscript/bibliography/ComplexGeometry.bib:
  01803f1af91d105f41bd1d85d11e0b66e5b5caaa085c9c2806174b5cc75203d6.

The bibliography entry supplies publication metadata; theorem numbering
was checked against the exact primary version above. No broad arbitrary-
field, nef-envelope, CLD comparison, or degree-zero approximation claim
is imported from these sources.
