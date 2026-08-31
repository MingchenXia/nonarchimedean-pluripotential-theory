## 1. The function class and the two different field scopes

For an analytic space Y, write A(Y) for the real-valued continuous functions which, on an ordinary neighborhood of each point, are uniform limits of sequences of ordinary CLD-smooth psh functions. Uniform convergence can equivalently be required on compact subsets of that neighborhood: shrink to a relatively compact ordinary neighborhood when using the uniform formulation. The approximating neighborhood must work for the entire sequence. A locally uniform smooth approximation with unrelated shrinking domains is not sufficient.

This is the first continuous-approximation stage. Its functions are locally approachable continuous psh functions in CLD Section 8.1. To see that uniform approximation also gives decreasing smooth approximation after shrinking, suppose f_j tends uniformly to f and put e_j=||f_j-f||. If infinitely many e_j vanish, f is itself smooth psh. Otherwise take a subsequence with e_(j+1)<e_j/3. The functions f_j+2e_j are smooth psh, decrease, and tend to f. Indeed f_(j+1)+2e_(j+1)<=f+3e_(j+1)<=f+e_j<=f_j+2e_j. No converse assertion concerning the whole transfinite CPsh sheaf is used. Throughout, strictness means the usual strictly K-analytic condition; this is sufficient also over a trivially valued field, without relying on CLD's enlarged strictness convention in Section 11.8.1.

Here are the two proposed conclusions.

(I) Let K be any complete non-Archimedean field. Let X be good, separated, strict, boundaryless and pure of dimension n>=1, with reduced analytic irreducible components X_i. Write j_i:X_i->X and delta_i=(j_i)_*delta_(X_i), and let m_i>0 be the generic multiplicities of X. For u,v in A(X),

    d'd''(u delta_X)=d'd''(v delta_X)
      if and only if
    d'd''(u delta_i)=d'd''(v delta_i) for every i.       (1.1)

No normality, reducedness, discreteness, residue-characteristic condition, or codimension-two intersection condition is imposed in (I).

## 2. The exact known analytic-nullity input

CLD 1204.6277v2, Corollary 16.9.4, states the following for a boundaryless n-dimensional analytic space: if u_1,...,u_m are continuous psh and locally approachable, every coefficient measure

    d'd''[u_1] wedge ... wedge d'd''[u_m] wedge alpha

with alpha a smooth (n-m,n-m)-form gives zero mass to a Zariski-closed analytic subset of dimension <n. The analytic hypotheses used here are within its good, separated setting. Its statement does not restrict the complete base field to nontrivial or discrete valuations. We use only m=1 on the reduced pure-dimensional component spaces.

The preceding Corollary 16.9.3 and Theorem 16.9.2 establish this by integrability against a locally approachable psh function V. The analytic step for a closed analytic Z with dim Z<n is local: on an affinoid neighborhood, prime avoidance chooses f vanishing on Z but on no top-dimensional component. The function log|f| is locally integrable for canonical integration and has pole set containing Z. The truncations log max(|f|,t), followed by smooth convex approximation of the maximum in the moment coordinates, supply its local approachability. Applying the integrability statement to V=log|f| forces zero mass on Z.

The nontrivial weighted integrability estimate in CLD Section 8.12 is a KNOWN INPUT here, not re-proved or generalized. Its proof uses smooth approximants of all potentials on a common neighborhood, the weighted Chern--Levine--Nirenberg inequality of Proposition 8.4.3, uniform-limit continuity, and monotone convergence of the truncations. These hypotheses explain exactly why that source does not automatically prove the same conclusion for every CPsh function.

For clarity about signed coefficients, the consequence we need is total-variation nullity. If alpha is positive, the coefficient measure is positive and its mass on Z is zero. Locally on a fixed compact test support a symmetric alpha is a difference of two positive smooth forms. Apply the positive case to each summand. The total variation of their difference is bounded by their sum and therefore also gives zero mass to Z. A J-antisymmetric part has zero pairing with the symmetric curvature current. Smooth partitions of unity reduce general compact tests to these local calculations. Mere signed equality mu(Z)=0 would not suffice.

## 3. Component currents and their coefficient measures

Analytic irreducible components are locally finite on compact sets in the present good setting. More explicitly, Ducros Theorem 4.20 gives G-local finiteness, including finiteness on affinoid domains; a compact set is covered by finitely many affinoid neighborhoods. Each component has dimension n, and the intersections of distinct components have local dimension <n. Unions of components are closed analytic. Therefore

    B_i=X_i intersect union_(j!=i) X_j                  (3.1)

is closed analytic in both X and X_i and has local dimension <n. It may have dimension n-1. All arguments below can be localized near a given compact support; no global finite-component or paracompactness assumption is required.

A closed immersion j_i is finite and has no relative boundary. Hence X_i is good, separated, strict and boundaryless, pure n-dimensional. Its canonical integration current is positive and separately closed by integration and Stokes. The pushed current delta_i is positive and separately closed as well. The fundamental-cycle formula CLD 13.5.2 and Proposition 16.6.3 gives

    delta_X=sum_i m_i delta_i.                          (3.2)

This formula remains valid when X is nonreduced. We neither erase its generic lengths nor replace all m_i by one.

Pullback by j_i preserves the class A. Pullback of a smooth psh function is smooth psh, since it commutes with d', d'', and positivity. A uniform approximation remains uniform on the inverse-image neighborhood; after a further relatively compact shrinking it also has the needed compact-uniform version. Only functions and smooth forms are pulled back. There is no pullback of an arbitrary current through a singular map.

For w in A(X), put

    S_i^w = d'd''(w delta_i)
          = (j_i)_* d'd''[(w|X_i)].                     (3.3)

The equality follows by testing and proper pushforward: continuous multiplication commutes with the pushforward of the positive integration current, and differentials commute with proper pushforward. Equivalently it is CLD Proposition 8.5.6. Positivity and separate closedness of the current on X_i follow from Lemma 8.5.5, or directly by the local uniform smooth approximation. Positivity and closedness then pass to its pushforward.

Let alpha be a smooth compactly supported (n-1,n-1)-form on X. Its pullback j_i^*alpha has compact support since j_i is topologically proper. The coefficient measure of S_i^w wedge alpha is precisely the pushforward of

    d'd''[(w|X_i)] wedge j_i^*alpha.                     (3.4)

This identity is first checked on smooth scalar test functions, by the definition of pushforward and (3.3). The coefficient measures are Radon; density of smooth compact scalar tests then identifies them as measures. Section 2, applied on X_i, shows that (3.4) has total variation zero on B_i. Pushforward preserves that nullity, because the total variation of a pushed signed measure is at most the pushforward of its total variation and j_i^(-1)(B_i)=B_i. Consequently

    |S_i^w wedge alpha|(B_i)=0.                         (3.5)

The same assertion holds locally for smooth forms not originally compactly supported, after multiplying by a compact cutoff. We will use (3.5) separately for u and v, not try to infer it from positivity of their difference.

## 4. Proof of the componentwise equivalence

Set R_i=S_i^u-S_i^v. Differentiating the locally finite sum (3.2) gives

    d'd''(u delta_X)-d'd''(v delta_X)=sum_i m_i R_i.     (4.1)

Thus componentwise equality implies canonical equality. Conversely assume the left side is zero. Outside X_i, R_i is zero by support. On the ordinary open X minus union_(j!=i) X_j, the canonical current equals m_i delta_i, so (4.1) implies m_i R_i=0 there. Since m_i is a strictly positive integer, R_i vanishes on that open. These two open sets cover X minus B_i. Therefore

    Supp(R_i) is contained in B_i.                      (4.2)

This is an equality argument entirely on X. It does not assume that pushforward by a normalization is injective, and does not divide (4.1) by m_i at points shared with another component.

Fix a compact smooth test alpha of degree (n-1,n-1). The signed coefficient measure R_i wedge alpha vanishes on X minus B_i: there R_i is the zero current, and smooth scalar tests determine the coefficient measure by density. On B_i its total variation is zero, since each of S_i^u wedge alpha and S_i^v wedge alpha has that property by (3.5). A signed Radon measure supported on B_i with zero total variation there is zero everywhere. A compact cutoff equal to one near Supp(alpha) now gives

    <R_i,alpha>=0.

This holds for every compact test, so R_i=0. It proves the forward implication in (1.1). The argument treats divisorial component intersections in exactly the same way as higher-codimension intersections. The extra input, compared with the preceding frozen classification note, is analytic-nullity of these PARTICULAR curvature coefficient measures, not a claim that all positive closed (1,1)-currents give zero mass to a divisor.

### 4.1. A stronger common-curvature criterion

Let now u,v be arbitrary functions in the continuous uniform-closure sheaf CPsh(X), with equal canonical curvature S=d'd''[u]=d'd''[v]. No first-stage approximation is assumed for this argument. Put B=union_i B_i. Local finiteness and the component dimension statements above make B closed analytic of local dimension <n. Assume that S wedge alpha has zero mass on B for every compact positive smooth (n-1,n-1)-form alpha. Equivalently all its signed coefficient measures have total variation zero there.

The currents S_i^u=d'd''(u delta_i) and S_i^v=d'd''(v delta_i) are positive by CLD Lemma 8.5.5, applied on X directly to the positive closed current delta_i. This lemma uses the defining minimal uniform-closure sheaf and does NOT require a direct smooth approximating sequence. Differentiate (3.2) to obtain the two locally finite decompositions into positive currents

    S=sum_j m_j S_j^u=sum_j m_j S_j^v.                  (4.3)

For each compact positive alpha, the corresponding measures therefore satisfy

    0 <= S_i^u wedge alpha <= (S wedge alpha)/m_i,
    0 <= S_i^v wedge alpha <= (S wedge alpha)/m_i.       (4.4)

To justify these as measure inequalities, test first against nonnegative smooth scalar functions. The complementary sums in (4.3) are positive and locally finite; density extends the inequalities to continuous compact tests and hence to Radon measures. Thus both component coefficient measures have zero mass on B_i, since B_i is a subset of B. Their difference R_i still has support in B_i by the argument giving (4.2), which needed only continuous multipliers. The signed-total-variation argument following (4.2) then gives R_i=0. Decomposing arbitrary compact forms into positive ones proves the current equality.

This criterion needs no approximation of u or v. It needs the stated zero-mass hypothesis on their COMMON curvature, which cannot just be presumed. If one of u,v belongs locally to A, CLD Corollary 16.9.4 on X with m=1 gives that hypothesis for S because B has dimension <n. More generally, it suffices that every point have an ordinary neighborhood on which S=d'd''[a] for some a in A; apply the same source theorem on that neighborhood and then use a finite partition for each compact test. The source applies to the possibly nonreduced X with its canonical integration normalization. Alternatively its nilpotent multiplicities can be retained explicitly through the locally finite positive formula (3.2).

In particular a common curvature S=0 automatically satisfies the criterion: (4.3) is a positive weighted sum equal to zero, so every component curvature is already zero. None of these arguments asserts that arbitrary positive closed currents have zero analytic mass.

