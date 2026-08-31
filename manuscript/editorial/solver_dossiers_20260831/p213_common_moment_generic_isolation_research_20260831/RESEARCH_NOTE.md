# Generic source isolation and noncontracted common-moment coefficients

Date: 31 August 2026. Author: `/root/p082_independent_reaudit`.

## Status and precise outcome

This is a new research candidate for independent review. It is not an independent audit of its own proof, not production-accepted, and not a solution of P21.3. The parent proposed investigating whether the strong isolation premise in the earlier common-moment supplement is automatic on noncontracted cells. The present author wrote that supplement and the earlier tame-branch/non-separation note; this provenance is explicit. All earlier files and audits remain unchanged.

The outcome is positive in a precise general-dimension scope. For an actual concatenated moment H=(F,G), a source H-top cell on which both projections have rank n lies in both projected source skeleta. After removing a finite closed PL subset of dimension less than n coming from the chosen cell boundaries, an ordinary open neighbourhood isolates exactly the same source patch for all three moments. Thus the previous strong shared-source premise can be derived generically on these cells. Conditional on the stated representation premise (R), normalized coefficients agree there.

For adjoining analytic units to one moment F, the corresponding one-projection assertion transfers normalized coefficients on every noncontracted H-top cell. Conversely, on a rank-drop H-top cell its interior is absent from the old source skeleton S_F. Such a cell is a full-dimensional missing source family, not part of the lower-dimensional exceptional set. Nothing here supplies its current coefficient from the old one, proves arbitrary accessibility, or identifies an entire current from one chart.

This is explicit proof support, not a priority claim. Source monotonicity and noncontraction already occur in CLD Example 5.5.7, and Proposition 7.5.7 compares descriptions of a skeletal current by passing through the concatenated moment. The contribution of this note to the present research packet is the explicit ordinary-open isolation argument and determinant bookkeeping under the displayed premise (R). Proposition 7.5.7 is recorded as related literature, not applied: its literal ambient hypothesis is local affine separation, whereas the analytic separation statement in Section 15.2.4 concerns local differential separation. No implication between those two hypotheses is supplied or needed here.

## 1. Exact setup and the conditional representation input

Let K be a complete nontrivially valued non-Archimedean field and let V be a good, separated, paracompact, boundaryless K-analytic space, pure of dimension n>=1. Let

\[
 f:V\longrightarrow\mathbf G_{m,K}^{r},\qquad
 g:V\longrightarrow\mathbf G_{m,K}^{s}
\]

be actual analytic moments, with tropical maps F and G. Form the analytic moment h=(f,g) on this same ordinary open space V and its tropical map

\[
 H=(F,G):V\longrightarrow E_F\times E_G,
 \qquad F=p_F H,\quad G=p_G H.                                  \tag{1}
\]

The maps p_F,p_G are the ambient affine projections. These equalities hold as ordinary maps on all of V, not only on a source skeleton or a target polyhedron.

For J in {F,G,H}, write S_J=Sigma_J^(n) for the maximal-variation source skeleton: the points where J has tropical dimension n. These are the source sets of CLD Definition 5.2.1. They are closed in V, are pure n-dimensional PL spaces, and J restricted to S_J is an immersion by pieces (Proposition 5.2.5). They are not substituted by their target images. The analytic realization of this setup is CLD Section 12.9, especially Lemma 12.9.2 and Section 12.9.5; Section 12.8 distinguishes this maximal-variation set from characteristic-skeleton notation on domains with boundary.

Choose locally finite decompositions D_J of S_J into compact J-cells, with J affine and injective on every cell. For the coefficient assertions assume that these decompositions have also been chosen or refined so that the following formulas have constant coefficients on their top cells.

Let T be a positive ordinary CLD current of bidegree (0,0), with d'T=d''T=0. **Assume (R)**: for every J under consideration, every smooth compactly supported ordinary source function rho, and every smooth ambient (n,n)-form alpha, one has the source-cell formula

\[
 \langle T,\rho J^*\alpha\rangle
 =\sum_{D\in\mathcal D_J,\,\dim D=n}
  b_{J,D}\int_{J(D)}\rho((J|_D)^{-1}(y))\,\alpha_D(y)\,dy,
 \qquad b_{J,D}\ge0,                                           \tag{2}
\]

where alpha restricted to the affine span of J(D) is alpha_D times the ordered top form in the chosen affine coordinates. There is no residual coefficient measure on the lower-dimensional cells. Use the analogous canonical integration formula with constants a_{J,D}>0, and set kappa_{J,D}=b_{J,D}/a_{J,D}. The same coordinates must be used in the two formulas. The canonical coefficients come from the CLD calibration; the assertion (2) for an arbitrary T is the separate, explicitly assumed source-representation packet. It is not reproved or independently certified here.

The geometric conclusions in Sections 2-4 below do not assume (R). The coefficient comparison in Section 5 does.

## 2. The source containments and the rank dichotomy

One always has

\[
                         S_F\cup S_G\subset S_H.              \tag{3}
\]

Indeed, on every compact analytic neighbourhood W of a point, dim(F(W))<=dim(H(W)) because F=p_F H; the same holds for G. Taking the local tropical dimensions, as defined in CLD Section 3.1.3, gives the inequality. Since every such dimension is at most n, (3) follows. This elementary source inclusion is also stated explicitly in the first part of CLD Example 5.5.7. No properness or pleasantness hypothesis from the later target-pushforward portion of that example is needed for (3).

Fix a compact n-cell C in D_H and put L_C=aff(H(C)). Let J be F or G. Because H|C is affine and injective, dim(L_C)=n. Then:

\[
 \begin{array}{ll}
 \operatorname{rank}(p_J|_{L_C})=n
       &\Longrightarrow\quad C\subset S_J,\\
 \operatorname{rank}(p_J|_{L_C})<n
       &\Longrightarrow\quad C^{\circ}\cap S_J=\varnothing.
 \end{array}                                                   \tag{4}
\]

Here the rank is that of the linear part on the direction space of L_C, and C-circle is relative interior. Rank is constant on this chosen affine cell.

For the first assertion, J|C is an affine homeomorphism onto an n-cell. At a point x of C-circle, every source neighbourhood meets C in a relatively open n-dimensional patch, whose J-image has dimension n. In particular every compact analytic neighbourhood of x has J-image of dimension at least n. Thus x lies in S_J by Definition 5.2.1; closedness of S_J and density of C-circle in C give C subset S_J. This is also precisely the source reasoning behind CLD Remark 5.4.2. It never identifies two distinct source points merely because they have the same tropical image.

There is a useful independent strong-support check on this argument. Choose affine coordinates on the n-plane p_J(L_C), extend them to E_J, and pull back their constant positive top form. Its restriction to C is a nowhere zero n-dimensional top form on C-circle because the projection has full rank. CLD Lemma 5.3.4 strongly supports this J-pullback on S_J. If a point of C-circle lay outside S_J, the pullback would vanish on an ordinary neighbourhood of that point and hence on the corresponding C-patch, a contradiction. Sections 5.3.1 and 5.3.6 justify reading strong support as actual support and not only a target-integral statement.

For the second assertion, C-circle is open in S_H: in a pure n-dimensional locally finite cell decomposition, CLD Lemma 2.2.8 identifies the open star of a top cell with its relative interior. Choose an ordinary open W in V whose trace on S_H is contained in C-circle. Such a W exists because S_H is a closed subspace of V. If x in W belonged to S_J, the nonempty open PL space W intersect S_J would be pure of dimension n, by Proposition 5.2.5. The immersion-by-pieces property would give a compact n-dimensional J-cell in W intersect S_J with n-dimensional J-image. But (3) puts that cell in C, whose J-image has dimension rank(p_J|L_C)<n. This contradiction proves the second assertion of (4).

In particular, failure of source overlap in the interior of an H-top cell is not an additional mystery once its projection rank is known: full rank gives overlap, and rank drop excludes it. Boundary points can be incident to different H-cells and are not covered by that interior dichotomy.

## 3. A precise finite exceptional set

First suppose the projection to a single J has rank n on C. Let B_J be the union of the cells of D_J of dimension less than n. Define

\[
                  Z_{C,J}=\partial C\ \cup\ (C\cap B_J).       \tag{5}
\]

This is a compact closed PL subset of C of dimension at most n-1. To check all parts of that assertion, (4) puts the compact set C inside S_J. Local finiteness of D_J means that only finitely many of its cells meet C. By the canonical source PL compatibility of CLD Lemma 3.2.8, their intersections with C are PL subsets with the induced canonical structures. Intersecting with a cell of dimension less than n cannot increase that dimension. The relevant cells and C are compact and closed in the Hausdorff source, so their intersections are compact and closed. Finally the boundary of an n-cell has dimension n-1 (Section 2.2.2). Taking this finite union proves the assertion. Consequently C minus Z_{C,J} is a nonempty relatively open dense subset of C.

If both projections have rank n, use

\[
        Z_C=\partial C\ \cup\ (C\cap B_F)\ \cup\ (C\cap B_G). \tag{6}
\]

Exactly the same proof gives dim(Z_C)<=n-1 and a relatively open dense complement. The set Z_C is an exception for the **chosen cell presentations**, not a set of full-dimensional rank-drop H-cells. It is constructed from source intersections, not intersections of tropical images. There is no claim that an arbitrary current gives zero mass to every analytic set suggested by such an image.

## 4. Deriving ordinary shared-source isolation and common refinement

Take x in C minus Z_C. By CLD Remarks 2.2.5-2.2.6, x lies in the relative interior of unique n-cells C_F in D_F and C_G in D_G. The top-cell interiors C-circle, C_F-circle and C_G-circle are open in their respective source skeleta. Since each source skeleton is closed in V, the set

\[
 U=V\setminus\bigl((S_H\setminus C^{\circ})
       \cup(S_F\setminus C_F^{\circ})
       \cup(S_G\setminus C_G^{\circ})\bigr)                    \tag{7}
\]

is an ordinary open neighbourhood of x. One may shrink it further around x. By (3), by C subset S_F intersect S_G, and by its definition, its trace is exactly

\[
 \begin{aligned}
 P:=U\cap S_H
    &=U\cap S_F=U\cap S_G\\
    &=U\cap C^{\circ}
      =U\cap C_F^{\circ}=U\cap C_G^{\circ}.                    \tag{8}
 \end{aligned}
\]

This is the earlier strong source-isolation condition S1, now derived at every x outside the explicit lower-dimensional set (6). The proof uses an ordinary open subset of the actual analytic source. It does not assert that C-circle itself is open in V; it is open only in S_H. It also does not rely on a polycylinder basis or ordinary covering sheets. For the one-projection version, omit G from (7)-(8) and use Z_{C,J}.

If finite common-refinement language is preferred, it is available on the fixed compact C. The finitely many sets C intersect D, where D ranges over cells of D_F and D_G meeting C, are compact PL subspaces of C. Apply CLD Corollary 2.2.14 to these sets, to the boundary of C, and to their affine coordinate maps, also including the coordinate map H|C. This gives a finite compact PL cell decomposition of C adapted to all these source sets and maps. Its n-cell interiors lie in C-circle and in the interiors of the appropriate n-cells C_F,C_G; the lower-dimensional locus contains (6). On each such top piece, (8) is available locally at every interior point. This is a common refinement of source cell presentations on C, not a claim about an arbitrary overlap of target polyhedra.

An ordinary restriction U does not create a different maximal-variation source set: Proposition 5.2.5(b) gives S_{J|U}=(S_J intersect U)^(n), and the latter is S_J intersect U because it is open in a pure n-dimensional PL space. Thus (8) also has the intended interpretation if moments are restricted to U.

## 5. Coefficients in every dimension, evaluated through H

Now assume (R). Fix x outside Z_C and choose U,P as in (8). Write b_H,a_H for the coefficients on C, and b_J,a_J for those on C_J, J=F,G. Choose affine coordinates x_1,...,x_n on L_C and y_{J,1},...,y_{J,n} on the span of J(C_J). The common patch P is relatively open in all three source cells. Therefore the span of J(C_J) equals p_J(L_C), and

\[
             y_J\circ p_J=A_Jx+c_J,
             \qquad j_J=|\det A_J|>0.                          \tag{9}
\]

Choose rho>=0 smooth with compact support in U, equal to one near x. This is an ordinary source cutoff, supplied by CLD Corollary 15.2.5; one can square its supplied cutoff for nonnegativity. Let I be the integral of rho on P in the x-coordinates of H. Its support is contained in the image of the compact set supp(rho) intersect C, and it is positive on a relatively open patch, so 0<I<infinity.

Extend y_J to affine functions on E_J and set

\[
                \alpha_J=\bigwedge_{i=1}^{n}
                         (d'y_{J,i}\wedge d''y_{J,i}).
\]

The same ordinary test has two legitimate descriptions on all of V,

\[
                 \rho J^*\alpha_J
                     =\rho H^*(p_J^*\alpha_J).                 \tag{10}
\]

Using J's formula (2) and then H's formula (2), with the isolation (8), gives respectively

\[
 \langle T,\rho J^*\alpha_J\rangle=b_Jj_JI,
 \qquad
 \langle T,\rho H^*p_J^*\alpha_J\rangle=b_Hj_J^2I.              \tag{11}
\]

The first factor is the absolute determinant in the change of Lebesgue coordinates. The second is the square determinant in the pullback of the ordered (n,n)-form: each of the two differential blocks contributes det(A_J), so the square has positive sign in every dimension. No orientation or integer-lattice normalization is suppressed. Since the two expressions in (11) evaluate the same test, b_J=j_J b_H. The identical argument for the canonical current gives a_J=j_J a_H. Hence

\[
                    \kappa_{F,C_F}=\kappa_{H,C}
                                    =\kappa_{G,C_G}.            \tag{12}
\]

Zero b-coefficients present no exception, since only a_H,a_J,j_J and I are divided by, and these are positive. The constants on the original cells are used; refining their presentation restricts those constants with the ordinary coordinate normalization.

The comparison (10)-(12) is through the actual analytic concatenation H. It never identifies an F-pullback with a G-pullback merely from agreement on P. It uses (R)'s arbitrary source multipliers and its lower-cell clause exactly where specified; (R) itself remains an assumption. The lower-dimensional presentation set Z_C carries no additional term in these fixed source-cell formulas, but this is not a universal noncharging statement for all unrelated moments.

## 6. Precise consequence for adjoining analytic units

Let f be one fixed ordinary analytic moment on V. Adjoin any finite list of analytic units g_1,...,g_s on this same V, and put h=(f,g_1,...,g_s). Assume (R) for F and H and take an H-top cell C in compatible coefficient-constant cell presentations.

If the projection from aff(H(C)) to E_F has rank n, the one-projection forms of (5), (7)-(8), and (10)-(11) apply. On every full-dimensional common-refinement piece of C, its normalized H-coefficient equals the normalized coefficient of the old F-cell meeting that piece. In particular, if all those old F-cells have ratio c, then kappa_{H,C}=c. No separately assumed shared-source isolation is necessary on this noncontracted locus.

If that projection has rank less than n, (4) gives C-circle disjoint from S_F. Every F-pullback of an (n,n)-form restricts to zero on C, since its affine differential rank is less than n. There is no conclusion here about b_{H,C} from the old F-coefficients. Such a rank-drop cell has dimension n in S_H and cannot be discarded as part of the dim<n set Z_{C,J}. The earlier branch and mixed-branch calculations illustrate additional closedness identities that can sometimes determine coefficients on such new families; they are not consequences of the noncontracted-cell argument.

Thus adjoining units automatically transports normalized coefficients across the source pieces where the old moment retains full rank. The genuinely new rank-drop pieces are the remaining problem for that refinement. This is not a proof that they are accessible, that finitely many further refinements suffice, or that any one known moment determines T.

## 7. Limits, preservation and review gate

The geometric isolation argument is about maximal-variation source skeleta of actual ordinary analytic moments on the same V and locally finite compact source cell decompositions. It removes the artificial extra S1 hypothesis on the generically noncontracted locus, not the representation premise or the full-rank hypothesis. It makes no assertion that two unrelated target images determine common source cells. Rank drop, failure to have a common ordinary domain, and lack of (R) are not repaired by this note.

This is a general-n common-refinement coefficient comparison under (R), plus the precise one-projection consequence for adjoining analytic units. No whole-current scalar rigidity, global P21.3 statement, all-chart accessibility theorem, or extension-of-scalars operation on currents is claimed. The historical common-moment supplement and its independent audit remain unchanged rather than being silently rewritten with this stronger result.

This packet is Markdown research support. No new TeX compilation or PDF production is claimed. Primary source locators, exact historical inputs and revalidation are recorded in `SOURCE_LEDGER.md`; freeze hashes are recorded separately. Independent review is pending. No live manuscript, inventory, git or production operation was performed.
