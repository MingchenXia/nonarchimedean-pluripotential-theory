# P05.2 graph classification verification receipt

## Controlling review

- Endpoint: local `/verify` service at `127.0.0.1:8107`.
- Model and effort: `gpt-6-astra`, `xhigh`.
- Local service archive: `20260925T194546Z_f78de6ebe9ec`.
- HTTP status: 200.
- Verdict: `correct`.
- Critical errors: 0.
- Gaps: 0.

The review checked the theorem in textual order, including the ambient
embedding, the slower rational-polyhedral norm, rational chordal
interpolation, preservation of the original vertex germs, the supporting
relation obtained from the cone slice, and the balanced-barycentre envelope
pinning argument.  It also checked that the theorem is stated only for the
real-piecewise-affine scalar extension and does not settle the literal
integral-slope or higher-dimensional problems.

## Exact-current identity

- `STATEMENT.tex`:
  `efb950a831b41bd7561bce361daedb9d71372ccae260c8c4392d5aa16217257c`
- `PROOF.tex`:
  `89a2ac92c3d8f04bae28e6b94fcdcb2def1d1582b3a6316cb331b88928c7d592`
- controlling request:
  `63aaa2e583e6f9140d47721b513e0e23d423f2e2a6663bc6e47801576b909682`
- controlling response:
  `00fda8ab3cc38eb304a6676ea97d96b6e2f2c42ceffb5c90f5e7ea4046ff9bcf`
- controlling safe headers:
  `faf2a39b8a2c29d87e6c0dcf9f78ea6a48255213a6bec9147c7674e388702ee7`

The statement and proof fields decoded from the controlling request match
the exact current dependency materialization and principal files byte for
byte.

## Exploratory predecessor

The earlier finite edge-jet packet also returned `correct`, with zero
critical errors and zero gaps.  Its request/response/safe-header SHA-256
values are
`cf90acd7a7bdfa67134a2897fe49c866a2a951f67ea60d6ff3f8cb80df95b30a`,
`b3253cafea7a8352afbd7e33c61025abf937a9b3b41db7504a8cafaaef91d590`,
and
`659f081d1b5f1d9459693cda90246ad959c9c7c7141b0efefa09195b59aaf05b`.
It is retained as exploration history and does not control the live theorem.

This receipt records model-backed review, not formal verification, peer
review, or a novelty certificate.
