# Foundational model and capacity repair checkpoint

31 August 2026. Editing base:
`4ec9fb514e9d33d0f8e1b6d918d6264a104cb676`.
This is a proof-repair/research checkpoint, not a verified textbook release.

## What changed

The completed nine-chapter syntax review was revalidated, then the
real-model maximum defect was investigated against the exact primary BFJ
source and the book's own D_R definition. The following replacements are
isolated; they are not inserted as established mathematics in live chapters.

1. **Chapters20/21.** Real theta-nef model functions need not be closed
   under maximum. An explicit rational-point blowup of P1 with reference
   component degrees (1,1) gives two such functions whose maximum has an
   irrational skeletal breakpoint and is not in D_R. The same continuous
   obstacle disproves directedness of its real-model minorants. The
   replacement retains real theta and real convex combinations, proves
   maximum closure for rational potentials, and proves fixed-real-theta
   rational approximation under the ample-generic-class hypothesis.
   A small rational downward shift preserves an arbitrary bounded obstacle,
   so the max-directed rational subfamily computes the same envelope in
   that scope. The other elementary real-model envelope properties retain
   their original merely semipositive reference assumption. Full BFJ psh
   maximum stability follows without falsely closing D_R under maximum.
2. **Chapter24.** The original real-input maximum/locality/comparison
   statements are preserved. The maximum may be continuous psh rather than
   model. The rational common-SNC coefficient argument is passed to real
   inputs by uniform fixed-form approximation and continuous tests supported
   on compact subsets of the fixed strict-inequality set. This avoids an
   invalid weak-limit assertion for moving sets. Numerical restriction is
   used for real divisors rather than an honest line bundle O(D).
3. **Chapters26/30.** Bounded decreasing model nets are controlled on
   cofinal tails without minima, maxima or translations that change the
   limit. The bounded energy continuity proof no longer asks for model
   approximations from below; it uses the earlier weighted MA continuity
   and the established bounded energy formula. Finite projection uses
   ordinary weak convergence against unrestricted continuous test functions.
4. **Chapter25.** The weighted capacity core was independently checked
   relative to its stated BFJ inputs. A quantifier gap in the long-chain
   example was repaired: the new example fixes P1 and the standard O(2)
   form and obtains divisorial-point capacities 1/N by successive smooth
   rational-point blowups. Thus the reference is genuinely fixed. A
   separate reviewer checked this new example. Point/tube versus full-mass
   wording and non-rational-node terminology were clarified.
5. **Chapter28.** The continuous-curve uniqueness replacement uses SNC
   intersection matrices, including multiplicities, and divisorial density.
   Its exact revised proof passed bounded independent review in the
   ordinary-connected original BFJ scope, without assuming a cofinal system
   of reduced semistable models over K.

These are corrections and elementary consequences, not newly retired
literature problems or claims to have disproved published BFJ theorems.

## Exact principal files

All directories below lie in `solver_dossiers_20260831/`.

| Object | Latest selected file / SHA256 |
| --- | --- |
| Ch20 maximum repair | `p081_ch20_ch21_real_model_max_repair_20260831/revised1/patched/ch20_model_forms.tex`, `3f2814e440f738708c084ee186a06e0930c0d48db89e80db1f21e7300e373ca2` |
| Ch21 maximum repair | same parent, `revised2/patched/ch21_bfj_psh.tex`, `81a1928677f59eba2e7eac6461480c5c90cadcccc70c15ea923ebbaeba6e0ed7` |
| Ch24 locality | `p081_ch24_real_maximum_locality_repair_20260831/patched/ch24_bfj_ma.tex`, `b831435e0e66562d10d368f359792c017c53160b0acf4e895b4d23f0d7c6238d` |
| Ch25 capacity | `p081_ch25_weighted_capacity_repair_20260831/revised1/patched/ch25_capacity.tex`, `4f66e1358ede7c8d9afff6b8b3c0fbaf53a27247d9741ce02f890fe24a0959a7` |
| Ch26 bounded nets | `p081_bounded_model_net_normalization_repair_20260831/patched/ch26_energy.tex`, `e37465c226a13e766ed2eecce014913fca3e5cdc2002e1766c151c83c73c6a74` |
| Ch30 bounded projection | same parent, `patched/ch30_functoriality.tex`, `02fa119b5732e3270989e3fddc0aa431add6eb04b27c40c208de9b3411ed2e28` |

The original maximum-defect audit, exact-revision review, and a separate
fresh independent review are preserved. The reviewers' provenance limits
are explicit. Parent technical reviews of the Chapter24 and bounded-net
replacements are not mislabeled as completely fresh independent review.
The additional exact-byte downstream review is complete, with scoped PASS
verdicts and explicit upstream/provenance limits. Its frozen reports are
`p081_bounded_net_and_ch24_downstream_independent_audit_20260831/`:
bounded-net audit SHA256
`bc04d196aaf6a616ce81d9e5bcda34c2e4d4fd499c878770d3c45203a656f853`,
Chapter24 audit SHA256
`bebbf1375759d3e4425c7325de43fa60d85d77f93cd86ce33ea427c218ecfa53`.
These reviews do not cover the final Chapter30 descent argument or the
general-SNC retraction proof. Every production Rethlas gate remains pending.

## Envelope-transfer research

The constant-variety transfer candidate and the nonconstant curve-base
extension both received separate independent mathematical audits. The
latter applies to smooth geometrically integral projective varieties and
ample polarizations already defined over k(t), completed to k((t)), with
k algebraically closed and trivially valued. Exact bounded weighted-FS
extension, a scaling collar of the full analytic fibre, and product-net
arguments give the claimed transfer conditional on the supplied ambient
trivial-field envelope property. The ambient proof itself was not newly
certified by these audits.

Nonconstant candidate statement/proof:
`6122b495f877fc78c861a99a3a29ce06d015ac3c9d27de982f7526fd245aace4` /
`96434222904dd0d66b60b67a2cf32230789f0cff139aac0d784be5bf382ca77e`.
Independent audit:
`p081_curve_base_fiber_extension_independent_audit_20260831/INDEPENDENT_AUDIT.md`,
SHA256 `5ffb47c8503c2dca2f5844f9943b2e18b727486523b3b30f09a87983a7606117`.

There is no claimed algebraization of arbitrary k((t))-varieties, no
arbitrary-complete-field theorem, no continuous-obstacle continuity result,
and no automatic CLD/BFJ identification. In particular the general
nontrivially valued envelope problem has not been solved here. No atom is
retired on the basis of a candidate or an AI audit.

## Build, live source and remaining boundaries

`p081_weighted_curve_full_syntax_review_20260831/revised2/` records the
eleven-chapter overlay build. Passes7--9 completed successfully; pass9
has no unresolved references, rerun-label warning or overfull boxes.
There are1020 underfull-box warnings and the existing document-class-name
warning. This is draft-mode syntax/reference evidence, not PDF layout or
mathematical verification. The final19-byte rational-Cartier clarification
then passed the full-manuscript pass10 with the same clean reference and
overfull-box result, recorded in `revised3/BUILD.json`. Its exact separate
independent addendum resolves the wording issue without changing the proof.

The only live source edit is the verification warning in the preface,
identically present in the temporary editing repository and durable
project. Its SHA256 is
`cf272800e9522242b103e693cfc522741859c690a282269f26e48fcd5ad3ec48`.
It explicitly warns about the manuscript's affected proofs and dependent
claims. No new mathematics is integrated. The existing3476-page PDF has
not been rebuilt and does not yet contain this newly expanded warning.

Still unresolved in the source: the full original-K SNC curve-retraction
framework, the nonreduced-model primitive-length convention, the remaining
Chapter30 model-maximum/descent consumers, and other stated upstream
verification dependencies. A standalone general-SNC candidate is now
drafted, but its complete independent review is unfinished. Its separate
convention/example audit does not certify the full proof. Reduced
semistable models must not be assumed cofinal over K. The research
distinguishes primitive affine edge length from the metric used for
resistance/intersection formulas, especially when gcd(b_i,b_j)>1.
These general-SNC files are outside this preservation selection. At the
user's direction, active research has shifted to Chapter72; the unfinished
SNC review and Chapter30 extension have been paused without a PASS claim.

The production submission approval gate remains unresolved. No retry by
another endpoint, tool, agent or weaker workflow has been used to bypass it.
Independent review is not formal verification or a substitute for that gate.

The active inventory was recounted directly from its51 tiered open entries,
including entries whose status says open after/beyond/residual. Its count
remains51 in14 formal problem environments. The book/research goal remains
active and is not complete or at a true impasse: substantial safe proof,
source and exposition work remains.
