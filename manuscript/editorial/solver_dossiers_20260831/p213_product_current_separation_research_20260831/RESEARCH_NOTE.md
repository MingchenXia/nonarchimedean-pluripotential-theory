# Product current separation: one additional closedness comparison

Date: 31 August 2026. Author: `/root/p082_independent_reaudit`.

## Status and exact outcome

This is a new, isolated research note, not an independent audit of its own arguments, not a production-accepted theorem, and not a solution of P21.3. The author previously independently audited the frozen product residual-functional packet. The parent suggested testing the extension of the initial complex-Laurent-series example to a complete DVR with perfect residue field and an invertible integer N. That extension is proved below. The parent also contributed to the broader research framework, so its preliminary review is not a fresh independent audit.

There are three distinct conclusions.

1. For every known residual-point collar and every integer N >= 2 invertible in the valuation ring, closedness transports its coefficient to a new source family: **B_T(p,N) = N b_T(p)**. The canonical coefficient there is **N [kappa(p):k]**. This calculation does not use the unaudited source-calibration representation.
2. Even the old collars together with all these additional families do not locally generate all smooth top-degree test forms. An explicit mixed-coordinate polyannulus detects the remaining gap. This is not a counterexample in the class of positive closed currents.
3. Conditional on the separate source-calibration representation, equality of the calibration ratio on every ordinary moment's source top cell does imply equality of analytic currents. What is still missing is a source-cell accessibility/closedness argument reaching all those cells. Equality on one moment, target overlap, or a supposed polycylinder basis does not replace that argument.

No frozen source packet, live manuscript, inventory, or production state was changed.

## 1. Setting and previously established collar data

Let K be a complete discretely valued non-Archimedean field, R its valuation ring, pi a uniformizer, and k its perfect residue field. Put v = -log|.| and ell = v(pi) > 0. Let Ccal/R be a smooth proper curve with geometrically connected fibres, with generic fibre C and special fibre C_0. Set

\[
 A=\{|\pi|<|z|<1\},\qquad X=A\times_K C^{\mathrm{an}}.
\]

All products below are analytic fibre products, not assertions that their point sets are Cartesian products. Let T be a positive ordinary CLD current of bidegree (0,0), with d'T = d''T = 0. In fact d'T = 0 is enough for the new comparison.

Fix a closed point p of C_0. Write d_p = [kappa(p):k]. The frozen product packet identifies the completed local ring with R_p[[w]], where R_p/R is finite unramified of degree d_p and K_p is its fraction field. Its tube is one open unit disc over K_p, viewed over K. A sufficiently small outer collar is the actual ordinary open domain

\[
 V_p=A_{K_p}\times_{K_p}\{e^{-\delta}<|w|<1\},
 \qquad u=v(z),\quad s=v(w).
\]

The primary henselian input is Stacks, Lemma 10.153.7 (04GK). Perfection makes kappa(p)/k separable; the finite etale lift gives R_p. The completed-ring identification and disc realization were proved explicitly in the frozen packet, not inferred from a statement assuming algebraically closed residue field.

For ordered real coordinates x,y use the positive orientation

\[
 \Omega_{xy}=\mathrm d'x\wedge\mathrm d''x\wedge
              \mathrm d'y\wedge\mathrm d''y.
\]

The previously constructed finite coefficient b = b_T(p) satisfies

\[
 \langle T,h(u,s)\Omega_{us}\rangle
   =b\int h(u,s)\,\mathrm du\,\mathrm ds,
 \qquad h\in C_c^\infty((0,\ell)\times(0,\delta)).                 \tag{1}
\]

Forms here and below are extended by zero from an ordinary open domain only after verifying that their analytic support is compactly contained in that domain. The frozen residual-functional proof further gives b_T(p) = c d_p for a single c >= 0. The new transport calculation needs only (1); it does not reprove or silently strengthen that earlier result.

## 2. An additional ramified source family

Fix an integer N >= 2 whose image in R is a unit, and put

\[
 t=z^N/\pi-1,\qquad u_0=\ell/N.
\]

Inside V_p consider the ordinary open domain

\[
 D_{p,N}=\{0<|t|<1\}\cap V_p.
\]

Let L_p = K_p[a]/(a^N-pi). The polynomial is Eisenstein, so L_p is a field, [L_p:K_p] = N, its residue field is kappa(p), and [L_p:K] = N d_p. No roots of unity need be present in K_p.

There is a power series P(T) in R[[T]], with P(0)=1 and P(T)^N=1+T. To see this without a characteristic-zero binomial expansion, solve its coefficients recursively. Once the coefficients below degree j have been found, the coefficient in degree j is N times the unknown coefficient plus an R-linear expression in the earlier coefficients. Division by N is allowed in R, so all coefficients stay in R. This determines P uniquely. On every closed disc of radius less than one the series converges uniformly; on the open unit disc |P|=1.

Consequently a = z/P(t) is an analytic function on D_{p,N} satisfying a^N=pi. There is an isomorphism of K-analytic domains

\[
 D_{p,N}\simeq
 \{0<|t|<1\}_{L_p}\times_{L_p}
 \{e^{-\delta}<|w|<1\}_{L_p}.                                  \tag{2}
\]

The maps are explicitly z=aP(t) in one direction and t=z^N/pi-1 in the other, with w unchanged. They are inverse on each strictly smaller closed annulus in t and w, and hence on their union. The recovered root a supplies the coefficient-field homomorphism, so the description includes every conjugate geometrically; it is **one L_p-domain viewed over K**, not N ordinary-open sheets. We do not pull T through a finite field extension. We only restrict it to the actual source domain D_{p,N}.

Put r=v(t). The moment (r,s) maps D_{p,N} to

\[
 Q^+ = (0,\infty)\times(0,\delta).
\]

The inverse image of a compact target set is compact: it is closed in a closed polyannulus over L_p. Thus the pullback of a compactly supported target test form has compact analytic support. Positivity and closedness give a unique finite number B = B_T(p,N) >= 0 such that

\[
 \langle T,h(r,s)\Omega_{rs}\rangle
     = B\int h(r,s)\,\mathrm dr\,\mathrm ds
 \qquad(h\in C_c^\infty(Q^+)).                                  \tag{3}
\]

For completeness, the scalar functional on the left is a positive distribution. On each fixed compact target support its absolute value is bounded by the sup norm times its value on a nonnegative cutoff equal to one on that support, so it is a locally finite positive measure. Pulling back the primitives obtained by deleting d'r or d's from Omega_rs shows that both distributional partial derivatives vanish. On a ball compactly contained in Q^+, convolution with Euclidean mollifiers is constant. Testing against one function of integral one gives the finite limit of those constants. Overlapping balls, and connectedness of Q^+, give one finite B. The mollification is only on the Euclidean target. This argument uses neither source-current slicing nor a representation theorem.

## 3. Complete cutoff proof of B_T(p,N) = N b_T(p)

On Y = V_p minus the zero locus of t, the functions u,r,s are smooth logarithms of analytic units. Their norms satisfy the following identities on whole ordinary open regions:

\[
 \begin{array}{c|c}
 u<u_0 & r=Nu-\ell<0,\\
 u>u_0 & r=0,\\
 r>0   & u=u_0.
 \end{array}                                                   \tag{4}
\]

These follow from strict ultrametric domination. In particular, d''r=0 on the second region and du=0 on the third. We make no assertion that r or u is locally constant at the central set u=u_0,r=0.

Choose a>0 with [u_0-2a,u_0+2a] contained in (0,ell), and choose eta in C_c^infinity(0,ell) equal to one on [u_0-a,u_0+a]. Choose 0<epsilon<Na and chi in C_c^infinity(R), supported in (-epsilon,epsilon), equal to one on a neighbourhood of zero. Finally take xi in C_c^infinity(0,delta) with integral one. On Y define the (1,2)-form

\[
 \beta=\eta(u)\chi(r)\xi(s)\,
       \mathrm d''r\wedge\mathrm d's\wedge\mathrm d''s.          \tag{5}
\]

Its support is compactly contained in Y. Indeed, u and s range in compact subintervals of their defining open intervals; these bounds give a compact closed polyannulus over K_p. Bounded r additionally bounds |t| away from zero. The support is a closed subset of that compact domain, disjoint from all excluded boundaries and t=0. Thus beta extends by zero to a legitimate smooth compactly supported form on X. This verifies the proper-support requirement directly.

Since d'd'' of a logarithm of an analytic unit is zero, differentiation gives

\[
 \mathrm d'\beta=\xi(s)\left[
  \eta'(u)\chi(r)\,\mathrm d'u\wedge\mathrm d''r
  +\eta(u)\chi'(r)\,\mathrm d'r\wedge\mathrm d''r
 \right]\wedge\mathrm d's\wedge\mathrm d''s.                    \tag{6}
\]

The derivative of xi duplicates d's and vanishes. On the old left region the first term vanishes wherever eta' is supported, since there r <= -Na and chi=0. On the right it vanishes because d''r=0; on the new branch eta'=0. More importantly, **the entire form d'beta is zero on a genuine ordinary neighbourhood of the central set u=u_0,r=0**: both eta' and chi' vanish there by continuity of (u,r). This is a statement about the actual form, not a negligibility assertion for an unknown current.

It follows that the support of d'beta decomposes into two compact pieces away from the central set: a piece with u<u_0 and a piece in D_{p,N}. The region u>u_0 contributes zero. This decomposition is made before pairing with T and does not require a current slice, ordinary covering sheets, or a lower-face noncharging theorem.

On the left, substitution of r=Nu-ell into (6) and use of (1) gives

\[
 \begin{aligned}
 I_-&=b\int_0^\ell
       \left[N\eta'(u)\chi(Nu-\ell)
             +N^2\eta(u)\chi'(Nu-\ell)\right]
       \mathbf 1_{u<u_0}\,\mathrm du\\
    &=Nb\,[\eta(u)\chi(Nu-\ell)]_{u=0}^{u=u_0}=Nb.
 \end{aligned}                                                 \tag{7}
\]

The integrand vanishes near u=u_0, so its restriction and extension used in (7) are smooth target tests. The lower endpoint contributes zero because eta vanishes near zero; the upper endpoint is one. The integral of xi has already been taken.

On D_{p,N}, u=u_0, eta=1, and (3) gives

\[
 I_+=B\int_0^\infty\chi'(r)\,\mathrm dr=-B.                    \tag{8}
\]

Here chi' is compactly supported away from r=0, exactly as required by (3). Closedness now says 0 = <T,d'beta> = I_-+I_+, proving

\[
                      B_T(p,N)=N b_T(p).                       \tag{9}
\]

The sign and multiplicity in (9) have separate origins: differentiating r=Nu-ell produces N^2 in the old top form, changing the integration variable removes one N, and the positive branch has integral chi(infinity)-chi(0) = -1. No normalization ell=1 was imposed, and no additional ell factor appears.

## 4. Canonical normalization and precise interpretation

The coordinates t,w in (2) are primitive torus coordinates over L_p. The canonical integration coefficient of their Gauss plane over L_p is one. CLD Remark 14.4.3 says that viewing this space over K multiplies its canonical calibration by the full field degree [L_p:K]. It applies to finite ramified extensions as well as unramified ones. Therefore

\[
 B_{\delta_X}(p,N)=N d_p,\qquad
 \frac{B_T(p,N)}{N d_p}=\frac{b_T(p)}{d_p}=c.                    \tag{10}
\]

The last equality uses the previous residual-functional result. The factor N is not counted again as an ordinary sheet count or an independent lattice correction. Formula (10) concerns the scalar coefficients in (1) and (3) without any additional premise.

If the separate source-calibration representation is assumed, then the injective source Gauss plane of the moment (r,s) has this same ratio c to the canonical calibration. This last source-cell interpretation is conditional. It does **not** yet imply equality of T and c delta_X on every test form supported in D_{p,N}, since another moment can have source cells missed by (r,s).

## 5. Two exact non-separation diagnostics

### 5.1 The old collars do not separate arbitrary currents

On D_{p,N}, u is constant. Thus every old collar top form Omega_us vanishes there as an actual smooth form, even after multiplication by an arbitrary smooth source function. The other residual-point collars are disjoint.

Choose a nonnegative, nonzero smooth function h(r,s), supported in a compact rectangle of Q^+, with partial_r h not identically zero. The positive current S = h(r,s) delta_X, extended by zero from D_{p,N}, is nonzero, and every old collar test pairs to zero with S. Consequently c delta_X and c delta_X+S give the same old collar data for every c >= 0.

This is expressly **not** a counterexample for positive closed currents. Indeed the compactly supported form

\[
 \gamma=(\partial_r h)(r,s)\,
              \mathrm d''r\wedge\mathrm d's\wedge\mathrm d''s
\]

satisfies

\[
 \langle S,\mathrm d'\gamma\rangle
   =N d_p\int h\,\partial_r^2h\,\mathrm dr\,\mathrm ds
   =-N d_p\int(\partial_rh)^2\,\mathrm dr\,\mathrm ds<0.         \tag{11}
\]

So S is not d'-closed. It proves only that a test-separation inference from the old coefficient list alone is invalid. The new comparison (9) supplies a genuine extra use of closedness which rules out precisely this unrestricted bump construction in that family.

### 5.2 Even all transported integer families miss mixed source forms

Fix p,N as above and work in the actual L_p-domain (2). Put q=w-t and choose

\[
 0<a<b<\min(\delta,\ell),\qquad b<c_1<d_1.
\]

The ordinary domain

\[
 E=\{a<v(t)<b,\quad c_1<v(q)<d_1\}
\]

is a product polyannulus over L_p in the coordinates t,q. Its inverse parameterization is w=t+q. Since |q|<|t|<1, it lies in D_{p,N} and satisfies

\[
 u=\ell/N,\qquad s=v(w)=v(t)=r.                                \tag{12}
\]

Thus the old moment (u,s) and the new moment (r,s) both have rank at most one on this entire ordinary domain, and their pulled-back top forms vanish.

For any other integer M >= 2, with M invertible in R and M != N, one has

\[
 v(z^M/\pi)=(M/N-1)\ell\ne0.
\]

Strict domination shows that v(z^M/pi-1) is constant on E: it is (M/N-1)ell when M<N and zero when M>N. Hence these moments, wherever their forms are defined, also give zero top forms on E. Their positive-branch domains are in fact disjoint from E when M != N. Other residual-point tubes remain disjoint. Changing the formal parameter at p does not fix the problem on this chosen collar: w'=a_0+a_1w+... with a_0 in pi R_p and a_1 a unit has |w'|=|w| whenever 0<s<ell, which is ensured here.

On the other hand, writing h_1=v(q), any nonnegative nonzero rho in C_c^infinity((a,b) x (c_1,d_1)) gives a genuine compactly supported top form

\[
 \alpha=\rho(r,h_1)\,
  \mathrm d'r\wedge\mathrm d''r\wedge
  \mathrm d'h_1\wedge\mathrm d''h_1,
 \qquad
 \int_X\alpha=N d_p\int\rho\,\mathrm dr\,\mathrm dh_1>0.        \tag{13}
\]

Therefore this form is not locally generated by the known collar top forms, even allowing arbitrary smooth source multipliers and all invertible integers M. A positive bump current on E also separates (13) from their linear span as continuous current tests. This is a precise obstruction to a spanning or density shortcut. It does not preclude a further closedness comparison involving q, nor does it disprove product rigidity.

## 6. Exact conditional current-separation reduction

Call (R) the source-calibration representation in the separate frozen `skeletal_representation` packet. Its proof has been read here to identify the interface, but it has **not** been independently validated in this task. Assume (R) for T on all ordinary moment domains under consideration.

For an ordinary moment F on an ordinary open V, (R) gives a locally finite decomposition of its maximal-variation source skeleton into top cells C, affine and injective under F. In fixed coordinates on each cell let b_{F,C} be T's coefficient and a_{F,C}>0 the canonical coefficient. Both pairings allow arbitrary smooth compactly supported source multipliers, and there is no residual coefficient measure on lower-dimensional cells.

Under (R), the following is an exact sufficient and necessary condition:

\[
 T=c\delta_X\quad\Longleftrightarrow\quad
 b_{F,C}=c\,a_{F,C}
 \ \text{for every such ordinary moment and source top cell}.    \tag{14}
\]

For sufficiency, take any compactly supported smooth (2,2)-form omega on X. CLD Proposition 15.1.1(b), as opposed to part (a), gives an **ordinary open** covering on which omega is a moment pullback. Shrink around its compact support as needed so the target superforms are represented by ambient smooth forms. Goodness and separation imply local holomorphic separation. CLD Corollary 15.2.9 (or Proposition 15.2.8 with paracompactness) then gives smooth compactly supported source cutoffs subordinate to the covering, with their sum one near supp(omega). Only finitely many relevant terms meet that compact support. Thus omega is a finite sum of forms rho_i F_i^*alpha_i to which (R) applies. Substituting every equality b_{F_i,C}=c a_{F_i,C} in the cell formula proves <T,omega>=c integral omega. The lower-cell clause of (R) is essential here. Necessity follows from uniqueness in the same representation; equivalently, localize a nonzero positive target top form to an interior patch of one source cell using a source cutoff and compare the two formulas.

A useful sufficient *accessibility hypothesis*, not proved in this note, is the following. For every F-cell C, there is a nonempty relatively open interior patch P and an ordinary source neighbourhood on which P is also an interior patch of a cell for a certified moment G, after a common refinement. Require explicitly that P lies in both source skeleta, both maps are affine and injective on P, both are of full rank there, and the locally finite cell structures permit isolation of a smaller patch by ordinary source cutoffs. The G-ratio on that patch must already be known to be c. These are actual source conditions; target images meeting is insufficient.

Under these stated conditions the ratio on C is c. Indeed, choose a nonzero positive test localized to the smaller common patch. The two source-cell formulas for this same current give the same local coefficient measure. The affine change of coordinates multiplies T's coefficient and the canonical coefficient by the same positive Jacobian normalization. Their ratio therefore agrees on the patch. Since that ratio is constant on the F-cell by (R), it agrees on C. A finite chain of such overlaps, or of independently proved closedness relations such as (9), gives the same conclusion.

The point of (14) is to identify the missing argument, not to assume accessibility. The domains in Section 5 show why the currently certified family cannot meet this requirement for every moment just by being named as a cover. No claim that polycylinders form an ordinary-open basis, no arbitrary analytic current slice, and no universal common dominating Radon measure has been used.

## 7. Remaining boundary and reproducibility

The branch comparison is proved for every complete DVR with perfect residue field in the stated product geometry, every known closed-point collar, and every integer N >= 2 invertible in R. It requires neither algebraic closure of K or k nor characteristic zero. It does not address N divisible by the residue characteristic; there the bounded integral Nth-root series used in (2) is unavailable in this form.

No proof is supplied that every arbitrary ordinary moment cell is accessible from these collars. No full assertion T=c delta_X is made. The conditional reduction and the rank-collapse examples identify that remaining support/separation problem without claiming that it is impossible. Nontrivial normal bundles, general semistable neighbourhoods, and the global P21.3 question remain outside this note.

This is a Markdown research packet. No TeX compilation or new PDF generation is claimed. Exact frozen input hashes and source locators are in `SOURCE_LEDGER.md`; a separate SHA256SUMS fixes the authored note and ledger together with those inputs.
