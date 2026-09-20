# P07.1 double-node support-plane reduction audit

Date: 20 September 2026

Status: verified and integrated into the live book.

## Claim boundary

The packet concerns a real-valued continuous function on the product of two
open exact trivalent-star charts.  It proves that the full balanced
double-node Jensen family is equivalent both to its subfamily with at most
five atoms and to one ambient affine minorant touching at the double node.

It does not prove that these conditions characterize the generated psh
sheaf.  It supplies a finite-rank description of the already necessary
double-node condition and leaves the stratified regularization problem open.

## Exact checks

1. Equal branchwise radial moments are equivalent to ambient barycentre zero
   because the three ray vectors sum to zero and the first two form a basis.
2. An extreme point of the finite weight polytope has at most five positive
   coordinates: normalization and four ambient moment coordinates give at
   most five independent equality rows.
3. On every compact collar, the convex envelope is finite near the origin;
   the mixed Jensen condition makes the node value equal to the envelope
   value there, so the interior supporting-hyperplane theorem applies.
4. The collarwise support-plane sets are nested.  Their first and second
   axis inequalities bound both dual components, hence one fixed set is
   compact and the nested intersection gives a single plane on the whole
   open chart.
5. Summing that affine minorant against balanced weights recovers the mixed
   Jensen inequality.
6. The displayed five vectors sum to zero, and the determinant of their four
   affine differences is exactly five.  Their positive barycentric
   coordinates are therefore unique, proving sharpness for barycentre
   representation.

## Verification history

The first model run returned final `correct`, but visual inspection found
two missing TeX command markers in the proof source.  That run is preserved
under `model_run_superseded_tex_escape/` and is not controlling.  A second
run, preserved under `model_run_superseded_extra_plus/`, repaired those
escapes but retained an unintended plus sign between two convex-envelope
constraints; automatic second-pass reading found it after the first full
book build.

After deleting only that stray sign, the exact current statement and proof
again passed the local `gpt-6-astra` verifier at `xhigh`, final `correct`,
with zero critical errors and zero gaps.  The strict exact-current receipt
audit also passed.
