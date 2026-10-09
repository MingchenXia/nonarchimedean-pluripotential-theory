There is a complete separable, skeletal, bounded equation and envelope theory on (X,θ) of n1–n2. This is a restricted theorem, not an intrinsic all-support E¹ theorem. Throughout, dy is probability Lebesgue measure on C=R/Z, while analytic Monge–Ampère measures have raw mass 2.

Let H={h∈C(C):ρ_h=dy+h''≥0 distributionally}. Every ρ_h has mass one. For G(y)=y²/2-y/2+1/12 extended periodically, G has mean zero and G''=dy-δ_0. Given any probability ν on C, h_ν=-G*ν satisfies ρ_(h_ν)=ν. Conversely h-h_(ρ_h) has zero distributional second derivative and is periodic, hence constant. Thus H/R is exactly the circle probability measures. Since G lies in [-1/24,1/12] and is 1/2-Lipschitz, its mean-zero solutions lie in [-1/12,1/24], are 1/2-Lipschitz, and have oscillation at most 1/8. The normalized set {h∈H:sup h=0} is uniformly bounded and equicontinuous, hence compact by Arzelà–Ascoli; positivity is closed under uniform convergence by distributional testing. These are explicit compactness replacements only in the circle directions.

Put S_θ={h_1∘τ_1+h_2∘τ_2:h_j∈H}. Convolution by nonnegative periodic smooth kernels gives uniform approximants with 1+h_j''≥0; diagonal local Hessians prove S_θ⊂C_θ. For u=h_1(x_1)+h_2(x_2), v=k_1(x_1)+k_2(x_2), the smooth identity-torus computation and n2's uniform continuity give

B(u,v)=i_*(ρ_(h_1)⊗ρ_(k_2)+ρ_(k_1)⊗ρ_(h_2)),
MA_θ(u)=2i_*(ρ_(h_1)⊗ρ_(h_2)).

Weak convergence of the product probabilities follows by density of finite sums of products of circle continuous functions on C². Continuity of the actual Gauss section i then gives convergence against analytic continuous test functions. Thus the equality is one of measures on X. It is not only a pushforward formula.

Every measure 2i_*(ν_1⊗ν_2), with ν_j arbitrary circle probabilities, is therefore solved by u=h_(ν_1)∘τ_1+h_(ν_2)∘τ_2. Marginal recovery and the preceding circle uniqueness prove uniqueness modulo constants within S_θ. This theorem makes no uniqueness assertion against an arbitrary member of C_θ or any proposed larger psh class.

All circle potentials are Lipschitz. Their energy

e(h)=∫_C h dy-(1/2)∫_C |h'|²dy

is finite. Distributional integration by parts is legitimate: convolution gives uniform convergence of h and L² convergence of h', while the positive measures ρ_h converge weakly. Hence ∫h dρ_h=∫hdy-∫|h'|²dy. For h,k∈H one obtains the exact identity

e(k)-e(h)=∫(k-h)dρ_h-(1/2)∫|k'-h'|²dy.

In particular e is concave, strictly concave modulo constants, and its derivative along every admissible circle segment is integration against ρ_h. Define E_sep(u)=2(e(h_1)+e(h_2)); moving a constant between the two factors does not change this expression. It has the required additive covariance E_sep(u+c)=E_sep(u)+2c. For the bounded CLD mixed energy

E_θ(u)=(1/3)∫_X u(θ²+θ∧α_u+MA_θ(u)),

the measure formulas above show E_θ=E_sep on S_θ. Indeed θ∧α_u=i_*(ρ_(h_1)⊗dy+dy⊗ρ_(h_2)); after summing the three terms and dividing by three, each factor contributes ∫hdy+∫h dρ_h=2e(h). This proves the normalization directly. It does not establish differentiability of E_θ in all analytic directions.

For ANY positive Radon μ on X of mass 2 define the restricted dual energy

E*_sep(μ)=sup_(u∈S_θ)(E_sep(u)-∫u dμ).

It is finite, between 0 and 1/2. To see this, normalize each h_j by sup h_j=0. Then -1/4≤u≤0 and E_sep(u)≤0, giving the upper bound; u=0 gives the lower bound. Let ν_j=(1/2)(τ_j)_*μ. The functional equals 2Σ_j(e(h_j)-∫h_j dν_j). The exact difference identity proves that its unique maximizing factors modulo constants satisfy ρ_(h_j)=ν_j. Their analytic Monge–Ampère measure is the product measure 2i_*(ν_1⊗ν_2), regardless of the original μ's analytic support or correlation. Consequently this finite dual functional does not certify full finite energy or solve arbitrary support.

For example let y be the K-rational analytic point (z_1,z_2)=(1,1) in the chosen quotient sheet, and μ=2δ_y. Its circle marginals are δ_0. The maximizer is u_0=-G(x_1)-G(x_2), whose derivative energy satisfies ∫_C|G'|²dy=1/12. Thus E_sep(u_0)=-1/6, u_0(y)=-1/6, and E*_sep(2δ_y)=1/6. But MA_θ(u_0)=2δ_(i(0)), and i(0)≠y since |z_j-1| is respectively 1 and 0. This proves failure of this restricted inverse problem for a measure of finite RESTRICTED dual energy. It is not a counterexample to the literal P16.7 finite-energy equation.

For completeness the circle envelope has the full obstacle properties in its exact scope. For a∈C(C), let P(a) be the pointwise supremum of all h∈H with h≤a. Constants give a nonempty family. The uniform Lipschitz bound and a finite upper bound make its supremum finite, continuous and 1/2-Lipschitz. On the real line, y²/2+P(a)(y) is a supremum of convex functions, hence convex. Thus P(a)∈H and is the largest admissible minorant. Monotonicity and translation by constants give ||P(a)-P(b)||_∞≤||a-b||_∞.

Its curvature measure is supported on the contact set {P(a)=a}. Write p=P(a) and F(y)=y²/2+p(y). If curvature charged a noncontact open arc, choose a short interval [c,d] compactly inside that arc with positive curvature in (c,d). The clearance a-p is positive on the interval. Replacing convex F by its endpoint chord on [c,d] raises it somewhere (otherwise its interior curvature is zero), preserves convexity because its chord slope lies between the adjacent exterior slopes, and raises it by less than the clearance when the interval is sufficiently short. The latter follows from local bounded slopes of F. Apply the same modification on every integer translate, using F(y+n)=F(y)+ny+n²/2. This preserves the periodicity of F-y²/2, makes an admissible larger minorant, and contradicts maximality. Positive curvature in a noncontact arc can always be localized in arbitrarily short such intervals. Therefore ∫(a-p)dρ_p=0.

Finally let p_b=P(a+bv) for v∈C(C). The energy difference identity and the two contact-support assertions imply

b∫v dρ_(p_b)≤e(p_b)-e(p)≤b∫v dρ_p.

Uniform nonexpansiveness gives p_b→p; distributional testing and fixed mass give weak convergence ρ_(p_b)→ρ_p. Dividing the inequalities for either sign of b yields d/db|_(b=0)e(P(a+bv))=∫v dρ_(P(a)). Thus envelope orthogonality and first variation are proved in every CIRCLE direction. They are not proved for obstacles on arbitrary ordinary analytic opens or for all analytic directions.

The proof is elementary circle analysis plus the ordinary bounded CLD calculus proved in n2. No imported whole373 claim is a premise. This reconstructs its useful separable conclusions with their mass and support restrictions made explicit. Artifacts: notes/n3.md, P16.7-partial-paper.md and proof-companion.md. Rerun own finite checks with `python scripts/diagnostics.py`; those checks do not prove any universal measure or analytic assertion.
