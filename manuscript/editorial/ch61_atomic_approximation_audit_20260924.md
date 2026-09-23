# Chapter 61: finite divisorial approximation on a fixed dual complex

Date: 24 September 2026.
Baseline: `e6ff6f0039bb3a0e2280c3454ac2f5a35569f90e`.
Scope: two additions, after the existing measure-approximation theorem
and after the divisorial-envelope corollary, plus the introductory
sentence before the domination principle. All other baseline Chapter 61
bytes, including its exact verifier-backed boundary-continuity passage,
are preserved. Chapters 59, 60 and 62 are unchanged.

These are elementary interpolation and stability consequences of the
chapter's established inputs. No frontier question is retired and no
novelty, independent-agent audit or production-verifier verdict is claimed.

## Fixed-model entropy and the atomic construction

For any weakly convergent net of Radon probability measures, entropy
after retraction to one fixed model converges. It is the integral of the
fixed continuous bounded model discrepancy. The pushforward notation is
explicitly extended to arbitrary probability measures for this argument;
finite energy before retraction is not needed. This statement alone is
not used to deduce strong convergence or continuity of unretracted entropy.

The existing uniform bound for normalized psh functions on a fixed dual
complex Delta gives 0<=T(v)<=M_Delta there. Every probability measure on
Delta consequently has dual energy between zero and M_Delta: normalized
energy is at most zero and the potential is at least -M_Delta. The
reduced discrepancy is continuous and affine on each original face,
so every such measure also has finite entropy.

Choose nested compatible rational triangulations subordinate to the
original faces, with vanishing mesh. Their nodal functions are
nonnegative and sum to one. Integrating those functions against the
given measure gives nonnegative real masses of sum one on finitely
many rational, hence divisorial, vertices. The coefficients need not
be rational; zero masses may be omitted. The triangulations are used
as finite-complex interpolation data. The proof does not assert that
each triangulation itself is the dual complex of an snc model.

For every continuous function g on Delta, the integral against the
atomic measure equals the integral of its affine interpolant against
the original measure. The interpolants converge uniformly by uniform
continuity and vanishing mesh, which proves weak convergence. For each
finite-energy psh u, facewise convexity makes its interpolants decrease
to u. Thus E(u)-int u dnu_m increases to E(u)-int u dnu. Taking the two
suprema in either order proves monotone dual-energy convergence. No
uniform convergence over the whole family of potentials is assumed.
Weak convergence together with this energy limit proves strong convergence.

Affine interpolation reproduces the reduced discrepancy exactly on
every simplex. Entropy is therefore identical at every approximation
step, not merely convergent. Isolated zero-dimensional faces, measures
with atoms on common faces, and zero nodal masses cause no change to
the construction; compatible nodal functions agree on shared faces.

## Curve example and continuity of solutions

On the point-blowup interval of P1, identify the monomial points with
t ord_p for 0<=t<=1. The reduced discrepancy has values zero at the root
and one at the exceptional vertex: its multiplicity and relative
canonical coefficient are both one. Affinity gives A(t ord_p)=t.
For Lebesgue probability measure, the dyadic-grid nodal weights are h/2
at both endpoints and h at every interior grid point. Their sum is one,
and their discrepancy moment is exactly 1/2 at every stage, including
the coarsest two-endpoint grid.

For two measures supported on the same Delta, the existing Calabi--Yau
theorem supplies normalized solutions and the regularity theorem makes
them continuous. The root-distance comparison bounds both J energies
by D_n M_Delta. With R=max(1,D_n M_Delta), the bounded-T evaluation
estimate bounds their difference on Delta by
C_n R^(1-2^(-n)) delta(mu,nu)^(2^(-n)). Applying support domination in
both directions extends this same bound to the whole space. Its
constant depends on the fixed complex and class, not on the measures.
The estimate is stated for n>=1; in dimension zero every normalized
solution is zero and approximation is constant.

The barycentric measures therefore give uniform and strong
approximation of the fixed-complex solution by normalized envelopes
of real PL obstacles, preserving entropy exactly. The existing finite-
constraint construction retains all central multiplicity factors.
Neither the interpolants of arbitrary continuous functions nor the
resulting psh envelopes are asserted to be model psh functions.

For a general finite-energy measure, first use the previously proved
retracted sequence with strong and entropy convergence. Then on each
of its fixed complexes choose one finite atomic approximation at
quasi-distance less than 1/j. Its entropy equals that of the retracted
measure. The quasi-triangle inequality gives strong convergence to the
original measure, and the Calabi--Yau homeomorphism gives strong
convergence of normalized potentials. This handles infinite limiting
entropy, although every approximant has finite entropy. The argument
does not claim a uniform potential limit when the complexes vary, nor
does it require a countable cofinal family of all models.

## Primary sources and retained inputs

The exact [MP--Witt Nystrom v1 PDF](https://arxiv.org/pdf/2509.09442v1)
was checked at printed pp. 27, 28 and 30, all rendered and inspected.
Lemmas 7.2.1--7.2.2 and Corollary 7.2.3 are the sources of the already
reconstructed retracted-measure approximation. Lemma 7.2.4, p. 28,
is precisely the fixed-model entropy-continuity argument. Theorem
8.2.1 and Proposition 8.3.2, p. 30, supply the existing continuous-
solution and PL-obstacle results used by the new consequences; Lemma
7.1.5, p. 27, is their finite-constraint input. The new barycentric
construction is proved explicitly, not attributed verbatim to those
source statements.

The source PDF has 689,695 bytes and SHA-256
`54c7f7e75bc9869f979fff2c2e0e56079660a408cc18d2df95d327dff01b7464`.
The [author's publication page](https://pietropic.github.io/publications/)
still lists the work as a preprint; no journal version was established
in the current primary-source search. The version-specific MPWN25 entry
and all bibliography files are unchanged.

The analytic envelope, locality, Calabi--Yau and quasi-metric inputs keep
their existing status. The exact boundary-continuity repair and its
dated verifier receipt are untouched. The only alteration to an older
paragraph removes an obsolete count of the uses of support domination.

## Two passes and validation

The first complete statement/proof/source/notation pass produced a full
build of 3,995 pages and 19,011,421 bytes. Physical pages 3406--3408 and
3410--3411 were rendered and inspected. The second pass checked the
pushforward domain, normalized energy bound, nested-mesh order,
supremum interchange, affine entropy identity, endpoint coefficients,
the uniform constant, both directions of domination, zero dimension,
and the diagonal sequence. It made the energy supremum and the curve
discrepancy calculation explicit.

Final full build: **3,995 pages, 19,012,697 bytes**. Physical pages
3406--3411 were rendered and visually inspected in full, covering every
changed passage and the adjacent approximation, locality, regularity,
envelope and source-note text. This is a scoped visual review.

- Reference/structure check: 390 TeX files, 11,673 unique labels; no
  missing input, duplicate label, dangling reference or structural defect.
- Final build log: no unresolved reference/citation, multiply defined
  label, rerun request or horizontal/vertical overflow. Existing underfull
  and class warnings remain.
- Scoped house audit: zero errors and one reviewed MPWN25 preprint
  warning. Normal audit exits 0; strict audit exits 1 for that warning.
- Inventory: PASS, 45 active atoms in 14 environments, tiers (0,5,8,15,17).
- Removing the two additions and restoring the one introductory sentence
  reproduces the baseline Chapter 61 byte for byte.
- `git diff --check`: PASS. The live PDF remains an ignored build product.

Final Chapter 61 SHA-256:
`1bc2e7024230c6c32c22a855af30a152e4f4c1567ab0984eb4c8b05c2c3264fd`.
Final PDF SHA-256:
`3eb84688dbbc1b7d01166b110e1f6d52ccb4850a82f796f9aa64bcc27a51fd7e`.
Preserved Chapter 60 SHA-256:
`0fdb5f601274ccf7df48afd5112a1bf3e452e3aff9df5a459c5c6a08e611ac93`.
Preserved P12.1 fragment SHA-256:
`8d9f9bd9edb057b95773479279bbdabb3240319e4cb56f6f15cb2bd923fb4380`.
The supplied normalized-links PDF and its archived copy retain
`71f5e0d50bdcbf493cb96a869e2db03a78bd591b3eba2f797da5a23f6253daaa`;
the supplied CURVE_PSH.tex retains
`9142aac73c5af7e4e715b3313def5ed56fae4e63e1ac8a53d0419df7d2194be9`.
P12.1 integration/provenance, P12.2--P12.6 residuals, all active research
atoms, author originals, frozen packets, verifier receipts and dated
releases retain their previous scope and bytes.
