# Complete actual Hultberg arXiv v1 reading notes

42 pages, 21 matching displays; no journal/recursive proof clearance.

# Hultberg toric-bundle source — actual reading 1

Read the complete selected text and matching displayed image for physical pages 1–2 of arXiv:2412.04169v1, 5 December 2024. The exact source is 42 physical pages; these two pages alone are credited. The receipt separately binds source, preparation, image, text and note hashes.

The introduction treats a semiabelian variety as an extension of an abelian variety by a torus, split after a finite field extension. The Weil–Barsotti identification imports the Picard-zero extension classification, not arbitrary Picard classes for a semiabelian group extension. For a general split torus torsor over a base, isomorphism classes are Hom(M,Pic(B)); character m uses the inverse action chi^(−m). The associated toric bundle is the contracted product of the torsor with the fan variety, whose fiber identification is canonical only up to torus action. An invariant divisor has a canonical induced global divisor, but fiber trivializations are not absolute global coordinates.

The text claims corresponding metrized and adelic torsor classifications and divisor transports, whose definitions/proofs are in Section 3 and have not yet been read. For a semiabelian compactification, multiplication extends for the chosen fan and toric canonical metrics are compared with transported canonical metrics of base Picard-zero classes. It explicitly says the mixed torus–abelian compactification is not a single polarized dynamical system: toric and abelian line-bundle contributions scale differently. This is relevant to keeping n versus n² and total multiplication degree distinct in the Xue audit, but no formal scaling theorem is cleared by the introduction alone.

The setup takes a complete rational fan refining the normal fan of a rational polytope and an integrable torus bundle over a proper base over a global field. The phrase “Cartier divisor defined by a rational polytope” requires integrality of the support-function slopes, or clearing denominators and a Q-Cartier formulation; an arbitrary rational interval such as [0,1/2] does not define an integral Cartier divisor on P1. Do not silently conflate rational and lattice polytopes. A fan refinement need not be projective merely because the original normal fan is projective. Source Section 2–3 may supply further conventions; do not infer hidden assumptions yet.

Definition 1.1.1 orders the Zhang minima increasingly: zeta_i is the infimum threshold for the height sublevel Zariski closure to have dimension at least i−1. Thus zeta_1 is the absolute minimum and zeta_(d+1) the essential minimum, opposite to the common descending indexing. The displayed definition has been read; subsequent minima theorems remain unread. No new book input, full-source credit, original result or independent-model verdict occurs.

---

# Hultberg toric-bundle source — actual reading 2

Complete selected text and matching displayed image read for physical pages 3–4 of the exact arXiv v1. Four of 42 pages have now been actually read in two chronological views. The main proofs and all later conventions remain unread; no result is cleared by its introductory statement.

Theorem A states the essential minimum of rho(Delta)+pi*L as the supremum over m∈Delta of the essential minimum of L+c(m) plus the global roof theta(m), assuming some L+c(m) is geometrically big. Under semipositivity of every such base metric, it states an absolute-minimum infimum over the interior Delta°. Remark 1.1.2 extends this to the closed polytope when every base class is geometrically big. Preserve supremum versus infimum, absolute versus essential, and the extra semipositivity/bigness hypotheses. The meaning of interior for lower-dimensional polytopes still needs the later conventions or a full-dimensional hypothesis; no empty-interior formula is silently imported.

Theorem B assumes an adelic integrable projective toric bundle of relative dimension t with smooth generic fiber, a smooth projective base of dimension g, and a flat projective model of that base. It uses operational arithmetic Chow cohomology to permit a model which need not be regular. Its exact factorial formula is i! rho(Delta)^(t+i) pi*gamma = (t+i)! integral_Delta (c(m)+theta(m)[infinity])^i gamma dm, with gamma of codimension g+1−i. The constant Green class is normalized to height 1 on every point. The full mixed expression, factorial conversion, degree/codimension bookkeeping and base intersection must survive any specialization. Polarization and approximation are described but their proofs are later.

Theorems C–D specialize to a semiabelian compactification, an ample symmetric canonically metrized base line bundle M, and an ample toric Cartier divisor. C prints the negative height formula −(d+1)! integral_Delta hhat(c(m)) dm; D makes the first g+1 successive minima equal and gives later ones as negative max-over-faces/min-over-face Néron–Tate heights, with face dimension t+g+1−i. The text transfers hhat through the polarization to the dual abelian variety. This normalization must be checked in Section 6 before reuse: scaling the base polarization changes that transferred quadratic form, and the base volume/factorial in the arithmetic intersection must be calibrated against Theorem B. Do not assume that the printed short formula already incorporates the usual base-degree factor, and do not claim a verified contradiction without reading the definitions/proof.

The article proposes, historically, an arithmetic analogue of the cohomology-ring description of smooth toric bundles. This introductory suggestion is not automatically a current 2026 open problem. Section 2 will define cycles and integrable intersections, Section 3 the metric transport, Section 4 the Okounkov and minima arguments, and Section 5 the BKK proof. No independent-model verdict, manuscript change, original theorem or new canonical problem status occurs.

---

# Hultberg toric-bundle source — actual reading 3

Complete selected text and matching displayed image read for physical pages 5–6 of arXiv v1. Six of 42 physical pages have now been actually read. The acknowledgements and organization confirm that Section 6 contains the semiabelian applications, but none of their proofs is yet credited.

Definitions 2.1.1–2.1.4 use normal toric varieties with split dense torus, dual character/cocharacter lattices and real piecewise-linear virtual support functions on rational fans. Toric Cartier divisors are invariant divisors, and real Cartier divisors are the real tensor extension. Theorem 2.1.5 explicitly identifies real virtual support functions with real toric Cartier divisors, consistent with the need to retain real coefficients when the polytope is not lattice-integral. This does not clear the introduction's use of integral Cartier terminology for arbitrary rational polytopes. The printed normal-fan definition uses maximizing faces; the sign of its later concave support-function dictionary must be checked before adopting a roof formula.

The displayed tropicalization on p6 sends x to m↦|chi^m(x)| but labels the codomain N_R. Literally this is not an additive homomorphism M→R: its value at the zero character is 1, and multiplication of characters multiplies absolute values rather than adding them. A logarithm (with the sign fixed by the subsequent convention) is missing. This is a local formula diagnostic, not a claimed refutation of the main theorems; do not reproduce the raw norm as an additive tropical coordinate.

Green functions use g+log|f| extending continuously across a local Cartier equation; thus g is the ordinary minus-log norm convention. Adelic metrics agree with one normal proper model on a dense open subset of the arithmetic/function-field base. Adelic effectivity requires an effective divisor and nonnegative Green functions at every place. Integrability is a difference of semipositive metrics, and the d+1-fold arithmetic pairing factors through integrable adelic real Cartier divisors. Continuous metrics alone do not automatically define the pairing. The cited Zhang/Ballaÿ intersection proofs remain imported and unread recursively. The real-coefficient definition continues on the next page.

This reading changes no book content and introduces no independent verification receipt, original theorem, full-source credit or canonical status change.

---

# Hultberg arXiv v1 — actual source reading 04

Physical pages 7–8 were read completely in the selected text and matching rendered two-page display. No other pages receive credit.

- Heights of varieties are explicitly unnormalized top arithmetic intersections Dbar^(d+1), rather than divided by (d+1)deg_D(X). This settles that possible explanation for the preliminary Theorem C coefficient question: a normalized variety height is not the convention here. The precise transferred Néron–Tate height remains to be checked in section 6.
- Toric concave metric functions, effective metrized polytopes, the group completion, local/global roof functions and almost-everywhere canonical adelic fans are introduced. Local weights for number fields are [K_v:Q_v]/[K:Q]. Carry these weights into every global roof and intersection; function-field place weights depend on the absolute-value convention and are not a universal unweighted sum.
- Definition 2.1.8 literally calls the hypographs of nonnegative concave roofs polytopes. General continuous concave roofs need not be polyhedral. The asserted isomorphism with all semipositive continuous metrics therefore needs either a convex-body/completion convention or a restriction to polyhedral metrics; no such clearance was supplied by these pages. Do not replace continuous semipositivity by model metrics silently.
- Theorem 2.1.10 is for a discretely valued nontrivial complete field and fixed compatible toric model fan. The printed proof says the divisor corresponding to the concave function psi is effective precisely when psi is nonnegative. In the usual convention already used with roof duality, the canonical effective divisor D_infinity on P1 has psi(u)=min(0,u), ordinary Green function log max(1,|z|), and roof zero on [0,1]. This is a literal sign diagnostic to check against their earlier/later conventions, not a verified counterexample to the arithmetic BKK theorem.
- A complete fan is incorrectly described once as lying in M_R before its model fan is placed in N_R plus the nonnegative real coordinate. Preserve the actual character/cocharacter roles. Compatibility is local piecewise linearity and eventual canonical models, rather than arbitrary fan refinements or universal projectivity.

No independent verifier receipt, new book integration, or main-theorem clearance is claimed.

---

# Hultberg arXiv v1 — actual source reading 05

Physical pages 9–10 were read completely in the selected text and matching rendered two-page display. No other pages receive credit.

- Definition 2.1.13 introduces place-wise interior inside a compatible effective cone; its vector-space/topological meaning must remain explicit for later directional derivatives.
- Section 2.2 defines the Okounkov body using a regular geometric point, completed local parameters and lexicographic valuation. Valuations are of nonzero sections and the scaled degrees must start at n=1 even though the displayed union literally starts at zero. Choice of flag/coordinates is load-bearing for transforms and absolute-minimum comparisons.
- The printed increasing filtration is spanned by section vectors of height at most t, and the printed transform is the infimum of membership thresholds. Standard concave Boucksom–Chen transforms instead use a decreasing filtration and a supremum. Their later metric/section sign convention must be inspected before importing this definition: an increasing height filtration produces the negative of the usual concave roof unless signs are changed. This is a definition diagnostic, not a cleared main-theorem counterexample.
- Theorem 2.2.1 asserts essential minimum = maximum of the transform for geometrically big real divisors, then absolute minimum = infimum if semipositive, referencing QY23/Ballaÿ. Need check the controlling primary imports, chosen flag and sign; the literal text here does not itself clear the wider absolute-minimum assertion.
- Theorem 2.2.2 keeps geometric volume d! times body volume, arithmetic positive-part volume (d+1)! integral max(0,G), and chi volume bounded by (d+1)! integral G, with equality under finite lower bound. The arithmetic normalization is explicitly distinguished from Ballaÿ's.
- Theorem 2.2.3 uses geometric nefness for volume=degree and semipositivity for chi volume=unnormalized arithmetic height, within the section's geometrically big projective setting. Do not remove these ambient hypotheses downstream.
- Section 2.3 explains the need for an adapted toric flag to identify the body and transform with the Newton polytope and toric roof. A smooth projective toric refinement is selected, rather than declaring every complete fan projective. This clarifies the earlier refinement scope.

No independent verifier receipt, book integration, recursive source clearance, or main-theorem clearance is claimed.

---

# Hultberg arXiv v1 — actual source reading 06

Physical pages 11–12 were read completely in the selected text and matching rendered two-page display. No other pages receive credit.

- The toric flag is from a smooth maximal cone with primitive rays forming a lattice basis. Translating the Newton polytope chooses a divisor representative with no support on the flag components, so monomial valuations identify with lattice coordinates. This adapted-flag statement does not settle arbitrary flag transforms.
- Definition 2.3.2 literally prints -log ||chi^m||_(v,sup) = theta_D(m/l) for sections of lD. Tensor power homogeneity requires the left side to be divided by l (equivalently the right side multiplied by l). A shifted canonical metric with positive constant c already gives lc versus c, and the standard Fubini–Study entropy roof gives the same scaling discrepancy for nonzero roof values. Treat as a literal definition error needing correction, not a refutation of the usual toric roof dictionary.
- Theorem 2.3.4 gives the norm of a sum at least the largest monomial summand norm, the controlling orthogonality direction. Proposition 2.3.3's proof then uses a section-height inequality and membership signs that require a consistent height convention. Together with the preceding increasing-filter/infimum definition, the printed signs cannot simply be imported as a proof of the standard concave-transform equality. The intended equality is classical in the properly signed framework; do not claim its failure from this exposition.
- The roof sum does include all local weights; its finiteness depends on canonical metrics outside finitely many places. The proof's abbreviated summation must not delete these weights.
- Section 2.4 develops arithmetic Chow homology and operational first Chern classes on flat projective models with smooth generic fiber, allowing nonregular special fibers. Intersection is multilinear and symmetric for hermitian line bundles. The displayed Green-current formula uses minus log norm, so squared-norm/curvature conventions need explicit translation before book use.
- The operational construction is called preliminary and does not assert pushforwards for arbitrary non-generically-smooth morphisms. Statements about unavailable pushforwards are historical to this 2024 source, not current literature conclusions.

No independent verifier receipt, book integration, main-theorem clearance or uninspected primary-import clearance is claimed.

---

# Hultberg arXiv v1 — actual source reading 07

Physical pages 13–14 were read completely in selected text and the matching image. No other reading credit.

Operational arithmetic cohomology is a compatible family on projective test schemes with smooth generic fiber. Proper compatibility is stated for generically smooth maps plus a fundamental-class provision; flat/lci compatibility includes special fibers with ordinary Chow groups. Proposition 2.4.3 extends intersections to integrable adelic metrics via model domination and sup-norm continuity. The archimedean argument decomposes a smooth curvature representative into strongly positive forms; a uniform mass bound, not merely pointwise positivity, is necessary for the constant K. The finite-place argument uses numerical nef dual classes and their pullback/intersection with nef divisors, importing FL17 Lemma 3.7. This import is not recursively checked here.

Definition 2.4.4 is restricted to a smooth proper variety over Q and inverse limits of proper flat integral models under proper pushforward. Positivity is tested against one effective vertical divisor and further relatively nef factors at finite places. Integrability is a difference of positive compatible b-cycles, rather than arbitrary inverse-limit cycles. Proposition 2.4.5's extension relies on exactly that positivity/control; do not broaden it to all arithmetic b-cycles, all singular generic fibers or undefined arbitrary bivariant pushforwards.

No book change, independent verifier verdict or main-theorem clearance.

---

# Hultberg arXiv v1 — actual source reading 08

Physical pages 15–16 were read completely in the selected text and matching image. No other pages credited.

Remark 2.4.6 passes operational classes to compatible b-cycles and permits computing bundle intersections on models flat over base models. Its final wording mentions arbitrary b-cycles, while the preceding continuity theorem explicitly requires integrable b-cycles; preserve that requirement unless a separate extension argument is supplied. No general pullback of b-cycles is asserted. Example 2.4.7 obtains finite-place positive b-cycles from closures of a fixed generic cycle and a Green current, using vertical effectiveness and relative nefness.

All torsors in section 3 are Zariski torsors for split tori. A torus bundle is encoded as a symmetric monoidal functor from the character lattice category to the category of line bundles, including coherent tensor isomorphisms and morphisms, not merely a map to abstract Picard classes. Metrized/adelic versions preserve these identifications and norms. Flat means both the bundle and its dual are semipositive; because a lattice contains m and -m, semipositivity of every image automatically implies flatness. Algebraic metrics may come from rational model line bundles, while model metrics here use actual line bundles.

Morphisms allow a torus homomorphism with contravariant character map alpha:M'→M and a monoidal natural transformation. Proposition 3.1.5's sections must be torsor sections/trivializations, hence nowhere vanishing and tensor-compatible; arbitrary vanishing vector-bundle sections would not give equivariant torsor maps. These distinctions are relevant to the semiabelian extension and period-norm constructions.

No book integration, independent verifier receipt or main-theorem clearance.

---

# Hultberg arXiv v1 — actual source reading 09

Physical pages 17–18 were read completely in selected text and the matching image. No other pages credited.

Metrized torsor morphisms are explicitly norm-one. Tensor-power maps and base pullbacks include their coherent identifications. The Weil–Barsotti discussion requires image in Pic^0 and a rigidification at the origin to recover the group law; an arbitrary torus torsor over an abelian base is not a semiabelian variety.

Definition 3.1.9 uses f*T ≅ T^r with r>1 for dynamical metrics. The assertion that its metrized isomorphism class does not depend on the chosen isomorphism needs an allowed coefficient/base-extension convention: rescaling an isomorphism changes the canonical metric by a (r-1)-st root of that scale, which need not be realized by a ground-field isomorphism. Fixed rigidifications or extension/coefficient changes can remove this issue, but are not implicit in an actual norm-one isomorphism over the ground field. No formal counterclaim is promoted here.

Toric bundles are Zariski-locally products with a fixed fan and arise by contracted products. Ordinary noncanonical DVR toric models need a broader relative construction. Orbit closures use the quotient torus with character lattice M intersect sigma-perpendicular; this supports keeping active quotient characters separate from arbitrary ambient characters.

Proposition 3.2.5's fan criterion classifies nondegenerate equivariant maps extending torsor maps. Its no-map clause must stay in that nondegenerate context, since boundary-constant maps can be equivariant. The printed proof self-cites Proposition 3.2.5; the preceding torsor classification is Proposition 3.1.5. This is a source locator defect rather than proof clearance or a claim that the standard fan-extension theorem fails.

No book integration, independent verifier receipt or main-theorem clearance.

---

# Hultberg arXiv v1 — actual source reading 10

Physical pages 19–20 were read completely in selected text and matching image. No other pages credited.

Example 3.2.6 confirms that general degenerate equivariant maps need not factor through a single fixed orbit closure, because orbit type can vary with the base point. The paper then deliberately defines toric-bundle morphisms as the narrower class that does factor as a nondegenerate map followed by an orbit embedding. Preserve that restriction in functoriality. Multiplication [n] on a semiabelian variety extends to fixed-fan compactifications via multiplication on cocharacters and [n] on the abelian base, with the rigidification retained. This does not identify the toric eigenweight n with the abelian polarization eigenweight n squared.

Section 3.3 uses T-linearized sheaves and their descent to the contracted product. A genuine linearization includes the cocycle/unit compatibility in addition to the displayed isomorphism. Proposition 3.3.2 constructs the descent functor locally with tensor-compatible trivializing sections and glues via that linearization. Equivariantly different divisor representatives that are ordinarily linearly equivalent can descend to inequivalent base twists; this is essential for c(m).

The metric descent is to use the unit-norm part of the torsor, with linearization isometric over the unit torus; naive quotients by all torus points would change metrics. Adelic vector bundles must also come from a model over a dense open of the global base. Canonical outside finitely many places and coherent metric descent remain necessary hypotheses.

No book integration, independent verifier receipt or main-theorem clearance.

---

# Hultberg arXiv v1 — actual source reading 11

Physical pages 21–22 were read completely in selected text and matching image. No other pages credited.

Proposition 3.3.4 constructs metrized descent through a local algebraic trivialization corrected by its tropical norm, since norm-one local trivializations generally do not exist. Unit-torus isometry gives the required factorization of metric distortion. Proposition 3.3.5 globalizes using models of both the torsor and vector bundle on one dense open. This keeps period/norm information rather than discarding it through arbitrary trivializations.

Lemma 3.3.6 requires a semipositive toric fiber metric and semipositive base twists L+T(m) for every rational point of the Newton polytope. The proof uses sup-norm/maximum-monomial norm comparison, then quotient metrics and uniform approximation on a semiample line bundle. The error is bounded by log(number of lattice points)/l, tending to zero. Some displayed indexing literally uses (1/l)Delta intersect M where sections of lD should use lDelta intersect M, or scaled points Delta intersect (1/l)M; keep the scaling straight when checking this proof. The needed approximation imports are CM18 and Moriwaki and are not recursively cleared here.

Corollary 3.3.7 distinguishes integrability preservation for an integrable torsor from semipositivity preservation for a flat torsor. The latter uses simultaneous positivity of all character twists, not arbitrary torsors or a single positive basis. This distinction will matter for Theorem A and the abelian Pic^0 application.

No book change, independent verifier receipt or main-theorem clearance.

---

# Hultberg arXiv v1 — actual source reading 12

Physical pages 23–24 were read completely in selected text and matching image. No other pages credited.

Integrability preservation is proved using one common positive base twist for the finitely many vertices of the Newton polytope and convexity, then semipositivity of the descended twist. Dynamical fiber metrics agree with descent of the fixed canonical torsor metric. This concerns the fiber divisor's r-eigenweight, not the abelian ample divisor's r-squared eigenweight.

Lemma 3.4.1 obtains pushforward/eigenspace decompositions by flat base change and gluing, with character twists T(m). Proposition 3.4.2 compares fiberwise supremum norms to descended section norms; a normed trivialization at an analytic fiber may require extending its residue field, rather than asserting a global norm-one trivialization. Lemma 3.4.3 uses orthogonality and the corrected tensor-homogeneous roof definition.

Section 3.5 assumes an integrable smooth projective toric bundle over a smooth projective base and a compatible smooth projective adelic fan. Proposition 3.5.1 states vanishing of arithmetic products for rays that span no cone, with model torsor metrics at finite places and smooth torsor metrics at infinity. Finite-place proof uses regular ambient toric models and empty intersections. The archimedean proof uses piecewise linear Green functions and support/flatness properties. A mere pointwise product of continuous Green functions equal to zero does not by itself imply vanishing of a curvature-product current; the shared-fan support geometry and an admissible approximation are necessary. The continuation of that proof is on the next page and not yet credited here.

No book change, independent verifier receipt or main-theorem clearance.

---

# Hultberg arXiv v1 — actual source reading 13

Physical pages 25–26 were read completely in selected text and matching image. No other pages credited.

Proposition 3.5.1's continuation identifies the archimedean intersection with its current integral. Rational model metrics are handled via torsor tensor powers. Proposition 3.5.2 then approximates each basis character metric as a difference of semipositive algebraic limits and extends coherently to the lattice. A common positive base twist controls all factors; a piecewise linear Green function's Lipschitz constant bounds metric changes by the tropical translation norm. This supplies genuine uniform convergence, rather than weak convergence alone. Its imported current/support and intersection-continuity inputs remain to be checked.

Section 3.6 explicitly takes Zariski closures of height-sublevel sets. Lemma 3.6.1 proves invariance of the closure under the full torus by first using torsion translations, whose tropicalizations vanish at all places, then their Zariski density. It does not say individual point heights are invariant under arbitrary torus translations.

The claim that Noetherianity forces an increasing height filtration of closed sets to have only finitely many stages is not justified: Noetherianity gives the descending chain condition on closed sets, not the ascending condition. For toric fibers there are finitely many orbit types, but that is a different input and does not settle arbitrary bases.

Fiber roof functions are theta(m)+h_T(m)(b), with weighted global sums and coherent trivialization norms. h_Delta(b) is their maximum, identifying the infimum of heights in the dense fiber torus in the usual toric setting. Exact sublevels at a minimum require attainment; a maximum roof value does not by itself produce a point of exactly that height. Keep epsilon-approximation and endpoint attainment separate in the forthcoming filtration/minimum argument, particularly in view of the separately unverified BGPS converse candidate.

No book change, independent verifier receipt or main-theorem clearance.

---

# Hultberg arXiv v1 — actual source reading 14

Physical pages 27–28 were read completely in selected text and matching image. No other pages credited.

The geometric adapted flag first cuts toric divisors down to a copy of the base, then extends by a base flag. Translating the fiber polytope changes the base twist L as well. Theorem 4.0.1 describes the body as a closure of (m,base-body) fibers; actual fiber equality is asserted where L+T(m) is geometrically big. It uses eigensection surjectivity and continuity/convexity inside the big cone, not arbitrary nonbig fiber equalities.

Theorem 4.1.1 similarly describes the concave transform as theta(m)+G_(L+T(m))(x) on geometrically big fibers, relying on the consistent signed/tensor-normalized roof and orthogonality. Its proof does not independently repair the earlier definition-sign issues. Remark 4.1.2 is a conditional research direction toward Ballaÿ–Sombra approximation criteria, not a general equidistribution theorem for every toric bundle.

Theorem A takes at least one geometrically big base twist and semipositive toric fiber metric; its absolute-minimum clause further needs every base twist semipositive. Essential minimum is a supremum over the closed polytope; the absolute expression uses its interior. The argument that a big base twist makes the whole bundle divisor big also needs a full-dimensional fiber polytope in the fiber character space, or an appropriate effective quotient dimension. The printed general setup does not explicitly supply that restriction here. An ordinary interior of a lower-dimensional polytope is empty. Retain this boundary diagnostic pending the next-page remark.

The essential proof restricts to the big-twist locus then uses concavity to approximate boundary values. Do not read it as equality of every nonbig Okounkov fiber or remove the big-locus qualification.

No book change, independent verifier receipt or main-theorem clearance.

---

# Hultberg arXiv v1 — actual source reading 15

Physical pages 29–30 were read completely in selected text and matching image. No other pages credited.

Theorem A's absolute-minimum proof uses nefness of every underlying base twist plus one big twist: convex combinations show interior twists are big. It still relies on the earlier general absolute-minimum/concave-transform assertion and upper-semicontinuity passage; these imports/signs are not independently cleared by this argument. No explicit lower-dimensional-polytope repair appears on these pages.

Theorem B is restated with relative toric dimension t, smooth generic fiber, smooth projective base of dimension g, integrable adelic torsor, operational gamma of codimension g+1-i on a flat projective base model, and a height-one trivial class [infinity]. Its exact coefficient is i! on the bundle intersection and (t+i)! on the integral of (c(m)+theta(m)[infinity])^i gamma. Keep lattice-normalized Lebesgue measure, weights, and the arithmetic base dimension g+1. A height-one trivial adelic class must still be model-canonical outside finitely many places, not a nonzero metric shift at infinitely many places.

Remark 5.0.1 permits extra integrable Chern factors by approximation, homological classes on a model when the torsor is modeled there, and suitably positive/integrable b-cycles in the general setting. It does not authorize all inverse-limit cycles without continuity control.

The proof overview compares homogeneous polynomial derivatives, inducting on i plus derivative multiplicity. The i=0 case is geometric BKK times the arithmetic degree of gamma, treating closed-point and archimedean-measure components separately via projection/Fubini. Subsequent derivative comparisons must preserve this normalization; the overview alone is not a completed proof.

No book change, independent verifier receipt or main-theorem clearance.

---

# Hultberg arXiv v1 — actual source reading 16

Physical pages 31–32 were read completely in selected text and matching image. No other pages credited.

Section 5.2 uses the Pukhlikov–Khovanskii convex-chain algebra, finite additive valuations, translation differences, degree-zero ideal and polynomial measures. Its convolution is the convex-chain/Euler-characteristic convolution from that framework, not ordinary Lebesgue convolution of indicator functions. The imported ideal relation gives polynomial degree at most ambient dimension plus translation degree; continuity on finite-dimensional subspaces excludes discontinuous polynomial pathologies.

Theorem 5.2.8 extends integrals of homogeneous polynomial functions to virtual polytopes with degree t+k. The arithmetic construction has finitely many active place coordinates and pushes their roofs to one global coordinate. This pushforward must use the local weights n_v when the global roof is sum n_v theta_v; a plain unweighted addition is only the equal-weight convention.

Theorem 5.2.9 reduces integral f(m,theta(m)) to integral f(m,0) over the underlying polytope plus integral partial_t f over the nonnegative roof hypograph. The latter has ambient dimension t+1 and polynomial degree k-1, yielding t+k. This elementary degree accounting is correct in the polyhedral/virtual framework, with a constant f handled separately when k=0. Extending from actual polytopes to arbitrary continuous concave roofs still requires the completion/continuity convention flagged earlier; no such source import has been independently checked here.

No book change, independent verifier receipt or main-theorem clearance.

---

# Hultberg arXiv v1 — actual source reading 17

Physical pages 33–34 were read completely in selected text and matching image. No other pages credited.

Corollary 5.2.10 gives degree t+i for the arithmetic polynomial. Section 5.3 uses directions dual to primitive fan rays with support value one, a simplicial compatible fan and place-wise interior points. Derivative comparisons depend on the distinction between integrating a polynomial over a hypograph and integrating its boundary value over the base.

Proposition 5.3.2 literally gives a (t+1)-st derivative of hat I_f as f evaluated at a roof vertex. For t=0, hat I_f(h)=f(h), whose derivative is f'(h), not f(h). The statement appears to confuse the hypograph-volume integral with the boundary-value functional. Corollary 5.3.3 does differentiate f in the roof variable, consistent with the preceding fundamental-theorem-of-calculus decomposition. Preserve this literal symbol/derivative diagnostic, not a claim that the later comparison is thereby false.

Lemma 5.3.1 prints multiplication by the determinant of primitive ray generators. For support-value coordinates, a nonunimodular cone usually gives the inverse determinant Jacobian; an exact rank-two cone calibration is needed before importing the simplicial generalization. The earlier smooth-fan context has determinant one and would not see this discrepancy. Place weights must also persist in derivatives of a weighted global roof.

Corollary 5.3.3 uses [infinity]^2=0 and gives i c(A)^(i-1)[infinity] gamma times the asserted determinant factor. Lemma 5.4.1 proposes the matching arithmetic derivative times (t+i)!/i!. Noncone derivatives vanish using Proposition 3.5.2; the expansion keeps the full multinomial coefficients. Its proof continues on the next page.

No book change, independent verifier receipt or main-theorem clearance.

---

# Hultberg arXiv v1 — actual source reading 18

Physical pages 35–36 were read completely in selected text and matching image. No other pages credited. This finishes the printed proof of Theorem B, but not recursive clearance of its imports.

The squarefree arithmetic derivative computation on page 35 literally has (t+i)!/i! times rho(Delta)^i and t+1 ray-divisor factors. Differentiating a degree t+i power t+1 times instead gives (t+i)!/(i-1)! times rho(Delta)^(i-1). The printed product has one excess codimension. The earlier Lemma 5.4.1's announced factor i(t+i)!/i! is consistent with the corrected falling factorial, suggesting a repair of this intermediate display, not a verified failure of the intended theorem. The vertex reduction and projection then require the corrected exponent and correct determinant/local-weight conventions.

The repeated-ray derivative step expresses one support derivative as a translation Lie derivative plus directions outside the current cone, reducing multiplicity. The Lie derivative computations give L_v I_gamma = i I_(c(v)gamma) and L_v F_gamma = (t+i) F_(c(v)gamma), with the extended c(v) including the roof-height coordinate. Induction on i produces the intended factorial relation. Some displayed arguments suppress theta and mislabel translation variables; do not reproduce them verbatim.

Polynomial homogeneity and all order-(t+1) derivative comparisons determine the degree-(t+i) difference for i>0; i=0 was separately treated by projection. Compatible fans/model approximation and continuous integrable intersections remain load-bearing. Literal display errors have been separated from any assertion about the true arithmetic BKK identity.

No book change, independent verifier receipt or main-theorem clearance.

---

# Hultberg arXiv v1 — actual source reading 19

Physical pages 37–38 were read completely in selected text and matching image. No other pages credited.

Section 6 now pins all key conventions: split torus, an ample fiber divisor with full-dimensional Newton polytope, ample symmetric base M with canonical metrics, and Néron–Tate height transferred to A-dual through M's polarization. It is not an intersection-degree-weighted replacement height. The total dimension is d=t+g. Lemma 6.0.1's intended body is Delta times the base Okounkov body, with constant base-fiber transform -hhat(c(m)). Translation by torsion makes point-height infimum and essential minimum equal in each twisted abelian base; it need not give exact attainment of every torus-fiber minimum.

The printed arithmetic degree quoted from Chambert–Loir on page 37 is -2 deg(M^g)/g times h_M(q). Dividing this by (g+1)deg(M^g) gives -2/[g(g+1)] h_M(q), not the printed -h_M(q) for general g. This is an exact internal coefficient mismatch; check the controlling original theorem before using either formula. At g=0 the displayed quotient is undefined, so the pure-torus case needs separate treatment.

Theorem C prints unnormalized total height = -(d+1)! integral_Delta hhat(c(m)) dm. Its proof first integrates over the product body, which requires multiplication by vol_R^g(Delta_A(M))=(M^g)/g!. Subsequent lines insert and cancel degree/volume factors without justification, dropping that base volume. The adopted height convention on page 7 and transferred Néron–Tate convention here do not absorb it. A scaling calibration of M versus the polarization-transferred height is now needed. This is a source/math audit diagnosis, not a promoted new result or an independently verified main-theorem counterexample.

Theorem D uses ascending minima: first g+1 equal the absolute minimum, then negative max over faces of dimension t+g+1-i of the minimum hhat on each face. The essential case is the full face; the absolute case is vertices. Restrictions to orbit closures require the appropriate base twist when a face is translated into its quotient character space. The proof continues next page.

No book change, independent verifier receipt or main-theorem clearance.

---

# Hultberg arXiv v1 — actual source reading 20

Physical pages 39–40 were read completely in selected text and matching image. No other pages credited. Theorem D and the source's mathematical body are now completely read; two reference pages remain.

The face restriction finishes by translating a face F by m_sigma and retaining the base twist c(m_sigma). Thus it does not discard the character-induced base contribution. For the anticanonical projective-space compactification, Delta=(t+1)standard-simplex minus the sum of basis vectors has barycentric vertex sum zero. Lemma 6.0.2 recovers an absolute-minimum vertex formula and points to Chambert–Loir Lemma 4.5, whose controlling primary text still needs inspection.

Lemma 6.0.3 prints height = -(d+1)deg(M)/[(t+1)(t+2)] times the sum of vertex Néron–Tate heights. M has continued to denote the base ample bundle, whereas converting the simplex integral to an unnormalized total height would involve the degree of the total bundle, including toric volume and the binomial/base dimension factors. In the exact formal calibration t=g=1, base degree one, Delta=[-1,1], and hhat(c(m))=H m^2, its displayed formula gives -H, while its own Theorem C gives -6*(2H/3)=-4H. This already tests an internal mismatch without invoking an uninspected external intersection theorem. Preserve the formulas and check them in an executable calibration; do not promote a new theorem from this diagnosis.

The homogeneous-polynomial simplex integration identity keeps volume divided by binomial(t+r,r), and for r=2 with vertex sum zero it reduces to volume/[(t+1)(t+2)] times the sum of diagonal values. That identity supplies a direct coefficient check; an external Lasserre–Avrachenkov reference is cited.

The reference list pins Ballaÿ 2021, Ballaÿ's March 2022 arithmetic Okounkov preprint, 2024 Ballaÿ–Sombra preprint, Boucksom–Chen 2011, arithmetic toric positivity 2016, Astérisque 360, successive minima 2015, and Chambert–Loir Ann. ENS 33(2000),789–821, DOI 10.1016/S0012-9593(00)01053-3. These bibliographic entries are reading anchors, not recursive proof clearance.

No book change, independent verifier receipt or main-theorem clearance.

---

# Hultberg arXiv v1 — actual source reading 21

Physical pages 41–42 were read completely in selected text and matching image. All 42 physical pages of this exact arXiv v1 are now actually read in 21 matched complete-text/image displays. Prepared but undisplayed material receives no additional credit, and this completion does not recursively clear cited sources.

The remaining bibliography pins Chambert–Loir–Tschinkel arithmetic torsors (2001), Chen–Moriwaki extension (2018), Cox–Little–Schenck, Demailly, Fulger–Lehmann dual-cycle cones (2017), Fulton toric varieties and intersection theory, Gillet–Soulé arithmetic Riemann–Roch (1992), Hofscheier–Khovanskii–Monin arXiv 2006.12043, Knop–Lange (1984), and Lasserre–Avrachenkov (2001). Subsequent entries anchor Lazarsfeld–Mustata 2009, Moriwaki adelic/semipositive works, Pukhlikov–Khovanskii 1992, Qu–Yin arXiv 2208.13230, Soulé's arithmetic intersection chapter, Witt Nyström's metric transform and Zhang's two foundational arithmetic positivity/small-point papers. Edition/version-sensitive numbers must be checked in those controlling sources before integration.

The primary next dependency is Chambert–Loir's published 2000 paper, for the actual arithmetic degree normalization in Theorem 2.5 and the compactification height formula. Exact internal calibrations of Hultberg's tensor scaling, derivative factorial and product-body volume will be preserved separately. The intended Theorems A–D remain unverified for book import; the standard special-case facts and classical identities are distinguished from literal printed auxiliary defects.

No book change, new theorem, independent verifier receipt or canonical problem-status change is claimed.
