# Fresh independent mathematical audit: Ch20/21 real versus rational model maxima

31 August 2026. Auditor: p213_skeletal_hostile. Author of the reviewed repair: root.

## Verdict and boundary

The new mathematical repair is sound on its stated original BFJ scope: rational model functions are closed under finite maxima for an arbitrary real closed model form; real psh model functions in an ample generic class can be approximated uniformly by rational psh model functions at the exact same form; this supplies the corrected envelope and full-PSH maximum arguments. No rationality assumption on the reference form has been introduced.

The original assembled packet nevertheless retained three local defects requiring correction: a denial of ample-cone openness used by the new proof, a refinement example claiming non-affineness without a genuine crossing hypothesis, and an incorrect BFJ lemma locator. These do not refute the repaired mathematical mechanism. The separately frozen revised1 addresses them; see REVISED1_EXACT_BYTE_ADDENDUM.md.

This review is independent of the development of the fixed-form-density and maximum repair. The auditor did not author that repair or these new proofs. The previously audited weighted Ch20 changes are retained inputs, not a fresh certification of the whole chapter. The Ch21 curve-retraction subsection remains outside this review and explicitly gated. No statement here certifies all of Ch21, Ch24 locality, Ch30 descent, or any arbitrary-field envelope theorem. No production submission or live integration was performed.

## Exact original input

Directory:
/private/tmp/nappt_p071_20260827/manuscript/editorial/solver_dossiers_20260831/p081_ch20_ch21_real_model_max_repair_20260831/.

- Full Ch20: 180714 bytes; SHA256 `7b287229f071aceeaa8396a8ea00bd6f6d70a566f67bdd452fc72bd2281fb586`.
- Full Ch21: 167372 bytes; SHA256 `957e2a2d16ff85c036aa42c1647aa055f56767fb9973a02b34d4853899d39310`.
- rational_approximation.tex: 5492 bytes; SHA256 `f857bbc52b34d75e9dcd3047fa0b55c79a052d7377732ce61f8d7038984b1572`.
- truncation.tex: 944 bytes; SHA256 `f3571d0f914f62c28cf4d5bd2d87765accf42337e6831de591b475265c9cdb3f`.
- envelope_directedness_proof.tex: 1422 bytes; SHA256 `0194587aca9555c20b4cd9783a65829a8919b78a0946d26cf362cd7a809cdf2c`.
- Original author manifest: 8471 bytes; SHA256 `c93d77d0cef6bec9b16ffe9ff3f499cae581237553f72872b87ee7f2bbc4421e`.

The original Ch20 is assembled on the already weighted/unit-node follow-up, SHA256 `bc479b67a29261f001d0409656e150bc3bf9441dbdf1ff90fb4298fe3c1ad414`, not directly on the live unweighted Ch20. The original Ch21 source is the live file, SHA256 `477db8e896633bcf5f89c8738e16e0afa8eaac55f36042c1d263b683daed72b3`.

## Hypothesis and convention check

The standing hypotheses are complete discretely valued \(K\), residue characteristic zero, \(v_K(\pi)=1\), and smooth connected projective \(X/K\); models are normal flat projective \(R\)-models. Connectedness is not silently replaced by geometric connectedness. The primary source has this same connected, not necessarily geometrically connected, scope.

Here \(\mathcal D(X)\) means the rational model space and \(\mathcal D(X)_{\mathbf R}\) its real linear extension: elements are finite real combinations of integral vertical Cartier divisor functions on one common model. This is not the space of all continuous functions that happen to be piecewise affine on an arbitrary real subdivision. In particular, real coefficients do not create irrational breakpoints.

The repaired rational-maximum proposition assumes neither generic ampleness nor semipositivity of the reference itself. It assumes that the input functions are psh at that reference. A vacuous input family causes no logical difficulty. The new fixed-form-density lemma assumes generic ampleness, but does not assume the real reference is semipositive or rational. The elementary envelope theorem assumes a semipositive reference; its added ampleness condition is confined to equality with the rational-family supremum and the resulting increasing-net representation. Its other assertions keep the original weaker hypothesis.

## Required corrections in the original assembled bytes

1. Original Ch20, special-fibre-test proof, lines 346–350, and adjacent cone-usage paragraph: the text denies needing or asserting relative ample-cone openness. The new density lemma explicitly uses it, and the lemma statement itself already calls the ample cone open. The needed fact is true: under the numerical restriction embedding with image \(V\), the relative ample cone is the intersection of \(V\) with the ample cone of the special fibre, hence is open in \(V\). Surjectivity of the restriction embedding is neither true in general nor necessary.
2. Original Ch20, ex:ch20-max-fails-naively, lines 2345–2354: the maximum of two affine functions need not be non-affine. Identical functions, or one dominating the other throughout a face, are immediate counterexamples to the unqualified sentence. Require a genuine crossing on that face. The repaired inequality placing a convex maximum below its affine vertex interpolant has the correct sign.
3. Original Ch21, lem:ch21-model-skeletal-properties, line 792: BFJ Lemma 5.3 is not the cited relative-ideal approximation. The pertinent statement is Lemma 5.7 in §5.2; 5.3 is a different corollary. This is a locator error, not a failure of the ideal approximation.

The first issue was identified in this fresh audit; the crossing defect reported in parallel was independently confirmed. The locator was checked directly against the primary PDF and text. None licenses changing the frozen original files.

One additional inherited wording issue is recorded explicitly: in Ch21's rational skeletal-proof Step 1, the phrase “on which D is Cartier” must be read as “on which D is a rational Cartier divisor,” or be preceded by clearing denominators. A rational model function need not admit an integral Cartier representative on a domination: the constant 1/2 already prevents that on a model retaining a multiplicity-one component. The proof only needs a rational Cartier divisor and later multiples; BFJ Lemma 5.7 states exactly that rational-divisor input. This precision correction does not change the mathematical mechanism reviewed here.

## Rational maxima at an arbitrary real form

The original Ch20 proposition at label prop:ch20-model-max has a valid finite-dimensional proof.

Choose a common determination of the two rational vertical divisors and the real form. An ample basis of the relative numerical space permits arbitrarily small positive perturbations of the form to a rational class while making each perturbed curvature ample. After clearing all denominators, relative global generation of both twisted line bundles implies global generation of their sum ideal. The normalized blowup realizes the maximum, with the sign convention \(\log|\mathcal O(mD_i)|=m\varphi_{D_i}\).

The critical final closure step is now justified on one fixed space. Choose once a denominator \(m_0\) for the two divisors and blow up the sum
\[
 \mathcal O(m_0D_1)+\mathcal O(m_0D_2).
\]
This determines the rational maximum independently of the perturbation parameter. Every perturbed curvature is a semipositive closed model form and is determined on this fixed model. Nefness on any determination follows from nef pullback and reflection. Closedness of that fixed nef cone then gives positivity of the original real reference plus the maximum's differential.

This argument does not claim that a uniform limit is a model function. Nor does it require a rational original reference: only temporary perturbations are rationalized. Rational convex combinations stay rational, and arbitrary real convex combinations stay in the real model space; both preserve relative nefness.

## Fixed-form rational approximation

Let \(f=\varphi_D\) be a real psh model function at \(\theta\). The cofinal positive-representative input is essential: it provides one model determining \(D\), \(\theta\), and a real vertical \(P\) with \(\theta+[P]\) ample there. Merely pulling an ample class onto an arbitrary later model would not preserve ampleness. The proof uses the cofinal construction instead.

For \(0<\delta<1\),
\[
 D_\delta=(1-\delta)D+\delta P,\qquad
 \theta+[D_\delta]=(1-\delta)(\theta+[D])+\delta(\theta+[P])
\]
is ample on that model. Since \(\varphi_{D_\delta}-f=\delta(\varphi_P-f)\), compactness and continuity give arbitrarily small global uniform error by shrinking \(\delta\). This does not use semipositivity of \(\theta\) alone; it uses the given nef curvature \(\theta+[D]\).

Write \(D_\delta=\sum a_jF_j\) in a finite family of integral vertical Cartier divisors. The inverse image of the relative ample cone under
\[
 (q_j)\longmapsto \theta+\sum q_j[F_j]
\]
is an open neighborhood of \((a_j)\), whether or not that affine map is injective or surjective. Rational vectors are dense in its domain. They may therefore be selected inside that neighborhood and with
\[
 \sum |q_j-a_j|\,\|\varphi_{F_j}\|_\infty<\varepsilon/2.
\]
The resulting rational divisor has ample curvature at the **unchanged** form \(\theta\), and the two uniform errors add to less than \(\varepsilon\). Zero-norm divisor functions and redundant generators cause no problem. No rounding of the generic or relative reference class occurs.

The finite-maximum uniform approximation corollary follows from the elementary one-Lipschitz estimate for maximum and the preceding rational maximum proposition. It asserts membership in a uniform closure, not in \(\mathcal D(X)_{\mathbf R}\).

## Irrational-breakpoint example and directedness

The blowup over \(\mathbf C[[\pi]]\) has intersection matrix
\[
 \begin{pmatrix}-1&1\\1&-1\end{pmatrix}
\]
for the strict transform \(C\) and exceptional component \(E\). The reference \(\rho^*\mathcal O(2)-E\) has component degrees \((1,1)\), so it is semipositive with ample generic class. For \(g=\varphi_E\), the degrees of \(\theta+\mathrm d\mathrm d^c g\) are \((2,0)\); hence \(g-a\) is psh for every real constant \(a\). Its values on the oriented unit interval are \(s-a\).

For irrational \(a\in(0,1)\), the function \(h=\max(0,g-a)\) has a genuine break at \(a\). Each rational model function restricts to a rational piecewise affine function on this fixed interval. A finite real linear combination has a finite common subdivision whose breakpoints remain rational. Cancellation can remove breakpoints, but cannot create a new irrational one inside an affine cell. Thus no choice of a higher determining model can make \(h\) a real model function.

This is stronger than saying the maximum fails to be determined on the original model. It rules out every model. Conversely it is entirely compatible with uniform approximation by rational psh model functions.

Use the globally defined continuous \(h\) as obstacle. The real minorants \(0\) and \(g-a\) are admissible. Any admissible common upper bound would equal \(h\), which is not a real model function. This establishes failure of upward directedness even at one fixed ample, semipositive reference and one fixed continuous obstacle. It does not deny finite-maximum stability of genuine PSH functions.

## Truncation and exact obstacle constraints

Rational truncation at a rational constant uses maximum closure; rational constants are actual rational model functions because \(v_K(\pi)=1\). Real constants are real model functions and have zero differential. Under generic ampleness, an arbitrary real truncation is uniformly approximable by rational psh model functions. The irrational example shows why actual real-model membership cannot be retained.

For a bounded obstacle \(\varphi\), the semipositive reference supplies constant admissible minorants in both model spaces. The rational subfamily is max-closed and hence directed. To compare suprema, the proof correctly makes a **downward** rational shift after rational approximation: if \(\|q-\psi\|_\infty<\varepsilon\) and \(\varepsilon<c<2\varepsilon\) is rational, then
\[
 \psi-3\varepsilon<q-c<\psi\leq\varphi.
\]
Thus \(q-c\) is an actual rational admissible minorant, with controlled loss. This works for arbitrary bounded obstacles, not only continuous or measurable ones. No limiting set-mass or obstacle-regularity assertion is involved.

Pointwise suprema of the two families agree. The rational family itself then indexes an increasing net realizing that common supremum. The proof does not claim order-cofinality in the full real family, exact rational domination of every real minorant, or countability.

Bounds, monotonicity, real translation, the sup-norm Lipschitz estimate, idempotence, concavity, and real model reference change are still elementary statements about the real family. Their proofs use inclusion, constants, or convex combinations, not max-closure or rational density; they impose no added ample-generic-class hypothesis.

The retained fixed-model curve envelope is correctly distinguished from a pointwise maximum of affine interpolants. Its vertexwise lattice calculation does not produce an irrational subdivision or prove the global envelope theorem. The corrected surrounding remarks do not assert failure of a higher-dimensional vertexwise lattice solely from the need to refine a model.

## Ch21 skeletal passage and the full PSH maximum

In the skeletal-model lemma, the rational part uses relative ideal approximation and the monomial/Gauss inequalities. The real extension now applies global uniform rational approximation at the fixed form. Uniform limits preserve facewise convexity and the retraction inequality. This extension uses the standing ample generic class; it does not change the reference, require the approximants to be determined on the test skeleton, or invoke the excluded curve-retraction theorem.

For the PSH maximum, fix a test SNC determination. Its two restrictions are finite continuous uniform limits of real psh model functions by the definition. Replace the \(k\)-th approximants globally by rational psh model functions at the same form with errors below \(1/k\). Their restrictions retain convergence, and their rational maxima converge uniformly to the desired maximum on the skeleton. Upper semicontinuity, nontriviality, and the retraction inequality pass directly to the maximum. Testing the cofinal family of all SNC determinations is part of the general BFJ setup, not reduced-semistable cofinality on a curve.

This proof is not circular through the full PSH maximum theorem. Its input order is: algebraic nef/ample cones and positive representative; rational model maximum; fixed-form density; then the skeletal definition of PSH. It needs no Ch25 capacity, Ch26 energy, real-class curve-envelope candidate, or Ch21 curve-retraction assertion.

## Sources and retained limits

See SOURCE_INTERFACE.md for exact hashes and primary-source locators. The PDF skill was used only for source reading and visual verification; no source PDF was edited or re-exported. The supplied BFJ text was checked against rendered source pages, including the coefficient conventions and proof of Proposition 5.2. This matters because that proof supplies a real divisor; one must not silently read it as a rational-divisor statement.

The result of this audit is the correctness of the bounded repair just analyzed, after the recorded local revision, using the standard algebraic inputs explicitly identified. It is not a fresh proof of every upstream chapter theorem, and it does not resolve the separate original-field curve-retraction defect. Production verification remains outstanding.
