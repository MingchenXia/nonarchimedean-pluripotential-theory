# Numerical Cartier potentials on excellent local boundaries

## Abstract and exact status

We construct a geometric model core using effective exceptional Cartier divisors on primary-ideal blowups and numerical nefness on actual contracted integral curves. For every positive-dimensional excellent reduced local ring, without a normality, characteristic, residue-field, equidimensionality or resolution hypothesis, its uniform closure on every primary normalized semivaluation boundary is exactly the uniform closure of rational primary-ideal potentials. The main point is a finite-algebra correction: globally generated negative model sections need not be elements of the original ring, but multiplication by a fixed primary ideal produces downstairs primary ideals with a uniformly vanishing error. Evaluation is finite and continuous even at semivaluations with nonminimal support.

For a finite birational algebra differing from the ring only at its closed point, we prove an exact bounded descent theorem. In particular, an isolated nonnormal germ has the product of the bounded cones of its local normalization branches. In dimension one the normalization is itself a primary-ideal blowup, so the geometric model core already realizes every finite nonpositive branch profile, including mixed-zero profiles. This is distinct from the radial analytic comparison stipulated in the task.

These are scoped mathematical results, presented as unverified research drafts without a priority claim. They do not solve the original P12.2 residual. The construction below is bounded and continuous; an unbounded formal-psh extension and the general conductor interface remain open here. Within the explicit smooth BFJ model framework we prove an inclusion into its formal psh class and exhibit an unbounded BFJ member outside our bounded class; the source-framework dependency is recorded in Section 10. We make no assertion about singular envelopes, products, energy, or geometric finite-map pushforwards.

## 1. Background, conventions, and theorems

Write \(X=\operatorname{Spec}R\), where \((R,\mathfrak m)\) is a reduced excellent Noetherian local ring of positive dimension, and \(U=X\setminus\{\mathfrak m\}\). Primary always means \(\mathfrak m\)-primary, except when another maximal ideal is named. An ideal with maximal radical is primary in a Noetherian ring: in its Artinian local quotient every element is either a unit or nilpotent. The total quotient ring is obtained by inverting all nonzerodivisors. Since \(R\) is reduced and Noetherian, it is the product of the fraction fields of its finitely many minimal components. Every primary ideal contains a nonzerodivisor. Indeed no minimal prime is \(\mathfrak m\) in this positive-dimensional local ring, and finite prime avoidance applies. This does not assume pure dimension.

We use the following ordinary background with precisely these hypotheses. They are mathematical inputs, not caller correctness grants.

**B1. Commutative algebra.** Excellence gives finite normalization for reduced rings and their reduced quotients; finite algebras and localizations remain excellent. A normal one-dimensional Noetherian local domain is a DVR. We use elementary lying over, Chinese remainders, Nakayama, localization of finite modules, and the description of units in a local ring. Only the finite-normalization consequence of excellence is needed for the boundary nonemptiness and normalization results; the bounded comparison proof itself uses only Noetherian projective geometry.

**B2. Proper coherent geometry.** For a proper morphism from a Noetherian scheme to a Noetherian affine scheme, the direct image of a coherent sheaf is coherent. Its module of sections is finite and localizes to the sections over base localizations. For a projective morphism and an ample invertible sheaf \(A\), every coherent sheaf \(F\) has \(F\otimes A^n\) relatively globally generated for all sufficiently large integers \(n\). Over an affine base relative global generation is generation by its finite module of global sections. We also use the proper valuative criterion, including valuation rings that are not discrete.

**B3. Ampleness.** On a projective scheme over an arbitrary field a real Cartier class with nonnegative degree on every integral curve is nef; a nef real class plus a positive multiple of an ample class is ample. In any fixed finite real span of line-bundle classes the ample set is open. A rational ample class has an ample integral multiple after clearing denominators. Ampleness on a closed fiber of a projective morphism is relative ampleness on a base neighborhood of that fiber. Over a local base an open neighborhood of the closed point is the entire base. Ampleness is unchanged by nilpotent thickening of the fiber. These facts apply to possibly reducible and nonpure-dimensional projective fibers; zero-dimensional fibers cause no exception. Our applications take place on the closed fiber, with real classes in a fixed finite span, so no unproved assertion about nef Weil traces is being used.

**B4. Blowups.** The blowup of a finite ideal is projective with its relatively ample tautological invertible ideal and has the universal property of making that ideal invertible. We explain below the reduced charts, the effective divisor, and the product domination needed in this paper. No cofinality among all projective modifications is assumed.

For a primary ideal \(\mathfrak a\), put

\[
V_{\mathfrak a}(R)=\{v:R\longrightarrow[0,+\infty]:v\text{ is a semivaluation},\ v(\mathfrak a)=1\}.
\]

Semivaluations are nonnegative, multiplicative, ultrametric, and satisfy \(v(0)=+\infty\), \(v(1)=0\). We exclude the closed-point semivaluation by the normalization. For a finite ideal \(I=(f_j)\), \(v(I)=\min_jv(f_j)\); ultrametricity and nonnegative coefficients prove independence of generators. Put

\[
\mathcal I_{\mathfrak a}(R)=\{0\}\cup\{-k^{-1}v(I):k\geq1,\ I\text{ primary}\},\qquad
C^{\mathrm{id}}_{\mathfrak a}(R)=\overline{\mathcal I_{\mathfrak a}(R)}^{\|\cdot\|_\infty}.
\]

This fixes the exact ideal family compared in arbitrary dimension. On reduced curves it agrees with the dossier's uniform closure of principal profiles, as independently proved in Section 9.

The finite-transfer fragment also defines an unclosed cone \(\mathcal P_{\mathfrak a}(A)\) of finite nonnegative real combinations of positive ideal gauges \(v(J)\), with \(J\) containing a boundary power. To compare exactly with that convention, define \(\mathcal F_{\mathfrak a}(R)\) to be the finite nonnegative real combinations of \(-v(J)\), with \(J\supseteq\mathfrak a^N\) for some \(N\). On a local ring each such ideal is primary or the unit ideal. On a normal local ring this is precisely the sign reversal \(-\mathcal P_{\mathfrak a}(R)\) of that fragment's finite cone. We prove below \(\mathcal F\subseteq\mathcal G\) and \(\overline{\mathcal F}=C^{\mathrm{id}}\); equality of uniform closures is not equality of these unclosed families. The fragment's normalization-based cone \(\mathcal P^{\nu}\) is a further, distinct object, discussed in Section 8.

For \(Y=\operatorname{Bl}_{\mathfrak b}X\), let \(E_{\mathfrak b}\) be the effective Cartier divisor with \(\mathfrak b\mathcal O_Y=\mathcal O_Y(-E_{\mathfrak b})\). An exceptional integral Cartier divisor means a Cartier divisor with its canonical rational trivialization on \(U\), whose support is contained in the closed fiber. Define the *negative effective Cartier cone* to consist of divisors

\[
D=-\sum_{j=1}^s a_jB_j,\qquad a_j\in\mathbb R_{\geq0},\quad B_j\text{ effective exceptional integral Cartier}.
\]

This explicit convention matters on a nonnormal scheme. We do not silently identify it with a cone defined by Weil coefficients. For such a real divisor, relative numerical nefness means \(\deg(D|_C)\geq0\) for every integral proper curve contracted to the closed point. Degrees of real divisors mean the real linear extension of degrees of line bundles. Let \(\mathcal G_{\mathfrak a}(R)\) be the restrictions of \(v\mapsto v(D)\) for these numerically nef divisors on primary blowups, including zero, and let \(C^{\mathrm{num}}_{\mathfrak a}(R)\) be its uniform closure. The evaluation will be constructed independently of ideal functions.

**Theorem A (bounded numerical comparison).** Every function in \(\mathcal G_{\mathfrak a}(R)\) is finite, continuous, and nonpositive on \(V_{\mathfrak a}(R)\). Evaluation and numerical nefness are unchanged under common primary-blowup domination. Moreover

\[
\mathcal I_{\mathfrak a}(R)\subseteq\mathcal G_{\mathfrak a}(R)
\subseteq C^{\mathrm{id}}_{\mathfrak a}(R),\qquad
C^{\mathrm{num}}_{\mathfrak a}(R)=C^{\mathrm{id}}_{\mathfrak a}(R).
\]

The two uniform closures are closed convex cones stable under finite maxima. Primary changes act by the exact degree-one homogeneous cocycle and give equivalent uniform norms. The result extends to nonreduced excellent rings by applying the construction to their reduction; the zero-dimensional reduction has empty boundary.

**Theorem B (isolated finite-birational descent).** Suppose \(R\subseteq T\subseteq Q(R)\) is a finite algebra and is an isomorphism over \(U\). Let \(\mathfrak n_1,\ldots,\mathfrak n_q\) be its maximal ideals, and write \(A_i=T_{\mathfrak n_i}\). Restriction identifies \(V_{\mathfrak a}(R)\) homeomorphically with the disjoint union of \(V_{\mathfrak aA_i}(A_i)\), and under this identification

\[
C^{\mathrm{num}}_{\mathfrak a}(R)
\simeq\prod_{i=1}^q C^{\mathrm{num}}_{\mathfrak aA_i}(A_i).
\]

The isomorphism is isometric for the maximum of the branch uniform norms. This applies to normalization when \(R^\nu/R\) is supported at the closed point. It is not claimed for general conductor support.

## 2. The intrinsic boundary and primary gauge

The support \(\mathfrak p=\{f:v(f)=+\infty\}\) is prime: closure under addition and multiplication follows from the axioms, and \(v(fg)=+\infty\) forces at least one infinite value. Units have value zero, since their value plus that of their inverse is zero. If \(0<v(\mathfrak m)<\infty\), every element of \(\mathfrak m\) has positive value and every unit has zero value, so the center is \(\mathfrak m\). The support may be any proper prime, not just a minimal prime.

Choose \(r\geq s\geq1\) such that

\[
\mathfrak m^r\subseteq\mathfrak a\subseteq\mathfrak m^s.
\]

Then \(s\,v(\mathfrak m)\leq v(\mathfrak a)\leq r\,v(\mathfrak m)\). Thus primary values are positive and finite on the centered cone. The semivaluation axioms cut out a closed subspace of \([0,+\infty]^R\): addition and minimum in the extended nonnegative half-line are continuous, and its order relation is closed. The condition \(v(\mathfrak m)=1\) is closed because \(\mathfrak m\) is finitely generated. Consequently \(V_{\mathfrak m}\) is compact Hausdorff. Normalization by \(v(\mathfrak a)\) gives a homeomorphism between \(V_{\mathfrak m}\) and \(V_{\mathfrak a}\); the denominator is bounded away from zero and infinity by the preceding inequalities. Hence all primary sections are compact Hausdorff.

For nonemptiness take a maximal chain of primes ending at \(\mathfrak m\) and let \(\mathfrak p\) be the penultimate prime. Then \(R/\mathfrak p\) is a one-dimensional excellent local domain. Its finite normalization, localized at any maximal ideal over the closed point, is a DVR by B1. Its order, pulled back to \(R\), has positive finite primary value. This also shows why a nonminimal support can naturally occur in higher dimension.

For another primary ideal \(\mathfrak d\), the unique ray-preserving map is

\[
H_{\mathfrak a,\mathfrak d}(v)=v/v(\mathfrak d).
\]

If \(\mathfrak m^u\subseteq\mathfrak d\subseteq\mathfrak m^t\), then \(t/r\leq v(\mathfrak d)\leq u/s\) on \(V_{\mathfrak a}\). Its inverse and the identity \(H_{\mathfrak d,\mathfrak e}H_{\mathfrak a,\mathfrak d}=H_{\mathfrak a,\mathfrak e}\) follow by homogeneity. The centered cone is homeomorphic to \((0,+\infty)\times V_{\mathfrak a}\) by \(v\mapsto(v(\mathfrak a),v/v(\mathfrak a))\), so the boundary is the intrinsic ray quotient.

If \(n\) is nilpotent, multiplicativity gives \(v(n)=+\infty\). Applying the ultrametric inequality to \(f+n\) and \(f=(f+n)-n\) gives \(v(f+n)=v(f)\). Thus reduction preserves the topology, ideal values and all primary gauges. A reduced zero-dimensional local ring is a field and has no centered finite-radial semivaluation. This justifies precisely our reduction convention; it asserts nothing about intersection multiplicities.

## 3. Primary blowup models and numerical pullback

Fix a primary ideal \(\mathfrak b\). On the standard chart associated to \(f\in\mathfrak b\), the coordinate ring is \(R[\mathfrak b/f]\subseteq R_f\). The chart is reduced, and \(f\) is a nonzerodivisor there because it is invertible in \(R_f\). The pulled-back ideal is generated by \(f\). These charts give a reduced blowup, an effective Cartier divisor \(E_{\mathfrak b}\), and the relatively ample line bundle \(\mathcal O(-E_{\mathfrak b})\). Outside the closed point \(\mathfrak b\) is the unit ideal, so the model is an isomorphism over \(U\). Every irreducible component meets \(U\) densely: on a chart no component is contained in \(f=0\), since in a reduced Noetherian ring a nonzerodivisor avoids every minimal prime. Thus there are no extra components confined to the fiber, and functions vanishing on \(U\) vanish on \(Y\).

The models are directed. Indeed on \(\operatorname{Bl}_{\mathfrak b\mathfrak d}X\) the product ideal is invertible. The following elementary local argument separates the factors even over a reduced ring. If finite ideals \(I,J\) in a local ring with total quotient ring satisfy \(IJ=(e)\) with \(e\) a nonzerodivisor, then \(I(J/e)=A\). Write \(1=\sum i_lj_l/e\); one summand is a unit. Its factor \(i_l\) is a nonzerodivisor, and for every \(x\in I\), \(xj_l/e\in A\); dividing by the unit \(i_lj_l/e\) shows \(x/i_l\in A\). Hence \(I=(i_l)\) is invertible, and so is \(J\). Applying the universal property gives maps to both individual blowups. They are projective and surjective, since their closed images contain the dense copy of \(U\). Repeating the argument gives common domination for every finite collection of our models.

Numerical nefness is preserved by pullback. For an integral curve on a higher closed fiber, its image is a point or an integral curve on the lower closed fiber. The pullback line bundle has degree zero in the first case and has degree equal to the finite degree of the induced curve map times the downstairs degree in the second. Conversely, for any downstairs integral curve \(C\), a projective surjection has a point of its generic fiber with residue field finite over \(k(C)\). The closure of that point is an integral proper curve dominating \(C\): both schemes here are of finite type over the residue field, and dimension of the closure is the transcendence degree, namely one. Its degree formula detects the downstairs degree. Therefore pullback is nef if and only if the original divisor is nef. This works over nonclosed fields and for inseparable curve maps. It concerns Cartier pullback, not traces of Weil divisors.

## 4. Finite semivaluation evaluation and divisor bounds

Let \(v\in V_{\mathfrak a}\), let \(\mathfrak p\) be its support, and let \(K=\operatorname{Frac}(R/\mathfrak p)\). The finite-valued part extends to a real valuation of \(K\), with valuation ring \(V\). Since \(\mathfrak p\ne\mathfrak m\), the map \(\operatorname{Spec}K\to X\) lies in \(U\). Its unique lift to the model extends uniquely to \(\operatorname{Spec}V\to Y\) by properness and separatedness. Denote the image of its closed point by \(y\).

An exceptional Cartier divisor \(B\), with its rational trivialization on \(U\), has a local equation \(g\) near \(y\). That equation restricts to a nonzero element of \(K\), because it is a unit on \(U\). Define \(v(B)=v_K(g)\). A change of local equation multiplies by a unit of \(\mathcal O_{Y,y}\), whose image is a unit in \(V\) and has value zero. Thus the value is well-defined. This definition never subtracts two infinite values. It is compatible with Cartier addition and pullback, hence extends linearly to real Cartier divisors. The proper lift to a higher model composes to the lower one, proving evaluation independence under common domination.

For \(E=E_{\mathfrak b}\) the value is \(v(\mathfrak b)\). One can see this either from the universal property or directly: choose a generator \(f\) with minimal finite value; all ratios of other generators by \(f\) are nonnegative and give the chart map to \(V\). The pulled-back ideal is generated by \(f\). This argument also handles nonminimal supports.

There are uniform divisor bounds

\[
-N E\leq B\leq N E
\]

for some integer \(N\) depending on the integral exceptional divisor \(B\). To prove them take a finite affine cover on which \(E\) and \(B\) have local equations \(e\) and \(g\). The complement of the closed fiber on that affine is exactly \(D(e)\). Thus \(g\) and \(g^{-1}\) lie in \(A_e\), since the Cartier divisor with its given rational section is trivial there. Clearing powers of \(e\) gives \(e^Ng,e^N/g\in A\). These are nonzerodivisors, because they are invertible after localizing by a nonzerodivisor and \(A\to A_e\) is injective. Taking the largest exponent over the cover proves both effective inequalities. Along any proper valuation lift they give

\[
|v(B)|\leq N v(\mathfrak b).
\]

In particular all values are finite and bounded on a primary section. For a real linear combination \(\sum a_jB_j\), the bound is \(\sum |a_j|N_j\,v(\mathfrak b)\). An effective Cartier equation maps to a nonzero element of \(V\), hence has nonnegative value. Thus the negative cone has nonpositive values. All these statements are scheme-theoretic, with no use of divisorial density.

## 5. The finite-algebra correction and continuity

Put \(T=H^0(Y,\mathcal O_Y)\). Proper coherence makes \(T\) a finite \(R\)-algebra. The injection \(R\to T\) follows from the density of \(U\) on every component. Localization over \(U\) is the identity, so the finite module \(T/R\) is supported at the closed point. It is killed by \(\mathfrak m^h\) for some \(h\geq0\). Choose once for this model

\[
\mathfrak c=\mathfrak m^{h+1}.
\]

Then \(\mathfrak cT\subseteq\mathfrak m\subset R\). The stronger inclusion into \(\mathfrak m\) will ensure properness of the descended ideals; an arbitrary annihilator would not by itself ensure that.

Let \(D'\) be a negative rational exceptional Cartier divisor for which an integral multiple \(kD'\) has relatively globally generated line bundle. Because it is negative in the explicit effective-cone sense and \(k\) clears its coefficients, \(\mathcal O(kD')\) is a coherent invertible ideal subsheaf of \(\mathcal O_Y\). Its finite section module

\[
F_k=H^0(Y,\mathcal O(kD'))\subseteq T
\]

generates that line bundle. Define \(I_k=\mathfrak cF_k\subset R\), using finite sums of products. It is a finite downstairs ideal, lies in \(\mathfrak m\), and localizes to \(R\) at every nonclosed prime, because \(F_k\) and \(\mathfrak c\) both become the unit module there. Thus \(I_k\) is primary. No equality \(F_k\subset R\) has been assumed.

At the center of any proper valuation lift, choose a local generator \(s\) of \(\mathcal O(kD')\). In the rational trivialization its value is \(-k v(D')\): a Cartier equation for \(kD'\) is the reciprocal of this generator. Write the finite generating sections as \(h_ls\). They generate if and only if the \(h_l\) generate the unit ideal locally. Their images in \(V\) are nonnegative and at least one is a unit, so their minimum value is zero. The minimum value of the sections is therefore \(-kv(D')\). After multiplication by finite generators of \(\mathfrak c\), the minimum value of the resulting downstairs generators is the sum of the two minima. Consequently, on every semivaluation,

\[
v(I_k)=v(\mathfrak c)-k v(D'),\qquad
-k^{-1}v(I_k)=v(D')-k^{-1}v(\mathfrak c). \tag{1}
\]

Both sides are finite. This proves the sign and the correction exactly, including nonminimal supports. It does not claim \(I_k\mathcal O_Y=\mathcal O(kD')\); the actual equality is \(I_k\mathcal O_Y=(\mathfrak c\mathcal O_Y)\mathcal O(kD')\).

For continuity of an arbitrary integral exceptional \(B\), choose \(n\) large enough that \(B-nE\leq0\), by Section 4, and that \(\mathcal O(B-nE)\) is globally generated, by B2 applied to \(\mathcal O(B)\) and the ample \(\mathcal O(-E)\). Applying the preceding argument to the integral divisor \(B-nE\), with \(k=1\), gives a primary ideal \(I\) with

\[
v(B)=v(\mathfrak c)+n v(\mathfrak b)-v(I). \tag{2}
\]

Each primary ideal evaluation is a finite continuous function on the primary section: it is a finite minimum of coordinate evaluations and is bounded by the primary gauge inequalities. Equation (2) proves continuity of \(v(B)\), and finite real linear combinations prove continuity for every divisor used in Theorem A. This also proves that the evaluation depends on the Cartier divisor, not on its chosen real presentation.

## 6. Ample approximation and proof of Theorem A

Let \(D=-\sum a_jB_j\) be numerically nef on \(Y=\operatorname{Bl}_{\mathfrak b}X\). The line-bundle class of \(-E\) is relatively ample. For every \(\epsilon>0\), B3, applied to the projective closed fiber, makes

\[
D-\epsilon E
\]

relatively ample. The coefficients lie in a finite real span. Openness there lets us choose nonnegative rational \(a'_j\) and a positive rational \(\epsilon'\), arbitrarily close to \(a_j\) and \(\epsilon\), such that

\[
D'=-\sum a'_jB_j-\epsilon'E
\]

is relatively ample. Coefficients equal to zero cause no difficulty: approximate them by zero or small nonnegative rationals. Hence \(D'\) stays in the negative effective cone; no rational-polyhedral assertion about a nonnormal Weil effective cone is needed.

Write \(M_{\mathfrak b}=\max_{V_{\mathfrak a}}v(\mathfrak b)<\infty\) and use the constants \(N_j\) of Section 4. The elementary bound

\[
\|v(D)-v(D')\|_\infty
\leq M_{\mathfrak b}\left(\sum_j |a_j-a'_j|N_j+\epsilon'\right)
\]

shows that this error can be arbitrarily small, first choosing \(\epsilon\), then the rational approximation. Clear all denominators by \(q\). The ample invertible ideal \(\mathcal O(qD')\) has all sufficiently high powers globally generated by B2. For \(k=q\ell\) in that range, Equation (1) gives primary ideals \(I_k\), and

\[
\|v(D)+k^{-1}v(I_k)\|_\infty
\leq\|v(D)-v(D')\|_\infty+M_{\mathfrak c}/k,
\qquad M_{\mathfrak c}=\max_{V_{\mathfrak a}}v(\mathfrak c).
\]

The ideal \(\mathfrak c\) is fixed for the chosen model and independent of \(D'\) and \(k\). Thus the second error tends to zero; choosing rational perturbations with errors tending to zero proves \(\mathcal G\subseteq C^{\mathrm{id}}\).

Conversely, on \(\operatorname{Bl}_I X\), \(-E_I/k\) is negative and numerically nef. Its line-bundle class is \(k^{-1}\) times that of \(I\mathcal O_Y\), which is generated by downstairs generators. A globally generated line bundle has nonnegative degree on every integral proper curve: choose a section nonzero at the generic point, whose zero divisor has nonnegative degree. This proof works over arbitrary residue fields. Its evaluation is \(-v(I)/k\). Zero is realized by \(D=0\). Therefore \(\mathcal I\subseteq\mathcal G\), proving both inclusions and the equality of uniform closures.

The ideal family has the requisite cone and lattice structure after closure. Positive rational multiples are realized by powers of an ideal and a denominator. Given denominators \(k,l\), addition is represented by \(I^lJ^k\) with denominator \(kl\), and maximum by \(I^l+J^k\) with the same denominator. These ideals remain primary. Approximation of real scalars by rational scalars and continuity of addition and maximum in the uniform norm give a closed convex cone stable under finite maxima. This is not a claim about arbitrary suprema or usc envelopes.

There is also a comparison before closure with the finite-transfer cone just defined. A finite real combination \(-\sum c_jv(J_j)\) is the value of \(-\sum c_jE_{J_j}\) on a common primary blowup, omitting unit ideals. Each \(-E_{J_j}\) is generated and nef; their nonnegative real sum is nef and remains in the negative effective Cartier cone. Hence \(\mathcal F\subseteq\mathcal G\). Conversely the rational family is contained in \(\mathcal F\), and each finite real combination is uniformly approximated by rational combinations since its constituent gauges are bounded. Common denominators and product ideals turn those rational combinations into \(\mathcal I\). Thus

\[
\mathcal I\subseteq\mathcal F\subseteq\mathcal G\subseteq
\overline{\mathcal F}=C^{\mathrm{id}}=C^{\mathrm{num}}.
\]

This proves the precise signed comparison to the dossier's finite real cone wherever that cone is defined, while keeping the completion operation explicit.

For a homogeneous model function \(G\), its restrictions transform by

\[
(T_{\mathfrak a,\mathfrak d}u)(H_{\mathfrak a,\mathfrak d}(v))
=u(v)/v(\mathfrak d). \tag{3}
\]

The gauge bounds in Section 2 make \(T\) and its inverse bounded linear maps for uniform norms. They carry each ideal profile and each geometric model function to the same homogeneous object on the new slice, and hence carry their closures bijectively. The cocycle follows from \(H(v)(\mathfrak e)=v(\mathfrak e)/v(\mathfrak d)\). The nilpotent and dimension-zero assertions were proved in Section 2. This completes Theorem A.

## 7. Exact bounded descent under an isolated finite modification

We prove Theorem B. Since \(T/R\) is finite and supported at the closed point, choose a primary \(\mathfrak c\) with \(\mathfrak cT\subseteq\mathfrak m\). For any \(v\in V_{\mathfrak a}(R)\), choose \(d\in\mathfrak c\) of finite value, possible because \(v(\mathfrak c)\) is finite. For \(t\in T\), define

\[
w(t)=v(dt)-v(d),
\]

interpreting infinity minus this finite number as infinity. Independence of \(d\) follows by comparing \(d'(dt)=d(d't)\). Comparing \((dt)(du)=d(dtu)\) proves multiplicativity, and ultrametricity follows immediately. Restriction to \(R\) equals \(v\). The resulting values are nonnegative: if \(w(t)<0\), a monic integral equation for \(t\) over \(R\) has its highest-degree term of strictly smaller value than all others, impossible for a sum equal to zero. Thus \(w\) is a semivaluation of \(T\), with \(w(\mathfrak aT)=1\). Any other lift must satisfy this formula, so the lift is unique. This construction is elementary and uses no theorem about valuation extensions of fields.

All centers of such semivaluations on \(T\) are maximal ideals above \(\mathfrak m\), since \(T/\mathfrak mT\) is finite over the residue field. A semivaluation extends to the localization at its center, because denominators outside the center have value zero. Conversely every local branch semivaluation restricts to one on \(T\). There are finitely many centers. Chinese remainders provide an element zero modulo one center and one modulo every other, so the corresponding positive-value locus selects that center and the finite partition is clopen. The union of these branch links is compact Hausdorff by Section 2 applied locally. Restriction is continuous and bijective, hence a homeomorphism. This proves the boundary assertion without a hidden minimal-support assumption.

By Theorem A it suffices to prove the assertion for uniform ideal closures. A downstairs primary ideal extends to a primary ideal in each \(A_i\): its quotient is finite over an Artinian local \(R\)-quotient, and its extension is proper since it is contained in \(\mathfrak n_i\). Thus restriction of downstairs model functions lies in the product of upstairs bounded cones.

For the converse approximate a given tuple of upstairs functions uniformly by ideal profiles or zero, one on each of the finitely many branches. Synchronize their integer denominators by taking powers, writing them as \(-k^{-1}w(B_i)\), with \(B_i=A_i\) permitted for a zero profile. Contract each nonunit \(B_i\) to \(T\) and intersect the resulting ideals, putting the unit ideal for a unit component. The contraction contains a power of \(\mathfrak n_i\) and has radical \(\mathfrak n_i\), so its Noetherian quotient is Artinian local and it is primary; it localizes to the unit ideal at every other maximal ideal. Therefore their intersection \(H\subseteq T\) has \(HA_i=B_i\) for each \(i\), and is the unit ideal away from the closed-point fiber.

For every positive integer \(M\), \(I_M=\mathfrak c H^M\subset R\) is a downstairs primary ideal: it lies in \(\mathfrak m\) and is a unit at every nonclosed prime. On the branch \(i\), the product-of-minima identity gives

\[
-(Mk)^{-1}w(I_M)=-k^{-1}w(B_i)-(Mk)^{-1}w(\mathfrak c). \tag{4}
\]

The ideal value of \(\mathfrak c\) is uniformly bounded across the finite branch union by its downstairs primary gauge. Letting \(M\) tend to infinity and then improving the original branch approximations proves density of downstairs profiles in the entire product. The homeomorphism of links makes the norm identity immediate. This proves Theorem B.

This proof is function descent by finite ideals. It does not assert that every branchwise line bundle or Cartier divisor descends as such. The finite algebra can be the normalization, but an algebra with positive-dimensional discrepancy support falls outside Theorem B.

## 8. General normalization quotient and its remaining cone gate

For completeness we reconstruct the boundary facts used to formulate the general conductor gap. Let \(S=R^\nu=\prod S_j\subseteq Q(R)\) be the finite normalization, and \(\mathfrak f=(R:S)\). It contains a nonzerodivisor, by multiplying denominators for a finite set of module generators. It is an ideal of both rings, and \(R=S\times_{S/\mathfrak f}R/\mathfrak f\): an element of \(S\) with residue coming from \(R/\mathfrak f\) differs from an element of \(R\) by an element of \(\mathfrak f\subset R\).

Here is a short independent valuation-extension argument, needed only for the general quotient. Any local domain \(B\) inside a field \(L\) has a dominating valuation ring. Take by Zorn a maximal local subring of \(L\) dominating \(B\); unions of chains are local and continue to dominate. Call it \((W,M)\). If \(x\notin W\), then \(MW[x]=W[x]\), since otherwise a localization at a maximal ideal above \(M\) would strictly enlarge this local ring. If both \(x\) and \(x^{-1}\) were absent, the corresponding equality for \(W[x^{-1}]\) would give \(1=\sum_{j=0}^n b_jx^{-j}\), \(b_j\in M\). Multiplying by \(x^n\) and dividing by the unit \(1-b_0\) makes \(x\) integral over \(W\). Then \(W[x]\) is finite, and \(MW[x]\ne W[x]\) by Nakayama, a contradiction. Thus \(W\) is a valuation ring.

Given a downstairs semivaluation with support \(\mathfrak p\), choose a minimal component contained in \(\mathfrak p\) and a prime \(P\) of its normalization over \(\mathfrak p\), by lying over. The resulting field \(L=\operatorname{Frac}(S_j/P)\) is finite over \(K=\operatorname{Frac}(R/\mathfrak p)\). Let \(A\) be the valuation ring of \(v\) in \(K\), take its integral closure in \(L\), localize at a prime over its maximal ideal, and use the preceding construction for a dominating valuation ring \(W\). Then \(W\cap K=A\): if \(x\notin A\), its inverse belongs to the maximal ideal of \(A\) and hence of \(W\), so \(x\notin W\).

Its value group admits a unique extension of the given real embedding. Indeed for any \(z\in L^*\), a polynomial relation over \(K\) has at least two terms of minimal valuation. Otherwise a sum with a unique strict minimum could not vanish. Subtracting their values gives \((i-j)w(z)\in\Gamma_A\). Hence \(\Gamma_W/\Gamma_A\) is torsion, and one defines the real value of \(\gamma\) as the prescribed value of \(N\gamma\) divided by \(N\). Common multiples prove independence and order preservation. All elements of \(S_j/P\) are integral over \(R/\mathfrak p\subset A\), so lie in the integrally closed \(W\). Restriction, with infinity on \(P\), gives a normalized nonnegative real semivaluation lifting \(v\).

The disjoint union of all local normalization branch links is compact: there are finitely many components and centers, and each local extended primary ideal is primary. Restriction is a continuous surjection onto the compact Hausdorff downstairs link. Its equivalence relation is equality of restrictions, hence closed. If \(v(\mathfrak f)<\infty\), choose \(d\in\mathfrak f\) of finite value. Every lift is determined by \(w(s)=v(ds)-v(d)\), so the fiber is a singleton. If \(v(\mathfrak f)=\infty\), every lift annihilates \(\mathfrak f\), and equal restriction is precisely equality on \(R/\mathfrak f\) after factorization through \(S/\mathfrak f\). These strata are closed by finite generation. The quotient, its finite-conductor uniqueness locus, and these identifications commute with every primary gauge, since \(w(\mathfrak dS)=v(\mathfrak d)\).

Pullback of a downstairs bounded cone member therefore lies in the product of the local normalization bounded cones and is constant on all these fibers. The inclusion follows from extension of downstairs primary ideals and Theorem A; uniform convergence is preserved by pullback. We have not proved that every fiber-constant upstairs cone member is in this image when \(S/R\) has positive-dimensional support. A conductor \(\mathfrak f\) in that setting can have infinite value, so the error \(-v(\mathfrak f)/k\) is not uniformly finite. Equation (4) cannot be used with this conductor. The topological quotient theorem alone does not imply cone descent.

In particular we do not equate this downstairs cone with the fragment's unclosed \(-\mathcal P^{\nu}_{\mathfrak a}(R)\), defined by finite real ideal-cone membership on normal components and fiber constancy. That raw normalization cone is contained in the fiber-constant product of the upstairs uniform cones, as is the image of our downstairs cone, but these two inclusions do not compare the two downstairs classes in general. In the isolated case Theorem B gives surjectivity onto that whole product and therefore contains the raw normalization cone. It also gives the uniform closure of the raw normalization cone: finite local tuples in the finite real cones can be assembled on each semilocal normal component using ideals primary at one center and unit at the other centers, by contraction and Chinese remainders; then nonnegative real sums assemble the local combinations. Approximating the finitely many components proves that the raw normalization cone is dense in the product. No unclosed-cone equality is asserted.

## 9. Reduced curves, a geometric mixed-zero model, and radial comparison

Suppose now \(\dim R=1\). A normalized semivaluation has nonmaximal support, hence minimal support. The induced valuation ring of the component fraction field contains its finite normalization and dominates one of its DVR localizations. Every nonzero field element is \(u\pi^n\); units in the dominating DVR have value zero, so the valuation is \(c\operatorname{ord}_{\mathfrak n}\). Therefore the branch link is the finite discrete set

\[
v_i=\operatorname{ord}_{\mathfrak n_i}/d_i,\qquad d_i=\operatorname{ord}_{\mathfrak n_i}(\mathfrak a)>0.
\]

Different branches cannot give the same normalized valuation: different components have different infinite loci; on the same field proportional valuations have the same valuation ring and normalization center. This proves the classification, including multiple branches of an irreducible curve.

The normalization \(S\) is a semilocal product of Dedekind domains. Its conductor \(\mathfrak f\) is an invertible \(S\)-ideal, is a primary \(R\)-ideal unless \(R=S\), and satisfies \(\mathfrak fS=\mathfrak f\). If \(R=S\), it is a local DVR and one may use its maximal ideal instead. The normalized curve is itself \(\operatorname{Bl}_{\mathfrak f}X\). To check this, on a chart with generator \(f\in\mathfrak f\), every \(s\in S\) has \(fs\in\mathfrak f\), hence its image belongs to \(R[\mathfrak f/f]\subset R_f\) by \(s=(fs)/f\). These are exactly the charts of \(\operatorname{Bl}_{\mathfrak f}S\); the images of \(S\) are understood in the corresponding component localizations if \(f\) is a zerodivisor on another component. Conversely their chart generators already lie in the downstairs chart. Thus the charts agree, and since \(\mathfrak f\) is invertible on \(S\), that blowup is \(\operatorname{Spec}S\). This verifies membership in our chosen model system, rather than assuming arbitrary separated models are allowed.

Each closed point \(P_i\) of \(S\) is an effective Cartier divisor. There are no contracted integral curves: this model is finite over \(X\), with zero-dimensional closed fiber. Given any finite tuple \(u_i\leq0\), the divisor

\[
D=\sum_i d_i u_i P_i
\]

belongs to our negative effective cone, is numerically nef vacuously, and has \(v_i(D)=u_i\). Thus already the geometric core, not merely its uniform closure, is every finite nonpositive branch profile. The decreasing completion of this bounded cone is every profile in \([-\infty,0]^q\), by truncation \(u\mapsto\max(u,-n)\). This last statement concerns a finite set and is not a general unbounded formal-psh theorem.

For comparison with the dossier's principal ideal family, we give the independent conductor calculation. Factor the conductor as \(\prod\mathfrak n_i^{c_i}\), with all \(c_i\) finite because it contains a nonzerodivisor. For any integers \(k_i\geq\max(c_i,1)\), the invertible ideal \(J=\prod\mathfrak n_i^{k_i}\) lies in \(R\). Chinese remainders choose \(f\in J\) nonzero in each one-dimensional space \(J/\mathfrak n_iJ\); Nakayama shows \(J=fS\). It is a nonzerodivisor in \(R\), lies in \(\mathfrak m\), and its only possible prime zero is \(\mathfrak m\), so \((f)\) is primary with exact orders \(k_i\). Every strictly negative rational tuple is consequently \(-v_i(f)/N\) after choosing a common sufficiently divisible denominator. Such tuples are uniformly dense in the finite nonpositive orthant. This proves exact agreement with the principal ideal cone specified by the task without importing that earlier result as a grant.

For the node \(R=k[[x,y]]/(xy)\), normalization is \(S=k[[x]]\times k[[y]]\); its image consists of pairs with equal constant term, and its conductor is \(\mathfrak m=(x,y)\). The \(x\)-chart of the blowup is \(k[[x]]\), because \(y/x=0\) in \(R_x\); the \(y\)-chart is \(k[[y]]\), and their overlap is empty. Thus \(\operatorname{Bl}_{\mathfrak m}X=\operatorname{Spec}S\). Let \(D=-P_x\). It is nef, with profile \((-1,0)\) on the \(\mathfrak m\)-link. Yet

\[
H^0(S,\mathcal O(kD))=x^kk[[x]]\times k[[y]]
\]

contains \((0,1)\) and is not a submodule of \(R\). Multiplying by \(\mathfrak m\) gives the downstairs primary ideal \(I_k=(x^{k+1},y)\), and its profile is

\[
(-1-1/k,-1/k)\longrightarrow(-1,0).
\]

This is an explicit proof that uncorrected exact section descent fails and the finite correction has the stated sign.

The task's specified closed-disc radial comparator is \(\{0\}\cup[-\infty,0)^q\). Our finite cone is \((\mathbb R_{\leq0})^q\), and its finite-link decreasing completion is \([-\infty,0]^q\). Relative to that comparator, the additional functions are exactly the mixed-zero profiles: at least one zero coordinate and at least one negative coordinate, including minus infinity. For \(q=1\) the completed sets coincide; for \(q\geq2\) the containment is strict. In particular the node model above lies outside the stipulated radial class. Numerically separated fiber geometry imposes no branch compatibility at a nodal analytic value.

We do not prove or grant the full CLD/classical radial classification here: the frozen proof invokes GR25 and Chapter 15 results whose original bytes are not bound. Its stated cone is used solely as the requested comparison specification. The mixed-zero exclusion can be reconstructed conditionally using just two analytic premises: upper semicontinuity forces the nodal value to be at least zero along a zero branch, while a closed-disc maximum principle on a negative branch forces it to be negative. We have not supplied a primary-source proof of those analytic premises or of CLD decreasing closedness. No claim of radial CLD equivalence is a theorem of this paper.

## 10. Smooth complex specialization: an inclusion, not full recovery

Here only take \(R=\mathbb C[z_1,\ldots,z_n]_{(z)}\), and normalize by \(\mathfrak m\). The BFJ source uses this smooth algebraic germ, its completion, smooth projective modifications, simple normal-crossing models, and their quasimonomial faces. We use these source-defined objects only in this setting. This section has the explicit framework hypothesis that the BFJ simple models and monomial retractions exist, and that every primary ideal admits a simple principalizing model. The immediate BFJ units asserting this are available and were inspected, but their original Hironaka/principalization dependency is not among the frozen primary bytes. We therefore record this smooth-framework interface as conditional on that standard characteristic-zero geometric input, without a separate source-PASS for it. Theorems A and B and the curve-model theorem do not use this hypothesis. A primary ideal of the completion comes from \(R\): if it contains \(\widehat{\mathfrak m}^N\), truncate finitely many generators modulo that power and use the equality of the truncated quotients. Thus no completion mismatch is hidden in the primary model family.

Let \(u\in C^{\mathrm{num}}_{\mathfrak m}\). Theorem A gives uniform approximation by rational primary ideal profiles or zero, denoted \(u_j\). At every divisorial point their normalized coefficients converge to those of \(u\), so BFJ Definition 2.1 puts the associated Weil divisor in its weakly closed nef cone. Restriction of \(u\) to every closed quasimonomial face is continuous, since \(u\) is globally continuous. Therefore it is strongly continuous and is a formal psh function in BFJ Definition 2.5. On each face the primary ideal functions are convex: in monomial coordinates negative valuation is the maximum of the negative affine monomial orders. A finite set of minimal monomials suffices by the elementary ascending-chain property of monomial ideals. Uniform limits preserve convexity. This verifies the relevant positivity and regularity, rather than appealing to the one-branch test.

We check the all-semivaluation extension in Definition 2.8. Each primary ideal function satisfies that extension formula: retraction to any simple model decreases valuations of local functions by the monomial minimum, and on a simple model principalizing the primary ideal its pullback generator is a unit times a boundary monomial, so retraction preserves its ideal value. Hence

\[
u_j(v)=\inf_\pi u_j(r_\pi v).
\]

For \(\|u-u_j\|_\infty\leq\delta_j\), taking infima gives

\[
\left|\inf_\pi u(r_\pi v)-u_j(v)\right|\leq\delta_j.
\]

Letting \(\delta_j\to0\) yields \(u(v)=\inf_\pi u(r_\pi v)\) at every semivaluation, including those with nonzero support. This is the actual BFJ extension rule. The simple-model existence and retraction objects belong to the smooth characteristic-zero BFJ setting; no such assertion was used for Theorem A.

For \(n\geq2\), the BFJ function \(g(v)=-v(z_1)\) is an explicit member outside our bounded continuous cone. Its divisorial divisor is the weak limit of the primary ideal divisors of \((z_1)+\mathfrak m^N\). On closed quasimonomial faces it is finite, continuous and convex by the same monomial calculation, hence is formal psh. Its all-semivaluation extension is \(-v(z_1)\): on quasimonomial points \(\max(g,-N)\) is the primary ideal function just displayed; applying the extension formula and the identity \(\inf\max(f,-N)=\max(\inf f,-N)\) proves the equality for every \(N\), and then for \(g\). At the monomial valuations with weights \((t,1,\ldots,1)\), its value is \(-t\); at a normalized semivaluation supported on \((z_1)\) it is minus infinity. Thus it is unbounded and does not belong to any uniform closure of our bounded primary profiles. For \(n=1\) the boundary is a single point and the finite cones agree with the finite one-variable formal class, but this does not repair the higher-dimensional defect.

We therefore prove

\[
C^{\mathrm{num}}_{\mathfrak m}(R)
\subseteq\{\text{globally continuous BFJ formal psh functions on }V\},
\]

with exact extension and positivity. We do not prove the reverse inclusion or claim to recover all bounded, possibly discontinuous, BFJ functions. The source's multiplier-ideal route to decreasing approximation, including Proposition 3.11, is a different gate. Its discrepancy bounds are on individual faces, not uniform on the entire normalized link. We do not apply that route to singular, nonnormal, or positive-characteristic rings.

## 11. Source restrictions, diagnostics, and original scope decision

BFJ is the author-hosted published *Valuations and Plurisubharmonic Singularities*, Publ. RIMS 44 (2008), 449--494, 46 PDF pages, at the URL recorded in the source ledger. We inspected the immediate definitions and proofs for its divisor/function dictionary, weak nef cone, Cartier numerical comparison, formal psh definition, retraction extension and multiplier-ideal comparison units. Definition 2.1, Proposition 2.2, Definitions 2.5 and 2.8, and Proposition 3.11 address distinct operations. The numerical-to-ideal implication required by our construction is proved in Sections 4--6, not imported from a source label. The only positive smooth statement here uses the source's explicitly smooth formal class, with the direct argument in Section 10.

BdFFU is the author version compiled June 27, 2013, filename BdFFU-13-2706, 17 PDF pages. Its spaces in Section 2 are finite real valuations of the function field, over \(\mathbb C\); its singular multiplier-ideal results assume normal varieties. This cannot supply our nonnormal all-semivaluation cone. We make no positive application of its theorems.

A literal check of this BdFFU version shows a sign defect in Proposition 2.4(b): it prints \(r_\pi^N(\nu)(\mathfrak a)\geq\nu(\mathfrak a)\). Its proof instead obtains \(\nu(f)\geq\nu_w(f)\). On \(\mathbb A^2\), with \(N\) the origin and \(\pi\) its blowup, choose the monomial valuation in coordinates \(x,z=x+y\) with \(\nu(x)=1\), \(\nu(z)=2\). Then \(\nu(y)=1\), \(\nu(\mathfrak m)=1\), and retraction to the single exceptional vertex is ordinary order. For \(\mathfrak a=(x+y)\), its retracted value is one and its actual value is two. This contradicts the printed inequality and verifies the reverse sign independently. The same page calls a minimum of affine functions concave and then calls the resulting ideal evaluation convex. Both discrepancies are present in PDF typography, not just text extraction. These are diagnostics about the bound author version, not a verdict on other versions or other theorems.

The BFJ printed Proposition 3.13 says primary ideals even for the zero function. Literally, with primary meaning proper maximal-primary, a decreasing sequence of primary profiles cannot converge to zero: each first value is strictly negative and later values are no larger. Unit ideals must be allowed for the zero case, or that case stated separately. We do not apply this source statement without that distinction. Our family explicitly includes zero.

The original excellent-germ atom remains OPEN in this artifact. The proved geometric core meets the independent model-positivity portion and its bounded ideal comparison on all excellent reductions. It does not meet the requirement of the full smooth BFJ specialization, and its normalization comparison is exact only for isolated finite discrepancy. General conductor-compatible unbounded functions, positivity of their limits, and an extension mechanism for arbitrary excellent germs remain gates. Defining a decreasing completion would not by itself close them. The constructed numerical cone is also strictly different from the task's radial disc extension class on multibranch curves.

P12.3--P12.6 remain separate. We prove no obstacle-envelope regularity, Monge--Ampere product, local energy, or geometric finite-map trace. Primary gauge compatibility here applies to functions only. The optional ROOT311 route is a research suggestion, not support. No repository production receipt or reviewer claim is used. There is no priority or accepted-original claim; the recorded decision is candidate=false.
