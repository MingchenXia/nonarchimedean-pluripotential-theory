# Chapter 61: strong topology and the variational limit — 22 September 2026

## Changes

The tail-envelope argument now proves weak upper semicontinuity of
energy, including the value minus infinity. Its normalized superlevel
sets are closed in the weakly compact psh space and lie in E1.
This supplies the compactness statement used by the variational proof.

The order of the two arguments in the potential energy gap is now
defined explicitly. The manuscript displays both the gap-control
estimate and the mixed integral estimate, with their exact MPWN25
locators. The latter has potential exponent 2^(-n), measure exponent
1/2 and a common energy bound R. It is used only for positive
dimension; the point case is treated directly.

Existence of the measure quasi-metric and identification of the strong
topologies are retained as imported theorems. The text no longer
describes the whole measure construction merely as a dual version.
Strong continuity of the Monge--Ampere operator is deduced from the
displayed quasi-metric identity.

The fixed-measure integral lemma now has a proof for nets. A fixed
finite-energy Monge--Ampere measure is approximated by model measures.
The mixed estimate controls the error uniformly in the varying
potentials. For each fixed model, divisorial convergence controls
the finite atomic integral. Taking these choices in that order proves
signed integral convergence. Applying it to max(phi_i,phi), whose
energy has the same lower bound, proves L1 convergence. The
identity |a-b|=2(max(a,b)-b)-(a-b) uses the minus sign; possible
infinite potential values are excluded on a measure-null set by
finite-energy integrability.

The Calabi--Yau proof now takes a maximizing sequence directly in E1,
derives its energy bound from the displayed gap estimate, and extracts
a weakly convergent subnet in a compact energy superlevel set.
The measures of the same maximizing sequence converge strongly by
their vanishing gaps before surjectivity is used. The uniform mixed
estimate and the proved fixed-measure lemma give the required integral
limit; upper semicontinuity then gives an actual maximizer. This
avoids both an unstated model-maximizer approximation and an assumption
of weak sequential compactness.

A new P1 model calculation tests the distinction between weak and
strong convergence on both sides. The potential has slope -1/j up to
distance j^2 on one ray and then is constant. It converges at every
fixed divisorial point to zero, but its energy stays -1/2. Its measure
is (1-1/j) times the root mass plus (1/j) times the mass at distance
j^2; the measure converges even in total variation to the root mass,
while its dual energy stays 1/2.

## Sources and scope

[MPWN25, arXiv v1](https://arxiv.org/html/2509.09442v1)
provides Lemma 2.3.6(2), Theorems 5.1.2 and 5.2.2, and the
quantitative estimate in Theorem 5.1.2(2). Its Lemma 5.0.5 and
Propositions 6.0.3--6.0.4 are the arguments reconstructed here.
The imported theorems remain the dependencies of this reconstruction;
the integral lemma is not offered as an independent proof of the
quasi-metric construction.

The published
[BJ22](https://afst.centre-mersenne.org/item/10.5802/afst.1705.pdf)
provides the algebraic antecedents in Lemma 9.15, Proposition 9.19
and Theorem 12.8. Its printed page 787 was inspected as an image:
the maximum identity there has a plus sign where a minus is required.
MPWN25 repeats this elementary sign error at the end of Lemma 5.0.5.
The corrected identity above gives the intended conclusion.
The book does not transfer algebraic conclusions to transcendental
classes without the identified analytic inputs.

## Validation

All five actual new blocks pass the strict writing audit with zero
errors and zero warnings. The second reading checked the order of J,
the uniform bound on its two-potential version, dependence of the
integral error on each index, integrability on null sets, the use of
a subnet, and the exact curve masses and energies. A long proof
heading that caused a small overflow was replaced by the ordinary
proof heading.

The production source check has 389 TeX files and 11,500 labels,
with no missing input, duplicate label, dangling reference or
structural defect. The final full build has 3,919 pages and
18,594,210 bytes, no unresolved references or citations, and no
horizontal or vertical overflow. Physical pages 3330--3331, 3333
and 3335--3339 were rendered and inspected; pages 3337--3339 were
inspected again after the final wording and layout corrections.
The source diff is whitespace-clean.

PDF SHA-256: `0eeea9e076838eaa4c076ca17a10d2ba9ce9194201cac147a336d6622f9d95e7`

Chapter 61 SHA-256: `2e8e4c54f73b9804c0c43670477ad3d7c95ddf8dc1514a75f2ef98f35ce8c66e`

The inventory remains 46 active atoms in 14 formal environments,
tiers (0,5,8,16,17). The checked dual-complex boundary proof later
in Chapter 61 is unchanged. The supplied CURVE_PSH.tex, Chapter 71,
frozen research inputs and dated release snapshots are unchanged.
No new research gate or closure of an open question is claimed.
