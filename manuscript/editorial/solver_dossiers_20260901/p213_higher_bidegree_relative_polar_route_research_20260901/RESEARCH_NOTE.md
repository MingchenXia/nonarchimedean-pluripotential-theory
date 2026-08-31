# Higher-bidegree multiplier independence: relative polar removal and its exact limits

Date: 1 September 2026. Investigator: /root/p082_independent_reaudit.
Status: UNVERIFIED RESEARCH CANDIDATE. Complete bounded arguments are recorded for independent review, not as production acceptance or a solution of P21.3. No live manuscript, frozen predecessor, git state, or production endpoint is changed.

## 1. Outcome and scope

The current Chapter 72 asks, on every ordinary open W of a good separated strict boundaryless pure n-dimensional analytic space, whether
\[
 u,v\in\operatorname{CPsh}(W),\qquad
 \mathrm d'\mathrm d''(u\delta_X)=\mathrm d'\mathrm d''(v\delta_X)
 \quad\Longrightarrow\quad
 \mathrm d'\mathrm d''(uT)=\mathrm d'\mathrm d''(vT)
 \tag{1.1}
\]
for every positive separately closed current T of bidegree (p,p), including \(1\le p\le n-1\). CPsh is the FULL least uniform-closed ordinary sheaf, not only its first smooth-approximation stage. Write \(\mathrm{dd}=\mathrm d'\mathrm d''\) and \(h=u-v\). All current products with continuous coefficients use the coefficient Radon measures of ordinary CLD currents.

This note obtains three bounded conclusions.

1. A relative one-factor polar estimate for an arbitrary positive closed T. If a locally approachable pole V is integrable against the local coefficient measures of T, then it is integrable against those of \(\mathrm{dd}(uT)\) for every full-CPsh u. Consequently (1.1) holds if h is ordinary smooth off a locally polar closed set Z for which such a T-integrable pole exists. No smoothness of T or representation R is assumed.
2. A primary-calculus proof that currents of given analytic effective-Cartier flags satisfy the continuous-pair predicate. This excludes coordinate analytic subspaces and effective Cartier divisors as a source of counterexamples. It does not factor an arbitrary current supported on a subspace through that subspace.
3. Two sharp warnings: an abstract higher-dimensional fan defeats a deduction based only on trace/energy domination; an ACTUAL analytic positive closed current on \((\mathbf P^1_K)^2\) shows that zero T-mass on a divisor does not imply logarithmic integrability there. The latter current is nevertheless Bedford--Taylor.

No theorem here places the nonsmooth locus of every h in (1.1) in such a polar set. No theorem here gives logarithmic integrability for every T. These are genuine remaining hypotheses, not disguised consequences of connectedness, a moment refinement, or zero canonical Hessian.

The frozen rank-drop diagnostic, conditional four-family transport, and cohomology diagnosis were read before beginning. None is imported as a theorem about higher bidegrees. In particular there is no scalar coefficient-propagation proof, no arbitrary-current pullback, no slicing, and no weakly-smooth replacement of the ordinary test sheaf. The preceding weighted-polar packet suggested the energy mechanism; the relative one-factor proof below is written out with an arbitrary base current and does not take that packet's new theorem as a premise. This is related follow-on authorship, not an independent audit of that packet.

## 2. The precise relative-pole hypothesis

For a positive current T of bidegree (p,p), put \(d=n-p\). A locally upper-bounded extended-real function V is **T-trace integrable** on an ordinary open if, for every compactly supported ordinary smooth (d,d)-form alpha, V is integrable against the total variation of the coefficient measure \(T\wedge\alpha\). Locally it suffices to verify this for positive smooth majorants of a finite test presentation. No universal global trace measure is postulated.

We shall use a locally approachable psh V: on a neighborhood of each point it is the decreasing limit of smooth psh functions \(V_j\) defined on that same neighborhood. The value minus infinity is allowed. A finite local constant can be subtracted so that \(V_j<0\) near any one fixed compact set.

The relative conclusion is
\[
 V\in L^1_{\mathrm{loc}}(T\wedge\alpha)\ \hbox{for all test traces}
 \quad\Longrightarrow\quad
 V\in L^1_{\mathrm{loc}}\bigl(\mathrm{dd}(uT)\wedge\beta\bigr)
 \tag{2.1}
\]
for every \(u\in\operatorname{CPsh}\) and every ordinary smooth (d-1,d-1)-form beta, using total variations. The geometric local hypothesis for the proof is the availability of smooth psh barriers rho with
\[
 \rho(x)<0,\qquad K_\delta=\{\rho\le\delta\}\Subset Y
 \quad(\delta>0)
 \tag{2.2}
\]
on arbitrarily small ordinary neighborhoods Y. Section 6 gives the original-field analytic construction. No properness of X is needed.

The assumption in (2.1) is stronger than \(T\wedge\alpha\) giving zero mass to \(\{V=-\infty\}\). Section 10 proves that the difference is real even for a positive closed analytic current.

## 3. Energy with an arbitrary fixed base current

The only primary analytic-calculus inputs here are CLD 8.1.7--8.1.8, 8.5.1, 8.5.5 and ordinary smooth product identities. They do not assume T is Bedford--Taylor.

For any positive closed S and local dpsh functions \(a,b\), define
\[
 \Gamma_S(a,b)
 =\tfrac12\{\mathrm{dd}(abS)-a\,\mathrm{dd}(bS)-b\,\mathrm{dd}(aS)\},
 \qquad
 \Gamma_S(a)=\tfrac12\mathrm{dd}(a^2S)-a\,\mathrm{dd}(aS).
 \tag{3.1}
\]
These are well-defined differences of positive order-zero currents. Here are the closure details needed for full CPsh.

Addition and smooth convex nondecreasing composition preserve CPsh by its minimal-subsheaf definition: the good class contains smooth psh functions and is stable under uniform limits. After adding a common sufficiently large constant to a local representation \(a=u-v\), write \(a=f-g\) with f,g positive CPsh. Squares of positive CPsh functions are CPsh, by extending the square on their positive range to a smooth convex nondecreasing function. Thus
\[
 a^2=2f^2+2g^2-(f+g)^2,\qquad
 ab=\tfrac12\{(a+b)^2-a^2-b^2\}
 \tag{3.2}
\]
are dpsh. CLD 8.5.5 gives order zero for their curvatures against S.

If the finitely many CPsh functions in these decompositions converge locally uniformly, (3.1) converges as currents, including after multiplication by any locally uniformly converging continuous coefficient. Indeed each curvature in (3.2) is a fixed finite linear combination of positive converging currents. Their masses against compact positive test majorants are uniformly bounded. CLD 8.5.1 applies separately to each positive summand. This does not multiply an uncontrolled signed weak limit by a varying coefficient.

For smooth a,b, the product rule gives
\[
 \Gamma_S(a,b)
 =\tfrac12(\mathrm d'a\wedge\mathrm d''b+
                 \mathrm d'b\wedge\mathrm d''a)\wedge S.
 \tag{3.3}
\]
In particular \(\Gamma_S(a)\ge0\). To obtain positivity for all dpsh a, first fix smooth psh v and use CPsh minimality in u for \(\Gamma_S(u-v)\); then fix arbitrary CPsh u and use minimality in v. The continuity just proved supplies both uniform-closure steps. Hence
\[
                              \Gamma_S(a)\ge0.
 \tag{3.4}
\]
No simultaneous first-stage smooth approximation of u and v is used.

For \(z=\mathrm e^{Bu}\), \(u\in\operatorname{CPsh}\), \(B>0\), the same minimal-subsheaf argument extends the smooth chain identities to
\[
 \mathrm{dd}(zS)
 =Bz\,\mathrm{dd}(uS)+B^2z\,\Gamma_S(u)
 =Bz\,\mathrm{dd}(uS)+z^{-1}\Gamma_S(z).
 \tag{3.5}
\]
All terms pass under uniform closure for the explicit positive-current reasons above.

We will need only a positive closed Q of bidegree (n-1,n-1), so its energies are measures. Bilinearity and (3.4) show
\[
 \Gamma_Q(a)+2t\Gamma_Q(a,b)+t^2\Gamma_Q(b)\ge0
 \quad(t\in\mathbf R).
 \tag{3.6}
\]
Take a measure dominating the variations of these three measures. For rational t, their Radon--Nikodym densities satisfy the indicated quadratic inequality outside one null set; countability and continuity in t give \(B^2\le AC\). This proves the weighted measure Schwarz and Young inequalities.

For smooth rho and any dpsh z, symmetry and the smooth product rule first give, and CPsh uniform closure then preserves,
\[
 \mathrm d'(zQ)\wedge\mathrm d''\rho=\Gamma_Q(z,\rho).
 \tag{3.7}
\]
This is an equality of top-degree distributions, with its right side a signed Radon measure. It does not claim \(\mathrm d'z\) is an ordinary smooth form.

## 4. A compact one-factor weighted bound

Fix Q as above, a barrier rho satisfying (2.2), \(U=\{\rho<0\}\), and an integer \(a\ge4\). Put
\[
 r=\max(-\rho,0),\quad l=a+1,\quad
 \theta=\mathrm{dd}\rho,\quad
 \eta=\mathrm d'\rho\wedge\mathrm d''\rho,\quad
 \beta=r^a\theta+a r^{a-1}\eta.
 \tag{4.1}
\]
The form beta is a compactly supported positive (1,1)-form with continuous (indeed \(C^2\)) chart coefficients. The scalar \(r^l\) also has compact \(C^2\) coefficients. Let V be smooth psh near \(K_\delta\), negative on U, and let u be full CPsh near \(K_\delta\). Then
\[
 \int (-V)r^{a+1}\,\mathrm{dd}(uQ)
 \le 2\mathrm e(a+1)\|u\|_U
                       \int (-V)\beta\wedge Q .
 \tag{4.2}
\]
This particular estimate is a research deduction, not a quotation of CLD 8.4.3. In particular the scalar endpoint has factor one in its derivative.

First justify compact \(C^2\) integration by parts. Convolve \(t\mapsto\max(-t,0)^b\) in one real variable. Its coefficients and first two derivatives converge uniformly on bounded intervals for every exponent used here. After composition with rho all sufficiently small convolutions have support in the ONE compact \(K_\delta\). Finite ordinary chart covers and positive test majorants justify the pairings and their limits. Derivatives are transferred to these \(C^2\) tests before taking limits. Nothing is extended by zero across a singular set with an unjustified differential-commutation claim.

For a positive CPsh z bounded above and away from zero near \(K_\delta\), let
\(J(z)=\int(-V)r^l\mathrm{dd}(zQ)\).
Ordinary product expansion, Stokes, symmetry and (3.7) yield
\[
 \begin{split}
 J(z)
 &=\int z\{V\,\mathrm{dd}(r^l)-r^l\mathrm{dd}V\}\wedge Q
       +2\int V\,\mathrm d'(zQ)\wedge\mathrm d''(r^l)\\
 &\le \int (-V)z[-\mathrm{dd}(r^l)]\wedge Q
          +2l\int(-V)r^{l-1}\Gamma_Q(z,\rho).
 \end{split}                                                   \tag{4.3}
\]
The sign follows, for example, by applying Stokes to
\(\mathrm d'(zV\,\mathrm d''(r^l)\wedge Q)\); the term involving
\(-z r^l\mathrm{dd}V\wedge Q\) is nonpositive. This calculation first holds for smooth z and also directly distributionally; (3.7) and the compact \(C^2\) limit justify it for general CPsh z.

Weighted Young applied to (3.6) gives
\[
 2l r^{l-1}\Gamma_Q(z,\rho)
 \le r^l z^{-1}\Gamma_Q(z)
            +l^2 z r^{l-2}\Gamma_Q(\rho).
 \tag{4.4}
\]
Both weights vanish harmlessly at \(r=0\), and \(z^{-1}\) is bounded. Since
\[
 \mathrm{dd}(r^l)
     =-l r^{l-1}\theta+l(l-1)r^{l-2}\eta,\qquad
 \Gamma_Q(\rho)=\eta\wedge Q,
\]
one has the positive-form bound
\[
 -\mathrm{dd}(r^l)+l^2r^{l-2}\eta
 =l r^{l-1}\theta+l r^{l-2}\eta
 \le l\beta .                                                \tag{4.5}
\]
Consequently, with \(J_0=\int(-V)\beta\wedge Q\),
\[
 J(z)\le l\|z\|_U J_0+
              \int(-V)r^l z^{-1}\Gamma_Q(z).                 \tag{4.6}
\]

Put \(M=\|u\|_U>0\), \(z=\mathrm e^{Bu}\). Formula (3.5), positivity and
\(u\ge-M\) on U imply
\[
 \mathrm{dd}(zQ)
 \ge B\mathrm e^{-BM}\mathrm{dd}(uQ)+z^{-1}\Gamma_Q(z).
\]
Multiplication by \((-V)r^l\) cancels exactly the last term of (4.6).
Thus
\[
 \int(-V)r^l\mathrm{dd}(uQ)
       \le l B^{-1}\mathrm e^{2BM}J_0 .
\]
Choose \(B=(2M)^{-1}\) to obtain (4.2). If M=0, u vanishes on U and the weight vanishes on its complement, so the left side is zero by locality and order zero. All smooth-V and \(C^2\) passages precede any polar limit.

## 5. Relative polar propagation and defect removal

Take a locally approachable psh V that is Q-trace integrable. Near the compact barrier set, write \(V_j\downarrow V\) with smooth psh \(V_j\), all on the same neighborhood, and subtract one constant so that \(V_j<0\) there. The right side of (4.2) is bounded uniformly in j by
\[
       2\mathrm e(a+1)\|u\|_U\int(-V)\beta\wedge Q<\infty .
\]
The final finiteness follows from the assumed trace integrability and compact coefficient majorants for beta. Monotone convergence on the LEFT gives local V-integrability for the positive measure \(\mathrm{dd}(uQ)\), since \(r^{a+1}\) is bounded below on each compact subset of U. In particular it gives zero mass to \(\{V=-\infty\}\).

Now let T have any bidegree (p,p), \(p\le n-1\). On a small ordinary presentation of a symmetric (d-1,d-1)-test beta, choose a smooth psh quadratic potential b in its moment coordinates. On the relevant compact tropical image ordinary linear algebra gives
\[
                 -C(\mathrm{dd}b)^{d-1}
                    \le\beta\le C(\mathrm{dd}b)^{d-1}.
 \tag{5.1}
\]
For d=1 this is just a bound on a scalar. The inequality is checked in the affine ambient coordinate space and pulled back as a FORM; it does not require full rank at each analytic point. Put
\[
                    Q=T\wedge(\mathrm{dd}b)^{d-1}.
\]
This is positive closed. T-trace integrability of V implies the required Q-trace integrability. The ordinary smooth closed product rule gives
\(\mathrm{dd}(uQ)=(\mathrm{dd}b)^{d-1}\wedge\mathrm{dd}(uT)\).
The preceding argument and (5.1) prove (2.1), including total variations. Local source cutoffs and a finite ordinary partition on a compact support complete the assertion for arbitrary tests.

Here is the promised sufficient condition for (1.1). Let Z be closed in W. Assume locally along Z that there is such a T-trace-integrable approachable pole V with
\(Z\subseteq\{V=-\infty\}\), and assume h is ordinary smooth on \(W\setminus Z\). The canonical equality in (1.1) and CLD 7.3.10/8.3.1 imply
\(\mathrm{dd}h=0\) as a smooth form on \(W\setminus Z\). Hence
\[
 D_T=\mathrm{dd}(uT)-\mathrm{dd}(vT)
\]
vanishes there, by the product rule. Each of its coefficient measures is supported on Z. But (2.1) shows that both positive curvature currents, hence the total variations of their difference, give zero mass to Z. Thus \(D_T=0\) on W.

This conclusion allows h to be nonsmooth ON Z. It neither requires nor proves that h and -h belong to CPsh on all of W. It also does not infer the conclusion from T having zero mass on Z.

More generally the same proof works if the target identity is already known off Z by some independently established local theorem, rather than by smoothness of h. The only additional work at Z is the relative polar estimate just proved.

## 6. Original-field barriers and actual logarithmic poles

For the Chapter 72 analytic class, (2.2) can be obtained inside a prescribed ordinary neighborhood. Choose an affinoid neighborhood A and then a rational affinoid neighborhood
\[
       B=\{|f_i|\le\lambda_i|g|,\ 1\le i\le s\}
                       \subset\operatorname{Int}(A).
\]
The functions \(g,f_1,\ldots,f_s\) have no common zero. For some \(\mu>1\), the enlargement \(B_\mu\) is still in \(\operatorname{Int}(A)\): otherwise compactness and the nested limit \(B_\mu\downarrow B\) would meet the closed complement there. Every \(B_\mu\) avoids g=0.

On \(Y=\operatorname{Int}(A)\cap\{g\ne0\}\), set
\(a_i=\log(|f_i/g|/\lambda_i)\), \(a_0=-1\).
Let \(t=\log\mu\), choose \(0<\epsilon<t/8\), and take a smooth convex coordinatewise increasing regularized maximum \(M_\epsilon\), within epsilon above the maximum and ignoring a coordinate more than \(2\epsilon\) below it. It is obtained by convolving the maximum with an even compact product probability kernel. Then
\[
             \rho=M_\epsilon(a_0,a_1,\ldots,a_s)-t/2
\]
is ordinary smooth psh. At a zero of any \(f_i\) that coordinate is ignored on an actual ordinary neighborhood; the constant branch covers simultaneous zeros. At the chosen point \(\rho<0\), while
\(\{\rho\le t/4\}\subset B_{\exp(3t/4)}\Subset Y\).
This proves (2.2) without base change, a polycylinder-basis assertion, or a G-open substitution.

For any analytic f, the pole \(\log|f|\) is locally approachable in an explicit way. Convolve \(\max(s,0)\) with an even smooth probability kernel supported in [-1,1], obtaining F with
\(0\le F'\le1\), \(F(s)=0\) for \(s\le-1\) and \(F(s)=s\) for \(s\ge1\).
Put
\[
                  F_m(s)=-m+F(s+m).
 \tag{6.1}
\]
Then \(F_m(\log|f|)\), extended as -m at f=0, is ordinary smooth psh: it is locally constant near every zero and a convex function of a log-unit elsewhere. It decreases to \(\log|f|\). However, for an ARBITRARY T its trace integrability is still an extra hypothesis. The canonical top-form support argument does not replace it for lower-degree traces.

## 7. Given analytic flags are not counterexamples

The following is a source-calculus deduction, not a new claimed primary theorem. On an ordinary open U suppose analytic functions \(f_1,\ldots,f_r\) define a flag
\[
 Z_0=U,\quad Z_j=V(f_1,\ldots,f_j),\quad 1\le j\le r,
 \tag{7.1}
\]
where every \(Z_j\) is pure of dimension \(n-j\), boundaryless, and each \(f_j|_{Z_{j-1}}\) is a regular analytic function (a non-zero-divisor). The closed inclusions are proper on compact supports. Multiplicities are the actual fundamental-cycle multiplicities. Then the pushed-forward current \(\delta_{Z_r}\) has continuous-pair Bedford--Taylor independence with respect to the ambient canonical curvature on U.

Proof by induction: \(\delta_U\) has the property tautologically. If S has it, so does \(\alpha\wedge S\) for a smooth positive closed form alpha, by the ordinary product rule. The class of positive closed currents with the continuous-pair property is stable under weak limits: for fixed continuous u,v, multiplication converges by CLD 8.5.1 and differentiation is continuous. These proofs are precisely the continuous scope of CLD 8.6.5--8.6.6.

The same class is stable under \(S\mapsto\mathrm{dd}(aS)\) for \(a\in\operatorname{CPsh}\): for a fixed S, the good a form a sheaf containing smooth psh functions and closed under uniform limits, using positivity and the preceding weak-limit argument. Hence CPsh minimality applies. This is CLD 8.6.8 with its closure proof retained; no Corollary 8.6.7 or 8.11.3 is used.

Assume therefore \(S=\delta_{Z_{j-1}}\) has the property. Apply this last operation with the AMBIENT smooth psh functions \(F_m(\log|f_j|)\) from (6.1). On \(Z_{j-1}\),
\[
 \mathrm{dd}\bigl(F_m(\log|f_j|)\delta_{Z_{j-1}}\bigr)
          \longrightarrow \delta_{Z_j}.                  \tag{7.2}
\]
To verify the convergence, test first the function currents on a compact top-degree smooth form of \(Z_{j-1}\). Its SUPPORT is disjoint from \(Z_j\), by CLD 15.2.1(b), since the latter has smaller intrinsic analytic dimension. The logarithm is bounded there, so (6.1) agrees EXACTLY with \(\log|f_j|\) there for every sufficiently large m. Differentiation and Poincare--Lelong, CLD 16.7.3 on \(Z_{j-1}\), give (7.2). Smooth tests and functions are pulled back by the closed immersion; arbitrary currents are never pulled back. Compactness is retained by that immersion. Weak closure proves the induction step.

This proves the flag assertion, including nonreduced multiplicities when the stated regular/purity hypotheses hold. In particular it covers effective Cartier divisors and coordinate flags in smooth polydomains or products of projective lines. It does NOT assert that every analytic cycle has a flag (7.1), nor that a positive current supported on an analytic subset must be a scalar integration current.

There is a useful restriction consequence when the smooth restriction sheaf along a given Z is locally generated by restrictions of ambient ordinary forms, as holds for the analytic closed immersions under consideration. Ambient curvature equality implies
\[
        \mathrm{dd}((u|_Z)\delta_Z)
             =\mathrm{dd}((v|_Z)\delta_Z)
 \tag{7.3}
\]
intrinsically. Indeed the flag result gives zero after pushforward; compact intrinsic smooth forms lift LOCALLY because analytic units on Z lift locally to ambient units, followed by an ordinary source cutoff. A finite partition lifts any compact test. This argument is about ordinary forms, not a pullback of the zero current. Alternatively retain only the ambient pushed-forward equality, which is already enough for the claimed flag-current predicate.

## 8. What positive approximation does and does not prove

If \(T_\nu\) are positive closed currents satisfying the continuous-pair predicate and \(T_\nu\to T\) weakly, then T satisfies it. For sequences this is the source result used above. The proof also works for nets: approximate a fixed continuous multiplier locally uniformly by smooth functions and use one compact positive test majorant; convergent positive currents have eventually bounded mass on that majorant. No metrizability or diagonal choice is needed.

Thus any locally weakly approximable positive closed cone generated by smooth positive closed forms, flag-cycle currents, and their CPsh curvature products is a sufficient class. This does not prove that every T lies in that cone. Ordinary current regularization cannot be replaced by approximation of a coarse tropical pushforward, nor by an unproved lifting of the approximation from a fiber. The conclusion is a genuine exclusion of those explicit counterexample classes, but the full density assertion remains unproved here.

## 9. A higher-bidegree obstruction to trace/energy-only reasoning

This is an ABSTRACT tropical diagnostic, not an analytic P21.3 counterexample. It refines the existing cross-fan warning specifically for the proposed energy route.

Let \(\Sigma\subset\mathbf R^2\) be the four coordinate rays with unit canonical weights, and let
\[
 \mathcal X=\Sigma\times\mathbf R^{n-1},\quad
 u=2|x_1|,\quad v=|x_1|+|x_2|,\quad h=|x_1|-|x_2|.
 \tag{9.1}
\]
Use the ordinary ambient superform sheaf on this calibrated product. The functions u,v are full CPsh: restrictions of
\(2\sqrt{x_1^2+\epsilon}\) and
\(\sqrt{x_1^2+\epsilon}+\sqrt{x_2^2+\epsilon}\) converge locally uniformly and are smooth convex.

Let \(D\) be the canonical integration current on the product, and \(D_w\) the current with horizontal-ray weights 2 and vertical-ray weights 1. Both are positive closed: the opposite rays balance separately, and the Euclidean product has no boundary. Thus \(0\le D_w\le2D\). If
\(\omega=\sum_{j=1}^{n-1}\mathrm d'y_j\wedge\mathrm d''y_j\), put for any \(1\le p\le n-1\)
\[
                 S=\omega^p\wedge D,\qquad
                 T=\omega^p\wedge D_w.
 \tag{9.2}
\]
They are positive closed of bidegree (p,p), with \(0\le T\le2S\). The ray-slope sums give
\[
 \mathrm{dd}(uD)=\mathrm{dd}(vD)
                =4\,\delta_{\{0\}}\boxtimes[\mathbf R^{n-1}],
 \qquad
 \mathrm{dd}(hT)
       =2\,\omega^p\wedge
                   (\delta_{\{0\}}\boxtimes[\mathbf R^{n-1}])\ne0 .
 \tag{9.3}
\]
The last nonzero assertion can be tested against a nonnegative compact form in the remaining Euclidean directions and a scalar equal to one near the vertex. It is true also at p=n-1, where the result is a top-degree measure.

Linearity in the base current and positivity of Gamma give, for EVERY dpsh a,
\[
                      0\le\Gamma_T(a)\le2\Gamma_S(a).
 \tag{9.4}
\]
Hence even CURRENT domination, which is stronger than an inequality for one trace, plus energy domination does not imply transfer of the canonical zero-Hessian kernel.

This example identifies two invalid shortcuts precisely. First,
\(\mathrm{dd}(hD)=0\) does not mean \(\Gamma_D(h)=0\): on each ray its density is the square of slope, equal to one. Already a nonconstant affine function on an ordinary interval has zero Hessian and nonzero energy. Second, the coefficient measures of T and \(\Gamma_T(h)\) do not charge the vertex wall
\(Z=\{0\}\times\mathbf R^{n-1}\): they are ray-length densities times Euclidean forms. Nevertheless the curvature defect (9.3) is supported exactly on Z. Nullity of the ORIGINAL trace or the energy trace at an interface is therefore not curvature nullity.

The existing analytic four-punctured realization does not supply the canonical equality in (9.3) upstairs. This note does not import it to do so. Nor is Z asserted to be an analytic polar subset in an analytic realization. In particular this diagnostic does not contradict Sections 4--5, whose APPROACHABLE POLE and integrability hypotheses contain extra analytic information.

## 10. Actual analytic zero-mass is weaker than log integrability

Let K be complete and nontrivially valued; choose \(0<|\pi|<1\) and
\(\ell=-\log|\pi|\). Work over this ORIGINAL field on
\[
 X=\mathbf P^1_{t,K}\times_K\mathbf P^1_{z,K},\qquad
 a_j=\pi^{j^2},\quad Y_j=\{t=a_j\},\quad Y_0=\{t=0\}.
\]
Each fiber is an actual closed analytic copy of \(\mathbf P^1_K\), not a set-theoretic product assertion. Define
\[
                              T=\sum_{j\ge1}j^{-2}\delta_{Y_j}.
 \tag{10.1}
\]
This is a well-defined positive closed (1,1)-current, although the supports are not a locally finite analytic cycle. Here is the needed boundedness proof.

For any compact ordinary smooth (1,1)-test beta on X, its top-degree derivative \(\mathrm{dd}\beta\) has support disjoint from \(Y_0\), by CLD 15.2.1(b). The function \(1/t\) is bounded on that compact support, so for all sufficiently large j,
\[
                      \log|1-a_j/t|=0
           \quad\hbox{on }\operatorname{supp}(\mathrm{dd}\beta).
\]
Poincare--Lelong applied to the regular meromorphic function
\((t-a_j)/t\) therefore gives
\[
                  \langle\delta_{Y_j},\beta\rangle
                       =\langle\delta_{Y_0},\beta\rangle
                  \quad\hbox{for all sufficiently large j}.       \tag{10.2}
\]
The finitely many earlier values are bounded as well. Thus (10.1) converges absolutely on every test and defines a symmetric positive linear functional on the ordinary test space. CLD 7.2.9 makes this functional an order-zero continuous current; no uniform-in-test version of (10.2) is needed. The partial sums converge weakly to it. Closedness passes distributionally. Each partial sum is Bedford--Taylor by the Cartier case of Section 7, so T has that property by Section 8.

On the ordinary domain \(|t|<1\), take \(V=\log|t|\). Choose a nonnegative compact smooth (1,1)-form omega on an annulus of \(\mathbf P^1_z\), with integral one. Choose a nonnegative ordinary smooth function chi in the t-variable, equal to one near 0 and with compact support in \(|t|<1\); it is obtained by a smooth cutoff of \(\log|t|\), constant near 0. Then
\(\alpha=\chi(t)\operatorname{pr}_z^*\omega\) is a positive compact (1,1)-test on the ACTUAL analytic product. For all sufficiently large j, \(\chi(a_j)=1\), and
\[
 \int(-V)\,T\wedge\alpha
 \ge\sum_{j\gg1}j^{-2}\,j^2\ell\int_{Y_j}\operatorname{pr}_z^*\omega
 =\infty .                                                     \tag{10.3}
\]
On the other hand \(T\wedge\alpha\) gives zero mass to \(Y_0\), as do all its coefficient traces: the measure is the countable sum of the finite measures on the disjoint fibers \(Y_j\), none of which meets \(Y_0\). Countable additivity, not a weak-limit assertion about null sets, proves this.

Thus even on a smooth proper algebraic surface a positive closed T can be null on an analytic divisor and yet fail its logarithmic-integrability test. This T is NOT a counterexample to (1.1); its explicit approximation proves the opposite. Relative polar removal is sufficient, not necessary.

## 11. Exactly what remains to reach arbitrary T

The new estimate supplies a usable conditional bridge, not a solution. A possible application must establish BOTH:

- the target identity off a specified closed Z (for example, ordinary smooth zero-Hessian regularity of h there);
- a local approachable pole for Z that is integrable for the actual T-traces, or some different proof that both \(\mathrm{dd}(uT)\) and \(\mathrm{dd}(vT)\) give zero mass to Z.

Neither follows from canonical curvature equality alone in this note. The analytic family (10.1) prevents replacing the second requirement by the weaker zero-T-mass assertion. The abstract example (9.1)--(9.4) prevents replacing it by bare trace/energy domination or by canonical zero-energy, which is false even for affine h.

Analytic flag currents can instead be handled by direct positive approximation, even when they charge the proposed pole. This suggests keeping the two mechanisms separate: positive-approximation closure for concentrated pieces, and relative polar removal for a remainder whose logarithmic integrability is independently known. A decomposition theorem giving those pieces for EVERY positive closed current would be new input. None is claimed here, and no nonexistent current restriction/slice is used to manufacture such a decomposition.

All tests are ordinary and compact in their actual domains. No inference uses equality on just one tropical chart, target overlap, an all-moment source coefficient assertion, or unproved density of smooth positive currents. There is no general counterexample, no retirement of P21.3, and no production-verification claim.
