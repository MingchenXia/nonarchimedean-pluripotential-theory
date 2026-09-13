# Self-hostile audit

Date: 13 September 2026

Status: local pass, followed by dependency-closed model-backed verification.

## Attacks

### Can the Stone quotient depend on uncountably many branches?

No.  A node factorization chart has one countable activity set.  Compactness
of the compact clopen parameter core gives finitely many such node charts for
each row.  Only those countably many branches require further branch charts,
and the union over a decreasing sequence remains countable.  The pulled-back
clopen bases therefore generate one countable Boolean algebra.

### Can a compact parameter supremum destroy the trace at minus infinity?

Not in the family used here.  The truncated family is finite-valued and
jointly upper semicontinuous on a compact parameter times a full branch.
Upper semicontinuity along the compact endpoint fibre supplies one terminal
interval valid for every parameter, while branch monotonicity supplies the
opposite inequality.

### Can a clopen maximum violate the junction balance?

No.  The finite-point balance is a positive-weight Jensen inequality at the
node.  Taking a supremum of its left side and then bounding the supremum of
the weighted sum by the weighted sum of the suprema preserves it.

### Is the countable active set enough for CLD smoothness?

Not directly.  At stage k, the proof retains only a finite subset of the
common countable set and makes every other full branch constant at the node
value.  The exact infinite-star slope budget survives because only
nonnegative full-branch slopes are discarded.

### Does smoothing lose exact monotonicity?

No.  The comparison truncations already decrease.  Smoothing w_k + 2^{-k}
within 2^{-(k+4)} leaves a strict positive gap after the next stage.

### Is the endpoint argument merely pointwise?

No.  The exact endpoint dependency supplies decreasing continuous
approximants to a finite continuous limit on a compact terminal core.  Dini's
theorem makes the convergence uniform.  Each clopen partition is finite, so
one accuracy choice works for the entire stage.

### Does the theorem solve P07.1?

No.  It treats a locally constant Stone factor times the exact CLD star.
Nonconstant Stone affine directions, non-CLD infinite stars, an additional
active polyhedral factor, and nonambient branch structures remain outside
the theorem.

## Outcome

The strict writing audit reported zero errors and zero warnings.  The exact
seven-page packet compiled without TeX warnings or bad boxes and was
visually inspected page by page.  The final local gpt-6-astra verification
returned correct, with zero critical errors and zero gaps.
