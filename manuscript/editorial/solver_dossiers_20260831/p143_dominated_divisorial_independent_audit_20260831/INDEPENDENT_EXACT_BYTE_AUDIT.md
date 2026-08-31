# P14.3 dominated divisorial density: independent exact-byte audit

Reviewer: p082_independent_reaudit. Date: 2026-08-31.

## Verdict

PASS for the full displayed dominated-divisorial-density theorem, including semivaluations with proper support and infinite values on nonzero ideals. PASS for the abstract USC antitone comparison. PASS, with its stated P14.2 dependency retained, for finite-energy Kahler raw = MP at every point of X^beth. No substantive mathematical gap was found in the frozen statement, proof, or diagnostics.

This is a mathematical audit, not production verification. The last corollary remains conditional on the exact frozen P14.2 USC input and uses the existing finite-energy correspondence identified in the packet. No claim about unrestricted Kahler cones, arbitrary pseudoeffective MP cones, continuous envelopes, or a monotone divisorial net is included. The separately authored full-Kahler truncation proof was not reviewed here.

## Exact scope and provenance

The candidate directory is `/private/tmp/nappt_p071_20260827/manuscript/editorial/solver_dossiers_20260831/p143_dominated_divisorial_research_20260831`.

| Frozen principal input | SHA-256 |
| --- | --- |
| statement.tex | 4ab292c9cfcc6c298968fca40819c09d560c12c96279947ddae46f4c22c5191f |
| proof.tex | bfd983aa2fa4580a9193bdd3f4fca78e7dd527d6ee1843f5ee647e4485180433 |
| diagnostics.tex | 773cd82034b3089abc0cb70112fab30249a55a5d5baf69f6a8680b4c192808d4 |
| MANIFEST.json | c2da7ad2ecb958415835af56e906b2e89a76587a365686b7a79c38e67be1b5a7 |
| INPUTS.json | ef05239ab54f8d4a952ff7b33a83f365270060d86b4958a25782dbf53c7c2418 |

The entire statement, proof, diagnostics, source matrix and dependency gate were read. The reviewer did not author the P14.3 argument. The reviewer previously independently audited the root-authored P14.2 USC construction; that history is disclosed, and its frozen statement/proof were reread here. Earlier work on Gauss fibres and curve metrics is not imported as an unproved comparison theorem. The parent's synopsis and preliminary assessment were not used as acceptance evidence. The geometry below was checked before using the desired raw = MP conclusion.

## 1. Topology and the compactness lift

The relevant spectrum is the closed subset of the product `[0,+infinity]^(coherent ideals)` defined by the semiring identities, with the extended order topology. Addition and minimum are continuous there, and the zero/unit conditions are closed. Thus compactness and Hausdorffness apply to this spectrum, not merely to finite-valued valuations. Pullback preserves finite sums and products of coherent ideals and is continuous on spectra.

For a proper bimeromorphic map of the stated smooth compact Kahler spaces, MP Remark 2.3.2 gives a lift of every rational divisorial point, including the trivial point. MP Theorem 2.3.6 gives ordinary density. The image of the compact source spectrum is closed in the Hausdorff target and contains that dense subset; it is therefore all of X^beth. This proves existence of a semivaluation lift even at proper support. There is no subtraction of two infinite values, no asserted uniqueness, and no extension of the valuation-only bijection in MP Proposition 2.1.6 by fiat. Ordinary density is used only here and does not provide the subsequent order inequality.

## 2. All-ideal monomial domination

This is the central new step, and it passes independently.

MP Lemma 2.1.1 constructs the central ideal as the sum of all coherent ideals with positive value. Consequently every positive-valued ideal is contained in it, not merely comparable to an arbitrarily chosen maximal ideal. Applied to O(-B_i), this gives Z contained in every selected B_i. A nonempty SNC intersection is smooth. Its connected components are disjoint, and the irreducible central variety Z lies in a unique one W. In particular the positive-weight list cannot contain more divisors than the dimension permits.

The monomial valuation along W uses positive rational transverse weights and weight zero in tangent directions. MP Proposition 2.3.4 gives point independence for evaluations of global coherent ideals, and Remark 2.3.5 gives a rationally scaled divisorial valuation. The argument does not treat W as an ordinary closed point or pretend that a tangent function vanishing at one point is zero in the local ring of W.

For each positive threshold s, the exponent set defining c_s is upward closed. Every minimal exponent lies in the finite box `beta_i <= ceil(s/a_i)`: beyond that bound, decreasing its i-th coordinate still leaves weight at least s. The finite minimal monomials generate the entire global sum because the corresponding Cartier ideal inclusions hold globally. This proves coherence without assigning a semivaluation to an infinite sum. Its value is the minimum of finitely many sums, each at least s. Zero exponents are omitted, so infinite component values cause no undefined product.

Here is a direct check of the analytic membership assertion. Write a germ as a convergent power series in the transverse coordinates, with holomorphic coefficient germs in the tangent coordinates. Iterated Taylor expansion to degree `ceil(s/a_i)-1` in each transverse coordinate leaves a remainder in the ideal generated by the pure powers `z_i^ceil(s/a_i)`. Every such power is in c_s. There are only finitely many remaining transverse exponents. Vanishing of those coefficient germs whose weight is less than s is therefore precisely membership in c_s. This is an analytic ideal statement, not only formal membership after completion. Point independence and finite local generators of j imply j contained in c_s near every point of W when s<q(j).

The annihilator then resolves the actual-centre issue exactly as claimed. The coherent quotient `(j+c_s)/c_s` vanishes on a neighborhood of W; its annihilator k is coherent, is the unit ideal there, and satisfies k*j contained in c_s globally. If the lifted semivaluation had positive value on k, central-ideal maximality would force k contained in I_Z, impossible at Z contained in W. Thus its value on k is zero. Multiplicativity and reversed ideal inclusion give

`vtilde(j) = vtilde(k*j) >= vtilde(c_s) >= s`.

This is an inequality for every global coherent ideal j. It does not require Z=W, equality of the lift with a monomial valuation, or extending a local semivaluation at a chosen closed point. Nonzero j has finite monomial value; letting s increase proves the claim. Monomial value zero is automatic, and the zero ideal has infinite value on both sides. The annihilator may depend on j and s, which does not affect the fixed valuation q or the universal inequality.

## 3. Principalization and the dominated approximation net

The required classical input is finite analytic principalization on a compact smooth complex manifold, followed if needed by resolution of the pair to obtain globally smooth SNC components. Bierstone--Milman Theorem 1.10 is a precise primary locator for principalization; see the source ledger. Its analytic and quasi-compact scope is sufficient here. Smooth-centre blowups preserve compact Kahlerness, so every lifting space used in Step 1 has the required hypotheses.

The latter preservation can also be checked geometrically: on a smooth blowup, O(-E) has a smooth Hermitian metric with curvature positive on the projective fibres of E. The pullback of a Kahler form is semipositive, and its kernel on E consists exactly of vertical tangent directions. Compactness then makes the sum of that pullback and a sufficiently small positive multiple of this curvature positive everywhere. Iterating gives the stated property; no false claim that every bimeromorphic image of a Kahler manifold is Kahler is used.

Principalizing the product suffices for the individual ideals. In a local domain, if a product of finitely generated nonzero ideals is invertible, each factor has a fractional-ideal inverse and is invertible. On the smooth resolved space its effective divisor is supported on the common SNC divisor. Hence each specified ideal value is the displayed finite sum of nonnegative integral multiplicities times component values, including infinity.

After discarding zero weights, every retained divisor contains the actual centre. A discarded SNC component cannot contain the selected stratum W: an additional distinct coordinate divisor cuts W in positive codimension, if it meets W at all. Its monomial value is zero. Thus the formula for every principalized input ideal is correct, even if that discarded divisor happens to contain a smaller part of the centre as a set.

Finite positive component values can be approximated from below by positive rationals, and infinite ones by arbitrarily large rationals. A finite-valued ideal cannot have a positive coefficient on an infinite component. Thus one can satisfy all finite error bounds and all infinite lower thresholds simultaneously. Pushforward remains rational divisorial and dominated on all ideals by functoriality. If there are no positive components, the trivial valuation handles all specified values.

The resulting choices meet every finite-coordinate neighborhood. Indexing by finite ideal sets and an integer accuracy parameter gives a convergent net; domination by v holds individually, not between different indices. This is sufficient for closure in a generally nonmetrizable product topology. The zero and unit ideals have fixed prescribed values. In dimension zero the trivial point handles the degenerate connected-manifold case.

## 4. The abstract comparison has the right semicontinuity directions

MP potentials are USC as decreasing limits of continuous PL functions. For a dominated convergent net q_lambda, antitonicity of F and divisorial agreement give `F(v)<=phi(q_lambda)` at every index. USC of phi then gives `F(v)<=phi(v)`. In particular, if phi(v) is minus infinity, its values along the net eventually lie below every real threshold, and the conclusion still follows. No convergence of F(q_lambda) is assumed.

Conversely MP Theorem 4.3.8 applies to the USC function F, with values in the allowed extended range, and gives phi<=F from their divisorial equality. This use needs neither positivity of F nor antitonicity of phi. Both inequalities therefore prove literal all-point equality.

## 5. Finite-energy correspondence and raw formula

The exact external input is an existing finite-energy MP potential associated to the DXZ finite-energy test curve, with its divisorial values given by the radial Lelong construction. MP Theorems 5.1.4 and 5.1.7 and Section 5.2 explicitly work in the Kahler setting; DXZ Section 3.4 and Theorem 3.17 also have compact Kahler scope. By the DXZ definition, finite energy is assigned only to metrics represented by an unperturbed positive-mass test curve. Thus this corollary does not need a new bounded-metric descent theorem for arbitrary inverse-system objects. Other components have the same integer multiplier ideals at interior levels, by the stipulated transition interface.

One source precision is worth recording: DXZ Proposition 3.1 itself is printed under a projective hypothesis. It is not directly a full-scope citation for the Kahler divisorial formula. The local input in its proof, published DX22 Lemma 3.14, explicitly holds on any complex manifold. It states the Lelong-number identity for the USC supremum of a nonempty family of nonpositive psh functions. Adding a common bounded local potential and shifting the radial function by b>c makes the family of level potentials satisfy those hypotheses. Pulling back to a model realizing a rational Gauss divisorial valuation and applying that local identity gives the infimum of the level Lelong numbers. Generic divisor coefficients obey the same identity: monotonicity gives one inequality, and the pointwise lemma, with pointwise Lelong numbers bounded below by their generic values, gives the other. No common generic point for an uncountable family is required. Thus the finite-energy divisorial interface has a local justification without projectivity, and does not use the new all-semivaluation comparison circularly.

The norm convention is also consistent. If u_t denotes the squared-norm DXZ ray, the ordinary-norm MP ray is `R_s=(1/2)u_(2s)` with `s=-log|z|`. Its test curve is half the DXZ test curve with the same parameter tau. Both the potential and logarithmic Lelong denominator are halved, leaving the coefficient, integer multiplier ideals under the respective norm conventions, and terminal c unchanged. There is no numerical factor of two in the raw divisorial value. At the trivial valuation each interior multiplier ideal is nonzero and has value zero, so the raw value is c; the MP value is the same radial slope.

The remaining deduction is exact and short. The raw function is bounded above by c. Each ideal evaluation increases under q<=v, so its first supremum increases, its negative decreases, and the outer supremum remains antitone. Frozen P14.2 supplies USC on all semivaluations. The preceding comparison therefore yields raw = MP everywhere, including proper support and the value minus infinity. Only the USC part of P14.2 is imported; none of its finite-ideal continuous approximants is declared MP psh.

## 6. Diagnostics, preservation, and review boundary

The curve and local `(sqrt(2),+infinity)` examples have the asserted values and domination. The normalized-simplex obstruction is also correct: coordinatewise decrease under a fixed positive weighted sum forces equality. It is a warning against one rounding method, not a counterexample to the unnormalized SNC-cone construction.

A fresh read-only check verified all 12 manifest entries and all seven pinned input entries, including both P14.2 principal hashes and the live Chapter 71/72 hashes. After its source was inspected, the candidate's read-only checker was also run against its existing draft output: 10 unique labels, 10 internal reference uses, no unresolved/duplicate labels, and no reported draft-log warnings/errors/box defects. The existing log SHA is `42cdfdb1944b4d15a1d4ce60d719bd774cc6e09d3879b82a6123a07e5c55e691`. No candidate PDF exists and no candidate-PDF visual QA is claimed. Relevant complete MP/DXZ primary PDF pages were separately rendered and inspected; details and hashes are in SOURCE_LEDGER.md.

Only this isolated audit dossier is authored. The candidate and live files are preserved. No production endpoint, external submission, approval escalation, permission workaround, or inventory change occurred. The result is suitable for the next independent/production gate in its exact finite-energy and conditional scope, not as evidence that any broader pending result is established.
