# Independent conditional exact-byte audit: nef-class DXZ intersection

Date: 31 August 2026. Reviewer: `/root/p082_independent_reaudit`.

## Verdict and scope

**PASS, conditional exactly on the stated full Kähler raw-function order comparison.** No unresolved substantive mathematical gap was found in the frozen statement, proof, or diagnostics. This verdict covers the displayed theorem for every connected compact Kähler manifold and every real nef class, including nef non-big classes. It does not silently impose projectivity, rationality, positive limiting mass, finite energy, or a semipositive smooth representative.

The conclusion is an order isomorphism from the full DXZ inverse-system space to the intersection of the already-defined MP cones of every positive Kähler perturbation, as actual functions on the entire ideal spectrum. Auxiliary-form and smooth-representative independence are included. The separately defined fixed-nef-class model completion is proved only to be contained in the intersection. Neither equality nor strictness of that inclusion is established.

The full Kähler comparison is an **assumed mathematical input** in this audit. Its core is not freshly audited here. The premise's raw-USC and dominated-divisorial dependencies remain separately gated. This is an independent mathematical review of this nef deduction, not production acceptance, a live-book change, or retirement of P14.3.

## Provenance and exact revision

The candidate was authored by `/root/p081_weighted_repair_fresh`; root proposed the perturbation-intersection target and pointed to the existing inverse-system lemma. This reviewer did not author the nef candidate or its expanded diagonal construction. This reviewer previously audited the P14.2 raw-USC and P14.3 dominated-divisorial packets and other related curve/closure work. Those related contributions are disclosed, not passed off as a fresh audit of the full Kähler comparison. The separate Kähler audit listed in `INPUTS.json` was checked for byte preservation only; its verdict was not used as independent proof of the nef argument.

Frozen candidate directory:

`../p143_nef_closure_research_20260831/`

| Input | Bytes | SHA-256 |
| --- | ---: | --- |
| `statement.tex` | 3270 | `6f329c5f65b9ff9481bf03c8bd189aa89ce07f577558ccb6e1707181ed3e0f85` |
| `proof.tex` | 10869 | `9cb99b9909c188fc24c9fadf1ffda0a0a0008185879ca7f7d90d4064a40fc329` |
| `diagnostics.tex` | 2475 | `970d7b8e1b13af70d1c01c297da3e750223c79c05f968bb857f8f866f3d69ec5` |
| `MANIFEST.json` | 1908 | `8b03ba68f6a8a1e901d19befd9e832088481d371c936b1349603898317a0bb3b` |
| `INPUTS.json` | 1757 | `13a60e547b6c257ec335734f4fa7148a0ea2f2c12f435c2207249acb6a1d0069` |

Full Kähler dependency, kept conditional:

- Statement: `befc29fb89ff79fe90172d03b1fe088e5f19ebf2ca28aedbd4c83cd05f008100`.
- Proof: `1ef28983e1ac242f9a23080e24ced0c21531899f56ab29a96312f4ce79757652`.
- Manifest: `f5e70b72c09601f27d2210391d8f72935bc37564481be9a5818c19f8926c0b8b`.

All 12 candidate manifest entries and all seven recorded predecessor inputs were independently checked against both size and SHA-256 after the author announced freezing. All matched. The full principal texts were read, not merely their summaries or a checker result.

## 1. Definitions, index directions, and common endpoints

The prime space in Xia, Definition 3.2, consists of decreasing concave curves of normalized I-model potentials on a half-line with finite endpoint. Its definition does not assume positive mass. Definition 3.5 defines the full space as a limit of precisely these prime spaces, in the category of sets. The transition from a smaller positive perturbation to a larger one is the I-envelope in the larger form. Thus the arrow direction in the candidate is correct: the reverse ordering on perturbations produces maps from smaller to larger perturbations.

Any two Kähler forms have a common strictly smaller positive multiple of a fixed Kähler form, by compactness and comparison of positive definite forms. This is enough for the entire construction; no countability, metrizability, completeness of a function-space topology, or convergence of an arbitrary chosen sequence is used. The harmless zero-dimensional case has only the trivial form comparison and the same set-theoretic construction.

Transition envelopes preserve the endpoint by their definition and preserve every fixed-level multiplier ideal. Hence comparison through a common smaller perturbation proves both a common finite endpoint and a single collection of ideals at each level. This is stronger than agreement of numerical values merely on divisors. Evaluating those identical ideals at any coherent-ideal semivaluation gives identical raw functions, including where some ideal values are infinite.

For a level below the endpoint, its quasi-psh potential is not identically minus infinity. Its multiplier ideal is a nonzero coherent ideal; the zero valuation consequently evaluates it as zero. Therefore the raw value at the zero valuation is exactly the finite endpoint. All raw values are bounded above by that endpoint because ideal values are nonnegative. The proof never inserts the post-terminal identically-minus-infinity level into the raw formula.

## 2. Inverse-limit flattening: independent check of both inverse identities

Write N(sigma) for the full space and C(sigma) for the prime space. Suppose `(G_epsilon)` is a compatible family of full objects for `sigma+epsilon*omega`.

For an arbitrary Kähler form eta, choose epsilon with `eta-epsilon*omega` Kähler and take the total component of `G_epsilon` at `sigma+eta`. That component is an element of C(sigma+eta), so no regularity or concavity is being created by taking a new limit. The required prime test-curve properties are inherited from an actual existing component.

If epsilon_1 and epsilon_2 are both admissible, choose `0<delta<min(epsilon_1,epsilon_2)`. Compatibility of the full objects says that each G_epsilon_i is the injection of G_delta. Evaluating this identity at the same total form sigma+eta proves that the two choices give the same component. Every expression exists because `eta-delta*omega` remains Kähler.

For eta' strictly larger than eta, a single epsilon admissible for eta is also admissible for eta'. Internal compatibility in G_epsilon gives exactly the desired prime transition identity. The common-smaller-delta argument also identifies all endpoints. Thus the constructed family really lies in N(sigma), rather than being only a collection of pointwise-compatible numerical transforms.

To recover G_epsilon from the constructed object, fix an additional perturbation nu and choose delta smaller than epsilon when defining the total component `sigma+epsilon*omega+nu`. Compatibility identifies that component with the corresponding component of G_epsilon. Since this holds for every nu, the re-injected full object is exactly G_epsilon. Conversely, starting from an object of N(sigma), the restriction and reconstruction simply select its existing total components. Both inverse identities hold.

The argument is valid for arbitrary pseudoeffective sigma at this set-theoretic stage. Nefness enters only later, when the Kähler comparison must apply at every arbitrarily small perturbation. The lemma does not recover a positive-mass unperturbed curve and does not invoke Xia Lemma 3.10.

Xia Lemma 3.7 directly supports the distinction between the prime-system, positive-mass-system, and full-system presentations. Its displayed intermediate-half-perturbation construction is consistent with the candidate. The present proof itself uses prime components and therefore does not need to claim that an arbitrary isolated prime curve has positive mass.

## 3. Change of representative and normalization

For `sigma'=sigma+ddc h`, the sign is correct: `U-h` is `(sigma'+eta)`-psh whenever U is `(sigma+eta)`-psh. Subtracting a smooth function does not preserve the normalized I-model representative pointwise. The candidate correctly applies the normalized I-envelope afterward.

The identification is the existing DXZ cohomological identification, explicitly stated in the source introduction, not a newly assumed equality of unnormalized potentials. Smooth h is bounded locally (and globally here), so the integrability condition defining every multiplier ideal is unchanged by adding or subtracting h. The envelope preserves the same ideals. Applying the inverse shift and re-enveloping recovers the original normalized I-model potential: at a fixed background, two normalized I-model potentials with identical ideal data have the same defining envelope.

This also makes the transition squares commute. Either route lands in the same final form with the same ideals and the same normalization. The endpoint is unaffected. Hence the raw function is literally unchanged on the entire ideal spectrum, without a density argument.

For completeness, the use of the source-defined curve identification does not hide a positive-mass hypothesis. Monotonicity of the envelope preserves decreasingness. Its concavity follows from the I-singularity order: a convex combination of two normalized envelopes is psh and at most zero, and its divisorial singularities are at least those of the intermediate concave input level. The valuative characterization of the I-order then makes that convex combination an admissible competitor for the intermediate envelope. This is compatible with the stated source identification and requires no mass lower bound.

Finally, a Kähler class need not be represented by the displayed form `theta+epsilon*omega`. The candidate explicitly transports to a positive representative before applying the conditional Kähler comparison. On a compact Kähler manifold the difference of cohomologous smooth closed real (1,1)-forms is `ddc h`, so the required transport exists. No semipositivity of theta is silently assumed.

## 4. Intersection, coherence, surjectivity, and order

For a nef alpha, every class `alpha+epsilon*[omega]` is Kähler. Mapping a full object in N(theta) into each perturbed full space preserves its raw function. The assumed full Kähler comparison therefore places that same actual function in every MP cone of the intersection. This establishes the forward map on precisely the advertised domain.

Conversely, let F be an actual function in the intersection. The conditional Kähler order isomorphism gives a unique full object G_epsilon in each perturbed class whose raw function is F. For epsilon<delta, the injection of G_epsilon to the delta class still has raw function F. Injectivity of the assumed comparison in that one delta class forces equality with G_delta. This is the required coherence; it is not inferred just from ordinary divisorial density.

All G_epsilon have the same finite endpoint F(o), since the comparison supplies genuine full objects in every perturbation. In particular, the intersection element is not identically minus infinity and there is no unbounded endpoint to repair. The explicit flattening lemma constructs a full object in N(theta). Any one of its perturbed images computes the same multiplier-ideal formula as F, giving equality at every semivaluation.

The order check uses Xia's componentwise order. An ordered pair in N(theta) gives ordered pairs in every perturbed space and therefore ordered raw functions by the conditional comparison. Conversely, ordered raw functions yield ordered G_epsilon in every perturbation; selecting a common admissible epsilon for any total component gives order of the original prime components. This proves reflection as well as preservation and also establishes injectivity.

There is no circular use of the nef conclusion to establish the Kähler input, no passage from equality on a dense subset to arbitrary functions, and no limit interchange involving mass or energies.

## 5. MP monotonicity and independence

MP Definition 4.1.2 tests a model function represented by a vertical divisor D on a dominating test configuration by relative nefness of `gamma_X+D`. Adding the pullback of the nef class `gamma'-gamma` preserves relative nefness and leaves D, hence the actual model function, unchanged. Definition 4.3.1 then allows the identical decreasing model net to be used in the larger class. Both endpoint classes in this invocation are Kähler, exactly as required by MP's standing scope.

This is a same-model argument. It uses neither a maximum nor a minimum of model functions, nor a false real-model max-closure assertion, nor any new rational approximation theorem. The pullback used is in the safe forward direction: pullback of a nef class is nef.

For two auxiliary Kähler forms omega_1 and omega_2 and any epsilon>0, choose delta>0 with `epsilon*omega_2-delta*omega_1` Kähler. Monotonicity then places every member of the first intersection in the chosen epsilon-cone of the second. Reversing the roles proves equality. The same comparison shows that the ray can be indexed by all positive real numbers or by the cofinal sequence 1/j without changing the intersection.

MP's criterion is cohomological, while the preceding normalized DXZ representative change preserves the raw function. Thus the asserted representative independence is an equality under the specified identification, not an assertion that normalized complex potentials themselves remain numerically unchanged. Injectivity of the raw comparison identifies inverses constructed with different auxiliary forms.

## 6. Boundary diagnostics and exclusions

The zero-class diagnostic is correct in positive dimension. At each positive perturbation eta, the constant-zero levels are normalized I-model, have unit multiplier ideals, and define a compatible curve with any prescribed finite endpoint c. The raw function is the constant c. Each component has positive mass, while the limiting mass is `epsilon^n * integral(omega^n)` and tends to zero. Thus positive mass of the inverse-system object cannot be imposed without excluding this legitimate example. The example makes no claim to classify the entire zero-class intersection.

For the auxiliary fixed-nef-class model completion, adding epsilon times the pullback of omega to each fixed-class relatively nef model preserves positivity. Its nontrivial decreasing limit therefore lies in every perturbed MP cone. This proves exactly the stated inclusion. The construction of compatible DXZ components does not supply a common decreasing net of relatively nef models in the fixed boundary class, and the proof correctly declines to assert the reverse inclusion.

For a pseudoeffective non-nef class, arbitrarily small perturbations on the chosen ray need not be Kähler. Restricting to large perturbations destroys cofinality toward zero. This is a genuine limitation of the deduction, accurately stated in the packet. No non-nef comparison, zero-volume energy or Monge-Ampère theory, general-envelope assertion, or inventory retirement follows from this audit.

## 7. Mechanical and visual checks

The candidate's checker was read in full before execution; it performs only reads and reports. Its post-freeze execution gave: 12 unique internal labels, 20 references, three resolved bibliography keys, seven unchanged predecessor inputs, 12 unchanged manifest entries, and no errors. A separate inline hash/size check independently verified the manifest and input entries. All four TeX inputs were independently scanned for prohibited control bytes; none were found.

The existing draft log was inspected through the read-only checker. It reports draft mode, no PDF, and zero undefined-reference, citation, LaTeX-warning, overfull, underfull, or error lines. Its SHA-256 is `3760204cb0d5f800024c3318d400f594d9abc99e0bea241542104c4c50580df8`. This is syntactic evidence only; no candidate PDF exists and no candidate-layout review is claimed.

Using the PDF skill, source pages were rendered and visually inspected in full: Xia printed pages 5, 8, 9, 10, 11, 13; MP pages 33 and 39; DXZ page 3. The prime marks, arrows, half-perturbation construction, endpoint domain, normalization, order definition, and relative-nef/decreasing-net definitions agree with the extracted text used in this audit. Source versions, local paths, exact hashes, primary URLs, and the additional published envelope interface are recorded in `SOURCE_LEDGER.md`.

No candidate, predecessor, live manuscript, inventory, or production setting was changed. Only this new audit dossier and disposable source-rendering files were written. No production call or permission workaround was attempted.
