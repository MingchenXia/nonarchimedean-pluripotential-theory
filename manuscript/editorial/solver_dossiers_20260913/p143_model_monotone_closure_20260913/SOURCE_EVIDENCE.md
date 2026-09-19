# P14.3 MP-section theorem: source and dependency ledger

The proposition is a book-internal formal consequence.  Its external source
interfaces enter only through already stated book results.

1. `def:mp-general-psh` reproduces Mesquita--Piccione, Definition 4.3.1:
   a nontrivial pointwise decreasing net of rational PL MP-psh functions
   defines an MP-psh function.
2. `thm:mp-psh-divisorial` reproduces Mesquita--Piccione, Theorem 4.3.3:
   every MP-psh function is finite on the rational divisorial locus, which
   includes the trivial semivaluation in the convention used here.
3. `thm:pseff-divisorial-inversion`, equation (71.32), records Xia,
   Lemma 4.2: the DXZ order is reflected by the positive divisorial values
   together with the endpoint value.  This makes the finite-energy DXZ
   preimages of a decreasing MP model net automatically decreasing.
4. `prop:pseff-operation-formulas`, equation (71.48), records Xia,
   Lemma 4.10: the raw ideal-valuative transform commutes on rational
   divisorial points with a decreasing DXZ infimum whose endpoints have a
   common finite lower bound.
5. `cor:p143-all-point-kahler-comparison` identifies each finite-energy DXZ
   input with its corresponding MP potential at every semivaluation.
6. `thm:p143-dominated-divisorial-density` promotes equality between an
   upper-semicontinuous antitone raw transform and an MP-psh potential from
   rational divisorial points to all semivaluations.
7. `def:operations-infimum` uses the standard endpoint extension for a
   decreasing infimum.  Hence the terminal parameter of the infimum is the
   infimum of the terminal parameters; together with
   `thm:pseff-perturbation-independent-transform`, this supplies the equality
   at the trivial semivaluation required by the convention
   `0 in X^divis`.

The P14.2 upper-semicontinuity conclusion remains an explicit premise.  The
new statement neither verifies P14.2's outstanding production gate nor
asserts that every DXZ raw transform is MP-psh.
