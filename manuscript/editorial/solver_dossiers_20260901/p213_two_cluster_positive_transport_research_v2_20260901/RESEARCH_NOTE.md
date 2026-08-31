# Two-cluster coefficient transport through the old moment's rank-drop bridge

Date: 1 September 2026 (Asia/Shanghai).
Author: /root/p082_independent_reaudit.
Status: complete authored CONDITIONAL research argument, frozen with the companion manifest; fresh independent review and production verification are separate. No live book or predecessor packet is changed.

## 1. Exact scope and conditional inputs

Work over the ORIGINAL field \(K=\mathbb C((\pi))\), with valuation ring \(R=\mathbb C[[\pi]]\), residue field \(k=\mathbb C\), \(v=-\log|\cdot|\), and \(\ell=v(\pi)>0\). Fix \(n\ge2\), put \(d=n-1\), and write
\[
 X=(\mathbb P^1_K)^n,\qquad
 W=(U_1\times_K\mathbb G_{m,K}^{d})^{an},\qquad
 U_1=\mathbb A^1_K\setminus\{0,\pi,1,1+\pi\}.
 \tag{1.1}
\]
The coordinates of the torus factor are \(t_2,\ldots,t_n\); write \(u_i=v(t_i)\). This is an actual analytic product over K, not a Cartesian product assertion about analytic point sets.

Let T be a positive separately \(\mathrm d'\)- and \(\mathrm d''\)-closed ordinary CLD current of bidegree (0,0) GIVEN ONLY ON W. Define the actual analytic moments, recorded in valuation coordinates, by
\[
 f(z)=\frac{z(z-1)}{(z-\pi)(z-1-\pi)},\quad
 F=(v(f),u_2,\ldots,u_n),\quad
 H=(v(f),u_2,\ldots,u_n,v(z),v(z-1)).
 \tag{1.2}
\]
All their functions are analytic units on W.

Assume these exact interfaces:

- **L:** the frozen local finite-projection note, SHA256
  \(3001c94985c0d3e60f184ffd9f0e9591775ea026a98cd20ee538005edac11b7a\).
  We use geometric properness and canonical degree, with the field and parameter restrictions stated there.
- **O:** the frozen ordinary-open outer-collar note, SHA256
  \(f629a77106d023763c7b99626c1ec1f8f449164f3749de475bf18bb0661e1d5b\).
  We use its local residual functional and compact principal-divisor tests at an independent normal point, conditional on L. We do not use a whole-residual-tube current theorem for T on W.
- **Q:** the frozen proper target-open comparison note, SHA256
  \(35d4ae59a167025ef595aa50a45101619ed1aef586be39abebca1486c62857ec\).
  Its input is the FULL inverse image of a connected ordinary target open inside L's positive weighted slice.
- **R:** ONLY the displayed source-multiplier identity
  labelled `eq:p213-source-cell-formula` in the frozen representation statement, SHA256
  \(5c06cd6f091e5964a16c07b3efddd2104fed938447605f4f9b19ff8dfea01f1a\).
  Here the reference is to that source equation label, not a label defined in this Markdown note. Assume the displayed identity for the coordinate moments used below, F, H, and their ordinary restrictions: locally finite convenient source cells have constant nonnegative coefficients, arbitrary compact ordinary smooth source multipliers are allowed, and there is no lower-cell residual term. No unverified local-affine-separation assertion or theorem proving R is imported.

For a source cell, “normalized coefficient” means the coefficient of T divided by its positive canonical integration coefficient IN THE SAME affine coordinates. The theorem below remains conditional on these interfaces even where a simpler direct proof is possible.

The earlier two-cluster diagnostic is motivation and an exact pinned comparison input, not a proof of the new coefficient equalities. The author previously authored O and source-comparison diagnostics; this is not an independent audit of those inputs or of the present argument. Root requested this finite test and flagged the all-torus-radii domain issue. The explicit model chain and proof below require a fresh reviewer.

## 2. The four domains and the precise conclusion

For \(c=0,1\), put \(s_c=v(z-c)\) and define ordinary source domains
\[
 D_c^-=\{y\in W:0<s_c(y)<\ell\},\qquad
 D_c^+=\{y\in W:s_c(y)>\ell\}.
 \tag{2.1}
\]
Their coordinate moments are
\[
 q_c^-=(u,s_c),\qquad q_c^+=(u,\tau_c),\quad
 \tau_c=v((z-c)/\pi)=s_c-\ell.
 \tag{2.2}
\]
Each is the tropicalization of an actual torus coordinate system on a full polyannulus. The coordinates \(u=(u_2,\ldots,u_n)\) have NO sign restriction. The residual coordinate has range \(I^-=(0,\ell)\) or \(I^+=(0,\infty)\).

These are full source domains, not just their Gauss sections. Indeed, \(0<s_c<\ell\) means \(|\pi|<|z-c|<1\), while \(s_c>\ell\) means \(0<|z-c|<|\pi|\). In either case the four removed points are avoided by strict dominance. In particular no point of the torus polyannulus has been deleted covertly.

There is a SINGLE finite number \(\kappa\ge0\) with the following properties.

1. On each of the four domains, for every compact ordinary smooth source multiplier \(\rho\) and coordinate target top form \(\alpha\),
\[
 \langle T,\rho(q_c^\pm)^*\alpha\rangle
   =\kappa\langle\delta_W,\rho(q_c^\pm)^*\alpha\rangle.
 \tag{2.3}
\]
The same holds for H-based tests supported in any of the four domains and F-based tests supported in \(D_c^+\).
2. Every corresponding full-dimensional convenient R source-cell germ has normalized coefficient \(\kappa\). Thus the two selected old F top-cell families over \(s_c>\ell\) and both H connecting-strip families over \(0<s_c<\ell\) have the same ratio.
3. The equalities cross the central \(s=0\) Gauss family and the two \(s_c=\ell\) interfaces by explicit residual-curve tests; they are NOT inferred by continuity of a coefficient across a lower-dimensional cell.

We do not assert equality on every source cell of F or H. In particular this statement does not cover the pole branches near \(\pi\) and \(1+\pi\), nor the outward H branch \(|z|>1\), nor arbitrary moments on W. No coefficient is assigned to a lower-dimensional interface itself. Equation (2.3) is not whole-current rigidity on W.

Strict dominance gives these identities on the ENTIRE indicated domains:
\[
\begin{array}{c|c|c}
\text{domain}&F&H\\ \hline
D_0^-&(0,u)&(0,u,s_0,0)\\
D_1^-&(0,u)&(0,u,0,s_1)\\
D_0^+&(\tau_0,u)&(\tau_0,u,\ell+\tau_0,0)\\
D_1^+&(\tau_1,u)&(\tau_1,u,0,\ell+\tau_1).
\end{array}
 \tag{2.4}
\]
For example, in \(D_0^-\), \(|z-\pi|=|z|\) and both \(|z-1|\), \(|z-1-\pi|\) equal one; in \(D_0^+\), \(|z-\pi|=|\pi|\) while the latter two norms still equal one. The other two rows are identical calculations centered at one. Hence H has rank n on each coordinate source family, but F has rank only \(n-1\) on the two minus strips. The proof must genuinely cross this rank drop.

## 3. Full polyannuli: exact positive-slice exhaustion and connected constants

We first prove that each domain in (2.1) has a single coordinate coefficient \(b_c^\pm\), independent of ALL torus radii. This is a real argument with connected domains; “Q exhaustion” alone would not establish it.

Temporarily let \(\zeta\) be \(z-c\) for the minus case and \((z-c)/\pi\) for the plus case. Its valuation \(t\) ranges in \(I=I^-\) or \(I^+\). For every integer \(N\ge1\), introduce
\[
 T_i=\pi^N t_i,\quad U_i=v(T_i)=u_i+N\ell,\qquad
 D_N=\{u_i>-N\ell\text{ for every }i,\ t\in I\}.
 \tag{3.1}
\]
As a K-analytic space, \(D_N\) is exactly
\[
 \{x=\pi,\quad 0<|x|,|T_2|,\ldots,|T_n|,|\zeta|<1,\
                  (U,t)\in\Omega\},\qquad
 \Omega=\mathbb R_{>0}^{d}\times I.
 \tag{3.2}
\]
For \(I=(0,\ell)\) the last restriction is imposed explicitly. There are no extra excluded source points, by Section 2.

This is L with coefficient field K, \(m=1\), \(\epsilon=1\), and ALL \(n\) exponents \(a_j=0\). Its positive weighted slice is the whole positive orthant. The connected ordinary open \(\Omega\) in (3.2) is therefore literally an allowed Q domain. The current is restricted to this full inverse image; it is never extended. Q gives a finite \(b_N\ge0\), canonical coefficient one, and
\[
 \langle T,\rho q_N^*\alpha\rangle
               =b_N\langle\delta_W,\rho q_N^*\alpha\rangle,
 \qquad q_N=(U,t).
 \tag{3.3}
\]
The target constant is not postulated: in Q it follows from proper pullback of compact primitives, vanishing distributional first derivatives, and connectedness of \(\Omega\).

The domains \(D_N\) are nested. On their common part,
\(q_{N+1}=q_N+(\ell,\ldots,\ell,0)\).
Choose a nonnegative smooth target function of integral one compactly supported in a small box inside \(q_N(D_N)\), and translate that same function for \(q_{N+1}\). The two pulled-back top forms are IDENTICAL on the actual source. Their full support is compact in \(D_N\), by L/Q properness. An ordinary source cutoff equal to one near that compact makes (3.3) applicable without changing the form. The two coordinate derivatives and Lebesgue measures are unchanged by translation. Pairing this one form gives \(b_N=b_{N+1}\).

Every compact subset of \(D=\bigcup_ND_N\) lies in some \(D_N\): each continuous finite \(u_i\) has a lower bound there. Hence every compact source-multiplied coordinate test lies in one \(D_N\), and (3.3), after translation, gives a single number \(b_D\) on D. Applied four times this defines \(b_0^-,b_1^-,b_0^+,b_1^+\).

For completeness, the full tropical map \(q:D\to\mathbb R^d\times I\) is proper as a map of ordinary topological spaces. A compact target set has lower bounds on all u_i and lies in one translated positive slice; its full inverse image is then the same compact inverse image supplied by L there. This verifies properness on the full domain without changing the current's domain. It also gives an alternative direct connected-target proof of the constant, but the nested same-test proof above already establishes it.

Under R the coordinate source coefficients themselves, rather than only their aggregate, equal \(b_D\). This is Q's source conclusion on every \(D_N\). Geometrically these are ordinary torus polyannuli: their coordinate skeleton consists of the unique Gauss point at each radius. Its canonical coordinate coefficient is one. No arbitrary-current scalar extension is used in that statement.

Equation (2.4) now handles moment changes on these SAME domains. H is an affine injective function of q on each domain; F is likewise on a plus domain. Any H- or eligible F-based target top form pulls back to a smooth q-based top form by that displayed affine map. Equation (3.3) therefore gives the corresponding equality for arbitrary compact source multipliers. On an isolatable convenient top-cell interior R then reads the same coefficient equality. Alternatively refine the coordinate and given source decompositions and use a source cutoff on one shared interior. The local source sets agree because the tropical functions agree affinely on a full ordinary neighborhood, not merely on a target overlap.

In q-induced coordinates the canonical coefficient is one; changing affine coordinates multiplies the T and canonical coefficients by the same absolute Jacobian. Thus the normalized coefficients are \(b_D\). This step compares neither the two disjoint plus domains nor any rank-dropped F cell: those comparisons are the remaining work.

## 4. An original-R proper model with a whole central residual curve

Construct a torus model rather than assume semistable reduction. Start with
\(\mathcal Y^{(0)}=(\mathbb P^1_R)^d\), with its special divisor and the zero/infinity horizontal coordinate divisors. Near the point \(t_2=\cdots=t_n=0\), successively do the following, for \(i=2,\ldots,n\):

Blow up the connected component, through the tracked point, of the intersection of the current strict transform of the ORIGINAL special divisor and the strict transform of \(t_i=0\). Choose the \(t_i\)-pivot chart at the tracked point. If the current local equation is
\(\pi=t_2\cdots t_{i-1}x\), this chart has \(x=t_i x_{\mathrm{new}}\), so after the last step
\[
                         \pi=x_0t_2\cdots t_n.
 \tag{4.1}
\]

All centers here are actual closed regular codimension-two strata of an SNC pair, contained in the special fibre. Their connected components are closed: the intersection is regular, so its irreducible components are disjoint. The two coordinate blowup charts at a center \((x,y)\) are given by \(y=xv\) and \(x=yw\). The quotient presentation in either chart has one eliminated parameter; its remaining parameters, together with local parameters along the center, give a regular system. Equivalently, in the completed regular local ring the displayed substitution embeds the Rees chart in the fraction field and the resulting local ring is regular. There is no extra torsion component: the actual chart is \(A[y/x]\subset\operatorname{Frac}(A)\) or \(A[x/y]\). The coordinate boundary remains SNC. The new vertical multiplicity is the old vertical multiplicity plus the horizontal multiplicity zero, hence one.

These elementary chart calculations apply along the entire chosen centers, not just at the tracked point. Blowups are projective, integral, and isomorphisms off their vertical centers. The resulting model \(\mathcal Y\) is proper, regular, integral and flat over R (integrality implies R-torsion-freeness). Its generic fibre is the ORIGINAL \((\mathbb P^1_K)^d\). At the tracked k-rational point \(p_T\), exactly n selected multiplicity-one vertical components meet, with equations \(x_0,t_2,\ldots,t_n\). The connected component of their closed intersection containing \(p_T\) is \(\{p_T\}\), since it is a regular zero-dimensional scheme with that rational point.

Set
\[
                 \mathcal X_{\mathrm{cen}}
                     =\mathbb P^1_{z,R}\times_R\mathcal Y.
 \tag{4.2}
\]
This is proper, regular, integral and flat, with smooth generic fibre X. Smooth base change preserves the SNC boundary. The selected n vertical components now have WHOLE connected intersection
\[
                     C_{\mathrm{cen}}
                           =\mathbb P^1_k\times\{p_T\}.
 \tag{4.3}
\]
This is a smooth proper geometrically integral residual curve. It is not a punctured stratum.

Choose
\[
 \Delta=\{u_i>0,\ \textstyle\sum_{i=2}^nu_i<\ell\},\quad
 u^*\in\Delta,\quad
 \ell,u_2^*,\ldots,u_n^*\text{ Q-linearly independent},
 \tag{4.4}
\]
and put \(\alpha_i=u_i^*\) for \(i\ge2\) and
\(\alpha_0=\ell-\sum_i u_i^*\).
The n positive normal values \(\alpha_0,\alpha_2,\ldots,\alpha_n\) are Q-linearly independent: substitution in any rational relation gives a relation among the n numbers in (4.4).

There is a concrete analytic point \(\xi_{\mathrm{cen}}\): take the z-Gauss point of radius one and the relative torus Gauss point with radii \(\mathrm e^{-u_i^*}\). Its seminorm on a Laurent polynomial in t with rational z coefficients is
\[
 \left|\sum_I a_I(z)t^I\right|
       =\max_I |a_I|_{\mathrm{Gauss},z}\,
                                     \mathrm e^{-I\cdot u^*}.
 \tag{4.5}
\]
This is a multiplicative seminorm over K. The residue of z is transcendental over k, the normal parameters have the stated positive values, and all nonzero elements of \(k(z)\) have value zero. Consequently its center on (4.2) is exactly \(\eta_{C_{\mathrm{cen}}}\). Its generic algebraic support is generic, so it belongs to W. This uses the actual relative Gauss construction, not a nonexistent Cartesian identification of all analytic points.

Thus the exact independent-normal-point hypotheses of O hold at \(\xi_{\mathrm{cen}}\), with omitted component \(E_0=(x_0=0)\) and \(N_0=1\).

## 5. Central comparison: the two rank-drop strips

Apply O to \(C_{\mathrm{cen}}\), the current on W, and the residual rational function
\[
                      \bar g(z)=z/(z-1),\qquad
                 \operatorname{div}(\bar g)=[0]-[1].
 \tag{5.1}
\]
All closed points here have residue degree one. Denote its local collar coefficients by \(\lambda_{\mathrm{cen}}(p)\). O gives
\[
                 \lambda_{\mathrm{cen}}(0)
                         =\lambda_{\mathrm{cen}}(1).
 \tag{5.2}
\]

We make the actual domains and supports explicit. At p=0 use \(w=z\); at p=1 use \(w=z-1\). The entire completed p-tube has equation (4.1), with all normal coordinates and w of norm less than one. The retained moment is
\[
 q_p=(u,s=v(w)),\quad
 Q_p=\{u_i>0,\ s>0,\ \textstyle\sum_i u_i<\ell\},\quad
                     v(x_0)=\ell-\sum_i u_i.
 \tag{5.3}
\]
There is no additional vertical component at these points: the exponent of w is zero. O supplies a normal box about \(u^*\) and shallow intervals. Choose a connected box B with compact closure inside those boxes and \(\Delta\), and \(0<\delta<\ell\) sufficiently small. L properness holds on the FULL inverse image of \(B\times(0,\delta)\). That entire inverse image is inside \(D_0^-\), respectively \(D_1^-\), and thus inside W.

At the zero-order bad point infinity use \(w=1/z\). Its shallow punctured collar has \(|z|>1\), so is in W; the point w=0 itself, which would lie outside the affine W, is excluded by the collar cutoff. At closed residual points different from 0,1,infinity, the entire tube has \(|z|=|z-1|=1\), and therefore \(|z-\pi|=|z-1-\pi|=1\); it lies in W. Normal bounds keep every t_i finite and nonzero. At the generic point of C the same model-unit equalities apply. These are statements about all source points, including points not on a Gauss section.

Here is the actual compact-test identification, not an equality inferred from matching target images. With
\[
 \omega_{u,s}=
   \left(\bigwedge_{i=2}^n\mathrm d'u_i\wedge\mathrm d''u_i\right)
                               \wedge\mathrm d's\wedge\mathrm d''s,
 \tag{5.4}
\]
choose \(h\ge0\) smooth of integral one with compact support in \(B\times(0,\delta)\). The pulled-back form
\(q_p^*(h\omega_{u,s})\) has compact support inside W by the proper restriction of L. The p-tube model coordinates are exactly the rational coordinates \(t_i,z-c\) on that full source domain. Thus this is the SAME form as the \(q_c^-\)-pullback on its full support. A smooth source cutoff equal to one near the compact support can be inserted on both sides. By the definition in O its T-pairing is \(\lambda_{\mathrm{cen}}(p)\); by Section 3 it is \(b_c^-\). The canonical pairing is one. Hence
\[
               b_0^-=\lambda_{\mathrm{cen}}(0)
                      =\lambda_{\mathrm{cen}}(1)=b_1^-.
 \tag{5.5}
\]

For clarity, (5.2) uses one genuine compact primitive, not a slice of T. In O's construction take a nonnegative normal test \(\phi(u)\) of integral one, compactly supported sufficiently close to \(u^*\), and lift \(\bar g\) by the actual rational unit \(g=z/(z-1)\) wherever it is used. Put \(r=u\), \(t=v(g)\), and
\[
 \beta=\phi(u)\chi(t)
       \left(\bigwedge_{i=2}^n\mathrm d'u_i\wedge\mathrm d''u_i\right)
                                                  \wedge\mathrm d''t.
 \tag{5.6}
\]
Here \(\chi\) is one near zero and compactly supported in a sufficiently small interval. Cut off the deep 0-, 1-, and infinity-tubes by O's ordinary smooth function eta. At 0, \(t=s\); at 1, \(t=-s\); on the entire shallow infinity collar, \(v(g)=0\), so \(\mathrm d''t=0\). Off the bad tubes \(t=0\), so \(\chi'(t)=0\) on an ordinary neighborhood of each such point because \(\chi\) is constant near zero; this makes no assertion that \(\mathrm d''t=0\) there. Normal support and all shallow cutoffs may be chosen in the finite common boxes above. O's support proof, using actual compact closed polydiscs including w=0 where necessary and excluding it from the surviving support, shows that \(\eta\beta\) is a compact ordinary form INSIDE W. The zero-order infinity cutoff contributes nothing to \(\mathrm d'\eta\wedge\beta\). For the two nonzero orders choose the support of \(\chi\) before the cutoff transition. Then closedness of T gives
\[
 0=\langle T,\mathrm d'(\eta\beta)\rangle
   =-\lambda_{\mathrm{cen}}(0)+\lambda_{\mathrm{cen}}(1).
 \tag{5.7}
\]
The sign is \(\int_0^\infty m^2\chi'(ms)\,\mathrm ds=-m\) for \(m=1,-1\). This is exactly O's principal test specialized to the present source. No unknown current has been extended across the omitted rigid infinity.

## 6. Interface models at each cluster: the whole curve \(\zeta=(z-c)/\pi\)

Fix c=0 or 1. We construct a separate proper vertical modification of \(\mathcal X_{\mathrm{cen}}\). There is no need to identify the two modified models with each other: BOTH generic fibres remain X, so all analytic forms and T remain on the same original W.

Add the horizontal divisor \(z=c\) to the SNC pair near \(C_{\mathrm{cen}}\). It is globally smooth and meets that curve at one k-rational point. Starting there, use the ordered list of pivots
\[
                          t_2,t_3,\ldots,t_n,x_0.
 \tag{6.1}
\]
The omitted normal coordinate x_0 is deliberately LAST.

Write \(w_0=z-c\). At the j-th step blow up the connected component through the tracked point of the intersection of the selected vertical component with local equation equal to the j-th pivot and the strict transform of the horizontal divisor \(w_{j-1}=0\). Retain the pivot chart:
\[
                         w_{j-1}=x_{\mathrm{pivot}}w_j.
 \tag{6.2}
\]
The selected vertical component at that position is replaced by the exceptional component; all other selected components are retained. On this chart its rational equation is still the same pivot. Each new selected multiplicity is one. After the n steps,
\[
        \pi=x_0t_2\cdots t_n,\qquad
        z-c=\pi\zeta,\qquad w_n=\zeta.
 \tag{6.3}
\]

We justify the GLOBAL curve and not merely the affine \(\zeta\)-chart. At every step the center is a closed regular codimension-two component of the intersection of one vertical and one horizontal boundary component. The other n-1 selected vertical components are transverse to it; none contains that center. Near the tracked point their restrictions cut the center down to that single k-rational point. For a coordinate regular immersion of codimension two, the exceptional divisor is the projectivization of the rank-two normal bundle: this follows from the associated graded algebra of the two parameter ideal. Its intersection with the strict transforms of these other selected components is consequently the WHOLE \(\mathbb P^1_k\) fibre above that point, not a single affine chart of that fibre.

The selected n-component intersection is regular of dimension one by the SNC calculation. The displayed closed \(\mathbb P^1_k\) fibre is its connected component through the tracked point. Indeed it is irreducible, closed, dimension one, and a regular intersection cannot attach a different irreducible curve component at one of its points. The new strict horizontal divisor meets this fibre at w_j=0; the former pivot divisor meets it at w_j=infinity. The next tracked center is at the former point, not the latter. Induction gives a whole smooth proper connected selected intersection at every step.

The pair stays SNC by the two parameter-chart calculation in Section 4. These are actual proper modifications with vertical centers, not alterations, ramified base extensions, or merely formal chart replacements. Their generic maps are the identity. Let \(\mathcal X_c\) be the final model, and denote the final whole proper curve by
\[
                             C_c\simeq\mathbb P^1_k.
 \tag{6.4}
\]
Its finite coordinate is \(\zeta\), and its two displayed points are 0 and infinity. Earlier exceptional incidences lie away from the tracked next center and do not introduce an extra component through the new fibre except for the former LAST pivot at infinity.

There is an actual point \(\xi_c\) centered at \(\eta_{C_c}\): take the Gauss point in z centered at c of radius \(|\pi|\), equivalently the radius-one Gauss point in \(\zeta=(z-c)/\pi\), and the relative torus Gauss point with radii \(\mathrm e^{-u_i^*}\). In the intermediate charts
\[
 v(w_j)=\ell-\sum_{\text{first }j\text{ pivots}}v(x_{\mathrm{pivot}})
\]
is positive before the final step, and is zero for \(w_n=\zeta\). Thus the actual point follows the chosen charts; on the final chart the normal values are exactly \(\alpha_0,u_2^*,\ldots,u_n^*\), while the residue of \(\zeta\) is transcendental. Its center is the generic point of the WHOLE curve in (6.4), not a closed point of it. It belongs to W. O therefore applies again with these independent normal values and with the final selected x_0-component omitted.

## 7. Both charts at the interface, including the positive remaining margin

At \(p=0\) on \(C_c\), use \(w=\zeta\). The completed local model is (6.3), with no extra vertical w-factor. Its moment is
\[
 q_0=(u,t=v(\zeta)),\quad
 Q_0=\{u_i>0,\ t>0,\ \sum_i u_i<\ell\},\quad
                         v(x_0)=\ell-\sum_i u_i.
 \tag{7.1}
\]
A shallow full inverse image \(q_0^{-1}(B\times(0,\delta))\) is contained in \(D_c^+\), since \(s_c=\ell+t\). All coordinate multiplicities, including the omitted one, equal one.

The infinity chart is different and is essential. Just BEFORE the last blowup, put
\(y_0=w_{n-1}=(z-c)/(t_2\cdots t_n)\).
The last center is \((x_0,y_0)\). On its y_0-pivot chart write
\[
 w=x_0/y_0=1/\zeta,\qquad
 x_0=y_0w,\qquad
 \pi=y_0w\,t_2\cdots t_n,\qquad z-c=y_0t_2\cdots t_n.
 \tag{7.2}
\]
Here the selected omitted normal is y_0, not x_0. The other retained selected normals are STILL the original rational t_i, which is why (6.1) ended with x_0. The old last-pivot vertical component is \(w=0\), an EXTRA vertical component of multiplicity one. The residual parameter is w, and
\[
 q_\infty=(u,t_\infty=v(w)),\quad
 Q_\infty=\{u_i>0,\ t_\infty>0,\ \sum_i u_i+t_\infty<\ell\},
\]
\[
 v(y_0)=\ell-\sum_i u_i-t_\infty,\qquad
                          s_c=\ell-t_\infty.
 \tag{7.3}
\]
In particular the omitted normal at infinity is NOT assigned the old value \(\ell-\sum u_i\); its remaining margin is reduced by \(t_\infty\).

Take the finite intersection of all needed O normal neighborhoods around \(u^*\), shrink to a box B with compact closure in \(\Delta\), and set
\[
 \mu=\min_{u\in\overline B}\left(\ell-\sum_i u_i\right)>0.
\]
Choose the local shallow intervals, and then their common upper bound \(\delta\), so that
\[
                     0<\delta<\min(\mu,\ell).
 \tag{7.4}
\]
Normal support for principal tests can be chosen in a still smaller compact box before these upper bounds are decreased. Equations (7.1)-(7.4) put the ENTIRE target boxes inside their respective L domains and keep all selected normal values strictly positive. On the infinity collar, \(0<s_c<\ell\), so the full source is in \(D_c^-\). L properness on this box is properness of the full inverse image, not of a chosen Gauss section or component.

At the zero-order point \(\zeta=1\) for the residual function \(\zeta\), the current domain W removes the rigid point \(z=c+\pi\). Set \(w_1=\zeta-1\) and retain only \(0<v(w_1)<\delta_1\). On this whole shallow collar \(|\zeta|=1\), \(w_1\ne0\), and both z-punctures of this cluster are avoided. The other cluster is at distance one. Outside the closed residual points 0,1,infinity, every point of the corresponding whole tube satisfies \(|\zeta|=|\zeta-1|=1\); again it lies in W. At infinity (7.4) gives \(0<s_c<\ell\), so it cannot meet the other cluster or algebraic infinity. All torus coordinates remain nonzero and finite.

This supplies actual all-source W containment for all pieces of the finite residual test, including the order-zero removed branch. It is not enough to check only \(\xi_c\) or a skeleton.

## 8. The same compact tests compare the two sides of \(s_c=\ell\)

Write \(\lambda_c(p)\) for O's local residual coefficients on \(C_c\), with the omitted final component fixed as in Section 7. Its multiplicity is one in BOTH charts. Apply O to
\[
                       \bar g=\zeta,\qquad
                \operatorname{div}(\bar g)=[0]-[\infty].
 \tag{8.1}
\]
The residue degrees are one, so
\[
                            \lambda_c(0)=\lambda_c(\infty).
 \tag{8.2}
\]

At zero, choose a nonnegative \(h\) of integral one supported compactly in a box allowed in (7.1)-(7.4). The full support of \(q_0^*(h\omega_{u,t})\) is compact in W, and its coordinate functions are IDENTICALLY those of \(q_c^+\). Pairing this SAME source form, with the same optional cutoff equal to one near the support, yields
\[
                                 \lambda_c(0)=b_c^+.
 \tag{8.3}
\]

At infinity let \(h_\infty\) be such a target test of integral one. On the entire collar in (7.3),
\[
 q_\infty^*(h_\infty(u,t_\infty)\omega_{u,t_\infty})
   =(q_c^-)^*\bigl(h_\infty(u,\ell-s_c)\omega_{u,s_c}\bigr).
 \tag{8.4}
\]
This is equality of ordinary forms on an actual ordinary source, not just equality on its skeleton. The substitution \(t_\infty=\ell-s_c\) has derivative -1 in each of the two differential blocks; the paired top form therefore has sign \(+1\), and the absolute Lebesgue Jacobian is one. The support on the right is the SAME compact subset as on the left and is a full subannulus of \(D_c^-\). L makes it compact inside W. Applying O and Section 3 to this one test gives
\[
                              \lambda_c(\infty)=b_c^-.
 \tag{8.5}
\]
The canonical coefficient in each coordinate system is one: \(N_0=1\), residue degree one, and the displayed Jacobian has absolute value one. No omitted-component factor is lost.

For the principal relation (8.2) itself, take the actual lift \(g=(z-c)/\pi=\zeta\) and the retained generic normal functions t_i. In O's notation the residual correction orders of these retained functions are zero on both displayed collars, so \(r=u\). Use the primitive (5.6) with \(t=v(g)\) and cut off the finite bad set \(0,1,\infty\). At zero \(t=s\); at infinity \(t=-s\). At the order-zero bad point 1, the entire shallow collar is an actual ordinary open set on which \(|\zeta|=1\); hence \(\mathrm d''t=0\) there. Away from the bad tubes we use only \(t=0\): since \(\chi\) is constant on a neighborhood of zero, \(\chi'(t)=0\) on an ordinary neighborhood of each such point. No vanishing of \(\mathrm d''t\) near the generic residual center is asserted. Choose the compact support of \(\phi\) first in the common normal boxes, then choose all collar cutoffs using (7.4) and the positive normal margins, and finally make the support of \(\chi\) end before their transitions.

O's support argument now proves that \(\eta\beta\) is one compact ordinary (n-1,n)-form supported inside W. Its support closure avoids the rigid removed point \(\zeta=1\), the zero/pole points, and all torus boundary divisors. Although the full proper residual curve was indispensable for this gluing, T is used only on W. Differentiating this SAME primitive and pairing with T gives
\[
 0=-\lambda_c(0)+\lambda_c(\infty),
 \tag{8.6}
\]
with the sign computation already displayed in (5.7). There is no current slicing, no comparison of unrelated target tests, and no extension of T to the complete \(C_c\)-tube.

Combining (8.2)-(8.5) gives \(b_c^+=b_c^-\) for each c.

## 9. Conclusion and precise failure boundary

Equations (5.5) and (8.2)-(8.5) prove
\[
                 b_0^+=b_0^-=b_1^-=b_1^+=:\kappa\ge0.
 \tag{9.1}
\]
Finiteness follows from one compact positive target test on any domain. Section 3 upgrades this equality at ONE chosen independent normal germ to the whole four specified connected polyannular source families, because their coordinate constants were proved independent of all u and of the residual radius throughout the connected intervals. No comparison between different independent normal germs on a residual curve is silently assumed.

The actual mechanism consists of three proper residual-curve comparisons: the central curve with divisor \([0]-[1]\), and the two interface curves with divisor \([0]-[\infty]\). The center and interfaces need not be top cells, and no coefficient continuity at those lower-dimensional sets is used. The old F projection genuinely drops rank on both connecting strips; H detects them, and their constants are compared by the exhibited model curves and common compact forms. Thus this specific obstruction to fixed-moment propagation is positively crossed under the stated interfaces.

This establishes neither automatic propagation for arbitrary moments nor connectedness of any universal incidence graph. It does not prove R, give an arbitrary source-cell model adaptation theorem, or show \(T=\kappa\delta_W\) on all ordinary top forms. It makes no statement for a general field, a non-split torus, arbitrary complete K, or an arbitrary ordinary W. No P21.3 retirement, live integration, production acceptance, or priority claim is made.

The source ledger separates standard coordinate blowup/Gauss ingredients from the conditional current inputs. The validation file records exact inputs, parameter/sign checks, and control-byte checks. This note is ready for a fresh independent audit of its explicit new assembly.
