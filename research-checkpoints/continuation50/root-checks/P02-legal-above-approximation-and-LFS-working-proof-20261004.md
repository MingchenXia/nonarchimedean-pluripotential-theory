# Legal above-approximation and a common-neighborhood LFS construction

This is a fresh local root working argument for the current P02.1/P02.2 batch. It has not been sent to either running author, independently reviewed, or accepted as a solution of an original target. It also explains a possible repair of the strict/non-strict G-site gap in the completed R39 subsidiary argument. The earlier frozen drafts, notes, helpers and gap records remain unchanged.

The published foundations used here are the exact cached versions of Thuillier's 2005 thesis and Gubler–Jell–Rabinoff, arXiv:2111.05741v3. Thuillier's lisse class is not identified with strict GJR real PL. The constructions below perform an additional admissible approximation.

## 1. A precise strictification lemma

Let K be complete, algebraically closed and nontrivially valued. Put Gamma = -log|K*|. Let Y be a compact strict rig-smooth affinoid curve, and let phi be a finite continuous Thuillier-lisse function defined on an ordinary neighborhood of Y, subharmonic on Int(Y). For every epsilon > 0, the proposed construction produces a global strict GJR real-PL function a on Y such that

\[
 \phi\le a\le\phi+\epsilon,
 \qquad a\text{ is semipositive on }Y.
\]

There is no assertion that phi itself is strict real PL.

**Finite graph representation.** Thuillier Proposition 3.2.4 applies to the compact strictly analytic domain Y inside the ordinary domain of phi. It represents phi|Y as F composed with the retraction tau of a simply semistable model, where F is continuous and piecewise affine on its finite skeleton. The finite separable extension in that proposition is trivial when K is algebraically closed. F has only finitely many affine pieces by compactness. The model vertices and edge lengths are legal: their coordinates lie in Gamma. All extra nonlegal breakpoints lie in interiors of model edges. In particular, they have two graph directions; they are not new positive-genus or branching vertices.

Since K is algebraically closed, Gamma is divisible. Choosing gamma > 0 in Gamma, it contains gamma Q, and is dense in R. Thus the following approximations use legal cuts over the same ground field.

**Above-approximation at a nonlegal bend.** Fix an edge coordinate t increasing along that edge. If t0 is a nonlegal bend, the adjacent slopes m_left and m_right satisfy m_left <= m_right. This is the one-dimensional subharmonicity inequality: on the open annulus the curvature of the affine skeleton function at t0 is m_right - m_left. This is also the interval case of Thuillier's ddc and Proposition 3.4.4.

Choose legal coordinates alpha < t0 < beta in Gamma, with [alpha,beta] containing no other bend or model vertex. Replace F on that interval by the chord joining (alpha,F(alpha)) and (beta,F(beta)). Its slope is

\[
 m=\frac{F(\beta)-F(\alpha)}{\beta-\alpha},
 \qquad m_{\rm left}\le m\le m_{\rm right}.
\]

Convexity on this two-piece interval gives F <= chord. The new curvature at alpha is m-m_left >= 0 and that at beta is m_right-m >= 0. At t0 the new function is affine, so its former nonnegative curvature has been replaced by nonnegative curvature at two legal points. The original slopes at every model vertex and every other bend are unchanged.

Do this on disjoint intervals around all nonlegal bends. If M is the maximum of the absolute slopes on the finite graph, the change on an interval of length d is at most 2 M d. For M=0 no change is required. Otherwise take all these intervals short enough that 2 M d <= epsilon. The resulting function A satisfies

\[
 F\le A\le F+\epsilon.
\]

Its affine subdivision is legal. Its interior vertex curvature is nonnegative: unchanged at old vertices, redistributed as above at moved bends, and zero elsewhere. No boundary sign is imposed.

**Actual global strict real-PL membership.** This is a necessary separate step. GJR 15.3 gives an admissible formal subdivision because every new vertex lies in Gamma. On a small legal star about a vertex v, let T_i be distance along arm i, and zero on the other arms. If that arm has length l_i in Gamma, choose gamma_i in K with -log|gamma_i| = l_i. In the node chart XY=gamma_i the vertical Cartier data for T_i are X on the node, 1 on the central side away from the node, gamma_i on the arm side, and 1 on all other node charts. The transition ratios are units: X on the central overlap and X/gamma_i = 1/Y on the arm overlap. These are the canonical Cartier data of GJR 15.4 for this legal integral affine function.

Consequently the associated formal metric on the generically trivial line bundle has -log||1|| = T_i composed with tau. It is an actual PL function, including at the central genus vertex; its residue line bundle there is O(p_i), not a demanded principal divisor. Every real affine star function is A(v) + sum_i s_i T_i with real outgoing slopes s_i. A real constant is real PL because K is nontrivially valued. This proves real-PL membership on the star. On each open edge there is the ordinary annulus-unit formula c+s(-log|T|). Off the skeleton the pullback is constant on each retraction fiber. These finitely many strict local constructions agree as functions. GJR Definition 5.1 and the sheaf property therefore give global strict real-PL membership of a=A composed with tau. No global commensurability of the real edge slopes is assumed.

**Actual semipositivity.** At an interior vertex the residue real line bundle has degree equal to the sum of its outgoing slopes, since K is algebraically closed and the attaching residue points have degree one. This is the degree computation in the proof of GJR Proposition 15.7, now applied to the line bundle actually constructed above. Its degree is nonnegative. A line bundle on a proper smooth curve is nef exactly when its degree is nonnegative, so the residue is nef. GJR's definition and formal residue criterion imply semipositivity at the ordinary germ. On edge interiors the function is harmonic, and off the skeleton it is constant. At a relative-boundary vertex the reduction curve is nonproper; GJR Proposition 15.5(2) says real PL is harmonic there, so it introduces no missing sign condition. This proves semipositivity on the whole Y. Uniform inequalities on the graph pull back to the whole analytic curve; omitted directions and type-4 points are included.

This lemma avoids the false strict/non-strict identification. It is not an ordinary smooth approximation theorem.

## 2. Decreasing sequences from the published net

Suppose in addition that K has a countable dense subset, and u is an arbitrary subharmonic function on an ordinary open neighborhood of Y. No continuity of u is assumed. Apply Thuillier Theorem 3.4.2 on a relatively compact ordinary open U containing Y whose closure is inside that starting domain. It gives a decreasing directed family of finite continuous lisse subharmonic functions phi_i on U with infimum u. The proof indexes it by finite sets of interior type-2/type-3 points, ordered by inclusion.

Here is the required countable extraction. A strict affinoid algebra over K is a separable Banach space: countably many Tate polynomials with coefficients from a countable dense subset have dense images. For bounded multiplicative seminorms,

\[
 \big|\,|f(x)|-|g(x)|\,\big|\le\|f-g\|.
\]

Thus evaluations on that dense subset separate points and generate all evaluations by uniform approximation. Its compact Berkovich spectrum embeds in a countable product of compact intervals, so is metrizable and second countable. A relatively compact ordinary open in a good separated space is covered by finitely many interiors of affinoid neighborhoods of its compact closure, hence is second countable as well.

For each rational r, the open set {u<r} is the union of {phi_i<r}. It is Lindelof. Choose a countable subcover for each r, enumerate all chosen indices, and take successive dominating indices in the directed set. The extracted phi_j decrease on the same ordinary U and have infimum u: if their limit at a point exceeded u, an intermediate rational r and its selected cover member would contradict that inequality. This also works at u=-infinity.

Apply the preceding lemma to each phi_j|Y with delta_j=4^{-j}, obtaining global semipositive strict real-PL a_j with phi_j <= a_j <= phi_j+delta_j. On the fixed W=Int(Y), set

\[
 b_j=a_j+2\delta_j.
\]

Then phi_j+2delta_j <= b_j <= phi_j+3delta_j, while

\[
 b_{j+1}\le\phi_{j+1}+3\delta_{j+1}
 \le\phi_j+\tfrac34\delta_j
 <\phi_j+2\delta_j\le b_j.
\]

Therefore b_j is a decreasing sequence of semipositive strict real-PL functions on one fixed ordinary W, converging pointwise to u, including any permitted -infinity values. Uniform convergence to u is not claimed. On an identically -infinity component one may instead use constants -j.

The sequence restricts to overlaps. Each of its semipositive real-PL members pulls back along every analytic morphism and every analytic field extension by GJR Proposition 7.6; pullback preserves the same inequalities and pointwise limit. This concerns the actual starting function and its approximants, not a scalar-envelope family identity.

## 3. The additional LFS step on an actual one-vertex star

This step has extra geometric hypotheses that must not be concealed. Assume Y is an actual strict semistable star domain with one central interior type-2 vertex v and all its other model vertices at relative boundary. Its central reduction curve C_v is proper smooth. Assume every other interior type-2 point of W=Int(Y) has reduction P1. These are the usual star/annulus/omitted-disc properties, but their application to an arbitrary analytic starting point must be justified separately before claiming a theorem on all curves.

Choose one arm of positive legal length, and let h'=T_1 composed with tau, using the formal Cartier construction in Section 1. Then h' is globally real PL and semipositive, satisfies 0 <= h' <= M for a finite M, and its residue at v is O(p_1), of positive degree. It is harmonic on all other interior germs.

For any semipositive real-PL a on Y and any eta>0, consider a+eta h'. At v its residue real line bundle has strictly positive degree. A real line bundle of positive degree on a proper smooth curve is real ample in the exact sense preceding GJR Definition 7.8. Here is the algebraic argument. Write its class as sum r_i L_i with integral line bundles L_i. The degree is a positive linear form with integral coefficients in these finitely many coordinates. Take a small rational box around the vector (r_i), all of whose corners still have positive degree, and express the vector as a convex combination of its rational corners. Clear denominators at each corner. This expresses the original class as a nonnegative real linear combination of integral positive-degree line bundles. Each such line bundle is ample: a sufficiently high power has degree at least 2g+1; Serre duality gives vanishing of H1 after removal of a length-two subscheme, so evaluation separates points and tangents and that power is very ample. Thus the real class is ample, and in particular semiample.

At every other interior type-2 point the reduction is P1. Its real Picard group is generated by O(1), and its nef classes are the nonnegative real multiples of O(1). They are semiample. At a type-3 point a legal real-PL graph function is affine in an annulus-unit log coordinate, so is an LFS expression after inverting the unit if necessary. At a type-1 or type-4 point a model graph function is locally constant off its finite skeleton, and is LFS there. Thus a+eta h' is LFS at every point of the same W by GJR Definition 7.8. A semiample residue, not just a nonnegative curvature measure, was proved.

Apply this to a_j from Section 2 with eta_j=delta_j/(M+1), and put

\[
 B_j=a_j+\eta_j h'+4\delta_j.
\]

Then on W,

\[
 \phi_j+4\delta_j\le B_j\le\phi_j+6\delta_j,
 \qquad B_{j+1}\le\phi_j+\tfrac32\delta_j<B_j.
\]

Each B_j is LFS on the same ordinary W and B_j decreases to u. This is a direct LFS sequence; it is not a diagonalization of unrelated germwise approximations from GJR Proposition 7.10. Pullback preserves LFS directly from GJR 7.9's ordinary local nonnegative combinations of finite maxima of analytic-unit log norms. Therefore the sequence and its limit pull back after every analytic field extension and curve morphism.

LFS functions themselves are ordinary CLD ordinal-stage-1 sections, by the explicit decreasing smooth log-sum-exponential construction in CD v2 Proposition 8.9.4. Hence this LFS sequence would also place u in ordinal stage 2 on W. It supplies no single ordinary smooth sequence decreasing to u, so stage 1 is not inferred.

## 4. Exact remaining applications and limitations

The strictification and monotonic-error arguments are independent of semiampleness. The final LFS application additionally requires the common actual star described in Section 3. For an arbitrary boundaryless rig-smooth curve point, one must verify the selection of a compact strict Y inside the domain of the published approximation net, with the required residue curves, an arm of positive length and no other positive-genus interior vertices. Standard semistable geometry suggests selecting a small legal star at a type-2 point, an annulus at a type-3 point, and a disc neighborhood at a type-1 or type-4 point. This selection, including domination of the model representing each phi_j without introducing a positive-genus interior germ, has not yet been fully checked against all indispensable primary source statements here. It is an outstanding application, not an omitted hypothesis.

The argument above is restricted to algebraically closed countably dense ground fields. No arbitrary-field descent of LFS, no countable extraction over nonseparable fields, and no positive statement at the relative boundary of a general starting analytic domain has been proved. The compact Y is an auxiliary domain; W is its ordinary interior.

A proper projective-fiber argument can reduce a globally defined classical psh function on an entire projective-space bundle to its base: an usc function on a compact connected boundaryless fiber attains a maximum, and the interior maximum principle makes its maximum locus open and closed, hence the function constant (or identically -infinity). Ordinary local sections then give the base psh function. This does not apply to an arbitrary open subset of a fiber, so it is not a theorem about every psh germ on every subdomain of that higher-dimensional bundle. That quantifier distinction must be resolved against the original P02 target before counting such a sector as sufficient progress.

No original sharp characterization, necessity theorem, or completed P02/P03 solution is claimed. No independent acceptance, provider submission, author feedback, GitHub push, or alteration of a frozen proof has occurred.
