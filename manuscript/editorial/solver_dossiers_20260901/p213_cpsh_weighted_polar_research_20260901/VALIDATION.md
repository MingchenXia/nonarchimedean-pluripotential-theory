# Author validation and exact scope

Date: 1 September 2026. This is AUTHOR self-check, not independent acceptance.
The complete final research note and the source ledger were read before manifest generation.

## Mathematical checks

1. Scope: n>=1; 0<=m<=n; original complete K may be trivially valued. Abstract X is locally differentially separated so positive currents and compact test majorants have the stated measure interpretation. Analytic good separated X satisfies this hypothesis. The local sublevel assumption is explicitly proved for the analytic setting.
2. CPsh closure: smooth convex nondecreasing composition, addition and scaling are obtained by the minimal subsheaf property. Positive squares use a global convex increasing extension after a common shift. No claim of one smooth sequence for an arbitrary CPsh function is used.
3. Products and order: h^2=2f^2+2g^2-(f+g)^2 and polarization give dpsh products. Every derivative and multiplier in Gamma is a finite sum of positive-current terms. The continuity proof uses fixed CPsh decompositions and CLD 8.5.1, not the pending weighted estimate.
4. Positivity: the u and v closures are separate and are local sheaf assertions. Once Gamma is positive, the exponential identities transfer by the same closure. Smooth rho is locally dpsh by 8.8.1.
5. Schwarz: one common Radon–Nikodym dominating measure for three energies and all rational parameters gives a common null exceptional set. The pointwise quadratic discriminant supplies the weighted Young bound. This is not a claimed first-order smoothness theorem.
6. Compact support: K_delta is one common compact; u_j, V and their required smooth coefficients are defined near it. Powers of exponent at least three converge in C2 under one-variable convolution. At rho=0 the limiting beta coefficients and the displayed weighted terms vanish. Derivatives of V_p are never required to be uniform in p.
7. Both endpoints: at k=n, beta_n has only one summand, so b_n=1; at k<n b_k=2. The bracket has coefficients (2l,2l(l+1)) in the two-summand case and (l,l) at k=n. Both are bounded by c_k beta_(k-1). The case n=1 is entirely the one-summand endpoint, covered by this computation. k=0 is the identity estimate.
8. Sign and cancellation: the compact IBP identity has +2 V d'(zS) wedge d''beta; its cross term is 2 b_k l(-V)r^(l-1)Gamma(z,rho). The nonpositive ddV term is dropped in the correct direction. The Young energy has coefficient ONE, identical to the energy lower bound from the exponential identity, so it cancels. The bound u>=-M is asserted only on U.
9. Zero norm: if M=0, u=0 on U, so locality gives zero curvature there; beta is zero elsewhere. No division by zero in B=1/(2M) is used.
10. Limits: first prove the nonsmooth CPsh estimate for each FIXED smooth polar truncation V_p, including C2 coefficient passage. Then use a single canonical L1 bound and monotone convergence in p. No null-set property is transferred by weak convergence alone.
11. Trace: remove the antisymmetric part, dominate the symmetric part in an ordinary tropical chart by +/-C(ddv)^(n-m), then pull the inequality back. No rank assumption is inserted. m=0 is included by the auxiliary smooth factors; m=n is multiplication by a locally bounded smooth scalar.
12. Analytic barrier: the rational neighbourhood W sits in Int(A), and nested compactness supplies W_mu still inside. The denominator has no zero there. A constant branch makes the regularized maximum smooth even where all numerator functions vanish. The positive closed sublevel is contained in one compact W_mu within the original ordinary open.
13. Analytic poles: prime avoidance avoids every top-dimensional component, including nonreduced generic multiplicities. CLD 15.2.1(b) places each compact top-form support away from the zero set. The explicit smooth max truncations are stage-one decreasing, including at the poles.
14. Exclusions: no discontinuous factors, no arbitrary-positive-current polar estimate, no field-change pullback, no representation/classification hypothesis in the proof, and no all-bidegree P21.3 retirement.

## Prefreeze changes after root's earlier full read

- Repaired the substantive k=n factor-two error using b_k and an explicit two-case bracket estimate; root identified the error.
- Derived square/exponential CPsh membership directly from minimality, avoiding an unnecessary appeal to 8.1.11.
- Restricted the exponential lower bound to U, where its scalar bound is valid.
- Made local differential separation and the numerical ranges explicit, cited the smooth-rho dpsh input, and covered m=n scalar alpha.
- Made the log pole's stage-one approximation and the symmetric trace part explicit.

No frozen predecessor was edited. A fresh exact-final mathematical reviewer must assess this proof; this document and the hash checker do not provide that independent review.

## Byte validation

Run the read-only check_packet.mjs with the bundled Node runtime. It verifies all manifest entries, external input pins, checksum rows, expected record counts, and scans authored text for forbidden control characters. It does not execute mathematical proofs or write files. A successful run is an identity/consistency check only.

