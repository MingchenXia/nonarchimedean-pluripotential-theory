# Dossier: finite-energy equations on polarized affine cones

Date: 23 August 2026.  Source-audit and solver packet for
`prob:frontier-affine-cone-ma`.  No Rethlas launch or verification receipt
exists.  The configured production account reported that its cap will reset
on 27 August 2026.

## Exact framework

Let (k) be algebraically closed and trivially valued of characteristic
zero.  Let ((X=\operatorname{Spec}R,T;\xi)) be a normal affine (T)-variety
with a good action and Reeb field (\xi).  Write

\[
 X_0=\{v\in X^{\mathrm{an}}:v(\mathfrak m)=0\}.
\]

The target problem is the conjunction of two source-stated residuals:

1. construct a quantitative comparison/addition calculus between
   (\operatorname{PSH}(\xi)) and (\operatorname{PSH}(\xi')) for
   nonproportional Reeb fields;
2. characterize the image of
   \[
   \operatorname{MA}_\xi:\mathcal E^1(\xi)/\mathbf R
      \longrightarrow\mathcal M^1(\xi)
   \]
   and solve (\operatorname{MA}_\xi(\varphi)=\mu) precisely for measures
   in that image.

The packet must not silently replace “characterize the image” by
surjectivity.  Surjectivity onto all of (\mathcal M^1(\xi)) is not a source
theorem.

## Established inputs

From Wu, arXiv:2406.13684v1:

- Proposition 3.3 gives only the proportional-ray rules
  \[
  a\varphi\in\operatorname{CPSH}(a^{-1}\xi),\qquad
  \varphi\in\operatorname{CPSH}(a\xi),\quad
  \psi\in\operatorname{CPSH}(b\xi)
  \Longrightarrow
  \varphi+\psi\in
  \operatorname{CPSH}\!\left(\frac{ab}{a+b}\xi\right).
  \]
- Theorem 1.1 and Theorem 6.3 extend the mixed Monge--Ampère operator to
  finite-energy inputs and prove the decreasing continuity needed in the
  book.
- Corollary 7.8 makes the single-potential operator bi-Lipschitz onto its
  image for the quasi-pseudometrics (I) and (I^\vee).
- Corollary 6.6(4) recovers the global Boucksom--Jonsson finite-energy class
  and energy when (\xi) is rational.  It is not an identification of the
  entire global theory and does not settle the affine-cone image problem.
- The introduction identifies uniform differentiability and comparison of
  nonproportional Reeb fields as the missing input for a full variational
  solution.

From Wu, arXiv:2106.13395 / *Math. Z.* 301 (2022):

- Lemma 5.11 embeds the rational quotient analytification into the invariant
  link;
- Proposition 5.13 gives the unnormalized projective/shell product identity;
- Corollary 5.14 compares Fubini--Study energies.

The normalized probability-measure identity includes the common factor
(1/\operatorname{vol}(\xi)=1/\operatorname{vol}(L)).

## Boundary tests that every proposed proof must pass

1. **Equivariance.** Adding two (\xi)-equivariant functions changes the
   equivariance weight.  Any fixed-polarization addition formula that ignores
   this is ill-typed.
2. **Nonproportionality.** Proposition 3.3 cannot be iterated to compare two
   genuinely different Reeb rays.
3. **Irrational support.** The Monge--Ampère image of a divisorial norm can be
   carried by a genuinely quasimonomial point.  A divisorial-only compactness
   argument is insufficient.
4. **Uniformity.** Rational approximation (\xi_j\to\xi) is useful only if
   the Hodge-index, (I\)--(J), and first-variation constants remain uniform
   on a compact Reeb slice.
5. **Constants.** The source and target are quotiented by constants; any
   claimed injectivity must be stated on
   (\mathcal E^1(\xi)/\mathbf R).
6. **Image versus codomain.** Bi-Lipschitz onto the image neither proves that
   the image is closed nor that it equals (\mathcal M^1(\xi)).

## Candidate route for the production solver

The production prompt should ask for the following sequence, stopping at the
first unproved implication.

1. Fix a compact convex slice (K) of the Reeb cone bounded away from its
   boundary.  Establish a common finite family of homogeneous generators and
   compare their (\xi)-weights uniformly for (\xi\in K).
2. Use those comparisons to build typed transport maps between continuous
   psh classes for nearby Reeb fields.  Quantify the error on (X_0); do not
   claim that the transported function is psh until a finite-max or closure
   proof is supplied.
3. Prove, or find a counterexample to, Reeb-uniform integration by parts,
   local Hodge-index, and (I\)--(J) inequalities on bounded energy sets.
4. If Step 3 succeeds, prove uniform differentiability of
   (t\mapsto E_{\xi_t}(\varphi_t)) along rational approximants.
5. Run the variational functional
   \[
   F_\mu(\varphi)=E_\xi(\varphi)-\int_{X_0}\varphi\,\mathrm d\mu
   \]
   on a normalized energy sublevel.  Verify compactness, upper
   semicontinuity, and the Euler--Lagrange implication separately.
6. Characterize the resulting image intrinsically.  If surjectivity fails,
   produce a finite-energy measure outside the image and identify the exact
   violated condition.

## Rejected shortcuts

- Passing to a rational projective quotient does not treat irrational Reeb
  fields and gives no uniform comparison for two nonproportional rational
  fields.
- Stone--Weierstrass density of differences of continuous psh functions
  separates measures but does not imply that every finite-energy measure is
  Monge--Ampère.
- The bi-Lipschitz estimate does not provide existence of a preimage.
- The global Boucksom--Jonsson variational theorem cannot be imported without
  proving that its compactness, envelope, and differentiability hypotheses
  descend to the affine-cone shell.

## Promotion boundary

No statement beyond the established inputs may be promoted until the exact
framework and proof receive a production `gpt-5.6-sol` / `xhigh` Rethlas
receipt and a separate post-integration source audit.  Until then the two
residuals remain coupled and open.
