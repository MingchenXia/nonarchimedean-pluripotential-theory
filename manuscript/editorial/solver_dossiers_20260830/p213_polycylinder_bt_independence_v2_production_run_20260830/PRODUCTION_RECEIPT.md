# Production verification receipt

The repaired P21.3 strict-open-polycylinder packet was submitted together
with the exact production-verified P06.2 v3 statement and proof on 30 August
2026.  Production Rethlas used `gpt-5.6-sol` at `xhigh` scrutiny and returned
the final verdict `correct`, with zero critical errors and zero gaps.

Principal frozen bytes:

- statement SHA-256: `955e1ab4323ddfe935b8bb54d7657915ea6f563e8d6e8f178ab589fcee5f16f1`;
- proof SHA-256: `70f34cad9f975402dd03f7f03de0b941898df112df2c018570bdbcba0b48f077`.

Dependency-closed materialization:

- statement SHA-256: `6c90e664468b815126ff64f1c0e2297b4d81bf0cf8d51e2a243ee778822f42ce`;
- proof SHA-256: `6eff86ba6c989143485449b189f1379e986f3d8349abc403dc23ae5d56e7fd33`.

Archived HTTP artifacts:

- request SHA-256: `add3a522de8d31ffb393d3c38c9ef63f33d125bccc5f56797cd7679cc3b7696d`;
- response SHA-256: `8ef692e78c8ab156238597405a0b5cd8003f5bc9bee94acc62ab4eb913317779`;
- headers SHA-256: `e0019f187ffc8b6c829d7fc4c700c4f0cae92a501c1288e4d67d3ab9c0018236`.

The verifier explicitly checked the exact fibre restriction argument, the
strict-annulus and iterated-Gauss classifications, continuous multiplication
of positive currents, the topology-basis quantifiers, the smooth-current
Leibniz identity, and the fixed-domain firewall.  This result narrows P21.3;
it does not retire the general higher-dimensional atom.
