# Every actual big bundle: numerical and section-growth definitions

Root continuation123, 5 October2026. This is an UNREVIEWED cross-check
of the full big rational-bundle domain in112 Section2 and113 Section3.3.
It does not alter their candidate=false results or the frozen native
reviews114/115. It is an algebraic proof on a retained projective
carrier, not an additional analytic grant or an original closure.

Let Y be smooth integral projective of dimension n>0 over any
algebraically closed characteristic-zero field k, without a cardinality
restriction. The proof in fact only needs an infinite field and the
stated projective algebraic background. Retain an ACTUAL rational
line bundle L. For a positive integer q clearing it, write F=qL.
Then the following conditions are equivalent:

    (i) c1(L) is in the interior of the closed effective cone;
    (ii) limsup_m m^-n h0(Y,mF)>0;
    (iii) L=A+D as ACTUAL rational bundles, A ample, D effective
          rational Cartier, with a retained bundle isomorphism.

The exact interpretation of (ii) is independent of the chosen cleared
multiple, as follows also from the equivalent condition (iii).

## 1. Numerical interior gives an actual divisor presentation

Fix an actual ample H. Retain the finite-dimensional rational divisor
class space and openness of its ample cone as projective algebraic
background. Numerical ampleness of actual representatives is the
premise whose primary statement and full printed proof in
Fujino--Miyamoto1.4 were preserved in112. For sufficiently small rational
epsilon>0, c1(L)-epsilon*c1(H) is in the closed effective cone.
Its definition gives approximations by finite nonnegative real
combinations of effective Cartier classes. Approximate their finite
coefficients by nonnegative rationals. This yields an ACTUAL effective
rational Cartier divisor D whose class is sufficiently close that
c1(L)-c1(D) is ample. Numerical ampleness makes the actual rational
bundle A=L-O(D) ample. The isomorphism in (iii) is then literal in
Pic(Y) tensor Q, including any numerically trivial twist of L.
No section-ring finite generation or infinite divisor is used.

## 2. An actual presentation gives positive section growth

Clear (iii) by an integer r. Multiplication by the nonzero section of
rD gives injective maps

    H0(Y,mrA) -> H0(Y,mrL)

for every m. Injectivity follows on an integral scheme from the
nonzero divisor section, not from a numerical equality. The actual
ample bundle rA has Hilbert polynomial with positive leading term
of degree n. Stacks0BEV supplies positivity of its top ample degree,
and0BJ8 combines that degree with Serre vanishing to give the stated
positive h0 growth. Thus the section growth of a cleared L is positive.
The same argument works for ANY cleared qL: choose a further multiple
of q which also clears A,D and use that subsequence in its limsup.
This proves (iii) implies (ii) for each allowed q.

## 3. Section growth supplies an actual presentation without Bertini

Suppose (ii), and choose an actual very ample integral bundle M on Y.
Take any nonzero section of M, with effective Cartier divisor T.
Since Y is integral and n>0, this is a Cartier hyperplane of pure
top dimension n-1; it need not be smooth or reduced. The argument
does not need an assertion about general hyperplanes over k.

On the projective scheme T, choose an actual ample N sufficiently
positive that N-F|T is globally generated. The finitely many associated
points of O_T give finitely many prohibited proper linear subspaces
in its section space. Global generation makes each prohibited
subspace proper. Since k is infinite, choose a section outside their
union. It is a regular section, so its powers give injections

    F^m|T -> N^m.

Serre vanishing and the coherent Euler-polynomial support bound on T
therefore give

    h0(T,F^m|T) <= h0(T,N^m) = O(m^(n-1)).

This bound is valid with nilpotents or embedded associated points on
T: the coherent sheaf has support dimension at most n-1. The usual
effective Cartier restriction sequence gives

    h0(Y,mF-M) >= h0(Y,mF) - O(m^(n-1)).

There are arbitrarily large m with h0(Y,mF) bounded below by a fixed
positive multiple of m^n. Choose one large enough that the right side
is positive. A nonzero section of mF-M has effective Cartier divisor
G. Its actual bundle identity yields

    L = M/(qm) + G/(qm).

Set A=M/(qm), D=G/(qm) and retain this isomorphism. This proves (iii)
directly from the growth definition. There is no modification of Y,
countable-field reduction, Bertini use or asymptotic section-ring
generation assumption. It is the complete argument in113 Section3.3
applied on the projective original carrier of112.

## 4. An actual ample-plus-effective presentation is numerical interior

For clarity, the ample cone is contained in the interior of the
closed effective cone without defining bigness by a circular rule.
Choose a finite rational divisor-class basis of N1(Y). Around an
ample class a choose a sufficiently small rational delta so that
a plus or minus delta times each basis vector is ample. Each such
rational ample class has an actual ample representative. A high
integral power has a nonzero section, hence its class is effective
after rational division. The convex hull of these finitely many
effective rational classes contains a neighborhood of a. Therefore
a is interior to the closed effective cone. Adding an effective
class preserves that interior. This proves (iii) implies (i).

## 5. Exact use and sources

Thus every big ACTUAL rational bundle in either standard definition
has the retained divisor data used by the proposed equation theorem,
and the two manuscripts cover the same full big domain. The possible
numerically trivial twist never disappears from a section calculation.
On a proper smooth original X,113's actual identity
H0(Y,pi^*F)=H0(X,F) transfers the growth definition to its projective
modification; the same construction then supplies A,D upstairs. It
does not assert an ample bundle on a nonprojective X.

The projective algebraic background is actual ample global generation
and Serre vanishing (Stacks01Q3 and0B5T), coherent Euler-polynomial
support bounds (Stacks0BEM), positive top ample degree and its precise
asymptotic h0 growth (Stacks0BEV and0BJ8), regular-section detection
at associated points, finite-dimensional N1 and numerical ampleness.
The numerical ampleness source is Fujino--Miyamoto1.4, with its exact
primary proof already preserved and read. The01Q3/0B5T/0BEM bodies
are preserved in113's algebraic-growth ledger and were freshly opened
here. The additional0BEV/0BJ8 statements and printed proofs were also
freshly opened and are retained with this note's source binding.
This note does not claim all their recursive background proofs were read.
All nonample analytic cone, local operator, reference, mass, energy,
target integrability and attained equation assertions still require
their own full reconstruction and independent review.
