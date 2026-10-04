ID: n3

SUMMARY:
A classical psh Gauss-boundary spike on a closed disc admits no local continuous sequence when the residue field is uncountable. For this particular spike, countable residue is sufficient via an explicit decreasing ordinary smooth positive-form sequence.

DETAILED SUMMARY:
Over a complete algebraically closed nontrivially valued field, set u=A>0 at the Gauss point of the closed unit disc and zero elsewhere. GR’s exact boundary proposition verifies that this USC function is classically psh, including scalar compatibility. Every neighborhood of the Gauss point contains all but finitely many whole residue discs. An uncountable collection of such directions defeats any pointwise continuous sequence on any fixed neighborhood. The obstruction also transfers to higher-dimensional products by an analytic section. When the residue field is countable, enumerated residue representatives and a smooth convex cutoff of j log|∏(T−a_i)| give actual decreasing ordinary CLD-smooth psh approximants on the entire fixed disc. This equivalence concerns the spike, not every target or a complete boundary characterization.

SUPPORT:
[]

TEXT:
Let K be complete, algebraically closed, and nontrivially valued. Put D=M(K〈T〉), let η be its Gauss point, and fix A>0. Define u(η)=A and u(x)=0 for x≠η. Since {η} is closed, u is upper semicontinuous. The analytic boundary of D is {η}, and u is zero on Int(D). GR arXiv:2506.13548v2 Proposition 3.5(3), whose literal scalar-compatible proof was checked, says u is subharmonic on D. GR 4.1.2 makes it classical psh. Thus the example belongs to the actual original starting class.

Residue directions. For each α in the residue field choose a representative a_α∈K° and let D_α={|T−a_α|<1}. These nonempty disjoint ordinary open discs partition D\{η}. Indeed, if a point has |T−a_α|=1 for every residue class, factor polynomials over K to see that its polynomial evaluations are the Gauss norms; approximation of Tate series by polynomials makes the point η. The ultrametric inequality gives uniqueness of the residue direction otherwise.

Every ordinary neighborhood of η contains all but finitely many whole D_α. A basic neighborhood uses finitely many Tate-series evaluations. A nonzero normalized series has a nonzero polynomial reduction because its coefficients tend to zero. Away from the finitely many roots of that reduction its absolute value is its Gauss norm throughout the corresponding residue disc. To verify this, translate by a_α: the constant term has full norm, while every nonconstant term multiplied by (T−a_α)^n has smaller norm on that disc. Thus finitely many evaluations exclude only finitely many directions.

Failure for uncountable residue. Suppose finite continuous v_j on an ordinary N containing η converge pointwise to u. Discard finitely many indices so that v_j(η)>3A/4. Continuity gives an ordinary neighborhood N_j⊂N of η with v_j>A/2. Each N_j contains every whole residue disc outside a finite exception set E_j. If the residue field is uncountable, choose α outside the countable union of E_j. At its rigid representative a_α all remaining v_j exceed A/2, contradicting u(a_α)=0. Neither decreasingness nor positivity was needed. In particular D fails P02.4 at its actual analytic boundary.

Higher-dimensional failure. On D×(P^m_K)^an, the projection pullback of u is classical psh by GR Proposition 4.2(6). Any continuous approximating sequence near (η,o), with o rational, restricts along the analytic section D×{o} to such a sequence near η. The preceding contradiction applies. These are good strictly analytic examples in every positive dimension of this product family.

Explicit countable-residue construction. Enumerate the residue field and choose representatives a_1,a_2,… . Choose a nonzero nonnegative smooth bump β supported in (−1,−1/2), and define
c=A/[∫(−t)β(t)dt],  χ(s)=c∫_(−∞)^s(s−t)β(t)dt.
Then χ is smooth, convex, nondecreasing, zero for s≤−1, and χ(0)=A. Put P_j=∏_(i≤j)(T−a_i) and v_j=χ(j log|P_j|), taking value zero at zeros of P_j. Away from zeros this is an ordinary smooth function of the logarithm of an analytic unit. On {|P_j|<exp(−1/j)} it is identically zero, proving ordinary smooth extension at zeros. These ordinary open representations agree on their overlaps.

Writing ℓ=j log|P_j| on the nonzero locus gives d′d″v_j=χ″(ℓ)d′ℓ∧d″ℓ≥0; on the constant neighborhoods it is zero. Thus these are ordinary CLD-smooth stage-zero psh functions. Current positivity is also valid on their boundaryless interiors; no unqualified boundary-current inference from CD §8.3 is made.

All log|T−a_i|≤0 on D. Consequently
(j+1)log|P_(j+1)|−j log|P_j|=∑_(i≤j)log|T−a_i|+(j+1)log|T−a_(j+1)|≤0.
Monotonicity of χ proves v_(j+1)≤v_j, also at zeros. At η every v_j=A. For x≠η choose i with r=|T−a_i|(x)<1. For j≥i, either P_j(x)=0 or j log|P_j(x)|≤j log r→−∞, so v_j(x) is eventually exactly zero. Hence v_j↓u on the entire fixed D.

Every analytic scalar extension preserves the polynomials, ordinary cutoff charts, positive Hessian formula, and decreasing inequalities. The pulled-back sequence converges to u∘π. If the new residue field is uncountable, this target is supported on the entire fibre π^(−1)(η), not just the new Gauss singleton, so there is no contradiction with the obstruction.

Sharpness and limits. Countability of the residue field is necessary and sufficient for this spike to admit the displayed ordinary smooth positive-form sequence. No characterization of all classical psh targets on countable-residue discs follows. This is an actual boundary obstruction, independent of harmonic ordinary-smoothness or residue-genus claims.

The complete proof and source application checks are retained in P02.4-argument.md, P02.4-paper.tex, and source-extracts/source-provenance.json. Rerun commands: python3 verify_sources.py and python3 build_and_check.py from the supplied workspace.

Artifacts: /workspace/research/campaigns/round-44/P02.4-public-source-decreasing-ordinary-smooth/artifacts/codex-QKCSac
