# Stratum incidence and finite controlled chamber chains

Date: 1 September 2026.
Author: /root/p213_skeletal_hostile.
Status: authored research, not independently reviewed or production verified. The elementary geometric statements below are proved; actual model augmentation and current interfaces are expressly separated as conditional inputs. No live or earlier frozen file is changed.

## 1. Scope, provenance, and the point of this reduction

Root requested a hostile check of whether ample horizontal cuts can repair a non-pure, or not codimension-one connected, SNC dual complex inside a prescribed ordinary neighbourhood. The author found the old-boundary-count descent in Sections 2–3 and the rooted-tree assembly in Section 7. Root suggested writing the positive-vertex normalization explicitly; Section 4 supplies its proof. /root/p082_independent_reaudit is separately authoring the actual saturation and global-model blowup construction. This document is NOT an independent audit of that construction.

The key distinction is between four assertions:

1. A graph of actual zero-dimensional intersections on a smooth proper stratum becomes connected by adding enough ample divisors. This is proved in Sections 2–3.
2. A strict superlevel in a finite affine simplex complex retracts onto its positive-vertex subcomplex. This is proved in Section 4.
3. If actual global model augmentations realize those graphs and preserve earlier witnesses, a finite controlled top-chamber chain exists on one model. The exact required interface and conditional proof are in Sections 5–8.
4. Turning that geometric chain into equality of current coefficients requires whole-source coordinate domains and identical compact forms, not only a picture of the dual complex. Section 9 proves the normalization/target-domain calculation conditional on the precise L/O/Q/displayed-R interfaces; Section 10 retains the separate arbitrary-moment anchoring obligation.

No original dual complex is assumed pure or connected in codimension one. The geometric construction uses actual closed points over the residue field, not just rational or geometric points. No unknown current is pulled back by scalar extension.

## 2. Closed intersection graphs on a proper stratum

Let k be a field and let S be a smooth connected projective k-scheme of pure dimension d>=1. Smoothness and connectedness imply that S is integral: its finitely many irreducible components are disjoint because its local rings are regular. Geometric connectedness is NOT assumed.

Let D be a reduced strict-normal-crossing divisor on S. A component of D means an actual irreducible k-component; disconnected restrictions of an ambient divisor must first be split into their disjoint regular components. Choose effective ample Cartier divisors H_1,...,H_d on S such that each H_j is smooth over k and

    B = D + H_1 + ... + H_d

is reduced with strict normal crossings. Different H_j share no irreducible component. The H_j need not be geometrically irreducible.

A closed intersection stratum is a connected component of a nonempty intersection of distinct irreducible components of B. Zero-dimensional strata are closed points with their actual residue fields. A one-dimensional CLOSED stratum is a regular connected proper curve, not the open curve obtained after deleting its further intersections. Over an imperfect field regularity need not mean smoothness over k; this graph proof needs only regularity. In the later model application k has characteristic zero and the strata are smooth over k.

Define a finite graph G_B:

- its vertices are the zero-dimensional strata of B;
- two distinct vertices are joined when they lie on one common closed one-dimensional stratum.

The graph may be regarded as having a clique for the finite set of zero-strata on each such proper curve. The empty intersection S itself is the permitted curve when d=1.

**Claim.** G_B is nonempty and connected.

First observe that, at a zero-stratum p, exactly d distinct components of B meet. More than d is forbidden by SNC; fewer cannot cut a zero-dimensional stratum. For each color j at most one component of H_j meets p, since H_j is smooth and its distinct components are disjoint.

Let k(p) now denote the NUMBER of old D-components at p (not the residue field). If k(p)>0, remove one of these old components from the d equations defining p. Let Z be the connected component through p of the intersection of the remaining d−1 components. It is a regular integral proper curve.

Exactly d−k(p) H-colors occur at p. Hence at least one H_j has not been used. Its support does not contain p, since otherwise d+1 boundary components would meet p. In particular it does not contain Z. The restriction O(H_j)|_Z is ample, so its degree on the proper integral curve Z is positive. The nonzero restricted section therefore has a nonempty finite zero scheme. Choose any closed point q of that scheme.

At q the d−1 retained components and one component of H_j meet. SNC excludes every additional boundary component there, including the old component just removed. Therefore q is a zero-stratum with

    k(q) = k(p)−1.

The points p and q are distinct and lie on the same proper curve Z, so they are adjacent in G_B. Iteration reaches a zero-stratum with no old component in at most k(p)<=d moves.

It remains to connect all zero-strata having no old component. They all lie in H_1 intersect ... intersect H_d. Put Y_0=S and successively Y_j=H_1 intersect ... intersect H_j for j<=d−1. These are nonempty, regular, proper, connected schemes of dimension d−j. Indeed at each step before reaching dimension one, the previous scheme is connected and regular of dimension at least two, the restricted ample section is regular, and its zero scheme is connected by Stacks Lemma 33.48.3, tag 0FD9. Nonemptiness and the expected dimension follow from ampleness and SNC. Thus Y_{d−1} is a regular connected proper curve; for d=1 it is S itself.

The ample divisor H_d has positive degree on that curve, so H_1 intersect ... intersect H_d is finite nonempty. All its points lie on the same closed one-dimensional stratum Y_{d−1}. To see the last assertion with actual component indexing, connectedness of Y_{d−1} places it in one component of each smooth H_j; it is the corresponding connected intersection component. No additional component of B can contain it by SNC. Hence all zero-strata with no old component belong to a single clique. This proves the claim.

The proof does not require D to have any top-dimensional intersection, any connected dual complex, or any connected link. Nor does it need any chosen q to be k-rational. Over a non-algebraically-closed k, degrees are taken over k and positive ample degree still gives an actual closed point.

## 3. Existence of the ample cuts over an infinite field

Suppose k is infinite and perfect. This includes every residue field of characteristic zero.

Embed S into projective space by a very ample line bundle. At each stage there are only finitely many connected closed intersections of the already chosen SNC boundary. Each is smooth over k. Apply the smooth Bertini statement, Stacks Lemma 33.47.3 in tag 0FD4, to the restricted projective embedding of every positive-dimensional such stratum. Also require the next hyperplane to avoid every zero-dimensional stratum. The latter is a finite collection of nonempty open conditions: restriction to each closed point is not identically zero, so the bad hyperplanes form proper k-linear subspaces of the parameter space.

The intersection of these finitely many nonempty Zariski opens is nonempty. Because the parameter space is an affine or projective space over an infinite field, it has a k-point in that open. Choosing that point gives an ample H_j defined over k, smooth and transverse to all existing strata. In regular local coordinates the new equation restricts to a nonzero cotangent direction on the smallest old stratum through the point; it therefore extends the old SNC parameters. This is the required SNC condition for the enlarged boundary. Repeat d times.

This argument uses smoothness of each stratum over the perfect field k. It does not silently substitute a geometrically irreducible Bertini theorem for a merely connected k-scheme. Connectedness of the successive ample intersections is supplied separately by tag 0FD9, whose statement is over an arbitrary field and uses depth at closed points. Smooth positive-dimensional projective schemes here meet its depth hypothesis whenever their dimension is at least two.

The construction in this section produces divisors ON S. Lifting them to global horizontal divisors of a proper model, retaining ampleness on S, is an additional model-realization obligation, stated in Section 5. Merely applying Bertini on S does not settle that obligation.

## 4. Positive vertices and strict superlevels

Let K be a finite complex made by gluing closed affine simplices along faces with affine face identifications and no repeated vertex within a simplex. Different simplices may have the same vertex set: actual connected-stratum indexing can give parallel cells. The proof is cellwise and applies to this case as well as an ordinary finite simplicial complex.

Let g:|K|->R be continuous and affine on every simplex, and fix a real a. Let

    V_K = {x:g(x)>a},
    K_+ = the subcomplex of all simplices whose vertices v satisfy g(v)>a.

No purity hypothesis is imposed. For a point x in a simplex sigma write its barycentric coordinates as lambda_v. Set

    h(x) = sum_{v in sigma, g(v)>a} lambda_v.

If g(x)>a, then h(x)>0: otherwise g(x) would be a convex combination of vertex values <=a. Define r(x) in the positive face of sigma by replacing each positive lambda_v with lambda_v/h(x) and each other coordinate with zero.

These definitions agree on faces. The resulting map r:V_K->|K_+| is continuous because its cellwise denominator is strictly positive on its domain. Moreover g(r(x))>a, and r is the identity on |K_+|. The straight-line homotopy inside the simplex,

    H(x,t)=(1−t)x+t r(x),

is well-defined and continuous across faces. Affineness gives g(H(x,t))>a for every t in [0,1]. It fixes |K_+| throughout. Thus r is a strong deformation retraction.

Connected components of |K_+| are exactly the components of its finite vertex-edge graph. One way to verify this without assuming local path-connectedness of an arbitrary input set is to partition the finite complex by its graph components: each simplex belongs to just one component, and these finite unions are both closed and open. Each such union is path connected by joining points to vertices and using finite edge paths.

Consequently, if a connected set P_K lies in V_K and contains x_0,x_1, then r(P_K) is connected and lies in one graph component. Any positive vertex of the smallest face containing x_i is in the same component as r(x_i). Hence one can join chosen positive vertices associated with x_0 and x_1 by a finite edge path all of whose vertices and entire edges satisfy g>a.

This does not require P_K itself to be locally connected or path connected. Nor is r assumed to be simplicial on the strict superlevel; it is the explicit normalized barycentric map.

For a model function determined by a vertical rational Cartier divisor D=sum a_i E_i on a DVR model with fibre sum N_i E_i, the normalized coordinates on a face are lambda_i=N_i U_i/ell and

    g=sum a_i U_i=sum lambda_i g(v_i),  g(v_i)=ell a_i/N_i.

Thus the affine hypothesis is the precise model-function hypothesis, not an arbitrary continuous function on a skeleton.

## 5. Exact model-realization interface

The next conclusion is CONDITIONAL on the following model interface. It is stated literally so that the separate actual-blowup proof can be checked against it.

Start with a proper regular PROJECTIVE model M over a complete DVR with perfect residue field of characteristic zero, smooth connected projective generic fibre of dimension n>=1, and strict-normal-crossing SUPPORT of its special fibre with positive multiplicities. Its cells are indexed by actual connected intersections. A rational model function g is determined on M. A finite list of old top chambers and closed one-dimensional intersection curves may already have been selected as witnesses.

For any selected vertical component E, an augmentation is required to provide a finite sequence of actual projective blowups supported in the special fibre, with regular SNC support at every stage, satisfying:

(A1) Every old simplex remains an actual monomial simplex in the new skeleton. Old n-chambers, including their zero-stratum points, are preserved. Every previously selected closed one-dimensional intersection curve is carried isomorphically to its strict transform, with all previously selected incident zero-stratum points preserved.

(A2) The strict transform of E is canonically the same smooth connected projective k-scheme E. The link of its vertex in the final model is indexed by the actual closed intersections of the boundary on E obtained by adding n effective ample smooth divisors H_1,...,H_n to its old SNC boundary. Their full union is SNC. If a restriction of an ambient divisor is disconnected, its separate smooth components are separately indexed.

(A3) Every newly created n-chamber contains the strict transform of E. New vertices in this augmentation have the same value of g as the vertex E; g remains the SAME model function, pulled back to the new model.

The intended geometric realization is to take global horizontal H_j transverse to all relevant strata and successively blow up strict E intersect strict H_j, retaining strict E. However, the conditional theorem below does not count an assertion of this intended realization as its proof.

There are useful independent local checks on these requirements.

First, if a regular SNC codimension-two centre is E intersect H and H avoids all current zero-dimensional vertical strata, a new top chamber cannot omit strict E. Such a chamber would require the exceptional divisor plus n other old vertical components; its image would belong to E and those n old components and also to H, contradicting avoidance of the old zero-stratum. Equivalently, the two Rees charts and the SNC parameter count give the same exclusion. This proves the relevant local part of (A3), once the global construction exists.

Second, on a proper old one-dimensional stratum C, if E is among its defining components, the induced centre on C is the Cartier divisor H|C, so the strict transform is C. If E is not among them, C intersect E is a union of old zero-strata and H avoids them, so the centre misses C. This explains (A1)'s witness preservation, but the global SNC and horizontal-divisor existence still belong to the separate model proof.

Third, the new exceptional multiplicity is N_E+0=N_E, and the pullback coefficient of the vertical model divisor is a_E+0=a_E. Its g-value is therefore ell a_E/N_E=g(E). This is a model-function calculation, independent of a current.

## 6. What one augmentation supplies

Assume (A1)–(A3) for a component E with g(E)>a.

Apply Section 2 to S=E, d=n and the boundary from (A2). Its zero-strata are exactly the n-chambers containing E. Its proper closed one-dimensional strata correspond to their shared (n−1)-faces containing E. Thus the top-chamber adjacency graph IN THIS STAR is finite, nonempty and connected. This is a result about the augmented star, not an assumption on the original dual complex.

Every adjacency face tau used here contains E. Because g(E)>a and g is affine, the relative interior of tau contains points arbitrarily close to E at which g>a. For n>1 choose all other normal radii positive and sufficiently small, and solve

    sum N_i alpha_i = ell

for the radius of E. These choices can also make the n positive normal radii Q-linearly independent: require ell and the n−1 freely chosen small radii to be Q-linearly independent, which excludes only a countable union of proper rational hyperplanes in a nonempty open box. The rational invertible change of coordinates then proves independence of the full normal vector. For n=1 the only normal value ell/N_E is nonzero and is already a one-element independent family.

The corresponding monomial point is centered at the generic point of the WHOLE proper curve attached to tau. If the strict superlevel V={g>a} in the analytic space is saturated and is contained in W, that point lies in W. This is only a geometric choice of a suitable normal point; current consequences still require Section 9.

A further fact will attach different stars. If E' is any old vertex joined to E by an actual old edge, let S be that edge's smooth connected proper intersection component E intersect E', of dimension n−1. For n=1 the edge itself is already a top chamber. For n>1, the restrictions of H_1,...,H_{n−1} to S are ample and meet transversely; their complete intersection is finite nonempty. Nonemptiness follows by successively taking nonempty ample sections down to a proper curve and then using positive degree. Each resulting closed point supplies an n-chamber containing BOTH E and E'. Thus an augmentation of the parent vertex produces a bridge chamber for every old edge incident to it.

## 7. Finite global assembly: parent before child

Assume (A1)–(A3) can be performed at each required stage, and suppose a connected component C_+ of the positive-vertex graph of M has been fixed. Choose a root and a finite rooted spanning tree of that component. Process its vertices in an order in which every parent precedes its children.

At the root, Section 6 supplies a finite connected graph of top chambers, together with bridge chambers along each tree edge to a child. When the child E is processed, the bridge chamber supplied by its parent's earlier augmentation is still an actual existing chamber by (A1), and it contains E. It is therefore a vertex of the new connected star graph for E. The child's star graph joins to the already connected witness graph along that SAME bridge chamber, not merely at a lower-dimensional point.

All old witness chambers and all proper-curve adjacencies survive subsequent rounds by (A1). Since the tree and every local graph are finite, this builds a finite connected top-chamber witness graph on one final model. Every edge of that witness graph comes with an actual proper residual curve and an independent normal point in {g>a}, as in Section 6.

In particular, any two ORIGINAL n-chambers having positive vertices in C_+ lie in the graph: each is included when one of its positive vertices is processed. The construction also connects all newly created n-chambers, since (A3) puts each new chamber in the star being processed when it is created.

There is no unstated scheduling assumption. Processing an arbitrary child before its parent and later inventing a common bridge would not by itself show that the late bridge lies in the child's earlier connected witness. The rooted order ensures the bridge exists BEFORE the child's star is connected.

If two original n-chambers merely have points x_0,x_1 in a connected subset of {g>a} in the skeleton, Section 4 puts positive vertices from these chambers in the same C_+. The preceding construction therefore connects them. Original non-purity causes no problem: even an isolated positive vertex obtains top chambers from its complete ample intersection. Existing chambers are not needed in order to start the construction.

This is the requested finite conditional model-geometric route. It does not assert existence of an arbitrary connected compact P in W; it uses one if supplied. It also does not silently equate a fixed source moment's coefficient with the coefficient of a model chamber.

## 8. Additional finite subdivisions

A separate model theorem may require an additional finite toroidal refinement, for example to impose irreducibility of all intersections. The existence and regularity of that actual refinement is NOT proved merely by naming a combinatorial subdivision. BFJ Theorem 3.15 by itself yields a normal vertically Q-factorial model, not automatically a regular model.

Here is the precise combinatorial preservation statement. Suppose an actual refinement identifies the new skeleton with a finite conforming simplicial subdivision of the old skeleton, with the same underlying points and the same function g. Then the controlled chamber-chain conclusion survives.

Inside an old n-simplex sigma the set sigma intersect {g>a} is convex, and its relative interior part is nonempty whenever sigma meets the strict superlevel. The new top simplices meeting it can be joined by a polygonal path in the open convex set int(sigma) intersect {g>a}, chosen to avoid the finitely many faces of codimension at least two. Such a choice follows by choosing a generic intermediate point (or finitely many generic intermediate points) off the finitely many proper affine conditions for an unwanted lower-face intersection. The path crosses only finitely many codimension-one faces. Each crossing takes place where g>a, and supplies adjacency of the two new top simplices.

If two old chambers met along an old wall tau at a point with g>a, choose a point in the relative interior of a new (n−1)-simplex of tau, still with g>a. There is a top simplex on each old side incident to it. This joins the two internal new chains. The dimension-one case is just subdivision of intervals; no codimension-two avoidance is needed.

Thus every finite old controlled chain has a finite new controlled chain. On an actual regular SNC refinement each new wall again corresponds to a proper residual curve. Independent normal radii can be chosen in its nonempty relative-open superlevel exactly as in Section 6.

## 9. The required whole-source current calculation

This section is a CONDITIONAL interface calculation in relative dimension n>=2, not a proof of the upstream analytic results. The graph results above also allow n=1, but the frozen O premise used here does not; no one-dimensional current consequence is imported from it. This section uses precisely the frozen research premises:

- L: finite projection, RESEARCH_NOTE.md SHA256 3001c94985c0d3e60f184ffd9f0e9591775ea026a98cd20ee538005edac11b7a.
- O: ordinary-W outer collars and local divisor functional, SHA256 f629a77106d023763c7b99626c1ec1f8f449164f3749de475bf18bb0661e1d5b.
- Q: proper target-open comparison, SHA256 35d4ae59a167025ef595aa50a45101619ed1aef586be39abebca1486c62857ec.
- R: ONLY the displayed eq:p213-source-cell-formula in statement.tex SHA256 5c06cd6f091e5964a16c07b3efddd2104fed938447605f4f9b19ff8dfea01f1a, on the actual coordinate domains used.

Let T be positive separately closed of bidegree (0,0), given only on W. Let the final model N be regular with SNC support, and suppose the SAME rational model function g is determined on N and V={g>a} is contained in W.

At a zero-dimensional vertical stratum p let the n+1 components have multiplicities N_0,...,N_n. Its actual completed-ring presentation over the unramified coefficient lift of kappa(p) is

    π = epsilon product_{i=0}^n x_i^{N_i},

with epsilon a formal unit. Here is the algebra behind this presentation. Fix a coefficient field k in R, so R=k[[pi]]. The residue extension kappa(p)/k is finite separable. A primitive element and Hensel's lemma lift it to a coefficient field in the completed local ring A of the model at p, extending the chosen k. The actual component generators x_0,...,x_n are a regular system of parameters. The complete regular-local-ring structure theorem therefore identifies A with kappa(p)[[x_0,...,x_n]] using THESE parameters. The equation for the special fibre is pi=epsilon product x_i^{N_i}, with epsilon a genuine unit, because its divisor is the stated SNC fibre. Put R_p=kappa(p)[[pi]], the finite unramified coefficient extension of R. The displayed presentation over R_p follows by eliminating the variable pi from its linear relation. Neither extracting a root of epsilon nor changing the unknown current by scalar extension occurs in this construction.

Use the actual-model/formal-tube identification in O Section 2 for this presentation, and assume L for the resulting analytic hypersurface's finite projection, properness and canonical degree. L alone does not assert that an arbitrary model tube has that presentation or identification. No ordinary-sheet description is inserted. Let d_p=[kappa(p):k]. On the entire actual p-tube every x_i is nonzero of norm <1 and epsilon has norm one. If the local coefficients of the vertical rational Cartier divisor defining g are a_i, then

    g = sum a_i U_i,  sum N_i U_i=ell,  U_i=v(x_i),

on the ENTIRE tube, since all remaining local formal units also have norm one. This is not a formula restricted to its monomial section.

Omit x_0 and put q=(U_1,...,U_n). The intersection of that tube with V is EXACTLY the full inverse image of

    Omega_p = {u_i>0, sum_{i=1}^n N_i u_i<ell,
               (a_0/N_0)(ell−sum_{i=1}^n N_i u_i)
                    +sum_{i=1}^n a_i u_i>a}.

This is a convex ordinary open set, possibly empty. If the chamber meets {g>a}, it is nonempty and connected. L gives properness over this target. Q, applied to T restricted to the FULL inverse image, gives one finite b_p>=0 and, under displayed R, the normalized coordinate coefficient

    kappa_p = b_p/(N_0 d_p).

In particular a small collar in this chamber is not being compared with the rest by informal skeleton connectedness; both belong to this one connected proper target-open problem.

Now take an adjacent proper residual curve C given by n selected vertical components, and an independent normal point of its wall at which g>a. Apply O with current domain W (or V) at that point. For any zero-stratum p on C corresponding to a neighbouring top chamber, choose the SAME local normal generators x_0,...,x_{n−1} and the extra-component parameter w=x_n for the O collar and the preceding maximal-stratum chart. They satisfy the same completed-ring equation and have the same q=(U_1,...,U_{n−1},s), s=v(w).

The full O collar B×(0,delta) lies inside Omega_p after shrinking. A compact target top form supported there pulls back to the SAME full compact source form whether evaluated as an O-collar test or as a test on q^{-1}(Omega_p). There are no additional source points on the latter side: both domains are inverse images under the same actual q on the same completed p-tube, and the target support is contained in the collar. An ordinary source cutoff equal to one on the common compact may be used on both sides. Hence the target coefficient b_p is exactly O's lambda_C(p).

O's principal-divisor argument gives lambda_C(p)=c_C d_p for the closed points on this proper curve. With the same omitted selected normal component of multiplicity N_0, all adjacent top chambers therefore have

    kappa_p = c_C/N_0.

The residue degree d_p cancels; it must not be suppressed earlier or replaced by one over a nonclosed residue field.

There is also no omitted-normal ambiguity. If x_j is omitted instead, the actual affine logarithmic coordinate change has absolute determinant N_j/N_0. Both differential blocks contribute the determinant, while the Lebesgue change contributes its absolute value once. Thus

    b_p^(j)=(N_j/N_0)b_p^(0),
    canonical_p^(j)=N_j d_p,

and the ratio remains kappa_p. These are identities on the entire unit-coordinate tube, not just its Gauss points. General arbitrary changes of model or moment are not asserted to be determinant one.

It follows conditionally that the finite geometric witness graph from Section 7 (or Section 8) identifies the represented coordinate-chamber coefficients throughout that graph. This uses an actual Q problem for EACH whole chamber, an actual O problem for EACH whole proper wall curve, and identical compact source tests at their overlap. No unknown current has been extended by zero or pulled back by a field extension.

## 10. Exact remaining boundary

The following are NOT established by the graph proofs:

- Existence of the global horizontal lift/augmentation in (A1)–(A3). That is a separate actual-model proof, not a consequence of the graph lemma.
- Existence of a common model and a saturated ordinary V contained in a given W. The separate BFJ-based saturation proof must supply those hypotheses.
- Existence of an actual final regular toroidal refinement with the desired intersection conventions. Section 8 proves only preservation once it exists.
- Identification of an arbitrary prescribed source cell of an unrelated analytic moment F with one of the model-chamber coefficients. That still requires the exact captured-model/actual common-source test interface, for example an independently checked A/Q argument. Equality of tropical images alone does not suffice.
- Proof of displayed R or any stronger source separation theorem.
- General field extensions beyond the stated hypotheses, arbitrary analytic spaces, whole-current scalar rigidity, or full P21.3.

In particular, if a former F top cell meets {g>a} only partially, choosing a positive model vertex does not itself identify its coefficient with a small collar coefficient near that vertex. The explicit whole-source coordinate calculation in Section 9 handles a MODEL chamber. Transport from F to that model chart remains a separate required anchor.

The finite geometric route is stronger than a repeated status statement: it supplies a proved local incidence mechanism, an explicit positive-vertex deformation, a finite rooted-tree assembly with a correct scheduling rule, preservation under actual finite subdivisions, and a degree-accurate conditional current overlap calculation. It does not convert an unfinished upstream model proof into an accepted theorem.
