# K3 hybrid dynamics: exact-source review

Date: 6 October 2026 UTC. Baseline work commit:
`c121c1faf468376f07ad7b09814c89a226dda859`; main:
`00957114db21b627e97369563032ceda9cea09c7`.

Irokawa's **arXiv:2405.12517v1** claims hybrid weak convergence from
Cantat's complex invariant measures to Filip's non-Archimedean invariant
measure for a meromorphically degenerating projective K3 family with
hyperbolic automorphisms. All eighteen actual PDF pages, including the
proofs and references, were read and displayed. The current arXiv record
lists only v1, submitted 21 May 2024, 06:08:26 UTC. This review does not
certify its proof or refute the underlying measure-limit theorem.

The decisive normalization issue occurs before the hybrid limit:
the printed backward potential uses the reciprocal eigenvalue as its
normalizing denominator, so its associated current grows instead of
being rescaled down. The resulting printed mixed approximants have
unbounded mass on a fixed projective K3 surface. Filip's checked source
uses the same decaying factor in both iteration directions. Further
issues involve model multiplicities, positivity, local frames and the
last integration-by-parts argument. They are retained individually below.

## Controlling editions and actual reading

* **Irokawa, K3 hybrid paper**, [2405.12517v1](https://arxiv.org/pdf/2405.12517v1):
  18 pages, 286,799 bytes, SHA-256
  `7363f584d7bdffae9674dd25b93c96b424f8e42e01416f0d0104e245c88da969`.
  All pages were read and displayed in nine sheets. Main claims:
  Theorem 1.1 on page 2; Theorems 5.4 and 5.5 on page 13, with proof
  concluding on page 17. This is the only complete paper reading here.
* **Filip, Tropical Dynamics of Area-Preserving Maps**, exact
  [1903.00794v1](https://arxiv.org/pdf/1903.00794v1): 59 actual pages,
  5,715,456 bytes, SHA-256
  `42bf93a25fafe9048d1a69adb0195ad2104db03938da5e632c908166de5515a5`.
  Pages **1–4, 14–15, 27–38** were read and displayed: eighteen pages.
  The arXiv metadata says 58 pages and submission on 2 March 2019;
  the PDF itself prints a 5 March revision date. These facts are kept
  distinct. The published article is J. Modern Dynamics 14 (2019),
  179–226, DOI 10.3934/jmd.2019007, with publisher metadata checked.
  Its public export returned an empty response and the advertised static
  path returned 404; no published PDF reading or numbering is claimed.
* **Cantat, Dynamique des automorphismes des surfaces K3**, published
  Acta Math. 187 (2001), 1–57, [digitized journal PDF](https://archive.ymsc.tsinghua.edu.cn/pacm_download/117/6611-11511_2006_Article_BF02392831.pdf):
  57 pages, 3,069,085 bytes, SHA-256
  `fd7b7c3afeaeec0fad0ebd8c720792416a3b68a81ce92b5d3a074b1e8be946d5`.
  Pages **1, 7–8, 11–15, 18–24** were read and displayed: fifteen pages.
  OCR is imperfect; the original page images were also inspected.
  The filename's 2006 string does not supersede the journal's 2001 date.
* **Demailly, Monge-Ampère Operators, Lelong Numbers and Intersection
  Theory**, [author PDF](https://www-fourier.univ-grenoble-alpes.fr/~demailly/manuscripts/trento.pdf):
  71 author pages, 625,248 bytes, SHA-256
  `1e0b0e8aadadc5ca4876d84b3789952a38f412d7e71fd7df3a126cc130f3f8d1`.
  Pages **5–9** were read and displayed. The normalization, integration
  by parts, locally bounded product construction, CLN estimate and
  Corollary 1.6 with its complete proof were checked. The later monotone
  theorem's statement was read, but its whole proof was not selected.
  These are author-layout locators, not the 1993 volume's page numbers.

There are **56 fresh source/page pairs in 29 displayed sheets**:
18 main pages and 38 dependency pages. Three dependency papers have
selected scopes. The preceding polynomial-dynamics source review is
reused for Favre's positive hybrid scaling, BE21's positivity and
regularizability distinctions, the CLD product-class boundaries and
Chambert–Loir's model multiplicities. That reused evidence is not counted
as a fresh reading or extended to unselected foundation chapters.

## Scoped diagnostics in the K3 v1

**K01 — Picard group versus real (1,1)-cohomology, page 3.** The asserted
isomorphism between these real spaces is false in general: a complex K3
has h(1,1)=20, while its Picard rank can be smaller. The eigenlines lie
in the real Néron–Severi space for projective hyperbolic dynamics; the
whole spaces need not coincide. Cantat pages 7–8 distinguish them.

**K02 — continuous-potential locator, page 3.** Cantat's Theorem 2.4
provides existence and uniqueness of eigen-currents on pages 13–15.
Projective continuous potentials are Theorem 3.1, proved on pages
18–21; the invariant measure is defined in Section 3.3 on page 22.
Use both anchors and state whether eigenlabels refer to pushforward or
pullback. The paper acknowledges that convention switch on pages 5–6.

**K03 — residue characteristic, page 3.** The stated general
non-Archimedean input assumes characteristic zero for the field alone.
Filip's checked setup also assumes residue characteristic zero. The
application to C((t)) meets both conditions; no mixed-characteristic
extension is licensed by the read source.

**K04 — complex differential normalization, pages 7–8.** The displayed
d^c=(partial−bar-partial)/(i pi) is twice Demailly's normalization on
author pages 5–6. Taken literally it gives dd^c log|z|=2 delta_0,
contrary to the following unit-multiplicity integration-current claim.
Restore the factor 1/2 and consistently use the first-Chern convention.
Probability rescaling does not fix incompatible intermediate identities.

**K05 — ideal evaluation, page 7.** Logarithmic norm evaluation of a
generated ideal uses the maximum of the generator norms, equivalently
the minimum of their negative logarithmic valuations. The printed
infimum of logarithmic norms is generator-dependent: generators (1)
and (1,t) describe the same unit ideal but give 0 and log r respectively.
The complex model weight also need not be nonnegative, as its declared
codomain suggests.

**K06 — generator category and domains, page 7.** Local ideal generators
belong to a chart algebra, not generally to the coefficient ring Ar.
For example (t,x) needs the coordinate x. Independence of a formal
model's ideal norm is evaluated on its model domains, not on arbitrary
hybrid points without a frame and bounded-coordinate specification.

**K07 — special-fibre multiplicities, pages 8–10.** The atomic model
measure and mixed limit omit b_E, although page 8 correctly writes
[X_0]=sum b_E[E]. The omitted factors change total mass on nonreduced
snc fibres. A concrete dimension-one check blows up a point of the
central fibre of P^1 x D, then the intersection of the two components.
The three resulting components have multiplicities (1,1,2) and
intersection matrix

    [-2  0  1]
    [ 0 -2  1]
    [ 1  1 -1].

The pullback of O(4), twisted by twice the first component plus the
third, has degrees (1,1,1). It is relatively ample and its generic
degree is 4. The printed unweighted central sum is 3; the weighted
sum is 4. This tests the stated general Proposition 4.1, not the K3
hybrid-limit theorem with correctly defined canonical measures.

**K08 — semipositivity and regularization, page 8.** Uniform limits of
arbitrary model metrics do not acquire positive curvature. The complex
metrics also require psh hypotheses. Retain relatively nef/semipositive
approximants and the precise psh-regularizable or locally approachable
classes; BE21 does not assert positivity from modelhood alone.

**K09 — line-bundle and lift data, page 11.** Coordinates of an arbitrary
ample bundle in an ample integral basis need not all be natural numbers;
one may instead explicitly choose a positive sum. A local lifted map
has nonvanishing coefficient functions as well as its monomial matrix.
Cantat's Remark 3.2 on page 20 exhibits these units. The paper later
reintroduces transition functions; keep source/range charts, units and
the character/cocharacter convention throughout.

**K10 — backward normalization, pages 11–13.** For a positive integer n,
the displayed definition gives G_{-n}=lambda^n times the unnormalized
backward potential. The correct expanding dynamics of f^{-1} also has
spectral radius lambda>1 and requires lambda^{-n}, just like the forward
direction. Filip's Corollary 5.6.8 on page 38 explicitly uses
lambda^{-n}(f^{+/-n})^*c_1(L). The printed signed-index normalization
cannot yield the asserted continuous backward limit.

**K11 — mass of mixed approximants, pages 12–13.** The printed factors
lambda^n and lambda^{-n} cancel in Proposition 5.2, leaving the mixed
pullbacks without lambda^{-2n}. In the standard first-Chern convention,
write an ample class as H=a alpha_+ + b alpha_- + w, where a,b>0,
q=alpha_+.alpha_->0, the eigenclasses are isotropic, and w belongs to
their negative-definite orthogonal complement. Then

    ((f^n)^*H . (f^{-n})^*H)
      = abq (lambda^{2n}+lambda^{-2n}) + O(1).

The raw masses therefore diverge. After multiplying both currents by
lambda^{-n}, their mixed masses tend to abq>0. Tensor-power division
by m^2 removes only tensor degree; it does not remove this exponential
growth. Filip page 38 retains lambda^{-2n}. This is a definite failure
of the printed approximant convergence on a fixed fibre, not a
counterexample to convergence of the correctly normalized invariant
measures in a degenerating family.

**K12 — changing homogeneity and chart scope, pages 13–16.** These
torsor potentials have changing real characters. Their differences can
be compared on compact subsets of the torsor or on compact chart
domains with bounded frames. A supremum over whole Zariski charts is
not generally finite: multiplying a section by a unit with a pole at
the deleted boundary exposes the nonzero character difference. Filip
Theorem 5.6.5, page 36, explicitly shrinks to precompact domains.
A meromorphic family's compact source/range model domains and vertical
orders are needed for a uniform logarithmic parameter estimate.

**K13 — spectral estimate and tail, pages 14–16.** The normalized matrix
convergence follows from the hyperbolic eigenvalues and the bounded
orthogonal action, but its displayed proof drops powers of unit-modulus
eigenvalues and one normalization factor. The recurrence needs delta>1.
If delta is smaller than lambda, its convolution is bounded using a
decay rate at most min(delta,lambda), rather than the faster printed
lambda rate. The final epsilon_n sum also uses n in every summand while
summing over i, so it is literally an infinite sum of one positive
constant. A genuine indexed geometric tail is required. None of these
display repairs settles the missing model-domain estimate by itself.

**K14 — non-Archimedean wedge continuity, page 13.** Attribute the
directional normalized potentials to Filip's actual statement and
ensure their products lie in the applicable non-Archimedean product
class. Locally uniform convergence of unspecified continuous functions
is insufficient to invoke a positive wedge operator. CLD editions and
their original numbering must remain distinct from the 2025 foundation
edition previously selected by the book.

**K15 — relative weights and positivity, pages 16–17.** The model test
function is a global relative weight. Its dd^c need not be positive;
positivity belongs to the reference curvature plus that dd^c. For a
global smooth relative function phi and a closed current T on a compact
surface, the integral of dd^c phi wedge T is zero by Stokes. The claimed
strictly positive cohomological integral cannot supply the required
bound. Retain reference curvature and control signed measures by total
variation or positive witnesses, with bounded cohomological masses.

**K16 — local integration by parts, pages 16–17.** A partition of unity
introduces its derivatives. They do not disappear from dd^c of the
cutoff times the test function. Also, the first display equates an
integral against eta_t to a finite-n product. That product represents
eta_{n,t}; the limit product uses both limiting potentials. A full
local argument must keep the two measures, cutoffs and cross terms.

**K17 — signed model values, page 10.** The error coefficient involving
2+sum g(x_E) need not be nonnegative. A vertical datum (t^N) makes model
values negative. Use absolute model values and the actual sup norm;
boundedness does not mean the bound equals 1.

**K18 — hybrid sign, pages 16–17.** The earlier definition correctly uses
log r/log|t|>0. The proof later replaces its denominator by log|t|^{-1}
without replacing the numerator by -log r. The absolute error uses the
right magnitude, but the preceding signed identity is inconsistent.

**K19 — last finite-n convergence reference, page 17.** The printed
reference to Theorem 5.5 cites the result being proved. The needed input
is Proposition 5.3 for fixed n. With an independently justified uniform
approximation and fixed-n mixed limit, the stated three-term argument
is the usual valid order of quantifiers: choose n, then choose t.

## Dependency boundaries

Filip's selected v1 distinguishes fixed real homogeneity from changing
approximant homogeneity, uses compact torsor subsets and delta>1, and
normalizes both directional currents down. Its field setup on page 27
requires completeness and characteristic zero also in the residue field.
The displayed uncompleted union of Puiseux fields is not itself complete;
use its completion if it is to instantiate that setup. The double
O(-1) label in the Weil/dual discussion on page 30 is not a license to
regard the tautological bundle as positive.

Cantat's lift proof uses an integral torus automorphism; its displayed
SL restriction on page 19 should not exclude GL matrices of determinant
-1. The stronger pointwise subsequence inference in Proposition 3.4(3),
page 24, does not follow from bounded psh compactness alone. This review
uses the explicitly uniform construction and Demailly's uniform
continuity input; it does not import an unrestricted pointwise
compactness principle. No verdict on all of Cantat's ergodic or
laminarity results, all of Filip's tropical dynamics, or the complete
CLD foundations is claimed.

## Preservation and next integration

This is a **source-only** checkpoint. All 425 active TeX inputs, both
bibliography files, 108 protected inputs, compiled book/index outputs,
81 prior frozen manifests, 142 exports and the 42-atom canonical
inventory are byte-preserved. The native catalogue source/PDF and open
editor are unchanged and are not recompiled or reopened. The checked
4,417-page index-polished book is reused, with no fresh book-page
reading or build claimed. No original result, model call or production
receipt is added, and no historical receipt scope is extended. The
BJ22 Theorem 6.21 Siu/envelope boundary remains unchanged.

Save the source reading records, diagnostic computations and preservation
gate in an immutable manifest, fetch main and work, publish normally
on work and update the existing draft PR. A later book insertion may
explain Cantat/Filip eigen-currents, symmetric degree normalization and
the conditional mixed hybrid passage. It must retain the uniform
meromorphic estimate and applicable product classes as inputs until
they are actually proved in the stated family setting. Continue with
Favre–Gong 2406.15892v4, revised 20 June 2026: its PDF is acquired but
its text has not been read at this checkpoint.
