# Obstructions, deformation diagnostic, and source comparison

Date: 2026-08-31. Author: /root/p213_skeletal_hostile.
Companion to RESEARCH_NOTE.md. This file separates source theorems, the new model-specific argument, and the still-missing arbitrary-wall interface.

## 1. An actual nonisotrivial strictly semistable neighborhood

Let R=C[[pi]], K=C((pi)), and set

\[
 B=R[x,y,((x+2)(x+3))^{-1}]/(xy-\pi),\qquad
 \lambda=3+x.
\]

Over Spec(B), take the smooth projective Legendre elliptic curve

\[
                  Y^2 Z=X(X-Z)(X-\lambda Z).          \tag{1.1}
\]

Its discriminant is 16*lambda^2*(1-lambda)^2, a unit of B, so this is a smooth proper elliptic scheme over the base. The base is regular strictly semistable over R; smooth pullback preserves the local normal-crossing description. Thus its total space is a regular strictly semistable relative surface over R.

The two special-fibre components meet along the proper smooth curve C=E_3. Complete along the special fibre and take the ordinary tube of that intersection. Projection by x is a proper smooth family of elliptic curves over

\[
                        |\pi|<|x|<1.                 \tag{1.2}
\]

Indeed xy=pi and reduction to the intersection give exactly |x|,|y|<1. The inverted factors x+2 and x+3 have norm one throughout (1.2). Closed radial strips in this tube are compact because the elliptic family is proper over the corresponding compact closed annulus.

Nevertheless this family is not an analytic product over the given annular base, even after restricting to a nonempty radial subannulus. Its j-invariant is

\[
 j(x)=256\frac{(\lambda^2-\lambda+1)^3}
                    {\lambda^2(\lambda-1)^2},\qquad \lambda=3+x.
                                                               \tag{1.3}
\]

This is nonconstant: its logarithmic derivative with respect to lambda at lambda=3 is 10/21, and j(3)!=0. An isomorphism over the annulus with a fixed elliptic curve would make j constant. Thus local étale equations and the proper residual curve do not justify a product identification preserving the tangential annulus.

The model in this example is proper over Spec(B), not asserted proper over R. It is used here as a concrete diagnostic of the false splitting inference, not silently inserted into the proper-model hypothesis of the principal statement. Its compact-strip property follows by the separate proper-family argument just given. No claim is made that its total space cannot admit some unrelated presentation or fibration; the disproved inference is the product presentation over the stated analytic normal coordinate.

The new proof in RESEARCH_NOTE.md does not need such a presentation. A numerator reducing to w^r on C may contain genuine terms in the ideal (x,y). On normal radii bounded below, those terms have strictly smaller norm on a sufficiently outer w-collar. This is uniform domination, not formal or analytic linearization.

## 2. Component orders alone fail to give a residual unit

At the generic point of a normal-crossing curve, take two local component generators x_i,x_j. The element

\[
                        z=x_i(x_i+x_j)                \tag{2.1}
\]

has order one along E_i and order zero along the other selected generic components, just as x_i does. At a generic point of E_i, x_j is a unit, so x_i+x_j does not increase that component order; the same observation handles E_j.

But z/x_i=x_i+x_j lies in the maximal ideal of O_{𝒳,η_C}. It has zero reduction in k(C), and is not a local-ring unit. Its valuation along normal directions involves min(v(x_i),v(x_j)), with additional cancellation where the norms tie; it cannot be priced as the order of a nonzero residual rational function times v(w).

This is why prescribing the component-order vector is insufficient. The proof chooses z_i to generate O(-E_i) at η_C and F to be a unit of that same local ring. Those stronger choices ensure numerator and denominator have nonzero reductions modulo the ideal of C.

## 3. Fixed-moment balancing does not force all branch ratios

There is an actual smooth example, not merely a drawn fan. Over K=C((pi)), take a product of n-1 open annuli with the ordinary open subset of P^1_K obtained by deleting 0,infinity,1,2. Use the analytic moment whose coordinates are the annulus coordinates together with

\[
                         Z,\qquad (Z-1)/(Z-2).         \tag{3.1}
\]

Near the Gauss point of the P^1 factor, the four source directions toward 0,infinity,1,2 have normal tropical vectors

\[
                         (1,0),\ (-1,0),\ (0,1),\ (0,-1).
                                                               \tag{3.2}
\]

The remaining annular coordinates give a common (n-1)-dimensional tangential factor. In primitive coordinates the four canonical weights are one.

The single moment's tropical balancing equation admits every nonnegative vector

\[
                             (A,A,B,B).               \tag{3.3}
\]

Indeed the vector sum of weights times (3.2) is zero. It forces equality within each opposite pair but does not force A=B.

This is not an actual positive closed-current counterexample: it is a nonuniqueness example for the constraints supplied by that fixed moment. Further residual rational functions mix the four points, and the independently audited product argument rules out A!=B for the corresponding actual current coefficients. The example explains why the source/refinement issue cannot be replaced by an appeal to ordinary tropical balancing alone.

More generally, under a proper source-local moment model and adequate source isolation, closedness yields the standard balanced-normal relation. If its space of relations is one-dimensional, comparison with the positive canonical relation forces proportionality. That is a familiar conditional tropical-cycle argument, not a solution of the missing wall problem. Neither existence of the proper isolated source star nor uniqueness of its normal relation is automatic for an arbitrary analytic moment.

## 4. What GRW actually supplies

The primary source is Gubler--Rabinoff--Werner, “Skeletons and tropicalizations,” arXiv:1404.7044v3, 28 February 2016.

Its standing field in Section 1.1 is complete, algebraically closed, and nontrivially valued. Section 3.1 concerns a proper strictly semistable pair. Section 3.2 explains base change from a complete DVR model. These hypotheses are not silently replaced by arbitrary good boundaryless analytic spaces.

For a codimension-one canonical face, Section 6.4 uses the proper curve given by the closure of its one-dimensional vertical stratum. The alpha-coefficients are intersection degrees of component line bundles restricted to that curve; some may be negative. Definitions 6.7.1 and 6.7.2 therefore include correction terms involving values or derivatives tangential to the face. They are not simply the uncorrected order along an arbitrarily chosen transverse direction. In dimensions greater than one the resulting slopes need not be integers.

Theorem 6.9 treats a rational function whose divisor is supported in the chosen horizontal boundary. The proof at (6.10.2)--(6.10.6) uses the degree-zero intersection of its PRINCIPAL CARTIER DIVISOR with the proper residual curve. It computes canonical intersection degrees and then rearranges those degrees into the stated slope formula.

That argument does not define an arbitrary-current functional λ_T, does not justify multiplying each local order by an unknown current coefficient, and does not construct a compact primitive for T. Replacing its intersection coefficients by b_T(p) before proving (2.4) of the principal note would assume exactly the missing statement.

Our proof instead uses local-ring UNIT lifts F of residual rational functions, and proves their b_T-weighted principal relation by closedness on the original analytic source. Its auxiliary normal generators z_i need not be residual units as sections of a globally trivial bundle: the orders n_{i,p} encode their normal-line-bundle twisting and need not sum to zero in degree. They enter determinant-one shears and the compact-support budget, not a false relation λ_T(sum n_{i,p}p)=0. No GRW curvature term is declared zero.

The source's Section 4.14 and Proposition 4.15 analyze actual formal fibres and a torus over a zero-dimensional stratum. The original-field completed-tube argument in the principal note explicitly adds the finite unramified coefficient extension R_p and its degree; it does not cite the algebraically closed statement as if residue degrees disappeared.

## 5. Why the two tempting CLD reductions do not finish an arbitrary wall

### 5.1 Calibrated residual cones are not a current-restriction theorem

CLD Theorem14.6.2, printed p.412, assumes an algebraically closed complete base, a boundaryless generically quasi-smooth n-dimensional germ with d_k(x)=n, and analytic functions of norm ONE at x. It compares tropical dimensions with the corresponding ordinary residual functions. Equality of the CANONICAL calibrated cones is asserted when those dimensions are n.

A codimension-one polyhedral wall does not by itself make the ordinary residue field a curve function field. Already on an annulus^{n-1} times a good-reduction curve:

- at a normal-radius point whose n-1 valuations are rationally independent modulo the base value group, the ordinary residue transcendence degree is one and the normal rank is n-1; norm-one functions have residual transcendence degree at most one, so the theorem's full-n comparison condition is unavailable;
- after normalizing rational radii over a suitable coefficient extension, the normal residual torus contributes n-1 further independent residual variables, so the ordinary residue field has transcendence degree n, not one.

Extracting the proper residual CURVE from either description requires additional geometry. Passing to the completed field of a tangential Gauss point may exhibit an analytic curve fibre, but the source theorem does not restrict an arbitrary (0,0)-current T to that fibre. Such a restriction would be a new operation requiring definition, existence, positivity, closedness, and compatibility with source coefficients.

The principal note avoids this operation because an actual model already supplies the residual curve C and completed p-tubes in the original n-dimensional space.

### 5.2 Variation of canonical calibrations is not variation of unknown weights

CLD Theorem14.7.2, printed pp.418--420, has a compact source satisfying (S_d), a regular base, pure relative dimension, and a RIGID reference point. It proves local constancy of canonically calibrated fibre tropicalizations and a product description of a CANONICAL calibrated tropical image near the corresponding coordinate boundary.

Its proof uses finite-flat degrees. It neither identifies an analytic neighborhood with a product nor transports arbitrary T-coefficients between fibres. A non-rigid tangential Gauss point is not the stated rigid reference point. Even when its hypotheses can be arranged after extra geometric work, a canonical degree equality is not a comparison of arbitrary closed-current weights.

Thus neither theorem licenses slicing T, or replacing an actual source cutoff by a formal Zariski cutoff, or inferring common source sheets from a common target cone.

## 6. Exact remaining interface

The principal note proves a residual divisor-functional relation on the tube of C in an ACTUAL proper regular strictly semistable DVR model. The gain over the product/torsor packets is that nonlinear deformation terms and higher-dimensional normal directions are handled without identifying the entire neighborhood with a split model.

To obtain the originally requested assertion for a general actual analytic tropical moment, at least the following still require proof in that setting:

1. suitable proper residual-curve geometry on the original source, or a replacement construction with the same compactness and unit-lift properties;
2. comparison of the current's source cells with the displayed residual collars, with correct residue and lattice factors and no aggregation of distinct source sheets;
3. a genuine source-form bridge for every refinement used to transfer a known ratio;
4. access to all the relevant full-dimensional source cells, not just this one model wall.

R is explicitly assumed wherever source-cell interpretation is made. The new proof of the displayed collar functional itself does not use R. These boundaries are part of the result, not deferred claims of full P21.3.

