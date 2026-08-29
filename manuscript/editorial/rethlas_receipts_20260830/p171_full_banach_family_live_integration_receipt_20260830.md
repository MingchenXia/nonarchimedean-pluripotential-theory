# P17.1 Banach-family Monge--Ampère continuity: exact-live receipt

Date: 30 August 2026 (Asia/Shanghai).

## Result

The exact live-book dependency closure, principal statement, and principal
proof for the Banach-base continuity theorem in Chapter 66 were submitted to
the production Rethlas verifier with `gpt-5.6-sol` at `xhigh` scrutiny.

- checked item: `pi_87b42b938a8d830222bed78f`;
- status: `final`;
- verdict: `correct`;
- critical errors: `0`;
- gaps: `0`;
- proof digest: `cdce552b3750faed4dfbb6a0284405094be10b56c138363482cca0464e20f4af`;
- context digest: `bad36c34adc27ef316e09c1508028c1d890d6d4e863b12b13a4e4743ee579522`;
- adaptive context digest: `12d70934ba4c7584cb7a639c200aa3c8e458b53e9eab35fb9b804878f01d68e5`.

The materialized statement and proof had 22,849 and 87,132 characters,
respectively, with SHA-256 values

- statement: `0ba26fe924a065af31198cfc74aa44e790feb128159eef24458f8ca0b151f8b4`;
- proof: `cdce552b3750faed4dfbb6a0284405094be10b56c138363482cca0464e20f4af`.

The principal live files themselves had SHA-256 values

- statement: `0d95354a4cd2bd15d03020dde630779f4f423b73e9661eb8e65e0511dc765e24`;
- proof: `9cab2f0f679b095b00b2d9f760a4a5315d3a24fe7b295a9d0a9bf414d91e434a`.

## Exact transport

- request SHA-256: `eb2099d6484792b38b8861bb404f44d1f7b5621c2cdd558baee2d1a1fdcfe487`;
- response SHA-256: `3e5619bb1f348ec74eec5038cfda6ce1df82e4fba2b3bcd794776825ae9704c1`;
- response-headers SHA-256: `d785c75cbf195a8e4c6a3dcedaa49bace66a065d359b0e6a9560e661ad9efa13`;
- HTTP status: `200`.

The archived request materializes the exact files in dependency order.  The
statement side contains the weighted Philippon--Gauss statement, the
relative-resultant statements, the closed-immersion reduction, the
fieldwise/Banach comparison statements, and the principal theorem.  The
proof side contains their exact proofs together with the powered
normalization and fibre-uniform Chern--Levine--Nirenberg block.

## Build and retirement decision

Before submission, the exact live source compiled as part of a clean
3318-page whole-book build.  Its final log had no undefined references or
citations, no duplicate labels, no undefined control sequences, and no
overfull boxes.  Representative pages 2898--2927 were rendered and inspected.

The theorem answers Pille--Schneider Question 4.9 with its original
quantifiers.  It retains the top fundamental cycle, including generic
lengths of nonreduced components, and it treats powered real and complex,
trivially valued, and nontrivially non-Archimedean fibres without a
reducedness or purity hypothesis.  P17.1 therefore retires.  The active
inventory changes from 15 formal environments and 54 atoms to 14 formal
environments and 53 atoms; the tier counts change from `(0,6,14,17,17)` to
`(0,5,14,17,17)`.

No novelty or priority claim is inferred from the verification result.
