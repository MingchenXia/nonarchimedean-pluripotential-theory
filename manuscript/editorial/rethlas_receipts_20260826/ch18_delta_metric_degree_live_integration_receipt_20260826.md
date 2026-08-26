# Chapter 18 delta-metric degree correction — live-integration receipt

## Scope and disposition

This receipt controls the exact replacement of
lem:ch18-delta-metric-gluing.  The replacement does not claim a new theorem.
It reconstructs, with the original hypotheses and quantifiers, the following
four statements from Gubler--Künnemann.

1. Facewise Hessians of a piecewise smoothly metrized line bundle define a
   global piecewise smooth Chern form.
2. The residual part is a canonical generalized delta-form of codimension
   one, uniquely characterized by its current after every algebraic pullback
   and restriction to every open subset.
3. Ordinary delta-metricity is the additional requirement that the
   facewise Hessian lift to an ambient bidegree-(1,1) superform with
   piecewise smooth coefficients; only then does one obtain the full first
   Chern delta-form.
4. Intersecting the ambient coefficient form with a codimension-c tropical
   cycle produces ambient bidegree (c+1,c+1), although the relative
   bidegree on the cycle remains (1,1).

The source audit uses GK17 Sections 9.7 and 9.13, Propositions 1.8, 1.14,
6.8, 9.8, and 9.11, Corollaries 1.15 and 3.19, Definitions 2.9, 9.9, and
9.12, Examples 2.10, and Remark 9.10.  No injectivity from generalized
delta-forms to currents on one fixed open set is assumed.

## Rejected first submission

Production run 20260826T010642Z_d35b3dc3efa6, item
pi_595c56d0350013e44fc58dd6, returned final wrong with two critical errors.

1. The statement had attributed uniqueness of the residual form to its
   current on the original open set, whereas GK Proposition 9.8 uses the
   universal pullback property.
2. The degree argument had not required the ambient intersection
   C = Trop(U) cap tilde-Omega to lie inside trop_U(V), so the Hessian
   identity was being used outside its stated domain.

The complete rejected request, response, headers, aggregate result, and
item-level process records are preserved under
rethlas_packets_20260826/ch18_delta_metric_degree_attempt1_run_20260826/.
The rejected response has SHA-256
444ef581032518204da07144bbfa17243e9761b22c344f065cce29e879466679.

## Controlling production verification

Both errors were repaired explicitly.  The corrected exact packet passed
production run 20260826T011701Z_1e7c96932016, item
pi_a860454e8a0004aa4767207c, with verifier gpt-5.6-sol at xhigh.
The final disposition is correct, with one of one item checked, zero
critical errors, zero gaps, and no request for expanded proofs.  The
item-level record reports 642.592 seconds and 83 tokens used.

The controlling hashes are:

| artifact | SHA-256 |
|---|---|
| exact statement | 1e7c9693201671bfe90d2843f9894fe2927ebe7d932bca0947b2499eb339075e |
| exact source-aware proof | 08391542696641113553a71e73d047d68d8b494fc5cd306b9ee6de541468e402 |
| source audit | c948f1ae64e618c19eb20c988bf5dc37d4a9414f34b76e39795be5fcb9946fa3 |
| request | 5161e9c633ef44f37bab428db6992fec89789ba5d8fce21c535e3c0b251425bd |
| response | 78ae5f0905768b550731dc2b047938a80600fbb9709586d39372003acaf92769 |
| headers | 86f105a77775f05c019cecf41ae4bb595f457eec5b0f892bb1b318267204d0d7 |
| aggregate manifest | 2e4697bd1eabb039eb4c7266a88f19ed1790580d6a26495bf99b97efb2aa06b7 |
| aggregate verification | dac978f169281e0bfe545ec37e264bc6db6007eadc2eb1d4ab214878a9beb23c |
| item log | 3241c960618a7039466223441ef8daac1b08f97527913c8aa4a15399132b3eed |
| item verification | ec19c70b91af4525b6ce5e237c694146973fa4fee70233265edd092cd09551fc |

The proof digest reported by the service is exactly
08391542696641113553a71e73d047d68d8b494fc5cd306b9ee6de541468e402,
identical to the installed proof file.

## Exact live integration

Chapter 18 inputs the frozen exact statement and proof files directly rather
than transcribing them.  The adjacent transition paragraph and hypothesis
ledger were rewritten to preserve the same four-way distinction.  The
revision log, Part II audit, chapter status, and source-boundary ledger now
record the controlling run and the rejected first attempt.

The production closure contains 109 files.  Its ledger is
editorial/current_source_closure_20260826.sha256, with SHA-256
8b16b58ceb11ad3049a7bd42879114988e68db0dd466c6d38a06a5b5a5ad2080.
Every listed file passed its hash check.

## Build, static, and visual gates

The converged whole-book build produced manuscript/book.pdf with 3,143
pages and 15,146,295 bytes.

- PDF SHA-256:
  54c403acc0de3d609072cdf1be909c1d1557562a0cfedd87c1f9e2f2e5fe8e08.
- Log SHA-256:
  6f264879ef7f0331dc747213b5d766679c11785438a818229dfac1a1d6ee47bc.
- The final log has no TeX error, undefined reference or citation, duplicate
  destination, rerun request, or overfull box.
- There remain 17 formal open-problem environments and 57 active atoms.
  This correctness repair retires none.
- There is no exercise environment and no optional conventional name on a
  theorem-like environment.
- The author remains empty and the acknowledgements have no body.
- git diff --check passed.

Visual inspection of PDF pages 862--866, printed pages 796--800, passed.
The transition, four-part lemma, imported-input ledger, proof, displayed
ambient representative, and following warning have no clipping, overlap,
malformed link, or unreadable text.

This receipt certifies the exact correction and integration only.  It makes
no publication, novelty, or priority claim.
