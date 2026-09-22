# Chapter 61: non-pluripolar points and Dirac energy — 22 September 2026

## Proof reconstruction

The chapter now explicitly assumes connectedness, consistently with
Chapter 60 and the use of one trivial valuation. The zero-dimensional
case is recorded separately.

The finiteness of the non-pluripolar-point metric is proved by finite
convex combinations with coefficients summing to one. An unbounded
evaluation would produce a decreasing psh sequence with value zero at
the trivial valuation and limit minus infinity at the chosen point.
The positive-pair decomposition and separation by PL functions prove
nondegeneracy. This expands MPWN25, Proposition 3.2.2.

The finite-energy tangent inequality is identified before using the
dual-energy formula for a Monge--Ampere measure. Its finite mixed
integrals remain an explicit source input from MPWN25, Proposition
2.3.5 and its proof. Thus the preceding integrability lemma is not
used to assume membership in the very measure class being established.

The point-energy estimate now has its truncation proof. For a
normalized bounded psh potential between -M and zero, the model
energy cocycle has n+1 mixed probability integrals. The zero-model
term is evaluation at the trivial valuation and tends to zero;
each of the other n terms is at least -M. Decreasing continuity
of the extended pairing gives E >= -nM/(n+1), as well as finite
energy of the truncation. Taking max(phi,-M) at a point where
phi < -M gives the lower bound T/(n+1). Monotonicity gives the
upper bound T. No passage to a limit with both an uncontrolled
integrand and a varying measure is used.

The P1 sharpness example formerly replaced the full supremum by
a supremum over one explicit family without proving they agree.
The revised argument first uses MA(phi_1)=delta_ord0 and the
finite-energy tangent identity to calculate the full dual energy.
For every model potential, positivity at the root bounds each
outgoing slope below by -1. Convexity along the ray and decreasing
approximation then bound every normalized psh potential at ord0
below by -1. The explicit potential attains that bound, proving
T(ord0)=1 and dual energy 1/2. The sharpness claim is stated in
dimension one, the dimension actually computed.

## Source scope

The primary sources are
[MPWN25, arXiv v1](https://arxiv.org/html/2509.09442v1)
and the published
[BJ22](https://afst.centre-mersenne.org/item/10.5802/afst.1705.pdf).
The former gives the finite-energy tangent inequality in
Proposition 2.3.5, the point metric in Proposition 3.2.2 and the
point-energy estimate in Proposition 3.2.3.
For BJ22 the precise antecedent used here is the proof of
Proposition 11.1, equation (11.3), printed page 799.
The published proposition goes on to prove a stronger algebraic
upper bound nT/(n+1). That additional conclusion is not silently
transferred to arbitrary compact Kähler classes here.

The argument uses the model mass, testing and energy formulas,
psh decreasing stability and extended pairing already established
or explicitly imported in Chapter 60. This unit does not replace
the general finite-energy pairing theorem, the analytic envelope
theorem or the mixed-energy estimates with a new independent proof.

## Validation

The actual new metric proof, tangent passage, Dirac argument and
P1 calculation each pass the strict writing audit with zero errors
and zero warnings. A second mathematical reading checked the convex
coefficients, the root term, the number of mixed terms, the direction
of the truncation inequality, and the full scope of the P1 extrema.

The production source check has 389 TeX files and 11,494 labels,
with no missing input, duplicate label, dangling reference or
structural defect. The full build has 3,915 pages and 18,583,821
bytes, no unresolved references or citations, and no horizontal
or vertical overflow. Physical pages 3330--3333 and 3337--3338
were rendered and inspected. The source diff is whitespace-clean.

PDF SHA-256: `5113c47049fadcd777e94b123f7aaa93e98d58bf08f0fbb026a76f08429e36cc`

Chapter 61 SHA-256: `72c95c695ee4c7f96c4a1115d3430d3755704238182a6a398fa509b3205a78cc`

The inventory remains 46 active atoms in 14 formal environments,
tiers (0,5,8,16,17). The supplied CURVE_PSH.tex, Chapter 71,
frozen research sources and dated release snapshots are unchanged.
No research-verification gate or new research result is claimed.
