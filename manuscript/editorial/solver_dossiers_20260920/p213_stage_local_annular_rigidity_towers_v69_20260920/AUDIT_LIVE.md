# Audit: stage-local annular rigidity over intermediate tower bases

Date: 20 September 2026

## Scope and claim boundary

This packet proves a new P21.3 subcase.  A finite tower starts from a
residual-Picard curve.  Each stage is either one of the four already treated
exact bundle types or an analytically locally trivial finite standard strict
open-polyannulus bundle.  At an annular stage, every member of a chosen
trivializing cover is required to have the two rigidity properties actually
used by the proof: continuous zero-current functions are classically
pluriharmonic and ordinary CLD-smooth with zero smooth Hessian, and adding
vanishing of the first current forces local constancy.

The conclusion is ordinary CLD smoothness with zero smooth Hessian on the top
space, followed by the whole-space, specified-cover, and every-open-basis
Bedford--Taylor consequences.  Annular charts may occur at arbitrary tower
levels; their radii, coordinates, and trivializations need not agree on
overlaps.  No global logarithmic coefficient formula is asserted.

This is strictly stronger than the preceding common-cover tower theorem,
because the annular charts need not be pulled back from the original curve.
It does not prove that the two required rigidity properties pass from an
intermediate whole space to every ordinary open subset.  Consequently it
does not cover an arbitrary locally trivial annular stage and does not retire
P21.3.  The inventory remains at 46 active atoms.

## Proof ledger

1. On each annular product chart, the established rigid-base product theorem
   writes a continuous zero-current function as a pullback of a base
   zero-current function plus locally constant slopes times logarithms of the
   annular coordinates.  It also supplies classical pluriharmonicity.
2. The stage-local hypothesis makes the base coefficient ordinary
   CLD-smooth with zero smooth Hessian.  Pullback functoriality, logarithmic
   smoothness for invertible analytic functions, and multiplication by the
   locally constant slopes give the same conclusion for every term of the
   chart formula.
3. Ordinary CLD smoothness and vanishing of the smooth Hessian are local, so
   the chartwise conclusions glue without any compatibility assertion for
   the displayed annular formulas.  The rigid-base theorem also transfers
   first-current rigidity.
4. On the residual-Picard curve, Wanner's harmonicity theorem supplies
   classical pluriharmonicity, the residual-Picard criterion supplies
   ordinary CLD smoothness with zero smooth Hessian, and the curve lemma
   supplies first-current rigidity.
5. Induct through the tower.  A length-one use of the mixed exact-bundle
   transfer handles each exact stage; the new stage-local proposition handles
   each annular stage.
6. The established smooth-zero-Hessian comparison gives Bedford--Taylor
   invariance on the whole top space.  Applying the tower theorem on the
   displayed cover, and then on a basis subordinate to it, gives the two
   localized forms.

## Scope firewall

- Whole-space rigidity on an intermediate base is not claimed to be inherited
  by all of its ordinary open subsets.
- No arbitrary locally trivial annular stage is admitted without the stated
  chart-base hypotheses.
- No compatibility of annular coordinates or slopes is used.
- No global logarithmic normal form is claimed.
- The full P21.3 problem remains open.

## Model-backed verification history

- Initial packet: verdict `wrong`, 0 critical errors and 1 gap.  The sole gap
  requested the exact Wanner theorem statement used at the residual-Picard
  base; no mathematical contradiction was reported.  Checked item:
  `pi_198d529bfc3a8b4ae2054da3`.
- Dependency-completed packet: verdict `correct`, 0 critical errors and
  0 gaps.  Checked item: `pi_5780d7e9efe59708af7868e9`.
- Exact final packet, after two grammatical corrections and with bytes
  identical to the live statement and proof: verdict `correct`, 0 critical
  errors and 0 gaps.  Checked item: `pi_dce25a9039e4769b5a3344fc`;
  proof digest
  `e058e97f86a7506683b7893e9633edcaadebd3c8efb094b03851e4ff4d7ab9c3`.

The request, response, and HTTP-header records for all three runs are retained
beside this audit.  The exact-final response has HTTP status 200 and final
verification status.
