# Chapter 23 fixed-skeleton selection: post-repair hostile audit

**Date:** 2026-08-24 (Asia/Shanghai)  
**Target:** `prop:ch23-fixed-skeleton-selection`  
**Result:** PASS from the source-level hostile audit.  The repaired exact
payload was subsequently resubmitted in production run
`20260824T044830Z_25024c43d265`, which returned final `correct`, zero critical
errors, and zero gaps.  Later provenance and line-breaking edits below the
verified interval changed the live Chapter 23 SHA-256 to
`acaf22a242ee48952d8d4339c9ebd7bd6fafdf5ac118dec66aaf1d67eaaa2bfd`
but left the exact contiguous proposition-and-proof slice byte-identical to
the verified payload, SHA-256
`d91003dd920d193192b4dcd8a064ac46d5535cb6befc53bd08670db8451d7786`.
The table below records the production-submission snapshot and is retained as
audit history.

## Adversarial scope

This audit starts from the five gaps in
`ch23_fixed_skeleton_selection_failed_gate_20260824.json` and attempts to
break the repaired proof at the metric, finiteness, selection, and uniform
convergence interfaces.  The imported geometric content is limited to the
three earlier results restated in the exact proof: skeletal finiteness and
continuity, a common facewise Lipschitz constant on the fixed determining
complex, and finiteness and connectedness of that complex.  All remaining
arguments are now internal to the submitted proof.

## Failed-gate closure

1. **Common facewise constant.**  The proof records one
   `L=L(Xcal,theta)>0`, independent of the psh function and valid on every
   face for the fixed system of norms.  This is exactly the specialization
   of `thm:bfj-skeletal-equicontinuity`(1) that the selection uses.
2. **Compatible global metric.**  The proof defines the length of a segment
   in the norm of its smallest carrier face and takes the infimum over
   facewise segment chains.  Uniform comparison with a Euclidean realization
   gives `d>=a rho`, hence nondegeneracy.  Finiteness of the face set shows
   that every sufficiently `rho`-close point to `x` shares a face with `x`,
   whence `d<=b rho` locally.  Thus the metric induces the simplicial
   topology, makes the complex compact, and summing the facewise estimate
   gives the asserted global modulus.
3. **Finiteness.**  Nonemptiness supplies `psi_0`.  The earlier skeletal
   theorem makes `psi_0|_Delta` real valued, while the common upper bound
   gives `psi_0(x)<=u(x)<=C_0`.  Therefore the pointwise supremum never takes
   either infinity and the dense-point selections are legitimate.
4. **Finite maxima.**  The proof no longer claims that a finite maximum is
   psh.  It proves directly the only required assertion,
   `|max_i f_i(x)-max_i f_i(y)| <= max_i |f_i(x)-f_i(y)|`, so every finite
   maximum retains the common modulus.
5. **Sequential Dini step.**  For fixed positive `epsilon`, the increasing
   open sets `V_j={u_j>u-epsilon}` cover the compact complex.  A finite
   subcover of a nested cover is already one member, yielding
   `0<=u-u_j<epsilon` for all sufficiently large `j`.  No unquoted Dini
   theorem remains.

## Further attempts to break the proof

- If the selected image family is finite, the construction still works:
  it enumerates the countable double index set and permits repetitions, so
  every selected pair occurs at a finite stage.
- The pointwise limit is finite because it is trapped between the first
  finite maximum and the finite function `u`.  Passing the common modulus to
  the supremum uses only the displayed two-sided inequality, not psh
  closure.
- Equality on the dense set follows by fixing `k`, allowing the stage to
  depend on `m`, and then sending `m` to infinity.  Continuity of both finite
  functions then promotes equality to the whole complex.
- The argument is explicitly fixed-skeleton.  It does not manufacture a
  countable cofinal model system, a sequence valid on every skeleton, or a
  replacement for the global net-valued envelope theorem.
- The empty-family counterexample is excluded by hypothesis, and the common
  upper bound is genuinely needed to exclude `+infinity`.  These hypotheses
  were not silently weakened.

No counterexample, circular dependency, hidden psh-maximum claim, or scope
leak survives these checks.

## Exact-current identities and compilation

The extracts compare byte for byte with live lines 1228--1237, 1239--1365,
and 1228--1365, respectively.

| Object | Bytes | SHA-256 |
|---|---:|---|
| live Chapter 23 source | 165480 | `72da809fadf0685c8e8bb05559e3c0fd7f8eb3d94a75f1ee8607b7289518f123` |
| exact proposition | 516 | `2fffb48dc500d93dd24cbffac1dc81c84f817bc6df9d1948d078c75dced75209` |
| exact proof | 6341 | `39884cd45e524d2fa6aaa4dd7320aac14d6d490c630870745f56ac7f763186f4` |
| exact proposition plus proof | 6858 | `d91003dd920d193192b4dcd8a064ac46d5535cb6befc53bd08670db8451d7786` |
| Rethlas target statement | 765 | `25024c43d265636b667320ddb4090b3882320790f029bbe8f3103808dd3595e8` |
| Rethlas context packet | 6662 | `c8e4074cd80cfdc208c884a9c54e6ac8d6b5059a37ea2c9da9bed720810180ba` |
| intake manifest | 3833 | `20bfb70d349c56d11c6d35df6bf8a8a538858a92a25bb579192a9a7ff25dd555` |

The last row records historical pre-submission metadata.  Those manifest
bytes were not retained, and the digest is not the hash of the current
manifest; the current manifest and its digest are identified in the
production receipt.

An isolated `includeonly` build of Chapters 20--23 completed with exit code
zero and produced a 271-page PDF with SHA-256
`b307731906b96f2d3a2165362a2ff89343603c8dfc8a2a3b82ec26473927741f`.
The log has no LaTeX errors, undefined references or citations, duplicate
labels or destinations, or overfull boxes.  The proposition and proof on
physical PDF pages 227--229 were also inspected visually.  Missing-link
destination warnings point only to chapters omitted by `includeonly`.
