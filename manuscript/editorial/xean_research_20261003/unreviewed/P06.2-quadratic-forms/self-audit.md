# Self-audit of the exact restricted higher-dimensional theorem

This is an author audit of an unverified mathematical draft. It is not independent review. No verdict from the preceding packet or its pending reviews is assumed. The audited exact result is equivalence of the ordinary zero-Hessian equations under a quadratic Galois extension satisfying (H), in every pure dimension n >= 1. Original P06.2 recognition remains open.

## The new load-bearing calculation

Scalar reconstruction alone is insufficient. The proof adds a genuine ordinary-form identity: if G = F + e are analytic units, then the moment (F/e,G/e) has image in the three-ray tropical line. The polynomial 1-form U dV - V dU restricts to zero on each ray and at their common vertex. CLD 3.4.4 establishes sheaf nullity, while the chart is on an ordinary neighbourhood, so the result is an equality of ordinary forms. Merely differentiating point values is not used.

For either prime differential, expansion gives x dz - z dx = r(dz-dx) + (x-z)dr. Adding the conjugate identity gives the formula (10) for the orbital form delta_i d delta_j - delta_j d delta_i. The normalized-unit sum S_i is used; it is not confused with the original unnormalized sum s_i. Combining it with dQ_ij gives each individual delta_i d delta_j. All pure-prime and mixed differential pairs then follow by differentiating these 1-forms. The mixed identity covers ordered indices, so no antisymmetric combination is silently dropped.

Every invariant polynomial superform has even total anti-invariant parity, counting scalar and differential factors. Pairing those factors exhausts scalar/scalar, scalar/differential, and every differential/differential pair. The proof uses the free polynomial/exterior monomial basis and graded signs. It requires no spanning claim based only on symmetric (1,1) Hessians, no J-symmetry reduction, no quotient by an integration kernel, and no appeal to an abstract tropical obstruction. The reconstructed descendants are actual ordinary sheaf sections on the downstairs analytic neighbourhood.

## Units, supports and the fixed locus

The units f_i are decomposed in the actual affinoid tensor algebra as u_i + a v_i. If v_i(x) = 0, u_i(x) is nonzero and a full-fibre strict norm inequality gives equality of both conjugate logarithms to a downstairs unit logarithm on a smaller neighbourhood. Thus delta_i = 0 as a function and all its derivatives vanish. If v_i(x) is nonzero, v_i becomes an actual downstairs unit and the normalized F_i is legitimate.

For e_ij = b_j-b_i, a zero value at x is handled by another strict norm inequality on the full fibre, giving equality of the normalized conjugate logarithms and delta_i = delta_j. There is no log of e_ij in this case. A nonzero value gives an actual unit e_ij. Norms of the normalized F_i are invariant units. All finite choices are retained by the compact-complement shrinking argument. Nilpotent coefficients with zero seminorm are handled by the same inequalities; the ring itself is not replaced by its reduction.

No formula divides by delta_i, delta_i squared, or a vanishing analytic coefficient. The fixed-locus formula is therefore exact rather than a limit of formulas on a punctured chart. A quotient inverse on delta != 0 was considered but is not used.

## Scalar reconstruction audit

The three trace rows have norm-one entries and norm-one pairwise determinants. At most one trace can have norm below the maximum magnitude of f and sigma f. The two traces selected at a singleton fibre are retained as units. Unequal-magnitude and equal-magnitude cases separately prove formula (4) everywhere, including cancellation directions. Applying it to f_i f_j and polarizing over the reals reconstructs cross products. Characteristic two causes no division by two in the field. Hypothesis (H) is not weakened to a rescaled trace condition.

The local two-point-fibre construction uses disjoint ordinary opens and the analytic structural sheaf to glue invariant units. It proves exact descent of the given invariant form, including its differential factors. It does not assume finite étale scalar projection is a local topological cover.

## Differentiated approximation audit

Ambient coefficient extension is supported by CLD 3.3.3 and 1.9.4, with the closedness condition retained. The coefficient form is symmetrized with its whole differential basis, not just its scalar coefficients. Gaussian convolution and finite Taylor approximants give C2 control on a fixed upstairs box. The finite unit lists and the downstairs polynomial generators are fixed for all degrees. The polynomial-superform proof supplies exact pullback equality for every approximant.

A finite cover of the compact image of the averaged support supplies fixed downstairs cutoffs. Each cutoff is compactly supported inside its ordinary local chart. Extension by zero is justified by a neighbourhood on which the product is zero. The sum-one identity is needed near the original support only; off that support the form is zero, so the global error identity still holds.

All approximate supports lie in one compact D, and its full inverse image is compact. The cutoff moments and original upstairs moments are combined in a finite fixed cover. The product rule controls the coefficients of d'd'' of the error. Derivatives of unit-log differential basis factors vanish by their affine moment descriptions. No C0 approximation or derivatives in reconstructed downstairs coefficient variables are used in place of the required upstairs C2 estimate.

## Higher-dimensional calibrated measure audit

On each fixed compact chart, top-form contraction is a finite coefficient matrix paired with tangent n-volume minors. The bound by N times the sum of squared minors follows from Cauchy--Schwarz, with N = binomial(r,n). The dominating form is xi^n/n!, whose contraction is precisely the squared-minor sum with the positive top-order convention. If the chart rank is less than n both top forms vanish. Lower-dimensional cells have no top measure.

Actual positive canonical calibration multiplies both sides. Compactness and CLD 5.10.1(c,d) make the dominating measure finite. Summing over the fixed finite cover controls total variation. The continuous multiplier is bounded on the same compact support, which proves convergence of differentiated pairings. No normalized probabilities, point counts or discarded generic lengths enter.

## Analytic structures and both field normalizations

The completed finite tensor is proved complete by bounded basis-coordinate maps. Its invariant algebra is computed by tensoring a linear kernel, which works in characteristic two. Invariant units descend with invariant inverses. The actual completed-residue-field fibre algebra is a field or a product of two fields. Existence and uniqueness of the field absolute values are checked by finite-affinoid spectra and the power norm argument. Invariant idempotents give orbit transitivity.

The restricted K-carrier and E-carrier have common local affinoid/unit charts and identical compact moment images. Their form nullity is identical by CLD 3.4.1--4; their ordinary sheaves agree, although their calibrations differ. The semilinear involution is applied as a genuine K-analytic automorphism of the restricted carrier. The isomorphism pushforward formula and the restriction-of-scalars factor 2 prove E-calibrated integration invariance.

Scalar projection is a different operation: CLD 14.3.6 and 15.3.1 give no extension-degree factor. They are applied to smooth differentiated forms and then integrated against h. This proves the pairing identity without pulling back an arbitrary current.

Purity upstairs is checked at minimal primes in every dimension. A point with kernel a downstairs minimal prime isolates its component in the local-dimension formula. The reduced tensor injects into a finite product of separable field tensors, and the unreduced nilradical is its actual nilpotent tensor ideal. Minimal primes upstairs contract to minimal primes downstairs. Finite integral component injections preserve dimension by explicit lying-over, going-up and incomparability arguments. Reduction is only a dimension check; actual measures still use the unreduced structure.

## Scope and source audit

The exact field assumption and every original strict ambient hypothesis are retained. The theorem treats arbitrary nonproduct pure-dimensional spaces under that restricted extension. It establishes scalar-current transport, not pluriharmonic recognition. The theorem is substantial relative to the preceding curve-only scalar gate, but no priority claim is made.

Every primary theorem used is stated with its relevant hypotheses in the authoritative argument and checked at the use site. Cached CLD and GR snapshots provide the chart, cutoff, dimension, calibration and boundary statements. Weakly smooth GJR descent, G-tropical relative integration and analytic-morphism descent are explicitly excluded as ordinary-form premises. Catalogue recognition descriptions are comparison data, not independently established assumptions.

No further finite-Galois class, completion of an infinite extension, arbitrary curve-current pullback, universal classical recognition or two-sign regularization follows in this packet. No new first-current equivalence is included in the claimed exact result. The author audit finds no remaining gap inside Theorems A--C, but this assessment is fallible and has no independent verdict.

## Reproduction audit

All new writes are in the fresh workspace. Programs, source snapshots, exact input, commands, outputs, environment, hashes and the twice-compiled PDF are retained. The checks cover finite polynomial/exterior identities and artifact production only. They do not verify analytic correctness. No installation, extra model call, collaboration agent, external message, configuration change, old-workspace write, SQL mutation or heavy computation was used.
