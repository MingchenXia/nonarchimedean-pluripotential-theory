# Production Rethlas receipt: nonrigid localization on a normal curve

Date: 29 August 2026

This receipt records verification of exact quarantine bytes.  It is not a
novelty or priority claim.

## Controlling exact inputs

- statement SHA-256:
  `335532b6a0b71b4174c97246e06cd6ea473d61dd83402fcd709301408692f3db`;
- proof SHA-256:
  `f6bf21cc24ba593ca097c4facaf4a80c5c5e297ccb341d7a1ab9bd6fa7f429e0`.

The proof gives a self-contained irreducibility argument for a connected
normal affinoid domain and cites the relative-boundary results at the
section level.  These changes supersede the earlier proof hash beginning
`77da7a`.

## Controlling verification result

The production service used `gpt-5.6-sol` at `xhigh` scrutiny.  The archived
response in
`p213_normal_curve_nonrigid_localization_revised_run_20260829_8108`
records:

- final verification status;
- verdict `correct`;
- checked item `pi_d119cd9e238f31f7303b5e88`;
- zero critical errors;
- zero gaps;
- proof digest equal to the exact proof hash above.

The archived request, response, and sanitized headers have SHA-256 values,
respectively,

```text
8cb1380aa1d84bc8d7f7d930ac371812b6aa25240b262d2328fa4a4ca89ad5e4
b577c7f1679f1d6350dc8af38e8ce8d7ff8a45bf26a8846fa8f5113dd373dd38
5d94016e6a06155a0a21bc250e392d3bf3c63c45dc4abc2cbaa1874f6dca1a77
```

The same exact statement and proof passed the independent hostile/source
audit
`p213_normal_curve_nonrigid_localization_irreducibility_exact_byte_reaudit_20260829.md`
with zero critical errors, zero proof gaps, and zero citation mismatches.
That audit has SHA-256
`593cb226927511f4f873f926b6e337efe55313d1bb7f1a34ec9a49776cd21727`.

## Superseded provenance

The earlier production response for proof hash beginning `77da7a` was
`correct`, but a later dependency-closed run detected that one supporting
sentence cited the wrong CLD subsection.  The mathematical assertion was
replaced by the self-contained argument in the controlling proof.  The
older run and audits remain archived as noncontrolling provenance.
