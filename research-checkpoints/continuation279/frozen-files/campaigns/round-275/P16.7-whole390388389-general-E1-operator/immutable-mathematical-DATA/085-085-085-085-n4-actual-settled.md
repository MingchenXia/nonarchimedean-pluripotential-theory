The branch potentials U_N of n2 prove that the rigid mass-two atom 2δ_y has infinite dual energy already over C_θ, although its separable dual energy is 1/6 by n3. This is an admissibility result, not a counterexample to the original finite-energy equation.

Use E_θ from n3 and define E*_(C_θ)(μ)=sup_(u∈C_θ)(E_θ(u)-∫u dμ) for μ of mass 2. Each mixed measure has mass 2, so E_θ(u+c)=E_θ(u)+2c and the objective is unchanged by constants. General concavity, compactness or energy differentiation on C_θ is not assumed.

The computation uses ordinary opens and coefficient measures, avoiding an unproved nonsmooth global integration-by-parts identity. Let α_0=θ+d′d″u_0, F=τ^-1(0) and W={|z_1-1|<1,|z_2-1|<1}. On W, x_1=x_2=0, so q and u_0 are constant. Thus θ|W=α_0|W=0. The continuous D_N vanishes outside W, including its boundary. The order-zero coefficient-measure calculus therefore gives D_Nθ=D_Nα_0=0 globally: the currents vanish on W and the multiplier vanishes on its complement.

Since α_(U_N)=α_0+d′d″D_N, smooth-factor multiplication and its continuous extension give θ∧α_(U_N)=θ∧α_0+d′d″(D_Nθ)=θ∧α_0. Outside the closed fiber F, U_N=u_0 on ordinary neighborhoods. Locality and MA_θ(u_0)=2δ_(i(0)) show that MA_θ(U_N) is supported on F. There u_0=-1/6. By n2, MA_θ(U_N)|W=δ_(ξ_N), its total mass is 2 and D_N(ξ_N)=-N. Consequently
∫U_N MA_θ(U_N)=-1/3-N.

D_N is zero everywhere on the original Gauss section: at a unit-radius Gauss point |z_j-1|=1, and elsewhere at least one d_j is zero. Since G has mean zero, ∫U_Nθ²=∫u_0θ²=0. Also θ∧α_0=i_*(dy⊗δ_0+δ_0⊗dy), giving ∫U_N(θ∧α_(U_N))=-1/6. Substitution into the defining three-term energy proves, for EVERY N≥1,
E_θ(U_N)=(0-1/6-1/3-N)/3=-1/6-N/3.

At the actual K-rational point y=(1,1), D_N(y)=-N and u_0(y)=-1/6. Therefore
E_θ(U_N)-2U_N(y)=1/6+5N/3→+∞,
so E*_(C_θ)(2δ_y)=+∞. F_L is not used. Any larger theory containing these bounded locally generated potentials and agreeing with their mixed energy also has infinite dual energy at this atom. Without a class-comparison theorem that is an explicit implication, not identification with an unspecified full psh theory. Dividing both raw measures and energies by 2 preserves divergence.

Since D_N≤0 and u_0 attains its maximum 1/12 outside F, sup U_N=1/12 for every N, while U_N(y)→-∞. This family is not uniformly precompact after sup normalization. Its energies tend to -∞, so it does not disprove compactness on energy-bounded sets or in weaker topologies. The decreasing extended limit is singular at y; no E¹ membership, full mass or unbounded decreasing continuity is claimed.

This proves the precise failure of using restricted finite dual energy as full admissibility. Artifacts are notes/n4.md, P16.7-partial-paper.md, proof-companion.md and evidence/diagnostics.json. `python scripts/diagnostics.py` checks eight rational instances; that finite computation is diagnostic only, while the current-and-measure argument proves the displayed formula for all N.