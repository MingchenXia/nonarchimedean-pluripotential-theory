# P11 moving-center Radon--Riesz counterexample: round-two production receipt

Date: 25 August 2026

## Verdict

- Production run: `20260825T042017Z_948e2b7cde7d`
- Item: `pi_0b7126d51ccabcab1920a96d`
- Model: `gpt-5.6-sol`
- Reasoning effort: `xhigh`
- Verification status: `final`
- Verdict: `correct`
- Checked items: 1 of 1
- Critical errors: 0
- Gaps: 0
- Adaptive round: 0
- Wrapper return code: 0
- Wrapper guard: `completed`
- Child guard: `completed`

The item verification expressly confirms the three substantive gates: the
exceptional-divisor valuations converge pointwise to
`ord_D`; both exhaustion values equal one; and the moving section supplied
by `Y_j` gives the uniform strong-distance gap at least one.

## Exact frozen input

- Statement SHA-256:
  `948e2b7cde7dc32411bea2acb46f6fa821e65afaa8cb8a546ec01759416cfb6c`
- Proof SHA-256:
  `46875db7cbe7869e95195f6345989df85031c82d0b52df298e0427515100e959`
- Round-two request SHA-256:
  `882f866c365ddf88206c9d1df32a7b399e2de5f9deaf64bdc10eec689e3144e0`
- Authenticated source PDF SHA-256:
  `8d5975337f4ac88a475929ea6a436ec4a15d08715d5582bc0ba0eb3e07152c52`

The request's `statement` and `proof` strings were compared byte-for-byte
with the named frozen TeX files before submission.  The returned proof
digest is exactly the frozen proof SHA-256 above.

## Preflight

A minimal wrapper containing only the exact statement and proof, together
with standard AMS packages and a theorem environment, compiled twice under
`pdflatex -halt-on-error -interaction=nonstopmode`.  The final pass had no
fatal error, undefined control sequence, or undefined reference.  The
rendered two-page result was visually inspected.

## Preserved production artifacts

- API response SHA-256:
  `978e78352153749b6ec86accb478c043a719699792eafd9dce3c6bdf229ab013`
- Run manifest SHA-256:
  `ee111de21f14b3569aa039accfdbe31ee30f4a48eef249e774d581179499eed1`
- Run verification SHA-256:
  `b29d496052f9f4ac095eb24b64b1055a541369ee118b52aa8a1212c7a567a1f8`
- Item verification SHA-256:
  `ef93f2d174f6e976eb393401aa45e92e76b15331e960d1ed4ff6d979acb81c40`
- Item log SHA-256:
  `7896c5eeaa4713cd312aa36c5340d3c2029ebf3596520a0544fb258f5aa3bee6`
- Wrapper guard SHA-256:
  `b08d0874ebafc592d9a603f1e4e24fa7f1483be7d7cd4c309b8e3035155a563f`
- Child guard SHA-256:
  `72cd6c2157821896f35ca1297502ee9e935b0bfff6e8656b544a25f34a73a06d`

All run, item, log, and guard copies were compared byte-for-byte with the
production result files.

## Rejection preservation and live-edit firewall

Round one, `20260825T040646Z_948e2b7cde7d`, remains preserved separately
with its `final/wrong` response, run artifacts, guards, and the exact
superseded statement/proof bytes.  Its cancellation objection is repaired
only in the round-two proof by writing
`div(f)=ord_D(f) D+E` and excluding the finite set
`D cap Supp(E)`.

No live chapter, ledger, status count, or integration file was edited in
this round-two audit or submission.
