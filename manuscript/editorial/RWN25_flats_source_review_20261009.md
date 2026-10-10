# Infinite-dimensional flats: revised support construction and proof interfaces

Date: 9 October 2026. Controlling primary: Rémi Reboulet and David Witt
Nyström, *Infinite-dimensional flats in the space of positive metrics on
an ample line bundle*, arXiv:2311.13451v2, 29 October 2025, 19 physical
pages. PDF SHA256:
40c18258943422946d29ea91e755a33313d6893709f1bc7c851bb51a19464f90.
All nineteen pages were actually read in order with complete selected
text, ten individually displayed matching images and ten chronological
notes/receipts. The IMRN 2025 edition is bibliographically identified,
but its publisher PDF fetch returned HTTP 429; no published-PDF byte
identity or reading is claimed.

The revised source supplies an explicit finite spectral-domain extension
and a useful algebraic decreasing-convex construction. Its main flat
theorem still requires consistently calibrated quantization, precise
endpoint/function conventions and the bounded completion argument.
This audit does not declare the intended corrected theorem false or
claim an independent hostile-model receipt. Eleven elementary
diagnostic families separate literal display defects from those
dependencies. The 4,661-page book, its core inputs and bibliographies,
native catalogue and canonical 42-atom/twelve-problem inventory are
unchanged. General BJ22 critical homogeneous Siu/envelopes remain OPEN,
LPWZ density UNVERIFIED, and the BJ22 Theorem 6.21 warning remains binding.

## The actual support repair

The setting is a compact projective complex manifold with an ample line
bundle L and a continuous positive initial metric. The filtration norm
is homogeneous for the trivial absolute value on C; it is a different
category from a complex Hermitian norm. Section 2.1 uses the genuine
bound exp(-delta k) times the trivial norm <= F_k <= exp(delta k) times
the trivial norm. The complex graded class in Definition 1.3 likewise
compares with sup norms of a bounded positive metric, rather than an
unrestricted comparison sequence. These are meaningful reference bounds.

Write lambda=-log F_k(s)/k. Section 2.2 explicitly acknowledges that
finite-degree lambda values can lie below the support [a,b] of the
limiting DH measure. For a convex decreasing f with finite right
derivative at a, it extends f below a affinely with that slope, to a
fixed interval containing all finite-degree spectral values. This
procedure is declared implicit in the subsequent formulas. A sign slip
in the explanation writes positive log F/k; the measure and actual
construction use negative log F/k.

This supplies a separate source convention relevant to the preceding
[Reboulet 2026 audit](Reboulet_filtrations_source_review_20261009.md).
That audit's finite-outlier example remains valid, but the present
revision shows how the cited finite-right-derivative construction
addresses its domain. This is an additional input, not a retroactive
change to the earlier frozen reading or a blanket proof of its whole
function-cone claim. General unbounded-derivative functions are handled
later through completion, not by this affine finite-degree formula alone.

The outlier is concrete. On (P1,O(1)), the trivially valued monomial
norm with weights (exp(k),1,...,1) is submultiplicative and linearly
bounded. Its normalized law is (delta_-1+k delta_0)/(k+1), with limiting
support {0}, yet the constant monomial requires f(-1). Extension
choices there become invisible to finite-p limiting probabilities when
the relevant continuous bounded integrands share a fixed interval.
They need not become invisible to the strong infinity metric. Any
claim of representative independence must name that topology and,
for positive metrics, the quantization input that transfers it.

## Algebraic constructions that can be followed directly

Theorem 2.2 assigns a modified trivially valued norm the basis weights
exp(k f(lambda)). If u and v have original negative-log weights alpha
and beta, each nonzero product coefficient has weight delta>=alpha+beta.
Decreasing f and convexity give

    (m+n) f(delta/(m+n))
      <= m f(alpha/m)+n f(beta/n).

Taking maxima proves the product inequality; ultrametric sums extend it
to arbitrary sections. The two-sided bound is sup |extended f| on the
full finite spectral interval. The printed constant sup f does not
work for negative constants. For nonzero vectors the modified norm
applies an increasing transform to the original norm level, which
also explains its independence of the chosen adapted basis.

Section 3 uses the complex sum-envelope

    A(eta,F)(w) = inf_{w=sum w_i} sum_i eta(w_i)F(w_i).

Finite positive upper/lower bounds on F make this a genuine complex
norm. For two submultiplicative graded inputs, product decompositions
give the double sum of costs over all u_q v_r; bounding and factoring
it proves submultiplicativity after taking infima. The printed proof
in Theorem 3.2 omits those sums and several f subscripts. With them
restored, its mechanism is the direct norm-envelope product argument.

This sum-envelope is generally not the weighted Hermitian norm, despite
the equality claimed on page 13. Take eta(a,b)=sqrt(|a|^2+|b|^2) and
the trivial-absolute-value norm F with weights (1,sqrt(2)). The weighted
Hermitian norm H(a,b)=sqrt(|a|^2+2|b|^2) has H(1,1)=sqrt(3), whereas
A(1,1)=2. A single-piece decomposition gives the upper bound 2. The
linear functional a+b is dominated by eta F: on b=0 it is |a|, and
off that line Cauchy–Schwarz gives |a+b|<=sqrt(2)eta(a,b). Every
decomposition cost is therefore at least 2. The same reasoning with
a-b gives A(1,-1)=2, so A violates the Hermitian parallelogram law
(8 on the left versus 6 on the right).

The actual needed interface is an approximation. In an eta-orthogonal,
F-adapted basis, H is below the product gauge and hence H<=A. Coordinate
decomposition gives A<=sum_i eta_i F_i |c_i|<=sqrt(N)H. Combining
this with ordinary norm comparison gives a logarithmic-rank error of
the type used in Lemma 3.1. Since N_k=O(k^n), log(N_k)/k tends to zero.
Thus the false finite equality does not refute the intended
Bernstein–Markov transfer or asymptotic flat theorem.

## Quantization and measure calibration

The following conventions cannot be combined literally as printed.
They require one consistent choice before the isometry is imported.

* Hermitian norm lengths have the quadratic formula. Proposition 1.1's
  geodesic uses a sum of absolute coordinates instead of the square
  root of the sum of squared weighted coordinates. At equal Euclidean
  endpoints it gives 2 at (1,1), instead of sqrt(2).
* A filtration weight sup{lambda:v in F^lambda} is not a positive
  norm; the required expression is its negative exponential. The body
  uses exp(-a_i), correcting the introductory formula.
* For a squared metric potential, a constant shift c changes L2 norm
  lengths by exp(-kc/2). The printed sup norm instead changes them by
  exp(-kc). Formula (3.2) changes Hermitian lengths by exp(kf), which
  gives squared FS weights exp(-2kf), while the introduction uses
  exp(-kf). The FS denominator is eta(v_i)^2, not exp(2 eta(v_i))
  as in literal (1.6). Degree division is missing in two FS limit
  displays although the Fekete proof uses it correctly.
* The finite norm spectral probability has mass one and uses 1/N_k.
  The source's DH measure uses k^{-n} sum delta_lambda and has the
  Hilbert leading-coefficient mass. Their conversion is k^n/N_k.
  On (P1,O(2)), N_k=2k+1 and the DH mass tends to 2, not 1.
  The MA mass convention must agree with the chosen spectral mass.
* The main calculation needs k^{-p}d_{p,k}^p, not k^{-1}d_{p,k}^p.
  With f=1 and g=0 all norm slopes are k; for p=2 the printed left
  side grows as k instead of remaining 1. Its finite integral also
  needs the extended full spectral interval, not the limiting support
  alone when outliers occur.

The arbitrary-sequence limsup version of the maximum identity (1.5)
has a separate issue. For xi_k=exp((-1)^k k)eta_k, the normalized d1
distance is always 1. Its two distances to the Hermitian maximum
alternate between zero and one, and each limsup is 1; their sum is
2. An actual common limit, or an appropriate submultiplicative
convergence theorem, is needed. The finite identity remains valid.
The short Ep characterization also needs full non-pluripolar MA mass,
not just a finite pth integral against a possibly mass-losing measure.
The original Darvas completion and Finski quantization statements must
control these premises and factors.

## Completion, endpoints and research scope

Theorem 3.5 replaces f near a by the chord from f(a) to f(a+epsilon),
obtaining a finite-right-derivative approximation. For continuous f at
a this converges uniformly. A bounded convex decreasing function can
have an endpoint jump: on [0,1], f(0)=1 and f(x)=0 for x>0 is such a
function. Its chord approximants converge in finite Lp for Lebesgue
measure but not uniformly. It has zero Lp distance from g=0 despite
being a different pointwise function. The asserted injectivity therefore
requires an a.e. quotient or an appropriate representative class.

Finite-p completeness supplies a limit in Ep. An increasing sequence
of bounded metrics does not on its own supply a bounded limit; a
common uniform bound is necessary. Also, affine extensions of the
chord approximations below a can grow as their slopes tend to minus
infinity, and their order there differs from their decreasing order
on the support. A fuller argument can first establish calibrated
extension independence, compare functions via compatible extensions,
and then use constant functions to provide bounds based on their
common range on S. Those steps must be stated; they are not established
by the source's single sentence about increasing bounded approximation.

Section 3.4 asks whether two arbitrary continuous positive metrics
share one filtration flat cone, proposes extensions to big,
prescribed-singularity and Kahler settings, and asks about the appearance
of the entire convex-function cone under a metrized toric degeneration.
These source-stated directions supplement the research discussion,
without adding or resolving a canonical atom.

For its toric sentence, multiplicativity of a norm alone does not
allow removal of decreasing f for every adapted-basis choice. Use
F=exp(-ord_X1) on C[X0,X1], the adapted degree-one basis
(X0+X1,X1), and monomial bases in degree two. With f(x)=x, the
modified norm of X0+X1 is 1 but that of its square is exp(2).
Actual multiplicative toric monomial bases make each monomial product
have one additive weight; Jensen then gives the intended all-convex
construction. The basis and equivariance premises must remain visible.

## Evidence and continuing source work

This checkpoint preserves the actual notes, receipts and eleven
elementary diagnostic families. Preparation, checksum/export work and
upload add zero reading credit. The complete external primary evidence
stays in a separate cloud archive; the GitHub checkpoint contains
authored records. No new whole-book pass is claimed: the last complete
ordered pass remains 4 October.

The Fin22 key in this source denotes arXiv:2210.03039, whereas the
2026 paper's Fin22 denotes arXiv:2209.03853. Exact locators must follow
their own keys and editions. Cloud copies of the 2025 PLMS author
edition and a partial Parreau author-PDF review already exist; inspect
their actual coverage before acquisition or new reading. The old
partial scopes are not silently enlarged. Continue with the controlling
Finski isometry, Parreau Proposition 2.18, BE21 Theorem 9.5 and the
original analytic/lattice inputs. Check incoming GitHub author research
and publish verified evidence regularly. Xean stays suspended.
