# A finite singular-Hodge module example, 5 October 2026

Appendix G now works out the known `U_(3,4)` intersection-cohomology
module after its Chow/Möbius comparison. The three graded objects,
their different products and the all-one positive Lefschetz class
are explicit. Appendix L records the finite source and admission scope.
The general singular-Hodge induction is not a new input of this checkpoint.

## Frozen primary source and reading scope

Braden--Huh--Matherne--Proudfoot--Wang, *Singular Hodge theory for
combinatorial geometries*, [arXiv:2010.06088v5](https://arxiv.org/abs/2010.06088v5),
revised 27 June 2026, controls the example. The acquired version-five PDF
has 120 pages, 1,202,205 bytes and SHA-256
`2cb15fe8ea6dab99667c289bacfb35803c1e3bc4b6edcbbd3ddc716214c48e6e`.
The arXiv record separates the original 13 October 2020 submission from
the June 2026 revision. Primary author pages list JAMS, *to appear*.
No final publisher PDF, DOI, publication year or page range was acquired
or assigned. The bibliography's 2026 date describes the frozen revision.
Older linked author copies and unrelated search hits are not substituted
for this source.

The complete extracted text was read in 31 successful bounded ranges:
1--190, 191--380, 381--570, 571--760, 761--950, 951--1140,
1141--1330, 1331--1520, 1521--1710, 1711--1900, 1901--2090,
2091--2280, 2281--2470, 2471--2660, 2661--2850, 2851--3040,
3041--3230, 3231--3420, 3421--3610, 3611--3800, 3801--3990,
3991--4180, 4181--4370, 4371--4560, 4561--4750, 4751--4940,
4941--5130, 5131--5320, 5321--5510, 5511--5700 and 5701--5750.
These are newline/sed coordinates; Python `splitlines()` additionally
splits the 120 formfeeds and counts 5,870 lines. The text SHA-256 is
`51443382a289066f6057f05ce80e89193a8ec44dca1ba75756bbfad234c3fb7c`.
All 16 selected actual primary pages were inspected: physical/printed
1, 6--8, 11, 18, 27--30, 62--63, 67, 71--72 and 87. Full text reading
is distinct from inspecting every page image. External dependency
papers were not freshly read in full.

The load-bearing finite inputs are Definitions 2.2 and 2.5 (augmented
presentation and normalized degree), Definition 3.4 (orthogonal
complement) and Example 3.7 (`U_(3,4)`). The introduction's §1.1 gives
the rank-flat palindromic characterization of `P` and `Z`. The standing
finite loopless convention is retained. Theorems 1.6, 1.9 and 3.21
are not needed to certify the displayed finite calculations.

## Exact named-example calculation

The standard-library checker reconstructs the rational augmented Chow
quotient in the eleven proper-flat variables, including the empty flat.
It eliminates `y_i=sum_(i not in F) x_F`, kills incomparable products,
and imposes `y_i x_F=0` for `i not in F`. Multiples of these quadratic
relations are reduced exactly through degree three. Complete-flag
degree is normalized to one. The resulting dimensions are `(1,11,11,1)`;
the Möbius subalgebra has `(1,4,6,1)`.

The degree-one and degree-two bases of the known exceptional summand
`K` are respectively `(x_empty,x_1,x_2,x_3,x_4)` and
`(x_empty^2,x_1 y_1,x_2 y_2,x_3 y_3,x_4 y_4)`. Their pairing is
`diag(3,-2,-2,-2,-2)`. The complement `IH=K^perp` has dimensions
`(1,6,6,1)` and a degree-one basis
`u_ab=x_ab+(x_a+x_b)/2+x_empty/3`. Exact tests check each individual
Möbius generator's action preserves this complement. The ambient square
`u_12^2` is outside `IH^2`, since its pairing with `x_empty` is `-1/3`.
This illustrates the source's module construction and precludes treating
this realization as an inherited subring.

The degree-one/degree-two duality determinant is `-1/4` in the recorded
computed bases. Multiplication by `ell=y_1+y_2+y_3+y_4` has rank six,
and `deg(ell^3)=24`. The primitive kernel has dimension five, with the
five displayed `u_ab-u_12` basis elements. Its signed degree form has
successive positive leading principal minors `3,27/4,21/2,16,24`.
All matrices and exact rational coordinates are preserved in the result
JSON. These calculations certify this matroid and this class; they do
not certify arbitrary positive coefficients, integral extensions or
the general induction.

The positive-degree Möbius ideal gives quotient dimensions `(1,2,0,0)`.
A separate finite polynomial calculation uses constant rank-at-most-two
contraction polynomials and the equation
`Z=P+4t+6t^2+t^3`. Palindromicity and `deg(P)<3/2` give `P=1+2t` and
`Z=1+6t+6t^2+t^3`. Their agreement with the module dimensions here
does not depend on importing the general Theorem 1.9.

## Literal source passages needing qualification

These diagnostics explain why the general proof is outside this
integration. They do not refute the main Hodge theorem or supply an
independently certified general repair.

1. On p. 11 the asserted closed coordinate slice uses `p_e=0 iff e in F`.
   This literal condition excludes extra zero coordinates. For the
   Boolean rank-two product, the intended slice `{0} x P^1` contains
   `(0,0)`, which the literal condition excludes. The finite module
   calculation uses no such geometric identification.
2. The same page's stalk vanishing for `k>=d` is weaker than the
   `k>=d/2` condition needed to obtain Proposition 1.7. This is a missing
   explanatory implication, not a counterexample to that weaker bound
   or to the combinatorial proposition.
3. Example 3.3 on p. 27 prints a positive ordinary singleton
   self-intersection `+2`. Definitions 2.2/2.5 in the specified augmented
   quotient give `deg(x_i^2 y_i)=-2`. The relation
   `x_i y_i=x_empty x_i` and the standard degree normalization identify
   this with the corresponding ordinary self-intersection. The book
   computes the negative sign from the defining relations; it does not
   copy the inconsistent printed scalar. The finite nondegeneracy
   computation is checked directly, rather than relying on the sign in
   that explanation.
4. Proposition 7.3 on pp. 62--63 labels the tensor pairing as the form
   whose adapted reduction is the ambient pairing, whereas its proof
   computes the opposite direction. The parent-versus-minor hypothesis
   also requires qualification. No general reformulation is admitted.
5. Lemma 7.14 on p. 67 asserts that the displayed matrix and its indicated
   block part have the same eigenvalues. A congruence or a nondegenerate
   deformation can preserve signature without preserving eigenvalues.
   The nondegeneracy and signature argument actually needed by the
   induction remains to be audited; no counterexample to the lemma is
   claimed here.
6. In the proof of Theorem 8.6 on pp. 71--72, `j=-k` and
   `k>(i-crk(F))/2` imply `i+2j<crk(F)`, while the printed proof uses
   the opposite inequality and stalk branch. The dual branch has the
   complementary label issue. The relevant stalk/costalk definitions
   must be retained before a general proof reformulation is attempted.
7. Section 9.3 on p. 87 equates the circle auxiliary module and `IH` in
   the odd-rank `U_(3,4)` discussion, whereas Example 3.7 has a nonzero
   `K_empty`. Here the circle module has `(1,7,7,1)` and `IH` has
   `(1,6,6,1)`. That auxiliary-module equality is not imported.

## Admission and release scope

The repository protocol permits ordinary source audits for explicitly
identified imported results, definitions, explanatory reformulations
and direct formal consequences. This is a worked named source example.
No new formal result/proof environment, original general repair,
production-model call, extended historical receipt or priority claim
is added. A full reading alone is not an independent proof certificate.

The baseline is work commit `bdea87bdc4b3ff7b48ca9c961656641580b47cbd`.
Appendices G and L are the only changed members of the 425-input active
closure. Their 27 and 4 existing formal blocks, including proofs, and old
label order are preserved. Two new labels give 12,604 unique labels;
the appended bibliography record gives 587 keys and 288 cited keys.
The reference and inventory checkers pass. The complete native book
build has 4,265 pages with no TeX/package/pdfTeX warnings or errors,
overfull boxes, missing citations/references or rerun requests. The
954 pre-existing underfull-box diagnostics remain. Bibliography, index
and navigation checks pass: 736 accepted index entries, zero rejected,
2,446 contents entries and no invalid internal or index destinations.
Twelve actual release pages were inspected: physical 64, 66,
3911--3914, 4033--4034, 4246--4247, 4253 and 4255. These cover the
contents, the finite example and neighboring comparisons, provenance,
new index destinations and the new bibliography record. The frozen
manifest records these checks and export hashes. All 108 protected inputs, all 42
complete problem-status strings and the open catalogue source/PDF retain
their previous bytes. No fresh whole-book rereading is claimed for this
checkpoint. Prior dated releases retain their bytes and scope.

Incoming author research is fetched and inspected before ordinary
publication to `work`. Main remains unchanged; no force push is used.
