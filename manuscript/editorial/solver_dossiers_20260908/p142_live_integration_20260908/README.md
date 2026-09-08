# P14.2 live-integration ledger — 8 September 2026

## Scope and status

This ledger records the live integration of the P14.2 candidate, the
upper-semicontinuity problem for the raw ideal-valuative transform.  It is
an integration and assembly record, **not** a retirement record.  P14.2 must
remain active in the Chapter 72 inventory until a production verification
returns `correct` with no critical errors or gaps, as required by that
inventory's retirement rule.

The live theorem is in Chapter 71, subsection *Upper semicontinuity from
finite ideal data* (source lines 608--930).  It proves that, for a decreasing
family of quasi-psh levels,

\[
 F_\Gamma(v)=\sup_{\tau<c}
 \{\tau-\nu_v^{\mathcal I}(\Gamma_\tau)\}
\]

is upper semicontinuous at every semivaluation of the tropical spectrum,
including those with nonzero support.  It also gives a decreasing sequence
of bounded, real-valued, continuous finite-ideal expressions converging to
the raw transform.  It does **not** assert MP plurisubharmonicity,
semipositivity of the approximants, a Monge--Ampère construction, or an
identification of \(P\)- and \(\mathcal I\)-equivalence.  Thus it targets
P14.2 only; P14.3--P14.6 and P14.8 are unchanged.

## Inputs and local repair

The source-closed target was independently audited in
`p142_source_closed_production_release_repaired_independent_hostile_audit_v2_20260901`:

- verdict: `PASS`;
- static test suite: 163/163;
- hostile mutation suite: 14/14 rejected;
- audited statement/proof/example SHA-256 values:
  `cc3f5fbdc8f4a491ca6121c0c254a20f05a0bfb6da5d91f11d6ae6e406a40bc2`,
  `7f2ff066d1213107e5e4e4d6e3653016be3b0b5959205f689fa9131ae16a3dac`, and
  `7010c2a461de6f2ed1fb7c1f0170c6eaa8aed38b88492ea919f8b0c1eea49f6f`.

The durable independent mathematical re-audit at
`solver_dossiers_20260831/p142_raw_transform_usc_stable_independent_reaudit_20260901`
also passed all 267 frozen checks.  Its hostile checks explicitly cover the
extended-valued Fekete argument, multiplier-ideal subadditivity, continuity
of the finite expressions, inverse-system transitions, the finite-grid/dense
parameter argument, and the infinite-ideal-value example.

During live integration, the audited proof contained the typesetting fragment
`\mathbf Z_{>0}^2$`, which is outside math mode.  The live source repairs only
that delimiter to `$\mathbf Z_{>0}^2$`; this changes no mathematical token,
quantifier, hypothesis, assertion, reference, or citation.  It is the reason
the archival proof hash must not be represented as an exact hash of the live
copy.

## Live source and build evidence

At the end of the integration build, the relevant SHA-256 values were:

| path | SHA-256 |
| --- | --- |
| `parts/part6/ch71_pseudoeffective_mp_dxz.tex` | `749a376fe598e7a994bf5d1f2bc38de18b5b2deaea96c87ff87e38a52a5b8456` |
| `parts/part6/ch72_major_open_problems.tex` | `ae6431e05c3bb1659f5dcf327f1f833c77d5519ecc70c830af10d50f28406a7f` |
| `editorial/open_problem_atomic_inventory_20260824.md` | `a5bafcd673c93f4bfceeb876447ecc71acbf531fd00b3f266ae57d3d10096ee5` |
| `book.pdf` | `40662a204c7e8927ae2b79372bd6dc7e9daadb7899ec56d49a97b9182fa4c889` |

The command

```text
latexmk -pdf -interaction=nonstopmode -halt-on-error book.tex
```

completed successfully in `manuscript/`, producing a 3,516-page PDF.  The
final log has no LaTeX errors, undefined references or citations, duplicate
labels, or overfull boxes.  The P14.2 labels occur exactly once in the Chapter
71 auxiliary file.  Visual inspection of PDF pages 3253 and 3256 (printed
pages 3185 and 3188) confirmed that the new subsection, finite-grid displays,
corollary, proof, and example are legible and correctly paginated.

## Outstanding production gate

With explicit user authorization, the required isolated final-path smoke was
run once on 8 September from a disposable copy of the independently audited
source-closed release.  It reached the 310-second cache horizon, made exactly
one configured MCP wait call, returned the prescribed terminal marker, and
recorded no target, source-bundle, runtime, workspace, model-catalog, or
process-identity drift.  The raw stdout and receipt hashes are respectively
`13fcdc8a5fbba2333df7dd36e28aa6bd2ef6eced03c5353624482fbcbccc48f4` and
`f7f44164f2c02ac2134e5ef414ca1d5bba410c8b698c3a2eebec672ff46e7c6d`.

The smoke nevertheless returned `failed`, and therefore supplies no
production-verification verdict.  Its frozen stderr parser accepts only two
September-1 Codex diagnostic forms.  The current Codex executable additionally
emitted an unrelated SQL maintenance warning, analytics-delivery warning, and
recoverable response-stream retry.  The parser rejected the first unrecognized
line before it could certify the otherwise successful run.  This is a
verification-infrastructure incompatibility, not evidence against the P14.2
statement or proof; the stderr hash is
`93b43a00489c9589614c70d831b77ee7a82354e22bad555d530937849ed5d026`.

No weaker substitute, altered receipt, inventory mutation, or retirement is
authorized by this evidence.  A successor release must give these
platform-diagnostic cases a narrow, independently audited treatment and then
run a new final-path smoke and production verification of the unchanged pinned
P14.2 pair.  Until that succeeds, P14.2 remains active in Chapter 72.

## Chapter 72 status reconciliation

On 8 September 2026, Chapter 72 and the atomic inventory were aligned with
the live Chapter 71 theorem.  They now state that the audited candidate proves
upper semicontinuity at all semivaluations, while retaining P14.2 as an active
T3 atom because the required source-closed production verification is still
pending.  The update removes the obsolete assertion that no upper
semicontinuity is inferred, removes upper semicontinuity from the substantive
residuals, and leaves every active-atom and tier count unchanged.  The full
book was rebuilt successfully after this documentation-only reconciliation;
it neither relaxes a verifier condition nor changes the mathematical target.
