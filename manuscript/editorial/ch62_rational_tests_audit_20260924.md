# Chapter 62: rational divisorial tests and the exact stability constant

Date: 24 September 2026.
Baseline: `5583e321461997dc61003c9132f58907b6b897cc`.
Scope: the completion argument, its two source-status passages, and
current progress records. The earlier model normalization, factor-n
verification block, beta criterion, cscK implication and volume formula
retain their previous bytes. Chapters 60 and 61 are unchanged.

These are direct continuity and approximation consequences of the
established chapter inputs. No frontier question is retired. No novelty,
independent-agent review or production-verifier verdict is claimed.

## Finite support and rational weights

For a fixed finite set of divisorial points, let M be the maximum of
their point sizes T. Every normalized finite-energy potential takes
values in [-M,0] at those points. Its energy is at most zero, so every
probability measure on this support has dual energy in [0,M]. The
variational formula, applied in both directions, bounds the difference
of two dual energies by M times the l1 difference of their mass vectors.
This estimate is uniform over the potentials in the variational supremum;
it does not presume that the maximizing potential varies continuously.

Convergent mass vectors give weak convergence and the dual-energy estimate
gives strong convergence. Entropy is the finite linear combination of
the fixed divisorial discrepancies. The normalized Calabi--Yau inverse
therefore converges strongly. Placing the support in one dual complex
and applying the previous chapter's uniform estimate gives uniform
convergence of the solutions as well. Zero weights, repeated support
points and M=0 do not affect the estimates.

Rational probability vectors can approximate any real probability vector,
including on its boundary: round down the first N-1 coordinates to
multiples of 1/j and put the remaining mass in the last coordinate.
The last coordinate remains nonnegative and all coordinates converge.
For N=1 this construction is constant. This rationalization gives
entropy convergence, not exact entropy preservation at each step.
The preceding chapter's barycentric approximation has the stronger
exact-entropy property before rationalization.

## Completion and optimal constant

The theorem is stated for each fixed real delta. It equates testing all
finite-energy potentials, continuous solutions supported on dual complexes,
all real PL envelopes, all normalized solutions with finite divisorial
measure, and the last class with rational masses. Restriction and the
existing divisorial-envelope construction provide the elementary arrows.
The mass-continuity proposition passes rational tests to real masses;
Chapter 61's simultaneous strong/entropy approximation then passes finite
divisorial tests to all finite-energy potentials.

The real-valued strongly continuous twisted energy G has the same source
and hypotheses as before. Its sign is fixed by the trace
n alpha^(n-1).K_X / V = -s. Decreasing model nets extend its energy
identity to all finite-energy potentials by finite mixed pairings.
Adding entropy gives Mabuchi energy. Infinite entropy is handled before
any subtraction or ratio: Mabuchi is +infinity and delta J is finite.
For finite entropy, both sides of the inequality converge, preserving
delta exactly. J is continuous on the normalized strong space.

For positive delta the same constant is preserved in the normalized
model test, using f_D>=1 before applying positive-product identities.
The raw all-big-model condition still only implies the normalized
condition. Neither arbitrary base translations of raw big invariants
nor an unrestricted YTD converse is asserted.

The corollary identifies the exact optimal M/J infimum with the infimum
over normalized rational-mass tests. It uses ratio convergence only
after J has become positive, and then a diagonal choice for the two
approximation stages. It includes an infimum of -infinity and an empty
testing set. Constants have J=M=0 and never enter a ratio.
The later beta/E-dual criterion retains its dimension-dependent comparison
constants; the new result does not identify those two thresholds.

Only masses are rational. Supports range over all divisorial points;
no countable cofinal family is claimed. PL obstacles may have real
coefficients and their envelopes are not asserted to be model psh.
The existing P1 family supplies a boundary check: rational 0<a<1 gives
positive ratios 2(1-a)/a tending to zero, and a=1 has positive J and
zero Mabuchi energy. Pointwise positivity is not a uniform lower bound.

## Sources and proof dependencies

The [published Boucksom--Jonsson author offprint](http://sebastien.boucksom.perso.math.cnrs.fr/publis/BJ_synthetic.pdf)
was downloaded again and checked at printed pp. 191--193, equation (4.2)
and Proposition 4.5. All three pages were rendered and inspected.
The orthogonality and submean hypotheses, normalized trace and
strong continuity for a general signed twisting class agree with the
application. This input remains imported. The file has 633,567 bytes
and SHA-256
`4ecf20801f0871223ddfc1ea3e09927904affaab75bb5e195bfe55a2b0f09498`.

The [MP--Witt Nystrom version 1 PDF](https://arxiv.org/pdf/2509.09442v1)
was checked at printed pp. 34--35, including Theorem 9.2.1 and Corollary
9.2.2; both pages were rendered and inspected. Its 689,695 bytes have
SHA-256
`54c7f7e75bc9869f979fff2c2e0e56079660a408cc18d2df95d327dff01b7464`.
The chapter records that theorem as the source antecedent. The revised
completion proof uses the newly established entropy density directly,
so the former extra toroidal subdivision argument is no longer needed
there. Its historical audit and its committed source remain available;
no old receipt has been rewritten. Chapter 61 retains the multiplicities
and full-vertex constraints in the PL-envelope construction.

The source-status table and final source note now distinguish the
reconstructed completion proof from the imported continuous-energy and
cscK theorems. The finite-mass estimate and rational threshold are
proved explicitly rather than attributed as verbatim source statements.
Bibliography databases and exact-version citation keys are unchanged.
The [author's publication page](https://pietropic.github.io/publications/)
still lists MPWN25 as a preprint; the current primary-source search did
not establish a published replacement for the checked version.

## Two passes and validation

The first complete statement/proof/source/notation pass produced a full
build of 3,995 pages and 19,013,880 bytes. Physical pages 3418--3421
and 3429--3430 were rendered and inspected. The second pass checked
finite energy before inversion, the uniform supremum bound, zero masses,
the probability-simplex boundary, every implication with one real delta,
infinite entropy, the positive-denominator tail and the two successive
ratio limits. It supplied the explicit rational vectors, retained
positive denominators, removed an unsourced result title, and ordered
the equation tags chronologically while preserving their reference labels.

Final full build: **3,995 pages, 19,014,663 bytes**. Physical pages
3418--3421 and 3429--3430 were rendered and inspected, covering the entire revised
argument, its adjacent model/cscK passages, and both source-status
passages. This is a scoped visual review, not a new whole-book audit.
The second build was made in a temporary export of the baseline with
the final Chapter 62 overlaid, after two automatic permission-review
timeouts. All its TeX inputs match the delivered project sources; the
current PDF is that checked output.

- Reference/structure check: 390 TeX inputs and 11,677 unique labels;
  no missing input, duplicate label, dangling reference or structural defect.
- Final log: no unresolved reference/citation, multiply defined label,
  rerun request, horizontal overflow or vertical overflow. Existing
  underfull and class warnings remain.
- Scoped house audit: zero errors and one reviewed MPWN25 preprint
  warning; normal audit exits 0 and strict audit exits 1 for that warning.
- Open-problem inventory: PASS, 45 active atoms in 14 environments,
  tiers (0,5,8,15,17).
- Outside the completion block and the two source-status replacements,
  Chapter 62 is byte-identical to the baseline, including the exact
  factor-n verifier block. All other chapter sources are unchanged.
- `git diff --check`: PASS. The live PDF remains an ignored build product.

Final Chapter 62 SHA-256:
`9e1e25065c5a19256b0abffd14e1a065c92fe13c01e6caa0b6f61311a3445dcd`.
Final PDF SHA-256:
`629276fd17483f48e0790b9e3eaf8a45ebb409003b81adfca0ecdd46b7228a6e`.
Preserved Chapter 61 SHA-256:
`1bc2e7024230c6c32c22a855af30a152e4f4c1567ab0984eb4c8b05c2c3264fd`.
Preserved Chapter 60 SHA-256:
`0fdb5f601274ccf7df48afd5112a1bf3e452e3aff9df5a459c5c6a08e611ac93`.
Preserved P12.1 fragment SHA-256:
`8d9f9bd9edb057b95773479279bbdabb3240319e4cb56f6f15cb2bd923fb4380`.
The author's supplied normalized-links PDF and its archived copy retain
`71f5e0d50bdcbf493cb96a869e2db03a78bd591b3eba2f797da5a23f6253daaa`;
the supplied CURVE_PSH.tex retains
`9142aac73c5af7e4e715b3313def5ed56fae4e63e1ac8a53d0419df7d2194be9`.
P12.1 integration/provenance, P12.2--P12.6 residuals, all active research
atoms, author originals, frozen packets, verifier receipts and dated
releases retain their previous scope and bytes.
