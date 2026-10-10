# Critical Siu division: repair routes and a two-branch diagnostic

Date: 4 October 2026. This continues the
[published proof-boundary correction](bj22_siu_proof_boundary_audit_20261004.md)
after the cyclic local-model checkpoint `1a09aa6`.
It records unsuccessful repair routes and a direct worked calculation.
It supplies no proof or counterexample to BJ22 Theorem 6.21 and no
independent production-model verdict. It is outside the active TeX closure.

## A fixed-line-bundle approximation that defeats coefficient reselection

Let the field be algebraically closed and trivially valued, let
\(X=\mathbf P^1\), and write \(p=\{z_0=0\}\),
\(q=\{z_1=0\}\). Set \(E=p+q\),
\(\ell_p=\log|s_p|\), \(\ell_q=\log|s_q|\), and
\(\ell_E=\ell_p+\ell_q\). For \(n\ge2\), put
\[
 c_n=1-\frac1n,\qquad
 \psi_n=\ell_p+c_n\ell_q.
\]
These functions are genuinely homogeneous Fubini--Study functions for
the **same ample line bundle** \(L=\mathcal O(2)\):
\[
 \psi_n=\frac1n\max\{
  \log|z_0^{n+1}z_1^{n-1}|,
  \log|z_0^nz_1^n|\}.
\]
Both displayed sections have degree \(2n\). Since \(z_0,z_1\)
have no common zero, their homogeneous maximum is zero, so the
displayed expression equals \(\ell_p+c_n\ell_q\) on every finite
valuation branch and at the two proper-support endpoints, where both
sections vanish. Its value at the generic trivial valuation is zero.
No undefined difference of infinite values is used.

Thus \(\psi_n\searrow\ell_E\) on all of \(X^{\mathrm{an}}\),
with \(c_1(L)=\theta=[E]\) fixed. On the two branches, for \(s>0\),
\[
\begin{array}{c|ccc}
 v&\ell_E(v)&\psi_n(v)&\psi_n(v)-t_n\ell_E(v)\\ \hline
 s\operatorname{ord}_p&-s&-s&(t_n-1)s\\
 s\operatorname{ord}_q&-s&-c_ns&(t_n-c_n)s.
\end{array}
\]
On all other finite branches both section functions are zero.
Consequently, positive coefficients satisfying
\(\psi_n\le t_n\ell_E\) must satisfy \(t_n\le c_n<1\).
The slice \(K_E=\{\ell_E=-1\}\) consists of
\(\operatorname{ord}_p,\operatorname{ord}_q\), and
\(\sup_{K_E}\psi_n=-c_n\to-1\).

If the section-defined residuals were decreasing, evaluation at
\(\operatorname{ord}_p\) would force \(t_n\) to be nonincreasing.
A nonincreasing net whose every coefficient is less than one cannot
converge to one: after any index its values are at most that index's
coefficient. The same argument applies after every cofinal reindexing,
because the residual at \(\operatorname{ord}_p\) is always \(t_i-1\)
and the bound is always \(t_i<1\).
Therefore **no admissible choice converging to one makes the residuals
decreasing for this fixed approximation**. This is stronger than merely
exhibiting one poorly chosen coefficient sequence.

This does not exclude replacing the entire approximation by another one.
Indeed, the constant approximation \(\psi_i=\ell_E\) works here,
and the critical residual is zero in \(\mathrm{PSH}(0)\).
The diagnostic concerns the published inference and its repair by
coefficient reselection, not the division theorem.

## Why constants or a raw global limit do not repair this family

Suppose finite constants \(a_i\) are added to the residuals.
For any fixed index \(i\), convergence \(t_j\to1\), together with
\(t_i<1\), gives a later index \(j\) with \(t_j>t_i\).
On \(s\operatorname{ord}_p\), the difference of corrected residuals is
\[
 (t_j-t_i)s+a_j-a_i.
\]
It is positive for a sufficiently large positive rational \(s\).
Hence no finite additive constants make the family decreasing on all
divisorial points. A uniform estimate on the slice alone cannot control
all divisorial rescalings. The constants used in BJ22's uniform-closure
proof do not provide such an estimate here.

For the canonical choice \(t_n=c_n\), section division is explicit:
divide both degree-\(2n\) sections by
\((z_0z_1)^{n-1}\). The quotient sections are
\(z_0^2,z_0z_1\), and their normalized maximum is
\[
 \rho_n=\frac1n\ell_p
 \in\mathrm{PSH}_{\mathrm{hom}}\bigl((2/n)[\mathcal O(1)]\bigr).
\]
The class shown is \(\theta-c_n[E]\); the residual's own divisor
class \((1/n)[p]\) is smaller, with the remaining nef slack.
On divisorial points \(\rho_n\to0\). At the proper-support endpoint
\(v_{p,\mathrm{triv}}\), however, each section-defined residual is
\(-\infty\). Its raw global pointwise limit is zero away from that
endpoint and \(-\infty\) at it, so is not upper semicontinuous.
The required psh residual is its zero extension, not that raw limit.
This makes the extension issue visible without forming
\(-\infty-(-\infty)\).

The [exact arithmetic script](research_calculations/bj22_siu_two_branch_20261004.py)
checks the two-section degrees, branch values, classes, and finite
rescaling witnesses. The finite samples supplement the universal
arguments above; they do not replace them or constitute an independent
verification receipt.

## Source-checked route ledger

| Proposed route | What is available | What remains missing |
| --- | --- | --- |
| Reselect the rational divisor coefficients | Dini gives admissible coefficients tending to one. | The fixed two-branch approximation above admits no decreasing residual family for any such choice. A different approximation would need a new construction. |
| Add small constants and diagonalize | BJ22 Lemma 4.6 proves nested decreasing closure; Theorem 4.7 proves uniform closure using constants. | Lemma 4.6 still starts with an outer decreasing net. The rescaling calculation excludes repairing this family by finite constants. Neither result supplies arbitrary pointwise closure. |
| Extract a compact subnet of residuals | BJ22 Theorem 5.11 identifies normalized psh compactness with the envelope property. | Using compactness before establishing that property assumes the target input. Corollary 6.22 also explicitly invokes Theorem 6.21 itself. |
| Divide at fixed \(t<1\), then let \(t\uparrow1\) | The strict fixed-coefficient argument gives psh residuals in classes \(\theta-t[E]\). | These residuals increase. BJGreen24 Proposition 17 uses independently established envelopes in its smooth characteristic-zero setting; it does not provide a general pre-envelope repair. |
| Pull back to a smooth model and descend | BJ22 Theorem 4.32 gives descent after adding an ideal-section error and an ample-class error. | Exact birational descent in Lemma 5.13 uses the envelope property. Shrinking the ideal error produces an increasing family, so smooth division alone does not discharge the missing normal descent input. |
| Extend the divisorial trace by semicontinuity | BJ22 Theorem 4.22 and Corollary 4.23 determine an already psh extension uniquely. | They do not prove existence or psh membership of an arbitrary limiting trace. The proper-support example above shows why a raw pointwise limit is insufficient. |

This ledger rejects these routes as complete independent repairs **on
the cited inputs alone**. It does not prove that every possible refinement
of them must fail.

## Primary-source and evidence scope

The controlling published BJ22 PDF is the same one pinned in the prior
audit, DOI [10.5802/afst.1705](https://doi.org/10.5802/afst.1705).
Fresh text was read at lines 830--885, 1535--1685, 2880--3135,
3270--3445, 3540--3805, 4150--4253, and 4290--4410.
Previously read gaps in those larger scopes were recovered explicitly.
Fourteen selected actual pages were viewed: physical pages
19, 34--35, 63--66, 71--72, 79--80 and 89--90, 92.
The Lemma 4.6 diagonal proof and Theorem 5.11 equivalence were read in
full; selected actual pages are not a whole-paper review.

BJGreen24's independent envelope standing scope and Proposition 17
were freshly reread at lines 575--714. Its actual physical page 13
was viewed at the preceding Siu checkpoint; that same-byte historical
view is reused rather than called a new view. Its controlling DOI is
[10.5802/crmath.579](https://doi.org/10.5802/crmath.579).
The companion manifest pins source files, these scopes, actual-page
records and exact arithmetic. No new acquisition or exhaustive current
literature search is asserted.

All active book inputs, the 86-page catalogue and 42-atom statuses
remain unchanged in this follow-up. The critical `(SD)_k` input is
unresolved. Continue with alternative approximation constructions and
precisely scoped related literature; do not use a rejected route as a
new theorem or an envelope proof.
