# Chapter 57: finite-section realization and trace comparison

Audit date: 23 September 2026.

## Mathematical changes

The trace comparison now supplies the missing passage from levelwise
decreasing trace convergence to convergence of the Legendre supremum.
It also proves the cutoff identity at the trivial valuation supported
on a subvariety without simply applying the ambient divisorial formula
at that proper-support point.

### Finite-section construction

The GF realization lemma is written explicitly. For section potentials
a_k and rational weights w_k, take the simplex of convex coefficients
and cut it by the inequality sum p_k w_k >= tau. Maximizing sum p_k a_k
over this polytope produces a decreasing concave curve. Each level is a
finite maximum over the vertices. Its Legendre value is computed by
linear optimization and equals max_k(a_k^An + w_k).

Projection in a class enlarged by a Kähler form has a uniform positive
mass bound, including the initial level. The terminal level uses the
closed endpoint convention. At rational parameters, the rational
vertices give actual analytic singularities after clearing denominators.
At real parameters the construction uses I-goodness under sums, finite
maxima and positive real scaling; it does not label irrational
combinations analytic. The existing two-section P1 example now displays
the raw maximum before projection.

The surjectivity input was checked against the published DXZ statement.
Theorem 3.12(ii) requires a big ambient M and an ample A with M-A big.
For a pseudoeffective L and an ample T, the text now applies it to
M=L+T and A=T/2, using the inclusion PSH(L) in PSH(L+T/2).
This verifies the big-difference hypothesis at the pseudoeffective boundary.

### Domain and cutoffs

For a GF metric the cutoff along Y is the largest weight of a section
not vanishing identically on Y. Equivalently, a zero generic Lelong
number means that the sliced simplex meets the face supported on these
surviving sections. The empty face gives cutoff -infinity.

For a general metric, sequential GF approximation is taken in classes
L+epsilon_j S, with epsilon_j decreasing to zero. All curves are realized
in theta+2 omega; their raw curvature is at least omega after discarding
a finite prefix, so every projected interior level has mass at least
integral omega^n. The common-background model limits are thus legitimate.
Their d_S convergence gives convergence of generic Lelong numbers along
Y, using the exceptional divisorial valuation over its generic smooth
locus when Y has positive codimension.

This proves that the cutoffs c_j decrease to c_Y(Gamma), and identifies
the latter with Gamma^An(v_Y,triv). The argument includes an empty
zero-Lelong interval and the case Y=X. The maximum principle then gives
the nontriviality criterion on all of Y^An. The criterion and cutoff
identity are established before using the trace comparison itself.

### Trace and the Legendre limit

For the finite-section case, restriction is performed only at rational
parameters strictly below the trace cutoff. Those levels are analytic
and nontrivial on the normalization. Monomials containing a section
vanishing on Y disappear; the surviving face of the simplex computes the
divisorial trace value exactly. This avoids applying a trace operator to
individual potentials outside its domain, and avoids assuming analytic
singularities at every real parameter.

For the limit, one fixed sufficiently large target perturbation is used.
Every parameter below the limiting cutoff lies in the analytic trace
domain of every approximant. The checked decreasing trace theorem and
d_S-continuity of the I-envelope and divisorial Lelong numbers give
decreasing finite profiles f_j(tau) -> f(tau) on that interval.

To justify the supremum interchange, f_j <= 0 bounds any parameter
with f_j(tau_j)+tau_j > r from below by r and from above by c_1.
A convergent subsequence has limit tau_* <= c because c_j -> c.
For every sigma < tau_*, decreasing order in the parameter gives
f(sigma) >= r-tau_*. Letting sigma increase to tau_* supplies the
reverse inequality for the suprema. This proves the interchange with
control of the maximizing parameters, without assuming pointwise
convergence at the moving endpoints.

The comparison remains stated on Y^Div, identified with the divisorial
valuations of its normalization. No full singular-space BJ comparison
is inferred. For zero-dimensional Y the divisorial assertion is empty,
while the cutoff formula still computes the value at its trivial point.

The new P2 example is phi=max(log|x_0|+1, log|x_1|). Along the line
x_0=0 its cutoff is 0 although the ambient terminal parameter is 1.
At t ord_p, for p=[0:0:1] on this line, the trace has value -t.
Restriction to the line is nontrivial, whereas restriction to the point
p is identically -infinity and the trace along that point is undefined.

## Primary sources and exact locators

- [Darvas--Xia--Zhang, published article](https://ems.press/journals/cmh/articles/14298510),
  Comment. Math. Helv. 100 (2025), 269--322: Theorem 2.12, page 286,
  is the decreasing sequential GF approximation in shrinking ample
  perturbations. Theorem 3.12, pages 294--296, supplies the realization
  input and its exact big-class hypotheses. The finite-section proof
  starts on page 295; Lemma 3.13 is on page 296.
- [Boucksom--Jonsson, published article](https://numdam.org/articles/10.5802/afst.1705/),
  Ann. Fac. Sci. Toulouse 31 (2022), 647--836: Lemma 1.4(i), page 663,
  is the maximum principle on a subvariety; Corollary 12.18, page 813,
  is the sequential approximation source. Its published PDF has a
  cover page, so these are physical pages 18 and 168.
- [Xia, operations paper, arXiv v3](https://arxiv.org/pdf/2312.17150v3),
  22 October 2024: Lemma 4.19, page 18; Theorem 4.21, pages 19--20;
  Corollary 4.23, page 20. Trace comparison is in Section 4.7, whereas
  Section 4.8 concerns birational functoriality. Numbered operations
  references in this chapter now use the checked version-specific entry;
  the published chapter remains separately identified.
- [Xia, final lecture manuscript](https://mingchenxia.github.io/Lectures/SGPT_final.pdf),
  18 July 2026: Proposition 3.1.12, pages 96--97, and Corollary 6.2.7,
  pages 215--216, for decreasing model convergence; Theorems 6.2.3
  and 6.2.4, pages 227 and 229, for the I-envelope and Lelong numbers;
  Proposition 7.2.1, pages 239--240, for I-good operations; Theorem
  13.4.5 and Lemma 13.4.9, pages 448--450, for trace comparison and
  nontriviality. The supplied chapter_NApotential.tex and chapter_comp.tex
  were read without alteration.

Rendered primary pages inspected: DXZ physical 18 and 27 (printed 286
and 295), BJ physical 168 (printed 813), and operations v3 pages 18--20.
Other listed locators were checked in the source text.

The second mathematical pass checked rational versus real coefficients,
the face of surviving sections, repeated or maximal weights, positive
mass in the common background, cutoff collapse, the signs in the
valuation formulas, the compact interval for maximizing parameters,
normalization and dimension-zero scope, and the half-ample perturbation
in the imported realization theorem.

## Validation and preservation

- Complete final `latexmk` build: 3,941 pages, 18,720,251 bytes.
- Reference and structural audit: 389 TeX inputs, 11,556 unique labels,
  no missing inputs, duplicate labels, dangling references or structural errors.
- The final log has no unresolved citations or references and no horizontal
  or vertical overflow. Existing underfull-box and class-name warnings
  remain outside this revision.
- The strict style audit of the complete edited mathematical blocks and
  shorter changed passages reports zero errors and zero warnings.
- The open-problem inventory passes: 46 active atoms in 14 environments,
  with tiers `(0,5,8,16,17)`; no classifications changed.
- Final rendered physical pages 3279--3280, 3282--3283 and 3285--3289
  were inspected, covering printed pages 3211--3212, 3214--3215 and
  3217--3221. All new displays, the realization hypothesis check, the
  trace proof, the examples and the source note are legible and unclipped.
- `git diff --check` passes; only the intended chapter and progress files
  are included in the commit.

SHA-256 records:

| Checked file | SHA-256 |
| --- | --- |
| Final local `book.pdf` | `b527d429e1404dbff90909c074884bde88be6f1e3536a1c5a1f38fc1c7108146` |
| `ch57_comparison_bj.tex` | `ff9b83be7e33b029118246d029ed120b7ee99adac4a5a9a0b7ea1414b8a6585f` |
| Published DXZ PDF | `467778ff37b893681482e43b4d8f1d717e947a34fe61026b2e6bc418e4a1f70e` |
| Published BJ PDF | `50bd6e6782c29088edc96d013a5d49257b0395d9fb398664f1a9859639992948` |
| Operations-paper v3 PDF | `773eea71af9f1fff112bf5fcab2b9046b81467df2e37165ee1da3949ff74c6d9` |
| Final lecture PDF | `c816eea5f06822021fa8dd75b70f82724ee47e6dcd6830729f5ecc109296b706` |
| Supplied `chapter_NApotential.tex` | `81dc584fdf60b7907551f6d2b1493fb740594bf94b27b2092ffd8df7f53516d1` |

Only Chapter 57 and current editorial records changed. In particular,
Chapters 51--54 and 56 retain their preceding committed bytes, and the
author's chapter_NApotential.tex remains unchanged. Frozen proof packets,
production verifier responses, research classifications and dated release
artifacts are preserved. The generated PDF remains an ignored local
artifact. These checks are local mathematical, source, style, build and
visual checks; no independent-agent or production Rethlas verification
and no research-atom closure are claimed.

The next bounded unit audits Chapter 56's Gauss complexification and
multiplier-ideal GF approximation: the parameter and sign conventions,
uniform generation input, decreasing convergence, and treatment of
semivaluations with proper support. Existing frozen comparison interfaces
must be identified before any dependent changes.
