# Production Rethlas receipt: arbitrary-valued normal analytic curves

Date: 29 August 2026

This receipt records the controlling verification of the exact frozen third
revision.  It is not a novelty or priority claim.

## Exact inputs and independent audits

- statement SHA-256:
  `339f8cb085fd6a7ce4d57d6163cfeafdacfb2ad01397d77f39c6f63328178cb7`;
- proof SHA-256:
  `d6d02762690b9eeed6e025a3f5aa200d19994859ed02b27050da22e03da57660`;
- revised source-audit SHA-256:
  `2a9f76a2c264c726d1c7c1df67b414532400afc537c2a14103be919ddb41a769`;
- independent hostile-audit SHA-256:
  `534154de06a9c7c63d5a060c4feac5d47a274af168177a305f64972483134c41`;
- independent compile-harness SHA-256:
  `eb8a19c8fcf714f32e7c818cf197efce7800a327118088f5f632fd69cac2bbea`.

The independent audit passed with zero critical errors and zero proof gaps.
Its ten-page harness compiled cleanly.  The revised source audit separates
every imported theorem from the arguments proved inside the packet.

## Controlling production result

The production service used `gpt-5.6-sol` at `xhigh` scrutiny.  The archive
`p213_variation_graph_arbitrary_curve_revised3_run_20260829_8107` records
HTTP status 200, final verdict `correct`, checked item
`pi_d9543424f0492e1412e0d203`, zero critical errors, and zero gaps.  The
returned proof digest is exactly the proof hash above.

The request, response, and sanitized-header archives have SHA-256 values

```text
d9a4ad02796009280917f1c0d1de216503c5fdcd25aef28c073570e26baebf1f
93c586e3de8884e30e7e7c320e6364cb2bb9c6c35d38593361e34c9a85f06860
0f0bcd114f923264cbcfb398d5d8fc10b556eda20373330912c3ef8fe3eca217
```

The earlier revisions and their rejection receipts remain noncontrolling
technical provenance.  In particular, the controlling proof uses the actual
calibration coefficient on an analytic branch rather than the lattice gcd,
and it contains the edge-overlap propagation and cutoff arguments requested
by the earlier audits.

## Mathematical scope

The packet proves that every positive closed ordinary CLD current of
bidegree `(0,0)` on a connected, good, separated, normal, boundaryless,
purely one-dimensional analytic space over a complete non-Archimedean field,
possibly trivially valued, is a nonnegative scalar multiple of the
integration current.  It consequently proves the full Bedford--Taylor
predicate of CLD Definition 8.6.2 for every such current, not merely the
continuous-pair specialization.  Reducible and nonreduced spaces are handled
only after the separately audited componentwise reduction has passed its own
dependency-closed production verification.
