# Early collapse of the CLD psh hierarchy

## Provenance and exact question

This packet is **prepared but not run**.  It records a corrected, book-formulated
question prompted by Chambert--Loir--Ducros, arXiv:1204.6277v2, Lemma 8.1.4
and Remark 8.1.6.

For an affine refined tropical space \(X\), CLD define sheaves
\(\operatorname{Psh}_{X,\alpha}\) by transfinite recursion:

1. \(\operatorname{Psh}_{X,0}\) consists of smooth \(u\) with
   \(\mathrm d'\mathrm d''u\geq 0\);
2. \(\operatorname{Psh}_{X,\alpha+1}\) consists locally of decreasing limits
   of functions in \(\operatorname{Psh}_{X,\alpha}\), with the local
   integrability required in their definition;
3. at a limit ordinal, membership is locally membership at an earlier stage.

Lemma 8.1.4 proves by a cardinality argument that this increasing hierarchy is
eventually stationary and equals the CLD psh sheaf.  Remark 8.1.6 nevertheless
says literally that stationarity is not known, then explains the intended
analytic issue: the complex hierarchy stops at stage one and every
non-Archimedean example known to the authors also lies at stage one.  The
literal sentence in the remark conflicts with the lemma.  Do not try to prove
eventual set-theoretic stabilization; it is already proved.

Determine instead:

- whether \(\operatorname{Psh}_{X,1}=\operatorname{Psh}_X\) for every affine
  refined tropical space in a natural geometric class;
- failing that, whether a finite, countable, or otherwise uniformly controlled
  ordinal bounds the hierarchy on such a class; or
- whether one can construct a psh function of genuinely higher closure rank.

## Required proof audit

A positive proof must flatten iterated local decreasing approximations without
silently replacing general local indexing/topology by a first-countable or
metrizable model.  Track local integrability, restriction, pullback, and the
difference between pointwise decreasing and locally uniform convergence for
continuous functions.  A counterexample must prove non-membership at every
earlier stage, not merely exhibit a failure of one chosen approximation.

Keep this question separate from whether every *classically* psh function is
CLD psh.  Early collapse concerns the internal rank of a function already in
the CLD sheaf.

