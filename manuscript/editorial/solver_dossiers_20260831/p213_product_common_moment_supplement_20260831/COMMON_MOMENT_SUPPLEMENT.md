# Explicit common-moment premise for the source-ratio comparison

Date: 31 August 2026. Author: `/root/p082_independent_reaudit`.

## Status and relation to the frozen note

This small supplement strengthens and makes explicit the sufficient compatibility premise in the final accessibility paragraph of Section 6 of `p213_product_current_separation_research_20260831/RESEARCH_NOTE.md`. That original note remains unchanged, SHA-256 `d4f1458e0849164c1a45d168238467c13222ccae427493069ed97f43cd789b81`. Its branch calculation and mixed-rank obstruction are not modified.

The parent identified the need for this precision: affine agreement on overlapping source-skeleton patches does not, by itself, identify two ordinary pullback forms on an analytic neighbourhood. The comparison below instead evaluates each of those forms through an actual common analytic moment. It is an explicitly conditional sufficient criterion, not a proof that its hypotheses occur for arbitrary charts. The separate source-calibration representation remains an assumed input, not a theorem independently certified here. This is an authored research supplement, not an independent audit or production acceptance.

## Explicit sufficient hypotheses

Retain the dimension-two product X and positive closed ordinary CLD current T of the frozen note. Let V be an ordinary open subset of X on which the representation premise below is assumed. Let

\[
 f:V\longrightarrow\mathbf G_m^{m},\qquad
 g:V\longrightarrow\mathbf G_m^{n}
\]

be analytic moments. Denote their tropical maps by F and G, and set

\[
 h=(f,g),\qquad H=(F,G),\qquad
 H:V\longrightarrow E_F\times E_G.
\]

Thus H is the tropicalization of the **actual analytic moment h on the same ordinary open V**. Let p_F and p_G denote the two ambient affine projections. In particular, F=p_F H and G=p_G H on all of V, not just on a skeletal patch.

Assume all of the following.

1. For each J in {F,G,H}, T has the source-cell formula (R) in the frozen representation packet, on V, with arbitrary smooth compactly supported source multipliers and no lower-dimensional residual coefficient measure. The canonical current delta_X restricted to V has the same kind of formula on the same cell decomposition. Let b_J >= 0 and a_J > 0 denote their constant coefficients on the cells selected below, in the chosen affine coordinates.
2. Choose represented compact two-dimensional source cells C_F, C_G, C_H, on each of which its own tropical map is affine and injective. There is an ordinary open U contained in V and a nonempty source subset P such that, for all three J,

   \[
   U\cap\Sigma_J^{(2)}=U\cap C_J^{\circ}=P.                    \tag{S1}
   \]

   All equalities here are equalities of subsets of the actual analytic source. The circle denotes relative interior. This is the explicit isolation assumption: the support of a source cutoff in U encounters no other represented top cell for any of the three moments. In particular P is a nonempty relatively open patch in each selected cell. Any lower-dimensional terms vanish by premise 1.
3. On the affine span L_H of H(C_H), each projection p_J, J in {F,G}, has rank two; its affine image is the span L_J of J(C_J). In affine coordinates x on L_H and y_J on L_J, write

   \[
   y_J\circ p_J=A_J x+c_J,\qquad \det A_J\ne0,
   \qquad j_J=|\det A_J|>0.                                   \tag{S2}
   \]

Premise (S1) is intentionally stronger than vague overlap or refinement language. No inclusion or equality of these source skeleta is deduced merely from target images meeting or from a rank calculation. If (S1), the common analytic moment, or its representation is unavailable in a proposed application, this criterion supplies no comparison for that application.

Under these assumptions the conclusion is

\[
 \frac{b_F}{a_F}=\frac{b_H}{a_H}=\frac{b_G}{a_G}.                \tag{S3}
\]

In particular a previously known G-ratio c gives the F-ratio c on the selected F-cell, since these coefficients are constant on that cell by premise 1. No assertion is made that every F-cell has such a comparison.

## Proof through H, with the normalization displayed

Choose a point of P. Goodness and separation give local holomorphic separation, so the ordinary source cutoff statement CLD Corollary 15.2.5 supplies a smooth compactly supported function on U equal to one near that point. Square it if necessary. We obtain rho >= 0, with support compactly contained in U and rho=1 near that point. Put

\[
 I=\int_{x(H(P))}
       \rho\bigl((x\circ H|_P)^{-1}(\xi)\bigr)\,
       \mathrm d\xi_1\,\mathrm d\xi_2.
                                                                    \tag{S4}
\]

The inverse is well defined by injectivity. The integral is finite, since the contributing subset is the image of supp(rho) intersected with the compact cell C_H, and it lies away from the cell boundary by (S1). It is strictly positive because rho=1 on a nonempty relatively open patch of the two-cell.

For J=F or G, extend the affine coordinates y_J from L_J to affine functions on the ambient E_J and let

\[
 \alpha_J=\mathrm d'y_{J,1}\wedge\mathrm d''y_{J,1}\wedge
           \mathrm d'y_{J,2}\wedge\mathrm d''y_{J,2}.
\]

These forms need not have compact target support: multiplication by rho makes their pullbacks legitimate compactly supported ordinary test forms. The crucial identities are the actual ordinary pullback identities

\[
 \rho F^*\alpha_F=\rho H^*(p_F^*\alpha_F),\qquad
 \rho G^*\alpha_G=\rho H^*(p_G^*\alpha_G),                       \tag{S5}
\]

which hold on V because h is the concatenated analytic moment. We do **not** identify F^*alpha_F with a G-pullback on an ordinary neighbourhood.

Evaluate the J-test in (S5) first using J's representation. The isolation assumption removes every cell but C_J, and the shared-source identity in (S1) identifies its contributing patch with the very same P. Changing from y_J to x via (S2) gives

\[
 \langle T,\rho J^*\alpha_J\rangle=b_J j_J I.                   \tag{S6}
\]

Evaluate this same J-test using H's representation. On L_H the algebraic rule for superform pullback gives

\[
 p_J^*\alpha_J|_{L_H}
    =(\det A_J)^2\,
      \mathrm d'x_1\wedge\mathrm d''x_1\wedge
      \mathrm d'x_2\wedge\mathrm d''x_2.
\]

The determinant occurs twice, once in each differential block, so its square is independent of orientation. By H's representation and (S1),

\[
 \langle T,\rho J^*\alpha_J\rangle=b_H j_J^2 I.                 \tag{S7}
\]

Since I and j_J are positive, (S6)-(S7) imply b_J=j_J b_H. Apply precisely the same two evaluations to the same test with the canonical current in place of T. Premise 1 then gives a_J=j_J a_H. Dividing these two relations proves b_J/a_J=b_H/a_H for J=F and J=G, hence (S3). No division by b_J or b_H is made, so zero current coefficients cause no exception.

This proof compares each pullback with itself through H. The square determinant in the form and the absolute determinant in Lebesgue change of variables are both included. Nothing in the proof turns agreement of forms on a source skeleton into agreement of ordinary forms off that skeleton.

## Boundary of the clarification

The only conclusion is the ratio comparison (S3) under premises 1-3. In particular, the common moment H and its represented, isolatable shared source top cell are not optional. A finite chain of comparisons would require verifying these premises for every link; no such chain or universal accessibility is asserted here. The original rank-collapse examples are not removed by this conditional clarification.

The all-moment separation implication in the earlier note still requires equality on every relevant ordinary moment's source top cells, together with the full representation premise. This supplement neither proves that premise nor supplies the missing access to all source cells. There is no new claim of product rigidity, no broader P21.3 result, no field-scope expansion, and no production or live-manuscript change.
