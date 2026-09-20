# Source and dependency audit

Date: 20 September 2026

The new corollary imports no external theorem.  Its only mathematical input
is the book-local theorem
`thm:p071-stone-infinite-star-polyhedral-collapse`, submitted with its full
dependency closure.  The remaining steps are internal sheaf operations:

- transfinite induction shows that the hierarchy stages commute with
  restriction to an open subset;
- the two-sided generator-preserving chart identifies every restricted
  hierarchy stage;
- the ambient theorem supplies equality, a fixed-neighbourhood decreasing
  approximation, and the nodewise common countable activity set;
- the intrinsic full generated sheaf identifies transported comparison
  sheaves on chart overlaps.

The earlier corollary
`cor:p071-locally-finite-generator-convex-collapse` uses the same local
transport mechanism without the exact-star factor.  It is explanatory
precedent, not a logical dependency of the new proof.
