# Self-contained FULL ORIGINAL P16.1 review evidence

The complete new proof remains independently unverified. All necessary mathematical scope bodies are supplied inline.



BEGIN MATHEMATICAL DATA: COMPLETE unchanged17-page original proof92
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

END MATHEMATICAL DATA



BEGIN MATHEMATICAL DATA: Exact unchanged original task
{
  "problem": "Original P16.1:\nP16.1 (T5): Finite-energy equations on singular or unibranch varieties\nExtend the ﬁnite-energy non-Archimedean Monge–Ampère operator and its existence-and-\nuniqueness theorem to singular or unibranch varieties, replacing each use of smoothness in\ncompactness, envelopes, energy diﬀerentiation and comparison. State all retained polarization\nand ﬁeld hypotheses.\n\nComplete unchanged mathematical family:\n\n10     The general non-Archimedean Monge–Ampère equation\nActive items: P16.1, P16.2, P16.3, P16.4, P16.5, P16.6, P16.7. Status: Open in the\nresidual scope.\n\n10.1    Atomic targets\nP16.1 (T5): Finite-energy equations on singular or unibranch varieties\nExtend the ﬁnite-energy non-Archimedean Monge–Ampère operator and its existence-and-\nuniqueness theorem to singular or unibranch varieties, replacing each use of smoothness in\ncompactness, envelopes, energy diﬀerentiation and comparison. State all retained polarization\nand ﬁeld hypotheses.\n\nP16.2 (T5): Proper nonprojective algebraizable equation theories\nConstruct an appropriate replacement positivity datum and the associated psh, ﬁnite-energy,\ncomparison and equation theory on proper nonprojective algebraizable spaces. A proper\nalgebraic scheme with an ample line bundle is already projective, so retaining that datum\nwhile dropping projectivity is not a new case.\n\nP16.3 (T5): Finite-energy equations in positive residue characteristic\nConstruct the required ﬁnite-energy operator and prove existence and uniqueness when the\noriginal residue-characteristic restriction is removed. Replace the resolution, model-regularity\nand envelope inputs wherever they are used rather than merely changing the standing ﬁeld\nhypothesis.\n\nP16.4 (T4): Finite-energy equations over arbitrary complete valued ﬁelds\nExtend the operator and existence theorem to nondiscrete valuations and arbitrary complete\nnon-Archimedean ﬁelds outside the established invariant-toric, skeleton-supported endpoint.\nA deﬁnition of the ﬁnite-energy space alone does not establish the operator or the equation.\n\nP16.5 (T5): Finite-energy equations for nonample positivity classes\nExtend the equation theory to big or pseudoeﬀective nonample classes, specifying the psh cone,\nreference singularity type, energy and total mass. At zero volume, the existing probability\nnormalization must be replaced rather than retained unchanged.\n\nP16.6 (T4): Arbitrary-support ﬁnite-energy measures\nProve the operator and existence-and-uniqueness theorem for arbitrary ﬁnite-energy measure\nsupport beyond the known toric skeletal regime. Measures must satisfy the correct mass and\nenergy conditions. Do not reduce arbitrary support to a single skeleton or replace the genuine\nMonge–Ampère measure by another inverse measure construction.\n\nP16.7 (T5): Finite-energy equations on nonalgebraizable analytic spaces\nConstruct the ﬁnite-energy operator and its existence-and-uniqueness theory on genuinely\nnonalgebraizable analytic spaces, with an explicit positivity datum and the necessary com-\npactness, envelope and comparison replacements.\n\n\n\n\n                                              73\n\n10.2    What constitutes a solution\nFor each axis, state the retained hypotheses and construct the ﬁnite-energy operator together\nwith the corresponding existence-and-uniqueness theorem. Specify the measure mass and\nﬁnite-energy condition, uniqueness modulo constants and the replacement inputs for com-\npactness, envelopes, energy diﬀerentiation and comparison. An endpoint solving a special\ntoric measure class does not remove a general axis.\n\n10.3    Full statement and detailed state of the art\nProblem 10.1. Extend the ﬁnite-energy existence and uniqueness theory for the NA Monge–\nAmpère equation beyond the currently proved combinations of smoothness, projectivity,\nresidue characteristic, valuation, positivity class, support, and algebraizability hypotheses.\n\n    This is not one yes-or-no assertion. Positive characteristic, singular or unibranch varieties,\nnondiscrete valuations, big classes, arbitrary support, and nonalgebraizable analytic spaces\nrequire diﬀerent inputs. The known variational proofs use compactness, envelope regularity,\ndiﬀerentiability of energy, and a comparison principle; deleting a geometric hypothesis is valid\nonly after replacing every place where it enters. The relevant positive results and their distinct\ndomains are surveyed in Book Chapter 28, Book Chapter 29.\n    The projectivity axis has one logical constraint. A proper algebraic K-scheme endowed\nwith an ample line bundle is already projective over K [Stacksb, Tag 0B5N]. Thus P16.2\ncannot mean that one retains the BFJ line-bundle polarization L while simply deleting the\nword “projective.” A nonprojective proper algebraizable extension must ﬁrst replace that\npositivity datum—and then construct the corresponding psh, ﬁnite-energy, and comparison\ntheory—rather than merely rerun the original argument. No canonical replacement with the\nrequired equation theory is asserted here.\n    One exact source-stated axis is especially clean. Pille–Schneider observes that the ﬁnite-\nenergy space can be deﬁned over an arbitrary non-Archimedean ﬁeld, but that the extension of\nthe Monge–Ampère operator is not known there in general; the discretely valued characteristic-\nzero and trivially valued cases are the established endpoints [PS23, Remark 4.4]. This should\nbe solved before bundling all remaining axes into a single theorem.\n\nProposition 10.1 (Arbitrary-ﬁeld invariant toric skeletal endpoint). Let K be a complete\nnontrivially valued non-Archimedean ﬁeld, XΣ a proper toric K-variety, and L an ample toric\nline bundle. If µ is a positive Radon measure on XΣan , is supported on the canonical skeleton\nNΣ , gives zero mass to NΣ \\NR , and has total mass degL (XΣ ), then there is a toric continuous\nsingular psh metric on L whose Monge–Ampère measure is µ. It is unique up to multiplication\nof the metric by a positive constant.\n\n    Thus nondiscreteness and the arbitrary complete ground ﬁeld cause no obstruction in\nthis invariant toric, skeleton-supported range. Here “continuous singular” has the source’s\nextended-valued meaning: local weights are continuous into R ∪ {−∞}, as in [BGGJK25,\n§5.3.1]. It does not imply ﬁnite real-valued weights or ﬁnite energy. This is not an arbitrary-\nﬁeld ﬁnite-energy theorem in the BFJ sense: the result permits a singular potential, requires\ntorus invariance and skeletal support, and does not construct the general extended Monge–\nAmpère operator. In particular, P16.4 and P16.6 retain the respectively nonskeletal and\nnoninvariant ﬁnite-energy residual scopes.\n    There is also a distinct, nonproper algebraic endpoint. Let n > d ≥ 1, let X be a smooth\nprojective Fano complex variety of dimension n, and let D be a reduced simple-normal-crossing\nanticanonical divisor whose dual complex is the standard (d−1)-simplex. For the aﬃne Calabi–\nYau complement X = X \\ D, Wang’s Theorem A constructs a continuous non-Archimedean\npsh function on X an , over the trivially valued ﬁeld C, whose local Monge–Ampère measure\n\n                                               74\n\nis the canonical Lebesgue measure on the essential skeleton [Wan25]. The source is a version-\none preprint and uses a local CLD/tropical–convex construction. In particular, it neither\nconstructs the BFJ ﬁnite-energy operator nor treats arbitrary measures or arbitrary aﬃne\nvarieties. Since X is aﬃne and hence not proper, this endpoint does not answer P16.2; it\nonly records a special nonprojective algebraic solution after the properness requirement is\nalso dropped.\n    There is a separate ﬁnite-atomic inverse statement which must not be called a ﬁnite-energy\nMonge–Ampère theorem. Under its standing assumptions that K is maximally complete and\n|K × | = R>0 , Fang ﬁxes an irreducible projective K-variety with an ample line bundle and a\nﬁnite set of graded birational points on its aﬃne cone. For every probability vector on that\nﬁnite set, the source constructs a Shilov-ﬁnite, possibly singular metric having the prescribed\nequidistribution measure [Fan25, Proposition 4.8]. The source itself says that comparing this\nBanach-algebra measure with the genuine Monge–Ampère measure requires the separate con-\ntinuity property of an envelope metric. Thus it supplies neither a continuous semipositive\nsolution nor the BFJ ﬁnite-energy operator for the prescribed atomic measure, and does not\nnarrow P16.6.\n    There is also a resolved negative regularity chronology. The ﬁrst skeletal-factorization\nquestion of Gubler–Jell–Künnemann–Martin already fails on their toric surface [GJKM19,\nAppendix A]. Boucksom–Jonsson then construct a ﬁnite atomic Monge–Ampère measure sup-\nported on a dual complex whose solution is invariant under no retraction attached to any\nSNC model; they also construct a divisorial Green function that is not Q-PL [BJ24b, Theo-\nrems A and B]. Hence support on a dual complex does not imply factorization through some\nreﬁned skeleton. This is a theorem-level obstruction to a proof strategy, not an open regularity\nexpectation.\n    The Rethlas programme treats each axis separately and ﬁrst searches the post-2020 liter-\nature for an existing theorem. Alterations and universal homeomorphisms can address some\nalgebraic descent questions, but they do not by themselves supply multiplier ideals or dif-\nferentiability in positive characteristic. The unrestricted formulation is open; several strictly\ndelimited axes are already known.\n\n\n\n\n                                               75\n\n",
  "completionCriteria": "Establish the genuine finite-energy operator, exact measure mass and energy condition, existence, uniqueness modulo constants, and every compactness/envelope/differentiation/comparison replacement for the singular/geometrically unibranch projective domain with explicitly retained field and polarization hypotheses. Verify the new envelope source and the actual general-variety global theory. No change to the original mathematical target is permitted."
}

END MATHEMATICAL DATA



BEGIN MATHEMATICAL DATA: Complete original supplied body bindings
[
  {
    "index": 0,
    "title": "NEW UNREVIEWED application of accepted lemmas: original first membership",
    "supplied_binding": "f4cfeaa8e8e6e489c5d6f5f848d3da2eec12fb2919159e8d46c3edf6e262bcf6",
    "preserved_sha256": "8fb7d461bd1606d15f204c0c8d7d244a673c0570fabd37c38ba69a8a9b946f60",
    "file": "granted/supplied-00.txt",
    "scope": "Supplied mathematical data only; not a registered support ID."
  },
  {
    "index": 1,
    "title": "UNCHANGED original P16.1 and full contextual family",
    "supplied_binding": "54bf3c1fcd3c5ea486b52033455be28a56976f4171a332e26b98dc915df70103",
    "preserved_sha256": "a08d2d7e8c2c489a865eaced39967be3e49f8bc8094aca7e41485a5eaf76ae6b",
    "file": "granted/supplied-01.txt",
    "scope": "Supplied mathematical data only; not a registered support ID."
  },
  {
    "index": 2,
    "title": "TASK-GRANTED exact accepted round77 mathematical body",
    "supplied_binding": "6a82ecc963545cb9cc6f741e016f73ad82c8c43d9258acab9aa6431b221dba17",
    "preserved_sha256": "d33033e308cf564f25bfd269fb594df77f9a2fc59c428967638f7b1ab10049de",
    "file": "granted/supplied-02.txt",
    "scope": "Supplied mathematical data only; not a registered support ID."
  },
  {
    "index": 3,
    "title": "Binding of the precise round77/actual80 scope",
    "supplied_binding": "3d15f7943bb285838a215aae181248bf45b195387aab44d0ed4ae1ade396af9b",
    "preserved_sha256": "0dd77203205c2fed0fbac4dd534b6717690b3d7be88947433c8e71de00655150",
    "file": "granted/supplied-03.txt",
    "scope": "Supplied mathematical data only; not a registered support ID."
  },
  {
    "index": 4,
    "title": "TASK-GRANTED actual80 partial review",
    "supplied_binding": "342418bf7b363d708000f3f1d9d1f4cc4bb876ba4e96e78ce084c4f7a5ef4499",
    "preserved_sha256": "d6ea73bbbbcf51ab807db510c92d9d12cf2b241a4e43729e5e6d5040966c5232",
    "file": "granted/supplied-04.txt",
    "scope": "Supplied mathematical data only; not a registered support ID."
  },
  {
    "index": 5,
    "title": "TASK-GRANTED actual86 precise PARTIAL review only",
    "supplied_binding": "7b995e992b639a526491b52eb85255c613e3f1e980235490858be3c6fde6616c",
    "preserved_sha256": "afbd213fc6ec89fecc65cecf5e519e7a86f3c7a3f0bfb51f21a25d6f3724888d",
    "file": "granted/supplied-05.txt",
    "scope": "Supplied mathematical data only; not a registered support ID."
  },
  {
    "index": 6,
    "title": "Binding scope of actual86",
    "supplied_binding": "8f7397a5849939545c371d978093de8264e46391ab041e43a2f713325cc3ae63",
    "preserved_sha256": "bc041a81a8b9914d17c3da72e88ee651cd629a69273bc4058d8a9f61a8c803f3",
    "file": "granted/supplied-06.txt",
    "scope": "Supplied mathematical data only; not a registered support ID."
  },
  {
    "index": 7,
    "title": "Exact body accepted ONLY within actual86 scope; historical status statements are documentary",
    "supplied_binding": "49f9dde261db15a4df3e8baca0fb0afa4ffab070e8f64a89bd2b531c716943a9",
    "preserved_sha256": "d24c0b97f7b4bcacb8db8acd94941002c8efff0db92940ad7c6121af975fc7a8",
    "file": "granted/supplied-07.txt",
    "scope": "Supplied mathematical data only; not a registered support ID."
  },
  {
    "index": 8,
    "title": "Exact body accepted ONLY within actual86 scope; historical status statements are documentary",
    "supplied_binding": "6c30c2e4c8b93394864fb5b373b2565436b20e0cd140794337541513f7bccec7",
    "preserved_sha256": "f7a5ec8109e75ce5f1f9329bf7e5c4a0632698ee8ef5ffb936208d639310001f",
    "file": "granted/supplied-08.txt",
    "scope": "Supplied mathematical data only; not a registered support ID."
  },
  {
    "index": 9,
    "title": "TASK-GRANTED actual87 precise PARTIAL review only",
    "supplied_binding": "915213c661085fbb723973f27cfaa732d3cdbf3893088c47120900d0ac7af50f",
    "preserved_sha256": "542caf38efb4820ef53a3052808ef389e02680ef354ef6745ca389f1de9b6440",
    "file": "granted/supplied-09.txt",
    "scope": "Supplied mathematical data only; not a registered support ID."
  },
  {
    "index": 10,
    "title": "Binding scope of actual87",
    "supplied_binding": "e9a31b01fc6327daef23539467760e53f89b0397ded5215d20fcdf0ea5d428ed",
    "preserved_sha256": "810590347035fa8b4d47bf9b7ca81c0b823ae1fbfeb2c1bcb0f917107488239e",
    "file": "granted/supplied-10.txt",
    "scope": "Supplied mathematical data only; not a registered support ID."
  },
  {
    "index": 11,
    "title": "Exact body accepted ONLY within actual87 scope; historical status statements are documentary",
    "supplied_binding": "1b6a3ffdf27b45f892f0bc1e225c721ecb01d4938fe3abeeed1604ac10905eb5",
    "preserved_sha256": "8b6d1811dcc3fbfa6e44ba15b6c79b0fc9ef7f21468b8edc835247cd82349942",
    "file": "granted/supplied-11.txt",
    "scope": "Supplied mathematical data only; not a registered support ID."
  },
  {
    "index": 12,
    "title": "TASK-GRANTED actual88 precise PARTIAL review only",
    "supplied_binding": "0b8e6619ab9d0401346e2d113200341e73e72031c27ed98bd71428b758003ee9",
    "preserved_sha256": "fe6ec432490119e1fd15991509013ae4f42d3a82944d1efd220615a7215cbbe3",
    "file": "granted/supplied-12.txt",
    "scope": "Supplied mathematical data only; not a registered support ID."
  },
  {
    "index": 13,
    "title": "Binding scope of actual88",
    "supplied_binding": "bba37d206249b85b2febefd7fb8fd84fbe107b082c71138e4c471bd2aed7015f",
    "preserved_sha256": "f7939dda604dddc46d681d5b8a208d7ad5c20220660354180f0d4620284f223c",
    "file": "granted/supplied-13.txt",
    "scope": "Supplied mathematical data only; not a registered support ID."
  },
  {
    "index": 14,
    "title": "Exact body accepted ONLY within actual88 scope; historical status statements are documentary",
    "supplied_binding": "447cf79483e6119171585b3630fd53890a9899fad848a9de11495db70b981877",
    "preserved_sha256": "122e1ca446de7e53afb4fe8cddc31ac4b0217e9a7ac23d1a0e7ad0ede911b086",
    "file": "granted/supplied-14.txt",
    "scope": "Supplied mathematical data only; not a registered support ID."
  },
  {
    "index": 15,
    "title": "Exact body accepted ONLY within actual88 scope; historical status statements are documentary",
    "supplied_binding": "c8e83ff56c71a8c3d7ecd1e67733f51e57a741883ba84d841e0003f5bc5bcdf6",
    "preserved_sha256": "4ebd4d1b5209e54f307373cbcbc4ff2811543eec416236607292e15f45f5d0ec",
    "file": "granted/supplied-15.txt",
    "scope": "Supplied mathematical data only; not a registered support ID."
  },
  {
    "index": 16,
    "title": "TASK-GRANTED actual89 precise PARTIAL review only",
    "supplied_binding": "18c79bafa71adc4aacbd99650176f00e6c710d7cd299898299d8dab8aa715512",
    "preserved_sha256": "2df1e2dd555da679e867e530a80919ca1efaa7598c3a654aeaa864717b14d71d",
    "file": "granted/supplied-16.txt",
    "scope": "Supplied mathematical data only; not a registered support ID."
  },
  {
    "index": 17,
    "title": "Binding scope of actual89",
    "supplied_binding": "76b0e8d802afd60f3417b81d262aece7c6cffef2925c092bd3893425d6785151",
    "preserved_sha256": "bb0e104336daf4e7d2a11dfc2f282f00de52c73bbc5d25e1e48ab8f5ea36fc6d",
    "file": "granted/supplied-17.txt",
    "scope": "Supplied mathematical data only; not a registered support ID."
  },
  {
    "index": 18,
    "title": "Exact body accepted ONLY within actual89 scope; historical status statements are documentary",
    "supplied_binding": "2cac3d27263a2230a409f375c4d1b94c12bfd5f5e007d5bf35d9e1f98cc52ecb",
    "preserved_sha256": "529f8c07e9382b97136fb5a813f7694c0b7e432907c5915d819cc2db68a4539b",
    "file": "granted/supplied-18.txt",
    "scope": "Supplied mathematical data only; not a registered support ID."
  },
  {
    "index": 19,
    "title": "Exact body accepted ONLY within actual89 scope; historical status statements are documentary",
    "supplied_binding": "c589d09159ecf118494dd677d02d0ae80ad6148dd44739abfc1f2be43cdbd402",
    "preserved_sha256": "082bf0858d9d24f0184f93b43f6a6b1748d1ea60775e1e1b8ab800802d650ca0",
    "file": "granted/supplied-19.txt",
    "scope": "Supplied mathematical data only; not a registered support ID."
  },
  {
    "index": 20,
    "title": "PRIMARY exact join unit or its source binding and reading limits",
    "supplied_binding": "b3ca837f0e204e91b74ad39ed2be8d6485cfa92573d504a70747f9c4642fcdfa",
    "preserved_sha256": "729ff5cd033512bffb4e6e320f189270483810858a4a2e0582a1a032e0c64e38",
    "file": "granted/supplied-20.txt",
    "scope": "Supplied mathematical data only; not a registered support ID."
  },
  {
    "index": 21,
    "title": "PRIMARY exact join unit or its source binding and reading limits",
    "supplied_binding": "deb3974526b8f2cda45979b634c74562b57bd092f1e138b255b8ed998c39f9e7",
    "preserved_sha256": "c8d10e50947190567863fbff92fa04796505716524a1d2fbe810ddcb78206aa3",
    "file": "granted/supplied-21.txt",
    "scope": "Supplied mathematical data only; not a registered support ID."
  },
  {
    "index": 22,
    "title": "PRIMARY exact join unit or its source binding and reading limits",
    "supplied_binding": "39deb0230b013306eaf995949df6259ab3f3d3fdd8e79820d856979b7f44caf5",
    "preserved_sha256": "7fb9983f36c433c965dca1c30dfaeaf3409d46959096d4d89d1f676dde7004c0",
    "file": "granted/supplied-22.txt",
    "scope": "Supplied mathematical data only; not a registered support ID."
  },
  {
    "index": 23,
    "title": "PRIMARY exact join unit or its source binding and reading limits",
    "supplied_binding": "f0bf826b71461d5db65319739cf1ee9a4fdebaa35146bec9e0ae705d6647262d",
    "preserved_sha256": "76f11c5a9a303907c68b55bc0aaa6d0be846515a9b94a9d647041515552f2a3a",
    "file": "granted/supplied-23.txt",
    "scope": "Supplied mathematical data only; not a registered support ID."
  },
  {
    "index": 24,
    "title": "PRIMARY exact join unit or its source binding and reading limits",
    "supplied_binding": "c6f30d464a871bb4e7fa14e51f471e5db4e997f1521d7187251f5dd4d3a96995",
    "preserved_sha256": "c6e33d5e8b6d44d821eb82818f3a5100604d53d72deb1c9e8da19a5a7ec18843",
    "file": "granted/supplied-24.txt",
    "scope": "Supplied mathematical data only; not a registered support ID."
  },
  {
    "index": 25,
    "title": "Read-only PRIMARY cache catalogue; paths authorize primary source reads only",
    "supplied_binding": "2eaf5679aaa2e26155fbdf5456919b3a4716d89ea04b963f8ba8e0853fbac844",
    "preserved_sha256": "d57f073432f6a31aa3ddc2f688b4cbc985dcea760c873f030a703dfee3de5c08",
    "file": "granted/supplied-25.txt",
    "scope": "Supplied mathematical data only; not a registered support ID."
  }
]

END MATHEMATICAL DATA



BEGIN MATHEMATICAL DATA: Original context 0: NEW UNREVIEWED application of accepted lemmas: original first membership

# Unreviewed join of independently accepted fiber and contact results

This is a new mathematical application proposal, not an accepted theorem.
Actual88 and actual89 separately passed only their exact partial scopes.
Actual86 and actual87 retain their respective conditional and geometric scopes.
The present application must be independently assessed. Original P16.1 remains
open pending a complete original-scope proof and review.

## 1. Precise proposed conclusion and dependencies

For every countable algebraically closed trivially valued characteristic-zero
field k, reduced irreducible geometrically unibranch projective k-variety X,
and actual ample rational line bundle L, the proposal proves:

(a) For a projective birational resolution pi:Y->X with smooth projective
integral source, genuine pullback identifies PSH(X,L) with PSH(Y,pi*L), in
their divisorial topologies and with their original suprema.

(b) The normalized target space is compact and c1(L) has the envelope property.

The separately accepted antecedents are:

F: actual88 on the exact root92+93 bodies and binding. Every genuine
pi*L-psh potential is constant on every analytic resolution fiber, including
minus infinity, and descends to an usc scalar on the original X. The connected
fiber application first factors through normalization but retains X and L.

C: actual89 on the exact continuation96 repaired body and binding. Over
countable k its countable affine chain and original projective consequence
apply to the specified usc, generically finite, upper-growth inputs with one
proper birational contact witness, original canonical frames, local decreasing
rational contact sequences, and GEO on the specified smooth affine operations.

R: actual86 on root90 supplies actual-reference local contact conversion of a
genuine pulled semiample potential without assuming target EP.

G: actual87 on root91 supplies the exact countable sequence extraction, actual
reference identities and GEO for the original restricted witnesses and finite
combinations/products. Its source is smooth; its projective birational morphism
need not be smooth.

None of these separate grants establishes the present application by itself.

## 2. Resolution, scalar and canonical charts

Temkin1.2.1 supplies a finite projective blowup resolution of the finite-type
characteristic-zero X, preserving its regular locus. Its smooth integral
projective source Y has actual semiample nef M=pi*L. By F, for every genuine
phi in PSH(Y,M) there is one usc psi on X with phi=psi composed with pi at
every analytic point. Proper surjectivity preserves the finite global upper
bound. The birational map preserves the generic trivial valuation, where phi
is finite, so psi is generically finite.

Choose q positive integral such that qL is an honest very ample bundle and a
generating section system s_0,...,s_N defining a closed immersion. On the
original affine chart U_i=D(s_i), its original coordinate ring is generated by
the ratios s_j/s_i. In the pulled s_i frame set

rho_i=q^(-1) max_j log|s_j/s_i|,   u_i=psi+rho_i.

The constant ratio is retained, hence rho_i>=0; its bounded simultaneous
seminorm domains are compact, so it is a proper original-ring affine FS
exhaustion. The zero-weight globally generating system has canonical potential
zero at every point: all canonical section norms are <=1 and one generating
section is a unit at the valuation center. Consequently
rho_i=-q^(-1)log||s_i||_triv. It is precisely the original raw canonical
reference weight, not an arbitrarily chosen numerical-class representative.
The pulled weight is rho_i composed with pi, including every analytic value.

Thus u_i is usc, locally bounded above, generically finite, and
u_i<=B+rho_i. A rational shift of the gate's exhaustion can absorb B or make
the exhaustion at least one; the original scalar u_i is unchanged.

## 3. Contacts on the same witness

Use the single original proper birational morphism
P_i=pi^(-1)(U_i)->U_i. P_i is integral of finite type and smooth over k. It
need not be affine or proper over k; properness is relative to U_i. The raw
pulled function is exactly phi+rho_i composed with pi.

R applies to phi on the actual M and this actual pulled frame. On each
specified compact seminorm neighborhood Q with ordinary interior in an affine
source open, it gives a decreasing net of finite rational affine FS weights
with this exact pointwise limit. Its conversion uses the valid ample
perturbation pairs and the actual bundle differences with zero potential,
then compact local approximation and summable positive rational shifts. It
does not assume same-bundle ample approximation on M or EP on X.

Since k is countable, the finite-type source has second countable seminorm
topology. G extracts increasing indices giving a decreasing sequence with
exactly the same infimum on Q, including minus infinity. Cofinality of the
selected indices is neither needed nor asserted. Work on the ordinary interior
of Q, a common neighborhood for every finite approximant.

At each tested point a finite branch attains the finite maximum. A nonconstant
winning branch has nonzero seminorm and is an invertible regular function on
its principal neighborhood; its rational positive multiple of log absolute
value plus the same constant supports the maximum from below and agrees
there. A floor branch supplies the constant support. Inactive branches and
vanishing sections cannot displace that finite support. Thus every local
sequence has precisely C's original contact input, with the same frame,
weights, supports and constants. Rational shifts are applied to both support
and weight. A finite-type affine cover handles the nonaffine P_i.

Restrictions and finite combinations use that original witness. Product
operations use P_i times A^1 and the logarithmic floors specified in C.
For each smooth affine operation, G supplies the smooth ample-boundary
completion and projective birational domination of the restricted witness,
retaining exceptional points and the actual raw reference. Its finite common
domination is invoked only for finitely many specified witnesses. The
completed residue-field comparisons inside F are not applications of the
countable affine theorem.

These checks supply the exact antecedents of C for the original u_i. If any
additional antecedent of its accepted body is indispensable, it must be
identified rather than inferred from the word "weak".

## 4. First target membership and compactness

C first gives original-ring affine regularization of u_i and then its
projective consequence on the ORIGINAL X. For every rational c>1, the chart
function psi-(c-1)rho_i, extended by minus infinity outside U_i, is genuinely
cL-psh. At every analytic point choose a maximal homogeneous coordinate.
That chart has rho_i=0, while every other chart contribution is <=psi.
Their finite maximum is therefore exactly psi at every point, including
minus infinity. Hence psi is cL-psh for every c>1. Apply varying-class
decreasing closure to the constant scalar family psi as c decreases to one.
The individual chart extensions increase and are not the family to which
this closure is applied. This proves first genuine L-membership without EP.

Genuine pullback in the other direction follows from BJ4.7; a birational
morphism preserves generic finiteness. F and first membership make pullback
an onto bijection. The divisorial coordinate sets on the common function
field are identical, so both this map and its inverse are continuous.
Analytic surjectivity preserves suprema. Thus normalized spaces are
homeomorphic. BJ5.20-5.21 give normalized compactness on the smooth source
for the nef class pi*L. Transport compactness and then apply general-projective
BJ5.11 to obtain EP on the original X.

This holds for every countable field, target and actual ample rational L
specified in section 1, and so supplies precisely antecedent E of actual86.
There is no use of BJ5.13 before approaching EP on the TARGET.

## 5. Subsequent original equation and verification boundary

Only if this join is accepted may actual86's countable-to-arbitrary implication
be used without its former E condition. It allows a separate larger countable
field for each finite obstacle and each finite actual-bundle competitor,
retains the original possibly nonnormal generic fiber, and transports actual
continuous raw curvature through orthogonality and domination. It gives EP
over every algebraically closed trivially valued characteristic-zero k with
no cardinality assumption, for the same geometrically unibranch projective X
and actual ample rational L.

The separately accepted root89/actual86 then yields the genuine raw
finite-energy operator and actual variational solution for every positive
Radon mu with raw mass V=(L^n) and finite intrinsic raw dual energy:
MA_raw(phi_mu)=mu, uniquely modulo constants. The calibration is
E_raw=V E_BJ and E_raw^dual(mu)=V E_BJ^dual(mu/V).
Normalization transport and unbounded mixed products are used only after
target EP and with their original cycles and generic degree one. Dimension
zero has V=1 and the unit point measure.

The present review proposal concentrates on sections 1-4 and the exact
antecedent match to E. A complete original paper still requires a full proof
of the operator, raw mass, energy condition, attainment, differentiation,
comparison, uniqueness and normalization through all unbounded limits.
No new original is recorded solved merely because the dependencies passed.



END MATHEMATICAL DATA



BEGIN MATHEMATICAL DATA: Original context 1: UNCHANGED original P16.1 and full contextual family

{
  "problem": "Original P16.1:\nP16.1 (T5): Finite-energy equations on singular or unibranch varieties\nExtend the ﬁnite-energy non-Archimedean Monge–Ampère operator and its existence-and-\nuniqueness theorem to singular or unibranch varieties, replacing each use of smoothness in\ncompactness, envelopes, energy diﬀerentiation and comparison. State all retained polarization\nand ﬁeld hypotheses.\n\nComplete unchanged mathematical family:\n\n10     The general non-Archimedean Monge–Ampère equation\nActive items: P16.1, P16.2, P16.3, P16.4, P16.5, P16.6, P16.7. Status: Open in the\nresidual scope.\n\n10.1    Atomic targets\nP16.1 (T5): Finite-energy equations on singular or unibranch varieties\nExtend the ﬁnite-energy non-Archimedean Monge–Ampère operator and its existence-and-\nuniqueness theorem to singular or unibranch varieties, replacing each use of smoothness in\ncompactness, envelopes, energy diﬀerentiation and comparison. State all retained polarization\nand ﬁeld hypotheses.\n\nP16.2 (T5): Proper nonprojective algebraizable equation theories\nConstruct an appropriate replacement positivity datum and the associated psh, ﬁnite-energy,\ncomparison and equation theory on proper nonprojective algebraizable spaces. A proper\nalgebraic scheme with an ample line bundle is already projective, so retaining that datum\nwhile dropping projectivity is not a new case.\n\nP16.3 (T5): Finite-energy equations in positive residue characteristic\nConstruct the required ﬁnite-energy operator and prove existence and uniqueness when the\noriginal residue-characteristic restriction is removed. Replace the resolution, model-regularity\nand envelope inputs wherever they are used rather than merely changing the standing ﬁeld\nhypothesis.\n\nP16.4 (T4): Finite-energy equations over arbitrary complete valued ﬁelds\nExtend the operator and existence theorem to nondiscrete valuations and arbitrary complete\nnon-Archimedean ﬁelds outside the established invariant-toric, skeleton-supported endpoint.\nA deﬁnition of the ﬁnite-energy space alone does not establish the operator or the equation.\n\nP16.5 (T5): Finite-energy equations for nonample positivity classes\nExtend the equation theory to big or pseudoeﬀective nonample classes, specifying the psh cone,\nreference singularity type, energy and total mass. At zero volume, the existing probability\nnormalization must be replaced rather than retained unchanged.\n\nP16.6 (T4): Arbitrary-support ﬁnite-energy measures\nProve the operator and existence-and-uniqueness theorem for arbitrary ﬁnite-energy measure\nsupport beyond the known toric skeletal regime. Measures must satisfy the correct mass and\nenergy conditions. Do not reduce arbitrary support to a single skeleton or replace the genuine\nMonge–Ampère measure by another inverse measure construction.\n\nP16.7 (T5): Finite-energy equations on nonalgebraizable analytic spaces\nConstruct the ﬁnite-energy operator and its existence-and-uniqueness theory on genuinely\nnonalgebraizable analytic spaces, with an explicit positivity datum and the necessary com-\npactness, envelope and comparison replacements.\n\n\n\n\n                                              73\n\n10.2    What constitutes a solution\nFor each axis, state the retained hypotheses and construct the ﬁnite-energy operator together\nwith the corresponding existence-and-uniqueness theorem. Specify the measure mass and\nﬁnite-energy condition, uniqueness modulo constants and the replacement inputs for com-\npactness, envelopes, energy diﬀerentiation and comparison. An endpoint solving a special\ntoric measure class does not remove a general axis.\n\n10.3    Full statement and detailed state of the art\nProblem 10.1. Extend the ﬁnite-energy existence and uniqueness theory for the NA Monge–\nAmpère equation beyond the currently proved combinations of smoothness, projectivity,\nresidue characteristic, valuation, positivity class, support, and algebraizability hypotheses.\n\n    This is not one yes-or-no assertion. Positive characteristic, singular or unibranch varieties,\nnondiscrete valuations, big classes, arbitrary support, and nonalgebraizable analytic spaces\nrequire diﬀerent inputs. The known variational proofs use compactness, envelope regularity,\ndiﬀerentiability of energy, and a comparison principle; deleting a geometric hypothesis is valid\nonly after replacing every place where it enters. The relevant positive results and their distinct\ndomains are surveyed in Book Chapter 28, Book Chapter 29.\n    The projectivity axis has one logical constraint. A proper algebraic K-scheme endowed\nwith an ample line bundle is already projective over K [Stacksb, Tag 0B5N]. Thus P16.2\ncannot mean that one retains the BFJ line-bundle polarization L while simply deleting the\nword “projective.” A nonprojective proper algebraizable extension must ﬁrst replace that\npositivity datum—and then construct the corresponding psh, ﬁnite-energy, and comparison\ntheory—rather than merely rerun the original argument. No canonical replacement with the\nrequired equation theory is asserted here.\n    One exact source-stated axis is especially clean. Pille–Schneider observes that the ﬁnite-\nenergy space can be deﬁned over an arbitrary non-Archimedean ﬁeld, but that the extension of\nthe Monge–Ampère operator is not known there in general; the discretely valued characteristic-\nzero and trivially valued cases are the established endpoints [PS23, Remark 4.4]. This should\nbe solved before bundling all remaining axes into a single theorem.\n\nProposition 10.1 (Arbitrary-ﬁeld invariant toric skeletal endpoint). Let K be a complete\nnontrivially valued non-Archimedean ﬁeld, XΣ a proper toric K-variety, and L an ample toric\nline bundle. If µ is a positive Radon measure on XΣan , is supported on the canonical skeleton\nNΣ , gives zero mass to NΣ \\NR , and has total mass degL (XΣ ), then there is a toric continuous\nsingular psh metric on L whose Monge–Ampère measure is µ. It is unique up to multiplication\nof the metric by a positive constant.\n\n    Thus nondiscreteness and the arbitrary complete ground ﬁeld cause no obstruction in\nthis invariant toric, skeleton-supported range. Here “continuous singular” has the source’s\nextended-valued meaning: local weights are continuous into R ∪ {−∞}, as in [BGGJK25,\n§5.3.1]. It does not imply ﬁnite real-valued weights or ﬁnite energy. This is not an arbitrary-\nﬁeld ﬁnite-energy theorem in the BFJ sense: the result permits a singular potential, requires\ntorus invariance and skeletal support, and does not construct the general extended Monge–\nAmpère operator. In particular, P16.4 and P16.6 retain the respectively nonskeletal and\nnoninvariant ﬁnite-energy residual scopes.\n    There is also a distinct, nonproper algebraic endpoint. Let n > d ≥ 1, let X be a smooth\nprojective Fano complex variety of dimension n, and let D be a reduced simple-normal-crossing\nanticanonical divisor whose dual complex is the standard (d−1)-simplex. For the aﬃne Calabi–\nYau complement X = X \\ D, Wang’s Theorem A constructs a continuous non-Archimedean\npsh function on X an , over the trivially valued ﬁeld C, whose local Monge–Ampère measure\n\n                                               74\n\nis the canonical Lebesgue measure on the essential skeleton [Wan25]. The source is a version-\none preprint and uses a local CLD/tropical–convex construction. In particular, it neither\nconstructs the BFJ ﬁnite-energy operator nor treats arbitrary measures or arbitrary aﬃne\nvarieties. Since X is aﬃne and hence not proper, this endpoint does not answer P16.2; it\nonly records a special nonprojective algebraic solution after the properness requirement is\nalso dropped.\n    There is a separate ﬁnite-atomic inverse statement which must not be called a ﬁnite-energy\nMonge–Ampère theorem. Under its standing assumptions that K is maximally complete and\n|K × | = R>0 , Fang ﬁxes an irreducible projective K-variety with an ample line bundle and a\nﬁnite set of graded birational points on its aﬃne cone. For every probability vector on that\nﬁnite set, the source constructs a Shilov-ﬁnite, possibly singular metric having the prescribed\nequidistribution measure [Fan25, Proposition 4.8]. The source itself says that comparing this\nBanach-algebra measure with the genuine Monge–Ampère measure requires the separate con-\ntinuity property of an envelope metric. Thus it supplies neither a continuous semipositive\nsolution nor the BFJ ﬁnite-energy operator for the prescribed atomic measure, and does not\nnarrow P16.6.\n    There is also a resolved negative regularity chronology. The ﬁrst skeletal-factorization\nquestion of Gubler–Jell–Künnemann–Martin already fails on their toric surface [GJKM19,\nAppendix A]. Boucksom–Jonsson then construct a ﬁnite atomic Monge–Ampère measure sup-\nported on a dual complex whose solution is invariant under no retraction attached to any\nSNC model; they also construct a divisorial Green function that is not Q-PL [BJ24b, Theo-\nrems A and B]. Hence support on a dual complex does not imply factorization through some\nreﬁned skeleton. This is a theorem-level obstruction to a proof strategy, not an open regularity\nexpectation.\n    The Rethlas programme treats each axis separately and ﬁrst searches the post-2020 liter-\nature for an existing theorem. Alterations and universal homeomorphisms can address some\nalgebraic descent questions, but they do not by themselves supply multiplier ideals or dif-\nferentiability in positive characteristic. The unrestricted formulation is open; several strictly\ndelimited axes are already known.\n\n\n\n\n                                               75\n\n",
  "completionCriteria": "Establish the genuine finite-energy operator, exact measure mass and energy condition, existence, uniqueness modulo constants, and every compactness/envelope/differentiation/comparison replacement for the singular/geometrically unibranch projective domain with explicitly retained field and polarization hypotheses. Verify the new envelope source and the actual general-variety global theory. No change to the original mathematical target is permitted."
}



END MATHEMATICAL DATA



BEGIN MATHEMATICAL DATA: Original context 2: TASK-GRANTED exact accepted round77 mathematical body

---
title: "Compact algebraic PL extensions, signed integration by parts, and the smooth gate"
author: "Primary-source reconstruction; unverified mathematical draft"
date: "5 October 2026"
geometry: margin=0.85in
fontsize: 10pt
header-includes:
  - \usepackage{amsmath,amssymb,amsthm}
  - \usepackage{longtable}
---

## 1. Exact target and disposition

The unchanged original P16.1 is **not solved**. Candidate=false. Its complete family and completion criterion remain those of `task-original.json`, reproduced from the preserved input. In particular the criterion is:

> P16.1 (T5): Finite-energy equations on singular or unibranch varieties. Extend the finite-energy non-Archimedean Monge--Ampere operator and its existence-and-uniqueness theorem to singular or unibranch varieties, replacing each use of smoothness in compactness, envelopes, energy differentiation and comparison. State all retained polarization and field hypotheses.

> Establish the genuine finite-energy operator, exact measure mass and energy condition, existence, uniqueness modulo constants, and every compactness/envelope/differentiation/comparison replacement for the singular/geometrically unibranch projective domain with explicitly retained field and polarization hypotheses. Verify the new envelope source and the actual general-variety global theory. No change to the original mathematical target is permitted.

The intended equation domain retains reduced irreducible geometrically unibranch projective varieties over arbitrary algebraically closed trivially valued characteristic-zero fields, ample line bundles, and arbitrary-support finite-dual-energy measures. No smooth special case in this paper replaces that domain. The original P16.2--P16.7 axes also remain unchanged; no result over arbitrary valued fields, nonample classes, or nonalgebraizable spaces is asserted.

This continuation provides new detailed proof drafts for the compact algebraic PL extension and signed-IBP gate, its raw-mass/comparison/domination consequences, and the smooth membership argument. It also gives an explicit route through smooth upper growth and removal, with the geometric witness hypotheses stated. The later singular Runge, envelope, cardinality and normalization chain is not completed. The embedded drafts are mathematical data. No path printed in them was read, and none of their results is imported as an accepted theorem.

Throughout Sections 2--8, $k$ is algebraically closed, trivially valued and of characteristic zero. Except where smoothness is expressly required, $X$ is reduced irreducible projective. $H$ and $L$ denote actual ample rational line bundles, not just numerical classes. Rational PL always means rational slopes and constants. Analytic contact weights mean the following binding hypothesis: on ordinary point neighborhoods the continuous weight is a finite continuous rational-affine selection in finitely many unit logarithms, with an affine local support below it and equal to it at the tested image point. The support inequality and equality have the **same constant**. Finite-floor logarithmic maxima are allowed by deleting inactive zero-coordinate branches before using unit charts. Local decreasing approximants are supplied on one common neighborhood for each finite tuple. These restrictions are substantive: arbitrary positive currents and arbitrary global weak rational approximations are not asserted to satisfy them.

## 2. Compact algebraic extensions on the original variety

### 2.1. Localization and bounded logarithms

Fix a very ample $H$. If $s$ is a nonzero section, then, without normality,
$$\Gamma(D(s),\mathcal O_X)=\varinjlim_m H^0(X,mH)/s^m. \tag{2.1}$$
On a finite affine trivializing cover this is module localization; the finitely many matching equalizers commute with filtered localization. This proves the assertion for the original structure sheaf. Thus inverting finitely many regular functions $\tau_i/s^{d_i}$ gives the literal chart
$$D(a)=D(s)\cap\bigcap_iD(\tau_i),\qquad a=s\prod_i\tau_i. \tag{2.2}$$
The extra factor $s$ retains the old boundary. Every regular function on this chart is $F/a^m$ for a global section of the appropriate power of $H$.

For a global section $F$, let $\mathfrak b_F$ be the coherent ideal locally generated by its coefficient in a center frame. Its logarithmic norm for the canonical trivial metric is $\log|\mathfrak b_F|$. At each analytic point this is independent of the center frame, since changes of center frame are units in its valuation ring. This also follows from BJ 1.24 and the subsequent definition of section evaluation (S1 LF883--900). Therefore
$$A_{F,N}=\max(\log|\mathfrak b_F|,-N)\in\operatorname{PL}(X) \tag{2.3}$$
for positive rational $N$, by the flag ideal $\mathfrak b_F+(t^N)$ after clearing denominators. If $f=F/a^m$ is a unit on a compact set $W\subset D(a)^{\rm an}$, choose rational clipping levels below the minima of both section logarithms on $W$. Then
$$\log|f|=A_{F,N}-m A_{a,N'}\quad\hbox{on a neighborhood of }W. \tag{2.4}$$
The equality is exact. A uniform approximation to a logarithm is not being substituted.

Analytic units can be treated on smaller compact rational domains as well. In the algebraic reduction of published Ducros 3.2 (S9 LF2087--2127), a rational domain is localized at a nonvanishing denominator $h$, and the functions $b/h^r$ in the original ring are dense in its affinoid algebra. For a unit $f$ choose an approximant $g$ with
$$\|f-g\|_W<\min_W|f|.$$
The ultrametric inequality gives $|g|=|f|$ at **every** point of $W$. A finite list is treated simultaneously. The original domain and principal localization are retained. This uses the precise rational-domain density mechanism in that proof, including its finite rational refinements; density of polynomials on an arbitrary analytic open is not claimed. Norm equality remains true after complete field extension because the same uniform inequality and lower bound pull back.

### 2.2. A finite selected weight has an actual PL extension

Suppose a finite continuous rational-affine selection is supplied near a compact set and its used coordinates are unit logarithms there. Choose compact rational neighborhoods inside its original charts with rational upper/lower bounds; their interiors cover the compact set. They are $\Gamma$-strict with $\Gamma=\exp(\mathbb Q)$, even over the trivial field. Ducros 3.2 applies to these **compact**, $\Gamma$-strict spaces and their **invertible** functions. Their logarithmic images are finite rational polytope complexes of dimension at most $\dim X$. No dimension equality is needed.

Refine the images by the finitely many hyperplanes where the selected affine expressions agree. On a relative open convex cell the distinct expressions have a fixed order. Continuity forces the selected expression class to be locally constant, hence constant on that cell. Continuity supplies its affine value on the closed cell. The result is a rational PL function on a finite compact rational polyhedral complex $T$.

Here is an elementary extension, so no unrestricted tropical selection theorem is hidden. Put $T$ in the interior of a rational box. Cut that box by all rational hyperplanes defining its cells and the expression domains, and barycentrically subdivide the resulting finite rational polytopes. This triangulates the box with $T$ as a subcomplex and each affine piece as a union of simplices. Assign the prescribed rational value to each vertex of $T$, assign zero to the box-boundary vertices, and assign arbitrary rational values to the other vertices. Affine interpolation on every simplex, followed by zero outside the box, gives a continuous finite rational PL function $E$ on the whole Euclidean space, equal to the selection on $T$.

Such $E$ is a difference of finite convex rational PL functions. To verify this directly, take all rational supporting hyperplanes $h_j=0$ of its affine cells. Across any wall, continuity makes the gradient jump normal to the wall. There are finitely many jumps. Choose positive rational $C$ so adding $C\sum_j|h_j|$ makes every oriented normal jump nonnegative. Restriction to each generic line is then convex; continuity handles lines through intersections. Hence $E+C\sum_j|h_j|$ is convex and is the maximum of its finitely many rational affine pieces. The penalty is also a finite convex maximum. Thus $E$ is a finite expression using rational affine combinations, maxima and subtraction.

Replace its unit-log coordinates by the actual global PL functions (2.4). BJ's rational PL space is a vector lattice (S1 LF962--1008), so this expression is a global algebraic PL function agreeing exactly with the local selected weight near the chosen compact set. This construction does not require a positive extension. It also does not identify PL on a polytope with PL on the original bundle without constructing the displayed algebraic functions.

### 2.3. Support-controlled gluing without multiplying PL functions

For compact $K\subset U\subset X^{\rm an}$, choose a continuous bump $b$, equal to one on a neighborhood of $K$, with compact support in $U$. Approximate it by a global rational algebraic PL $p$ with error less than $1/8$, using BJ 2.2 and its lattice proof. Put
$$\chi=\min(1,\max(0,2p-1/2)). \tag{2.5}$$
Then $0\le\chi\le1$, it is one near $K$, and
$$\operatorname{Supp}\chi\subset\{p\ge1/4\}\Subset U.$$ 
Outside $U$, $p<1/8$, and the compact threshold set misses the complement of $U$. This proves controlled support, rather than simply extending a bump by zero.

If finitely many local extensions $E_i$ agree with one continuous function $f$ on opens containing $\operatorname{Supp}\chi_i$, and some $\chi_i=1$ near every point of $K$, choose rational $C$ larger than all necessary compact bounds. Then
$$E=\max_i\bigl(E_i-C(1-\chi_i)\bigr) \tag{2.6}$$
equals $f$ near $K$. Indeed a positive $\chi_i$ puts the point in its agreement chart, where its expression is at most $f$; for $\chi_i=0$ the choice of $C$ suppresses the bounded global $E_i$; a winning $\chi_i=1$ gives equality. Only the tested compact neighborhood is used when $f$ is local. For a global $f$ the same argument applies on all of compact $X^{\rm an}$.

Choose another cutoff $\eta$ equal to one near $K$ with support compact in $U$, and rational $B>\sup_{\operatorname{Supp}\eta}|E|$. The compact signed extension
$$\widetilde f=\max(-B\eta,\min(B\eta,E)) \tag{2.7}$$
equals $f$ near $K$, vanishes on a neighborhood of $X^{\rm an}\setminus U$, and satisfies $|\widetilde f|\le B\eta$. Multiplication of two variable PL functions has **not** been used. A product $\eta E$ need not be PL.

Given a finite open cover, choose compact shrinkings $K_i\subset U_i$ covering $X^{\rm an}$ and cutoffs $\chi_i$ as above. The actual rational PL partition is
$$\rho_1=\chi_1,\qquad \rho_i=\min(\chi_i,1-\sum_{j<i}\rho_j). \tag{2.8}$$
Induction gives $\sum_{j\le i}\rho_j=\min(1,\sum_{j\le i}\chi_j)$. Thus every $\rho_i\ge0$, its support is compact in $U_i$, and $\sum_i\rho_i=1$. No variable denominator occurs.

### 2.4. Exact differences in one actual ample class

For any finite list $a_i\in\operatorname{PL}(X)$, BJ 2.25--2.26 gives $a_i=a_i^+-a_i^-$ with $a_i^\pm=c_i^\pm q_i^\pm$, $c_i^\pm\in\mathbb Q_{\ge0}$ and $q_i^\pm\in H(H)$. Choose a common rational $R\ge c_i^\pm$ and set
$$q_{i,R}^\pm=c_i^\pm q_i^\pm+(R-c_i^\pm)0\in H(RH). \tag{2.9}$$
The zero is the actual canonical FS metric on $H$. Tensor products of the generating sections prove the asserted FS membership; denominators are cleared once for the finite list. Thus $a_i=q_{i,R}^+-q_{i,R}^-$ exactly. In original frames $e_\alpha=g_{\alpha\beta}e_\beta$ of $H$, both terms have weights $Rh_{0,\alpha}+q_{i,R}^\pm$ and transition $g_{\alpha\beta}^{NR}$ on the cleared tensor power. Their difference is $a_i$. This is the same algebraic bundle, same cocycle, same reference and same class. Positivity of an abstract numerical class alone is not used.

## 3. Audit and reconstruction of the continuous contact metric bridge

Let a continuous rational contact metric be **already glued** on an ample rational $L$. In a standard very ample frame $e=s_j$ of $qL$, its canonical reference weight is
$$h_{0,j}=q^{-1}\max_l\log|s_l/s_j|,$$
with the $l=j$ term giving a zero floor. Its actual potential is $\phi=b_j-h_{0,j}$, independent of the frame. The finite-floor zero reductions and Section 2 extend its local rational selected weights exactly. Formula (2.6), on the finite compact cover of $X^{\rm an}$, proves
$$\phi\in\operatorname{PL}(X)$$
on the original variety and original $L$.

BJ 2.7/2.31 now supplies an actual algebraic test-configuration line bundle $\mathcal L$ with generic bundle $L$ and model function $\phi$. Take relative integral closure inside that prescribed generic fiber, not absolute normalization. Complete at the test parameter after clearing rational tensor weights over $K=k((t))$, $|t|=e^{-1}$. The model metric is exactly the pullback of the original metric: for a flag ideal its norm is the maximum of the norms of the **separate** ideal generators $a_\lambda t^{-\lambda}$; differences preserve equality. This is an equality at all $K$-analytic points, not only the Gauss section. The model identification uses the original $L$ and its original cocycle.

This is a new resolution of the algebraization dependency in the supplied bridge. GM 2.4 algebraizes a formal blowup ideal, while GM 2.6 cites the separate GK17 8.13 for arbitrary formal line-bundle algebraization (S4 LF249--295). That latter full proof is not in the authorized caches. Here no arbitrary formal line bundle is algebraized: the algebraic test configuration was constructed **first** by BJ's flag-ideal representation. Proper formal-model refinements in the following primary criteria remain background theorems with their precise applications; a title is not presented as their proof.

Over a completed algebraic closure of $K$, pull back a contact support through any smooth analytic curve map into an ordinary weight chart. It becomes
$$h_x=\sum_j a_j\log|f_j|+C,$$
harmonic by Thuillier 2.3.21. If $b-h$ has a local maximum $M$ for any harmonic $h$, then $h_x-h\le b-h\le M$ with equality at $x$. The harmonic maximum principle forces $h_x-h=M$ nearby and then $b-h=M$ nearby. Thuillier 3.1.12 gives subharmonicity. This proves the curve test from supplied local expressions; it does not pull back arbitrary positive currents. For decreasing local approximants, restrict **each** one first and use Thuillier 3.1.8(ii) afterwards. A bounded floor excludes the identically $-\infty$ alternative.

The completed model metric is already rational PL on the original bundle. GR 5.1/5.4, whose full proofs are pinned at S8 LF803--926, therefore give semipositivity on each ordinary point neighborhood. GR's proof lifts the generic reduction point of an entire proper residual curve, retaining the interior condition; its local curve-lifting theorem is pinned at LF489--800. GM 3.11 tests every proper residual curve of the represented global model, using its generic reduction point, a neighborhood and a common dominating model. The closure of that point's reduction remains the **entire** proper curve (S4 LF754--782). GM 3.5 and 3.3 then test nefness on the already supplied algebraic model and detect it before field extension. There is no positivity assertion from a Laurent G-cover alone. GR Remark 1.8 leaves the unrestricted current converse unknown.

BE 7.8 now applies over the nontrivial $K$ to the ample $L_K$. It interpolates the nef model with an ample model of the **same** generic bundle. The resulting semiample models give uniform pure FS approximation. The printed $H/A$ switch in its proof is resolved by using one ample model consistently.

For exact descent, expand each pure FS section on $mL_K$ in the finite $k$-space $H^0(X,mL)$:
$$s_j=\sum_{r\ge r_0}t^r f_{jr}.$$
At the independent-variable Gauss lift of $x$, the FS potential is
$$m^{-1}\max_{j,r}\{\log\|f_{jr}(x)\|_{mh_0}-r\}. \tag{3.1}$$
Every $k$-section has norm at most one in the canonical metric, by its valuation-ring center. The left side is finite continuous on compact $X^{\rm an}$, so has a finite lower bound. Every sufficiently large $r$ term lies uniformly below that bound. The infinite maximum is therefore **exactly** a finite cutoff. Retained coefficients generate, since a common algebraic zero would contradict finiteness and the same tail bound. They are sections of the original $mL$, with rational weights. Uniform errors survive Gauss restriction. BE 7.6 or BJ decreasing closure yields genuine continuous PSH on the original $L$ over $k$.

For a continuous target choose uniform errors $\epsilon_j=4^{-j}$ and shifts $B_j=2\sum_{i\ge j}\epsilon_i$. Then shifted FS approximants decrease, since the consecutive lower bound is $2\epsilon_j-\epsilon_j-\epsilon_{j+1}>0$. This proves the continuous contact bridge without any assertion that every continuous weak metric has global rational weak approximants.

## 4. Genuine collars and bounded local weighted products

The supplied round75 collar is reconstructed, including its reference. On a principal chart (2.2), write the finite defining constraints as $F_j/a^m$. Enlarge $m$ so its tensor power is very ample and append a complete section system; its ratios generate the **original** affine chart ring. Rational strict margins and a negative floor give an actual FS local weight $v$ on a fixed ample $H$, with
$$Q=\{v\le0\}\Subset U,\qquad P=\{v\le-\epsilon\},\qquad x\in\operatorname{int}P.$$ 
If the tensor denominator is $q$, the weight is $q^{-1}\max(q\lambda,\log|F_j/a^m|-C_j)$; the thresholds are $C_j$, not $qC_j$. Generator bounds ensure compactness. Write $v=h_0+p$ in that frame, with $p$ its actual global FS potential and $\omega=c_1(H)$.

Let $u_i$ be a finite tuple of bounded local decreasing contact limits on a neighborhood of $Q$, including a bounded test if needed. Choose rational $M$ bounding the limits there and rational $A$ with $A\epsilon>2M+2$. Put $h=Av+M+1$. On $P$, $h<-M$; on the compact outer strip $v\ge-1/(2A)$, $h\ge M+1/2$. The closed sets $\{u_{ij}\ge M+1/4\}$ on this strip decrease to the empty set. The finite-intersection property gives one common eventual tail strictly below $h$ on the **whole** strip. This is not Dini's theorem for a discontinuous limit.

Define
$$\Psi_{ij}=\max(u_{ij}-h,0)\text{ on }Q,\qquad \Psi_{ij}=0\text{ outside},$$
and
$$\Phi_{ij}=p+A^{-1}\Psi_{ij}. \tag{4.1}$$
Their actual local metric weights on $H$ are $A^{-1}\max(u_{ij}-M-1,Av)$ inside, and $v$ on a whole reference-winning collar and outside. The contact bridge, applied after clearing $A$, proves that these are genuine metrics on the **same** $H$. Their original cocycle is unchanged. The bounded decreasing limits $\Phi_i$ are genuine finite energy by global decreasing closure. On $\operatorname{int}P$,
$$u_i=A\Phi_i+Ah_0+M+1,\qquad
dd^c u_i=A(\omega+dd^c\Phi_i). \tag{4.2}$$
This is the exact reference identity. $\Psi_i/A$ alone is not a canonical-reference potential. The local product is the restriction of $A^n$ times the genuine **raw** mixed measure of the $\Phi_i$.

For continuous inputs this equals the continuous local product: BJ 7.23 invokes actual BE 8.18, whose proof and fundamental-cycle conventions are pinned; BJ 7.42 supplies continuous locality. CLD 8.7.2 is used only within its continuous locally-uniform premise (S3 LF10432--10449). For bounded decreasing inputs, use BJ 7.19/7.21 on the actual global $\Phi_{ij}$.

Independence is checked on a third smaller shared collar. At every continuous stage the old and smaller collar products agree on their common inner open, because their actual weights and scaling agree there. Pass both genuine decreasing limits against compact continuous tests. In the shared collar different supplied sequences have the same explicit global limit $\max(u_i-h,0)$, zero outside. Their genuine measures therefore agree. This proves sequence, collar and reference independence; the local positive Radon measures glue.

For the bounded test, (4.2) is a genuine decreasing potential plus a fixed continuous local reference. BJ 7.21 supplies weighted convergence for its genuine part; ordinary weak convergence supplies the reference part against compact cutoffs. In that source the correct identity is the test-containing pairing **minus** the zero-test pairing (S1 LF4108--4113); the opposite signs at LF4119--4123 are a printed error. Translate the test below zero, apply the positive weighted-measure lemma to its negative, and subtract in the correct order. Signed tests that are differences of such bounded weights are treated term by term; their difference need not decrease.

## 5. Compact signed IBP from actual global pairings

Let $a$ be a rational algebraic PL test with support $K\Subset U$, and let $u_0,u_1,\ldots,u_{n-1}$ be bounded local contact limits on a common neighborhood of $K$. Choose one genuine collar for the finite tuple and an additional compact cutoff equal to one near $K$. For $a=q^+-q^-$ use (2.9) in one actual ample class $RH$. The positive global mixed measures obtained by adding $q^+$ or $q^-$ separately need **not** be supported in $K$. Their **difference** is: on the open complement of $K$, $a=0$, so $q^+=q^-$ and genuine mixed locality makes their measures equal there. The same argument works on every open where $a$ is constant. Cancellation is retained before any outside contribution is discarded.

For each collar, extend the local reference term in (4.2) to a compact signed algebraic PL $G_0$ agreeing with $Ah_0+M+1$ near $K$, using Section 2. Then
$$F_0=A\Phi_0+G_0\in\widetilde{\mathcal E}^{1}$$
is an actual global signed finite-energy function and equals $u_0$ near $K$. The zero-class curvature of $F_0$ agrees there with $dd^cu_0$. To verify the reference cancellation, do it first for the continuous collar approximants, using continuous local compatibility. The difference of the reference curvature and the curvature of the matching $G_0$ is zero on the same open. Pass the bounded genuine mixed limits in each positive term. Thus that cancellation still holds with the discontinuous bounded other factors.

The symmetric global mixed pairing now gives
$$\int_U a\,dd^cu_0\wedge\bigwedge_{i=1}^{n-1}dd^cu_i
=\int_U u_0\,dd^ca\wedge\bigwedge_{i=1}^{n-1}dd^cu_i. \tag{5.1}$$
Precisely, both sides are the global pairing with the two zero-class entries $(0,a)$ and $(0,F_0)$ in opposite orders, multiplied by the other collar scaling factors. The left test vanishes outside $K$; the signed measure on the right vanishes there by the cancellation just proved. Every remaining integral is of bounded functions over a compact set against finite signed Radon measures. This proves compact IBP without first assuming a weak/global theorem.

One can equivalently prove (5.1) at continuous stages and pass each positive global mixed term using weighted convergence from Section 4. The total variations are bounded by the sum of their fixed positive raw intersection masses. No discontinuous local limit is called locally uniform. No difference of decreasing sequences is called decreasing. Extension of each $u_i$ on all of $U$ is neither needed nor asserted; matching near the controlled support suffices.

## 6. Raw mass, comparison, domination, and smooth membership

### 6.1. The support-controlled telescope

Let $\phi$ be bounded on $X^{\rm an}$, locally a contact limit relative to an actual continuous rational semipositive reference on $L$. For notation first take the canonical reference and write $T=\omega+dd^c\phi$, $T_0=\omega$, and
$$S=\sum_{j=0}^{n-1}T^jT_0^{n-1-j}.$$
These are locally defined products, not presumed global genuine products. Choose a finite common-neighborhood cover and (2.8). In each chart use the **same** local reference $g_i$ for $\phi+g_i$ and $g_i$. Subtract their compact IBP identities:
$$\int\rho_i(T^n-T_0^n)=\int\phi\,dd^c\rho_i\wedge S. \tag{6.1}$$
The signed measures on the right have support compact in that chart, and their weighted integrals agree on overlaps by the genuine-collar construction. Summing is legitimate for this finite cover. Locally, multilinearity gives
$$\sum_i dd^c\rho_i\wedge S=dd^c1\wedge S=0.$$
Consequently the global positive local product has raw mass
$$\int_{X^{\rm an}}T^n=\int T_0^n=(L^n)=V. \tag{6.2}$$
Replacing one factor at a time proves mixed mass $(L_1\cdots L_n)$ with actual rational reference bundles. For a noncanonical semipositive reference, use its actual local weights in both subtracted terms; its genuine reference product has the same raw intersection mass. This is a proof of mass, not probability normalization by definition.

### 6.2. Winning loci and comparison

On a shared collar the two floors are inactive on the inner open and
$$\Psi_{\max(u,v)}=\max(\Psi_u,\Psi_v).$$
Genuine BJ 7.40 therefore proves strict winning-locus locality for the bounded local products, including their Borel winning sets. Equal raw masses (6.2), positivity and $\max(\phi,\psi-\epsilon)$ give
$$\int_{\{\phi<\psi\}}T_\psi^n\le\int_{\{\phi<\psi\}}T_\phi^n. \tag{6.3}$$
Letting $\epsilon\downarrow0$ uses ordinary continuity from below of the Borel measures. There is no envelope assumption in this step.

### 6.3. Divisorial order and an atom test without a Dirac equation

If two bounded locally psh potentials with the same reference satisfy $\phi\le\psi$ at every BJ divisorial point, take their shared collar. On divisorial points inside $Q$ their genuine truncations are ordered; outside $Q$ both are zero. BJ 4.22 orders those global genuine potentials everywhere. Recovering their inactive-floor weights on $P$ proves $\phi\le\psi$ at every point. Density plus usc is not the argument.

Fix any BJ divisorial point $v$. BJ 1.20 realizes it as a central component on an actual relatively integrally closed test configuration; dominate the trivial configuration. BJ 2.33 gives an ample model of the original $L$ on this determination. Its genuine rational FS potential $b$ has raw measure with a strictly positive atom at $v$:
$$m_v=b_E(\mathcal L|_E)^n>0.$$ 
The entire component $E$, its multiplicity $b_E=\operatorname{ord}_E(t)$, and its ample intersection degree are retained. A measure equal to a single Dirac and an inverse equation are unnecessary.

Suppose $\phi\le\psi$ almost everywhere for $T_\psi^n$. Translate $b$ so $b<\phi$ uniformly, possible because both are bounded. For rational $t\in(0,1)$ put $\phi_t=(1-t)\phi+tb$. Local mixed positivity yields $T_{\phi_t}^n\ge t^nT_b^n$. Since $\phi_t<\phi\le\psi$ almost everywhere for $T_\psi^n$, (6.3) and (6.2) imply
$$V\le\int_{\{\phi_t<\psi\}}T_{\phi_t}^n\le V.$$
Thus the complement has zero mass and the positive atom forces $\phi_t(v)<\psi(v)$. Let $t\downarrow0$ and use the divisorial order argument. This proves bounded local domination. It does not assume the local cone already equals the genuine cone, and does not invoke a Dirac solution.

### 6.4. EP supplies the first genuine membership

Assume the genuine ample class has EP. For a bounded usc locally psh $\phi$, take the directed decreasing net of all continuous majorants with common bounds, allowing finite minima. Compact Hausdorff separation proves its pointwise infimum is $\phi$; a sequence is not assumed. EP and BJ 5.17 give continuous genuine envelopes $p_j=P(f_j)$. They belong to the local contact class: on the actual rational $L$ they have uniform rational FS approximants, shifted into decreasing sequences as in Section 3. BJ 13.1, under its explicit EP hypothesis, gives $f_j=p_j$ almost everywhere for $T_{p_j}^n$. Hence $\phi\le p_j$ there, and the **local** domination just proved yields $\phi\le p_j\le f_j$ everywhere. Genuine decreasing closure proves $\phi=\inf_jp_j$ is genuine.

In particular BJ 5.20 supplies this EP premise on smooth projective $X$ in characteristic zero, proving smooth local/global equality for the stated exact local class. For unbounded inputs, floor relative to the same actual semipositive reference and let the floor decrease. For a rational nef bundle with an actual continuous semipositive reference, add $\epsilon A$ with its specified FS reference, apply the smooth ample result, and use BJ varying-class closure as $\epsilon\downarrow0$. The local weights are literally the old weight plus $\epsilon h_A$; a numerically nef class alone would not identify them.

This is the first-membership step missing from the old upper-growth attempt. BJ 12.18 is applied only **after** this step.

## 7. Smooth weak upper growth and controlled removal

This section records the analytic deduction with its geometric background explicit. A weak input $u$ on smooth irreducible affine $Y$ is supplied with one proper birational witness whose pullback is locally a decreasing contact limit, and is finite at the generic trivial seminorm. Assume the usual characteristic-zero compactification, projective domination and resolution construction, yielding a smooth projective $X\supset Y$, an effective ample boundary, and a smooth projective morphism $\bar\pi:Z\to X$ dominating that **one** witness over $Y$. These are standard geometric resolution/Chow inputs, not consequences of the analytic proof or pinned Stacks webpages; no full proof of them is claimed in this deliverable.

For completeness the boundary sign is determined: a boundary blowup has effective exceptional $E$ with $-E$ relatively ample. If $D$ is the old ample boundary and the center is supported there, $m\pi^*D-E$ is ample for large $m$ and effective with positive coefficient on every new boundary component. Iterating retains exactly $X\setminus Y$ as support. Choose $B=\mathcal O(rD)$ very ample, its boundary section $s$, and a rational complete FS metric $h=h_0+p$. Shift so
$$g=-\log\|s\|_h=g_0+p\ge1.$$
It is a proper exhaustion tending to infinity at the boundary. Localization (2.1) expresses every original generator and each regular branch of an AFS upper bound as $F/s^d$. Finite section-norm bounds give $\log|F/s^d|\le dg+C_F$. Thus the assumed **upper** growth $u\le H+C$ implies $u\le Ag$ for a rational $A$. The printed lower-growth convention in Wu is not used.

For rational $c>1$ and $M<0$ define, relative to the actual nef metric $cA\bar\pi^*h$,
$$\Psi_M=\max(\bar\pi^*u-cA\bar\pi^*g,M)\text{ over }Y,
\qquad\Psi_M=M\text{ elsewhere}. \tag{7.1}$$
The bound is at most $-(c-1)A\bar\pi^*g$, so each floor has a whole constant boundary collar. Its actual local weights are contact limits with that fixed pulled reference. Section 6.4 on smooth $Z$, including its nef reference argument, gives genuine membership. Let $M\downarrow-\infty$. The limit is nontrivial because the original input is finite at its generic point.

The canonical potential is $Q_M=\Psi_M+cA\bar\pi^*p$. BJ 5.13 applies to the smooth target $X$ with class $cA c_1(B)$: approaching larger **target-side** ample classes have smooth EP. The descended genuine $Q$ equals
$$Q=u-cAg+cAp=u-cAg_0\text{ on }Y,$$
and is $-\infty$ on the boundary, by literal pullback equality and analytic surjectivity. Only now apply BJ 12.18(iii) and Example 3.9 to obtain a decreasing rational FS sequence on the **same** $cAB$. In the boundary-section frame the weights decrease to $u$. Append the constant branch and a complete sufficiently high very ample section system with low rational weights, dominated by each continuous metric on compact $X^{\rm an}$. The values do not change. Their ratios retain every original affine generator. This is actual upper-growth AFS regularization, with exact values and original ring.

### 7.1. Controlled bounds by expanding collars

For an already AFS-regularizable $v\le g$, first compactify the actual AFS reference $g$: clear its positive slopes, include their integer powers **and** all original generators at dominated low weights, and take the projective closure. Its standard chart is exactly $Y$. Powers alone would not establish this.

Take rational $C_r\downarrow-\infty$, $R_r\uparrow\infty$ with $R_r>2-C_r$, and an increasing subsequence of supplied approximants $v_{j_r}<g+1$ on $\{g\le R_r\}$. The latter choice follows from decreasing compact superlevel-set emptiness. Set
$$\phi_r=\max(v_{j_r}-2g,C_r)\text{ on }\{g\le R_r\},\qquad
\phi_r=C_r\text{ outside}. \tag{7.2}$$
The continuous contact bridge gives genuine metrics in twice the actual reference bundle; the outer reference wins on a whole collar. On the expanding annulus the new first branch is at most $1-g\le1-R_{r-1}<C_{r-1}$, and the old function is its old floor. This proves the global decrease, including that annulus. The limit is $v-2g$ on $Y$, and $-\infty$ on the boundary.

Uniform rational FS approximation with summable shifts gives a decreasing FS sequence converging to these truncations' limit. After exact original-generator conversion its affine weights $w_r$ satisfy
$$w_r\downarrow v,\qquad w_r\le2g+B$$
for one constant $B$. Equivalently one can first use genuine decreasing closure for the limit in (7.2), then genuine same-class regularization and a common upper bound on its first approximant. No smoothness or singular EP is used in this controlled step.

### 7.2. Principal-open removal and the values on the original witness

Let $f\ne0$ and let $v$ be actual AFS-regularizable on $Y_f$, bounded above by an AFS reference $g$ from $Y$. For rational $c>0$ take
$$g_c=\max(g,-(c/3)\log|f|)$$
as an actual AFS exhaustion of the original localized ring, including $f^{-1}$. Controlled approximants $w_i\le2g_c+B$ give
$$w_i+c\log|f|\le\max(2g+c\log|f|,(c/3)\log|f|)+B. \tag{7.3}$$
On every bounded neighborhood of $Z(f)$ the right side tends to $-\infty$. Floors $D_i\downarrow-\infty$ make $b_i=\max(w_i+c\log|f|,D_i)$ continuous contact functions on $Y$, equal to $D_i$ on an actual neighborhood of each removed point. Polynomial degree bounds give one AFS $h\ge1$ on $Y$ dominating all $b_i$. Applying whole-floor collars to $b_i-2h$ puts each in the same genuine ample class on the reference compactification. Their decreasing limit and genuine sequential regularization prove an actual AFS extension of
$$v_c=v+c\log|f|\text{ on }Y_f,\qquad v_c=-\infty\text{ on }Z(f).$$

Now use smooth EP, rather than incorrectly assuming these $v_c$ decrease as $c\downarrow0$. On the smooth ample-boundary compactification put their canonical potentials in one fixed ample class, subtracting a common large multiple of $g_0$. The genuine tail envelopes $(\sup_{j\ge m}Q_j)^*$ decrease. On $Y_f$, with $a=\log|f|$ finite,
$$\sup_{j\ge m}c_j a=c_m\max(a,0),$$
including its generally unattained zero value when $a<0$. Their limit is a genuine extension of $v$ with the original upper bound, and a same-class sequence gives its actual AFS regularization.

Exact uniqueness, including agreement with a given original weak $u$, uses **the same original resolved witness**. Pull back the regularized extension and $u$ there. Every divisorial point of that integral birational witness has generic algebraic support; since $f$ is nonzero in its function field, it lies over $Y_f$. Thus the two functions agree at all those points. Near any tested point floor both local functions by the same constant, use the same reference and genuine collar, and apply the divisorial order argument of Section 6.3 in both directions. Let the floor tend to $-\infty$. Their values agree at every tested analytic point, including the removed and exceptional sets. Neither dense-open equality plus usc nor an assertion about lifting a prescribed net is used.

The analytic smooth gate in this section is therefore established under the explicitly retained standard geometric witness construction. It is not a general-field affine theorem over every completed residue field.

## 8. Independent nonflat trace audit and its present limit

The embedded norm-law proposals can be checked algebraically without assuming a weak-trace theorem. Let $A$ be normal integral and $B$ finite integral over it, both finite type in characteristic zero, and set $d=[\operatorname{Frac}B:\operatorname{Frac}A]$. For finite module generators $b_i$, the generic norm $N(\sum T_i b_i)$ and all characteristic coefficients lie in $A[T]$: their conjugate products are integral and belong to the fraction field, and $A[T]$ is normal. Translation by every module relation, multiplication, homogeneity, and Cayley--Hamilton are polynomial identities, valid generically and hence over $A$. Tensoring a finite presentation is right exact, so they define the specialized law on every $B\otimes_A\mathcal H(s)$, including new fiber relations.

Over an algebraic closure of $\mathcal H(s)$, its unit-group character is trivial on the nilpotent units. Indeed the finite polynomial logarithm identifies them with an additive vector group, which has no invertible nonconstant polynomial character. On the residue torus, comparison in $P(xy)=P(x)P(y)$ gives one monomial. Polynomiality gives nonnegative integer exponents and homogeneity makes their sum $d$. Every exponent is positive: otherwise the idempotent zero on that factor and one elsewhere would have nonzero norm and hence be invertible by the specialized characteristic identity, a contradiction. Multiplying an exponent by the separable residue degree gives canonical integers $m_y>0$ on the actual analytic fiber, summing to $d$. Unique norm extension over complete fields and residue-factor degree sums prove compatibility with every complete residue-field extension. On the flat locus these are usual Artinian length times residue degree; nonflat fiber dimensions are not substituted.

For $u=D^{-1}\max_i(\log|b_i|+w_i)$, with a constant floor, expand the actual polynomial $N(\sum T_i b_i)=\sum a_\alpha T^\alpha$. Multiplicativity of arbitrary-radius weighted Gauss norms yields the **whole-base** identity
$$\sum_y m_yu(y)=D^{-1}\max_{|\alpha|=d}\left(\log|a_\alpha|+\sum_i\alpha_iw_i\right). \tag{8.1}$$
The constant-floor coefficient is nonzero. Original base generators are retained by appending dominated branches, using their polynomial expressions in retained source generators. Thus this is actual AFS. The weight bound gives $\|N_\pi a-N_\pi b\|_E\le d\|a-b\|_{\pi^{-1}E}$; only a **continuous** decreasing limit invokes compact Dini. A trace of a clopen indicator is continuous and integer valued, hence locally constant; disconnected opens need not share its integer.

Here are the two necessary elementary details. For weighted Gauss multiplicativity, choose the lexicographically largest exponent among maximal-weight terms in each polynomial. Their sum has a unique contribution among pairs of maximal-weight terms: equality of the sum with a different pair would force one exponent to exceed its selected lexicographic maximum. Lower-weight pairs cannot cancel that coefficient. This works at arbitrary positive real radii, including those outside the coefficient field's value group.

To justify continuity also for a clopen indicator or any continuous input on a compact preimage, differences of actual AFS form a rational vector lattice: positive sums and maxima distribute, and $\max(a-b,c-d)=\max(a+d,c+b)-(b+d)$. Generator branches at sufficiently low intercepts make rational constants available on the compact set. Truncated norms of a distinguishing regular function separate its seminorms. For a continuous target, approximately interpolate at each pair $x,y$ using separation and rational scaling; a finite maximum over $y$ supplies its lower bound everywhere and upper bound near $x$, and a finite minimum over $x$ supplies both bounds everywhere. Thus these differences are uniformly dense there. Their traces are continuous by (8.1), and the degree bound passes continuity to the limit. Applied to an indicator of a clopen piece over an open base neighborhood, its trace is exactly the integer sum on that piece. Only local constancy follows.

As an exact diagnostic, $A=k[x,y]$, $I=(x,y)$ and $B=A\oplus Iz$ inside $z^2=x$ has generic degree two but fiber dimension three at the origin. Its norm is $N(a+uz)=a^2-xu^2$, which specializes to $a(0)^2$. Its sole fiber point has canonical weight two, not three.

This audit proves the finite logarithmic test formula; it does not itself identify an arbitrary weak trace at every nonflat point. Section 7 supplies the smooth open regularization/removal prerequisite in its retained geometric setting. To finish the whole weak trace application, the normalized line slice, proper lift to the single witness, local Gauss map $t=cz^e$, all residue-field refinements, and the limiting equality must be checked together for that input. The embedded radial proof remains a proposed application, not an automatically accepted theorem. In particular no affine regularization theorem over arbitrary $\mathcal H(s)$ follows from Section 7.

## 9. Genuine global equation theory and remaining singular obligations

BJ's conventions (S1 LF435--469) allow reduced nonnormal varieties, and Section 7 explicitly resumes general projective scope (LF3649--3658). Its genuine finite-energy operator is available on that scope. On a relatively integrally closed test configuration its raw model measure is
$$\sum_E b_E\bigl((\omega_{\mathcal X}+D)|_E\bigr)^n\delta_{v_E},\qquad
b_E=\operatorname{ord}_E(t),\quad v_E=b_E^{-1}\operatorname{ord}_E|_{k(X)}.$$ 
The fundamental-cycle multiplicities and vertical DVRs are essential. The generic fiber is the original nonnormal variety. BJ 7.18 extends the actual mixed intersection pairing to a positive Radon operator; 7.19 gives raw mass $V=(L^n)$ and genuine decreasing continuity. This is not an auxiliary inverse measure construction.

Write
$$E_\omega(\phi)=\frac{\langle(\omega,\phi)^{n+1}\rangle}{(n+1)V},\qquad
\mathcal E^1=\{\phi\in\operatorname{PSH}(\omega):E_\omega(\phi)>-\infty\}.$$
The exact raw target is a positive Radon $\nu$ with $\nu(X^{\rm an})=V$ and, for $\mu=\nu/V$,
$$E_\omega^\vee(\mu)=\sup_{\psi\in\mathcal E^1}\left(E_\omega(\psi)-\int\psi\,d\mu\right)<\infty.$$ 
BJ 9.20 equates this intrinsic condition with integrability of every genuine finite-energy potential on irreducible $X$; there is no support restriction. BJ 10.4/10.6 give uniqueness modulo one real constant and genuine domination without EP.

Existence is not unconditional on singular $X$. The actual general-variety theorem is BJ **12.8**, equating genuine EP with onto finite-energy MA. Under EP its proof takes a normalized dual maximizing sequence, uses weak PSH compactness, a bounded-energy estimate and target integral continuity (9.19), then energy usc to get an actual maximizer. Genuine energy differentiation identifies its MA. The raw objective $VE-\int\phi\,d\nu$ is constant invariant exactly at mass $V$. This proves existence on smooth $X$ using 5.20, but requires a proved singular EP on the requested target.

The remaining chain is concrete:

1. Complete the weak whole-base trace application just identified, then reprove the split-piece maximum principle with the original witness, fixed hull neighborhood, positive canonical weights and a locally constant integer sum on **all** subsequently tested fibers. Complete descending-$Z$, strict Hartogs and reduced-singular-stratum inductions, with Runge before coefficient radii and the final empty-$Z$ globalization.
2. Establish resolved-nef fiber constancy using actual varying-class metric references and curve-morphism restrictions, geometrically connected fibers over every completed residue field, and the divisorial minimum-usc descent. The supplied Stacks paraphrases have not been promoted to pinned primary proofs.
3. Obtain countable rational geometrically unibranch EP. Wu v1's complete envelope proof at LF2697--2755 expressly invokes its Proposition 2.24 and weak/global Theorem 6.5 at LF2705--2717. Its printed statement is not an independent validation of those gates.
4. Complete finite-data descent to arbitrary algebraically closed trivial $k$, preserving nonnormal generic fibers, relative integral closure, vertical $R_1,S_2$, component multiplicities, positive raw mass, orthogonality and domination. Individual finite PL/model obstacles and competitors may use different countable enlargements; arbitrary PSH competitors do not simultaneously descend.
5. Prove target-side approaching EP before normalization onto; retain the degree-one fundamental-cycle projection, continuous pairing compatibility, and unbounded $\mathcal E^1$/MA compatibility. Then apply the actual singular compactness/differentiation/attainment theorem to every target above.

These are indispensable missing applications, not nonexistence results and not a counterexample to corrected upper growth. The printed lower-growth quadratic diagnostic is not used to reject EP. An abstract completion or the finite trace law does not solve P16.1. No original problem is declared closed.

## 10. Reproduction, evidence, and epistemic status

Run `python3 rerun.py` in this workspace. It preserves `input.json` byte identically as `input-original.json`, retains the exact task value and assignment string, checks all 23 supplied primary-file hashes, copies only authorized sources, and pins 43 literal statement/proof units. Inclusive one-based coordinates use UTF-8 bytes decode and `split('\n')`. Source versions, whole-file hashes, literal bodies, applications and limits are in `source-extracts/source-provenance.json`.

Existing Pandoc generates `P16.1-paper.tex`; existing pdfLaTeX runs twice to create `P16.1-paper.pdf`. Exact argv, stdout/stderr, both pass logs, environment versions and output hashes are retained. The finite checks concern the PL saturation partition, compact clipping, collar margins, summable shifts and quadratic norm identity on explicitly declared finite rational grids. They are exhaustive only there. Compilation, matching hashes and finite arithmetic are **observations**, not mathematical correctness certificates.

`status.json` has exactly `id`, `status`, `exact_result`, `proof_file`, `concrete_gaps`. `canonical-notes.json` has at most four backward-supported local notes. All mathematical arguments and combined primary applications remain unverified drafts; no independent review is claimed. Only the supplied input, authorized primary caches and fresh workspace were read. No installation, other worker/model/subagent, network request, private/campaign read, source edit, message or runtime/auth change was used. No resource-heavy computation was needed. No supervised compute service was exposed.

## Primary bindings

S1: Boucksom--Jonsson, *Global pluripotential theory over a trivially valued field*, 1801.08229v4. S2: Wu, *On the local theory of non-archimedean psh functions*, 2609.27610v1, public September 2026 v1. S3: Chambert-Loir--Ducros, 1204.6277v2. S4: Gubler--Martin, *On Zhang's semipositive metrics*, 1608.08030v3. S5: Wanner, 1801.04713v3. S6: Thuillier thesis, tel-00010990v1. S7: Boucksom--Eriksson, *Spaces of norms, determinant of cohomology and Fekete points in non-Archimedean geometry*, 1805.01016v3. S8: Gubler--Rabinoff, *On semipositive piecewise linear functions in non-archimedean analytic geometry*, 2503.05513v1. S9: Ducros, published *Confluentes Mathematici* 4(4), 1250007, DOI10.1142/S1793744212500077. S10: Gubler--Jell--Rabinoff, *Forms on Berkovich spaces based on harmonic tropicalizations*, 2111.05741v3.



END MATHEMATICAL DATA



BEGIN MATHEMATICAL DATA: Original context 3: Binding of the precise round77/actual80 scope

# Binding reading clarifications from actual round80 review

- Section7: 'smooth projective morphism' means projective birational domination with smooth projective source, retaining the explicit original resolution-witness antecedent.

- Harmonic logarithms are logarithms of units on their indicated domains.

- The H/A naming switch in BE7.8 is a source naming typo.

- The weighted pairing is the test-containing pairing minus the zero-test pairing.

- IBP formulas are for dimension n>=1; reduced irreducible dimension-zero X is one point and its empty product has raw mass one.

These are exactly the harmless interpretations retained by the actual PASS. They do not discharge any conditional geometric antecedent or prove singular EP.



END MATHEMATICAL DATA



BEGIN MATHEMATICAL DATA: Original context 4: TASK-GRANTED actual80 partial review

{
  "verdict": "PASS",
  "report": "The retained PARTIAL scope is correct under its stated contact hypotheses and conditional geometric witness antecedents. This verdict does not close P16.1 or establish singular EP. No supplied draft or note was treated as granted background.\n\nFor n1, original-ring section localization works without normality: localization commutes with the finite matching conditions on an affine trivializing cover. The extra factor s in a=s∏τ_i preserves the original boundary. Clipped section-ideal logarithms give exact logarithms near the tested compact set. On the specified rational domains, density in the localized original ring and the strict ultrametric approximation inequality give identical unit norms, including after complete field extension. Ducros supplies precisely the compact Γ-strict norm-image theorem required here. Refinement by branch-equality hyperplanes, rational triangulation, affine interpolation and the finite wall penalty establish the polyhedral extension and DC decomposition. The cutoff, maximum-penalty gluing, clipping and saturation partition use lattice operations, with no multiplication of variable PL functions. Padding the finite FS decompositions by the canonical zero metric gives differences in one actual ample rational bundle, with the original cocycle and reference.\n\nThe continuous contact bridge correctly constructs the algebraic model before testing positivity. Relative integral closure preserves the nonnormal generic fiber. The flag-ideal identity holds at every Laurent analytic point because the homogeneous generators remain separate generators; it is not merely a Gauss-section identity. Unit-log supports pull back to harmonic functions. The same-constant contact equality proves the harmonic maximum test. The supplied harmonic-test proof can be checked directly, and decreasing subharmonic limits follow from compact boundary comparison; bounded floors exclude the identically −∞ case. The harmonic analytic inputs are corroborated by Wanner’s accessible primary treatment. GR is applied to already represented PL weights and tests curves throughout ordinary neighborhoods. Its residual-curve argument retains properness, the generic reduction point and the interior condition. GM consequently detects nefness of the represented model before field extension. BE interpolates models of the same generic bundle. The coefficient expansion at the independent-variable Gauss lift has an exact finite cutoff: canonical coefficient norms are at most one, while the continuous FS potential has a uniform finite lower bound. A common zero of the retained coefficients would contradict that bound. Thus the descended approximants use the original mL and rational weights.\n\nFor n2, the collar construction retains v=h₀+p and Φ=p+Ψ/A. Compact decreasing superlevel-set emptiness supplies a common eventual tail on the entire outer strip; this does not require uniform convergence to a discontinuous limit. On the inner open, u=AΦ+Ah₀+M+1, so the raw mixed product carries Aⁿ. A third shared collar proves independence using continuous compatibility followed by genuine decreasing convergence. Weighted convergence treats the genuine potential and fixed continuous reference separately. The correct pairing identity is test-containing pairing minus zero-test pairing; translating the test below zero permits the positive weighted-measure lemma to be applied to its negative.\n\nCompact signed IBP is valid. The two positive measures associated with q⁺ and q⁻ need not individually have controlled support. Their difference vanishes outside the support of a because q⁺=q⁻ there and genuine mixed locality applies. Matching-reference curvature cancellation is first checked continuously and then passed term by term through the bounded genuine limits. Symmetry of the global pairing gives IBP with the remaining collar factors and scaling retained. The partition telescope then proves raw intersection mass, rather than defining it by normalization. Borel strict-winning locality and displaced maxima give bounded comparison. Every BJ divisorial point admits an ample-model measure with atom b_E(ℒ|E)ⁿ>0 before any inverse Dirac equation is invoked. Mixing with this bounded FS potential, comparison and equal mass prove local domination. Divisorial order follows through shared genuine truncations, rather than density plus usc.\n\nThe EP membership argument establishes first membership correctly. Continuous majorants form a decreasing net on the possibly nonmetrizable compact analytification. EP gives continuous genuine envelopes; orthogonality and the independently established local domination place the original bounded local potential below each envelope. Decreasing closure gives membership. Smooth characteristic-zero EP supplies the smooth instance. Floors and varying-class closure extend it to the stated unbounded and nef cases with actual semipositive references. Sequential regularization is used only afterwards.\n\nFor n3, the geometric compactification, projective birational domination and resolution witness remain conditional hypotheses. They are not inferred analytically. The boundary sign mπ*D−E, the exhaustion g=g₀+p, original-generator localization and upper-growth estimate are correct. Whole boundary collars give genuine membership for the nef truncations on the smooth witness. Birational descent uses approaching EP on the smooth target, exactly as BJ 5.13 requires. Subsequent FS regularization uses the same actual bundle, and dominated complete-system branches retain the original generators without changing values. Expanding collars decrease on the old region, the new annulus and the exterior separately. Their upper controls give a common bound for the regularized sequence. Principal-open logarithmic penalties have the asserted vanishing behavior near the removed set. Their removal uses decreasing tail envelopes, not a falsely decreasing sequence in c. Equality with the original weak input is proved in both directions on the same resolved witness: its divisorial points have generic algebraic support and therefore lie over Y_f. Shared floors and collars then identify every removed and exceptional value.\n\nThe nonflat norm argument is self-contained and correct. Normality of A puts the generic norm and characteristic coefficients in A[T]. Universal polynomial identities and right exactness of specialization handle new fiber relations. After algebraic closure, the norm character is trivial on nilpotent units and is a residue-torus monomial. Cayley–Hamilton makes every exponent strictly positive. Multiplication by separable residue degrees gives canonical positive integer weights totaling d, compatible with complete residue-field extensions. Weighted Gauss multiplicativity holds at arbitrary positive radii by the unique maximal lexicographic contribution. This proves the whole-base finite AFS formula. The lattice-density argument and the degree bound prove continuity for continuous inputs; indicator traces are locally constant, not necessarily constant on disconnected opens. In the diagnostic example, the origin has weight two despite fiber dimension three.\n\nHarmless wording clarifications are required. “Smooth projective morphism” in Section 7 should read “projective birational domination with smooth projective source,” as required by the stated resolution-witness antecedent and BJ 5.13. Logarithms asserted harmonic are logarithms of units. The H/A switch in BE 7.8 is a naming typo. The reversed signs in BJ 7.21(ii) must be read with the corrected pairing order stated above. Positive-dimensional IBP formulas are understood for n≥1; for reduced irreducible zero-dimensional X, X is one point and the empty product has raw mass one. None of these clarifications requires a new substantive argument.\n\nThe mathematical limitations in n4 are accurate. The genuine reduced-projective finite-energy operator, its raw mass, intrinsic dual-energy condition and uniqueness are available independently of singular EP. [BJ Theorem 12.8](https://arxiv.org/pdf/1801.08229v4#page=121) makes onto finite-energy MA equivalent to EP. Its variational proof retains compactness, bounded-energy control, target integral continuity, energy usc and actual attainment. [Wu’s envelope proof](https://arxiv.org/pdf/2609.27610v1#page=51) explicitly uses its resolved-nef descent and weak/global gates. The present argument leaves whole-base weak radial trace, Runge and singular induction, resolved-nef fiber descent, arbitrary-cardinality finite-data descent and normalization compatibility unfinished. The finite norm formula and smooth conditional gate do not supply those missing applications. Compilation, hashes and finite arithmetic observations play no role in this verdict.",
  "passages": [
    {
      "id": "e713d8d8-ccee-48b8-a347-4e0378a86db7/0",
      "statement": "For a reduced projective variety X over an algebraically closed trivially valued field, BJ’s rational PL(X) is a vector lattice uniformly dense in C(Xan). Every rational PL potential on an actual rational line bundle L is represented by a test configuration of (X,L). Relative integral closure is taken inside its prescribed generic fiber and preserves that fiber; its local rings at generic points of the central fiber are DVRs. These are BJ Definition 1.10, Theorem 1.13, Theorems 2.2 and 2.7, and Theorem 2.31.",
      "url": "https://arxiv.org/pdf/1801.08229v4#page=21",
      "quote": "stable under finite maxima and minima",
      "premise": 0
    },
    {
      "id": "e713d8d8-ccee-48b8-a347-4e0378a86db7/1",
      "statement": "For a compact Γ-strict k-analytic space W of dimension d and invertible analytic functions f₁,…,f_r on W, Ducros Theorem 3.2 makes their norm image a finite (Q,(|k*|Γ)^Q)-polytope of dimension at most d. In its algebraic reduction, a Γ-rational domain in an algebraic affine analytification can be described using original-ring functions and a nonvanishing denominator h, and A[h⁻¹] is dense in that domain’s affinoid algebra.",
      "url": "https://www.numdam.org/item/10.1142/S1793744212500077.pdf#page=40",
      "quote": "L’image |f|(X) est un c-polytope",
      "premise": 1
    },
    {
      "id": "e713d8d8-ccee-48b8-a347-4e0378a86db7/2",
      "statement": "For a reduced projective variety X over an algebraically closed trivially valued field and an actual ample rational line bundle H, every rational PL function is a difference of nonnegative rational multiples of FS potentials in H(H) (BJ 2.25–2.26). Every BJ divisorial valuation is a central-component valuation on a relatively integrally closed test configuration (Lemma 1.20). Any test configuration dominating the trivial configuration admits an ample model of any prescribed actual ample rational L (Lemma 2.33); its raw model measure has component coefficient ord_E(t)(ℒ|E)ⁿ.",
      "url": "https://arxiv.org/pdf/1801.08229v4#page=18",
      "quote": "Lemma 1.20.",
      "premise": 2
    },
    {
      "id": "e713d8d8-ccee-48b8-a347-4e0378a86db7/3",
      "statement": "On a smooth strictly analytic curve over an algebraically closed complete nontrivially valued field, harmonic functions on compact strictly affinoid domains are described by harmonic functions on semistable finite skeleta. The logarithm of the absolute value of an invertible analytic function is harmonic. Wanner gives this description in §5.3 and proves the unit-log assertion in Proposition 5.3.15.",
      "url": "https://d-nb.info/1136471502/34#page=93",
      "quote": "the function log |f| is harmonic",
      "premise": 3
    },
    {
      "id": "e713d8d8-ccee-48b8-a347-4e0378a86db7/4",
      "statement": "Let K be complete and nontrivially valued, X a good strictly K-analytic space, and h an R-PL function. GR Corollary 5.4 says h is semipositive exactly when, over an algebraically closed analytic field extension F, h_F pulled back by every morphism from a smooth analytic curve over F is semipositive. On a smooth strictly analytic curve, R-PL semipositivity is equivalent to Thuillier subharmonicity (Proposition 5.1). Semipositivity at a point is equivalent to a nef formal representation on an ordinary strictly affinoid neighborhood.",
      "url": "https://arxiv.org/pdf/2503.05513v1#page=17",
      "quote": "for every smooth analytic curve C",
      "premise": 4
    },
    {
      "id": "e713d8d8-ccee-48b8-a347-4e0378a86db7/5",
      "statement": "For a formal metric on an actual line bundle over a separated paracompact strictly analytic space over a complete nontrivially valued field, semipositivity on ordinary point neighborhoods is equivalent to global formal semipositivity (GM Proposition 3.11). A represented formal metric is semipositive exactly when its representing line bundle is nef (Proposition 3.5). Nefness of a formal line bundle is equivalent to nefness after any complete analytic field extension (Lemma 3.3).",
      "url": "https://arxiv.org/pdf/1608.08030v3#page=13",
      "quote": "if and only if L is a nef formal K◦-model.",
      "premise": 5
    },
    {
      "id": "e713d8d8-ccee-48b8-a347-4e0378a86db7/6",
      "statement": "For an actual ample rational line bundle L on a projective scheme over a complete nontrivially valued non-Archimedean field, a continuous metric is nef exactly when it is psh, and hence exactly when it is a uniform limit of pure FS metrics on the same L (BE Corollary 7.6 and Theorem 7.8). The proof approximates a nef model using an ample model with the same generic bundle.",
      "url": "https://arxiv.org/pdf/1805.01016v3#page=49",
      "quote": "Then a continuous metric on L is nef iff it is psh",
      "premise": 6
    },
    {
      "id": "e713d8d8-ccee-48b8-a347-4e0378a86db7/7",
      "statement": "On an n-dimensional projective scheme over a complete valued field, continuous psh-regularizable metrics on actual rational line bundles have symmetric positive mixed Radon measures, with raw mass equal to the fundamental-cycle intersection number, continuous under uniform convergence. Continuous FS-limit metrics on semiample bundles are psh-regularizable. Model Deligne pairings agree with algebraic model pairings, and the measures and pairings retain fundamental-cycle multiplicities and complete-field base-change compatibility (BE 7.14, 8.3–8.5 and 8.18–8.21).",
      "url": "https://arxiv.org/pdf/1805.01016v3#page=65",
      "quote": "Theorem 8.18.",
      "premise": 7
    },
    {
      "id": "e713d8d8-ccee-48b8-a347-4e0378a86db7/8",
      "statement": "Under CLD’s analytic-space hypotheses, if positive closed currents T_j converge to T and continuous functions u_{0,j},…,u_{q,j} converge locally uniformly to u₀,…,u_q, with u_{i,j} psh for i≥1, then u_{0,j} d′d″u_{1,j}∧…∧d′d″u_{q,j}∧T_j converges to u₀ d′d″u₁∧…∧d′d″u_q∧T. This is CLD Proposition 8.7.2.",
      "url": "https://arxiv.org/pdf/1204.6277v2#page=209",
      "quote": "des suites de fonctions continues",
      "premise": 8
    },
    {
      "id": "e713d8d8-ccee-48b8-a347-4e0378a86db7/9",
      "statement": "For a reduced projective variety over an algebraically closed trivially valued field, BJ’s genuine finite-energy pairing extends symmetrically and multilinearly to signed finite-energy entries and defines signed mixed Radon measures. For genuine psh entries these measures are positive, have raw intersection mass and satisfy the central-component model formula. They converge weakly along decreasing genuine finite-energy nets. If ω_i are ample, φ_i∈E¹(ω_i), and a psh test φ₀ is integrable for their mixed measure, decreasing approximations also converge as weighted measures; bounded other factors ensure that integrability. Genuine mixed measures agree on open sets where their potentials agree, and MA(max(φ,ψ)) agrees with MA(φ) on the Borel set {φ>ψ} for φ,ψ∈E¹(ω). These are BJ 7.14, 7.18–7.21 and 7.40–7.42.",
      "url": "https://arxiv.org/pdf/1801.08229v4#page=81",
      "quote": "Theorem 7.18.",
      "premise": 9
    },
    {
      "id": "e713d8d8-ccee-48b8-a347-4e0378a86db7/10",
      "statement": "For a projective variety over an algebraically closed trivially valued field, θ∈N¹(X), φ∈PSH(θ), and an usc function ψ:Xan→R∪{−∞}, the inequality φ≤ψ holds on all of Xan if and only if it holds on BJ’s divisorial points. This is BJ Theorem 4.22.",
      "url": "https://arxiv.org/pdf/1801.08229v4#page=51",
      "quote": "ϕ ≤ ψ",
      "premise": 10
    },
    {
      "id": "e713d8d8-ccee-48b8-a347-4e0378a86db7/11",
      "statement": "For a projective variety over an algebraically closed trivially valued field, a generically finite decreasing limit of φ_i∈PSH(θ_i), with θ_i→θ, belongs to PSH(θ). For an actual ample rational L, continuous genuine L-psh potentials are uniform limits of rational FS potentials on L, and every genuine L-psh potential admits a decreasing sequence in Hdom(c₁(L))⊂H(L). These are BJ 4.5, 4.7, 12.18(iii) and Example 3.9.",
      "url": "https://arxiv.org/pdf/1801.08229v4#page=125",
      "quote": "Corollary 12.18.",
      "premise": 11
    },
    {
      "id": "e713d8d8-ccee-48b8-a347-4e0378a86db7/12",
      "statement": "For an irreducible projective variety over an algebraically closed trivially valued field and an ample class ω satisfying EP, the envelope P_ω(f) of a finite continuous function f is continuous and genuine ω-psh. Moreover, P_ω(f)=f almost everywhere for MA_ω(P_ω(f)). These are BJ Lemma 5.17 and Theorem 13.1, with their explicit EP hypothesis.",
      "url": "https://arxiv.org/pdf/1801.08229v4#page=126",
      "quote": "Theorem 13.1.",
      "premise": 12
    },
    {
      "id": "e713d8d8-ccee-48b8-a347-4e0378a86db7/13",
      "statement": "Every nef class on a smooth connected projective variety over an algebraically closed trivially valued characteristic-zero field has EP (BJ Theorem 5.20). For a projective birational morphism π:Y→X and θ∈N¹(X), if θ is the limit of target classes θ_m such that θ_m−θ is ample and θ_m has EP, then π*:PSH(X,θ)→PSH(Y,π*θ) is a homeomorphism, in particular onto (BJ Lemma 5.13).",
      "url": "https://arxiv.org/pdf/1801.08229v4#page=59",
      "quote": "Lemma 5.13.",
      "premise": 13
    },
    {
      "id": "e713d8d8-ccee-48b8-a347-4e0378a86db7/14",
      "statement": "For reduced irreducible projective X over an algebraically closed trivially valued field and ample ω, set V=(ωⁿ) and E_ω(φ)=⟨(ω,φ)ⁿ⁺¹⟩/((n+1)V). The genuine E¹ Monge–Ampère measure has raw mass V. A positive raw target ν of mass V has finite dual energy exactly when E_ω^∨(ν/V)=sup_{ψ∈E¹}(E_ω(ψ)−∫ψ d(ν/V)) is finite; this is equivalent to integrability of every genuine E¹ potential. Genuine solutions with the same measure differ by one real constant, and genuine domination holds without EP. The normalized genuine MA map onto all finite-dual-energy probability measures is surjective if and only if ω has EP. These are BJ 7.18–7.19, 9.20, 10.4, 10.6 and 12.8.",
      "url": "https://arxiv.org/pdf/1801.08229v4#page=121",
      "quote": "onto",
      "premise": 14
    }
  ],
  "premises": [
    "For a reduced projective variety X over an algebraically closed trivially valued field, BJ’s rational PL(X) is a vector lattice uniformly dense in C(Xan). Every rational PL potential on an actual rational line bundle L is represented by a test configuration of (X,L). Relative integral closure is taken inside its prescribed generic fiber and preserves that fiber; its local rings at generic points of the central fiber are DVRs. These are BJ Definition 1.10, Theorem 1.13, Theorems 2.2 and 2.7, and Theorem 2.31.",
    "For a compact Γ-strict k-analytic space W of dimension d and invertible analytic functions f₁,…,f_r on W, Ducros Theorem 3.2 makes their norm image a finite (Q,(|k*|Γ)^Q)-polytope of dimension at most d. In its algebraic reduction, a Γ-rational domain in an algebraic affine analytification can be described using original-ring functions and a nonvanishing denominator h, and A[h⁻¹] is dense in that domain’s affinoid algebra.",
    "For a reduced projective variety X over an algebraically closed trivially valued field and an actual ample rational line bundle H, every rational PL function is a difference of nonnegative rational multiples of FS potentials in H(H) (BJ 2.25–2.26). Every BJ divisorial valuation is a central-component valuation on a relatively integrally closed test configuration (Lemma 1.20). Any test configuration dominating the trivial configuration admits an ample model of any prescribed actual ample rational L (Lemma 2.33); its raw model measure has component coefficient ord_E(t)(ℒ|E)ⁿ.",
    "On a smooth strictly analytic curve over an algebraically closed complete nontrivially valued field, harmonic functions on compact strictly affinoid domains are described by harmonic functions on semistable finite skeleta. The logarithm of the absolute value of an invertible analytic function is harmonic. Wanner gives this description in §5.3 and proves the unit-log assertion in Proposition 5.3.15.",
    "Let K be complete and nontrivially valued, X a good strictly K-analytic space, and h an R-PL function. GR Corollary 5.4 says h is semipositive exactly when, over an algebraically closed analytic field extension F, h_F pulled back by every morphism from a smooth analytic curve over F is semipositive. On a smooth strictly analytic curve, R-PL semipositivity is equivalent to Thuillier subharmonicity (Proposition 5.1). Semipositivity at a point is equivalent to a nef formal representation on an ordinary strictly affinoid neighborhood.",
    "For a formal metric on an actual line bundle over a separated paracompact strictly analytic space over a complete nontrivially valued field, semipositivity on ordinary point neighborhoods is equivalent to global formal semipositivity (GM Proposition 3.11). A represented formal metric is semipositive exactly when its representing line bundle is nef (Proposition 3.5). Nefness of a formal line bundle is equivalent to nefness after any complete analytic field extension (Lemma 3.3).",
    "For an actual ample rational line bundle L on a projective scheme over a complete nontrivially valued non-Archimedean field, a continuous metric is nef exactly when it is psh, and hence exactly when it is a uniform limit of pure FS metrics on the same L (BE Corollary 7.6 and Theorem 7.8). The proof approximates a nef model using an ample model with the same generic bundle.",
    "On an n-dimensional projective scheme over a complete valued field, continuous psh-regularizable metrics on actual rational line bundles have symmetric positive mixed Radon measures, with raw mass equal to the fundamental-cycle intersection number, continuous under uniform convergence. Continuous FS-limit metrics on semiample bundles are psh-regularizable. Model Deligne pairings agree with algebraic model pairings, and the measures and pairings retain fundamental-cycle multiplicities and complete-field base-change compatibility (BE 7.14, 8.3–8.5 and 8.18–8.21).",
    "Under CLD’s analytic-space hypotheses, if positive closed currents T_j converge to T and continuous functions u_{0,j},…,u_{q,j} converge locally uniformly to u₀,…,u_q, with u_{i,j} psh for i≥1, then u_{0,j} d′d″u_{1,j}∧…∧d′d″u_{q,j}∧T_j converges to u₀ d′d″u₁∧…∧d′d″u_q∧T. This is CLD Proposition 8.7.2.",
    "For a reduced projective variety over an algebraically closed trivially valued field, BJ’s genuine finite-energy pairing extends symmetrically and multilinearly to signed finite-energy entries and defines signed mixed Radon measures. For genuine psh entries these measures are positive, have raw intersection mass and satisfy the central-component model formula. They converge weakly along decreasing genuine finite-energy nets. If ω_i are ample, φ_i∈E¹(ω_i), and a psh test φ₀ is integrable for their mixed measure, decreasing approximations also converge as weighted measures; bounded other factors ensure that integrability. Genuine mixed measures agree on open sets where their potentials agree, and MA(max(φ,ψ)) agrees with MA(φ) on the Borel set {φ>ψ} for φ,ψ∈E¹(ω). These are BJ 7.14, 7.18–7.21 and 7.40–7.42.",
    "For a projective variety over an algebraically closed trivially valued field, θ∈N¹(X), φ∈PSH(θ), and an usc function ψ:Xan→R∪{−∞}, the inequality φ≤ψ holds on all of Xan if and only if it holds on BJ’s divisorial points. This is BJ Theorem 4.22.",
    "For a projective variety over an algebraically closed trivially valued field, a generically finite decreasing limit of φ_i∈PSH(θ_i), with θ_i→θ, belongs to PSH(θ). For an actual ample rational L, continuous genuine L-psh potentials are uniform limits of rational FS potentials on L, and every genuine L-psh potential admits a decreasing sequence in Hdom(c₁(L))⊂H(L). These are BJ 4.5, 4.7, 12.18(iii) and Example 3.9.",
    "For an irreducible projective variety over an algebraically closed trivially valued field and an ample class ω satisfying EP, the envelope P_ω(f) of a finite continuous function f is continuous and genuine ω-psh. Moreover, P_ω(f)=f almost everywhere for MA_ω(P_ω(f)). These are BJ Lemma 5.17 and Theorem 13.1, with their explicit EP hypothesis.",
    "Every nef class on a smooth connected projective variety over an algebraically closed trivially valued characteristic-zero field has EP (BJ Theorem 5.20). For a projective birational morphism π:Y→X and θ∈N¹(X), if θ is the limit of target classes θ_m such that θ_m−θ is ample and θ_m has EP, then π*:PSH(X,θ)→PSH(Y,π*θ) is a homeomorphism, in particular onto (BJ Lemma 5.13).",
    "For reduced irreducible projective X over an algebraically closed trivially valued field and ample ω, set V=(ωⁿ) and E_ω(φ)=⟨(ω,φ)ⁿ⁺¹⟩/((n+1)V). The genuine E¹ Monge–Ampère measure has raw mass V. A positive raw target ν of mass V has finite dual energy exactly when E_ω^∨(ν/V)=sup_{ψ∈E¹}(E_ω(ψ)−∫ψ d(ν/V)) is finite; this is equivalent to integrability of every genuine E¹ potential. Genuine solutions with the same measure differ by one real constant, and genuine domination holds without EP. The normalized genuine MA map onto all finite-dual-energy probability measures is surjective if and only if ω has EP. These are BJ 7.18–7.19, 9.20, 10.4, 10.6 and 12.8."
  ],
  "kind": "codex-report",
  "operationId": "e713d8d8-ccee-48b8-a347-4e0378a86db7",
  "reportedAt": "2026-10-05T08:35:32.111Z"
}



END MATHEMATICAL DATA



BEGIN MATHEMATICAL DATA: Original context 5: TASK-GRANTED actual86 precise PARTIAL review only

{
  "verdict": "PASS",
  "report": "PASS for the precise retained conditional partial scope. The operator construction, target-EP-to-equation implication, local reference conversion, conditional cardinality reduction, and after-EP normalization transport are correct. This does not establish singular EP or close P16.1. E remains the explicit antecedent of the cardinality implication; all-point fiber constancy and countable global C1 remain separate missing gates. Neither pending author result nor documentary observations were used as mathematical background.\n\nThe retained domain is an algebraically closed trivially valued field of characteristic zero, a reduced irreducible projective variety, and an actual ample rational line bundle L. The relevant BJ constructions allow singular varieties. The multilinear extension in BJ7.14 supplies the test-containing pairing used in BJ7.18; positivity, PL density, and the constant test produce the genuine Radon operator. Its model coefficients retain every b_E, and its raw mass is V=(L^n). Thus MA_raw=V MA_BJ, E_raw=V E_BJ, and E_raw-dual(μ)=V E_BJ-dual(μ/V). BJ9.20 applies because X is irreducible: finite dual energy is equivalent to integrability of every actual E1 potential. No support restriction is introduced. These are statements about the published operator, not an assigned inverse measure. [BJ](https://arxiv.org/pdf/1801.08229v4)\n\nUnder target EP, BJ5.11 gives compactness of the normalized target PSH space in the divisorial topology. The maximizing sequence has bounded J by BJ9.15–9.16. Its convergent subnet has an actual normalized PSH limit, and lower semicontinuity of J puts that limit in E1. BJ9.19 gives target-measure L1 convergence; energy upper semicontinuity then proves attainment of the variational supremum. Applying the PL variation estimate with both f and −f identifies the maximizing potential’s probability MA with μ/V, hence its raw MA with μ. This establishes an actual solution, rather than only convergence of measures. Irreducibility gives uniqueness modulo constants through BJ10.4. Genuine finite-energy locality and comparison are available before EP.\n\nThe supplied sign corrections are mathematically harmless and correct. The absolute-value identity is |a−b|=2(max(a,b)−b)−(a−b). The weighted integral is the test-containing pairing minus the zero-test pairing, at both finite stages and the limit. For continuous directions, the error is |t|ε on each side before division by t; the derivative follows by taking the PL derivative first and then sending ε to zero. For locality’s limiting step, the appropriate weighted convergence result is BJ7.21(ii); the source’s reference to BJ7.19(iii) there is a harmless cross-reference slip.\n\nContinuous base change has the required fixed reference. BJ3.9 literally places Hdom(L) inside H(L) for the same actual ample rational bundle, and BJ4.16 supplies uniform approximation without EP. Consequently BE7.14 applies to the corresponding fixed-bundle metrics. The smooth regularized FS formulas pull back with their real weights unchanged. BE8.3(iv) preserves the fundamental cycle and the raw measure at each smooth stage; BE8.4 and continuity of pushforward on compact analytic spaces pass the identity to continuous metrics. BE8.18, including its dimension-zero induction and relatively regular section argument, and BJ7.23 identify this operator with the energy-pairing operator. No probability factor, component multiplicity, or reference change is lost. [BE](https://arxiv.org/pdf/1805.01016v3)\n\nThe local conversion also preserves the actual reference. For two valid pairs, choose a smaller positive rational δ and an index beyond both original indices and the ample-cone tail for that δ. This proves directedness. Adding zero in the ample difference class preserves the scalar potential. In section frames, h_A≥0 because the constant branch 1 occurs, so the raw weights decrease as the index increases and δ decreases. Their limit is φ+h_M, including at −∞.\n\nThe required compact neighborhoods can be obtained directly: choose affine algebra generators g_a and radii R_a in exp(Q) strictly exceeding their values at the tested point. The simultaneous inequalities |g_a|≤R_a define a compact seminorm space, by closedness inside a product of bounded intervals; the strict inequalities give an ordinary open neighborhood of the point. This does not assert strict affinoidness over the trivial field. The reference weights are finite and bounded there. Clearing rational tensor powers makes the section ratios regular functions in the original frames. Every appended original generator branch and constant floor can be placed strictly below the old finite minimum on all of Q.\n\nFor the fixed-pair approximation, a safe verification of BJ3.10 interpolates ω+D toward ω+H by ω+(1−t)D+tH, followed by rational approximation. This avoids relying on the printed interpolation ω+D+tH. The summable shifts in the argument then give the asserted decreasing sequence. Flattening requires no minimum closure: strictly shifted finite continuous majorants are ordered by pointwise domination, and compactness supplies a common upper index. Two harmless clarifications make the application fully literal. One may use the whole real-weight affine FS family, which is stable under real constants; alternatively the same compact proof uses positive rational shifts throughout and retains rational weights. At a −∞ limit, use an arbitrary finite threshold R instead of an expression such as −∞+ε. These clarifications preserve the construction and its conclusion. The local result supplies neither all-point fiber constancy nor original singular global PSH membership.\n\nFor cardinality, the normalization and its finite algebra structure, gluing data, and inverse on a dense open descend together with X, L, and the finite obstacle. Faithful flatness preserves integrality downward and descends normality. A finite normal birational algebra inside the common fraction field equals the integral closure: every element integral over the smaller algebra is also integral over that normal algebra. Descent therefore retains the actual normalization and the original possibly nonnormal X. Universal-homeomorphism descent and the local normalization definition give geometric unibranchness of X0. Thus the conditional E applies with its exact field, variety, and actual-bundle hypotheses. [Normality descent](https://stacks.math.columbia.edu/tag/033G), [universal-homeomorphism descent](https://stacks.math.columbia.edu/tag/0CEX)\n\nRestriction is surjective for every analytic point. The radius-one Gauss norm on H(x)(T) is multiplicative and unchanged on H(x); with an infinite transcendence basis, every polynomial still uses finitely many variables. After completion, valuation extension to an algebraic closure can be chosen without changing this real-valued norm. Indeed, a dominating valuation ring restricts to the original valuation ring, and the finite-extension value-group bound embeds each algebraic extension group into the divisible hull of the original real value group. Completing again preserves the embeddings. The embedded k is trivially valued: a monic equation with nonzero constant term rules out both norms greater than one and norms less than one. Evaluation into this complete field gives the required norm-preserving lift.\n\nEach finite Hdom(L) competitor has an actual same-mL section representation. Only its finitely many coefficients need enter its own larger countable field k2. The finite-cover equalizer proves section base change, and faithful flatness descends the vanishing of the evaluation cokernel. Restriction surjectivity transfers the obstacle inequality. The pulled-back envelope is continuous, genuine, and bounded, hence E1 on k2 without EP there. Continuous raw pushforward transfers the nonnegative orthogonality integral. BJ10.6 then gives domination on this irreducible competitor variety without assuming EP or inverse-equation existence there. No common countable field is assigned to an arbitrary family.\n\nFor an arbitrary PSH competitor q≤f, the decreasing compact superlevel sets {h_j≥f+ε} have empty intersection, so an entire tail is empty. Rational shifts remain in Hdom(L). The finite-competitor argument yields q≤ψ+ε, and then q≤ψ. Feasibility gives the exact target envelope identity. PL density, the envelope Lipschitz bound, and genuine uniform closure extend this to continuous obstacles; BJ5.17 supplies EP. Rational ample classes approaching a real ample class from above give the final extension by BJ5.9 and varying-class closure. This proves E implies arbitrary-cardinality EP, while preserving E as an unproved antecedent.\n\nNormalization transport is used only after the target approaching classes have EP. Every (1+1/m)ω satisfies the strict-from-above hypothesis of BJ5.13. Its onto PSH pullback, together with exact normalization energy identities, gives onto E1 pullback, including unbounded potentials. The finite birational normalization has generic degree one, so ν_*[Xν]=[X] and the volume remains V. Its analytic homeomorphism transports integrals and dual energy, while BJ7.19 gives genuine raw pushforward for E1 potentials. In dimension zero, X is one point, V=1, the energy is the scalar potential, and the raw measure is the unit point mass. No positive-dimensional estimate is used in that case.",
  "passages": [
    {
      "id": "2ab3bb03-f082-4dd3-91d7-64154be7c597/0",
      "statement": "BJ2.18, 2.31, 3.9 and 3.10: For a reduced projective variety X over an algebraically closed trivially valued field and an actual ample rational line bundle L, Hdom(c1(L)) is contained in H(L) for that same bundle. Elements of H(L) have formulas m^(-1) max_i(log|s_i|+λ_i), with rational weights and sections of the actual mL without common zeros. For every ample numerical class ω, every element of PL_R(X)∩PSH(ω) is a uniform limit of elements of Hdom(ω).",
      "url": "https://arxiv.org/pdf/1801.08229v4",
      "quote": "Hdom (L) := Hdom (c1 (L)) ⊂ H(L)",
      "premise": 0
    },
    {
      "id": "2ab3bb03-f082-4dd3-91d7-64154be7c597/1",
      "statement": "BJ2.18, 2.31, 3.9 and 3.10: For a reduced projective variety X over an algebraically closed trivially valued field and an actual ample rational line bundle L, Hdom(c1(L)) is contained in H(L) for that same bundle. Elements of H(L) have formulas m^(-1) max_i(log|s_i|+λ_i), with rational weights and sections of the actual mL without common zeros. For every ample numerical class ω, every element of PL_R(X)∩PSH(ω) is a uniform limit of elements of Hdom(ω).",
      "url": "https://arxiv.org/pdf/1801.08229v4",
      "quote": "Proposition 3.10. If ω ∈ Amp(X), then every ϕ ∈ PLR ∩ PSH(ω) is a uniform limit of functions in Hdom (ω).",
      "premise": 0
    },
    {
      "id": "2ab3bb03-f082-4dd3-91d7-64154be7c597/2",
      "statement": "BJ4.15(ii): For a reduced projective variety X over an algebraically closed trivially valued field, a nef numerical class θ, and φ∈PSH(θ), there is a decreasing net φ_i∈H(L_i), where the actual rational bundles L_i are ample, c1(L_i)−θ is ample, and c1(L_i) tends to θ.",
      "url": "https://arxiv.org/pdf/1801.08229v4",
      "quote": "if θ ∈ Nef(X) then (i) holds with ϕi ∈ H(Li ) = HQ (Li ) and Li ample;",
      "premise": 1
    },
    {
      "id": "2ab3bb03-f082-4dd3-91d7-64154be7c597/3",
      "statement": "BJ4.3, 4.5 and 4.7: On a reduced projective variety over an algebraically closed trivially valued field, zero is θ-psh exactly when θ is nef; PL positivity agrees with the nef test-configuration definition; PSH(θ)+PSH(θ′)⊂PSH(θ+θ′) and PSH(tθ)=tPSH(θ) for t>0. PSH classes are stable under finite maxima, real constants and uniform limits. A generically finite decreasing limit of φ_i∈PSH(θ_i), with θ_i tending to θ, belongs to PSH(θ).",
      "url": "https://arxiv.org/pdf/1801.08229v4",
      "quote": "PSH(θ) contains all constant functions ⇐⇒ θ ∈ Nef(X)",
      "premise": 2
    },
    {
      "id": "2ab3bb03-f082-4dd3-91d7-64154be7c597/4",
      "statement": "BJ4.3, 4.5 and 4.7: On a reduced projective variety over an algebraically closed trivially valued field, zero is θ-psh exactly when θ is nef; PL positivity agrees with the nef test-configuration definition; PSH(θ)+PSH(θ′)⊂PSH(θ+θ′) and PSH(tθ)=tPSH(θ) for t>0. PSH classes are stable under finite maxima, real constants and uniform limits. A generically finite decreasing limit of φ_i∈PSH(θ_i), with θ_i tending to θ, belongs to PSH(θ).",
      "url": "https://arxiv.org/pdf/1801.08229v4",
      "quote": "PSH(θ) + PSH(θ0 ) ⊂ PSH(θ + θ0 ) and PSH(tθ) = tPSH(θ);",
      "premise": 2
    },
    {
      "id": "2ab3bb03-f082-4dd3-91d7-64154be7c597/5",
      "statement": "BJ4.15(iii) and 4.16: On a reduced projective variety over an algebraically closed trivially valued field, every φ∈PSH(ω), for ω ample, is a decreasing limit of a net in Hdom(ω). CPSH(ω) is exactly the uniform closure of Hdom(ω). Neither assertion assumes EP.",
      "url": "https://arxiv.org/pdf/1801.08229v4",
      "quote": "if ω := θ ∈ Amp(X), then ϕ can be written as the limit of a decreasing net in Hdom (ω)",
      "premise": 3
    },
    {
      "id": "2ab3bb03-f082-4dd3-91d7-64154be7c597/6",
      "statement": "BJ4.15(iii) and 4.16: On a reduced projective variety over an algebraically closed trivially valued field, every φ∈PSH(ω), for ω ample, is a decreasing limit of a net in Hdom(ω). CPSH(ω) is exactly the uniform closure of Hdom(ω). Neither assertion assumes EP.",
      "url": "https://arxiv.org/pdf/1801.08229v4",
      "quote": "CPSH(ω) = C0 (X) ∩ PSH(ω) is the closure of Hdom (ω)",
      "premise": 3
    },
    {
      "id": "2ab3bb03-f082-4dd3-91d7-64154be7c597/7",
      "statement": "The finite-valued, one-parameter specialization of BJ4.6: Let Q be compact and F a family of finite continuous real-valued functions on Q stable under addition of constants. If each member of a decreasing outer net is a decreasing limit of functions in F, then the outer net’s pointwise limit, allowed to take −∞, is a decreasing limit of a single net in F. Minimum closure of F is unnecessary.",
      "url": "https://arxiv.org/pdf/1801.08229v4",
      "quote": "By construction, (gα )α∈A is a decreasing net",
      "premise": 4
    },
    {
      "id": "2ab3bb03-f082-4dd3-91d7-64154be7c597/8",
      "statement": "BJ2.2, 4.22 and 4.28: For a reduced projective variety over an algebraically closed trivially valued field, rational PL functions are uniformly dense in C0(X^an). If φ is θ-psh and ψ is upper semicontinuous, φ≤ψ on divisorial points implies φ≤ψ everywhere. For fixed continuous ψ, φ↦sup(φ−ψ) is continuous on PSH(θ) in the topology of divisorial pointwise convergence.",
      "url": "https://arxiv.org/pdf/1801.08229v4",
      "quote": "By density of PL(X) in C0 (X)",
      "premise": 5
    },
    {
      "id": "2ab3bb03-f082-4dd3-91d7-64154be7c597/9",
      "statement": "BJ2.2, 4.22 and 4.28: For a reduced projective variety over an algebraically closed trivially valued field, rational PL functions are uniformly dense in C0(X^an). If φ is θ-psh and ψ is upper semicontinuous, φ≤ψ on divisorial points implies φ≤ψ everywhere. For fixed continuous ψ, φ↦sup(φ−ψ) is continuous on PSH(θ) in the topology of divisorial pointwise convergence.",
      "url": "https://arxiv.org/pdf/1801.08229v4",
      "quote": "ϕ 7→ sup(ϕ − ψi ) is continuous on PSH(ωi )",
      "premise": 5
    },
    {
      "id": "2ab3bb03-f082-4dd3-91d7-64154be7c597/10",
      "statement": "BJ7.1, 7.2, 7.7 and 7.8: On a reduced projective variety X of dimension n over an algebraically closed trivially valued field, the algebraic energy pairing for ample classes has a unique increasing upper semicontinuous extension to PSH tuples, given by the infimum over Hdom majorants and continuous along decreasing nets. For ω ample and V=(ω^n), Eω(φ)=(ω,φ)^(n+1)/((n+1)V) is increasing, concave, upper semicontinuous, translation-equivariant and decreasing-net continuous. E1(ω)={φ∈PSH(ω):Eω(φ)>−∞} contains bounded potentials and is upward closed within PSH(ω). Pullback to the normalization preserves the pairing and energy, and detects finite energy.",
      "url": "https://arxiv.org/pdf/1801.08229v4",
      "quote": "admits a unique extension",
      "premise": 6
    },
    {
      "id": "2ab3bb03-f082-4dd3-91d7-64154be7c597/11",
      "statement": "BJ7.1, 7.2, 7.7 and 7.8: On a reduced projective variety X of dimension n over an algebraically closed trivially valued field, the algebraic energy pairing for ample classes has a unique increasing upper semicontinuous extension to PSH tuples, given by the infimum over Hdom majorants and continuous along decreasing nets. For ω ample and V=(ω^n), Eω(φ)=(ω,φ)^(n+1)/((n+1)V) is increasing, concave, upper semicontinuous, translation-equivariant and decreasing-net continuous. E1(ω)={φ∈PSH(ω):Eω(φ)>−∞} contains bounded potentials and is upward closed within PSH(ω). Pullback to the normalization preserves the pairing and energy, and detects finite energy.",
      "url": "https://arxiv.org/pdf/1801.08229v4",
      "quote": "Eω (ϕ) = Eν ? ω (ν ? ϕ)",
      "premise": 6
    },
    {
      "id": "2ab3bb03-f082-4dd3-91d7-64154be7c597/12",
      "statement": "BJ7.14, 7.18, 7.19 and 7.21: For a reduced projective variety X over an algebraically closed trivially valued field, the finite-energy pairing extends multilinearly to differences of finite-energy potentials. It defines unique mixed signed Radon measures through the PL test pairing; nef psh inputs give positive measures. Their mass is the mixed intersection number, their model coefficients include ord_E(X0), and they commute with normalization pushforward and decreasing E1 nets. Every E1 test potential is integrable against mixed E1 measures. If φ0∈PSH(ω0) is integrable against the limiting mixed measure and all potentials decrease to the specified limits, then the corresponding weighted measures converge weakly.",
      "url": "https://arxiv.org/pdf/1801.08229v4",
      "quote": "cE := ordE (X0 )(θ1,X + D1 )|E · . . . · (θn,X + Dn )|E",
      "premise": 7
    },
    {
      "id": "2ab3bb03-f082-4dd3-91d7-64154be7c597/13",
      "statement": "BJ7.14, 7.18, 7.19 and 7.21: For a reduced projective variety X over an algebraically closed trivially valued field, the finite-energy pairing extends multilinearly to differences of finite-energy potentials. It defines unique mixed signed Radon measures through the PL test pairing; nef psh inputs give positive measures. Their mass is the mixed intersection number, their model coefficients include ord_E(X0), and they commute with normalization pushforward and decreasing E1 nets. Every E1 test potential is integrable against mixed E1 measures. If φ0∈PSH(ω0) is integrable against the limiting mixed measure and all potentials decrease to the specified limits, then the corresponding weighted measures converge weakly.",
      "url": "https://arxiv.org/pdf/1801.08229v4",
      "quote": "ϕ0j µj → ϕ0 µ weakly in C0 (X)∨ .",
      "premise": 7
    },
    {
      "id": "2ab3bb03-f082-4dd3-91d7-64154be7c597/14",
      "statement": "BJ7.27, 7.40, 7.44 and 7.45: On a reduced projective variety over an algebraically closed trivially valued field, for ω ample and E1(ω) potentials, I is nonnegative, J and I are comparable, and I satisfies a quasi-triangle inequality. Finite-energy MA is local under maxima on the set where one potential is strictly larger; consequently ∫_{φ<ψ}MA(φ)≥∫_{φ<ψ}MA(ψ), and I(φ,ψ)=I(φ,max(φ,ψ))+I(max(φ,ψ),ψ). These assertions do not require EP.",
      "url": "https://arxiv.org/pdf/1801.08229v4",
      "quote": "1{ϕ>ϕ0 } MA(max{ϕ, ϕ0 }) = 1{ϕ>ϕ0 } MA(ϕ)",
      "premise": 8
    },
    {
      "id": "2ab3bb03-f082-4dd3-91d7-64154be7c597/15",
      "statement": "BJ9.20: For a reduced irreducible projective variety over an algebraically closed trivially valued field and an ample class ω, a Radon probability measure μ has finite dual energy sup_{φ∈E1(ω)}(Eω(φ)−∫φ dμ) if and only if every φ∈E1(ω) is μ-integrable.",
      "url": "https://arxiv.org/pdf/1801.08229v4",
      "quote": "E1 ⊂ L1(µ).",
      "premise": 9
    },
    {
      "id": "2ab3bb03-f082-4dd3-91d7-64154be7c597/16",
      "statement": "BJ5.11: For an irreducible projective variety over an algebraically closed trivially valued field and θ∈N1(X), EP for θ is equivalent to compactness of {φ∈PSH(θ):supφ=0} in the divisorial pointwise topology, and to convergence in PSH(θ) of every bounded-above increasing net.",
      "url": "https://arxiv.org/pdf/1801.08229v4",
      "quote": "the space PSHsup(θ) := {ϕ ∈ PSH(θ) | sup ϕ = 0} is compact;",
      "premise": 10
    },
    {
      "id": "2ab3bb03-f082-4dd3-91d7-64154be7c597/17",
      "statement": "BJ9.15–9.19: For a projective variety over an algebraically closed trivially valued field, an ample class ω, and a finite-dual-energy probability measure μ, J(φ) is bounded by a dimensional constant times Jμ(φ)+E∨(μ), so maximizing nets have eventually bounded J. Any convergent net φ_i→φ in PSH(ω) with eventually bounded J converges to φ in L1(μ).",
      "url": "https://arxiv.org/pdf/1801.08229v4",
      "quote": "J(ϕ) . Jµ (ϕ) + E∨ (µ).",
      "premise": 11
    },
    {
      "id": "2ab3bb03-f082-4dd3-91d7-64154be7c597/18",
      "statement": "BJ9.15–9.19: For a projective variety over an algebraically closed trivially valued field, an ample class ω, and a finite-dual-energy probability measure μ, J(φ) is bounded by a dimensional constant times Jμ(φ)+E∨(μ), so maximizing nets have eventually bounded J. Any convergent net φ_i→φ in PSH(ω) with eventually bounded J converges to φ in L1(μ).",
      "url": "https://arxiv.org/pdf/1801.08229v4",
      "quote": "For any µ ∈ M1 we then have ϕi → ϕ in L1 (µ).",
      "premise": 11
    },
    {
      "id": "2ab3bb03-f082-4dd3-91d7-64154be7c597/19",
      "statement": "BJ8.3, 8.5 and 9.11: For a projective variety over an algebraically closed trivially valued field and an ample class ω, the outer energy E↓ is increasing and satisfies E↓(u+c)=E↓(u)+c. For φ∈E1(ω) and fixed f∈PL_R(X), E↓(φ+tf)=Eω(φ)+t∫f MAω(φ)+O(t²), with a constant uniform in φ. Under EP, this outer energy equals Eω(Pω(φ+tf)). For every finite-dual-energy probability measure μ, the MA measures of every maximizing E1 net converge weakly to μ.",
      "url": "https://arxiv.org/pdf/1801.08229v4",
      "quote": "the implicit constant in the O is uniform with respect to ϕ.",
      "premise": 12
    },
    {
      "id": "2ab3bb03-f082-4dd3-91d7-64154be7c597/20",
      "statement": "BJ8.3, 8.5 and 9.11: For a projective variety over an algebraically closed trivially valued field and an ample class ω, the outer energy E↓ is increasing and satisfies E↓(u+c)=E↓(u)+c. For φ∈E1(ω) and fixed f∈PL_R(X), E↓(φ+tf)=Eω(φ)+t∫f MAω(φ)+O(t²), with a constant uniform in φ. Under EP, this outer energy equals Eω(Pω(φ+tf)). For every finite-dual-energy probability measure μ, the MA measures of every maximizing E1 net converge weakly to μ.",
      "url": "https://arxiv.org/pdf/1801.08229v4",
      "quote": "For any maximizing net (ϕi ) for µ we have MA(ϕi ) → µ weakly in M.",
      "premise": 12
    },
    {
      "id": "2ab3bb03-f082-4dd3-91d7-64154be7c597/21",
      "statement": "BJ10.4 and 10.6: For an equidimensional reduced projective variety over an algebraically closed trivially valued field and an ample class ω, equality of the MA measures of two E1(ω) potentials is equivalent to I=0 and to their difference being locally constant. If u∈PSH(ω), v∈E1(ω), and u≤v almost everywhere for MAω(v), then u≤v everywhere. Neither assertion requires EP.",
      "url": "https://arxiv.org/pdf/1801.08229v4",
      "quote": "assume ϕ ≤ ψ a.e. with respect to MA(ψ). Then ϕ ≤ ψ on X an .",
      "premise": 13
    },
    {
      "id": "2ab3bb03-f082-4dd3-91d7-64154be7c597/22",
      "statement": "BE7.12–7.14: On a projective scheme over a complete non-Archimedean field, including a trivially valued field, every psh metric defined by decreasing fixed-bundle FS approximation on a semiample rational line bundle is a decreasing limit of smooth semipositive metrics on that same bundle. For a continuous metric the approximation is uniform. Smooth regularized FS metrics permit arbitrary real finite weights.",
      "url": "https://arxiv.org/pdf/1805.01016v3",
      "quote": "Every psh metric φ on a semiample Q-line bundle L is psh-regularizable.",
      "premise": 14
    },
    {
      "id": "2ab3bb03-f082-4dd3-91d7-64154be7c597/23",
      "statement": "BE8.3(iv) and 8.4–8.5: On a projective scheme over a complete non-Archimedean field, smooth mixed Monge–Ampère measures, including the analytic fundamental cycle, commute with pushforward under every complete field extension. On fixed rational line bundles the operator has a unique extension to continuous psh-regularizable metrics, continuous for uniform convergence of metrics and weak convergence of measures; semipositive inputs give positive measures with mass equal to the mixed intersection number.",
      "url": "https://arxiv.org/pdf/1805.01016v3",
      "quote": "for any complete field extension F/K",
      "premise": 15
    },
    {
      "id": "2ab3bb03-f082-4dd3-91d7-64154be7c597/24",
      "statement": "BE8.3(iv) and 8.4–8.5: On a projective scheme over a complete non-Archimedean field, smooth mixed Monge–Ampère measures, including the analytic fundamental cycle, commute with pushforward under every complete field extension. On fixed rational line bundles the operator has a unique extension to continuous psh-regularizable metrics, continuous for uniform convergence of metrics and weak convergence of measures; semipositive inputs give positive measures with mass equal to the mixed intersection number.",
      "url": "https://arxiv.org/pdf/1805.01016v3",
      "quote": "admits a unique continuous extension to tuples of continuous, psh-regularizable metrics on the Li",
      "premise": 15
    },
    {
      "id": "2ab3bb03-f082-4dd3-91d7-64154be7c597/25",
      "statement": "BE8.18 and BJ7.23: The analytic Deligne pairing of model metrics on actual generic-fiber line bundles equals the metric induced by their model Deligne pairing. For continuous ample-class psh potentials on a reduced projective variety over an algebraically closed trivially valued field, the resulting continuous CLD/BE Monge–Ampère operator agrees with the BJ energy-pairing operator, without assuming EP.",
      "url": "https://arxiv.org/pdf/1805.01016v3",
      "quote": "hφ0 , . . . , φn i = φhL0 ,...,Ln i .",
      "premise": 16
    },
    {
      "id": "2ab3bb03-f082-4dd3-91d7-64154be7c597/26",
      "statement": "BE8.18 and BJ7.23: The analytic Deligne pairing of model metrics on actual generic-fiber line bundles equals the metric induced by their model Deligne pairing. For continuous ample-class psh potentials on a reduced projective variety over an algebraically closed trivially valued field, the resulting continuous CLD/BE Monge–Ampère operator agrees with the BJ energy-pairing operator, without assuming EP.",
      "url": "https://arxiv.org/pdf/1801.08229v4",
      "quote": "the present approach is compatible with [CLD12] for continuous ω-psh functions.",
      "premise": 16
    },
    {
      "id": "2ab3bb03-f082-4dd3-91d7-64154be7c597/27",
      "statement": "BJ13.1, continuous-obstacle case: For a reduced irreducible projective variety over an algebraically closed trivially valued field, an ample class ω with EP, and f∈C0(X^an), ψ=Pω(f) is continuous and ω-psh, and ∫(f−ψ)MAω(ψ)=0. In particular f=ψ almost everywhere for MAω(ψ).",
      "url": "https://arxiv.org/pdf/1801.08229v4",
      "quote": "P(ϕ)? = P(ϕ) = ϕ a.e. for MA(P(ϕ)? ).",
      "premise": 17
    },
    {
      "id": "2ab3bb03-f082-4dd3-91d7-64154be7c597/28",
      "statement": "BJ5.17 and 5.9: For an irreducible projective variety over an algebraically closed trivially valued field and an ample class ω, EP is equivalent to continuity of Pω(f) for every continuous obstacle f; under EP these envelopes are genuine ω-psh potentials. If θ is a limit of classes θ_j≥θ having EP, then θ has EP.",
      "url": "https://arxiv.org/pdf/1801.08229v4",
      "quote": "for any ϕ ∈ C0 (X), Pω (ϕ) is continuous.",
      "premise": 18
    },
    {
      "id": "2ab3bb03-f082-4dd3-91d7-64154be7c597/29",
      "statement": "BJ5.13: Let π:Y→X be a birational morphism of projective varieties over an algebraically closed trivially valued field. If θ∈N1(X) is the limit of a sequence θ_m such that θ_m−θ is ample and every θ_m has EP on X, then pullback PSH(X,θ)→PSH(Y,π*θ) is an onto homeomorphism in the divisorial pointwise topologies.",
      "url": "https://arxiv.org/pdf/1801.08229v4",
      "quote": "θm > θ with the envelope property.",
      "premise": 19
    },
    {
      "id": "2ab3bb03-f082-4dd3-91d7-64154be7c597/30",
      "statement": "BJ5.13: Let π:Y→X be a birational morphism of projective varieties over an algebraically closed trivially valued field. If θ∈N1(X) is the limit of a sequence θ_m such that θ_m−θ is ample and every θ_m has EP on X, then pullback PSH(X,θ)→PSH(Y,π*θ) is an onto homeomorphism in the divisorial pointwise topologies.",
      "url": "https://arxiv.org/pdf/1801.08229v4",
      "quote": "is a homeomorphism.",
      "premise": 19
    },
    {
      "id": "2ab3bb03-f082-4dd3-91d7-64154be7c597/31",
      "statement": "Stacks033G: If R→S is a faithfully flat ring map and S is normal, then R is normal.",
      "url": "https://stacks.math.columbia.edu/tag/033G",
      "quote": "Then $R$ is a normal ring.",
      "premise": 20
    },
    {
      "id": "2ab3bb03-f082-4dd3-91d7-64154be7c597/32",
      "statement": "Stacks0CEX: The property that a morphism is a universal homeomorphism is fpqc local on its target.",
      "url": "https://stacks.math.columbia.edu/tag/0CEX",
      "quote": "“$f$ is a universal homeomorphism” is fpqc local on the base.",
      "premise": 21
    },
    {
      "id": "2ab3bb03-f082-4dd3-91d7-64154be7c597/33",
      "statement": "Stacks0BPZ: A local ring A is geometrically unibranch exactly when A_red is a domain, its integral closure A′ in its fraction field is local, and the residue field of A′ is purely inseparable over that of A.",
      "url": "https://stacks.math.columbia.edu/tag/0BPZ",
      "quote": "the residue field of $A'$ is purely inseparable over the residue field of $A$.",
      "premise": 22
    },
    {
      "id": "2ab3bb03-f082-4dd3-91d7-64154be7c597/34",
      "statement": "Stacks035A and 035S: A scheme locally of finite type over a Nagata scheme is Nagata. The normalization of a Nagata scheme is finite. In particular these assertions apply to varieties over fields, since fields are Nagata.",
      "url": "https://stacks.math.columbia.edu/tag/035A",
      "quote": "If $S$ is Nagata and $f$ locally of finite type then $X$ is Nagata.",
      "premise": 23
    },
    {
      "id": "2ab3bb03-f082-4dd3-91d7-64154be7c597/35",
      "statement": "Stacks035A and 035S: A scheme locally of finite type over a Nagata scheme is Nagata. The normalization of a Nagata scheme is finite. In particular these assertions apply to varieties over fields, since fields are Nagata.",
      "url": "https://stacks.math.columbia.edu/tag/035S",
      "quote": "Let $X$ be a Nagata scheme. The normalization $\\nu : X^\\nu \\to X$ is a finite morphism.",
      "premise": 23
    },
    {
      "id": "2ab3bb03-f082-4dd3-91d7-64154be7c597/36",
      "statement": "Stacks30.17.2: If R is Noetherian, X and Y are proper over R, f:Y→X is finite and surjective, and L is an invertible sheaf on X, then L is ample if and only if f*L is ample.",
      "url": "https://stacks.math.columbia.edu/tag/01XO",
      "quote": "Then $\\mathcal{L}$ is ample if and only if $f^*\\mathcal{L}$ is ample.",
      "premise": 24
    },
    {
      "id": "2ab3bb03-f082-4dd3-91d7-64154be7c597/37",
      "statement": "Stacks10.50.2: For a field K and a local subring A⊂K, there exists a valuation ring with fraction field K dominating A.",
      "url": "https://stacks.math.columbia.edu/tag/00I8",
      "quote": "Then there exists a valuation ring with fraction field $K$ dominating $A$.",
      "premise": 25
    },
    {
      "id": "2ab3bb03-f082-4dd3-91d7-64154be7c597/38",
      "statement": "Stacks15.125.2: If A⊂B is an injective local extension of valuation rings with fraction fields K⊂L and L/K finite, then both the residue extension and the value-group index are finite, and [Γ_B:Γ_A][κ_B:κ_A]≤[L:K].",
      "url": "https://stacks.math.columbia.edu/tag/0ASF",
      "quote": "[\\Gamma _ B : \\Gamma _ A] [\\kappa _ B : \\kappa _ A] \\leq [L : K].",
      "premise": 26
    }
  ],
  "premises": [
    "BJ2.18, 2.31, 3.9 and 3.10: For a reduced projective variety X over an algebraically closed trivially valued field and an actual ample rational line bundle L, Hdom(c1(L)) is contained in H(L) for that same bundle. Elements of H(L) have formulas m^(-1) max_i(log|s_i|+λ_i), with rational weights and sections of the actual mL without common zeros. For every ample numerical class ω, every element of PL_R(X)∩PSH(ω) is a uniform limit of elements of Hdom(ω).",
    "BJ4.15(ii): For a reduced projective variety X over an algebraically closed trivially valued field, a nef numerical class θ, and φ∈PSH(θ), there is a decreasing net φ_i∈H(L_i), where the actual rational bundles L_i are ample, c1(L_i)−θ is ample, and c1(L_i) tends to θ.",
    "BJ4.3, 4.5 and 4.7: On a reduced projective variety over an algebraically closed trivially valued field, zero is θ-psh exactly when θ is nef; PL positivity agrees with the nef test-configuration definition; PSH(θ)+PSH(θ′)⊂PSH(θ+θ′) and PSH(tθ)=tPSH(θ) for t>0. PSH classes are stable under finite maxima, real constants and uniform limits. A generically finite decreasing limit of φ_i∈PSH(θ_i), with θ_i tending to θ, belongs to PSH(θ).",
    "BJ4.15(iii) and 4.16: On a reduced projective variety over an algebraically closed trivially valued field, every φ∈PSH(ω), for ω ample, is a decreasing limit of a net in Hdom(ω). CPSH(ω) is exactly the uniform closure of Hdom(ω). Neither assertion assumes EP.",
    "The finite-valued, one-parameter specialization of BJ4.6: Let Q be compact and F a family of finite continuous real-valued functions on Q stable under addition of constants. If each member of a decreasing outer net is a decreasing limit of functions in F, then the outer net’s pointwise limit, allowed to take −∞, is a decreasing limit of a single net in F. Minimum closure of F is unnecessary.",
    "BJ2.2, 4.22 and 4.28: For a reduced projective variety over an algebraically closed trivially valued field, rational PL functions are uniformly dense in C0(X^an). If φ is θ-psh and ψ is upper semicontinuous, φ≤ψ on divisorial points implies φ≤ψ everywhere. For fixed continuous ψ, φ↦sup(φ−ψ) is continuous on PSH(θ) in the topology of divisorial pointwise convergence.",
    "BJ7.1, 7.2, 7.7 and 7.8: On a reduced projective variety X of dimension n over an algebraically closed trivially valued field, the algebraic energy pairing for ample classes has a unique increasing upper semicontinuous extension to PSH tuples, given by the infimum over Hdom majorants and continuous along decreasing nets. For ω ample and V=(ω^n), Eω(φ)=(ω,φ)^(n+1)/((n+1)V) is increasing, concave, upper semicontinuous, translation-equivariant and decreasing-net continuous. E1(ω)={φ∈PSH(ω):Eω(φ)>−∞} contains bounded potentials and is upward closed within PSH(ω). Pullback to the normalization preserves the pairing and energy, and detects finite energy.",
    "BJ7.14, 7.18, 7.19 and 7.21: For a reduced projective variety X over an algebraically closed trivially valued field, the finite-energy pairing extends multilinearly to differences of finite-energy potentials. It defines unique mixed signed Radon measures through the PL test pairing; nef psh inputs give positive measures. Their mass is the mixed intersection number, their model coefficients include ord_E(X0), and they commute with normalization pushforward and decreasing E1 nets. Every E1 test potential is integrable against mixed E1 measures. If φ0∈PSH(ω0) is integrable against the limiting mixed measure and all potentials decrease to the specified limits, then the corresponding weighted measures converge weakly.",
    "BJ7.27, 7.40, 7.44 and 7.45: On a reduced projective variety over an algebraically closed trivially valued field, for ω ample and E1(ω) potentials, I is nonnegative, J and I are comparable, and I satisfies a quasi-triangle inequality. Finite-energy MA is local under maxima on the set where one potential is strictly larger; consequently ∫_{φ<ψ}MA(φ)≥∫_{φ<ψ}MA(ψ), and I(φ,ψ)=I(φ,max(φ,ψ))+I(max(φ,ψ),ψ). These assertions do not require EP.",
    "BJ9.20: For a reduced irreducible projective variety over an algebraically closed trivially valued field and an ample class ω, a Radon probability measure μ has finite dual energy sup_{φ∈E1(ω)}(Eω(φ)−∫φ dμ) if and only if every φ∈E1(ω) is μ-integrable.",
    "BJ5.11: For an irreducible projective variety over an algebraically closed trivially valued field and θ∈N1(X), EP for θ is equivalent to compactness of {φ∈PSH(θ):supφ=0} in the divisorial pointwise topology, and to convergence in PSH(θ) of every bounded-above increasing net.",
    "BJ9.15–9.19: For a projective variety over an algebraically closed trivially valued field, an ample class ω, and a finite-dual-energy probability measure μ, J(φ) is bounded by a dimensional constant times Jμ(φ)+E∨(μ), so maximizing nets have eventually bounded J. Any convergent net φ_i→φ in PSH(ω) with eventually bounded J converges to φ in L1(μ).",
    "BJ8.3, 8.5 and 9.11: For a projective variety over an algebraically closed trivially valued field and an ample class ω, the outer energy E↓ is increasing and satisfies E↓(u+c)=E↓(u)+c. For φ∈E1(ω) and fixed f∈PL_R(X), E↓(φ+tf)=Eω(φ)+t∫f MAω(φ)+O(t²), with a constant uniform in φ. Under EP, this outer energy equals Eω(Pω(φ+tf)). For every finite-dual-energy probability measure μ, the MA measures of every maximizing E1 net converge weakly to μ.",
    "BJ10.4 and 10.6: For an equidimensional reduced projective variety over an algebraically closed trivially valued field and an ample class ω, equality of the MA measures of two E1(ω) potentials is equivalent to I=0 and to their difference being locally constant. If u∈PSH(ω), v∈E1(ω), and u≤v almost everywhere for MAω(v), then u≤v everywhere. Neither assertion requires EP.",
    "BE7.12–7.14: On a projective scheme over a complete non-Archimedean field, including a trivially valued field, every psh metric defined by decreasing fixed-bundle FS approximation on a semiample rational line bundle is a decreasing limit of smooth semipositive metrics on that same bundle. For a continuous metric the approximation is uniform. Smooth regularized FS metrics permit arbitrary real finite weights.",
    "BE8.3(iv) and 8.4–8.5: On a projective scheme over a complete non-Archimedean field, smooth mixed Monge–Ampère measures, including the analytic fundamental cycle, commute with pushforward under every complete field extension. On fixed rational line bundles the operator has a unique extension to continuous psh-regularizable metrics, continuous for uniform convergence of metrics and weak convergence of measures; semipositive inputs give positive measures with mass equal to the mixed intersection number.",
    "BE8.18 and BJ7.23: The analytic Deligne pairing of model metrics on actual generic-fiber line bundles equals the metric induced by their model Deligne pairing. For continuous ample-class psh potentials on a reduced projective variety over an algebraically closed trivially valued field, the resulting continuous CLD/BE Monge–Ampère operator agrees with the BJ energy-pairing operator, without assuming EP.",
    "BJ13.1, continuous-obstacle case: For a reduced irreducible projective variety over an algebraically closed trivially valued field, an ample class ω with EP, and f∈C0(X^an), ψ=Pω(f) is continuous and ω-psh, and ∫(f−ψ)MAω(ψ)=0. In particular f=ψ almost everywhere for MAω(ψ).",
    "BJ5.17 and 5.9: For an irreducible projective variety over an algebraically closed trivially valued field and an ample class ω, EP is equivalent to continuity of Pω(f) for every continuous obstacle f; under EP these envelopes are genuine ω-psh potentials. If θ is a limit of classes θ_j≥θ having EP, then θ has EP.",
    "BJ5.13: Let π:Y→X be a birational morphism of projective varieties over an algebraically closed trivially valued field. If θ∈N1(X) is the limit of a sequence θ_m such that θ_m−θ is ample and every θ_m has EP on X, then pullback PSH(X,θ)→PSH(Y,π*θ) is an onto homeomorphism in the divisorial pointwise topologies.",
    "Stacks033G: If R→S is a faithfully flat ring map and S is normal, then R is normal.",
    "Stacks0CEX: The property that a morphism is a universal homeomorphism is fpqc local on its target.",
    "Stacks0BPZ: A local ring A is geometrically unibranch exactly when A_red is a domain, its integral closure A′ in its fraction field is local, and the residue field of A′ is purely inseparable over that of A.",
    "Stacks035A and 035S: A scheme locally of finite type over a Nagata scheme is Nagata. The normalization of a Nagata scheme is finite. In particular these assertions apply to varieties over fields, since fields are Nagata.",
    "Stacks30.17.2: If R is Noetherian, X and Y are proper over R, f:Y→X is finite and surjective, and L is an invertible sheaf on X, then L is ample if and only if f*L is ample.",
    "Stacks10.50.2: For a field K and a local subring A⊂K, there exists a valuation ring with fraction field K dominating A.",
    "Stacks15.125.2: If A⊂B is an injective local extension of valuation rings with fraction fields K⊂L and L/K finite, then both the residue extension and the value-group index are finite, and [Γ_B:Γ_A][κ_B:κ_A]≤[L:K]."
  ],
  "kind": "codex-report",
  "operationId": "2ab3bb03-f082-4dd3-91d7-64154be7c597",
  "reportedAt": "2026-10-05T10:27:58.230Z"
}



END MATHEMATICAL DATA



BEGIN MATHEMATICAL DATA: Original context 6: Binding scope of actual86

# Binding scope of the actual round86 partial PASS

The actual canonical review is P16.1-round86-actual-partial-mathematical-review-20261005.json, SHA256 7b995e992b639a526491b52eb85255c613e3f1e980235490858be3c6fde6616c, operation 2ab3bb03-f082-4dd3-91d7-64154be7c597, reported 2026-10-05T10:27:58.230Z. It returns PASS for the precise conditional partial task, not original P16.1 completion. Its entire report, 27 external premises and 39 passages were read; all actual nonnegative premise indices and exact statement bindings were verified. These assertions concern the actual canonical output, not private reviewer artifacts or transcripts.

The grant covers the unchanged roots89/90 only within that review task: the genuine general-variety raw operator and normalization; target-EP-to-actual-equation implication; continuous same-actual-bundle raw base-change compatibility; local actual-reference conversion; the implication from the explicitly conditional countable EP premise E to arbitrary-cardinality EP; and normalization transport after target EP. E, all-point fiber constancy, and countable global C1 are not proved or granted by this PASS.

Binding clarifications in the actual review:

1. In BJ3.10, safely interpolate the nef model class as \(\omega+(1-t)D+tH\), then approximate rationally. Do not rely on the printed expression \(\omega+D+tH\) as that interpolation.
2. For local net flattening, one can use the real-weight affine FS family, stable under real constants; for the rational family needed by countable contacts, use positive rational shifts throughout the compact proof. At a \(-\infty\) limit use an arbitrary finite threshold, never the expression \(-\infty+\varepsilon\).
3. Finite-energy locality's weighted limiting step uses BJ7.21(ii). The source's BJ7.19(iii) reference at that step is a cross-reference slip.
4. Retain the already independently assessed sign corrections: \(|a-b|=2(\max(a,b)-b)-(a-b)\), and weighted energy tests are the test-containing pairing MINUS the zero-test pairing. Continuous-direction bounds use \(|t|\varepsilon\).

The original frozen mathematical drafts and review input are unchanged. This binding addendum states how future uses of the accepted deduction must be read. No whole-source-file or recursive-primary-proof reading claim is made.



END MATHEMATICAL DATA



BEGIN MATHEMATICAL DATA: Original context 7: Exact body accepted ONLY within actual86 scope; historical status statements are documentary

# Exact envelope-to-equation reduction and continuous base change

This is a new unreviewed primary-source reconstruction for original P16.1. It does not prove the missing singular envelope property. Native original continuations83 and84 keep their independently frozen inputs and receive no feedback from this draft. The original solved count remains four.

## 1. The existing general-variety theorem has the required operator

Fix an algebraically closed trivially valued field \(k\) of characteristic zero, a reduced irreducible projective \(k\)-variety \(X\), an actual ample rational line bundle \(L\), \(\omega=c_1(L)\), and \(V=(L^n)>0\). No smoothness hypothesis appears in the opening of BJ Section7, Section9, Section10 or Theorem12.8. Geometric unibranchness remains relevant to obtaining the envelope property, rather than being a replacement for it.

BJ Theorem7.1 extends the actual algebraic energy pairing by decreasing finite \(H^{dom}\) majorants. Its monotonicity and upper semicontinuity are proved in the original divisorial topology; upper semicontinuity uses the continuity of \(\sup(\varphi-\psi)\) for a fixed PL majorant. BJ Theorem7.18 then constructs the mixed measure by the positive linear functional
\[
 \int f\,(\omega_1+dd^c\varphi_1)\wedge\cdots\wedge
 (\omega_n+dd^c\varphi_n)
 =(0,f)\cdot(\omega_1,\varphi_1)\cdots(\omega_n,\varphi_n)
\]
for a PL test \(f\). Positivity and density extend this functional uniquely to \(C^0(X^{an})\). This is the genuine operator defined by the algebraic energy pairing. It is not a new measure assigned to an inverse-support construction.

BJ7.19 gives positivity, raw mixed mass \((\omega_1\cdots\omega_n)\), monotone continuity on actual \(E^1\), the model formula with every \(b_E=\operatorname{ord}_E(X_0)\), and normalization pushforward. For the top product write
\[
 \operatorname{MA}_{\rm raw,L}(\varphi)=(\omega+dd^c\varphi)^n,\qquad
 \operatorname{MA}_{\rm BJ,L}(\varphi)=V^{-1}\operatorname{MA}_{\rm raw,L}(\varphi).
\]
The first has mass \(V\), the second mass one. These are two normalizations of the SAME operator.

Let
\[
 E_{\rm BJ,L}(\varphi)=\frac{(\omega,\varphi)^{n+1}}{(n+1)V},
 \qquad E_{\rm raw,L}=V E_{\rm BJ,L}.
\]
The actual finite-energy space is \(\{\varphi\in\operatorname{PSH}(X,L):E_{\rm BJ,L}(\varphi)>-\infty\}\). For a positive Radon measure \(\mu\) of mass \(V\), put \(\bar\mu=\mu/V\). Its exact finite-dual-energy condition is
\[
 E_{\rm raw,L}^{\vee}(\mu)
 =\sup_{\varphi\in E^1(X,L)}
 \left(E_{\rm raw,L}(\varphi)-\int\varphi\,d\mu\right)
 =V E_{\rm BJ,L}^{\vee}(\bar\mu)<+\infty.
\]
By BJ9.20 this is equivalent to integrability of every actual \(E^1(X,L)\) potential against \(\mu\). Arbitrary support is retained.

## 2. Conditional attainment is an actual maximizer

Assume the envelope property for this original \(\omega\) on \(X\). BJ5.11 gives weak compactness of \(\operatorname{PSH}_{\sup}(X,L)\), in the actual topology of pointwise divisorial values. This assertion is obtained from target EP, not from compactness of a resolution by itself.

Choose a maximizing sequence for \(E_{\rm BJ,L}^{\vee}(\bar\mu)\), normalized by \(\sup\varphi_j=0\). Translation cancels in the functional. BJ9.15–9.16 bound \(J(\varphi_j)\) by the finite target dual energy and the vanishing deficit. Weak compactness supplies a subnet with actual weak limit \(\varphi\) in the normalized target psh class. Lower semicontinuity of \(J\) makes \(\varphi\in E^1(X,L)\).

BJ9.19 gives convergence in \(L^1(\bar\mu)\) for this energy-bounded weak subnet. Together with upper semicontinuity of energy,
\[
 E_{\rm BJ,L}(\varphi)-\int\varphi\,d\bar\mu
 \ge \limsup_j\left(E_{\rm BJ,L}(\varphi_j)
                 -\int\varphi_j\,d\bar\mu\right)
 =E_{\rm BJ,L}^{\vee}(\bar\mu).
\]
The reverse inequality is the definition of the supremum. Thus the limit is an ACTUAL maximizer; the proof does not stop at a weak measure limit or an \(I\)-Cauchy sequence.

BJ8.5 proves uniform outer energy differentiation for every fixed PL direction, and BJ9.11 applies it with both \(f\) and \(-f\) to any maximizing net. In particular a constant net at this actual maximizer has \(\operatorname{MA}_{\rm BJ,L}(\varphi)=\bar\mu\). Consequently
\[
 \operatorname{MA}_{\rm raw,L}(\varphi)=\mu.
\]
BJ10.4 gives uniqueness up to constants because \(X\) is irreducible, hence equidimensional and connected. BJ7.40–7.44 provide genuine finite-energy locality and comparison on this same original target. The general implication is exactly BJ12.8: target EP implies onto the actual finite-energy MA operator. Its converse also explains why merely producing approximants cannot bypass the envelope issue.

## 3. Correct signs in the pertinent source proofs

The actual cached PDF, not only extracted text, has a plus sign in the absolute-value line of BJ9.19 on printed/PDF page105. The required elementary identity is
\[
 |a-b|=2(\max(a,b)-b)-(a-b).
\]
With \(\varphi'_j=\max(\varphi_j,\varphi)\), both the integrals of \(\varphi_j-\varphi\) and \(\varphi'_j-\varphi\) tend to zero by the first part of that proof, so this CORRECT identity yields \(L^1\) convergence. The typo does not change the resulting proposition.

The actual PDF page84 in BJ7.21(ii) reverses the two energy-pairing terms. The test-containing pairing MINUS the zero-test pairing is the correct integral, as already stated in BJ7.15 and the proof of7.21(i). Reversing both finite-stage and limiting terms repairs that line; both pairings still converge, so the weighted convergence conclusion is the same.

The continuous-direction extension of BJ8.6 is most safely written directly. If \(\|f-f_m\|_\infty\le\epsilon_m\), then for EVERY real \(t\),
\[
 \varphi+t f_m-|t|\epsilon_m
 \le \varphi+t f
 \le \varphi+t f_m+|t|\epsilon_m.
\]
Monotonicity and translation of the actual outer energy give
\[
 |E^\downarrow(\varphi+t f)-E^\downarrow(\varphi+t f_m)|
 \le |t|\epsilon_m.
\]
Apply the PL derivative first and then \(\epsilon_m\downarrow0\). This gives the exact continuous-direction derivative, with the upper error \(+\epsilon_m\) and lower error \(-\epsilon_m\). It does not rely on the misplaced factors/signs in the printed intermediate inequalities.

These corrections are algebraic and preserve the theorem scopes. The two PDF pages were rendered from the cached primary PDF and visually inspected. No whole-PDF or recursively complete source-proof reading is asserted.

## 4. Continuous base-change pushforward with the actual reference

Let \(k_0\subset k_2\) be algebraically closed trivially valued characteristic-zero fields and \(r:X_{k_2}^{an}\to X_{k_0}^{an}\) the restriction map. Let \(\varphi_0\in\operatorname{CPSH}(X_{k_0},L_0)\), for an ACTUAL ample rational \(L_0\), and denote its actual pullback by \(\varphi_2=\varphi_0\circ r\). BJ4.16 makes \(\varphi_0\) a uniform limit of \(H^{dom}(L_0)\) functions. Crucially BJ Example3.9 (LF1700–1705) gives \(H^{dom}(L_0)\subset H(L_0)\), where these are FS functions on the SAME actual rational bundle \(L_0\). This uses Theorem2.31 on actual test-configuration bundles, not merely their numerical classes. Thus the required fixed-bundle/reference identification is available here WITHOUT EP. It is the ample rational case; no same-bundle assertion in a nonample nef class is being made.

BE7.14 makes every such continuous fixed-bundle psh metric a uniform limit of smooth semipositive metrics on the SAME line bundle. Each finite smooth regularized FS formula pulls back to the corresponding smooth semipositive formula over \(k_2\); its real finite weights remain real constants. BE8.3(iv) gives the actual pushforward identity for every finite smooth stage, including the analytic fundamental cycle. BE8.4, whose entire pertinent proof has now been read, gives uniform continuity of the genuine continuous operator into the weak topology of measures. Properness makes both analytic spaces compact, and restriction is continuous, so pushforward is weakly continuous. Passing to the genuine continuous operators therefore gives
\[
 r_*\operatorname{MA}_{\rm raw,L_2}(\varphi_2)
   =\operatorname{MA}_{\rm raw,L_0}(\varphi_0),\qquad
 \operatorname{MA}_{\rm raw,L_2}(\varphi_2)(X_{k_2}^{an})=V.
\]
BJ7.23 identifies this continuous operator with the genuine energy-pairing operator. BE8.18 identifies the model Deligne pairing on the actual generic bundle; its induction and entire pertinent proof, including8.19, were read. Neither cycle multiplicities nor residue factors are dropped in the comparison.

The longer model/nef/FS/Gauss route in reviewed round77 remains useful for converting locally supplied contact metrics. It is unnecessary for this already genuine continuous ample rational input: the literal inclusion in BJ3.9 and uniform approximation in BJ4.16 already supply the same actual bundle. In particular continuous C3 in continuation80 has no additional fixed-reference gate in this precise ample rational setting.

## 5. What the countable finite-data argument now needs

Assume target EP over every countable algebraically closed trivially valued characteristic-zero field in the stated original unibranch domain. Orthogonality for continuous obstacles is then a primary consequence of BJ13.1 under exactly that EP premise. Its short continuous case keeps \(P(\psi+t(f-\psi))=\psi\) for \(0\le t\le1\); the corrected continuous-direction derivative in section3 gives \(\int(f-\psi)\operatorname{MA}_{\rm raw}(\psi)=0\).

The required domination principle is BJ10.6 on an equidimensional projective target; its proof does not require inverse MA existence or new target EP. For \(u\in\operatorname{PSH}\), \(v\in E^1\), \(u\le v\) almost everywhere for \(\operatorname{MA}(v)\), replace \(u\) by \(\max(u,v)\). This lies in \(E^1\). The genuine
\[
 I(u,v)=\int(u-v)(\operatorname{MA}(v)-\operatorname{MA}(u))\ge0
\]
is also at most zero by the assumed almost-everywhere equality and \(u\ge v\). Thus \(I=0\), and BJ10.4 makes the difference constant. Equality almost everywhere against the positive mass-one measure fixes that constant to zero.

Accordingly the orthogonality and domination parts of continuation80 C4 need no additional singular inverse-equation theorem once countable EP is established. Continuous C3 is supplied by section4 on actual ample rational bundles. BJ3.9 also permits the finite \(H^{dom}(L)\) competitor to be descended through its literal fixed-\(L\) FS section formula: basepoint-freeness descends by faithful flatness, so one need not descend a separate varying bundle or nef model inequality for that competitor. The remaining cardinality argument needs finite-data descent of the original variety/normalization/universal homeomorphism, analytic restriction surjectivity, and the missing countable EP itself. Continuation81 gives source-aware geometric leads; native84 is reconstructing them independently. They are not granted by this draft.

## 6. Normalization is used after target EP

For the finite universal-homeomorphism normalization \(\nu:X^\nu\to X\), finite pullback preserves ampleness. Once target EP is proved for all positive rational multiples of \(L\), use the approaching classes \((1+1/m)\omega\) in BJ5.13. This gives onto pullback of genuine psh classes at \(\omega\). It is not used earlier to obtain EP.

BJ7.2 and7.7 give exact energy preservation on actual pullbacks; BJ7.8(vii) identifies finite energy; BJ7.19(iii) gives the raw mixed-measure pushforward. Projection for the finite birational fundamental cycle retains \(V=(L^n)=(\nu^*L)^n\). Together with the analytic homeomorphism, onto genuine psh/E1 pullback transports integrals and finite dual energy as well. This is an actual operator/energy comparison, rather than a statement about point-set topology alone.

In dimension zero, the reduced irreducible algebraically closed projective variety is one point. The empty product has raw mass \(V=1\), energy is its scalar potential, and the unique positive measure of that mass solves the equation; every two potentials differ by a constant. The curve/Dirichlet/positive-dimensional \(I\) arguments are not needed there.

The missing singular target EP is still indispensable. Sections1–6 provide a precise conditional equation conclusion on the whole arbitrary-support singular domain over the retained trivial fields. They do not assert the discrete, arbitrary complete-field, nonample or nonalgebraizable axes, and do not close original P16.1 without the missing envelope proof.

Primary reading for this record: BJ1801.08229v4 LF1400–1464,1596–1735,2894–2976,3650–3735,3780–3840,3963–4148,4200–4288,4498–4618,4835–5013,5100–5180,5190–5265,5390–5485,6070–6148,6302–6440; BE1805.01016v3 LF2340–2422,2629–2808,3118–3190. Whole applicable proof units in these ranges were read; many recursively cited theorems remain primary background statements rather than independently reconstructed full proofs. The general energy/MA construction is an exact published source theorem. All new applications and the proposed reduction remain unreviewed.



END MATHEMATICAL DATA



BEGIN MATHEMATICAL DATA: Original context 8: Exact body accepted ONLY within actual86 scope; historical status statements are documentary

# Local reference conversion and countable-to-arbitrary envelope reduction

New unreviewed root reconstruction. No original problem is declared solved. The two native continuations83/84 keep frozen independent inputs. This record supplies two precise proposed reductions using newly checked BJ3.9–3.10; it does not establish the missing countable singular envelope theorem.

## 1. Genuine nef potentials supply local decreasing raw FS weights

Let \(Y\) be a reduced irreducible projective variety over an algebraically closed trivially valued characteristic-zero field. Let \(M\) be an ACTUAL semiample rational line bundle, \(\theta=c_1(M)\), and let \(A\) be an actual very ample bundle with its canonical FS reference. Let \(\varphi\in\operatorname{PSH}(Y,\theta)\). The claim is that the local weights of the metric \(h_M+\varphi\), in the original \(M\) frames, are locally decreasing limits of genuine affine FS weights. No same-bundle regularization in the nonample nef class is asserted.

BJ4.15(ii) gives a decreasing NET \(\varphi_i\in H(L_i)\), with actual ample rational \(L_i\) and \(c_1(L_i)\to\theta\). These are finite continuous rational PL potentials. For each positive rational \(\delta\), the class \(\theta+\delta c_1(A)\) is ample. Openness of the ample cone implies that
\[
 \theta+\delta c_1(A)-c_1(L_i)\in\operatorname{Amp}(Y)
\]
for all sufficiently large \(i\). Set \(M_\delta=M+\delta A\). On every VALID pair \((i,\delta)\) satisfying this inequality, \(\varphi_i\in\operatorname{PL}\cap\operatorname{PSH}(M_\delta)\): add the genuine zero potential in the indicated nef difference class. This uses the original scalar \(\varphi_i\), not a new function identified only on divisorial points.

Fix local frames \(e_M,e_A\) on a Zariski affine neighborhood \(U\). Choose \(e_A\) from a basepoint-free section system for \(A\); its canonical local reference weight
\[
 h_A=\max_j\log|s_j/e_A|
\]
is nonnegative, since the \(e_A/e_A=1\) term occurs. The canonical trivial metric is multiplicative on rational tensor products, so the actual \(M_\delta\) reference in these SAME frames is \(h_M+\delta h_A\). Choose a compact rational analytic neighborhood \(Q\Subset U^{an}\) containing the tested point in its ordinary interior, allowing radii in \(\exp(\mathbb Q)\); strictness over the trivially valued ground field is not assumed. Dense rational logarithmic bounds in the finite affine charts supply such neighborhoods. On \(Q\), both reference weights are finite continuous and bounded.

Order valid pairs by increasing \(i\) and decreasing \(\delta\). This set is directed: for two pairs choose a smaller positive rational \(\delta'\) and an \(i'\) above both indices and past the ample-cone tail for \(\delta'\). The raw weights
\[
 w_{i,\delta}=\varphi_i+h_M+\delta h_A
\]
decrease on \(Q\). Their pointwise limit is \(w=\varphi+h_M\). For every tested point choose \(\delta\) small using boundedness of \(h_A\), and then a valid sufficiently large \(i\); this proves the limit even when \(w=-\infty\).

For each fixed valid pair, BJ3.10 gives uniform approximation of \(\varphi_i\) by \(H^{dom}(M_\delta)\). The crucial literal inclusion in BJ3.9 is
\[
 H^{dom}(M_\delta)\subset H(M_\delta),
\]
because \(M_\delta\) is an ACTUAL ample rational line bundle. Thus the approximants are metrics on this same bundle. With errors \(\epsilon_j=4^{-j}\) and shifts \(B_j=2\sum_{\ell\ge j}\epsilon_\ell\), shifted FS approximants decrease uniformly to \(\varphi_i\). Indeed the consecutive downward difference is at least \(2\epsilon_j-\epsilon_j-\epsilon_{j+1}>0\). Adding the fixed \(h_M+\delta h_A\) gives decreasing genuine raw FS weights tending to \(w_{i,\delta}\).

Clear the rational tensor exponent in \(M_\delta\). In the frame \(e_M^m e_A^{m\delta}\), these raw weights are finite maxima of logarithms of regular section ratios on \(U\), divided by \(m\), with rational finite weights. Their generating sections have no common zero. If the affine FS convention requires all generators of the ORIGINAL coordinate ring of \(U\), append their positive logarithmic branches and a constant floor with sufficiently negative finite weights. On compact \(Q\) the old maximum has a finite minimum and every generator a finite upper norm bound. The appended branches can therefore be made strictly inactive on ALL of \(Q\); the values and decreasing order on \(Q\) remain exact.

Apply BJ Lemma4.6 on the compact space \(Q\), with the collection of these raw affine FS functions as the families, stable under adding constants, and the parameter space reduced to one point. Every outer \(w_{i,\delta}\) is a decreasing limit from that collection; the outer net itself decreases to \(w\). The lemma therefore flattens the two levels to ONE decreasing net of genuine affine FS weights on \(Q\). It requires neither minimum stability of the psh class nor a diagonal sequence for an uncountable net. Its proof uses compactness and strictly shifted continuous majorants. Restrict to the ordinary open interior of \(Q\) to obtain the required common local neighborhood.

The canonical reference on a semiample rational \(M\) is literally the zero-weight FS metric from any globally generating tensor power, so this identifies the original local metric, not just a class. On a resolution with \(M=\pi^*L\), proper functoriality of the trivial model metric identifies \(h_M\) with the pullback of the original \(h_L\). Once all-point scalar fiber constancy is proved, the descended \(\psi+h_L\) therefore has ONE proper birational witness whose pullback is locally genuinely regularizable.

This supplies the proposed LOCAL input to the countable weak-to-genuine theorem. Its final global membership in the ORIGINAL ample target class is still the unresolved C1 theorem. The proof above does not infer singular EP from a local curve test or apply BJ5.13 before its EP hypotheses.

## 2. Precise countable-to-arbitrary envelope implication

Assume the following SINGLE analytic premise E:

> Every reduced irreducible geometrically unibranch projective variety over every COUNTABLE algebraically closed trivially valued characteristic-zero field has the envelope property in every actual ample rational line-bundle class.

The proposed conclusion is the same statement over arbitrary-cardinality algebraically closed trivially valued characteristic-zero fields. Premise E is not established or granted by either pending native run.

Fix \(X,L\) over such an arbitrary \(k\), and first take a finite rational PL obstacle \(f\). Descend finitely many coefficients of \(X,L,f\) to a countable algebraically closed \(k_0\subset k\). Include an ample embedding, finite presentations of the normalization \(\nu:X^\nu\to X\), its multiplication tables and overlap maps, and its inverse on one nonempty affine open. These finitely many data descend a finite birational morphism \(\nu_0:N_0\to X_0\). Faithful flatness makes \(X_0\) reduced and integral. Normality of \(N_0\) descends by Stacks033G; its proof contracts a principal ideal under faithful flatness. A finite normal birational algebra inside the common fraction field is the actual integral closure, so \(\nu_0\) is the normalization.

The original \(\nu\) is a universal homeomorphism by geometric unibranchness. This property descends along the fpqc morphism \(X_k\to X_0\) by Stacks0CEX. Consequently the local normalization rings of \(X_0\) are local with purely inseparable residue extensions; Stacks0BPZ's definition makes \(X_0\) geometrically unibranch. The finite presentations and inverse on a dense open retain the ORIGINAL nonnormal generic fiber. The ample embedding retains an actual ample rational \(L_0\). Thus E applies to \(X_0,L_0\).

Let \(r_0:X_k^{an}\to X_0^{an}\). This is surjective. For an explicit value lift of \(x\in X_0^{an}\), start with \(\mathscr H(x)\), adjoin independent variables of Gauss radius one indexed by a transcendence basis of \(k/k_0\), and complete the Gauss field. Embed the algebraic extension \(k/k_0(T)\) into its algebraic closure and complete again. Its restriction to \(k\) is trivial: a nonzero element algebraic over the trivially normed \(k_0(T)\) cannot have norm greater or less than one by the dominant-term test in a monic equation with nonzero constant. The original \(\mathscr H(x)\) norm is unchanged. Composing the coordinate maps to this complete field defines a point over \(k\) lifting \(x\). Only finite polynomials enter each Gauss norm, so an infinite transcendence basis causes no change.

By E and BJ5.17,
\[
 \psi_0=P_{L_0}(f_0)
\]
is continuous and genuinely \(L_0\)-psh. Pullback of its fixed-\(L_0\) FS approximants makes \(\psi=\psi_0\circ r_0\) continuous and genuinely \(L\)-psh. Section4 of continuation89 gives the ACTUAL continuous raw MA base-change pushforward, with its proof now using the literal BJ3.9 inclusion. BJ13.1 orthogonality on \(X_0\) yields
\[
 \int(f-\psi)\,\operatorname{MA}_{\rm raw,L}(\psi)=0.
\]
The integrand is nonnegative. This proves equality almost everywhere, without asserting any inverse-image equality of measure supports.

Take a finite \(h\in H^{dom}(L)\) with \(h\le f\). BJ3.9 represents it by a literal finite FS section system on the SAME actual \(mL\), with no common zero. Descend its finitely many section coefficients to a countable algebraically closed \(k_2\subset k\) containing \(k_0\). Global sections commute with field extension: on a finite affine trivializing cover they are the matching equalizer, and flat extension commutes with that finite equalizer. Include only the finitely many coefficients occurring in that representation. The cokernel of its generating evaluation map vanishes after faithfully flat base change to \(k\), hence vanishes already over \(k_2\). Thus the descended \(h_2\) is genuinely in \(H(L_2)\). No separate varying bundle or model nef inequality is needed for this finite competitor.

Surjectivity of restriction transfers \(h\le f\) to \(h_2\le f_2\). The continuous \(\psi_2=\psi_0\circ r_{2/0}\) is genuine and bounded, hence in \(E^1(X_2,L_2)\), without assuming E anew for \(X_2\). Actual MA pushforward transfers orthogonality from \(k_0\) to \(k_2\), so \(h_2\le f_2=\psi_2\) almost everywhere for \(\operatorname{MA}(\psi_2)\). BJ10.6 domination on this irreducible projective \(X_2\) yields \(h_2\le\psi_2\) everywhere. Its hypotheses do not require EP or inverse MA existence on \(X_2\). Pullback gives \(h\le\psi\) on the original \(X_k\).

Now take ANY actual competitor \(q\in\operatorname{PSH}(X,L)\) with \(q\le f\). BJ4.15(iii) gives decreasing continuous \(H^{dom}(L)\) majorants \(h_j\to q\). For rational \(\epsilon>0\), the decreasing closed sets \(\{h_j\ge f+\epsilon\}\) have empty intersection. Compactness forces one entire tail empty. Then \(h_j-\epsilon\le f\); its rational constant shift remains in \(H^{dom}(L)\), and the finite-competitor argument gives
\[
 q\le h_j\le\psi+\epsilon.
\]
Let \(\epsilon\downarrow0\). Since \(\psi\le f\) is itself feasible, this proves the exact envelope identity
\[
 P_L(f)=P_{L_0}(f_0)\circ r_0.
\]
It is continuous and genuinely in the original class. Each finite competitor descended to its OWN countable field; an arbitrary net or family was never assigned one common field.

Finite rational PL tests are uniformly dense in \(C^0(X^{an})\). The envelope Lipschitz inequality and genuine uniform closure extend the conclusion to every continuous obstacle. BJ5.17 then gives EP in \(c_1(L)\). For a real ample class, choose rational ample classes tending to it from above and use the actual nef-reference inclusion and BJ4.5 varying-class closure, as in BJ5.9. This last step uses numerical class closure only after the genuine rational target classes have been established.

Thus, subject to checking all new applications, the arbitrary-cardinality step is reduced to premise E. It does not require a new singular finite-energy inverse theorem for the larger countable competitor field or descent of a whole PSH space.

Primary bodies newly checked: BJ1801.08229v4 LF1400–1464,1596–1735,2170–2295,2408–2494,2894–2976; the energy/base-change/orthogonality units and exact source limits recorded in continuation89. Live Stacks033G rendered lines24–31,0CEX lines22–23 and0BPZ lines23–24 were read in full for the pertinent statements/proofs. These web coordinates are not cached LF hashes and no complete web-page pin is asserted. Ordinary Gauss extension and algebraic-closure norm extension are basic valued-field inputs, not affine regularization theorems over those auxiliary fields. The countable singular EP premise, all-point fiber constancy and original equation conclusion remain unproved by this record.



END MATHEMATICAL DATA



BEGIN MATHEMATICAL DATA: Original context 9: TASK-GRANTED actual87 precise PARTIAL review only

{
  "verdict": "PASS",
  "report": "PASS for root91’s precise retained partial scope. The geometric constructions, actual-reference identities, and countable sequence extraction are correct. This does not establish singular EP, fiber constancy, antecedent E, the pending affine chain, or original P16.1. The supplied accepted bodies are used only within their task-granted scopes; their earlier verdicts do not certify any new root91 assertion.\n\nThe original generators give a surjection k[x₁,…,xₙ]→R and hence an actual closed affine embedding. The reduced projective closure X₀ is integral and restricts scheme-theoretically to U on x₀≠0. The section x₀ of O(1)|X₀ is nonzero at the generic point, so its local equations are nonzerodivisors. Its zero scheme is therefore an effective Cartier divisor with exactly the required complement as support, and its bundle is ample.\n\nTemkin’s hypotheses are satisfied: X₀ is Noetherian, excellent, integral and generically reduced, and characteristic zero supplies its morphism to Spec(Q). The theorem preserves the entire original regular locus, which contains all of U. Its blowup sequence is finite; the proof’s codimension construction stabilizes, as checked in Lemma 4.1.3 and the main proof. Every center has a coherent ideal, so each blowup is projective. The intermediate schemes remain integral: their nonempty affine blowup charts are subrings of the original function field. The final regular finite-type k-scheme is smooth because k is perfect. Neither a cardinality restriction nor an SNC-boundary theorem is needed. [Temkin](https://arxiv.org/pdf/0904.1592v2), [regularity and smoothness](https://stacks.math.columbia.edu/tag/0B8X).\n\nThe boundary induction is valid on singular intermediate schemes. On a finite affine cover trivializing Dⱼ, write its ideal as (d). Center support inside V(d) implies d lies in the radical of the center ideal; a maximum of the finitely many local exponents gives one uniform N. Pullback preserves the ideal containment, without requiring flatness. On a blowup chart with exceptional equation e, dᴺ=e q for a regular q. Since the chart is a domain and dᴺ is nonzero, q is a nonzerodivisor. Thus Nb*Dⱼ−E is an effective Cartier divisor. This verifies effectivity directly, without using Weil coefficients on a singular scheme.\n\nThe sign is O(−E)=O(1), and this bundle is relatively ample. For m≥N+1, the equation q d^(m−N) shows that mb*Dⱼ−E is effective and has precisely the full inverse-image boundary support. Outside that support both factors are units. Relative ampleness combined with the old ample bundle makes this divisor absolutely ample for every sufficiently large m, so the two bounds on m can be imposed together. Iterating preserves all of U and proves the claimed ample-boundary completion. [Blowup properties](https://stacks.math.columbia.edu/tag/01OF), [projectivity](https://stacks.math.columbia.edu/tag/02NS), [ample twisting](https://stacks.math.columbia.edu/tag/01VG).\n\nRelative Chow is applied over the same U. Properness of P→U supplies the separated finite-type hypothesis; properness of P over k is unnecessary. Taking the schematic closure of the dense isomorphism open and then the reduced refinement gives an integral P′ birational to P. The immersion P′→Pʳ_U is proper: its graph is closed because Pʳ_U is separated over U, and the graph projection is a base change of the proper map P′→U. Consequently it is a closed immersion. [Relative Chow and refinements](https://stacks.math.columbia.edu/tag/02O2), [closed-image immersions](https://stacks.math.columbia.edu/tag/01IQ).\n\nThe schematic closure of P′ in X×Pʳ_k restricts to all of P′ over U. Locally this follows by restricting the closure ideal to the open ambient space containing the already closed P′; reduction changes nothing there. The closure is integral, projective over k, and projective birational over X. Resolving it gives a smooth integral projective source Z. Restriction over U produces actual proper birational maps Z_U→P′→P. Their images contain the generic point and are closed, so they are surjective. The original witness and its exceptional points are retained. Pulling back each supplied contact approximant preserves its support inequality, contact equality, constant, unit logarithms and pointwise decreasing limit.\n\nFor finitely many witnesses, choose a common dense open where all are isomorphisms. The reduced closure of its diagonal in their fiber product is integral and proper over U. Each projection is proper and has dense, hence full, image in the corresponding integral witness. Chow refinement and resolution preserve these dominating maps. This retains every exceptional point of each witness individually; it asserts neither realization of every tuple in the fiber product nor domination of an infinite family.\n\nSection localization is literal in the original ring. On finitely many affine charts trivializing D, every zᵢ is a fraction with a power of the local boundary equation as denominator. One common exponent clears all denominators, and the resulting sections glue because they represent the same rational section zᵢs_Dʳ. All sufficiently large powers of the ample bundle are very ample, so one r satisfies both extension and very-ampleness requirements. Append these sections and s_Dʳ to a finite generating system. Every ratio belongs to R, and the displayed generator ratios are exactly the original zᵢ. [Large very ample powers](https://stacks.math.columbia.edu/tag/02NO).\n\nThe constant ratio gives g≥0, and the generator ratios give log|zᵢ|≤g. For a polynomial F of degree d, the ultrametric inequality and trivial coefficient norms give log|F|≤dg. Applying this to the finitely many branches of the original affine FS bound gives H≤Ag+C with rational A>0. The original input and its growth hypothesis are unchanged. If the accepted smooth gate requires g≥1 and an absorbed additive constant, a rational constant shift of the FS weights supplies that normalization.\n\nThe metric identity uses the actual B and π̄*B. Set g₀=−log||s_Dʳ||triv and p=maxⱼ log||σⱼ||triv; then g=g₀+p in the boundary-section frame. Here the chosen zero-weight generating system gives p=0, which is a genuine FS potential. Canonical metrics pull back exactly because proper maps carry valuation centers to their images and pulled center frames still have norm one. Finite FS formulas pull back section by section, retaining their weights, including vanishing-section values. Thus the identities hold at every analytic point. Pullback preserves the generating system, so π̄*B is semiample; its curve degrees are nonnegative by the projection formula, hence it is nef. [Canonical metrics and FS formulas](https://arxiv.org/pdf/1801.08229v4).\n\nThese constructions apply independently to any smooth integral affine open and to its product with A¹: the product has original ring R[t], is smooth and integral, and a proper birational witness may be supplied there or obtained by base change. This establishes the geometric inputs, while retaining the contact, growth and analytic hypotheses of the accepted smooth gate. It does not establish the pending affine chain.\n\nOver countable k, a finite-type affine ring is countable. The seminorm evaluation map identifies its analytification with a subspace of a countable product of real half-lines, with the induced topology. Such a product, and every subspace, is second countable. A finite affine open cover gives the same conclusion for the auxiliary finite-type varieties and their analytic domains. This argument does not infer metrizability from separability. [Affine seminorm topology](https://arxiv.org/pdf/1805.01016v3#page=31).\n\nThe extraction lemma is self-contained and correct. For every rational t, infᵢaᵢ(x)<t holds exactly when some aᵢ(x)<t. Thus the displayed open-sublevel union is exact, including where the infimum is −∞. Second countability passes to each open subspace and implies Lindelöfness: from a countable base, choose a covering member for each base element contained in one. Selecting countably many indices for each rational t and then taking their countable union suffices. Directedness recursively supplies indices above the preceding index and each newly selected index. The resulting sequence decreases, stays above a, and eventually falls below every rational threshold greater than a(x). Its infimum is therefore exactly a at every point, including −∞. Compactness is unnecessary for this extraction itself.\n\nThe sequence consequence preserves continuation90’s actual-reference conversion hypotheses. Its rational-weight version uses the already supplied positive rational shifts. Restricting a flattened net to the extracted indices preserves its values and order on the common Q. At any tested point an active finite branch either is the floor or has nonzero seminorm. In the latter case its regular function is a unit on its principal open, and its logarithmic branch is a support with precisely the same constant and value. Zero branches are locally suppressed by the finite floor; finitely many surviving branches or tested functions admit a common intersection neighborhood. This proves contact support at all analytic values without replacing the reference or asserting same-nef-bundle global approximation.\n\nHarmless clarifications: p need not be nonzero; increasing extracted indices need not be cofinal in the original directed set; a finite selected index set can be enumerated with repetitions; and smooth source does not mean smooth morphism. In dimension zero, the empty boundary is an effective Cartier divisor and its trivial bundle is ample. These require no substantive repair.\n\nAll-point fiber constancy, scalar descent, target first membership, singular EP and E remain separate hypotheses or missing gates exactly as stated. The final conditional sequence consequence establishes none of them. Hashes, compilation and runtime observations play no role in this verdict.",
  "passages": [
    {
      "id": "330a7655-d91a-4178-977d-ca08bcc5d7ac/0",
      "statement": "Every scheme locally of finite type over a field is excellent (Stacks Lemma 29.20.7).",
      "url": "https://stacks.math.columbia.edu/tag/0HA6",
      "quote": "Any scheme locally of finite type over a field.",
      "premise": 0
    },
    {
      "id": "330a7655-d91a-4178-977d-ca08bcc5d7ac/1",
      "statement": "For every Noetherian quasi-excellent generically reduced scheme X over Spec(Q), Temkin Theorem 1.2.1 supplies a finite sequence of blowups whose centers are regular and disjoint from the inverse images of the original regular locus, and whose final scheme is regular. A blowup sequence in this theorem is a composition of finitely many blowups, as defined in §2.2.2.",
      "url": "https://arxiv.org/pdf/0904.1592v2#page=3",
      "quote": "the centers of the blow ups are disjoint from the preimages of the regular locus",
      "premise": 1
    },
    {
      "id": "330a7655-d91a-4178-977d-ca08bcc5d7ac/2",
      "statement": "For every Noetherian quasi-excellent generically reduced scheme X over Spec(Q), Temkin Theorem 1.2.1 supplies a finite sequence of blowups whose centers are regular and disjoint from the inverse images of the original regular locus, and whose final scheme is regular. A blowup sequence in this theorem is a composition of finitely many blowups, as defined in §2.2.2.",
      "url": "https://arxiv.org/pdf/0904.1592v2#page=10",
      "quote": "composition of n ≥ 0 blow ups",
      "premise": 1
    },
    {
      "id": "330a7655-d91a-4178-977d-ca08bcc5d7ac/3",
      "statement": "For a scheme X and a finite-type quasi-coherent ideal I defining a closed subscheme C, the blowup b:X′→X is projective and O_X′(1) is relatively ample. It is an isomorphism over X\\C; E=b⁻¹(C) is an effective Cartier divisor, I O_X′=O_X′(−E), and O_X′(−E)≅O_X′(1) (Stacks Lemmas 31.33.4 and 31.33.13).",
      "url": "https://stacks.math.columbia.edu/tag/01OF",
      "quote": "the exceptional divisor $E = b^{-1}(Z)$ is an effective Cartier divisor on $X'$",
      "premise": 2
    },
    {
      "id": "330a7655-d91a-4178-977d-ca08bcc5d7ac/4",
      "statement": "For a scheme X and a finite-type quasi-coherent ideal I defining a closed subscheme C, the blowup b:X′→X is projective and O_X′(1) is relatively ample. It is an isomorphism over X\\C; E=b⁻¹(C) is an effective Cartier divisor, I O_X′=O_X′(−E), and O_X′(−E)≅O_X′(1) (Stacks Lemmas 31.33.4 and 31.33.13).",
      "url": "https://stacks.math.columbia.edu/tag/01OF",
      "quote": "$\\mathcal{O}_{X'}(-1) = \\mathcal{O}_{X'}(E)$",
      "premise": 2
    },
    {
      "id": "330a7655-d91a-4178-977d-ca08bcc5d7ac/5",
      "statement": "For a scheme X and a finite-type quasi-coherent ideal I defining a closed subscheme C, the blowup b:X′→X is projective and O_X′(1) is relatively ample. It is an isomorphism over X\\C; E=b⁻¹(C) is an effective Cartier divisor, I O_X′=O_X′(−E), and O_X′(−E)≅O_X′(1) (Stacks Lemmas 31.33.4 and 31.33.13).",
      "url": "https://stacks.math.columbia.edu/tag/02NS",
      "quote": "$\\mathcal{O}_{X'}(1)$ is a $b$-relatively ample invertible sheaf.",
      "premise": 2
    },
    {
      "id": "330a7655-d91a-4178-977d-ca08bcc5d7ac/6",
      "statement": "For a morphism f:X→Y of schemes, an f-ample invertible sheaf L on X, and an ample invertible sheaf M on Y, L⊗f*M^a is ample on X for every sufficiently large integer a (Stacks Lemma 29.38.7).",
      "url": "https://stacks.math.columbia.edu/tag/01VG",
      "quote": "then $\\mathcal{L} \\otimes f^*\\mathcal{M}^{\\otimes a}$ is ample for $a \\gg 0$.",
      "premise": 3
    },
    {
      "id": "330a7655-d91a-4178-977d-ca08bcc5d7ac/7",
      "statement": "For a perfect field k and a reduced scheme X locally of finite type over k, the locus where X→Spec(k) is smooth equals the locus where the local rings of X are regular (Stacks Lemma 33.25.8).",
      "url": "https://stacks.math.columbia.edu/tag/0B8X",
      "quote": "The equality of the two sets follows immediately from Algebra, Lemma 10.140.5",
      "premise": 4
    },
    {
      "id": "330a7655-d91a-4178-977d-ca08bcc5d7ac/8",
      "statement": "If S is Noetherian and T→S is separated and of finite type, there exist an immersion T′→Pⁿ_S and a proper surjective S-morphism T′→T that is an isomorphism over a dense open W⊂T. T′ can be replaced by the schematic closure of that isomorphism open; if T is reduced, T′ can be chosen reduced (Stacks Lemma 30.18.1 and Remark 30.18.2).",
      "url": "https://stacks.math.columbia.edu/tag/02O2",
      "quote": "proper and surjective",
      "premise": 5
    },
    {
      "id": "330a7655-d91a-4178-977d-ca08bcc5d7ac/9",
      "statement": "If S is Noetherian and T→S is separated and of finite type, there exist an immersion T′→Pⁿ_S and a proper surjective S-morphism T′→T that is an isomorphism over a dense open W⊂T. T′ can be replaced by the schematic closure of that isomorphism open; if T is reduced, T′ can be chosen reduced (Stacks Lemma 30.18.1 and Remark 30.18.2).",
      "url": "https://stacks.math.columbia.edu/tag/02O2",
      "quote": "If $X$ is reduced then we may choose $X'$ reduced.",
      "premise": 5
    },
    {
      "id": "330a7655-d91a-4178-977d-ca08bcc5d7ac/10",
      "statement": "An immersion f:Y→X of schemes is a closed immersion if and only if its image f(Y) is a closed subset of X (Stacks Lemma 26.10.4).",
      "url": "https://stacks.math.columbia.edu/tag/01IQ",
      "quote": "if and only if $f(Y) \\subset X$ is a closed subset.",
      "premise": 6
    },
    {
      "id": "330a7655-d91a-4178-977d-ca08bcc5d7ac/11",
      "statement": "If X is a finite-type scheme over a field k and L is an ample invertible sheaf on X, then for every sufficiently large integer d there is a finite globally generating section system of L^d defining an immersion X→Pⁿ_k with pullback O(1)≅L^d. If X is proper over k, this immersion is closed (Stacks Lemmas 29.40.3–29.40.4 and 26.10.4).",
      "url": "https://stacks.math.columbia.edu/tag/02NO",
      "quote": "for every $d \\geq d_0$ there exist an $n \\geq 0$ and an immersion",
      "premise": 7
    },
    {
      "id": "330a7655-d91a-4178-977d-ca08bcc5d7ac/12",
      "statement": "For a reduced projective variety X over an algebraically closed trivially valued field and an actual rational line bundle L, the canonical trivial metric is continuous and gives norm one to frames at valuation centers. Globally generating sections s_j of mL and rational weights λ_j define a finite continuous genuine L-psh potential m⁻¹max_j(log||s_j||triv+λ_j). For a morphism f:Y→X of projective varieties, its pullback is the FS potential on f*L defined by the pulled sections and unchanged weights (BJ Remark 1.24, Definition 2.18, Proposition 2.19(iv), and Definition 4.1).",
      "url": "https://arxiv.org/pdf/1801.08229v4#page=19",
      "quote": "continuous metric characterized by |τ | ≡ 1",
      "premise": 8
    },
    {
      "id": "330a7655-d91a-4178-977d-ca08bcc5d7ac/13",
      "statement": "For a reduced projective variety X over an algebraically closed trivially valued field and an actual rational line bundle L, the canonical trivial metric is continuous and gives norm one to frames at valuation centers. Globally generating sections s_j of mL and rational weights λ_j define a finite continuous genuine L-psh potential m⁻¹max_j(log||s_j||triv+λ_j). For a morphism f:Y→X of projective varieties, its pullback is the FS potential on f*L defined by the pulled sections and unchanged weights (BJ Remark 1.24, Definition 2.18, Proposition 2.19(iv), and Definition 4.1).",
      "url": "https://arxiv.org/pdf/1801.08229v4#page=26",
      "quote": "for any morphism f : Y → X from a projective variety we have",
      "premise": 8
    },
    {
      "id": "330a7655-d91a-4178-977d-ca08bcc5d7ac/14",
      "statement": "For an affine finite-type scheme Spec(A) over a complete non-Archimedean field K, its Berkovich analytification is the set of multiplicative seminorms on A extending the given absolute value, with the topology of pointwise convergence. Analytifications of separated finite-type schemes are obtained by gluing their affine analytifications along the corresponding open subsets (Boucksom–Eriksson §4.1).",
      "url": "https://arxiv.org/pdf/1805.01016v3#page=31",
      "quote": "endowed with the topology of pointwise convergence.",
      "premise": 9
    }
  ],
  "premises": [
    "Every scheme locally of finite type over a field is excellent (Stacks Lemma 29.20.7).",
    "For every Noetherian quasi-excellent generically reduced scheme X over Spec(Q), Temkin Theorem 1.2.1 supplies a finite sequence of blowups whose centers are regular and disjoint from the inverse images of the original regular locus, and whose final scheme is regular. A blowup sequence in this theorem is a composition of finitely many blowups, as defined in §2.2.2.",
    "For a scheme X and a finite-type quasi-coherent ideal I defining a closed subscheme C, the blowup b:X′→X is projective and O_X′(1) is relatively ample. It is an isomorphism over X\\C; E=b⁻¹(C) is an effective Cartier divisor, I O_X′=O_X′(−E), and O_X′(−E)≅O_X′(1) (Stacks Lemmas 31.33.4 and 31.33.13).",
    "For a morphism f:X→Y of schemes, an f-ample invertible sheaf L on X, and an ample invertible sheaf M on Y, L⊗f*M^a is ample on X for every sufficiently large integer a (Stacks Lemma 29.38.7).",
    "For a perfect field k and a reduced scheme X locally of finite type over k, the locus where X→Spec(k) is smooth equals the locus where the local rings of X are regular (Stacks Lemma 33.25.8).",
    "If S is Noetherian and T→S is separated and of finite type, there exist an immersion T′→Pⁿ_S and a proper surjective S-morphism T′→T that is an isomorphism over a dense open W⊂T. T′ can be replaced by the schematic closure of that isomorphism open; if T is reduced, T′ can be chosen reduced (Stacks Lemma 30.18.1 and Remark 30.18.2).",
    "An immersion f:Y→X of schemes is a closed immersion if and only if its image f(Y) is a closed subset of X (Stacks Lemma 26.10.4).",
    "If X is a finite-type scheme over a field k and L is an ample invertible sheaf on X, then for every sufficiently large integer d there is a finite globally generating section system of L^d defining an immersion X→Pⁿ_k with pullback O(1)≅L^d. If X is proper over k, this immersion is closed (Stacks Lemmas 29.40.3–29.40.4 and 26.10.4).",
    "For a reduced projective variety X over an algebraically closed trivially valued field and an actual rational line bundle L, the canonical trivial metric is continuous and gives norm one to frames at valuation centers. Globally generating sections s_j of mL and rational weights λ_j define a finite continuous genuine L-psh potential m⁻¹max_j(log||s_j||triv+λ_j). For a morphism f:Y→X of projective varieties, its pullback is the FS potential on f*L defined by the pulled sections and unchanged weights (BJ Remark 1.24, Definition 2.18, Proposition 2.19(iv), and Definition 4.1).",
    "For an affine finite-type scheme Spec(A) over a complete non-Archimedean field K, its Berkovich analytification is the set of multiplicative seminorms on A extending the given absolute value, with the topology of pointwise convergence. Analytifications of separated finite-type schemes are obtained by gluing their affine analytifications along the corresponding open subsets (Boucksom–Eriksson §4.1)."
  ],
  "kind": "codex-report",
  "operationId": "330a7655-d91a-4178-977d-ca08bcc5d7ac",
  "reportedAt": "2026-10-05T10:48:18.881Z"
}



END MATHEMATICAL DATA



BEGIN MATHEMATICAL DATA: Original context 10: Binding scope of actual87

# Binding scope of actual round87 partial PASS

The actual canonical review is P16.1-round87-actual-partial-mathematical-review-20261005.json, SHA256 915213c661085fbb723973f27cfaa732d3cdbf3893088c47120900d0ac7af50f, operation 330a7655-d91a-4178-977d-ca08bcc5d7ac, reported 2026-10-05T10:48:18.881Z. It returns PASS only for root91's retained geometric, actual-reference and countable-sequence scope. Its entire report, ten premises and fifteen passages were read and all nonnegative exact premise bindings verified.

The grant supplies the smooth affine ample-boundary completion, proper domination of the ONE original witness, finite witness domination, actual original-generator reference identities, products, and exact countable local sequence extraction. It does not grant the pending affine chain, all-point fiber constancy, target first membership, singular EP, antecedent E or original P16.1.

Read root91 with these actual-review clarifications:

1. For the zero-weight globally generating section system, the global canonical FS potential p is zero. This is a genuine FS potential; it need not be nonzero. The raw affine weight g equals its actual boundary-section reference g0.
2. If the smooth gate needs g at least one or absorbs an additive constant, a rational constant shift of its finite FS weights gives that normalization, preserving the original scalar input and growth hypothesis.
3. Extracted indices need not be cofinal in the old directed set. The open-sublevel proof gives exact pointwise equality. A finite selected set can be enumerated with repetitions. Compactness is unnecessary for extraction itself.
4. Finite witness domination retains each individual witness and every exceptional point; it does not realize every tuple in a fiber product or dominate an arbitrary infinite family.
5. A smooth source is not a smooth morphism. In dimension zero the empty boundary is effective Cartier and its trivial bundle is ample.

The frozen root91 and review input remain unchanged. This addendum binds later use to the actual precise partial grant. Pertinent source bodies were read as recorded previously; reading every listed external proof or whole primary file is not claimed.



END MATHEMATICAL DATA



BEGIN MATHEMATICAL DATA: Original context 11: Exact body accepted ONLY within actual87 scope; historical status statements are documentary

# Geometric witnesses and local sequences for the conditional affine chain

New unreviewed reconstruction for original P16.1. The original solved count remains four. Native review85 assesses the unchanged author83 chain, review86 assesses the unchanged reductions89/90, and author84 retains its independently frozen fiber-reference input. None receives feedback from this draft.

## 1. A smooth affine variety has a smooth projective ample-boundary completion

Let \(k\) be algebraically closed of characteristic zero, with no cardinality restriction, and let \(U=\operatorname{Spec}R\) be a smooth integral affine variety. Embed \(U\) as a CLOSED subscheme of an actual affine space using generators of its original ring. Its reduced projective closure \(X_0\) is integral, \(U=X_0\cap D_+(x_0)\), and the hyperplane section \(D_0=V(x_0)|_{X_0}\) is an effective ample Cartier divisor. The defining section is nonzero in the function field, so it is a nonzerodivisor. Its support is exactly \(X_0\setminus U\).

Apply Temkin0904.1592v2, Theorem1.2.1, to \(X_0\). A finite-type scheme over a field is excellent by Stacks0HA6, Lemma29.20.7; \(X_0\) is Noetherian and generically reduced and has a morphism to \(\operatorname{Spec}\mathbb Q\). Thus the theorem supplies a FINITE sequence of blowups with centers disjoint from the preimage of the original regular locus, ending at a regular variety \(X\). Its definition of a blowup sequence is a finite composition (LF480–492). Every center is therefore supported outside the unchanged smooth \(U\). Blowups are projective because the coherent Rees algebra is generated in degree one. The final \(X\) is projective over \(k\), regular, and smooth over the perfect field \(k\), and its map to \(X_0\) is an isomorphism over ALL of \(U\).

An ample boundary can be retained at EVERY blowup, including on intermediate singular varieties. Suppose \(b:X'\to X_j\) blows up a coherent ideal \(\mathcal I\) whose center is supported on an effective ample Cartier divisor \(D_j\). Because the schemes are Noetherian and quasi-compact, some \(N>0\) satisfies
\[
 \mathcal O(-ND_j)\subset\mathcal I.
\]
This is the local radical-ideal criterion for support inclusion, with a uniform exponent on a finite affine cover. Stacks31.33.4 gives the effective Cartier divisor \(E\), \(\mathcal I\mathcal O_{X'}=\mathcal O(-E)\), and \(\mathcal O(-E)=\mathcal O_{X'}(1)\). This last bundle is \(b\)-relatively ample. Pullback of \(D_j\) remains Cartier: each blowup chart is a subring of a localization of the original integral domain, so its nonzero local defining function remains a nonzerodivisor (also Temkin Lemma4.3.1).

The pulled ideal inclusion gives an effective Cartier difference
\[
 Nb^*D_j-E\ge0.
\]
For \(m\ge N+1\), the divisor
\[
 D_{j+1}=mb^*D_j-E
       =(Nb^*D_j-E)+(m-N)b^*D_j
\]
is effective and has support EXACTLY \(b^{-1}(\operatorname{Supp}D_j)\). It contains that full support through its second summand; both summands have no support outside it. This proves positivity without assigning Weil coefficients on a singular intermediate scheme. Stacks29.38.7 makes \(\mathcal O(-E)\otimes b^*\mathcal O(D_j)^m\) ample for all sufficiently large \(m\). Choose \(m\) satisfying both requirements. Iteration yields a smooth projective \(X\supset U\) with an effective AMPLE Cartier divisor \(D\) supported exactly on \(X\setminus U\). A simple-normal-crossings boundary is not needed for the accepted smooth affine gate.

## 2. Projective smooth domination of the ONE original proper witness

Let \(\mu:P\to U\) be the original proper birational morphism of integral finite-type \(k\)-schemes. Do not assume \(P\) is projective or proper over \(k\). Apply relative Chow's lemma, Stacks30.18.1, with the SAME base \(U\). It supplies a proper surjection \(P'\to P\), an isomorphism over a dense open of \(P\), and an immersion \(P'\to\mathbb P_U^r\). By the schematic-closure refinement in Remark30.18.2, take \(P'\) integral and reduced, so \(P'\to P\) is birational. Its composite \(P'\to U\) is proper.

The immersion into \(\mathbb P_U^r\) is a CLOSED immersion. Indeed its graph into \(P'\times_U\mathbb P_U^r\) is closed because the target is separated over \(U\), and projection to \(\mathbb P_U^r\) is proper by base change of \(P'\to U\). Thus the immersion is proper and has closed image; Stacks01IQ makes it closed. Its reduced schematic closure \(Z_0\) in \(X\times_k\mathbb P_k^r\) is integral and projective over \(k\), projective and birational over \(X\), and satisfies
\[
 Z_0\times_X U=P'
\]
as an ACTUAL scheme, since \(P'\) was closed in the restricted projective space. No exceptional part of the proper witness is lost by closing only its generic graph.

Resolve \(Z_0\) by Temkin1.2.1, obtaining a smooth integral projective \(Z\) and a projective birational morphism \(Z\to Z_0\). The composite
\[
 \bar\pi:Z\longrightarrow X
\]
is projective and birational and has a SMOOTH SOURCE. It need not be a smooth morphism. Over \(U\) it factors as
\[
 Z_U\longrightarrow P'\longrightarrow P\stackrel{\mu}{\longrightarrow}U.
\]
The first two arrows are proper, and their composite dominates the original witness. Pulling an original continuous contact approximant through this composite retains its actual value, its same constant support equality, and logarithms of units; take its decreasing limit only AFTER this pullback. This uses the one specified witness, with an actual dominating map to it, rather than silently replacing the input by a different weak function.

For a FINITE collection of proper birational witnesses over the same \(U\), take the reduced closure of their common generic graph in their fiber product over \(U\), apply relative Chow and resolve as above. It dominates each original witness: every proper projection has closed image containing a dense open of that integral witness. This finite construction makes no assertion for an arbitrary family of witnesses.

## 3. Actual affine and pulled metric references

Choose \(r\) so \(B=\mathcal O_X(rD)\) is very ample, with boundary section \(s_D^r\). Section localization shows that each original generator \(z_i\in R=\Gamma(U,\mathcal O_U)\) is a section ratio on a sufficiently large tensor power of \(\mathcal O(D)\). Enlarge \(r\) so ALL finitely many \(z_i s_D^r\) extend to global sections of \(B\). Include them and \(s_D^r\) in a finite globally generating section system of \(B\). Its finite zero-weight FS metric has raw affine weight
\[
 g=\max_j\log|\sigma_j/s_D^r|\quad\text{on }U.
\]
It is nonnegative through the constant branch and dominates \(\log|z_i|\) for EVERY original generator. Polynomial degree bounds therefore dominate any prescribed original finite affine FS exhaustion by \(Ag+C\), with a positive rational \(A\). A growth hypothesis on the original input is retained; the scalar input is not altered.

Write \(g=g_0+p\), with the actual canonical boundary-section reference \(g_0\) and the genuine global FS potential \(p\) on \(B\). The pullback bundle is the actual \(\bar\pi^*B\), not an ample numerical substitute; it is nef and semiample on smooth \(Z\). Its canonical trivial metric and the finite FS formula pull back functorially in the pulled frames. One can see this literally on the product trivial test configuration \(X\times\mathbb A^1\) and its pulled line bundle. Thus the affine reference upstairs is the pullback of \(g_0\), the global FS term is \(\bar\pi^*p\), and the raw weight is \(g\circ\bar\pi\). This is all-value frame compatibility, not identification only on divisorial points.

These constructions supply the geometrical antecedents called GEO in author83 and the accepted round77 smooth upper-growth/principal-removal theorem, on their scheme-theoretic witness domain. They apply separately to each smooth affine open and to its product with \(\mathbb A^1\). The corresponding analytic theorem still retains its contact hypotheses and smooth genuine nef EP input. This new geometric application has not yet passed independent mathematical review, and neither review85 nor the frozen author84 is allowed to treat it as an already granted result.

## 4. A local decreasing net becomes a sequence over countable \(k\)

Suppose now \(k\) is countable. Every finite-type affine coordinate ring is countable. The seminorm topology is the topology induced by all coordinates \(|f|\), \(f\in R\), in a countable product of real half-lines. Its analytic space and every compact analytic domain \(Q\) are second countable. No metrizability is asserted when \(k\) is uncountable.

Here is the exact extraction lemma. Let \(Q\) be second countable, let \((a_i)\) be a directed decreasing net of finite continuous functions on \(Q\), and let \(a=\inf_i a_i\), including possible value \(-\infty\). For each rational \(t\),
\[
 \{a<t\}=\bigcup_i\{a_i<t\}.
\]
Every open subspace of a second-countable space is Lindelöf, so a COUNTABLE subfamily suffices for each \(t\). Collect these indices over all rational \(t\) and enumerate them. Directedness gives increasing indices \(i_j\), with each \(i_j\) above the first \(j\) selected indices and the preceding \(i_{j-1}\). Then \(a_{i_j}\) decreases and its infimum is exactly \(a\): for any \(x\) and rational \(t>a(x)\), one selected open contains \(x\), and its value bounds the sequence eventually below \(t\). This also proves convergence when \(a(x)=-\infty\). It uses open-sublevel covers, not convergence on a dense countable set or uniform convergence at logarithmic poles.

Consequently, IF continuation90's compact local actual-reference affine-FS conversion is correct, its flattened decreasing net on \(Q\) has a decreasing sequence with the SAME pointwise limit over countable \(k\). Each finite raw FS weight has the required finite rational contact form. At a tested point choose one active finite branch; its regular section ratio has nonzero seminorm and is a unit on the corresponding principal Zariski neighborhood. That branch's logarithmic affine support lies below the whole maximum and has the SAME value and SAME additive constant at the point. A floor handles all zero branches. Thus it has precisely the unit-log support property of the accepted contact class, on one common local neighborhood. No subtraction of psh or same-nef-bundle global FS approximation is used.

After all-point fiber constancy and scalar usc descent on a single resolution are independently established, this extraction would put its actual local pulled metric into the sequence form required by the conditional countable affine chain. It does not itself establish fiber constancy, target first membership, target EP or the original equation.

## 5. Exact primary reading and remaining dependence

The cached Temkin0904.1592v2 PDF has SHA256 \(0c5e2f27ff35a48d605ab1573b9acb027b4fd550574855417e643d24336b5cc3\). Its layout text has SHA256 \(c89838b3bca2d63ac132f370bd694d21a4f4ec4987ccd849927160f5576fc5ee\). UTF8 byte decode and one-based inclusive LF83–147,274–405,462–553,1490–1608 were read. This includes the exact Theorem1.2.1 statement, finite blowup-sequence definition, Cartier pullback proof, and the full pertinent main-theorem proof body. The earlier construction and recursively cited resolution algorithms remain published primary background; a complete independent reconstruction of desingularization is not claimed.

Live primary bodies read: Stacks02O2 rendered22–56, including the entire Chow proof and schematic-closure/reduced refinements; 01OF rendered20–56, including the blowup Cartier/twist proof; 01VG rendered69–79, including the ample-pullback-twist proof; 0HA6 rendered61–70, including the finite-type excellence assertion and proof; 01IQ rendered22–26, the entire closed-image immersion proof. Their observations are saved with live URLs and rendered coordinates, not imaginary immutable editions or original-HTML LF pins.

This draft supplies proposed geometric and countable sequence inputs for joining the independently assessed partial chains. It retains the ORIGINAL nonnormal target and generic fiber, uses resolutions only as dominating auxiliary sources, and retains actual line bundles and all analytic values. The decisive resolved-nef fiber descent, singular countable EP, and independent verification of the resulting complete original proof are still required.



END MATHEMATICAL DATA



BEGIN MATHEMATICAL DATA: Original context 12: TASK-GRANTED actual88 precise PARTIAL review only

{
  "verdict": "PASS",
  "report": "PASS for the specified partial scope: root92 with root93 establishes all-point fiber constancy, including −∞, proper scalar usc descent, and the resolution-fiber application. The later first-membership/EP join is valid only conditionally. This verdict establishes neither global C1 nor singular EP nor original P16.1.\n\nThe valid pairs are directed: choose a smaller positive rational δ, then an index above both given indices and the ample-cone tail for that δ. Their index projection is cofinal and δ tends to zero. For the actual bundle B=M+δA, the actual difference B−L_i is ample; adding its genuine zero potential preserves the scalar φ_i. Literal BJ3.9 and the corrected BJ3.10 interpolation supply uniform rational FS approximation on that same B without EP. The interpolation is toward the ample divisor, followed by rational approximation. Finite section formulas are pulled back before either uniform approximation limits or the original decreasing-net limit. The accepted round86 and round87 bodies are used only within their stated scopes.\n\nThe auxiliary field construction preserves the tested norms. The weighted Gauss norm on F(τ), with |τ|=e⁻¹, is multiplicative: the largest-degree maximal terms give a unique maximal contribution to their product coefficient. Constants retain their original norms. Completion, algebraic closure and completion again produce the required K; roots of τ insert Q into its additive value group. This construction is performed even when F is already nontrivially valued. For F=H(y), evaluation gives an actual K-rational lift of y. A closed fiber point z has finite residue field over H(s); uniqueness of the extended complete-field norm makes every compatible embedding into K isometric. Consequently the lifts retain exactly φ(y) and φ(z), including −∞.\n\nThe one graph model gives compatible maps to both product models. Its flat finite-type structure is finitely presented over K°, without a Noetherian assumption. The two maps to the X-model agree generically; separatedness and schematic generic density of a flat model make them agree everywhere. Thus the actual M-model is pulled from a free line over K°, and its reference is constant in a fixed frame with zero curvature. The actual A-model has nonnegative degree on every special-fiber curve, including contracted curves. Reduced-model replacement is used only over the chosen algebraically closed nontrivial K. The resulting fixed σ_A has the exact component degrees, type-II support and mass deg(f*A). Reduction of fiber topology is never used to discard curvature multiplicities. [BE](https://arxiv.org/pdf/1805.01016v3)\n\nAt each finite approximation stage, rational weights become scalar norms, so the pulled metric is pure FS on the actual B=f*(M+δA). Clearing tensor powers and taking a common model gives a difference metric on the actual trivial generic bundle, using the same generic identification of B. Its signed curvature is μ_j−δσ_A. Completion preserves this metric; semistable refinement pulls back the specified line bundle and frames through a generic-identity morphism, thereby preserving the specified metric. The formal/PL dictionary and curve slope formula therefore give the finite-stage CLD equality. Where KRZB2.6 is invoked, a further type-II refinement avoids its excluded one-point skeleton. Uniform convergence controls current evaluation by the total variation of the fixed measure d'd''q; genuine BE weak curvature convergence on the same bundle gives d'd''[v_i,δ]=[μ_i,δ−δσ_A]. This verifies the signed identity, not merely its mass. [GK](https://arxiv.org/pdf/1406.7637v3), [Wanner](https://arxiv.org/pdf/1801.04713v3), [slope formula](https://arxiv.org/pdf/1504.00694)\n\nRoot93's correction works on every connected strict affinoid V. Only interior background atoms are included. At type II, Wanner4.2 identifies the signed lisse current; its rational short-edge construction applies because Q is already in the value group. At types I and IV the function is locally constant. At an interior type-III point away from its Laplacian support, a smaller annulus gives the affine expression a log|T|+b, whose two Laplacians vanish. Hence the Green current is exactly −δ_ζ on the interior. With p_δ=−δΣa_ζg_ζ, the correction adds precisely the missing positive atoms. It vanishes on the whole boundary and satisfies ||p_δ||≤B_Vδ. Continuous positive-current comparison and the compact maximum principle apply. Boundary atoms require no correction.\n\nThe limit argument uses the original decreasing functions. Compact decreasing boundary superlevel sets have empty intersection, so an entire directed tail is empty. Boundary comparison then gives v_i,δ≤H+ε+B_Vδ; taking the original net limit and then ε↓0 proves harmonic comparison, also at −∞. No monotonicity of the corrected functions is asserted. For each genuine floor max(φ,−m), choose a common upper bound B≥max(0,sup φ). Its curve pullback is bounded usc subharmonic on proper connected C, attains a maximum, and is constant by the strong maximum principle. Floor limits give constancy with all extended values. The supplied Thuillier bodies and the accessible primary thesis statements support the Green and maximum-principle uses; the HAL endpoint itself did not supply a live PDF. [Wanner thesis](https://d-nb.info/1190888386/34)\n\nThe geometric comparison is also valid independently of root81's claimed status. The connected reduced geometric fiber has a connected finite component graph. Resolve its integral components and lift endpoints and intersection points by proper surjectivity. In dimension at least two, blow up two distinct smooth lifts and take general very ample sections. Smoothness follows from Bertini; connectedness follows at each stage from properness, ampleness and depth at least two. The exceptional intersections have positive degree, so the final smooth proper connected curve has points above both endpoints. These are curve morphisms into the original component, and do not require a smooth embedded curve through a singular point. Dimension one uses normalization; dimension zero contributes its single point. Finite chains compare every y to the same fixed z, although K may depend on y. No density substitute is used. [Resolution](https://arxiv.org/pdf/0904.1592v2), [Bertini](https://stacks.math.columbia.edu/tag/0FD6), [connected sections](https://stacks.math.columbia.edu/tag/0FD9)\n\nNonempty geometrically connected fibers give analytic surjectivity. Compactness and Hausdorffness make πan a closed quotient. Thus {ψ≥a}=πan({φ≥a}) is closed for every finite a, proving scalar usc descent. In the birational case the generic trivial point lifts to the generic trivial point, where the genuine potential is finite.\n\nFor a resolution, factor the smooth normal source through the actual normalization Xν first. The induced map p is proper by its closed graph in Y×_X Xν. Its normal integral base, reduced integral source, dominance of every source generic point, and generic fiber Spec k(Xν) satisfy all six 0AY8 hypotheses, including H⁰ of the generic fiber. The theorem therefore applies on Xν. By 0GIQ, normalization is a universal homeomorphism after every residue-field extension. Its finite fiber has one reduced point with purely inseparable residue extension; characteristic zero makes that residue extension the identity. The resulting nilpotent thickening changes neither geometric fiber topology nor analytic seminorms. This verifies every analytic resolution fiber while retaining the original possibly nonnormal X and original L. [Normalization factorization](https://stacks.math.columbia.edu/tag/035Q), [0AY8](https://stacks.math.columbia.edu/tag/0AY8), [0GIQ](https://stacks.math.columbia.edu/tag/0GIQ)\n\nThe conditional join has the correct order. Independently established first membership would make pullback onto; birational divisorial identification and preservation of the generic trivial point then give the normalized homeomorphism. Smooth nef source compactness transports to the target, after which BJ5.11 gives target EP. To supply E, this must hold for every countable allowed target and every actual ample rational L. Only then may the granted cardinality implication and subsequent equation implications be applied. [Smooth source compactness](https://arxiv.org/pdf/1801.08229v4)\n\nThe C1 interface remains unproved here. It must accept the supplied weak local sequences on the one fixed witness, the original bundle/frame, the common ordinary local neighborhoods, and contacts of finite approximants with their exact extended-valued limit. Any additional growth, Runge, principal-removal or globalization requirements must be independently established. Increasing extracted indices need not be cofinal; equality of the pointwise infimum is what is available. Root91's geometric constructions and local contact extraction alone do not certify this global interface.\n\nHarmless corrections are explicit: use a nonnegative common floor upper bound; require Green nonnegativity, with strict positivity only on the relevant interior component; and use smaller annuli inside open skeletal edges. In Wanner4.6–4.7, the needed support condition is containment in the affinoid, not equality with it. The metric-difference sign, uniform regularization upper bound, and dominant logarithmic-coordinate sign are read consistently with the formulas and positive compact test construction. These corrections preserve the retained argument. Documentary hashes and reading logs supply no mathematical acceptance.",
  "passages": [
    {
      "id": "fc6565f4-f59a-487c-9fe4-9e6ef0c6f381/0",
      "statement": "For complete non-Archimedean F, its absolute value extends uniquely to finite algebraic extensions; the completion of its algebraic closure is algebraically closed.",
      "url": "https://arxiv.org/pdf/1805.01016v3",
      "quote": "unique extension",
      "premise": 0
    },
    {
      "id": "fc6565f4-f59a-487c-9fe4-9e6ef0c6f381/1",
      "statement": "For complete non-Archimedean F, its absolute value extends uniquely to finite algebraic extensions; the completion of its algebraic closure is algebraically closed.",
      "url": "https://arxiv.org/pdf/1805.01016v3",
      "quote": "complete algebraically closed extension",
      "premise": 0
    },
    {
      "id": "fc6565f4-f59a-487c-9fe4-9e6ef0c6f381/2",
      "statement": "Flat finite-type K°-models over complete non-Archimedean K are finitely presented. For projective K-schemes and a projective target model, graph models extending a projective morphism are cofinal among projective models and induce exactly the pulled-back model metric.",
      "url": "https://arxiv.org/pdf/1805.01016v3",
      "quote": "finitely presented over K◦",
      "premise": 1
    },
    {
      "id": "fc6565f4-f59a-487c-9fe4-9e6ef0c6f381/3",
      "statement": "Flat finite-type K°-models over complete non-Archimedean K are finitely presented. For projective K-schemes and a projective target model, graph models extending a projective morphism are cofinal among projective models and induce exactly the pulled-back model metric.",
      "url": "https://arxiv.org/pdf/1805.01016v3",
      "quote": "graph of f",
      "premise": 1
    },
    {
      "id": "fc6565f4-f59a-487c-9fe4-9e6ef0c6f381/4",
      "statement": "For algebraically closed complete nontrivially valued K and reduced finite-type K-scheme Z, the integral closure of any K°-model in Z is finite and has reduced special fiber.",
      "url": "https://arxiv.org/pdf/1805.01016v3",
      "quote": "is further reduced.",
      "premise": 2
    },
    {
      "id": "fc6565f4-f59a-487c-9fe4-9e6ef0c6f381/5",
      "statement": "Pure FS metrics on actual rational bundles of projective schemes over complete non-Archimedean K are exactly semiample rational model metrics. On a smooth proper curve over algebraically closed nontrivial K, a reduced projective model gives curvature Σ_E deg(ℒ|E)δ_ζE, at type-II Shilov points, with mass deg(L).",
      "url": "https://arxiv.org/pdf/1805.01016v3",
      "quote": "pure Fubini–Study metric",
      "premise": 3
    },
    {
      "id": "fc6565f4-f59a-487c-9fe4-9e6ef0c6f381/6",
      "statement": "Pure FS metrics on actual rational bundles of projective schemes over complete non-Archimedean K are exactly semiample rational model metrics. On a smooth proper curve over algebraically closed nontrivial K, a reduced projective model gives curvature Σ_E deg(ℒ|E)δ_ζE, at type-II Shilov points, with mass deg(L).",
      "url": "https://arxiv.org/pdf/1805.01016v3",
      "quote": "has finite support.",
      "premise": 3
    },
    {
      "id": "fc6565f4-f59a-487c-9fe4-9e6ef0c6f381/7",
      "statement": "Over algebraically closed complete nontrivially valued K, formal metrics on actual line bundles of varieties are equivalent to integral value-group-affine PL metrics and to strict G-coverings with unit-norm frames. Algebraic metrics become formal by completion; tensor, dual and pullback operations preserve these metrics.",
      "url": "https://arxiv.org/pdf/1406.7637v3",
      "quote": "every algebraic metric is a formal metric.",
      "premise": 4
    },
    {
      "id": "fc6565f4-f59a-487c-9fe4-9e6ef0c6f381/8",
      "statement": "Over algebraically closed complete nontrivially valued K, formal metrics on actual line bundles of varieties are equivalent to integral value-group-affine PL metrics and to strict G-coverings with unit-norm frames. Algebraic metrics become formal by completion; tensor, dual and pullback operations preserve these metrics.",
      "url": "https://arxiv.org/pdf/1406.7637v3",
      "quote": "the following properties are equivalent:",
      "premise": 4
    },
    {
      "id": "fc6565f4-f59a-487c-9fe4-9e6ef0c6f381/9",
      "statement": "Every admissible formal model of a compact connected rig-smooth strictly analytic curve over algebraically closed complete nontrivially valued K admits a semistable refinement by an admissible blowup.",
      "url": "https://math.huji.ac.il/~temkin/papers/Introduction_to_Berkovich_Spaces.pdf",
      "quote": "any formal model C of C admits an admissible blow up",
      "premise": 5
    },
    {
      "id": "fc6565f4-f59a-487c-9fe4-9e6ef0c6f381/10",
      "statement": "For a smooth proper connected curve over algebraically closed complete nontrivially valued K, finite prescribed type-II sets extend to semistable vertex sets. Semistable formal models correspond to these sets, with domination corresponding to inclusion; open skeletal edges come from annuli, value-group points are type II, and complements of analytic open balls are affinoid.",
      "url": "https://arxiv.org/pdf/1404.0279",
      "quote": "sets up a bijection",
      "premise": 6
    },
    {
      "id": "fc6565f4-f59a-487c-9fe4-9e6ef0c6f381/11",
      "statement": "For a smooth proper connected curve over algebraically closed complete nontrivially valued K, finite prescribed type-II sets extend to semistable vertex sets. Semistable formal models correspond to these sets, with domination corresponding to inclusion; open skeletal edges come from annuli, value-group points are type II, and complements of analytic open balls are affinoid.",
      "url": "https://arxiv.org/pdf/1404.0279",
      "quote": "there is a semistable vertex set",
      "premise": 6
    },
    {
      "id": "fc6565f4-f59a-487c-9fe4-9e6ef0c6f381/12",
      "statement": "For a smooth proper connected curve over algebraically closed complete nontrivially valued K, finite prescribed type-II sets extend to semistable vertex sets. Semistable formal models correspond to these sets, with domination corresponding to inclusion; open skeletal edges come from annuli, value-group points are type II, and complements of analytic open balls are affinoid.",
      "url": "https://arxiv.org/pdf/1404.0279",
      "quote": "is an affinoid domain",
      "premise": 6
    },
    {
      "id": "fc6565f4-f59a-487c-9fe4-9e6ef0c6f381/13",
      "statement": "For smooth proper C over algebraically closed complete nontrivially valued K, a rational semistable formal metric w on the actual O_C satisfies d'd''[w]=[Σ_E deg(ℒ|E)δ_ζE]=[dd^c_Thuillier w], with tensor-power normalization. Smooth compactly supported (1,1)-forms define finite signed Radon measures.",
      "url": "https://arxiv.org/pdf/1801.04713v3",
      "quote": "MA(f) = ddcF = ddcf.",
      "premise": 7
    },
    {
      "id": "fc6565f4-f59a-487c-9fe4-9e6ef0c6f381/14",
      "statement": "For smooth proper C over algebraically closed complete nontrivially valued K, a rational semistable formal metric w on the actual O_C satisfies d'd''[w]=[Σ_E deg(ℒ|E)δ_ζE]=[dd^c_Thuillier w], with tensor-power normalization. Smooth compactly supported (1,1)-forms define finite signed Radon measures.",
      "url": "https://arxiv.org/pdf/1801.04713v3",
      "quote": "signed Radon measure",
      "premise": 7
    },
    {
      "id": "fc6565f4-f59a-487c-9fe4-9e6ef0c6f381/15",
      "statement": "For smooth proper C over algebraically closed complete nontrivially valued K, a rational semistable formal metric w on the actual O_C satisfies d'd''[w]=[Σ_E deg(ℒ|E)δ_ζE]=[dd^c_Thuillier w], with tensor-power normalization. Smooth compactly supported (1,1)-forms define finite signed Radon measures.",
      "url": "https://arxiv.org/pdf/1504.00694",
      "quote": "Assume that X is not smooth",
      "premise": 7
    },
    {
      "id": "fc6565f4-f59a-487c-9fe4-9e6ef0c6f381/16",
      "statement": "For such C with Q contained in −log|K×|, a lisse function's CLD current equals its Thuillier Laplacian near type-II points, and the function is locally constant at type-I and IV points. A continuous real function with positive CLD current on an open subset is Thuillier-subharmonic there.",
      "url": "https://arxiv.org/pdf/1801.04713v3",
      "quote": "every type II point",
      "premise": 8
    },
    {
      "id": "fc6565f4-f59a-487c-9fe4-9e6ef0c6f381/17",
      "statement": "For such C with Q contained in −log|K×|, a lisse function's CLD current equals its Thuillier Laplacian near type-II points, and the function is locally constant at type-I and IV points. A continuous real function with positive CLD current on an open subset is Thuillier-subharmonic there.",
      "url": "https://arxiv.org/pdf/1801.04713v3",
      "quote": "then f is subharmonic.",
      "premise": 8
    },
    {
      "id": "fc6565f4-f59a-487c-9fe4-9e6ef0c6f381/18",
      "statement": "On a smooth proper curve over algebraically closed complete nontrivially valued K, a connected strict affinoid V and interior type-II point ζ admit a nonnegative continuous lisse Green function, zero on the boundary and outside V, with interior Laplacian −δ_ζ. A Thuillier-subharmonic function attaining a local maximum is locally constant there.",
      "url": "https://d-nb.info/1190888386/34",
      "quote": "equal to zero on",
      "premise": 9
    },
    {
      "id": "fc6565f4-f59a-487c-9fe4-9e6ef0c6f381/19",
      "statement": "On a smooth proper curve over algebraically closed complete nontrivially valued K, a connected strict affinoid V and interior type-II point ζ admit a nonnegative continuous lisse Green function, zero on the boundary and outside V, with interior Laplacian −δ_ζ. A Thuillier-subharmonic function attaining a local maximum is locally constant there.",
      "url": "https://d-nb.info/1190888386/34",
      "quote": "admits a local maximum",
      "premise": 9
    },
    {
      "id": "fc6565f4-f59a-487c-9fe4-9e6ef0c6f381/20",
      "statement": "Every Noetherian quasi-excellent generically reduced scheme over Spec(Q) admits a finite sequence of blowups with regular centers avoiding the inverse image of its original regular locus and with regular final scheme (Temkin1.2.1).",
      "url": "https://arxiv.org/pdf/0904.1592v2",
      "quote": "Xn is regular",
      "premise": 10
    },
    {
      "id": "fc6565f4-f59a-487c-9fe4-9e6ef0c6f381/21",
      "statement": "Every Noetherian quasi-excellent generically reduced scheme over Spec(Q) admits a finite sequence of blowups with regular centers avoiding the inverse image of its original regular locus and with regular final scheme (Temkin1.2.1).",
      "url": "https://arxiv.org/pdf/0904.1592v2",
      "quote": "composition of n ≥ 0 blow ups",
      "premise": 10
    },
    {
      "id": "fc6565f4-f59a-487c-9fe4-9e6ef0c6f381/22",
      "statement": "For a smooth finite-type scheme over an algebraically closed field, a finite-dimensional globally generating section system of an invertible sheaf whose associated projective map is an immersion has smooth general zero schemes (Stacks0FD6).",
      "url": "https://stacks.math.columbia.edu/tag/0FD6",
      "quote": "the scheme $H_ v$ is smooth over $k'$.",
      "premise": 11
    },
    {
      "id": "fc6565f4-f59a-487c-9fe4-9e6ef0c6f381/23",
      "statement": "If X is proper and connected over a field, ℒ is ample, s is a regular section, and every closed local ring has depth at least two, then Z(s) is connected (Stacks0FD9).",
      "url": "https://stacks.math.columbia.edu/tag/0FD9",
      "quote": "Then the zero scheme $Z(s)$ of $s$ is connected.",
      "premise": 12
    },
    {
      "id": "fc6565f4-f59a-487c-9fe4-9e6ef0c6f381/24",
      "statement": "If every quasi-compact open of X has finitely many irreducible components, a morphism Z→X from a normal scheme whose components dominate components of X factors uniquely through the actual normalization Xν (Stacks035Q).",
      "url": "https://stacks.math.columbia.edu/tag/035Q",
      "quote": "there exists a unique factorization",
      "premise": 13
    },
    {
      "id": "fc6565f4-f59a-487c-9fe4-9e6ef0c6f381/25",
      "statement": "If f:T→S is proper, S is normal integral with generic point ξ, T is reduced, every component generic point of T maps to ξ, and H⁰(T_ξ,O)=κ(ξ), then f_*O_T=O_S and f has geometrically connected fibers (Stacks0AY8).",
      "url": "https://stacks.math.columbia.edu/tag/0AY8",
      "quote": "$f$ has geometrically connected fibres.",
      "premise": 14
    },
    {
      "id": "fc6565f4-f59a-487c-9fe4-9e6ef0c6f381/26",
      "statement": "The normalization of an irreducible geometrically unibranch scheme is a universal homeomorphism (Stacks0GIQ).",
      "url": "https://stacks.math.columbia.edu/tag/0GIQ",
      "quote": "is a universal homeomorphism.",
      "premise": 15
    },
    {
      "id": "fc6565f4-f59a-487c-9fe4-9e6ef0c6f381/27",
      "statement": "A separated finite-type scheme over complete non-Archimedean K has Hausdorff locally compact analytification, compact when proper.",
      "url": "https://arxiv.org/pdf/1805.01016v3",
      "quote": "Hausdorff",
      "premise": 16
    },
    {
      "id": "fc6565f4-f59a-487c-9fe4-9e6ef0c6f381/28",
      "statement": "For a smooth connected projective variety over an algebraically closed trivially valued characteristic-zero field, every nef numerical class has EP and its sup-zero genuine PSH space is compact in the divisorial pointwise topology (BJ5.20–5.21).",
      "url": "https://arxiv.org/pdf/1801.08229v4",
      "quote": "is compact.",
      "premise": 17
    }
  ],
  "premises": [
    "For complete non-Archimedean F, its absolute value extends uniquely to finite algebraic extensions; the completion of its algebraic closure is algebraically closed.",
    "Flat finite-type K°-models over complete non-Archimedean K are finitely presented. For projective K-schemes and a projective target model, graph models extending a projective morphism are cofinal among projective models and induce exactly the pulled-back model metric.",
    "For algebraically closed complete nontrivially valued K and reduced finite-type K-scheme Z, the integral closure of any K°-model in Z is finite and has reduced special fiber.",
    "Pure FS metrics on actual rational bundles of projective schemes over complete non-Archimedean K are exactly semiample rational model metrics. On a smooth proper curve over algebraically closed nontrivial K, a reduced projective model gives curvature Σ_E deg(ℒ|E)δ_ζE, at type-II Shilov points, with mass deg(L).",
    "Over algebraically closed complete nontrivially valued K, formal metrics on actual line bundles of varieties are equivalent to integral value-group-affine PL metrics and to strict G-coverings with unit-norm frames. Algebraic metrics become formal by completion; tensor, dual and pullback operations preserve these metrics.",
    "Every admissible formal model of a compact connected rig-smooth strictly analytic curve over algebraically closed complete nontrivially valued K admits a semistable refinement by an admissible blowup.",
    "For a smooth proper connected curve over algebraically closed complete nontrivially valued K, finite prescribed type-II sets extend to semistable vertex sets. Semistable formal models correspond to these sets, with domination corresponding to inclusion; open skeletal edges come from annuli, value-group points are type II, and complements of analytic open balls are affinoid.",
    "For smooth proper C over algebraically closed complete nontrivially valued K, a rational semistable formal metric w on the actual O_C satisfies d'd''[w]=[Σ_E deg(ℒ|E)δ_ζE]=[dd^c_Thuillier w], with tensor-power normalization. Smooth compactly supported (1,1)-forms define finite signed Radon measures.",
    "For such C with Q contained in −log|K×|, a lisse function's CLD current equals its Thuillier Laplacian near type-II points, and the function is locally constant at type-I and IV points. A continuous real function with positive CLD current on an open subset is Thuillier-subharmonic there.",
    "On a smooth proper curve over algebraically closed complete nontrivially valued K, a connected strict affinoid V and interior type-II point ζ admit a nonnegative continuous lisse Green function, zero on the boundary and outside V, with interior Laplacian −δ_ζ. A Thuillier-subharmonic function attaining a local maximum is locally constant there.",
    "Every Noetherian quasi-excellent generically reduced scheme over Spec(Q) admits a finite sequence of blowups with regular centers avoiding the inverse image of its original regular locus and with regular final scheme (Temkin1.2.1).",
    "For a smooth finite-type scheme over an algebraically closed field, a finite-dimensional globally generating section system of an invertible sheaf whose associated projective map is an immersion has smooth general zero schemes (Stacks0FD6).",
    "If X is proper and connected over a field, ℒ is ample, s is a regular section, and every closed local ring has depth at least two, then Z(s) is connected (Stacks0FD9).",
    "If every quasi-compact open of X has finitely many irreducible components, a morphism Z→X from a normal scheme whose components dominate components of X factors uniquely through the actual normalization Xν (Stacks035Q).",
    "If f:T→S is proper, S is normal integral with generic point ξ, T is reduced, every component generic point of T maps to ξ, and H⁰(T_ξ,O)=κ(ξ), then f_*O_T=O_S and f has geometrically connected fibers (Stacks0AY8).",
    "The normalization of an irreducible geometrically unibranch scheme is a universal homeomorphism (Stacks0GIQ).",
    "A separated finite-type scheme over complete non-Archimedean K has Hausdorff locally compact analytification, compact when proper.",
    "For a smooth connected projective variety over an algebraically closed trivially valued characteristic-zero field, every nef numerical class has EP and its sup-zero genuine PSH space is compact in the divisorial pointwise topology (BJ5.20–5.21)."
  ],
  "kind": "codex-report",
  "operationId": "fc6565f4-f59a-487c-9fe4-9e6ef0c6f381",
  "reportedAt": "2026-10-05T12:01:28.874Z"
}



END MATHEMATICAL DATA



BEGIN MATHEMATICAL DATA: Original context 13: Binding scope of actual88

# Actual review88: binding, reading and retained scope

The completed native Xean result, operation fc6565f4-f59a-487c-9fe4-9e6ef0c6f381,
reported at 2026-10-05T12:01:28.874Z, is PASS only for root92 together with root93.
Its entire report, all 18 premises and all 29 passages have been read at root.
Each nonnegative passage index must be verified against the literal premise
statement in the preservation helper; that verification is documentary binding.

The accepted mathematical scope is the original decreasing-net proof of
all-analytic-point constancy on the indicated proper geometrically connected
fibers, including minus infinity, scalar upper-semicontinuous quotient descent,
and its actual resolution-fiber application. It uses the actual fixed ample
perturbation bundle and reference, the metric-preserving semistable refinement,
the signed curve-current identity, Green correction of interior atoms, and
pointwise curve chains after isometric field extension. It is not only a
divisorial-point or generic-fiber assertion.

Retain the report's harmless clarifications explicitly: a floor has a common
upper bound at least zero; a Green function is nonnegative, and is strictly
positive only on the relevant interior component; use smaller annuli within
open skeletal edges; Wanner's needed support hypothesis is containment in the
affinoid. The auxiliary Gauss extension is made even for nontrivially valued
completed residue fields. The one-point skeleton exception in the applied
slope formula requires an additional type-II refinement. Topological reduction
does not remove curvature multiplicities.

The application to a resolution first factors through the actual normalization.
Connectedness is applied on its normal base with every 0AY8 hypothesis verified,
then transported across the geometric-unibranch universal homeomorphism while
retaining the original possibly nonnormal variety and original polarization.

The first-membership/EP consequence is conditional on a separate local contact
and globalization theorem. Increasing countable extracted indices need not be
cofinal; their exact pointwise infimum is what is proved. Local ordinary
neighborhoods, fixed original witnesses, original frames, growth, principal
removal, Runge and globalization hypotheses must be checked in any later join.
Neither global C1, singular EP nor original P16.1 is solved by review88 alone.

Root94's join, root95's alternative smooth-current proof, author84's new
finite-data arguments, and root98's newly corrected Temkin source application
were not inputs to this review and acquire no grant from its PASS.



END MATHEMATICAL DATA



BEGIN MATHEMATICAL DATA: Original context 14: Exact body accepted ONLY within actual88 scope; historical status statements are documentary

# Fixed actual ample perturbations for all-point fiber descent

New, unreviewed mathematical reconstruction for original P16.1. It does not close an original problem. The actual round86 PASS grants the unchanged root89/90 deductions only in their precise conditional partial scope. Author84, review85 and the new review87 retain immutable independent inputs; this draft is not feedback to them.

## 1. Statement and fixed-bundle reduction

Let \(k\) be algebraically closed, trivially valued, and of characteristic zero. Let \(\pi:Y\to X\) be a projective morphism of integral projective varieties with geometrically connected fibers, let \(L\) be an actual ample rational line bundle on \(X\), and set \(M=\pi^*L\), \(\theta=c_1(M)\). The proposed conclusion is that every \(\varphi\in\operatorname{PSH}(Y,\theta)\) is constant on every fiber of \(\pi^{\mathrm{an}}\), on ALL analytic points and allowing value \(-\infty\). No countability is needed for this proposed fiber statement. A resolution over a geometrically unibranch target is the application.

Choose ONE actual very ample line bundle \(A\) on \(Y\). By BJ4.15(ii), there is a decreasing net of finite continuous rational PL functions \(\varphi_i\in\mathcal H(L_i)\), with actual ample rational \(L_i\), \(c_1(L_i)\to\theta\), and pointwise limit \(\varphi\). For each positive rational \(\delta\), sufficiently large \(i\) satisfies
\[
 \theta+\delta c_1(A)-c_1(L_i)\in\operatorname{Amp}(Y).
\]
Use only these VALID pairs \((i,\delta)\), ordered by increasing \(i\) and decreasing \(\delta\). They form a directed set: choose a smaller rational \(\delta\) than two given parameters, then an index above their indices and the ample-cone tail for this parameter. The scalar functions \(\varphi_i\) still decrease to \(\varphi\). Adding the genuine zero potential in the ample difference class shows
\[
 \varphi_i\in\operatorname{PSH}\bigl(Y,c_1(M+\delta A)\bigr).
\]
This is class addition preserving the ACTUAL scalar function. It does not equate two unrelated line-bundle metrics.

For a fixed pair, BJ3.10 and the literal same-bundle inclusion BJ3.9 give uniform approximation of \(\varphi_i\) by \(\mathcal H_{\mathrm{dom}}(M+\delta A)\subset\mathcal H(M+\delta A)\). The safe rational interpolation in the actual round86 report applies. Thus the metric with scalar potential \(\varphi_i\) has genuine uniform fixed-bundle FS approximation on the actual ample rational bundle \(M+\delta A\), without any EP assumption. Pull each finite section formula before taking its uniform limit. No decreasing fixed-nef-bundle approximation, abstract higher-dimensional current pullback, or unknown affine theorem over an extended field is being asserted.

## 2. A norm-preserving field with rational weights in its value group

Fix \(s\in X^{\mathrm{an}}\) and a complete valued extension \(F\) of \(\mathcal H(s)\). To use proper smooth algebraic curves through rational lifts, extend \(F\) by an independent Gauss variable \(\tau\) with \(|\tau|=e^{-1}\), complete, take an algebraic closure with an extended absolute value, and complete again. Denote the resulting complete algebraically closed nontrivially valued field by \(K\).

Adjoin \(\tau\) EVEN IF \(F\) already has a nontrivial absolute value. This preserves every original norm while ensuring \(\mathbb Q\subset\log|K^\times|\). Consequently all rational weights in the FS approximations are realized by norms of scalars after base change. No renormalization of \(\mathcal H(s)\) or of the tested analytic point occurs. The original trivially valued \(k\) remains embedded isometrically.

Let \(f:C\to Y_K\) be any nonconstant algebraic morphism from a smooth connected proper \(K\)-curve whose composite with \(\pi_K\) is the \(K\)-point \(s_K\). For a constant morphism the desired assertion is immediate. The analytic scalar pullbacks \(v_{i,\delta}=\varphi_i\circ f^{\mathrm{an}}\) are finite continuous, decrease, and have limit \(v=\varphi\circ f^{\mathrm{an}}\).

## 3. One graph model and one positive finite background measure

Take the product models \(\mathcal Y=Y\times_kK^\circ\), \(\mathcal X=X\times_kK^\circ\), with the pulled actual models \(\mathcal M=\pi^*L\) and \(\mathcal A=A\). BE5.13 gives ONE projective graph model \(\mathcal C\) of \(C\) with an extension of \(f\) to \(\mathcal Y\). Its flat finite-type model is finitely presented by BE4.5; \(K^\circ\) is not assumed Noetherian. It is enough to use the graph construction, without its optional flattening clause.

Properness extends \(s_K:\operatorname{Spec}K\to\mathcal X\) to a section over \(K^\circ\). The composite \(\mathcal C\to\mathcal X\) agrees generically with that section composed with \(\mathcal C\to\operatorname{Spec}K^\circ\). The two maps agree everywhere: the equalizer is closed by separatedness and contains the schematically dense generic fiber of the flat model. Hence \(f^*\mathcal M\) on \(\mathcal C\) is literally pulled from a line on \(\operatorname{Spec}K^\circ\). That line is free. Its reference metric on \(C\) is constant in a fixed frame and has zero curvature.

The model \(f^*\mathcal A\) is nef on every irreducible special-fiber curve. Indeed it is pulled from the original ample \(A\) along that component's morphism into a residue-field base change of \(Y\); its degree is nonnegative, including zero for constant images. BE4.20 permits a reduced-special-fiber dominating model over this algebraically closed nontrivially valued \(K\), and pullback retains the metric and nefness. BE8.11 then supplies ONE positive finitely supported curve curvature measure
\[
 \sigma_A=\sum_{\zeta\in\Sigma}a_\zeta\delta_\zeta,\qquad
 a_\zeta\ge0,\qquad \sigma_A(C)=\deg_C(f^*A).
\]
The support consists of the finitely many type-II Shilov points of the model. Reduced-model formula (8.3) is applied with its exact hypotheses; any use on an unreduced model must retain its fundamental cycle and multiplicities. No coefficient is discarded. The background for the actual reference \(f^*(M+\delta A)\) is exactly \(\delta\sigma_A\).

For each valid pair, pull the actual fixed-bundle FS formulas to \(C\). Basepoint freeness persists. BE7.14 and BE8.4 give the positive finite curvature \(\mu_{i,\delta}\) of the resulting continuous metric on \(f^*(M+\delta A)\), with mass \(\delta\deg_C(f^*A)\). Linearity for differences of the actual continuous metrics gives
\[
 dd^c v_{i,\delta}=\mu_{i,\delta}-\delta\sigma_A.
 \tag{1}
\]
Here the canonical \(M\)-reference is flat and the \(A\)-reference is FIXED. Wanner3.27–3.28 identify model-function CLD measures with Thuillier's curve Laplacian on semistable refinements, and the continuous uniform approximation determines the same current difference. The model-to-semistable-refinement and model-to-piecewise-linear dictionaries used in those published theorems remain primary curve background with their exact hypotheses. Independent verification of this dictionary and (1), rather than a degree-only claim, is a required part of the proposed proof.

## 4. Vanishing Green corrections and comparison of the original limit

Let \(V\subset C^{\mathrm{an}}\) be a connected strict affinoid domain with ordinary interior, with its finite boundary avoiding \(\Sigma\). Such domains can be chosen locally around any point of the smooth curve over nontrivial algebraically closed \(K\), moving their boundary to avoid finitely many specified type-II points. For each \(\zeta\in\Sigma\cap(V\setminus\partial V)\), Thuillier3.3.7(ii) gives a nonnegative continuous lisse Green function \(g_\zeta^V\), zero on \(\partial V\), whose interior Laplacian is \(-\delta_\zeta\). Set
\[
 p_\delta=-\delta\sum_{\zeta\in\Sigma\cap V}a_\zeta g_\zeta^V.
\]
The finite sum gives \(\|p_\delta\|_V\le B_V\delta\), \(p_\delta|_{\partial V}=0\), and, by (1),
\[
 dd^c(v_{i,\delta}+p_\delta)=\mu_{i,\delta}\ge0
 \quad\text{on }V\setminus\partial V.
\]
The corrected function is continuous. Wanner4.7 identifies continuous CLD-psh functions with Thuillier-subharmonic functions on that interior. Positivity of the lisse correction current uses the same signed model/slope dictionary. A compact boundary comparison follows from the curve maximum principle, as in Thuillier3.1.11–3.1.12.

The corrected functions need NOT be decreasing. Compare the ORIGINAL decreasing net directly. Suppose \(H\in H(V)\) and \(v\le H\) on \(\partial V\). For \(\varepsilon>0\), the compact closed sets
\[
 \{x\in\partial V:v_{i,\delta}(x)\ge H(x)+\varepsilon\}
\]
decrease with empty intersection. Directedness and compactness imply that eventually all are empty. On that tail the corrected function is at most \(H+\varepsilon\) on the boundary, hence throughout \(V\). Thus
\[
 v_{i,\delta}\le H+\varepsilon+B_V\delta\quad\text{on }V.
\]
Taking the net limit, for which \(\delta\to0\), and then \(\varepsilon\downarrow0\), gives \(v\le H\) throughout \(V\). This proof is valid at \(-\infty\) and never uses a nonexistent monotone corrected net.

The limit \(v\) is usc as the infimum of continuous functions. Its local harmonic comparison shows it is subharmonic or identically \(-\infty\) on a connected component, with the usual curve convention. To avoid any component-identically-infinite issue in the final application, apply the entire argument instead to the bounded floors
\[
 \varphi^{(m)}=\max\{\varphi,-m\}\in\operatorname{PSH}(Y,\theta).
\]
Zero is genuinely \(\theta\)-psh since \(M\) is semiample and nef, and maxima are allowed by BJ4.3. Each floor is bounded above by the global bound for \(\varphi\) and below by \(-m\). Its pullback to the proper connected \(C^{\mathrm{an}}\) is bounded usc subharmonic, attains a maximum, and is constant by Thuillier3.1.11. Letting \(m\to\infty\) proves that \(\varphi\circ f\) is constant, including the possible constant \(-\infty\).

## 5. Every analytic point, rather than only dense rational lifts

The analytic fiber over \(s\) is the analytification of the proper projective algebraic fiber \(Y_s\) over \(\mathcal H(s)\). Fix ONE closed point \(z\) of \(Y_s\). Its residue field is finite over \(\mathcal H(s)\), with the uniquely extended complete-field absolute value. For ANY analytic \(y\in Y_s^{\mathrm{an}}\), begin the preceding construction with \(F=\mathcal H(y)\). A compatible embedding of \(\kappa(z)\) into the resulting algebraically closed \(K\) is norm preserving. Both the evaluation giving \(y\) and this embedding giving \(z\) therefore define actual \(K\)-rational points on the geometric fiber, and their scalar pullback values are the ORIGINAL \(\varphi(y)\) and \(\varphi(z)\).

The geometric fiber is connected; reduction retains its topology. Its finite irreducible-component adjacency graph is connected. Choose closed \(K\)-points in the relevant component intersections. Within an integral projective component of positive dimension, any two closed points can be joined by a finite chain of morphisms from smooth connected proper curves. One construction resolves the component, lifts the two points by proper surjectivity, blows up the two distinct smooth lifts, takes sufficiently positive very ample complete intersections through their exceptional loci by Bertini, and maps the resulting smooth proper curves back. In dimension one use the normalization; zero-dimensional components contribute only their point. The precise Stacks/Bertini construction recorded in root81 must be checked as a scheme-theoretic curve-MORPHISM chain; an embedded smooth curve through a singular point is not required.

Constancy of every floor on those curves implies \(\varphi^{(m)}(y)=\varphi^{(m)}(z)\) for all \(m\), and hence \(\varphi(y)=\varphi(z)\). This compares each analytic point to the SAME closed point, even though its auxiliary field \(K\) depends on \(y\). No density argument for usc functions is used.

Consequently \(\varphi=\pi^*\psi\) as actual scalar functions for a unique \(\psi\) on \(X^{\mathrm{an}}\). Proper analytic surjectivity and compactness give usc descent: for every finite \(a\), \(\{\psi\ge a\}=\pi(\{\varphi\ge a\})\) is closed. The function is globally bounded above. In the birational case, the generic trivial valuation lifts to the generic trivial valuation, so \(\psi\) is finite there.

## 6. Proposed join to countable singular EP, retaining unproved inputs

For a resolution \(\pi:Y\to X\) of a geometrically unibranch projective characteristic-zero target, Stacks0GIQ and 0AY8 give geometrically connected fibers under their exact normalization/Stein hypotheses, as recorded in root81. The original possibly nonnormal \(X\) is retained. No normalization inverse theorem requiring target EP is used at this stage.

Suppose \(k\) is countable. The accepted actual-reference conversion in root90/round86 supplies a local decreasing rational affine-FS net for \(\pi^*\psi+h_{\pi^*L}\). The root91 countable extraction supplies a sequence on the same local neighborhood, with genuine unit-log contacts. The original witness is ONE fixed resolution \(\pi\), and the frame is the pullback of the original \(L\)-frame. Thus the proposed scalar descent has the precise weak local contact input needed by the conditional author83 global first-membership chain.

IF the unchanged author83 conditional global C1 chain is independently accepted and the root91 geometrical construction supplies its GEO antecedents, it follows that the ORIGINAL \(\psi\) belongs to \(\operatorname{PSH}(X,L)\). This is first membership before any target EP assertion. Pullback already preserves genuine target PSH; scalar fiber constancy and first membership make pullback onto. Birational identification of divisorial valuations then makes the onto map a homeomorphism in the divisorial pointwise topologies. The generic trivial point, hence the sup normalization, is also preserved.

Smooth nef source compactness (BJ5.20–5.21) now transports to normalized target PSH. BJ5.11 supplies countable target EP for EVERY actual ample rational \(L\). This would discharge E in the independently accepted round86 cardinality implication. That implication would then give arbitrary-cardinality target EP, followed by the accepted root89 actual raw equation, uniqueness, and after-EP normalization transport. The logic is ordered to avoid assuming target EP to prove the first onto pullback.

These implications are proposed joins, not already accepted conclusions. This draft still needs independent verification of the fixed-model curve Laplacian identity, Green/current comparison, all-point curve chains and resolution fibers, and their exact compatibility with the countable first-membership chain. Pending native author/review results must be read in their actual canonical scope before any join or original closure.

## 7. Exact primary reading and publication limits

The new literal units read use UTF8 byte decoding and one-based inclusive LF coordinates: BE1805.01016v3 LF1514–1590,1970–1995,2765–2808; Thuillier tel-00010990v1 LF3366–3445,4800–4902; Wanner1801.04713v3 LF735–821. The current-source SHA256 and exact literal-unit hashes will be recorded separately before freezing. Existing frozen root88 units include the full pertinent Green/max-principle bodies, BE graph/model-reduction material, Wanner4.6 and the complete pertinent 4.7 proof, and BJ smooth-nef EP. Only the listed pertinent source bodies are claimed read, not whole source files or every recursive model/semistable/Bertini proof.

Primary URLs: https://arxiv.org/pdf/1805.01016v3 ; https://theses.hal.science/tel-00010990v1/document ; https://arxiv.org/pdf/1801.04713v3 ; https://arxiv.org/pdf/1801.08229v4 . The proof uses published primary curve and resolution background with stated hypotheses; documentary provenance alone supplies no mathematical acceptance.



END MATHEMATICAL DATA



BEGIN MATHEMATICAL DATA: Original context 15: Exact body accepted ONLY within actual88 scope; historical status statements are documentary

# Curve current identity for the fixed-reference fiber draft

This is a new unreviewed mathematical addendum to the unchanged, checkpoint91-frozen root92 draft. It is not a grant, feedback to active native runs, or an original solution. It makes the proposed curve calculation more explicit and removes an unnecessary affinoid-boundary restriction.

## 1. Finite stages on the same actual bundle

Retain the field \(K\), the smooth connected proper curve \(C\), the morphism \(f\), the graph model, and the fixed actual references from root92. In particular \(K\) is complete algebraically closed nontrivially valued, its value group contains \(\mathbb Q\), the \(M\)-reference is flat in one fixed frame, and the \(A\)-reference has the fixed positive finite measure \(\sigma_A\). Fix one valid pair \((i,\delta)\) and write \(B=f^*(M+\delta A)\).

The uniform same-actual-bundle FS approximation from the accepted round86 local-reference argument, used here globally for the finite continuous PL \(\varphi_i\), gives rational FS metrics \(h_j\) on \(B\). They converge uniformly to the metric whose scalar difference from the fixed \(B\)-reference is \(v_{i,\delta}\). Every rational FS weight is in \(\log|K^\times|\). Thus \(h_j\) is a PURE FS metric on the actual \(B\), induced by a semiample rational model by BE5.14. The fixed reference is induced by the actual model \(f^*(\mathcal M+\delta\mathcal A)\). After clearing tensor powers and taking a common dominating graph model, their DIFFERENCE \(w_j\) is a rational model metric on the trivial bundle, with its actual generic-fiber identification. The reference has curvature \(\delta\sigma_A\), so the model difference has the signed curvature
\[
 \operatorname{curv}(w_j)=\mu_j-\delta\sigma_A.
\]
Here \(\mu_j\) is the positive curvature of \(h_j\), including the fundamental cycle, of mass \(\deg B=\delta\deg(f^*A)\). This is an additive actual-model identity, rather than comparison of equal degrees alone.

Algebraic model metrics are formal by completion. GK1406.7637v3, 8.8–8.11, supplies the precise formal/piecewise-linear dictionary, tensor/dual/pullback operations, and G-cover criterion over an algebraically closed complete NONTRIVIAL field. Its 8.13 statement is also read, but the nontrivial formal-to-algebraic converse is not needed for this direction. On a smooth proper curve the semistable formal model dictionary in Wanner3.26–3.28 puts a rational trivial model metric into a skeleton description and identifies its CLD measure with its Thuillier Laplacian. This uses the published curve semistable-model background with its stated field hypotheses; it does not assume higher-dimensional semistable reduction over an arbitrary valuation ring. The curve model refinement needed to preserve a specified formal metric remains part of the exact primary dictionary to be verified independently.

Consequently, for every finite stage,
\[
 d'd''[w_j]=[\mu_j-\delta\sigma_A].
 \tag{2}
\]
For a compactly supported smooth test \(q\), uniform convergence \(w_j\to v_{i,\delta}\) gives convergence of the left side: \(d'd''q\) is a fixed compactly supported signed Radon measure on the curve, and the integral difference is bounded by \(\|w_j-v_{i,\delta}\|_\infty\) times its total variation. BE8.4 gives weak convergence \(\mu_j\to\mu_{i,\delta}\) on this SAME actual generic-fiber bundle. Passing to the limit in (2) gives the precise current form of root92's identity:
\[
 d'd''[v_{i,\delta}]=[\mu_{i,\delta}-\delta\sigma_A].
 \tag{3}
\]
Both limits are uniform/weak limits of genuine fixed-bundle metrics. No pullback of an unspecified higher-dimensional current or preexisting singular EP is used.

## 2. Exact lisse correction current, including point types

Wanner4.2 proves that the CLD current and Thuillier Laplacian of a lisse function agree locally at every type-II point. Its proof constructs local signed model functions with integral slopes on rational-length edges, expresses the lisse function as a real linear combination plus a constant, and applies 3.27–3.28. The rational lengths can be chosen here because the auxiliary Gauss variable ensured \(\mathbb Q\subset\log|K^\times|\); the original absolute values remain unchanged.

For the Green functions used here, the Thuillier Laplacian on the affinoid interior is supported at the specified type-II center. At a type-I or IV point, a lisse function is locally constant, as in Wanner4.3. At a type-III point away from the discrete Laplacian support, its skeletal restriction is locally affine on the corresponding annulus. In an annulus coordinate it is \(a\log|T|+b\), and both currents vanish by Poincare–Lelong for the invertible analytic \(T\). Thus the type-II equality and these other point-type calculations give
\[
 d'd''[g_\zeta^V]=[-\delta_\zeta]
 \quad\text{on the interior of }V.
\]
This supplies the signed equality for the Green correction itself; positivity of a current of \(-g_\zeta^V\) alone would not identify its exact measure.

By linearity and (3), the finite lisse correction in root92 therefore satisfies
\[
 d'd''[v_{i,\delta}+p_\delta]=[\mu_{i,\delta}]\ge0
\]
on the interior. The function is continuous. Wanner4.7 then supplies genuine Thuillier subharmonicity there. The compact boundary maximum principle and the original-net comparison in root92 apply verbatim. In particular monotonicity of the corrected functions is never required.

## 3. No need to move the affinoid boundary

The demand in root92 that \(\partial V\) avoid the finite set \(\Sigma\) is UNNECESSARY. Use ANY connected strict affinoid \(V\) with interior. Define \(p_\delta\) using only \(\zeta\in\Sigma\cap\operatorname{Int}(V)\). Atoms of \(\sigma_A\) on \(\partial V\) are absent from its restriction to the interior current in (3), so they require no correction there. Every interior Green function still vanishes on all of \(\partial V\), and the same finite uniform estimate holds. Hence (3), positivity on the interior, compact boundary comparison, and the limit \(v\le H\) hold for every such \(V\).

For the bounded floors of root92 this verifies exactly Wanner2.4's harmonic-comparison definition on every connected strict affinoid. For a disconnected strict affinoid apply the same comparison on its finitely many connected components. The curve is strict and good over this \(K\); local strict affinoid neighborhoods exist. Thus no separate boundary-avoidance or point-density assertion is needed to infer subharmonicity of a bounded floor.

The subsequent maximum principle on the proper connected curve, comparison of each analytic fiber point to one fixed closed point by curve morphism chains, and the countable first-membership join retain root92's exact dependencies. This addendum does not independently verify or grant those later steps.

## 4. Primary bodies read and exact scope

New bodies read by UTF8 byte decode with one-based inclusive LF coordinates: Wanner1801.04713v3 LF232–312 and 822–990, including the exact harmonic/lisse/Green definitions and complete pertinent 4.2–4.5 proof bodies; GK1406.7637v3 LF353–385 and 3380–3595, including the standing field/variety hypotheses, 8.4 full G-cover proof, and 8.11–8.13 statements and pertinent proofs. The fixed GK PDF is https://arxiv.org/pdf/1406.7637v3, verified as the latest listed v3 (13 September 2016) at its live abstract page, not assigned an imaginary edition. PDF SHA256 62c7e4dfebab75d725f529c6ef78c300856c63fd050a9399e8a86879e569315d; layout text SHA256 4336903644edf53838f829cf22a3326257f909adfae1f906738f9f8534d1826b.

Live Stacks0AY8 rendered24–39 and 0GIQ rendered22–24 were read in full: the former requires the NORMAL base in all six hypotheses and gives geometric connectedness; the latter supplies a universal-homeomorphism normalization of an irreducible geometrically unibranch target. Thus in root92's resolution application, factor the smooth source through the actual normalization, apply 0AY8 to that normal base, then use the universal homeomorphism to identify every geometric target fiber topologically. This retains nonnormal \(X\) and every analytic fiber; it does not apply 0AY8 directly to a nonnormal base. Properness over the normal base follows from the graph/properness argument, with the same generic function field and all source generic points dominating it.

The new live observations are saved in continuation93-live-curve-model-and-fiber-primary-observation.json. No whole GK/Wanner source file or every recursive Raynaud/formal-GAGA/semistable proof is claimed read. The fresh mathematical uses and the complete fiber/first-membership join remain unreviewed.



END MATHEMATICAL DATA



BEGIN MATHEMATICAL DATA: Original context 16: TASK-GRANTED actual89 precise PARTIAL review only

{
  "verdict": "PASS",
  "report": "PASS for the repaired retained partial scope: the original-witness trace, controlled affine tools, conditional countable Runge–Hartogs chain, and original projective ample-reference membership consequence. This does not establish original P16.1, resolved-nef fiber descent, singular EP, or arbitrary-cardinality existence. The old actual85 report supplies no mathematical grant.\n\nI used round77/actual80 and root91/actual87 only within their expressly granted scopes. In particular, I checked the GEO applications rather than accepting the label. Restriction of the original proper birational witness to each smooth affine open remains proper and birational. The granted geometric construction supplies an actual smooth projective domination mapping to that restriction, including its exceptional points. Products use P×A¹ and its restrictions. The auxiliary ample boundary reference is built from the actual original generators; its growth comparison changes the reference used by the gate, not the scalar input. Its pullback uses the actual bundle and boundary-section frame. The projective consequence subsequently returns to ORIGINAL X and L through G, after affine membership has been established. Countable extraction concerns an already available decreasing continuous net; it establishes no descent or first membership.\n\nFor n1, the dense principal good open can exclude both the finite map’s non-étale locus and the finite image of the original witness’s non-isomorphism locus. Monic equations give the stated seminorm bounds and rational growth comparisons. The smooth gate, norm identity T1, and smooth principal-open removal construct the original-base function v before assigning any removed-fiber value. No nonflat fiber length enters this construction.\n\nThe slicing argument checks every minimal reduced component. Geometric integrality survives extension to F=H(s). The height bound and field dimension formula give dimension at least one; finiteness over the parameter curve gives dimension at most one and excludes vertical components. Normalization of the entire reduction is finite, its components are smooth over the perfect field F, and their finite nonconstant maps to T are flat. Their total generic rank is d because normalization changes nothing over the entire good étale inverse image. The n=1 and n=0 cases have the stated interpretations.\n\nEvery normalized component lifts to the SAME P_F using relative properness over Y_F, its closed-point DVRs, spreading, and separated gluing. Absolute properness over F is unnecessary. Original contact approximants are pulled back before taking limits. A supporting harmonic function and the harmonic maximum principle give the harmonic-test condition for each continuous approximant. Decreasing comparison follows by applying compact nested-superlevel emptiness on the finite affinoid boundary with an arbitrarily small positive error. The limit is subharmonic on a component where it is not identically −∞. The independent slice/radial calculation also prevents a finite weak value from being confined to a removed algebraic set, justifying the generic-finiteness restrictions needed by the gates.\n\nThe analytic-coordinate proof uses a genuine Jacobian contraction on small polydiscs, with uniqueness after every complete residue extension; it does not substitute a formal completed local ring for an analytic neighborhood. After the stated nontrivial extension and completed algebraic closure, the applied curve results have their required field hypotheses. Smooth projective curve compactification supplies the proper-curve setting of the accessible primary statements. At a finite center, comparison with the finite Gauss-boundary constant and usc prove the strict-disc radial limit. Boundary finiteness can also be checked directly here: a boundary value −∞ would permit comparison with every negative constant and contradict the finite center value. At a −∞ center, usc alone proves the same radial limit.\n\nResidue characteristic zero permits the convergent unit root and the exact local expression t=bz^e. After scaling strict radii, Z^e−T is irreducible by Eisenstein, so the exhibited point has completed residue degree e and is unique in that disc. The fixed compact finite inverse image, with ALL center neighborhoods removed, excludes every additional sufficiently small Gauss-fiber point. Before splitting centers, flat-curve specialization gives e_x[κ(x):F]. Equality of polynomial-law coefficients on the dense good parameter open identifies their grouped characters with the ORIGINAL norm law at zero. Complete-extension compatibility then recovers the original m_y. Positive finite summation handles a −∞ summand because all other terms remain bounded above. Thus T2 holds at every original analytic point, including nonflat and exceptional fibers.\n\nFor n2’s G, membership is supplied at the outset. Including unpowered original generators makes the projective affine chart literally Spec R. The actual canonical potential is a_i−cg₀, with boundary C_i+cp; using a_i−cg would lose the reference. Compact superlevel emptiness supplies the indices without Dini convergence to a discontinuous limit. The strict whole collars and the separate old-domain, new-annulus, and exterior inequalities give a decreasing family in ONE actual bundle. Genuine decreasing closure establishes membership before regularization. The alternative uniform same-bundle approximation with summable shifts also directly constructs the required decreasing sequence. Section localization and dominated padding return literal original-ring functions and retain positive generator slopes.\n\nThe denominator counterexample is correct, and its printed conclusion is not used. The replacement checks every height-one valuation of the finite normalization. It proves h=b^Nf^(Nc/q) integral, not necessarily original-ring regular. Finiteness of R[h] supplies ONE multiplier f^M clearing EVERY h^j. Testing those original polynomials in the hull and taking j-th roots proves the stated branch error, including a zero supremum. Compact decreasing suprema converge to the supremum of the usc limit, also when that supremum is −∞. Taking the sequence limit and then c↓0 proves H in the ordinary original source ring.\n\nThe entropy support argument includes every infinite-coordinate face. Positive finite-coordinate probabilities and p₀ make the recession gap strictly positive in every nonzero direction. Omitted coordinates are handled separately by their positive exponential contribution when they leave an infinity neighborhood. Face-respecting rational grids and rational height intervals give global convex-roof and conjugate errors, not merely approximation on bounded Euclidean boxes. The positive countable tail bound makes the displayed upper partial sums decrease. Rational coefficient intervals correctly choose the upper endpoint for positive logarithms and the lower endpoint for negative ones, retaining −∞ at zeros. Decreasing floor/generator padding tends to −∞ at each fixed point and therefore changes no limit. Support replacement is established through positive expressions, without subtracting psh functions.\n\nThe original polynomial hull equals the AFS hull, and generator bounds make it compact. Finite strict separations provide the thick polynomial neighborhoods used subsequently. In the repaired Rossi assertion, z∈V is essential and is now established: the glued function is positive at z and zero on L. The compact bad boundary portion is disjoint from hull(L), allowing a reference that vanishes near that hull and wins on the entire boundary collar. Same-bundle approximation converts the separator back to the original ring. Both applications satisfy the repaired antecedent: the off-bad-set proof chooses V around its finite maximum y, and the split proof chooses V around x. The off-bad-set proof uses ORIGINAL u’s genuine local regularizability, controlled compact closure in a principal chart, and the error cδ from the support replacement. It does not infer regularizability by subtracting cρ.\n\nFor n3, the singleton base hull lies in the closed-immersion image. Properness controls its ENTIRE inverse image and the two compact pieces. The indicator trace is only locally constant; the proof correctly retains ONE shrunken neighborhood N on which its raw positive integer sum is γ. Central analytic injectivity gives the unique W₁ point. The γ=1 case needs no division. For γ>1, usc and properness control all other W₁ fiber values in that same N. The boundary estimates are uniform: on Z they are at most −γ min(δ,cδ′); off Z they are at most −m_yδ+(γ−m_y)δ/[2(γ−1)]≤−δ/2. For γ=1 the latter value is −δ. The reference wins on the whole outer collar, and n1 applies to the modified function on the same original witness. These bounds contradict the original-ring Rossi hull inequality.\n\nRunge on the PRODUCT is proved before Hartogs is invoked. H=log|w|+u∘p uses the SAME product witness, decreasing logarithmic floors, and positive products of original approximants. The countable compact exhaustion gives genuinely nested strict polynomial opens with controlled closures. Their zero-section domains Ω_r retain the strict constant-coefficient conditions. Gauss norms at EVERY positive real radius prove D exactly, including equality at the excluded endpoint, zero coefficients, and infinite radius. Compact closed fiber discs establish convergence of the exhaustion radii to the domain radius. Original coefficients and reference-winning gluing establish membership before same-bundle regularization and generator padding.\n\nThe descending-Z proof checks every component: closed-immersion images are incomparable, finiteness forces each original component to remain a component of the full inverse image, and complementary closure omits its generic point. Localization is saturated and uses exactly U=π⁻¹(S′). Jacobson coverage supplies the algebraic good cover at intermediate stages as well as at the end. The finite-projection proof does not apply the integral-variety statement blindly to the reduced union T. Its secant exclusion, tangent injectivity, single fiber, and two Nakayama arguments establish the required local isomorphism for that union. Repeated projections preserve this property; the final saturated U=r⁻¹(S) avoids the boundary and lies in ORIGINAL Y. Reduced singular strata drop dimension componentwise. At the final empty stratum the proof performs the additional GLOBAL empty-Z product/Hartogs argument, rather than stopping at local membership.\n\nThe projective consequence is correct for countable k, ORIGINAL reduced irreducible geometrically unibranch projective X, actual ample rational L, and the stipulated original affine contact witnesses. The argument in fact does not use unibranchness once those contacts are supplied. Very ample coordinates provide the actual chart exhaustion ρ_i and canonical reference. Affine regularization precedes G on ORIGINAL X. For every rational c>1, each extension φ−(c−1)ρ_i, with value −∞ outside its chart, has genuine cL-membership. At every analytic point a maximal homogeneous coordinate gives ρ_i=0, so their finite maximum is exactly φ, including −∞ values. Consequently φ∈PSH(cL) for every c>1. Varying-class decreasing closure applies to the CONSTANT family φ as c↓1. It need not be applied to the individual chart extensions, which increase.\n\nFor n4, the raw convention is consistent: shifting the variational potential by a changes the functional by a(V−ν(X)), so mass V is necessary. The dimension-zero convention is literal. The opened [BJ primary text](https://arxiv.org/pdf/1801.08229v4) confirms relative closure inside the prescribed generic fiber, the fundamental-cycle raw operator, intrinsic dual energy, general-scope uniqueness/domination, and the attained-maximizer proof under EP. Its Lemma 5.13 requires approaching EP on the TARGET. The [Wu v1 proof](https://arxiv.org/pdf/2609.27610v1) explicitly invokes both Proposition 2.24 and Theorem 6.5. Neither invocation is supplied by the new partial result alone.\n\nThus resolved-nef all-point fiber constancy and scalar descent, the requisite contacts for a descended potential, singular target EP, arbitrary-cardinality obstacle/competitor descent, and normalization/E¹/MA compatibility through unbounded limits remain unresolved gates. GEO remains an explicit antecedent of the retained statements; for the actual algebraic witness applications audited here, the granted root91 construction supplies it. Accordingly n4’s wording ‘not proved here’ must not be read as an additional unverified geometric premise for those already granted applications. This is a scope clarification, not a new descent theorem.\n\nThe binding slope clarification is valid: multiplication retains scaled positive slopes; lowering a constant does not restore unit slope. Real normalizations are implemented by decreasing rational shifts applied equally to weights and their supports, preserving contact equality and −∞ values. Applying the curve statements after the explicitly specified field extension, and using the constant family in projective varying-class closure, are harmless explanatory clarifications. No substantial repair beyond the retained Rossi antecedent is needed. Hashes, compilation, finite diagnostics, and previous verdicts played no role in this mathematical verdict.",
  "passages": [
    {
      "id": "f12124b7-3be3-4de2-bcb8-ab7a4fcf6f2a/0",
      "statement": "For a scheme locally of finite type over a field, normalization is finite and dominant, factors through reduction, and has normal integral components. For a reduced finite-type scheme it is birational.",
      "url": "https://stacks.math.columbia.edu/tag/0BXQ",
      "quote": "$\\nu $ is finite, dominant",
      "premise": 0
    },
    {
      "id": "f12124b7-3be3-4de2-bcb8-ab7a4fcf6f2a/1",
      "statement": "For a scheme locally of finite type over a field, normalization is finite and dominant, factors through reduction, and has normal integral components. For a reduced finite-type scheme it is birational.",
      "url": "https://stacks.math.columbia.edu/tag/0BXQ",
      "quote": "if $X$ is a reduced algebraic scheme, then $\\nu $ is birational",
      "premise": 0
    },
    {
      "id": "f12124b7-3be3-4de2-bcb8-ab7a4fcf6f2a/2",
      "statement": "In a Noetherian ring, every prime minimal over an ideal generated by r elements has height at most r.",
      "url": "https://stacks.math.columbia.edu/tag/0BBZ",
      "quote": "then the height of $\\mathfrak p$ is $\\leq r$.",
      "premise": 1
    },
    {
      "id": "f12124b7-3be3-4de2-bcb8-ab7a4fcf6f2a/3",
      "statement": "Every field is universally catenary. For a finite-type domain R over a field F and every prime p of R, height(p)+trdeg_F κ(p)=trdeg_F Frac(R), and dim R=trdeg_F Frac(R).",
      "url": "https://stacks.math.columbia.edu/tag/02IJ",
      "quote": "with equality if $R$ is universally catenary.",
      "premise": 2
    },
    {
      "id": "f12124b7-3be3-4de2-bcb8-ab7a4fcf6f2a/4",
      "statement": "Every field is universally catenary. For a finite-type domain R over a field F and every prime p of R, height(p)+trdeg_F κ(p)=trdeg_F Frac(R), and dim R=trdeg_F Frac(R).",
      "url": "https://stacks.math.columbia.edu/tag/02JB",
      "quote": "Any scheme locally of finite type over a field.",
      "premise": 2
    },
    {
      "id": "f12124b7-3be3-4de2-bcb8-ab7a4fcf6f2a/5",
      "statement": "Every field is universally catenary. For a finite-type domain R over a field F and every prime p of R, height(p)+trdeg_F κ(p)=trdeg_F Frac(R), and dim R=trdeg_F Frac(R).",
      "url": "https://stacks.math.columbia.edu/tag/0A21",
      "quote": "$\\dim (X) = \\text{trdeg}_ k(\\kappa (x))$.",
      "premise": 2
    },
    {
      "id": "f12124b7-3be3-4de2-bcb8-ab7a4fcf6f2a/6",
      "statement": "An integral finite-type scheme over an algebraically closed field remains integral after every field extension.",
      "url": "https://stacks.math.columbia.edu/tag/038H",
      "quote": "induces a bijection of irreducible components.",
      "premise": 3
    },
    {
      "id": "f12124b7-3be3-4de2-bcb8-ab7a4fcf6f2a/7",
      "statement": "An integral finite-type scheme over an algebraically closed field remains integral after every field extension.",
      "url": "https://stacks.math.columbia.edu/tag/020I",
      "quote": "If $X$ is reduced, then $X$ is geometrically reduced over $k$.",
      "premise": 3
    },
    {
      "id": "f12124b7-3be3-4de2-bcb8-ab7a4fcf6f2a/8",
      "statement": "A normal integral finite-type curve over a perfect field is smooth, and its local rings at closed points are discrete valuation rings.",
      "url": "https://stacks.math.columbia.edu/tag/0B8Y",
      "quote": "$\\mathcal{O}_{X, x}$ is a discrete valuation ring",
      "premise": 4
    },
    {
      "id": "f12124b7-3be3-4de2-bcb8-ab7a4fcf6f2a/9",
      "statement": "A normal integral finite-type curve over a perfect field is smooth, and its local rings at closed points are discrete valuation rings.",
      "url": "https://stacks.math.columbia.edu/tag/0B8Y",
      "quote": "If $k$ is perfect",
      "premise": 4
    },
    {
      "id": "f12124b7-3be3-4de2-bcb8-ab7a4fcf6f2a/10",
      "statement": "A nonconstant morphism of integral curves over a field is flat if its target is normal.",
      "url": "https://stacks.math.columbia.edu/tag/0BXX",
      "quote": "If $Y$ is normal, then $f$ is flat.",
      "premise": 5
    },
    {
      "id": "f12124b7-3be3-4de2-bcb8-ab7a4fcf6f2a/11",
      "statement": "Let X be a Noetherian S-scheme, U⊂X open, x∈closure(U), and O_{X,x} a valuation ring. If Z→S is proper, every S-morphism U→Z extends to an S-morphism on an open subset containing U and x.",
      "url": "https://stacks.math.columbia.edu/tag/0BX4",
      "quote": "$Y \\to S$ is proper",
      "premise": 6
    },
    {
      "id": "f12124b7-3be3-4de2-bcb8-ab7a4fcf6f2a/12",
      "statement": "Let X be a Noetherian S-scheme, U⊂X open, x∈closure(U), and O_{X,x} a valuation ring. If Z→S is proper, every S-morphism U→Z extends to an S-morphism on an open subset containing U and x.",
      "url": "https://stacks.math.columbia.edu/tag/0BX4",
      "quote": "extending $f$.",
      "premise": 6
    },
    {
      "id": "f12124b7-3be3-4de2-bcb8-ab7a4fcf6f2a/13",
      "statement": "Over a complete algebraically closed nontrivially valued non-Archimedean field, the logarithm of the absolute value of an invertible analytic function on an open subset of a smooth analytic curve is harmonic in Thuillier’s sense.",
      "url": "https://aif.centre-mersenne.org/item/10.5802/aif.3432.pdf",
      "quote": "strongly harmonic functions are harmonic in the sense of Thuillier.",
      "premise": 7
    },
    {
      "id": "f12124b7-3be3-4de2-bcb8-ab7a4fcf6f2a/14",
      "statement": "On an open subset Ω of a smooth proper curve over a complete algebraically closed nontrivially valued non-Archimedean field, harmonic functions satisfy the local maximum principle. An usc function Ω→R∪{−∞}, not identically −∞ on any connected component, is subharmonic exactly when its difference with every local harmonic test satisfies that principle; subharmonic functions satisfy harmonic comparison on strictly affinoid domains.",
      "url": "https://d-nb.info/1190888386/34",
      "quote": "locally constant at x0.",
      "premise": 8
    },
    {
      "id": "f12124b7-3be3-4de2-bcb8-ab7a4fcf6f2a/15",
      "statement": "On an open subset Ω of a smooth proper curve over a complete algebraically closed nontrivially valued non-Archimedean field, harmonic functions satisfy the local maximum principle. An usc function Ω→R∪{−∞}, not identically −∞ on any connected component, is subharmonic exactly when its difference with every local harmonic test satisfies that principle; subharmonic functions satisfy harmonic comparison on strictly affinoid domains.",
      "url": "https://d-nb.info/1190888386/34",
      "quote": "the following are equivalent:",
      "premise": 8
    },
    {
      "id": "f12124b7-3be3-4de2-bcb8-ab7a4fcf6f2a/16",
      "statement": "On an open subset of a smooth proper curve over a complete algebraically closed nontrivially valued non-Archimedean field, a subharmonic function is finite at every point of type II or III.",
      "url": "https://d-nb.info/1190888386/34",
      "quote": "valued on I(W).",
      "premise": 9
    },
    {
      "id": "f12124b7-3be3-4de2-bcb8-ab7a4fcf6f2a/17",
      "statement": "Every smooth integral affine curve over a perfect field admits an open immersion into a smooth projective curve.",
      "url": "https://stacks.math.columbia.edu/tag/0BXX",
      "quote": "$Y$ is a smooth projective curve.",
      "premise": 10
    },
    {
      "id": "f12124b7-3be3-4de2-bcb8-ab7a4fcf6f2a/18",
      "statement": "The absolute value of a complete real-valued non-Archimedean field extends uniquely to every algebraic field extension; a finite extension equipped with that absolute value is complete.",
      "url": "https://kskedlaya.org/18.787/compiledv1.pdf",
      "quote": "admits a unique extension",
      "premise": 11
    },
    {
      "id": "f12124b7-3be3-4de2-bcb8-ab7a4fcf6f2a/19",
      "statement": "The completion of an algebraically closed non-Archimedean valued field is algebraically closed.",
      "url": "https://kskedlaya.org/18.787/compiledv1.pdf",
      "quote": "completion of F is also algebraically closed.",
      "premise": 12
    },
    {
      "id": "f12124b7-3be3-4de2-bcb8-ab7a4fcf6f2a/20",
      "statement": "The Berkovich spectrum of a commutative unital Banach ring is compact.",
      "url": "https://arxiv.org/pdf/1010.2235",
      "quote": "The spectrum X = M(A) is compact,",
      "premise": 13
    },
    {
      "id": "f12124b7-3be3-4de2-bcb8-ab7a4fcf6f2a/21",
      "statement": "Analytification preserves finite and proper morphisms of separated finite-type schemes over a complete non-Archimedean field. A finite analytic morphism is proper, and inverse images of compact analytic domains under a proper analytic morphism are compact.",
      "url": "https://arxiv.org/pdf/1010.2235",
      "quote": "Any finite morphism is proper.",
      "premise": 14
    },
    {
      "id": "f12124b7-3be3-4de2-bcb8-ab7a4fcf6f2a/22",
      "statement": "Analytification preserves finite and proper morphisms of separated finite-type schemes over a complete non-Archimedean field. A finite analytic morphism is proper, and inverse images of compact analytic domains under a proper analytic morphism are compact.",
      "url": "https://arxiv.org/pdf/1010.2235",
      "quote": "finite, closed immersion, open immersion, isomorphism, proper, separated.",
      "premise": 14
    },
    {
      "id": "f12124b7-3be3-4de2-bcb8-ab7a4fcf6f2a/23",
      "statement": "A Noetherian normal domain R equals the intersection, inside its fraction field, of R_p over all height-one primes p.",
      "url": "https://stacks.math.columbia.edu/tag/031T",
      "quote": "R = \\bigcap \\nolimits _{\\text{height}(\\mathfrak p) = 1} R_{\\mathfrak p}",
      "premise": 15
    },
    {
      "id": "f12124b7-3be3-4de2-bcb8-ab7a4fcf6f2a/24",
      "statement": "A Noetherian local normal domain of dimension one is a discrete valuation ring.",
      "url": "https://stacks.math.columbia.edu/tag/00PD",
      "quote": "The ring $A$ is a Noetherian local normal domain of dimension $1$.",
      "premise": 16
    },
    {
      "id": "f12124b7-3be3-4de2-bcb8-ab7a4fcf6f2a/25",
      "statement": "For a closed subscheme X⊊P^D over an algebraically closed field and a closed point p∉X, projection from p restricts to a finite morphism X→P^{D−1}.",
      "url": "https://stacks.math.columbia.edu/tag/0B1P",
      "quote": "defines a finite morphism",
      "premise": 17
    },
    {
      "id": "f12124b7-3be3-4de2-bcb8-ab7a4fcf6f2a/26",
      "statement": "For an integral closed variety T⊂P^D over an algebraically closed field, a nonsingular point z∈T, and dim T<D−1, a nonempty open set of projection centers gives projections that are isomorphisms onto their images over neighborhoods of the image of z.",
      "url": "https://stacks.math.columbia.edu/tag/0B1Q",
      "quote": "is an isomorphism over an open neighbourhood of $r_ p(x)$.",
      "premise": 18
    },
    {
      "id": "f12124b7-3be3-4de2-bcb8-ab7a4fcf6f2a/27",
      "statement": "A scheme locally of finite type over a field is Jacobson, and its closed-point residue fields are algebraic over that field.",
      "url": "https://stacks.math.columbia.edu/tag/0478",
      "quote": "$X$ is a Jacobson scheme",
      "premise": 19
    },
    {
      "id": "f12124b7-3be3-4de2-bcb8-ab7a4fcf6f2a/28",
      "statement": "For a reduced scheme locally of finite type over a perfect field, the smooth locus equals the regular locus and is dense and open.",
      "url": "https://stacks.math.columbia.edu/tag/0B8X",
      "quote": "and this is a dense open subscheme of $X$.",
      "premise": 20
    },
    {
      "id": "f12124b7-3be3-4de2-bcb8-ab7a4fcf6f2a/29",
      "statement": "Wu, arXiv:2609.27610v1, invokes Proposition 2.24 and Theorem 6.5 in the countable-dense-subfield part of the proof of Theorem 7.1.",
      "url": "https://arxiv.org/pdf/2609.27610v1",
      "quote": "by Proposition 2.24",
      "premise": 21
    },
    {
      "id": "f12124b7-3be3-4de2-bcb8-ab7a4fcf6f2a/30",
      "statement": "Wu, arXiv:2609.27610v1, invokes Proposition 2.24 and Theorem 6.5 in the countable-dense-subfield part of the proof of Theorem 7.1.",
      "url": "https://arxiv.org/pdf/2609.27610v1",
      "quote": "Theorem 6.5 implies",
      "premise": 21
    },
    {
      "id": "f12124b7-3be3-4de2-bcb8-ab7a4fcf6f2a/31",
      "statement": "The exact accepted round77/actual80 and exact GEO/countable extraction root91/actual87 plus binding are granted only for their stated partial scope.",
      "url": "urn:xean:task",
      "quote": "The exact accepted round77/actual80 and exact GEO/countable extraction root91/actual87 plus binding are granted only for their stated partial scope.",
      "premise": 22
    }
  ],
  "premises": [
    "For a scheme locally of finite type over a field, normalization is finite and dominant, factors through reduction, and has normal integral components. For a reduced finite-type scheme it is birational.",
    "In a Noetherian ring, every prime minimal over an ideal generated by r elements has height at most r.",
    "Every field is universally catenary. For a finite-type domain R over a field F and every prime p of R, height(p)+trdeg_F κ(p)=trdeg_F Frac(R), and dim R=trdeg_F Frac(R).",
    "An integral finite-type scheme over an algebraically closed field remains integral after every field extension.",
    "A normal integral finite-type curve over a perfect field is smooth, and its local rings at closed points are discrete valuation rings.",
    "A nonconstant morphism of integral curves over a field is flat if its target is normal.",
    "Let X be a Noetherian S-scheme, U⊂X open, x∈closure(U), and O_{X,x} a valuation ring. If Z→S is proper, every S-morphism U→Z extends to an S-morphism on an open subset containing U and x.",
    "Over a complete algebraically closed nontrivially valued non-Archimedean field, the logarithm of the absolute value of an invertible analytic function on an open subset of a smooth analytic curve is harmonic in Thuillier’s sense.",
    "On an open subset Ω of a smooth proper curve over a complete algebraically closed nontrivially valued non-Archimedean field, harmonic functions satisfy the local maximum principle. An usc function Ω→R∪{−∞}, not identically −∞ on any connected component, is subharmonic exactly when its difference with every local harmonic test satisfies that principle; subharmonic functions satisfy harmonic comparison on strictly affinoid domains.",
    "On an open subset of a smooth proper curve over a complete algebraically closed nontrivially valued non-Archimedean field, a subharmonic function is finite at every point of type II or III.",
    "Every smooth integral affine curve over a perfect field admits an open immersion into a smooth projective curve.",
    "The absolute value of a complete real-valued non-Archimedean field extends uniquely to every algebraic field extension; a finite extension equipped with that absolute value is complete.",
    "The completion of an algebraically closed non-Archimedean valued field is algebraically closed.",
    "The Berkovich spectrum of a commutative unital Banach ring is compact.",
    "Analytification preserves finite and proper morphisms of separated finite-type schemes over a complete non-Archimedean field. A finite analytic morphism is proper, and inverse images of compact analytic domains under a proper analytic morphism are compact.",
    "A Noetherian normal domain R equals the intersection, inside its fraction field, of R_p over all height-one primes p.",
    "A Noetherian local normal domain of dimension one is a discrete valuation ring.",
    "For a closed subscheme X⊊P^D over an algebraically closed field and a closed point p∉X, projection from p restricts to a finite morphism X→P^{D−1}.",
    "For an integral closed variety T⊂P^D over an algebraically closed field, a nonsingular point z∈T, and dim T<D−1, a nonempty open set of projection centers gives projections that are isomorphisms onto their images over neighborhoods of the image of z.",
    "A scheme locally of finite type over a field is Jacobson, and its closed-point residue fields are algebraic over that field.",
    "For a reduced scheme locally of finite type over a perfect field, the smooth locus equals the regular locus and is dense and open.",
    "Wu, arXiv:2609.27610v1, invokes Proposition 2.24 and Theorem 6.5 in the countable-dense-subfield part of the proof of Theorem 7.1.",
    "The exact accepted round77/actual80 and exact GEO/countable extraction root91/actual87 plus binding are granted only for their stated partial scope."
  ],
  "kind": "codex-report",
  "operationId": "f12124b7-3be3-4de2-bcb8-ab7a4fcf6f2a",
  "reportedAt": "2026-10-05T12:03:37.842Z"
}



END MATHEMATICAL DATA



BEGIN MATHEMATICAL DATA: Original context 17: Binding scope of actual89

# Actual review89: repaired retained scope and application requirements

The completed native Xean result, operation f12124b7-3be3-4de2-bcb8-ab7a4fcf6f2a,
reported at 2026-10-05T12:03:37.842Z, is PASS for the repaired retained partial
argument. Its entire report, all 23 premises and all 32 passages have been read
at root. The preservation helper must independently verify each nonnegative
passage's exact premise binding.

This grant is for the exact repaired continuation96 body and binding, not the
failed original83 assertion. Actual85's FAIL and its missing Rossi neighborhood
antecedent remain preserved. In the repaired assertion z belongs to V; both
applications establish this essential condition at their tested point.

The retained scope is the original-witness trace at every original analytic
point, controlled affine tools, the conditional countable Runge-Hartogs chain,
and the original projective ample-reference membership consequence. Original
norm multiplicities, nonflat and exceptional fibers, extended values, every
reduced slice component, the same relative proper witness, and the full product
argument at the final empty bad stratum are included.

GEO is supplied for the actual algebraic witness applications by the separately
accepted root91 construction. A smooth source with a projective birational
morphism is intended; the morphism itself need not be smooth. Growth comparisons
use the constructed actual boundary reference without changing the scalar
input. Membership precedes regularization and return to the original ring.

The projective consequence assumes the specified original affine contact
witnesses. For each very ample chart use its actual canonical reference and
exhaustion rho_i. After affine membership, the chart extension in cL is
phi-(c-1)rho_i, equal to minus infinity outside. A maximal homogeneous coordinate
gives rho_i=0 at every analytic point; the finite maximum is exactly phi.
The varying-class closure is applied to the constant scalar family phi as
c decreases to one, rather than to the increasing chart extensions.

Retain the slope and constant clarifications: multiplying generators retains
scaled positive slopes; lowering a constant does not make the slopes one.
Real shifts are implemented by decreasing rational shifts of weights and
supports together, retaining equality at contacts and minus infinity.

Resolved-nef fiber descent, contacts for a descended potential, singular target
EP, cardinality descent, and unbounded normalization/energy/MA compatibility
are not supplied by this review. Later independently accepted results may
provide these gates, but their application requires a new explicit join.
Original P16.1 is not closed by this partial PASS.



END MATHEMATICAL DATA



BEGIN MATHEMATICAL DATA: Original context 18: Exact body accepted ONLY within actual89 scope; historical status statements are documentary

---
title: "Original-witness trace and a conditional countable Runge chain"
author: "Unverified mathematical proof draft"
date: "5 October 2026"
geometry: margin=0.85in
fontsize: 10pt
---

Candidate=false. The exact unchanged original P16.1 is not solved. The results below retain every contact and geometric antecedent of the task-granted round77 theorem and precise round80 PASS. The mathematical deductions are drafts; documentary execution does not validate them.

# n1. Whole-base trace on the original witness

This is a conditional mathematical proof draft. The field \(k\) is algebraically closed, trivially valued, and of characteristic zero, without a cardinality restriction. Let \(S=D(a)\subset\mathbb A_k^n\), let \(Y=\operatorname{Spec} B\) be integral, and let \(\pi:Y\to S\) be finite and surjective, of function-field degree \(d\). Let \(u:Y^{\rm an}\to\mathbb R\cup\{-\infty\}\) be usc, locally bounded above, generically finite, and satisfy \(u\le Cg\circ\pi+B_0\) for an actual affine FS exhaustion \(g\) of the original base ring. There is ONE proper birational witness \(\mu:P\to Y\); on it the pullback is locally a decreasing limit on a common neighborhood of the exact rational contact weights in the task-granted round77/80 theorem. Supports are in logarithms of units, lie below their weight, and agree at the tested point with the same additive constant.

Retain the geometric antecedents of that accepted smooth gate in EVERY smooth-open/base-removal application below: a smooth ample-boundary projective compactification and projective birational domination of the restricted original witness by a smooth projective source, with the specified matching reference. This note does not prove those compactification/domination/resolution antecedents. Write GEO for this collection of applications, not for an arbitrary completed-residue-field regularization theorem.

The task grants the entire positive norm-law theorem, not merely a flat-fiber formula. With \(A=k[S]\) normal, its generic degree-\(d\) norm and characteristic coefficients extend as polynomial laws over \(A\). After specialization and algebraic closure, the norm is the product of residue coordinates with strictly positive integer exponents. Nilpotent units have trivial character; Cayley--Hamilton excludes a zero exponent. For an original analytic fiber point \(y\), its weight is
\[
 m_y=e_y[\kappa_y:\mathcal H(s)]>0,\qquad\sum_{y\mid s}m_y=d.
\]
Here \(e_y\) is the residue-character exponent and \(\kappa_y\) the finite residue field of the corresponding Artinian factor. These are not nonflat fiber lengths. The weights regroup under every complete extension. This granted result includes continuity of traces of continuous functions on controlled compact preimages and local constancy of the integer trace of a clopen indicator.

For clarity the granted finite test identity is
\[
 \sum_{y\mid s}m_y D^{-1}\max_i(\log|b_i(y)|+\lambda_i)
 =D^{-1}\max_{|\alpha|=d}\bigl(\log|a_\alpha(s)|+\alpha\cdot\lambda\bigr),
 \quad N\Bigl(\sum_iT_i b_i\Bigr)=\sum_\alpha a_\alpha T^\alpha.
 \tag{T1}
\]
The constant branch is retained, and the original base generators can be appended at dominated positive slopes. Weighted Gauss multiplicativity applies at every positive real radius. The theorem proved here under GEO is that the left trace of the ORIGINAL weak \(u\), with every finite or minus-infinity value, is an actual decreasing original-ring affine FS limit on the WHOLE base.

## Construct the base extension before identifying the bad values

Choose one principal \(W=D(f)\subset S\) on which \(\pi\) is finite étale and the original witness is an isomorphism over \(\pi^{-1}W\). Such an open exists: in characteristic zero the generic extension is separable; clear denominators in a primitive-element presentation, then invert its discriminant and the finitely many remaining module denominators. Remove also the finite image of the complement of the witness's isomorphism locus. A nonzero product of the relevant functions gives \(f\). Thus \(U=\pi^{-1}W\) is smooth affine. Apply the accepted conditional smooth upper-growth gate to \(u|_U\), with the same restricted witness. An affine FS exhaustion of \(U\) includes all original source generators and the inverted functions. It dominates the original upper bound. Conversely finite integrality bounds original source generators by base generators: for a monic equation \(z^r+\sum_{i<r}a_i z^i=0\), at every seminorm,
\[
 |z|\le\max(1,\max_{i<r}|a_i|^{1/(r-i)}).
\]
Polynomial degree bounds give the required rational affine upper growth without changing either algebra.

Trace the resulting decreasing AFS sequence using \(T1\). This gives an actual decreasing AFS sequence on \(W\), with limit \(N_\pi u\) there. Positivity and \(\sum m_y=d\) give the upper bound \(Cd g+dB_0\) for its limit. The accepted principal-open removal gate on the SMOOTH ORIGINAL \(S\), retaining GEO, furnishes an actual affine FS limit \(v\) on \(S\) agreeing with this trace on \(W\). No bad-fiber value has yet been identified. Generic finiteness is preserved: on the generic good fiber there is the generic trivial point, and its trace is finite.

## Slice at an arbitrary analytic point

Fix \(s\in S^{\rm an}\), set \(F=\mathcal H(s)\), and write its original coordinates as \(\alpha\in F^n\). If \(s\in W^{\rm an}\) the conclusion is already true. Otherwise choose \(z_0\in W(k)\) and set
\[
 c(t)=\alpha+t(z_0-\alpha).
\]
This is a nonconstant actual \(F\)-line. Work in the parameter open \(T\subset\mathbb A_F^1\) where all base-chart denominators are nonzero; it contains 0 and 1. The restrictions of \(a\) and \(f\) to the line are nonzero polynomials, since their values at 1 are nonzero. Every sufficiently small positive-radius parameter Gauss point belongs to \(T\) and maps to \(W^{\rm an}\): a nonzero polynomial has nonzero Gauss norm. The original image \(s_r\) tends to \(s\).

The original \(Y\) is geometrically integral because \(k\) is algebraically closed. The line inverse image in \(Y_F\) is defined by \(n-1\) affine linear equations. Krull's height bound gives height at most \(n-1\) for every minimal prime; the finite-type domain dimension formula over \(F\) gives component dimension at least one. Finiteness over \(T\) gives dimension at most one. Thus, after reduction, EVERY component is a horizontal curve. There are no isolated reduced vertical components. Normalize this reduction to obtain
\[
 q:C^\nu\longrightarrow T,\qquad p:C^\nu\longrightarrow Y_F.
\]
Normalization is finite; each component is regular and smooth over the perfect field \(F\). A nonconstant map to the regular parameter curve is flat: its local modules over the base DVR are torsion free. The total generic rank is exactly \(d\), since over the good open the entire inverse image is the original finite étale base change and normalization changes nothing there. For \(n=1\) there are no cutting equations and the same argument applies. For \(n=0\), \(S,Y\) are single points and the assertion is the direct degree-one identity.

External algebraic inputs, with every hypothesis used here, are [Stacks normalization 33.27.1](https://stacks.math.columbia.edu/tag/0BXQ), [height bound 10.60.12](https://stacks.math.columbia.edu/tag/0BBZ), [dimension formula 10.113.1](https://stacks.math.columbia.edu/tag/02IJ), [normal curve smoothness 33.43.8](https://stacks.math.columbia.edu/tag/0B8Y), and [curve flatness 53.2.3](https://stacks.math.columbia.edu/tag/0BXX). The fields here have characteristic zero; finiteness and the domain conditions are essential.

## Lift the entire curve to the ONE original witness

Each normalized component maps generically into the isomorphism locus of \(\mu_F\), hence has a rational lift. At every closed curve point the local ring is a DVR. Apply the RELATIVE valuative criterion to \(P_F\to Y_F\), using \(C^\nu\to Y_F\) as the base map. The unique local extension spreads to a neighborhood by finite presentation. Separatedness identifies overlaps. This gives a lift of the entire \(C^\nu\) to the original \(P_F\), and it remains this lift after further field extension. The target need not be proper over \(F\). [Stacks 29.43.5](https://stacks.math.columbia.edu/tag/0BX4) has exactly this relative hypothesis; its pertinent proof uses 29.43.1 and spreading of the local map.

At a lifted center restrict EACH original continuous contact approximant before taking its decreasing limit. Its affine support becomes a real linear combination of logarithms of analytic units, hence harmonic on the smooth analytic curve. If the weight minus a harmonic test attains a local maximum, its supporting harmonic function minus that test has the same local maximum and is locally constant; the two inequalities force the weight minus the test to be constant nearby. The harmonic-test characterization and decreasing closure give subharmonicity, or the identically-minus-infinity alternative on a local connected component. The same applies to \(v\circ c\), using its actual decreasing AFS approximants. No positive-current pullback or affine theorem over \(F\) is invoked.

The curve inputs are exactly the pertinent units of [Thuillier, tel-00010990v1](https://theses.hal.science/tel-00010990v1/document): unit logarithms at LF3580--3627; harmonic maximum at LF3730--3741; subharmonic comparison, closure and finite boundary values at LF3783--3852; harmonic-test characterization at LF3860--3904. These were retained by UTF8 byte decode and inclusive one-based LF split. A local component containing a point with finite limit is not the identically-minus-infinity alternative.

## An actual disc coordinate and a direct radial limit

If \(F\) is trivially valued, first complete \(F(\tau)\) with an independent nontrivial Gauss norm. In all cases pass isometrically to a completed algebraic closure \(L\). All original pulled values stay unchanged. The residue characteristic is zero: the trivially valued subfield \(k\supset\mathbb Q\) embeds into the residue field. The finite center fiber of the smooth \(C^\nu_L\) consists of \(L\)-rational points.

Here is the analytic-coordinate argument rather than a formal-local-ring substitution. At such a point smoothness gives a local algebraic presentation \(F_i(z,w)=0\) with a square invertible \(w\)-Jacobian \(J\) at the center, translated to 0. On sufficiently small closed polydiscs the nonlinear part has \(w\)-Lipschitz norm strictly less than one after multiplication by \(J^{-1}\); choose a smaller \(z\)-radius so the constant \(w\)-term fits in that \(w\)-disc. The map \(w\mapsto w-J^{-1}F(z,w)\) is then a strict contraction preserving the disc. The successive iterates converge in its Tate algebra to an analytic \(w(z)\). For every complete residue extension the same contraction proves uniqueness of a solution. Thus the graph and projection are inverse on the actual Berkovich neighborhood. A presentation of the smooth local scheme is obtained by choosing a nonvanishing Jacobian minor and shrinking its algebraic open; the independent equations generate the local ideal there. This prevents extra graph components. The identical contraction argument shows that \(z+O(z^2)\) is an analytic coordinate after shrinking.

Let \(h\) be one of the pulled decreasing limits and \(x\) the center. On a strict closed disc \(D_R\) in this coordinate its boundary is the unique Gauss point \(\xi_R\). If \(h(x)\) is finite, the local limit is subharmonic, its boundary value is finite by Thuillier 3.1.9, and comparison with that constant gives
\[
 h(x)\le h(\xi_R).
\]
Upper semicontinuity and \(\xi_R\to x\) give the reverse limsup. Hence \(h(\xi_R)\to h(x)\). If \(h(x)=-\infty\), usc gives this limit directly: for every real \(M\) all sufficiently close values are below \(M\). Local upper boundedness excludes a compensating plus-infinity term. This proves a particular strict-disc radial limit, not just a punctured-neighborhood limsup.

## Entire Gauss fibers, degrees, and canonical regrouping

At each center \(x\in q^{-1}(0)(L)\) the map has form \(t=b_xz^{e_x}U_x(z)\), where \(b_x\ne0\), \(e_x\ge1\), and \(U_x(0)=1\). On a smaller disc \(|U_x-1|<1\). The binomial series for an \(e_x\)-th root converges because all rational coefficients have norm at most one and its argument has norm less than one. Replacing \(z\) by \(zU_x^{1/e_x}\) is an analytic coordinate as just proved. The map is EXACTLY \(t=b_xz^{e_x}\).

For small strict \(r\in|L^\times|\), the disc above \(\zeta_r\) has the one Gauss point of radius \(R_x=(r/|b_x|)^{1/e_x}\), of completed residue degree \(e_x\). To check uniqueness and degree, scale the radii to one. Over the completed Gauss field the polynomial has residue \(Z^{e_x}-T\), irreducible over \(\widetilde L(T)\) by Eisenstein at \(T\). Its quotient is a field of degree \(e_x\), and a complete field has a unique extension of its absolute value to a finite extension. Thus there is one analytic point, with exactly that degree. Divisibility of \(|L^\times|\) ensures \(R_x\) is also strict.

No missing points are concealed outside these coordinates. Fix a small strict closed base disc in \(T_L^{\rm an}\). Its inverse image under the finite \(q_L\) is compact: it is the spectrum of a finite algebra over the corresponding disc affinoid algebra. Equivalently monic equations bound finitely many algebra generators; all inverted chart denominators are uniformly nonzero on the chosen base disc. In this fixed compact inverse image take the closed complement of the union of ALL center neighborhoods. Intersect it with inverse images of successively smaller closed base discs. These compact sets decrease to the empty set, since their intersection would lie over 0 and the full finite center fiber was covered. Compactness makes one of them empty. Hence the center discs account for the ENTIRE sufficiently small Gauss fiber, not only its exhibited branches.

Before splitting the centers, the trace coefficient at a closed \(F\)-point \(x\) of the normalized curve is \(e_x[\kappa(x):F]\); their sum is \(d\). Why are these the ORIGINAL nonflat norm weights at 0? Pull the original polynomial norm law to \(T\). Over its dense good open it is the determinant norm of the finite étale cover. The product of determinant norms of the finite flat normalized horizontal curves is a regular polynomial law on \(T\), with the same law on that open. Coefficientwise equality over an integral parameter ring gives equality at 0. A uniformizer of order \(e_x\) makes the curve norm specialize to its residue norm raised to \(e_x\). This identifies every residue character, so grouping the centers by their images in \(Y_F\) gives exactly \(m_y\). Subsequent complete-field compatibility groups split \(L\)-centers back into each original analytic fiber point. No fiber-dimension formula at a nonflat point is used. This also proves independence from the chosen good line.

For all sufficiently small strict radii, therefore,
\[
 v(s_r)=N_\pi u(s_r)
       =\sum_{x\in q^{-1}(0)(L)} e_x\,u\bigl(p(\xi_{x,r})\bigr).
\]
The first equality was established on \(W\) BEFORE this argument. Apply the radial limits to the left and every term. If all center values are finite, ordinary finite summation applies. If one is minus infinity, its positive-weight term tends to minus infinity and the other finitely many terms remain bounded above, so the entire sum tends to minus infinity. Regrouping yields
\[
 v(s)=\sum_{y\mid s}m_y u(y)=N_\pi u(s).
\tag{T2}
\]
This establishes the whole-base trace application under GEO on the original ring and witness, including every nonflat, exceptional, removed, and minus-infinity value. The norm-law part and smooth gate are task-granted background with their binding restrictions, not invented native support IDs. Singular EP, fiber descent, and the original equation are not consequences of \(T2\).

Artifacts: `n1-trace.md`, combined `P16.1-argument.md`, standalone `P16.1-paper.tex` and `P16.1-paper.pdf`; primary units in `source-extracts/`, web retrievals in `web-primary-01.json` through `web-primary-04.json`, premise coverage in `external-premises.json`. Reproduce with `python3 rerun.py`. All new combined deductions are unverified drafts.


# n2. Controlled approximation, original-ring hulls, and a countable barrier

All claims in this note are unverified mathematical proof drafts. Except in the explicitly countable barrier construction, retain an arbitrary algebraically closed trivially valued field k of characteristic zero. Y=Spec R is integral affine of finite type. An AFS function means a rational finite maximum of positive multiples of original regular-function logarithms and a rational constant floor, retaining a positive-slope branch for EVERY chosen original ring generator. A genuine AFS limit is an already supplied decreasing sequence of such functions; membership is not inferred from singular EP. The algebraic-first continuous contact/model/nef/FS bridge and genuine decreasing closure are task-granted background in their exact round80 scope.

## G: a controlled original-reference approximation

Let g be an actual rational AFS exhaustion, shifted so g>=0, and let v_j decrease to a generically finite v with v<=g+B. Fix rational c>1. We prove that v admits a decreasing original-ring AFS sequence w_j with a common upper bound cg+B', and with |w_j-cg| bounded on Y for each individual j. Neither the bounds nor this conclusion assume singular envelopes.

First compactify the actual g. Clear its positive rational slopes with an integer D. Use projective coordinates consisting of 1, the integer powers occurring in Dg, AND all original generators z_l. Take D large enough that the extra branches D^(-1)log|z_l|+lambda_l are dominated by g; polynomial degree bounds and the exhaustion bound allow rational lambda_l. The projective closure has the ORIGINAL affine chart Y, since these unpowered generators generate R. Powers alone would not prove this. Its boundary section s of H=O(1) and the actual rational bundle B_ref=H/D have an FS metric with affine weight exactly g. Write g=g_0+p, where g_0 is the canonical boundary-section reference and p the actual global FS potential, with its original cocycle.

Choose rational C_i decreasing to minus infinity and rational R_i increasing to infinity, with (c-1)R_i>B-C_i+2. Let Q_i={g<=R_i}, which is compact. Choose increasing indices j_i such that v_{j_i}<g+B+1 on Q_i. This follows because the closed sets {v_j>=g+B+1} in Q_i decrease to the empty set. It does NOT require Dini convergence to a discontinuous limit.

Define a_i=max(v_{j_i},cg+C_i) on Q_i and a_i=cg+C_i outside Q_i. Near its entire outer boundary the second branch wins strictly, so this is a continuous contact weight with a whole reference-winning collar. The canonical potential is a_i-cg_0, not a_i-cg; its boundary value is C_i+cp. The granted bridge puts it in the genuine class cB_ref on the original compactification. These weights decrease: on Q_i both branches decrease; on Q_{i+1}\Q_i the new first branch is at most g+B+1<cg+C_i, the old exterior value; on the remaining exterior the floor decreases. Their limit is v on Y and minus infinity relative to g_0 at the boundary. Genuine decreasing closure supplies membership before any sequential regularization is invoked.

Genuine same-bundle FS regularization of this limit now gives w_j. In the section-s frame, compact boundedness of each continuous canonical potential gives |w_j-cg|=O(1); the first potential bounds all later ones, giving the common upper bound. Alternatively, uniformly approximate each continuous a_i in the same bundle with errors epsilon_i=4^(-i) and shifts b_i=2 sum_{r>=i}epsilon_r. Since b_i-b_{i+1}=2epsilon_i>=epsilon_i+epsilon_{i+1}, these shifted approximants decrease. This also constructs the desired sequence without EP.

Conversion to R is literal: a section on a tensor power divided by s to that power is an original regular function. Append s^m as the floor and the sections representing z_l times suitable powers of s at very low rational weights. For sufficiently large common m they exist by section localization. On the compact projective space their continuous norms are bounded, whereas the approximating metric has a finite lower bound; thus these added terms are dominated everywhere and change no value. EVERY original generator remains, with positive slope 1/m. The reference, tensor bundle and transition functions stay the same. The construction works on a singular Y and a singular compactification for an ALREADY genuine affine FS limit.

## Correct pole control through finite normalization

The printed denominator-order argument is false: in k[x], f=x^2 and p=x, p is not in (f) but vanishes on V(f). With q=3/2, b=p/f=1/x, q log|b|<=max(0,log|f^(-1)|), while the printed q times denominator exponent is 3/2>1. The reference G=max(0,log|x|) retains the original generator and only enlarges this upper bound, so the counterexample satisfies the genuine original-reference requirement. Its conclusion cannot be used.

Here is the replacement. Suppose b in R_f is nonzero and q,c are positive rational numbers, and

q log|b| <= max(G,c log|f^(-1)|)+B_0

on Y_f, where G is an original-ring AFS function finite everywhere on Y. Choose N so m=Nc/q is an integer and put h=b^N f^m. Let Rbar be the finite normalization of R. At each height-one prime E of Rbar containing f, use the seminorm exp(-t ord_E), t>0. It restricts to an analytic point of Y_f; every original regular function has norm <=1, so G is bounded above independently of t. Divide the displayed inequality by t and let t tend to infinity. It gives q ord_E(b)+c ord_E(f)>=0, hence ord_E(h)>=0. At other height-one primes h is already regular, since h belongs to R_f. A normal Noetherian domain is the intersection of its height-one localizations, so h belongs to Rbar and is integral over R.

This uses precisely [finite normalization, Stacks 33.27.1](https://stacks.math.columbia.edu/tag/0BXQ), [height-one intersection, 10.157.6](https://stacks.math.columbia.edu/tag/031T), and [the DVR characterization](https://stacks.math.columbia.edu/tag/00PD). R is a finite-type domain over a field, so its normalization is finite and Noetherian; h is in its fraction field. All hypotheses are retained.

The integral algebra R[h] is a finite R-module contained in R_f. Choose a finite module generating list and clear its denominators with ONE f^M. Then

f^M h^j belongs to the ORIGINAL R for EVERY integer j>=0.

No assertion that h itself, or a specified power of h, belongs to R is needed. For example, R=k[t^2,t^3], f=t^2, b=t^(-1), and h=bf=t is integral, with h^2=f, but h is not in R. The ONE multiplier f puts EVERY h^j into R, since f h^j=t^(j+2) and every integer >=2 is in the semigroup generated by 2 and 3. If x is in the original polynomial hull of a compact L contained in Y_f and x is also in Y_f, apply its defining inequalities to these original polynomials. They give

|f(x)|^M |h(x)|^j <= sup_L |f|^M |h|^j <= (sup_L |f|)^M (sup_L |h|)^j.

If the last h-supremum is zero, the inequality already forces h(x)=0. Otherwise take j-th roots and let j increase. Thus |h(x)|<=sup_L |h|. If |log|f||<=M_1 on L union {x}, substitution of h gives

q log|b(x)| <= sup_L q log|b| + 2cM_1.                     (P)

The constant branch satisfies the hull bound directly. Apply (P) branchwise to an AFS w<=max(g,c log|f^(-1)|)+O(1). Maxima commute with the finite supremum, so the same 2cM_1 error holds for w.

Now let v be an already genuine AFS limit on Y_f, bounded above by an original AFS reference on Y. Choose g large enough, including every original generator, and set g_c=max(g,c log|f^(-1)|); it is an actual reference for the ORIGINAL localized ring, including f^(-1). G with multiplier 2 supplies w_i decreasing to v, with w_i<=2g_c+B'. Formula (P) therefore gives w_i(x)<=sup_L w_i+4cM_1. On a compact L, for decreasing continuous w_i and usc limit v, sup_L w_i decreases to sup_L v. Indeed, if a level exceeds the latter supremum, the nested closed superlevel sets eventually become empty. This argument also covers sup_L v=-infinity. Let i increase and then c decrease to zero. We obtain the exact original-ring hull inequality

v(x)<=sup_L v.                                           (H)

The case v(x)=-infinity is immediate. This proves principal-open hull control, rather than a false denominator estimate.

## Countable entropy barrier, including every coordinate face

Here assume k countable, so R is countable. Choose original generators z_1,...,z_k, enumerate every element f_1,f_2,... of R, and put g=max(0,log|z_l|). For s coordinates t in (R union {+infinity})^s choose rational beta>=log(s+1), and define

chi_s(t)=beta^(-1)log(1+sum_i exp(-beta t_i)), exp(-beta infinity)=0.

Then max(0,-t_i)<=chi_s<=max(0,-t_i)+1. At a point with finite coordinate set I let p_i=exp(-beta t_i)/(1+sum exp(-beta t_l)), and p_0=1/(1+sum exp(-beta t_l)); omitted coordinates have p_i=0. Its support is ell=-sum_{i in I}p_i t_i+C, with C chosen for equality at that point. The entropy inequality proves ell<=chi_s. Equality is unique: on the finite face strict log-sum-exp convexity uses p_i>0 and p_0>0; an omitted coordinate becoming finite adds a positive term.

The support has a UNIFORM positive gap outside any neighborhood of the point. On the finite face its recession expression is max(0,-a_i)+sum p_i a_i. It is positive for every nonzero vector a, since all p_i and p_0 are positive. Hence the support difference is coercive there. Restricting the finite coordinates to a compact box, any omitted coordinate leaving a prescribed neighborhood of +infinity has a positive lower bound on its exponential contribution. Compactness and strict equality then give the claimed gap. At the all-infinity point the support is zero and the same exponential argument applies. No coefficient is placed on an infinite coordinate.

Here is global rational approximation, including those faces. On the probability simplex in coordinates p_0,...,p_s define E(p)=beta^(-1)sum p_i log p_i, with 0 log0=0. Triangulate it by rational grids of mesh tending to zero, respecting ALL coordinate faces. At each grid vertex choose rational h_p in [E(p),E(p)+epsilon]. Its convex roof is between E and E+delta, where delta tends to zero: the lower bound is convexity, and the upper bound follows by interpolation and uniform continuity on the compact simplex. Take its conjugate. Explicitly

H_r(x)=max_{grid vertices p}(sum_{i>=1}p_i x_i-h_p)+delta_r

satisfies chi_s(-x)<=H_r(x)<=chi_s(-x)+delta_r globally, with rational delta_r tending to zero. All slopes are nonnegative rational; all heights are rational. If x_i=-infinity, discard vertices with p_i>0. The face triangulation gives the SAME error bound, including the all-infinity face p_0=1. This is not an approximation proved only on a finite Euclidean box. Clearing rational slopes converts each branch to an original monomial logarithm. Rational majorants can be made decreasing by the summable-error shifts used in G.

Let rho_j=chi_{k+j}(-log|z_1|,...,-log|z_k|,-log|f_1|,...,-log|f_j|). Polynomial degree bounds give rho_j<=D_j g+1, and rho_j>=g. Choose positive rational gamma_j with gamma_j(D_j+1)<=2^(-j). Then

rho=sum_{j>=1}gamma_j rho_j

converges uniformly on every compact generator-bounded set, is continuous, nonnegative, and bounded by g+1. The upper partial sums P_r=sum_{j<=r}gamma_j rho_j+2^(-r)(g+1) decrease, since the next summand is at most 2^(-(r+1))(g+1). Uniform rational approximations to their finite sums, with summable shifts, give a decreasing actual AFS sequence for rho. Generator branches are already dominated by rho_j>=g and may be appended unchanged. This proves membership directly from rational maxima and the granted bridge/closure, not from the printed affine main theorem.

Given an analytic x and an open U containing x, countability and the seminorm topology give a finite coordinate neighborhood with inverse image contained in U. Choose j including those coordinates. Replace rho_j by its support ell at x and keep ALL the other positive summands. The resulting rho' satisfies rho'<=rho, rho'(x)=rho(x), and rho'<=rho-delta outside U, for some delta>0. Near x its support contains only logarithms of units. Globally it can be unbounded below or equal minus infinity; it has no plus-infinity values.

We must prove actual AFS membership of this replacement rather than subtract a psh function. A positive real coefficient a times log|f| is approximated by nested rational intervals a_r increasing to a and b_r decreasing to a, with a_r>0. The functions max(a_r log|f|,b_r log|f|) decrease to a log|f|: use b_r for a positive logarithm, a_r for a negative one, and retain minus infinity at a zero. Zero coefficients are omitted. Choose decreasing rational constants approaching C. Approximate the other positive rho_i-summands with the same positive tail bounds and summable shifts. These explicit sums and maxima are decreasing rational logarithmic expressions with the stated pointwise limit, including minus infinity.

To retain a constant floor and EVERY original generator, append max(epsilon_r g-r, the expression), with positive rational epsilon_r decreasing to zero. The appended AFS expression decreases because g>=0, and at every fixed analytic point epsilon_r g-r tends to minus infinity. It changes the LIMIT nowhere, including its minus-infinity locus. It need not converge uniformly there, and uniform convergence is not claimed. Restriction to a principal chart uses the identical padding with an exhaustion of its actual localized ring, including every new generator such as f^(-1). Positive sums and maxima of already genuine AFS limits use products of monomials and the same padding. Thus rho' is constructed positively; subtracting rho-rho' is never used as a positivity principle.

## Polynomial hulls and Rossi

For compact L the polynomial hull K={x: |f(x)|<=sup_L|f| for every f in R} is closed and compact: inequalities for the original generators place it inside a compact affine polydisc domain. The AFS hull is the same hull. One inclusion follows branchwise. For the other, a separating original polynomial and rational threshold yield an AFS separator after adding a very low constant floor and all original generator branches at dominated low weights on L union {x}.

If compact polynomially convex K lies in an open U, first choose an ambient generator-bounded compact domain with K in its strict interior. Every point of its compact complement of U has a separating polynomial, and a rational log threshold strictly between its value and its K-supremum. Finitely many such strict separations, together with bounds for every original generator, give a compact polynomial polytope P contained in U and a STRICT polynomial open Q containing K, with Q subset P. A strict finite polynomial domain is Runge: the suprema on any compact subset are strictly below its defining thresholds, so its polynomial hull stays in that strict domain. No equality between arbitrary topological interior and the displayed strict inequalities is used. Hulls respect closed immersions by the quotient-ring definition; increasing unions of Runge opens are Runge by compactness.

Let z belong to hull(L)\L and let V be a relatively compact open NEIGHBORHOOD OF z, with compact closure disjoint from L. Rossi asserts z belongs to hull(K_V), where K_V=boundary(V) intersect hull(L). Suppose log|f(z)|>t>sup_{K_V}log|f|. Choose a nonnegative original AFS g_0 equal to zero on a neighborhood of hull(L), with compact zero-polytope in an open avoiding the bad part of boundary(V) where log|f|>=t. It has a strictly positive lower bound on that compact bad part. Choose rational C so Cg_0>log|f|-t on the ENTIRE boundary. Glue max(Cg_0,log|f|-t) on V to Cg_0 outside. A whole boundary collar is reference-winning. This continuous rational contact weight equals the actual FS reference outside a compact set. On its actual projective reference compactification the granted bridge gives uniform same-bundle FS approximation, hence uniform original AFS approximation after section conversion and generator retention. The glued weight is zero on L and positive at z. A sufficiently accurate approximant contradicts the AFS hull equality. This proves Rossi with compact controlled closures; V itself is not called compact.

## The off-bad-set maximum inequality

Assume the ORIGINAL u is locally genuinely AFS regularizable on an affine cover of Y\Z, has original upper growth, and is weak on one witness. It is not enough to know this only for u+c rho: subtracting psh is unavailable. For rational c>0 put u_c=u+c rho. We prove u_c(x)<=sup_L u_c for x in hull(L)\Z.

If this fails, take generators of the ideal of Z and a=max log|f_i|, with its empty-bad-set version a=0. Choose small positive rational epsilon so u_c+epsilon a still violates the inequality at x. It is usc and upper bounded on compact hull(L), equals minus infinity on Z, and has a finite attained maximum y outside Z union L. Take V around y, with controlled compact closure in one good principal affine chart, disjoint from L. Replace rho by rho' with equality at y and gap delta on boundary(V). The explicit function w=u+c rho'+epsilon a is an actual affine FS limit on that chart, using ORIGINAL u's local regularizability and the positive constructions above. Its upper growth comes from an original global AFS reference, since rho'<=rho. It satisfies w(y)>sup_{K_V}w, with gap at least c delta. Rossi puts y in the original hull of K_V; (H) on the principal chart gives w(y)<=sup_{K_V}w, a contradiction. Every special value and the factor c are retained.

This note proves G, corrected original-ring pole control, the countable barrier, Rossi, and the off-bad-set inequality. It does not assert weak/global equality or singular EP. The task-granted background is cited as an assumption, not as a registered native support. Diagnostic Wu v1 LF911--1017,1603--1730,1815--1885,1965--2108 is retained to identify the repaired dependencies; its printed theorems are not premises. Artifacts: n2-affine-tools.md, sources/, source-extracts/, external-premises.json. Rerun python3 rerun.py.


# n3. Conditional countable-field Runge, Hartogs, and singular-stratum chain

This is a full mathematical proof draft of a CONDITIONAL countable-field chain, using n1 and n2. The field k is countable, algebraically closed, trivially valued, and of characteristic zero. Y is integral affine of finite type. The original u is usc, generically finite, locally bounded above, has an upper bound by an actual original-ring AFS exhaustion, and is weak on ONE proper birational contact witness. All uses of the accepted smooth affine gate retain GEO as defined in n1, including the required smooth ample-boundary compactification and projective birational domination of that same restricted witness by a smooth projective source. No arbitrary completed-residue-field affine theorem or singular EP is imported.

## Split pieces on one controlled neighborhood, including gamma=1

Suppose pi:Y->S is finite surjective onto a principal affine open of A^n. Suppose Z is closed, pi|Z is a CLOSED IMMERSION onto its image, and Z and Z'=pi^(-1)(pi(Z))\Z are disjoint closed subsets. Assume the ORIGINAL u is locally genuinely AFS regularizable off Z. We prove its strict sublevels are Runge.

Use n2's countable nonnegative rho and its positive support replacements. If a strict sublevel of u_c=u+c rho, c>0 rational, is not Runge, there is compact L such that its compact polynomial hull K contains a point where u_c>=0 although sup_L u_c<0. After an additive normalization let sup_K u_c=0 and sup_L u_c=-delta<0; if the latter is minus infinity choose any finite delta with sup_L u_c<=-delta. The finite attained maximum x belongs to Z by n2's off-bad-set inequality.

Put C=hull_S{pi(x)}. Because pi|Z is a closed immersion, the quotient-ring hull property gives C subset pi(Z)^an. The ENTIRE compact preimage of C consists of disjoint compact pieces C_1 in Z and C_2 in Z'. Choose disjoint open neighborhoods A_1,A_2 of these pieces, with A_1 avoiding Z' and A_2 avoiding Z. Properness of the finite analytic map gives an open neighborhood A of C whose entire preimage is in A_1 union A_2: take the complement of the closed image of Y^an\(A_1 union A_2).

By n2's strict polynomial neighborhoods choose a nonnegative actual base AFS g with C in an inner strict neighborhood U where g=0, and {g<=1} compactly contained in A. Let W={g<1}; its preimage splits into the clopen OPEN pieces W_i=pi^(-1)(W) intersect A_i. These interiors are not compact; their controlled closures in pi^(-1){g<=1} are compact. On the preimage of W put h=1 on W_1 and 0 on W_2. The global continuous contact weight H=max(3g circ pi-1,h) there, and 3g circ pi-1 elsewhere, has a whole reference-winning outer collar, and equals h over U.

The task-granted continuous canonical norm trace makes the trace of this indicator over U continuous and integer valued:

gamma_1(s)=sum_{y in pi^(-1)(s) intersect W_1}m_y.

It is only LOCALLY constant. Shrink ONE base neighborhood N of pi(x) inside U where gamma_1 is the positive integer gamma; retain this N for EVERY subsequent hull, boundary and fiber test. All weights m_y are the raw positive canonical integers of n1, never fiber lengths. A closed immersion guarantees analytic fiber injectivity, so the W_1 fiber above pi(x) is exactly {x}, even after a completed residue-field extension.

For gamma>1 shrink N further so all its W_1 fiber values of u_c are <delta/[2(gamma-1)]. This follows from usc at the unique central point x and properness: cover that point by the requisite strict sublevel, cover the other central piece by W_2, and exclude the closed image of the complement. For gamma=1 do not divide by gamma-1. Positivity and integrality imply every W_1 fiber over N is one point of weight one.

Choose a relatively compact open V around x with compact closure in pi^(-1)(N) intersect W_1, disjoint from L. Let K_V=boundary(V) intersect K. Replace rho by rho' with equality at x and rho'<=rho-delta' on boundary(V). Put u'_c=u+c rho'. Then u'_c(x)=0, u'_c<=u_c, and sup_{K_V}u'_c<=-c delta'. The factor c is essential.

On W_1 put v=u'_c, on W_2 put v=0. On the controlled compact closure these have a finite common upper bound M. Choose a rational C_0>M+1+delta and define

tilde v=max(C_0 g circ pi-delta,v) on pi^(-1)(W),
tilde v=C_0 g circ pi-delta outside.

For g sufficiently close to 1 the reference wins on the ENTIRE collar. Pullbacks, products, support replacements and maxima all use the SAME original witness. Its pullback remains locally a decreasing contact limit. The global upper bound is an actual original reference, and the floor makes tilde v finite. Over U it is max(u'_c,-delta) on W_1 and zero on W_2. Apply n1, retaining its GEO applications, to obtain w=N_pi(tilde v) as a genuine original-base AFS limit. Pullback w circ pi is a genuine original-source AFS limit. To retain every source generator, use its monic norm bound to dominate a source exhaustion by a positive multiple of a base exhaustion and append decreasing low floor/generator branches as in n2; the limit is unchanged at every point.

Rossi gives x in hull_Y(K_V), hence w(pi(x))<=sup_{K_V}w circ pi. Its left side is zero. For z in K_V intersect Z, analytic injectivity and avoidance of Z' make the W_1 fiber exactly {z}, of weight gamma, giving

w(pi(z))<=-gamma min(delta,c delta').

For y in K_V\Z, the off-bad-set inequality gives u_c(y)<=sup_L u_c<=-delta, so tilde v(y)=-delta. Every other W_1 fiber point is in the SAME pi^(-1)(N); when gamma>1 its value is at most delta/[2(gamma-1)]. Thus, writing its positive weight m_y>=1,

w(pi(y)) <= -m_y delta+(gamma-m_y)delta/[2(gamma-1)] <= -delta/2.

When gamma=1 there is no other W_1 point and w(pi(y))=-delta. The W_2 values are zero. These are uniform negative bounds on ALL of K_V, a contradiction. Consequently each {u+c rho<0} is Runge. As rational c decreases to zero these opens increase to {u<0}, since rho is finite and nonnegative; compactness gives Runge for their union. The argument applies at every translated level. It preserves minus infinity, all raw weights, the whole collar, and one controlled base neighborhood.

## Genuine Runge exhaustion before coefficient radii

For a countable ring R, the seminorm topology of Y^an is a subspace topology of the countable product of the norm coordinates |f|, f in R. It is second countable and metrizable. Generator-bounded polydisc domains are compact and exhaust Y^an through their strict interiors. Hence every open Runge D admits a countable exhaustion by compact subsets L_r with controlled interiors.

Inductively take the polynomial hull of L_r union the previous controlled closure. It is compact and stays in D by the Runge property. Apply n2's thick polynomial-neighborhood construction to obtain STRICT finite polynomial opens Q_r, with compact controlled closures P_r contained in D, satisfying P_{r-1} subset Q_r and L_r subset Q_r. Then Q_r increase and exhaust D. Their defining polynomials retain bounds for EVERY original generator. We use Q_r={log|P_{rj}|<b_{rj}}, with rational b_{rj}; we do not identify the interior of an arbitrary closed weak-inequality domain with its strict-inequality locus.

Apply this to a genuinely established Runge D in (Y times A^1)^an containing the zero section, writing each P_{rj}=sum_i a_{rji} w^i in ORIGINAL R[w]. The opens where zero lies in Q_r are

Omega_r={log|a_{rj0}|<b_{rj} for all j};

they increase and cover Y^an. For y in Omega_r the fiber is the analytic affine line over F=H(y). Define its open-disc containment radius d_r(y). The EXACT formula is

-log d_r(y)=max_{j,i>=1}(log|a_{rji}(y)|-b_{rj})/i.       (D)

Zero coefficients contribute minus infinity; an empty maximum is minus infinity and means radius infinity. The constant-coefficient conditions defining Omega_r are indispensable.

To prove (D), on a closed radius-s disc the polynomial Gauss norm is max_i |a_i|s^i at EVERY positive real s, whether or not s is in the value group. The ultrametric inequality bounds every point by that norm. Hence the open radius-r disc is contained in all strict constraints exactly when each positive-degree coefficient has |a_i|r^i<=exp(b_j), given the strict constant constraints. Equality at the endpoint causes no problem, since the endpoint is excluded. Conversely a larger open radius contains a Gauss point violating a constraint. This proves (D) over any completed residue field using only polynomial norms, not a regularization theorem there.

By the nesting, d_r increase. For every s<d_D(y), the compact closed fiber disc of radius s lies in D, so a finite subcover of the increasing Q_r puts it in one Q_r. Thus d_r(y) increase to d_D(y), including infinity, and A_r=-log d_r decrease to -log d_D on every eventually defined Omega_r. The exhaustion includes a w-bound, so individual A_r can be taken to have a constant floor. Their rational positive coefficient maxima are continuous contact weights on Omega_r.

If u_D=-log d_D is generically finite and bounded above by an original AFS reference g+B, we now prove controlled ORIGINAL-ring regularization. Choose R_i increasing and C_i decreasing as in n2's G, and indices r_i increasing so the compact {g<=R_i} lies in Omega_{r_i} and A_{r_i}<g+B+1 there. The latter assertion follows from nested compact closed superlevel emptiness; no Dini assertion for u_D is used. Glue max(A_{r_i},cg+C_i) inside {g<=R_i} to cg+C_i outside. The outer reference wins on a whole collar. These continuous contact weights decrease on the old compact domain, the new annulus and the exterior separately, exactly as in G. The granted bridge and decreasing genuine closure give membership in ONE actual bundle cB_ref, then same-class FS regularization gives original-ring affine FS weights decreasing to u_D. Every original coefficient and every original generator is retained by localization and dominated padding. Infinite radius values give minus infinity correctly. This proves the needed Hartogs conclusion after Runge, without presupposing the affine weak/global theorem.

## Hartogs on the same product witness

For any original u as above put H=log|w|+u circ p on Y times A^1, defining its value to be minus infinity when w=0 or u=-infinity. There are no plus-infinity values. Its one witness is P times A^1. Restrict each original contact approximant and approximate log|w| by its decreasing rational floors on the same neighborhoods before taking sums and limits. Supports away from its zeros are unit logarithms, and the zero floors provide continuous contact weights. Thus H is weak on that SAME product witness. It has upper growth by a product exhaustion retaining every Y-generator and w.

On a good affine chart where ORIGINAL u is an AFS limit, H is an actual AFS limit: form products for positive sums, use decreasing floors for log|w|, and append decreasing low generator branches retaining every product-chart generator. If the split-piece hypotheses hold on Y, they hold on Y times A^1 with Z times A^1 and pi times identity, including closed immersion and closed disjoint complementary piece. Applying the already proved split argument to H proves

D={log|w|+u circ p<0}

is genuinely Runge in the PRODUCT. This is not inferred merely from sublevels on Y. It contains the zero section, and its fiber radius is exp(-u(y)), with infinity when u(y)=-infinity. Therefore the preceding coefficient argument gives actual AFS regularization of u. The same reasoning with EMPTY bad set will supply the final local-to-global step.

## Descending Z and localization

Suppose only pi|Z is a closed immersion; drop the initial disjoint-piece hypothesis. Define reduced closed sets Z_1=Z and

Z_{r+1}=Z_r intersect closure_Y(pi^(-1)(pi(Z_r))\Z_r).

They strictly drop dimension until empty. To check ALL components, a closed immersion identifies pi(Z_r) with Z_r; images of its irreducible components are distinct and incomparable. Each component T of Z_r is a component of pi^(-1)(pi(Z_r)): a containing component maps onto a containing component of pi(Z_r), and finiteness preserves its dimension, forcing equality. The closure of the complementary union therefore omits the generic point of every component T. Its intersection with Z_r has strictly smaller maximum dimension. Outside pi^(-1)(pi(Z_{r+1})), the complementary piece pi^(-1)(pi(Z_r))\Z_r is closed, since the only new closure points on Z_r are in Z_{r+1}. This also proves the required localization equality, rather than just a set-theoretic dimension estimate.

Inductively let Pi_r assert ORIGINAL local AFS regularizability at every closed point of Y\Z_r. Pi_1 is the assumed off-Z cover. A closed y in pi^(-1)(pi(Z_{r+1}))\Z_{r+1} is off ORIGINAL Z: otherwise closed-immersion injectivity places it in Z_{r+1}. Use the original off-Z cover. For any other y in Y\Z_{r+1}, choose a principal affine base S' inside S\pi(Z_{r+1}) around pi(y), and set U=pi^(-1)(S') EXACTLY. The induced finite map is onto S'. On U the bad set U intersect Z_r and its complementary inverse-image piece are disjoint closed; the off-bad-set local hypothesis is Pi_r. Apply the split proof on U times A^1 using the same product witness. Its Hartogs domain is Runge, so the preceding coefficient argument gives actual AFS regularization on U. This proves Pi_{r+1}.

At the empty last Z_r we have an algebraic affine local cover. Closed-point neighborhoods cover every scheme point: finite-type schemes over a field are Jacobson, so a nonempty closed complement would contain a closed point ([Stacks 33.14.1](https://stacks.math.columbia.edu/tag/0478)). Their analytifications therefore cover every analytic point. A local cover is not yet the desired global affine conclusion. Apply n2's off-bad-set proof with Z empty to get every {u+c rho<0} Runge, hence {u<0} Runge. Apply that SAME empty-bad-set reasoning to H on the product; now its Hartogs domain is Runge, and the coefficient argument gives ORIGINAL global AFS regularization of u. This supplies the final LOCAL-TO-GLOBAL implication that was missing from the printed induction.

## Finite projection along a smooth stratum, with the correct U

Let Y be integral affine of dimension n and Z proper smooth closed, with dim Z<=n-1. For a closed k-point z in Z, embed the projective closure X into P^D with D>=n+1. Let B=X\Y and T=closure_X Z union B, reduced. T has dimension <=n-1 and is smooth at z, since z is outside B.

Choose a projection center p outside X, outside the closed secant cone from z to T\{z}, and outside the projective tangent space of T at z. The secant cone has dimension <=dim T+1<=n<D. The tangent space and X also have dimension <D, so a k-point outside their union exists. Projection from p is finite on X by [Stacks 43.23.1](https://stacks.math.columbia.edu/tag/0B1P). Its T-fiber over the image of z is only z, and its differential on T there is injective. This is the secant/tangent argument of [43.23.2](https://stacks.math.columbia.edu/tag/0B1Q); the following local algebra proves the needed statement also for the reduced union T with possibly several components away from z.

Let C be the local ring of the scheme-theoretic image at q, and D_T the finite local ring above it. There is just the one point above q, with residue field k. Injective differential gives a surjection on cotangent spaces, so m_{D_T}=m_C D_T+m_{D_T}^2. Nakayama gives m_{D_T}=m_C D_T. Thus D_T/m_C D_T=k is generated by 1; Nakayama for the finite C-module D_T gives D_T=C. The image inclusion and projection are consequently inverse over a Zariski neighborhood of q, after shrinking to kill the finite kernel and cokernel. Here T is smooth at z, and the secant exclusion gives the single fiber; it is not enough to know an arbitrary set-theoretic injectivity statement.

Repeat the projection while the ambient dimension exceeds n. At each step the image T is still smooth at the tested point through the just proved local isomorphism, and has dimension <=n-1; the integral projective image of X has dimension n. The final image of X in P^n is all P^n. The tested point is outside the image of B, since B is part of T and the T-fiber was the single z. Choose a principal affine open S around its image, avoiding the image of B and lying in the isomorphism neighborhood of T. Set

U=r^(-1)(S), pi=r|U:U->S.

This is the correct U, not the printed r^(-1)(W) with a different target S. U is affine, is contained in the ORIGINAL Y, pi is finite onto S, and pi|Z_U is an isomorphism onto a closed image. Its analytic restriction is injective because a closed immersion stays a closed immersion after every complete field extension. Restricting u and its original witness preserves the hypotheses; monic integrality bounds give the required reference growth on S. This geometric finite-projection step is proved here. It does not discharge GEO's separate compactification/resolution antecedents.

## Singular-stratum induction and the conditional affine conclusion

Let Y_0=Y and Y_{r+1} be the reduced singular locus of Y_r. In characteristic zero the regular locus is smooth and dense in EVERY reduced irreducible component ([Stacks 33.25.8](https://stacks.math.columbia.edu/tag/0B8X)), so maximum dimension strictly drops until Y_r is empty. Reducible and unequal-dimensional strata are allowed. Let Sigma_r assert local genuine AFS regularizability at all closed points of Y\Y_r. Sigma_1 follows on smooth affine opens from the accepted smooth gate, retaining all its GEO hypotheses and restrictions of the SAME original witness.

At a new point y in Y_r\Y_{r+1}, choose an affine neighborhood V inside Y\Y_{r+1}. Its Z=V intersect Y_r is a smooth proper closed stratum. The finite projection just proved supplies U around y and pi:U->S with pi|Z_U a closed immersion. The induction gives ORIGINAL local AFS regularizability on U\Z_U. The descending-Z/product-Hartogs theorem supplies actual AFS regularizability on U. This proves Sigma_{r+1}. At the final empty stratum, invoke the EMPTY-Z local-to-global conclusion above, not merely the existence of a local cover.

Consequently, under GEO for its specified smooth applications, every original upper-growth weak input on integral affine Y over countable k is an ORIGINAL-ring decreasing AFS limit, and every strict sublevel is Runge. Every whole-base trace used in this chain is n1's trace on the one original witness. No singular envelope theorem, Wu affine main theorem, arbitrary-field affine regularization, or printed denominator-order claim is a premise.

## A limited countable global membership consequence

Let X be integral projective over countable k, L ample rational, and phi generically finite, globally upper bounded and weak relative to the canonical reference of L. Require the same contact/GEO hypotheses on each of its specified affine witnesses; a common domination, if used, remains a conditional geometric antecedent. Choose a very ample tensor qL with homogeneous sections z_i. Its principal charts Y_i have actual reference weights rho_i=q^(-1)max_j log|z_j/z_i|>=0. Then u_i=phi+rho_i has upper growth and the conditional affine theorem applies.

Use G on the ORIGINAL projective compactification X, with its actual section z_i and matching reference rho_i. For each rational c>1 this proves genuine membership in cL of the function phi-(c-1)rho_i on Y_i, minus infinity outside. At every analytic point one of the homogeneous coordinates attains the maximum; there rho_i=0. Therefore the maximum over all chart functions equals ORIGINAL phi on all of X^an, including minus infinity. Finite maxima and varying-class decreasing closure as c decreases to one prove phi in PSH(L).

This is conditional countable weak/global membership for the stated actual ample canonical reference. It does NOT show that every genuine resolved-nef potential is constant on the analytic fibers of a resolution, and so it supplies no singular EP by itself. Onto birational descent cannot be inferred from EP on the resolution: BJ5.13 needs approaching EP on the TARGET.

Evidence and reproduction: n1-trace.md and n2-affine-tools.md contain the required trace and elementary tools. Diagnostic Wu v1 LF1731--1814,1886--1964,2200--2696 and its envelope proof LF2697--2755 are pinned; their printed conclusions are not granted premises. The primary projection units are retained in web-primary-03.json and external-premises.json. Run python3 rerun.py for the complete paper, both TeX passes, hashes and finite documentary checks. All conclusions remain unverified drafts; the unchanged original P16.1 is not solved.


# n4. Exact equation domain, source audit, and the remaining gates

Candidate=false. The unchanged original P16.1 and its entire P16.2--P16.7 family remain exactly those preserved in task-original.json and input-original.json. The new countable conditional affine theorem does not replace the original arbitrary-cardinality singular/geometrically unibranch projective equation domain.

The retained equation domain is reduced irreducible geometrically unibranch projective X over an ARBITRARY algebraically closed trivially valued characteristic-zero field k, an ACTUAL ample rational line bundle L, every dimension, and positive Radon targets with arbitrary support and the intrinsic finite-dual-energy condition. Nothing here establishes arbitrary nontrivially valued fields, positive residue characteristic, nonample classes, proper nonprojective positivity, or nonalgebraizable spaces. The special contact class and GEO in n1--n3 remain binding assumptions of those intermediate results.

## What the new drafts establish and what is conditional

n1 reconstructs the whole-base trace-value application at every original analytic point under the accepted smooth gate's retained GEO antecedents. The base extension is constructed first on the original smooth normal base. Every normalized horizontal slice component, every residue degree and every canonical norm character is retained. Relative properness lifts the curves to the ONE original witness. Actual contraction coordinates and strict-disc radial limits include minus infinity; compactness covers the ENTIRE finite Gauss fiber. Original nonflat weights are recovered by equality of polynomial norm laws and complete-field regrouping, never by fiber dimensions.

n2 proves controlled approximation G for an ALREADY genuine AFS limit on a possibly singular variety, with original reference, whole collars, original generators, and no singular EP. Its finite-normalization pole repair replaces the false denominator-order claim by height-one bounds and ONE uniform f^M putting every power back in the ORIGINAL ring. Its entropy-grid approximation treats all coordinate faces, rational vertex heights/slopes, global errors, rational coefficient intervals, countable tails and summable shifts. Rossi and off-bad-set control use the ORIGINAL u's local regularizability; no subtraction of psh is used.

n3 gives the conditional countable-field split-piece proof with only locally constant integer branch sums, one shrunken controlled base neighborhood, raw positive weights, the factor c in the boundary gap, and a separate gamma=1 case. It proves descending Z, localization, genuine Runge exhaustion BEFORE strict coefficient radii, infinite radius values, original coefficient regularization, finite projection along a smooth stratum with EXACT U=pi^(-1)(S), singular-stratum induction, and the final EMPTY-Z local-to-global step. Products and maxima retain the original witness. The finite-projection geometry is reconstructed; GEO's other compactification/projective-domination/resolution applications are NOT independently discharged. A canonical ample-reference countable weak/global membership consequence is correspondingly conditional.

These are mathematical proof drafts, not independently reviewed results. No root86/root87 draft, printed Wu affine main theorem, printed Wu envelope conclusion, or arbitrary completed-residue-field regularization theorem was promoted to a premise. Task-granted round77/80 bodies are background assumptions, not registered native support IDs and not negative-index external premises.

## Genuine global operator and exact raw equation conventions

The task-granted global source audit of Boucksom--Jonsson, 1801.08229v4, is confirmed against its exact authorized primary text. Its convention permits reduced possibly nonnormal projective varieties; Section 7 resumes general projective scope. Relative integral closure of a test configuration is INSIDE its prescribed generic fiber, preserving that original nonnormal fiber. Its raw model measure is

\[
 \operatorname{MA}^{\rm raw}(\phi)
 =\sum_E b_E\bigl((\omega_{\mathcal X}+D)|_E\bigr)^n\delta_{v_E},
 \qquad b_E=\operatorname{ord}_E(t),\quad
 v_E=b_E^{-1}\operatorname{ord}_E|_{k(X)}.
\]

Central fundamental-cycle multiplicities, vertical DVRs, and the actual bundle are essential. The genuine mixed finite-energy pairing constructs positive Radon measures of raw mass V=(L^n), with genuine decreasing continuity. This is an existing genuine operator on general reduced projective varieties, not an inverse Banach-algebra measure construction.

Use the normalized energy

\[
 E_\omega(\phi)=\frac{\langle(\omega,\phi)^{n+1}\rangle}{(n+1)V},
 \qquad\mathcal E^1(\omega)=\{\phi\in\operatorname{PSH}(\omega):E_\omega(\phi)>-\infty\}.
\]

A raw target nu must be positive Radon with nu(X^an)=V. For mu=nu/V its precise energy requirement is

\[
 E_\omega^\vee(\mu)=\sup_{\psi\in\mathcal E^1}
       \left(E_\omega(\psi)-\int\psi\,d\mu\right)<\infty.
\]

BJ9.20 equates this with integrability of EVERY genuine finite-energy potential on irreducible X. There is no support restriction. BJ10.4 and 10.6 give uniqueness modulo one real constant and genuine domination without assuming EP. In dimension zero X is one point, V=1, and the empty product and constant ambiguity have their literal meaning.

The actual general-variety theorem is [BJ12.8](https://arxiv.org/pdf/1801.08229v4#page=121): onto finite-energy Monge--Ampere is equivalent to EP. Under EP, its variational proof uses normalized weak PSH compactness, a bounded-energy estimate, finite-energy target integral continuity (9.19), and upper semicontinuity of energy to obtain an ACTUAL maximizer. The differentiated envelope energy identifies its genuine measure. The raw functional VE_omega(phi)-integral phi dnu is constant invariant exactly at mass V. This proof cannot be replaced by an I-Cauchy sequence, an abstract completion, or approximate maximizers without attainment. Smooth EP on a resolution alone is not target EP.

Exact primary units retained include BJ LF435--469 (variety convention), LF3649--3692 (general scope), LF3980--4148 (operator/mass/decreasing continuity), LF5230--5304 (integral continuity and intrinsic energy), LF5440--5479 (uniqueness/domination), LF6092--6146 (actual EP/onto theorem and proof), LF6230--6268 (sequential regularization AFTER membership), and LF2859--2876 (target-side birational descent). Coordinates are inclusive one-based UTF8 bytes decode split('\n'). The catalogue manifest identifies any broader retained range containing these units; source files and literal bodies are preserved. These citations describe task-granted background, not a new singular existence assertion.

## Concrete indispensable gaps

1. GEO is still conditional in its stated applications: smooth ample-boundary compactifications and projective birational domination/resolution of the ONE original witness with matching actual references have not been proved here from exact primary geometric statements. The analytic deductions retain them rather than silently discharging them.

2. Genuine resolved-nef fiber-value descent has not been established. It requires constancy of every relevant genuine pulled-nef potential on all geometrically connected analytic fibers after EVERY completed residue-field extension, including minus infinity; actual varying-class references, restrictions through curve MORPHISMS, and minimum/usc descent must be checked. The affine theorem over countable k cannot be reapplied over arbitrary H(s). BJ5.13 cannot supply onto descent from EP on the smooth source: it requires approaching EP on the TARGET.

3. Singular countable EP is therefore not proved. [Wu2609.27610v1's envelope proof](https://arxiv.org/pdf/2609.27610v1#page=51), retained at LF2697--2755, explicitly calls its resolved-nef Proposition2.24 and weak/global Theorem6.5. n3 repairs a conditional version of the latter gate; it does not independently validate the former or the resulting envelope.

4. The original ARBITRARY-CARDINALITY field domain still requires finite-data obstacle/competitor descent and ascent. Relative integral closure must preserve the original nonnormal generic fiber, vertical R1/S2 behavior, component multiplicities, positive raw intersection masses, reference compatibility, orthogonality and domination. Different finite competitors can require different larger countable fields. An arbitrary collection of PSH competitors does not simultaneously descend merely because one finite model does.

5. Normalization/geometrically unibranch descent still requires approaching target-side EP, degree-one fundamental-cycle pairing projection, and compatibility of energies and the genuine E1/MA operator through unbounded limits. It is not enough to identify analytic point sets or continuous model measures.

6. Only after these gates can the actual singular envelope compactness/differentiation/attainment proof yield MA_raw(phi)=nu for EVERY prescribed finite-dual-energy raw mass-V target. The operator and uniqueness already available in general scope do not provide this missing existence assertion.

## Documentary execution, not correctness certification

The exact input bytes are preserved. The 23 authorized primary files and 54 exact LF units were hash checked and copied; public primary Stacks statement/proof snapshots are additionally retained with their own hashes, actual URLs and nonnegative premise indices. Web snapshot LF means the stored UTF8 tool-rendered text's LF coordinates, not imaginary source-HTML coordinates or an immutable Stacks edition. Cached arXiv/HAL versions remain exact. External-premises.json covers the external geometric/algebraic/radial facts used; task-granted full bodies are recorded separately as background.

Run python3 rerun.py in this workspace. It checks preservation and source/unit hashes, regenerates the complete argument and native notes/status, runs finite rational diagnostics, invokes the EXISTING Pandoc and pdfTeX twice, and saves commands, both pass logs, outputs, environment and artifact hashes. finite-checks.json declares exactly which finite cases were tested. These are finite observations only. No compilation, hash agreement, snapshot retention or finite check establishes mathematical correctness.

No other model/worker/subagent, installation, external message, source-cache edit, credential/auth/runtime/sandbox mutation, campaign/private/SQL/transcript read or heavy compute was used. The managed-runtime skill was read as required by higher-level environment instructions; its status tool was unavailable and no credential configuration was inspected. No supervised compute facility was exposed; none was needed or launched.

Artifacts: P16.1-argument.md, P16.1-paper.tex, P16.1-paper.pdf, n1-trace.md, n2-affine-tools.md, n3-runge-chain.md, n4-disposition.md, canonical-notes.json, status.json, source-extracts/source-provenance.json, external-premises.json, finite-checks.json, command-log.json, build-pass-1.log and build-pass-2.log. The unchanged mathematical target remains open in this deliverable, candidate=false.


# Exact unchanged task and full family

Original P16.1:
P16.1 (T5): Finite-energy equations on singular or unibranch varieties
Extend the ﬁnite-energy non-Archimedean Monge–Ampère operator and its existence-and-
uniqueness theorem to singular or unibranch varieties, replacing each use of smoothness in
compactness, envelopes, energy diﬀerentiation and comparison. State all retained polarization
and ﬁeld hypotheses.

Complete unchanged mathematical family:

10     The general non-Archimedean Monge–Ampère equation
Active items: P16.1, P16.2, P16.3, P16.4, P16.5, P16.6, P16.7. Status: Open in the
residual scope.

10.1    Atomic targets
P16.1 (T5): Finite-energy equations on singular or unibranch varieties
Extend the ﬁnite-energy non-Archimedean Monge–Ampère operator and its existence-and-
uniqueness theorem to singular or unibranch varieties, replacing each use of smoothness in
compactness, envelopes, energy diﬀerentiation and comparison. State all retained polarization
and ﬁeld hypotheses.

P16.2 (T5): Proper nonprojective algebraizable equation theories
Construct an appropriate replacement positivity datum and the associated psh, ﬁnite-energy,
comparison and equation theory on proper nonprojective algebraizable spaces. A proper
algebraic scheme with an ample line bundle is already projective, so retaining that datum
while dropping projectivity is not a new case.

P16.3 (T5): Finite-energy equations in positive residue characteristic
Construct the required ﬁnite-energy operator and prove existence and uniqueness when the
original residue-characteristic restriction is removed. Replace the resolution, model-regularity
and envelope inputs wherever they are used rather than merely changing the standing ﬁeld
hypothesis.

P16.4 (T4): Finite-energy equations over arbitrary complete valued ﬁelds
Extend the operator and existence theorem to nondiscrete valuations and arbitrary complete
non-Archimedean ﬁelds outside the established invariant-toric, skeleton-supported endpoint.
A deﬁnition of the ﬁnite-energy space alone does not establish the operator or the equation.

P16.5 (T5): Finite-energy equations for nonample positivity classes
Extend the equation theory to big or pseudoeﬀective nonample classes, specifying the psh cone,
reference singularity type, energy and total mass. At zero volume, the existing probability
normalization must be replaced rather than retained unchanged.

P16.6 (T4): Arbitrary-support ﬁnite-energy measures
Prove the operator and existence-and-uniqueness theorem for arbitrary ﬁnite-energy measure
support beyond the known toric skeletal regime. Measures must satisfy the correct mass and
energy conditions. Do not reduce arbitrary support to a single skeleton or replace the genuine
Monge–Ampère measure by another inverse measure construction.

P16.7 (T5): Finite-energy equations on nonalgebraizable analytic spaces
Construct the ﬁnite-energy operator and its existence-and-uniqueness theory on genuinely
nonalgebraizable analytic spaces, with an explicit positivity datum and the necessary com-
pactness, envelope and comparison replacements.




                                              73

10.2    What constitutes a solution
For each axis, state the retained hypotheses and construct the ﬁnite-energy operator together
with the corresponding existence-and-uniqueness theorem. Specify the measure mass and
ﬁnite-energy condition, uniqueness modulo constants and the replacement inputs for com-
pactness, envelopes, energy diﬀerentiation and comparison. An endpoint solving a special
toric measure class does not remove a general axis.

10.3    Full statement and detailed state of the art
Problem 10.1. Extend the ﬁnite-energy existence and uniqueness theory for the NA Monge–
Ampère equation beyond the currently proved combinations of smoothness, projectivity,
residue characteristic, valuation, positivity class, support, and algebraizability hypotheses.

    This is not one yes-or-no assertion. Positive characteristic, singular or unibranch varieties,
nondiscrete valuations, big classes, arbitrary support, and nonalgebraizable analytic spaces
require diﬀerent inputs. The known variational proofs use compactness, envelope regularity,
diﬀerentiability of energy, and a comparison principle; deleting a geometric hypothesis is valid
only after replacing every place where it enters. The relevant positive results and their distinct
domains are surveyed in Book Chapter 28, Book Chapter 29.
    The projectivity axis has one logical constraint. A proper algebraic K-scheme endowed
with an ample line bundle is already projective over K [Stacksb, Tag 0B5N]. Thus P16.2
cannot mean that one retains the BFJ line-bundle polarization L while simply deleting the
word “projective.” A nonprojective proper algebraizable extension must ﬁrst replace that
positivity datum—and then construct the corresponding psh, ﬁnite-energy, and comparison
theory—rather than merely rerun the original argument. No canonical replacement with the
required equation theory is asserted here.
    One exact source-stated axis is especially clean. Pille–Schneider observes that the ﬁnite-
energy space can be deﬁned over an arbitrary non-Archimedean ﬁeld, but that the extension of
the Monge–Ampère operator is not known there in general; the discretely valued characteristic-
zero and trivially valued cases are the established endpoints [PS23, Remark 4.4]. This should
be solved before bundling all remaining axes into a single theorem.

Proposition 10.1 (Arbitrary-ﬁeld invariant toric skeletal endpoint). Let K be a complete
nontrivially valued non-Archimedean ﬁeld, XΣ a proper toric K-variety, and L an ample toric
line bundle. If µ is a positive Radon measure on XΣan , is supported on the canonical skeleton
NΣ , gives zero mass to NΣ \NR , and has total mass degL (XΣ ), then there is a toric continuous
singular psh metric on L whose Monge–Ampère measure is µ. It is unique up to multiplication
of the metric by a positive constant.

    Thus nondiscreteness and the arbitrary complete ground ﬁeld cause no obstruction in
this invariant toric, skeleton-supported range. Here “continuous singular” has the source’s
extended-valued meaning: local weights are continuous into R ∪ {−∞}, as in [BGGJK25,
§5.3.1]. It does not imply ﬁnite real-valued weights or ﬁnite energy. This is not an arbitrary-
ﬁeld ﬁnite-energy theorem in the BFJ sense: the result permits a singular potential, requires
torus invariance and skeletal support, and does not construct the general extended Monge–
Ampère operator. In particular, P16.4 and P16.6 retain the respectively nonskeletal and
noninvariant ﬁnite-energy residual scopes.
    There is also a distinct, nonproper algebraic endpoint. Let n > d ≥ 1, let X be a smooth
projective Fano complex variety of dimension n, and let D be a reduced simple-normal-crossing
anticanonical divisor whose dual complex is the standard (d−1)-simplex. For the aﬃne Calabi–
Yau complement X = X \ D, Wang’s Theorem A constructs a continuous non-Archimedean
psh function on X an , over the trivially valued ﬁeld C, whose local Monge–Ampère measure

                                               74

is the canonical Lebesgue measure on the essential skeleton [Wan25]. The source is a version-
one preprint and uses a local CLD/tropical–convex construction. In particular, it neither
constructs the BFJ ﬁnite-energy operator nor treats arbitrary measures or arbitrary aﬃne
varieties. Since X is aﬃne and hence not proper, this endpoint does not answer P16.2; it
only records a special nonprojective algebraic solution after the properness requirement is
also dropped.
    There is a separate ﬁnite-atomic inverse statement which must not be called a ﬁnite-energy
Monge–Ampère theorem. Under its standing assumptions that K is maximally complete and
|K × | = R>0 , Fang ﬁxes an irreducible projective K-variety with an ample line bundle and a
ﬁnite set of graded birational points on its aﬃne cone. For every probability vector on that
ﬁnite set, the source constructs a Shilov-ﬁnite, possibly singular metric having the prescribed
equidistribution measure [Fan25, Proposition 4.8]. The source itself says that comparing this
Banach-algebra measure with the genuine Monge–Ampère measure requires the separate con-
tinuity property of an envelope metric. Thus it supplies neither a continuous semipositive
solution nor the BFJ ﬁnite-energy operator for the prescribed atomic measure, and does not
narrow P16.6.
    There is also a resolved negative regularity chronology. The ﬁrst skeletal-factorization
question of Gubler–Jell–Künnemann–Martin already fails on their toric surface [GJKM19,
Appendix A]. Boucksom–Jonsson then construct a ﬁnite atomic Monge–Ampère measure sup-
ported on a dual complex whose solution is invariant under no retraction attached to any
SNC model; they also construct a divisorial Green function that is not Q-PL [BJ24b, Theo-
rems A and B]. Hence support on a dual complex does not imply factorization through some
reﬁned skeleton. This is a theorem-level obstruction to a proof strategy, not an open regularity
expectation.
    The Rethlas programme treats each axis separately and ﬁrst searches the post-2020 liter-
ature for an existing theorem. Alterations and universal homeomorphisms can address some
algebraic descent questions, but they do not by themselves supply multiplier ideals or dif-
ferentiability in positive characteristic. The unrestricted formulation is open; several strictly
delimited axes are already known.




                                               75



## Exact completion criterion

Establish the genuine finite-energy operator, exact measure mass and energy condition, existence, uniqueness modulo constants, and every compactness/envelope/differentiation/comparison replacement for the singular/geometrically unibranch projective domain with explicitly retained field and polarization hypotheses. Verify the new envelope source and the actual general-variety global theory. No change to the original mathematical target is permitted.



END MATHEMATICAL DATA



BEGIN MATHEMATICAL DATA: Original context 19: Exact body accepted ONLY within actual89 scope; historical status statements are documentary

# Exact Rossi neighborhood repair; independently unreviewed

The actual round85 report is FAIL. No portion of author83 is promoted to an accepted theorem by that report. The new retained argument is the entire author83 argument with exactly one sentence changed: V is now explicitly a relatively compact open neighborhood of the tested z. Its old canonical notes, old paper and failed proof remain historical unchanged data, not assertions of the new retained body.

The missing condition is necessary. For trivially valued Qbar, L={the radius-one Gauss point at zero}, z=0 and V={|T-1|<1/2}, z lies in the original k[T] hull of L but outside V. Its boundary hull has |T-1| at most 1/2, whereas |T-1|(z)=1. Therefore the old conclusion is false. The repair excludes this counterexample by the essential antecedent z in V.

In the repaired proof, the glued maximum equals max(Cg0,log|f|-t) at z because z lies in V. The controlled g0 vanishes on a neighborhood of hull(L), so its value at z is zero. Strict separation gives log|f(z)|-t>0, while the glued function is zero on L because the compact closure of V is disjoint from L. The whole reference-winning boundary collar and all original-ring regularization inputs still require the precise accepted background; the added condition alone does not grant their mathematics.

Both uses retain the new antecedent. The off-bad-set proof chooses V around its finite maximum y; its boundary hull K_V is contained in hull(L), and Rossi is applied with tested y. The split-piece proof chooses V around x, with controlled compact closure inside pi^{-1}(N) intersect W_1 and disjoint from L; it applies Rossi with tested x. The original polynomial hull and compact controlled closures are kept.

Two binding clarifications apply throughout this new review. In a positive weighted sum, padding generator branches keeps their scaled positive logarithmic slopes: multiplying a log branch by positive c scales its slope by c; lowering a rational constant does not restore unit slope. Finite maxima/products still preserve the original generator data. Where a real additive normalization is used while the local contact convention requires rational constants, take decreasing rational shifts converging to that real value and flatten with rational shifts. Limits, same constants in equality contacts, original references and all minus-infinity values remain unchanged.

The full n1/n2/n3 chain and its projective canonical-reference consequence must be independently reconstructed again. Actual round87 provides only its exact geometric witness construction and countable net-to-sequence scope with its binding clarification; its application to every witness here must be checked. Actual round80 grants only the precise round77 partial background and errata. Resolved-nef all-point fiber descent, first target membership, target EP and the original equation are not granted. This fresh repair is not hot feedback to pending review88, does not alter any prior frozen input, and does not close original P16.1.



END MATHEMATICAL DATA



BEGIN MATHEMATICAL DATA: Original context 20: PRIMARY exact join unit or its source binding and reading limits

               XF
                 NORMS, DETERMINANT OF COHOMOLOGY AND FEKETE POINTS                               55

by (7.1). By Theorem 6.6, m−1 d∞ (k · kmφF , (k · kmφ )F ) → 0, and are done.                     

Part 3. Asymptotics of relative volumes
                  8. Monge–Ampère measures and Deligne pairings
   In this section, we review some basic properties of Monge–Ampère operators, and use them
to define metrics on Deligne pairings (Theorem 8.16), following Deligne’s program [Del87].
In what follows, X is as before an n-dimensional projective scheme over a complete valued
field K.
8.1. Mixed Monge–Ampère measures. The (algebraic) fundamental class of X is the
n-dimensional cycle               X
                            [X] =   mα [Xα ],
                                                     α
where the Xα denote the n-dimensional irreducible components of X (with their reduced
structure) and mα is the length of the local ring of X at the generic point of Xα . The
intersection number of Q-line bundles L1 , . . . , Ln on X is defined as
                      (L1 · . . . · Ln ) := deg π⋆ (c1 (L1 ) · . . . · c1 (Ln ) · [X]) ,
with π : X → Spec K the structure morphism.
  Now let φ1 , . . . , φn be smooth metrics on L1 , . . . , Ln , and recall that ddc φi denotes the
curvature form of φi , a smooth, closed (1, 1)-form on X an (cf. [CLD12, §6.4.1] for the non-
Archimedean case). The smooth (n, n)-form ddc φ1 ∧. . .∧ddc φn determines a Radon measure
                                               X
                ddc φ1 ∧ . . . ∧ ddc φn ∧ δX =   mα ddc φ1 ∧ . . . ∧ ddc φn ∧ δXα             (8.1)
                                       α
                          an
on the topological space X , the mixed Monge–Ampère measure     of the φi , with δX =
P
  α m  δ
      α Xα denoting the analytic fundamental class of X (see [CLD12,  §3.7] for the non-
Archimedean case).
Remark 8.1. When K = R, we define ddc φ1 ∧ . . . ∧ ddc φn ∧ δX as the image of the
corresponding measure on X(C) = XCan by the projection map XCan → X an .
Example 8.2. Assume that n = 0, i.e. X = Spec A with A a finite K-algebra. The pre-
vious construction produces a positive measure δX on Q    the finite set X an , which is described
as follows. We have a product decomposition A = i Ai into local finite K-algebras Ai
corresponding to the connected components of X. The (reduced) irreducible components of
X are given by Xi = Spec Ki , where the residue field Ki of Ai is a finite extension of K,
and the uniquePextension of the absolute value of K to Ki defines a point xi ∈ X an . The
current δX = i mi δXi is a measure on X an , and the requirement that δXi has total mass
deg π⋆ [Xi ] = [Ki : K] yields δXi = [Ki : K]δxi . As mi [Ki : K] = dimK Ai , we conclude that
                                           X
                                     δX =     (dimK Ai )δxi .
                                                 i

Proposition 8.3. For each tuple φ1 , . . . , φn of smooth metrics on Q-line bundles L1 , . . . , Ln ,
the mixed Monge–Ampère measure ddc φ1 ∧ . . . ∧ ddc φn ∧ δX satisfies the following properties:
    (i) it is a symmetric, multilinear function of the φi , and a positive Radon measure if
        the φi are semipositive, i.e. ddc φi ≥ 0;
56                         SÉBASTIEN BOUCKSOM AND DENNIS ERIKSSON
           R
      (ii) ddc φ1 ∧ . . . ∧ ddc φn ∧ δX = (L1 · . . . · Ln );
     (iii) if L0 = L1 = OX (and hence φ0 , φ1 are smooth functions on X an ), then
      Z                                              Z
          φ0 dd φ1 ∧ dd φ2 ∧ . . . ∧ dd φn ∧ δX = φ1 ddc φ0 ∧ ddc φ2 ∧ . . . ∧ ddc φn ∧ δX .
               c        c              c
                                                                                               (8.2)

     (iv) for any complete field extension F/K, we have
                 p⋆ (ddc φ1,F ∧ . . . ∧ ddc φn,F ∧ δXF ) = ddc φ1 ∧ . . . ∧ ddc φn ∧ δX ,
         where φi,F is the pullback of φi to Li,F and p : XFan → X an is the canonical projection.
Proof. (i) is straightforward. (ii) is classical in the Archimedean case, and proved in [CLD12,
Proposition 6.4.3] in the non-Archimedean case. (iii) is a consequence of the Stokes formula
(see [CLD12, Théorème 3.12.2] in the non-Archimedean case). In the Archimedean case, (iv)
is nontrivial only when K = R, F = C, in which case it holds by definition (see Remark 8.1).
In the non-Archimedean case, it is implicit in [CLD12], and can be checked as follows. Pick
a smooth, compactly supported function f on X an , and consider the smooth, compactly
supported (n, n)-form α := f ddc φ1 ∧ . . . ∧ ddc φn . According to [Gub16, Proposition 5.13],
there exists a Zariski open subset U ⊂ X with a closed embedding U ֒→ Grm,K and a
compactly supported smooth (n, n)-superform on Rr such that α is obtained by pulling-
back η by the tropicalization map Trop : U an → Rr , and
                             Z                                  Z
                                      c              c
                                f dd φ1 ∧ · · · ∧ dd φn ∧ δX =     α
                                                                          X
is defined as the integral of η on the tropical cycle Trop(U ). Unravelling the definitions, it
is clear that the pull-back αF of α to XFan is simply the pull-back of η by the tropicalization
map TropF : UFan → Rr . The construction of the tropical cycle of an algebraic variety being
invariant under ground field extension,
                                  R       Rwe have TropF (UF ) = Trop(U ) as tropical cycles,
and we conclude as desired that X α = XF αF .                                                 
   Recall from §7.3 that a continuous metric on a Q-line bundle L is psh-regularizable iff it is
a uniform limit of smooth semipositive metrics on L. If L is semiample, then any continuous
psh metric (in the sense of Definition 7.2, i.e. a uniform limit of Fubini–Study metrics) is
psh-regularizable, by Theorem 7.14.
Theorem 8.4. Let L1 , . . . , Ln be Q-line bundles on X. The measure-valued operator
                             (φ1 , . . . , φn ) 7→ ddc φ1 ∧ . . . ∧ ddc φn ∧ δX ,
defined so far on smooth metrics, admits a unique continuous extension to tuples of contin-
uous, psh-regularizable metrics on the Li , with respect to uniform convergence for tuples of
metrics, and the weak topology on Radon measures.
     As a direct consequence of Proposition 8.3, we get:
Proposition 8.5. For each tuple of continuous, psh-regularizable metrics (φi ),
                                            X
             ddc φ1 ∧ . . . ∧ ddc φn ∧ δX =   mα ddc φ1 ∧ . . . ∧ ddc φn ∧ δXα
                                                     α

is a positive Radon measure on X an , of total mass (L1 · . . . · Ln ). It is further symmetric
and multiadditive as a function of the φi .
                    NORMS, DETERMINANT OF COHOMOLOGY AND FEKETE POINTS                                          57

   Theorem 8.4 follows from the classical Bedford–Taylor theory [BT76] in the Archimedean
case, and from its analogue in the non-Archimedean case [CLD12, Corollaire 5.6.5]. In the
present global setting, one can however provide a simple direct argument, based on the
following global version of the classical Chern–Levine–Nirenberg inequality that will be put
to use again a bit later.
Lemma 8.6. Let L0 , . . . , Ln be line bundles on X, and suppose given a pair of smooth,
semipositive metrics φi , φ′i on each Li . Then
       Z                                            Z
          (φ0 − φ′0 ) ddc φ1 ∧ . . . ∧ ddc φn ∧ δX − (φ0 − φ′0 ) ddc φ′1 ∧ . . . ∧ ddc φ′n ∧ δX

                                                  n
                                                  X
                                           ≤C           sup |φi − φ′i |
                                                  i=1

with C := 2 max1≤i≤n (L0 · L1 · . . . · Lbi · . . . · Ln ).
Proof. For brevity of notation, set T := ddc φ2 ∧ . . . ∧ ddc φn ∧ δX . By (8.2),
       Z                         Z                          Z
         (φ0 − φ′0 ) ddc φ1 ∧ T − (φ0 − φ′0 ) ddc φ′1 ∧ T = (φ0 − φ′0 ) ddc (φ1 − φ′1 ) ∧ T
          Z                                       Z                              Z
      =       (φ1 − φ′1 ) ddc (φ0 − φ′0 ) ∧ T =       (φ1 − φ′1 ) ddc φ0 ∧ T +       (φ1 − φ′1 ) ddc φ′0 ∧ T.

Since ddc φ0 ∧ T and ddc φ′0 ∧ T are both positive measures of mass (L0 · L2 · . . . · Ln ), we infer
     Z                          Z
       (φ0 − φ0 ) dd φ1 ∧ T − (φ0 − φ′0 ) ddc φ′1 ∧ T ≤ 2(L0 · L2 · . . . · Ln ) sup |φ1 − φ′1 |.
                ′   c


We conclude by symmetry and multilinearity.                                                                     
Proof of Theorem 8.4. Assume first that K is non-Archimedean, and pick f ∈ PLR (X an ).
By Lemma 5.17, we can find a pair of Fubini–Study metrics on an ample line bundle L0 such
that f = φ0 − φ′0 . By Theorem 7.14, φ0 and φ′0 are uniform limits of smooth, semipositive
metrics on L0 . Lemma 8.6 thus shows that
                                             Z
                        (φ1 , . . . , φn ) 7→ f ddc φ1 ∧ . . . ∧ ddc φn ∧ δX

is Lipschitz continuous with respect to the supnorm on tuples of smooth, semipositive met-
rics (with Lipschitz constant depending on f ), and hence extends continuously to tuples of
continuous, psh-regularizable metrics. For eachR tuple of continuous, psh-regularizable met-
rics (φi ), the linear form on PLR (X an ) f 7→ f ddc φ1 ∧ . . . ∧ ddc φn ∧ δX is positive, hence
continuous, and it thus extends to a positive linear form on C0 (X), by density of PLR (X an ).
   In the Archimedean case, the argument is similar, arguing with a smooth function f
instead. It is in fact even simpler, since f can directly be written as a difference of smooth
psh metrics on some ample line bundle.                                                         
   In order to exploit the multilinearity of the previous construction, it is convenient to
introduce the following terminology.
Definition 8.7. We say that a continuous metric φ on a line bundle L is dpsh if it can be
written as a difference of continuous, psh-regularizable metrics.
58                        SÉBASTIEN BOUCKSOM AND DENNIS ERIKSSON

     A dpsh metric is thus the same as an approachable metric in the sense of [CLD12, §6.3].
Lemma 8.8. Every line bundle L admits a smooth, dpsh metric.
Proof. By Theorem 7.14, any ample line bundle admits a smooth, semipositive metric, and
the result follows since L can be written as a difference of ample line bundles.      
Example 8.9. If K is Archimedean, every smooth metric is dpsh.
   While this is probably true in the non-Archimedean case as well, it is less obvious, since
strictly positive (1, 1)-forms do not exist globally in this context.
Example 8.10. If K is non-Archimedean, every R-PL metric is dpsh, by Lemma 5.17.
   The operator (φ1 , . . . , φn ) 7→ ddc φ1 ∧. . .∧ddc φn ∧δX , being symmetric and multiadditive on
tuples of continuous, psh-regularizable metrics, extends to a symmetric, multilinear operator
on continuous dpsh metrics, with values in signed Radon measure. Note that Proposition 8.3
still holds for such metrics.


END MATHEMATICAL DATA



BEGIN MATHEMATICAL DATA: Original context 21: PRIMARY exact join unit or its source binding and reading limits

with m ∈ Z>0 such that mL is an honest line bundle, (sj ) a finite set of sections of
H0 (X, mL), and λj ∈ Λ. (Recall that (2.8) means ϕ(v) = m−1 maxj {−v(sj ) + λj } for
all v ∈ X an ). Using Lemma 1.4, the next result is straightforward:
Lemma 2.17. Every function ϕ : X an → R ∪ {−∞} of the form (2.8) is continuous, de-
creasing, and satisfies B(L)(k) ⊂ {ϕ = −∞}. Furthermore, the following are equivalent:
     (i) ϕ is generically finite, i.e. ϕ|Xαan 6≡ −∞ for all α (see Definition 1.3);
    (ii) ϕ is finite at vtriv,α for all α (see §1.1.5);
   (iii) ϕ is finite valued on X val .
Definition 2.18. Given a subgroup Λ ⊂ R and a Q-line bundle L on X, we say that a
function ϕ : X an → R ∪ {−∞} is
    (i) a Λ-rational, generically finite Fubini–Study function for L if ϕ is of the form (2.8)
        and generically finite, i.e. finite valued on X val (see Lemma 2.17);
   (ii) a Λ-rational Fubini–Study function for L if ϕ is further finite valued on all of X an .
                       gf
We denote by HΛ (L) ⊂ HΛ  (L) the spaces so defined.
  Note that these sets only depend on the isomorphism class of L, i.e. its image in Pic(X)Q .
Further,
                                            gf
                                HΛ (L) = HΛ    (L) ∩ C0 (X).
For any ϕ as in (2.8), we have
                                ϕ = (rm)−1 max{log |srj | + rλj }                          (2.9)
                                                 j

for all r ∈ Z>0 . Thus
                             gf        gf
                            HΛ  (L) = HQΛ (L),       HΛ (L) = HQΛ (L),                   (2.10)
which means that the subgroup Λ ⊂ R can always be assumed to be divisible in the above
definition. Finally, we trivially have
                  H0gf (L) ⊂ HΛ
                              gf        gf
                                 (L) ⊂ HR  (L),      H0 (L) ⊂ HΛ (L) ⊂ HR (L).
These sets can be empty; more precisely, it is straightforward to check that
                           gf
                          HR  (L) 6= ∅ ⇐⇒ H0gf (L) 6= ∅ ⇐⇒ L effective;                  (2.11)
                         HR (L) 6= ∅ ⇐⇒ H0 (L) = {0} ⇐⇒ L semiample.                     (2.12)
26                        SÉBASTIEN BOUCKSOM AND MATTIAS JONSSON

The next result summarizes further properties that are also readily checked (compare [BE20,
Proposition 5.4]).
Proposition 2.19. Pick any L ∈ Pic(X)Q . Then:
                        gf
       (i) each ϕ ∈ HΛ     (L) is decreasing on X an , and hence satisfies the maximum princi-
           ple (1.4) (see Lemma 1.4); further, ϕ ≡ −∞ on B(L)an ;
             gf
      (ii) HΛ   (L) and HΛ (L) are both invariant under the scaling action (1.3) restricted to the
           subgroup {t ∈ R>0 | tΛ ⊂ Λ} of R>0 ;
     (iii) for all L0 ∈ Pic(X)Q and a ∈ Q>0 we have
                     gf          gf           gf        gf          gf
                    HΛ  (aL) = aHΛ  (L),     HΛ  (L) + HΛ  (L0 ) ⊂ HΛ  (L + L0 ),
          and similarly for HΛ ;
     (iv) for any morphism f : Y → X from a projective variety we have
                                      f ? HΛ (L) ⊂ HΛ (f ? L),
                                  gf
          and the same holds for HΛ  if f is surjective.
               gf
     When ϕ ∈ HΛ  (L) is written as in (2.8), the scaling action in (ii) is simply given by
                                 t · ϕ = m−1 max{log |sj | + tλj }.
                                                j

For any v ∈ X an , we similarly have
                                ϕ(tv) = m−1 max{−tv(sj ) + λj },
                                                 j

which yields:
                         gf
Lemma 2.20. For any ϕ ∈ HR  (L) and v ∈ X an , t 7→ ϕ(tv) is convex and decreasing on
R>0 .
   Proposition 2.19 (iv) admits the following partial converse, a key ingredient in the proof
of Theorem 4.32 below.


END MATHEMATICAL DATA



BEGIN MATHEMATICAL DATA: Original context 22: PRIMARY exact join unit or its source binding and reading limits

Proof of Theorem 4.7. We will repeatedly use Proposition 2.19. Pick ϕ ∈ PSH(θ), ϕ0 ∈
PSH(θ0 ). As ϕ and ϕ0 are finite on vtriv,α for all α, so is the function ϕ+ϕ0 , which is therefore
generically finite. Further, ϕ and ϕ0 can be written as the limits of decreasing nets (ϕi )i∈I
                             gf               gf
and (ϕ0j )j∈I 0 with ϕi ∈ HR    (Li ), ϕ0j ∈ HR  (L0j ) for Li , L0j ∈ Pic(X)Q such that limi c1 (Li ) = θ
and limj c1 (L0j ) = θ0 , respectively. The net (ϕi + ϕ0j )(i,j)∈I×I 0 is decreasing, and converges
                                              gf
pointwise to ϕ + ϕ0 . Now ϕi + ϕ0j ∈ HR          (Li + L0j ), and hence ϕ + ϕ0 ∈ PSH(θ + θ0 ), since
                          0           0
lim(i,j) (c1 (Li ) + c1 (Lj )) = θ + θ . This proves the first inclusion in (i).
                                                                  gf
    For any c ∈ R and t ∈ R>0 , ϕi + c and t · ϕi belong to HR       (Li ), and decrease, respectively,
to ϕ + c and t · ϕ, which therefore belong to PSH(θ).
    We next show that tϕ ∈ PSH(tθ). If t is rational, this is clear, since each tLi is a Q-line
                   gf
bundle, tϕi ∈ HR      (tLi ) and tϕi & tϕ. In the general case, we may assume, after replacing ϕ
with ϕ − sup ϕ, that ϕ ≤ 0. Writing t as the limit of an increasing sequence tm ∈ Q>0 , we
then have tm ϕ ∈ PSH(tm θ) and tm ϕ & tϕ, tm θ → tθ, and hence tϕ ∈ PSH(tθ), by (PSH2).
This concludes the proof of (i), which implies that PSH(θ) is convex.
    To prove that PSH(θ) is stable under maxima, pick ϕ, ϕ0 ∈ PSH(θ). By Lemma 4.9, we
                                                        gf
can find a net (Li ) of Q-line bundles and ϕi , ϕ0i ∈ HR   (Li ) such that limi c1 (Li ) → θ, ϕi & ϕ,
                                      gf
ϕi & ϕ . Then max{ϕi , ϕi } ∈ HR (Li ) decreases to max{ϕ, ϕ0 }, which therefore belongs to
  0      0                     0

PSH(θ).
    If a net in PSH(θ) converges uniformly to a function ψ : X an → R ∪ {−∞}, then ψ is
generically finite, and is also the uniform limit of a sequence (ψm ) in PSH(θ). After passing
to a subsequence, it is then easy to find constants cm → 0 such that (ψm + cm ) is decreasing,
and we infer ψ ∈ PSH(θ), by (PSH2). This concludes the proof of (ii).
                                                                                                  gf
    Next we prove (iii). Write ϕ ∈ PSH(θ) as the decreasing limit of a net ϕi ∈ HR                   (Li )
                                                     gf                           ?        gf ?
such that limi c1 (Li ) → θ. Then each ϕi ∈ HR (Li ) satisfies either f ϕi ∈ HR (f Li ) or
f ? ϕi ≡ −∞ on some irreducible component of Y an . If f ? ϕ is generically finite, then the
latter case never occurs, since f ? ϕ ≤ f ? ϕi . Since f ? ϕi & f ? ϕ and c1 (f ? Li ) → f ? θ, (PSH2)
yields f ? ϕ ∈ PSH(f ? θ).
    Finally, (iv) follows from (iii) since ϕ is generically finite.                                    
Corollary 4.10. Pick θ ∈ N1 (X), ϕ, ψ ∈ PSH(θ) with ϕ ≤ ψ, and let χ : (−∞, 0] → R be
a continuous convex function such that 0 ≤ χ0 ≤ 1. Then χ ◦ (ϕ − ψ) + ψ ∈ PSH(θ).
Proof. Note that χ ◦ (ϕ − ψ) + ψ is generically finite. Now, χ can be written as a decreasing
limit of functions χm that are finite maxima of affine functions of the form `(t) = at + b,
where a ∈ [0, 1] and b ∈ R. For each m, χm ◦ (ϕ − ψ) + ψ is a finite maximum of functions
of the form ` ◦ (ϕ − ψ) + ψ = (1 − a)ψ + aϕ + b, and hence χm ◦ (ϕ − ψ) + ψ ∈ PSH(θ), by
Theorem 4.7. Now χm ◦ (ϕ − ψ) + ψ & χ ◦ (ϕ − ψ) + ψ, and the result follows, by (PSH2). 
Corollary 4.11. If θ ∈ Nef(X) and 0 ≥ ϕ ∈ PSH(θ), then exp(ϕ) ∈ E ∞ (θ).
             GLOBAL PLURIPOTENTIAL THEORY OVER A TRIVIALLY VALUED FIELD                       49

   Indeed, we can pick ψ = 0 (since θ is nef, see (4.2)). This corollary will allow us to reduce
certain statements about general θ-psh functions to the case of bounded ones.


END MATHEMATICAL DATA



BEGIN MATHEMATICAL DATA: Original context 23: PRIMARY exact join unit or its source binding and reading limits

for all E. We need to show that the polar scheme P of a is empty. Suppose this is not the
case, and pick an associated point ξ of P . By Lemma 1.19 (ii), ξ is the generic point of some
component E of X0 , and the assumption ordE (a) ≥ 0 thus yields aξ ⊂ OX ,ξ , i.e. ξ ∈   / P, a
contradiction.                                                                               
1.5. Valuations of linear growth. Let L be a line bundle on X. A semivaluation v ∈ X an
can be naturally evaluated on any section s ∈ H0 (X, L), by defining v(s) as the value of v on
the germ in OX corresponding to s in any local trivialization of L at the center of v. Thus
v(s) ∈ [0, +∞], v(s) = ∞ iff s vanishes along the support of v, and v(s) > 0 iff s vanishes
at the center of v. Setting |s|(v) := e−v(s) defines a continuous function |s| : X an → [0, 1].
Remark 1.24. This construction reflects the existence of the trivial metric | · | of Lan , a
continuous metric characterized by |τ | ≡ 1 on the compact set c−1 (U ) for any trivializing
section τ ∈ H0 (U, L) on an open subset U ⊂ X.
  In what follows, we fix an ample line bundle L on X.
Lemma 1.25. A semivaluation v ∈ X an is a valuation iff v(s) < +∞ for all regular sections
s ∈ H0 (X, mL), m ∈ N.
Proof. Suppose v ∈/ X val , so that its support Y ⊂ X is not an irreducible component of X.
Since L is ample, we can find for m  1 a nonzero section s ∈ H0 (X, mL) that vanishes
along Y , but not along any irreducible component of X. Then s is regular, and v(s) = ∞.
The converse direction is clear.                                                         
  Following [BKMS15, BlJ20], we introduce:
Definition 1.26. The maximal vanishing order of L at v ∈ X an is defined as
           TL (v) = sup m−1 v(s) | m ≥ 1, s ∈ H0 (X, mL) regular ∈ [0, +∞].
                       

We say that v has linear growth if TL (v) < +∞, and denote by X lin the corresponding
subset of X an .
   The linear growth condition is easily seen to be independent of the choice of an ample
line bundle L. By Lemma 1.25, we have X lin ⊂ X val , and the inclusion is strict in gen-
eral [BKMS15, Example 2.19]. We will later interpret X lin as the set of nonpluripolar points
of X an , cf. Proposition 4.38 below.
Lemma 1.27. Pick an irreducible component Xα of X, and set Lα := L|Xα . For each
v ∈ Xαan ⊂ X an we then have TLα (v) = TL (v). In particular,
                                             a
                                     X lin =    Xαlin .
                                               α

Proof. Since the restriction to Xα of a regular section on X is regular, we trivially have
TLα (v) ≥ TL (v). Conversely pick a nonzero section s ∈ H0 (Xα , mLα ). For r  1, sr
extends to a regular section s̃ ∈ H0 (X, rmL). Then rv(s) = v(sr ) = v(s̃) ≤ TL (v)mr, and


END MATHEMATICAL DATA



BEGIN MATHEMATICAL DATA: Original context 24: PRIMARY exact join unit or its source binding and reading limits

{
  "recorded_utc": "2026-10-05T11:24:20.190255+00:00",
  "proposals": [
    {
      "path": "/workspace/research/root-checks/P16.1-countable-first-membership-join-interface-20261005-continuation94.md",
      "sha256": "61c5443c8a59055a89d43cd10f51665fccf17c721b2698c2e396fd57e5f5ffc9",
      "whole_current_proposal_root_read": true,
      "accepted_dependency": false,
      "original_closed": false
    },
    {
      "path": "/workspace/research/root-checks/P16.1-smooth-fixed-bundle-current-proof-20261005-continuation95.md",
      "sha256": "3eaa82155efeb5dcf06cc2fd90680df71c787dab45347905c75a5a9d44b4ced6",
      "whole_current_proposal_root_read": true,
      "accepted_dependency": false,
      "original_closed": false
    }
  ],
  "units": [
    {
      "source": "/workspace/research/shared-sources/P16-arxiv-1801.08229-20261004.txt",
      "source_sha256": "659bb8d2e5335781041f03cdb168bac70126487bc0db394f3dac8cf1e9f076d0",
      "url": "https://arxiv.org/pdf/1801.08229v4",
      "inclusive_one_based_LF": [
        882,
        920
      ],
      "literal_file": "/workspace/research/root-checks/continuation94-95-interface-primary-read-units/BJ-1801.08229v4-LF882-920.txt",
      "literal_sha256": "f0bf826b71461d5db65319739cf1ee9a4fdebaa35146bec9e0ae705d6647262d",
      "whole_pertinent_unit_root_read": true,
      "whole_source_file_root_read": false,
      "all_recursive_primary_proofs_root_read": false
    },
    {
      "source": "/workspace/research/shared-sources/P16-arxiv-1801.08229-20261004.txt",
      "source_sha256": "659bb8d2e5335781041f03cdb168bac70126487bc0db394f3dac8cf1e9f076d0",
      "url": "https://arxiv.org/pdf/1801.08229v4",
      "inclusive_one_based_LF": [
        1174,
        1242
      ],
      "literal_file": "/workspace/research/root-checks/continuation94-95-interface-primary-read-units/BJ-1801.08229v4-LF1174-1242.txt",
      "literal_sha256": "deb3974526b8f2cda45979b634c74562b57bd092f1e138b255b8ed998c39f9e7",
      "whole_pertinent_unit_root_read": true,
      "whole_source_file_root_read": false,
      "all_recursive_primary_proofs_root_read": false
    },
    {
      "source": "/workspace/research/shared-sources/P16-arxiv-1801.08229-20261004.txt",
      "source_sha256": "659bb8d2e5335781041f03cdb168bac70126487bc0db394f3dac8cf1e9f076d0",
      "url": "https://arxiv.org/pdf/1801.08229v4",
      "inclusive_one_based_LF": [
        2330,
        2380
      ],
      "literal_file": "/workspace/research/root-checks/continuation94-95-interface-primary-read-units/BJ-1801.08229v4-LF2330-2380.txt",
      "literal_sha256": "39deb0230b013306eaf995949df6259ab3f3d3fdd8e79820d856979b7f44caf5",
      "whole_pertinent_unit_root_read": true,
      "whole_source_file_root_read": false,
      "all_recursive_primary_proofs_root_read": false
    },
    {
      "source": "/workspace/research/shared-sources/P16-arxiv-1805.01016-20261004.txt",
      "source_sha256": "8e584521fe3d41f179bef93d14315414ac7796532c65518c1861717416f99233",
      "url": "https://arxiv.org/pdf/1805.01016v3",
      "inclusive_one_based_LF": [
        2605,
        2767
      ],
      "literal_file": "/workspace/research/root-checks/continuation94-95-interface-primary-read-units/BE-1805.01016v3-LF2605-2767.txt",
      "literal_sha256": "b3ca837f0e204e91b74ad39ed2be8d6485cfa92573d504a70747f9c4642fcdfa",
      "whole_pertinent_unit_root_read": true,
      "whole_source_file_root_read": false,
      "all_recursive_primary_proofs_root_read": false
    }
  ],
  "author83_interface_reread_inclusive_LF": [
    [
      1,
      31
    ],
    [
      297,
      315
    ],
    [
      365,
      378
    ]
  ],
  "scope": "Only pertinent source bodies read. The first-membership join retains pending F and C; the direct smooth-current proof is new unreviewed mathematics, not feedback to pending88."
}



END MATHEMATICAL DATA



BEGIN MATHEMATICAL DATA: Original context25 primary catalogue: losslessly factored literal strings
{
  "sources": [
    {
      "id": "S1",
      "version": "1801.08229v4",
      "title": "[1801.08229] Global pluripotential theory over a trivially valued field",
      "public_source": "https://arxiv.org/pdf/1801.08229v4",
      "files": [
        {
          "authorized_path": "/workspace/research/shared-sources/P16-arxiv-1801.08229-20261004.pdf",
          "local_copy": "sources/S1-pdf.pdf",
          "sha256": "8d5975337f4ac88a475929ea6a436ec4a15d08715d5582bc0ba0eb3e07152c52",
          "bytes": 1627763,
          "expected_sha256": "8d5975337f4ac88a475929ea6a436ec4a15d08715d5582bc0ba0eb3e07152c52"
        },
        {
          "authorized_path": "/workspace/research/shared-sources/P16-arxiv-1801.08229-20261004.txt",
          "local_copy": "sources/S1-literal_extract.txt",
          "sha256": "659bb8d2e5335781041f03cdb168bac70126487bc0db394f3dac8cf1e9f076d0",
          "bytes": 506945,
          "expected_sha256": "659bb8d2e5335781041f03cdb168bac70126487bc0db394f3dac8cf1e9f076d0",
          "LF_count": 7228,
          "coordinate_rule": "UTF-8 bytes decode; split('\\n'); inclusive one-based"
        },
        {
          "authorized_path": "/workspace/research/shared-sources/P16-arxiv-1801.08229-20261004.html",
          "local_copy": "sources/S1-abstract_html.html",
          "sha256": "680fc70f252a7203bf277dccb65c9fddf4f0725c387d2b41b64d467f087c2304",
          "bytes": 39270,
          "expected_sha256": "680fc70f252a7203bf277dccb65c9fddf4f0725c387d2b41b64d467f087c2304"
        }
      ]
    },
    {
      "id": "S2",
      "version": "2609.27610v1",
      "title": "Lyuhui Wu, On the local theory of non-archimedean psh functions",
      "public_source": "https://arxiv.org/pdf/2609.27610v1",
      "files": [
        {
          "authorized_path": "/workspace/research/shared-sources/new-primary-2609.27610v1-20261004.pdf",
          "local_copy": "sources/S2-pdf.pdf",
          "sha256": "11808a6c9ede9c0158b27e16700fc180a4ac8df12a4586a7178e1958e8f6bba8",
          "bytes": 845301,
          "expected_sha256": "11808a6c9ede9c0158b27e16700fc180a4ac8df12a4586a7178e1958e8f6bba8"
        },
        {
          "authorized_path": "/workspace/research/shared-sources/new-primary-2609.27610v1-20261004.txt",
          "local_copy": "sources/S2-literal_extract.txt",
          "sha256": "c8ffe91a631da67f6d3872a1a06ab8d15755aed2f926cdf326725ca3662cef7d",
          "bytes": 216006,
          "expected_sha256": "c8ffe91a631da67f6d3872a1a06ab8d15755aed2f926cdf326725ca3662cef7d",
          "LF_count": 2912,
          "coordinate_rule": "UTF-8 bytes decode; split('\\n'); inclusive one-based"
        },
        {
          "authorized_path": "/workspace/research/shared-sources/new-primary-2609.27610-20261004.html",
          "local_copy": "sources/S2-abstract_html.html",
          "sha256": "fb78c30f3021e7683a23b91fc2e967cc7a1f3777eb8f083c20823a73d67b663e",
          "bytes": 38722,
          "expected_sha256": "fb78c30f3021e7683a23b91fc2e967cc7a1f3777eb8f083c20823a73d67b663e"
        }
      ]
    },
    {
      "id": "S3",
      "version": "1204.6277v2",
      "title": null,
      "public_source": "https://arxiv.org/pdf/1204.6277v2",
      "files": [
        {
          "authorized_path": "/workspace/research/shared-sources/new-primary-1204.6277v2-20261004-continuation64.pdf",
          "local_copy": "sources/S3-pdf.pdf",
          "sha256": "5690f999523017d184ab751bb55857ab1637b197d1186ad4fd2edba7e1bda719",
          "bytes": 4659053,
          "expected_sha256": "5690f999523017d184ab751bb55857ab1637b197d1186ad4fd2edba7e1bda719"
        },
        {
          "authorized_path": "/workspace/research/shared-sources/new-primary-1204.6277v2-20261004-continuation64.txt",
          "local_copy": "sources/S3-literal_extract.txt",
          "sha256": "64846cb00926267c6238d1afac61b5eaed0a0e3a6349725738f9b1bf163de085",
          "bytes": 2153101,
          "expected_sha256": "64846cb00926267c6238d1afac61b5eaed0a0e3a6349725738f9b1bf163de085",
          "LF_count": 31019,
          "coordinate_rule": "UTF-8 bytes decode; split('\\n'); inclusive one-based"
        }
      ]
    },
    {
      "id": "S4",
      "version": "1608.08030v3",
      "title": "Walter Gubler and Florent Martin, On Zhang's semipositive metrics",
      "public_source": "https://arxiv.org/pdf/1608.08030v3",
      "files": [
        {
          "authorized_path": "/workspace/research/shared-sources/GM1608.08030v3-20261004-continuation66.pdf",
          "local_copy": "sources/S4-pdf.pdf",
          "sha256": "3a3de12f0bf765955b2b297d37704f31a432dea33cfe849145a7ff3dfe5f2571",
          "bytes": 499744,
          "expected_sha256": "3a3de12f0bf765955b2b297d37704f31a432dea33cfe849145a7ff3dfe5f2571"
        },
        {
          "authorized_path": "/workspace/research/shared-sources/GM1608.08030v3-20261004-continuation66.txt",
          "local_copy": "sources/S4-literal_extract.txt",
          "sha256": "d4427404d299d40fd70c03b2aebbe8e9dd8ffaccb05d8ef5eb04a95a23d3970a",
          "bytes": 134593,
          "expected_sha256": "d4427404d299d40fd70c03b2aebbe8e9dd8ffaccb05d8ef5eb04a95a23d3970a",
          "LF_count": 1729,
          "coordinate_rule": "UTF-8 bytes decode; split('\\n'); inclusive one-based"
        }
      ]
    },
    {
      "id": "S5",
      "version": "1801.04713v3",
      "title": "Veronika Wanner, Comparison of two notions of subharmonicity on non-Archimedean curves",
      "public_source": "https://arxiv.org/pdf/1801.04713v3",
      "files": [
        {
          "authorized_path": "/workspace/research/shared-sources/Wanner-1801.04713v3.pdf",
          "local_copy": "sources/S5-pdf.pdf",
          "sha256": "8df4a1af5dce69c1ef3a6bad2169997b5d72f8c7ced5f95d8a7dcd33ae6dd1b7",
          "bytes": 421527,
          "expected_sha256": "8df4a1af5dce69c1ef3a6bad2169997b5d72f8c7ced5f95d8a7dcd33ae6dd1b7"
        },
        {
          "authorized_path": "/workspace/research/shared-sources/Wanner-1801.04713v3-20261004.txt",
          "local_copy": "sources/S5-literal_extract.txt",
          "sha256": "e83a0516614296bc5720c6af22845255031671293dfab9acd05b12284984798f",
          "bytes": 123544,
          "expected_sha256": "e83a0516614296bc5720c6af22845255031671293dfab9acd05b12284984798f",
          "LF_count": 1829,
          "coordinate_rule": "UTF-8 bytes decode; split('\\n'); inclusive one-based"
        }
      ]
    },
    {
      "id": "S6",
      "version": "tel-00010990v1",
      "title": "Amaury Thuillier, Theorie du potentiel sur les courbes en geometrie analytique non archimedienne. Applications a la theorie d Arakelov",
      "public_source": "https://theses.hal.science/tel-00010990v1/document",
      "files": [
        {
          "authorized_path": "/workspace/research/shared-sources/Thuillier-tel-00010990v1.pdf",
          "local_copy": "sources/S6-pdf.pdf",
          "sha256": "9c57da951e8dca2676d762e9e8c6ace302675938d72434a5b0390f15af7ea29a",
          "bytes": 1507314,
          "expected_sha256": "9c57da951e8dca2676d762e9e8c6ace302675938d72434a5b0390f15af7ea29a"
        },
        {
          "authorized_path": "/workspace/research/shared-sources/Thuillier-tel-00010990v1.txt",
          "local_copy": "sources/S6-literal_extract.txt",
          "sha256": "e82226b3dde6a8088c35e1481bfd43f64bb69ee309b5cfda92c8c927a7885570",
          "bytes": 679353,
          "expected_sha256": "e82226b3dde6a8088c35e1481bfd43f64bb69ee309b5cfda92c8c927a7885570",
          "LF_count": 10587,
          "coordinate_rule": "UTF-8 bytes decode; split('\\n'); inclusive one-based"
        }
      ]
    },
    {
      "id": "S7",
      "version": "1805.01016v3",
      "title": "Boucksom--Eriksson, Spaces of norms, determinant of cohomology and Fekete points in non-Archimedean geometry",
      "public_source": "https://arxiv.org/pdf/1805.01016v3",
      "files": [
        {
          "authorized_path": "/workspace/research/shared-sources/P16-arxiv-1805.01016-20261004.pdf",
          "local_copy": "sources/S7-pdf.pdf",
          "sha256": "51d02f75a65aa463f8e22393933f5ebef9036e322d720fc632f87759c2b71cb2",
          "bytes": 1034400,
          "expected_sha256": "51d02f75a65aa463f8e22393933f5ebef9036e322d720fc632f87759c2b71cb2"
        },
        {
          "authorized_path": "/workspace/research/shared-sources/P16-arxiv-1805.01016-20261004.txt",
          "local_copy": "sources/S7-literal_extract.txt",
          "sha256": "8e584521fe3d41f179bef93d14315414ac7796532c65518c1861717416f99233",
          "bytes": 344553,
          "expected_sha256": "8e584521fe3d41f179bef93d14315414ac7796532c65518c1861717416f99233",
          "LF_count": 4787,
          "coordinate_rule": "UTF-8 bytes decode; split('\\n'); inclusive one-based"
        },
        {
          "authorized_path": "/workspace/research/shared-sources/P16-arxiv-1805.01016-20261004.html",
          "local_copy": "sources/S7-html.html",
          "sha256": "d15154ca2fe8e5e1942e16f2d77a8221dffc5162ddfa3c4bd0544c8d6f1b9a1a",
          "bytes": 41303,
          "expected_sha256": "d15154ca2fe8e5e1942e16f2d77a8221dffc5162ddfa3c4bd0544c8d6f1b9a1a"
        }
      ]
    },
    {
      "id": "S8",
      "version": "2503.05513v1",
      "title": "On semipositive piecewise linear functions in non-archimedean analytic geometry",
      "public_source": "https://arxiv.org/pdf/2503.05513v1",
      "files": [
        {
          "authorized_path": "/workspace/research/shared-sources/GR2503.05513v1-20261005-continuation72.pdf",
          "local_copy": "sources/S8-pdf.pdf",
          "sha256": "2ac2d4bd2016c1692271b1a124013585c903288f5d182081dcdaaf824095eb1b",
          "bytes": 351000,
          "expected_sha256": "2ac2d4bd2016c1692271b1a124013585c903288f5d182081dcdaaf824095eb1b"
        },
        {
          "authorized_path": "/workspace/research/shared-sources/GR2503.05513v1-20261005-continuation72.txt",
          "local_copy": "sources/S8-literal_extract.txt",
          "sha256": "5871a9252fb70f2faf39187e2baf341a42f20412ee66fdc2706b97df90ccba0c",
          "bytes": 101075,
          "expected_sha256": "5871a9252fb70f2faf39187e2baf341a42f20412ee66fdc2706b97df90ccba0c",
          "LF_count": 1399,
          "coordinate_rule": "UTF-8 bytes decode; split('\\n'); inclusive one-based"
        }
      ]
    },
    {
      "id": "S9",
      "version": "Published Confluentes Mathematici 4(4) 1250007, DOI10.1142/S1793744212500077",
      "title": "Espaces de Berkovich, polytopes, squelettes et theorie des modeles",
      "public_source": "https://cml.centre-mersenne.org/item/10.1142/S1793744212500077.pdf",
      "files": [
        {
          "authorized_path": "/workspace/research/shared-sources/Ducros-published-1250007-20261005-continuation72.pdf",
          "local_copy": "sources/S9-pdf.pdf",
          "sha256": "6aeb8b111d9a2969b1a750da31b256713d91116a3713c9a88b63fa1c798aa42f",
          "bytes": 951777,
          "expected_sha256": "6aeb8b111d9a2969b1a750da31b256713d91116a3713c9a88b63fa1c798aa42f"
        },
        {
          "authorized_path": "/workspace/research/shared-sources/Ducros-published-1250007-20261005-continuation72.txt",
          "local_copy": "sources/S9-literal_extract.txt",
          "sha256": "c3275ab4def257991b4cd4cf86d9929c717aeb3b66fab623d8162b9af6326dfa",
          "bytes": 191130,
          "expected_sha256": "c3275ab4def257991b4cd4cf86d9929c717aeb3b66fab623d8162b9af6326dfa",
          "LF_count": 3014,
          "coordinate_rule": "UTF-8 bytes decode; split('\\n'); inclusive one-based"
        }
      ]
    },
    {
      "id": "S10",
      "version": "2111.05741v3",
      "title": "Forms on Berkovich spaces based on harmonic tropicalizations",
      "public_source": "https://arxiv.org/pdf/2111.05741v3",
      "files": [
        {
          "authorized_path": "/workspace/research/shared-sources/GJR2111.05741v3-20261005-continuation72.pdf",
          "local_copy": "sources/S10-pdf.pdf",
          "sha256": "572d51c9f8907dbb814684f7d136612243c0e0b70cddbe6759bb686f0bcfbd42",
          "bytes": 1092577,
          "expected_sha256": "572d51c9f8907dbb814684f7d136612243c0e0b70cddbe6759bb686f0bcfbd42"
        },
        {
          "authorized_path": "/workspace/research/shared-sources/GJR2111.05741v3-20261005-continuation72.txt",
          "local_copy": "sources/S10-literal_extract.txt",
          "sha256": "57dfcae1d8dfc25d5ef217f34fabe9e80b679ec2956db1bced3b31bc9afdf8d3",
          "bytes": 339797,
          "expected_sha256": "57dfcae1d8dfc25d5ef217f34fabe9e80b679ec2956db1bced3b31bc9afdf8d3",
          "LF_count": 4442,
          "coordinate_rule": "UTF-8 bytes decode; split('\\n'); inclusive one-based"
        }
      ]
    }
  ],
  "units": [
    {
      "id": "e1",
      "source": "S1",
      "source_text_sha256": "659bb8d2e5335781041f03cdb168bac70126487bc0db394f3dac8cf1e9f076d0",
      "inclusive_LF": [
        435,
        469
      ],
      "sha256": "0a052b9c946f29ceacd251e92b166dc557ee078e76c19ff17f15107ace4dbd7d",
      "artifact": "source-extracts/01-S1-435-469.txt",
      "application": "general reduced-variety conventions",
      "limit": "Pinned source data; retention and hashes are not independent mathematical validation.",
      "literal_from_dictionary_sha256": "0a052b9c946f29ceacd251e92b166dc557ee078e76c19ff17f15107ace4dbd7d"
    },
    {
      "id": "e2",
      "source": "S1",
      "source_text_sha256": "659bb8d2e5335781041f03cdb168bac70126487bc0db394f3dac8cf1e9f076d0",
      "inclusive_LF": [
        759,
        874
      ],
      "sha256": "4b8a7305f07bd16782a74a0b620eb098c455aa96fb2bfac4917b43bcc6fa1044",
      "artifact": "source-extracts/02-S1-759-874.txt",
      "application": "relative integral closure and vertical DVRs",
      "limit": "Pinned source data; retention and hashes are not independent mathematical validation.",
      "literal_from_dictionary_sha256": "4b8a7305f07bd16782a74a0b620eb098c455aa96fb2bfac4917b43bcc6fa1044"
    },
    {
      "id": "e3",
      "source": "S1",
      "source_text_sha256": "659bb8d2e5335781041f03cdb168bac70126487bc0db394f3dac8cf1e9f076d0",
      "inclusive_LF": [
        938,
        1089
      ],
      "sha256": "0d683eecb0ed666f06dd4f29a6c98da6fb22286f60525105a6f00d00e527c912",
      "artifact": "source-extracts/03-S1-938-1089.txt",
      "application": "flag ideals, PL lattice, density, actual divisor representation",
      "limit": "Pinned source data; retention and hashes are not independent mathematical validation.",
      "literal_from_dictionary_sha256": "0d683eecb0ed666f06dd4f29a6c98da6fb22286f60525105a6f00d00e527c912"
    },
    {
      "id": "e4",
      "source": "S1",
      "source_text_sha256": "659bb8d2e5335781041f03cdb168bac70126487bc0db394f3dac8cf1e9f076d0",
      "inclusive_LF": [
        1309,
        1352
      ],
      "sha256": "e051a9b70c06023f3fdb41255282f838d12d32fb30fcf3ffa22420c769d190ff",
      "artifact": "source-extracts/04-S1-1309-1352.txt",
      "application": "same-bundle FS generation and span",
      "limit": "Pinned source data; retention and hashes are not independent mathematical validation.",
      "literal_from_dictionary_sha256": "e051a9b70c06023f3fdb41255282f838d12d32fb30fcf3ffa22420c769d190ff"
    },
    {
      "id": "e5",
      "source": "S1",
      "source_text_sha256": "659bb8d2e5335781041f03cdb168bac70126487bc0db394f3dac8cf1e9f076d0",
      "inclusive_LF": [
        1420,
        1455
      ],
      "sha256": "426b32a79eaabddd722a2f8c7b7d1b6d65311937cd704dae4a1d0a4332e17fec",
      "artifact": "source-extracts/05-S1-1420-1455.txt",
      "application": "actual test configuration and ample model",
      "limit": "Pinned source data; retention and hashes are not independent mathematical validation.",
      "literal_from_dictionary_sha256": "426b32a79eaabddd722a2f8c7b7d1b6d65311937cd704dae4a1d0a4332e17fec"
    },
    {
      "id": "e6",
      "source": "S1",
      "source_text_sha256": "659bb8d2e5335781041f03cdb168bac70126487bc0db394f3dac8cf1e9f076d0",
      "inclusive_LF": [
        1687,
        1738
      ],
      "sha256": "a44581a6ec6d137d3e65e97270e451228d73fb3dda60f5a11ce4b261a22eb9b1",
      "artifact": "source-extracts/06-S1-1687-1738.txt",
      "application": "Hdom on a fixed actual bundle",
      "limit": "Pinned source data; retention and hashes are not independent mathematical validation.",
      "literal_from_dictionary_sha256": "a44581a6ec6d137d3e65e97270e451228d73fb3dda60f5a11ce4b261a22eb9b1"
    },
    {
      "id": "e7",
      "source": "S1",
      "source_text_sha256": "659bb8d2e5335781041f03cdb168bac70126487bc0db394f3dac8cf1e9f076d0",
      "inclusive_LF": [
        1810,
        1858
      ],
      "sha256": "672069804343eb355735bee9c0c0d857d31e20a1fc18847f2464885e22022048",
      "artifact": "source-extracts/07-S1-1810-1858.txt",
      "application": "raw model measure and compact-pairing IBP",
      "limit": "Pinned source data; retention and hashes are not independent mathematical validation.",
      "literal_from_dictionary_sha256": "672069804343eb355735bee9c0c0d857d31e20a1fc18847f2464885e22022048"
    },
    {
      "id": "e8",
      "source": "S1",
      "source_text_sha256": "659bb8d2e5335781041f03cdb168bac70126487bc0db394f3dac8cf1e9f076d0",
      "inclusive_LF": [
        2190,
        2289
      ],
      "sha256": "1366ec7573822a5524928b2a060d4a297a7c2bb3e4e048b9783589094edda81d",
      "artifact": "source-extracts/08-S1-2190-2289.txt",
      "application": "genuine cone and class closure",
      "limit": "Pinned source data; retention and hashes are not independent mathematical validation.",
      "literal_from_dictionary_sha256": "1366ec7573822a5524928b2a060d4a297a7c2bb3e4e048b9783589094edda81d"
    },
    {
      "id": "e9",
      "source": "S1",
      "source_text_sha256": "659bb8d2e5335781041f03cdb168bac70126487bc0db394f3dac8cf1e9f076d0",
      "inclusive_LF": [
        2414,
        2462
      ],
      "sha256": "2452bb775162149812ac4f238f20d3a7360c89cddda7c7918f3e48188b0fcf83",
      "artifact": "source-extracts/09-S1-2414-2462.txt",
      "application": "regularization and genuine FS membership",
      "limit": "Pinned source data; retention and hashes are not independent mathematical validation.",
      "literal_from_dictionary_sha256": "2452bb775162149812ac4f238f20d3a7360c89cddda7c7918f3e48188b0fcf83"
    },
    {
      "id": "e10",
      "source": "S1",
      "source_text_sha256": "659bb8d2e5335781041f03cdb168bac70126487bc0db394f3dac8cf1e9f076d0",
      "inclusive_LF": [
        2488,
        2541
      ],
      "sha256": "3709e976c34a7aa779a92d36986fe5aaa83efc65384af64c8df047cbbdee3c47",
      "artifact": "source-extracts/10-S1-2488-2541.txt",
      "application": "divisorial order, minimum usc extension",
      "limit": "Pinned source data; retention and hashes are not independent mathematical validation.",
      "literal_from_dictionary_sha256": "3709e976c34a7aa779a92d36986fe5aaa83efc65384af64c8df047cbbdee3c47"
    },
    {
      "id": "e11",
      "source": "S1",
      "source_text_sha256": "659bb8d2e5335781041f03cdb168bac70126487bc0db394f3dac8cf1e9f076d0",
      "inclusive_LF": [
        2859,
        2876
      ],
      "sha256": "dd64c9e9fcffab905d7ca45c52532d5ce99bbf2b31ebd1a6ce5c62689b2714ca",
      "artifact": "source-extracts/11-S1-2859-2876.txt",
      "application": "birational onto with target-side approaching EP",
      "limit": "Pinned source data; retention and hashes are not independent mathematical validation.",
      "literal_from_dictionary_sha256": "dd64c9e9fcffab905d7ca45c52532d5ce99bbf2b31ebd1a6ce5c62689b2714ca"
    },
    {
      "id": "e12",
      "source": "S1",
      "source_text_sha256": "659bb8d2e5335781041f03cdb168bac70126487bc0db394f3dac8cf1e9f076d0",
      "inclusive_LF": [
        2887,
        2957
      ],
      "sha256": "4b40a2545a02632b81053a4aa795fcd6319fdccd24465040441826dbc1685a3d",
      "artifact": "source-extracts/12-S1-2887-2957.txt",
      "application": "continuity of envelopes; compact-majorant nets",
      "limit": "Pinned source data; retention and hashes are not independent mathematical validation.",
      "literal_from_dictionary_sha256": "4b40a2545a02632b81053a4aa795fcd6319fdccd24465040441826dbc1685a3d"
    },
    {
      "id": "e13",
      "source": "S1",
      "source_text_sha256": "659bb8d2e5335781041f03cdb168bac70126487bc0db394f3dac8cf1e9f076d0",
      "inclusive_LF": [
        2980,
        3065
      ],
      "sha256": "4ae7a90b4df57248c04456a5d20f552c569d9753cc7b332ab43d75446aca1613",
      "artifact": "source-extracts/13-S1-2980-3065.txt",
      "application": "smooth envelope theorem and proof",
      "limit": "Pinned source data; retention and hashes are not independent mathematical validation.",
      "literal_from_dictionary_sha256": "4ae7a90b4df57248c04456a5d20f552c569d9753cc7b332ab43d75446aca1613"
    },
    {
      "id": "e14",
      "source": "S1",
      "source_text_sha256": "659bb8d2e5335781041f03cdb168bac70126487bc0db394f3dac8cf1e9f076d0",
      "inclusive_LF": [
        3649,
        3692
      ],
      "sha256": "7586713d8cfeadb3c14431c977530b6ab7e8cd770418b97433c6a8cb5e4fe9af",
      "artifact": "source-extracts/14-S1-3649-3692.txt",
      "application": "general projective scope of global pairings",
      "limit": "Pinned source data; retention and hashes are not independent mathematical validation.",
      "literal_from_dictionary_sha256": "7586713d8cfeadb3c14431c977530b6ab7e8cd770418b97433c6a8cb5e4fe9af"
    },
    {
      "id": "e15",
      "source": "S1",
      "source_text_sha256": "659bb8d2e5335781041f03cdb168bac70126487bc0db394f3dac8cf1e9f076d0",
      "inclusive_LF": [
        3980,
        4148
      ],
      "sha256": "35889077944e327cab290328e7574af5034fe06cbbfa97b8df356e917c9a96db",
      "artifact": "source-extracts/15-S1-3980-4148.txt",
      "application": "genuine mixed operator, weighted convergence, continuous compatibility",
      "limit": "Pinned source data; retention and hashes are not independent mathematical validation.",
      "literal_from_dictionary_sha256": "35889077944e327cab290328e7574af5034fe06cbbfa97b8df356e917c9a96db"
    },
    {
      "id": "e16",
      "source": "S1",
      "source_text_sha256": "659bb8d2e5335781041f03cdb168bac70126487bc0db394f3dac8cf1e9f076d0",
      "inclusive_LF": [
        4519,
        4607
      ],
      "sha256": "fc205b71fa16f7a8a9be5278f5ede544014742d555d733274dc8b473587e26f2",
      "artifact": "source-extracts/16-S1-4519-4607.txt",
      "application": "winning-locus locality and comparison",
      "limit": "Pinned source data; retention and hashes are not independent mathematical validation.",
      "literal_from_dictionary_sha256": "fc205b71fa16f7a8a9be5278f5ede544014742d555d733274dc8b473587e26f2"
    },
    {
      "id": "e17",
      "source": "S1",
      "source_text_sha256": "659bb8d2e5335781041f03cdb168bac70126487bc0db394f3dac8cf1e9f076d0",
      "inclusive_LF": [
        4892,
        4960
      ],
      "sha256": "6761fc6a62172ae300314992e07f19aad4374781c7751d19e493ec0bc482e75d",
      "artifact": "source-extracts/17-S1-4892-4960.txt",
      "application": "energy differentiation and its limits",
      "limit": "Pinned source data; retention and hashes are not independent mathematical validation.",
      "literal_from_dictionary_sha256": "6761fc6a62172ae300314992e07f19aad4374781c7751d19e493ec0bc482e75d"
    },
    {
      "id": "e18",
      "source": "S1",
      "source_text_sha256": "659bb8d2e5335781041f03cdb168bac70126487bc0db394f3dac8cf1e9f076d0",
      "inclusive_LF": [
        5230,
        5304
      ],
      "sha256": "270fead3dbb82f56e8bbef72623105fefa2846687a26b95f4a9f15a28b502f36",
      "artifact": "source-extracts/18-S1-5230-5304.txt",
      "application": "target integral continuity and intrinsic energy condition",
      "limit": "Pinned source data; retention and hashes are not independent mathematical validation.",
      "literal_from_dictionary_sha256": "270fead3dbb82f56e8bbef72623105fefa2846687a26b95f4a9f15a28b502f36"
    },
    {
      "id": "e19",
      "source": "S1",
      "source_text_sha256": "659bb8d2e5335781041f03cdb168bac70126487bc0db394f3dac8cf1e9f076d0",
      "inclusive_LF": [
        5440,
        5479
      ],
      "sha256": "62f80f85972d10a128333605eab0a471a0637f52978e2bf99fd42723b6ba6858",
      "artifact": "source-extracts/19-S1-5440-5479.txt",
      "application": "uniqueness and domination",
      "limit": "Pinned source data; retention and hashes are not independent mathematical validation.",
      "literal_from_dictionary_sha256": "62f80f85972d10a128333605eab0a471a0637f52978e2bf99fd42723b6ba6858"
    },
    {
      "id": "e20",
      "source": "S1",
      "source_text_sha256": "659bb8d2e5335781041f03cdb168bac70126487bc0db394f3dac8cf1e9f076d0",
      "inclusive_LF": [
        6092,
        6146
      ],
      "sha256": "6bb578ad44c78dbe18f74ff227167f6d88a7660585784c3d499fac7a48f2705a",
      "artifact": "source-extracts/20-S1-6092-6146.txt",
      "application": "EP equivalent to actual variational solvability",
      "limit": "Pinned source data; retention and hashes are not independent mathematical validation.",
      "literal_from_dictionary_sha256": "6bb578ad44c78dbe18f74ff227167f6d88a7660585784c3d499fac7a48f2705a"
    },
    {
      "id": "e21",
      "source": "S1",
      "source_text_sha256": "659bb8d2e5335781041f03cdb168bac70126487bc0db394f3dac8cf1e9f076d0",
      "inclusive_LF": [
        6230,
        6268
      ],
      "sha256": "1a960d306b0bfa9c63f5fccc4deaf63139c4f5ef3d7d2649af14fc4f133ab07b",
      "artifact": "source-extracts/21-S1-6230-6268.txt",
      "application": "sequential approximation only after membership",
      "limit": "Pinned source data; retention and hashes are not independent mathematical validation.",
      "literal_from_dictionary_sha256": "1a960d306b0bfa9c63f5fccc4deaf63139c4f5ef3d7d2649af14fc4f133ab07b"
    },
    {
      "id": "e22",
      "source": "S1",
      "source_text_sha256": "659bb8d2e5335781041f03cdb168bac70126487bc0db394f3dac8cf1e9f076d0",
      "inclusive_LF": [
        6304,
        6372
      ],
      "sha256": "9164b6c60b64ef76bb4b8260838d913b5cec28f2e8cc11af1f62b15bb923fbc6",
      "artifact": "source-extracts/22-S1-6304-6372.txt",
      "application": "EP assumed for contact orthogonality",
      "limit": "Pinned source data; retention and hashes are not independent mathematical validation.",
      "literal_from_dictionary_sha256": "9164b6c60b64ef76bb4b8260838d913b5cec28f2e8cc11af1f62b15bb923fbc6"
    },
    {
      "id": "e23",
      "source": "S2",
      "source_text_sha256": "c8ffe91a631da67f6d3872a1a06ab8d15755aed2f926cdf326725ca3662cef7d",
      "inclusive_LF": [
        635,
        781
      ],
      "sha256": "6ef0dbe653c6c6a3e1b3f96c864805cce13d08f4e63b320be0da28ca0a0db8de",
      "artifact": "source-extracts/23-S2-635-781.txt",
      "application": "actual local definitions and printed contact/growth conventions",
      "limit": "Pinned source data; retention and hashes are not independent mathematical validation.",
      "literal_from_dictionary_sha256": "6ef0dbe653c6c6a3e1b3f96c864805cce13d08f4e63b320be0da28ca0a0db8de"
    },
    {
      "id": "e24",
      "source": "S2",
      "source_text_sha256": "c8ffe91a631da67f6d3872a1a06ab8d15755aed2f926cdf326725ca3662cef7d",
      "inclusive_LF": [
        1236,
        1309
      ],
      "sha256": "fcd5dcafe19d130eb9b96c252801302db3f9aabbd192370259bae3e7a63c4a23",
      "artifact": "source-extracts/24-S2-1236-1309.txt",
      "application": "bounded collar product claim and its convergence premises",
      "limit": "Pinned source data; retention and hashes are not independent mathematical validation.",
      "literal_from_dictionary_sha256": "fcd5dcafe19d130eb9b96c252801302db3f9aabbd192370259bae3e7a63c4a23"
    },
    {
      "id": "e25",
      "source": "S2",
      "source_text_sha256": "c8ffe91a631da67f6d3872a1a06ab8d15755aed2f926cdf326725ca3662cef7d",
      "inclusive_LF": [
        1331,
        1537
      ],
      "sha256": "89d0992afffad46a10fc840aff477a4936d21d78f2589d043a54d5c9963d4c5d",
      "artifact": "source-extracts/25-S2-1331-1537.txt",
      "application": "entire compact IBP, mass, comparison, membership proof",
      "limit": "Pinned source data; retention and hashes are not independent mathematical validation.",
      "literal_from_dictionary_sha256": "89d0992afffad46a10fc840aff477a4936d21d78f2589d043a54d5c9963d4c5d"
    },
    {
      "id": "e26",
      "source": "S2",
      "source_text_sha256": "c8ffe91a631da67f6d3872a1a06ab8d15755aed2f926cdf326725ca3662cef7d",
      "inclusive_LF": [
        1560,
        1579
      ],
      "sha256": "9ed3f20282976fc38e35582716b216684336bf500bd87173777e8224c582b9a8",
      "artifact": "source-extracts/26-S2-1560-1579.txt",
      "application": "printed smooth growth statement",
      "limit": "Pinned source data; retention and hashes are not independent mathematical validation.",
      "literal_from_dictionary_sha256": "9ed3f20282976fc38e35582716b216684336bf500bd87173777e8224c582b9a8"
    },
    {
      "id": "e27",
      "source": "S2",
      "source_text_sha256": "c8ffe91a631da67f6d3872a1a06ab8d15755aed2f926cdf326725ca3662cef7d",
      "inclusive_LF": [
        2200,
        2372
      ],
      "sha256": "2413512b2e94bdf20b8e74b21f5174bc0b24cd98d575cfbf02c2ed0fb9f59baf",
      "artifact": "source-extracts/27-S2-2200-2372.txt",
      "application": "entire original nonflat trace argument",
      "limit": "Pinned source data; retention and hashes are not independent mathematical validation.",
      "literal_from_dictionary_sha256": "2413512b2e94bdf20b8e74b21f5174bc0b24cd98d575cfbf02c2ed0fb9f59baf"
    },
    {
      "id": "e28",
      "source": "S2",
      "source_text_sha256": "c8ffe91a631da67f6d3872a1a06ab8d15755aed2f926cdf326725ca3662cef7d",
      "inclusive_LF": [
        2697,
        2755
      ],
      "sha256": "691df9c820eaec929f098e9fb256d3943f5ca34f6c66e451609c7d633c0de76e",
      "artifact": "source-extracts/28-S2-2697-2755.txt",
      "application": "entire envelope and field-descent argument",
      "limit": "Pinned source data; retention and hashes are not independent mathematical validation.",
      "literal_from_dictionary_sha256": "691df9c820eaec929f098e9fb256d3943f5ca34f6c66e451609c7d633c0de76e"
    },
    {
      "id": "e29",
      "source": "S3",
      "source_text_sha256": "64846cb00926267c6238d1afac61b5eaed0a0e3a6349725738f9b1bf163de085",
      "inclusive_LF": [
        10432,
        10449
      ],
      "sha256": "309dcfe51944e02b86cd08a3e2dba736974f98a5c468deb524169f76dea30e78",
      "artifact": "source-extracts/29-S3-10432-10449.txt",
      "application": "CLD convergence is locally uniform and continuous",
      "limit": "Pinned source data; retention and hashes are not independent mathematical validation.",
      "literal_from_dictionary_sha256": "309dcfe51944e02b86cd08a3e2dba736974f98a5c468deb524169f76dea30e78"
    },
    {
      "id": "e30",
      "source": "S4",
      "source_text_sha256": "d4427404d299d40fd70c03b2aebbe8e9dd8ffaccb05d8ef5eb04a95a23d3970a",
      "inclusive_LF": [
        249,
        295
      ],
      "sha256": "dc1373dcd4b0ae7f36d6f3bef91bf45cd82573b3fc3ddf1cda8565cc97d73447",
      "artifact": "source-extracts/30-S4-249-295.txt",
      "application": "formal/algebraic dependency actually cited",
      "limit": "Pinned source data; retention and hashes are not independent mathematical validation.",
      "literal_from_dictionary_sha256": "dc1373dcd4b0ae7f36d6f3bef91bf45cd82573b3fc3ddf1cda8565cc97d73447"
    },
    {
      "id": "e31",
      "source": "S4",
      "source_text_sha256": "d4427404d299d40fd70c03b2aebbe8e9dd8ffaccb05d8ef5eb04a95a23d3970a",
      "inclusive_LF": [
        633,
        782
      ],
      "sha256": "6d18741f8932b971cfd7952be2ef1d067305cc7bfe1080d93352be097e42ffd8",
      "artifact": "source-extracts/31-S4-633-782.txt",
      "application": "represented-model nef detection and proper residual-curve proof",
      "limit": "Pinned source data; retention and hashes are not independent mathematical validation.",
      "literal_from_dictionary_sha256": "6d18741f8932b971cfd7952be2ef1d067305cc7bfe1080d93352be097e42ffd8"
    },
    {
      "id": "e32",
      "source": "S6",
      "source_text_sha256": "e82226b3dde6a8088c35e1481bfd43f64bb69ee309b5cfda92c8c927a7885570",
      "inclusive_LF": [
        3580,
        3627
      ],
      "sha256": "240a02e69e032853a4d040d4dc0003b0323a11b54c1ec85d7fbf671ee083500b",
      "artifact": "source-extracts/32-S6-3580-3627.txt",
      "application": "analytic units are harmonic",
      "limit": "Pinned source data; retention and hashes are not independent mathematical validation.",
      "literal_from_dictionary_sha256": "240a02e69e032853a4d040d4dc0003b0323a11b54c1ec85d7fbf671ee083500b"
    },
    {
      "id": "e33",
      "source": "S6",
      "source_text_sha256": "e82226b3dde6a8088c35e1481bfd43f64bb69ee309b5cfda92c8c927a7885570",
      "inclusive_LF": [
        3730,
        3741
      ],
      "sha256": "cd12932de3c4cd0dee40f8ac44b0531b9795312ab37f1068b36a2a7eecabb558",
      "artifact": "source-extracts/33-S6-3730-3741.txt",
      "application": "harmonic maximum principle",
      "limit": "Pinned source data; retention and hashes are not independent mathematical validation.",
      "literal_from_dictionary_sha256": "cd12932de3c4cd0dee40f8ac44b0531b9795312ab37f1068b36a2a7eecabb558"
    },
    {
      "id": "e34",
      "source": "S6",
      "source_text_sha256": "e82226b3dde6a8088c35e1481bfd43f64bb69ee309b5cfda92c8c927a7885570",
      "inclusive_LF": [
        3783,
        3820
      ],
      "sha256": "e6679c4ed22bf386251a069fc8f648b473c02405cef3687841aed57bd582186e",
      "artifact": "source-extracts/34-S6-3783-3820.txt",
      "application": "subharmonic logs and decreasing limits",
      "limit": "Pinned source data; retention and hashes are not independent mathematical validation.",
      "literal_from_dictionary_sha256": "e6679c4ed22bf386251a069fc8f648b473c02405cef3687841aed57bd582186e"
    },
    {
      "id": "e35",
      "source": "S6",
      "source_text_sha256": "e82226b3dde6a8088c35e1481bfd43f64bb69ee309b5cfda92c8c927a7885570",
      "inclusive_LF": [
        3860,
        3907
      ],
      "sha256": "5e0db20c0db4acc10fb61ca401b8b7804099346aead443ce6ca1724684f4e4de",
      "artifact": "source-extracts/35-S6-3860-3907.txt",
      "application": "harmonic-test characterization",
      "limit": "Pinned source data; retention and hashes are not independent mathematical validation.",
      "literal_from_dictionary_sha256": "5e0db20c0db4acc10fb61ca401b8b7804099346aead443ce6ca1724684f4e4de"
    },
    {
      "id": "e36",
      "source": "S7",
      "source_text_sha256": "8e584521fe3d41f179bef93d14315414ac7796532c65518c1861717416f99233",
      "inclusive_LF": [
        2281,
        2363
      ],
      "sha256": "03db35ca81bc95d4d7ebd173b99f693c6eff6d22ed74c6188e39ad5d8260fb4c",
      "artifact": "source-extracts/36-S7-2281-2363.txt",
      "application": "same-ample-class continuous FS theorem",
      "limit": "Pinned source data; retention and hashes are not independent mathematical validation.",
      "literal_from_dictionary_sha256": "03db35ca81bc95d4d7ebd173b99f693c6eff6d22ed74c6188e39ad5d8260fb4c"
    },
    {
      "id": "e37",
      "source": "S7",
      "source_text_sha256": "8e584521fe3d41f179bef93d14315414ac7796532c65518c1861717416f99233",
      "inclusive_LF": [
        2611,
        2779
      ],
      "sha256": "1ffe08a5900d483d40d3a6de9e5a4efdc6b6efa1efc4df7c6f35d7169c408993",
      "artifact": "source-extracts/37-S7-2611-2779.txt",
      "application": "continuous products and uniform extension",
      "limit": "Pinned source data; retention and hashes are not independent mathematical validation.",
      "literal_from_dictionary_sha256": "1ffe08a5900d483d40d3a6de9e5a4efdc6b6efa1efc4df7c6f35d7169c408993"
    },
    {
      "id": "e38",
      "source": "S7",
      "source_text_sha256": "8e584521fe3d41f179bef93d14315414ac7796532c65518c1861717416f99233",
      "inclusive_LF": [
        3125,
        3202
      ],
      "sha256": "1db7782548c52fe9ce85efc3d4c88ed30a65323334bf8da1bc8a21483dcea58b",
      "artifact": "source-extracts/38-S7-3125-3202.txt",
      "application": "continuous Deligne comparison including proof",
      "limit": "Pinned source data; retention and hashes are not independent mathematical validation.",
      "literal_from_dictionary_sha256": "1db7782548c52fe9ce85efc3d4c88ed30a65323334bf8da1bc8a21483dcea58b"
    },
    {
      "id": "e39",
      "source": "S8",
      "source_text_sha256": "5871a9252fb70f2faf39187e2baf341a42f20412ee66fdc2706b97df90ccba0c",
      "inclusive_LF": [
        147,
        164
      ],
      "sha256": "efd93bc7c655ffb0de961623bfee2c439eb44fbce26686557a9cf10fd0f8fe90",
      "artifact": "source-extracts/39-S8-147-164.txt",
      "application": "general positive-current converse remains unknown",
      "limit": "Pinned source data; retention and hashes are not independent mathematical validation.",
      "literal_from_dictionary_sha256": "efd93bc7c655ffb0de961623bfee2c439eb44fbce26686557a9cf10fd0f8fe90"
    },
    {
      "id": "e40",
      "source": "S8",
      "source_text_sha256": "5871a9252fb70f2faf39187e2baf341a42f20412ee66fdc2706b97df90ccba0c",
      "inclusive_LF": [
        489,
        800
      ],
      "sha256": "b03d31f8ee06459fa5717a8ecba30a1ea5875ef773072aaa5d6a044eb85e9060",
      "artifact": "source-extracts/40-S8-489-800.txt",
      "application": "entire local curve-lifting theorem and proof",
      "limit": "Pinned source data; retention and hashes are not independent mathematical validation.",
      "literal_from_dictionary_sha256": "b03d31f8ee06459fa5717a8ecba30a1ea5875ef773072aaa5d6a044eb85e9060"
    },
    {
      "id": "e41",
      "source": "S8",
      "source_text_sha256": "5871a9252fb70f2faf39187e2baf341a42f20412ee66fdc2706b97df90ccba0c",
      "inclusive_LF": [
        803,
        926
      ],
      "sha256": "c4f861b42719d76be8cab3099618d3c7a04c8440524bab471915834df5b5c92e",
      "artifact": "source-extracts/41-S8-803-926.txt",
      "application": "represented PL curve criteria and entire proofs",
      "limit": "Pinned source data; retention and hashes are not independent mathematical validation.",
      "literal_from_dictionary_sha256": "c4f861b42719d76be8cab3099618d3c7a04c8440524bab471915834df5b5c92e"
    },
    {
      "id": "e42",
      "source": "S9",
      "source_text_sha256": "c3275ab4def257991b4cd4cf86d9929c717aeb3b66fab623d8162b9af6326dfa",
      "inclusive_LF": [
        2077,
        2155
      ],
      "sha256": "874dd983a3cbaf8744b9beaf27b49bcf2305591c97e411699dfd91d6b420cceb",
      "artifact": "source-extracts/42-S9-2077-2155.txt",
      "application": "compact norm-image theorem and exact algebraic reduction",
      "limit": "Pinned source data; retention and hashes are not independent mathematical validation.",
      "literal_from_dictionary_sha256": "874dd983a3cbaf8744b9beaf27b49bcf2305591c97e411699dfd91d6b420cceb"
    },
    {
      "id": "e43",
      "source": "S10",
      "source_text_sha256": "57dfcae1d8dfc25d5ef217f34fabe9e80b679ec2956db1bced3b31bc9afdf8d3",
      "inclusive_LF": [
        2540,
        2589
      ],
      "sha256": "0c4ed10aa0e6bb8a9cdc7c011be276fcc6f1a487124cdb57594cc0d89d5c71a3",
      "artifact": "source-extracts/43-S10-2540-2589.txt",
      "application": "model positivity and proper residue tests",
      "limit": "Pinned source data; retention and hashes are not independent mathematical validation.",
      "literal_from_dictionary_sha256": "0c4ed10aa0e6bb8a9cdc7c011be276fcc6f1a487124cdb57594cc0d89d5c71a3"
    }
  ]
}

END MATHEMATICAL DATA



BEGIN MATHEMATICAL DATA: All17 new proof92 external premises: losslessly factored passage literals
{
  "coordinate_rule": "UTF-8 bytes decode; split('\\n'); inclusive one-based",
  "limits": "Every top-level external premise is indexed and has exact HTTP(S) primary statement/proof evidence. Recursive inputs wholly inside task-granted accepted proofs retain their exact scope as grants, not invented external premises. Source-byte checks do not validate applications.",
  "premises": [
    {
      "index": 0,
      "statement": "For every Noetherian quasi-excellent generically reduced scheme X over Spec(Q), Temkin 0904.1592v2 Theorem 1.2.1 supplies a finite blowup sequence with regular final scheme, regular centers disjoint from the preimages of the original regular locus, and the stated regular-morphism functoriality. A sequence means a finite composition; the pertinent construction and its stabilization are those in Section 4.3.",
      "passages": [
        {
          "unit": "t00",
          "url": "https://arxiv.org/pdf/0904.1592v2",
          "version": "0904.1592v2 (11 December 2011)",
          "source_text_sha256": "8941c77866ad807731aee46072be77eeb0bf184559424730b140263f502c98b9",
          "inclusive_LF": [
            83,
            92
          ],
          "sha256": "8e04c8c70067b9241eac60096b1d40f71432c02710482d42b86cda7b4327d64f",
          "artifact": "source-extracts/t00-Temkin-rendered-83-92.txt",
          "literal_from_dictionary_sha256": "8e04c8c70067b9241eac60096b1d40f71432c02710482d42b86cda7b4327d64f"
        },
        {
          "unit": "t01",
          "url": "https://arxiv.org/pdf/0904.1592v2",
          "version": "0904.1592v2 (11 December 2011)",
          "source_text_sha256": "8941c77866ad807731aee46072be77eeb0bf184559424730b140263f502c98b9",
          "inclusive_LF": [
            422,
            434
          ],
          "sha256": "d8b77b3db1f70b041281e41dae04484dbed2c36141832172abfcf7e3b7869c58",
          "artifact": "source-extracts/t01-Temkin-rendered-422-434.txt",
          "literal_from_dictionary_sha256": "d8b77b3db1f70b041281e41dae04484dbed2c36141832172abfcf7e3b7869c58"
        },
        {
          "unit": "t02",
          "url": "https://arxiv.org/pdf/0904.1592v2",
          "version": "0904.1592v2 (11 December 2011)",
          "source_text_sha256": "8941c77866ad807731aee46072be77eeb0bf184559424730b140263f502c98b9",
          "inclusive_LF": [
            1527,
            1552
          ],
          "sha256": "0e83f63e3296a2fe2043512f2317647039a7010757aec51315752e217ac4c9d0",
          "artifact": "source-extracts/t02-Temkin-rendered-1527-1552.txt",
          "literal_from_dictionary_sha256": "0e83f63e3296a2fe2043512f2317647039a7010757aec51315752e217ac4c9d0"
        },
        {
          "unit": "t03",
          "url": "https://arxiv.org/pdf/0904.1592v2",
          "version": "0904.1592v2 (11 December 2011)",
          "source_text_sha256": "8941c77866ad807731aee46072be77eeb0bf184559424730b140263f502c98b9",
          "inclusive_LF": [
            1694,
            1887
          ],
          "sha256": "33518fa382ca7543017cd847eec37abbc72a2fa03d9ace110dfc9b0942b4cf24",
          "artifact": "source-extracts/t03-Temkin-rendered-1694-1887.txt",
          "literal_from_dictionary_sha256": "33518fa382ca7543017cd847eec37abbc72a2fa03d9ace110dfc9b0942b4cf24"
        }
      ],
      "short_pertinent_quote": "For any noetherian quasi-excellent generically reduced scheme",
      "kind": "External primary mathematical premise; not a native registered support."
    },
    {
      "index": 1,
      "statement": "BJ 1801.08229v4 works over algebraically closed trivially valued fields with reduced projective varieties, permitting nonnormal, reducible and unequal-dimensional varieties. Canonical section evaluation at valuation-ring centers gives norms in [0,1] and the trivial reference metric. Rational PL functions form a vector lattice uniformly dense in C0(Xan).",
      "passages": [
        {
          "unit": "x00",
          "url": "https://arxiv.org/pdf/1801.08229v4",
          "version": "1801.08229v4",
          "source_text_sha256": "659bb8d2e5335781041f03cdb168bac70126487bc0db394f3dac8cf1e9f076d0",
          "inclusive_LF": [
            435,
            469
          ],
          "sha256": "0a052b9c946f29ceacd251e92b166dc557ee078e76c19ff17f15107ace4dbd7d",
          "artifact": "source-extracts/x00-S1-435-469.txt",
          "literal_from_dictionary_sha256": "0a052b9c946f29ceacd251e92b166dc557ee078e76c19ff17f15107ace4dbd7d"
        },
        {
          "unit": "x01",
          "url": "https://arxiv.org/pdf/1801.08229v4",
          "version": "1801.08229v4",
          "source_text_sha256": "659bb8d2e5335781041f03cdb168bac70126487bc0db394f3dac8cf1e9f076d0",
          "inclusive_LF": [
            886,
            900
          ],
          "sha256": "c4ad8d70a4bdebbd888b86893e9c6fbaa0c9a79e7cc277c3e1a64f8b2871b742",
          "artifact": "source-extracts/x01-S1-886-900.txt",
          "literal_from_dictionary_sha256": "c4ad8d70a4bdebbd888b86893e9c6fbaa0c9a79e7cc277c3e1a64f8b2871b742"
        },
        {
          "unit": "x02",
          "url": "https://arxiv.org/pdf/1801.08229v4",
          "version": "1801.08229v4",
          "source_text_sha256": "659bb8d2e5335781041f03cdb168bac70126487bc0db394f3dac8cf1e9f076d0",
          "inclusive_LF": [
            962,
            1030
          ],
          "sha256": "e565799b443d5db3b4ba800952d6df60207bba05a7b673e8cb9815d26f84cbc0",
          "artifact": "source-extracts/x02-S1-962-1030.txt",
          "literal_from_dictionary_sha256": "e565799b443d5db3b4ba800952d6df60207bba05a7b673e8cb9815d26f84cbc0"
        }
      ],
      "short_pertinent_quote": "is reduced, but not necessarily irreducible, nor even equidimensional",
      "kind": "External primary mathematical premise; not a native registered support."
    },
    {
      "index": 2,
      "statement": "For an actual ample rational bundle L on a reduced projective variety over an algebraically closed trivially valued field, BJ 2.18, 2.31 and 3.9 identify finite FS potentials with actual same-bundle model metrics, with Hdom(c1(L)) contained in H(L). BJ 3.10 uniformly approximates any genuine PL_R potential in an ample class by Hdom of that class.",
      "passages": [
        {
          "unit": "x03",
          "url": "https://arxiv.org/pdf/1801.08229v4",
          "version": "1801.08229v4",
          "source_text_sha256": "659bb8d2e5335781041f03cdb168bac70126487bc0db394f3dac8cf1e9f076d0",
          "inclusive_LF": [
            1390,
            1464
          ],
          "sha256": "0deecfcb8093f8efae3de37a562f6a7b4aaa7a36b02b48cb6232d9a9aa71ffe5",
          "artifact": "source-extracts/x03-S1-1390-1464.txt",
          "literal_from_dictionary_sha256": "0deecfcb8093f8efae3de37a562f6a7b4aaa7a36b02b48cb6232d9a9aa71ffe5"
        },
        {
          "unit": "x04",
          "url": "https://arxiv.org/pdf/1801.08229v4",
          "version": "1801.08229v4",
          "source_text_sha256": "659bb8d2e5335781041f03cdb168bac70126487bc0db394f3dac8cf1e9f076d0",
          "inclusive_LF": [
            1692,
            1729
          ],
          "sha256": "fc3d3b08864bcfeefe833a1079e5530224c333242d000add352f344be9ac4219",
          "artifact": "source-extracts/x04-S1-1692-1729.txt",
          "literal_from_dictionary_sha256": "fc3d3b08864bcfeefe833a1079e5530224c333242d000add352f344be9ac4219"
        }
      ],
      "short_pertinent_quote": "Hdom (L) := Hdom (c1 (L)) ⊂ H(L)",
      "kind": "External primary mathematical premise; not a native registered support."
    },
    {
      "index": 3,
      "statement": "On a reduced projective variety over an algebraically closed trivially valued field, BJ 4.3, 4.5-4.7 give zero in every nef psh class, positive addition and scaling, maxima, constants, uniform closure, decreasing varying-class closure for generically finite limits, and genuine pullback when the pullback is generically finite. BJ 4.15-4.16 give decreasing Hdom nets in ample classes and uniform fixed-class approximation of continuous psh potentials, without EP.",
      "passages": [
        {
          "unit": "x05",
          "url": "https://arxiv.org/pdf/1801.08229v4",
          "version": "1801.08229v4",
          "source_text_sha256": "659bb8d2e5335781041f03cdb168bac70126487bc0db394f3dac8cf1e9f076d0",
          "inclusive_LF": [
            2170,
            2368
          ],
          "sha256": "31dcf643b431ee85afa779d0aa54f37eb920945c87f46d5c3fd532e72fb4929b",
          "artifact": "source-extracts/x05-S1-2170-2368.txt",
          "literal_from_dictionary_sha256": "31dcf643b431ee85afa779d0aa54f37eb920945c87f46d5c3fd532e72fb4929b"
        },
        {
          "unit": "x06",
          "url": "https://arxiv.org/pdf/1801.08229v4",
          "version": "1801.08229v4",
          "source_text_sha256": "659bb8d2e5335781041f03cdb168bac70126487bc0db394f3dac8cf1e9f076d0",
          "inclusive_LF": [
            2418,
            2468
          ],
          "sha256": "bee2dd5ee40e955868a1651e9c679c9f87594840ae634e587041b8da37487c91",
          "artifact": "source-extracts/x06-S1-2418-2468.txt",
          "literal_from_dictionary_sha256": "bee2dd5ee40e955868a1651e9c679c9f87594840ae634e587041b8da37487c91"
        }
      ],
      "short_pertinent_quote": "Theorem 4.7.",
      "kind": "External primary mathematical premise; not a native registered support."
    },
    {
      "index": 4,
      "statement": "On a reduced projective variety over an algebraically closed trivially valued field, a genuine theta-psh potential is ordered below any USC scalar exactly when that order holds at all BJ divisorial valuations (4.22); for fixed continuous psi, sup(phi-psi) is continuous in the divisorial topology (4.28).",
      "passages": [
        {
          "unit": "x07",
          "url": "https://arxiv.org/pdf/1801.08229v4",
          "version": "1801.08229v4",
          "source_text_sha256": "659bb8d2e5335781041f03cdb168bac70126487bc0db394f3dac8cf1e9f076d0",
          "inclusive_LF": [
            2494,
            2541
          ],
          "sha256": "d521600de8d1a3e8a8ac95c3a5c6bdde1eb9668274cf065cdd3208652d3b3979",
          "artifact": "source-extracts/x07-S1-2494-2541.txt",
          "literal_from_dictionary_sha256": "d521600de8d1a3e8a8ac95c3a5c6bdde1eb9668274cf065cdd3208652d3b3979"
        }
      ],
      "short_pertinent_quote": "Theorem 4.22.",
      "kind": "External primary mathematical premise; not a native registered support."
    },
    {
      "index": 5,
      "statement": "For an irreducible projective variety over an algebraically closed trivially valued field, BJ 5.11 equates EP with compactness of normalized genuine PSH in the divisorial topology. For ample omega, 5.17 equates EP with continuity of envelopes of every finite continuous obstacle, and the envelope is genuine under EP; envelopes satisfy the sup-norm Lipschitz estimate.",
      "passages": [
        {
          "unit": "x08",
          "url": "https://arxiv.org/pdf/1801.08229v4",
          "version": "1801.08229v4",
          "source_text_sha256": "659bb8d2e5335781041f03cdb168bac70126487bc0db394f3dac8cf1e9f076d0",
          "inclusive_LF": [
            2754,
            2887
          ],
          "sha256": "a27b6d01787f2f77554c294d08827ed78f546cef4affb8020902aff09baf58d5",
          "artifact": "source-extracts/x08-S1-2754-2887.txt",
          "literal_from_dictionary_sha256": "a27b6d01787f2f77554c294d08827ed78f546cef4affb8020902aff09baf58d5"
        },
        {
          "unit": "x09",
          "url": "https://arxiv.org/pdf/1801.08229v4",
          "version": "1801.08229v4",
          "source_text_sha256": "659bb8d2e5335781041f03cdb168bac70126487bc0db394f3dac8cf1e9f076d0",
          "inclusive_LF": [
            2894,
            2976
          ],
          "sha256": "9e9789c16e6e0105ad20368fdf05e44daabb8ecbe2cb583d8790c7662ddb1ebd",
          "artifact": "source-extracts/x09-S1-2894-2976.txt",
          "literal_from_dictionary_sha256": "9e9789c16e6e0105ad20368fdf05e44daabb8ecbe2cb583d8790c7662ddb1ebd"
        }
      ],
      "short_pertinent_quote": "Theorem 5.11.",
      "kind": "External primary mathematical premise; not a native registered support."
    },
    {
      "index": 6,
      "statement": "For a smooth connected projective variety over an algebraically closed trivially valued characteristic-zero field, every nef class has EP and normalized PSH is compact (BJ 5.20-5.21). No ampleness or countability of the nef source class is required.",
      "passages": [
        {
          "unit": "x10",
          "url": "https://arxiv.org/pdf/1801.08229v4",
          "version": "1801.08229v4",
          "source_text_sha256": "659bb8d2e5335781041f03cdb168bac70126487bc0db394f3dac8cf1e9f076d0",
          "inclusive_LF": [
            2978,
            3064
          ],
          "sha256": "d3ca4292fe8b2ed4ba44e91cdfe75dcc582672904b6fd48fb43a478b9daba779",
          "artifact": "source-extracts/x10-S1-2978-3064.txt",
          "literal_from_dictionary_sha256": "d3ca4292fe8b2ed4ba44e91cdfe75dcc582672904b6fd48fb43a478b9daba779"
        }
      ],
      "short_pertinent_quote": "Then any θ ∈ Nef(X) has the envelope property.",
      "kind": "External primary mathematical premise; not a native registered support."
    },
    {
      "index": 7,
      "statement": "For a projective birational morphism pi:Y->X of projective varieties over an algebraically closed trivially valued field, if theta is approached by target classes theta_m having EP with theta_m-theta ample, BJ 5.13 gives an onto homeomorphic genuine psh pullback at theta. This premise is used only after original-target approaching EP.",
      "passages": [
        {
          "unit": "x08",
          "url": "https://arxiv.org/pdf/1801.08229v4",
          "version": "1801.08229v4",
          "source_text_sha256": "659bb8d2e5335781041f03cdb168bac70126487bc0db394f3dac8cf1e9f076d0",
          "inclusive_LF": [
            2754,
            2887
          ],
          "sha256": "a27b6d01787f2f77554c294d08827ed78f546cef4affb8020902aff09baf58d5",
          "artifact": "source-extracts/x08-S1-2754-2887.txt",
          "literal_from_dictionary_sha256": "a27b6d01787f2f77554c294d08827ed78f546cef4affb8020902aff09baf58d5"
        }
      ],
      "short_pertinent_quote": "Lemma 5.13.",
      "kind": "External primary mathematical premise; not a native registered support."
    },
    {
      "index": 8,
      "statement": "For a reduced projective variety over an algebraically closed trivially valued field and ample numerical classes, BJ 7.1-7.2 extend the actual symmetric intersection pairing by infima of genuine finite Hdom majorants, weakly USC and decreasing-net continuous. BJ 7.7-7.8 give concave translation-equivariant energy, the genuine finite-energy cone, mixed finiteness and normalization energy compatibility. These statements do not require smoothness or EP.",
      "passages": [
        {
          "unit": "x11",
          "url": "https://arxiv.org/pdf/1801.08229v4",
          "version": "1801.08229v4",
          "source_text_sha256": "659bb8d2e5335781041f03cdb168bac70126487bc0db394f3dac8cf1e9f076d0",
          "inclusive_LF": [
            3649,
            3889
          ],
          "sha256": "16208ee6a6df43b461fc984129af92d717f5b0c859850f1d2c91e95d572cb474",
          "artifact": "source-extracts/x11-S1-3649-3889.txt",
          "literal_from_dictionary_sha256": "16208ee6a6df43b461fc984129af92d717f5b0c859850f1d2c91e95d572cb474"
        }
      ],
      "short_pertinent_quote": "In this section, X denotes a projective variety",
      "kind": "External primary mathematical premise; not a native registered support."
    },
    {
      "index": 9,
      "statement": "For a reduced projective variety over an algebraically closed trivially valued field, BJ 7.14 and 7.18-7.21 extend the signed finite-energy pairing, construct positive genuine mixed Radon measures for genuine nef entries, give their raw intersection mass and model formula with ord_E(t), normalization pushforward, integrability of finite-energy tests, unbounded genuine decreasing-net continuity, and weighted continuity when the limiting psh test is integrable. The defining weighted integral is test-containing pairing minus zero-test pairing.",
      "passages": [
        {
          "unit": "x12",
          "url": "https://arxiv.org/pdf/1801.08229v4",
          "version": "1801.08229v4",
          "source_text_sha256": "659bb8d2e5335781041f03cdb168bac70126487bc0db394f3dac8cf1e9f076d0",
          "inclusive_LF": [
            3890,
            4135
          ],
          "sha256": "e3aed860597e20cf9bc441ca10b30bf8b8f043fc2d24ca18ed590e1b63e59767",
          "artifact": "source-extracts/x12-S1-3890-4135.txt",
          "literal_from_dictionary_sha256": "e3aed860597e20cf9bc441ca10b30bf8b8f043fc2d24ca18ed590e1b63e59767"
        }
      ],
      "short_pertinent_quote": "Theorem 7.18.",
      "kind": "External primary mathematical premise; not a native registered support."
    },
    {
      "index": 10,
      "statement": "For a reduced projective variety over an algebraically closed trivially valued field and ample omega, BJ 8.2-8.8 define outer energy, continuous on decreasing USC nets and equal to genuine energy on psh; under EP it equals energy of the genuine envelope. For fixed real PL f, its expansion at any actual E1 potential is E_down(phi+tf)=E(phi)+t integral(f MA_BJ(phi))+O(t^2), uniformly in phi. Both signed continuous directions follow by uniform PL approximation. No smoothness hypothesis enters these global derivative theorems.",
      "passages": [
        {
          "unit": "x15",
          "url": "https://arxiv.org/pdf/1801.08229v4",
          "version": "1801.08229v4",
          "source_text_sha256": "659bb8d2e5335781041f03cdb168bac70126487bc0db394f3dac8cf1e9f076d0",
          "inclusive_LF": [
            4674,
            4962
          ],
          "sha256": "0d8d872a3323e4100bae27cb6e8b676a500abdf1989b7c1e024af35849a97912",
          "artifact": "source-extracts/x15-S1-4674-4962.txt",
          "literal_from_dictionary_sha256": "0d8d872a3323e4100bae27cb6e8b676a500abdf1989b7c1e024af35849a97912"
        }
      ],
      "short_pertinent_quote": "where the implicit constant in the O is uniform with respect to ϕ.",
      "kind": "External primary mathematical premise; not a native registered support."
    },
    {
      "index": 11,
      "statement": "For a reduced projective variety over an algebraically closed trivially valued field and ample omega, BJ 9.1 defines intrinsic dual energy on probability Radon measures by the supremum over genuine E1. BJ 9.9 gives USC outer-energy duality, and 9.11-9.12 identify a genuinely attained E1 maximizer with its actual Monge-Ampere equation, using f and -f and PL density. No inverse-support operator or EP is assumed in this identification.",
      "passages": [
        {
          "unit": "x16",
          "url": "https://arxiv.org/pdf/1801.08229v4",
          "version": "1801.08229v4",
          "source_text_sha256": "659bb8d2e5335781041f03cdb168bac70126487bc0db394f3dac8cf1e9f076d0",
          "inclusive_LF": [
            4970,
            5035
          ],
          "sha256": "0d1fe3897017983ff0019ce21e31375b437e0ec6ac241f485c4b4be1ce7a3bfb",
          "artifact": "source-extracts/x16-S1-4970-5035.txt",
          "literal_from_dictionary_sha256": "0d1fe3897017983ff0019ce21e31375b437e0ec6ac241f485c4b4be1ce7a3bfb"
        },
        {
          "unit": "x17",
          "url": "https://arxiv.org/pdf/1801.08229v4",
          "version": "1801.08229v4",
          "source_text_sha256": "659bb8d2e5335781041f03cdb168bac70126487bc0db394f3dac8cf1e9f076d0",
          "inclusive_LF": [
            5110,
            5158
          ],
          "sha256": "8c4787d9dd7c44e5dff7df46694689982d269d05ef3f964e8a769bed43ef3154",
          "artifact": "source-extracts/x17-S1-5110-5158.txt",
          "literal_from_dictionary_sha256": "8c4787d9dd7c44e5dff7df46694689982d269d05ef3f964e8a769bed43ef3154"
        }
      ],
      "short_pertinent_quote": "and replacing f with −f yields the result.",
      "kind": "External primary mathematical premise; not a native registered support."
    },
    {
      "index": 12,
      "statement": "On an irreducible projective variety over an algebraically closed trivially valued field, BJ 9.15-9.16 bound J on dual maximizing nets, and 9.19 gives target L1 convergence for weakly convergent genuine psh nets with eventually bounded J against every finite-dual-energy target. BJ 9.20 says finite intrinsic dual energy is equivalent to integrability of all actual E1 potentials. General finite-energy concavity, I/J and scaling estimates used here are those of 7.28-7.33. No smoothness or support condition is imposed.",
      "passages": [
        {
          "unit": "x13",
          "url": "https://arxiv.org/pdf/1801.08229v4",
          "version": "1801.08229v4",
          "source_text_sha256": "659bb8d2e5335781041f03cdb168bac70126487bc0db394f3dac8cf1e9f076d0",
          "inclusive_LF": [
            4165,
            4340
          ],
          "sha256": "c915032bf0eebe8ad404adbb1262524c60dd0957a37dd0431389370c7693214f",
          "artifact": "source-extracts/x13-S1-4165-4340.txt",
          "literal_from_dictionary_sha256": "c915032bf0eebe8ad404adbb1262524c60dd0957a37dd0431389370c7693214f"
        },
        {
          "unit": "x18",
          "url": "https://arxiv.org/pdf/1801.08229v4",
          "version": "1801.08229v4",
          "source_text_sha256": "659bb8d2e5335781041f03cdb168bac70126487bc0db394f3dac8cf1e9f076d0",
          "inclusive_LF": [
            5180,
            5301
          ],
          "sha256": "8fea27f105319057b1c2362e8de17ca887a5bcbb1d1070f757aaf0be2cc75b31",
          "artifact": "source-extracts/x18-S1-5180-5301.txt",
          "literal_from_dictionary_sha256": "8fea27f105319057b1c2362e8de17ca887a5bcbb1d1070f757aaf0be2cc75b31"
        }
      ],
      "short_pertinent_quote": "A Radon probability measure µ ∈ M has finite energy iff E 1 ⊂ L1 (µ).",
      "kind": "External primary mathematical premise; not a native registered support."
    },
    {
      "index": 13,
      "statement": "On a reduced projective variety over an algebraically closed trivially valued field with ample omega, BJ 7.40-7.44 give genuine unbounded E1 strict-winning Borel locality, mixed open locality and comparison. On an equidimensional projective variety, 10.3-10.6 give equality of genuine MA iff I=0 iff the potential difference is locally constant, and domination of a psh potential by an E1 potential when the inequality holds almost everywhere for its MA. These theorems require neither smoothness nor EP; irreducibility makes the difference one constant.",
      "passages": [
        {
          "unit": "x14",
          "url": "https://arxiv.org/pdf/1801.08229v4",
          "version": "1801.08229v4",
          "source_text_sha256": "659bb8d2e5335781041f03cdb168bac70126487bc0db394f3dac8cf1e9f076d0",
          "inclusive_LF": [
            4529,
            4602
          ],
          "sha256": "18e1abc1b9d68ea1a5ffbfb4c1d03eeb30a5b4fac482f44f9ea2b9a64c5d4233",
          "artifact": "source-extracts/x14-S1-4529-4602.txt",
          "literal_from_dictionary_sha256": "18e1abc1b9d68ea1a5ffbfb4c1d03eeb30a5b4fac482f44f9ea2b9a64c5d4233"
        },
        {
          "unit": "x19",
          "url": "https://arxiv.org/pdf/1801.08229v4",
          "version": "1801.08229v4",
          "source_text_sha256": "659bb8d2e5335781041f03cdb168bac70126487bc0db394f3dac8cf1e9f076d0",
          "inclusive_LF": [
            5426,
            5477
          ],
          "sha256": "bb829a66d12c3edcf4a1630b08e62a103f7cd7e61972c6c7a16d5a5190a06466",
          "artifact": "source-extracts/x19-S1-5426-5477.txt",
          "literal_from_dictionary_sha256": "bb829a66d12c3edcf4a1630b08e62a103f7cd7e61972c6c7a16d5a5190a06466"
        }
      ],
      "short_pertinent_quote": "Corollary 10.6 (Domination principle).",
      "kind": "External primary mathematical premise; not a native registered support."
    },
    {
      "index": 14,
      "statement": "For a reduced projective variety over an algebraically closed trivially valued field and ample omega, BJ 12.8 says EP is equivalent to surjectivity of the genuine E1 Monge-Ampere operator onto all intrinsic finite-dual-energy probability Radon measures. Its EP-to-surjectivity proof obtains an actual normalized psh subnet limit using general EP compactness, bounded J, target integral continuity and energy USC to attain the variational supremum. The smooth 12.9 corollary is a separate statement.",
      "passages": [
        {
          "unit": "x20",
          "url": "https://arxiv.org/pdf/1801.08229v4",
          "version": "1801.08229v4",
          "source_text_sha256": "659bb8d2e5335781041f03cdb168bac70126487bc0db394f3dac8cf1e9f076d0",
          "inclusive_LF": [
            6092,
            6146
          ],
          "sha256": "6bb578ad44c78dbe18f74ff227167f6d88a7660585784c3d499fac7a48f2705a",
          "artifact": "source-extracts/x20-S1-6092-6146.txt",
          "literal_from_dictionary_sha256": "6bb578ad44c78dbe18f74ff227167f6d88a7660585784c3d499fac7a48f2705a"
        }
      ],
      "short_pertinent_quote": "This proves (i)⇒(ii).",
      "kind": "External primary mathematical premise; not a native registered support."
    },
    {
      "index": 15,
      "statement": "For an irreducible projective variety over an algebraically closed trivially valued field, ample omega with EP, and a finite continuous obstacle f, BJ 13.1 gives genuine continuous envelope p and integral((f-p) MA_BJ(p))=0. Its continuous proof uses P(p+t(f-p))=p and the continuous energy derivative. EP is a stated hypothesis.",
      "passages": [
        {
          "unit": "x21",
          "url": "https://arxiv.org/pdf/1801.08229v4",
          "version": "1801.08229v4",
          "source_text_sha256": "659bb8d2e5335781041f03cdb168bac70126487bc0db394f3dac8cf1e9f076d0",
          "inclusive_LF": [
            6302,
            6359
          ],
          "sha256": "fa43d7783b4a4bc09ecddf5dc9051ca0f2b97a44aaa137243baa56fa4464de79",
          "artifact": "source-extracts/x21-S1-6302-6359.txt",
          "literal_from_dictionary_sha256": "fa43d7783b4a4bc09ecddf5dc9051ca0f2b97a44aaa137243baa56fa4464de79"
        }
      ],
      "short_pertinent_quote": "and we assume that the envelope property holds for ω",
      "kind": "External primary mathematical premise; not a native registered support."
    },
    {
      "index": 16,
      "statement": "For a projective scheme of dimension n over a complete valued field and actual rational semiample bundles, BE 1805.01016v3 7.14 makes FS-limit metrics psh-regularizable on the same bundles. Its 8.3-8.5 construct positive continuous mixed Radon measures of raw fundamental-cycle intersection mass, uniform continuity and complete-field pushforward. The full fundamental cycle includes generic lengths. BE 8.18-8.21 identify model Deligne pairing and vertical intersections, including the zero-dimensional induction and relatively regular section proof. BJ 7.23 identifies this continuous operator with its energy-pairing operator.",
      "passages": [
        {
          "unit": "x22",
          "url": "https://arxiv.org/pdf/1805.01016v3",
          "version": "1805.01016v3",
          "source_text_sha256": "8e584521fe3d41f179bef93d14315414ac7796532c65518c1861717416f99233",
          "inclusive_LF": [
            2358,
            2379
          ],
          "sha256": "e8a2fa603ab776d8fe4365fa5223a77a08f1d03c28595fc0f0c95fcdafc1eb8b",
          "artifact": "source-extracts/x22-S7-2358-2379.txt",
          "literal_from_dictionary_sha256": "e8a2fa603ab776d8fe4365fa5223a77a08f1d03c28595fc0f0c95fcdafc1eb8b"
        },
        {
          "unit": "x23",
          "url": "https://arxiv.org/pdf/1805.01016v3",
          "version": "1805.01016v3",
          "source_text_sha256": "8e584521fe3d41f179bef93d14315414ac7796532c65518c1861717416f99233",
          "inclusive_LF": [
            2611,
            2779
          ],
          "sha256": "1ffe08a5900d483d40d3a6de9e5a4efdc6b6efa1efc4df7c6f35d7169c408993",
          "artifact": "source-extracts/x23-S7-2611-2779.txt",
          "literal_from_dictionary_sha256": "1ffe08a5900d483d40d3a6de9e5a4efdc6b6efa1efc4df7c6f35d7169c408993"
        },
        {
          "unit": "x24",
          "url": "https://arxiv.org/pdf/1805.01016v3",
          "version": "1805.01016v3",
          "source_text_sha256": "8e584521fe3d41f179bef93d14315414ac7796532c65518c1861717416f99233",
          "inclusive_LF": [
            3125,
            3202
          ],
          "sha256": "1db7782548c52fe9ce85efc3d4c88ed30a65323334bf8da1bc8a21483dcea58b",
          "artifact": "source-extracts/x24-S7-3125-3202.txt",
          "literal_from_dictionary_sha256": "1db7782548c52fe9ce85efc3d4c88ed30a65323334bf8da1bc8a21483dcea58b"
        },
        {
          "unit": "x12",
          "url": "https://arxiv.org/pdf/1801.08229v4",
          "version": "1801.08229v4",
          "source_text_sha256": "659bb8d2e5335781041f03cdb168bac70126487bc0db394f3dac8cf1e9f076d0",
          "inclusive_LF": [
            3890,
            4135
          ],
          "sha256": "e3aed860597e20cf9bc441ca10b30bf8b8f043fc2d24ca18ed590e1b63e59767",
          "artifact": "source-extracts/x12-S1-3890-4135.txt",
          "literal_from_dictionary_sha256": "e3aed860597e20cf9bc441ca10b30bf8b8f043fc2d24ca18ed590e1b63e59767"
        }
      ],
      "short_pertinent_quote": "for any complete field extension F/K",
      "kind": "External primary mathematical premise; not a native registered support."
    }
  ]
}

END MATHEMATICAL DATA



BEGIN MATHEMATICAL DATA: COMPLETE exact literal body dictionary for both catalogues
{
  "0a052b9c946f29ceacd251e92b166dc557ee078e76c19ff17f15107ace4dbd7d": "Notation and conventions.\n     • We use the standard abbreviations usc for ‘upper semicontinuous’, lsc for ‘lower\n       semicontinuous’, wlog for ‘without loss of generality”, and iff for ‘if and only if’.\n       We also use PL for ‘piecewise linear’, snc for ‘simple normal crossing’, and psh for\n       ‘plurisubharmonic’.\n     • Following the Bourbaki convention, all compact and locally compact topological\n       spaces are required to be Hausdorff.\n     • A net in a set X is a family (xi )i∈I of elements of X indexed by a directed set, i.e.\n       a partially preordered set in which any two elements are dominated by a third one.\n       A subnet of (xi )i∈I is a net of the form (xϕ(j) )j∈J where ϕ : J → I is increasing and\n       final, i.e. for each i ∈ I there exists j ∈ J with ϕ(j) ≥ i. A (Hausdorff) topological\n       space X is compact iff every net in X admits a convergent subnet.\n     • If X is a Hausdorff topological space, and ϕ : X → R ∪ {±∞} is any function, then\n       the usc regularization ϕ? of ϕ is the smallest usc function with ϕ? ≥ ϕ. Concretely,\n       ϕ? (x) = lim supy→x ϕ(y). The lsc regularization is defined by ϕ? = −(−ϕ)? .\n     • We work over an algebraically closed field k, for the most part of arbitrary charac-\n       teristic. In this paper, a variety (over k) is a separated k-scheme of finite type that\n       is reduced, but not necessarily irreducible, nor even equidimensional.\n\f10                      SÉBASTIEN BOUCKSOM AND MATTIAS JONSSON\n\n     • For any variety X, we denote by Pic(X) the Picard group of isomorphism classes of\n       line bundles. Elements of the associated Q-vector space Pic(X)Q := Pic(X) ⊗Z Q\n       can be viewed as isomorphism classes of Q-line bundles.\n     • If X is a projective variety, we denote by N1 (X) the finite dimensional R-vector\n       space of numerical classes of R-Cartier divisors on X. It comes with a surjective\n       linear map Pic(X)R → N1 (X) induced by L 7→ c1 (L) .\n     • Ample classes form a nonempty open convex cone Amp(X) ⊂ N1 (X), whose closure\n       is the closed convex cone Nef(X) ⊂ N1 (X) of nef classes. For θ, θ0 ∈ N1 (X), we\n       write θ ≥ θ0 if θ − θ0 is nef. We generally denote by θ an element of N1 (X), and by\n       ω an element of Amp(X).\n     • The cone Psef(X) ⊂ N1 (X) of pseudoeffective classes is defined as the closed convex\n       cone generated by classes of effective R-Cartier divisors; its interior Big(X) is the\n       cone of big classes.\n     • A section of a line bundle on X is regular if it does not vanish identically along any\n       irreducible component of X. Its zero scheme is then a Cartier divisor on X.",
  "4b8a7305f07bd16782a74a0b620eb098c455aa96fb2bfac4917b43bcc6fa1044": "Definition 1.10. We say that a test configuration X for X is integrally closed if the scheme\nX is integrally closed in the generic fiber Xk($) of π : X → A1 .\n  In other words, X is integrally closed iff it can be covered by affine open subsets U =\nSpec A such that the k[$]-algebra A is integrally closed in Ak($) . Note that X is normal iff\nX is normal and X is integrally closed.\nExample 1.11. The trivial test configuration Xtriv = X × A1 is integrally closed.\n   The integral closure of any test configuration X in Xk($) defines a finite, Gm -equivariant\nmorphism Xe → X (because the scheme X , being of finite type over a field, is excellent),\nwhich induces an isomorphism on the generic fibers over A1 . Thus Xe is an integrally closed\ntest configuration for X, which we simply call the integral closure of X . It is characterized\nas the unique integrally closed test configuration that dominates X via a finite morphism.\n   When X is normal, the integral closure Xe of any test configuration X coincides with its\nnormalization X ν (see also Remark 1.22).\nLemma 1.12 (Zariski’s main theorem). If X is integrally closed and µ : X 0 → X is a\nmorphism of test configurations, then µ? OX 0 = OX .\nProof. By coherence of direct images, µ? OX 0 is a finite OX -module. Sections of µ? OX 0 on\nan open U ⊂ X are thus rational functions on U that are regular on the generic fiber and\nintegral over OU , and hence belong to OU .                                                \u0003\n  Integral closedness admits the following characterization, a ‘vertical version’ of the usual\nSerre criterion for normality.\nTheorem 1.13. A test configuration X is integrally closed iff it is:\n   (i) vertically R1 , in the sense that X is regular at each generic points of X0 ;\n  (ii) vertically S2 , in the sense that depth OX ,ξ ≥ min{2, dim OX ,ξ } for all ξ ∈ X0 .\nRemark 1.14. Condition (i) was called partially normal in [Oda13, Definition 3.7].\nLemma 1.15. For any test configuration X for X, we have:\n   (i) X is vertically S2 ⇐⇒ X0 is S1 , i.e. without embedded points;\n  (ii) X is S2 ⇐⇒ X is S2 and X is vertically S2 .\n\f             GLOBAL PLURIPOTENTIAL THEORY OVER A TRIVIALLY VALUED FIELD                       17\n\nProof. Since X0 is a Cartier divisor, each ξ ∈ X0 satisfies\n                depth OX ,ξ = depth OX0 ,ξ + 1,    dim OX ,ξ = dim OX0 ,ξ + 1.\nThis yields (i), while (ii) is a direct consequence of the isomorphism\n                                      X \\ X0 ≃ X × Gm .\n                                                                                              \u0003\nCorollary 1.16. For any test configuration X , the following are equivalent:\n   (i) X0 is reduced;\n  (ii) X is integrally closed, and X0 is generically reduced.\nProof. The scheme X0 is reduced iff it is generically reduced and S1 . By Lemma 1.15, X0\nis thus reduced iff it is generically reduced and X is vertically S2 . Finally, X0 generically\nreduced implies that X is regular at each generic point of X0 , since the latter is a Cartier\ndivisor. The result is now a consequence of Theorem 1.13.                                   \u0003\n  Before entering the proof of Theorem 1.13, we introduce some terminology that will be\nused throughout this paper.\nDefinition 1.17. Let X be a test configuration for X.\n    (i) A vertical fractional ideal a on X is a coherent fractional ideal sheaf that is Gm -\n        invariant, and trivial outside X0 .\n   (ii) The polar scheme P ⊂ X of a vertical fractional ideal a is the closed subscheme of\n        X defined by the ideal of poles p := {f ∈ OX | f a ⊂ OX }.\n  (iii) A vertical Cartier divisor D on X is a Gm -invariant Cartier divisor with support in\n        X0 .\n   Note that P in (ii) is supported in X0 , a being trivial outside X0 .\n   Vertical Cartier divisors on X are in 1–1 correspondence with locally principal vertical\nfractional ideals of X , via D 7→ OX (D). If D is further effective, then it coincides with the\npolar scheme of OX (D).\nLemma 1.18. A test configuration X is integrally closed iff every vertical fractional ideal\na on X that is integral over OX satisfies a ⊂ OX .\nProof. The ‘only if’ part is obvious. Conversely, consider the integral closure µ : Xe → X .\nThen a := µ? OXe is a vertical fractional ideal that is integral over OX , and the ‘if part’\nfollows.                                                                                  \u0003\n  The next result is the key step in the proof of Theorem 1.13.\nLemma 1.19. Let X be an integrally closed test configuration for X, and a be a vertical\nfractional ideal on X . Then:\n     (i) every associated point of the scheme of poles of a is a generic point of X0 ;\n    (ii) X is vertically R1 .\nProof. We follow the usual proof of Serre’s criterion for normality. Let p = {f ∈ OX |\nf a ∈ OX } be the ideal of poles, and pick an associated point ξ ∈ X0 of the polar scheme\nP ⊂ X . By definition of an associated point, there exists f ∈ OX ,ξ such that f ∈      / pξ but\nf mξ ⊂ pξ , with mξ the maximal ideal of OX ,ξ . Then f mξ · aξ is an ideal of OX ,ξ , and hence\nf mξ ·aξ ⊂ mξ or f mξ ·aξ = OX ,ξ . In the former case, the usual determinant trick implies that\n\f18                       SÉBASTIEN BOUCKSOM AND MATTIAS JONSSON\n\nf aξ is integral over OX ,ξ . Since X is integrally closed, we infer f aξ ⊂ OX ,ξ , i.e. f ∈ pξ , a\ncontradiction. We thus necessarily have f mξ · aξ = OX ,ξ , which proves that mξ is invertible,\nand hence that OX ,ξ is a DVR. This proves (i), as well as (ii), taking a = OX (X0 ).            \u0003\nProof of Theorem 1.13. Assume that X is integrally closed. By Lemma 1.19, X is vertically\nR1 , and the polar scheme X0 of OX (X0 ) has no embedded points. By Lemma 1.15, X is\nthus vertically S2 , which proves (i)=⇒(ii).\n   Assume, conversely, that X is vertically R1 and S2 , and pick a vertical fractional ideal a on\nX that is integral over OX . According to Lemma 1.18, we need to show that a ⊂ OX , which\nmeans that its ideal of poles p := {f ∈ OX | f a ⊂ OX } is trivial. Arguing by contradiction,\nsuppose that the polar scheme P is non-empty, and pick an associated point ξ ∈ X0 of P .\nIf dim OX ,ξ = 1, then ξ is a generic point of X0 . Since X is vertically R1 , OX ,ξ is regular,\nand hence integrally closed. Thus aξ ⊂ OX ,ξ , which contradicts ξ ∈ P . We thus have\ndim OX ,ξ ≥ 2, and hence depth OX ,ξ ≥ 2, since X is vertically S2 .\n   Since ξ is an associated point of P , we can find, as above, f ∈ OX ,ξ such that f ∈   / pξ but\nf mξ ⊂ bξ , i.e. f mξ · aξ ⊂ OX ,ξ . Since f ∈\n                                             / pξ , there exists g ∈ aξ such that h := f g ∈\n                                                                                           / OX ,ξ .\nWrite h = a/b with a, b ∈ OX ,ξ and b a non-zerodivisor. Then a ∈      / (b), but amξ ⊂ (b). Thus\nξ is an associated point of the Cartier divisor D = (b = 0), which contradicts depth OD,ξ ≥\n1.                                                                                               \u0003\n   Generalizing [BHJ17, §4.2], we associate to every irreducible component E of the central\nfiber X0 of an integrally closed test configuration X a divisorial valuation vE ∈ X div , as\nfollows.\n   By Theorem 1.13, the local ring of X at the generic point of E is a DVR (compare [CLT09,\nLemme 2.1]), and hence defines a divisorial valuation ordE : k(X )× → Z. As in [BHJ17,\nDefinition 4.4], we set bE := ordE ($) = ordE (X0 ), and define a valuation vE on X as the\nrestriction of wE := b−1\n                      E ordE to\n                              k(X) ⊂ k(X)($) = k(Xtriv ) ≃ k(X ).\nSince wE   is k × -invariant and w   E ($) = 1, we have σ(vE ) = wE .\n\nLemma 1.20. A valuation v on X is divisorial iff v = vE for an irreducible component E\nof some integrally closed test configuration X for X.\n   This follows from [BHJ17, Theorem 4.6]. While the latter assumes X normal, its proof is\na rather simple consequence of a theorem of Zariski [KM98, Lemma 2.45], which does not\ndepend on this assumption.\nExample 1.21. Assume X is smooth, and let Z ⊂ X be a smooth irreducible subvariety.\nThe vanishing order at the generic point of Z is then a divisorial valuation ordZ ∈ X div ;\nindeed, denoting by π : X e → X the blowup of Z and E its exceptional divisor, we have\nordZ = ordE . Alternatively, ordZ = vP with P the exceptional divisor of the blowup X →\nXtriv of Z × {0}, i.e. the deformation to the normal cone of Z in X (see Example 1.7).\nRemark 1.22. The normalization X ν of a test configuration X for X is a test configuration\nfor the normalization X ν of X. The normalization morphism X ν → X factors through\nthe integral closure Xe, and the induced morphism X ν → Xe is an isomorphism over each\ngeneric point of Xe0 , Xe being regular at such points (compare [Oda13, Lemma 3.9]). As",
  "0d683eecb0ed666f06dd4f29a6c98da6fb22286f60525105a6f00d00e527c912": "                  2. Piecewise linear and Fubini–Study functions\n  As before, X denotes a projective variety. We introduce the classes of piecewise linear\nand Fubini–Study functions on the Berkovich space X an , and interpret them in terms of test\nconfigurations, along the lines of [BHJ17].\n\n2.1. Flag ideals and piecewise linear functions. Recall from §1.1 that to any ideal\nb ⊂ OX is associated a continuous function X an → [0, +∞] given by v 7→ v(b). For reasons\nthat will become clearer later, we define\n                                        log |b| : X an → [−∞, 0]\nby setting log |b|(v) := −v(b). The function log |b| is homogeneous with respect to the\nscaling action of R>0 , and (1.2) yields\n              log |b · b0 | = log |b| + log |b0 |,    log |b + b0 | = max{log |b|, log |b0 |}   (2.1)\nfor all ideals b, b0 ⊂ OX .\n   Following [Oda13, BHJ17], we define a flag ideal a as a vertical fractional ideal on Xtriv =\nX × A1 , i.e. a Gm -invariant, coherent fractional ideal sheaf that is trivial on X × Gm ,\naccording to our conventions. We then have a weight decomposition\n                                          X\n                                      a=       aλ $−λ                                     (2.2)\n                                                     λ∈Z\n\nfor a decreasing sequence of ideals aλ ⊂ OX such that aλ = OX for λ \u001c 0 and aλ = 0 for\nλ \u001d 0. For any v ∈ X an with Gauss extension σ(v), we have\n                                     σ(v)(a) = min{v(aλ ) − λ}.\n                                                      λ\n\nWe define a continuous function ϕa : X an → R by setting ϕa (v) = −σ(v)(a), i.e.\n                                       ϕa = max{log |aλ | + λ}.                                 (2.3)\n                                                λ\n\nFor any two flag ideals a, a0 , we have\n                            ϕa·a0 = ϕa + ϕa0 ,        ϕa+a0 = max{ϕa , ϕa0 }.                   (2.4)\n\f              GLOBAL PLURIPOTENTIAL THEORY OVER A TRIVIALLY VALUED FIELD                      21\n\nDefinition 2.1. We define the space of piecewise linear (PL) functions on X an as the\nQ-linear subspace\n                                      PL(X) ⊂ C0 (X)\ngenerated by all functions ϕa attached to flag ideals a.\n  By (2.4), the subset\n                    PL+ (X) := m−1 ϕa | m ∈ Z>0 , a flag ideal ⊂ PL(X)\n                              \b\n                                                                                           (2.5)\n    is stable under sums and finite maxima, and contains all Q-valued constant functions. It\nis also stable under multiplication by Q+ : if c ∈ Q+ , then cϕa = m−1 ϕamc for any m ∈ Z>0\nis such thatP mc ∈−λZ. Further, it is stable     under the scaling action of Q>0 : if t ∈ Q>0\n                                         −1 ϕ 0 , where m ∈ Z\nand a =         aλ $   , then t · ϕ a = m    a                  >0 is such that mt ∈ Z, and\n  0\n       P m λ −mtλ\na = λ aλ $           .\n    It follows that the Q-vector space PL(X) is stable under finite maxima and minima, and\nunder the scaling action of Q>0 , and it contains all constant Q-valued functions. Further,\nany function in PL(X) can be written as a difference of functions in PL+ (X), and is Q-valued\non X div .\n    We refer to Theorem 2.7 and Appendix A for an interpretation of PL functions in terms\nof test configurations and PL functions on simplicial complexes, respectively. In our setting,\nPL functions play the role of smooth functions in the complex analytic case, as illustrated\nby the next result.\nTheorem 2.2. The space PL(X) is dense in C0 (X) for the topology of uniform convergence.\n  By the ‘lattice version’ of the Stone–Weierstrass theorem, this is a direct consequence of\nthe following result.\nLemma 2.3. The Q-linear subspace PL(X) ⊂ C0 (X) is stable under max (and hence min),\ncontains the constants in Q, and separates the points of X an .\nProof. The first two properties are clear. As mentioned in §1.1, the topology of X an is\ngenerated by the functions log |b| attached to ideals b ⊂ OX . For any two v, v 0 ∈ X an we\ncan thus find an ideal b such that log |b|(v) 6= log |b|(v 0 ) (since X an is Hausdorff), and it\nfollows that ϕ := max{log |b|, −m} ∈ PL(X) separates v, v 0 for m \u001d 1.                        \u0003\nRemark 2.4. We will occasionally consider the R-vector space PL(X)R ⊂ C0 (X) generated\nby PL(X). As opposed to the latter, PL(X)R is not closed under max.\nExample 2.5. Given a closed subscheme Z ⊂ X with ideal b ⊂ OX , the function\n                                   ϕZ := max{log |b|, −1}\n          +\nlies in PL (X), since ϕZ = ϕa with a = b + ($). Note that\n                                   t · ϕZ = max{log |b|, −t}                               (2.6)\nfor all t ∈ Q>0 .\nExample 2.6. Assume X is a smooth irreducible curve, and recall the description of X an\nin §1.1.6. As a special case of Example 2.5, each p ∈ X(k) defines a function ϕp ∈ PL+ (X)\nthat satisfies for all q ∈ X(k) and t ∈ [0, +∞]\n                                        \u001a\n                             ?            max{−t, −1} if q = p;\n                            ιq ϕp (t) =\n                                          0            otherwise.\n\f22                       SÉBASTIEN BOUCKSOM AND MATTIAS JONSSON\n                                                                                        P\nUsing (2.6) and the fact that every nontrivial ideal of X is of the form b = OX (− i ai pi )\nfor a finite set (pi ) in X(k) and ai ∈ Z>0 , one checks that the functions t · ϕp with t ∈ Q>0\nand p ∈ X(k) span PL(X). A function ϕ ∈ C0 (X) is PL iff ϕ is constant on all but finitely\nmany rays of X an and Q-PL on these rays, and ϕ ∈ PL+ (X) iff ϕ is further convex (and\nhence decreasing, being bounded) on each ray.\n2.2. PL functions and test configurations. Let X be a test configuration for X, and\nrecall that Gauss extension of (semi)valuations yields an embedding σX : X an ,→ X an onto\nthe set of k × -invariant semivaluations w ∈ X an such that w(X0 ) = w($) = 1.\n   Recall also that a vertical Q-Cartier divisor on X means a Gm -invariant Q-Cartier divisor\nwith support in X0 (see Example 1.5). Such divisors form a finite dimensional Q-vector space,\ndenoted by\n                                          VCar(X )Q .\n     To each D ∈ VCar(X )Q we associate a continuous function ϕD ∈ C0 (X) by setting\n                                        ϕD (v) := σX (v)(D)\nfor v ∈ X an , where the right-hand side is defined as m−1 σX (v)(OX (−mD)) for any choice\nof m ∈ Z>0 such that mD is a Cartier divisor (and hence D ≥ 0 ⇒ ϕD ≥ 0).\n   The map D 7→ ϕD is Q-linear, and invariant under pull-back: if µ : X 0 → X is a morphism\nof test configurations then σX 0 (v)(µ? D) = σX (v)(D) for all v ∈ X an , and hence ϕµ? D = ϕD .\nIt thus gives rise to a Q-linear map\n                                   lim VCar(X )Q → C0 (X),                                 (2.7)\n                                   −→\n                                    X\n\nwhere the direct limit ranges over the directed poset of (isomorphism classes of) test con-\nfigurations (or merely integrally closed ones, since they form a cofinal subset).\nTheorem 2.7. The map D 7→ ϕD in (2.7) induces a Q-linear isomorphism\n                                   lim VCar(X )Q ≃ PL(X).\n                                   −→\n                                   X\n\nLemma 2.8. Let X be an integrally closed test configuration for X, and D ∈ VCar(X )Q .\nThen D is effective iff ϕD (vE ) ≥ 0 for each irreducible component E of X0 .\nProof. After passing to a multiple, we may assume that D is Cartier. Since σX (vE ) =\nb−1                                             −1\n  E ordE , Lemma 1.23 shows that −ϕD (vE ) = bE ordE (OX (−D)) is nonnegative for all E\niff OX (−D) ⊂ OX , which is also equivalent to D being effective.                     \u0003\nLemma 2.9. For any ϕ ∈ C0 (X), the following properties are equivalent:\n   (i) ϕ ∈ PL+ (X);\n  (ii) there exists a test configuration X that dominates Xtriv via µ : X → Xtriv , and a\n       µ-semiample vertical Q-divisor D ∈ VCar(X )Q such that ϕ = ϕD .\nProof. Assume (i), and write ϕ = m−1 ϕa for a flag ideal a on Xtriv and m ∈ Z>0 . Denote by\nµ : X → Xtriv the blowup of a, so that a · OX = OX (E) with E ∈ VCar(X ). Then ϕ = ϕD\nwith D := m−1 E ∈ VCar(X )Q , which is µ-semiample. This proves (i)⇒(ii). Conversely,\nassume (ii), and pick m sufficiently divisible such that OX (mD) is µ-globally generated.\nThen OX (mD) = a · OX with a := µ? OX (mD), and hence ϕ = m−1 ϕa , which proves\n(ii)⇒(i).                                                                                 \u0003\n\f             GLOBAL PLURIPOTENTIAL THEORY OVER A TRIVIALLY VALUED FIELD                        23\n\nProof of Theorem 2.7. Lemma 2.8 implies that (2.7) is injective. Any D ∈ VCar(X )Q with\nµ : X → Xtriv can be written as a difference of µ-(semi)ample divisors; on the other hand,\nany ϕ ∈ PL(X) is a difference of functions in PL+ (X), and Lemma 2.9 thus shows that the\nimage of (2.7) is precisely PL(X).                                                      \u0003\n  Next we prove a result that will be used in §4.4.\nDefinition 2.10. Given a flag ideal a, we define the set Σa ⊂ X div of Rees valuations of a\nas the finite set of divisorial valuations associated to the irreducible components of X0 , where\nX → Xtriv is the integral closure of the blowup of a.\n   As the blowup of any ideal is canonically isomorphic to the blowup of any power of that\nideal, we have Σar = Σa for any r ≥ 1.\nRemark 2.11. Let X → Xtriv be the integral closure of the blowup along a flag ideal a ⊂\nOXtriv , and (Ei ) the irreducible components of X0 . The Rees valuations of a are then the\nvaluations vEi ∈ X div on X. Note that the terminology is a bit abusive, as (assuming X is\nnormal) the divisorial valuations ordEi on X can also be seen as the Rees valuations of the\nideal a.\nLemma 2.12. Every divisorial valuation is a Rees valuation of some flag ideal. More\ngenerally, for any finite subset Σ ⊂ X div there exists a flag ideal a of X such that Σ ⊂ Σa .\nProof. It suffices to consider the case Σ = {v}, v ∈ X div . By Lemma 1.20, there exists an\nintegrally closed test configuration X for X, and an irreducible component E of X0 such\nthat vE = v. Passing to a higher test configuration, we may assume that X is the integral\nclosure of the blowup of Xtriv along a flag ideal a, and then v ∈ Σa .                    \u0003",
  "e051a9b70c06023f3fdb41255282f838d12d32fb30fcf3ffa22420c769d190ff": "details.\n\n2.5. Fubini–Study functions and PL functions. We now study the relation between\nH(L) and the space PL(X) introduced in §2.1.\nProposition 2.25. For any L ∈ Pic(X)Q and ϕ : X an → R ∪ {−∞}, we have ϕ ∈ H(L)\niff ϕ = m−1 ϕa for a flag ideal a and m ∈ Z>0 such that mL is an honest line bundle and\nmLtriv ⊗ a is globally generated on Xtriv .\n\f28                       SÉBASTIEN BOUCKSOM AND MATTIAS JONSSON\n\n   Here (Xtriv , Ltriv ) is the trivial test configuration for (X , L), see Example 1.6. In terms\nof the weight decomposition (2.2), note that mLtriv ⊗ a is globally generated iff mL ⊗ aλ is\nglobally generated for all λ ∈ Z.\nProof. Assume first ϕ ∈ H(L) and write ϕ = m−1 maxi {log |si | + λi } for a finite set (si ) in\nH0 (X, mL) and λi ∈ Z. The rational sections (si $−λi ) of mLtriv on Xtriv generate a flag\nideal a such that mLtriv ⊗ a is globally generated on Xtriv , and ϕ = m−1 ϕa .\n   Assume, conversely, that ϕ = m      −1         a a flag ideal such that mLtriv ⊗ a is globally\n                                     P a with−λ\ngenerated. As above, write a = λ∈Z aλ $ . For each λ ∈ Z, OX (mL) ⊗ aλ is globally\ngenerated by a finite set (sλ,i )i of sections in H0 (X, mL), and (2.3) shows that\n\n                                 ϕ = m−1 max{log |sλ,i | + λ},\n                                            λ,i\nwhich proves that ϕ ∈ H(L).                                                                    \u0003\nCorollary 2.26. For any L ∈ Pic(X)Q , we have Q+ H(L) ⊂ PL+ (X), and equality holds if\nL is ample. In particular, H(L) spans the Q-vector space PL(X) whenever L is ample.\n  In view of Proposition 2.19 (iii), this implies\nCorollary 2.27. We have PL+ (X) = L H(L), where L ranges over ample classes in\n                                           S\nPic(X).\n   Given a flag ideal a, we get an evaluation map PL(X) → QΣa . We now show that this\nmap is surjective. Using Lemma 2.12, this will imply that the evaluation map PL(X) → QΣ\nis surjective for any finite subset Σ ⊂ X div . For later purposes, we prove a more precise\nresult.\nLemma 2.28. For any flag ideal a, and L ∈ Pic(X)Q ample, the following property holds\nfor m sufficiently divisible. For any c ∈ QΣa , there exists r ≥ 1 and ρ ∈ H(L) such that\nψ := r(ϕa − mρ) ∈ PL(X) satisfies ψ(v) = cv for all v ∈ Σa .\n     Before proving the lemma, we establish the following version of [BHJ17, Theorem 1.10].\nLemma 2.29. Let a be a flag ideal. Denote by µ : X → Xtriv the integral closure of the\nblowup along a, and by E1 , . . . , EN the irreducible components of X0 . Then\n   \\                                            \\\n     {f ∈ OXtriv | ordEi (f ) ≥ ordEi (am )}       {f ∈ OXtriv | ordEi (f ) ≥ ordEi (am )} (2.13)\n     i                                            i>1\nfor all m ∈ N large enough.\nProof. The (antieffective) vertical Cartier divisor D on X such that OX (D) = a · OX is",
  "426b32a79eaabddd722a2f8c7b7d1b6d65311937cd704dae4a1d0a4332e17fec": "dence between:\n    (i) the set of equivalence classes of test configurations for L and PL(X);\n   (ii) the set of equivalence classes of semiample test configurations for L and H(L).\n   Note that the sets in (ii) are nonempty only if L is semiample. Combined with Proposi-\ntion 2.30, we infer:\nCorollary 2.32. If L is an ample Q-line bundle, then L 7→ ϕL defines a 1–1 correspondence\nbetween the set of ample, integrally closed test configurations for L and H(L).\n     The set H(L) thus corresponds to HNA (L) in the notation of [BHJ17, Definition 6.2].\nProof of Theorem 2.31. By construction, the map L 7→ ϕL is the composition of D 7→ ϕD\nwith the canonical bijection between equivalence classes of test configurations for L and\nlimX VCar(X )Q . Thus (i) is a direct consequence of Theorem 2.7.\n−→\n   To prove (ii), let (X , L) be a semiample test configuration for (X, L). After replacing L\nwith a multiple and pulling-back to a higher test configuration, we may assume without loss\nthat L is a globally generated line bundle, and that X dominates the trivial test configuration\nvia µ : X → Xtriv . Set D := L − µ? Ltriv ∈ VCar(X ), so that ϕL = ϕD . Since L is globally\ngenerated, OX (D) is µ-globally generated, and the flag ideal a := µ? OX (D) thus satisfies\na·OX = OX (D), and hence ϕa = ϕD = ϕL . Denote by a0 ⊂ a the flag ideal locally generated\nby\n                                H0 (Xtriv , Ltriv ⊗ a) ≃ H0 (X , L).\nSince L is globally generated, we have a0 · OX = OX (D) = a · OX ; hence ϕa0 = ϕL . By\nconstruction, L ⊗ a0 is globally generated, and Proposition 2.25 thus yields, as desired,\nϕL ∈ H(L).\n   Conversely pick ϕ ∈ H(L). After replacing L with a multiple, Proposition 2.25 yields\nϕ = ϕa for a flag ideal a on Xtriv such that Ltriv ⊗ a is globally generated. Denoting by\nµ : X → Xtriv the blowup along a, we have a · OX = OX (D) for a vertical Cartier divisor D\nsuch that L := µ? Ltriv + D is globally generated, and ϕL = ϕD = ϕa = ϕ.                      \u0003\n     The next result will be needed in §3.1.\nLemma 2.33. If L is an ample Q-line bundle on X and X any test configuration for X\nthat dominates Xtriv , then L admits an ample test configuration L determined on X .\nProof. By Lemma 1.8, we can find D ∈ VCar(X )Q that is relatively ample over Xtriv .\nDenoting by LX the pullback of L to X , it follows that L := LX + εD is ample for ε ∈ Q>0\nsmall enough, and we are done.                                                         \u0003\n2.8. Geometric interpretation of the scaling action. As noted in §2.1, the spaces\nPL(X) and PL+ (X) admit a natural scaling action by Q>0 . We now give a geometric\ninterpretation of the scaling action of Z>0 in terms of base change.",
  "a44581a6ec6d137d3e65e97270e451228d73fb3dda60f5a11ce4b261a22eb9b1": "f ? ϕ = ϕf ? D , and the result thus follows from the fact that θY + f ? D = f ? (θX + D) is nef,\nas the pullback of a nef class. If f : Y → X is surjective, then f : Y → X is surjective as\nwell, and (vi) follows.                                                                        \u0003\n\f36                       SÉBASTIEN BOUCKSOM AND MATTIAS JONSSON\n\n   Given a test configuration π : X → A1 , we denote by Amp(X /A1 ) ⊂ Nef(X /A1 ) the set\nof π-ample classes α ∈ N1 (X /A1 ), that is, classes whose restriction to X0 is ample.\nDefinition 3.8. For any ω ∈ Amp(X), we denote by Hdom (ω) ⊂ PL ∩ PSH(ω) the set of ω-\npsh PL functions of the form ϕD with D ∈ VCar(X )Q for a test configuration X dominating\nXtriv and ωX + D ∈ Amp(X /A1 ).\n   After pulling back by the (finite) integral closure morphism Xe → X , one may always\narrange that X is integrally closed in this definition.\nExample 3.9. If ω = c1 (L) for an ample Q-line bundle, then H(L) is in 1–1 correspon-\ndence with the set of ample, integrally closed test configurations (X , L) for (X, L) (see Corol-\nlary 2.32), and\n                              Hdom (L) := Hdom (c1 (L)) ⊂ H(L)\ncorresponds to the subset such that X dominates Xtriv .\n     As in Corollary 2.26, we have\n                                     Q+ Hdom (ω) = PL+ (X)                                 (3.2)\nfor any ω ∈ Amp(X), so that Hdom (ω) spans the Q-vector space PL(X).\nProposition 3.10. If ω ∈ Amp(X), then every ϕ ∈ PLR ∩ PSH(ω) is a uniform limit of\nfunctions in Hdom (ω).\nLemma 3.11. For any ω ∈ Amp(X), the set of test configurations X dominating Xtriv such\nthat there exists H ∈ VCar(X )Q with ωX + H ∈ Amp(X /A1 ) is cofinal in the set of all test\nconfigurations.\nProof. By Lemma 1.8, any test configuration for X is dominated by a test configuration X\nwith a morphism µ : X → Xtriv such that VCar(X )Q contains a µ-ample divisor A. Since\nωXtriv ∈ N1 (Xtriv /A1 ) is ample, ωX + εA = µ? ωXtriv + εA ∈ N1 (X /A1 ) is ample for ε ∈ Q>0\nsmall enough, and setting H := εA yields the result.                                        \u0003\nProof of Proposition 3.10. Pick any ϕ ∈ PLR ∩ PSH(ω), and write ϕ = ϕD for some D ∈\nVCar(X )R , where X is an integrally closed test configuration. Thus ωX + D ∈ N1 (X /A1 ) is\nnef. By Lemma 3.11 we may assume that there exists P    H ∈ VCar(X )PR such that ωX + H is\nample. Pick a basis (Ci ) for VCar(X )Q and write D = i ci Ci , H = i c0i Ci with ci , c0i ∈ R.\n                                  1                                                          1\nFor m \u001d 1, the class ωX + D + m     H ∈ N1 (X /A1 ) is ample, and we can pick εm,i ∈ (0, m     )\n                    P          0\n                              ci\nsuch that if Dm := i (ci + m + εm,i )Ci , then Dm ∈ VCar(X )Q and ωX + Dm is ample. It\n                                                     1\nfollows that ϕDm ∈ Hdom (ω), and that ϕDm − ϕ = m\n                                                             P\n                                                       ϕH + i εm,i ϕCi tends to 0 uniformly\non X an .                                                                                     \u0003\n3.2. The energy pairing. Recall that every test configuration π : X → A1 admits a canon-\nical compactification π : X̄ → P1 . If X dominates Xtriv , then any θ ∈ N1 (X) pulls back to a\nclass θX̄ ∈ N1 (X̄ ), whose image in N1 (X /A1 ) coincides with θX considered above.\n   Pick an (n + 1)-tuple of pairs (θi , ϕi ) ∈ N1 (X) × PLR , i = 0, . . . , n, and choose a test\nconfiguration X dominating Xtriv and divisors Di ∈ VCar(X )R that determined the ϕi .\nFollowing [BHJ17, Definition 6.11], we introduce:\nDefinition 3.12. The energy pairing takes an (n+1)-tuple of pairs (θi , ϕi ) ∈ N1 (X)×PLR ,\ni = 0, . . . , n to\n                                                                 \u0001                    \u0001",
  "672069804343eb355735bee9c0c0d857d31e20a1fc18847f2464885e22022048": "     For psh pairs, (3.5) implies the following crucial monotonicity property:\nLemma 3.15. Consider psh pairs (θi , ϕi ) ∈ Nef(X) × PLR , i = 1, . . . , n, and pick also\nθ0 ∈ N1 (X) and ϕ0 , ϕ00 ∈ PLR . Then\n         ϕ0 ≤ ϕ00 =⇒ (θ0 , ϕ0 ) · (θ1 , ϕ1 ) · . . . · (θn , ϕn ) ≤ (θ0 , ϕ00 ) · (θ1 , ϕ1 ) · . . . · (θn , ϕn ).\n     Combined with Proposition 3.14 (iii), this yields:\nCorollary 3.16. For all psh pairs (θi , ϕi ) ∈ Nef(X) × PLR , i = 0, . . . , n, we have\n                                  ∀i ϕi ≤ 0 =⇒ (θ0 , ϕ0 ) · . . . · (θn , ϕn ) ≤ 0;\n                                  ∀i ϕi ≥ 0 =⇒ (θ0 , ϕ0 ) · . . . · (θn , ϕn ) ≥ 0.\n  Anticipating on the more general construction of §7.3, it is convenient to interpret (3.5)\nby attaching to any tuple (θi , ϕi ) ∈ N1 (X) × PLR , i = 1, . . . , n its mixed Monge–Ampère\nmeasure\n                                 n\n                                 ^                     X\n                                     (θi + ddc ϕi ) :=   cE δvE                          (3.6)\n                                          i=1                        E\nwith cE := bE (θ1,X + D1 )|E · . . . · (θn,X + Dn )|E . It is thus a signed Radon measure on X an ,\nwith support a finite subset of X div , and characterized by\n                    ˆ      ^n\n                        ϕ      (θi + ddc ϕi ) = (0, ϕ) · (θ1 , ϕ1 ) · . . . · (θn , ϕn )     (3.7)\n                          X an     i=1\n\nfor all ϕ ∈ PL (recall that PL is dense in C0 (X), see Theorem 2.2). By Proposition 3.14 (i),\n                            ˆ     n\n                                  ^\n                                    (θi + ddc ϕi ) = (θ1 · . . . · θn )X .             (3.8)\n                                     X an i=1\n\nThe symmetry of the intersection pairing yields the ‘integration by parts’ formula\n         ˆ                  n\n                            ^                  ˆ                 ^n\n                     c                 c\n              ϕ0 dd ϕ1 ∧ (θi + dd ϕi ) =            ϕ1 ddc ϕ0 ∧ (θi + ddc ϕi )                                       (3.9)\n                 X an                 i=2                        X an                  i=2\n\f             GLOBAL PLURIPOTENTIAL THEORY OVER A TRIVIALLY VALUED FIELD                          39\n\nfor all ϕi ∈ PLR , while Proposition 3.14 (iv) yields\n                           ^                          ^\n                             (θi + ddc (t · ϕi )) = t? (θi + ddc ϕi )                       (3.10)\n                             i                                i\nfor all t ∈ Q>0 . When ϕi = 0 for some i, we drop the term ddc ϕi from the notation.\nExample 3.17. We have\n                                              X\n                        θ1 ∧ · · · ∧ θn =               (θ1 · . . . · θn )Xα δvtriv,α .     (3.11)\n                                            dim Xα =n\n\nExample 3.18. Assume Z ⊂ X are both smooth and irreducible, with associated valuation\nordZ ∈ X div . Set d := dim Z, and consider the function ϕZ of Example 2.5. Denoting by\nµ : X → Xtriv the blowup of Z × {0} and P its exceptional divisor, we have X0 = X    e +P\n(see Example 1.7), ϕZ = −ϕP , vXe = vtriv and vP = ordZ (see Example 1.21). For any",
  "1366ec7573822a5524928b2a060d4a297a7c2bb3e4e048b9783589094edda81d": " (PSH1) for any L ∈ Pic(X)Q , we have HR           (L) ⊂ PSH(L) := PSH(c1 (L));\n (PSH2) if a generically finite function ϕ : X an → R ∪ {−∞} arises as the pointwise limit of\n           a decreasing net (ϕi ) with ϕi ∈ PSH(θi ) and limi θi = θ, then ϕ ∈ PSH(θ).\n  Note that (PSH2) implies the following two properties:\n(PSH2a) for any function ϕ : X an → R ∪ {−∞}, the set of θ ∈ N1 (X) such that ϕ ∈ PSH(θ)\n           is closed (possibly empty);\n(PSH2b) for any θ ∈ N1 (X), the set PSH(θ) is closed under decreasing limits (provided the\n           limit function is generically finite).\n  Taking (PSH1) and (PSH2) as minimal requirements directly leads to the following defini-\n  tion:\n  Definition 4.1. For any θ ∈ N1 (X), we define a θ-psh function ϕ : X an → R ∪ {−∞} as a\n  generically finite, usc function that can be written as the pointwise limit of a decreasing net\n         gf\n  ϕi ∈ HR   (Li ) with Li ∈ Pic(X)Q such that limi c1 (Li ) = θ in N1 (X).\n    We denote by PSH(θ) the set of θ-psh functions, and by\n                        CPSH(θ) := C0 (X) ∩ PSH(θ) ⊂ E ∞ (θ) ⊂ PSH(θ)\n  the subsets of continuous and bounded θ-psh functions, respectively. When needed, we also\n  write PSH(X, θ) = PSH(θ) etc. Using the notation in the definition, we have:\n                 gf\n        • since HR  (Li ) is non-empty, Li is necessarily effective, by (2.11), and hence\n                                   PSH(θ) 6= ∅ =⇒ θ ∈ Psef(X);                                (4.1)\n        • if ϕ is bounded, then ϕi is finite valued, i.e. ϕi ∈ H(Li ); this implies that Li is\n          semiample, by (2.12), and hence\n                                    E ∞ (θ) 6= ∅ =⇒ θ ∈ Nef(X);                               (4.2)\n        • if ϕ ∈ CPSH(θ) is further continuous, then ϕi → ϕ uniformly on X an , by Dini’s\n          lemma.\n  Remark 4.2. In the complex analytic case, psh functions and metrics are defined in a\n  different way, which is local in nature. However, when X is smooth, well-known arguments\n  due to Demailly [Dem92] and relying on the Ohsawa–Takegoshi extension theorem show that\n  any psh metric on a (necessarily pseudoeffective) line bundle L can be approximated from\n  above by metrics attached to sections of mL + A, where A is a fixed ample line bundle and\n\f46                        SÉBASTIEN BOUCKSOM AND MATTIAS JONSSON\n\nm is large (compare for instance [Bou04, Theorem 5.4] or [GZ05, Appendix]). As a result,\nany such metric satisfies the analogue of Definition 4.1.\nLemma 4.3. For functions in PL(X)R , Definition 4.1 is consistent with Definition 3.2.\nIn other words, given θ ∈ N1 (X), a test configuration X that dominates Xtriv and D ∈\nVCar(X )R , we have\n                        ϕD ∈ PSH(θ) ⇐⇒ θX + D ∈ Nef(X /A1 ).\n  Indeed, this follows from Lemma 3.5, Lemma 3.7 and Corollary 3.22. For any θ ∈ N1 (X),\nwe get, in particular,\n                   PSH(θ) contains all constant functions ⇐⇒ θ ∈ Nef(X),                       (4.3)\nwhich provides a converse to (4.2).\nRemark 4.4. If L is a Q-line bundle, then functions in PSH(L) = PSH(c1 (L)) can be\ninterpreted as psh metrics on L, using the trivial metric. By (4.3), any nef line bundle L\nadmits a bounded (continuous) psh metric, to wit the trivial metric. This is in stark contrast\nwith the complex analytic case, where a nef and big line bundle may not admit any bounded\npsh metric (see [BEGZ10, Example 5.4], based on [DPS94, Example 1.7]).\nTheorem 4.5. Properties (PSH1) and (PSH2) above are satisfied.\n  As a consequence, Definition 4.1 is indeed the minimal one for which (PSH1) and (PSH2)\nare satisfied.\nLemma 4.6. Let K be a compact topological space, and assume we are given:\n      • a set S and, for each s ∈ S, a family Fs of continuous functions f : K → R ∪ {−∞},\n         stable under addition of a constant;\n      • a map ρ : S → T to a metrizable topological space T .\nFor each t ∈ T , denote by Fet the set of all (usc) functions g : K → R ∪ {−∞} that can\nbe written as the pointwise limit of a decreasing net (fi ) with fi ∈ Fsi for a net (si ) of S\n                                          ≈\nsuch that limi ρ(si ) = t in T . Then Ft = Fet for any t ∈ T . In other words, if a function\ng : K → R ∪ {−∞} can be written as the pointwise limit of a decreasing net (gi )i∈I with\ngi ∈ Feti for a net (ti ) of T such that limi ti = t, then g ∈ Fet .\nProof. Pick a metric d on T inducing the given topology. For each i ∈ I, gi is the pointwise\nlimit of a decreasing net (fi,j )j∈Ji with fi,j ∈ Fsi,j for a net (si,j )j∈Ji in S such that ti,j :=\nρ(si,j ) satisfies limj ti,j = ti . Denote by A the set of triples α = (i, j, ε) with i ∈ I, j ∈ Ji\nand ε ∈ R>0 , and define a partial preorder on A by setting\n                                                 i ≥ i0\n                                                \n                                  0 0 0\n                    (i, j, ε) ≥ (i , j , ε ) ⇐⇒   fi,j + ε ≤ fi0 ,j 0 + ε0 on K                 (4.4)\n                                                  d(ti,j , ti ) + ε ≤ d(ti0 ,j 0 , ti0 ) + ε0 ,\n                                                \n\nWe claim that A is directed. To see this, pick α1 = (i1 , j1 , ε1 ), α2 = (i2 , j2 , ε2 ) in A. Since\nI is directed, we can choose i3 ∈ I with i3 ≥ i1 , i2 . Pick also ε3 > 0 with ε3 < min{ε1 , ε2 }.\nSince (gi )i is decreasing, we have gi3 ≤ min{gi1 , gi2 } ≤ min{fi1 ,j1 , fi2 ,j2 }, and hence\n                              gi3 + ε3 < min{fi1 ,j1 + ε1 , fi2 ,j2 + ε2 }                     (4.5)\npointwise on K. For each j ∈ Ji3 , define hj : K → R by\n                   hj := exp (fi3 ,j + ε3 ) − exp (min{fi1 ,j1 + ε1 , fi2 ,j2 + ε2 }) .\n\f              GLOBAL PLURIPOTENTIAL THEORY OVER A TRIVIALLY VALUED FIELD                                      47\n\nThen (hj ) is a decreasing net of continuous functions such that limj hj < 0 pointwise on K,\nby (4.5). The compact space K can thus be written as the increasing union of the open sets\n{hj < 0}, and hence K = {hj3 < 0} for some j3 ∈ Ji3 , i.e.\n                            fi3 ,j3 + ε3 < min{fi1 ,j1 + ε1 , fi2 ,j2 + ε2 } on K.\nSince limj ti3 ,j = ti3 and ε3 < min{ε1 , ε2 }, we can further arrange, after increasing j3 if\nneeded, that\n          d(ti3 ,j3 , ti3 ) + ε3 < min{ε1 , ε2 } ≤ min {d(ti1 ,j1 , ti1 ) + ε1 , d(ti2 ,j2 , ti2 ) + ε2 } .\nThus α3 := (i3 , j3 , ε3 ) ∈ A satisfies α3 ≥ α1 , α2 , which proves, as desired, that A is directed.\n  Now, for each α = (i, j, ε) ∈ A, set\n                  sα := si,j ∈ S,       tα = ρ(sα ) ∈ T,        and gα := fi,j + ε ∈ Fsα ,\nwhere the last containment holds because Fsα is assumed to be stable under addition of a\nconstant. By construction, (gα )α∈A is a decreasing net, and it will suffice to show limα gα = g\npointwise on K and limα tα = t. Pick δ > 0 and x ∈ K. Since limi gi (x) = g(x) and\nlimi ti = t, we can find i0 ∈ I such that gi0 (x) < g(x) + δ and d(ti , t) < δ for all i ≥ i0 .\nUsing limj fi0 ,j (x) = gi0 (x) and limj ti0 ,j = ti0 , we next pick j0 ∈ Ji0 and 0 < ε0 \u001c 1 such\nthat fi0 ,j0 (x) + ε0 < g(x) + δ and d(ti0 ,j0 , ti0 ) + ε0 < δ. Set α0 := (i0 , j0 , ε0 ) ∈ A. For each\nα = (i, j, ε) ∈ A such that α ≥ α0 , we then have, by (4.4),\n                           gα (x) = fi,j (x) + ε ≤ fi0 ,j0 (x) + ε0 < g(x) + δ,\n\n                    d(tα , ti ) = d(ti,j , ti ) ≤ d(ti,j , ti ) + ε ≤ d(ti0 ,j0 , ti0 ) + ε0 < δ,",
  "2452bb775162149812ac4f238f20d3a7360c89cddda7c7918f3e48188b0fcf83": "4.3. The regularization theorem. Many properties of θ-psh functions are obtained by\nregularization, that is, approximation by nicer θ-psh functions. In our present approach,\nregularization of θ-psh functions is built into their definition. One can, however, improve\nthe properties of the approximants as follows:\nTheorem 4.15. Pick θ ∈ N1 (X) and ϕ ∈ PSH(θ). Then:\n                                                                   gf\n     (i) ϕ can be written as the limit of a decreasing net ϕi ∈ HQ    (Li ) with Li ∈ Pic(X)Q\n         such that c1 (Li ) − θ is ample and limi c1 (Li ) = θ;\n    (ii) if θ ∈ Nef(X) then (i) holds with ϕi ∈ H(Li ) = HQ (Li ) and Li ample;\n   (iii) if ω := θ ∈ Amp(X), then ϕ can be written as the limit of a decreasing net in\n         Hdom (ω) (see Definition 3.8).\n\f50                       SÉBASTIEN BOUCKSOM AND MATTIAS JONSSON\n\n   We shall later prove that these results actually hold with (countable) sequences instead\nof nets, see Corollary 12.18.\n   As already indicated by (iii), the class of θ-psh functions has particularly good properties\nwhen θ ∈ Amp(X) is ample. In this case, we typically write ω instead of θ.\nCorollary 4.16. For any ω ∈ Amp(X), the space CPSH(ω) = C0 (X) ∩ PSH(ω) is the\nclosure of Hdom (ω) ⊂ C0 (X) in the topology of uniform convergence.\nProof. By Theorem 4.7, CPSH(ω) is closed in the topology of uniform convergence. By\nTheorem 4.15 and Dini’s lemma, any ϕ ∈ CPSH(ω) is the uniform limit of a net in Hdom (ω),\nand the result follows.                                                                \u0003\nCorollary 4.17. For any θ ∈ N1 (X) and any ϕ ∈ PSH(θ) we have ϕ > −∞ on X lin .\nProof. Pick an ample line ` bundle L such that c1 (L) − θ is nef. Then ϕ ∈ PSH(L). Using\nTheorem 4.7 and X lin = α Xαlin , we may assume X is irreducible. Now pick v ∈ X lin . Then\nTL (v) < ∞, and we claim that ϕ(v) ≥ ϕ(vtriv ) − TL (v). Indeed, TL (v) is the supremum of\nm−1 v(s) over m ∈ Z>0 and s ∈ H0 (X, mL) \\ {0}. Equivalently, ψ := m−1 log |s| satisfies\nψ(v) ≥ ψ(vtriv ) − TL (v). Adding constants and taking finite maxima shows that this also\nholds for all ψ ∈ H(L), and then for all ϕ ∈ PSH(L), by Theorem 4.15.                     \u0003\n     As another consequence, we get:\nCorollary 4.18. Assume that X is irreducible, and let L be an ample Q-line bundle. Then\nPSH(L) is the smallest class of functions ϕ : X an → R ∪ {−∞}, not identically −∞, that\ncontains all functions of the form m−1 log |s| with m ∈ Z>0 and s ∈ H0 (X, mL) \\ {0}, and\nis stable under addition of a real constant, finite maxima, and decreasing limits.\n                                                                                gf\nProof of Theorem 4.15. By definition, ϕ is the limit of a decreasing net ϕi ∈ HR   (Li ) with\nc1 (Li ) → θ. Using (2.8) it is straightforward to see that each ϕi can further be written\n                                         gf\nas a decreasing limit of functions in HQ    (Li ). By Lemma 4.6, we may thus assume that\n        gf\nϕi ∈ HQ    (Li ). We can also arrange that c1 (Li ) − θ ∈ Amp(X). Indeed, given any ample\nline bundle A, we can find εi ∈ Q>0 such that limi εi = 0 and Li − θ + εi A is ample. By\n                                    gf          gf\nProposition 2.19, we have ϕi ∈ HQ      (Li ) ⊂ HQ  (Li + εi A), and replacing Li with Li + εi A\nyields the claim. This proves (i).\n   Assume next that θ is nef. In the notation of (i), it follows that each Li is ample. Further,\neach ϕi is the decreasing limit of max{ϕi , −m} ∈ H(Li ), and Lemma 4.6 yields (ii).\n   Finally assume that ω := θ is ample. Replacing ϕ with ϕ − sup ϕ, we may assume\nϕ ≤ 0. By Proposition 3.10, any function in PL ∩ PSH(ω) is a decreasing limit of functions",
  "3709e976c34a7aa779a92d36986fe5aaa83efc65384af64c8df047cbbdee3c47": "Definition 4.20. We endow PSH(θ) with the topology of pointwise convergence on X div .\n  As we shall later see in Theorem   11.4, this topology coincides with the topology of point-\n                       lin        lin\n                            `\nwise convergence on X = α Xα . In view of (4.6), we have:\nExample 4.21. The map ϕ 7→ sup ϕ = maxα ϕ(vtriv,α ) is continuous on PSH(θ).\nTheorem 4.22. For any ϕ ∈ PSH(θ) and any usc function ψ : X an → R ∪ {−∞}, we have\n                             ϕ ≤ ψ on X div ⇐⇒ ϕ ≤ ψ on X an .\nIn particular, ϕ is the smallest usc extension of ϕ|X div to X an .\nCorollary 4.23. Every θ-psh function is uniquely determined by its restriction to X div , and\nthe topology of PSH(θ) is Hausdorff.\n   Because of this, we will occasionally say that a function ϕ : X div → R is θ-psh if it admits\na (necessarily unique) extension to a θ-psh function on X an .\nCorollary 4.24. If X is connected, then any 0-psh function is constant, i.e. PSH(0) = R.\nProof. By GAGA, X an is connected, and after replacing X with an irreducible component,\nwe may assume that X is irreducible. By Corollary 4.23, it is then enough to show that any\nϕ ∈ PSH(0) with sup ϕ = ϕ(vtriv ) = 0 satisfies ϕ(v) = 0 for any v ∈ X div . Consider the\ndecreasing sequence (mϕ)m∈N and its pointwise limit ψ := limm (mϕ). Since ψ(vtriv ) = 0,\nwe have ψ ∈ PSH(0) (see Theorem 4.5). By Corollary 4.17, we thus have ψ(v) > −∞, i.e.\nϕ(v) = 0.                                                                                \u0003\nCorollary 4.25. Pick a decreasing net (ϕi ) in PSH(θ), and assume that it converges to\nϕ ∈ PSH(θ). Then ϕ = limi ϕi pointwise on X an .\nProof. The pointwise limit ψ of (ϕi ) on X an coincides with ϕ on X div . In particular,\nψ(vtriv,α ) is finite for any α, and hence ψ ∈ PSH(θ), by Theorem 4.5. By Corollary 4.23, we\ninfer ϕ = ψ, which means that ϕi converges to ϕ pointwise on X an                          \u0003\nLemma 4.26. For each ψ ∈ PL(X), there exists a finite set Σ ⊂ X div such that\n                                  sup(ϕ − ψ) = max(ϕ − ψ)                                  (4.7)\n                                   X an            Σ\n\nfor all ϕ ∈ PL+ (X), and the same result then holds for all ϕ ∈ PSH(θ), θ ∈ N1 (X).\nMoreover, if ψ = r(ϕa − ρ), where r ∈ Q>0 , a is a flag ideal, and ρ ∈ PL+ (X), then we can\npick Σ = Σa , the set of Rees valuations of a.\nProof. We can always write ψ = r(ϕa − ρ) as above, and by homogeneity we may assume\nr = 1. The case ϕ ∈ PL+ (X) now follows from Lemma 2.13, since ϕ + ρ ∈ PL+ (X).\n  Now assume ϕ ∈ PSH(θ) for some θ ∈ N1 (X). After replacing θ with ω ∈ Amp(X)\nsuch that ω − θ is nef, we may assume θ = ω is ample. By Theorem 4.15, we can find a\ndecreasing net (ϕi ) in Hdom (ω) ⊂ PL+ (X) such that ϕi & ϕ. For each v ∈ X an , we then\nhave ϕi (v) − ψ(v) ≤ maxΣa (ϕi − ψ) for all i, and hence ϕ(v) − ψ(v) ≤ maxΣa (ϕ − ψ). \u0003\n\f52                      SÉBASTIEN BOUCKSOM AND MATTIAS JONSSON\n\nProof of Theorem 4.22. If ψ ∈ PL(X), the result follows from Lemma 4.26. Assume next\nψ ∈ C0 (X). By Theorem 2.2, ψ is a uniform limit of functions in PL(X), and the result\nthus holds for ψ as well. In the general case, we can find a decreasing net (ψi ) in C0 (X)\nwith ψi → ψ. Then ϕ ≤ ψ ≤ ψi on X div implies ϕ ≤ ψi on X an , and hence ϕ ≤ ψ on X an\nas well.                                                                                  \u0003\nRemark 4.27. Assume char k = 0. By Corollary A.3, any v ∈ X an is the limit of a net\n(vi ) in X div such that vi ≤ v for all i. As any ϕ ∈ PSH(θ) is decreasing and usc, it follows\nthat ϕ(vi ) → ϕ(v), which provides a slightly more precise version of Corollary 4.23 in that\ncase.\n     We record another useful consequence of Lemma 4.26.\nProposition 4.28. For any ψ ∈ C0 (X), ϕ 7→ supX an (ϕ − ψ) is continuous on PSH(θ).\nProof. When ψ is PL, this is a direct consequence of Lemma 4.26. As above, the general\ncase follows by density of PL(X) in C0 (X) with respect to uniform convergence.     \u0003\nCorollary 4.29. For any v ∈ X an , the evaluation map ϕ 7→ ϕ(v) is usc on PSH(θ).",
  "dd64c9e9fcffab905d7ca45c52532d5ce99bbf2b31ebd1a6ce5c62689b2714ca": "Lemma 5.13. Let π : Y → X be a birational morphism. Pick θ ∈ N1 (X), and assume that\nθ can be written as the limit of a sequence of classes θm > θ with the envelope property.\n                  ∼\nThen π ? : PSH(θ) → PSH(π ? θ) is a homeomorphism.\n  Recall that θm > θ means that θm − θ is ample.\n\nProof. After passing to a subsequence, we may assume that θm > θm+1 for all m, and hence\n                                                           ∼\nPSH(θm+1 ) ⊂ PSH(θm ). Since π induces a bijection Y div → X div , π ? : PSH(θ) → PSH(π ? θ)\nis a topological embedding, and it suffices to show that it is onto. Pick ψ ∈ PSH(π ? θ), and\nwrite π as the blowup of an ideal b ⊂ OX . By Theorem 4.32, there exists a sequence εm & 0\nsuch that ψ + εm π ? log |b| = π ? ϕm with ϕm ∈ PSH(θm ). By Theorem 4.22, ϕm is uniquely\ndetermined, and (ϕm )m≥m0 is an increasing sequence in PSH(θm0 ) for any given m0 . By\nTheorem 5.11, ϕm converges pointwise on X div to ϕ ∈ PSH(θ), which satisfies ψ = π ? ϕ on\nY div . The result follows.                                                                 \u0003\n\nProof of Theorem 5.12. Since the normalization morphism ν : X ν → X is finite, ν ? ω is\nample, and hence Hdom (ν ? ω) spans PL(X ν ), see (3.2). By Lemma 2.3, PL(X ν ) separates",
  "4b40a2545a02632b81053a4aa795fcd6319fdccd24465040441826dbc1685a3d": "smooth, and char k = 0 (see Theorem 5.20).\nRemark 5.15. The envelope property makes sense also when X is reducible. It is easy to\nsee that θ ∈ N1 (X) has the envelope property iff θ|Y ∈ N1 (Y ) has the envelope property\nfor every connected component Y of X. Moreover, if X is connected, then the proof of\nTheorem 5.12 shows that if the envelope property holds for some ample class in N1 (X), then\nthe normalization morphism ν : X ν → X is a homeomorphism, which implies that X is\nirreducible (and unibranch).\n5.3. Envelopes. For ample classes, the envelope property admits a useful reformulation.\nWe continue to assume that X is irreducible unless stated otherwise. Fix a class ω ∈\nAmp(X).\nDefinition 5.16. The ω-psh envelope of a function ϕ : X an → R ∪ {±∞} is the function\nPω (ϕ) : X an → R ∪ {±∞} defined as the pointwise supremum\n                           Pω (ϕ) := sup {ψ ∈ PSH(ω) | ψ ≤ ϕ} .\n  Thus Pω (ϕ) ≡ −∞ iff there is no ψ ∈ PSH(ω) with ψ ≤ ϕ. Despite the name, Pω (ϕ) is\nnot always ω-psh (and indeed not even usc in general). However, it is clear that\n     • ϕ 7→ Pω (ϕ) is increasing;\n     • Pω (ϕ + c) = Pω (ϕ) + c for all c ∈ R.\n\f60                        SÉBASTIEN BOUCKSOM AND MATTIAS JONSSON\n\nThese properties formally imply the Lipschitz estimate\n                               sup Pω (ϕ) − Pω (ϕ0 ) ≤ sup |ϕ − ϕ0 |.                     (5.1)\nwhen ϕ, ϕ0 are bounded.\nLemma 5.17. For any ω ∈ Amp(X), the following statements are equivalent:\n   (i) ω has the envelope property;\n  (ii) for any function ϕ : X an → R ∪ {±∞}, we have\n                      Pω (ϕ) ≡ −∞, Pω (ϕ)? ≡ +∞, or Pω (ϕ)? ∈ PSH(ω).\n     (iii) for any ϕ ∈ C0 (X), Pω (ϕ) is continuous.\n     We refer to the property in (iii) as continuity of envelopes.\nProof. First assume (i). Pick any ϕ : X an → R ∪ {±∞}, and suppose that the set F :=\n{ψ ∈ PSH(θ) | ψ ≤ ϕ} is nonempty, so that Pω (ϕ) 6≡ −∞. If the functions in F are uniformly\nbounded above, then Pω (ϕ)? ∈ PSH(ω), by (i). If not, then, by the definition of the\nAlexander–Taylor capacity we have\n             Pω (ϕ)(v) = sup {ψ(v) | ψ ∈ F} ≥ sup {sup ψ | ψ ∈ F} − Tω (v) = +∞\nfor all v ∈ X div , and hence Pω (ϕ)? ≡ +∞, by density of X div . This proves (i)⇒(ii).\n   Next we prove (ii)⇒(iii), so pick ϕ ∈ C0 (X). Then Pω (ϕ)? ∈ PSH(ω) is a competitor in\nthe definition of Pω (ϕ), and hence Pω (ϕ)? ≤ Pω (ϕ). We conclude that Pω (ϕ)? = Pω (ϕ) is\nusc. We claim that Pω (ϕ) is also lsc, and hence continuous. To prove the claim, it suffices to\nshow that Pω (ϕ) is a supremum of continuous functions, and for this it suffices to prove that\nfor any ψ ∈ PSH(ω) with ψ ≤ ϕ and any ε > 0, there exists ψ 0 ∈ C0 (X) with ψ ≤ ψ 0 ≤ ϕ+ε.\nPick a decreasing net ψi ∈ Hdom (ω) converging pointwise to ψ. For each v ∈ X an , the set\n{ψi < ϕ + ε} is an open neighborhood of v for i large enough, by lower semicontinuity of\nϕ − ψi . By compactness of X an , it follows that ψi < ϕ + ε for all i large enough, so we can\ntake ψ 0 = ψi .\n   Finally, we prove (iii)⇒(i), following [BE20, Lemma 7.30]. Let (ϕi ) be a bounded-above\nfamily in PSH(ω), and set ϕ := sup?i ϕi . Since ϕ is usc and X an is compact, we can find\na decreasing net of continuous functions (ψj ) such that ψj → ϕ. For each i, j, we have\nϕi ≤ ψj , and hence ϕi ≤ Pω (ψj ), which in turn yields ϕ ≤ Pω (ψj ) ≤ ψj . We have thus\nwritten ϕ as the limit of the decreasing net of ω-psh functions Pω (ψj ), which shows that ϕ\nis ω-psh.                                                                                    \u0003\nCorollary 5.18. Assume that ω ∈ Amp(X) has the envelope property, and consider a usc\nfunction ϕ : X an → R ∪ {−∞}. Then:\n    (i) Pω (ϕ) is ω-psh, or Pω (ϕ) ≡ −∞;\n   (ii) if ϕ is the limit of a decreasing net (ϕj ) of bounded-above, usc functions, then\n        Pω (ϕj ) & Pω (ϕ).\nProof. By Lemma 5.17, either ψ := Pω (ϕ)? is ω-psh, or Pω (ϕ) ≡ −∞. Since Pω (ϕ) ≤ ϕ and\nϕ is usc, we also have ψ ≤ ϕ. If ψ is ω-psh, then ψ ≤ Pω (ϕ), which proves (i).\n  To see (ii), note that ρ := limj Pω (ϕj ) satisfies either ρ ∈ PSH(ω) or ρ ≡ −∞, by\nTheorem 4.7. Furthermore, Pω (ϕj ) ≤ ϕj yields in the limit ρ ≤ ϕ, and hence ρ ≤ Pω (ϕ) (by\ndefinition of Pω (ϕ) if ρ ∈ PSH(ω), and trivially if ρ ≡ −∞). Thus limj Pω (ϕj ) = ρ = Pω (ϕ).\nOn the other hand, Pω (ϕj ) ≥ Pω (ϕ) implies ρ ≥ Pω (ϕ), which completes the proof of (ii). \u0003\n\f              GLOBAL PLURIPOTENTIAL THEORY OVER A TRIVIALLY VALUED FIELD                      61\n\n  For any function ϕ : X an → R ∪ {±∞}, we also introduce the pointwise envelope\n                           Qω (ϕ) := sup {ψ ∈ CPSH(ω) | ψ ≤ ϕ} ;\nthis is lsc and bounded below if ϕ is bounded below, and ≡ −∞ otherwise. Since each\nψ ∈ CPSH(ω) is the uniform limit of functions in Hdom (ω) (see Theorem 4.7), one easily\nchecks that\n                            Qω (ϕ) = sup{ψ ∈ Hdom (ω) | ψ ≤ ϕ}.\nLemma 5.19. Suppose ϕ : X an → R ∪ {+∞} is bounded below, with lsc regularization\nϕ? : X an → R ∪ {+∞}. Then:\n     (i) Qω (ϕ) = Pω (ϕ? );",
  "4ae7a90b4df57248c04456a5d20f552c569d9753cc7b332ab43d75446aca1613": "Theorem 5.20. Assume that X is smooth and connected, and that either char k = 0 or\ndim X ≤ 2. Then any θ ∈ Nef(X) has the envelope property.\n  We do not know whether a class θ ∈ N1 (X) that is not nef has the envelope property.\nCorollary 5.21. Under the assumptions of Theorem 5.20, the set\n                           PSHsup (θ) = {ϕ ∈ PSH(θ) | sup ϕ = 0}\nis compact.\n  In [BFJ16], the above compactness property was established in the discretely valued\ncase, by relying on much more involved arguments based on dual complexes and toroidal\nmodifications.\n\f62                      SÉBASTIEN BOUCKSOM AND MATTIAS JONSSON\n\nLemma 5.22. Let L be an ample line bundle on X, and (X , L) a test configuration for\n(X, L), with L an honest line bundle. Denote by am ⊂ OX the base ideal of mL, which is a\nvertical ideal of X for all m \u001d 1. Then\n                       PL (ϕL ) − ϕL = sup m−1 ϕam = lim m−1 ϕam\n                                       m≥1             m→∞\n\npointwise on X an . Furthermore, PL (ϕL ) is continuous iff m−1 ϕam converges uniformly on\nX an .\n  As with flag ideals, see §2.1, the function ϕam ∈ PL(X) is defined by ϕam (v) = −σ(v)(am ),\nwhere σ = σX denotes Gauss extension (see Remark 1.9).\nProof. Set ϕm := ϕL + m−1 ϕam . Note first that (am )m is a graded sequence of ideals, i.e.\nam · am0 ⊂ am+m0 for all m, m0 ∈ N. The sequence m 7→ ϕam is thus superadditive, and\nFekete’s lemma yields supm≥1 m−1 ϕam = limm→∞ m−1 ϕam .\n  Next write L = LX + D with a vertical Cartier divisor D on X , so that ϕL = ϕD . For\neach m, denote by µm : Xm → X the integral closure of the blowup along am , and by Dm the\n(antieffective) divisor on Xm such that OXm · am = OXm (Dm ); thus ϕm = ϕD + m−1 ϕDm .\nBy construction, OX (mL) ⊗ am is globally generated. This implies that\n                         µ? (mL) + Dm = mLXm + µ? (mD) + Dm\nis nef, and hence ϕm ∈ PL ∩ PSH(L). Furthermore, ϕDm ≤ 0, so ϕm ≤ ϕL , and hence\nϕm ≤ PL (ϕL ), which proves\n                               sup ϕm = lim ϕm ≤ PL (ϕL ).\n                               m≥1       m→∞\n\nConversely, Lemma 5.19 implies\n                      PL (ϕL ) = QL (ϕL ) = sup {ψ ∈ H(L) | ψ ≤ ϕL } .\nPick ψ ∈ H(L) with ψ ≤ ϕL . After replacing X with a higher test configuration, we may\nand do assume, for the sake of notational simplicity, that ψ is determined by a vertical\nQ-Cartier divisor E on X . For m large and divisible enough, Theorem 2.31 shows that\nmLX + mE = mL + m(E − D) is globally generated, and hence OX (m(E − D)) ⊂ am . This\nyields\n                             m(ψ − ϕL ) = ϕm(E−D) ≤ ϕam ,\nand hence ψ ≤ ϕm , which yields, as desired, the converse inequality\n                      PL (ϕL ) = sup {ψ ∈ H(L) | ψ ≤ ϕL } ≤ sup ϕm .\n                                                               m\nThe final assertion is a simple consequence of Dini’s lemma, using the superadditivity of\nm 7→ mϕm .                                                                             \u0003\nProof of Theorem 5.20. By Lemma 5.9, we may assume that θ = c1 (L) with L ∈ Pic(X)Q\nample. Pick ϕ ∈ C0 (X). By Lemma 5.17, we need to show that PL (ϕ) is continuous. Since\nPL(X) is dense in C0 (X) with respect to uniform convergence (see Theorem 2.2), we may\nassume ϕ ∈ PL(X), by (5.1). By Theorem 2.31, we have ϕ = ϕL for a test configuration\n(X , L) for (X, L). After replacing L with a multiple, we may further assume that L and L\nare honest line bundle.\n   Using the notation of Lemma 5.22, we need to show that ϕm := ϕL + m−1 ϕam converges\nuniformly to PL (ϕL ). Since we assume that char k = 0 or dim X ≤ 2 (and hence dim X ≤ 3),\nwe can rely on resolution of singularities and assume that X is smooth and X0 has simple\n\f             GLOBAL PLURIPOTENTIAL THEORY OVER A TRIVIALLY VALUED FIELD                         63\n\nnormal crossings support. We may also assume that there exists an effective vertical Q-\ndivisor E on X such that A := L − E is ample.\n   Assume first that char k = 0, and let bm be the multiplier ideal of the graded sequence am\n                                                                                            • .\n                                                            l\nThe inclusion am ⊂ bm is elementary, and we have bml ⊂ bm for all m, l by the subadditivity\nof multiplier ideals. This implies that\n                      m−1 ϕbm ≥ (ml)−1 ϕbml ≥ (ml)−1 ϕaml ≥ m−1 ϕam\nfor all sufficiently divisible m and l. Letting l → ∞ shows that\n                                ϕL + m−1 ϕbm ≥ PL (ϕL ) ≥ ϕm                                (5.2)\nfor all sufficiently divisible m. By the uniform global generation of multiplier ideals there\nexists m0 ∈ N such that\n\n               OX (mL + m0 A) ⊗ bm = OX ((m + m0 )L) ⊗ OX (−m0 E) ⊗ bm\n  is globally generated for all sufficiently divisible m. This implies that\n                                      ϕbm ≤ ϕam+m0 + C\nfor a constant C independent of m. Combining this with (5.2) yields\n\n                                            m0            m0        C\n                       ϕm ≤ PL (ϕL ) ≤ (1 +    )ϕm+m0 −       ϕL + ,\n                                            m              m        m\nfor all sufficiently divisible m. This shows that PL (ϕL ) is a uniform limit of continuous\nfunctions, and hence continuous.\n   When char k > 0, the very same argument applies with test ideals in place of multiplier\nideals, see [GJKM17] for details.                                                        \u0003\nRemark 5.23. In view of Remark 5.15, Theorem 5.20 is valid also when X is smooth but\npossibly disconnected. A suitable version of Corollary 5.21 is also true.\n",
  "7586713d8cfeadb3c14431c977530b6ab7e8cd770418b97433c6a8cb5e4fe9af": "       7. Functions of finite energy and mixed Monge–Ampère measures\n   In this section, X denotes a projective variety of dimension n, with irreducible components\nXα . We extend the energy pairing to arbitrary psh functions, and use this to define functions\nof finite energy, and the mixed Monge–Ampère operator thereon.\n7.1. Extending the energy pairing. In §3.2, the energy pairing\n                                  (θ0 , ϕ0 ) · . . . · (θn , ϕn ) ∈ R\nwas defined for pairs (θi , ϕi ) ∈ N1 (X) × PLR . When the ϕi are θi -psh, this is an increasing\nfunction of the ϕi , by Lemma 3.15. On the other hand, any ω-psh function with ω ∈\nAmp(X) can be written as a decreasing limit of functions in Hdom (ω) ⊂ PL ∩ PSH(ω) (see\nTheorem 4.15). This allows to extend the energy pairing by monotonicity, as follows.\n\f                GLOBAL PLURIPOTENTIAL THEORY OVER A TRIVIALLY VALUED FIELD                                                       75\n\nTheorem 7.1. For each (n + 1)-tuple ω0 , . . . , ωn ∈ Amp(X), the energy pairing\n                           (ϕ0 , . . . , ϕn ) 7→ (ω0 , ϕ0 ) · . . . · (ωn , ϕn )\nadmits a unique extension to a map ni=0 PSH(ωi ) → R ∪ {−∞} that is\n                                          Q\n\n     • upper semicontinuous;\n     • increasing in each variable.\nFurthermore, this map is continuous along decreasing nets, and satisfies\n                  (ω0 , ϕ0 ) · . . . · (ωn , ϕn ) =             inf             (ω0 , ψ0 ) · . . . · (ωn , ψn )              (7.1)\n                                                       ψi ∈Hdom (ωi ), ψi ≥ϕi\n                  Q\nfor all (ϕi ) ∈       i PSH(ωi ).\n\nProof. Any map that is both usc and increasing is automatically continuous along decreasing\nnets. Since all functions in PSH(ωi ) are limits of decreasing nets in Hdom (ωi ) ⊂ PL(X) ∩\nPSH(ωi ), uniqueness is clear. To prove existence, it suffices to show that (7.1) has the\nrequired properties.\n  Monotonicity is obvious. To prove upper semicontinuity, suppose that ϕi ∈ PSH(ωi ),\n0 ≤ i ≤ n, and t ∈ R satisfy\n                                (ω0 , ϕ0 ) · . . . · (ωn , ϕn ) < t,\nBy definition, we can choose ψi ∈ Hdom (ωi ) and 0 < ε \u001c 1 such that ϕi ≤ ψi and\n                                        (ω0 , ψ0 ) · . . . · (ωn , ψn ) < t − ε.\nSet                                          X\n                                     C :=     (ω0 · . . . · ωbi · . . . · ωn ) > 0.\n                                               i\nBy Proposition 4.28, ϕ 7→ sup(ϕ − ψi ) is continuous on PSH(ωi ), and we can thus find an\nopen neighborhood Ui of ϕi in PSH(ωi ) such that ϕ0i ≤ ψi + εC −1 for all ϕ0i ∈ Ui . By\nmonotonicity of the energy pairing and Proposition 3.14, this gives\n                   (ω0 , ϕ00 ) · . . . · (ωn , ϕ0n ) ≤ (ω0 , ψ0 + εC −1 ) · . . . · (ωn , ψn + εC −1 )\n                                = (ω0 , ψ0 ) · . . . · (ωn , ψn ) + ε < t\n         0\nfor all ϕi ∈ Ui , which proves upper semicontinuity.                                                                             \u0003",
  "35889077944e327cab290328e7574af5034fe06cbbfa97b8df356e917c9a96db": "Theorem 7.18. For each n-tuple (θi , ϕi ) ∈ N1 (X) × E~1 , i = 1, . . . , n, there exists a unique\nsigned measure\n                                                      ^\n             (θ1 + ddc ϕ1 ) ∧ · · · ∧ (θn + ddc ϕn ) = (θi + ddc ϕi ) ∈ C0 (X)∨              (7.14)\n                                                                    i\nsuch that             ˆ             ^\n                                ϕ    (θi + ddc ϕi ) = (0, ϕ) · (θ1 , ϕ1 ) · . . . · (θn , ϕn )    (7.15)\n                         X an        i\nfor all ϕ ∈ PL(X)R . If further θi ∈ Nef(X) and ϕi ∈ PSH(θi ) for i = 1, . . . , n, then (7.14)\nis a positive measure.\n  While the notation mimics the one for mixed Monge–Ampère measures in the complex\nanalytic case, we will not define the individual factors θi + ddc ϕi . At least if the ϕi are\ncontinuous, this could, however, be done using the approach in [CLD12] (cf. Remark 7.23\nbelow).\nProof. By density of PL(X) in C0 (X) (see Theorem 2.2), the prescription (7.15) uniquely\ndetermines the measure (7.14). To show existence, we may assume, by multilinearity, that\nθi ∈ Nef(X) and ϕi ∈ E~1 ∩ PSH(θi ) for i = 1, . . . , n. Since any ϕ ∈ PL(X)R can be written\nas a difference of functions in PLR ∩ PSH(ω) for some ω ∈ Amp(X) (see (3.2)), Lemma 7.15\nshows that ϕ 7→ (0, ϕ) · (θ1 , ϕ1 ) · . . . · (θn , ϕn ) is a positive linear form on PL(X)R . By density\nof PL(X)R in C0 (X), it thus uniquely extends to a positive linear form on C0 (X), and we\nare done.                                                                                              \u0003\n\f82                           SÉBASTIEN BOUCKSOM AND MATTIAS JONSSON\n\nProposition 7.19. Mixed Monge–Ampère measures satisfy the following properties:\n   (i) the signed measure i (θi + ddc ϕi ) is a symmetric and multilinear function of the\n                              V\n\n       n-tuple (θi , ϕi ) ∈ N1 (X) × E~1 , of total mass\n                             ˆ     ^\n                                     (θi + ddc ϕi ) = (θ1 · . . . · θn )X ;\n                                       X an i\n\n     (ii) assume (θi , ϕi ) ∈ N1 (X) × PLR , and pick an integrally closed test configuration X\n          dominating Xtriv and Di ∈ VCar(X )R such that ϕi = ϕDi ; then\n                                   ^                   X\n                                      (θi + ddc ϕi ) =   cE δvE ,\n                                           i                          E\n\n          where E ranges over the irreducible components of X0 and\n                         cE := ordE (X0 )(θ1,X + D1 )|E · . . . · (θn,X + Dn )|E ;\n     (iii) for all (θi , ϕi ) ∈ N1 (X) × E~1 and t ∈ R>0 we have\n                                 ^                           ^\n                                    (θi + ddc (t · ϕi )) = t? (θi + ddc ϕi ),                    (7.16)\n                                   i                                   i\n                        ^                              X        ^\n                             (θi + ddc ϕi ) =                          θi |Xα + ddc ϕi |Xαan ,\n                                                                                            \u0001\n                                                                                                 (7.17)\n                         i                          dim Xα =n i\n                              ^                              ^\n                                       (θi + ddc ϕi ) = ν?          (ν ? θi + ddc ν ? ϕi ) ,     (7.18)\n                               i                                i\n          with ν : X ν → X the normalization;\n     (iv) for any ω ∈ Amp(X), the map E 1 (ω)n 3 (ϕ1 , . . . , ϕn ) 7→ i (θi +ddc ϕi ) is continuous\n                                                                      V\n          along decreasing nets;\n      (v) for all (θi , ϕi ) ∈ N1 (X) × E~1 and ϕ ∈ E~1 , ϕ is integrable against i (θi + ddc ϕi ),\n                                                                                   V\n          and (7.15) holds.\n  When ϕi = 0 for some i, we drop the term ddc ϕi from the notation. As a special case of\nProposition 7.19 (ii), we then have\n                                          X\n                        θ1 ∧ · · · ∧ θn =   (θ1 · . . . · θn )Xα δvtriv,α .        (7.19)\n                                                    dim Xα =n\n\nProof of Proposition 7.19. Points (i) and (iii) follow from Proposition 7.2, while (ii) is a\nreformulation of (3.5). By density of PL(X) in C0 (X), (iv) is equivalent to the fact that,\nfor each ϕ ∈ PL(X),\n                                 ˆ  ^\n            (ϕ1 , . . . , ϕn ) 7→ ϕ   (θi + ddc ϕi ) = (0, ϕ) · (θ1 , ϕ1 ) · . . . · (θn , ϕn )\n                                                i\n\nis continuous along decreasing nets in E 1 (ω)n+1 . Now ϕ can be written as a difference of\nfunctions in PL ∩ PSH(ω 0 ) for some ω 0 ∈ Amp(X), and the desired continuity is thus a\nconsequence of Theorem 7.14. To prove (v), we may assume θi ∈ Amp(X) and ϕi ∈ E 1 (θi ),\nby multilinearity. Any ϕ ∈ E 1 (ω) with ω ∈ Amp(X) can be written as the pointwise limit\nof a decreasing net in PL ∩ PSH(ω), and (7.15) thus holds for ϕ, by monotone convergence\nand the continuity of the energy pairing along decreasing limits.                        \u0003\n\f              GLOBAL PLURIPOTENTIAL THEORY OVER A TRIVIALLY VALUED FIELD                                 83\n\nExample 7.20. Assume X is a smooth curve and pick ω ∈ Amp(X). By Example 4.13,\nany ϕ ∈ PSH(ω) determines a positive Radon measure (deg ω)δvtriv + ∆ϕ, with\n              X \u0014d                                                     d2\n                                                                                     \u0015\n                                             d\n        ∆ϕ =              ϕ(t ordp )δvtriv −       ϕ(t ordp )δvp,triv + 2 ϕ(t ordp )\n                    dt 0+                    dt +∞                     dt\n                 p∈X(k)\n\nthe tree Laplacian (see [FJ04, §7]). As we saw in Example 3.19, we have ω + ddc ϕ =\n(deg ω)δvtriv + ∆ϕ for any ϕ ∈ PLR ∩ PSH(ω), and this remains true for any ϕ ∈ E 1 (ω),\nby monotone approximation. For such functions, ω + ddc ϕ further puts no mass on the\nendpoints vp,triv , which means that the convex function t 7→ ϕ(t ordp ) has sublinear growth\n(see respectively Corollary 7.49 and Theorem 11.11).\nProposition 7.21. Pick ωi ∈ Amp(X) and ϕi ∈ E 1 (ωi ), i = 1, . . . , n, and choose also\nω0 ∈ Amp(X) and ϕ0 ∈ PSH(ω0 ). Then:\n    (i) ϕ0 is integrable with respect to µ := i (ωi + ddc ϕi ) iff (ω0 , ϕ0 ) · . . . · (ωn , ϕn ) > −∞,\n                                             V\n        and this holds as soon as ϕi is bounded for i = 1, . . . , n;\n   (ii) assume ϕ0 ∈ L1 (µ). Pick for i = 0, . . . ,Vn a decreasing net (ϕij )j in PSH(ωi ) that\n        converges pointwise to ϕi , and set µj := i (ωi + ddc ϕij ). Then ϕ0j ∈ L1 (µj ) for all\n        j, and ϕ0j µj → ϕ0 µ weakly in C0 (X)∨ .\nLemma 7.22. Let K be a compact topological space with a weakly convergent net of positive\nRadon measures µj → µ. Assume also given an increasing net of lsc             ´ fj : K →\n                                                                     ´ functions\nR ∪ {+∞} such that fj ∈ L1 (µj ) for all j, f := limj fj ∈ L1 (µ) and fj µj → f µ. Then\nfj µj → f µ weakly in C0 (K)∨ .\nProof. Being lsc, each fj is bounded below, and the increasing net (fj ) is thus ultimately\nbounded below. Since ´µj → µ, we may therefore assume, after adding a constant, that\nfj ≥ 0 for all j. Since fj µj converges, the positive measures σj := fj µj stay in a fixed\nweakly compact subset of C0 (X)∨ , and it suffices\n                                              ´ to show\n                                                      ´    that any\n                                                                 ´ limit ´point σ∞ of σj\nmust coincide with σ := f µ. By assumption, σj → σ, hence σ∞ = σ, and it will\nthus be enough to show that σ∞ ≥ σ. To this end, pick 0 ≤ g ∈ C0 (K). For all j ≥ k we\nhave fj ≥ fk , and hence       ˆ       ˆ           ˆ\n                                      g σj =    gfj µj ≥      gfk µj .\n                                                                                    ´            ´\nBy lower semicontinuity of gfk and the weak convergence µj → µ, we infer                g σ∞ ≥       gfk µ.\nUsing monotone convergence, this now yields in turn,\n                                ˆ         ˆ         ˆ\n                                   g σ∞ ≥ gf µ = g σ,\n\nwhich concludes the proof.                                                                               \u0003\nProof of Proposition 7.21. Set c := (ω0 , 0) · (ω1 , ϕ1 ) · . . . · (ωn , ϕn ) ∈ R, and pick a decreasing\nnet (ϕ0j ) in PL ∩ PSH(ω0 ) such that ϕ0j → ϕ0 pointwise. By construction of µ, we have for\neach j                         ˆ\n                                  ϕ0j µ = (ω0 , ϕ0j ) · (ω1 , ϕ1 ) · . . . · (ωn , ϕn ) − c.\n                         ´           ´\nBy Lemma 7.17, ϕ0j µ → ϕ0 µ. By Theorem 7.1, we have on the other hand (ω0 , ϕ0j ) ·\n(ω1 , ϕ1 ) · . . . · (ωn , ϕn ) → (ω0 , ϕ0 ) · (ω1 , ϕ1 ) · . . . · (ωn , ϕn ). Thus\n                                ˆ\n                                   ϕ0 µ = (ω0 , ϕ0 ) · (ω1 , ϕ1 ) · . . . · (ωn , ϕn ) − c,\n\f84                            SÉBASTIEN BOUCKSOM AND MATTIAS JONSSON\n\nand (i) follows.\n  We turn to (ii). By Proposition 7.19 (iv), we have µj → µ. Further,\n            ˆ\n              ϕ0j µj = (ω0 , 0) · (ω1 , ϕ1j ) · . . . · (ωn , ϕnj ) − (ω0 , ϕ0j ) · . . . · (ωn , ϕnj )\n\nis finite for each j, and converges to\n                ˆ\n                  ϕ0 µ = (θ0 , 0) · (ω1 , ϕ1 ) · . . . · (ωn , ϕn ) − (ω0 , ϕ0 ) · . . . · (ωn , ϕn ).\n\nThe result is now a consequence of Lemma 7.22.                                                                \u0003\nRemark 7.23. For continuous ω-psh functions, mixed Monge–Ampère measures can also be\ndefined using the general theory developed by Chambert-Loir and Ducros [CLD12]. By base\nchange invariance of their theory, it follows from Proposition 7.19 (ii) and [BE20, Theorem\n8.18] that the present approach is compatible with [CLD12] for continuous ω-psh functions.\n7.4. The Monge–Ampère operator and energy functionals. In this section we fix\nω ∈ Amp(X). We denote by V := (ω n ) its volume, and write E 1 := E 1 (ω) and E := Eω .\nDefinition 7.24. The Monge–Ampère operator takes ϕ ∈ E 1 to the Radon probability\nmeasure\n                      MA(ϕ) = MAω (ϕ) := V −1 (ω + ddc ϕ)n\non X an .\nDefinition 7.25. For any two ϕ, ψ ∈ E 1 we set\n                                                                      ˆ\n                         Jψ (ϕ) = Jω,ψ (ϕ) = E(ψ) − E(ϕ) +                (ϕ − ψ) MA(ψ)\n\nand\n                                                      ˆ\n                           I(ϕ, ψ) = Iω (ϕ, ψ) =          (ϕ − ψ) (MA(ψ) − MA(ϕ))\n                                                   = Jψ (ϕ) + Jϕ (ψ).\n\n Note that Jψ (ϕ) and I(ϕ, ψ) are both invariant under translation of ϕ, ψ by constants.\nWhen ψ = 0 we simply write\n                                      ˆ             ˆ\n                     I(ϕ) := I(ϕ, 0) = ϕ MA(0) − ϕ MA(ϕ)",
  "fc205b71fa16f7a8a9be5278f5ede544014742d555d733274dc8b473587e26f2": "   l\n\nThus\n                      lim(θ0 , ϕ0j ) · . . . · (θn , ϕnj ) ≥ (θ0 , 0) · (θ1 , ϕ1 ) · . . . · (θn , ϕn )\n                       j\n             ˆ\n         +       ϕ0 (θ1 + ddc ϕ1 ) ∧ · · · ∧ (θn + ddc ϕn ) = (θ0 , ϕ0 ) · (θ1 , ϕ1 ) · . . . · (θn , ϕn ),\nand we are done.                                                                                                  \u0003\nRemark 7.39. Lemma 7.37 and Theorem 7.38 remain valid when X is reducible, by (7.17)\nand (7.4), respectively.\n7.6. Locality and the comparison principle. The next result and its consequences play a\ncrucial role in analyzing deep properties of ω-psh functions and the Monge-Ampère operator.\nTheorem 7.40. If ω ∈ Amp(X), then\n                                1{ϕ>ϕ0 } MA(max{ϕ, ϕ0 }) = 1{ϕ>ϕ0 } MA(ϕ)                                     (7.32)\nfor all ϕ, ϕ0 ∈ E 1 (ω).\n  A first consequence is the fact that the mixed Monge–Ampère operator is local in nature,\nsomething that is not an immediate consequence of our definition in §7.3.\nCorollary 7.41. Let G ⊂ X an be open set. If ωi ∈ Amp(X) and ϕi , ψi ∈ E 1 (ωi ), 1 ≤ i ≤ n,\nare such that ϕi = ψi on G, then\n       (ω1 + ddc ϕ1 ) ∧ · · · ∧ (ωn + ddc ϕn ) = (ω1 + ddc ψ1 ) ∧ · · · ∧ (ωn + ddc ψn ) on G.\nIn particular, if ω ∈ Amp(X) and ϕ, ϕ0 ∈ E 1 (ω) are such that ϕ = ϕ0 on G, then MA(ϕ) =\nMA(ϕ0 ) on G.\nProof. By multilinearity, it suffices to prove the final statement. As in [BFJ15, Corollary 5.2],\ngiven ε > 0 we apply Theorem 7.40 to ϕ+ε and ϕ0 . This gives MA(max{ϕ+ε, ϕ0 }) = MA(ϕ)\non G ⊆ {ϕ+ε > ϕ0 }. Letting ε → 0 gives MA(max{ϕ, ϕ0 }) = MA(ϕ) on G, since the Monge–\nAmpère operator is continuous under decreasing limits. Exchanging the roles of ϕ and ϕ0\ncompletes the proof.                                                                           \u0003\nRemark 7.42. As mentioned in Remark 7.23, when all the functions involved are continu-\nous, the mixed Monge–Ampère measure coincides with the one in [CLD12]. Since the latter\nis local in nature, Theorem 7.40 and Corollary 7.41 follow in this case. However, for appli-\ncations it is important to consider functions ϕ, ϕ0 that are not continuous, and in this case\nthe Borel set {ϕ > ϕ0 } can be quite complicated. By definition, it is an open subset in the\nplurifine topology, see [BT87].\nLemma 7.43. Let ϕ, ϕ0 ∈ PL(X), and pick an integrally closed test configuration X such\nthat ϕ, ϕ0 and ϕ00 := max{ϕ, ϕ0 } are associated to elements D, D0 , D00 of VCar(X )Q . Pick\nan irreducible component E of X0 , and assume that ϕ(vE ) > ϕ0 (vE ). Then ϕ(vF ) ≥ ϕ0 (vF )\nfor any irreducible component F of X0 that intersects E.\n\f92                          SÉBASTIEN BOUCKSOM AND MATTIAS JONSSON\n\nProof. First, ϕD00 −D = ϕD00 − ϕD ≥ 0 implies D00 − D ≥ 0, by Lemma 2.8, and similarly\nD00 − D0 ≥ 0. Furthermore, 0 < ϕ00 (vE ) − ϕ0 (vE ) = σ(vE )(D00 − D0 ), and E is thus in the\nsupport of D00 − D0 . Now pick any k × -invariant divisorial valuation w on X with center\nξ ∈ E ∩ F , normalized by w(X0 ) = 1; denote by v ∈ X div its restriction to k(X) ,→ k(X ), so\nthat w = σ(v) (see §1.3). Then w(D00 − D0 ) = ϕ00 (v) − ϕ0 (v) > 0, and hence ϕ00 (v) = ϕ(v).\nThis means that D00 = D at ξ; hence 0 = σ(vF )(D00 − D) = ϕ00 (vF ) − ϕ(vF ), which proves\nthe result.                                                                                 \u0003\nProof of Theorem 7.40. First assume that ϕ, ψ ∈ PL ∩ PSH(ω). As in Lemma 7.43, pick\nan integrally closed test configuration X dominating the trivial one, such that ϕ = ϕD ,\nϕ0 = ϕD0 and max{ϕ, ϕ0 } = ϕD00 with D, D0 , D00 ∈ VCar(X )Q . As in Proposition 7.19 (ii)\nwe have                                  X\n                         MA(ϕD ) = V −1     bE ((ωX + D)|E )n δvE ,\n                                                   E\nand a similar formula holds for MA(ϕ ). We thus need to show that ((ωX + D)|E )n =\n                                             D00\n((ωX + D00 ])|E )n for any E with ϕD (vE ) > ϕD0 (vE ). Now Lemma 7.43 yields ϕD (vF ) =\nmax{ϕ(vF ), ϕ0 (vF )} = ϕD00 (vF ) for all components F of X0 that intersect E. This implies\nthat D and D00 coincide in a neighborhood of E. Hence D|E = D00 |E , which implies the\nresult.\n   Now consider the general case. Set\n                             f := max{ϕ − ϕ0 , 0} = max{ϕ, ϕ0 } − ϕ0 .\nThen {ϕ > ϕ0 } = {f > 0}, and it thus suffices to prove that\n                                  f MA(max{ϕ, ϕ0 }) = f MA(ϕ).                                   (7.33)\nIndeed, multiplying by f −1 on {f > 0} will then yield the result.             Let (ϕj )j and (ϕ0j )j be\ndecreasing nets in PL ∩ PSH(ω) converging to ϕ and ϕ0 , respectively, and set\n                            fj := max{ϕj − ϕ0j , 0} = max{ϕj , ϕ0j } − ϕ0j .\nBy the first part of the proof we have fj MA(max{ϕj , ϕ0j }) = fj MA(ϕj ), and (7.33) is now\na consequence of Proposition 7.19 (iii), since max{ϕj , ϕ0j } ∈ E 1 (ω) decreases to max{ϕ, ϕ0 }.\n                                                                                               \u0003\n     Using Theorem 7.40 we obtain the very useful comparison principle.\nTheorem 7.44. If ω ∈ Amp(X) and ϕ, ψ ∈ E 1 (ω), then\n                          ˆ                 ˆ\n                              MA(ϕ) ≥           MA(ψ).\n                                  {ϕ<ψ}                {ϕ<ψ}\n\nProof. We follow [GZ07, Theorem 1.5]. For any ε > 0 we have\n      ˆ                         ˆ                                          ˆ\n  1 = MA(max{ϕ, ψ − ε}) ≥             MA(max{ϕ, ψ − ε}) +                          MA(max{ϕ, ψ − ε})\n                                    {ϕ<ψ−ε}                              {ϕ>ψ−ε}\n                    ˆ                    ˆ                       ˆ                     ˆ\n              =             MA(ψ) +             MA(ϕ) = 1 +              MA(ψ) −              MA(ϕ),\n                  {ϕ<ψ−ε}             {ϕ>ψ−ε}                  {ϕ<ψ−ε}              {ϕ≤ψ−ε}\n\nwhere the second equality follows from Theorem 7.40 and from MA(ϕ − ε) = MA(ϕ). We\ncomplete the proof by letting ε → 0.                                             \u0003\n\f            GLOBAL PLURIPOTENTIAL THEORY OVER A TRIVIALLY VALUED FIELD                          93\n\n  Another simple consequence of Theorem 7.40 is the following formula for the I-functional.\nProposition 7.45. If ω ∈ Amp(X), and ϕ, ψ ∈ E 1 (ω), then max{ϕ, ψ} ∈ E 1 (ω), and\n                          I(ϕ, ψ) = I (ϕ, max{ϕ, ψ}) + I (max{ϕ, ψ}, ψ) .                   (7.34)",
  "6761fc6a62172ae300314992e07f19aad4374781c7751d19e493ec0bc482e75d": "by monotonicity of volL . On the other hand, Theorem 5.1.1 of [Reb21] (which is valid for\narbitrary non-Archimedean fields; see also [BoJ18b, Theorem 4.13] for the trivially valued\ncase) shows that\n                                                           |s|\n                           ρm := m−1 log       sup\n                                             0\n                                          s∈H (X,mL)\\{0} ksk mρ\n\nsatisfies ρm ∈ PLR ∩ PSH(ω), ρm ≤ ρ and EL (ρm ) → volL (ρ); the claim follows.\n   In particular, EL (ϕ + f ) = volL (ϕ + f ) and EL (ϕ) = volL (ϕ). The desired estimate is\nnow a consequence of Lemma 8.8 below, itself a reformulation of [BGM20, Lemma 3.2]. \u0003\nLemma 8.8. Let L and L0 be ample line bundles on X, and set ω = c1 (L), ω 0 = c1 (L0 ).\nConsider functions ϕ ∈ CPSH(ω), and ψ1 , ψ2 ∈ CPSH(ω 0 ). Set f := ψ1 − ψ2 ∈ C0 and\nC := Vω+ω0 − Vω > 0. Then\n               ˆ\n    C inf\n        an\n           f≤      f (ω + ω 0 + ddc (ϕ + ψ1 ))n − Vω (volL (ϕ + f ) − volL (ϕ)) ≤ C sup f.\n       X        X an                                                              X an\n\f             GLOBAL PLURIPOTENTIAL THEORY OVER A TRIVIALLY VALUED FIELD                      99\n\nProof. This is a reformulation in our context of [BGM20, Lemma 3.2] in the special case\nof a trivially valued field k. The fact that k is trivially valued means that we can view ϕ,\nψ1 , ψ2 as continuous psh metrics on the Berkovich analytifications of the line bundles L and\nL0 , respectively. The difference volL (ϕ + f ) − volL (ϕ) can be viewed as the relative volume\nof the metrics ϕ + f and ϕ on L. Note that our current normalization of the volume differs\nfrom the one in loc.cit. by a factor Vω = (Ln ).                                              \u0003\nProof of Theorem 8.5. We argue along the lines of the proof of [BGM20, Theorem 3.1].\nWrite ϕ ∈ E 1 as the limit of a decreasing net (ϕi ) in CPSH(ω). Then E(ϕi +εf ) → E↓ (ϕ+εf )\n(by Proposition 8.3 (v)), E(ϕi ) → E(ϕ) (by continuity of E along decreasing nets in PSH(ω)),\nand MA(ϕi ) → MA(ϕ) weakly (by Proposition 7.19).\n  It is therefore enough to prove the result for ϕ ∈ CPSH(ω). Since f ∈ PL(X)R , we can\nchoose ω 0 ∈ Amp(X) and ψ1 , ψ2 ∈ PLR ∩ PSH(ω 0 ) such that f = ψ1 − ψ2 . By Lemma 8.7\nwe have, for any ε > 0,\n                                   ˆ\n                                −1\n                                                                    \u0001n\n   Eω (ϕ + εf ) − Eω (ϕ) − εVω       f ω + ddc ϕ + ε(ω 0 + ddc ψ1 )\n\n                                                                ≤ ε Vω−1 Vω+εω0 − 1 sup |f |.\n                                                                                   \u0001\n\nNow Vω−1 Vω+εω0 − 1 = O(ε), while\n                                              n \u0012 \u0013\n                               \u0001n             X  n j\nVω−1         c          0          c       −1\n       ω + dd ϕ + ε(ω + dd ψ1 ) = MAω (ϕ)+Vω       ε (ω+ddc ϕ)n−j ∧(ω 0 +ddc ψ1 )j ,\n                                                 j\n                                                          j=1\n\nwhere (ω + ddc ϕ)n−j ∧ (ω 0 + ddc ψ1 )j is a Radon measure of mass (ω n−j · ω 0j ). The result\nfollows.                                                                                    \u0003\nProof of Corollary 8.6. For f ∈ PL(X)R the result follows directly from Theorem 8.5. For\nan arbitrary f ∈ C0 (X) we argue as in the proof of [BGM20, Theorem 3.1]. By Theorem 2.2,\nwe can pick a sequence (fm ) in PL(X)R such that εm := sup |f − fm | → 0. For each t > 0,\nwe have fm − tεm ≤ f ≤ fm + tεm ; Proposition 8.3 (i) thus yields\n                  E↓ (ϕ + tfm ) − tεm ≤ E↓ (ϕ + tf ) ≤ E↓ (ϕ + tfm ) + tεm ,\nand hence          ˆ                                \u0010                 \u0011\n                     fm MA(ϕ) − εm ≤ lim inf t−1 E↓ (ϕ + tf ) − E↓ (ϕ)\n                                           t→0+\n                                \u0010                    \u0011 ˆ\n                             −1    ↓             ↓\n                 ≤ lim sup t      E (ϕ + tf ) − E (ϕ) ≤ fm MA(ϕ) − εm ,\n                       t→0+\nby Theorem 8.5 applied to fm . Letting m → ∞, we get\n                               \u0010                    \u0011 ˆ\n                            −1    ↓             ↓\n                      lim t      E (ϕ + tf ) − E (ϕ) = f MA(ϕ),\n                            t→0+",
  "270fead3dbb82f56e8bbef72623105fefa2846687a26b95f4a9f15a28b502f36": "Corollary 9.18. Pick µ ∈ M1 . If (ϕi ) is maximizing for µ then limi ϕi (MA(ϕi ) − µ) = 0\nand limi E∨ (MA(ϕi )) = E∨ (µ).\n\f             GLOBAL PLURIPOTENTIAL THEORY OVER A TRIVIALLY VALUED FIELD                            105\n\nProof. By Corollary 9.16, J(ϕi ) is bounded for i large enough. By Lemma 9.17, it follows\nthat                         ˆ         ˆ\n                                                                1\n                        ci := ϕi µ − ϕi MA(ϕi ) = O(Jµ (ϕi ) 2 )\ntends to 0, and hence\n                                       ˆ                           ˆ\n             ∨\n            E (MA(ϕi )) = E(ϕi ) −         ϕi MA(ϕi ) = E(ϕi ) −       ϕi µ + ci → E∨ (µ),\n\ncompleting the proof.                                                                               \u0003\n  As another useful consequence, we get:\nProposition 9.19. Let ϕi → ϕ be a convergent net in PSH(ω), and assume that J(ϕi ) is\neventually bounded. For any µ ∈ M1 we then have ϕi → ϕ in L1 (µ).\n                                    ´\nProof. We first claim that ψ 7→ ψ µ is continuous on {J ≤ C} ⊂ PSH(ω) for ´any C > 0.\nTo see this, pick a maximizing net (ρj )j for µ in PL ∩ PSH(ω). For each          ´ j, ϕ 7→ ϕ MA(ρ ´ j)\nis continuous on PSH(ω), by Proposition 7.19 (ii). By Lemma 9.17, ψ MA(ρj ) → ψ µ\nuniformly for ψ ∈ {J ≤ C} ⊂ PSH(ω), and the claim follows since continuity is preserved\nunder uniform convergence.\n   The functional J is lsc, so J(ϕ) ≤ lim inf J(ϕi ) < ∞. Set ϕ0i := max{ϕi , ϕ}, so that\n|ϕi − ϕ| = 2(ϕ0i − ϕ) + (ϕi − ϕ). Then ϕ0i → ϕ pointwise on X div , i.e. ϕ0i → ϕ in PSH(ω).\nBy (7.34) we further have I(ϕ0i , ϕ) ≤ I(ϕi , ϕ), and J(ϕ0i ) ≈ I(ϕ0i , 0) is thus eventually\n                                                                                        ´      bounded,\n                                                                                                  ´\nby\n´ 0 the quasi-triangle\n          ´            inequality\n                            ´      for I. The  first part of  the proof    thus  yields   ϕi µ → ϕ µ,\n  ϕi µ → ϕ µ, and hence |ϕi − ϕ|µ → 0, which concludes the proof.                                    \u0003\n9.4. Dependence on the ample class. In this section, X is assumed to be irreducible.\nAs in [BBGZ13, Proposition 3.4] we then have the following useful characterization of mea-\nsures of finite energy.\nTheorem 9.20. A Radon probability measure µ ∈ M has finite energy iff E 1 ⊂ L1 (µ).\nProof. Assume that´ µ is finite on E 1 . We first claim that for each C > 0 there exists\n  0                           0\nC > 0 such that ϕ µ ≥ −C for all ϕ ∈ Esup   1  such that − E(ϕ) = J(ϕ) ≤ C. Arguing by\ncontradiction, we may assume there exist C > 0 and a sequence (ϕj )∞          1\n                                                                      1 in Esup such that\n                ´          j\n                                                    Pm −j\nJ(ϕ) ≤ C and ϕj µ ≤ −2 for all j. Set ψm := j=1 2 ϕj for m ≥ 1. Then ψm is a\ndecreasing sequence in PSH(ω) converging to ψ := ∞          −j\n                                                    P\n                                                      j=1 2 ϕj , which is thus either ω-psh\nor identically −∞ (since X is irreducible). By concavity of E we have E(ψm ) ≥ −C for all\nm; hence ψ is ω-psh, with E(ψ) = limm→∞ E(ψm ) ≥ −C. On the other hand, monotone\nconvergence gives\n                   ˆ              ˆ               m\n                                                  X       ˆ\n                     ψ µ = lim      ψm µ = lim        2−j ϕj µ = −∞,\n                               m→∞                  m→∞\n                                                          j=1\na contradiction. We next claim that there exist A, B > 0 such that\n                                 ˆ\n                                    ϕ µ ≤ A J(ϕ)1/2 + B\n             1 , which will imply, as desired, that\nfor all ϕ ∈ Esup\n                                             \u0012 ˆ      \u0013\n                              ∨\n                             E (µ) = sup − ϕ µ − J(ϕ)\n                                              1\n                                           ϕ∈Esup\n\f106                       SÉBASTIEN BOUCKSOM AND MATTIAS JONSSON\n\nis finite. If J(ϕ) ≤ 1 then the estimate follows from the first part of the proof. We may\nthus assume t := J(ϕ)−1/2 ≤ 1. By Lemma 7.33, J(tϕ) ´. t2 J(ϕ) = 1, and the first part of\nthe proof yields a uniform constant A > 0 such that t ϕ µ ≤ A, which gives the desired\nestimate.                                                                              \u0003\n  As in [DiN16, Proposition 4.1], we infer:\nCorollary 9.21. The set M1 (ω) of measures of finite energy is independent of the choice\nof ω ∈ Amp(X), and it is dense in the space M of all Radon probability measures on X an .",
  "62f80f85972d10a128333605eab0a471a0637f52978e2bf99fd42723b6ba6858": "                             ˆ           ˆ\n                        0 ≤ ϕ MA(0) − ϕ µ ≤ J(ϕ) + E∨ (µ),\n\nwhich holds by definition of E∨ .\n  As an important consequence of Theorem 10.3, we have:\nCorollary 10.4. Assume that X is equidimensional. If ϕ, ψ ∈ E 1 , then the following\nproperties are equivalent:\n     (i) MA(ϕ) = MA(ψ);\n    (ii) I(ϕ, ψ) = 0;\n   (iii) ϕ − ψ is locally constant.\n                                                                                        \u0001\nProof. The implications (iii)⇒(i)⇒(ii) are clear. If I(ϕ, ψ) = 0, then I ϕ|Xαan , ψ|Xαan = 0\nfor each irreducible component Xα of X, by (7.26). In order to prove that ϕ − ψ is locally\nconstant, we may thus assume that X is irreducible. After adding constant, assume sup ϕ =\nsup ψ. Then ϕ(v) = ψ(v) for every v ∈ X div , as a consequence of Theorem 10.3 with µ = δv\nand µ0 = δvtriv , since δv ∈ M1 by Proposition 11.1. By Theorem 4.22, we infer ϕ = ψ on\nX an , which proves (ii)⇒(iii).                                                           \u0003\n\f             GLOBAL PLURIPOTENTIAL THEORY OVER A TRIVIALLY VALUED FIELD             109\n\n  Corollary 10.4 in turn implies the following useful results.\nCorollary 10.5. Assume that X is equidimensional. If ϕ, ψ ∈ E 1 satisfy ϕ ≥ ψ and\nE(ϕ) = E(ψ), then ϕ = ψ.\nProof. By (7.4), we may assume that X is connected. From (7.22) and the assumptions, it\nfollows that           ˆ                  ˆ\n                              (ϕ − ψ) MA(ϕ) =          (ϕ − ψ) MA(ψ) = 0.\n                ´\nThus I(ϕ, ψ) = (ϕ − ψ)(MA(ψ) − MA(ϕ)) = 0, and hence ψ = ϕ + c for a constant c, by\nCorollary 10.4. But then E(ϕ) = E(ψ) = 0 gives c = 0 and we are done.             \u0003\nCorollary 10.6 (Domination principle). Assume that X is equidimensional. Let ϕ ∈\nPSH(ω), ψ ∈ E 1 , and assume ϕ ≤ ψ a.e. with respect to MA(ψ). Then ϕ ≤ ψ on X an .\nProof. Arguing on each connected component, we may assume that X is connected. After\nreplacing ϕ with max{ϕ, ψ}, we may assume ϕ ≥ ψ, and hence ϕ ∈ E 1 . The assumption\nthen becomes ϕ = ψ a.e for MA(ψ), and we need to show ϕ = ψ. Note that\n                      ˆ                            ˆ\n             I(ϕ, ψ) = (ϕ − ψ)(MA(ψ) − MA(ϕ)) = (ψ − ϕ) MA(ϕ) ≤ 0.\n\nBy Corollary 10.4, we infer ϕ = ψ + c with c ∈ R, and ϕ = ψ a.e. for MA(ψ) implies\nc = 0.                                                                          \u0003\n\n10.2. Proof of Theorems 10.2 and 10.3.",
  "6bb578ad44c78dbe18f74ff227167f6d88a7660585784c3d499fac7a48f2705a": "Theorem 12.8. For any ω ∈ Amp(X), the following are equivalent:\n    (i) the envelope property holds for ω;\n   (ii) the Monge–Ampère operator MAω : E 1 (ω) → M1 is onto;\n  (iii) the Monge–Ampère operator induces a bi-Lipschitz isomorphism\n                                  (E 1 (ω)/R, Iω ) ≃ (M1 , I∨\n                                                            ω );\n\f122                         SÉBASTIEN BOUCKSOM AND MATTIAS JONSSON\n\n      (iv) (E 1 (ω)/R, Iω ) is complete;\n       (v) (E 1 (ω), Iω ) is complete.\n  In particular, E 1 (ω) can only be complete if X is unibranch, cf. Theorem 5.12.\nProof. Assume (i). By Corollary 9.12, (ii) holds iff the supremum defining\n                                            \u0012          ˆ     \u0013\n                              ∨\n                             E (µ) = sup E(ϕ) − ϕ µ\n                                             ϕ∈E 1\n\nis achieved for any µ ∈ M1 . Thus choose a maximizing sequence (ϕi ) for µ in Esup     1 . By\n\nCorollary 5.21, PSHsup is weakly compact, and we may thus assume, after passing to a\nsubnet, that (ϕi ) converges weakly to ϕ ∈ PSHsup . Since Jµ (ϕi ) → 0, (9.11) shows that J(ϕi )\nis eventually bounded, and hence that ´ϕ ∈ E 1 (ω),\n                                                 ´ since J is weakly lsc. By Proposition 9.19,\nthe weak convergence ϕi → ϕ implies ϕi µ → ϕ µ, and hence\n                             ˆ              \u0012          ˆ       \u0013\n                     E(ϕ) − ϕ µ ≥ lim sup E(ϕi ) − ϕi µ = E∨ (µ),\n                                             i\nsince E is weakly usc. This proves (i)⇒(ii). Proposition 12.7 gives (ii)⇔(iii), and (iii)⇒(iv)\nfollows from the completeness of (M1 , I∨    ω ) (Theorem 10.14).\n   Assume (iv), and pick a Cauchy sequence (ϕi ) in (E 1 (ω), Iω ). Then (ϕi −sup ϕi ) is Cauchy\n     1 (ω) ≃ E 1 (ω)/R, and hence strongly convergent in E 1 (ω). Now (sup ϕ ) is Cauchy as\nin Esup                                                                            i\nwell, and hence convergent in R, so we conclude that (ϕi ) is strongly convergent, proving\n(iv)⇒(v).\n   Finally we prove (v)⇒(i). Assume that E 1 (ω) is complete. By Theorem 5.11, (i) is\nequivalent to the fact that any bounded, increasing net (ϕi ) in PSH(ω) converges weakly in\nPSH(ω). Since the increasing net (sup ϕi ) converges in R, it will be enough to show that\n(ϕi ) is Cauchy in E 1 (ω)/R, i.e. that\n                                                                 ˆ\n              Iω (ϕi , ϕj ) ≈ Jω,ϕi (ϕj ) = Eω (ϕi ) − Eω (ϕj ) + (ϕj − ϕi ) MAω (ϕi )\n\ntends to 0 as i, j → ∞, where by symmetry of Iω we may assume i ≤ j. The increasing net\n(Eω (ϕi )) converges in R. Given ε > 0, choose i0 such that 0 ≤ Eω (ϕj ) − Eω (ϕi ) ≤ ε for\nj ≥ i ≥ i0 . As ϕi ≤ ϕj , (7.22) yields\n                   ˆ\n              0 ≤ (ϕj − ϕi ) MAω (ϕi ) ≤ (n + 1) (Eω (ϕj ) − Eω (ϕi )) ≤ (n + 1)ε.\n\nThus                                               ˆ\n                           Eω (ϕi ) − Eω (ϕj ) +       (ϕj − ϕi ) MAω (ϕi ) ≤ nε,\nwhich proves, as desired, that (ϕi ) is Cauchy in E 1 (ω)/R.                                  \u0003\n   As a direct consequence of Theorem 12.8 and Theorem 5.20, we have the following result,\ncf. Theorem A.\nTheorem 12.9. Suppose that X is smooth, that char k = 0 or dim X ≤ 2, and fix ω ∈\nAmp(X). Then the Monge–Ampère equation MA(ϕ) = µ admits a solution ϕ ∈ E 1 (ω),\nunique up to translation, for every µ ∈ M1 .",
  "1a960d306b0bfa9c63f5fccc4deaf63139c4f5ef3d7d2649af14fc4f133ab07b": "Theorem 12.16. Pick θ ∈ N1 (X). Let (ϕi )i∈I be a monotone (i.e. increasing or decreasing)\nnet in PSH(θ), and assume that it converges to ϕ ∈ PSH(θ). Then there exists an increasing\nmap N → I m 7→ i(m) such that limm→∞ ϕi(m) = ϕ in PSH(θ).\nRemark 12.17. Note that (ϕi(m) )m∈N is not claimed to be a subnet of (ϕi )i∈I , as the directed\nset I might not admit any countable cofinal subset. On the other hand, by monotonicity of\n(ϕi ), the sequence (ϕi0 (m) ) also converges to ϕ for any increasing map m 7→ i0 (m) such that\ni0 (m) ≥ i(m).\nProof. Assume first that X is irreducible. Pick θ0 ∈ Amp(X) such that θ0 − θ is nef. Then\nPSH(θ) ⊂ PSH(θ0 ), and it is enough to show the result when ω := θ is ample, which we now\nassume.\n   Suppose first that ϕ and all the ϕi lie in E 1 (ω). By Example 12.2 (resp. Theorem 12.5),\nwe have ϕi → ϕ strongly, i.e. limi∈I I(ϕi , ϕ) = 0. We can thus inductively construct an\n\f             GLOBAL PLURIPOTENTIAL THEORY OVER A TRIVIALLY VALUED FIELD                           125\n\nincreasing map m 7→ i(m) such that I(ϕi(m) , ϕ) ≤ 1/m. Then limm ϕi(m) = ϕ strongly in\nE 1 (ω), and hence in PSH(ω) (i.e. pointwise on X div ).\n    Consider now the general case. Observe first that we may assume wlog ϕ ≤ 0 and ϕi ≤ 0\nfor all i. If (ϕi ) is increasing, it suffices to replace ϕi with ϕi − sup ϕ. If (ϕi ) is decreasing,\nreplace I with {i ∈ I | i ≥ i0 } for some i0 ∈ I, and ϕi with ϕi − sup ϕi0 .\n    By Corollary 4.11, we then have\n                         ϕ̃ := exp(ϕ), ϕ̃i := exp(ϕi ) ∈ E ∞ (ω) ⊂ E 1 (ω).\nBy what precedes, we can find an increasing map m 7→ i(m) such that ϕ̃i(m) → ϕ̃ pointwise\non X div . Since the ϕi and ϕ are finite-valued on X div , this implies ϕi(m) → ϕ on X div , and\nwe are done.\n   Assume finally that X is reducible. For each α, the previous step yields an increasing\nm 7→ iα (m) such that ϕiα (m) → ϕ on Xαan . By Remark 12.17, it remains to pick any\nincreasing map m 7→ i(m) such that i(m) ≥ maxα iα (m) for all m; such a map is easily\nconstructed by induction on m.                                                                 \u0003\n  Combining Theorem 12.16 with Theorem 4.15, we infer:\nCorollary 12.18. Pick θ ∈ N1 (X) and ϕ ∈ PSH(θ). Then:\n                                                                        gf\n     (i) ϕ can be written as the limit of a decreasing sequence ϕm ∈ HQ    (Lm ) with Lm ∈\n         Pic(X)Q such that c1 (Lm ) − θ is ample and limm c1 (Lm ) = θ;\n    (ii) if θ ∈ Nef(X) then (i) holds with ϕm ∈ H(Lm ) and Lm ample;\n   (iii) if θ ∈ Amp(X), then ϕ can be written as the limit of a decreasing sequence in\n         Hdom (θ) (see Definition 3.8).\nRemark 12.19. A version of (iii) was proved in [BFJ15, Proposition 4.7], using the\nBedford–Taylor capacity instead of the energy functionals.\n   This implies in turn that psh functions are non-constant only on relatively small subsets",
  "9164b6c60b64ef76bb4b8260838d913b5cec28f2e8cc11af1f62b15bb923fbc6": "adapting to our setting classical arguments from the complex analytic case. In particular,\nwe prove the fundamental result that negligible sets are the same as pluripolar sets.\n  In what follows, X is of dimension n and irreducible. We fix an ample class ω ∈ Amp(X),\nand we assume that the envelope property holds for ω, see §5.2. As before, we write\nV = Vω = (ω n ) and MA(ϕ) := V −1 (ω + ddc ϕ)n for ϕ ∈ E 1 = E 1 (ω).\n13.1. Envelopes of lsc functions. Consider an arbitrary function ϕ : X an → R ∪ {+∞},\nand assume that ϕ is bounded below. By Lemma 5.17, the usc regularization\n                              P(ϕ)? = sup? {ψ ∈ PSH | ψ ≤ ϕ}\nof the ω-psh envelope P(ϕ) is either ω-psh and bounded, or satisfies P(ϕ)? ≡ +∞.\nTheorem 13.1. Pick any lsc function ϕ : X an → R ∪ {+∞}, and assume P(ϕ)? 6≡ +∞.\nThen\n                     P(ϕ)? = P(ϕ) = ϕ a.e. for MA(P(ϕ)? ).\n  In particular, the orthogonality property\n                             ˆ\n                                   (ϕ − P(ϕ)? ) MA(P(ϕ)? ) = 0                           (13.1)\n                                X an\nholds (compare [BFJ15, BGM20]).\nLemma 13.2. If N ⊂ X an is a negligible Borel set (see Definition 5.1), then µ(N ) = 0 for\nall measures of finite energy µ ∈ M1 .\n   This strengthens in particular Lemma 9.2, since pluripolar sets are negligible (Proposi-\ntion 5.3),\nProof. By Choquet’s lemma (see Corollary 12.22), there exists an increasing, uniformly\nbounded sequence (ϕm )∞                                          ?\n                           1 in PSH(ω) such that N ⊂ {ϕ < ϕ }, where ϕ := limm ϕm\npointwise. Recall that ϕ? ∈ PSH(ω), thanks to the standing assumption that the envelope\nproperty holds. On X div we have ϕ? = ϕ, by Theorem´5.6. Thus ´ϕm → ϕ? weakly in E 1 (and\nin fact strongly as well, by Theorem 12.5), and hence ϕm µ → ϕ? µ,  ´ by Proposition\n                                                                              ´      9.19.\nOn\n´ ?  the other hand, the   monotone convergence  theorem shows that   ϕ m µ →   ϕ µ. Thus\n  (ϕ − ϕ)µ = 0, which implies µ(N ) = 0.                                                \u0003\n\f             GLOBAL PLURIPOTENTIAL THEORY OVER A TRIVIALLY VALUED FIELD                     127\n\nProof of Theorem 13.1. Set ψ := P(ϕ)? and µ := MA(ψ). Assume first ϕ ∈ C0 (X), so that\nψ = P(ϕ) is continuous and ω-psh. Arguing as in the proof of [BGM20, Lemma 3.5], set\nf := ϕ − ψ ≥ 0, and observe that for t ∈ [0, 1],\n                                ϕt := ψ + tf = (1 − t) P(ϕ) + tϕ\nsatisfies P(ϕ) ≤ ϕt ≤ ϕ, and hence P(ϕt ) = P(ϕ). Thus E(ψ + tf ) = E(P(ϕ)) for t ∈ [0, 1],\nand Corollary 8.6 yields\n                         ˆ\n                                             d\n                           (ϕ − ψ) MA(ψ) =          E(ψ + tf ) = 0,\n                                             dt t=0\nand hence ϕ = ψ µ-a.e.\n   Now consider the general case. Since the Borel set {ψ > P(ϕ)} is negligible, Lemma 13.2\nshows that ψ = P(ϕ) µ-a.e. In particular, ψ ≤ ϕ µ-a.e., and it thus remains to show that µ\nputs no mass on the open set U := {ψ < ϕ}.\n   Since ϕ is lsc and X an is compact, there exists an increasing net (ϕj ) in C0 (X) that con-\nverges pointwise to ϕ. By Lemma 5.19, the increasing net ψj := P(ϕj ) converges pointwise\nto P(ϕ). By Theorem 5.6, we thus have ψj → ψ on X div , and Theorem 12.5 implies that\nµj := MA(ψj ) converges weakly to µ. By the first part of the proof, µj puts no mass on the\nopen set Uj := {ψj < ϕj }, and we want to take the limit and deduce that µ(U ) = 0; this\nwill conclude the proof. To do so, suppose µ(U ) > 0, and pick a point v ∈ U ∩ supp µ. Thus\nψ(v) < ϕ(v), so there exists j0 such that ψ(v) < ϕj (v) for j ≥ j0 . Set V := {ψ < ϕj0 }.\nThen V is open, v ∈ V and V ⊂ Uj for j ≥ j0 . Since v ∈ supp µ, we have µ(V ) > 0. As\nµj → µ weakly, we must have µj (V ) > 0 for j \u001d 0, which contradicts µj (Uj ) = 0.           \u0003\n\n13.2. The Bedford–Taylor capacity, reprise. Recall from §7.7 that we have set, for each\nBorel set E ⊂ X an ,\n                                     \u001aˆ                               \u001b\n            Cap(E) = Capω (E) := sup    MA(ψ) | ψ ∈ PSH, −1 ≤ ψ ≤ 0 .\n                                             E\n\nNote that 0 ≤ Cap(E) ≤ 1 for all Borel sets E ⊂ X an , and that Cap(X) = 1.\nProposition 13.3. The function Cap is a precapacity, i.e. it satisfies:\n                                E ⊂ E 0 =⇒ Cap(E) ≤ Cap(E 0 )                           (13.2)\nfor all Borel subsets E, E 0 , and\n                                                !\n                                       [",
  "6ef0dbe653c6c6a3e1b3f96c864805cce13d08f4e63b320be0da28ca0a0db8de": "                           3. A local theory of PSH functions\n   In this section, unless indicated otherwise, we assume that K is any completed NA field, X\nis a projective variety over K, and Y is an affine variety over K.\n\n3.1. Tropically convex functions. Let T :“ R Y t`8u. We make the convention that\nx ` p`8q “ `8 for any x P T, and 0 ¨ p`8q “ 0, a ¨ p`8q “ `8 for any a P Rą0 ,\na ¨ p`8q “ ´8 for any a P Ră0 . We equip T with the usual extended topology. Let U Ă Tk\nbe an open subset.\nDefinition 3.1.       (1) A Q-affine (resp. R-affine) function l on U is a real-valued continuous\n       function l : U Ñ R of the form\n                             ÿ\n                     lptq “       ai t i ` b  for any t “ pt1 , ¨ ¨ ¨ , tk q P U,\n                                 1ďiďk\n\f14                                                  LYUHUI WU\n\n          with a1 , ¨ ¨ ¨ , ak , b P Q (resp. a1 , ¨ ¨ ¨ , ak , b P R), such that for any t “ pt1 , ¨ ¨ ¨ , tk q P U\n          and for each 1 ď i ď k, we have ´8 ă ai ti ă `8. We use Aff Q pU q (resp. Aff R pU q)\n          to denote the space of Q-affine (resp. R-affine) functions on U .\n      (2) A Q-PL (resp. R-PL) function f on U is a real-valued continuous function f : U Ñ R\n          such that there exists a finite open cover tUα uαPI , and a finite collection of Q-affine\n          (resp. R-affine) functions tlα,i uiPIα for each α P I such that\n                                f pxq P tlα,i pxquαPI, iPIα       for any x P Uα .\n          We use PLQ pU q (resp. PLR pU q) to denote the space of Q-PL (resp. R-PL) functions\n          on U . When there is no ambiguity, we write PLpU q :“ PLQ pU q.\n      (3) A convex function f on U is a real-valued continuous function f : U Ñ R such that\n          for any x P U , there exists an open neighborhood V of x in U , C P R and l P Aff R pV q\n          such that\n                          upxq “ lpxq ` C,       and upx1 q ě lpx1 q for any x1 P V.\nRemark 3.2. Let x “ p8, yq P Tk1 ˆRk2 Ă Tk with 8 “ p`8, ¨ ¨ ¨ , `8q P Tk1 and k “ k1 `k2 .\nSuppose that f is a PL (resp. affine) function on an open subset of Tk containing x. Then, by\ndefinition, there exists a neighborhood U of x in Tk and f 1 P PLpppU qq such that ppU q Ă Rk2\nand f “ f 1 ˝ p on U , where p : Tk Ñ Tk2 denotes the projection map.                        ˛\nRemark 3.3. Here we give some non-examples of affine functions and PL functions.\n      (1) lpt1 , t2 q “ 2t1 ´ 3t2 is not an affine function in a neighborhood of p`8, `8q in T2\n          since 2 ¨ p`8q “ `8 and p´3q ¨ p`8q “ ´8.\n      (2) In our definition, a PL (resp. convex) function is always assumed to take values in R.\n          For example, f pxq “ x is not a PL (resp. convex) function on T1 since f p`8q “ `8.\n      (3) f pt1 , t2 q “ maxtt1 ´ t2 , 0u is not a PL function on T2 because it is not continuous\n          around p`8, `8q.\n                                                                                                                  ˛\nLemma 3.4.        (1) Let f P C 0 pU q. Suppose that f |U XRk is convex. Then, f P ConvpU q.\n  (2) Let tfi uiPI Ă ConvpU q be a finite class of convex functions. Then, maxtfi uiPI P\n      ConvpU q.\n  (3) Suppose that U is compact. Let f P ConvpTk q. Then, for any ϵ ą 0, there exists\n      g P Conv X PLpU q such that }f ´ g}C 0 pU q ă ϵ.\n  (4) For any f P PLpU q, there exists f ` , f ´ P TConv XPLpU q such that f “ f ` ´ f ´ .\nProof. Statement (1), (2), (3) are proven respectively in Proposition 3.10, Proposition 3.15\n(3), Theorem 5.14 of [APW26b]. Statement (4) is classical in convex analysis.             □\n\n     Now, let X be a projective variety over K.\nLemma 3.5 ([GM19, Theorem 1]). Let u be a function on X an . Then, u P PLpXq (after\nDefinition 2.1 in our paper) iff there exists a finite affine open cover tYi u1ďiďr of X, tropical-\nization maps Tropi : Yian Ñ Tki and fi P PLpTki q for each i, such that u “ fi ˝ Tropi on Yian .\n□\n     Therefore, we introduce the following definitions.\n\f                ON THE LOCAL THEORY OF NON-ARCHIMEDEAN PSH FUNCTIONS                           15\n\nDefinition 3.6. Let W be an open subset in X an , and u is a function on W . We say that u\nis a PL function on W if there exists a finite affine open cover tYi u1ďiďr of X, tropicalization\nmaps Tropi : Yian Ñ Tki and fi P PLpTropi pW X Yian qq for each i, such that u “ fi ˝ Tropi on\nW X Yian . We use PLpW q to denote the space of PL functions on W .\nDefinition 3.7. Let W be an open subset in X an , and u : W Ñ R be a function. We say that\nu is tropically convex if there exists an affine open subvariety Y Ă X, a tropicalization map\nTrop : Y an Ñ Tn and f P ConvpTroppW qq such that W Ă Y an , and u “ f ˝ Trop. We use\nTConvpW q to denote the space of tropically convex functions on W , and use TConv XPLpW q\nto denote the space of tropically convex PL functions on W .\n3.2. Local psh functions. In this subsection, we assume that X is a projective variety over\nK, and U Ă X an is an open subset.\nDefinition 3.8. Let u : U Ñ R Y t´8u be a function. We say that u is a psh function if\n    (1) u is generically finite and usc on U .\n    (2) For each x P U , there exists an open neighborhood Ux of x in U , and a decreasing\n         sequence of functions tui uiě1 Ă TConv XPLpUx q which converges pointwise to u on\n         Ux .\nWe say that u is locally bounded if for each x P U , there exists an open neighborhood Vx of x\nin U , such that u is bounded on Vx .\n   We use PSHpU q to denote the set of psh functions on U , and use PSH X L8   loc pU q to denote\nthe set of locally bounded psh functions on U .\nRemark 3.9. Let OU denote the structure sheaf of the Berkovich space U , i.e. the sheaf\nof analytic functions on U . For an open subset W Ă U and a function u on W , we say\nthat u is analytically tropically convex PL function if there exists g1 , ¨ ¨ ¨ , gk P OpW q and\nf P Conv X PLpTk q such that u “ f ˝ Trop, where Trop : W Ñ Tk is the tropicalization map\ndefined by p´ log |g1 |, ¨ ¨ ¨ , ´ log |gk |q.\n   Let x P U , and let V be a rational domain V of X an such that x P V Ă U . Then,\nthere exists an affine open subvariety Y Ă X with V Ă Y an . Moreover, for any p P OpV q,\nthere exists a sequence of polynomials tpi uiě1 Ă KrY s such that |pi | converges uniformly to\n|p|. On the other hand, consider the map ´Log : Rkě0 Ñ Tk defined by ´Logpt1 , ¨ ¨ ¨ , tk q :“\np´ log t1 , ¨ ¨ ¨ , ´ log tk q, and f P PLpTk q. With Remark 3.2, it’s not hard to show that f ˝\np´Logq is Lipschitz on any compact subset of Rkě0 . Combining these together, we obtain that\nfor any analytically tropically convex PL function u on V , there exists a sequence tui uiě1 Ă\nTConv XPLpV q converging locally uniformly to u on V .\n   Thus, the pointwise limit of any decreasing sequence of analytically tropically convex PL\nfunction on V 1 can be written locally as the pointwise limit of a decreasing sequence of tropi-\ncally convex PL function, and thereby is a psh function (after Definition 3.8) on V . This shows\nthat the definition of PSHpU q only depends on the analytic structure on U . In particular, it\ndoes not depend on the choice of the projective variety X containing U .                       ˛\nDefinition 3.10. Let ω P Z 1,1 pXq. A potential function of ω on U is a finite-valued PL\n                                                   1\nfunction g P PLpU q which can be written as g “ ´ m  log |s|ω ` λ, where m ě 1 such that\n                                          0\nmLpωq is an actual line bundle on X, s P H pU, mLpωq|U q is a nowhere vanishing section, and\nλ P Q.\n\f16                                              LYUHUI WU\n\nRemark 3.11.        (1) For any x P U , there exists an affine open neighborhood V of x in\n      X an and a nowhere vanishing section s P H 0 pV, L|V q. Therefore, ω admits a potential\n      g P PLpV q on U X V .\n  (2) Let g1 , g2 be potentials of ω on U . Then, g1 ´ g2 “ log |f | for some f P Oˆ pU q.  ˛\n                              1,1\nDefinition 3.12. Let ω P Zě0      pXq and let φ : X an Ñ R Y t´8u be a function. We say that\nφ is a locally ω-psh function if for each x P X an , there exists an open neighborhood U of x in\nX an and a potential g P PLpU q of ω such that φ ` g P PSHpU q. In particular, φ is generically\nfinite and usc on X an .\nLemma 3.13.        (1) Let tui uiPI Ă PSHpU q be a finite class of functions. Then, maxtui uiPI P\n      PSHpU q.\n  (2) Let tφi uiPI Ă LPSHω pXq be a finite class of functions. Then, maxtφi uiPI P LPSHω pXq.\nProof. The lemma follows from the observation that the supreme of any finite collection of\ntropically convex functions is tropically convex, which is an easy corollary of Lemma 3.4\n(2).                                                                                    □\nRemark 3.14. Let V Ă U Ă X an be open subsets. Let u P PSHpU q and v P PSHpV q. Define\nthe function u1 : U Ñ R Y t´8u by\n                       u1 “ maxtu, vu on V,           and        u1 “ u on U ∖ V.\nSet W :“ tx P V, upxq ă vpxqu, and assume that W Ă V . Then, u1 P PSHpU q. Moreover,\nif u P PSH X PLpU q and v P PSH X PLpV q, then u1 P PSH X PLpU q. To see this, we have\nu1 |V P PSHpV q by Lemma 3.13. On the other hand, since U is locally compact Hausdorff, for\nany x P U ∖ V , there exists an open neighborhood Ux of x in U such that Ux X W “ ∅. Then,\nby assumption, u1 |Ux “ u|Ux P PSHpUx q.                                                  ˛\n3.3. Fubini-Study functions. Let Y be an affine variety over K.\nDefinition 3.15.          (1) A function u on Y an is called a Fubini-Study function if there exists\n       f1 , ¨ ¨ ¨ , fk P KrY s, c1 , ¨ ¨ ¨ , ck P Qą0 and C1 , ¨ ¨ ¨ , Ck , λ P Q such that f1 , ¨ ¨ ¨ fk are\n       generators of KrY s, and u “ max1ďiďk tci log |fi | ` Ci , λu. We use FSpY an q to denote\n       the set of Fubini-Study functions on Y an .\n   (2) We say that a psh function v P PSHpY an q is of logarithmic growth if there exists\n       u P FSpY an q such that u ď v ` Op1q on Y an . We use PSHlog pY an q to denote the set of\n       psh functions of logarithmic growth on Y an .\n   (3) We say that a psh function of logarithmic growth v is regularizable if there exists a\n       decreasing function sequence tvi uiě1 Ă FSpY an q converging pointwise to v. We use\n       PSHlog         an\n               reg pY q to denote the set of regularizable psh functions of logarithmic growth on\n         an\n       Y .\nLemma 3.16. Let u P FSpY an q.\n  (1) For any v P FSpY an q, there exists C ą 0 such that u ď Cv ` Op1q.\n  (2) Suppose that S is another affine variety over K and π : Y Ñ S is a finite surjective\n      morphism. Then, for any w P FSpS an q, there exists C 1 ą 0 such that u ď C 1 pw ˝ π an q `\n      Op1q.\nProof. (1) Suppose that v :“řmaxtlog |z1 |, ¨ ¨ ¨ , log |zk |, 0u ` 1 P FSpY an\n                                       α",
  "fcd5dcafe19d130eb9b96c252801302db3f9aabbd192370259bae3e7a63c4a23": "                                          k dd uk :“       k pωk ` dd φk q.\n\n4.2. Local Bedford-Taylor theory.\nTheorem 4.2. For each open subset U Ă X an , there is a unique mixed Monge–Ampère oper-\nator\n                                                n\n                           pPSH X L8  loc pU qq     Ñ Radon` pU q\n                                pu1 , ¨ ¨ ¨ , un q ÞÑ ddc u1 ^ ¨ ¨ ¨ ^ ddc un\nsatisfying the following properties.\n    (1) It extends the local mixed Monge–Ampère operator on TConv XPLpU q.\n         Ź c that V Ź\n    (2) Suppose          Ă U Ă X an are open subsets and u1 , ¨ ¨ ¨ un P PSH X L8      loc pU q. Then,\n        p k dd uk q|V “ k ddc puk |V q.\n                     an              subset and u0 , u1 , ¨ ¨ ¨ , un Ă PSH X L8\n        Ź Uc Ă X be an open\n    (3) Let                                                                   loc pU q. Denote µ :“\n                                 1\n          k dd uk . Then, u0 P L pU, µq.\n    (4) Under the hypothesis of (3), suppose further that for each 0 ď k ď n, tujk ujě1 Ă\n        TConv XPLpU q is a decreasing function sequence converging pointwise to uk , and de-\n        note µj :“ k ddc ujk . Then, uj0 µj converges weakly to u0 µ on U .\n                    Ź\n\nProof. Let U Ă X an be an open subset, we say that u P PSHpU q is regularizable on U if there\nexists a decreasing sequence of tropically convex PL functions converging pointwise to u on U ,\nand we denote by PSHreg pU q the space of regularizable psh functions on U . Property (1) and\n(4) show that the mixed Monge–Ampère operator on PSHreg X L8 pU q is unique, and property\n(2) imply further that the mixed Monge–Ampère operator is unique on PSH X L8          loc pU q. It\nremains to prove the existence. It suffices to show that for each open subset U Ă X an , there\nexists a mixed Monge–Ampère operator on PSHreg X L8 pU q satisfying property (1) to (4) in\nthe statement.\n             1,1\n   Fix ω P Zě0   pXq such that c1 pLpωqq P AmppXq. Let U Ă X an open, and let u0 , u1 , ¨ ¨ ¨ , un P\nPSHreg X L8 pU q. Then, by Proposition 3.28 (1), for any x P U , there exists an open neigh-\nborhood Ux of x in U only depending on pU, xq, constants tCi u0ďkďn Ă Qą0 , tgi u0ďkďn Ă\n\f26                                                LYUHUI WU\n\nTConv XPLpUx q and tφk u0ďkďn Ă PSHω X L8 pXq such that for each 0 ď k ď n, gk is a\npotential of ω on Ux , and φk ` gk “ Ck u on Ux . We define the nonnegative Radon measure\non Ux by                                     ź\n                                               Ci q´1 ¨   pω ` ddc φk q\n                                                        Ź\n               µpUx ; u1 , ¨ ¨ ¨ , un q :“ p                            on Ux .\n                                           1ďkďn             1ďkďn\nThen,\n   (a) Proposition 4.1 (3) implies that µpUx ; u1 , ¨ ¨ ¨ , un q “ ddc u1 ^ ¨ ¨ ¨ ^ ddc un on Ux when\n       tuk u1ďkďn Ă TConv XPLpUx q.\n   (b) Theorem 2.22 (2) implies that u0 P L1 pUx , µpUx ; u1 , ¨ ¨ ¨ , un qq.\n   (c) Let tujk ujě1 Ă TConv XPLpUx q be a decreasing function sequence converging pointwise\n       to uk on Ux for each 0 ď k ď n. Then, after the proof of Proposition 3.28 (2), there\n       exists j0 P N and φjk P PSHω X L8 pXq for each 0 ď k ď n and j ě j0 such that,\n       φjk ` gk “ Ck u on Ux , and tφjk ujěj0 converges pointwise to φk on X an . Then, Theorem\n       2.22 (3) implies that uj0 µpUx ; uj1 , ¨ ¨ ¨ , ujn q converges weakly to u0 µpUx ; u1 , ¨ ¨ ¨ , un q on\n       Ux .\nCombining (a) and (c), we obtain that for any x, y P U ,\n                        µpUx ; u1 , ¨ ¨ ¨ , un q|Ux XUy “ µpUy ; u1 , ¨ ¨ ¨ , un q|Ux XUy .\nTherefore, we define the mixed Monge–Ampère measure for u1 , ¨ ¨ ¨ , un P PSHreg X L8 pU q by\n                 pddc u1 ^ ¨ ¨ ¨ ^ ddc un q|Ux “ µpUx ; u1 , ¨ ¨ ¨ , un q       for any x P U.\nThen, property (1), (3) and (4) follows from (a), (b) and (c) respectively. Property (2) follows\nfrom the locality of the mixed Monge–Ampère operator on TConv XPLpU q and property (1),\n(4).                                                                                          □\nRemark 4.3. Combining Proposition 4.1 (3) and Theorem 4.2 (1), we obtain that the mixed\nMonge–Ampère measures for bounded local psh functions are compatible with the mixed\nMonge–Ampère measures for bounded ω-psh functions defined in Theorem 2.22.            ˛\nRemark 4.4. Since the Monge–Ampère operator for PL functions is local, Theorem 4.2 (1)\nimplies that the definition of mixed Monge–Ampère operators for locally bounded psh functions\non U does not depend on the choices of X.                                                   ˛\nRemark 4.5. Let u1 , ¨ ¨ ¨ , un P PSH X L8  loc pU q. By Proposition 4.1 (2) and Theorem 4.2 (1),\nif u1 “ log |f | for some f P Oˆ pU q, then, ddc u1 ^ ¨ ¨ ¨ ^ ddc un “ 0 on U .                ˛\nRemark 4.6. Suppose that U Ă X an is an open subset and tui uiě1 Ă PSHpU q is a decreasing\nfunction sequence. Let u be the pointwise limit of tui uiě1 . It is not known to the author\nwhether in general, u P PSHpU q. This is because for x P U , the open neighborhood Ux,i on\nwhich ui is regularizable depends on i. However, u P PSHpU q when X satisfies the envelope\nproperty (see Corollary 4.18 (1)).                                                        ˛",
  "89d0992afffad46a10fc840aff477a4936d21d78f2589d043a54d5c9963d4c5d": "Theorem 4.11 (Locality for Monge–Ampère measures).\n  (1) Let U Ă X an be an open subset and u, v P PSH X L8\n                                                       loc pU q. Then,\n                       1tuąvu MApmaxtu, vuq “ 1tuąvu MApvq           on U.\n                1,1\n   (2) Let ω P Zě0  pXq and φ, ψ P LPSHω X L8 pXq. Then,\n                    1tφąψu MAω pmaxtφ, ψuq “ 1tφąψu MAω pφq           on X an .\nProof. This follows from the locality for Monge–Ampère measures for ω-psh functions (Theo-\nrem 2.23) and Proposition 3.28.                                                         □\n4.3. Global Properties of Monge–Ampère measures.\n                                       1,1\nProposition 4.12. Let ω1 ¨ ¨ ¨ , ωn P Zě0  pXq, and let φ1 , ¨ ¨ ¨ , φn P LPSHω X L8 pXq. Then,\n                        ż n                       ż\n                               Ź            c\n                                  pωk ` dd φk q “     ω1 ^ ¨ ¨ ¨ ^ ωn .\n                             X k“1                   X\n                            1,1                            ş\nIn particular, for any ω P Zě0  pXq and φ P LPSHω X L8 pXq, X MAω pφq “ degpω d q.\nLemma 4.13 (Partition of unity for finite open covers by PL functions). Let tUα uαPI be a\nfinite open cover of X an . Then, for each α P I, there exists ρα P PLpUα q such that\n         For each α P I, Supppρα q Ť Uα , and 0 ď ρα ď 1.\n     (1) ř\n     (2) αPI ρα “ 1 on X an .\nProof. After shrinking each Uα , we may assume that there exists a tropicalization map Trop : X an Ñ\nTPΣ and open subsets Vα for each α such that Trop´1 pVα q “ Uα (see Section 2.1.1). Since the\ncomposition of a PL function on TPΣ and Trop is a PL function on X an (see Lemma 3.5), it\nis enough to prove the partition of unity for a finite open cover tVα uαPI of the tropical toric\nvariety TPΣ .\n    We may take a simplicial polyhedral complex Π whose support equal to TPΣ having the\nfollowing property: there exists a map i : V Ñ I such that Πv Ă Vipvq for each v P V . Here, V\ndenotes the set of vertices of Π, and Πv denotes the star Πv of v.\n    For each v P V , define the function χv : V Ñ R by χv pvq “ 1 and χv pv 1 q “ 0 for any\nv 1 ‰ v P V . Define the facewise affine function ρv on Π as the linear extension of the χv to\nTPΣ . More precisely, let σ P Π be a simplicial polyhedron. If σ is a simplex, then ρv equals\nto the unique affine function on σ whose restriction to the vertices of σ equals χv . Otherwise,\nthere exists a canonical projection p : σ Ñ τ with τ P Π a simplex, and we have ρv “ ρv ˝ p on\nσ.\n    Note that we have řvPV ρv “ 1 on TPΣ , and Supppρv q “ Πv for each v P V . For each\n                       ř\nα P I, we define ρα :“ vPi´1 pαq ρv . Then, tρα uαPI gives a partition of unity subordinate to\nthe cover tVα uαPI .                                                                          □\n\f28                                               LYUHUI WU\n\nLemma 4.14. Let U Ă X an be an open subset. Let f1 , ¨ ¨ ¨ , fn P PLpU q, and let g P PLpU q\nsuch that Supppgq Ť U . Then,\n            ż                                    ż\n                   c       c               c\n               g dd f1 ^ dd f2 ^ ¨ ¨ ¨ ^ dd fn “   f1 ddc g ^ ddc f2 ^ ¨ ¨ ¨ ^ ddc fn\n                U                                              U\n\nProof. Let fr1 , ¨ ¨ ¨ , frn P PLpXq be extensions of f1 , ¨ ¨ ¨ , fn . Since Supppgq Ť pU q, we may\nextend g to gr P PLpXq by setting gr ” 0 on X an ∖ U . By Remark 4.5, we have\n            ż                                       ż\n                         c       c            c\n                  g dd f1 ^ dd f2 ^ ¨ ¨ ¨ ^ dd fn “    gr ddc fr1 ^ ddc fr2 ^ ¨ ¨ ¨ ^ ddc frn ,\n              U                                             X\n\nand\n            ż                                              ż\n                    f1 ddc g ^ ddc f2 ^ ¨ ¨ ¨ ^ ddc fn “           fr1 ddc gr ^ ddc fr2 ^ ¨ ¨ ¨ ^ ddc frn .\n              U                                             X\n\nThen, the lemma follows from the global integration-by-parts for PL functions ([BFJ15, Propo-\nsition 2.20]).                                                                             □\n\nProof of Proposition 4.12. Denote T “ pω2 ` ddc ψ2 q ^ ¨ ¨ ¨ ^ pωn ` ddc ψn q. We show that\n                           ż               ż\n                                 c\n(4.1)                        1 dd φ1 ^ T “    φ1 pddc 1q ^ T “ 0\n                                    X                   X\n\nGranted this equation, repeated application yields\n        ż n                    ż        ˆ n               ˙          ż\n             Ź          c                 Ź          c\n               pωk ` dd φk q “    ω1 ^       pωk ` dd φk q “ ¨ ¨ ¨ “   ω1 ^ ¨ ¨ ¨ ω n .\n           X k“1                        X         k“2                                       X\n\nTherefore, the proposition is proved.\n  Now we prove Equation 4.1. Let tUα uαPI be a finite open cover of X such that, for each\nα P I and 0 ď k ď n, there exists a potential gk,α P TConv XPLpUα q of ωk , and a decreasing\nfunction sequence tuik,α uiě1 Ă PSHpUα q satisfying uik,α Ñ uk,α on Uα , where uk,α :“ φk `gk,α P\nPSHpUα q. For each α P I and i ě 1, denote Tαi :“ nk“2 ddc ujk,α . Let pρα q P PL X Cc0 pUα q be\n                                                         Ź\n\na partition of unity of tUα uαPI . Then,\nż                  ÿż\n        c\n   1 dd φ1 ^ T “            ρα pddc u1,α ´ ddc g1,α q ^ T\n X                      αPI Uα\n                        ÿˆ          ż                              ż                         ˙\n                    “         lim       ρα ddc ui1,α ^ Tαi ´              ρα dd g1,α ^ Tαi\n                                                                                c\n                                                                                                   pTheorem 4.2 p4qq\n                              iÑ`8 Uα                                Uα\n                        αPI\n                        ÿˆ          ż                              ż                         ˙\n                    “         lim       ui1,α ddc ρα ^ Tαi ´              g1,α dd ρα ^ Tαi\n                                                                                    c\n                                                                                                   pLemma 4.14q .\n                              iÑ`8 Uα                                Uα\n                        αPI\n\n   By Lemma 3.4 (4), for each α P I, there exists ρ`    ´\n                                                   α , ρα P TConv XP LpUα q such that ρα “\nρ`    ´                                                    c      i\n α ´ ρα . On the other hand, Remark 4.5 implies that dd ρα ^ Tα “ 0 on Uα ∖ Supppρα q,\n                                          1             0\nand Lemma 4.13 implies that there exists ρα P PL X Cc pUα q such that ρ1α ” 1 on Supppρα q.\n\f                    ON THE LOCAL THEORY OF NON-ARCHIMEDEAN PSH FUNCTIONS                                     29\n\nHence,\n           ż                                    ż\n                   ui1,α ddc ρα ^ Tαi “            ρ1α ui1,α ddc ρ`      c ´    i\n                                                            `                ˘\n     lim                                lim                       α ´ dd ρα ^ Tα\n    iÑ`8 Uα                            iÑ`8 Uα\n                                       ż\n                                           ρ1α u1,α ddc ρ`         c ´\n                                                    `                  ˘\n                                     “                      α ´ dd ρα ^ T      pTheorem 4.2 p4qq\n                                        Uα\n                                       ż\n                                     “     u1,α ddc ρα ^ T.\n                                          Uα\nCombining the above formulas, we have\n                    ż                 ÿż\n                           c\n                       1 dd φ1 ^ T “                            pu1,α ´ g1,α q ddc ρα ^ T\n                            X                       αPI Uα\n                                                    ż\n                                               “            φ1 ddc 1 ^ T “ 0.\n                                                        X\nTherefore, Equation 4.1 is proved.                                                                           □\nTheorem 4.15 (Comparison Principle). Let φ, ψ P LPSHω X L8 pXq. We have\n                        ż                  ż\n                               MAω pψq ď          MAω pφq\n                                     tφăψu                       tφăψu\n\nProof. By Lemma 3.13, for any ϵ ą 0, maxtφ, ψ ´ ϵu P LPSHω X L8 pXq. Then,\n                  ż\n             d\n        degpω q “    MAω pmaxtφ, ψ ´ ϵuq                          pProposition 4.12q\n                   X\n           ż                             ż\n     ě         MAω pmaxtφ, ψ ´ ϵuq `          MAω pmaxtφ, ψ ´ ϵuq\n         tφăψ´ϵu                                    tφąψ´ϵu\n               ż                     ż\n     “               MAω pψq `                MAω pφq                                       pTheorem 4.11q\n         tφăψ´ϵu                 tφąψ´ϵu\n               ż                                        ż\n                                          d\n     “               MAω pψq ` degpω q ´                       MAω pφq\n         tφăψ´ϵu                                tφďψ´ϵu\n                        ş                           ş\nTherefore, we have       tφăψ´ϵu MAω pψq ď              tφďψ´ϵu MAω pφq.    The proof is completed by letting\nϵ Ñ 0.                                                                                                     □\n                                                                               1,1\nTheorem 4.16 (Domination Principle). Assume that X is irreducible. Let ω P Zě0     pXq such\nthat c1 pLpωqq P AmppXq and PSHω pXq satisfies the envelope property. Let φ, ψ P LPSHω X\nL8 pXq. Suppose that φ ď ψ almost everywhere on SupppMAω pψqq. Then φ ď ψ on X.\nProof. By Proposition 3.29, it is enough to prove that φpxq ď ψpxq for any x P X div . We\nassume that degpω d q “ 1. For any v P LPSHω X L8 pX an q, denote ωv :“ ω ` ddc v. Let µ “ δx\nbe the Dirac mass measure supported on txu. Then by [BFJ15], there exists u P C 0 XPSHω pXq\nsuch that MAω puq “ pωu qd “ µ. Since both u and φ are bounded, after adding a constant to\nu, we may assume that u ă φ.\n   For any ϵ ą 0, denote φϵ :“ p1 ´ ϵqφ ` ϵu P LPSHω X L8 pXq. Then, MAω pφϵ q “ pp1 ´\nϵqωφ ` ϵωu qd “ dj“0 pp1 ´ ϵqωφ qj ^ pϵωu qd´j ě ϵd ω d “ ϵd µ. Therefore, MAω pφϵ qptxuq ą 0.\n               ř\n\f30                                       LYUHUI WU\n\n  That u ă φ implies φϵ ă φ on X an . Then, by assumption, φϵ ă φ ď ψ on SupppMAω pψqq.\nBy comparison principle (Theorem 4.15) and Proposition 4.12, we have\n                         ż                  ż\n                    d\n              degpω q “         MAω pψq ď          MAω pφϵ q ď degpω d q\n                           tφϵ ăψu             tφϵ ăψu\n             ş\nThis implies tφϵ ăψu MAω pφϵ q “ degpω d q, and hence x P tφϵ ă ψu. Now by letting ϵ Ñ 0`,\nwe conclude that φpxq ď ψpxq.                                                           □\n4.4. Comparison between two notions of ω-psh functions.\n                         1,1\nTheorem 4.17. Let ω P Zě0    pXq. Assume that PSHω pXq satisfies the envelope property.\nThen, PSHω pXq “ LPSHω pXq.\nProof. Since PSHω pXq satisfies the envelope property, [BJ22, Remark 5.15] implies that each\nconnected component of X is irreducible. Therefore, we may assume that X is irreducible. Let\n       1,1\nθ P Zě0    pXq such that c1 pLpθqq P AmppXq. Note that for any function φ : X an Ñ R Y t´8u,\nφ P PSHω pXq (resp. LPSHω pXq) iff φ P PSHω`ϵθ pXq (resp. LPSHω`ϵθ pXq) for each ϵ ą 0,\nand c1 pLpω ` ϵθqq P AmppXq for any ϵ ą 0. Therefore, we may henceforth assume that\nc1 pLpωqq P AmppXq.\n    By Corollary 3.19, we have PSHω pXq Ă LPSHω pXq. Thus, we only need to prove the\nreverse direction. Let φ P LPSHω pXq, our aim is to show that φ P PSHω pXq. To show this,\nit is enough to show that suptφ, M u P PSHω pXq for any M P R (Theorem 2.12). Therefore,\nwe assume henceforth that φ is bounded.\n    Since φ is usc on X, we may choose a decreasing sequence of functions tfi uiě1 Ă C 0 pXq\nsuch that fi converges pointwise to φ. For each i ě 1, recall that the ω-psh envelope of fi is\ndefined to be\n                               Pω pfi q :“ suptψ P PSHω pXq | ψ ď f u.\nSince PSHω pXq satisfies the envelope property, Lemma 2.20 implies that Pω pfi q P PSHω X\nC 0 pXq. Furthermore, the orthogonality property for PSHω pXq (Theorem 13.1 in [BJ22])\nimplies that for each i ě 1\n                            SupppMAω pPω pfi qqq Ă tfi “ Pω pfi qu.\nHence, φ ď fi “ Pω pfi q on SupppMAω pPω pfi qqq. By domination principle (Theorem 4.16),\nwe have φ ď Pω pfi q on X an . Thus, tPω pfi quiě1 Ă PSHω X C 0 pXq is a decreasing sequence\nconverging pointwise to φ. Therefore, by Theorem 2.12, φ P PSHω pXq.                      □\nCorollary 4.18. Let U Ă X an be an open subset. Suppose that X satisfies the envelope\nproperty over K. Then,",
  "9ed3f20282976fc38e35582716b216684336bf500bd87173777e8224c582b9a8": "Proposition 4.19. Suppose that K is a discretely valued or trivially valued NA field of\nequicharacteristic 0, and Y is a smooth affine variety over K. Then, PSHlog pY an q “ PSHlog   an\n                                                                                         reg pY q.\n\nProof. As explained in the proof of Theorem 3.31, Hironaka’s theorem and Lemma 3.32 implies\nthat there exists a smooth projective compactification X of Y over K, a very ample line bundle\n                                                                    1,1\nL on X with s P H 0 pX, Lq satisfying Y “ X ∖ Zpsq. Let θ P Zą0         pXq such that L “ Lpθq,\nand let | ¨ |θ be a Fubini-Study metric on L. Then, by Proposition 3.17 (1), g :“ ´ log |s|θ\nis a Fubini-Study function on Y an . Let u P PSHlog pY an q. By Lemma 3.16, there exists\nA ą 0 such that u ď Ag ` Op1q. Fix c ą 1. Define the function φ : X an Ñ R Y t´8u\nby φ “ u ´ cAg on Y an and φ “ ´8 on X an ∖ Y an . Then, Lemma 3.25 (1) implies that\nφ P LPSHcAθ pXq. Recall that X satisfies the envelope property over K (Theorem 2.19). Then,\n                                                            1,1\nTheorem 4.17 implies that φ P PSHcAθ pXq. Since cAθ P Zą0       pXq, Corollary 3.18 implies that\n                     log  an\nu “ φ ` cAg P PSHreg pY q.                                                                    □\n\n                                      5. Runge domains\n  In this section, In this section, unless indicated otherwise, we assume that K is a discretely",
  "2413512b2e94bdf20b8e74b21f5174bc0b24cd98d575cfbf02c2ed0fb9f59baf": "Thus, we obtain that Nπ pui q|intpPr q P PSH X PLpintpPr qq, and statement (1) is proved.\n   For statement (2), for each r ě 1, tui uiě1 converges uniformly to u on Er by Dini’s theorem.\nThen, Lemma 6.10 implies that }Nπ pui q ´ Nπ puj q}C 0 pPr q ď degpπq }ui ´ uj }C 0 pEr q . Therefore,\ntNπ pui quiě1 converges uniformly to Nπ puq on Pr , and statement (2) follows. Statement (3)\nfollows from the fact that the norm functor for line bundles, and thereby the norm functor for\nmodel metrics commutes with base changes (see [BE21, Theorem A.21]).                                □\n\n6.3.2. Norms under finite surjective morphisms with smooth targets.\nProposition 6.12. Let K be a discretely valued or trivially valued NA field of equicharacter-\nistic 0 such that K admits a countable dense subfield. Let Y be an irreducible affine variety\n     5More precisely, there exists a model pX , Mq representing ϕ , a model T of T , and a proper flat morphism\n                                                                i\nX Ñ T extending τ such that pT , Nτ pMqq represents Nτ pϕi q.\n\f                  ON THE LOCAL THEORY OF NON-ARCHIMEDEAN PSH FUNCTIONS                                   43\n\nover K with dim Y “ n. Let S be an affine open subvariety of AnK . Let π : Y Ñ S be a finite\nsurjective morphism. Then, there exists a map\n                                          Y an ÝÑ Zą0\n                                             y ÞÝÑ multy pπq\nsuch that\n   (1) There exists an affine open subvariety W of S such that π is flat over W , and multy pπq “\n       multy pπ|π´1 pW q q for any y P π ´1 pW q, where multy pπ|π´1 pW q q is the multiplicity at y of\n       the finite flat surjective morphism π|π´1 pW q : π ´1 pW q Ñ W defined by Equation 6.1.\n                              log\n   (2) For any u P WPSH\n                     ř            pY an q, we have Nπ puq P PSHlog   an\n                                                               reg pS q, with\n       Nπ puqpsq :“ yPπ´1 psq multy pπqupyq.\nProof. Step 1. We define multy pπq for each y P Y an . Since char K “ 0 and being unramified\nis an open condition, these together with the generic flatness ([Sta26, Proposition 29.28.1])\nimply that there exists an affine open subvariety W Ă S such that π is flat and unramified over\nW . Then, π is étale and in particular smooth over W ([Sta26, Lemma 29.37.5 and Lemma\n29.37.15]). Thus, U :“ π ´1 pW q is a smooth affine variety over K.\n   Denote by πU “ π|U : U Ñ W the restriction of π on U . By assumption, πU is a finite\nflat surjective morphism. For any y P U an , define multy pπq :“ multy pπU q, where multy pπU q\nis the multiplicity of πU at y defined by Equation 6.1.\n   Now, we define multz pπq for z P Z an , where Z :“ Y ∖ U . Let s “ πpzq P S an , and let\nK :“ Hpsq denote the completed residue field of s. Let πK : YK Ñ SK be the base change of π to\nK, and let rK{K denote the restriction maps on Berkovich spaces induced by the base change\nK{K. Then, there exists an K-rational point s1 P SK          an such that r          1\n                                                                               K{K ps q “ s. Moreover,\n                                           an        an\nit is not hard to see that rK{K : YK Ñ Y induces a homeomorphism from pπK                    an q´1 ps1 q to\n\npπ an q´1 psq.\n   Recall that SK is an affine open subvariety of AnK . Since WK is Zariski open dense in SK , we\nmay take an affine line Cs in SK Ă AnK passing s1 such that Cs is contained in WK generically.\nLet t1 , ¨ ¨ ¨ , tn´1 be linear functions on SK Ă AnK such that KrCs s – KrSs{pt1 , ¨ ¨ ¨ , tn´1 q. Con-\nsider the scheme theoretical preimage Cs ˆSK YK . Then, Krull’s principal ideal theorem implies\nthat each irreducible component of Cs ˆSK YK “ Spec KrY s{pt1 , ¨ ¨ ¨ , tn´1 q is of dimension at\nleast 1. On the other hand, since π is finite, dimpCs ˆSK YK q ď 1. This implies that Cs ˆSK YK\nis a scheme of equidimension 1.\n   Let Cs :“ πK     ´1\n                       pCs q, be the reduction of Cs ˆSK YK . Let p : Csν Ñ Cs be the normalization\nmap, and denote q “ pπK q ˝ p : Csν Ñ Cs . By construction, Cs is a variety of equidimension 1,\nand q is a finite surjective morphism. Since both Csν and Cs are smooth, the miracle flatness\n([Vak25, 26.2.11]) implies that q is flat.\n   Consider multx pqq, the multiplicity of the finite flat surjective morphism q at x defined by\nEquation 6.1 for x P pCsν qan . Let z 1 be the unique point in pπK an q´1 ps1 q such that r        1\n                                                                                            K{K pz q “ s .\n                                                                                                           1\n\nThen, z 1 P Csan “ pπK   an q´1 pC an q. Now, we define\n                                   s\n                                                        ÿ\n                                        multz pπq :“      multx1 pqq.\n                                                  x1 Pp´1 pz 1 q\n\n   We would like to say more about multx pqq before we start the next step. Since πK is\nétale over WK and Cs is a smooth variety over K, we obtain that pCs X WK q ˆSK YK is a\nsmooth scheme over K. In particular, pCs X WK q ˆSK YK is reduced, and hence the reduction\n\f44                                              LYUHUI WU\n\nmorphism Cs X UK “ πK      ´1\n                              pCs X WK q Ñ pCs X WK q ˆSK YK is an isomorphism. This implies\nthat Cs X UK is smooth over K, and thereby p is an isomorphism over Cs X UK . It also implies\nthat πK |pCs XUK q : Cs X UK Ñ Cs X WK is a finite flat surjective morphism. 6 Moreover, for each\nt P pCs X WK qan , we have\n        HSK ptq ˆSK YK “ HCs ptq ˆCs pCs ˆSK YK q – HCs ptq ˆCs Cs – HCs ptq ˆCs Csν ,\nwhere HSK ptq “ HCs ptq denote the completed residue field at t. In particular, HSK ptq ˆSK\nYK and HCs ptq ˆCs Csν admit isomorphic decompositions as products of local finite algebras,\n                   ´1\nindexed by fibres πK  ptq “ q´1 ptq. Thus, for each x P p´1 pCs X UK qan , we have\n(6.3)                    multx pqq “ multppxq pπK |Cs XUK q “ multppxq pπK |UK q.\nHere, multppxq pπK |pCs XUK q q and multppxq pπK |UK q denote the multiplicity at ppxq of the finite\nflat surjective morphisms πK |pCs XUK q : Cs X UK Ñ Cs X WK and πK |UK : UK Ñ WK respectively.\nCombining this with Lemma 6.10, we obtain that\n                                ÿ                      ÿ\n                degpqq “             multx pqq “              multy pπK |U q “ degpπq,\n                            xPpqan q´1 ptq           yPpπ an q´1 ptq\n\nwhere t P pCs X W qan .\n   Step 2. Fix u PřWPSHlog pY an q, and we would like to show that Nπ puq P PSHlog            an\n                                                                                        reg pS q,\nwhere Nπ puqpsq :“ yPπ´1 psq multy pπqupyq with multy pπq defined in Step 1. To emphasize the\nrole of π, we use the notation N pπ; uq :“ Nπ puq interchangeably in the rest of the proof.\n   Since U is smooth, Proposition 6.2 (2) implies that u|U P PSHlogreg pU\n                                                                          an q. Since π| : U Ñ\n                                                                                        U\nW is a finite flat surjective morphism, Proposition 6.11 implies that\n                             Nπ puq|W an “ N pπ|U ; u|U an q P PSHlog\n                                                                  reg pW\n                                                                         an\n                                                                            q.\n  Fix g P FSpS an q. By Lemma 3.16 (2), there exists C ą 0 such that u ď Cpg ˝ π an q ` Op1q.\nThen, by Lemma 6.10, we have\n Nπ puq|W an “ N pπ|U ; u|U an q ď C ¨ N pπ|U ; pg ˝ π an q|U an q ` Op1q “ C degpπq ¨ g|W an ` Op1q.\nTherefore, Theorem 3.31 implies that there exists v P PSHlog       an\n                                                             reg pS q such that v|W an “ Nπ puq|W an .\n   Step 3. It remains to show that Nπ puqpsq “ vpsq for any s P pS ∖ W qan . Fix s P pS ∖ W qan\nand denote K :“ HS psq. Let s1 P SK     an be the K-rational point and C Ă S be the curve\n                                                                             s     K\npassing s1 chosen in Step 1 to define multz pπq for z P π ´1 psq. For any function f on S an (resp.\nY an ), denote by fK :“ f ˝ rK{K .\n   Then, we have vK P PSHlog       an                               log  an\n                             reg pSK q, and thereby vK |Cs P PSHreg pCs q. By Proposition 6.11\n(3), we have\n(6.4)        vK |WKan “ pNπ puqK q |WKan “ N pπ|U ; u|U an q ˝ rK{K “ N pπK |UK ; puK q|U an q .\n   Now, we consider uK |Cs P WPSHlog pCsan q. Let µ : Yr Ñ Y be a proper birational morphism\nsuch that u ˝ µan P PSHlog pYr an q. Let Crs Ă YrK be the proper transform of Cs under µK . Then,\nthere exists a proper birational morphism r : Csν Ñ Crs such that p “ µK ˝ r. By definition,\n                        ÿ                           ÿ\n(6.5)    Nπ puqpsq “          multz pπq upzq “            multx1 pqq uK px1 q “ N pq; uK ˝ pqps1 q,\n                         zPπ ´1 psq                 x1 Pq´1 ps1 q\n\n     6We remind the readers that C ˆ K might not be reduced, and therefore π | : C Ñ C might not be\n                                  s S                                       K Cs  s   s\nflat.\n\f                 ON THE LOCAL THEORY OF NON-ARCHIMEDEAN PSH FUNCTIONS                                 45\n\nwhere N pq; uK ˝ pq is the norm under the finite flat surjective morphism q “ pπK q ˝ p : Csν Ñ Cs .\nNote that pu ˝ µan qK P PSHlog pYrKan q, and thereby uK ˝ p “ pu ˝ µan qK ˝ r P PSHlog ppCsν qan q.\nSince Csν is an affine smooth curve, we have uK ˝p P PSHlog        ν an\n                                                            reg ppCs q q by Proposition 4.19. Then,\nProposition 6.11 implies that N pq; uK ˝ pq P PSHlog        an\n                                                      reg pCs q. On the other hand, recall that p\ninduces an isomorphism from p pCs X UK q to Cs X UK . Equation 6.3 implies that for any\n                                  ´1\n\nt P pCs X WK qan , we have\n(6.6)                 ÿ                           ÿ\nN pq; uK ˝pqptq “         multx pqq uK pppxqq “          multy pπK |UK q uK pyq “ N pπK |UK ; uK |U an q.\n                  xPq´1 ptq                           ´1\n                                                   yPπK  ptq\n\n   In summary, we obtain that vK |Cs P PSHlog      an                        log    an\n                                            reg pCs q and N pq; uK ˝ pq P PSHreg pCs q satisfying\n                                                                                  1\nvK |Cs XW “ N pq; uK ˝ pq|Cs XW . Moreover, we have Nπ puqpsq “ N pq; uK ˝ pqps q. Since Cs is\na smooth curve over the complete NA field K “ HS psq, it follows from Lemma 6.13 vK |Cs “\nN pq; uK ˝ pq on Csan . Combining these, we obtain that vpsq “ vK ps1 q “ N pq; uK ˝ pqps1 q “\nNπ puqpsq. This shows that Nπ puq “ v P PSHlog       an\n                                              reg pS q and finishes the proof.                 □\nLemma 6.13. Let F be any complete NA field, and C be a smooth algebraic curve over F .\nLet z P C an be a closed point. Then, for any u P PSHpC an q, we have\n                                      upzq “      lim sup         upxq\n                                               xÑz, xPC an ∖tzu\n\nProof. Note that r : pC p qan Ñ C an is a surjective continuous map, and u ˝ r P PSHppC p qan q,\n                       F                                                                 F\nwhere F denotes the completion of the algebraic closure of F . Therefore, it is enough to prove\n       p\nthe lemma when F is algebraically closed. When F is trivially valued, the lemma is proven\nin Proposition 3.29 (1). Thus, we may assume that F is nontrivially valued and algebraically\nclosed. In this setting, we say that a function f on an open subset W is subharmonic if it\nis subharmonic on W under the definition of Thuillier ([Thu05, Definition 3.1.5], [Wan19b,\nDefinition 3.1.5]). Let tWα uαPI be an open cover of C an such that for each α P I, there exists a\ndecreasing function sequence tuα,i uiě1 P TConv XPLpWα q converging pointwise to u|Wα . Since\nMApuα,i q “ ddc uα,i ě 0, [Wan19a, Theorem 2] implies that uα,i is subharmonic on Wα . Then,\n[Thu05, Proposition 3.1.8] implies that u|Wα is subharmonic. Therefore, u is subharmonic\non C an , and the lemma follows from [Wan19b, Lemma 3.1.33] (see also [BR10, Proposition\n8.11]).                                                                                         □\n6.4.",
  "691df9c820eaec929f098e9fb256d3943f5ca34f6c66e451609c7d633c0de76e": "Theorem 7.1. Let K be a discretely valued or trivially valued non-archimedean field of\nequicharacteristic 0 and X be a geometrically unibranch projective variety over K, then X\nsatisfies the envelope property over K.\nRemark 7.2. Since any normal scheme is geometrically unibranch ([Sta26, Lemma 28.16.2]),\nevery projective normal variety satisfies the envelope property over K.               ˛\nProof. By [BJ22, Lemma 5.9], it is enough to prove that PSHω pXq satisfies the envelope\n                         1,1\nproperty for any ω P Zě0     pXq with c1 pLpωqq P AmppXq.\n   We first prove the theorem in the case when K admits a countable dense subfield. Let\ntφi uiPI Ă PSHω pXq be a class of functions. Let π : X    r Ñ X be a resolution of singularities,\nand denote φ              an\n              ri :“ φi ˝ π P PSHπ˚ ω pXq.  r By Theorem 2.19, φ                 ri q‹ P PSHπ˚ ω pXq.\n                                                                   r :“ psupiPI φ                 r\nSince X is geometrically unibranch, every geometric fibre of π is connected ([Gro61a, Corollary\n4.3.7]). Then, by Proposition 2.24, there exists a usc function φ on X an such that φ     r “ φ ˝ π an\n                                                                                        div\nand φ is the minimum usc extension of φ|X div . On the other hand, for any x P X , Theorem\n2.16 implies that φpxq “ φpxq  r              ri pxq “ supiPI φi pxq. Therefore, φ “ psupiPI φi q‹ .\n                                     “ supiPI φ\nNow, by definition, φ P WPSHω pXq, and Theorem 6.5 implies that φ P WPSHω pXq “\nPSHω pXq. Therefore, the theorem is proved when K admits a countable dense subfield.\n   Now we consider K without the cardinality restriction. By Lemma 2.20, it is enough to\nshow that Pω pf q P C 0 pX an q for each f P PLpXq. Since Y is of finite type over K, there exists\na countable subfield F1 Ă K such that X, ω and f is defined over F1 . More precisely, let K1\nbe the completion of F1 . Denote by pXK1 qan the Berkovich analytification of X over K1 , and\ndenote by rK{K1 : X an “ pXK qan Ñ pXK1 qan the morphism induced by the base change K{K1 .\n                               1,1\nThen, there exists ωK1 P Zě0       pXK1 q and fK1 P PLppXK1 qan q such that ω “ ωK1 ˝ rK{K1 and\nf “ fK1 ˝ rK{K1 .\n   Consider the ωK1 -psh envelope ϕK1 :“ PωK1 pfK1 q on pXK1 qan . Since we have already\nshown that PSHωK1 ppXK1 qan q satisfies the envelope property, Lemma 2.20 implies that ϕK1 P\nC 0 ppXK1 qan q. Now set ϕK :“ PωK1 pfK1 q ˝ rK1 P C 0 pX an q, and we claim that Pω pf q “ ϕK . By\n\f52                                          LYUHUI WU\n\n[BJ22, Lemma 5.19], it is enough to show that ψ ď ϕ for each ψ P PLpXq. There exists a\ncountable field F2 such that F1 Ă F2 Ă K and ψ is defined over F2 . Let K2 be the completion\nof F2 , and ψK2 P PSHωK2 X PLppXK2 qan q such that ψK2 “ ψ ˝ rK2 . Here, ωK2 , fK2 , ϕK2 denote\nthe pullback of ωK1 , fK1 , ϕK1 via the morphism rK2 {K1 : pXK2 qan Ñ pXK1 qan induced by the\nbase change K2 {K1 . The orthogonality property over K1 implies that\n                    SupppMAωK1 pϕK1 qq Ă tfK1 “ ϕK1 u         on pXK1 qan .\nNote that\n                  prK2 ,K1 q˚ pMAωK2 pϕK2 qq “ MAωK1 pϕK1 q     on pXK1 qan .\nTherefore, on       on pXK2 qan , we have\n                       ´1                              ´1\n SupppMAωK2 pϕK2 qq Ă rK 2 {K1\n                               pSupppMAωK1 pϕK1 qqq “ rK2 {K1\n                                                              ptfK1 “ ϕK1 uq “ tfK2 “ ϕK2 u.\nThis implies that ψK2 ď fK2 “ ϕK2 on SupppMAωK2 pϕK2 qq. Since PSHωK2 ppXK2 qan q satisfies\nthe envelope property, the domination principle (Theorem 4.16 implies that ψK2 ď ϕK2 on\npXK2 qan . This proves that ψ ď ϕK on X an , and Pω pf q “ ϕK P C 0 pX an q. Hence, the theorem\nis proved.                                                                                    □\n\n            Appendix A. PSH functions d’après Chambert-Loir–Ducros\n   In this appendix, we assume that K is a discretely valued or trivially valued NA field. Let\nY be an affine variety over K, and let U Ă Y an be an open subset. Following [CLD25], we say\nthat a function u on U is smooth if for any x P U , there exists an open neighborhood Ux of x\nin U , a tropicalization map Trop : Y an Ñ Tk , an open subset W Ă Rk and f P C 8 pW q such\nthat TroppUx q Ă W Ă Rk , and u “ f ˝ Trop on Ux . We say that u is a smooth convex function\nif moreover, there exists a polyhedral structure Π on the tropical variety TroppY an q such that",
  "309dcfe51944e02b86cd08a3e2dba736974f98a5c468deb524169f76dea30e78": "Proposition 8.7.2. — Soit (Tk ) une suite de courants positifs fermés qui converge vers\nun courant positif fermé T . Soit (uk0 ), (uk1 ), . . . , (ukq ) des suites de fonctions continues\nsur X qui convergent localement uniformément vers des fonctions u0 , u1 , . . . , uq sur X.\nOn suppose que pour tout j ∈ {1, . . . , q} et tout k, la fonction ukj est psh. Alors, la suite\nde courants\n                            uk0 d′ d′′ (uk1 ) ∧ · · · ∧ d′ d′′ (uqq ) ∧ Tk\nconverge vers le courant\n                                      u0 d′ d′′ (u1 ) ∧ · · · ∧ d′ d′′ (uq ) ∧ T.\nDémonstration. — On raisonne par récurrence sur q. Pour q = 0, l’assertion résulte du\nlemme 8.5.1. Supposons q ⩾ 1 et l’assertion démontrée pour q − 1. Pour tout k, po-\nsons Sk = d′ d′′ (uk2 d′ d′′ (. . . d′ d′′ (ukq Tk ))) et S = d′ d′′ (u2 d′ d′′ (. . . d′ d′′ (uq T ))) ; ce sont des\ncourants positifs fermés, par récurrence, et l’on a Sk → S. D’après le lemme 8.5.1,\non a uk1 Sk → u1 S. Par continuité de l’opérateur d′ d′′ sur les courants, on a donc\n\f210                              CHAPITRE 8. THÉORIE DE BEDFORD–TAYLOR\n\nd′ d′′ (uk1 Sk ) → d′ d′′ (u1 S). Comme pour tout k, le courant d′ d′′ (uk1 Sk ) est positif fermé,\nle courant d′ d′′ (u1 S) l’est également. En appliquant de nouveau le lemme 8.5.1, on en\nconclut que uk0 d′ d′′ (uk1 Sk ) converge vers u0 d′ d′′ (u1 S), ce qu’il fallait démontrer.",
  "dc1373dcd4b0ae7f36d6f3bef91bf45cd82573b3fc3ddf1cda8565cc97d73447": "Remark 2.3. If X is a proper scheme over K with a line bundle L, then we denote the an-\nalytifications by X an and Lan (in the category of Berkovich spaces). By formal completion,\nevery algebraic K ◦ -model (X , L ) of (X, L) induces a formal K ◦ -model (Xˆ , Lˆ) of (X an , Lan ).\nNote that the special fiber Xs of X is canonically isomorphic to the special fiber of the formal\ncompletion Xˆ and hence the above yields a reduction map π : X an → Xs .\nLemma 2.4. Let X be a proper scheme over K and let X be a formal K ◦ -model of X an . Then\nthere exists an algebraic K ◦ -model X of X such that Xˆ dominates X.\nProof. Let us fix an algebraic K ◦ -model X0 of X. As recalled in 2.2, the set of isomorphism\nclasses of formal K ◦ -models of X an is a directed set, hence there exists a formal K ◦ -model V\nwhich dominates both X   c0 and X. Replacing V by a larger formal K ◦ -model of X an , it follows\nfrom [Bos14, Lemma 8.4.4 (d)] that the canonical map ϕ : V → X        c0 may be assumed to be\n\f6                            WALTER GUBLER AND FLORENT MARTIN\n\n\nan admissible formal blowing up in an open coherent ideal b of X    c0 . Using the formal GAGA-\nprinciple proved by Fujiwara–Kato [FK18, Theorem I.10.1.2], b is actually the formal completion\nof a coherent vertical ideal a on X0 . Hence if X is the vertical blowing up of X0 in the ideal a,\nby [Bos14, Proposition 8.2.6] we have V ∼ = Xˆ which dominates X.                               \u0003\nDefinition 2.5. Let (V, L) be a formal K ◦ -model of (V, L) as in 2.2. Then we get an associated\nformal metric k kL on L uniquely determined by requiring kskL = 1 on the generic fibre W of\nany frame s of L over any formal open subset W of V. This is well-defined because a change of\nframe involves an invertible function f on W and we have |f | = 1 on W .\nRemark 2.6. If (X , L ) is an algebraic K ◦ -model of (X, L) as in 2.1, then we get an associated\nalgebraic metric k kL on Lan by using the above construction for the formal K ◦ -model (Xˆ , Lˆ)\nof (X an , Lan ) from Remark 2.3. By construction, every algebraic metric is a formal metric. The\nconverse is also true as shown in [GK17, Proposition 8.13] (as the argument does not use the\nassumption that K is algebraically closed).\n    We have the following extension result from [GK15, Proposition 5.11]\nProposition 2.7. Let L be line bundle on a paracompact strictly K-analytic space V and let W\nbe a compact strictly K-analytic domain of V . Then every formal metric on the restriction of L\nto W extends to a formal metric on L.\nProof. Since this is stated here under more general assumptions than in [GK15, Proposition\n5.11], we sketch the argument. Let (W, L) be the formal K ◦ -model for the given formal metric\non L|W . We may assume that W is a formal open subset of a formal K ◦ -model V of V [Bos14,\nLemma 8.4.5]. By the argument in [BL93a, Lemma 5.7], there is a coherent OV -module F\non V which extends L. This works even for paracompact V as noted in the proof of [CD12,\nProposition 6.2.13] and the argument there (or in the proof of [Gub98, Lemma 7.6]) shows that\nafter replacing V by a suitable admissible blowing-up, we may assume that F is a line bundle.\nThen the associated formal metric satisfies the claim.                                      \u0003\nDefinition 2.8. Let V be a paracompact strictly K-analytic space with a line bundle L. A\nmetric k k on L is called piecewise linear if there is a G-covering (Vi )i∈I and frames si of L over\nVi for every i ∈ I such that ksi k = 1 on Vi . A function ϕ : V → R is called a piecewise linear\nfunction if it induces a piecewise linear metric on the trivial line bundle OV . Note that these\nare G-local definitions (see [GK15, Proposition 5.10] for the argument). In particular, these\nproperties are local with respect to the Berkovich topology.\nLemma 2.9. Any given G-covering of a connected paracompact strictly K-analytic space V can\nbe refined to an at most countable G-covering (Wi )i∈I of finite type (see 2.2) made by strictly",
  "6d18741f8932b971cfd7952be2ef1d067305cc7bfe1080d93352be097e42ffd8": "   We will first introduce semipositive formal metrics. We have seen in Proposition 2.10 that\nformal metrics are the same as piecewise linear metrics and hence everything applies to piecewise\nlinear metrics as well.\n3.1. Let X be a proper scheme over K with a line bundle L over X. We call an algebraic\nK ◦ -model (X , L ) of (X, L) numerically effective (briefly nef) if degL (C) ≥ 0 for every closed\ncurve C in X which is proper over K ◦ . Of course, properness implies that C is contained in\nthe special fiber Xs . An algebraic metric k k on Lan is said to be semipositive if there is a nef\nalgebraic K ◦ -model (X , L ) of (X, L) such that k k = k kL . We say that a line bundle L on\nX is numerically trivial if degL (C) = 0 for every closed curve C in X which is proper over\nK ◦ . Equivalently, we can require that L and L −1 are both nef. We say that L is numerically\nequivalent to a line bundle L ′ on X if L ′ ⊗ L −1 is numerically trivial.\n3.2. The above definition is easily generalized to the analytic setting: Let L be a line bundle on\na paracompact strictly K-analytic space V . A formal K ◦ -model (V, L) of (V, L) is called nef if\ndegL (C) ≥ 0 for any closed curve C in the special fiber Vs which is proper over the residue field\nK̃. A formal metric k k on L is called semipositive if there is a nef formal K ◦ -model (V, L) of\n(V, L) such that k k = k kL . Obviously, the trivial metric on OV is a semipositive formal metric.\n   It will follow from Proposition 3.5 below that we may use any model to test semipositivity of\nthe associated metrics. Based on this result, it is easy to check that the tensor product of two\nsemipositive formal metrics is again a semipositive formal metric.\nLemma 3.3. Let V be a paracompact strictly K-analytic space, L a line bundle on V and (V, L)\na formal K ◦ -model of (V, L). Let F be a non-archimedean extension of K and (VF , LF ) the\nformal F ◦ -model of (VF , LF ) obtained by base change. Then L is nef if and only if LF is nef.\nProof. We remark that Vs ⊗K̃ L̃ ∼      ˆ K ◦ L◦ )s . Hence the result follows from the fact that a\n                                   = (V⊗\nline bundle on a proper scheme over K̃ is nef if and only if its pull-back to F̃ is nef. This is\nproven in the projective case in [EFM, Remark 1.3.25] and the proper case follows from Chow’s\nlemma and the projection formula.                                                               \u0003\nLemma 3.4. Let V be a paracompact strictly K-analytic space, L a line bundle on V and (V, L)\na formal K ◦ -model of (V, L). Let (Vred , Lred ) be the formal K ◦ -model of (Vred , Lred) obtained by\nputting the induced reduced structure. Then L is nef if and only if Lred is nef.\nProof. Let Vred be the induced reduced structure on V. Since Vred → V is finite (in fact a\nclosed immersion), we deduce that the induced map (Vred )s → Vs between the special fibers is\nfinite. By the projection formula, we conclude that L is nef if and only if Lred is nef.   \u0003\n\f                               ON ZHANG’S SEMIPOSITIVE METRICS                                     13\n\n\nProposition 3.5. Let (V, L) be a formal K ◦ -model of (V, L). Then k kL is a semipositive formal\nmetric if and only if L is a nef formal K ◦ -model.\nProof. By definition if L is nef, then k kL is semipositive, so we only have to prove the reverse\nimplication. Hence we assume that k kL is a semipositive formal metric and we have to show\nthat L is nef. Using Lemma 3.3, we can replace K by CK and hence we may assume that K is\nalgebraically closed.\n   By definition of semipositivity, there is a nef formal K ◦ -model M of L on some formal K ◦ -\nmodel W of V with k kL = k kM . There exists a model X of V which dominates both V and\nW. Let π : X → V be the induced morphism. Since the induced morphism on the special fibers\nπs : Xs → Vs is proper and surjective, by the projection formula, L is nef if and only π ∗ L is nef.\nHence replacing (V, L) by (X, π ∗ L), we can assume that V dominates W.\n   Let Vred be the induced reduced structure on V. Hence Vred → V is finite. Locally, Vred\nis given by Spf(A) for some reduced admissible K ◦ -algebra A. Let A := A ⊗K ◦ K. It is a\nstrictly K-affinoid algebra, and by [BGR84, 6.4.3] A′ := A ◦ is an admissible K ◦ -algebra as K is\nalgebraically closed, and by [BPR16, Proposition 3.8], A → A′ is finite. By definition of A′ we\nhave an isomorphism A⊗    ˆ K◦ K ∼    ˆ K◦ K ∼\n                                 = A′ ⊗      = A . By [BGR84, Proposition 7.2.6/3], we can glue\nthe morphisms Spf(A ) → Spf(A) to get a formal K ◦ -model V′ of Vred such that V′ → Vred is\n                        ′\n\nfinite. In particular, we deduce that the induced morphisms V′s → (Vred )s → Vs are proper and\nsurjective, and we conclude from the projection formula that L is nef if and only if its pull-back\nL′ to V′ is nef.\n   By construction, V′ is locally of the form Spf(A ◦ ), hence we deduce that V′s is locally given\nby Spec(A˜) which is reduced. Now we use the fact that on an admissible formal scheme with\nreduced special fibre and with K algebraically closed, the metric k kL′ determines the model L′\nup to isomorphism (see [Gub98, Proposition 7.5]). Using that k kM′ = k kL = k kL′ for the\npull-back M′ of M to V′ , we deduce that M′ ∼   = L′ . As above, the pull-back M′ of M is nef and\n         ′\nhence L is nef.                                                                                   \u0003\nProposition 3.6. Let f : V ′ → V be a morphism of paracompact strictly K-analytic spaces and\nlet k k be a formal metric on a line bundle L of V .\n     (a) If k k is a semipositive formal metric, then f ∗ k k is a semipositive formal metric.\n    (b) If f is a surjective proper morphism and if f ∗ k k is a semipositive formal metric, then\n         k k is a semipositive formal metric.\nProof. There is a formal K ◦ -model (V, L) of (V, L) such that k k = k kL . We use Raynaud’s\ntheorem to extend f to a morphism ϕ : V′ → V of formal K ◦ -models. Then\n(3.6.1)                                   f ∗ k k = k k ϕ∗ L\nshows that f ∗ k k is a formal metric. To check semipositivity, Lemma 3.3 shows that K may be\nassumed to be algebraically closed which will allow us to use the results of [Kle66]. Then the\nclaims follow from [Kle66, Proposition I.4.1] applied to ϕs . For (b), we use additionally that ϕs\nis proper by [Tem00, Corollary 4.4] and surjective (as f and the reduction map V → Vs are\nsurjective).\n                                                                                                \u0003\nLemma 3.7. Let X be a proper scheme over K, L a line bundle on X and (X , L ) an algebraic\nK ◦ -model of (X, L) with k k := k kL . Let (Xi )i∈I be the irreducible components of X equipped\nwith their induced reduced structures. Then k k is semipositive if and only if k k|Xi is semipositive\nfor all i ∈ I.\nProof. For each i ∈ I, let Xi be the closed subscheme of X defined as the topological closure of\nXi in X equipped with the induced reduced structure. We then get for each i ∈ I a cartesian\n\f14                            WALTER GUBLER AND FLORENT MARTIN\n\n\ndiagram\n                                            Xi       // X\n\n\n                                            \u000f\u000f           \u000f\u000f\n                                           Xi        // X\n                    `\nSince the morphism i∈I Xi → X is finite surjective, the projection formula shows that L is\nnef on X if and only if L |Xi is nef on Xi for all i.                                   \u0003\n3.8. Following a suggestion of Tony Yue Yu, we can define semipositivity locally on V . We\nsay that a piecewise linear metric on L is semipositive at x ∈ V if there is a compact strictly\nK-analytic domain W in V which is a neighborhood of x such that the restriction of k k to L|W\nis a semipositive formal metric in the sense of 3.2 (using the equivalence of Proposition 2.10).\nWe say that k k is a semipositive piecewise linear metric if it is semipositive at all x ∈ V . We\nwill see in Proposition 3.11 that this fits with the definition in 3.2 assuming that V is separated.\nDefinition 3.9. Let k k be a piecewise Q-linear metric on the line bundle L over V and let\nx ∈ V . Then k k is called semipositive at x ∈ V if and only if we may choose a compact strictly\n                                                                                          ⊗k\nK-analytic domain W which is a neighborhood of x and some integer k ≥ 1 such that k k|W       is\na semipositive formal metric.\n   It follows easily from Proposition 3.5 that a piecewise linear metric on L is semipositive as a\npiecewise linear metric if and only if it is semipositive as a piecewise Q-linear metric.\nProposition 3.10. Let L be a line bundle on a paracompact strictly K-analytic space V . Let\nx ∈ V and let k k be a piecewise Q-linear metric on L.\n    (a) The set of points in V where k k is semipositive is open in V .\n   (b) The tensor product of two piecewise Q-linear metrics which are semipositive at x is again\n        semipositive at x.\n    (c) Let f : V ′ → V be a morphism of paracompact strictly K-analytic spaces. If k k is\n        semipositive at x, then f ∗ k k is semipositive at any point of f −1 (x).\nProof. Property (a) is obvious from the definitions. Property (b) follows easily from Proposition\n3.5 and the linearity of the degree of a proper curve with respect to the divisor. Finally (c)\nfollows from Proposition 3.6.                                                                   \u0003\nProposition 3.11. Let L be a line bundle on the separated paracompact strictly K-analytic space\nV and let k k be a formal metric on L. Then k k is a semipositive formal metric as globally\ndefined in 3.2 if and only if k k is a semipositive piecewise linear metric in every x ∈ V as defined\nin 3.8.\nProof. The proof follows mainly the arguments in [GK15, Proposition 6.4]. It is clear that a\nsemipositive formal metric is a semipositive piecewise linear metric in every x ∈ X and we will\nprove now the converse. Let (V, L) be a formal K ◦ -model of (V, L) with k k = k kL . Since the\ngeneric fiber V is separated, it follows from [BL93a, Proposition 4.7] that the model V is also\nseparated and hence we may apply [CD12, Lemma 6.5.1]. This is a criterion which characterizes\nthe points v in the relative interior Int(V ) over the base K (defined in [Ber93, Definition 1.5.4])\nby the property that the closure of the reduction of v in the special fiber Vs is proper over K̃.\n   We assume that k k is semipositive at every x ∈ V . We choose a closed curve C in Vs which\nis proper over K̃. We have to show that degL (C) ≥ 0. By surjectivity of the reduction map\nπ : V → Vs , there is x ∈ V such that π(x) is the generic point of C. Using [CD12, Lemma 6.5.1],\nthe properness of C yields that x ∈ Int(V ). Since k k is semipositive at x, there is a compact\nstrictly K-analytic neighborhood W of x, a nef formal K ◦ -model (W, M) of (W, L|W ) and a\n\f                                 ON ZHANG’S SEMIPOSITIVE METRICS                                      15\n\n                               ⊗k\nnon-zero k ∈ N such that k k = k kM over W . Using Proposition 3.5, we may always replace\nthe models W and V by dominating formal K ◦ -models and the line bundles M and L by their\npull-backs. By [BL93b, Corollary 5.4 (b)]2, we may therefore assume that W is a formal open\nsubset of V. Then L|⊗k                       ◦             ⊗k\n                       W is also a formal K -model of L|W and hence Proposition 3.5 implies\nthat L|W is nef.\n   Since W is a neighborhood of x and since Int(W ) is contained in the intersection of Int(V ) with\nthe topological interior of W in V by [Ber93, Proposition 1.5.5], we conclude that x ∈ Int(W ).\nUsing [CD12, Lemma 6.5.1] again, the closure of the reduction of x in Ws is proper over K̃ and\nhence equal to C. Since L|W is nef, it follows that degL (C) ≥ 0.                                 \u0003",
  "240a02e69e032853a4d040d4dc0003b0323a11b54c1ec85d7fbf671ee083500b": "Proposition 2.3.20. \u0016 Pour toute se tion f ∈ Γ(X, OX ), la fon tion log |f | est harmo-\nnique sur X .\nDémonstration. Il su\u001et de véri\u001cer que la restri tion de la fon tion log |f | à tout domaine\nstri tement k-a\u001enoïde Y ⊂ X appartient au sous-espa e H(Y ) ⊂ C0 (|Y |, R) ; vu le lemme\n2.3.5 et le théorème 2.3.8, on peut en outre supposer que Y est la \u001cbre générique d'une S -\n ourbe simplement semi-stable, auquel as il ne reste plus qu'à invoquer le point (iii) de la\nproposition 2.2.24.                                                                              2\nThéorème 2.3.21. \u0016 Soit X une ourbe stri tement k -analytique lisse. Le fais eau de R-\n                                                                                                 ×\nve toriels engendré par les germes de fon tions log |f |, f étant un germe de se tion de OX        ,\nest un sous-fais eau de HX ; le quotient est un fais eau gratte- iel sur |X| et il est nul si l'une\ndes deux onditions suivantes est véri\u001cée :\n\f58\n\n\n\n     \u0015 le orps e\n               k est algébrique sur un orps \u001cni ;\n     \u0015 la ourbe X ⊗  ca est lo alement isomorphe à P1 .\n                  b kk                               a        k\nDémonstration. Soit FX le sous-fais eau de CX asso ié au préfais eau sur |X| faisant orres-\npondre à un ouvert U le sous-espa e ve toriel de C0 (U, R) engendré par les fon tions log |f |,\n               ×\nf ∈ Γ(U, OX      ) ; 'est un sous-fais eau de HX en vertu de la proposition pré édente. Les germes\nde FX et HX oïn ident en tout point x de X de type (1), (3) ou (4) :\n    \u0015 si x est de type (1) ou (4), e point admet un système fondamental de voisinages k-\n       a\u001enoïdes ayant un unique point de Shilov et les se tions de FX et HX sont don\n        onstantes au voisinage de x ;\n    \u0015 si x est de type (3), e point admet un système fondamental de voisinages k-a\u001enoïdes\n       ayant exa tement deux points de Shilov ; les espa es ve toriels FX,x et HX,x sont alors\n       de dimension 2, engendrés par les germes de la fon tion onstante 1 et de la fon tion\n       log |f |, f étant une se tion quel onque de OX au voisinage de x telle que |f | ne soit pas\n       lo alement onstante en x.\n    Soient maintenant x ∈ X un point de type (2), k′ une extension \u001cnie galoisienne de k et x′ un\npoint de X ′ = X⊗k k′ au-dessus de x : l'égalité FX ′ ,x′ = HX ′ ,x′ implique l'égalité FX,x = HX,x .\nEn e\u001bet, si V est un voisinage stri tement k-a\u001enoïde de x dans X , V ′ est la omposante\n onnexe de x′ dans V ⊗k k′ , et f ′ ∈ A×                                                        ×\n                                                    V ′ , la norme f de f est un élément de AV tel que\n                                                                              ′\n                      ′\np∗ |f ||V ′ = |f ′ |[k :k] ; si une fon tion h ∈ H(V ) est telle que p∗ h|V ′ soit une ombinaison linéaire\nde fon tions log |f |, f ∈ A×                                                                           ×\n                                    V ′ , 'est don une ombinaison linéaire de fon tions log |f |, f ∈ AV .\nCette remarque préliminaire permet de supposer que X est isomorphe à la \u001cbre générique\nd'une S - ourbe simplement semi-stable X et que le point x orrespond à une omposante\nirrédu tible propre et géométriquement onnexe Cx de Xs .\nLemme 2.3.22. \u0016 Ave les notations en vigueur, l'espa e ve toriel HX,x /FX,x est anoni-\nquement isomorphe à l'espa e ve toriel Pic0 (Cx ) ⊗Z R.",
  "cd12932de3c4cd0dee40f8ac44b0531b9795312ab37f1068b36a2a7eecabb558": "                              3.1. Le problème de Diri hlet\n  Dans e qui suit, X est une ourbe stri tement k-analytique lisse.\n3.1.1. Propriétés fondamentales des fon tions harmoniques.\n  Les se tions du fais eau HX satisfont au prin ipe du maximum.\nProposition 3.1.1. \u0016 Étant donné un ouvert Ω de X , une fon tion h ∈ Γ(Ω, HX ) admet\nun extremum lo al en un point x de Ω si et seulement si elle est onstante au voisinage de x.\n  C'est la onjon tion de la proposition 2.3.13 et du orollaire 2.3.14.\n   Le problème de Diri hlet est lo alement résoluble : tout point x ∈ X admet un système\nfondamental de voisinages ouverts relativement ompa ts Ω tels que l'appli ation de restri tion\n                              C0 (Ω, R) ∩ Γ(Ω, HX ) → C0 (∂Ω, R)\nsoit un isomorphisme. Il su\u001et en e\u001bet de prendre pour Ω l'intérieur d'un voisinage stri tement\nk-a\u001enoïde Y de x dans X et d'appliquer le lemme 2.3.9.",
  "e6679c4ed22bf386251a069fc8f648b473c02405cef3687841aed57bd582186e": "3.1.2. Fon tions sous-harmoniques.\nDéfinition 3.1.5. \u0016 Soit Ω un ouvert de X ; une fon tion u : Ω → R ∪ {−∞} est dite\nsous-harmonique si elle est semi- ontinue supérieurement, n'est identiquement égale à −∞\nsur au une omposante onnexe de Ω et satisfait à la ondition suivante : pour tout domaine\nstri tement k-a\u001enoïde Y dans X et toute fon tion h ∈ H(Y ),\n                                  (u|∂Y ≤ h|∂Y ) =⇒ (u|Y ≤ h).\n\n     L'assertion suivante n'est pas surprenante.\nProposition 3.1.6. \u0016 Soient Ω ⊂ X un ouvert et f ∈ Γ(Ω, OX ) une se tion inversible\nsur un ouvert dense de Ω ; la fon tion log |f | est sous-harmonique sur Ω.\nDémonstration. La fon tion log |f | est ontinue sur Ω et, f étant inversible sur un ouvert\ndense, n'est identiquement égale à −∞ sur au une des omposante onnexes de Ω.\n   Soient Y ⊂ Ω un domaine stri tement k-a\u001enoïde et h ∈ H(Y ) une fon tion majorant log |f |\nsur Γ(Y ) = ∂Y ; puisqu'il su\u001et de prouver l'inégalité log |f ||Y ≤ h après avoir e\u001be tué une\nextension \u001cnie k′ de k, nous pouvons supposer que Y est la \u001cbre générique d'une S - ourbe\nsimplement semi-stable Y , de squelette S(Y) et de rétra tion τY : Y → S(Y). Dans es\n onditions :\n   \u0015 H = h|S(Y) ∈ H(S(Y), Γ(Y )) et h = H ◦ τY ;\n   \u0015 la fon tion F = log |f ||S(Y) est sous-harmonique sur S(Y) − Γ(Y ) (proposition 2.2.24,\n     (iii)) et log |f ||Y ≤ F ◦ τY (proposition 2.2.24, (ii)) ;\nla on lusion dé oule alors de l'inégalité F ≤ H sur S(Y).                                  2\nRemarque 3.1.7. \u0016 Nous verrons plus loin (proposition 3.4.6) que, pour toute S - ourbe\nsimplement semi-stable X et toute fon tion sous-harmonique u sur Xη − Γ(Xη ), la restri tion\nU de u à S(X ) − Γ(Xη ) est sous-harmonique (= onvexe) : ddc U ≥ 0, l'opérateur ddc étant\nentendu au sens des ourants, omme expliqué à en 1.2.5.\n\n     Les propriétés suivantes des fon tions sous-harmoniques sont évidentes.\nProposition 3.1.8. \u0016 Étant donné un ouvert Ω de X ,\n   (i ) l'ensemble des fon tions sous-harmoniques sur Ω est un \u001dne réel stable par max : pour\ntoutes fon tions u, v sous-harmoniques sur Ω et tous nombres réels positifs µ, ν , les fon tions\nµu + νv et max(u, v) sont sous-harmoniques sur Ω ;\n   (ii ) l'enveloppe inférieure d'une famille dé roissante de fon tions sous-harmoniques sur Ω\nest, sur ha une des omposantes onnexes de Ω, sous-harmonique ou identiquement égale à\n−∞ ;\n   (iii ) la régularisation semi- ontinue supérieurement de l'enveloppe supérieure d'une famille\n roissante et lo alement bornée de fon tions sous-harmoniques sur Ω est sous-harmonique.\n\n     Le \u001dne des fon tions sous-harmoniques sur un ouvert Ω de X est noté SH(Ω).",
  "5e0db20c0db4acc10fb61ca401b8b7804099346aead443ce6ca1724684f4e4de": "  Les fon tions sous-harmoniques satisfont au prin ipe du maximum suivant.\n\nProposition 3.1.11. \u0016 Étant donné un ouvert Ω de X , une fon tion sous-harmonique u\nsur Ω admettant un maximum lo al en un point x de Ω est lo alement onstante au voisinage\nde x.\n\nDémonstration. Soit u une fon tion sous-harmonique admettant un maximum au point x\nde Ω et soit U un voisinage ouvert onnexe de x dans Ω tel que u|U ≤ u(x) ; puisque u|U n'est\npas identiquement égale à −∞, u(x) > −∞.\n   Soit Y un voisinage stri tement k-a\u001enoïde onnexe Y de x dans U . La restri tion de u à\nΓ(Y ) est onstante, égale à u(x) : s'il existait, en e\u001bet, un point y ∈ Γ(Y ) tel que u(y) < u(x),\nle lemme 2.3.9 fournirait une fon tion h ∈ H(Y ) telle que\n   \u0015 h(y) = u(y) ;\n   \u0015 h|Γ(Y )−{y} = u(x) ;\n\f64\n\n\n\npuisque Y est onnexe et h non onstante, le prin ipe du maximum pour les fon tions harmo-\nniques impliquerait alors h|Y −Γ(Y ) < u(x) et don , par sous-harmoni ité, l'inégalité absurde\nu(x) ≤ h(x) < u(x).\n   La on lusion est maintenant immédiate : l'ensemble des points de Shilov des voisinages\nstri tement k-a\u001enoïdes onnexes de x dans U étant une partie dense de U , la fon tion semi-\n ontinue supérieurement u|U est onstante, égale à u(x).                                     2\n\nCorollaire 3.1.12. \u0016 Soient Ω ⊂ X un ouvert et u : Ω → R ∪ {−∞} une fon tion semi-\n ontinue supérieurement qui n'est identiquement égale à −∞ sur au une omposante onnexe\nde Ω. Les propriétés suivantes sont équivalentes :\n   (i ) u est sous-harmonique ;\n   (ii ) pour tout ouvert Ω′ ⊂ Ω et pour toute fon tion harmonique h sur Ω′ , la fon tion u|Ω′ −h\nsatisfait au prin ipe du maximum (proposition 3.1.11) sur Ω′ .\nDémonstration. L'impli ation (i) ⇒ (ii) est l'appli ation dire te de la proposition pré é-\ndente puisque toute fon tion harmonique est sous-harmonique.\n   L'impli ation ré iproque est immédiate : étant donnés un domaine stri tement k-a\u001enoïde\nV ⊂ Ω et une fon tion h ∈ H(V ) telle que u|∂V ≤ h|∂V , l'appli ation du prin ipe du maximum\nà la fon tion u − h sur v − ∂V implique que elle- i atteint son maximum en un point de ∂V ;\nelle est don négative. La fon tion u est bien sous-harmonique sur Ω.                            2\n   La reformulation pré édente de la dé\u001cnition 3.1.5 met en éviden e le ara tère lo al de la\nsous-harmoni ité.\n\nCorollaire 3.1.13. \u0016 Le préfais eau SH sur |X| est un fais eau.\n\nDémonstration. La semi- ontinuité supérieure et le fait de ne pas être identiquement −∞\nsur une omposante onnexe sont des propriétés de nature lo ale. La propriété (ii) du orollaire\npré édent est également de nature lo ale.                                                  2\n\nProposition 3.1.14. \u0016 Soit X une ourbe stri tement k -analytique lisse. Étant donnés\nune ourbe stri tement k-analytique lisse Y , un morphisme f : Y → X et une fon tion sous-",
  "03db35ca81bc95d4d7ebd173b99f693c6eff6d22ed74c6188e39ad5d8260fb4c": "     In view of Theorem 7.1, it is natural to introduce as in [BJ18a]:\nDefinition 7.2. Assume that K is non-Archimedean, and let L be a semiample Q-line\nbundle. We say that a (possibly singular) metric φ on L is plurisubharmonic ( psh for short)\nif φ can be written as the pointwise limit of a decreasing net φi ∈ FS(L) of Fubini–Study\nmetrics on L. We denote by PSH(L) the set of psh metrics on L.\n   Given a subgroup Γ ⊂ R, nontrivial if K is trivially valued, FSΓ (L) is dense in FS(L)\nwith respect to uniform convergence, by Proposition 5.4 (v); it would thus be equivalent to\nrequire φi ∈ FSΓ (L) in the above definition.\n  As a direct consequence of Corollary 5.7, we have:\nLemma 7.3. Let A be the Stein factorization of L. Then\n                               PSH(A) ≃ PSH(L) ≃ PSH(Lred ).\n   The following general result, borrowed from [BJ18a, Proposition 5.6], ensures that PSH(L)\nis closed under decreasing limits.\nLemma 7.4. Let F ⊂ C0 (L) be a family of continuous metrics on a Q-line bundle L, closed\nunder addition of a constant, and define Fe as the set of possibly singular metrics on L that\ncan be written as decreasing limits of nets in F. Then Fe is closed under decreasing limits.\n                                           e For each i ∈ I choose a decreasing net (φi,j )j∈J\nProof. Let (φi )i∈I be a decreasing net in F.                                                  i\nin F converging to φi . Let A be the set of triples α = (i, j, m) with i ∈ I, j ∈ Ji and\nm ∈ Z>0 . For each α = (i, j, m) in A, set\n                                     ψα := φi,j + m−1 ∈ F,\nand define a partial order on A by\n                                     α ≥ α′ ⇐⇒ ψα ≤ ψα′ .\nWe claim that A is directed, i.e. any two elements a1 = (i1 , j1 , m1 ), a2 = (i2 , j2 , m2 ) in\nA can be dominated by a third. To see this, first pick i ≥ i1 , i2 , so that φi ≤ φi1 and\nφi ≤ φi2 , and set m := max{m1 , m2 } + 1. A simple variant of Dini’s lemma shows that\nφi,j + m−1 ≤ φik ,jk + m−1\n                         k = ψak on X\n                                       an for k = 1, 2 and all j ∈ J large enough, which\n                                                                      i\nproves the claim. By construction, (ψα )α∈A is a decreasing net in F such that ψα → φ\n                                  e\npointwise on X an , and hence φ ∈ F.                                                          \u0003\nCorollary 7.5. The space PSH(L) is stable under finite max and decreasing limits.\nCorollary 7.6. Pick a subgroup Γ ⊂ R, nontrivial if K is trivially valued. For any semi-\nample Q-line bundle L, the set C0 ∩ PSH(L) of continuous psh metrics on L is the closure\nof FSΓ (L) with respect to uniform convergence.\nProof. Let φ be a continuous psh metric, and pick a decreasing net (φi ) in FSΓ (L) converging\npointwise to φ. By Dini’s lemma, φi → φ uniformly on X an , and φ is thus in the closure\nof FSΓ (L). Conversely, let (φi ) be a sequence in FSΓ (L) converging unifornly to some\n(continuous) metric φ. We can inductively construct a sequence of constants ci → 0 such\nthat φi + ci is decreasing, and it follows that φ = limi (φi + ci ) is psh.                  \u0003\n\f                NORMS, DETERMINANT OF COHOMOLOGY AND FEKETE POINTS                           49\n\n7.2. Nef metrics. Assume that K is non-Archimedean. A model metric φ on a Q-line\nbundle L is nef if φ = φL for some Q-model L of L which is nef, i.e. L · C ≥ 0 for each\ne\nK-projective  curve C ⊂ Xs . By [GM19, Proposition 3.5], any Q-model L′ of L such that\nφ = φL′ is then also nef.\nDefinition 7.7. A nef metric on a Q-line bundle L is a continuous metric φ that can be\nwritten as a uniform limit of nef model metrics.\n   This is usually known as a semipositive metric in the sense of S.W. Zhang, cf. [GM19] for\na thorough discussion. When K is trivially valued, the trivial metric is the only nef metric.\nTheorem 7.8. Assume that K is nontrivially valued, and let L be an ample Q-line bundle.\nThen a continuous metric on L is nef iff it is psh (in the sense of Definition 7.2).\n   A proof of this result is also sketched, in a slightly different language, in [CMor18, Remark\n3.18]; we nevertheless provide a proof below, for completeness. By [GM19, Corollary 1.4],\nwe get:\nCorollary 7.9. Let L be an ample Q-line bundle, and pick a Q-model L of L. Then φL is\npsh iff L is nef.\nProof of Theorem 7.8. By Theorem 5.14, pure Fubini–Study metrics on L coincide with\nmodel metrics associated to Q-models L of L that are semiample, and hence nef. Since K\nis nontrivially valued, Corollary 7.6 implies that every continuous psh metric is a uniform\nlimit of pure Fubini–Study metrics, and hence is nef.\n   To prove the converse, let L be a nef Q-model of L, determined on a model X of X.\nUsing again Theorem 5.14, it will be enough to show that φL is a uniform limit of model\nmetrics associated to semiample Q-models. Since L is ample, it admits an ample Q-model\nA on some projective model X ′ dominating X (cf. [GM19, Lemma 4.12]). The pull-back\nL′ of L to X ′ is nef. For each ε ∈ (0, 1) ∩ Q, Lε := (1 − ε)L′ + εH is thus ample on Xs ,\nand hence on X , by [EGA, IV.9.6.4]. In particular, Lε is a semiample model of L. Since\nφL = φL′ (Lemma 5.10), φLε − φL = ε(φH − φL ) converges to 0 uniformly as ε > 0, and we\nare done.                                                                                 \u0003\nRemark 7.10. We expect Theorem 7.8 and Corollary 7.9 to hold when L is merely semi-\nample. For this, it would be enough to show that any nef model metric on L descends to the\nStein factorization A as in Lemma 5.5; this would for instance follow from a relative version\nof the local Hodge index theorem proved in [YZ16, Theorem 2.1].\n7.3. Psh-regularizable metrics. The curvature form of a smooth metric φ on a line bun-\ndle L is a closed (1, 1)-form, which we denote by ddc φ (see [CLD12, §6.4.1] for the non-\nArchimedean case). For each trivializing section τ of L over an open U ⊂ X, the function\nlog |τ |φ is smooth, and ddc φ = −ddc log |τ |φ on U an . Again, this makes sense for Q-line\nbundles as well.\nDefinition 7.11. A smooth metric φ on a Q-line bundle L is semipositive if its curvature\nform ddc φ is semipositive (see [CLD12, §5.4] for the non-Archimedean case).",
  "1ffe08a5900d483d40d3a6de9e5a4efdc6b6efa1efc4df7c6f35d7169c408993": "                  8. Monge–Ampère measures and Deligne pairings\n   In this section, we review some basic properties of Monge–Ampère operators, and use them\nto define metrics on Deligne pairings (Theorem 8.16), following Deligne’s program [Del87].\nIn what follows, X is as before an n-dimensional projective scheme over a complete valued\nfield K.\n8.1. Mixed Monge–Ampère measures. The (algebraic) fundamental class of X is the\nn-dimensional cycle               X\n                            [X] =   mα [Xα ],\n                                                     α\nwhere the Xα denote the n-dimensional irreducible components of X (with their reduced\nstructure) and mα is the length of the local ring of X at the generic point of Xα . The\nintersection number of Q-line bundles L1 , . . . , Ln on X is defined as\n                      (L1 · . . . · Ln ) := deg π⋆ (c1 (L1 ) · . . . · c1 (Ln ) · [X]) ,\nwith π : X → Spec K the structure morphism.\n  Now let φ1 , . . . , φn be smooth metrics on L1 , . . . , Ln , and recall that ddc φi denotes the\ncurvature form of φi , a smooth, closed (1, 1)-form on X an (cf. [CLD12, §6.4.1] for the non-\nArchimedean case). The smooth (n, n)-form ddc φ1 ∧. . .∧ddc φn determines a Radon measure\n                                               X\n                ddc φ1 ∧ . . . ∧ ddc φn ∧ δX =   mα ddc φ1 ∧ . . . ∧ ddc φn ∧ δXα             (8.1)\n                                       α\n                          an\non the topological space X , the mixed Monge–Ampère measure     of the φi , with δX =\nP\n  α m  δ\n      α Xα denoting the analytic fundamental class of X (see [CLD12,  §3.7] for the non-\nArchimedean case).\nRemark 8.1. When K = R, we define ddc φ1 ∧ . . . ∧ ddc φn ∧ δX as the image of the\ncorresponding measure on X(C) = XCan by the projection map XCan → X an .\nExample 8.2. Assume that n = 0, i.e. X = Spec A with A a finite K-algebra. The pre-\nvious construction produces a positive measure δX on Q    the finite set X an , which is described\nas follows. We have a product decomposition A = i Ai into local finite K-algebras Ai\ncorresponding to the connected components of X. The (reduced) irreducible components of\nX are given by Xi = Spec Ki , where the residue field Ki of Ai is a finite extension of K,\nand the uniquePextension of the absolute value of K to Ki defines a point xi ∈ X an . The\ncurrent δX = i mi δXi is a measure on X an , and the requirement that δXi has total mass\ndeg π⋆ [Xi ] = [Ki : K] yields δXi = [Ki : K]δxi . As mi [Ki : K] = dimK Ai , we conclude that\n                                           X\n                                     δX =     (dimK Ai )δxi .\n                                                 i\n\nProposition 8.3. For each tuple φ1 , . . . , φn of smooth metrics on Q-line bundles L1 , . . . , Ln ,\nthe mixed Monge–Ampère measure ddc φ1 ∧ . . . ∧ ddc φn ∧ δX satisfies the following properties:\n    (i) it is a symmetric, multilinear function of the φi , and a positive Radon measure if\n        the φi are semipositive, i.e. ddc φi ≥ 0;\n\f56                         SÉBASTIEN BOUCKSOM AND DENNIS ERIKSSON\n           R\n      (ii) ddc φ1 ∧ . . . ∧ ddc φn ∧ δX = (L1 · . . . · Ln );\n     (iii) if L0 = L1 = OX (and hence φ0 , φ1 are smooth functions on X an ), then\n      Z                                              Z\n          φ0 dd φ1 ∧ dd φ2 ∧ . . . ∧ dd φn ∧ δX = φ1 ddc φ0 ∧ ddc φ2 ∧ . . . ∧ ddc φn ∧ δX .\n               c        c              c\n                                                                                               (8.2)\n\n     (iv) for any complete field extension F/K, we have\n                 p⋆ (ddc φ1,F ∧ . . . ∧ ddc φn,F ∧ δXF ) = ddc φ1 ∧ . . . ∧ ddc φn ∧ δX ,\n         where φi,F is the pullback of φi to Li,F and p : XFan → X an is the canonical projection.\nProof. (i) is straightforward. (ii) is classical in the Archimedean case, and proved in [CLD12,\nProposition 6.4.3] in the non-Archimedean case. (iii) is a consequence of the Stokes formula\n(see [CLD12, Théorème 3.12.2] in the non-Archimedean case). In the Archimedean case, (iv)\nis nontrivial only when K = R, F = C, in which case it holds by definition (see Remark 8.1).\nIn the non-Archimedean case, it is implicit in [CLD12], and can be checked as follows. Pick\na smooth, compactly supported function f on X an , and consider the smooth, compactly\nsupported (n, n)-form α := f ddc φ1 ∧ . . . ∧ ddc φn . According to [Gub16, Proposition 5.13],\nthere exists a Zariski open subset U ⊂ X with a closed embedding U ֒→ Grm,K and a\ncompactly supported smooth (n, n)-superform on Rr such that α is obtained by pulling-\nback η by the tropicalization map Trop : U an → Rr , and\n                             Z                                  Z\n                                      c              c\n                                f dd φ1 ∧ · · · ∧ dd φn ∧ δX =     α\n                                                                          X\nis defined as the integral of η on the tropical cycle Trop(U ). Unravelling the definitions, it\nis clear that the pull-back αF of α to XFan is simply the pull-back of η by the tropicalization\nmap TropF : UFan → Rr . The construction of the tropical cycle of an algebraic variety being\ninvariant under ground field extension,\n                                  R       Rwe have TropF (UF ) = Trop(U ) as tropical cycles,\nand we conclude as desired that X α = XF αF .                                                 \u0003\n   Recall from §7.3 that a continuous metric on a Q-line bundle L is psh-regularizable iff it is\na uniform limit of smooth semipositive metrics on L. If L is semiample, then any continuous\npsh metric (in the sense of Definition 7.2, i.e. a uniform limit of Fubini–Study metrics) is\npsh-regularizable, by Theorem 7.14.\nTheorem 8.4. Let L1 , . . . , Ln be Q-line bundles on X. The measure-valued operator\n                             (φ1 , . . . , φn ) 7→ ddc φ1 ∧ . . . ∧ ddc φn ∧ δX ,\ndefined so far on smooth metrics, admits a unique continuous extension to tuples of contin-\nuous, psh-regularizable metrics on the Li , with respect to uniform convergence for tuples of\nmetrics, and the weak topology on Radon measures.\n     As a direct consequence of Proposition 8.3, we get:\nProposition 8.5. For each tuple of continuous, psh-regularizable metrics (φi ),\n                                            X\n             ddc φ1 ∧ . . . ∧ ddc φn ∧ δX =   mα ddc φ1 ∧ . . . ∧ ddc φn ∧ δXα\n                                                     α\n\nis a positive Radon measure on X an , of total mass (L1 · . . . · Ln ). It is further symmetric\nand multiadditive as a function of the φi .\n\f                    NORMS, DETERMINANT OF COHOMOLOGY AND FEKETE POINTS                                          57\n\n   Theorem 8.4 follows from the classical Bedford–Taylor theory [BT76] in the Archimedean\ncase, and from its analogue in the non-Archimedean case [CLD12, Corollaire 5.6.5]. In the\npresent global setting, one can however provide a simple direct argument, based on the\nfollowing global version of the classical Chern–Levine–Nirenberg inequality that will be put\nto use again a bit later.\nLemma 8.6. Let L0 , . . . , Ln be line bundles on X, and suppose given a pair of smooth,\nsemipositive metrics φi , φ′i on each Li . Then\n       Z                                            Z\n          (φ0 − φ′0 ) ddc φ1 ∧ . . . ∧ ddc φn ∧ δX − (φ0 − φ′0 ) ddc φ′1 ∧ . . . ∧ ddc φ′n ∧ δX\n\n                                                  n\n                                                  X\n                                           ≤C           sup |φi − φ′i |\n                                                  i=1\n\nwith C := 2 max1≤i≤n (L0 · L1 · . . . · Lbi · . . . · Ln ).\nProof. For brevity of notation, set T := ddc φ2 ∧ . . . ∧ ddc φn ∧ δX . By (8.2),\n       Z                         Z                          Z\n         (φ0 − φ′0 ) ddc φ1 ∧ T − (φ0 − φ′0 ) ddc φ′1 ∧ T = (φ0 − φ′0 ) ddc (φ1 − φ′1 ) ∧ T\n          Z                                       Z                              Z\n      =       (φ1 − φ′1 ) ddc (φ0 − φ′0 ) ∧ T =       (φ1 − φ′1 ) ddc φ0 ∧ T +       (φ1 − φ′1 ) ddc φ′0 ∧ T.\n\nSince ddc φ0 ∧ T and ddc φ′0 ∧ T are both positive measures of mass (L0 · L2 · . . . · Ln ), we infer\n     Z                          Z\n       (φ0 − φ0 ) dd φ1 ∧ T − (φ0 − φ′0 ) ddc φ′1 ∧ T ≤ 2(L0 · L2 · . . . · Ln ) sup |φ1 − φ′1 |.\n                ′   c\n\n\nWe conclude by symmetry and multilinearity.                                                                     \u0003\nProof of Theorem 8.4. Assume first that K is non-Archimedean, and pick f ∈ PLR (X an ).\nBy Lemma 5.17, we can find a pair of Fubini–Study metrics on an ample line bundle L0 such\nthat f = φ0 − φ′0 . By Theorem 7.14, φ0 and φ′0 are uniform limits of smooth, semipositive\nmetrics on L0 . Lemma 8.6 thus shows that\n                                             Z\n                        (φ1 , . . . , φn ) 7→ f ddc φ1 ∧ . . . ∧ ddc φn ∧ δX\n\nis Lipschitz continuous with respect to the supnorm on tuples of smooth, semipositive met-\nrics (with Lipschitz constant depending on f ), and hence extends continuously to tuples of\ncontinuous, psh-regularizable metrics. For eachR tuple of continuous, psh-regularizable met-\nrics (φi ), the linear form on PLR (X an ) f 7→ f ddc φ1 ∧ . . . ∧ ddc φn ∧ δX is positive, hence\ncontinuous, and it thus extends to a positive linear form on C0 (X), by density of PLR (X an ).\n   In the Archimedean case, the argument is similar, arguing with a smooth function f\ninstead. It is in fact even simpler, since f can directly be written as a difference of smooth\npsh metrics on some ample line bundle.                                                         \u0003\n   In order to exploit the multilinearity of the previous construction, it is convenient to\nintroduce the following terminology.\nDefinition 8.7. We say that a continuous metric φ on a line bundle L is dpsh if it can be\nwritten as a difference of continuous, psh-regularizable metrics.\n\f58                        SÉBASTIEN BOUCKSOM AND DENNIS ERIKSSON\n\n     A dpsh metric is thus the same as an approachable metric in the sense of [CLD12, §6.3].\nLemma 8.8. Every line bundle L admits a smooth, dpsh metric.\nProof. By Theorem 7.14, any ample line bundle admits a smooth, semipositive metric, and\nthe result follows since L can be written as a difference of ample line bundles.      \u0003\nExample 8.9. If K is Archimedean, every smooth metric is dpsh.\n   While this is probably true in the non-Archimedean case as well, it is less obvious, since\nstrictly positive (1, 1)-forms do not exist globally in this context.\nExample 8.10. If K is non-Archimedean, every R-PL metric is dpsh, by Lemma 5.17.\n   The operator (φ1 , . . . , φn ) 7→ ddc φ1 ∧. . .∧ddc φn ∧δX , being symmetric and multiadditive on\ntuples of continuous, psh-regularizable metrics, extends to a symmetric, multilinear operator\non continuous dpsh metrics, with values in signed Radon measure. Note that Proposition 8.3\nstill holds for such metrics.\nExample 8.11. If K is non-Archimedean and φ1 , . . . φn are R-PL metrics, then ddc φ1 ∧. . .∧\nddc φn ∧ δX has finite support. By ground field invariance, we may indeed assume that K is\nalgebraically closed, and that its value group is large enough to ensure that the φi become pure\nafter base change. By Proposition 5.16, φ1 , . . . , φn are then induced by Q-models L1 , . . . , Ln\nof L1 , . . . , Ln determined on a projective model X of X. By linearity with respect to the\nfundamental class [X], we may further assume that X is (geometrically) irreducible, which\nallows us to assume that Xs is reduced, by Theorem 4.20. Each irreducible component Y of\nXs then determines a unique Shilov point xY ∈ Γ(X ), and\n                                                       X\n                        ddc φ1 ∧ . . . ∧ ddc φn ∧ δX =  (L1 |Y · . . . · Ln |Y )δxY ,         (8.3)\n                                                    Y\nby [CLD12, Proposition 6.9.2] (compare [Gub07, Proposition 3.11]).",
  "1db7782548c52fe9ce85efc3d4c88ed30a65323334bf8da1bc8a21483dcea58b": "Theorem 8.18. Let L0 , . . . , Ln be line bundles on a projective K-scheme X of dimension\nn. Let L0 , . . . , Ln be models of L0 , . . . , Ln , determined on a projective model X of X, and\ndenote by φ0 , . . . , φn the corresponding model metrics. Then\n                                         hφ0 , . . . , φn i = φhL0 ,...,Ln i .                        (8.15)\n  Here hL0 , . . . , Ln i is the Deligne pairing with respect to the flat projective morphism X →\nSpec K ◦ , cf. Appendix A. Since Deligne pairings commute with base change, hL0 , . . . , Ln i is\na model of hL0 , . . . , Ln i, and φhL0 ,...,Ln i denotes the corresponding model metric.\nProof. We argue by induction on n. Assume first n = 0, and hence X = Spec A with A finite\nfree over K ◦ . As recalled in Lemma A.19, any line bundle on X is trivial in a neighborhood\nof the special fiber of X , and hence trivial on X . A trivializing section s ∈ H0 (L0 ) induces\na trivializing section hsi = NX /K ◦ (s) of hL0 i = NX /K ◦ (L0 ), as well as a trivializing section\ns ∈ H0 (X, L0 ), such that |s|φ0 = 1 on X an . By (8.11), we infer\n                                                Z\n                                log |hsi|hφ0 i = log |s|φ0 δX = 0,\n\nwhich is equivalent to hφ0 i = φhL0 i .\n   Let now L0 , . . . , Ln be line bundle on a projective K-scheme X of dimension n, and\nL0 , . . . , Ln be models of L0 , . . . , Ln determined on a projective model X of X. Since any\nline bundle on X can be written as a difference of ample line bundles, we may assume that\nL0 is ample, by linearity. After passing to a large enough multiple, we assume that there\nexists a relatively regular section s ∈ H0 (L0 ), by Proposition A.15. Denote by Z its divisor,\nwith generic fiber Z. By the restriction property of Deligne pairings on models, s induces\nan isomorphism\n                                   hL0 , · · · , Ln i = hL1 |Z , . . . , Ln |Z i\nof models of hL0 , . . . , Ln i = hL1 |Z , . . . , Ln |Z i. By induction, we get\n                        φhL0 ,··· ,Ln i = φhL1 |Z ,...,Ln |Z i = hφ1 |Z , . . . , φn |Z i\n                                           Z\n                     = hφ0 , . . . , φn i + log |s|φ0 ddc φ1 ∧ . . . ∧ ddc φn ∧ δX ,\n\f66                       SÉBASTIEN BOUCKSOM AND DENNIS ERIKSSON\n\nusing the restriction property of Theorem 8.16. It remains to show that the right-hand\nintegral vanishes, which follows from the fact that ddc φ1 ∧ . . . ∧ ddc φn ∧ δX is supported on\nΓ(X ) (cf. Example 8.11) together with Lemma 8.19 below.                                       \u0003\nLemma 8.19. If s is a relatively regular section of a line bundle L on a model X , then\n|s|φL = 1 on Γ(X ).\nProof. Since s doesn’t vanish at the associated points of Xs , s is nonzero on the reduction\nξ := redX (x) of any Shilov point x ∈ X an defined by X . In other words, s defines a\ntrivializing section of L on an open neighborhood U of ξ, and we infer |s|φL ≡ 1 on U i , by\ndefinition of the model metric φL .                                                        \u0003\n   Using Theorem 8.18, we relate Deligne pairings and Gubler’s intersection theory on mod-\nels [Gub98].\nDefinition 8.20. If D is a vertical Cartier divisor and L1 , . . . , Ln are line bundles on a\nprojective model X of X, we define their intersection number as the real number\n                             (D · L1 · . . . · Ln ) := φhOX (D),L1 ,...,Lni .\n   Here the right-hand side is a model function on Spec K, identified with its value on the\nunique point of Spec K. Equivalently, (D · L1 . . . · Ln ) = vK (f ) for any choice of generator\nf of the free K ◦ -module\n                                       hO(D), L1 , . . . , Ln i ֒→ K.\nIn particular, (D · L1 . . . · Ln ) belongs to the (additive) value group ΓK ⊂ R.\n   As a special case of Theorem 8.18, we have\n                                            Z\n                     (D · L1 . . . · Ln ) = φD ddc φL1 ∧ . . . ∧ ddc φLn ∧ δX .           (8.16)\n\nOn the other hand, in [Gub98, §3] Gubler associates to every vertical Cartier divisor D on\nX an n-dimensional cycle cyc(D) with coefficients in ΓK on the finite type K̃-scheme Xs ,\nsuch that the following holds:\n     (i) if µ : X ′ → X is a morphism of projective models, then cyc(D) = µ⋆ cyc(µ⋆ D);\n    (ii) if F/K is a non-Archimedean extension and DF is the pull-back of D to the base\n         change of X to F ◦ , then cyc(DF ) = cyc(D)Fe ;\n   (iii) if Xs is reduced, every irreducible component Y of Xs determines a unique Shilov\n         point xY ∈ Γ(X ), and\n                                             X\n                                   cyc(D) =      φD (xY )[Y ].\n                                                  Y\nCorollary 8.21. Let L1 , . . . , Ln be line bundles on a model X of X, and D be a vertical\nCartier divisor on X . Then\n                      (D · L1 · . . . · Ln ) = (cyc(D) · L1 |Xs · . . . · Ln |Xs ) .\nProof. By (8.16), (D · L1 · . . . · Ln ) is invariant under ground field extension, and we may\nthus assume that K is algebraically closed and nontrivially valued. By multilinearity, we\nmay further assume that X is (geometrically) reduced. After replacing X with a higher\nmodel, we can arrange for Xs to be reduced, by Theorem 4.20. By (8.3), we then have\n                                                Z\n                       (D · L1 · . . . · Ln ) = φD ddc φ1 ∧ · · · ∧ ddc φn\n\f                  NORMS, DETERMINANT OF COHOMOLOGY AND FEKETE POINTS                                    67\n                    X\n                =       φD (xY ) (L1 |Y · . . . · Ln |Y ) = (cyc(D) · L1 |Xs · . . . · Ln |Xs ) .\n                    Y\n                                                                                                        \u0003",
  "efd93bc7c655ffb0de961623bfee2c439eb44fbce26686557a9cf10fd0f8fe90": "    In the theory of Chambert-Loir and Ducros [CD12, §5.4], we can associate to every\ncontinuous real function u on X an associated current [u]. The function h is called\nplurisubharmonic (or just psh) in the sense of Chambert-Loir and Ducros if the associated\ncurrent d′ d′′ [h] is positive. See [CD12, §5.5] for details. Then we can show the following\nmaximum principle.\nTheorem 1.7. Let X be a good, separated, strictly k-analytic space, and let u be a piecewise\nsmooth function on X which is psh in the sense of Chambert-Loir and Ducros. If u has a\nlocal maximum on x ∈ X \\ ∂ X , then u is locally constant at x.\n   Since any semipositive R-PL function is psh in the sense of Chambert-Loir and Ducros\n[GJR21, Theorem 7.14], the maximum principle holds for semipositive R-PL functions.\nWe prove Theorem 1.7 by proving a tropical analogue in Theorem 7.4: namely, if C ⊂\nRn is a tropical variety of pure dimension d and if f : C → R is weakly tropically psh,\nin the sense that the Lagerberg current d′ d′′ [ f ] is positive, then f satisfies a similar\nmaximum principle. The proof uses the Bieri–Groves theorem for affinoid varieties given\nin Theorem 1.6. Then Theorem 1.7 is shown in Theorem 7.7.\nRemark 1.8. We do not know whether an R-PL function that is psh in the sense of\nChambert-Loir and Ducros is necessarily semipositive. This is strongly related to the\nquestion of whether psh functions are stable under pullback, which is likewise unknown.",
  "b03d31f8ee06459fa5717a8ecba30a1ea5875ef773072aaa5d6a044eb85e9060": "Theorem 4.1. Let X be a good, compact, strictly k-analytic space, let X be an admissible\nformal k◦ -model of X , let x ∈ X , and let η ∈ Xs be the reduction of x. Suppose that the\nZariski closure of {η} has dimension d. Then for every neighborhood W of x, there is a point\nz ∈ W ∩ red−1 (η), a neighborhood U of z contained in W , and an irreducible d-dimensional\nZariski-closed subspace Y ⊂ U containing z.\nRemark 4.2. In the situation of the theorem, any Zariski-closed subspace Y ⊂ U with\nz ∈ Y has dimension bounded below by d. This can be seen as follows. For a point z of\na k-analytic space Z we set\n                                                                    \u0001\n                                  f(z)/ek) + dimQ (|H (z)|/|k|) ⊗Z Q .\n                  dk (z) = tr.deg(H\nIt is a fact [Duc18, 1.4.6, A.4.11] that dim(Z) = supz∈Z dk (z). Taking Z = Y and z ∈ Y as\nin the theorem, we have a canonical inclusion κ(η) ,→ H   f(z), where κ(η) is the residue\nfield of η. In particular,\n                                           f(z)/ek) ≥ tr.deg(e\n                 dim(Y ) ≥ dk (z) ≥ tr.deg(H                 κ(η)/ek) = d.\n     We will use the following lemma in the proof.\nLemma 4.3. Let F /ek be a finitely generated field extension of transcendence degree d. There\nexists a finitely generated field extension L/k of transcendence degree d equipped with an\n                                                                                  ∼\nabsolute value extending the given absolute value on k and a ek-isomorphism eL −→ F .\nProof. Let K be the field of rational functions k(x 1 , . . . , x d ) endowed with the Gauss ab-\nsolute value. The residue field of K is equal to ek(x 1 , . . . , x d ). Choosing a transcendence\nbasis for F /ek, we obtain a ek-homomorphism K      e → F . Since F /ek is finitely generated of\ntranscendence degree d, it follows that [F : K     e ] < ∞. Choose an algebraic closure K a\n                                     a\nof K and an absolute value on K extending the Gauss absolute value on K. Noting that\nfa is algebraically closed, we choose a K\nK                                            e -homomorphism F → K        fa . Replacing F with its\nimage in K fa , we are reduced to the following statement:\n    (*) Let K be a field, let K a be an algebraic closure endowed with a non-Archimedean\n         absolute value, and let F /K  e be a finite subextension of K    e a /K\n                                                                               e . Then there exists\n                                           a          e\n         a finite subextension L/K of K /K with L = F .\n   Arguing by induction on m = [F : K   e ], we may assume that F = K          e for some primitive\n                                                                           e (β)\n          e           e                                  e\nelement β ∈ F . Let f be the minimal polynomial of β over K         e . Choose a monic polynomial\n       ◦             e            ◦◦\nf ∈ K [x] lifting f modulo K . Let β1 , . . . , βm be the roots of f in K a (counted with\n\f      ON SEMIPOSITIVE PIECEWISE LINEAR FUNCTIONS IN NON-ARCHIMEDEAN ANALYTIC GEOMETRY                 11\n\nmultiplicity), so that f = (x − β1 ) · · · (x − βm ) ∈ K a [x]. By Gauss’ Lemma, each βi is\ncontained in (K a )◦ , so fe = (x − βe1 ) · · · (x − βem ) in K\n                                                              fa [x]. In particular, we have βe = βei for\nsome i. Set β = βi and L = K(β), so that F ⊂ eL . Again by Gauss’ Lemma, the polynomial\n f is irreducible over K, so m = [L : K]. Then m = [F : K              e ] ≤ [eL : K\n                                                                                   e ] ≤ [L : K] = m, so\neL = F , as desired.                                                                                   \u0003\nProof of Theorem 4.1. First we reduce to the case W = X , which we call the global version\nof Theorem 4.1. By shrinking W , we may assume that W is a strictly affinoid neighbor-\nhood of x. By Raynaud’s theorem [Bos14, Theorem 8.4.3] and [BL93b, Corollary 5.4(b)],\nthere is an admissible formal blowing up X′ → X and a formal open subset W′ ⊂ X′ with\nW′η = W . We get an induced morphism W′s → Xs of schemes of finite type over ek. The\nfiber over η is a scheme of finite type over the residue field κ(η). This fiber contains\nredX′ (x), so it is non-empty; thus it contains a closed point η′ . We have\n           tr.deg(κ(η′ )/ek) = tr.deg(κ(η′ )/κ(η)) + tr.deg(κ(η)/ek) = 0 + d = d.\nFrom the global version of Theorem 4.1 as applied to the formal model W′ of W and to\nthe point η′ ∈ W′s , we deduce that there exists z ∈ W with redX′ (z) = η′ , a neighborhood\nU of z in W , and an irreducible d-dimensional Zariski-closed subspace Y ⊂ U containing\nz. Since X′ → X maps redX′ (z) to redX (z), we conclude that redX (z) = η. This proves\nthat Theorem 4.1 follows from its global version.\n   We assume from now on that W = X . The residue field κ(η) is a finitely generated field\nextension of ek of transcendence degree d. By Lemma 4.3, there is a finitely generated field\nextension L/k of transcendence degree d endowed with an absolute value extending the\n                                               ∼\ngiven one on k and a ek-isomorphism ρ : eL −→ κ(η). Choose an integral affine k-scheme\nT of dimension d with function field L. Since the points of T an are those multiplicative\nseminorms on O (T an ) which extend the given absolute value on k, the absolute value on\nL defines a point t ∈ T an . Note that H (t) is the completion of L and that H  f(t) = eL .\nReductions of germs. Let z be a point of the tube red−1 (η). Since red(z) = η, there is\na canonical homomorphism κ(η) ,→ H       f(z). Let PHf(z)/ek be the Riemann–Zariski space of\nthe residue field extension H  f(z)/ek. The closure E ⊂ Xs of η is a ek-variety, and there\n                                       2\n\nis a canonical morphism ek(E) = κ(η) ,→ H    f(z) over ek, where ek(E) is the function field\nof E. In such a situation, we call E a premodel of H     f(z) over ek.3 Let PHf(z)/ek {E} be the\nset of valuations in PHf(z)/ek with center in E. This is a quasi-compact open subset of\nPHf(z)/ek depending only on the germ (X , z); it is called Temkin’s reduction of the germ and\nis denoted red(X , z).\n                                                                             ∼\n   The identification Hf(t) = eL composed with the isomorphism ρ : eL −→ κ(η) and the\ncanonical inclusion κ(η) ,→ H   f(z) yields a homomorphism H      f(t) ,→ H f(z). Restriction\nof valuations induces a morphism of Riemann–Zariski spaces π: PHf(z)/ek → PHf(t)/ek . The\n                                                           ∼\nisomorphism ρ also induces an isomorphism H        f(t) −→ ek(E), so we may regard E as a\n(pre)model of H  f(t)/ek, which defines a quasi-compact open subset P f e {E} ⊂ P f e .\n                                                                                 H (t)/k         H (t)/k\n\n  2\n   For a summary about Riemann–Zariski spaces, we refer to [CD12, 6.1].\n  3\n   For a model, we would require that the embedding ek(E) ,→ H\n                                                             f(z) be an isomorphism.\n\f12                                   W. GUBLER AND J. RABINOFF\n\nBy construction and the fact that a valuation always extends along field extensions, we\nhave π−1 (PHf(t)/ek {E}) = PHf(z)/ek {E}. Note that this is true for any z ∈ red−1 (η).\n  The analytification of a scheme of finite type over k is boundaryless [Ber90, The-\norem 3.4.1], so by [Tem00, Theorem 4.1], we have red(T, t) = PHf(t)/ek . Temkin has\nshown [Tem00, Theorem 2.4] that reduction of germs establishes a bijective correspon-\ndence between strictly analytic domains of the germ (T, t) and non-empty quasi-compact\nopen subsets of red(T, t) = PHf(t)/ek . Let (T0 , t) be the strictly analytic domain with germ\nequal to PHf(t)/ek {E}. We fix a strictly affinoid domain T0 ⊂ T representing this germ. The\nprevious paragraph gives\n(4.3.1)                          π−1 (red(T0, t)) = red(X , z).\n  The special fiber of the H (t)◦-formal scheme X′ = X⊗     b k◦ H (t)◦ is equal to Xs ⊗ek eL , so\n                        ∼\nthe isomorphism ρ : eL −→ κ(η) induces a canonical eL -rational point η′ ∈ X′s lying over η.\nSince the reduction map is an anti-continuous surjective map [GRW17, Proposition 2.17]\nand {η′ } is closed, the tube Ω = red−1 (η′ ) is a non-empty open subset of the H (t)-\nanalytic space X′η = X ⊗ b k H (t). Let p1 : X ×k T0 → X and p2 : X ×k T0 → T0 be the\nprojection morphisms. We may identify X ⊗    b k H (t) with the fiber p2−1 (t).\nBoundarylessness. Claim: Both p1 and p2 are boundaryless at any point v ∈ Ω.\n   In other words, we claim that Ω ⊂ Int(X ×k T0 /T0 ) ∩ Int(X ×k T0 /X ). Fix v ∈ Ω. By\ndefinition of the tube Ω, the reduction of v in X′s is equal to η′ , and p2 (v) = t. Let\nz = p1 (v) ∈ X , and let π1 : PHf(v)/ek → PHf(z)/ek (resp. π2 : PHf(v)/ek → PHf(t)/ek ) be the map\nof Riemann–Zariski spaces corresponding to the ek-algebra homomorphism p1∗ : H              f(z) →\nH                 f(t) → H\n f(v) (resp. p∗ : H         f(v)). By a result of Temkin [Tem00, Theorem 4.1], showing\n               2\nthat p1 and p2 are boundaryless at v is equivalent to proving that\n(4.3.2)             π−1\n                     1\n                        (red(X , z)) = red(X ×k T0 , v) = π−1\n                                                           2\n                                                              (red(T0 , t)).\nBy [Tem04, Proposition 4.6], which is easily adapted to non-graded reductions of germs\nin the case of good strictly analytic spaces, we have\n(4.3.3)              red(X ×k T0 , v) = π−1\n                                         1\n                                            (red(X , z)) ∩ π−1\n                                                            2\n                                                               (red(T0, t))\ninside of PHf(v)/ek , so (4.3.2) amounts to the equality π−1\n                                                          1\n                                                             (red(X , z)) = π−1\n                                                                             2\n                                                                                (red(T0, t)).\n                                                                             ◦\n                                                                   b k◦ H (t) → X, we have\n   By functoriality of the reduction map as applied to p1 : X⊗\n                                               ′\nred(z) = red(p1 (v)) = p1 (red(v)) = p1 (η ) = η. Thus there are canonical homomor-\nphisms κ(η) → H      f(z) and κ(η′ ) → H f(v) making the right square commute in the fol-\nlowing diagram of field extensions:\n\n                                                 f(v)\n                                                 H            p1∗\n                                             →            →\n                                                              ←\n                                                  →\n\n\n\n\n                                   p2∗                              f(z)\n                                                                    H\n(4.3.4)\n                                                  ←\n\n\n\n\n                                                                     →\n\n\n\n\n                                                 κ(η′ )\n                                 ←\n\n\n\n\n                                         σ                    ι\n                                             →\n                                                          →\n                                                                     ←\n\n\n\n\n                                         ←\n                                                   ∼\n                                                              ←\n                              f(t)\n                              H\n                                         ←\n                                                   ρ          → κ(η)\n\f     ON SEMIPOSITIVE PIECEWISE LINEAR FUNCTIONS IN NON-ARCHIMEDEAN ANALYTIC GEOMETRY              13\n\nHere, the map σ : H    f(t) → κ(η′ ) is induced by the fact that η′ is a point of the H     f(t)-\n           ′                        ′                               ′\nscheme Xs , and ι : κ(η) → κ(η ) is induced by the fact that η is lying over η. By (4.3.1),\nwe have that π−1 (red(T0 , t)) = red(X , z). Recall that π: PHf(z)/ek → PHf(t)/ek is induced\nby the composition of the arrow on the bottom with the arrow on the right. The map\nπ2 : PHf(v)/ek → PHf(t)/ek is induced by the extension on the left, and π1 : PHf(v)/ek → PHf(z)/ek is\ninduced by the extension on the top right. If the outer part of the diagram is commutative\nthen we have π2 = π ◦ π1 , such that (4.3.1) yields π−1    2\n                                                             (red(T0 , t)) = π−1\n                                                                               1\n                                                                                 (red(X , z)).\n    The homomorphism κ(η ) → H   ′      f(v) comes from the reduction map red: X′ → X′\n                                                                                          η         s\n                                f   ◦           ′                     f\nassociated to the formal H (t) -scheme X , so it is a map of H (t)-algebras. This shows\nthat the upper left triangle is commutative. It remains to see that the bottom triangle is\ncommutative. Recall that η′ is the image of the map Spec(H      f(t)) → Xs ⊗ek H f(t) defined by\n                                                                                                  ∼\nr ⊗1, where r : Spec(H     f(t)) → Xs is the composition of the map (ρ −1)∗ : Spec(H    f(t)) −→\nSpec(κ(η)) with the canonical map Spec(κ(η)) → Xs . The morphism r ⊗ 1 induces\naH  f(t)-homomorphism ϕ : κ(η′ ) → H         f(t). As σ is induced by the structure map of\n  ′            f\nXs = Xs ⊗ek H (t), we have ϕ◦σ = 1, so ϕ and σ are inverse isomorphisms. The definition\nof r ⊗ 1 shows that the triangle\n\n                                                   κ(η′ )\n                                           ϕ                       ι\n(4.3.5)                                    →\n                                               ←              →←\n                                   f(t)\n                                   H\n                                           →\n                                                               ← κ(η)\n                                                       ρ −1\n\n\ncommutes. We conclude that all maps in the triangle (4.3.5) are isomorphisms. The\ncommutativity of the bottom triangle of (4.3.4) now follows readily from ϕ ◦ ι = ρ −1 and\nfrom ϕ −1 = σ. This concludes the proof that p1 and p2 are boundaryless at v.\n\nFlat, quasi-finite multisections. Since fibers in the category of analytic spaces have the\ninduced topology [Ber93, 1.4], there is an open subset V ⊂ X ×k T0 with V ∩ p2−1 (t) = Ω.\nSince X is flat over k, it is clear that X ×k T0 is flat over T0 (in the sense of [Duc18]), so\nV → T0 is again flat. By a theorem of Ducros on multisections [Duc18, Theorem 9.1.2(B)]\n(with Y = V, X = T0 , F = OV , y = any point of Ω, and x = t; here we use that p2 is\nboundaryless along Ω), there is a strictly k-affinoid space S and a commutative triangle\n\n                                                              V\n                                                              ←\n\n\n\n\n                                                   ψ      →\n                                                              →\n\n\n\n\n                                               ←\n\n                                                    ϕ→\n                                               ←\n                                           S                  T0\n\nsuch that ϕ is a finite at a point s ∈ ϕ −1 (t). Shrinking S and T0 if necessary, we may\nand do assume that ϕ is finite [Ber93, Proposition 3.1.4(b)]. In particular, we have\ndim(S) ≤ dim(T0) = d. Since ψ(s) lies over t ∈ T0 , we have ψ(s) ∈ V ∩ p2−1 (t) = Ω. Set\nv = ψ(s) and z = p1 (v) ∈ X . As above, the reduction of z is equal to η, so\n\n                                       f(z)/ek) ≥ tr.deg(κ(η)/ek) = d,\n                       dk (z) ≥ tr.deg(H\n\f14                                 W. GUBLER AND J. RABINOFF\n\nwhere the second inequality holds because κ(η) ⊂ H   f(z). Since z = p1 (v) = (p1 ◦ ψ)(s),\nwe have dk (s) ≥ dk (z) ≥ d. Since dim(S) = sups′ ∈S dk (s′ ) ≤ d, it follows that dim(S) =\ndk (s) = d.\n   Composing p1 with ψ: S → V ⊂ X ×k T0 gives a map p1 ◦ ψ: S → X . We claim that\nSz := (p1 ◦ ψ)−1(z) has dimension zero. If not, then dim(Sz ) ≥ 1, so there exists s′ ∈ Sz\nwith dH (z) (s′ ) ≥ 1. But then\n\n                       dk (s′ ) = dH (z) (s′ ) + dk (z) ≥ 1 + dk (z) ≥ 1 + d\n\n(the first equality is additivity in towers), which contradicts sups′ ∈S dk (s′ ) = dim(S) = d.\n   We claim now that p1 ◦ ψ is finite at s. Since s is isolated in its fiber, by [Ber93,\nProposition 3.1.4(c)] it is enough to show that p1 ◦ ψ is boundaryless at s. Since ϕ : S →\nT0 is boundaryless (it is finite) and since ψ: S → V factors ϕ, it follows from [Ber90,\nProposition 3.1.3(ii)] that ψ is boundaryless. We showed before that p1 is boundaryless\nat v, and the composition of two boundaryless morphisms is again boundaryless, so p1 ◦ψ\nis boundaryless, hence finite, at s.\n   Again by [Ber93, Proposition 3.1.4(b)], there exist affinoid neighborhoods U ′ of s and\nU of z such that p1 ◦ ψ induces a finite morphism U ′ → U. The image p1 ◦ ψ(U ′ ) is\ntherefore a Zariski-closed d-dimensional subspace Y of U containing z. Replacing Y be\nan irreducible component containing z (see [Duc18, §1.5]), we get the theorem. Here\nwe use that the dimension of a Zariski-closed subspace containing z is bounded below\nby d, as noted in Remark 4.2.                                                                \u0003\n\n   Let X be an analytic space and let x ∈ X . The infimum of the integers dimk {x}VZar\nfor V running through the set of analytic neighborhoods of x in X is called the central\ndimension of x in X and is denoted centdim(X , x) [Duc18, Definition 3.2.2]. For any\nanalytic neighborhood V of x in X one has dimk {x}VZar ≥ dk (x), as noted in Remark 4.2;\nit follows that centdim(X , x) ≥ dk (x).\n   A point has central dimension zero if and only if it is a rig-point. The following Corol-\nlary thus generalizes the fact that the rig-points are dense in an analytic space.\n\nCorollary 4.4. Let X be a good, strictly k-analytic space of pure dimension n. Then for any\nnonnegative integer d ≤ n, the set\n                         \b\n                           x ∈ X : centdim(X , x) = dk (x) = d\n\nis dense in X .\n\nProof. Let x ∈ X , let V be a strictly affinoid neighborhood of x, and let W be the interior\nof V in X ; this is an open neighborhood of x in X . Choose an admissible formal model V\nof V . The special fiber Vs has dimension n. Let E ⊂ Vs be an irreducible d-dimensional\nclosed subset and let η be its generic point. We apply Theorem 4.1 to V and W to get a\nneighborhood U of z in W , a point z ∈ W with reduction η, and a d-dimensional Zariski-\nclosed subspace Y ⊂ U with z ∈ Y . It follows that centdim(X , z) ≤ d, and equality holds\nby Remark 4.2.                                                                            \u0003",
  "c4f861b42719d76be8cab3099618d3c7a04c8440524bab471915834df5b5c92e": "                             5. SEMIPOSITIVE R-PL FUNCTIONS\n   Let k be a non-trivially valued non-Archimedean field. We consider a good, strictly\nk-analytic space X . We refer to 2.5 for the definition of PL functions. Recall from the in-\ntroduction that an R-PL function u: X → R is called semipositive at x ∈ X if the associated\nresidue line bundle Lu (x) ∈ Pic(red(X , x))R is nef, where we refer to [GJR21, 6.16–6.19]\nfor residue line bundles. Equivalently, there is a strictly affinoid neighbourhood U of x\nsuch that u = hL for a formal k◦ -model (U, L) of (U, OU ) with L nef [GJR21, Proposition\n7.1].\n   We will show first that for an R-PL function on a smooth curve, semipositivity is the\nsame as subharmonicity in the sense of Thuillier’s thesis [Thu05, Définition 3.1.5]. Re-\ncall that Thuillier defines a subharmonic function on a smooth k-analytic curve X as a\nsemicontinuous function u: X → R ∪ {−∞} which is not identically −∞ on any con-\nnected component of X and which has the property that for every harmonic function h\non a strictly affinoid domain U of X with u|∂ U ≤ h|∂ U , we have u|U ≤ h.\n\nProposition 5.1. Let X be a smooth, strictly k-analytic curve and let u: X → R be an R-PL\nfunction. Then u is subharmonic at x ∈ X in the sense of Thuillier if and only if Lu (x) is nef.\n\nProof. First we treat the case when k is algebraically closed. As explained in 2.5, there\nexists a compact strictly analytic neighborhood U of x in X , a formal k◦ -model U of U,\nand a formal model L of OU such that u|U = hL . Since k is algebraically closed, we may\nassume that the special fiber Us is reduced, which implies that U is covered by formal\naffines of the form Spf(A ◦ ) for a strictly k-affinoid algebra A [GJR21, §2.4]. It follows\nfrom [Ber90, Proposition 2.4.4] that for every irreducible component Y of Us , there is a\nunique point ξY ∈ U reducing to the generic point of Y . In the formalism of real valued\nforms and currents on Berkovich spaces [CD12], it is well known that d′ d′′ [u]|U is the\ndiscrete measure on U supported on the points ξY of U for Y an irreducible component\nof Us , with multiplicity at ξY equal to degL (Y ). See [CD12, §6.9] for a more general\nstatement. Wanner showed that subharmonicity of u on U is equivalent to the positivity\nof the current d′ d′′ [u]: see [Wan19, Theorems 1 and 2] and use the fact that X is locally\nalgebraic [vdP80]. Thus Ls is nef if and only if u is subharmonic on U. Suppose that u is\nsubharmonic at x. Shrinking U, we may assume that u is subharmonic on U. This implies\nthat Ls is nef, so it follows from [GJR21, Proposition 7.1] that Lu (x) is nef. Conversely, if\nLu (x) is nef, then by [GJR21, Proposition 7.1], we may shrink U so that Ls is nef, which\nas above implies that u is subharmonic on U.\n   It remains to show that subharmonicity of u at x and numerical effectivity of Lu (x)\ncan be checked after extending scalars to the completion of an algebraic closure K =\n(k)∧ . By [GJR21, Proposition 7.6(2)], one can check that Lh (x) is nef after base change\nto K. The same is true for subharmonicity: this follows directly from Thuillier’s definition\nand the fact that the base change of a harmonic function remains harmonic [Thu05,\nProposition 2.3.18].                                                                       \u0003\n\n  Our next goal is a characterisation of semipositive R-PL functions by restriction to\nsubcurves as in the complex case. We need the following characterization of boundary\npoints:\n\f16                                W. GUBLER AND J. RABINOFF\n\n5.2. Let X be an admissible formal k◦ -scheme and let x ∈ Xη . Then x ∈ Int(X ) = X \\ ∂ X\nif and only if the closure of redX (x) is a proper ek-scheme. This follows from [CD12,\nLemme 6.5.1] in the separated case and from [Vil21, Corollary A.4] in general.\nTheorem 5.3. Let X be a good, strictly k-analytic space, and let h: X → R be an R-PL\nfunction. For x ∈ X , the following conditions are equivalent.\n    (1) The function h is semipositive at x.\n    (2) There is a neighborhood W of x such for every strictly analytic neighborhood U ⊂ W\n        of x and every Zariski-closed curve C in U, the restriction h|C is semipositive.\nProof. Since semipositivity is an open property that is stable under pullback [GJR21,\nProposition 7.6], it is clear that (1) yields (2).\n   Assume that h satisfies (2). By shrinking W , we may assume that W is a strictly affinoid\nneighborhood of x and that there is a formal model W of U and a model L of OW on W\nwith coefficients in R such that h = hL on W . Let Y ⊂ Ws be a curve which is proper over\nthe residue field ek. To prove semipositivity at x, it is enough to show that degL (Y ) ≥ 0.\n   Choose any point y ∈ W reducing to the generic point η of Y . By Theorem 4.1 as\napplied to X = W and X = W, there exist z ∈ W with redW (z) = η, a neighborhood U\nof z in W , and an irreducible 1-dimensional Zariski-closed subspace C of U containing\nz. By shrinking U, we may assume that U is strictly affinoid. By results of Bosch and\nLütkebohmert [Bos14, Theorem 8.4.3] [BL93b, Corollary 5.4(b)], there is a formal model\nU of U and a morphism π: U → W extending the inclusion U ,→ W on generic fibers. Let\nC be the formal closure of C in U. This is an admissible formal model of C whose special\nfiber Cs is a closed 1-dimensional subscheme of Us containing η′ = redU (z). Functoriality\nof reductions shows that π(η′ ) = η, so the closure Y ′ of η′ is a curve mapping to Y .\nSince the closure of η in Ws is the proper curve Y , we conclude from 5.2 that z ∈ W \\\n∂ W . The boundary ∂ U is the union of ∂ W ∩ U with the topological boundary of U in\nW [Ber90, Proposition 3.1.3], so since U is a neighborhood of z in W , we have z ∈ U \\∂ U.\nApplying 5.2 to U and its formal model U shows that Y ′ is proper as well. Therefore,\nthe map Y ′ → Y is finite and surjective. Note that Y ′ is an irreducible component of Cs .\nApplying (2) to U and C, we have that h|C is semipositive, and so we deduce from [GJR21,\nLemma 7.4] as applied to (π∗L)|C that degπ∗ L (Y ′ ) ≥ 0. The projection formula then shows\ndegL (Y ) ≥ 0, as required.                                                                \u0003\n   To apply results from Thuillier’s thesis [Thu05], we would like to use only smooth an-\nalytic curves. To give a variant of the above result suitable for this purpose, we introduce\nthe following notations:\n   For a real function h on X and an analytic field extension F of k, we denote by h F\nthe induced function on the base change X F = X ⊗     b k F of X . We call an R-PL function\nh pluriharmonic if ±h are both semipositive. A strictly k-analytic space X is called rig-\nsmooth if the sheaf of Kähler differentials, considered on the G-topology, is locally free of\nrank equal to the local dimension. The space X is smooth if and only if X is rig-smooth and\nboundaryless. See [Duc18] for details (Ducros calls rig-smooth spaces quasi-smooth).\nCorollary 5.4. Let X be a good, strictly k-analytic space and let h: X → R be an R-PL\nfunction. Then the following conditions are equivalent:\n\f     ON SEMIPOSITIVE PIECEWISE LINEAR FUNCTIONS IN NON-ARCHIMEDEAN ANALYTIC GEOMETRY        17\n\n   (1) The function h is semipositive (resp. pluriharmonic).\n   (2) There is an algebraically closed analytic field extension F of k such that for every\n       rig-smooth analytic curve C over F and every morphism ϕ : C → X F , the function\n       h F ◦ ϕ is semipositive (resp. harmonic) on C.\n   (3) There is an algebraically closed analytic field extension F of k such that for every\n       smooth analytic curve C over F and every morphism ϕ : C → X F , the function h F ◦ϕ\n       is semipositive (resp. harmonic) on C.\n\n   If (2) or (3) is true for an algebraically closed analytic field extension F of k, then\nit is true for all analytic field extensions. This follows from Corollary 5.4 and Propo-\nsition [GJR21, Proposition 7.6(2’)] which allows to check semipositivity over any field\nextension.\n\nProof. It is enough to prove the claim for semipositive functions, as h is pluriharmonic if\nand only if h and −h are semipositive. Since semipositivity is stable under pullback and\nextension of scalars [GJR21, Proposition 7.6], clearly (1) yields (2). Since a smooth an-\nalytic curve is just a boundaryless rig-smooth curve, it is clear that (2) yields (3). In fact,\nthese two conditions are equivalent as an R-PL function is automatically semipositive in\nevery boundary point y of an analytic curve C. Indeed, it follows from 5.2 that red(C, y)\nis non-proper and hence there is no condition for semipositivity at y.\n   It remains to show that that (2) yields (1). Assume that (2) holds. By base change\nusing [GJR21, Proposition 7.6(2’)], we may assume that k = F . Let x ∈ X and let U be\na strictly analytic neighborhood of x. For any Zariski-closed curve Y in U, we will show\nthat h|Y is semipositive. Replacing Y by Yred and using [GJR21, Proposition 7.6(3’)], we\nmay assume that Y is reduced. Let ϕ : C → Y be the normalization of Y (see [Ber90]\nbefore Proposition 3.1.8). Then C is a rig-smooth curve because k is perfect (it is alge-\nbraically closed). By (2), the function h ◦ ϕ is semipositive on C. Since the normalization\nmorphism is finite and surjective, it follows from [GJR21, Proposition 7.6(1’)] that h|Y is\nsemipositive. By Theorem 5.3, we conclude that h is semipositive at x. Since x was an\narbitrary point of X , we get (1).                                                           \u0003\nCorollary 5.5. Let X be a good, strictly k-analytic space and let Λ be either Z or Q. Let\nh1 , h2 : X → R be semipositive Λ-PL functions. Then max(h1 , h2 ) is a semipositive Λ-PL\nfunction.",
  "874dd983a3cbaf8744b9beaf27b49bcf2305591c97e411699dfd91d6b420cceb": "Théorème 3.2. Soit X un espace k-analytique compact et Γ-strict de dimension d,\net soit f = (f1 , . . . , fn ) une famille de fonctions analytiques inversibles sur X ;\nnotons |f | l’application (|f1 |, . . . , |fn |) de X vers (R∗+ )n . Posons c = (Q, (|k ∗ | · Γ)Q ).\n1) L’image |f |(X) est un c-polytope de (R∗+ )n , qui est de dimension inférieure ou\n   égale à d.\n2) L’image |f |(∂X) est contenue dans un c-polytope de (R∗+ )n qui est de dimension\n   inférieure ou égale à d − 1 ; lorsque X est aﬃnoı̈de |f |(∂X) est elle-même un c-\n   polytope de (R∗+ )n de dimension inférieure ou égale à d − 1.\n    Démonstration. La seconde assertion se déduira de la première.\n(3.2.1) Preuve de 1) : réduction à une situation algébrique. On peut supposer\nque X est aﬃnoı̈de et irréductible, et l’on procède alors par récurrence sur d. Si d = 0\nil n’y a rien à démontrer. Supposons que d > 0 et que 1) est vraie en dimension < d.\n     Le théorème à établir est purement topologique. On peut donc supposer k parfait\n(en étendant les scalaires au complété de la clôture radicelle de k), et X réduit (en\nle remplaçant par Xred ). L’espace X est alors génériquement quasi-lisse. Soit Y son\nlieu de non-quasi-lissité. C’est un fermé de Zariski de X dont toutes les composantes\nirréductibles sont de dimension < d. Par hypothèse de récurrence, |f |(Y ) est un\nc-polytope de (R∗+ )n de dimension ⩽ d − 1. Son image réciproque |f |−1 (|f |(Y )) est\nun domaine analytique Γ-strict de X contenant Y . Comme Y \b→ X est sans bord, Y\nest contenu dans l’intérieur topologique de |f |−1 (|f |(Y )). Ce dernier apparaı̂t ainsi\ncomme un voisinage de Y dont l’image par |f | est un c-polytope de dimension\n⩽ d − 1.\n     Soit x ∈ X − Y . Comme X est quasi-lisse en x, le lemme 0.21 assure l’existence\nd’un voisinage aﬃnoı̈de V de x dans X, et d’une k-variété aﬃne X de dimension d,\ntelle que V s’identiﬁe à un domaine aﬃnoı̈de Γ-strict de X an (on peut imposer à X\nd’être lisse, mais nous ne nous en servirons pas).\n     Par compacité de X, on se ramène ﬁnalement au cas où X lui-même est est un\ndomaine aﬃnoı̈de Γ-strict de l’analytiﬁcation X an d’une k-variété algébrique X\naﬃne de dimension d.\n     Écrivons X ≃ Spec A où A est une k-algèbre de type ﬁni, et soit (a1 , . . . , ar )\nun système de générateurs de A. Il existe R ∈ Γ · |k ∗ | tel que X soit contenu\ndans le domaine aﬃnoı̈de W de X an déﬁni par les conditions |ai | ⩽ R. En vertu\ndu théorème de Gerritzen-Grauert (0.20.7), le domaine X est réunion ﬁnie de\ndomaines Γ-rationnels de W ; il suﬃt dès lors de traiter le cas où X est lui-même\nun domaine Γ-rationnel de W .\n     Il est alors déﬁni par une conjonction d’inégalités de la forme |gi | ⩽ λi |h| où les λi\nappartiennent à Γ et où (g1 , . . . , gr , h) engendre l’idéal des fonctions analytiques\nsur W . Cette dernière condition implique que h ne s’annule pas sur X (tout zéro\nde h sur X est un zéro commun à h et aux gi ), et l’on peut donc, par compacité,\n                                            1250007-40\n\f                            Espaces de Berkovich, polytopes, squelettes et théorie des modèles\n\n\nrajouter une condition de la forme |h| ⩾ r à la déﬁnition de X, où r est un élément\nconvenable de (Γ · |k ∗ |)Q . Il est dès lors immédiat que V ne change pas si l’on\nperturbe un peu les gi et h ; on peut par conséquent supposer que toutes ces\nfonctions appartiennent à A.\n    L’anneau des fonctions de la forme a/h\u0005 , où a ∈ A, et \u0010 ⩾ 0, est dense dans\nl’anneau des fonctions de X. Cela permet de supposer, quitte à remplacer X\npar D(h), à remplacer gi par gi /h et à approcher convenablement chacune des fi ,\nque fi ∈ A pour tout i et que h = 1.\n(3.2.2) Nature c-polytopale de |f |(X) dans le cas algébrique. Soit (F, |.|) une\nextension valuée de k (on ne suppose pas que le groupe ordonné |F ∗ | est de\nrang 1). On peut donner un sens naturel à la notation X(F ), coı̈ncidant avec sa\nsigniﬁcation usuelle lorsque F est un corps ultramétrique complet : c’est le sous-\nensemble de X (F ) formé des points P tels que |gi (P )| ⩽ λi pour tout i.\n    Le théorème 1.2 assure l’existence d’un sous-foncteur fermé et déﬁnissable D\nde GnΓ·|k∗ | , de dimension majorée par d (les notations et déﬁnitions sont celles de\n0.32 et sq.) tel que\n                             |f |(X(F )) = D(|F ∗ |) ⊂ |F ∗ |n\npour tout F ∈ Ck,Γ·|k∗ | .\n     Si F est une extension ultramétrique complète et algébriquement close de k\nmunie d’un |k ∗ |-isomorphisme |F ∗ | ≃ R∗+ , tout point P de X(F ) déﬁnit un point x\nde l’espace k-aﬃnoı̈de X, et |f |(x) = |f |(P ) ∈ (R∗+ )n .\n     Réciproquement si x ∈ X il existe une extension complète et algébriquement\nclose F de H (x) et un |H (x)∗ |-isomorphisme |F ∗ | ≃ R∗+ , et x est alors induit par\nun F -point canonique de X.\n     En conséquence, le compact |f |(X) est le sous-ensemble D(R∗+ ) de (R∗+ )n , ce\nqui achève de prouver 1).\n                                                                                  \u0005\n(3.2.3) Démonstration de l’assertion 2. Si X s’écrit comme une réunion ﬁnie Xi\noù les Xi sont aﬃnoı̈des et Γ-stricts, son bord est contenu dans la réunion des bords\ndes Xi . On peut donc supposer que X est aﬃnoı̈de, auquel cas le résultat découle\nde l’assertion 1) déjà établie et du lemme 3.1.\n(3.3) Remarque. Faute d’avoir réussi à exhiber une description suﬃsamment\nmaniable de ∂X en général, l’auteur ignore s’il peut arriver que |f |(∂X) ne soit\npas un polytope, lorsque X n’est pas aﬃnoı̈de. Il serait évidemment intéressant de\ndisposer d’un tel exemple — ou, au contraire, d’une preuve que |f |(∂X) est toujours\nun polytope.",
  "0c4ed10aa0e6bb8a9cdc7c011be276fcc6f1a487124cdb57594cc0d89d5c71a3": "Lemme 5.5.2]).\n   By [CD12, Lemme 5.5.3], a smooth function h is psh if and only if every x ∈ X has a\n                                                                                r,an\ncompact strictly analytic neighbourhood V with a moment map ϕ : V → Gm               such that\nh|V = u◦ϕtrop for a continuous function u on ϕtrop (V ) which restricts to a convex function\non each face. This characterization shows that smooth psh functions admit pull-backs\nwith respect to morphisms.\nTheorem 7.14. Let X be a good separated strictly analytic space over K and let h: X → R\nbe a semipositive R-PL function. Then h restricts to a psh function on X \\ ∂ X .\nProof. By restriction to X \\ ∂ X , we may assume that X is boundaryless. The claim is local\nin X and so we may assume that h is a uniform limit of R-PL LFS functions hi on X by\nusing Proposition 7.10. It follows from 7.9 and from [CD12, Corollaire 6.3.2] that an\nR-PL locally Fubini–Study function is locally a uniform limit of smooth psh functions and\nhence hi is psh. For any positive form ω ∈ Asm,c (X ), we deduce from uniform convergence\nthat                                 Z                  Z\n                      〈ω, d′ d′′ [h]〉 =        h · d′ d′′ ω = lim       hi · d′ d′′ ω ≥ 0.\n                                                              i\n                                           X                        X\n  6\n    Currents in analysis work well only in the boundaryless case, as otherwise there are disturbing residues\nalong the boundary. Note that Chambert-Loir and Ducros also omit the boundary in their definition of\ncurrents [CD12, 4.2.2], as their currents act on smooth forms with compact support disjoint from the\nboundary.\n\f50                                W. GUBLER, P. JELL, AND J. RABINOFF\n\nWe conclude that h is psh.                                                                          \u0003\nCorollary 7.15. Let h be a harmonic function on a good separated strictly analytic space X\nover K. Then the restriction of the current d′ d′′ [h] to X \\ ∂ X is zero.\nProof. We may assume that X is boundaryless. It follows from Theorem 7.14 that h and\n−h are psh on X . By linearity in the irreducible components and by arguing locally, we\nmay assume that X is of pure dimension d. Let η ∈ Asm,c             d−1,d−1\n                                                                            (X ). Since d′ d′′ [h] is a\nsymmetric current on X , we have\n                           1                                             \u0001 1\n         〈η, d′ d′′ [h]〉 =    〈η, d′ d′′ [h]〉 + (−1)d−1 〈Jη, d′ d′′ [h]〉 = 〈ω, d′ d′′ [h]〉\n                           2                                                  2\nfor the symmetric form ω := η + (−1)d−1 Jη ∈ Asm,c       d−1,d−1\n                                                                 (X ). By Lemma 7.12, there are\n                             d−1,d−1\npositive forms ω1 , ω2 ∈ Asm,c (X ) such that ω = ω1 − ω2 . As h and −h are psh, we get\n                 2〈η, d′ d′′ [h]〉 = 〈ω1 , d′ d′′ [h]〉 − 〈ω2 , d′ d′′ [h]〉 = 0 − 0 = 0,\nproving the claim.                                                                                  \u0003\nRemark 7.16. In this section, we have focused on the concept of semipositive and har-\nmonic functions. In fact, all the results immediately transfer to Λ-PL metrics k k of a\nline bundle L over a good strictly analytic space X . Indeed, the choice of a local frame s\ngives rise to a Λ-PL function h := − log ksk, to which we can apply the above results. Then\nTheorem 7.14 yields that on a good separated strictly analytic space X every semipositive\nR-PL metric of L has a positive first Chern current c1 (L, k k) as defined in [CD12, 6.4.1].\nThe same holds for uniform limits of such metrics on L which includes all the metrics\nconsidered by Zhang [Zha95] over projective varieties.",
  "8e04c8c70067b9241eac60096b1d40f71432c02710482d42b86cda7b4327d64f": "L82@P2: Theorem 1.2.1. For any noetherian quasi-excellent generically reduced scheme\nL83@P2: X = X0 over Spec(Q) there exists a blow up sequence F(X): Xn 99K X0 such that\nL84@P2: the following conditions are satisfied:\nL85@P2: (i) the centers of the blow ups are disjoint from the preimages of the regular locus\nL86@P2: Xreg;\nL87@P2: (ii) the centers of the blow ups are regular;\nL88@P2: (iii) Xn is regular;\nL89@P2: (iv) the blow up sequence F(X) is functorial with respect to all regular morphisms\nL90@P2: X′ → X, in the sense that F(X′) is obtained from F(X) ×X X′by omitting all\nL91@P2: empty blow ups.",
  "d8b77b3db1f70b041281e41dae04484dbed2c36141832172abfcf7e3b7869c58": "L421@P9: 2.2.2. Blow up sequences. A price one has to pay for using a finer notion of blow ups\nL422@P9: is that the composition X′′ → X′ → X of blow ups cannot be considered as a blow\nL423@P9: up in a natural way: though X′′ → X is isomorphic to a blow up BlW (X) → X, it\nL424@P9: is not clear how to choose W canonically. Therefore we define a blow up sequence\nL425@P9: of length n to be a composition of n ≥ 0 blow ups Xn\nL426@P9: fn→ · · ·f2→ X1f1→ X0 with\nL427@P9: centers Vi֒→ Xi. In particular, a blow up sequence of length 0 is just the object\nL428@P9: X0 itself. Such sequence is called empty. It will be convenient to denote a blow up\nL429@P9: sequence as f : Xn 99K X0 and say that Vi’s are its centers. We stress that a blow\nL430@P9: up sequence is not defined by the morphism Xn → X even when we blow up regular\nL431@P9: schemes along regular centers, see [Kol, 3.33]. A sequence will be called contracted\nL432@P9: if all its blow ups are non-empty. Using dashed arrows we will sometimes split blow\nL433@P9: up sequences, e.g. f : Xn 99K Xi+1 → Xi 99K X0.",
  "0e83f63e3296a2fe2043512f2317647039a7010757aec51315752e217ac4c9d0": "L1526@P26: Lemma 4.1.3. (i) Each equicodimensional desingularization functor F defines a\nL1527@P26: compatible sequence {F≤d}d∈N of equicodimensional desingularizations up to codi\u0002mension d.\nL1528@P26: (ii) Conversely, assume that {F≤d}d∈N is a compatible sequence of equicodi\u0002mensional desingularizations up to codimension d, and for any scheme X from\nL1529@P26: QEp=0,reg and numbers e ≥ d the centers of F\nL1530@P26: ≤e\nL1531@P26: (X) of X-codimension > d are\nL1532@P26: Td-supported, where Td = F\nL1533@P26: ≤d\nL1534@P26: sing(X) is the unresolved locus of F\nL1535@P26: ≤d\nL1536@P26: (X). Then the\nL1537@P26: sequence {F≤d(X)}d∈N stabilizes for large d’s, and hence the sequence {F≤d}d∈N\nL1538@P26-27: gives rise to an equicodimensional desingularization functor F on QEp=0,reg.28 MICHAEL TEMKIN\nL1539@P27: Proof. The assertion of (i) was observed earlier. Assume given a sequence F\nL1540@P27: ≤d and\nL1541@P27: a scheme X as in (ii). The condition on the centers implies that F\nL1542@P27: ≤d\nL1543@P27: (X)|X\\Td =\nL1544@P27: F\nL1545@P27: ≤e\nL1546@P27: (X)|X\\Tdand hence Te ⊆ Td. Thus, T1 ⊇ T2 ⊇ T3 . . . and hence this sequence\nL1547@P27: stabilizes by noetherian induction. However, Tn is of codimension n, hence the only\nL1548@P27: possibility for stabilization is that Tn = ∅ for large enough n, and then the sequence\nL1549@P27: F\nL1550@P27: ≤d\nL1551@P27: (X) stabilizes for d ≥ n. \u0003",
  "33518fa382ca7543017cd847eec37abbc72a2fa03d9ace110dfc9b0942b4cf24": "L1693@P28: Proof of Theorem 1.2.1. By Lemma 4.1.3 it suffices to build a compatible sequence\nL1694@P28: of functors F\nL1695@P28: ≤d which provide an equicodimensional (resp. strong) desingulariza\u0002tion up to codimension d and such that the centers of F\nL1696@P28: ≤d of X-codimension d sit\nL1697@P28: over Td−1 = F\nL1698@P28: ≤d−1\nL1699@P28: sing . The construction will be done inductively, and we start with\nL1700@P28: empty F\nL1701@P28: ≤0\nL1702@P28: since generically reduced schemes are regular in codimension 0. Thus,\nL1703@P28: we can assume that the sequence F\nL1704@P28: ≤0\nL1705@P28: , . . . , F\nL1706@P28: ≤d−1\nL1707@P28: is already constructed, and our\nL1708@P28: aim is to construct F\nL1709@P28: ≤d\nL1710@P28: . First we will construct F\nL1711@P28: ≤d\nL1712@P28: (X) for a single scheme X, and\nL1713@P28: then we will check that the construction is functorial. The required sequence will\nL1714@P28: be obtained by extending the blow up sequence f = F\nL1715@P28: ≤d−1\nL1716@P28: (X): Xm 99K X0 = X\nL1717@P28: few times. To simplify notation, after each extension we will denote the obtained\nL1718@P28: blow up sequence as f : Xm 99K X0, but this should not cause any confusion. By\nL1719@P28: our assumption, Td−1 is a closed subset of X≥d, hence it has finitely many points of\nL1720@P28: codimension d, which are the generic points of the irreducible components of Td−1\nL1721@P28: of codimension d. Let T denote the set of these points.\nL1722@P28: Extension 0. We denote by T the Zariski closure of T with the reduced scheme\nL1723@P28: structure and extend f in the sense of Definition 4.2.2 by inserting g : BlT(X) → X\nL1724@P28: as the first blow up. As an output we obtain a blow up sequence F\nL1725@P28: ≤d\nL1726@P28: 0\nL1727@P28: (X): X′\nL1728@P28: m 99K\nL1729@P28: X′\nL1730@P28: 0 → X0 = X of length m + 1 where the first center (the inserted one) is regular\nL1731@P28: over a neighborhood of T . As agreed above, we set f = F\nL1732@P28: ≤d\nL1733@P28: 0\nL1734@P28: (X) and increase m\nL1735@P28: by one after this step. We claim that the scheme-theoretic preimage of T in each\nL1736@P28: Xi with i > 0 is a Cartier divisor Di. Indeed, this is obvious for D1 and for larger\nL1737@P28-29: i’s we use the following lemma.30 MICHAEL TEMKIN\nL1738@P29: Lemma 4.3.1. If X′ → X is a blow up and D ֒→ X is a Cartier divisor then the\nL1739@P29: locally principal closed subscheme D′ = D ×X X′ of X′is a Cartier divisor.\nL1740@P29: Proof. We can work locally on X, so let X = Spec(A), D = (f), and X′ be the blow\nL1741@P29: up along an ideal I ⊂ A. It is suffices to check the claim for a chart Spec(A[\nL1742@P29: I\nL1743@P29: a\nL1744@P29: ]) of\nL1745@P29: the blow up, where a ∈ I. Since f is a regular element of A, it is a regular element\nL1746@P29: of Aa and hence also a regular element of A[\nL1747@P29: I\nL1748@P29: a\nL1749@P29: ] ⊆ Aa. Thus, D′is a Cartier divisor\nL1750@P29: in X′. \u0003\nL1751@P29: Extensions 1, . . . , n. This step is needed only in the case of strong desingulariza\u0002tion (otherwise one can run it as well, but this would only unnecessarily complicate\nL1752@P29: the algorithm). The last n centers of F\nL1753@P29: ≤d\nL1754@P29: 0\nL1755@P29: (X) are regular over X≤d \\ T but do not\nL1756@P29: have to be so over T . We remedy this problems by n successive extensions. Let\nL1757@P29: us describe the i-th one. It obtains as an input a blow up sequence f = F\nL1758@P29: ≤d\nL1759@P29: i−1\nL1760@P29: (X)\nL1761@P29: in which only the last n − i centers can be non-regular over T and outputs a blow\nL1762@P29: up sequence F\nL1763@P29: ≤d\nL1764@P29: i\nL1765@P29: (X) with only n − i − 1 bad blow ups in the end. By our as\u0002sumption, Xi+1 → Xi\nL1766@P29: is the first blow up of f whose center W can be non-regular\nL1767@P29: over T . The intersection of Wsing with the preimage of T can be non-empty, but\nL1768@P29: it is definitely contained in W ∩ X\nL1769@P29: ≤d\nL1770@P29: i ⊆ W≤d−1\nL1771@P29: . Consider the blow up sequence\nL1772@P29: F\nL1773@P29: ≤d−1\nL1774@P29: (W): W′ 99K W, which exists by the induction assumption. Its centers Vj\nL1775@P29: can have singularities only over W≥d, in particular, the image of (Vj )sing in X is\nL1776@P29: contained in X>d. By Lemma 4.2.1, the pushforward X′\nL1777@P29: i\nL1778@P29: 99K Xi of F\nL1779@P29: ≤d−1\nL1780@P29: (W) with\nL1781@P29: respect to the closed immersion W ֒→ Xiis a blow up sequence with centers Vj . In\nL1782@P29: particular, its centers are regular over X≤d.\nL1783@P29: Let now f\nL1784@P29: ′\nL1785@P29: : X′\nL1786@P29: m 99K X′\nL1787@P29: i\nL1788@P29: 99K Xi 99K X0 be obtained from f by inserting X′\nL1789@P29: i\nL1790@P29: 99K\nL1791@P29: Xiinstead of Xi+1 → Xi as in Definition 4.2.2. By Lemma 4.2.3 the center of\nL1792@P29: X′\nL1793@P29: i+1 → X′i\nL1794@P29: is the strict transform of W, hence it is W′. Since W′is regular over\nL1795@P29: X≤d by the construction, only the last i − 1 blow ups of f\nL1796@P29: ′\nL1797@P29: can be non-regular over\nL1798@P29: T (the blow ups from the sequence X′\nL1799@P29: m 99K X′\nL1800@P29: i+1). So, we can set F\nL1801@P29: ≤d\nL1802@P29: i\nL1803@P29: (X) = f\nL1804@P29: ′\nL1805@P29: .\nL1806@P29: Remark 4.3.2. The scheme W does not have to be integral. So, we essentially\nL1807@P29: exploited here that the resolution functor F is defined for all reduced schemes.\nL1808@P29: Extension n + 1. At this stage we already have a blow up sequence f = F\nL1809@P29: ≤d\nL1810@P29: n\nL1811@P29: (X)\nL1812@P29: such that all its centers are regular over X≤d. The only problem is that though\nL1813@P29: the singular locus of Xm is disjoint from the preimage of X≤d \\ T it can intersect\nL1814@P29: the preimage of T . For any x ∈ T consider the pro-open subscheme Xx := Xm ×X\nL1815@P29: Spec(OX,x) of Xm and the scheme-theoretic preimage Dx = (Dm)|Xx of x. Clearly,\nL1816@P29: (Xx)sing ⊆ Dx, and Dx is a Cartier divisor by Extension 0. Thus, the pair (Xx, Dx)\nL1817@P29: is an object of Csmall, and hence so is (`\nL1818@P29: x∈T Xx,\nL1819@P29: `\nL1820@P29: x∈T Dx). Applying FVar to the\nL1821@P29: latter pair we obtain a list of (resp. strong) desingularizations fx : X′\nL1822@P29: x 99K Xx for all\nL1823@P29: x ∈ T . (Actually, each fx is FVar(Xx, Dx) saturated with few synchronizing empty\nL1824@P29: blow ups.) Let U ֒→ X be an open neighborhood of X≤dsuch that the closures\nL1825@P29: x ∈ U of distinct points x ∈ T are pairwise disjoint, and set Um = Xm ×X U. Define\nL1826@P29: gx : Ux 99K Um as the pushforward of fx with respect to the pro-open immersion\nL1827@P29: Xx ֒→ Um. Since each gx is x-supported, Lemma 4.2.4 implies that we can merge\nL1828@P29: all gx’s into a single blow up sequence g : U\nL1829@P29: ′\nL1830@P29: m 99K Um. Finally, we define f\nL1831@P29: ′\nL1832@P29: : X′\nL1833@P29: m 99K\nL1834@P29: Xm to be the pushforward of g with respect to the open immersion Um ֒→ Xm,\nL1835@P29: and set F\nL1836@P29: ≤d\nL1837@P29: (X) = f ◦ f\nL1838@P29: ′\nL1839@P29: . Then F\nL1840@P29: ≤d\nL1841@P29: (X) coincides with F\nL1842@P29: ≤d−1\nL1843@P29: (X) over X≤d \\ T\nL1844@P29-30: and coincides with f ◦ fx over each Spec(OX,x) for x ∈ T . By our construction theFUNCTORIAL DESINGULARIZATION OVER Q: THE NON-EMBEDDED CASE 31\nL1845@P30: latter is a (resp. strong) desingularization of Spec(OX,x), hence the constructed\nL1846@P30: F\nL1847@P30: ≤d\nL1848@P30: (X) is a (resp. strong) desingularization of X up to codimension d.\nL1849@P30: Remark 4.3.3. To illustrate a certain flexibility (and non-canonicity) of the method,\nL1850@P30: note that we could use the blow up sequences FVar(Xx, Dx) instead of fx’s in the\nL1851@P30: construction of F\nL1852@P30: ≤d\nL1853@P30: (X) (in other words, we could omit all empty blow ups in\nL1854@P30: fx’s). Although such choice would work as well, our construction seems to be more\nL1855@P30: natural.\nL1856@P30: It remains to check that F\nL1857@P30: ≤d\nL1858@P30: is functorial. By Lemma 4.2.5 the operations\nL1859@P30: of pushing forward, extending and merging of blow ups are compatible with a\nL1860@P30: regular (and even flat) base change h: Xe → X, and we claim that it follows easily\nL1861@P30: that all intermediate constructions in our proof are functorial. Indeed, the set of\nL1862@P30: the maximal points of h\nL1863@P30: −1\nL1864@P30: (T ) is exactly the set Te of points of Xe ≤d over which\nL1865@P30: F\nL1866@P30: ≤d−1\nL1867@P30: (Xe) is not a desingularization. Hence the Zariski closure of Te coincides with\nL1868@P30: T ×X Xe in Extension 0, and therefore the blow up sequence F\nL1869@P30: ≤d\nL1870@P30: 0\nL1871@P30: is functorial.\nL1872@P30: In the i-th Extension we have that Wf = W ×X Xe by inductive functoriality of\nL1873@P30: F\nL1874@P30: ≤d\nL1875@P30: i−1\nL1876@P30: . Hence F\nL1877@P30: ≤d−1\nL1878@P30: (Wf) is a trivial extension of F\nL1879@P30: ≤d−1\nL1880@P30: (W) ×X Xe by functoriality\nL1881@P30: of F\nL1882@P30: ≤d−1\nL1883@P30: , and so F\nL1884@P30: ≤d\nL1885@P30: i\nL1886@P30: is functorial. The last Extension is dealt with similarly. \u0003",
  "c4ad8d70a4bdebbd888b86893e9c6fbaa0c9a79e7cc277c3e1a64f8b2871b742": "1.5. Valuations of linear growth. Let L be a line bundle on X. A semivaluation v ∈ X an\ncan be naturally evaluated on any section s ∈ H0 (X, L), by defining v(s) as the value of v on\nthe germ in OX corresponding to s in any local trivialization of L at the center of v. Thus\nv(s) ∈ [0, +∞], v(s) = ∞ iff s vanishes along the support of v, and v(s) > 0 iff s vanishes\nat the center of v. Setting |s|(v) := e−v(s) defines a continuous function |s| : X an → [0, 1].\nRemark 1.24. This construction reflects the existence of the trivial metric | · | of Lan , a\ncontinuous metric characterized by |τ | ≡ 1 on the compact set c−1 (U ) for any trivializing\nsection τ ∈ H0 (U, L) on an open subset U ⊂ X.\n  In what follows, we fix an ample line bundle L on X.\nLemma 1.25. A semivaluation v ∈ X an is a valuation iff v(s) < +∞ for all regular sections\ns ∈ H0 (X, mL), m ∈ N.\nProof. Suppose v ∈/ X val , so that its support Y ⊂ X is not an irreducible component of X.\nSince L is ample, we can find for m \u001d 1 a nonzero section s ∈ H0 (X, mL) that vanishes\nalong Y , but not along any irreducible component of X. Then s is regular, and v(s) = ∞.\nThe converse direction is clear.                                                         \u0003",
  "e565799b443d5db3b4ba800952d6df60207bba05a7b673e8cb9815d26f84cbc0": "\nWe define a continuous function ϕa : X an → R by setting ϕa (v) = −σ(v)(a), i.e.\n                                       ϕa = max{log |aλ | + λ}.                                 (2.3)\n                                                λ\n\nFor any two flag ideals a, a0 , we have\n                            ϕa·a0 = ϕa + ϕa0 ,        ϕa+a0 = max{ϕa , ϕa0 }.                   (2.4)\n\f              GLOBAL PLURIPOTENTIAL THEORY OVER A TRIVIALLY VALUED FIELD                      21\n\nDefinition 2.1. We define the space of piecewise linear (PL) functions on X an as the\nQ-linear subspace\n                                      PL(X) ⊂ C0 (X)\ngenerated by all functions ϕa attached to flag ideals a.\n  By (2.4), the subset\n                    PL+ (X) := m−1 ϕa | m ∈ Z>0 , a flag ideal ⊂ PL(X)\n                              \b\n                                                                                           (2.5)\n    is stable under sums and finite maxima, and contains all Q-valued constant functions. It\nis also stable under multiplication by Q+ : if c ∈ Q+ , then cϕa = m−1 ϕamc for any m ∈ Z>0\nis such thatP mc ∈−λZ. Further, it is stable     under the scaling action of Q>0 : if t ∈ Q>0\n                                         −1 ϕ 0 , where m ∈ Z\nand a =         aλ $   , then t · ϕ a = m    a                  >0 is such that mt ∈ Z, and\n  0\n       P m λ −mtλ\na = λ aλ $           .\n    It follows that the Q-vector space PL(X) is stable under finite maxima and minima, and\nunder the scaling action of Q>0 , and it contains all constant Q-valued functions. Further,\nany function in PL(X) can be written as a difference of functions in PL+ (X), and is Q-valued\non X div .\n    We refer to Theorem 2.7 and Appendix A for an interpretation of PL functions in terms\nof test configurations and PL functions on simplicial complexes, respectively. In our setting,\nPL functions play the role of smooth functions in the complex analytic case, as illustrated\nby the next result.\nTheorem 2.2. The space PL(X) is dense in C0 (X) for the topology of uniform convergence.\n  By the ‘lattice version’ of the Stone–Weierstrass theorem, this is a direct consequence of\nthe following result.\nLemma 2.3. The Q-linear subspace PL(X) ⊂ C0 (X) is stable under max (and hence min),\ncontains the constants in Q, and separates the points of X an .\nProof. The first two properties are clear. As mentioned in §1.1, the topology of X an is\ngenerated by the functions log |b| attached to ideals b ⊂ OX . For any two v, v 0 ∈ X an we\ncan thus find an ideal b such that log |b|(v) 6= log |b|(v 0 ) (since X an is Hausdorff), and it\nfollows that ϕ := max{log |b|, −m} ∈ PL(X) separates v, v 0 for m \u001d 1.                        \u0003\nRemark 2.4. We will occasionally consider the R-vector space PL(X)R ⊂ C0 (X) generated\nby PL(X). As opposed to the latter, PL(X)R is not closed under max.\nExample 2.5. Given a closed subscheme Z ⊂ X with ideal b ⊂ OX , the function\n                                   ϕZ := max{log |b|, −1}\n          +\nlies in PL (X), since ϕZ = ϕa with a = b + ($). Note that\n                                   t · ϕZ = max{log |b|, −t}                               (2.6)\nfor all t ∈ Q>0 .\nExample 2.6. Assume X is a smooth irreducible curve, and recall the description of X an\nin §1.1.6. As a special case of Example 2.5, each p ∈ X(k) defines a function ϕp ∈ PL+ (X)\nthat satisfies for all q ∈ X(k) and t ∈ [0, +∞]\n                                        \u001a\n                             ?            max{−t, −1} if q = p;\n                            ιq ϕp (t) =\n                                          0            otherwise.\n\f22                       SÉBASTIEN BOUCKSOM AND MATTIAS JONSSON\n                                                                                        P\nUsing (2.6) and the fact that every nontrivial ideal of X is of the form b = OX (− i ai pi )\nfor a finite set (pi ) in X(k) and ai ∈ Z>0 , one checks that the functions t · ϕp with t ∈ Q>0\nand p ∈ X(k) span PL(X). A function ϕ ∈ C0 (X) is PL iff ϕ is constant on all but finitely\nmany rays of X an and Q-PL on these rays, and ϕ ∈ PL+ (X) iff ϕ is further convex (and\nhence decreasing, being bounded) on each ray.\n2.2. PL functions and test configurations. Let X be a test configuration for X, and\nrecall that Gauss extension of (semi)valuations yields an embedding σX : X an ,→ X an onto\nthe set of k × -invariant semivaluations w ∈ X an such that w(X0 ) = w($) = 1.\n   Recall also that a vertical Q-Cartier divisor on X means a Gm -invariant Q-Cartier divisor\nwith support in X0 (see Example 1.5). Such divisors form a finite dimensional Q-vector space,",
  "0deecfcb8093f8efae3de37a562f6a7b4aaa7a36b02b48cb6232d9a9aa71ffe5": "normal), we have:\nProposition 2.30. If L is an ample Q-line bundle, then every semiample test configuration\nfor (X, L) is equivalent to a unique ample, integrally closed test configuration.\nProof. By [BHJ17, Proposition 2.17], every semiample test configuration is equivalent to an\nample test configuration, which can further be assumed to be integrally closed after passing\nto the integral closure. This proves existence.\n    To prove uniqueness, let (X , L), (X 0 , L0 ) be two ample, integrally closed test configurations\nfor (X, L) that are equivalent. After replacing L with a multiple, we may assume that L, L0\nare honest line bundles. By ampleness, it will then be enough to show that H0 (X , mL) =\nH0 (X 0 , mL0 ) for all m ∈ N, as k[$]-submodules of H0 (X, mL)k[$±1 ] (see §1.2). Choose\na test configuration X 00 dominating X and X 0 via µ : X 00 → X , µ0 : X 00 → X 0 , such that\nL00 := µ? L = µ0? L0 . Since X and X 0 are integrally closed, Lemma 1.12 yields µ? OX 00 = OX ,\nµ0? OX 00 = OX 0 , and the projection formula shows that\n                           H0 (X , mL) = H0 X 00 , mL00 = H0 (X 0 , mL0 ).\n                                                          \u0001\n\nThe proof is complete.                                                                             \u0003\n2.7. Fubini–Study functions and test configurations. Let L be a Q-line bundle on X.\nFor any test configuration (X , L) for (X, L), we can choose a test configuration X 0 with two\nmorphisms µ : X 0 → X , ρ : X 0 → Xtriv . Then\n                                D := µ? L − ρ? Ltriv ∈ VCar(X )Q ,\nand mapping L to D yields a 1–1 correspondence between the set of equivalence classes\nof test configurations for (X, L) and the Q-vector space limX VCar(X )Q , which in turn is\n                                                         −→\nisomorphic to PL(X), by Theorem 2.7. We write ϕL for the element of PL(X) associated to\n\f30                        SÉBASTIEN BOUCKSOM AND MATTIAS JONSSON\n\nL. The restriction of ϕL to X div coincides with the function associated to the equivalence\nclass of (X , L) in [BHJ17, §6].\nTheorem 2.31. For any Q-line bundle L on X, the map L 7→ ϕL sets up a 1–1 correspon-\ndence between:\n    (i) the set of equivalence classes of test configurations for L and PL(X);\n   (ii) the set of equivalence classes of semiample test configurations for L and H(L).\n   Note that the sets in (ii) are nonempty only if L is semiample. Combined with Proposi-\ntion 2.30, we infer:\nCorollary 2.32. If L is an ample Q-line bundle, then L 7→ ϕL defines a 1–1 correspondence\nbetween the set of ample, integrally closed test configurations for L and H(L).\n     The set H(L) thus corresponds to HNA (L) in the notation of [BHJ17, Definition 6.2].\nProof of Theorem 2.31. By construction, the map L 7→ ϕL is the composition of D 7→ ϕD\nwith the canonical bijection between equivalence classes of test configurations for L and\nlimX VCar(X )Q . Thus (i) is a direct consequence of Theorem 2.7.\n−→\n   To prove (ii), let (X , L) be a semiample test configuration for (X, L). After replacing L\nwith a multiple and pulling-back to a higher test configuration, we may assume without loss\nthat L is a globally generated line bundle, and that X dominates the trivial test configuration\nvia µ : X → Xtriv . Set D := L − µ? Ltriv ∈ VCar(X ), so that ϕL = ϕD . Since L is globally\ngenerated, OX (D) is µ-globally generated, and the flag ideal a := µ? OX (D) thus satisfies\na·OX = OX (D), and hence ϕa = ϕD = ϕL . Denote by a0 ⊂ a the flag ideal locally generated\nby\n                                H0 (Xtriv , Ltriv ⊗ a) ≃ H0 (X , L).\nSince L is globally generated, we have a0 · OX = OX (D) = a · OX ; hence ϕa0 = ϕL . By\nconstruction, L ⊗ a0 is globally generated, and Proposition 2.25 thus yields, as desired,\nϕL ∈ H(L).\n   Conversely pick ϕ ∈ H(L). After replacing L with a multiple, Proposition 2.25 yields\nϕ = ϕa for a flag ideal a on Xtriv such that Ltriv ⊗ a is globally generated. Denoting by\nµ : X → Xtriv the blowup along a, we have a · OX = OX (D) for a vertical Cartier divisor D\nsuch that L := µ? Ltriv + D is globally generated, and ϕL = ϕD = ϕa = ϕ.                      \u0003\n     The next result will be needed in §3.1.\nLemma 2.33. If L is an ample Q-line bundle on X and X any test configuration for X\nthat dominates Xtriv , then L admits an ample test configuration L determined on X .\nProof. By Lemma 1.8, we can find D ∈ VCar(X )Q that is relatively ample over Xtriv .\nDenoting by LX the pullback of L to X , it follows that L := LX + εD is ample for ε ∈ Q>0\nsmall enough, and we are done.                                                         \u0003\n2.8. Geometric interpretation of the scaling action. As noted in §2.1, the spaces\nPL(X) and PL+ (X) admit a natural scaling action by Q>0 . We now give a geometric\ninterpretation of the scaling action of Z>0 in terms of base change.\n   Using flag ideals, this is easy: any function ϕ ∈ PL+ (X) can be written ϕ = m−1 ϕa for\nsome m ∈ Z>0 and some flag ideal a on Xtriv = X × A1 . It then follows from the discussion\nafter (2.5) that if d ∈ Z>0 , then d · ϕ = m−1 ϕa(d) , where a(d) is the pullback of a under the\nmap Xtriv → Xtriv given by $ 7→ $d .\n\f             GLOBAL PLURIPOTENTIAL THEORY OVER A TRIVIALLY VALUED FIELD                           31\n\n  Following [BHJ17, §6.3], we can give a smilar interpretation of the scaling action when\nthe functions are associated to test configurations.\n  Let L be a Q-line bundle on X. For any test configuration (X , L) for (X, L) and d ∈ Z>0 ,",
  "fc3d3b08864bcfeefe833a1079e5530224c333242d000add352f344be9ac4219": "   Given a test configuration π : X → A1 , we denote by Amp(X /A1 ) ⊂ Nef(X /A1 ) the set\nof π-ample classes α ∈ N1 (X /A1 ), that is, classes whose restriction to X0 is ample.\nDefinition 3.8. For any ω ∈ Amp(X), we denote by Hdom (ω) ⊂ PL ∩ PSH(ω) the set of ω-\npsh PL functions of the form ϕD with D ∈ VCar(X )Q for a test configuration X dominating\nXtriv and ωX + D ∈ Amp(X /A1 ).\n   After pulling back by the (finite) integral closure morphism Xe → X , one may always\narrange that X is integrally closed in this definition.\nExample 3.9. If ω = c1 (L) for an ample Q-line bundle, then H(L) is in 1–1 correspon-\ndence with the set of ample, integrally closed test configurations (X , L) for (X, L) (see Corol-\nlary 2.32), and\n                              Hdom (L) := Hdom (c1 (L)) ⊂ H(L)\ncorresponds to the subset such that X dominates Xtriv .\n     As in Corollary 2.26, we have\n                                     Q+ Hdom (ω) = PL+ (X)                                 (3.2)\nfor any ω ∈ Amp(X), so that Hdom (ω) spans the Q-vector space PL(X).\nProposition 3.10. If ω ∈ Amp(X), then every ϕ ∈ PLR ∩ PSH(ω) is a uniform limit of\nfunctions in Hdom (ω).\nLemma 3.11. For any ω ∈ Amp(X), the set of test configurations X dominating Xtriv such\nthat there exists H ∈ VCar(X )Q with ωX + H ∈ Amp(X /A1 ) is cofinal in the set of all test\nconfigurations.\nProof. By Lemma 1.8, any test configuration for X is dominated by a test configuration X\nwith a morphism µ : X → Xtriv such that VCar(X )Q contains a µ-ample divisor A. Since\nωXtriv ∈ N1 (Xtriv /A1 ) is ample, ωX + εA = µ? ωXtriv + εA ∈ N1 (X /A1 ) is ample for ε ∈ Q>0\nsmall enough, and setting H := εA yields the result.                                        \u0003\nProof of Proposition 3.10. Pick any ϕ ∈ PLR ∩ PSH(ω), and write ϕ = ϕD for some D ∈\nVCar(X )R , where X is an integrally closed test configuration. Thus ωX + D ∈ N1 (X /A1 ) is\nnef. By Lemma 3.11 we may assume that there exists P    H ∈ VCar(X )PR such that ωX + H is\nample. Pick a basis (Ci ) for VCar(X )Q and write D = i ci Ci , H = i c0i Ci with ci , c0i ∈ R.\n                                  1                                                          1\nFor m \u001d 1, the class ωX + D + m     H ∈ N1 (X /A1 ) is ample, and we can pick εm,i ∈ (0, m     )\n                    P          0\n                              ci\nsuch that if Dm := i (ci + m + εm,i )Ci , then Dm ∈ VCar(X )Q and ωX + Dm is ample. It\n                                                     1\nfollows that ϕDm ∈ Hdom (ω), and that ϕDm − ϕ = m\n                                                             P\n                                                       ϕH + i εm,i ϕCi tends to 0 uniformly\non X an .                                                                                     \u0003",
  "31dcf643b431ee85afa779d0aa54f37eb920945c87f46d5c3fd532e72fb4929b": "to an arbitrary numerical class θ ∈ N1 (X). We also study pluripolar sets, i.e. loci where\nθ-psh functions take the value −∞.\n\f               GLOBAL PLURIPOTENTIAL THEORY OVER A TRIVIALLY VALUED FIELD                        45\n\n  4.1. The class of θ-psh functions. Recall that:\n       • a function ϕ ∈ X an → R ∪ {−∞} is called generically finite if ϕ|Xαan 6≡ −∞ for all α\n         (see Definition 1.3);\n                                gf\n       • for any L ∈ Pic(X)Q , HR  (L) denotes the set of generically finite (continuous) func-\n                    an\n         tions ϕ : X → R ∪ {−∞} of the form\n                                    ϕ = m−1 max{log |si | + λi }\n                                                i\n           where (si ) is a finite set of sections of mL with m sufficiently divisible, λi ∈ R (see\n           Definition 2.18). This set is non-empty iff L is effective.\n  Given any numerical class θ ∈ N1 (X), we are seeking to define a class PSH(θ) of θ-\n  plurisubharmonic functions (θ-psh functions for short) ϕ : X an → R ∪ {−∞}. By analogy\n  with the complex analytic setting, these functions should be usc and generically finite, and\n  the following properties should hold:\n                                                gf\n (PSH1) for any L ∈ Pic(X)Q , we have HR           (L) ⊂ PSH(L) := PSH(c1 (L));\n (PSH2) if a generically finite function ϕ : X an → R ∪ {−∞} arises as the pointwise limit of\n           a decreasing net (ϕi ) with ϕi ∈ PSH(θi ) and limi θi = θ, then ϕ ∈ PSH(θ).\n  Note that (PSH2) implies the following two properties:\n(PSH2a) for any function ϕ : X an → R ∪ {−∞}, the set of θ ∈ N1 (X) such that ϕ ∈ PSH(θ)\n           is closed (possibly empty);\n(PSH2b) for any θ ∈ N1 (X), the set PSH(θ) is closed under decreasing limits (provided the\n           limit function is generically finite).\n  Taking (PSH1) and (PSH2) as minimal requirements directly leads to the following defini-\n  tion:\n  Definition 4.1. For any θ ∈ N1 (X), we define a θ-psh function ϕ : X an → R ∪ {−∞} as a\n  generically finite, usc function that can be written as the pointwise limit of a decreasing net\n         gf\n  ϕi ∈ HR   (Li ) with Li ∈ Pic(X)Q such that limi c1 (Li ) = θ in N1 (X).\n    We denote by PSH(θ) the set of θ-psh functions, and by\n                        CPSH(θ) := C0 (X) ∩ PSH(θ) ⊂ E ∞ (θ) ⊂ PSH(θ)\n  the subsets of continuous and bounded θ-psh functions, respectively. When needed, we also\n  write PSH(X, θ) = PSH(θ) etc. Using the notation in the definition, we have:\n                 gf\n        • since HR  (Li ) is non-empty, Li is necessarily effective, by (2.11), and hence\n                                   PSH(θ) 6= ∅ =⇒ θ ∈ Psef(X);                                (4.1)\n        • if ϕ is bounded, then ϕi is finite valued, i.e. ϕi ∈ H(Li ); this implies that Li is\n          semiample, by (2.12), and hence\n                                    E ∞ (θ) 6= ∅ =⇒ θ ∈ Nef(X);                               (4.2)\n        • if ϕ ∈ CPSH(θ) is further continuous, then ϕi → ϕ uniformly on X an , by Dini’s\n          lemma.\n  Remark 4.2. In the complex analytic case, psh functions and metrics are defined in a\n  different way, which is local in nature. However, when X is smooth, well-known arguments\n  due to Demailly [Dem92] and relying on the Ohsawa–Takegoshi extension theorem show that\n  any psh metric on a (necessarily pseudoeffective) line bundle L can be approximated from\n  above by metrics attached to sections of mL + A, where A is a fixed ample line bundle and\n\f46                        SÉBASTIEN BOUCKSOM AND MATTIAS JONSSON\n\nm is large (compare for instance [Bou04, Theorem 5.4] or [GZ05, Appendix]). As a result,\nany such metric satisfies the analogue of Definition 4.1.\nLemma 4.3. For functions in PL(X)R , Definition 4.1 is consistent with Definition 3.2.\nIn other words, given θ ∈ N1 (X), a test configuration X that dominates Xtriv and D ∈\nVCar(X )R , we have\n                        ϕD ∈ PSH(θ) ⇐⇒ θX + D ∈ Nef(X /A1 ).\n  Indeed, this follows from Lemma 3.5, Lemma 3.7 and Corollary 3.22. For any θ ∈ N1 (X),\nwe get, in particular,\n                   PSH(θ) contains all constant functions ⇐⇒ θ ∈ Nef(X),                       (4.3)\nwhich provides a converse to (4.2).\nRemark 4.4. If L is a Q-line bundle, then functions in PSH(L) = PSH(c1 (L)) can be\ninterpreted as psh metrics on L, using the trivial metric. By (4.3), any nef line bundle L\nadmits a bounded (continuous) psh metric, to wit the trivial metric. This is in stark contrast\nwith the complex analytic case, where a nef and big line bundle may not admit any bounded\npsh metric (see [BEGZ10, Example 5.4], based on [DPS94, Example 1.7]).\nTheorem 4.5. Properties (PSH1) and (PSH2) above are satisfied.\n  As a consequence, Definition 4.1 is indeed the minimal one for which (PSH1) and (PSH2)\nare satisfied.\nLemma 4.6. Let K be a compact topological space, and assume we are given:\n      • a set S and, for each s ∈ S, a family Fs of continuous functions f : K → R ∪ {−∞},\n         stable under addition of a constant;\n      • a map ρ : S → T to a metrizable topological space T .\nFor each t ∈ T , denote by Fet the set of all (usc) functions g : K → R ∪ {−∞} that can\nbe written as the pointwise limit of a decreasing net (fi ) with fi ∈ Fsi for a net (si ) of S\n                                          ≈\nsuch that limi ρ(si ) = t in T . Then Ft = Fet for any t ∈ T . In other words, if a function\ng : K → R ∪ {−∞} can be written as the pointwise limit of a decreasing net (gi )i∈I with\ngi ∈ Feti for a net (ti ) of T such that limi ti = t, then g ∈ Fet .\nProof. Pick a metric d on T inducing the given topology. For each i ∈ I, gi is the pointwise\nlimit of a decreasing net (fi,j )j∈Ji with fi,j ∈ Fsi,j for a net (si,j )j∈Ji in S such that ti,j :=\nρ(si,j ) satisfies limj ti,j = ti . Denote by A the set of triples α = (i, j, ε) with i ∈ I, j ∈ Ji\nand ε ∈ R>0 , and define a partial preorder on A by setting\n                                                 i ≥ i0\n                                                \n                                  0 0 0\n                    (i, j, ε) ≥ (i , j , ε ) ⇐⇒   fi,j + ε ≤ fi0 ,j 0 + ε0 on K                 (4.4)\n                                                  d(ti,j , ti ) + ε ≤ d(ti0 ,j 0 , ti0 ) + ε0 ,\n                                                \n\nWe claim that A is directed. To see this, pick α1 = (i1 , j1 , ε1 ), α2 = (i2 , j2 , ε2 ) in A. Since\nI is directed, we can choose i3 ∈ I with i3 ≥ i1 , i2 . Pick also ε3 > 0 with ε3 < min{ε1 , ε2 }.\nSince (gi )i is decreasing, we have gi3 ≤ min{gi1 , gi2 } ≤ min{fi1 ,j1 , fi2 ,j2 }, and hence\n                              gi3 + ε3 < min{fi1 ,j1 + ε1 , fi2 ,j2 + ε2 }                     (4.5)\npointwise on K. For each j ∈ Ji3 , define hj : K → R by\n                   hj := exp (fi3 ,j + ε3 ) − exp (min{fi1 ,j1 + ε1 , fi2 ,j2 + ε2 }) .\n\f              GLOBAL PLURIPOTENTIAL THEORY OVER A TRIVIALLY VALUED FIELD                                      47\n\nThen (hj ) is a decreasing net of continuous functions such that limj hj < 0 pointwise on K,\nby (4.5). The compact space K can thus be written as the increasing union of the open sets\n{hj < 0}, and hence K = {hj3 < 0} for some j3 ∈ Ji3 , i.e.\n                            fi3 ,j3 + ε3 < min{fi1 ,j1 + ε1 , fi2 ,j2 + ε2 } on K.\nSince limj ti3 ,j = ti3 and ε3 < min{ε1 , ε2 }, we can further arrange, after increasing j3 if\nneeded, that\n          d(ti3 ,j3 , ti3 ) + ε3 < min{ε1 , ε2 } ≤ min {d(ti1 ,j1 , ti1 ) + ε1 , d(ti2 ,j2 , ti2 ) + ε2 } .\nThus α3 := (i3 , j3 , ε3 ) ∈ A satisfies α3 ≥ α1 , α2 , which proves, as desired, that A is directed.\n  Now, for each α = (i, j, ε) ∈ A, set\n                  sα := si,j ∈ S,       tα = ρ(sα ) ∈ T,        and gα := fi,j + ε ∈ Fsα ,\nwhere the last containment holds because Fsα is assumed to be stable under addition of a\nconstant. By construction, (gα )α∈A is a decreasing net, and it will suffice to show limα gα = g\npointwise on K and limα tα = t. Pick δ > 0 and x ∈ K. Since limi gi (x) = g(x) and\nlimi ti = t, we can find i0 ∈ I such that gi0 (x) < g(x) + δ and d(ti , t) < δ for all i ≥ i0 .\nUsing limj fi0 ,j (x) = gi0 (x) and limj ti0 ,j = ti0 , we next pick j0 ∈ Ji0 and 0 < ε0 \u001c 1 such\nthat fi0 ,j0 (x) + ε0 < g(x) + δ and d(ti0 ,j0 , ti0 ) + ε0 < δ. Set α0 := (i0 , j0 , ε0 ) ∈ A. For each\nα = (i, j, ε) ∈ A such that α ≥ α0 , we then have, by (4.4),\n                           gα (x) = fi,j (x) + ε ≤ fi0 ,j0 (x) + ε0 < g(x) + δ,\n\n                    d(tα , ti ) = d(ti,j , ti ) ≤ d(ti,j , ti ) + ε ≤ d(ti0 ,j0 , ti0 ) + ε0 < δ,\nas well as i ≥ i0 , which implies d(ti , t) < δ and hence d(tα , t) < 2δ. This shows, as desired,\nlimα gα (x) = g(x) and limα tα = t, which concludes the proof.                                 \u0003\n\nProof of Theorem 4.5. That (PSH1) holds is clear from Definition 4.1. As for (PSH2), it\n                                                                             gf\ncorresponds to the special case of Lemma 4.6 in which K := X an , FL := HR      (L) for L ∈ S :=\nPic(X)Q , and ρ : S → T := N1 (X) maps L ∈ Pic(X)Q to c1 (L). Indeed, for any θ ∈ N1 (X),\nPSH(θ) is precisely the set of functions in Feθ that are generically finite.                   \u0003\n\n4.2. Basic properties. The next few results provide some basic but important properties\nof θ-psh functions.\nTheorem 4.7. For all θ, θ0 ∈ N1 (X) and t ∈ R>0 , we have:\n     (i) PSH(θ) + PSH(θ0 ) ⊂ PSH(θ + θ0 ) and PSH(tθ) = t PSH(θ);\n    (ii) the set PSH(θ) is convex, and stable under uniform limits, finite maxima, the additive\n         action of R, and the scaling action of R>0 ;\n   (iii) for any morphism f : Y → X and ϕ ∈ PSH(X, θ), either f ? ϕ ∈ PSH(Y, f ? θ) or\n         f ? ϕ ≡ −∞ on some irreducible component of Y an ;\n   (iv) for any ϕ ∈ PSH(θ) and any α, we have ϕ|Xαan ∈ PSH(Xα , θ|Xα ).\n\nRemark 4.8. If XQ is disconnected, with connected components X β , then it is easy to see\n                           β\nthat PSH(X, θ) = β PSH(X , θ|X β ).\n\nLemma 4.9. For any θ ∈ N1 (X) and ϕ, ϕ0 ∈ PSH(θ), we can find a net (Li ) of Q-line\n                        gf\nbundles and ϕi , ϕ0i ∈ HR  (Li ) such that limi c1 (Li ) → θ, ϕi & ϕ, ϕ0i & ϕ0 .\n\f48                         SÉBASTIEN BOUCKSOM AND MATTIAS JONSSON\n\nProof. By definition, we can find decreasing nets (ϕi )i∈I , (ϕ0j )j∈I 0 and Q-line bundles Mi ,\n                        gf                 gf\nMj0 such that ϕi ∈ HR      (Mi ), ϕ0j ∈ HR    (Mj0 ), limi c1 (Mi ) = limj c1 (Mj0 ) = θ and limi ϕi = ϕ,\n      0\nlimj ϕj = ϕ . Replacing I, I with the directed set I × I 0 (equipped with the product\n               0                    0\n\npreorder), we may assume I = I 0 . Fix an ample line bundle A. Since limi (c1 (Mi )−c1 (Mi0 )) =\n0, we can find εi ∈ Q>0 such that Mi − Mi0 + εi A is ample and limi εi = 0. If Li := Mi + εi A,\nthen c1 (Li ) → θ, and since Li − Mi and Li − Mi0 are both ample, Proposition 2.19 yields\n        gf          gf                gf\nϕi ∈ HR    (Mi ) ⊂ HR  (Li ), ϕ0i ∈ HR   (Li ), and we are done.                                       \u0003\nProof of Theorem 4.7. We will repeatedly use Proposition 2.19. Pick ϕ ∈ PSH(θ), ϕ0 ∈\nPSH(θ0 ). As ϕ and ϕ0 are finite on vtriv,α for all α, so is the function ϕ+ϕ0 , which is therefore\ngenerically finite. Further, ϕ and ϕ0 can be written as the limits of decreasing nets (ϕi )i∈I\n                             gf               gf\nand (ϕ0j )j∈I 0 with ϕi ∈ HR    (Li ), ϕ0j ∈ HR  (L0j ) for Li , L0j ∈ Pic(X)Q such that limi c1 (Li ) = θ\nand limj c1 (L0j ) = θ0 , respectively. The net (ϕi + ϕ0j )(i,j)∈I×I 0 is decreasing, and converges\n                                              gf\npointwise to ϕ + ϕ0 . Now ϕi + ϕ0j ∈ HR          (Li + L0j ), and hence ϕ + ϕ0 ∈ PSH(θ + θ0 ), since\n                          0           0\nlim(i,j) (c1 (Li ) + c1 (Lj )) = θ + θ . This proves the first inclusion in (i).\n                                                                  gf\n    For any c ∈ R and t ∈ R>0 , ϕi + c and t · ϕi belong to HR       (Li ), and decrease, respectively,\nto ϕ + c and t · ϕ, which therefore belong to PSH(θ).\n    We next show that tϕ ∈ PSH(tθ). If t is rational, this is clear, since each tLi is a Q-line\n                   gf\nbundle, tϕi ∈ HR      (tLi ) and tϕi & tϕ. In the general case, we may assume, after replacing ϕ\nwith ϕ − sup ϕ, that ϕ ≤ 0. Writing t as the limit of an increasing sequence tm ∈ Q>0 , we\nthen have tm ϕ ∈ PSH(tm θ) and tm ϕ & tϕ, tm θ → tθ, and hence tϕ ∈ PSH(tθ), by (PSH2).\nThis concludes the proof of (i), which implies that PSH(θ) is convex.\n    To prove that PSH(θ) is stable under maxima, pick ϕ, ϕ0 ∈ PSH(θ). By Lemma 4.9, we\n                                                        gf\ncan find a net (Li ) of Q-line bundles and ϕi , ϕ0i ∈ HR   (Li ) such that limi c1 (Li ) → θ, ϕi & ϕ,\n                                      gf\nϕi & ϕ . Then max{ϕi , ϕi } ∈ HR (Li ) decreases to max{ϕ, ϕ0 }, which therefore belongs to\n  0      0                     0\n\nPSH(θ).\n    If a net in PSH(θ) converges uniformly to a function ψ : X an → R ∪ {−∞}, then ψ is\ngenerically finite, and is also the uniform limit of a sequence (ψm ) in PSH(θ). After passing\nto a subsequence, it is then easy to find constants cm → 0 such that (ψm + cm ) is decreasing,\nand we infer ψ ∈ PSH(θ), by (PSH2). This concludes the proof of (ii).\n                                                                                                  gf\n    Next we prove (iii). Write ϕ ∈ PSH(θ) as the decreasing limit of a net ϕi ∈ HR                   (Li )\n                                                     gf                           ?        gf ?\nsuch that limi c1 (Li ) → θ. Then each ϕi ∈ HR (Li ) satisfies either f ϕi ∈ HR (f Li ) or\nf ? ϕi ≡ −∞ on some irreducible component of Y an . If f ? ϕ is generically finite, then the\nlatter case never occurs, since f ? ϕ ≤ f ? ϕi . Since f ? ϕi & f ? ϕ and c1 (f ? Li ) → f ? θ, (PSH2)\nyields f ? ϕ ∈ PSH(f ? θ).\n    Finally, (iv) follows from (iii) since ϕ is generically finite.                                    \u0003",
  "bee2dd5ee40e955868a1651e9c679c9f87594840ae634e587041b8da37487c91": "Theorem 4.15. Pick θ ∈ N1 (X) and ϕ ∈ PSH(θ). Then:\n                                                                   gf\n     (i) ϕ can be written as the limit of a decreasing net ϕi ∈ HQ    (Li ) with Li ∈ Pic(X)Q\n         such that c1 (Li ) − θ is ample and limi c1 (Li ) = θ;\n    (ii) if θ ∈ Nef(X) then (i) holds with ϕi ∈ H(Li ) = HQ (Li ) and Li ample;\n   (iii) if ω := θ ∈ Amp(X), then ϕ can be written as the limit of a decreasing net in\n         Hdom (ω) (see Definition 3.8).\n\f50                       SÉBASTIEN BOUCKSOM AND MATTIAS JONSSON\n\n   We shall later prove that these results actually hold with (countable) sequences instead\nof nets, see Corollary 12.18.\n   As already indicated by (iii), the class of θ-psh functions has particularly good properties\nwhen θ ∈ Amp(X) is ample. In this case, we typically write ω instead of θ.\nCorollary 4.16. For any ω ∈ Amp(X), the space CPSH(ω) = C0 (X) ∩ PSH(ω) is the\nclosure of Hdom (ω) ⊂ C0 (X) in the topology of uniform convergence.\nProof. By Theorem 4.7, CPSH(ω) is closed in the topology of uniform convergence. By\nTheorem 4.15 and Dini’s lemma, any ϕ ∈ CPSH(ω) is the uniform limit of a net in Hdom (ω),\nand the result follows.                                                                \u0003\nCorollary 4.17. For any θ ∈ N1 (X) and any ϕ ∈ PSH(θ) we have ϕ > −∞ on X lin .\nProof. Pick an ample line ` bundle L such that c1 (L) − θ is nef. Then ϕ ∈ PSH(L). Using\nTheorem 4.7 and X lin = α Xαlin , we may assume X is irreducible. Now pick v ∈ X lin . Then\nTL (v) < ∞, and we claim that ϕ(v) ≥ ϕ(vtriv ) − TL (v). Indeed, TL (v) is the supremum of\nm−1 v(s) over m ∈ Z>0 and s ∈ H0 (X, mL) \\ {0}. Equivalently, ψ := m−1 log |s| satisfies\nψ(v) ≥ ψ(vtriv ) − TL (v). Adding constants and taking finite maxima shows that this also\nholds for all ψ ∈ H(L), and then for all ϕ ∈ PSH(L), by Theorem 4.15.                     \u0003\n     As another consequence, we get:\nCorollary 4.18. Assume that X is irreducible, and let L be an ample Q-line bundle. Then\nPSH(L) is the smallest class of functions ϕ : X an → R ∪ {−∞}, not identically −∞, that\ncontains all functions of the form m−1 log |s| with m ∈ Z>0 and s ∈ H0 (X, mL) \\ {0}, and\nis stable under addition of a real constant, finite maxima, and decreasing limits.\n                                                                                gf\nProof of Theorem 4.15. By definition, ϕ is the limit of a decreasing net ϕi ∈ HR   (Li ) with\nc1 (Li ) → θ. Using (2.8) it is straightforward to see that each ϕi can further be written\n                                         gf\nas a decreasing limit of functions in HQ    (Li ). By Lemma 4.6, we may thus assume that\n        gf\nϕi ∈ HQ    (Li ). We can also arrange that c1 (Li ) − θ ∈ Amp(X). Indeed, given any ample\nline bundle A, we can find εi ∈ Q>0 such that limi εi = 0 and Li − θ + εi A is ample. By\n                                    gf          gf\nProposition 2.19, we have ϕi ∈ HQ      (Li ) ⊂ HQ  (Li + εi A), and replacing Li with Li + εi A\nyields the claim. This proves (i).\n   Assume next that θ is nef. In the notation of (i), it follows that each Li is ample. Further,\neach ϕi is the decreasing limit of max{ϕi , −m} ∈ H(Li ), and Lemma 4.6 yields (ii).\n   Finally assume that ω := θ is ample. Replacing ϕ with ϕ − sup ϕ, we may assume\nϕ ≤ 0. By Proposition 3.10, any function in PL ∩ PSH(ω) is a decreasing limit of functions\nin Hdom (ω). Relying again on Lemma 4.6, it will thus be enough to show that ϕ is the\ndecreasing limit of functions in PL ∩ PSH(ω). Use the notation of (ii), and pick t ∈ Q>1 .\nFor all i large enough we then have tω − c1 (Li ) ∈ Amp(X) for i large enough, and hence\nH(Li ) ⊂ PL ∩ PSH(tω). It follows that t−1 ϕ is the decreasing limit of a net in PL ∩ PSH(ω).\nSince ϕ ≤ 0, we have t−1 ϕ & ϕ as t & 1, and another application of Lemma 4.6 shows that\nϕ is also the decreasing limit of functions in PL ∩ PSH(ω). This proves (iii).                \u0003",
  "d521600de8d1a3e8a8ac95c3a5c6bdde1eb9668274cf065cdd3208652d3b3979": "Theorem 4.22. For any ϕ ∈ PSH(θ) and any usc function ψ : X an → R ∪ {−∞}, we have\n                             ϕ ≤ ψ on X div ⇐⇒ ϕ ≤ ψ on X an .\nIn particular, ϕ is the smallest usc extension of ϕ|X div to X an .\nCorollary 4.23. Every θ-psh function is uniquely determined by its restriction to X div , and\nthe topology of PSH(θ) is Hausdorff.\n   Because of this, we will occasionally say that a function ϕ : X div → R is θ-psh if it admits\na (necessarily unique) extension to a θ-psh function on X an .\nCorollary 4.24. If X is connected, then any 0-psh function is constant, i.e. PSH(0) = R.\nProof. By GAGA, X an is connected, and after replacing X with an irreducible component,\nwe may assume that X is irreducible. By Corollary 4.23, it is then enough to show that any\nϕ ∈ PSH(0) with sup ϕ = ϕ(vtriv ) = 0 satisfies ϕ(v) = 0 for any v ∈ X div . Consider the\ndecreasing sequence (mϕ)m∈N and its pointwise limit ψ := limm (mϕ). Since ψ(vtriv ) = 0,\nwe have ψ ∈ PSH(0) (see Theorem 4.5). By Corollary 4.17, we thus have ψ(v) > −∞, i.e.\nϕ(v) = 0.                                                                                \u0003\nCorollary 4.25. Pick a decreasing net (ϕi ) in PSH(θ), and assume that it converges to\nϕ ∈ PSH(θ). Then ϕ = limi ϕi pointwise on X an .\nProof. The pointwise limit ψ of (ϕi ) on X an coincides with ϕ on X div . In particular,\nψ(vtriv,α ) is finite for any α, and hence ψ ∈ PSH(θ), by Theorem 4.5. By Corollary 4.23, we\ninfer ϕ = ψ, which means that ϕi converges to ϕ pointwise on X an                          \u0003\nLemma 4.26. For each ψ ∈ PL(X), there exists a finite set Σ ⊂ X div such that\n                                  sup(ϕ − ψ) = max(ϕ − ψ)                                  (4.7)\n                                   X an            Σ\n\nfor all ϕ ∈ PL+ (X), and the same result then holds for all ϕ ∈ PSH(θ), θ ∈ N1 (X).\nMoreover, if ψ = r(ϕa − ρ), where r ∈ Q>0 , a is a flag ideal, and ρ ∈ PL+ (X), then we can\npick Σ = Σa , the set of Rees valuations of a.\nProof. We can always write ψ = r(ϕa − ρ) as above, and by homogeneity we may assume\nr = 1. The case ϕ ∈ PL+ (X) now follows from Lemma 2.13, since ϕ + ρ ∈ PL+ (X).\n  Now assume ϕ ∈ PSH(θ) for some θ ∈ N1 (X). After replacing θ with ω ∈ Amp(X)\nsuch that ω − θ is nef, we may assume θ = ω is ample. By Theorem 4.15, we can find a\ndecreasing net (ϕi ) in Hdom (ω) ⊂ PL+ (X) such that ϕi & ϕ. For each v ∈ X an , we then\nhave ϕi (v) − ψ(v) ≤ maxΣa (ϕi − ψ) for all i, and hence ϕ(v) − ψ(v) ≤ maxΣa (ϕ − ψ). \u0003\n\f52                      SÉBASTIEN BOUCKSOM AND MATTIAS JONSSON\n\nProof of Theorem 4.22. If ψ ∈ PL(X), the result follows from Lemma 4.26. Assume next\nψ ∈ C0 (X). By Theorem 2.2, ψ is a uniform limit of functions in PL(X), and the result\nthus holds for ψ as well. In the general case, we can find a decreasing net (ψi ) in C0 (X)\nwith ψi → ψ. Then ϕ ≤ ψ ≤ ψi on X div implies ϕ ≤ ψi on X an , and hence ϕ ≤ ψ on X an\nas well.                                                                                  \u0003\nRemark 4.27. Assume char k = 0. By Corollary A.3, any v ∈ X an is the limit of a net\n(vi ) in X div such that vi ≤ v for all i. As any ϕ ∈ PSH(θ) is decreasing and usc, it follows\nthat ϕ(vi ) → ϕ(v), which provides a slightly more precise version of Corollary 4.23 in that\ncase.\n     We record another useful consequence of Lemma 4.26.\nProposition 4.28. For any ψ ∈ C0 (X), ϕ 7→ supX an (ϕ − ψ) is continuous on PSH(θ).\nProof. When ψ is PL, this is a direct consequence of Lemma 4.26. As above, the general\ncase follows by density of PL(X) in C0 (X) with respect to uniform convergence.     \u0003\nCorollary 4.29. For any v ∈ X an , the evaluation map ϕ 7→ ϕ(v) is usc on PSH(θ).",
  "a27b6d01787f2f77554c294d08827ed78f546cef4affb8020902aff09baf58d5": "ϕ := supm ϕm . Then ϕ ≡ −∞ on E and ϕ ≡ 0 on X an \\ E. Since E has empty interior (see\nCorollary 4.39), ϕ? ≡ 0 on X an , and E = {ϕ < ϕ? } is thus negligible.             \u0003\n     Just like pluripolar sets, the class of negligible sets is birationally invariant.\nLemma 5.4. If π : Y → X is a birational morphism, then a subset E ⊂ X an is negligible\niff π −1 (E) ⊂ Y an is negligible.\nProof. We follow the setup and notation of the proof of Lemma 4.40.\n  First suppose E is negligible, and pick a family (ϕi )i in PSH(ωX ) uniformly bounded\nabove such that supi ϕi < sup?i ϕi on E. If we set ψi := π ? ϕi , then (ψi )i is a family in\nPSH(π ? ωX ) that is uniformly bounded above. Moreover, supi ψi < sup?i ψi on π −1 (E) \\ W an ,\nso π −1 (E) \\ W an is negligible. As W an is pluripolar, and hence also negligible, it follows\nthat π −1 (E) is negligible, see Lemma 5.2.\n  If instead π −1 (E) is negligible, then there exists a family (ψi )i in PSH(ωY ) uniformly\nbounded above, such that supi ψi < sup?i ψi on π −1 (E). We can find ϕi ∈ PSH(ωX ) such\n\f             GLOBAL PLURIPOTENTIAL THEORY OVER A TRIVIALLY VALUED FIELD                        57\n\nthat ψi + π ? ϕX = π ? ϕi . Then (ϕi )i is uniformly bounded above, and supi ϕi < sup?i ϕi on\nE \\ Z an , so E \\ Z an is negligible, and we conclude as above.                             \u0003\nCorollary 5.5. A subset E ⊂ X an is negligible iff E ∩ Xαan is a negligible subset of Xαan for\nall α.\n  The following result will play a crucial role in what follows.\nTheorem 5.6. Divisorial points are nonnegligible.\n  Thus non-empty open sets are also nonnegligible, as they contain divisorial points, by\ndensity of X div . The key ingredient is the following partial converse to Lemma 4.26.\nLemma 5.7. Assume that X is irreducible. Then, for each θ ∈ N1 (X) and v ∈ X div , there\nexists ψ ∈ PL(X) such that\n                            sup(ϕ − ψ) = (ϕ − ψ)(v)\n                                   X an\nfor all ϕ ∈ PSH(θ).\nProof. By Lemma 2.12 we may find a flag ideal a for which v is a Rees valuation, that is,\nv ∈ Σa . Pick L ∈ Pic(X)Q ample such that c1 (L) ≥ θ. Then PSH(θ) ⊂ PSH(L), so we may\nassume θ = c1 (L). As X is irreducible, there exists C > 0 such that |ϕ(v) − ϕ(w)| ≤ C for\nall w ∈ Σa and all ϕ ∈ PSH(L); for example, we can take C = 2 maxw∈Σa TL (w), as follows\nfrom the proof of Corollary 4.17. By Lemma 2.28 there exists m, r ≥ 1 and ρ ∈ H(L) such\nthat if we set ψ := r(ϕa − mρ), then ψ(v) = 0 and ψ(w) = 2C for w ∈ Σa , w 6= v. Then\nψ ∈ PL(X), and for any ϕ ∈ PSH(L), the max of ϕ − ψ over Σa is attained at v. On the\nother hand, it follows from Lemma 4.26 that the supremum of ϕ − ψ on X an is attained on\nΣa . The proof is complete.                                                             \u0003\nProof of Theorem 5.6. In view of Corollary 5.5 we may assume that X is irreducible. Con-\nsider θ ∈ N1 (X) and a bounded-above family (ϕi ) in PSH(θ), and set ϕ := supi ϕi . Pick v ∈\nX div , and choose a PL function ψ as in Lemma 5.7. For each i we have ϕi ≤ ϕi (v)−ψ(v)+ψ.\nThus ϕ ≤ ϕ(v) − ψ(v) + ψ, and hence ϕ? ≤ ϕ(v) − ψ(v) + ψ, by continuity of ψ. This yields\nϕ? (v) = ϕ(v), which proves that v is nonnegligible.                                       \u0003\n\n5.2. The envelope property and unibranch varieties. In the rest of §4 we assume that\nX is irreducible unless stated otherwise. (See Remark 5.15.)\nDefinition 5.8. We say that a class θ ∈ N1 (X) has the envelope property if, for any\nbounded-above family (ϕi ) in PSH(θ), the usc upper envelope sup?i ϕi is θ-psh.\n   In the complex analytic case, it is a basic fact that psh functions on domains in Cn\nsatisfy the analogue of the envelope property. As a consequence, θ-psh functions satisfy the\nenvelope property for any projective complex manifold X and any closed (1, 1)-form θ. More\ngenerally, the latter property holds when X is unibranch (i.e. locally analytically irreducible),\ncf. [Dem85, Théorème 1.7], but fails in general, for the same reason as Theorem 5.12 below.\n   With our global definition of θ-psh functions, the envelope property turns out to be\nespecially delicate. The purpose of what follows is to explore various implications, and\nestablish it in an important special case. We first observe:\nLemma 5.9. Assume that θ ∈ N1 (X) can be written as the limit of classes θj ≥ θ that\nsatisfy the envelope property. Then θ has the envelope property as well.\n\f58                       SÉBASTIEN BOUCKSOM AND MATTIAS JONSSON\n\nProof. Pick a bounded-above family (ϕi ) in PSH(θ). Since θ ≤ θj , we have PSH(θ) ⊂\nPSH(θj ). Thus sup?i ϕi is θj -psh for all j, and hence θ-psh, by Theorem 4.5.    \u0003\nCorollary 5.10. If the continuity property holds for all ω ∈ Amp(X), then it holds for all\nθ ∈ Nef(X).\n  We next prove that the envelope property is equivalent to the analogue of a basic com-\npactness property in the complex analytic case.\nTheorem 5.11. For any θ ∈ N1 (X), the following properties are equivalent:\n    (i) the envelope property holds for θ;\n   (ii) the space PSHsup (θ) := {ϕ ∈ PSH(θ) | sup ϕ = 0} is compact;\n  (iii) every bounded-above, increasing net (ϕj ) in PSH(θ) converges in PSH(θ).\nProof. Assume (i), and pick a net (ϕi ) in PSHsup (θ). By Proposition 4.38, (ϕi (v)) is a\nbounded net in R for each v ∈ X div . By Tychonoff’s theorem, after passing to a subnet,\nwe may thus assume that (ϕi ) converges pointwise on X div to a function ϕ : X div → R,\nand it suffices to show that ϕ extends to a function in PSH(θ) (necessarily unique, by\nCorollary 4.23). By (i), ψi := sup?j≥i ϕj is θ-psh for each i. The net (ψi ) is further decreasing,\nand its pointwise limit ψ := limi ψi is thus either θ-psh, or identically −∞, by Theorem 4.5.\nNow Theorem 5.6 implies that ψi = supj≥i ϕj on X div . Thus ψ = ϕ on X div . In particular,\nψ 6≡ −∞, hence ψ ∈ PSH(θ). This proves (i)⇒(ii).\n   Next, assume (ii), and consider a bounded-above, increasing net (ϕj ) in PSH(θ). Then a\nsubnet ϕji −sup ϕji converges to some ϕ ∈ PSH(θ). Since (sup ϕj ) is increasing and bounded-\nabove, it converges to some c ∈ R. Thus ϕji → ϕ + c on X div , and hence ϕj → ϕ + c on\nX div since (ϕj ) is increasing. This proves (ii)⇒(iii).\n   Finally, assume (iii). Let (ϕi )i∈I be a bounded-above family of θ-psh functions, and\nconsider the increasing net ψJ := maxi∈J ϕi parametrized by finite subsets J ⊂ I. Then ψJ\nadmits a limit ψ in PSH(θ), and we claim that ψ = sup?i ϕi . On X div we have\n                              ψ = lim max ϕi = supi ϕi = sup?i ϕi ,\n                                    J   i∈J\nby Theorem 5.6. Since ψ is θ-psh and sup?i ϕi is usc, Theorem 4.22 yields ψ ≤ sup?i ϕi on\nX an . Similarly, Theorem 4.22 yields ϕi ≤ ψ, and hence sup?i ϕi ≤ ψ, since ψ is usc. This\nproves the claim, and hence (iii)⇒(i).                                                  \u0003\n   Recall that the variety X is said to be unibranch if the following equivalent conditions\nhold (see [EGA, IV.7.6.3] and [Kol16, Corollary 32]):\n      • the normalization morphism ν : X ν → X is a homeomorphism;\n      • the formal completion of X at each of its points is irreducible.\nIn particular, any normal variety is unibranch. When k = C, X is unibranch iff the associated\ncomplex analytic space is locally irreducible in the analytic topology. This is also true for\nthe Berkovich analytification as considered in this paper: the variety X is unibranch iff\nthe k-analytic space X an is locally irreducible in the analytic topology (see [Duc09, Lemme\n5.19]).\nTheorem 5.12. If the envelope property holds for some ω ∈ Amp(X), then X is necessarily\nunibranch.\n  The analogue of this result is known in the complex analytic setting, too. We have not\nbeen able to locate a precise reference, but the proof below of Theorem 5.12 can easily be\nadapted to that setting.\n\f            GLOBAL PLURIPOTENTIAL THEORY OVER A TRIVIALLY VALUED FIELD                     59\n\nLemma 5.13. Let π : Y → X be a birational morphism. Pick θ ∈ N1 (X), and assume that\nθ can be written as the limit of a sequence of classes θm > θ with the envelope property.\n                  ∼\nThen π ? : PSH(θ) → PSH(π ? θ) is a homeomorphism.\n  Recall that θm > θ means that θm − θ is ample.\n\nProof. After passing to a subsequence, we may assume that θm > θm+1 for all m, and hence\n                                                           ∼\nPSH(θm+1 ) ⊂ PSH(θm ). Since π induces a bijection Y div → X div , π ? : PSH(θ) → PSH(π ? θ)\nis a topological embedding, and it suffices to show that it is onto. Pick ψ ∈ PSH(π ? θ), and\nwrite π as the blowup of an ideal b ⊂ OX . By Theorem 4.32, there exists a sequence εm & 0\nsuch that ψ + εm π ? log |b| = π ? ϕm with ϕm ∈ PSH(θm ). By Theorem 4.22, ϕm is uniquely\ndetermined, and (ϕm )m≥m0 is an increasing sequence in PSH(θm0 ) for any given m0 . By\nTheorem 5.11, ϕm converges pointwise on X div to ϕ ∈ PSH(θ), which satisfies ψ = π ? ϕ on\nY div . The result follows.                                                                 \u0003\n\nProof of Theorem 5.12. Since the normalization morphism ν : X ν → X is finite, ν ? ω is\nample, and hence Hdom (ν ? ω) spans PL(X ν ), see (3.2). By Lemma 2.3, PL(X ν ) separates\nthe points of (X ν )an , and it is thus already the case of Hdom (ν ? ω). On the other hand,\nLemma 5.13 implies that all functions in Hdom (ν ? ω) ⊂ PSH(ν ? ω) descend to X an (take ωm =\n(1 + m−1 )ω). As a consequence, ν an : (X ν )an → X an is injective. By the non-Archimedean\nGAGA principle, this implies that ν : X ν → X is injective as well (see [Berk90, §3.4]); this\nis enough to conclude that ν is a homeomorphism, and hence that X is unibranch.             \u0003\n\n   As mentioned above, in the complex analytic case the envelope property conversely holds\nas soon as X is unibranch. It is thus natural to conjecture:\nConjecture 5.14. If X is unibranch, then the envelope property holds for all θ ∈ N1 (X).\n  We will establish this conjecture in the important special case where θ is ample, X is\nsmooth, and char k = 0 (see Theorem 5.20).",
  "9e9789c16e6e0105ad20368fdf05e44daabb8ecbe2cb583d8790c7662ddb1ebd": "5.3. Envelopes. For ample classes, the envelope property admits a useful reformulation.\nWe continue to assume that X is irreducible unless stated otherwise. Fix a class ω ∈\nAmp(X).\nDefinition 5.16. The ω-psh envelope of a function ϕ : X an → R ∪ {±∞} is the function\nPω (ϕ) : X an → R ∪ {±∞} defined as the pointwise supremum\n                           Pω (ϕ) := sup {ψ ∈ PSH(ω) | ψ ≤ ϕ} .\n  Thus Pω (ϕ) ≡ −∞ iff there is no ψ ∈ PSH(ω) with ψ ≤ ϕ. Despite the name, Pω (ϕ) is\nnot always ω-psh (and indeed not even usc in general). However, it is clear that\n     • ϕ 7→ Pω (ϕ) is increasing;\n     • Pω (ϕ + c) = Pω (ϕ) + c for all c ∈ R.\n\f60                        SÉBASTIEN BOUCKSOM AND MATTIAS JONSSON\n\nThese properties formally imply the Lipschitz estimate\n                               sup Pω (ϕ) − Pω (ϕ0 ) ≤ sup |ϕ − ϕ0 |.                     (5.1)\nwhen ϕ, ϕ0 are bounded.\nLemma 5.17. For any ω ∈ Amp(X), the following statements are equivalent:\n   (i) ω has the envelope property;\n  (ii) for any function ϕ : X an → R ∪ {±∞}, we have\n                      Pω (ϕ) ≡ −∞, Pω (ϕ)? ≡ +∞, or Pω (ϕ)? ∈ PSH(ω).\n     (iii) for any ϕ ∈ C0 (X), Pω (ϕ) is continuous.\n     We refer to the property in (iii) as continuity of envelopes.\nProof. First assume (i). Pick any ϕ : X an → R ∪ {±∞}, and suppose that the set F :=\n{ψ ∈ PSH(θ) | ψ ≤ ϕ} is nonempty, so that Pω (ϕ) 6≡ −∞. If the functions in F are uniformly\nbounded above, then Pω (ϕ)? ∈ PSH(ω), by (i). If not, then, by the definition of the\nAlexander–Taylor capacity we have\n             Pω (ϕ)(v) = sup {ψ(v) | ψ ∈ F} ≥ sup {sup ψ | ψ ∈ F} − Tω (v) = +∞\nfor all v ∈ X div , and hence Pω (ϕ)? ≡ +∞, by density of X div . This proves (i)⇒(ii).\n   Next we prove (ii)⇒(iii), so pick ϕ ∈ C0 (X). Then Pω (ϕ)? ∈ PSH(ω) is a competitor in\nthe definition of Pω (ϕ), and hence Pω (ϕ)? ≤ Pω (ϕ). We conclude that Pω (ϕ)? = Pω (ϕ) is\nusc. We claim that Pω (ϕ) is also lsc, and hence continuous. To prove the claim, it suffices to\nshow that Pω (ϕ) is a supremum of continuous functions, and for this it suffices to prove that\nfor any ψ ∈ PSH(ω) with ψ ≤ ϕ and any ε > 0, there exists ψ 0 ∈ C0 (X) with ψ ≤ ψ 0 ≤ ϕ+ε.\nPick a decreasing net ψi ∈ Hdom (ω) converging pointwise to ψ. For each v ∈ X an , the set\n{ψi < ϕ + ε} is an open neighborhood of v for i large enough, by lower semicontinuity of\nϕ − ψi . By compactness of X an , it follows that ψi < ϕ + ε for all i large enough, so we can\ntake ψ 0 = ψi .\n   Finally, we prove (iii)⇒(i), following [BE20, Lemma 7.30]. Let (ϕi ) be a bounded-above\nfamily in PSH(ω), and set ϕ := sup?i ϕi . Since ϕ is usc and X an is compact, we can find\na decreasing net of continuous functions (ψj ) such that ψj → ϕ. For each i, j, we have\nϕi ≤ ψj , and hence ϕi ≤ Pω (ψj ), which in turn yields ϕ ≤ Pω (ψj ) ≤ ψj . We have thus\nwritten ϕ as the limit of the decreasing net of ω-psh functions Pω (ψj ), which shows that ϕ\nis ω-psh.                                                                                    \u0003\nCorollary 5.18. Assume that ω ∈ Amp(X) has the envelope property, and consider a usc\nfunction ϕ : X an → R ∪ {−∞}. Then:\n    (i) Pω (ϕ) is ω-psh, or Pω (ϕ) ≡ −∞;\n   (ii) if ϕ is the limit of a decreasing net (ϕj ) of bounded-above, usc functions, then\n        Pω (ϕj ) & Pω (ϕ).\nProof. By Lemma 5.17, either ψ := Pω (ϕ)? is ω-psh, or Pω (ϕ) ≡ −∞. Since Pω (ϕ) ≤ ϕ and\nϕ is usc, we also have ψ ≤ ϕ. If ψ is ω-psh, then ψ ≤ Pω (ϕ), which proves (i).\n  To see (ii), note that ρ := limj Pω (ϕj ) satisfies either ρ ∈ PSH(ω) or ρ ≡ −∞, by\nTheorem 4.7. Furthermore, Pω (ϕj ) ≤ ϕj yields in the limit ρ ≤ ϕ, and hence ρ ≤ Pω (ϕ) (by\ndefinition of Pω (ϕ) if ρ ∈ PSH(ω), and trivially if ρ ≡ −∞). Thus limj Pω (ϕj ) = ρ = Pω (ϕ).\nOn the other hand, Pω (ϕj ) ≥ Pω (ϕ) implies ρ ≥ Pω (ϕ), which completes the proof of (ii). \u0003\n\f              GLOBAL PLURIPOTENTIAL THEORY OVER A TRIVIALLY VALUED FIELD                      61\n\n  For any function ϕ : X an → R ∪ {±∞}, we also introduce the pointwise envelope\n                           Qω (ϕ) := sup {ψ ∈ CPSH(ω) | ψ ≤ ϕ} ;\nthis is lsc and bounded below if ϕ is bounded below, and ≡ −∞ otherwise. Since each\nψ ∈ CPSH(ω) is the uniform limit of functions in Hdom (ω) (see Theorem 4.7), one easily\nchecks that\n                            Qω (ϕ) = sup{ψ ∈ Hdom (ω) | ψ ≤ ϕ}.\nLemma 5.19. Suppose ϕ : X an → R ∪ {+∞} is bounded below, with lsc regularization\nϕ? : X an → R ∪ {+∞}. Then:\n     (i) Qω (ϕ) = Pω (ϕ? );\n    (ii) Qω (ϕ) ∈ C0 (X) ⇐⇒ Qω (ϕ) ∈ PSH(ω);\n   (iii) if ϕ is the pointwise limit of an increasing net (ϕj ) of bounded-below, lsc functions\n         (and hence ϕ is lsc), then Pω (ϕj ) % Pω (ϕ).\nProof. A function ψ ∈ CPSH(ω) satisfies ψ ≤ ϕ iff ψ ≤ ϕ? . Thus Qω (ϕ) = Qω (ϕ? ), and we\nmay therefore assume wlog that ϕ is lsc. Trivially, Pω (ϕ) ≥ Qω (ϕ). Pick ψ ∈ PSH(ω) such\nthat ψ ≤ ϕ, and let (ψi ) be a decreasing net in CPSH(ω) converging pointwise to ψ. For\neach ε > 0 and v ∈ X an , we can find i such that {ψi < ϕ + ε} is an open neighborhood of\nv, by lower semicontinuity of ϕ − ψi . By compactness of X an , it follows that ψi < ϕ + ε for\nall i large enough. Thus ψ ≤ ψi ≤ Qω (ϕ + ε) = Qω (ϕ) + ε, which proves (i).\n   As noted above, Qω (ϕ) is lsc and bounded below. If Qω (ϕ) is ω-psh, then it is in particular\nusc, and hence Qω (ϕ) ∈ C0 (X). Assume, conversely, that Qω (ϕ) ∈ C0 (X). Since CPSH(ω)\nis stable under finite maxima, Qω (ϕ) is the pointwise limit of an increasing net (ψi ) in\nCPSH(ω). By Dini’s lemma, ψi → Qω (ϕ) uniformly on X an , and hence Qω (ϕ) ∈ PSH(ω),\nby Theorem 4.7. This proves (ii).\n   Consider finally a net (ϕj ) as in (iii). We trivially have limj Pω (ϕj ) = supj Pω (ϕj ) ≤\nPω (ϕ). Pick ε > 0 and ψ ∈ CPSH(ω) such that ψ ≤ ϕ. As above, for all j large enough\nwe have ψ ≤ ϕj + ε, and hence ψ ≤ Pω (ϕj ) + ε. Thus Pω (ϕ) ≤ supj Pω (ϕj ), and we are\ndone.                                                                                         \u0003\n",
  "d3ca4292fe8b2ed4ba44e91cdfe75dcc582672904b6fd48fb43a478b9daba779": "would not be particularly useful unless we have examples of classes where the envelope\nproperty holds. Arguing along the lines of [BFJ16, Theorem 8.5], we will prove:\nTheorem 5.20. Assume that X is smooth and connected, and that either char k = 0 or\ndim X ≤ 2. Then any θ ∈ Nef(X) has the envelope property.\n  We do not know whether a class θ ∈ N1 (X) that is not nef has the envelope property.\nCorollary 5.21. Under the assumptions of Theorem 5.20, the set\n                           PSHsup (θ) = {ϕ ∈ PSH(θ) | sup ϕ = 0}\nis compact.\n  In [BFJ16], the above compactness property was established in the discretely valued\ncase, by relying on much more involved arguments based on dual complexes and toroidal\nmodifications.\n\f62                      SÉBASTIEN BOUCKSOM AND MATTIAS JONSSON\n\nLemma 5.22. Let L be an ample line bundle on X, and (X , L) a test configuration for\n(X, L), with L an honest line bundle. Denote by am ⊂ OX the base ideal of mL, which is a\nvertical ideal of X for all m \u001d 1. Then\n                       PL (ϕL ) − ϕL = sup m−1 ϕam = lim m−1 ϕam\n                                       m≥1             m→∞\n\npointwise on X an . Furthermore, PL (ϕL ) is continuous iff m−1 ϕam converges uniformly on\nX an .\n  As with flag ideals, see §2.1, the function ϕam ∈ PL(X) is defined by ϕam (v) = −σ(v)(am ),\nwhere σ = σX denotes Gauss extension (see Remark 1.9).\nProof. Set ϕm := ϕL + m−1 ϕam . Note first that (am )m is a graded sequence of ideals, i.e.\nam · am0 ⊂ am+m0 for all m, m0 ∈ N. The sequence m 7→ ϕam is thus superadditive, and\nFekete’s lemma yields supm≥1 m−1 ϕam = limm→∞ m−1 ϕam .\n  Next write L = LX + D with a vertical Cartier divisor D on X , so that ϕL = ϕD . For\neach m, denote by µm : Xm → X the integral closure of the blowup along am , and by Dm the\n(antieffective) divisor on Xm such that OXm · am = OXm (Dm ); thus ϕm = ϕD + m−1 ϕDm .\nBy construction, OX (mL) ⊗ am is globally generated. This implies that\n                         µ? (mL) + Dm = mLXm + µ? (mD) + Dm\nis nef, and hence ϕm ∈ PL ∩ PSH(L). Furthermore, ϕDm ≤ 0, so ϕm ≤ ϕL , and hence\nϕm ≤ PL (ϕL ), which proves\n                               sup ϕm = lim ϕm ≤ PL (ϕL ).\n                               m≥1       m→∞\n\nConversely, Lemma 5.19 implies\n                      PL (ϕL ) = QL (ϕL ) = sup {ψ ∈ H(L) | ψ ≤ ϕL } .\nPick ψ ∈ H(L) with ψ ≤ ϕL . After replacing X with a higher test configuration, we may\nand do assume, for the sake of notational simplicity, that ψ is determined by a vertical\nQ-Cartier divisor E on X . For m large and divisible enough, Theorem 2.31 shows that\nmLX + mE = mL + m(E − D) is globally generated, and hence OX (m(E − D)) ⊂ am . This\nyields\n                             m(ψ − ϕL ) = ϕm(E−D) ≤ ϕam ,\nand hence ψ ≤ ϕm , which yields, as desired, the converse inequality\n                      PL (ϕL ) = sup {ψ ∈ H(L) | ψ ≤ ϕL } ≤ sup ϕm .\n                                                               m\nThe final assertion is a simple consequence of Dini’s lemma, using the superadditivity of\nm 7→ mϕm .                                                                             \u0003\nProof of Theorem 5.20. By Lemma 5.9, we may assume that θ = c1 (L) with L ∈ Pic(X)Q\nample. Pick ϕ ∈ C0 (X). By Lemma 5.17, we need to show that PL (ϕ) is continuous. Since\nPL(X) is dense in C0 (X) with respect to uniform convergence (see Theorem 2.2), we may\nassume ϕ ∈ PL(X), by (5.1). By Theorem 2.31, we have ϕ = ϕL for a test configuration\n(X , L) for (X, L). After replacing L with a multiple, we may further assume that L and L\nare honest line bundle.\n   Using the notation of Lemma 5.22, we need to show that ϕm := ϕL + m−1 ϕam converges\nuniformly to PL (ϕL ). Since we assume that char k = 0 or dim X ≤ 2 (and hence dim X ≤ 3),\nwe can rely on resolution of singularities and assume that X is smooth and X0 has simple\n\f             GLOBAL PLURIPOTENTIAL THEORY OVER A TRIVIALLY VALUED FIELD                         63\n\nnormal crossings support. We may also assume that there exists an effective vertical Q-\ndivisor E on X such that A := L − E is ample.\n   Assume first that char k = 0, and let bm be the multiplier ideal of the graded sequence am\n                                                                                            • .\n                                                            l\nThe inclusion am ⊂ bm is elementary, and we have bml ⊂ bm for all m, l by the subadditivity\nof multiplier ideals. This implies that\n                      m−1 ϕbm ≥ (ml)−1 ϕbml ≥ (ml)−1 ϕaml ≥ m−1 ϕam\nfor all sufficiently divisible m and l. Letting l → ∞ shows that\n                                ϕL + m−1 ϕbm ≥ PL (ϕL ) ≥ ϕm                                (5.2)\nfor all sufficiently divisible m. By the uniform global generation of multiplier ideals there\nexists m0 ∈ N such that\n\n               OX (mL + m0 A) ⊗ bm = OX ((m + m0 )L) ⊗ OX (−m0 E) ⊗ bm\n  is globally generated for all sufficiently divisible m. This implies that\n                                      ϕbm ≤ ϕam+m0 + C\nfor a constant C independent of m. Combining this with (5.2) yields\n\n                                            m0            m0        C\n                       ϕm ≤ PL (ϕL ) ≤ (1 +    )ϕm+m0 −       ϕL + ,\n                                            m              m        m\nfor all sufficiently divisible m. This shows that PL (ϕL ) is a uniform limit of continuous\nfunctions, and hence continuous.\n   When char k > 0, the very same argument applies with test ideals in place of multiplier\nideals, see [GJKM17] for details.                                                        \u0003\nRemark 5.23. In view of Remark 5.15, Theorem 5.20 is valid also when X is smooth but\npossibly disconnected. A suitable version of Corollary 5.21 is also true.",
  "16208ee6a6df43b461fc984129af92d717f5b0c859850f1d2c91e95d572cb474": "       7. Functions of finite energy and mixed Monge–Ampère measures\n   In this section, X denotes a projective variety of dimension n, with irreducible components\nXα . We extend the energy pairing to arbitrary psh functions, and use this to define functions\nof finite energy, and the mixed Monge–Ampère operator thereon.\n7.1. Extending the energy pairing. In §3.2, the energy pairing\n                                  (θ0 , ϕ0 ) · . . . · (θn , ϕn ) ∈ R\nwas defined for pairs (θi , ϕi ) ∈ N1 (X) × PLR . When the ϕi are θi -psh, this is an increasing\nfunction of the ϕi , by Lemma 3.15. On the other hand, any ω-psh function with ω ∈\nAmp(X) can be written as a decreasing limit of functions in Hdom (ω) ⊂ PL ∩ PSH(ω) (see\nTheorem 4.15). This allows to extend the energy pairing by monotonicity, as follows.\n\f                GLOBAL PLURIPOTENTIAL THEORY OVER A TRIVIALLY VALUED FIELD                                                       75\n\nTheorem 7.1. For each (n + 1)-tuple ω0 , . . . , ωn ∈ Amp(X), the energy pairing\n                           (ϕ0 , . . . , ϕn ) 7→ (ω0 , ϕ0 ) · . . . · (ωn , ϕn )\nadmits a unique extension to a map ni=0 PSH(ωi ) → R ∪ {−∞} that is\n                                          Q\n\n     • upper semicontinuous;\n     • increasing in each variable.\nFurthermore, this map is continuous along decreasing nets, and satisfies\n                  (ω0 , ϕ0 ) · . . . · (ωn , ϕn ) =             inf             (ω0 , ψ0 ) · . . . · (ωn , ψn )              (7.1)\n                                                       ψi ∈Hdom (ωi ), ψi ≥ϕi\n                  Q\nfor all (ϕi ) ∈       i PSH(ωi ).\n\nProof. Any map that is both usc and increasing is automatically continuous along decreasing\nnets. Since all functions in PSH(ωi ) are limits of decreasing nets in Hdom (ωi ) ⊂ PL(X) ∩\nPSH(ωi ), uniqueness is clear. To prove existence, it suffices to show that (7.1) has the\nrequired properties.\n  Monotonicity is obvious. To prove upper semicontinuity, suppose that ϕi ∈ PSH(ωi ),\n0 ≤ i ≤ n, and t ∈ R satisfy\n                                (ω0 , ϕ0 ) · . . . · (ωn , ϕn ) < t,\nBy definition, we can choose ψi ∈ Hdom (ωi ) and 0 < ε \u001c 1 such that ϕi ≤ ψi and\n                                        (ω0 , ψ0 ) · . . . · (ωn , ψn ) < t − ε.\nSet                                          X\n                                     C :=     (ω0 · . . . · ωbi · . . . · ωn ) > 0.\n                                               i\nBy Proposition 4.28, ϕ 7→ sup(ϕ − ψi ) is continuous on PSH(ωi ), and we can thus find an\nopen neighborhood Ui of ϕi in PSH(ωi ) such that ϕ0i ≤ ψi + εC −1 for all ϕ0i ∈ Ui . By\nmonotonicity of the energy pairing and Proposition 3.14, this gives\n                   (ω0 , ϕ00 ) · . . . · (ωn , ϕ0n ) ≤ (ω0 , ψ0 + εC −1 ) · . . . · (ωn , ψn + εC −1 )\n                                = (ω0 , ψ0 ) · . . . · (ωn , ψn ) + ε < t\n         0\nfor all ϕi ∈ Ui , which proves upper semicontinuity.                                                                             \u0003\nProposition 7.2. The energy pairing (ω0 , ϕ0 ) · . . . · (ωn , ϕn ) is symmetric and R>0 -linear\nwith respect to each variable (ωi , ϕi ) with ωi ∈ Amp(X) and ϕi ∈ PSH(ωi ). Furthermore,\n\n                                                                                    n\n                                                                                    X\n (ω0 , ϕ0 + c0 ) · . . . · (ωn , ϕn + cn ) = (ω0 , ϕ0 ) · . . . · (ωn , ϕn ) +            ci (ω0 · . . . · ωbi · . . . · ωn )X (7.2)\n                                                                                    i=0\nfor all ci ∈ R,\n                         (ω0 , t · ϕ0 ) · . . . · (ωn , t · ϕn ) = t(ω0 , ϕ0 ) · . . . · (ωn , ϕn )                          (7.3)\nfor all t ∈ R>0 ,\n                                                          X\n                   (ω0 , ϕ0 ) · . . . · (ωn , ϕn ) =              (ω0 , ϕ0 )|Xα · . . . · (ωn , ϕn )|Xα ,                    (7.4)\n                                                       dim Xα =n\nand\n                 (ν ? ω0 , ν ? ϕ0 ) · . . . · (ν ? ωn , ν ? ϕn ) = (ω0 , ϕ0 ) · . . . · (ωn , ϕn )                           (7.5)\nwith ν : X ν → X the normalization morphism.\n\f76                                 SÉBASTIEN BOUCKSOM AND MATTIAS JONSSON\n\nProof. Using approximation by decreasing nets in Hdom (ωi ), everything is clear from Propo-\nsition 3.14, except that this only provides a proof of (7.3) for t ∈ Q>0 . To get the general\ncase, we may replace ϕi with ϕi − sup ϕi and assume ϕi ≤ 0 for all i. Write a given t ∈ R>0\nas the limit of an increasing sequence tm ∈ Q>0 . For each i, (tm · ϕi )m is a decreasing\nsequence in PSH(ωi ) that converges to t · ϕi , and hence\n                    lim (ω0 , tm · ϕ0 ) · . . . · (ωn , tm · ϕn ) = (ω0 , t · ϕ0 ) · . . . · (ωn , t · ϕn ).\n                   m→∞\nThe result follows.                                                                                                           \u0003\n     We also record the following useful monotonicity property with respect to ωi .\nProposition 7.3. For i = 0, . . . , n, pick ωi , ωi0 ∈ Amp(X) such that ωi0 ≥ ωi , and ϕi ∈\nPSH(ωi ) ⊂ PSH(ωi0 ). Then\n   (i) if ϕi ≤ 0 for all i, then (ω00 , ϕ0 ) · . . . · (ωn0 , ϕn ) ≤ (ω0 , ϕ0 ) · . . . · (ωn , ϕn ) ≤ 0;\n  (ii) if ϕi ≥ 0 for all i, then (ω00 , ϕ0 ) · . . . · (ωn0 , ϕn ) ≥ (ω0 , ϕ0 ) · . . . · (ωn , ϕn ) ≥ 0.\nProof. By monotone approximation, we may assume ϕi ∈ PL ∩ PSH(ωi ). By assumption,\nθi := ωi0 − ωi is nef. The result thus follows by expanding out\n                 (ω00 , ϕ0 ) · . . . · (ωn0 , ϕn ) = ((ω0 , ϕ0 ) + (θ0 , 0)) · . . . · ((ωn , ϕn ) + (θn , 0))\nand applying Corollary 3.16.                                                                                                  \u0003\n  For any θ ∈ N1 (X), recall that CPSH(θ) = C0 (X) ∩ PSH(θ) ⊂ E ∞ (θ) respectively denote\nthe sets of continuous and bounded θ-psh functions. We conclude this section with a general\ncontinuity result for the energy pairing involving such functions. It is an analogue of the\nChern–Levine–Nirenberg inequality in the complex case.\nTheorem 7.4. For all ω0 , . . . , ωn ∈ Amp(X), the energy pairing\n                                      (ϕ0 , . . . , ϕn ) 7→ (ω0 , ϕ0 ) · . . . · (ωn , ϕn )\nis finite-valued and continuous on PSH(ω0 )× ni=1 CPSH(ωi ) with its natural topology (point-\n                                                              Q\n\nwise convergence on X div for the first factor, and uniform convergence for the other ones).\nLemma 7.5. Pick (ϕ0 , . . . , ϕn ) ∈ PSH(ω0 ) × ni=1 E ∞ (ωi ). Then:\n                                                                Q\n\n      (i) (ω0 , ϕ0 ) · . . . · (ωn , ϕn ) ∈QR is finite;\n     (ii) for any (ϕ01 , . . . , ϕ0n ) ∈ ni=1 E ∞ (ωi ) we have\n                                                                                                          n\n                                                                                                          X\n     (ω0 , ϕ0 ) · (ω1 , ϕ1 ) · . . . · (ωn , ϕn ) − (ω0 , ϕ0 ) · (ω1 , ϕ01 ) · . . . · (ωn , ϕ0n )   ≤C         sup |ϕi − ϕ0i |\n                                                                                                          i=1\n                                                                                                                           (7.6)\n            with C := max1≤i≤n (ω0 · . . . · ωbi · . . . · ωn ).\n     We emphasize that the estimate is uniform with respect to ϕ0 .\nProof. For any t ∈ R such that ϕi ≥ t for i ≥ 1, (7.2) yields\n                       (ω0 , ϕ0 ) · . . . · (ωn , ϕn ) ≥ (ω0 , ϕ0 ) · (ω1 , 0) · . . . · (ωn , 0) + ntC.                   (7.7)\nTo prove (i) we may therefore assume ϕi = 0 for 1 ≤ i ≤ n. For ϕ0 ∈ PLR , (7.4) and (3.5)\nyield                                                   X\n             (ω0 , ϕ0 ) · (ω1 , 0) · . . . · (ωn , 0) =   ϕ0 (vtriv,α )(ω1 · . . . · ωn )|Xα\n                                                               dim Xα =n\nBy monotone approximation, this remains true for all ϕ0 ∈ PSH(ω0 ), proving (i).\n\f                GLOBAL PLURIPOTENTIAL THEORY OVER A TRIVIALLY VALUED FIELD                                                    77\n\n  For (ii), we may assume that ϕi = ϕ0i for i > 1, by multilinearity and symmetry. Then\nϕ1 ≤ ϕ01 + sup |ϕ1 − ϕ01 | implies\n    (ω0 , ϕ0 ) · . . . · (ωn , ϕn ) ≤ (ω0 , ϕ0 ) · (ω1 , ϕ01 ) · (ω2 , ϕ2 ) · . . . · (ωn , ϕn ) + C sup |ϕ1 − ϕ01 |,\nusing again (7.2). The result follows.                                                                                        \u0003\nProof of Theorem 7.4. Assume first that all ϕi are PL, and pick an integrally closed test\nconfiguration X dominating Xtriv and Bi ∈ VCar(X )Q such that ϕi = ϕBi for i = 1, . . . , n.\nBy (3.5), we have\n  (ω0 , ϕ0 ) · . . . · (ωn , ϕn ) = (ω0 , 0) · (ω1 , ϕ1 ) · . . . · (ωn , ϕn )\n                                                 X\n                                              +       bE ϕ0 (vE )(ω1,X + B1 )|E · . . . · (ωn,X + Bn )|E (7.8)\n                                                   E\nwith E ranging over all irreducible components of X0 . By continuity along decreasing nets,\nthis remains true for any ϕ0 ∈ PSH(ω0 ), and shows that ϕ0 7→ (ω0 , ϕ0 )·(ω1 , ϕ1 )·. . .·(ωn , ϕn )\nis continuous on PSH(ω0 ) when ϕi is PL for i ≥ 1.\n   Assume next ϕi ∈ CPSH(ωi ) for i = 1, . . . , n. For each i ≥ 1, we can choose a sequence\n(ϕij )j in Hdom (ωi ) ⊂ PL ∩ PSH(ωi ) converging uniformly to ϕi . By (7.6), the sequence of\ncontinuous functions on PSH(ω0 )\n                                   ϕ0 7→ (ω0 , ϕ0 ) · (ω1 , ϕ1j ) · . . . · (ωn , ϕnj )\nconverges uniformly to\n                                    ϕ0 7→ (ω0 , ϕ0 ) · (ω1 , ϕ1 ) · . . . · (ωn , ϕn ),\nwhich is therefore continuous as well. Finally consider an arbitrary convergent net\n                                    (ϕ0j , ϕ1j , . . . , ϕnj ) → (ϕ0 , ϕ1 , . . . , ϕn )\n                   Qn\nin PSH(ω0 ) × i=1 CPSH(ωi ), so that ϕ0j → ϕ0 in PSH(ω0 ) (i.e. pointwise on X div ) and\nϕij → ϕi uniformly for i ≥ 1. Write\n  (ω0 , ϕ0j ) · . . . · (ωn , ϕnj ) − (ω0 , ϕ0 ) · . . . · (ωn , ϕn )\n            = [(ω0 , ϕ0j ) · (ω1 , ϕ1j ) · . . . · (ωn , ϕnj ) − (ω0 , ϕ0j ) · (ω1 , ϕ1 ) · . . . · (ωn , ϕn )]\n                         + [(ω0 , ϕ0j ) · (ω1 , ϕ1 ) · . . . · (ωn , ϕn ) − (ω0 , ϕ0 ) · (ω1 , ϕ1 ) · . . . · (ωn , ϕn )] .\nBy (7.6), the first term tends to 0 as j → ∞, while the previous step of the proof shows\nthat the second term tends to 0 as well, so we are done.                              \u0003\n7.2. Functions of finite energy.\nDefinition 7.6. For each ω ∈ Amp(X), we define the Monge–Ampère energy functional\n                                            Eω : PSH(ω) → R ∪ {−∞}\nby setting, for ϕ ∈ PSH(ω),\n                                             (ω, ϕ)n+1\n                                               Eω (ϕ) :=  .                                                            (7.9)\n                                            (n + 1)(ω n )\nWe say that ϕ has finite energy if Eω (ϕ) > −∞.\n  We denote by\n                                       E 1 (ω) ⊂ PSH(ω)\nthe set of ω-psh functions of finite energy.\n\f78                                SÉBASTIEN BOUCKSOM AND MATTIAS JONSSON\n\nProposition 7.7. For each ω ∈ Amp(X), the functional Eω : PSH(ω) → R∪{−∞} satisfies:\n    (i) Eω is increasing, concave, usc, and continuous along decreasing nets;\n   (ii) Eω (ϕ + c) = Eω (ϕ) + c for ϕ ∈ PSH(ω) and c ∈ R;\n  (iii) for each ϕ ∈ PSH(ω) and t ∈ R>0 we have Eω (t·ϕ) = t Eω (ϕ) and Etω (tϕ) = t Eω (ϕ);\n  (iv) for each ϕ ∈ PSH(ω) we have\n                                   X\n                          Eω (ϕ) =    cα Eω|Xα (ϕ|Xαan ) = Eν ? ω (ν ? ϕ)             (7.10)\n                                                       α\n           with cα    := (ω n )   Xα   /(ω n )   X and ν : X\n                                                               ν → X the normalization morphism.\n                                                                      P\n     Note that cα > 0 iff Xα is top-dimensional, and                      α cα = 1.\n\nProof. Concavity follows from Theorem 3.25, by monotone approximation. The rest of (i)–\n(ii) and the first half of (iii) are consequences of Proposition 7.2. Pick ϕ ∈ PSH(ω). For any\nt ∈ R>0 , tϕ ∈ PSH(tω) satisfies\n                                              (tω, tϕ)n+1        (ω, ϕ)n+1\n                           Etω (tϕ) =                       = t               = t Eω (ϕ),\n                                            (n + 1)((tω)n )     (n + 1)(ω n )\nwhich concludes the proof of (iii). Finally, (iv) is a consequence of (7.4).                       \u0003\nTheorem 7.8. Given ample classes ω, ω 0 , ω0 , . . . , ωn ∈ Amp(X), we have:\n    (i) E 1 (ω) is a convex subset of PSH(ω), and contains all bounded ω-psh functions;\n   (ii) E 1 (ω) is stable under addition of a constant and the scaling action of R>0 ;\n  (iii) if ϕ ∈ E 1 (ω), then any ψ ∈ PSH(ω) such that ψ ≥ ϕ is also in E 1 (ω);\n  (iv) if ω ≤ ω 0 then E 1 (ω) ⊂ E 1 (ω 0 );\n   (v) E 1 (tω) = t E 1 (ω) for all t ∈ R>0 , and\n                                             E 1 (ω) + E 1 (ω 0 ) ⊂ E 1 (ω + ω 0 );\n      (vi) if ϕi ∈ E 1 (ωi ), i = 0, . . . , n, then (ω0 , ϕ0 ) · . . . · (ωn , ϕn ) is finite;\n     (vii) if ϕ ∈ PSH(ω) then\n                    ϕ ∈ E 1 (ω) ⇐⇒ ν ? ϕ ∈ E 1 (ν ? ω)\n                    ⇐⇒ ϕ|Xαan ∈ E 1 (ω|Xα ) for all top-dimensional components Xα .\nLemma 7.9. Pick ω, ω 0 ∈ Amp(X) and t ≥ 1 such that ω ≤ ω 0 ≤ tω. For all nonpositive\nϕ ∈ PSH(ω) ⊂ PSH(ω 0 ) we have\n                                   0 ≥ (ω, ϕ)n+1 ≥ (ω 0 , ϕ)n+1 ≥ tn (ω, ϕ)n+1 .\nProof. By Proposition 7.3 we have\n                      0 ≥ (ω, ϕ)n+1 ≥ (ω 0 , ϕ)n+1 ≥ (tω, ϕ)n+1 = tn+1 (ω, t−1 ϕ)n+1 .\nSince ϕ ∈ PSH(ω) and t−1 ∈ [0, 1], concavity of the energy yields (ω, t−1 ϕ)n+1 ≥ t−1 (ω, ϕ)n+1 ,\nand the result follows.                                                                      \u0003\nLemma 7.10. Pick r ≥ 1, ω0 , . . . , ωr ∈ Amp(X), 0 ≥ ϕi ∈ PSH(ωi ) for i = 0, . . . , r.\nAssume also given t ≥ 1 such that ωi ≤ tωj for all i, j. Then\n                                      !n+1\n                         X       X                     X\n                            ωi ,   ϕi      ≥ Cr,n trn     (ωi , ϕi )n+1        (7.11)\n                                        i          i                        i\nwith Cr,n     := (2r r!)n .\n\f             GLOBAL PLURIPOTENTIAL THEORY OVER A TRIVIALLY VALUED FIELD                               79\n\n                                            t\nProof. Assume first r = 1. Set ω̃ := 1+t      (ω0 + ω1 ), and observe that ω0 ≤ ω̃ ≤ tω0 and\nω1 ≤ ω̃ ≤ tω1 . Thus\n                                                             \u0001n+1\n  (ω0 + ω1 , ϕ0 + ϕ1 )n+1 = 2n+1 21 (ω0 + ω1 ), 21 (ϕ0 + ϕ1 )\n                                          \u0001n+1       \u0010                          \u0011\n                 ≥ 2n+1 ω̃, 21 (ϕ0 + ϕ1 )      ≥ 2n (ω̃, ϕ0 )n+1 + (ω̃, ϕ1 )n+1\n                                                         ≥ (2t)n (ω0 , ϕ0 )n+1 + (ω1 , ϕ1 )n+1 ,\n                                                                                              \u0001\n\nwhere the first inequality holds by Proposition 7.3, the second one by concavity of ψ 7→\n(ω̃, ψ)n+1 , and the third one by Lemma  P 7.9.\n   Assume now r ≥ 2, and set ω00 := i>0 ωi , ϕ00 := i>0 ϕi . Since t−1 ω0 ≤ ω00 ≤ rtω0 , the\n                                                          P\nfirst part of the proof yields\n                       !n+1\n        X         X\n                            = (ω0 + ω00 , ϕ0 + ϕ00 )n+1 ≥ (2rt)n (ω0 , ϕ0 )n+1 + (ω00 , ϕ00 )n+1\n                                                                                                 \u0001\n             ωi ,   ϕi\n        i       i\nBy induction, we have on the other hand\n                                                               X\n                           (ω00 , ϕ00 )n+1 ≥ Cr−1,n t(r−1)n     (ωi , ϕi )n+1 ,\n                                                               i>0\n\nThe result follows, since (ω0 , ϕ0 )n+1 ≤ 0 and\n                                Cr,n trn = (2rt)n Cr−1,n ≥ (2rt)n .\n                                                                                                      \u0003\nCorollary 7.11. With the notation of Lemma 7.10 we have\n                                                           2\n                          (ω0 , ϕ0 ) · . . . · (ωn , ϕn ) & tn min (ωi , ϕi )n+1                  (7.12)\n                                                               0≤i≤n\n\nfor all nonpositive ϕi ∈ PSH(ωi ).\nProof. Expanding out (ω0 + · · · + ωn , ϕ0 + · · · + ϕn )n+1 yields\n             (ω0 + · · · + ωn , ϕ0 + · · · + ϕn )n+1 ≤ (n + 1)!(ω0 , ϕ0 ) · . . . · (ωn , ϕn ),\nand we conclude by Lemma 7.10 with r = n.                                                             \u0003\nProof of Theorem 7.8. Properties (i)–(iii) follow from Proposition 7.7, while (iv), (v) and (vi),\nrespectively, follow from Lemmas 7.9, 7.10 and Corollary 7.11. Finally, (vii) follows from (7.10).\n                                                                                              \u0003",
  "e3aed860597e20cf9bc441ca10b30bf8b8f043fc2d24ca18ed590e1b63e59767": "  It will be convenient to extend the energy pairing to a multilinear map. Recall that any\nω-psh function is finite-valued on X lin , see Corollary 4.17. We now introduce\nDefinition 7.12. We define a function of finite energy as a function ϕ : X lin → R of the\nform ϕ = ϕ+ − ϕ− with ϕ± ∈ E 1 (ω) for some ω ∈ Amp(X).\n   By Theorem 7.8, ω∈Amp(X) E 1 (ω) forms a convex cone in the R-linear space of all func-\n                      S\n\ntions ϕ : X lin → R, and the set\n                                           E~1 = E~1 (X)\nof functions of finite energy thus forms an R-vector space, which contains PL(X)R , by (3.2).\nNote further that E~1 is generated by E 1 (ω) for any given ω ∈ Amp(X), by Theorem 7.8 (iv),\n(v).\n\f80                           SÉBASTIEN BOUCKSOM AND MATTIAS JONSSON\n\n\nLemma 7.13. For each ω ∈ Amp(X), we have E 1 (ω) = E~1 ∩ PSH(ω).\n   In other words, E 1 (ω) consists precisely of functions that are ω-psh and of finite energy,\nso that the chosen terminology is consistent.\nProof. The inclusion E 1 (ω) ⊂ E~1 ∩ PSH(ω) is clear. Conversely, pick ϕ ∈ E~1 ∩ PSH(ω),\nand write ϕ = ϕ+ − ϕ− with ϕ± ∈ E 1 (ω 0 ) for some ω 0 ∈ Amp(X). After adding constants,\n                                                     n+1\nwe may assume ϕ, ϕ± ≤ 0. Then ((ω, ϕ) + (ω 0 , ϕ− ))       ≤ (ω, ϕ)n+1 , by expanding out the\nleft-hand side. By Theorem 7.8 (iv), we infer\n                                                              \u0001n+1\n                −∞ < (ω + ω 0 , ϕ+ )n+1 = (ω, ϕ) + (ω 0 , ϕ− )     ≤ (ω, ϕ)n+1 .\nThus ϕ ∈ E 1 (ω), which proves the result.                                                                    \u0003\nTheorem 7.14. There exists a unique multilinear symmetric pairing\n       \u0010              \u0011n+1\n         N1 (X) × E~1      3 ((θ0 , ϕ0 ), . . . , (θn , ϕn )) 7→ (θ0 , ϕ0 ) · . . . · (θn , ϕn ) ∈ R\n\nthat is compatible with the one defined in Theorem 7.1 for tuples (θi , ϕi ) ∈ N1 (X) × E~1 such\nthat θi ∈ Amp(X) and ϕi ∈ E 1 (θi ) = E~1 ∩ PSH(θi ). Furthermore:\n     (i) this pairing is compatible with the one defined in §3.2 for tuples in N1 (X) × PL(X)R ;\n    (ii) (7.3), (7.4) and (7.5) remain valid on N1 (X) × E~1 ;\n   (iii) for any ω ∈ Amp(X) and θ0 , . . . , θn ∈ N1 (X), the map\n                                 (ϕ0 , . . . , ϕn ) 7→ (θ0 , ϕ0 ) · . . . · (θn , ϕn )\n          is continuous along decreasing nets in E 1 (ω).\nProof. Consider the vector space V := N1 (X) × E~1 . By Theorem 7.8 (v),\n                                       [\n                               C :=          {ω} × E 1 (ω).\n                                               ω∈Amp(X)\n\nis a convex cone in V , and the energy pairing is an R>0 -multilinear pairing on C, by Propo-\nsition 7.2. Since Amp(X) spans N1 (X), it is straightforward to see, using Theorem 7.8 (iv),\nthat C spans V . It is now a simple general fact that the pairing on C uniquely extends to\nan R-multilinear pairing on V .\n   The first compatibility assertion follows from Lemma 7.13. The pairing on C restricts to\nthe one from §3.2 on the subcone\n                                   [\n                          C 0 :=          {ω} × (PL(X)R ∩ PSH(ω)),\n                                     ω∈Amp(X)\n\nwhich spans V 0 := N1 (X) × PL(X)R ; the extended pairing on V thus coincides with the\ngiven one on V 0 , which proves (i). Next, (ii) is immediate by multilinearity. Finally (iii)\nholds when θi ≥ ω, by Theorem 7.1; the general case follows, again by multilinearity.                         \u0003\n     By multilinearity, (7.3), (7.4) and (7.5) remain valid on N1 (X) × E~1 . We also note:\nLemma 7.15. If θ0 , . . . , θn ∈ Nef(X), then (θ0 , ϕ0 ) · . . . · (θn , ϕn ) is an increasing function\nof ϕi ∈ PSH(θi ) ∩ E~1 .\nProof. It suffices to write (θ0 , ϕ0 ) · . . . · (θn , ϕn ) = limε→0 (θ0 + εθ, ϕ0 ) · . . . · (θn + εθ, ϕn ) with\nθ ∈ Amp(X).                                                                                                    \u0003\n\f              GLOBAL PLURIPOTENTIAL THEORY OVER A TRIVIALLY VALUED FIELD                              81\n\nRemark 7.16. Mimicking the complex analytic case, one can define E 1 (θ) for any θ ∈\nNef(X) as the set of ϕ ∈ PSH(θ) such that inf j (θ, ϕj )n+1 > −∞ with ϕj := max{ϕ, −j} ∈\nE ∞ (θ). The proof of Lemma 7.13 still yields E~1 ∩ PSH(θ) ⊂ E 1 (θ), but the inclusion is strict\nin general when θ is not ample (compare [DiN16]).\n7.3. Mixed Monge–Ampère measures. Recall that a Radon measure µ on the compact\nspace X an is a regular (positive) Borel measure on X an . By the Riesz representation theorem,\nRadon measures are in 1–1 correspondence with positive linear forms on C0 (X), see for\ninstance [Fol99, §7.1–2]. Any usc function f : X an → R ∪ {−∞} satisfies\n                                   f = inf g ∈ C0 (X), g ≥ f\n                                          \b\n\npointwise, and\n                     ˆ                   \u001aˆ                                \u001b\n                                                            0\n                          f µ = inf            g µ | g ∈ C (X), g ≥ f          ∈ R ∪ {−∞}.        (7.13)\n\n   We will sometimes need to rely on the following monotone convergence theorem for (pos-\nsibly uncountable) nets of usc functions, a simple consequence of (7.13) and Dini’s lemma\n(see for instance [Fol99, Proposition 7.12]).\nLemma 7.17. If µ is a Radon measure on X an and (fj )j a decreasing\n                                                             ´      ´net of usc functions\n    an\non X , converging pointwise to a (usc) function f , then limj fj µ = f µ.\n  More generally, continuous linear forms in C0 (X)∨ correspond to signed Radon mea-\nsures on X an . Any such measure can be written as a difference of Radon measures, and\nLemma 7.17 thus applies as well when µ is a signed measure.\n  With these preliminaries in hand, we now generalize the construction of mixed Monge–\nAmpère measures, introduced in §3.2 in the PL case.\nTheorem 7.18. For each n-tuple (θi , ϕi ) ∈ N1 (X) × E~1 , i = 1, . . . , n, there exists a unique\nsigned measure\n                                                      ^\n             (θ1 + ddc ϕ1 ) ∧ · · · ∧ (θn + ddc ϕn ) = (θi + ddc ϕi ) ∈ C0 (X)∨              (7.14)\n                                                                    i\nsuch that             ˆ             ^\n                                ϕ    (θi + ddc ϕi ) = (0, ϕ) · (θ1 , ϕ1 ) · . . . · (θn , ϕn )    (7.15)\n                         X an        i\nfor all ϕ ∈ PL(X)R . If further θi ∈ Nef(X) and ϕi ∈ PSH(θi ) for i = 1, . . . , n, then (7.14)\nis a positive measure.\n  While the notation mimics the one for mixed Monge–Ampère measures in the complex\nanalytic case, we will not define the individual factors θi + ddc ϕi . At least if the ϕi are\ncontinuous, this could, however, be done using the approach in [CLD12] (cf. Remark 7.23\nbelow).\nProof. By density of PL(X) in C0 (X) (see Theorem 2.2), the prescription (7.15) uniquely\ndetermines the measure (7.14). To show existence, we may assume, by multilinearity, that\nθi ∈ Nef(X) and ϕi ∈ E~1 ∩ PSH(θi ) for i = 1, . . . , n. Since any ϕ ∈ PL(X)R can be written\nas a difference of functions in PLR ∩ PSH(ω) for some ω ∈ Amp(X) (see (3.2)), Lemma 7.15\nshows that ϕ 7→ (0, ϕ) · (θ1 , ϕ1 ) · . . . · (θn , ϕn ) is a positive linear form on PL(X)R . By density\nof PL(X)R in C0 (X), it thus uniquely extends to a positive linear form on C0 (X), and we\nare done.                                                                                              \u0003\n\f82                           SÉBASTIEN BOUCKSOM AND MATTIAS JONSSON\n\nProposition 7.19. Mixed Monge–Ampère measures satisfy the following properties:\n   (i) the signed measure i (θi + ddc ϕi ) is a symmetric and multilinear function of the\n                              V\n\n       n-tuple (θi , ϕi ) ∈ N1 (X) × E~1 , of total mass\n                             ˆ     ^\n                                     (θi + ddc ϕi ) = (θ1 · . . . · θn )X ;\n                                       X an i\n\n     (ii) assume (θi , ϕi ) ∈ N1 (X) × PLR , and pick an integrally closed test configuration X\n          dominating Xtriv and Di ∈ VCar(X )R such that ϕi = ϕDi ; then\n                                   ^                   X\n                                      (θi + ddc ϕi ) =   cE δvE ,\n                                           i                          E\n\n          where E ranges over the irreducible components of X0 and\n                         cE := ordE (X0 )(θ1,X + D1 )|E · . . . · (θn,X + Dn )|E ;\n     (iii) for all (θi , ϕi ) ∈ N1 (X) × E~1 and t ∈ R>0 we have\n                                 ^                           ^\n                                    (θi + ddc (t · ϕi )) = t? (θi + ddc ϕi ),                    (7.16)\n                                   i                                   i\n                        ^                              X        ^\n                             (θi + ddc ϕi ) =                          θi |Xα + ddc ϕi |Xαan ,\n                                                                                            \u0001\n                                                                                                 (7.17)\n                         i                          dim Xα =n i\n                              ^                              ^\n                                       (θi + ddc ϕi ) = ν?          (ν ? θi + ddc ν ? ϕi ) ,     (7.18)\n                               i                                i\n          with ν : X ν → X the normalization;\n     (iv) for any ω ∈ Amp(X), the map E 1 (ω)n 3 (ϕ1 , . . . , ϕn ) 7→ i (θi +ddc ϕi ) is continuous\n                                                                      V\n          along decreasing nets;\n      (v) for all (θi , ϕi ) ∈ N1 (X) × E~1 and ϕ ∈ E~1 , ϕ is integrable against i (θi + ddc ϕi ),\n                                                                                   V\n          and (7.15) holds.\n  When ϕi = 0 for some i, we drop the term ddc ϕi from the notation. As a special case of\nProposition 7.19 (ii), we then have\n                                          X\n                        θ1 ∧ · · · ∧ θn =   (θ1 · . . . · θn )Xα δvtriv,α .        (7.19)\n                                                    dim Xα =n\n\nProof of Proposition 7.19. Points (i) and (iii) follow from Proposition 7.2, while (ii) is a\nreformulation of (3.5). By density of PL(X) in C0 (X), (iv) is equivalent to the fact that,\nfor each ϕ ∈ PL(X),\n                                 ˆ  ^\n            (ϕ1 , . . . , ϕn ) 7→ ϕ   (θi + ddc ϕi ) = (0, ϕ) · (θ1 , ϕ1 ) · . . . · (θn , ϕn )\n                                                i\n\nis continuous along decreasing nets in E 1 (ω)n+1 . Now ϕ can be written as a difference of\nfunctions in PL ∩ PSH(ω 0 ) for some ω 0 ∈ Amp(X), and the desired continuity is thus a\nconsequence of Theorem 7.14. To prove (v), we may assume θi ∈ Amp(X) and ϕi ∈ E 1 (θi ),\nby multilinearity. Any ϕ ∈ E 1 (ω) with ω ∈ Amp(X) can be written as the pointwise limit\nof a decreasing net in PL ∩ PSH(ω), and (7.15) thus holds for ϕ, by monotone convergence\nand the continuity of the energy pairing along decreasing limits.                        \u0003\n\f              GLOBAL PLURIPOTENTIAL THEORY OVER A TRIVIALLY VALUED FIELD                                 83\n\nExample 7.20. Assume X is a smooth curve and pick ω ∈ Amp(X). By Example 4.13,\nany ϕ ∈ PSH(ω) determines a positive Radon measure (deg ω)δvtriv + ∆ϕ, with\n              X \u0014d                                                     d2\n                                                                                     \u0015\n                                             d\n        ∆ϕ =              ϕ(t ordp )δvtriv −       ϕ(t ordp )δvp,triv + 2 ϕ(t ordp )\n                    dt 0+                    dt +∞                     dt\n                 p∈X(k)\n\nthe tree Laplacian (see [FJ04, §7]). As we saw in Example 3.19, we have ω + ddc ϕ =\n(deg ω)δvtriv + ∆ϕ for any ϕ ∈ PLR ∩ PSH(ω), and this remains true for any ϕ ∈ E 1 (ω),\nby monotone approximation. For such functions, ω + ddc ϕ further puts no mass on the\nendpoints vp,triv , which means that the convex function t 7→ ϕ(t ordp ) has sublinear growth\n(see respectively Corollary 7.49 and Theorem 11.11).\nProposition 7.21. Pick ωi ∈ Amp(X) and ϕi ∈ E 1 (ωi ), i = 1, . . . , n, and choose also\nω0 ∈ Amp(X) and ϕ0 ∈ PSH(ω0 ). Then:\n    (i) ϕ0 is integrable with respect to µ := i (ωi + ddc ϕi ) iff (ω0 , ϕ0 ) · . . . · (ωn , ϕn ) > −∞,\n                                             V\n        and this holds as soon as ϕi is bounded for i = 1, . . . , n;\n   (ii) assume ϕ0 ∈ L1 (µ). Pick for i = 0, . . . ,Vn a decreasing net (ϕij )j in PSH(ωi ) that\n        converges pointwise to ϕi , and set µj := i (ωi + ddc ϕij ). Then ϕ0j ∈ L1 (µj ) for all\n        j, and ϕ0j µj → ϕ0 µ weakly in C0 (X)∨ .\nLemma 7.22. Let K be a compact topological space with a weakly convergent net of positive\nRadon measures µj → µ. Assume also given an increasing net of lsc             ´ fj : K →\n                                                                     ´ functions\nR ∪ {+∞} such that fj ∈ L1 (µj ) for all j, f := limj fj ∈ L1 (µ) and fj µj → f µ. Then\nfj µj → f µ weakly in C0 (K)∨ .\nProof. Being lsc, each fj is bounded below, and the increasing net (fj ) is thus ultimately\nbounded below. Since ´µj → µ, we may therefore assume, after adding a constant, that\nfj ≥ 0 for all j. Since fj µj converges, the positive measures σj := fj µj stay in a fixed\nweakly compact subset of C0 (X)∨ , and it suffices\n                                              ´ to show\n                                                      ´    that any\n                                                                 ´ limit ´point σ∞ of σj\nmust coincide with σ := f µ. By assumption, σj → σ, hence σ∞ = σ, and it will\nthus be enough to show that σ∞ ≥ σ. To this end, pick 0 ≤ g ∈ C0 (K). For all j ≥ k we\nhave fj ≥ fk , and hence       ˆ       ˆ           ˆ\n                                      g σj =    gfj µj ≥      gfk µj .\n                                                                                    ´            ´\nBy lower semicontinuity of gfk and the weak convergence µj → µ, we infer                g σ∞ ≥       gfk µ.\nUsing monotone convergence, this now yields in turn,\n                                ˆ         ˆ         ˆ\n                                   g σ∞ ≥ gf µ = g σ,\n\nwhich concludes the proof.                                                                               \u0003\nProof of Proposition 7.21. Set c := (ω0 , 0) · (ω1 , ϕ1 ) · . . . · (ωn , ϕn ) ∈ R, and pick a decreasing\nnet (ϕ0j ) in PL ∩ PSH(ω0 ) such that ϕ0j → ϕ0 pointwise. By construction of µ, we have for\neach j                         ˆ\n                                  ϕ0j µ = (ω0 , ϕ0j ) · (ω1 , ϕ1 ) · . . . · (ωn , ϕn ) − c.\n                         ´           ´\nBy Lemma 7.17, ϕ0j µ → ϕ0 µ. By Theorem 7.1, we have on the other hand (ω0 , ϕ0j ) ·\n(ω1 , ϕ1 ) · . . . · (ωn , ϕn ) → (ω0 , ϕ0 ) · (ω1 , ϕ1 ) · . . . · (ωn , ϕn ). Thus\n                                ˆ\n                                   ϕ0 µ = (ω0 , ϕ0 ) · (ω1 , ϕ1 ) · . . . · (ωn , ϕn ) − c,\n\f84                            SÉBASTIEN BOUCKSOM AND MATTIAS JONSSON\n\nand (i) follows.\n  We turn to (ii). By Proposition 7.19 (iv), we have µj → µ. Further,\n            ˆ\n              ϕ0j µj = (ω0 , 0) · (ω1 , ϕ1j ) · . . . · (ωn , ϕnj ) − (ω0 , ϕ0j ) · . . . · (ωn , ϕnj )\n\nis finite for each j, and converges to\n                ˆ\n                  ϕ0 µ = (θ0 , 0) · (ω1 , ϕ1 ) · . . . · (ωn , ϕn ) − (ω0 , ϕ0 ) · . . . · (ωn , ϕn ).\n\nThe result is now a consequence of Lemma 7.22.                                                                \u0003\nRemark 7.23. For continuous ω-psh functions, mixed Monge–Ampère measures can also be\ndefined using the general theory developed by Chambert-Loir and Ducros [CLD12]. By base\nchange invariance of their theory, it follows from Proposition 7.19 (ii) and [BE20, Theorem\n8.18] that the present approach is compatible with [CLD12] for continuous ω-psh functions.\n7.4. The Monge–Ampère operator and energy functionals. In this section we fix\nω ∈ Amp(X). We denote by V := (ω n ) its volume, and write E 1 := E 1 (ω) and E := Eω .\nDefinition 7.24. The Monge–Ampère operator takes ϕ ∈ E 1 to the Radon probability\nmeasure\n                      MA(ϕ) = MAω (ϕ) := V −1 (ω + ddc ϕ)n\non X an .",
  "0d8d872a3323e4100bae27cb6e8b676a500abdf1989b7c1e024af35849a97912": "                                                                          if dim Xα = n\n     1Xα µ =\n                 0                                                        otherwise\nProof. By Proposition 7.19 (v), µ integrates all functions ψ ∈ E 1 (ω), and (i) thus follows\nfrom Corollary 7.48.\n   By Lemma 4.36, Xαan ∩ Xαan0 is pluripolar for all α 6= α0 , being a nowhere dense Zariski\nclosed subset. By (i), we thus have µ(Xαan ∩ Xαan0 ) = 0, and (ii) is now a consequence of\nProposition 7.19 (ii).                                                                    \u0003\n\n              8. Differentiability of the extended energy functional\n   As before, X is a projective variety of dimension n, with irreducible components Xα . Fix\nan ample class ω ∈ Amp(X). Above we considered the Monge–Ampère energy functional\nE : PSH(ω) → R ∪ {−∞}, defined the set E 1 = {E > −∞}, and associated a Monge-Ampère\nmeasure MA(ϕ) to each ϕ ∈ E 1 . Formally, MA is the differential of E, but E 1 is not a real\nvector space. In this section, we extend the Monge–Ampère energy to various spaces of\nfunctions on X an , and prove quite precise differentiability results for these extensions.\n8.1. Extending the Monge–Ampère energy. Unless stated otherwise, ω ∈ Amp(X) is\nan ample class, and we set PSH := PSH(ω), E 1 := E 1 (ω) etc. The increasing functional\n                                   E : PSH → R ∪ {−∞}\nadmits a natural extension to arbitrary functions ϕ : X an → R ∪ {±∞} by setting\n                       E(ϕ) = Eω (ϕ) := sup {E(ψ) | ψ ∈ PSH, ψ ≤ ϕ} ,                   (8.1)\nwith the convention sup ∅ = −∞. For ψ ∈ PSH(ω), ψ ≤ ϕ ⇔ ψ ≤ P(ϕ), and hence\n                                      E(ϕ) = E (P(ϕ)) .                                 (8.2)\n     We will mainly be concerned with the case when ϕ is bounded, or even continuous.\nProposition 8.1. The extended functional E : C0 (X) → R satisfies the following properties:\n\f             GLOBAL PLURIPOTENTIAL THEORY OVER A TRIVIALLY VALUED FIELD                            95\n\n    (i) it is increasing, concave, and 1-Lipschitz continuous;\n   (ii) for each ϕ ∈ C0 (X), c ∈ R and t ∈ R>0 we have\n            E(ϕ + c) = E(ϕ) + c,         E(t · ϕ) = t E(ϕ),   and    Etω (tϕ) = t Eω (ϕ);\n   (iii) for any ϕ ∈ C0 (X), ω 7→ Eω (ϕ) is continuous on Amp(X);\n   (iv) for each ϕ ∈ C0 (X) we have\n                                            X\n                                   E(ϕ) =      cα E(ϕ|Xα )                                      (8.3)\n                                                  α\n\n        with cα := (ω n )Xα /(ω n )X .\nProof. Properties (i) and (ii) are straightforward consequences of Proposition 7.7.\n  To prove (iii), we may replace ϕ with ϕ − inf ϕ and assume ϕ ≥ 0, by (ii). Then\n                           E(ϕ) = sup {E(ψ) | ψ ∈ PSH, 0 ≤ ψ ≤ ϕ} .                             (8.4)\nNow pick a convergent sequence ωi → ω in Amp(X). We can then find a sequence (ti ) in\nR>0 such that t−1\n               i ω ≤ ωi ≤ ti ω and ti → 1. By Proposition 7.3, any\n\n                                     ψ ∈ PSH(ωi ) ⊂ PSH(ti ω)\nsuch that 0 ≤ ψ ≤ ϕ satisfies (ωi , ψ)n+1 ≤ (ti ω, ψ)n+1 , and (8.4) thus yields\n                                Eωi (ϕ) ≤ ci Eti ω (ϕ) = ci ti Eω (t−1\n                                                                    i ϕ)\n\nwith ci := tni (ω n )/(ωin ) → 1, where the right-hand equality follows from (ii). Similarly,\n                                t−1                          0\n                                 i Eω (ti ϕ) = Et−1 ω (ϕ) ≤ ci Eωi (ϕ)\n                                                   i\n\nwith c0i := tni (ωin )/(ω n ) → 1. Since t−1\n                                          i ϕ → ϕ and ti ϕ → ϕ uniformly, we conclude, as\ndesired, Eωi (ϕ) → Eω (ϕ) by continuity of Eω , proving (iii). `\n   The proof of (iv) is slightly more involved. Introduce Y := α Xα , with its canonical\nbirational morphism π : Y → X. The data of a family of functions ψα ∈ PSH(ω|Xα ) with\nψα ≤ ϕ|Xαan is equivalent to that of ψ ∈ PSH(π ? ω) with ψ ≤ π ? ϕ, and (7.10) implies that\nthe right-hand side of (8.3) coincides with Eπ? ω (π ? ϕ). Since π ? PSH(ω) ⊂ PSH(π ? ω), (7.10)\nfurther yields Eω (ϕ) ≤ Eπ? ω (π ? ϕ).\n   Conversely, pick ψ ∈ PSH(π ? ω) such that ψ ≤ π ? ϕ. After replacing ψ with max{ψ, c}\nfor a constant c ≤ ϕ, we may assume that ψ is bounded. Choose ωX ∈ Amp(X) and\nϕX ∈ PSH(ωX ) as in Theorem 4.32. Replacing ωX and ϕX with small enough multiples,\nwe may assume ωX ≤ ω, and hence ϕX ∈ PSH(ω). Since ϕ and ψ are both bounded, we\nmay further arrange, after adding a constant to ϕX , that ϕX ≤ ϕ and π ? ϕX ≤ ψ. For each\nm ∈ Z>0 , we get ϕm ∈ PSH(ω) such that\n                                   π ? ϕm = (1 − m\n                                                 1      1 ?\n                                                   )ψ + m π ϕX .\nSince ϕX ≤ ϕ, we have π ? ϕm ≤ π ? ϕ, and hence ϕm ≤ ϕ, see Theorem 4.22. On the\nother hand, since π ? ϕX ≤ ψ, Theorem 4.22 shows that (ϕm ) is an increasing sequence\nin PSH(ω), such that π ? ϕm → ψ pointwise on Y div . Now set c := min{inf ϕ, inf ψ} and\nϕ0m := max{ϕm , c}. Then (ϕ0m ) is also an increasing sequence, this time in E ∞ (ω) ⊂ E 1 (ω),\nwith π ? ϕ0m → ψ pointwise on Y div . Further, ϕ0m ≤ ϕ, and hence\n                         X\n                            cα Eω|Xα (ϕ0m |Xαan ) = Eω (ϕ0m ) ≤ Eω (ϕ),\n                            α\n\f96                         SÉBASTIEN BOUCKSOM AND MATTIAS JONSSON\n\nby (7.10). Since ϕ0m |Xαan → ψ|Xαan pointwise on Xαdiv , Theorem 7.38 yields Eω|Xα (ϕ0m |Xαan ) →\nEω|Xα (ψ|Xαan ), and hence\n                                       X\n                           Eπ? ω (ψ) =    cα Eω|Xα (ψ|Xαan ) ≤ Eω (ϕ).\n                                        α\nTaking the supremum over all ψ, we conclude, as desired, Eπ? ω (π ? ϕ) ≤ Eω (ϕ).               \u0003\n8.2. Further extensions. Using the extension of the Monge–Ampère energy E to continu-\nous functions, we now go further and extend it to (upper or lower) semicontinuous functions.\nDefinition 8.2. For any ϕ : X an → R ∪ {±∞} we set\n                       E↑ (ϕ) := sup E(ψ) | ψ ∈ C0 (X), ψ ≤ ϕ\n                                    \b\n                                                                                           (8.5)\nand\n                            E↓ (ϕ) := inf E(ψ) | ψ ∈ C0 (X), ψ ≥ ϕ .\n                                         \b\n                                                                                           (8.6)\n   While E↑ and E↓ are defined for arbitrary functions, they are mainly of interest when\nrestricted to lsc and usc functions, respectively.\nProposition 8.3. The functionals E↑ and E↓ satisfy the following properties:\n   (i) they are increasing, concave, and satisfy the algebraic properties of Proposition 8.1 (ii);\n  (ii) for any ϕ : X an → R ∪ {±∞},\n                                    E↑ (ϕ) ≤ E(ϕ) ≤ E↓ (ϕ),\n           and E↑ (ϕ) > −∞ (resp. E↓ (ϕ) < +∞) iff ϕ is bounded below (resp. bounded above);\n     (iii) we have\n                      E↑ (ϕ) = E(Q(ϕ)) = sup {E(ψ) | ρ ∈ CPSH, ψ ≤ ϕ} ;\n         we further have\n                                  E↑ (ϕ) = E(ϕ? ) = E(P(ϕ? ))\n          if ϕ is bounded below;\n     (iv) if ϕ is bounded above, then\n                                        E↓ (ϕ) = E↓ (ϕ? )\n         we further have\n                                   E↓ (ϕ) = E (ϕ? ) = E (P(ϕ? ))                           (8.7)\n                  0\n         if ϕ ∈ C (X), or ϕ ∈ PSH(ω), and for any ϕ bounded above if the envelope property\n         holds for ω;\n     (v) E↑ (resp. E↓ ) is continuous along increasing (resp. decreasing) nets of bounded-below,\n         lsc (resp. bounded above, usc) functions.\nProof. (i) and (ii) are obvious. We prove (iii). For any ψ ∈ C0 (X), we have P(ψ) = Q(ψ)\nby Lemma 5.19, and (8.2) yields\n                E(ψ) = E(P(ψ)) = E(Q(ψ)) = sup {E(ρ) | ρ ∈ CPSH, ρ ≤ ψ} .\nThis implies in turn\n  E↑ (ϕ) = sup E(ψ) | ψ ∈ C0 (X), ψ ≤ ϕ = sup {E(ρ) | ρ ∈ CPSH, ρ ≤ ϕ} = E(Q(ϕ)),\n                \b\n\nby monotonicity of E. If ϕ is bounded below, then Q(ϕ) = P(ϕ? ) by Lemma 5.19, and hence\nE(Q(ϕ)) = E(P(ϕ? )) = E(ϕ? ), which proves (iii).\n\f            GLOBAL PLURIPOTENTIAL THEORY OVER A TRIVIALLY VALUED FIELD                               97\n\n  Next we show that E↑ is continuous along increasing nets of bounded-below, lsc functions.\nLet thus (ϕi ) be an increasing net of such functions, converging to the lsc function ϕ =\nsupi ϕi . On the one hand, ϕ ≥ ϕi implies\n                           E↑ (ϕ) ≥ S := sup E↑ (ϕi ) = lim E↑ (ϕi ).\n                                             i                   i\n\nOn the other hand, for each ε > 0 we can find ψ ∈ C0 (X) such that ψ ≤ ϕ and E(ψ) ≥\nE↑ (ϕ)S− ε. Setting, for each i, Vi := {ψ < ϕi + ε} defines an increasing family of open sets\nwith i Vi = X an . By compactness, we get Vi = X an for all i large enough, i.e. ψ ≤ ϕi + ε\non X an , and hence E(ψ) ≤ E↑ (ϕi ) + ε ≤ S + ε. We thus have E↑ (ϕ) ≤ S + 2ε for all ε > 0,\nand we get, as desired, E↑ (ϕ) = S.\n   The proof that E↓ is continuous along decreasing nets of bounded-above usc functions is\nentirely similar; hence (v).\n   If ϕ ∈ C0 (X) then (8.7) follows from (8.2). If ϕ ∈ PSH(ω), write it as the limit of a\ndecreasing net in CPSH(ω). Then E(ϕi ) → E↓ (ϕ), by (v), and E(ϕi ) → E(ϕ), by continuity\nof E along decreasing nets in PSH(ω). This proves (8.7) in that case.\n   Now consider the general case, assuming the envelope property. Write ϕ? as the decreasing\nlimit of a net (ϕi ) in C0 (X). For each i we have E↓ (ϕi ) = E(P(ϕi )). On the one hand,\nE↓ (ϕi ) → E↓ (ϕ), by (v). On the other hand, Corollary 5.18 implies that P(ϕi ) decreases\nto P(ϕ? ) in PSH(ω), and hence E(P(ϕi )) → E(P(ϕ? )) = E(ϕ? ), by continuity of E along\ndecreasing nets in PSH(ω) and (8.2). This concludes the proof of (iv).                     \u0003\nCorollary 8.4. If ϕ : X an → R ∪ {−∞} is usc, then\n                                        X\n                               E↓ (ϕ) =   cα E↓ (ϕ|Xαan ).\n                                                 α\nIf ϕ : X an → R ∪ {+∞} is lsc, then\n                                             X\n                                 E↑ (ϕ) =            cα E↑ (ϕ|Xαan ).\n                                                 α\n\nProof. Assume ϕ : X an → R∪{−∞} is usc, and pickPa decreasing net (ϕi ) in C0 (X) such that\nϕi & ϕ pointwise. For each i, (8.3) yields E(ϕi ) =           α cα E(ϕi |Xα\n                                                                          an ). By Proposition 8.3 (v),\n\nwe have\n          E(ϕi ) = E↓ (ϕi ) & E↓ (ϕ)   and       E(ϕi |Xαan ) = E↓ (ϕi |Xαan ) & E↓ (ϕ|Xαan ),\nand the first point follows. In the lsc case, the proof is similar, using an increasing net\ninstead.                                                                                 \u0003\n8.3. Uniform differentiability of the energy. Building on [BGM20] we prove the fol-\nlowing uniform differentiability result, which is crucial for what follows.\nTheorem 8.5. Pick f ∈ PL(X)R . For any ϕ ∈ E 1 , we then have\n                                          ˆ\n                      ↓\n                    E (ϕ + εf ) = E(ϕ) + ε f MA(ϕ) + O(ε2 )\n\nas ε → 0, where the implicit constant in the O is uniform with respect to ϕ.\n   If ϕ ∈ CPSH(ω) (and for any ϕ ∈ E 1 , if the envelope property holds), the left-hand side\nsatisfies\n                       E↓ (ϕ + εf ) = E(ϕ + εf ) = E(P(ϕ + εf )),\nby (8.7).\n\f98                      SÉBASTIEN BOUCKSOM AND MATTIAS JONSSON\n\nCorollary 8.6. For any ϕ ∈ E 1 and f ∈ C0 (X) we have\n                                               ˆ\n                           d       ↓\n                                 E (ϕ + tf ) = f MA(ϕ).\n                          dt t=0\n\n  Again, one can replace E↓ with E = E ◦ P if ϕ ∈ CPSH(ω), or if the envelope property\nholds.\n  For any ω ∈ Amp(X) we set Vω := (ω n ).\nLemma 8.7. Pick ω, ω 0 ∈ Amp(X), ψ1 , ψ2 ∈ PLR ∩ PSH(ω 0 ), and set f := ψ1 − ψ2 . For\nany ϕ ∈ CPSH(ω) we then have\n                               ˆ\n                            −1\n                                                           \u0001n\n                                 f ω + ω 0 + ddc (ϕ + ψ1 )    ≤ Vω−1 Vω+ω0 − 1 sup |f |.\n                                                                              \u0001\n    Eω (ϕ + f ) − Eω (ϕ) − Vω\n\nProof. We may assume ω = c1 (L), ω 0 = c1 (L0 ) for ample line bundles L, L0 on X, Indeed, by\nhomogeneity, we then obtain the case when L, L0 are ample Q-line bundles, and the general\ncase by a simple perturbation argument based on Proposition 8.1 (iii).\n   Consider first any continuous function ρ ∈ C0 (X). For each m ∈ N, ρ defines a sup-norm\nk · kmρ on H0 (X, mL), defined by\n                                   kskmρ = sup |s|e−mρ .\n                                             X an\n\nThis norm induces a norm det k · kmρ on the determinant line det H0 (X, mL). Comparing\nwith the trivial norm, we can and will think of det k · kmρ as a number. It now follows\nfrom [CMac15] (see [BE20, Theorem 9.5]) that the volume\n                                                1\n                        volL (ρ) := − lim             log det k · kmρ\n                                      m→∞ mh0 (mL)\n\nexists in R. We claim that volL (ρ) = EL (ρ). Using [BE20, (9.7)] and (8.3), it is enough\nto prove this when X is irreducible. When ρ ∈ CPSH(L), the equality holds by [BE20,\nTheorem A] (or [BoJ18b, Lemma 4.5]). In the general case, this yields\n                  EL (ρ) = sup {EL (ψ) | ψ ∈ CPSH(L), ψ ≤ ρ} ≤ volL (ρ),\nby monotonicity of volL . On the other hand, Theorem 5.1.1 of [Reb21] (which is valid for\narbitrary non-Archimedean fields; see also [BoJ18b, Theorem 4.13] for the trivially valued\ncase) shows that\n                                                           |s|\n                           ρm := m−1 log       sup\n                                             0\n                                          s∈H (X,mL)\\{0} ksk mρ\n\nsatisfies ρm ∈ PLR ∩ PSH(ω), ρm ≤ ρ and EL (ρm ) → volL (ρ); the claim follows.\n   In particular, EL (ϕ + f ) = volL (ϕ + f ) and EL (ϕ) = volL (ϕ). The desired estimate is\nnow a consequence of Lemma 8.8 below, itself a reformulation of [BGM20, Lemma 3.2]. \u0003\nLemma 8.8. Let L and L0 be ample line bundles on X, and set ω = c1 (L), ω 0 = c1 (L0 ).\nConsider functions ϕ ∈ CPSH(ω), and ψ1 , ψ2 ∈ CPSH(ω 0 ). Set f := ψ1 − ψ2 ∈ C0 and\nC := Vω+ω0 − Vω > 0. Then\n               ˆ\n    C inf\n        an\n           f≤      f (ω + ω 0 + ddc (ϕ + ψ1 ))n − Vω (volL (ϕ + f ) − volL (ϕ)) ≤ C sup f.\n       X        X an                                                              X an\n\f             GLOBAL PLURIPOTENTIAL THEORY OVER A TRIVIALLY VALUED FIELD                      99\n\nProof. This is a reformulation in our context of [BGM20, Lemma 3.2] in the special case\nof a trivially valued field k. The fact that k is trivially valued means that we can view ϕ,\nψ1 , ψ2 as continuous psh metrics on the Berkovich analytifications of the line bundles L and\nL0 , respectively. The difference volL (ϕ + f ) − volL (ϕ) can be viewed as the relative volume\nof the metrics ϕ + f and ϕ on L. Note that our current normalization of the volume differs\nfrom the one in loc.cit. by a factor Vω = (Ln ).                                              \u0003\nProof of Theorem 8.5. We argue along the lines of the proof of [BGM20, Theorem 3.1].\nWrite ϕ ∈ E 1 as the limit of a decreasing net (ϕi ) in CPSH(ω). Then E(ϕi +εf ) → E↓ (ϕ+εf )\n(by Proposition 8.3 (v)), E(ϕi ) → E(ϕ) (by continuity of E along decreasing nets in PSH(ω)),\nand MA(ϕi ) → MA(ϕ) weakly (by Proposition 7.19).\n  It is therefore enough to prove the result for ϕ ∈ CPSH(ω). Since f ∈ PL(X)R , we can\nchoose ω 0 ∈ Amp(X) and ψ1 , ψ2 ∈ PLR ∩ PSH(ω 0 ) such that f = ψ1 − ψ2 . By Lemma 8.7\nwe have, for any ε > 0,\n                                   ˆ\n                                −1\n                                                                    \u0001n\n   Eω (ϕ + εf ) − Eω (ϕ) − εVω       f ω + ddc ϕ + ε(ω 0 + ddc ψ1 )\n\n                                                                ≤ ε Vω−1 Vω+εω0 − 1 sup |f |.\n                                                                                   \u0001\n\nNow Vω−1 Vω+εω0 − 1 = O(ε), while\n                                              n \u0012 \u0013\n                               \u0001n             X  n j\nVω−1         c          0          c       −1\n       ω + dd ϕ + ε(ω + dd ψ1 ) = MAω (ϕ)+Vω       ε (ω+ddc ϕ)n−j ∧(ω 0 +ddc ψ1 )j ,\n                                                 j\n                                                          j=1\n\nwhere (ω + ddc ϕ)n−j ∧ (ω 0 + ddc ψ1 )j is a Radon measure of mass (ω n−j · ω 0j ). The result\nfollows.                                                                                    \u0003\nProof of Corollary 8.6. For f ∈ PL(X)R the result follows directly from Theorem 8.5. For\nan arbitrary f ∈ C0 (X) we argue as in the proof of [BGM20, Theorem 3.1]. By Theorem 2.2,\nwe can pick a sequence (fm ) in PL(X)R such that εm := sup |f − fm | → 0. For each t > 0,\nwe have fm − tεm ≤ f ≤ fm + tεm ; Proposition 8.3 (i) thus yields\n                  E↓ (ϕ + tfm ) − tεm ≤ E↓ (ϕ + tf ) ≤ E↓ (ϕ + tfm ) + tεm ,\nand hence          ˆ                                \u0010                 \u0011\n                     fm MA(ϕ) − εm ≤ lim inf t−1 E↓ (ϕ + tf ) − E↓ (ϕ)\n                                           t→0+\n                                \u0010                    \u0011 ˆ\n                             −1    ↓             ↓\n                 ≤ lim sup t      E (ϕ + tf ) − E (ϕ) ≤ fm MA(ϕ) − εm ,\n                       t→0+\nby Theorem 8.5 applied to fm . Letting m → ∞, we get\n                               \u0010                    \u0011 ˆ\n                            −1    ↓             ↓\n                      lim t      E (ϕ + tf ) − E (ϕ) = f MA(ϕ),\n                            t→0+\n\nand replacing f with −f concludes the proof.                                                 \u0003",
  "0d1fe3897017983ff0019ce21e31375b437e0ec6ac241f485c4b4be1ce7a3bfb": "9.1. The energy of a measure. Denote by M = M(X) the space of Radon probability\nmeasures on X an . It is a compact convex subset of the dual C0 (X)∨ for the weak topology.\nFix a class ω ∈ Amp(X).\nDefinition 9.1. The energy of a Radon probability measure µ ∈ M is defined by\n                                          \u0012       ˆ     \u0013\n                  E∨ (µ) := E∨\n                             ω (µ) := sup  E(ϕ) −   ϕ µ   ∈ [0, +∞].                       (9.1)\n                                                  ϕ∈E 1\n\nWe say that µ has finite energy if E∨ (µ) < +∞, and denote by M1 ⊂ M the set of such\nmeasures.\n   Here we write E 1 = E 1 (ω) for simplicity. As we shall see, measures in M1 = M1 (ω) have\na prescribed mass on each Xαan , determined by ω (see Corollary 9.13). However, when X is\nirreducible, M1 turns out to be independent of ω ∈ Amp(X) cf. Theorem 9.24 below.\n   By definition, measures of finite energy integrate all functions in E 1 . Combined with\nCorollary 7.48, this implies:\nLemma 9.2. Measures in M1 put no mass on pluripolar sets.\n  We will later study the dependence Amp(X) 3 ω → E∨    ω (µ) for a fixed measure µ ∈ M.\nAlready now, we note that Proposition 7.7 (iii) implies\nLemma 9.3. For ω ∈ Amp(X), t ∈ R>0 and µ ∈ M, we have E∨           ∨\n                                                       tω (µ) = t Eω (µ).\n\nProposition 9.4. The energy functional E∨ : M → [0, +∞] satisfies:\n      (i) for each µ ∈ M we have\n                                                          \u0012      ˆ   \u0013\n                                     ∨\n                                 E (µ) =          sup      E(ϕ) − ϕ µ ;                    (9.2)\n                                            ϕ∈Hdom (ω)\n\n      (ii) E∨ is convex, lsc, and homogeneous with respect to the scaling action of R>0 , i.e.\n                                            E∨ (t? µ) = t E∨ (µ)\n          for all µ ∈ M and t ∈ R>0 ;\nProof. Denote by S ∈ [0, +∞] the right-hand side of (9.2). Trivially, E∨ (µ) ≥ S. Conversely\npick ϕ ∈ E 1 , and choose a decreasing net (ϕj ) in Hdom (ω) such that ϕj → ϕ. Then\nE(ϕ) ≤ E(ϕj ), and hence\n                 ˆ        \u0012         ˆ      \u0013 ˆ                        ˆ\n         E(ϕ) − ϕ µ ≤ E(ϕj ) − ϕj µ + (ϕj − ϕ)µ ≤ S + (ϕj − ϕ)µ.\n                    ´            ´\nBy Lemma 7.17,          ϕj µ →       ϕ µ; hence\n                                            \u0012       ˆ   \u0013\n                                     ∨        ∨\n                                 E (µ) = sup E (ϕ) − ϕ µ ≤ S,\n                                            ϕ∈E 1\n\nwhich proves (i).                                                                      ´\n   Convexity and lower semicontinuity of E∨ follow directly from (i), since µ 7→ E(ϕ) − ϕ µ\nis affine and continuous for every ϕ ∈ PL ∩ PSH(ω). Now pick µ ∈ M and t ∈ R>0 . Note\n\f             GLOBAL PLURIPOTENTIAL THEORY OVER A TRIVIALLY VALUED FIELD              101\n\nthat ϕ 7→ t · ϕ = tϕ(t−1 ·) is a bijection of E 1 . By Proposition 7.7 we infer\n                   \u0012             ˆ             \u0013\n  E∨ (t? µ) = sup E(t · ϕ) − (t · ϕ)(t? µ)\n               ϕ∈E 1\n                                  \u0012        ˆ   \u0013       \u0012      ˆ  \u0013\n                             = sup t E(ϕ) − tϕµ = t sup E(ϕ) − ϕµ = t E∨ (µ),\n                               ϕ∈E 1                         ϕ∈E 1\n\nwhich concludes the proof of (ii).                                                    \u0003\nDefinition 9.5. For each C > 0 we set\n                           M1C := µ ∈ M | E∨ (µ) ≤ C .\n                                   \b\n\n  By (ii) of Proposition 9.4, M1C is a (weakly) compact, convex subset of M.\n  The next result provides an important source of examples of measures of finite energy.\nIn fact, we will see in §12.2 that when the envelope property holds for ω, every measure\nµ ∈ M1 is of the form MA(ϕ) for ϕ ∈ E 1 .",
  "8c4787d9dd7c44e5dff7df46694689982d269d05ef3f964e8a769bed43ef3154": "  The next duality statement will be used in the proof of Theorem 9.11.\nProposition 9.9. For any usc function ϕ : X an → R ∪ {−∞}, we have\n                                        \u0012         ˆ    \u0013\n                          E↓ (ϕ) = inf E∨ (µ) + ϕ µ .                                   (9.8)\n                                           µ∈M\n\nProof. Write ϕ as the limit of a decreasing net (ϕi ) in C0 (X). On the one hand, for each\nµ ∈ M we have                                           ˆ\n                             E↓ (ϕ) ≤ E(ϕi ) ≤ E∨ (µ) + ϕi µ,\n                                      ´\nby (9.7), and hence E↓ (ϕ) ≤ E∨ (µ) + ϕ µ, by Lemma 7.17. On the other hand,\n                     \u0012          ˆ     \u0013       \u0012        ˆ      \u0013\n                        ∨                        ∨\n                 inf E (µ) + ϕ µ ≤ inf E (µ) + ϕi µ = E(ϕi ),\n                    µ                            µ\n\nwhere the right-hand side converges to E↓ (ϕ), by Proposition 8.3 (v). This proves (9.8).   \u0003\n\f            GLOBAL PLURIPOTENTIAL THEORY OVER A TRIVIALLY VALUED FIELD                     103\n\n9.3. Maximizing nets. With a view towards solving the Monge–Ampère equation MA(ϕ) =\nµ, we introduce the following notion.\nDefinition 9.10. Given a measure µ of finite energy, we ´shall \u0001say that a net (ϕi ) in E 1 is\nmaximizing for µ if it computes E∨ (µ) = supϕ∈E 1 E(ϕ) − ϕ µ in the sense that\n                                         ˆ\n                                E(ϕi ) − ϕi µ → E∨ (µ).\n\n  As a key consequence of the uniform differentiability property of Theorem 8.5, we prove:\nTheorem 9.11. Let µ be a measure of finite energy. For any maximizing net (ϕi ) for µ we\nhave MA(ϕi ) → µ weakly in M.\n                             ´              ´\nProof. It is enough to ´show f MA(ϕi ) → f µ for any f ∈ PL(X), by Theorem 2.2. Set\nδi := E∨ (µ) − E(ϕi ) + ϕi µ, so that δi → 0. For any ε > 0, (9.8) shows that\n                               ˆ                                ˆ\n                 ↓                              ∨\n                E (ϕi + εf ) − (ϕi + εf ) µ ≤ E (µ) = E(ϕi ) − ϕi µ + δi .\n\nBy Theorem 8.5, we infer\n                                ˆ                      ˆ\n                            ε        f MA(ϕi ) ≤ ε         f µ + δi + Cε2\n\n                              ´ of i and ε. Dividing by ε, letting i → ∞, and then ε → 0,\nfor a constant C´ > 0 independent\nwe get lim supi f MA(ϕi ) ≤ f µ, and replacing f with −f yields the result.            \u0003\n  This yields a variational characterization of solutions to Monge–Ampère equations:\nCorollary 9.12.´ Pick\u0001 ϕ ∈ E 1 and µ ∈ M1 . Then MA(ϕ) = µ iff ϕ computes E∨ (µ) =\nsupψ∈E 1 E(ψ) − ψ µ . In particular, E∨ (µ) = 0 iff µ = MA(0).\n                                  ´\nProof. If MA(ϕ) = µ then E(ϕ) − ϕ µ = E∨ (µ) by (9.3). If the converse holds then the\nconstant net ϕi = ϕ is maximizing, and hence MA(ϕ) = µ, by Theorem 9.11.           \u0003",
  "c915032bf0eebe8ad404adbb1262524c60dd0957a37dd0431389370c7693214f": "    Thanks to Theorem 7.8, we can make sense of the definitions from §3.3 for functions in\nE 1 . In particular, we set, for any two ϕ, ψ ∈ E 1 ,\n                        dω (ϕ, ψ) :=    max kϕ − ψk2(ω,ϕ)j ·(ω,ψ)n−1−j\n                                       0≤j≤n−1\n\nwith\n  kϕ − ψk2(ω,ϕ)j ·(ω,ψ)n−1−j = −(0, ϕ − ψ)2 · (ω, ϕ)j · (ω, ψ)n−j\n                               ˆ\n                           = − (ϕ − ψ) ddc (ϕ − ψ) ∧ (ω + ddc ϕ)j ∧ (ω + ddc ψ)n−j . (7.21)\n\nProposition 7.27. For all ϕ, ψ ∈ E 1 we have:\n                            n       ˆ\n                       1 X −1\n     E(ϕ) − E(ψ) =             V      (ϕ − ψ) (ω + ddc ϕ)j ∧ (ω + ddc ψ)n−j ;          (7.22)\n                    n+1\n                           j=0\n                ˆ                                   ˆ\n                  (ϕ − ψ) MA(ϕ) ≤ E(ϕ) − E(ψ) ≤ (ϕ − ψ) MA(ψ);                         (7.23)\n                                                ˆ\n                     d\n                            E((1 − t)ϕ + tψ) = (ψ − ϕ) MA(ϕ);                          (7.24)\n                     dt t=0\n                                             n−1\n                                             X\n                                       −1\n                         I(ϕ, ψ) = V               kϕ − ψk2(ω,ϕ)j ,(ω,ψ)n−1−j ;        (7.25)\n                                             j=0\n                                             X\n                               I(ϕ, ψ) =           cα I(ϕ|Xαan , ψ|Xαan ).             (7.26)\n                                              α\n                                       n−1\n                                       X     j+1\n                       Jψ (ϕ) = V −1             kϕ − ψk2(ω,ϕ)j ,(ω,ψ)n−1−j ;          (7.27)\n                                             n+1\n                                       j=0\n                               1                       n\n                             n+1 I(ϕ, ψ) ≤ Jψ (ϕ) ≤ n+1 I(ϕ, ψ);                       (7.28)\n                          V −1 dω (ϕ, ψ) ≈ I(ϕ, ψ) ≈ Jψ (ϕ) ≈ Jϕ (ψ);                  (7.29)\n                              I(ϕ1 , ϕ2 ) . I(ϕ1 , ϕ3 ) + I(ϕ3 , ϕ2 ).                 (7.30)\nProof. As in Lemma 3.26, (7.22), (7.24), (7.25) and (7.27) follow from straightforward com-\nputations based on the multilinearity and symmetry of the energy pairing on E 1 , while (7.26)\nfollows from (7.4). Equation (7.23) follows from (3.16) by monotone approximation. Equa-\ntions (7.25) and (7.27) imply (7.28) and (7.29), and (7.30) is now a consequence of Theo-\nrem 3.31 and monotone approximation.                                                        \u0003\n  Taking into account (7.24), we can write (7.28) as\n                        E(ψ) + E0 (ψ)(ϕ − ψ) − E(ϕ) ≥ n+1\n                                                       1\n                                                          I(ϕ, ψ),                     (7.31)\nwhich can be seen as a strict concavity property of E with respect to I. Indeed, it yields the\nfollowing uniform concavity estimate:\nTheorem 7.28. For any two ϕ, ψ ∈ E 1 and t ∈ [0, 1] we have\n                E((1 − t)ϕ + tψ) − ((1 − t) E(ϕ) + t E(ψ)) & t(1 − t) I(ϕ, ψ).\n  The proof relies on the following elementary estimate, which is certainly well-known.\nLemma 7.29. For all a, b ∈ R≥0 and t ∈ [0, 1] we have (1 − t)a + tb ≥ t(1 − t)(a + b).\n\f86                           SÉBASTIEN BOUCKSOM AND MATTIAS JONSSON\n\nProof. By homogeneity we may assume a + b = 1. Write t = 21 + x and a = 12 + y with\nx, y ∈ [− 12 , 21 ], where we may assume x ≥ 0, by symmetry. Then\n              1      1        1      1     1                    1    1       1\n(1−t)a+tb = ( −x)( +y)+( +x)( −y) = −2xy, t(1−t)(a+b) = ( +x)( −x) = −x2 ,\n              2      2        2      2     2                    2    2       4\nand hence\n                                       1            1 1           1\n      (1 − t)a + tb − t(1 − t)(a + b) = − 2xy + x2 ≥ − x + x2 = ( − x)2 ≥ 0.\n                                       4            4 2           2\n                                                                               \u0003\n\nProof of Theorem 7.28. Set ϕt := (1 − t)ϕ + tψ. By (7.31), we have\n                              ˆ\n                      E(ϕt ) + (ϕ − ϕt ) MA(ϕt ) − E(ϕ) & I(ϕ, ϕt )\n\nand                                    ˆ\n                            E(ϕt ) +       (ψ − ϕt ) MA(ϕt ) − E(ψ) & I(ϕt , ψ),\n\nSince (1 − t)(ϕ − ϕt ) + t(ψ − ϕt ) = 0, this yields\n                    E(ϕt ) − ((1 − t) E(ϕ) + t E(ψ)) & (1 − t) I(ϕ, ϕt ) + t I(ψ, ϕt )\n\n                           ≥ t(1 − t) (I(ϕ, ϕt ) + I(ϕt , ψ)) & t(1 − t) I(ϕ, ψ),\nby Lemma 7.29 and (7.30).                                                                                             \u0003\n\n  For later use, we record the following crucial consequence of Corollary 3.34 (compare [BBGZ13,\nLemma 3.13]).\nLemma 7.30. For all ϕ, ϕ0 , ψ, ψ 0 ∈ E 1 we have\n  ˆ\n                                                        1                                  1\n    (ϕ − ϕ0 ) MA(ψ) − MA(ψ 0 ) . I(ϕ, ϕ0 )αn I(ψ, ψ 0 ) 2 max{J(ϕ), J(ϕ0 ), J(ψ), J(ψ 0 )} 2 −αn\n                               \u0001\n\n\nwith αn := 2−n .\nProof. After regularization, we may assume ϕ, ϕ0 , ψ, ψ 0 ∈ PLR ∩ PSH(ω). Note that\n    ˆ\n  V (ϕ − ϕ0 ) MA(ψ) − MA(ψ 0 ) = (0, ϕ − ϕ0 ) · (ω, ψ)n − (0, ϕ − ϕ0 ) · (ω, ψ 0 )n\n                                 \u0001\n\n                                                    n−1\n                                                    X\n                                                =         (0, ϕ − ϕ0 ) · (0, ψ − ψ 0 ) · (ω, ψ)j · (ω, ψ 0 )n−1−j .\n                                                    j=1\n\nBy the Cauchy–Schwarz inequality (3.17) we infer\n\n     (0, ϕ − ϕ0 ) · (ω, ψ)n − (ϕ − ϕ0 ) · (ω, ψ 0 )n\n                     . max kϕ − ϕ0 k(ω,ψ)j ·(ω,ψ0 )n−1−j kψ − ψ 0 k(ω,ψ)j ·(ω,ψ0 )n−1−j\n                                                                                        \u0001\n                        j\n                                                     \u0012                                    \u0013\n                                                                                                  1\n                                                  ≤ max kϕ − ϕ k(ω,ψ)j ·(ω,ψ0 )n−1−j dω (ψ, ψ 0 ) 2\n                                                                     0\n                                                                 j\n\nand Corollary 3.34 together with (7.29) yield the desired estimate.                                                   \u0003\n\f             GLOBAL PLURIPOTENTIAL THEORY OVER A TRIVIALLY VALUED FIELD                      87\n\nCorollary 7.31. For all ϕ, ϕ0 , ψ ∈ E 1 we have\n                  | Jψ (ϕ) − Jψ (ϕ0 )| . I(ϕ, ϕ0 )αn max{J(ϕ), J(ϕ0 ), J(ψ)}1−αn\nwith αn = 2−n .\nProof. Set M := max{J(ϕ), J(ϕ0 ), J(ψ)}. We have\n                                 ˆ                          ˆ\nJψ (ϕ) − Jψ (ϕ ) = E(ϕ ) − E(ϕ) + (ϕ − ϕ ) MA(ψ) = Jϕ0 (ϕ) + (ϕ − ϕ0 )(MA(ψ) − MA(ϕ0 )),\n              0       0                  0\n\n\nand (7.28) and Lemma 7.30 thus yield\n                                                                           1    1\n                   | Jψ (ϕ) − Jψ (ϕ0 )| . I(ϕ, ϕ0 ) + I(ϕ, ϕ0 )αn I(ψ, ϕ0 ) 2 M 2 −αn .\nBy the quasi-triangle inequality, we have\n                      I(ϕ, ϕ0 ) = I(ϕ, ϕ0 )αn I(ϕ, ϕ0 )1−αn . I(ϕ, ϕ0 )αn M 1−αn\nand I(ψ, ϕ0 ) . M , and we obtain, as desired, | Jψ (ϕ) − Jψ (ϕ0 )| . I(ϕ, ϕ0 )αn M 1−αn .   \u0003\n   By Proposition 7.21 (i), Monge–Ampère measures of bounded ω-psh functions integrate\nall ω-psh functions. In that setting, (7.6) yields the following simpler variant of Lemma 7.30,\nwhich can be viewed as a version of the classical Chern–Levine–Nirenberg inequality.\nLemma 7.32. If ψ, ψ 0 ∈ PSH(ω) are bounded, then\n                       ˆ\n                         ϕ MA(ψ) − MA(ψ 0 ) ≤ n sup |ψ − ψ 0 |\n                                             \u0001\n\n\nfor all ϕ ∈ PSH(ω).\n  We conclude this section with two useful additional estimates.\nLemma 7.33. For each ϕ, ψ ∈ E 1 and t ∈ [0, 1] we have\n                   I(tϕ + (1 − t)ψ, ψ) ≤ (1 − (1 − t)n ) I(ϕ, ψ) ≤ nt2 I(ϕ, ψ)\nand\n                                                               1\n                              Jψ (tϕ + (1 − t)ψ) ≤ t1+ n Jψ (ϕ).\n                                                ´\nProof. Adding a constant to ´ϕ, we may assume (ϕ−ψ) MA(ψ) = 0. Set ϕt := tϕ+(1−t)ψ.\nThen ϕt − ψ = t(ϕ − ψ), so (ϕt − ψ) MA(ψ) = 0, and\n                ˆ\n  I(ϕt , ψ) = −t (ϕ − ψ) MA(ϕt )\n                              n \u0012 \u0013               ˆ\n                             X    n j\n                    = −tV −1          t (1 − t)n−j (ϕ − ψ)(ω + ddc ϕ)j ∧ (ω + ddc ψ)n−j .\n                                  j\n                             j=0\n                                                             ´\nHere the integral vanishes for j = 0 and is bounded below by (ϕ − ψ) MA(ϕ) for j > 0, so\n                                             ˆ\n                I(ϕt , ψ) ≤ −t(1 − (1 − t)n ) (ϕ − ψ) MA(ϕ) ≤ nt2 I(ϕ, ψ),\n\nby the concavity of t 7→ (1 − (1 − t)n ).\n  To prove the last inequality, note that\n                                                          ˆ\n                         Jψ (ϕt ) = E(ψ) − E(ϕt ) + t         (ϕ − ψ) MA(ψ).\n\f88                           SÉBASTIEN BOUCKSOM AND MATTIAS JONSSON\n\nDifferentiating this with respect to t, and using (7.28), gives\n                   ˆ                     ˆ\n     d\n       Jψ (ϕt ) = − (ϕ − ψ) MA(ϕt ) + (ϕ − ψ) MA(ψ) = t−1 I(ϕt , ψ) ≥ n+1\n                                                                       n t\n                                                                          −1\n                                                                             Jψ (ϕt )\n    dt\nfor 0 < t ≤ 1, from which the desired estimate follows easily.                        \u0003",
  "8fea27f105319057b1c2362e8de17ca887a5bcbb1d1070f757aaf0be2cc75b31": "Definition 9.14. For any µ ∈ M1 we define a functional Jµ : E 1 → [0, +∞) by\n                                                   ˆ\n                                      ∨\n                           Jµ (ϕ) := E (µ) − E(ϕ) + ϕ µ.\n\n  The notation is justified by the fact that for ϕ, ψ ∈ E 1 we have\n                                   ˆ                       ˆ\n            JMA(ψ) (ϕ) = E(ψ) − ψ MA(ψ) − E(ϕ) + ϕ MA(ψ) = Jψ (ϕ).                         (9.9)\n\nNote also that\n                                         Jµ (0) = E∨ (µ),                                (9.10)\nand that a net (ϕi ) in E 1 is maximizing for µ iff Jµ (ϕi ) → 0.\nLemma 9.15. For all ϕ, ϕ0 ∈ E 1 we have\n                               I(ϕ, ϕ0 ) ≈ inf (Jµ (ϕ) + Jµ (ϕ0 )).\n                                          µ∈M1\n\nIn particular, we have for all ϕ ∈ E 1 and µ ∈ M1\n                                     J(ϕ) . Jµ (ϕ) + E∨ (µ).                             (9.11)\nProof. On the one hand, inf µ (Jµ (ϕ) + Jµ (ϕ0 )) ≤ Jϕ (ϕ0 ) ≈ I(ϕ, ϕ0 ), thanks to (7.28). Con-\nversely, set τ := 12 (ϕ + ϕ0 ). By strict concavity of E (Theorem 7.28),\n                            ˆ                               ˆ\n           ∨                          1             0     1\n          E (µ) ≥ E(τ ) − τ µ ≥ (E(ϕ) + E(ϕ )) −              (ϕ + ϕ0 ) µ + Cn−1 I(ϕ, ϕ0 ),\n                                      2                   2\nand hence\n                                inf (Jµ (ϕ) + Jµ (ϕ0 )) & I(ϕ, ϕ0 ).\n                                 µ\n\nIn particular, J(ϕ) ≈ I(ϕ, 0) . Jµ (ϕ) + Jµ (0) = Jµ (ϕ) + E∨ (µ), which proves the final\npoint.                                                                                 \u0003\nCorollary 9.16. Pick µ ∈ M1 , and choose a maximizing net (ϕi ) for µ. Then J(ϕi ) .\nE∨ (µ) + o(1) for all i large enough.\nLemma 9.17. For each C > 0 we have\n                         ˆ\n                                                     1\n                            ϕ (µ − MA(ψ)) . C Jµ (ψ) 2\n\nfor all ϕ, ψ ∈ {J ≤ C} ⊂ E 1 and µ ∈ M1C .\nProof. By monotone approximation, we may assume ϕ ∈ PLR . Pick a maximizing sequence\n(ψi ) for µ. By Corollary 9.16, J(ψi ) . C + o(1) for all i large enough. By Lemma 7.30, we\ninfer\n           ˆ\n                                                          1                        1\n             ϕ(MA(ψi ) − MA(ψ)) . (C + o(1)) I(ψi , ψ) 2 . C max{Jµ (ψi ), Jµ (ψ)} 2 ,\n\nwhere the right-hand inequality\n                            ´   follows from\n                                          ´ Lemma 9.15. By Theorem 9.11, we have\nMA(ϕi ) → µ weakly; hence ϕ MA(ψi ) → ϕ µ, while Jµ (ψi ) → 0, so we are done.         \u0003\n                                                                    ´\nCorollary 9.18. Pick µ ∈ M1 . If (ϕi ) is maximizing for µ then limi ϕi (MA(ϕi ) − µ) = 0\nand limi E∨ (MA(ϕi )) = E∨ (µ).\n\f             GLOBAL PLURIPOTENTIAL THEORY OVER A TRIVIALLY VALUED FIELD                            105\n\nProof. By Corollary 9.16, J(ϕi ) is bounded for i large enough. By Lemma 9.17, it follows\nthat                         ˆ         ˆ\n                                                                1\n                        ci := ϕi µ − ϕi MA(ϕi ) = O(Jµ (ϕi ) 2 )\ntends to 0, and hence\n                                       ˆ                           ˆ\n             ∨\n            E (MA(ϕi )) = E(ϕi ) −         ϕi MA(ϕi ) = E(ϕi ) −       ϕi µ + ci → E∨ (µ),\n\ncompleting the proof.                                                                               \u0003\n  As another useful consequence, we get:\nProposition 9.19. Let ϕi → ϕ be a convergent net in PSH(ω), and assume that J(ϕi ) is\neventually bounded. For any µ ∈ M1 we then have ϕi → ϕ in L1 (µ).\n                                    ´\nProof. We first claim that ψ 7→ ψ µ is continuous on {J ≤ C} ⊂ PSH(ω) for ´any C > 0.\nTo see this, pick a maximizing net (ρj )j for µ in PL ∩ PSH(ω). For each          ´ j, ϕ 7→ ϕ MA(ρ ´ j)\nis continuous on PSH(ω), by Proposition 7.19 (ii). By Lemma 9.17, ψ MA(ρj ) → ψ µ\nuniformly for ψ ∈ {J ≤ C} ⊂ PSH(ω), and the claim follows since continuity is preserved\nunder uniform convergence.\n   The functional J is lsc, so J(ϕ) ≤ lim inf J(ϕi ) < ∞. Set ϕ0i := max{ϕi , ϕ}, so that\n|ϕi − ϕ| = 2(ϕ0i − ϕ) + (ϕi − ϕ). Then ϕ0i → ϕ pointwise on X div , i.e. ϕ0i → ϕ in PSH(ω).\nBy (7.34) we further have I(ϕ0i , ϕ) ≤ I(ϕi , ϕ), and J(ϕ0i ) ≈ I(ϕ0i , 0) is thus eventually\n                                                                                        ´      bounded,\n                                                                                                  ´\nby\n´ 0 the quasi-triangle\n          ´            inequality\n                            ´      for I. The  first part of  the proof    thus  yields   ϕi µ → ϕ µ,\n  ϕi µ → ϕ µ, and hence |ϕi − ϕ|µ → 0, which concludes the proof.                                    \u0003\n9.4. Dependence on the ample class. In this section, X is assumed to be irreducible.\nAs in [BBGZ13, Proposition 3.4] we then have the following useful characterization of mea-\nsures of finite energy.\nTheorem 9.20. A Radon probability measure µ ∈ M has finite energy iff E 1 ⊂ L1 (µ).\nProof. Assume that´ µ is finite on E 1 . We first claim that for each C > 0 there exists\n  0                           0\nC > 0 such that ϕ µ ≥ −C for all ϕ ∈ Esup   1  such that − E(ϕ) = J(ϕ) ≤ C. Arguing by\ncontradiction, we may assume there exist C > 0 and a sequence (ϕj )∞          1\n                                                                      1 in Esup such that\n                ´          j\n                                                    Pm −j\nJ(ϕ) ≤ C and ϕj µ ≤ −2 for all j. Set ψm := j=1 2 ϕj for m ≥ 1. Then ψm is a\ndecreasing sequence in PSH(ω) converging to ψ := ∞          −j\n                                                    P\n                                                      j=1 2 ϕj , which is thus either ω-psh\nor identically −∞ (since X is irreducible). By concavity of E we have E(ψm ) ≥ −C for all\nm; hence ψ is ω-psh, with E(ψ) = limm→∞ E(ψm ) ≥ −C. On the other hand, monotone\nconvergence gives\n                   ˆ              ˆ               m\n                                                  X       ˆ\n                     ψ µ = lim      ψm µ = lim        2−j ϕj µ = −∞,\n                               m→∞                  m→∞\n                                                          j=1\na contradiction. We next claim that there exist A, B > 0 such that\n                                 ˆ\n                                    ϕ µ ≤ A J(ϕ)1/2 + B\n             1 , which will imply, as desired, that\nfor all ϕ ∈ Esup\n                                             \u0012 ˆ      \u0013\n                              ∨\n                             E (µ) = sup − ϕ µ − J(ϕ)\n                                              1\n                                           ϕ∈Esup\n\f106                       SÉBASTIEN BOUCKSOM AND MATTIAS JONSSON\n\nis finite. If J(ϕ) ≤ 1 then the estimate follows from the first part of the proof. We may\nthus assume t := J(ϕ)−1/2 ≤ 1. By Lemma 7.33, J(tϕ) ´. t2 J(ϕ) = 1, and the first part of\nthe proof yields a uniform constant A > 0 such that t ϕ µ ≤ A, which gives the desired\nestimate.                                                                              \u0003",
  "18e1abc1b9d68ea1a5ffbfb4c1d03eeb30a5b4fac482f44f9ea2b9a64c5d4233": "7.6. Locality and the comparison principle. The next result and its consequences play a\ncrucial role in analyzing deep properties of ω-psh functions and the Monge-Ampère operator.\nTheorem 7.40. If ω ∈ Amp(X), then\n                                1{ϕ>ϕ0 } MA(max{ϕ, ϕ0 }) = 1{ϕ>ϕ0 } MA(ϕ)                                     (7.32)\nfor all ϕ, ϕ0 ∈ E 1 (ω).\n  A first consequence is the fact that the mixed Monge–Ampère operator is local in nature,\nsomething that is not an immediate consequence of our definition in §7.3.\nCorollary 7.41. Let G ⊂ X an be open set. If ωi ∈ Amp(X) and ϕi , ψi ∈ E 1 (ωi ), 1 ≤ i ≤ n,\nare such that ϕi = ψi on G, then\n       (ω1 + ddc ϕ1 ) ∧ · · · ∧ (ωn + ddc ϕn ) = (ω1 + ddc ψ1 ) ∧ · · · ∧ (ωn + ddc ψn ) on G.\nIn particular, if ω ∈ Amp(X) and ϕ, ϕ0 ∈ E 1 (ω) are such that ϕ = ϕ0 on G, then MA(ϕ) =\nMA(ϕ0 ) on G.\nProof. By multilinearity, it suffices to prove the final statement. As in [BFJ15, Corollary 5.2],\ngiven ε > 0 we apply Theorem 7.40 to ϕ+ε and ϕ0 . This gives MA(max{ϕ+ε, ϕ0 }) = MA(ϕ)\non G ⊆ {ϕ+ε > ϕ0 }. Letting ε → 0 gives MA(max{ϕ, ϕ0 }) = MA(ϕ) on G, since the Monge–\nAmpère operator is continuous under decreasing limits. Exchanging the roles of ϕ and ϕ0\ncompletes the proof.                                                                           \u0003\nRemark 7.42. As mentioned in Remark 7.23, when all the functions involved are continu-\nous, the mixed Monge–Ampère measure coincides with the one in [CLD12]. Since the latter\nis local in nature, Theorem 7.40 and Corollary 7.41 follow in this case. However, for appli-\ncations it is important to consider functions ϕ, ϕ0 that are not continuous, and in this case\nthe Borel set {ϕ > ϕ0 } can be quite complicated. By definition, it is an open subset in the\nplurifine topology, see [BT87].\nLemma 7.43. Let ϕ, ϕ0 ∈ PL(X), and pick an integrally closed test configuration X such\nthat ϕ, ϕ0 and ϕ00 := max{ϕ, ϕ0 } are associated to elements D, D0 , D00 of VCar(X )Q . Pick\nan irreducible component E of X0 , and assume that ϕ(vE ) > ϕ0 (vE ). Then ϕ(vF ) ≥ ϕ0 (vF )\nfor any irreducible component F of X0 that intersects E.\n\f92                          SÉBASTIEN BOUCKSOM AND MATTIAS JONSSON\n\nProof. First, ϕD00 −D = ϕD00 − ϕD ≥ 0 implies D00 − D ≥ 0, by Lemma 2.8, and similarly\nD00 − D0 ≥ 0. Furthermore, 0 < ϕ00 (vE ) − ϕ0 (vE ) = σ(vE )(D00 − D0 ), and E is thus in the\nsupport of D00 − D0 . Now pick any k × -invariant divisorial valuation w on X with center\nξ ∈ E ∩ F , normalized by w(X0 ) = 1; denote by v ∈ X div its restriction to k(X) ,→ k(X ), so\nthat w = σ(v) (see §1.3). Then w(D00 − D0 ) = ϕ00 (v) − ϕ0 (v) > 0, and hence ϕ00 (v) = ϕ(v).\nThis means that D00 = D at ξ; hence 0 = σ(vF )(D00 − D) = ϕ00 (vF ) − ϕ(vF ), which proves\nthe result.                                                                                 \u0003\nProof of Theorem 7.40. First assume that ϕ, ψ ∈ PL ∩ PSH(ω). As in Lemma 7.43, pick\nan integrally closed test configuration X dominating the trivial one, such that ϕ = ϕD ,\nϕ0 = ϕD0 and max{ϕ, ϕ0 } = ϕD00 with D, D0 , D00 ∈ VCar(X )Q . As in Proposition 7.19 (ii)\nwe have                                  X\n                         MA(ϕD ) = V −1     bE ((ωX + D)|E )n δvE ,\n                                                   E\nand a similar formula holds for MA(ϕ ). We thus need to show that ((ωX + D)|E )n =\n                                             D00\n((ωX + D00 ])|E )n for any E with ϕD (vE ) > ϕD0 (vE ). Now Lemma 7.43 yields ϕD (vF ) =\nmax{ϕ(vF ), ϕ0 (vF )} = ϕD00 (vF ) for all components F of X0 that intersect E. This implies\nthat D and D00 coincide in a neighborhood of E. Hence D|E = D00 |E , which implies the\nresult.\n   Now consider the general case. Set\n                             f := max{ϕ − ϕ0 , 0} = max{ϕ, ϕ0 } − ϕ0 .\nThen {ϕ > ϕ0 } = {f > 0}, and it thus suffices to prove that\n                                  f MA(max{ϕ, ϕ0 }) = f MA(ϕ).                                   (7.33)\nIndeed, multiplying by f −1 on {f > 0} will then yield the result.             Let (ϕj )j and (ϕ0j )j be\ndecreasing nets in PL ∩ PSH(ω) converging to ϕ and ϕ0 , respectively, and set\n                            fj := max{ϕj − ϕ0j , 0} = max{ϕj , ϕ0j } − ϕ0j .\nBy the first part of the proof we have fj MA(max{ϕj , ϕ0j }) = fj MA(ϕj ), and (7.33) is now\na consequence of Proposition 7.19 (iii), since max{ϕj , ϕ0j } ∈ E 1 (ω) decreases to max{ϕ, ϕ0 }.\n                                                                                               \u0003\n     Using Theorem 7.40 we obtain the very useful comparison principle.\nTheorem 7.44. If ω ∈ Amp(X) and ϕ, ψ ∈ E 1 (ω), then\n                          ˆ                 ˆ\n                              MA(ϕ) ≥           MA(ψ).\n                                  {ϕ<ψ}                {ϕ<ψ}\n\nProof. We follow [GZ07, Theorem 1.5]. For any ε > 0 we have\n      ˆ                         ˆ                                          ˆ\n  1 = MA(max{ϕ, ψ − ε}) ≥             MA(max{ϕ, ψ − ε}) +                          MA(max{ϕ, ψ − ε})\n                                    {ϕ<ψ−ε}                              {ϕ>ψ−ε}\n                    ˆ                    ˆ                       ˆ                     ˆ\n              =             MA(ψ) +             MA(ϕ) = 1 +              MA(ψ) −              MA(ϕ),\n                  {ϕ<ψ−ε}             {ϕ>ψ−ε}                  {ϕ<ψ−ε}              {ϕ≤ψ−ε}\n\nwhere the second equality follows from Theorem 7.40 and from MA(ϕ − ε) = MA(ϕ). We\ncomplete the proof by letting ε → 0.                                             \u0003",
  "bb829a66d12c3edcf4a1630b08e62a103f7cd7e61972c6c7a16d5a5190a06466": "  Theorem 10.2 will be proved below, together with the following crucial estimates.\nTheorem 10.3. For all ϕ, ϕ0 ∈ E 1 (ω) and µ, µ0 ∈ M1 we have\n    ˆ\n                                                 1                                     1\n      (ϕ − ϕ0 ) µ − µ0 . I(ϕ, ϕ0 )αn I∨ (µ, µ0 ) 2 max{J(ϕ), J(ϕ0 ), E∨ (µ), E∨ (µ0 )} 2 −αn\n                      \u0001\n\n\nwith αn := 2−n . In particular,\n                   ˆ            ˆ\n                                               1\n              0 ≤ ϕ MA(0) − ϕ µ . max{1, J(ϕ)} 2 max{1, E∨ (µ)}1−αn .\n\n  This last estimate should be compared with the trivial bound\n                             ˆ           ˆ\n                        0 ≤ ϕ MA(0) − ϕ µ ≤ J(ϕ) + E∨ (µ),\n\nwhich holds by definition of E∨ .\n  As an important consequence of Theorem 10.3, we have:\nCorollary 10.4. Assume that X is equidimensional. If ϕ, ψ ∈ E 1 , then the following\nproperties are equivalent:\n     (i) MA(ϕ) = MA(ψ);\n    (ii) I(ϕ, ψ) = 0;\n   (iii) ϕ − ψ is locally constant.\n                                                                                        \u0001\nProof. The implications (iii)⇒(i)⇒(ii) are clear. If I(ϕ, ψ) = 0, then I ϕ|Xαan , ψ|Xαan = 0\nfor each irreducible component Xα of X, by (7.26). In order to prove that ϕ − ψ is locally\nconstant, we may thus assume that X is irreducible. After adding constant, assume sup ϕ =\nsup ψ. Then ϕ(v) = ψ(v) for every v ∈ X div , as a consequence of Theorem 10.3 with µ = δv\nand µ0 = δvtriv , since δv ∈ M1 by Proposition 11.1. By Theorem 4.22, we infer ϕ = ψ on\nX an , which proves (ii)⇒(iii).                                                           \u0003\n\f             GLOBAL PLURIPOTENTIAL THEORY OVER A TRIVIALLY VALUED FIELD             109\n\n  Corollary 10.4 in turn implies the following useful results.\nCorollary 10.5. Assume that X is equidimensional. If ϕ, ψ ∈ E 1 satisfy ϕ ≥ ψ and\nE(ϕ) = E(ψ), then ϕ = ψ.\nProof. By (7.4), we may assume that X is connected. From (7.22) and the assumptions, it\nfollows that           ˆ                  ˆ\n                              (ϕ − ψ) MA(ϕ) =          (ϕ − ψ) MA(ψ) = 0.\n                ´\nThus I(ϕ, ψ) = (ϕ − ψ)(MA(ψ) − MA(ϕ)) = 0, and hence ψ = ϕ + c for a constant c, by\nCorollary 10.4. But then E(ϕ) = E(ψ) = 0 gives c = 0 and we are done.             \u0003\nCorollary 10.6 (Domination principle). Assume that X is equidimensional. Let ϕ ∈\nPSH(ω), ψ ∈ E 1 , and assume ϕ ≤ ψ a.e. with respect to MA(ψ). Then ϕ ≤ ψ on X an .\nProof. Arguing on each connected component, we may assume that X is connected. After\nreplacing ϕ with max{ϕ, ψ}, we may assume ϕ ≥ ψ, and hence ϕ ∈ E 1 . The assumption\nthen becomes ϕ = ψ a.e for MA(ψ), and we need to show ϕ = ψ. Note that\n                      ˆ                            ˆ\n             I(ϕ, ψ) = (ϕ − ψ)(MA(ψ) − MA(ϕ)) = (ψ − ϕ) MA(ϕ) ≤ 0.\n\nBy Corollary 10.4, we infer ϕ = ψ + c with c ∈ R, and ϕ = ψ a.e. for MA(ψ) implies\nc = 0.                                                                          \u0003",
  "fa43d7783b4a4bc09ecddf5dc9051ca0f2b97a44aaa137243baa56fa4464de79": "                13. Capacities, pluripolar sets, and negligible sets\n  Assuming the envelope property, we make a more detailed study of pluripotential theory,\nadapting to our setting classical arguments from the complex analytic case. In particular,\nwe prove the fundamental result that negligible sets are the same as pluripolar sets.\n  In what follows, X is of dimension n and irreducible. We fix an ample class ω ∈ Amp(X),\nand we assume that the envelope property holds for ω, see §5.2. As before, we write\nV = Vω = (ω n ) and MA(ϕ) := V −1 (ω + ddc ϕ)n for ϕ ∈ E 1 = E 1 (ω).\n13.1. Envelopes of lsc functions. Consider an arbitrary function ϕ : X an → R ∪ {+∞},\nand assume that ϕ is bounded below. By Lemma 5.17, the usc regularization\n                              P(ϕ)? = sup? {ψ ∈ PSH | ψ ≤ ϕ}\nof the ω-psh envelope P(ϕ) is either ω-psh and bounded, or satisfies P(ϕ)? ≡ +∞.\nTheorem 13.1. Pick any lsc function ϕ : X an → R ∪ {+∞}, and assume P(ϕ)? 6≡ +∞.\nThen\n                     P(ϕ)? = P(ϕ) = ϕ a.e. for MA(P(ϕ)? ).\n  In particular, the orthogonality property\n                             ˆ\n                                   (ϕ − P(ϕ)? ) MA(P(ϕ)? ) = 0                           (13.1)\n                                X an\nholds (compare [BFJ15, BGM20]).\nLemma 13.2. If N ⊂ X an is a negligible Borel set (see Definition 5.1), then µ(N ) = 0 for\nall measures of finite energy µ ∈ M1 .\n   This strengthens in particular Lemma 9.2, since pluripolar sets are negligible (Proposi-\ntion 5.3),\nProof. By Choquet’s lemma (see Corollary 12.22), there exists an increasing, uniformly\nbounded sequence (ϕm )∞                                          ?\n                           1 in PSH(ω) such that N ⊂ {ϕ < ϕ }, where ϕ := limm ϕm\npointwise. Recall that ϕ? ∈ PSH(ω), thanks to the standing assumption that the envelope\nproperty holds. On X div we have ϕ? = ϕ, by Theorem´5.6. Thus ´ϕm → ϕ? weakly in E 1 (and\nin fact strongly as well, by Theorem 12.5), and hence ϕm µ → ϕ? µ,  ´ by Proposition\n                                                                              ´      9.19.\nOn\n´ ?  the other hand, the   monotone convergence  theorem shows that   ϕ m µ →   ϕ µ. Thus\n  (ϕ − ϕ)µ = 0, which implies µ(N ) = 0.                                                \u0003\n\f             GLOBAL PLURIPOTENTIAL THEORY OVER A TRIVIALLY VALUED FIELD                     127\n\nProof of Theorem 13.1. Set ψ := P(ϕ)? and µ := MA(ψ). Assume first ϕ ∈ C0 (X), so that\nψ = P(ϕ) is continuous and ω-psh. Arguing as in the proof of [BGM20, Lemma 3.5], set\nf := ϕ − ψ ≥ 0, and observe that for t ∈ [0, 1],\n                                ϕt := ψ + tf = (1 − t) P(ϕ) + tϕ\nsatisfies P(ϕ) ≤ ϕt ≤ ϕ, and hence P(ϕt ) = P(ϕ). Thus E(ψ + tf ) = E(P(ϕ)) for t ∈ [0, 1],\nand Corollary 8.6 yields\n                         ˆ\n                                             d\n                           (ϕ − ψ) MA(ψ) =          E(ψ + tf ) = 0,\n                                             dt t=0\nand hence ϕ = ψ µ-a.e.\n   Now consider the general case. Since the Borel set {ψ > P(ϕ)} is negligible, Lemma 13.2\nshows that ψ = P(ϕ) µ-a.e. In particular, ψ ≤ ϕ µ-a.e., and it thus remains to show that µ\nputs no mass on the open set U := {ψ < ϕ}.\n   Since ϕ is lsc and X an is compact, there exists an increasing net (ϕj ) in C0 (X) that con-\nverges pointwise to ϕ. By Lemma 5.19, the increasing net ψj := P(ϕj ) converges pointwise\nto P(ϕ). By Theorem 5.6, we thus have ψj → ψ on X div , and Theorem 12.5 implies that\nµj := MA(ψj ) converges weakly to µ. By the first part of the proof, µj puts no mass on the\nopen set Uj := {ψj < ϕj }, and we want to take the limit and deduce that µ(U ) = 0; this\nwill conclude the proof. To do so, suppose µ(U ) > 0, and pick a point v ∈ U ∩ supp µ. Thus\nψ(v) < ϕ(v), so there exists j0 such that ψ(v) < ϕj (v) for j ≥ j0 . Set V := {ψ < ϕj0 }.\nThen V is open, v ∈ V and V ⊂ Uj for j ≥ j0 . Since v ∈ supp µ, we have µ(V ) > 0. As\nµj → µ weakly, we must have µj (V ) > 0 for j \u001d 0, which contradicts µj (Uj ) = 0.           \u0003",
  "e8a2fa603ab776d8fe4365fa5223a77a08f1d03c28595fc0f0c95fcdafc1eb8b": "dle L is a closed (1, 1)-form, which we denote by ddc φ (see [CLD12, §6.4.1] for the non-\nArchimedean case). For each trivializing section τ of L over an open U ⊂ X, the function\nlog |τ |φ is smooth, and ddc φ = −ddc log |τ |φ on U an . Again, this makes sense for Q-line\nbundles as well.\nDefinition 7.11. A smooth metric φ on a Q-line bundle L is semipositive if its curvature\nform ddc φ is semipositive (see [CLD12, §5.4] for the non-Archimedean case).\nExample 7.12. Let L be a line bundle, s1 , . . . sr ∈ H0 (L) be sections without common zeroes,\nλ1 , . . . , λr ∈ R, and maxε : Rr → R a regularized max function. Then\n                          φ := maxε {log |s1 | + λ1 , . . . , log |sr | + λr }\n\f50                        SÉBASTIEN BOUCKSOM AND DENNIS ERIKSSON\n\nis a smooth semipositive metric on L, see [CLD12, 6.3.2].\nDefinition 7.13. A (possibly singular) metric φ on a line bundle L is psh-regularizable if\nφ can be written as the limit of a decreasing net φi of smooth semipositive metrics.\n     If φ is continuous then φi → φ uniformly, by Dini’s lemma.\nTheorem 7.14. Every psh metric φ on a semiample Q-line bundle L is psh-regularizable.\nProof. By Lemma 7.4, it is enough to prove the result when φ is a Fubini–Study metric.\nAfter replacing L with a multiple, there exists a basis (s1 , . . . , sN ) of H0 (L) without common\nzeroes and constants λi ∈ R such that φ = max {log |s1 | + λ1 . . . , log |sN | + λN }, and φ is\nthus the uniform limit as ε → 0 of the smooth semipositive metrics\n                           φε = maxε {log |s1 | + λ1 . . . , log |sN | + λN }\nas in Example 7.12.                                                                             \u0003"
}

END MATHEMATICAL DATA



PREVIOUS FULL REVIEW97 REPORT, diagnostic only; not a mathematical premise:
The full original theorem is not certified by this review. I found no concrete mathematical defect in the deductions I checked, but indispensable scope checks remain unresolved.

I read the supplied argument and opened the version-pinned BJ, BE, Temkin and Wu primary papers. This session exposes no filesystem-reading tool or filesystem MCP resource. Consequently, I could not read the six expressly referenced public-reader files or independently reconcile their contents with the complete grant bindings. Section 1.1’s author-written summaries cannot substitute for that reconciliation. In particular, I cannot certify that every contact, restriction, product, witness domination, collar construction and projective globalization in Sections 3–5 falls within the exact accepted bodies. This is an audit limitation, not a demonstrated mathematical counterexample.

The first-membership deduction has the correct logical order in the accessible text. It retains the original canonical reference, uses whole-boundary collars, takes finite chart maxima, and then applies varying-class closure to the constant scalar ψ. It does not incorrectly use the individually increasing chart extensions as a decreasing family. Once genuine membership is established, the common divisorial coordinates and analytic surjectivity justify the asserted homeomorphism and preservation of suprema. What remains unverified is the complete binding-scope match supplying that membership.

The arbitrary-field argument treats each finite competitor over its own enlarged countable field. Its analytic-surjectivity construction preserves the trivial norm on the enlarged ground field. Orthogonality is transferred by the actual nonnegative integral identity; domination is available without target EP. The compact closed-set argument handles arbitrary genuine competitors without descending an entire psh family. These deductions depend on the countable theorem having been established throughout precisely the granted domain, which the incomplete binding audit prevents me from certifying.

The global theory’s stated scope is supported by [BJ v4](https://arxiv.org/pdf/1801.08229v4): its variety convention permits nonnormal varieties, Section 7 resumes general projective scope, and Theorem 12.8 supplies the EP-to-surjectivity implication. The raw construction retains relative integral closure inside the original generic fiber, central multiplicities b_E, fundamental-cycle intersections, positivity and intersection mass. [BE v3](https://arxiv.org/pdf/1805.01016v3) supports continuous same-bundle approximation, complete-field pushforward and model Deligne-pairing compatibility. The draft does not substitute absolute normalization for the original generic fiber.

The later variational deduction is valid conditional on established target EP: normalized compactness gives an actual psh limit; the bounded-J estimate makes it finite energy; target L1 continuity and energy upper semicontinuity give attainment. Both variation signs then identify the genuine measure against dense PL tests. Raw/probability scaling is consistent, and equal measures give uniqueness modulo a constant. Normalization is used only after approaching target EP; onto E1, mixed unbounded limits and equality of intrinsic dual suprema require the genuine pullback and pairing compatibilities stated in the argument, rather than merely an analytic homeomorphism.

The stated elementary corrections are harmless and valid: the weighted integral is the potential pairing minus the zero-potential pairing; |b−a|=2(max(b,a)−a)−(b−a); continuous-direction errors are |t|ε with both signs; the compactness reference in BJ 12.8 can be replaced by general Theorem 5.11 under EP. BJ’s printed first inequality in Lemma 7.33 also omits a factor t; its proof contains the factor and yields the quadratic estimate used here through I–J comparability.

I checked [Wu v1’s envelope proof](https://arxiv.org/pdf/2609.27610v1#page=51). It calls Proposition 2.24 and Theorem 6.5 before its field-enlargement argument. Its printed envelope conclusion is not an additional granted premise and does not independently discharge proof92’s replacement gates.

The zero-dimensional case is established directly: X is one point, V=1, E_raw(a)=a, the sole mass-one target is the unit point measure, and all finite potentials differ by constants.

Final verified scope: the zero-dimensional case and the primary-source general projective finite-energy equation theory conditional on target EP, with the stated retained field and ample rational polarization hypotheses. The unconditional envelope/first-membership extension for every possibly nonnormal geometrically unibranch target over every permitted field remains unverified in this audit. Compilation, hashes, historical verdicts and serialization observations were not used as mathematical evidence.
