# Hostile boundary audit

## Verdict before production verification

**No fatal mathematical gap was found in the exact product-scope
candidate.** This is an internal audit only, not a Rethlas verdict and not
authorization to integrate the result into the live book.

## Failure attempts

### 1. Nonmetrizable parameter space

An uncountable Cantor cube is not first countable or metrizable, so one
cannot regularize directly in its topology. The proof uses only countably
many local quotient data, because a CLD successor operation is sequential
and each row has a finite cover of the compact core. The generated Boolean
algebra is countable, hence its evaluation quotient is compact metrizable.
No metrizability of \(Z\) is imported.

### 2. Shrinking row neighbourhoods

The proof does not select from the original row approximants. It first
places the full generated sheaf inside a comparison sheaf stable under
decreasing limits, then constructs a fresh approximation from the single
factorization of the limit germ on \(C\times B_0\). Thus the original
shrinking-neighbourhood obstruction is genuinely bypassed in this product
scope.

### 3. Product-quotient USC gap

The assertion that \(\bar v\) is USC is not inferred merely from continuity
of \(q\). For a strict sublevel, compactness of \(q^{-1}(y)\) gives one
finite product neighbourhood contained in the pulled-back sublevel, and
closedness of \(q\) produces an open neighbourhood downstairs. This closes
the common product-quotient gap.

### 4. Fibrewise \(-\infty\)

The comparison class does not permit a partly polar convex fibre. The
midpoint argument proves that a locally convex
\(\mathbf R\cup\{-\infty\}\)-valued function on a connected ball is either
finite everywhere or identically \(-\infty\). The floors \(-k\) make every
upper envelope finite, and joint USC proves convergence even at a polar
point.

### 5. Supremum could be infinite

The shifts used in one envelope remain in the compact set
\(\overline{B_1}+r_1\overline{\mathbb B}\Subset B_0\). A
\(\mathbf R\cup\{-\infty\}\)-valued USC function is bounded above on the
resulting compact product with \(Y\). Hence every envelope is finite after
the floor.

### 6. Smoothing could break monotonicity

Different levels use different convolution radii, so monotonicity does not
survive literally. Jensen and the finite-family approximation estimate
give the exact chain
\[
 w_{k+1}\le a_{k+1}+\eta_{k+1}
 \le a_k+\eta_{k+1}\le w_k+\eta_{k+1}.
\]
The summable tail constants then make the corrected sequence exactly
decreasing.

### 7. Positivity at clopen seams

There are no seams in the local topology: every
\(q^{-1}(P)\) is clopen in \(Z\). Near each point a smoothed approximant is
one Euclidean smooth convex branch, so it is smooth psh for the exact
product affine structure.

### 8. Degenerate Euclidean factor

The proof treats \(d=0\) separately. The approximants are finite-level
locally constant functions, so no nonexistent convolution or strict ball
nesting is used.

### 9. Illegal choice of parlinear parameters

For a smaller value group \(G\), an arbitrary finite subset of
\(\mathbf R^m\) need not be a legal \(G\)-polyhedron. The statement
therefore fixes CLD's body convention \(K=\mathbf Q,G=\mathbf R\).
Dropping this hypothesis has not been audited.

### 10. A hidden claim for another affine structure

The proof uses decisively that all parameter-direction affine functions are
locally constant. A different affine structure on the same topological
space can add Hessian directions or coupling conditions and is outside the
statement.

## Exact surviving boundary

The following cases remain outside the packet:

- nontrivial affine directions in the parameter factor;
- polyhedral face gluing and junction positivity constraints;
- arbitrary affine G-tropical spaces;
- a counterexample genuinely requiring the second CLD stage;
- any uniform early ordinal for the remaining geometries.

Accordingly, the packet narrows P07.1 but does not solve or retire it, and
it gives no result on P07.2.

