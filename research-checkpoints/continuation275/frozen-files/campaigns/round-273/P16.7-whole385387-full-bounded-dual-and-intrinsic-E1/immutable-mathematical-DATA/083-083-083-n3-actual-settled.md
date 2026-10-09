This is a complete restricted separable, skeletal, bounded equation and envelope theory on (X,θ) of n1–n2, not an intrinsic all-support E¹ theorem. Circle Lebesgue dy has probability mass one; analytic Monge–Ampère measures retain raw mass 2.

Let C=R/Z and H={h∈C(C):ρ_h=dy+h″≥0 distributionally}. Every ρ_h has mass one. The periodic G(y)=y²/2-y/2+1/12 has mean zero and G″=dy-δ_0. For any circle probability ν, h_ν=-G*ν satisfies ρ_(h_ν)=ν. Conversely h-h_(ρ_h) has zero second derivative and is periodic, hence constant. Thus H/R is precisely the circle probabilities. Since G∈[-1/24,1/12] and is 1/2-Lipschitz, mean-zero solutions lie in [-1/12,1/24], are 1/2-Lipschitz and have oscillation ≤1/8. The sup-zero normalized set is uniformly bounded and equicontinuous, hence compact by Arzelà–Ascoli; distributional positivity is closed under uniform limits. This is compactness only in the circle directions.

Put S_θ={h_1∘τ_1+h_2∘τ_2:h_j∈H}. Positive periodic convolution gives smooth uniform approximants with 1+h_j″≥0, so S_θ⊂C_θ. For u=h_1(x_1)+h_2(x_2), v=k_1(x_1)+k_2(x_2), the smooth identity-chart computation and n2's continuity give
B(u,v)=i_*(ρ_(h_1)⊗ρ_(k_2)+ρ_(k_1)⊗ρ_(h_2)),
MA_θ(u)=2i_*(ρ_(h_1)⊗ρ_(h_2)).
Weak convergence of product probabilities follows by density of finite sums of products of circle continuous functions. Continuity of the actual section i gives convergence against analytic continuous tests. These are equalities of measures on X.

Every measure 2i_*(ν_1⊗ν_2) is solved by h_(ν_1)∘τ_1+h_(ν_2)∘τ_2. Marginal recovery and circle uniqueness prove uniqueness modulo constants WITHIN S_θ. No uniqueness against arbitrary C_θ or a larger psh class is asserted.

All h∈H are Lipschitz, and e(h)=∫hdy-(1/2)∫|h′|²dy is finite. Convolution gives uniform convergence of h, L² convergence of derivatives and weak curvature convergence, proving distributional integration by parts ∫h dρ_h=∫hdy-∫|h′|²dy. Consequently
 e(k)-e(h)=∫(k-h)dρ_h-(1/2)∫|k′-h′|²dy.
Thus e is concave, strictly concave modulo constants, with derivative along every admissible circle segment equal to integration against ρ_h.

Define E_sep(u)=2(e(h_1)+e(h_2)). Moving a constant between factors changes neither its value nor the represented u, and E_sep(u+c)=E_sep(u)+2c. Define the bounded mixed energy
E_θ(u)=(1/3)∫_X u(θ²+θ∧α_u+MA_θ(u)).
On S_θ one has θ∧α_u=i_*(ρ_(h_1)⊗dy+dy⊗ρ_(h_2)). Summing the three energy terms makes each factor contribute ∫hdy+∫h dρ_h=2e(h); hence E_θ=E_sep. This checks normalization directly, without claiming energy differentiability in all analytic directions.

For ANY positive analytic Radon μ of mass 2 define E*_sep(μ)=sup_(u∈S_θ)(E_sep(u)-∫u dμ). This lies between 0 and 1/2: normalize both factors by sup h_j=0, giving -1/4≤u≤0 and E_sep(u)≤0; u=0 gives the lower bound. For ν_j=(1/2)(τ_j)_*μ the objective equals 2Σ_j(e(h_j)-∫h_j dν_j). The exact energy-difference identity proves that its maximizing factors, uniquely modulo constants, satisfy ρ_(h_j)=ν_j. Their analytic MA is 2i_*(ν_1⊗ν_2), irrespective of μ's original support or correlation. Finiteness of this restricted dual does not certify full finite energy.

For the K-rational point y=(1,1), μ=2δ_y has both marginals δ_0. Its maximizer is u_0=-G(x_1)-G(x_2). Since ∫|G′|²dy=1/12, E_sep(u_0)=-1/6 and u_0(y)=-1/6, so E*_sep(2δ_y)=1/6. But MA_θ(u_0)=2δ_(i(0)), and i(0)≠y: |z_j-1| is respectively one and zero. This disproves that restricted inverse problem for this restricted-admissible measure; it does not disprove P16.7.

Circle obstacle envelopes have full properties in their exact scope. For continuous a let P(a)=sup{h∈H:h≤a}. Constants make the family nonempty. Its common Lipschitz bound and finite bounds make the supremum finite, continuous and 1/2-Lipschitz. On R, y²/2+P(a)(y) is the supremum of convex functions, hence convex. Thus P(a)∈H and is the largest admissible minorant. Monotonicity and constant translation give ||P(a)-P(b)||_∞≤||a-b||_∞.

Its curvature is supported on {P(a)=a}. If F(y)=y²/2+P(a)(y) had curvature in a noncontact arc, choose a short interval compactly inside that arc, with positive interior curvature and positive obstacle clearance. Replace F on the interval by its endpoint chord. This raises it somewhere, preserves convexity because the chord slope lies between exterior slopes, and stays within clearance when the interval is short, by bounded local slopes. Repeat on integer translates using F(y+n)=F(y)+ny+n²/2. The result gives a larger periodic admissible minorant, contradiction. Therefore ∫(a-P(a))dρ_(P(a))=0.

Let p=P(a), p_b=P(a+bv) for continuous circle v. The difference identity and the two contact-support statements give
b∫v dρ_(p_b)≤e(p_b)-e(p)≤b∫v dρ_p.
Nonexpansiveness gives p_b→p uniformly; distributional testing and fixed mass give ρ_(p_b)→ρ_p weakly. Dividing for either sign of b proves d/db|_0 e(P(a+bv))=∫v dρ_p. Orthogonality and first variation are thereby established in every CIRCLE direction, not for arbitrary analytic obstacles or all analytic directions.

This reconstructs the useful whole373 conclusions through elementary circle analysis and n2's repaired bounded calculus. No imported whole373 result is a premise. Artifacts are notes/n3.md, P16.7-partial-paper.md and proof-companion.md. Own diagnostic checks rerun with `python scripts/diagnostics.py`; they do not establish universal analytic assertions.