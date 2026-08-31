# Positive closed scalar currents on normal analytic spaces

Date: 1 September 2026. Research author: /root.

Status: new research candidate, not a live theorem or a production Rethlas result. This note extends the separately frozen quasi-smooth scalar-current assembly. Its new arguments require their own exact-final independent review. Known extension and nullity theorems are explicitly identified as external inputs, not presented as new results. No novelty claim or problem retirement is made.

## 1. Statements and dependency boundary

Let K be complete discretely valued with residue characteristic zero. Let X be a good separated strict boundaryless NORMAL K-analytic space, pure of dimension n>=2. The proposed conclusion is that on every nonempty connected ordinary open W of X, each positive ordinary CLD current T of bidegree (0,0), separately closed under d' and d'', has the form

    T = c delta_W,   for one unique finite c>=0.              (1.1)

Normality replaces the quasi-smoothness hypothesis of the preceding assembly. No global algebraization or projectivity is assumed. In particular, X is allowed to have singularities. We do not assert (1.1) on every connected reduced, nonnormal space.

Consequently, for a positive closed (0,0)-current on any ordinary open U of X and continuous functions u,v for which the curvature currents agree, one has

    d'd''[u] = d'd''[v]  ==>  d'd''(uT) = d'd''(vT).         (1.2)

This includes the continuous psh pairs in P21.3. No psh hypothesis on their difference is needed. It is still only the bidegree-zero subcase of P21.3, not the full question about all positive bidegrees, all singular spaces and all valued fields.

The quasi-smooth input is the complete frozen note

    ../p213_qualified_scalar_assembly_research_20260901/RESEARCH_NOTE.md
    SHA256 5809b99def2c16becb716eb2eb7c24382a8a31655b9b43902804e585cb53bb5c.

We use its theorem on arbitrary connected ordinary opens of good separated strict boundaryless quasi-smooth pure n-dimensional spaces, not merely its projective stage. Its independent audit is evidence about this input, not a proof premise or a production receipt. The new dependency chain is: coefficient-measure nullity gives uniqueness across an exceptional set; bounded analytic extension gives ordinary connectedness of the smooth complement; the quasi-smooth input determines T on that complement; uniqueness restores equality on W. None of the new conclusions is used in the quasi-smooth input.

Differentials d',d'' will be typeset with upright d in an eventual TeX integration. This research note introduces no new conventional theorem name.

## 2. Uniqueness across a set of zero tropical measure

This step has a wider scope than (1.1). Let K be any complete NONTRIVIALLY valued field, let Y be good separated boundaryless and pure of dimension n, and let 0<=p<n. Put q=n-p. Let A be a closed subset such that for every G-tropical chart F on a compact analytic domain D of Y, the set F(A intersect D) has zero q-dimensional Hausdorff measure. Let T_1,T_2 be positive closed ordinary CLD currents of bidegree (p,p) on Y. Then

    T_1|_(Y\A) = T_2|_(Y\A)  ==>  T_1 = T_2.              (2.1)

Here the source theorem is CLD Definition 16.8.3 and Theorem 16.8.5. The latter says precisely that each coefficient measure T_i wedge alpha, for an ordinary smooth (q,q)-form alpha, gives A zero mass. Nullity is used in the measure-theoretic sense: the restriction of its total variation to A is zero, not just cancellation of the total signed mass of A. The theorem applies to each positive closed T_i separately. It is not applied to their generally nonpositive difference.

For completeness, the deduction of (2.1) is as follows. Work on an ordinary neighborhood carrying a form alpha. Positivity makes the functional

    rho |-> <T_i, rho alpha>

an order-zero functional and hence a signed Radon coefficient measure mu_i; the usual decomposition into positive coefficients, or the explicit coefficient conclusion of CLD 16.8.5, handles alpha without a positivity assumption. Equality of the two currents on Y\A gives equality of mu_1 and mu_2 on that open set: smooth compact functions test their restrictions, and ordinary smooth density extends this equality to all continuous compact tests. Set mu=mu_1-mu_2. The two nullity conclusions imply

    |mu||_A <= (|mu_1|+|mu_2|)|_A = 0.

The restriction of mu to the complementary open set is also zero, so mu is the zero measure. Thus all localized coefficient functionals agree. For a compactly supported test form, choose finitely many such ordinary descriptions and a subordinate smooth partition of its compact support. The equality just proved on each piece gives equality on the original test form. Global paracompactness is unnecessary: the partition is finite on the particular compact support. This proves (2.1).

In particular, restriction to Y\A is injective on the cone of positive closed currents in this bidegree. This is a UNIQUENESS assertion. It does not say that a current given only on Y\A has a locally finite extension across A, let alone a closed or positive extension. For a positive closed current already defined on Y and supported on A, comparison with zero in (2.1) gives T=0.

A useful sufficient condition is that A be a closed analytic subset of dimension <q. Indeed it is weakly analytic of that dimension: on compact affinoid pieces take generators of its ideal and their common zero fibre, and cover a compact analytic domain by finitely many such pieces. CLD Example 16.8.4 then makes A tropical H^q-negligible. Equivalently, every relevant tropical image has dimension at most dim A<q. This is an all-chart assertion, not nullity in one chosen moment map. The local dimension bound suffices when there is no global finite affinoid cover.

For p=0 we require only dim A<n. The singular locus of a normal characteristic-zero space will satisfy the stronger bound dim A<=n-2. For general p, the displayed sufficient inequality is dim A<n-p, not merely dim A<n. That distinction prevents a false positive-bidegree extension.

## 3. Ordinary connectedness of the smooth complement

We give the ordinary-topology argument explicitly; rigid connectedness by itself is not substituted for it.

### 3.1. Analytic preliminaries and their exact scope

On a good strict analytic space, normality is compatible with analytic-domain restriction and with the affinoid algebra description. The precise Berkovich reference is Ducros, Les espaces de Berkovich sont excellents, Theorem 3.4 and Section 3.4: the relevant local properties are preserved on analytic domains, and normality is the conjunction R_1 and S_2. On a normal strict affinoid D=M(B), B is a noetherian normal ring; it is a finite product of normal domains when D is disconnected. The corresponding rigid affinoid Sp(B) is normal. Conrad, Irreducible components of rigid spaces, Sections 1.1--1.2 and the construction preceding Lemma 2.1.1, gives the strict rigid local-ring comparison. The good analytic and strict rigid descriptions use the same affinoid rings and rational-domain maps.

Since K has characteristic zero, it is perfect. On each such affinoid, the nonsmooth locus is a closed analytic subset, obtained from the Jacobian/smooth-locus criterion. It agrees with the nonregular locus and has codimension at least two by normality. Ducros Proposition 6.3, Remark 6.5 and Proposition 6.6 give regularity equals quasi-smoothness over a perfect field and the Zariski openness of this locus at all Berkovich points. The reduced closed ideals of its complement agree on overlapping affinoids by locality and define S=X\X_qs. Conrad's discussion before Lemma 3.3.2 and the characteristic-zero case of Lemma 3.3.5 give the corresponding strict affinoid codimension assertion. This is the quasi-smooth locus convention on a domain that may have boundary; on a boundaryless ordinary open it is the smooth locus. For a pure n-dimensional X, dim(S)<=n-2 locally. In particular S meets no affinoid irreducible component in a full-dimensional subset. Its complement is also ordinarily dense, by Ducros Lemma 4.24, not only Zariski dense.

We use the Bartenwerfer theorem in Conrad, Moishezon spaces in rigid geometry, Theorem 2.1.1: bounded analytic functions on the complement of a nowhere-dense analytic subset of a normal rigid space extend uniquely. Section 1.4 of that paper allows any complete nontrivially valued ground field. Neither algebraic closedness nor geometric normality is required for this version. The paper also explicitly applies the theorem to idempotents in the proof of Lemma 2.1.3. We use the theorem as an external analytic input; our argument below is the passage to the ordinary topology needed here.

### 3.2. From an ordinary disconnection to an affinoid idempotent

Let W be a nonempty connected ordinary open in X. It is still good separated strict boundaryless and normal. Suppose, for contradiction, that its smooth complement W^o=W\S is a disjoint union of two nonempty ordinary open-and-closed subsets U_0 and U_1. The function h equal to 0 on U_0 and to 1 on U_1 is an ordinary analytic function on W^o, by the sheaf property for this open cover. It is bounded by 1. We shall extend it as an idempotent over W.

Fix x in W and choose a strict affinoid neighborhood D=M(B) contained in W with x in the ordinary interior of D. Such neighborhoods exist here by goodness, strictness and boundarylessness. More explicitly, take an inner affinoid presentation at x and shrink the coordinate bounds from r_i to s_i in the divisible value group, with |f_i(x)|<s_i<r_i. The resulting strict Weierstrass domain remains a neighborhood of x. The relative/intrinsic interior identities give ordinary interior in W. This uses exactly the inner-presentation and interior facts spelled out in the preceding assembly audit; it does not call every G-domain ordinary open. Normality and purity persist on D.

Let f_1,...,f_r generate the ideal defining S intersect D; if the set is empty, take the generator 1. The rigid analytic subset Z_D=V(f_1,...,f_r) in Sp(B) is nowhere dense, since its dimension is at most n-2 and all components of B have dimension n. Choose any a in K with 0<|a|<1. The Laurent domains

    D_(j,m) = {y in D : |f_j(y)| >= |a|^m},  m>=1,        (3.1)

cover D\S. Their defining rings are B{a^m/f_j}=B{t}/(f_j t-a^m). They form an admissible cover of the rigid complement as well. One direct check is that on any affinoid rigid test space mapping into that complement the pulled-back f_j generate the unit ideal. Write 1=sum b_j f_j there. Boundedness of the finitely many b_j yields a uniform positive lower bound for max |f_j|, so finitely many domains at one sufficiently large m cover the test space. This is an admissible rational cover; it proves the required admissibility without identifying arbitrary G-covers with ordinary covers.

The restrictions of h to these affinoid domains give compatible elements of their affinoid algebras. They therefore define a rigid analytic function on Sp(B)\Z_D, bounded by 1. The Bartenwerfer theorem supplies H_D in B extending it. Equality of analytic functions on each D_(j,m) is equality in that affinoid algebra, so the extension agrees with h at all Berkovich points there, not merely the classical points. If desired this can also be checked using reducedness and the intersection of maximal ideals of a reduced affinoid algebra.

The analytic function H_D^2-H_D vanishes on the rigid complement. It is bounded on the affinoid D and extends the zero function. Uniqueness in the same theorem yields H_D^2=H_D. Thus no value other than 0 or 1 can occur for H_D at any analytic point.

### 3.3. Gluing on ordinary interiors

For two such neighborhoods D and E, consider their ordinary interiors in W. At a point of their overlap take a still smaller strict affinoid neighborhood F contained in that overlap. It is normal, and S intersect F has nowhere-dense rigid support by the same dimension argument. Both restricted functions H_D and H_E extend h on F\S and are bounded on F. Uniqueness in the Bartenwerfer theorem shows that they agree on F. Their ordinary germs therefore agree at every overlap point.

The ordinary interiors of the D cover W. Their functions glue to an ordinary analytic H on W, still idempotent, and H|W^o=h. The continuous function |H| takes only the values 0 and 1. Its two level sets are ordinary open and closed, and both are nonempty because U_0 and U_1 were nonempty. This contradicts connectedness of W.

The complement W^o is nonempty: a pure n-dimensional nonempty neighborhood cannot be contained in the analytic set of dimension at most n-2. We have proved that it is connected in the ordinary topology. There is no countability, global paracompactness, or global algebraization hypothesis in this argument. No extension of a current has been used, and no change of K has taken place.

## 4. Restoring the scalar-current identity across S

Let W and T satisfy (1.1). The restriction W^o is good separated strict boundaryless and quasi-smooth of pure dimension n. By Section 3 it is nonempty and ordinarily connected. Restrict T to it and apply the frozen quasi-smooth scalar assembly to obtain a unique finite c>=0 with

    T|W^o = c delta_(W^o).                                 (4.1)

The canonical integration current delta_W is defined on the whole, possibly singular, pure-dimensional space W. It is positive and separately closed by integration and Stokes; no smoothness of W is needed for this fact. Its restriction to W^o is delta_(W^o). Relevant CLD source interfaces are 7.3.1, Proposition 5.11.1 and Theorem 15.7.1, transferring the tropical integration formalism to analytic spaces with their analytic boundary. Here the boundary is empty.

Both T and c delta_W are thus positive closed (0,0)-currents already defined on W. The closed analytic subset S intersect W has dimension at most n-2<n and hence is tropical H^n-negligible. Apply (2.1) with p=0 to (4.1). This proves T=c delta_W on every compact test in W, including tests meeting S. There is no missing distribution supported on S: positivity and closedness of the two original currents, via CLD nullity, exclude it.

Uniqueness and finiteness of c already follow from restriction to W^o. Concretely, a small smooth ordinary neighborhood in W^o admits a compact positive top form of nonzero canonical integral, as established in the preceding assembly. Evaluation there determines c. The same argument covers c=0.

This establishes the proposed normal extension from the supplied quasi-smooth theorem and the stated standard inputs. It does not rely on a resolution of the singular analytic space W or on pulling T back to its normalization. Those operations would require their own current functoriality checks and are not used.

## 5. Equal-curvature pairs

The preceding scalar description is local on any ordinary U of X; connected shrinking is available for these analytic spaces. On a neighborhood where T=c delta and c is constant, multiplication by a continuous function is multiplication of the order-zero coefficient measures, so uT=c[u] and vT=c[v]. Differentiation of currents gives

    d'd''(uT) = c d'd''[u] = c d'd''[v] = d'd''(vT).

These local equalities glue, proving (1.2) even if U is disconnected. This argument does not assume that d'd''(uT)-d'd''(vT) is positive, or invoke a nullity theorem for that difference. The equality is obtained after the scalar identity has been restored across S. We do not differentiate u or v as ordinary smooth functions.

## 6. Examples and the necessity of the boundary of the statement

### 6.1. A normal quadratic cone

Over K, consider the affine n-dimensional variety

    Y = Spec K[u,v,w,z_1,...,z_(n-2)]/(uv-w^2).

Its coordinate ring is the invariant subring of K[s,t,z_1,...,z_(n-2)] under (s,t) |-> (-s,-t): u=s^2, v=t^2, w=st. The even-total-degree monomials in s,t are generated by these three elements, and their sole relation is uv=w^2 (reduce a polynomial using this relation and compare its distinct s,t monomials). The polynomial ring is integrally closed. If an element of the fraction field of the invariant ring is integral over that invariant ring, it is integral over the polynomial ring as well, hence lies in that ring; it is fixed by the involution, so lies in the invariant ring. This proves normality directly.

The partial derivatives of uv-w^2 are v,u,-2w. Since char K=0, its singular locus is u=v=w=0, of dimension n-2. Analytification preserves normality by the local comparison in Ducros Theorem 3.4, and this affine analytification is good, separated, strict and boundaryless. On every nonempty connected ordinary open of Y^an, including one containing a point of this singular locus, the proposed conclusion is T=c delta. The example illustrates exactly what the normal extension adds to the quasi-smooth theorem.

### 6.2. Two components crossing

Let Y be the reduced union uv=0 in affine (n+1)-space with coordinates u,v,z_1,...,z_(n-1). Its two components Y_1 and Y_2 are affine n-spaces and meet in affine (n-1)-space. Their analytic integration currents, pushed into Y^an by the closed embeddings, are positive and closed. Thus

    T = delta_(Y_1^an) + 2 delta_(Y_2^an)

is positive closed of bidegree (0,0). On the ordinary open where v is nonzero it has coefficient 1 relative to delta_Y, whereas on the ordinary open where u is nonzero it has coefficient 2. Both opens contain compact positive tests with positive canonical integral. It cannot be a single multiple of delta_Y on Y^an, which is connected because its two connected analytic affine components intersect.

The intersection is lower-dimensional and receives no coefficient mass from T. Thus zero mass on a singular set alone does not force the constants on disconnected complementary branches to agree. Normality entered precisely through the idempotent extension argument. This example disproves the unqualified constant-multiple assertion on all connected reduced spaces; it is NOT a counterexample to Bedford--Taylor independence and does not retire P21.3.

## 7. Verification status and remaining targets

All new deductions here remain a research candidate until separately reviewed and production Rethlas verified. The older candidate and its audit are frozen and are not rewritten by this extension. The source-review dossier is a separate literature check, not automatically an audit of this complete argument.

The uniqueness principle (2.1) works for positive bidegrees under its sharper tropical-dimension inequality. It does not supply the missing positive-bidegree smooth-case comparison. Normality removes one part of the singular-space restriction for p=0; it does not settle all nonnormal or nonreduced spaces. No arbitrary-field envelope theorem, full equivalence of psh definitions, or novelty claim follows. No live chapter or open-problem count is changed by this note.
