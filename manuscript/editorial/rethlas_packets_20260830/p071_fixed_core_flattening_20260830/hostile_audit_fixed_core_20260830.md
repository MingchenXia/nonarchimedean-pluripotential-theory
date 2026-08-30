# Hostile audit of the frozen P07.1 fixed-core packet

Date: 2026-08-30

Result: **PASS**.

This is a fail-closed audit of the exact frozen mathematical inputs

- `statement.tex`, SHA-256
  `b29ccabac98982c239fcedcc34a701c9a9bb98ca95710d6ed7fbaa3f0f96e4d9`;
- `proof.tex`, SHA-256
  `7677ba46620cc4cef8a74d502cdf9fde344e045b04bbc66a4274a5c20b1838c2`.

No live-book file was edited and no Rethlas call was made in this audit.

## 1. Exact hypotheses and domains

The argument uses only the following consequences of the stated hypotheses.

1. A compact neighbourhood \(K\) of \(x\) has an open interior \(K^\circ\)
   containing \(x\).
2. Every row domain \(\Omega_n\) is open and contains all of \(K\).  Hence,
   at each finite induction stage, the finitely many functions being compared
   are defined on the open intersection of their domains, which is an open
   neighbourhood of \(K\).  The proof never requires the countable
   intersection \(\bigcap_n\Omega_n\) to be open.
3. Smooth real-valued functions on an affine \(G\)-tropical space are
   continuous.  Thus every strict comparison locus used in the compactness
   argument is open.
4. A decreasing row \(v_{n,k}\downarrow u_n\) dominates its possibly
   \(-\infty\)-valued limit pointwise.  No continuity or finiteness of
   \(u_n\) is used.

These dependencies are all explicit in the statement or part of the cited
CLD definitions.  In particular, the theorem does not silently assume a
single ambient open set on which all rows are defined.

## 2. Uniform diagonal choices

Fix an induction stage \(n\).  For every \(y\in K\), each target on the
right-hand side of (4)--(5) is finite and continuous, while

\[
 u_{n+1}(y)\leq w_n(y),\qquad
 u_{n+1}(y)\leq v_{r,s}(y)\quad(1\leq r,s\leq n).
\]

Since \(\delta_n>0\) and \(v_{n+1,k}(y)\downarrow u_{n+1}(y)\), one index
works for the finitely many strict inequalities at that point, including
when equality holds at the row limit or when the row limit is \(-\infty\).
For each \(k\), the simultaneous strict-comparison locus is open; these loci
increase with \(k\) because the row is decreasing, and they cover \(K\).
A finite subcover followed by taking the largest of its indices yields one
index \(k_{n+1}\) valid on all of \(K\).  Thus the compactness step is sound
and makes no unjustified Dini or uniform-convergence assumption.

## 3. Positivity and monotonicity

The tails

\[
 c_n=\sum_{m\geq n}\delta_m
\]

are finite, satisfy \(c_n=\delta_n+c_{n+1}\), and tend to zero.  Restriction
to \(K^\circ\) and addition of the constant \(c_n\) preserve smoothness and
the inequality \(\mathrm d'\mathrm d''\geq0\).  Inequality (4) therefore
gives, pointwise on \(K^\circ\),

\[
 g_{n+1}=w_{n+1}+c_{n+1}
 <w_n+\delta_n+c_{n+1}=g_n.
\]

Hence the claimed non-strict monotonicity \(g_{n+1}\leq g_n\) follows (in
fact it is strict).  There is no sign error in the tail correction.

## 4. Identification of the limit

The easy bound is

\[
 g_n\geq w_n\geq u_n\geq u,
\]

so \(g:=\inf_n g_n\geq u\).  For fixed \(r,s\), whenever
\(N-1\geq\max\{r,s\}\), condition (5) from the selection of \(w_N\) gives

\[
 g_N=w_N+c_N<v_{r,s}+\delta_{N-1}+c_N.
\]

Letting \(N\to\infty\) yields \(g\leq v_{r,s}\), because both error terms
tend to zero and \(g_N\downarrow g\).  Taking the infimum first over \(s\)
and then over \(r\) gives

\[
 g\leq u_r\quad\text{for every }r,
 \qquad g\leq\inf_r u_r=u.
\]

Thus \(g=u\), including at points where \(u=-\infty\).  The expanding
finite-square requirement (5) is exactly what closes the limit-identification
gap; (4) alone would not suffice.

## 5. Conditional CLD consequence

Under the final hypothesis of `statement.tex`, the preceding local argument
applies to every point of \(U\).  Consequently the pointwise decreasing
limit of any sequence in \(\operatorname{Psh}_{X,1}(U)\) belongs locally,
and hence by the sheaf property globally, to
\(\operatorname{Psh}_{X,1}(U)\).  This sheaf contains
\(\operatorname{Psh}_{X,0}\) and is then stable under the operation in CLD
Definition 8.1.1.  Minimality gives
\(\operatorname{Psh}_X\subseteq\operatorname{Psh}_{X,1}\), while CLD's
transfinite construction gives the reverse inclusion.  The equality in (2)
is therefore valid **only under the stated fixed-core realization property**.

The packet does not claim that arbitrary affine \(G\)-tropical spaces have
that property.  The research memo repeatedly labels the result conditional,
states that P07.1 remains open, and identifies common-core
extension/globalization as the residual obstruction.  Its discussion of CLD
Proposition 16.9.1 does not promote that barrier construction to an
unproved extension theorem.  Thus neither the statement nor its surrounding
interpretation claims an unconditional collapse of the CLD hierarchy.

## 6. Fail-closed conclusion

No quantifier mismatch, domain incompatibility, compactness gap, strictness
error, positivity defect, tail-correction error, or limit-identification gap
was found.  The cited CLD definitions supply exactly the two inclusions used
in the conditional final paragraph.  The frozen statement and proof are
dependency-closed for their asserted conditional theorem and are suitable
for the next independent verification gate without modification.
