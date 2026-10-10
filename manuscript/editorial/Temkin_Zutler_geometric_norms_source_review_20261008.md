# Geometric non-Archimedean norms: source audit, 8 October 2026

Controlling primary source: Michael Temkin and Grigory Zutler, *Geometrically multiplicative non-Archimedean norms*, arXiv:2608.19481v1 (19 August 2026), 15 pages, PDF SHA256 769d96661b6f1227ee6e0535ad707c91ddbf958c985d2fabf800f99500413abd. The complete text and all eight matching page images were actually read. Dependency reading covers Poineau's complete downloaded 33-page published PDF (31 article pages, printed 267–297, plus wrapper and blank page) and physical pages 36–51 of Temkin arXiv:0707.3953v3, 16 of its 60 pages. Combined actual coverage is 64 physical pages and 33 individually displayed images, two full files and one partial file. Preparation, discovery, export and checksum work earns no additional reading credit. This is not another full-book reread.

## Safe scope for a proposed Chapter 4 explanation

Retain the complete base field convention. Define the algebraic projective tensor seminorm by the infimum of the maximum of products over finite presentations, and form the separated completion explicitly. Distinguish multiplicativity of this norm, power multiplicativity of it, and multiplicativity of its spectral seminorm. Spectralization is the completion after dividing by the kernel of the spectral seminorm, which can be larger than the original seminorm kernel or the algebraic nilradical. The spectral seminorm is the greatest dominated power-multiplicative seminorm: the elementary power estimate proves the direction, contrary to the word “minimal” on primary page 2.

Poineau Definition 3.2, Remark 3.8 and Corollaries 3.14 and 3.16 (published pp. 279–283) are the exact sources for actual universal multiplicativity, its distinction from spectral multiplicativity, and the algebraically closed complete-base result. Lemma 3.1 (pp. 277–278) preserves isometric embeddings under the tensor seminorm in that complete-base convention. Universal lifting identifies a canonical dominating point of a scalar-extension fiber; it does not identify every point of the fiber with that lift. Poineau's proofs explicitly import Berkovich, BGR and Ducros's correction, which are not recursively read in this batch.

Proposed worked examples use only finite-dimensional coefficient estimates and elementary polynomial factorization: a purely inseparable self-tensor has a nonzero nilpotent with positive tensor norm but zero spectral norm; an unramified quadratic separable self-tensor is a product with complementary norm-one idempotents; distinct wild cubic conjugate fields can share a conjugate root without containing the chosen root; and a Gauss point has both a Gauss lift and a distinct evaluation lift over its own completed residue field. These are direct computations and explanatory consequences, not new theorem promotions or priority claims.

## Auxiliary assertions that cannot be imported as printed

1. The finite criterion in Lemma 4.2.1(iv), primary p. 11, fails for the generic S5 extension in the diagnostic proof below. Absence of an embedded nontrivial subextension of a chosen finite extension does not ensure the reduced tensor is a field. Its factors can have degrees two and three without a linear factor. This does not refute the universal relative-separable-closure criterion of Theorem 4.3.1: the base is not separably closed in the diagnostic field.
2. Example 3.6.3(a), primary p. 9, fails for distinct cubic conjugate fields over Q_3. The chosen root is absent but a different conjugate is present. The printed non-strict conjugate-distance condition also holds at equality. The separate equality-of-base-distance criterion is not contradicted.
3. In Lemma 3.1.1(iv), primary p. 6, ordinary injectivity into metric completion cannot detect an incomplete-base dimension loss. The Q_7 diagnostic distinguishes that automatic injection from the scalar-extended map V tensor_k k-hat -> V-hat. Restrict the explanatory book account to complete bases.
4. Corollary 3.5.2's coefficient orthogonality threshold requires distance normalized by |alpha|. In the Frobenius estimate of Lemma 5.2.1, use a strict margin r<s^p and s^p>|p| before choosing coefficient approximations; a non-strict unattained thickness bound does not supply a strict approximation. The main printed threshold must retain |p| and the completeness reduction where needed. No general incomplete-base perfectoid/spectrality theorem is cleared here.

## Dependency proof qualifications

All 25 dependency notes remain controlling. Poineau Theorem 2.14's witness algebra inverts P(x) and Q(y), and specialization applies to the point coordinates. Lemma 3.1's adapted approximately Cartesian basis uses s<=r, with a maximum over the presentation terms. Proposition 4.13's displayed coefficient clearing gives leading coefficient q, so applying its monic-polynomial boundary lemma requires further justification; the full general signature is not newly verified in this batch. Theorem 4.22's general-base algebraic-closure step also needs a stated reduction/descent. These observations do not assert counterexamples and are not used to change the book's existing topology results.

Temkin section 6 assumes analytic complete fields. Corollary 6.3.6 (v3 physical pp. 50–51) asserts stability only for type-2 or type-3 one-dimensional analytic fields over a stable analytic base. The split type-4 tensor calculation (pp. 44–45) needs both the translated Gauss upper bound and a contractive rational-evaluation lower bound; denominator roots lie outside the limiting disc because the distance to the algebraic closure is positive and unattained. This supplies the exact isometric identification under the split hypotheses, not merely an upper estimate. The prime-degree conjugate-distance argument in pp. 40–41 also uses transitivity of equal-radius clusters, besides Krasner. Type-4 fields are not asserted stable.

## Related open direction

Temkin–Zutler Remark 5.3.3 asks whether the uniform p-versal hypothesis can be weakened when the p-rank is infinite. A weak pointwise improvement and a uniform contraction factor are different quantifiers; they agree under the finite-p-rank hypothesis stated there. This remains an attributed research direction, not a new canonical atom or a solved problem. The broad criteria have not been certified by an independent model receipt.

The 42 canonical atoms and 12 formal problems are unchanged. General BJ22 Theorem 6.21 critical homogeneous Siu division and general envelopes remain OPEN; LPWZ density remains UNVERIFIED. No independent gpt-6.1-sol xhigh receipt is claimed. GitHub publication is not claimed. The native open-problem catalogue is unchanged.

## Complete direct finite diagnostics

# Direct finite-field diagnostics for Temkin–Zutler v1

These are worked checks of printed auxiliary assertions in arXiv:2608.19481v1, SHA256 769d96661b6f1227ee6e0535ad707c91ddbf958c985d2fabf800f99500413abd. They are not independent-model receipts, new theorem promotions, priority claims, or disproofs of the universal main criteria.

## A. The finite non-Galois criterion needs linear disjointness

Let E=Q(x1,x2,x3,x4,x5), with five algebraically independent variables. The full symmetric group S5 acts by permuting the variables. Put F=E^S5, G1=the subgroup fixing x1, H=the subgroup preserving the two sets {x1,x2} and {x3,x4,x5}, L0=E^G1, and K0=E^H. The finite group fixed-field theorem gives [E:F]=120, [L0:F]=5 and [K0:F]=10. In particular L0=F(x1), and its minimal polynomial is P(X)=product_{i=1}^5(X-xi), whose coefficients are symmetric and belong to F.

The subgroup H has two orbits of sizes 2 and 3 and fixes no xi. Therefore no root of P belongs to K0, and there is no F-embedding of L0 into K0. There is also no proper intermediate nontrivial extension of L0/F, since its degree is prime. Nevertheless over K0 the polynomial factors as

    P(X)=[(X-x1)(X-x2)] [(X-x3)(X-x4)(X-x5)].

Each factor has coefficients in K0 and is irreducible there, because H is transitive on its set of roots and E/K0 is Galois with group H. The factors are distinct and coprime. Consequently K0 tensor_F L0 is a product of a degree-two field and a degree-three field, rather than a field.

To obtain exactly the complete henselian real-valued signature of Lemma 4.2.1, use the Laurent series fields k=F((t)), l=L0((t)) and K=K0((t)), with |t|=exp(-1) and trivial coefficient norms. These are complete, l/k is finite separable of degree five, and both chosen extensions are unramified and defectless. Set A=K with its multiplicative norm, so A is initially spectrally multiplicative and its spectralized fraction field is K.

No k-embedding of l into K exists. Indeed an embedding would send x1 to a root of P in K. The only roots are the five constant xi in the common finite extension E((t)); an algebraic constant in K=K0((t)) must lie in K0. H fixes none of these roots. Since [l:k]=5, there are no other nontrivial separable subextensions of l to test. Henselization and completion change none of the three fields.

The tensor K tensor_k l is still the product of the two unramified factors, now of degrees 2 and 3 over K. The Cartesian tensor norm is the coefficientwise Laurent maximum and has two spectral points. Its spectral seminorm is their maximum and is not multiplicative: the two nonzero complementary idempotents have spectral norm one and product zero. Thus Lemma 4.2.1(iv) holds, but (i)–(iii) fail. A fixed finite-extension test must use the reduced tensor being a field, or the appropriate linear-disjointness condition, rather than only absence of an embedded subextension. The universal relative-separable-closure criterion is not refuted: k is already not separably closed in K, which contains the nontrivial constant extension K0/F.

The permutation and factor calculations are checked separately; the field-degree statements use the usual finite-group fixed-field theorem, not numerical evidence.

## B. A wild prime-degree extension can share a different conjugate

Let k=Q_3 and choose alpha with alpha^3=3. Then l=k(alpha) is a complete Eisenstein extension of degree three, with ramification index three, hence wild. Let zeta be a primitive cube root of unity in a common algebraic closure and put beta=zeta alpha, K=k(beta). The polynomial X^3-3 is also Eisenstein for beta, so [K:k]=3 and v(K^times)=(1/3)Z when v(3)=1.

Writing U=zeta-1, the cyclotomic equation is U^2+3U+3=0, Eisenstein of degree two. Therefore v(zeta-1)=1/2. In particular zeta is not in K, since its displacement from 1 has valuation outside (1/3)Z. Thus the chosen alpha is not in K: otherwise zeta=beta/alpha would belong to K. Nevertheless X^3-3 has the root beta in K, so K tensor_k l=K[X]/(X^3-3) is not a field. This disproves the field-equivalence step in Example 3.6.3(a) under its printed non-Galois prime-degree signature.

Its distance formulation has the same problem at equality. The distances between distinct conjugates of alpha have valuation 1/3+1/2=5/6, so r(alpha,k)=3^(-5/6). Also d(alpha,k)=3^(-1/3): every element of k has integral valuation, and cannot cancel alpha's valuation 1/3 more closely than zero does. For c in K,

    alpha-c=(alpha-beta)+(beta-c).

The first summand has valuation 5/6, while a nonzero second summand has valuation in (1/3)Z. They cannot have the same valuation, so the sum cannot be closer than alpha-beta. Taking c=beta attains that bound and gives d(alpha,K)=r(alpha,k)=3^(-5/6). Hence the displayed r<=d condition holds while the tensor is not a field. This does not contradict the separate criterion based on equality d(alpha,K)=d(alpha,k), which is false here.

## C. Ordinary normed completion is injective even when dimension drops

Give Q its 7-adic absolute value. The polynomial X^2-2 has a simple root 3 modulo 7, since 3^2-2=7 and 2*3 is a 7-adic unit. Hensel lifting gives alpha=sqrt(2) in Q_7, with alpha not in Q. Let V=Q+Q alpha, normed as a subspace of Q_7. It has Q-dimension two, and its metric completion is Q_7 because it contains the dense subfield Q.

The ordinary completion map V->Q_7 is injective and isometric. Its completed dimension is one over Q_7. It has no r-orthogonal Q-basis for any r>0: for any putative basis v1,v2, approximate v2/v1 in Q_7 by rational c_j. Then ||v2-c_j v1|| tends to zero while max{||v2||,||c_j v1||} is eventually ||v2||>0. This contradicts the fixed r lower bound. Thus condition (iv) of Lemma 3.1.1 cannot mean merely injectivity of ordinary metric completion. The relevant condition would be injectivity of V tensor_Q Q_7 -> V-hat, which fails here. This diagnostic does not apply to the book's default complete ground-field category, where finite-dimensional norms are equivalent to Cartesian norms.

## D. The spectral seminorm has the greatest dominated direction

For a submultiplicative seminorm alpha and a dominated power-multiplicative seminorm beta, beta(f)=beta(f^m)^(1/m)<=alpha(f^m)^(1/m). Taking the infimum/limit gives beta(f)<=rho_alpha(f). Provided the spectral seminorm is itself a seminorm, it is the greatest dominated power-multiplicative seminorm, rather than the minimal one printed on physical page 2. This is a direct reformulation of the book's existing spectral-bound calculation, not a new result.

All four checks leave the general BJ22 critical homogeneous Siu-division/envelope problem OPEN and LPWZ density UNVERIFIED. No independent gpt-6.1-sol xhigh verification receipt or canonical problem-status change is claimed.
