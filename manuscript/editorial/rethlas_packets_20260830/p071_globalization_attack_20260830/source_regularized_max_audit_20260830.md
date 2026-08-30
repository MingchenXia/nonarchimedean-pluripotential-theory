# P07.1 source and regularized-maximum audit

Date: 30 August 2026

Status: staging only; no live-book input; no production Rethlas claim.

## Exact source map

The audited CLD PDF has SHA-256
f659b1fd1423baba9552c03e4738f59e5ee985df0bbf671c8ce9d9718a5d0629.
The following are the exact source statements relevant to the proposed
globalization.

| CLD location | What it supplies | What it does not supply |
|---|---|---|
| Sections 3.1.1--3.1.3 and Definition 3.1.4 | Hausdorff local compactness, a basis of opens countable at infinity, domains, and the G-sheaf of piecewise-affine functions | A common neighbourhood inside a countable family of neighbourhoods |
| Definition 6.2.1 and Section 6.2.2 | The sheaf of smooth forms/functions and stability under \(\mathrm d'\), \(\mathrm d''\), \(J\), and wedge product | Positivity under multiplication by an arbitrary smooth function |
| Corollary 6.2.4 | A smooth plateau equal to one near a compact set and compactly supported in a prescribed open set, assuming local differential separation | A psh or convex plateau |
| Proposition 6.2.7 | Smooth partitions of unity on a paracompact, locally differentially separated affine G-tropical space | Psh partitions of unity |
| Proposition 6.3.2(a) | Local extension of a smooth form from a domain at a decent point | Preservation of \(\mathrm d'\mathrm d''\geq0\) |
| Proposition 6.3.2(b)--(c) | Global, and compactly supported, smooth extension under decency and local differential separation | Preservation of psh positivity; its proof multiplies local extensions by smooth partition functions |
| Definition 8.1.1 and Lemma 8.1.4 | The minimal psh sheaf, the transfinite hierarchy, and local successor presentations | De-sheafification of countably many local rows onto one fixed open set |
| Definition 8.1.13 | Locally approachable means membership in \(\operatorname{Psh}_{X,1}\) | A fixed-domain presentation for a countable family of locally approachable sections |
| Proposition 8.2.1 | Smooth convex coordinatewise nondecreasing composition preserves psh and the current ordinal stage | Extension of a branch beyond the open set on which it is defined |
| Corollary 8.2.3 | A finite maximum of stage-\(\alpha\) psh functions is psh at stage \(\sup(\alpha,1)\) | A smooth stage-zero maximum; a domain-gluing theorem |
| Proposition 12.4.7 | The analytic affine G-tropical structure is decent at an almost-good point | Local affine separation or a psh extension theorem |
| Corollary 15.2.4 | Local holomorphic separation implies local differential separation | Psh cutoffs |
| Corollary 15.2.5 and Proposition 15.2.8 | Analytic versions of the smooth plateau and partition-of-unity results | Positivity of those functions |

No CLD proposition in this chain states that a smooth psh function on a
domain extends as a smooth psh function to a larger neighbourhood, or that
local decreasing psh rows can be fused on a prescribed relatively compact
open set.

## Positivity audit of the cutoff route

On the standard affine tropical line, smooth psh functions are smooth convex
functions.  A compactly supported smooth convex function \(h\) is zero:
\(h'=0\) on both tails and \(h'\) is nondecreasing, so \(h'=0\)
everywhere, and compact support then gives \(h=0\).  Therefore the
nontrivial plateau supplied by CLD Corollary 6.2.4 is necessarily non-psh in
this model.

For a local smooth psh function \(v\) and a smooth cutoff \(\chi\), the
exact formula is

\[
\mathrm d'\mathrm d''(\chi v)
 =\chi\,\mathrm d'\mathrm d''v+v\,\mathrm d'\mathrm d''\chi
  +\mathrm d'\chi\wedge\mathrm d''v
  +\mathrm d'v\wedge\mathrm d''\chi.
\]

Only the first term has a controlled nonnegative sign.  The CLD cutoff and
extension propositions provide no estimate absorbing the other three terms.
Thus the naive operation “multiply by a CLD plateau and extend by zero” is
not a positivity-preserving commonization procedure.

This is a precise no-go result for the **naive cutoff/partition route**.  It
does not prove that every nonlinear or geometry-adapted globalization method
is impossible.

## Regularized-maximum audit

The validated regularized-max-negativity-budget card applies locally after
both branches are defined on an overlap.  In the present fully psh case both
negative-index budgets are zero.  For a smooth convex, coordinatewise
nondecreasing, translation-equivariant regularized maximum \(M\), put
\(w=M(u,v)\).  Its Hessian is

\[
\mathrm d'\mathrm d''w
 =a\,\mathrm d'\mathrm d''u+b\,\mathrm d'\mathrm d''v+P,
\]

where \(a,b\geq0\), \(a+b=1\), and \(P\geq0\) is the
Hessian-gradient term.  Hence \(\mathrm d'\mathrm d''w\geq0\).  This is
the real/tropical version of the identity written in CLD Proposition 8.2.1;
Corollary 8.2.3 gives the nonsmooth finite maximum at the appropriate stage.

The card explicitly warns that this signature calculation does not provide
**exact branch agreement**.  To extend the glued function past the boundary
of one branch's domain, the other branch must dominate by more than the
regularization width on a boundary collar.  CLD stage-one presentations give
pointwise decreasing convergence, not such two-sided uniform collar gaps.
The cutoff route that might manufacture those gaps has the uncontrolled
Hessian terms above.

Accordingly, the regularized-maximum mechanism stops at a missing
quantitative dominance-collar hypothesis.  It validates positivity of a
fusion once that hypothesis is furnished; it does not furnish the
globalization.

## Interaction with the exact \(X_B\) obstruction

The frozen \(X_B\) packet, independently audited in
independent_exact_byte_audit_20260830.md, shows more than a shrinking-open
topology: a prescribed countable family of smooth-psh germs has no common
smooth-psh representative domain.  The negative centre derivative on
\(b_n\) is legal only while that branch is exceptional; on any common
standard neighbourhood, some \(b_n\) is full, and constant-collar
convexity forbids the negative derivative.

This proves that neither stalks, smooth extensions, cutoffs, nor a formal
regularized maximum can commonize arbitrary chosen rows.  It leaves open the
only relevant existential possibility: re-select entirely different rows
for the given stage-one sections.  The zero target in the packet has global
constant rows, so the distinction is concrete.

## Conclusion

The source audit proves non-availability of the naive
positivity-preserving cutoff/partition/global-extension route.  It does not
prove impossibility of all globalization.  P07.1 remains open outside the
positive models already listed in Chapter 16.  A positive solution still
requires a genuinely new relative Richberg/fusion theorem, a quantitative
strictly psh barrier construction, or a presentation-independent comparison
sheaf with fixed-domain regularization.
