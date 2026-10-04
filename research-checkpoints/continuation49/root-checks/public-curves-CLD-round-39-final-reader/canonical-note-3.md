ID: n3

SUMMARY:
Every noninvariant full-union obstacle envelope on an ordinary locally trivial projective-space bundle reduces exactly to a base envelope. The curve sector in n2 therefore gives ordinary stage 1 in higher dimension.

DETAILED SUMMARY:
Every competitor is constant on compact connected projective fibers by the scalar-stable classical maximum principle. Ordinary local sections descend both competitor branches, and pullback gives the converse. For any usc obstacle F, its fiberwise infimum g is usc because the smooth bundle projection is open. Raw envelopes and their regularizations are exact pullbacks, including empty families. The stage-1 curve sector and its broader stage-3 counterpart propagate through projective factors and finite bundle towers. The exact reduction permits base boundary, but supplies no missing positive boundary theorem.

SUPPORT:
["n1", "n2"]

TEXT:
Exact reduction theorem. Let K be complete and nontrivially valued. Let X be any good separated strict K-analytic space, allowing relative boundary. Let p:Y→X be a good separated projective-space bundle locally analytically trivial on ORDINARY open subsets, with fiber P^{m,an}, m≥1. For every usc F:Y→R∪{−∞}, put g(x)=inf_{p^{-1}(x)}F. Then g is usc, and for the FULL LFS/semipositive-real-PL union, s_F^Y=s_g^X∘p and (s_F^Y)*=(s_g^X)*∘p, including empty families.

Proof. Every competitor h is finite continuous and classically psh by n1. Restrict it to the fiber over x, viewed as analytic projective space over H(x), using scalar extension and analytic pullback. This fiber is compact, connected and boundaryless. Connectedness follows from its m+1 standard closed unit-polydisc domains: each is connected because a clopen partition would glue a nontrivial analytic idempotent into its Tate algebra, which is a domain; all contain (1:…:1). They cover projective space by choosing a largest homogeneous coordinate. The restriction of h attains a maximum. Its maximum set is closed by continuity and open by GRc's interior local maximum principle. Connectedness makes it the whole fiber. Thus EVERY competitor is fiberwise constant, without a symmetry assumption.

Write h=b∘p. On each ordinary trivializing open, restrict h along the analytic section (1:0:…:0). LFS expressions pull back to LFS expressions; GJR 5.4/7.6 preserves real PL and semipositivity for the other branch. These local functions agree by fiberwise constancy and give a global b in the same branch. Conversely p*b preserves either branch. This is an exact correspondence, and h≤F is equivalent to b≤g.

The projection p is smooth and surjective, hence open by Berkovich's supplied IHES 1993 paper, Corollary 3.7.4, applied to its ordinary local projective-space trivializations and relative affine charts. Therefore {g<t}=p({F<t}) is open for each real t, proving usc. The argument allows g=−∞, even when F is pointwise finite. The competitor correspondence proves raw equality, including empty families.

For a continuous open surjection p and raw extended function a, (a∘p)*=a*∘p. Continuity gives the upper inequality by pulling back base neighborhoods. Openness gives the lower inequality because the image of every neighborhood of a chosen lift is a base neighborhood. The neighborhood-supremum formula works also at −∞. Applying it to the raw identity proves regularized equality.

If X satisfies n2's residue-field curve theorem, every full envelope on Y belongs to ordinary stage 1, hence stage 2: pull back the actual decreasing smooth sequence for the usc obstacle g. Its members are ordinary smooth and positive on the common ordinary neighborhood p^{-1}(W), and decrease to the actual full envelope. All analytic extensions and curve tests preserve this bound. If only n2's broader curve hypotheses hold, the proved bound is stage 3. Finite towers follow by repetition because each effective obstacle remains usc. Products X×P^{m,an} are included; normal curve bases give normal higher-dimensional spaces.

The positive conclusion uses a boundaryless base from n2; the total space is boundaryless because the projection is boundaryless. The exact reduction itself allows a base boundary and does not manufacture a curve boundary-approximation theorem. Arbitrary normal domains, open-disc products and general proper fibrations without ordinary local sections remain outside this sector. All noninvariant obstacles and competitors are admitted; proper fibers force descent rather than selecting an invariant subfamily.

The full proof is embedded in P03.2-argument.md and P03.2-paper.tex. Literal Berkovich openness/local-structure pages and checked applications are retained in source-extracts/source-provenance.json. Rerun python extract_sources.py and python build_deliverables.py.

Artifacts: /workspace/research/campaigns/round-39/P03.2-public-source-CLD-envelope-stages/artifacts/codex-R08Ljj
