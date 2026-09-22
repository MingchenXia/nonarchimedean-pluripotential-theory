# Curve lengths, weights and compatible norms — 22 September 2026

## Issue and correction

Chapter 5 distinguished the values 1/(b_i b_j) and
1/lcm(b_i,b_j), but called the former the analytic length
inherited from the Berkovich space and claimed the model mass
forced it uniquely. Chapter 22 then identified that first length
with a norm compatible with the integral affine lattice. The
latter assertion contradicts its definition of compatible norm.

The revised explanation separates the intersection metric from the
lattice (stable) metric. If g=gcd(b_i,b_j), lattice distances are g
times intersection distances. Node residue weight m for the
intersection convention becomes gm for the lattice convention.
The weighted slope, and hence the model measure, is unchanged.
This arithmetic identity is now displayed in Chapter 5 and used
in Chapters 20 and 22 and Appendix J.

The model with adjacent multiplicities (2,2) checks both
normalizations: endpoint difference -1/2, intersection length 1/4
and weight 1 give mass -2; lattice length 1/2 and weight 2 give
the same mass. The example explicitly assumes algebraically closed
residue field, so its blowup point and node are rational.
The Eisenstein function T^2-c pi supplies the independent degree-two
check. It no longer purports to determine a length without a weight.
Node blowup preserves the gcd and the sum of the edge lengths
in both conventions.

A primitive affine coordinate defines the one-dimensional compatible
norm, hence lattice length. Its Lipschitz constant in intersection
length is g times its lattice Lipschitz constant. On a fixed finite
complex these are bounded comparison factors. The new (2,2) example
checks this factor and its persistence after inserting multiplicity
four. The old claim that a changed subdivision norm made any uniform
estimate impossible is replaced by the precise failure to restrict
the original norm.

Chapter 20 also now keeps residue degrees in the reduced
strictly semistable proof: the intersection number of components
is a sum of node degrees, not necessarily a number of edges.
The nonreduced graph formula uses an snc model and states its
length-weight convention. Appendix J records both conventions,
and the Chapter 19 computational checklist now asks for matching
edge weights as well as length normalization.

## Primary literature

The new bibliography entry BN16Weight identifies the published
[Baker--Nicaise paper](https://msp.org/ant/2016/10-10/ant-v10-n10-p01-p.pdf),
Algebra & Number Theory 10 (2016), 2053--2079.
Equation (2.1.3), Theorem 2.3.3 and Remark 2.3.4 give the
intersection metric and distinguish the other convention.
Appendix A.1.2--A.1.4 gives the stable lattice metric.
Proposition A.2.3 compares it with the geometric skeletal metric.
The book retains that proposition's algebraically closed residue
field and residue-characteristic-zero scope, and the exclusion
of principal vertices. It identifies the comparison as a source
input; the source itself omits its proof. This is not used to
assert an unrestricted comparison in wild characteristic.

The published pages 2057 and 2076--2077 were inspected as images.
The arXiv v2 counterpart numbers the appendix as Section 4;
the book uses the published Appendix A locators.

## Validation and limits

The two complete rewritten remarks, the Chapter 20 graph proof,
and the Chapter 22 norm explanation and example pass the strict
writing audit with zero errors and zero warnings.
The second reading checked primitive slope, gcd preservation,
both slope normalizations, rational residue degrees, the
Eisenstein point and the direction of the Lipschitz rescaling.
The complete production closure was searched for consumers.
The unit-multiplicity examples and the Farey refinements in
Chapters 5, 8, 22 and 34 remain consistent: adjacent gcds are one.

The final source check has 389 TeX files and 11,493 labels,
with no missing input, duplicate label, dangling reference or
structural defect. The full build has 3,915 pages and 18,577,703
bytes, no unresolved references or citations, and no horizontal
or vertical overflow. The source diff is whitespace-clean.
Physical pages 191--193, 1532--1533, 1619--1620 and 3822 were
rendered and inspected. The final Chapter 22 wording and
Appendix J formula layout were rendered again after their
follow-up.

PDF SHA-256: `c54b31452fe2133fd7e0bab0f9d67f11a8c4d891e32ba881eb147a6760e48def`

Production-file SHA-256 values:

- parts/part1/ch05_skeleta.tex: `a0f92be9fd9754fa81a6be703c234637202137d86d54ddd0df7620224f9a1dcc`
- parts/part3/ch20_model_forms.tex: `1d30ed45f5717d53cea695f0370c99313bf8b35837aad019553e43f3a754afc2`
- parts/part3/ch22_compactness.tex: `f05517a0c158dcecc13f16d0dfcc1e5953d46dfdba635e865233bd5c232a420b`
- appendices/appJ_normalizations.tex: `03776be9bb0ec9dc694ec09ab37fff1d9e0255c3a57fe4b5d23c042bbc83490d`

The inventory remains 46 active atoms in 14 formal environments,
tiers (0,5,8,16,17). Frozen research inputs, CURVE_PSH.tex,
Chapter 71 and dated release snapshots are unchanged.
This corrects definitions, elementary calculations and source
attribution; no new research-verification gate is claimed.
