# Exact residual claims from the general non-Archimedean Monge--Ampere attempt

Audit the following two statement--proof pairs.  They are intended as a
conditional theorem and a counterexample, not as a solution of the general
non-Archimedean Monge--Ampere equation.  Reject any hidden compactness,
differentiability, geometric-integrality, component-mass, or descent
assumption.

## Conditional variational statement

Let \(V>0\), and let \(\mathcal E^1\) be a class of potentials, stable under
addition of constants, with an energy \(E\) and a measure map \(\operatorname{MA}\)
satisfying
\[
 E(u+c)=E(u)+cV,
 \qquad \operatorname{MA}(u)(X)=V.
\]
Let \(\mu\) be a positive Radon measure of mass \(V\) such that every member
of \(\mathcal E^1\) is \(\mu\)-integrable, and set
\[
 F_\mu(u)=E(u)-\int_Xu\,\mathrm d\mu.
\]
Assume the following four hypotheses.

1. \(F_\mu\) is finite somewhere.  Every normalized maximizing sequence has
   a convergent subsequence with limit in \(\mathcal E^1\), and \(F_\mu\) is
   upper semicontinuous for this convergence.
2. For every function \(f\) in a measure-determining vector space
   \(\mathcal T\subset C^0(X)\), the rooftop envelope
   \(P_t=P(u+tf)\) belongs to \(\mathcal E^1\), satisfies
   \(P_t\leq u+tf\), and obeys
   \[
   \left.\frac{\mathrm d}{\mathrm dt}\right|_{t=0}
       E(P(u+tf))=\int_X f\,\operatorname{MA}(u).
   \]
3. The same first-variation statement holds with \(-f\) in place of \(f\).
4. The equality case of comparison holds:
   \(\operatorname{MA}(u)=\operatorname{MA}(v)\) implies that \(u-v\) is
   constant.

Then \(F_\mu\) has a maximizer \(u\), this maximizer satisfies
\(\operatorname{MA}(u)=\mu\), and it is unique modulo constants.

### Proof

The two mass identities make \(F_\mu\) invariant under constants.  Normalize
a maximizing sequence.  Hypothesis 1 gives a convergent subsequence with
limit \(u\in\mathcal E^1\), and upper semicontinuity shows that \(u\) is a
maximizer.  Fix \(f\in\mathcal T\).  Maximality and \(P_t\leq u+tf\) give,
for \(t>0\),
\[
 E(P_t)-E(u)
 \leq \int_X(P_t-u)\,\mathrm d\mu
 \leq t\int_X f\,\mathrm d\mu.
\]
Divide by \(t\) and let \(t\downarrow0\).  Hypothesis 2 yields
\[
 \int_X f\,\operatorname{MA}(u)\leq\int_X f\,\mathrm d\mu.
\]
Apply the same argument to \(-f\), using Hypothesis 3, to obtain the reverse
inequality.  The two measures therefore agree on the measure-determining
space \(\mathcal T\), hence \(\operatorname{MA}(u)=\mu\).  If \(v\) is
another solution, Hypothesis 4 makes \(u-v\) constant.

## Base-change counterexample

There is no rule that determines a base-changed Monge--Ampere measure from
only its downstairs pushforward and total mass for every integral projective
variety.  More precisely, let \(F/K\) be a finite separable extension of
degree \(d>1\), let
\[
 X=\mathbf P^1_F
\]
be viewed as an integral projective \(K\)-variety, and let
\(L=\mathcal O_{\mathbf P^1_F}(1)\).  Choose a complete extension \(K'/K\)
that splits \(F/K\).  Then
\[
 X_{K'}\simeq\coprod_{i=1}^d\mathbf P^1_{K'},
\]
and the inverse image of the downstairs model Gauss point \(x\) consists of
model Gauss points \(y_1,\ldots,y_d\).  Every measure
\[
 \nu_{\mathbf w}=\sum_{i=1}^d w_i\delta_{y_i},
 \qquad w_i\geq0,\qquad\sum_iw_i=d,
\]
has total mass \(d\) and pushforward \(d\delta_x\).  If some \(w_i\ne1\),
however, \(\nu_{\mathbf w}\) is not the Monge--Ampere measure of a
semipositive metric on the pullback of \(L\), since the restriction of such
a measure to the \(i\)-th connected component has the fixed mass
\(\deg\mathcal O_{\mathbf P^1}(1)=1\).  Thus pushforward and total mass do
not determine the geometric lift; componentwise masses or equivalent descent
data are indispensable.  Moreover, even for the geometric lift
\(\sum_i\delta_{y_i}\), solutions on the split space are unique only up to
one additive constant on each component, not up to a single global constant.

### Proof

Separable splitting gives
\(F\otimes_KK'\simeq\prod_{i=1}^dK'\), hence the displayed decomposition of
\(X_{K'}\).  Each \(y_i\) maps to \(x\), which proves both the pushforward
formula and the total-mass formula for \(\nu_{\mathbf w}\).  The total
Monge--Ampere mass on a connected projective curve is the degree of the
polarizing line bundle.  Restricting the pullback of \(L\) to each component
therefore forces mass one on that component, excluding every unequal weight
vector.  Finally, adding a constant independently on each open-and-closed
component changes no curvature measure.  This proves the asserted ambiguity
and the failure of one-constant uniqueness.
