# Whole finite, scalar and conditional bridges for P16.5

BEGIN COMPLETE MATHEMATICAL BODY G0 ACTUAL AMPLE ONLY
BEGIN COMPLETE MATHEMATICAL THEOREM GRANT: G0: Entire original P16.1, ONLY actual ample rational bundles and exact retained hypotheses/foundations
## Sole exact actual-AMPLE mathematical input G0

---
title: "Finite-energy non-Archimedean equations on geometrically unibranch projective varieties"
author: "Research draft reconstructed from the specified primary sources and task-granted lemmas"
date: "5 October 2026"
geometry: margin=0.85in
fontsize: 10pt
header-includes:
  - \usepackage{amsmath,amssymb,amsthm}
  - \usepackage{longtable}
---

# Abstract

We establish the retained domain of original P16.1: reduced irreducible geometrically unibranch projective varieties over an arbitrary algebraically closed trivially valued field of characteristic zero, polarized by an actual ample rational line bundle. The conclusion concerns the genuine intersection-theoretic finite-energy Monge--Ampère operator and all positive Radon targets of its intersection mass and finite intrinsic dual energy, with arbitrary support. The new deduction is original-target envelope regularity. We prove the application joining the specified accepted all-point fiber theorem, actual-reference local conversion, geometric witness construction, and repaired countable original-ring affine theorem. First genuine membership on the original variety precedes envelope regularity and every use of onto birational descent. A separate countable field for each finite competitor removes countability. The general-variety energy theory then gives an actually attained variational maximizer and its equation, with both derivative signs. Normalization, mixed products and unbounded limits preserve the original cycle and raw mass.

This is an unverified research draft. Its mathematical premises include exactly the accepted intermediate bodies supplied with the assignment, in the scopes stated below. Their previous acceptance is a task grant, not a claim of a new independent review. The new application and the final theorem are proved here relative to those grants. Compilation and provenance checks have no mathematical force.

# 1. Statement, conventions and premises

Throughout, $k$ is algebraically closed, has characteristic zero, and has the trivial absolute value. There is no countability assumption unless explicitly imposed in Sections 3--5. A variety is reduced and of finite type. The target $X$ is irreducible, geometrically unibranch, and projective over $k$. It may be nonnormal and singular. Its dimension is $n$. The polarization $L$ is an **actual ample rational line bundle**: a positive integral multiple is an honest ample line bundle. Put $\omega=c_1(L)$ and $V=(L^n)>0$. Intersections use the fundamental cycle. A rational bundle is cleared by tensor powers whenever sections or models occur. Analytic spaces and Radon measures are Berkovich spaces and regular Borel measures. Potentials are scalar differences from the canonical trivial metric on the specified bundle, with values in $\mathbb R\cup\{-\infty\}$.

The genuine space $\operatorname{PSH}(X,L)$ is the space of generically finite psh potentials in the sense of Boucksom--Jonsson (BJ). For ample rational $L$, it is the decreasing-net closure of finite Fubini--Study potentials on that same bundle. Its topology is pointwise convergence on divisorial valuations of $k(X)/k$. This topology is called weak below; it is not convergence at every analytic point. Write $\operatorname{PSH}_{\sup}$ for $\sup_X\varphi=0$. For irreducible $X$, the supremum equals the value at the generic trivial valuation. Finite maxima, constants, genuine pullback and decreasing varying-class closure have their usual BJ meanings.

**Theorem 1 (original retained P16.1).** For every $k,X,L$ just specified, $\omega$ has the envelope property, and $\operatorname{PSH}_{\sup}(X,L)$ is compact in the divisorial topology. There are symmetric positive raw mixed Radon measures
$$
 (\omega_1+dd^c\varphi_1)\wedge\cdots\wedge(\omega_n+dd^c\varphi_n)
$$
for actual ample rational $L_i$ and genuine $\varphi_i\in\mathcal E^1(X,L_i)$, of mass $(L_1\cdots L_n)$, continuous along unbounded decreasing nets with genuine finite-energy limits. In particular
$$
 \operatorname{MA}_{\rm raw,L}(\varphi)=(\omega+dd^c\varphi)^n,
 \qquad \operatorname{MA}_{\rm raw,L}(\varphi)(X^{\rm an})=V.
$$
Define
$$
 E_{\rm raw}(\varphi)=\frac{(\omega,\varphi)^{n+1}}{n+1},\quad
 E_{\rm BJ}=V^{-1}E_{\rm raw},\quad
 \mathcal E^1(X,L)=\{\varphi\in\operatorname{PSH}(X,L):E_{\rm raw}(\varphi)>-\infty\}.
$$
Every positive Radon $\mu$ with $\mu(X^{\rm an})=V$ and
$$
 E_{\rm raw}^{\vee}(\mu)
 :=\sup_{\varphi\in\mathcal E^1(X,L)}
       \left(E_{\rm raw}(\varphi)-\int\varphi\,d\mu\right)<\infty
 \tag{1.1}
$$
has a solution $\varphi_\mu\in\mathcal E^1(X,L)$ of
$$\operatorname{MA}_{\rm raw,L}(\varphi_\mu)=\mu.$$
It is unique modulo one real constant. Condition (1.1) is equivalent to integrability of **every genuine** $\mathcal E^1(X,L)$ potential against $\mu$. There is no imposed support condition. The raw outer energy satisfies
$$
 \left.\frac{d}{dt}\right|_{t=0} E_{\rm raw}^{\downarrow}(\varphi+tf)
       =\int f\,\operatorname{MA}_{\rm raw,L}(\varphi)
 \tag{1.2}
$$
for $\varphi\in\mathcal E^1$ and $f\in C^0(X^{\rm an})$. Finite-energy locality, comparison and domination hold on the original $X$.

For $n=0$, $X=\operatorname{Spec}k$ is literally one point, $V=1$, $E_{\rm raw}(a)=a$, and the empty product is the unit point measure. All finite scalar potentials are solutions; their differences are constants. The arguments involving curves, $I$, or positive-dimensional products below are used only for $n\ge1$.

The theorem retains projectivity, an ample actual rational line bundle, algebraizability, characteristic zero, algebraic closedness and the trivial valuation. It makes no assertion about the other P16 axes, or about nonunibranch singular targets. Arbitrary support here means all measures satisfying the intrinsic condition (1.1); integrability itself excludes prohibited singular mass.

## 1.1. Exact accepted intermediate mathematical assumptions

We use the following supplied theorems. Their names describe mathematical statements, rather than importing an application from a report label. The complete supplied proof bodies are preserved verbatim in the evidence bundle. The binding strings identify which body and clarification are assumed.

**Compact contact theorem.** On a reduced irreducible projective variety over the present fields, continuous rational local contact weights already glued on an actual ample rational bundle admit the algebraic-first PL/model/nef/FS construction. Bounded local decreasing contact limits admit genuine collars with the actual reference, positive raw local products, compact signed integration by parts, mass, comparison and local domination. With genuine EP, these local potentials are genuinely psh. The smooth upper-growth and principal-open removal consequences retain smooth ample-boundary completion and projective birational domination of the **one original witness**, and apply only to the exact unit-log same-constant contact class. Binding of the complete mathematical body: `6a82ecc963545cb9cc6f741e016f73ad82c8c43d9258acab9aa6431b221dba17`; scope clarification: `3d15f7943bb285838a215aae181248bf45b195387aab44d0ed4ae1ade396af9b`. In a collar $v=h_0+p$, the genuine potential is $\Phi=p+\Psi/A$, and $u=A\Phi+Ah_0+M+1$ on the inner open. This exact identity, rather than $\Psi/A$ alone, governs raw products.

**Actual-reference and finite-data theorem.** A genuine psh potential on an actual semiample rational bundle has, on each compact generator-bounded neighborhood with ordinary interior, a decreasing net of finite rational affine FS raw weights in its specified original frame. No target EP is required. If every countable field in the entire geometrically unibranch projective ample-rational domain has EP, then every field in that same domain has EP, by finite obstacle and separate finite-competitor descent. Continuous raw curvature commutes with complete-field pushforward on fixed actual bundles. The general reduced-projective energy operator, target-EP-to-attained-equation deduction, and normalization transport **after approaching target EP** have the stated scopes. Granted binding: `7b995e992b639a526491b52eb85255c613e3f1e980235490858be3c6fde6616c`; complete mathematical proofs are the supplied envelope-to-equation and local-reference/finite-data bodies. We reconstruct the relevant deductions in Sections 6--10; the countable antecedent is proved in Section 5.

**Geometric witness theorem.** A smooth integral affine variety over any algebraically closed characteristic-zero $k$ has a smooth projective compactification with an effective ample Cartier boundary supported exactly on its complement. Each specified proper birational integral witness over that affine variety has a projective birational domination with smooth projective source, retaining a map to the entire witness and the actual pulled references. The same holds for restrictions, products with $\mathbb A^1$, and finite common dominations. Over countable $k$, local decreasing continuous nets have increasing-index sequences with the same pointwise infimum, including $-\infty$, on the prescribed compact neighborhoods. This is not cofinal sequence extraction. The supplied accepted geometric body and its scope are preserved; its complete proof is the text entitled *Geometric witnesses and local sequences for the conditional affine chain*.

**All-point fiber theorem.** For a projective morphism $\pi:Y\to X$ of integral projective varieties with geometrically connected fibers and an actual ample rational $L$ on $X$, every genuine $\pi^*L$-psh potential is constant on every analytic fiber, including the value $-\infty$. Its descended scalar is usc. For a resolution of a geometrically unibranch target, geometric connectedness is proved by factoring through the actual normalization and applying the normal-base Stein theorem before the universal homeomorphism. The complete fixed-ample-perturbation body and its exact curve-current addendum are granted. Section 2 reproduces the mechanism, including its all-point argument.

**Repaired countable original-ring theorem.** Let $k$ be countable in the present field domain and $U=\operatorname{Spec}R$ integral affine. Let $u$ be usc, locally bounded above, finite at the generic trivial seminorm, and bounded above by an actual original-ring affine FS exhaustion. Suppose one proper birational integral witness pulls $u$ back locally to decreasing rational contact sequences on common ordinary neighborhoods. A contact has finitely many unit-log affine coordinates, lies below its weight, and agrees at the tested point with the **same additive constant**; floors handle zero branches. Suppose each specified smooth affine operation has the geometric completions and dominations of the preceding theorem, retaining the restricted witness and actual references. Then $u$ has decreasing original-$R$ affine FS regularization, and strict sublevels are Runge. Its projective consequence uses the **original canonical reference of an actual ample rational bundle**. The complete whole-base trace, controlled approximation, countable barrier, Rossi, Runge, Hartogs and singular-stratum body is granted with its repair. In every Rossi application the relatively compact open $V$ is a neighborhood of the tested point $z$. Positive generator slopes remain positively scaled; real constants are limits of decreasing rational shifts. Sections 3--4 reproduce substantive parts of this proof. Neither a printed weak/global theorem nor the printed envelope theorem alone is a premise.

These are mathematical assumptions in their exact binding scopes; they are not registered note supports. The supplied notes array was empty. Historical provisional qualifications inside the preserved bodies are historical text; the assignment explicitly grants only the exact accepted partial statements above. The first-membership application is not among these assumptions.

| Accepted mathematical proof | Exact supplied body binding | Complete preserved proof |
|:--|:--|:--|
| Geometric witnesses and exact sequence extraction | `1b6a3ffdf27b45f892f0bc1e225c721ecb01d4938fe3abeeed1604ac10905eb5` | `granted/supplied-11.txt` |
| Fixed actual perturbation fiber proof | `447cf79483e6119171585b3630fd53890a9899fad848a9de11495db70b981877` | `granted/supplied-14.txt` |
| Exact curve-current and normalization-factorization addendum | `c8e83ff56c71a8c3d7ecd1e67733f51e57a741883ba84d841e0003f5bc5bcdf6` | `granted/supplied-15.txt` |
| Whole repaired original-witness affine chain | `2cac3d27263a2230a409f375c4d1b94c12bfd5f5e007d5bf35d9e1f98cc52ecb` | `granted/supplied-18.txt` |
| Essential Rossi and rational-constant repair | `c589d09159ecf118494dd677d02d0ae80ad6148dd44739abfc1f2be43cdbd402` | `granted/supplied-19.txt` |

The accepted scope bindings are, respectively, `e9a31b01fc6327daef23539467760e53f89b0397ded5215d20fcdf0ea5d428ed`, `bba37d206249b85b2febefd7fb8fd84fbe107b082c71138e4c471bd2aed7015f`, and `76b0e8d802afd60f3417b81d262aece7c6cffef2925c092bd3893425d6785151`. The complete original-reference/cardinality and equation bodies are `granted/supplied-08.txt` and `granted/supplied-07.txt`; their exact supplied bindings and the retained contact proof's binding are recorded in `supplied-bindings.json`. The original binding strings are identifiers supplied by the task; hashes of the preserved bytes are separately computed, with no claim that a differently delimited body must hash to its binding.

## 1.2. Primary-source scope

BJ means *Global pluripotential theory over a trivially valued field*, arXiv:1801.08229v4, dated March 2022. BE means Boucksom--Eriksson, arXiv:1805.01016v3. The new envelope source is Wu, arXiv:2609.27610v1. We inspect its full pertinent envelope proof, not merely its statement: it calls resolved-nef fiber descent and the weak/global theorem. Our proof supplies the particular application of the accepted replacements instead of treating that printed call as independent evidence. BJ's standing convention allows reduced nonnormal varieties. Section 7 explicitly resumes general projective scope; Sections 8--10 and Theorem 12.8 do not assume a smooth variety. Section 5.20 does, and is used only on the smooth auxiliary source. Theorem 12.9 is the smooth corollary, not the theorem invoked for the final singular target.

The evidence appendix gives a nonnegative indexed external-premise register, exact HTTP(S) primary passages, and complete pertinent statement/proof units. The source files are hashed; LF coordinates always use UTF-8 byte decoding followed by `split('\n')`, inclusively and one-based. No whole-source or recursively complete resolution/semistable proof reading is claimed.

# 2. Fiber constancy with the fixed actual reference

Choose a projective birational resolution $\pi:Y\to X$ with smooth integral projective source. The resolution application is legitimate: a finite-type characteristic-zero integral scheme is Noetherian, excellent, generically reduced and a scheme over $\mathbb Q$. Temkin's exact Theorem 1.2.1 in arXiv:0904.1592v2 supplies a finite sequence of blowups, with centers away from the preimages of the original regular locus and regular final scheme. A blowup is projective from its degree-one generated Rees algebra; integral blowup charts are subrings of the common function field. Thus the composite is projective birational, the original generic fiber is retained, and the final regular variety is smooth over perfect $k$. No strong-resolution correction from an unsupplied continuation is used.

Let $\nu:X^\nu\to X$ be the actual normalization. The smooth normal $Y$ factors through $X^\nu$ in the common function field. The factor is proper by the graph/properness argument, birational, and all its generic points dominate the normal base. The normal-base Stein connectedness theorem therefore gives geometrically connected fibers of $Y\to X^\nu$. Geometric unibranchness makes the finite normalization a universal homeomorphism. After every field extension its geometric fibers have one underlying point; hence the fibers of $Y\to X$ remain geometrically connected. This applies the normal-base theorem to the normal base, not to nonnormal $X$. It uses normalization as an algebraic factorization, without any assertion of onto psh pullback.

Set $M=\pi^*L$. It is an actual semiample nef rational bundle. Here is the fixed-reference proof of the granted fiber conclusion, retaining the parts needed for its present application. Fix an actual very ample $A$ on $Y$. Genuine nef approximation provides finite continuous rational PL $\varphi_i$ decreasing to $\varphi\in\operatorname{PSH}(Y,M)$, with ample classes tending to $c_1(M)$. Use valid pairs $(i,\delta)$, $\delta>0$ rational, for which
$$c_1(M+\delta A)-c_1(L_i)\text{ is ample}.$$
Increasing $i$ and decreasing $\delta$ is directed: take a smaller $\delta$ and an index beyond both original indices and its ample-cone tail. Adding the zero potential in the ample difference class preserves the original scalar $\varphi_i$. Uniform approximation on the **actual** ample $M+\delta A$ is justified by the fixed-bundle FS inclusion, without EP. Pull the finite section formulas before their uniform limits.

For $s\in X^{\rm an}$ and any $y$ in its analytic fiber, extend $\mathcal H(y)$ isometrically by an independent Gauss variable of norm $e^{-1}$, then to a completed algebraic closure $K$. This ensures $\mathbb Q\subset\log|K^\times|$, also when the original norm is nontrivial. The point $y$ has its original scalar value at its $K$-rational lift. On a smooth proper curve $f:C\to Y_K$ mapping into the geometric fiber, a single graph model extends $f$. Its composite into the product model of $X$ is the section $s_K$ everywhere: the equalizer is closed and contains the schematically dense generic fiber of the flat model. Consequently $f^*M$ is literally pulled from a free line over $K^\circ$, with constant reference and zero curvature. The fixed $f^*A$ model is nef and has one positive finite curve curvature $\sigma_A$, of mass $\deg f^*A$. Every component coefficient is retained.

For $v_{i,\delta}=\varphi_i\circ f$, actual fixed-bundle model differences and uniform convergence give the signed current identity
$$dd^c v_{i,\delta}=\mu_{i,\delta}-\delta\sigma_A,\qquad \mu_{i,\delta}\ge0.$$
This is the exact granted curve-current identity, not an assertion based on equality of degrees. On a connected strict affinoid $V$ take the finite Green correction
$$p_\delta=-\delta\sum_{\zeta\in\operatorname{Int}V}a_\zeta g_\zeta^V,
 \quad p_\delta|_{\partial V}=0,\quad \|p_\delta\|\le B_V\delta.$$
The Green functions have interior Laplacian $-\delta_\zeta$. At boundary atoms no interior correction is needed. The exact lisse-current dictionary, including all curve point types, gives $dd^c(v_{i,\delta}+p_\delta)\ge0$ on the interior, hence subharmonicity.

The corrected functions need not decrease. If the original limit $v$ is at most a harmonic $H$ on $\partial V$, the compact closed sets $\{v_{i,\delta}\ge H+\varepsilon\}$ decrease to the empty set. An entire tail is empty. Boundary comparison gives
$$v_{i,\delta}\le H+\varepsilon+B_V\delta$$
throughout $V$. Taking the original net limit, then $\varepsilon\downarrow0$, proves harmonic comparison for $v$. Apply this argument to the bounded genuine floors $\max(\varphi,-m)$; zero is $M$-psh. Each floor pulled to the proper connected curve is bounded subharmonic, attains a maximum, and is constant. Letting $m\to\infty$ proves constancy, including $-\infty$.

This curve assertion compares **every analytic point**. Choose one closed point $z$ in the proper fiber over $\mathcal H(s)$. For each $y$, its above auxiliary $K$ contains a norm-preserving embedding of $\kappa(z)$, since finite extensions of a complete field have a unique extended norm. The geometric fiber is connected. Its reduced component graph is connected, and any two closed points of an integral projective component can be joined by a chain of morphisms from smooth proper curves: resolve the component, lift the points, use sufficiently ample complete intersections through their lifts, and map back; in dimension one use normalization, and dimension-zero components contribute their point. This exact curve-morphism assertion is part of the accepted fiber scope. Constancy of the floors along that chain gives $\varphi(y)=\varphi(z)$. The auxiliary $K$ depends on $y$, but the comparison is to the same original $z$. No usc density argument is substituted.

We obtain one scalar $\psi$ on the **original** $X^{\rm an}$ with $\varphi=\psi\circ\pi$ at every point. Proper analytic surjectivity gives
$$\{\psi\ge a\}=\pi(\{\varphi\ge a\})$$
closed for every finite $a$. Thus $\psi$ is usc, globally bounded above, and finite at the generic trivial valuation, whose birational lift is the generic trivial valuation of $Y$. No genuine target membership has yet been asserted.

# 3. Original contact inputs and geometric witnesses

Assume for now that $k$ is countable. Choose $q>0$ integral so that $qL$ is an honest very ample bundle and choose a generating homogeneous system $s_0,\ldots,s_N$ defining a closed immersion. Put $U_i=D(s_i)$. Its **original** coordinate ring is generated by $s_j/s_i$. In the original $s_i$ frame set
$$\rho_i=q^{-1}\max_j\log|s_j/s_i|,\qquad u_i=\psi+\rho_i.$$
The constant ratio occurs, so $\rho_i\ge0$. Bounded simultaneous generator seminorms are compact, and therefore $\rho_i$ is a proper affine FS exhaustion. Each original section has canonical norm at most one at its valuation-ring center, and a generating section is a unit there. Thus the zero-weight global FS potential is exactly zero. Consequently
$$\rho_i=-q^{-1}\log\|s_i\|_{\rm triv}$$
on $U_i$, the actual original canonical reference. The canonical pulled metric on $M$ is the pullback trivial metric, at every analytic point. Hence the pulled raw weight is exactly $\varphi+\rho_i\circ\pi$. Since $\psi\le B$,
$$u_i\le B+\rho_i.$$
It is usc, locally upper bounded, and finite at the generic trivial point. A rational shift absorbs $B$ in an exhaustion when needed, without changing $u_i$.

The one witness is $P_i=\pi^{-1}U_i\to U_i$. It is integral, finite type, smooth over $k$, and proper birational **over $U_i$**. It need not be affine or proper over $k$. A finite algebraic affine cover of $P_i$ is sufficient for its local contacts.

On a source affine open fix the pulled original $M$ frame and a generating frame of an actual very ample $A$. On a compact generator-bounded $Q$ with strict rational radii exceeding the tested generator norms, the ordinary interior contains the point and both reference weights are finite bounded. Compactness follows from the closed seminorm conditions inside a product of bounded intervals; strict affinoidness over trivial $k$ is unnecessary. With valid pairs as in Section 2 the raw weights are
$$w_{i,\delta}=\varphi_i+h_M+\delta h_A.$$
Here $h_A\ge0$ from its constant branch; the raw net decreases as $i$ increases and $\delta$ decreases, to $\varphi+h_M$, including at $-\infty$. Each fixed pair has uniform FS approximants on the actual $M+\delta A$. Errors $\epsilon_j=4^{-j}$ and rational shifts $b_j=2\sum_{\ell\ge j}\epsilon_\ell$ turn these into decreasing approximants, since $b_j-b_{j+1}=2\epsilon_j>\epsilon_j+\epsilon_{j+1}$. Clear tensor powers. Ratios in the same frame are regular functions. Append all original affine generators and a constant floor at strictly inactive rational weights on $Q$. Flatten by strictly positively shifted finite continuous majorants: compactness supplies a common lower approximant for two such majorants, so minimum closure is unnecessary. This is the granted actual-reference construction, now on the literal pulled frame.

Since $k$ and each finite-type affine ring are countable, seminorm spaces are subspaces of a countable product of real half-lines and are second countable. For the decreasing raw net $a_\alpha$ on $Q$, each open sublevel of its infimum satisfies
$$\{\inf a_\alpha<t\}=\bigcup_\alpha\{a_\alpha<t\}.$$
For rational $t$ a countable subfamily covers it. Gather these indices for every rational $t$ and choose increasing upper indices. The resulting sequence has exactly the same infimum at every point, including $-\infty$. Cofinality is neither required nor claimed. Restrict to the ordinary interior of $Q$, which is a common neighborhood for all finite weights.

At a tested point a finite branch attains the finite maximum. If it is a nonconstant branch, its regular ratio has nonzero seminorm and is an algebraic unit on its principal neighborhood. Its positive rational logarithm plus the same constant lies below the weight and equals it at the point. If the floor wins, its constant is the support. Vanishing inactive branches cannot remove that support. Every rational shift is made to weight and support together. These are exactly the unit-log, rational, same-constant contacts of the repaired countable theorem, not arbitrary positive currents.

We check its geometric hypotheses for every operation, rather than using the word weak to bypass them. A restricted smooth affine open is embedded using generators of its original ring. Its projective closure has the original affine chart and an effective ample hyperplane boundary. Resolve without modifying that smooth open. At a boundary blowup $b$ along $\mathcal I$, some $N$ satisfies $\mathcal O(-ND)\subset\mathcal I$. The effective exceptional Cartier divisor $E$ has $\mathcal O(-E)=\mathcal O(1)$ relatively ample. For sufficiently large $m\ge N+1$,
$$D'=mb^*D-E=(Nb^*D-E)+(m-N)b^*D$$
is effective ample, with support exactly the pulled boundary. This formula works on integral singular intermediate schemes and avoids assigning Weil coefficients there. Iteration supplies the smooth ample-boundary completion.

For the restricted original proper witness use relative Chow over that same affine base; its birational refinement is a closed subscheme of a relative projective space because its immersion is proper. Close **that entire refinement**, rather than only an arbitrarily chosen open generic graph, in the completed base times projective space and resolve. The resulting projective birational map has smooth projective source and retains a dominating map to the entire original witness, including exceptional points. It is not asserted to be a smooth morphism. Localization expresses every original generator as a section ratio in a power of the boundary bundle; append these generators and its boundary section to the actual FS reference. Its pulled reference is the actual pulled bundle/reference at all points.

Restrictions in the trace and removal arguments use this same construction separately. Finite positive combinations and maxima use the original witness and contact sequences first, then limits. Products use $P_i\times\mathbb A^1$ and decreasing logarithmic floors; smooth affine product operations have the same ample-boundary construction. If finitely many witnesses are specified, close their common generic graph in their fiber product, then apply relative Chow and resolution; proper projections dominate all the integral witnesses. This assertion concerns only finitely many witnesses. None of the completed-residue-field comparisons in Section 2 is an application of the countable affine theorem.

Thus every antecedent of the repaired countable original-ring theorem is met for each $u_i$: countable algebraically closed trivial characteristic-zero field; original integral affine ring; usc, locally upper bounded and generically finite input; actual upper growth; one proper birational contact witness; rational decreasing common-neighborhood contacts in the original pulled frame; and the specified geometric completions, restrictions, finite dominations and products. The target EP has not been used.

# 4. Repaired original-witness Runge and Hartogs mechanism

We give proof details of the accepted affine mechanism to make clear what is applied. They are retained under the exact hypotheses of Section 1.1 and now furnished by Section 3.

## 4.1. Whole-base trace, including bad fibers

For a finite surjection $\tau:U\to S\subset\mathbb A^d$ with integral source and normal original base ring, the generic norm extends as a polynomial law. At an analytic fiber its residue characters give positive integer weights $m_y$, totaling the generic degree. They regroup after every complete-field extension; nonflat fiber dimensions are not used. For a finite logarithmic maximum, weighted Gauss multiplicativity gives the original-ring formula
$$
 \sum_{y\mid s}m_y D^{-1}\max_i(\log|b_i(y)|+\lambda_i)
 =D^{-1}\max_{|\alpha|=\deg\tau}(\log|a_\alpha(s)|+\alpha\cdot\lambda),
 \quad N(\sum T_i b_i)=\sum a_\alpha T^\alpha.
 \tag{4.1}
$$
Norm and characteristic coefficients lie in the normal base ring by integrality and its normality. Polynomial Cayley--Hamilton rules out zero residue-character exponents. This explains positivity at nonflat fibers.

Construct the base extension before identifying bad values. On one principal good open where $\tau$ is étale and the original witness is an isomorphism, smooth upper-growth regularization applies with that same witness. Trace its sequence by (4.1), then use smooth principal-open removal on the original base to construct an AFS limit $v$. At a bad analytic point $s$, write its coordinates in $F=\mathcal H(s)$ and join them by an actual $F$-line to a $k$-point of the good open. The reduced inverse image of this line has only horizontal curves: the $d-1$ equations give component dimension at least one, and finiteness gives at most one. Normalize these curves. Their map to the smooth parameter line is finite flat of total degree $\deg\tau$. The rational lift to the **one original witness** extends everywhere by the relative proper valuative criterion at the curve DVRs. The witness need not be proper over $F$.

Restrict every contact approximant along this lift before passing to a decreasing limit. Unit-log contacts become harmonic supports and their same-constant equality proves the harmonic maximum test. The limits are subharmonic or identically $-\infty$. After an isometric nontrivial extension and completed algebraic closure, a smooth curve point has an actual analytic disc coordinate; the inverse is given by the convergent Jacobian contraction on a sufficiently small disc. The parameter map is $t=bz^eU(z)$, $U(0)=1$. In residue characteristic zero, take the convergent $e$-th root of $U$ and change coordinate to get exactly $t=bz^e$.

Above a small strict Gauss radius $r$ there is one Gauss point in each center disc, of radius $(r/|b|)^{1/e}$ and degree $e$. Scaling to radius one reduces its residue polynomial to $Z^e-T$, irreducible over the Gauss residue field; unique extension of a complete-field norm proves uniqueness. Compactness of the finite preimage excludes other points for all sufficiently small radii. Harmonic comparison with the single disc-boundary value gives the radial limit at a finite center; usc gives it at a $-\infty$ center. Equality of polynomial norm laws on the good parameter open identifies the regrouped $e[\kappa:F]$ coefficients with the original $m_y$ at the bad point. Passing the finite positive sum to its radial limit therefore proves $v(s)=\sum m_yu(y)$, even at $-\infty$. This uses no affine regularization theorem over $\mathcal H(s)$.

## 4.2. Original-ring control and the repaired Rossi step

An already regularizable $v\le g+B$ admits decreasing original-ring AFS approximants bounded above by $cg+B'$ for any rational $c>1$, each differing from $cg$ by a bounded function. Compactify the actual $g$ using its cleared monomial powers **and unpowered original generators**. On $Q_i=\{g\le R_i\}$ take a late approximant $v_{j_i}<g+B+1$, and glue
$$a_i=\max(v_{j_i},cg+C_i)\text{ on }Q_i,\qquad a_i=cg+C_i\text{ outside}$$
with $C_i\downarrow-\infty$ and $(c-1)R_i>B-C_i+2$. The reference wins on the whole boundary collar. In the section frame the genuine potential is $a_i-cg_0$, with $g=g_0+p$, and the exterior potential is $C_i+cp$. It is in the actual class $cB_{\rm ref}$ by the compact contact theorem. These weights decrease on the old region, new annulus and exterior separately. Genuine decreasing closure precedes same-bundle FS regularization. Section localization and dominated positive generator padding return literal original-ring approximants.

Pole control is through finite normalization, not a denominator-order assertion. If a branch $b\in R_f$ satisfies
$$q\log|b|\le\max(G,c\log|f^{-1}|)+O(1),$$
height-one valuations of the finite normalization give $q\operatorname{ord}_E b+c\operatorname{ord}_E f\ge0$. Clear denominators and set $h=b^N f^{Nc/q}$. It is integral over $R$. A single $f^M$ clears denominators of a finite module generating list of $R[h]$, so $f^Mh^j\in R$ for **all** $j\ge0$. Original polynomial-hull inequalities, followed by $j$-th roots, give $|h(x)|\le\sup_K|h|$. This proves the hull inequality for branches with an error proportional to $c\sup|\log|f||$. Controlled approximants and then $c\downarrow0$ give the exact hull inequality for the original principal-open limit. It does not assert that an integral function or a prescribed power lies in $R$.

Countability supplies a continuous nonnegative AFS barrier $\rho$ with $\rho\le g+1$ and positive support replacements $\rho'$ satisfying $\rho'\le\rho$, equality at a tested point, and a fixed gap off its neighborhood. One construction enumerates the original ring, uses log-sum-exp of the negative logarithmic coordinates, and sums with rapidly decreasing positive rational coefficients. At a finite-coordinate face its entropy support has positive gap by strict convexity and coercivity; omitted coordinates carry zero coefficients. Rational triangulation of the probability simplex on **all faces** gives uniform rational logarithmic maxima. Positive slope intervals and decreasing rational constants approximate real supports. Floors $\max(\epsilon_jg-j,\cdot)$ retain every original generator and tend to $-\infty$ without changing the limit. Thus a replacement is constructed positively, not by subtracting psh functions.

For compact $K$ the original polynomial hull is compact by its original generator bounds and equals the AFS hull. Strict polynomial neighborhoods with controlled compact closures follow by finite separation of a compact complement. The repaired Rossi statement is: if $z\in\widehat K\setminus K$ and $V$ is a relatively compact open **neighborhood of $z$** with closure disjoint from $K$, then $z\in\widehat{\partial V\cap\widehat K}$. A strict polynomial separator would allow gluing $\max(Cg_0,\log|f|-t)$ inside $V$ to $Cg_0$ outside, with a whole reference-winning collar and $g_0=0$ near $\widehat K$. The compact contact bridge supplies original AFS approximants, zero up to arbitrarily small error on $K$ and positive at $z$, contradicting its hull membership. The condition $z\in V$ is essential and is included in both uses below.

## 4.3. Split pieces and product Hartogs

Suppose a finite $\tau:U\to S$ embeds a bad closed set $Z$ and its complementary inverse-image piece is closed and disjoint. If a sublevel of $u_c=u+c\rho$ is not Runge, a compact hull has an attained finite maximum $x\in Z$, normalized to zero, while the original compact set has supremum at most $-\delta$. Off $Z$, the support-replacement/Rossi/hull argument forces the opposite inequality; hence the maximum is in $Z$.

The hull of $\tau(x)$ lies in $\tau(Z)$. Its compact preimage has two disjoint pieces; properness gives a controlled base neighborhood with entire fibers inside their separated open neighborhoods. The canonical trace of the clopen indicator is continuous integer valued, hence **locally** constant. Shrink one base neighborhood $N$ where the first-piece weight is the positive integer $\gamma$, and retain $N$ for every later boundary and fiber test. The central first-piece fiber is the singleton $x$ by the closed immersion. If $\gamma>1$, usc and properness shrink $N$ so all other first-piece values are less than $\delta/[2(\gamma-1)]$. For $\gamma=1$ its positive integer weights force a singleton of weight one; no division is made.

Take $V$ around $x$, with controlled compact closure in that first piece over $N$ and disjoint from the original compact set. A replacement $\rho'$ equals $\rho$ at $x$ and has boundary gap $\delta'$. The gap of $u+c\rho'$ is $c\delta'$. Glue it on the first piece and zero on the second piece using the global floor/reference $C_0g\circ\tau-\delta$, reference-winning on the whole collar. Its whole-base trace is a genuine original-base AFS limit by Section 4.1, and pulling it back retains all original source generators by monic norm bounds and low padding. Rossi puts $x$ in the hull of its boundary test set. Yet the trace at $\tau(x)$ is zero; at a boundary point in $Z$ it is at most $-\gamma\min(\delta,c\delta')$, and off $Z$ it is at most
$$-m_y\delta+(\gamma-m_y)\frac{\delta}{2(\gamma-1)}\le-\delta/2.$$
For $\gamma=1$ it is $-\delta$. These bounds concern every fiber in the **same $N$**, with the original positive weights. This contradiction proves Runge. Let rational $c\downarrow0$ to get the original sublevel; increasing Runge unions are Runge by compactness.

Runge on $U$ alone is insufficient for Hartogs. On the same product witness $P\times\mathbb A^1$ use
$$H=\log|w|+u\circ p,$$
with $-\infty$ on the zero section and where $u=-\infty$. Decreasing floors of $\log|w|$ and positive sums of the original contacts verify the product input. The split proof on $\tau\times\mathrm{id}$ gives the genuine product Runge domain $D=\{H<0\}$.

Only **after** this, take an increasing exhaustion by strict polynomial opens with compact controlled closures inside $D$, possible from countability and Runge. Write their original polynomials as $\sum_i a_{rji}w^i$. On
$$\Omega_r=\{\log|a_{rj0}|<b_{rj}\ \forall j\},$$
the fiber's open-disc radius is exactly
$$-\log d_r(y)=\max_{j,i\ge1}\frac{\log|a_{rji}(y)|-b_{rj}}{i}.$$
The strict constant-coefficient conditions are indispensable. Arbitrary-radius Gauss norms prove the formula, including an infinite radius/empty maximum. Compact closed discs and exhaustion imply $d_r\uparrow d_D$, with $-\log d_D=u$. Expanding whole-floor collars, the actual reference and genuine decreasing closure give original-ring AFS regularization of $u$. No convergence of an unbounded discontinuous limit is called Dini convergence.

## 4.4. All strata and final globalization

When only $\tau|Z$ is a closed immersion, descend
$$Z_{r+1}=Z_r\cap\overline{\tau^{-1}\tau(Z_r)\setminus Z_r}.$$
Every component of $Z_r$ is a component of its inverse image by finiteness and dimension preservation, so the complementary closure omits its generic point. Dimensions strictly decrease. Outside the inverse image of $\tau(Z_{r+1})$ the split pieces are closed and disjoint. Use exact original opens $U'=\tau^{-1}(S')$; product split/Hartogs gives local regularization at the next stage. Points still over $\tau(Z_{r+1})$ but off $Z_{r+1}$ are off the original $Z$ by injectivity and use the original good cover.

For a smooth proper closed stratum through a closed point, projection of a projective closure successively from points outside its secant cone, tangent space and ambient closure gives a finite map to a principal open of affine space embedding the stratum. Secant exclusion gives a singleton fiber; injective differential and Nakayama show the finite local image algebra equals the stratum algebra. Keep the boundary in the projected auxiliary closed set and choose the base open avoiding its image. Thus the inverse-image affine open is contained in the **original** affine variety. Monic integrality supplies the required base-growth bound.

The reduced singular loci in characteristic zero strictly drop dimension on every component, including reducible unequal-dimensional strata. Smooth affine gate regularization initializes the induction; the projection and descending-$Z$ argument handle each new smooth stratum with the restricted original witness. A closed-point cover covers all scheme and analytic points because finite-type schemes over a field are Jacobson. Finally apply the **empty-$Z$** off-bad-set argument, then its product Runge/Hartogs argument, to the local cover. This is the missing final local-to-global step; a local cover alone is not the affine conclusion. It proves the original-ring regularization used in Section 5. All its smooth geometric operations have been supplied in Section 3.

# 5. New join: first genuine membership, compactness, target EP

Apply the now matched countable theorem to each original $u_i$. Its output is a decreasing affine FS sequence in the original ring of $U_i$. For rational $c>1$ perform the controlled construction on **the original projective compactification $X$**, actual bundle $L$, section $s_i$ and reference $\rho_i$. The limit in the actual class $cL$ is
$$
 \psi_i^{(c)}=\psi-(c-1)\rho_i\text{ on }U_i^{\rm an},\qquad
 \psi_i^{(c)}=-\infty\text{ outside }U_i^{\rm an}.
 \tag{5.1}
$$
Indeed its raw weight there is $u_i$, and subtracting the $cL$ reference $c\rho_i$ gives (5.1). On each expanding collar the reference wins on the full boundary neighborhood; the original scalar growth $u_i\le\rho_i+B$ forces the canonical limit to $-\infty$ at the boundary. Genuine decreasing closure, followed by same-class FS conversion, proves (5.1) is genuine. The raw reference is not silently replaced by a numerical representative.

At every analytic point choose a homogeneous coordinate of maximal canonical norm. It is nonzero, its chart contains the point, and $\rho_i=0$ in that chart. All other defined $\rho_j\ge0$, and absent-chart contributions are $-\infty$. Therefore
$$\max_i\psi_i^{(c)}=\psi$$
at every analytic point, including where $\psi=-\infty$. Finite maxima show $\psi\in\operatorname{PSH}(X,cL)$ for each rational $c>1$. Use the **constant scalar family $\psi$** as $c\downarrow1$ in varying-class decreasing closure. It is generically finite by Section 2, so $\psi\in\operatorname{PSH}(X,L)$. The individual chart extensions increase with decreasing $c$; they are not the decreasing family used in this closure. This proves first genuine original membership without target EP.

Genuine pullback in the other direction follows from BJ 4.7 and birational generic finiteness. Fiber constancy and first membership make
$$\pi^*: \operatorname{PSH}(X,L)\longrightarrow\operatorname{PSH}(Y,\pi^*L)$$
an onto bijection. Divisorial valuations on the common function field are the same coordinate set. The map and inverse are continuous in their pointwise divisorial topologies; this conclusion uses actual equality of values, not merely density. Analytic surjectivity preserves original suprema. Normalized spaces are consequently homeomorphic.

BJ 5.20 and 5.21 give EP and normalized compactness on the smooth projective source for the nef class $c_1(\pi^*L)$. Transport compactness through this homeomorphism. General-projective BJ 5.11 now gives EP for $\omega$ on the original $X$. We have proved this for **every** countable algebraically closed trivial characteristic-zero field, reduced irreducible geometrically unibranch projective target, and actual ample rational $L$. This is precisely the entire antecedent of the granted finite-data theorem, rather than one fixed field or one line bundle. No use of BJ 5.13 has occurred.

# 6. Removing countability one finite competitor at a time

Let $k$ now be arbitrary. First let $f$ be a finite rational PL obstacle. Its finite flag/model description, $X,L$, an ample embedding, and the actual normalization descend to some countable algebraically closed $k_0\subset k$. Include normalization presentations, finite multiplication tables, overlaps, and inverse on a dense open. Faithful flatness descends integrality and reducedness; it descends normality of the finite normal source. In the common function field, a finite normal birational algebra is the integral closure, so the descended map is the **actual** normalization. The universal-homeomorphism property descends fpqc, giving geometric unibranchness of the original $X_0$. This is the exact finite-data descent theorem granted in Section 1.1. It does not normalize the generic fiber of a test configuration or replace nonnormal $X_0$ by its normalization. The ample embedding retains the actual rational $L_0$.

Restriction $r:X_k^{\rm an}\to X_0^{\rm an}$ is surjective. Explicitly, for $x\in X_0^{\rm an}$ adjoin to $\mathcal H(x)$ independent radius-one Gauss variables for a transcendence basis of $k/k_0$, complete, extend its real norm to an algebraic closure, embed the algebraic extension defining $k$, and complete again. Each polynomial involves finitely many variables. The embedded $k$ has trivial norm by the dominant-term test in a monic equation with nonzero constant, while the norm of $\mathcal H(x)$ is unchanged. Evaluation gives the required lift. No cardinality bound is involved.

By Section 5, $\psi_0=P_{L_0}(f_0)$ is continuous and genuine. Its pullback $\psi$ is continuous and genuine on the original $L$. On these actual fixed bundles, continuous raw curvature has pushforward
$$r_*\operatorname{MA}_{\rm raw}(\psi)=\operatorname{MA}_{\rm raw}(\psi_0). \tag{6.1}$$
Here BJ 3.9 puts $\mathcal H^{\rm dom}(c_1(L_0))$ in $\mathcal H(L_0)$ for the same bundle, and BJ 4.16 gives uniform approximation without EP. BE 7.14 supplies corresponding smooth semipositive metrics; BE 8.3(iv) gives pushforward at every smooth stage with the analytic fundamental cycle, and BE 8.4 gives weak continuity under uniform limits. Pushforward is weakly continuous on compact analytic spaces. BE 8.18 and BJ 7.23 identify this with the genuine energy-pairing operator. The actual reference, coefficients, multiplicities and volume are unchanged. No unbounded base-change limit is used in (6.1).

Orthogonality on $X_0$ follows from EP. For $p=P(f_0)$, the envelope of $p+t(f_0-p)$ is still $p$ for $0\le t\le1$. The energy derivative gives
$$\int(f_0-p)\,\operatorname{MA}_{\rm raw}(p)=0.$$
The nonnegative integrand and (6.1) transfer this equality. This integral identity, rather than an unjustified equality of inverse images of supports, is used below.

For **each** finite competitor $h\in\mathcal H^{\rm dom}(c_1(L))$, $h\le f$, use its literal same-$mL$ section representation. Choose its own enlarged countable algebraically closed field $k_h\supset k_0$ containing the finitely many coefficients of its sections. Section base change follows from the matching equalizer on a finite affine trivializing cover; flat extension commutes with that finite equalizer. Faithful flatness descends vanishing of the evaluation cokernel, so its sections still generate. Thus $h_h\in\mathcal H(L_h)$ is genuine. Surjectivity of restriction transfers $h_h\le f_h$.

The pullback $\psi_h$ of $\psi_0$ is continuous genuine and bounded, hence finite energy, without assuming EP over $k_h$ anew. Continuous raw pushforward transfers orthogonality to $k_h$. Therefore $h_h\le f_h=\psi_h$ almost everywhere for $\operatorname{MA}(\psi_h)$. General irreducible-projective domination, which requires no EP or inverse equation, gives $h_h\le\psi_h$ everywhere. Pullback gives $h\le\psi$ on the original $X_k$.

For an arbitrary actual competitor $a\in\operatorname{PSH}(X,L)$ with $a\le f$, take its genuine decreasing net $h_j\in\mathcal H^{\rm dom}(c_1(L))$. For rational $\varepsilon>0$, the compact closed sets $\{h_j\ge f+\varepsilon\}$ decrease to the empty set. An entire tail is empty. Apply the finite-competitor argument to $h_j-\varepsilon$, with a **separate enlarged field for each such finite representation**. Then $a\le h_j\le\psi+\varepsilon$. Let $\varepsilon\downarrow0$. Since $\psi\le f$ is feasible, this proves the exact original envelope identity
$$P_L(f)=P_{L_0}(f_0)\circ r.$$
No field is assigned to an arbitrary psh family or net.

Rational PL density and the envelope Lipschitz inequality extend continuity to all continuous obstacles; genuine uniform closure keeps their envelopes genuine. BJ 5.17 gives EP. General BJ 5.11 then gives normalized compactness on this possibly nonmetrizable original target. In particular all positive rational multiples of $L$ have EP. These are the approaching target classes needed later. If real ample classes are desired, BJ 5.9 and closure from rational ample classes above give the same conclusion; the theorem itself requires the actual rational $L$.

# 7. Genuine raw energy and mixed operator on the original variety

We spell out why the primary global theory does not require smoothness. On a relatively integrally closed test configuration dominating the trivial configuration, the generic fiber remains the **original** reduced variety. Integral closure is relative inside its given generic fiber. At generic points of the central fiber the vertical local rings are DVRs. If $E$ is a central component, write
$$b_E=\operatorname{ord}_E(t),\qquad v_E=b_E^{-1}\operatorname{ord}_E|_{k(X)}.$$
For genuine PL entries the raw mixed measure is
$$\sum_E b_E\bigl((\omega_{1,\mathcal X}+D_1)|_E\cdots
                         (\omega_{n,\mathcal X}+D_n)|_E\bigr)\delta_{v_E}. \tag{7.1}$$
Nefness makes its coefficients nonnegative. The fundamental-cycle projection gives its raw intersection mass. Neither $b_E$ nor the original generic-fiber identification can be suppressed by absolute normalization.

The algebraic symmetric intersection pairing extends to psh entries by the infimum over genuine finite $\mathcal H^{\rm dom}$ majorants. It is monotone and weakly usc: if a tuple's infimum is below $t$, choose finite majorants whose pairing is below $t-\epsilon$. Continuity of $\sup(\varphi-\psi)$ for fixed PL $\psi$ supplies neighborhoods in which the old majorants plus small constants remain majorants; the constant intersection formula bounds the pairing below $t$. Monotonicity and usc give decreasing-net continuity. This is BJ 7.1 on general projective $X$.

The energy $E_{\rm BJ}$ is concave, monotone, weakly usc and decreasing-net continuous; $E_{\rm BJ}(\varphi+c)=E_{\rm BJ}(\varphi)+c$, whereas $E_{\rm raw}(\varphi+c)=E_{\rm raw}(\varphi)+Vc$. Its finite-energy cone is upward closed within psh, contains bounded psh, and has finite mixed pairings. BJ 7.8 proves the necessary mixed finiteness and class comparison from intersection estimates on the PL cone and monotone passage. Differences of finite-energy potentials, taken on the linear-growth locus where their values are finite, span a vector space $\widetilde{\mathcal E}^1$. The positive cone of pairs $(\omega,\varphi)$ spans $N^1(X)\times\widetilde{\mathcal E}^1$. Its symmetric positive multilinear pairing consequently has a unique signed multilinear extension, BJ 7.14. It does not define pointwise subtraction of two $-\infty$ values on all of $X^{\rm an}$.

For a PL real test $f$ define
$$\ell(f)=(0,f)\cdot(\omega_1,\varphi_1)\cdots(\omega_n,\varphi_n).$$
Monotonicity implies positivity when the $\varphi_i$ are genuine psh. The constant test gives $\ell(1)=(L_1\cdots L_n)$, so positivity gives $|\ell(f)|\le\ell(1)\|f\|_\infty$. PL density extends $\ell$ uniquely to a positive continuous functional on $C^0(X^{\rm an})$. Riesz representation gives the genuine positive mixed Radon measure, BJ 7.18, with raw mass and model formula (7.1), BJ 7.19. For signed entries it gives signed measures by multilinearity. The symbols $\omega_i+dd^c\varphi_i$ denote this product construction; no undefined singular individual current factors are needed.

For decreasing genuine nets $\varphi_{ij}\downarrow\varphi_i$ with finite-energy limits, all PL test pairings converge by BJ 7.14. Their positive measures have the fixed raw mass; uniform PL approximation of any continuous test therefore proves weak convergence. This is an **unbounded net** assertion, not only a bounded or sequential construction. For different ample classes take one sufficiently large actual ample reference class dominating their finite list; genuine zero-class additions and the class comparison of BJ 7.8 place all factors in the common finite-energy cone, without changing their actual scalars.

Weighted convergence holds if the psh test $\varphi_0$ is integrable for the limiting mixed measure. Its integral is exactly
$$
 (\omega_0,\varphi_0)\cdot\prod_{i=1}^n(\omega_i,\varphi_i)
 -(\omega_0,0)\cdot\prod_{i=1}^n(\omega_i,\varphi_i).
 \tag{7.2}
$$
The same order holds at every finite stage. Decreasing pairing continuity gives convergence of total weighted integrals; translating the tests below zero, apply the positive lsc weighted-measure lemma to their negatives and obtain weak weighted convergence, BJ 7.21(ii). The printed reverse order in the proof is corrected by the defining identity (7.2). Bounded other factors ensure integrability; finite-energy tests are integrable for finite-energy mixed factors by BJ 7.19(v). A difference of two decreasing sequences need not decrease and is handled by its two converging terms.

All these proofs use relative integral closure, nef intersections, PL density, monotone energy and finite mixed estimates on a reduced projective variety. Smoothness is not one of their hypotheses. The result is the existing genuine operator, rather than a measure assigned by an inverse construction.

# 8. Intrinsic dual energy, derivatives and comparison

Put $\bar\mu=\mu/V$. Directly from the definitions,
$$E_{\rm raw}=V E_{\rm BJ},\qquad
 E_{\rm raw}^{\vee}(\mu)=V E_{\rm BJ}^{\vee}(\bar\mu),\qquad
 \operatorname{MA}_{\rm raw}=V\operatorname{MA}_{\rm BJ}. \tag{8.1}$$
No probability factor is included in (7.1) or in the raw mixed mass. The variational objective is constant invariant exactly for targets of mass $V$.

Finite dual energy immediately implies integrability of every genuine finite-energy potential. Conversely suppose all are integrable. Normalize $\sup\varphi=0$, so $J(\varphi)=-E_{\rm BJ}(\varphi)$. Integrals of $-\varphi$ are bounded uniformly on every set $J\le C$: otherwise select $\varphi_j$ with $\int-\varphi_j\,d\bar\mu\ge2^j$ and form the genuine decreasing sums $\sum_{j\le m}2^{-j}\varphi_j$, adding unused weight times zero. Concavity gives energy at least $-C$, the generic trivial value remains zero, and decreasing closure gives an actual finite-energy limit. Its integral is infinite by monotone convergence, a contradiction.

For arbitrary normalized $\varphi$, apply this bound to $t\varphi$, $t=J(\varphi)^{-1/2}\le1$ when $J\ge1$. The energy estimate $J(t\varphi)\le C_n t^2J(\varphi)$ gives
$$\int(-\varphi)\,d\bar\mu\le A\sqrt{J(\varphi)}+B.$$
Consequently $E_{\rm BJ}(\varphi)-\int\varphi\,d\bar\mu\le-J+A\sqrt J+B$ has finite supremum. This is BJ 9.20 on irreducible projective varieties. The signs are expressed for the nonnegative integral of $-\varphi$. No support restriction or solution is assumed in this integrability characterization.

Define the extended energy on continuous $f$ by the supremum of psh energies below it, and its outer extension on upper bounded usc $u$ by
$$E_{\rm BJ}^{\downarrow}(u)=\inf_{f\in C^0,\ f\ge u}E_{\rm BJ}(f).$$
It is monotone, concave, translation equivariant and decreasing-net continuous. On genuine psh it agrees with energy. Under the now proved target EP it equals $E_{\rm BJ}(P(u))$ for upper bounded usc $u$, BJ 8.3.

BJ 8.5 is a general-projective theorem: for fixed $f\in\operatorname{PL}_{\mathbb R}(X)$,
$$E_{\rm BJ}^{\downarrow}(\varphi+tf)
 =E_{\rm BJ}(\varphi)+t\int f\,\operatorname{MA}_{\rm BJ}(\varphi)+O(t^2), \tag{8.2}$$
uniformly in $\varphi\in\mathcal E^1$. Its proof first writes $f=\psi_1-\psi_2$ with genuine PL $\psi_i$ in one actual ample class. The continuous relative-volume estimate in BJ 8.7--8.8 compares the energy difference to the mixed product after adding $t(\omega'+dd^c\psi_1)$. The volume difference is $O(t)$ and the finite positive mixed terms have their fixed intersection masses, yielding $O(t^2)$. The case of negative $t$ follows by $-f$. A decreasing genuine continuous net to an unbounded $\varphi$ passes this estimate to outer energy, by its decreasing continuity and the raw mixed convergence of Section 7. The constant is uniform, so no unbounded-stage error is lost. The theorem's use of volumes of sections and continuous metrics on ample bundles is on general projective varieties; it does not require resolving $X$ or multiplier ideals on $X$ here. The exact accepted global deduction and the primary full proof unit justify this input, including its cited relative-volume background within that deduction.

For $f\in C^0$ approximate uniformly by PL $f_m$ with error $\epsilon_m$. For every real $t$,
$$\varphi+tf_m-|t|\epsilon_m\le\varphi+tf\le\varphi+tf_m+|t|\epsilon_m.$$
Outer monotonicity and translation bound the energy error by $|t|\epsilon_m$. Apply (8.2) first, divide by $t$ with the appropriate sign, then let $m\to\infty$. The lower and upper errors are $-\epsilon_m$ and $+\epsilon_m$. This proves both derivatives and, after multiplication by $V$, (1.2). No $t^2\epsilon_m$ error is mistakenly substituted.

Genuine locality and comparison are also general-projective. For PL potentials, on a central component where one strictly wins over the other, the model divisor of their maximum agrees with the winning divisor near the entire component; (7.1) proves equality of its coefficient. For unbounded $\varphi,\psi\in\mathcal E^1$, approximate both decreasingly and use the nonnegative difference $\max(\varphi,\psi)-\psi$. Weighted convergence is applied term by term to the two genuine tests in (7.2), not to a falsely decreasing difference. This gives
$$\mathbf1_{\{\varphi>\psi\}}\operatorname{MA}_{\rm raw}(\max(\varphi,\psi))
 =\mathbf1_{\{\varphi>\psi\}}\operatorname{MA}_{\rm raw}(\varphi).$$
The Borel strict winning set need not be open in the analytic topology. Displaced maxima $\max(\varphi,\psi-\epsilon)$ and equal raw masses $V$ imply
$$\int_{\{\varphi<\psi\}}\operatorname{MA}_{\rm raw}(\psi)
 \le\int_{\{\varphi<\psi\}}\operatorname{MA}_{\rm raw}(\varphi). \tag{8.3}$$
Letting $\epsilon\downarrow0$ uses ordinary continuity from below. Mixed locality follows by polarization. These are BJ 7.40--7.44. The proof's limiting cross-reference is read as the weighted result 7.21(ii), not the unrelated scaling assertion 7.19(iii).

With probability calibration define
$$I(\varphi,\psi)=\int(\varphi-\psi)
       (\operatorname{MA}_{\rm BJ}(\psi)-\operatorname{MA}_{\rm BJ}(\varphi))\ge0.$$
BJ's general equidimensional uniqueness estimate makes $I=0$ imply equality modulo constants. Its proof normalizes the suprema, tests the energy estimates against divisorial Dirac measures (finite energy independently of an inverse Dirac equation), and applies divisorial determination to get equality everywhere. Irreducible $X$ is connected and equidimensional, so one constant suffices. If $a\in\operatorname{PSH}$ is at most $b\in\mathcal E^1$ almost everywhere for $\operatorname{MA}(b)$, replace $a$ by $\max(a,b)\in\mathcal E^1$. Then
$$I(a,b)=\int(b-a)\operatorname{MA}(a)\le0,$$
so $I=0$; almost-everywhere equality fixes the constant to zero. This proves domination, BJ 10.6, without EP or inverse-equation existence. It is the principle used in Section 6. Thus smoothness is unnecessary for differentiation, comparison, uniqueness and domination; the hypotheses actually needed are those of the general reduced-projective primary theory.

# 9. An actually attained variational solution

Let $\mu$ satisfy (1.1) and let $D=E_{\rm BJ}^{\vee}(\bar\mu)<\infty$. Take a sequence of **genuine** $\mathcal E^1$ potentials $\varphi_j$, normalized to supremum zero, whose objective tends to $D$. Set
$$J_{\bar\mu}(\varphi)=D-E_{\rm BJ}(\varphi)+\int\varphi\,d\bar\mu\ge0.$$
The general-projective strict energy concavity estimate, BJ 9.15--9.16, gives
$$J(\varphi_j)\le C_n\bigl(J_{\bar\mu}(\varphi_j)+D\bigr).$$
The right side is eventually bounded. Section 6 supplies compactness of the **original** normalized PSH space, so a subnet converges weakly to an actual $\varphi\in\operatorname{PSH}_{\sup}(X,L)$. Weak lower semicontinuity of $J$ implies $J(\varphi)<\infty$, hence $\varphi\in\mathcal E^1$. Compactness is net compactness; the possibly uncountable field is never made metrizable here.

We use the exact target-integral continuity of BJ 9.19. On each bounded-$J$ set, $a\mapsto\int a\,d\bar\mu$ is a uniform limit of the continuous integrals against finite PL model measures obtained from maximizing PL potentials for the finite-energy target. The quantitative energy estimate controls this approximation uniformly; these finite model integrals are continuous in divisorial coordinates. For a weak bounded-$J$ net to $a$, its maxima with $a$ still have bounded $J$. The correct identity
$$|b-a|=2(\max(b,a)-a)-(b-a)$$
then yields $L^1(\bar\mu)$ convergence. The printed plus sign in that identity is corrected. Applying this to our subnet gives $\int\varphi_j\,d\bar\mu\to\int\varphi\,d\bar\mu$.

Weak energy upper semicontinuity now gives
$$E_{\rm BJ}(\varphi)-\int\varphi\,d\bar\mu
 \ge\limsup_j\left(E_{\rm BJ}(\varphi_j)-\int\varphi_j\,d\bar\mu\right)=D.$$
The definition of $D$ gives the reverse inequality. Thus $\varphi$ is an **actually attained genuine finite-energy maximizer**. This proof does not merely produce weak convergence of measures, an abstract completion, an $I$-Cauchy object or an approximate maximizer. BJ 12.8(i)$\Rightarrow$(ii) is precisely this general-variety implication. Its compactness input is the general 5.11 under EP; the smooth 5.21 reference in its proof is not a new smoothness assumption.

For a PL test $f$ and $t\in\mathbb R$, duality for upper bounded usc functions gives
$$E_{\rm raw}^{\downarrow}(\varphi+tf)-\int(\varphi+tf)\,d\mu
 \le E_{\rm raw}^{\vee}(\mu)
 =E_{\rm raw}(\varphi)-\int\varphi\,d\mu.$$
One may see this directly after target EP: $P(\varphi+tf)$ has energy $E^{\downarrow}$, lies at most $\varphi+tf$, and lies between $\varphi\pm|t|\|f\|_\infty$, hence is genuine finite energy. Its objective bounds the displayed left side and is at most the attained supremum. Use the raw version of (8.2). For $t>0$, divide by $t$ and let $t\downarrow0$ to obtain
$$\int f\,\operatorname{MA}_{\rm raw}(\varphi)\le\int f\,d\mu.$$
Use $-f$, or divide the $t<0$ inequality with the reversed sign, to get the opposite inequality. Equality holds for every real PL test. Uniform density and the common finite mass $V$ identify the positive Radon measures on all continuous tests. Therefore
$$\operatorname{MA}_{\rm raw,L}(\varphi)=\mu.$$
Equal measures make $I=0$ and Section 8 proves uniqueness modulo constants. Conversely an actual finite-energy solution has finite dual energy by energy concavity and computes the dual supremum, so (1.1) is the exact equation class. No retraction, invariance, skeletal support, alternative measure or regularity stronger than actual finite energy is used.

# 10. After-EP normalization and every unbounded transport

Only now use BJ 5.13. For each $m$, $(1+1/m)\omega$ has target EP by Sections 5--6, and its difference from $\omega$ is ample. The finite birational normalization $\nu:X^\nu\to X$ is a projective birational map and $\nu^*L$ is ample. BJ 5.13 therefore gives onto genuine psh pullback at $\omega$. The analytic normalization map is a homeomorphism because the algebraic map is a finite universal homeomorphism; complete-field fibers have one analytic norm extension. This topological statement alone is not the finite-energy comparison.

The generic degree is one and
$$\nu_*[X^\nu]=[X],\qquad (\nu^*L)^n=(L^n)=V.$$
At finite PL stages, projection of the original fundamental cycle gives equality of the raw intersection pairings with the actual pulled bundles. Continuous compatibility uses the original metrics and their fixed-bundle approximation; the central coefficients remain $b_E$ and the fundamental multiplicities. For unbounded genuine pulled potentials, take genuine decreasing finite approximants on the original target. BJ 7.1--7.2 passes the equality to extended pairings, including value $-\infty$. BJ 7.7 and 7.8 identify finite energy exactly, so onto psh pullback is onto $\mathcal E^1$, not just onto bounded potentials.

For every tuple of these finite-energy potentials, BJ 7.19, or their decreasing approximants tested by PL and then continuous functions, gives
$$\nu_*\bigwedge_i(\nu^*\omega_i+dd^c\nu^*\varphi_i)
       =\bigwedge_i(\omega_i+dd^c\varphi_i).$$
All limits have genuine finite-energy endpoints; masses stay the fixed raw intersection masses; pushforward is continuous for weak Radon convergence on compact spaces. Integrable weights pass by the correctly signed test pairing (7.2), not by bounded convergence for discontinuous unbounded weights. This handles every unbounded mixed-product and energy transport used here. No singular normalization inverse theorem was used to prove Section 5.

If $\mu^\nu$ is the unique transported measure under the analytic homeomorphism, integration of an actual pulled potential is identical to its original integral, including $-\infty$. Onto $\mathcal E^1$ and preserved raw energy give identical dual-energy suprema. The positive raw equation, comparison and uniqueness therefore agree on the normalization and the original target. This transport retains nonnormal $X$ as the equation target. The resolution's nonample pulled class was used only for first membership and compactness; the final operator and variational argument take place on the original ample target.

# 11. Evidence, reproducibility and conclusion of the proof

The new join has no remaining geometric or analytic antecedent in its retained domain: Section 2 supplies all-point scalar descent, Section 3 checks every contact/witness/growth/geometric input, Sections 4--5 give original-reference first membership and compactness, and Section 6 matches and removes the entire countable antecedent. Sections 7--9 construct the genuine operator and an attained raw equation solution; Section 10 orders normalization and all unbounded limits after approaching target EP. Thus Theorem 1 proves exactly the assigned retained P16.1 domain relative to the task-granted accepted intermediate theorems, unconditionally with respect to the geometric, contact and countability conditions of that domain.

The evidence bundle preserves `input-original.json` byte identically; `task-original.json` preserves its exact task value and `assignment-original.txt` its exact assignment string. It contains the 23 catalogue primary files with exact checksums, all 43 supplied literal source units, additional complete relevant BJ statement/proof units, the preserved accepted mathematical bodies, and primary HTTP response observations. The newly fetched Temkin evidence is a version-pinned primary **rendered transcript**; its transcript bytes and complete pertinent proof units are hashed. A shell PDF download failed because its proxy connection was unavailable, so no locally downloaded Temkin PDF hash or original-PDF LF coordinates are invented. Its exact public version and original rendered line labels are retained, alongside one-based LF coordinates in the saved transcript. Desingularization's earlier recursively cited algorithms remain published background, within the geometric task grant; a new full proof of resolution is not claimed.

Run `python3 rerun.py` here. It verifies exact preserved inputs, source checksums, literal inclusive-LF slices, external-premise coverage, and the backwards note-support registry; existing Pandoc generates `P16.1-paper.tex`, and existing pdfLaTeX runs twice. Exact argv, stdout/stderr, pass logs, versions, environment details and final hashes are retained. No tools are installed. No editor, source cache, repository, authentication or runtime is modified. Only the supplied input, authorized primary paths, exact public primary sources and this fresh workspace are read. No other worker or frozen independent review is inspected or used. No resource-heavy computation is needed; no supervised compute facility was exposed.

The mathematical conclusion is a proof draft, not a certification by compilation, hashes or prior historical verdicts. The premise ledger distinguishes external primary theorems from the task-granted partial bodies and from the new applications proved above. Diagnostic historical text does not supply a new premise. The unchanged contextual P16 family and completion criterion remain in the preserved task; only original P16.1 in the explicitly retained domain is claimed here.

# Appendix A. Primary statements and complete pertinent proof units

The external register generated with this paper assigns consecutive indices starting at zero. Each record states a standalone mathematical premise, its exact public version and URL, and the retained literal statement and proof units with byte hashes and inclusive LF coordinates. The following are the primary theorem groups used in the argument. Underlying theorems used wholly inside an accepted mathematical body are part of that task-granted body's scope, not invented additional registered supports.

1. **Resolution.** Temkin, arXiv:0904.1592v2, Theorem 1.2.1: every Noetherian quasi-excellent generically reduced scheme over $\operatorname{Spec}\mathbb Q$ has the finite regular-final blowup sequence specified in Section 2. The statement, finite-sequence definition, stabilization lemma, Cartier pullback lemma and entire pertinent Section 4.3 proof are retained from the public primary transcript. The geometric hypotheses for our application are verified in Section 2 and included in the accepted geometric construction.
2. **Genuine cones and original reference.** BJ's conventions, canonical section evaluation, fixed actual-bundle FS representation and inclusion, decreasing varying-class closure, genuine pullback, divisorial determination and finite approximation: Definitions and Theorems 2.18, 2.31, 3.9--3.10, 4.5--4.7, 4.15--4.16, 4.22 and 4.28. The field is algebraically closed trivial; projective varieties may be nonnormal.
3. **Envelopes and compactness.** BJ 5.11 and 5.17 apply on irreducible projective targets, with no smoothness assumption. BJ 5.20--5.21 supply the characteristic-zero smooth-source nef case. BJ 5.13 requires approaching EP on the target and is used only in Section 10.
4. **Energy and operator.** BJ 7.1--7.2, 7.7--7.8, 7.14, 7.18--7.21 extend the actual symmetric pairing and give raw positive mixed Radon measures, intersection mass, every central $b_E$, integrability and unbounded decreasing-net continuity on the general reduced-projective domain.
5. **Derivatives.** BJ 8.2--8.8 give outer energy and its uniform PL derivative on general projective $X$, and the continuous-direction extension. The exact proof units retain the relative-volume input and their published scopes; Section 8 supplies the corrected elementary signs and factors.
6. **Measure energy and attainment.** BJ 9.1, 9.9--9.20 give duality, both PL test signs, bounded-$J$ estimates, target $L^1$ continuity, and the irreducible integrability criterion. BJ 12.8 is the general-projective EP-to-surjectivity theorem with the actual attainment proof; its smooth corollary 12.9 is not substituted.
7. **Locality and uniqueness.** BJ 7.40--7.44 and 10.3--10.6 give genuine finite-energy strict-winning locality, comparison, equidimensional uniqueness and domination, without EP. Our irreducible target satisfies equidimensionality and connectedness.
8. **Continuous operator compatibility.** BE 7.14 and 8.3--8.5, 8.18--8.21 apply to projective schemes over complete valued fields, with actual rational bundles and fundamental-cycle multiplicities. Uniform same-bundle metrics, raw complete-field pushforward and model Deligne pairing compatibility supply Section 6. Their full pertinent statements and proofs are retained; BJ 7.23 identifies the same operator.

The source audit also retains Wu's entire v1 envelope proof, inclusive LF2697--2755 of the catalogue text. Its use of the fiber and weak/global gates is an observation about that proof, not an independent envelope premise. The granted contact proof's pertinent GR, GM, Ducros, CLD, Thuillier and GJR source units are retained in the catalogue evidence; their full source files are not claimed read. No Temkin correction from another continuation, finite-data novelty claim, unsupplied generated output, or independent-review conclusion is used.


END COMPLETE MATHEMATICAL BODY
END COMPLETE MATHEMATICAL BODY

BEGIN COMPLETE MATHEMATICAL BODY G1 RELATIVE GENERATION AND ONE NET ONLY
BEGIN COMPLETE MATHEMATICAL THEOREM GRANT: G1: Uniform actual relative multiplier-ideal generation and its single FS-net consequence; no general closure/energy/equation
\documentclass[10pt]{article}
\usepackage[a4paper,margin=26mm]{geometry}
\usepackage{amsmath,amssymb,amsthm,hyperref}
\newtheorem{theorem}{Theorem}
\newtheorem{lemma}{Lemma}
\newtheorem{corollary}{Corollary}
\newcommand{\FS}{\operatorname{FS}}
\newcommand{\J}{\mathcal J}
\newcommand{\OO}{\mathcal O}
\newcommand{\GG}{\mathbf G_m}
\title{Relative multiplier-ideal generation by compactification and field descent}
\author{An algebraic foundation for the big-class equation programme}
\date{6 October 2026}
\begin{document}
\maketitle
\begin{abstract}
We prove a uniform generation theorem for relative complete-system
asymptotic multiplier ideals on actual equivariant models of a big
rational bundle over every algebraically closed field of characteristic
zero. A single time twist makes the absolute complete systems restrict
to the exact relative base ideals in every degree. The resulting absolute
bundle is big. The complex projective multiplier-ideal theorem then
descends through a finitely generated field of definition, with one
generation twist for all degrees. This gives the actual decreasing
multiplier-ideal FS net without importing nonample decreasing closure.
The entire Monge--Amp\`ere equation and its inverse remain separate
proof obligations. No general-big compactness theorem is used here.
\end{abstract}

\paragraph{Actual data and conventions.}
Let $k$ be algebraically closed of characteristic zero, $X$ smooth
integral projective of dimension $n$, and $B$ an actual big rational
line bundle. Let
\[
 \pi:\mathcal X\longrightarrow X\times\mathbf P^1,
 \qquad p:\mathcal X\longrightarrow\mathbf P^1
\]
be a smooth equivariant projective modification, a product away from
time zero. We choose an actual linearized very ample bundle $H$ on
$\mathcal X$. Such a choice is available on the resolved equivariant
blowup models needed for rational model functions: the product has
linearized ample bundles, invariant blowup ideals give linearized
exceptional bundles, and sufficiently positive pullback powers tensored
with negative exceptional divisors are ample at each blowup. An ample
power is very ample. Equivariant characteristic-zero resolution can be
performed by invariant smooth centers. Thus this choice does not restrict
the rational model obstacles to toric or finitely generated series.

Write $F=p^*\{0\}=\sum b_EE$ and
$\mathcal B=\pi_X^*B+D$, where $D$ is an actual rational Cartier
divisor supported on $F$. Denominators are cleared in every section
system; all indices below are admissible positive integers. The
The associated rational model function is $f$. Throughout,
$\FS(B)$ denotes the full generically finite section-metric class,
allowing common zeros and supported $-\infty$ poles. Our time convention
is $\phi_F=1$. For an ideal $\mathfrak a$, write
$\phi_{\mathfrak a}=-v(\mathfrak a)$ on the normalized Gauss carrier,
with the usual value $-\infty$ at supported zeros. For its relative base
ideals $\mathfrak a_m$ on $\mathcal X_0=p^{-1}(\mathbf A^1)$ put
\[
 \mathfrak b_m=\J(\mathfrak a_\bullet^m)
   =\max_q\J(\mathfrak a_q^{\,m/q}).                    \tag{1}
\]
The maximum is over a cofinal divisibility sequence of sufficiently
large admissible $q$; it is a coherent ideal, not a formal infinite sum.

\begin{theorem}\label{uniform}
There is one actual linearized ample integral bundle $\mathcal C$ on
$\mathcal X$, independent of $m$, such that on $\mathcal X_0$
\[
 \mathfrak a_m\subset\mathfrak b_m,\qquad
 \mathfrak b_{m\ell}\subset\mathfrak b_m^\ell,\qquad
 (m\mathcal B+\mathcal C)\otimes\mathfrak b_m
       \text{ is generated by relative global sections}.          \tag{2}
\]
Here $m\ell$ is admissible and $\ell$ is a positive integer.
The bundle may be chosen with bounded model function $\phi_{\mathcal C}
\geq0$. Generation is by actual finitely many equivariant sections on
the affine time chart. All statements hold over the given field $k$,
without an embedding of $k$ in $\mathbf C$.
\end{theorem}

\section{One compactification twist identifies every base ideal}
After denominator clearing choose an integer $M$ with
$-MF\leq D\leq MF$. Set $V_m=H^0(X,mB)$ and let
\[
 \Lambda_m=H^0(\mathcal X_0,m\mathcal B)
       \subset V_m\otimes_k k[t,t^{-1}].
\]
Effective Cartier-divisor comparison gives
\[
 t^{mM}V_m\otimes k[t]\ \subset\ \Lambda_m
       \ \subset\ t^{-mM}V_m\otimes k[t].                \tag{3}
\]
Indeed the end terms are the sections of
$\pi_X^*(mB)\mp mMF$. Proper birational normality gives
$\pi_*\OO_{\mathcal X}=\OO_{X\times\mathbf P^1}$;
projection formula identifies their section modules exactly.
This is a statement about the true line bundles and their lattices.

Equivariance grades $\Lambda_m$ by the $t$ degree. The subspaces
$W_a=\{s\in V_m:t^as\in\Lambda_m\}$ form an increasing finite flag,
zero for $a<-mM$ and equal to $V_m$ for $a\geq mM$.
Choosing a basis adapted to this flag gives
\[
 \Lambda_m=\bigoplus_j t^{-w_{mj}}k[t]s_{mj},
                 \qquad -mM\leq w_{mj}\leq mM.           \tag{4}
\]
Every homogeneous lattice element is included by the flag construction,
and membership of a polynomial is membership of each homogeneous term.
Thus (4) does not presume finite generation of the whole section ring.

Fix a single integer $c>M$ and put
$P=\mathcal B+cF$. On the affine chart its section lattice is
$t^{-mc}\Lambda_m$. Each lowest-power generator
$t^{-(w_{mj}+mc)}s_{mj}$ extends across infinity, since there the
model is the product and $w_{mj}+mc\geq0$. More explicitly the absolute
global sections have the basis
\[
 t^{-(w_{mj}+mc)+r}s_{mj},
                 \qquad 0\leq r\leq w_{mj}+mc.           \tag{5}
\]
The upper bound expresses regularity at infinity. The lower bound
expresses membership of the lattice at zero. Restricting (5) to
$\mathcal X_0$ generates the entire relative lattice
$t^{-mc}\Lambda_m$ as a $k[t]$-module. Under the canonical local
bundle identification given by the frame $t^{-mc}$, its base ideal
is consequently exactly $\mathfrak a_m$:
\[
 \mathfrak a_m(P)|_{\mathcal X_0}=\mathfrak a_m.          \tag{6}
\]
No sections are discarded and no numerical-equivalence substitution
has been made.

Moreover (5) gives
\[
 h^0(\mathcal X,mP)
   =\sum_j(w_{mj}+mc+1)
   \geq\bigl(m(c-M)+1\bigr)h^0(X,mB).                  \tag{7}
\]
Because $B$ is big, its section growth along admissible degrees has
positive $m^n$ leading limsup. Equation (7) gives positive
$m^{n+1}$ growth, so $P$ is an actual big rational bundle on the
absolute smooth projective variety $\mathcal X$.

\section{The precise absolute complex theorem}
The ordinary multiplier-ideal input is the following projective
complex theorem, applied to an actual big bundle rather than a
nef substitute. On a smooth complex projective $d$-fold $Z$, for
an actual big integral bundle $L$ and a very ample bundle $H$,
\[
 \mathfrak a_m(L)\subset\J(\|mL\|),\qquad
 \J(\|m\ell L\|)\subset\J(\|mL\|)^\ell,                \tag{8}
\]
and
\[
 (mL+K_Z+(d+1)H)\otimes\J(\|mL\|)
                     \text{ is globally generated}.               \tag{9}
\]
For (8)'s first inclusion and (9), use Demailly--Ein--Lazarsfeld,
Theorem 1.8(i),(iii), with $L$ replaced by $mL$. For the second
inclusion use Variant 2.4 with $mL$ and exponent $\ell$.
These are absolute smooth complex projective assertions. Their proof
uses the asymptotic ideal's realization by one finite linear system,
Nadel vanishing and the Castelnuovo--Mumford generation lemma. They
do not assert the relative arbitrary-field theorem (2). We now prove
the passage needed for that theorem. For a rational $L$, first take
an integral multiple and rescale the admissible degrees.

\section{Finite-field descent, including asymptotic ideals}
All the finite data $(Z,L,H)$ descend to a finitely generated field
$F_0\subset k$ over $\mathbf Q$. Choose the projective embedding
defined by $H$ and include the finite coefficients of its equations,
the bundle presentations, and their isomorphisms in $F_0$. The
embedding and $H=\OO(1)|_Z$ then descend, preserving projectivity
and very ampleness. Smoothness descends along the faithfully flat
extension to $k$. An algebraic closure of $F_0$ embeds in $k$;
integrality descends from $Z_k$ to that algebraic closure, proving
geometric integrality. A finitely generated characteristic-zero
field embeds in $\mathbf C$: embed a finite transcendence basis as
algebraically independent complex numbers and extend over its finite
algebraic extension. We use $F_0\to\mathbf C$, never $k\to\mathbf C$.

For every field extension $F_0\subset F'$, flat cohomology base change
\cite{stacks} identifies $H^0(Z_{F'},qL)$ with
$H^0(Z_{F_0},qL)\otimes_{F_0}F'$. Hence complete-system evaluation
maps and base ideals commute with that extension. The same is true
of each fixed multiplier ideal. Indeed choose a characteristic-zero
log resolution $\mu:Y\to Z_{F_0}$ with
$\mathfrak a\OO_Y=\OO_Y(-G)$. The finite resolution formula is
\[
 \J(\mathfrak a^r)
    =\mu_*\OO_Y(K_{Y/Z}-\lfloor rG\rfloor).              \tag{10}
\]
After field extension the resolution is still smooth with geometric
simple normal crossings, the discrepancy and floor commute with
pullback, and proper pushforward commutes with flat base change.
This proves the claim. For a fixed $q$ and rational exponent, only
that one finite resolution is required.

The asymptotic operation also commutes with extension. To see this
without a uniform stabilization-degree assumption, write
$I_q=\J(\mathfrak a_q^{m/q})$. Graded multiplication gives
$I_q\subset I_{q\ell}$; the family is directed by common multiples.
The ascending chain condition on coherent ideals on the noetherian
quasicompact variety gives a unique maximum $I_{q_m}$. Its extension
contains every $I_q\otimes F'$ and is itself one such member.
It is therefore precisely the maximum after extension. Equivalently,
one may choose the maximizing degree after the complex extension:
faithful flatness descends each inclusion into that chosen member.
There is no need for the same $q_m$ to work for all $m$.

Apply (8)--(9) on $Z_{\mathbf C}$. Ideal inclusions descend by faithful
flatness. Global generation descends too: the evaluation map has
coherent cokernel, its source uses the just established $H^0$ base
change, and vanishing of its complex pullback forces that cokernel
to vanish. Then extend from $F_0$ to $k$. The same actual twist
$K_Z+(d+1)H$ works for every $m$ because the complex theorem uses
that fixed twist in every degree. Countably many separate finite
stabilizing indices do not require infinitely many coefficients
in the field of definition: all complete systems belong to the one
fixed descended bundle and commute with field extension.

\section{Restriction gives the actual relative theorem}
Apply the descended result to the big absolute bundle
$P=\mathcal B+cF$ from Section 1, with $d=n+1$.
Restriction to the open affine time chart commutes with (10).
Together with the exact base-ideal identification (6), it gives
\[
 \J(\|mP\|)|_{\mathcal X_0}
                      =\J(\mathfrak a_\bullet^m)=\mathfrak b_m.
                                                               \tag{11}
\]
Both sides are the maximum of the same restricted finite-degree
ideals. The global maximum is itself a restricted member and
dominates every other one, so no exchange with an unspecified
infinite sum is used. The inclusions in (2) follow from (8) and (11).

Put $\mathcal C_0=K_{\mathcal X}+(d+1)H$. Add $rH$, for one large
integer $r\geq0$, so that $\mathcal C_1=\mathcal C_0+rH$ is ample.
Since $rH$ is globally generated, tensoring (9) preserves global
generation. Finally add $qF$ for a sufficiently large integer $q\geq0$.
The bundle $qF=p^*\OO_{\mathbf P^1}(q)$ is globally generated and
nef; hence $\mathcal C=\mathcal C_1+qF$ remains ample and preserves
generation. All these bundles have actual linearizations. The generic
bundle $C=\mathcal C|_X$ is ample. Relative to the product identification
away from zero, $\phi_{\mathcal C_1}$ is a bounded rational model
function. Since adding $qF$ adds the scalar $q$, we choose $q$ so
$\phi_{\mathcal C}\geq0$.

Absolute generation of $(mP+\mathcal C)\J(\|mP\|)$ restricts to
relative generation of $(m\mathcal B+\mathcal C)\mathfrak b_m$:
the extra $mcF$ is removed by its canonical frame on the affine chart.
Its generating sections are actual relative sections, not fictitious
absolute sections of the untwisted bundle. The sheaf is equivariant.
Its proper pushforward to $\mathbf A^1$ is a finite graded module;
decomposing a finite set of generators into weight components supplies
finitely many homogeneous sections. They generate the same sheaf.
This completes the proof of Theorem~\ref{uniform}.

\section{The resulting single FS net}
The elementary all-point section-extension calculation gives
\[
 f_m=f+\frac1m\phi_{\mathfrak a_m}\in\FS(B),\qquad
 f_m\nearrow Q_B(f):=\sup\{u\in\FS(B):u\leq f\},        \tag{12}
\]
Here the membership assertion concerns degrees with $H^0(X,mB)\ne0$;
these contain a cofinal divisibility subset because $B$ is big. The
limit uses that subset, ordered by divisibility. The generation theorem
holds in every admissible degree. The two assertions use the actual
complete relative lattice: a weighted section below the model
obstacle extends on the normal model, and conversely extension
imposes that inequality. This is the algebraic calculation in
Boucksom--Jonsson's Addendum, Lemmas 1.5--1.7, before any invocation
of general decreasing closure. No general $P$-envelope identity is
being imported into (12).

Theorem~\ref{uniform} now supplies actual stages
\[
 \Psi_m=f+\frac1m\phi_{\mathfrak b_m}
                 +\frac1m\phi_{\mathcal C}
                  \in\FS(B+C/m).                       \tag{13}
\]
Their expression follows from the generated sheaf in (2), or its
resolved ideal: removal of the fixed ideal divisor gives the genuine
section system in the displayed actual bundle. Subadditivity and
$\phi_{\mathcal C}\geq0$ make (13) decrease in divisibility order.
For fixed $m$, (2) implies
$\mathfrak a_{m\ell}\subset\mathfrak b_m^\ell$ for every $\ell$;
using cofinal multiples in (12), we obtain
\[
 Q_B(f)\leq f+\frac1m\phi_{\mathfrak b_m}
           \leq\Psi_m\leq f+\frac1m\phi_{\mathcal C}.    \tag{14}
\]
A shifted nonzero section of a multiple of $B$ lies below the bounded
$f$, so $Q_B(f)$ has finite generic value. Therefore the endpoint of
this one decreasing net is generically finite. Its numerical classes
converge to $c_1(B)$. By the defining FS-net convention it is a genuine
psh function in that class, at every point of the original carrier.
This conclusion needs no theorem flattening a twice-closed family.

\paragraph{Exact scope and remaining original work.}
The algebraic theorem, including field descent and exact relative
generation, and its single FS-net consequence have passed independent
verification in their stated scope. The two section-class and nonempty-degree
clarifications above preserve that scope. It is designed to fill the first conditional input of
the relative-floor closure construction. That construction's closure,
compactness and full envelope identity are not granted by this paper.
Nor are the entire finite-energy operator, all continuous derivatives,
arbitrary-target attainment, comparison or uniqueness asserted here.
The zero-volume equation range is untouched. The original P16.5
completion count is unchanged.

\begin{thebibliography}{9}
\bibitem{DEL} J.-P. Demailly, L. Ein and R. Lazarsfeld,
\emph{A subadditivity property of multiplier ideals},
\href{https://arxiv.org/html/math/0002035v2}{arXiv:math/0002035v2},
Definition 1.7, Theorem 1.8 and Variant 2.4. Only their absolute smooth
complex projective statements are used before the descent proof.
\bibitem{addendum} S. Boucksom and M. Jonsson,
\emph{Addendum to global pluripotential theory over a trivially valued field},
\href{https://arxiv.org/pdf/2206.07183v2}{arXiv:2206.07183v2},
Lemmas 1.5--1.7: actual model/section/base-ideal calculation.
General nonample decreasing closure is not a premise.
\bibitem{stacks} The Stacks Project,
\href{https://stacks.math.columbia.edu/tag/02KH}{Lemma 30.5.2}:
flat cohomology base change for quasicompact quasiseparated morphisms.
Our structure morphisms and resolution morphisms are proper, the
sheaves are coherent, and every field extension is flat. Finite descent
uses the explicit projective and bundle presentations described above.
\end{thebibliography}
\end{document}

END COMPLETE MATHEMATICAL BODY
END COMPLETE MATHEMATICAL BODY

BEGIN COMPLETE MATHEMATICAL BODY WHOLE159
\documentclass[10pt]{article}
\usepackage[a4paper,margin=25mm]{geometry}
\usepackage{amsmath,amssymb,amsthm,mathrsfs,longtable,hyperref}
\emergencystretch=3em
\newtheorem{theorem}{Theorem}[section]
\newtheorem{lemma}[theorem]{Lemma}
\newtheorem{proposition}[theorem]{Proposition}
\newtheorem{corollary}[theorem]{Corollary}
\newcommand{\PSH}{\operatorname{PSH}}
\newcommand{\FS}{\operatorname{FS}}
\newcommand{\MA}{\operatorname{MA}}
\newcommand{\vol}{\operatorname{vol}}
\newcommand{\OO}{\mathcal O}
\newcommand{\E}{\mathcal E}
\newcommand{\an}{\mathrm{an}}
\newcommand{\dd}{dd^c}
\title{Absolute model estimates and a conditional attainment mechanism\\
\large A standalone incomplete paper for the unchanged original P16.5}
\author{Research draft from the two specified mathematical grants}
\date{6 October 2026}
\begin{document}
\maketitle
\begin{abstract}
We prove a raw finite-model absolute-value contraction, retaining all central
multiplicities, and compare the midpoint energy defect with the finite Hodge
distance. We independently reconstruct the uniform finite-model Taylor
estimate from full section lattices, positive deficient measures, and algebraic
volume differentiation. A smallness condition keeps both signed perturbations
inside the big cone. We then give a conditional original-carrier continuation
of the proposed arbitrary-target approximation: an absolute midpoint estimate,
transferred with the missing-rank error retained, rules out energy jumps at
model near-maximizers. Finite divisorial supporting planes suffice for actual
attainment, and divisorial probes give strict separation. This continuation
requires the explicitly listed genuine scalar, compactness, and moving-output
foundations; those foundations are not proved in their entirety here. Full
unbounded mixed independence and strict Borel comparison are also not proved.
Thus this paper does not solve original P16.5 and has canonical result
\texttt{candidate=false}. No zero mass is probability-normalized.
\end{abstract}

\section{Exact scope and mathematical authority}
Throughout the sought positive-volume domain is every algebraically closed,
trivially valued characteristic-zero field $k$, every smooth integral
projective $k$-variety $X$ of dimension $n\geq1$, and every actual big rational
line bundle $L\in\operatorname{Pic}(X)\otimes\mathbb Q$.
Write $K=X^\an$, $\theta=c_1(L)$, $V=\vol_X(L)>0$, and let $v_0$ denote
the generic trivial valuation. No countability, finite-generation, toric,
skeletal, or target-support restriction is added. All supported semivaluations
remain on the original compact Hausdorff carrier $K$. Canonical section norms
are at most one and are one at $v_0$ for each nonzero section.
An actual bundle identity is required for section multiplication; numerical
classes enter only ampleness and intersections. All rational tensor powers
and divisor coefficients are cleared before sections or ideals are used.

The only caller grants are the entire supplied G0, in its \emph{actual ample}
rational-bundle domain and exact retained field and geometric hypotheses,
and G1, in its exact resolved smooth equivariant relative-generation signature
and its \emph{one} generically finite FS net. We do not regard the other supplied
bodies or ledgers as premises. In particular the uniform variation calculation
below is a new reconstruction, whereas the scalar/moving package in
Section~\ref{package} is a list of unresolved antecedents. All uses of its
assertions are explicitly conditional.

Ordinary algebraic background consists of intersection theory on smooth
projective models, characteristic-zero equivariant principalization and SNC
resolution, nef positivity, Kodaira decomposition, high-power ample generation,
normal proper birational section descent, section-volume asymptotics, and the
ordinary algebraic positive-product and volume results of BFJ. These are not
nonample NA equation grants. Complete pertinent BFJ and finite BJ proof units
were retrieved independently; the source appendix gives literal coordinates.
We do not assert a recursive new proof of resolution, Fujita approximation,
or algebraic Hodge index.

The cone convention retained here is the literal single-net convention.
An FS scalar on an actual $B$ has the form
\[
 h=m^{-1}\max_j\{\log\|s_j\|_{\rm triv}+\lambda_j\},\qquad
 0\ne s_j\in H^0(X,mB),\quad\lambda_j\in\mathbb R.
\]
Common zeros and supported $-\infty$ poles are allowed. $\PSH(\theta)$
consists of all-point decreasing limits of \emph{one} such net on varying
actual bundles $B_i$ with $c_1(B_i)\to\theta$ and finite generic endpoint.
This definition alone does not give decreasing closure of a twice-closed
family. The intended reference is $R=P_\theta(0)$ and the intended energy is
the outer full-section energy specified in Section~\ref{package}. We never put
a polar physical section function into $\E^1$ merely by factoring its divisor.

One elementary embedding uses G0 without nonample closure: if $\Omega-L$ is
ample, a tail of a defining net has $\Omega-B_i$ ample. Tensor its sections
with a weight-zero generating system of a cleared power of that actual
difference. The scalar does not change, since a generator is a unit at the
center of every semivaluation. To make the stages finite, append generators
of $\Omega$ at weights $-mN$ and use the product net $\max(h_i,-N)$.
This is a genuine single decreasing ample net. G0 gives finite divisorial
values and all-point order determination for its endpoint. Thus for each
fixed rational divisorial $z$ there is a finite $C_z$ with
\begin{equation}\label{coordinate-bound}
 -C_z\leq u(z)\leq0
 \quad\text{for every normalized }u\in\PSH(\theta).
\end{equation}
Here normalization is $u(v_0)=\sup_Ku=0$. G0 compactness gives the bound
in the one actual ample cone. No equality of ample and big energies is used.
Rational divisorial scalings suffice for order determination: along a
divisorial ray $t\operatorname{ord}_E$, every defining FS stage is a finite
maximum of affine functions of $t>0$. Its decreasing endpoint is convex
and finite by the ample embedding, hence continuous on $(0,\infty)$.
An inequality on rational scalings therefore extends to all real scalings,
after which G0's divisorial order determination applies. This uses neither
countability of the field nor equality only on a skeletal carrier.

\section{Absolute-value contraction with every multiplicity}
Let $Y\to Z\times\mathbb P^1$ be a smooth SNC equivariant model, product
away from zero, with $\dim Z=n$. Write its full central fiber as
$F=\sum_i b_iE_i$, $b_i>0$. Let $N_1,\ldots,N_{n-1}$ be actual rational
relatively nef model bundles. For a vertical rational Cartier divisor
$D=\sum_i d_iE_i$, put $a_i=d_i/b_i$, and let $f_D$ be its scalar model
function. When $n=1$ the product of the $N_j$ is empty.
Denote $\Gamma=N_1\cdots N_{n-1}$.

\begin{lemma}[Graph identity]\label{graph}
With $c_{ij}=b_ib_j(E_iE_j\Gamma)$ for $i<j$, one has
\begin{equation}\label{graph-eq}
 -D^2\Gamma=\sum_{i<j}c_{ij}(a_i-a_j)^2,\qquad c_{ij}\geq0.
\end{equation}
For every rational continuous model function $f$,
\begin{equation}\label{abs-contract}
 \|\,|f|\,\|_\Gamma^2\leq\|f\|_\Gamma^2,
 \qquad\|f_D\|_\Gamma^2=-D^2\Gamma.
\end{equation}
The same contraction holds for a rational Lipschitz piecewise linear
function $P(f)$ of Lipschitz constant one, provided it is represented by
the corresponding resolved model function.
\end{lemma}
\begin{proof}
The line bundle $\OO(F)$ restricts trivially to each $E_i$. Hence
$\sum_j b_j(E_iE_j\Gamma)=0$ for every $i$. For $i\ne j$, $E_iE_j$ is
an effective SNC stratum, and the relatively nef $N_l$ restrict to nef
bundles on this projective vertical stratum. Thus its intersection is
nonnegative. Expanding $D^2\Gamma$, replacing its diagonal terms with
the preceding zero-row identities, and collecting unordered pairs proves
\eqref{graph-eq}. This derivation includes the diagonal coefficients,
the $b_i$, and every exceptional component.

Resolve the absolute value \emph{before} applying the graph identity.
Choose integral $q$ clearing $D$ and rational $C$ sufficiently large that
$q(CF+D)$ and $q(CF-D)$ are effective integral vertical Cartier divisors.
Principalize the invariant ideal
\[
 \OO(-q(CF+D))+\OO(-q(CF-D)).
\]
On a dominating SNC model it is $\OO(-G)$, and $CF-G/q$ represents
$|f_D|$: its semivaluative coefficient is
$C-\min(C+f_D,C-f_D)=|f_D|$.
The ideal is the unit ideal off the central fiber; no horizontal poles
are introduced. On every central component of this refined model the
normalized coefficient of the new divisor is precisely $|a_i|$ for the
pulled $D$. Pull back all $N_l$ and $F$, retaining their new central
multiplicities. Apply \eqref{graph-eq} on this model and use
$||a_i|-|a_j||\leq|a_i-a_j|$ term by term. Projection formula preserves
the old right quadratic form. This proves \eqref{abs-contract}.
The last assertion has exactly the same proof using
$|P(a_i)-P(a_j)|\leq|a_i-a_j|$ after resolving its rational maxima and
minima. No abstract chain rule or unspecified Dirichlet form is assumed.
\end{proof}

\section{Midpoint defect and a raw absolute moment}
On one actual nef rational generic bundle $A$ on a smooth projective
$n$-fold, let $\xi,\eta,\psi$ be bounded rational relatively nef model
scalars. Put $T_\xi=(A,\xi)$, $T_0=(A,0)$, $V_A=A^n$, and
\[
 e_A(\xi)=T_\xi^{n+1}/(n+1),\quad
 J_A(\xi)=\xi(v_0)V_A-e_A(\xi),\quad
 d_A(\xi,\eta)=\max_{0\leq j<n}
   \|\xi-\eta\|_{T_\xi^jT_\eta^{n-1-j}}^2.
\]
These are finite raw intersection quantities. Relatively nef model top
measures are positive with mass $V_A$ and coefficient
$b_E(T_\xi|_E)^n$ at $v_E=b_E^{-1}\operatorname{ord}_E|_{k(Z)}$.
They follow from G0 by a fixed-model ample perturbation and finite
polynomial passage, or from the finite intersection calculus directly.
No unbounded nef or big equation is invoked.

Two telescoping sums, with $S=(0,\xi-\eta)$, give
\begin{equation}\label{correct}
 T_\eta^{n+1}-T_\xi^{n+1}+(n+1)ST_\eta^n
 =-\sum_{j=0}^{n-1}(n-j)S^2T_\xi^jT_\eta^{n-1-j}.
\end{equation}
Indeed the term with index $j$ occurs in the inner telescoping sum for
$k=j+1,\ldots,n$. Consequently
\begin{equation}\label{J-formula}
 J_A(\xi)=\frac1{n+1}\sum_{j=0}^{n-1}(n-j)
       \|\xi\|_{T_\xi^jT_0^{n-1-j}}^2\asymp_n d_A(\xi,0).
\end{equation}
The orientation $j+1$ with these retained factors is not used.

\begin{lemma}[Midpoint defect]\label{midpoint}
For $\delta_A(\xi,\eta)=e_A((\xi+\eta)/2)
 -(e_A(\xi)+e_A(\eta))/2$, one has
\begin{equation}\label{midbound}
 \frac{n}{4^{n+1}}d_A(\xi,\eta)
 \leq\delta_A(\xi,\eta)\leq\frac n8d_A(\xi,\eta).
\end{equation}
\end{lemma}
\begin{proof}
Let $p(t)=e_A(\eta+t(\xi-\eta))$. Multilinearity gives
\[
 -p''(t)=n\sum_{j=0}^{n-1}\binom{n-1}{j}
          t^j(1-t)^{n-1-j}Q_j,\quad
 Q_j=\|\xi-\eta\|_{T_\xi^jT_\eta^{n-1-j}}^2\geq0.
\]
The one-dimensional Green formula for linear interpolation gives
$\delta_A=\int_0^1 k(t)(-p''(t))dt$ with
$k(t)=\min(t,1-t)/2$. Its integral is $1/8$, giving the upper bound.
On $[1/4,3/4]$, $k\geq1/8$ and each
$t^j(1-t)^{n-1-j}\geq4^{1-n}$. Every coefficient of $Q_j$ is therefore
at least $n/4^{n+1}$. This gives the lower bound for their maximum.
For $n=1$ the exact identity is $\delta_A=Q_0/8$.
\end{proof}

\begin{lemma}[Finite slot changes]\label{slots}
Writing $\beta=2^{1-n}$, one has for relatively nef model potentials
$\xi,\eta,\rho_1,\ldots,\rho_{n-1}$
\begin{equation}\label{slotbound}
 \|\xi-\eta\|_{T_{\rho_1}\cdots T_{\rho_{n-1}}}^2
 \leq C_n d_A(\xi,\eta)^\beta
       \max\{J_A(\xi),J_A(\eta),J_A(\rho_l)\}^{1-\beta}.
\end{equation}
\end{lemma}
\begin{proof}
We record the finite proof to specify its scope. Expanding the average
$\tau=(\xi+\eta)/2$ gives
$d_A(\xi,\eta)\asymp_n\|\xi-\eta\|_{T_\tau^{n-1}}^2$.
The tangent remainder in \eqref{correct}, divided by $n+1$, is
comparable to $d_A$ and is convex in its first potential by concavity
of the finite energy. Thus $d_A$ is quasi-convex in that potential.

Fix another potential $\rho$. Set $a=d_A(\xi,\eta)$,
$b=\max(d_A(\xi,\rho),d_A(\eta,\rho))$, $f=\xi-\eta$, and
$b_j=\|f\|_{T_\rho^jT_\tau^{n-1-j}}^2$.
The average formula gives $b_0\leq C_na$; the seminorm triangle
inequality gives $b_{n-1}\leq4b$.
Replacing one slot and writing $(0,f)=T_\xi-T_\eta$ gives
\[
 b_{j+1}-b_j=-(0,f)^2(0,\rho-\tau)
                       T_\rho^jT_\tau^{n-2-j}.
\]
Cauchy--Schwarz in the two nef products obtained from $T_\xi,T_\eta$,
and $T_\xi,T_\eta\leq2T_\tau$ in these quadratic forms, bound this
by $C_n\sqrt{b_jd_A(\tau,\rho)}\leq C'_n\sqrt{b_jb}$.
The quadratic forms are nonnegative by Lemma~\ref{graph}; hence their
polarizations satisfy Cauchy--Schwarz. If $a\leq b$, induction gives
$b_j\leq C_na^{2^{-j}}b^{1-2^{-j}}$. If $a>b$, use $b_{n-1}\leq4b$.
This proves the single repeated-slot estimate.

For a third potential $\zeta$, apply that estimate to both differences
$\xi-\zeta$ and $\zeta-\eta$ in the average $T_\tau^{n-1}$.
Quasi-convexity and the average formula yield
$d\leq C_nb^\beta\max(d,b)^{1-\beta}$, where
$d=d_A(\xi,\eta)$ and $b=\max(d_A(\xi,\zeta),d_A(\eta,\zeta))$.
If $d\geq b$ divide by $d^{1-\beta}$; otherwise the conclusion is
immediate. Thus $d_A$ satisfies a dimension-only quasi-triangle bound.
Average all the desired $\rho_l$. Expanding its $(n-1)$st power
dominates each nonnegative mixed quadratic form, and the repeated-slot
bound, quasi-convexity, quasi-triangle bound, and \eqref{J-formula}
give \eqref{slotbound}. When $n=1$, there is one empty-slot seminorm
and the assertion is immediate with $\beta=1$.
\end{proof}

\begin{theorem}[Absolute finite moment]\label{absolute-finite}
Set $\alpha=2^{-n}$ and
$B_* =\max(J_A(\xi),J_A(\eta),J_A(\psi))$.
Then
\begin{equation}\label{absolute-finite-eq}
 \int|\xi-\eta|\,d\MA_{A,\rm raw}(\psi)
 \leq |\xi(v_0)-\eta(v_0)|V_A
      +C_n\delta_A(\xi,\eta)^\alpha
         J_A(\psi)^{1/2}B_*^{1/2-\alpha}.
\end{equation}
This assertion includes $V_A=0$, with no division by volume.
\end{theorem}
\begin{proof}
Let $g=|\xi-\eta|$ and resolve it as in Lemma~\ref{graph}. Since the
trivial metric has measure $V_A\delta_{v_0}$, telescoping from $j=0$ gives
\[
 \int g\,d(\MA_A(\psi)-\MA_A(0))
  =\sum_{j=0}^{n-1}(0,g)(0,\psi)T_\psi^jT_0^{n-1-j}.
\]
Bound each term by Cauchy--Schwarz. The first seminorm is at most the
one for $\xi-\eta$ by \eqref{abs-contract}, and \eqref{slotbound}
controls it. The second is at most $C_nJ_A(\psi)^{1/2}$ by
\eqref{J-formula}. Use \eqref{midbound} and sum the $n$ terms.
This proves \eqref{absolute-finite-eq}. Constants have zero quadratic
form, so no normalization changes the estimate. If $V_A=0$, positivity
and mass force the top measure to be zero already. Zero-factor cases
are read by continuity; for $n=1$ the last factor has exponent zero
and is omitted.
\end{proof}

\section{Independent uniform finite-model variation}\label{variation-section}
In this section $L$ is any of the retained actual big rational bundles.
Let $Y\to X\times\mathbb P^1$ be a smooth equivariant modification,
product away from zero, $F=\sum b_EE$, and $D$ an actual vertical
rational Cartier divisor. Write $f=f_D$ and $d=n+1$.
The full relative section lattice, for $R_m=H^0(X,mL)$, is
\begin{equation}\label{lattice}
 \Lambda_m=\bigoplus_j t^{-w_{mj}}k[t]s_{mj},\qquad
 ma\leq w_{mj}\leq mb
\end{equation}
when $aF\leq D\leq bF$. Indeed divisor comparison gives
$t^{-ma}R_m[t]\subset\Lambda_m\subset t^{-mb}R_m[t]$;
equivariance grades this lattice and an adapted basis of its finite
homogeneous flag gives \eqref{lattice}. Proper normal birational section
descent retains the \emph{whole} original $R_m$. No finite generation
of the section ring is assumed. Gluing to the product lattice at infinity gives
\begin{equation}\label{dimformula}
 h^0(Y,m(\rho_X^*L+D+cF))
          =\sum_j\max(w_{mj}+mc+1,0).
\end{equation}
For sufficiently large rational $c$, this is $(mc+1)\dim R_m+\sum_jw_{mj}$.
Section-volume limits therefore give an intrinsic eventual intercept
\begin{equation}\label{intercept}
 \vol_Y(\rho_X^*L+D+cF)/d=cV+\mathscr E(f).
\end{equation}
The full-section lattice shows that $\mathscr E$ is invariant under
model refinement, monotone, $V$-translation equivariant, and
$V$-Lipschitz for the original sup norm. Ordinary volume-root concavity,
applied to \eqref{intercept} and expanded at $c\to\infty$, makes it
concave on rational model functions. It has a unique Lipschitz extension
to $C(K)$ by actual ample model density from G0.

BFJ volume differentiation on this \emph{big algebraic} $(n+1)$-fold gives,
for large $c$,
\begin{equation}\label{finite-mu}
 \mu_D=\sum_E b_E\langle(\rho_X^*L+D+cF)^n\rangle\cdot E\,\delta_{v_E},
 \quad \mu_D(K)=V,\quad D\mathscr E_f(h)=\int h\,d\mu_D.
\end{equation}
Every coefficient is nonnegative by the volume derivative in the effective
$E$ direction. Each is independent of sufficiently large $c$, by
differentiating \eqref{intercept} in $D+sE$ on a common eventual half-line.
The derivative in $F$ gives the mass. Refinement is compatible: an
effective exceptional prime $G$ has $p_*\OO(rG)=\OO$ for $r\geq0$;
adding it to a pulled bundle does not change sections. The derivative
coefficient there is zero. Projection and pullback retain the other
coefficients. Equivalently the original functional and its model
derivatives are unchanged. This constructs finite model measures, not
an unbounded original operator.

\begin{lemma}[Positive deficient measures]\label{deficient}
Suppose $f_D\leq0$ and $\mathscr E(f_D)\geq-B$, $B\geq0$.
For every $c>B/V$, the class $\alpha_D(c)=\rho_X^*L+D+cF$ is big, and
\begin{equation}\label{deficient-eq}
 0\leq\mu_{D,c}:=\sum_Eb_E\langle\alpha_D(c)^n\rangle\cdot E\,\delta_{v_E}
 \leq\mu_D,\qquad (\mu_D-\mu_{D,c})(K)\leq B/c.
\end{equation}
\end{lemma}
\begin{proof}
Set $g_D(c)=\vol(\alpha_D(c))/d$. Formula \eqref{dimformula} gives
a convex function of $c$, with $g_D(0)=0$, slope bounded by $V$,
eventual expression $cV+\mathscr E(f_D)$, and
$g_D(c)\geq cV+\mathscr E(f_D)$. For $c>B/V$ this is positive,
so the actual bundle is big. At that point BFJ differentiation gives
$g_D'(c)=\mu_{D,c}(K)$. Convexity gives
$g_D'(c)\geq g_D(c)/c\geq V-B/c$, and its eventual slope gives
$g_D'(c)\leq V$.

The coefficient assertion requires more than this mass bound. The full
filtered-space trace in \eqref{dimformula} gives
\[
 T_D(c):=\mathscr E(f_D)+cV-g_D(c)
       =\lim_m\frac{n!}{m^{n+1}}\sum_j\min(w_{mj}+mc,0).
\]
Terms arising from the $+1$ in \eqref{dimformula} tend to zero, since
$\dim R_m=O(m^n)$. Increasing an effective vertical divisor increases
each ordered weight of its full lattice: this follows from inclusion
of every filtration space, or its dimension distribution. Thus each
finite trace of the increasing function $\min(x+mc,0)$ increases.
The same is true of $T_D(c)$. Its derivative in each effective $E$
is nonnegative and equals the coefficient of $\mu_D-\mu_{D,c}$
divided by $b_E$. This proves coefficientwise positivity.
Together with the mass estimate it proves \eqref{deficient-eq}.
\end{proof}

\begin{theorem}[Uniform finite-model Taylor estimate]\label{taylor}
Fix a rational original model direction $h$, a cost bound $B$, and
$c>B/V$. There exist $K_c<\infty$ and $t_c>0$, independent of the
nonpositive obstacle $f_D$ and of its refinement, such that
\begin{equation}\label{taylor-eq}
 |\mathscr E(f_D+th)-\mathscr E(f_D)-t\int h\,d\mu_D|
 \leq K_ct^2/2+|t|\|h\|_\infty(2B+2V\|h\|_\infty)/c
\end{equation}
whenever $\mathscr E(f_D)\geq-B$ and $|t|<t_c$.
\end{theorem}
\begin{proof}
Represent $h$ by a signed vertical Cartier $H$ on one fixed smooth
determination $Z$. Choose an actual ample $T$ there, and refine to carry
each $D$, always pulling $T,H$ back. Let
$\gamma=\rho_X^*L+cF$, $\alpha=\alpha_D(c)$,
$\kappa=d(cV-B)>0$, and $M=d\langle\gamma^n\rangle\cdot T$.
We have $\alpha\leq\gamma$ in psef order and $\vol(\alpha)\geq\kappa$.
While $\alpha-rT$ stays big, volume differentiation and positive-product
monotonicity bound its volume loss by $rM$. Thus
$\alpha-r_0T$ is big for $r_0=\kappa/[2(M+1)]$: a first earlier exit
would contradict volume continuity and the remaining positive volume.
The constants are unchanged under refinement, since their tests live on $Z$.

Choose $a>0$ with $aT\pm H$ nef and put $\lambda=a/r_0$.
Then $\lambda\alpha\pm H$ are psef. For $|s|\lambda<1/2$, positivity
and monotonicity sandwich
\[
 (1-\lambda|s|)^n\langle\alpha^n\rangle
 \leq\langle(\alpha+sH)^n\rangle
 \leq(1+\lambda|s|)^n\langle\alpha^n\rangle.
\]
To pair with $H$, decompose it into the \emph{two fixed nef tests}
$H_1=aT+H$, $H_2=aT$. Their pairings are bounded by
$\langle\gamma^n\rangle\cdot H_l$, fixed before the model varies.
The sandwich implies a common Lipschitz bound on the derivative of
$\vol(\alpha+sH)/d$. Integrating gives
\[
 |g_{D+tH}(c)-g_D(c)-t\int h\,d\mu_{D,c}|\leq K_ct^2/2.
\]
No signed test is inserted into an effective-order inequality.

Put $H_0=\|h\|_\infty$. At parameter $s$, use the nonpositive obstacle
$f_D+sh-|s|H_0$ and time parameter $c_s=c+|s|H_0$. Its cost is at
most $B_s=B+2V|s|H_0$, by the actual Lipschitz and constant laws.
Crucially choose $t_c\leq1$ and, if $H_0>0$,
$t_c<(c-B/V)/(2H_0)$. Then $c_s>B_s/V$ for both signs throughout
the integration path. The rough fixed bound $B+2VH_0$ alone would
not justify this big-cone condition when $c$ is near $B/V$.
Its deficient class is exactly $\alpha+sH$. Its full derivative measure
is unchanged by the scalar shift. Lemma~\ref{deficient} bounds the
positive derivative tail by $B_s/c_s\leq(B+2VH_0)/c$.
Integrate the $h$-derivative along this path and replace the initial
deficient derivative by $\mu_D$, at extra cost $|t|H_0B/c$.
The resulting sum is \eqref{taylor-eq}. The finite-model energy is $C^1$
on the path, since one sufficiently large time twist realizes its
intercept in a common neighborhood of actual big classes. This proves
the integration for both signs. When $H_0=0$ there is nothing to prove.
\end{proof}

Theorem~\ref{taylor} verifies the \emph{finite-model} variation ingredient.
It does not itself construct the scalar outer energy on every genuine base,
prove its envelope identity, construct a weakly continuous unbounded output,
or identify weighted moving products. Those distinctions are retained next.

\section{Explicit unresolved original-carrier antecedents}\label{package}
The rest of the positive-volume conclusions are conditional on the following
package S--M. It is stated for the \emph{entire} retained domain of Section 1,
with the literal single-net cone; no narrower space is substituted.
We do not claim to have proved the entire package independently.
\begin{enumerate}
\item[S1.] That cone is convex, finite-max closed and decreasing closed at
finite generic endpoints. Its normalized space is compact in the topology
of pointwise convergence at rational divisorial valuations. Each upper
bounded usc obstacle with a genuine generically finite minorant has a
genuine all-point envelope. The minimal reference is $R=P_\theta(0)$,
$R(v_0)=0$, and every normalized genuine $u$ satisfies $u\leq R\leq0$.
\item[S2.] The scalar energy on the \emph{whole} genuine cone is
\[
 E(u)=\inf_{f\in C(K),\ f\geq u}\mathscr E(f),\quad
 \E^1_\theta=\{u\in\PSH(\theta):E(u)>-\infty\},\quad B(u)=-E(u)
\]
for normalized $u$. It is concave, monotone, weakly usc, decreasing-net
continuous, has $E(R)=0$ and $E(u+c)=E(u)+cV$, and satisfies
$E(P_\theta(f))=\mathscr E(f)$ for continuous obstacles. Every normalized
$u\in\E^1_\theta$ has decreasing nonpositive rational model majorants
$f_i\downarrow u$ with $f_i(v_0)=0$, whose envelopes $a_i=P_\theta(f_i)$
decrease all-point to $u$ and whose energies decrease to $E(u)$.
For fixed $h\in C(K)$, their perturbed envelopes decrease to
$P_\theta(u+th)$ at each fixed $t$. Outer energy on usc obstacles equals
the energy of this envelope. Its continuous-obstacle value is the
full-section trace constructed from $W_m(f;s)$ below.
\item[S3.] There is an actual Kodaira identity $L=aA+E_0$ with $a>0$,
$A$ ample and $E_0\geq0$. Write $Z=E_0^\an$, $U=K\setminus Z$.
There is a normalized actual $w_Z\in\E^1_\theta$ with $w_Z=-\infty$
on $Z$. Genuine relative contraction holds with a dimension constant
$C_0\geq1$:
\[
 B((1-r)R+ru)\leq C_0r^2B(u),\qquad 0<r<1.
\]
\item[M1.] A target-independent map $M$ on every actual $\E^1_\theta$
has positive original Radon outputs of raw mass $V$, constant invariance,
and $M(P_\theta(f_D))=\mu_D$ from \eqref{finite-mu}.
For the canonical majorants in S2, $M(a_i)\to M(u)$ weakly on $K$.
Every such output gives $Z$ zero mass. The map is not defined using an
inverse target construction.
\item[M2.] For any fixed finite list of normalized nonpositive rational
model obstacles, resolve the \emph{full} $|mL|$ system and their full
relative lattices on common smooth equivariant models. One has the
actual generic identity $p_m^*L=A_m+T_m$, with $mA_m$ generated,
$mT_m$ effective, and bounded relatively nef model scalars $\psi_{m,D}$
on this \emph{same actual} $A_m$, such that
\[
 \phi_{m,D}=q_{T_m}+\psi_{m,D},\quad\phi_{m,0}=q_{T_m},\quad
 A_m^n\to V,\quad e_{A_m}(\psi_{m,D})\to E(P_\theta(f_D)),\quad
 \psi_{m,D}(v_0)\to0.
\]
These full complete-system stages are minorants of their original
envelopes. Their pushed auxiliary raw top measures converge to $\mu_D$.
All degree limits are cofinal divisibility limits with nonempty systems.
The auxiliary bounded nef trace agrees with the finite intersection
energy $e_{A_m}$. Multiplication by $s_{\ell T_m}$ injects
$H^0(X_m,\ell A_m)$ into the \emph{full original} $H^0(X,\ell L)$
in cleared degrees. No assertion of original $\E^1$ membership is made
for the physical functions $q_{T_m}+\psi_{m,D}$.
\end{enumerate}
Here M2 is only a finite-list, finite-obstacle compatibility assertion.
It does not assume an unbounded mixed product, arbitrary approximation
independence, attainment, comparison, whole supporting planes, or separation.
Theorem~\ref{taylor} supplies its finite variation ingredient; no further
uniform Taylor hypothesis is hidden in S--M.

The supplied scalar constructions and moving-product arguments suggest
S--M, but checking all their antecedents and unbounded passages is separate
work. In particular G1 alone does not grant S1, and G0 does not grant M1
on a big nonnef class. The conditional theorem below will show exactly
what follows if this package is established.

\section{Independent bounded-obstacle density and directed integration}
The density result in this section requires only the single-net definition,
genuine obstacle envelopes from S1, and ordinary Kodaira/ample background.
It reconstructs the bounded ingredient of the supplied ROOT198 bridge.
Let $W=q_{E_0}\leq0$. It is finite continuous on $U$, and tensoring its
single section with a weight-zero generating system of $aA$ realizes it
as an actual FS scalar on $L$.

For $f\in C(K)$ and nonzero $s\in H^0(X,mL)$ put
\[
 W_m(f;s)=\inf_K(mf-\log\|s\|),
 \qquad
 \phi_{m,f}=m^{-1}\max_j(\log\|s_{mj}\|+\lfloor W_m(f;s_{mj})\rfloor).
\]
At a section zero the bracket is $+\infty$. Its bounds are
$m\min f\leq W_m(f;s)\leq m f(v_0)$. Superlevel subspaces of the
full section space form a finite closed-endpoint flag; choose an adapted
basis. The ultrametric inequality over trivial $k$ makes $\phi_{m,f}$
basis independent. Powers of sections and superadditivity of weights
make these stages increase in divisibility order. In the model case
they are exactly the complete relative-lattice stages by the all-point
section-extension calculation in G1. Real FS weights are dominated in
the supremum: raising a degree-$r$ section to its $\ell$th power loses
less than $1/(r\ell)$ upon flooring its weight.

\begin{lemma}[Actual bounded density]\label{density}
If $u_f=P_\theta(f)$ is genuine, then
\[
 u_f=\sup_m\phi_{m,f}\quad\text{on }U.
\]
This envelope is finite continuous on $U$ and the stages converge
uniformly on each compact subset of $U$. For $|f|\leq C$, the relative
function $u_f-R$ is bounded by $C$ on $U$.
\end{lemma}
\begin{proof}
Take $C$ a positive integer with $|f|\leq C$. The genuine minorant
$W-C$ makes $u_f$ finite on $U$. Given a defining net $h_i\downarrow u_f$
on actual $B_i$, fix rational $0<t<1$ and $\epsilon>0$ \emph{before}
taking a tail. The actual difference
\[
 L-(1-t)B_i-t(L-aA)
\]
is eventually ample, since its numerical class tends to $ta[A]$.
Compactness of the nested closed sets $\{h_i\geq f+\epsilon\}$ gives
a tail with $h_i<f+\epsilon$ on \emph{all} of $K$, including supported
poles. Tensor with a generated system of that actual ample difference.
The scalar $(1-t)(h_i-\epsilon)+t(W-C)$ is then an actual FS function
on $L$ below $f$ everywhere. At $x\in U$, let $i$ tend to its endpoint,
then $t\downarrow0$, then $\epsilon\downarrow0$. Full-system domination
including the real-weight flooring observation proves the reverse
inequality $u_f\leq\sup_m\phi_{m,f}$. The other inequality follows
because each stage is a genuine minorant.

One cleared Kodaira-section tensor degree has no common zeros on $U$.
For all its multiples the stages are finite continuous there; their
supremum is lsc, while the genuine envelope is usc. Thus equality makes
it continuous. On a fixed compact subset the decreasing continuous gaps
to this envelope have empty positive-margin superlevel intersections.
Compactness yields uniform convergence for the divisibility-directed
stages. Finally constant shifts and envelope order give
$R-C\leq u_f\leq R+C$ on $U$. No equality on $Z$ is asserted.
\end{proof}

\begin{lemma}[Bounded weighted passage]\label{bounded-passage}
If positive Radon measures $\sigma_i\to\sigma$ weakly on $K$ with
converging masses, $\sigma(Z)=0$, and $b$ is bounded continuous on $U$,
then its bounded extension by zero on $Z$ has converging integrals.
The same holds for bounded changing section quotients which converge
uniformly to $b$ on every compact subset of $U$.
\end{lemma}
\begin{proof}
Choose a compact $F\subset U$ with arbitrarily small omitted $\sigma$
mass. By compact Hausdorff normality choose a continuous $0\leq\chi\leq1$,
equal to one on $F$ with compact support in $U$. The product $\chi b$
extends continuously by zero on $K$. Pass that fixed continuous integral
through weak convergence. Bound each omitted part by the common bound
times $\sigma_i(K)-\int\chi d\sigma_i$, which tends to its arbitrarily
small limiting value. For changing quotients first fix this collar,
then their uniform error on its support, and only then take the index.
This proves the claim without indicators of changing Borel sets or
uniform convergence at polar points.
\end{proof}

\begin{lemma}[Radon finite-cover lemma]\label{radon}
Let $c_i\geq0$ be a directed increasing net of continuous functions on
$U$, and let $\nu$ be finite Radon on $K$ with $\nu(Z)=0$.
Then $\int_U\sup_i c_i\,d\nu=\sup_i\int_U c_i\,d\nu$,
allowing $+\infty$.
\end{lemma}
\begin{proof}
For $a>0$, the open set $\{\sup_i c_i>a\}$ is the union of the open
superlevels of the $c_i$. Each compact subset has a finite subcover;
directedness gives one index dominating that finite set. Radon inner
regularity identifies the superlevel mass with the supremum of these
masses. Finitely many threshold masses can be approached simultaneously
by a common index. Use finite lower layer-cake step sums for the cap
$\min(\sup_i c_i,N)$, refine the threshold mesh, then let $N\to\infty$.
The reverse inequality follows from pointwise order. This proves the
net integral assertion; measurable monotone convergence for arbitrary
uncountable nets was not used.
\end{proof}

\section{Reconstruction of arbitrary-target output approximation}\label{target-approx}
For a normalized actual $u\in\E^1_\theta$, all differences below are
taken where $R$ is finite. An intrinsic target is a positive original
Radon measure $\nu$ with
\begin{equation}\label{target}
 \begin{aligned}
 &\nu(K)=V,\qquad\nu\{R=-\infty\}=0,\\
 &I_\nu(u)=\int(R-u)d\nu<\infty\quad\text{for every actual }u\in\E^1_\theta,\\
 &D_\nu=\sup_{u(v_0)=0}\{E(u)+I_\nu(u)\}<\infty.
 \end{aligned}
\end{equation}
The redundant integrability clause is displayed to retain every actual
test: finite dual energy directly forces each integral to be finite.
No absolute integrability of $R$ is imposed. S3 and $w_Z$ give
$\nu(Z)=0$, since its relative cost is infinite on $Z$ outside the
already excluded reference poles. These are intrinsic targets of the
specified reference, not a support-restricted class.

\begin{proposition}[Same fixed increment at every genuine base]\label{fixed-increment}
Under S--M, \eqref{taylor-eq} holds with its same constants at every
normalized genuine $u$ of cost at most $B$, replacing its left side by
\[
 |E(P_\theta(u+th))-E(u)-t\int h\,dM(u)|.
\]
Both derivative signs exist for every original $h\in C(K)$ and equal
$\int h\,dM(u)$.
\end{proposition}
\begin{proof}
Apply Theorem~\ref{taylor} to the S2 model majorants $f_i$. Their
envelope costs are at most $B$. At fixed $t$, the perturbed envelopes
and their energies decrease to those of $P_\theta(u+th)$, and M1
passes the fixed continuous $h$ integral. Thus the whole finite
increment estimate passes with unchanged constants. There is no
exchange of a derivative with a net. Divide by $t$ with both signs,
first let $t\to0$ at fixed $c>B/V$, then $c\to\infty$.
Uniform model approximation of any original continuous $h$ changes
the divided energy increment and the measure integral by at most
$V$ times its sup-norm error. Fix the approximation before $t\to0$,
then let this error tend to zero. This proves both continuous signs.
\end{proof}

\begin{proposition}[Output approximation before attainment]\label{output-approx}
Under S--M, every target \eqref{target} has normalized model-envelope
near-maximizers $u_k$ with
\[
 E(u_k)+I_\nu(u_k)\geq D_\nu-1/k,\quad
 B(u_k)\leq Q_\nu:=4C_0D_\nu+2,\quad M(u_k)\to\nu\text{ weakly}.
\]
\end{proposition}
\begin{proof}
For the actual majorants $a_i$ of any $u$, the costs $R-a_i$ are
nonnegative bounded continuous on $U$ by Lemma~\ref{density}, increase
to $R-u$, and have finite $\nu$ integral. Lemma~\ref{radon} and S2
show convergence of the objective. Its supremum over model envelopes
is therefore exactly $D_\nu$. Choose a sequence within $1/k$ of that
real supremum; this does not impose metrizability on $K$.

Reference contraction gives
$rI_\nu(u)-C_0r^2B(u)\leq D_\nu$. At $r=1/(2C_0)$ it gives
$I_\nu(u)\leq B(u)/2+2C_0D_\nu$. The near-maximizer lower bound
then gives $B(u_k)\leq Q_\nu$.

For a fixed rational model $h$, perturb the \emph{actual base}
$u_k+th$, not its larger physical model obstacle. Its envelope $z_{k,t}$
lies between $u_k\pm|t|\|h\|_\infty$ and is actual finite energy by S2.
The obstacle inequality gives
$I_\nu(z_{k,t})\geq I_\nu(u_k)-t\int h\,d\nu$.
Normalize it only when using \eqref{target}; the raw constant law and
mass keep the objective unchanged. Near maximality implies
\[
 E(z_{k,t})-E(u_k)-t\int h\,d\nu\leq1/k.
\]
Proposition~\ref{fixed-increment} at bound $Q_\nu$, with both signs,
gives for $0<t<t_c$
\[
 \left|\int h\,d(M(u_k)-\nu)\right|
 \leq \frac1{kt}+K_ct/2+
           \|h\|_\infty(2Q_\nu+2V\|h\|_\infty)/c.
\]
Send $k\to\infty$ at fixed $c,t$, then $t\downarrow0$ at that $c$,
then $c\to\infty$. Uniform model density and the common raw mass
extend convergence to every continuous test. This independently
reconstructs the conditional ROOT199 bridge, before attainment.
\end{proof}

\section{Midpoint transfer with the lost-volume error retained}\label{transfer}
For normalized genuine $a,b$ define the scalar midpoint defect
\[
 \delta(a,b)=E((a+b)/2)-(E(a)+E(b))/2\geq0.
\]
The central new original-carrier assertion of this paper is the following
\emph{conditional} absolute estimate.

\begin{theorem}[Absolute midpoint modulus]\label{absolute-original}
Assume S--M. For any normalized $a,b,w\in\E^1_\theta$,
\begin{equation}\label{modulus-output}
 \int_U|a-b|\,dM(w)
 \leq C_n\delta(a,b)^\alpha B(w)^{1/2}
           \max\{B(a),B(b),B(w)\}^{1/2-\alpha},\quad \alpha=2^{-n}.
\end{equation}
Every genuine relative test is integrable for $M(w)$, and these outputs
have finite intrinsic dual energy. For any target \eqref{target},
\begin{equation}\label{modulus-target}
 \int_U|a-b|\,d\nu
 \leq C_n\delta(a,b)^\alpha Q_\nu^{1/2}
          \max\{B(a),B(b),Q_\nu\}^{1/2-\alpha}.
\end{equation}
All these integrals use original actual functions and relative values.
For unbounded pairs the absolute difference is defined where both relative
costs are finite, which has full measure by the integrability proof below
(or by the target condition), and assigned zero on its null complement.
No subtraction of two infinite values is made.
\end{theorem}
\begin{proof}
First fix normalized model envelopes $a=P(f_H)$, $b=P(f_J)$,
$w=P(f_D)$. Use M2's common moving $A_m,T_m$ and set
$\xi_m=\psi_{m,H}$, $\eta_m=\psi_{m,J}$, $\psi_m=\psi_{m,D}$.
The finite endpoint energies and generic values have the stipulated
limits. We need only an \emph{upper} bound for the midpoint auxiliary
energy; its equality to the original midpoint energy is not presumed.

Fix one finite original continuous $f\geq(a+b)/2$. The literal section
minorants give on the entire pulled carrier
\[
 q_{T_m}+(\xi_m+\eta_m)/2\leq(a+b)/2\leq f.
\]
For this fixed $m$, inject the full auxiliary $H^0(\ell A_m)$ via
$s_{\ell T_m}$ into the full original $H^0(\ell L)$.
Every injected section has original $f$-weight at least its auxiliary
midpoint-metric weight: cancel the actual section factor where finite,
and note that its zero branches have original weight expression
$+\infty$ and cannot lower the infimum. Analytic surjectivity identifies
the original infimum with the infimum on all lifts. All remaining
original weights are at least $\ell\min_Kf$, since canonical section
norms are at most one. Extend an adapted subspace basis to a full
adapted basis; the quotient weights have this lower bound.

Take $\ell\to\infty$ with $m,f$ fixed. Full section asymptotics and the
finite auxiliary nef trace from M2 give exactly
\begin{equation}\label{trace-error}
 \mathscr E(f)\geq
 e_{A_m}((\xi_m+\eta_m)/2)+(\min_Kf)(V-A_m^n).
\end{equation}
The rounding error is bounded by the ranks and disappears at this
first degree limit. The last term is generally negative and has not
been discarded at finite $m$. Now let $m\to\infty$; only for this
\emph{fixed finite} $f$ does the term vanish. Finally take the outer
infimum over $f$. Thus
\[
 \limsup_m\delta_{A_m}(\xi_m,\eta_m)\leq\delta(a,b).
\]
This uses no original $\E^1$ membership of a physical complete-system
function and no equality of its energy with an auxiliary energy.

Theorem~\ref{absolute-finite} now bounds the integrals of
$|\xi_m-\eta_m|$ against the auxiliary raw output of $\psi_m$.
Its generic error $|\xi_m(v_0)-\eta_m(v_0)|A_m^n$ tends to zero
\emph{after} this finite estimate; all $J$ factors tend to $B(a),B(b),B(w)$.
At the pushed function-field divisorial atoms, that test is exactly
$|\phi_{m,H}-\phi_{m,J}|$. On $U$ these quotients converge uniformly
on compact sets to $|a-b|$, by Lemma~\ref{density}; their global
support values have a fixed bound from time-lattice comparison.
Indeed the full weights for $f_H$ and $f_J$ differ by at most
$m\|f_H-f_J\|_\infty$, up to a rounding error of one.
Lemma~\ref{bounded-passage}, with limiting finite divisorial $\mu_D$
which misses $Z$, identifies the full limiting integral. This proves
\eqref{modulus-output} for model pairs at model outputs.

For a fixed model pair $a,b$, its absolute difference is bounded
continuous on $U$. Apply Lemma~\ref{bounded-passage} along canonical
model outputs of an arbitrary $w$, using M1 and their bounded costs,
to obtain \eqref{modulus-output} for this pair at $M(w)$.
Apply it instead along Proposition~\ref{output-approx} to obtain
\eqref{modulus-target} for each fixed model pair. This requires only
bounded relative integration off the actual divisor, not optional
unbounded approximants or a changing test against $\nu$.

We next justify all unbounded tests. Take $a=R$ and a decreasing
normalized model-majorant envelope $b_j$ of $v\in\E^1_\theta$.
Since $v\leq b_j\leq R$, monotonicity gives
$\delta(R,b_j)\leq B(b_j)/2\leq B(v)/2$.
The model-pair estimate uniformly bounds $\int(R-b_j)dM(w)$ by
\[
 C_n B(v)^\alpha B(w)^{1/2}\max\{B(v),B(w)\}^{1/2-\alpha}.
\]
These nonnegative continuous costs on $U$ increase to $R-v$.
Lemma~\ref{radon} therefore proves its actual integrability at the
fixed output. In particular the model majorants converge in its
relative $L^1$. The same directed integral argument works at a
target by its prescribed integrability.
For two arbitrary tests $a,b$, pass their two model-majorant nets
separately in $L^1$ at the fixed measure; their midpoint energies
decrease by S2. The absolute-value error is bounded by the sum of
those two $L^1$ errors. This proves both full estimates.

The reference-pole set is contained in $Z$, since $R\geq W$.
Outputs already give $Z$ zero mass. To check finite intrinsic dual
energy, use the displayed moment bound. If $B(v)\geq B(w)$ it is at
most $C_n\sqrt{B(v)B(w)}$; if $B(v)<B(w)$ it is at most $C_nB(w)$.
Subtracting $B(v)$ gives a finite supremum, of size at most a
dimension constant times $B(w)$. This verifies the target condition
for outputs without an inverse definition.
\end{proof}

The argument also reconstructs the optional fixed-test part of ROOT199,
but its hypotheses should be kept explicit. If $b=R-v$ on $U$, extended
by zero on $Z$, then $b$ is nonnegative lsc on $K$.
If actual $a_\eta\in C(K)$ satisfy $0\leq a_\eta\leq b$ and
$\sup_k\int(b-a_\eta)dM(u_k)<\eta$, the nonnegative lsc Portmanteau
inequality gives $\int(b-a_\eta)d\nu\leq\eta$.
Fixed continuous integrals then pass, giving fixed-test weighted convergence.
On compact Hausdorff $K$, this Portmanteau inequality follows by approximating
nonnegative lsc functions from below by continuous functions, using Radon
inner regularity of their open superlevels. It holds for nets.
The existence of these below-approximants is an additional assumption in
that optional argument; the observation alone does not prove it.
Our midpoint proof below does not assume those approximants.

\section{Actual conditional attainment, excluding the energy jump}
We first establish precisely the finite supporting planes used in the proof.

\begin{lemma}[Finite whole planes]\label{finite-plane}
Under S--M, if $a=P_\theta(f_D)$ is a model envelope, then for every
actual $v\in\E^1_\theta$
\begin{equation}\label{plane}
 E(v)\leq E(a)+\int(v-a)d\mu_D.
\end{equation}
This is a finite divisorial integral and is finite for every actual test.
\end{lemma}
\begin{proof}
Concavity and the finite derivative in \eqref{finite-mu} give a plane
at $f_D$ for every continuous obstacle. Uniform model approximation
extends this continuous-obstacle plane to $C(K)$.
Take decreasing continuous majorants of $v$ and pass their values
on the fixed finite divisorial support; G0's actual ample embedding
ensures all of these limiting divisorial values are finite.
S2 passes the outer energies. Thus
$E(v)\leq\mathscr E(f_D)+\int(v-f_D)d\mu_D$.
At $v=a$, S2 gives equality of the two energies, while $a\leq f_D$.
Hence the nonnegative contact integral $\int(f_D-a)d\mu_D$ is zero.
Replacing $f_D$ by $a$ in the plane proves \eqref{plane}.
No passage at nonalgebraic poles occurs at this finite support.
\end{proof}

\begin{theorem}[Conditional attained equation for the outer map]\label{attainment}
Assume S--M for the entire retained big domain. Then every target
\eqref{target} has an actual normalized maximizing $u\in\E^1_\theta$
on $K$, and $M(u)=\nu$. In particular no abstract completion or lift
on a modification replaces the solution. This theorem is conditional
on S--M and does not identify $M$ with every required mixed operator.
\end{theorem}
\begin{proof}
Use Proposition~\ref{output-approx} and put $\epsilon_k=1/k$,
$F_\nu(v)=E(v)+I_\nu(v)$.
Linearity of actual target relative integrals on convex combinations gives
\begin{equation}\label{near-mid}
 0\leq\delta(u_i,u_j)
 =F_\nu((u_i+u_j)/2)-(F_\nu(u_i)+F_\nu(u_j))/2
 \leq(\epsilon_i+\epsilon_j)/2.
\end{equation}
For each rational divisorial $z$, the raw target $V\delta_z$ is
intrinsic: it misses reference poles, every genuine test is finite
there by \eqref{coordinate-bound}, and its normalized relative integral
is at most $VC_z$, so its dual energy is finite. This conclusion
uses no Dirac inverse equation. Applying \eqref{modulus-target}
to this target shows that $u_k(z)$ is Cauchy.
S1 compactness and all-point divisorial determination therefore give
one actual normalized weak limit $u$ for the whole sequence. S2
upper semicontinuity and the cost bound give $E(u)\geq-Q_\nu$,
so the limit is genuinely in $\E^1_\theta$.

The finite planes and \eqref{modulus-output} give
\[
 |E(u_i)-E(u_j)|\leq
 \max_{l=i,j}\int|u_i-u_j|dM(u_l)
 \leq C_{n,Q_\nu}(\epsilon_i+\epsilon_j)^\alpha.
\]
Hence these energies have a real limit $e$ and $E(u)\geq e$.
An energy jump is excluded by a \emph{fixed finite} plane.
For fixed $i$, $M(u_i)=\mu_i$ has finite divisorial support. Weak
convergence of the potentials on that support gives
\[
 \int|u-u_i|d\mu_i
   =\lim_j\int|u_j-u_i|d\mu_i
   \leq C_{n,Q_\nu}\epsilon_i^\alpha.
\]
Lemma~\ref{finite-plane} now gives
$E(u)\leq E(u_i)+C_{n,Q_\nu}\epsilon_i^\alpha$.
Let $i\to\infty$. Thus $E(u)=e$. The direction of this inequality
is the missing direction that compactness and energy usc alone cannot give.

The midpoints $(u_i+u)/2$ converge weakly to $u$. Concavity gives
their energy lower bound tending to $E(u)$; energy usc gives the matching
upper bound. Therefore $\delta(u_i,u)\to0$.
The full target modulus \eqref{modulus-target} yields
$\int|u_i-u|d\nu\to0$. The varying relative integrals, previously
uncontrolled, now converge to the actual limit's integral. Together
with the proved energy equality this gives $F_\nu(u)=D_\nu$.

For fixed original continuous $h$, set $z_t=P_\theta(u+th)$.
The same actual obstacle inequality used earlier gives
$E(z_t)-E(u)-t\int h d\nu\leq0$ by maximality.
Both continuous derivative signs from Proposition~\ref{fixed-increment}
give $\int h dM(u)=\int h d\nu$. Common finite mass and Riesz
uniqueness identify these measures. Attainment precedes this equation;
the target did not define $M$.
\end{proof}

\section{Conditional whole planes and every-solution separation}
The same absolute estimate also addresses an obligation independent of
attainment: every operator solution must belong to the maximizing family,
and that family must be separated by actual probes.

\begin{proposition}[Fixed tests and whole planes]\label{whole-planes}
Under S--M, if $\sigma_i=M(w_i)\to M(w)$ weakly with uniformly bounded
costs, then every \emph{fixed} actual relative finite-energy test has
converging integrals. Moreover
\begin{equation}\label{whole-plane}
 E(v)\leq E(u)+\int(v-u)dM(u),\qquad u,v\in\E^1_\theta.
\end{equation}
\end{proposition}
\begin{proof}
For a fixed normalized $v$, take model majorants $v_j\downarrow v$.
Their ordered midpoint defects satisfy
$\delta(v_j,v)\leq(E(v_j)-E(v))/2\to0$.
Estimate \eqref{modulus-output} therefore gives uniform absolute
$L^1$ error over the bounded-cost family of outputs for replacing
$R-v$ by the bounded relative test $R-v_j$.
At each fixed $j$, Lemma~\ref{density} and
Lemma~\ref{bounded-passage} pass that bounded relative integral through
weak convergence, since the limiting output misses $Z$. This proves
the fixed-test assertion, also after multiplying by a fixed $h\in C(K)$.
The collar is fixed at this bounded step before the output index.

Take canonical model envelopes $a_i\downarrow u$. Their costs are
bounded and their outputs converge by M1. Apply their finite planes
to $v$, writing $v-a_i=(v-u)-(a_i-u)$ on $U$.
The first integral converges by the fixed-test result just proved,
applied separately to $v$ and $u$. The second tends to zero by
\eqref{modulus-output} and
$\delta(a_i,u)\leq(E(a_i)-E(u))/2$.
Pass the decreasing energies to obtain \eqref{whole-plane}.
Constants are restored using raw mass $V$ and the energy constant law.
\end{proof}

\begin{corollary}[Every-solution uniqueness for the conditional map]
Under S--M every actual $M$-solution for an intrinsic target is unique
modulo a real constant. Every such solution maximizes the intrinsic objective.
\end{corollary}
\begin{proof}
If $M(a)=\nu$, \eqref{whole-plane} gives $F_\nu(v)\leq F_\nu(a)$
for every actual $v$. Normalize any two solutions $a,b$ at $v_0$.
They maximize the same objective; its value at their midpoint is
at least this common maximum by concavity and at most it by definition.
Thus $\delta(a,b)=0$.
For every rational divisorial $z$, apply the intrinsic-probe estimate
\eqref{modulus-target} at $V\delta_z$. It gives $a(z)=b(z)$.
G0 order determination in the common actual ample cone gives equality
on \emph{all} original points, including supported poles. Removing
normalization restores one real constant. This proof treats every
solution of the conditional map; it does not merely pick one maximizer.
\end{proof}

This separation mechanism does not supply strict Borel locality or comparison.
No claim that $\{u<v\}$ is open appears in it. Nor does it identify every
unbounded mixed moving quotient with an original genuine test. Thus even
the conditional attained-and-separated equation above is not the full
original P16.5 theorem required by the assignment.

\section{The additional zero-volume range actually proved}
Here let the actual rational bundle $L$ be numerically trivial on the
same smooth integral projective $X$, including nontorsion elements of
$\operatorname{Pic}^0(X)$. Use the literal varying-actual-bundle cone
at numerical class zero and the canonical zero scalar as reference.
The following result uses G0 and the single-net definition directly,
and does not require S--M.

\begin{proposition}[Numerical zero]
In this convention $\PSH(0)=\mathbb R$. Its raw energy is zero,
$\E^1(0)=\mathbb R$, and its raw top operator on constants is zero.
The only positive mass-zero target is literally the zero measure,
and its equation is attained and unique modulo constants.
\end{proposition}
\begin{proof}
For every positive rational $\epsilon$, the actual $L+\epsilon A$
is ample. Its weight-zero generating system is zero on every original
point. These constant scalars give one defining net for zero, and
constant shifts give all real constants. Conversely normalize
$u\in\PSH(0)$ to generic value zero. Integer tensoring makes
$m u\in\PSH(0)$ for every positive integer $m$. Embed each into
one fixed actual ample cone by the elementary embedding in Section 1.
The same ample coordinate bound gives $-C_z\leq m u(z)\leq0$ for
every $m$, hence $u(z)=0$ for each rational divisorial $z$.
G0 all-point determination gives $u=0$ everywhere.

The constant raw ample energies are $c\epsilon^n(A^n)$ and the
constant raw top measures have this positive mass. Positivity bounds
their integral against any continuous test by its sup norm times
$\epsilon^n(A^n)\to0$. Their unique raw limit is zero, and the
energy is zero on every constant. This gives the stated energy and
operator on the \emph{entire} classified cone. A positive Radon
measure of zero total mass is zero. Its relative dual energy is zero.
The quotient of solutions by constants has one element. Comparison
and both zero energy derivative signs are immediate. No zero volume
is divided out and no probability measure is retained.
\end{proof}

This is precisely the numerical-zero range, not the full pseudoeffective
zero-volume cone. On $\mathbb P^1\times\mathbb P^1$ take the nonzero nef
$L=p_1^*\OO(1)$. Its volume is zero, and the pullback of
$\max(\log\|z_1\|_{\rm triv},-1)$ is a nonconstant bounded generated-system
scalar in its nef cone, while zero is another. The same scalar can be
written with the actual generated sections $z_1,z_0$ and respective
weights $0,-1$, so it is not a merely local formula.
Tensor into $L+\epsilon\OO(1,1)$. Their positive raw top masses are
$2\epsilon(1+\epsilon)\to0$, hence both raw top limits vanish although
the original potentials differ by more than a constant. Thus a general
raw mass-zero top equation cannot retain uniqueness on that entire
nonzero nef cone. This is a safeguard, not a counterexample to the
requested positive-volume theorem or a solution for all zero-volume data.

\section{Precise unproved statements and canonical result}\label{gaps}
The original completion criterion is not achieved. The retained domain
remains \emph{every} actual big rational bundle on every retained smooth
integral projective $n$-fold over every retained field. The precise boundary
of this submission is as follows.
\begin{enumerate}
\item Independently establish S1--S3 on the literal single-net cone,
including closure across old supported poles, original envelopes, actual
normalized compactness, weak usc and all-point outer full-section energy,
canonical nonpositive model majorants, finite-energy divisor poles, and
genuine contraction. None is a consequence just of deleting ``ample''
from G0; G1's one endpoint does not grant the whole package.
\item Independently establish M1--M2 in the entire domain. In particular,
complete the target-independent output construction, its finite-model
compatibility, every required weak limit, algebraic-divisor nullness,
the actual shared horizontal-factor identities and the finite-moving
energy and raw top-measure limits. The finite Taylor calculation in
Section~\ref{variation-section} is not this whole construction.
\item Construct and identify the \emph{genuine original} finite-energy
operator with every admissible approximation, all unbounded mixed
products, all raw weighted limits and their independence. The finite
absolute modulus and the conditional whole planes do not identify
simultaneously changing physical quotients which are outside original
$\E^1$. Ordinary big positive products are not made multilinear here.
\item Prove original strict-winning locality and strict Borel comparison
for every actual finite-energy pair. The set $\{u<v\}$ need not be
open. Neither the fixed-continuous weak limits nor the discarded one
algebraic divisor justify passing its indicator through changing measures.
Nonalgebraic negligible-set nullness needs its own proof when used.
\item To make the conditional attained-and-separated equation in
Theorem~\ref{attainment} an original-scope theorem, first discharge
the package in the preceding items and identify the map used there
with the genuine required operator. The attainment and strict-probe
arguments themselves have full proofs here under their explicit
antecedents; they are not independent grants for those antecedents.
\item Specify and prove any further nonzero zero-volume pseudoeffective
range with its actual reference and replacing datum. Only the
numerically trivial rational-bundle range is established here.
\end{enumerate}
These are unresolved assertions of this draft, not a bibliographical
claim that no theorem exists. No other P16 family axis is claimed solved.
The exact unchanged original task and full contextual family are preserved
in the frozen input. No narrowed endpoint or formal conditional transfer
is counted as the original solution. The canonical result is
\texttt{candidate=false}.

\appendix
\section{Primary evidence, literal reading coordinates, and authority}
The two caller grants are preserved whole in
\texttt{supplied/unit-00.txt} and \texttt{supplied/unit-01.txt}.
Every other supplied body and ledger is preserved as mathematical data
in \texttt{supplied/}; \texttt{supplied/index.json} maps each whole unit
to the inclusive LF coordinates of the exact decoded assignment.
No historical path from those ledgers was opened. No independent reviewer,
private output, other campaign, or earlier claimed acceptance was inspected.

The raw public primary connector responses are saved in \texttt{sources/}.
The script \texttt{extract\_sources.py} constructs six complete pertinent
statement/proof units and maps their local LF lines to literal renderer
labels, preserving PDF page labels separately. Its corrected parser handles
multiple source documents inside one connector text block. All six selected
intervals are complete and overlap consistently; no missing renderer label
or conflicting text remains. Local coordinates mean UTF-8 decoding followed
by splitting on LF, inclusive and one-based. Renderer labels are zero-based;
they are not represented as LF lines of a locally downloaded original PDF.
No original PDF download or original PDF byte hash is asserted.

\begin{longtable}{p{.16\linewidth}p{.24\linewidth}p{.51\linewidth}}
Version & Exact retained coordinates & Application and limitation\\\hline
BJ v4, arXiv:\allowbreak 1801.08229v4, PDF date 24 March 2022 &
Renderer 2705--2789, local LF1--85 &
Complete finite Hodge/concavity unit. Finite model calculus only;
the algebraic Hodge input cited there is ordinary background.\\
BJ v4 & Renderer 2790--3107, local LF1--318 &
Complete finite distance, slot replacement and quasi-triangle proof unit.
We reconstruct it with the independently proved $n-j$ orientation.
The printed repeated-potential quasi-triangle expression is not used.\\
BJ v4 & Renderer 6157--6257, local LF1--101 &
Complete ample four-point lemma/proof, diagnostic only. Its unbounded
ample regularization is not transferred to a big nonnef class.\\
BFJ v2, arXiv:\allowbreak math/\allowbreak 0608260v2, posted 4 September 2007 &
Renderer 310--441, local LF1--132 &
Complete positive-product construction, directed compactness, monotonicity,
continuity and nef agreement units. Used in actual smooth big algebraic
determinations, paired through fixed nef tests.\\
BFJ v2 & Renderer 445--545, local LF1--101 &
Concavity/volume statements and complete pertinent volume derivative proof.
Both derivative signs and continuity at the big boundary are retained;
Fujita, section asymptotics and the cited Morse background are explicitly
ordinary algebraic inputs, not an NA equation.\\
Addendum v2, arXiv:\allowbreak 2206.07183v2, PDF date 7 September 2023 &
Renderer 128--257, local LF1--130 &
Complete bounded FS-envelope and model/lattice statements and proofs.
Source matching only for the independently reconstructed density; the
single-net proof does not import its general nonample closure call.
Actual section-extension use is covered by G1's exact signature.\\
\end{longtable}

The BFJ HTML's automatically generated date is not a new source version.
Its characteristic-zero algebraically closed field statement is retained
from the independent primary read, separately from its theorem units.
The source-application ledger distinguishes G0/G1, ordinary published
algebraic premises, new proofs, explicit conditional inputs, and diagnostic
readings. A source ledger from an earlier author is not our reading evidence.
No snippets or unsupplied mathematical verdicts are used as premises.

\section{Reproducibility and checks}
\texttt{frozen/input-original.json} preserves the exact supplied input bytes;
the decoded task and assignment are separately frozen. The complete assignment
still contains every supplied positive-volume and additional zero-volume
statement, without relying on this paper's paraphrases. Run
\texttt{python3 rerun.py} here. It verifies frozen preservation, every
supplied whole-unit coordinate and hash, source-unit maps, source overlap,
backwards local note support, and finite exact rational transcription checks.
It then compiles \texttt{paper.tex} twice using the existing pdfLaTeX.
The program retains argv, stdout/stderr, status, versions, finite check inputs
and outputs, and an artifact manifest. No package is installed.

The finite checks cover dimensions 1--12 for the corrected polynomial and
midpoint coefficients, and concrete rational weighted graphs for the absolute
contraction. These are \emph{finite checks}, not an exhaustive theorem over
all models. The all-dimension arguments are the mathematical proofs in
Sections 2--3. Compiling this paper and passing these tests certify neither
the algebraic imported background nor the conditional package.

No subagents or campaigns were launched. No credentials, account, auth,
runtime configuration, or environment variables were read or changed.
Only this fresh workspace and public primary sources were used.
No operator-provided supervised compute facility was exposed; no
resource-heavy local calculation was launched. The exact native model
identifier is not exposed in the recorded command environment, and no
model/runtime change was attempted. This is an unverified mathematical draft.

\begin{thebibliography}{9}
\bibitem{BJ} S. Boucksom and M. Jonsson,
\emph{Global pluripotential theory over a trivially valued field},
\href{https://arxiv.org/pdf/1801.08229v4}{arXiv:1801.08229v4}.
\bibitem{BFJ} S. Boucksom, C. Favre and M. Jonsson,
\emph{Differentiability of volumes of divisors and a problem of Teissier},
\href{https://arxiv.org/html/math/0608260v2}{arXiv:math/0608260v2}.
\bibitem{ADD} S. Boucksom and M. Jonsson,
\emph{Addendum to global pluripotential theory over a trivially valued field},
\href{https://arxiv.org/pdf/2206.07183v2}{arXiv:2206.07183v2}.
\end{thebibliography}
\end{document}

END COMPLETE MATHEMATICAL BODY

BEGIN COMPLETE MATHEMATICAL BODY 159 OWN SOURCE LEDGER
{
  "status": "unverified incomplete mathematical draft; candidate=false",
  "grants": [
    {
      "name": "G0",
      "scope": "Only complete supplied actual AMPLE rational-bundle theorem and exact foundations",
      "file": "supplied/unit-00.txt"
    },
    {
      "name": "G1",
      "scope": "Only resolved actual relative generation and its one generically finite FS net",
      "file": "supplied/unit-01.txt"
    }
  ],
  "unreviewed_supplied_data": "All other supplied whole bodies and ledgers. No external historical path or private review opened.",
  "primary_versions": {
    "BJ-v4": {
      "url": "https://arxiv.org/pdf/1801.08229v4",
      "pdf_date": "2022-03-24"
    },
    "BFJ-v2": {
      "url": "https://arxiv.org/html/math/0608260v2",
      "posted": "2007-09-04",
      "html_automatic_date_is_not_version": true
    },
    "ADD-v2": {
      "url": "https://arxiv.org/pdf/2206.07183v2",
      "pdf_date": "2023-09-07"
    }
  },
  "complete_pertinent_units": [
    {
      "source": "BJ-v4",
      "name": "finite-Hodge",
      "file": "sources/units/BJ-v4-finite-Hodge.txt",
      "map": "sources/units/BJ-v4-finite-Hodge.map.json",
      "renderer_start": 2705,
      "renderer_end": 2789,
      "missing": [],
      "local_lf_start": 1,
      "local_lf_end": 85,
      "sha256": "efdbe3c6b22da46f59e5701b2cb1d309296e5844f8c6096e7a67651dae18923b"
    },
    {
      "source": "BJ-v4",
      "name": "finite-slots",
      "file": "sources/units/BJ-v4-finite-slots.txt",
      "map": "sources/units/BJ-v4-finite-slots.map.json",
      "renderer_start": 2790,
      "renderer_end": 3107,
      "missing": [],
      "local_lf_start": 1,
      "local_lf_end": 318,
      "sha256": "b35990fe47f0ed8e4301e79d96e26157fb312ef4f52ff62da96977fbb9cfb149"
    },
    {
      "source": "ADD-v2",
      "name": "FS-and-model-lattices",
      "file": "sources/units/ADD-v2-FS-and-model-lattices.txt",
      "map": "sources/units/ADD-v2-FS-and-model-lattices.map.json",
      "renderer_start": 128,
      "renderer_end": 257,
      "missing": [],
      "local_lf_start": 1,
      "local_lf_end": 130,
      "sha256": "346d25bb6b160181a4baa68960e2b70c1c463de6cbeac60c5e6d88f8c20ac70c"
    },
    {
      "source": "BFJ-v2",
      "name": "positive-products",
      "file": "sources/units/BFJ-v2-positive-products.txt",
      "map": "sources/units/BFJ-v2-positive-products.map.json",
      "renderer_start": 310,
      "renderer_end": 441,
      "missing": [],
      "local_lf_start": 1,
      "local_lf_end": 132,
      "sha256": "6c15466488dfc98ca2b08915a967e744399ae3309639ca9c3d543d686f895c8a"
    },
    {
      "source": "BFJ-v2",
      "name": "volume-differentiation",
      "file": "sources/units/BFJ-v2-volume-differentiation.txt",
      "map": "sources/units/BFJ-v2-volume-differentiation.map.json",
      "renderer_start": 445,
      "renderer_end": 545,
      "missing": [],
      "local_lf_start": 1,
      "local_lf_end": 101,
      "sha256": "8651090225d1a0201460f316a49cd69fc8a7734a1a9d4dc29ded54b60aaf1c47"
    },
    {
      "source": "BJ-v4",
      "name": "ample-four-point-diagnostic",
      "file": "sources/units/BJ-v4-ample-four-point-diagnostic.txt",
      "map": "sources/units/BJ-v4-ample-four-point-diagnostic.map.json",
      "renderer_start": 6157,
      "renderer_end": 6257,
      "missing": [],
      "local_lf_start": 1,
      "local_lf_end": 101,
      "sha256": "ecc0e3ad4f9f05571058823dea1f35e37d06cd73019bbfc638997434cb2ae5b0"
    }
  ],
  "separate_field_read": {
    "file": "sources/BFJ_field.json",
    "literal_renderer_line": 147,
    "claim": "ordinary algebraic theory extends to every algebraically closed characteristic-zero field"
  },
  "applications": [
    {
      "index": 0,
      "claim": "Finite vertical quadratic forms and finite slot-change estimates",
      "units": [
        "BJ-v4-finite-Hodge",
        "BJ-v4-finite-slots"
      ],
      "scope": "rational bounded relatively nef models only; corrected n-j orientation independently proved"
    },
    {
      "index": 1,
      "claim": "Algebraic positive products, nef/psef monotonicity and continuity",
      "units": [
        "BFJ-v2-positive-products"
      ],
      "scope": "actual smooth projective big determinations, fixed signed tests decomposed into two fixed nef tests"
    },
    {
      "index": 2,
      "claim": "Volume intercept, gradient, positive time-deficient derivatives and uniform finite-model variation",
      "units": [
        "BFJ-v2-volume-differentiation"
      ],
      "scope": "big algebraic classes only; no unbounded NA inverse equation"
    },
    {
      "index": 3,
      "claim": "Exact actual FS and full relative model-section conventions",
      "units": [
        "ADD-v2-FS-and-model-lattices"
      ],
      "scope": "primary source matching; density independently proved and G1 section-extension scope retained"
    },
    {
      "index": 4,
      "claim": "Ample four-point estimate diagnostic",
      "units": [
        "BJ-v4-ample-four-point-diagnostic"
      ],
      "scope": "not an unbounded big-class premise"
    }
  ],
  "new_proofs": [
    "Resolved absolute-value graph contraction with every central multiplicity",
    "Midpoint-defect raw absolute finite moment",
    "Uniform finite-model Taylor reconstruction with signed big-cone margin",
    "Conditional midpoint trace transfer retaining the lost-volume term",
    "Conditional actual attainment excluding an energy jump using finite planes",
    "Conditional every-solution separation via raw divisorial probes",
    "G0-only numerical-zero cone and raw zero equation"
  ],
  "unproved_conditions": "paper.tex Section 5 S1-S3 and M1-M2; complete package is not claimed established",
  "remaining_original_gaps": "gaps.md and paper.tex Section 12: full scalar/output foundations, all unbounded mixed independence and strict Borel comparison",
  "ordinary_background_not_recursively_reproved": [
    "intersection theory and characteristic-zero equivariant principalization/SNC resolution",
    "Kodaira decomposition and ample generation",
    "normal proper birational section descent",
    "section-volume asymptotics and Fujita",
    "ordinary algebraic Hodge index and nef positivity",
    "compact Hausdorff normality and Radon regularity"
  ],
  "whole_primary_sources_read": false,
  "recursive_background_proofs_read": false,
  "coordinate_convention": "Inclusive one-based LF in saved UTF-8 text; original zero-based renderer and PDF page labels retained separately.",
  "original_pdf_download_claim": false,
  "retained_response_files": [
    {
      "file": "sources/ADD_full.json",
      "sha256": "2c99f7e618c4f930998f81845721c52c7f5027c615440ad6cbed7780cfb1bd41",
      "acquisition": {
        "open": [
          {
            "ref_id": "turn984795view2",
            "lineno": 90
          }
        ],
        "response_length": "long"
      }
    },
    {
      "file": "sources/BFJ_field.json",
      "sha256": "0741e3d521bfa6421d1c4bc45692f065691adb46cfcccb512f78ced65108e829",
      "acquisition": {
        "open": [
          {
            "ref_id": "https://arxiv.org/html/math/0608260v2",
            "lineno": 147
          }
        ],
        "response_length": "long"
      }
    },
    {
      "file": "sources/BFJ_positive.json",
      "sha256": "8ff23b9bb6bce3cc0fbbdb7032546acdf83902dcff3c41370310ca36bb877b32",
      "acquisition": {
        "open": [
          {
            "ref_id": "turn984795view1",
            "lineno": 299
          }
        ],
        "response_length": "long"
      }
    },
    {
      "file": "sources/BFJ_volume.json",
      "sha256": "dc99cfd68d55f139d488e00ba672486a7fe266d70a7da8f5b13f72833fead360",
      "acquisition": {
        "open": [
          {
            "ref_id": "turn984795view1",
            "lineno": 485
          }
        ],
        "response_length": "long"
      }
    },
    {
      "file": "sources/BJ_ample_continuity.json",
      "sha256": "990accfbad5e001678f02ef1f45473b9b1e2000c37098581638289e5dcc9da10",
      "acquisition": {
        "open": [
          {
            "ref_id": "turn984795view0",
            "lineno": 7790
          }
        ],
        "response_length": "long"
      }
    },
    {
      "file": "sources/BJ_attain.json",
      "sha256": "bae6603f75f80509eaa6a31e120232466378f6415435503d923ba2dda514c360",
      "acquisition": {
        "open": [
          {
            "ref_id": "turn984795view0",
            "lineno": 9600
          }
        ],
        "response_length": "long"
      }
    },
    {
      "file": "sources/BJ_finite.json",
      "sha256": "9452662b00245ec3fc327613bb4d65180266b40652193080b772d408aff8d3c7",
      "acquisition": {
        "open": [
          {
            "ref_id": "turn984795view0",
            "lineno": 2685
          }
        ],
        "response_length": "long"
      }
    },
    {
      "file": "sources/BJ_slot_tail.json",
      "sha256": "6775f955d3994924a0660ce5120a3c9cc4f67551b3ee2a03a0de1dbaf5f0412a",
      "acquisition": {
        "open": [
          {
            "ref_id": "turn984795view0",
            "lineno": 3020
          }
        ],
        "response_length": "long"
      }
    },
    {
      "file": "sources/BJ_volume_scope.json",
      "sha256": "99aa77989d9b979d3113be3dccb0bf19d224b8b87166220b5a28675564c46a6d",
      "acquisition": {
        "open": [
          {
            "ref_id": "turn984795view0",
            "lineno": 6170
          }
        ],
        "response_length": "long"
      }
    },
    {
      "file": "sources/initial.json",
      "sha256": "0a135d99abc882492615ed7d86fccb292554cdb6515a6b97b3b7ee4071411b3b",
      "acquisition": {
        "open": [
          "BJ",
          "BFJ",
          "ADD"
        ]
      }
    }
  ],
  "operator_supervised_compute": "No service exposed; no heavy calculation launched",
  "mathematical_certification": false
}

END COMPLETE MATHEMATICAL BODY

BEGIN COMPLETE MATHEMATICAL BODY WHOLE160
\documentclass[10pt]{article}
\usepackage[a4paper,margin=25mm]{geometry}
\usepackage{amsmath,amssymb,amsthm,mathrsfs,longtable,hyperref}
\setlength{\emergencystretch}{3em}
\newtheorem{theorem}{Theorem}[section]
\newtheorem{lemma}[theorem]{Lemma}
\newtheorem{proposition}[theorem]{Proposition}
\newtheorem{corollary}[theorem]{Corollary}
\newcommand{\PSH}{\operatorname{PSH}}
\newcommand{\FS}{\operatorname{FS}}
\newcommand{\MA}{\operatorname{MA}}
\newcommand{\vol}{\operatorname{vol}}
\newcommand{\an}{\mathrm{an}}
\newcommand{\EE}{\mathcal E^1_\theta}
\title{Single-net regularization and exact negligible-set transfer in big classes\\
\large An incomplete standalone paper for the unchanged original P16.5}
\author{Research draft relative to the two precise caller grants}
\date{6 October 2026}
\begin{document}
\maketitle
\begin{abstract}
We reconstruct genuine decreasing closure, envelopes, and normalized
compactness on the original carrier from the actual ample theorem and the
single resolved multiplier-ideal net granted with the assignment. The
flattening argument keeps an explicit weakened pole floor and a separate
positive guard. We then prove that every raw-supremum discrepancy of the
retained cone is covered by a genuine big-class psh pole. The raw supremum
and its usc regularization are identified literally at every point in a
common actual ample embedding; the pole returns by an actual section
tensor identity. Measure nullness follows only under explicitly stated
finite-energy and contraction inputs. A separate finite polarization
calculation identifies exactly what bounded convex-combination convergence
would supply for mixed products, and an algebraic example excludes replacing
that input by ordinary volume interpolation. We have not constructed every
unbounded mixed or weighted product, or established the complete equation.
The canonical result is candidate=false.
\end{abstract}

\section{Exact task, domain, and authority}
The original P16.5 asks for the finite-energy non-Archimedean equation
in big or pseudoeffective nonample classes, with the psh cone, reference
singularity, energy, and total mass specified, and with a replacement for
probability normalization at zero volume. The retained first domain is
every smooth integral projective $k$-variety $X$, of every dimension
$n\geq1$, over every algebraically closed characteristic-zero field
with the trivial absolute value, and every actual big rational line bundle
$L\in\operatorname{Pic}(X)\otimes\mathbb Q$. Write
$K=X^\an$, $\theta=c_1(L)$, and $V=\vol_X(L)>0$. No countability,
finite-generation, invariance, skeleton, or support hypothesis is added.
All supported semivaluations stay in the compact Hausdorff space $K$.
The scalar reference of a bundle is its canonical trivial metric.

Only G0 and G1 are caller mathematical grants. G0 is the supplied
complete actual ample rational-bundle theorem with its exact retained
field and geometric hypotheses. G1 is the supplied resolved relative
generation theorem and its one generically finite FS net. We use G0 on
the original smooth $X$ in actual ample classes. We use G1 on smooth
equivariant modifications with the stated actual vertical Cartier data,
full relative systems, and actual ample twist. No extension of either
grant to big-class energy or equations is presumed. Other manuscripts
are unreviewed mathematical data; their propositions are not premises
of the positive results below.

Ordinary algebraic background is Kodaira's ample-plus-effective
decomposition of a big rational bundle, openness and numerical invariance
of ampleness, eventual global generation, and characteristic-zero
equivariant model resolution. Section 5 uses a separately retrieved
primary theorem in its actual ample scope. We distinguish that application
from both grants. We do not claim a recursive new proof of algebraic
resolution or the whole ample capacity theory.

An actual FS scalar on a rational bundle $B$ is
\[
 h=\frac1m\max_j\bigl(\log\|s_j\|_{\rm triv}+\lambda_j\bigr),
 \quad 0\ne s_j\in H^0(X,mB),\quad\lambda_j\in\mathbb R.
 \tag{1}
\]
Common zeros are permitted. These are continuous into
$\mathbb R\cup\{-\infty\}$ and have finite value at the generic
trivial valuation $v_0$. A genuine $\theta$-psh scalar is the all-point
decreasing limit of \emph{one} such net on actual $B_i$ with
$c_1(B_i)\to\theta$, and with finite generic endpoint. This is our
literal cone $\PSH(\theta)$, rather than a twice-closed family.
Every bundle exponent is cleared before taking sections.

The intended energy and target data, not constructed here in their
whole required scope, are the section-volume outer energy
\[
 E(u)=\inf_{f\in C(K),\ f\geq u}\mathscr E(f),\qquad
 \EE=\{u\in\PSH(\theta):E(u)>-\infty\},\qquad R=P_\theta(0),
 \tag{2}
\]
and positive Radon targets of raw mass $V$ such that
\[
 \nu\{R=-\infty\}=0,\qquad
 D_\nu=\sup_{u\in\EE,\ u(v_0)=0}
 \left(E(u)+\int(R-u)\,d\nu\right)<\infty.                 \tag{3}
\]
Differences in (3) are taken where $R$ is finite; no absolute
integrability of $R$ is silently required. The genuine full space in
(2), rather than only its bounded relative part, is an outstanding
operator obligation. The reference $R$ itself is constructed below.

\section{Exact scalar operations and bounded section density}
At the valuation-ring center of each original analytic point, a
generating section of an actual globally generated bundle is a unit.
All canonical section norms are at most one. Consequently the
weight-zero maximum of a generating system is exactly zero at every
point, including supported points. Tensoring with this system changes
the actual bundle but preserves the scalar everywhere.

\begin{lemma}[Common actual ample embedding]\label{embed}
Choose an actual ample rational $\Omega$ such that $\Omega-L$ is
ample. Every $u\in\PSH(\theta)$ is the same all-point scalar function
in the genuine ample cone of $\Omega$.
\end{lemma}
\begin{proof}
For a tail of a defining net, $\Omega-B_i$ is ample. Clear powers
and tensor with its generating system to obtain the same scalar on
$\Omega$. To remove common zeros, replace the scalar stage by
$\max(h_i,-N)$ using generators of a power of $\Omega$ with weight
$-mN$. The product-directed net $(i,N)$ is decreasing, has fixed
actual bundle $\Omega$, and has all-point infimum $u$. Its generic
endpoint remains finite. It is an actual ample defining net within G0.
No infinite value was subtracted and no modification of $X$ was used.
\end{proof}

In particular the generic value equals the supremum; all divisorial
values are finite and determine all-point order by G0. Normalized
functions have finite uniform coordinate bounds in the one compact
normalized ample cone. The same embedding works at any fixed real
numerical class $\eta$ using an actual ample $\Omega$ with
$c_1(\Omega)-\eta$ ample, without requiring a rational representative
of $\eta$.

Finite maxima in the same class have single defining nets: put two
incoming stages on the actual $L+\varepsilon A$ whenever both actual
differences are ample, and unite their section systems. Valid triples
of indices and rational $\varepsilon>0$ are directed by choosing a
smaller $\varepsilon$ and sufficiently late indices. The scalars
decrease and their classes tend to $\theta$.
For a real convex coefficient $0<r<1$, put incoming scalars below a
common finite $C$, choose positive rational $r_j\uparrow r$ and
$s_j\uparrow1-r$, and use
\[
 r_j(h_i-C)+s_j(g_l-C)+C.
\]
This is a decreasing product net of actual FS scalars on
$r_jB_i+s_jB'_l$. Its class tends to $\theta$ and its generic endpoint
is finite. Constants, rational scaling, and integer tensoring are direct.

Fix one actual Kodaira identity $L=aA+E_0$, with $a>0$ rational,
$A$ ample, and $E_0$ effective rational Cartier. Set
$W=\log\|s_{E_0}\|\leq0$, $Z=E_0^\an$, and $U=K\setminus Z$.
Tensoring its section with a generating power of $aA$ realizes $W$
on the actual $L$. It is finite continuous on $U$.

\begin{lemma}[Bounded minorants]\label{density}
For every bounded continuous $f$ and every genuine $u\leq f$,
\[
 u\leq Q_L(f):=\sup\{h\in\FS(L):h\leq f\}\quad\text{on }U.
 \tag{4}
\]
This statement does not presume decreasing closure or a genuine envelope.
\end{lemma}
\begin{proof}
Take its literal net $h_i\downarrow u$ on $B_i$. Fix rational
$0<t<1$ and $\epsilon>0$ before taking a tail. The actual bundle
$L-(1-t)B_i-t(L-aA)$ is eventually ample. The nested compact sets
$\{h_i\geq f+\epsilon\}$ have empty intersection, so a whole tail
has $h_i<f+\epsilon$ on all of $K$. Set $C=\|f\|_\infty$.
Tensor the sections with the zero-weight system of the actual ample
difference. This gives the actual $L$-FS minorant
\[
 (1-t)(h_i-\epsilon)+t(W-C)\leq f
\]
at every original point. At $x\in U$ with $u(x)$ finite, take the
incoming endpoint, then $t\downarrow0$, then $\epsilon\downarrow0$.
The value of $W(x)$ is finite, giving (4). If $u(x)=-\infty$, the
inequality is immediate. Supported zeros satisfy the minorant inequality
literally as extended values.
\end{proof}

\begin{proposition}[First genuine model envelope]\label{model}
For every rational continuous model obstacle $f$, its all-point raw
envelope $P_\theta(f)$ is genuine. In particular $R=P_\theta(0)$
is genuine, $R(v_0)=0$, and normalized genuine $u$ satisfy $u\leq R\leq0$.
\end{proposition}
\begin{proof}
Represent $f$ on a resolved equivariant model in G1's exact signature.
That grant supplies one genuine endpoint $\Psi$ with
$Q_L(f)\leq\Psi\leq f$. Lemma~\ref{density} puts every genuine
competitor below $\Psi$ off $Z$, hence at every divisorial valuation.
Embed the two already genuine functions into the same actual ample
$\Omega$. G0 order determination gives the inequality at every point
of $K$. The endpoint $\Psi$ is itself a competitor, so it is exactly
$P_\theta(f)$, without taking any second decreasing closure.
For $f=0$, $W$ is a genuine minorant with generic value zero, proving
the reference normalization and the stated maximality.
\end{proof}

For any actual big rational $B$, the same result constructs $R_B$.
A late G1 stage for its zero obstacle, on the actual $S=B+C/m$,
can be normalized to a scalar $\psi_B\leq0$. Its original generic
shift $c_B$ is finite and
\[
 R_B\leq\psi_B+c_B.                                      \tag{5}
\]
We do not assert that the separately normalized stages form a
decreasing net; only each fixed reference in (5) is used next.

\section{Single-net decreasing closure across old poles}
\begin{lemma}[Compact pole comparison]\label{polecompare}
Let $\psi\leq0$ be an actual FS scalar and let an actual FS scalar
$F$ satisfy $F\geq(1-\delta)\psi-k$, where $0<\delta<1$.
For usc $h\leq\psi+C$, the comparison $h-F$, assigned value
$-\infty$ at poles of $F$, is usc. Decreasing such $h$ give decreasing
comparison functions. If their infimum is negative everywhere, a whole
tail of the comparisons is negative everywhere.
\end{lemma}
\begin{proof}
Where $F$ is finite the comparison is usc and at most
$\delta\psi+C+k$. A pole of $F$ forces $\psi=h=-\infty$.
Extended continuity of $\psi$ makes this upper bound tend to
$-\infty$ near that point, proving usc of the assigned comparison.
This is an extension of a comparison, not arithmetic
$(-\infty)-(-\infty)$. The nonnegative superlevels are nested compact
sets. Empty intersection and directedness make one such set, then
all later ones, empty.
\end{proof}

\begin{theorem}[Genuine decreasing closure]\label{closure}
If $u_i\in\PSH(\theta)$ decrease all-point to $u$ with $u(v_0)$
finite, then $u$ has one all-point decreasing FS net with classes
tending to $\theta$.
\end{theorem}
\begin{proof}
Restrict to a tail $u_i\leq M$. For rational $\eta>0$ let
$T_\eta=L+\eta A$. Choose $0<\epsilon<\eta/4$ and
$B=L+\epsilon A$. Use (5) to choose a normalized reference stage
$\psi\leq0$ on an actual $S$ sufficiently close to $B$ that
$T_\eta-S$ is ample. Choose small rational $0<\delta<1$ with
$T_\eta-(1-\delta)S$ still ample.

A special stage is an actual FS scalar on the specified $T_\eta$
with complete reference data as above and with
\[
 F\geq u+\kappa,\qquad F\geq(1-\delta)\psi-k,
 \tag{6}
\]
where $\kappa>0$ is rational and $k$ finite. Such a stage exists:
tensor a late defining majorant of one $u_i$, shifted by $\kappa$,
and the pole floor into $T_\eta$, then take their maximum.

For every fixed old $B_l,\psi_l$, all $u_i$ embed as scalars in
$\PSH(c_1(B_l))$: their incoming stages eventually have actual ample
difference to $B_l$. Late stages $h$ of a fixed $u_i$ do likewise.
Their generic values are eventually at most $M+1$. The model
reference maximality, valid before closure, gives
\[
 h\leq R_{B_l}+M+1\leq\psi_l+c_l+M+1.                    \tag{7}
\]
The same bound holds for all $u_i$. This is the common old-pole
control needed for Lemma~\ref{polecompare}.

Given finitely many old special stages $F_l$ with guards $\kappa_l$,
choose new $\eta$ arbitrarily small below all their $\epsilon_l$.
Choose its new reference stage $\psi$ on $S$ sufficiently close to
$L+\epsilon A$ that $B_l-S$ is ample for every $l$. Thus
$\psi\leq R_{B_l}\leq\psi_l+c_l$. Choose
$0<\delta<\min_l\delta_l$ satisfying the new target ample gap.
Where $F_l$ is finite, the new floor $b=(1-\delta)\psi-k$ satisfies
\[
 b-F_l\leq(\delta_l-\delta)\psi_l+(1-\delta)c_l+k_l-k.
\]
Since $\psi_l\leq0$, one large $k$ gives $b\leq F_l$ for all $l$.
At an old pole, the reference inequality forces $b=-\infty$, so
this inequality is literal there too.

Choose $0<\kappa<\min_l\kappa_l/4$. Apply
Lemma~\ref{polecompare} to the decreasing $u_i+2\kappa$ using (7).
Its limit comparison is negative: at a finite old value it is at
most $2\kappa-\kappa_l<0$, and at an old pole it is assigned
$-\infty$. One common late $i$ satisfies every old comparison.
Apply the lemma again to the literal defining tail of this fixed
$u_i$, shifted by $\kappa$, with (7). Choose one stage $h$, late
enough to fit the new actual $T_\eta$, such that
$h+\kappa\leq F_l$ for all $l$. Then
\[
 F=\max(h+\kappa,b)\leq F_l\quad(\text{all }l),
 \qquad F\geq u+\kappa.
\]
It is a new special stage. Order all special stages by scalar
decrease and by $\eta$ decrease. This is a directed net whose class
tends to $\theta$.

Its infimum is $u$ at every point. Given $x$ and finite $t>u(x)$,
choose $u_i(x)<t$ with margin, choose a target gap $\eta$ before
a sufficiently late defining stage $h$ fitting it, and choose its
positive guard sufficiently small that $h(x)+\kappa<t$. A large
$k$ makes the floor below $t$ at $x$, or it already has value
$-\infty$ there. This constructs a special stage below $t$ at $x$;
directedness can impose every old constraint afterwards. The argument
works for every finite $t$ when $u(x)=-\infty$. All special stages
stay above $u$ and the stipulated generic endpoint is finite.
\end{proof}

\section{Genuine envelopes and original compactness}
\begin{theorem}[Envelopes and raw-supremum regularization]\label{envelopes}
Every upper bounded usc obstacle $f$ with a genuine generically finite
minorant has a genuine all-point envelope $P_\theta(f)$.
For any nonempty uniformly upper bounded family $(u_\alpha)$ in
$\PSH(\theta)$, the literal function
$(\sup_\alpha u_\alpha)^*$ is genuine $\theta$-psh.
\end{theorem}
\begin{proof}
On a compact Hausdorff space an upper bounded usc function, including
one with poles, is the pointwise infimum of continuous majorants.
For each point and strict finite upper value, use a continuous cutoff
inside the open strict sublevel neighborhood, and a global upper
bound outside that neighborhood. Uniform rational model density from
G0 and finite minima give a directed decreasing net of rational
model majorants with the same infimum. Their envelopes are genuine
by Proposition~\ref{model}, decrease, and dominate the stipulated
minorant at the generic point. Theorem~\ref{closure} makes their
endpoint genuine. It is below $f$ at every point; every original
competitor is below each envelope. Thus the endpoint is exactly
the raw $P_\theta(f)$.

Let $S=\sup_\alpha u_\alpha$ and $f=S^*$. There is a finite generic
lower bound from any one family member and a finite global upper bound.
Each member is a minorant of $f$, so $P_\theta(f)$ dominates $S$.
It is usc, hence dominates the least usc majorant $S^*$. The obstacle
inequality gives the opposite inequality. Therefore
$P_\theta(S^*)=S^*$ literally at every original point, not merely
on divisorial coordinates.
\end{proof}

For continuous $f$, Lemma~\ref{density} now proves
$P_\theta(f)=Q_L(f)$ on $U$. The left side is usc, the right side
is lsc, and both are finite there, so the envelope is continuous on
this ordinary open set. This equality is not asserted on $Z$.

\begin{theorem}[Normalized compactness]\label{compact}
The normalized genuine cone $\{u\in\PSH(\theta):u(v_0)=0\}$ is compact
in its divisorial topology.
\end{theorem}
\begin{proof}
Embed it into the compact normalized actual ample cone of $\Omega$.
Consider a net in the big cone converging in that ample cone to $a$.
Let $S_i^*=(\sup_{j\geq i}u_j)^*$. By Theorem~\ref{envelopes} these
are genuine $\theta$-psh, decrease, and have generic value zero.
Theorem~\ref{closure} gives their all-point infimum $b$ in the
normalized big cone. The primary finite separator theorem in the
actual ample cone, BJ Theorem 5.6 and Lemma 5.7, gives
$S_i^*(z)=\sup_{j\geq i}u_j(z)$ at each divisorial $z$. Hence
$b(z)=a(z)$ at all those coordinates. G0 all-point determination
in $\Omega$ gives $b=a$ everywhere. The normalized big cone is
therefore a closed subset of the compact ample cone.

The external separator result is applied only after the literal
common ample embedding. Its pertinent primary statement and full
proof have been independently read and saved. No big energy compactness
or equation is used in this proof.
\end{proof}

If the topology is indexed only by rational divisorial scalings, the
conclusion is unchanged. Along a ray $t\operatorname{ord}_E$, an FS
stage is a maximum of affine functions with nonpositive slopes. Its
finite decreasing endpoint is convex and decreasing on $t>0$.
Uniform ample coordinate bounds on a larger compact interval give
a uniform Lipschitz bound on each smaller interval, using the usual
secant inequalities for convex functions. Values on rational scalings
therefore determine both real-scaled values and their convergence.
This adds no field-countability assumption.

\section{Literal negligible-set transfer and genuine big poles}
For a bounded-above family in one single-net numerical cone, put
$S=\sup_\alpha u_\alpha$ pointwise and define its discrepancy
$D=\{S<S^*\}$. A negligible subset means any subset of such a
discrepancy, with the same original analytic topology.

\begin{theorem}[All-point negligible-to-big-pole transfer]\label{neglig}
Every such negligible subset $D'\subset K$, including discrepancies
from any fixed real numerical class with the single-net convention,
is contained in $\{q=-\infty\}$ for a genuine
$q\in\PSH(\theta)$ on the original $K$.
In particular this applies to every discrepancy of the retained big
cone. The witness has one actual section defining net.
\end{theorem}
\begin{proof}
Choose one actual ample $\Omega$ whose numerical difference from
the input family's class is ample. Lemma~\ref{embed} (with that
class) embeds each member as the \emph{identical scalar function} at
every point of $K$. Thus the raw supremum is identical, and its usc
regularization is identical, because the underlying topology and all
pointwise values are identical. Explicitly its value is the infimum
over neighborhoods $O$ of $x$ of $\sup_{y\in O}S(y)$ in both
descriptions. There is no equality inferred from divisorial density.
Hence $D'$ is an actual ample negligible subset in the exact primary
Definition 5.1 convention.

Apply BJ v4 Theorem 13.17 in that ample class: $X$ is irreducible,
$\Omega$ is ample, and EP is granted by G0. There is an ample-psh
$p$ with $p=-\infty$ on $D'$. Normalize $p(v_0)=0$.
This source theorem is an external premise in its ample domain,
not an assertion that negligible and polar mean the same by definition.
The whole pertinent statement/proof, including Lemma 13.19, has
been independently read; its capacity/Choquet dependencies are
documented in the evidence appendix.

Choose a positive rational $t$ so small that $L-t\Omega$ is big.
A nonzero section of a cleared positive multiple supplies an actual
effective rational divisor $E$ and an actual rational bundle identity
$L=t\Omega+E$. Let $q_E=\log\|s_E\|\leq0$.
G0 supplies a literal decreasing fixed-bundle FS net $p_i\downarrow p$
on $\Omega$. Clear $t$, the incoming section powers, and the divisor
power. Tensor each section of $p_i$ with the canonical section of
$E$ to obtain an actual $L$-FS stage with scalar
\[
 q_i=t p_i+q_E.
\]
This is one decreasing net. At $q_E$ poles it has value
$-\infty$ at every stage, and elsewhere its infimum is
$tp+q_E$. Thus its all-point endpoint $q$ is genuine in
$\PSH(\theta)$, is finite at $v_0$, and is $-\infty$ on $D'$.
This is an actual tensor identity on the original $X$, with no
arbitrary lift and no subtraction of supported poles.
\end{proof}

Conversely a genuine big-class pole is an ample pole by
Lemma~\ref{embed}. Thus the big and ample pole-covering collections
agree for this retained big domain. This assertion alone gives no
finite-energy membership for the transferred $q$: its chosen fixed
effective divisor can exceed the minimal singularity type. In
particular it does not give an unconditional output-nullness theorem.

Theorem~\ref{envelopes} supplies genuine big regularization independently
of this source application. For a big input family, $S^*$ is the same
all-point regularized scalar in both cones and is genuinely in the
big cone. We have proved precisely the all-point statement missing
from a merely divisorial identification.

\section{The remaining finite-energy nullness antecedents}
The following lemma makes the logical boundary of the new negligible
argument explicit. In this section only, assume that the energy (2)
has been independently established on the entire genuine cone, with
concavity, monotonicity, decreasing continuity, $E(R)=0$ and raw
constant law $E(u+c)=E(u)+cV$. Assume also its genuine contraction
\[
 B((1-r)R+ru)\leq C r^2 B(u),\quad B(u)=-E(u),
 \quad u(v_0)=0,\quad0<r<1,                              \tag{8}
\]
where $C$ is independent of $u$. These are additional unproved
energy inputs of this paper, not consequences of Section 5 or new grants.

\begin{lemma}[One genuine E1 pole covers each psh pole]\label{e1pole}
Under these energy inputs, for every normalized
$q\in\PSH(\theta)$ there is $p\in\EE$ such that
\[
 \{q=-\infty,\ R> -\infty\}\subset\{p=-\infty\}.
\]
\end{lemma}
\begin{proof}
Let $N_j=16^j$, $r_j=8^{-j}$, and $\lambda_j=2^{-j}$.
The genuine truncation $q_j=\max(q,R-N_j)$ is normalized and
$R-N_j\leq q_j\leq R$. Monotonicity and the raw constant law
give $B(q_j)\leq VN_j$, so $q_j\in\EE$.
Set $a_j=(1-r_j)R+r_jq_j$. Then (8) gives
$B(a_j)\leq CV4^{-j}$. The actual convex functions
\[
 p_m=\sum_{j\leq m}\lambda_j a_j+2^{-m}R
\]
decrease, have generic value zero, and have energy at least
$-CV\sum_{j\geq1}8^{-j}=-CV/7$ by concavity.
Theorem~\ref{closure} gives a genuine all-point endpoint; the
assumed decreasing energy continuity puts it in $\EE$.
Where $q=-\infty$ and $R$ is finite, $R-q_j=N_j$ and the exact
finite relative sum is
$R-p_m=\sum_{j\leq m}\lambda_jr_jN_j=m$. Thus $p=-\infty$ there.
\end{proof}

\begin{corollary}[Conditional full negligible nullness]\label{null}
Under these energy inputs, any finite positive Radon measure missing
$\{R=-\infty\}$ and integrating every genuine relative E1 test
has outer measure zero on every negligible subset of Section 5.
\end{corollary}
\begin{proof}
Theorem~\ref{neglig} supplies $q$. Lemma~\ref{e1pole} supplies one
actual E1 pole covering its pole outside the excluded reference poles.
Its nonnegative relative cost has finite integral, so the measure of
that Borel infinite-cost set is zero. The reference-pole set is also
Borel and null. Their union is a Borel null superset of the original
negligible set, even when the latter is not itself assumed Borel.
\end{proof}

This implication treats nonalgebraic raw-supremum discrepancies.
It cannot be used to establish its own energy or all-test output
integrability antecedents. In particular we have not proved that
the proposed outer-energy outputs satisfy those antecedents.
The finite-dual targets (3) would satisfy the all-test condition
directly once (2) is established, since each genuine test has finite
cost. The operator image inclusion remains a separate assertion.

\section{Finite polarization: an exact implementation and its boundary}
On any one finite common model, with nef slots $T_1,\ldots,T_n$
of the same generic bundle, the raw mixed measure has component
coefficient $b_E(T_1|_E\cdots T_n|_E)$ at $v_E$. These are ordinary
finite intersections. Their positive finite nef interpretation follows
from G0 on the actual ample $A+\epsilon H$ and the finite polynomial
limit as rational $\epsilon\downarrow0$; the scalar models are kept
fixed during that limit. Multilinearity gives
\[
 T_1\cdots T_n=\frac1{n!}
 \sum_{\varnothing\ne S\subset\{1,\ldots,n\}}
 (-1)^{n-|S|}\Bigl(\sum_{i\in S}T_i\Bigr)^n.             \tag{9}
\]
For raw model measures this is equivalently
\[
 \mu(T_1,\ldots,T_n)=\frac1{n!}
 \sum_{S\ne\varnothing}(-1)^{n-|S|}|S|^n\,
 \MA_{\rm raw}\left(|S|^{-1}\sum_{i\in S}T_i\right).
 \tag{10}
\]
Every central multiplicity is retained in each diagonal measure.
There is no division by the generic volume in this formula.

\begin{proposition}[What diagonal convergence would prove]\label{polarization}
Suppose, for a fixed finite list of genuine endpoints and admissible
shared moving approximants, the diagonal raw measures converge for
each of the finitely many rational barycenters in (10), with the
correct actual endpoint operator. Then the finite mixed measures
converge weakly to the expression (10) of those endpoint outputs.
That limit is positive, has the limiting raw mixed mass, and is
independent of any approximant family satisfying the same hypothesis.
\end{proposition}
\begin{proof}
Equation (9) follows by expanding homogeneous monomials of degree
$n$. A monomial whose support is a proper subset cancels in the
alternating superset sum. The only full-support monomial has every
exponent one and coefficient $n!$. This proves (9) for all $n$,
then (10) by homogeneity of the raw diagonal product.
For each fixed continuous test the finite sum (10) passes through
the stipulated diagonal limits. Each finite mixed measure is
positive, so its limiting integral of every nonnegative continuous
test is nonnegative. Riesz positivity gives the positive Radon
limit. The constant test gives its raw mass, and the resulting finite
sum depends only on the endpoint outputs. This proves the claimed
restricted independence. No unbounded test has been passed.
\end{proof}

The exact rational recipe is implemented in \texttt{polarize.py}.
For example in dimension two it is
$2\MA((u_1+u_2)/2)-(\MA(u_1)+\MA(u_2))/2$.
The program gives subset coefficients and checks the polynomial
identity and the raw mass coefficient. The proof is the all-dimension
cancellation argument, not its finite tests.

The hypotheses of Proposition~\ref{polarization} are \emph{not}
proved by the bounded moving-max argument in the supplied ROOT201.
A union of degree-$m$ systems represents a maximum on that same
degree. A rational convex combination generally uses tensor products
on a larger degree; the horizontal moving factor and its full-section
defect must be compared again. Convergence for endpoints and their
maximum alone does not prove the barycenter limits in (10).
The raw positive products of big algebraic classes are not
multilinear substitutes for this step.

Here is a direct algebraic safeguard, with no specialized external
volume-differentiation premise. On $\operatorname{Bl}_p\mathbb P^2$
write $H$ for the pulled hyperplane and $E$ for the exceptional curve.
For rational $-1<a<1$ let $D(a)=H+aE$. In a denominator-cleared
degree, if $a\geq0$, negative intersection with $E$ forces $maE$
as a fixed component; removal gives the whole system $|mH|$.
If $a=-b<0$, sections are degree-$m$ polynomials vanishing to order
$mb$ at $p$. In affine coordinates at $p$ the monomials of total
degree less than $mb$ impose independent conditions, because $mb<m$.
Therefore
\[
 h^0(mD(a))=\begin{cases}
 \binom{m+2}{2},&a\geq0,\\
 \binom{m+2}{2}-\binom{mb+1}{2},&a=-b<0,
 \end{cases}
\quad
 \vol(D(a))=\begin{cases}1,&a\geq0,\\1-a^2,&a<0.\end{cases} \tag{11}
\]
All these bundles are big. The volume function is constant on one
open half-interval and nonconstant on the other, so it is not one
polynomial on this entirely big segment. A quadratic fit at
$a=-1/2,0,1/2$ gives $1+a/4-a^2/2$; at $a=1/4$ it gives
$33/32$ while the true volume is $1$. This rules out obtaining the
required polarization merely by interpolating ordinary algebraic
volume along arbitrary big classes. It does not rule out a valid
same-class finite-energy mixed construction.

\section{Audit of the Borel transfer and remaining original obligations}
We separately checked the fixed-ramp mechanism of the supplied ROOT201.
Its crucial implication is correct under its stated genuine and output
inputs. With canonical $u_i\downarrow u$, $v_i\downarrow v$, a fixed
index $j$, and a fixed ramp vanishing when $u_j-v_j\leq\epsilon$,
an incorrect selection at $i\geq j$ with $u_i\leq v_i$ forces
$u_j-u_i>\epsilon$. Uniform ordered absolute errors therefore bound
the two offending positive measures before a weak limit is taken.
The test is held continuous and fixed through that limit; afterwards
one takes $j$ to its endpoint in absolute L1, then an ordinary
sequence of ramp widths to zero at fixed measures. This is a valid
conditional Borel-selection argument. No openness of the unbounded
winner or weak test by its moving indicator is required.

This check does not discharge the whole inputs. The scalar cone,
all-point envelopes, and compactness are reconstructed in Sections
2--4. We have not independently established the whole raw outer
energy, its unbounded mixed compatibility, contraction, uniform
absolute midpoint estimates, or the output map used by that Borel
argument. In particular finite nef locality needs the genuine finite
model coefficient calculus from G0 before a finite polynomial ample
perturbation; it cannot justify an unbounded nonample passage by itself.

The exact remaining statements for the unchanged original are:
\begin{enumerate}
\item Establish the entire scalar energy (2) and its weak usc,
decreasing continuity, raw mass constant law, genuine contraction,
and every finite moving trace compatibility, retaining lost-volume
errors until the fixed-continuous-test limit.
\item Construct the target-independent original-carrier operator
and prove both continuous energy derivative signs. Identify it
with all bounded rational barycenter approximations needed in (10),
then all mixed products in the full genuine E1 domain.
\item Identify every admissible simultaneous unbounded physical
weighted approximation and its independence. Physical section
functions with horizontal poles are not thereby original E1 tests.
Prove uniform time-deficient tail bounds and caps with every degree,
collar, cost, and raw mass limit in a justified order.
\item Establish all genuine relative E1 output integrability and
contraction. Only then Corollary~\ref{null} supplies full negligible
nullness, rather than just algebraic-divisor nullness.
\item Audit and discharge the hypotheses of the supplied absolute
midpoint, no-jump, attainment, full supporting-plane, and strict
separation arguments. An equation for the outer map alone is
insufficient until the required original operator is identified.
\item Discharge the bounded-max measure input and uniform ordered
errors of the strict Borel argument, then obtain genuine comparison
and uniqueness of every solution modulo constants.
\item Specify a replacement datum for any additional nonzero
zero-volume pseudoeffective range. No such additional range is
established in this paper.
\end{enumerate}
These are limitations of this submission, not a claim of
bibliographical nonexistence. No original P16.5 solution or other
P16-axis solution is asserted.

\section{The additional zero-volume range retained independently}
For the actual numerically trivial rational-bundle range, use the
same varying-actual-bundle cone at class zero, with zero reference.
This result needs only G0 and the literal single-net convention.

\begin{proposition}
In this convention $\PSH(0)=\mathbb R$. The raw zero-class top
operator and raw energy are zero on the entire cone; its finite-energy
space is $\mathbb R$ and its sole positive mass-zero target is the
zero measure. The equation is attained and unique modulo constants.
\end{proposition}
\begin{proof}
For any positive rational $\epsilon$, an actual numerically trivial
$L+\epsilon A$ is ample. Its zero-weight generating scalar is exactly
zero everywhere. These constant scalar stages with classes tending
to zero give one defining net; shifts give all constants.
Conversely normalize $u\in\PSH(0)$ at $v_0$ to zero. Integer
tensoring makes $mu\in\PSH(0)$ for every positive integer $m$.
Embed all of them into one fixed actual ample $\Omega$. Its normalized
compactness and finite continuous divisorial coordinates give
$-C_z\leq mu(z)\leq0$, uniformly in $m$. Thus $u(z)=0$ for
all divisorial $z$, and all-point determination gives $u=0$ on $K$.
The ample perturbations have raw mass $\epsilon^n(A^n)\to0$.
Positivity bounds every continuous test integral by this mass times
its sup norm. Thus the operator limit is zero. Its constant energies
are $c\epsilon^n(A^n)\to0$, giving zero energy on the entire
classified cone. A positive Radon measure with mass zero is literally
zero, and all solutions are constants. Comparison and the two zero
energy derivative signs are immediate. There is no division by zero.
\end{proof}

The nonzero nef class $p_1^*\mathcal O(1)$ on
$\mathbb P^1\times\mathbb P^1$ has zero volume and a nonconstant
bounded generated-system scalar obtained by pulling back the weighted
maximum of the two homogeneous coordinates with weights $0,-1$.
It and zero have vanishing raw top limits: their common positive ample
perturbation masses are $2\epsilon(1+\epsilon)\to0$. Therefore
uniqueness modulo constants fails for that whole zero-volume bounded
cone with the raw top equation. This safeguard is not an additional
nonzero zero-volume equation theorem.

\appendix
\section{Primary reading, preserved inputs, and reproducibility}
The exact input bytes, task object, full family, assignment, and all
18 marked supplied mathematical bodies are preserved in
\texttt{frozen/} and \texttt{supplied/}. Whole-unit inclusive
assignment-LF coordinates and hashes are in \texttt{supplied/index.json}.
Historical paths and hashes inside ledgers are documentary data; no
such path was opened and no historical or private verdict was inspected.

BJ means arXiv:1801.08229v4, PDF dated 24 March 2022. Primary
connector responses were fetched independently in this workspace.
The complete applied finite-separator unit is original renderer
3996--4022. The applied negligible-to-polar unit is 10614--10647,
including its exact ample-EP hypotheses and full pertinent proofs.
Ancillary statement/proof units read are 3863--3898 (polar detection),
10092--10108 (Choquet), 10289--10613 (quasicontinuity and capacity
comparison), and 10738--10847 (outer capacity). The literal
negligible definition is 3921--3928. Countable auxiliary selections
in the ample primary proof are conclusions of that theory, not
countability assumptions on our field, carrier, or given families.

The Addendum is arXiv:2206.07183v2. Its complete bounded-section-density
statement/proof at renderer 128--183 was independently read as source
matching; our proof uses its own actual ample-gap calculation and does
not import the Addendum's general closure. G1 alone supplies its exact
resolved model endpoint. BFJ v2 was opened diagnostically; no new
BFJ theorem is an external premise of this paper. The elementary
volume computation (11) is proved from its explicit section counts.

\texttt{sources/unit-index.json} maps all eight complete selected units
to local inclusive one-based LF coordinates and byte hashes, keeping
the original renderer and PDF page labels separate. No overlap conflict
or missing line remains. The source appendix records complete pertinent
units, not a claim to have read whole primary papers or recursively
all their background proofs. No original downloaded PDF is asserted:
a default-transport request failed with operation not permitted, and
the observation is preserved in \texttt{logs/network-attempt.json}.

Run \texttt{python3 rerun.py} here. It verifies the frozen bytes,
whole-unit slices, primary coordinates, backward note-support order,
and exact finite polarization and volume examples, and compiles this
paper twice with the installed pdfLaTeX. Programs, inputs, commands,
outputs, tool versions, and manifest are retained locally. These
checks are reproducibility and transcription evidence, not mathematical
certification. No resource-heavy calculation was launched; no
operator-provided supervised compute service was exposed. No agents,
credentials, account state, runtime settings, or other campaigns
were read or changed. The current native model identity is not
exposed by these tools and no model switch was attempted.

\begin{thebibliography}{9}
\bibitem{BJ} S. Boucksom and M. Jonsson,
\emph{Global pluripotential theory over a trivially valued field},
\href{https://arxiv.org/pdf/1801.08229v4}{arXiv:1801.08229v4}.
\bibitem{ADD} S. Boucksom and M. Jonsson,
\emph{Addendum to global pluripotential theory over a trivially valued field},
\href{https://arxiv.org/pdf/2206.07183v2}{arXiv:2206.07183v2}.
\end{thebibliography}
\end{document}

END COMPLETE MATHEMATICAL BODY

BEGIN COMPLETE MATHEMATICAL BODY 160 OWN SOURCE LEDGER
{
  "status": "Unverified incomplete proof draft; candidate=false",
  "frozen_input": {
    "file": "input.json",
    "bytes": 501731,
    "sha256": "e08d1880d1f321f082e67e31c60fc88ce0d5388f7728422e3e9816f841acc598"
  },
  "grants": [
    {
      "name": "G0",
      "file": "supplied/unit-00.txt",
      "scope": "Only complete actual AMPLE rational-bundle theorem and exact retained hypotheses/foundations"
    },
    {
      "name": "G1",
      "file": "supplied/unit-01.txt",
      "scope": "Only resolved relative generation and its one actual generically finite FS net"
    }
  ],
  "other_supplied_bodies": "All remaining supplied whole bodies and ledgers are unreviewed mathematical/provenance data. No historical path or verdict was opened.",
  "primary_versions": {
    "BJ-v4": {
      "url": "https://arxiv.org/pdf/1801.08229v4",
      "pdf_date": "2022-03-24"
    },
    "ADD-v2": {
      "url": "https://arxiv.org/pdf/2206.07183v2",
      "pdf_date": "2023-09-07"
    },
    "BFJ-v2": {
      "url": "https://arxiv.org/html/math/0608260v2",
      "scope": "Diagnostic opening only; no new BFJ theorem applied"
    }
  },
  "complete_pertinent_primary_units": [
    {
      "source": "BJ-v4",
      "url": "https://arxiv.org/pdf/1801.08229v4",
      "name": "nonnegligibility-full-proof",
      "file": "sources/units/BJ-v4-nonnegligibility-full-proof.txt",
      "map": "sources/units/BJ-v4-nonnegligibility-full-proof.map.json",
      "renderer_start": 3996,
      "renderer_end": 4022,
      "local_lf_start": 1,
      "local_lf_end": 27,
      "missing": [],
      "sha256": "aa6e55ab73cab1141ef754a6793f8e42a75c0d64a22e0dbf1ce3dfa7f78626dd",
      "application": "Applied only in the common ACTUAL ample cone for divisorial coordinates."
    },
    {
      "source": "BJ-v4",
      "url": "https://arxiv.org/pdf/1801.08229v4",
      "name": "definition-of-negligible",
      "file": "sources/units/BJ-v4-definition-of-negligible.txt",
      "map": "sources/units/BJ-v4-definition-of-negligible.map.json",
      "renderer_start": 3921,
      "renderer_end": 3928,
      "local_lf_start": 1,
      "local_lf_end": 8,
      "missing": [],
      "sha256": "d4896387ab2b5d5aac03049c4f56278afabf09a81e005b7f7ffbc7e7eb468209",
      "application": "Literal raw-supremum convention; common scalar embedding proved independently."
    },
    {
      "source": "BJ-v4",
      "url": "https://arxiv.org/pdf/1801.08229v4",
      "name": "negligible-polar-full-proof",
      "file": "sources/units/BJ-v4-negligible-polar-full-proof.txt",
      "map": "sources/units/BJ-v4-negligible-polar-full-proof.map.json",
      "renderer_start": 10614,
      "renderer_end": 10647,
      "local_lf_start": 1,
      "local_lf_end": 34,
      "missing": [],
      "sha256": "e38711fa9d3b9cb5f0c97aff89da4d9bd4621fbc32ffe1ea475c9b90a27347c3",
      "application": "Theorem 13.17 and Lemma 13.19 with their complete proofs, actual ample EP domain."
    },
    {
      "source": "BJ-v4",
      "url": "https://arxiv.org/pdf/1801.08229v4",
      "name": "capacity-quasicontinuity-and-comparison",
      "file": "sources/units/BJ-v4-capacity-quasicontinuity-and-comparison.txt",
      "map": "sources/units/BJ-v4-capacity-quasicontinuity-and-comparison.map.json",
      "renderer_start": 10289,
      "renderer_end": 10613,
      "local_lf_start": 1,
      "local_lf_end": 325,
      "missing": [],
      "sha256": "551940bc7a188cebec2f92f2e7c2c4e26f5a34acbedd53768c8ccae3653e8ad1",
      "application": "Antecedent reading for Theorem 13.17; no direct big-class capacity application."
    },
    {
      "source": "BJ-v4",
      "url": "https://arxiv.org/pdf/1801.08229v4",
      "name": "capacity-polar-detection",
      "file": "sources/units/BJ-v4-capacity-polar-detection.txt",
      "map": "sources/units/BJ-v4-capacity-polar-detection.map.json",
      "renderer_start": 3863,
      "renderer_end": 3898,
      "local_lf_start": 1,
      "local_lf_end": 36,
      "missing": [],
      "sha256": "110d4905ab899d0473f867cd945194f44ba48876ea6d1aa7eaa745afd0c23058",
      "application": "Theorem 4.45 complete statement and proof, actual ample domain."
    },
    {
      "source": "BJ-v4",
      "url": "https://arxiv.org/pdf/1801.08229v4",
      "name": "choquet-full-proof",
      "file": "sources/units/BJ-v4-choquet-full-proof.txt",
      "map": "sources/units/BJ-v4-choquet-full-proof.map.json",
      "renderer_start": 10092,
      "renderer_end": 10108,
      "local_lf_start": 1,
      "local_lf_end": 17,
      "missing": [],
      "sha256": "4378a8b5b97fb355164a8a79b6ddeef85559942f56d1ad76a112d5ea1178f78b",
      "application": "Corollary 12.22 complete statement/proof; source does not assume countable k."
    },
    {
      "source": "BJ-v4",
      "url": "https://arxiv.org/pdf/1801.08229v4",
      "name": "outer-capacity-full-proof",
      "file": "sources/units/BJ-v4-outer-capacity-full-proof.txt",
      "map": "sources/units/BJ-v4-outer-capacity-full-proof.map.json",
      "renderer_start": 10738,
      "renderer_end": 10847,
      "local_lf_start": 1,
      "local_lf_end": 110,
      "missing": [],
      "sha256": "967883b2182a6698697122d43a4b3167e6559ac384e179909c03379d7ab22dcc",
      "application": "Theorem 13.26 and pertinent lemmata/proofs; ancillary source audit."
    },
    {
      "source": "ADD-v2",
      "url": "https://arxiv.org/pdf/2206.07183v2",
      "name": "bounded-section-density-full-proof",
      "file": "sources/units/ADD-v2-bounded-section-density-full-proof.txt",
      "map": "sources/units/ADD-v2-bounded-section-density-full-proof.map.json",
      "renderer_start": 128,
      "renderer_end": 183,
      "local_lf_start": 1,
      "local_lf_end": 56,
      "missing": [],
      "sha256": "cd7d3081cc7ecf863d039a56046615b9c6bbc89944293f56dd9dd0c601d4c1c2",
      "application": "Matching source reading; our proof does not import general nonample closure."
    }
  ],
  "independently_acquired_response_files": [
    {
      "file": "sources/capacity.json",
      "sha256": "94f4769a7f4508e6ae6348717d2997ef8b1dad76dc8e7fde6b2cc66453485a64",
      "acquisition": "Independently retrieved public primary MCP response in this fresh workspace; literal renderer labels preserved"
    },
    {
      "file": "sources/cone_sources.json",
      "sha256": "2fef433f33193b3132194f094fadf2896be9e85fc71dd86e4275599cda586b34",
      "acquisition": "Independently retrieved public primary MCP response in this fresh workspace; literal renderer labels preserved"
    },
    {
      "file": "sources/find.json",
      "sha256": "b1347fb7ae94517e536557fd10fd83968864dfbe77e0a5ff7e156d6d5b2f48b3",
      "acquisition": "Independently retrieved public primary MCP response in this fresh workspace; literal renderer labels preserved"
    },
    {
      "file": "sources/initial.json",
      "sha256": "9e69a158a9fe5c67cb1e3381e63bda507773cf48638690011b4481570d22bac7",
      "acquisition": "Independently retrieved public primary MCP response in this fresh workspace; literal renderer labels preserved"
    },
    {
      "file": "sources/neglig.json",
      "sha256": "b3ad216d1235624c44266d65b52478d908127fe903e00b8439ff9311f90015da",
      "acquisition": "Independently retrieved public primary MCP response in this fresh workspace; literal renderer labels preserved"
    },
    {
      "file": "sources/neglig_antecedents.json",
      "sha256": "80d128cb6cb4e296efd1124c0da49f32a3db20a4098e3cc39af968727da07b2f",
      "acquisition": "Independently retrieved public primary MCP response in this fresh workspace; literal renderer labels preserved"
    },
    {
      "file": "sources/proofs.json",
      "sha256": "c7c40cd843257f02e6b4c249464133715be700250b4eba1053dac2f7c7ad824e",
      "acquisition": "Independently retrieved public primary MCP response in this fresh workspace; literal renderer labels preserved"
    }
  ],
  "essential_external_applications": [
    {
      "index": 0,
      "claim": "An ample raw supremum has no divisorial discrepancy, permitting closedness of the reconstructed normalized big cone",
      "statement_and_proof": "BJ-v4-nonnegligibility-full-proof",
      "scope": "Only the common ACTUAL ample cone; literal tensor embedding precedes application; entire theorem proof and finite separator lemma read"
    },
    {
      "index": 1,
      "claim": "Every actual ample negligible subset is covered by an ample psh pole",
      "statement_and_proof": "BJ-v4-negligible-polar-full-proof",
      "scope": "X irreducible, Omega actual ample and EP from G0; complete Theorem 13.17 and Lemma 13.19 proofs read; all-point raw identification independently proved before application"
    }
  ],
  "ancillary_readings": "Complete selected polar detection, Choquet, capacity/quasicontinuity/comparison and outer-capacity units; no claim of recursive reading of every cited theorem. Addendum density unit source matching only, not a nonample closure premise.",
  "new_proof_drafts": [
    "Actual single-net ample embedding with supported poles",
    "Bounded section minorants and first genuine G1 model envelope",
    "Weakened pole floor plus positive guard flatten decreasing families into one FS net",
    "Usc envelopes and normalized big compactness",
    "Exact all-point raw-sup and regularization identification; actual tensor pole return",
    "Conditional E1 pole series and non-Borel negligible outer nullness",
    "All-dimension finite raw polarization and its explicit missing barycenter hypotheses",
    "Blowup section-count obstruction to ordinary big-volume interpolation",
    "Numerical-zero cone and raw zero equation"
  ],
  "ordinary_background_not_recursively_reproved": [
    "Kodaira ample-plus-effective decomposition",
    "Numerical invariance and openness of ampleness, eventual generation",
    "Equivariant smooth model resolution and actual rational Cartier model representation",
    "Finite intersection theory, nef positivity and component coefficient formulas",
    "Compact Hausdorff normality and regular Borel measure facts"
  ],
  "unproved_conditions": "Whole genuine scalar energy and contraction; complete moving/barycenter compatibility; full operator/unbounded mixed and physical weighted identification; all E1 output integrability; attainment, every-solution uniqueness and genuine strict comparison; any additional nonzero zero-volume range",
  "whole_primary_papers_read": false,
  "recursive_background_proofs_read": false,
  "coordinate_convention": "Inclusive one-based LF in saved UTF-8 units; original zero-based renderer labels and PDF page labels retained separately",
  "original_pdf_download_claim": false,
  "supervised_compute_service": "Not exposed; no resource-heavy calculation launched",
  "mathematical_certification": false
}

END COMPLETE MATHEMATICAL BODY

BEGIN COMPLETE MATHEMATICAL BODY WHOLE201
\documentclass[11pt]{article}
\usepackage[a4paper,margin=26mm]{geometry}
\usepackage{amsmath,amssymb,amsthm,mathrsfs,hyperref}
\setlength{\emergencystretch}{3em}
\newtheorem{theorem}{Theorem}
\newtheorem{lemma}[theorem]{Lemma}
\newtheorem{proposition}[theorem]{Proposition}
\newcommand{\MA}{\operatorname{MA}}
\newcommand{\EE}{\mathcal E^1_\theta}
\newcommand{\vol}{\operatorname{vol}}
\title{Strict Borel locality from bounded moving maxima\protect\\
and fixed continuous ramps}
\author{Unreviewed conditional research, continuation 201}
\date{6 October 2026}
\begin{document}
\maketitle
\begin{abstract}
For a big rational bundle, we give a conditional route from its finite-list
complete moving systems to strict locality for every original finite-energy
pair. A moving maximum is identified by an energy squeeze against canonical
majorants. A fixed base twist gives uniform algebraic collars and fixed-test
quadratic bounds, so the squeeze also identifies its raw measure.
Finite nef locality follows from finite ample locality. For unbounded pairs,
fixed continuous ramps select the winning region; uniform ordered
finite-energy errors control the incorrect selections before either limit.
This proves a strict Borel comparison inequality without assuming that the
winning region is open. A separate convex-series argument proves nullness
of poles of every genuine plurisubharmonic function. The genuine scalar and
moving foundations, and the absolute midpoint modulus used for the ordered
errors, remain explicit unproved antecedents. This paper does not identify
all unbounded mixed approximations or all negligible sets and does not
solve original P16.5.
\end{abstract}

\section{Original domain and explicit conditional inputs}
Let $X$ be any smooth integral projective $n$-fold, $n\geq1$, over any
algebraically closed trivially valued characteristic-zero field.
Let $L$ be any actual big rational line bundle, $\theta=c_1(L)$,
$K=X^{\mathrm{an}}$, and $V=\vol(L)>0$.
The genuine cone is the all-point single decreasing FS-net cone on
varying actual bundles with numerical classes tending to $\theta$.
No supported semivaluations are removed. Normalize at the generic trivial
valuation $v_0$ and put $R=P_\theta(0)$ and $B(u)=-E(u)$.
Choose an actual Kodaira identity $L=aA+E_0$, $A$ ample, $E_0$ effective;
write $Z=E_0^{\mathrm{an}}$ and $U=K\setminus Z$.
Clear rational powers before using any sections or ideals.

All results below are conditional on the following whole package.
It is mathematical proof data, not an accepted theorem.
\begin{enumerate}
\item[(S)] The literal genuine cone is convex, finite-max and decreasing
closed at finite generic endpoints and admits genuine all-point envelopes.
Its normalized space is compact in the divisorial-coordinate topology.
The whole outer full-section energy is
\[
 E(u)=\inf_{f\in C(K),\,f\geq u}\mathscr E(f),
 \qquad E(P_\theta(f))=\mathscr E(f).
\]
It is concave, monotone, weakly upper semicontinuous, decreasing-net
continuous and $V$-translation equivariant, with $E(R)=0$.
Every normalized $u\in\EE$ has nonpositive rational original model
majorants $f_i\downarrow u$, with $f_i(v_0)=0$ and
$P_\theta(f_i)\downarrow u$ with decreasing energies.
Perturbed canonical envelopes have the same decreasing continuity.
Every normalized genuine function is at most $R\leq0$.
\item[(M)] A target-independent map $M:\EE\to\mathcal M^+(K)$ has
raw mass $V$, is constant invariant, agrees at model envelopes with
the finite divisorial derivative of $\mathscr E$, has weak canonical
decreasing convergence, and gives $Z$ zero mass.
For every finite list of model obstacles, the complete moving systems
have common actual data $p_m^*L=A_m+T_m$, with $mA_m$ generated
and $mT_m$ effective. Their physical stages and bounded rational
relatively generated model quotients satisfy
\[
 \phi_{m,f}=q_{T_m}+\psi_{m,f},\qquad
 \phi_{m,0}=q_{T_m},\qquad A_m^n\longrightarrow V .
\]
The physical stage is at most $P_\theta(f)$ on all lifts.
The auxiliary energy tends to $E(P_\theta(f))$ and its pushed raw
measure tends weakly to $M(P_\theta(f))$; its generic value tends to zero.
The full auxiliary section trace is its finite intersection energy.
Multiplication by the actual $T_m$ section injects the full auxiliary
section space into the full original one in cleared degrees.
The quotients converge uniformly on compact subsets of $U$ to
$P_\theta(f)-R$. For a nonpositive bounded model obstacle they lie
between its minimum, with a vanishing floor error, and zero.
\item[(A)] Every genuine relative finite-energy test is integrable at
every output. With $\alpha=2^{-n}$ and
$\delta(u,v)=E((u+v)/2)-(E(u)+E(v))/2$, the absolute midpoint estimate is
\[
 \int_U|u-v|\,dM(w)
 \leq C_n\delta(u,v)^\alpha B(w)^{1/2}
       \max\{B(u),B(v),B(w)\}^{1/2-\alpha}.                 \tag{1}
\]
When $n=1$ the last exponent-zero factor is omitted.
The uniform finite-model Taylor estimate passes as a whole fixed
increment to every genuine base and gives both original continuous
derivatives of $E(P_\theta(u+th))$ equal to $\int h\,dM(u)$.
\item[(C)] Genuine relative contraction satisfies
$B((1-r)R+ru)\leq C_n r^2B(u)$ for $0<r<1$.
\end{enumerate}
These are respectively the explicitly unproved scalar and moving
package and the conditional conclusions reconstructed in the completed
round159 paper, Sections 5--10. Continuation200 gives another unreviewed
conditional construction. Neither body is a caller grant.
Here the only accepted NA input is G0 in its actual \emph{ample} domain,
used below only for finite bounded ample locality and original model
testing. Ordinary resolution, nef intersection theory, algebraic positive
products and volume differentiation, and compact Hausdorff Radon facts
are distinguished background.

For clarity, an intrinsic finite-dual-energy target is a positive Radon
measure of raw mass $V$, missing $\{R=-\infty\}$, integrating every
$R-u$, $u\in\EE$, and with
$\sup_{u(v_0)=0}(E(u)+\int(R-u)d\nu)<\infty$.
The pole argument at the end applies to such targets too.

\section{Uniform collars for bounded auxiliary models}
Fix a positive integer $C$ and auxiliary models $\xi$ satisfying
$-C\leq\xi\leq0$ on the generated $A_m$.
Their defining lattice may be taken with all time weights in $[-mC,0]$.
After clearing degrees and resolving its base ideal, a single fixed
integer $c>C+1$ makes
\[
 \Gamma_\xi(c)=p^*L-T_m+D_\xi+cF
\]
globally generated and hence nef on its compactified model.
Here $F$ is the full fiber, with every central multiplicity.
Indeed on the zero chart the weighted section system generates the
resolved lattice; on the infinity chart it is the generated generic
bundle. Twisting by $\mathcal O_{\mathbb P^1}(mc)$ supplies all
monomials between the two charts, since each interval of exponents
has length at least $m(c-C)>0$. This constructs a generating system
on both charts, not merely relative nefness.
The same argument applies to the maximum of two such scalars:
take the union of their weighted generating systems and principalize
its actual ideal. All weights remain in $[-mC,0]$.
In effective order, on every common refinement,
\[
 0\leq\Gamma_\xi(c)\leq\gamma:=p^*L+cF.                  \tag{2}
\]
The right class is big on the fixed product determination; the
horizontal $T_m$ and $-D_\xi$ account for the difference.
For each fixed $m$, this global twist also identifies the full
auxiliary section-volume intercept with $e_{A_m}(\xi)$:
large twists are nef, their volume is their ordinary top intersection,
and its affine fiber term is $cA_m^n$. Thus this finite trace equality
applies to the new maximum as well as to the supplied endpoint models.

\begin{lemma}[Algebraic collars and fixed quadratic tests]\label{collars}
For any fixed actual effective Cartier divisor $S$ on $X$, there is
$C_{S,c}$ independent of $m$ and of these auxiliary models such that
\[
 \int v(S)\,d\MA_{A_m,\mathrm{raw}}(\xi)\leq C_{S,c}.     \tag{3}
\]
After pushforward every weak limit gives $S^{\mathrm{an}}$ zero mass.
For any fixed original rational model test $h=f_H$, its quadratic form
in any $n-1$ of these auxiliary slots is bounded by a constant
$C_{h,c}$ independent of their refinements and $m$.
\end{lemma}
\begin{proof}
On a common SNC determination write $F=\sum_Eb_EE$.
The vertical part of the pulled $S$ has coefficient $b_Ev_E(S)$.
The raw measure coefficient is $b_E(\Gamma_\xi(c)|_E)^n$:
adding $cF$ does not change a central restriction.
The horizontal part of the pulled effective $S$ is effective.
Nef positivity therefore gives
\[
 \int v(S)\,d\MA(\xi)
 \leq \Gamma_\xi(c)^n\,p^*S.
\]
Choose one fixed ample $T$ on a smooth determination and $d$ with
$dT-p^*S$ nef. Algebraic positive-product order and (2) imply
\[
 \Gamma_\xi(c)^n p^*S
 \leq d\Gamma_\xi(c)^n T
 \leq d\langle\gamma^n\rangle T .
\]
Only fixed nef tests are paired with effective-order inequalities.
This proves (3), also for nef classes on the boundary by nef continuity.
The original capped functions $\min(v(S),N)$ are continuous on $K$.
Weak convergence and (3) bound each limiting cap integral by $C_{S,c}$.
Thus the mass of $S^{\mathrm{an}}$, where every cap is $N$, is at most
$C_{S,c}/N$, and is zero. Before any limit the same caps bound the
mass of the collar $\{v(S)\geq N\}$ by $C_{S,c}/N$.

For the quadratic claim choose a single determination carrying $H$.
Write $H=H_1-H_2$ with two \emph{fixed} globally nef Cartier classes,
for example $H_1=aT+H$ and $H_2=aT$ for sufficiently large $a$.
For $\Lambda$ a product of $n-1$ auxiliary slots,
\[
 |-H^2\Lambda|
 \leq\sum_{k,l=1}^2 H_kH_l\Lambda
 \leq\sum_{k,l=1}^2\langle\gamma^{n-1}\rangle H_kH_l .
                                                               \tag{4}
\]
The slots can be replaced by their twists $\Gamma_\xi(c)$ because
every term containing $F$ in a vertical quadratic intersection is zero.
Each term in the middle expression is nonnegative; positive-product
order is used only against the fixed nef products $H_kH_l$.
All choices precede the moving model. For $n=1$ the product is empty
and (4) is an ordinary fixed intersection bound.
\end{proof}

\section{Identifying the bounded moving maximum}
Fix normalized model envelopes $a=P_\theta(f)$ and $b=P_\theta(g)$
of nonpositive model obstacles. Let
\[
 w=\max(a,b),\qquad
 \rho_m=\max(\psi_{m,f},\psi_{m,g}).
\]
The maximum is an actual relatively generated scalar on the same $A_m$.
On the whole pulled carrier its physical stage is
$q_{T_m}+\rho_m=\max(\phi_{m,f},\phi_{m,g})\leq w$.
Choose one integer $C$ so that all endpoint quotient weights and $\rho_m$
lie in $[-C,0]$ and $R-C\leq w\leq R$.
No equality $w=P_\theta(\max(f,g))$ is assumed.

\begin{lemma}[Trace inequality]\label{trace}
For every fixed continuous original majorant $h\geq w$,
\[
 \mathscr E(h)\geq e_{A_m}(\rho_m)
                    +(\min_Kh)(V-A_m^n).               \tag{5}
\]
Consequently $E(w)\geq\limsup_m e_{A_m}(\rho_m)$.
\end{lemma}
\begin{proof}
At fixed $m$ multiply the full auxiliary section system in degree
$\ell A_m$ by the actual $\ell T_m$ section.
Its $h$ filtration weights are at least the weights of $\rho_m$,
because its physical scalar is at most $h$ at every lift.
At supported zero branches the original section expression is
$+\infty$ and cannot lower the weight infimum.
Extend an adapted basis of this injected subspace to a full
original filtered basis. Every remaining weight is at least
$\ell\min_Kh$. First take the degree $\ell$ to infinity at this
fixed $m,h$; the bounded generated-nef trace gives (5).
The floor error divided by $\ell$ tends to zero.
Only after that limit let $m$ tend cofinally to infinity, still with
the same finite $h$. The retained, possibly negative,
$(\min h)(V-A_m^n)$ then vanishes.
Finally take the outer infimum over $h$. No physical stage is
assigned membership in the original $\EE$.
\end{proof}

\begin{theorem}[Bounded maximum energy and measure]\label{maxlimit}
Under (S)--(M),
\[
 e_{A_m}(\rho_m)\longrightarrow E(w),\qquad
 p_{m*}\MA_{A_m,\mathrm{raw}}(\rho_m)\longrightarrow M(w)
                                                        \tag{6}
\]
weakly on the original $K$.
\end{theorem}
\begin{proof}
Take canonical original model majorants $h_j\downarrow w$ and
$w_j=P_\theta(h_j)\downarrow w$.
For fixed $j$ put $\sigma_{m,j}=\psi_{m,h_j}$.
The full filtration order gives $\sigma_{m,j}\geq\rho_m$.
Moreover \emph{the same} $C$ bounds all these $\sigma_{m,j}$:
$h_j\geq w\geq R-C\geq\phi_{m,0}-C$.
Every full original section has zero-obstacle weight zero and its
scalar is at most $\phi_{m,0}$. Thus every $h_j$ weight is at least
$-mC$; its generic upper bound is zero.
Integer $C$ removes a floor error. No bound for $\|h_j\|_\infty$
uniform in $j$ is needed.

The measures of $\rho_m$ have converging raw masses $A_m^n\to V$.
Their energies are bounded above and below: monotonicity bounds them
below by the energy of either endpoint, and all normalized quotient
energies are at most zero. Take any joint convergent subnet with
measure limit $\nu$ and energy limit $e_*$. Lemma~\ref{collars},
with a cleared $E_0$, gives $\nu(Z)=0$.
Finite concavity at the lower potential gives, for fixed $j$,
\[
 0\leq e_{A_m}(\sigma_{m,j})-e_{A_m}(\rho_m)
       \leq\int(\sigma_{m,j}-\rho_m)\,d\MA_{A_m}(\rho_m).
                                                               \tag{7}
\]
On every compact subset of $U$ the changing test tends uniformly
to $w_j-w$. It is between zero and $C$.
Fix a continuous collar in $U$ before taking the subnet; its omitted
mass can be made arbitrarily small using $\nu(Z)=0$ and weak
convergence. This passes the right integral of (7), so
\[
 E(w_j)-e_*\leq\int_U(w_j-w)\,d\nu .
\]
The continuous bounded differences decrease to zero on $U$.
Compact Dini convergence on a fixed collar, followed by its omitted
Radon mass, gives convergence of the last integral to zero even for
the directed $j$ net. Decreasing energy continuity gives
$E(w)\leq e_*$. Lemma~\ref{trace} gives the reverse inequality.
Every joint cluster therefore has energy $E(w)$.

To identify its measure, retain one fixed rational original model
test $h=f_H$. On a common refinement the finite ordered energy gap
$\Delta_{m,j}=e(\sigma_{m,j})-e(\rho_m)$ controls
\[
 I_{m,j}:=\int(\sigma_{m,j}-\rho_m)
                   \,d(\MA(\rho_m)-\MA(\sigma_{m,j}))
        \leq(n+1)\Delta_{m,j}.                           \tag{8}
\]
Indeed the finite energy telescoping sum has $n+1$ nonnegative
terms; its first term is $\int(\sigma-\rho)d\MA(\rho)$.
Subtracting the nonnegative integral at $\sigma$ gives (8).
The same telescoping expresses $I_{m,j}$ as the sum of the
nonnegative mixed quadratic forms of $\sigma-\rho$.
Cauchy--Schwarz in those forms, and the fixed bound (4), therefore give
\[
 \left|\int h\,d(\MA(\rho_m)-\MA(\sigma_{m,j}))\right|
       \leq C_{h,c}\sqrt{\Delta_{m,j}}.                  \tag{9}
\]
This constant is independent of both $j$ and $m$.
At fixed $j$ take the subnet limit, using (M):
\[
 |\nu(h)-M(w_j)(h)|
       \leq C_{h,c}\sqrt{E(w_j)-E(w)}.
\]
Then take $j$ to its endpoint. Canonical weak convergence in (M)
gives $\nu(h)=M(w)(h)$. Model functions are uniformly dense in
$C(K)$, and masses agree, so this identifies $\nu$.
Compactness of bounded-mass Radon measures and uniqueness of all
clusters prove the whole weak limit (6).
\end{proof}

\section{Finite nef locality and bounded original locality}
Finite bounded relatively nef models on an actual nef $A$ satisfy
strict-winning locality. To see this within the exact G0 grant,
choose an actual ample $H$ on the generic carrier and add the same
zero metric in class $\epsilon H$ to both scalar models and their
maximum. Their actual generic bundle $A+\epsilon H$ is ample.
G0 finite ample locality applies; the winning scalar inequality
is unchanged. On each fixed common determination the raw measures
are finite polynomials in $\epsilon$, with every central multiplicity.
Let rational $\epsilon\downarrow0$. Positivity and the finite
coefficient formulas give the asserted finite nef identity.
This passage imports no unbounded ample estimate.

For $a,b,w$ of the previous section and a continuous original test
$h$ with compact support in $\{a>b\}\cap U$, compactness gives a
positive minimum for $a-b$ on that support.
The moving quotient gap converges uniformly there, so
$\psi_{m,f}>\psi_{m,g}$ at every pushed atom where $h$ is nonzero,
eventually. Finite nef locality gives equality of the $h$ integrals
of $\MA(\rho_m)$ and $\MA(\psi_{m,f})$.
Pass both weak limits using (6) and (M).
Radon uniqueness on the open subset of $U$ yields
\[
 \mathbf1_{\{a>b\}\cap U}M(\max(a,b))
       =\mathbf1_{\{a>b\}\cap U}M(a).                   \tag{10}
\]
The analogous identity holds where $b>a$.
The bounded winner is open in $U$ because these model envelopes are
continuous there. The unbounded extension below will not use
openness of its winner.

\section{All decreasing bases and uniformly small ordered errors}
\begin{lemma}[Decreasing weak continuity]\label{decreasing}
Under (S)--(M)--(A), every genuine decreasing net
$u_i\downarrow u\in\EE$ has $M(u_i)\to M(u)$ weakly.
\end{lemma}
\begin{proof}
For fixed $h\in C(K)$ and fixed $t$, the envelopes
$P_\theta(u_i+th)$ decrease to $P_\theta(u+th)$.
Their decreasing endpoint is genuine by (S), is below $u+th$
at every original point, and is above its envelope; hence it equals
that envelope. Its generic endpoint is finite because it lies
between $u\pm|t|\|h\|_\infty$.
Their energies converge decreasingly.
The concave functions $H_i(t)=E(P_\theta(u_i+th))$ thus converge
at each fixed $t$ to $H(t)$.
Their derivatives at zero are $\int h\,dM(u_i)$ by (A).
For $t>0$, the two secants at $-t,0,t$ bracket each such derivative.
First take the net limit at this fixed $t$, then let $t\downarrow0$.
Both derivative signs of $H$ agree by (A), so the bracket shrinks
to $\int h\,dM(u)$. This is weak convergence on the original $K$.
\end{proof}

For any canonical majorants $a_j\downarrow u$, monotonicity gives
\[
 0\leq\delta(a_j,u)\leq\frac{E(a_j)-E(u)}2.
\]
Consequently (1) gives numbers $\eta_j(D)\downarrow0$ such that
\[
 \sup_{B(z)\leq D}\int_U(a_j-u)\,dM(z)
       \leq\eta_j(D).                                  \tag{11}
\]
For example use (1) with $B(a_j)\leq B(u)$ and the displayed
energy gap. This is a uniform estimate for the \emph{fixed} test
majorant error against every output of cost at most $D$.
It follows from the absolute modulus, not from weak convergence
of any indicator.

\section{Strict Borel locality for all genuine pairs}
\begin{theorem}[Strict Borel locality]\label{borel}
Under the explicit inputs (S)--(M)--(A), every normalized
$u,v\in\EE$ satisfies
\[
 \mathbf1_{\{u>v\}}M(\max(u,v))
       =\mathbf1_{\{u>v\}}M(u),\qquad
 \mathbf1_{\{v>u\}}M(\max(u,v))
       =\mathbf1_{\{v>u\}}M(v).                         \tag{12}
\]
These are identities of original Borel measures.
\end{theorem}
\begin{proof}
Take canonical model envelopes $u_i\downarrow u$, $v_i\downarrow v$
on a product-directed index and put $w_i=\max(u_i,v_i)$,
$w=\max(u,v)$. Then $w_i\downarrow w$ genuinely and all output
costs are bounded by one $D$.
Lemma~\ref{decreasing} passes $M(w_i)$ and $M(u_i)$ weakly to
$M(w)$ and $M(u)$.

Let $\beta:\mathbb R\to[0,1]$ be zero on $(-\infty,1]$,
one on $[2,\infty)$ and linear between; its Lipschitz constant is one.
Fix $h\in C(K)$ with compact support in $U$.
For a fixed model index $j$ and $\varepsilon>0$, define on $U$
\[
 b_{j,\varepsilon}=\beta((u_j-v_j)/\varepsilon).
\]
The fixed function $h b_{j,\varepsilon}$ extends continuously by zero
to $K$. If $i\geq j$, $b_{j,\varepsilon}>0$ and $u_i\leq v_i$,
then $u_j-v_j>\varepsilon$, $v_i\leq v_j$, and hence
$u_j-u_i>\varepsilon$.
On the region $u_i>v_i$, identity (10) cancels the two measures.
On its complement, the preceding inequality and (11) bound both
positive measures. Thus
\[
 \left|\int h b_{j,\varepsilon}\,d(M(w_i)-M(u_i))\right|
       \leq \frac{2\|h\|_\infty}{\varepsilon}\eta_j(D).
                                                               \tag{13}
\]
Here $u_j-u_i\leq u_j-u$; no moving set is used as a weak test.
Take $i$ to its endpoint at this fixed $j,\varepsilon$.
Weak convergence passes the fixed continuous test in (13).

At the two now fixed measures $M(w),M(u)$ define
$b_\varepsilon=\beta((u-v)/\varepsilon)$ where both relative
costs are finite. Their complements have zero mass by (A).
The Lipschitz bound gives
\[
 |b_{j,\varepsilon}-b_\varepsilon|
 \leq \varepsilon^{-1}\big((u_j-u)+(v_j-v)\big)
\]
on this full-measure set. Estimate (11), separately for the
$u$ and $v$ nets, proves absolute $L^1$ convergence at these
two fixed measures. Sending $j$ to its endpoint in (13) gives
$\int h b_\varepsilon\,d(M(w)-M(u))=0$.

Finally take an ordinary positive sequence $\varepsilon\downarrow0$.
Bounded dominated convergence at the two fixed measures gives
$b_\varepsilon\to\mathbf1_{\{u>v\}}$ almost everywhere.
Thus their restrictions to that original Borel set have equal
integrals against every compactly supported continuous test in $U$.
Radon uniqueness gives (12) on $U$; all three measures miss $Z$
by (M), so it holds on $K$. Interchange $u,v$ for the other identity.
\end{proof}

\begin{theorem}[Strict Borel comparison]
For every genuine $u,v\in\EE$, under the same conditional inputs,
\[
 \int_{\{u<v\}}dM(v)\leq\int_{\{u<v\}}dM(u).             \tag{14}
\]
\end{theorem}
\begin{proof}
For $\varepsilon>0$ let $w_\varepsilon=\max(u,v-\varepsilon)$.
Finite energy and genuine membership follow by max closure and
energy monotonicity; restore constants when needed.
By (12) and constant invariance, its measure agrees with $M(v)$
on $\{u<v-\varepsilon\}$ and with $M(u)$ on
$\{u>v-\varepsilon\}$. All raw masses are $V$. Hence
\[
 M(v)\{u<v-\varepsilon\}
 \leq V-M(u)\{u>v-\varepsilon\}
 =M(u)\{u\leq v-\varepsilon\}.
\]
Send an ordinary sequence $\varepsilon\downarrow0$.
Both sets increase to $\{u<v\}$ off the null set where a relative
cost is infinite. Finite-measure continuity from below proves (14).
No winner is assumed open, and no indicator passes through weak convergence.
\end{proof}

\section{Every genuine plurisubharmonic pole is null}
\begin{proposition}[A finite-energy pole covering]\label{polar}
Under (S)--(C), for every normalized genuine $q\in\operatorname{PSH}(\theta)$,
there is an actual $p\in\EE$ whose pole set contains
$\{q=-\infty,\ R>-\infty\}$.
Consequently every output in (A) and every intrinsic target gives
$\{q=-\infty\}$ zero mass.
\end{proposition}
\begin{proof}
Put $N_j=16^j$, $r_j=8^{-j}$ and $\lambda_j=2^{-j}$, $j\geq1$.
The genuine truncation $q_j=\max(q,R-N_j)$ lies in $\EE$ since
$R-N_j\leq q_j\leq R$, and $B(q_j)\leq VN_j$.
Set $a_j=(1-r_j)R+r_jq_j$.
Contraction gives $B(a_j)\leq C_nV4^{-j}$.
The genuine finite sums
\[
 p_m=\sum_{j=1}^m\lambda_j a_j
           +\left(1-\sum_{j=1}^m\lambda_j\right)R
\]
decrease all-point, have generic value zero, and by concavity satisfy
$E(p_m)\geq-C_nV\sum_{j\geq1}8^{-j}$.
Decreasing closure and energy continuity in (S) give a genuine
finite-energy endpoint $p$.
Where $q=-\infty$ and $R$ is finite, $R-q_j=N_j$ and hence
$R-p_m=\sum_{j=1}^m\lambda_j r_jN_j=m$.
Thus $p=-\infty$ there.
Integrability of this one actual relative finite-energy test forces
zero measure on that set for every stated measure.
The remaining set $\{R=-\infty\}$ is already null by (M), or by
the intrinsic-target definition. This proves the assertion.
\end{proof}

\section{Limits of the result and source application scope}
All positive-volume conclusions here remain \emph{conditional}.
The whole scalar and moving foundation package has not been accepted.
The absolute midpoint modulus and derivative passage are unreviewed
conditional results of the whole round159 and continuation200 bodies.
This manuscript proves the bounded moving-max energy and measure
identification and its Borel-selection argument under those explicit inputs.
It does not turn those inputs into proved foundations.

The pole result concerns genuine $\theta$-plurisubharmonic pole sets.
It does not assert that every raw-supremum negligible discrepancy is
such a pole set. A proof of the requisite negligible-set theorem remains
separate. All unbounded mixed products, simultaneously changing physical
weighted approximations, their independence and their equality with this
outer map remain separate original obligations. No additional zero-volume
range is established by this positive-volume paper.
Original P16.5 therefore remains open; this draft has no independent
acceptance and causes no change to the solved-original count.

G0's complete supplied actual ample locality unit, inclusive saved
LF260--335, was read with its retained finite component coefficient
formula and complete locality/comparison statement. Only its bounded
finite ample assertion is applied here; a finite polynomial limit
handles nef models. The fixed-nef positive-product comparisons use the
ordinary algebraic BFJ theory with its characteristic-zero hypotheses,
not an unbounded big-class NA equation.
The complete saved BFJ v2 positive-product unit, inclusive LF1--132,
and volume/differentiation unit LF1--101 were read for this application.
Their original renderer coordinates are 310--441 and 445--545.
They include the nef agreement and characterization by dominated nef
competitors used in (2)--(4); no multilinearity of big positive
products is asserted.
The trace inequality (5), uniform base-twist generation, ordered
finite gap (8), fixed ramp estimate (13), and convex pole series are
proved above. The related whole unreviewed manuscript bodies have
been read; their source ledgers are provenance, not primary reading.
No new original PDF-byte hash, whole-primary reading, or recursive
background proof reading is claimed.

\begin{thebibliography}{9}
\bibitem{BJ} S. Boucksom and M. Jonsson,
\emph{Global pluripotential theory over a trivially valued field},
\href{https://arxiv.org/pdf/1801.08229v4}{arXiv:1801.08229v4}.
\bibitem{BFJ} S. Boucksom, C. Favre and M. Jonsson,
\emph{Differentiability of volumes of divisors and a problem of Teissier},
\href{https://arxiv.org/html/math/0608260v2}{arXiv:math/0608260v2}.
\end{thebibliography}
\end{document}

END COMPLETE MATHEMATICAL BODY

BEGIN COMPLETE MATHEMATICAL BODY 201 OWN APPLICATION LEDGER
{
  "recorded_utc": "2026-10-06T12:23:03.284357+00:00",
  "classification": "Unreviewed conditional201, no original closure or independent acceptance.",
  "final_tex_sha256": "321db9ceb2877ce22820490ba7dfb9ef3703c39ec4cba4d7b2768876c7c91508",
  "whole_final_source_root_read": true,
  "whole_final_source_read_chunks": [
    "1-225",
    "226-450",
    "451-end"
  ],
  "actual_visual_pages": [
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8
  ],
  "explicit_unproved_package": "S whole genuine scalar cone/envelope/energy; M original output and finite-list full moving compatibility; A whole absolute midpoint modulus/continuous derivatives; C genuine contraction.",
  "conditional_proof_data": [
    {
      "file": "/workspace/research/root-checks/public-P16.5-round159-partial-conditional-attainment-reader/paper.tex",
      "sha256": "678a18615d419117e65a01de1ff6059e5d9478c457edae509a0608f3a5e54e55",
      "whole_body_root_read": true,
      "authority": "Unreviewed complete conditional manuscript; not a theorem grant."
    },
    {
      "file": "/workspace/research/root-checks/P16.5-absolute-Hodge-estimate-and-genuine-variational-attainment-candidate-20261006-continuation200.tex",
      "sha256": "28882f205280c492cd638063d2e45fca8dd6f204c5387bb93fcae91ea34a1b9d",
      "whole_body_root_read": true,
      "authority": "Unreviewed complete conditional manuscript; not a theorem grant."
    }
  ],
  "accepted_G0_application": {
    "file": "/workspace/research/campaigns/round-151/P16.5-original-big-class-entire-equation-generation-moving-trace-retry1/artifacts/codex-8Ar6As/supplied/G0.txt",
    "sha256": "d15e65b4baea444e13693c2de69c682d0ff0e2e251e45d56a77c840d0bc3959f",
    "whole_applied_saved_LF_unit": [
      260,
      335
    ],
    "whole_applied_unit_root_read": true,
    "scope": "Only bounded finite actual ample locality and retained component coefficient formula; finite polynomial ample perturbation to nef, no unbounded nonample transfer."
  },
  "new_proofs": [
    "Fixed base twist globally generates every bounded weighted auxiliary system and its actual maximum, uniformly over moving models; all multiplicities retained.",
    "Fixed-nef algebraic positive-product bounds supply uniform section-divisor caps/collars and signed fixed-test quadratic forms.",
    "Actual generic-factor injection retains (min h)(V-A_m^n) through degree, moving and outer-majorant limit orders.",
    "For bounded genuine model-envelope maximum, canonical dominating full systems, uniform collars and concavity prove exact auxiliary energy; finite ordered gap and uniform fixed Hodge bounds identify its raw weak measure.",
    "Finite nef locality follows only finite ample locality by a common zero ample perturbation and finite polynomial limit.",
    "Genuine decreasing weak output continuity follows original continuous energy secant brackets.",
    "Fixed original continuous ramps select strict winner; uniform ordered absolute errors bound incorrect selection before weak limit, majorant limit and ordinary ramp-width limit. This proves strict original Borel locality and raw comparison without openness of winner.",
    "Truncations, genuine quadratic contraction and actual convex-series energy continuity make one E1 pole containing every genuine PSH pole outside reference poles."
  ],
  "whole_pertinent_primary_units": [
    {
      "source": "BFJ arXiv:math/0608260v2",
      "url": "https://arxiv.org/html/math/0608260v2",
      "file": "/workspace/research/campaigns/round-159/P16.5-original-equation-after-arbitrary-target-output-approximation/artifacts/codex-0lpuxa/sources/units/BFJ-v2-positive-products.txt",
      "sha256": "6c15466488dfc98ca2b08915a967e744399ae3309639ca9c3d543d686f895c8a",
      "inclusive_local_LF": [
        1,
        132
      ],
      "inclusive_original_renderer": [
        310,
        441
      ],
      "whole_pertinent_unit_root_read": true,
      "application": "Ordinary algebraic nef agreement/dominated-nef characterization, fixed-nef test order and finite nef section-volume trace; no unbounded nonample NA grant."
    },
    {
      "source": "BFJ arXiv:math/0608260v2",
      "url": "https://arxiv.org/html/math/0608260v2",
      "file": "/workspace/research/campaigns/round-159/P16.5-original-equation-after-arbitrary-target-output-approximation/artifacts/codex-0lpuxa/sources/units/BFJ-v2-volume-differentiation.txt",
      "sha256": "8651090225d1a0201460f316a49cd69fc8a7734a1a9d4dc29ded54b60aaf1c47",
      "inclusive_local_LF": [
        1,
        101
      ],
      "inclusive_original_renderer": [
        445,
        545
      ],
      "whole_pertinent_unit_root_read": true,
      "application": "Ordinary algebraic nef agreement/dominated-nef characterization, fixed-nef test order and finite nef section-volume trace; no unbounded nonample NA grant."
    }
  ],
  "whole_primary_sources_read": false,
  "all_recursive_primary_foundations_read": false,
  "original_pdf_byte_hash_claim": false,
  "primary_quotations_republished": false,
  "independent_acceptance": false,
  "original_closed": false,
  "accepted_paper_count_unchanged": 59,
  "remaining": "All antecedents still unreviewed; all unbounded mixed/physical weighted identification and independence, every nonpolar negligible discrepancy, additional nonzero zero-volume range.",
  "active_private_outputs_read": false,
  "hot_feedback_sent": false
}

END COMPLETE MATHEMATICAL BODY

BEGIN COMPLETE MATHEMATICAL BODY WHOLE202
\documentclass[11pt]{article}
\usepackage[a4paper,margin=26mm]{geometry}
\usepackage{amsmath,amssymb,amsthm,mathrsfs,hyperref}
\setlength{\emergencystretch}{3em}
\newtheorem{theorem}{Theorem}
\newtheorem{lemma}[theorem]{Lemma}
\newtheorem{proposition}[theorem]{Proposition}
\newcommand{\MA}{\operatorname{MA}}
\newcommand{\EE}{\mathcal E^1_\theta}
\newcommand{\vol}{\operatorname{vol}}
\title{Filtered quotient traces and genuine mixed measures\protect\\
under the explicit scalar and output foundations}
\author{Unreviewed conditional research, continuation 202}
\date{6 October 2026}
\begin{document}
\maketitle
\begin{abstract}
A full original filtered section space and an injected auxiliary
subspace have an exact quotient filtration. Its trace has Lipschitz
constant equal to the missing raw volume; at model obstacles its
derivative is a positive measure of precisely that missing mass.
Under explicit unproved genuine scalar and output foundations,
this finite statement identifies any uniformly bounded generated
moving quotient converging locally to a bounded relative genuine
function. Genuine floors give the energy squeeze, and full/subspace
derivative comparison gives the measure squeeze.
In particular the construction applies to rational convex combinations
of bounded model envelopes. Finite polynomial interpolation then defines
positive symmetric mixed measures on the entire genuine finite-energy
space and proves canonical decreasing weighted continuity.
All results involving that genuine space remain conditional.
The paper does not identify every simultaneously unbounded physical
approximation or all negligible sets; original P16.5 remains open.
\end{abstract}

\section{Domain, conventions and explicit antecedents}
Retain every smooth integral projective $n$-fold $X$, $n\geq1$, over
every algebraically closed trivially valued characteristic-zero field,
every actual big rational bundle $L$, the original carrier
$K=X^{\mathrm{an}}$, and raw volume $V=\vol(L)>0$.
Clear rational degrees before sections, divisors or ideals are used.
The genuine cone is the original all-point single decreasing FS-net
cone on varying actual bundles. It is not replaced by a completion
or by functions only on divisorial points.

The following input package is \emph{unproved in this paper}.
It is the complete S--M package and its conditional conclusions
in the whole completed round159 paper; no author body is a caller grant.
\begin{enumerate}
\item Genuine convex, finite-max and decreasing closure, all-point
envelopes and normalized divisorial compactness hold. The reference
$R=P_\theta(0)$ has generic value zero and dominates every normalized
genuine function. The whole outer energy
$E(u)=\inf_{f\in C(K),f\geq u}\mathscr E(f)$ is concave, monotone,
weakly upper semicontinuous, decreasing-net continuous and
$V$-translation equivariant, with $E(R)=0$ and
$E(P_\theta(f))=\mathscr E(f)$. Every actual finite-energy
$u$ has canonical nonpositive rational model majorants and their
envelopes decrease to $u$ with decreasing energies.
\item A target-independent original map $M$ on every actual $\EE$
has positive Radon outputs of raw mass $V$, constant invariance,
finite divisorial model-envelope compatibility, canonical weak
convergence and algebraic-divisor nullness.
The complete finite-list moving systems have actual common factors
$p_m^*L=A_m+T_m$, with $A_m$ generated in cleared degree,
$T_m$ effective, and $A_m^n\to V$.
Their physical stages are $q_{T_m}+\psi_{m,f}\leq P_\theta(f)$,
their auxiliary energies and pushed measures have the stipulated
finite-obstacle limits, and their quotients converge uniformly
on compact subsets of $U$ to $P_\theta(f)-R$.
Here $U=K\setminus Z$ for one actual cleared Kodaira divisor $Z$.
The zero quotient is zero, and $q_{T_m}\to R$ uniformly on such
compact subsets. Model envelopes and $R$ are continuous there,
and bounded obstacles give bounded relative differences.
\item Every genuine relative finite-energy test is output-integrable.
There are whole supporting planes
\[
 E(v)\leq E(u)+\int(v-u)\,dM(u).
\]
With $B(u)=-E(u)$ after generic normalization, and
$\delta(u,v)=E((u+v)/2)-(E(u)+E(v))/2$, the full absolute modulus is
\[
 \int|u-v|\,dM(w)\leq
 C_n\delta(u,v)^{2^{-n}}B(w)^{1/2}
 \max\{B(u),B(v),B(w)\}^{1/2-2^{-n}}.                    \tag{1}
\]
For $n=1$ omit the last exponent-zero factor.
The uniform finite-model Taylor estimate passes with the same
constants as a whole fixed increment to every genuine base, giving
both original continuous derivatives of $E(P_\theta(u+th))$.
\end{enumerate}
Differences in (1) are taken where both relative costs are finite,
a full-measure set. Constants are restored by raw mass and the
energy constant law.
Only G0 in its actual ample domain and G1 in its exact resolved
relative-generation and one-net signature are accepted NA inputs.
Finite full-section intercepts, positive deficient measures and the
corrected finite Hodge calculus are reconstructed finite algebraic
proofs, as in round159 Sections 2--4.
Ordinary algebraic volume asymptotics, Fujita, BFJ positive products
and volume differentiation, normal birational section descent and
resolution are distinguished background.

\section{An exact filtered quotient and its derivative}
Fix an actual birational model $p:Y\to X$ and
$p^*L=A+T$, with $A$ an actual nef generated rational bundle and
$T$ effective. Write $V_A=A^n$ and $\varepsilon=V-V_A\geq0$.
In cleared degree $\ell$ multiplication by the actual $T$ section
injects
\[
 S_\ell:=s_{\ell T}H^0(Y,\ell A)
               \ \subset\ R_\ell:=H^0(X,\ell L).
\]
Use normal proper birational section descent for the right space.
For an original continuous obstacle $f$, assign weights
$W_\ell(f;s)=\inf_K(\ell f-\log\|s\|)$ on the full $R_\ell$.
At a supported zero the section expression is $+\infty$.
The induced subspace filtration on $S_\ell$ and the quotient
filtration on $R_\ell/S_\ell$ form an exact filtered sequence.

\begin{lemma}[Quotient trace and missing-volume derivative]\label{quotient}
For rational model obstacles, let $\mathscr H_A(f)$ be the
full restricted trace on $S_\ell$, with the same factor
$n!\ell^{-n-1}$ as the original trace.
Both traces exist. Their difference
$\mathscr Q_A=\mathscr E-\mathscr H_A$ has
\[
 |\mathscr Q_A(f)-\mathscr Q_A(g)|
              \leq\varepsilon\|f-g\|_\infty.            \tag{2}
\]
At every original model obstacle $f$ its derivative satisfies
\[
 0\leq\mu_f-p_*\mu_{A,T;f},\qquad
 (\mu_f-p_*\mu_{A,T;f})(K)=\varepsilon,                 \tag{3}
\]
where $\mu_{A,T;f}$ is the full auxiliary restricted-trace derivative.
In particular its total variation is $\varepsilon$, independently
of the size of $f$ or the determination carrying it.
\end{lemma}
\begin{proof}
If $V_A=0$, use the direct rank argument in the last paragraph
of this proof. In its algebraic differentiations assume $V_A>0$.
Extend an adapted basis of the filtered subspace to an adapted
basis of the full space. The full sum of weights is exactly the
subspace sum plus the quotient sum. This is a trace equality, not
an assertion about an arbitrary unadapted basis.
If $\|f-g\|_\infty\leq d$, the full flags are sandwiched by shifts
of $\ell d$. The same holds for their images in the fixed quotient.
Thus each ordered quotient weight changes by at most $\ell d$.
Its rank is
$\dim R_\ell-\dim S_\ell=
\varepsilon\ell^n/n!+o(\ell^n)$.
After trace scaling the finite bound gives (2).
The floor error has size at most the rank and vanishes in this
scaling. The same argument proves monotonicity of the quotient trace.

To verify existence and the model derivative, work on one smooth
equivariant determination carrying $f=f_D$ and $T$.
Write the total pullback of $T$ as its horizontal closure $T^{\rm hor}$
plus a vertical part $T^{\rm ver}$.
The restricted section lattice is exactly that of
\[
 p^*L+D-T^{\rm hor}
          =p^*A+D+T^{\rm ver}.
\]
Indeed dividing the original section by the fixed horizontal
vanishing leaves precisely the full generic $A$ section space;
the vertical coefficients are retained in its extension condition.
All denominators are cleared. Equivariant diagonalization and
gluing at infinity give the full section-volume formula
$h^0=\sum_j\max(w_{\ell j}+\ell c+1,0)$.
For sufficiently large $c$ its intercept is $\mathscr H_A(f)$;
the analogous full intercept is $\mathscr E(f)$.
BFJ differentiation on these actual big algebraic classes gives
finite positive divisorial derivatives with masses $V_A$ and $V$.
Both differentiate the same original model direction.
No unbounded auxiliary NA operator is assumed.

The derivative of the difference is a bounded functional of norm
at most $\varepsilon$ by (2), and its value on the constant one is
$\varepsilon$ by the two trace constant laws.
A real functional whose norm equals this nonnegative constant
value is positive: for $0\leq h\leq1$,
$|\ell(1-h)|\leq\varepsilon$ implies $\ell(h)\geq0$.
Uniform model density extends this fact to $C(K)$.
The finite divisorial derivatives therefore give (3).
If $V_A=0$, the restricted rank is $o(\ell^n)$ and every fixed
obstacle has weights bounded by a constant times $\ell$.
Its intercept and derivative are therefore zero directly; this
case needs no differentiation of a nonbig auxiliary class.
In all later moving arguments a cofinal tail has $A_m^n>0$.
\end{proof}

\section{Uniform collars for original and bounded auxiliary outputs}
The following two estimates have different finite origins.
For original genuine outputs of cost at most $D$, and a fixed
effective Cartier divisor $S$, one has
\[
 \int\min(v(S),H)\,dM(u)\leq C_{S,c}+HD/c,\qquad c>D/V. \tag{4}
\]
To reconstruct it, use canonical nonpositive model majorants
$f_j=f_{D_j}$ of $u$. The finite positive deficient measure
$\mu_{D_j,c}$ is coefficientwise at most $\mu_{D_j}$ and loses
mass at most $D/c$.
Its vertical $S$ moment is at most its algebraic positive-product
intersection with the total pulled $S$; the effective horizontal
part has nonnegative volume derivative.
Since $D_j\leq0$, its class is dominated by the fixed
$\gamma=p^*L+cF$.
Choose one fixed ample $H_0$ and $d$ with $dH_0-p^*S$ nef.
Pairing only with this fixed nef test bounds the moment by
$d\langle\gamma^n\rangle H_0=C_{S,c}$.
Add the capped moment of the positive lost tail.
Canonical weak convergence passes the original continuous cap,
proving (4). This uses the complete finite positive-deficient proof,
not a signed effective-order intersection.

For any bounded generated auxiliary scalar
$-C\leq\xi\leq0$ on $A_m$, a fixed integer $c>C+1$ globally
generates its compactification
$\Gamma_\xi(c)=p^*L-T_m+D_\xi+cF$.
Its weighted generators have time weights in $[-mC,0]$;
the base twist supplies every exponent between the zero and
infinity charts. It is nef and effectively at most $p^*L+cF$.
The same fixed-nef comparison gives
\[
 \int v(S)\,d\MA_{A_m,\rm raw}(\xi)\leq C_{S,c}.        \tag{5}
\]
It also bounds every fixed original model quadratic test
$-H^2\Gamma_1\cdots\Gamma_{n-1}$ uniformly over these models:
write $H=H_1-H_2$ with two fixed globally nef classes and bound
the four terms by
$\langle(p^*L+cF)^{n-1}\rangle H_kH_l$.
Twisting by $F$ changes no vertical quadratic intersection.
Every central multiplicity is retained.

For (4), choose $c$ first and then the cap height $H$.
The collar mass is at most $C_{S,c}/H+D/c$, uniformly in $u$.
For (5) it is at most $C_{S,c}/H$, uniformly in $m$.
Take $S$ with support $Z$.
The complements $\{v(S)\leq H\}$ are fixed compact subsets of $U$.
These are uniform algebraic collars, not a claim that weak
convergence by itself controls changing Borel indicators.

\section{Bounded restricted full systems}
Fix $m$ and a bounded rational relatively generated scalar $\xi_m$
on $A_m$, with $-C\leq\xi_m\leq0$.
Suppose its physical scalar $v_m=q_{T_m}+\xi_m$ is an actual
original FS minorant of a genuine function $w$.
Let $f=f_D$ be any original model obstacle with $f\geq v_m$
and $f(v_0)\leq0$.
For every full auxiliary section, its restricted $f$ weight is
between $-\ell C$ and zero: compare to the metric $\xi_m$ for
the lower bound, and evaluate at $v_0$ for the upper bound.
In cleared degrees its complete restricted generated scalar
$\sigma_{\ell,f}$ therefore satisfies
\[
 -C\leq\xi_m\leq\sigma_{\ell,f}\leq0,\qquad
 \sigma_{\ell,f}\leq f-q_{T_m}
\]
at all finite function-field lifts.
Domination of $\xi_m$ follows by taking powers of every generator
of its actual rational weighted system; clearing its weights makes
the floor error zero. No unbounded auxiliary envelope is assumed.

\begin{lemma}[Finite restricted limits and ordered gap]\label{restricted}
The full restricted stages have
\[
 e_{A_m}(\sigma_{\ell,f})\to\mathscr H_{A_m}(f),\qquad
 p_*\MA_{A_m,\rm raw}(\sigma_{\ell,f})
                   \to p_*\mu_{A_m,T_m;f}.
\]
Moreover, with $\sigma_m=\MA_{A_m,\rm raw}(\xi_m)$,
\[
 0\leq\mathscr H_{A_m}(f)-e_{A_m}(\xi_m)
 \leq\int\min(C,f-v_m)\,d\sigma_m.                     \tag{6}
\]
For each fixed original rational model test $h$,
\[
 \left|\int h\,d(p_*\mu_{A_m,T_m;f}-p_*\sigma_m)\right|
 \leq C_{h,C}\sqrt{\mathscr H_{A_m}(f)-e_{A_m}(\xi_m)}. \tag{7}
\]
The constant is independent of $m,f$ and all their refinements.
\end{lemma}
\begin{proof}
For a fixed integer $c>C+1$, all complete compactified restricted
systems are globally generated on their resolved models and are
the complete base systems of the fixed auxiliary class
$\beta=p^*A_m+D+T_m^{\rm ver}+cF$.
The section-volume formula is affine for $c>C$ because every
weight lies in $[-\ell C,0]$.
Ordinary complete-base-system Fujita gives convergence of their
top nef volumes to $\vol(\beta)$.
Since each nef top intersection divided by $n+1$ is
$cA_m^n+e_{A_m}(\sigma_{\ell,f})$,
the intercept identity proves the energy limit.

For completeness volume convergence also identifies all fixed
derivative tests without assuming an unbounded NA limit.
Let $\Gamma_\ell\leq\beta$ be these globally nef complete models.
They are also effectively at most the fixed $p^*L+cF$.
For a fixed Cartier test $H$, choose a fixed globally nef big
$\omega$ with $\Gamma_\ell\leq\omega$ and $\omega\pm H$ nef.
The finite algebraic Morse estimate of BFJ Corollary 3.4 gives
\[
 \vol(\beta+tH)\geq
 \vol(\Gamma_\ell)+(n+1)t\Gamma_\ell^nH-Kt^2
\]
for both signs and a common $K$, by effective volume order.
Take $\ell$ to infinity, divide at fixed signed $t$ and then
let $t\to0$.
BFJ differentiability of $\vol(\beta+tH)$ shows
$\Gamma_\ell^nH\to\langle\beta^n\rangle H$.
For vertical $H$ this is precisely the claimed finite
restricted derivative measure. Model density passes every $C(K)$
test using the common mass $A_m^n$.
No uniformity of a Fujita limit across changing $f$ was used.

Finite concavity at the lower $\xi_m$ gives
$e(\sigma_{\ell,f})-e(\xi_m)
\leq\int(\sigma_{\ell,f}-\xi_m)d\sigma_m$.
On the fixed finite divisorial support of $\sigma_m$ that gap is
between zero and $\min(C,f-v_m)$.
This proves (6) after the degree limit.
For two ordered finite nef models, telescoping energy gives
$I(\sigma_{\ell,f},\xi_m)\leq
(n+1)(e(\sigma_{\ell,f})-e(\xi_m))$,
and $I$ is the sum of the mixed nonnegative quadratic forms of
their difference. Cauchy--Schwarz against the fixed $H$ and the
uniform quadratic bounds following (5) give (7), first at finite
degree and then at its already identified limit.
\end{proof}

\section{Identifying every uniformly bounded generated quotient}
\begin{theorem}[Bounded physical approximation]\label{bounded}
Assume the explicit genuine input package.
Suppose $w\in\EE$ is normalized, continuous on $U$ and
$R-C\leq w\leq R$ on the whole carrier.
Suppose rational relatively generated $\xi_m$ on the common
$A_m$ satisfy $-C\leq\xi_m\leq0$,
$\xi_m(v_0)\to0$, and
\[
 v_m=q_{T_m}+\xi_m\leq w
\]
on all lifts. Require $v_m$ to be an actual FS scalar on the
original $L$, and require
$\xi_m\to w-R$ uniformly on each compact subset of $U$.
Then
\[
 e_{A_m}(\xi_m)\to E(w),\qquad
 p_{m*}\MA_{A_m,\rm raw}(\xi_m)\to M(w)                 \tag{8}
\]
weakly on $K$. A physical $v_m$ is not asserted to belong to $\EE$.
\end{theorem}
\begin{proof}
Choose one fixed integer $N>C+2$, and set
$u_m=\max(v_m,R-N)$.
It is genuine by finite-max closure, lies between $R-N$ and $w$,
and is actual finite energy by energy monotonicity.
Its generic value is
$b_m=\max(\xi_m(v_0),-N)\leq0$, tending to zero.
After normalization its cost is at most $NV$.
On each fixed compact subset of $U$, $v_m\to w$ and hence $u_m\to w$
uniformly; on $U$ the gap $0\leq w-u_m\leq N$.
The uniform \emph{original} collars (4) show
$\int(w-u_m)dM(u_m)\to0$.
The whole plane at $u_m$, with constants restored, gives
\[
 E(u_m)\leq E(w)\leq E(u_m)+\int(w-u_m)dM(u_m).
\]
Thus $E(u_m)\to E(w)$.

The same fixed-increment Taylor estimate identifies their outputs.
For fixed rational model $h$ and $t>0$, obstacle order gives
$E(P(u_m\pm th))\leq E(P(w\pm th))$.
Subtract $E(u_m)$ and use the common lower Taylor bounds at the
cost bound $NV$, for both signs.
First take $m\to\infty$, then $t\to0$ at fixed time cutoff
$c>NV/V=N$, and finally $c\to\infty$.
The two derivatives at $w$ then squeeze
$\int h\,dM(u_m)$ to $\int h\,dM(w)$.
Uniform model density and common mass prove
$M(u_m)\to M(w)$ weakly.

Now fix $m$ and canonical model majorants $f_j\downarrow u_m$.
They are obtained from normalized majorants by the constant $b_m$,
so $f_j(v_0)=b_m\leq0$ and $f_j\leq0$.
All full quotient weights are nonpositive. Their trace is therefore
nonpositive, giving
$\mathscr E(f_j)\leq\mathscr H_{A_m}(f_j)$.
By Lemma~\ref{restricted},
\[
 E(u_m)\leq e_{A_m}(\xi_m)+C\sigma_m\{v_m<R-N\},        \tag{9}
\]
after sending $j$ to its endpoint on the fixed finite support of
$\sigma_m$. On the complement of that strict set, $u_m=v_m$,
so the capped error in (6) tends to zero.

The \emph{auxiliary} collars (5) make the last mass in (9) tend
to zero as $m\to\infty$: on any fixed compact subset of $U$,
$v_m\to w\geq R-C>R-N$, with a fixed positive margin.
Choose the collar before the degree and only then pass $m$.
Thus $\liminf e_{A_m}(\xi_m)\geq E(w)$.
The reverse inequality retains the missing rank.
For every fixed finite original $f\geq w$, multiply full
auxiliary sections by $s_{\ell T_m}$ and extend an adapted basis.
Every remaining weight is at least $\ell\min f$, so first at
fixed $m,f$ take $\ell\to\infty$ to obtain
\[
 \mathscr E(f)\geq e_{A_m}(\xi_m)
                       +(\min f)(V-A_m^n).
\]
Only then take $m\to\infty$, and finally the outer infimum over
this fixed finite-majorant family. This gives
$E(w)\geq\limsup e_{A_m}(\xi_m)$.
The energy equality in (8) follows.

For the measure equality apply the missing-volume derivative
bound (3) and the ordered comparison (7) at each $f_j$.
Canonical output convergence passes the fixed continuous $h$.
The error (6) on the fixed finite auxiliary support gives
\[
 \left|\int h\,d(M(u_m)-p_*\sigma_m)\right|
 \leq (V-A_m^n)\|h\|_\infty
      +C_{h,C}\sqrt{C\sigma_m\{v_m<R-N\}}.              \tag{10}
\]
Both terms tend to zero. The already proved weak limit of $M(u_m)$
identifies the auxiliary limit with $M(w)$ on all model tests.
Density and the converging raw masses prove (8).
The generic floor errors have been retained as $b_m\to0$;
no physical energy is substituted for the auxiliary energy.
\end{proof}

\section{Rational combinations and bounded mixed coefficients}
Fix normalized model envelopes $a_1,\ldots,a_q$ and one finite-list
complete moving system. For rational $t_i\geq0$, $\sum t_i=1$, put
\[
 a_t=\sum_i t_ia_i,\qquad \xi_{m,t}=\sum_i t_i\psi_{m,i}.
\]
Clear the rational coefficients and tensor the actual generators.
This realizes $\xi_{m,t}$ as a relatively generated rational model
on the same $A_m$, and its physical scalar is an actual FS scalar
on $L$: the horizontal factors sum to exactly $T_m$.
It is at most $a_t$ at every original lift.
A single $C$ bounds all endpoint quotients and their combinations
in $[-C,0]$, and $R-C\leq a_t\leq R$.
All hypotheses of Theorem~\ref{bounded} hold.
Thus the finite auxiliary energy polynomial and raw measure polynomial
converge at every rational simplex point to $E(a_t)$ and $M(a_t)$.

Finite-dimensional polynomial interpolation recovers their coefficients.
Choose once a finite rational unisolvent set for homogeneous degree
$n+1$ polynomials for energy and degree $n$ for measures.
Such a set exists: a nonzero homogeneous polynomial cannot vanish
on the whole rational interior of the simplex; select points
successively until the evaluation matrix has full rank.
Its fixed inverse is taken \emph{before} any moving limit.
Each auxiliary mixed raw coefficient is a positive Radon measure
of mass $A_m^n$, with the actual coefficient
$b_E(T_{m,i_1}|_E)\cdots(T_{m,i_n}|_E)$.
Their coefficient limits are therefore positive Radon measures
of raw mass $V$, symmetric in the slots. Denote them
$M(a_{i_1},\ldots,a_{i_n})$.
One has
\[
 M(a_t)=\sum_{|\beta|=n}\binom n\beta t^\beta
                   M(a_1^{[\beta_1]},\ldots,a_q^{[\beta_q]}).
                                                               \tag{11}
\]
The bounded relative-order estimate
$|a_t-a_s|\leq C\|t-s\|_1$ holds as two constant-shift inequalities
on the whole carrier, including common reference poles.
Energy and perturbed energy are Lipschitz in this estimate.
Their fixed secants, or the uniform fixed-increment bounds,
show weak continuity of $M(a_t)$ in $t$.
Thus (11) and the energy polynomial hold also at every real simplex point.
Coefficient uniqueness proves independence of the chosen complete
moving system. No multilinearity of big positive products is used.

\section{The entire genuine mixed map}
\begin{lemma}[Every genuine decreasing base]\label{decreasing}
The explicit input package implies $M(u_j)\to M(u)$ weakly for
every genuine decreasing net $u_j\downarrow u\in\EE$.
\end{lemma}
\begin{proof}
For fixed $h\in C(K)$ and $t$, the genuine envelopes
$P(u_j+th)$ decrease to $P(u+th)$:
their genuine decreasing endpoint is below the obstacle at every
point and above its envelope, and its generic value is finite.
Decreasing energy continuity passes the secants at $-t,0,t$.
They bracket the original derivative $\int h\,dM(u_j)$.
Take the net limit at fixed $t$, then $t\downarrow0$; the
two original derivative signs at the limiting base agree.
This proves the claimed weak convergence without interchanging
a derivative and a net.
\end{proof}

\begin{theorem}[Conditional genuine mixed measures]\label{mixed}
Under the explicit input package there are unique positive symmetric
raw mixed measures $M(u_1,\ldots,u_n)$ for all actual
$u_i\in\EE$, satisfying the polynomial polarization of $M$,
with mass $V$ and canonical decreasing weak continuity.
They are independent of every choice of canonical model majorants.
For normalized endpoints,
\[
 M(u_1,\ldots,u_n)
 \leq\frac{n^n}{n!}M\!\left(\frac{u_1+\cdots+u_n}{n}\right).
                                                               \tag{12}
\]
They give $Z$ zero mass and integrate every actual relative
finite-energy test.
\end{theorem}
\begin{proof}
For any finite list of actual endpoints choose canonical model
envelopes $a_{i,j}\downarrow u_i$ on the product-directed index.
At every fixed point of the rational unisolvent set the genuine
convex combinations decrease to the corresponding genuine
combination of the $u_i$. Lemma~\ref{decreasing} passes each
diagonal output. The same fixed inverse evaluation matrix
therefore passes every mixed coefficient.
Their positive masses are $V$, so their limits are positive Radon
measures of mass $V$.
The coefficient formula in terms of the diagonal map alone
proves symmetry and independence of the chosen majorant nets.
It also proves weak continuity along any genuine decreasing
net in each slot, again by a finite set of diagonal tests.

For any \emph{fixed real} simplex point, the bounded coefficient
identity (11) holds at every model-majorant index.
Its genuine combination decreases, so Lemma~\ref{decreasing}
passes the diagonal output there too.
The already identified coefficient limits pass the right side.
Thus the genuine coefficient identity holds for all real weights,
including boundary faces, without a parameter-limit exchange.

At the equal-weight point for $n$ endpoints, all coefficients of
the finite polynomial are nonnegative.
The term using each of the $n$ slots once has coefficient
$n!/n^n$. Passing this positive measure inequality gives (12).
The genuine average has cost at most the average endpoint costs
by concavity. Its output misses $Z$ and integrates every relative
finite-energy test by the input package. Measure domination
proves these assertions for the mixed output too.
Restore constants using constant invariance of the diagonal
map and hence of its polarization.
\end{proof}

\section{Canonical weighted continuity}
\begin{theorem}[All genuine relative tests and decreasing mixed limits]
Let $u_{r,j}\downarrow u_r\in\EE$ for $r=1,\ldots,n$.
For every fixed actual $v\in\EE$ and $h\in C(K)$,
\[
 \int h(R-v)\,dM(u_{1,j},\ldots,u_{n,j})
 \longrightarrow
 \int h(R-v)\,dM(u_1,\ldots,u_n).                       \tag{13}
\]
The same holds if the test is replaced by any genuine
decreasing $v_k\downarrow v$, in the full product-directed
$(j,k)$ limit. The integrals are actual original relative integrals.
\end{theorem}
\begin{proof}
Normalize the fixed test $v$ first; its restored constant contributes
only a fixed continuous $h$ integral, already covered by weak convergence.
Take canonical bounded model envelopes $b_\ell\downarrow v$.
For the ordered pair, energy monotonicity gives
$\delta(b_\ell,v)\leq(E(b_\ell)-E(v))/2\to0$.
The absolute estimate (1), together with (12), bounds
\[
 \int(b_\ell-v)\,dM(u_{1,j},\ldots,u_{n,j})
\]
by a quantity tending to zero uniformly in $j$ on a cofinal tail.
All genuine average output costs are bounded by one $D$ there:
the endpoint generic values and energies decrease to finite limits,
so their generically normalized costs are uniformly bounded.
The limiting mixed measure satisfies the same bound.
At a fixed $\ell$, $R-b_\ell$ is bounded continuous on $U$.
All mixed measures miss $Z$, and their weak limit misses it by
(12). Choose one continuous collar in $U$ before taking $j$;
its omitted mass passes through weak convergence.
This passes the bounded relative test multiplied by fixed $h$.
Only then let $\ell$ tend to its endpoint.
The uniform absolute errors prove (13).
For a general decreasing test $v_k\downarrow v$, its energies
decrease and
$\delta(v_k,v)\leq(E(v_k)-E(v))/2$.
Its normalized costs are uniformly bounded on a cofinal tail.
The midpoint defect is constant invariant, and normalization adds
only the error $V|v_k(v_0)-v(v_0)|\to0$ to the absolute integral.
The same bound is therefore uniform in $j$ and proves the product limit.
No arbitrary measurable-net monotone convergence or moving
Borel-set weak test is used.
\end{proof}

\section{Entire genuine energy differences}
\begin{theorem}[Mixed energy identity]
For every pair of actual finite-energy functions, under the same
explicit input package,
\[
 E(u)-E(v)=\frac1{n+1}\sum_{j=0}^{n}
       \int(u-v)\,dM(u^{[j]},v^{[n-j]}).                \tag{14}
\]
All terms are finite original relative integrals.
\end{theorem}
\begin{proof}
For normalized bounded model envelopes, use their common
complete moving systems. The finite nef telescoping identity
holds on that same actual $A_m$ with all raw multiplicities.
Theorem~\ref{bounded} and coefficient interpolation pass its
energies and mixed measures.
The auxiliary difference $\psi_{m,u}-\psi_{m,v}$ is bounded
and converges uniformly on compact subsets of $U$ to $u-v$.
The analogue of (5) for mixed nef slots follows by the same
effective horizontal-divisor decomposition and fixed-nef bound.
It provides uniform auxiliary collars. Fix these collars before
passing the changing bounded test and the weak mixed measure.
Thus the finite identity passes to the bounded original pair.

For arbitrary normalized $u,v$, use their two canonical
model-envelope nets. Their energies decrease.
The mixed measures converge by Theorem~\ref{mixed}, and (13)
passes each fixed relative test. The changing test error is
bounded by the sum of the two ordered errors of $u,v$;
(1) and (12) make these uniformly small over all mixed outputs
of the uniformly bounded endpoint costs.
Hence the full product-directed limit passes every term of the
bounded identity and proves (14).
For arbitrary constants, each mixed raw mass is $V$ and there
are $n+1$ terms, so the energy constant law gives the same formula.
\end{proof}

\section{What has and has not been established}
Every assertion involving the whole genuine space is conditional
on the explicit package in Section 1.
The finite quotient trace and missing-volume derivative are new
finite algebraic statements, with a proof retaining the exact
full/subspace/quotient flags.
The bounded physical identification allows any uniformly bounded
generated quotient satisfying the stated actual-minorant and
compact-convergence hypotheses. It proves more than a formal
choice of a mixed polarization, since its finite raw intersection
coefficients are identified on the original carrier.
The mixed map and all canonical genuine weighted limits above
are then uniquely determined by the target-independent diagonal map.

This is not a proof for every simultaneously unbounded physical
approximation. If the auxiliary bound $C$ grows with the model,
neither the fixed global twist nor the constants in (7)--(10)
remain uniform. A finite energy bound alone does not justify
discarding a growing bound times a disappearing collar mass.
Full unbounded physical independence requires an additional
uniform energy-tail and trace-defect argument in the original
admissibility convention. It has not been supplied here.
Nor is a raw-supremum negligible discrepancy simply declared
polar. The original negligible-set theorem remains separate.
The entire genuine foundation package is still unreviewed,
and no additional nonzero zero-volume theory is proved.
Original P16.5 remains open and no original or accepted-paper
count changes because of this draft.

\section{Primary applications and reading scope}
The complete BFJ v2 saved positive-product unit LF1--132
(original renderer 310--441) and volume/differentiation unit
LF1--101 (renderer 445--545) were read.
They supply ordinary algebraic nef agreement, dominated-nef
comparison, volume differentiation and the \emph{complete}
Corollary 3.4 Morse estimate used in the derivative squeeze.
Complete-base-system volume convergence is ordinary algebraic
Fujita background; it is not an unbounded NA operator grant.
The exact relative-lattice section-extension convention is G1.
G0 is used only for actual ample model testing/density and its
retained finite background.
The full unreviewed round159 paper and continuations200--201
were read as proof data, with their explicit conditional boundaries.
Their source ledgers are provenance and do not substitute for
primary reading. No new original PDF download, whole-primary
reading, or recursive proof of all background is claimed.

\begin{thebibliography}{9}
\bibitem{BFJ} S. Boucksom, C. Favre and M. Jonsson,
\emph{Differentiability of volumes of divisors and a problem of Teissier},
\href{https://arxiv.org/html/math/0608260v2}{arXiv:math/0608260v2}.
\bibitem{BJ} S. Boucksom and M. Jonsson,
\emph{Global pluripotential theory over a trivially valued field},
\href{https://arxiv.org/pdf/1801.08229v4}{arXiv:1801.08229v4}.
\end{thebibliography}
\end{document}

END COMPLETE MATHEMATICAL BODY

BEGIN COMPLETE MATHEMATICAL BODY 202 OWN APPLICATION LEDGER
{
  "recorded_utc": "2026-10-06T12:50:45.392704+00:00",
  "classification": "Unreviewed finite and conditional202; entire genuine foundations remain unproved.",
  "final_tex_sha256": "e12ba3ba9b34505497b577515c41a596eb4242e56eb88a5a2aaa349594d67f5b",
  "whole_final_source_root_read": true,
  "whole_final_source_read_chunks": [
    "1-235",
    "236-470",
    "471-end",
    "whole corrected general-net normalization unit"
  ],
  "actual_visual_pages": [
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8,
    9
  ],
  "conditional_proof_data": [
    {
      "label": "whole159",
      "file": "/workspace/research/root-checks/public-P16.5-round159-partial-conditional-attainment-reader/paper.tex",
      "sha256": "678a18615d419117e65a01de1ff6059e5d9478c457edae509a0608f3a5e54e55",
      "whole_body_root_read": true,
      "authority": "Unreviewed mathematical proof and explicitly conditional conclusions; no theorem grant."
    },
    {
      "label": "whole200",
      "file": "/workspace/research/root-checks/P16.5-absolute-Hodge-estimate-and-genuine-variational-attainment-candidate-20261006-continuation200.tex",
      "sha256": "28882f205280c492cd638063d2e45fca8dd6f204c5387bb93fcae91ea34a1b9d",
      "whole_body_root_read": true,
      "authority": "Unreviewed mathematical proof and explicitly conditional conclusions; no theorem grant."
    },
    {
      "label": "whole201",
      "file": "/workspace/research/root-checks/P16.5-strict-Borel-locality-from-bounded-moving-maxima-candidate-20261006-continuation201.tex",
      "sha256": "321db9ceb2877ce22820490ba7dfb9ef3703c39ec4cba4d7b2768876c7c91508",
      "whole_body_root_read": true,
      "authority": "Unreviewed mathematical proof and explicitly conditional conclusions; no theorem grant."
    }
  ],
  "new_finite_proofs": [
    "Exact filtered full/subspace/quotient sequence preserves trace additivity. Sup-norm flag shifts bound quotient trace Lipschitz constant by the missing raw rank-volume V-A^n.",
    "Full restricted lattice is actual p*L+D-horizontal(T)=p*A+D+vertical(T). Both finite model derivatives are positive Div measures; derivative difference norm<=missing mass and constant value=missing mass force positivity and total variation exactly V-A^n. Zero auxiliary volume handled directly by subleading rank.",
    "Positive time-deficient full measures and fixed-nef algebraic tests reconstruct uniform capped divisor moments at every bounded-cost original output; bounded generated auxiliary models have their own fixed-twist uniform collars and signed quadratic tests.",
    "Complete restricted full systems stay in one bounded time window and global fixed twist. Complete-base-system Fujita volumes converge; full BFJ3.4 Morse inequality with two signs and fixed nef upper class identifies each derivative measure, not just volume.",
    "Finite ordered gap controls uniform fixed-model test difference by square root gap, with all raw multiplicities and generic errors retained."
  ],
  "new_conditional_proofs": [
    "Original genuine floors max(physical,R-N) have bounded normalized costs. Whole planes, compact relative convergence and ORIGINAL uniform collars give exact genuine floor energy; whole fixed-increment Taylor bounds identify their diagonal output.",
    "At shifted canonical majorants of the floor, quotient trace is nonpositive; restricted trace gap is supported on the physical-floor losing region. AUXILIARY uniform collars make it vanish. Missing-volume derivative then identifies every uniformly bounded generated physical quotient with the genuine target-independent map.",
    "Rational tensor products of actual generators realize convex combinations on shared A_m and horizontal factor T_m. A fixed finite rational unisolvent matrix passes energy and positive mixed-measure coefficients; all real weights follow bounded relative-order parameter continuity.",
    "Entire actual E1 mixed map defined by coefficient polarization along canonical majorants; every real simplex point passes by fixed-weight genuine decreasing continuity. Positive domination by n^n/n! times diagonal average gives all genuine-test integrability and algebraic nullness.",
    "Uniform ordered midpoint errors and fixed original C0 collars prove weighted canonical decreasing mixed continuity, including simultaneously decreasing actual tests. General-net generic normalization errors retained explicitly.",
    "Finite common-A_m telescoping passes bounded relative differences through mixed uniform collars; genuine ordered absolute errors pass all unbounded paired terms to the full mixed energy identity."
  ],
  "whole_pertinent_primary_units": [
    {
      "source": "BFJ arXiv:math/0608260v2",
      "url": "https://arxiv.org/html/math/0608260v2",
      "file": "/workspace/research/campaigns/round-159/P16.5-original-equation-after-arbitrary-target-output-approximation/artifacts/codex-0lpuxa/sources/units/BFJ-v2-positive-products.txt",
      "sha256": "6c15466488dfc98ca2b08915a967e744399ae3309639ca9c3d543d686f895c8a",
      "inclusive_local_LF": [
        1,
        132
      ],
      "inclusive_original_renderer": [
        310,
        441
      ],
      "whole_pertinent_unit_root_read": true,
      "application": "Ordinary nef agreement/dominated-nef comparison and finite full-section-volume derivatives. Complete Corollary3.4 Morse bound supplies derivative convergence from complete-base-system Fujita volume convergence; no unbounded nonample NA grant."
    },
    {
      "source": "BFJ arXiv:math/0608260v2",
      "url": "https://arxiv.org/html/math/0608260v2",
      "file": "/workspace/research/campaigns/round-159/P16.5-original-equation-after-arbitrary-target-output-approximation/artifacts/codex-0lpuxa/sources/units/BFJ-v2-volume-differentiation.txt",
      "sha256": "8651090225d1a0201460f316a49cd69fc8a7734a1a9d4dc29ded54b60aaf1c47",
      "inclusive_local_LF": [
        1,
        101
      ],
      "inclusive_original_renderer": [
        445,
        545
      ],
      "whole_pertinent_unit_root_read": true,
      "application": "Ordinary nef agreement/dominated-nef comparison and finite full-section-volume derivatives. Complete Corollary3.4 Morse bound supplies derivative convergence from complete-base-system Fujita volume convergence; no unbounded nonample NA grant."
    }
  ],
  "whole_primary_sources_read": false,
  "all_recursive_primary_foundations_read": false,
  "primary_quotations_republished": false,
  "original_pdf_byte_hash_claim": false,
  "ordinary_background_not_recursively_reproved": [
    "Complete-base-system algebraic Fujita volume approximation.",
    "Normal birational full-section descent and equivariant section lattices.",
    "Resolution/principalization, finite Hodge graph/intersection calculus, compact Hausdorff Radon collars and polynomial interpolation."
  ],
  "independent_acceptance": false,
  "original_closed": false,
  "accepted_paper_count_unchanged": 59,
  "remaining": "Entire genuine foundations; every simultaneously unbounded physical approximation needs separate uniform energy-tail/trace-defect control, and all raw-supremum negligible discrepancies remain unproved. Further nonzero zero-volume range not handled.",
  "active_private_outputs_read": false,
  "hot_feedback_sent": false
}

END COMPLETE MATHEMATICAL BODY
