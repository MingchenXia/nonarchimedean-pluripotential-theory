# Verification receipt

Date: 20 September 2026

The dependency-closed packet was checked by the local verifier at
`http://127.0.0.1:8107/verify` using `gpt-6-astra` with reasoning effort
`xhigh`.

- Verdict: `correct`
- Verification status: `final`
- Checked items: 1
- Critical errors: 0
- Gaps: 0
- Checked item: `pi_289ea5bf00583ce43371f809`
- Proof payload digest:
  `26c427d31048de8f40627d380e5f36ce0d3cf3830ceb309980b9a19c65174ac4`
- Context digest:
  `a4218624b3d28235d5326f984be56b3868f7c693c455300e928d572bc7394c6a`
- Adaptive context digest:
  `57dc68157858d7abbf366d0ba07586ac7ff2bcbaafd1d66320a72578d5b38b05`
- Principal statement SHA-256:
  `fceb1f33684cd431298d020b0be3649a4ef1f96d0f06719562660ab9fcbb7615`
- Principal proof SHA-256:
  `9a693cc3d087557132a23584817de1dc8018ce35c8e101948c548a5f87996513`
- Request SHA-256:
  `ac6d606c41cd9c1945dff1486e7e366108406db4c8968752cd1903a1d06e3d83`
- Response SHA-256:
  `2ca78da177806f66dc9d79f91891f68640d68c604a5f17c2ab26bb7a696c34df`
- Header SHA-256:
  `a05e697bb3131b6d2db9d32d1b2da1e27750ec4e5638fda78a7052e06f44e738`

The strict exact-current audit passed.  It reproduced the current payload
bytes, target coverage, proof and context digests, adaptive attestation, and
the independently inspected verifier-source bindings.
