# Production-verification problem: P21.3 rigid exceptional set

Verify the exact proposition and proof in
`p213_rigid_exception_extension_statement_20260829.tex` and
`p213_rigid_exception_extension_proof_20260829.tex`.

Treat the following theorem as an already production-verified imported
dependency, with the exact live hashes recorded in the source audit:

> Let `K` be a complete nontrivially valued non-Archimedean field and let
> `Y` be a connected good separated strict rig-smooth `K`-analytic curve
> without boundary. Every positive `d'`- and `d''`-closed CLD current of
> bidegree `(0,0)` on `Y` is `c delta_Y` for a unique `c>=0`.

Audit every remaining step rather than reproving that dependency.  In
particular:

1. Check that a locally finite set of rigid points is closed in the
   separated analytic curve and that the complement inherits the hypotheses
   needed by the imported theorem.
2. Check exactly the cited Ducros chain: analytic curves are graphs;
   connected graphs admit injective arcs; rigid points on a normal analytic
   curve are unibranch; interior points of injective arcs are pluribranch.
   Decide whether this proves that the complement is nonempty and connected.
3. Check the CLD support argument at the level of test forms, not measures:
   Proposition 3.3.6 and Proposition 15.2.1(a) should imply that every smooth
   compactly supported `(1,1)` test form misses every rigid point.
4. Check that `T|_Y=c delta_Y` then forces `T=c delta_X`, including the
   restriction identity for integration currents and compact support after
   restriction.
5. Check the continuous-pair Bedford--Taylor deduction and all current
   multiplications, signs, bidegrees, and continuity hypotheses.
6. Search for counterexamples within the printed hypotheses, especially
   over imperfect or non-algebraically-closed fields and when `E` is
   infinite but locally finite.
7. Check every source citation in the primary CLD v2 and Ducros v1 PDFs
   identified in the source audit.

Do not broaden the conclusion to nonrigid exceptional points, nonnormal
curves, non-locally-finite exceptional sets, trivially valued fields,
discontinuous psh functions, or higher dimension.  Return `correct` only if
there are zero mathematical gaps and all citations support exactly the uses
made of them.
