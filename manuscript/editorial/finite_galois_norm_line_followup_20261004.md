# Local norm frames and support in the finite descent candidate

Date: 4 October 2026. Baseline: `13886a2`.
This is a supplementary same-agent check of the
[finite descent candidate](finite_galois_psh_descent_candidate_20261004.md).
The candidate remains outside active TeX, with independent verification
pending. No conditional hypothesis or problem status is removed.
The earlier candidate and its boundary manifest retain their dated bytes.

## The frame identification being checked

For the finite Galois normalization \(q:S\to X\), choose frames
`e_a` of a line bundle `M` on the full inverse images of base opens
`U_a`, as provided by Stacks Lemma 31.18.1. Write
\(e_a=v_{ab}e_b\) on overlaps. The norm line in Lemma 31.18.2 has
frames `n_a` with transition
\[
 n_a=\mathrm N(v_{ab})n_b,
 \qquad \mathrm N(v_{ab})=
       \prod_{\sigma\in G}\sigma^*v_{ab}.
\]
Consequently the local identification
\[
 q^*n_a\longmapsto\bigotimes_{\sigma\in G}\sigma^*e_a
\]
has matching transition functions. Multiplicativity of the norm also
preserves the cocycle condition on triple overlaps. The tensor factors
are ordinary invertible sheaves; no sign from a graded tensor convention
is introduced. This describes the proposed global line identification
directly through the source construction, without a determinant on a
non-locally-free algebra.

For a purely inseparable map of degree `d`, the field norm is
\(v\mapsto v^d\). The analogous local map is
\(q^*n_a\mapsto e_a^{\otimes d}\). It also identifies the pullback
of a norm section with the `d`-th power of that section. These are the
candidate's frame checks; their use in its general proof has not received
independent adversarial verification.

The trivial reference metric must be checked at the analytic center.
An analytic point of a projective variety over the trivially valued field
has a center, and morphisms carry centers to centers. A frame change that
is a local unit at that center and its inverse both lie in the dominated
local ring, so the unit has absolute value one. Thus the matching local
frames above introduce no logarithmic weight shift. This reasoning uses
frames on full preimages of a base neighborhood of the center; it does
not treat an arbitrary rational function as a unit there.

## Coefficients and weights under a base frame change

If a local section coefficient `b` is replaced by `w b`, then the
coefficient of index `r` of its orbit polynomial is replaced by
\(w^r a_r\). Therefore
\[
 \max_r\frac1r\log|w^r a_r|
       =\log|w|+\max_r\frac1r\log|a_r|.
\]
At a center where `w` is a frame unit, \(\log|w|=0\).
The section weights are unchanged, and raising coefficients to powers
to clear the denominators preserves the same frame rule.

The supplementary
[calculation](research_calculations/finite_galois_frame_covariance_20261004.py)
and [result](research_calculations/finite_galois_frame_covariance_20261004.json)
check ten scaled orbit/purely-inseparable polynomial identities and
seventeen norm-unit identities. The latter use
\(z-a\) on the full preimage of \(D(x)\) in an Artin--Schreier cover,
where \(x=z^p-z\):
\[
 \prod_{c\in\mathbb F_p}(z+c-a)=x.
\]
After inverting `x`, each factor is a unit, as its inverse is the product
of the other factors divided by `x`.

There are 1,152 selected exact weight/valuation covariance cases. Of
these, 384 use frame-unit valuation zero and test the reference-metric
value directly. The remaining nonzero frame-factor valuations test
formal covariance only; they are not passed off as local frame units at
those centers. These finite checks do not prove the full general theorem
or substitute for an independent model receipt.

## Proper support and the nonflat fiber

The cached target statements and printed proofs of Stacks Tags 0BRI and
0BRJ were freshly reread. The first gives transitivity on support primes
over an invariant-ring prime. The second gives normality of the residue
extension and surjectivity from the decomposition group to its residue
automorphism group. The valuation-extension step still uses the named
classical input in the book. Together with normality and finiteness in
the quotient setup, this is the same all-support argument already
recorded in Chapter 41; no fresh whole-antecedent audit is claimed.

The coefficient formula is an identity of regular functions before
evaluation. At an analytic point `y`, evaluate
\(\prod_{\sigma\in G}(Z-\sigma^*b)\) in its residue field.
This has degree `d`, with repetitions from the group action if roots
coincide. Its root-radius identity does not require that the fiber
algebra have dimension `d`.

In the nonflat cone example, the vertex fiber algebra has length three,
while the field degree is two. The evaluated generic norm/orbit
polynomial still has degree two. It is not asserted to be the
characteristic polynomial of multiplication on the three-dimensional
fiber algebra. No arbitrary-base-change determinant identity or guessed
sum of Artin lengths is used in this check.

## The class-limit check still needing independent review

The candidate's proposed norm map on numerical classes is restricted to
the Galois and purely inseparable normalization maps. The line identities
would give
\[
 q^*c_1(\mathrm N(M))=
    \sum_{\sigma\in G}\sigma^*c_1(M)
 \quad\text{or}\quad
 q^*c_1(\mathrm N(M))=d\,c_1(M),
\]
respectively. Injectivity of finite numerical pullback would then show
that every real numerical relation upstairs maps to a numerical relation
downstairs. A well-defined linear map between the finite-dimensional
spaces is continuous; the inverse on the image of the injective pullback
is also continuous. These are the proposed mechanisms for controlling
the rational base classes in the decreasing net, rather than a putative
pushforward for arbitrary proper maps.

The next review must check this passage together with the norm-line
identification, generic finiteness of each descended section system,
and the factorization for a general finite extension. Even acceptance of
that finite descent argument would leave the birational descent and
critical Siu issues unresolved. The active book, catalogue and inventory
remain unchanged.
