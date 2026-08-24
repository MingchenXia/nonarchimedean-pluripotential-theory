# Alignment of the simplified envelope manuscript with Part IV

**Source supplied:** *The envelope property for unibranch projective varieties*,
version 4, 34 pages, received 19 August 2026.  Filed as
`source_material/envelope/envelope_simplified.pdf`; extracted text for grepping at
`refs/envelope_simplified.txt`.

**Status.** This supersedes the earlier supplied archive as the proof source for
Chapters 37--45.  It is still an unpublished manuscript, so the book's existing
discipline is unchanged: results proved only here are identified as coming from a
supplied manuscript and are never presented as previously published theorems.

---

## 1. The good news: the book's chapter decomposition already matches

The manuscript's proof chain is

\[
  \text{smooth}\ \xRightarrow{\ \text{Thm 4.1}\ }\ \text{normal}
  \ \xRightarrow{\ \text{Cor 5.6}\ }\ \text{unibranch}\ \ (\text{Thm 7.1}),
\]

and its five working sections map onto the book's chapters essentially one to one.
No restructuring of Part IV is required.

| Manuscript | Result | Book chapter |
|---|---|---|
| §2.1--2.2 | Prop 2.1 (the psh property package), Def 2.2 (EP), Prop 2.3 (increasing-net form) | Ch. 34, Ch. 36 |
| §2.3 | Legendre slices (2.4)--(2.5), homogeneous Siu division (2.6) | Ch. 35 |
| §2.4 | b-divisors, coefficient function, dictionary | Ch. 35, App. F |
| §2.5 | obstacle reduction, \(Q_L\le P_L\), reduction to big rational classes | Ch. 36, Ch. 40 |
| §2.6 | asymptotic test ideals; the valuative bound (2.10) | Ch. 40, App. C |
| §2.7 | subintegral extensions; additive powers (2.11) | Ch. 44, App. A |
| §2.8 | Stacks toolbox (8 items, tagged) | App. I |
| §3.1 | Lemma 3.1, ordered rational approximation | **Ch. 38** |
| §3.2 | **Prop 3.2, Cartier realization** | **Ch. 38** |
| §3.3 | Thm 3.3, homogeneous birational descent (\(\beta^*\) a bijection) | **Ch. 39** |
| §3.4 | Lemma 3.4 (dyadic carrier), Thm 3.5 (carrier descent) | **Ch. 39** |
| §3.5 | Lemma 3.6 (canonical carrier), Thm 3.7 (EP descends birationally) | **Ch. 39** |
| §4 | Thm 4.1 (smooth, all characteristics), Lemma 4.2 | **Ch. 40** |
| §5.1--5.3 | Lemma 5.1 (analytic openness), Prop 5.2 (fibre average), Cor 5.3, Lemma 5.4 (flattening) | **Ch. 41** |
| §5.4 | Thm 5.5 (EP descends along finite maps) | **Ch. 41** |
| §5.5 | **Cor 5.6 (normal case, via de Jong alterations)** | **Ch. 42** |
| §6.1--6.4 | Lemma 6.1--6.3, Prop 6.4 (Frobenius, char \(p\)) | **Ch. 43** |
| §6.5 | Lemma 6.5 (additive-power sandwich), Prop 6.6 (char 0) | **Ch. 44** |
| §6.6 | Thm 6.7 (descent through normalization), Lemma 6.8 | **Ch. 43/44 shared** |
| §7 | Thm 7.1 = Theorem A | **Ch. 37, Ch. 45** |

---

## 2. What is genuinely simpler here, and should be adopted

Five things in this version are cleaner than the architecture the first draft was
written against, and the remaining chapters should follow them.

**(a) Cartier realization does not presuppose the envelope property.**
Prop 3.2 realizes the coefficient function of an anti-effective real Cartier
b-divisor with nef total class as a homogeneous psh function, via an explicitly
ordered tower of rational semiample approximations — built by *activating* the
support of \(\mathbb B\) with a single divisor \(F\) pulled back from \(X\), and
extracting a relatively ample buffer on \(Y\).  This is exactly the firewall the
book has been enforcing by hand, and it is now a property of the proof rather than
a side condition.  Chapter 38's expansion independently arrived at the same
activation/buffer structure, which is a good sign.

**(b) The homogeneous carrier replaces ad hoc boundedness hypotheses.**
General psh functions are not controlled by constants.  The manuscript's device
(Lemma 3.4, Thm 3.5, Lemma 3.6) is: dominate \(u\) by \(p+C\) with \(p\)
homogeneous, decompose \(u\) into homogeneous Legendre slices, descend the
compactly supported part slice by slice, and let \(p\) control the tail — with a
summable dyadic grid keeping the construction monotone.  Lemma 3.6 then shows that
when the source has EP, the envelope of all sup-normalized psh functions *is* such
a carrier, for every psh function.  Chapter 39 should be checked against this.

**(c) Finite descent by a universal norm polynomial.**
Prop 5.2 is the sharpest simplification.  After Raynaud--Gruson flattening
(Lemma 5.4) the pure transform becomes finite flat \(q:W\to Z\) of rank \(d\), and
one descends a GF function \(\varphi=\frac1m\max_j\{\log|s_j|+\lambda_j\}\) by
norming the coefficients of the **universal weighted linear form**
\(N_q(\sum_j T_j s_j)\), weighting by \(\sum_j I_j\lambda_j\) and normalizing by
\(1/(md)\).  The result computes the exact fibre average
\[
  \operatorname{Av}_q(\varphi)(z)=\frac1d\sum_{w\mid z}e(w/z)\,\varphi(w)
\]
at **every** analytic point.  The manuscript is explicit that norming a universal
linear form, rather than a product over chosen geometric sheets, is what makes the
formula valid in inseparable and nonreduced fibres and at points where both sides
are \(-\infty\).  This is precisely the generality Chapter 41 needed, and Chapter 41
should be re-read against it — its expansion already flagged a false universal
property in this area.

**(d) The valuative test-ideal bound is isolated as (2.10).**
\(w(\tau(I^t))\ge t\,w(I)-A_S(w)\), from Canton's log-discrepancy bound for Cartier
algebras.  This is the characteristic-\(p\) replacement for the multiplier-ideal /
valuation-ideal comparison, and Chapter 40 should cite it in exactly this form.

**(e) Prop 2.1 as a stated package.**
The manuscript never needs the definition of \(\mathrm{PSH}(X,\theta)\) — only six
listed properties, with PSH2 (decreasing nets with *converging classes*) as item
(1).  This vindicates the correction made to Chapter 34 earlier in this session:
the class must be allowed to vary, and PSH2 is the operative closure property.
Chapter 34 should adopt Prop 2.1's list as its statement of the package, cited to
the manuscript and to BJ22b.

---

## 3. Consequences for chapters already expanded

- **Ch. 34.** The corrected `def:bj-psh` (varying classes) agrees with the
  manuscript.  Consider restating the closure package in the form of Prop 2.1(1)--(6);
  in particular item (6) — every \(\theta\)-psh function attains its supremum at
  \(v_{\mathrm{triv}}\), and homogeneous psh functions are nonpositive — is used
  repeatedly downstream and is worth having as a numbered statement.
- **Ch. 38.** Cross-check the realization theorem against Prop 3.2 and Lemma 3.1.
  The activation divisor, the buffer path (3.4)--(3.6), and the rational stages
  (3.7)--(3.10) give an exact template.
- **Ch. 39.** Cross-check against Thm 3.3 (six steps), Lemma 3.4, Thm 3.5,
  Lemma 3.6, Thm 3.7.
- **Ch. 40.** Cross-check against Thm 4.1 and Lemma 4.2, and adopt (2.10).
- **Ch. 41.** Cross-check against Lemma 5.1, Prop 5.2, Cor 5.3, Lemma 5.4, Thm 5.5.

None of these is a correction of record until it is actually checked; this section
is a work list, not a claim that the chapters are wrong.

---

## 4. Bibliography

The manuscript cites `Can20` (Canton, log discrepancy of Cartier algebras),
`RS93`/`RRS96` (Roberts--Singh additive powers), `Swa80` (Swan, seminormality),
`Mus12` (Mustaţă, uniform generation), `Jon96` (de Jong, alterations),
`RG71` (Raynaud--Gruson), `HY03`, `BMS08`, `ST12`, `Fer98`, `Duc20`, `DF22`,
`Sho03`, `Cor07`.  Any of these not already keyed in
`bibliography/*.bib` must be added before being cited — never invented inline.
