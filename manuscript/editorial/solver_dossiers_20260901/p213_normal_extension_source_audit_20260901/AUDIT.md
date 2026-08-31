# Normal singular extension: independent source and ordinary-topology audit

Date: 2026-09-01. Reviewer: `/root/p213_general_propagation_fresh_audit`.

This is a fresh source/interface report. It does not edit or replace any frozen manuscript, does not audit the not-yet-frozen normal-extension manuscript, and is not a production or novelty certificate. The earlier qualified scalar result is used only as the explicitly identified smooth-input theorem. The present investigation is independent of the author's new normal-extension proof.

## 1. Result and exact scope

The ordinary-topology obstruction can be resolved under the proposed hypotheses. More precisely, the source theorems and the explicit local argument below establish:

**Connected-complement lemma.** Let K be a complete nontrivially discretely valued field. Let W be a nonempty connected ordinary open subset of a good, strictly K-analytic, boundaryless normal space. Let S be a closed analytic subset whose intersection with every affinoid domain contains no irreducible component of that domain. Then W minus S is nonempty and connected in the ordinary Berkovich topology. Here S denotes its intersection with W.

For the proposed application, K has residue characteristic zero and S is the non-quasi-smooth locus. This S satisfies the required condition, is locally of dimension strictly below the ambient pure dimension n, and has ordinary-dense complement. No geometric connectedness assumption, algebraic closure, extension of K, global affinoid presentation, quasi-compactness, or global paracompactness of W is used.

The current-theoretic consequence furnished by CLD is a **uniqueness/injectivity** mechanism for already defined positive closed currents. It is not an existence theorem extending an arbitrary current from W minus S. Section 7 records that interface separately. A mathematical verdict on the author's subsequent exact normal-extension manuscript remains a separate review.

## 2. Sources actually checked and their precise roles

### 2.1. Bartenwerfer theorem as stated in Conrad's primary research paper

[Brian Conrad, Moishezon spaces in rigid geometry](https://math.stanford.edu/~conrad/papers/moish.pdf), §1.4, Theorem 2.1.1, and the proof of Lemma 2.1.3, printed pp. 2–5, were read. The ground field in the rigid portions is any complete nontrivially valued non-Archimedean field. Theorem 2.1.1 asserts unique extension of a bounded analytic function across a nowhere-dense analytic subset of a normal rigid space. No geometric-normality or algebraically-closed-field assumption is present. Conrad explicitly applies this theorem to idempotents to obtain connectedness of such complements in connected normal rigid spaces.

The attribution immediately preceding that theorem distinguishes Lütkebohmert's geometric-normality version from Bartenwerfer's general version. The original reference is W. Bartenwerfer, *Der erste Riemannsche Hebbarkeitssatz im nichtarchimedischen Fall*, J. Reine Angew. Math. 286/287 (1976), 144–163, DOI [10.1515/crll.1976.286-287.144](https://doi.org/10.1515/crll.1976.286-287.144). Attempts to read the original publisher PDF and EuDML record did not return accessible content. Therefore this report does **not** claim to have read or re-proved Bartenwerfer's original proof. Its exact theorem statement was verified in Conrad's primary research paper, not inferred from a search snippet.

### 2.2. Conrad's irreducible-component paper

[Brian Conrad, Irreducible components of rigid spaces](https://math.stanford.edu/~conrad/papers/irredpaper.pdf), especially §2.1, Lemma 2.1.4, §2.2, and the proof of Theorem 2.3.1, was checked. The terminology is rigid/admissible, not ordinary Berkovich topology. On Sp(A), an analytic V(I) is nowhere dense precisely when I avoids all minimal primes of A. Connectedness is detected by analytic idempotents. Normal connected rigid spaces are irreducible. These facts alone do not justify asserting that an arbitrary admissible or ordinary open subset is connected. Moreover, the extension argument inside the proof of Theorem 2.3.1 occurs after an algebraically-closed-field reduction; that reduction must not silently be discarded.

The later erratum in the Moishezon paper concerns assertions about line bundles/Fredholm hypersurfaces in §4 of the irreducible-component paper. None of those assertions is used here.

### 2.3. Ducros: the Berkovich local algebra and density interfaces

[Antoine Ducros, Les espaces de Berkovich sont excellents, AIF 59 (2009), 1443–1552](https://www.numdam.org/article/AIF_2009__59_4_1443_0.pdf), published version, was checked at the following locations:

- Theorem 3.4 and §3.4, pp. 1495–1496: local regularity, R_m and S_m are unchanged upon restriction to analytic domains; normality is R_1 plus S_2.
- Lemma 4.21 and Proposition 4.22, pp. 1505–1506: local dimensions and irreducible-component dimensions under analytic domains.
- Lemma 4.24, pp. 1506–1507: a Zariski open is ordinary-dense exactly when it meets every irreducible component.
- Proposition 5.14, p. 1517: normal analytic spaces have the same irreducible and ordinary connected components.
- Proposition 6.3, Remark 6.5 and Proposition 6.6, pp. 1522–1524: over a perfect field regularity equals quasi-smoothness, whose locus is Zariski open.

These are Berkovich assertions; they supply the interfaces missing from a rigid-only citation. The affinoid excellence input is Theorem 2.13, also recalled in the proof of Theorem 3.4.

### 2.4. Affinoid interiors and rigid comparison

[Michael Temkin, Introduction to Berkovich analytic spaces, arXiv:1010.2235v2](https://arxiv.org/pdf/1010.2235v2), Definition 3.4.2.1, Fact 3.4.2.3, §4.2.4 and §5.4, was checked. An interior point has a convergent power-series presentation with strict inequalities for the coordinate values. Relative interiors compose; a domain's relative interior is its ordinary topological interior. Strict affinoid Berkovich and rigid domains use the same affinoid algebras and restriction maps, while their topologies are different. The strict affinoid Nullstellensatz identifies rigid points with maximal ideals having finite residue fields.

### 2.5. CLD current input

[Chambert-Loir–Ducros, arXiv:1204.6277v2](https://arxiv.org/abs/1204.6277v2), Definition 16.8.3, Example 16.8.4 and Theorem 16.8.5 including its proof, printed pp. 463–465, were reread in the exact pinned local text. A closed low-dimensional analytic subset in a topologically separated analytic space is tropical-H^q-null when its dimension is below q. On a boundaryless analytic n-space over a nontrivially valued field, every coefficient measure of a positive closed current of bidimension (q,q) is negligible there. The proof is local and does not impose global paracompactness on W.

The measure conclusion must mean nullity for total variation, not merely cancellation of the signed measure's mass on the whole set. Positivity and decomposition of local test forms into differences of positive forms justify the measure interpretation; one must not replace this with the invalid assertion that signed mass zero implies variation zero.

## 3. Why the singular set is nowhere dense on each domain

Let the ambient space be normal, pure n-dimensional, good, separated and boundaryless over the field in the proposed task. Residue characteristic zero implies characteristic zero for K, hence K is perfect. Define S to be the complement of the quasi-smooth locus; on a boundaryless space this is also the complement of the smooth locus.

Take an affinoid domain D=M(A) contained in W. Normality is inherited by D, by Ducros §3.4, and A is a normal excellent noetherian ring. Local regularity of D agrees with regularity of the corresponding local rings of Spec(A), by Theorem 3.4. Perfection then identifies this regularity with quasi-smoothness. Thus S intersect D is the closed analytic locus coming from the nonregular locus of Spec(A), not an unrelated topological exceptional set.

At each minimal prime p of the reduced ring A, A_p is a field and is regular. Excellence makes the regular locus Zariski open. Consequently its closed complement is defined by an ideal contained in no minimal prime. This verifies exactly Conrad's rigid nowhere-density criterion. Under the affinoid algebra/space component correspondence, D minus S meets every analytic irreducible component. Ducros Lemma 4.24 therefore gives ordinary density as well.

Purity is preserved under analytic-domain restriction. A proper closed analytic subset of each n-dimensional irreducible component has dimension below n; hence dim(S intersect D)<n. Normality's R_1 condition gives the stronger absence of height-zero and height-one nonregular primes, but the argument here needs only strict dimension drop. No assertion about the dimension of an arbitrary ordinary closed set is substituted for this analytic statement.

The same verification applies to all smaller affinoid domains used in overlaps. This matters: density only in the original large space would not, by itself, prove the needed rigid nowhere-density property after restriction.

## 4. Strict affinoid ordinary-neighborhood basis: explicit check

Given x in an ordinary open U contained in W, goodness and boundarylessness provide an affinoid neighborhood D_0 contained in U with x in its intrinsic interior. In an inner presentation

    K{r_1^(-1)T_1,...,r_m^(-1)T_m} -> O(D_0),  T_i -> f_i,

one has |f_i(x)|<r_i. Choose s_i in the divisible closure sqrt(|K^*|) with

    |f_i(x)| < s_i < r_i.

Such choices are possible since the group |pi|^Q is dense in the positive real numbers. The Weierstrass domain

    D = {y in D_0 : |f_i(y)| <= s_i for every i}

is strictly K-affinoid and is an ordinary neighborhood of x. Indeed its algebra has a quotient presentation by K{s^(-1)T}; radii in sqrt(|K^*|) give a strict K-affinoid algebra. If s_i^{e_i}=|a_i|, this strictness can also be expressed using the bounded variable T_i^{e_i}/a_i, with T_i integral over the resulting strict algebra. The strict inequalities at x exhibit an ordinary neighborhood contained in D. All constructions stay over K.

The relative-interior formula confirms x lies in the ordinary interior of D in W. Normality of D follows from Section 3. Neither D nor D_0 is asserted to be boundaryless as an entire affinoid space. It is also not asserted that every affinoid domain in a strict space is strict. Only the explicitly chosen neighborhood domains need be strict.

## 5. Ordinary discontinuity yields an admissible bounded idempotent

Suppose, for contradiction, that W minus S is the disjoint union of nonempty ordinary open-and-closed sets P and Q. Define h to be 0 on P and 1 on Q. Since it is locally constant, h is an analytic section on the ordinary open W minus S, and |h|<=1. This uses ordinary sheaf gluing of the two constant sections, not a claim that an arbitrary ordinary covering is an admissible rigid covering.

Fix a strictly affinoid neighborhood D=M(A) as above. Write S intersect D=V(f_1,...,f_r), using a finite generating family of its coherent defining ideal. If the set is empty the extension is already defined, so assume otherwise. For j=1,...,r and m>=1 put

    D_{j,m} = {y in D : |f_j(y)| >= |pi|^m}
            = M(A{T}/(f_j*T-pi^m)).

These are strict Laurent domains, contained in D minus S. They cover every Berkovich point of D minus S; for each such point one may choose m large enough to make the displayed lower inequality strict. On each D_{j,m}, h is a global analytic function in its affinoid algebra. The restrictions agree on intersections.

Here is the needed G-admissibility check, rather than an unproved topology transfer. For a rigid affinoid test V=Sp(B) mapping to Sp(A) minus V(f_1,...,f_r), the pulled-back f_j have no common maximal zero. Hence they generate the unit ideal of B:

    1 = a_1*f_1 + ... + a_r*f_r.

Since the a_j are bounded, there is a uniform c>0 such that max_j |f_j(y)|>=c on M(B). Choose M with |pi|^M<=c. The finite family of pulled-back Laurent domains {|f_j|>=|pi|^M}, j=1,...,r, covers V. This is an admissible finite affinoid covering and refines the pulled-back family {D_{j,m}}. That proves the required admissibility of the displayed covering of the rigid complement.

Therefore the compatible affinoid functions really define a bounded rigid analytic function h_D on Sp(A) minus (S intersect D)^rig. Its values at rigid points have bound 1, sufficient for Conrad Theorem 2.1.1. The correspondence uses actual affinoid algebras and maps, not a passage to an alteration, a finite extension, or a hypothetical global rigid model for W.

## 6. Extension and ordinary gluing

Conrad Theorem 2.1.1 now gives a unique H_D in A extending h_D. Its Berkovich analytic function agrees with the original h on each D_{j,m}, since the affinoid restrictions agree. Also H_D^2-H_D restricts to zero on the rigid complement. Uniqueness of extension, applied to the zero function, implies

    H_D^2 = H_D in A.

This is an algebraic identity, not just pointwise equality at selected classical points.

Consider two chosen domains D and D'. Their ordinary interiors overlap in an ordinary open. For each point of this overlap, choose a smaller strict affinoid ordinary neighborhood E contained in both interiors. Section 3 verifies normality of E and nowhere density of S intersect E. Both H_D|E and H_D'|E extend the same h on E minus S. Extension uniqueness on Sp(O(E)) therefore proves equality on E. Since these E cover the overlap ordinarily, the analytic sections agree on the whole overlap.

The H_D consequently glue over the ordinary interiors to H in O(W), and H^2=H. At each Berkovich point, evaluation in its completed residue field makes H equal to 0 or 1. Continuity of |H| then makes {H=0} and {H=1} ordinary open-and-closed subsets of W. Both are nonempty because H restricts to h on P and Q. This contradicts ordinary connectedness of W.

Nonemptiness of W minus S follows from its ordinary density and nonemptiness of W. This completes the connected-complement lemma, and in particular the ordinary connectedness of W_reg in the stated characteristic-zero normal case.

The proof is local followed by ordinary sheaf gluing. An uncountable cover causes no difficulty. There is no finite-cover, countable-exhaustion or global paracompactness step.

## 7. Current equality across the set: verified interface, not existence

The following is the appropriate elementary deduction from CLD's coefficient-measure nullity. Let T_1 and T_2 be positive closed currents of the same bidimension (q,q), already defined on W, with identical restrictions to W minus A. Assume A is closed and tropical-H^q-null. For any local smooth (q,q)-form alpha, the coefficient measures

    mu_i = T_i wedge alpha

have total variation zero on A. Their signed difference has zero restriction off A and total variation zero on A. It is therefore the zero Radon measure. These statements are local; smooth compact test functions on ordinary open subsets determine the Radon measures, and a compact cutoff equal to 1 near a test form's support recovers the current pairing. Hence T_1=T_2.

Do not apply CLD's positive-current theorem directly to T_1-T_2, which need not be positive. Apply it to each current first. Do not prove only mu_i(A)=0: cancellation of signed masses would be insufficient. Do not infer existence of T_i from this injectivity argument.

For the proposed p=0 application one sets q=n, A=S, and compares T with c times the canonical integration current. The smooth-input theorem on the now-connected ordinary W_reg furnishes the candidate c>=0. Completion requires the canonical integration current on the normal pure-dimensional space to be the intended positive closed current and to restrict to the same canonical normalization on W_reg. These are the concrete CLD integration/restriction checks for the forthcoming manuscript; this source report does not substitute a new manuscript for those checks.

## 8. Tests against false generalizations

**Normality is not disposable.** For n>=2 the analytification of Spec(K[x,y,z_1,...,z_{n-1}]/(xy)) is connected, reduced, pure n-dimensional, good, separated, strict and boundaryless. It is the union of two affine n-spaces meeting along an affine (n-1)-space. Its smooth locus is the disjoint union of the two branches with their intersection removed, namely {x!=0} and {y!=0}. Thus its smooth locus is disconnected in the ordinary topology. This is a counterexample to the proposed topological statement with “normal” weakened to “reduced”; it is not a counterexample under the actual hypotheses.

**Small ordinary dimension alone is not an extension hypothesis.** Removing a Gauss point from a Berkovich analytic line disconnects it. Such a point is not a closed analytic subspace of the line. Thus one cannot replace “closed analytic” in the connected-complement argument by an arbitrary small closed set, or justify connectedness merely by citing CLD's tropical nullity.

**Boundedness belongs to the theorem.** The function 1/t on a punctured disc does not extend holomorphically to its center. The idempotent used above is bounded by construction, so this obstruction does not occur.

**Perfectness is actually used.** Regularity and quasi-smoothness must not be identified over an arbitrary imperfect field. The present residue-characteristic-zero hypothesis avoids that issue. This report claims neither a same-proof extension to imperfect K nor geometric connectedness after base change.

**Topology is not cosmetic.** Normal connected equals irreducible in the appropriate category, by itself, does not prove that every open subset is connected. The analytic complement and bounded-idempotent argument are the work being done here. No conclusion about normalization-weighted currents on all reduced spaces is included.

## 9. Remaining obligations and freeze boundary

Resolved in this report: actual normal affinoid domains; strict ordinary-neighborhood basis; nowhere density of the non-quasi-smooth locus on every smaller domain; explicit rigid-admissible puncture covering; bounded analytic idempotent; ordinary uniqueness gluing; ordinary connectedness; exact hypotheses of the cited Riemann theorem; the uniqueness-versus-existence distinction.

For a future full normal p=0 theorem, the exact manuscript still needs an independent check of: (i) the imported smooth scalar theorem's unchanged n>=2/field/current conventions; (ii) canonical integration positivity, closedness and restriction normalization on singular pure-dimensional spaces; (iii) total-variation coefficient nullity and test-form recovery, not signed-set-mass cancellation; and (iv) any Bedford–Taylor corollary's exact continuous-psh and p=0 scope. These are review obligations, not assertions that a mathematical gap exists.

The forthcoming normal-extension draft was not an input to this report and receives no verdict here. Bartenwerfer's original 1976 proof was not accessible; the exact general theorem is verified through Conrad's stated primary research source. The online PDFs were read at the cited versions/URLs but were not archived or byte-pinned here. The local CLD text and earlier smooth theorem/report are pinned in REVIEWED_INPUTS.json. The read-only checker verifies only those identities and this report's checksum set, not any mathematical conclusion.
