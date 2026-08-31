# Bounded model-net normalization: isolated author candidate

Date: 31 August 2026. Scope is the full bounded-potential statements in
Chapters 26 and 30, not new field hypotheses or a new descent theorem.
The candidate is not independently or production verified.

## Exact editing bases

- Chapter 26 starts from the frozen weighted-energy overlay
  `../p081_weighted_energy_consumers_repair_20260831/patched/ch26_energy.tex`,
  SHA-256 `8552d7b5e4c5c58cf48e94db28bf44f3286af4f997adf3f4716cee52d8f26d28`.
  It does not start from the live unweighted chapter.
- Chapter 30 starts from live `manuscript/parts/part3/ch30_functoriality.tex`,
  SHA-256 `61957fd06cf4cd24833cd5d7d698b9aa8640d9d094ca7d8237a235be395bf951`.
- Live Chapter 26 is recorded only as the application base of the combined
  patch: SHA-256
  `242f10b4c8be9e90bc457f897999f00d24d011a6c1b564436fe9c3a82f8d3d3d`.

`assembly_edits.json` contains the exact old and new spans. Each full copy
is exactly its editing base with that one span replaced. The validator
checks this equality, unchanged theorem statements, all old labels, and
the exact frozen Chapter 26 weighted graph fragment. In particular no
curve-energy formula, conductance, or earlier weighted proof is changed.

`incremental_overlay.patch` is for a tree already carrying that Chapter 26
weighted overlay and the recorded Chapter 30 base. `combined_live.patch`
contains both the existing Chapter 26 weighted changes and this new
normalization repair and is checked against the recorded live chapters.
They are alternative application routes, not patches to apply successively.
Neither has been applied to the manuscript.

## Corrections and their proof dependencies

1. Chapter 26, `prop:bounded-energy-identities`: a decreasing model net
   already majorizes its bounded limit. Its continuous approximants and
   compact analytification give a cofinal tail below `sup(phi)+1` by a
   finite open subcover and a common upper bound of its indices. The tail
   is bounded on both sides, has the same limit, and consists of the exact
   same model functions. No minimum, maximum, translation of the limit,
   or uniform convergence assertion is used. The comparison translation
   in Step 2 is only a model majorant used to compare energy values.
2. The same proposition's former Step 4 incorrectly requested model nets
   below each bounded potential and asserted an unexplained decreasing
   diagonal. It is replaced at full bounded-net scope: the bounded energy
   formula, already proved in Step 1, has finitely many integrals to which
   Chapter 24 weighted monotone continuity directly applies. Fixing one
   index gives a uniformly bounded tail even when the members are merely
   bounded psh, since the fixed member bounds every subsequent member.
   Step 3 supplies energy monotonicity, so convergence is decreasing.
3. Chapter 30, `thm:ch30-finite-bounded-projection`: the lower maximum was
   redundant because every approximant already lies above the limit. It
   could not establish an upper bound. The replacement gives the same
   finite-cover argument separately in each slot and then explicitly uses
   the finite product of the cofinal tails. Pullback retains the bounds,
   decreasingness, and actual model/psh properties.
4. The adjoining proof incorrectly applied weighted monotone continuity
   directly to an arbitrary continuous or model test function. The new
   proof uses weak convergence on both spaces from Step 6 of
   `thm:bounded-ma-extension`, the model measure projection identity, and
   weak continuity of pushforward. The labelled accompanying remark now
   explains the distinction. `lem:ch24-psh-difference` concerns model
   functions; it does not state that every continuous function is the
   difference of two continuous psh functions.

The chronology was checked in the current source. Chapter 24 constructs its
own mixed scalar pairing from model intersections, extends it by the
compactness sandwich lemma and decreasing regularization, and then obtains
bounded mixed measures and weighted monotone continuity. Its discussion
immediately before `sec:ch24-masses` explicitly disclaims using the energy
functional developed in Chapter 26. Thus the new Chapter 26 Step 4 uses an
earlier bounded-measure theorem and its own already-established bounded
formula, not its desired monotone energy conclusion. Chapter 30 uses the
measure consequence of that earlier Chapter 24 theorem. Neither correction
uses Chapter 25 capacity, any curve graph lemma, or final Chapter 30 descent.

The relevant prerequisites are preserved as inputs, not re-proved or
certified here: proper analytic compactness; original-scope BFJ decreasing
regularization; the bounded Chapter 24 operator and its continuity; model
energy identities/monotonicity/translation; model pullback of vertical real
divisors with nefness; and the model projection formula. Their exact source
files and all referenced label owners are recorded in `SOURCE_HASHES.json`
and `VALIDATION.json`. The separate upstream real/Q model-max repair and
all its integration gates remain separate. The replacement Chapter 30
proof uses only the divisor and ddc items of the model-pullback lemma, not
its problematic maximum-closure item.

## Audit of other min/max and normalization occurrences

The full Chapter 26 overlay and Chapter 30 source were searched for maxima,
minima, decreasing arrows, replacements, constants, uniform bounds, and
model-max citations; relevant proof neighborhoods were read in context.

| Location in recorded source | Finding and disposition |
| --- | --- |
| Ch26 around 835--844 | Improper clipping by `min(phi_alpha,sup(phi)+1)` and simultaneous untracked translation; replaced. Even minima of affine functions can create a concave corner on a reference-flat graph edge, so psh closure under maximum could not justify it. |
| Ch26 around 896--904 | Approximation from below/diagonal error directly adjoining the normalization; replaced using the existing bounded formula and weighted continuity. |
| Ch26 around 1295--1395 | Model majorants in extended energy are from above; no corresponding clipping assertion. Not changed. |
| Ch26 canonical truncations and common translations, including around 2270--2330 | These concern bounded psh truncations of singular potentials, not a claim that clipping arbitrary real model approximants preserves the model class. Their truncation/translation identities are not replaced. |
| Ch30 around 832--838 | Redundant lower maximum and missing upper bound; replaced. |
| Ch30 around 840--892 | Direct test-class mismatch and overstated continuous-psh decomposition; replaced together with the full projection proof. |
| Ch30 `lem:ch30-pullback-model-calculus`, especially 323--326 and 354--361 | Distinct real/Q maximum-closure consumer: composition commutes pointwise with maxima, but the proof says arbitrary real model maxima remain model functions. This is false in general over the original DVR. Not a bounded-net normalization, hence left unchanged and flagged for the separate root-owned real/Q model-max work. The actual divisor/psh pullback items used here do not require it. |
| Ch30 around 499, 968--975 | Canonical bounded psh truncations, not model-net normalization. Left unchanged. |
| Ch30 around 2154--2172 | Refers back to the bounded/finite-energy transfer argument for scalar extension, without a new clipping construction. It inherits the corrected bounded proof. No full scalar-extension theorem audit is claimed here. |
| Ch30 around 2820--2838 | The final singular-descent discussion repeats a finite-minima/model-max mistake. Explicitly excluded from this repair, as detailed below. |
| Remaining valuation/tropical minima and maxima | Valuation sums, Gauss formulas, and graph examples, not min/max normalization of decreasing approximating nets. Not changed. |

## Unresolved excluded final Chapter 30 descent

The paragraph headed “Singular potentials are not covered” in
`sec:ch30-descent-limits` says finite Galois averaging becomes monotone
only after passing to finite minima, allegedly model functions by the
model-max proposition. That justification is invalid: psh minima are not
generally psh, and the cited maximum result does not give the assertion.
For an already decreasing net, averaging over one fixed finite group is
itself order preserving and decreasing; no finite minima are needed for
that elementary fact. This observation alone is not a full proof of the
paragraph's arbitrary-singular descent assertion. Model descent at every
stage, invariant approximation, and the precise original descent hypotheses
must be checked in a separate full-proof repair. No such descent conclusion
is certified, narrowed, or removed by this dossier. The exact excluded
paragraph is retained in the Chapter 30 full copy.

## Scope and gates

Both original labelled theorem statements are byte-for-byte retained. All
bounded psh functions and arbitrary directed nets in those statements are
retained; no continuity, sequence, rational-coefficient, skeletal-support,
or algebraically closed-field restriction has been added. All earlier
weighted-energy edits are preserved. Checks and draft compilation establish
only assembly/syntax consistency, not mathematical verification. Independent
review and the required production Rethlas sol/xhigh review of all new bytes
remain required before any live integration. No production call, permission
bypass, PDF generation, or live-manuscript mutation has been made here.
