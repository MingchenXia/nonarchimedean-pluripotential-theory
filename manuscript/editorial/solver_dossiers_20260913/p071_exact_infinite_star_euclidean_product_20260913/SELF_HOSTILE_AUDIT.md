# Self-hostile audit

Date: 20 September 2026

Status: local mathematical and typesetting pass complete; model-backed gate
passed.

## Attacks

### Does restriction change which branches are exceptional?

Yes, and the proof accounts for it with an explicit \(A\cup E\) ledger.
Contract a junction tuple toward the node and retain the contracted data on
every original branch in \(A\cup F\).  Each newly exceptional branch in
\(E\setminus F\) is sampled at the central Euclidean coordinate.  It was
full before restriction, so its value is at most the central value;
subtracting its central term produces a nonpositive contribution which can
be discarded.  The proof records the resulting reciprocal-weight term
explicitly: if
`Theta=sum_{e in E\F} 1/sigma_e`, the new samples contribute
`sum_{e in E\F}(u_e(sigma_e,y_0)-c(y_0))/sigma_e <= 0`; the retained
branches then satisfy the original junction inequality with the same
Euclidean barycentre.  Thus locality is not being inferred from a silent
shrinking of the exceptional set.

### Can a decreasing family require uncountably many active branches?

No.  For each row, finitely many node charts cover a compact Euclidean core.
The union of their finite exceptional and countable activity sets is
countable.  Taking the union over the sequence remains countable and works
on one product germ.

### Does the partial Legendre transform preserve the junction condition?

Yes.  Independent minimizers of the finitely many branch terms have a
weighted barycentre in the compact convex core.  Applying the product
junction inequality there and subtracting the common dual affine term gives
the scalar exact-star Jensen inequality.  Conversely, adding the Euclidean
barycentre identity to the scalar inequality and taking a dual supremum
recovers the product junction inequality.

### Can local biconjugacy lose the desired function?

Not on the selected open set strictly inside the compact convex core.
Every finite convex Euclidean slice has a supporting covector there.  The
supremum of the truncated scalar intercepts is therefore exactly
`max(u_b,c-n)` on retained branches and exactly `c` on inactive branches.

### Is continuity at the node only pointwise in the Euclidean variable?

The proof now includes the missing joint boundary lemma.  A finite convex
function on a half-cylinder whose fixed-fibre limits equal its continuous
boundary trace is jointly continuous at the boundary.  The upper estimate
uses interpolation from the boundary to a fixed interior slice; the lower
estimate solves a convexity inequality after fixing one near-boundary slice.
Only finitely many branches remain active, so the cofinite-branch topology
then gives continuity on the compact star product.

### Does finite dual sampling still majorize the target after smoothing?

This check found and repaired a real draft defect.  A finite dual maximum is
only within `epsilon_n` from below.  The scalar smoothings are therefore
shifted by `2 epsilon_n`, and the regularized maximum is shifted once more.
The exact bound is now

`H_n <= W_n <= H_n + 5 epsilon_n`.

Accordingly the monotonicity correction is
`5 sum_{k>n} epsilon_k`.  The displayed cross-stage inequality now closes
with no missing lower-error term.

### Does the regularized maximum preserve exact node balance?

Yes.  At the node the partial derivatives of the smooth maximum with
respect to its finitely many inputs depend only on their common branchwise
node values, hence are independent of the branch.  Summing branch
derivatives first reduces the balance to the zero balance of each input.

### Are full endpoints controlled uniformly in the Euclidean variable?

Yes.  After truncation the endpoint slice is finite and continuous.  The
branch slices converge monotonically to it, and Dini's theorem gives the
uniform terminal control on the compact Euclidean core needed for finite
dual sampling and a common collar: apply Dini along any sequence decreasing
to the endpoint, then use branch monotonicity to control every sufficiently
terminal parameter.  A second hostile pass found that this
alone did not prove cross-stage monotonicity: the earlier draft merely cited
a regularized maximum and a tail correction.  The proof now repeats the
complete finite-sampling estimate at the endpoint, shifts the scalar
approximants by `2 epsilon_n`, charges one `epsilon_n` for the regularized
maximum and one more for strict majorization, and obtains
`H_n <= W_n <= H_n + 5 epsilon_n` on one fixed terminal product
neighbourhood.  With `d_n=5 sum_{k>n} epsilon_k`, the displayed inequality
`G_{n+1} <= H_{n+1}+5 epsilon_{n+1}+d_{n+1} <= H_n+d_n <= G_n`
closes the endpoint case quantitatively.

### Does the theorem retire P07.1?

No.  Polyhedral faces and corners in the active factor, a simultaneous
Stone parameter, non-CLD infinite stars, separately convex generators, and
nonambient branch structures remain outside the result.

## Local outcome

The final house-style bytes pass the strict Mingchen writing audit with zero
errors and zero warnings.  Dependency-closed local verification with
`gpt-6-astra` at `xhigh` returned final `correct`, zero critical errors, and
zero gaps.  The current full book compiles successfully, and every page of
the theorem and proof has been visually inspected without clipping,
collision, malformed mathematics, or illegible text.  Exact verifier and
build hashes are recorded in `VERIFICATION_RECEIPT.md` and `BUILD_REPORT.md`.
