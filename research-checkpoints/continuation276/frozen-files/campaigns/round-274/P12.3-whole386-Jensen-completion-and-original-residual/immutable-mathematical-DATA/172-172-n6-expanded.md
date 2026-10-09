# n6. Singular relative trace generation and isolated characteristic-p envelopes

Use n2--n5 and qualified G331. Work on the actual normal primary Y and boundary Delta constructed in n5. All test ideals are BIG/nonfinitistic. CEMS v4 Definitions2.2--4 apply: Y is normal integral, F-finite, separated and of finite type over the perfect field; dualizing Frobenius trace has the required F!omega=omega. No anticanonical finite-generation hypothesis is imposed.

First justify the asymptotic family without smooth Frobenius roots. For any nonzero ideal b and r>=1, tau(Delta,b^t)=tau(Delta,(b^r)^{t/r}). With q=p^e the exponents A=ceil(qt), B=r ceil(qt/r) obey A<=B<=A+r-1. Choose a common big test element c for both expressions. One trace inclusion is immediate. For the reverse choose nonzero z in b^r; cz is also a test element and cz b^A subset c b^B. The large-e trace formula proves the reverse inclusion. Gradedness and this power invariance direct tau(Delta,b_ell^{m/ell}) under common multiples. Noetherianity and a finite affine cover give a maximal member, with simultaneous stabilization for finitely many families. Define t_m=tau(Y,Delta,b_bullet^m), s_m=tau(Y,b_bullet^m).

Write H=-F, A=O(H), L=K_Y+Delta Cartier. Choose c_0 so (c_0-i)H-L is ample for 1<=i<=dimY, using ordinary ample twisting. Fix m and ell attaining t_m; lambda=m/ell. CEMS2.3, including its arbitrarily large-e tail, gives
t_m=sum_{e>=e_0} Image[F_*^e(b_ell^{ceil(lambda q)} O(K_Y-qL-D_0))->O_Y].
Here D_0 is an effective SCHEME-GLOBAL Cartier test divisor. Its construction needs justification: take finitely many affine test elements, absorb the bounded rounding differences, and form an effective Weil divisor containing the closures of their zeros and the fixed rounding bounds. For large r the coherent O(-E) tensor A^r is generated and has a nonzero global section. Viewed as a section of A^r, its zero divisor D_0 is effective Cartier and dominates E. At each affine chart its local equation divided by the chosen test element is regular by the normal height-one criterion. Multiples of a test element remain test elements. Thus the affine tail formulas glue for this D_0. It may depend on m,ell, while c_0 does NOT.

Put a_e=ceil(qm/ell), j_e=ell a_e-qm, so 0<=j_e<ell. Products of global I_ell sections generate b_ell^{a_e} O(a_e ell C). After twisting the trace target by O(mC+c_0H), multiplication by these products INSIDE F_*^e gives an O_Y-linear surjection from finitely many copies of
Q_{e,j_e}=F_*^e O(q(c_0H-L)+K_Y-D_0-j_e C)
onto the trace source. In local notation each map is F_*t |-> F_*(s t); it is linear since the module action is by q-th powers. No base-module factor has been pulled out of Frobenius.

For 1<=i<=dimY, H^i(Q_{e,j} tensor A^{-i}) equals, as an abelian group, H^i(O(K_Y-D_0-jC) tensor O(q((c_0-i)H-L))). The first factor is a fixed coherent reflexive sheaf, even on non-CM Y. There are only finitely many j,i. Serre vanishing kills these groups for all sufficiently large e. N3's independently proved relative regularity makes every such Q_{e,j} globally generated. Each trace source and each trace image is therefore globally generated. The tail sum stabilizes as a coherent sheaf on quasi-compact Y, so t_m O(mC+c_0H) is generated for ALL m. Tensor once more with A and set c=c_0+1. The Serre threshold can depend on m; c cannot and does not.

Set F_m=t_m O(mC) A^c and J_m=Gamma(Y,F_m). Hartogs places its sections in B. Generation gives the exact equality J_m O_Y=F_m on EVERY support. Before the extra A twist the generated sheaf has its sections in B and hence is a subsheaf of O_Y; the extra twist puts F_m inside J O_Y. Thus J_m is proper. Let T_0=tau(Y,Delta). Localization and regularity of the puncture make T_0 unit there; it contains J^r O_Y for some r. The multiplication formula below gives b_m T_0 subset t_m. Consequently I_m J^{r+c} subset J_m, so it contains a primary power. It is an actual primary ideal, not just a fractional test-module image. At every support
g_m=-v(J_m)/m=f_C-(c v(J)+v(t_m))/m
is a continuous geometric primary profile below f_C.

For completeness, b T_0 subset tau(Delta,b) follows from a common test element z: f phi(F_*^e z)=phi(F_*^e(f^q z)) for f in b, and f^q belongs to b^q. Sum the trace formula and localize. The ell=ml term therefore gives b_{ml}T_0 subset t_{ml} subset s_{ml}. N4's corrected subadditivity gives Jac^{l-1}s_{ml} subset s_m^l. Every ideal value here is finite on all support quotients, since these coherent ideals contain primary powers on Y.

Let h=f_C-p(f_C). N5 and Fekete give h=lim_l v(b_{ml})/(ml). Reversing the two ideal inclusions and dividing yields
v(s_m)/m <= v(s_{ml})/(ml)+(l-1)v(Jac)/(ml)
<= [v(b_{ml})+v(T_0)]/(ml)+(l-1)v(Jac)/(ml).
At a fixed semivaluation let l tend to infinity: v(s_m)<=m h+v(Jac). Boundary monotonicity and the Cartier shift, with 0<=Delta<=bF, give O(-bF)s_m subset t_m subset s_m, hence v(t_m)<=v(s_m)+b v(J). Substitution proves
0<=p(f_C)-g_m<=[c v(J)+v(Jac)+b v(J)]/m<=(c+a+b)N_J/m
on EVERY normalized point, including nonzero supports and infinite values of individual functions. The finite T_0 term disappears pointwise before the resulting uniform bound. This is uniform approximation by actual C profiles, so p(f_C) belongs to C. No increasing-D, energy or capacity recognition is used.

The finite collection in n5 was arbitrary. Every signed rational primary obstacle is therefore represented by a supported Cartier divisor on such a model; clear denominators and use positive homogeneity. N2's signed lattice density and nonexpansivity give p(f) in C for EVERY finite continuous obstacle. It is finite continuous, equals its USC regularization and is the greatest geometric minorant. N2 then constructs bounded USC greatest minorants with ONE decreasing C-net and proves the exact primary-gauge cocycle.

This proves the exact scoped isolated theorem proposed in ROOT377, relative to the qualified G331 cone and the stated ordinary published algebraic foundations, with the new regularity proof and finite-field repair. It is an independently reconstructed UNVERIFIED draft theorem. No assertion is inherited from ROOT377 and no count or acceptance is changed. Scope: normal isolated AFFINE finite-type germs at CLOSED codimension>=2 points over PERFECT characteristic-p fields, every dimension and every semivaluation support. It makes no smooth-model or resolution hypothesis. It does not apply to nonisolated, imperfect, mixed-characteristic, nonalgebraic or arbitrary excellent normal germs.

Artifacts: n6.md, whole-proof.md, source-application-ledger.md, P12.3-paper.md and uncompiled P12.3-paper.tex. Rerun: python build_delivery.py; python final_audit.py. Execution is not mathematical verification.
