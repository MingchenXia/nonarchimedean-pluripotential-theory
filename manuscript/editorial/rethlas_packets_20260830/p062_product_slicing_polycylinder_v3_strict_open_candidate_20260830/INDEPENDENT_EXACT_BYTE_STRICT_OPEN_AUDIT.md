# Independent exact-byte audit of P06.2 v3 strict-open packet

Date: 30 August 2026

Auditor role: independent, fail-closed exact-byte and dependency-closure
review. I did not prepare the v3 packet, did not edit either frozen
mathematical file or any live-book file, and did not call Rethlas. Any
uncertainty was to be counted as a gap.

## Exact target identity

The bytes independently reviewed were:

| target | independently recomputed SHA-256 |
|---|---|
| `p062_product_slicing_polycylinder_v3_strict_open_statement_20260830.tex` | `985be85d97b583f72be5cee65988df6f31c1edb49a685121b834df179fa87fda` |
| `p062_product_slicing_polycylinder_v3_strict_open_proof_20260830.tex` | `42b592bf8ac26ed46c36928e5e90272225ae6883bd2bfe62d3ff2840f01d46e5` |

These agree with the hashes assigned for this audit and with the packet's
`SHA256SUMS`. The comparison targets were the exact v2 statement and proof,
whose independently recomputed SHA-256 values are respectively
`147612fc96ddb973f5dd2df7ccc3da38798e3f3df46b462cd38b6cfaa9f1167b`
and
`e146c0eec6372995f881a3db054719969575515a913474a14d073ec17010627d`.
The v2 production response was reread at SHA-256
`9343e51748df7764fddf021ce2cee6ead02983b2931c95951bae7ad546a9c58c`;
its failed verdict was used only to locate the rejected endpoint material.

## Exact v2-to-v3 diff audit

The complete unified diffs of statement against statement and proof against
proof were inspected. They contain exactly the following changes.

1. The quarantine header comments identify v3 and its strict-open scope.
2. The statement deletes the annulus sentence that asserted closed and
   half-closed variants from an equation on the absolute analytic interior.
3. The statement deletes the analogous closed/half-closed polycylinder
   assertion.
4. The statement adds a purely negative scope firewall: all three assertions
   concern strict open standard domains, and no conclusion is asserted for a
   closed or half-closed domain, a non-strict endpoint, or merely from a
   current equation on an absolute analytic interior.
5. The annulus proof deletes its final sentence claiming all closed and
   half-closed variants by restriction and continuity.
6. The polycylinder proof deletes its final paragraph falsely identifying the
   absolute analytic interior with the coordinatewise open polycylinder and
   using density and continuity to obtain endpoint variants.

Apart from the changed quarantine comments, those four deletions, and the
negative scope firewall, every retained mathematical byte of the strict-open
statement and proof is identical to v2. In particular, no replacement
endpoint argument or new positive implication was inserted.

Exact-string searches also confirm that v3 contains none of the four rejected
formulations: `The same conclusion holds`, `The same assertion holds`,
`Restriction to the absolute interior`, or `continuity proves the endpoint
variants`.

## Semantic scope audit

- Every hypothesis in the three frozen assertions uses a standard strict open
  disc, annulus, or polycylinder, with strict displayed inequalities.
- The words `target closed disc` in the annulus proof describe only an
  auxiliary Gauss boundary point used inside the retained strict-open annulus
  argument. They do not assert a zero-current theorem on a closed source
  annulus or polycylinder.
- The phrase `common, order-independent endpoint` in the polycylinder proof
  means the endpoint of successive coordinate replacements at a radius vector
  lying in the open radius rectangle. The following paragraphs explicitly
  identify it with the multivariate Gauss point on the open polyannulus; it is
  not a boundary-radius assertion.
- The explanatory phrase `no endpoint at T=0` distinguishes an open annulus
  from a disc and does not extend the theorem to any non-strict endpoint.
- The scope firewall is grammatically and logically a denial of endpoint
  conclusions. It cannot be read as a theorem for closed, half-closed, or
  absolute-interior domains.

Thus neither rejected endpoint assertion survives explicitly or implicitly.

## Dependency closure

Deletion of the endpoint claims strictly reduces the dependency burden and
introduces no new mathematical dependency. The retained dependency graph is
unchanged from the strict-open core of v2, which the production response
expressly reports as passing sequential and reference checks.

- Every theorem-like cross-reference is either internal to the two frozen
  files or one of the three materialized verified dependencies
  `prop:p062-rational-centred-traces`,
  `prop:p062-finite-flat-continuous-trace`, and
  `prop:p062-arbitrary-field-disc`.
- Every `\eqref` target is defined in the frozen statement/proof pair.
- The only explicit citation key in the pair is `CLD25`, and it is supplied by
  the minimal wrapper. The retained external uses and their precise scopes are
  recorded in the v2 source matrix; none is changed by v3.
- The statement's regularity consequences, the split-torus calculation, and
  the local rigid-density step are unchanged retained consequences already
  included in that dependency ledger. The negative scope firewall needs no
  source.

No undefined dependency, circular use, or deleted endpoint premise remains.

## Fresh independent compilation and visual check

The three source files were copied without modification to the fresh directory
`/private/tmp/p062_v3_exact_audit.THYTzq`. The minimal wrapper, SHA-256
`73d8dbeb3056f697580581470672734f8d5f811ac97aac801372e73667759e3b`,
was compiled there with
`latexmk -pdf -interaction=nonstopmode -halt-on-error`. Latexmk performed
three `pdflatex` passes and exited with status zero.

The final log contains no warning, undefined reference, undefined citation,
overfull box, underfull box, fatal error, or LaTeX error. The independently
produced PDF has eight A4 pages and SHA-256
`40394b423b9c4f32792dae4e326b45e0c4b463adf939cbe983957d753a5d6270`.
All eight pages were rendered at 110 dpi and inspected: the statement, scope
firewall, proof transitions, equations, citations, page breaks, margins, and
final bibliography are legible, with no clipping, overlap, black boxes, or
missing glyphs. The frozen statement and proof retained their assigned hashes
after the build.

## Verdict

**PASS: zero critical errors and zero unresolved gaps.**

This receipt verifies the exact strict-open narrowing and dependency closure;
it is not a production Rethlas verdict. The packet must remain quarantined
until these exact frozen bytes receive a fresh production verification.
