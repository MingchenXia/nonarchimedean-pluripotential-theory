# Chapter 60: finite-energy stability and its model interface

Date: 24 September 2026.
Baseline: `8c43d3bc14245da9a0ec5ffe85bae21a5524bfba`.
Scope: the finite-energy uniform-stability definition through the Chapter 60
source note. All preceding Chapter 60 source, including the entropy-slope
proof completed in the preceding unit, retains its baseline bytes.
This is an exposition and direct-consequence audit of established inputs;
it introduces no research-frontier closure or production-verifier claim.

## Functional normalization and the actual testing set

The new normalization proposition passes invariance of the model measure
under constants to finite energy, using the existing decreasing-limit
measure construction. Entropy is consequently unchanged even when infinite.
The finite mixed-pairing translation identity gives E(phi+c)=E(phi)+c
and changes twisted energy by n c (beta.alpha^(n-1))/V. Taking
beta=-c1(X) cancels the scalar-energy translation exactly. In particular,
the factor n is needed in the general scalar coefficient; the existing
Chapter 62 coefficient correction and its dated verifier receipt are
preserved, not replaced by a new receipt.

J is invariant under constants, is nonnegative, and vanishes exactly on
constants by the earlier test-curve mass-defect result. A constant has
trivial Monge--Ampere measure, zero reduced entropy and zero Mabuchi
functional. Infinite entropy gives infinite Mabuchi, since the other
terms are finite. Thus every nonautomatic stability test can be normalized
at the trivial valuation and has positive finite J and finite entropy.

The optimal constant is the infimum of M/J over precisely that set.
Each ratio is real, but the infimum may be minus infinity; the empty
infimum is plus infinity. For each positive real delta, the full
inequality is equivalent to delta being at most that infimum. In dimension
zero all data are constants and the testing set is empty. No attainment
of the infimum, sequential approximation or quotient by zero is needed.

## Projective-line test and ray growth

On the blowup of one point of P1 times the base, write D=-aE with
0<=a<=1. Degrees of A-aE on the exceptional and strict-transform central
components are a and 1-a, so the entire closed interval is relatively nef.
Both central multiplicities are one. The model measure is
(1-a)delta_triv+a delta_ord0; A^2=A.E=0 and E^2=-1 give
E=-a^2/2 and J=a^2/2. The twisted energy is zero, the reduced entropy is
a, and the scalar coefficient is 2. Hence M=a-a^2 and, for a>0,
M/J=2(1-a)/a. The zero endpoint is constant; at the other endpoint
J=1/2 while M=0. Ratios are positive on the open interval but have no
common positive lower bound. Fubini--Study has Ricci form twice itself,
so this is also an explicit failure of the converse from cscK existence
to the ordinary, nonrelative uniform condition. It is an elementary
model calculation, not an assertion about automorphism-relative stability.

For normalized nonconstant data and the maximal ray starting at zero,
the earlier order and energy identities give U_s<=0 and d1(U_s,0)=sJ.
The reduced slope theorem therefore yields liminf M(U_s)/d1(U_s,0)>=delta.
For each fixed ray, every epsilon gives an eventual (delta-epsilon)
bound. The onset time may depend on that ray and on epsilon. Infinite
entropy gives divergence. This does not turn an arbitrary ray into a
maximal ray or yield one complex coercivity estimate uniform over all
rays; the cscK existence implication remains an explicitly imported input.

## Precise source and chapter interfaces

The exact [MP--Witt Nystrom v1 PDF](https://arxiv.org/pdf/2509.09442v1)
was downloaded from the primary source and checked at printed pp. 13,
31, 34 and 35. All four pages were rendered and visually inspected.
The PDF has 689,695 bytes and SHA-256
`54c7f7e75bc9869f979fff2c2e0e56079660a408cc18d2df95d327dff01b7464`.

- Definitions 2.4.1--2.4.2 and Theorem 2.4.3, p. 13, supply reduced
  discrepancy, a single coercivity constant for every finite-energy
  potential, and literal uniqueness of the cscK metric. The printed scalar
  coefficient omits n; the existing audited Chapter 62 correction remains
  explicit. Dimension zero is treated directly in the book.
- Theorem 9.1.1, p. 31, requires the obstacle normalization f_D>=1.
  Corollary 9.1.6, p. 34, states the further raw-model equivalence; the
  book's existing limitation on that step is retained.
- Theorem 9.2.1, pp. 34--35, uses strong convergence together with entropy
  convergence, then approximation on one fixed dual complex. Corollary
  9.2.2, p. 35, gives the model-to-cscK implication.
- The [author's publication page](https://pietropic.github.io/publications/)
  still lists this work as a preprint; no new journal record was established.
  The source note also retains exact MPTropicalV2 citations for the
  earlier construction, whose published MP record is already in the
  bibliography. The two corresponding house-audit warnings are reviewed.

The closing text now points to the precise internal Calabi--Yau theorem,
completion theorem and normalized-model corollary. It distinguishes all
finite-energy data, continuous data with measure on one dual complex,
and real PL envelopes, with the same delta in their equivalence. The
all-raw-big-model condition implies those conditions by restriction. Its
converse is not deduced from translation of potential functionals: raw
positive-product invariants can change under a base translation. No part
of Chapters 61 or 62, their original corrections, or their verifier records
is edited. The BHJ and earlier MP/BJ source-note locators retain the scopes
checked in the preceding chapter audits.

## Two passes and validation

The first complete statement/proof/source/notation pass produced a full
build of 3,989 pages and 18,986,998 bytes, with no unresolved reference or
citation and no layout overflow. Physical pages 3384--3388 were rendered
and inspected. The second pass checked the constant translations, signed
twisting class, finite denominator and extended-real infimum, both curve
endpoints, central multiplicities, fixed-ray quantifiers, zero dimension,
and each model-completion implication. It added the minus-infinity
infimum convention, made the zero endpoint explicit, cited the exact ray
order result and source pages, and removed redundant closing prose.

Final full build: **3,989 pages, 18,987,738 bytes**. Physical pages
3384--3389 were rendered and inspected in full, including the preceding
entropy-proof boundary and the opening of Chapter 61. This is a scoped
visual review, not a new visual audit of every page in the book.

- Input/reference check: 390 TeX files, 11,657 unique labels; no missing
  input, duplicate label, dangling reference or structural defect.
- Final log: no unresolved reference/citation, multiply defined label,
  rerun request or horizontal/vertical overflow. Existing class and
  underfull warnings remain.
- Scoped strict house audit: zero errors and two reviewed warnings for
  MPWN25 and MPTropicalV2; exit status 1, not a warning-free strict pass.
  The normal scoped audit exits successfully with those warnings.
- Inventory: PASS, 45 active atoms across 14 formal environments,
  tiers (0,5,8,15,17).
- Every byte before the finite-energy stability definition is identical
  to the baseline; the rest of the book source is unchanged.
- `git diff --check`: PASS.

Final Chapter 60 SHA-256:
`0fdb5f601274ccf7df48afd5112a1bf3e452e3aff9df5a459c5c6a08e611ac93`.
Final live PDF SHA-256:
`4d68e07efe035263e7e21efb69cbce226cda66251421c0c0d5e9b7442d4a2e8d`.

The preserved P12.1 fragment has SHA-256
`8d9f9bd9edb057b95773479279bbdabb3240319e4cb56f6f15cb2bd923fb4380`.
The supplied normalized-links PDF and archived copy both retain SHA-256
`71f5e0d50bdcbf493cb96a869e2db03a78bd591b3eba2f797da5a23f6253daaa`.
The supplied CURVE_PSH.tex retains SHA-256
`9142aac73c5af7e4e715b3313def5ed56fae4e63e1ac8a53d0419df7d2194be9`.

The 45 active research atoms, completed P12.1 integration/provenance,
P12.2--P12.6 residuals, supplied originals, bibliography, frozen packets,
verifier receipts and dated releases are preserved. This is a local
two-pass proof/source/build audit, with no independent-agent or production-
verifier pass asserted. The live PDF remains an ignored build product.
