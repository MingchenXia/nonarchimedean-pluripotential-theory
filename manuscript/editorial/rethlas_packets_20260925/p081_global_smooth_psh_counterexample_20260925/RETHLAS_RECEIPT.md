# P08.1 model-verifier receipt — 25 September 2026

## Frozen inputs

- Principal statement SHA-256: `60d573d3ec8e021e644ad9f559f3b6c1abaaf81375117dc8e0287db3bbb05b8b`.
- Principal proof SHA-256: `07d6cec9b6393175f89425c9ef03613a03f7149466f3348c26c41aebfdb2a2a9`.
- Primary-source extracts SHA-256: `89a4381edf6953f1679ec95499ee13feea21a8f058030f08b9727edf7f7bf9bf`.
- Review-scope instructions SHA-256: `8ce7462aca063e732a4ce6da036063ab0864d791fc72f22d24136e01dd62c24c`.

The two dependency files were prepended to the proof by the repository's
submission tool. The exact materialized request is preserved under `run/`.

## Execution

- Endpoint: `http://127.0.0.1:8107/verify`.
- Service-allocated run: `20260925T000718Z_60d573d3ec8e`.
- Model invocation: `gpt-6-astra` with `model_reasoning_effort=xhigh`.
- HTTP status: `200`.
- Request SHA-256: `4aae29650932e850dca3aba6166dd34b6eaf06a4043efca0ce45783078da3bb7`.
- Response SHA-256: `410e27b751324b85d5ecd22729213070c152878578448966e699bae050929e9b`.
- Headers SHA-256: `12a776546c438f3a12f764504dca170fc9f43decdec7f6a3e99b54cab6feef74`.

The local service was launched from the public Rethlas verification-agent
source at commit `887cc46427636bbdd235160a112f9a30ae81d040` after the older
iCloud-backed runtime proved unavailable. Its command line fixed the model
and effort before accepting the request. The response archive is kept byte
for byte; it does not itself echo the service run id or model configuration,
so those are recorded here rather than inserted into the response.

## Verdict

The verifier returned `correct`. Its sequential audit recorded 17 statement
checks and 12 reference checks, with zero critical errors and zero gaps. In
particular, it checked the sign in the residual-disc integration, the
degree-zero torsion reduction, the non-torsion point, the constant-model
nefness, the elliptic divisor identity, the convex smoothing and uniform
error estimate, and the cited CLD definitions and hypotheses in the
25 July 2025 primary text.

This is a model-backed verification record, not an authorship, priority or
publication claim and not a substitute for the separate local proof/source
review.
