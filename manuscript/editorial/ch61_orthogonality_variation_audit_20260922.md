# Chapter 61: orthogonality and envelope variation — 22 September 2026

## Correction and expansion

The text after the restricted-volume formula said that its coefficients
sum to V, although the displayed probability measure already divided
those coefficients by V. The proof now displays the unnormalized
identity separately and states that the normalized masses sum to one.
For example, on the trivial P1 model with a class of degree two,
the raw component mass is two and the probability mass is one.

The contact argument now records its actual approximation inequality.
For each component and epsilon > 0, the imported regularization
provides a model competitor whose value is at least the obstacle
minus (minimal multiplicity + epsilon)/component multiplicity.
Taking the envelope and then epsilon to zero gives the contact gap
bound. A component with positive minimal multiplicity has zero
restricted-volume mass; every nonzero atom is therefore a contact
point. The positive epsilon is the approximation from above to the
minimal multiplicity. The minus-epsilon expression in the source
v1 proof cannot hold at a zero minimal multiplicity.

The extension to continuous obstacles now separates uniform convergence
of the contact gaps from weak convergence of the probability measures.
The integral error is bounded by the uniform gap error plus the
integral of one fixed continuous test against the measure difference.

The envelope first variation is derived by applying the finite-energy
tangent inequality in both orders. Contact with the two obstacles
gives

    t integral(g dmu_t) <= E(u_t)-E(u_0) <= t integral(g dmu_0).

The envelope contraction implies uniform convergence of u_t and hence
weak convergence of mu_t. Division by negative t reverses the bounds.
Both one-sided quotients then have the required derivative.

## Source scope

The exact inputs are
[MPWN25, arXiv v1](https://arxiv.org/html/2509.09442v1),
Propositions 4.2.1--4.2.3 for the mass, measure and contact formulas,
Proposition 2.3.2 for continuity under uniform convergence, and
Proposition 2.3.5 for the finite-energy tangent inequality.
The reconstruction proves the limit passage and the first-variation
deduction from those inputs. It does not claim a new proof of
restricted-volume differentiability or analytic regularization.

## Validation

The new proof and remark pass the strict writing audit with zero errors
and zero warnings. The second reading checked the raw versus probability
mass, the sign and divisor multiplicity in the contact bound, both
contact sets, the negative-parameter quotient, and the fixed-test
justification of the integral limit.

The source check has 389 TeX files and 11,501 labels, with no missing
input, duplicate label, dangling reference or structural defect.
The full build has 3,919 pages and 18,600,422 bytes, no unresolved
references or citations, and no horizontal or vertical overflow.
Physical pages 3334--3336 were rendered and inspected. The source
diff is whitespace-clean.

PDF SHA-256: `16d9f9d8102afa76c672c2ccd80bf24ad97c2037c847b8474c9b86c54638a870`

Chapter 61 SHA-256: `67169ec58ab7ea017284907ea78968ffd1639500eb76bdc6f81378c6ee14ac3e`

The inventory remains 46 active atoms in 14 formal environments,
tiers (0,5,8,16,17). The checked dual-complex boundary proof,
supplied CURVE_PSH.tex, Chapter 71, frozen research inputs and
dated release artifacts are unchanged. No research gate or new
research result is claimed.
