# Saturated ordinary neighborhoods and model-realized star augmentation

Date: 1 September 2026. Research author: /root/p082_independent_reaudit.
Status: bounded research proof-support, not production acceptance and not a proof of P21.3.

Root supplied the propagation question and emphasized full ordinary saturation. The author proved and checked the model-function and blowup interfaces below. A separately authored companion by /root/p213_skeletal_hostile handles the incidence-graph and finite-polyhedral assembly. That companion is not silently treated as an independently verified theorem here. Earlier source-cell access, L, O, Q and the displayed source representation R remain distinct conditional inputs wherever currents are discussed.

## 1. Exact scope and outputs

Let R be a complete discrete valuation ring, K its fraction field, k its residue field of characteristic zero, pi a uniformizer, and ell=v(pi)>0. Let X be a smooth connected PROJECTIVE K-variety of dimension n>=2. Projective is intentional: the model-function density theorem used here has this hypothesis. Neither algebraic closure of K nor of k is assumed.

A model means a projective flat integral R-scheme with generic fibre IDENTIFIED with X. All modifications constructed in this note are vertical blowups, and their generic-fibre map is the identity of X. No arbitrary current is pulled back along an alteration or along a nontrivial generic birational map.

We use two conventions separately.

- A regular SNC-support model has a regular total space and special fibre supported on a strict normal crossings divisor, with arbitrary positive multiplicities. Its cells are indexed by ACTUAL connected intersection strata. A closed zero-dimensional stratum need not be k-rational.
- A BFJ-SNC model additionally has every intersection of distinct special-fibre components irreducible or empty. This is BFJ Definition 1.1, stronger than the preceding convention. Such models are cofinal in the stated characteristic-zero projective setting.

The proved outputs are:

1. A compact connected set inside an ordinary open W admits a relatively compact ordinary neighborhood V inside W that is the FULL inverse image of a strict model-function superlevel set on every sufficiently high BFJ-SNC model.
2. Ample cuts on a chosen proper residual stratum are realized by actual original-R vertical blowups retaining that entire stratum, with exact special-fibre multiplicities.
3. Those blowups preserve all existing maximal-stratum points and all existing proper residual-curve incidences, provided the cuts avoid the finitely many current maximal-stratum points.
4. In a vertex-star augmentation every new maximal chamber contains the retained vertex; the value of every new exceptional vertex under a previously determined model function equals that of the retained vertex. Every old incident edge acquires a common maximal chamber with that retained vertex.
5. The resulting full-source containment and the precise interface to a finite residual-curve coefficient chain are explained. The global combinatorial assembly and the passage from arbitrary generic-birational access models to one same-generic-X controlled model are NOT asserted here without their additional arguments.

These statements concern actual analytic source points and whole proper algebraic curves, not merely overlapping tropical targets.

## 2. Saturated ordinary neighborhood: statement

Let W be an ordinary open subset of X^an, and let P be a nonempty compact connected subset of W. Fix finitely many BFJ-SNC models of X. There exist a rational model function g, a BFJ-SNC model M dominating these models and determining g, and an ordinary open V such that
\[
 P\subset V,\qquad \overline V\subset W,\qquad
 V=\{g>1/2\}.
 \tag{2.1}
\]
For EVERY BFJ-SNC model N dominating M,
\[
 g\circ p_N=g,\qquad
 V=p_N^{-1}\bigl(V\cap\operatorname{Sk}(N)\bigr).
 \tag{2.2}
\]
Here p_N is the ordinary continuous BFJ retraction on the SAME space X^an. In particular, (2.2) includes every point of the indicated inverse image, not only the monomial section.

Moreover p_N(P) is compact and connected and lies in V intersect Sk(N). Every point of P lying on one of the prescribed skeleta is fixed by p_N.

If W is nonempty and connected, then any two points of W lie in such a compact connected P. If the endpoints lie on prescribed skeleta, they therefore remain endpoints of the connected skeletal image p_N(P). No conclusion is made that the ENTIRE set V intersect Sk(N) is connected.

## 3. Saturated ordinary neighborhood: complete proof

The space X^an is compact Hausdorff because X is projective. Its closed sets P and X^an minus W are disjoint. Normality and Urysohn's lemma give a continuous function h with values in [0,1], equal to 1 on P and to 0 on X^an minus W.

BFJ Corollary 2.3, in the scope fixed in their Section 2.4, says that rational model functions are uniformly dense in continuous real functions. Choose a rational model function g with
\[
                        \|g-h\|_\infty<1/4.
 \tag{3.1}
\]
Then g>3/4 on P. Define V as in (2.1). Since g is continuous,
\[
 \overline V\subset\{g\ge1/2\}\subset\{h\ge1/4\}\subset W.
 \tag{3.2}
\]
The last set is compact, so V is relatively compact in W. Only rational model functions and their density are used. There is no assertion that a real linear span of model functions is stable under maximum.

Choose a model determining g. The directedness of models and SNC cofinality, BFJ Sections 1.1 and 2.4, give a BFJ-SNC common domination M of that determination and the finitely many prescribed models. Write g=phi_D for a vertical rational Cartier divisor D on M. If N dominates M, the pullback divisor determines the SAME function g on the same generic analytic space.

BFJ Lemma 3.5(ii) applies literally to a vertical real divisor determined on the current model. It gives
\[
                 \phi_D(p_N(y))=\phi_D(y)
                          \quad(y\in X^{\mathrm{an}}).
 \tag{3.3}
\]
For clarity, its proof evaluates the same divisor on ev_N(y) and on ev_N(p_N(y)); the equality ev_N composed with emb_N equals the identity makes these evaluations identical. This is equality, not an inequality for a nondetermined ideal function. In particular it is NOT an application of BFJ Proposition 3.12(ii), whose general ideal-function conclusion is only phi <= phi composed with p_N.

Because p_N takes values in Sk(N), (3.3) gives, point by point,
\[
 y\in V\ \Longleftrightarrow\ g(y)>1/2\
 \Longleftrightarrow\ g(p_N(y))>1/2\
 \Longleftrightarrow\ p_N(y)\in V\cap\operatorname{Sk}(N).
\]
This proves the full saturation (2.2). Continuity of p_N proves compactness and connectedness of p_N(P). BFJ Proposition 3.6(iii) says that a higher-model retraction fixes the entire skeleton of a lower model, proving the endpoint assertion.

Finally, Berkovich's 1999 Theorem 9.1 applies to strict analytic spaces locally embeddable in a smooth analytic space, over any complete nontrivially valued field. The analytification of smooth X, and every ordinary open subset of it, meet these hypotheses. Thus W is locally contractible, hence locally path connected. Path components of a locally path-connected space are open: each point has a path-connected open neighborhood in its path component. Connectedness of W therefore implies path connectedness. A path from one endpoint to the other has compact connected image P, actually contains both endpoints, and lies in W. This proves the last assertion without using any alteration occurring inside the proof of the cited topological theorem as a map on currents.

## 4. A local full-source version on any SNC-support model

A useful consequence does not require confusing BFJ's stronger combinatorial convention with general SNC support.

Suppose g is determined on a regular SNC-support model N by a vertical rational divisor
\[
                        D=\sum_i d_i E_i.
 \tag{4.1}
\]
Near a stratum choose regular local equations z_i for the vertical components through it. The local equation for D is a product of powers of these equations, up to a model unit. A model unit and its inverse both have absolute value at most one at every analytic point reducing to that local open; hence its absolute value is one. Thus, on the ENTIRE corresponding source tube,
\[
                            g(y)=\sum_i d_i v(z_i(y)).
 \tag{4.2}
\]
The convention is phi_D=log|O(D)|, so the sign in (4.2) is positive.

The local monomial cells and their continuous embeddings for actual connected strata are obtained from the completed regular local ring exactly as in BFJ Section 3.3. That construction is local at the generic point of a stratum; it does not identify two distinct connected strata having the same component labels. Formula (4.2) therefore implies that whenever a coordinate target set Omega satisfies the affine inequality g>1/2 on its monomial section, its FULL source inverse image satisfies the same inequality.

In particular, let C be a whole proper connected curve cut out by n vertical components, with multiplicities N_0,...,N_{n-1}>0. Let alpha_i>0 satisfy sum N_i alpha_i=ell and suppose
\[
                            \sum_{i=0}^{n-1}d_i\alpha_i>1/2.
 \tag{4.3}
\]
At a closed point p of C, let w be a residual parameter, s=v(w), and omit z_0 as in L. If an additional vertical component passes through p, give it multiplicity N_p and coefficient d_p in D; otherwise put N_p=d_p=0. On the entire punctured p-tube,
\[
 \begin{split}
 v(z_0)&=(\ell-\sum_{i=1}^{n-1}N_i u_i-N_p s)/N_0,\\
 g&=d_0(\ell-\sum_{i=1}^{n-1}N_i u_i-N_p s)/N_0
                 +\sum_{i=1}^{n-1}d_i u_i+d_p s.
 \end{split}
 \tag{4.4}
\]
Both identities use model units of norm one on all actual source points.

A sufficiently small normal box about alpha and sufficiently shallow residual intervals preserve (4.3), by the explicit affine expression (4.4). Only finitely many p meet an additional vertical component. Away from those points g has no residual-coordinate term at all. Therefore the containment required here is full-source containment inside V, not a Gauss-point estimate. If L supplies properness of the coordinate inverse image, any compact target support has compact inverse image in W. For the global residual principal-divisor primitive, O remains the exact input providing the finite bad set, zero-order cutoffs, and compact source gluing; this note does not replace O by (4.4) alone.

Independent normal values required by O can be chosen in every nonempty relative open subset of the positive normal face. Indeed choose alpha_1,...,alpha_{n-1} so that ell,alpha_1,...,alpha_{n-1} are rationally independent and put alpha_0=(ell-sum N_i alpha_i)/N_0. The prohibited rational relations form countably many proper affine hyperplanes. Then all n selected alpha_i are rationally independent.

## 5. General cuts over the ORIGINAL residue field

Let N be a projective regular SNC-support model. A vertical stratum means a connected component of an intersection of distinct vertical components. It is smooth over k, since it is regular and k has characteristic zero, and it is projective. Its connected components are integral; geometric connectedness is not asserted.

Fix finitely many strata and, if desired, finitely many additional closed points to avoid. After choosing a projective embedding of N over R, general hyperplanes on its special fibre restrict to smooth effective Cartier divisors on every positive-dimensional stratum and avoid all zero-dimensional strata and the prescribed finite points. Their coefficients may be chosen in k and lifted to R.

Here is why no algebraic closure or rational-point assumption is hidden. The ambient hyperplane system restricts to a basepoint-free system inducing a closed immersion on each stratum. Stacks Lemma 33.47.3 (tag 0FD4) gives a nonempty Zariski-open condition in the SAME k-parameter space for smoothness. Avoidance of a closed point is also a nonempty k-open condition: a hyperplane need not vanish in its finite residue field. There are finitely many conditions. Their intersection is nonempty because the parameter space is integral, and it has a k-point because the infinite field k has Zariski-dense rational points in affine space. This last elementary fact follows by induction on the number of variables for a nonzero polynomial. Lift the finitely many coefficients to R. Restriction to any positive-dimensional proper stratum is ample and cannot be nowhere vanishing, since a nowhere-vanishing section would trivialize an ample line bundle on a positive-dimensional proper scheme.

Cuts may be chosen successively. At each stage apply the same finite conditions to all previous mixed intersections. This gives a divisor with SNC support near the closed fibre after adjoining all selected horizontal cuts. In particular a new cut avoids every zero-dimensional mixed intersection already present.

For a smooth connected projective stratum S of dimension d>=2, a smooth ample section is connected by Stacks Lemma 33.48.3 (tag 0FD9): the section is regular and every closed local ring of S has depth d>=2. Its smooth connected zero locus is integral. Repeating until dimension one shows that d-1 general cuts on S have a whole smooth connected proper curve as intersection. One further ample cut meets it in nonempty finitely many closed points. This argument is over k itself; it does not replace connected with geometrically connected. When d=1 the starting curve is S and no preliminary cut is needed.

The horizontal divisors used below need only have the stated regularity near the special fibre. Their centers are vertical, so no assertion about their generic-fibre smoothness is needed.

## 6. Actual vertical blowup and its two charts

Fix one vertical component E of multiplicity N_E>0, and a horizontal cut H transverse to every vertical stratum. The center Z=E intersect H is a regular closed subscheme of codimension two. It is vertical. Blow it up and retain the strict transform of E.

At a point of Z let x be an equation of E and h one of H. Together with the other vertical equations z_j these are part of a regular parameter system. Locally
\[
                  \pi=\varepsilon x^{N_E}\prod_jz_j^{N_j},
 \tag{6.1}
\]
where epsilon is a unit. The two affine Rees charts are the following.

On the h-chart, x=h x', and
\[
           \pi=\varepsilon (x')^{N_E}h^{N_E}
                            \prod_jz_j^{N_j}.
 \tag{6.2}
\]
The retained E is x'=0 and the exceptional divisor G is h=0.

On the x-chart, h=x h', and
\[
                       \pi=\varepsilon x^{N_E}
                                      \prod_jz_j^{N_j}.
 \tag{6.3}
\]
Here G is x=0, the strict transform of E is absent, and the strict transform of H is h'=0.

These are actual charts of the blowup of (x,h), not charts after extracting a root of pi. Their regularity is checked directly: the equations x-hx' or h-xh' eliminate one regular parameter; at a point over the center its class has a nonzero coefficient in the cotangent direction of that parameter. The remaining vertical and horizontal equations are part of a regular parameter system. Thus the total space stays regular, the special fibre has SNC support, and its new exceptional multiplicity is EXACTLY N_E. No reduced-special-fibre conclusion is made. Away from Z the map is an isomorphism.

The blowup is projective and integral, its generic fibre is X with the identity identification, and it is flat over R because its coordinate rings are torsion-free over the DVR. Its strict E is isomorphic to the whole old E: in the h-chart it is given by x'=0 with the old equations of E, and it does not occur in the other chart. Equivalently it is the blowup of E in the Cartier divisor H restricted to E, which is the identity.

All these observations remain true when the center has several connected components. The exceptional divisor then has the corresponding components; each has multiplicity N_E. In the vertex-star application n>=2, the cuts on the smooth connected n-fold E can be chosen connected as in Section 5.

## 7. Retaining a whole old face and realizing its boundary cuts

Let I be a set of r vertical components including E, and let S be one connected component of their intersection. Put d=n+1-r. Assume d>=1; if d=0 this is already a maximal-stratum point and no cuts are needed.

Choose d horizontal cuts H_1,...,H_d by Section 5, transverse to every current mixed stratum. Successively blow up
\[
             E^{(j-1)}\cap H_j^{(j-1)}
                         \quad (j=1,\ldots,d),
 \tag{7.1}
\]
where superscripts denote strict transforms and E is always retained. At each step the selected stratum S is unchanged as a WHOLE projective scheme: the center restricts to the Cartier divisor H_j restricted to S, and the h-chart identifies its strict transform with S. Earlier cuts and old boundary equations remain transverse in that chart.

Write D_S for the reduced boundary on S cut out by all additional old vertical components. It is an SNC divisor, indexed by its actual connected components. In the final model, the extra vertical boundary on the retained S is exactly
\[
                         D_S+\sum_{j=1}^d H_j|_S.
 \tag{7.2}
\]
The new exceptional component G_j restricts to H_j|S and has multiplicity N_E. Formula (7.2) is a scheme-theoretic local statement about regular coordinate divisors; it records every actual connected intersection and every closed point, not just ambient component labels.

Consequently, the top-dimensional cells incident to the retained old face are the actual zero-dimensional strata of (7.2), and their codimension-one incidences are the whole connected proper curve components of the corresponding intersections of d-1 boundary components. The dimensions are exact: r+d=n+1 components cut a closed point in the (n+1)-dimensional model, while r+d-1=n cut a proper curve.

The old monomial face is not moved as an analytic subset of X^an. At the generic point of any old stratum H_j is a unit, since no cut contains that stratum. In the retaining chart v(h_j)=0 and v(x')=v(x). For rationally independent positive weights this gives exactly the same valuation by the finite-initial-term argument in the completed regular local ring; continuity of the monomial embeddings gives the same statement on the whole face, including its faces. Thus these modifications add incident source cells rather than merely drawing new cells over the same tropical image.

This section supplies the ACTUAL MODEL interface for an incidence-graph lemma on the projective pair (S,D_S+sum H_j|S). The companion author proves that its zero-dimensional strata are connected by proper one-dimensional strata. That graph result is kept separately attributed and is not needed to establish (7.1)--(7.2).

## 8. Previously obtained proper-curve witnesses survive later cuts

Assume H avoids every current zero-dimensional vertical stratum. There are only finitely many such closed points. Then the following preservation statements hold after blowing up E intersect H.

First, every old maximal-stratum point p is disjoint from the center. The map is an isomorphism over an ordinary algebraic neighborhood of p, so its ENTIRE analytic p-tube is unchanged. In particular no old top chamber or chosen compact source test in that tube is lost.

Second, let C be any connected component of an intersection of n current vertical components. It is a whole smooth proper curve. If E is one of these n components, the strict transform of C is C itself: the center restricts to the Cartier divisor H|C, and the retaining chart gives the identity on C. The old maximal-stratum points of C are untouched because H avoids them. If E is not one of the n components, every point of C intersect E is an old zero-dimensional vertical stratum, by the SNC parameter count. The center is disjoint from all these points and therefore from C. Again the whole curve and its old incidences are unchanged.

Third, old higher-dimensional strata and their monomial faces remain present. A stratum containing E is unchanged as above. A stratum not containing E is either disjoint from the center or its strict transform is the blowup along a regular intersection of the old boundary E with H; it remains smooth, proper and integral and has the same generic point. In particular no old stratum disappears. Its generic-point monomial face agrees with the old face by the unit argument of Section 7.

These statements may be iterated, since Section 5 supplies new cuts avoiding all zero-dimensional strata of the CURRENT model, including ones created earlier. Hence any finite collection of previously achieved maximal chambers and whole proper-curve incidences is preserved through later star augmentations. This is not a claim that a G-open chart is an ordinary neighborhood, or that newly chosen primitives have automatic support control; ordinary support is governed separately by Sections 2--4 and O.

## 9. Three additional vertex-star interfaces

For use in a finite global assembly, take S=E, of dimension n, and make n successive cuts.

### 9.1 Every new top chamber contains the retained E

For a single step, a new maximal-stratum point must lie on a new exceptional component G. Suppose it does not lie on strict E. The x-chart then describes it as lying on G and n other old vertical components. Its image would lie on E and those n components, hence on an old zero-dimensional vertical stratum, and also on H because G maps to the center. This contradicts avoidance of every such point by H. Thus every new maximal chamber contains strict E. Applying this argument at each step with the current boundary proves the assertion for the full n-cut round.

The statement is about genuinely new chambers, not a claim that every old chamber contains E.

### 9.2 Each new exceptional vertex has the old value g(E)

Suppose g is already determined on the incoming model by D=sum d_i E_i. At the generic point of the center E intersect H, no other old vertical component occurs: transverse additional intersections have positive codimension in the center. Therefore the exceptional coefficient in the pullback D is d_E, while its special-fibre multiplicity is N_E by (6.2). The divisorial point of either component has v of its local equation equal to ell divided by its special multiplicity. Hence
\[
                 g(x_G)=\ell d_E/N_E=g(x_E).
 \tag{9.1}
\]
This holds for each component if the center is disconnected. In particular an augmentation at a vertex with g>1/2 creates only vertices of that SAME positive superlevel value. The function g on the analytic generic fibre has not changed.

### 9.3 Every old incident edge acquires a common top chamber

Let E and E' be old vertical components whose intersection has a nonempty connected component S'. It has dimension n-1. The first n-1 general ample cuts on S' have nonempty zero-dimensional intersection. To see nonemptiness, cut successively; before the last cut there is a positive-dimensional proper scheme and an ample effective divisor cannot be empty. Smooth transversality gives the expected dimension. For n=2 this is simply a nonempty ample divisor on the proper curve S'.

At every resulting closed point the final model has the n+1 vertical components
\[
                       E,\ E',\ G_1,\ldots,G_{n-1}.
 \tag{9.2}
\]
They form a maximal stratum. The remaining nth cut avoids these points, since it is transverse to all previously formed mixed intersections; alternatively choose it after the first n-1 steps using current-point avoidance. Thus a whole top chamber incident to both the retained E and the old E' is present after the round and survives subsequent rounds by Section 8.

If both original vertices satisfy g>1/2, EVERY vertex of the common chamber (9.2) satisfies g>1/2: the G_j have the value of E by (9.1). Since g is affine on that chamber, its ENTIRE closed monomial simplex lies in V. Formula (4.2), or (2.2) after a BFJ-compatible refinement, supplies the corresponding full-source superlevel containment. This is an actual model bridge; it does not yet assert that an arbitrary pair of original source cells has been put on the same controlled model.

## 10. BFJ's extra intersection convention and later subdivisions

The cuts may create several closed points with the same collection of ambient component labels, so a regular SNC-support model produced above need not already satisfy BFJ's irreducible-intersections convention.

BFJ Section 1.1 explicitly permits achieving that convention by further blowups along connected components of intersections. These are toroidal stratum blowups. Locally, blowing up (z_i : i in J) has charts z_j=z_i t_j for j in J minus {i}. The new exceptional multiplicity is sum_{j in J} N_j, positive. The charts are regular coordinate charts, and the model's monomial support is unchanged: choosing a minimum of the old weights selects a chart, with new weights v(t_j)=v(z_j)-v(z_i). This gives precisely a subdivision of the old normal cone. Restricting to sum N_j v(z_j)=ell gives a finite subdivision of its actual monomial simplex. No new analytic points are introduced in that skeleton.

Thus the SNC-support constructions may be followed by a BFJ-compatible toroidal refinement. The original model function remains determined, and Section 2's full saturation applies on the resulting model. A finite controlled chamber chain, if already constructed, survives this subdivision: in each old simplex its nonempty strict affine superlevel set is convex; finite subdivision permits a polygonal path between prescribed new top-simplex interiors avoiding the finite codimension-at-least-two faces and crossing only finitely many codimension-one faces. Common old walls are treated by choosing a positive point in a new wall interior. This is a geometric subdivision observation, not an assumption that an arbitrary SNC dual complex was pure or codimension-one connected before augmentation.

## 11. Exact conditional current interface

The saturated-neighborhood and blowup statements above are purely geometric and do not assume R.

Suppose one has, on a single same-generic-X model dominating the determination of g, a FINITE chain of full-dimensional coordinate chambers and codimension-one faces with these properties:

- The relevant chamber pieces lie in {g>1/2}.
- Every crossing face corresponds to a whole proper connected residual curve defined by n vertical components.
- The endpoints are tied to their original moment-source coefficients by actual full-rank common-source identities and the SAME compact ordinary top-form test, as in frozen access v2 or the common-moment comparison.
- For every chamber comparison the relevant coordinate domain is an entire inverse image of a connected open target subset, not a selected sheet.
- L, O, Q and the displayed R formula hold on the exact domains used.

Then normalized coefficients propagate along that FINITE chain. Here is the precise reason, not a replacement for the geometric chain.

On the target piece of a maximal chamber the determined model function is affine, so its strict superlevel subset is convex and connected. Formula (4.2) gives full-source containment in W. Q compares all compact source tests of that coordinate moment on this connected proper target-open domain with one normalized constant. At a crossing face choose an independent positive normal point in its nonempty superlevel part. O, on the SAME current defined on W, supplies full shallow residual collars and a principal-divisor functional on the whole proper curve. It identifies the residual coefficients as c_C times [kappa(p):k]. With omitted normal multiplicity N_0, the canonical coefficient is N_0[kappa(p):k]; hence every collar has normalized ratio c_C/N_0.

At each of the two specified adjacent closed points choose a compact target patch and a compact ordinary source cutoff in a common represented source top cell. The SAME resulting ordinary top form is evaluated once by Q in the chamber coordinates and once in the collar coordinates. Their affine Jacobian multiplies both the current and canonical coefficients. A positive canonical pairing therefore forces equality of the normalized chamber constant and c_C/N_0. Finite repetition compares the endpoints.

This uses the full source formula R for arbitrary ordinary source multipliers. It does not infer current equality from a tropical pushforward aggregate alone. It also does not identify a pullback from one unrelated moment with a pullback from another without an actual common analytic moment. All primitives and all compact tests remain in W. Nothing here extends zero currents across singular loci, pulls T back under an alteration, or assumes all-chart accessibility.

## 12. What is and is not solved by these interfaces

The full ordinary saturation in (2.2) removes a real support-control obstacle: a later skeleton path lying in this controlled superlevel region has its ENTIRE retraction inverse image in W. The vertex-star blowup interfaces give actual proper residual geometry which can add chambers at formerly lower-dimensional attachments, while preserving finite witnesses already built. Connectedness of an old dual complex alone would not give those properties.

A finite-polyhedral incidence assembly is being proved separately by /root/p213_skeletal_hostile. Its model inputs can be stated exactly as Sections 7--10: actual connected strata, old-witness preservation, new chambers incident to the retained vertex, exceptional values copied from that vertex, and common chambers over old incident edges. Merely naming a graph or presuming its connectedness is not a substitute for that proof. This note does not certify the companion's final assembly before independent review.

There is also a distinct SAME-GENERIC-X interface. Frozen source-cell access v2 starts with smooth PROPER X and can return a smooth proper Y with a generic proper birational map Y->X that is an isomorphism only over a rational-unit open U. The saturation lemma here starts with PROJECTIVE X and models whose generic fibre is exactly X. One cannot silently regard all of those access models as models of this X. To use a common generic modification, one must preserve actual endpoint source patches and establish controlled connected paths in the analytic locus where the generic map is an isomorphism, or prove a suitable alternative transport/removability statement with its degree hypotheses. No such unrestricted transport is claimed in this packet.

Even after the geometric chain and endpoint matching are supplied, a whole-current conclusion additionally requires the displayed R representation and a finite ordinary source partition for every compact top-form test, with ONE coefficient proved common across its summands. The equality T=c delta_X is therefore not asserted here. The packet does not retire P21.3, extend BFJ density from projective to arbitrary proper X, assume every dual complex is pure, or compare target-overlapping but source-disjoint cells. It supplies explicit original-field geometric mechanisms for the next bounded assembly.
