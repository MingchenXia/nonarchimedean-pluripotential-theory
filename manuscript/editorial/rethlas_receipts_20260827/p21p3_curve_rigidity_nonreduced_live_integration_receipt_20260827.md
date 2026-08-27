# P21.3 reduction invariance and nonreduced curve extension: live integration receipt

**Date:** 27 August 2026

**Local archive label:** `20260827T133151Z_3ee099341ca1`

**Model:** `gpt-5.6-sol`

**Reasoning effort:** `xhigh`

**Verdict:** `correct`

**Critical errors:** `0`

**Gaps:** `0`

The production endpoint assigned no run identifier, item identifier, or
verification-status identifier.  The label above is only the verifier
service's local archive address; no endpoint identifier is inferred or
invented.

## Exact-byte identity

Chapter 16 inputs the following files directly, without mathematical-text or
label transformation:

- statement:
  `editorial/rethlas_packets_20260827/p21p3_curve_rigidity_nonreduced_addendum_statement_20260827.tex`,
  SHA-256
  `3ee099341ca1ba77d806082ca2903320fd9db25c448b48f3dab9c2bb607a777e`;
- proof:
  `editorial/rethlas_packets_20260827/p21p3_curve_rigidity_nonreduced_addendum_proof_20260827.tex`,
  SHA-256
  `b8aac711aafa611750c56a960177182ff1b7b8f78b489d7b43575d03b28b7f43`.

The production request's two JSON strings compare byte-for-byte equal with
these files.  The production request, response, and headers have SHA-256
digests
`3b5f6e32a1de8954d0bfb4827f79ec7f43f85949e4b2ac8e42531da28f28e5cf`,
`50bb1132de3b5d9d4a9c95de23c671107615979abc4b739596ac5be4bbb8f1f5`,
and
`e3cc7aed80b56f668bda8f20ce282303abf06989118645ae125e0ed6653ef83d`.
The exact standalone PDF, compile driver, minimal cross-reference data, and
compile log have digests
`96ceb3a464104c400d0c76e99ee2f5d73597b434d6f967f13438a057e1cb94ad`,
`6beb6e228af8a1112253f539754ab398d71f3c72cbd4711ac71aa2f4794051ac`,
`dcdd7be33e6309a70373e92c83b4c658332d01f4f821650e8a4e0529d1dd6965`,
and
`7323c34992ee11588335ef99cc19b282596e5797d6c208b973738b064c45ca95`.
Every entry of the frozen packet manifest verifies; the manifest digest is
`21c8dd25839754b56528f66bb91b922ceb33678f2f9d45a09f243de7bc774640`.

## Mathematical and source audits

Three independent exact-byte pre-production audits passed.  They checked the
ordinary-open and G-domain reduction statements separately, the compact-test
final topology, current duality and bidegrees, positive-current Borel
multiplication, transfinite psh filtrations, fundamental-cycle
multiplicities, componentwise classification, the type-1 zero-atom
no-cancellation argument, and the Bedford--Taylor predicate.  Every cited
CLD locator and every open-set restriction was checked; no audit requested a
repair.

A fresh hostile post-integration audit then compared the request bytes with
the directly input files, confirmed both entries in `book.fls`, verified the
121-file source-closure ledger, rescanned all live and editorial P21.3 scope
statements, and recomputed the structural frontier.  It found no stale claim
that the verified nonreduced algebraically closed curve slice remains open,
no byte-identity or scope defect, and made no mathematical edit.

Chapter 13 was corrected at the same gate to cite the ordinary-open lifting
statement of CLD Proposition 15.1.3(b) for ordinary forms.  Its separate
G-domain part (a) is used only for G-forms.  The live proof therefore does not
silently substitute a G-domain refinement for an ordinary neighbourhood.

## Exact scope and conclusion

The proposition treats a good separated strict pure one-dimensional
boundaryless analytic space over an algebraically closed complete
nontrivially valued field, without a reducedness assumption, provided that
the normalizations of the irreducible components of the reduction are
rig-smooth.  It proves:

- invariance under reduction of ordinary forms and compact-test topology,
  currents and weak topology, positivity, closedness, the stated products,
  CLD psh sheaves, and G-forms;
- the multiplicity-sensitive identity
  `delta_X = sum_i m_i delta_i`;
- unique locally finite classification of every positive closed bidegree
  `(0,0)` current as `sum_i c_i delta_i`, with `c_i >= 0`;
- equivalence of multiplicity-weighted and reduced curvature equality and,
  hence, the Bedford--Taylor property for every such current.

The theorem does not relax algebraic closedness, completeness,
nontriviality of the valuation, goodness, separatedness, strictness,
boundarylessness, pure dimension one, or rig-smoothness of the reduced
component normalizations.  It says nothing about analytic dimension at least
two.  Accordingly P21.3 remains one T2 residual atom and the inventory stays
at sixteen formal problem environments and fifty-five active atoms, with
tier counts 0/7/14/17/17.

## Whole-book gate

- Final PDF: 3,193 pages, 15,368,835 bytes, SHA-256
  `f6ac291a3a3e0ba3455b734e41dfd3693f723d311a90abcd8f9edcd9752bab14`.
- Final log SHA-256:
  `762e6b3c8e09cbc597a25d695e4bacc84ae0db8bff2a81580915dc095419796b`.
- No TeX error, undefined reference or citation, duplicate label or
  destination, BibTeX or index warning, rerun request, or overfull box.
  There are 991 underfull-box notices from the monograph layout and long
  tables.  The only `Warning:` line is the harmless historical class-path
  mismatch: the requested local file `style/svmono` declares itself as
  `svmono`.
- Exact source closure: 121 files; manifest SHA-256
  `6f90d646f518ce1950ab2a4af3c8ed1180dd50bcc51ab7754d53a6655a9ef55d`;
  every entry verifies.
- Structural frontier: 16 formal problem environments and 55 active atoms,
  with tier counts 0/7/14/17/17.
- Author blank; acknowledgements empty; no exercises; no optional
  conventional theorem-like names.
- Rendered inspection passed on physical PDF pages 571--573, 746--754,
  3019--3022, and 3168--3171.  These pages cover the corrected source
  distinction, exact proposition and proof, example, scope firewall,
  open-problem status, provenance, and all neighbouring transitions.

This receipt controls exact-byte integration and scope.  It makes no novelty
or priority claim.
