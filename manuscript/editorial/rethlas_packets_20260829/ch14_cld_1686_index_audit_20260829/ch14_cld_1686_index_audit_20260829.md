# Quarantine audit: the Hausdorff exponent in CLD Corollary 16.8.6

Date: 29 August 2026

Status: **correction required; no live file has been edited**.

## Frozen inputs

- live chapter inspected:
  `manuscript/parts/part2/ch14_currents.tex`, SHA-256
  `a3127a670613678e1bc9c950f37e6ef5e9c297711db8f195386d04579ca9d6b0`;
- CLD source PDF: arXiv:1204.6277v2, 25 July 2025, SHA-256
  `f659b1fd1423baba9552c03e4738f59e5ee985df0bbf671c8ce9d9718a5d0629`;
- extracted CLD source text, SHA-256
  `24920a1f4c8bd4944c83d89c8747c95b0206ae0754053eb0ed4d3de95e0f7727`.

The source files are frozen under
`manuscript/editorial/rethlas_packets_20260829/`
`p213_trivially_valued_curve_candidate_audit_20260829/sources/`.

## Exact live ranges

1. `ch14_currents.tex:2888--2936`.  The citation to
   `Corollary 16.8.6` is at line 2933.  The relevant theorem statement is at
   lines 2888--2896, and the scalar-extension paragraph is at lines
   2928--2935.
2. `ch14_currents.tex:3497--3501`.  The second citation to
   `Corollary 16.8.6` is at line 3501, in the source ledger.
3. The chapter's conventions are fixed at lines 164--172: on a pure
   `n`-space, bidegree `(a,b)` means bidimension `(n-a,n-b)`.

## Exact source ranges

In the frozen extracted CLD text:

- Definition 16.8.3 is at lines 23619--23624.
- Theorem 16.8.5 is at lines 23629--23632.  It pairs a positive closed
  current of bidimension `(r,r)` with an `(r,r)`-form and assumes tropical
  `H^r`-negligibility.
- Corollary 16.8.6 is at lines 23671--23674.  Its symbol `p` counts the
  curvature factors, so its Bedford--Taylor current has bidegree `(p,p)` and
  bidimension `(n-p,n-p)`, while the complementary smooth form has bidegree
  `(n-p,n-p)`.
- The proof says explicitly that the nontrivially valued case is a special
  case of Theorem 16.8.5 (lines 23675--23677), and its Gauss-extension
  argument is at lines 23680--23697.
- Proposition 16.8.2 and its reminder of Proposition 8.7.5 are at lines
  23594--23603; they give Shilov support and exact pushforward for the
  scalar-extended Bedford--Taylor current.

## Mathematical diagnosis

The exponent printed in CLD Corollary 16.8.6 is wrong.  If `q` is the number
of curvature factors, then

```text
bidegree of T       = (q,q),
bidimension of T    = (n-q,n-q),
degree of alpha     = (n-q,n-q).
```

Theorem 16.8.5 therefore applies with its bidimension parameter equal to
`n-q`, and the required Hausdorff exponent is `n-q`.  Thus the `H^p` printed
in Corollary 16.8.6 must be `H^{n-p}` when the corollary's `p` denotes the
number of curvature factors.  The corollary's own first proof sentence forces
this substitution.

The book repeats the same index collision at lines 2928--2935: the symbol
`p` in Theorem `thm:cld-positive-support` denotes the **bidimension**, but the
display at line 2929 uses the same `p` as the **number of curvature factors**.
Except when `n=2p`, that product has bidimension `(n-p,n-p)`, not `(p,p)`, so
the preceding theorem cannot be applied as written.  In addition, the current
theorem statement assumes a nontrivial valuation and does not state the
trivially valued conclusion proved in its last paragraph.

The correct minimal translation into the chapter's notation is to use
`n-p` curvature factors in the trivially valued clause.  The resulting
Bedford--Taylor current has bidegree `(n-p,n-p)` and bidimension `(p,p)`;
the chapter's `H^p` hypothesis and its `(p,p)` smooth factor are then exactly
the corrected `H^{n-q}` and `(n-q,n-q)` conditions with `q=n-p`.

The occurrence at line 3501 does not itself print an exponent, but it
currently conceals the index error and attributes the support theorem jointly
to Theorem 16.8.5 and the misprinted corollary.  It should distinguish the
nontrivially valued theorem from the corrected scalar-extension statement.

No index change is needed in lines 2890--2926 or 2942--2958: there `p`
consistently denotes bidimension, as in Theorem 16.8.5.  There is, however, a
separate source-fidelity issue at lines 2901--2926: CLD Theorem 16.8.5 does
not state the displayed ball-growth estimate.  Its printed proof uses proper
tropical pushforward and Lagerberg's Euclidean negligibility theorem, exactly
as the chapter itself explains at lines 2938--2962.  The conclusion is
source-supported, but the sentence at lines 2925--2926 should not be read as
a citation for that stronger quantitative estimate.  This observation is
independent of the exponent correction below.

## Proposed minimal replacement text

### Replace lines 2888--2896

```tex
\begin{theorem}
\label{thm:cld-positive-support}
Let $T$ be a positive closed current of bidimension $(p,p)$ on $X$, and let
$A\subset X$ be closed and \emph{tropically $H^p$-negligible}: for every
compact analytic domain $V$ and every tropical chart
$f:V\to\mathbf R^r$, the set $f(A\cap V)$ has zero $p$-dimensional
Hausdorff measure.  Assume either that $|K^\times|$ is nontrivial, or that
$K$ is trivially valued and
\begin{equation}
\label{eq:ch14-trivial-bt-support-form}
             T=\bigwedge_{i=1}^{n-p}\dprimeddprime u_i
\end{equation}
for continuous dpsh functions $u_1,\ldots,u_{n-p}$ on $X$.  Then, for every
smooth $\alpha\in A_X^{p,p}(X)$, the measure $T\wedge\alpha$ does not
charge $A$.
\end{theorem}
```

This preserves the theorem label and makes the already-present second case
part of the statement.  The equation label is new and may be omitted if the
project prefers an unnumbered display.

### Replace lines 2928--2936

```tex
It remains to treat the trivially valued case in
\eqref{eq:ch14-trivial-bt-support-form}.  Put $q=n-p$, so that $q$ is the
number of curvature factors.  The scalar-extension argument in the proof of
\cite[Corollary~16.8.6]{CLD25} applies with this indexing.  In the printed
statement of that corollary, $H^q$ must be read as $H^{n-q}$: the current
$\bigwedge_{i=1}^q\dprimeddprime u_i$ has bidegree $(q,q)$ and hence
bidimension $(n-q,n-q)$, so this is the exponent required by
\cite[Theorem~16.8.5]{CLD25}.  Here $n-q=p$, exactly the exponent in the
hypothesis above.

More explicitly, after passing to a one-radius Gauss extension, the proof of
that corollary shows that the Shilov image of $A$ is tropically
$H^p$-negligible.  The scalar-extended measure is supported on the Shilov
image by \cite[Proposition~16.8.2]{CLD25}, and it pushes forward to
$T\wedge\alpha$ by \cite[Proposition~8.7.5]{CLD25}.  Applying
\cite[Theorem~16.8.5]{CLD25} upstairs and pushing forward proves that
$T\wedge\alpha$ does not charge $A$.
\end{proof}
```

This proof uses the source's actual mechanism and records rather than repeats
the printed index error.

### Replace the final clause of lines 3497--3501

Replace

```tex
the projection formula for Bedford--Taylor products is
\cite[Theorem~16.5.7]{CLD25}, and the support theorem is
\cite[Theorem~16.8.5 and Corollary~16.8.6]{CLD25}.
```

by

```tex
the projection formula for Bedford--Taylor products is
\cite[Theorem~16.5.7]{CLD25}, and the support theorem over a nontrivially
valued field is \cite[Theorem~16.8.5]{CLD25}.  Its scalar-extension form for
Bedford--Taylor products uses \cite[Proposition~16.8.2 and
Proposition~8.7.5]{CLD25} and the proof of
\cite[Corollary~16.8.6]{CLD25}; in the printed statement of that corollary,
$H^p$ must be read as $H^{n-p}$ when $p$ is the number of curvature factors.
```

## Scope of this audit

This report proposes text only.  It does not modify the live chapter, change
any theorem label, or claim that the separate quantitative ball-growth sketch
at lines 2901--2926 has been independently proved.
