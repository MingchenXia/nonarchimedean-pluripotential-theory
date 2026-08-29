# P21.3 arbitrary-valued normal curves: live integration receipt

**Date:** 29 August 2026

**Model and scrutiny:** `gpt-5.6-sol`, `xhigh`

**Controlling item:** `pi_d9543424f0492e1412e0d203`

**Verdict:** `correct`; **critical errors:** `0`; **gaps:** `0`

This receipt controls the exact-byte integration of the arbitrary-valued
normal-curve theorem.  It is not a novelty or priority claim.

## Exact verified inputs

Chapter 16 directly inputs the following frozen files:

| Live input | SHA-256 |
|---|---|
| `editorial/rethlas_packets_20260829/p213_variation_graph_arbitrary_curve_20260829/p213_variation_graph_arbitrary_curve_statement_revised3_20260829.tex` | `339f8cb085fd6a7ce4d57d6163cfeafdacfb2ad01397d77f39c6f63328178cb7` |
| `editorial/rethlas_packets_20260829/p213_variation_graph_arbitrary_curve_20260829/p213_variation_graph_arbitrary_curve_proof_revised3_20260829.tex` | `d6d02762690b9eeed6e025a3f5aa200d19994859ed02b27050da22e03da57660` |

The independent hostile audit has SHA-256
`534154de06a9c7c63d5a060c4feac5d47a274af168177a305f64972483134c41`.
The controlling packet receipt has SHA-256
`5da9aee07589e72bf9c515097ca6542d51d5fa5b9c116932fd8bc3ea7513456d`.
The production request, response, and sanitized headers have SHA-256 values

```text
d9a4ad02796009280917f1c0d1de216503c5fdcd25aef28c073570e26baebf1f
93c586e3de8884e30e7e7c320e6364cb2bb9c6c35d38593361e34c9a85f06860
0f0bcd114f923264cbcfb398d5d8fc10b556eda20373330912c3ef8fe3eca217
```

Decoding the archived request reproduces the statement and proof digests
above exactly.  The returned proof digest is the exact proof digest.  Earlier
revisions, including the calibration-defective and smooth-locus-defective
versions, remain archived as noncontrolling rejected provenance.

## Mathematical scope

Let (K) be any complete non-Archimedean field, possibly trivially valued.
On every connected good separated normal boundaryless pure one-dimensional
(K)-analytic space (Y), every positive closed ordinary CLD current of
bidegree ((0,0)) is (c\delta_Y) for a unique (c\geq 0).  No strictness or
smoothness hypothesis is imposed.  The conclusion gives the full predicate
of CLD Definition 8.6.2, rather than only the continuous-pair specialization.

The separately verified direct trivially valued examples remain in the book
as illustrations and consistency checks.  Their exact statement and proof
digests are
`cd1032050a8ce5d3617fbf1952b411a1fe638db2f658aec9b7e0810e3b32d77b`
and
`37ed90b0b7f079b0f34d140a79c61c510b1206da6629953696d4a2d98c8a3ee8`;
production item `pi_ed915de7970791904bc0ec6e` returned `correct`, zero
critical errors, and zero gaps.  Their historical scope sentence is retained
for byte identity and is immediately followed by the controlling broad-scope
clarification.

## Live integration and post-integration audit

The theorem and proof are input without mathematical-text transformation in
Chapter 16, then recorded consistently in Chapter 72, Appendix L, the atomic
inventory, and the verification ledger.  The relevant post-integration
SHA-256 values are

```text
9839912710c298c21baab77d01a2c007a9fb63cce52368503c9c4bc73c9f4fc3  ch16_bedford_taylor.tex
97684f7b96b4ca3bf9b8e6aa3a211b36f4401ee052b2d6e4336ceeac204dd712  ch72_major_open_problems.tex
76db1b15d470c380c21468cf4f8d6bab71f20ccad59b2eb147c39045462cfa2b  open_problem_atomic_inventory_20260824.md
4ca41f56a061ec94557a88d6f5d062f6d3076c2f894543fcf355d88697dd69ee  rethlas_verified_results.md
d1056a3f6d0b902dacff7f30013ca45b6693c77875e5ea79ed820c3da192264f  appL_provenance.tex
```

An independent post-integration audit rehashed the live files and decoded
production request, checked all new labels and compiled inputs, and found no
scope, chronology, reference, convention, or layout defect.

## Whole-book gate

- PDF: 3,282 pages, 15,765,463 bytes, SHA-256
  `ee3ef27eebb5449b703e25e91d48b804598049a3f47244117cdd823e9a3497d0`.
- Build log SHA-256:
  `3619f042f18a1a73734c5dff76378fc480469affb2e96d50b17927195823ecb8`.
- No TeX error, undefined reference or citation, duplicate label or
  destination, rerun request, or overfull box.
- Final rendered inspection passed on physical PDF pages 793, 802, 812,
  818--819, 3103--3106, and 3255--3257; the complete new theorem block on
  pages 793--812 had already passed page-by-page inspection before the final
  forced rebuild.

