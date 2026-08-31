# Source coefficients on a proper target-open restriction

Date: 1 September 2026. Research author: /root.
Status: authored conditional localization argument; independent and production verification pending. Not a live-book theorem or a priority claim.

## 1. The domain issue being checked

The finite-projection packet describes a current given on an entire completed tube. An ordinary-open locality argument may instead give a current only on the full inverse image of a small target box. One must not silently extend that current to the full tube. This note checks that the source-coefficient comparison can be proved entirely on the smaller domain.

The exact conditional input (L) is

`../../solver_dossiers_20260831/p213_nonreduced_tube_finite_projection_research_20260831/RESEARCH_NOTE.md`,

SHA-256 `3001c94985c0d3e60f184ffd9f0e9591775ea026a98cd20ee538005edac11b7a`.

We use its geometric finite-flatness/properness statement, canonical calibration, and unramified-DVR single-Gauss-source assertion. We do NOT apply its whole-domain current statement to a current defined only on a smaller domain. The representation premise (R) below means only the precise displayed source-multiplier identity in the frozen source representation statement, not its additional unverified local-affine-separation wording.

Root authored L. This localization argument requires a different independent reviewer; previous acceptance of L is not an audit of the new domain check.

## 2. Statement

Let K be complete discretely valued, pi a uniformizer, and \(\ell=-\log|\pi|>0\). Let L/K be finite unramified of degree d, let m be a positive integer, and let \(a_1,\ldots,a_n\ge0\), where \(n\ge1\). Let epsilon be a bounded formal unit over \(L^\circ\) with unit constant coefficient. Consider the actual punctured tube
\[
 D=\{x^m\epsilon(x,z)\prod_{j=1}^nz_j^{a_j}=\pi,
                 \quad 0<|x|,|z_j|<1\},
\]
viewed as a K-analytic space. Let g be the moment \((z_1,\ldots,z_n)\), and
\[
 q=\operatorname{trop}(g):D\longrightarrow
 Q=\{u_j>0:\ \textstyle\sum_j a_ju_j<\ell\}.
 \tag{2.1}
\]
Assume the geometric conclusions of L. For ANY nonempty connected ordinary open subset \(\Omega\subset Q\), put \(D_\Omega=q^{-1}(\Omega)\). This is the full inverse image, not a chosen source sheet. Let T be a positive separately \(\mathrm d'\)- and \(\mathrm d''\)-closed current of bidegree (0,0) given only on \(D_\Omega\).

There is a finite b greater than or equal to zero such that, with
\(\omega=\bigwedge_{j=1}^n\mathrm d'u_j\wedge\mathrm d''u_j\),
\[
 \langle T,q^*(h\omega)\rangle
                 =b\int_\Omega h\,\mathrm d u,
 \qquad h\in C_c^\infty(\Omega).
 \tag{2.2}
\]
For the canonical integration current, b=md.

Assume in addition the displayed representation identity R on the actual ordinary source \(D_\Omega\) with moment g. Namely its locally finite source cells have constant nonnegative coefficients in the coordinates u; for every compact ordinary smooth source multiplier rho and every smooth target top form, the pairing is the sum of the source-cell integrals with those coefficients and no lower-cell residual term. Then every full-dimensional convenient source-cell coefficient is b, its canonical coefficient is md, and therefore its normalized ratio is
\[
                              \frac{b}{md}.
 \tag{2.3}
\]
In particular for every such compact rho and target top form alpha,
\[
 \langle T,\rho q^*\alpha\rangle
       =\frac{b}{md}\langle\delta_{D_\Omega},\rho q^*\alpha\rangle.
 \tag{2.4}
\]
Here delta denotes the canonical integration current. Equation (2.4) is an equality for the specified g-based tests, including arbitrary compact SOURCE multipliers. It is not an assertion about all ordinary top forms for all possible moments.

## 3. Properness after restriction and the target constant

The tube D is good, separated, boundaryless and pure n-dimensional by the geometric L premise. Its ordinary open subset \(D_\Omega\) has those same properties. The target \(\Omega\), being open in Euclidean space, admits a countable compact exhaustion. Properness of q makes the corresponding full inverse images compact and gives a countable compact exhaustion of \(D_\Omega\). In particular this locally compact Hausdorff space is paracompact, as required for the stated R interface.

For a compact subset H of \(\Omega\), its inverse image under the restricted q is the same compact \(q^{-1}(H)\) as in D. It lies entirely inside \(D_\Omega\). Hence every compact target test, including a primitive of bidegree (n-1,n), pulls back to a compact ordinary test on the current's actual domain.

Push T forward by these compact pairings. Positivity makes its top-coefficient distribution a positive Radon measure \(\mu\) on \(\Omega\). For each j, testing \(\mathrm d'T=0\) against the pullback of a scalar test times the coordinate form with \(\mathrm d'u_j\) omitted gives
\[
                      \int\partial_j h\,\mathrm d\mu=0.
 \tag{3.1}
\]
The exterior sign is irrelevant because the expression is zero. Thus every distributional first derivative of mu vanishes.

Convolve on a ball whose closure lies in \(\Omega\) with nonnegative smooth approximate identities. On a smaller ball the resulting smooth density has all first derivatives zero, hence is constant. Testing a fixed nonnegative scalar function of integral one on a still smaller ball identifies its finite constant in the distributional limit. Thus mu is a constant multiple of Lebesgue measure locally. Overlapping balls identify the constants, and connectedness of \(\Omega\) identifies them globally. This proves (2.2), without convexity of \(\Omega\) or an extension of T.

The canonical coefficient md restricts from L's actual finite-degree computation: degree m over L and the full finite-field calibration factor d when the same space is viewed over K. This is not a scalar extension of an unknown current.

## 4. Individual source cells, not just a positive aggregate

We recall exactly why the geometric single-source assertion applies on this smaller domain. The vectors \(u\) for which \(\ell,u_1,\ldots,u_n\) are Q-linearly independent form a dense subset of every nonempty open subset of \(\Omega\). The finite fibre algebra above the L-Gauss point of such radii has dimension m. Its residue fields contain x with valuation
\[
                    \frac{\ell-\sum_j a_ju_j}{m}.
\]
This value has exact order m modulo \(\ell\mathbf Z+\sum_j u_j\mathbf Z\). Hence each residue field has degree at least m. The total dimension m forces the entire fibre algebra to be one field of degree m, with no other factor or nilpotent length. It therefore has one analytic point. This is L, Section 6, applied to the geometric fibre, not to T. The finite unramified coefficient extension gives the same unique source over the K-Gauss point as in L, Section 7. Its use is unaffected by restricting the tropical target to \(\Omega\).

For this n-coordinate moment the characteristic skeleton is the preimage of the torus Gauss skeleton. It is closed in \(D_\Omega\). Its full-dimensional cells map affine-injectively to full-dimensional target cells. Refine the R decomposition to convenient cells if necessary; the displayed coefficients restrict unchanged. The canonical local degree is constant on each convenient cell interior, by CLD Proposition 14.2.2. Its open target image contains independent u as above, so its local degree is m over L and its canonical coordinate coefficient is md over K.

Two distinct top-cell interiors cannot have images overlapping on a nonempty target open: that open would contain an independent u and thus two distinct points above its Gauss point, contradicting uniqueness. This only rules out overlapping top-cell images here; it is not a general assertion for arbitrary finite maps or ramified coefficient extensions.

Fix a top cell C. Choose a target ball with compact closure in its open image and in \(\Omega\). Properness makes the full inverse image of that closure compact. Closedness of the characteristic skeleton and local finiteness of the cell decomposition imply that only finitely many cells meet that compact. Avoid the finitely many lower-dimensional images of their faces, and shrink to a smaller ball. Its top-dimensional source-cell contribution can now only be C. This exclusion uses actual source cells over a proper target compact; it is not a selection of just the visible points of a target cone.

Choose a scalar test h of integral one in that smaller ball. Its full inverse-image support is compact in \(D_\Omega\). Choose an ordinary smooth source cutoff rho equal to one on a neighbourhood of that compact. Then \(q^*(h\omega)=\rho q^*(h\omega)\). Formula R applied on \(D_\Omega\) expresses this actual pairing as the coefficient of C times the integral of h, whereas (2.2) gives b. The coefficient of C is therefore b.

All full-dimensional cells have thus been compared; the R identity has no lower-cell residual. Comparing it with the canonical source-calibration definition of integration proves (2.4) for every compact multiplier rho. Neither the unknown current nor its derivatives have been extended by zero. Only compact test forms have been used.

## 5. How this applies to local residual functionals

Suppose a separate modelled-curve argument, for a current defined only on an ordinary neighbourhood W, provides full inverse-image collar boxes
\[
 D_p=q_p^{-1}(B_p\times(0,\delta_p))\subset W,
\]
with constant target coefficients \(\lambda_T(p)=c_T[\kappa(p):k]\). This is an EXPLICIT additional premise, not established in the present note. For the actual coordinate tube at p substitute m=N_0 and \(d=[\kappa(p):k]\) in the preceding proof. Provided R is available on that actual collar, its displayed coordinate-moment cells have normalized ratio
\[
 \frac{\lambda_T(p)}{N_0[\kappa(p):k]}=\frac{c_T}{N_0}.
 \tag{5.1}
\]
The ratio is independent of p for those collar cells. The current need not be defined on the whole original residual-curve tube for this implication.

This supplies only the local source-cell interpretation of a separately proved residual functional. It does not construct the model or the independent normal point, show that any prescribed analytic cell meets a controlled collar, access cells contracted by a coordinate projection, or compare all unrelated moments. In particular it does not resolve full P21.3 or justify an open-problem retirement.
