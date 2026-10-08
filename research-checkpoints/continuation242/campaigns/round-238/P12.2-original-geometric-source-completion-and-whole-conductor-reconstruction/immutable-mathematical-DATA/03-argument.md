# Original P12.2: complete OPEN reconstruction

All statements are unverified drafts. The geometric comparison is conditional; original P12.2 remains OPEN.

## n1: Intrinsic boundary, conductor fibres and completion

Earlier local supports: none.

Intrinsic sections, finite restriction, conductor fibres, and completion.

Let (R,m) be a Noetherian local ring and a a proper m-primary ideal. A semivaluation takes values in [0,infinity], sends 0 to infinity and 1 to zero, is multiplicative, and satisfies the ultrametric inequality. The centred cone requires \(0<v(m)<\infty\). Its support is a prime strictly below m; it is never assumed minimal. Write \(V_a(R)=\{v:v(a)=1\}\), with pointwise topology in the compact extended interval. Ideal values are minima over finite generating sets. Expressing generators in terms of each other proves independence, \(v(IJ)=v(I)+v(J)\), and \(v(I+J)=\min(v(I),v(J))\). Units have value zero.

The axioms are closed in \([0,\infty]^R\): extended addition and minimum are continuous and the order relation is closed. The condition v(m)=1 is closed. If \(m^r\subset a\subset m^s\), then \(s v(m)\le v(a)\le r v(m)\). Consequently rescaling identifies the compact Hausdorff m-section with the a-section. All primary ideal values are positive finite continuous bounded functions on that section. For a second primary b, put \(H_{a,b}(v)=v/v(b)\). Its denominator and reciprocal are bounded; the inverse is H(b,a), and direct substitution gives \(H_{b,d}H_{a,b}=H_{a,d}\). A degree-one homogeneous function transforms by
\[
 h_b(H_{a,b}(v))=h_a(v)/v(b).
\]
The cone is the product of a section with the positive real radial coordinate v(a). A nonprimary ideal gives only the open domain where its value is positive and finite. Its section can be noncompact. The unit and zero ideals have no level-one section.

Nilpotents have infinite value. Applying the ultrametric inequality to f+n and then to (f+n)-n proves v(f+n)=v(f), so reduction preserves all sections and ideal gauges. A zero-dimensional local reduction is a field and has empty centred cone. If the reduced excellent local ring has positive dimension, a penultimate prime in a saturated chain gives a one-dimensional excellent domain quotient. Its finite normalization has a local normal one-dimensional factor, hence a DVR, whose order gives a point of every primary section. Here and subsequently, the algebraic consequences of excellence used are stability under quotients and finite-type localization, universal catenarity, and finiteness of integral closures in finite fraction-field extensions (the Nagata property). These are ordinary algebraic background at the stated excellent hypotheses; no resolution or characteristic assumption is inferred from them.

For a finite integral injection R into a reduced finite algebra B, restriction of the aB-section is onto V(a,R), retaining every support. To prove this, choose a prime P over the support p of v, and put K=Frac(R/p), L=Frac(B/P), a finite field extension. The valuation ring A of v in K has an integral closure A' in L. Choose a prime of A' above its maximal ideal, and a valuation ring W of L dominating that local ring. This existence can be proved by Zorn: a maximal dominating local subring is a valuation ring, because for each x either its maximal ideal stays proper in the extension by x or in the extension by its inverse. Indeed, a relation \(1=\sum_{i=0}^n a_i x^{-i}\), all a_i in the maximal ideal, makes x integral; lying over then makes that ideal proper in A[x]. Localization and maximality give the assertion. This is also the complete immediate argument of Swanson--Huneke Lemma 6.4.1 and Theorem 6.4.2, printed 126--127, which were inspected. W intersects K in A: if x is outside A, its inverse is in the maximal ideal of A and hence that of W, so x cannot belong to W. In an algebraic equation for a nonzero element of L, two least terms have equal value. Therefore a positive integer multiple of each new value is an old value. Dividing in the given real group defines a unique order-preserving real extension; common multiples establish well-definedness and additivity. Integral elements have nonnegative value by the unique-smallest-leading-term argument for a monic equation. Give P infinite value to obtain the required lift to B. Thus restriction is a continuous compact surjection and a quotient map. The same proof applies before fixing a primary section.

If S is the finite normalization of a reduced excellent R and c=(R:S), denominator clearing gives a regular element in c. It is an ideal of S and R and
\[
 R=S\mathbin{\times}_{S/c}(R/c).
\]
Indeed an element of S whose residue comes from R differs from an element of R by an element of c. The boundary of S is the finite disjoint union of its local normal-centre sections above m. Primitive idempotents select minimal components, and localization at a centre changes no value of its denominators. The centre pieces are clopen: in the Artinian ring S/aS choose an idempotent separating a chosen local factor and lift it to S. A semivaluation at a centre has value zero on the lift that is a unit there; on the other pieces the lift belongs to the maximal ideal. The open positivity and finite-generation bounds, or these lifts and their complements, separate the pieces. It is the local normalization centres, not just minimal primes, that index these branches.

For v(c)<infinity choose c0 in c of finite value. Every normalization lift satisfies \(w(s)=v(c_0s)-v(c_0)\), hence is unique. The subtraction uses a finite second term. If v(c)=infinity, all lifts kill c; their identification is exactly equality of restrictions through S/c to R/c. The infinity stratum is CLOSED, and its finite complement is OPEN, not necessarily closed. The compact quotient shows that a finite continuous function upstairs descends continuously if and only if it is fibre constant. For upper semicontinuous fibre-constant u, descent is upper semicontinuous as well: its superlevel sets are images of compact superlevel sets upstairs. This remains valid for extended nonpositive u. None of these topological assertions asserts positivity of a descended function.

Completion requires no excellence. For F in the m-adic completion choose representatives F_N modulo m^N. Put d=v(m)>0. The estimates \(v(F_M-F_N)\ge Nd\), M>=N, imply either finite stabilization when v(F_N)<Nd, or convergence to infinity. Define the limit as vhat(F). It is independent of representatives and satisfies
\[
 \min(\widehat v(F),Nd)=\min(v(F_N),Nd).
\]
Representatives of sums and products prove the semivaluation axioms, including infinity; a completed unit has a unit representative modulo m. Finite generation preserves v(a)=1. The displayed identities force uniqueness of an extension. For continuity compose values with \(q(t)=t/(1+t)\), q(infinity)=1. The continuous truncation expression approximates q(vhat(F)) uniformly within \(1/(1+N/r)\), since d>=1/r. Thus restriction between the completed and original sections is a homeomorphism on ALL semivaluations.

Every completed primary J contains m^N Rhat. Lift its generators modulo that power through \(R/m^N\simeq\widehat R/m^N\widehat R\). These lifts are in J intersect R and generate J together with the boundary power, proving \(J=(J\cap R)\widehat R\). The same quotient argument proves contraction of a primary extension is the original ideal. Corresponding unit-or-primary ideal functions, their uniform closures, and their decreasing completions therefore agree exactly. This is not a model-category equivalence.

This note is a mathematical proof using the explicitly stated ordinary algebraic background. Its source application is limited to the complete valuation-domination units and the stated standard consequences of excellence; it asserts no independent reading of their historical foundations. Artifact n1.md contains this full note. The fresh paper and argument incorporate it; rerun python build_delivery.py after the input audit. No hash or build proves mathematics.

## n2: Exact algebraic source applications

Earlier local supports: n1.

Exact algebraic source applications and their domains.

This note fixes the published algebraic inputs used in subsequent new arguments. It is a source-applied mathematical note, not an independent proof of the historical Izumi, Rees, or dimension theorems. The bound Swanson--Huneke author PDF is the CURRENT file created July 2024, not a claim of byte identity with the 2006 printing. Literal newline ranges and PDF inspections are recorded in source-application-ledger.md and source-excerpts. Earlier local support is n1 for the section and reduction conventions.

Swanson--Huneke Theorem 6.8.3 and Proposition 6.8.4, printed 139--140, give the following exact application. Let E be Noetherian semilocal, J contain a primary boundary power, and Q be a finite ideal. Assume \(w(Q)\ge w(J)\) at all normalized centred semivaluations AND that Q has zero image on every zero-dimensional minimal component on which J is nonunit. Then \(Q\subset\overline J\). Apply the criterion to every minimal component and every centred rank-one DVR of each positive-dimensional local factor. Normalize the DVR by the boundary power. On a zero-dimensional minimal component the boundary is zero. In all applications below Q contains a positive boundary factor, so its image there is zero and is integral over every image ideal. Unit J-components are automatic. The extra zero-dimensional condition cannot be omitted merely because the corresponding boundary is empty. For a nonreduced E, componentwise integral equations can be lifted and multiplied over the finitely many minimal primes; the resulting error is nilpotent. Raising to a power gives an actual monic integral equation whose degree-i coefficients lie in J^i. This verifies explicitly the minimal-component qualification; it is not a replacement by a single generic component. The complete immediate proofs of 6.8.1--6.8.4 and the finite-minimal-prime argument in 1.1.5 were read. PDF pixels on printed 140 confirm the overbars.

If \(Q\subset\overline J\), the finitely generated graded algebra E[(J+Q)t] is integral and finite over E[Jt]. Each q t satisfies the homogeneous monic equation obtained from ideal-integrality of q. Finitely many generators give module finiteness. Choose homogeneous module generators of degrees at most h. For every N>=1, degree N+h then gives
\[
 Q^{N+h}\subset (J+Q)^{N+h}\subset J^N.
\]
Indeed every degree-d generator contributes a coefficient from J^(N+h-d), contained in J^N. This proof works even on nonreduced E; no finiteness of the whole normalized Rees algebra is asserted. The same conclusion follows from the exact reduction criterion in 1.2.4--1.2.5 and Remark 1.2.3, whose complete immediate chain was inspected. Printed 6 was viewed to confirm \(I\subset\overline K\), rather than I subset K.

For an excellent local DOMAIN A and a nonzero primary ideal, the finitely many Rees DVRs exist, are centred at the closed point, and are divisorial with residue transcendence degree dim(A)-1. The applications are Theorem 10.2.2 with its complete proof ending at Proposition 10.2.3, printed 200--202, and Proposition 10.4.3 with its complete proof, printed 209--210. The latter needs formal equidimensionality. Excellence gives universal catenarity; Theorem B.5.1, printed 418--419, gives the equivalence with local formal equidimensionality at the domain hypotheses. Its complete immediate statement/proof was inspected. The same theorem gives, for any finite-type birational DOMAIN B over an excellent domain A and a prime P over m,
\[
 \dim B_P+\operatorname{trdeg}_{A/m}\kappa(P)=\dim A.
\]
The fraction-field transcendence term is zero. The use below is on a particular ratio chart and its Rees divisor, never a singular SNC resolution. Theorem B.3.2 was also read; its proof is referred by the book to a modification of an earlier dimension-inequality argument, and no independent historical proof-reading claim is made.

Stacks Lemma 15.53.6, tag 0C23, has the exact statement: a normal Noetherian local ring with normal formal fibres has normal completion; excellent or quasi-excellent suffices. The entire immediate HTML statement/proof was inspected; the proof refers to Algebra Lemma 10.163.8, not separately supplied or read here. A normal completed local ring is a domain. Thus an excellent normal local A is analytically irreducible and analytically unramified. No such conclusion is asserted for a general nonnormal excellent domain.

Rond--Spivakovsky arXiv 1404.4885v1, pages 1--2, Definitions 1.1--1.2, Theorems 1.3, 1.4, 1.7 and their intervening context were read completely. Theorem 1.3 is the published Izumi--Rees comparison for any analytically irreducible local DOMAIN, not merely a complete domain. Theorem 1.4 represents the asymptotic m-order by finitely many m-Rees valuations. Theorem 1.7 bounds the asymptotic order above by ord_m plus an additive constant in an analytically unramified local ring. For a centred divisorial nu, comparison with each m-Rees nu_j gives constants c_j such that \(\nu(f)\le c_j\nu_j(f)\). Hence with \(C_0=\max_j c_j\nu_j(m)\),
\[
 \nu(f)\le C_0\min_j\frac{\nu_j(f)}{\nu_j(m)}
       =C_0\overline{\operatorname{ord}}_m(f)
       \le C_0(\operatorname{ord}_m(f)+K).
\]
For a nonzero nonunit ord_m(f)>=1, so \(\nu(f)\le C_0(1+K)\operatorname{ord}_m(f)\). For units both sides are zero and are handled separately. Krull intersection ensures finite order for nonzero f in a Noetherian local domain. The literal STRICT inequality in Remark 1.6 would give 0<0 for units; it is not used. Swanson's complete Section 5 context, printed 17--18, was also inspected: its Theorem 5.2 states only the complete-domain version. We use the general theorem as stated in exact Rond--Spivakovsky v1, not an extension of 5.2. Original Rees 1989, Izumi's surface proofs, and all cited historical editions have NOT been independently read.

These precise ordinary published applications establish the inputs at the listed domains, subject to ordinary reliance on the named published theorems and their disclosed historical dependencies. They supply neither singular BFJ retractions nor positive-characteristic resolution. Subsequent notes prove their new consequences rather than treating ROOT317/319/320 labels as supports. Artifact n2.md and the source ledger retain all application bounds and limitations. Rerun python audit_inputs.py for extraction and identities; this command is not mathematical verification.

## n3: Corrected lattice and normal-target norm trace

Earlier local supports: n1.

Continuous ideal cones, a corrected density lattice, and normal-target descent.

Use n1's sections. Define P(A) as the raw finite nonnegative REAL sums of positive gauges v(I), for ideals containing a boundary power (unit allowed). Put Q(A)=-P(A), C(A)=the uniform closure of Q(A), and D(A)=infima of nonempty decreasing C(A)-nets, including zero and bottom. For a local ring, a nonunit ideal containing a boundary power is proper primary. On a finite semilocal algebra use the finite product over its closed centres and permit unit ideals on selected centres. This agrees with the semilocal ideal definition: finite tuples glue in the Artinian quotient by a common boundary power; synchronize rational denominators by ideal powers. Rational profiles -v(I)/k are dense in C, because finite real coefficients can be approximated rationally and common denominators turn finite sums into a product ideal. C is a closed convex cone of finite continuous nonpositive functions, stable under finite maxima by the ideal-sum identity. D-functions are upper semicontinuous. Positive scaling, addition and finite maxima preserve D by product directed sets; zero scaling is defined as zero. No closure under increasing limits or arbitrary infima is presumed.

The rational difference span of the bounded gauges is a lattice. After a common positive integer denominator, each element is (v(I)-v(J))/d; products and powers keep boundary powers in all ideals. The identity
\[
 \min(v(I)-v(J),v(K)-v(H))=v(IH+KJ)-v(JH)
\]
proves the assertion. It contains rational constants (the boundary gauge is 1) and separates points, since \(v((f)+a^N)=\min(v(f),N)\) distinguishes any differing coordinate for sufficiently large N. Its UNIFORM CLOSURE, rather than the arbitrary finite real span, is a real vector lattice. A compact lattice argument proves density in all real continuous functions: use real affine combinations of a separating gauge to match a target at any two points; approximate the two coefficients rationally; continuity then gives local strict error bounds. Finite minima over neighbourhoods of the second point give a function controlling the whole space with the desired value at the first. Finite maxima over neighbourhoods of the first point give a uniform approximation. All these operations belong to the closed lattice. This also gives the corrected Stone--Weierstrass argument without assigning finite integer ideal expressions to arbitrary irrational coefficients.

Let A be excellent normal local DOMAIN, A subset B a finite DOMAIN extension, K subset L its fraction fields, n=[L:K]. For a B-ideal J choose finite A-module generators b_l. Define the norm-coefficient ideal N(J) from the coefficients of
\[
 N_{L(T)/K(T)}\left(\sum_l T_l b_l\right).
\]
Let Sigma be the K-embeddings of L in an algebraic closure and q=n/|Sigma|. In a finite field M containing all their images the norm polynomial is \(\prod_{\sigma}(\sum_l T_l\sigma(b_l))^q\): over an algebraic closure L tensor Omega is a product of Artinian factors, each of length q, and multiplication has determinant the residue scalar to that length. Every coefficient is integral over A and in K, hence in A by normality. Substituting A-linear forms for generators in both directions proves independence of the coefficient ideal.

Normalize A's boundary by a. Let E be the finite integral closure of A in M and extend a base semivaluation to E by n1, INCLUDING its nonzero support. Never extend that semivaluation to the old fraction field before killing its support. The coefficient-minimum Gauss value of a polynomial is multiplicative: quotient by the support, enter the valued fraction field, divide by a least-valued nonzero coefficient, and reduce the resulting polynomial over the residue field. Nonzero polynomials have nonzero product. If a factor is zero modulo support its coefficient value is infinity, and the same assertion holds. Thus
\[
 v(N(J))=q\sum_{\sigma\in\Sigma}w_\sigma(J).
\]
For J containing a boundary power all the summands are finite. Adding base elements x in a^N as redundant generators puts x^n in N(J), so N(J) contains a boundary power and has finite continuous gauge.

The finite positive measure \(\mu_v=q\sum_\sigma\delta_{w_\sigma}\) has mass n. The norm identity determines its integrals on all bounded ideal gauges, and the corrected density argument and common mass determine it on every continuous function, independently of the extension choices. Its support is exactly the restriction fibre. To see the reverse inclusion, extend any given fibre valuation on B to E with the identity embedding of B; E is also integral and finite over B. The identity summand gives the desired point positive mass. Choice independence then proves the assertion for every point, so the fibre is finite, of cardinality at most n. All weights are generic inseparable multiplicities, not a defectless e f formula for arbitrary valuations.

The operator \(T H(v)=\int H\,d\mu_v\) is positive of norm n and continuous-valued: the norm identity proves continuity on gauges; uniform density and the mass bound give it for all H. It sends -v(J)/k to -v(N(J))/k, hence preserves C. On a decreasing C-net its finite positive sum commutes with the extended nonpositive limit, so it also defines descent of fibre-constant D-functions. There is no cancellation of opposite infinities.

For a reduced finite injection into normal local A, retain the source minimal components that dominate A and normalize them. At least one exists by lying over zero. Each resulting normal finite domain has a generic degree n_j and the foregoing trace. A fibre-constant C-function, pulled back to these normalizations, descends by the normalized sum \(\sum T_j/\sum n_j\), giving its actual value at EVERY base semivaluation. Vertical source components are not assigned generic degrees; fibre constancy on the whole source ensures the traced values are nevertheless the correct target value. For a decreasing representing net the same argument gives D-descent. Thus normal targets have exact C- and D-image equal to the fibre-constant subclass, regardless of vertical components.

This is an independently proved norm-coefficient construction, not an imported chapter70 trace theorem. The complete immediate norm/trace units in the supplied chapter70 fragment were read as data; the lattice wording there has been repaired here. Earlier supports are n1 only; ordinary field-norm and finite integral-extension algebra is explicitly proved above. The classes and trace have the exact gauge cocycle because every extension has the same base gauge denominator. Artifact n3.md contains this proof; rerun python build_delivery.py to incorporate it. It makes no assertion of a geometric trace on arbitrary nonnormal targets.

## n4: Bounded finite-injection conductor descent

Earlier local supports: n1, n2, n3.

Bounded uniform descent for every finite reduced injection.

The theorem is \(f^*C_a(R)=\{u\in C_{aB}(B):u\text{ is fibre constant}\}\) for every finite injective map from excellent reduced local R to reduced nonzero B. Pullback is an isometry. Earlier supports are n1, n2, n3. This is a theorem about the continuous uniform cone, not its raw finite cone and not its decreasing completion.

Induct on target dimension. Dimension zero has empty sections on both sides and is vacuous. Normal local targets were proved in n3. In dimension d first prove the normalization assertion using the full finite-injection theorem in dimensions below d. Then deduce arbitrary finite injections by normal-base change.

Let S be the finite normalization of R, c its conductor, C0=R/c, E=S/c. A regular conductor element and the finite dimension of R give dim(C0)<d. The injection C0 into E stays injective after reduction: nilpotence in an injected subring is detected upstairs. Reduction preserves all classes by n1. Let u in C(S) be fibre constant, with continuous descent h on V(R). Restriction of every primary profile and uniform approximation shows that its restriction to the closed infinity-conductor stratum belongs to C(E). By induction it descends to h0 in C(C0). If the latter section is empty there is no quotient estimate below; every base point then has finite conductor value.

Fix eps>0. Approximate u within eps by a rational semilocal profile j=-w(J)/k, and h0 within eps by kappa=-v(K)/k; synchronize denominators by ideal powers. Both ideals contain boundary powers. Increase the common denominator so 1/k<eps. If needed multiply J by aS with arbitrarily large denominator, incurring arbitrarily small additional error, to ensure its contraction is proper; start with tighter errors to absorb this. When u is zero the zero downstairs model suffices. On E,
\[
 |w(K_E)-w(J_E)|<2k\,\mathrm{eps}.
\]
Choose integer L with \(2k\,\mathrm{eps}<L\le2k\,\mathrm{eps}+1\), so L/k<3eps. Put \(Q=K_E(aE)^L\). All normalized boundary semivaluations satisfy w(Q)>=w(J_E). At zero-dimensional minimal components the positive boundary factor kills Q, and unit J_E-components are automatic. The exact application in n2 therefore gives \(Q\subset\overline{J_E}\) without discarding any minimal component or nilpotent quotient. Finite graded integrality supplies h>=0 with \(Q^{N+h}\subset J_E^N\) for every N>=1.

Set \(I_N=J^N\cap R\). It is proper primary: J contains (aS)^M for some M, hence I_N contains a^(MN); properness follows from a proper local-centre component. The conductor fibre product gives the EXACT identity
\[
 (I_N+c)/c=J_E^N\cap C0.
\]
A residue on the right has a representative in J^N whose image comes from C0, so that representative belongs to R. The reverse inclusion is immediate. This is not a general intersection/base-change assertion. Since Q^(N+h) is contained in J_E^N, the C0-ideal \(K^{N+h}(aC0)^{L(N+h)}\) is contained in this image.

At v(c)=infinity the quotient semivaluation thus gives
\[
 \frac{v(I_N)}{kN}\le(1+h/N)\left(\frac{v(K)}k+\frac Lk\right).
\]
All values here are finite. At finite conductor value, the unique lift w and \(cJ^N\subset I_N\) instead give
\[
 \frac{w(J)}k\le\frac{v(I_N)}{kN}\le\frac{w(J)}k+\frac{v(c)}{kN}.
\]
This second estimate is used ONLY on the finite-conductor locus. On every point, I_N subset J^N gives the lower bound \(v(I_N)/(kN)\ge-u(w)-\mathrm{eps}=-h(v)-\mathrm{eps}\). Consequently the dyadic functions \(b_n=v(I_{2^n})/(k2^n)\) have pointwise infimum between -h-eps and -h+4eps. They decrease because I_N^2 subset I_(2N), and are finite continuous bounded functions. The increasing open sets \(\{v:b_n(v)+h(v)<5\,\mathrm{eps}\}\) cover the compact base section. A finite subcover supplies one n satisfying the inequality globally. The lower bound then proves uniform error at most 5eps for -b_n versus h. Letting eps go to zero proves h in C(R). The dyadic approximation was used internally; its negative increases and is not a decreasing regularization.

For a general finite reduced injection R into B, set \(B'=(B\otimes_R S)_{\rm red}\). The base-changed spectrum surjects onto Spec S; its kernel in reduced S lies in all primes and is zero. On each normal local centre of S, the pulled-back u is fibre constant over S: equality of S-restrictions implies equality of R-restrictions of the underlying B-points. N3 descends it to C(S). It is precisely h pulled back to S, hence fibre constant for normalization. The normalization assertion just proved descends it to C(R). This closes the dimension induction. Pullback inclusion follows from extension of ideals, and surjectivity of boundary restriction gives the isometry.

Let Q_R be the negative raw finite real downstairs cone and N_R the continuous descended functions whose normalization pullbacks lie in the analogous RAW cones at every local normal centre. The theorem gives
\[
 Q_R\subset N_R\subset C_R,\qquad
 \overline{Q_R}^{\|\cdot\|_\infty}=\overline{N_R}^{\|\cdot\|_\infty}=C_R.
\]
No equality of the raw cones is asserted; n9 will prove a strict example. Fibres on the infinite-conductor locus are the full quotient-restriction fibres of n1, including nonminimal supports.

The argument reconstructs the proposal labelled ROOT317, with the corrected density lattice of n3 and the explicit zero-dimensional premise of n2. ROOT317 is not a registered support. Artifact n4.md contains the full proof; python build_delivery.py reproduces its inclusion in the paper. It does not prove the general contraction asymptotic formula for arbitrary incompatible J; n10 records a counterexample to that tempting formula.

## n5: Strict-negative unbounded descent

Earlier local supports: n1, n2, n3, n4.

Strictly negative unbounded descent by continuous majorant insertion.

For every excellent reduced finite injection R into B, a fibre-constant u in D(B) descends into D(R) if it is everywhere strictly negative. Minus-infinity values, discontinuity and absence of a lower bound are allowed. Zero descends separately. Earlier supports are n1, n2, n3, n4; n4 supplies the already proved conductor residue identity and base-change algebra. Its bounded theorem is not used to flatten unbounded completed nets.

Descent h is upper semicontinuous by n1. Compactness implies h<=-c0 for some c0>0 unless the section is empty; all-bottom is handled directly by -N times the boundary gauge. Normal targets follow by n3's finite trace, which commutes with decreasing nonpositive extended limits. Induct on target dimension exactly as in n4: first normalization from the lower-dimensional finite-injection assertion, then arbitrary injection by reduced normalization base change and normal-target trace. Thus it suffices to prove the normalization step and a continuous insertion lemma.

Let S,c,C0,E be as in n4. Restrict a decreasing C(S)-net to E; its fibre-constant limit descends by dimension induction to h0 in D(C0). It is strictly negative on the quotient section. Suppose F is any finite continuous function on V(R) with F>h pointwise. The extended lower semicontinuous gap F-h has a positive finite lower bound e>0 on the compact space (choose any sufficiently small finite bound when the minimum is infinity). We claim that there is q in C(R) with h<q<F everywhere.

Choose a continuous C(S)-majorant g from the decreasing representing net with \(u\le g<-c0/2\) and \(g<F\circ f-e/2\). Each strict-test open set eventually contains each point; compactness and directedness give one index for both tests. This is not uniform convergence to u. Choose b in (0,1/2) with b||g||<e/8. Then (1-b)g stays below F-e/4 and is above u+b c0/2 at finite-u points. Approximate uniformly by a rational profile \(j=-w(J)/k\), with error less than min(e/8,b c0/4), and if necessary further tighten it to ensure j<0 uniformly. Obtain a fixed s>0 such that
\[
 u+s\le j<F\circ f-e/8,
\]
where the first inequality is automatic at bottom points. J is proper at every positive-dimensional centre and contains a boundary power. Put M=||j||.

For arbitrarily small delta>0 choose a rational profile \(\kappa=-v(K)/k\) on C0 with h0<=kappa and \(\kappa\circ f_E<j|_E+\delta\). To justify this without uniform convergence, start with a decreasing continuous C(C0)-net g_i to h0 and a number b1 in (0,1/2) with b1 M<s/4. Since u|E<=j|E-s,
\[
 (1-b1)u|E\le(1-b1)(j|E-s)<j|E-s/4.
\]
Compactness on E selects an index with (1-b1)g_i pulled back below j|E-s/8; select simultaneously g_i<-c0/2 on C0. The latter test makes (1-b1)g_i exceed h0 by b1 c0/2. Uniform rational approximation with error less than min(b1 c0/4,s/16) yields kappa with the claimed properties. Synchronize the denominators for J,K by powers, then enlarge k so 1/k<delta. If the quotient section is empty none of this quotient construction is needed.

Choose integer L with k delta<L<=k delta+1. Thus L/k<2delta. For \(Q=K_E(aE)^L\), the inequalities on E imply w(Q)>=w(J_E). The positive boundary factor handles every zero-dimensional minimal component, and n2 gives \(Q\subset\overline{J_E}\), then \(Q^{N+h'}\subset J_E^N\) for a fixed exponent h'. Contract \(I_N=J^N\cap R\); the exact conductor residue identity of n4 follows directly again. It gives at infinity-conductor points
\[
 \liminf_N\left[-\frac{v(I_N)}{kN}\right]\ge\kappa(v)-2\delta\ge h(v)-2\delta.
\]
At finite-conductor points the conductor-product estimate gives the limit j(w)>=h(v)+s. No infinity is divided by N. For dyadic N put \(f_n=-v(I_{2^n})/(k2^n)\). These finite continuous profiles INCREASE, have f_n<=j on every lift, and their limit is >=h-2delta everywhere. The sets \(\{v:f_n(v)>h(v)-3\delta\}\) are open because h is upper semicontinuous; they increase and cover the compact space, also at bottom points. Select one n valid everywhere.

Take delta so small that eta=3delta/c0<1/2 and eta M<e/16. Set q=(1-eta)f_n, a real-scaled profile in C(R). At finite h<=-c0,
\[
 q>(1-\eta)(h-3\delta)
   \ge h+\eta c0-3\delta(1-\eta)=h+3\delta\eta>h.
\]
At bottom points q is finite. Since f_n<=j and j>=-M, q<j+e/16<F. This proves insertion. Real positive scaling is justified by uniform rational approximation; q need not have a rational coefficient.

Let Q be all continuous C(R)-functions strictly above h. It contains zero. Given q1,q2 in Q, use the continuous TEST F=min(q1,q2) in insertion to obtain a member below both. There is no assertion that this minimum is psh. Hence Q is downward directed. At any point v and real t>h(v), choose a finite continuous F>h with F(v)<t: pick a finite level ell between h(v) and t, an open neighbourhood on which h<ell, and a Urysohn cutoff supported there; interpolate between ell near v and a global bound strictly above h elsewhere. Shrink the neighbourhood before making the cutoff so strictness persists on its support. Insertion gives q(v)<t. Thus inf(Q)=h, and ordering Q by reverse pointwise order gives an ACTUAL decreasing C(R)-net to h. This completes the normalization step, the normal-base-change induction, and the theorem.

All-bottom and empty sections were separated, and the proof includes partial-bottom and nonminimal supports. The result reconstructs the entire strict-negative proposal labelled ROOT319 without treating that label as a support. It uses compact open-cover insertion instead of a Dini assertion for a discontinuous limit. Artifact n5.md contains the proof, incorporated by python build_delivery.py. Mixed-zero descent remains a separate issue addressed by n6.

## n6: Full mixed-zero completed conductor descent

Earlier local supports: n1, n2, n3, n4, n5.

Divisorial density, the normal-branch zero dichotomy, and FULL completed descent.

The theorem is
\[
 f^*D_a(R)=\{u\in D_{aB}(B):u\text{ is constant on every restriction fibre}\}
\]
for every excellent reduced local R and nonzero reduced finite injection into B. Every primary gauge, nonminimal support, infinite-conductor fibre, zero pattern and minus-infinity value is included. This is the ideal-uniform decreasing class of n3. Earlier supports are n1, n2, n3, n4, n5. Transfer to a geometric class is conditional on the separate comparison in n8; this theorem alone does not solve original P12.2.

First prove direct divisorial density on an excellent local DOMAIN A of positive dimension. Let v in V(a,A) and choose finitely many strict coordinate tests defining a neighbourhood. Select a generator a0 of a with v(a0)=1 and include all ratios a_j/a0 in a finite-type birational subalgebra B0 of Frac(A). For a finite positive coordinate f, choose rational bounds p/q<v(f)<r/s strictly inside its required interval, with p>=0 and q,s>0. For an infinity coordinate keep only a rational lower bound. Include
\[
 f^q/a0^p\quad\text{for lower tests},\qquad
 a0^r/f^s\quad\text{for finite upper tests}.
\]
Units and zero coordinates are fixed at zero and infinity respectively. Every denominator has finite v-value, so v extends nonnegatively to B0 even when f has infinite value in a lower test. Let P be its positive-value prime. It contains the strict-test ratios and a0; thus the excellent local domain (B0)_P has positive dimension. Take a Rees DVR of its maximal ideal, whose existence and divisorial residue-degree property are the exact n2 applications. Its valuation nu is positive on every element of P and nonnegative on B0. Hence nu(a)=nu(a0)>0. Rescale by this number: positivity of the ratios gives exactly the strict lower and upper tests, so the rescaled nu belongs to the original neighbourhood.

It is divisorial OVER A. The n2 finite-type birational dimension formula gives
\[
 \dim (B0)_P+\operatorname{trdeg}_{A/m}\kappa(P)=\dim A,
\]
and the Rees DVR has residue transcendence degree dim((B0)_P)-1 over kappa(P). Additivity therefore gives residue transcendence degree dim(A)-1 over A/m. Its value group is discrete rank one and its centre on A is m since the primary gauge is positive. This is the exact divisorial definition used by Rond--Spivakovsky. It proves density in the actual pointwise topology, INCLUDING points with nonzero support. It imports neither smooth retractions nor singular resolution in arbitrary characteristic.

Now A is excellent NORMAL local. N2's normal-completion lemma and the general Izumi--Rees derivation supply, for each centred divisorial nu, a finite C_nu with \(\nu(f)\le C_\nu\operatorname{ord}_m(f)\) for every nonzero nonunit; units are zero separately. Normalize nu by a and absorb its denominator into C_nu. If m^r subset a then at any v0 in the section, v0(m)>=1/r and
\[
 v0(f)\ge\operatorname{ord}_m(f)v0(m).
\]
For a proper primary I choose a nonzero f attaining its finite v0-value. The last estimates give \(\nu(I)\le C_\nu r v0(I)\). The unit ideal also satisfies this. Therefore for every raw negative profile, every finite real sum, and by uniform approximation every g in C(A),
\[
 g(\nu)\ge C_\nu r\,g(v0).
\]
If g(v0)=0, nonpositivity forces zero at every divisorial nu. Density and continuity force g=0 everywhere. Thus a nonzero C-function on a normal local branch is strictly negative at EVERY point. For u=inf(g_i) in D, if u(v0)=0 then each nonpositive g_i(v0)=0 and each g_i is zero. The same dichotomy holds for D, including bottom. Compact upper semicontinuity bounds each nonzero D-function above by a negative constant.

Let u in D(S) be normalization-fibre constant. There are finitely many local normal centres of S. Each component function is either identically zero or everywhere strictly negative. Call the latter centres active, including bottom centres. Active and inactive points cannot share a fibre, since their u-values differ in sign. The tuple sigma=-1 on active centres, zero on inactive centres belongs to C(S): realize -1 by the negative extended boundary gauge at the chosen centre, zero by units at the others, and glue using an Artinian boundary quotient. It is fibre constant. Apply the INDEPENDENTLY PROVED bounded theorem n4 to descend sigma into C(R). This positivity step is essential; topological descent alone is insufficient. Its active set \(T=\{v:\sigma(v)=-1\}\) is clopen, h=0 off T, and h<=-c on T for a common c>0. Empty T gives zero directly.

For every delta>0, u-delta belongs to D(S), is fibre constant and everywhere strictly negative. Addition is justified by product directed sets in n3. N5 gives \(h-\delta\in D(R)\). Let F be any finite continuous test on the compact clopen T with F>h. The lower semicontinuous gap has a positive finite lower bound e. Choose eta in (0,1/2) with \(\eta(\|F\|+e)<e/4\), and set \(\delta=\eta c/[2(1-\eta)]\). At finite h on T,
\[
 (1-\eta)(h-\delta)=h+\eta(-h-c/2)>h.
\]
Also h<=F-e gives \((1-\eta)(h-\delta)<F-e/2\); the bound on eta controls the finite F term even when h is unbounded below. At bottom points the latter inequality still holds and any finite majorant will be above h.

Choose a decreasing C(R)-net g_i to h-delta. Its scaled terms dominate the scaled target. The strict open tests \((1-\eta)g_i<F-e/4\) cover T; compactness and directedness choose one i for the whole of T. Choose positive N with -N<min(T,F). Then
\[
 q=\max\{(1-\eta)g_i,N\sigma\}\in C(R)
\]
satisfies h<q<F on T and q=0=h EXACTLY off T. Both terms are below F on T; the first is strictly above finite h and q is finite at bottom points. Off T the second is zero and the first nonpositive. Only positive scaling and maxima in the continuous cone have been used; no positive constant was added to a nef class.

Let Q consist of all C(R)-functions exactly zero off T and strictly above h on T. It contains zero. Given two members, the continuous TEST min(q1,q2) on T permits the preceding insertion and gives another member below both. The minimum itself is not assumed psh. The Urysohn construction in n5 supplies, at each v in T and each finite t>h(v), a continuous F>h with F(v)<t. Thus inf(Q)=h on T and is zero elsewhere. Q ordered by reverse pointwise order is an actual decreasing net of C(R)-functions. This proves full normalization descent. It does NOT take an increasing delta-limit or assert a general flattening theorem for completed nets.

Finally for a finite injection R into B take B'=(B tensor_R S)_red. By n4 it is finite injective over S. A fibre-constant u in D(B) pulls back into D(B') and is fibre constant over S. N3's normal-target trace on every local normal centre descends it into D(S). It is precisely h pulled back to S, so is normalization-fibre constant. The full normalization result descends it into D(R). The reverse inclusion is ideal extension and commutation with uniform and decreasing limits. This proves the theorem for all finite injections.

All-zero, mixed zero with partial bottom, all-bottom, and positive-dimensional conductor-infinite supports are covered. A zero-dimensional local reduction has the singleton empty-function class rather than a nonempty branch link. Local normalization centres, not irreducible components alone, determine the dichotomy. This reconstructs the ROOT320 proposal with independently proved n4 indicator descent and n5 insertion. All original labels are provenance, not support IDs. Artifact n6.md contains the full proof; rerun python build_delivery.py. Published background applications are those of n2, with its explicit historical reading limits. No execution or registration turns this unverified proof into accepted mathematics.

## n7: Full smooth BFJ specialization

Earlier local supports: n1, n3.

FULL smooth BFJ specialization on ALL semivaluations.

At a smooth closed point of an affine variety over an algebraically closed characteristic-zero field, identify the local m-section with BFJ's V by localization and n1's completion homeomorphism. All base-field nonzero constants are units and automatically have zero value. For dimension at least two the source setting and complete immediate units are: Sections 1.2--1.7, Definition 2.1, Proposition 2.2, Definitions 2.5/2.8 and Proposition 2.7, the multiplier units 3.6--3.10, complete Propositions 3.11/3.13/3.14 and proofs, and the complete Section 3.5--3.6 reductions of Theorems 3.9/3.10. They were inspected from the bound published PDF/TXT, with printed 475 additionally viewed for the approximation exponents. This is a precise application of those published BFJ results at their ACTUAL hypotheses. The historical proofs of Hironaka, smooth Izumi, and multiplier-ideal subadditivity are disclosed dependencies, not independently read editions. Earlier supports are n1 and n3 for boundary and C,D definitions.

BFJ formal psh means a finite strongly continuous function on the quasimonomial locus, whose divisorial Weil divisor belongs to the weak closed nef cone of Definition 2.1, extended to ALL V by
\[
 g(v)=\inf_\pi g(r_\pi(v)).
\]
Proposition 3.11 gives the unique continuous CONVEX function on each CLOSED simplex for every nef Weil divisor; its proof uses the bounded thinness A on that simplex and the uniform multiplier error A/k. Continuity at faces is a substantive published theorem, not a consequence of finite convexity in an open simplex. Proposition 3.14 gives \(C_v g(v_m)\le g(v)\le g(v_m)\) on the quasimonomial locus; the upper bound extends to all points by Proposition 2.7 and Definition 2.8. A nonzero formal function has g(v_m)<0.

For proper primary I, its negative ideal divisor is Cartier and relatively generated; Propositions 1.14 and 2.2 identify its canonical function with -v(I). This equality also follows directly at nonminimal supports: after principalization I is an exceptional monomial times a unit, and the valuation and all sufficiently high retractions have the same exceptional linear combination. Proposition 2.7 makes the all-retraction infimum this actual ideal value. Zero is formal separately.

The literal proper-primary wording in Proposition 3.13 has a zero/unit exception. Its PDF formula is
\[
 A_j=\mathcal L^2(2^j g)+\widehat m^{4^j},\quad
 h_j=2^{-j}\log|\mathcal L^2(2^j g)|,\quad
 g_j=-2^{-j}v(A_j)=\max\{h_j,-2^j\}.
\]
Theorems 3.9 and 3.10 give decreasing convergence on quasimonomials. If g=0, Definition 3.6 makes the multiplier ideal the UNIT ideal, so all A_j are unit. A decreasing family of proper-primary negative profiles cannot converge to zero, since its first term is strictly negative at every point. Retain zero separately. If g is nonzero put c=g(v_m)<0. The multiplier estimate gives \(h_j(v_m)\le c+2^{-j}A(v_m)<0\) eventually; thus late multiplier ideals are proper, and A_j are then proper primary. Discard the finite initial unit terms.

At an arbitrary point v and real t>g(v), Definition 2.8 chooses a retraction with g(r_pi(v))<t. For sufficiently late j, g_j(r_pi(v))<t, while \(g(v)\le g_j(v)\le g_j(r_\pi(v))\). Hence the same sequence decreases to g on ALL semivaluations, including minus-infinity values. N1 contracts the completed primary ideals exactly to the original local ring. This is the corrected full approximation statement, rather than a bounded-only result.

Every globally continuous BFJ formal function is in C: the corrected sequence converges uniformly by compactness and the increasing open-cover proof of Dini. Conversely let primary profiles h_l converge uniformly to h, a finite continuous function. Their divisorial coefficients converge to a compatible Weil divisor W with finite coefficients; it is weakly nef by the source's closed-cone definition. Proposition 3.11 supplies H_W. On each closed simplex, h and H_W agree on the dense rational divisorial points and therefore on the whole simplex by continuity. Since each h_l satisfies its all-retraction infimum and uniform errors pass through an infimum,
\[
 h(v)=\inf_\pi h(r_\pi(v))=H_W(v)
\]
on the entire V. This proves C equals the continuous BFJ subcone; no bounded upper semicontinuous function is renamed continuous.

For a decreasing C-net h_i with nonbottom limit g, its order-valuation infimum is finite. Otherwise \(h_i(v)\le h_i(v_m)\) would force bottom everywhere. The published lower bound then makes g finite on EVERY quasimonomial valuation. Its finite divisorial limit W is weakly nef. On any rational closed simplex the limit g is finite and convex, since the convexity inequalities pass to the decreasing limit. For each point take the MINIMAL face containing it; g is continuous on that face's relative interior by the elementary finite-convex theorem. Dense rational divisorial points there agree with H_W, so both functions agree throughout that relative interior. Doing this separately on all lower-dimensional faces covers every boundary point and establishes the correct closed-face extension. Interior convexity alone was not used to assert boundary continuity.

Finally infima commute as infima over a product index set, with extended values:
\[
 g(v)=\inf_i\inf_\pi h_i(r_\pi(v))
     =\inf_\pi\inf_i h_i(r_\pi(v))
     =\inf_\pi g(r_\pi(v)).
\]
It is exactly BFJ Definition 2.8, so g=H_W everywhere. Conversely the corrected Proposition 3.13 gives decreasing continuous approximants to each nonzero BFJ function, and zero has its constant net. Thus D minus its IDENTICALLY minus-infinity bottom equals the full BFJ formal class, and D is that class with bottom adjoined. Bottom is actually the decreasing sequence -N v(m); it is excluded from the ordinary BFJ class because the latter is finite on quasimonomials. This does not assert that all bounded usc functions are continuous or that every singular weak Weil divisor admits such an extension.

At another primary gauge divide by the bounded positive denominator in n1. A smooth one-dimensional germ is a DVR, not an implicit application of the higher-dimensional BFJ exceptional models: V_(z^d) is the singleton ord_z/d; every proper primary ideal has some integer order, so C is all finite nonpositive constants, and D adds minus-infinity. Negative real closed-point Cartier divisors on the identity model have this same evaluation and no contracted curve tests. Dimension zero has empty section. These exceptions fix both the bottom and unit conventions.

The source application does not extend BFJ to singular, nonnormal, positive-characteristic, or arbitrary-residue-field SNC settings. BdFFU Proposition 2.4(b) is not used; n10 checks its sign independently. Artifact n7.md and source-application-ledger.md retain this complete proof and the exact reading limits. Rerun python audit_inputs.py and python build_delivery.py; successful extraction and compilation do not prove the BFJ application or this draft mathematically correct.

## n8: Actual Cartier numerical geometry: conditional comparison

Earlier local supports: n1, n3.

Independent actual-Cartier numerical models and a CONDITIONAL geometric comparison.

Earlier supports are n1 and n3. The independent definition below uses actual algebraic geometry on reduced excellent local germs, not an ideal gauge as a positivity definition. This note proves the comparison IMPLICATION under precise relative-geometry premises. Their complete immediate primary proof units are absent from the supplied packet, so they are explicitly retained as the unresolved source/proof gate. Calling these familiar theorems does not supply the missing immediate-unit check required by this assignment. In particular this note does not register an unconditional complete original solution.

Admissible models are actual \(Y_I=\operatorname{Bl}_I\operatorname{Spec}R\) for proper primary I. Their Rees algebras are subalgebras of the reduced ring R[t], so the models are reduced, projective and isomorphisms off the closed point. On a chart with a regular tautological generator, \(I\mathcal O_Y=\mathcal O_Y(-E_I)\), where E_I is an ACTUAL effective integral Cartier divisor and -E_I is relatively ample. Charts may use a zero-divisor generator in R, but the chart lies in R[1/f], where that generator is regular; generic components on which f is zero are absent from that chart. All generic components are retained by the whole primary blowup.

An exceptional Cartier divisor includes its trivialization away from the closed fibre. A real exceptional divisor is a finite real combination of integral exceptional divisors. The effective real cone is the cone generated by ACTUAL effective integral Cartier divisors, with these trivializations. Thus -D effective means an actual finite effective presentation, not nonnegative Weil coefficients on a nonnormal model. Require also \(\deg_C\mathcal O(D)\ge0\) for every contracted proper integral curve, extended linearly for real D. Denote its nonpositive evaluation functions by M_geom, including zero. Its uniform closure is C_geom; its decreasing completion is D_geom.

Directedness is proved over the reduced ring. Y_(IJ) makes the product of the pulled-back ideals invertible. Locally write it as the regular principal ideal (f), and set J'=f^(-1)J in the total quotient ring of the local model. Then IJ'=A and 1=sum x_l y_l with x_l in I, y_l in J'. Each multiplication by y_l maps I into A, and the displayed expression is a dual basis. I is finite projective and has rank one at every generic point, hence locally rank one; likewise J. The universal property gives maps to Y_I,Y_J. Each primary ideal contains a regular element by avoidance of finitely many minimal primes, so the maps preserve all generic components and Cartier pullbacks. Pullback preserves actual effectivity. The degree on a contracted curve is zero if its image is a point, or a positive degree times the downstairs curve degree, so it preserves numerical nefness as well.

For an integral exceptional F on Y_I there is an integer N with \(-NE_I\le F\le NE_I\) in ACTUAL Cartier order. Inside the total quotient sheaf, the coherent sheaves O(F)+O and O(-F)+O have quotients by O supported on the closed fibre. A boundary power annihilates both on a finite affine cover. The inclusions \(O(F)\subset O(NE_I)\) and \(O(-F)\subset O(NE_I)\) give the stated bounds. Thus E_I is an order unit in every fixed finite real span.

At a semivaluation with support p, quotient by p and use its valuation ring in Frac(R/p). Its generic map is in the punctured model and extends uniquely to Y_I. This can be seen directly on a chart with a minimizing primary generator, as in n1, rather than by subtracting infinite values. Pull back the line bundle O(F) with its generic trivialization; a local generator has a nonzero finite value in the valued field. Define f_F as its NEGATIVE value. For effective E this equals the positive value of a generator of O(-E). Additivity, real linear extension, degree-one homogeneity and model-pullback invariance follow from tensor products and local units. The order bounds give \(|f_F|\le N v(I)\). They do not yet give continuity; that is proved conditionally below by an exact primary-ideal expression.

The exact unresolved background schema is the following, applied only to projective primary blowups over a Noetherian affine local base. G1: proper direct image of coherent sheaves is coherent. G2: high divisible powers of a relatively ample rational line bundle are relatively generated by global sections; sufficiently ample twists of any fixed line bundle are ample. G3: curve-degree nef plus a positive ample real perturbation is ample, and ampleness is open in every fixed finite-dimensional real Cartier span. In G3 the fibre is the PROJECTIVE closed fibre over the residue field; it may be nonreduced, and one must also justify ampleness invariance under nilpotent thickening, then fibre-ampleness implying relative ampleness near the closed point. A neighbourhood of that point in a local spectrum is the whole spectrum. These are familiar correct-looking relative-geometry statements, but no full primary statement/proof unit for these general nonnormal, arbitrary-characteristic applications was supplied or independently inspected here. BFJ Proposition 2.2 is at smooth characteristic-zero hypotheses and cannot discharge G3 in this domain. We retain G1--G3 as explicit premises of the implication, rather than extending BFJ.

Assuming G1--G3, set \(T=H^0(Y_I,O_Y)\). It is a finite R-algebra, embeds in the total quotient ring, contains R, and agrees with R off m. Therefore T/R is killed by m^h for some h. Set \(c_0=m^{h+1}\); then \(c_0T\subset m\) as ACTUAL elements of R. This fixed primary correction concerns the algebra of this primary model, not the full normalization, whose conductor may be nonprimary.

Let L be rational exceptional, actually negative, with O(L) relatively ample. For sufficiently large divisible k, G2 generates O(kL) by \(F_k=H^0(Y_I,O(kL))\subset T\). Define \(J_k=c_0F_k\subset R\). It is a finite R-ideal, proper because c0 T subset m, and unit off m, hence contains a boundary power and is primary. Its extension is \((c_0O_Y)O(kL)\). At a valuation-ring centre one generating coefficient of the line bundle is a unit, so on EVERY semivaluation
\[
 -v(J_k)/k=f_L-v(c_0)/k.
\]
This does not assert that F_k is an R-ideal, or that its corrected pullback equals O(kL) without the factor c0. For arbitrary integral F choose N with L=F-NE_I negative and ample. The identity gives
\[
 f_F=-v(J_k)/k+N v(I)+v(c_0)/k.
\]
All values are finite continuous primary gauges, establishing continuity, including nonminimal supports.

Let D be actually negative real and numerically nef. Under G3, D-delta E_I is ample for small delta>0. Write \(D=-\sum_j d_j A_j\), with d_j>=0 and actual effective integral Cartier A_j. Round these coefficients UP to nearby rationals and perturb delta slightly rationally, retaining ampleness by openness. The result D' is actually negative rational, \(D'\le D-(\delta/2)E_I\), and has arbitrarily small uniform evaluation error. Divisible integral multiples of D' are genuinely negative integral Cartier divisors on the nonnormal model. Apply the corrected section construction and let k grow:
\[
 -v(J_k)/k\le f_D,\qquad \|f_D+v(J_k)/k\|_\infty\longrightarrow0.
\]
The fixed c0-error is uniformly small because c0 is primary. Conversely a raw negative ideal profile is the evaluation of -t E_J on its actual primary blowup, which is relatively generated and nef. Common models and sums handle finite real combinations. Hence the PROVED CONDITIONAL implication is
\[
 \text{G1--G3}\quad\Longrightarrow\quad C_{\rm geom}=C,\quad D_{\rm geom}=D.
\]
It is uniform approximation from BELOW, not decreasing primary regularization. The actual Cartier effective presentation is essential to the rational approximation; coefficientwise Weil effectivity would not prove it on a nonnormal model.

The independent model definition and its evaluation are homogeneous; the exact n1 gauge cocycle therefore applies, with bounded denominators preserving uniform closure and decreasing nets. A normalization branch's extended-primary blowup maps to the downstairs primary blowup, preserving the stated effectivity, numerical positivity and evaluation. If G1--G3 are discharged, n4 and n6 give the complete reverse C,D conductor rules, n7 gives full smooth BFJ specialization, and n9 gives the correct strict raw-cone relationship. No radial analytic/CLD cone is identified: a multibranch mixed-zero boundary function may belong to C,D even though the closed-disc logarithmic radial extension theorem excludes it. No envelopes, products, energy, or nonnormal geometric trace are supplied.

This independently reconstructs the complete used numerical model units of native234 and the ROOT311/312 comparison proposals, with their domains and effectivity qualifications. ROOT314's completion and smooth gates are separately proved in n1/n7. The conditional implication is substantial exact-scope progress, but it is not whole-original closure. Artifact n8.md gives the full argument; the gate is listed verbatim in source-application-ledger.md and whole-proof-coverage.md. Rerun python build_delivery.py. Successful compilation cannot discharge G1--G3.

## n9: Cusp strict raw-cone separation

Earlier local supports: n1, n3, n4.

An explicit nonisolated cusp: strict raw-cone separation and uniform approximation on every semivaluation.

Earlier supports are n1, n3, n4. Work in characteristic zero with
\[
 R=k[t^2,t^3,z]_{(t^2,t^3,z)}\subset S=k[t,z]_{(t,z)},\quad m=(t^2,t^3,z).
\]
The normalization is S: t is integral, the field is unchanged, S is finite with generators 1,t and is normal. The conductor is c=t^2S. Before localization R consists of polynomials in t,z with no t-linear coefficient; modulo t^2S it is k[z]. Multiplication by t tests that an R-element is in the conductor exactly when its t-constant coefficient vanishes, proving the formula also after localization. The conductor support is the positive-dimensional z-axis. The quotients are k[z]_(z) and k[z,t]_(z,t)/(t^2); semivaluations kill the nilpotent t and the quotient boundaries coincide. Thus normalization restriction is a HOMEOMORPHISM on all boundary points by n1, even on the conductor-infinite stratum.

Write s=w(t), u=w(z) on the m-section, so s,u>0, either may be infinite, and min(2s,u)=1. The conductor stratum is s=infinity,u=1. The monomial points s=N,u=1 converge to it on every localized polynomial, so the finite-conductor complement is not closed and 2s/k is not uniformly a vanishing error.

Put b=z+t and \(A(w)=w((b,t^2))=\min(w(b),2s)\). This is a continuous finite positive normalization-ideal gauge. Its negative belongs to the RAW normalization cone N_R since fibres are singletons. For each integer k>=1 define actual downstairs primary ideals
\[
 K_k=(b^k(z-kt),\ t^2b^k,\ t^{2k+2})\subset R.
\]
The t-linear coefficient in the first generator is kz^k-kz^k=0, so it belongs to R. All other generators belong to the conductor. Their common zero in S forces t=0 and then z=0, proving primaryness by integral lying over. They are proper. Each generator has value >=kA. We prove the ALL-semivaluation bound \(kA\le w(K_k)\le kA+2\).

If A=2s<=w(b), then s is finite and w(b)>s. Distinct-value ultrametric equality forces u=s; normalization gives s=u=1. The generator t^(2k+2) has value kA+2. Otherwise A=w(b). If s<=u then min(2s,u)=1 gives s<=1, and t^2b^k has value kA+2s<=kA+2. If s>u, then u=1, w(b)=u and w(z-kt)=u because k is a nonzero unit and the two terms have distinct values. The first generator gives kA+1; this includes s=infinity. The u=infinity endpoint falls in s<=u. Cancellation when s=u and nonminimal supports are covered by these cases; no infinite value is treated as finite. Hence
\[
 \|k^{-1}v(K_k)\circ\rho-A\|_\infty\le2/k.
\]
It follows directly that -A descends into C_R. The sequence approximates from below; it is not claimed decreasing. This conclusion needs no conditional geometry from n8.

Separation is from the ENTIRE finite REAL raw cone, not only from individual ideal gauges. Let w_infty be the axis valuation and w_star monomial in coordinates (t,b) with weights 1,2. Then w_star(z)=1, so it is m-normalized, and A(w_infty)=1,A(w_star)=2. For any proper primary I downstairs set d=w_infty(I), a finite positive integer, and choose f in I whose restriction to t=0 has z-order d. Its formal expansion in (t,z) has zero t-linear coefficient even after localization: both numerator and unit denominator have zero derivative at t=0, so their quotient does also. The total-degree-d homogeneous part P_d has a nonzero z^d coefficient and zero t z^(d-1) coefficient. After substituting z=b-t it cannot be a scalar multiple of b^d, since such a multiple has t z^(d-1) coefficient d times its nonzero z^d coefficient in characteristic zero. Some nonzero term t^(d-j)b^j has j<d, of w_star-value d+j<=2d-1. Other total degrees cannot cancel this particular monomial. Consequently
\[
 w_{\rm star}(I)<2w_{\rm infty}(I).
\]
Unit ideals have both values zero. Every nonzero finite nonnegative real combination of unit-or-primary gauges has the same STRICT inequality. A has equality and is nonzero, so A lies outside the entire positive downstairs cone, or -A outside Q_R. Thus \(Q_R\subsetneq N_R\subset C_R\) in this example, while both raw cones have the same uniform closure by n4. No equality of C with the raw normalization cone is asserted.

The own exact program exact_checks.py was fully inspected before execution. It retained 32 coefficient checks and 2,976 rational case samples with no failures. The samples use seven positive rational preweights, normalize by min(2s,u), include seven compatible cancellation possibilities when s=u and two support endpoints, for k=1,...,32. The report's maximal error is 2/k for each tested k. This is an exhaustive result for that FINITE grid, not for all semivaluations. The foregoing symbolic case proof is the all-semivaluation argument. Artifacts are n9.md, exact_checks.py and reports/exact-checks.json; rerun python exact_checks.py and python build_delivery.py. No supplied checker was executed.

## n10: Failed contraction shortcut and source sign diagnostics

Earlier local supports: n1, n2, n3.

Diagnostics: an invalid contraction formula and the BdFFU sign/domain caution.

Earlier local supports are n1, n2, n3 for section conventions and the already stated source qualifications. The first tempting shortcut is false even for a finite reduced diagonal injection. Let R=k[[x,y]], B=R times R, and \(J=((x,y^2),(x^2,y))\). At v(x)=v(y)=1, both component ideal values are 1. But \(J^N\cap R\) is the intersection of the two monomial powers. Its exponent conditions are
\[
 2a+b\ge2N,\qquad a+2b\ge2N.
\]
Adding gives a+b>=4N/3. For N divisible by 3, a=b=2N/3 gives membership and total order 4N/3. Thus the asymptotic contracted order is 4/3, not the maximum component order 1. In fact the minimum for every N is ceil(4N/3): choose balanced nonnegative integers with that total, whose smaller coordinate is at least 2N minus that total. The own finite diagnostic enumerated all a,b from 0 to 2N for N=1,...,24 and confirmed this minimum, retaining witnesses in reports/exact-checks.json. The symbolic argument proves the asymptotic statement. This is a failed approach, not evidence against the fibre-compatible target theorem in n4. Earlier support is n3 for the distinction between raw gauges and uniform functions.

The bound BdFFU paper is on normal complex algebraic varieties with good resolutions of normalizing subschemes, and its Val_X uses valuations of the function field, rather than all semivaluations with prime support in n1's section. Its complete immediate Proposition 2.4 statement/proof and Definitions 2.1--2.2 context were read. The printed assertion 2.4(b) says r_pi(v)(a)>=v(a), but the local expansion argument in its proof says the reverse. The reverse is the correct positive-gauge sign: cancellation may increase an actual valuation above its monomial retraction.

For an explicit test, start on k[[x,y]] with the divisorial monomial valuation in coordinates x,b=x+y having values 1,2. On the first blowup of m its centre is the point where 1+y/x vanishes, so its retraction to the first exceptional divisor is the order valuation. For the proper primary ideal I=(x+y,x^3), its actual value is min(2,3)=2 while the order-retraction value is min(1,3)=1. Both have v(m)=1. Hence \(r(v)(I)=1<2=v(I)\). The sign in the negative psh convention is correspondingly -v(I)<=-r(v)(I), agreeing with BFJ Proposition 2.7. The source proof also has a sentence calling a minimum of affine functions convex after correctly deriving concavity; no such literal sentence is used. This diagnostic does not refute the corrected useful source statement.

No BdFFU retraction, singular SNC resolution, multiplier theorem or domain extension is used in the proofs. Its exact unit was inspected to preserve the mandatory sign/domain warning, not as a correctness grant. The general Izumi--Rees source's strict Remark 1.6 similarly cannot include units: its 0<0 unit test is handled by n2's non-strict derivation. This note supplies source diagnostics only and is not a whole-original refutation. Artifact n10.md contains the mathematical arguments; rerun python exact_checks.py for the finite lattice observations. No script can prove the published source application correct.

## n11: Whole-original OPEN decision

Earlier local supports: n1, n2, n3, n4, n5, n6, n7, n8, n9, n10.

Whole-original decision: OPEN, with full ideal-conductor reconstruction and a precise geometric gate.

Earlier local supports are n1, n2, n3, n4, n5, n6, n7, n8, n9, n10. The exact original-task.json, including the entire family dossier, controls this decision. P12.2 asks for an independently geometric singular/nonnormal excellent-germ valuative psh cone, a PROVED comparison to the exact ideal conventions, correct full smooth specialization, primary-gauge changes, and normalization/conductor rules. P12.3 envelopes, P12.4 products, P12.5 energy, and P12.6 geometric operators are separate. No claims about their closure are made.

The new retained results are substantial and stronger than a bounded-only reconstruction. N1 proves intrinsic sections, completion, finite lifting and full conductor fibres without removing nonminimal supports. N2 establishes precise source applications at their actual algebraic domains, disclosing historical dependencies and correcting the unit test. N3 proves the corrected density lattice and a normal-target norm trace including all supports, without flatness or defectless e f assumptions. N4 proves continuous uniform descent for EVERY excellent reduced local finite injection by conductor quotient dimension induction, approximate ideal-integrality matching and common powers. N5 constructs continuous strict majorants for unbounded strictly negative fibre-constant completed functions, including partial minus-infinity. N6 proves direct divisorial density, uses analytically irreducible Izumi--Rees to obtain the normal-branch zero dichotomy, descends the active indicator via n4 and produces an ACTUAL decreasing continuous net for mixed-zero descent. This includes all-bottom, all-zero, partial-bottom, conductor-infinite and nonminimal-prime supports. N7 gives the full source-applied smooth BFJ specialization on ALL semivaluations, with the primary/unit exception, minimal-face argument, commuting retraction infima, smooth DVR and empty dimension-zero cases. N9 proves strict separation from the entire raw finite real downstairs ideal cone while giving explicit uniform approximants on every cusp semivaluation. N10 rejects an invalid contraction shortcut and records the mandatory BdFFU sign/domain warning.

N8 supplies an independent ACTUAL Cartier curve-nef definition, directedness and finite evaluation, and a detailed conditional uniform comparison using T=H0(O_Y), a FIXED primary c0 with c0 T inside m, relative ample perturbation and sections. The exact remaining gate is G1--G3 in n8: complete immediate primary proof units for coherence, relative generation/twists, and curve-nef plus ample/openness/fibre-to-relative ampleness at arbitrary excellent reduced NONNORMAL primary blowups are not in the supplied source packet and were not independently read or proved here. The logical comparison implication is proved, but the binding exact-source protocol does not permit promoting those missing premises to unconditional source PASS. No counterexample to these standard-looking statements has been found or claimed. Thus the general independently geometric=ideal comparison has not been certified at the required whole-original proof scope. This is a precise missing geometric premise, not the previously unresolved mixed-zero conductor problem; the latter has been reconstructed in n6 at the ideal-uniform level.

Consequently ORIGINAL P12.2 REMAINS OPEN and candidate=false. The last note DOES NOT claim a complete solution. Familiar background theorem names, supplied receipts, whole-body labels, JSON registration and successful execution do not resolve the gate. There were zero caller mathematical or source grants, and no supplied label is used as a registered support. The historical native232 and native234 actualFINAL files are inventoried data, not imported theorem chains. The complete used native234 paper and ROOT311/312/314/317/319/320 proof units were read and reconstructed with explicit qualifications; unused bodies are not claimed inspected. The original entire family dossier was read as controlling scope. No private active235/P05.1 output, other excluded ACTIVE data, supplied script, network, nested provider, or agent was used.

Fresh deliverables are P12.2-paper.tex and its built PDF, argument.md, source-application-ledger.md, exact-scope.md, whole-proof-coverage.md, original-scope-decision.md, native-notes.json, n1.md through n11.md, own scripts and reports. Rerun commands are python audit_inputs.py, python exact_checks.py, python build_delivery.py, and python final_audit.py. These commands execute only fresh own code, with subprocess argument lists and explicit no-shell-escape for the document build. The own input audit found 42 bound immutable files, all hashes matching, in 47 records including bindings/task files. The finite diagnostics had 32 coefficient checks, 2,976 cusp samples, and 24 exact finite exponent minimizations, with no failures; they are not infinite-domain proofs. Input and own SHA-256 manifests are retained in reports/input-hashes.json and reports/own-hashes.json. Environment and every build attempt, including first warnings and failures if any, are retained. Display truncation warnings during reading were repaired by smaller complete source-unit reads and recorded in reports/execution-history.md. No supervised compute facility was supplied or used; no heavy computation was needed or launched. No runtime, authentication, HOME, CODEX_HOME, proxy, CA, editor, or account settings were mutated.

All notes are unverified drafts. Their valid earlier-local support chain is a bookkeeping property, not mathematical acceptance. This reconstruction supplies useful exact-scope progress and a complete auditable OPEN paper; independent subsequent whole-original review is still necessary for any closure or count change.

