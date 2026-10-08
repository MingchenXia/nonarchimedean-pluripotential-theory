Use n1's ordinary products and signed coefficient measures. Let F(O)⊂C(O,R) be a restriction-compatible class of finite functions. A positive doubly closed T is BT for F if on EVERY ordinary O, all u,v∈F(O) with D[u]=D[v] satisfy D((u-v)T)=0. Initial BT is an explicit transfer hypothesis. The original individually continuous psh class can be used without replacing it by generated CPsh.

Multiplication compatibility is proved by measures. For smooth β and a complementary compact test ω,
⟨β∧(hT),ω⟩=∫h dμ(T,β∧ω).                              (6)
T has even total degree. If β∧T=0, evaluate on fω for every smooth scalar f. Uniqueness forces μ(T,β∧ω)=0 and thus β∧(hT)=0. For a smooth scalar a, uniqueness gives μ(T,aθ)=a μ(T,θ), hence a(hT)=(ah)T. If C=γ∧T is positive, its coefficient measure equals μ(T,γ∧ω), so
hC=γ∧(hT).                                               (7)
For continuous a≥0 the same argument with positive aT gives h(aT)=(ha)T. No continuous wedge on an arbitrary signed current is invented.

For any current S and smooth β of total degree b, signed transposition gives
d(β∧S)=dβ∧S+(-1)^b β∧dS, d=d',d''.
Indeed commuting β past a total-degree-m current gives (-1)^{bm}; transposing differentiation gives (-1)^{m+b+1}; expanding d(β∧ω) on each compact test yields exactly those signs. This is the correctly indexed CLD7.7.7 calculation and assumes no closedness of S. For a smooth (k,k)-form γ the full second derivative is
D(γ∧S)=Dγ∧S-d''γ∧d'S+d'γ∧d''S+γ∧DS.                    (8)

Suppose T and C=γ∧T are both doubly closed. First-order Leibniz gives d'γ∧T=d''γ∧T=0. Differentiating the second relation gives Dγ∧T=0. For S=hT, the measure argument inherits ALL THREE annihilators. Differentiate d'γ∧S=0 by d'' and d''γ∧S=0 by d'; the form factors have odd total degree, giving
0=-Dγ∧S-d'γ∧d''S,
0=Dγ∧S-d''γ∧d'S.
Both cross terms in (8), and its Dγ term, therefore vanish. Thus
D(γ∧(hT))=γ∧D(hT).                                      (9)
The calculation explicitly allows hT to be nonclosed. For a scalar a it reads D((ah)T)=aD(hT), provided aT is doubly closed.

Consequently, for initial BT T, the actual smooth-factor product C=γ∧T is BT exactly when it is positive and doubly closed. Necessity is part of the definition. For sufficiency restrict to arbitrary ordinary O, take an admissible pair, and combine initial D(hT)=0 with (7) and (9). γ itself need be neither positive nor closed. Its actual product must be positive; closedness means precisely d'γ∧T=d''γ∧T=0. Require p+k≤n; for the nontrivial original degree range require p+k≤n-1. Degree n has no Hessian tests. Smooth a≥0 is allowable exactly when aT is doubly closed.

Fixed-T scalar nets: if locally smooth a_i≥0 converge locally uniformly to continuous a, and EVERY a_iT is doubly closed for the FIXED initial BT T, then aT is positive and closed by n1's measure convergence and transposition. For an admissible h on an arbitrary ordinary subopen and compact detector ω,
⟨D((a_i-a)hT),ω⟩=∫(a_i-a)h dμ(T,Dω)→0,
because the measure is finite and h bounded on its compact support. Each approximating BT identity is zero; locality completes the every-open conclusion. Arbitrary scalar smoothing supplies none of the required closedness equations.

Common-chart form nets: suppose every smooth γ_i∧T is positive and doubly closed, and γ_i converges in coefficients on compact supports in a FIXED finite family of common moment charts to a SMOOTH γ. Localize each test and expand in finite exterior monomial bases. Each monomial times the localized test has a fixed finite signed coefficient measure of T. Uniform coefficient convergence gives weak convergence of the products. Apply the same argument to d'ω and d''ω to get closedness; use positive tests for positivity. For BT apply it to Dω with the fixed bounded scalar h, then use (7). This constructs no nonsmooth wedge, changing-chart theorem, or arbitrary-current density.

The closedness diagnostic is an actual analytic example. Let X=(G_m,Q_ell²)^an, s_i=-log|T_i|, and a=2+s_1². X is good separated strict boundaryless pure dimension2. Its δ_X is positive doubly closed and tautologically BT. Nevertheless
D(aδ_X)=[2d's_1∧d''s_1].
For nonzero ζ≥0 smooth compact on R², ω=ζ(s)d's_2∧d''s_2 is an actual compact smooth upstairs test: its support lies in a compact closed analytic polyannulus. The identity moment has finite-flat degree1; CLD14.3.1–5,14.5.2–3 and5.8.4 give standard calibration and paired positive orientation. Hence
⟨D(aδ_X),ω⟩=2∫_{R²}ζ(s) ds_1 ds_2>0.
Thus aδ_X is INELIGIBLE as an original P21.3 current. This diagnoses the missing closedness premise in literal CLD8.6.7; it is not an original counterexample. Conversely S=(d's_1∧d''s_1)∧δ_X is positive closed BT, and d'a∧S=d''a∧S=0 by repeated generators, so aS is closed BT. Nonconstant relative weights are allowed.

The entire scalar367 and relative368 statement chains are reconstructed after replacing their unsupported strong-cone steps with n1's middle-cone construction. The repaired whole372 chain retains initial BT, actual product positivity/double closedness, every approximant's equations, and the smooth common-chart form limit. CLD8.5.5's generated-CPsh proof is not substituted for full original psh recognition; no arbitrary-current exhaustion follows from the printed closure propositions.

Artifacts: P21.3-review-paper.tex, P21.3-proof-companion.md, and independent-whole372-verdict.json. Rerun python audit.py and python build_review.py. No supplied program was executed or imported.