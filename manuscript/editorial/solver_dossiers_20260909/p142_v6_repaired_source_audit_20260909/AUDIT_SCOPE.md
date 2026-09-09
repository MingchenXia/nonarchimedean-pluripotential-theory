# P14.2 V6 repaired source-stage hostile audit

Candidate: `/private/tmp/p142_hostile_repair_v6_20260909`

Manifest SHA-256: `3511b635413d7ace9013edd278216017096d7359ac5dd2b3155cbf179c83e97f`

This packet covers only repaired source-stage release controls. It does not
contain a final-path smoke receipt or a production-verification request.

The audit must examine the exact checker, runner, hardened host/MCP source,
pin data, source decoder, and focused adversarial regressions appended to the
proof context. A clean verdict enables only the distinct next smoke gate.
