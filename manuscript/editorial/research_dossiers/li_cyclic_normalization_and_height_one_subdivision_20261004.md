# Cyclic normalization, reduced fibres and height-one subdivisions

Date: 4 October 2026. This book-external local calculation separates the
normalization and reducedness steps from the regular semistable-model
construction. It is a formal consequence of the standard character
lattice description, written with its algebraic proof and exact source
boundaries. It does not supply a global compatible subdivision theorem,
certify an analytic/germ comparison or admit a new book theorem.

## Local signature and irreducible factors

Work over C, with r>=1 boundary coordinates z_1,...,z_r, positive
integers b_i, and ordinary transverse coordinates w. The local model is

\[
                  t=z^b=\prod_{i=1}^r z_i^{b_i}.
                                                               \tag{1}
\]

An analytic unit in (1) can be removed after taking a local holomorphic
root on a sufficiently small coordinate neighborhood. This is a local
choice, not a global root. We first treat the affine polynomial model;
transfer to its analytic germ and compatibility with normalization are
explicit comparison inputs. Ordinary w factors do not change any boundary
lattice or valuation calculation below.

For t=tau^q, q>=1, let

\[
 d=\gcd(q,b_1,\ldots,b_r),\quad q'=q/d,\quad b'=b/d.
                                                               \tag{2}
\]

The equation tau^q=z^b has d irreducible factors
tau^{q'}=z^{b'} times a root of unity. Constants have roots in C, so
the factors are isomorphic over the z-space. Their normalizations are
disjoint. These are local factors; d is not asserted to be the number
of connected components of a global family or its generic fibre.

For one factor put

\[
 M=\mathbb Z^r,\quad M'=M+\mathbb Z\frac bq,
 \qquad
 N'=\{v\in\mathbb Z^r:b\cdot v\in q\mathbb Z\},
 \qquad \sigma=\mathbb R_{\geq0}^r.                    \tag{3}
\]

The least k>0 for which k b/q lies in M is q', so [M':M]=q'.
The group algebra C[M'] is the domain obtained by adjoining the
character chi^{b/q} to C[M]; its free C[M]-basis consists of these
characters to the powers 0,...,q'-1. Thus the factor polynomial has
degree q' and is irreducible on the torus, hence in the polynomial
ring. This also proves the stated factor count without treating a
possibly reducible root hypersurface as normal.

## Normalization of the semigroup ring

The factor's coordinate ring is C[S], where

\[
 S=\mathbb Z_{\geq0}^r+\mathbb Z_{\geq0}\frac bq
                  \subset M'.
\]

Its normalization is

\[
                \mathbb C[\sigma^\vee\cap M'].
                                                               \tag{4}
\]

Here the cone is self-dual in the displayed coordinates. To verify (4),
each m in sigma^vee intersect M' has q m in Z_{>=0}^r.
The monomial chi^m is therefore integral, satisfying
X^q-chi^{q m}=0. Conversely, an element integral over C[S]
belongs to C[M']: localizing by its boundary monomials gives the
normal Laurent group algebra. For each coordinate, the minimum
coordinate exponent defines a discrete monomial valuation on its
fraction field. Its valuation ring contains C[S], so an integral
element has nonnegative value at every coordinate valuation. Within
the Laurent algebra this says that all its monomial exponents lie
in sigma^vee; distinct Laurent characters prevent a lowest-level
term from disappearing without being zero. This proves the reverse
inclusion.

Finiteness here can be checked directly. In the coset
j b/q+M, 0<=j<q', the smallest coordinatewise nonnegative
representative is

\[
 m_j=\frac{j b}{q}-\left\lfloor\frac{j b}{q}\right\rfloor.
\]

Every nonnegative exponent in this coset is m_j plus an element
of Z_{>=0}^r. The q' characters chi^{m_j} consequently generate
(4) as a module over C[z_1,...,z_r]. They also generate it over
C[S]. The normalization map is finite on this affine local model.
This direct calculation is not an assertion of finite normalization
in every analytic or scheme category.

Ambro arXiv:1310.3951v2, Proposition 3.7, physical page 24, gives
precisely the normalized toric description. Its proof uses the torus
calculation of Proposition 2.10 and normalization in the field extension.
The latter torus calculation has a complete displayed proof on page 16.
Section 3, rather than the earlier unnormalized-root remark, controls
the use of (4).

## Multiplicity after normalization

The primitive lattice vector on the i-th boundary ray is

\[
 v_i=\lambda_i e_i,\qquad
 \lambda_i=\frac q{\gcd(q,b_i)}.                       \tag{5}
\]

Indeed, k e_i lies in N' exactly when q divides k b_i.
The normalized parameter character has height

\[
 \ell(v)=\frac{b\cdot v}{q}\in\mathbb Z\quad(v\in N'),
 \qquad
 c_i=\ell(v_i)=\frac{b_i}{\gcd(q,b_i)}.                \tag{6}
\]

The divisor of tau on this normalized toric chart therefore has
coefficient c_i along the boundary component associated to v_i.
No new rays appear under this finite normalization. The ramification
index of the projection along that boundary is lambda_i. This
agrees with Ambro Lemmas 3.4–3.5 on physical page 22: their
ramification index is q/gcd(q,ord_E(t)), while the parameter
order is obtained by dividing its pulled-back order by q.

If each b_i divides q, then every c_i is one, and the central fibre
is scheme-theoretically reduced. One can also check reducedness
directly in (4). The ray valuations of a monomial are the integers
lambda_i m_i. Membership in (tau) is equivalent to
lambda_i m_i>=1 for every i, because the exponent of tau has
each such value equal to one. Consequently (tau) is the intersection
of the boundary prime ideals. This is a radical ideal. Conversely,
a coefficient c_i>1 is visible at the generic DVR of that boundary
and makes the central fibre nonreduced. Thus divisibility by every
b_i is exactly the reducedness condition on this local normalized
cover.

This proves reducedness, not regularity of the total space. For
example, t=xy with q=2 becomes tau^2=xy. Its coordinate ring is
already normal, its central fibre is the reduced union xy=0, and
its total space is singular at the origin. In (3),
N'={(a,b):a+b is even}; the two primitive boundary vectors
2e_1,2e_2 generate an index-two sublattice of N'. The Jacobian
of tau^2-xy vanishes at the origin as well. This elementary local
example is not a counterexample to semistable reduction.

For comparison, when r=1,b_1=3,q=2, normalization is
z=u^2,tau=u^3. It is smooth, but its central fibre has multiplicity
three, in agreement with (6). Neither total regularity nor reducedness
implies the other without the required model hypotheses.

## The regular and reduced subdivision criterion

The usual affine toric smoothness criterion is that the primitive
vectors of each full-dimensional cone form a basis of N'. For the
unsubdivided chart their index is

\[
 [N':\bigoplus_i\mathbb Z v_i]
       =\frac{\prod_i\lambda_i}{q/d}.                 \tag{7}
\]

This follows by computing both sublattice indices in Z^r:
[Z^r:N']=q/d and the diagonal-vector lattice has index
product lambda_i. The toric smoothness criterion is a standard
import, not a new general singularity theorem proved here.

Assume henceforth every b_i divides q. The height-one slice is the
lattice simplex

\[
 P_q=\{v\in\sigma:b\cdot v=q\}
          =\operatorname{conv}\{(q/b_i)e_i\}_i.        \tag{8}
\]

A simplicial fan subdivision of sigma is smooth and has reduced
central divisor if every maximal cone is generated by a lattice
basis and every primitive ray has height one. Equivalently its
height-one slice is a unimodular triangulation of P_q in the
affine lattice N' intersect {ell=1}. The difference lattice is

\[
              H=\{v\in\mathbb Z^r:b\cdot v=0\}.
                                                               \tag{9}
\]

For completeness, pick one height-one vertex v_0. The height
homomorphism N'->Z is surjective, since ell(v_0)=1, and
N'=H plus Z v_0. For a height-one simplex with vertices
v_0,...,v_{r-1}, the determinant index of its cone is the index
of v_1-v_0,...,v_{r-1}-v_0 in H. This proves the equivalence
with affine unimodularity, including the r=1 point case.

A further cover of total degree a q replaces N' by

\[
 N_a=\{v\in\mathbb Z^r:b\cdot v\in a q\mathbb Z\},
 \qquad P_{a q}=aP_q.                                 \tag{10}
\]

The difference lattice H is unchanged. Translation by a v_0
identifies the affine lattice on aP_q with H. Thus the additional
parameter cover is exactly a dilation problem for the height-one
polytope, with the same difference lattice, rather than an arbitrary
resolution of the original cone. A coherent unimodular triangulation
of aP_q would give a projective regular reduced toric model.
No existence assertion for that triangulation is supplied by (10).

An arbitrary blowup can lose reducedness. In the already reduced
model t=xy, blowing up x=y=0 has a chart x=u,y=uv and therefore
t=u^2v. The exceptional component has multiplicity two. This direct
coordinate calculation explains why resolving the normalized cover
and retaining reducedness are separate requirements.

## A coherent subdivision as a normalized monomial blowup

On a single affine toric chart, suppose a finite coherent rational
subdivision has been supplied. In the usual sign convention its
order function can be written

\[
                 h(v)=\min_j\langle m_j,v\rangle
\]

with integral m_j after clearing a common denominator. Add the
same sufficiently large integral interior linear form to all m_j
so that they lie in sigma^vee intersect M'. This changes no
domains of linearity. The monomial ideal

\[
                         I=(\chi^{m_j})_j             \tag{11}
\]

is coherent and nonzero and equals O off tau=0. The blowup chart
where chi^{m_i} generates is the semigroup algebra obtained by
adjoining every chi^{m_j-m_i}. Normalizing this chart saturates
its exponent semigroup; its cone is

\[
 \{v\in\sigma:\langle m_j-m_i,v\rangle\geq0
                              \text{ for every }j\}.
                                                               \tag{12}
\]

These are exactly the domains where m_i realizes the minimum h.
They glue to the supplied subdivision. The standard toric
normalization/gluing and finite generation for rational cones are
explicit imports at this step. This gives a normalized monomial
blowup presentation when the coherent subdivision is supplied.
The previous positive-model dossier can therefore be applied to
such a local projective subdivision, conditional on a global
compatible projective realization.

Globalization requires a simultaneous subdivision of the finite
cone/height-slice complex, agreeing on every common face, together
with a global integral order function and its coherent vertical
ideal. Applying a triangulation theorem separately to every maximal
polytope does not prove this compatibility. Analytic descent from
coordinate charts, projectivity and normalization finiteness remain
category requirements too.

## Precise source boundaries and literal diagnostics

Ambro's Theorem 3.8, physical pages 24–25, preserves the category of
quasi-smooth toroidal embeddings for normalized roots under its
normality, characteristic and integral-on-the-open-part hypotheses.
Its proof reduces to Proposition 3.7 and imports the local toroidal
chart and divisor-class inputs. These antecedents are not all newly
checked here; the theorem is not substituted for smooth reduced
semistable reduction.

The early unnormalized-root statements require care. Physical page
16, Remark 2.11, identifies the ordinary root of a regular torus
character with the normal toric lattice-change space. With X=A^1,
q=2 and character z^3, the ordinary root is the cusp
C[z,tau]/(tau^2-z^3)=C[u^2,u^3]. The element u=tau/z lies in
its fraction field and satisfies u^2=z, but is not in the ring,
as its exponents belong to the semigroup generated by 2 and 3.
Thus it is not normal and cannot equal C[u], the toric normalization.
The same distinction affects the literal component/line description
in Example 2.9 on page 15. The bars and missing distinction were
checked in the actual PDF, rather than inferred from extracted text.
These are diagnostics of those literal auxiliary statements; they
do not disprove Proposition 3.7, whose normalized formulation is
used above, or the paper's principal theorem. No corrected journal
edition was acquired or asserted equivalent.

Abramovich–Karu arXiv:alg-geom/9707012v1 explicitly labels itself
a preliminary version. Definition 0.1 on page 2 distinguishes weak
semistability from semistability by total smoothness. Its construction
is said on page 3 to modify even a smooth generic fibre; it therefore
cannot automatically preserve the fixed CY family in our route.
Proposition 5.9 and the proof of Proposition 5.1 describe the lattice
change and reduced rays. Definitions 8.1–8.3 and the later discussion
separate lattice alteration, regularity and subdivision. Its general
Theorem 0.3 and the remaining proof dependencies have not received
a complete new proof verification, and its historical conjectures
are not asserted to describe the current 2026 state of the art.

The next source task is a primary-source triangulation result with
coherence and face-compatible finite-complex scope, not just the
single-polytope existence statement. The current local calculation
changes no active manuscript, frozen artifact, open-problem status
or verifier receipt. No new finite experiment or separate production
verifier was run.
