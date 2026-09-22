# Chapter 60: model measures and energy — 22 September 2026

## Model Monge--Ampère measures

The model construction was checked against
[MP24, arXiv version 2, Section 4.2.1](https://arxiv.org/html/2409.06221v2).
The book now spells out its independence under snc domination: strict
transforms retain their multiplicities, valuations and top intersections;
exceptional components mapping to lower-dimensional sets contribute zero
by projection formula.

`prop:mp-model-ma-mass` now states both facts supplied by the intersection
calculation. For any background with positive top self-intersection, the
signed model measure has mass one. For a Kähler background and a relatively
nef model class it is nonnegative, hence a probability measure. The latter
assertion is no longer restricted to the relatively Kähler locus. The proof
uses nonnegative top self-intersections of nef classes on the smooth
central components; it does not assume that strict positivity survives a
resolution. The dimension-zero case is explicit. The normalization is
written as `V_beta^{-1} V_beta = 1` at the level of the displayed formula.

## Deformation-to-the-normal-cone example

The two-component, interval-skeleton example now assumes that X is
connected of positive dimension and that its center is nonempty, connected,
proper and a closed complex submanifold. These conditions exclude the
identity blowup along the whole central fibre, disconnected exceptional
components, and a nonclosed center. The parameter c is positive rational
and sufficiently small, as required for a rational model function in the
chapter's `H(alpha)` convention.

For a point center, the calculation separates dimensions at least two from
the curve case. On a curve the blowup at the Cartier point is the identity;
the strict transform still meets the other central component at that point,
and its restricted class has degree `V_alpha-c`. Thus the same two weights
`1-c^n/V_alpha` and `c^n/V_alpha` apply, without calling the point an
exceptional divisor of a nontrivial curve modification. The existing
projective-plane energy and entropy calculation is unchanged.

## Validation and next check

The second reading checked normalization, exceptional zero weights, nef
positivity, dimension zero, connectedness of the two components and their
intersection, denominator restrictions, and the point-center calculation
in dimensions one and at least two. The new prose and proof pass the strict
writing audit with no errors or warnings. The final scoped Chapter 60
build has 86 pages, no overfull box or unresolved citation, and the same
three occurrences of an external Chapter 71 label. Physical pages 62--64
were rendered and inspected. The two-atom display now has two lines, with
its equation number properly aligned.

The available source closure remains 388 files and 11,429 labels, with no
duplicate or structural defect. The existing missing Chapter 70 input and
thirteen unresolved file/label pairs still prevent a complete-book build.
The inventory and whitespace checks pass; no research problem is retired.

The next energy pass will examine the actual proof of the Zariski
inequality and the real-parameter domain used in first variation. In
particular, a derivative along a real affine segment requires an explicitly
defined real model energy, and a difference of two model psh functions
need not itself be model psh.
