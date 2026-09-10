# P02.1 invariant split-toric semipositive real-PL regularization

Status: source-scoped positive companion result.  It constructs decreasing
semipositive real-PL approximants only for finite continuous
maximal-compact-torus-invariant current-psh functions on one ordinary convex chamber
and on a displayed good strictly analytic subdomain.  It does not identify
arbitrary classical psh functions with that class and does not retire P02.1.

## Claim-to-source map

| Step | Source / direct argument | Scope control |
| --- | --- | --- |
| Invariant finite continuous psh potentials descend to finite convex tropical potentials | BGJKK25, Theorem 5.3.11 | The argument starts with the invariant current-psh class, not every classically psh function. |
| Decreasing smooth convex potentials exist on an interior ball | The book's \(\Cref{prop:ch09-radial-mollification}\) | The ball is compactly contained in the dense open convex chamber. |
| Each smooth convex potential has a finite real-polyhedral upper approximation | Direct finite tangent-plane compactness argument | The positive additive gaps \(2^{-j}\) enforce monotonicity between successive polyhedral approximants. |
| Tropical pullbacks of the polyhedral potentials are semipositive real PL | BGJKK25, Theorem 5.3.11; \(\Cref{thm:cld-to-classical-psh}\); and \(\Cref{thm:gr-pl-comparison}\) | Convexity first gives CLD-psh, hence classical psh; the real-PL comparison then needs only that the displayed domain be good and strictly analytic. |

Primary source: J. I. Burgos Gil, W. Gubler, P. Jell, and K. Künnemann,
Pluripotential theory for tropical toric varieties and non-Archimedean
Monge--Ampère equations, Kyoto J. Math. 65 (2025),
doi:10.1215/21562261-2024-0010.

https://gubler.app.uni-regensburg.de/Publikationen/2102.07392.pdf

## Deliberate boundaries

1. The result concerns finite continuous invariant psh functions, not
   arbitrary classically psh functions.
2. It is local on an ordinary Euclidean ball in the dense torus chamber; it
   makes no toric-boundary or nonconvex-domain assertion.
3. The good strictly analytic real-PL comparison hypotheses are part of the
   statement; they are not inferred for an arbitrary toric domain.
4. No local-Fubini--Study, weakly smooth, or ordinary CLD-smooth conclusion
   follows from these real-PL approximants.
