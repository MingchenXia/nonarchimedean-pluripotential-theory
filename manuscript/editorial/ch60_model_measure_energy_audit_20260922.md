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

## Zariski inequality and real model energy

The former Zariski paragraph attributed a componentwise Hodge-index
argument to MP24 Lemma 4.2.6. The checked source instead uses the
intersection matrix of central components. The book now gives that
finite-dimensional argument explicitly. Writing the central fibre as
`sum b_i E_i`, the divisor of psi as `sum b_i a_i E_i`, and the mixed
intersection matrix as Q, one has nonnegative off-diagonal entries and
`sum_j b_j Q_ij = 0`. Consequently

`D^2 Gamma = -sum_{i<j} b_i b_j Q_ij (a_i-a_j)^2 <= 0`.

The proof includes real coefficients, empty or disconnected pairwise
intersections, zero weights and the empty mixed product in dimension one.
An exact two-component arithmetic check with multiplicities 2 and 3,
off-diagonal intersection 5 and values 1 and 4 gives -270 on both sides;
the proof for all dimensions and all coefficients is the displayed
weighted-row-sum calculation, not this check.

The real model psh class is now explicitly defined by relative nefness of
real vertical divisors. The signed model measure and its mass/positivity
proof use the same real domain. Energy and J are defined as polynomials
on the real divisor space of a fixed model, so differentiation along a
real affine segment is meaningful. The rational energy agrees with
[MP24 Definition 4.2.9, arXiv version 2](https://arxiv.org/html/2409.06221v2);
the existing multilinear pairing supplies the real extension.

The first-variation and cocycle identities now allow arbitrary real PL
directions. For monotonicity between ordered model psh endpoints, the
proof differentiates their affine segment and pairs their nonnegative
difference with a positive Monge--Ampère measure. It does not assert that
the difference is psh. Concavity uses the Zariski inequality for dimension
at least one; in dimension zero the energy polynomial is affine. The
definition of J was split into two displayed lines without changing its
formula.

The automatic second pass checked the b_i normalization, the off-diagonal
intersection dimensions, the weighted row sums and their quadratic
expansion, the signed-measure versus positive-measure scopes, both
variation directions, and the dimension-zero exception. The writing
audit has zero errors and one reviewed warning for the retained existing
definition title “Energy and J”. The final scoped build has 87 pages,
no overfull box or unresolved citation, and the same three occurrences
of the external Chapter 71 reference. Physical pages 57--59 and 62--66
were rendered and inspected, covering the real-class definition,
measure extension, matrix proof, first variation and their transitions.
The warning's closing rule remains with its final paragraph across its
page break.

The source, inventory and whitespace checks retain their previous status:
388 available files, 11,429 labels, no duplicate or structural defects,
and the same missing Chapter 70 input with thirteen file/label pairs.
No full-build success, research novelty or problem retirement is claimed.


## Finite-energy measures

The mixed finiteness import is now identified as
[MP24, arXiv version 2, Proposition 4.4.4](https://arxiv.org/html/2409.06221v2).
The twisted pairing with a general background beta is explicitly the
difference of the finite pairings with C alpha + beta and C alpha.
Its independence of C follows by taking the two finite decreasing limits
of the model identity. The coordinates remain (class, potential), as in
MP24 Definition 4.4.6; the reversed coordinates printed in that version's
Definition 4.4.7 are not copied.

For an arbitrary rational PL test function psi, the proof first chooses
a strictly positive rational vertical perturbation A on a fixed model.
For sufficiently large integer N, both N phi_A + psi and N phi_A are
model psh in N alpha. Their finite pairings define the test-function
pairing by subtraction. Using one decreasing model net proves
independence of this representation; the canonical extended pairings in
turn prove independence of the net. The argument does not presume that
psi itself becomes psh just by increasing its pulled-back background.

`prop:mp-e1-ma-existence` now supplies the positive-functional construction
implicit in MP24 Remark 4.4.8. Model testing gives rational linearity,
positivity, norm at most one and value one on constants. Uniform density
extends the functional to real continuous functions, and Riesz
representation on the compact Hausdorff spectrum gives a unique Radon
probability measure. An explicit uniform-approximation estimate proves
weak convergence along every decreasing model net with finite-energy
limit. No metrizability, countable model family or exchange of two
infinite quantities is assumed.

The second pass checked domains of both difference constructions,
strict positivity on all central components, finiteness before subtraction,
independence in both choices, rational-to-real extension, positivity and
mass, and the directed-net weak-convergence estimate. The new text passes
the strict writing audit with zero errors or warnings. The final scoped
build has 89 pages, no overfull box or unresolved citation, and the same
three external Chapter 71 reference occurrences. Physical pages 70–72
were inspected after the second revision; the twisted-energy formula
now stays with its introducing sentence. The source closure has 388 files
and 11,431 labels, with the same missing Chapter 70 input and thirteen
unresolved file/label pairs. Structure, inventory and whitespace checks
retain their passing status. No full-build or research-retirement claim
is made. The joint psh and growth hypotheses in the ray construction are
the next check.
