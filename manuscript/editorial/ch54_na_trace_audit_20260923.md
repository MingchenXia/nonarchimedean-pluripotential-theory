# Chapter 54: non-Archimedean trace, mass and endpoints

Audit date: 23 September 2026.

## Construction and domain

The trace construction in Section 54.7 is now proved before it is used as an
inverse-system component. The former proof asserted positive mass from the
domain condition without supplying the needed lower bound.

At each fixed interior parameter, all ambient perturbed components are
I-equivalent: compare them with a common smaller Kähler perturbation.
Their generic Lelong numbers along Y are therefore equal. Monotonicity in
the level parameter makes the zero-Lelong set an initial interval.
Thus the domain can be tested at one interior level in one perturbation.
Its supremum c_Y(Gamma) is finite, independent of perturbation, and at
most Gamma_max. Every strictly smaller level belongs to the analytic
trace domain. The former warning about a terminal-level test has been
replaced by these precise statements.

For a target Kähler perturbation eta, set beta = rho^* theta + eta and
choose an ambient perturbation with rho^* omega_tilde <= eta/4.
For a quasi-equisingular approximation a_k of one ambient level, a tail
has epsilon_k rho^* omega_0 <= eta/4. Consequently the nontrivial analytic
restrictions r_k = rho^* a_k satisfy

    beta + ddc r_k >= eta/2,
    integral <(beta + ddc r_k)^m> >= 2^(-m) integral eta^m > 0.

The bound is independent of the level and the approximation index in its
tail; the starting index of that tail may depend on the level.
The decreasing normalized model envelopes converge with this bound.
Their limit has the analytic trace class and is I-good, so its P-envelope
and I-envelope agree. This constructs the target normalized level and
proves its positivity. Dimension zero is treated separately, with
normalized constant zero and mass one.

The inner trace in (54.30) now uses the class-valued analytic trace.
Existence of a representative in the target beta is established by the
preceding construction, rather than assuming a representative exists in
the smaller restricted ambient background. This agrees with the
class-valued formula in the checked operations-paper version.

## Test curves, compatibility and birational pullback

The proof verifies decreasing order and concavity after normalization.
The convex combination of two target levels is beta-psh and nonpositive;
analytic trace calculus puts it below the intermediate trace in P-order.
The order description of the I-envelope converts that comparison into a
pointwise inequality. The usc-regularized initial supremum has positive
mass and is I-model by increasing closure.

The cutoff level is the decreasing left limit of normalized levels.
The uniform mass floor survives there, and decreasing I-model closure
gives its normalization. Only levels strictly beyond the cutoff are
identically -infinity. Perturbation compatibility is proved for interior
levels by equality of trace classes, at the cutoff by positive-mass
decreasing d_S continuity, and at the initial level by increasing
envelope continuity.

The birational statement explicitly requires a smooth compact Kähler
ambient manifold upstairs, as in the analytic trace input. Generic Lelong
numbers agree near the generic isomorphism locus, giving the same domain
and cutoff. The proof uses the precise analytic pullback lemma, whose
approximants commute with restriction on the entire normalization.
Projection to a common target background gives equal normalized levels.
The argument is not inferred solely from equality on the isomorphism
locus, and makes no claim about ambient regularization on arbitrary
singular spaces.

## Worked cutoff and its Chapter 52 dependency

The existing hyperplane filtration on P2 has ambient terminal parameter 1
and generic Lelong profile max(tau,0) along H. Its trace along H has cutoff
0 and constant minimal-singularity levels up to and including that cutoff.
This computes a strict drop in the terminal parameter and makes the
retained endpoint visible.

While checking this dependency, two points in Example 52.6.2 were repaired:

- The displayed monomial formula for the filtration is stated for
  tau >= 0. For tau <= 0, the filtration is the entire section space;
  a negative power of the hyperplane equation must not be used to describe
  a holomorphic section subspace.
- Analytic singularities use rational coefficients in this manuscript.
  For irrational levels, the bounded equivalence with tau times the
  divisor weight instead gives I-goodness by positive real scaling.
  This is the property needed to identify the P- and I-envelopes.

The bounded-difference argument was retained and shortened to avoid
leaving the last three lines of Chapter 52 alone on an extra page.

## Sources and second pass

Primary locators were checked in
[Xia, Operations on transcendental non-Archimedean metrics, arXiv v3](https://arxiv.org/pdf/2312.17150v3),
22 October 2024:

- Definitions 4.18 and 4.20, page 18: the trace domain and component
  formula on the normalization.
- Section 4.8, pages 20--21: birational pullback of non-Archimedean
  metrics and operations.

The version-specific XiaOperationsV3 entry is retained, separately from
the published chapter. The author's
[final lecture manuscript](https://mingchenxia.github.io/Lectures/SGPT_final.pdf),
18 July 2026, supplies the following further locators:

- Definition 13.2.8, page 433, and Proposition 13.2.19, pages 434--435:
  the general Kähler trace construction and birational statement.
- Lemma 8.2.1, pages 266--267: analytic trace and bimeromorphic pullback;
  its inputs include Corollary 7.1.3 (quasi-equisingular pullback),
  Lemma 6.1.4 and Corollary 6.2.3.
- Corollary 6.2.7, pages 215--216: decreasing model-envelope convergence
  with a uniform positive mass floor.
- Corollary 6.1.3, page 199: the order candidate description of the
  I-envelope.
- Propositions 3.2.12--3.2.13, page 129: decreasing and increasing
  I-model closure.
- Theorem 6.2.3, page 227: continuity of the I-envelope in d_S.
- Proposition 7.2.1, pages 239--240: I-goodness under positive real scaling.
- Appendix B.3, pages 504--505: the normal-target calculus.

Lecture physical pages 283 and 449--451, and operations-paper page 18,
were rendered and inspected. The other locators were checked in source
text. The supplied chapter_NApotential.tex, chapter_trace.tex and
chapter_testcurve.tex were read without alteration.
The chapter source note now distinguishes the accepted trace-paper
version DXTraceV2, Section 3, and lecture Sections 8.1--8.2.

The second mathematical pass checked the direction of perturbation
transitions, the pointwise candidate argument for concavity, the
level-independent mass bound with a level-dependent tail, both endpoint
limits, the zero-dimensional case, the birational source hypotheses,
and the nonpositive and irrational parameters in the worked example.
The initial diff-only style extraction omitted unchanged semantic labels;
the final strict audit used complete edited blocks and excluded untouched
legacy markup.

## Validation and preservation

- The final complete `latexmk` build passes: 3,939 pages, 18,707,423 bytes.
- `refcheck.py` passes on 389 TeX inputs and 11,548 unique labels:
  no missing inputs, duplicate labels, dangling references or structural errors.
- The final log contains no unresolved references or citations and no
  horizontal or vertical overflow. Existing underfull-box and class-name
  warnings remain outside this unit.
- The open-problem inventory passes: 46 active atoms in 14 environments,
  with tiers `(0,5,8,16,17)`.
- The strict style audit of complete edited blocks reports zero errors
  and zero warnings. `git diff --check` passes.
- Final PDF physical pages 3206--3207 and 3231--3235 were rendered and
  inspected. The Chapter 52 end now fits on printed page 3138; Chapter 53
  starts immediately on page 3139. The new construction, mass estimate,
  endpoint, example and source note occupy printed pages 3163--3167,
  with no clipped text or display overlap.
- Protected Chapters 51, 53 and 62 retain their preceding checked hashes.
  The supplied `CURVE_PSH.tex` and the restored repository copy remain
  byte-identical, SHA-256
  `9142aac73c5af7e4e715b3313def5ed56fae4e63e1ac8a53d0419df7d2194be9`.

Final SHA-256 records:

| File | SHA-256 |
| --- | --- |
| Current local `book.pdf` | `a6eabee2793d08a614841dcf7153a608133a7373cd0fa18b48cf9f21729c6a8b` |
| `ch52_rays_test_curves.tex` | `4ecefa847652933a28ced0aee5254781ed818bc3768fc0ad5e4e65fb4aa171e8` |
| `ch54_operations_trace.tex` | `bfccc0ecb36c4a0afe016c0397b6d2bae943997a341a51de447defd59ba1302b` |
| Read-only supplied `chapter_NApotential.tex` | `81dc584fdf60b7907551f6d2b1493fb740594bf94b27b2092ffd8df7f53516d1` |
| Checked lecture PDF | `c816eea5f06822021fa8dd75b70f82724ee47e6dcd6830729f5ecc109296b706` |
| Checked operations-paper v3 PDF | `773eea71af9f1fff112bf5fcab2b9046b81467df2e37165ee1da3949ff74c6d9` |
| Checked accepted trace-paper v2 PDF | `5d6f43d96be101f6aa1a3ddbdd92b5bc49131a0deabbf199e03111d6c0fbaa3c` |

Only Chapters 52 and 54 and current editorial records were changed.
Frozen proof packets, production verifier responses, author-supplied
sources, research classifications and dated release artifacts are
preserved. The PDF is an ignored local build artifact.
These are local mathematical/source/style/build/visual checks, not an
independent-agent or production Rethlas verification. No research atom
was closed or promoted.

The next bounded unit checks Chapter 57's comparison of analytic trace
with divisorial restriction: its nontriviality criterion, approximation
domain, and the exchange of decreasing approximation with the Legendre
supremum. The source scope and existing frozen interfaces must be
checked before editing.
