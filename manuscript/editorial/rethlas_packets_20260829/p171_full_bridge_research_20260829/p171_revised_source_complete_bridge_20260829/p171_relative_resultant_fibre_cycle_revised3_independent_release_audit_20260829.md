# P17.1 relative resultant/fibre-cycle revised3 independent release audit

Date: 29 August 2026.  Scope: quarantined P17.1 research module; no live-book
integration is certified by this receipt.

## Verdict

**PASS.**  The revised3 mathematical statement and proof differ from the
independently audited revised2 bytes only in seven theorem/corollary
cross-reference commands (`\ref` to `\cref`).  The harness adds `cleveref`
with the live-book option set and updates only its revision marker.  No
formula, hypothesis, label key, citation, proof step, or theorem environment
was changed.

## Mathematical audit inherited under byte invariance

The independent revised2 hostile audit checked and passed the following
load-bearing points, all of which are byte-identical in revised3:

- the cycle computation is made on the finite-type ambient scheme before
  localization; Stacks Tag 02RA is used only for finite-type flat/open maps,
  and Tag 02TB supplies the height-one localization step;
- successive Cartier cuts, the final line-bundle quotient, proper
  push-forward, generic local lengths, and residue-field degrees give the
  claimed fibre cycle, including nonreduced and nonpure fibres;
- the complete fibre over the original Banach ring is formed before affine
  substitution over the residue field, so no norm chart or projective map is
  pulled through a coefficient specialization with kernel;
- both complete and substituted rank-one, dimension-zero cases are treated
  separately;
- finite and imperfect residue fields, exponent one, positive norm
  orientation, scalar normalization, and one-stage descent were checked;
- arbitrary base change is asserted only for the intersection line, using
  Stacks Tag 0B91; the optional Ducrot section-base-change lemma is not used.

## Cross-reference and build gates

The revised3 statement contains one `\eqref`, one `\cref`, no bare `\ref`,
and no optional theorem heading.  The proof contains nine `\eqref`, six
`\cref`, no bare `\ref`, and no optional theorem or proof heading.  Thus the
combined release count is ten equation references, seven clever references,
zero bare references, and zero conventional optional theorem names.

An isolated two-pass build produced five pages with no final warning,
undefined reference, duplicate destination, or box error.  All five pages
were inspected.  References render as “Theorem 1”, “Theorem 2”, and
“Corollary 3”; there is no clipping, overlap, broken glyph, unresolved marker,
or pagination defect.  Extracted text agrees with the frozen revised2 PDF
apart from the harness revision number.

## Exact hashes

```text
afc63819afda47bee2214268d1d9be9a1cf4d4020c3f7fbf5552e7973e052baf  p171_relative_resultant_fibre_cycle_statement_revised3_20260829.tex
fba3810153c0e5440a1caf0f56c34035ae9bb80b36857b9c7012f00edc51dc03  p171_relative_resultant_fibre_cycle_proof_revised3_20260829.tex
e865814f7d6fab39836ba62175ada70d86fdedc15a893a1fc3f0535bbc281573  p171_relative_resultant_fibre_cycle_compile_revised3_20260829.tex
df1e113e7dffcc9050c43de157c7d568b0ef588bcf6e227bc94b121f36db4863  p171_relative_resultant_fibre_cycle_compile_revised3_20260829.pdf
bfd3299c3f9694afc31a01a901fd01ec6c1824172306f423a53265381c80b292  p171_relative_resultant_fibre_cycle_compile_revised3_20260829.log
```

Release gate: cleared for production Rethlas submission as a scoped module.
The full P17.1 bridge remains open until every dependency and the assembled
comparison have separately passed production verification.
