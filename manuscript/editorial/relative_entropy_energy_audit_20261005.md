# Relative entropy and normalized power energies

This checkpoint follows `4851791` on the cloud-only `work` branch.
Chapter 65 adds a section connecting model singularity types to density
entropy and relative energy. Appendix L.39 pins the published source and
the selected arXiv dependencies. All previous releases, native catalogue
bytes and complete problem statuses remain historical records.

## Primary sources and reading scope

The controlling source is Di Nezza–Trapani–Trusiani, *Entropy for
Monge–Ampère Measures in the Prescribed Singularities Setting*,
[SIGMA 20 (2024), 039](https://sigma-journal.com/2024/039/),
DOI 10.3842/SIGMA.2024.039, published online 8 May 2024.
The acquired publisher PDF has 19 pages, 472,323 bytes and SHA-256
`cabd23b228351a164d8f6e704bc43d02ffe19323e3b90b6726b533bae7c63551`.
Its complete 1,217-line extraction and all actual PDF pages were read and
inspected in the preceding research phase, recorded before `4851791`.
This import reuses that complete reading and the inspected contact sheets;
it does not claim a new acquisition or second full reading. All source
locators refer to this publisher file, not its separate arXiv versions.

The admitted known inputs are the Section 3 entropy definition, Lemma 2.5,
the power case of Theorem 3.5, Theorem 3.7, Lemmas 3.8–3.9, and
Propositions 3.10 and 3.12. The power estimate occupies actual pages 10–13,
the entropy-energy argument 14–16 and the stability arguments 17–18.
The audit does not import every example or claim from the paper.

Six selected dependency pages of Darvas–Di Nezza–Lu arXiv:2303.11584v2,
revised 3 October 2023, were freshly inspected. Theorem 1.4 is on actual
page 7, printed page 5; Lemma 3.5 on actual 23, printed 21;
Lemma 5.19 and its proof on actual 53–55, printed 51–53;
Theorem 6.15 on actual 70, printed 68. The 73-page PDF SHA-256 is
`e72213a3154bff5cab1a41f9651568201f8ead79beb662925884e58994c19fd0`.
The statements, normalization proof and concave-composition approximation
were checked selectively. This is not a complete survey rereading, and its
arXiv locators are not replaced by the published survey's pagination.
A preliminary page-selection sheet exposed the two-page printed/actual
offset; the final dependency selection uses the corrected actual positions.

## Mass and differential conventions

The ambient category is a connected smooth compact Kähler manifold of
complex dimension n>=1 with fixed smooth big form theta and smooth
Kähler reference omega. A model phi=P_theta[phi] has positive raw
non-pluripolar mass M. Relative full-mass u has the same raw mass.
Normalize the measure as mu_u=MA(u)/M, not MA(u)/Vol(theta).
For MA(u)=f nu the probability density is g=f/M and
H=integral g log g=integral f log f/M-log M.
Zero model mass is excluded; no division by zero or pole-mass restoration
is implicit. Extended-real differences are evaluated off polar sets.

The source uses ddc_s=2 ddc_b. Set theta_s=2 theta_b and keep both
potentials. Source currents scale by two, raw masses and raw energies by
2^n. Probability measures, normalized energies and entropy agree.
This compact class conversion is distinct from the local fixed-current
potential conversion in the preceding checkpoint.

## Power estimate and truncation

For sup u=-1, the model normalization identity gives phi-u>=1.
For r>0, e_r=integral (phi-u)^r dmu_u and E_r=M e_r.
The published Theorem 3.5 with chi_1(t)=t^r has
chi_2(t)=t^(1+r/n)/(1+r/n). Its actual page 13 coefficient is
c_0 M^(1/n)/2. Multiplication by E_r^(-1/n) cancels M exactly.
Hence the normalized power estimate has fixed-geometry constants
independent of the positive model type. It is not a uniform estimate
for an arbitrary family of ambient forms or degenerating geometry.

The proof first works with bounded relative difference. The obstacle
then has a genuine psh minorant and its envelope has the same model
type. The inverse derivative contradiction uses the full relative mass
before Skoda integrability. A variable scalar multiple of a positive
current need not be closed; the measure comparison relies on the local
regularization and plurifine localization in DDL Lemma 5.19. It is not
obtained by simply taking a top wedge of that scalar-weight current.

For u_j=max(u,phi-j), locality and equal total masses identify the raw
energy exactly with integral min(phi-u,j)^r MA(u). It increases to E_r.
Fatou passes the exponential inequality to general finite-energy u.
No assumption of a smooth-volume density is made in this power estimate.
The general-weight theorem is not restated beyond the power case here.

## Finite entropy and the critical energy

For n>1 let p=n/(n-1), so 1+p/n=p. Use the probability density g and
Psi(g)=(g+1)log(g+1)-g. The pointwise estimate Psi(g)<=g log g+1
and Young's inequality give integral h dmu<=B+1+integral(e^h-h-1)dnu.
First apply this to h=a(phi-v)^p for every relative E^p test v,
with its own positive a from the power estimate. The known DDL
measure characterization with weight t^p and raw measure M mu then
establishes u in E^p. Its mass and noncharging-of-model-poles premises
are explicit. Normalizing an arbitrary test by an additive constant
preserves the required L^p integrability.

Only after this finiteness step take h=c e_p^(-1/n)(phi-u)^p.
The left side is c e_p^(1-1/n); the exponential term is uniformly
bounded. This proves a bound depending on geometry and B, and a
uniform positive exponential coefficient follows. The calculation is
a probability-normalized reformulation of the source's known proof,
not a new theorem or an improvement of the critical exponent.

For n=1 the source's qualitative conclusion is bounded difference
u-phi. The import does not copy the literal globalized circle-measure
formula in Lemma 3.8 or the unchecked local gluing wording of Example
3.4. No higher-dimensional bounded-difference, Hessian or regularity
claim is inferred from the critical energy statement.

## Reference changes and perturbations

Smooth positive reference volumes differ by a bounded logarithmic
density, so their entropies differ by a finite integral. The one-way
bounded-density inequality also applies to a semipositive pullback
volume on a smooth bimeromorphic Kähler modification: no positive lower
Jacobian bound is assumed. Non-pluripolar measure identities hold off
analytic exceptional sets and the measures give those sets no mass.
This is a known complex statement, not a non-Archimedean functoriality
claim.

Proposition 3.12 assumes finite entropy at a positive perturbation
in addition to the original class. Positivity of the binomial mixed
measures gives their densities; S_t<=max(1,(t/epsilon)^n)S_epsilon
then preserves L log L integrability. Each positive perturbed mass
normalizes its own probability measure. In dimension one the only
additional measure is smooth t omega, so the positive answer follows
by the explicitly identified direct binomial calculation. The general
higher-dimensional premise is retained. No answer to the published
Questions 1.1/3.11, and no current open-problem retirement, is claimed.
The targeted current literature search did not identify a checked
resolution; this is not an exhaustive absence claim.

## Research-only follow-up and unchanged boundaries

The fully read and inspected Guedj–Lu arXiv:2502.02313v2 source remains
research-only. Its asymptotic condition (K), Luxembourg normalization,
radial examples and nonlinear-equation constants need their own import
scope. The August big-class uniform-estimate source remains unimported.
The preceding logarithmic modulus keeps its explicit minimal-singularity
bound. Berman–Berndtsson is still only a selected text reading.

This checkpoint contains identified known results and direct formal
consequences under the repository protocol, with no original-result
claim, independent model calls or extension of earlier receipts.
All canonical problem statuses, general Siu/closure boundaries,
non-Archimedean entropy comparisons, spectral laws and A2–A4 convergence
retain their previous scope.

## Final build and scoped release review

The final v1 build has 4,319 pages, 20,085,883 bytes and SHA-256
`6c70265df5498505214313ae55fe38a01f499e9256d40658d67309a025c10715`.
It reports no TeX errors, package/pdfTeX warnings, unresolved references,
missing characters, rerun requests or overfull boxes. The 954 underfull
boxes are recorded. All 328 cited bibliography entries and the 743
accepted index entries pass their own checks; index rejection and warning
counts are zero. The 742 numeric index-page groups resolve to 404 valid
distinct destinations. The PDF has 21,670 named destinations, 46,618
internal links, 163 URL links, 2,502 contents entries and six parts;
all internal and contents targets pass the destination check.

The 425-input active source closure is byte checked. Its 423 inputs outside
Chapter 65 and Appendix L are unchanged, as are all 108 protected inputs,
49 pre-existing formal blocks including their proofs and 37 preceding
frozen manifests. Six new equation tags, 65.66–65.71, and eleven labels
raise the unique-label count to 12,691. The new published bibliography
entry raises available/cited keys to 623/328. The inventory checker passes
42 complete atoms, twelve families and unchanged tiers 0/3/7/15/17.
The catalogue remains the same 86-page source/PDF pair in its existing
native editor; no catalogue compilation or fresh catalogue review is
claimed.

Twenty matching final-book pages were freshly displayed: actual pages
1, 59, 60, 67, 3473–3478, 4084–4087, 4295, 4303, 4309, 4310, 4318 and
4319. They cover the new section in full, its transitions, provenance
L.39 in full, contents entries, selected index endpoints and bibliography.
The 20-page review has 328,841 bytes and SHA-256
`7a935829f944595eb482c95aa6d3f93a076baa70684a819ac61c6fa57380ef0e`.
This is a scoped release review, not a new whole-book reading.
The manifest and source archive record the final bytes separately from
the unchanged earlier exports.
