# Independent exact-byte audit: nonreduced SNC residual-wall functional

Date: 31 August 2026. Reviewer: /root/p082_independent_reaudit.

## Verdict and exact conditional meaning

PASS within the complete written scope. No substantive mathematical gap or required correction was found in the frozen global proof.

The residual principal-divisor identity and b_0(p)=c_0[kappa(p):k] are conditional on the exact local premise (L), Sections 2-5. The final individual coordinate-moment source-cell ratio additionally uses (L), Sections 6-7, and the expressly assumed representation formula (R). This review does not independently re-prove or certify (L) or (R), and does not confer production acceptance.

The model is an actual integral proper flat REGULAR model over the ORIGINAL complete DVR, with strict-normal-crossing SUPPORT and arbitrary positive vertical multiplicities, smooth generic fibre and perfect residue field. All n selected components are VERTICAL. The current is defined on the WHOLE tube X_C of a connected proper residual curve. No residue-characteristic-zero restriction, reduced-special-fibre assumption, or tameness assumption is added to make this verdict pass.

Ordinary-W locality, selected horizontal components, model realization of arbitrary analytic moments, all-moment accessibility, and full P21.3 remain outside this result.

## 1. Frozen bytes and review procedure

Candidate: sibling p213_nonreduced_snc_wall_residual_functional_research_20260831.

| File | Bytes | SHA256 |
| --- | ---: | --- |
| RESEARCH_NOTE.md | 30325 | d9e57c21c276edb40bc7619562b7f0a782cdc7a7eb05a04dd0b0cf0770dc9ea9 |
| SOURCE_LEDGER.md | 9122 | 5be17264811305baedb22ca98830969bf52f087678348519e820f2473992fb03 |
| INTERNAL_CHECK_AND_SCOPE.md | 4560 | 585decd6cbb01d474b7fbbb5a8e359bce13d908ff652b22d99dbc26adac86fbc |
| VALIDATION.json | 5828 | cf342531331fbf32b9198ee0127a0234d743b2190a72118c4cf91de46e53f018 |
| MANIFEST.json | 6146 | caa674cb64156f39871a0b4749c21f633a6e253956c64fdaf0073d8774815a92 |
| SHA256SUMS | 2300 | 7f4cf39f1cadda8c11693a670277f6c323587d1e3bf1da94ed8664358cca6e67 |

The author confirmed this freeze explicitly. I read the complete note and source ledger, the internal scope ledger and validation record, and checked the final completion-to-tube citation and shear notation against the frozen revision. All 15 candidate manifest entries and all 16 candidate checksums match. Every byte below 32 except LF/tab, and byte 127, was checked in all six candidate files: none occurred. All 30 displayed equation tags are distinct. These are integrity checks, not substitutes for the mathematical review.

The local premise is sibling p213_nonreduced_tube_finite_projection_research_20260831/RESEARCH_NOTE.md, SHA256 3001c94985c0d3e60f184ffd9f0e9591775ea026a98cd20ee538005edac11b7a. I read its exact Sections 2 and 6-9 to check the interface. Its separate independent PASS is not treated as an audit of the new global proof.

## 2. Independence and related work

The candidate was authored by /root/p213_skeletal_hostile. Root supplied the multiplicity outline and the omitted-coordinate warning, so root's earlier read is not counted as the independent review here.

I previously audited the product residual-curve functional and related current packets, and authored the common-moment, derivative-degree, and model-adaptation diagnostics. That familiarity is disclosed. I did not author this nonreduced global proof, supply its weighted outline, or edit its candidate bytes. In particular, my model-adaptation note is NOT an input theorem: no rationalization, resolution, modification transport, or model-capture conclusion from it is used below. The proof is audited on its actual given model.

## 3. Regular local algebra and the unramified coefficient ring

The intersection is the scheme-theoretic intersection of the REDUCED components E_i, not of their multiplicity-thickened divisors. Strict normal crossings puts their equations into a regular parameter system. At a closed p the ambient local ring has dimension n+1, the selected n equations leave a regular one-dimensional quotient, and at most one additional vertical component can occur. This justifies the two meanings of w and the integer N_p. Over perfect k, the regular finite-type curve is smooth. Its connected regular component is integral and proper; geometric connectedness is not needed.

The extension kappa(p)/k is finite separable. Finite-etale lifting over the complete henselian DVR gives a local finite-etale R_p of rank d_p, hence an unramified DVR with uniformizer pi. A simple-root Hensel lift in the completed local ring supplies the R-map R_p -> Ahat_p inducing the chosen residue identification. This map is injective: a nonzero DVR kernel would kill a power of pi, whereas the regular completed domain contains the original nonzero pi. This argument does not require a coefficient FIELD in mixed characteristic.

The formal presentation has been proved rather than inferred from a nonexistent semistable chart. The variables map to all n+1 actual regular parameters. Successive maximal-ideal approximation gives a surjection R_p[[X_0,...,X_{n-1},W]] -> Ahat_p. Equality of the full local Cartier divisor of pi supplies the relation F=pi-epsilon product X_i^{N_i}W^{N_p}. Since sum N_i>=n>=2, F has precisely the nonzero linear pi class modulo the square of the maximal ideal of the source regular ring. Thus quotienting by F gives a regular local domain of dimension n+1. The further surjection to the regular completed ring of that same dimension has zero kernel.

The unit epsilon can be lifted with unit constant coefficient. All coefficients belong to R_p. On each strictly smaller closed polydisc the nonconstant part has norm <1; therefore |epsilon|=1 on the whole open polydisc. None of these steps divides by a multiplicity or extracts a root, so residue-characteristic divisibility causes no hidden loss of scope.

## 4. Entire completed tube versus the punctured local premise

Berkovich's special-formal construction and Proposition 1.3 identify the completed local formal generic fibre with the actual tube, as analytic spaces and not just sets of Gauss points. The frozen algebraic isomorphism therefore identifies the ENTIRE p-tube with the displayed equation where all parameters have norm <1.

The selected x_i are nowhere zero on the generic fibre by the equation for pi. If N_p>0, w is also nowhere zero. If N_p=0, the locus w=0 can exist and is removed ONLY before applying (L). With m=N_0, coefficient field K_p, and exponents (N_1,...,N_{n-1},N_p), the punctured equation matches (L) exactly.

The source is viewed as a K-analytic space. The given T is restricted to this ordinary open source; it is not pulled back to K_p. The unramified extension is part of the description of that same source, not d_p ordinary-open sheets. Properness in (L) makes the pullback of each compact target test compact in the punctured tube, so its extension by zero to X_C is legitimate.

## 5. Global radii and parameter independence

For a vertical Cartier divisor, the generic section 1 of O(E_alpha) has a positive continuous formal norm. Locally its norm is |a_alpha|, giving U_alpha=v(a_alpha)>=0. Formal unit frame changes have norm one. The weighted equality sum N_alpha U_alpha=ell follows from the divisor of pi and tensor products of formal metrics. All U_alpha are finite on the generic fibre. The proof never differentiates these possibly nonsmooth global functions.

The simultaneous inequalities U_i>0 describe the tube of the full selected intersection. Its finitely many connected-component tubes partition it into ordinary open, hence clopen, pieces. The set with all U_i>=a is closed in compact X and lies inside that intersection tube. Its C-piece is compact, establishing K_a without a local product or a formal-open/ordinary-open substitution.

Changing a component equation multiplies it by a local unit, preserving its norm on the entire tube. For N_p=0, the second curve parameter has the form w'=wV+sum x_iB_i with bounded coefficients and V a unit. On all U_i>rho and 0<v(w)<delta<rho, the first term dominates. Conversely, v(w')<delta and those same normal bounds force |w|=|w'|. The explicit small-rho condition makes this common normal slice nonempty. A compact target test there has the same actual source support and the same pullback in both coordinates, so it compares the constants rather than merely comparing target images.

The omitted-component change is correctly NOT included in this norm-one/determinant-one parameter argument.

## 6. Rational lifts, finite bad points, and exact dominance

The z_i generate the actual Cartier ideals at eta_C. Hence z_i/x_i are units in A=O_{mathcal X,eta_C}. Knowing only their orders at selected components would not suffice, but the stronger property is explicitly required and available. Any residual rational f lifts to a unit of A because its residue is nonzero.

The supports defining B_f do not contain eta_C, so their intersections with the proper integral curve are finite. The bad set includes extra vertical components and zero-order bad points. Outside these tubes, the ratios and F have norm one pointwise. The proof does not strengthen this to ordinary-neighbourhood constancy at all such points.

At each bad p, reduction modulo the ideal of C is kappa(p)[[w]], despite the special-fibre multiplicities. Numerators and denominators of the finitely many relevant units have nonzero reduction. Each can be written w^rV+sum x_iA_i with V a unit and bounded coefficients. On W_rho the error has norm <=exp(-rho). Choosing r delta_p<rho gives STRICT domination and exact valuations, not an asymptotic equality. Quotients then give r_i=U_i+n_{i,p}s and t=m_ps. Both equations are first proved on W_rho; the subsequent radial inference does not assume them outside that domain.

## 7. Cutoff support, especially w=0

The compact support of phi lies in the weighted simplex with margin 4rho for retained radii and 4N_0 rho for the omitted weighted radius. The two bounds in (8.2) imply U_i>3rho, including U_0. The N_p term in the omitted-radius identity is retained.

The most delicate gluing point passes. On W_rho the support of 1-eta_p is contained in a closed smaller polydisc cut out by the actual analytic equation, with |x_i|<=exp(-rho) and |w|<=exp(-a_p). The series converges there; the zero locus is compact and entirely inside the p-tube. If N_p=0 it explicitly includes w=0. Thus compactness is NOT being inferred from the punctured (L) at a point outside its domain.

At w=0 the function eta_p is identically zero on an ordinary neighbourhood, because it is zero already for sufficiently small |w|. The support closure of 1-eta_p cannot meet the complement of the p-tube inside W_rho. It consequently extends smoothly by zero there. The finitely many bad tubes are disjoint, so the global eta gluing is valid in the ordinary topology.

All poles/zeros of the actual rational functions excluded from V lie in regions where eta vanishes on a neighbourhood. Combined with the 3rho support margin, this extends eta beta across those loci and across the boundary of W_rho as a compact ORDINARY test form. Only test forms are extended; no derivative-commutation rule for zero-extended currents is invoked.

## 8. Closedness and the signed principal-divisor integral

The error d'eta wedge beta vanishes for two distinct reasons, both included in the proof. If m_p is nonzero, the transition satisfies |t|>=|m_p|a_p>h, so chi(t)=0. If m_p=0, t is identically zero on the ordinary transition collar, hence d''t=0. Nonzero normal twisting n_{i,p}, or an extra N_p, does not invalidate the second case.

Where the logarithmic functions are defined, d'd''r_i=d'd''t=0. Derivatives of phi repeat a d'r_i; Omega_r has even total degree. This gives the displayed positive exterior sign in d'beta. Off the contributing bad tubes, chi'(t) vanishes on an ordinary neighbourhood because t=0 there and chi' vanishes near zero. This step uses continuity, not a false ordinary-open constancy assertion about the complement of tubes.

For a contributing p, chi' confines s to a compact interval bounded away from zero and below a_p. The normal margins keep all points away from every face of Q_p. Properness from (L) makes the corresponding source supports compact. The full target pullback introduces no hidden extra source points outside W_rho: whenever the translated phi and chi' are nonzero, the weighted equation itself forces all U_i>3rho.

The fixed-omission shear (u,s)->(u+n_ps,s) has determinant one. Its domain is weighted, but its determinant is not. The two differential blocks of t=m_ps contribute m_p^2. Translation preserves the full phi integral because the support remains inside the actual slice. For either sign of m_p,
integral_0^{delta_p} m_p^2 chi'(m_ps) ds = -m_p.
Closedness on the original n-dimensional source therefore yields sum ord_p(f)b_0(p)=0. No slicing or pointwise evaluation of an arbitrary current occurs.

If all m_p vanish the identity is immediate; no cutoff construction is needed in that case.

## 9. Positivity, non-geometrically-connected curves, and normalization

Define lambda on the group of divisors using the individually finite nonnegative b_0(p). Divisors have finite support, so no summability over all closed points is required.

The Riemann-Roch argument uses chi_k and degree_k, not the formula 1-g with an implicit H^0(C,O_C)=k assumption. For deg_k D=0, choose an effective H with deg_k H+chi_k(O_C)>0. Then h^0(H+jD)>0 for every integer j. Positivity and principal-divisor invariance imply lambda(H)+j lambda(D)>=0 for all positive and negative j, forcing lambda(D)=0. Applying this to d_q p-d_p q proves b_0(p)/d_p is constant. Zero is allowed. No rational point, algebraically closed residue field, or geometric connectedness is needed.

The canonical coefficient is N_0 d_p through the exact finite degree and restriction-of-scalars factor in (L). It is NOT assigned to the unknown T by positivity alone.

For omission of E_j, solve the weighted relation for U_0. The affine change q_j=A_jq_0+a_j has absolute determinant N_j/N_0, including the possible w term. Its inverse maps Q_j back to Q_0, so compact supports correspond. Top superforms acquire the square determinant; Lebesgue substitution removes one absolute determinant. Therefore b_j=(N_j/N_0)b_0 and c_j/N_j=c_0/N_0. The factor and direction are correct; the check N_0=2,N_j=3 gives 3/2.

## 10. Final source interpretation and exclusions

The hypotheses of (L), Sections 6-7, are checked rather than suppressed: original K is discretely valued, pi is its uniformizer, and K_p/K is unramified. Only with those additional local source conclusions AND (R) does an individual displayed coordinate-moment cell inherit the aggregate coefficient b_0(p), hence normalized ratio c_0/N_0.

This is not equality of T and a scalar integration current on all arbitrary tests. It does not manufacture a common-moment bridge to an unrelated source family. It also does not put the required compact strips inside an arbitrary ordinary W. The proof and ledger explicitly exclude selected horizontal normals, whose zero weights and potentially infinite radii require another global support argument. These limitations are genuine and preserved.

## 11. Source, visual, and preservation checks

The companion SOURCE_MATRIX.md records exact primary passages read independently and their use. Berkovich's introduction and complete relevant Section 1 theorem text were read through the primary web PDF. Screenshot requests yielded only textual references, so no visual inspection of that remote PDF is claimed.

The PDF skill was used for read-only source checking. I independently viewed the complete existing renders of CLD printed pages 410 and 493, verifying the finite-field calibration factor and formal-metric construction against the extracted text. Both pages were legible, with no clipping affecting the relevant formulas. Those images are source-QA inputs, not newly authored pages; their hashes are pinned.

No candidate, historical input, live manuscript, source PDF, git state, or production service was changed. This isolated audit is a mathematical review with explicit premises, not a production receipt.
