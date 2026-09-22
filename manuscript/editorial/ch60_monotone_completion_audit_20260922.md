# Chapter 60: model approximation and monotone completion — 22 September 2026

## Fixed-model approximation

The real model class had been introduced before real-parameter energy
variation, while the general psh class was defined using rational model
functions. `prop:mp-real-model-approximation` now supplies the missing
connection. On one smooth snc domination, a vertical relatively ample
divisor for the morphism to the product gives a rational relatively Kähler
perturbation of the pulled-back background. Convex interpolation into this
positive locus and rational approximation of the finitely many vertical
coefficients give strictly positive rational model functions converging
uniformly to the original real nef model function.

The model constructions are those of
[MP24, arXiv version 2, Remark 2.5.2 and the proof of Theorem 2.6.4](https://arxiv.org/html/2409.06221v2).
The proof spells out the negative exceptional-divisor combination, the
curvature form positive on the relative tangent kernel, and the compactness
argument for a small positive multiple. Positivity on the union of central
components uses
[Demailly–Păun Proposition 3.3(ii)](https://annals.math.princeton.edu/wp-content/uploads/annals-v159-n3-p05.pdf).
The smooth model and its finite divisor space remain fixed throughout the
approximation. No projectivity of X, integral background class, or uniform
positive margin as the interpolation parameter tends to zero is required.

For uniform errors epsilon_j = 4^(-j), translation by 2 epsilon_j places
the j-th approximant strictly between phi + epsilon_j and phi + 3 epsilon_j.
Since 3 epsilon_(j+1) < epsilon_j, these rational translations make the
sequence decreasing. This proves membership of each real nef model
function in the rationally defined psh completion. It does not assert a
countable cofinal family of all analytic models.

## Arbitrary decreasing nets and divisorial comparison

`prop:mp-psh-decreasing-stability` now states the full directed-net result
already supported by its compactness proof. The upper index is chosen to
dominate the two input indices in the original directed set. The minimum
of two model majorants is only a continuous comparison function; its
positivity is never assumed. The same argument, using the new fixed-model
approximations, supplies decreasing H(alpha) majorants for every psh
function. The auxiliary rational nef family is denoted P, distinct from
the strictly positive family H(alpha).

The chapter now assumes connected X, matching Chapter 59. This hypothesis
is needed by the imported divisorial finiteness estimate. Without it,
potentials equal to zero on one component and -j on another decrease to a
function that is not identically -infinity but is -infinity on every
divisorial point of the second component. Dimension zero is treated
separately before using intersections with gamma^(n-1).

The continuous-obstacle step in divisorial comparison now chooses a
rational upper bound q_j for each uniform approximation error. This keeps
h_j + q_j in rational PL; the norm itself need not be rational. The source
locators checked here are MP24 arXiv version 2, Theorem 4.3.3, Proposition
4.3.6 and Theorem 4.3.8. The finite-dimensional bound remains an explicit
import. No new independent verification of its analytic-cycle inputs or
of the frozen Chapter 71 comparison is claimed.

## Extended energy

The introductory energy sentence no longer says that the earlier
polynomial definition was restricted to rational psh model functions.
Agreement of the extended pairing with the real nef model pairing is now
proved by two inequalities: mixed nef positivity bounds every tuple of
majorants from below, and the fixed-model coefficient approximation gives
the reverse inequality by convergence of intersection polynomials. This
avoids assuming the very model compatibility that is being proved.

The first term in J is explicitly phi(v_triv), since the zero model
measure is the Dirac measure there. Divisorial finiteness makes this a
finite real number. Thus J remains well defined with value +infinity when
E is -infinity. The general upper semicontinuity and decreasing-net
continuity of the extended pairing remain the import from MP24 arXiv
version 2, Lemma 4.4.1 and its following discussion.

## Validation

The second reading checked exceptional-divisor signs, relative tangent
kernels, the fixed-model requirement, coefficient rationality, monotone
error bands, arbitrary directed indices, the possible value -infinity,
connectedness and dimension zero, and both inequalities in model-energy
compatibility. The new proof and replacement paragraphs pass the strict
Mingchen writing audit with zero errors or warnings. A wider audit of the
whole legacy section still flags its existing inline-math delimiters and
three existing definition titles; that section is not reported as passing
the strict house-style audit.

The final scoped Chapter 60 build has 88 pages, no overfull box or
unresolved citation, and the same three occurrences of the external
Chapter 71 reference. Physical pages 66–70 were rendered and inspected,
including both new propositions, divisorial comparison, the energy
definition and its agreement proof. No clipping or overlapping formula
was found. The available source closure has 388 files and 11,430 labels,
with no duplicate labels or structural defects. The missing Chapter 70
input and its thirteen unresolved file/label pairs remain unchanged.
The exact open-problem inventory and whitespace checks pass. This is
expository completion of model approximation, not a research retirement
or a successful full-book build.

Next: audit the finite-energy measure construction and the precise joint
psh hypothesis in the radial correspondence.
