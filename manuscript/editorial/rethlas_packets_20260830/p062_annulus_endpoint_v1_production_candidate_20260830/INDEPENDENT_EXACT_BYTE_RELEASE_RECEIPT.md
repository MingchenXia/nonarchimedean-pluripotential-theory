# Independent exact-byte release receipt

Date: 30 August 2026

Audit scope: the frozen one-dimensional annulus endpoint candidate only.
No production Rethlas call was made and no live-book file was edited.

## Verdict

**PASS.**  The exact statement and proof below implement every precision
condition from the predecessor hostile audit and are ready for a new
dependency-closed production Rethlas verification.

This receipt verifies no product, polycylinder, or higher-dimensional
endpoint assertion.

## Exact frozen bytes

- statement:
  `p062_annulus_endpoint_statement_20260830.tex`;
  SHA-256
  `a54723f040926d5a309494bb77d3c734c1c9d27bfb9fd18c56fc70ea4d03c9e1`;
- proof:
  `p062_annulus_endpoint_proof_20260830.tex`;
  SHA-256
  `461afad5804a3269cb385550af6f4abcb5543d4f3151db56f986490c74e6947e`.

Both hashes were recomputed independently and agree with `SHA256SUMS`.

The exact predecessor independent audit is
`../p062_annulus_endpoint_only_dossier_20260830/INDEPENDENT_HOSTILE_AUDIT.md`,
SHA-256
`02f11da24f3003d489d7a8c64157a813a9c8c97e52ce28996e8ea011d13dc297`.

## Scope check

The proposition treats exactly three one-dimensional domains in
`(G_m,K)^an`:

```text
{r<|T|<=R},  {r<=|T|<R},  {r<=|T|<=R}.
```

It retains all required hypotheses: `K` is complete, its absolute value is
nontrivial, `0<r<R`, and `r,R in |K^x|`.  The equation is assumed on the
absolute analytic interior and the conclusion is only

```text
h=a log|T|+b.
```

The words `product`, `polycylinder`, and `higher-dimensional` occur only in
the explicit scope firewall.  The proof has one coordinate, one annulus, and
one polynomial tube.  No product-slicing statement, multivariate Gauss
section, or higher-dimensional conclusion appears.

## Verification of the three required repairs

1. **The closed tube is exact.**  The proof states

   ```text
   bar(X)_y={|P(T)|<=S}={|T|<=s}.
   ```

   The coefficient inequalities justify this equality: below `s` the
   constant term has norm `S`, at `s` every term has norm at most `S`, and
   above `s` the monic leading term strictly dominates.  The resulting
   closed disc is used only as the compact source of the finite polynomial
   map.

2. **There is no closed trace of an undefined function.**  The proof
   explicitly refuses to extend `h` to `bar(X)_y\A`.  For each `q<S`, every
   point over the target Gauss point `xi_q` has `|P|=q<S`, hence belongs to
   the open tube `X_y subset A`.  The endpoint limit is instead obtained as
   follows: the complement of a neighbourhood of `eta_s` in the compact
   closed source has closed image under the finite map; the singleton fibre
   over `xi_S` keeps `xi_S` out of that image; and `xi_q -> xi_S` forces all
   fibres into the neighbourhood.  Continuity of `h` on the subspace `A`
   and total calibrated fibre degree `d` then give

   ```text
   H(xi_q) -> d h(eta_s).
   ```

   Every evaluation of `h` is therefore inside its stated domain.

3. **The unnecessary branch claim is removed.**  The proof uses only that
   `X_y={|P|<S}` is ambient open in the analytic torus and contained in the
   endpoint circle, so `X_y subset Int(A)`.  It explicitly says that no
   assertion placing the entire tube in one specified virtual-disc branch is
   needed.  No connectedness substitute is introduced.

## Remaining mathematical checks

- The BPR result is used only under its algebraically closed field
  hypothesis; Ducros supplies the arbitrary-field virtual-disc topology.
- Berkovich's relative-interior result is composed through the boundaryless
  analytic torus, so the current equation applies on the ambient-open tube.
- The polynomial map on the open tube is the base change of a finite free
  degree-`d` morphism.  Its zero fibre is the single rigid point `y`, with
  calibrated degree `d`.
- After normalizing by an element of norm `s`, the residue polynomial has
  degree exactly `d`.  The rational-function residue extension therefore has
  degree `d`, including inseparability.  The graded fundamental inequality
  and the total-degree formula prove that the target boundary Gauss fibre is
  exactly `{eta_s}`, of local degree `d`.
- Constancy of the production-verified open-disc trace compares `h(y)` with
  `h(eta_s)`.  The strict-open annulus theorem fixes the skeletal formula.
  Rigid density within every ambient-open nonskeletal endpoint branch and
  continuity extend it to all endpoint points.  The endpoint Gauss points
  were already handled by skeletal continuity.
- Since `r<R`, the skeletal coordinate `log|T|` is nonconstant and the two
  coefficients are unique.

No circular use of the desired endpoint theorem, no scalar pullback of a
continuous current, and no value-group or separability assumption absent
from the statement was found.

## Independent compile

The three exact source files (statement, proof, and minimal wrapper) were
copied to a fresh directory
`/private/tmp/p062_endpoint_reaudit.MQ2OXs` and compiled independently with

```text
latexmk -pdf -interaction=nonstopmode -halt-on-error
```

The build converged after two pdfLaTeX passes and produced a four-page PDF.
The final log contains no undefined reference, undefined citation,
multiply-defined label, overfull-box, underfull-box, or TeX error warning.
The independently built PDF has SHA-256
`230b890d5ea232c504e1e9edf0ae262e30c690d6264a8d0b1084f4f976f4f97e`.

## Release decision

The exact statement/proof pair named above passes independent release audit.
Only those exact hashes are covered.  Any mathematical edit requires a new
independent exact-byte audit before production submission.
