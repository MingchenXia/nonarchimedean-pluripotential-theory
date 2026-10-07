# Chern flow, Chern moments, and tropical generation: source review

Date: 7 October 2026. Baseline `work`
`01919039a1cfc48806537c7683a64b1723ba7736`; observed `main`
`00957114db21b627e97369563032ceda9cea09c7`.

This source-only checkpoint reads **182 distinct source/page pairs in 94
individually displayed matching sheets**, with complete selected text and
sequential notes. Three PDFs are read completely; eight others partially.
The principal source is **Khai-Hoan Nguyen-Dang and Zhenpeng Wang**, *Chern
flow and Chern moment algebras*, arXiv:2609.02850v4, 13 September 2026,
74 pages. Both authors belong to the main paper. Acquisition and preparation
records initially give zero reading credit; the separately frozen actual
reading receipts record the completed work.

The proposed reader path connects Appendix D's factorial normalization to
Appendix F's generated Chern intersection models, then to actual quotient
flag towers, full Chern moment algebras, and Appendix G's matroid geometry.
It distinguishes exact rational volume realization, Lorentzianity, Hodge
theory of a full moment algebra, and Hodge theory of a smaller apolar
specialization. The last distinction has an explicit toric quartic example.

The current **4,535-page book** is unchanged. All 425 active TeX inputs,
both bibliographies, 108 protected inputs, 119 prior frozen manifests and
202 prior exports are byte preserved. The native 86-page catalogue and
its open editor remain untouched. No new compilation or whole-book reread
is claimed. The canonical 42-atom/12-problem inventory is unchanged;
the general BJ22 Theorem 6.21 critical Siu-division/envelope input stays
open, and the LPWZ elliptic-density candidate stays unverified. No original
result or independent-model verification receipt is admitted. The user
has expressly authorized evidence uploads to the existing private GitHub
repository; uploads do not change repository visibility.

## Controlling editions and actual reading

Page numbers are physical PDF pages. Hashes, acquisition URLs, full
reading notes and matching images are pinned in the companion evidence.
An unversioned download is identified by its returned stamp and bytes,
not assumed to be a published or latest edition.

| Source | Pages actually read | Whole PDF? |
| --- | --- | --- |
| Nguyen-Dang--Wang, 2609.02850v4, 13 September 2026 | 1--74 | yes |
| Amini--Huh--Larson, 2511.02026v1, 3 November 2025 | 1--5, 14--16, 24--28 of 39 | no |
| Larson--Partida, 2604.21925v1, 23 April 2026 | 1--19 | yes |
| Kaveh--Manon, 2405.03576v2, 14 August 2024 | 1--4, 9--17, 19--21, 23--25 of 38 | no |
| Berget--Eur--Spink--Tseng, 2103.08021v4, 14 April 2023 | 1--3, 11--17 of 71 | no |
| Ardila, math/0404370v1, 20 April 2004 | 1--8 of 13 | no |
| Buciumas--Scrimshaw--Weber, 1908.07364v2, 31 March 2020 | 1--3, 5--7 of 23 | no |
| Monical--Tokcan--Yong, returned 1703.02583v2, 10 March 2017 | 1--3, 14--17, 20--23 of 30 | no |
| Mészáros--Setiabrata--St. Dizier, returned 2201.09452v1, 24 January 2022 | 1--3 of 15 | no |
| Huh, returned 1008.4749v3, 10 February 2012 | 1--2, 15--18 of 21 | no |
| Cattani, 0707.1352v2, 19 February 2008 | 1--13 | yes |

The primary reading has 74 pages/37 images; the initial dependency
selection has 90 pages/47 images; the disjoint additional selection has
18 pages/10 images. The latter adds AHL Proposition 2.10's proof, KM's
flag convention, and the complete Cattani paper. Reading a printed proof
does not recursively certify its cited foundations. Existing complete
GHMSW and Jiang--Li readings from the preceding volume/Richardson
checkpoint are reused only as frozen source evidence, with **zero fresh
page credit** here.

Early primary notes 19--21 and 24 used the incorrect shorthand “AHK” for
reference [26]. Primary note 37 explicitly corrects it to
**Amini--Huh--Larson**, 2511.02026v1, §4.3 Lemma 4.6, physical p.26.
The earlier notes are preserved; no book edit was made from that shorthand.

## Realization, normalization, and tower gates

**C01 -- Exact realization retains the field and rational scale.** Primary
§§1.1, 2.2--2.3, pp.3--5, 11--15, defines `RV_k` using integral
projective varieties over the original field, semiample Cartier divisors,
`1/d!` top intersections and a nonnegative rational scalar. Zero is
included. Coefficients live in rational polynomial algebra independently
of geometric characteristic; no factorial is inverted in the geometric
field. Complex Hodge arguments and characteristic-zero smooth resolution
are separate from the arbitrary-field incidence proof.

**C02 -- Ordinary operators and divided powers have separate roles.**
Definitions in §§2.1, 3.1 and Appendix A use
`partial_i f=(f-s_i f)/(x_i-x_(i+1))`,
`K_i^z f=partial_i[x_i(x_(i+1)+z)f]`,
`bar K_i^z=K_i^z-z id`, and
`D_i^z f=partial_i[(x_(i+1)+z)f]`.
The reciprocal row operator is
`Gamma_i^(epsilon,z) f=partial_i[x_(i+1)^epsilon(x_i+z)f]`.
Reduced words act rightmost first. BSW pp.6--7 confirms the operator,
braid, atom and stabilizer conventions, but its full vertex-model proof
was not selected. No individual divided-difference operator is asserted
to preserve all volume or SNP polynomials.

**C03 -- Finite complement is not unqualified exponent reversal.**
For a box `m`, `D_m` acts on `x^[alpha]` by `x^[m-alpha]`, whereas raw
reciprocity acts on ordinary monomials. `D_m N(f)=N(R_m f)`. Successive
operators change the homogenizing cap; Appendix A retains those changes
and variable reversal. A common cap can be enlarged through divided-power
translation. The proof does not establish arbitrary finite-complement
closure for volume polynomials.

**C04 -- Incidence avoids unsupported irreducibility.** Proposition 2.8,
pp.13--14, starts with an integral projective source, a generated bundle
`V` and a generating sequence with positive-rank kernel `K`. The integral
source `P(K^dual)` has generated tautological class `H`; its fibre-top
pushforward is `c_top(V)`. An ordinary derivative of order `M=dim P(W^dual)`
of the normalized intersection polynomial, followed by setting that
variable to zero, extracts the finite-box normalized class with **no extra
`M!`**. A general zero scheme of a generated bundle need not be integral;
the proof does not assume it is. Smooth final realization uses the
characteristic-zero refinement of the separately attributed volume input.

**C05 -- Total Chern intersections have a generated kernel-dual model.**
Proposition 2.10, pp.14--15, uses products of quotient projective bundles
of globally generated evaluation-kernel duals. The inverse Chern relation
and fibre-top extraction give `N(x^b T)`, and differentiation removes the
padding. The construction is arbitrary-field intersection theory, rather
than an assertion that every Chern class has all Hodge signs on the original
source.

**C06 -- Generation occurs for whole rows, not individual roots.**
§3, pp.16--22, modifies an actual quotient flag through rank-two projective
bundles. Prefixes remain generated quotients of the pulled-back original
bundle; kernel lines and individual quotient roots need not be generated.
Canonical inverse-Lehmer rows have decreasing starting indices. At row
completion a generated split tail surjects onto the whole row bundle.
Atoms instead use generated co-row bundles at row start and the old upper
roots at their correct time. The Gysin divided difference is polynomial
and does not invert a difference of divisor classes.

**C07 -- Rank and creation time are both essential.** Definitions 4.3--4.4,
pp.23--24, identify passive pullbacks only. At step `t` of colour `i_t`,
the edge runs from the newly created rank-`i_t` prefix to the existing
rank-`i_t+1` prefix. Equal ranks do not identify unrelated bundles. Proposition
4.1, pp.22--23, sums actual exact-sequence relations in `K^0`: nonnegative
incoming-minus-outgoing multiplicities produce a generated direct sum of
vertex bundles with the required top Chern product. The general identity
requires no acyclicity; equal rank equations alone do not establish it.

**C08 -- Terminal supply is a proved condition, not optional padding.**
Lemma 4.6, p.25, gives the all-kernel canonical-row criterion
`d_j >= 1{m_j>0 and L_j>L_(j-1)}` for `j<n`; rank `n` has no outgoing
edge. Staircase differences always suffice. Theorem 4.7, pp.25--26,
constructs the generated packet bundle only with the actual nonnegative
divergence. Appendix B's interval inequalities distinguish internal states
from final states; adding terminal supply cannot repair an internal deficit.
The general profile preserves actual creation states and whole rows.

**C09 -- Treat a complete packet before extracting layers.** §5,
pp.27--37, and Appendix A, p.59, convert Lascoux, atom and Grothendieck
packets through cap-aware reciprocity. For a homogeneous packet
`Q=sum P_k z^(L-k)`, ordinary differentiation gives
`partial_z^(L-k) N(Q)|_(z=0)=N(P_k)`. Removing padding uses a derivative
without this specialization. Nonzero minimal padding uses the actual
maximum excess; zero packets do not acquire an undefined maximum.
Remark 5.11's `u=312` obstruction rules out deleting common row factors
and organizing the remaining kernels into unrooted paths first.

**C10 -- Support conclusions retain their exact families.** Corollaries
5.12--5.14, pp.35--37, give attributed normalized volume/Lorentzian and
polymatroid support conclusions for the ordinary families covered by the
packet construction. M-natural convexity gives augmentation and interval
closure for ordinary inhomogeneous supports. MTY v2 has ordinary
Schubert SNP at 5.1, Grothendieck at 5.5, Lascoux at 5.6, atom at 5.7,
key at 3.10 and Demazure atom at 3.14. Its double-Schubert 5.2 and stronger
Schubitope 3.9/5.13 descriptions are separate. MSD v1 Conjectures 1.1--1.4
concern support; 1.5--1.6 concern signed coefficients and do not follow
merely from support convexity. These historical comparisons are attributed
literature statements, not changes to the book's canonical problem statuses.
Straight flagged Schur uses a separately cited Postnikov--Stanley input,
not read here; arbitrary flagged skew shapes are not admitted by that route.

## Full moments, boundary descent, and smaller apolar algebras

**C11 -- The coefficient algebra is specified.** §§6.1--6.3,
pp.38--43, use a finite graded duality algebra and a multiplication
annihilator of the Chern-moment functional. In the geometric package the
base is the **real diagonal Hodge cohomology algebra** of a smooth complex
projective source. It is not an arbitrary Chow ring presumed to satisfy
the standard conjectures. The moment ideal is not the linear kernel of
the degree functional and is not radicalized. The marked algebra and
degree have a formal duality/uniqueness property independent of positivity.

**C12 -- A monic inverse relation is not a positive certificate.**
Definition 6.7 and Propositions 6.6--6.8, pp.40--41, present the moments
as `B/ann(eta)`, with `eta=product xi_i^(s_i-1)`. Positivity requires a
full open convex Hodge cone on `B` and the relative generators in its
closure; base directions must also be in that closure. Algebraic inversion
of `K_i(t) C_i(t)=1` alone establishes neither cone membership nor Hodge
positivity. The geometric certificate uses generated kernel duals and
fibre-positive Fubini--Study forms, keeping base Kähler directions.

**C13 -- Classical descent is explicitly imported.** AHL Lemma 4.6,
p.26, allows `gamma` in the cone closure, retaining the coefficient
algebra and cone while replacing the module by `M/ann(gamma)` and its
pairing by `Q(x,gamma*y)`, with degree lowered by one. The source cites
CKS87 Lemma 1.16/Cattani Theorem 3.2. The latter's exact statement on
Cattani p.8 requires `T+lambda*N_0` Lefschetz for every `lambda>0`, takes
the image `T V`, regrades `tilde V_l=T V_(l+1)` and uses
`tilde Q(Tu,Tv)=Q(u,Tv)`. A closure class satisfies that condition because
adding a positive interior class stays interior. Cattani p.9 explicitly
does **not** reproduce the involved CKS §2 proof. That proof remains a
cited foundation, not a completed independent verification.

**C14 -- The subalgebra transfer has extra hypotheses.** AHL
Proposition 2.10, pp.15--16, assumes a graded subring with one-dimensional
top, no higher degree, a nondegenerate multiplication pairing, and
generation by closure-cone classes. Its conclusion has a relative-interior
cone and an orientation sign. Its printed proof invokes the paper's main
decomposition results, whose complete proof was not selected. LP Proposition
3.8 applies precisely this transfer after constructing its monic duality
subalgebra. AHL Proposition 2.8 about numerical Chow rings is explicitly
conditional on standard conjectures and is not imported unconditionally.

**C15 -- Apolar recovery needs generating directions.** Proposition
6.12 and Corollaries 6.15--6.16, pp.43--46, require degree-one generation
and directions spanning the relevant degree-one algebra to recover the
full algebra as an apolar quotient. Canonical-row sources have this
property; ample integral directions can complete a smaller displayed
polynomial. The completion has the full package. It does not automatically
give higher Hodge--Riemann relations to every smaller specialization.
Differentiation in `z` inserts generated hyperplane powers; maximal Chern
insertion and fixed base insertion retain their respective normalizations.

**C16 -- The obstruction concerns the middle sign, not Lorentzianity.**
Example 6.17, pp.46--47, has divided coefficients `(1,2,2,2,1)` and an
arbitrary-field toric rational volume model. Huh 1008.4749v3 Lemma 36,
p.17, gives the ordered-simplex formula and cites Shephard without
reproducing its proof. The quartic's apolar Hilbert vector is
`(1,2,3,2,1)`; `L=partial_x+partial_y` satisfies Hard Lefschetz, but a
nonzero primitive degree-two class has square `-30`. Its quadratic
derivative Hessians have determinants `-2,0,-2`. Thus a realizable
Lorentzian volume polynomial need not have all Hodge signs in its smaller
apolar algebra. Finite exact calculations confirm this example; they
are not a universal classification proof.

**C17 -- Nonflat base change and insertion differ.** Appendix D,
pp.67--69, identifies the moment ideal through a class-valued Hankel
map over the capped finite free algebra. Its base-change kernel is
`Tor_1(coker H_C,A')`, so a flat coefficient change commutes with moments,
but ordinary nonflat tensor restriction can fail. Example D.2 has
dimensions three versus two, with square-zero kernel generated by
`z-2h`. Fixed nonzero insertion instead gives an exact annihilator quotient
without flatness. Active-index shifts use `C_(alpha+beta)` and cannot be
replaced by products `C_alpha C_beta`. Tensor products of coefficient
algebras are not automatically the full diagonal Hodge ring of a product.

**C18 -- Positive abstract data need not have a fixed geometric source.**
Appendix D, pp.69--71, compresses auxiliary ranks at the certificate-algebra
level without constructing a geometric kernel of every smaller rank.
The lowering-operator hull requires an interior polarization and need not
be degree-one-generated. Example D.7 has a 12-dimensional containing
duality algebra inside a 16-dimensional ambient algebra. Proposition D.9
has positive moment data `(a,b)=(3,1)` and an integral virtual rank-two
lift, but no generated rank-two bundle on the specified `P^2`; its Ext
argument is read in the primary source. This is a fixed-source obstruction,
not nonrealizability of the scalar polynomial on every source.

## Tropical and nonvanishing gates

**C19 -- Tropical generation means the checked finite witness.**
Primary §7, pp.47--52, uses loopless Kaveh--Manon bundles on smooth
projective fans, integral apartment maps and the minimum-on-circuits
convention. KM Definition 5.3, p.20, supplies equivariant Chern classes;
Definition 6.4/Theorem 6.5, p.24, supplies a basis per maximal cone whose
characters lie in the parliament polyhedra. Higher tropical sheaf
cohomology and exact bundle kernels are not supplied. KM's Euler
characteristic is defined as an alternating sum of ranks.

**C20 -- Dual matroid and equivariant signs stay visible.** BEST
pp.11--15 uses minimum normal fans and inverse ambient characters; KM
uses outer maximum-basis cones. Primary Lemmas 7.3--7.5 duplicate finite
generating witnesses, take their parallel matroid `P`, and use `Q=P^*`,
with zero-weight padding loops in `P` becoming coloops in `Q`. Complements
of maximum bases are minimum bases. Before ordinary specialization the
identity contains the full global-character factor, not `1`; it becomes
`K(t)C(t)=1` only after global characters vanish. Dualization and signs
cannot be removed from the certificate.

**C21 -- LP proves a combinatorial certificate, not representability.**
The complete Larson--Partida paper verifies its monic projective-bundle
relation through biflag cancellation/degree detection, and proves the
joint Hodge package in Theorem 3.9, pp.17--18, by simultaneous fan
refinement, a full duality subalgebra and AHL Proposition 2.10. The Higgs
lift, Speyer truncation and foundational fan Hodge theorems remain cited
inputs; BEST Appendix III was not selected. The algebra can coincide
with a toric cohomology ring without the prescribed relative class being
nef on that geometric model. Nonrepresentable matroids do not become
geometric evaluation bundles. LP's citation “KM26” is Khan--Maclagan,
not Kaveh--Manon.

**C22 -- A local printed convention discrepancy is bounded.**
KM Definition 3.2, p.14, writes positive flat-indicator cones but describes
their successive coordinate layers in the reverse order from that formula
and Lemma 3.4's upper-flat characterization. Proposition 3.7's increasing
initial-span paragraph inherits this ordering issue. The circuit condition,
maximum-basis criterion, fundamental-circuit weight formula and upper-flat
proof are used instead. An exact `U_(2,3)` witness confirms the discrepancy.
It is not declared a disproof of Chern flow's main theorem, and no claim
is made about an uninspected later edition. Other source shorthand typos
in KM's power-sum and high-twist expressions are not reproduced.

**C23 -- The closure formula includes a sign convention.** Ardila
pp.3--8 proves its minimum-basis/max-on-circuits ultrametric projection,
including circuit/cocircuit exchange and the optimal-basis formula.
Negating gives the minimum-on-circuits least-majorant convention of
primary Proposition 7.10. The finite character-adaptation tests describe
allowed local Chern data, not isomorphism classes of all tropical bundles.
The labelled dual involution retains loops/coloops and the character sign;
rank-marked Whitney networks require the asserted series relations and
adapted terminal data.

**C24 -- Vanishing and equality have specified ambient meanings.**
§8, pp.53--58, detects generated geometric Chern products on smooth
complex projective sources by positive ample degree and nonzero real
cycle class; a general zero scheme can be reducible. The tropical analogue
uses numerical duality and ample domination. The rank function of total
Chern nonvanishing is a polymatroid, and residual ranks shift active indices.
The geometric cloned matroid's algebraicity uses the already read GHMSW
support/contraction inputs. Weighted layer masses include `(d+k)!` and
factorial coefficients; unweighted coefficient totals are not substituted.
Equality is an annihilator/proportionality statement in the appropriate
moment quotient and is not a vector-bundle splitting theorem.

**C25 -- Appendix refinements do not enlarge unsupported scopes.**
Appendices B--C, pp.60--66, give balanced-packet differential preservation,
cap-independent reflected support and an explicitly characteristic-zero
algebraic-dual argument. No unrestricted positive-characteristic algebraic
polymatroid duality is asserted. Relative co-rows require strictly
decreasing starts and generated tails; repeated starts can expose `O(-1)`.
Independent row twists are identified geometrically before factorial
normalization, which does not commute with variable identification.
The DAG path cone and total-unimodular bounded flow polytopes retain their
stated graph hypotheses; the general `K^0` identity does not need them.

## Exact finite diagnostics and preservation

The passing v2 receipt contains nine exact groups: the two-variable
Lascoux normalization; the `2143` packet/operator/reciprocal identities;
its creation-state divergence plus **2,141 binary terminal profiles for
all permutations through `n=5`**; the quartic apolar matrices and signs;
the ordered-simplex coefficient substitution; the `P^2` moment quotient,
nonflat restriction, free extension and virtual Chern class; the
noncommuting normalization/substitution example; the squarefree hull
example; and the KM flag-order witness. These are finite diagnostics,
not independent proofs of the universal theorems or Shephard's formula.

The first helper failed because it mistakenly inserted an extra factor
in the normalization/substitution example. Its failed helper and diagnostic
are retained. The repaired v2 uses the actual Remark B.8 quadratic:
`N_(u,v)((u+v)^2)|_(u=v=z)=3z^2`, while `N_z(4z^2)=2z^2`.
The failed version is never called a receipt or rerun as a repair.

The source-review PDF concatenates exactly the 182 selected physical
pages. The evidence archive contains controlling sources, acquisition and
reading records, all 94 individually displayed images and complete selected
texts, the unchanged 427-member TeX/bibliography closure, finite diagnostics
and frozen helper sources. Archive assembly/hash checks are not a fresh
book build, a new rendered-page reading, or an isolated ZIP compilation.
The compact published manifest points to bounded UTF-8 evidence parts,
whose byte concatenation reconstructs the complete manifest. Future
integration requires its own source gate, build and actual rendered-page
review; no unreviewed source-era open question is promoted here.
