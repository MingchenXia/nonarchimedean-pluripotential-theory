# Exact after-patch independent review

Date: 2026-09-01. Read this together with `AUDIT_REPORT.md` for provenance and exclusions.

## Exact reviewed bytes and bounded verdict

- Ch16, 223897 bytes, SHA256 `41333978fbce28644d1f63aac6431f763dd3f3cc1dd792faf1b20b43ab3a9e83`.
- Ch19, 210866 bytes, SHA256 `4d59d219eec46bea029d6d131e6f55c110a7fbf4c3f30be9dcf4147a4c5a6652`.

Full paths and exact before/after excerpts are in the input/evidence files. The root authored these working-tree revisions. This auditor read their entire diff and the relevant book and primary-source interfaces. No substantive gap was found in the changed arguments, conditional only in the ordinary sense of using the existing named book theorems as inputs. This is not a fresh audit or production acceptance of those foundational inputs.

## A. Ch16 multiplier warning, revised lines 1625–1635

The warning now correctly distinguishes positive multiplication from closedness. Its displayed smooth Leibniz identity is valid for closed `T`. It does not claim that a merely continuous `f` possesses an ordinary differential; instead it uses the smooth case to show why arbitrary approximation is insufficient. It preserves the proven locally constant corollary and makes no assertion about the old additional condition `fT` closed.

The single actual consumer only multiplies by a locally constant nonnegative function. No consumer requires the deleted strengthening.

## B. Ch16 harmonic continuity, revised lines 2377–2405

The proposition explicitly assumes `u_i^a,u_i ∈ CPsh_X` for every inner factor `1≤i≤q`. The outer multiplier `u_0^a` only needs continuity and local uniform convergence, as in the standard continuity theorem. The continuous image of a source compact is compact, so the target convergence gives the needed source convergence. The proof is now a direct application of `thm:cld-bt-continuity` and does not make a recursive assertion about all harmonic-chart G-form products.

The explanatory paragraph accurately identifies the missing hypothesis in the more general source argument. It neither announces that all instances of the source continuity statement are false nor treats its citation as an independent proof.

## C. Ch16 fixed skeletal Bedford–Taylor current, revised lines 3847–3879

Let `T` be the stated skeletal Bedford–Taylor current and `u_j=F_j∘f`, where convolution on the entire target gives smooth convex `F_j→F` locally uniformly. Continuity and convexity of `F` on all of finite-dimensional real space suffice for these mollifications; no growth bound at infinity is used on a compact test support.

The Hessian of `F_j` is positive semidefinite, so its pulled-back (1,1) G-form is positive. Harmonic compatibility for **the fixed T**, first for the zero-form `u_j` and then for `d''u_j`, gives

`d'd''(u_j T) = T ∧ d'd''u_j ≥ 0`.

No intermediate current is asserted to satisfy the same hypotheses. Exactness gives both separate closedness conditions. As `u_j→F∘f` locally uniformly, `lem:continuous-times-positive-current` with the constant net of positive currents `T` gives `u_jT→(F∘f)T`. Differentiation of currents is continuous. Positivity and closedness persist in this limit. Thus the revised conclusion is exactly what the proof establishes.

The paragraph explicitly declines ordinary smooth/local-approachable and arbitrary-current conclusions. Its reference to the analytic strict-PL alternative is supported by CLD 18.8.9 and is concretely implemented in Ch19.

## D. Ch19 canonical positivity, revised lines 2617–2676

### D1. Original-field hypotheses and the formal term

The theorem already assumes nontrivial valuation and the chapter's actual split Raynaud data over its fixed field. The analytic spaces `B` and `E` here are separated and boundaryless. The metrics supplied by the formal bundles are strictly integral parlinear, in particular integral parlinear. The existing `thm:ch17-psh-residual-nef` therefore has the required scope. Its residual-bundle functoriality gives the pullback of a nef residual bundle; it supplies ordinary pshness of `q^*M`, not just a statement in a weakly smooth/delta form theory.

The replacement of both GK references is necessary and appropriate: the former named Ch18 theorem explicitly requires algebraically closed `K`. No scalar extension or descent of an arbitrary current is used by the new proof.

### D2. The two signs of each coordinate

`prop:ch19-tau-coordinates` supplies integral parlinearity of every lattice coordinate `h_j` and the current identity `d'd''[h_j]=0`. Hence the trivial metrized line bundles with weights `h_j` and `-h_j` both have zero, thus positive, first Chern current. The Ch17 equivalence proves each weight ordinary psh near every point. Membership is a sheaf condition, so these weights belong to ordinary CPsh on the fixed whole space `E`.

This is not an invocation of the revised Ch16 fixed-current corollary to infer pshness. It is the separate analytic residual-line-bundle argument. Arbitrary real affine combinations of the coordinates are CPsh because each signed coordinate is CPsh, and the cone is closed under finite nonnegative sums and contains all real constants. Negative scalar coefficients cause no difficulty: use the positive coefficient multiplying `-h_j`. Zero coefficients are omitted.

### D3. Quadratic normalization

The metric decomposition uses `F=q_L/2`. In the implication under consideration its Hessian `H` is a constant positive semidefinite matrix. For the tangent affine function at `a`,

`ℓ_a(t)=F(a)+∇F(a)·(t-a)`,

the identity

`F(t)-ℓ_a(t)= (t-a)^T H(t-a)/2`

is exact, including the factor one half. The operator-norm bound is valid in a chosen Euclidean norm. Every tangent is a global supporting affine function even when `H` is singular. No strict convexity or inverse of `H` is required.

### D4. Fixed-neighbourhood uniform convergence

For any chosen compact analytic neighbourhood `K` inside `E`, take a finite ε-net in the compact target set `τ(K)` (or any fixed compact set containing it). At every point of that set, at least one selected tangent has error at most `||H|| ε²/2`; every tangent is below `F`. Consequently the maximum of these finitely many tangents satisfies the same uniform error bound.

Each finite maximum pulls back to an ordinary CPsh function on **all of E**, by D2 and `cor:ch16-max-psh`. Taking, for example, ε=1/j gives a sequence defined on the same fixed neighbourhood, uniformly convergent on `K`. The existing local uniform-closure theorem implies pshness of `F∘τ` on the interior of `K`. Such interiors cover `E`. There is no ε-dependent shrinking domain and no passage from a G-smooth approximation to ordinary smoothness.

This interpretation is exactly the local argument in the reviewed paragraph; it does not assert that choosing one net on one compact automatically yields convergence on every other compact. Either work on one fixed neighbourhood at a time, as the text says, or exhaust the target if a single global sequence is desired. Only the former is needed.

### D5. Rank zero and the full metric weight

For `r=0` the target is a point and the function is constant; the proof explicitly treats this case. For `H=0` in positive rank, all tangents agree with the affine function and the error is zero.

The actual weight in `eq:ch19-canonical-weight` is `f`, not just `F`. The final bytes explicitly state that `f-F` is real affine and use D2 to show its pullback psh. Thus `f∘τ` is psh, and the sum of its weight with the psh formal metric weight gives `p^*L` psh. The already available local analytic sections of `p` descend this local pshness to `L`. No affine term is lost.

The reverse implication's final formal-curvature-to-nef step also uses the correctly scoped Ch17 theorem. The remainder of that old implication was not rewritten in this repair and is not being globally re-certified here.

## E. Preservation and remaining status

The canonical-positivity theorem statement is byte-for-byte unchanged. Every Ch16 and Ch19 label is retained, with no new label. The narrowed Ch16 statements are explicit corrections, not concealed changes in the scope of Ch19. The root's source triangulation concern is avoided by the displayed tangent-max proof.

There is no required further change to these exact corrected arguments. The one leftover citation-range imprecision at Ch16:1559 is separately recorded in the main report. This review does not convert any open continuous-harmonic multiplication problem into a theorem and does not remove a research verification gate.
