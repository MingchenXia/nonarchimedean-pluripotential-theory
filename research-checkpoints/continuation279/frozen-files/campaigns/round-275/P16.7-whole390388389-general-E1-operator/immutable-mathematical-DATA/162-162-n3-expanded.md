# Exact branch-family dual at the actual finite-depth Dirac point

Use n1's bounded calculus and n2's finite branch family. Let B be all u_c=u0+sum c_i D_(N_i)+constant with finitely many depths N_i>0, c_i>=0, sum c_i<=1, including the empty sum. Constants do not affect a raw-mass-two dual. B is a concrete subset of C_theta. Fix any finite N0>0 and the ACTUAL analytic point xi_(N0) in W; this is distinct from the rigid point (1,1).

The exact result is

sup_(u in B)(E(u)-2u(xi_(N0)))=1/6+5N0/3,

attained by U_(N0). This proves only a restricted dual value, not finite dual energy over C_theta or over a full intrinsic E1 class.

Here is an all-parameters proof, not finite numerical evidence. For a finite sum define its decreasing tail C(t)=sum_(N_i>=t)c_i for t>0. It takes values in [0,1] and vanishes beyond the largest depth. At xi_(N0), sum c_i(-D_(N_i))=sum c_i min(N0,N_i)=integral_0^N0 C(t)dt. The branch mass tail at depth t is sum_(N_i>=t)p_i=C(t)^2 by the telescoping formula in n2. Tonelli on finite nonnegative sums gives

S=sum_i p_i sum_j c_j min(N_i,N_j)=integral_0^infinity C(t)^3dt.

Thus the objective is

1/6+integral_0^N0 (2C(t)-C(t)^3/3)dt
      -(1/3)integral_N0^infinity C(t)^3dt.

On [0,1], 2c-c^3/3 is increasing and its maximum is 5/3. The tail term is nonpositive. Hence the objective is at most 1/6+5N0/3. Take C(t)=1 on (0,N0) and zero after N0, namely U_(N0), to obtain equality. For the older single-pencil tests this same formula reduces to E(V_(a,N))-2V_(a,N)(xi_(N0))=1/6+2a min(N,N0)-a^3N/3; there is no divergence as N tends to infinity at fixed xi_(N0).

More generally for mu_p=(2-p)delta_i(0)+p delta_xi_(N0), 0<=p<=2, the B-dual is

1/6+N0 times [ (2/3)p^(3/2) if 0<=p<=1;
                      p-1/3 if 1<=p<=2 ].

Replace 2C by pC in the preceding objective. The maximizing value on [0,1] of pc-c^3/3 occurs at c=sqrt(p) when p<=1 and at c=1 when p>=1; the tail is again best zero. This proves the exact formula and attainment by V_(sqrt(p),N0) or U_(N0), respectively. For p<=1 the maximizing potential's actual MA is mu_p by n2. For p>1 its actual MA is delta_i(0)+delta_xi_(N0), which differs from mu_p. In particular the B-maximizer for 2delta_xi_(N0) is NOT a solution. This explicit calculation exhibits the difference between restricted variational optimization and solving the genuine equation.

The only implication for the full bounded dual is the lower bound E*_C_theta(2delta_xi_(N0))>=1/6+5N0/3. It provides no upper bound. No universal analytic atom cap or local Newton-body bound for arbitrary all-direction psh potentials is proved. In particular, the inability of B to realize branch mass two cannot show nonexistence in C_theta or in any full-mass E1 extension. The infinite-dual rigid test cannot be transplanted to this finite-depth point. Both full-dual admissibility and a full-domain solution/universal obstruction remain unresolved.

Artifacts: notes/n3.md, proof-companion.md, P16.7-independent-paper.tex and evidence/diagnostics.json. Rerun `python audit_and_build.py`; its exact finite rational rows merely check algebraic instances of the universal tail argument above. Support: n1, n2.
