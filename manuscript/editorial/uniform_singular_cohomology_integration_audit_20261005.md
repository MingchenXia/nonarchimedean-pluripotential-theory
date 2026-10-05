# Singular cohomology of the ordinary Bergman variety, 5 October 2026

Appendix G now works out a second known `U_(3,4)` example: rational
singular cohomology of the smooth complex toric variety defined by the
ordinary Bergman fan in `Z^4/Z(1,1,1,1)`. This nonproper variety has complex
dimension three. Its odd cohomology and weights distinguish it from the
ordinary Chow ring, the augmented Chow ring and the previously described
intersection-cohomology module. Appendix L records the source boundaries.

## Controlling sources and acquisition

Binder, *The singular cohomology ring of a uniform matroid: combinatorics
and Lefschetz properties*, [arXiv:2606.07490v1](https://arxiv.org/abs/2606.07490v1),
submitted 5 June 2026, supplies Definitions 2.1/2.3/2.4 and Example 3.20.
The acquired frozen PDF has 21 pages, 369,204 bytes and SHA-256
`f4999ff18bce7e13ba90c753863921042cbca9fe9e63fbbe44254e38d43b5cf8`.
Its full extracted text was read in successful newline ranges 1--180,
181--360, 361--540, 541--720, 721--900, 901--1080 and 1081--1210.
Python `splitlines()` additionally splits 21 formfeeds and counts 1,231
lines. Eight actual pages were inspected: physical/printed 1, 2, 6--8,
12, 18 and 20. These cover the standing category, Koszul and weight
conventions, named example, uniform tables and Lefschetz statement/proof.
The full reading does not constitute an independent general proof receipt.

Binder, *The singular cohomology ring of a matroid*,
[arXiv:2412.05732v2](https://arxiv.org/abs/2412.05732v2), revised 18 March
2026, supplies the finite square-free subcomplex, Definition A.4 and
Lemma A.5. The frozen PDF has 35 pages, 490,259 bytes and SHA-256
`f9167e4edf09ee5a254a1ff4a95348b63f965e44397df4b7cb822e1865bf62f8`.
The successful targeted reading is lines 1473--1628, including the full
Definition A.4 and proof of Lemma A.5. Actual pages 30--31 were inspected.
No full reading of this entire base paper is claimed. Its rewritten
March version is distinguished from the December 2024 first version.

Franz--Fu, *Cohomology of smooth toric varieties: naturality*, Journal of
Pure and Applied Algebra 228(6) (2024), 107590,
[DOI 10.1016/j.jpaa.2023.107590](https://doi.org/10.1016/j.jpaa.2023.107590),
supplies the canonical rational Tor product and its naturality in
Theorems 1.1/1.2. The acquired 38-page institutional article copy is
`https://bimsa.net/doc/publication/3264.pdf`, 664,669 bytes, SHA-256
`84218ee3f8b500ce12daecdd58bec0ce7787b381483bac736a2319ca30ffb39d`.
The first page records publication metadata and 19 December 2023 as its
online date. Exact publisher-file identity was not independently acquired.
Successful targeted readings are lines 1--190 and 2072--2235, covering
the rational statements and §§7.3--7.4. Actual pages 2, 35--37 were viewed.
The coefficient condition that two be invertible is retained; no integral
untwisted ring extension is inferred. The cited earlier Franz inputs are
identified dependencies, not freshly read full papers in this checkpoint.

Weber, *Weights in the cohomology of toric varieties*, Central European
Journal of Mathematics 2(3) (2004), 478--492,
[DOI 10.2478/BF02475240](https://doi.org/10.2478/BF02475240), supplies
the smooth toric weight and power-map conventions in §§3.2 and 5.
The acquired 16-page author copy is
`https://www.mimuw.edu.pl/~aweber/ps/tv2.pdf`, 192,694 bytes, SHA-256
`187a5df8c7f879eb71136cd61ad6ec0b87961ffcb26dc94495cfc6e636bf7d01`.
It was read in full in successful newline ranges 1--190, 191--380,
381--570 and 571--743 (759 Python split lines including formfeeds).
Actual author-copy pages 4, 6, 11 and 12 were viewed. Its pagination and
result numbering are not asserted to match the 15-page published article;
the book uses section locators. Direct publisher acquisition returned
HTTP 202 with a non-PDF response, recorded as failure. No publisher-file
identity or complete published-text comparison is claimed.

In total eighteen actual primary pages were inspected. Full versus
targeted reading and author/institutional versus publisher acquisition
are recorded separately. Further external dependencies were not freshly
read in full.

## Exact finite Koszul calculation

The checker uses ten proper nonempty flat variables and the ordinary
Stanley--Reisner ideal. Its character basis is
`m_i=ell_i-ell_4`, `i=1,2,3`, and it constructs the full polynomial
Koszul differential in internal degrees zero through six. Every computed
differential squares to zero. Source-named cycles are closed, independent
modulo boundaries and have the required number in each nonzero bidegree.
The nonzero Koszul dimensions and their topological grading are:

| Homological i | Internal j | Dimension | Cohomological 2j-i | Weight 2j |
| --- | --- | --- | --- | --- |
| 0 | 0 | 1 | 0 | 0 |
| 0 | 1 | 7 | 2 | 2 |
| 0 | 2 | 1 | 4 | 4 |
| 1 | 2 | 6 | 3 | 4 |
| 1 | 3 | 3 | 5 | 6 |

A separate construction applies Definition A.4's square-free condition.
For a monomial supported on a cone, the exterior coefficient must have
zero contraction by each ray of the support. The checker builds these
spaces exactly, verifies the subcomplex inclusion and ranks, and checks
the named cycles lie in them. Its complete nonzero degrees are:

| Internal j | Chain dimensions i=0,1,2,3 | Differential ranks i=1,2,3 | Homology i=0,1,2,3 |
| --- | --- | --- | --- |
| 0 | (1,0,0,0) | (0,0,0) | (1,0,0,0) |
| 1 | (10,3,0,0) | (3,0,0) | (7,0,0,0) |
| 2 | (12,20,3,0) | (11,3,0) | (1,6,0,0) |
| 3 | (0,12,10,1) | (0,9,1) | (0,3,0,0) |

Square-free supports have at most two independent rays in a
three-dimensional lattice. A support of size p permits exterior degree
at most `3-p`, so internal degree is at most three. This bound concerns
the specified finite complex. Its global quasi-isomorphism to the
polynomial complex remains the identified known Lemma A.5 input; no new
general quasi-isomorphism is proved by finite rank calculations.

The known ring identification over Q and the source weight convention
give Poincaré polynomial `1+7t^2+6t^3+t^4+3t^5` and Hodge--Poincaré
polynomial `1+7x+x^2+6wx^2+3wx^3`. On the specified class
`eta=3 sum_singleton x_i+4 sum_pair x_ij`, exact ranks are one for
`H^0 -> H^2`, `H^0 -> H^4` by its square, and `H^2 -> H^4`, and three
for `H^3 -> H^5`. These are finite class calculations, not a general
Lefschetz proof or a computation for arbitrary classes.

## Weight clause excluded and follow-up boundaries

After formula 5.8, the author-copy p. 12 states `H^k(C_l)=0 for k>l`.
That literal inequality conflicts with its own Example 3.5/5.10,
where `H^3` has weight four (`l=2`); even projective pure degree-two
cohomology conflicts with it. The correct smooth weight range has
`l<=k<=2l`. The inconsistent clause is excluded, without claiming a
counterexample to Theorem 5.5 or that the final published article has the
same text. The book uses the weight/power-map description and the
explicit Koszul grading, not this auxiliary vanishing paragraph.

Naturality makes the toric q-power map act by `q^j` in Koszul internal
degree j: each polynomial generator and character is multiplied by q.
The smooth toric weight convention of §3.2 assigns this eigenvalue
weight `2j`. This records the normalization underlying the displayed
weight formula. No ring or weight identification with Lee's different
compactification is inferred. General matroid Lefschetz questions remain
follow-up directions. A fresh search found Binder--Vecchi,
arXiv:2609.15946v1, submitted 14 September 2026, reporting the June
uniform refined real-rootedness Conjecture 5.8 proved and further
augmented-fan results. It is queued for complete primary-source review;
this checkpoint makes no abstract-based theorem import or current
negative literature claim. No new atom is marked solved or added to
the active catalogue on the strength of these finite examples.

## Admission and release scope

This is an ordinary import of known definitions, algebraic identifications
and a worked named example under the repository verification protocol.
There is no new formal result/proof environment, original general repair,
independent production-model call or extended historical receipt.
The baseline is work commit `5340030710b7d2d7f321ace78570d5eb7c8c66d1`.
Appendices G and L are the only changed members of the 425-input closure.
Their 31 existing formal blocks and old labels are byte-preserved. The
source checks pass with 12,606 unique labels, 591 bibliography keys and
292 cited keys; all 425 active inputs resolve. The full book compiles to
4,269 pages with no TeX errors, package or pdfTeX warnings, overfull boxes,
unresolved references/citations or rerun requests. The 954 underfull boxes
are unchanged from the preceding checkpoint. All 738 accepted index entries,
21,476 named destinations and 46,299 internal links pass their checks.
Actual release pages 64, 66, 3913--3916, 4036--4037, 4250--4251,
4258--4259, 4263 and 4268 were inspected for contents, the example and its
neighboring text, provenance, index entries and bibliography. All 108
protected inputs, all 42 complete statuses and catalogue source/PDF
retain their previous bytes. No fresh whole-book rereading is claimed
at this checkpoint. Older dated exports retain their scope and bytes.
Author updates are fetched and inspected before ordinary publication
to `work`; main remains unchanged and no force push is used.
