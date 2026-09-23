# Chapter 56: Gauss normalization and multiplier-ideal approximation

Audit date: 23 September 2026.

## Mathematical changes

The Gauss extension now has an explicit support and normalization check.
Its kernel is the polynomial extension of the support ideal, so its
support is exactly Y times A1, and its center is c(v) times {0}.
Initial forms prove multiplicativity. For v=(a/b)ord_E with coprime
positive integers a,b, the normalized weighted blowup with weights
(a,b) gives sigma(v)=b^(-1)ord_D. The full-support trivial valuation
gives the central fiber. The rational convention in Chapter 32 is
preserved: irrational real multiples have Gauss extensions of rational
rank two, so the divisorial proof is not applied to them.

The complexification is formed only after the terminal parameter has
been moved to a nonpositive value. Every summand then extends as a
psh potential across the central fiber, and the initial potential gives
a common local upper bound. The envelope identity is proved using
increasing finite maxima, local L1 convergence on the Gauss model,
upper semicontinuity of generic Lelong numbers, and the reverse
inequality from domination of each summand. This is a divisorial
identification; proper-support values enter later through ideals.

### Hyperplane example

The former example used an unshifted curve with terminal parameter 1
in the central-fiber calculation. It also applied a semivaluation to
a smooth expression, asserted a positive-level formula at negative
parameters, and used the divisorial formula on arbitrary supports.
The rewritten calculation removes these problems.

For the Chapter 52 hyperplane curve, the divisorial value is
F(v)=max(0,1-v(I_H)). The sections x_0,...,x_n with weights 1,0,...,0
give the full Fubini--Study extension. The equality uses the disjoint
pole loci H and P_0, hence remains valid for infinite ideal values.
Only rational positive levels are called analytic; real levels use
I-goodness, in agreement with Chapter 52.

After replacing Gamma_tau by Gamma_(tau+1), the complexification is
log(a_0+|z|^2 sum_(i>0) a_i). In a local frame its holomorphic
generators are x_0,zx_1,...,zx_n. They generate the ideal of the
smooth codimension-two center Z=H times {0}, locally (u,z).
The Gauss ideal value is min(v(I_H),1), and the metric is F-1.

Direct radial integration in the two normal variables yields
I(m Phi)=I_Z^(m-1) for all integers m>=1. The dyadic stages are
-(1-2^(-j)) min(v(I_H),1), decreasing from 0 to F-1. For support
contained in H, this limit is -1; after translating back, F=0.
For v_triv, F=1. The first stage m=1 and infinite ideal values were
checked separately. These explicit formulas are mathematical checks,
not a substitute for the general approximation theorem.

### Uniform generation and extension

For one fixed potential, the proof chooses a very ample H and one
integer b such that H^b minus K_X minus qH is ample for 1<=q<=n.
Nadel vanishing and Castelnuovo--Mumford regularity then give global
generation for every k with the same b. Reading sections in a local
frame justifies ideal evaluation on all semivaluations, including
the case where every generator vanishes on the support.

For a ray, equality of the product multiplier ideals over the punctured
disk is proved on compact annuli. The relative full-mass rooftop of
the two endpoint slices lies below the geodesic, while the initial
model potential lies above it. Their multiplier ideals agree by the
relative full-mass theorem. The local product formula for ideals
then sandwiches the complexified ideal between two equal pullbacks.
This justifies gluing and algebraization. Fiberwise equality alone
is not used as a product-ideal theorem.

The coefficient chain stabilizes at I(m phi), which need not be the
unit ideal for an unbounded initial potential. The family-generation
proof checks bigness of L, imports the exact uniform family theorem,
and explains coefficient extraction: Taylor coefficients of global
generators of degree <=i generate the i-th coefficient ideal, using
the increasing coefficient chain. The twist T is independent of m
and i.

The GF stages display the section weights -i explicitly. Subadditivity
gives monotonicity on every semivaluation; the separate asymptotic
multiplier-ideal theorem identifies the divisorial limit. Its finite
value at v_triv prevents collapse before BJ closedness is used.
Uniqueness applies BJ divisorial domination in both directions to
two psh extensions. Equality with an arbitrary usc extension is not
asserted. At the pseudoeffective boundary, equality between different
perturbations is first established on divisorial points and then
extended in a common larger class using the same domination theorem.

## Primary sources and exact locators

- [Darvas--Xia--Zhang, published article](https://ems.press/journals/cmh/articles/14298510),
  Comment. Math. Helv. 100 (2025), 269--322: Proposition 3.1, page 288,
  gives the Gauss identity; Lemmas 3.5 and 3.7--3.8, page 291, give
  the fixed-potential approximation and ideal algebraization;
  Lemma 3.9, page 292, is uniform family generation; Proposition
  3.10, pages 292--293, proves the annulus ideal identity and
  approximation; Corollary 3.11, page 294, treats test curves.
- [Demailly, author-hosted Analytic Methods in Algebraic Geometry](https://www-fourier.univ-grenoble-alpes.fr/~demailly/manuscripts/analmeth_book.pdf):
  Theorem 6.27 and its proof, pages 51--52, give uniform global
  generation. The product formula is Theorem 15.2(a), page 159,
  in this checked author file. Its Proposition 15.3 is the pullback
  statement; Corollary 14.3 instead concerns Lelong upperlevel sets.
  Accordingly, the chapter cites the checked published DXZ proof
  for the product step rather than copying its Demailly locator
  across versions. The author PDF is distinguished from the 2012
  print edition in the existing bibliography.
- [Matsumura, published article](https://content.algebraicgeometry.nl/2022-2/2022-2-005.pdf),
  Algebraic Geometry 9 (2022), 122--158: Theorem 1.7, page 125,
  is the relative vanishing input for a surjective projective map
  from a complex manifold. The chapter uses the resulting uniform
  generation statement in DXZ Lemma 3.9, not an unsupported
  assertion that generation on fibers suffices.
- [Boucksom--Jonsson, published article](https://numdam.org/articles/10.5802/afst.1705/),
  Ann. Fac. Sci. Toulouse 31 (2022), 647--836: Theorem 4.5, pages
  708--709, supplies decreasing closedness; Theorem 4.22 and
  Corollary 4.23, page 715,
  give one-sided divisorial domination and uniqueness among psh
  extensions. The one-sided quantifiers were checked explicitly.

Rendered source pages inspected: DXZ physical 20, 24 and 25 (printed
288, 292 and 293); Demailly pages 51--52; Matsumura physical 4
(printed 125); BJ physical 70 (printed 715). Other listed locators
were checked in the extracted source text.

The second local mathematical pass checked the rational Gauss weights,
the common envelope upper bound, the shift and both ideal centers in
the example, transverse codimension and multiplier exponents, the
annulus sandwich, the nonunit terminal coefficient, the extraction
of Taylor generators, negative GF weights, the order of the dyadic
inequality, noncollapse, and two-sided use of divisorial domination.
Relative rooftop stability, full-mass ideal equality, uniform family
generation and asymptotic multiplier approximation remain explicit
imported analytic inputs.

## Validation and preservation

- Final complete build: 3,941 pages, 18,728,957 bytes.
- Reference/structure check: 389 inputs, 11,562 labels; no missing
  inputs, duplicate labels, dangling references or structural errors.
- Final build log: no unresolved references or citations, and no
  horizontal or vertical overflow. Existing underfull-box and
  class-name warnings remain outside this revision.
- Strict style audit of the complete changed mathematical blocks
  and revised prose: zero errors and zero warnings.
- Research inventory: 46 active atoms in 14 environments, with tiers
  `(0,5,8,16,17)`; no classification changes.
- Final rendered physical pages 3268--3276 (printed 3200--3208)
  inspected. The revised displays, proof continuations and source
  note are legible and unclipped. The page affected by the final
  citation correction was inspected again after rebuilding.
- `git diff --check` passes. The checked PDF is an ignored local
  artifact and is not included in the commit.

SHA-256 records:

| File | SHA-256 |
| --- | --- |
| Chapter 56 before this revision | `cca2805a816d187427679efdb28d3f81c84855053a635223639cb837d0e649d9` |
| Final Chapter 56 | `8d9cd1f51c87deb1cac4743fd3237da0d268d5c533a8c78d92b395ad1e121959` |
| Final local book.pdf | `3086f0799eded46cf8db9450a10e021904bc6f2fe6a5587fa88cd6d07204dc3a` |
| Published DXZ PDF | `467778ff37b893681482e43b4d8f1d717e947a34fe61026b2e6bc418e4a1f70e` |
| Published BJ PDF | `50bd6e6782c29088edc96d013a5d49257b0395d9fb398664f1a9859639992948` |
| Demailly author PDF | `6f4682f322d6ae0c0ce3feae4964792c473a3d9051fe01288ef9017ca341d009` |
| Matsumura published PDF | `382e6266c9eed07c8d2df8ce027de48a3dfc3a8377d70bef4f9953857a4a8b1d` |
| Both supplied and restored CURVE_PSH.tex | `9142aac73c5af7e4e715b3313def5ed56fae4e63e1ac8a53d0419df7d2194be9` |

Only Chapter 56 and current progress records change. Chapters 32,
51--55 and 57, the author sources, frozen comparison proofs, production
verifier records, research classifications and dated release artifacts
retain their previous bytes. These are local mathematical, source,
style, build and visual checks; no independent-agent or production
Rethlas verification and no research-atom closure are claimed.

The next bounded unit is Chapter 57's order-reflection argument:
check rational versus real valuation scaling, closedness of the
valuative parameter profiles at their endpoints, and the hypotheses
needed for Legendre inversion before passing from divisorial order
to all points. Preserve the separately frozen comparison interfaces.
