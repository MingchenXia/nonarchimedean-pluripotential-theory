The bounded analytic branch potentials U_N of n2 give a new exact dual-energy obstruction: the raw-mass-two rigid atom 2δ_y has infinite dual energy already when the supremum is taken over C_θ, although its separable dual energy in n3 equals 1/6. This is an admissibility result, not a counterexample to the original finite-energy Monge–Ampère problem.

Use the bounded mixed energy E_θ from n3 and put E*_(C_θ)(μ)=sup_(u∈C_θ)(E_θ(u)-∫u dμ), for μ of mass 2. The additive covariance follows directly from the three mixed measures of mass 2, so the functional is invariant under addition of constants. No general concavity, compactness, or energy differentiability on C_θ is assumed in this note.

All details of the energy computation take place on ordinary opens and use coefficient measures, not an unproved global integration-by-parts identity for two nonsmooth functions. Let α_0=θ+d'd''u_0 and F=τ^-1(0), W={|z_1-1|<1,|z_2-1|<1} in the quotient sheet. On W one has x_1=x_2=0, so both q and u_0 are constant there. Hence θ|W=0 and α_0|W=0 as currents. The continuous function D_N vanishes outside W, including its boundary. The order-zero coefficient-measure construction in n2 therefore implies D_Nθ=D_Nα_0=0 globally: on W the current restricts to zero and on its complement the scalar is zero. This uses the same ordinary open and compact-support calculus throughout.

Since α_(U_N)=α_0+d'd''D_N, smooth-factor multiplication and its continuous extension give

θ∧α_(U_N)=θ∧α_0+d'd''(D_Nθ)=θ∧α_0.

Outside the closed fiber F one has U_N=u_0 on an ordinary neighborhood. Locality and MA_θ(u_0)=2δ_(i(0)) imply that MA_θ(U_N) is supported on F. On F, u_0=-1/6. From n2, MA_θ(U_N)|W=δ_(ξ_N), total mass is 2, D_N is zero outside W, and D_N(ξ_N)=-N. Therefore

∫_X U_N MA_θ(U_N)=-(1/6)·2+∫_W D_N dδ_(ξ_N)=-1/3-N.

The Gauss section has D_N=0 everywhere: at a Gauss point with |z_j|=1, |z_j-1|=1, and elsewhere at least one d_j is zero. Also ∫u_0θ²=2∫_(C²)u_0 dx=0 because G has mean zero. The mixed measure θ∧α_0 is i_*(dy⊗δ_0+δ_0⊗dy). Thus

∫U_Nθ²=0,
∫U_N(θ∧α_(U_N))=∫u_0(θ∧α_0)=-1/6.

Substitution into the defining three-term formula yields the exact equality

E_θ(U_N)=-1/6-N/3.

At the K-rational point y=(1,1), D_N(y)=-N and u_0(y)=-1/6. Hence

E_θ(U_N)-2U_N(y)=1/6+5N/3→+∞.

It follows rigorously that E*_(C_θ)(2δ_y)=+∞. This conclusion holds on the unconditional quotient X; the Picard foundation F_L in n1 is not used. Any proposed larger finite-energy theory which contains these bounded locally generated potentials and agrees with their mixed energy must also assign infinite dual energy to 2δ_y. Without a class-comparison theorem this last statement is an explicit implication, not an identification of C_θ with an unspecified full psh class. Dividing all raw energies and measures by 2 to use probability mass changes the values by a fixed factor and does not remove divergence.

The normalized family also illustrates the missing topology. Since D_N≤0 and u_0 attains its maximum 1/12 outside F, sup U_N=1/12 for every N, while U_N(y)→-∞. Thus these sup-normalized potentials are not uniformly precompact. Their energies tend to -∞, so they do not disprove a compactness theorem on an energy-bounded set or in a weaker topology. U_N decreases pointwise to an extended weight singular at y; no assertion that this limit belongs to E¹, has full mass, or satisfies decreasing operator continuity is made.

This explicitly separates the finite restricted dual energy from admissibility for an all-direction theory and supplies a local analytic branch test such a theory must pass. Artifacts: notes/n4.md, P16.7-partial-paper.md, proof-companion.md and evidence/diagnostics.json. Rerun the own rational-value checks with `python scripts/diagnostics.py`; checking finitely many N is diagnostic evidence only, while the displayed analytic derivation proves the formula for every N≥1.
