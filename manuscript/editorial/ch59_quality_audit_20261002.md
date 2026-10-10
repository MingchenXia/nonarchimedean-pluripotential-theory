# Chapter 59 completion audit

Date: 2 October 2026

Base: local Chapter 58 commit `71dff7d`.

Scope: `parts/part5/ch59_complex_dual_complexes.tex`, under the sequential
quality programme. Chapter 60 is next; the whole-book goal continues.
Independent Chapter 72 research remains paused. Frozen receipts are preserved.

## Mathematical and expository review

The complete source, seventeen formal assertions and twelve examples were
reviewed. Every assertion has its proof and explicit source interface.
All 33 reusable environments have semantic labels; there are eighty labels.
The six numbered sections, six new model subsections and source note are
labelled. The long model section now exposes the order of flag evaluation,
Cartier correspondence, density, retraction and inverse limit.

The principal checks and repairs are:

- PL density reuses Chapter 58's ideal-product and difference identities.
  The uniform closure is explicitly a real vector lattice; rational PL
  functions themselves are dense, as needed for closed-set separation.
- Integral closure uses global finite reduction before any cancellation,
  includes infinite values and retains the normal proper blowup formula.
  The finite divisorial test keeps local branches and includes nonexceptional
  divisors, units, zero ideals and dimension zero. The projective-plane
  calculation verifies its missing integral generator and exact reduction.
- The Stein interface retains finite presentation, excellent compacta and
  proper coherent support. Bingener's dimension assertion is separate from
  existence of analytification. Its local blowup is now a labelled example,
  with an explicit range of codimensions and the invertible-ideal case: the
  fiber over the point is not called exceptional when the blowup is identity.
- Monomial globalization keeps coefficients as germs at zero weights,
  coherent intrinsic filtrations, intersection components, finite minimal
  supports and the terminating ordinary-blowup construction with its scalar.
  The local vertical restriction keeps the residual-transcendence-degree
  argument over excellent analytic rings. Global realization extracts centers
  directly over the central fiber, rather than using a modification of X on
  every fiber. Central multiplicities remain in normalized orders.
- Flag evaluation and vertical Cartier correspondence retain finite Gauss
  values, integral-closure cancellation, signs and rational denominators.
  Kernel injectivity precedes divisorial density. The surjectivity argument
  constructs a vertical relatively ample divisor and uses finite compact
  generation bounds on projective germs; no global meromorphic function
  field for a nonalgebraic manifold is substituted.
- Retractions use the finite closed-stratum ideal embedding, including
  repeated intersection components and proper-support characters. Their
  transition matrices keep the component label. The inverse-limit proof
  uses compact fibers and the finite intersection property. Point approximation
  is a model-indexed net, separate from uniform function sequences.
- Discrepancy keeps the exceptional boundary hypothesis, logarithmic
  Jacobian bound, rational realization, continuous real cone comparison and
  normalized total-model envelope. Gauss values include every positive
  rational factor and the trivial valuation. The repeated point blowups
  supply an explicit character of infinite reduced discrepancy.
- The entropy warning now gives the exact shift for any positive finite
  measure: its mass, not an implicit unit. Nonnegative extended integrals
  make the formula valid at infinite entropy. A new curve example checks
  finite atoms, scaling, zero mass, the infinite atom and its zero-weight
  endpoint without subtracting infinite quantities. The nonprojective torus
  and K3 calculations retain their source and ideal-character scope.

The eight dated Chapter 59 unit audits remain historical evidence for their
identified revisions, not new independent receipts for this chapter.

## Direct source interfaces

Eight primary PDFs and 47 rendered source pages were directly inspected.

| Source and version | Principal interfaces | Physical pages inspected |
| --- | --- | --- |
| Mesquita-Piccione, arXiv 2409.06221 v2, 18 September 2025 | Monomial globalization, equivariant models, divisor restriction, flags, PL correspondence, density, inverse limit and total discrepancy/entropy | 16--18, 20, 22--32, 51 |
| Jonsson--Mustata, published AIF 62 (2012) | Monomial coordinates and zero weights, exceptional-boundary convention, relative Abhyankar/divisorial criterion and discrepancy | 23--25, 29--30, 36--38 |
| Boucksom--Hisamoto--Jonsson, published AIF 67 (2017) | Restriction, Gauss extension and invariant divisor realization | 41--43 |
| Xia, Stein spaces, snapshot dated 3 July 2026 | Excellent singleton, relative analytification, proper coherent algebraization, closed subspaces and morphism germs | 157, 185--186, 232--237 |
| Bingener, author-hosted retyping of the 1976 text | Aussage 2.8, its proof and nonproper counterexample | 12--13 |
| Mesquita-Piccione--Witt Nystrom, arXiv 2509.09442 v1 | Definition 2.4.1: reduced entropy | 13 |
| Boucksom--Jonsson, published AFST 31 (2022) | Appendix A, normalized weights, Theorem A.1 and Lemma A.2 | 181--183 |
| Lejeune-Jalabert--Teissier, published AFST 17 (2008), Numdam PDF | Analytic integral-dependence, coherent closure and finite divisor tests | 20, 25--26, 33--34 |

PDF SHA-256 values, in that order:

1. `9eb2ea7686a5962ebc11c5eacd23b0cb3dcb081e27ac48292933f291fc82cb23`
2. `b0360dbfeb5b19601500e3ed03e8b186f4ac84b6c771a2a300fe25efa0d5fb57`
3. `edfd3b1506b49cf42ae85014d731bd9d86af5ed248134397cd562fba70c6f60e`
4. `a205506763db45f0ad2ab38b788e69a9d5b1eac56c8db7b84e01c6a94f81b26e`
5. `5e66a0f1eabddd6c9d805c30a5fa4a51e9d98d7da80a12b6e6813dfc6c5eb124`
6. `54c7f7e75bc9869f979fff2c2e0e56079660a408cc18d2df95d327dff01b7464`
7. `50bd6e6782c29088edc96d013a5d49257b0395d9fb398664f1a9859639992948`
8. `f580565e97b7b7c3f08e106bdabe3ba2b29487411ad8f58e02e6f5b6f1a2c406`

The Numdam delivery of the last article has different PDF bytes from the
publisher delivery identified in the dated audit; its inspected printed
statements and locators agree. Source files and older checksums are preserved.
Four Stacks statements and proofs were read from fresh HTML: Tags 031T,
0C4K, 0892 and 01Q3, respectively normal height-one intersections, composition
of relative ampleness, its finite-section proof and eventual generation.
Their hypotheses are applied through the projective-germ equivalence.
HTML SHA-256 values:

1. `60ca68ba7864eb7885f7d8525b4f2071ec88f04d8e2c2bcb310ab7c23c9f46dc`
2. `441e44c5d503eedd1cfb8540b8704108838daa9c52b7bc5fdbe3f90f9f97b335`
3. `e3f876a9219fe22371d04c1373ef07f3663aa736ddf37dc1297c4cff02dd3be0`
4. `5211e2d8b963df3ecf95b8c2ab886b59f05e30786833a5a7457cbe6076e8df7d`

The K3 existence/Kahler inputs retain their preceding exact-source audit;
the Siu PDF endpoint returned HTTP 403 in this pass, so no fresh inspection
of that PDF is claimed. Exact-version author locators remain separate from
the published Mesquita-Piccione entry. No bibliography changes are needed.

## Verification and rendered review

The exact rational/integer supplement passes 15,136 checks: the integral
reduction and Newton values, primitive blowup descent and monomial weight
preservation, finite flags and twists, normalized transition matrices,
repeated-edge separation, K3 ideal/discrepancy values, Gauss normalization,
finite-mass entropy and point-supported truncation vertices. These check
calculations, not the analytic or geometric imports.

Scoped checks before and after rendering find no unlabelled reusable
objects, proofless assertions, duplicate labels, nesting errors, legacy
inline delimiters, double-dollar displays or TODO/FIXME/TBD markers. The
proof-adjacency check recognizes the existing minipage around the Cartier
proposition; its proof follows that layout wrapper. The legacy writing-audit
executable is unavailable; its warning counts are not claimed. References
pass for 425 inputs and 12,160 labels. All six regression tests pass. The
inventory remains 42 atoms in twelve environments, tiers (0,3,7,15,17).
Post-render scoped and reference checks and `git diff --check` pass.

The full workspace-local TeX Live 2025 latexmk build succeeds. Final PDF:
4,126 pages, 19,265,823 bytes, SHA-256
`fb9997aaf563f318c5aca92eda7e24b286161057f52ebb3779c3fab8f4273cc1`.
Final chapter source SHA-256:
`02a7392e365792a64a5710a39c8989ec82cb8a3614fc8e12355980012d4d3ee2`.
There are no unresolved references or citations, missing glyphs, rerun
requests or fatal errors. Chapter 59 has no overfull boxes or LaTeX/package
warnings. Nineteen overfull boxes elsewhere and thirteen duplicate PDF
destinations in Chapter 70 remain recorded.

All thirty physical chapter pages 3165--3194 (printed 3095--3124) and
both adjoining seams were inspected at detail size. Physical page 3194 is
intentionally blank. No reviewed clipping, overlap, bad glyph, formula
overflow or hierarchy defect remains.

This is a direct editorial/source audit, not an independent-agent verifier
verdict. Generated PDFs remain local review artifacts. Frozen releases,
checksum ledgers and research atoms are unchanged. Verified work remains
local pending explicit remote-push approval.
