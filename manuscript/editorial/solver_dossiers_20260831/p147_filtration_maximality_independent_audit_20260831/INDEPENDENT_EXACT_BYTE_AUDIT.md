# P14.7 filtration maximality: independent exact-byte full-scope audit

Date: 2026-08-31. Reviewer: `/root/p082_independent_reaudit`.

Verdict: **PASS for the exact frozen theorem, its proof, the particular terminal corollary, and the stated elementary diagnostics.** No critical error or unresolved substantive proof gap was found. The theorem retains every strict-interior parameter of every decreasing, left-continuous, multiplicative, linearly bounded filtration of the full section ring of a big line bundle on a connected smooth complex projective variety. No ampleness, finite generation, nefness, or rational-parameter restriction was inserted to obtain this verdict.

This is a mathematical/source/assembly review, not production verification. The approval gate remains unchanged. No live chapter, inventory, old dossier, or candidate file was edited. No production call or permission workaround was made. P14.8 is not retired, and no novelty or priority is claimed.

## 1. Frozen inputs and independence

Candidate directory:

`/private/tmp/nappt_p071_20260827/manuscript/editorial/solver_dossiers_20260831/p147_filtration_maximality_research_20260831/`

| Frozen object | SHA-256 |
| --- | --- |
| `MANIFEST.json`, 12 entries | `3ffa1f46f96ce438bf46dd0159cd036f10e79437c1b242a688359b53d652b7fb` |
| `statement.tex` | `d6fca037467563e9af28d2ca97917eb1d2f5697c0b36d36f6a6217439bdd444c` |
| `proof.tex` | `865717efa134e64f113ccf3b57a339b657059bc2b0ee7368ee5b70dd9872a362` |
| `diagnostics.tex` | `969a55ac2a16374b3131d381d2b2d122f6d720dd4cc2ec7f85b8ed3c32883b8a` |

The principal text was authored by `/root/p081_weighted_repair_fresh`, not this reviewer. The reviewer did not supply the fixed-degree/conductor construction or edit its proof. Prior work by this reviewer on curve metrics, real-model density, and Gauss/fibre extensions is disclosed but is not an input. The previous P14.2 audit is logically independent. The root's preliminary review and the author's source ledger were not accepted as evidence of correctness. The present review independently checked all displayed inference chains and the relevant primary-source hypotheses.

The exact complete statement, 330-line proof, diagnostics, source matrix, source corrections, gate note, input ledger, syntax wrapper, bibliography and mechanical report were read. The separate later Finski addendum was read only as literature-status context; its full comparison is not part of this frozen-core verdict.

## 2. Definitions, normalization and quantifiers

The candidate's ordinary envelope is the normalized upper envelope of theta-psh competitors below zero with singularities at least as strong as the argument. Replacing obstacle zero with V_theta is legitimate: every theta-psh competitor below zero is already below V_theta. The I-envelope imposes the distinct multiplier-ideal condition. Neither definition identifies arbitrary bounded shifts with their normalized envelope.

Squared Hermitian norms, the factor 1/m and dd^c=i partial bar-partial/(2 pi) agree with DXZ and Berman. For nonzero finite-dimensional W_m, normalized evaluation is the dual norm of evaluation, whose square is continuous; its logarithm is theta-psh after division by m. Equivalence of norms gives an analytic **singularity type**, not a claim that the arbitrary sup-norm potential has a smooth analytic-singularity remainder. The proof uses only the type. The phrase about the logarithm of the dual norm is to be understood with the displayed squared-norm convention; all actual formulas have the correct square and factor.

Each raw finite-degree potential is at most zero, so its upper-regularized supremum is also at most zero. A zero section space gives -infinity, never an undefined normalized section. The dimension-zero case is correctly separated: any nonzero slice evaluates to zero at the unique point, and the strict-interior supremum has a nonzero degree. No positive-dimensional resolution or mass argument is incorrectly used there.

For positive dimension the fixed-degree estimate is first proved for an arbitrary multiplicative graded series with one birational degree. Its constants are allowed to depend on that fixed degree. Only afterward is it applied at a sequence of filtration degrees. No uniform estimate in the fixed degree, the parameter tau, or the smoothing index is needed or claimed.

## 3. Resolution, bounded residual obstacle and exact descent

Principalizing the base ideal of W_m over smooth X gives a smooth connected projective Y and mu^*(mL)=A+E, with E effective Cartier and a generating subspace V of A. The resolved map to its integral image is birational by the hypothesis on W_m. Thus A=f^*O_Z(1) is big and globally generated even though Z can be nonnormal and V need not be complete. A smooth semipositive Fubini--Study metric a exists from V.

The quotient metric on O(E) is smooth. With g=log|s_E|^2, the identities for curvature and dd^c g have the stated signs. On dividing evaluation by s_E, one obtains m mu^*u_m=g+v_m with v_m bounded continuous alpha-psh; generation prevents zero evaluation, and compactness bounds the residual norm above and below.

The obstacle chi=-g is bounded below, smooth off E and +infinity on E. A constant below its infimum is alpha-psh because alpha is semipositive. To check the less immediate upper bound, suppose admissible q_j have maxima tending to infinity. Their normalized versions q_j-sup q_j belong to an L1-compact family. On one fixed nonempty coordinate ball disjoint from E they are bounded above by a fixed constant minus sup q_j, so their L1 norms there tend to infinity. This contradicts the normalized compactness. Connectedness is used here. Hence all competitors have a common global upper bound.

The regularized upper envelope Q is therefore alpha-psh and bounded on both sides. Off E its regularization respects chi because chi is continuous; on E the bound by chi is automatic. Thus Q itself is admissible. No assertion that an arbitrary lower-semicontinuous obstacle is preserved everywhere by regularization is being made.

The identity mu^*P_theta[u_m]=(g+Q)/m is verified in both directions. If v is a normalized ordinary competitor, m mu^*v-g is alpha-psh off E and is locally bounded above near E by the singularity comparison with g+v_m. Removable singularities extend its local psh weights. The result is bounded by chi off E and automatically on E. Conversely, an alpha-psh q<=chi gives the mu^*theta-psh function (g+q)/m<=0. On the isomorphism locus of mu it descends; the local weights downstairs are bounded above near the exceptional image, because mu is proper and the weights upstairs are bounded above over compact neighbourhoods. Removable singularities extend them on smooth X. Pullback recovers the original psh weight by uniqueness from equality off a proper analytic subset.

Finally q has a global upper bound and v_m a lower bound, so the descended function is no less singular than u_m in the required direction. Upper envelopes agree on the isomorphism locus away from E, then as psh representatives everywhere. The proof never descends psh functions to the nonnormal image Z. It also never subtracts infinity from infinity on E: the difference is defined first off E and extended.

## 4. Quantization of the extended-real obstacle

The proposed weighted sup norm is finite since exp(g)=|s_E|^2 is a bounded smooth function. It is definite because its weight is positive off the proper divisor E; a holomorphic section vanishing on that nonempty open set vanishes identically. Every normalized section potential is an admissible competitor for Q, including at E where the obstacle is infinite. Consequently b_{chi,k}<=Q.

The functions chi_j=-log(|s_E|^2+1/j) are smooth and increase to chi. For any fixed admissible q and epsilon>0, the sets {q-epsilon<chi_j} are open: q is upper semicontinuous and chi_j continuous. They increase and cover Y, including E, because q is bounded above and chi=+infinity there. Compactness implies that one of these increasing open sets equals all of Y. Hence q-epsilon is admissible for Q_j=P_alpha(chi_j). Taking q=Q, which was proved admissible and finite, even gives Q-epsilon<=Q_j<=Q for all sufficiently large j. The weaker almost-everywhere conclusion used by the candidate certainly follows. There is no false Dini argument requiring q to be continuous.

For each fixed j, Berman Theorem 1.4 applies on smooth projective Y to the big line bundle A and the smooth metric a exp(-chi_j), with the fixed auxiliary line bundle trivial. No curvature positivity of this metric is assumed by the cited theorem. The equilibrium local weight relative to a is exactly Q_j. The theorem is applied to full sections of A^k, not to the original filtered system and not directly to the infinite obstacle.

The L2/sup conversion is correct. With volume normalized to one, L2 norm is at most sup norm. In local charts, the holomorphic mean-value inequality on a radius k^{-1} ball costs a factor k^{2n} for squared norms; multiplying a smooth metric's oscillation by k costs only a fixed factor. Thus sup norm is at most C_j k^n times L2 norm. The difference of normalized logarithmic evaluation weights is bounded by 2 log(C_j k^n)/k. Constants may depend on j, which is held fixed first.

Since chi_j<=chi, the smooth-obstacle unit ball is contained in the extended-obstacle unit ball, giving b_{chi_j,k}<=b_{chi,k}<=Q in the correct direction. Take liminf in k for each fixed j, then the countable supremum over j. Outside the augmented base locus and the null exceptional set of increasing psh regularization, the lower bound equals Q. This proves almost-everywhere convergence. No uniform convergence at E or continuity of Q is used. A countable union of the relevant null sets is harmless; there is no uncountable exceptional-set interchange.

## 5. Conductor return: exact inclusion, degree and norm

The normalization of integral Z is finite. The factor Y to Z^nu is proper birational with normal integral target, so f_*O_Y=nu_*O_{Z^nu}. All hypotheses of Stacks 0AY8 were checked, including the generic-fibre function field. The normalization quotient has zero generic stalk; its coherent annihilator c is a nonzero ideal and satisfies c nu_*O_{Z^nu} subset O_Z.

A high ample twist of c has a fixed nonzero global section b in c(r), with r>=1. Projection formula then gives the needed direction b H0(Y,A^k) subset H0(Z,O_Z(k+r)). This would not follow without the conductor. Serre vanishing for the projective embedding supplies homogeneous polynomial lifts of every element on the right in all sufficiently high degrees. Pulling back and restoring the exceptional factors gives precisely

`s_E^(k+r) b s in mu^*(image(Sym^(k+r) W_m -> W_(m(k+r))))`.

There is no assumed normality of Z, projective normality, surjectivity in all degrees, or finite generation of the entire graded series. The denominator is m(k+r), not mk. The exponent k+r on s_E is essential and is correct.

The fixed number B=sup |b|_{a^r} exp(rg/2) is finite and positive; the nonvanishing loci of b and s_E have nonempty intersection on integral Y. If the input complete section has weighted norm at most one, the returned section has original h-sup norm at most B, by the exact tensor-product norm identity. Proper surjectivity of mu equates the upstairs and downstairs sup norms. No norm bound for a polynomial expression or for a choice of lift is required: only the norm of the resulting actual section enters the original definition.

After division by B and taking evaluation suprema, the displayed lower bound is

`mu^*u_W >= g/m + (k b_(chi,k) + beta - 2 log B)/(m(k+r))`.

This is correct at every point outside E and the zero divisor of b. First hold m, r, b, B fixed and let k tend to infinity. The fixed degree overhead and logarithmic cost vanish; the right side tends almost everywhere to (g+Q)/m. The excluded analytic sets have measure zero. Transfer through the birational isomorphism locus and uniqueness/order of psh representatives give u_W>=P_theta[u_m] everywhere. In particular, the proof supplies a normalized function inequality, not merely matching dimensions, multiplier ideals, or total mass.

## 6. Filtration, ample series, and the dyadic source identity

For each fixed tau<c, BC Lemma 1.6 applies to the full big section ring with the stated bounded multiplicative filtration. Its ample subsystem implies that W_{m0 q} is birational for all sufficiently large q for one m0 depending on tau. Taking q=2^j is allowed. One does not assume that the arbitrary divisibility index m0 divides a dyadic integer.

The m0-th power of any norm-one section in W_{2^j} belongs to W_{m0 2^j}, remains norm at most one, and has exactly the same normalized evaluation logarithm. Thus u_{tau,2^j}<=u_{tau,m0 2^j}; applying envelope monotonicity and the fixed-degree estimate yields P[u_{tau,2^j}]<=u_tau for all sufficiently large j. This bridges the divisibility and dyadic indices correctly.

DXZ Lemma 4.5 and its proof were read directly and visually checked. They provide the increasing finite-level envelope identity, not the sought raw fixed point. To make its compressed closure step explicit, put psi_j=u_{tau,2^j}, p_j=P[psi_j]=P[psi_j]_I and chi=(sup_j p_j)^*. Fekete gives psi_j increasing almost everywhere to u_tau; analytic singularity type gives the finite-level equality by DX22 Proposition 2.20. Hence u_tau<=chi<=P[u_tau], p_j is increasing, and chi has positive mass.

The printed DX22 Lemma 2.21(iii) also assumes its limit is model, so positivity alone is not a complete recital of that lemma's hypotheses. The missing recital is a standard ordinary-model closure input, not the desired raw maximality: increasing quasi-psh sequences converge in capacity; mass semicontinuity and monotonicity ensure that the p_j have positive mass eventually; DDNL21 Proposition 2.6(i) then identifies their ceiling fixed points with P-fixed points, and Corollary 4.7 makes chi a P-fixed point. The sources and their exact hypotheses were checked independently. Equivalently, monotone capacity convergence follows from quasi-continuity, removing a set of arbitrarily small capacity for the countably many potentials and their pluripolar exceptional set, then Dini on the remaining compact set.

Now DX22 Lemma 2.21(iii) applies and makes chi I-model. The order u_tau<=chi<=P[u_tau] then implies P[u_tau]<=P[chi]=chi, so chi=P[u_tau]=P[u_tau]_I. This verifies the exact DXZ identity used by the candidate without presupposing u_tau=P[u_tau]. The candidate imports the identity directly from DXZ's proof; expanding this background in the audit is a source-precision note, not a substantive amendment or a new theorem assumption.

Taking upper regularizations of the established bound p_j<=u_tau gives P[u_tau]<=u_tau. The reverse inequality follows because u_tau<=0 is itself an ordinary competitor. The ordinary/I-envelope equality then supplies the second equality in the theorem.

The separate positive-mass justification is valid for the full strict interior: choose a<tau<b<c with u_a=V_theta at the bounded lower end. Concavity gives u_tau>=(1-t)V_theta+t u_b, where 0<t<1. Positivity and multilinearity of the nonpluripolar product give at least (1-t)^n times the positive volume of the big class; monotonicity under less singular potentials preserves this lower bound. No positive mass is assumed at the terminal point.

## 7. Endpoint and diagnostics

The terminal assertion uses only the prescribed DXZ left-limit convention. A nonidentically-minus-infinity decreasing limit u_c is theta-psh and at most zero. Since u_c<=u_tau for every tau<c, monotonicity of each envelope gives P[u_c]<=u_tau and P[u_c]_I<=u_tau. Taking the infimum over tau yields both envelopes <=u_c. Their reverse inequalities follow from admissibility of u_c itself. This works even when the top mass is zero, and does not invoke positive-mass increasing closure at the boundary. The identically-minus-infinity terminal slice is kept within the stated extended convention.

The bounded-shift diagnostic is correct: V_theta-1 has the same singularity type and every fixed-weight multiplier ideal as V_theta, while both normalized envelopes equal V_theta. Its curvature and nonpluripolar measure are unchanged. This refutes inference from singularity data alone, not the actual filtration theorem.

The blowup calculation is correct. The restriction of the j-th positive exceptional twist to E is O_E(-j), so all sections of mu^*O(md)+mE are divisible by s_E^m; no order-m vanishing is imposed downstairs. The exceptional order is m+mult_p(t). Counting monomials of total (x1,x2)-degree below ell gives ell(ell+1)/2 missing monomials. The candidate's dimension formula, normalized endpoint c=d+1, strict-interior volumes and linear terminal dimension md+1 follow. The independent checker repeats all 2436 finite arithmetic cases. The big globally generated pullback H has E in its augmented base locus but no base points, confirming the distinction used in the source corrections.

These diagnostics do not determine a normalized filtered envelope by themselves. The old 15 August universal exclusion and zero-mass hardness reduction were unsupported. Correcting them is logically separate from acceptance of the new proof.

## 8. Mechanical/source checks and final limitations

`check_exact_packet.mjs` verifies all 12 candidate manifest entries and four principal hashes, all six recorded historical inputs, 19 unique labels, 12 internal references, six bibliography keys, and absence of forbidden TeX control bytes. It independently enumerates the 2436 blowup cases. It reads and hash-checks the existing draft log and bibliography but does not execute any author script or rebuild anything.

The author's scratch log records eight draft pages with resolved references/citations and no substantive layout/syntax warnings. The expected pdfdraftmode warning is present. There is no candidate PDF and therefore no candidate-PDF visual acceptance. Only the relevant existing DXZ source pages were rendered and visually inspected by this reviewer. Berman, BC, Stacks, DX22 and DDNL primary interfaces were checked in the forms precisely disclosed in `SOURCE_LEDGER.md`; no nonexistent local PDF hashes or successful visual inspections are invented.

No unresolved mathematical gap remains in the frozen core. Optional editorial precision is to expand the standard model-closure input behind DXZ Lemma 4.5 and say 'logarithm of the squared dual evaluation norm'; the displayed formulas and invoked exact source identity are already correct. These are not restrictions of the theorem's scope.

The separate Finski addendum says a newer preprint covers the deduction. This review makes no independent priority determination and does not use that preprint to justify the candidate. The core's mathematical pass is compatible with a literature-covered status. Any promotion should retain exact attribution and the separate production/editorial gates.

The result concerns big line bundles and actual filtered section-ring data on smooth projective complex varieties. It does not prove an MP cone comparison, an arbitrary transcendental pseudoeffective extension, a general zero-mass reconstruction theorem, or a general envelope property. In particular, the terminal-left-limit corollary is not authorization to retire P14.8 without a separate exact formulation and scope review. This verdict binds only the hashes in Section 1; later changes require a new exact-revision check.
