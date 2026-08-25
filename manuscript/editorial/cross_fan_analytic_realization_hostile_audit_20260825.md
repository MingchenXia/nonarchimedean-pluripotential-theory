# Hostile audit: cross-fan analytic realization candidate

Date: 2026-08-25

Audited objects:

- manuscript/editorial/rethlas_packets_20260824/ch69_cross_fan_analytic_specialized_blueprint.md;
- manuscript/editorial/solver_dossiers_20260824/cross_fan_analytic_realization_candidate.md;
- the frozen candidate statement, proof, and dependency record;
- the live formulations P21.1 and P21.2 and the displayed cross-fan counterexample;
- the live CLD/Gubler--Rabinoff conventions for harmonic tropicalizations, calibrated tropical cycles, currents, and psh functions.

No live chapter was edited. Nothing was transmitted externally. This is a scope and correctness audit, not a novelty assessment.

## Verdict

**FAIL as an exact affirmative solution of the full analytic-realization packet.**

**PASS for the narrower statement that the displayed weighted cross-fan calculation is the proper pushforward of a concrete noncompact analytic construction.**

The construction and its numerical factors are correct. The blocking issue is logical scope: the full unbounded cross cannot be the image of a harmonic tropicalization in the book's live sense, because that definition has a compact strict analytic domain. Moreover, the two analytic psh potentials do not have equal curvature currents upstairs; their equality appears only after applying the noninjective proper pushforward.

## Checks that pass

### 1. Analytic space and tropicalization

Let
\[
A=K[x^{\pm1},y^{\pm1}]/((x-1)(y-1)),\qquad
X=(\operatorname{Spec}A)^{\mathrm{an}}.
\]
Then
\[
X=Y_h\cup Y_v,\qquad
Y_h=V(y-1)^{\mathrm{an}},\qquad
Y_v=V(x-1)^{\mathrm{an}}.
\]
Each component is a closed analytic copy of \(\mathbf G_m^{\mathrm{an}}\); the two components meet at the single rigid point \(p=(1,1)\). Thus \(X\) is reduced, pure one-dimensional, good, strict, and boundaryless. The claimed good/strict status follows from the standard strict Laurent-affinoid exhaustion of each component and gluing at \(p\).

The map
\[
\tau:X\longrightarrow\mathbf R^2,\qquad
\tau(q)=(-\log|x(q)|,-\log|y(q)|)
\]
is a proper ordinary moment tropicalization. Its image is the whole cross
\[
\Sigma=(\mathbf R\times\{0\})\cup(\{0\}\times\mathbf R).
\]
On each component its nonconstant coordinate is locally the negative logarithm of an analytic unit, so the map is locally harmonic in the Gubler--Jell--Rabinoff sense.

For every finite radius \(\rho\), the compact strict domain \(X_\rho\) is a harmonic tropicalization in the live book definition, and its image is the truncated cross \(\Sigma_\rho\). These compact domains have four boundary endpoints. The full \(X\) is boundaryless but noncompact.

### 2. Weights and calibration

On each of the four primitive rays the lattice index, generic analytic degree, and residue degree are all one. Hence the fundamental cycle \([X]\) pushes forward to the cross with ray weight one.

For
\[
Z=2[Y_h]+[Y_v],\qquad T=\delta_Z,
\]
the induced ray weights, in the order \(+e_1,-e_1,+e_2,-e_2\), are
\[
(2,2,1,1).
\]
These are exactly the weights in the displayed tropical counterexample. There is no hidden ramification or lattice-index factor.

The current \(T\) is a strongly positive order-zero current. It is \(d'\)- and \(d''\)-closed: each irreducible component is a boundaryless analytic curve, and compactly supported test forms produce no endpoint contribution. This agrees with the CLD calibrated-integration and Stokes conventions.

### 3. Psh approximants and current factors

For \(\varepsilon_j\downarrow0\), set
\[
u_j(s,t)=2\sqrt{s^2+\varepsilon_j},\qquad
v_j(s,t)=\sqrt{s^2+\varepsilon_j}+\sqrt{t^2+\varepsilon_j}.
\]
These functions are smooth and convex, and decrease locally uniformly to
\[
u(s,t)=2|s|,\qquad v(s,t)=|s|+|t|.
\]
Their pullbacks by \(\tau\) are smooth psh functions. Their locally uniform limits
\[
U=u\circ\tau,\qquad V=v\circ\tau
\]
are continuous psh functions.

Let \(q_h\) and \(q_v\) be the unit Gauss points of \(Y_h\) and \(Y_v\). They are distinct points of \(X\), although
\[
\tau(q_h)=\tau(q_v)=0.
\]
With the manuscript's Lagerberg normalization,
\[
\frac{\mathrm d^2}{\mathrm ds^2}|s|=2\delta_0.
\]
Consequently the analytic current identities are
\[
\mathrm d'\mathrm d''[U]=4\delta_{q_h},
\]
\[
\mathrm d'\mathrm d''[V]
=2\delta_{q_h}+2\delta_{q_v},
\]
and
\[
\mathrm d'\mathrm d''\bigl((U-V)T\bigr)
=4\delta_{q_h}-2\delta_{q_v}.
\]
The signs and factors are correct. Near the node \(p\), both coordinate logarithms vanish, so no node atom occurs. At infinity there is no contribution because all test forms are compactly supported.

Proper pushforward gives
\[
\tau_*\mathrm d'\mathrm d''[U]
=\tau_*\mathrm d'\mathrm d''[V]
=4\delta_0
\]
and
\[
\tau_*\mathrm d'\mathrm d''\bigl((U-V)T\bigr)=2\delta_0.
\]
Equivalently, one should display the projection identities
\[
\tau_*T=T_\Sigma,\qquad
\tau_*\bigl((U-V)T\bigr)=(u-v)T_\Sigma,
\]
and then commute proper pushforward with \(\mathrm d'\mathrm d''\). This makes explicit that the pushed-forward calculation is precisely the displayed cross-fan calculation, with the same four rays, weights, potentials, and residual atom; it is not merely a one-ray or local surrogate.

## Blocking scope defects

### A. Literal P21.1 cannot have the proposed affirmative answer

The live definition of a harmonic tropicalization starts with a **compact strict analytic domain** \(W\). Its continuous image is compact. Therefore no harmonic tropicalization in that exact sense can have image equal to the unbounded cross \(\Sigma\).

The candidate uses the noncompact boundaryless space \(X\) for the full cross. This is a proper ordinary moment tropicalization that is locally harmonic, and it is exhausted by compact harmonic tropicalizations \(X_\rho\to\Sigma_\rho\). It is not itself a harmonic tropicalization under the live definition.

Thus literal P21.1 has a short negative answer by compactness. The candidate supplies a positive answer only after replacing the requested object by a noncompact ordinary/local-harmonic variant.

### B. The analytic curvatures are not equal upstairs

The external packet asks for analytic psh pullbacks for which the same current calculation holds. In the displayed tropical counterexample the premise is
\[
\mathrm d'\mathrm d''u=\mathrm d'\mathrm d''v.
\]
For the proposed analytic lifts one instead has
\[
\mathrm d'\mathrm d''[U]=4\delta_{q_h}
\ne
2\delta_{q_h}+2\delta_{q_v}
=\mathrm d'\mathrm d''[V].
\]
They become equal only because proper pushforward identifies \(q_h\) and \(q_v\).

Therefore the candidate is an analytic source whose pushforward realizes the tropical counterexample. It is not an analytic counterexample to an upstairs implication with the same equality hypothesis.

Changing the cycle coefficients cannot repair this defect: \(Z\) does not enter the unweighted premise \(\mathrm d'\mathrm d''[U]=\mathrm d'\mathrm d''[V]\).

### C. P21.2 is solved only in the standalone ordinary scope

The map \(\tau:X\to\Sigma\) does give a boundaryless, good, strict, pure one-dimensional analytic space with the desired full cross and weights. Hence P21.2 is affirmatively solved if it asks only for an ordinary moment tropicalization.

If P21.2 is read jointly with literal P21.1, requiring the same full unbounded image to arise from a compact-domain harmonic tropicalization, the joint request is impossible.

## Required repairs before promotion

1. **Split the conclusions.** Record literal P21.1 as negatively settled by compactness. State separately the positive noncompact ordinary/local-harmonic realization and its compact exhaustion.

2. **Narrow the promotion claim.** Say that the candidate analytically realizes the displayed tropical counterexample after proper pushforward. Do not call it an analytic counterexample with equal curvature currents upstairs.

3. **Retain an explicit unresolved atom if desired.** A stronger construction with distinct analytic psh functions satisfying
\[
\mathrm d'\mathrm d''[U]=\mathrm d'\mathrm d''[V]
\]
upstairs and still violating the weighted implication is not supplied by this candidate.

4. **Display the projection formula.** Include
\[
\tau_*T=T_\Sigma,\qquad
\tau_*((U-V)T)=(u-v)T_\Sigma
\]
before the final current calculation, together with properness of \(\tau\).

5. **Keep the status words exact.** Use “good, strict, boundaryless, noncompact ordinary moment tropicalization, locally harmonic, with compact harmonic truncations.” Do not abbreviate this to “harmonic tropicalization of the full cross.”

## Final classification

- Geometry, ray weights, calibration: **PASS**.
- Positivity and closedness of the analytic cycle current: **PASS**.
- Convex approximation and psh descent: **PASS**.
- Signs, factors, lack of node/infinity atoms: **PASS**.
- Exact reproduction of the displayed tropical counterexample after pushforward: **PASS**.
- Literal compact-domain harmonic realization of the full cross: **FAIL, impossible by compactness**.
- Equal analytic curvature currents upstairs: **FAIL, not established and false for the displayed lifts**.
- Promotion as the exact full-packet solution: **FAIL until the scope is repaired as above**.
