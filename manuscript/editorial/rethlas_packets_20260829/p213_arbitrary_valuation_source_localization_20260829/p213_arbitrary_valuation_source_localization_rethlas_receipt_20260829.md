# Production Rethlas receipt: arbitrary-valuation source localization

Date: 29 August 2026

This receipt records the controlling dependency-closed verification.  It is
not a novelty or priority claim.

## Exact candidate bytes

- principal statement SHA-256:
  `ad13ea2d3a6ef526146607fee1731d39ebd26a225ff46cb5e2766ee4521fa1b1`;
- principal proof SHA-256:
  `ff0b5efcbb83d9765a7493ffb7219804510d1b3973916bfaf8388708dfd3d6a6`;
- atomic dependency statement SHA-256:
  `335532b6a0b71b4174c97246e06cd6ea473d61dd83402fcd709301408692f3db`;
- atomic dependency proof SHA-256:
  `f6bf21cc24ba593ca097c4facaf4a80c5c5e297ccb341d7a1ab9bd6fa7f429e0`.

The materialized statement and proof SHA-256 values are, respectively,

```text
e2d5cedea4b3b06f8c5f0db181a33b3cf595326822d255069f1ee15deb760fe2
9ed858931023a23b6b1de52650ccad8f9c3cdba252e0d9cee324ef63d30e6497
```

## Verification result

The archived response in
`p213_arbitrary_valuation_source_localization_revised_dependency_run_20260829_8108`
records final verdict `correct`, checked item
`pi_16e5f8b5146cec29dfcdaa81`, zero critical errors, and zero gaps.  The
production service used `gpt-5.6-sol` at `xhigh` scrutiny.  Its proof digest
is the exact materialized proof hash above.

The request, response, and sanitized-header archives have SHA-256 values

```text
0520d79404e5e94952de4e2da2cebb56d9c16d69e907e888747f038a3414faeb
230a6b84943ebc15e785fe8026dd8a23afef06fac8f0a88f5a9623e341b70aaa
24d60a348bd60d827d06f2e405957f122d341c497c912a23ae42511909dea346
```

The exact principal bytes independently passed
`p213_arbitrary_valuation_source_localization_exact_byte_reaudit_20260829.md`,
SHA-256
`4a574a50ab5e5ea57e68f000cbfc8881a23697f76ef89402e0c6a9b093d67f0b`,
with zero critical errors and zero proof gaps.  The exact revised atomic
dependency has its own independent audit and production receipt.

## Rejected noncontrolling run

The earlier dependency-closed submission used the superseded atomic proof
whose supporting irreducibility sentence cited the wrong CLD subsection.
It returned `wrong`, one critical error, and zero gaps.  The principal
source-localization bytes were unchanged.  That response remains archived
as provenance and is not a controlling verification.
