# Arithmetic Fujita over adelic curves: full v4 source audit

Chunhui Liu, Arithmetic Fujita approximation over adelic curves,
arXiv:2401.15271v4, 25 January 2026. PDF SHA256:
fc0b9e65342154a0db29e3cf4ecd7110114b7406de205a7149220544fd265597.
All 27 physical pages were actually read in fourteen ordered matching
complete-text/image displays, including all proofs, declarations and
references. The internal footer says 27 January; it does not replace
the controlling arXiv date. Earlier versions and later journal full text
have not been read or diagnosed. This is a reading and scoped proof audit,
not recursive certification of every imported result.

## Main statement and exact hypotheses

Theorem 1.1 (pages 3–4), restated as Theorem 5.5 (page 25), assumes a
PROPER adelic curve, PERFECT K, and either a discrete sigma-algebra or a
COUNTABLE SUBFIELD dense in EVERY K_w. It concerns an arithmetically big
adelic R-line bundle on a projective variety of dimension d. Its claimed
birational decomposition of the p-th tensor power has an arithmetically
ample factor and an R-effective residual with a nonzero small section,
with p^(-(d+1)) arithmetic-volume error below epsilon. The nef/integral
case is Theorem 5.1 on pages 21–22; the ample upgrade is Corollary 5.2 on
pages 22–23; the rational case clears denominators in Corollary 5.3.
The intended main result remains **UNVERIFIED FOR BOOK IMPORT**, pending
an exact norm/degree/approximation reconstruction. This audit does not
assert that its intended conclusion is false.

Properness is the product formula, definitions 2.1–2.2 on page 5. The
common dense-subfield alternative ensures closure of normed bundle
constructions; it is stronger data than merely possessing a set of
absolute values and differs from requiring the entire field to be
countable. Perfection is retained when slope criteria are converted to
arithmetic positivity. The main hypotheses cannot be omitted when
relating the result to the new GVF height representation in Chapter 27.

## Norms and two kinds of smallness

Section 3.1.2 uses an INTEGRATED placewise sup distance for semipositivity
and normalized quotient-metric approximants. Section 3.1.3 combines
relative positivity with a uniform GLOBAL arithmetic intersection bound
over integral subschemes. Section 3.1.5 defines a nonzero small section
by sup norm <=1 at EVERY place. A global slope/intersection condition
must not be silently replaced by the latter simultaneous local condition.
The explicit three-place projective model is reconstructed in the
separate own_three_place_model_reconstruction record. It realizes
Example 4.4's constant norm data, has arithmetic volume 1/2 and minimal
asymptotic slope 1/4, and has no nonzero small section in a positive power.
Yet it has nontrivial ample/small-residual decompositions for every p>=2,
with normalized ample-volume error 1/(2p). The printed inference from
arithmetic ampleness to all-places smallness is therefore not used.
No source general theorem is required for this direct classical model.

## Printed normalization and degree qualifications

1. The older relative-Fujita summary on page 3 puts the growing p t bound
   on the fixed L instead of clearly naming the moving factor. Preserve
   the primary locator rather than copying this auxiliary formula.
2. The slope flag on page 8 mixes distinct jumps and rank-indexed weights.
   Repeated slopes are handled by their actual dimension multiplicities.
3. Proposition 3.6 on page 13 omits rank from the probability moment.
   Rank-r constant weight one over a trivial place has total positive
   degree r and probability moment one, with zero archimedean error.
   The corrected finite expression multiplies the moment by rank.
4. Proposition 3.9 on page 15 keeps the intended asymptotic relation
   vol_hat=(d+1) vol lambda_plus. The logarithmic rank error is lower order
   after the appropriate geometric section growth normalization.
5. Proposition 4.2's proof on page 17 needs the actual degree q=kd+p,
   the fixed effective-factor section, and a sufficiently projectively
   normal ample power. The printed pk/k and pD/qD indices are not copied.
6. Proposition 4.5 on pages 19–20 uses finite non-atomic threshold grids,
   simultaneous dimension approximation, rank-tail integration and Abel
   summation. Its Step II uses RESCALED probability moments correctly;
   Step III mixes those moments with the unscaled degree denominator.
   The consistent finite expression is N rank moment divided by
   N^(d+1)/(d+1)!, for actual degree N=np. The printed expression tends to
   zero on a constant-shift P^d test, whereas the intended volume is
   (d+1)C. The correction must also declare Veronese degree conventions.
7. Theorem 5.1's generated moving bundle is globally generated; an
   absolute embedding does not follow without additional hypotheses.
   The relative graph/blowup is the relevant construction. Degree-n
   section injections retain L^(np), and the residual metric retains L^p.
8. The quotient-metric evaluation argument needs all analytic points and
   infima or approximate lifts; a norm-attaining representative from a
   blanket nonarchimedean Hahn–Banach invocation is not assumed.
9. Step III of Theorem 5.1 mixes the original-degree normalization with
   the m-graded Veronese denominator. On a complete degree-p P1 series,
   unnormalized Veronese volume is p^2 times original volume, so the
   printed inequality compares incompatible conventions.
10. Zero SPECTRAL threshold is not exact finite-level nonnegativity of
    ORIGINAL HN minimal slopes. The precise comparison, its losses and
    any positive threshold/slack must be supplied before applying the
    arithmetic nefness criterion. Nonnegative does not mean positive.
11. The ample upgrade's small-section step requires its own hypotheses;
    the Luo Remark 5.7 citation supports the preceding birational-bigness
    clause, as corrected in the fresh note-precision addendum. It must
    not be blamed for the subsequent unqualified small-section claim.
12. The real-case effective-direction argument must retain the given
    metrics and the appropriate Q/R-line-bundle convention. Effective
    powers of geometric big bundles and nonnegative small volume error
    are sufficient; printed degree-one effectivity and strict error
    need their separate justifications.

These qualifications are local source issues and reconstruction
requirements. Correcting a finite identity is not a recursive proof of
all model-theoretic, norm-family or geometric inputs, and it does not
supply a general arithmetic Fujita verifier.

## Own exact diagnostics and their limits

The finite/symbolic checks include 64 rank tests (63 literal missing-rank
failures), 2,240 factorial/degree checks, 35 corrected-versus-printed
symbolic limits, 420 Veronese conventions (385 mixed-convention failures),
64 three-place degree/no-small-power tests, 64 explicit nontrivial
ample/small-residual decompositions and 64 rank-tail/Abel comparisons.
The first helper failed before writing a checkpoint because its empty
zero-dimensional product became a Python float; a fresh corrected helper
uses exact SymPy integers. Both helpers and the failure record are frozen.
No mathematical counterexample is inferred from that implementation error.

## Primary dependency boundaries and future book use

Chen arithmetic Fujita (Annales ENS 2010), Chen–Moriwaki LNM 2258 (2020)
and Progress in Mathematics 355 (2024), Bost–Chen tensor estimates,
Lazarsfeld–Mustata approximability, geometric Kodaira decomposition,
and the exact quotient/spectral-norm comparisons are disclosed imports.
They have not all been newly recursively read. Reference [19] is Luo's
Continuous extension and birational invariance of chi-volume over an
adelic curve, EJM 11 (2025), Paper 33; it is different from the separate
metadata-only relative-bigness arXiv:2112.13206 lead. The Sedillot v2
reading remains limited to the earlier five selected pages. No reading
credit is obtained merely by listing a dependency.

Potential accurate explanatory import is the explicit three-place model
and the difference between global arithmetic positivity and simultaneous
small sections. The general main statement requires further reconstruction.
Even a verified volume approximation theorem would not by itself prove
Ballaÿ–Sombra's separate essential-minimum/defect or weaker logarithmic-test
questions, homogeneous Siu decomposition, or envelope continuity.
The active 4,685-page book and native catalogue/editor remain unchanged
by this source-only audit. Canonical 42 atoms/twelve problems, tiers
(0,3,7,15,17), remain; BJ22 general homogeneous Siu/envelopes stay OPEN,
LPWZ density UNVERIFIED. No original theorem, independent production
receipt or canonical closure is promoted. Work remains cloud-only,
Xean suspended. Author-owned evidence excludes primary PDF/full text/images.
