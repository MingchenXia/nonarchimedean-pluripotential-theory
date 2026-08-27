# P06.3 ordinary CLD-smooth curve regularization: live integration receipt

**Date:** 27 August 2026
**Production run:** `20260827T090645Z_767cbf81c723`
**Model:** `gpt-5.6-sol`
**Reasoning effort:** `xhigh`
**Verdict:** `correct`
**Critical errors:** `0`
**Gaps:** `0`

The direct endpoint assigned no item identifier.  None is inferred or
invented.

## Exact-byte identity

Chapter 19 inputs the following files directly, without label or mathematical
text transformation:

- statement:
  `editorial/rethlas_packets_20260827/p063_curve_cld_monotone_regularization_statement_20260827.tex`,
  SHA-256
  `767cbf81c723279c1218df4136f8e299465240b325f41f6b0663d001fb5d8a68`;
- proof:
  `editorial/rethlas_packets_20260827/p063_curve_cld_monotone_regularization_proof_20260827.tex`,
  SHA-256
  `d1db3c2db861d920598697fdad5d002a2b1ce947dbdbd95ad9b78b8f9f312bd8`.

The production request and response SHA-256 digests are
`81972c8453e6949d35e9dda7e0195f4550c65f48c206bb2111fac01415c0188e`
and
`0f06e94d8febf12e090c8a0054746646d5cb41febef2c09672ef76efa03b268a`.
The standalone PDF digest is
`c80370917813f90d8dc1e7f5f8a5ef7486ae98b15932e9b7710751d80af8a931`.
All `p063-*` statement, proof, and equation labels are unchanged.  The
packet's internal pre-verification comments are frozen historical comments;
the surrounding Chapter 19 prose explicitly says why they are retained.

Three independent exact-byte mathematical, source, and boundary audits
passed before submission.  A further post-integration hostile scan checked
every live P06.3 reference and corrected the Chapter 31 C5 census, four
field-scope omissions, and the arbitrary-singular/full-hierarchy firewalls.
No substantive integration defect remains.

## Exact scope and non-claims

The integrated theorem applies to a continuous function on an open subset of
the analytification of a smooth proper algebraic curve over an algebraically
closed complete nontrivially valued field.  In that scope it proves

1. current positivity;
2. Thuillier subharmonicity; and
3. local uniform decreasing ordinary CLD-smooth psh regularization

are equivalent.

It does not prove ordinary-smooth harmonic regularization, regularization of
arbitrary singular or `-infinity`-valued functions, full curve-hierarchy or
higher-dimensional collapse, a result for nonproper or nonalgebraizable
analytic curves, descent to a different BFJ base field, global BFJ numerical
positivity, or model-semipositive global metric approximation.  The live
text states each of these boundaries explicitly.

## Whole-book gate

- Final PDF: 3,181 pages, 15,329,788 bytes, SHA-256
  `c748ff631165674847f2b75916530c65f2b799e94164fe4cfee0a437f1ae3eaa`.
- Final log SHA-256:
  `aac330c5db747f5e80e4780be975722195d38f0ae9885ff98fc3aad7b4e61fde`.
- No TeX error, undefined reference/citation, duplicate label/destination,
  BibTeX/index warning, rerun request, or overfull box.
- Exact source closure: 117 files; manifest SHA-256
  `9132f4cd13d4ffd28777536c1044511646159e2945090cd5ee7d3bcba06770b9`;
  all entries verify and the path set equals the converged local build inputs
  plus the five build-control/bibliography inputs.
- Research frontier: 16 formal problem environments and 55 active atoms,
  with tier counts 7/14/17/17.
- Author blank; acknowledgements empty; no exercises; no optional
  conventional theorem-like names.
- Rendered inspection passed on PDF pages 948--960, 1000, and 2996--2999.

This receipt controls exact-byte integration and scope.  It makes no novelty
or priority claim.
