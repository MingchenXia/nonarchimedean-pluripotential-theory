# Author audit of the finite-Galois gate

4 October 2026. This is the same native model's reconstruction and adversarial
author audit, not an independent model call, formal verification, or priority
certificate. No extra model or sub-agent was used. The draft claims the
finite-Galois gate, while original P06.2 remains open.

The audit checks the complete theorem for arbitrary compact ordinary
(n-1,n-1) tests. It does not substitute a scalar test or a curve probe.

| Possible failure | Reconstruction and outcome |
|---|---|
| A residue constant is only present in a completion | Section 2 approximates a primitive separable root by a fraction from the actual affinoid algebra, then introduces strict rational variables controlling g, P(g), and the actual derivative inverse. Newton converges in the quotient Banach algebra. Root uniqueness identifies its evaluated value. |
| Spectral bounds miss nilpotents | The estimates are quotient-norm bounds from actual algebra relations, not estimates on the reduction. The final F embedding, all norm units, and all scalar tensor products remain in the actual algebra. |
| F is only an abstract field of germs | The root lives on a strict affinoid neighborhood. A bounded F action yields an equivalent F-homogeneous complete auxiliary norm and a strict F-Tate presentation with equivalent quotient norm. The auxiliary norm need not normalize the unit to one; the final affinoid quotient norm does. Common rational domains identify the actual sheaves on ordinary neighborhoods. |
| The induction loses boundarylessness or purity | Ordinary opens are boundaryless. The relative-interior composition equality for U->M(F)->M(K) gives boundarylessness over F. Every minimal component is checked by actual finite integral domain extensions; no maximum-total-dimension shortcut is used. |
| A proper stabilizer is not a Galois stage | The finite fibre is an actual product of fields. G is transitive on its points, D_y^H=H(x), and a primitive E element has exactly |H| conjugates over H(x). E/E^H is Galois even if E^H/K is not Galois. All other tensor components use conjugate stages of the same smaller order. |
| A degree factor is misplaced | Same-carrier F/K calibration is [F:K] and is cancelled only in (15). Canonical scalar projection in (21) and (30) has no factor. The primary Artinian degree-sum proof and its lengths are embedded. |
| Invariant complementary forms are assumed to descend | Only P0^* i^* omega descends, using actual norm units. The remaining form has zero restriction to the fixed moment subspace and is handled by weak approximation. No exact descent of the whole invariant form is claimed. |
| The downstairs cutoff loses the full fibre | At a G-fixed point the fibre is singleton; a compact-complement image argument chooses V with all of V_E inside the unit/chart domain. All cutoff supports are ordinary compact subsets of V and their whole inverse images are compact. |
| Second cutoff derivatives diverge at rank one | The only surviving no-transverse-generator component has coefficient A(u,0)=0 and A=O(t). Components with either transverse generator kill the second normal derivative term. First-cutoff terms are only O(delta^-1) on an O(delta) collar. |
| A cell touches W only along a boundary face | The affine-span calculation compares a collar point to w0+u on ambient W, whether or not that point belongs to the cell. Global ambient smooth extension makes this comparison legitimate. No interior intersection assumption is used. |
| Low-rank moments create invisible top measures | Only the n-dimensional part carries top measures. If a moment image has dimension <n, its represented top form is zero. Correct polyhedrality and dimension upper bounds are imported from Ducros 3.2; the false universal equality in CLD 12.2.4 is excluded. |
| Signed pushforward conceals divergent variation | (23) is derived from the positive skeletal sheets before signed summation, using actual constant finite-flat degrees. It is not derived solely from a signed integral identity. |
| L1 convergence on the original moment does not control a new smooth multiplier | For each fixed smooth multiplier a, section 7 adds all moment coordinates describing a. The enlarged ambient fixed subspace is W times the extra coordinate space. The undifferentiated error still tends to zero in L1 there. |
| Green's formula silently assumes symmetric tests | The proof uses two separate Stokes calculations, showing the signs in (27). The complementary form need not be symmetric. The source's separately stated symmetric Green formula is not used. |
| Continuous approximation is insufficient for differentiated measures | It is paired with the uniform total-variation bound (26) on a single fixed compact carrier. The three-epsilon argument is written explicitly in (29). No Radon-Hessian hypothesis is introduced. |
| Smooth scalar density is too broad on a nonparacompact space | Only finite compact partitions are needed. A direct affinoid separator construction proves compact cutoffs; finite small-oscillation covers then give scalar approximation on the one fixed compact. |
| Catalogue descriptions or older verdicts are treated as grants | Neither is a premise. The earlier quadratic manuscript was read for comparison but its proof and verdict were not imported. All novel steps are reconstructed and all necessary imported primary bodies are embedded. |
| The gate is confused with original P06.2 | The status is partial and candidate=false. No two-sign regularization, completed-algebraic complementary-form gluing, mixed-finite ascent, transcendental ascent, or arbitrary-dimensional classical recognition is claimed. |

No failed mathematical estimate or indispensable unresolved step was found
in this author audit of the finite-Galois draft. That is an author assessment,
not a grant of correctness. In particular, the primary theory is imported
with its precise hypotheses; this audit does not reverify the entire CLD
theory or all source-internal references from scratch.

The source extraction was initially rejected by its own strict checks for
one incorrect end-heading pattern and one repeated theorem-heading pattern.
The patterns were corrected using the primary text. No unit was accepted
with a missing end marker. A first LuaLaTeX build failed because its font
loader was absent. The first XeLaTeX build exposed a misplaced equation
tag; the tag was moved outside its split environment. A subsequent build
exposed four unsupported source glyphs. PDF-only equivalents were used,
while authoritative primary bytes were retained. All these failure logs
remain in build; they are implementation diagnostics, not mathematical
counterexamples or proof-verification results.

Rerun the source embedding with `python embed_sources.py`, the finite
diagnostics with `python diagnostics/finite_checks.py > diagnostics/output.json`,
the two-pass build with `python build_documents.py`, and the integrity checks
with `python validate_artifacts.py`. The authoritative proof is
P06.2-argument.md and its standalone documents are P06.2-partial.tex and
P06.2-partial.pdf.
