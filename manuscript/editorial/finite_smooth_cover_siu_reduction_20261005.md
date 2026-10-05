# Smooth finite covers and the critical Siu boundary

Date: 5 October 2026. Baseline: `27fd9b2`.
This is a conditional follow-up to the unadmitted
[finite descent draft](finite_galois_global_descent_followup_20261004.md).
It remains outside active TeX. The finite reflection premise is displayed
below and has not passed independent verification. None of the arguments
here removes the book's general `(SD)_k` input or solves a listed atom.

## The premise and the narrower geometric situation

For a particular finite surjection \(f:Y\to X\) of normal integral
projective varieties, denote by \(\mathrm{(FD)}_f\) the assertion
\[
 f^*u\in\operatorname{PSH}_Y(f^*\eta)
       \quad\Longrightarrow\quad
 u\in\operatorname{PSH}_X(\eta)
 \qquad(\eta\in N^1(X)_{\mathbb R}).
\]
This is an assumption in this note, not a theorem established by its
notation. The previous draft proposes it without assuming envelopes or
critical Siu division; its independent and literature gates remain pending.

For this follow-up, `k` is algebraically closed, trivially valued and of
characteristic zero. Suppose a **global finite surjection** \(f:Y\to X\)
exists with `Y` smooth and projective and `X` normal and integral.
Published BJ22b Theorem A gives the all-class envelope property on `Y`.
Published BJGreen24 Proposition 17 supplies critical homogeneous division
on that smooth variety for effective rational Cartier divisors.

This is an additional geometric hypothesis. A resolution is generally
projective birational, and does not supply such a finite map. Local
quotient charts do not supply a global smooth finite cover or the global
section-based descent required here. No local-to-global psh argument is
implicitly imported from an unacquired paper.

## Conditional all-class envelopes downstairs

Assume \(\mathrm{(FD)}_f\). Take a nonempty family
\(\{u_a\}\subset\operatorname{PSH}_X(\eta)\) uniformly bounded
above. Its pullbacks are psh by BJ22 Theorem 4.7(iii); dominance and the
finite value at the generic trivial valuation retain generic finiteness.
Put \(u=\sup_a u_a\). All-class envelopes on `Y` give
\[
 (f^*u)^*\in\operatorname{PSH}_Y(f^*\eta).
\]
The independently proved analytic openness of a finite dominant map to a
normal variety gives
\[
 f^*(u^*)=(f^*u)^*.
\]
Indeed every neighborhood upstairs maps to a neighborhood downstairs,
while every inverse image of a base neighborhood is a neighborhood of
each lift; the two neighborhood formulas for usc regularization agree.
This uses openness, not only compactness or analytic surjectivity.
The assumed \(\mathrm{(FD)}_f\) would then give
\(u^*\in\operatorname{PSH}_X(\eta)\). The class `eta` is arbitrary;
it is not asserted to be ample or nef. Thus this is an all-class
envelope reduction for varieties with the stated smooth finite cover,
conditional on finite psh reflection.

This deduction does not use the Siu theorem to prove the needed finite
openness. Chapter 41's algebraic/valuation quotient proof is the separate
input; its deeper valuation-conjugacy antecedents are reused, not freshly
reaudited in this note.

## Conditional direct descent of the Siu residual

Let \(\alpha\in N^1(X)_{\mathbb R}\), let `D` be an effective
rational Cartier divisor, and let
\[
 \psi\in\operatorname{PSH}_{\mathrm{hom},X}(\alpha),
 \qquad \psi\le\ell_D:=\log|s_D|,
 \qquad \beta=\alpha-[D].
\]
Smooth division on `Y` provides
\[
 r_Y\in\operatorname{PSH}_{\mathrm{hom},Y}(f^*\beta),
 \qquad r_Y+f^*\ell_D=f^*\psi.
\]
Use this additive formulation on the entire analytic space. The finite
divisorial difference in the source result determines the residual;
psh determination extends the additive identity to all points. The
formula does not define \(-\infty-(-\infty)\) at a proper pole.

In characteristic zero the function-field extension is separable. Take
its finite Galois closure, and let \(q:S\to X\) be normalization in
that closure. There is a finite surjection \(\rho:S\to Y\) with
\(q=f\rho\), by integral closure and the same Nagata input used in
the finite draft. Define \(r_S=\rho^*r_Y\). It is psh in
\(q^*\beta\), homogeneous, and satisfies
\[
 r_S+q^*\ell_D=q^*\psi.
\]
The Galois closure `S` need **not** be smooth. No envelope or Siu theorem
on `S` is used: the residual there is a pullback of the independently
obtained residual on `Y`.

Let `G` be the Galois group. Every group translate of `r_S` is psh in
the same class and satisfies the same additive identity. On divisorial
valuations, the values of \(q^*\ell_D\) are finite, so cancellation
there gives \(\sigma^*r_S=r_S\). Psh determination then gives this
equality at every analytic point. The independent analytic quotient
description in Chapter 41 makes each fiber a `G`-orbit, so `r_S` is
constant on each fiber.

There is therefore a base function `r_X` with \(q^*r_X=r_S\).
It is usc: for each real `c`, the closed set \(\{r_S\ge c\}\)
is saturated, and its image under the closed surjection `q^an` is
\(\{r_X\ge c\}\). Its value at the generic trivial valuation is
finite. To conclude psh membership, however, one still needs the
displayed premise \(\mathrm{(FD)}_q\), now for the Galois closure
map. Fiber constancy and usc alone do not provide it.

Assuming \(\mathrm{(FD)}_q\), we would obtain
\(r_X\in\operatorname{PSH}_X(\beta)\). Pullback commutes with
the positive-real scaling action; the homogeneity of `r_S` and
injectivity of pullback on functions give homogeneity of `r_X`.
Analytic surjectivity gives
\[
 r_X+\ell_D=\psi
\]
from its pullback identity. Uniqueness follows by cancellation on
divisorial valuations and psh determination. This would be the needed
instance of critical homogeneous division on `X`, conditional on
\(\mathrm{(FD)}_q\) and the global smooth finite cover.

For a global smooth finite **Galois** cover, `S=Y` and `q=f`, so one
reflection premise suffices for both routes. For a nongalois smooth cover,
the envelope route uses \(\mathrm{(FD)}_f\), while the direct residual
route above uses \(\mathrm{(FD)}_q\). A verified universal finite
candidate would provide both. This note does not assume that a Galois
closure of a smooth cover remains smooth.

## A concrete section calculation on the nonflat cone

The existing Chapter 41 example supplies
\[
 q:\mathbf P^2\to\mathbf P(1,1,2),
 \qquad [U:V:W]\mapsto[U:V:W^2],
\]
in characteristic different from two. Write the base weight-one
coordinates as `a,b`, its weight-two coordinate as `Z`, and
\(A=a^2\). Put \(H=\mathcal O_X(2)\). Then `H` is an actual
line bundle and \(q^*H=\mathcal O_{\mathbf P^2}(2)\).
The cover is not flat at the vertex: its fiber has length three,
although its generic field degree is two.

Let \(D=(Z=0)\), an effective Cartier divisor in class `H`. The
following are explicit homogeneous section functions:
\[
 r_X=\frac12\log|A|\in\mathcal H_{\mathrm{hom}}(H/2),
 \qquad
 \psi=\frac12\log|AZ^2|
       \in\mathcal H_{\mathrm{hom}}(3H/2).
\]
Both assertions follow directly from the indicated actual sections:
`A` is a section of `H`, and `AZ^2` is a section of `3H`; denominator
two gives the stated rational classes. Since \(\log|A|\le0\),
\(\psi\le\ell_D=\log|Z|\), and
\[
 r_X+\ell_D=\psi,
 \qquad q^*r_X=\log|U|,
 \qquad q^*\psi=\log|U|+2\log|W|.
\]
At `Z=0` the divisor term is negative infinite; at `A=0` the residual
is negative infinite. At their intersection both are negative infinite
and their sum is negative infinite, with no undefined subtraction.
At the vertex `Z` is a frame unit and `A` vanishes, so the residual
and `psi` are negative infinite while the divisor term is zero.

This example uses only global section identities and the defining
Fubini--Study class. Its division identity is unconditional and needs
neither \(\mathrm{(FD)}\) nor envelopes. It does not verify critical
division for an arbitrary psh function on this cone, and a guessed
average over two ordinary vertex points would not prove it. It is a
worked instance of the existing formal definitions, not a counterexample
to the general theorem and not a new general result.

## Remaining boundary and source record

The additional BE21 convention check matters for the literature
comparison. Its Definition 7.2 uses a fixed **semiample** rational line
bundle and decreasing ordinary Fubini--Study metrics on that line.
BJ22 Definition 4.1 instead permits generically finite section systems
and varying rational numerical classes converging to an arbitrary real
class. These are different scopes. BE21 Proposition 5.13 constructs
pullbacks of model metrics and flat extensions of models; it does not
state arbitrary-real-class reflection along a finite variety map.
BE21 Theorem 7.31 reflects psh membership after an extension of the
**ground field**, for continuous metrics on a semiample line bundle.
That is another relevant descent result, with a different displayed
map and hypotheses. No novelty claim for the present finite candidate
follows from this bounded comparison.

BE21 Proposition 5.13's target/proof, Definition 7.2, and Theorem 7.31's
target/proof were freshly checked on actual physical pages 53, 61 and
70 (printed pages 52, 60 and 69). The deeper inputs in those proofs
are not freshly audited. These checks supplement the prior selected
finite-flat norm targets; none of the cited statements authenticates
the full current candidate's scope.

The entire BJGreen24 Proposition 17 argument and its standing smooth
characteristic-zero envelope scope were reread at cached text lines
575--715. The same-byte actual source page reviewed in the earlier
audit is reused, not relabeled as a new visual review. The independent
BJ22b Theorem A source audit is also reused. The finite quotient and
nonflat cone arguments are the existing Chapter 41 inputs. No new
primary paper has been acquired in this checkpoint.

Positive-characteristic norm tests in the previous candidate do not
establish smooth all-class envelopes in that characteristic. Local
quotient singularities, nonglobal covers, nontrivially valued settings,
and a general projective birational resolution remain outside the
deductions above. In particular, the finite-cover hypotheses are not
provided by the unresolved birational approximation route. The book's
conditional general Siu/envelope interfaces remain unchanged.

For a resolution \(\pi:Y\to X\), one has `k(Y)=k(X)`. Normalizing
`X` in the Galois closure of that extension merely returns `X`; it does
not give a morphism `X->Y` inverse to the resolution. The integral-closure
argument used above constructs a map to a **finite** intermediate
normalization. It does not extend a rational map to an arbitrary proper
birational model. Closing and resolving the graph may modify the source,
after which its map to `X` can cease to be finite.

Likewise, flattening a generically finite projective alteration changes
the base to a modification `X'`. Even if its proper transform were a
smooth finite cover and gave envelopes on `X'`, passing back to `X`
would still require the unresolved birational step. The proper transform
is not automatically smooth; resolving it can again destroy finiteness.
Thus neither taking a function-field closure nor invoking flattening
turns the general resolution route into the smooth finite-cover case.
