# Chapter 55 Cao locator primary-source audit

**Audit date:** 2026-08-24 (Asia/Shanghai)  
**Rethlas run rejected:** `20260824T045229Z_703e3b501202`  
**Verdict:** **PASS.  The run's sole criticism is a primary-source locator
false positive and is rejected.**  Chapter 55 correctly cites Cao,
Proposition 4.4.  The paper has a Lemma 4.3 and no Proposition 4.3.

## Controlling primary source

The controlling persistent file is
`tmp/pdfs/Cao14_arxiv1210.5692_primary.pdf`, 35 pages and 309,281 bytes,
with SHA-256
`17717664b0ae2b154e76e2ecb68c9f63f09dc74be6f25bac7f04b7ee0103b0d6`.
It is the PDF of arXiv:1210.5692 used for the bibliography entry `Cao14`.
The source was checked by layout-preserving text extraction and by direct
visual inspection of physical pages 17 and 19.

## What the primary source says

Physical page 19 visibly begins the numerical criterion with the heading
**Proposition 4.4**.  For a pseudo-effective metrized line bundle
\((L,\varphi)\) on a projective variety and a very ample line bundle \(A\),
it characterizes \(\operatorname{nd}(L,\varphi)=d\) by saying that the
\(\varepsilon\)-logarithmic order of

\[
 \overline{\lim}_{m\to\infty}
 \frac{h^0\!\left(X,m\varepsilon A+mL\otimes
              \mathcal I(m\varphi)\right)}{m^n}
\]

is \(n-d\).  The bar on the inner limit is visible in the primary PDF.
The first paragraph of the proof, still under Proposition 4.4, compares
sections defined by \(\mathcal I(m\varphi)\), by the upper-regularized ideal
\(\mathcal I_+(m\varphi)\), and by \(\mathcal I((m+1)\varphi)\), and concludes
that the ordinary and upper-regularized ideals have the same asymptotic
behavior needed in the criterion.

Physical page 17 says that the deferred estimate is proved in Lemma 4.3 and
then displays the heading **Lemma 4.3**.  A complete text scan of Section 4
finds Proposition 4.2 followed by Proposition 4.4, while the intervening
number 4.3 belongs to the lemma.  No occurrence of a heading “Proposition
4.3” exists in the PDF.

## Match with Chapter 55

The current live Chapter 55 source has 64,938 bytes and SHA-256
`b2134d6b59f7687f8f5f296023a7d80703122210909032856b965f12f61619ab`.
The intervening Schneider locator corrections occur before, and change no
byte of, the toric theorem or proof interval audited here.
At live line 1488 it cites `\cite[Proposition~4.4]{Cao14}` and immediately
uses the same projective data, ordinary multiplier ideal, normalization by
\(m^n\), and outer logarithmic quotient.

There is no hidden limsup mismatch.  Cao's statement uses the inner
\(\overline{\lim}\).  Chapter 55 has already proved the stronger assertion
that the normalized toric section count has an actual limit along the
integers for which \(m\varepsilon\) is integral.  Hence its sentence “Since
the preceding inner limit exists” legitimately replaces Cao's limsup by that
limit.  Restricting \(\varepsilon\downarrow0\) to positive rationals is the
natural Cartier-divisibility interpretation of Cao's expression and does not
change the logarithmic exponent.  The use of the ordinary multiplier ideal
is also exactly what Proposition 4.4 states; the comparison with
\(\mathcal I_+\) is part of that proposition's proof.

Thus every interface used at the decisive final step of
`thm:ok-toric-zero-mass` matches the primary source:

| Interface | Cao, Proposition 4.4 | Chapter 55 |
|---|---|---|
| Geometric setting | projective, pseudo-effective metrized line bundle; very ample \(A\) | same after the explicit rational denominator clearing |
| Section count | \(h^0(X,m\varepsilon A+mL\otimes\mathcal I(m\varphi))\) | the identical space counted by toric characters |
| Normalization | division by \(m^n\) | division by \(m^n\), with no \(n!\) |
| Inner asymptotic | limsup | an actual limit, hence the same limsup |
| Outer exponent | \(n-d\) | \(n-\nu_{\mathrm{Cao}}(T)\) |
| Ideal convention | ordinary \(\mathcal I\); proof compares \(\mathcal I_+\) | ordinary \(\mathcal I\), with that comparison explicitly noted |

## Rejection of the run finding

The archived raw response for run
`20260824T045229Z_703e3b501202` has one critical error and no gaps.  It says
that the displayed criterion and the ordinary/upper-regularized comparison
belong to Proposition 4.3 and recommends changing `4.4` to `4.3`.  Both
parts of that assertion are contradicted by physical page 19; physical page
17 independently shows why the proposed number is impossible.

Accordingly, the run verdict `wrong` does not control the mathematical or
bibliographic status of this proof.  Its only finding is explicitly rejected
as a source-locator hallucination.  Chapter 55 and Chapter 69 require no edit
for this issue.  No Rethlas submission was made in this audit.
