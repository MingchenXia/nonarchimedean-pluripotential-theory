# P06.2 curve arbitrary-field candidate: hostile exact-byte audit

**Date:** 2026-08-30
**Verdict:** **PASS** for the frozen mathematical candidate; no blocking defect found.
**Status boundary:** this is a research audit, not a production Rethlas verification and not authorization for live-book insertion.

## Frozen inputs

- statement SHA-256: 67a8d8a21e23cb34cf9b8f6685efbf2c9eaa6ff484b3696cbc1867a8940e095c
- proof SHA-256: 479643ee3aa534bbfc98adcf69837356d3cd8eff22d92accd1319aabb049553e

The two TeX files were read only. A fresh minimal pdflatex build with halt-on-error succeeded. No live-book file was edited.

## Differential re-audit

The statement is byte-identical to the preceding audited version. The proof changed from SHA-256 be2b0d5214eed40a3c76379af7aba85c31b2153bdee0f1571d3a2cd971316ae6 only in the following two source-fidelity repairs:

1. proof lines 14--17 now say that CLD Theorem 16.3.3(d) makes \(H_j\) \(G\)-smooth, hence continuous;
2. proof lines 154--157 now quote Berkovich Proposition 2.1.15 only for strict affinoid domains, apply it directly to \(D_R^+\), and obtain the open-disc case locally from a strict-affinoid covering.

Both changes replace earlier harmless overstatements by the precise primary-source conclusions. Neither changes a hypothesis, current identity, degree calculation, endpoint argument, or density conclusion. No mathematical regression was found.

## 1. Arbitrary continuous multiplier and continuity of the finite trace

The key proposition is supported by the cited primary results.

1. On an affinoid target domain \(U\), the finite inverse image \(Y_U\) is affinoid. It is locally holomorphically separated, so CLD Theorem 15.2.6 applies to the continuous restriction \(h|_{Y_U}\) and gives ordinary smooth \(h_j\to h\) uniformly.
2. A finite morphism is boundaryless. For relative dimension zero, flatness and CLD Theorem 16.3.3(d) make

   \[
       H_j(x)=\int_{Y_x}h_j
   \]

   \(G\)-tropically \(C^\infty\), hence continuous. The revised proof now states exactly this output.
3. CLD Sections 13.3.1--13.3.2 and Lemma 13.3.8 identify the calibrated zero-dimensional fibre mass with the ordinary finite-flat degree. Thus every fibre has mass \(d\), including ramified, nonreduced, residue-extension, defective, and inseparable contributions, and

   \[
      \|H_j-\operatorname{Tr}_p(h)\|_\infty
       \le d\|h_j-h\|_\infty.
   \]

   This proves continuity of the trace without labeling sheets.
4. CLD Corollary 16.5.5 states exactly \(p_*[\omega]=[u_\omega]\). Its dense-flat-locus and \(p\)-compact-support hypotheses hold here because \(p\) is finite flat. Passing to the uniform limit against compactly supported top-degree test forms proves

   \[
                    p_*[h]=[\operatorname{Tr}_p(h)].
   \]
5. CLD 7.7.8 gives commutation of compact direct image with \(d'\) and \(d''\). Restriction to an ordinary open \(V\) therefore gives the asserted zero-Hessian trace identity.

I found no counterexample at a ramification merger: the calibrated fibre weights, not the number of underlying points, are what remain constant. Likewise, in characteristic \(p\), a one-point purely inseparable fibre may carry degree \(p\), exactly as required.

## 2. Minimal-polynomial finite maps

For a rigid point \(y\), the monic irreducible polynomial \(P\) has degree \(d=[\mathscr H(y):K]\), and its zero fibre is the single underlying analytic point \(y\). Completeness of \(K\) gives a unique extended absolute value on finite algebraic extensions. Hence every conjugate of \(T(y)\), counted with inseparable multiplicity, has norm \(s=|T(y)|\), and

\[
                         |c_j|\le s^{d-j}.
\]

These bounds prove the claimed inverse-image identities:

- if \(s<R\), then \(|P(x)|<R^d\) exactly when \(|T(x)|<R\);
- if \(s\le R\), then \(|P(x)|\le R^d\) exactly when \(|T(x)|\le R\).

Outside the source disc the leading monomial strictly dominates. Since \(P(T)-Z\) is monic of degree \(d\) in \(T\), the induced disc maps are finite free of rank \(d\). This remains valid for inseparable \(P\).

## 3. Hostile audit of the single Gauss fibre

This is the most delicate point, and the argument survives the audit.

At the source \(t\)-Gauss point let \(U\) be the homogeneous residue of \(T\), and at the target \(q=t^d\) Gauss point let \(V\) be the homogeneous residue of \(Z\). The coefficient bound makes the initial polynomial

\[
               f(U):=\operatorname{in}_t(P)(U)
\]

nonconstant of degree \(d\). In the strict outer case \(t>s\), it is simply \(U^d\); at the closed endpoint \(t=s=R\), lower terms may remain, but the degree is still \(d\).

Because \(U\) is graded-transcendental, \(f(U)\) is graded-transcendental. Therefore composition with \(P\) sends the \(t\)-Gauss valuation to the \(q\)-Gauss valuation. Moreover,

\[
 [\widetilde K^{\bullet}(U):\widetilde K^{\bullet}(f(U))]=d.
\]

One way to see the lower bound, avoiding circular use of irreducibility, is the valuation at infinity: \(f\) has pole order \(d\), so the ramification index at infinity of the rational-function extension is \(d\). The opposite inequality follows because \(U\) satisfies \(f(X)-f(U)\), of degree \(d\). This argument retains the purely inseparable part when the characteristic divides \(d\). Equivalently, \(f(X)-V\) is irreducible over the graded rational field in \(V\).

The graded fundamental inequality now forces analytic local degree at least \(d\) at \(\eta_t\). Finite flatness says that the sum of all local fibre degrees is exactly \(d\). Hence

\[
                       p^{-1}(\xi_{t^d})=\{\eta_t\},
              \qquad  \deg_{\eta_t}(p)=d.
\]

Thus there is no omitted branch, no separability assumption, and no loss of multiplicity.

## 4. Closed-disc interior and both endpoints

For the strict closed disc, the absolute analytic boundary is the single Gauss point \(\eta_R\), and the target boundary is \(\xi_{R^d}\). Applying the preceding calculation separately with \(t=R\) gives

\[
                        p^{-1}(\xi_{R^d})=\{\eta_R\}.
\]

Therefore the inverse image of a compactly supported test form in the target interior is compact and lies in the source interior, where the current equation for \(h\) is assumed. This justifies the target trace equation in the closed case. It also covers the \(s<R\) branch: the boundary calculation uses \(t=R\) separately from the interior radius \(s<t<R\) used later.

At the zero endpoint, \(P^{-1}(0)=\{y\}\) with calibrated mass \(d\), so \(H(0)=d h(y)\). At the chosen outer or boundary Gauss point, the single-fibre calculation gives \(H(\xi_q)=d h(\eta_t)\). The already frozen rational-centred Gauss trace theorem then yields \(h(y)=h(\eta_t)=h(0)\).

## 5. Density citation

Berkovich Proposition 2.1.15 states density of rigid/maximal points for a strictly affinoid space over a nontrivially valued field. It applies directly to \(D_R^+\). Since \(R\in|K^\times|\), the open disc \(D_R^-\) is a strict analytic space and is locally covered by strict affinoid neighborhoods, so the same density conclusion is local and applies there as well. The revised proof now matches this literal scope and local argument.

## 6. Separate Chapter 18 source defect

The audited Chapter 18 source, SHA-256 b1a8b00d223f71ce00991a4b85f6b20a077f2ef3e140aa82280339649060ab45, cites “CLD Proposition 4.6.6” at lines 2028--2041 as an analytic tropical fibre theorem. In the checked primary CLD text, Proposition 4.6.6 is instead *Compensation des bords* (boundary compensation), not a finite-fibre/calibration theorem. Thus lem:ch18-fibre-cylinder is not supported by that citation as written.

This citation defect does not enter the frozen curve proof: its continuous trace is supplied by CLD 15.2.6, 16.3.3(d), and 16.5.5, with degree normalization from Sections 13.3.1--13.3.2 and Lemma 13.3.8. No live-book correction was made in this audit.

## Final disposition

**PASS** on the exact hashes above. The two former wording notes have been resolved without mathematical regression. The candidate still requires the requested production Rethlas verification before it can be called verified or moved into the live book.
