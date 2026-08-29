# Second independent hostile audit: P21.3 componentwise rigid exceptions

Date: 29 August 2026
Disposition: **PASS**
Scope: exact frozen statement/proof bytes listed below. This report was prepared independently and does not rely on the first audit report. It does not constitute production Rethlas verification.

## Frozen objects

- Statement SHA-256: `5b03b18f255625809a863c1079e9d84df146cb06a8c3b752ce08c58c700aeca8`
- Proof SHA-256: `3893a89ffd59f7636a7ab160c4746fecd520b328281ac60f0bbd0401dd2d21e5`

Frozen dependencies checked:

- Normal rigid zero-atom statement: `469024d04e8eb5e08900b9caea6480057398c743ca0b46076b524f2109cf80ac`
- Normal rigid zero-atom proof: `661100a4b25e82297c5b2b2712775e9c9501c337d619a64280f2d49922a4bcc2`
- Rigid-exception extension statement: `cf53c4101b6fe798d89c7e37188f2d1f03f389a5a468fdd055b6fba8bf8cf2f5`
- Rigid-exception extension proof: `cf94877ec4b2a1010a3eb51915c7cbc20a134da0bf2563b90585deab992850ce`

## Verdict

I found no false assertion, missing hypothesis, circular use of the desired conclusion, or field-theoretic counterexample. Every implication needed for the four conclusions closes under the stated assumptions. In particular, the weighted/unweighted curvature equivalence does not silently assume that the component multiplicities are equal: the local zero-atom lemma eliminates the only possible cancellation locus.

## Hostile checkpoints

### 1. Nilreduction, ordinary forms, G-forms, and current topology

Analytic seminorms annihilate the nilradical, so the nilpotent closed immersion has the same points, topology, completed residue fields, and absolute-value functions. A unit modulo a nilpotent ideal lifts to a unit: if a provisional inverse has product `1+n`, the finite geometric series for `(1+n)^{-1}` repairs it. Thus moment maps lift locally with literally identical tropicalizations. This is the mechanism behind CLD Proposition 15.1.3(b) and its stated form/G-form variant.

The topology claim is also justified, not merely the algebraic sheaf claim. For fixed compact support, lifted and restricted finite moment-chart data are cofinal; corresponding tropical images, Lagerberg representatives, subdivisions, and all defining `C^r` seminorms are identical. Hence compactly supported test-form spaces are locally convex homeomorphic. Transposition therefore gives both the current-space isomorphism and the weak-topology isomorphism. Positivity cones and the two differentials are preserved chartwise.

For positive currents, locally bounded Borel multiplication is transported through the attached Radon measures (CLD Example 7.2.12). The proof correctly checks decomposition-independence for a difference of positive currents and correctly refrains from defining the product for an arbitrary order-zero current. The transfinite psh and continuous-psh filtrations use the same stage zero, the same functions and open sets, and the same decreasing or locally uniform convergence; induction therefore identifies the two spaces' respective sheaves. No discontinuous Bedford--Taylor assertion is smuggled in.

### 2. Reduction and ambient hypotheses

Goodness, separatedness, strictness, and pure dimension one pass to the reduction. The finite nilpotent immersion has empty relative boundary, and the CLD boundary-composition formula transfers boundarylessness. The local holomorphic/differential separation hypotheses needed for Radon measures and Borel multiplication follow from goodness and topological separatedness.

### 3. Conductor, component intersections, rigidity, and local finiteness

Excellence of analytic local rings makes the componentwise normalization finite. Its quotient by the reduced structure sheaf and the conductor are coherent. Because the reduction is pure one-dimensional and normalization is generically an isomorphism on each component, conductor support misses every minimal component and is zero-dimensional. Pairwise intersections of distinct irreducible components are likewise proper zero-dimensional analytic loci.

Irreducible components are locally finite; on a relatively compact affinoid only finitely many occur. Each zero-dimensional closed analytic locus there is finite because its strict affinoid coordinate algebra is noetherian Artinian. The strict affinoid Nullstellensatz yields finite residue extensions of `K`, so these points are rigid, not necessarily `K`-rational. Finite normalization preserves rigidity of their inverse images, and properness plus local finiteness gives local finiteness of every `Z_i`. This reasoning remains valid over imperfect and non-algebraically closed `K`.

### 4. Connectedness after deleting rigid points

Ducros Theorem 3.5.1 and section 1.3.5 give injective-arc connectedness of a connected analytic curve. Ducros Proposition 3.5.2, whose proof explicitly handles arbitrary ground fields, identifies the number of branches at a rigid point with the normalization-fibre cardinality; a rigid point on a normal curve is therefore unibranch. Section 1.3.12 makes every interior point of an injective arc pluribranch. Consequently an arc joining two points outside `Z_i` cannot cross `Z_i`, proving connectedness of `U_i`.

Nonemptiness is also secured: a connected pure one-dimensional normal curve is not an isolated point; the unique branch at a rigid point contains a nontrivial arc, whose interior supplies a pluribranch, hence nonrigid, point outside `Z_i`. Thus all hypotheses of the frozen rigid-exception extension apply to `(U_i,E_i')`.

### 5. Generic multiplicities and integration currents

CLD Definition 13.2.5 and section 13.5.2 give `[X]=sum_i m_i[X_i]` and `[X_red]=sum_i[X_i]`; CLD Proposition 16.6.3 identifies integration with the fundamental-cycle current. The normalization has calibrated degree one where it is an isomorphism. Its exceptional image is contained in the rigid zero-dimensional set `Z`, while CLD Propositions 3.3.6 and 15.2.1(a) force every smooth `(1,1)` test-form germ to vanish at such a point. Therefore pushing the normalization integration current forward gives exactly the current of the reduced component, globally, and the two displayed current identities with and without `m_i` follow.

Local finiteness of components makes both sums legitimate. Conversely, restricting equality of the two currents to a nonempty rig-smooth component open disjoint from `Z` and the other components detects `m_i`; the local integration current there is nonzero. Thus equality holds exactly under generic reducedness.

### 6. Classification and the rigid-support argument

The nilreduction current isomorphism transports a positive closed `(0,0)` current to the reduction. Off `Z`, the components are disjoint and the normalization is an isomorphism, so the frozen rigid-exception classification gives one nonnegative coefficient per component. The residual current is supported on `Z`.

At a rigid point, both summands in the CLD dimension formula vanish, hence `d_K=0`. CLD Proposition 15.2.1(a) confines a smooth `(1,1)` test form to `{d_K>=1}`. Every such test form is therefore supported off `Z`, so a current supported on `Z` acts as zero. This proves the global decomposition without using the zero-atom lemma. Uniqueness follows on a nonempty rig-smooth component open.

### 7. Component measures, pushforward, and weighted versus unweighted equality

Each `tilde W_i` is an open subset of the boundaryless normal curve `tilde X_i`; it is therefore boundaryless. Pullbacks of the continuous psh functions are continuous psh, and CLD Lemma 8.5.5 makes their curvatures positive Radon measures. Multiplying the two cycle-current identities by a continuous function is legitimate, and direct testing yields the two function-current decompositions. Proper finite pushforward commutes with the current differentials. Injectivity of `iota_*` then converts equality on `X` into the weighted equality on `X_red`; equality on `X_red` gives the unweighted equality.

Off `Z`, component images are disjoint and each normalization is an analytic isomorphism. Restricting either sum to a single component image, and using `m_i>0` in the weighted case, forces the signed component curvature measure `sigma_i` to be supported on `Z_i`. No cancellation between different components is possible away from `Z`.

### 8. Exact use of the local zero-atom lemma

For every `z in Z_i cap tilde W_i`, the ambient space `tilde X_i` is good, separated, strict, normal, pure one-dimensional, and boundaryless; `z` is rigid and interior, and its analytic local ring is normal. Taking the lemma's open pure-one-dimensional neighborhood to be `tilde W_i` is valid. Since the ambient curve is boundaryless, the lemma's `Omega^o=Omega cap Int(tilde X_i/K)` is exactly `tilde W_i`, so its measure is precisely the measure used in this packet, with no boundary mismatch.

The lemma gives zero mass at every point of `Z_i` for each of the two positive measures. Their difference is a signed Radon measure supported on the locally finite set `Z_i`. Locally that support is a singleton, so the signed measure is its atom; the atom is zero. Hence every `sigma_i` is zero. This closes both implications between the weighted and unweighted sums and establishes the final Bedford--Taylor identity componentwise.

### 9. Arbitrary-field stress test

No step uses algebraic closedness, perfectness, or rationality of the exceptional points. Strictness supplies finite residue extensions; Ducros's branch theorem is formulated over an arbitrary complete non-Archimedean field and its proof treats the imperfect case by perfect-completion base change; multiplicities and calibrated degrees are intrinsic; and the frozen zero-atom lemma assumes only a rigid interior point with normal local ring. Thus the obvious imperfect-field and non-algebraically-closed-field counterexample routes do not apply.

## Build diagnostic

An isolated hostile rebuild of the exact statement/proof dependency graph completed successfully as a 12-page letter-size PDF with empty author metadata. The log contained no TeX error, undefined reference/citation, multiply-defined label, or overfull/underfull box. PDF/log hashes are intentionally not made part of the mathematical freeze because their bytes contain build-time metadata and can change across forced rebuilds.

## Final conclusion and boundary

**PASS** for the exact statement/proof hashes above. The proof's nearest genuine boundary is exactly the one it states: it needs nontrivial valuation, strictness to force zero-dimensional exceptional points to be rigid, boundarylessness for the CLD curvature formalism and exact zero-atom input, and local finiteness of the exceptional rigid loci. The packet should still pass through the mandated production Rethlas run before insertion into the live manuscript.
