# P17.1 powered normalization/CLN revised6 independent release audit

Date: 29 August 2026.  Scope: quarantined P17.1 research module; this receipt
does not certify the assembled bridge or authorize live-book integration by
itself.

## Verdict

**PASS, scoped and conditional.**  The exact revised6 source has SHA-256
`d4b105483ada85492bfe803790953fe50f6fa9e4c42c656ed7776bd48ba9ce71`.
The two mathematical blockers found in revised2 are closed, the later
cross-reference and typography-only revisions preserve the audited
mathematics, and no remaining internal proof gap was found under the module's
declared inputs.

## Mathematical gates

- The power function separates the non-Archimedean and powered Archimedean
  loci.  Metric unpowering is derived from Pille--Schneider Proposition 3.2,
  and the resulting differential-operator formula is honestly described as a
  source-forced unpacking rather than verbatim source notation.
- PN1 retains the fundamental-cycle generic lengths and uses the real
  push-forward convention.  The dimension-zero metric constant is obtained
  from Boucksom--Eriksson formula (8.11); Example 8.2 contributes exactly
  `m_j[K_j:K]`, formula (8.12) checks the frame law, and Remark 8.1 excludes
  an extra real factor two.
- PN2 states frame compatibility, symmetry, multilinearity, the dimension-zero
  base case, restriction recursion, and uniqueness.  The Philippon harmonic
  correction acquires one power factor and an `e^Q` frame change gives
  `-Q log|u|`.
- The CLN statement requires continuous psh-regularizable semipositive pairs
  in every slot, explicitly including slot zero.  Its smooth proof swaps only
  the Monge--Ampere slots; the extension approximates all `2(n+1)` metrics.
  The case `n=0` has constant zero.  No arbitrary continuous test is inserted
  into this estimate.
- The endpoint family argument starts from FS pairs in every slot.  In the
  product net, CLN is used only with the DFS pair `(alpha_q,beta_q)`; the
  arbitrary limit test is controlled by common mass.  Cofinality begins with
  an arbitrary ambient index and assumes neither a sequence nor a uniform
  bound on the constants `C_q`.
- The weighted Philippon--Gauss endpoint and frame law are imported from the
  separately production-verified exact fragments; the focused reconstruction
  in this module is not called an exact-byte replacement for that proof.

## Source, reference, and typography gates

The final source has 31 `\eqref`, eight `\cref`, no bare `\ref`, and no
optional theorem/lemma/corollary names.  Its sole explicit integration
differential is `\,\mathrm d\eta`.  Relative to the mathematically audited
revised3 source, later revisions make only the internal-reference migration,
the upright-differential repair, revision metadata, and terminal-newline
normalization.  The final file ends exactly in `\end{document}\n`.

The independent production-statement audit also passed.  The packet has
SHA-256
`f79967685839fe37c6b3819936f131a196b1ea75733c56ff609e5cd850c1eeff`;
every claim is present in revised6, no conclusion is broader, all CLN and
finite-level-continuity conditions are explicit, and all scope caveats remain.

## Build and visual gates

The forced two-pass build produced ten pages.  The PDF SHA-256 is
`1b2edf3fcb22c66a1cae5de33423d8e97731638a4edb75d867ed275a19e18c01`.
The final log has zero LaTeX/package warnings, undefined or multiply-defined
references, overfull/underfull boxes, or duplicate destinations.  All ten
pages were rendered and inspected; the upright differential is correct and
there is no clipping, overlap, missing glyph, unresolved marker, malformed
reference, or new layout regression.

## Remaining external gates

1. The differential-operator transport is a source-forced convention
   unpacking, not verbatim notation from the cited sources.
2. The product-net conclusion assumes finite-level fibre-integral continuity.
3. The relative resultant tensor and fibre cycle are a separate production
   module.
4. The local-frame synchronized resultant/Chen--Moriwaki/PN2 comparison is not
   proved in this module.  Consequently P17.1 remains open at the assembled
   comparison gate.

Release decision: cleared for scoped production Rethlas submission only.
