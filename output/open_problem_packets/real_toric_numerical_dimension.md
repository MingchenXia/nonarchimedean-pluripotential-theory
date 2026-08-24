# Real transcendental toric numerical dimension

Let \(X\) be a smooth projective toric variety and let \(T\) be a
torus-invariant positive current in a big real \((1,1)\)-class. Let
\(\Delta(T)\) be its compact Newton body, with affine dimension taken in the
ambient character space and Euclidean volume normalized by the character
lattice whenever lattice counting is used.  Use Cao's cohomological product
from Definition 3, formed from the absolutely continuous parts of
quasi-equisingular approximants, and set
\[
 \nu_{\mathrm{Cao}}(T):=
 \max\{q\in\{0,\ldots,n\}:\langle T^q\rangle_{\mathrm{Cao}}\ne0\}.
\]
When \(T=(\mathrm i/2\pi)\Theta_\varphi(L)\) comes from a
pseudoeffective metric pair, this is the same nonvanishing invariant as
Cao's \(\operatorname{nd}(L,\varphi)\) in Definition 4 (the harmless constant
normalization does not affect nonvanishing).  The intended rational
line-bundle baseline is
\[
                     \nu_{\mathrm{Cao}}(T)=\dim\Delta(T)
\]
via the toric multiplier-ideal criterion, asymptotic lattice counting, and
Cao's projective numerical criterion.  Audit and prove that baseline as part
of the solution: neither supplied source states this global toric identity
verbatim.  Guenancia Theorem 1.13 gives the local monomial criterion
\(z^\alpha\in\mathcal I(\varphi)\) exactly when \(\alpha+\mathbf1\) lies in
the interior of the local Newton body, while Cao Proposition 4.4 is a
projective line-bundle section-growth criterion.  Passing between them still
requires global toric gluing and normalized lattice asymptotics.

Determine whether the identity extends to arbitrary real transcendental toric
classes. The proof must address that Cao's section-growth criterion is stated
in Proposition 4.4 for line bundles and multiplier ideals, so the existing
rational proof cannot simply be repeated: rational approximation varies the
cohomology class and the graded section algebra.

Try:

1. continuity of Cao's positive products under rational class approximation;
2. a purely convex characterization of numerical dimension for invariant
   currents;
3. approximation of Newton bodies with uniform control of singularity type;
4. reduction to the dimension of the affine span via mixed positive
   intersection products.

Test irrational nef classes, real big non-nef classes, lower-dimensional
Newton bodies, and changes of toric compactification. Keep lattice
normalization and the \(n!\) convention explicit. If the exact Cao invariant
is compared with another transcendental numerical dimension, first prove that
the two definitions agree; do not redefine Cao's already analytic invariant
through a nonexistent real section algebra.
