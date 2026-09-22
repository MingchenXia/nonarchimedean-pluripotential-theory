# Chapter 52: projected operations and directed suprema — 23 September 2026

## Correction and dependent proof

Equation (52.25) previously identified the Legendre transform of the
modelized sum with the ordinary sum of rays, and the modelized maximum
with their pointwise maximum. Both equalities dropped the final model
envelope. They now appear as inequalities, while the exact equalities
are assigned to the raw sup-convolution and raw closed concave majorant.

The sum now uses the P-envelope for general test curves. Its
identification with the I-envelope is made only for I-model inputs,
where the raw positive-mass obstacle is I-good. The raw supremum is
proved psh using scalar biconjugacy and Kiselman's principle, with its
compact scalar parameter interval and extended-real endpoints specified.

The maximum is constructed in a fixed background by inverse Legendre
transform of the raw maximum, followed by the model envelope.
Its least-upper-bound property follows from concavity and envelope
monotonicity. Initial model potentials and typed Kähler transitions
are explicit; a transition identity after projection is not treated
as an identity for raw geodesic rays.

The dependent Chapter 54 passage and algebra proof are repaired.
Addition associativity uses the final model envelope of a triple
sup-convolution and the exact source result allowing insertion of
inner projections. Maximum associativity uses its least-upper-bound
property. Translation is an order isomorphism. These arguments
replace the former appeal to ordinary addition and maxima of rays.

## Two direct checks on the projective line

The two opposite coordinate actions give

    u_t = log(1 + (exp(t)-1) r),
    v_t = log(1 + (exp(t)-1) (1-r)).

At each level below 1, the maximum of the two test-curve potentials
is bounded because their poles occur at different points. The raw
concave majorant is therefore bounded, and its model projection is zero.
The joined curve has constant level zero up to terminal parameter 1,
so its ray is t. This strictly dominates max(u_t,v_t) for every
positive t and 0 < r < 1.

For w_t = u_t + v_t in the class 2 omega_FS, the initial velocity is
constant 1, and the initial acceleration is 2 r(1-r). The first
variation of the unnormalized energy gives

    E''(0) = 4 integral_0^1 r(1-r) dr = 2/3.

Thus the ordinary sum has nonaffine energy and is not a geodesic ray.
It cannot equal the ray of the modelized test-curve sum.

The integral was checked exactly with rational arithmetic.
Three independent numerical evaluations of the full curve energy,
using step sizes 0.02, 0.01 and 0.005, give second differences
0.6666488896, 0.6666622223 and 0.6666655556.
Thirty sampled pairs (t,r) corroborate the strict maximum inequality.
These checks supplement the analytical arguments; sampling is not
used as proof of either global conclusion.

## Suprema, countable reduction and transition

An arbitrary family now has a precise supremum construction:
form the modelized finite joins, then take the usc supremum of this
increasing net. The old proof omitted the finite joins and implicitly
assumed that a supremum of concave profiles is concave.

The countable reduction is applied to finite-join levels at rational
parameters. The union of the selected finite index sets is countable.
Nontrivial rational levels recover the common terminal parameter;
the closed decreasing profiles established in the preceding audit
recover every real level from left rational limits.
No countable cofinal subset of the original net is asserted.

The first three limit operations are explicitly in one fixed big class.
The positive-mass hypothesis for decreasing limits is retained.
Its transition compatibility is attributed to the source theorem using
the singularity metric, rather than to envelope idempotence alone.
Under rescaling by lambda, the Kähler perturbation also scales by lambda.

## Primary-source audit

The supplied author chapter was read without modification:
`author/chapter_testcurve.tex`, in the author's supplied lecture archive.
Its operations section contains labels def:sumtestcur, lma:testcurvplus,
prop:testcurvesumproperty, lma:testcursumcomp, def:testcurlor,
lma:testcurlor, cor:testcurvlorprop, lma:testcurlorPthetapomega,
def:testcursup, prop:supsincnetteestcur, def:testcurvsupsgeneral,
prop:testcurvChoquet and the transition lemmas.
Its SHA-256 remains
`b39e18f7e00c84916d791b54d8040bf6a2ad9a923f2c8e3497170ca2da7594d0`.

Exact locators were matched against the author's
[public final lecture manuscript](https://mingchenxia.github.io/Lectures/SGPT_final.pdf),
cover date July 18, 2026:

- Definition 9.4.2 and Lemma 9.4.2, pages 309--310: raw sup-convolution,
  P-projection and the I-model hypothesis.
- Proposition 9.4.1, pages 310--311: initial potential and associativity.
- Lemma 9.4.3, pages 311--312: the two-background transition formula.
- Definition 9.4.4 and Lemma 9.4.4, pages 313--314: the concave majorant
  and the separate model-envelope step.
- Corollary 9.4.1 and Lemma 9.4.5, pages 314--316: least upper bound
  and transition.
- Definitions 9.4.5--9.4.6 and Propositions 9.4.3--9.4.5,
  pages 316--319: increasing nets, finite joins and countable reduction.
- Lemmas 9.4.6--9.4.9, pages 317--321: transition for suprema,
  scaling and nondegenerate decreasing limits.

Source physical pages 325--326, 329--330 and 334--335 were rendered
and inspected. The PDF SHA-256 is
`c816eea5f06822021fa8dd75b70f82724ee47e6dcd6830729f5ecc109296b706`.
These exact locators are cited under the existing XiaBook key.

The [version history](https://arxiv.org/abs/2312.17150) of
*Operations on transcendental non-Archimedean metrics* identifies
version 3 as dated 22 October 2024. Its
[versioned PDF](https://arxiv.org/pdf/2312.17150v3) was checked at
Definitions 4.5, 4.12 and 4.15 and Lemma 4.17:
it likewise retains model projection in maxima and addition and
finite joins in arbitrary suprema.
PDF SHA-256:
`773eea71af9f1fff112bf5fcab2b9046b81467df2e37165ee1da3949ff74c6d9`.
The author's [homepage](https://mingchenxia.github.io/) warns that the
published volume contains an earlier version. Accordingly, this audit
does not assign the checked arXiv locators to the published chapter.
No bibliography entry was rewritten. The new precise book citations
use the separately checked lecture manuscript.

## Validation, preservation and remaining work

The full build succeeds with 3,929 pages and 18,659,359 bytes.
There are no unresolved references or citations and no horizontal or
vertical overflows. The remaining class-name warning is pre-existing.
The initial build and the subsequent mathematical and layout passes
all completed; the final short proposition is kept together on one page.

Final physical pages 3199--3203 and 3206 (Chapter 52) and 3218--3220
(Chapter 54, including the following section boundary) were rendered and
inspected. The final edited blocks pass the strict writing audit with
zero errors and zero warnings. Legacy untouched optional titles and
inline delimiters were not included in that scoped style claim.

The complete closure has 389 TeX inputs and 11,522 unique labels:
no missing input, duplicate label, dangling reference or structural defect.
The active research inventory is unchanged: 46 atoms in 14 formal
environments, with tiers (0,5,8,16,17). The second mathematical pass
checked class types, the I-model hypotheses, extended scalar endpoints,
raw-versus-projected transforms, the finite-join step, countability,
the scaling of perturbations and both projective-line calculations.

PDF SHA-256:
`64777e02b260e6d30365196cf731fc25c5c496b36d7900b3aa7e37f86c2481be`

Chapter 52 SHA-256:
`a5879cbe5df3ca4677c99663cb4430546f8d669b5aa0266e6cccaf5b1991e4c9`

Chapter 54 SHA-256:
`7aa58523c6064807bd6cfa4b5ece19610fb93fd5619fbe95a8fabe2d21df6437`

The author-supplied CURVE_PSH.tex is still byte-identical to its
recovered repository copy. The consulted author chapter, Chapter 62,
all other manuscript sources, frozen research packets, verifier records,
bibliography databases and dated release artifacts were not edited.
The current PDF remains an ignored local build artifact. This is a
local source/proof/style/build audit, not a production Rethlas gate or
an independent-agent verification.


The next bounded audit is the Chapter 53--54 perturbation argument:
check order reflection and the uniform positive-mass bound obtained
from a smaller Kähler perturbation before forming a decreasing
inverse-system limit. The present unit does not claim a new
research-frontier theorem, close an active research atom, or independently
reverify the general singularity-metric and model-envelope inputs.
