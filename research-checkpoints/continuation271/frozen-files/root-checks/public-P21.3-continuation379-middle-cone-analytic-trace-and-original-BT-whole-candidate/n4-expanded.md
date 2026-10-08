# Analytic-trace removability, the whole372 verdict, and the original decision

The independently reconstructed partial theorem is as follows. Work in the original ambient category of n1. Let \(Z\subset W\) be ordinary closed and locally Zariski closed in analytic domains. Suppose \(h\in C(W,\mathbb R)\) is ordinary smooth with zero smooth Hessian on \(W\setminus Z\). Suppose each point of \(Z\) has an ordinary neighborhood \(N\) and ordinary smooth \(g\) there with \(Dg=0\) and \(h=g\) on \(Z\cap N\). Then \(D(hT)=0\) for EVERY positive doubly closed ordinary \((p,p)\)-current, \(0\leq p\leq n-1\). There is no dimension bound and no assumed cutoff mass bound. The same conclusion holds if off \(Z\) smooth harmonicity is replaced by local uniform-on-compact approximation by ordinary smooth zero-Hessian functions: n1 proves the identical defect-support premise needed below. This small extension retains the substantial approximation and analytic-trace assumptions. It is not original P21.3 closure.

Here is a full construction of the cutoff certificates. Localize inside an affinoid neighborhood and choose a relatively compact ordinary subopen \(N\) carrying the trace \(g\). Affinoid noetherianity supplies analytic \(f_1,\ldots,f_m\) whose common zero set in \(N\) is \(Z\cap N\). The affinoid neighborhood is contained in a domain on which the analytic-locus description is valid. Choose a real \(A\) at least two greater than the upper bounds for their finite logarithmic norms. Real constants avoid any use of nontrivial field scaling.

Let \(R_m\) be convolution of \(\max(s_1,\ldots,s_m)\) with a product of nonnegative smooth probability kernels supported in \([-1/4,1/4]\). It is smooth convex, translation-equivariant in the all-ones direction, and differs from the maximum by at most \(1/4\). If \(s_i\) is at least one below the largest other coordinate, then even after every translation in the kernel support it cannot attain the maximum: the gap stays at least \(1/2\). Integrating out that coordinate omits it exactly. Repeated omission permits coordinates equal to \(-\infty\). In particular near a zero of one \(f_i\) outside the common zero locus, its coordinate is inactive, and the remaining active functions are actual analytic units after ordinary shrinking.

Define off \(Z\)
\[
 t=A-R_m(\log|f_1|,\ldots,\log|f_m|).
\]
CLD 15.1.1--2, as checked in n1's source ledger, makes this an ordinary smooth function on actual unit-moment charts. Its smooth Hessian is nonpositive: the logarithmic-unit functions are affine in those charts and the Hessian of \(R_m\) is PSD. We have \(t\geq0\), and \(t\to+\infty\) at \(Z\). The exponentiated regularized maximum is continuous and zero exactly at the common zero locus, so the assertions about neighborhoods are ordinary-topology assertions, not log-domain charts across zeros.

Choose a smooth nondecreasing concave \(b:[0,\infty)\to[0,4]\), identity on \([0,2]\) and constant for arguments at least four. Integrating a smooth nonincreasing derivative, equal to one up to two and zero after four, constructs it. Put \(u_L=L b(t/L)\), \(L\geq1\), and give it its constant capped value on \(Z\). For each fixed \(L\), it is constant on an ordinary neighborhood of \(Z\), so it is ordinary smooth on all \(N\), including any component contained in \(Z\). The chain rule gives
\[
 0\leq u_L\leq4L,\qquad Du_L\leq0,\qquad u_L=t\quad(t\leq2L).             \tag{10}
\]

Fix a compact symmetric detecting \((r,r)\)-test \(\alpha\), \(K=\operatorname{supp}\alpha\). By the ordinary moment presentation theorem, take finitely many ordinary charts \(U_j\subset N\) with unit logarithmic coordinates \(s_j\), presenting \(\alpha\). Refine these finitely so that symmetrized smooth ambient representatives and their derivatives are defined near the compact coordinate images used below. This is permitted by the local definition of smooth forms on paralin spaces and compactness. Choose compact subsets with interiors covering \(K\) and plateaus \(0\leq\rho_j\leq1\) compact in \(U_j\), one near those subsets. Hence each point of \(K\) has at least one \(\rho_j=1\) on a neighborhood. We require neither a global moment for \(N\) nor a partition with a global presentation.

On \(U_j\), set
\[
 \lambda_j=\sum_a d's_{j,a}\wedge d''s_{j,a},\qquad\eta_j=\lambda_j^r,
\]
with \(\eta_j=1\) when \(r=0\). These are ordinary smooth positive and doubly closed on \(U_j\). Their analytic pullbacks may be degenerate; all domination is established in the genuine ambient coefficient spaces first. Define finite constants
\[
 M_j=|\mu_{T|_{U_j},D\rho_j\wedge\eta_j}|(U_j),\quad
 F_j=\langle T|_{U_j},\rho_j\lambda_j^q\rangle,\qquad
 M=\sum_jM_j,\quad F=\sum_jF_j.
\]
All coefficient measures exist by n1. Terms with \(\rho_j\) have compact support inside \(U_j\) and extend smoothly by zero to the SAME \(N\).

Put
\[
 K_{j,L}=\langle T,\rho_j(-Du_L)\wedge\eta_j\rangle,\qquad
 E_{j,L}=\langle T,\rho_j d'u_L\wedge d''u_L\wedge\eta_j\rangle.
\]
They are nonnegative. The actual smooth-factor current \(T|_{U_j}\wedge\eta_j\) is positive and doubly closed by ordinary Leibniz; this needs no initial BT assumption. Smooth duality for this closed current and (10) yields
\[
 K_{j,L}=-\langle u_LT,D\rho_j\wedge\eta_j\rangle\leq4LM_j.                \tag{11}
\]
Using \(D(u_L^2)=2u_LDu_L+2d'u_L\wedge d''u_L\), the same duality gives
\[
 2E_{j,L}=\langle u_L^2T,D\rho_j\wedge\eta_j\rangle
       -2\langle T,\rho_j u_LDu_L\wedge\eta_j\rangle
 \leq16L^2M_j+8LK_{j,L}\leq48L^2M_j.                                    \tag{12}
\]
Thus \(K_L=\sum_jK_{j,L}\leq4LM\) and \(E_L=\sum_jE_{j,L}\leq24L^2M\). These are estimates from fixed signed measures, not uniform bounds silently assigned to a changing family of tests.

Choose a smooth nondecreasing \(\theta\) zero on \(( -\infty,1]\), one on \([2,\infty)\). Define \(v_L=\theta(t/L)\), \(\sigma_L=\theta(2t/L)\), extended as one on \(Z\). They are ordinary smooth by constancy near \(Z\). Choose a compact plateau \(\rho_*=1\) near \(K\); let \(\chi_L=\rho_*v_L\). It equals one near \(Z\cap K\), and
\[
 \beta_L=D(\chi_L\alpha)=D(v_L\alpha)
 =v_LD\alpha+d'v_L\wedge d''\alpha-d''v_L\wedge d'\alpha
   +Dv_L\wedge\alpha.                                                   \tag{13}
\]
The plateau derivatives miss \(K\). This form is compact in \(K\), zero for \(t\leq L\). Derivatives of \(v_L\) occur only on \(L\leq t\leq2L\), where \(u_L=t\), and
\[
 Dv_L=L^{-1}\theta'(t/L)Dt+L^{-2}\theta''(t/L)d't\wedge d''t.
\]

The cross-block estimate in (13) deserves an explicit ordinary-chart justification. On a fixed \(U_j\), all coefficients of \(\alpha,D\alpha,d'\alpha,d''\alpha\) are bounded in the chosen smooth ambient representative on the compact image of \(\operatorname{supp}\rho_j\). Middle PSD order units give \(-C\lambda_j^r\leq\alpha\leq C\lambda_j^r\) and \(-C\lambda_j^q\leq D\alpha\leq C\lambda_j^q\). A degree exceeding the coordinate dimension has zero exterior coefficient space; no estimate assumes moment dimension is analytic dimension.

For the symmetric cross term, append a FORMAL independent covector \(dy\) to the old coefficient space, solely for linear algebra. Its \(q\)-th exterior space splits orthogonally as old \(q\)-vectors and \(dy\) wedged with old \(r\)-vectors. The two cross terms form off-diagonal blocks between these summands, with no diagonal block. A bounded block \(A_j\) obeys \(2|\langle A_jv,w\rangle|\leq C(|v|^2+|w|^2)\). Rescaling \(w\) by \(L^{-1}\) bounds both signs by
\[
 C\big(\lambda_j^q+L^{-2}d't\wedge d''t\wedge\lambda_j^r\big).
\]
Factorials in powers of \(\lambda_j\) are fixed positive constants absorbed into \(C\).

This formal \(y\) is not asserted to be an analytic unit or a moment coordinate. At each actual point of the transition region, inactive-variable omission gives units for the active \(f_i\). Append those actual units to the old moment. In that genuine refined chart, \(t=\tau(z)\) is an ordinary smooth function. On each cell the FIRST-JET linear map sends the old covectors to their old-coordinate projections and \(dy\) to \(d\tau(z)\), and sends primed and double-primed copies in the same way. PSD pullback under that pointwise linear map preserves the inequality. The chain rule supplies the actual first-derivative cross terms. The Hessian term is handled separately: \(-Dt\geq0\) in this genuine chart, so wedging the middle bounds for \(\alpha\) with \(-Dt\) and \(d't\wedge d''t\) gives
\[
 \pm(Dv_L\wedge\alpha)\leq
 C\big(L^{-1}(-Du_L)\wedge\eta_j
       +L^{-2}d'u_L\wedge d''u_L\wedge\eta_j\big)
\]
on the transition region. Outside it the terms vanish. At \(Z\), \(u_L,v_L\) are locally constant, so their derivative terms vanish and only the bounded \(D\alpha\) term remains. This proves the required positivity in actual ordinary charts; it uses no pullback of a nonsmooth current and no nonexistent analytic chart for \(y\).

Take a common \(C\) for the finite coefficient bounds and the fixed derivatives of \(\theta\), independent of \(L\). Then the actual compact smooth positive form
\[
 B_L=C\sum_j\rho_j\sigma_L
 \big(\lambda_j^q+L^{-2}d'u_L\wedge d''u_L\wedge\eta_j
               +L^{-1}(-Du_L)\wedge\eta_j\big)                            \tag{14}
\]
dominates both signs of \(\beta_L\). Wherever \(\beta_L\) may be nonzero, some \(\rho_j=1\), and \(\sigma_L=1\) there; that summand dominates, and every other summand is positive. Elsewhere \(\beta_L=0\). Consequently
\[
 \eta_{L,\pm}=(B_L\pm\beta_L)/2\geq0,\qquad
 \eta_{L,+}-\eta_{L,-}=\beta_L.
\]
All supports are in the fixed compact \(H=\bigcup_j\operatorname{supp}\rho_j\) and in \(t\geq L/2\), with \(t=+\infty\) on \(Z\). They are compact inside the SAME ordinary open \(O_L=\{t>L/3\}\cup Z\subset N\). The strict margin is important; no support is merely contained in the closure of that open. Positivity, \(0\leq\sigma_L\leq1\), and (11)--(12) give the actual uniform bound
\[
 \langle T,\eta_{L,+}+\eta_{L,-}\rangle
 \leq C(F+L^{-2}E_L+L^{-1}K_L)\leq C(F+28M).                             \tag{15}
\]

Continuity and the ordinary analytic trace \(h=g\) on \(Z\cap H\) implies \(\sup_{\operatorname{supp}B_L}|h-g|\to0\). Indeed for any small-error neighborhood of this compact trace set, its complement in \(H\) is compact and disjoint from \(Z\); there \(\max_i|f_i|\) has a positive lower bound, so \(t\) has a finite upper bound. For large \(L\), every moving support misses that complement. If the trace set is empty, the supports eventually are empty. Apply n2's exact estimate (4) to the actual triple \((\chi_L,\eta_{L,\pm},g)\); (15) makes every detecting pairing zero. Ordinary finite localization proves the theorem on \(W\). When \(r=0\), \(\eta_j=1\); the same proof and both energy estimates still apply. No nonempty-locus conclusion is extracted from the dimension theorem in that degree.

For a closed locally zero-dimensional analytic locus, local support is finite and points can be isolated. The dimension here is ANALYTIC dimension, as defined in CLD 11.2.3 by strictification and Krull dimension after a suitable complete scalar extension; Krull dimension of a possibly nonstrict affinoid algebra alone is insufficient. An additional freshly read primary unit, CLD 13.3.1--3, supplies the exact foundation: a point in a zero-dimensional fiber is isolated and has finite-dimensional residue-local algebra over the completed base residue field; a compact zero-dimensional fiber is a finite analytic space over that field. Apply the latter to a compact affinoid piece of the zero-dimensional locus mapping to \(\mathcal M(K)\). Its algebra is consequently finite-dimensional over \(K\), hence Artinian and a finite product of local Artinian rings. Seminorms kill nilpotents and select one factor, and completeness gives the unique extended norm on each finite residue field. Isolate each point \(z\), choose the constant trace \(g=h(z)\), and apply the theorem. Thus isolated analytic points are removable in every allowed current degree, including \(p=n-1\), under the stated off-locus regularity or approximation. Nonstrict ordinary domains are permitted; a blanket finite-residue-field Nullstellensatz for arbitrary nonstrict affinoid algebras is NOT imported. Affinoid noetherianity and the finite-ideal/coherent-subspace correspondence are standard foundations in Berkovich, Spectral theory and analytic geometry over non-Archimedean fields, Mathematical Surveys and Monographs 33 (1990), Chapter 2, sections 2.1--2.2. A tropical trace or a closed skeleton is not an ordinary analytic locus satisfying these hypotheses.

For completeness, the closed torus approximation sector in whole372 is also constructed. On \((\mathbb G_{m,K}^n)^{\rm an}\), fix \(I\subset\{1,\ldots,n\}\), \(|I|=p\leq n-1\), \(s_j=-\log|T_j|\), and
\[
 S_I=\big(\bigwedge_{j\in I}d's_j\wedge d''s_j\big)\wedge\delta_X.
\]
The form is positive and doubly closed, so n3 transfers tautological BT from \(\delta_X\) to \(S_I\). For continuous \(A\geq0\) on \(\mathbb R^I\), compact nonnegative kernel convolution constructs smooth \(A_i\geq0\), uniformly convergent on compact sets. Set \(a_i=A_i(s_I)\). Every differentiated coordinate already occurs in \(S_I\), hence \(d'a_i\wedge S_I=d''a_i\wedge S_I=0\). Each \(a_iS_I\) is positive doubly closed BT; n3's fixed-current theorem gives the same for the actual ordinary product \(A(s_I)S_I\). No growth bound at infinity is needed for compact-kernel convolution. This is a constructed sector, including \(A(s_1)=|s_1|\); it establishes no density among arbitrary currents. For empty \(I\), only constants result.

The independent whole372 mathematical verdict is affirmative for its CONDITIONAL statements with the explicit source repairs, degrees, and ordinary-chart details above. All ten 369 items, the complete scalar367 and relative368 factor chains, the analytic-trace logarithmic proof, its isolated-point conclusion, and its torus sector have been reconstructed. The original 367/368 strong-cone proof steps require correction. Four actual372 FINAL notes equal the four expanded notes field by field; all three actual369 text fields differ from their expanded counterparts. Both sets were treated as data. The whole372 TeX and 71103-byte proof, source metadata and scope/ROOT binding were inspected; historical reading claims give no grant. The recursive CLD analytic foundations were imported openly, not entirely rederived. This is an independent draft verdict, not formal verification or catalogue acceptance.

The ORIGINAL completion decision is separate: candidate=false. No theorem here establishes off-locus ordinary smooth harmonicity or harmonic approximability, an appropriate locally analytic exceptional set, or an ordinary smooth harmonic trace for every original difference \(h=U-V\) with \(D[U]=D[V]\). No exhaustive positive/doubly-closed-current approximation or ordinary-product-compatible harmonic lifting has been constructed. There is no actual admissible analytic counterexample with separately finite continuous individually psh \(U,V\), a positive doubly closed \(T\), exact upstairs curvature equality, and a compact smooth nonzero detector.

The remaining quantifiers are all complete fields, including trivial valuation; arbitrary good separated STRICT boundaryless pure \(n\geq2\) spaces, including singular, reducible and nonreduced ones; every ordinary open; every \(p=0,\ldots,n-1\); arbitrary positive doubly closed ordinary CLD currents; individually admissible finite continuous psh pairs with exact upstairs curvature equality; and actual generic Artinian integration weights. The dossier's already removed curve, polycylinder, invariant toric, and specified weak-closure cases are not counted as new original resolutions. Specified covers and every-open bases remain distinct. No generated-class tautology, two-nonsmooth-factor symmetry, scalar ascent of arbitrary currents, or strong-to-ordinary identification is used.

Deliverables: P21.3-review-paper.tex, P21.3-proof-companion.md, source-ledger-independent.json, full-literal-source-ledger-LOCALONLY.json, whole-proof-coverage.json, independent-whole372-verdict.json, and original-decision.json. Rerun python audit.py and python build_review.py in this workspace. All 157 input bindings and all 31 literal LF-based units matched the retained full source; formfeeds are preserved. The small Plucker diagnostic exhausted 6561 vector pairs, but proves no analytic theorem. The TeX is uncompiled. No supplied program was executed/imported, no subagent or additional model call was used, and no external messages, editor actions, publication, or catalogue writes occurred. No supervised heavy-compute facility was supplied; no resource-heavy computation was launched. All retained mathematical claims are unverified drafts, and execution success does not establish correctness.
