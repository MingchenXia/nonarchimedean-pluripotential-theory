# Matroid Snapper-polynomial integration — 5 October 2026

Appendix G9.7 introduces the known line-class Snapper formula, its
integer-weight magic positivity and its real-rooted generating numerator.
It distinguishes the combinatorial Euler functional on a nonproper
Bergman toric variety from sheaf Euler characteristic on a proper
wonderful realization. Appendix L28 identifies the sources and checks.

The baseline work-branch commit is
03b075a60667ca9522b0012612d0172129362c4e. This is an ordinary import and
exposition of existing mathematics, within the user's ongoing literature
integration request. It admits no original general theorem and records
no fresh independent production-model call or receipt.

## Source versions and actual reading

The controlling paper is Shiyue Li, *Magic positivity of Snapper
polynomials for matroids*, arXiv:2609.24917v1, submitted
21 September 2026 at 17:17:20 UTC. The 32-page PDF was acquired on
5 October at 12:27:43.804277 UTC, HTTP 200, 753,752 bytes, SHA-256
944b56af304d32e77847977615c717d0f2442c9d5a01dd75541b6b93ae2cfca2.
All 1,785 extracted-text newline positions were read in ten bounded
ranges, including the moduli-space applications and references.
The extraction's embedded-font warning is retained; controlling
formulas were inspected on actual PDF pages.

The following dependencies were selectively read, not read in full:

- Larson–Li–Payne–Proudfoot, *K-rings of wonderful varieties and matroids*,
  arXiv:2210.03169v2, revised 3 February 2024: 38 pages, 430,894 bytes,
  SHA-256 67658ab8acbe04abdbf63ae714574c1d34124a0f040580da29c9fcf7c3a82493.
  Text ranges 285–461 and 1499–1640 cover the definitions, exceptional
  isomorphism, Euler functional and section 7 proof.
- The author-hosted paginated published copy of that article, *Advances
  in Mathematics* 441 (2024), 109554,
  DOI 10.1016/j.aim.2024.109554: 43 pages, 687,853 bytes, SHA-256
  6ade53145a320a688337dc43bbab321b7395da6b2a184a6ac0c73137d2cbbaf5.
  Text ranges 1–38, 423–575 and 1728–1868 check the publication metadata,
  actual locators and Euler proof. It came from Sam Payne's institutional
  author page; an independent publisher-download byte identity is not
  asserted.
- Beck–Jochemko–McCullough, *h-star polynomials of zonotopes*,
  arXiv:1609.08596v3, revised 25 August 2017: 20 pages, 639,104 bytes,
  SHA-256 a470ed7ab14345dee12c76efab37f7f335a8e14ae70fb89eca0d35d091c64ed2.
  Text ranges 265–380 and 558–710 cover refined descents, the
  known interlacing input, cube proof and Corollary 4.5.
  Published metadata is *Transactions of the AMS* 371(3) (2019),
  2021–2042, DOI 10.1090/tran/7384.
- Backman–Eur–Simpson, *Simplicial generation of Chow rings of matroids*,
  arXiv:1905.07114v6, revised 15 March 2025: 37 pages, 502,000 bytes,
  SHA-256 0209c6104213b3057f0a38ffa79dab8c2220fdd05106f84ffcff0ae31af39ea2.
  Text range 1320–1450 covers the corrected transversal statement and
  direct quotient proof of the degree formula. Publisher metadata
  confirms *JEMS* 26(11) (2024), 4491–4535, DOI 10.4171/JEMS/1350,
  with online publication on 13 June 2023. The printed article is not
  asserted to include the 2025 arXiv correction.

All dependency PDFs were acquired by HTTP 200 on 5 October. Their exact
acquisition times, URLs and extraction diagnostics are preserved in the
ignored source_material/matroid_magic_positivity_20261005 cache.
The integration manifest retains its metadata and hashes.

Thirteen actual page sheets were viewed, containing 25 primary pages:
Li 2–3, 6–9, 11–12, 14–18 and 25; the LLPP published author copy
8–9 and 29–31; BJM 5–6, 10 and 12; BES 26–27.
Full controlling-text reading, selected dependency-text reading and
actual page inspection are separate claims.

## Known inputs and proof scope

The active argument retains the nonempty loopless ground set, rank at
least one and nonnegative integer weights on rank-two flats. Zero-weight
lines are removed before the polynomial degree is used. The degree need
not be rank minus one; the zero-weight or rank-one case is constant one.

LLPP Proposition 1.6 compares vector-bundle K-rings with the smooth
projective wonderful realization. Theorem 1.8 supplies the exceptional
integral ring isomorphism, with zeta(1-[L_F]^-1)=h_F. Section 1.5 defines
the Euler functional using 1+alpha+...+alpha^(r-1), and identifies its
realized sheaf-Euler meaning. It is not a proper pushforward from the
ambient nonproper toric variety. Neither zeta nor that factor is
identified with the classical Chern character or Todd class.

Corollary 7.5 supplies the rising-binomial formula. Singleton
dragon Hall–Rado inequalities for a rank-two flat restrict its
multiplicity to zero or one. Nonzero-subtuple inequalities then become
exactly the Dilworth-line independence inequalities, yielding Li
Theorem 3.6. The top-degree input BES Theorem 5.2.4 has its own
elementary-quotient proof, which was reviewed.

Theorem 3.7 partitions independent sets into lexicographic shelling
intervals. Its transformed factors 1+(weight-1)y are nonnegative
because retained integer weights are at least one. No arbitrary real
weight extension is asserted. BJM Corollary 4.5 identifies the
real-rooted numerator. Its general compatible refined-Eulerian input
from Savage–Visontai is an identified known input; that external paper
was not newly read in full and no fresh independent certificate is
claimed. BJM's last-letter n+1-j convention and Li's first-letter j
convention agree after reversing and complementing permutations.

Li's term “zonotopal class” refers to line-flat weights; a simplex on a
rank-two flat of cardinality at least three need not be a zonotope.
The moduli-space and saturated-class applications were read but supply
no active inputs at this checkpoint.

## Literal auxiliary issues excluded from the imports

1. Li's LLPP citations to Proposition 1.13, Theorem 1.16 and Lemma 1.20
   do not occur in either acquired LLPP edition. Actual locators are
   Proposition 1.6, Theorem 1.8 and section 1.5; Corollary 7.5 is unchanged.
2. The literal “strict for all subtuples” phrase in LLPP section 7 would
   include the zero subtuple and require 0>0. The operative domain is
   nonzero subtuples, as explicitly stated in Li; the zero DHR tuple is
   included and chi(1)=1 is preserved.
3. The fixed-element equivalence in the BES v6 Proposition 5.2.3 proof
   is too strong if read for one fixed element. For U_(2,3),
   A_1={1} and e=2, the collection {{e},A_1} has an independent
   transversal, while the singleton DHR inequality fails. The actual
   proposition quantifies over **every** nonloop element and is not
   refuted by this test. The degree input uses Theorem 5.2.4's
   separate quotient proof, not that literal fixed-element clause.
4. Li Proposition 5.7's linear-coefficient necessity step is false.
   The actual coefficient is y*H_d-d; at d=3,y=2 the magic vector
   is (1,2/3,-1/3,0). Its linear coefficient is positive although
   y<d, but full magic positivity still fails. The matroid
   Theorems 3.6–3.7 do not depend on that moduli-space step.
   No refutation of their statements or general repair is inferred.

These issues are not silently reused as proof inputs.

## Exact finite checks and independent surface calculation

The standard-library checker enumerates all 36 nonempty loopless
labelled matroids on one through four elements, with counts 1,2,6,27.
It tests all 2,032 line-weight assignments in {0,1,2}. Truncation basis
exchange holds, shelling intervals partition independent sets, and the
weighted shelling expression matches the magic transform. Exact finite
differences give the generating numerator. Magic and numerator
coefficients are nonnegative. Roots use quadratic and cubic
discriminants, with constant and linear cases separate; no Sturm or
higher-degree root claim is made. Three root-predicate self-checks
include the known local Kazhdan–Lusztig cubic of discriminant -268.

Twenty-eight refined-Eulerian basis cases through degree six are checked
by direct permutations of at most seven letters. This verifies the
transform identity and both letter conventions, not real-rootedness
in those higher degrees. Ten named graph/matroid profiles reproduce
Li's examples. Complete-graph profiles give 1+6q+15q^2+16q^3 for B4
and 1+6q+15q^2 for U34, with magic vectors (1,3,6,6) and (1,4,10) and
numerators 1+34t+55t^2+6t^3 and 1+19t+10t^2.

For a generic complex four-line arrangement, the wonderful surface is
the blowup of P2 at six distinct pairwise intersection points. The line
classes are pencils H-E_F. With intersection matrix
diag(1,-1,-1,-1,-1,-1,-1), canonical class -3H+sum(E_F) and chi(O)=1,
the all-one divisor satisfies D^2=30 and D.K=-12. Classical surface
Riemann–Roch gives the uniform polynomial above. All 729 integer
assignments in the same finite domain give coefficients 1, sum(weights)
and sum_(F<G) weight_F*weight_G. This uses known blowup geometry and
classical Riemann–Roch, not a new general positivity proof.

## Preservation and release evidence

Snapper, Ehrhart, ordinary toric cohomology, intersection cohomology,
local P and global Z retain distinct meanings. No Siu, general envelope,
non-nef closure or tropical-family comparison is inferred. All 42 complete
problem statuses, 108 protected Appendix M–N inputs and catalogue
source/PDF retain their bytes. Existing formal G/L statements and proofs
are byte preserved.

The companion manifest and artifact record retain the full-book build,
source closure, references, index, navigation and actual selected-page
review. Prior frozen exports are preserved; an isolated fresh compilation
from the new source archive is not claimed. Cloud-only work continues
and Xean remains suspended.
