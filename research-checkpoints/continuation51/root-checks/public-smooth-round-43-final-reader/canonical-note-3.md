ID: n3

SUMMARY:
Draft noninvariant higher-dimensional sector: all arbitrary classical psh functions on saturated proper connected-fibre domains with local sections over the curves of n2 descend and regularize on one fixed saturated ordinary neighborhood. Singular fibres are allowed. Nonsaturated affine germs remain outside the result.

DETAILED SUMMARY:
Proper connected fibres force extended-real classical psh functions to be constant by the maximum principle over completed residue fields. Local analytic sections make their descended base functions classical psh. Pulling back n2 gives weakly smooth positive decreasing sequences and compatibility with all analytic scalar extensions. Products with projective space or connected nodal projective curves give actual higher-dimensional examples without torus invariance. The domain quantifier is essential: this covers every function on each saturated domain, but not every sheaf germ on arbitrary smaller opens.

SUPPORT:
["n1", "n2"]

TEXT:
Draft theorem. Let K and C satisfy n2. Let f:X→C be proper and surjective, with nonempty geometrically connected analytic fibres and analytic sections on an ordinary open cover of C. Assume X is Hausdorff, good, strictly analytic and pure of dimension d≥2. For every ordinary open D⊂C and every arbitrary classical psh u on the saturated domain f^{-1}(D), each x has one fixed ordinary neighborhood f^{-1}(V), f(x)∈V⊂D, carrying finite weakly smooth classical psh functions w_j with positive strong curvature currents and w_j decreasing pointwise to u. For finite continuous u the convergence is locally uniform. Every analytic scalar extension pulls back the same sequence with these properties. Neither normality nor smoothness of the fibres is required.

Proof of fibre constancy. For c∈D pass to the completed residue field H(c). GR scalar stability and pullback make the restriction of u to X_c classically psh. The proper connected fibre is compact and has empty analytic boundary. If u is not identically minus infinity there, upper semicontinuity gives a finite attained maximum M. Its maximum set is nonempty and closed; GR Theorem 6.1 makes it open because every fibre point is an analytic interior point. Connectedness makes it the whole fibre. If the restriction is identically minus infinity, it is already constant. This proves constancy on every fibre, including those over nonrigid base points; no density argument is used.

There is therefore a unique a:D→R union {-infinity} with u=a∘f. On each ordinary open possessing a section s, a=u∘s is upper semicontinuous and classically psh by GR pullback. These definitions agree on overlaps by fibre constancy. Ordinary sheafiness gives a classical psh base function a. Apply n2 at f(x), on a fixed V, and define w_j=v_j∘f.

The requested harmonic smoothness is explicit. A local harmonic preform (h,alpha) for v_j pulls back to (h∘f,alpha). GJR 7.6 preserves the integer harmonic coordinates. Equality on overlapping charts is pulled back through the joint chart (h,h'), as in GJR Definition 10.3 and Proposition 10.9. The zero-curvature and positive-Hessian descriptions established in n2 pull back; over the constant neighborhood of a singular base point the curvature is zero. The integration argument in n2 proves positive strong currents. Properness gives empty relative boundary, and the boundaryless base gives empty absolute boundary for X and f^{-1}(V), so the current argument has no boundary residues.

For any analytic extension L/K, let p:X_L→X. On the fixed ordinary domain p^{-1}(f^{-1}(V))=f_L^{-1}(V_L), the sequence is w_j∘p. At each z its values decrease to u(p(z)). Harmonic coordinate pullback, the scalar positivity proof in n2 and GR scalar stability prove the other assertions. This is extension of one base-field sequence, not descent of arbitrarily chosen extension-field approximants. If u is finite continuous, its restriction through local sections makes a finite continuous; compact images under f transfer the local uniform convergence of v_j to w_j.

Concrete examples are F^an×C with F geometrically connected and proper, possessing a K-point, and with the displayed product pure-dimensional. A point of F supplies a section. F=P^m gives dimension m+1. A geometrically connected reduced nodal projective curve F gives a singular surface when C is a curve. For C=A1^an, log|T-a| pulled back from the base, a≠0, gives a classical target with a genuine pole; on a torus open it is generally not maximal-compact-torus invariant. The theorem assumes no torus invariance of any target.

The saturated-domain restriction is indispensable to this proof. On an affine chart of P^m×C, log|Z_1| is classical psh and varies along the affine fibres. Those fibres are not the compact proper fibres used above. Consequently this result cannot be advertised as regularization of all sheaf germs on the product or as a characterization of the original higher-dimensional local property.

The mathematical proof and limitation are retained in P02.3-argument.md, Section 4, and standalone P02.3-paper.tex. Rerun python3 make_paper.py and python3 build_paper.py. Successful builds do not verify fibre constancy, descent or the new proof.

Artifacts: /workspace/research/campaigns/round-43/P02.3-public-source-decreasing-weakly-smooth/artifacts/codex-4O8X0J
