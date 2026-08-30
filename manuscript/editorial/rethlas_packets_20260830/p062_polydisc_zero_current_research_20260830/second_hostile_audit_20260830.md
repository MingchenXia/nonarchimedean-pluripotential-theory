# P06.2 strict-polydisc zero-current candidate: second hostile audit

**Date:** 2026-08-30  
**Verdict:** **PASS**  
**Statement SHA-256:** `017f3da108ae737e4bbc1d490d6988faf76ce643b4cb52104aae53c4dcda75d6`  
**Proof SHA-256:** `3763bf9a7e4b1f47602544ad2c3248d9b8abd7b9d34109e3c14259e422393bbd`

This is an independent, from-scratch audit of the exact frozen bytes above. I did not open or use the first hostile-audit report. I made no change to the statement, proof, or live book, and did not call Rethlas.

## Bottom line

I found no counterexample and no hidden mathematical gap in the proposed implication
\[
        d'd''[h]=0 \quad\Longrightarrow\quad h\text{ is constant}
\]
on either the strict open polydisc or the closed polydisc with the current equation imposed on its analytic interior. The delicate step is not a positivity argument: it is the identity of **signed Radon measures** attached to a pulled-back top form. The cited torus support and calibrated-integration results do support that identity, including for sign-changing coefficients and an arbitrary continuous multiplier after the measure identity has been established.

There are two bibliographic improvements, neither affecting correctness:

1. The closed-polydisc paragraph should cite Berkovich Proposition 1.5.5 **(i) and (ii)**, since (ii) is the composition statement actually used.
2. If the editorial source ledger points to older CLD section numbers for signed Radon measures and currents, it should be synchronized with the edition ultimately cited. The relevant material in the inspected newer source is in Sections 5.8--5.10 and 7.1, 7.7.

## Hostile checks

### 1. CLD current restriction and test form

For a compactly supported \((n-1,n-1)\)-form \(\beta\) on the tropical orthant, split-torus tropicalization is proper, so \(F_a^*\beta\) has compact support on the punctured torus domain. Restricting a current to that open domain is defined by extension by zero of compactly supported test forms. The CLD definitions also give
\[
 \langle d'd''[h],F_a^*\beta\rangle
   =\langle[h],d'd''F_a^*\beta\rangle
   =\int h\,F_a^*(d'd''\beta),
\]
with the convention-compatible sign (and any global sign would in any event be immaterial to vanishing). Thus the proof neither pulls back the current \([h]\) nor assumes smoothness of \(h\).

Direct checks: CLD's current restriction is defined using \(j_!\), extension by zero; restriction commutes with \(d'\) and \(d''\); and the displayed double-differential pairing has the asserted sign. In the inspected source these occur in Proposition 6.4.5 and Sections 7.1 and 7.7.

### 2. Support of a sign-changing torus top form

BGJKK Proposition 2.3.6 applies to an arbitrary \((p,q)\)-form with \(\max(p,q)=n\), not merely to a positive form. It gives the exact support on the canonical torus skeleton; the proof needs only the weaker inclusion
\[
 \operatorname{supp}(F_a^*\alpha)_{\rm Rad}
 \subseteq \iota_a(\operatorname{supp}\alpha).
\]
Consequently a coefficient \(q\) of changing sign in \(\alpha=d'd''\beta\) creates no off-skeleton mass and no cancellation-based loophole.

Direct source check: `/private/tmp/bgjk2102.07392-src/bgjk.tex`, Proposition `lem: support on skeleton`, source lines 1010--1051 (published Proposition 2.3.6).

### 3. Signed Radon pushforward and continuous multiplier

The top-degree form \(F_a^*\alpha\) defines a finite signed Radon measure on the compact set over \(\operatorname{supp}\alpha\). GJR Proposition 11.1 and Example 11.7 give, on the split torus with lattice multiplicity one, equality against compactly supported smooth multipliers. This statement is linear; it does not require \(q\geq0\).

Smooth compactly supported functions are uniformly dense on the common compact support. Equality on them therefore implies, by uniqueness for finite signed Radon measures,
\[
             (F_a)_*\mu_\alpha=\alpha_{\rm Rad}.
\]
The BGJKK support result puts \(\mu_\alpha\) on the Gauss section, and \(F_a\) is a homeomorphism there with inverse \(\iota_a\). Hence
\[
             \mu_\alpha=(\iota_a)_*\alpha_{\rm Rad}.
\]
This last conclusion is valid for signed measures: pushforward by a homeomorphism is injective on finite signed Radon measures. It follows immediately that one may integrate the arbitrary continuous function \(h\):
\[
 \int h\,d\mu_\alpha
   =\int h(\iota_a(u))\,d\alpha_{\rm Rad}(u).
\]
No positivity, monotone convergence, Cartesian-product factorization, approximation of \(h\), or pullback of \([h]\) is being smuggled in.

Direct source checks: `/private/tmp/gjr211105741v3/harmonictrop.tex`, Proposition 11.1 and Example 11.7; `/private/tmp/cld1204.6277v2-src/calibrage.tex` for the signed Radon measure of a top form; and `/private/tmp/cld1204.6277v2-src/app-mesure.tex` for uniqueness and proper pushforward of signed Radon measures. BGJKK also writes the same continuous-multiplier skeleton formula explicitly at `/private/tmp/bgjk2102.07392-src/bgjk.tex`, source lines 2709--2717.

The `partially-integrated-psh-distinguished-boundary-mass` audit mechanism was checked and deliberately not invoked: its positivity hypothesis is absent here because \(d'd''\beta\) is signed. This candidate correctly uses the signed-measure route instead.

### 4. From all tests to the distributional Hessian

The test \(\beta\) is arbitrary of bidegree \((n-1,n-1)\). Therefore
\[
 \int_{\Omega_\rho}\tau_{a,\rho}\,d'd''\beta=0
\]
is exactly \(d'd''[\tau_{a,\rho}]=0\), equivalently the vanishing of every distributional second partial \(\partial_i\partial_j\tau\). On the connected convex orthant, mollification on relatively compact balls makes each regularization affine; compatibility on overlaps and continuity of \(\tau\) yield one global affine function. There is no missing first-order or skew component.

### 5. Coordinate-stratum limits kill every affine slope

With all other radii fixed and \(r_i=e^{-u_i}\to0\), the Gauss seminorm
\[
 \max_\nu |c_\nu|r^\nu
\]
converges on polynomials to the seminorm obtained by retaining only terms with \(\nu_i=0\), namely the Gauss point on \(T_i=a_i\). To pass from polynomials to analytic functions, all points can be placed in a single strict closed subpolydisc and polynomial uniform approximation used there. Such a containing strict radius exists because an algebraically closed nontrivially valued field has divisible, hence dense, value group in logarithmic coordinates. The limiting coordinate-stratum point remains in the relevant open or closed polydisc.

Continuity of \(h\) therefore gives a finite limit as \(u_i\to\infty\). An affine trace can have such a limit only when its \(u_i\)-slope is zero. Repeating for every coordinate kills all slopes; sending all radii to zero then gives \(h(\eta_{a,r})=h(a)\).

### 6. Translation equality

If \(|a_i-b_i|\le r_i\), the two multivariate Gauss norms coincide. Expanding \((T-a)^\nu\) in powers of \((T-b)\), the ultrametric inequality gives one norm inequality; interchanging \(a,b\) gives the reverse inequality. Thus \(\eta_{a,r}=\eta_{b,r}\). The choices of \(r_i<\rho_i<R_i\) in the open case are possible because \(|a_i-b_i|<R_i\). In the closed case equality with \(R_i\) is handled by the already established limiting extension to radii \(r_i=R_i\). There is no uncovered boundary-distance case.

### 7. Density and non-Abhyankar points

Strict closed polydiscs are strictly affinoid, rigid points are dense in them, and over algebraically closed \(K\) their rigid points are \(K\)-rational. The open polydisc is exhausted pointwise by strict closed subpolydiscs: for each point, choose value-group radii strictly between its coordinate seminorms and \(R_i\). Hence constancy on \(K\)-points plus continuity reaches every Berkovich point, including non-Abhyankar points. This avoids the false assertion that every point lies on a moment skeleton.

The original Berkovich book was not locally packaged for direct inspection. The use of its density theorem is independently corroborated in `/private/tmp/gr2506.13548v2-src/harmonicity.tex`, source lines 1150--1154, which invokes Berkovich Proposition 2.1.15 precisely as density of rigid points in a strictly affinoid space. This is a source-packaging caveat, not a mathematical defect.

### 8. Closed-polydisc analytic interior

For any boundary or interior centre \(a\) and \(\rho_i<R_i\),
\[
 A_{a,\rho}=\{0<|T_i-a_i|<\rho_i\ \forall i\}
\]
is an ambient open analytic subspace and the ultrametric inequality places it in \(D^+_{\mathbf R}\). It is therefore contained in the topological interior of that analytic domain. Berkovich Proposition 1.5.5(i) identifies this with the relative analytic interior. Proposition 1.5.5(ii), together with the boundarylessness of analytic affine space, puts it in the absolute analytic interior on which the current is assumed zero. Thus the test-form argument is available even for centres whose coordinates have modulus \(R_i\).

Direct source check: Berkovich, *Etale cohomology for non-Archimedean analytic spaces*, Proposition 1.5.5(i)--(ii), `/private/tmp/berkovich_etale_1993.txt`, lines 1300--1322. The proof text cites (i) and explicitly invokes the composition formula; adding “(ii)” would only make the citation exact.

### 9. Consequences and attempted counterexamples

Once \(h\) is constant, weak smoothness, vanishing weakly smooth Hessian, GJR harmonicity, and classical pluriharmonicity are immediate. GJR Proposition 10.17 confirms the weakly-smooth/harmonic equivalence. Constants and their negatives remain harmonic after scalar extension and pullback to every analytic curve.

Standard would-be counterexamples do not survive the hypotheses: \(\log|T_i-a_i|\) is singular at its divisor; truncated radial functions have a nonzero corner current; and changing values only away from the Gauss skeleton is impossible after translation equality and density plus continuity.

## Final determination

**PASS.** The frozen statement and proof are mathematically sound under their stated hypotheses. The two citation refinements above are editorial only and do not require altering the theorem or proof logic. The argument would fail if one removed continuity of \(h\), properness/compact support in the tropical test, the top-form skeleton support theorem, or the signed Radon pushforward identity; none of those ingredients is missing here.
