# Independent audit: uniform full-fibre FS extension and conditional envelope transfer

Date: 31 August 2026. Reviewer: `/root/p081_weighted_repair_fresh`.

The reviewer did not participate in the construction of this argument. The candidate was authored by `/root/p082_independent_reaudit` with substantive parent/root contributions, as its README discloses. This is an independent review of that candidate, not a production verdict or an audit of the entire supplied unibranch-envelope paper.

## Exact-byte verdict

No substantive mathematical gap was found in the two stated claims at these exact hashes:

- `statement.tex`: `4a758e5271862cad16c2242c5a2778c49de3cb4bff4797ff2a5d22ef0b00b503`.
- `proof.tex`: `f1b2014cbc612885421d1df26383f146809a0e621c43c98ea30993bf1f3ad3fa`.

Directory:

`/private/tmp/nappt_p071_20260827/manuscript/editorial/solver_dossiers_20260831/p081_uniform_fiber_extension_research_20260831/`

The extension proposition is independent of the envelope-property hypothesis. The transfer theorem is valid **conditional on the explicitly assumed BJ envelope property on the product in the specified ample classes**. The cited supplied paper asserts that hypothesis, but this audit does not re-certify its full proof.

This verdict does not remove the production sol/xhigh gate, authorize live integration, assert continuous-obstacle continuity, identify the target with CLD/BFJ classes, extend to nonconstant varieties or arbitrary complete fields, or retire an inventory/open-problem item.

The complete 76-line statement and 244-line proof were read, together with every candidate support file and the primary interfaces listed below.

## 1. Constant geometry and section lattice

The hypotheses are used exactly where needed. Since X is integral over algebraically closed k, its generic trivial valuation and corresponding generic Gauss extension are available without a component choice. Projectivity makes V=H⁰(X,mL) finite dimensional. Flat base change identifies H⁰(X_K,mL_K) with V tensor K; because the given K-section system generates, faithful flatness makes the full evaluation map of V generate mL over k. No relative section-algebra generation theorem is being assumed.

For every k-section, the trivial norm is at most one. A generating finite system has maximum norm exactly one. The same statement on the full fibre follows from the centre on the proper constant R-model and a norm-one model frame. At a proper-support point some sections can vanish, but at least one generating coefficient is a unit. Thus the all-points bounds do not silently discard points with nonzero kernel.

In a k-basis of V, the first nonzero Laurent coefficient of a section is a nonzero global section. In a generic rational frame it is a nonzero element of k(X), with trivial valuation zero. The generic Gauss norm is therefore exactly the maximum of the coefficient norms. In particular, norm at most one at this one point detects the lattice V tensor k[[t]]. This assertion is special to the constant finite-dimensional k-section space; it is not a model-lattice theorem for a general family.

## 2. Weight normalization and exact truncation

Writing λ_j=n_j+α_j with integer n_j and 0≤α_j<1, and replacing s_j by a_j=t^{-n_j}s_j, has the correct sign: |t^{-n_j}|=exp(n_j). The weighted maximum is unchanged. Its bound at the generic Gauss point implies that every a_j is integral, with order at least ceil(α_j).

For D=mC, the discarded tail starts at D+1. At every fibre point its weighted norm is at most exp(α_j−D−1), strictly less than exp(−D), hence strictly below exp(mf) because C≥M. The strict inequality persists even when C=M and regardless of the number of sections or the weight denominators.

The normed-line maximum argument then gives equality of the old and truncated finite maxima point by point. At an index attaining the positive maximum, a smaller error cannot change the norm; every other truncated term stays below that maximum. The proof uses the Gauss no-cancellation formula only to detect coefficient integrality, not at an arbitrary point where retained terms may cancel. Completed-residue-field convergence and the finite-basis tail estimate justify the infinite series also at proper-support points.

Thus the error really is zero on the whole fibre. There is no hidden accuracy-dependent increase of C.

## 3. Homogenization, negative padding, fixed twist

Every truncated section homogenizes in H⁰(S,mA), with A=p*L tensor q*O(C) and base degree exactly mC. The two padding systems q_ℓ U^{mC} and q_ℓ T^{mC} generate mA globally: one base coordinate is nonzero and the q_ℓ generate mL. This includes the central fibre and infinity, so the final weighted system is genuinely FS rather than a generically finite system with a surviving base locus.

Giving the padding weight −mC makes its fibre contribution at most exp(−mC), which cannot raise the existing maximum. Globally, all k-sections have trivial norm at most one and the padding maximum has norm one. The resulting bounds are −C≤Φ≤1/m≤1. The normalized weights are α_j/m or −C, hence lie in [−C,1), with absolute value at most C because C≥1.

Rational input weights stay rational. The optional tensor-power step for rational weights is also valid: after clearing their denominators, the integer weights can all be absorbed into powers of t, so the residual weights are zero. No real tensor exponent is used.

The fixed-reference adjustment is correct: ψ=ρ_K+φ gives −(M+a+b)≤ψ−a≤0. Extending ψ−a and setting H=Φ+a−p*ρ yields exactly φ on the fibre and −C≤H≤a+b+1. The underlying absolute metric is FS with potential Φ+a; H is correctly described as its relative potential, not declared an FS function relative to the trivial metric.

## 4. Full fibre and collar topology

The fibre of q at η is the analytic base change to the completed residue field H(η)=k((t)), not the image of the Gauss section. Temkin's fibre and affine-analytification constructions supply this identification at all analytic points. The evaluation description in the proof gives the usual fibre subspace topology. Equivalently, the natural continuous bijection from the compact projective analytification X_K^an to this Hausdorff fibre is a homeomorphism.

On 0<|t|<1, a nonzero base polynomial has a unique lowest term in valuation, so the base valuation is necessarily a·ord_0 with a=−log|t|>0. Jointly continuous positive scaling acts on all semivaluations of S, preserving support and centre. Scaling by 1/a therefore lands in the whole fibre F, and the displayed maps F×R_{>0}↔C are continuous inverses. This is a collar of the full analytic fibre, not a parametrization only of invariant/Gauss points.

The proof does not require the fibre inclusion to be open. It constructs an open ambient collar and then uses product neighbourhoods inside it.

## 5. Uniform radial control and usc regularization

For a normalized FS expression, comparing its finite maximum at ax with a times its maximum at x changes only the normalized weights β_j versus aβ_j. Their uniform bound gives |Φ_i(ax)−aΦ_i(x)|≤C|a−1|. Since Φ_i(x)=f_i(x) lies in [−M,0], the second bound with 2C follows. Terms with value minus infinity cannot spoil the maximum estimate because the systems generate.

Taking the supremum preserves this uniform radial estimate. The neighbourhood definition of fibre usc regularization supplies a fibre neighbourhood W on which the raw supremum is at most g(x)+ε. Its product with a sufficiently short radial interval is an ambient neighbourhood where the raw supremum is at most g(x)+2ε. This proves the nonformal direction of the claimed equality. Restriction of ambient neighbourhoods gives the other direction.

The argument is valid for arbitrary families and nonmetrizable F; it does not replace neighbourhoods or nets with sequences. The supplied topological counterexample without a uniform radial bound correctly explains why mere continuity of the fibre inclusion would be insufficient.

## 6. Ambient EP and restriction of approximants

The extensions all belong to one H_R(A), hence to the BJ psh class of c₁(A), and are bounded above by one. Also A is ample because L is ample and C≥1. The assumed EP therefore applies to their ambient regularized supremum Ψ.

The fixed-line-bundle interface is genuine: BJ22 Theorem 4.15(iii), together with Definition 3.8 and Example 3.9, gives decreasing H^dom(A) approximants inside H_Q(A), not merely FS approximants in nearby numerical classes. The source theorem is not restricted to characteristic zero.

Each generating section system remains generating after restriction to F. The factor U^{mC} is a norm-one frame there, and the restricted trivial metric from p*L is the constant-model metric on L_K. Hence each restricted expression is an FS potential on the actual fixed L_K. The restricted net decreases to Ψ|_F, already identified with the fibre regularized supremum. No independent target-field restriction theorem or envelope theorem is inserted.

## 7. Closure, product nets, and removal of the lower bound

The decreasing-limit closure of the target class follows from the cited abstract compact-space lemma with singleton class parameter. Its hypotheses are met: the FS potentials are continuous and stable under addition of arbitrary real constants. BE Lemma 7.4 gives the exact metric version; neither lemma assumes EP. Finite maxima follow by common tensor powers, concatenated section systems, and products of the individual decreasing nets.

For −M≤u_i≤0, every member of a decreasing FS approximating net is at least −M. The increasing open cover {u_{i,j}<1} of compact F gives a tail bounded above by one uniformly on F, for each i. After shifting by one, the bounded-FS result applies in a single class determined by M+1.

The coordinatewise product of the tail index sets is directed, with ordinary choice as stated. Its regularized suprema decrease and stay at least −M. They are all usc majorants of s=sup_i u_i, so their limit W majorizes s*. Conversely, each continuous majorant v of s can be met within ε by a sufficiently late approximant in every coordinate, uniformly on F by compactness. The resulting product index gives W≤v+ε, hence W≤v.

For bounded s on compact Hausdorff F, s* is the pointwise infimum of its continuous majorants. The bump-function proof is valid: on a neighbourhood where s* is less than s*(x)+δ the constant term already dominates, and outside it a sufficiently large nonnegative bump supplies the missing upper bound. Thus W=s*. No interchange of arbitrary infimum and supremum is presumed.

Finally finite maxima with constants preserve the target class, so lower truncations max(u_i,−M) are admissible. Maximum with a fixed constant commutes with usc regularization even at minus infinity. The resulting psh functions decrease to the requested regularized supremum. It is not identically minus infinity because the family is nonempty and it majorizes any chosen member. This is exactly the nontriviality condition needed for the final decreasing-limit closure.

## Primary interfaces actually checked

The inventory in this audit's manifest records exact paths, sizes and hashes for all source bytes. The PDF files were hashed, not newly rendered or visually reviewed. The following selected source statements/proofs were read directly in their matching extracted texts:

| Primary input | Directly read interface | Role and scope |
|---|---|---|
| BJ22, published version | Conventions; §§1.1.2, 1.1.4, 1.3; Remark 1.24 | Compact Hausdorff semivaluation topology, scaling, generic Gauss formula, trivial section norms. No use of Remark 1.9's full-image sentence. |
| BJ22 | Formula (2.8), Definition 2.18, (2.9); Definition 3.8, Example 3.9 | Real/negative weights, tensor powers, actual fixed-line-bundle FS representatives. |
| BJ22 | Lemma 4.6 with proof; Theorem 4.15 with proof; Definition 5.8 | Decreasing-net closure, fixed ample-class regularization, and EP rather than continuous-obstacle continuity. |
| BE, arXiv 1805.01016v3 | Definition 5.2, Proposition 5.4; Definition 7.2, Lemma 7.4 with proof, Corollary 7.5 | FS metric convention and the exact target decreasing-FS metric class over a complete non-Archimedean field. |
| Temkin, arXiv 1010.2235v2 | Fact 4.1.5.1, Definition/Exercise 4.1.7.1, §5.1.1 | Full analytic fibre, completed residue field, affine seminorm charts and analytification. |
| Supplied bj_envelope.tex | Introduction/main EP statements, preliminary BJ interfaces, smooth EP statement, final theorem and assembly proof | It asserts the ambient hypothesis for smooth integral S in arbitrary characteristic. Its entire internal EP proof is not re-audited here. |

The published/source hypotheses match the uses just listed. The proof does not use BJ22's characteristic-zero comparison to the nontrivially valued BFJ class, BE's later nef/psh comparison, or any continuous-envelope theorem.

## Mechanical evidence and remaining gates

The frozen candidate SHA256SUMS file has hash `97a7c2bacd9aeabd7eafc7ebce32cc4ba253a88c573f4317efd74ba62abda262`. All thirteen listed principal/support/primary-source entries were independently rehashed with zero mismatches. The read-only checker also tests principal-file control bytes, local label/reference resolution, and bibliography keys; these are not mathematical certification.

No change to the frozen candidate or a live manuscript was made. This audit did not compile a PDF and makes no compile or visual-QA claim. No production request or permission workaround was attempted.

There is no required mathematical repair identified in these exact principal bytes. Future presentation may add the compact-to-Hausdorff sentence above to make the fibre topology even more explicit, but that is not a condition of this no-gap verdict. Any subsequent change still requires exact-byte tracking. Production verification, acceptance of the explicitly imported ambient EP theorem as applicable, and any eventual manuscript assembly review remain separate gates.
