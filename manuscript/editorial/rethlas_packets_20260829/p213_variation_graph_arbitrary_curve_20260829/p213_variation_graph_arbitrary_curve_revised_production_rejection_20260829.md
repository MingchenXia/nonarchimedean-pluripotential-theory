# Production rejection: first revised arbitrary-valued normal-curve packet

Date: 29 August 2026  
Status: final production rejection; permanently noncontrolling and not eligible
for live-book integration.

## Exact frozen inputs

- Statement SHA-256: `8c736e3df2df1efd7b6925dd4edccddfcf03cc1ee0b68250bd1219f80169be5a`
- Proof SHA-256: `9cb4d5eef1370ef97ccf1fa51e9ece16ab418c44092df61bd1a403f3f1d99ed9`
- Archived request SHA-256: `3eea582039988690c179ab7270df30555f7b45cbf2b86144cad8bc96e10e4138`
- Archived response SHA-256: `23308b2792ea62fb0e4f28cbdeca9a439ae102f5488421dc1119b3f981510826`
- Archived headers SHA-256: `c916c77b664c2c97dfe1437a40f10604e9c5341c154e2c074fe8fd3a7d108cb9`

Extracting the two JSON string fields with no added newline gives statement
and proof hashes equal to the frozen hashes above.

## Production result

- Service run: `20260829T085210Z_8c736e3df2df`
- Checked item: `pi_cce730f1dff58a14d9cf9ad0`
- Model: `gpt-5.6-sol`
- Reasoning effort: `xhigh`
- Verification status: `final`
- Verdict: `wrong`
- Critical errors: `1`
- Gaps: `2`
- Proof digest: `9cb4d5eef1370ef97ccf1fa51e9ece16ab418c44092df61bd1a403f3f1d99ed9`
- Context digest: `391c941fdb989e1adc294ae76076029c45e6489ffb9a983da204d3ea096b19ee`
- Adaptive context digest: `65f1d0f10fb003b579a8e244fca2a0eacaf019b57abf427778dcf530d8d8cb92`

The service process completed normally with return code zero, and its output
passed schema validation.  This is a mathematical rejection, not a transport
or infrastructure failure.

## Controlling diagnosis

The proof incorrectly identified the coefficient of
`(F_trop)_*(delta_Y)` on a primitive target ray with the gcd `q_b(F)` of
the normalized integer slope vector.  This identification requires a
generic quasi-smoothness hypothesis that the theorem does not assume.
Purely inseparable multiplicity can disappear after completed-perfect-closure
reduction while remaining in the analytic calibration/local degree.  On
`Y=A^1_{K(t^(1/p))}` over `K=F_p((t))`, the coordinate moment can have
`q_b(F)=1` although the canonical pushforward coefficient is `p`.
Consequently the ratio `t_b/q_b` used in the rejected proof is not the
ratio to the integration current.

Two additional steps were incomplete:

1. nodewise equality of ratios was not accompanied by an overlap argument
   showing constancy along an open graph edge;
2. CLD Corollary 15.2.5 was used as though it directly supplied a cutoff in
   `[0,1]`, whereas a smooth scalar postcomposition is required.

The classification theorem itself is not disproved by this response.  The
scope-preserving repair is to use the actual positive analytic calibration
coefficient of the integration-current pushforward, never to identify it
with `q_b(F)`, and then run the divisor-functional argument for that actual
coefficient.  Any such repair is a new packet and must pass a new independent
exact-byte audit and a new production verification.

## Archived service evidence

- `service_manifest.json`: `96d20674d4c42387ecc19206779d20dd9ffe4a8ea6866d7bf2b499dee9d9f6a6`
- `service_verification.json`: `b91a5f17a953a3fbe7113df8a5df8936a234d2c1d68e4cd91f9f8fa0bcd0170a`
- `service_item_log.md`: `ee5ae0c69ee23e6ec8d8e81c53ef806f8f07cb9c22330dfe42b2d2e982fabc03`
- `service_item_verification.json`: `530740e1f45532f8d83fbb488f8f247dc14f6c5b54bfa6b35847bb12f512d602`
- `service_process_guard.json`: `7d03f01f31c04c09e9b47e02f1b7b40ec18e71b3ca7e6bd64b2a732a81d84413`
- `service_process_child_guard.json`: `2558b3f38a36eee589fdd99cf53f570b5f345ac35f937b95dccb517b4d2f13d8`

All of these files are archived under
`p213_variation_graph_arbitrary_curve_revised_run_20260829_8108/`.
