# Source and scope ledger

Date: 2026-08-31. Author: /root/p082_independent_reaudit.
Status: source-checked authoring, not independent audit or production PASS.

## 1. Exact result and dependency

The extension lemma is unconditional under its stated algebraic hypotheses.
For the normal integral family S/P1, A must be an actual ample globally
generated line bundle, E1 must be globally generated, and Sym^m(E1) -> Em
must be surjective for every m>=1. One integer C>=max(1,M) works for all
FS inputs in [-M,0]. The resulting extensions are in the same actual
B_C=A tensor pi*O(C), globally in [-C,1], with normalized weight modulus
at most C and zero restriction error.

The envelope theorem explicitly assumes BJ envelope property on S in
these ample classes. The supplied unibranch paper asserts this because
S is normal. This packet does not re-audit its entire proof.
The target is precisely the non-identically-minus-infinity part of the
decreasing-FS metric class of BE Definition 7.2.

The arrangement proposition handles any smooth geometrically integral
projective (Y,L0) already defined over k(t), with L0 ample. It constructs
a model satisfying the hypotheses for a tensor power, then descends the
metric statement by positive scaling. It does not descend arbitrary
k((t))-equations to k(t). All Laurent-series coefficients of sections
on the fixed family are allowed; those are different from coefficients
defining an arbitrary variety.

## 2. Local primary sources: exact versions and interfaces

### P0. Supplied unibranch-envelope manuscript

Path:
/Users/mingchen/Projects/Yethlas/bj_envelope_latex_source/bj_envelope.tex.

SHA256:
6a075400ead7837a254d7b16eaf5ab6da3d65fa720ac0da272f2958faf20f3bf.

Title: The envelope property for unibranch projective varieties.
The supplied author field is empty. Read the actual introduction
thm:intro-main and final thm:main statement/proof in this task.
Both assert EP for integral projective unibranch varieties over
algebraically closed trivial k, in arbitrary characteristic and dimension.
The hypothesis concerns usc suprema of bounded-above psh families,
not continuity for a continuous obstacle.

### P1. Boucksom--Jonsson, published BJ22

Global pluripotential theory over a trivially valued field,
Ann. Fac. Sci. Toulouse (6) 31(3) (2022), 647--836.
[Publisher DOI page](https://afst.centre-mersenne.org/articles/10.5802/afst.1705/).

PDF: /private/tmp/bj22.pdf, SHA256
50bd6e6782c29088edc96d013a5d49257b0395d9fb398664f1a9859639992948.
Identical PDF copy: /Users/mingchen/Projects/Yethlas/tmp/BJ22.pdf.

Text: /private/tmp/bj22.txt, SHA256
0caf7da441e678675b1ec1bc3461cc21e293cee6809fcf8dfdbe1947b5617777.

| Exact location | Interface used |
| --- | --- |
| Section 1.1.2, p. 660 | Compact Hausdorff topology of projective analytification |
| Section 1.1.4, p. 662 | Jointly continuous positive-real scaling of semivaluations |
| Remark 1.24, p. 671 | Trivial metric evaluated in a frame at the centre; global section norms <=1 |
| (2.8), Definition 2.18 and (2.9), pp. 679--680 | Real/rational weighted FS functions and tensor presentations |
| Definition 3.8 and Example 3.9, p. 694 | Hdom of an ample actual line bundle lies in its fixed rational FS space |
| Theorem 4.15(iii), p. 713 | Decreasing regularization in the same ample bundle |
| Definition 5.8, p. 723 | Exact envelope-property definition |

The scaling, metric, FS definition, Example 3.9, Theorem 4.15 including
its proof, and EP definition were read directly. The abstract closure
step here is sourced more directly to BE Lemma 7.4, not to an EP theorem.

Printed Remark 1.9 is not an input. The incorrect full-image
identification adjacent to the legitimate Gauss-section formula was
previously confirmed by the parent in the actual PDF. Here neither
that identification nor a generic Gauss point is used for integrality.
The entire fibre is obtained via completed residue fields, and the
unit ball uses all vertical codimension-one points.

### P2. Boucksom--Eriksson, exact arXiv version 3

Spaces of norms, determinant of cohomology and Fekete points in
non-Archimedean geometry,
[arXiv:1805.01016v3](https://arxiv.org/abs/1805.01016v3),
8 January 2021, internal date 11 January 2021, 99 pages.

PDF: /private/tmp/BoucksomEriksson_1805.01016.pdf, SHA256
51d02f75a65aa463f8e22393933f5ebef9036e322d720fc632f87759c2b71cb2.

Text: /private/tmp/BoucksomEriksson_1805.01016.txt, SHA256
1ab23277bee5b344a371e6d6ca3685ef55bbcaac4848c2febac708948c658286.

| Exact location | Interface and scope check |
| --- | --- |
| Example 4.11, Section 4.3 | Normal-model vertical generic point gives the valuation/model point; here the model is Noetherian over a DVR |
| Theorem 4.19, p. 36 | Audit warning: normality/integral closure alone does NOT imply equality of the whole sup and lattice norms in the discrete case |
| Definition 5.2, p. 38 | Arbitrary real FS weights on a finite basepoint-free section system |
| Proposition 5.4(iii),(vi), pp. 38--39 | Positive tensor scaling and finite maxima |
| Section 5.3, pp. 40--41 | Model reference metric, norm-one local frames, trivial metric |
| Definition 7.2, p. 48 | Exact target decreasing-net FS metric definition |
| Lemma 7.4 and Corollary 7.5, p. 48 | Decreasing-net and finite-max closure, independent of EP |

All listed statements and the relevant proofs were read directly.
Theorem 4.19 is not invoked to identify a discrete lattice norm with the
sup norm. Only the unit ball is identified; its proof is given explicitly
using horizontal regularity and vertical divisorial points with
multiplicities ord_E(t). No reduced special fibre, non-Noetherian lattice
claim, later BE envelope theorem, or nef/psh comparison is imported.

### P3. Temkin, exact arXiv version 2

Introduction to Berkovich analytic spaces,
[arXiv:1010.2235v2](https://arxiv.org/abs/1010.2235v2),
16 December 2011.

PDF: /private/tmp/Temkin_Berkovich_Intro.pdf, SHA256
b8a7ac414e98fdd46db3961c43e08068203aec7225457f455dc077f87b32b914.

Text: /private/tmp/Temkin_Berkovich_Intro.txt, SHA256
65e4ba4c4071fd09115f640470ba3b6987cd0a255cd5fe3a0a4d2ddda5ce5980.

Definition/Exercise 4.1.7.1, pp. 26--27, and Section 5.1.1,
pp. 33--34, were read directly. They give the fibre as base change
to the completed residue field and the affine-seminorm construction
of analytification. Here H(eta)=k((t)), and projectivity plus
Hausdorffness upgrades the natural continuous fibre bijection to a
homeomorphism. No arbitrary singular-psh restriction theorem is used.

## 3. Primary Stacks algebraic interfaces

Read the exact HTML theorem texts, and relevant proofs, on 2026-08-31.
Stable tags, rather than mutable numerical labels, control the citations.
The accessed HTML was not downloaded or byte-frozen, so no hash of that
remote content is claimed. The local proof spells out the applications.

| Stable tag | Accessed statement | Exact use |
| --- | --- | --- |
| [0539](https://stacks.math.columbia.edu/tag/0539) | Lemma 15.22.10 | Torsion-free over a valuation ring implies flat; applies at each DVR of P1 |
| [07QS](https://stacks.math.columbia.edu/tag/07QS) | Section 15.53, Definition 15.53.1, Lemma 15.53.2, Proposition 15.53.3, Lemma 15.53.5 | R0 is excellent; finite-type k-schemes are Nagata |
| [07GH](https://stacks.math.columbia.edu/tag/07GH) | Definition 15.51.1 | Excellent local R0 is a G-ring, so its map to its completion is regular |
| [07C1](https://stacks.math.columbia.edu/tag/07C1) | Lemma 15.42.3 | Regularity preserved by the finite-type affine base change from R0 to a chart of S_R0 |
| [0C22](https://stacks.math.columbia.edu/tag/0C22) | Lemma 10.163.8 | Normality ascends under a flat map of Noetherian rings with normal fibres |
| [031T](https://stacks.math.columbia.edu/tag/031T) | Lemma 10.157.6(2) | Normal Noetherian domain is intersection of its height-one localizations |
| [02KH](https://stacks.math.columbia.edu/tag/02KH) | Lemma 30.5.2 | Flat H0 base change along R0 -> R; no special-fibre H0 base change is asserted |
| [035S](https://stacks.math.columbia.edu/tag/035S) | Lemma 29.55.11 | Normalization of Nagata scheme is finite |
| [0B5V](https://stacks.math.columbia.edu/tag/0B5V) | Lemma 30.17.2 | Finite pullback of an ample line bundle is ample |
| [0B5T](https://stacks.math.columbia.edu/tag/0B5T) | Lemma 30.16.1(4) | Serre vanishing for the graph ideal on each affine base chart |

The two auxiliary conclusions are proved, not hidden in vague source
references:

1. The completed model is integral because it is flat and its generic
   fibre is geometrically integral. On a nonempty affine chart,
   localization at t is a domain and the localization map is injective.
2. The degree-one generation after a Veronese follows from the explicit
   polynomial surjections in all degrees n>=n0 and grouping degree-md
   monomials into m degree-d monomials. No assertion that every arbitrary
   finitely generated graded algebra has a suitable unexplained Veronese
   is required.

## 4. Proof gap analysis and boundaries

- Normality after completion: finite-type charts, Noetherian rings,
  regular completion map, normal ascent are all checked explicitly.
  Formal normality is not merely assumed.
- Unit ball: horizontal codimension-one points use existing generic
  regularity; vertical points use ord_E/b_E. Higher codimension uses the
  normal intersection theorem. Nonreduced special fibres are permitted.
- Reference: a generating system for E1 alone is insufficient unless
  A is also globally generated. Both hypotheses are stated; q_l generate
  both. The model reference equals restriction of the trivial reference.
- Coefficients: right exactness after the prescribed symmetric-power
  surjection gives integral monomial coefficients. Nonuniqueness is
  harmless. The tail estimate uses finitely many monomials of norm <=1.
- Cancellation: the normed-line strict-error argument proves equality
  of maxima at every analytic point, including proper support. No generic
  Gauss cancellation rule is applied at a general point.
- Global generation: negative weights, not polynomial smallness,
  make U- and T-padding invisible on the fibre while removing base loci
  at zero, every other finite base point, and infinity.
- Fixed ample class: C is independent of denominators and all other
  presentation data. Every normalized weight is bounded in modulus by C.
- USC restriction: collar scaling is on all S-analytic points in
  0<|t|<1, not a Gauss-section subset. The uniform radial estimate proves
  both inequalities; mere continuity of a closed-fibre inclusion would
  not suffice.
- PSH: only ambient psh is regularized by BJ4.15(iii). Its actual
  fixed-bundle FS systems restrict explicitly. Individual arbitrary
  fibrewise psh functions are never assumed liftable.
- Nets: compactness handles cofinal tails and continuous majorants;
  products of directed sets are used with ordinary choice. No sequential
  approximation or unjustified sup/inf interchange is assumed.
- Scope of arrangement: normalization and ample powers are over k;
  the generic fibre remains the given smooth Y/F0. No finite field
  extension, alteration, resolution, or reduced-fibre replacement is
  hidden. General K-varieties not defined over k(t) remain outside scope.

The author found no unresolved algebraic or analytic step in the written
scope. This is not a substitute for independent hostile review. The
unibranch EP remains an explicitly imported theorem. No claims about
continuous-obstacle continuity, all numerical classes on X, general
nontrivially valued fields, or other psh definitions are made.
