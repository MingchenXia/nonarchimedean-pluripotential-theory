Use G331 and n2–n5. On n5’s actual normal primary Y put H=-F, A=O(H), L=K_Y+Delta Cartier. CEMS v4 big test ideals apply because Y is normal integral, F-finite, separated finite type over perfect k with the stated duality. No anticanonical finite-generation assumption is imposed.

Power invariance is proved without smooth roots. For b nonzero and r>=1, A_e=ceil(qt) and B_e=r ceil(qt/r) satisfy A_e<=B_e<=A_e+r-1. With a common big test element c, one inclusion of tau(Delta,b^t) and tau(Delta,(b^r)^{t/r}) is immediate. For the reverse take nonzero z in b^r; cz is also a test element and cz b^{A_e} subset c b^{B_e}. The tail trace formula proves equality. Gradedness directs tau(Delta,b_ell^{m/ell}) under common multiples; Noetherianity on a finite affine cover gives global stabilization. Denote its maximal member t_m and the zero-boundary version s_m.

Choose c_0 with (c_0-i)H-L ample for i=1..dimY. Fix m and ell attaining t_m; lambda=m/ell. CEMS2.3 gives, for any sufficiently large lower tail index,
t_m=sum_e Image[F_*^e(b_ell^{ceil(lambda q)} O(K_Y-qL-D_0))->O_Y].
The Cartier test divisor D_0 is SCHEME-GLOBAL: on a finite affine cover choose test elements and bounded rounding corrections; an effective Weil E contains their closed zero divisors. For large r, a nonzero section of generated O(-E) tensor A^r, viewed in A^r, has effective Cartier zero divisor D_0>=E. Normal height-one intersection shows its local equations are multiples of the local test elements. Multiples remain test elements, so the affine arbitrary-tail formulas glue. D_0 may depend on m,ell; c_0 does not.

Set a_e=ceil(qm/ell), j_e=ell a_e-qm in[0,ell-1]. Products of global I_ell sections generate b_ell^{a_e} O(a_e ell C). After twisting the trace target by O(mC+c_0H), multiplication by these products INSIDE Frobenius gives a surjection from copies of
Q_{e,j}=F_*^e O(q(c_0H-L)+K_Y-D_0-jC)
onto the trace source. These maps are O-linear since scalar action is by q-th powers; no base factor is incorrectly pulled through Frobenius.

H^i(Q_{e,j} A^{-i}) equals the cohomology of the fixed coherent reflexive O(K_Y-D_0-jC) tensored by the ample q-th power O(q((c_0-i)H-L)). There are finitely many i,j. Serre vanishing and n3 make every sufficiently large Q_{e,j} generated. Trace images are generated and their tail sum stabilizes. Hence t_m O(mC+c_0H) is generated for EVERY m, with fixed c_0. Set c=c_0+1 and tensor once more by A.

Let F_m=t_m O(mC) A^c and J_m=Gamma(F_m). Hartogs puts sections in B; generation gives EXACTLY J_m O_Y=F_m on every support. Before the extra A, the generated sheaf’s sections lie in B, so it is a subsheaf of O_Y. The extra twist puts F_m inside J O_Y and makes J_m proper. T_0=tau(Y,Delta) is unit off the fibre and contains J^r O_Y. A common test element proves b T_0 subset tau(Delta,b): f phi(F_*z)=phi(F_*(f^q z)) for f in b. Thus b_m T_0 subset t_m and I_m J^{r+c} subset J_m. This supplies a primary power. J_m is an ACTUAL primary ideal and
g_m=-v(J_m)/m=f_C-[c v(J)+v(t_m)]/m
is a continuous geometric competitor.

For every l, b_{ml}T_0 subset t_{ml} subset s_{ml}, while n4 gives Jac^{l-1}s_{ml} subset s_m^l. These ideal values are finite on ALL supports because they contain primary powers. Put h=f_C-p(f_C)=lim_l v(b_{ml})/(ml). Reversing containment gives
v(s_m)/m <= [v(b_{ml})+v(T_0)]/(ml)+(l-1)v(Jac)/(ml).
At a fixed support let l tend to infinity: v(s_m)<=m h+v(Jac). Boundary monotonicity and the Cartier shift with 0<=Delta<=bF give O(-bF)s_m subset t_m subset s_m, so v(t_m)<=v(s_m)+b v(J). Therefore
0<=p(f_C)-g_m<=[c v(J)+v(Jac)+b v(J)]/m<=(c+a+b)N_J/m.
The finite T_0 term disappears pointwise before this uniform bound. Individual functions may have infinite values; all correction ideals remain finite. Uniform approximation by actual C profiles recognizes p(f_C) in C. No increasing-D, energy or capacity shortcut is used.

The finite primary collection was arbitrary. Signed rational obstacles are carried on these models; denominator clearing and positive homogeneity apply. N2’s density and nonexpansivity prove CE for EVERY finite continuous obstacle. N2 then supplies bounded USC greatest minorants from ONE decreasing C-net and the exact primary-gauge cocycle.

This independently reconstructs ROOT377’s exact proposed isolated sector, with both repairs. It is an UNVERIFIED mathematical draft relative to qualified G331 and the explicitly disclosed published foundations. It proves no nonisolated universal, imperfect, mixed-characteristic, nonalgebraic or arbitrary excellent theorem and changes no acceptance count. Artifacts: n6.md, whole-proof.md, P12.3-paper.md and uncompiled P12.3-paper.tex. Rerun: python build_delivery.py; python final_audit.py.