# Chapter 46: curve energies and finite identities — 22 September 2026

## Curve profiles

The energy example formerly called max(h,-j) a PL truncation for an
arbitrary convex h. It also multiplied the possibly infinite endpoint
value by a limiting slope and then canceled boundary terms.

The revised proof first replaces h(t) by h(min(t,R)) for an integer R.
Its convex linear interpolants on nested dyadic subdivisions decrease
uniformly to this bounded profile. They have rational breakpoints and
real coefficients and give real PL psh model potentials. At every finite
stage, model integration by parts gives E = -(1/2) integral_0^R |h'|^2,
including the slope jump at R. Dominated convergence justifies grid
refinement; decreasing energy continuity then permits R to tend to
infinity. For degree d the coefficient is 1/(2d).

The graph measure now uses the distributional measure D^2h, retaining
corner atoms and the atom at the proper-support endpoint. Its agreement
with the finite-energy Monge–Ampère operator is asserted on that domain.
The graph measure for h=-t is explicitly distinguished from that operator.
The logarithmic and linear profiles retain their finite/infinite energy
conclusions. The added profile -2(sqrt(1+t)-1) has no endpoint atom but
infinite squared-slope integral; absence of that atom is insufficient
for finite energy.

The later curve example obtains its mass from weak convergence tested
against 1. It no longer claims that every finite-energy profile is
eventually constant. Reversing the Laplacian sign gives a negative atom
at ord_p; the former claim about negative energy of the trivial metric
was incorrect.

## Finite identities

The cocycle proof factors A^(n+1)-B^(n+1) in the finite pairing.
The concave polynomial segment energy has endpoint derivatives equal
to the tangent integrals. Divisorial determination extends the two
ordered psh inequalities and proves the sup bound almost everywhere.
Integration by parts follows directly from symmetry of the finite
pairing and its duality for integrable tests against signed measures.
Neither proof now infers convergence of varying unbounded tests merely
from weak convergence of measures.

For the Dirichlet inequality, positive model Gram matrices converge
entrywise using finite-pairing continuity after expansion of the psh
constituents. Nef backgrounds are treated by adding epsilon times an
ample class and taking the polynomial limit.

The checked published background is the
[Boucksom–Jonsson paper](https://afst.centre-mersenne.org/item/10.5802/afst.1705.pdf),
Example 4.13, Lemma 7.13, Theorem 7.14, Proposition 7.19 and
Example 7.20. The finite-energy estimates remain source inputs.
No research question is retired.

## Validation

The second reading checked endpoint values, the interpolation direction,
slope bounds, the distributional jump at R, the degree normalization,
both energy limits, the finite-pairing degrees and tangent signs, and
the distinct ample and nef stages of the Dirichlet argument.

The rewritten blocks pass the strict Mingchen writing audit with zero
errors and warnings; this is not a style certification of the legacy
chapter. The current Chapter 46 scoped PDF has 129 pages, no unresolved
reference or citation, and no overfull box. Its auxiliary context now
includes the restored whole-book build and is not compared directly
with the earlier pre-recovery scoped count. Physical pages 89–90 and
95–97 were rendered and read, with no clipping or overlapping formulas.

The full build succeeds with 3,403 pages and 17,984,631 bytes.
PDF SHA-256:
`cdb9a6a7bcc695075b80384caa5c3dce957c5f0596f88858ebccc0e1157f92ca`.
The complete graph has 389 TeX inputs and 11,476 unique labels, with
no missing input, duplicate label, dangling reference or structural
defect. All references and citations resolve in the final log.
The existing 38 horizontal overflows and class-path warning remain;
there is no vertical overflow. The inventory remains 46 active atoms
in 14 formal environments, with tiers (0,5,8,16,17).

Relative to the preceding
[support audit](ch47_49_support_capacity_audit_20260922.md), only Chapter 46
changed among the production inputs. Its SHA-256 is
`fefa911b34f04bcdd3c0b959824293c2f620abd4cfb36b82c1a71019e93f90d0`.
That receipt and the recovery checksum ledger identify the other inputs.

Next: audit Chapter 60's maximal-ray construction, its sequential
regularization input and the identification of the limit's radial energy.
