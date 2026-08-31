# Residual coefficient comparison for a mixed SNC pair

Date: 31 August 2026. Research author: /root.
Status: conditional research candidate, not a live-book theorem. Fresh independent review and production Rethlas verification remain separate requirements.

## 1. What is being reduced

The all-vertical residual-divisor argument uses finite continuous vertical model radii. It cannot simply be applied to horizontal radii, which can be infinite. The reduction below does not extend that cutoff argument to infinite radii. Instead it constructs a smaller, whole, all-vertical curve tube inside the given mixed curve tube. Its local moment coordinates are exactly the old ones. One compact test in the smaller target then identifies the two already constant pushforward coefficients.

The inputs are explicitly conditional:

- (L): `p213_nonreduced_tube_finite_projection_research_20260831/RESEARCH_NOTE.md`, SHA-256 `3001c94985c0d3e60f184ffd9f0e9591775ea026a98cd20ee538005edac11b7a`. Sections 2-5 supply finite flatness, proper tropical projection, constant positive closed-current coefficients, and canonical calibration for the actual formal-unit equation. Zero retained exponents are allowed.
- (V): `p213_nonreduced_snc_wall_residual_functional_research_20260831/RESEARCH_NOTE.md`, SHA-256 `d9e57c21c276edb40bc7619562b7f0a782cdc7a7eb05a04dd0b0cf0770dc9ea9`. Its full all-selected-vertical theorem, conditional on (L), supplies the residual divisor identity on a whole proper curve tube with arbitrary positive vertical multiplicities.
- (R) is used only in the final optional source-cell interpretation, not in the geometric reduction or the coefficient comparison. Its exact statement/proof pins are recorded in the source ledger.

Root authored (L) and contributed to the outline of (V); neither is independently verified anew here. An independent audit of this reduction must regard them as the stated premises and check every new geometric and support step. Familiar blowup constructions are credited; no priority claim is made.

## 2. Statement and local coefficient

Let K be a complete discretely valued field, R its valuation ring, k its perfect residue field, and pi a uniformizer. Write \(v=-\log|\cdot|\) and \(\ell=v(\pi)>0\). Let \(\mathcal X\) be an integral proper flat regular R-scheme of finite type, of relative dimension \(n\ge2\), with smooth generic fibre. Suppose a reduced divisor B has strict normal crossings and contains the support of the special fibre. Its remaining components are horizontal. Multiplicities in the special fibre are retained and need not be prime to the residue characteristic.

Choose n distinct components \(D_0,\ldots,D_{n-1}\) of B such that \(D_0\) is vertical, and a nonempty connected component C of their scheme-theoretic intersection. Put \(N_i=\operatorname{ord}_{D_i}(\pi)\), so \(N_0>0\), while the other N_i may vanish. Write
\[
 I=\{i:1\le i<n,\ N_i=0\},\qquad h=|I|.
 \tag{2.1}
\]
C is a proper smooth integral k-curve, not necessarily geometrically connected: strict normal crossings gives regularity and codimension n, D_0 places the intersection in the special fibre, and k is perfect. Let T be a positive CLD current of bidegree (0,0), separately \(\mathrm d'\)- and \(\mathrm d''\)-closed, on the WHOLE ordinary open tube \(X_C=\operatorname{red}^{-1}(C)\) in \(X=\mathcal X_K^{\mathrm{an}}\).

At a closed point p of C choose actual regular parameters \(x_0,\ldots,x_{n-1},w\), with x_i an equation of D_i and w a curve parameter. If a further vertical component occurs at p, choose its equation for w and call its multiplicity N_p; otherwise put N_p=0. There is at most one further boundary component at p. Put \(d_p=[\kappa(p):k]\). The completed tube equation is
\[
 \pi=\epsilon(x,w)x_0^{N_0}\prod_{i=1}^{n-1}x_i^{N_i}w^{N_p},
 \qquad |x_i|<1,\quad |w|<1,
 \tag{2.2}
\]
over the unramified DVR extension R_p/R with residue field \(\kappa(p)\), where epsilon is a bounded formal unit with unit constant coefficient. Section 3 checks the small difference from (V)'s presentation when there is only one vertical parameter of multiplicity one.

Remove all selected horizontal zero loci \(x_i=0\) and, when N_p=0, also w=0. Denote this punctured p-tube by P_p. All the other displayed coordinates are automatically nonzero. The actual moment and target are
\[
 q_p=(v(x_1),\ldots,v(x_{n-1}),v(w))=(u,s),
\]
\[
 Q_p=\{u_i>0,\ s>0:\ \sum_{i=1}^{n-1}N_i u_i+N_p s<\ell\}.
 \tag{2.3}
\]
By (L), its projection omitting x_0 is finite flat of degree N_0 over K_p, and its tropicalization q_p is proper. Restricting the actual original K-current gives a finite coefficient \(b_0(p)\ge0\) characterized by
\[
 \langle T,q_p^*(\varphi\Omega)\rangle
   =b_0(p)\int_{Q_p}\varphi(u,s)\,\mathrm d u\,\mathrm d s,
 \qquad \varphi\in C_c^\infty(Q_p),
 \tag{2.4}
\]
where \(\Omega=(\bigwedge_{i=1}^{n-1}\mathrm d'u_i\wedge\mathrm d''u_i)\wedge\mathrm d's\wedge\mathrm d''s\). Pullbacks here are compact test forms, extended by zero to X_C. No extension of an unknown current is being used. Finite means finite at each p.

Conditional on (L) and (V), this note proves
\[
 \sum_{p\in C^{(1)}}\operatorname{ord}_p(f)b_0(p)=0
 \quad(f\in k(C)^\times),\qquad
 b_0(p)=c_0d_p\quad(c_0\ge0).
 \tag{2.5}
\]
The coefficient is independent of the chosen regular parameters with D_0 omitted. Its canonical value is N_0d_p. For another VERTICAL selected component D_j,
\[
 b_j(p)=\frac{N_j}{N_0}b_0(p).
 \tag{2.6}
\]
Omitting a horizontal component is not included: its exponent is zero and the corresponding finite-projection assertion is unavailable.

The new geometric assertion is stronger than a pointwise change of tropical coordinates: exactly h admissible blowups produce a curve \(C^+\simeq C\), all of whose n selected components are vertical, and an inclusion of its ENTIRE tube into X_C under the generic-fibre isomorphism. On each punctured closed-point tube the comparison moment is literally unchanged, with target
\[
 Q_p^+=\{u_i>0,\ s>0:\
       \sum_{i=1}^{n-1}N_i u_i+N_0\sum_{i\in I}u_i+N_p s<\ell\}.
 \tag{2.7}
\]
This open set is nonempty and lies in Q_p. It is generally not all of Q_p.

## 3. The local equation with zero exponents

Let A be the regular local ring at p, of dimension n+1. The full divisor of pi is supported on the vertical components. Dividing pi by the displayed product of component parameters therefore gives a unit in A. The parameters generate the maximal ideal. The quotient by the selected parameters is the complete curve ring \(\kappa(p)[[w]]\) after completion.

As in (V), separability of \(\kappa(p)/k\), the henselian lifting property, and completeness give an injective coefficient map \(R_p\to\widehat A\). Sending variables to the actual parameters gives a surjection from the regular local ring
\[
 R_p[[X_0,\ldots,X_{n-1},W]]
\]
of dimension n+2 to \(\widehat A\). Lift the unit in the divisor identity to a formal unit epsilon. The kernel contains
\[
 F=\pi-\epsilon X_0^{N_0}\prod_{i=1}^{n-1}X_i^{N_i}W^{N_p}.
\]
If the total monomial degree is at least two, F has nonzero linear class pi. If it is one, necessarily N_0=1 and every other exponent is zero; its linear class is then \(\pi-\bar\epsilon X_0\), also nonzero. In either case F is part of a regular parameter system. The quotient by F is a regular local ring of dimension n+1. Its surjection onto the regular domain \(\widehat A\) of the same dimension is an isomorphism. This gives (2.2), without a coefficient field in mixed characteristic or extraction of a root.

The completion-to-tube identification is the same special-formal generic-fibre construction used in (V), not a semistable chart assumption. Thus (L) applies to the actual punctured tube, with m=N_0 and retained exponents \((N_1,\ldots,N_{n-1},N_p)\), including their zero entries. The source is viewed over K; no scalar extension of T is made.

Changing a component equation multiplies it by a local unit, of norm one on the tube. For N_p>0 the same applies to w. When N_p=0 a new curve parameter has
\[
 w'=wV(w)+\sum_{i=0}^{n-1}x_iA_i,
 \tag{3.1}
\]
with V a unit and bounded coefficients. Choose a nonempty normal slice where every \(v(x_i)>\rho>0\), and then \(0<s<\delta<\rho\). Such a slice exists by choosing rho small compared with ell and the positive vertical multiplicities; the horizontal radii may also be chosen finite and greater than rho. The first term in (3.1) strictly dominates, giving \(v(w')=v(w)\). Conversely \(v(w')<\delta\) on that slice forces the same equality. Hence a nonzero compact target test in this collar has the same entire source support and pullback in both coordinates. Equation (2.4) proves parameter independence. This argument does not assign a finite value to a horizontal radius at its zero locus; it takes place in P_p.

## 4. One blowup and its two sections

Keep one selected vertical component V, of multiplicity N_0, distinguished. Let H be a selected horizontal component, and let Z be the connected component of V intersect H containing the current curve C. Since their intersection is regular, its connected components are disjoint integral schemes. Thus Z is a closed regular center of codimension two. It is proper and contained in the special fibre. No third boundary component contains Z: strict normal crossings would force its intersection with V and H to have codimension three. This applies to every other selected component as well as to any extra boundary component through a point of C.

Blow up Z. The morphism is projective and is an isomorphism on the generic fibre. Near Z choose x,y as the equations of V,H. Its two charts have equations
\[
 x=yt\quad\hbox{and}\quad y=xr.
 \tag{4.1}
\]
These are the affine Rees charts, with no extra torsion component: x,y form a regular sequence. For example the first chart is \(A[t]/(x-yt)=A[x/y]\). To check the absence of y-torsion explicitly, if \(yg=(x-yt)a\), reduction modulo y gives \(x\bar a=0\) in \((A/y)[t]\). As x is a nonzerodivisor modulo y, a=ya_1. Cancellation of y then gives \(g=(x-yt)a_1\). Thus this quotient embeds in its localization at y, where t=x/y; its image is precisely A[x/y]. The usual affine blowup description is Stacks, Section 31.33, Lemma 31.33.2.

Both charts are regular. At a point above Z, in the regular polynomial ambient local ring the equation x-yt has nonzero cotangent class \(x-\bar t y\); x,y stay independent normal directions after the residue-field extension. If t vanishes there, the remaining parameters include y,t and every other boundary parameter. If t is a unit, y and every other boundary parameter form part of a regular system and the strict transform of V is absent. The second chart gives the corresponding statement with x,r. Consequently the reduced total transform of B again has strict normal crossings everywhere over Z; away from Z nothing changed. This also proves the claim when the center has positive dimension or the residue extension is nontrivial.

In the first chart the exceptional divisor E is y=0, the strict transform \(\widetilde V\) is t=0, and the strict transform of H is absent. Locally their intersection is x=y=t=0 with coordinate ring A/(x,y). These local descriptions glue to an isomorphism
\[
 E\cap\widetilde V\ \simeq\ Z.
 \tag{4.2}
\]
There is a second, disjoint section \(E\cap\widetilde H\simeq Z\) in the other chart. This is not a choice of a global trivialization of the normal bundle. If x and y are replaced by units times x and y, t changes by their unit ratio; the section t=0 and the isomorphism (4.2) are unchanged. Equivalently these are the two sections of the projective normal bundle determined by its two component line directions.

If D is another boundary component through Z, Z is not contained in D. Its equation z is a third regular parameter wherever it meets Z, so in the displayed chart the strict transform has the same equation z. Restricting to the section (4.2) gives exactly \(D\cap Z\), scheme-theoretically. Intersecting all the other n-2 selected strict transforms with this section therefore gives the same whole regular intersection as before over Z. The component corresponding to C is a complete connected component, denoted C', and maps isomorphically to C. No open subset of C has replaced the proper curve. The full new selected intersection lies over Z because it contains E, so there are no unaccounted components outside this comparison.

We ALWAYS select this strict-V section. The new selected tuple replaces V by \(\widetilde V\), replaces H by E, and takes the strict transforms of the other selected divisors. If locally
\[
 \pi=e x^{N_0}\prod z_i^{N_i}w^{N_p},
\]
then the first chart gives
\[
 \pi=e(yt,\ldots)t^{N_0}y^{N_0}\prod z_i^{N_i}w^{N_p}.
 \tag{4.3}
\]
Thus the distinguished component still has multiplicity N_0, and the replacement for H is vertical of multiplicity N_0. Other selected multiplicities and the extra exponent N_p do not change. The generic fibre is unchanged and smooth; the new integral model is flat over R because it is torsion-free over this DVR.

## 5. Iteration without a prescribed-radius algorithm

Apply Section 4 once to each selected horizontal component, in any fixed order, keeping the strict transform of D_0 distinguished. After a step the new selected tuple has exactly one fewer horizontal component. Its curve is still isomorphic to C and its full reduced boundary is SNC. Hence the next step has the same hypotheses. After h steps all selected components are vertical.

The horizontal component eliminated at a step has strict transform disjoint from the chosen new curve: it meets the opposite exceptional section, not (4.2). Subsequent curves map into that curve, so its later strict transforms remain disjoint from them. No discarded selected horizontal component reappears at a later closed point of C.

Let \(\mathcal X^+\to\mathcal X\) be the composite and let \(C^+\simeq C\) be the final curve. Label the new selected components by their original slots. Their multiplicities are
\[
 N_0^+=N_0,\qquad
 N_i^+=\begin{cases}N_0,&i\in I,\\N_i,&i\notin I.\end{cases}
 \tag{5.1}
\]
Around any p and its unique p^+ on C^+, all INCLUDED coordinates and the curve parameter can be kept exactly:
\[
 x_i^+=x_i\ (1\le i<n),\quad w^+=w,\qquad
 x_0=\left(\prod_{i\in I}x_i\right)x_0^+.
 \tag{5.2}
\]
These are equalities of functions in the common generic function field in the indicated local charts. The completed final equation is obtained by substitution in (2.2), with bounded unit \(\epsilon((\prod_{i\in I}x_i)x_0^+,x_1,\ldots,w)\). It has unit constant coefficient. The residue field at p^+ is still \(\kappa(p)\), and the same coefficient lift R_p can be used through the completed local map.

There is no need to realize an arbitrary prescribed normal weight. Choosing a small nonempty final collar suffices to compare a scalar known to be constant on Q_p. In particular no rational-independence, continued subtraction, field extension or infinite sequence of blowups is used in this proof.

## 6. The whole tube and the exact local source domain

Identify the generic analytic fibres by the actual isomorphism induced by the blowups. Reduction is compatible with these model morphisms. Because the complete curve C^+ maps into C, one obtains
\[
 X_{C^+}\subset X_C.
 \tag{6.1}
\]
These are ordinary open tubes of closed subschemes in proper models. Thus T restricts to a positive closed current T^+ on the WHOLE X_{C^+}. No pullback of an arbitrary current along a modification is required: the generic-fibre morphism here is an isomorphism, and (6.1) is an ordinary-open restriction.

More precisely, puncture the final p^+-tube at w=0 if N_p=0 and call it P_p^+. Every selected final coordinate is automatically nonzero, since every selected multiplicity is positive. Under the generic-fibre identification,
\[
 P_p^+=q_p^{-1}(Q_p^+)\ \subset P_p,
 \qquad q_p^+=q_p|_{P_p^+}.
 \tag{6.2}
\]
Here q_p^{-1} means the ENTIRE inverse image, not its skeleton or a selected analytic sheet.

To prove both directions, use the actual local charts (5.2). A point in the final p^+-tube has all \(|x_i^+|,|w|<1\); its image has all old parameters of norm less than one by (5.2) and therefore reduces to p. The vertical equation forces all selected parameters to be nonzero. The exact norm of the formal unit is one, so
\[
 N_0v(x_0^+)=\ell-\sum_{i=1}^{n-1}N_i u_i
                           -N_0\sum_{i\in I}u_i-N_p s>0.
 \tag{6.3}
\]
This proves one inclusion in (6.2).

Conversely take any point of P_p over Q_p^+. The analytic function \(x_0^+=x_0/\prod_{i\in I}x_i\) is defined and nonzero there. Equation (6.3) gives \(|x_0^+|<1\). At every intermediate step the quotient x_0 by the product of the already processed horizontal coordinates also has norm less than one: its valuation is the final positive valuation plus the positive valuations of the remaining horizontal coordinates. The point therefore lies in each chosen chart and reduces to its strict-V section. At the last step it reduces to the unique p^+, and all final parameters have norm less than one. These inverse maps are analytic on these ordinary domains and come from the blowup charts. They prove (6.2) as an analytic-domain identification, not just a norm correspondence.

Nonemptiness of Q_p^+ follows by choosing all u_i and s sufficiently small and positive; there are finitely many nonnegative coefficients and ell is positive. No uniform choice for all closed p is needed. It is an open subset of \(\mathbf R^n\), so it contains a nonzero nonnegative smooth compactly supported test. Compact subsets of Q_p^+ are also compact subsets of Q_p, and (L) makes their ENTIRE inverse images compact in both tubes.

## 7. Coefficients, divisors and normalization

Apply (L) at p^+ to T^+, obtaining a constant \(b_0^+(p^+)\). Choose \(\varphi\in C_c^\infty(Q_p^+)\) with integral one. Its extension by zero is smooth and compactly supported in Q_p, since its support is compact inside Q_p^+. By (6.2), its old and new pulled-back top forms have the same entire compact source support and are literally equal after extension to X_C. The coordinates, form \(\Omega\), target Lebesgue measure and residue degree are unchanged. Hence
\[
 b_0(p)=\langle T,q_p^*(\varphi\Omega)\rangle
       =\langle T^+,(q_p^+)^*(\varphi\Omega)\rangle
       =b_0^+(p^+).
 \tag{7.1}
\]
There is no Jacobian factor in this particular blowup comparison, and no passage from an aggregate to individual source coefficients. Properness and the exact inverse-image statement are what allow the compact test comparison.

Now every selected component of \(\mathcal X^+\) is vertical with positive multiplicity, the special fibre has strict SNC support, C^+ is a whole proper connected component of their intersection, and T^+ is defined on its whole tube. All the hypotheses of the conditional premise (V) hold over the original K. For \(f\in k(C)^\times=k(C^+)^\times\), the isomorphism of curves identifies every closed point, its residue degree and its order of f. Equations (V) and (7.1) give (2.5), including \(b_0(p)=c_0d_p\).

For the canonical integration current, (L) gives N_0d_p both before and after the blowups. A different selected VERTICAL omitted component D_j is compared on the same original P_p by the exact norm relation in (2.2). The affine change of the retained n target coordinates has determinant of absolute value N_j/N_0. Pullback of the top (n,n) form contributes its square, and Lebesgue change of variables contributes its absolute value. The domains map onto each other, so no support is lost. This proves (2.6). Its determinant is zero if N_j=0, explaining why a horizontal omission is excluded.

Only if one additionally assumes (R) and (L), Sections 6-7, does their single generic Gauss-source argument identify the represented coordinate-moment top-cell coefficient divided by its canonical calibration with c_0/N_0. This extra interpretation uses that K_p/K is unramified and pi remains a uniformizer. Finite degree by itself would not justify it.

## 8. Example: a product model with one horizontal normal

Let \(\mathcal X=\mathbf P^1_R\times_R\mathbf P^1_R\), V its special fibre, and H the closure of the divisor z=0 on the first factor. Then \(C=V\cap H\simeq\mathbf P^1_k\), n=2, N_0=1, and N_1=0. At a closed point of C, x_0=pi, x_1=z and a parameter w of the second factor are regular parameters; there is no extra vertical component. The punctured p-tube has moment target \(Q_p=\{u>0,s>0\}\).

Blow up V intersect H and select the strict-V section. Its chart is \(\pi=z t\). The two selected components t=0 and z=0 are now both vertical, and their intersection is again the whole \(\mathbf P^1_k\). The final punctured tube has target
\[
 Q_p^+=\{0<u<\ell,\ s>0\}.
\]
The moment (v(z),v(w)) did not change. A test supported in this strip computes the same coefficient as before; the all-vertical divisor identity therefore controls the original coefficient on the entire quadrant, because that coefficient was already constant. This does not assert that the final tube contains the points u greater than or equal to ell, or that it covers the horizontal zero locus z=0.

## 9. Remaining scope and what this does not solve

This reduction removes the selected-horizontal restriction from the residual coefficient functional on a WHOLE modelled proper curve tube, conditional on (L) and (V). It avoids introducing upper cutoffs for infinite horizontal model radii. The proof is over the original discretely valued field and does not assume reduced special fibre, residue characteristic zero, tame multiplicities or geometric connectedness of C.

It does not prove any of the following:

- that a prescribed ordinary open W contains X_C or the smaller complete X_{C^+};
- that an arbitrary full-dimensional cell or wall of an analytic moment is captured by such a proper model and its controlled coordinate moments;
- that adjoining moment coordinates controls cells contracted by one projection;
- that the ratios for every unrelated controlled model tube agree;
- that equality of these coefficients identifies T on every ordinary test form;
- the higher-bidegree part, or the full statement, of P21.3.

In particular the smaller target in (2.7) need not meet a given prescribed source patch. Equality (7.1) transfers one scalar for an already proper local moment; it is not an all-cell capture theorem. These unresolved interfaces cannot be removed from the inventory on the strength of this note.
