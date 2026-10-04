# Exact final status

{
  "id": "P03.3",
  "status": "partial",
  "exact_result": "Unverified draft sufficient theorem: every finite continuous obstacle has a finite continuous full exact LFS/semipositive-real-PL raw envelope on arbitrary compact strict rig-smooth curve affinoids over any complete nontrivially valued field, with global real-PL approximating minorants, genus and cycles allowed, and exact raw-envelope compatibility for every analytic scalar extension. The same continuity holds on actual analytic projective bundles and products with smooth geometrically connected proper projective varieties, via the continuous minimum over actual analytic fibers. Homeomorphic normalization gives a further ground-field curve sector over perfect fields. A fresh explicit analytic nodal counterexample, also with projective factors, obstructs an unrestricted assertion. The original sharp geometric classification is not claimed.",
  "proof_file": "P03.3-argument.md",
  "concrete_gaps": [
    "No sharp necessary-and-sufficient classification for general good strict analytic domains or normal/geometrically unibranch higher-dimensional domains.",
    "No higher-dimensional realization, semipositive globalization, or arbitrary nonprojective descent theorem for the full exact competitor family.",
    "No extension of the finite-separable semistable argument to non-rig-smooth normal curves over imperfect fields.",
    "No scalar-envelope identity asserted for the extra pointwise-bijective-normalization sector when normalization splits after extension.",
    "The nodal counterexample does not prove necessity for every branched or nonnormal space; relative-boundary behavior on general noncompact domains remains unclassified."
  ]
}

# Entire final proof

# P03.3: full curve envelopes and actual projective factors

This is a fresh, unverified mathematical draft addressing P03.3 only. It proves a sufficient geometric sector and an analytic branch counterexample. It does not claim the original sharp classification. In particular, no unpublished book assertion in the input is used as a theorem.

## 1. Precise result and conventions

Let K be a complete non-Archimedean field with nontrivial valuation. All spaces below are good, separated and strictly analytic. Put

E_X(f) = {h : X -> R : h <= f, and h is locally Fubini–Study or semipositive real PL},
P_X(f) = sup E_X(f).

PL and LFS have their published meanings in Gubler–Jell–Rabinoff, arXiv:2111.05741v3 (7 March 2025), Definitions 5.1 and 7.8. In particular, an LFS function is an R-PL function whose residue line bundle is semiample; it is semipositive. Thus this exact union is the entire semipositive real-PL family. We do not replace it by invariant functions, graph functions, an equicontinuous family, or the LFS-only family. Real constants belong to the family: choose alpha in K with 0 < |alpha| < 1 and express a constant as a real multiple of log|alpha|.

**Theorem A (affinoid curves).** If X is a compact strictly affinoid rig-smooth curve of pure dimension one, then, for every finite continuous f on X, P_X(f) is finite and continuous and P_X(f)^* = P_X(f). There is a sequence of GLOBAL semipositive R-PL minorants b_n <= f with

0 <= P_X(f) - b_n <= 2/n everywhere on X.

No genus, tree, rationality, or acyclicity condition is imposed. X may be disconnected; connected normal curves over a perfect K, in particular algebraically closed K, are included. For EVERY analytic extension F/K,

P_{X_F}(f o pi) = P_X(f) o pi.

The upstairs envelope here also uses its entire competitor union. All these envelopes and pullbacks are continuous. Their classical pshness is a separate consequence of uniform approximation, not the reason continuity holds. No CLD-v2 classification is asserted.

**Theorem B (actual projective geometry).** Let X be as in Theorem A. Let either Y = P_X(V) for an analytic locally free sheaf V of positive rank, or Y = X x_K Q^an for a smooth geometrically connected proper projective K-variety Q. Let p:Y -> X be the actual analytic projection. For a finite continuous obstacle f on Y define

g(x) = min {f(y) : y in p^{-1}(x)}.

Then g is finite continuous, and

P_Y(f) = P_X(g) o p.

The right side is continuous and equals its usc regularization. This conclusion uses every competitor on Y and every finite continuous obstacle, including noninvariant obstacles. It also commutes with every analytic scalar extension. More generally the displayed envelope identity is valid for these projections over any compact good separated strict base; continuity then follows whenever the base has the asserted envelope-continuity property.

**Additional normalization sector.** Over a perfect nontrivially valued K, let X be a reduced strict affinoid curve whose normalization nu:Xtilde -> X is pointwise bijective. Then P_X(f) is continuous for every finite continuous f. This conclusion is on the ground space. It does not assert that pointwise-bijective normalization persists under extension, or that this extra sector has the scalar-envelope identity of Theorem A.

## 2. Checked public foundations and their precise uses

Write GJR for arXiv:2111.05741v3; GRa for arXiv:2506.13548v2 (17 September 2025); GRb for arXiv:2503.05513v1 (7 March 2025); Thu for Thuillier's 2005 thesis, HAL tel-00010990v1; Ber for Berkovich, IHES 78 (1993).

1. GJR Definition 5.1 and Remark 5.2 define real PL by G-local finite real linear combinations of logarithms of analytic units. PL membership is a G-sheaf. Semipositivity is instead an ordinary analytic germ condition, GJR Definition 7.2 and Remark 7.3(3); it cannot merely be glued from positivity on a G-cover.
2. GJR 15.1–15.4 and Proposition 15.5 construct a vertical Cartier metric from a legally subdivided integral affine skeleton function. In the dense-value-group case subdivision vertices must lie in Sigma(Gamma), not at arbitrary real points. Proposition 15.5(2) says an R-PL function at a relative-boundary point of a rig-smooth curve is harmonic there; its affine reduction component imposes no nef degree sign.
3. In the proof of GJR Proposition 15.7, degree on an interior proper reduction component is the weighted sum of outgoing slopes. GJR Lemma 7.4 identifies nef formal line bundles and semipositive model functions. Genus affects the residue Picard class but not the nef degree condition on a curve.
4. GJR Proposition 7.6 gives analytic pullback, all analytic scalar extensions, and proper-surjective descent of semipositivity once R-PL membership is known. Corollaries 5.12 and 5.13 and Proposition 7.7 give real-PL and semipositive real-PL descent along finite Galois scalar extensions. Proposition 5.11 proves the PL descent by a finite-flat formal norm. We use these results with coefficient group R, which is divisible, and only finite extensions.
5. Thu Theorem 2.3.8 applies to a strict rig-smooth affinoid of pure dimension one. Its proof first embeds it, after finite separable extension, as an affinoid domain of a smooth projective curve. Thu Proposition 3.2.4 represents a Thuillier-lisse function on a compact analytic domain by a finite affine skeleton function after finite separable extension. Thu Proposition 3.2.7, its proof, Lemma 3.2.8, and Corollary 3.2.9 give uniform density on a compact smooth boundaryless curve. We apply those density statements on the ambient projective curve, not on a boundary point of the given affinoid. Thuillier-lisse membership is not itself our proof of real-PL membership.
6. GRa Theorem 4.3 says that on a good strict space over a nontrivially valued field an R-PL function is semipositive iff classically psh. Definition 4.1 quantifies over all analytic extensions and curve morphisms. Theorem 6.1 is the local maximum principle at interior points. Lemma 6.2 gives nonempty relative boundary for each positive-dimensional affinoid component. In 2.11(5'), extended boundary is contained over base boundary. Theorem 6.5 and its proof give stability under a pointwise limit that is already usc.
7. GRa Lemma 3.9(1,4,6) gives rig-smooth normalization over a perfect field, quotient topology for normalization, and R-PL descent through normalization. Its proof of (6) uses local constancy near a non-normal rig-point, so it does not require analytic invertible functions to generate every harmonic germ at a positive-genus vertex.
8. Ber Corollary 3.7.4 says a smooth morphism is open. The projective projections in Theorem B are smooth in this relative, boundaryless sense. A scalar projection is not declared open. Ber Theorem 7.1.1 gives algebraic/analytic cohomology comparison with compact support for a compactifiable scheme and an abelian torsion sheaf. Applied in degree zero to a proper connected scheme and the constant Z/2 sheaf, it proves connectedness of its analytification: a nontrivial analytic clopen partition would give an extra section. Properness makes compact-support degree-zero cohomology equal to ordinary degree-zero cohomology here.

The complete literal selected pages, statement/proof selections, and checked applications are retained in source-extracts/source-provenance.json and the accompanying text files. GJR PDF page 78 and Thu PDF page 85 (printed page 71) were also inspected as rendered PDF images. The crucial GJR restriction is Gamma, not its unrestricted real closure; the crucial Thu density space is A^0, not a positivity cone. GRb's relevant statement in the supplied v1 is Proposition 5.1, although GRa's cross-reference calls its earlier numbering Proposition 3.1; we do not conflate these versions. Hashes only authenticate the supplied bytes.

## 3. Actual real-PL realization on a finite skeleton

First suppose Z is a compact rig-smooth curve with a strictly semistable formal model. Its skeleton Sigma is a finite weighted metric graph, and tau:Z -> Sigma is the deformation retraction. An edge e has length in Gamma = -log|K^*| and weight w(e). Boundary vertices B correspond to nonproper special-fiber components. For an affinoid, B is its relative boundary, and every connected component meets B.

A subdivision will be called legal here if every new cut is at a Gamma-coordinate on its edge. GJR 15.3 then gives an admissible formal subdivision model. The strictly semistable models in GJR 15.2 have smooth irreducible special-fiber components, hence no self-node loop edges. Cycles consisting of several edges are fully allowed.

**Realization lemma.** If A is continuous on Sigma, affine on each edge of a finite legal subdivision, with arbitrary REAL slopes and values, then H=A o tau is a GLOBAL R-PL function on Z. It is semipositive precisely when

sum_{e out of v} w(e) partial_e A >= 0

at every interior vertex v of that subdivision. No inequality is required at B. It is harmonic away from vertices with nonzero slope sum (and is harmonic at relative-boundary vertices).

Here is the local formal construction, including the genus issue. Around a vertex v choose a small closed star with all arm lengths in Gamma. Its inverse image is a compact strict analytic neighborhood of v. After the legal formal subdivision, its special fiber consists of the central component C_v and the arm components. For each arm i there is an integral function T_i on this star which is distance from v on arm i and zero on every other arm.

On the formal node joining C_v to arm i, use the semistable chart XY=gamma_i, with -log|gamma_i| equal to that arm's length and t=-log|X| measured from C_v. Define the vertical Cartier divisor D_i by the following local equations: X on the node chart, 1 on the central side away from that node, and gamma_i on the arm side away from the node. The ratios are units: X is a unit on the central overlap; on the arm overlap X/gamma_i=1/Y is a unit. On all other node charts the equation is 1. These local Cartier data also agree on etale overlaps, using the specified central/arm branches. This is the construction of GJR 15.4 in these local coordinates; for nonrational nodes the same Cartier data are taken on the etale chart and descend, and the closed-point residue degree is the edge weight.

The line bundle O(D_i), trivialized on the generic fiber by its canonical section 1, has

-log||1|| = T_i o tau.

This follows on each of the above charts from -log|X|, 0, and -log|gamma_i|, respectively. Thus it is an actual PL function, G-locally the logarithm of an analytic unit with the appropriate sign. Its restriction to C_v has divisor class O(p_i), where p_i is the attaching closed point; its degree is [kappa(p_i):ktilde]=w(e_i). This is why no PRINCIPAL divisor on C_v is required. In positive genus O(p_i) generally is not principal, and that causes no difficulty for a formal metric on the analytically trivial line bundle.

Now on this star

A o tau = A(v) + sum_i s_i (T_i o tau)

for its real outgoing slopes s_i. The constant is R-PL, so this is an actual finite real linear combination of PL metrics. On open edge neighborhoods an annulus coordinate gives the expression c+s(-log|T|). On every omitted residue disc the function is constant. These expressions cover Z and agree as functions, hence prove GLOBAL R-PL membership by Definition 5.1 and the sheaf property. They do not assert that all global real graph functions share one globally commensurable integral slope vector. There is no such requirement in real-PL membership.

At an interior vertex the residue real line bundle has degree sum_i w(e_i)s_i. On the proper smooth reduction curve nef means degree >=0, and numerically trivial means degree zero. This proves the positivity and harmonicity assertions at ordinary germs, independently of G-cover gluing. At relative boundary the reduction component is nonproper and the nef curve test is vacuous, exactly as GJR Proposition 15.5(2). Off the finite vertices the formulas are harmonic. Points of types 1 and 4, including points not visible on the finite skeleton, lie in constant fibers locally; they introduce no untested sign or membership condition.

The construction permits nonprincipal degree-zero residue classes at genus vertices. It therefore does not confuse harmonic functions with ordinary-local logarithms of analytic units; GJR Remark 15.10 and Thu Theorem 2.3.21 explicitly distinguish them.

## 4. The finite graph obstacle problem and full analytic comparison

Let G be real affine on every edge of a finite legal subdivision of Sigma. For vertices V and a vector a in R^V, put

D a(v) = sum_{vw} [w(vw)/length(vw)] (a(w)-a(v)).

Take all vectors satisfying a(v)<=G(v) and D a(v)>=0 for v outside B. Let m=min_V G. The constant vector m is feasible. The coordinatewise maximum of two feasible vectors is feasible: at v select the vector supplying its maximum value, and each neighboring maximum is at least that selected neighbor value. Thus its D value cannot decrease at v.

Intersect the feasible set with [m,max_V G]^V. This is compact and nonempty. Maximize each coordinate separately, and take the coordinatewise maximum of those finitely many maximizing vectors. The result u is the greatest feasible vector. It is greatest among ALL feasible vectors, since clipping another vector from below at m preserves feasibility.

At a boundary vertex, u(v)=G(v): increasing that coordinate would only help inequalities at adjacent interior vertices. At an interior vertex with u(v)<G(v), D u(v)=0: otherwise one could increase u(v) slightly, retaining its own inequality and helping its neighbors. Consequently the affine interpolant U of u is below G, has nonnegative interior slope sums, and is harmonic off the finite contact vertex set

S={v : u(v)=G(v)}.

S contains B. By the realization lemma H=U o tau is a GLOBAL semipositive real-PL minorant of g=G o tau. A selected graph function has now been shown to be an actual global competitor.

To prove that it bounds the FULL analytic family, take any h in E_Z(g). It is continuous and classically psh by GJR Definition 7.8 and GRa Theorem 4.3. On S, h<=g=H. Off S, H is harmonic in the real-PL sense, so h-H is classically psh there. If max_Z(h-H)=M>0, the maximum locus is nonempty and closed in compact Z and disjoint from S. Every point of that locus lies in Int(Z), since B is contained in S. The local maximum principle makes that locus open in Z. It therefore contains an entire connected component of Z, contradicting that every such component meets B. Thus h<=H on ALL of Z, not only on the skeleton. We have proved

P_Z(g)=H.

This includes all noninvariant analytic competitors, every omitted direction, and type-4 points. It is not an envelope computation restricted to graph competitors.

The same comparison holds after EVERY analytic extension E/K. Pull H back to Z_E. It remains semipositive, and harmonic off pi^{-1}(S), by GJR Proposition 7.6. Boundary satisfies partial Z_E subset pi^{-1}(B), by GRa 2.11(5'), and every affinoid component of Z_E has nonempty boundary, by Lemma 6.2. On pi^{-1}(S), H o pi=g o pi. Repeat the maximum-locus argument for an arbitrary upstairs competitor. This proves the strong exact identity

P_{Z_E}(g o pi)=H o pi.

It requires neither openness of pi, nor any statement about commuting usc regularization, nor constancy of an unproved scalar fiber regularization.

## 5. Uniform density for arbitrary obstacles and legal cuts

For a strict rig-smooth affinoid X/K, finite separable extension embeds X in a smooth projective curve C; this is the first step in the checked proof of Thu Theorem 2.3.8. For disconnected X apply it componentwise and take a common finite extension. The projective Berkovich space is compact Hausdorff. The affinoid is a closed subspace, so Tietze's extension theorem extends any finite continuous obstacle f to a continuous real function on C^an.

Apply Thu Corollary 3.2.9 on this smooth BOUNDARYLESS curve, with the compact set X. For every eta>0 obtain a Thuillier-lisse function uniformly within eta of f on X. By Proposition 3.2.4, after another finite separable extension its restriction to X is A o tau for a continuous finite piecewise affine A on a semistable skeleton. This step gives graph factorization, not yet our PL realization. It is valid for arbitrary continuous f, not only radial or invariant f. In particular its uniform error controls values on all omitted directions and type-4 points.

A may have breakpoints not legal for a formal subdivision. Retain the original model vertices. On every edge, move each of the finitely many interior breakpoints to a nearby LEGAL coordinate and retain the corresponding function values; use affine interpolation on the moved intervals. If edge lengths are fixed and successive breakpoints stay distinct and in their original order, the new interpolant converges uniformly to the old one as the displacements tend to zero. For example, on each interval it is A composed with a piecewise affine increasing homeomorphism tending uniformly to the identity. Uniform continuity of A proves the asserted error estimate.

If Gamma is dense, coordinates in Gamma supply all needed approximations, without an extension. If Gamma is discrete, write Gamma=delta Z and choose a sufficiently fine grid (delta/N)Z, with N prime to char(K) when that characteristic is positive. Adjoin an N-th root of an element of valuation delta. This is a finite separable extension, and its value group contains that grid. Its semistable base-change model admits the desired legal Gamma-cuts. Thus arbitrary real subdivisions are never silently claimed to be formal-model subdivisions. In the algebraically closed case Gamma is divisible and dense, so no discrete case arises.

Finally pass to a finite Galois extension L/K containing these finitely many separable extensions. Scalar base change preserves the semistable model; its retraction and skeleton maps have the functoriality in Thu Proposition 2.2.21 and the node-chart description used in GJR 15.2. The pulled graph function is still a finite legal affine graph function, possibly on a split or weighted refined skeleton. Because scalar projection is surjective, all uniform error estimates are unchanged.

Choosing the preliminary density and interpolation errors with sum <=epsilon proves the following usable statement:

For every epsilon>0 there are a finite Galois L/K, a semistable model of X_L, and a finite legal affine graph obstacle g=G o tau on X_L with ||g-f o pi_L|| <= epsilon.

No restriction has been placed on f. The realization lemma gives actual global real-PL membership for this g (it need not be semipositive); Section 4 supplies its actual semipositive graph envelope H=P_{X_L}(g).

## 6. Finite Galois averaging, continuity, and all scalar extensions

For sigma in Gal(L/K) put g_sigma=g o sigma and H_sigma=H o sigma. Each H_sigma is a global semipositive R-PL function; all g_sigma are within epsilon of f o pi_L. Section 4's comparison applies to each translated pair and, importantly, after any further scalar extension.

Set A=(1/|Gal(L/K)|) sum_sigma H_sigma. It is invariant, continuous, globally semipositive R-PL, and A-epsilon <= f o pi_L. By GJR Proposition 7.7 it descends to a GLOBAL semipositive R-PL function b_epsilon on X with

b_epsilon o pi_L = A-epsilon.

This uses sums, scalar multiplication, and verified invariant descent. It never assumes a maximum of real-PL functions is real PL.

Take ANY ground competitor h<=f. Then h o pi_L-epsilon <= g_sigma for every sigma. It is still a semipositive real-PL function, so exact full-family comparison implies h o pi_L<=H_sigma+epsilon for every sigma. Average and descend the inequality. Since b_epsilon is a minorant,

b_epsilon <= P_X(f) <= b_epsilon+2epsilon.

Taking epsilon=1/n gives the sequence in Theorem A. It proves finiteness (constants also give a baseline) and continuity as a uniform limit on the ENTIRE compact analytic space. Only now may one conclude P_X(f)^*=P_X(f).

For an arbitrary analytic extension F/K, take a common analytic extension E of F and the finite L; one can choose a field factor of F tensor_K L, since L/K is finite separable. Pull an arbitrary full upstairs competitor h_F<=f o pi_F to X_E. For every sigma its pullback minus epsilon is bounded by the pulled g_sigma. The scalar form of Section 4 gives

h_F o pi_{E/F} <= (A+epsilon) o pi_{E/L}.

Since A-epsilon=b_epsilon o pi_L, surjectivity of X_E -> X_F yields

h_F <= b_epsilon o pi_F+2epsilon.

Conversely b_epsilon o pi_F is an upstairs competitor. Consequently

b_epsilon o pi_F <= P_{X_F}(f o pi_F) <= b_epsilon o pi_F+2epsilon.

The SAME ground sequence tends uniformly to both sides' asserted common limit, proving the scalar identity in Theorem A. This handles all analytic extensions, not merely finite, algebraic, or completed algebraic-closure extensions.

For clarity, positivity of the resulting continuous function also has the full quantifiers. Each b_n is classically psh by GRa Theorem 4.3, so its pullback along any extended analytic test curve is subharmonic. Uniform convergence persists under pullback. On a strict affinoid test domain, harmonic boundary comparison for the limit follows by applying it to b_n with an added arbitrarily small constant and then passing to the limit. Equivalently this is the checked proof of GRa Theorem 6.5. This verifies the curve and scalar tests separately from the continuity proof. It asserts no CLD-v2 result.

If K is perfect, a normal curve is rig-smooth by GRa Lemma 3.9(1), so the theorem includes the requested arbitrary normal affinoids over algebraically closed K. Positive-genus reduction vertices and cyclic finite skeleta have nowhere been excluded.

For the extra normalization sector, a finite bijective normalization of an affinoid is a homeomorphism, by compactness and Hausdorffness (or GRa Lemma 3.9(4)). Given a semipositive real-PL function htilde on Xtilde, transfer it to a continuous function h on X. GRa Lemma 3.9(6) makes h R-PL. GJR Proposition 7.6(1') makes h semipositive, since normalization is proper surjective. Conversely every base competitor pulls back. Thus the two FULL envelopes agree through this homeomorphism. Theorem A on Xtilde gives continuity on X. Uniformly approximating competitors also descend. The statement does not identify envelopes on arbitrary scalar extensions where normalization can cease to be bijective.

In that last sector the ground envelope's pullback is still continuous and passes all extended curve tests, by its descended uniform semipositive approximants. What is deliberately left unclaimed is equality with the envelope of the enlarged upstairs competitor family.

## 7. Proper projective factors and projective bundles

First, a finite continuous classically psh function on a connected compact boundaryless analytic space is constant. It attains a maximum; by GRa Theorem 6.1 the maximum locus is open, and by continuity it is closed. Connectedness forces it to be the whole space. Hence on a connected proper projective analytic space the full obstacle envelope is simply the constant min f. This observation concerns ordinary real functions, not metrics with a nontrivial background line bundle.

This statement also applies to connected singular proper projective spaces: no normality assumption entered the maximum-locus proof. Thus normality is not a necessary condition in the original unrestricted domain class. The discontinuous affinoid branch example below and the constant proper envelopes must both be respected by any proposed sharp classification.

For p:Y -> X in Theorem B, the analytic fiber over x is a proper connected space over H(x): it is P(V_x)^an or Q_{H(x)}^an. Algebraic geometric connectedness makes the scheme over H(x) connected. To check the analytic connectedness used here, apply Ber Theorem 7.1.1 in degree zero with the constant Z/2 sheaf to this proper scheme. Algebraic global sections of that constant sheaf are exactly its two constant values; a nontrivial analytic clopen partition would give a third section, contradicting comparison. A competitor h on Y restricts to a classically psh function on this fiber, because the fiber is an analytic morphism into Y_{H(x)} and the definition permits the scalar extension H(x)/K. It is continuous and therefore constant there. These are actual Berkovich fibers, not a product of sets of K-points.

Consequently h=a o p for a function a on X. Properness makes p a closed surjection with compact fibers; since h is continuous and fiberwise constant, the quotient topology makes a continuous. For a projective bundle, ordinary analytic trivializations of V give analytic sections over an ordinary open cover of X. Restrict h to such a section: a is R-PL and semipositive there, by GJR Proposition 7.6. The ordinary local definitions give GLOBAL semipositive R-PL membership of a.

For a factor Q with no K-rational point, choose a closed point of the nonempty projective variety Q. Its residue is a finite extension L/K, so Q_L has an L-point. The section x -> (x,q) over X_L shows a o pi_L is semipositive R-PL. GJR Corollary 5.12 and Proposition 7.6(2') descend real-PL membership and semipositivity of a. No rational point over K is required and no unproved higher-dimensional PL descent is invoked.

Conversely every base semipositive real-PL a pulls back as an admissible competitor on Y. Since h<=f iff a(x)<=min_{p^{-1}(x)} f=g(x), this proves a bijection between the entire competitor families. Therefore P_Y(f)=P_X(g) o p, including for the full exact union.

It remains to establish continuity of g, rather than assume it. Properness and compact fibers give attainment. If g(x)>c, the closed set {y:f(y)<=c} has closed image under p, and its complement is {x:g(x)>c}; hence g is lower semicontinuous. If g(x)<c, some y in the fiber has f(y)<c. The open set {y:f(y)<c} has open image, because p is smooth and thus open by Ber Corollary 3.7.4. Its image is {x:g(x)<c}; hence g is upper semicontinuous. It is therefore finite continuous. Theorem A now proves Theorem B.

For any analytic extension F/K and any x' over x, the extended analytic fiber is Y_x tensor_{H(x)} H(x'). Scalar projection of this fiber onto Y_x is surjective. The minimum of f pulled back to it therefore is exactly g(x). Thus the new base obstacle is g o pi_F. The family identification holds over F as well, and Theorem A gives the asserted raw-envelope scalar compatibility and continuity. Boundary is handled through the base curve; the projective projection has no relative boundary. There is no extra slope sign imposed on the inherited base-boundary fibers.

## 8. A fresh actual analytic branch counterexample

Let K be any complete nontrivially valued field, choose alpha with 0<|alpha|<1, put A=-log|alpha|, and fix a>0. Take

X=M(K<x,y>/(xy)).

It is the union of the closed x-disc D_x and the closed y-disc D_y, meeting at their rigid origins o. Define the finite continuous obstacle by f=0 on D_x and

f(y)=-a min(|y|,1)=-a|y|

on D_y. The formulas agree at o, and their restrictions are continuous on the two closed branches. The y-Gauss point eta_y has f(eta_y)=-a, while f(o)=0.

For ANY full competitor h on X, its restriction to D_y is semipositive R-PL and classically psh. The singleton-Shilov maximum principle, GRa Theorem 6.4, implies h<=h(eta_y)<=-a on D_y. The constant -a is a global competitor, so P_X(f)=-a on the entire y-disc, including o.

For each integer n>=1 define the actual analytic function

q_n=log max(|alpha|^n,|x|),   h_n=(a/(nA)) q_n.

q_n is PL on the global rational cover {|x|<=|alpha|^n}, {|x|>=|alpha|^n}: on the first domain it is n log|alpha|; on the second it is log|x| and x is invertible. Thus h_n is a GLOBAL real-PL function. GRa Proposition 4.2 makes q_n classically psh, as the finite maximum of a constant and log|x|, allowing the latter to be -infinity where x=0. GRa Theorem 4.3 makes h_n semipositive. It is -a on D_y and <=0 on D_x, hence is a full competitor below f.

For any point of D_x other than o, |x|>0, and h_n ->0. Since f=0 there, P_X(f)=0 on D_x minus o. Therefore the raw envelope is exactly

P_X(f)=0 on D_x minus {o}, and -a on D_y.

Its usc regularization changes only o to 0. Every other y-branch point still has value -a. The sequence of y-rigid points y=alpha^m tends to o, proving an actual discontinuity. No book counterexample or previous generated proof is used.

The projective-family identification in Section 7 holds also over this singular base, without invoking Theorem A. Thus X x_K P^r with obstacle pulled back from f has the pulled-back full raw envelope, and its regularization is likewise discontinuous at the nodal projective fiber. The last regularization statement follows locally from p being open: for a continuous open surjection p and locally bounded s, (s o p)^*=s^* o p, directly by the neighborhood definition of limsup. Alternatively evaluate along a fixed analytic projective section and the two branch approaches. These are actual proper projective factors; they do not cure the branch obstruction.

## 9. What remains open and what this argument does not establish

The original P03.3 asks for sharp additional geometric hypotheses on general good strict analytic domains, with necessity, all finite continuous obstacles, and the full competitor family. Theorems A and B do not classify normal or geometrically unibranch higher-dimensional spaces; they treat curves and geometry whose global competitors are forced to descend along proper fibers.

The new curve argument closes the realization obligation for legal finite-skeleton real functions on strict rig-smooth affinoids, with genus and cycles allowed. It does not prove a corresponding realization or density-preserving semipositive globalization theorem on arbitrary higher-dimensional normal domains. It proves no general envelope descent along a positive-dimensional nonprojective projection, arbitrary finite cover, or normalization with several points in a fiber. The extra pointwise-bijective-normalization sector is not asserted stable under arbitrary scalar extension.

Normal curves over imperfect fields which are not rig-smooth are not covered by the finite separable semistable-reduction argument as stated. Purely inseparable/perfection descent for their exact competitor family is not supplied here. No claim that algebraic closedness is necessary is made: Theorem A expressly removes it in the rig-smooth range. Relative-boundary regularity for general noncompact domains, general branched-curve necessity, and higher-dimensional necessity including codimension-two pinching remain unclassified. The fresh nodal example proves a concrete obstruction, not a necessity theorem for all nonnormal spaces.

No step infers continuity from positivity, an invariant toric result, a modulus bound on a selected family, or finite graph computations. The key comparison bounds EVERY analytic competitor, and the error is uniform for EVERY continuous obstacle and after EVERY analytic extension. This establishes the displayed sufficient sectors, while preserving the original target as open.

## 10. Artifacts and reproducibility

Inputs are retained verbatim in input.json and input-original.json; task-original.json preserves the task object and assignment-original.txt preserves the assignment string. The entire argument is also embedded in the standalone P03.3-paper.tex. status.json has only the requested keys.

Rerun source retention with: python prepare_sources.py

Rerun document checks and the two TeX builds with: python verify_deliverable.py

Actual command output, environment versions, source extraction diagnostics and build logs are under checks/. Rendered source checks are checks/gjr-78.png and checks/thuillier-85.png. The generated PDF is P03.3-paper.pdf when both installed-environment builds succeed. No package installation, alternate model or worker, external message, private campaign material, or heavy computation is used. Successful execution is administrative evidence, not mathematical verification.


# Every actual native canonical note

[
  {
    "id": "n1",
    "summary": "Draft sufficient theorem for the FULL exact union on every compact strict rig-smooth curve affinoid over any complete nontrivially valued field, including normal curves over perfect fields, genus vertices and cycles. Legal skeleton functions are realized as global semipositive real PL; all finite continuous obstacles and all analytic scalar extensions are controlled. This is not the original sharp classification.",
    "detailedSummary": "The raw full LFS/semipositive-real-PL envelope is a uniform limit of global semipositive real-PL minorants b_n with 0<=P-b_n<=2/n, hence finite continuous and equal to its usc regularization. Exact raw-envelope pullback holds for every analytic extension. The proof constructs actual vertical Cartier star metrics before checking proper reduction-component degrees, solves the finite graph obstacle, compares against every analytic competitor, obtains arbitrary-obstacle density on an ambient projective curve after finite separable extension, uses legal value-group cuts, and descends finite Galois averages. Over a perfect field, bijective normalization gives another ground-field continuity sector, without asserting its scalar full-family envelope identity when branches split. All assertions are unverified drafts; higher-dimensional sharpness and necessity remain open.",
    "text": "Let K be complete and nontrivially valued and X a good separated strictly affinoid rig-smooth curve of pure dimension one, possibly disconnected. For finite continuous f let P_X(f) be the supremum of ALL finite functions h<=f which are locally Fubini–Study or semipositive real PL. Use the published definitions in Gubler–Jell–Rabinoff (GJR), arXiv:2111.05741v3, 7 March 2025, Definitions 5.1 and 7.8. LFS is a subclass of semipositive R-PL, so the exact union is the entire semipositive R-PL family. Constants belong to it. The draft theorem is that P_X(f) is finite continuous, equals its usc regularization, admits GLOBAL semipositive R-PL minorants b_n with 0<=P_X(f)-b_n<=2/n, and satisfies P_{X_F}(f composed with pi)=P_X(f) composed with pi for EVERY analytic extension F/K, with the full upstairs family.\n\nActual realization precedes positivity. For a strictly semistable model, its finite weighted skeleton Sigma has edge lengths in Gamma=-log|K*| and relative-boundary vertices B. New formal subdivision vertices are chosen at Gamma coordinates. GJR 15.3–15.4 and Proposition 15.5 give admissible subdivisions and vertical Cartier metrics in this legal range. On a small legal star about v, let T_i be distance along arm i and zero on every other arm. In the formal node chart XY=gamma_i, with central endpoint -log|X|=0 and arm endpoint -log|X|=-log|gamma_i|, the vertical Cartier divisor has equations X on the node, 1 on the central side away from it, gamma_i on the arm side away from it, and 1 on other nodes. The central overlap has X a unit; the arm overlap has X/gamma_i=1/Y a unit. These are the canonical Cartier data of GJR 15.4, also on etale charts. The metric on O(D_i), canonically trivial on the generic fiber, has -log||1||=T_i composed with tau. Its residue restriction on the central component is O(p_i), with degree the edge weight. It need not be principal at a positive-genus vertex.\n\nAn arbitrary REAL affine star function is c+sum s_i T_i. Thus its pullback is actually R-PL by a finite real linear combination of these PL metrics. On an edge it has an annulus-coordinate expression c+s(-log|T|), and on omitted residue discs it is constant. These local expressions agree globally and prove GLOBAL R-PL membership by GJR Definition 5.1 and Remark 5.2. There is no assumption of globally commensurable integral slopes around cycles. Positivity is checked at ordinary germs: on each interior proper reduction component the residue real line bundle has degree sum w(e) partial_e A, as in the checked proof of GJR Proposition 15.7. Nefness on that curve is precisely nonnegative degree; degree zero gives harmonicity. At a relative-boundary vertex the reduction component is nonproper and imposes no sign, GJR Proposition 15.5(2). Off the finite vertices the formulas are harmonic. All omitted directions and type-4 points are included in the analytic construction.\n\nFor an obstacle G affine on a finite legal graph subdivision, consider vertex vectors a<=G with D a(v)=sum_{vw}w(vw)(a(w)-a(v))/length(vw)>=0 at vertices outside B. Constants at min G are feasible. Coordinatewise maxima preserve these inequalities: at v select the vector giving its maximum there, and all neighboring maximum values only increase its D value. A compact truncation between min G and max G therefore has a greatest feasible vector u, obtained by maximizing each coordinate and taking their finite coordinatewise maximum. It is greatest among all feasible vectors by clipping from below at min G. At B it saturates G; at an interior vertex below G it has D u=0, since otherwise that coordinate could be increased slightly. Its affine interpolant U is below G and its pullback H is a GLOBAL semipositive R-PL competitor. It is harmonic off the contact vertex set S={u=G}, which contains B.\n\nNow bound every analytic competitor, not merely graph competitors. By Gubler–Rabinoff (GRa), arXiv:2506.13548v2, 17 September 2025, Theorem 4.3, each full competitor h is continuous and classically psh. On S it satisfies h<=G composed with tau=H. Off S, h-H is classically psh since H is harmonic. A positive global maximum of h-H has a closed nonempty maximum locus disjoint from S. All its points are interior because B is in S. GRa Theorem 6.1 makes the locus open. It would contain an entire connected component, impossible because each affinoid curve component has nonempty boundary (GRa Lemma 6.2). Therefore P(G composed with tau)=H on the WHOLE analytic curve.\n\nThe same comparison holds after EVERY analytic extension E: H pulls back semipositively and harmonically off pi^{-1}(S) by GJR Proposition 7.6, extended boundary is contained over B by GRa 2.11(5'), and each extended affinoid component has nonempty boundary. Hence the full upstairs envelope of the pulled graph obstacle is exactly H pulled back. No openness of scalar projection or commutation of usc regularization is assumed.\n\nArbitrary-obstacle density is obtained using actual published hypotheses. Thuillier's 2005 thesis, HAL tel-00010990v1, Theorem 2.3.8 and its proof embed a strict rig-smooth affinoid, after finite separable extension, in a smooth projective curve. Extend f continuously to that compact Hausdorff curve by Tietze. Apply Thu Corollary 3.2.9 and the proof of Proposition 3.2.7 there, on the boundaryless ambient curve. Proposition 3.2.4 gives finite skeleton factorization after another finite separable extension. This is not yet declared real PL. Move its finitely many interior breakpoints to legal nearby coordinates, keeping their values and interpolating. A piecewise affine increasing homeomorphism of each edge tends uniformly to the identity, so uniform continuity gives uniform convergence of these legal interpolants. Dense Gamma supplies the cuts directly. If Gamma=delta Z, adjoin an Nth root of an element of valuation delta, with N prime to char K when needed; a sufficiently fine delta/N grid is then legal in a finite separable extension. Finally take a finite Galois L/K containing all these fields. Semistable base-change retractions commute in the node charts and on component tubes, as in Thu Proposition 2.2.21. Uniform errors are preserved by surjectivity. Thus for every epsilon>0 a finite Galois L and a legal graph obstacle g on X_L satisfy ||g-f pulled back||<=epsilon. This controls arbitrary noninvariant obstacles, including their omitted-direction and type-4 values.\n\nLet H=P_{X_L}(g), already realized and fully compared. Conjugating its formal charts and residue bundles shows every Galois translate H_sigma is globally semipositive R-PL. Put A=average_sigma H_sigma. Addition, not a pointwise maximum of real-PL functions, makes A invariant semipositive R-PL. GJR Corollary 5.13 and Proposition 7.7 descend A-epsilon to a global semipositive R-PL function b_epsilon on X. It is <=f. For EVERY ground competitor h, h pulled back minus epsilon is below every translated g. Comparison therefore gives h pulled back <=H_sigma+epsilon for each sigma. Averaging and surjectivity give b_epsilon<=P_X(f)<=b_epsilon+2epsilon. Taking epsilon=1/n proves continuity by uniform convergence on the entire X.\n\nFor arbitrary F/K choose a common analytic extension E of F and finite L, for instance a field factor of F tensor_K L. Pull any full F-competitor to E and repeat comparison against each translated graph obstacle. Surjectivity of X_E -> X_F gives b_epsilon pulled back <=P_{X_F}(f pulled back)<=b_epsilon pulled back+2epsilon. The same sequence therefore proves exact raw-envelope compatibility and continuity for every analytic extension. Every extended curve pullback of the limit is subharmonic: pass uniform limits in harmonic comparison on a strict affinoid test domain, or use GRa Theorem 6.5 and its checked proof. Positivity is a separate consequence and no CLD-v2 assertion is made.\n\nFor perfect K a normal curve is rig-smooth (GRa Lemma 3.9(1)), so this includes every requested normal affinoid over algebraically closed K with genus vertices and cyclic skeleta. Also, if a reduced strict affinoid over perfect K has bijective normalization, that finite map is a homeomorphism. A transferred normalization competitor is R-PL by GRa Lemma 3.9(6), then semipositive by proper-surjective descent, GJR Proposition 7.6(1'). The full envelopes and uniform approximants therefore descend, giving ground-field continuity. Its pulled-back ground envelope remains continuous and passes extended curve tests. Equality with the enlarged upstairs competitor envelope is not claimed where normalization splits.\n\nThe full proof is P03.3-argument.md, also entirely embedded in standalone P03.3-paper.tex. Literal primary pages/proofs and checked hypotheses are in source-extracts/source-provenance.json. Rerun source retention with python prepare_sources.py and builds/checks with python verify_deliverable.py. All six supplied source hashes matched; GJR page 78 and Thu PDF page 85 were visually checked for the legal-value-group and density statements. These are provenance observations, not proof certificates. This theorem is an unverified sufficient-sector draft, not a sharp classification of the original P03.3; higher-dimensional normal/unibranch domains and imperfect non-rig-smooth normal curves remain unresolved.\n\nArtifacts: /workspace/research/campaigns/round-40/P03.3-public-source-general-curve-continuity/artifacts/codex-y7aOMx",
    "support": []
  },
  {
    "id": "n2",
    "summary": "Draft full-family continuity extends to actual analytic projective bundles and products of the curve sector with smooth geometrically connected proper projective varieties, for EVERY finite continuous obstacle. The envelope is the base envelope of the minimum over actual analytic fibers. Connected proper spaces, even singular, have constant envelopes, so normality is not necessary in the unrestricted domain class.",
    "detailedSummary": "Every full competitor is constant on each proper connected analytic fiber by the published interior maximum principle. Real-PL descent is proved using ordinary-local analytic sections for projective bundles, or a finite field extension supplying a closed point for a proper factor, followed by checked real-PL and semipositivity descent. Properness and relative smooth openness make the fiber-minimum obstacle continuous. Applying n1 gives continuity and exact raw-envelope compatibility for every scalar extension. The analytic fiber over x is over H(x), not a set of K-points. This does not cover arbitrary higher-dimensional normal spaces or nonprojective projections.",
    "text": "Assume the field and full exact competitor definitions of n1. Let X be its compact strict rig-smooth curve affinoid and let p:Y -> X be either the actual projectivization P_X(V) of an analytic locally free sheaf of positive rank, or the actual analytic product X x_K Q^an with Q a nonempty smooth geometrically connected proper projective K-variety. For every finite continuous obstacle f on Y put g(x)=min_{y in p^{-1}(x)}f(y). The draft conclusion is P_Y(f)=P_X(g) composed with p, finite continuous and equal to its usc regularization, with full families and every analytic scalar extension.\n\nFirst, every finite continuous classically psh function on a connected compact boundaryless space is constant. It attains a maximum; its maximum locus is closed and is open by GRa (arXiv:2506.13548v2, 17 September 2025) Theorem 6.1. Connectedness makes it the whole space. Therefore the full envelope on any connected good strict proper projective analytic space is the constant min f. Singularity does not change this proof, so normality cannot be necessary in the original unrestricted domain class.\n\nFor a full competitor h on Y, its restriction to the ACTUAL fiber over x is a continuous classically psh function on P(V_x)^an or Q_{H(x)}^an. Algebraic geometric connectedness makes the scheme over H(x) connected; its analytification is connected by Berkovich, IHES 78 (1993), Theorem 7.1.1 applied in degree zero to the constant Z/2 sheaf. Properness identifies compact-support and ordinary degree-zero cohomology, and a nontrivial analytic clopen partition would supply more than the two algebraic constant sections. This use of the residue field is legitimate: the fiber maps analytically into Y_{H(x)}, and the classical psh definition permits the analytic extension H(x)/K. The fiber is proper connected and hence h is constant on it. Thus h=a composed with p. Properness makes p a closed surjection with compact fibers; quotient topology makes a continuous.\n\nMembership downstairs is established, not inferred from classical harmonicity. For a projective bundle, ordinary analytic trivializations of V provide local analytic sections x -> [1:0:...:0]. Restricting h along each section gives a as an R-PL semipositive function by GJR (arXiv:2111.05741v3, 7 March 2025) Proposition 7.6. The local definitions make a GLOBAL semipositive R-PL function. For a factor Q without a K-point, a closed point has finite residue extension L/K and gives an L-point of Q_L. Restrict h_L along its section of X_L x Q_L. This gives a pulled back as semipositive R-PL. GJR Corollary 5.12 gives real-PL descent along that finite scalar extension and Proposition 7.6(2') gives semipositivity descent. A K-rational point is not necessary. Conversely every global base semipositive R-PL function pulls back to a full competitor.\n\nThe inequality h<=f is equivalent to a<=g. We have therefore identified the ENTIRE competitor families and proved P_Y(f)=P_X(g) composed with p. This identity works over any compact good separated strict base; only its continuity application uses n1.\n\nThe fiber minimum exists by compactness. For a real c, {x:g(x)>c} is the complement of the closed image p({f<=c}); this proves lower semicontinuity. Also {x:g(x)<c}=p({f<c}) is open, because p is a smooth morphism with no relative boundary and Berkovich, IHES 78 (1993), Corollary 3.7.4 says such a morphism is open. Thus g is finite continuous. Invoke n1 for the full base envelope. Base relative-boundary vertices remain unrestricted in sign; the projective map contributes no relative boundary.\n\nFor every analytic extension F/K and x' over x, the new fiber is the scalar extension Y_x tensor_{H(x)} H(x'). Its projection onto Y_x is surjective, so the minimum of the pulled obstacle is exactly g(x). The fiber-minimum obstacle upstairs is consequently g pulled back. The family identification holds over F, and n1 proves raw-envelope scalar compatibility and continuity. This does not assume openness of arbitrary scalar projections, nor confuse analytic products with products of sets of rational points.\n\nThe complete proof is in P03.3-argument.md, Section 7, and standalone P03.3-paper.tex. Exact checked primary statements and literal pages are retained in source-extracts/source-provenance.json. Rerun with python prepare_sources.py and python verify_deliverable.py. These are unverified sufficient results on genuine proper-projective factors and bundles; they are not a classification of arbitrary normal/geometrically unibranch higher-dimensional geometry.\n\nArtifacts: /workspace/research/campaigns/round-40/P03.3-public-source-general-curve-continuity/artifacts/codex-y7aOMx",
    "support": [
      "n1"
    ]
  },
  {
    "id": "n3",
    "summary": "Fresh actual analytic counterexample on M(K<x,y>/(xy)): a finite continuous obstacle has raw full envelope 0 on the punctured x-branch and -a on the y-branch, with nodal regularization 0 and a resulting discontinuity. Actual projective factors preserve this obstruction. Deliverables and two clean TeX builds are retained; original sharp P03.3 stays open and candidate=false.",
    "detailedSummary": "The obstacle is 0 on the x-disc and -a|y| on the y-disc. The singleton-Shilov maximum principle bounds every competitor by -a on the y-disc. Explicit global real-PL psh functions (a/(nA))log max(|alpha|^n,|x|), with A=-log|alpha|, approach 0 at every punctured x-branch point and equal -a on the y-branch. Rational-domain charts verify actual global membership before semipositivity is invoked. This independently proves the discontinuity without using the input's book claims. n2 transfers it to products with projective space. Sharp higher-dimensional necessity, general branched necessity, imperfect non-rig-smooth normal curves, and noncompact boundary behavior remain unresolved. Both final TeX passes exited 0 without warnings and produced a 10-page PDF; these are administrative observations, not mathematical verification.",
    "text": "Let K be any complete nontrivially valued field, choose alpha with 0<|alpha|<1, put A=-log|alpha|, and fix a>0. On X=M(K<x,y>/(xy)), write D_x and D_y for the two closed branch discs and o for their common rigid origin. Define f=0 on D_x and f=-a|y| on D_y. Both restrictions are continuous and agree at o, so f is a finite continuous obstacle. Its value at the y-Gauss point eta_y is -a.\n\nEvery full competitor restricts to a semipositive real-PL, hence classically psh, function on D_y. GRa, arXiv:2506.13548v2, Theorems 4.3 and 6.4 give the singleton-Shilov maximum principle there: h<=h(eta_y)<=-a on D_y. Since the constant -a is a global minorant, P_X(f)=-a on all of D_y, including o.\n\nDefine q_n=log max(|alpha|^n,|x|) and h_n=(a/(nA))q_n. The global rational-domain cover {|x|<=|alpha|^n}, {|x|>=|alpha|^n} verifies actual PL membership: q_n is respectively the constant n log|alpha| and log|x|, with x an analytic unit on the second domain. Thus h_n is GLOBAL real PL. GRa Proposition 4.2 makes q_n classically psh as max of a constant and log|x|, with the latter allowed to be -infinity where x vanishes; Theorem 4.3 makes h_n semipositive. It equals -a on D_y, is <=0 on D_x, and hence belongs to the FULL exact competitor union below f.\n\nAt every point of D_x except o, |x|>0 and h_n tends to 0. Thus the exact raw envelope is 0 on D_x minus o and -a on D_y. Its usc regularization changes only o to 0. On every other y-branch point it remains -a. The y-rigid points y=alpha^m tend to o, and their regularized values stay -a; this proves an actual discontinuity. This proof uses no unpublished book statement or previous generated note.\n\nBy n2's full-family identification, which works also over this singular compact base, the full raw envelope on X x_K P^r with the pulled obstacle is the pullback of this raw envelope. The projection is smooth and open. For any continuous open surjection p and locally bounded s, the neighborhood definition of limsup gives (s composed with p)^*=s^* composed with p: continuity supplies one inequality and openness of p on each neighborhood supplies the other. Therefore the regularized projective-product envelope is discontinuous as well. Proper factors alone do not remove a branch obstruction.\n\nTogether n1 and n2 prove genuinely broader sufficient geometric sectors, not the original sharp classification. No necessary-and-sufficient theorem is supplied for general good strict analytic domains or higher-dimensional normal/geometrically unibranch spaces. The argument does not realize or globalize arbitrary higher-dimensional semipositive competitors, treat non-rig-smooth normal curves over imperfect fields, classify all branched affinoids, or classify noncompact relative-boundary behavior. The extra pointwise-bijective-normalization sector deliberately does not claim full upstairs envelope equality when normalization splits. The original P03.3 remains open, and candidate is false.\n\nThe full argument is P03.3-argument.md; standalone P03.3-paper.tex embeds it all. input.json and input-original.json are byte-identical; task-original.json preserves the task object and assignment-original.txt preserves the assignment string. status.json has exactly id,status,exact_result,proof_file,concrete_gaps and status partial. Literal selected primary pages/proofs, exact versions, hashes, visual ambiguity checks and checked applications are retained in source-extracts/source-provenance.json.\n\nRerun commands: python prepare_sources.py; python verify_deliverable.py; python package_notes.py. The actual TeX command is pdflatex -interaction=nonstopmode -halt-on-error P03.3-paper.tex, executed twice in the final check. Both passes returned exit code 0, with no warnings in either final log, producing P03.3-paper.pdf, 10 pages and 199384 bytes. checks/deliverable-checks.json, checks/tex-pass-1.log and checks/tex-pass-2.log retain these outputs; checks/environment.json records installed tool versions; checks/source-extraction-diagnostics.json records actual extraction/rendering diagnostics, including harmless Type 3 glyph bounding-box warnings from the old thesis PDF; checks/proof-review.md is a fresh self-review, not an independent verification. All source hashes matched the supplied hashes. No alternate model, subagent, worker, installation, account/runtime change, private campaign material, external message or heavy computation was used. The workspace cannot independently authenticate the requested model route. Source hashes, successful execution, finite administrative checks and TeX builds do not establish mathematical correctness.\n\nArtifacts: /workspace/research/campaigns/round-40/P03.3-public-source-general-curve-continuity/artifacts/codex-y7aOMx",
    "support": [
      "n1",
      "n2"
    ]
  }
]

# Published source versions, provenance and application checks

{
  "sources": [
    {
      "id": "GJR",
      "public_source": "https://arxiv.org/pdf/2111.05741",
      "exact_version": "arXiv:2111.05741v3, 7 March 2025",
      "pdf": "/workspace/research/shared-sources/GJR-2111.05741.pdf",
      "pdf_sha256": "572d51c9f8907dbb814684f7d136612243c0e0b70cddbe6759bb686f0bcfbd42",
      "literal_cache": "/workspace/research/shared-sources/GJR-2111.05741.txt",
      "literal_cache_sha256": "57dfcae1d8dfc25d5ef217f34fabe9e80b679ec2956db1bced3b31bc9afdf8d3",
      "selected_pages": [
        {
          "pdf_first": 30,
          "pdf_last": 36,
          "artifact": "source-extracts/GJR-pdf-pages-30-36.txt"
        },
        {
          "pdf_first": 44,
          "pdf_last": 48,
          "artifact": "source-extracts/GJR-pdf-pages-44-48.txt"
        },
        {
          "pdf_first": 76,
          "pdf_last": 80,
          "artifact": "source-extracts/GJR-pdf-pages-76-80.txt"
        }
      ]
    },
    {
      "id": "GRa",
      "public_source": "https://arxiv.org/pdf/2506.13548v2",
      "exact_version": "arXiv:2506.13548v2, 17 September 2025",
      "pdf": "/workspace/research/shared-sources/GR-2506.13548v2-20261004.pdf",
      "pdf_sha256": "83ca9a19394f44bb2e4e1aa316de95938f311acd53a00fe250fa0f605184b726",
      "literal_cache": "/workspace/research/shared-sources/GR-2506.13548v2-20261004.txt",
      "literal_cache_sha256": "3a221b86116604c950db07e4c60ab184701f0624deebabd92502e5c81871436b",
      "selected_pages": [
        {
          "pdf_first": 7,
          "pdf_last": 14,
          "artifact": "source-extracts/GRa-pdf-pages-7-14.txt"
        },
        {
          "pdf_first": 21,
          "pdf_last": 23,
          "artifact": "source-extracts/GRa-pdf-pages-21-23.txt"
        },
        {
          "pdf_first": 30,
          "pdf_last": 34,
          "artifact": "source-extracts/GRa-pdf-pages-30-34.txt"
        }
      ]
    },
    {
      "id": "GRb",
      "public_source": "https://arxiv.org/pdf/2503.05513",
      "exact_version": "arXiv:2503.05513v1, 7 March 2025",
      "pdf": "/workspace/research/shared-sources/GR-2503.05513-20261004.pdf",
      "pdf_sha256": "2ac2d4bd2016c1692271b1a124013585c903288f5d182081dcdaaf824095eb1b",
      "literal_cache": "/workspace/research/shared-sources/GR-2503.05513-20261004.txt",
      "literal_cache_sha256": "5871a9252fb70f2faf39187e2baf341a42f20412ee66fdc2706b97df90ccba0c",
      "selected_pages": [
        {
          "pdf_first": 1,
          "pdf_last": 3,
          "artifact": "source-extracts/GRb-pdf-pages-1-3.txt"
        },
        {
          "pdf_first": 15,
          "pdf_last": 20,
          "artifact": "source-extracts/GRb-pdf-pages-15-20.txt"
        }
      ]
    },
    {
      "id": "Thu",
      "public_source": "https://theses.hal.science/tel-00010990v1/document",
      "exact_version": "HAL tel-00010990v1, 2005 thesis; PDF page = printed page + 14 in the used chapter",
      "pdf": "/workspace/research/shared-sources/Thuillier-tel-00010990v1.pdf",
      "pdf_sha256": "9c57da951e8dca2676d762e9e8c6ace302675938d72434a5b0390f15af7ea29a",
      "literal_cache": "/workspace/research/shared-sources/Thuillier-tel-00010990v1.txt",
      "literal_cache_sha256": "e82226b3dde6a8088c35e1481bfd43f64bb69ee309b5cfda92c8c927a7885570",
      "selected_pages": [
        {
          "pdf_first": 56,
          "pdf_last": 59,
          "artifact": "source-extracts/Thu-pdf-pages-56-59.txt"
        },
        {
          "pdf_first": 65,
          "pdf_last": 68,
          "artifact": "source-extracts/Thu-pdf-pages-65-68.txt"
        },
        {
          "pdf_first": 75,
          "pdf_last": 78,
          "artifact": "source-extracts/Thu-pdf-pages-75-78.txt"
        },
        {
          "pdf_first": 82,
          "pdf_last": 85,
          "artifact": "source-extracts/Thu-pdf-pages-82-85.txt"
        }
      ]
    },
    {
      "id": "Ber",
      "public_source": "https://www.numdam.org/item/PMIHES_1993__78__5_0/",
      "exact_version": "Publications IHES 78 (1993), Etale cohomology for non-Archimedean analytic spaces",
      "pdf": "/workspace/research/shared-sources/Berkovich-PMIHES-1993-78-5.pdf",
      "pdf_sha256": "bd864c89ed8b6e8f27a90f459837221549db75afa75554ab51414e17771066af",
      "literal_cache": "/workspace/research/shared-sources/Berkovich-PMIHES-1993-78-5.txt",
      "literal_cache_sha256": "694ba4de951bb7e40c73fa4057e4bed5ce073757690ac7379bb1cbbabaf62c1d",
      "selected_pages": [
        {
          "pdf_first": 73,
          "pdf_last": 77,
          "artifact": "source-extracts/Ber-pdf-pages-73-77.txt"
        },
        {
          "pdf_first": 125,
          "pdf_last": 126,
          "artifact": "source-extracts/Ber-pdf-pages-125-126.txt"
        }
      ]
    },
    {
      "id": "CD",
      "public_source": "https://arxiv.org/pdf/1204.6277v2",
      "exact_version": "arXiv:1204.6277v2, 25 July 2025; consulted, not needed by the proof",
      "pdf": "/workspace/research/shared-sources/CD-1204.6277v2-20261004.pdf",
      "pdf_sha256": "5690f999523017d184ab751bb55857ab1637b197d1186ad4fd2edba7e1bda719",
      "literal_cache": "/workspace/research/shared-sources/CD-1204.6277v2-20261004.txt",
      "literal_cache_sha256": "64846cb00926267c6238d1afac61b5eaed0a0e3a6349725738f9b1bf163de085",
      "selected_pages": []
    }
  ],
  "checked_applications": [
    {
      "source": "GJR",
      "statements": "Definition 5.1; Remark 5.2(4,5); Corollary 5.9",
      "hypotheses": "Good strictly analytic spaces; nontrivial valuation; real coefficients.",
      "use": "Local formal Cartier metrics give actual real-PL membership; membership glues in the G-topology and the ordinary topology.",
      "restriction": "Semipositivity does not glue from a G-cover alone; it is checked at ordinary germs by degrees."
    },
    {
      "source": "GJR",
      "statements": "15.1-15.4; Proposition 15.5(1,2); proof of Proposition 15.7",
      "hypotheses": "Compact rig-smooth curve with strictly semistable formal model; legal subdivision vertices in the value group in the dense case.",
      "use": "Legal affine star functions are vertical Cartier metrics. Degree equals weighted outgoing slope sum on a proper reduction component. Relative-boundary reduction components are affine and impose no nef degree sign.",
      "restriction": "No arbitrary irrational subdivision is asserted to be a formal subdivision; no global rational slope commensurability is assumed."
    },
    {
      "source": "GJR",
      "statements": "Proposition 5.11 and its norm proof; Corollaries 5.12,5.13; Proposition 7.7",
      "hypotheses": "Good strict spaces and divisible coefficient group R; finite Galois extensions in our application.",
      "use": "An invariant average of semipositive real-PL functions descends as a semipositive real-PL function.",
      "restriction": "Uses addition and averaging, never a maximum of real-PL functions."
    },
    {
      "source": "GJR",
      "statements": "Proposition 7.6; Definition 7.8",
      "hypotheses": "Good strictly analytic source and target, nontrivial valuation.",
      "use": "Semipositive and harmonic real-PL functions pull back along analytic morphisms and all analytic scalar extensions. LFS is a subclass of semipositive real PL.",
      "restriction": "Only the full union, not a separate LFS-only envelope, is identified."
    },
    {
      "source": "Thu",
      "statements": "Theorem 2.3.8 and its proof; Proposition 3.2.4; Proposition 3.2.7 and proof; Lemma 3.2.8 and proof; Corollary 3.2.9",
      "hypotheses": "Strict rig-smooth affinoid, pure dimension one; finite separable extension for embedding/semistable reduction. Density and representation are applied on an ambient smooth boundaryless projective curve.",
      "use": "After finite extensions, every continuous obstacle is uniformly approximable on the entire affinoid by a finite-skeleton affine obstacle. A Tietze extension puts the obstacle on the ambient projective curve.",
      "restriction": "Thuillier-lisse is not initially declared real PL; formal real-PL membership is separately proved after legal subdivisions."
    },
    {
      "source": "GRa",
      "statements": "Theorem 4.3; Definition 4.1; Proposition 4.2; Theorem 6.1; Lemma 6.2; Theorem 6.5 and proof",
      "hypotheses": "Nontrivial valuation and good strict space for Theorem 4.3; unrestricted analytic scalar extensions and curve morphisms in Definition 4.1.",
      "use": "Every competitor is classically psh. Harmonic comparison bounds the full family. Uniform limits are classically psh. Each affinoid curve component has nonempty relative boundary.",
      "restriction": "Positivity alone is never used to infer continuity."
    },
    {
      "source": "GRa",
      "statements": "2.9; 2.11(5'); Lemma 3.9(1,4,6) and proof",
      "hypotheses": "Analytic scalar extensions; reduced strict curves, perfect field for rig-smooth normalization.",
      "use": "Scalar projections are surjective and closed; extended relative boundary is contained over base relative boundary. Homeomorphic normalization gives a further continuity sector using real-PL descent.",
      "restriction": "No openness of arbitrary scalar projection, and no automatic preservation of homeomorphic normalization under extensions, is asserted."
    },
    {
      "source": "Ber",
      "statements": "Corollary 3.7.4, following Theorem 3.7.2 and Corollary 3.7.3",
      "hypotheses": "Smooth morphisms in Berkovich's sense, including absence of relative boundary.",
      "use": "Actual projective-bundle and smooth proper-projective-factor projections are open. With properness, their fiber minimum of a continuous obstacle is continuous.",
      "restriction": "Does not say that a scalar projection is open."
    },
    {
      "source": "Ber",
      "statements": "Theorem 7.1.1 and its proof",
      "hypotheses": "Compactifiable scheme over a complete non-Archimedean field; abelian torsion sheaf. Our scheme is proper and connected and our sheaf is constant Z/2.",
      "use": "In degree zero properness identifies compact-support with ordinary cohomology. Comparison excludes a nontrivial clopen analytic partition, proving that the actual proper fibers are analytically connected.",
      "restriction": "Used only for connectedness, not for envelope descent or continuity."
    }
  ],
  "pdf_visual_checks": [
    {
      "source": "GJR",
      "pdf_page": 78,
      "resolution": "Read actual PDF image: dense Gamma requires vertices in Sigma(Gamma); Proposition 15.5(2) imposes no boundary sign."
    },
    {
      "source": "Thu",
      "pdf_page": 85,
      "printed_page": 71,
      "resolution": "Read actual PDF image: Corollary 3.2.9 concerns A^0(X), density in C^0(X,R); it does not itself establish semipositivity or formal-model membership."
    }
  ],
  "proof_status": "Unverified mathematical draft; source hashes and execution are not correctness certificates."
}

## GJR PDF pages 30-36

30                              W. GUBLER, P. JELL, AND J. RABINOFF

x ∈ NΓ . Then Sϕ (X ) ∩ X ω is the Shilov boundary of X ω by Remark 3.19. Hence we
may assume x ∈ Sϕ (X ) ∩ X ω as otherwise all tropical multiplicities are zero. Using the
notations of 4.14, we let Ke (C x ) denote the function field of C x . The homomorphism
                                                  ∼
Aω → H (x) induces an isomorphism K     e (C x ) −→ Hf(x) by [Ber90, Proposition 2.4.4(ii)].
                            ◦                                                            e (M
By the definition of Aω ⊂ Aω , the function field of ιs (C x ) is precisely the subfield K  e (x))
of Remark 3.8. We have length(OX ,x ) = 1 because X is reduced, so
                                f(x) : K
                  mϕ (X , x) = [H      e (M
                                          e (x))] = [C x : ι(C x )] = mrel (x)
by Remark 4.2(8).                                                                              
Example 4.16 (Continuation of Example 3.15). We continue with the notation in Exam-
ple 3.15. By [BPR16, Theorem 5.8], for any point P in the interior of an edge e in the
skeleton S, the relative multiplicity mrel (P) is equal to the “expansion factor” of the edge e
with respect to the tropicalization map ϕtrop . In this situation, the expansion factor of
every edge is equal to 1, except for the edge BD, which has expansion factor 0 as it is
crushed to a point.
   We claim that mϕ (X , P) = 1 for P ∈ {A, B, C, D}. This can be checked directly from
the definition of mϕ (X , P). We give the proof in case P = A which reduces to the generic
point of the line x = 0 in the special fiber of Xmin . By [Ber90, Proposition 2.4.4(ii)],
we have H  f(A) = K e ( y). Recall that trop(A) = (1, 0). If M = Z2 be the character lattice
of T = G2m , then Ke ( M(A))
                       e      is the subfield of H f(A) generated by the reductions of x/p
and of y/1 = y. This shows H     f(A) = K e (M
                                             e (A)), and hence 4.2(8) yields that mϕ (X , A) =
[Hf(A) : K
         e (Me (A))] = 1. The proof for the points P = B, C, D is similar.
   We conclude that mrel (P) = mϕ (X , P) = 1 for every point P of Sϕ (X ). It follows that
mϕ (X , ω) just counts the preimages of ω in Sϕ (X ) under ϕtrop ; these tropical multiplicities
are indicated in Figure 1.

                              5. PIECEWISE LINEAR FUNCTIONS
   In this section we discuss piecewise linear functions on analytic spaces. Most of these
results are standard in one form or another: for instance, see [CD12, Gub98, GM19].
However, the terminology in the literature is somewhat nonstandard, so it is important
to fix our ideas. We will find it useful to work slightly more generally with piecewise
linear functions with slopes contained in an additive subgroup Λ ⊂ R, and in some cases
new arguments are needed. In practice we will usually take Λ = Z, Q, or R, in which case
either Λ = Z or Λ is divisible.
   In this section, K is a non-Archimedean field with a non-trivial valuation v and value
group Γ := v(K × ) ⊂ R. We consider a good strictly K-analytic space X and an additive
subgroup Λ ⊂ R. Recall from 2.3 that a strictly analytic space is good provided that that
every point has a strictly affinoid neighbourhood. Most strictly analytic spaces occurring
in practice are good: for example, any strictly affinoid space, a space with no boundary,
or an analytic subdomain of the analytification of an algebraic variety. We restrict our
attention to good spaces as then the coherent modules on the Berkovich space X are
the same as the coherent modules on the space X G endowed with the G-topology [Ber93,
Proposition 1.3.4], which makes it reasonable to work with line bundles on X . We always
               FORMS ON BERKOVICH SPACES BASED ON HARMONIC TROPICALIZATIONS                       31

use the G-topology on X generated by the strictly affinoid domains. Let C(X ) be the space
of continuous real functions on X .
Definition 5.1. A function h: X → R is called piecewise Λ-linear or Λ-PL if there exists a
                                                                                                    ×
G-covering {XP i } of X such that for each i, there are finitely many λi j ∈ Λ and f i j ∈ O (X i )
with h|X i = j λi j log | f i j |. A Z-PL function is called piecewise linear or PL.
  We denote the group of PL functions on X by PL(X ), and the group of Λ-PL functions
by PLΛ (X ). These are subgroups of C(X ).
5.2. Some remarks:
   (1) A function h: X → R is PL if and only if there exists a G-covering {X i } of X and
       f i ∈ O (X i )× such that h|X i = log | f i |.
   (2) The set of Λ-PL functions on X forms a group since any two G-coverings {X i } and
       {X ′j } admit the common refinement {X i ∩ X ′j }.
   (3) The restriction of a Λ-PL function to a strictly analytic domain is Λ-PL.
   (4) The presheaf U 7→ PLΛ (U) is a sheaf in the G-topology, and therefore in the ana-
       lytic topology as well.
   (5) A function h: X → R is Λ-PL if and only if there exists a G-covering {X i } of
       X suchPthat for each i, there are finitely many λi j ∈ Λ and hi j ∈ PL(X i ) with
       h|X i = j λi j hi j .
   (6) A function h: X → R is Q-PL if and only if, locally in the analytic topology, there
       exists a positive integer N such that N h is PL.
   (7) If Λ = Z or Λ = Q then the minimum and maximum of two Λ-PL functions is
       again Λ-PL by [GM19, Proposition 2.12(d)].
Example 5.3. The assertion of 5.2(7) is not true for Λ strictly containing Q. For example,
if the value group of K is Q and X = Gan m
                                            = Spec(K[t ±1])an is the split torus of rank 1, then
the tropicalization of any strictly affinoid domain in X is a union of compact intervals with
rational vertices. We conclude that for Λ = R, the function h := π log |t|+1 = −π trop +1
is Λ-PL, but max(h, 0) is not Λ-PL as max(h, 0) = ϕ ◦ trop for ϕ(u) = max(−πu + 1, 0),
and as the piecewise linear function ϕ has a bend at the irrational number 1/π.
  Here we list some basic functoriality properties of Λ-PL functions.
Lemma 5.4. Let h: X → R be a function.
   (1) Let f : X ′ → X be a morphism of good strictly K-analytic spaces. If h ∈ PLΛ (X ) then
       h ◦ f ∈ PLΛ (X ′ ).
   (2) Let K ′ /K be a non-Archimedean field extension, let X ′ = X ⊗
                                                                    b K K ′ , and let π: X ′ → X
       be the structure morphism. If h ∈ PLΛ (X ) then h ◦ π ∈ PLΛ (X ′ ).
   (3) Let ι : X red → X be the inclusion of the reduction of X , and let h′ = h ◦ ι. Then
       h ∈ PLΛ (X ) if and only if h′ ∈ PLΛ (X red ).
Proof. The first two assertions are obvious. For the third, by (1), the only thing to show is
that if h′ is Λ-PL then h is Λ-PL. Let U = M (A ) ⊂ X be a strictly    Paffinoid domain, and let
                                                           ′                                    ×
Ured = M (Ared ) ⊂ X red be its reduction. Suppose that P h |Ured = λi log |g i | for g i ∈ Ared  .
If f i ∈ A lifts g i then f i ∈ A × is a unit, and h|U = λi log | f i |. Since X red has a G-cover
by such affinoid domains, the same is true for X , so h is Λ-PL.                                 
32                              W. GUBLER, P. JELL, AND J. RABINOFF

   At this point we assume that the reader is familiar with formal geometry as recalled
in 2.4. We give an interpretation of Λ-PL functions in terms of formal geometry which
we will use to prove some more subtle properties of piecewise Λ-linearity. Recall that
a formal K ◦ -model of a paracompact strictly K-analytic space X is an admissible formal
scheme X over K ◦ equipped with an identification Xη = X .

     A frame of a line bundle on an open set is a nowhere vanishing section.

5.5 (Functions from Formal Models of OX ). We assume now that X is paracompact. This
allows us to use Raynaud’s theory of formal K ◦ -models, as in 2.4. We will later apply
this only locally on a good, strictly analytic space, where we can always find a compact
strictly analytic neighbourhood (even a strictly affinoid neighbourhood as X is good).
Hence the reader loses nothing by assuming here and in the following that X is compact.
(Paracompactness has the advantage that one can apply these considerations also to the
analytification of algebraic varieties over K.)
   Let X be a formal K ◦ -model of X . The isomorphism classes of line bundles L on X
equipped with an identification Lη = OX form an abelian group denoted by M (X). Then
L ∈ M (X) determines a canonical metric k kL on OX , defined as follows: if s is a frame of
L over a formal open subset U ⊂ X, then we set ksk = 1 on Uη . This metric is well-defined
because any two frames differ by a unit with constant absolute value 1.
   Equivalently, we get a canonical function hL = − log k1kL : X → R with − log k f kL =
− log | f |+hL for an analytic function f on any open subset U of X . If U = Uη for a formal
open subset U of X and if f ∈ Γ (U, L) ⊂ Γ (Uη , OX ) is a frame of L, then by definition
0 = − log | f | + hL , so hL is PL because X has a G-cover by such U = Uη .

5.6 (PL Functions are Model Functions). If X is paracompact, then [GM19, Proposi-
tion 2.10] yields that h: X → R is PL if and only if there exists a formal K ◦ -model (X, L)
of (X , OX ) such that h = − log k1kL .

5.7 (Λ-PL Functions from Formal Models). For paracompact X , we extend 5.6 to the
case of Λ-PL functions as follows. Choose a formal K ◦ -model X of X , and set M (X)Λ :=
M (X)⊗Z Λ. We have a unique homomorphism h: M (X)Λ −→ C(X ), written        Pm L 7→ hL , such
that hλL =P   −λ log k1kL for all L ∈ M (X) and λ ∈ Λ. Note that if L = i=1 λi Li ∈ M (X)Λ
                m
then hL = i=1 λi hLi ∈ PLΛ (X ) by 5.2(5).
   If f : X′ → X is a morphism of formal K ◦ -models of X , then h f ∗ L = hL for all L ∈ M (X)Λ .
More generally, if f : X′ → X is any morphism of separated admissible formal schemes
then h f ∗ L = hL ◦ fη for all L ∈ M (X)Λ . (See 2.4 for separatedness of formal models.)
   For L ∈ M (X)Λ , we get a unique continuous metric k kL on OX defined by − log k f kL =
− log | f | + hL for an analytic function f on any open subset U of X .

   We want to extend the result of 5.6 locally in the analytic topology to Λ-coefficients as
in 5.7. To do this we need to show that a Λ-PL function is locally in the analytic topology a
linear combination of PL functions with Λ-coefficients. (For our purposes, we could have
taken the statement of Proposition 5.8 as the definition of Λ-PL; we chose Definition 5.1
because it is more compatible with the terminology in the literature.)
                 FORMS ON BERKOVICH SPACES BASED ON HARMONIC TROPICALIZATIONS                             33

Proposition 5.8. Suppose that Λ = Z or that Λ is divisible. A function h: X → R is Λ-
       Pm only if for every x ∈ X , there exists an open neighbourhood U of x such that
PL if and
h|U = i=1 λi hi for finitely many λ1 , . . . , λm ∈ Λ and h1 , . . . , hm ∈ PL(U).
  Before proving the proposition, we state the desired corollary.
Corollary 5.9. Suppose that Λ = Z or that Λ is divisible. A real function h: X → R is Λ-PL
if and only if for every point x ∈ X , there exists a compact strictly analytic neighbourhood
U of x, a formal K ◦ -model U of U, and L ∈ M (U)Λ , such that h|U = hL . In this case, such a
neighbourhood U can be chosen arbitrarily small.
Proof.
     PmSuppose that h is Λ-PL. By Proposition 5.8, after shrinking X , we may assume that
h = i=1 λi hi for λ1 , . . . , λm ∈ Λ and PL functions h1 , . . . , hm : X → R. Since every point of
X has a compact strictly analytic neighbourhood, we may also assume that X is compact.
By 5.6, for each i there is a model (Xi , Li ) of (X , OX ) such that hi = hLi . Finding a model X
                                                                              Pm
dominating
       Pm    all X i , we may   assume  all X i = X. Then  h  =  h  L for L =     λ L . Conversely,
                                                                               i=1 i i P
                                                                                         m
if L = i=1 λi Li on U for λ1 , . . . , λm ∈ Λ and L1 , . . . , Lm ∈ M (U) then hL = i=1 λi hLi is
Λ-PL by 5.2(5). We can choose U sufficiently small because U can be taken arbitrarily
small in Proposition 5.8.                                                                         
  We will use the following lemma in the proof of Proposition 5.8; we will use it again
several times.
Lemma 5.10. Suppose that Λ is a divisible additive subgroup of R. Let P be an abelian
group, and let x 1 , . . . , x r ∈ Λ ⊗Z P be a finite collection of elements. Then P            there is a Q-
                                                                                                   n
linearly independent subset {λ1 , . . . , λn } ⊂ Λ such that each x i has the form j=1 λi ⊗ x i j
for x i j ∈ P.
                       P mi
Proof. Write x i = j=1        λi j ⊗ yi j . Let λ1 , . . . , λn be a basis of the Q-subspace of Λ generated
by the λi j . Since Λ is divisible, we may assume that every λi j is a Z-linear combination of
                                                 P mi
λ1 , . . . , λn . Expanding λi j in the sum j=1            λi j ⊗ yi j and rearranging proves the lemma. 
Proof of Proposition 5.8. The “if” direction is trivial because a covering by open sets is a
G-covering. Suppose then that h is Λ-PL. If Λ = Z then h is itself PL, so we may assume
Λ is divisible. Fix x ∈ X , and replace X by a compact strictly analytic neighbourhood of
x to assume X is compact.PChoose a G-covering {X i }i∈I of X by compact strictly analytic
                              mi
domains such that h|X i = j=1    λi j log | f i j | for finitely many λi j ∈ Λ and f i j ∈ O (X i )× . We
may assume that every X i contains x and that I is a finite set. By Lemma 5.10, there
are Q-linearly
       Pm       independent elements λ1 , . . . , λm ∈ Λ such that for every i ∈ I, we have
h|X i = k=1 λk hik with hik = log |g ik | for g ik ∈ O (X i )× .
  We claim that there is a neighbourhood U of x such that for all i, j ∈ I and all y ∈
U ∩ X i ∩ X j we have
(5.10.1)                         hik ( y) − hik (x) = h jk ( y) − h jk (x).
To prove this, we pick i, j ∈ I, set X i j := X i ∩ X j and consider the smooth tropicalization
map H i j : X i j → R2m given by y 7→ (hik ( y), h jk ( y))k=1,...,m . By 3.2 and 3.3, the tropical
variety of the germ (X i j , x) is the germ at H i j (x) of a finite union of (Z, Γ )-polytopes ∆.
34                                     W. GUBLER, P. JELL, AND J. RABINOFF

Choosing them sufficiently small, we may       S assume every ∆ is contained in H i j (X i j ). It is
enough to show (5.10.1) for y ∈ Ui j := ∆ H i−1         j
                                                          (∆) as Ui j is a neighbourhood of x in X i j ,
hence has the form U ∩ X i j for a neighbourhood U of x in X .
  We fix i, j ∈ I and pick a polytope ∆ as above. Since ∆ is a Z-polytope, the set (H i j (x)+
Q2m ) ∩ ∆ is dense in ∆. By construction, there are coordinate functions ℓik , ℓ jk of R2m
such that hik = ℓik ◦ H i j and h jk = ℓ jk ◦ H i j . Hence it is enough to show (5.10.1) for all
y ∈ X i j with H i j ( y) ∈ ∆ and with ω = H i j ( y) − H i j (x) ∈ Q2m . Using
                        X                X                X                X
                0=         λk hik ( y) −   λk h jk ( y) −     λk hik (x) +     λk h jk (x)
                        k                   k                    k                      k
                        X                                                      
                   =         λk hik ( y) − hik (x) − h jk ( y) + h jk (x)
                         k

and hik ( y) − hik (x) − h jk ( y) + h jk (x) = ℓik (ω) − ℓ jk (ω) ∈ Q, the Q-linear independence
of λ1 , . . . , λm yields (5.10.1) for all such y. This finishes the proof of the claim.
    Let us fix i ∈ I. We deduce from (5.10.1) that there are constants ci jk such that hik =
h jk + ci jk on U ∩ X i j for all j ∈ I and k = 1, . . . , m. Evaluating at a rig-point of U ∩ X i j , we
                    p
see that ci jk ∈ Γ . Replacing h by an integer multiple, we may assume ci jk = −v(γi jk ) ∈ Γ
for some γi jk ∈ K × . We conclude that γi jk g jk is an invertible function on X j . We claim
that there is a unique piecewise linear function hk : U → R that agrees with log |γi jk g jk | =
ci jk +h jk on U ∩X j for every j ∈ I. To see that the functions ci jk +h jk indeed glue, we know
from (5.10.1) that they agree on intersections up to constants and the claim follows as
ci jk + h jk (x) = hik (x) does not depend on j ∈ I. We note that
                     X                        X                  X                      
                         λk h jk (x) = h(x) =    λk hik (x) =       λk h jk (x) + ci jk
                    k                                 k                    k
             P
and hence        k λ k c i jk = 0. For y ∈ U ∩ X j , we deduce that
                             X                    X                    X                X
                 h( y) =         λk h jk ( y) =       λk h jk ( y) +       λk ci jk =       λk hk ( y)
                             k                    k                    k
                   P
and hence h =           λk hk on U. This proves the proposition.                                         
  With these foundations in place, we can use formal models to show that piecewise
Λ-linearity can sometimes be checked after pull-back, at least when Λ is divisible.
Proposition 5.11. Let f : X ′ → X be a finite, flat, surjective morphism of good strictly K-
analytic spaces. Suppose that Λ is divisible. If h: X → R is a function and h′ = h ◦ f , then
h ∈ PLΛ (X ) if and only if h′ ∈ PLΛ (X ′ ).
Proof. By Lemma 5.4(1), we only need to show that if h′ is Λ-PL then so is h. By [Ber93,
Proposition 3.2.7], the map f is open. Let x ∈ X , choosePx ′ ∈ X ′ mapping to x, and
                                                                  m
let U ′ be an open neighbourhood of x ′ such that h′ |U ′ = i=1 λi h′i for λ1 , . . . , λm ∈ Λ
and h′1 , . . . , h′m ∈ PL(U ′ ). Such a neighbourhood exists by Proposition 5.8. By [Ber93,
Lemma 3.1.2, Definition 3.2.5], after shrinking U ′ , the morphism f |U ′ : U ′ →Pf (U ′ ) is
                                                                                        m
finite and flat. Thus we may replace X ′ by U ′ and X by f (U ′ ) to assume h′ = i=1 λi h′i
on X ′ . Shrinking further, we may assume X and X ′ are compact. By 5.6, each PL function
h′i is induced by a line bundle on a formal model of X ′ . Passing to a dominating formal
                FORMS ON BERKOVICH SPACES BASED ON HARMONIC TROPICALIZATIONS                                         35

model, we may assume that there is a formal K ◦ -model X′ of X ′ and L′i ∈ M (X′ ) such
that h′i = hL′i for each i.
   Using Raynaud’s theorem [Bos14, Theorem 8.4.3, Lemma 8.4.4], after passing to an
admissible formal blowup, we can extend f to a morphism f : X′ → X for some for-
mal K ◦ -model X of X . By [BL93b, Theorem 5.2, Corollary 5.3(b)], after passing to
admissible formal blowups of X and X′ , we may assume f : X′ → X is flat and quasi-
finite. By [Tem00, Corollary 4.4] the morphism f : X′s → Xs is proper, so it is finite; by
Nakayama’s lemma, the morphism f : X′ → X is finite. Working locally, we may thus
assume X = Spf(A) and X′ = Spf(A′ ) are formal affines, with X connected. Then A′ is a
finite, flat A-module, which is locally of finite presentation by [Bos14, Theorem 7.3.4],
so it is a locally free A-module of some constant rank n by [Sta21, Lemma 02KB]. Thus
we can define the norm N (L′ ) of a line bundle L′ on X′ as in [EGAII, 6.5]. This is a line
bundle on X and a model of OX⊗n = OX , so we get a homomorphism N : M (X′ ) → M (X).
Tensoring with Λ, we have an induced homomorphism N : M (X′ )Λ → M (X)Λ .
   Now we can transfer the considerations in [BE21, 8.5] to the analytic setting. For
L′ ∈ M (X′ ) and x ∈ X , we claim that
                                                Y         my
(5.11.1)                        k1(x)kN (L′ ) =    k1( y)kL′ ,
                                                                 y7→ x

where m y = dimH (x) (O f −1 (x), y ) is the multiplicity of y in f −1 (x). With this in place, letting
L = N (L′ ), it follows that
                                                  X
                                         hL (x) =     m y hL′ ( y).
                                                             y7→ x

Extending by linearity,
                     Pmthe above      equation holds for L′ ∈ M (X′ )Λ and L = N (L′ ) ∈
                   ′
M (X)Λ . Letting L = i=1 λi Li and L = N (L′ ), we have h′ = hL′ , and for x ∈ X we have
                               ′

                     X                 X                         X
            hL (x) =    m y hL′ ( y) =     m y h ◦ f ( y) = h(x)   m y = n h(x).
                          y7→ x                      y7→ x                                 y7→ x

It follows that h = hn−1 L is Λ-PL.
   It remains to prove (5.11.1). Let x ∈ X , and let y1 , . . . , yr be the points of f −1 (x). Let
R j := O f −1 (x), y j , let F := H (x), and let m j := dim F (R j ) = m y j . We have the decomposi-
                                 Q
tion R := O ( f −1 (x)) =          j R j into local Artinian rings. Working locally on X = Spf(A),
by [Sta21, Lemma 0BUT] we may assume that L′ is trivial over X′ = Spf(A′ ). Choose a
frame s′ for L′ and let γ = 1/s′ ∈ (A′ ⊗K ◦ K)× , so k1kL′ = |γ| on X ′ . The norm s := N (s′ )
is a frame of N (L), and 1/s = NA′ /A(γ) ∈ (A ⊗K ◦ K)× , so
                                  k1(x)kN (L′ ) = |NA′ /A(γ)(x)| = |NR/F (γ)|.
Let K j be the residue field of R j , let γ j be the image of γ in R j , and let γ j be the residue
class in K j . A Jordan–Hölder argument (see [Ser97, 2.1c, p.9]) shows that NR j /F (γ j ) =
NK j /F (γ j )[R j :F ]/[K j :F ] . Since the canonical valuation on H ( y j ) extends the canonical valu-
ation on the complete non-archimedean field F = H (x), we have
                 |γ( y j )|[K j :F ] = |γ j |[K j :F ] = |NK j /F (γ j ))| = |NR j /F (γ j )|[K j :F ]/[R j :F ] .
36                               W. GUBLER, P. JELL, AND J. RABINOFF

Putting all these together, we deduce
                                     Y                    Y                 Y           mj
        k1(x)kN (L′ ) = |NR/F (γ)| =   |NR j /F (γ j )| =   |γ( y j )|m j =   k1( y j )kL′ .
                                        j                   j                j

This proves the claim in (5.11.1) and hence the proposition.                                      
     Proposition 5.11 gives the following variant of Lemma 5.4(2).
Corollary 5.12. Let X be a good strictly K-analytic space, let K ′ be the completion of an
algebraic field extension of K, let X ′ = X ⊗
                                            b K K ′ , and let π: X ′ → X be the structure morphism.
Suppose that Λ is divisible. If h: X → R is a function and h′ = h ◦ π, then h ∈ PLΛ (X ) if and
only if h′ ∈ PLΛ (X ′ ).
Proof. By Lemma 5.4(2), we only need to show that if h′ is Λ-PL then so is h. When K ′
is a finite extension of K then this is a special case of Proposition 5.11. We reduce to this
case as follows.
    Since piecewise Λ-linearity is a local property in the analytic topology, we may assume
that X is compact. Then X ′ is also compact, so by Proposition 5.8 there are finitely many
                                       ′
compact strictly analytic domains UP   i
                                         such that the interiors Vi′ of the Ui′ cover X ′ and such
that hi := h |Ui′ has the form hi = j λi j h′i j for finitely many h′i j ∈ PL(Ui′ ) and λi j ∈ Λ.
        ′      ′                   ′

By [GM19, Propositions 2.7 and 2.10], the functions h′i j extend to PL functions on X ′ .
                                                                           P
We denote the extensions also by h′i j leading to an extension j λi j h′i j of h′i which we
denote also by h′i . By [GM19, Proposition 2.18(b)], there is a finite subextension F /K of
K ′ /K such that for all i, j, there are PL functions hi j on X F := X ⊗KPF whose pull-backs
to X ′ agree with hi j . Then the pull-back of the Λ-PL function hi := j λi j hi j agrees with
h′i on X ′ . As seen at the beginning, it is enough to show that the pull-back of h to X F is
Λ-PL, so we may replace K by F and X by X F . Piecewise Λ-linearity is a local property, so
we show it in a neighbourhood of any y ∈ X . It follows from [Ber90, Proposition 1.3.5,
Corollary 1.3.6] that the structure map p : X ′ → X is open and surjective, and hence the
sets p(Vi′ ) form an open covering of X . For y ∈ X , we choose i such that y ∈ p(Vi′ ). For
all x ′ ∈ Vi′ and x = p(x ′ ), we have h(x) = h′ (x ′ ) = h′i (x ′ ) = hi (x), proving that h is Λ-PL
on the neighbourhood p(Vi′ ) of y.                                                                 
Corollary 5.13. Suppose that Λ is divisible. Let L/K be a (potentially infinite) normal
extension with automorphism group G := Aut(L/K). Let K ′ be the completion of L and let
X ′ := X ⊗
         b K K ′ , with structure morphism π: X ′ → X . Then h 7→ h◦π induces an isomorphism
          ∼
PLΛ (X ) −→ PLΛ (X ′ )G , where PLΛ (X ′ )G is the space of G-invariant Λ-PL functions on X ′ .
Proof. By [Ber90, Proposition 1.3.5, Corollary 1.3.6], we have X = X ′ /G, so the claim
follows from Corollary 5.12.                                                          

                 6. REDUCTION OF GERMS AND RESIDUES OF PL FUNCTIONS
   We will characterize semipositive and harmonic functions in 7 in the language of
Temkin’s theory of reductions of germs [Tem00], using residues of line bundles with
piecewise linear metrics from [CD12, Section 6]. In this section, we recall the theory
following quite closely [CD12, 6.1], and prove then the preliminary results we need.


## GJR PDF pages 44-48

44                                 W. GUBLER, P. JELL, AND J. RABINOFF

ℓ: Pic(red(X , x))Λ → R, and
                                                     X
                                                     r
                                   0 = ℓ(Lh (x)) =          λi ℓ(Lhi (x))
                                                      i=1

is a non-trivial Q-linear combination of λ1 , . . . , λ r which is a contradiction.                     
6.19 (Functoriality of residues). Let f : (X ′ , x ′ ) → (X , x) be a morphism of good strictly
K-analytic germs. For h ∈ PLΛ (X , x), we get h′ = h ◦ f ∈ PLΛ (X ′ , x ′ ). We have an induced
morphism fe : red(X ′ , x ′ ) → red(X , x), and Lh′ (x ′ ) = fe∗ Lh (x) by [CD12, 6.6.7]. A similar
statement holds for extension of scalars.

                          7. SEMIPOSITIVITY AND HARMONIC FUNCTIONS
   In this section, we study positivity conditions on piecewise linear functions. We will
introduce the crucial notion of a harmonic function, on which our theory of differential
forms rests. We consider a good strictly K-analytic space X and an additive subgroup
Λ ⊂ R. We will always assume that Λ = Z or that Λ is divisible.
   We can characterize semipositivity either in terms of formal geometry or residues of
Λ-PL functions, as elaborated in 6. A line bundle L on an admissible formal scheme X
is called nef (resp. numerically trivial) if its restriction to Xs has the same property. In
other words, the line bundle L is nef if the degree of L|C is nonnegative for every closed
integral curve C ⊂ Xs which is proper over K   e .5
   Let X be a formal K ◦ -model of a paracompact good strictly K-analytic space X . Recall
from 5.5 that M (X) denotes the group of models of OX , and that we have defined a
homomorphism h 7→ hL : M (X)Λ → PL(X )Λ . We will also use the residue Lh (x) of h at
x ∈ X from 6.16.
Proposition 7.1. Let h: X → R be a Λ-PL function and x ∈ X . The following are equivalent:
         (1) There exists a paracompact neighbourhood U of x in X , a formal K ◦ -model U of U,
             and a nef (resp. numerically trivial) element L ∈ M (U)Λ , such that h|U = hL .
         (2) The residue Lh (x) ∈ Pic(red(X , x))Λ is nef (resp. numerically trivial).
Proof. The first assertion implies the second by the description of Lh (x) in 6.16. We will
prove the nef case, as the numerically trivial case is identical. The following argument
is similar to [GK19, Proposition 6.5]. Suppose that Lh (x) is nef. By Corollary 5.9, there
exists a compact strictly analytic neighbourhood U of x, a formal K ◦ -model U of U, and an
element L ∈ M (U)Λ , such that h = hL . As in 6.16 we let VU,x be the closure of redU (x) and
we let LU,x be the restriction of L to VU,x . Then (VU,x , LU,x ) is a model of (red(X , x), Lh (x)),
so LU,x is nef by Lemma 6.11. Let W be a compact, strictly analytic neighbourhood of x
contained in the open set red−1 U
                                    (VU,x ). By [BL93a, Lemma 4.4], there exists an admissible
formal blowup f : U′ → U such that W = Wη for a formal open subset W ⊂ U′ . Note that
h|W = h f ∗ L|W . We claim that f ∗ L|W is nef.
     5
    If X is a proper K ◦ -model of a proper variety X over K and L is a line bundle on X with L = L |X
such that the restriction of L to the special fiber of X is nef, then L is a nef line bundle on X by [GM19,
4.8].
              FORMS ON BERKOVICH SPACES BASED ON HARMONIC TROPICALIZATIONS                 45

  By functoriality of reductions, the set-theoretic image of W under f is contained in
VU,x . In particular, if C is any integral, proper subcurve of Ws , then f (C) ⊂ VU,x . Since
C is reduced, the schematic image of C is contained in VU,x , so we have a commutative
square of morphisms of ek-schemes:
                                            C    /W
                                                       s
                                        f              f
                                                  
                                        VU,x     /U
                                                       s

Since LU,x is nef, we have f ∗ LU,x .C ≥ 0 by the projection formula.                       
Definition 7.2. A Λ-PL function h: X → R is called semipositive at a point x ∈ X if it
satisfies the equivalent conditions of Proposition 7.1, and it is harmonic at x if both h
and −h are semipositive at x. We say that h is semipositive if it is semipositive at all
points of X .
   A harmonic function on X is an R-PL function h: X → R which is harmonic at all points
of X . A Λ-PL harmonic function is called Λ-harmonic.
7.3. Some remarks:
   (1) A Λ-PL function h is harmonic at x ∈ X if and only if Lh (x) is numerically trivial.
       Equivalently, there exists a paracompact neighbourhood U of x, a formal K ◦ -
       model U of U, and a numerically trivial element L ∈ M (U)Λ , such that h = hL .
   (2) Semipositivity and harmonicity are insensitive to the group Λ, in the following
       sense: if h ∈ PLΛ (X ), then h is semipositive at a point x if and only if its image in
       PLR (X ) is semipositive at x.
   (3) Semipositivity and harmonicity of h at x is intrinsic to the germ of h in PLΛ (X , x).
       In particular, the semipositive (resp. harmonic) functions on X form a sheaf in
       the analytic topology. (They do not form a sheaf in the G-topology).
   (4) It follows from Proposition 7.1(1) that the locus of all points x ∈ X at which h is
       semipositive (resp. harmonic) is open.
   (5) The set of semipositive functions at a point forms a monoid (resp. a cone if
       Λ = R), and the set of harmonic functions at a point forms a group (resp. an
       R-subspace).
   (6) If h = log | f | for an invertible analytic function f in a neighbourhood of x, then h
       is harmonic at x by Lemma 6.17 (the converse does not hold: see Remark 15.10).
   (7) Harmonic functions generalize smooth functions in the same way that numerical
       equivalence generalizes rational equivalence in algebraic geometry.
Lemma 7.4. Suppose that X is paracompact. Let X be a formal K ◦ -model of X and let L ∈
M (X)Λ . Then hL is semipositive (resp. harmonic) if and only if L is nef (resp. numerically
trivial).
Proof. The harmonic case follows from the semipositive case. If L is nef then hL is semi-
positive by definition. Suppose then that h := hL is semipositive. Let C ⊂ Xs be an
integral, proper closed curve. By surjectivity of redX , there exists a point x ∈ X reducing
to the generic point of C. Then (C, L|C ) is a model of (red(X , x), Lh (x)), so L|C is nef by
Lemma 6.11. In particular, c1 (L).C ≥ 0, so L is nef.                                       
46                               W. GUBLER, P. JELL, AND J. RABINOFF

  Combined with 5.6, we see that a PL function h: X → R on a paracompact space X is
semipositive (resp. harmonic) if and only if there exists a formal K ◦ -model X of X and a
nef (resp. numerically trivial) line bundle L ∈ M (X) such that h = hL = − log k1kL .
  We have the following alternative characterization of harmonic functions. We do not
know if the same characterization holds for semipositive functions.
Proposition 7.5. Let h: X → R be a Λ-PL function and let x ∈ X . Then h is harmonic Pm at x
if and only if there exists a strictly analytic neighbourhood U of x such that h|U = i=1 λi hi
for Z-harmonic functions h1 , . . . , hm on U and λ1 , . . . , λm ∈ Λ.
Proof. The proposition is vacuous when Λ = Z, so assume Λ is divisible. The “if” direc-
tion is trivial. Suppose then thatPmh is harmonic at x. By Proposition 5.8, after shrinking
X , we may assume that h = i=1 λi hi for λ1 , . . . , λm ∈ Λ and h1 , . . . , hm ∈ PL(X ). By
Lemma 5.10, we may assume that   Pm λ1 , . . . , λm are Q-linearly independent. By Lemma 6.18,
the residue Lh (x) is equal to i=1 λi Lhi (x). Let V be a model for red(X , x) in the sense
of 6.2 such that each Lhi (x) is the pullback of a line bundle L V,i on V . Let C ⊂ V be an inte-
                                                                            Pm
gral, proper closed curve. Since Lh (x) is numerically trivial, we have i=1 λi c1 (L V,i (x)).C =
0. But c1 (L V,i (x)).C ∈ Z for each i, so by linear independence, we have c1 (L V,i (x)).C = 0
for each i. Thus L V,i is numerically trivial, so hi is harmonic.                              
     Now we gather some functoriality properties of semipositive and harmonic functions.
Proposition 7.6. Let X be a good strictly K-analytic space and let h ∈ PLΛ (X ).
   Let f : X ′ → X be a morphism of good strictly K-analytic spaces and let h′ = h ◦ f .
     (1) For x ′ ∈ X ′ , let x = f (x ′ ). If h is semipositive at x, then h′ is semipositive at x ′ .
           The converse holds if x ′ ∈ Int(X ′ /X ).
    (1′ ) If h is semipositive, then h′ is semipositive. The converse holds if f is proper and
           surjective.
Let K /K be a non-Archimedean field extension, let X ′ = X ⊗
       ′                                                             b K K ′ , let π: X ′ → X be the
structure morphism, let x ′ ∈ X ′ , let x = π(x ′ ), and let h′ = h ◦ π.
     (2) If h is semipositive at x, then h′ is semipositive at x ′ . The converse holds if we have
           tr.deg(Ke ′H  f(x)/K
                              e ′ ) = tr.deg(Hf(x)/K e ), where K
                                                                e ′H
                                                                   f(x) is the smallest subfield of
           Hf(x ) containing H
                 ′                f(x) and K e.′

    (2 ) The function h is semipositive if and only if h′ is semipositive.
       ′

Let ι : X red → X be the inclusion of the reduction of X and let h′ = h ◦ ι.
     (3) For x ′ ∈ X red , the function h is semipositive at x = ι(x ′ ) if and only if h′ is semipos-
           itive at x ′ .
    (3 ) The function h is semipositive if and only if h′ is semipositive.
       ′

The statements (1)–(3) and (1′ )–(3′ ) hold with “semipositive” replaced by “harmonic.”
Proof. In each case, harmonicity follows easily from semipositivity. In all cases, the func-
tion h′ is Λ-PL by Lemma 5.4.
   We prove first (1). If h is semipositive at x then h′ is semipositive at x ′ by Lemma 6.12
and functoriality of reduction. The converse holds if x ∈ Int(X ′ /X ) by Theorem 6.15
and Lemma 6.12(1), using functoriality of residues 6.19. Assertion (1′ ) follows because
a proper morphism has no boundary.
                 FORMS ON BERKOVICH SPACES BASED ON HARMONIC TROPICALIZATIONS                             47

  To prove (2), let ϕ : PHf(x ′ )/Ke ′ → PHf(x)/Ke be the natural morphism. We have seen in 6.13
that ϕ −1 (red(X , x)) = red(X ′ , x ′ ). The assertions now follow from Lemma 6.12 and
functoriality of residues 6.19. To prove (2′ ), by Corollary 5.9 we may shrink X such that
X is compact with formal model X and such that there is L ∈ M (X)Λ with h = hL . Then
the claim follows from Lemma 6.8(2) and Lemma 7.4.
  The claims (3) and (3′ ) follow from (7.6,1′ ) since X red → X is proper and surjective. 
 The following proposition allows us to pass to Galois extensions when studying har-
monic and semipositive functions.
Proposition 7.7. Suppose that Λ is divisible. Let L/K be a (potentially infinite) normal
extension with automorphism group G := Aut(L/K). Let K ′ be the completion of L and let
X ′ := X ⊗
         b K K ′ , with structure morphism π: X ′ → X . Then h 7→ h ◦ π induces an isomor-
phism from the monoid of semipositive Λ-PL functions on X (resp. the group of Λ-harmonic
functions on X ) to the monoid of G-invariant semipositive Λ-PL functions on X ′ (resp. the
group of G-invariant Λ-harmonic functions on X ′ ).
Proof. This is an immediate consequence of Corollary 5.13 and Proposition 7.6(2′ ).                       
  Our next goal is to approximate locally semipositive metrics by local Fubini–Study
metrics (Proposition 7.10). This will be a crucial ingredient in proving the balancing
condition in Section 9.
  Recall that a line bundle on a scheme Y is called semiample if some positive tensor
power is globally generated. We say that L ∈ Pic(Y )R is ample (resp. semiample) if there
P r ample (resp. semiample) line bundles H1 , . . . , H r and λ1 , . . . , λ r ∈ R≥0 such that L =
are
     λ H ∈ Pic(Y )R . An ample L is semiample and a semiample L is nef.
  j=1 j j

Definition 7.8. Let h: X → R be an R-PL function. We say that h is Fubini–Study at a
point x ∈ X if Lh (x) is semiample. We say that h is locally Fubini–Study or LFS if it is
Fubini–Study at every point of X .
  Clearly if h is Fubini–Study at x then it is semipositive at x.
7.9. It follows from [CD12, Proposition 6.8.2] that h is Fubini–Study at x if and only if
there is an open neighbourhood U of x such that h|U is an R≥0 -linear combination of func-
tions of the form max{− log | f1 |, . . . , − log | f n |} for invertible analytic functions f1 , . . . , f n
on U.
  The following proposition can be seen as a local analogue of the fact that one can
approximate a nef Q-line bundle by ample Q-line bundles on a projective variety.
Proposition 7.10. Let h: X → R be an R-PL function that is semipositive at a point x ∈
Int(X ). Then there exists a strictly analytic neighbourhood U of x and a sequence h1 , h2 , . . .
of R-PL LFS functions on U such that hi → h|U uniformly.
Proof. We may shrink X to assume it is compact. By Corollary 5.9, we may assume that
there exists a formal K ◦ -model X of X and a line bundle L ∈ M (X)R with h = hL , using
the notation of 5.7. Since x is inner, the closure VX,x of redX (x) in Xs is proper (with the
notation of 6.13): see [CD12, Lemma 6.5.1] and [Vil21, Appendix A]. By Chow’s lemma,
48                               W. GUBLER, P. JELL, AND J. RABINOFF

there is a proper birational morphism V → VX,x with V projective over K              e . Let L ′ be an
                                                                                ′
ample line bundle on V . By [CD12, 6.6.5], there is a PL function h on the germ (X , x)
such that (V, L ′ ) is a model of the residue Lh′ (x). Let U be a compact strictly analytic
neighbourhood of x on which h′ is defined. Then there is a formal K ◦ -model U of U and
a line bundle L′ on U with h′ = hL′ . By Lemma 6.14, there is a compact strictly analytic
neighbourhood U ′ of x and a formal K ◦ -model U′ of U ′ such that the closure V ′ := VU′ ,x
of redU′ (x) dominates V . We may assume that U ′ ⊂ U and that this inclusion extends to
a morphism f : U′ → U by using Raynaud’s theorem. Let L ′ |V ′ be the pull-back of L ′ with
respect to V ′ → V . Then L ′ |V ′ and f ∗ (L′ )|V ′ are both models for Lh′ (x). We conclude that
there is a dominating model V ′′ of red(X , x) such that the pull-backs of L ′ |V ′ and f ∗ (L′ )|V ′
to V ′′ agree. Using Lemma 6.14 again and the arguments above, we may assume that
V ′′ = VU′′ ,x for a formal K ◦ -model U′′ of a compact strictly analytic neighbourhood U ′′
of x contained in U ′ such that the inclusion U ′′ ⊂ U ′ extends to a morphism U′′ → U′ .
Moreover, we may assume that U ′′ ⊂ X extends to a morphism U′′ → X. Replacing X by
U′′ and L, L′ by their pull-backs to U′′ , we put ourselves in the following situation:
     (1) The closure V ′ of redX (x) in Xs dominates V .
     (2) There is L ∈ M (X)R and L ∈ Pic(V )R such that h = hL and L|V ′ is the pullback of
         L under V ′ → V , and such that (V, L) is a model of Lh (x).
     (3) There is a line bundle L′ on X and an ample line bundle L ′ on V such that h′ = hL′
         and L′ |V ′ is the pullback of L ′ under V ′ → V .
We recycle notation now and let U := red−1       X
                                                     (V ′ ). By anticontinuity of the reduction map,
the set U is an open neighbourhood of x. For ǫ ∈ Q>0 let Lǫ := L + ǫ L ′ , Lǫ := L + ǫ L′ ,
and hǫ := hLǫ = h + ǫh′ . Then hǫ is an R-PL function on X and Lǫ |V ′ is the pullback of Lǫ
under V ′ → V . Note that hǫ → h uniformly as ǫ → 0. If h is semipositive at x then L is
nef by Lemma 6.11, so Lǫ is ample as a consequence of Kleiman’s theorem, see [Laz04,
Corollary 1.4.10]. It follows that Lǫ |V ′ is semiample. If y ∈ U then redX ( y) ∈ V ′ , so the
closure Y of redX ( y) in Xs is contained in V ′ . Since h = hL and h′ = hL′ on all of X ,
the pair (Y, Lǫ |Y ) is a model of Lhǫ ( y) by the construction in 6.16. Since Lǫ |Y is again
semiample, we see that hǫ is Fubini–Study at y. Thus hǫ is LFS on U.                                 
Remark 7.11. Let X be a proper scheme over K. It is shown in [GM19, Section 5] that
a pointwise limit of semipositive Q-PL metrics is semipositive. We expect the analogous
result to hold in our situation. In particular, we expect the converse of Proposition 7.10
to hold true: namely, if an R-PL function h is a uniform limit of R-PL LFS functions on
a strictly analytic neighbourhood U of an interior point x, then h is semipositive at x.
This would imply that if h and h′ are R-PL functions that are semipositive at x, then so is
max{h, h′ }. Indeed, we can write h = lim hi and h′ = lim h′i for R-PL LFS functions hi , h′i
in a neighbourhood U of x. By 7.9, the functions max{hi , h′i } are R-PL LFS functions on
U, and we have max{h, h′ } = lim max{hi , h′i }.
   Now we relate semipositivity to positive forms and currents. See 2.8 for the definitions
of positivity based on the corresponding notions for Lagerberg forms and Lagerberg cur-
rents introduced in 2.7. The next result serves as a replacement for [CD12, Lemmas 5.2.3
and 5.3.3] where the result is claimed for strongly positive forms; this is not correct, as
explained in [BGJK21a, Example 2.3.6].


## GJR PDF pages 76-80

76                                W. GUBLER, P. JELL, AND J. RABINOFF

suitable non-zero integer m, weQ may assume that h is Z-harmonic and is hence a harmonic
                                         nµ
tropicalization map. Let pµ :      µ∈R R    → Rnµ be the projection to the µ-th factor. It
                                                                S
follows from (14.2.2) that the restriction of pµ∗ (α′µ ) to h′ ( ρ∈R U ρ ) is independent of the
choice of µ. For any µ ∈ R, this shows that the weakly smooth form ω := h∗ (pµ∗ (α′µ)) on
U satisfies π∗ (ω) = ω′ , proving surjectivity and hence the Proposition.                     
  The Galois action on forms respects the differential graded algebra structure on A(X ),
so it induces an action on the Dolbeault cohomology groups H p,q (X ).
Corollary 14.3. We have H p,q (X ) ∼
                                   = H p,q (X ′ )G .
Proof. Since higher cohomology groups of a finite group are torsion [Ser68, Proposi-
tion VII.6], it is clear that W → W G is an exact functor on the category of R-vector spaces
with G-action. We conclude that the fixed point sets of the Dolbeault complex (13.2.1)
for X ′ compute H p,q (X ′ )G , so the claim follows from Proposition 14.2.               
14.4 (Galois Action on Piecewise Smooth Forms). In the same way as 14.1, we can de-
fine the G-action on the sheaf A•,•
                                  ps
                                     of piecewise smooth forms on X . It is clear that
Proposition 14.2 holds also for piecewise smooth forms. By construction, this G-action
is compatible with the G-action on the subsheaf A•,• of weakly smooth forms.
Proposition 14.5. Let X be a good d-dimensional strictly analytic space X over K, let K ′ /K
be a finite Galois extension with Galois group G, and let X ′ be the base change of X to K ′ .
                                       R          R
                    d,d
    (1) For ω ∈ Aps,c   (X ), we have X ′ π∗ (ω) = X ω.
                                                  R              R
    (2) For ω′ ∈ Aps,c
                     d,d
                         (X ′ ) and σ ∈ G, we have X ′ σ∗ (ω′ ) = X ′ ω′ .
Proof. Suppose first that X is compact and that ω is a piecewise smooth preform given
by a PL tropicalization h: X → Rn and a Lagerberg form α ∈ A p,q (h(X )) with h∗ (α) =
ω. Then π∗ (ω) is a piecewise smooth preform on X ′ given by the PL tropicalization
h′ := h ◦ π: X ′ → Rn . Using that h′ (X ′ )d = h(X )d as weighted polytopal complexes by
                                 ′ ∗           ∗ ∗             ∗
Proposition 8.11 andR that (h ) (α) = π (h (α)) = π (ω), it is clear that both integrals in
(1) coincide with h(X ) α. Proposition 11.1 then yields (1) in general.
                          d
   To prove (2), we choose a finite covering (X i′ )i∈I of supp(ω′ ) by compact strictly ana-
lytic domains X i′ such that ω′ |X i′ = h∗i (α′i ) for some α′i ∈ Aps
                                                                   d,d
                                                                       (h(X i′ )) and a piecewise linear
tropicalization hi : X i′ → Rni . Then the compact strictly analytic domains σ−1 (X i′ ) cover
the support of σ∗ (ω′ ), and the restriction of σ∗ (ω′ ) to σ−1 (X i′ ) is given by (σ ◦ hi )∗ (α′i ).
By Proposition 11.1(3), we have
                              Z                        Z          Z
                                               σ∗ (ω) =                α′i =          ω.
                                 σ−1 (X i′ )              hi (X i′ )           X i′

The integrals in (2) can be computed by the inclusion-exclusion formula (11.1.1) as in
the proof of Proposition 11.1, so (2) follows.                                      
                             15. HARMONIC FUNCTIONS ON CURVES
                                                                                  p
   Let K be a non-Archimedean field with nontrivial value group Γ ⊂ R, and let Γ :=
{t ∈ R | ∃k ∈ N>0 such that kt ∈ Γ } be the divisible hull. We will show that our notion
              FORMS ON BERKOVICH SPACES BASED ON HARMONIC TROPICALIZATIONS                77

of harmonic functions introduced in Section 7 agrees in the case of a rig-smooth curve
with the harmonic functions in Thuillier’s thesis [Thu05]. This will be important in the
companion paper [GJR21].
   First, we recall some notions from the theory of graphs and their relationship to the
structure of non-Archimedean analytic curves. For more details, we refer to [GJR21].

15.1 (Metric Graphs with Boundary). We consider a weighted metric graph (Σ, ∂ Σ) with
boundary. This is a finite multigraph with no loop edges endowed with positive edge
lengths assumed to be in Γ . The boundary ∂ Σ is any subset of the vertices of Σ. Every
edge is endowed with the additional datum of a weight w(e) ∈ Z>0 . If we ignore the
boundary, then we get a compact piecewise (Z, Γ )-linear space of dimension at most 1 as
introduced in 2.5. (Note that isolated vertices are allowed.)
   A function h: Σ → R is called harmonic if the restriction
                                                        P         of h to any edge is affine
R-linear, and if for any vertex x of Σ \ ∂ Σ, we have e− =x w(e)de (h) = 0, where e ranges
over all edges with tail vertex x and de (h) is the outgoing slope of h at x in the direction
of e.
   For a subgroup Λ of R containing Γ , we let Σ(Λ) denote the subset of Σ consisting of
all points x such that f (x) ∈ Λ for all (Z, Γ )-linear functionspf on an edge e containing
x. Let U ⊂ Σ be a subgraph with vertices contained in Σ( Γ ). A function h: U → R
is called piecewise (Z, Γ )-linear if there
                                        p is a subdivision of the subgraph U such that the
vertices of the subdivision are in Σ( Γ ) and such that the restriction of h to any edge e
of the subdivision extends to a (Z, Γ )-linear function on the edge of Σ containing e.

15.2 (Skeletons of Curves). Metric graphs with boundary arise in non-Archimedean ge-
ometry as follows. Let X be a compact rig-smooth curve over K, i.e., a compact rig-smooth
strictly analytic space of pure dimension 1. We assume that X has a strictly semistable
model X over the valuation ring K ◦ . This is a formal K ◦ -model of X (see 2.4) whose spe-
cial fiber Xs is geometrically reduced with smooth irreducible components and at most
double points as singularities. This is equivalent to [Thu05, Definition 2.2.8], where
such models are called simplement semi-stable. To such a model is associated a weighted
metric graph with boundary Σ := S(X), called the skeleton of X. There is a canonical
inclusion Σ ,→ X . The vertices of Σ correspond to the irreducible components of Xs and
the edges correspond to the singular points of Xs , so that Σ is the incidence graph of Xs .
The boundary ∂ Σ consists of the vertices of Σ corresponding to non-proper irreducible
components of Xs . If x ∈ Xs is a singular point with corresponding edge e, then the
weight of e is defined to be w(e) = [Ke (x) : K
                                              e ]. There is an étale neighbourhood of x of
the form Spf(K{X , Y }/(X Y − ̟)) for some ̟ ∈ K ◦◦ \ {0}; the length of e is then defined
to be v(̟). There is a canonical deformation retraction map τ: X → S(X).

15.3 (Subdivisions of the Skeleton). Consider
                                      p         a subdivision Σ′ of the skeleton Σ = S(X)
such that all vertices of Σ′ are in Σ( Γ ). Vilsmeier [Vil21, Construction 2.6] has de-
fined a canonical formal scheme X′ with generic fiber X and reduced special fiber, and a
canonical morphism ι : X′ → X extending IdX , such that for any edge e′ of Σ′ , the analytic
subdomain (τ)−1(e′ ) of X is the generic fiber of an open subset of X′ . Note that X′ is not
necessarily an admissible formal scheme, i.e. not necessarily of topologically finite type.
78                             W. GUBLER, P. JELL, AND J. RABINOFF

By [Gub13b, Propositions 6.7 and 6.9], the formal scheme X′ is admissible if the value
group Γ is discrete or if the vertices of Σ′ are contained in Σ(Γ ).
15.4 (Piecewise Affine Functions on the Skeleton).
                                             p         Let Σ = S(X) as in 15.2, let U be a
subgraph of Σ with vertices contained in Σ( Γ ), and let h: U → R be a piecewise (Z, Γ )-
linear function in the sense of 15.1. Passing to a subdivision of U, we may assume that
h is (Z, Γ )-linear on each edge of U. The vertices of U induce a subdivision Σ′ of Σ; we
denote the associated formal K ◦ -model of X by X′ as in 15.3, with canonical morphism
ι : X′ → X. When Γ dense in R, we assume that all vertices of U are in Σ(Γ ); then
X′ is an admissible formal scheme. The subset Y := τ−1 (U) is the generic fiber of a
unique open formal subscheme Y′ in X′ . By the arguments used in the proof of [Vil21,
Proposition 2.11], there is a canonical vertical Cartier divisor D on Y′ with associated
formal metric on OY determined by − log k1kO (D) = h ◦ τ. See 5.5.
Proposition 15.5. Let X be a compact rig-smooth curve over K and let h: X → R.
     (1) If X is a strictly semistable model of X over K ◦ , then h = hL for a line bundle
         L ∈ M (X) if and only if there is a function f : S(X) → R which is (Z, Γ )-linear on
         each edge such that h = f ◦ τ.
     (2) If x ∈ ∂ X , then h is harmonic at x if and only if h is R-PL at x.
Proof. The “if” part in (1) follows from 15.4. Conversely, assume that h = hL for L ∈
M (X). Using the identification L|X = OX , the meromorphic section 1 of L induces a
vertical Cartier divisor D on X. There is a covering of X by open subsets U such that S(U)
is either an edge or a vertex of S(X) and such that D|U = div(γ) for some γ ∈ O (U)×,
where U = Uη . It follows from [Ber99, Theorem 5.3 and Step 13 in its proof] that
h|U = − log |γ| factorizes through a (Z, Γ )-linear function on S(U). This proves (1).
   Since x ∈ ∂ X , the curve ∂ X is affine and hence the nef condition in Proposition 7.1 is
vacuous. This proves (2).                                                                 
15.6 (Thuillier’s Harmonic Functions). We consider now an arbitrary rig-smooth curve
X over K. We call a function h: X → R harmonic in the sense of Thuillier if every x ∈ X
has a strictly affinoid neighbourhood V , a finite Galois extension K ′ /K, and a strictly
semistable model V′ of V ′ := V ⊗K K ′ , such that the pullback h′ of h|V factorizes through
the skeleton S(V′ ) and such that h′ |S(V′ ) is a harmonic function on the skeleton S(V′ )
considered as a weighted metric graph with boundary as in 15.2.
   For x ∈ ∂ X , Proposition 15.5 and Corollary 5.12 show that the above harmonicity
condition at x is equivalent to piecewise R-linearity at x, using that the boundary of
S(X) is ∂ X . Note that Thuillier [Thu05, Section 2.3] used this definition only for strictly
affinoid or boundaryfree X , so the above definition is slightly more general than his.
Proposition 15.7. Let X be a rig-smooth curve. Then a function h: X → R is harmonic in
the sense of Definition 7.2 if and only if h is harmonic in the sense of Thuillier.
Proof. The claim is local on X , so we may assume X strictly affinoid. We first show
that the harmonicity notions agree for a piecewise linear function h ∈ PL(X ). By 5.6,
we have that h = − log k1kL for a model L of OX on a formal K ◦ -model X of X . Using
base change, Proposition 7.6 and [Thu05, Remarque 2.3.17], we are free to pass to a
              FORMS ON BERKOVICH SPACES BASED ON HARMONIC TROPICALIZATIONS                79

finite Galois extension of K. Arguing locally, the semistable reduction theorem ([Thu05,
Théorème 2.3.8] under these hypotheses; see also [BL85, Section 7] and [Duc24, Theo-
rem 5.1.14(iv), 6.1.3]) shows that we may assume that X is a strictly semistable model.
By Proposition 15.5, there is a function f on the skeleton S(X) which is (Z, Γ )-linear on
each edge such that h = f ◦ τ. For x ∈ S(X) \ ∂ X with corresponding proper irreducible
component C := redX (x) of Xs , it follows as in [KRZB16, Theorem 2.6] that the sum of
outgoing slopes of f at x is equal to deg(L|C ). We conclude that h is harmonic in the
sense of Thuillier if and only if L is numerically equivalent to 0. The latter is equivalent
to harmonicity of h in the sense of Definition 7.2, as we have shown in Lemma 7.4.
   Now we prove the proposition for any function h: X → R. Assume that h is a harmonic
function on X as in Definition 7.2. By Proposition 7.5, the function h is locally an R-linear
combination of Z-harmonic functions, so we are reduced to the case handled above since
the set of Thuillier-harmonic functions forms a real vector space.
   Conversely, let h be a harmonic function in the sense of Thuillier. We have to check
for any x ∈ X that h is harmonic at x. As above, we are free to pass to a finite Galois
extension of X , so we may extend scalars and shrink X to assume that X has a strictly
semistable model X and that h factorizes through a harmonic function f : S(X) → R. It
is enough to show that f is an R-linear combination of piecewise (Z, Γ )-linear harmonic
functions f i on S(X). Indeed, by Proposition 15.5, we have that f i ◦ τ is piecewise linear,
so f i ◦ τ is harmonic by the the first paragraph of this proof, and hence h is harmonic.
   Suppose first that x ∈ ∂ X = ∂ S(X). After shrinking X, we may assume that S(X)
is a star around the vertex x, so that f is affine R-linear on each edge. Translating by
a constant function, we may assume f (x) = 0. Then f is an R-linear combination of
piecewise Z-linear functions f e on S(X): namely, the functions f e that have slope 1 on a
given edge e and slope 0 on the others. Since x ∈ ∂ S(X), Proposition 15.5 yields that
each f e is harmonic and hence h is harmonic.
   If x ∈ X \ ∂ X , then as above, we may assume that S(X) is either an edge containing
τ(x) in its interior, or that S(X) is a star around the vertex τ(x). In the first case, f is
an R-multiple of a (Z, Γ )-linear function on the edge, so h is harmonic. In the second
case, we may assume that f (τ(x)) = 0. Then f is harmonic if and only if f is linear on
each edge and the weighted sum of the outgoing slopes at τ(x) is zero. This is a linear
equation for the slopes which is defined over Q, so there is a basis of solutions defined
over Q and even over Z. The elements f i of such a basis induce piecewise (Z, Γ )-linear
functions f i which are harmonic on S(X). Since f is an R-linear combination of the f i ,
we have that h is harmonic.                                                                

   Note that Γ is either dense inpR or is a discrete subgroup. In the following, we set
Λ := Γ if Γ is dense and Λ := Γ (the divisible hull in R) if Γ is discrete. When Γ is
discrete, we may rescale the valuation to assume Γ = Z.

15.8. Let X be a compact rig-smooth curve over K with strictly semistable model X. As
in 15.2, the skeleton S(X) is viewed as a weighted metric graph with boundary. Let U
be a subgraph of Σ := S(X) with vertices contained in Σ(Λ), then τ−1 (U) is a compact
strictly analytic domain in X .
80                              W. GUBLER, P. JELL, AND J. RABINOFF

Proposition 15.9. With the notation above, let f : U → R be a piecewise (Z, Γ )-linear
harmonic function as in 15.1. Then h := f ◦ τ: τ−1 (U) → R is Z-harmonic.
Proof. Replacing U be a subdivision, we may assume that f is affine (Z, Γ )-linear on each
edge. The vertices of U induce a subdivison of S(X) and hence 15.3 yields a canonical
formal K ◦ -model X′ of X over X. By 15.4, we get a canonical open formal subscheme Y′ of
X′ with generic fiber Y = τ−1 (U). It follows from 5.6 and 15.4 that h is piecewise linear,
so by definition, it is Z-harmonic if and only if it is harmonic. After a finite, separable
extension of the ground field, the graph U becomes a skeleton of Y with respect to some
strictly semistable model (see Remark 5.3.6 in [GJR21]). Thus h is harmonic in the sense
of Thuillier, so by Proposition 15.7, it is harmonic in the sense of Definition 7.2.     
Remark 15.10. Let X be a smooth curve (that is, a rig-smooth curve without boundary),
let H be the sheaf of harmonic functions on X , and let F be the subsheaf of R-vector
spaces generated by the germs log | f | for local invertible analytic functions f . Then Thuil-
lier [Thu05, 2.3.4] has shown that F might be a strict subsheaf of H , with equality when
X is potentially locally isomorphic to P1,an or when K e is algebraic over a finite field. It was
shown in [Wan16, 5.2, 5.3] that F is the kernel of d′ d′′ : A0,0 sm
                                                                    → A1,1
                                                                         sm
                                                                             and that F is the
sheaf of smooth harmonic functions on X . The latter follows also by Proposition 10.17.
We conclude that there is a non-smooth harmonic function on an open subset of X if and
only if the inclusion F ⊂ H is strict. If F = H , then every harmonic tropicalization
map is a smooth tropicalization map, and Asm = A.
  Wanner’s regularization theorem [Wan19, Corollary 5.4], obtained for Mumford curves
or in case of an algebraic residue field over a finite field, can now be generalized as fol-
lows (compare Remark 15.10).
Proposition 15.11. Let X be a smooth curve (a rig-smooth curve without boundary) over
a non-trivially valued non-Archimedean field K, and let f be a subharmonic function on X
as defined in [Thu05, 3.1.2]. Then for any relatively compact open subset U of X , there is
a decreasing net of weakly smooth psh functions f i on U converging pointwise to f |U .
Proof. By Thuillier’s regularization theorem [Thu05, Théorème 3.4.2], there is a decreas-
ing net of piecewise R-linear subharmonic functions on U converging pointwise to f , so
we may assume that f is piecewise R-linear. (Note that piecewise R-linear functions are
called lisse in [Thu05, Definition 3.2.1].) As in the proof of [Thu05, Theorem 3.4.2],
we may assume that U = Y \ ∂ Y for a compact strictly analytic domain Y of X . By
[Thu05, Proposition 3.2.4], there is a finite Galois extension K ′ /K such that Y has a
strictly semistable model Y over the valuation ring of K ′ and such that f = F ◦ τ for a
piecewise R-linear function F on the skeleton S(Y), where τ: Y → S(Y) is the retraction.
Since the subharmonic functions over K are the Galois-invariant subharmonic functions
over K ′ and the same holds for weakly smooth functions, it is enough to prove the claim
over K ′ , so we may assume K = K ′ .
   Now we can follow Wanner’s arguments [Wan19, Lemma 5.2]. Note that the curvature
ddc ( f |U ) is a discrete measure on U; we denote by S its support. In what follows, we
allow subdivisions of Σ := S(Y) at arbitrary points in Σ (not just type-II points); we do
not claim that the subdivision is the skeleton of a formal model of U. By subdividing the


## GRa PDF pages 7-14

             CLASSICALLY PSH AND PLURIHARMONIC FUNCTIONS ON BERKOVICH SPACES                 7

   For any k-analytic space X and r ∈ R>0n
                                             , the structure map πkr /k : X kr → X has a canon-
ical section σ : X → X r mapping x ∈ X to the unique Shilov boundary point of the fiber
π−1
  k r /k
         (x) = M (H (x)⊗b k r ) = M (H (x) r ) (which is the weighted Gauss point η r ). We
call σ the Shilov section. The Shilov section is continuous: see [Ber90, Lemma 3.2.2(i)],
[Duc18, 1.2.16].

2.11. Relative boundary. An important notion in this paper is that of the relative bound-
ary of a morphism ϕ : X → Y of k-analytic spaces. This is a closed subset of X which we
denote by ∂ (X /Y ). We will not give the details of this definition, but let us try to explain
the literature on the subject. In [Ber90, §2.5], Berkovich defines the relative boundary
∂ (X /Y ) for k-affinoid spaces X and Y . Then in [Ber90, §3.1], he generalizes ∂ (X /Y ) for
good k-analytic spaces using that all points of X and Y have k-affinoid neighborhoods.
Berkovich calls ϕ closed if ∂ (X /Y ) = ;. Berkovich defines ∂ (X /Y ) for arbitrary k-analytic
spaces in [Ber93, 1.5.3(ii)], as follows. A morphism ϕ is closed if for every morphism
Y ′ → Y from a good k-analytic space Y ′ , the fiber product X ′ := X ×Y Y ′ is good and the
canonical morphism X ′ → Y ′ is closed in the previous sense. Finally in [Ber93, Defini-
tion 1.5.4], a point x ∈ X is defined to be in Int(X /Y ) if x has an open neighborhood U
such that ϕ induces a closed morphism U → Y in the above sense. We refer to [Tem15,
Definition 4.2.4.1] for a more explicit equivalent definition of ∂ (X /Y ). Note that in this
paper, we will use the notion closed map in the usual topological sense meaning that it
maps closed sets to closed sets. This is different from Berkovich’s terminology.
   The complement Int(X /Y ) := X \ ∂ (X /Y ) is called the relative interior. We will usually
apply this in the case Y = M (k), in which case we call ∂ X := ∂ (X /M (k)) the boundary
of X and Int(X ) := X \ ∂ X the interior. If ∂ X = ;, we say that X boundaryless. A bound-
aryless space is good by definition. Note that Berkovich calls boundaryless k-analytic
spaces closed.
   We list here some properties of the boundary and interior which we will use throughout
the paper:
   (1) A point x ∈ X is contained in Int(X /Y ) if and only if there is an open neighbor-
       hood U of x such that Int(U/Y ) = U: this is part of the above definition.
   (2) If ϕ : X → Y is finite, then Int(X /Y ) = X [Ber93, Example 1.5.3(iii)].
   (3) If X is an analytic domain in Y , then Int(X /Y ) is the topological interior of X in
       Y [Ber93, Proposition 1.5.5(i)].
             ϕ     ψ
   (4) If X → Y → S are morphisms of k-analytic spaces, then

(2.11.1)                   Int(X /Y ) ∩ ϕ −1 Int(Y /S) ⊂ Int(X /S)

        [Ber93, Proposition 1.5.5(ii)], with equality if ψ is locally separated [Tem04,
        Corollary 5.7]. Taking S = M (k), this becomes

(2.11.2)                      Int(X /Y ) ∩ ϕ −1 Int(Y ) ⊂ Int(X ).

   (5) If k′ /k is an analytic extension field, then

                                π−1
                                 k′ /k
                                       Int(X /Y ) ⊂ Int(X k′ /Yk′ )
8                                      W. GUBLER AND J. RABINOFF

         [Ber93, Proposition 1.5.5(iii)]. Taking Y = M (k), this becomes
                                       π−1
                                        k′ /k
                                              Int(X ) ⊂ Int(X k′ ).
For convenience, we restate these properties in terms of the relative boundary:
   (1′ ) A point x ∈ X is contained in ∂ (X /Y ) if and only if ∂ (U/Y ) ̸= ; for every open
         neighborhood U of x.
   (2′ ) If ϕ is finite, then ∂ (X /Y ) = ;.
   (3′ ) If X is an analytic domain in Y , then ∂ (X /Y ) is the topological boundary of X
         in Y .
               ϕ     ψ
     ′
   (4 ) If X → Y → S are morphisms of k-analytic spaces, then
(2.11.3)                        ∂ (X /S) ⊂ ∂ (X /Y ) ∪ ϕ −1 (∂ (Y /S)),
         with equality if ψ is locally separated. Taking S = M (k), this becomes
(2.11.4)                             ∂ X ⊂ ∂ (X /Y ) ∪ ϕ −1 (∂ Y ).
    (5′ ) If k′ /k is an analytic extension field, then
                                     ∂ (X k′ /Yk′ ) ⊂ π−1
                                                       k′ /k
                                                             ∂ (X /Y ).
         Taking Y = M (k), this becomes
                                           ∂ X k′ ⊂ π−1
                                                     k′ /k
                                                           ∂ X.
We will need the following lemma, which is a consequence of deep results in [CT21] in
general, although it has an elementary proof for good spaces.
Lemma 2.12. If X is a k-analytic space and k′ /k is an analytic field extension, then
                                          πk′ /k (∂ X k′ ) = ∂ X .
Proof. We have πk′ /k (∂ X k′ ) ⊂ ∂ X by 2.11(5′ ). Let x ∈ ∂ X , and let U ⊂ X be a compact
neighborhood of x. We claim that x ∈ ∂ U. If not, then there is an open neighborhood
V of x in U such that ∂ V = ; by 2.11(1′ ). If V ′ ⊂ V is a smaller open neighborhood of
x in X , then ∂ V ′ = ; as well by 2.11(3′ ) and by (2.11.4) as applied to V ′ → V → M (k).
Thus we may assume that V is open in X , which implies by 2.11(1) that x ∈ Int(X ), a
contradiction. Hence x ∈ ∂ U. If x ′ ∈ π−1      k′ /k
                                                      (x), then x ′ ∈ ∂ Uk′ if and only if x ′ ∈ ∂ X k′
for the same reason. We need to show π−1        k′ /k
                                                      (x) ∩ ∂ X k′ ̸= ;, so we may replace X by U to
assume that X is compact. In this case, the closed subset ∂ X k′ is compact; suppose that
it is disjoint from π−1
                      k′ /k
                            (x). Then πk′ /k (∂ X k′ ) is a closed subset of X not containing x, so
there exists an open neighborhood V of x such that Vk′ = π−1            k′ /k
                                                                              (V ) ⊂ Int(X k′ ). This means
that ∂ Vk′ = ; by 2.11(3,4). But x ∈ ∂ V , and boundarylessness can be checked after
extension of scalars by [CT21, Theorem 11.5]. This contradiction proves the claim. □
2.13. A k-analytic space X is called rig-smooth at x ∈ X if it is flat (in the sense of
[Duc18]) and if the sheaf of Kähler differentials ΩX (considered on the G-topology) is
free at x of rank equal to the dimension of X at y. We call X smooth if it is rig-smooth
and boundaryless. We refer to [Duc18, Chapter 5] for a discussion (note that rig-smooth
is called quasi-smooth there) and comparison to other definitions.
             CLASSICALLY PSH AND PLURIHARMONIC FUNCTIONS ON BERKOVICH SPACES                9

2.14. Models and formal geometry. A quasi-compact admissible formal scheme over
k◦ is a quasi-compact formal scheme X over k◦ with an open covering by affine formal
schemes Spf(A) for k◦ -algebras A which are topologically of finite type and flat over k◦ .
The generic fiber Xη of X is the strictly k-analytic space obtained by gluing the Berkovich
spectra M (A ⊗k◦ k), and the special fiber Xs is the scheme over ek obtained by gluing the
affine schemes Spec(A ⊗k◦ ek).

Definition 2.15. A formal k◦ -model X for a quasi-compact strictly k-analytic space X is a
quasi-compact admissible formal scheme X over k◦ with an identification Xη = X .

   In the above setting, there is a canonical reduction map redX : X → Xs which is surjec-
tive and anticontinuous [GRW16, Section 2]. We call x ∈ X a divisorial point associated
to the model X if redX (x) is a generic point of the special fiber Xs . Note that the set of
divisorial points is finite: see [GM19, Appendix A]. In ibid, the valuation on k is assumed
to be non-trivial, but this finiteness also holds in the trivially valued case as then Xη is
just the analytification of the special fiber and the generic points of the special fiber have
a unique preimage under the reduction.

2.16. PL functions. We will assume k is non-trivially valued when we discuss PL func-
tions. Let Λ be a subgroup of R which is either divisible or equal to Z. We consider a
good, strictly k-analytic space PX . A function h: X → R is called Λ-piecewise linear or
Λ-PL if G-locally we have h = j λ j log | f j | for finitely many λ j ∈ Λ and invertible ana-
lytic functions f j . Here we use the G-topology of X generated by the strictly k-analytic
domains. We refer to [GJR21, Section 5] for more on Λ-PL functions.

2.17. Reduction of germs. For a good, strictly k-analytic space X over a non-trivially
valued field, Temkin [Tem00] introduced the reduction of the germ (X , x) at x ∈ X as
an open subset of a Zariski–Riemann space PHf(x)/ek of H    f(x)/ek. Roughly speaking, it
is the projective limit of all canonical reductions Spec(A  f) where M (A ) ranges over
all k-affinoid neighborhoods of x. The germ (X , x) is naturally a quasicompact locally
ringed space. See also [CD12, Section 6.1] for an excellent summary. An R-PL function
h: X → R induces a residue line bundle L(h) ∈ Pic(X , x)R . This was introduced in [CD12],
and is explained in [GJR21, Section 6]. We call h semipositive at x if L(h) is nef in the
sense of [GJR21, Section 7]. A semipositive R-PL function is semipositive at all x ∈ X .

2.18. Graded reduction. While the reduction in 2.17 works well for (good) strictly k-
analytic spaces, this concept does not fit very well for non-strictly k-analytic spaces or
in the trivially valued case. To handle the general case, Temkin introduced [Tem04] the
graded reduction of the germ (X , x). We need it only for Lemma 6.3, so we introduce
here only the graded reduction of a k-algebra A endowed with a multiplicative seminorm
ρ. In our applications, the algebra A will be either a k-affinoid algebra endowed with
| |sup or the completed residue field H (x) in a point x of a k-analytic space endowed
with its canonical absolute value. For r ∈ R>0 , we set
               A≤r := {a ∈ A | ρ(a) ≤ r}    and    A<r := {a ∈ A | ρ(a) < r}.
10                                W. GUBLER AND J. RABINOFF

Then the graded residue field of A is given by
                                           M
                                    e• :=
                                    A          A≤r /A<r .
                                           r∈R>0

We refer to [Tem04] for properties of this functorial construction.

                   3. SUBHARMONIC FUNCTIONS ON ANALYTIC CURVES
  In this section, we generalize Thuillier’s theory [Thu05] of subharmonic functions from
smooth strictly analytic curves to arbitrary k-analytic curves.
3.1 (k-Analytic Curves). By a k-analytic curve we mean a separated k-analytic space of
pure dimension 1. We gather the following facts about k-analytic curves:
   (1) A k-analytic curve is good, i.e., every point has an affinoid neighborhood. [Duc24,
        Proposition 3.3.7]
   (2) A k-analytic curve is paracompact. [Duc24, Théorème 4.5.10]
   (3) If X is an affinoid k-analytic curve, then ∂ X coincides with the Shilov boundary
        of X . [Thu05, 2.1.2]
An analytic domain in a k-analytic curve (for example, an open subset) is again a k-
analytic curve.
3.2 (Thuillier’s Harmonic Functions). Thuillier [Thu05, §2.3] defines a sheaf of harmonic
functions on a smooth, strictly k-analytic curve for a non-trivially valued k, roughly as
follows. If X is affinoid, then a continuous function h: X → R is harmonic if, after passing
to a finite, separable field extension, it coincides with the composition of a harmonic
function on a skeleton of X (in the sense of graph theory) with the retraction to the
skeleton. If X is smooth, then a harmonic function on an open subset of X is defined to be
a continuous function whose restriction to every strictly affinoid subdomain is harmonic.
3.3 (Thuillier’s Subharmonic Functions). For a non-trivally valued k, Thuillier [Thu05,
Définition 3.1.5] defines a subharmonic function on a smooth, strictly k-analytic curve X
to be an upper semicontinuous function u: X → R ∪ {−∞} that is not identically −∞
on any connected component of X and that satisfies the following property: for every
strictly k-affinoid domain U ⊂ X and every harmonic function h: U → R, if u ≤ h on ∂ U
then u ≤ h on U.
  Now we extend this definition to the case of non-smooth curves. The idea is that a
function should be subharmonic if it pulls back to a subharmonic function along any
morphism from a smooth curve. However, an inseparable curve over an imperfect field
does not admit any non-constant morphisms from a smooth curve, so one has to allow
an extension of scalars as well. We also consider the constant function −∞ to be sub-
harmonic, following Demailly [Dem85] in the complex case.
Definition 3.4 (Subharmonic functions). Let X be a k-analytic curve and let u: X →
R ∪ {−∞} be an upper semicontinuous function. We say that u is subharmonic provided
that, for every non-trivially valued analytic extension field k′ /k, every smooth, connected,
strictly k′ -analytic curve Y , and every morphism Y → X k′ , the composition
                                        πk′ /k     u
                              Y −→ X k′ −→ X −→ R ∪ {−∞}
             CLASSICALLY PSH AND PLURIHARMONIC FUNCTIONS ON BERKOVICH SPACES              11

is either subharmonic on Y in the sense of [Thu05, Définition 3.1.5], or is identically −∞.
3.4.1. If X is a smooth, connected, strictly k-analytic curve over a non-trivially valued k,
then an upper semicontinuous function u: X → R ∪ {−∞} is subharmonic in our sense
if and only if it is either subharmonic in Thuillier’s sense or is identically −∞. Indeed, if
u is subharmonic in our sense then one can take k = k′ and Y = X to see that it is either
subharmonic in Thuillier’s sense or is identically −∞. Conversely, if u is identically −∞
then it is clearly subharmonic in our sense, and if u is subharmonic in Thuillier’s sense
then it is subharmonic in our sense by [Thu05, Proposition 3.1.14 and Corollaire 3.4.5].
3.4.2. As a special case of (3.4.1), if X is a smooth, connected, strictly k-analytic curve
over a non-trivially valued k, then a function u: X → R (taking finite values) is subhar-
monic in our sense if and only if it is subharmonic in Thuillier’s sense.
  Here we collect the basic properties of subharmonic functions, which we will prove
over the course of this section.
Proposition 3.5. Let X be a k-analytic curve and let u: X → R ∪ {−∞} be an upper
semicontinuous function.
   (1) (Sheafiness) The subharmonic functions form a sheaf on X .
   (2) (Analytic functions) If f ∈ Γ (X , OX ) then log | f | : X → R ∪ {−∞} is subharmonic.
   (3) (Boundaries) If u is subharmonic on Int(X ), then u is subharmonic on X .
   (4) (Cone Property) If u1 , u2 : X → R ∪ {−∞} are subharmonic and λ1 , λ2 ∈ R≥0 then
       λ1 u1 + λ2 u2 and max{u1 , u2 } are subharmonic.
   (5) (Limits) The infimum of a decreasing net of subharmonic functions is subharmonic.
   (6) (Maximum Principle) If u is subharmonic and u attains a local maximum at x ∈
       Int(X ), then u is constant in a neighborhood of x.
   (7) (Extension of scalars) Let k′ /k be an analytic extension field. Then u is subharmonic
       if and only if u ◦ πk′ /k : X k′ → R ∪ {∞} is subharmonic.
   (8) (Functoriality) Let Y be a k-analytic curve and let f : Y → X be a morphism. If u
       is subharmonic then u ◦ f is subharmonic, and the converse holds if f is finite and
       surjective.
   (9) (Finite Values) If u is subharmonic and u(x) = −∞ for a non-rig-point x ∈ X ,
       then u ≡ −∞ on the irreducible component of Int(X ) ∪ {x} containing x.
  Let us make some remarks regarding the content of Proposition 3.5.
3.5.1. If U ⊂ X is an open subset then U is again a k-analytic curve, so it makes sense
to speak of subharmonic functions on U. It is immediate from the definition that a sub-
harmonic function on X restricts to a subharmonic function on U. Hence subharmonic
functions form a presheaf on X . Proposition 3.5(1) asserts that this presheaf is a sheaf.
3.5.2. The maximum principle (Proposition 3.5(6)) is [Thu05, Proposition 3.4.10] in the
smooth, strictly analytic case.
3.5.3. In the situation of Proposition 3.5(7), it is immediate from Definition 3.4 that
u ◦ πk′ /k is subharmonic when u is subharmonic. This is the difficult direction in the
smooth, strictly analytic case: see [Thu05, Corollaire 3.4.5]. This result is hidden in the
12                                 W. GUBLER AND J. RABINOFF

fact that Definition 3.4 essentially recovers Thuillier’s definition of subharmonicity in that
case 3.4.1.
3.5.4. In the situation of Proposition 3.5(8), it is immediate from Definition 3.4 that u◦ f
is subharmonic when u is subharmonic. The remark in 3.5.3 applies to a lesser extent in
this case: see [Thu05, Proposition 3.1.14].
3.5.5. For any x ∈ X , the subset Int(X )∪{x} is open in X . This is obvious if x ∈ Int(X ), and
if x ∈ ∂ X then it follows from the fact that ∂ X is discrete in X . In particular, Int(X ) ∪ {x}
is again a k-analytic curve, so it makes sense to speak of its irreducible components
in Proposition 3.5(9). Irreducible components can only meet at rig-points (their inter-
sections are Zariski-closed), so a non-rig-point x is contained in a unique irreducible
component of Int(X ) ∪ {x}; this is implicit in Proposition 3.5(9).
3.5.6. Proposition 3.5(9) implies that if u is subharmonic and u(x) = −∞ for a non-rig-
point x ∈ X , then u ≡ −∞ in a neighborhood of x.
3.6. In order to extend Thuillier’s results, we will pass from a k-analytic curve to a
smooth, strictly k-analytic curve in four steps:
      (1) Extend scalars to a field as in 2.10 to make the curve strictly analytic.
                                                                                          −∞
      (2) If char(k) = p, then extend scalars to the completion of the perfect closure k p .
      (3) Replace the analytic curve by the underlying reduced curve.
      (4) Pass to the interior of the normalization, which is smooth (see 2.13).
We begin with some lemmas about this process.
                                                                                 −∞
Lemma 3.7. Suppose that char(k) = p > 0. Let k′ be the completion of k p . Then k′ is
perfect, and if X is a k-analytic space then πk′ /k : X k′ → X is a homeomorphism such that
π(∂ X k′ ) = ∂ X .
Proof. We leave it as an exercise for the reader to verify that k′ is perfect. The fact that
πk′ /k is a homeomorphism is [Duc09, Remarque 0.5], and the assertion about boundaries
is Lemma 2.12.                                                                            □
     We make the following observation to mirror Lemma 3.7. Its proof is immediate.
Lemma 3.8. Let X be a strictly k-analytic space and let ι : X red ,→ X be the inclusion of the
underlying reduced space. Then ι is a homeomorphism of underlying topological spaces, and
ι(∂ X red ) = ∂ X .
  We refer the reader to [Ber90, before Proposition 3.1.8] for the construction of the
normalization.
Lemma 3.9. Let X be a reduced, strictly k-analytic curve and let ν: Xe → X be its normal-
ization. Then the following hold:
    (1) Xe is rig-smooth if k is perfect.
    (2) ν is an isomorphism outside of a discrete set of rig-points of X .
                                     ∼
    (3) ν induces a bijection ∂ Xe −→ ∂ X .
    (4) ν is a topological quotient.
              CLASSICALLY PSH AND PLURIHARMONIC FUNCTIONS ON BERKOVICH SPACES                       13

                                                                             e = ν−1 (U) →
    (5) Let x ∈ X , let U be an open neighborhood of x, and consider the map U
        U. If U is a sufficiently small connected open neighborhood of x, then:
         (a) Ue → U is injective on connected components of U.  e
                                                                 ∼
         (b) Ue → U restricts to an isomorphism U  e \ ν−1 (x) −→ U \ {x}.
         (c) Every connected component of U   e intersects ν−1 (x).
    (6) A function h: X → R is R-PL if and only if h ◦ ν is R-PL.



Proof. The normalization Xe is locally the Berkovich spectrum of a Dedekind domain, so it
is rig-smooth when k is perfect because it is regular; this proves (1). Normalization is an
isomorphism away from codimension 1 as in algebraic geometry, which yields (2). Since
ν is finite, we have ∂ Xe = ν−1 (∂ X ) by the properties (2′ ) and (4′ ) of 2.11, so (3) follows
from (2) because the boundaries do not contain any rig-points. Assertion (4) was noted
in [Duc24, (3.1.3)].
    Now we prove (5). Since normalization is a local construction, we may shrink X to
assume that it is normal away from x. Suppose that ν−1 (x) = {x 1 , . . . , x n }, and choose
disjoint, connected open neighborhoods U1′ , . . . , Un′ of x 1 , . . . , x n , respectively. Let U ′ =
Sn                                                                         ∼
   i=1
       ν(Ui′ ).FSince ν induces an isomorphism Xe \ {x 1 , . . . , x n } −→ X \ {x}, it is clear that
                      n
ν−1 (U ′ ) = i=1 Ui′ . Since ν is a topological quotient, we have that U ′ is open, and ν is
injective on each Ui′ by construction.
    Suppose now that U ⊂ U ′ is a connected open neighborhood of x. By [Ber90, Theorem
3.2.1], U is path-connected. Clearly U satisfies (a) and (b). Let Ui = ν−1 (U) ∩ Ui′ , so that
                      e = ν−1 (U) = n Ui . In order to prove (c), it is enough to show that Ui
                                      F
x i ∈ Ui and U                          i=1
is path-connected. Let y ∈ Ui \ {x i }, and let γ: [0, 1] → U be a path from π( y) to x.
We may assume that γ−1 (x) = {1}, so that γ restricts to a path [0, 1) → U \ {x}. Let
γ
e : [0, 1) → U       e \ ν−1 (x) be the composition of γ|[0,1) with the inverse of the isomorphism
                      ∼
e \ ν−1 (x) −→ U \ {x}. Then γ
U                                        e(0) = y, so the image of γ e is contained in Ui . Extend γ  e
to a function [0, 1] → Ui by setting γ        e(1) = x i . One checks continuity of γ e at 1 using the
fact that an open neighborhood of x is the same as a collection of open neighborhoods
of x 1 , . . . , x n , as in the previous paragraph. This shows that Ui is path-connected.
    In the situation of (6), if h is R-PL then h◦ν is R-PL by [GJR21, Lemma 5.4(1)]. Suppose
then that h ◦ ν is R-PL. Piecewise linearity of h is local on X , and ν is an isomorphism
away from a finite set of (non-normal) rig-points, so it is enough to check that h is R-PL
in a neighborhood of a single rig-point x. Let x ′ ∈ Xe be a preimage ofPx. There is a
                                                                                          n
covering of Xe by strictly affinoid domains on which h ◦ ν has the form i=1 λi log | f i |,
where λi ∈ R and f i ∈ O × . Since x ′ is      Pan rig-point, it is contained in the interior   of one
of these affinoid domains, so h ◦ ν = i=1 λi log | f i | in a neighborhood of x . But if f is
                                                                                          ′

invertible in a neighborhood of a rig-point x ′ , then | f | is constant on a neighborhood of
x ′ (this elementary fact can be seen as a very special case of [Duc12, Theorem 3.4]). It
follows that h◦ν is constant in a neighborhood of x ′ . Suppose that ν−1 (x) = {x 1 , . . . , x n }.
For eachSn i choose an open neighborhood Ui of x i on which h ◦ ν is constant. As above,
U = i=1 ν(Ui ) is an open neighborhood of x, and clearly h is constant, hence R-PL,
on U.                                                                                                 □
14                                  W. GUBLER AND J. RABINOFF

Proof of Proposition 3.5(1). This follows from the corresponding fact for subharmonic
functions on smooth, strictly analytic curves [Thu05, Corollaire 3.1.13], except that one
has to be careful about where a function takes the value −∞. Suppose then that {Ui }
is an open cover of X and that u: X → R ∪ {−∞} is subharmonic on each Ui . Note that
u is upper semicontinuous. Let k′ /k be an analytic extension field with k′ non-trivially
valued, let Y be a smooth, connected, strictly k′ -analytic curve, and let f : Y → X k′ be a
morphism. Assume that u ◦ πk′ /k ◦ f ̸≡ −∞, so we must show that u ◦ πk′ /k ◦ f is sub-
harmonic in Thuillier’s sense. Let Ui′ = π−1 k′ /k
                                                   (Ui ) = (Ui )k′ and let Yi = f −1 (Ui′ ). Since u
is subharmonic on Ui , the composition u ◦ πk′ /k ◦ f |Yi is either subharmonic in Thuillier’s
sense or is identically −∞ on each connected component of Yi .
   Let W1 be the set of all points y ∈ Y that admit a neighborhood on which u ◦ πk′ /k ◦ f
is subharmonic in Thuillier’s sense, and let W2 be the set of all points y ∈ Y that admit a
neighborhood on which u ◦ πk′ /k ◦ f ≡ −∞. Clearly W1 and W2 are open, and they cover
Y since Y is covered by the connected components of the Yi . They are disjoint because if
u ◦ πk′ /k ◦ f is subharmonic in Thuillier’s sense on a connected neighborhood of y ∈ Y ,
then it cannot be identically −∞ on any neighborhood of y [Thu05, Lemme 3.1.9].
Since Y is connected and u ◦ πk′ /k ◦ f ̸≡ −∞, we have Y = W1 . The result now follows
from [Thu05, Corollaire 3.1.13].                                                                  □


Proof of Proposition 3.5(2). Let f be an analytic function on X . The function | f | is con-
tinuous and hence u := log | f | is upper semicontinuous as a continuous function with
values in R ∪ {−∞}. According to our definition of subharmonic functions, we have to
show that after base change of u with respect to an analytic field extension k′ /k with k′
non-trivially valued and then pull-back to a smooth strictly k′ -analytic curve, the resulting
function is subharmonic. This boils down to showing that u is subharmonic in the special
case of a smooth strictly k-analytic curve X . For this, we may assume X connected. If
f = 0, then u is identically −∞ and hence subharmonic in the sense of Definition 3.4. If
f is not identically zero, then the Poincaré–Lelong formula [Thu05, Proposition 3.3.15]
and the characterization in terms of positive currents [Thu05, Proposition 3.4.4] show
that u is subharmonic in the sense of Thuillier.                                            □


  We will use the following lemma in the proofs of Proposition 3.5(3,9). If X is a k-
analytic space and k′ /k is an analytic extension field, then π−1
                                                               k′ /k
                                                                     (x) = M (H (x)⊗
                                                                                   b k k′ )
has a finite Shilov boundary for any Abhyankar point x ∈ X by [Duc24, 3.2.14]; we
denote this boundary by x [k′ ] .

Lemma 3.10. Let X be a k-analytic curve and let k′ /k be an analytic field extension. Then
for all x ∈ ∂ X we have (∂ X k′ ) ∩ π−1
                                     k′ /k
                                           (x) = x [k′ ] .

Proof. Replacing X by an affinoid neighborhood of x, we may assume that X = M (A )
is affinoid. By a result of Ducros [Duc12, Lemme 3.1], there exists a morphism g : X →
B1 (0, s) for some s ∈ R>0 such that x ∈ g −1 (ηs ), where ηs is the maximal point of B1 (0, s).


## GRa PDF pages 21-23

             CLASSICALLY PSH AND PLURIHARMONIC FUNCTIONS ON BERKOVICH SPACES               21

Remark 3.16. We still assume that X is a strictly k-analytic curve over a non-trivially
valued field k and that h: X → R is continuous. Proposition 3.15 and Proposition 3.14(6)
imply in particular that if h◦πk′ /k is harmonic for some analytic extension field k′ /k, then
h◦πk′′ /k is R-PL for any analytic extension k′′ /k, which is by no means obvious. Likewise,
Proposition 3.14(7) implies that if f : Y → X is finite and surjective and h◦ f is harmonic,
then h is R-PL, and Proposition 3.14(8) implies that if h|Int(X ) is harmonic then h is R-PL.

                     4. CLASSICALLY PLURISUBHARMONIC FUNCTIONS
  In this section we define the notion of a classically plurisubharmonic function. The
definition follows Definition 3.4.
Definition 4.1 (Classically Plurisubharmonic Functions). Let X be a k-analytic space and
let u: X → R ∪ {−∞} be an upper semicontinuous function. We say that u is classically
plurisubharmonic or classically psh provided that, for every analytic extension field k′ /k,
every k′ -analytic curve Y , and every morphism f : Y → X k′ , the function u◦πk′ /k ◦ f : Y →
R ∪ {−∞} is subharmonic on Y in the sense of Definition 3.4.
4.1.1. Any class of psh functions should respect extension of scalars and should be stable
under pullback, so the conditions in Definition 4.1 are necessary. In complex analysis,
this condition (without the extension of scalars) is the definition of plurisubharmonicity,
which is why we call the notion “classically psh”.
4.1.2. If X is a k-analytic curve, then a function u: X → R∪{−∞} is classically psh if and
only if it is subharmonic. Indeed, if u is classically psh then taking k′ = k and Y = X in
Definition 4.1 shows that u is subharmonic, and if u is subharmonic then it is classically
psh by Proposition 3.5(7,8).
4.1.3. In Definition 4.1, one can assume that Y is a connected, smooth, strictly k′ -analytic
curve: this follows from Definition 3.4.
  Classically psh functions satisfy the basic properties of subharmonic functions on curves.
Proposition 4.2. Let X be a k-analytic space.
   (1) (Sheafiness) The classically psh functions form a sheaf on X .
   (2) If f ∈ Γ (X , OX ) then log | f |: X → R ∪ {−∞} is classically psh.
   (3) (Cone Property) If u1 , u2 : X → R∪{−∞} are classically psh and λ1 , λ2 ∈ R≥0 then
       λ1 u1 + λ2 u2 and max{u1 , u2 } are classically psh.
   (4) (Limits) The infimum of a decreasing net of classically psh functions is classically
       psh. For arbitrary pointwise limits, we refer to Theorem 6.5.
   (5) (Extension of Scalars) Let k′ /k be an analytic extension field. A function u: X →
       R ∪ {−∞} is classically psh if and only if u ◦ πk′ /k : X k′ → R ∪ {−∞} is classically
       psh.
   (6) (Functoriality) Let Y be a k-analytic space and let f : Y → X be a morphism. If
       u: X → R ∪ {−∞} is classically psh then u ◦ f is classically psh, and the converse
       holds if f is finite and surjective.
Proof. Properties (1,3,4) follow immediately from Proposition 3.5(1,4,5). For Proposi-
tion 4.2(2), we consider an analytic function f on X . As | f | is continuous, we deduce
22                                  W. GUBLER AND J. RABINOFF

that log | f | is a continuous function with values in R ∪ {−∞} and hence it is upper semi-
continuous. Then Proposition 4.2(2) follows from Proposition 3.5(2).
    To prove Proposition 4.2(5), it is clear from the definitions that if u is classically psh,
then u ◦ πk′ /k is classically psh for every analytic extension field k′ /k. To prove the con-
verse, we assume that k′ /k is an analytic extension field and that u′ := u ◦ πk′ /k is a
classically psh function on X k′ . Since the morphism πk′ /k is closed and surjective 2.9,
it is clear that u is upper semicontinuous. Let k′′ /k be an analytic extension field and
let f : Y → X k′′ be a morphism over k′′ from a k′′ -analytic curve Y . We have to show
that u ◦ πk′′ /k ◦ f is subharmonic. As in the proof of Proposition 3.5(7), we consider
a simultaneous analytic extension field K of k′ and k′′ . It follows from the above that
u ◦ πK/k = u′ ◦ πK/k′ is classically psh and hence u ◦ πK/k ◦ f K is subharmonic. We con-
clude from the commutative diagram (3.10.1) that u ◦ πK/k ◦ f K = u ◦ πk′′ /k ◦ f ◦ πK/k′′ is
subharmonic and hence u ◦ πk′′ /k ◦ f is subharmonic by Proposition 3.5(7).
    Likewise, the proof of Proposition 4.2(6) follows the same lines as the proof of Propo-
sition 3.5(8). Again, it follows from the definitions if u is a classically psh function on X ,
then u ◦ f is a classically psh function on Y . Conversely, we assume that u ◦ f is a clas-
sically psh function for a finite surjective morphism f : Y → X . Since finite morphisms
are proper and hence closed, we deduce from upper semicontinuity of u ◦ f and from
surjectivity of f that u is upper semicontinuous. It remains to show that u ◦ πk′ /k ◦ g is
subharmonic for any analytic extension field k′ /k and any morphism g : Z → X k′ from a
connected k′ -analytic curve Z. Setting W := Z ×X k′ Yk′ , we get a morphism g ′ : W → Yk′
from f by base change with respect to f ′ : Yk′ → X k′ as in (3.10.2). Since u ◦ f is classi-
cally psh, it follows from Proposition 4.2(5) that u ◦ πk′ /k ◦ f ′ = u ◦ f ◦ πk′ /k is classically
psh. The morphism f is finite and surjective, hence the same holds for f ′ . We con-
clude that the base change f ′′ : W → Z of the morphism f ′ is finite and surjective. The
k′ -analytic space W has irreducible components of dimension 1 and maybe isolated irre-
ducible components of dimension 0. Removing the latter, we obtain a k′ -analytic curve
W ′ as an open and closed subset of W . Since Z is a connected k′ -analytic curve and f ′′
is a finite surjective map from W onto Z, we get an induced finite surjective morphism
W ′ → Z. Indeed, as W ′ is also Zariski-closed in W , we deduce from finiteness of f ′′ that
f ′′ (W ′ ) is a Zariski-closed subset in Z of dimension 1 and hence f ′′ (W ′ ) = Z as Z is a
connected k′ -analytic curve. Since the inclusion W ′ → W is obviously finite, the com-
position W ′ → Z is also finite. In the following, we replace W by W ′ , which preserves
the commutativity of the diagram (3.10.2) and has the advantage that W is a k′ -analytic
curve. It follows that u ◦ πk′ /k ◦ f ′ ◦ g ′ = u ◦ πk′ /k ◦ g ◦ f ′′ is subharmonic on W . The
morphism of k′ -analytic curves f ′′ : W → Z is finite and surjective, so we deduce from
Proposition 3.5(8) that u ◦ πk′ /k ◦ g is subharmonic.                                           □

  In the paper [GR25], we have studied semipositive R-PL functions on a good strictly
k-analytic space over a non-trivially valued non-archimedean field k. This turns out to
be the same as an R-PL function that is classically psh, as we now show.

Theorem 4.3. Suppose that the valuation on k is nontrivial. Let X be a good, strictly k-
analytic space and let h: X → R be an R-PL function. Then h is semipositive if and only if h
is classically psh.
              CLASSICALLY PSH AND PLURIHARMONIC FUNCTIONS ON BERKOVICH SPACES                  23

Proof. For x ∈ X , an R-PL function h: X → R induces a residue line bundle Lh (x) ∈
Pic(red(X , x))R on the reduction red(X , x) of the germ (X , x): see 2.17. Recall from
[GJR21, Definition 7.2] that h is semipositive at x ∈ X if and only if the associated residue
line bundle Lh (x) is nef. We have shown in [GR25, Proposition 3.1] that for a smooth
strictly k-analytic curve, an R-PL function is semipositive if and only if it is subharmonic.
Since semipositivity is stable under base extension and pull-back [GJR21, Proposition
7.6], we conclude that a semipositive R-PL function on X is classically psh.
   The converse follows from [GR25, Corollary 3.5], which shows that an R-PL function h
on X is semipositive if and only if there is an algebraically closed analytic extension field
F of k such that for every smooth F -analytic curve C and every morphism ϕ : C → X F ,
we have h ◦ ϕ semipositive.                                                                □
                                 5. CONNECTIVITY BY CURVES
  We will prove a maximum principle for classically psh functions by reducing to the
case of curves. For this we will need to prove that it is possible to connect a point of an
analytic space to its neighbors using analytic curves, potentially defined over large field
extensions.
Definition 5.1. Let X be a k-analytic space. An analytic curve in X is a subset Γ ⊂ X
satisfying the following property: there is an analytic extension field k′ /k, a compact,
separated k′ -analytic space C of dimension at most 1, and a morphism ϕ : C → X k′ , such
that Γ = πk′ /k ◦ ϕ(C).
  An analytic curve Γ in X is overconvergent if there exist (k′ , C, ϕ) as above such that ϕ
factors as
                                          ψ
                                           → Int(C ′ ) -← → C ′
                                      ←
                                  C
                                      ←
(5.1.1)                                                     ←
                                          ϕ →            ϕ′
                                                           →
                                               X k′
where C ′ is a separated k′ -analytic space of dimension at most 1, and ϕ ′ and ψ are
morphisms.
5.1.2. The compactness hypothesis in Definition 5.1 is crucial. When X is Hausdorff, it
implies that if Γ , Γ ′ are analytic curves in X such that Γ ∪ Γ ′ is connected, then Γ ∩ Γ ′ ̸= ;
(the compact sets Γ , Γ ′ are closed, so they cannot be disjoint by connectedness). However,
a non-proper compact curve has a nonempty boundary, which causes problems when
trying to reduce the maximum principle to the case of curves. This is the reason for
introducing overconvergent curves in X .
5.1.3. One can always pass to a larger analytic extension field k′′ /k′ in Definition 5.1.
Indeed, we have a commutative diagram
                                          ←   ϕk′′
                                   Ck′′         → X k′′
                                                                   πk′′ /k
                                      ←



                                                       ←




                                                               ←
                                                πk′′ /k′
                                                                   →
                                   ↠



                                                      →




                                          ←                  ←
                                      C       ϕ→      X k′         → X.
                                                               πk′ /k


## GRa PDF pages 30-34

30                                   W. GUBLER AND J. RABINOFF

after recentering, we can assume that ϕ(V ) ⊂ B+n . For x ′ ∈ V let y ′ = ϕ(x ′ ) ∈ B+n and
let Σ x ′ be the connected component of ϕ −1 ([ y ′ , 0]) containing x ′ . Since [ y ′ , 0] ⊂ B+n we
have ϕ −1 ([ y ′ , 0]) ⊂ Int(Y ), and since Σ x ′ is connected and x ′ ∈ V we have Σ x ′ ⊂ V . As
before, there exists an open neighborhood U of x in V such that Σ x ′ ∩ Σ x ̸= ; for all
x ′ ∈ U.
     By Lemma 5.9, for any y ′ ∈ B+n there is a connected, overconvergent analytic curve
Γ y ′ in B+n containing [ y ′ , 0]. For x ′ ∈ V mapping to y ′ , we let Γ x ′ be the connected
component of ϕ −1 (Γ y ′ ) containing x ′ , so that Γ x ′ ⊂ V for the same reason that Σ x ′ ⊂ V .
By Lemma 5.2(1,4), this Γ x ′ is again a connected, overconvergent analytic curve in X .
Clearly Σ x ′ ⊂ Γ x ′ , so for x ′ ∈ U we have Γ x ′ ∩ Γ x ̸= ;. This completes the proof as in the
previous case.                                                                                     □

              6. THE MAXIMUM PRINCIPLES FOR CLASSICALLY PSH FUNCTIONS
  In this section, we consider a non-Archimedean field k. We will prove first that the
local maximum principle holds for classically psh functions, and then we will show a
global maximum principle in the affinoid case; more specifically, that that a classically
psh function takes its global maximum at a Shilov point.
Theorem 6.1 (Local Maximum Principle). Let X be a k-analytic space and let u be a clas-
sically psh function on X . If u has a local maximum at x ∈ Int(X ), then u is locally constant
at x.
Proof. We may replace X by a connected, Hausdorff open neighborhood of x in Int(X ) to
assume that X is connected and boundaryless and that u attains a global maximum at x.
Let R = u(x). Let Γ be a connected, overconvergent analytic curve in X containing x. We
claim that u ≡ R on Γ . Consider the set Γu=R = {z ∈ Γ | u(z) = R}. This set is closed in Γ
by upper semicontinuity of u, so since Γ is connected, it suffices to show that Γu=R is open
in Γ .
   By 5.1.3, there exist an analytic extension field k′ /k, a compact, separated strictly k′ -
analytic space C of dimension at most 1, a separated strictly k′ -analytic space C ′ of dimen-
sion at most 1, and morphisms ψ: C → C ′ and ϕ ′ : C ′ → X k′ , such that ψ(C) ⊂ Int(C ′ )
and πk′ /k ◦ ϕ(C) = Γ , where ϕ = ϕ ′ ◦ ψ. The composition u ◦ πk′ /k ◦ ϕ ′ is subharmonic
on 1-dimensional connected components of C ′ because u is classically psh.
   Let y ∈ Γu=R , let z ∈ C be a point lying over y, and let z ′ = ψ(z) ∈ Int(C ′ ), so that
R = u ◦ πk′ /k ◦ ϕ ′ (z ′ ) = u ◦ πk′ /k ◦ ϕ(z). If {z ′ } is a connected component of C ′ then clearly
u ◦ πk′ /k ◦ ϕ ′ ≡ R in a neighborhood of z ′ . Otherwise, the connected component of z ′
in C ′ is a strictly k′ -analytic curve, in which case u ◦ πk′ /k ◦ ϕ ′ ≡ R in a neighborhood
of z ′ by Proposition 3.5(6) (here we use z ′ ∈ Int(C ′ )). Taking the ψ-inverse image of
such a neighborhood, we see that u ◦ πk′ /k ◦ ϕ ≡ R in a neighborhood of z. Applying
this argument to each z ∈ (πk′ /k ◦ ϕ)−1 ( y), we construct an open set V ⊂ C containing
(πk′ /k ◦ ϕ)−1 ( y) such that u ◦ πk′ /k ◦ ϕ|V ≡ R.
   The complement C \ V is a closed subset of the compact space C, so it is a compact
subset of C that is disjoint from (πk′ /k ◦ ϕ)−1 ( y). Its image is a compact subset of X that
does not meet y, so there is an open neighborhood W of y such that (πk′ /k ◦ϕ)−1 (W ) ⊂ V .
              CLASSICALLY PSH AND PLURIHARMONIC FUNCTIONS ON BERKOVICH SPACES                     31

It follows that u ≡ R on W ∩ Γ . This proves that Γu=R is open in Γ . As remarked above,
this yields u ≡ R on Γ .
   Let y ∈ X be any point. By Theorem 5.4, there is a connected, overconvergent analytic
curve Γ in X containing x and y. We showed above that u ≡ R on Γ , so that u( y) = R.
As y was arbitrary, we have u ≡ R on X .                                              □

  The global maximum principle for classically psh functions involves the Shilov bound-
ary. For this, we need the following two lemmas. The first is well-known, but we were
unable to find a reference.

Lemma 6.2. Let X be a k-affinoid space of pure dimension d ≥ 1. Then the Shilov boundary
of X is contained in the relative boundary ∂ X of X over k. In particular, ∂ X ̸= ;.

Proof. Let k′ /k be an analytic field extension such that X k′ is strictly affinoid. Note that
the base change morphism πk′ /k maps ∂ X k′ to ∂ X 2.11(5′ ) and maps the Shilov boundary
onto the Shilov boundary [GRW17, Proposition 2.21], so we may assume that X is strictly
affinoid and k′ non-trivially valued. Choose a formal affine k◦ -model X of X . The interior
X \ ∂ X consists of the points x ∈ X such that the closure of redX (x) in Xs is proper over
the residue field ek by [CD12, Lemme 6.5.1]. Since X is affine, the special fiber Xs is
affine, so x ∈ ∂ X if and only if redX (x) is not a closed point of Xs . Since d ≥ 1, the
special fiber Xs is of pure dimension d ≥ 1, and hence the generic points of Xs are not
closed. By [GM19, Proposition A.3], the divisorial points of X (i.e. the points of X which
reduce to the generic points of Xs ) are precisely the Shilov points of X . We conclude that
all Shilov points are in the boundary of X .                                                □

   Let X = M (A ) be an affinoid space over k of pure dimension d. By a result of Ducros
[Duc12, Lemme 3.1], the boundary ∂ X of X can be expressed as a union of affinoid spaces
of lower dimension, defined over certain extension fields of k. We use his argument to
give a stratification of ∂ X . Choose non-nilpotent elements g1 , . . . , g r ∈ A such that the
graded reductions e   g1• , . . . , e
                                    g r• generate the graded ek• -algebra A
                                                                          f• . Let ri be the spectral
radius of g i . Then for any I ⊂ {1, . . . , r}, we get a morphism

                                p I : X −→ B(I),       x 7→ (g i (x))i∈I

to the closed poly-disc B(I) = i∈I B(0, ri ) of dimension s = |I|. Let η(I) be the weighted
                                     Q

Gauss point of B(I) and let k I := H (η(I) ), which is the completion of the field of rational
functions k((t i )i∈I ) in the variables (t i )i∈I with respect to the weighted Gauss valuation
for the weight (ri )i∈I .

Lemma 6.3. With the above notations, set X I := p−1
                                                 I
                                                    (η(I) ). By convention, we set X ; = X .
Then:
                 k I -affinoid space of pure dimension d − s if non-empty.
    (1) X I is a S
    (2) ∂ X I = i∈{1,...,r}\I X I∪{i} .
    (3) X I = {x ∈ X | (e   g i• (x))i∈I are algebraically independent in H
                                                                          f• (x) over ek• }.
                                                                                     S
    (4) If X has pure dimension d, then the Shilov boundary of X is equal to |I|=d X I .
32                                  W. GUBLER AND J. RABINOFF

   We note that the affinoid space X I is naturally homeomorphic to the fiber p−1
                                                                               I
                                                                                  (η(s) ) ⊂ X
in the subspace topology: see [Ber93, §1.4]. If I is non-empty, then we call X I a stratum
set for the boundary.
Proof. Since p I is a morphism between the k-affinoid spaces X and B(I) of pure dimension
d and s, respectively, and since the Gauss point η(I) is an Abhyankar point of B(I), we de-
duce from [Duc18, Lemma 1.5.11] that X I is a H (η(I) )-affinoid space of pure dimension
d − s if non-empty. This proves (1).
  The remaining argument is based on the following description of the boundary given
by Ducros in [Duc12, Lemme 3.1]. For any x ∈ X = M (A ), we get an induced character
ψ: A → H (x). Then Temkin’s graded reduction of the germ (X , x) is given by [Tem00,
§2]
                               red(X , x) = PHf(x)/ek {ψ
                                                       e• (A )}.

By definition, this is the set of graded valuations w on H           f• (x) which are trivial on ek
and which satisfy |ψ     e• (g)|w ≤ 1 for all g ∈ A . Using that the graded reductions of our
fixed family g1 , . . . , g r ∈ A generate the graded ek• -algebra A     f• , it is enough to check
|ψe• (g)|w ≤ 1 for g = g1 , . . . , g r . Based on Temkin’s result on graded reductions, Ducros
shows that x ∈ ∂ X is equivalent to the existence of some i ∈ {1, . . . , r} and of a graded
valuation w on H       f• (x) which is trivial on ek• such that |ψ(g i )|w > 1. Ducros shows in
his argument that this is equivalent to e      g i• (x) ∈ H
                                                          f• (x) being transcendental over ek• . For
i = 1, . . . , r, he considers the morphism pi : X → B(0, ri ) induced by g i . Let X i be the fiber
over the weighted Gauss point η(i) of the closed disc B(0, ri ) = M (k〈ri−1 t〉) (of radius ri ).
By (1), we have that X i is a H (η(i) )-affinoid space of pure dimension d − 1 if non-empty.
It follows from the above that the union of all of the X i is equal to ∂ X .
   Let us summarize the construction. For each i ∈ {1, . . . , r}, we define
                       X i := {x ∈ X | e
                                       g i• (x) is transcendental over ek• }.
This set might be empty. We have seen that g i defines a morphism pi : X → B(0, ri ) =
M (k〈ri−1 t〉) for the Tate algebra k〈ri−1 t〉 in the variable t, and that X i is the fiber of pi
over the weighted Gauss point η(i) . In any case, X i is an affinoid space over the non-
archimedean field ki := H (η(i) ) which is the completion of k(t) with respect to the
weighted Gauss valuation for the weight ri . If X i is non-empty, then X i has pure dimen-
sion d − 1. Ducros has shown that
                                                [
                                     ∂X =            Xi.
                                               i∈{1,...,r}

   We prove now the claims (2)–(3) by induction on s = |I|. If s = 0, then I = ; and
X I = X . Then the above description of the boundary due to Ducros proves (2) and
(3). Now assume that s > 0. We pick i ∈ I and set J := I \ {i}. As seen above, we
have that X i := pi−1 (η(i) ) is an affinoid space over ki = H (η(i) ), and we denote the
corresponding affinoid algebra by Ai := O (X i ). Note here that ki is the completion of
k(t) with respect to the weighted Gauss norm for the weight ri . For Ai = A ⊗          b k ki , the
                                                            •               •
same elements g1 , . . . , g r induce generators of Ai as a graded ki -algebra. Note that
                                                          f               e
H (η(I) ) is the completion of k((t i ′ )i ′ ∈I ) with respect to the Gauss norm for the weight
               CLASSICALLY PSH AND PLURIHARMONIC FUNCTIONS ON BERKOVICH SPACES                           33

(ri ′ )i ′ ∈I and hence also the completion of ki (r j ) j∈J with respect to the weighted Gauss
norm for the weight (r j ) j∈J identifying the variable t ∈ ki with t i . It follows readily that
for any H ⊂ {1, . . . , r}, we have (X i )H = X {i}∪H as affinoid spaces over k I . Applying this
with H = J and using our induction hypothesis for X i , property (2) for the boundary of
X I = (X i )J follows by induction applied to X i . The same inductive argument shows that
X I is the set of points x ∈ X 1 where (e      g j (x)) j∈J are algebraically independent over eki . We
have seen that X i is non-empty if and only if e           g i (x) is transcendental over ek. Since t = t i
in ki satisfies pi (t) = g i , we conclude that x ∈ X I if and only if (e
                      ∗
                                                                               g l (x))l∈I are algebraically
independent over ek. This proves (3).
   Finally, we claim that the union of the minimal strata X I for |I| = d is the Shilov
boundary of X . If d = 0, this is obious as X = X ; . Now assume that d ≥ 1. If x ∈ X I then
(3) shows that the graded residue field H            f(x)• contains the d algebraically independent
elements (e     g i )i∈I over ek• . Since the reduction Xe in the sense of Temkin [Tem04, Section
3] is of pure dimension d (using [Tem04, Proposition 3.1(v)] for base change to the
strictly affinoid case), we conclude that the reduction of x in Xe is a generic point of Xe .
By [Tem04, Proposition 3.3], we conclude that x is a Shilov point of X . Conversely, for
every a ∈ A , the function |a| takes its maximum in a Shilov point. We conclude from
Lemma 6.2 that |a| takes its maximum in ∂ X ̸= ;. By (2), we conclude that |a| takes its
maximum in one of the strata sets X I . By induction on the dimension d, this occurs when
|I| = d proving (4).                                                                                      □
  We return to the setting where k is any non-Archimedean field which might be trivially
valued. We give now the global maximum principle for affinoids.
Theorem 6.4. Let h be a classically psh function on a k-affinoid space X . Then h takes its
maximum in a Shilov point of X .
  An analogue for θ -psh functions on a proper scheme is in [GM19, Proposition 4.22].
Proof. By base change to a non-trivially valued analytic extension field k′ /k such that X k′
is strictly affinoid, and using that πk′ /k maps the Shilov boundary of X k′ to the Shilov
boundary of X [GRW17, Proposition 2.21],    S we may assume that X is strictly affinoid and
that k is non-trivially valued. Let X = j X j be the partition of X into its irreducible
components. It follows from [GRW17, Proposition 2.15] that the union of the Shilov
points of all X j gives the Shilov points of X . So it is enough to prove the claim for every
X j , and hence we may assume X irreducible. This will be a bit to strong for our inductive
argument later, but the argument shows that we may assume X of pure dimension d.
    If d ≥ 1, then we claim that h takes its maximum in the boundary ∂ X . We prove this
by contradiction. It is clear that the boundary ∂ X is the disjoint union of the boundaries
of the connected components of X , and the same holds if we replace the boundary by the
Shilov boundary, so we may assume X connected. Let M be the set of points of X where
h is maximal. We assumed that M ∩ ∂ X = ;. Since h is continuous, it is clear that M is
a closed subset of X . We know from Theorem 6.1 that if a classically psh function takes
a (local) maximum on X \ ∂ X , then h is locally constant. This implies M open in X . As
M is non-empty and X is connected, we deduce M = X . Since ∂ X ̸= ; as we have d ≥ 1
(see Lemma 6.2), we get M ∩ ∂ X ̸= ;, which is a contradiction.
34                                 W. GUBLER AND J. RABINOFF

    Let now
        S h be a classically psh function on X . We need the description of the boundary
∂ X = X i given in Lemma 6.3, where i runs through {1, . . . , r} and X i = X {i} as before.
We claim by induction on d that h takes its maximum in one of the sets X I with |I| = d,
and hence in the Shilov boundary of X , which proves the theorem. If h is constant, then
this is obvious; this also settles the case d = 0. If h is non-constant, then we have seen
at the beginning of the proof that h takes its maximum in ∂ X , and hence in one of the
X i . Since X i is of dimension d − 1, we are done by induction as the strata sets of ∂ X i are
strata sets of ∂ X using Lemma 6.3.                                                          □
  The following result was suggested by a referee of the paper [GR25]. We are very
grateful for this hint.
Theorem 6.5. Let (u j ) j∈J be a net of classically psh functions on the k-analytic space X
which converges pointwise to an upper semicontinuous function u. Then u is classically psh.
   For a sequence of semipositive R-PL functions converging pointwise to an R-PL func-
tion, the above result was shown in [GR25, Theorem 5.6]. When X is a proper algebraic
variety, this was known before ([GK19, Proposition 7.2] for uniform limits, [GM19, The-
orem 1.3] for pointwise limits).
Proof. Since u is upper semicontinuous, using the definition of classically psh functions,
we may assume that X is a connected smooth curve over a non-trivially valued field.
We may assume that u is not identically −∞. Then for every strictly k-affinoid domain
U of X and every harmonic function h on U with u ≤ h on ∂ U, we have to show that
u ≤ h holds on U. Since u j → u pointwise and since ∂ U is finite, for any ϵ > 0 we have
u j − h ≤ ϵ on ∂ U for all j sufficiently large. Since u j − h is a classically psh function by
Proposition 3.5(4) and since the Shilov boundary of U agrees with ∂ U [Thu05, §2.1.2],
the global affinoid maximum principle in Theorem 6.4 shows that u j − h ≤ ϵ on U for all
j sufficiently large. It follows that u − h ≤ ϵ on U, which implies u ≤ h on U since ϵ was
arbitrary.                                                                                   □

                               7. PLURIHARMONIC FUNCTIONS
  In this section, we consider a k-analytic space X over any non-Archimedean field k.
Following the discussion of harmonic functions on curves in 3.12, we generalize this
notion as follows to higher dimensions.
Definition 7.1. A function h: X → R is called pluriharmonic if h and −h are classically
psh functions (see Definition 4.1).
Proposition 7.2. Pluriharmonic functions are continuous and have the properties:
     (1) (Sheafiness) The pluriharmonic functions form a sheaf on X .
     (2) If f ∈ Γ (X , OX× ) then log | f | is pluriharmonic.
     (3) (Vector Space) The pluriharmonic functions on X form a real vector space which
         we denote by PH(X ).
     (4) (Limits) If a function h: X → R is locally a uniform limit of pluriharmonic functions,
         then h is pluriharmonic.


## GRb PDF pages 1-3

                                             ON SEMIPOSITIVE PIECEWISE LINEAR FUNCTIONS IN NON-ARCHIMEDEAN
                                                                   ANALYTIC GEOMETRY

                                                                        WALTER GUBLER AND JOSEPH RABINOFF
arXiv:2503.05513v1 [math.AG] 7 Mar 2025




                                                  ABSTRACT. In this paper, we generalize results on Zhang’s semipositive model metrics
                                                  from the algebraic setting to strictly analytic spaces over a non-trivially valued non-
                                                  Archimedean field. We prove stability under pointwise limits and under forming the
                                                  maximum. We also prove the maximum principle. As tools, we use a local lifting theo-
                                                  rem from the special fiber to the generic fiber of a model and an affinoid Bieri–Groves
                                                  theorem.



                                                                                   1. INTRODUCTION
                                             In Diophantine Geometry, an important tool is the height of a proper variety X with
                                          respect to a given metrized line bundle L. This height is defined as an arithmetic self
                                          intersection number introduced by Gillet and Soulé [GS90] in higher dimensions. Zhang
                                          [Zha95] realized that the contribution of a non-Archimedean place v to this arithmetic
                                          intersection product is given by a v-adic metric associated to a model (X , L ) of (X , L)
                                          over the valuation ring of v. Such a model metric is called semipositive if the model L
                                          is a nef line bundle on the proper variety X . More generally, Zhang introduced semi-
                                          positive continuous metrics as uniform limits of semipositive model metrics. He showed
                                          that the canonical metrics of polarized dynamical systems are semipositive continuous
                                          metrics. This point of view turned out to be very important in the proof of the Bogomolov
                                          conjecture by Ullmo [Ull98] and Zhang [Zha98]. As pointed out in [Gub98], the model
                                          metrics can be studied over any non-trivially valued non-Archimedean field working with
                                          Berkovich spaces and their formal models leading to a theory of local heights for proper
                                          varieties.
                                             Let k be a field that is complete with respect to a nontrivial, non-Archimedean abso-
                                          lute value. The theory of subharmonic functions on a smooth, strictly analytic k-curve
                                          X has been worked out by Thuillier in his thesis [Thu05]. In higher dimensions, we still
                                          lack a completely satisfactory theory of plurisubharmonic functions on Berkovich spaces.
                                          As work of Boucksom and Jonsson [BJ22] in the algebraic setting suggests, such a the-
                                          ory might be build upon regularization by semipositive piecewise linear functions. This
                                          means that plurisubharmonic functions should be given as decreasing limits of semipos-
                                          itive piecewise linear functions. The latter are the local analogues of semipositive model
                                          metrics. The crucial role of semipositive piecewise linear functions is then supported by
                                          Zhang’s global approach to semipositive continuous metrics.
                                             2020 Mathematics Subject Classification. Primary 14G40; Secondary 31C05, 32P05, 32U05.
                                             Key words and phrases. Berkovich spaces, tropicalization, plurisubharmonic functions.
                                             W. Gubler was supported by the collaborative research center SFB 1085 Higher Invariants - Interactions
                                          between Arithmetic Geometry and Global Analysis funded by the Deutsche Forschungsgemeinschaft.
                                                                                             1
2                                   W. GUBLER AND J. RABINOFF

  In this paper, we study semipositivity of piecewise linear functions on a good strictly k-
analytic space X . This completes our study of such functions in [GJR21], and generalizes
results given in [GM19] from the algebraic to the analytic setting.

Piecewise linear functions. Let X be a good strictly k-analytic space X (see Section 2
for more details on the prerequisites on non-Archimedean analytic spaces). We say that
h: X → R is piecewise linear if for any x ∈ X there are finitelyS  many strictly k-analytic
domains Vj and invertible analytic functions g j on Vj such that Vj is a neighbourhood
of x in X and such that h = log |g j | on Vj . An R-PL function is a real function which is
locally an R-linear combination of piecewise linear functions.
   The semipositivity condition can be best described in terms of Temkin’s reduction of
germs. To any point x ∈ X , Temkin associates [Tem00] the reduction red(X , x) of the
germ (X , x); this is a kind of Riemann–Zariski space defined over the residue field ek which
keeps track of all local formal models over the valuation ring of k. There is a canonical
homomorphism u 7→ Lu (x) from the space of germs of PL functions at x to Pic(red(X , x)).
This homomorphism extends to a homomorphism from the space of germs of R-PL func-
tions to Pic(red(X , x)) ⊗ R. We say that an R-PL function h is semipositive at x ∈ X if
Lu (x) is nef in Pic(red(X , x)) ⊗ R. See [GJR21, Section 6] for more details.

Lifting theorems. The idea is to relate the notion of numerical effectivity of the line
bundle Lu (x) on the reduction, which is a condition that is checked on curves embedded
in the special fiber of some formal model, to the plurisubharmonicity of u, which is a
condition that is by definition checked on curves embedded in the generic fiber. This is
made possible by a suitable local lifting theorem, which allows us locally to lift a subvariety
of the special fiber of a formal model to a Zariski-closed subspace of the analytic generic
fiber. This is the technical heart of the paper. We only describe here in the introduction
the affine lifting theorem, given in Theorem 3.1, which is of global nature.
Theorem 1.1. Let X be a strictly k-affinoid space with affine formal model X. Then for every
d-dimensional irreducible closed subvariety W of the special fibre of X, there is an irreducible
Zariski closed subspace Y of X of dimension d such that W is an irreducible component of
the special fibre of the formal closure of Y in X.
   For flat algebraic (but not necessarily affine) schemes over the valuation ring of k,
this was shown in [GK19, Theorem 4.1]. In the analytic setting, Theorem 1.1 does not
imply a global result, as a Zariski-closed subspace of an affinoid domain in an analytic
space does not usually extend to the whole space. This is the reason that we can prove
only locally a lifting theorem in case of an arbitrary good quasi-compact strictly k-analytic
space (Theorem 4.1). The argument is independent of Theorem 1.1 and is due to Antoine
Ducros.

1.2. Semipositivity and restriction to curves. The local lifting theorem shows that
semipositivity of R-PL functions is the analogue of plurisubharmonicity in the complex
setting, where psh is defined in terms of restriction to curves.
Theorem 1.3. Let x be a point of a good strictly analytic space X over k and let h: X → R
be R-PL. Then h is semipositive at x if and only if for every sufficiently small strictly analytic
     ON SEMIPOSITIVE PIECEWISE LINEAR FUNCTIONS IN NON-ARCHIMEDEAN ANALYTIC GEOMETRY         3

neighbourhood U of x and every Zariski-closed curve C in U, the restriction of h to C is a
semipositive R-PL function.
   This will be shown in Theorem 5.3. We can then use base change and normalization
to reduce semipositivity of R-PL functions to the case of smooth analytic curves (Corol-
lary 5.4). As an application, we deduce immediately from the corresponding result for
smooth curves in Thuillier’s thesis that the maximum of two semipositive Q-PL functions
is again a semipositive Q-PL function (Corollary 5.5). This and the following application
of Corollary 5.4 were shown in [GM19] only for proper algebraic schemes X over k.
Theorem 1.4. Let X be a good strictly k-analytic space of k. We assume that the sequence
(h j ) j∈N of semipositive R-PL functions converges pointwise to an R-PL function h. Then h is
semipositive.
   This result, shown in Theorem 5.6, gives also a new proof in the algebraic case.
   We say that an R-PL function h: X → R is a locally Fubini–Study function if the residue
Lh (x) is semiample in Pic(red(X , x)) ⊗ R for every x ∈ X . It is clear that locally Fubini–
Study functions are semipositive R-PL functions. We can then prove the following local
regularization result.
Theorem 1.5. Let h: X → R be an R-PL function on a boundaryless strictly k-analytic
space X and let x ∈ X . Then h is semipositive at x if and only if there is a strictly analytic
neighbourhood U of x and locally Fubini–Study functions (h j ) j∈N on U converging uniformly
to h|U .
   The only if direction is shown in [GJR21, Proposition 7.10] and the converse follows
from Theorem 1.4.
Affinoid Bieri–Groves theorem. Recall that the Bieri–Groves theorem is a crucial re-
sult in tropical geometry showing that for a closed d-dimensional subvariety Y of the
                        n
multipicative torus Gm    , the associated tropical variety Trop(Y ) is a finite union of d-
dimensional (Z, Γ )-polyhedra in Rn (see 2.6 for the conventions in polyhedral geometry),
where Γ = v(k× ) is the value group of the valuation v = − log | | of k. For a quasicompact
                                                                             n,an
strictly analytic space X of pure dimension d and a morphism ϕ : X → Gm           , we define a
                                            n
smooth tropicalization map ϕtrop : X → R by trop ◦ϕ and the associated tropical variety
by ϕtrop (X ). By results of Berkovich and Ducros (see [Duc03]), this tropical variety is
analogously a finite union of (Z, Γ )-polytopes of dimension ≤ d, but the inequality might
be strict. Ducros [Duc12, Théorème 3.4] has shown that trop(∂ X ) is of dimension < d.
In the affinoid case, the results of Ducros yield the following more precise fact which we
will show in Theorem 6.6.
Theorem 1.6. Let X be a strictly affinoid space over k of pure dimension d with relative
                                  n,an
boundary ∂ X and let ϕ : X → Gm        be a morphism. Then the associated tropical variety
ϕtrop (X ) has pure dimension d at every point of ϕtrop (X ) \ ϕtrop (∂ X ).
Maximum principle. We will study the maximum principle in the class of piecewise
smooth functions. Let X be a separated good strictly k-analytic space. A function u: X →
R is called piecewise smooth if there is a G-covering of X by compact strictly k-analytic do-
mains (Vi )i∈I such that for every i ∈ I, there is a smooth tropicalization map ϕi,trop : Vi →


## GRb PDF pages 15-20

     ON SEMIPOSITIVE PIECEWISE LINEAR FUNCTIONS IN NON-ARCHIMEDEAN ANALYTIC GEOMETRY         15

                             5. SEMIPOSITIVE R-PL FUNCTIONS
   Let k be a non-trivially valued non-Archimedean field. We consider a good, strictly
k-analytic space X . We refer to 2.5 for the definition of PL functions. Recall from the in-
troduction that an R-PL function u: X → R is called semipositive at x ∈ X if the associated
residue line bundle Lu (x) ∈ Pic(red(X , x))R is nef, where we refer to [GJR21, 6.16–6.19]
for residue line bundles. Equivalently, there is a strictly affinoid neighbourhood U of x
such that u = hL for a formal k◦ -model (U, L) of (U, OU ) with L nef [GJR21, Proposition
7.1].
   We will show first that for an R-PL function on a smooth curve, semipositivity is the
same as subharmonicity in the sense of Thuillier’s thesis [Thu05, Définition 3.1.5]. Re-
call that Thuillier defines a subharmonic function on a smooth k-analytic curve X as a
semicontinuous function u: X → R ∪ {−∞} which is not identically −∞ on any con-
nected component of X and which has the property that for every harmonic function h
on a strictly affinoid domain U of X with u|∂ U ≤ h|∂ U , we have u|U ≤ h.

Proposition 5.1. Let X be a smooth, strictly k-analytic curve and let u: X → R be an R-PL
function. Then u is subharmonic at x ∈ X in the sense of Thuillier if and only if Lu (x) is nef.

Proof. First we treat the case when k is algebraically closed. As explained in 2.5, there
exists a compact strictly analytic neighborhood U of x in X , a formal k◦ -model U of U,
and a formal model L of OU such that u|U = hL . Since k is algebraically closed, we may
assume that the special fiber Us is reduced, which implies that U is covered by formal
affines of the form Spf(A ◦ ) for a strictly k-affinoid algebra A [GJR21, §2.4]. It follows
from [Ber90, Proposition 2.4.4] that for every irreducible component Y of Us , there is a
unique point ξY ∈ U reducing to the generic point of Y . In the formalism of real valued
forms and currents on Berkovich spaces [CD12], it is well known that d′ d′′ [u]|U is the
discrete measure on U supported on the points ξY of U for Y an irreducible component
of Us , with multiplicity at ξY equal to degL (Y ). See [CD12, §6.9] for a more general
statement. Wanner showed that subharmonicity of u on U is equivalent to the positivity
of the current d′ d′′ [u]: see [Wan19, Theorems 1 and 2] and use the fact that X is locally
algebraic [vdP80]. Thus Ls is nef if and only if u is subharmonic on U. Suppose that u is
subharmonic at x. Shrinking U, we may assume that u is subharmonic on U. This implies
that Ls is nef, so it follows from [GJR21, Proposition 7.1] that Lu (x) is nef. Conversely, if
Lu (x) is nef, then by [GJR21, Proposition 7.1], we may shrink U so that Ls is nef, which
as above implies that u is subharmonic on U.
   It remains to show that subharmonicity of u at x and numerical effectivity of Lu (x)
can be checked after extending scalars to the completion of an algebraic closure K =
(k)∧ . By [GJR21, Proposition 7.6(2)], one can check that Lh (x) is nef after base change
to K. The same is true for subharmonicity: this follows directly from Thuillier’s definition
and the fact that the base change of a harmonic function remains harmonic [Thu05,
Proposition 2.3.18].                                                                       

  Our next goal is a characterisation of semipositive R-PL functions by restriction to
subcurves as in the complex case. We need the following characterization of boundary
points:
16                                W. GUBLER AND J. RABINOFF

5.2. Let X be an admissible formal k◦ -scheme and let x ∈ Xη . Then x ∈ Int(X ) = X \ ∂ X
if and only if the closure of redX (x) is a proper ek-scheme. This follows from [CD12,
Lemme 6.5.1] in the separated case and from [Vil21, Corollary A.4] in general.
Theorem 5.3. Let X be a good, strictly k-analytic space, and let h: X → R be an R-PL
function. For x ∈ X , the following conditions are equivalent.
    (1) The function h is semipositive at x.
    (2) There is a neighborhood W of x such for every strictly analytic neighborhood U ⊂ W
        of x and every Zariski-closed curve C in U, the restriction h|C is semipositive.
Proof. Since semipositivity is an open property that is stable under pullback [GJR21,
Proposition 7.6], it is clear that (1) yields (2).
   Assume that h satisfies (2). By shrinking W , we may assume that W is a strictly affinoid
neighborhood of x and that there is a formal model W of U and a model L of OW on W
with coefficients in R such that h = hL on W . Let Y ⊂ Ws be a curve which is proper over
the residue field ek. To prove semipositivity at x, it is enough to show that degL (Y ) ≥ 0.
   Choose any point y ∈ W reducing to the generic point η of Y . By Theorem 4.1 as
applied to X = W and X = W, there exist z ∈ W with redW (z) = η, a neighborhood U
of z in W , and an irreducible 1-dimensional Zariski-closed subspace C of U containing
z. By shrinking U, we may assume that U is strictly affinoid. By results of Bosch and
Lütkebohmert [Bos14, Theorem 8.4.3] [BL93b, Corollary 5.4(b)], there is a formal model
U of U and a morphism π: U → W extending the inclusion U ,→ W on generic fibers. Let
C be the formal closure of C in U. This is an admissible formal model of C whose special
fiber Cs is a closed 1-dimensional subscheme of Us containing η′ = redU (z). Functoriality
of reductions shows that π(η′ ) = η, so the closure Y ′ of η′ is a curve mapping to Y .
Since the closure of η in Ws is the proper curve Y , we conclude from 5.2 that z ∈ W \
∂ W . The boundary ∂ U is the union of ∂ W ∩ U with the topological boundary of U in
W [Ber90, Proposition 3.1.3], so since U is a neighborhood of z in W , we have z ∈ U \∂ U.
Applying 5.2 to U and its formal model U shows that Y ′ is proper as well. Therefore,
the map Y ′ → Y is finite and surjective. Note that Y ′ is an irreducible component of Cs .
Applying (2) to U and C, we have that h|C is semipositive, and so we deduce from [GJR21,
Lemma 7.4] as applied to (π∗L)|C that degπ∗ L (Y ′ ) ≥ 0. The projection formula then shows
degL (Y ) ≥ 0, as required.                                                                
   To apply results from Thuillier’s thesis [Thu05], we would like to use only smooth an-
alytic curves. To give a variant of the above result suitable for this purpose, we introduce
the following notations:
   For a real function h on X and an analytic field extension F of k, we denote by h F
the induced function on the base change X F = X ⊗     b k F of X . We call an R-PL function
h pluriharmonic if ±h are both semipositive. A strictly k-analytic space X is called rig-
smooth if the sheaf of Kähler differentials, considered on the G-topology, is locally free of
rank equal to the local dimension. The space X is smooth if and only if X is rig-smooth and
boundaryless. See [Duc18] for details (Ducros calls rig-smooth spaces quasi-smooth).
Corollary 5.4. Let X be a good, strictly k-analytic space and let h: X → R be an R-PL
function. Then the following conditions are equivalent:
     ON SEMIPOSITIVE PIECEWISE LINEAR FUNCTIONS IN NON-ARCHIMEDEAN ANALYTIC GEOMETRY        17

   (1) The function h is semipositive (resp. pluriharmonic).
   (2) There is an algebraically closed analytic field extension F of k such that for every
       rig-smooth analytic curve C over F and every morphism ϕ : C → X F , the function
       h F ◦ ϕ is semipositive (resp. harmonic) on C.
   (3) There is an algebraically closed analytic field extension F of k such that for every
       smooth analytic curve C over F and every morphism ϕ : C → X F , the function h F ◦ϕ
       is semipositive (resp. harmonic) on C.

   If (2) or (3) is true for an algebraically closed analytic field extension F of k, then
it is true for all analytic field extensions. This follows from Corollary 5.4 and Propo-
sition [GJR21, Proposition 7.6(2’)] which allows to check semipositivity over any field
extension.

Proof. It is enough to prove the claim for semipositive functions, as h is pluriharmonic if
and only if h and −h are semipositive. Since semipositivity is stable under pullback and
extension of scalars [GJR21, Proposition 7.6], clearly (1) yields (2). Since a smooth an-
alytic curve is just a boundaryless rig-smooth curve, it is clear that (2) yields (3). In fact,
these two conditions are equivalent as an R-PL function is automatically semipositive in
every boundary point y of an analytic curve C. Indeed, it follows from 5.2 that red(C, y)
is non-proper and hence there is no condition for semipositivity at y.
   It remains to show that that (2) yields (1). Assume that (2) holds. By base change
using [GJR21, Proposition 7.6(2’)], we may assume that k = F . Let x ∈ X and let U be
a strictly analytic neighborhood of x. For any Zariski-closed curve Y in U, we will show
that h|Y is semipositive. Replacing Y by Yred and using [GJR21, Proposition 7.6(3’)], we
may assume that Y is reduced. Let ϕ : C → Y be the normalization of Y (see [Ber90]
before Proposition 3.1.8). Then C is a rig-smooth curve because k is perfect (it is alge-
braically closed). By (2), the function h ◦ ϕ is semipositive on C. Since the normalization
morphism is finite and surjective, it follows from [GJR21, Proposition 7.6(1’)] that h|Y is
semipositive. By Theorem 5.3, we conclude that h is semipositive at x. Since x was an
arbitrary point of X , we get (1).                                                           
Corollary 5.5. Let X be a good, strictly k-analytic space and let Λ be either Z or Q. Let
h1 , h2 : X → R be semipositive Λ-PL functions. Then max(h1 , h2 ) is a semipositive Λ-PL
function.

  Corollary 5.5 fails for Λ strictly containing Q, but only because we restrict ourselves to
the G-topology generated by strictly analytic domains. See [GJR21, Example 5.3].

Proof. We first note that max(h1 , h2 ) is a Λ-PL function [GJR21, Remark 5.2]. Using
Corollary 5.4, it is enough to prove that max(h1 , h2 ) is semipositive in case of a smooth
analytic curve X . Since the maximum of two subharmonic functions on such a curve is
subharmonic [Thu05, Proposition 3.1.8], the claim follows from Proposition 5.1.          

Theorem 5.6. Let X be a good, strictly k-analytic space and let (h j ) j∈N be a sequence of
semipositive R-PL functions on X converging pointwise to an R-PL function h. Then h is
semipositive.
18                                    W. GUBLER AND J. RABINOFF

  For Q-PL functions on the analytification of a proper algebraic variety over K, this was
shown in [GM19, Theorem 1.3]. The weaker statement assuming uniform convergence
was proven in [GK19, Proposition 7.2].

Proof. We can check semipositivity after extending scalars [GJR21, Proposition 7.6(2’)],
so we may assume that k is algebraically closed. By Corollary 5.4, we may assume that
X is a smooth analytic curve. Fix a point x ∈ X ; we must show that h is semipositive
at x. Since X is locally algebraic by a result of van der Put [vdP80], we may assume
that X is an open subset of C an for a proper algebraic curve C over k. Replacing X by
the interior of a compact neighborhood of x, we may assume that all h j and h extend to
R-PL functions e h j and eh on C an ([GK19, Proposition 5.11], [GM19, Proposition 2.7]). An
R-PL function e h on C an is the same as a metric on OC an associated to a model L with R-
coefficients [GM19, Proposition 2.10]; we denote the associated formal metric by k keh .
This allows us to use the theory of local heights from [Gub07, §3]. Passing to a dominant
model, we may assume that L is a line bundle with R-coefficients on a formal model C
of C with reduced special fiber, as explained in [GJR21, §2.4]. Then, by definition, the
Chambert-Loir measure c1 (OC , e    h) associated to eh (and L) is the discrete measure on C an
                                     an
supported on the points z ∈ C reducing to generic points of Cs ; we call such points
divisorial points. The multiplicity at a divisorial point z is degL (Z), where Z is the closure
of redC (z) in Cs . These measures were introduced by Chambert-Loir in [CL06]; for the
current setting with formal metrics, we refer to [Gub07, §3].
   We want to prove semipositivity of h on the open subset X of C an . It is equivalent to
show that the Chambert–Loir measure c1 (OC , e      h) has positive multiplicity in every divi-
sorial point x ∈ X associated to C: see [GK19, Lemma 6.8] or the proof of Proposition
5.1.
   Suppose now that x is a divisorial point in X associated to C. By [GM19, Lemma 2.13],
there is a Q-PL function ϕ on C an with ϕ(x) = 1 and with support contained in an open
neighborhood W of x contained in X and not containing any other divisorial points z 6= x.
Using that Q-PL functions are stable under minimum and maximum [GM19, Proposition
2.12], we may assume 0 ≤ ϕ ≤ 1.
   Let m be the multiplicity of c1 (OC , eh) at x. We have
                                            Z
                                        m=       ϕ c1 (OC , e
                                                            h)
                                              C an

by the choice of ϕ. The right hand side is the local height of C with respect to two
metrized line bundles (OC , k kϕ ) and (OC , k keh ) using the canonical section 1 (and the
corresponding trivial Cartier divisor) for the line bundles [Gub07, 3.8]. Here the metric
k kϕ is determined by − log k1kϕ = ϕ, and similarly for e        h. Now symmetry of the local
heights [Gub07, Proposition 3.9] based on commutativity of intersection numbers on
formal models [Gub98, Theorem 5.9] gives the integration by parts formula
                            Z                   Z
                                ϕ c1 (OC , e
                                           h) =      eh c1 (OC , ϕ).
                               C an                  C an
     ON SEMIPOSITIVE PIECEWISE LINEAR FUNCTIONS IN NON-ARCHIMEDEAN ANALYTIC GEOMETRY         19

In [CD12, §6], a Monge–Ampère measure was introduced for PL-metrics based on a local
analytic construction. It was shown in [CD12, §6.9] and in [GK17, Theorem 10.5] that
this Monge–Ampère measure agrees with the corresponding Chambert-Loir measure and
hence the latter is local in the Berkovich topology. We conclude that c1 (OC , ϕ) is a finite
discrete measure on C an with support contained in W ⊂ X , so we get
                           Z                          Z
                      m=         lim h j c1 (OC , ϕ) = lim           h j c1 (OC , ϕ).
                                 j→∞                      j→∞
                             W                                   W

Now we do the same steps backwards with h j instead of h to deduce
                          Z                         Z
                 m = lim      e
                              h j c1 (OC , ϕ) = lim   ϕ c1 (OC , e
                                                                 h j ).
                          j→∞                             j→∞
                                  C an                           C an

Since ϕ ≥ 0 with support in X and since c1 (OC , h j ) restricts to a positive discrete measure
c1 (OX , h j ) on X as h j is semipositive on X , we obtain
                                              Z
                                 m = lim           ϕ c1 (OX , h j ) ≥ 0,
                                         k→∞
                                               X

proving the claim.                                                                           

                  6. THE BIERI–GROVES THEOREM FOR AFFINOID SPACES
   The Bieri–Groves theorem [BG84] shows that for every closed subscheme of pure di-
mension d in a multiplicative torus T of rank n over k, the tropicalization is a union of
d-dimensional (Z, Γ )-polyhedra in Rn . This was generalized to closed analytic subvari-
eties of polytopal subdomains of T in [Gub07]. Berkovich and Ducros generalized the
Bieri–Groves theorem to arbitrary analytic spaces, but the tropicalization then can be of
lower dimension. We give here the pure dimensionality of the tropical variety of an affi-
noid space away from the tropicalization of the boundary. The arguments rely crucially
on results of Ducros on the tropicalization of the germ of an analytic space and on tropical
skeletons.
   Let k be a non-trivially valued non-Archimedean field with valuation v and value group
Γ ⊂ R. In this section, we consider a compact strictly analytic space X over k. Note that
the strictness assumption on X and the non-triviality of v can be always achieved by base
change, so this is not really a restriction of generality as tropical varieties are invariant
under base change.
                                   n
6.1. Consider the split torus T = Gm = Spec k[χ1± , . . . , χn± ] of rank n over k for which we
have the tropicalization map
                      trop: Tan −→ Rn ,        x 7→ (|χ1 (x)|, . . . , |χn (x)|).

The classical Bieri–Groves theorem [BG84] shows that for any closed subvariety Y of T of
dimension d, the tropical variety Trop(Y ) := trop(Y an ) is a finite union of (Z, Γ )-polyhedra
of dimension d.
20                                 W. GUBLER AND J. RABINOFF

6.2. A morphism ϕ : X → Tan to the split torus T = Gm
                                                    n
                                                      with character lattice M = Zn is
called a moment map. Then
                                 ϕtrop := trop ◦ϕ : X −→ Rn
is called a smooth tropicalization. Such maps are at the core in the theory of Chambert–
Loir and Ducros [CD12] of real valued (p, q)-forms on X . Results of Berkovich and Ducros
show that the tropical variety ϕtrop (X ) is a finite union of (Z, Γ )-polyhedra of dimension at
most d: see [Duc12, Théorème 3.2]. Ducros shows in loc. cit. that ϕtrop (∂ X ) is contained
in a finite union of (Z, Γ )-polytopes in Rn of dimension at most d − 1.
6.3. For x ∈ X , we have the completed residue field H (x). We denote by H            f(x) the
                                    f     •
residue field of H (x) and by H (x) the graded residue field of H (x), in the sense
of [Duc12]. We have a canonical homomorphism χ x : OX ,x → H (x); we let χ                ex• be
the composition of χ x with H (x) → H       f(x)• . Let M e (x) = {χex• (ϕ ∗u) | u ∈ M } and let
e • ( M(x))
K     e     be the graded subfield of the graded residue field H     f(x)• generated over K   e•
      e
by M(x).    We set as in [GJR21, 3.6]
                                                                 
                             dϕ (X , x) := tr.deg Ke •( M
                                                        e (x))/K
                                                               e• .

  A basic tool for the study of the tropical variety ϕtrop (X ) is the following local result of
Ducros.
Theorem 6.4 ([Duc12, Théorème 3.4]). For x ∈ X , there is a compact strictly ana-
lytic neighbourhood V (x) of x such that for all compact strictly analytic neighbourhoods
W ⊂ V (x) of x, the germs of the tropical varieties ϕtrop (W ) and ϕtrop (V (x)) agree at
ω = ϕtrop (x). We denote this germ at ω by ϕtrop (X , x). The following properties hold:
     (1) The germ ϕtrop (X , x) is a rational fan of dimension at most dϕ (X , x).
     (2) If x 6∈ ∂ X , then ϕtrop (X , x) has pure dimension dϕ (X , x).
     Next, we will recall the tropical skeleton of ϕ from [GJR21, Section 3].
6.5. Assume that X has pure dimension d. The tropical skeleton of ϕ is defined by
Sϕ (X ) := {x ∈ X | dϕ (X , x) = d}. By results of Ducros [Duc12], the tropical skeleton
is a closed subset of X consisting only of Abhyankar points and has a canonical piecewise
linear structure such that ϕtrop restricts to a surjective piecewise linear map Sϕ (X ) →
ϕtrop (X ) with finite fibers. We refer to [GJR21, Section 3] for details. For x ∈ Int(X ) =
X \ ∂ X , it follows from Theorem 6.4 that x ∈ Sϕ (X ) if and only if dim(ϕtrop (X , x)) = d.
     We are now ready to state our global pure dimensionality result for affinoid spaces.
Theorem 6.6. Let X = M (A ) be a strictly affinoid space over k of pure dimension d and
let ϕtrop : X → Rn be a smooth tropicalization map. Then the tropical variety ϕtrop (X ) has
pure dimension d at every point of ϕtrop (X ) \ ϕtrop (∂ X ).
  Note that one cannot drop the requirement that X be affinoid: indeed, if X is proper
then it is compact and has no boundary, but ϕtrop (X ) could have dimension zero.
Proof. Let ω ∈ ϕtrop (X ) \ ϕtrop (∂ X ). If there exists a point x of Sϕ (X ) contained in
  −1
ϕtrop (ω), then 6.5 shows dim ϕtrop (X , x) = d since x ∈ Int(X ), which implies that the


## Thu PDF pages 56-59

42



  Le as général s'obtient en re ouvrant Ys par des ouverts onnexes U ontenant au plus
un point singulier de Ys et pour lesquels il existe un morphisme étale pU : Y|U → S(a(U )),
a(U ) ∈ k◦ − {0} induisant un isomorphisme entre les polytopes entiers S(X|U ) et S(S(a(u))).
2
     La démonstration du théorème 2.2.10 est maintenant a hevée.
Proposition 2.2.21.  Soit         X une S - ourbe simplement semi-stable ; quelle que
soit l'extension non ar himédienne K/k, le morphisme anonique d'espa es analytiques
p K : Xη ⊗b k K → Xη envoie S(X ×S Spf(K ◦ )) dans S(X ) et l'appli ation induite est un
isomorphisme G-lo al de polyèdres entiers pondérés.
Démonstration. Les deux assertions de l'énon é sont démontrées si elles le sont pour ha une
des S - ourbes X|U , U par ourant un re ouvrement ouvert de Xs ; nous pouvons don supposer
qu'il existe un morphisme étale q : X → S(a) induisant un isomorphisme du polyèdre entier
S(X ) sur S(S(a)). Considérons le diagramme ommutatif
                                                           pK
                                         b kK
                                      Xη ⊗                        / Xη

                                     qη,K                                    qη
                                                                        
                                          b kK
                                    S(a)η ⊗                     / S(a)η ;
                                                           p′K

il a été noté au début de 2.2.1 que le morphisme p′K induit un isomorphisme du polyèdre entier
S(S(a) ×S Spf(K ◦ )) sur S(S(a)), d'où il dé oule que le morphisme pK dénit une appli ation
de S(X ×S Spf(K ◦ )) dans S(X ) qui est un morphisme de polyèdres entiers s'insérant dans le
diagramme ommutatif
                                                           pK
                                S(X ×S Spf(K ◦ ))                             / S(X )

                                    qη,K                                              qη
                                                                                 
                              S(S(a) ×S Spf(K ◦ )) ′                   / S(S(a)).
                                                           pK

Les è hes p′K et qη sont des isomorphismes et, d'après la proposition 2.2.20, la è he qη,K
est un isomorphisme G-lo al ; le morphisme pK : S(X ×S Spf(K ◦ )) → S(X ) est nalement un
isomorphisme G-lo al de polyèdres entiers.
     Nous é rirons S(X )K en lieu et pla e de S(X ×S Spf(K ◦ )).
  Il reste à vérier la ompatibilité ave les poids. Notons r : Xη → Xs et rK : Xη ⊗ b kK →
                
              ◦            e
 X ×S Spf(K ) s = Xs ⊗ek K les appli ations de rédu tion, qui s'insèrent dans le diagramme
 ommutatif :
                                             r
                                   Xη ⊗                e
                                      b k K K / Xs ⊗ e K
                                                     k
                                      pK                               pK
                                                                        e
                                                                  
                                       Xη              r
                                                                / Xs .

Considérons un point ξ de S0 (X ) et un élément t de Tξ S(X ), e dernier orrespondant à
un point singulier x
                   e de Xs ontenu dans la omposante irrédu tible de point générique r(ξ).
Étant donné un voisinage U de x  e dans X et un morphisme étale p : U → S(a), a ∈ k◦ ,
on peut restreindre U de telle sorte que x
                                         e soit l'unique point de la bre p−1 (p(e
                                                                                 x)) ; elle- i
est alors un κ(p(e      e
                 x)) = k-s héma ni et réduit (p est étale), de rang [κ(e     e
                                                                         x) : k]. La bre de
                                                                                                 43



(p ⊗ 1) : U ⊗S Spf(K ◦ ) → S(a) ⊗S Spf(K ◦ ) au-dessus du point singulier est, de même, un
Ke -s héma ni et réduit ; puisqu'il s'identie à p−1 (p(x)) ⊗e K                     x) : e
                                                                e , il est de rang [κ(e
                                                                        k
                                                                                           k] et don

                                                       X
                                    x) : e
                                 [κ(e    k] =                            e
                                                                  x′ ) : K].
                                                               [κ(e
                                                     e′ ∈p−1
                                                     x       e)
                                                          e (x
                                                         K


Cette dernière identité se réé rit sous la forme
                                          X                   X
                            wξ (t) =                                          wξ ′ (t′ ),
                                       ξ ′ ∈p−1       t′ ∈Tξ′ S(X )K ,t′ →t
                                             K (ξ)



  e qui établit que pK est un isomorphisme de polyèdres entiers pondérés ( f. remarque 1.2.3,
2).                                                                                         2
    La notation iK que nous employons dans le lemme suivant a été dénie en 2.1.3 (Extension
des s alaires ). Rappelons que, pour tout point x de X , s(x) est le degré de trans endan e de
             e
l'extension H(x)/  e
                   k ; x est dit de type (2) si et seulement si s(x) = 1.
Lemme 2.2.22.  Soit X         une S - ourbe simplement semi-stable.
   (i ) Étant donné un sous-ensemble ni Σ ⊂ S(X ), il existe une extension non ar himédienne
K/k et un é latement admissible Y → X ×S Spf(K ◦ ) tels que Y soit une Spf(K ◦ )- ourbe
simplement semi-stable et iK (Σ) ⊂ S0 (Y). L'extension K/k peut être hoisie nie (séparable)
si et seulement si tous les points de Σ sont de type (2).
   (ii ) Étant donné un ensemble ni Σ′ de points de type (2) ou (3) dans Xη , il existe une
extension nie (séparable) k′ /k et un é latement admissible Y ′ → X ×S Spf(k′ ◦ ) tels que Y ′
soit une Spf(k′ ◦ )- ourbe simplement semi-stable et ik′ (Σ′ ) ⊂ S(Y ′ ).
Démonstration. Traitons d'abord le as X = S(a).
(i) On peut supposer que l'ensemble Σ est réduit à un point x.
    Considérons une extension non ar himédienne K/k telle que |H(x′ )× | = |K × |, où x′ est le
point de S(S(a))K orrespondant à x dans l'identi ation anonique S(S(a))K = S(S(a)) ;
  ette extension peut être hoisie si (et seulement si) x est de type (2).
    Fixons b ∈ K × tel que |T0 (x′ )| = |b| ; |a| ≤ |b| ≤ 1 et l'é latement sur S ×S Spf(K ◦ ) de
l'Idéal (T0 , b)  inversible en dehors du point singulier de S(a)s  donne lieu à un morphisme
q : Z → S(a) ×S Spf(K ◦ ) tel que Z soit une Spf(K ◦ )- ourbe simplement semi-stable et
S0 (Z) = S0 (S(a)) ∪ {x′ }.
(ii) On peut de nouveau supposer Σ′ réduit à un point x. Si x ∈ S(S(a)), il n'y a rien
à démontrer ; sinon, le point x′ = τ (x) de S(S(a)) est tel que s(x′ ) = 1 et on vient de
prouver qu'il existe une extension nie k′ /k telle que le point de S(S(a))k′ orrespondant à
x′ dans l'identi ation anonique S(S(a))k′ = S(S(a)) appartienne à S0 (S(a) ×S Spf(k′ ◦ )).
On est ainsi ramené au as d'un point x tel que τ (x) ∈ S0 (S(a)). L'appli ation de rédu tion
S(a)η → S(a)s envoie x sur un point lisse x    e appartenant à la omposante irrédu tible de
point générique r(τ (x)).
   Le omplémentaire E de la omposante onnexe non bornée de S(a)η − {x} ⊂ A1k − {x} est
un disque fermé de point de Shilov x. Soit y un point dans E tel que l'extension κ(y)/k soit
nie, de polynme minimal f normalisé de telle sorte que |f (τ (x))| = 1 ; hoisissons également
b ∈ k× tel que |f (x)| > |b|. L'Idéal I sur S(a) tel que Ixe = f OS(a),xe + bOS(a),xe et I = OS(a)
sur S(a)s − {ex} est admissible et son é latement q : Z → S(a) fournit une S - ourbe Z dont
44



la bre spé iale est la somme amalgamée du diagramme

                                          P1e
                                              Ok
                                          0

                                        Spec(e
                                             k)         e
                                                        x
                                                            / S(a)s ,

qui devient simplement semi-stable après une extension nie k′ /k et telle que S(Z ×S Spf(k′ ◦ )
 ontienne le sous-ensemble ik′ (x).
   Le as d'une ourbe simplement semi-stable quel onque se déduit dire tement de e qui
pré ède. On peut en eet supposer que X est munie d'un morphisme étale p : X → S(a) ar
la question est lo ale sur Xη .
   Étant donnée une extension non-ar himédienne (resp. une extension nie) K/k telle
qu'il existe un é latement admissible q : Z → S(a) ×S Spf(K ◦ ) satisfaisant à la ondition
iK (pη (Σ)) ⊂ S0 (Z) (resp. iK (Σ) ⊂ S(Z)), l'é latement admissible q ′ : Y → X ×S Spf(K ◦ )
déni par le diagramme artésien
                                          q′
                                    Y               / X ×S Spf(K ◦ )

                                                                 p
                                                            
                                    Z              / S(a) ×S Spf(K ◦ )
                                              q

fournit une S - ourbe simplement semi-stable Y telle que iK (Σ) ⊂ S0 (Y) (resp. iK (Σ) ⊂
S(Z ′ )).
  L'extension K/k peut être hoisie nie si tous les points de pη (Σ) sont de type (2), don si
tous les points de Σ sont de type (2).
     Toutes les extensions nies peuvent être hoisies séparables.                             2
   La proposition suivante sera utilisée au hapitre 3 ( f. théorème 3.2.10).
Proposition 2.2.23.  Soit Y un espa e k -anoïde rig-lisse de dimension 1. Toute om-
posante onnexe Ω de Int(Y ) et la réunion d'une suite de domaines k-anoïdes telle que, pour
tout n :
- Vn ⊂ Vn+1 − ∂Vn+1 ;
- la frontière de haque omposante onnexe de Vn+1 − Vn ne ren ontre Vn (resp. Vn+1 ) qu'en
un seul point.
Démonstration. Si l'on dispose d'une telle suite après une extension non ar himédienne
K/k, son image par la proje tion anonique p : Y ⊗ b k K → Y satisfait aux onditions imposées
 ar p(∂(V ⊗ b k K)) = ∂V pour tout domaine k-anoïde V ([3℄, proposition 3.1.3, (iv)). Nous
pouvons don supposer que Y est un domaine sri tement k-anoïde, bre générique d'une
S - ourbe simplement semi-stable Y .
   La omposante onnexe Ω de Y = Yη est l'image ré iproque par l'appli ation de rédu tion
r : Yη → Ys d'un sous-s héma fermé (réduit) Z de Ys , propre sur e   k et onnexe. Les points
de ∂Ω sont en bije tion ave l'ensemble des points génériques des omposantes irrédu tibles
anes de Ys ren ontrant Z .
   L'interse tion Ω ∩ S(Y) est un ouvert de S(Y). Elle est vide si et seulement si Z est un
point fermé lisse de Ys et la on lusion est dans e as immédiate puisque Ω est la réunion
d'une suite roissante de domaines stri tement k-anoïdes ayant un unique point de Shilov
                                                                                                  45



( orollaire 2.2.12). Si Ω ∩ S(Y) est non vide, il dé oule immédiatement de la onstru tion de
S(Y)) que
                                      Ω = τ −1 (Ω ∩ S(Y));
il ne reste alors plus qu'à dénir les domaines k-anoïdes désirés par :
                                          Vn = τ −1 (Sn ),
où (Sn ) est une suite roissante de domaines polyédraux ompa ts de réunion S telle que, pour
tout n, les omposantes onnexes de Sn+1 − Sn soient des polytopes entiers de dimension 1.
2

2.2.4. Polygones de Newton généralisés
   La notion lassique de polygone de Newton d'une série de Laurent à oe ients dans k per-
met l'étude des fon tions holomorphes sur les ouronnes {r ≤ |T1 | ≤ R} ⊂ Gmk , 0 < r < R,
lesquelles sont essentiellement les bres génériques des S - ourbes S(a) ( f. [Man℄, hapter 1,
par exemple). La onstru tion du squelette d'une S - ourbe simplement semi-stable X fournit
le adre d'une généralisation évidente pour les éléments f de Γ(Xη , OXη ), ledit polygone de
Newton n'étant autre que le graphe de la fon tion réelle log |f ||S(X ) .

Proposition 2.2.24.  Soient X une S - ourbe simplement semi-stable, de bre générique
X = Xη , et f une se tion globale de OX , inversible sur un ouvert dense de X .
   (i ) La restri tion F de la fon tion log |f | à S(X ) ⊂ X est ane par mor eaux : F ∈
A0Z (S(X )).
   (ii ) Pour tout point x ∈ S(X ), log |f | ≤ F (x) sur τX−1 (x), ave égalité si et seulement si f
ne s'annule pas sur τX−1 (x) ; ainsi, la fon tion F ◦ τX majore log |f | sur X , et il y a égalité si
et seulement si f ∈ Γ(X, OX )× .
   (iii ) Pour tout x ∈ S(X ) − ∂X , le oe ient de δx dans ddc F est le degré du diviseur
div(f )|τ −1 (x) ; la mesure induite par ddc F sur S(X )−∂X est don positive et F est harmonique
        X
sur S(X ) − ∂X si et seulement si f est inversible sur l'ouvert τ −1 (S(X ) − ∂X) de X .
Démonstration. Observons tout d'abord que la fon tion log |f | prend des valeurs nies sur
S(X ) ⊂ X : en eet, f étant génériquement inversible, elle ne peut s'annuler qu'en des points
x ∈ X tels que |κ(x) : k] < ∞ et la on lusion dé oule de e que l'extension κ(x)/k est
trans endante pour tout point x ∈ S(X ).
   Le support du diviseur de f étant un fermé lo alement ni de X , son image Σ par l'appli-
  ation propre τX est un fermé lo alement ni de S(X ) tel que s(x) = 1 pour tout x ∈ Σ ;
il existe alors, par appli ation du lemme 2.2.22, une extension nie k′ /k et un é latement
admissible q : Y → X ×S Spf(k′ ◦ ) tel que Y soit une Spf(k′ ◦ )- ourbe simplement semi-stable
et q −1 (Σ) ⊂ S0 (Y). Posons S ′ = Spf(k′ ◦ ) ; le morphisme anonique p : Xη ⊗k k′ → Xη induit
un isomorphisme G-lo al entre les poyèdres entiers pondérés S(X ×S S ′ ) et S(X ) (proposition
2.2.21) et
                                       ddc F = p∗ ddc p∗ F
(remarque 1.2.8, 4). Il est don susant de démontrer la proposition pour p∗ f ∈ Γ(X ⊗k
k′ , OX⊗k k′ ), e qui permet de supposer que Σ est ontenu dans S0 (X ) ou, de manière équiva-
lente, que l'image du support de div(f ) par l'appli ation de rédu tion X → Xs est disjointe
du lieu singulier Sing(Xs ) de Xs .
  Soit, pour tout point x e ∈ Sing(Xs ), Uxe un voisinage ouvert onnexe de x      e dans
Xs − r(|div(f )|) tel que U − {e
                               x} soit lisse ; f étant inversible sur ha un des domaines


## Thu PDF pages 65-68

                                                                                               51



et l'égalité
                            Z                               Z
                                     c      ∗
                                   dd S(f ) Φ = (degx f )                 ddc Φ
                             {x}                                {f (x)}

pour toute fon tion Φ ∈ A0 (S(Y)) s'en déduit immédiatement par linéarité.
    Le as général se déduit du pré édent en appliquant la proposition 2.2.21 et le lemme 2.2.22.
2


                                   2.3. Fon tions harmoniques
2.3.1. L'espa e H(X ).
   Étant donnée une S - ourbe X , le bord de l'espa e k-analytique Xη (2.1.2) est le sous-
ensemble ∂Xη de S0 (X ) formé des points au-dessus des points génériques des omposantes
irrédu tibles anes de Xs .
Définition 2.3.1.  Soit X une S - ourbe simplement semi-stable ; le sous-espa e ve toriel

                                           τX∗ H(S(X ), ∂Xη )
de C0 (|Xη |, R) est noté H(X ).

   Nous nous restreindrons, dans e qui suit, à la onsidération de S - ourbes simplement
simplement semi-stables X qui sont quasi- ompa tes ; ette hypothèse équivaut à la ompa ité
de l'espa e topologique |Xη |.
Proposition 2.3.2
  (i ) Lorsque la e
                  k- ourbe Xs est propre, H(X ) est l'espa e des fon tions réelles lo alement
 onstantes sur Xη .
  (ii ) Lorsque ∂Xη ren ontre haque omposante onnexe de |Xη |, l'appli ation de restri tion
                                         H(X ) → Hom(∂Xη , R)
est bije tive.
Démonstration.
(i) Si la e
          k- ourbe Xs est propre, l'ensemble ∂Xη est vide ; l'assertion dé oule don du orollaire
1.2.11.
(ii) Si l'ensemble ∂Xη ren ontre ha une des omposantes onnexes de |Xη |, il ren ontre éga-
lement haque omposante onnexe de S(X ) (remarque 2.2.19,3) et l'assertion dé oule de la
proposition 1.2.15.                                                                           2

    Comme annon é en introdu tion de e hapitre, nous allons établir le résultat suivant.
Proposition 2.3.3.  Soient X , X
                                       ′ deux S - ourbes simplement semi-stables et f : X ′ →
                                                                                             η
Xη un morphisme quasi-ni. L'appli ation R-linéaire f ∗ : C0 (|Xη |, R) → C0 (|Xη′ |, R) envoie le
sous-espa e H(X ) dans le sous-espa e H(X ′ ).
Démonstration. Vu la proposition 2.2.26, le résultat s'obtient en ombinant les trois lemmes
suivants.                                                                                       2
Lemme 2.3.4.  Soient X         une S - ourbe simplement semi-stable et q : Y → X un é late-
ment admissible tel que Y soit une S - ourbe simplement simplement semi-stable ; l'isomor-
                            ∼
phisme qη∗ : C0 (|Xη |, R) −→ C0 (|Yη |, R) identie les sous-espa es H(X ) et H(Y).
52



Démonstration. L'isomorphisme qη identie ∂Yη et ∂Xη .
  D'après la proposition 2.2.26, le polyèdre entier S(X ) s'identie à un domaine polyédral
dans le polyèdre entier S(Y) tel que, posant S(q) = τX ◦ qη |S(Y) , le diagramme
                                                    τY
                                           Yη            / S(Y)

                                       qη                           S(q)
                                                               
                                           Xη       τX
                                                         / S(X )

soit ommutatif, haque omposante onnexe de S(Y) − S(X ) ne ren ontre S(X ) qu'en un
seul point et l'appli ation S(q) soit la rétra tion envoyant ha une de es omposantes sur le
point orrespondant de S(X ).
   Les espa es k-analytiques Yη et Xη sont identiés via l'isomorphisme qη ; on déduit du
diagramme ommutatif pré édent que, pour toute fon tion F sur S(X ), la fon tion f = F ◦τX
sur Xη = Yη se fa torise par τX sous la forme :
                                     f = (F ◦ S(q)) ◦ τY .
L'appli ation linéaire
                              S(q)∗ : A0 (S(X )) → A0 (S(Y))
induisant un isomorphisme de H(S(X ), ∂Xη ) sur H(S(Y), ∂Yη ) (proposition 1.2.20), il en
résulte que l'isomorphisme anonique de C0 (|Xη |, R) sur C0 (|Yη |, R) envoie le sous-espa e
H(X ) dans H(Y) et induit un isomorphisme de l'un sur l'autre.                            2
Lemme 2.3.5.  Soient X         une S - ourbe simplement semi-stable (quasi- ompa te ) et K/k
une extension non-ar himédienne ; une fon tion h ∈ C0 (|Xη |, R) appartient au sous-espa e
H(X ) si et seulement si la fon tion p∗K h appartient au sous-espa e H(X ×S Spf(K ◦ )).
Démonstration. Le morphisme anonique pK : Xη ⊗            b k K → Xη induit un isomorphisme
G-lo al surje tif S(X )K → S(X ) de polyèdres entiers pondérés (proposition 2.2.21) et, les
 omposantes irrédu tibles anes de la K   e - ourbe Xs ⊗e K   e étant les images ré iproques des
                                                           k
                                                             −1
 omposantes irrédu tibles anes de Xs , ∂(Xη ⊗  b k K) = pK (∂Xη )) ∩ S0 (X ×S Spf(K ◦ )). Ce i
implique, pour tout fon tion Φ ∈ A (S(X )), que la fon tion p∗K Φ appartient à A0 (S(X )K ) et
                                     0

que le support de la mesure ddc Φ = (pK )∗ ddc p∗K Φ est ontenu dans ∂Xη si et seulement si
 elui de la mesure ddc p∗K Φ est ontenu dans ∂(Xη ⊗  b k K).                                  2
Lemme 2.3.6.  Soient X , Y deux S - ourbes simplement semi-stables et f : Yη → Xη un
morphisme quasi-ni ; l'homomorphisme f ∗ : C0 (|Yη |, R) → C0 (|Xη |, R) envoie le sous-espa e
H(Y) dans H(X ).
Démonstration. Appliquant la proposition 2.2.27 et les deux lemmes pré édents, on peut
supposer que f induit un morphisme de Y dans X . On a alors un diagramme ommutatif
                                                    τX
                                       Xη                / S(X )

                                       f                            S(f )
                                                           
                                       Yη           τY
                                                         / S(Y),

où S(f ) = τY ◦ f est un morphisme de polyèdres entiers.
  Étant donnée une fon tion H dans H(S(Y), ∂Yη ),
                                  f ∗ (H ◦ τY ) = S(f )∗ H ◦ τX
                                                                                                53



et S(f )∗ H ∈ A0 (S(X )). Il reste à vérier que la fon tion S(f )∗ H est harmonique sur S(X ) −
∂Xη . C'est une onséquen e dire te du point (iv) de la proposition 2.2.27 : f (x) ∈ / ∂Yη pour
tout point x ∈ S(X ) − ∂Xη et
                         Z                              Z
                               ddc S(f )∗ H = (degx f )       ddc H = 0.
                          {x}                             {f (x)}
                                                                                                 2
  Si X est un espa e stri tement k-anoïde et ϕ : X → ˜ Xη est un isomorphisme de X sur la
bre générique d'une S - ourbe simplement semi-stable X , le sous-espa e ve toriel réel ϕ∗ H(X )
de C0 (|X|, R) ne dépend pas du hoix de X et de ϕ ; il est noté H(X).
   De manière générale, étant donnés un espa e k-analytique X et une lture algébrique ka de
k, le groupe de Galois G de la fermeture séparable ksep de k dans ka opère par automorphismes
sur l'espa e c                b kc
             ka -analytique X ⊗  ka . On dispose d'un morphisme G-équivariant anonique
                                          p : X⊗  ca → X
                                               b kk
d'espa es analytiques et l'appli ation ontinue sous-ja ente est un quotient de |X ⊗        ca | par
                                                                                        b kk
l'a tion de G dans la atégorie des espa es topologiques : 'est en eet un quotient dans la
  atégorie des ensembles d'après le orollaire 1.3.6 de [3℄ et l'appli ation ontinue p est ouverte.
Proposition 2.3.7.  Quelles que soient la S - ourbe simplement semi-stable X et l'ex-
tension nie galoisienne k′ /k, l'a tion du groupe G = Gal(k′ /k) sur C0 (|Xη ⊗k k′ |, R) stabilise
le sous-espa e H(Xη ) et l'isomorphisme anonique
                                 C0 (|Xη |, R) → C0 (|Xη ⊗k k′ |, R)G
induit un isomorphisme de H(Xη ) sur H(Xη ⊗k k′ )G .
Démonstration. On peut supposer Xη onnexe.
   Si Xη est propre, H(Xη ) (resp. H(Xη ⊗k k′ )) est l'espa e des fon tions onstantes sur Xη
(resp. lo alement onstantes sur Xη ⊗k k′ ) (proposition 2.3.2, 1) et l'assertion est évidente.
   Si Xη n'est pas propre, alors il en est de même pour haque omposante onnexe de Xη ⊗k k′
et, d'après la proposition 2.3.2,2, les restri tions
                                      H(Xη ) → Hom(∂Xη , R)
et
                                H(Xη ⊗k k′ ) → Hom(∂(Xη ⊗k k′ , R)
sont bije tives. L'assertion résulte ainsi de l'identité ∂Xη = ∂(Xη ⊗k k′ )G .                   2

2.3.2. Le théorème de rédu tion semi-stable.
   C'est i i qu'intervient le théorème de rédu tion semi-stable.
Théorème 2.3.8.  Soit X un espa e stri tement k -anoïde purement de dimension 1
et rig-lisse ; il existe une extension nie séparable k′ de k telle que le domaine k′ -anoïde
X ⊗k k′ soit isomorphe à la bre générique d'une Spf(k′ ◦ )- ourbe simplement semi-stable.
Démonstration. Il existe une extension nie séparable k1 de k et une ourbe algébrique C
propre et lisse sur k1 telles que X ⊗k k1 soit isomorphe à un domaine anoïde de C ([31℄,
theorem 1). Appliquant le théorème de rédu tion semi-stable sous la forme rigide-analytique
établie par S. Bos h et W. Lütkebohmert dans [9℄, il existe une extension nie séparable k′
de k1 telle que C ⊗k1 k′ soit isomorphe à la bre générique d'une Spf(k′ ◦ )- ourbe C dont la
bre spé iale est simplement semi-stable ; 'est automatiquement une S - ourbe semi-stable
54



(remarque 2.2.9, 3). En hoisissant onvenablement k′ , on peut en outre supposer que tout
point x du bord de X ⊗k k′ satisfait à la ondition |κ(x)× | = |k′ × |.
    Envisageons X ′ = X ⊗k k′ omme un domaine stri tement k′ -anoïde de Cη et soit q :
C ′ → C un é latement admissible tel que C ′ soit une Spf(k′ ◦ )- ourbe simplement semi-stable,
ave ∂X ′ ⊂ S0 (C ′ ) (lemme 2.2.22). L'image de X ′ par l'appli ation de rédu tion Cη′ → Cs
est un ouvert U et X ′ est isomorphe à la bre générique de la Spf(k′ ◦ )- ourbe simplement
semi-stable X = C|U′ .                                                                       2
  Soient X un espa e stri tement k-anoïde purement de dimension 1 rig-lisse et k′ , k′′ deux
extensions nies galoisiennes de k telles que X ⊗k k′ et X ⊗k k′′ soient isomorphes aux bres
génériques de ourbes stri tement semi-stables ; étant donnée une extension nie galoisienne
K de k oiant k′ et k′′ , la proposition 2.3.7 implique l'identité des espa es H(X ⊗k k′ ) et
                   ′                                          ′′
H(X ⊗k K)Gal(K/k ) (resp. H(X ⊗k k′′ ) et H(X ⊗k K)Gal(K/k ) ), d'où dé oule l'égalité
                               ′                                              ′′
              H(X ⊗k k′ )Gal(k /k) = H(X ⊗k K)Gal(K/k) = H(X ⊗k k′′ )Gal(k /k) .
Le théorème pré édent permet ainsi de dénir, pour tout espa e stri tement k-anoïde X
purement de dimension 1 et rig-lisse, un sous-espa e ve toriel H(X) de C0 (|X|, R) : H(X) =
                ′
H(X ⊗k k′ )Gal(k /k) ⊂ C0 (|X|, R), k′ étant une extension nie galoisienne de k telle que X ⊗k k′
soit isomorphe à la bre générique d'une Spf(k′ ◦ )- ourbe simplement semi-stable.
   Désignant par C la atégorie dont les objets sont les espa es stri tement k-anoïdes, pure-
ment de dimension 1 et rig-lisses, et les morphismes les immersions anoïdes, il dé oule de la
proposition 2.3.3 que l'on vient ainsi de dénir un fon teur H sur Cop à valeurs dans VectR .
  Nous aurons besoin des deux résultats suivants.
Lemme 2.3.9.  Pour tout espa e stri tement k -anoïde Y rig-lisse et purement de di-
mension 1, l'appli ation de restri tion
                                   C0 (|Y |, R) → Hom(Γ(Y ), R)
induit un isomorphisme du sous-espa e H(Y ) sur Hom(Γ(Y ), R).
Démonstration. Soit k′ une extension galoisienne nie de k telle que l'espa e stri tement
k′ -anoïde Y ⊗k k′ soit isomorphe à la bre générique d'une Spf(k′ ◦ )- ourbe simplement semi-
                                                                                            ′
stable Y . La proje tion anonique p : Y ⊗k k′ → Y induit une bije tion de Γ(Y ⊗k k′ )Gal(k /k)
sur Γ(Y ) et l'appli ation de restri tion
                                   C0 (|Y |, R) → Hom(Γ(Y ), R)
 oïn ide ave l'appli ation induite par la restri tion
                            C0 (|Y ⊗k k′ |, R) → Hom(Γ(Y ⊗k k′ ), R)
                                                                                           ′
entre les sous-espa es des invariants sous Gal(k′ /k) ; puisque H(Y ) = H(Y ⊗k k′ )Gal(k /k) , la
 on lusion dé oule de la proposition 2.3.2.                                                    2
Lemme 2.3.10.  Soient Y un espa e stri tement k -anoïde onnexe, de dimension 1 et
rig-lisse, et (hn ) une suite roissante de fon tions appartenant à H(Y ). L'alternative suivante
est vraie :
    soit la suite (hn ) onverge, uniformément sur Y , vers une fon tion h ∈ H(Y ),
    soit la suite (hn ) onverge, lo alement uniformément sur Y − Γ(Y ), vers ∞.
Démonstration. Soient k′ une extension nie galoisienne de k telle que Y ′ = Y ⊗k k′ soit
isomorphe à la bre générique d'une Spf(k′ ◦ )- ourbe simplement nodale Y′ et p : Y ′ → Y la
proje tion anonique. Si l'assertion est démontrée pour la suite (p∗ hn ) dans H(Y ′ ), elle l'est
                                                                      ′
également pour la suite (hn ) : en eet, puisque H(Y ) = H(Y ′ )Gal(k /k) , il sut de s'assurer


## Thu PDF pages 75-78

                                                                                              61



                              3. Théorie du potentiel



                              3.1. Le problème de Diri hlet
  Dans e qui suit, X est une ourbe stri tement k-analytique lisse.
3.1.1. Propriétés fondamentales des fon tions harmoniques.
  Les se tions du fais eau HX satisfont au prin ipe du maximum.
Proposition 3.1.1.  Étant donné un ouvert Ω de X , une fon tion h ∈ Γ(Ω, HX ) admet
un extremum lo al en un point x de Ω si et seulement si elle est onstante au voisinage de x.
  C'est la onjon tion de la proposition 2.3.13 et du orollaire 2.3.14.
   Le problème de Diri hlet est lo alement résoluble : tout point x ∈ X admet un système
fondamental de voisinages ouverts relativement ompa ts Ω tels que l'appli ation de restri tion
                              C0 (Ω, R) ∩ Γ(Ω, HX ) → C0 (∂Ω, R)
soit un isomorphisme. Il sut en eet de prendre pour Ω l'intérieur d'un voisinage stri tement
k-anoïde Y de x dans X et d'appliquer le lemme 2.3.9.
  Le prin ipe de Harna k est valide
Proposition 3.1.2.  Soient Ω un ouvert onnexe de X et (Ωn ) une suite d'ouverts de
X telle que haque point de Ω admette un voisinage ontenu dans presque tous les Ωn : quelle
que soit la suite roissante de fon tions hn ∈ Γ(Ωn , HX ), l'alternative est la suivante :
   soit (hn ) onverge vers +∞ uniformément sur tout ompa t de Ω,

   soit (hn ) onverge vers une fon tion h ∈ Γ(Ω, HX ), uniformément sur tout ompa t de
     Ω.
Démonstration. Puisque tout point de x admet un système fondamental de voisinages stri -
tement k-anoïdes, il dé oule du lemme 2.3.10 que l'ensemble U (resp. U ′ = Ω−U ) des points
de Ω en lesquels la suite (hn ) est majorée (resp. n'est pas majorée) est une partie ouverte ; de
plus, toujours par appli ation de e lemme, la suite (hn ) onverge
   lo alement uniformément vers ∞ sur U ′ ;
   lo alement uniformément sur U vers une fon tion h  né essairement ontinue  telle que,
     pour tout domaine stri tement k-anoïde Y de Ω, la restri tion de h à Y appartienne à
     H(Y ) ; vu la dénition du fais eau HX (2.3.3), la fon tion h est harmonique sur Ω.
                                                                                               2
   Notons également le résultat de onvergen e suivant :
Proposition 3.1.3.  Soient Ω un ouvert de X et (hn ) une suite de fon tions harmo-
niques sur Ω ; si la suite (hn ) est lo alement bornée, on peut en extraire une sous-suite onver-
geant, lo alement uniformément sur Ω, vers une fon tion harmonique.
Démonstration. Nous démontrerons au orollaire 3.3.7 que toute famille lo alement bornée
de fon tions harmoniques sur Ω est automatiquement équi ontinue en tout point de Ω ; bien
entendu, la proposition ne sera pas utilisée d'i i là. Appliquant le théorème d'As oli, on peut
extraire une sous-suite de (hn ) qui onverge lo alement uniformément.
   Il est fa ile de vérier qu'une limite lo alement uniforme de fon tions harmoniques est
harmonique : pour tout domaine k-anoïde V de X , le sous-espa e Γ(V − ∂V ) ∩ C0 (V, R) de
l'espa e de Bana h C0 (V, R) est fermé ar 'est un espa e ve toriel de dimension nie.          2
62



Remarque 3.1.4.  Puisque, pour tout domaine stri tement k-anoïde Y , l'espa e ve to-
riel H(Y ) est de dimension nie, la limite h d'une suite simplement onvergente de fon tions
harmoniques sur un ouvert Ω de X est harmonique et la onvergen e est lo alement uniforme
sur Ω.

  Les propriétés du fais eau HX énon ées dans les trois paragraphes pré édents permettent,
en re opiant les démonstration du paragraphe 2.2 du hapitre V de [Ahl℄, de résoudre le
problème de Diri hlet par la méthode de Perron ; e i est l'objet de la n de la se tion 3.1.

3.1.2. Fon tions sous-harmoniques.
Définition 3.1.5.  Soit Ω un ouvert de X ; une fon tion u : Ω → R ∪ {−∞} est dite
sous-harmonique si elle est semi- ontinue supérieurement, n'est identiquement égale à −∞
sur au une omposante onnexe de Ω et satisfait à la ondition suivante : pour tout domaine
stri tement k-anoïde Y dans X et toute fon tion h ∈ H(Y ),
                                  (u|∂Y ≤ h|∂Y ) =⇒ (u|Y ≤ h).

     L'assertion suivante n'est pas surprenante.
Proposition 3.1.6.  Soient Ω ⊂ X un ouvert et f ∈ Γ(Ω, OX ) une se tion inversible
sur un ouvert dense de Ω ; la fon tion log |f | est sous-harmonique sur Ω.
Démonstration. La fon tion log |f | est ontinue sur Ω et, f étant inversible sur un ouvert
dense, n'est identiquement égale à −∞ sur au une des omposante onnexes de Ω.
   Soient Y ⊂ Ω un domaine stri tement k-anoïde et h ∈ H(Y ) une fon tion majorant log |f |
sur Γ(Y ) = ∂Y ; puisqu'il sut de prouver l'inégalité log |f ||Y ≤ h après avoir ee tué une
extension nie k′ de k, nous pouvons supposer que Y est la bre générique d'une S - ourbe
simplement semi-stable Y , de squelette S(Y) et de rétra tion τY : Y → S(Y). Dans es
 onditions :
    H = h|S(Y) ∈ H(S(Y), Γ(Y )) et h = H ◦ τY ;
    la fon tion F = log |f ||S(Y) est sous-harmonique sur S(Y) − Γ(Y ) (proposition 2.2.24,
     (iii)) et log |f ||Y ≤ F ◦ τY (proposition 2.2.24, (ii)) ;
la on lusion dé oule alors de l'inégalité F ≤ H sur S(Y).                                  2
Remarque 3.1.7.  Nous verrons plus loin (proposition 3.4.6) que, pour toute S - ourbe
simplement semi-stable X et toute fon tion sous-harmonique u sur Xη − Γ(Xη ), la restri tion
U de u à S(X ) − Γ(Xη ) est sous-harmonique (= onvexe) : ddc U ≥ 0, l'opérateur ddc étant
entendu au sens des ourants, omme expliqué à en 1.2.5.

     Les propriétés suivantes des fon tions sous-harmoniques sont évidentes.
Proposition 3.1.8.  Étant donné un ouvert Ω de X ,
   (i ) l'ensemble des fon tions sous-harmoniques sur Ω est un ne réel stable par max : pour
toutes fon tions u, v sous-harmoniques sur Ω et tous nombres réels positifs µ, ν , les fon tions
µu + νv et max(u, v) sont sous-harmoniques sur Ω ;
   (ii ) l'enveloppe inférieure d'une famille dé roissante de fon tions sous-harmoniques sur Ω
est, sur ha une des omposantes onnexes de Ω, sous-harmonique ou identiquement égale à
−∞ ;
   (iii ) la régularisation semi- ontinue supérieurement de l'enveloppe supérieure d'une famille
 roissante et lo alement bornée de fon tions sous-harmoniques sur Ω est sous-harmonique.

     Le ne des fon tions sous-harmoniques sur un ouvert Ω de X est noté SH(Ω).
                                                                                               63



Lemme 3.1.9.  Soit Y     un domaine stri tement k-anoïde onnexe dans X ; toute fon -
tion sous-harmonique u sur un voisinage de Y prend des valeurs nies aux points de Γ(Y ) =
∂Y .

Démonstration. Raisonnons par l'absurde en supposant qu'il existe une fon tion sous-
harmonique u sur un voisinage Ω de Y prenant la valeur −∞ en un point x de Γ(Y ). Notant
M un majorant de u sur Γ(Y ), le lemme 2.3.9 fournit, pour tout entier naturel N , une fon tion
hN dans H(Y ) valant −N en x et égale à M sur Γ(Y ) − {x} ; la suite (hN ) est dé roissante et
 onverge, lo alement uniformément sur Y − Γ(Y ), vers −∞ par appli ation du lemme 2.3.10.
La restri tion de u à Y − Γ(Y ), majorée par hN pour tout N , est don identiquement égale
à −∞.
   Étant donné un domaine stri tement k-anoïde Y ′ dans X dont le bord de Shilov ren ontre
Int(Y ) = Y −Γ(Y ), le raisonnement pré édent implique u|Int(Y ′ ) = −∞. On onsidère alors un
re ouvrement lo alement ni V de la omposante onnexe de x dans Ω par des domaines stri -
tement k-anoïdes de X tel qu'il existe pour tout V ∈ V un domaine V ′ dans V satisfaisant à
la ondition : Γ(V ) ∩ Int(V ′ ) 6= ∅. D'après la première partie de la démonstration, la fon tion
u est identiquement égale à −∞ sur la omposante onnexe de x dans Ω, en ontradi tion
ave la dénition 3.1.5.                                                                         2

Remarque 3.1.10.  1. Le résultat pré édent sera étendu plus loin (3.4.10) au as d'un
domaine k-anoïde quel onque dans X .
2. Le lemme 3.1.9 permet de reformuler ainsi la dénition de la sous-harmoni ité : une fon -
tion semi- ontinue supérieurement u : Ω → R ∪ {−∞} est sous-harmonique si elle n'est pas
identiquement égale à −∞ sur une omposante onnexe de Ω et si, pour tout domaine stri te-
ment k-anoïde V in Ω, la fon tion h ∈ H(V ) qui oïn ide ave u sur Γ(V )  dont l'existen e
dé oule des lemmes 3.1.9 et 2.3.9  majore u sur tout Y . Cette dénition est équivalente à
la pré édente en vertu du prin ipe du maximum pour les fon tions harmoniques (proposition
3.1.1).

   Soit Ω un ouvert de X ; l'ensemble des points de Shilov des domaines stri tement k-
anoïdes de X étant partout dense, le lemme pré édent implique immédiatement que la
restri tion d'une fon tion sous-harmonique sur Ω à un ouvert Ω′ ⊂ Ω ne peut être identique-
ment égale à −∞ sur au une omposante onnexe de Ω′ . La orrespondan e Ω 7→ SH(Ω) est
par onséquent un préfais eau de nes réels sur |X|. Nous bientt qu'il s'agit en fait d'un
fais eau ( orollaire 3.1.13).
  Les fon tions sous-harmoniques satisfont au prin ipe du maximum suivant.

Proposition 3.1.11.  Étant donné un ouvert Ω de X , une fon tion sous-harmonique u
sur Ω admettant un maximum lo al en un point x de Ω est lo alement onstante au voisinage
de x.

Démonstration. Soit u une fon tion sous-harmonique admettant un maximum au point x
de Ω et soit U un voisinage ouvert onnexe de x dans Ω tel que u|U ≤ u(x) ; puisque u|U n'est
pas identiquement égale à −∞, u(x) > −∞.
   Soit Y un voisinage stri tement k-anoïde onnexe Y de x dans U . La restri tion de u à
Γ(Y ) est onstante, égale à u(x) : s'il existait, en eet, un point y ∈ Γ(Y ) tel que u(y) < u(x),
le lemme 2.3.9 fournirait une fon tion h ∈ H(Y ) telle que
    h(y) = u(y) ;
    h|Γ(Y )−{y} = u(x) ;
64



puisque Y est onnexe et h non onstante, le prin ipe du maximum pour les fon tions harmo-
niques impliquerait alors h|Y −Γ(Y ) < u(x) et don , par sous-harmoni ité, l'inégalité absurde
u(x) ≤ h(x) < u(x).
   La on lusion est maintenant immédiate : l'ensemble des points de Shilov des voisinages
stri tement k-anoïdes onnexes de x dans U étant une partie dense de U , la fon tion semi-
 ontinue supérieurement u|U est onstante, égale à u(x).                                     2

Corollaire 3.1.12.  Soient Ω ⊂ X un ouvert et u : Ω → R ∪ {−∞} une fon tion semi-
 ontinue supérieurement qui n'est identiquement égale à −∞ sur au une omposante onnexe
de Ω. Les propriétés suivantes sont équivalentes :
   (i ) u est sous-harmonique ;
   (ii ) pour tout ouvert Ω′ ⊂ Ω et pour toute fon tion harmonique h sur Ω′ , la fon tion u|Ω′ −h
satisfait au prin ipe du maximum (proposition 3.1.11) sur Ω′ .
Démonstration. L'impli ation (i) ⇒ (ii) est l'appli ation dire te de la proposition pré é-
dente puisque toute fon tion harmonique est sous-harmonique.
   L'impli ation ré iproque est immédiate : étant donnés un domaine stri tement k-anoïde
V ⊂ Ω et une fon tion h ∈ H(V ) telle que u|∂V ≤ h|∂V , l'appli ation du prin ipe du maximum
à la fon tion u − h sur v − ∂V implique que elle- i atteint son maximum en un point de ∂V ;
elle est don négative. La fon tion u est bien sous-harmonique sur Ω.                            2
   La reformulation pré édente de la dénition 3.1.5 met en éviden e le ara tère lo al de la
sous-harmoni ité.

Corollaire 3.1.13.  Le préfais eau SH sur |X| est un fais eau.

Démonstration. La semi- ontinuité supérieure et le fait de ne pas être identiquement −∞
sur une omposante onnexe sont des propriétés de nature lo ale. La propriété (ii) du orollaire
pré édent est également de nature lo ale.                                                  2

Proposition 3.1.14.  Soit X une ourbe stri tement k -analytique lisse. Étant donnés
une ourbe stri tement k-analytique lisse Y , un morphisme f : Y → X et une fon tion sous-
harmonique u sur X , la fon tion f ∗ u = u ◦ f est sous-harmonique ou identiquement égale à
−∞ sur haque omposante onnexe de Y .
Démonstration.
La ourbe Y peut être supposée onnexe et, l'assertion étant évidente pour un morphisme
 onstant, il sut de traiter le as d'un morphisme quasi-ni.
   Soit u une fon tion sous-harmonique sur X ; puisqu'il est loisible de se lo aliser sur Y pour
établir la sous-harmoni ité de f ∗ u, on peut supposer que le morphisme f est ni. Considérons
alors un domaine stri tement k-anoïde V ⊂ Y et une fon tion h dans H(V ) qui oïn ide
ave f ∗ u sur ∂V = Γ(V ) ; W = f (V ) est un domaine stri tement k-anoïde dans X tel que
f −1 (∂W ) = ∂V en vertu des proposition 3.1.3 (ii) et orollaire 2.5.13 (i) de [3℄ (la première
implique ∂V = f −1 (∂W ) ∩ (V − Int(f )), la se onde fournit l'égalité Int(f ) = V ).
   Soit h′ la fon tion dans H(W ) qui oïn ide ave u sur ∂W . La fon tion f ∗ h′ appartient à
H(f −1 (W )) (proposition 2.3.19) et est égale à h sur ∂f −1 (W ) = ∂V ; le prin ipe du maximum
implique alors l'identité h = f ∗ h′ , d'où dé oule l'inégalité
                                        f ∗ u ≤ f ∗ h = h′
en vertu de la sous-harmoni ité de u.                                                          2

Remarque 3.1.15.  Soit Ω un ouvert relativement ompa t de X ; toute fon tion sous-
harmonique u sur Ω se prolonge de façon unique en une fon tion semi- ontinue supérieurement


## Thu PDF pages 82-85

68



Démonstration. Il sut d'appliquer les deux propositions pré édentes à l'ouvert relative-
ment ompa t Int(Y ) ⊂ X .                                                                     2


                            3.2. Fon tions lisses, opérateur ddc
   Disposant du fais eau HX des germes de fon tions harmoniques sur une ourbe stri tement
k-analytique lisse X et de la résolution partielle du problème de Diri hlet obtenue à la se tion
pré édente, nous allons maintenant dénir les fais eaux A0X (resp. A1X ) des germes de fon tions
lisses (resp. formes lisses ) sur X et un  opérateur de Lapla e  ddc : A0X → A1X ; elui- i
sera lassiquement étendu à des espa es de distributions dans la se tion suivante.

   Désignons par I(X) l'ensemble des points de X de type (2) ou (3) ; de manière équivalente,
I(X) est l'ensemble des points de Shilov des domaines k-anoïdes de X . Plus pré isément :
le bord de Shilov Γ(Y ) d'un domaine k-anoïde Y de X est un sous-ensemble ni de I(X) et
toute partie nie S de I(X) est la réunion des bords de Shilov d'un nombre ni de domaines
k-anoïdes.

3.2.1. Les fais eaux A0X et A1X sur XG .
     Dans e qui suit, X désigne une ourbe stri tement k-analytique lisse.
Définition 3.2.1.  Soit Ω ⊂ X un ouvert.
   (i ) Une fon tion réelle ϕ ∈ C (Ω, R) est dite lisse s'il existe un re ouvrement lo alement
                           0

ni V de Ω par des domaines k-anoïdes Y tel que ϕ|Y ∈ H(Y ). L'ensemble des fon tions
lisses sur Ω est un sous-espa e ve toriel de C0 (Ω, R), noté A0 (Ω).
   (ii ) On désigne par A1 (Ω) l'espa e ve toriel des mesures réelles sur Ω dont le support est
un sous-ensemble lo alement ni de I(Ω). Les éléments de A1 (Ω) seront appelés formes lisses
(sur Ω).

  (iii ) Le sous-espa e ve toriel de A0 (Ω) (resp. A1 (Ω)) onstituté des fon tions (resp. me-
sures) dont le support est ompa t se note A0c (Ω) (resp. A1c (Ω)).

   La orrespondan e Ω 7→ A0 (Ω) est un sous-fais eau du fais eau CX
                                                                  0 des germes de fon tions

réelles ontinues sur X .
   La dénition du fais eau A0X s'étend d'elle même au G-site XG de X : il sut, pour tout
objet V de XG , de dénir A0 (V ) omme le sous-espa e ve toriel de C0 (V, R) onstitué des
fon tions ϕ ontinues sur V qui satisfont à la ondition suivante : tout point x ∈ V possède
un voisinage k-anoïde W ⊂ V tel que ϕ|W ∈ H(W ). Désignant par A0X le fais eau ainsi
déni sur XG et notant π : XG → |X| le morphisme de sites anonique, l'identité
                                         A0X = π∗ A0X
est évidente. La proposition suivante l'est tout autant.

Proposition 3.2.2.  L'homomorphisme            anonique de préfais eaux HX → A0X sur le site
XG identie A0X au fais eau asso ié à HX .

Remarque 3.2.3
     1. La proposition pré édente répond à la question soulevée par le point 2 de la remarque
        2.3.11.
                                                                                              69



  2. Pour toute extension nie galoisienne k′ /k, l'homomorphisme anonique
                                                           ′
                                   A0X → (A0 X⊗k k′ )Gal(k /k)
     est un isomorphisme de fais eaux sur XG .

 La proposition suivante n'est guère surprenante, ompte tenu de la onstru tion du fais eau
HX .
Proposition 3.2.4.  Une fon tion réelle ϕ sur un ouvert Ω ⊂ X est lisse si et seulement
s'il existe, pour tout domaine stri tement k-analytique ompa t Y ⊂ Ω, une extension nie
(séparable ) k′ /k et une Spf(k′ ◦ )- ourbe simplement semi-stable Y telles que :
    Yη = Y ⊗k k ′ ;
    la fon tion Φ = (ϕ ⊗ 1)|S(Y) appartienne à l'espa e A0 (S(Y)) ;
    ϕ|Y ⊗k k′ = Φ ◦ τY .
Démonstration. Soit Y ⊂ X un domaine stri tement k-analytique ompa t.
   Étant données une extension nie galoisienne k′ /k et une Spf(k′ ◦ )- ourbe simplement semi-
stable Y de bre générique Y ⊗k k′ , onsidérons une fon tion Φ ∈ A0 (S(Y)) et notons S la
réunion du support de la mesure ddc Φ et du bord de Shilov Γ(Yη ) de Yη . Quelle que soit la
 omposante onnexe c de S(X ) − S , la restri tion de Φ au domaine polyédral c appartient
à l'espa e H(c) et la fon tion Φ|c ◦ τY = (Φ ◦ τY )|τ −1 (c) sur le domaine k-analytique τY−1 (c)
                                                      Y
de Y ⊗k k′ appartient à H(τY−1 (c)) ; en vertu de la proposition pré édente, ela implique
Φ ◦ τY ∈ A0 (Y ⊗k k′ ). La ondition de l'énon é est don susante.
   Considérons ré iproquement une fon tion ϕ ∈ A0 (Y ) et un re ouvrement ni V de Y par
des domaines k-anoïdes V tels que ϕ|V ∈ H(V ) ; par appli ation du point (ii) du lemme
2.2.22, il existe une extension nie (séparable) k′ /k et une Spf(k′ ◦ )- ourbe simplement semi-
stable Y , de bre générique Y ⊗k k′ , dont le squelette S(Y) ontient l'ensemble Γ des points de
Shilov des domaines k′ -anoïdes V ⊗k k′ , V ∈ V . Désignons par Φ la restri tion de ϕ′ = ϕ ⊗ 1
au squelette S(Y) de Y . Les bres de la rétra tion τY sont des domaines k′ -anoïdes dont le
bord de Shilov est réduit à un point ; la fon tion ϕ′ , étant harmonique sur Y ⊗k k′ − Γ, est
par suite onstante haque bre de τY en vertu du prin ipe du maximum et
                                          ϕ′ = Φ ◦ τY .
Vérions enn l'appartenan e de Φ à l'espa e A0 (S(Y)) : quel que soit le polytope entier
P ⊂ S(Y) − Γ dont le bord est formé de points de type (2), W = τY−1 (P ) est un domaine
stri tement k-anoïde dans Y tel que ϕ′|W ∈ H(τY−1 (P )) ( orollaire 2.3.14) ; on a don Φ|P =
(ϕ′|W )|P ∈ H(P ) et la fon tion ontinue Φ est bien ane par mor eaux sur S(Y).              2
   La proposition 3.2.2 peut maintenant être pré isée de manière à donner une nouvelle dé-
nition du fais eau A0X sur le G-site XG de X . Étant donné un domaine k-analytique V ⊂ X ,
 onvenons de désigner par R log |OX (V )× | le sous-espa e ve toriel réel de C0 (V, R) engendré
par les fon tions de la forme log |f |, f ∈ OX (V )× . La orrespondan e
                                       ×
                               R log |OX | : V 7→ R log |OX (V )× |

est un sous-préfais eau de A0X sur XG puisque R log |OX (V )× | ⊂ H(V ) pour tout domaine
k-anoïde V ⊂ X .
                                                                   ×
Proposition 3.2.5.  L'homomorphisme              anonique R log |OX | → A0X identie A0X au
                                        ×
fais eau asso ié au préfais eau R log |OX |.
70



Démonstration. Soit FX le fais eau sur XG asso ié au préfais eau R log |OX× |. Quelle que
                                                                                   ×
soit l'extension galoisienne nie k′ /k, la norme Nk′ /k : (pk′ )∗ (OX ⊗k k′ )× → OX induit un
homomorphisme Nk′ /k : (pk )∗ FX⊗k k → F tel que
                             ′        ′

                                           1
                                   f=              Nk′ /k (f ⊗ 1)
                                        [k′ : k]
pour toute se tion f de F , pk′ désignant la proje tion anonique de X ⊗k k′ sur X . Il sut don
de prouver qu'une se tion ϕ de A0X provient de FX après passage à une extension galoisienne
nie de k.
    Soient Y ⊂ X un domaine k-analytique ompa t et ϕ une fon tion dans A0X (Y ). Il existe par
hypothèse un re ouvrement ni V de Y par des domaines k-anoïdes V tels que ϕ|V ∈ H(V )
et, omme dans la démonstration pré édente, on peut trouver une extension galoisienne nie
k′ /k et une Spf(k′ ◦ )- ourbe simplement semi-stable Y dont la bre générique est un voisinage
de Y ⊗k k′ dans X ⊗k k′ et dont le squelette S(Y) ontient l'ensemble Γ de tous les points de
Shilov des domaines k-anoïdes V ⊗k k′ , V ∈ V .
    Considérons alors une dé omposition élémentaire D de S(Y) telle que Γ ⊂ D[0] (on rappelle
que D[0] est l'ensemble des 0-fa es des polytopes gurant dans D ). Quel que soit le polytope
Q ∈ D , τ −1 (Q) est un domaine k-anoïde et, par onstru tion,
                           ϕ|Q ∈ H(τ −1 (Q)) = R log |OX (τ −1 (Q))|.
                                                                                              2
Remarque 3.2.6.  Cette proposition est à rappro her des onsidérations de 2.3.4.
3.2.2. Un résultat de densité.
   Soit E un espa e topologique lo alement ompa t. L'ensemble des fon tions réelles onti-
nues sur E dont le support est ontenu dans un ompa t K de E est noté C0 (E, R)K et la
norme supK |.| en fait un espa e de Bana h. La restri tion de E à K induit une isométrie
de C0 (E, R)K sur le sous-espa e ve toriel fermé de l'espa e de Bana h C0 (K, R) formé des
fon tions s'annulant sur ∂K = K ∩ E − K .
   L'espa e ve toriel C0c (E, R) des fon tions réelles ontinues sur E dont le support est ompa t
est muni de la topologie lo alement onvexe limite indu tive des topologies d'espa es de
Bana h sur les C0 (E, R)K ; 'est la topologie lo alement onvexe la plus ne rendant ontinues
les inje tions C0 (E, R)K → C0c (E, R).
   Lorsque E est l'espa e topologique sous-ja ent à une ourbe stri tement k-analytique lisse
X , il est loisible de ne onsidérer que des ompa ts K qui sont des domaines stri tement
k-analytiques (i.e. des réunions nies de domaines stri tement k-anoïdes) : tout ompa t de
X est en eet ontenu dans un domaine stri tement k-analytique ompa t.
Proposition 3.2.7.  Le sous-espa e Ac (X) est dense dans Cc (X, R).
                                                0                      0

Démonstration. Soient K un domaine k analytique ompa t de X , ε ∈ R>0 et f une
fon tion ontinue sur X s'annulant en dehors de K . De l'uniforme ontinuité de f sur K
dé oule l'existen e d'une famille nie V de domaines k-anoïdes dans X dont la réunion K ′
 ontient K et telle que, pour tout V ∈ V et tous x, y ∈ V , |f (x) − f (y)| ≤ ε/2. Appliquant
le lemme suivant au domaine k-analytique ompa t K ′ et au sous-ensemble Σ réunion des
points de Shilov des V ∈ V et de la frontière de K , il existe une fon tion g ∈ A0 (X) telle que
gΣ = fΣ . Cette fon tion s'annule sur la frontière de K ′ et appartient don à A0 (X)K .
   Étant donné V ∈ V , la fon tion g satisfait, par onstru tion, à l'inégalité
                                                          ε
                                         |g(x) − g(y)| ≤
                                                          2
                                                                                                71



pour tous points x, y ∈ Σ ∩ V et don , en vertu du prin ipe du maximum,
                                                           ε
                                         |g(x) − g(y)| ≤
                                                           2
pour tous x ∈ V , y ∈ Σ ∩ V . Fixant un point y dans l'ensemble non vide Σ ∩ V (il ontient
Γ(V )), il vient alors
        |g(x) − f (x)| ≤ |g(x) − g(y)| + |g(y) − f (x)| = |g(x) − g(y)| + |f (y) − f (x)| ≤ ε
pour tout x ∈ V et, don
                       supK |f − g| ≤ supK ′ |f − g| = max |f|V − g|V | ≤ ε.
                                                        V ∈V

La proposition est démontrée.                                                                   2
Lemme 3.2.8.  Soit K un domaine k -analytique          ompa t de X ; pour tout sous-ensemble
ni Σ ⊂ K et toute fon tion f ∈ C (K, R), il existe une fon tion g ∈ A0 (X) telle que
                               0

f (x) = g(x) pour tout point x ∈ Σ ; si, de plus, f ∈ A0 (X)K , on peut supposer g ∈ A0 (X)K .
Démonstration. Soit K ′ ⊂ X un domaine k-analytique ompa t tel que K ⊂ K ′ − ∂K ′ .
Soit, pour tout point x ∈ Σ, Vx un voisinage k-anoïde onnexe de x dans K , Vx et Vy
étant disjoints si x 6= y . Notant V la réunion des Vx , x ∈ Σ, les propositions 3.1.21 et
3.1.22 garantissent l'existen e d'une (unique) fon tion g, ontinue sur X , harmonique sur
X − (∂V ∪ ∂K ∪ ∂K ′ ) et telle que :

    g∂Vx = f (x) pour tout x ∈ Σ ;
    g|∂K = f|∂K ;
    g|X−K ′ = 0.
La fon tion g est lisse et, pour tout x ∈ Σ, sa restri tion à Vx est onstante en vertu du
prin ipe du maximum. On a don g(x) = f (x) pour tout x ∈ Σ et g appartient à A0 (X)K si
et seulement si f appartient à C0 (X, R)K .                                             2
Corollaire 3.2.9.  Le sous-espa e A (X) est dense dans l'espa e de Fré het C (X, R).
                                    0                                        0

     Démonstration. L'appli ation linéaire anonique C0c (X, R)c → C0 (X, R) est ontinue 
 ar l'espa e d'arrivée est lo alement onvexe et ses restri tions aux sous-espa es C0 (X, R)K
sont ontinues  et d'image dense ; la densité de A0c (X) dans C0 (X, R) en dé oule immédia-
tement.
  On peut aussi dire tement utiliser le lemme pré édent.                                   2
  Convenons enn de munir les espa es ve toriels A0c (X) et A1c (X) des topologies lo alement
 onvexe limites indu tives des topologies ve torielles anoniques sur les espa es de dimension
nie A0c (X)S et A1c (X)S , où S par ourt l'ensemble des parties nies de I(X),

                                A0c (X)S = A0c (X) ∩ Γ(X − S, HX )
et
                                                                     M
                       A1c (X)S = {ω ∈ A1 (X) ; Supp(ω) ⊂ S} =             Rδx .
                                                                     x∈S

   Ce sont les plus nes des topologies lo alement onvexes séparées sur es espa es ve toriels,
 ara térisées par le fait que toute appli ation linéaire à valeurs dans un espa e ve toriel
lo alement onvexe est ontinue. En parti ulier, les espa es ve toriels duaux au sens algébrique
et au sens topologique sont les mêmes.


## Ber PDF pages 73-77

76                               VLADIMIR G. BERKOVICH

3.7. The local structure of a smooth morphism

       3.7.1. Definitions. — (i) A morphism <p : Y -> X is said to be an elementary fibration
of pure dimension one (resp. at a pointy e Y) if it can be included to a commutative diagram

                  Y c-^ z <— V = U (X x E,)
                                         »==!




                           X
such that
      a) ^ : Z -> X is a smooth proper morphism whose geometric fibres are irreducible
curves of genus g ^ 0;
      b) Y is an open subset of Z, and V = Z\Y;
      c ) V is an analytic domain in Z isomorphic to a disjoint union 11*"= i (X X E,),
m ^ 1, where E, are closed discs in A1 with center at zero, andj&r is the canonical projection;
      d ) there exists an analytic domain V C V such that the isomorphism
                  V^U^(XxE,)
from c ) extends to an isomorphism V'^-U^^X X E,'), where E,' is a closed disc
in A1 which contains E, and has a bigger radius;
     e ) the pair (Z^, YJ (resp. the triple (Z^, Y^,j/)), where x = 9(^)3 is elementary.
     (ii) A morphism is said to be an elementary fibration if it is a composition of ele-
mentary fibrations of pure dimension one.
     (iii) A morphism 9 : Y -> X is said to be standard of pure dimension one if everything
from (i), except the property e), is true for it. A composition of standard morphisms of
pure dimension one is said to be standard,
     We remark that the geometric fibers of a standard morphism are nonempty and
connected. Furthermore, elementary fibrations (resp. standard morphisms) are preserved
under any base change functor and under any ground field extension functor.

      3.7.2. Theorem. — Let 9 : Y -> X be a smooth morphism of pure dimension one, and
suppose that X (and therefore V) is good. Then for any pointy e Y there exist an etale morphism
f: X' -> X and an open subset Y" C Y7 = Y x^ X'
                  Y -^ X
                  A         A

                  r         r
                  Y' -^ X'

                  t V
                  Y"
such that y has a unique preimage y' in Y" and 9" : Y" -> X' is an elementary jibraiion of pure
dimension one at the point y.
            fiTALE COHOMOLOGY FOR NON-ARCHIMEDEAN ANALYTIC SPACES                           77

      3.7.3. Corollary. — Let <p : Y -> X be a smooth morphism of good k-analytic spaces. Then
for any point y e Y there exist ttale morphisms f: X' -> X and g : Y" -> Y' = Y Xx X'

                 Y ^> X

                            I7
                  A         A

                  r
                  Y' -^ X'

                  t- -7
                  Y"
such that y e/'C?(Y")) ^ 9" is an elementary fibration. •

      3.7.4. Corollary. — A smooth morphism is an open map. •

      Proof of Theorem 3.7.2. — All the analytic spaces considered in the proof are
assumed to be good. For numbers 0 < r' ^ r" (resp. 0 < r ' < r") we denote by A(r', r " )
(resp. B(r', r")) the closed (resp. open) annulus E(0, r")\D(0, r') (resp. D(0,r")\E(0,r'))
with center at zero.

       3.7.5. Proposition. — Let 9 : Y -> X be a separated smooth morphism of pure dimension
one, and let x eX. Suppose that the fibre Y^ is isomorphic to the open annulus B(r, R)^^). Then
there exist numbers r < r' < R' < R, an open neighborhood W ofx and an open subset i^ C (p"1^)
such that
      a) Y^ coincides with B(r', R').^,) under the identification of Y^ with B(r, R).^);
      b) i^ is isomorphic to the direct product ^ X B(r', R') over W.

      3.7.6. Lemma. — Let Y be an open subset of A^, and suppose that

                  Y, = D(0, r)^\ U E(^, r^              m ^ 0,
                                     i=l


wA^ r, < r aW | T(^) | < r (^T ^ ^ coordinate function on A1}. Then
       (i) if m == 0, ^ /or ^ w^w&^r 0 < r' < r ^r^ exists an open neighborhood % of x
 such that Y contains the direct product % X D(0, r').
        (ii) if m^ 1, then for any numbers max.([ T(aJ |, r,) < r' < r" < r, ^r<? exists an
 open neighborhood % of x such that Y contains the direct product % X B(r', r").

       proof. — In the case (i) (resp. (ii)) the intersection of all compact sets of the form
 U X E(0,r') (resp. U X A(r', r")), where U runs through compact neighborhoods
 of the point x, coincides with E(0, r')^ (resp. A(V, r")^), and therefore it is contained
 in the open set Y. It follows that there exists a compact neighborhood U of A: with
 U X E(0, r') C Y (resp. U X A(r', r") C Y). •
78                                VLADIMIR G. BERKOVICH

      3.7.7. Lemma. —Suppose we are given a commutative diagram




with smooth <p and ^ of the same pure dimension, and let y e Y and x = y(j^). Suppose that the
induced morphism fy^: Y^ -> Z^ is a local isomorphism at the pointy. Then f is a local isomorphism
at y.

      Proof. — Since Y^, is the fibre product of Y and Z^ over Z, the inverse image of
the sheaf of differentials of/on Y^ coincides with that of/. But the latter sheaf is equal
to zero at the point y. Therefore we may decrease Y and assume that f is unramified.
By Proposition 3.3.2 (i), the canonical homomorphism /"(^z/x) ~^^Y/X ls surjective.
Since both ^-modules are locally free and of the same rank, we have/*(Q^x) ^^Y/X-
From Proposition 3.5.3 (ii) it follows that/is dtale at the point y. By hypothesise/induces
an isomorphism of fields J^( z ) ^>^{y). By Proposition 2.4.1, K(^) ^K(j^), and there-
fore / is a local isomorphism at y, by Theorem 3.4.1. •

      Proof of Proposition 3.7.5. — We may assume that X ==e^(j^) is ^-affinoid. Take
a number r< t< R and set y ==j^(E(0, t)) <=Y^. Let V be an affinoid neighborhood
ofy in Y. Shrinking X and Y, we may assume that the fibre V^; is connected. Then

                  V,=E(0,R')^\UD(^,r,)^,

where / < R' < R, r, < R' and | T(ff,) [ < R' (T is the coordinate function on B(r, R)^(J.
Let V =^(^?). Since the image of S9®^K[x) in SS^^{x) is everywhere dense, we
can shrink X and assume that there exists an element f e 38 such that the norm of/— T
in SS^^^^x) is less than min(^, t). It follows that the morphism/: V -^A^ induces
 an isomorphism Vg; ^> V^ and f{y) =j&(E(0,^)). Take an open neighborhood i^ of
 the pointy such that Y^CV. Then the induced morphism /: i^ -> A^ satisfies the
 hypothesis of Lemma 3.7.7, and therefore / is a local isomorphism at the point y. The
 required statement now follows from Lemma 3.7.6. •

       3.7.8. Proposition. — Let 9 : Y -> X be a smooth morphism of pure dimension one, and let
 x e X. Suppose that the fibre Y^ is isomorphic to the open disc D(0, R).^) and that the morphism 9
 is a composition of an open immersion Y c-^ Z with a compact morphism ^ : Z -> X. Then for
 any 0 < r < R there exist an open neighborhood ^ of x and an open subset i^ C (p""^^) such that
       a) Y^ coincides with D(0, r)^^ under the identification ofl^ with D(0, R)^(^);
       b) T is isomorphic to W x D(0, r) over %.

       Let P and Q, be Hausdorff topological spaces, and let P^ C P and Q^ C Q be their
 open subsets for which there is a homeomorphism/: Pi ^ Q,r The topological space,
            £TALE COHOMOLOGY FOR NON-ARCHIMEDEAN ANALYTIC SPACES                            79

which is obtained by gluing P and Q via/.will be denoted by P u^Q. The following
statement is trivial.

       3.7.9. Lemma. — Suppose that there exists an open subset P'C P such that P^C P' and
the space P' u^Q is Hausdorff. Then the space P u^ is Hausdorff. Furthermore, suppose in
addition that P\Pi is compact and Q,^ P^ u, Q^is relatively compact in P' u^ Q. Then the space
P u/Q^ is compact. •

      Proof of Proposition 3.7.8. — We may assume that X is yfe-affinoid. In particular,
Z is Hausdorff and compact. From Proposition 3.7.5 it follows that we can shrink X
and find an open subset ^C Y such that ^ = B(r', R')^ and -T-^ X X B(r', R/)
for some r < r' < R' < R. Take numbers r' < r " < t < R" < R' and denote by IT
the open subset of V which corresponds to X x B(r", R"). The subset SC-lT, which
corresponds to X x A(^), is compact because X is compact, and therefore Z\S is
an open subset of Z. We apply the above gluing procedure to the spaces P == Z\S,
P == ^\S, P, = ^T\S, Q== X x (P^O, r")) U X X D(0, R"),
                 Q^ == X x B(r", t) U X x B(^, R"),

and to the canonical isomorphism /: P^ ^> Qi. One has
                 P' u, Q-^ X x (P^O, r')) U X x D(0, R').

From Lemma 3.7.9 it follows that the space T = P u^Q is Hausdorff and compact.
 In particular, the morphism ^' : Z' -> X is compact.
       Furthermore, the above construction restricted to the fibre at x gives a compact
JT (A;)-analytic space Z^ such that the connected component ofD(0, R)^) is isomorphic
to the projective line P^) . Moreover, the morphism ij/ is smooth at all points of this
connected component. Since ^' is compact, we can shrink X and replace Z' by the
connected component of D(0, R)^) in Z' so that the morphism ^' becomes proper smooth
of pure dimension one. It has a section a : X -> Z' defined by the point infinity of the
disc P^E^, r'). One has dirn^ H°(Z,, ^) == 1 and H^Z;, ^) = 0. By the Semi-
continuity Theorem ([Ber], 3.3.11), we can shrink X and assume that the same is true
for all x ' e X. It follows that all the fibres of ^ are isomorphic to the projective line.
       Finally, let L be the invertible sheaf on Z' which corresponds to o(X), and let L^
denote the inverse image of L on the fibre Z^, x ' e X. Then H^Z^LJ ==0 and
dimH°(Z^,L^) == 2. It follows that ^:(L) is a locally free fi^odule of rank two.
Shrinking X, we may assume that ^(L) is free. In this case it defines a morphism Z' -> P^
over X which is evidently an isomorphism. The required statement now follows from
Lemma 3.7.6 (i). •
       We are now ready to prove the theorem. First of all we remark that if K is a
finite separable extension of the field K(x), then there exists an dtale morphism/: X' -> X
such that/"1 (x) == { x ' } and K(^') === K. The preimage of the pointy under the morphism
80                                 VLADIMIR G. BERKOVICH

j f ' : Y ' = Y X x X' -> Y is a nonempty finite set of points. Fixing one of them, say y,
 we can replace 9 by a morphism Y" -> X', where Y" is an open neighborhood ofy
 which does not contain other points from/'"^j;). If we make the above procedure,
 we say for brevity that we increase the field K(x). Furthermore, we may assume that the
 space X is A-affinoid.

        Step 1. — One can increase the field K{x) so that <p is included in a commutative diagram

                   Y c-L» z



                            X
where
       a) ^ is a smooth proper morphism of pure dimension one whose geometric fibres are irreducible
curves of genus g^ 0, and j is an open immersion,
        ^) if 8^ I? ^7Z ^x has good reduction and y is the generic point of Z^..

      Let Z be an affinoid neighborhood of the point y. Replacing Y by a small open
neighborhood ofj/ which is contained in Z, we may assume that the morphism 9 : Y -> X
is a composition of an open immersion Y <-> Z with a compact morphism ^ : Z -> X.
By Proposition 3.6.1, we can increase the field K(x) and assume that the pair (Y^,j/)
is elementary. In particular, Y^ contains a disjoint union of m ^ 1 open annuli B(r,, R,)^(^)
such that the set Y^Ll^ B(r,, R,)^) is a connected compact neighborhood of the
pointy (Remark 3.6.3 (i)). By Proposition 3.7.5, we can shrink X, Y and the annuli
and assume that there are pairwise disjoint open subsets ^ C Y, 1 ^ i ^ m, such that
^ == B(r,, R,).^) and ^ -^ X X B(r,, R,). We take numbers r, < r\ < t, < R,' < R,
and denote by ^ the open subset of ^ which corresponds to X X B(r^, R,'). The
set S,C ^, which corresponds to X x A(^, ^), is compact because X is compact, and
therefore Z\U^ i S, is an open subset of Z. We apply the gluing procedure to the
spaces p = z\ur^ s,, p' = Ur^(^\s,), p, - U^^A),
                   Q= U^,(X x (^£(0, r;)) U X x D(0, RQ),
                   Q^ == U^,(X x B(r;, t,) U X x B(^, R;)),

and to the canonical isomorphism f\ P^ -^ Qr One has

                   P' u,Q^ U (X x (P^O, rj) U X x D(0, R,)).
                          1=1
From Lemma 3.7.9 it follows that the space Z' = P u^Q is Hausdorff and compact.
In particular, the morphism ^' : Z' -> X is compact.
      Furthermore, the above construction restricted to the fibre at x gives a compact
Jf (^-analytic space Z^ such that the connected component of the point y is a smooth


## Ber PDF pages 125-126

128                                VLADIMIR G. BERKOVICH

where 9 is a proper morphism and j is an open immersion. For a sheaf ^ on ^ one
defines
                   R^^R^^).

By Nagata's Theorem, any separated morphism of finite type is compactifiable.

       7 . 1 . 1 . Theorem. — Let S£ be a compactifiable scheme over k, and let 3^ he an abelian
torsion sheaf on St'. Then for any q ^ 0 there is a canonical isomorphism

                   H^, y} ^ ny, ^an).

       Proof. — Let 9 : W -> !C be a compactifiable morphism between schemes of locally
finite type over Spec(e^), where ^ is a A-affinoid algebra (the situation is slightly more
general for a further use). For a point x e SE we denote by ^ ^e fibre of 9 at x and
set ^ == ^ ® ^( x ) 8 ? and for an abelian torsion sheaf ^ on ^, we denote by ^ an(! ^x
the pullbacks of ^ on ^ ^d ^x? respectively. By the Base Change Theorem for Coho-
mology with Compact Support for schemes, one has

                   (R<^,^=H^,^).

Furthermore, for a point x e ^an over x, we fix an embedding of fields A(x) 8 <->^{x)\
It gives rise to an isomorphism

                   (^x^^T^^T.
Since the cohomology with compact support of schemes are preserved under separably
closed extensions of the ground field, one has

                  H^x, ^x) ^H^®^^?)°, ^).

Finally, the Weak Base Change Theorem 5.3.1 tells that

                  R^ 9an(^aI% == H^(^|11, ^n).

      We use the above remarks to establish the following two facts.

      7.1.2. Lemma. — In the above situation assume that the dimension of y is at most one.
Then for any q ^ 0 one has

                  (R3 9. ^ -^ R3 9T" ^an.

Furthermore, if in addition °K and. W are compactifiable over k and the theorem is true for SK^ then
it is also true for W.
             fiTALE COHOMOLOGY FOR NON-ARCHIMEDEAN ANALYTIC SPACES                                   129

     Proof. — The first statement follows from Theorem 6.1.1 and the above remarks,
and the homomorphism of Leray spectral sequences
                     H^, R^y. ^) ==> H^^, ^)

                             i
                   H^^, R3 9^ ^an) ==> H^0^, ^an)
                                                          i
shows that the second statement is also true. •

     7.1.3. Lemma. — In the above situation assume that the morphism 9 is finite and surjective.
Then if 2^ and W are compactifiable over k and the theorem is true for @<, then it is also true for SC.

      Proof. — Let ^ be an abelian torsion sheaf on 3C. Since 9 is finite and surjecdve,
the canonical homomorphism y -> 9^(9* ^") is injective. Furthermore, by Corol-
lary 4.3.2, for an abelian sheaf ^ on W one has H^.^, 9^ ^an) ^ H^®^, ^an).
In particular, the hypothesis implies that the theorem is true for all sheaves of the
form 9^ ^S. Thus, one can construct a resolution of ^", 0 -> 3F -> ^ro ->^"1 - > . . . ,
such that the theorem is true for all ^ri. The homomorphism of spectral sequences
                    H^H^^,^-)) ———> H^^,^)


                   ^(H^^ , ^
                             i
                             0    ran
                                     ')) ==> H^ - ^"1,^"1)
                                                    4 0
                                                          i
shows that the theorem is also true for ^r. •
      We are now ready to prove the theorem.
      1) The theorem is true for the direct product (P1)", where P1 is a the projective line over k.
— This follows from Lemma 7.1.2.
      2) The theorem is true for the projective space P^ over k. — Indeed, there exists a finite
surjecdve morphism (P1)" -> P71, and we can use Lemma 7.1.3.
      3) The theorem is true for any projective scheme over k. — This follows from Lemma 7.1.2.
      4) The theorem is true for any affine scheme of finite type over k. —- This is so because
such a scheme is isomorphic to an open subscheme of a projective scheme.
      5) The theorem is true for any proper scheme over k. — For a proper scheme SC we can
find an open everywhere dense affine subscheme ^, and so the dimension of the closed
subscheme W == 3E\^U is strictly less than the dimension of^*. Therefore the statement
is obtained by induction using the exact cohomological sequences associated with the
embeddings W ^ X <- W and ^an <-^ ^an <- ^an and the five-lemma.
      6) The theorem is true for any compactifiable scheme. — This is already clear. •
      7.1.4. Corollary. — Let 9 : W -> 3C be a compactifiable morphism between schemes of
locally finite type over Spec(J^), where ^ is a k-affinoid algebra^ and let ^S be an abelian torsion
sheaf on W. Then for any q ^ 0 there is a canonical isomorphism
                   (R^. ^ ^ R3 9^ ^an.
                                                                                                17
