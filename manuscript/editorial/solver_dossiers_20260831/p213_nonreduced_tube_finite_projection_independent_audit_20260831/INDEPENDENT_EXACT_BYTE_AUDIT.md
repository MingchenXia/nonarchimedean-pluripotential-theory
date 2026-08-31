# Independent exact-byte audit: finite projection of a multiplicity tube

Date: 2026-08-31. Reviewer: /root/p081_weighted_repair_fresh.

## Verdict

PASS for all conclusions within their stated hypotheses: the general-field analytic finite-flat map and proper current pushforward; the additional unramified-DVR generic Gauss-fibre uniqueness; and, conditional on the displayed representation premise (R), the individual source-cell comparison in Section 7. No substantive mathematical gap or required correction was found in the frozen packet.

This is a local theorem for the explicitly given equation, not a completed nonreduced-SNC residual-divisor theorem. Ordinary-W locality, global compact cutoffs/divisor relations, arbitrary-wall realization, full P21.3, production acceptance, and live integration remain outside this verdict.

## 1. Exact bytes and independence

Candidate directory: sibling p213_nonreduced_tube_finite_projection_research_20260831.

- RESEARCH_NOTE.md, 21186 bytes: 3001c94985c0d3e60f184ffd9f0e9591775ea026a98cd20ee538005edac11b7a.
- SOURCE_LEDGER.md, 4133 bytes: cdf06f52596133e91abaa2c2e5870bbfb2db0f56ee71dd10dd2311636ccb9898.
- freeze.mjs, 4180 bytes: 13cd68503e1d9d97c7efc1cc8113614e689a94f9cc6b2e374e5a1355354672ab.
- MANIFEST.json: d82be02c8b536651f8e9366c407448139c88cf7044158edc419834c515b58fec.
- SHA256SUMS: ffa51a4eb20e08654387444c57b8fff6e8bb995f182ed112c694bf995b476c6f.

The author supplied the freeze before this audit. I read the complete note, source ledger, and freeze script. My independent read-only checker matches all three announced pins, all eight manifest entries, and all nine checksum entries. No forbidden control bytes were found. The author script was inspected rather than used to rewrite anything.

Root authored this candidate. I did not contribute its argument or provide a replacement proof. I previously audited the strictly semistable-wall, torsor, representation, and common-moment packets; that familiarity is disclosed, but none of those earlier pass labels certifies the present result. The prior reduced-model note is motivation only. The representation identity (R) is expressly assumed only in Section 7, not self-certified here.

## 2. Generalized Banach division is valid

Section 3 works with the ordinary commutative unital non-Archimedean Banach-algebra convention. All estimates use submultiplicativity and the ultrametric inequality, not multiplicativity of the Banach norm.

For k=jm+r, the remainder norm is at most ||c||^j R^r<=R^k. Every term of the quotient has norm at most
||c||^i R^{k-m(i+1)}<=R^{k-m}.
Thus the maps extend from polynomials to restricted series, because ||f_k||R^k tends to zero. Completeness and continuity give all three identities in (3.4). The finite remainder space carries the weighted coefficient norm, so its inclusion and projection are bounded.

Multiplication by E followed by division has norm at most R^{-m}||E||<1. The Neumann series therefore converges in bounded operators, including for arbitrary positive real R. Applying the division identity to f-Eq gives f=(P+E)q+r. Applying D_P to a zero decomposition proves uniqueness.

The remainder map for F is a bounded projection onto the degree-<m polynomials. Its kernel is exactly F times the Banach algebra, hence that principal ideal is closed. The resulting quotient is topologically, not merely algebraically, free of rank m over A. The inverse maps are bounded by the construction; the weighted finite-rank norm is equivalent to the usual norm on A^m.

This last topological assertion matters for generalized affinoids. CLD11.4.4 explicitly requires the finite-module Banach topology, not just an abstract finite algebra. The proof provides it. No generalized preparation theorem, coefficient-field enlargement, or root of epsilon is needed.

## 3. Applying division to the whole analytic preimage

On every compact box in Q, all upper z-radii are <1 and lower radii are >0. The product annulus has its standard complete generalized affinoid algebra and submultiplicative Gauss norm. The strict inequality defining Q gives ||lambda||<1, where lambda=pi product z_j^{-a_j}.

Writing epsilon=sum e_j(z)X^j is legitimate: bounded original coefficients and the upper radii <1 give convergent z-series with ||e_j||<=1. The nonconstant z-part of e_0 has norm <1. Its constant coefficient has norm one, so e_0 and its inverse both have norm one.

Choosing ||lambda||^{1/m}<R<1 gives the exact estimates ||c||<R^m and ||E||<=R^{m+1}<R^m. The zero space in that closed R-disc is therefore a finite free affinoid space of rank m over the box.

Equation (4.3) proves that this is the ENTIRE inverse image. On both the original domain and the closed-disc zero space, |epsilon|=1, so |x|^m=|lambda| and |x|<R. Conversely every original solution over the box lies there. The identification is an equality of analytic subspaces obtained by restricting the same analytic equation to a domain containing all its points, not a replacement of a possibly nonreduced space by its point set. No boundary roots or other components are discarded. The rank-m fibre algebra is nonzero at every base point, and a nonzero finite algebra over a complete field has a Berkovich point, establishing surjectivity.

Full-dimensional small boxes whose interiors cover Q give a generalized affinoid neighborhood cover of B. Finiteness is G-local on the target, so the local maps give a finite map globally. The finite free module remains free after completed base change to an affinoid algebra, which verifies analytic flatness, rather than merely naive flatness of one local ring. No currents are glued on this analytic-domain cover.

## 4. Geometry and compact support

The source is a closed analytic hypersurface in an ordinary open polydisc. It is good and separated. Finiteness gives absence of relative boundary; the base B is boundaryless, so D is boundaryless. Finite flatness of positive rank over the pure n-dimensional base gives purity of dimension n. This is the analytic finite-flat dimension statement; no equality of analytic dimension with the Krull dimension of an arbitrary non-strict affinoid is required.

A compact set in Q is contained in a finite union of boxes compactly contained in Q. Its inverse image in B is closed in the corresponding compact union of polyannuli. Taking finite inverse images under g proves properness of q. A countable compact exhaustion of Q, chosen with interiors exhausting Q, pulls back to a compact exhaustion of D. In particular the source has the paracompactness needed in Section 7.

All compact target forms and their derivative primitives consequently pull back to actual compact source forms. This is the precise support assertion needed for the current argument. No extension of T from a smaller arbitrary ordinary open is attempted.

## 5. Positive-current pushforward and canonical degree

Section 5 defines q_*T by the actual moment pullback. On a fixed compact target support, that pullback is continuous in the usual smooth test topology; properness preserves compact source supports. Positivity gives an order-zero scalar distribution, hence a locally finite positive Radon measure.

Deleting one d' coordinate factor from the interleaved volume form gives a compact (n-1,n)-primitive. Transposition and d'T=0 imply that every distributional partial derivative of the target measure vanishes. Convolution on smaller Euclidean balls, followed by overlap and connectedness of convex Q, gives one finite constant b>=0. The locally constant convolution values converge, as seen by a fixed integral-one test. No pointwise evaluation or slicing of T is used. The general statement correctly needs only d'T=0.

The canonical value is a separate finite-degree calculation. The characteristic skeleton is the inverse image of the torus Gauss skeleton; finite flatness and boundarylessness give its full-dimensional part. Its tropical image is Q, and properness of q makes the moment pleasant in the precise sense of CLD14.1.7. Taking the identity target torus map and a small open n-cell about a given u satisfies CLD14.5.3: the actual analytic map is finite flat of degree m above that Gauss point. Thus the target canonical calibration is m.

These canonical degrees include analytic multiplicities. The general-field statement does not assert that D or every fibre is reduced. For example in characteristic p with m=p, all a_j=0, epsilon=1, and pi a p-th power in L, the equation is a p-fold thickening. Its finite-flat degree and canonical integration coefficient are p, not the coefficient of its reduced subspace. The exact CLD source construction uses finite-flat local degrees and imposes no generically reduced hypothesis here.

Viewing the same L-analytic space over K with L/K finite multiplies canonical calibration by the full degree [L:K], by CLD14.4.3. The arbitrary K-current argument is then performed directly on that K-analytic space. It is not a base-change operation on an L-current or a pullback through g.

## 6. Generic Gauss fibres: exact value group and total algebra dimension

The additional hypotheses in Section 6 are essential: pi is a uniformizer of K and L/K is unramified, so v(L^times)=ell Z. The rationally independent tuples form a dense subset of every open subset of Q; the excluded rational relations are a countable union of proper affine hyperplanes.

For such a tuple, the Laurent Gauss valuation has value group ell Z+sum u_j Z. Distinct monomials have distinct valuations, and the rational function field is dense in the completed residue field by CLD12.1.6. Completion does not enlarge this value group: a sequence converging to a nonzero element eventually has that element's absolute value. Conversely the field already contains constants and coordinate monomials, so every value in the displayed group occurs.

Let A_u be the entire rank-m fibre algebra. Every residue field F of A_u is finite over H, and the equation gives v(x)=(ell-sum a_j u_j)/m. This class has exact order m modulo v(H^times): multiplying by m puts it in that group; any integer multiple putting it in the group must have integer coefficient j/m of ell by rational independence.

The needed fundamental inequality has an elementary check here. The elements 1,x,...,x^{m-1} in F have values in distinct cosets modulo v(H^times). In any nonzero H-linear combination their nonzero terms have distinct valuations, so the least-valued term cannot cancel. They are H-linearly independent. Thus [F:H]>=m, with no separability or defectlessness hypothesis.

The quotient map A_u onto F has H-dimension m in its domain and at least m in its codomain. It is therefore an isomorphism. This proves simultaneously that A_u is one field of degree m, that no other factor is present, and that there is no nilpotent length. It does not confuse a residue-field degree with the dimension of an unreduced fibre. A finite extension of the complete non-Archimedean field H has a unique absolute value extension, hence gives one analytic point.

The proof does not assume the conclusion for all radii. Its dense-set conclusion is used only through constant degrees and cell geometry in Section 7.

## 7. Actual source cells and the conditional comparison

Now assume (R), with both d'T and d''T zero, as the note explicitly requires.

The skeleton here is closed in D because it is the actual inverse image of the closed torus Gauss skeleton. Since D is boundaryless, the n-dimensional characteristic skeleton agrees with that skeleton. Thus the locally finite compact-cell decomposition required by (R) applies to a closed paracompact source subset. By CLD14.1.4(b), its g-cells are already convenient in this boundaryless setting; refining as in Lemma14.1.5 is harmless. Use the ordinary q-coordinates for the coefficients b_C.

Each top-cell image has nonempty open interior in R^n. Choosing an independent u in that interior selects its actual source point above the Gauss point eta_u, not merely a point with the same tropical image. Section 6 gives a unique fibre point of degree m there. Proposition14.2.2 then makes the local finite degree m on the whole convenient-cell interior, and the canonical q-coordinate coefficient is m over L.

Over K, CLD12.1.8(b) applies to the finite coefficient extension of the TORUS: its graded residue extension is algebraic, and the K-Gauss point has exactly the L-Gauss point above it. Its completed-tensor description is a field, preserving the finite degree [L:K]. Composing with the rank-m map therefore gives the unique source point and total degree m[L:K]. This changes no current and aggregates no additional source sheets.

Two distinct top-cell interiors cannot have images overlapping in an open set: an independent tuple in that overlap would give two distinct points above the same Gauss point. On a compact target neighborhood, properness and the closed skeleton make only finitely many cells relevant. Their lower-dimensional cells and boundaries have lower-dimensional images. Removing that finite exceptional set leaves a small ball inside the chosen top-cell image seeing exactly that one represented top sheet.

For a compact test in this ball, q^{-1}(supp h) is compact. An ordinary smooth source cutoff equal to one near it is available on this good separated boundaryless source. Applying the actual identity (R) with that cutoff and the same target top form yields b_C integral h; the independently established pushforward formula yields b integral h. Choosing integral h nonzero gives b_C=b. No equality on a dense set is used directly to identify arbitrary currents or arbitrary source test forms.

The resulting ratio (7.1) is therefore correct under (R). It concerns this coordinate moment on this tube, not comparisons between different p-tubes or arbitrary moment refinements. The stronger local-affine-separation adjective is not imported.

## 8. Aggregation diagnostic and excluded extension

The example in Section 8 checks: if pi^{1/m} and all m-th roots of unity lie in L and the residue characteristic does not divide m, x^m=pi splits into m distinct components, each mapping isomorphically to B when a_j=0. Arbitrary nonnegative constants on those open-and-closed components give closed positive currents; the pushforward sees only their sum. This genuinely demonstrates why finite flatness alone cannot identify individual coefficients. It violates the uniformizer/unramified value-group condition used in Section 6 and is not a counterexample to that result or P21.3.

The prospective formula (9.1) also has the correct algebraic support-budget sign after substituting r_i=U_i+n_{i,p}s into the weighted radius relation. It is labelled only as a necessary future budget. No existence of that global model presentation, global primitive, principal-divisor identity, or inclusion of a residual tube in the current's arbitrary ordinary domain is claimed.

## 9. Source/verification record and minor exposition points

No mandatory correction is requested. For eventual typesetting it would be useful to say explicitly that b_C uses q as its affine coordinates; this is already the normalization used in Section 7's canonical-coefficient sentence. Likewise Omega in q^*(h Omega) is first the coordinate top form on the target Q. These are notation clarifications, not missing mathematical hypotheses.

SOURCE_LEDGER.md records the exact primary interfaces, including additional CLD11.4.4-11.4.6 checks that close the generalized-affinoid topology and flatness interface. No broad Weierstrass theorem or defectless-field theorem was silently assumed.

The PDF skill was used only for read-only inspection of ten full CLD source pages. All were legible, with no rendering warning or failed render. No PDF artifact or TeX compile was produced. The reviewer-created temporary PNGs are removed after recording their hashes and commands. Candidate and source hashes are preserved.

The machine checks establish byte identity, not mathematical validity. The reasoning in this report supplies the independent scoped verdict. Production verification and any future live integration gate remain unchanged.

