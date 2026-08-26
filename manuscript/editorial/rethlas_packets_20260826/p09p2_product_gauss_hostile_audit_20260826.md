# P09.2 product--Gauss hostile audit

Date: 26 August 2026
Scope: hostile review of the abstract product--Gauss argument only.  This is
an isolated editorial artifact.  It is not a verified result and is not live
chapter text.

## Abstract statement audited

Let (K) be algebraically closed, complete, and nontrivially valued.  Let
(X) be an algebraic (K)-variety equipped with an algebraic action of a
split torus (T), with character and cocharacter lattices (M) and (N).
Let

\[
 h:X^{\mathrm{an}}\longrightarrow N_{\mathbf R}
\]

be integral PL and suppose

\[
 h(t\mathbin{\cdot}x)=\operatorname{trop}_T(t)+h(x).
\]

Let (q) be a symmetric nondegenerate real bilinear form on
(N_{\mathbf R}), and put

\[
 F(y)=\frac12q(y,y)+\ell(y)+c.
\]

The proposed conclusion is that, if the metric on the trivial bundle with
weight (F\circ h) is an ordinary Gubler--K\"unnemann delta-metric, then
every coordinate of (h) is CLD-smooth.

## Verdict

No counterexample or fatal defect was found after repairing the points listed
below.  The product--Gauss mechanism is substantially stronger than the
earlier attempt at constructing torus lineality directly on a Raynaud
extension: the auxiliary first torus factor supplies the missing directions,
and a specialization lemma brings the resulting linearity back to (X).

The argument is viable under the hypotheses above, provided that
``CLD-smooth'' means smooth as a CLD function, equivalently locally a real
linear combination of logarithms of analytic units in the present PL
situation.  The proof does not automatically show that each coordinate is
the logarithm of one analytic unit.  Nothing in this audit constitutes
production Rethlas verification.

## The common-cell lemma

Let

\[
 \pi:T\times X\longrightarrow X,
 \qquad
 \rho(t,z)=\operatorname{trop}_T(t)+h(z).
\]

Fix (x\in X^{\mathrm{an}}).  For (w\in N_{\mathbf R}), denote by
(y_w\) the relative Gauss point in the analytic fibre

\[
 T_{\mathscr H(x)}^{\mathrm{an}}
   =\pi^{-1}(x)
\]

whose seminorm is

\[
 \left|\sum_m a_m\chi^m\right|_{y_w}
   =\max_m |a_m|\exp(-\langle m,w\rangle).
\]

This is the precise meaning of the informal notation
((\eta_w,x)); the underlying set of a Berkovich fibre product is not a
Cartesian product of underlying sets.

Choose an ordinary delta-chart for the pullback of the metric by the algebraic
action map

\[
 \mu:T\times X\longrightarrow X.
\]

Refine it simultaneously with:

1. an algebraic tropical presentation of the finitely many coordinates of
   the integral-PL map \(\rho\);
2. the characters of a basis of the first torus factor;
3. local complexes of definition for the PL factor and for the coefficients
   of the ambient codimension-zero superform.

The refinement must be an ordinary algebraic tropical chart, obtained for
example from a graph embedding of a common very affine open, rather than
merely an analytic moment map.  Write it as

\[
 \Phi:V\longrightarrow P\subset\mathbf R^s,
 \qquad
 \rho|_V=H\circ\Phi,
\]

where (H:P\to N_{\mathbf R}) is piecewise integral affine.  Pull the old
ambient superform to the new ambient space by the integral-affine projection
to the old chart.

Let (f_1,\ldots,f_s) be the algebraic unit coordinates of the final chart.
After restriction to the fibre over (x), each (f_j) is an element of

\[
 \mathscr H(x)(M)^\times.
\]

Consequently, it is a quotient of two finite Laurent polynomials, and

\[
 z(w'):=\Phi(y_{w'})
\]

is a finite piecewise integral-affine function of (w').  The walls on which
a numerator or denominator has more than one leading Laurent monomial form a
finite polyhedral arrangement locally.  The included first-factor characters
show that the linear part

\[
 a:N_{\mathbf R}\longrightarrow\mathbf R^s
\]

of (z) on every full-dimensional chamber is injective.

All chart coordinates and all target complexes have now been fixed.  Pull
their finitely many local walls back along (z).  Since the value group
(\Gamma=-\log|K^\times|) is a nonzero divisible subgroup of
(\mathbf R), the set (N\otimes_{\mathbf Z}\Gamma) is dense in
(N_{\mathbf R}).  We may therefore choose a
(\Gamma)-rational (w), arbitrarily close to the original value, in the
relative interior of a full-dimensional stratum of the pulled-back
arrangement.  For (w') near (w),

\[
 z(w')=z_0+a(w'-w),
 \qquad z_0=z(w),
\]

and this affine piece lies in one cell (C) of the common target complex,
with (z_0\in\operatorname{relint}(C)).  Hence

\[
 a(N_{\mathbf R})\subset L_C.
\]

Since

\[
 H(z(w'))=\rho(y_{w'})=w'+h(x),
\]

differentiation along this affine Gauss locus gives

\[
 D_C H\circ a=\operatorname{id}_{N_{\mathbf R}}.
\]

If (\sigma\) lies in the star of (C), the affine restrictions of (H) to
(\sigma) and (C) agree on (C).  Therefore

\[
 D_\sigma H\circ a=D_C H\circ a
   =\operatorname{id}_{N_{\mathbf R}}.
\]

This proof deliberately uses only the relative Gauss path.  It does not claim
that torus points with small tropicalization are analytically close to the
identity, and it does not require a whole analytic neighbourhood to be stable
under such translations.

## The ambient-tensor contraction

Let the codimension-zero ambient superform in the final chart be

\[
 \gamma=\sum_{i,j}G_{ij}(z)\,\mathrm d'z_i\wedge\mathrm d''z_j.
\]

The coefficient functions in Gubler--K\"unnemann Definition 9.9(ii) are
single-valued continuous piecewise-smooth functions on the full ambient
space.  Thus they have one coefficient tensor (G_0) at (z_0).  On the
relative interior of every cell (\sigma\) in the star of (C), the
facewise Hessian of (F\circ H) is

\[
 q(D_\sigma H\,\mathord\cdot,D_\sigma H\,\mathord\cdot).
\]

Taking the limit to (z_0) gives

\[
 G_0|_{L_\sigma\times L_\sigma}
  =q(D_\sigma H\,\mathord\cdot,
     D_\sigma H\,\mathord\cdot).
\]

For (v\in N_{\mathbf R}), set

\[
 \alpha_v=G_0(a(v),\mathord\cdot).
\]

The common-cell lemma yields

\[
 \alpha_v|_{L_\sigma}
  =q(v,D_\sigma H\,\mathord\cdot)
  =\mathrm d\bigl(q(v,H)\bigr)|_\sigma.
\]

The cells in the star all contain (C), and their affine restrictions have
the same value at (z_0).  It follows that, on the whole star germ,

\[
 q(v,H(z))=q(v,H(z_0))+\alpha_v(z-z_0).
\]

Thus (q(v,\rho)) is represented by one real affine function on one ordinary
algebraic tropical chart, and is an \(\mathbf R\)-linear analytic germ.

For (m=q^\sharp(v)\), this says

\[
 \langle m,\operatorname{trop}_T\rangle
   +\pi^*\langle m,h\rangle
\]

is \(\mathbf R\)-linear at (y_w).  Since (q^\sharp) is an isomorphism,
this applies to every lattice coordinate (m\in M).

## The Gauss-specialization lemma

Let (u) be an \(\mathbf R\)-PL germ at (x\), let (m\in M), and assume

\[
 \pi^*u+\langle m,\operatorname{trop}_T\rangle
\]

is \(\mathbf R\)-linear at the \(\Gamma\)-rational relative Gauss point
(y_w\).  Then (u) is \(\mathbf R\)-linear at (x).

Indeed, on an ordinary analytic neighbourhood (W\) of (y_w), write

\[
 \pi^*u+\langle m,\operatorname{trop}_T\rangle
   =c+\sum_{j=1}^k\lambda_j\log|g_j|,
 \qquad g_j\in\mathcal O(W)^\times.
\]

The fibre neighbourhood

\[
 W_x=W\cap T_{\mathscr H(x)}^{\mathrm{an}}
\]

contains an \(\mathscr H(x)\)-rational torus point.  To see this, scale the
coordinates by elements of (K^\times) so that (w=0).  A basic
neighbourhood of the unit Gauss point imposes only finitely many strict
conditions on analytic Laurent series.  The relevant normalized initial
forms are nonzero Laurent polynomials.  The residue field

\[
 \widetilde{\mathscr H(x)}
\]

contains the algebraically closed, hence infinite, residue field of (K).
A nonempty Zariski open subset of a split torus over an infinite field has a
rational point.  Choose a residue tuple avoiding the finitely many initial
zero loci and lift it to an \(\mathscr H(x)\)-rational point
(t_x\in W_x\).

The field \(\mathscr H(x)\) is the completion of the residue field of the
analytic local ring \(\mathcal O_{X^{\mathrm{an}},x}\).  Approximate the
finitely many coordinates of (t_x) sufficiently closely by values of germs

\[
 b_1,\ldots,b_r\in\mathcal O_{X^{\mathrm{an}},x}^\times.
\]

The approximations can be chosen so that
((b_1(x),\ldots,b_r(x))\) still belongs to (W_x).  The germs define an
analytic local section

\[
 s:U\longrightarrow T\times X,
 \qquad
 z\longmapsto(b_1(z),\ldots,b_r(z),z).
\]

After shrinking (U), its image lies in (W).  Pulling the displayed
\(\mathbf R\)-linear identity back by (s) and subtracting

\[
 \langle m,\operatorname{trop}_T(b_1,\ldots,b_r)\rangle,
\]

which is the logarithm of an analytic unit, proves that (u) is
\(\mathbf R\)-linear at (x).

Notice that the section does not pass through the Gauss point.  It passes
through a rational point in the same neighbourhood on which the germ identity
holds.  Direct ``evaluation at the Gauss point'' would not prove the lemma.

Combining this specialization lemma with the ambient-tensor contraction for
a lattice basis of (M) proves that all coordinate functions of (h) are
CLD-smooth.

## Exact gap ledger

1. **The product point must be defined correctly.**  The symbol
   ((\eta_w,x)) must mean the relative Gauss point of
   (T_{\mathscr H(x)}^{\mathrm{an}}).  A Berkovich fibre product is not a
   Cartesian product of underlying point sets.

2. **The generic point is chosen last and is \(\Gamma\)-rational.**  The
   ordinary chart, every algebraized coordinate, and every local complex must
   be fixed before (w) is chosen.  Otherwise new coordinates introduce new
   Laurent tie walls.  \(\Gamma\)-rationality is also required by the
   specialization argument.

3. **The common refinement is algebraic.**  An analytic moment map alone is
   insufficient for ordinary delta-metricity.  One must algebraize the finite
   moment coordinates, take a common very affine graph embedding, and pull the
   old ambient form back by the resulting integral-affine projection.

4. **No analytic-smallness assertion for tropical translations is allowed.**
   Elements of (T(K)) whose tropicalizations tend to zero need not tend to
   the identity in the analytic topology.  The proof above avoids this false
   step by using only the affine path of relative Gauss points and restriction
   from (C) to its star.

5. **The ambient object must have codimension zero.**  The single tensor
   (G_0) is supplied specifically by the full-ambient superform with
   continuous piecewise-smooth coefficients in GK Definition 9.9(ii).  It
   does not follow from an arbitrary PS form on a lower-dimensional support
   or from a higher-codimension delta-preform.

6. **Specialization is not evaluation at the Gauss point.**  One must find a
   rational fibre point inside the neighbourhood on which the
   \(\mathbf R\)-linear identity holds, lift its coordinates to analytic unit
   germs, and pull the identity back along the resulting local section.

7. **The field hypotheses are used essentially.**  Density of
   (N\otimes\Gamma), existence of the required rational-radius Gauss point,
   and rational points in the relevant reduction open all use the stated
   hypotheses.  With a non-dense value group, non-rational (w), or a finite
   residue field for the completed residue field, the proof requires a base
   extension or a different argument.

8. **The conclusion must not be overstated.**  The proof gives
   \(\mathbf R\)-linearity and hence CLD-smoothness of each component.  It
   does not, without an additional integrality argument, give a representation
   of each component as the logarithm of one analytic unit in the sense of a
   smooth tropicalization map with no outer smooth function.

9. **Nondegeneracy and symmetry of the quadratic part are indispensable.**
   Only coordinates in \(\operatorname{im}(q^\sharp)\) are detected by the
   contraction.  For degenerate (q), the claimed conclusion for all
   coordinates is false in this level of generality.  The Hessian sees the
   symmetric part of the quadratic form, so that part must be nondegenerate.

## Hostile conclusion

Subject to the nine repairs above, the product--Gauss proof has a coherent
local topology, an ordinary algebraic common chart, a valid star-lineality
argument, and a valid descent from the Gauss fibre to the original germ.  The
old residue-class identification is not needed.  The resulting theorem is a
credible candidate for independent and production Rethlas verification, but
it must remain isolated until that verification succeeds.
