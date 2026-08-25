# Cross-fan analytic realization: production receipt

**Receipt date:** 25 August 2026 (Asia/Shanghai)

**Status:** verified frozen packet; live integration pending at receipt time.

**Verifier:** production Rethlas, gpt-5.6-sol, xhigh.

## Verdict

- Run: 20260825T021353Z_058a4390b0fb.
- Verification status and verdict: final/correct.
- Checked proof items: seven.
- Failed or blocked proof items: zero.
- Critical errors and gaps: zero.
- Proof SHA-256:
  4a68b379e8d043b6a62293496af981fca77371575474a8af0040d7b6b70a56fc.
- Aggregate context SHA-256:
  231cd9ff12723a7c64b9f70e4d574fccfcc709ab29c96433925e1d66cb15dbdd.
- Adaptive context SHA-256:
  ae1e5f7b6664fa373b4f249d45ace6eaf1b60b0edceb558aa62001f5dfebcb35.

The seven verified item identifiers are

1. pi_f8ecdfa8db447f454931ae43;
2. pi_1be1830d41202b6a77688bbf;
3. pi_bf41713d671e8c334a78fc22;
4. pi_8e3508b8e0856bdc73a21021;
5. pi_ebcadc24814cbca3d8a32319;
6. pi_0b9de1b9a02bda380bdc9708;
7. pi_145f93be3a26f3692441ccad.

The fifth item, the equality
\[
 \mathrm d'\mathrm d''[|-\log|T||]=2\delta_{\eta_0}
\]
against arbitrary compactly supported analytic test functions, initially
returned needs_context. Rethlas expanded the complete calibrated
integration/current dependency pi_bf41713d671e8c334a78fc22 and then
returned final/correct. The round-zero request for context and the
successful round-one verdict are both preserved.

## Frozen bytes

| Artifact | Bytes | SHA-256 |
|---|---:|---|
| ../rethlas_packets_20260824/ch69_cross_fan_analytic_specialized_blueprint.md | 28746 | 810de7cd399ddb522e510890c57b037cb844ba0e447960ec3b769f914b974b17 |
| decoded request statement | 2289 | 058a4390b0fba4e83d462b9b125a623d304390bb0ac64341134b1a8b5896058f |
| decoded request proof | 28720 | 4a68b379e8d043b6a62293496af981fca77371575474a8af0040d7b6b70a56fc |
| ../rethlas_packets_20260824/ch69_cross_fan_analytic_specialized_request_20260824.json | 33168 | 95f4a09ecf2d84f0500e7650e670fce469e0ca17bfc69542c1ded7ec4547cd7e |
| cross_fan_analytic_specialized_response_20260825.json | 2409 | 029b3e6020bccf019d9371b590566185681fe5c5b3b720ae6f4dc10ff025cbda |

The complete aggregate manifest and verification, every item-level
verification and log, and every process and child-process guard are
preserved in cross_fan_analytic_specialized_run_20260825/.

## Exact verified scope

For
\[
 X=V((x-1)(y-1))^{\mathrm{an}}
 \subset(\mathbf G_m^2)^{\mathrm{an}},
 \qquad
 \tau=(-\log|x|,-\log|y|),
\]
the frozen packet proves the following.

- \(X\) is a reduced, pure one-dimensional, good, strict and boundaryless
  analytic space, and \(\tau\) is a proper ordinary tropicalization with
  locally integral harmonic coordinates and image the full cross.
- Each compact truncation is a genuine harmonic-tropicalization chart.
- The effective cycle \(2[Y_h]+[Y_v]\) defines a positive closed order-zero
  current whose pushforward has ray weights \((2,2,1,1)\).
- The displayed potentials are decreasing locally uniform limits of smooth
  psh pullbacks.
- The exact upstairs current identities and their pushed identities hold,
  including the residual pushed defect \(2\delta_0\).

The packet explicitly does **not** prove equality of the two curvature
currents upstairs. They are
\[
 4\delta_{q_h}
 \quad\text{and}\quad
 2\delta_{q_h}+2\delta_{q_v},
\]
with \(q_h\ne q_v\); they agree only after \(\tau\) identifies the two Gauss
points. Thus this receipt certifies an analytic realization of the
weighted fan, current, psh approximation and pushed calculation, not an
analytic Bedford--Taylor counterexample.

The separate literal compact-source obstruction is not part of this
receipt and requires its own verification object before promotion.
