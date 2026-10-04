ID: n2

SUMMARY:
Published partial theorem: with positive characteristic and trivial valuation, the genuine E1 operator exists in every dimension; arbitrary-support finite-energy measures have unique solutions on smooth projective varieties of dimension at most two. This does not solve the nontrivial valuation axis.

DETAILED SUMMARY:
Apply Boucksom–Jonsson 1801.08229v4 over algebraically closed trivially valued k of characteristic p>0, smooth connected projective X and ample L. The canonical trivial reference has raw mass V=(L^n). The exact measure condition is sup_H{V E(u)−∫u dμ}<∞ and μ(Xan)=V. The finite-energy pairing defines an approximation-independent genuine MA measure. Comparison and injectivity hold in every dimension. Unconditional positive-characteristic surjectivity uses envelopes proved for dim X≤2, resolving test configurations of dimension n+1≤3 and replacing multiplier ideals with test ideals. Higher-dimensional surjectivity remains conditional on the envelope property.

SUPPORT:
["n1"]

TEXT:
This is an application of the published theorem in Boucksom–Jonsson 1801.08229v4, not a new solution of P16.3.

Hypotheses: k is algebraically closed of characteristic p>0 with trivial absolute value; X/k is smooth, connected and projective, dimension n≥1; L is ample. Fix the canonical trivial reference metric ρ, write ω=c1(L) and V=(L^n)>0. PSH(L) consists of nontrivial usc decreasing limits of Fubini–Study functions m^{-1}max_i(log|s_i|+λ_i), using basepoint-free sections of mL and rational λ_i. Weak convergence means convergence at divisorial valuations. E(u)=(ω,u)^{n+1}/((n+1)V), extended monotonically, and E1={E>−∞}. Raw energy is V E.

The exact measure condition is positivity, μ(Xan)=V, and E*raw_ρ(μ)=sup_H[V E(u)−∫u dμ]<∞. For ν=μ/V this equals V E∨(ν), and the supremum equals that over E1. To prove this passage, take u_j∈H decreasing to u∈E1. Then E(u_j)→E(u), while ∫u_j dν≥E(u_j)−E∨(ν). Monotone integration of usc functions on compact Xan gives convergence of the integrals; their uniform lower bound proves u∈L1(ν). Every E1 expression is therefore a limit of model expressions. The reverse supremum inequality follows from H⊂E1. Constant tests give c(V−μ(Xan)); rational constants already force exact mass V whenever raw dual energy is finite. No restricted measure is renormalized.

Construction: use the finite-energy multilinear pairing of Theorem 7.14, whose existence and monotone continuity are published inputs. On PL tests define T_u(f)=(0,f)·(ω,u)^n. Theorem 7.18 gives positivity, T_u(1)=V and |T_u(f)|≤V||f||∞. PL density in C0 and Riesz representation give a unique positive Radon measure MAraw_ρ(u). Pairing continuity gives convergence against every PL test for any decreasing model approximation; the uniform bound extends convergence to all continuous tests. Thus the limit is approximation-independent. Proposition 7.19 identifies the model case with Σ_F b_F((ω_𝓧+D)|_F)^n δ_{v_F}, proves raw mass V and finite-energy integrability. Theorem A supplies strong continuity and dense image in finite-energy measures in every dimension.

Locality is Theorem 7.40 on {u>v}. Apply it to max(u,v−ε), using positivity and mass V, to obtain ∫_{u<v−ε}MAraw(v)≤∫_{u≤v−ε}MAraw(u). Infinite loci are null by finite-energy integrability. Let ε decrease to zero to obtain comparison: ∫_{u<v}MAraw(v)≤∫_{u<v}MAraw(u). Equal MA measures give I(u,v)=0. Corollary 10.4 uses divisorial energy estimates and divisorial determination to infer that u−v is locally constant; connectedness gives one constant. Injectivity holds in every dimension.

For n≤2, Theorem 5.20 proves the envelope property in characteristic p. The proof reduces obstacles to PL functions, represents envelopes by normalized base ideals, resolves a test configuration of dimension n+1≤3, then uses test ideals for subadditivity/global generation. The resulting estimate forces uniform convergence of nef approximants. Resolution and test-ideal results are background used by the published theorem, not new unrestricted claims. Actual PDF page 62 distinguishes dim X≤2 from dim 𝓧≤3; page 63 states the test-ideal replacement.

The envelope property gives normalized weak compactness by Theorem 5.11. For finite-energy ν, take a maximizing sequence for Fν(u)=E(u)−∫u dν, normalized to sup u=0. Lemma 9.15 and Corollary 9.16 bound J(u)=sup u−E(u). Compactness gives a subnet limit; upper semicontinuity of energy puts that limit u in E1. Proposition 9.19 supplies L1(ν) convergence. Consequently Fν(u)≥limsup Fν(u_j)=E∨(ν), so u actually attains the supremum.

Theorem 8.5 gives E↓(u+tf)=E(u)+t∫f MA(u)+O(t²) for PL f, uniformly in u. With the envelope property E↓ is envelope energy. For maximizing functions with defect δ_j→0 this gives t∫f MA(u_j)≤t∫f dν+δ_j+C_f t². First let j tend to the limit, then t decrease to zero, and repeat with −f. The constant maximizing sequence u_j=u proves MA(u)=ν; multiplying by V proves MAraw(u)=μ. This is the applicable variational argument of Theorem 12.8 and the positive-characteristic conclusion of Theorem 12.9.

Therefore every arbitrary-support positive Radon measure of raw mass V and finite raw dual energy has a unique finite-energy solution on these smooth projective curves and surfaces. Continuity of the solution is not asserted. For n≥3, operator construction, comparison and injectivity remain established, but surjectivity is conditional on the envelope property. This endpoint does not apply to arbitrary varieties over F_p((t)) or Q_p.

The full cited argument is in P16.3-argument.md, Section 3, and standalone P16.3-paper.tex. Literal proofs and actual PDF checks are retained in source-extracts/source-provenance.json. Rerun generation/build: python3 build_and_check.py.

Artifacts: /workspace/research/campaigns/round-47/P16.3-public-source-positive-residue-characteristic/artifacts/codex-69HHDl
