## Actual round70 rational local bridge, smooth weak theorem and finite trace draft; UNREVIEWED

---
title: "Smooth weak globalization and open traces in the unibranch equation problem"
author: "Fresh primary-source reconstruction; unverified proof draft"
date: "5 October 2026"
---

# Disposition and retained domain

The unchanged original P16.1 is not solved here. The target still includes every reduced irreducible geometrically unibranch projective variety over every algebraically closed trivially valued characteristic-zero field, every dimension, every ample line bundle, and arbitrary-support finite-dual-energy measures of raw mass $(L^n)$. The candidate flag is false. No smoothness, countability, normality, or support restriction replaces this target.

The main new partial result is a proof draft of smooth upper-growth **weak affine regularization**, smooth principal-open removal, and the resulting open determinant trace. Its auxiliary inputs are rational corrected local contact functions, defined below. The bridges leading to it are reconstructed here from the ten actual primary sources, rather than assumed from the embedded rounds. In particular the proof establishes genuine membership before applying sequential regularization, and applies birational onto descent only to a smooth target with the required envelope hypotheses. The later countable singular Runge and envelope induction is audited, but not completed.

Throughout $k$ is algebraically closed, trivially valued and characteristic zero. The general projective variety $X$ is reduced irreducible, $n=\dim X$, $L$ is ample, $\omega=c_1(L)$, and $V=(L^n)>0$. BJ's general global results also apply to ample real numerical Cartier classes; no new singular real-class envelope theorem is asserted. The new local constructions use rational line-bundle classes, rational selected branch slopes and rational constants. Contact supports may be real. The sources are BJ 1801.08229v4, Wu 2609.27610v1, CLD 1204.6277v2, GM 1608.08030v3, Wanner 1801.04713v3, Thuillier tel-00010990v1, BE 1805.01016v3, GR 2503.05513v1, published Ducros DOI10.1142/S1793744212500077, and GJR 2111.05741v3. Wu is a public version-one preprint, with no independent correctness verdict assumed. All mathematical claims below are unverified drafts. Execution checks are separate observations.

# Genuine global theory, before singular envelopes

BJ's conventions LF435--469 allow nonnormal reduced varieties. LF3649--3658 explicitly resume general projective varieties in Section 7. Consequently its mixed operator is already a singular-space operator, not a smooth construction transferred to a quotient.

A test configuration is closed integrally in its prescribed generic fiber: on an affine chart close $A$ in $A\otimes_{k[t]}k(t)$. BJ 1.10--1.13 give finiteness, equivariance, generic-fiber preservation and the vertical $R_1,S_2$ criterion. Absolute normalization would change a nonnormal generic fiber and is not substituted. The polar-ideal argument in 1.13 forces the associated polar points to be vertical DVRs by the determinant trick, while depth two excludes higher-codimension poles. Thus each central component $E$ has $b_E=\operatorname{ord}_E(t)>0$ and $v_E=b_E^{-1}\operatorname{ord}_E|_{k(X)}$.

On a common such determination, relatively nef model data give the actual mixed raw measure
$$
 M^{\rm raw}((\theta_1,\phi_1),\ldots,(\theta_n,\phi_n))
 =\sum_E b_E\bigl((\theta_{1,\mathcal X}+D_1)|_E\cdots
                  (\theta_{n,\mathcal X}+D_n)|_E\bigr)\delta_{v_E}. \tag{1}
$$
The intersection includes the central fundamental cycle. Nef restrictions give nonnegative weights. Rational equivalence of central and generic fibers gives mass $(\theta_1\cdots\theta_n)_X$. BJ 4.3 is the actual general-variety model nef criterion.

Compactification over $\mathbb P^1$ gives the symmetric intersection pairing. Projection formula makes it independent of the determination. Translating entry $i$ by $c$ adds $c(\prod_{j\ne i}\theta_j)_X$. BJ 7.1 extends the pairing by the infimum over model majorants. Nef intersections give monotonicity. For usc, select a majorant tuple below a prescribed pairing threshold; the continuous functionals $\sup(\phi_i-\psi_i)$ allow slightly translated majorants near it, and the translation rule bounds the error. This yields decreasing-net continuity. BJ 7.8--7.14 give finite mixed pairings and multilinear extension on differences of finite-energy potentials. Their bounds compare ample classes by positive multiples, estimate the energy of sums, and expand into the mixed nonpositive terms after subtracting constants.

The actual energy and space are
$$
 E_\omega(\phi)=\frac{\langle(\omega,\phi)^{n+1}\rangle}{(n+1)V},\qquad
 \mathcal E^1(X,\omega)=\{\phi\in\operatorname{PSH}(X,\omega):E_\omega(\phi)>-\infty\}.
 \tag{2}
$$
Here $E(0)=0$, $E(\phi+c)=E(\phi)+c$, and $E$ is increasing, concave, usc and decreasing-continuous. PSH is BJ's genuine generated global cone; no auxiliary local cone replaces it.

For an actual algebraic PL test $a$ prescribe
$$
 \int a\,dM^{\rm raw}=\langle(0,a),(\theta_1,\phi_1),\ldots,(\theta_n,\phi_n)\rangle. \tag{3}
$$
Positivity bounds the functional by its mass times $\|a\|_\infty$. BJ 2.2 density and Radon representation construct the measure; multilinearity gives signed products. BJ 7.18--7.19 prove model agreement, exact mass, mixed integrability and decreasing continuity. Weighted continuity 7.21 uses the pairing containing the test **minus** the pairing containing zero. Both pairings converge, and Lemma 7.22 applied to a translated negative test gives weighted weak convergence. This convention corrects the reversed printed differences at LF4119--4123.

The diagonal probability measure is $\operatorname{MA}_\omega(\phi)=V^{-1}M^{\rm raw}_\omega(\phi)$. In the integral scope $\operatorname{MA}(0)=\delta_{v_{\rm triv}}$. Actual model agreement on a strict winning component and weighted continuity give
$$
 \mathbf1_{\{\phi>\psi\}}\operatorname{MA}(\max(\phi,\psi))
 =\mathbf1_{\{\phi>\psi\}}\operatorname{MA}(\phi). \tag{4}
$$
The limiting test is $\max(\phi_j,\psi_j)-\psi_j$. Apply 7.21 separately to its two decreasing psh terms; the difference itself need not decrease. This repairs the last citation at LF4585. Equal masses and (4), with a displaced competitor, give
$$\int_{\{\phi<\psi\}}\operatorname{MA}(\psi)
 \le\int_{\{\phi<\psi\}}\operatorname{MA}(\phi). \tag{5}$$
Ordinary-open mixed locality is BJ 7.41, proved by maxima, decreasing limits and polarization.

Put $I(\phi,\psi)=\int(\phi-\psi)(\operatorname{MA}(\psi)-\operatorname{MA}(\phi))$. Mixed intersection negativity gives $I\ge0$, $I/(n+1)\le J_\psi\le nI/(n+1)$, and
$$E(\phi)-E(\psi)=\frac1{(n+1)V}\sum_{j=0}^n
 \int(\phi-\psi)(\omega+dd^c\phi)^j(\omega+dd^c\psi)^{n-j}. \tag{6}$$
The separation estimate 10.3, finite-dual-energy divisorial Diracs 11.1, and divisorial order theorem 4.22 prove that $I=0$ forces equality after equal-sup normalization. Thus equal measures give one additive real constant on integral $X$. Global domination 10.6 also precedes EP and applies to genuine global potentials. Replacing the lower potential by its maximum with the upper one makes its $I$ nonpositive under the a.e. hypothesis; separation and the a.e. equality remove the constant.

For a positive Radon raw target $\nu$ the exact mass is $V$. With $\mu=\nu/V$, the target condition is
$$E^\vee_\omega(\mu)=\sup_{\psi\in\mathcal E^1}
 \left(E_\omega(\psi)-\int\psi\,d\mu\right)<\infty. \tag{7}$$
BJ 9.20 equates it with integrability of every $\mathcal E^1$ potential on irreducible $X$. To see the operative bounds, normalize $\sup\psi=0$. If integrals were unbounded below on $J\le C$, choose $\psi_j$ with $\int\psi_jd\mu\le-2^j$. The convex partial sums $\sum_{j\le m}2^{-j}\psi_j+2^{-m}0$ decrease, have energy at least $-C$, and limit to a finite-energy potential with integral $-\infty$, a contradiction. The mixed expansion gives $I(t\psi,0)\le nt^2I(\psi,0)$ for $0\le t\le1$. Scaling by $J^{-1/2}$ gives $-\int\psi d\mu\le A\sqrt J+B$, hence (7). A solution necessarily satisfies (7) by the mixed tangent energy inequality. No support restriction is used.

**Conditional equation theorem.** If the genuine envelope property EP holds for $\omega$, every target (7) has a finite-energy solution, unique modulo constants. Conversely onto MA for all such targets implies EP: this is the actual general-variety BJ 12.8, not its smooth sufficient theorem 12.9.

Under EP, 5.11 supplies normalized-PSH compactness: bounded divisorial evaluations, Tychonoff, genuine usc tail suprema, and 5.6 nonnegligibility identify a nontrivial decreasing limit. The uniform energy expansion 8.5 is
$$E^\downarrow(\phi+tf)=E(\phi)+t\int f\operatorname{MA}(\phi)+O_f(t^2),\quad f\in\operatorname{PL}_{\mathbb R}. \tag{8}$$
It writes $f$ as two auxiliary ample model potentials, uses the model-volume bound, and expands mixed positive measures of fixed degrees. Apply both signs. Uniform PL approximation gives the continuous derivative with lower and upper endpoints $\int f_m\operatorname{MA}(\phi)\mp\epsilon_m$; the printed two-minus squeeze is not used. For unbounded $\phi$, identifying $E^\downarrow$ with $E(P(\phi+tf))$ needs EP.

A normalized maximizing sequence for (7) has bounded $J$ by 9.15. Compactness gives a weak subnet, lsc of $J$ makes its limit finite energy, and 9.19 gives target $L^1$ convergence. That theorem uses approximation by maximizing model MA measures before attainment, with uniform errors on bounded-$J$ sets. Its absolute-difference identity is $|a-b|=2\max(a,b)-a-b$. Energy usc gives attainment. Testing (8) for $f$ and $-f$ then gives the genuine equation. The raw objective $VE-\int\phi d\nu$ is translation invariant exactly because $\nu(X^{\rm an})=V$. Strong target completeness and the MA embedding give completeness after surjectivity. Conversely increasing bounded model maxima are Cauchy by (6), and completeness plus divisorial determination gives EP. Strict concavity does not supply this missing geometric antecedent.

Dimension zero is separate: $X=\operatorname{Spec}k$, $V=1$, $E(c)=c$, and the one-point equation is immediate.

# Corrected rational auxiliary classes and elementary closures

A finite continuous local function belongs to $\mathcal C_{\mathbb Q}$ if locally it is a continuous selection from finitely many rational affine formulas in regular log norms, with rational constants. Each formula must be finite on its stated neighborhood. Thus at an infinite coordinate its coefficient is zero on the chart containing that point; after shrinking, the remaining used functions are units. Positivity means an affine support $\ell+C$, finite nearby on the relative image, with
$$b(t')\ge\ell(t')+C,\qquad b(t)=\ell(t)+C. \tag{9}$$
The same constant occurs in both expressions. Supports can be real even though selected branches are rational. The usc nontrivial local decreasing limits of sequences in this class, on common neighborhoods, form $\mathcal P_{\mathbb Q}$. Limits may have logarithmic poles. This is an auxiliary correction, not a redefinition of genuine global PSH.

For affine $Y=\operatorname{Spec}R$, actual AFS means
$$\operatorname{AFS}(R)=\{\max(\lambda,c_i\log|f_i|+C_i)_i:\ c_i>0,\ c_i,\lambda,C_i\in\mathbb Q,\ (f_i)\text{ includes algebra generators}\}.$$
Upper growth always means $u\le b+O(1)$. The literal lower-growth convention in Wu 3.15(2) excludes $\max(\log|z|,-m)\downarrow\log|z|$ at zero and cannot be used. Omitting $C$ in the minorant inequality likewise makes the printed contact condition inadequate.

Restriction, algebraic pullback, maximum and positive rational sums preserve these local classes: concatenate coordinates; at a maximum choose the support of a winning function; for a sum add supports. For decreasing sequences distribute finite products of indices along a diagonal, because only finitely many sequences are involved locally. Adding a harmonic unit logarithm changes the support by that affine term. Real constants in limits can be approximated from above rationally.

Finite maxima and positive rational sums preserve AFS. Distribute maxima and clear rational exponents into regular monomials. To retain a generator branch, choose the floors in all other factors. The resulting coefficient is positive rational and the intercept rational; the floor is the sum of floors. Differences form a rational vector lattice by $\max(a-b,c-d)=\max(a+d,c+b)-(b+d)$. AFS sublevels are compact because generator branches bound the seminorms in a closed affine embedding.

A weak input on an affine variety means a function finite at the generic trivial seminorm whose pullback by a proper birational algebraic witness is locally in $\mathcal P_{\mathbb Q}$. Proper closedness proves usc downstairs: the closed superlevel set is the image of its closed upstairs inverse image. This does not yet prove genuine global membership.

# Strict rational representation and the continuous metric bridge

## Rational polyhedral branch domains

Take $K=k((\varpi))$ with $-\log|\varpi|=1/q$. On a compact strict analytic domain, finitely many analytic units have finite rational polyhedral log image by published Ducros 3.2. Its proof uses valued-field image 1.2: closedness is obtained by coarsening an infinitesimally perturbed valuation; independent varying coordinates force a transcendence-degree upper bound. The conclusion is dimension **at most** the analytic dimension. The unnecessary CLD dimension equality is not used; a constant moment map has dimension zero.

Refine the finite image by all equality hyperplanes of the candidate rational affine expressions. On a connected relative open cell, two expressions either agree identically or differ everywhere. At a point the selected value is separated from all different values, so continuity makes its equivalence class locally constant. Connectedness makes it fixed on the cell; continuity extends its value to the closed cell. Each closed-cell preimage is defined by finitely many rational monomial inequalities in units. Clear slopes and constants: inequalities become $|\varpi^a\prod u_j^{m_j}|\le1$. They are strict Laurent domains, with equality expressed in both directions. They form a finite admissible cover. Indeed they are closed and cover the compact original domain, and the union of members containing a point contains a neighborhood of that point after discarding the finitely many closed members not containing it. This is the quasi-net condition for the finite strict-domain G-cover. On each member an integer multiple of the selected weight is $\log|a|$ for a unit $a$.

The compact strict neighborhoods used here are constructed below, before Ducros is applied. Infinite and identically zero coordinates are discarded on their finite affine chart. Compactness gives a finite cover and one common tensor denominator. A continuous relative PL picture alone, or arbitrary real slopes, would not supply this conclusion.

## Analytic curve sign test

Let $\Omega=\widehat{\overline K}$. On every smooth analytic $\Omega$-curve map into a weight chart, coordinate pullbacks remain analytic units. GR 5.1 uses local algebraicity of the source curve; it does not turn the map or its units into algebraic ones. On a small strictly affinoid curve neighborhood the unit-log harmonicity theorem Thuillier 2.3.21 and the definition of harmonic functions give one common semistable skeleton. Equivalently, 2.2.24 applies the Shilov bound to a unit and its inverse, obtaining equality on every retraction fiber. Its log is piecewise affine and has zero interior weighted Laplacian. Finitely many units use the same skeleton, with common refinements.

On subdivided edges, a finite selection of affine functions can switch only at intersections of different affine functions. There are finitely many; coincident functions give the same value. This proves lisse membership, allowing real breakpoints. At an interior point subtract the pulled support $H=\ell(\log|u_j|)+C$. It is harmonic, and $b-H$ has local minimum zero. Every outgoing slope is nonnegative and the weighted sum of the slopes of $H$ is zero. Therefore
$$\Delta b(\{x\})=\sum_e w_e\partial_e(b-H)\ge0. \tag{10}$$
The type III case has two outgoing directions. At type I and IV points, unit-log germs are constant on a smaller neighborhood by the proof of Thuillier 2.3.21, LF3604--3607; a continuous selection of finitely many constant values is locally constant. Discard zero and identically zero coordinates before taking logs. Affinoid boundary slopes are not tested on the curve open. Thuillier 3.4.4/Wanner 2.11 and the sheaf property give subharmonicity; 3.1.8 gives decreasing stability with the identically $-\infty$ alternative.

Wanner's field is complete algebraically closed nontrivially valued. Section 4 additionally fixes a smooth proper algebraic curve. If using its current identification, first compactify a locally algebraic source curve by its normal projective function-field model, smooth over perfect $\Omega$, and apply only on the original open. The direct slope test above already works with analytic units and does not require extending the function through that boundary.

## An actually glued ample metric

Suppose $B$ is an ample rational bundle on projective $X$, and an actual globally glued continuous metric has local weights in $\mathcal C_{\mathbb Q}$. Rational strict neighborhoods and the selection argument give strict integer PL after one tensor power. If $N$ times a local weight is $\log|a_i|$, then $a_i e_i^N$ has norm one. On overlaps its transition is $(a_i/a_j)(e_i/e_j)^N$, an actual unit of norm one. GM 2.10 constructs the formal bundle: a common model realizes the finite domains as formal opens, and admissible blowups make every transition and inverse integral. The transition cocycle is the given metric on the given bundle.

The curve test proves subharmonicity for every smooth analytic curve map over $\Omega$. Now actual strict PL membership permits GR 5.1 and 5.4, giving residue nefness. GJR 7.1 realizes it by a nef model on a compact strict neighborhood, and 7.6 permits field detection. Frame changes add harmonic unit logs. GM 3.11 tests every proper residual curve of the global represented model by a point reducing to its generic point; its actual interior-neighborhood condition and a common dominating model identify the local residual closure with that curve. This proves global nefness. GM **Lemma** 3.3 detects nefness back on the already represented $K$-model if checked over $\Omega$ first.

Proper formal/algebraic representation is GM 2.6. Projective representation follows by GM 2.4: dominate by the completion of a vertical blowup of an initial projective model over the noetherian Laurent DVR, then algebraize the bundle. Its prescribed generic fiber remains $X_K$. BE 7.8 applies over nontrivial $K$ to the ample $B_K$, with no smoothness hypothesis. It perturbs a nef model toward an ample model of the same generic bundle and gives uniform pure FS approximation; use $\epsilon\downarrow0$ and the same ample model consistently in the printed $H/A$ formulas.

No general current pullback/converse is assumed. GR Remark 1.8 warns this is unknown for general R-PL positive currents. CLD 17.8.4 is nef-to-psh for strict integer PL; 18.8.4 and 18.8.6 concern already represented integer PL metrics. They cannot supply their own representation antecedents. The route above avoids smooth-only BJ 4.19.

# Exact Gauss descent, compact PL extension and collars

## Global FS coefficient cutoff

BJ Remark 1.9 gives a continuous Gauss section $\sigma$ of $\pi:X_K^{\rm an}\to X^{\rm an}$. Independently, complete $H(x)(T)$ with independent Gauss variable of radius $e^{-1/q}$ and map $\varpi$ to $T$. For Laurent coefficients in a finite $k$-span of chart functions,
$$\left|\sum_{r\ge r_0}\varpi^r f_r\right|_{\sigma(x)}
 =\max_{r\ge r_0}e^{-r/q}|f_r(x)|. \tag{11}$$
Tails tend uniformly to zero on compact charts; finite maxima prove continuity and localizations agree. Independence of $T$ prevents cancellation, even if its radius belongs to $|H(x)^\times|$. This is not an expansion over $\Omega$.

For a generating FS system in $H^0(X_K,mB_K)$, flat $H^0$ base change expands $s_j=\sum_r\varpi^r f_{jr}$ with $f_{jr}\in H^0(X,mB)$. Properness gives a valuation-ring center at every $x$; in a frame there, every $k$-section is regular, so its norm for the canonical trivial metric $h_0$ is at most one. Thus the Gauss potential is
$$\sigma^*\psi=\frac1m\max_{j,r}
 \{\log\|f_{jr}\|_{mh_0}+\lambda_j-r/q\}. \tag{12}$$
The left side is finite continuous on compact $X^{\rm an}$, with lower bound $b$. All sufficiently large $r$ terms are uniformly below $b$, so (12) is exactly a finite maximum. Its retained sections generate: a nonempty common zero locus has a closed $k$-point, contradicting finiteness there. Rational weights stay rational. Uniform errors and decreasing limits survive pullback by $\sigma$. Over trivial $k$ these FS systems belong to BJ's $H(B)$, and 4.18 identifies the decreasing generated cone with genuine PSH. The continuous metric just constructed is therefore genuine CPSH.

## Exact model-function descent

A rational model function $F_K$ is a model metric on $\mathcal O_{X_K}$. On a projective algebraic determination clear its denominator. BE 5.14/5.16(vi) express it exactly as $\psi-\psi'$: twist its model bundle by $r\mathcal A$ for any ample model bundle $\mathcal A$ and large $r$. Suitable multiples of $r\mathcal A+\mathcal B$ and $r\mathcal A$ are relatively globally generated. Their finite sections give exact pure FS metrics. Their common generic rational class $M$ need not descend.

Choose a fixed ample $H/k$ and $a$ large so $aH_K-M$ is ample. A pure FS metric $\tau$ on it cancels in $(\psi+\tau)-(\psi'+\tau)$. Product sections, with common tensor multiples, put both on the same descending $aH_K$, exactly as in BE 5.17. Apply (12) only to the **final** sections of multiples of $aH_K$. The difference of the two descended rational FS potentials is $F_K\circ\sigma$, so it is actual BJ algebraic PL. Neither equivariance nor a prescribed generic class for $\mathcal A$ is needed; positivity of the difference is not inferred.

For a finite rational local selection $f$ near a compact set $C\Subset U$, choose a compact union $W$ of the rational neighborhoods below with $C\subset\operatorname{int}W\subset W\subset U$. Over a finite Laurent field the selection lemma makes $Nf_K$ an actual formal metric on the trivial bundle on compact strict $W_K$. GM 2.7 extends it to that same bundle on paracompact strict $X_K^{\rm an}$. Algebraize and apply exact model-function descent. The resulting global BJ PL function agrees with $f$ on $W$, hence near $C$. No agreement on all of $U$ is claimed or needed.

## Principal-open collar algebra on nonnormal $X$

Choose a very ample power and a section $s$ nonzero at the algebraic support of $x\in U$. The affine $D(s)$ contains a basic neighborhood given by finitely many upper/lower regular evaluations. Invert only the functions with a positive lower bound containing $x$. None vanishes at $x$; inverse functions convert those bounds into upper bounds.

Section localization does not need normality. On a finite affine trivializing cover it is ordinary module localization, and finite equalizers and matching relations commute with filtered colimits. Hence
$$\Gamma(D(s),\mathcal O_X)=\varinjlim_d H^0(X,A^d)/s^d.$$
Write the inverted functions as $\tau_i/s^{d_i}$. Then $a=s\prod_i\tau_i$ is a section of some positive ample power $L^d$, with
$$D(a)=D(s)\cap\bigcap_iD(\tau_i)$$
exactly. The extra $s$ excludes the old boundary. Clear every new regular constraint by one power $a^m$, and take $m$ large enough that $L^{dm}$ is very ample. Add a complete section system, the constraint numerators and $a^m$. Ratios of the complete system to $a^m$ generate $k[D(a)]$ by its closed affine standard-chart embedding.

Give all constraints rational upper bounds strictly containing $x$, and give additional generators large rational bounds. With rational $\lambda<0$, the FS weight in class $c_1(L)$ is
$$v=\frac1{dm}\max\{dm\lambda,\log|\sigma_j/a^m|-C_j\}. \tag{13}$$
The constraint bound is $C_j$, not $dmC_j$. Generator bounds make $Q=\{v\le0\}$ compact, and the original constraints put it inside $U$. Choose rational $\epsilon>0$ below all divided margins and with $\lambda<-\epsilon$. Then $x\in\operatorname{int}P$, $P=\{v\le-\epsilon\}\subset\operatorname{int}Q$. The inclusion uses the uniform strict margin in every constraint. After clearing rational thresholds, the domains are strict affinoid over a finite Laurent field. This also constructs the compact neighborhoods used earlier.

# Bounded rational local products and smooth local/global equality

Here all inputs are bounded common-neighborhood decreasing limits in $\mathcal P_{\mathbb Q}$. The theorem does not identify arbitrary weak inputs with that class.

Write the FS reference in (13) as $\theta=\omega+dd^cp$, where $p$ is a bounded rational global model potential. For a finite mixed tuple and its tests, choose a common bound $M$ on a neighborhood of $Q$, rational $A$ with $A\epsilon>2M+1$, and $h=Av+M+1$. On $P$, $h<-M$. On the compact strip $Q\cap\{v\ge-1/(2A)\}$, $h\ge M+1/2$. The closed sets $\{u_{i,j}\ge h\}$ there decrease to the empty set. Compactness gives one whole tail with strict inequality, without Dini to a discontinuous limit.

Set $\Psi_{i,j}=\max(u_{i,j}-h,0)$ on $Q$, zero outside. A whole reference-winning collar makes it continuous globally. Its interior metric weight is $\max(u_{i,j}-M-1,Av)$; elsewhere it is the reference. The continuous metric bridge gives genuine global PSH in class $A\theta$. Its bounded decreasing limit is genuine and finite energy. Set
$$\Phi_i=\Psi_i/A+p,\qquad G=v-p+(M+1)/A. \tag{14}$$
On $P$, $u_i/A=\Phi_i+G$ and the curvature of $G$ is the original reference $\omega$, so
$$dd^cu_i=A(\omega+dd^c\Phi_i). \tag{15}$$
Define the local mixed measure by $A^n\bigwedge_i(\omega+dd^c\Phi_i)$ on the inner domain. If retaining the metrics in class $A\theta$ instead, the factors already contain $A$ and no extra $A^n$ is inserted.

For continuous inputs genuine continuous compatibility BJ 7.23/7.42 and CLD locally uniform convergence identify this with the intrinsic continuous products. The actual BE Section 8 fixes an arbitrary projective scheme and includes fundamental-cycle lengths, not only a smooth variety. Its 8.4 uniform extension is proved by testing against an FS difference and transferring $dd^c$ by IBP. In the display at LF2726 the last term must be subtracted; the triangle bound by the two positive mixed degrees still follows. Its 8.18 proof uses a relatively regular model section, induction on dimension and vanishing of its log norm at Shilov points, justified by 8.19. Thus it identifies actual model Deligne intersections with continuous products, including signed differences. These statements handle continuous metrics; they supply no bounded-decreasing local theorem by themselves. Fixed-collar limits are the explicit truncations $\max(u_i-h,0)$, hence independent of the supplied sequence. To compare two collars or sequences, choose a third smaller shared collar. Compare the first sequence in its original and shared data using continuous locality and decreasing convergence against compactly supported continuous tests; repeat for the second. In the shared data both have the same explicit global limit. This proves overlap and approximation independence without equality of unrelated approximant measures or MA monotonicity.

For a bounded decreasing local test use $u_{0,j}=A\Phi_{0,j}+AG$. BJ 7.21 treats the first term; compact cutoffs treat fixed continuous $G$. A signed global PL cutoff is a difference of two positive global curvature pairs on one common ample class, by the FS difference construction. Pass each positive term separately using 7.19 and 7.21 before subtracting. Bounded tests are integrable.

Construct actual global rational PL cutoffs from BJ density and lattice operations. For compact shrinkings $K_i\Subset U_i$ covering compact $X^{\rm an}$, take continuous bumps $a_i=1$ on $K_i$, supported in $U_i$. Approximate within $1/8$ by rational PL $p_i$ and put $\chi_i=\min(1,\max(0,2p_i-1/2))$. Its support lies in the compact set $\{p_i\ge1/4\}\Subset U_i$, and it is one on $K_i$. Define
$$\rho_1=\chi_1,\qquad \rho_i=\min(\chi_i,1-\sum_{j<i}\rho_j). \tag{16}$$
The partial sum is $\min(1,\sum_{j\le i}\chi_j)$, so all entries are nonnegative, subordinate, rational PL and sum to one. No variable denominator appears.

Exact compact local PL extensions and symmetric global pairing give compact model IBP, with support in the cutoff chart:
$$\int a\,dd^cu_1\wedge T=\int u_1\,dd^ca\wedge T. \tag{17}$$
For arbitrary signed local rational PL weights split into same-class FS differences. Continuous compatibility and locality justify restriction of their global extensions. Passing continuous approximants to bounded limits uses the weighted theorem above, with a further cutoff one near the original support. The signed cutoff measure remains supported there: it is zero on constant opens at the continuous level, and testing these opens passes this assertion separately for the two positive terms. CLD 8.7.2 is used only for continuous locally uniform convergence, never as a bounded-decreasing theorem.

For a bounded global locally $L$-psh $\phi$, put $T=\omega+dd^c\phi$, $T_0=\omega$ and $S=\sum_{j=0}^{n-1}T^jT_0^{n-1-j}$. In a chart use the same reference weight $g_i$ for both $\phi+g_i$ and $g_i$. Subtract their compact IBP identities to obtain
$$\int\rho_i(T^n-T_0^n)=\int\phi\,dd^c\rho_i\wedge S.$$
All signed measures and bounded weighted integrals agree on overlaps, have their controlled supports, and are finite. Thus their sum is $dd^c(\sum\rho_i)\wedge S=dd^c1\wedge S=0$. Summing proves exact raw mass $V$. Changing one factor at a time proves mixed mass $(L_1\cdots L_n)$ for rational reference data. This is a telescoping mass proof, not a normalization convention.

On a shared inner collar the floors are inactive, and maximum commutes with truncation. Genuine winning-locus locality transfers (4), and equal raw mass gives (5) for bounded global local potentials. For divisorial order, compare two potentials with the same reference and collar. Their genuine truncations are ordered on divisorial points inside $Q$ and equal to zero outside. BJ 4.22 orders them everywhere; on $P$ the floors are inactive and (15) recovers the desired order. This is independent local divisorial determination, not merely injectivity of evaluations.

BJ 2.12 realizes each source-convention rationally scaled divisorial point as a central component on a relatively integrally closed flag blowup. BJ 2.33 puts an ample test bundle there, giving positive actual weight $b_E(\mathcal L|_E)^n$. Thus a bounded genuine model test has a positive atom without any Dirac equation. Its local class membership follows from uniform decreasing rational FS approximation, rather than assuming its local weight is an algebraic convex maximum. Translate the test $b$ below $\phi$ with uniform margin and use $\phi_t=(1-t)\phi+tb$, rational $t\downarrow0$. Under $\phi\le\psi$ MA$(\psi)$-a.e., comparison gives full MA$(\phi_t)$ mass to $\{\phi_t<\psi\}$, while mixed positivity gives an atom at the tested point of size at least $t^n$ times that of $b$. Let $t\downarrow0$ and use divisorial order. This proves bounded local domination.

On smooth projective $X$, known smooth EP 5.20 now proves local/global equality. Use the directed decreasing net of all continuous majorants of a bounded usc obstacle, with common bounds and finite minima. Compact Hausdorff separation proves its pointwise infimum is the obstacle; no majorant sequence is assumed. Continuous genuine envelope metrics have decreasing rational FS sequences by uniform density, rational rounding and error shifts, so belong to the stated local class. For $p=P(f)$, the envelope of $p+t(f-p)$ is still $p$ for $0\le t\le1$: it lies between $p$ and $f$. The actual continuous energy derivative gives $\int(f-p)\operatorname{MA}(p)=0$. On contact the local obstacle is below $p$, and local domination gives this everywhere. Decreasing global closure identifies the obstacle with the limit. Bounded floors extend the conclusion to nontrivial unbounded local inputs. For an actual rational nef pullback reference, add a positive rational multiple of an ample FS reference, use the smooth ample result, and use genuine class closure from above. This gives precisely the smooth nef local/global input used next, without singular EP.

# New smooth weak affine regularization

**Theorem (auxiliary smooth weak theorem).** Let $Y$ be smooth irreducible affine over the retained arbitrary $k$. Let $u$ be weak in the corrected rational local sense (in particular finite at the generic trivial seminorm), and $u\le b+C$ for actual AFS $b$ on $Y$. Then $u$ is a pointwise decreasing limit of actual rational AFS functions on all of $Y^{\rm an}$. No countable-field hypothesis is used.

We supply the algebraic compactification and signs. Embed $Y$ as a closed affine standard chart of a projective closure, with ample effective hyperplane boundary. Characteristic-zero resolution can be chosen as a finite sequence of blowups outside smooth $Y$, so the resolution is an isomorphism there. For a boundary blowup $\pi$, let $I_Z\mathcal O=\mathcal O(-E)$. Then $E$ is effective and **$-E$ is relatively ample**. Since the center is supported in $D$, some $\mathcal O(-m_0D)$ lies in $I_Z$, so $m_0\pi^*D-E$ is effective. For $m$ sufficiently large, $m\pi^*D-E$ is ample, and every component of $\pi^{-1}\operatorname{Supp}D$ has positive coefficient: its coefficient is $m\operatorname{ord}_F(\pi^*D)-\operatorname{ord}_F(E)$ and the first order is positive. No other component occurs. Iterating gives a smooth projective $X\supset Y$ with effective ample boundary of exactly the required support. This corrects the two exceptional-bundle signs in Wu LF1193--1196.

Choose very ample $B=\mathcal O(rD)$, boundary section $s$, and a rational complete FS reference $h=h_0+p$. Shift rationally so $g=-\log\|s\|_h\ge1$. It is a proper exhaustion tending uniformly to infinity at the boundary. Section localization expresses each source generator and every polynomial appearing in $b$ as $F/s^d$. Bounded section norms for continuous $h$ give $\log|F/s^d|\le dg+C_F$. There are finitely many branches; enlarge a rational $A$ to absorb their constants and the growth constant using $g\ge1$. Then $u\le Ag$ uniformly on $Y$.

Resolve and projectively dominate the proper birational witness, then compactify its graph and resolve it to a smooth projective map $\bar\pi:Z\to X$, still dominating that witness over $Y$. Projective domination is necessary if the original witness is not quasiprojective. Pullback preserves the local corrected class by the elementary closures above; maps need not be analytic isomorphisms. Resolution and projective domination are the retained characteristic-zero algebraic inputs, not consequences of an equation theorem.

For rational $c>1$ and rational $M<0$, define a potential relative to the actual nef reference $cA\bar\pi^*h$ by
$$\Psi_M=\max(\bar\pi^*u-cA\bar\pi^*g,M)\text{ on }\bar\pi^{-1}Y,
 \qquad\Psi_M=M\text{ on its complement}. \tag{18}$$
The bound $\bar\pi^*u-cA\bar\pi^*g\le-(c-1)A\bar\pi^*g$ gives a whole constant collar at every boundary point. On the interior the metric weight is $\max(\bar\pi^*u,M+cA\bar\pi^*g)$, in the local decreasing class by max stability. On the collar it is the actual reference plus a constant. The potential is globally bounded; smooth nef local/global equality makes it genuine. Decreasing $M$ to minus infinity gives a nontrivial genuine limit, since $u$ is finite somewhere. Its boundary value is minus infinity.

The BJ potential relative to the canonical metric is $Q_M=\Psi_M+cA\bar\pi^*p$, not just $\Psi_M$. Apply actual BJ **Lemma** 5.13 to $\bar\pi$ with target class $cA c_1(B)$. Approaching larger ample target classes have known smooth EP. This meets the target-side hypothesis; no singular-target birational descent is used. The descended potential $Q$ equals $u-cAg+cAp=u-cAg_0$ on $Y$, where $g_0=-\log\|s\|_{h_0}$, and is minus infinity on $X\setminus Y$. This follows from equality of the pullback metrics and analytic surjectivity, since the values in (18) were fiber-constant already.

Now BJ 12.16 and 12.18(iii) apply to an **already genuine** global potential in a fixed ample rational class. They have no countable-field antecedent and do not inherit EP from the preceding subsection. In the general proof, after normalizing below zero, $\exp(Q)$ is bounded finite energy by 4.11, and monotone strong convergence yields an increasing index map from $\mathbb N$. It need not be a cofinal subnet. Divisorial finiteness and order determine the original limit. The nef case gives varying classes, so the same-class sequence is used only after descent to the ample smooth target.

Let $Q_j\downarrow Q$ be the sequence in $H^{\rm dom}(cA c_1(B))$. Example 3.9 places each in actual $H(cAB)$. Its local weight along the boundary-section frame on $Y$ is
$$u_j=Q_j+cAg_0,$$
which decreases exactly to $u$. After clearing tensors, all numerator sections are regular ratios by a power of $s$. Append the constant branch $s^l$ and a complete high very ample section system on the same power, with rational weights sufficiently low to be dominated by that particular continuous metric on compact $X$. The appended branches change no maximum. Their ratios generate $k[Y]$ by the standard-chart closed embedding. Thus the result is actual AFS, with a positive rational tensor factor, generators and floor. A basepoint-free system alone was not declared to be an affine embedding. This completes the theorem for the stated corrected rational auxiliary class.

# Controlled approximation and exact smooth removal

We reconstruct the controlled step rather than cite Wu 3.25 as its own proof. An AFS exhaustion $g\ge1$ has an explicit rational ample compactification: clear its slopes by $D$, embed using their integer powers and all original affine generators, and add the original generators at low dominated weights. The domination follows from $\log|z|-M\le\max(D\lambda,p\log|z|+DC)$ for $p\ge1$ and large $M$. The hyperplane chart is exactly $Y$, and its rational FS local weight is $g$.

For an already supplied AFS sequence $u_j\downarrow u\le g$, choose negative integers $C_r\downarrow-\infty$, rational $R_r\uparrow\infty$ with $R_r>2-C_r$, and increasing $j_r$ with $u_{j_r}<g+1$ on $Q_r=\{g\le R_r\}$. Compact decreasing closed-set emptiness proves this last choice. Set, relative to twice the reference class,
$$\phi_r=\max(u_{j_r}-2g,C_r)\text{ on }Q_r,\qquad \phi_r=C_r\text{ outside}. \tag{19}$$
Near the boundary the first term is below $1-R_r<C_r$, giving a whole constant collar. The continuous metric bridge makes it genuine CPSH. On $Q_{r-1}$ both branches decrease. On the expanding annulus the old potential equals $C_{r-1}$ and the new first branch is below $1-g\le1-R_{r-1}<C_{r-1}$. Outside $Q_r$ both are their floors. Thus the sequence decreases globally, with limit $u-2g$ on $Y$ and minus infinity on the boundary.

Choose rational uniform FS approximants $F_r$ with errors $\epsilon_r=4^{-r}$ and shifts $B_r=2\sum_{i\ge r}\epsilon_i$. Then $H_r=F_r+B_r$ decreases, since $H_r-H_{r-1}\le\epsilon_r-\epsilon_{r-1}\le0$. After actual generator/floor conversion its affine weights $w_r=H_r+2g$ decrease to $u$ and obey $w_r\le2g+\sup H_1$. Errors are metric differences and remain uniform on the entire affine chart. The same moving truncation with one continuous $\mathcal C_{\mathbb Q}$ function $b\le h$ in every collar proves genuine global membership of $b-2h$ without assuming prior affine regularizability.

For already regularizable $v$ on $Y_f$ with $v\le g$ on that open, use $g_c=\max(g,-(c/3)\log|f|)$, rational $c>0$. This is an actual exhaustion of $Y_f$ with the old generators and $f^{-1}$. Controlled approximants obey
$$w_i+c\log|f|\le\max(2g+c\log|f|,(c/3)\log|f|)+B. \tag{20}$$
On every bounded neighborhood the right side tends to minus infinity along $Z(f)$. Floors $D_i\downarrow-\infty$ therefore give continuous contact rational functions $b_i=\max(w_i+c\log|f|,D_i)$ on $Y_f$, equal to $D_i$ on a genuine neighborhood of each point of $Z(f)$. Polynomial degree bounds dominate them all by one AFS exhaustion $h$ on $Y$. Single-function moving collars make $\psi_i=b_i-2h$ genuine on a fixed compactification, with boundary minus infinity. They decrease and satisfy $\psi_i\le-h$. Hence $\eta_i=\max(\psi_i,-i)$ is continuous genuine CPSH with a whole constant boundary collar. Uniform FS approximations and the same summable shifts yield an explicitly decreasing AFS sequence for $v_c=v+c\log|f|$ on $Y_f$, minus infinity on $Z(f)$. All max and uniform-density uses occur in the genuine cone after membership has been proved.

**Smooth removal theorem.** If $Y$ is smooth and $v$ is such an already regularizable input on $Y_f$ with upper growth from $Y$, it has a unique regularizable extension on $Y$ with upper growth. For uniqueness, and to match a given weak $u$ extending it, use the divisorial argument below.

Choose $c_j\downarrow0$ rational and one AFS $h$ dominating every $v_{c_j}$, using $c_j\log|f|\le\max(c_1\log|f|,0)$ and polynomial bounds. On a smooth ample-boundary compactification dominate $h\le Ag$, $g\ge1$. The already-regularizable collar construction gives genuine canonical potentials
$$Q_j=v_{c_j}-2Ag+2Ap=v_{c_j}-2Ag_0\text{ on }Y,$$
with boundary minus infinity, in the one fixed ample class $2Ac_1(B)$. They have a common global upper bound. Known smooth EP makes $H_m=(\sup_{j\ge m}Q_j)^*$ genuine; these tail envelopes decrease. On $Y_f$, with $a=\log|f|$ finite continuous,
$$\sup_{j\ge m}c_ja=c_m\max(a,0). \tag{21}$$
For $a<0$ the supremum is zero, generally unattained. Therefore the tail supremum there is the usc function $v-2Ag_0+c_m\max(a,0)$, and its regularization does not change it on that open. The decreasing genuine limit $H$ is nontrivial and equals $v-2Ag_0$ there. This proves membership without a false global monotonicity claim. The common growth bound, continuous on $Y$, survives usc regularization and yields the extension's upper growth. The fixed-class FS sequence and exact generator conversion give a regularizable extension $\widetilde v=H+2Ag_0$.

Every source-convention divisorial point has generic algebraic support and thus belongs to $Y_f$. Two regularizable extensions agree there. Near a compact collar, floor both by $-M$, add the same local reference, and apply the bounded divisorial-order construction in both directions; then let $M\to\infty$. This proves uniqueness. If an existing weak $u$ is given, pull both functions to its resolved proper witness. They agree at every divisorial point, all lying over $Y_f$; the same bounded-floor argument identifies their values even on the exceptional locus and on $Z(f)$. Ordinary density or usc alone would not prove this equality.

# Actual open determinant traces and radial identification

Let $\pi:Y\to S$ be finite surjective with $Y$ integral affine and $S$ a smooth affine open of $\mathbb A_k^n$. For a finite locally free $B/A$ of rank $d$, a fiber over $s$ is $B\otimes_AH(s)=\prod_yB_{s,y}$ with $m_y=\dim_{H(s)}B_{s,y}$ and $\sum m_y=d$. These weights include Artinian length and residue degree.

For $u=\max(\lambda,c_i\log|f_i|+C_i)$ clear coefficients by $D$, take $b_0=1$, $b_i=f_i^{Dc_i}$, $w_0=D\lambda$, $w_i=DC_i$, and the basis-independent determinant
$$P(T)=\det(\operatorname{mult}_{\sum T_i b_i})=\sum_{|\beta|=d}a_\beta T^\beta\in A[T].$$
It is an endomorphism of the invertible determinant module; global freeness is unnecessary. Geometric Artinian composition series factor it into residue linear forms repeated with their lengths. Weighted Gauss norms are multiplicative at every positive real radius: the lexicographically largest maximal exponents in two polynomials yield a unique maximal contribution at their sum, which cannot cancel. Hence
$$N(u)=\sum_y m_yu(y)=\max_\beta
 \left(D^{-1}\log|a_\beta|+D^{-1}\sum_i\beta_iw_i\right). \tag{22}$$
The $T_0^d$ coefficient gives floor $d\lambda$. Source generators express every pulled base generator polynomially; small positive rational $\eta_j$ and large rational $M_j$ give $u\ge\eta_j\log|g_j\circ\pi|-M_j$. Adding the dominated traced branches $d\eta_j\log|g_j|-dM_j$ leaves (22) unchanged and supplies actual base-algebra generators. Thus the trace is actual AFS. Supplied decreasing sequences trace termwise; generic nontriviality is checked separately.

Under complete field extension, original idempotent factors split into refined Artinian factors whose dimensions sum to the original dimension. Their residue norms restrict uniquely. Trace base change therefore holds for every pulled function, including minus infinity with local upper bounds, without any regularization antecedent.

Choose a dense **principal** $W\subset S$ with $\pi$ étale above it, shrinking also so a supplied proper witness for the weak $u$ is an isomorphism over its inverse image if needed later. Finite images of the exceptional closed set have smaller dimension, so such a shrink is available. The smooth weak theorem regularizes $u$ on the smooth affine $\pi^{-1}W$. Determinants trace that sequence on $W$. Monic root bounds for integral source coordinates and polynomial bounds on base coefficients give $u\le Cg\circ\pi+C'$ for one actual base exhaustion. Its trace is bounded by $dCg+dC'$, retaining the rank. Smooth principal-open removal on the smooth base now gives a genuine AFS-regularizable extension of the open trace to $S$. At the generic trivial fiber the source has one degree-$d$ function-field factor and $u$ is finite by the smooth theorem, so the trace limit is nontrivial. This constructs the previously missing open-trace Step 2 in the corrected rational auxiliary scope.

The nonflat weights and radial Step 3 are separate. For global AFS tests, the generic norm polynomial extends across the nonflat locus: its coefficients are integral over normal $A[T]$ and belong to $\operatorname{Frac}(A)[T]$, hence belong to $A[T]$. Normalize the preimage of a line through the $H(s)$-rational lift, generically in the étale open. The height bound gives dimension at least one for each component and finiteness at most one. Each dominates the line; normalization is a smooth finite-flat curve over the perfect completed field, of total rank $d$. Its positive slicing weights are not necessarily original nonflat fiber-algebra dimensions.

For a finite map between smooth curves over any complete residue-characteristic-zero field, extend to a completed algebraic closure, adjoining a Laurent parameter first if trivial. The curve lemma makes the pulled local decreasing inputs subharmonic or identically minus infinity. At a rational center, disk comparison gives $h(0)\le h(\xi_R)$, where $\xi_R$ is the boundary Gauss point; usc and $\xi_R\to0$ give $h(\xi_R)\to h(0)$, including minus infinity. This is a radial Gauss limit, not an arbitrary punctured limit. Locally $t=cz^eU(z)$, $U(0)=1$; residue characteristic zero permits a convergent analytic $e$th root of $U$ and an invertible coordinate change, giving $t=cy^e$. A small target Gauss point has one source Gauss point in each source disk, with residue equation $Y^e=\alpha T$ irreducible by Eisenstein at $T$. Its actual fiber dimension is $e$, the same as the center's Artinian length. Finite properness excludes other preimages nearby. Radial limits pass the open weighted trace equality to the center. If a summand tends to minus infinity, the other finitely many terms are locally bounded above, so no subtraction of infinities occurs.

Global AFS tests fix the slicing weights before choosing a weak witness: their difference lattice contains rational constants and separates finite fibers by truncated distinguishing regular norms and dominated generator branches. Its uniform closure on a finite set interpolates all real values by finite lattice operations. Equal trace sums for all tests therefore force equality of each weight for different slices. For a weak input, choose a line after shrinking the witness isomorphism locus; properness extends its generic lift through each normalized curve DVR. The curve lemma and radial argument identify the already constructed open-trace extension with the fixed weighted sum everywhere. No affine regularization theorem over arbitrary $H(s)$ was used.

These are auxiliary trace results, not an equation theorem on $Y$ or $S$, and not yet the complete weak split-piece/Runge theorem.

# Further analytic applications and the indispensable remaining gates

The continuous Rossi input has a noncircular construction. An actual AFS reference has the ample hyperplane compactification described above. A continuous corrected contact rational $v$ equal to that reference off a compact set gives a globally continuous metric: its difference is zero on an open neighborhood of the projective boundary. The continuous metric bridge yields uniform global FS approximation. High very ample section systems with low dominated weights give actual affine generators and a floor. Uniform metric error is the same on the whole affine chart. Errors with $3\epsilon_{j+1}\le\epsilon_j$ and shifts $2\epsilon_j$ make a decreasing sequence.

For a compact hull point $z$ and relatively compact analytic neighborhood $V$ disjoint from the original compact set, finitely many separating polynomials exclude the compact bad boundary set $\partial V\cap\{|f|\ge e^t\}$ while containing the hull. Add generator bounds to get a compact polytope $P$. Its rational AFS function $u$ vanishes on $P$ and is positive on the bad boundary. A positive integer $C$ gives $Cu>\log|f|-t$ on the whole boundary, hence on a whole winning collar. The function $Cu$ outside $V$ and $\max(Cu,\log|f|-t)$ inside is a continuous rational contact compact perturbation. At zeros the finite branch wins. A uniform AFS approximant of error below a third of its positive value at $z$ contradicts hull membership. This reconstructs the continuous arbitrary-neighborhood Rossi step, with actual compact-perturbation membership first.

There is also a direct pole-order localization input. If $R$ is integral nonnormal, $a\log|h|+b\le\max(u,-c\log|f|)+O(1)$, $h\in R_f$, and $u$ is AFS, divisorial rays on the finite normalization force $a\max(-\operatorname{ord}_Dh,0)\le c\operatorname{ord}_Df$. For $q/p>c/a$, $z=h^pf^q$ is integral over $R$ and lies in $R_f$. One $f^N$ kills $R[z]/R$, so $z^lf^N\in R$ for every $l$. At an original $R$-hull point $x$, with $|\log|f||\le M$ on it and the compact set $L_0$, these actual regular hull tests give
$$a\log|h(x)|+b\le\sup_{L_0}(a\log|h|+b)+2cM,$$
after $l\to\infty$ and $q/p\downarrow c/a$, including zero endpoints. The denominator-counting shortcut fails for $f=z^2,h=z^{-1},a=2,c=1$. Controlled approximants above are a necessary separate input when using this for regularizable limits.

The **complete original target remains unresolved in this deliverable**, for the following concrete reasons. These are missing reconstructions, not proofs that the corresponding source conclusions are false.

1. The new smooth weak and trace theorems do not prove Wu 6.15's full weak split-piece maximum principle. That proof requires a global proper witness for the analytic pieces, uniform support and winning-collar control after its strict supporting perturbation, and an integer trace constant on the whole compact set relevant to the hull argument. Integer-valued continuity gives only local constancy. A shrink around the tested point must preserve every subsequent hull/support inclusion; this has not been proved here. When $\gamma=1$ the other piece's positive-weight sum is zero, and the estimate must be rewritten without division by $\gamma-1$. Merely noting these repairs does not supply the full application.
An explicit diagnostic shows why the integer-trace shrink needs proof. For $z\mapsto a=z^2$ over trivial $k$, take the base open to be disjoint disks of radius $\rho<1$ about $a=0$ and $a=1$. A source piece can contain the whole preimage of the first disk and only the disk about $z=1$ over the second; its complementary piece contains the disk about $z=-1$. The locally constant test equal to one on the first piece and zero on the second has trace two over the first base disk and one over the second. At the branch center the fiber has Artinian length two; over the unit disk the binomial root expansions give the two disjoint simple disks. Thus continuity supplies no single integer on this disconnected open. This example does not disprove the desired local maximum principle; it disproves the unrestricted constancy inference. A local shrink must also be shown compatible with the hull used later.

2. The countable strict supporting barrier and all controlled algebraic-localization applications in 6.7--6.9 have not been fully reconstructed here together with that split-piece proof. Real support branches need actual decreasing AFS formulas at zero coordinates, not rational slope substitution. A Hartogs radius formula from polynomial coefficients on an **already Runge** domain does not prove the weak Hartogs domain Runge. Its later use requires nested strict polynomial opens, common approximation neighborhoods, and global upper-growth collar control; the printed identity between the interior of a weak polytope and strict constraints fails for constant constraints. The finite-projection geometry in 6.16 and every step of the singular-stratum induction 6.3--6.5 still require a complete repaired proof. We have not asserted these by citation to the diagnostic source.
3. Wu 7.1, actual LF2716--2717, explicitly invokes weak/global 6.5 after descending a smooth-resolution envelope. Consequently the countable rational singular EP base has not been established here. Neither the genuine singular operator, the continuous rational bridge, the smooth weak theorem, nor the new open trace establishes this antecedent.
4. Arbitrary-cardinality and real-class envelope passage, onto normalization, unbounded envelope-energy differentiation and variational attainment for the original singular domain consequently remain conditional. Finite algebraic data can descend to countable algebraically closed subfields, but relative integral closure must preserve the nonnormal generic fiber, vertical DVRs, depths, components and multiplicities. Mixed pushforward and genuine contact orthogonality must be obtained before global domination compares competitors. None supplies the missing countable base. Rational classes approaching a real ample class from above give EP by BJ 5.9 only after the rational EP base has been proved.

For normalization $q:X^\nu\to X$ in the geometrically unibranch domain, singleton geometric fibers and characteristic-zero purely inseparable residue extensions imply unchanged residue fields and a universal homeomorphism. Norms then give a bijective analytic map; properness on compact Hausdorff spaces makes it a homeomorphism. Unconditionally, genuine pullback, model projection formula and decreasing pairings give equal volume and energy and
$$q_*\bigwedge_i(q^*\omega_i+dd^cq^*\phi_i)
 =\bigwedge_i(\omega_i+dd^c\phi_i). \tag{23}$$
Onto PSH is separate: BJ 5.13 requires larger target classes with EP. Only then do onto $\mathcal E^1$ and equality of dual-energy target sets follow. The smooth-target application in (18) cannot be repeated on the singular target without this antecedent.

The known nodal obstruction illustrates the distinction: on a rational nodal curve, a degree-$d$ nef blowup model on its normalization has raw measure $d\delta_{\operatorname{ord}_{p_1}}$ and unequal values $0,d$ at the two node preimages. A downstairs solution would pull back with that target by (23) and mass/positivity, and uniqueness upstairs would force that model plus a constant, contradicting equal values of a downstairs pullback. This is outside the requested unibranch domain and does not refute it.

# Evidence, artifacts and rerun

The full input values and bytes are retained in `input.json`, byte-identical `input-original.json`, `assignment-original.txt`, and `task-original.json`. `source-extracts/source-provenance.json` retains the ten exact versions, hashes, literal statements and pertinent proof bodies, inclusive one-based LF ranges defined by UTF-8 `split('\n')`, applications and concrete limits. Its excerpts do not claim a whole-source audit. Local copies of the authorized primary files are in `sources/`.

The complete partial argument is this `P16.1-argument.md`; the standalone rendering is `P16.1-paper.tex`. `status.json` has exactly `id`, `status`, `exact_result`, `proof_file`, `concrete_gaps`, and records partial. `mathematical-audit.json` separates primary-source consequences, independent proof drafts, conditional statements and gaps. `notes.json` contains at most four canonical notes with earlier-local-ID support only.

Run `python3 rerun.py` in this workspace. Existing Pandoc writes standalone TeX, and existing pdfLaTeX runs twice. Exact commands, stdout/stderr, separate TeX logs, return codes and hashes are retained. `algebra-checks.json` checks finite rational partition/shift/scalar identities and the two-sheet determinant example; it does not test the infinite analytic results. `environment.json` retains paths and environment details. No heavy computation was needed, no software was installed, and no other campaign, root file, worker, subagent, private record, account/auth/runtime modification, external message or external write was used. The requested model configuration was neither inspected nor changed.

Hashes, preservation and compilation are observations, not proofs of mathematics or novelty. The singular-envelope and original arbitrary-support existence obligations remain indispensable and unresolved. Candidate=false.

# References

BJ: Boucksom--Jonsson, *Global pluripotential theory over a trivially valued field*, arXiv:1801.08229v4.

Wu: Lyuhui Wu, *On the local theory of non-archimedean psh functions*, arXiv:2609.27610v1.

CLD: Chambert-Loir--Ducros, *Formes differentielles reelles et courants sur les espaces de Berkovich*, arXiv:1204.6277v2.

GM: Gubler--Martin, *On Zhang's semipositive metrics*, arXiv:1608.08030v3.

Wanner: *Comparison of two notions of subharmonicity on non-Archimedean curves*, arXiv:1801.04713v3.

Thuillier: *Theorie du potentiel sur les courbes en geometrie analytique non archimedienne*, tel-00010990v1.

BE: Boucksom--Eriksson, *Spaces of norms, determinant of cohomology and Fekete points in non-Archimedean geometry*, arXiv:1805.01016v3.

GR: Gubler--Rabinoff, *On semipositive piecewise linear functions in non-archimedean analytic geometry*, arXiv:2503.05513v1.

Ducros: *Espaces de Berkovich, polytopes, squelettes et theorie des modeles*, Confluentes Mathematici 4(4), 1250007, DOI10.1142/S1793744212500077.

GJR: Gubler--Jell--Rabinoff, *Forms on Berkovich spaces based on harmonic tropicalizations*. Source version: arXiv:2111.05741v3.



