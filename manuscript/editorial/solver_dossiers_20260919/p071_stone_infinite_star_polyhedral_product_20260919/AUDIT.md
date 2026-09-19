# P07.1 Stone--exact-star--polyhedral product — dependency audit

Date: 19 September 2026

## Claim boundary

The theorem permits three factors simultaneously: an arbitrary locally
compact Hausdorff clopen-base space carrying only locally constant affine
functions, an exact Chambert--Loir--Ducros star with an arbitrary nonempty
branch set, and one nonempty convex polyhedron with all its affine
directions, faces, and corners.  The generator is jointly convex in the
branch and polyhedral variables.

It does not add nonconstant affine directions on the Stone factor, replace
the exact CLD star by a non-CLD or nonambient branch structure, weaken joint
convexity to separate convexity, or treat nonconvex or branched chamber
gluings.  P07.1 therefore remains open, and its atom and tier counts are
unchanged.

## Proof ledger

1. For a decreasing sequence of comparison sections, compactness gives
   finitely many node charts for each term.  Their exceptional and active
   branch sets have a countable union, which is one activity set common to
   the whole Stone family and to the limiting section.
2. The clopen bases of all metrizable Stone quotients generate a countable
   Boolean algebra.  Its evaluation map is a continuous quotient onto a
   compact metrizable zero-dimensional space, and all terms descend through
   that single quotient.
3. Upper semicontinuity descends because a compact-to-Hausdorff quotient is
   closed.  Fibrewise membership passes to the limit by the established
   decreasing closure of the exact star--polyhedral comparison sheaf.
4. Collapsing inactive branches gives a compact metrizable exact-star core.
   Sup-metric regularization supplies finite continuous decreasing
   obstacles, and the exact comparison envelope is nonexpanding in the
   uniform norm.  The resulting fibre envelopes are therefore jointly
   continuous in the Stone parameter.
5. Maxima over finite clopen cells preserve joint convexity, the node
   inequalities, and the exact endpoint trace.  Compactness of the terminal
   prism controls that trace uniformly.  The established two-stage
   barycentre calculation restores every inactive branch without leaving
   the exact comparison class.
6. The uniform one-step estimate applies to each finite clopen family on
   one prescribed smaller star--polyhedral neighbourhood.  A summable error
   tail converts the approximate monotonicity into an actual decreasing
   generator sequence.
7. At full endpoints the nonexpanding terminal insertion and constant-five
   smoothing give the same construction.  Ordinary branch points reduce to
   the existing Stone--polyhedral theorem.

## Scope firewalls

- The Stone coordinate is locally constant in every generator.
- Only one convex polyhedron is used locally; no chamber gluing is inferred.
- Exact CLD endpoint and node identities are retained throughout the
  envelope, maximum, inactive-branch lift, and smoothing steps.
- The conclusion is a positive P07.1 case, not a retirement of P07.1 and not
  a claim that a second decreasing-limit stage is never needed in general.
