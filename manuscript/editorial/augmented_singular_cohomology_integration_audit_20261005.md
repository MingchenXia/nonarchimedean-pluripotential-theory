# Uniform real-rootedness and augmentation, 5 October 2026

Appendix G continues the ordinary toric singular-cohomology example with
the September 2026 uniform real-rootedness theorem and the distinction
between ordinary, augmented and modified augmented Bergman fans.
Appendix L records the identified known inputs and excluded auxiliary
clauses. This is a source-attributed literature update, not admission of
an original general theorem or an independent model verification receipt.

## Controlling September source

Binder--Vecchi, *Augmented singular cohomology, uniform matroids, and
real-rootedness*, [arXiv:2609.15946v1](https://arxiv.org/abs/2609.15946v1),
submitted 14 September 2026, has 27 pages, 495,542 bytes and SHA-256
`587d60cc21f052dd677a46583cd574dbd49fe3b8aedac808891601634d70c70e`.
The full extracted text was read in successful newline ranges 1--180,
181--360, 361--540, 541--720, 721--900, 901--1080, 1081--1260,
1261--1440 and 1441--1515. Python splits 27 additional formfeeds and
counts 1,542 lines. The extraction reports a font-type mismatch; actual
pages confirm the mathematical symbols and the distinction between
underlined, augmented and modified notation. Eighteen actual source pages
were inspected: 1, 3--6, 9, 11--12, 18--27.

Known imports are Theorems 1.3/1.4/1.6, Definition 4.1, Proposition 6.6,
equation (7), the explicit positive-basis polynomial in the proof of
Theorem 1.4, and Example 7.5. Their setting is rational singular cohomology
of specified smooth complex toric varieties. Ordinary fans use
`Z^n/Z(1,...,1)`; augmented and modified fans use `Z^n`. Their toric
varieties have complex dimensions n-1 and n respectively, regardless of
the dimension of the fan's maximal cones. The modified fan contains the
full positive orthant and is nonpure for r<n. Parameters are
`1<=r<=n`, `0<=i<=n-r`; all displayed positive-degree formulas retain
`1<=i<=n-r`. No rank-zero extension is imported.

Theorem 1.4 resolves the June uniform refined real-rootedness Conjecture
5.8. The September paper's Conjecture 1.5 asks for the same property for
arbitrary loopless matroids; it is not promoted to a theorem. The modified
real-rootedness and weight-graded Lefschetz conclusions concern that
different fan. They do not identify its full singular cohomology with an
intersection-cohomology module or a tropical compactification. No new
active Chapter 72 atom is added or marked solved.

## Dependency acquisition and reading boundaries

Brändén--Solus, *Symmetric decompositions and real-rootedness*, IMRN
2021(10), 7764--7798,
[DOI 10.1093/imrn/rnz059](https://doi.org/10.1093/imrn/rnz059), supplies
Corollary 3.7. Its frozen [arXiv v3](https://arxiv.org/abs/1808.04141v3),
revised 12 January 2020, has 26 pages, 342,756 bytes and SHA-256
`713bb325cad4b69cdb620a302e0492980d249fa1a8582ee72935b21debda69ab`.
Lines 537--690 were read, covering §3.2's operator and criterion with its
proof. Actual pages 11--14 were viewed. The positivity condition is a
nonnegative combination of `x^k(1+x)^(a-k)` for a fixed a; monomial
coefficient positivity alone does not give that hypothesis. General
stability-classification inputs remain identified external dependencies,
not fresh full readings or an independent general proof certificate.

Athanasiadis, *On the real-rootedness of the Eulerian transformation*,
JLMS 111(2) (2025), e70083,
[DOI 10.1112/jlms.70083](https://doi.org/10.1112/jlms.70083), supplies
Theorem 1.1. The frozen [arXiv v5](https://arxiv.org/abs/2302.00754v5),
revised 18 February 2025 and marked final, has 21 pages, 287,788 bytes and
SHA-256 `32eff719541150ee1da7a2c9f366057414799caf1d1f836c675284abcdf4a9cc`.
Its 21-page layout is distinguished from the published 23-page record.
Successful readings are 1--100, 101--135 and 238--505, including the
positive-basis hypothesis, normalization `A°(1)=1`, `A°(x^k)=x A_k(x)`
for k>=1, and the §3 proof. Actual pages 2, 8--10 were viewed. The publisher
page returned HTTP 403 to the web tool; final publisher-file identity is
not asserted. Other sections were not read in full.

Brändén--Vecchi, *Chow polynomials of uniform matroids are real-rooted*,
Combinatorial Theory 6(1) (2026), article 15,
[DOI 10.5070/C66165702](https://doi.org/10.5070/C66165702), supplies
Theorem 1.1 for ordinary degree zero. The publisher-hosted eleven-page
article was acquired from eScholarship's content URL, 339,855 bytes,
SHA-256 `f02e860c91482e3347ac44ca04e217446ac28d39478af61c6a9e105885eb7ccc`.
The first page states publication on 20 April 2026. Its complete text was
read in ranges 1--180, 181--360 and 361--513. Actual pages 1 and 7--9 were
viewed. Its different augmented alternative argument is excluded below.
Its literal Möbius-function and maximal-poset initial-value passages are
not additional inputs of this update.

Ferroni--Matherne--Stevens--Vecchi, *Hilbert--Poincaré series of matroid
Chow rings and intersection cohomology*, Advances in Mathematics 449
(2024), 109733,
[DOI 10.1016/j.aim.2024.109733](https://doi.org/10.1016/j.aim.2024.109733),
supplies the identified augmented degree-zero Theorem 1.10. The attempted
institutional final published PDF returned HTTP 403, recorded as failure.
The frozen [arXiv v3](https://arxiv.org/abs/2212.03190v3), revised 4 June
2024 and marked final accepted, has 43 pages, 635,806 bytes and SHA-256
`33edfb888c22c93257bae69d0b9fa0c0d647b467bdd268ae6299e3bffd115f0b`.
Its layout is distinguished from the published 55-page article. Targeted
readings 295--315 and 1890--1985 check Theorem 1.10 and §5.1's identified
Haglund--Zhang route. Actual pages 1, 6, 31--32 were viewed. Appendix B and
the external Haglund--Zhang proof were not freshly read in full. This is
an import of the known theorem, not an independent proof certification.

There are 34 selected actual primary-page views in this checkpoint:
18 controlling pages and 16 dependency pages. Full versus targeted
reading and acquired edition versus publication metadata are recorded
separately. No complete image-by-image review of all sources is claimed.

## Exact finite checks and excluded clauses

The standard-library checker uses integer coefficient polynomials and
exact Fraction arithmetic for square-free reduction and Sturm chains.
It verifies Eulerian and derangement definitions by direct permutation
enumeration through n=7. For all 286 triples with `2<=n<=12`,
`1<=r<n`, `1<=i<=n-r`, it compares the ordinary binomial/derangement
formula with the reversed positive-basis deranged transform. It compares
the modified Eulerian formula with both the reversed positive-basis
Eulerian transform from Lemma 7.6 and the contraction sum. Exact Sturm
counts give real roots for both ordinary and modified polynomials.

In 56 of those triples with n<=7, a separate enumeration builds every
strict subset flag ending at a hyperplane, tests the weak covering
condition and successor-wedge admissibility, and counts actual basis
elements by row degree. Its dimensions agree with the ordinary formula.
Independent enumeration of disjoint basis/wedge sets with
`min J < min B` recovers the augmentation coefficient. A separate
degree-zero calculation covers 78 rank/cardinality pairs through n=12,
including the Boolean boundary, and checks ordinary and augmented Chow
real-rootedness by Sturm counts. These are finite polynomial/basis checks;
the general cohomological identifications remain known source inputs.

The known Example 7.5 polynomials are reproduced exactly:
`H_aug(U_3,8,i=4)=140x+372x²+259x³`, with discriminant -6656 after
removing x, and
`H_aug(U_4,30,i=24)=1319500x+9083815x²+8789785x³+8811999x⁴`.
The latter is not unimodal. Its independence contribution is 7,634,250;
removing it gives the modified last coefficient 1,177,749. Exact root
counts also check both named modified polynomials.

The September source's Definition 6.1 says W0,i=W1,i. For U3,4 with i=1,
direct enumeration gives both cardinalities as three, while the literal
binomial count displayed in the proof of Lemma 6.2 gives eight at j=1.
Lemma 6.4 and the proof of Theorem 1.4 exclude j=1 from their cardinality
comparison. Since d1=0, that auxiliary coefficient disappears from the
polynomial formula. The update uses the polynomial identity and this
explicit exclusion, not the inconsistent cardinality clause. No
counterexample to the real-rootedness theorem is claimed.

The published Brändén--Vecchi p. 8 alternative augmented proof defines
`A_n,k=sum_(j=0)^(k-1) binom(n,j) A_j` with the p. 4 normalization
`A0=A1=1` and writes `g_n,k=x g_n,k-1+A_n,k`. At n=4,k=2 this literal
recurrence yields `5+x+x²`, while the known augmented Chow polynomial
is `1+5x+x²`. Its Eulerian-transform/interlacing normalization is therefore
not imported as an augmented proof input. The book instead identifies
FMSV Theorem 1.10 and uses Athanasiadis's explicit shifted normalization
for positive homological degrees. This diagnoses the displayed auxiliary
recurrence, without refuting either main uniform real-rootedness theorem
or claiming an independently admitted general repair.

## Admission and release scope

The baseline is work commit `deecca1edf20f942f3341fc5cc991dba84af7e98`.
Only Appendices G and L change within the 425-input active closure.
Existing formal blocks and labels, all 108 protected Appendix M--N inputs,
all 42 complete inventory statuses and the catalogue source/PDF are
preserved. This update is an ordinary identified known-result import under
the repository verification protocol. No original theorem, model call or
historical verifier receipt is admitted or extended. General loopless
real-rootedness, the Siu assertion and pseudoeffective closure retain
their previous scope. The source checks pass with 12,608 unique labels,
596 bibliography keys and 297 cited keys. All 31 existing formal blocks
in the two changed appendices are byte-preserved. The full book has
4,269 pages and compiles with zero TeX errors, package/pdfTeX warnings,
unresolved references/citations, rerun requests or overfull boxes. Its
954 underfull diagnostics are unchanged. All 740 accepted index entries,
21,483 named destinations and 46,325 internal links pass their checks.
Actual release pages 64, 66, 3914--3917, 4037--4038, 4251, 4253--4254,
4257, 4260, 4263 and 4268--4269 were inspected for contents, the update
and neighboring example/comparison, provenance, index and bibliography.
These sixteen actual-page views precede freezing the new exports. Older
dated artifacts remain immutable; no fresh whole-book rereading or fresh
isolated source-archive build is claimed at this checkpoint.
