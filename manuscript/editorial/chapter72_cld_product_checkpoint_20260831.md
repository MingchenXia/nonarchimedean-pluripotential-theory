# Chapter 72: product-case CLD progress — 31 August 2026

This supplements, and does not rewrite, the frozen comparison checkpoint.
The comparison proofs and P14.7/P14.8 source corrections were committed and
pushed in `1c3e36f88bf8b4f955349628a80d3491c4b975ef`. This checkpoint records
the next independently reviewed mathematical step. **P21.3 remains open.**

## What the new proof establishes

Let K be complete discretely valued with perfect residue field k. Let C
have a smooth proper model with geometrically connected fibres, and let
X be the product of its analytification with the standard open annulus
|pi|<|z|<1. For an actual positive closed ordinary CLD current T of
bidegree (0,0), the proof constructs a finite nonnegative coefficient b_T(p)
on the individual outer collar of every closed point p of the special fibre.
For every residual rational function f it proves

\[
 \sum_p\operatorname{ord}_p(f)b_T(p)=0,
 \qquad b_T(p)=c[\kappa(p):k]\quad(c\geq0).
\]

This supplies the analytic current-to-divisor-functional interface in this
product setting. It does not merely assume the principal-divisor relation.
The argument uses legitimate compactly supported source forms and accounts
for residual-order-zero tubes containing deeper cancelling zeros and poles.
The finite coefficient-field degree is a calibration factor, not a number
of ordinary analytic sheets. The proof's degree-two and nonprimitive-coordinate
diagnostics check that distinction explicitly.

The construction and principal relation do **not** assume the earlier
source-representation packet. Only the final interpretation as ratios of
source-cell calibrations assumes that separate statement. Equality of these
collar ratios is not yet equality of the currents on the whole product.
Neither a full scalar-rigidity theorem nor general higher-dimensional
Bedford–Taylor independence follows from this packet alone.

## Independent review and exact bytes

All paths in this section are under `solver_dossiers_20260831/`.

- Candidate: `p213_residual_curve_functional_interface_research_20260831`.
  Statement SHA-256: `5ad73a96dd4e41296003e2824711cf7d6301aa489fdc67ed11a2158682d135fc`.
  Proof: `209ce1db0b33f460952e7c423c09baa58ab2f6cdc14a3d55b9310ddcbde9b224`.
  Manifest: `175b64dfd4e08ad59dcb561928ab50172194e04af264c4641b49c8dcc0359278`.
- Independent audit:
  `p213_residual_curve_functional_interface_independent_audit_20260831/INDEPENDENT_EXACT_BYTE_AUDIT.md`.
  Report SHA-256: `177d0ca3454b6f73caedf81fe4eaa34f674a712460ace16409b36115892f2359`.
  Verdict: no substantive gap found in the exact displayed product scope.
- Draft check: `p213_residual_curve_functional_draftcheck_20260831`.
  Manifest SHA-256: `d4f5a7653dc06fdad87ba7d342cb5ce268ff6b469ca77f6abf90be15c6e8db76`.
  Three draft-mode TeX passes and BibTeX completed with no final error,
  undefined reference/citation, or box warning. Five labels and six internal
  references resolve. No PDF was produced.

Root read the complete proof, source interface, independent report and
source ledger; all 16 audit checksum entries matched. The read-only draft
checker also confirmed all four direct inputs, 13 parent-manifest entries,
and 15 local-manifest entries. These mechanical checks are not mathematical
verification. The frozen candidate's original pending-audit status is
historical; the separate later audit records the outcome without changing
its bytes. Production Rethlas review remains pending.

## Points to retain in an eventual pedagogical integration

Explain the completed local ring and unramified coefficient field before
constructing a collar. Derive its constant coefficient by distributional
derivatives, then construct the rational lift and source cutoff. Retain the
signed boundary integral, the degree-two residual point, and the hidden
zero/pole cancellation example. Do not replace this sequence by a citation
to the GRW slope formula: that formula does not construct the functional of
an arbitrary current here.

The independent audit clarifies one support point: at the central Gauss
locus, equality v(F)=0 need not imply ordinary local constancy. Instead,
chi' vanishes near zero, and continuity of v(F) supplies the ordinary-open
neighbourhood on which the differentiated test vanishes. Include this
explanation in any integrated proof.

Use roman exponential constants at frozen proof lines 46 and 171, and
roman imaginary constants in the degree-two example. The exponent variable
e in the nonprimitive-coordinate example remains a variable, not the
exponential constant. Preserve equation references as `eqref` and use
`cref` for proposition/section references. These future typography changes
must not be silently applied to the reviewed frozen source.

## Next interfaces, not proved by this checkpoint

1. Extend the actual-current relation to an annular torsor of a nontrivial
   line bundle, tracking normal-bundle transitions and metric curvature.
2. Determine what source-chart separation is needed to deduce equality of
   currents from the product collar ratios.
3. Address general semistable neighbourhoods, arbitrary complete fields,
   and positive current bidegrees; these are not consequences of either
   proposed interface without further proofs.

The first two are being investigated separately. No unfinished follow-up is
included in the frozen product verdict or used to retire an inventory item.
There are still 51 administratively active entries in 14 environments, with
the literature-covered/project-verification-pending and underspecified
entries distinguished as in the preceding checkpoint. No new live theorem
or chapter PDF was generated by this step.

## Targeted literature recheck

On 31 August 2026 the primary arXiv records still list
[MP v2](https://arxiv.org/abs/2409.06221) and
[DXZ v3](https://arxiv.org/abs/2302.02541) as their latest versions.
The already-cited
[Mesquita-Piccione–Witt Nyström preprint](https://arxiv.org/html/2509.09442v1#S2.SS2)
states its inverse ray construction in Proposition 2.2.2 for finite-energy
potentials. This passage alone does not assert the full raw all-point
comparison developed in the separate research packets. This targeted check
is not an exhaustive priority search or an independent audit of that paper.

No production call, endpoint change or permission workaround was attempted.
The preservation record accompanying this checkpoint identifies exactly
the new research, independent audit and draft-check files copied to the
durable private project. Earlier packets and unrelated work are untouched.
