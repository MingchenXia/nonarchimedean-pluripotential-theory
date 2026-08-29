# Production Rethlas receipt: CLD support-index correction

Date: 29 August 2026

This receipt records the controlling verification of the exact frozen packet.
It is not a novelty or priority claim.

## Exact inputs and independent audit

- statement SHA-256:
  `2b291fc55872ab32d40fa3a67e9a9308fc12ac9726113b48950d0a9e50cfd8c1`;
- proof SHA-256:
  `9f21f7ece49c761d3f19c07acd8b56e48e9939be493e0bbbd39c0a4d3176e668`;
- independent hostile-audit SHA-256:
  `62520258d3a5a4d6e73a3d7f9d0dfd8679586ec718d03acf4f32bebcabe7adaa`.

The independent audit passed with zero critical errors, zero proof gaps, zero
source mismatches, and zero degree/index collisions.  Its independent harness
compiled cleanly to four pages.

## Controlling production result

The production service used `gpt-5.6-sol` at `xhigh` scrutiny.  The retry
archive `ch14_cld_support_correction_retry_run_20260829_8107` records HTTP
status 200, final verdict `correct`, checked item
`pi_d8921af65dfc0c98f29a5fb7`, zero critical errors, and zero gaps.  The
returned proof digest is exactly the proof hash above.

The request, response, and sanitized-header archives have SHA-256 values

```text
68ab52a8e32bcb09f706bc22923ae49996c86c4bed4eb31ed2e6e166c21387cc
267334e78b0d797d4408a87e74d26c97d32a71f10f3d3b873787b6f383c3f415
3f9a2090608cc6b53c490ba2ba033138f20e4e11bfeb4456aabdf420bd243b0e
```

The earlier directory `ch14_cld_support_correction_run_20260829_8107`
contains a request from an interrupted service attempt and no verdict.  It is
retained as noncontrolling technical provenance.

## Mathematical scope

The packet reconstructs the proper-tropical-pushforward proof of the
nontrivially valued support theorem, proves the scalar-extension statement
with Hausdorff exponent equal to the current's bidimension, and gives an
explicit trivially valued one-dimensional counterexample to the exponent
printed in CLD Corollary 16.8.6.  It does not extend the trivially valued
claim from Bedford--Taylor products to arbitrary positive closed currents.
