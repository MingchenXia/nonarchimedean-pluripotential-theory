# Chapter 61: ordered quasi-distances and strong pairings

Date: 24 September 2026.
Baseline: `d9b8f20a53026f73fef85f984a7b79449f375c3a`.
Scope: the opening of the strong-topology section through the material
immediately preceding `lem:mpwn-fixed-measure-integral`. The preceding
weak-compactness, dual-energy, envelope and orthogonality text and the
following integral-convergence, variational and regularity text retain
their baseline bytes. Chapter 60 is unchanged.

This unit supplies exposition and direct consequences of established
inputs. It neither closes a frontier question nor asserts an independent-
agent or production-verifier pass.

## Ordered distances and the Monge--Ampere image

The section now states the precise quasi-metric convention: a continuous
nonnegative function separating points, with a triangle inequality and
symmetry up to fixed factors, and the topology induced by its balls.
The order of each argument is retained throughout.

For the trivial measure mu_0, monotonicity and constant competitors give
E^vee(mu_0)=0. Substitution in the imported measure quasi-metric identity
then gives delta(mu,mu_0)=E^vee(mu), whereas
delta(mu_0,MA(phi))=J(phi). On the Monge--Ampere image the exact identity
is delta(MA(phi),MA(psi))=J(phi,psi). The potential distance adds the
absolute difference of the root values. Hence the normalized map is a
quasi-metric isometry onto its image and a strong topological embedding.
This argument uses arbitrary nets and does not invoke the later
surjectivity theorem. Constant shifts explain the lost root coordinate.
Quasi-symmetry also compares E^vee(MA(phi)) and J(phi) in both directions,
with constants depending only on the dimension.

## Joint pairing estimate and point evaluations

The difference of two pairings is decomposed into the root difference,
the integral of phi-psi against mu-mu_0, and the integral of psi-0 against
mu-nu. All integrals are finite by the earlier integrability lemma.
Apply the imported mixed-gap estimate separately, using one bound R on
the four energies. The second potential gap is J(psi,0), not J(0,psi);
the proof explicitly replaces it using the preceding energy comparison.
This only enlarges the dimension-dependent constant.

For n>=1 the exponent q=2^(-n) satisfies 1/2-q>=0. Thus enlarging the
source's maximum of the energies to any R>=max(1, those energies) is
legitimate, including when all energies vanish. A strongly convergent
pair of nets has a single such R on a tail. The root difference and
the two quasi-distances tend to zero, proving joint strong continuity.
When n=0, connectedness makes the space a point, all potentials are
constants, and the pairing assertion is immediate. The positive-
dimensional estimate is not applied with q=1.

Taking both measures equal to delta_v gives uniform evaluation on
non-pluripolar points with T(v)<=R. The proof uses the inequality
E^vee(delta_v)<=T(v), not an equality between these quantities. It yields
the explicit bound C_n R^(1-q) J(phi,psi)^q for normalized potentials.
For a fixed bounded-T set and a strongly convergent normalized net, one
enlarged R works on a tail. This does not assert uniform convergence on
the entire non-Archimedean space or replace the following weaker
fixed-measure convergence lemma.

## Surface calculation

On the point blowup of P2 times the base, both central multiplicities
are one. For a positive rational a<1 sufficiently small, the existing
relative-Kahler calculation applies to A-aE_1. The central component
degrees are 1-a^2 and a^2, and the model values are 0 and -a. Since the
ambient blowup is a threefold, E_1^3=1, while A restricted to E_1 is
zero and A^3=0. Thus E=-a^3/3 and the measure integral is -a^3.
The two ordered distances are a^3/3 and 2a^3/3. The example is on a
relatively Kahler model; it uses neither a raw big-class formula nor a
regularity conclusion for a general finite-energy measure.

## Exact source and retained boundaries

The [MP--Witt Nystrom v1 PDF](https://arxiv.org/pdf/2509.09442v1)
was checked at printed pp. 20--22; all three pages were rendered and
visually inspected. Definition 5.1.1 supplies the convention, Theorem
5.1.2(1)--(2) supplies the ordered measure identity and quantitative
mixed-gap estimate, Theorem 5.1.3 gives strong continuity of MA, and
Theorem 5.2.2 supplies the potential quasi-metric and topology.
The PDF has 689,695 bytes and SHA-256
`54c7f7e75bc9869f979fff2c2e0e56079660a408cc18d2df95d327dff01b7464`.
The exact v1 HTML was also retrieved from arXiv. The
[author's CV](https://pietropic.github.io/cv/) still identifies this work
as a preprint; no journal version was established in the current search.
The existing version-specific bibliography entry is preserved.

Existence of both quasi-metrics, identification of their strong topologies
and the mixed-gap estimate remain explicitly imported inputs. The new
identities and estimates are proved as consequences, with no novelty
claim. The previously repaired net argument, the signed-to-L1 identity
in the fixed-measure lemma, and the weak-but-not-strong curve example are
unchanged. So are the later exact verifier-backed dual-complex passages.

## Two passes and validation

The first complete statement/proof/source/notation pass produced a full
build of 3,991 pages and 18,997,057 bytes. Physical pages 3395--3399 were
rendered and inspected. The second pass rechecked argument order,
root translations, the common energy bound, finite integrals, arbitrary
nets, zero dimension, bounded-T evaluation, relative positivity and
central multiplicities. It made the energy comparison and constant
dependence explicit and recalled T and the model pullback class locally.

Final full build: **3,991 pages, 18,997,823 bytes**. Physical pages
3396--3400 were rendered and inspected, including the preceding envelope
boundary, all changed text, the preserved fixed-measure lemma and the
transition to the variational theorem. This is a scoped visual audit,
not a new page-by-page review of the whole book.

- Reference/structure check: 390 TeX files, 11,664 unique labels; no
  missing input, duplicate label, dangling reference or structural defect.
- Final build log: no unresolved reference/citation, multiply defined
  label, rerun request or horizontal/vertical overflow. Existing underfull
  and class warnings remain.
- Scoped house audit: zero errors, one reviewed MPWN25 preprint warning.
  Normal audit exits 0; strict audit exits 1 because of that warning.
- Inventory: PASS, 45 active atoms in 14 formal environments, with tiers
  (0,5,8,15,17).
- The builds were performed in a temporary review copy after two local
  write-approval timeouts. All 4,079 other tracked manuscript files in
  that copy were compared byte for byte with the working repository.
  Only the checked chapter, progress records and this audit are intended
  for synchronization; the live PDF remains an ignored build product.
- Chapter bytes outside the stated scope match the baseline exactly.

Final Chapter 61 SHA-256:
`c4e2161151784f0866e88e345d1fd01f87d1f944180e4c98b6244a596e9b0384`.
Final PDF SHA-256:
`44fb6110e93bac8ae14787bf4dd158329d27a52dbb90a46a243a112b77a47fb7`.
Preserved Chapter 60 SHA-256:
`0fdb5f601274ccf7df48afd5112a1bf3e452e3aff9df5a459c5c6a08e611ac93`.

The P12.1 fragment retains SHA-256
`8d9f9bd9edb057b95773479279bbdabb3240319e4cb56f6f15cb2bd923fb4380`.
The supplied normalized-links PDF and its archived copy both retain
`71f5e0d50bdcbf493cb96a869e2db03a78bd591b3eba2f797da5a23f6253daaa`.
The supplied CURVE_PSH.tex retains
`9142aac73c5af7e4e715b3313def5ed56fae4e63e1ac8a53d0419df7d2194be9`.
P12.1 integration/provenance, P12.2--P12.6 residuals, all active atoms,
author originals, bibliography, frozen packets, verifier receipts and
dated releases are preserved.
