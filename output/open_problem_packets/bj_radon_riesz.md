# The Boucksom--Jonsson Radon--Riesz problem

Work over an algebraically closed trivially valued field. Let \(X\) be an
irreducible projective variety, fix an ample numerical class \(\omega\), let
\(X^{\mathrm{lin}}\) be the linear-growth valuation space, let the weak
topology be the topology inherited from \(X^{\mathrm{an}}\), and let the
strong topology be the metric topology of
\(d_{\infty,\omega}\).  Normalize
\[
 T_\omega(v)=\sup_{\varphi\in\operatorname{PSH}(\omega)}
       \bigl(\sup_X\varphi-\varphi(v)\bigr)
      =d_{\infty,\omega}(v,v_{\mathrm{triv}}).
\]

Address Boucksom--Jonsson Question 11.16 in its exact published form: for an
arbitrary net \((v_i)\) in \(X^{\mathrm{lin}}\), is
\[
 v_i\longrightarrow v\text{ strongly}
 \quad\Longleftrightarrow\quad
 v_i\longrightarrow v\text{ weakly and }
 T_\omega(v_i)\longrightarrow T_\omega(v)?
\]
Corollary 11.15 proves this characterization with
\(E_\omega^\vee(\delta_v)\) in place of \(T_\omega(v)\); Question 11.16 asks
whether \(T_\omega\) can replace that energy.  Do not conflate the two
quantities merely because Proposition 11.1 only proves the comparison
\[
 \frac{1}{n+1}T_\omega(v)\leq E_\omega^\vee(\delta_v)
 \leq\frac{n}{n+1}T_\omega(v).
\]

Known positive locus: on a fixed snc dual complex for smooth projective
\(X\) in characteristic zero, BJ Appendix A, Theorem A.4 gives
equi-Lipschitz continuity of all psh restrictions and strong compactness;
compact-to-Hausdorff comparison then identifies the weak and strong
topologies on that one complex.

Try:

1. exhaustion by dual complexes plus quantitative control uniform in the
   model;
2. Izumi-type inequalities and normalized retractions;
3. reduction to divisorial valuations and Dini/compactness;
4. an abstract convex-analytic Radon--Riesz principle;
5. counterexamples from escaping models or increasingly thin exceptional
   divisors.

Also determine whether the fixed-dual-complex statement extends to arbitrary
characteristic without resolution. Separate the global question from the
fixed-complex theorem. Do not infer global compactness from finite
dimensionality of each individual complex.
