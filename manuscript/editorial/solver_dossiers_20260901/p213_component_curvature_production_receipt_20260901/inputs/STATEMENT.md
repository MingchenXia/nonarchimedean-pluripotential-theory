# Componentwise equality from approachable or crossing-null common curvature

## Ambient space and notation

Let K be any complete non-Archimedean field, possibly trivially valued. Let X be a good, separated, usual-strictly K-analytic space, boundaryless and pure of dimension n>=1. X need not be reduced or normal. Let X_i be its actual reduced analytic irreducible components over K, let j_i:X_i->X be the closed immersions, and put delta_i=(j_i)_*delta_(X_i). Write delta_X for canonical integration and m_i>0 for the generic multiplicities; thus delta_X=sum_i m_i delta_i, locally finitely.

Let CPsh(X) denote the least subsheaf of real continuous functions containing the ordinary CLD-smooth psh functions and stable under local uniform closure. Let A(X) consist of real continuous functions which, on one ordinary neighborhood of each point, are uniform limits of a sequence of ordinary smooth psh functions defined on that same neighborhood. Compact-uniform convergence on that neighborhood is equivalent after a relatively compact shrinking. No identification of A with all of CPsh is assumed.

Write dd=d'd'', [w]=w delta_X, and

    B_i=X_i intersect union_(j!=i) X_j,
    B=union_i B_i.

These are locally finite closed analytic crossing loci of dimension <n. Products of continuous functions with the positive integration currents and their dd derivatives are interpreted as ordinary CLD currents.

## Target (I): first-stage componentwise equivalence

For every u,v in A(X),

    dd(u delta_X)=dd(v delta_X)
      if and only if
    dd(u delta_i)=dd(v delta_i) for every i.

There is no discreteness, residue-characteristic, perfectness, reducedness, normality, or codimension-two crossing assumption.

## Target (4.1): explicit common-curvature criterion

Let u,v be arbitrary members of CPsh(X) with common canonical curvature

    S=dd[u]=dd[v].

Assume that for every compactly supported positive ordinary smooth (n-1,n-1)-form alpha, the positive Radon measure S wedge alpha gives zero mass to B. Equivalently every signed coefficient measure S wedge alpha has total variation zero on B. Then

    dd(u delta_i)=dd(v delta_i) for every i.

The zero-mass hypothesis is satisfied in each of the following cases, included in this target:

- one of u or v belongs locally to A;
- every point has an ordinary neighborhood on which S has a potential a in A, namely S=dd[a] there;
- S=0.

The other potential need only be in CPsh. The local potential a need not equal either of the given potentials. The hypothesis of zero mass is NOT asserted for a completely arbitrary common CPsh curvature.

## External source interfaces and excluded targets

The proof imports only the established CLD current calculus, first-stage analytic-nullity theorem, and analytic component geometry: Chambert-Loir–Ducros, arXiv:1204.6277v2, Sections 7.2, 8.1, Lemma 8.5.5, Proposition 8.5.6, Sections 13.5.2 and 16.6, and Corollary 16.9.4 (with its locally approachable hypothesis retained); and Ducros, *Les espaces de Berkovich sont excellents*, AIF 59 (2009), Section 4, especially Theorem 4.20 and 4.21–4.24. The extracted proof states the exact uses, including positive coefficients, total variation, local finiteness, and canonical multiplicities.

The submitted target is precisely the classification-independent assertion (I) and Section 4.1 of the frozen source. It does NOT include conclusion (II), any classification of arbitrary positive closed scalar currents, a statement for every arbitrary current on every open, or unconditional polar nullity for all CPsh factors. No new general-CPsh weighted estimate is an input. Usual strictness is a hypothesis on X; it is not asserted to pass to every ordinary open over a trivially valued field.
