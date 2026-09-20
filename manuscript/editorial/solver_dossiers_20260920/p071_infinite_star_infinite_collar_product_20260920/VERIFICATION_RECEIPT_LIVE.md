# P07.1 infinite-star × infinite-collar product: verification receipt

Date: 2026-09-20

## Accepted principal bytes

- Statement SHA-256:
  `ec4503f598beba8b853e18a50561d476b754f5f0bf615ff221e26e78a36c6576`.
- Proof SHA-256:
  `d915ae5a407e65ef82a9eb02d205c0cd3e8871e6ba0c8dfec94b182d2edff49c`.

## Final accepted dependency-closed run

- Service: local `gpt-6-astra`, reasoning effort `xhigh`.
- Endpoint: `http://127.0.0.1:8107/verify`.
- Verification status: `final`.
- Verdict: `correct`.
- Checked item: `pi_7f64cae4c772b9edf730c3eb`.
- Critical errors: `0`.
- Gaps: `0`.
- Materialized proof digest:
  `e4d69046a16ca808870bd7b9f8ed4abc20c5a9a96ab6fa75b3a89c02fbf77597`.
- Context digest:
  `15ef179a84f0e42db8a3f19fb76961f467c9d88787a2005240e16b1b542d96aa`.
- Adaptive context digest:
  `df5147da1613b1089114ccbdecd82f985e52b9a11054eadbfa66951198d89146`.
- Item context digest:
  `d474ec60b486053d2cafbdd2772cc85b2fb4d55b0df74e19da5b99cd3305e23e`.
- Archived request SHA-256:
  `9b53dfdf0d1a76c24bbbcaa5179c4b821ee777a1bf90acd11081e161e5dfcd86`.
- Archived response SHA-256:
  `a69eecac58cbb9c738807ff43cfe045bed837f8c63efd43e2bcf7c9e255dc45d`.
- Archived safe headers SHA-256:
  `a6ea6a6ad975234cbce6c8eb2fd974a6ac39759d369288b465be41a9518feac1`.

## Superseded mathematical pass retained

Before the final visual audit, the repaired dependency-closed packet passed
as item `pi_6e42f81c8aed3484a0f4ce21`, with zero critical errors and zero gaps.
That request and response remain in `model_run_repaired_dependency_closed/`.
The visual audit then found two missing TeX backslashes in displayed spacing
commands.  They did not change the mathematics, but they changed the proof
bytes, so the corrected exact packet was submitted afresh and is the final
accepted run recorded above.

## Rejected precursor retained

The original dependency-closed run returned `wrong`, with one critical
error and one gap.  It checked item `pi_dddabcb5edbe492cf0dc8342`.  The
original proof SHA-256 was
`eae99d977bbf137f7d28da3cddbcfd778b3b41ea05d6154fc712abb76a3d35ac`.
Its archived request, response, and safe-header SHA-256 values are,
respectively,
`c38b7ce60bea5db6795913d859247bbdb4641f8dd0b16bbcc1f4643da1f9d671`,
`02fc0173f3c1e6c28f520017eb22065159628b31a73e2ca1af39d4dffdd35900`,
and
`b93cc55641a019a9d05c1de0f49699ab44d71b4edffaa37960bbb41c34576b16`.
The repair ledger records the two exact repairs.
