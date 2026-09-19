# P07.1 dependency-closed verification receipt

Date: 2026-09-20 (Asia/Shanghai)

## Final principal bytes

- `STATEMENT.tex` SHA-256:
  `8b9c6605c4016b4c69e489e5165d214360a8d5d3a34bf08b8f96419acde97e15`
- `PROOF.tex` SHA-256:
  `452530d86fbc979d2e6f95e2c8a489a24fa87a2ba466477933455cd68cea3d94`

The only change from the 2026-09-13 locally frozen candidate was the
mechanical house-style conversion of inline mathematical delimiters from
`\(...\)` to `$...$`.  The mathematical statement and proof content did not
change.  The final bytes passed the strict Mingchen writing audit with zero
errors and zero warnings before submission.

## Dependency closure

The request prepended the complete exact statement and proof of both
dependencies, in this order:

1. exact CLD infinite-star collapse, statement/proof SHA-256
   `99c1a6a6a712005e73ee3b7cdae297606895b22ce79c80a6411dfd7f4863c963` /
   `ca49ad210cf8e64100cc00c31c16a76f207ecd0d4b37dc365e8e1c61ce903090`;
2. Stone--Euclidean collapse, statement/proof SHA-256
   `dfd8c7cc9d6d26f50260707975ff62d4f292627f084400bcd37b32253c876cdc` /
   `9316e1a9df86c73a68ec099d3254e451ceaaac17a15c2a92441ad44961d863f6`.

No dependency proof was replaced by a summary.

## Verifier result

- Endpoint: `http://127.0.0.1:8107/verify`
- Model: `gpt-6-astra`
- Reasoning effort: `xhigh`
- Verification status: `final`
- Verdict: `correct`
- Checked proof items: 1
- Checked item: `pi_7f5f067d2ad2d7160b612eea`
- Critical errors: 0
- Gaps: 0
- Proof digest:
  `55c31b5ea8d4626ad8d6d28da49b83d8e9a550f0a4ae73b806a54027fddd1909`
- Context digest:
  `becd20cc465263489437dbcc59b09c46022df64b951a7176ee2d524c0b476cad`

## Archived transport

Directory: `VERIFICATION_RUN_ASTRA_20260920/`

- `request.json` SHA-256:
  `af8696b3af1527198e85a7559b592a310883a6911253225f8728aa3739cdbee8`
- `response.json` SHA-256:
  `e94df5b40ac7d3ae4f771fb708637466a38ba1898b30a712a85328fb26d7a8d7`
- `headers.json` SHA-256:
  `794ea8f4c4fa06fb9f3a8a509cbbeb1020577224a26f327028dc45bfd45e5ff7`

The response records final `correct` and states: “Checked all 1 proof items;
0 item(s) failed or were blocked.”
