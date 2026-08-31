# Scalar-current classification by analytic components

Date: 1 September 2026. Research author: /root.

Status: new candidate, requiring its own exact-final independent review and production Rethlas verification. No live theorem, retirement, or priority claim. The preceding normal-space manuscript remains frozen; the simpler analytic-support argument here is a sibling, not a silent replacement of its general tropical-nullity proof.

## 1. Proposed classification and its exact field scope

Let K be a complete discretely valued non-Archimedean field with residue characteristic zero. Let X be good, separated, strict and boundaryless, pure of dimension n>=2. We impose NEITHER reducedness NOR normality. Let (X_i) be its analytic irreducible components with their reduced structures, and let delta_i denote their integration currents pushed into X. The proposed classification is

    {positive separately d',d''-closed (0,0)-currents on X}
      = { sum_i c_i delta_i : c_i is finite and >=0 }.       (1.1)

The coefficients are unique. The sum is locally finite on compact tests; no boundedness condition across different components is required. The canonical current has a different, fixed normalization,

    delta_X = sum_i m_i delta_i,                            (1.2)

where m_i>0 is the generic scheme-theoretic multiplicity of X along X_i. Consequently a positive closed scalar current on an IRREDUCIBLE ordinary domain is a single nonnegative constant multiple of its canonical current, even when that domain is singular, nonnormal or nonreduced. Connectedness alone is insufficient when there is more than one analytic component.

The nontrivial geometric input remains the frozen quasi-smooth scalar assembly, SHA256 5809b99def2c16becb716eb2eb7c24382a8a31655b9b43902804e585cb53bb5c. Its original-field and dimension hypotheses are retained. The reductions below do not extend that input to arbitrary valued fields or positive-bidegree currents.

## 2. The analytic-support observation

CLD Proposition 15.2.1(b) says that if A is a closed analytic subset of an analytic domain and dim A<max(a,b), the support of an ordinary smooth (a,b)-form does not meet A. This means vanishing of the FORM GERM near every point of A, not just its restriction to A. It follows from the pointwise invariant d_K and the strong-support property; it is much stronger than a statement that a chosen tropical image has measure zero.

In particular, if A is a closed analytic subset of a pure n-dimensional Y and dim A<q, any compactly supported ordinary (q,q)-test form on Y has compact support contained in Y\A. Therefore two currents acting on these test forms which agree on Y\A agree on Y. No positivity or closedness of the two currents is needed for this deduction. Restrict a test form to Y\A and apply the given equality there; its support is still compact in that open subspace. Extension by zero recovers the original test form. The local dimension version follows by a finite partition of the particular compact test support.

This observation is sufficient for the analytic exceptional sets in this note. It does not replace the preceding normal note's stronger result for arbitrary closed TROPICAL-Hausdorff-negligible sets, which need not be analytic. Nor does it assert that arbitrary currents given on a complement extend as CLOSED currents: the test degrees for their derivatives are different, and boundary terms may survive in those lower degrees.

## 3. Connected complements in the normalization

We need the following precise consequence of bounded analytic extension. If N is a nonempty connected good separated strict boundaryless normal K-analytic space, pure of dimension n, and E is closed analytic of local dimension <n, then N\E is nonempty and ordinarily connected. The set E need not be the singular set of N and may have codimension one.

Here is the proof with the topology made explicit. Normality passes to analytic domains, by Ducros Theorem 3.4 and Section 3.4. Around every point of N take a strict affinoid neighborhood D whose ordinary interior contains that point. The inner-presentation construction in Temkin 3.4.2.1 and 3.4.2.3 provides such neighborhoods inside any prescribed ordinary open, without extending K. The ring B of D is normal and pure n-dimensional. The ideal of E intersect D contains no minimal prime, since the analytic subset has smaller dimension on every component. Thus its rigid counterpart is nowhere dense.

An ordinary disconnection N\E=P disjoint-union Q would define the bounded analytic idempotent h=0 on P and h=1 on Q. On D write E intersect D=V(f_1,...,f_r). Choose a in K with 0<|a|<1. The strict Laurent domains |f_j|>=|a|^m, j=1,...,r and m>=1, cover D\E and form a rigid admissible cover. To check this last assertion, on an affinoid test mapping into the complement the f_j generate the unit ideal; an identity 1=sum b_j f_j and bounds for the b_j give a uniform lower bound on max|f_j|. A finite cover at sufficiently large m then suffices. The compatible affinoid restrictions of h therefore define a bounded rigid analytic function on Sp(B)\V(f_1,...,f_r).

Bartenwerfer's extension theorem, in the general-normal form of Conrad's Moishezon spaces, Theorem 2.1.1, extends it uniquely to H_D in B. Uniqueness gives H_D^2=H_D. On overlapping ordinary interiors of two D, take smaller normal strict affinoid neighborhoods; the same uniqueness theorem makes the extended functions agree. They glue ordinarily to H on N. The continuous function |H| takes only 0 and 1, and both values occur, contradicting connectedness of N. Nonemptiness of N\E follows from dimension or from Ducros Lemma 4.24. No global rigid model of N or global paracompactness is invoked.

This is the same general-complement argument independently checked in p213_normal_extension_source_audit_20260901. That report is not an independent review of the rest of this manuscript. We give the argument here to make explicit why a divisorial conductor is allowed for CONNECTEDNESS, although the later curvature comparison will have a different dimension threshold.

## 4. Reduced spaces: construction and uniqueness of the coefficients

Assume first that X is reduced. The irreducible components X_i form a G-locally finite family of closed analytic subsets, by Ducros Theorem 4.20. Every affinoid domain meets only finitely many, and purity plus Proposition 4.22 makes every component pure n-dimensional. Since X is good, every compact subset can be covered by finitely many affinoid neighborhoods. Hence it meets only finitely many X_i. This is exactly the finiteness needed for all sums of currents below.

Let S be the non-quasi-smooth locus of X. Over the perfect field K, the regular and quasi-smooth loci agree; their complement is closed analytic. A reduced affinoid algebra is regular at each minimal prime, and excellence makes this regular locus Zariski open. Therefore S contains no component, and dim S<n locally. On X\S, different irreducible components are disjoint: a regular local ring is a domain. For each i put

    U_i = X_i\S.

Each U_i is an ordinary OPEN subset of X, not merely open in X_i: after deleting S, each point lies on just one component and the union of all the other components is a closed analytic set. Each U_i is nonempty.

Let nu_i:N_i->X_i be the finite normalization. Ducros Theorem 5.13 and Theorem 5.17 give existence, finiteness, purity and connectedness of N_i. A finite morphism preserves strictness, its inverse images of affinoid neighborhoods are affinoid, and it has no relative boundary. Thus N_i is good, separated, strict, normal and boundaryless, pure n-dimensional. Closed immersions X_i->X have the same boundary property. These statements stay over K.

Set E_i=nu_i^(-1)(S intersect X_i). Finite morphisms preserve dimensions of closed subsets under inverse image, so E_i has local dimension <n. It is proper because normalization is an isomorphism over the regular locus, which is dense. The map

    N_i\E_i -> U_i

is an analytic isomorphism. Section 3 shows its source is nonempty and ordinarily connected. Consequently U_i is nonempty and ordinarily connected as well. It is quasi-smooth, good, separated, strict and boundaryless of pure dimension n.

Now let T be positive closed of bidegree (0,0) on X. Restriction to U_i is legitimate; no pullback of T by nu_i over E_i is being defined. Apply the frozen quasi-smooth scalar theorem to T|U_i to obtain a unique finite c_i>=0 such that

    T|U_i = c_i delta_(U_i).                                (4.1)

Define C=sum_i c_i delta_i on X. Each delta_i is positive and closed: it is the proper pushforward of the canonical positive integration current on the pure boundaryless X_i, and Stokes gives separate closedness. Local finiteness proved above makes C a current, since on a fixed compact support it is a finite sum of continuous functionals. It also makes C positive and closed. Its restriction to U_i is c_i delta_(U_i); all other summands vanish there.

Thus T-C is zero on X\S. Every compact smooth (n,n)-form on X has support disjoint from S by Section 2. Testing T-C against such a form gives zero, proving (1.1) for reduced X. In this last step no coefficient-measure theorem is needed and no unexamined distribution at S is discarded: every test form itself has its support in the established equality locus.

Uniqueness follows from (4.1). Each U_i contains a compact positive test of strictly positive canonical integral, as in the quasi-smooth input. Evaluation on that test recovers c_i. Conversely every finite nonnegative family defines a positive closed current by the same locally finite construction. This proves both directions of (1.1) for reduced spaces.

## 5. Nilpotents and generic multiplicities

Let j:X_red->X be nilreduction. Their underlying spaces and completed residue fields agree, since seminorms kill nilpotents. Goodness, separatedness, strictness and pure dimension pass to the reduction. The finite immersion has no relative boundary, so X_red is boundaryless.

On an affinoid quotient A->A/I with I nilpotent, a unit of A/I lifts to a unit of A. Indeed lift it and its inverse to a,b with ab=1+r, r nilpotent; the finite geometric series for (1+r)^(-1) corrects b to an inverse of a. Lifted units have the same absolute values at every analytic point. Ordinary moments on the reduction therefore lift locally after shrinking, and moments on X restrict with identical tropicalizations. The form variant of CLD Proposition 15.1.3(b), valid here because X is good and topologically separated, gives the resulting identifications of ordinary smooth form sheaves in every bidegree.

The identifications commute with wedge product, J and the two differentials and preserve support and positivity cones. They also identify the compact-test locally convex topologies: a compact-test presentation uses finitely many moments, tropical representatives and their derivative seminorms; the lifted and restricted presentations form cofinal systems with the same images and the same representatives. Thus j^* is a homeomorphism of compact-test form spaces. Its continuous transpose j_* is an isomorphism of current spaces preserving positivity and separate closedness. This is not an extension of a current through a noninvertible normalization map; nilreduction has identical test calculus.

Write T=j_*T_red. Apply Section 4 to T_red and push its classification forward. This gives (1.1) with delta_i interpreted as the reduced component current in X, without a reducedness hypothesis. The same isomorphism, or direct testing of coefficient measures, commutes with multiplication by a continuous function f: j_*(fT_red)=f j_*T_red. No product for an arbitrary higher-order distribution is introduced.

The generic multiplicities in (1.2) are NOT removed by this calculus identification. By CLD 13.5.2 the fundamental cycle is [X]=sum m_i[X_i], where m_i is the positive length at the generic point of an affinoid component and these local definitions agree. Proposition 16.6.3 gives delta_X=delta_[X], which is exactly (1.2). In particular, if X has one irreducible component, (1.1) reads T=c_1 delta_1=(c_1/m_1)delta_X. Every factor is positive and finite. This explains why currents have a nilpotent-invariant test calculus while the chosen fundamental current remembers multiplicity.

## 6. The exact remaining bidegree-zero curvature question

Let u,v be continuous functions on the whole X; write [u]=u delta_X and [v]=v delta_X. The following argument applies in particular to the continuous psh pairs of P21.3, but does not need positivity of their curvature difference. Define currents on X

    R_i = d'd''(u delta_i)-d'd''(v delta_i).                 (6.1)

All products here are continuous multiplications of the positive order-zero component currents. Differentiating the locally finite sum (1.2) shows

    d'd''[u]=d'd''[v]  <==>  sum_i m_i R_i=0.              (6.2)

For a current T=sum_i c_i delta_i classified above,

    d'd''(uT)-d'd''(vT)=sum_i c_i R_i.                     (6.3)

Consequently, for a fixed pair satisfying (6.2), Bedford--Taylor independence for EVERY positive closed (0,0)-current is equivalent to

    R_i=0 for every i.                                     (6.4)

The reverse implication is (6.3); for the forward implication choose T=delta_i, which is itself admissible. This is an exact reduction, not a proof that the weighted relation (6.2) has no cancellation.

Let B_i=X_i intersect union_(j!=i) X_j. It is closed analytic, and the family (B_i) is locally finite. We claim

    Supp(R_i) is contained in B_i.                         (6.5)

Outside X_i, the current R_i vanishes by support. On X minus the union of the other components, formula (1.2) becomes delta_X=m_i delta_i. Restricting (6.2) there gives m_i R_i=0, hence R_i=0. Together these two open loci cover X\B_i, proving (6.5). This argument is on X itself; it does not infer injectivity of arbitrary finite proper pushforward.

If dim B_i<n-1 locally for all i, the ordinary (n-1,n-1)-test forms have supports disjoint from B_i, by CLD 15.2.1(b). Equation (6.5) then forces R_i=0. Thus the proposed bidegree-zero independence holds on every fixed ordinary domain whose distinct analytic irreducible components meet only in codimension at least two. It also holds on any irreducible ordinary domain, where each B_i is empty. On a space with an ordinary-neighborhood basis of irreducible analytic opens, the latter argument gives the local result on arbitrary ordinary U.

The codimension-one case is left unresolved by this deduction. There the test degree is n-1 and the strict inequality needed by Proposition 15.2.1(b) fails. One must still exclude or realize cancellation of the R_i on those intersections for continuous psh pairs. The earlier curve proofs used special zero-atom arguments at rigid conductor points; their one-dimensional conclusion is not a proof of this higher-dimensional step. No weighted relation is silently divided componentwise at a shared divisor.

## 7. Examples and interpretation

For two reduced affine n-spaces crossing along an affine (n-1)-space, (1.1) allows independent nonnegative coefficients on the two components. It thus explains the earlier current delta_1+2 delta_2. Formula (6.2) can only compare the two possible curvature defects on their intersection; this example of a current is not by itself a counterexample for any continuous psh pair.

For a crossing of codimension two, take in affine (n+2)-space with coordinates z_1,z_2,z_3,z_4,t_1,...,t_(n-2) the union of the linear spaces

    X_1={z_1=z_2=0},   X_2={z_3=z_4=0}.

Each component has dimension n and their intersection has dimension n-2. The reduced union is good separated strict boundaryless after analytification. The classification again permits arbitrary weights, but now (6.5) and the test-degree inequality rule out every component curvature defect. Hence the fixed-domain bidegree-zero statement holds for every equal-curvature continuous pair on this union. The singular space is not normal; normality was a sufficient way to obtain a single scalar, not necessary for this componentwise conclusion.

For a thickened irreducible space of generic multiplicity m, the canonical current is m times the reduced component current, while a general positive closed scalar current has any nonnegative coefficient c. The factor converting it to a multiple of the canonical current is c/m. It must not be replaced by c without changing conventions.

## 8. What this does and does not settle

Subject to independent and production verification, the proposed classification removes normality and reducedness from the scalar-current description over the retained field. It supplies irreducible-domain and codimension-at-least-two component-intersection cases of p=0 independence. The new ordinary-complement bridge and the analytic-support observation are supplied with their actual hypotheses.

It does not settle general positive-bidegree currents, the divisorial component-curvature cancellation question, discontinuous-potential versions, arbitrary valued fields, or envelope regularity. No claim of novelty is made for the classification or reductions. This complete manuscript has not yet been independently or production verified and is not a book theorem.
