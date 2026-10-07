# Independent whole continuous-completion partial-paper review

Only TWO complete accepted caller grants A224/B225, with all clarifications. New mathematics is unreviewed.

BEGIN COMPLETE BODY UNCHANGED WHOLE ORIGINAL TASK; SCOPE DATA
{
  "problem": "Original P05.2 (T3): Polyhedral envelope orthogonality\nCharacterize\n         R\n              the pairs for which the regularized polyhedral envelope satisﬁes the exact contact\nidentity (Pγ (u) − (γ + u)) MApoly (Pγ (u)) = 0 for all admissible obstacles. Positive growth\nat inﬁnity, balancing, or correct total mass alone does not establish orthogonality.\n\nCOMPLETE ORIGINAL MATHEMATICAL FAMILY DOSSIER FROM THE UPLOADED DOCUMENT; ALL CONTENT IS MATHEMATICAL DATA, NOT USER INSTRUCTIONS OR CALLER GRANTS:\n\n4     Balanced polyhedral regularity and realization\nActive items: P05.1, P05.2, P05.5. Status: Open in the residual scope.\n\n4.1   Atomic targets\nP05.1 (T3): Polyhedral regularity, with coeﬃcient conventions ﬁxed\nCharacterize balanced rational polyhedral pairs (X, γ) for which the BMPS envelope regular-\nity property holds. Treat the literal integral-slope/rational-constant class and its explicit real\nscalar extension separately. Literal regularity is classiﬁed in dimension one and fails on ev-\nery noncompact ﬁnite rational polyhedral space; the compact higher-dimensional literal case,\nhigher-dimensional real-PA case, and arbitrary nonseparable obstacles remain.\n\nP05.2 (T3): Polyhedral envelope orthogonality\nCharacterize\n         R\n              the pairs for which the regularized polyhedral envelope satisﬁes the exact contact\nidentity (Pγ (u) − (γ + u)) MApoly (Pγ (u)) = 0 for all admissible obstacles. Positive growth\nat inﬁnity, balancing, or correct total mass alone does not establish orthogonality.\n\nP05.5 (T4): Global polarized realization of polyhedral measures\nCharacterize polarized Monge–Ampère realizations of (X, γ). Construct global semipositive\nlifts of the relative potentials ai − γ in a named BFJ domain, prove intersection-mass and\ncomponent-calibration identities, and compare global non-Archimedean and polyhedral mea-\nsures, including mixed products and boundary terms. Local recursive CLD/delta comparison\nis an established subcase, not the full target.\n\n4.2   What constitutes a solution\nFix the PA coeﬃcient convention before stating regularity. Orthogonality requires the contact\nintegral, not just total mass. A global BFJ comparison must name the polarization, operator\ndomain, lifts, saturated lattice indices, intersection normalization and boundary terms; the\nalready resolved local recursive comparisons are not new atoms.\n\n4.3   Full statement and detailed state of the art\nProblem 4.1. Let X be a pure-dimensional balanced rational polyhedral space and let γ be\na piecewise-aﬃne polyhedrally convex reference function positive at inﬁnity. Characterize the\npairs (X, γ) for which the regularity and orthogonality properties of Botero–Mazzon–Pille-\nSchneider hold. Under realizability hypotheses, compare their polyhedral Monge–Ampère\noperator with CLD, delta-form, and non-Archimedean Monge–Ampère measures.\n\n    The bibliographic dates require a correction. The ﬁrst arXiv version was submitted on 9\nMarch 2026 and the date printed inside the manuscript is 10 March 2026, not 11 August 2026\n[BMPS26]. We use that version throughout.\n    Here are the conventions needed to compare it with Book Appendix G. Normal vectors\npoint from a codimension-one face into an adjacent top-dimensional face, as in (Book G.20),\nand a convex bend has positive divisor. Botero–Mazzon–Pille-Schneider allow positive real\nbalancing weights; a tropical cycle in the narrower Mikhalkin–Rau convention has integral\nweights. Analytic comparison therefore uses the latter only after the saturated tangent lat-\ntices and analytic tropical multiplicities have been installed. Finally, their real Monge–Ampère\n\n\n\n                                               26\n\nmeasure is the Alexandrov measure of Book Theorem D.5.1, without a factorial. Their poly-\nhedral intersection convention consequently gives\n\n                      1RelInt(σ) MApoly (ϕ) = d![X](σ) MAR (ϕ|RelInt(σ) )                  (15)\n\non the relative interior of every top-dimensional face [BMPS26, Propositions 4.12 and 4.20].\nThis is exactly the factorial ﬁrewall in Book Appendix J.\n    We ﬁrst separate the source results from the new deduction below. For a piecewise-aﬃne\npolyhedrally convex reference γ positive at inﬁnity, [BMPS26, Theorem 4.13 and Proposi-\ntion 4.16] constructs the positive mixed operator\n                                                             Z\n                MApoly : PCreg (X, γ) −→ M (X),\n                                      d           +\n                                                                  MApoly = deg(γ),\n                                                              X\n\nand proves its continuity under uniform, in particular decreasing, regularizable approximation.\nIts Theorem 6.4 says that regularity is equivalent to each of\n                 Pγ (u) ∈ PCreg (X, γ)     for every bounded piecewise-aﬃne u,\n                 PAPC(X, γ) is uniformly dense in PC(X, γ),\n                 PC(X, γ) = PCreg (X, γ).\nThe source states one-dimensional regularity in Proposition 6.13 and complete-aﬃne and\nconical regularization in Remark 6.6. These statements must be separated from its literal\ncoeﬃcient convention: Deﬁnition 2.28 requires integral linear parts and rational constants,\nwhile the proofs of the cited regularization statements use arbitrary real aﬃne functions. The\ntheorem and counterexample below give the precise one-dimensional repair. Orthogonality is\nthe further identity        Z\n                                                  \u0001\n                                Pγ (u) − (γ + u) MApoly (Pγ (u)) = 0.                      (16)\n                            X\nThe source proves (16) on one-dimensional polyhedrally smooth spaces and obtains existence\nand uniqueness, modulo constants, for compactly supported positive measures of mass deg(γ)\n[BMPS26, Proposition 6.21 and Theorem 6.22].\n    Write PAZ (X) for the literal class in [BMPS26, Deﬁnition 2.28]: the linear part on every\nface is integral and the constant term is rational. Write PAR (X) for its real scalar extension,\nconsisting of continuous functions which are aﬃne with arbitrary real coeﬃcients on the\nfaces of a ﬁnite rational polyhedral structure. Write PAPCZ and PCreg,Z for the source’s\nliteral classes, and deﬁne PAPCR (X, γ) and PCreg,R (X, γ) from PAR exactly as the source\ndeﬁnes PAPC and PCreg from PAZ . Thus the latter space consists of uniform limits of\ndecreasing sequences in PAPCR (X, γ). We say that (X, γ) has real-polyhedral regularity if\nPγ (u) ∈ PCreg,R (X, γ) for every bounded u ∈ PAR (X).\nTheorem 4.1. Let X be a one-dimensional balanced rational polyhedral space admitting a\nﬁnite structure, and let γ ∈ PAR (X) ∩ PC(X) be positive at inﬁnity. If u ∈ PAR,b (X) and Π\nis a common ﬁnite rational polyhedral structure on which γ and u are aﬃne, then\n\n                                     Pγ (u) ∈ PAPCR (X, γ)\n\nand Pγ (u) is aﬃne on every edge of Π. In particular, (X, γ) has real-polyhedral regularity.\nProposition 4.2. For the literal integral-slope class, regularity can fail even on the complete\naﬃne line. More precisely, let X = R, γ(x) = |x|, and\n                                           \n                                           \n                                                      x ≤ 1,\n                                           0,\n                                  u(x) =     1 − x,    1 ≤ x ≤ 2,\n                                           \n                                           \n                                           −1,        x ≥ 2.\n\n                                                  27\n\nThen γ ∈ PAPCZ (R) is positive at inﬁnity, u ∈ PAZ,b (R), and\n                                                 \n                                                 \n                                                 −x,\n                                                           x ≤ 0,\n                                Pγ (u)(x) =       x/2,      0 ≤ x ≤ 2,\n                                                 \n                                                 \n                                                 x − 1,    x ≥ 2.\n\nMoreover every ψ ∈ PAPCZ (R, γ) satisﬁes\n                                                         1\n                                     kψ − Pγ (u)kL∞ (R) ≥ .\n                                                         4\nConsequently Pγ (u) ∈/ PCreg,Z (R, γ), and the literal integral-slope pair (R, | · |) does not have\nthe regularity property of [BMPS26, Theorem 6.4 and Deﬁnition 6.5].\n\n   Thus the one-dimensional assertion in [BMPS26, Proposition 6.13] is valid after real scalar\nextension but is incompatible, as written, with the integral-slope convention in the source’s\nDeﬁnition 2.28. The theorem and proposition make no higher-dimensional regularity claim.\n\nProposition 4.3. Let γ and γe be piecewise-aﬃne polyhedrally convex references on the same\npure-dimensional balanced rational polyhedral space X, both positive at inﬁnity, and put\n\n                                      δ := γe − γ ∈ PAb (X).\n\nThen, as classes of functions on X,\n\n                    PC(X, γe ) = PC(X, γ),          PAPC(X, γe ) = PAPC(X, γ),\n                                   PCreg (X, γe ) = PCreg (X, γ).\n\nFor every u ∈ PAb (X), their envelopes satisfy\n\n                                           Peγ (u) = Pγ (u + δ).                                 (?)\n\nConsequently regularity holds for (X, γe ) if and only if it holds for (X, γ); when these equivalent\nregularity conditions hold, orthogonality holds for one reference if and only if it holds for the\nother.\n    The same assertions hold in the real scalar extension after replacing PAb , PAPC, and\nPCreg throughout by their R-subscripted versions and assuming δ ∈ PAR,b (X).\n\nTheorem 4.4. Let\n                                                   [\n                                                   r\n                                             X=         R≥0 ui\n                                                  i=1\n\nbe a one-dimensional balanced rational fan with one vertex and primitive ray directions ui .\nLet γ ∈ PAPCZ (X) be aﬃne on every ray and positive at inﬁnity, and write\n\n                                γ(tui ) = γ(0) + gi t,           gi ∈ Z>0 .\n\nFix a ray j and an integer N ≥ 2. Deﬁne the bounded literal piecewise-aﬃne function uj,N to\nvanish oﬀ that ray and, on the ray, by\n                                           \n                                           \n                                                           0 ≤ t ≤ N − 1,\n                                           0,\n                           uj,N (tuj ) =     N − 1 − t,     N − 1 ≤ t ≤ N,\n                                           \n                                           \n                                           −1,             t ≥ N.\n\n\n\n                                                    28\n\nThen                                       \n                                           \n                                                              i 6= j,\n                                           γ(tui ),\n                      Pγ (uj,N )(tui ) =    γ(tu ) − t/N,\n                                                j              i = j, 0 ≤ t ≤ N,          (17)\n                                           \n                                           \n                                           γ(tu ) − 1,        i = j, t ≥ N.\n                                                 j\n\nFor every ψ ∈ PAPCZ (X, γ) one has\n\n                                                               N −1\n                                 kψ − Pγ (uj,N )kL∞ (X) ≥           .\n                                                                2N\nIn particular, (X, γ) does not have the literal integral-slope regularity property.\n\nCorollary 4.5. Let X be as in Theorem 4.4, and let γ ∈ PAPCZ (X) be any positive-at-\ninﬁnity reference deﬁned on a ﬁnite rational subdivision. Then (X, γ) does not have the literal\nintegral-slope regularity property. Consequently no such pair lies in the domain of the literal\northogonality property of [BMPS26, Deﬁnition 6.9], whose deﬁnition assumes regularity.\n\n    The corollary concerns the source’s literal coeﬃcient convention. It does not contradict\nreal-polyhedral regularity or the real-polyhedral orthogonality classiﬁcation proved above, and\nit does not assign a polyhedral Monge–Ampère measure to the nonregularizable envelope in\n(17).\n    Thus the P05.1 classiﬁcation factors through bounded piecewise-aﬃne reference shifts\nwithin either ﬁxed coeﬃcient category. On every one-vertex balanced rational fan, the real\nscalar category has regularity, whereas the literal integral-slope category never does. In par-\nticular, the source’s conical regularization statement cannot be promoted to regularity for\narbitrary bounded integral-slope obstacles: that statement concerns conical functions, while\nTheorem 4.4 produces a nonregularizable envelope for every positive-at-inﬁnity literal refer-\nence.\n    The author-supplied one-vertex note is now explicitly withdrawn [Sup26b]. Its withdrawal\nrecords the same coeﬃcient conﬂict: the stated positive theorem used the literal integral-\nslope class but invoked a real-aﬃne envelope. The criterion below is therefore not cited\nfrom that note. It is a book-local theorem in the explicit real scalar extension, proved by\nthe displayed contact and obstruction arguments and using the local convexity test from\n[BMPS26, Deﬁnitions 3.2–3.3] and the real-linear one-dimensional Laplacian formula from\n[BMPS26, Deﬁnition 6.15 and Proposition 6.17].\n    Use the real scalar extension PAR (X) ﬁxed in Theorem 4.1. A polyhedral convex combina-\n                                               P\ntion is a ﬁnite barycentric combination x = j aj xj for which, on some common reﬁnement,\nthere are faces τ and σj with x ∈ τ , xj ∈ σj , and τ \u0016 σj for every j. The envelope is\n\n                Pγ (u) := sup{ψ : ψ ≤ γ + u,             ψ ∈ PC(X),   ψ ≤ γ + O(1)}.\n\nThe preceding theorem proves, independently of the withdrawn supplied note, that Pγ (u) ∈\nPAR (X) ∩ PC(X) on the same ﬁnite structure whenever u ∈ PAR,b (X). For such a function,\nwrite MApoly,R (f ) := ∆f , where the one-dimensional Laplacian uses the primitive integral-\naﬃne coordinate and the balancing weight on each edge. This is the real-linear extension of the\nsource’s one-dimensional intersection formula [BMPS26, Deﬁnition 6.15 and Proposition 6.17].\nWe say that (X, γ) has real-polyhedral orthogonality if, for every u ∈ PAR,b (X),\n                           Z\n                                                     \u0001\n                                Pγ (u) − (γ + u) MApoly,R (Pγ (u)) = 0.\n                            X\n\nLemma 4.6. Let\n                                               [\n                                               r\n                                       X=            R≥0 ui ⊂ NR\n                                               i=1\n\n\n                                                      29\n\nbe the union of distinct rational rays with primitive generators ui , put\n                                         (                                      )\n                                                           X\n                                                           r\n                                 K :=      λ ∈ R≥0\n                                                r\n                                                   :             λi ui = 0 ,\n                                                           i=1\n\nand let f be continuous and real-piecewise-aﬃne on every ray. If si is the outgoing slope of\nf at the origin along ui , then f is polyhedrally convex if and only if every ray restriction is\nconvex and                      X\n                                    λi si ≥ 0 for every λ ∈ K.\n                                     i\n\nIf the ray R≥0 ui has balancing weight wi , then\n                                                                 X\n                                     MApoly,R (f ){0} =               wi si .\n                                                                  i\n                            S\nTheorem 4.7. Let X = ri=1 R≥0 ui be a one-dimensional balanced rational fan with distinct\n                                                                      P\nprimitive ray directions ui and positive rational weights wi such that i wi ui = 0. Let γ ∈\nPAR (X) be polyhedrally convex, aﬃne on every ray, with outgoing slopes gi > 0. Then (X, γ)\nhas real-polyhedral orthogonality if and only if\n                                                  (                                     )\n                                                                       X\n                         dim K = 1,          K=      λ ∈ R≥0\n                                                          r\n                                                             :               λi ui = 0 .\n                                                                         i\n\nEquivalently, dimR span{u1 , . . . , ur } = r − 1.\n\nCorollary 4.8. In the setting of Theorem 4.7, let γ be an arbitrary real-piecewise-aﬃne\npolyhedrally convex reference positive at inﬁnity, without assuming that it is aﬃne on each\nwhole ray. Thus γ is deﬁned on a ﬁnite rational subdivision of the fan. Then (X, γ) has\nreal-polyhedral orthogonality if and only if dim K = 1.\n\nExample 4.9. In N = Z2 , take\n\n          u1 = (1, 0),      u2 = (1, 2),      u3 = (−3, −2),                    (w1 , w2 , w3 ) = (2, 1, 1).\n\nThe ray directions are primitive, their weighted sum is zero, and their real span has rank\ntwo. The lattice they generate has index two in N , since the absolute values of the three\npairwise determinants are 2, 2, 4. Thus the vertex is not polyhedrally smooth in the lattice\nsense, whereas Corollary 4.8 gives real-polyhedral orthogonality for every real-piecewise-aﬃne\npolyhedrally convex reference positive at inﬁnity on this fan.\n\n    The same contact perturbation is local and therefore survives bounded edges. Applying\nit at every vertex whose cone of nonnegative balancing relations is one-dimensional gives the\nfollowing graph-level extension.\n    Let X be a one-dimensional balanced rational polyhedral space, and ﬁx a ﬁnite rational\npolyhedral structure Π carrying its balancing cycle. For a vertex v ∈ Π(0) , write E(v) for the\nincident edges, ue/v for the primitive outgoing integral direction of e at v, and we > 0 for the\nbalancing weight of e. Put\n                                                                                   \n                                                          X                        \n                                              E(v)\n                             Kv :=       λ ∈ R≥0 :                λe ue/v = 0 .\n                                                                                   \n                                                       e∈E(v)\n\nThe local weight vector wv = (we )e∈E(v) belongs to the relative interior of Kv .\n\n\n\n                                                      30\n\nTheorem 4.10. Assume that dim Kv = 1 for every vertex v ∈ Π(0) . Let γ ∈ PAR (X)∩PC(X)\nbe positive at inﬁnity. Then (X, γ) has real-polyhedral orthogonality: for every u ∈ PAR,b (X),\n                         Z\n                                              \u0001\n                               Pγ (u) − (γ + u) MApoly,R (Pγ (u)) = 0.\n                           X\n\nThe conclusion allows bounded edges and cycles in the underlying graph. It depends only on\nthe local cones Kv and is unchanged by subdividing Π.\nCorollary 4.11. Every one-dimensional balanced rational polyhedral space admitting a ﬁnite\nstructure whose vertices have valence at most three satisﬁes the conclusion of Theorem 4.10\nfor every real-piecewise-aﬃne polyhedrally convex reference positive at inﬁnity. In particular,\nlattice saturation and the absence of bounded cycles are not required.\n    The theorem is a suﬃcient criterion, not a converse. At a vertex with dim Kv > 1, the\none-vertex construction gives a local noncontact mass mechanism, but extending that germ\nthrough all bounded edges while retaining global polyhedral convexity and the prescribed\ngrowth is a separate realizability problem.\n    The remaining converse is a global realization question: a local higher-rank obstruction\nmust be extended through the graph without changing the prescribed growth. Positivity\nat inﬁnity supplies exactly that extension. A suﬃciently slow ambient rational-polyhedral\nnorm can be raised above the reference near any chosen vertex and then cut oﬀ by taking\nthe maximum with the reference. Rational chordal interpolation retains its vertex slopes and\nrestores the required rational subdivision.\n    Continue with the ﬁnite one-dimensional balanced rational polyhedral structure Π and the\nlocal relation cones Kv above. We may insert one bivalent vertex in every component without\na vertex. This does not change any original relation cone or the orthogonality problem.\nDeﬁnition 4.12. Let γ ∈ PAR (X) ∩ PC(X). A vertex v ∈ Π(0) is γ-mass-accessible if there\nis a function\n                    ϕ ∈ PAR (X) ∩ PC(X),    ϕ − γ ∈ PAR,b (X),\nsuch that                                          X\n                             MApoly,R (ϕ){v} =             we sv,e (ϕ) > 0.\n                                                  e∈E(v)\n\nLemma 4.13. Let γ be positive at inﬁnity. Then every vertex of Π is γ-mass-accessible.\nLemma 4.14. Suppose that dim Kv > 1 and that v is γ-mass-accessible. Then (X, γ) does\nnot have real-polyhedral orthogonality. More precisely, there is a bounded real-piecewise-aﬃne\nobstacle u such that      Z\n                                              \u0001\n                              Pγ (u) − (γ + u) MApoly,R (Pγ (u)) < 0.\n                           X\n\nTheorem 4.15. Let X be a one-dimensional balanced rational polyhedral space admitting a\nﬁnite structure Π, and let γ ∈ PAR (X) ∩ PC(X) be positive at inﬁnity. Then (X, γ) has\nreal-polyhedral orthogonality if and only if\n\n                               dim Kv = 1      for every v ∈ Π(0) .\n\nThus the repaired one-dimensional classiﬁcation is local at the vertices: bounded edges, graph\ncycles, and lattice saturation introduce no additional condition.\n   Positivity at inﬁnity enters the converse only through Lemma 4.13: it permits an ambient\npolyhedral norm with strictly smaller recession slope on every unbounded edge. The state-\nment neither repairs the literal integral-slope class nor addresses higher-dimensional balanced\nspaces.\n\n                                                 31\n\n    The same local relation cones also sharpen the negative result in the literal coeﬃcient\ncategory. The one-vertex construction used positivity of each ray slope. In a graph, the exact\nreplacement is strict positivity of the whole slope vector on every nonzero local balancing\nrelation.\n    Let X be a one-dimensional balanced rational polyhedral space with a ﬁnite rational\npolyhedral structure Π. For a vertex v ∈ Π(0) , retain the notation\n                                                                             \n                                                            X                \n                                      E(v)\n                            Kv = λ ∈ R≥0 :                          λe ue/v = 0 .\n                                                                             \n                                                           e∈E(v)\n\nTheorem 4.16. Let γ ∈ PAPCZ (X) be positive at inﬁnity, and reﬁne Π so that γ is aﬃne\non every edge. Fix a vertex v, and let se ∈ Z be the outgoing slope of γ on the edge germ\ne ∈ E(v). Suppose that\n                            X\n                                     λe se > 0         for every λ ∈ Kv \\ {0}.               (18)\n                           e∈E(v)\n\nThen (X, γ) does not have the literal integral-slope regularity property.\n   More precisely, choose a positive rational number R such that the closed edge-germ seg-\nments\n                             xe ([0, R]),     xe (t) := v + tue/v ,\nhave pairwise disjoint interiors, contain no other vertex, and lie in the aﬃne pieces of γ.\nThere are arbitrarily large integers N ≥ 2 such that\n                           X         \u0012            \u0013\n                                              1\n                                λe       se −         ≥0      for every λ ∈ Kv .             (19)\n                            e                 N\n\nFor any such N , put c := R/N and deﬁne the bounded literal piecewise-aﬃne obstacle uv,R,N\nby                       (\n                          c,     0 ≤ t ≤ R − c,\n       uv,R,N (xe (t)) =                           uv,R,N = 0 oﬀ the closed star.\n                          R − t, R − c ≤ t ≤ R,\nIts envelope is\n                                                             R−t\n                   Pγ (uv,R,N )(xe (t)) = γ(xe (t)) +                  (0 ≤ t ≤ R),\n                                                              N                              (20)\n                          Pγ (uv,R,N ) = γ                             oﬀ the closed star.\n\nEvery literal integral-slope approximant satisﬁes\n                                                      (N − 1)R\n                  kψ − Pγ (uv,R,N )kL∞ (X) ≥                   ,        ψ ∈ PAPCZ (X, γ).    (21)\n                                                        2N 2\nCorollary 4.17. Assume that dim Kv = 1 at every vertex of a ﬁnite rational polyhedral\nstructure on X. Let γ ∈ PAPCZ (X) be positive at inﬁnity and have positive degree. Then\n(X, γ) does not have the literal integral-slope regularity property.\n\n    Thus, on the graph class where real-polyhedral orthogonality holds by Theorem 4.15, every\npositive-degree literal reference instead fails the regularity hypothesis required by the source’s\nliteral orthogonality deﬁnition. The two statements concern diﬀerent coeﬃcient categories.\n    The degree-zero case has the opposite behaviour. Positivity at inﬁnity makes every un-\nbounded end contribute strictly positive degree. When the degree vanishes, the graph is\ncompact, and balancing at a maximum vertex forces every polyhedrally convex function to\nbe componentwise constant.\n\n                                                        32\n\nTheorem 4.18. Let X be a one-dimensional balanced rational polyhedral space admitting a\nﬁnite structure, and let γ ∈ PAPCZ (X) be positive at inﬁnity. Then the following conditions\nare equivalent:\n\n  (1) deg(γ) = 0;\n\n  (2) X is compact.\n\nWhen these conditions hold, every function in PC(X, γ) is constant on each connected compo-\nnent. For every bounded literal piecewise-aﬃne function u ∈ PAZ,b (X) and every connected\ncomponent C of X, one has\n                                                                  \u0001\n                                  Pγ (u)|C = min γ(x) + u(x) .                             (22)\n                                              x∈C\n\nThe right-hand side is a rational constant. In particular, Pγ (u) ∈ PAPCZ (X, γ) and (X, γ)\nhas the literal integral-slope regularity property.\n\n    Thus the zero-degree branch of the one-dimensional literal problem is regular. Together\nwith Theorem 4.16, this leaves only positive-degree graphs for which every positive-mass vertex\nhas a higher-dimensional local relation cone and the reference slope vector lies on a proper\nface of its dual cone.\n    The remaining positive-degree boundary admits a global obstruction which does not de-\npend on a strict reference vertex. The point is to place a rational convex combination strictly\nbetween the reference and a second literal convex function. Edgewise integral-slope concave\nroofs then give a literal obstacle whose convex envelope is that combination.\n\nTheorem 4.19. Let X be a one-dimensional balanced rational polyhedral space admitting a\nﬁnite structure, and let γ ∈ PAPCZ (X) be positive at inﬁnity. The following are equivalent:\n\n  (1) (X, γ) has the literal integral-slope regularity property;\n\n  (2) deg(γ) = 0;\n\n  (3) X is compact.\n\n   More precisely, suppose that deg(γ) > 0. Choose a rational point v in a noncompact\nconnected component, a rational number C > γ(v), and put\n\n                                        ϕ := max{γ, C}.\n\nThere is a ﬁnite rational subdivision on which γ and ϕ are aﬃne and an oriented bounded\nedge cell e on which ϕ − γ has a nonzero integral slope ke . For every integer N > |ke |, there\nis a bounded literal piecewise-aﬃne obstacle uN such that\n                                             \u0012         \u0013\n                                                 1              1\n                                  Pγ (uN ) = 1 −           γ+     ϕ.                       (23)\n                                                 N              N\n\nIf Le is the integral-aﬃne length of e and qe is the slope of the right-hand side of (23) on e,\nthen every literal integral-slope polyhedrally convex function ψ satisﬁes\n                                                      Le\n                           kψ − Pγ (uN )kL∞ (X) ≥        dist(qe , Z) > 0.                 (24)\n                                                      4\nThus the failure in positive degree is independent of the dimensions and faces of the local\nrelation cones.\n\n\n\n                                                 33\n\n    In higher dimension the edgewise concave roof has no canonical analogue, but the vertex-\ncontact mechanism does. For each vertex, an integral piecewise-aﬃne lattice norm gives a cone\nmajorizing the rational gap. Taking the minimum of these cones and the original integral gap\npreserves the prescribed vertex values while forcing the obstacle to vanish on every unbounded\ncell. This removes dimension, balancing, and local-relation hypotheses from the noncompact\nliteral obstruction.\nTheorem 4.20. Let X ⊂ NR be a noncompact rational polyhedral space admitting a ﬁnite\nstructure, and let γ ∈ PAPCZ (X) be positive at inﬁnity. Then (X, γ) does not have the literal\nintegral-slope regularity property.\n    More precisely, choose a rational point x in a noncompact connected component, a rational\nnumber C > γ(x), and put\n                                ϕ := max{γ, C},         D := ϕ − γ.\nThere are a ﬁnite rational subdivision Π, a bounded positive-dimensional cell σ ∈ Π, a primitive\nvector w ∈ Nσ , and a rational segment\n                                   I = x0 + [0, L]w ⊂ relint(σ)\nsuch that D is aﬃne on σ and its linear part k ∈ Mσ satisﬁes k(w) 6= 0. For every integer\nN > |k(w)|, there is a bounded literal piecewise-aﬃne function uN for which\n                                                   \u0012        \u0013\n                                              D      1               1\n                             Pγ (uN ) = γ +     = 1−            γ+     ϕ.                        (25)\n                                              N      N               N\nIf q is the slope of this envelope along the primitive direction w on I, then every literal integral-\nslope polyhedrally convex function ψ satisﬁes\n                                                       L\n                             kψ − Pγ (uN )kL∞ (X) ≥      dist(q, Z) > 0.                         (26)\n                                                       4\nIn particular, the literal complete-aﬃne regularity assertion fails on NR in every positive\ndimension.\n    This completely classiﬁes the repaired real-piecewise-aﬃne version of P05.2 on every one-\ndimensional balanced rational polyhedral space admitting a ﬁnite structure. Orthogonality\nholds exactly when every local cone of nonnegative balancing relations is one-dimensional.\nThe theorem allows bounded edges and cycles and shows that lattice saturation is irrelevant.\nIn the literal coeﬃcient category, one-dimensional regularity holds exactly in degree zero,\nequivalently exactly when the space is compact. Every positive-degree graph reference fails\nliteral regularity, independently of the local relation cones. More generally, literal regularity\nfails on every noncompact ﬁnite rational polyhedral space in every dimension, whether or\nnot it is balanced; in particular, the source’s literal complete-aﬃne assertion fails in every\npositive dimension. The earlier strict-vertex theorem remains a local quantitative form of this\nobstruction. Thus every graph on which real-polyhedral orthogonality holds is negative for\nliteral regularity when the literal degree is positive, but the literal failure is not conﬁned to that\ngraph class. The one-vertex orthogonality theorem and its bounded-reference-shift corollary\nare book-local real-scalar results, not results cited from the withdrawn note. The classiﬁcation\nalso explains Example 4.25: the four-ray cross has a two-dimensional cone of nonnegative\nbalancing relations. Conversely, Example 4.9 shows that lattice smoothness is suﬃcient but\nnot necessary in this class. The higher-dimensional real-PA classiﬁcation, compact higher-\ndimensional literal case, arbitrary nonseparable product obstacles, and the source coeﬃcient-\nconvention repair remain open, so P05.1 and P05.2 remain active.\n    The following elementary convex-envelope fact is the missing contact mechanism on a\ncomplete aﬃne space.\n\n                                                 34\n\nLemma 4.21. Let f : Rd → R be continuous and coercive, and let P be its greatest lower-\nsemicontinuous convex minorant. Suppose that P is polyhedral. If ∂P (x) has positive d-\ndimensional volume, then P (x) = f (x).\nTheorem 4.22. Let N have rank d, let X = NR carry the constant balancing weight c >\n0, and let γ ∈ PAR (NR ) be polyhedrally convex and positive at inﬁnity. Then (X, γ) has\nreal-polyhedral regularity in every dimension. Moreover, for every u ∈ PAR,b (NR ), writing\nP = Pγ (u) and\n                                 MApoly,R (P ) := d!c MAR (P ),\none has                        Z\n                                                      \u0001\n                                      P − (γ + u) MApoly,R (P ) = 0.\n                                NR\nNo strict-convexity hypothesis beyond positivity at inﬁnity is needed.\n    The epigraph proof in Theorem 4.22 is the real-aﬃne argument underlying the complete-\nspace discussion in [BMPS26, Remark 6.6]; the contact deduction is book-local. It cannot\nbe read as a theorem in the literal integral-slope category: Proposition 4.2 disproves that\ninterpretation already for NR = R.\n    Let r ≥ 1. For 1 ≤ i ≤ r, let Xi be a rational polyhedral space admitting a ﬁnite structure,\n                    Q\nand write pi : X := i Xi → Xi for the projection. Give X the product polyhedral structure.\nLet γi ∈ PAR (Xi ) ∩ PC(Xi ) and ui ∈ PAR,b (Xi ), and put\n                                                                      X\n                                                                      r                       X\n                                                                                              r\n             ai := γi + ui ,       Pi := Pγi (ui ),         γ :=            p∗i γi ,   u :=         p∗i ui .\n                                                                      i=1                     i=1\n\nTheorem 4.23. With the notation above, assume that\n\n                               Pi ∈ PAPCR (Xi , γi )                 (1 ≤ i ≤ r).\n\nThen\n                                                          X\n                                                          r\n                                           Pγ (u) =             p∗i Pi .                                       (*)\n                                                          i=1\nIn particular, the envelope of the separable obstacle u belongs to PAPCR (X, γ).\nCorollary 4.24. Assume in addition that every Xi is either a complete aﬃne space Ni,R or a\none-dimensional balanced rational polyhedral space admitting a ﬁnite structure, and that every\nγi is positive at inﬁnity. The product carries its product balancing cycle, the sum reference γ is\npositive at inﬁnity, and (*) holds for every tuple of bounded real-piecewise-aﬃne obstacles ui .\nThus products of ﬁnite balanced graphs and complete aﬃne spaces have real-piecewise-aﬃne\nenvelopes for all separable bounded obstacles. This includes higher-dimensional products with\nbranched singular factors.\n                                                                                  P\n    The corollary concerns the separable obstacle class u = i p∗i ui . It does not assert the\nregularity property for an arbitrary bounded real-piecewise-aﬃne function on the product.\n    The next example shows why completeness of the ambient convex geometry cannot be\nreplaced by strict positivity of the reference alone.\nExample 4.25. Let\n                                     X = (R × {0}) ∪ ({0} × R)\nwith all four ray weights equal to one, and put γ(x, y) = |x| + |y| on X. This reference is\npositive at inﬁnity and strictly polyhedrally convex on the four-ray complex. For ε > 0, deﬁne\nthe obstacle\n                    f (x, 0) = |x| + ε,   f (0, y) = |y| − ε ,    u = f − γ.\n\n                                                      35\n\nThen u is bounded and piecewise aﬃne, and\n\n                      Pγ (u)(x, 0) = |x|,       Pγ (u)(0, y) = max{0, |y| − ε}.\n\n    Indeed, the displayed candidate is the restriction of the ambient convex function\nmax{|x|, |y| − ε, 0}, hence is polyhedrally convex and lies below f . Conversely, if q ≤ f\nis an admissible polyhedrally convex function, convexity between (0, ε) and (0, −ε) gives\nq(0, 0) ≤ 0. On either horizontal ray, convexity and the asymptotic slope bound one give\nq(x, 0) ≤ |x|. On the positive vertical ray, convexity ﬁrst gives q(0, y) ≤ 0 for 0 ≤ y ≤ ε, and\nthen the same slope bound gives q(0, y) ≤ y − ε for y ≥ ε; the negative ray is identical. This\nproves the envelope formula. Its outgoing slopes at the origin have sum two, so\n\n                  MApoly (Pγ (u)){(0, 0)} = 2,         Pγ (u)(0, 0) − f (0, 0) = −ε.\n\nAll other atoms lie on the contact set, and the orthogonality integral is therefore −2ε. Finally,\na positive local one-cycle at the origin has weights a, a, b, b > 0 on the two opposing horizontal\nand two opposing vertical rays; intersection with γ has coeﬃcient 2a + 2b > 0. The strict-\nconvexity criterion of [BMPS26, Remark 3.9] applies. This is the source’s Example 6.23 with\nits sign and contact calculation made explicit.\n    There is a complementary smooth-fan warning in [BMPS26, Example 6.24, Claim 6.25,\nand Remark 6.26]. On the Bergman fan of the uniform matroid U3,4 , assign value zero to\nthe opposite rays generated by e12 and e34 = −e12 , and value one to the other primitive ray\ngenerators. The resulting polyhedrally convex reference γ admits a bounded piecewise-aﬃne\nobstacle g ≥ γ for which\n\n                    Pγ (g − γ) = γ,         MApoly (γ){0} = 4,        γ(0) < g(0).\n\nThe source proves the envelope identity cone by cone: equality ﬁrst holds on the line Re12 , then\non the original rays by one-variable convexity, and ﬁnally on each two-dimensional cone by\njoining its boundary to the diagonal ray. The mass is the direct iterated-divisor computation\non that fan. This example is tropically smooth but γ is identically zero on Re12 . Hence\nit is neither strictly convex nor positive at inﬁnity. It does not disprove the conjunction\nof a suitable higher-dimensional smoothness condition with the strict growth hypotheses in\nProblem 4.1.\n    The same Bergman-fan mechanism nevertheless survives the growth condition itself. The\npoint is to retain a ﬁnite ﬂat segment of the exceptional line, which forces contact at the\norigin, while making the reference grow outside that segment.\n\nProposition 4.26. In the notation of [BMPS26, Example 6.24 and Claim 6.25], let g ≥ γ\nbe its obstacle and put u = g − γ. Write `(x1 , x2 , x3 ) = x1 + x2 , so that\n                                                                            \u0001\n           `(e12 ) = 2,     `(e34 ) = −2,        `(e1 ), `(e2 ), `(e3 ), `(e4 ) = (1, 1, 0, −2).\n\nFor λ ∈ Q ∩ (0, 12 ) and R ∈ Q with R > 2λε, set\n\n                               γλ,R := max{γ, λ` − R, −λ` − R}.\n\nThen γλ,R is piecewise-aﬃne polyhedrally convex and positive at inﬁnity. If\n\n                                            P := Pγλ,R (u),\n\nthen P = γ on a neighbourhood of the origin. Moreover, either\n\n                                      P ∈\n                                        / PCreg,R (X, γλ,R ),\n\n                                                  36\n\nor                            Z\n                                                      \u0001\n                                   P − (γλ,R + u) MApoly,R (P ) ≤ −4ε < 0.\n                               X\nConsequently (X, γλ,R ) cannot have both real-polyhedral regularity and real-polyhedral orthog-\nonality. The same dichotomy precludes simultaneous literal regularity and orthogonality.\n\n    Thus a higher-dimensional smoothness-and-orthogonality theorem requires more than a\npolyhedrally convex reference positive at inﬁnity: even on this Bergman fan, that growth\ncondition is compatible with a forced noncontact Monge–Ampère atom. The proposition\nleaves open whether an additional combined intrinsic-smoothness and strict-convexity package\nrestores orthogonality.\n    Balancing also does not, by itself, produce an analytic space. Once a proper calibrated\ntropical morphism has been supplied, however, the recursive comparison follows from the\ncalibration and the stated generated-psh pullback condition. Genuine algebraic tropicaliza-\ntions give the principal local analytic case under the value-group hypothesis in the following\ncorollary.\n\nProposition 4.27. Let d ≥ 1, and let (X, [X]) be a pure d-dimensional balanced rational\npolyhedral space, endowed with its boundaryless tropical-space structure and its integration\ncurrent δ[X] . Let Y be a pure d-dimensional boundaryless CLD tropical space, let [Y ] be its\npositive closed current of integration, and let\n\n                                                   h : Y −→ X\n     be a topologically proper morphism of tropical spaces. Assume that\n\n                                                   h∗ [Y ] = δ[X]                                              (27)\n     and that\n\n                                          h∗ PAPC(X) ⊆ CPsh(Y ).                                               (28)\n     For a1 , . . . , ad ∈ PAPC(X), set\n                                                                         \u0001\n                         S0 = [Y ],         Sj = d0 d00 (aj ◦ h)Sj−1          (1 ≤ j ≤ d),                     (29)\n     and\n\n                                         c0 = [X],         cj = aj · cj−1 .                                    (30)\n     Then every Sj is positive and closed, every cj is an eﬀective balanced tropical cycle, and\n\n                                           h∗ Sj = δcj      (0 ≤ j ≤ d).                                       (31)\n     In particular,\n                                                               \u0001\n           h∗ d0 d00 [a1 ◦ h] ∧ · · · ∧ d0 d00 [ad ◦ h] ∧ [Y ] = δa1 ···ad ·[X] = MApoly (a1 , . . . , ad ).   (32)\n   Both iterated products in (32) are independent of the displayed order.\n   Let now γ be a piecewise-aﬃne polyhedrally convex reference function that is positive at\ninﬁnity. If\n\n                                           a1 , . . . , ad ∈ PCreg (X, γ),\n     then every ai ◦ h is continuous psh and\n\n\n                                                          37\n\n                                                                     \u0001\n                  h∗ d0 d00 [a1 ◦ h] ∧ · · · ∧ d0 d00 [ad ◦ h] ∧ [Y ] = MApoly (a1 , . . . , ad )         (33)\n   as Radon measures on X. For every simplicial polyhedral structure Π carrying γ, the\nmeasure on the right, viewed on the associated BMPS compactiﬁcation XΠ , has zero mass on\nXΠ \\ X.\n\nCorollary 4.28. Let K be an algebraically closed complete ﬁeld with a nontrivial non-\nArchimedean absolute value, with Q ⊆ − log |K × |, and let U be an irreducible very aﬃne\nK-variety of dimension d. Use the convention\n\n                 h = tropU = (− log |f1 |, . . . , − log |fn |) : U an −→ X := Trop(U )\n    for a closed embedding of U in a split torus. On the CLD side this is the sign-reversed mo-\nment chart. Equip X with its saturated lattices and analytic tropical multiplicities, and assume\nthat it is a rational balanced polyhedral space in the sense of Botero–Mazzon–Pille-Schneider.\nThen (27) and (28) hold for Y = U an . Consequently, all conclusions of Proposition 4.27\napply.\n    For ai ∈ PAPC(X), put ui = ai ◦h, endow the trivial line bundle with the piecewise-smooth\ndelta-metric\n\n                                                     k1ki = e−ui ,\n    and write Θi = c1 (OU , k·ki ) for its ﬁrst Chern delta-form. Each Θi is a positive delta-\nform. More precisely, for every ordering and every 1 ≤ j ≤ d, the product of the ﬁrst j factors\nis a positive generalized delta-form; this assertion is made for these particular Chern forms\nand not for arbitrary products of positive generalized delta-forms. The top-degree delta-form\nΘ1 ∧ · · · ∧ Θd therefore induces a positive, locally ﬁnite Radon measure µδ on U an , and\n\n            [µδ ] = d0 d00 [u1 ] ∧ · · · ∧ d0 d00 [ud ] ∧ [U an ],   h∗ µδ = MApoly (a1 , . . . , ad ).   (34)\n   No ﬁniteness of the total mass of µδ is asserted without an additional properness or support\nhypothesis.\n   More generally, take ai ∈ PCreg (X, γ) and arbitrary decreasing approximations\n\n                                     ai,k ∈ PAPC(X, γ),              ai,k & ai .\n   Let µδ,k be the locally ﬁnite delta-form measure associated with a1,k , . . . , ad,k . Then µδ,k\nconverges vaguely on U an to\n\n                                µCLD := d0 d00 [u1 ] ∧ · · · ∧ d0 d00 [ud ] ∧ [U an ].                    (35)\n    The limit is independent of all approximating sequences and satisﬁes\n\n                                        h∗ µCLD = MApoly (a1 , . . . , ad ).                              (36)\n   No assertion is made that µCLD is represented by a ﬁnite delta-form or has ﬁnite total\nmass without an additional properness or support hypothesis.\n\n    The proposition and its algebraic-chart corollary remove the recursive projection and lo-\ncal delta-form comparison gaps formerly isolated as P05.3 and P05.4 under their explicit\noperator-domain hypotheses. In the algebraic corollary, Q ⊆ − log |K × | ensures that the ra-\ntional polyhedral weights pull back to real PL functions, so the book’s PL comparison gives\nmembership in the generated psh sheaf. For a general valued ﬁeld this membership remains an\nadditional input, even when the ordinary current is positive. The propositions do not supply\n\n\n                                                           38\n\nthat general-ﬁeld operator-domain bridge, a proper polarized realization, a global semipositive\nlift, or the mass calibration required by P05.5.\n     The ﬁnal boundary step in a polarized realization is nevertheless formal once the local\ncomparison and the exact total masses are known:\nProposition 4.29. Let j : X ,→ X be an open embedding of locally compact Hausdorﬀ spaces.\nLet Y be a locally compact Hausdorﬀ space, let h : Y → X be a proper continuous map, and\nput\n                                 −1\n                           U := h (X),       h := h|U : U −→ X.\nLet µNA be a ﬁnite positive Radon measure on Y , and let µpoly be a ﬁnite positive Radon\nmeasure on X. Suppose that                 \u0001\n                                  h∗ µNA |U = µpoly                                  (37)\nand\n                                       µNA (Y ) = µpoly (X) < ∞.                                        (38)\nThen\n                                              µNA (Y \\ U ) = 0                                          (39)\nand\n                                              h∗ µNA = j∗ µpoly                                         (40)\nas ﬁnite positive Radon measures on X, where j∗ µpoly denotes extension by zero across X \\ X.\n    Consequently, in a polarized realization for P05.5, assume that\n\n                               µNA = MAθ (u),                µpoly = MApoly (a),\n\nthat (37) holds, and that established mass formulae give\n\n                                µNA (Y ) = (Ld ) = deg(γ) = µpoly (X).\n\nThen the global comparison is (40). This consequence asserts none of the required realization,\npolarization, plurisubharmonicity, local-comparison, or mass-formula hypotheses.\n   At the model level, the local comparison, mass identity, and calibration inputs can be\npackaged into an explicit common-measure statement. The following proposition also records\nexactly where the GK comparison is not being asserted under the standing discretely valued\nﬁeld hypotheses.\nProposition 4.30. Assume the BFJ ﬁeld and variety hypotheses of (Book 24.1), with the\nvariety denoted by Y and dim Y = d. Let X be a pure d-dimensional balanced rational polyhe-\ndral space, let γ be a piecewise-aﬃne polyhedrally convex reference function positive at inﬁnity,\nand let a1 , . . . , ad ∈ PAPC(X, γ). Write\n                                                 X                                 X\n          µpoly := MApoly (a1 , . . . , ad ) =         mq δ q ,     mq > 0,              mq = deg(γ),   (41)\n                                                 q∈Q                               q∈Q\n\nwhere Q ⊆ X is ﬁnite.\n   Let j : X ,→ X be an open embedding into a locally compact Hausdorﬀ space. Let L be an\nample line bundle on Y , let k · k0 be a semipositive model metric on L, and put θ = c1 (L, k · k0 ).\nFor 1 ≤ i ≤ d, let\n                                          k · ki = e−ui k · k0                                 (42)\nbe a semipositive model metric on L, and set θi = θ + ddc ui . Suppose that all the θi are\ndetermined on one normal ﬂat projective model Y, write\n                                         X\n                                  Ys =        bE E,            xE = b−1\n                                                                     E ordE ,\n                                          E\n\n\n                                                          39\n\nand deﬁne the nonnegative intersection weights\n                                                                \u0001\n                                wE := bE θ1,Y |E · · · θd,Y |E ≥ 0.                      (43)\n\n      Let h : Y an → X be a proper continuous map, put\n                                            −1\n                                  U := h         (X),    h := h|U ,\n\nand assume that\n                              ui |U = (ai − γ) ◦ h        (1 ≤ i ≤ d).                   (44)\nAssume moreover the exact mass identity\n\n                                            (Ld ) = deg(γ)                               (45)\n\nand the componentwise calibration\n                                      X\n                                            w E = mq       (q ∈ Q).                      (46)\n                                 E: xE ∈U\n                                 h(xE )=q\n\n   Then the BFJ mixed model measure, the Chambert–Loir mixed measure, and the CLD\nproduct of the formal ﬁrst Chern currents all coincide with\n                                                               X\n                             µNA := MAθ (u1 , . . . , ud ) =        wE δxE .             (47)\n                                                                E\n\nThey satisfy\n                                          µNA (Y an \\ U ) = 0                            (48)\nand\n                                          h∗ µNA = j∗ µpoly                              (49)\nas ﬁnite positive Radon measures on X.\n    The conclusion is conditional on the proper polarized realization, the global model lifts\n(44), semipositivity, the mass identity (45), and the intersection-theoretic calibration (46).\nIt asserts none of those inputs for an arbitrary balanced polyhedral space. It also makes no\nassertion about a GK delta-form product on the original analytiﬁcation under these discretely\nvalued ﬁeld hypotheses.\n\n   Thus no separate compactiﬁcation argument is needed after those two hard inputs have\nbeen established. The two propositions do not construct a proper polarized realization or the\ncomponentwise calibration and therefore narrow, but do not retire, P05.5.\n   The unconditional analytic result in the source is narrower. For the toric degenerations\nof Calabi–Yau complete intersections in its §7, let X be the tropicalization, let γ be the\npolarization weight, and let µ0 be Lebesgue measure on the essential skeleton. Under the\nthree assumptions\n\n                    (Ld ) = deg(γ),       ϕ ∈ PCreg (X, γ),         MApoly (ϕ) = µ0 ,\n\nand semipositivity of Ψ = ϕ0 +(ϕ−γ)◦trop, Proposition 7.2 of [BMPS26] proves MANA (Ψ) =\nµ0 and, over C((t)), the comparison property. Its Lemma 7.3 computes every maximal-cell\nweight as one from analytic degree divided by lattice index. The local equality is then (15)\ntogether with Vilsmeier’s real/non-Archimedean comparison [Vil21, Theorem 1.1]; equality\naway from lower-dimensional skeleton faces and equality of total masses force the global\nidentity. None of this is a realization theorem for an abstract balanced space.\n\n                                                    40\n\n    The source itself formulates three sharper tasks that organize this broad problem: enlarge\nthe notion of polyhedral smoothness so that higher-dimensional regularity and orthogonality\nhold; characterize polarized Calabi–Yau families whose tropicalizations satisfy those proper-\nties; and determine which matroids have Bergman fans satisfying orthogonality [BMPS26,\npp. 3–5, §1.5, and Remark 6.27]. By contrast, the analytic realization of the cross-fan was\na diagnostic problem formulated in this book, not a question attributed to Botero–Mazzon–\nPille–Schneider. Its literal compact-source and weighted-current parts are now settled by\nBook Proposition 69.2.3, Book Proposition 69.2.4. The source’s only stronger strict-positivity\nprospect is expressly assigned to its upcoming sequel: its bibliography lists that sequel as “in\npreparation.” It is therefore not used here as an available theorem on regularity or orthog-\nonality [BMPS26, pp. 5 and 60]. The stronger upstairs-equality problem in Problem 12.1\nis not merely book-local: after removing an ill-deﬁned delta-current alternative, it is pre-\ncisely the analytic specialization of the Bedford–Taylor question posed in [CLD25, §8.6.1 and\nDeﬁnition 8.6.2].\n    Thus the audit gives six verdicts. The real-scalar complete aﬃne case in Theorem 4.22\nis veriﬁed, whereas literal integral-slope regularity already fails on the aﬃne line by Proposi-\ntion 4.2; strict positivity alone is disproved by Example 4.25; positive growth alone, even on\nthe displayed Bergman fan, cannot force the conjunction of regularity and orthogonality by\nProposition 4.26; the recursive CLD and delta-form comparison is veriﬁed under the intrinsic\nproper calibration hypotheses of Proposition 4.27, with the genuine algebraic tropicalization\nsupplied, under its stated value-group hypothesis, by Corollary 4.28; the global polarized\nnon-Archimedean Monge–Ampère comparison remains open beyond the realized source cases\nbecause the proper polarization, lift, mass, and component calibration are additional inputs;\nand the main higher-dimensional local contact problem remains open. The missing local asser-\ntion is a contact theorem on singular fans: under an intrinsic smoothness and strict-positivity\npackage, positive top intersection mass of an envelope should force contact with the obstacle.\nNeither a proof nor a counterexample satisfying both parts of that package is presently known.\n\n\n\n\n                                              41\n\n",
  "completionCriteria": "Solve the entire originalP05.2 classification problem: give rigorous necessary and sufficient structural/geometric conditions on the balanced rational polyhedral pair and actual reference, with the exact contact integral for ALL admissible obstacles in the stated coefficient category. Check all envelope/regularization and genuine MApoly antecedents rather than declaring a measure of a nonregularizable endpoint. Fix literal integral-slope/rational-constant and explicit real-scalar conventions separately wherever relevant. A tautological restatement of orthogonality, only total mass, a narrower cone/product/fan/obstacle class, or an added unexplained conditional premise does not close the whole original. A genuine new scoped theorem or obstruction may be reported precisely with candidate=false and the full original kept open. Existing known one-dimensional/complete-affine/product or supplied-book cases are context, not a new full solution. Every essential ungranted dependency must be reconstructed or exactly primary-source checked, including the complete pertinent proof unit and each exact application."
}
END COMPLETE BODY UNCHANGED WHOLE ORIGINAL TASK; SCOPE DATA

BEGIN COMPLETE BODY COMPLETE CALLER GRANT A
\documentclass[11pt]{article}
\usepackage[margin=1in]{geometry}
\usepackage{amsmath,amssymb,amsthm,booktabs,array}
\usepackage[T1]{fontenc}
\usepackage{hyperref}
\hypersetup{colorlinks=true,linkcolor=blue,urlcolor=blue}
\newtheorem{theorem}{Theorem}
\newtheorem{lemma}[theorem]{Lemma}
\newtheorem{proposition}[theorem]{Proposition}
\newtheorem{remark}[theorem]{Remark}
\newcommand{\R}{\mathbb R}
\newcommand{\Z}{\mathbb Z}
\newcommand{\Q}{\mathbb Q}
\newcommand{\MA}{\operatorname{MA}_{\mathrm{poly}}}
\newcommand{\MARpoly}{\operatorname{MA}_{\mathrm{poly},\R}}
\newcommand{\PC}{\operatorname{PC}}
\newcommand{\PA}{\operatorname{PA}}
\newcommand{\PAPC}{\operatorname{PAPC}}
\newcommand{\reg}{\mathrm{reg}}
\newcommand{\relint}{\operatorname{relint}}
\newcommand{\eps}{\varepsilon}
\title{A strict-growth contact obstruction on the\texorpdfstring{$U_{3,4}$}{U3,4} Bergman fan\\\large Scoped progress on original P05.2}
\author{Research draft}
\date{7 October 2026}
\begin{document}
\maketitle
\begin{abstract}
We construct a bounded continuous integral piecewise-affine obstacle on the weight-one, two-dimensional $U_{3,4}$ Bergman fan. The reference is integral piecewise affine, strictly convex relative to its fine fan, and positive at infinity. Its exact envelope is itself integral piecewise affine and regularizable. The raw recursive intersection masses are $4,3,3$, the total mass equals the reference degree $10$, and the contact integral is $-4\eps$. A larger explicit parameter family has the same mechanism. All geometry, convexity, envelope, and divisor calculations are proved directly. A second explicit obstacle shows failure of literal regularity for the simplest reference. This is an obstruction, not a classification of general balanced rational polyhedral pairs; original P05.2 remains unresolved in this submission.
\end{abstract}

\section{Conventions, antecedents, and scope}
We test the envelope and raw polyhedral intersection definitions in the fixed primary version \cite{BMPS}, not a replacement operator. A finite rational polyhedral structure has saturated tangent lattices $N_\sigma=N\cap\operatorname{span}_{\R}(\sigma-\sigma)$. An inward normal $n_{\sigma/\tau}$ represents the primitive generator of $N_\sigma/N_\tau$ pointing into $\sigma$. For a balanced $k$-cycle $c$ and a piecewise-affine $f$, the divisor is
\begin{equation}\label{divisor}
 (f\cdot c)(\tau)=\sum_{\sigma\succ\tau}c(\sigma)f_\sigma(n_{\sigma/\tau})
 -f_\tau\left(\sum_{\sigma\succ\tau}c(\sigma)n_{\sigma/\tau}\right).
\end{equation}
Here $f_\sigma$ denotes its linear part, and balancing makes the summed normal tangent to $\tau$. A convex bend has positive sign. In dimension two the raw measure is
\[\MA(f)=\sum_v(f\cdot(f\cdot[X]))(v)\delta_v.\]
No further factorial is inserted. Alexandrov mass is lattice-normalized subgradient area, without a factorial. At the complete affine germs occurring below we verify directly that the raw mass is $2!$ times that area. No ambient Alexandrov measure is substituted at the singular origin.

We distinguish $\PA_{\Z}$, with integral linear parts and rational constants, from $\PA_{\R}$, with arbitrary real affine coefficients on a finite \emph{rational} structure. A polyhedral convex combination (PCC) is a barycentric combination $x=\sum\alpha_i x_i$ whose center lies in a face $\tau$ and whose endpoints lie in faces $\sigma_i\succeq\tau$ on some rational structure. The source prints rational endpoints; our upper-bound argument respects that restriction. Our constructed continuous functions satisfy Jensen inequalities even for real endpoints. Set $\PAPC_*=\PA_*\cap\PC$, $*=\Z,\R$, and let $\PC^{\reg}_*(X,\Gamma)$ consist of uniform decreasing limits of $\PAPC_*$ functions with bounded difference from $\Gamma$.

The envelope is
\begin{equation}\label{envelope}
 P_\Gamma(U)=\sup\{q:q\leq\Gamma+U,\ q\in\PC(X),\ q\leq\Gamma+O(1)\}.
\end{equation}
The competitors in this definition are not restricted to integral slopes. Every measured envelope in our obstruction is already PA and regularizable: a constant approximating sequence suffices, or one can add decreasing positive rational constants. We assert no real regularity theorem for all obstacles on this fan. The source's orthogonality definition assumes pair-level regularity. Our conclusions therefore exclude simultaneous regularity and universal orthogonality and exhibit actual failure of contact at a valid endpoint; they do not assume that antecedent for all other obstacles.

Strictness below is the precise local affine-support condition relative to the fine fan: a support equals the reference on each proper face and is strictly smaller nearby off that face. It implies strict Jensen inequalities for nontrivial PCCs with positive active coefficients. Zero-coefficient terms are discarded for this strict test. The printed source combines coefficients in $[0,1]$ with a strict condition counting endpoints; counting zero-coefficient endpoints would make any strict function impossible. Our strict supports and positive divisor tests are independent of that degeneracy. Weak PC is unchanged.

\section{The balanced lattice fan}
Put $N=\Z^3$ and
\[e_1=(1,0,0),\quad e_2=(0,1,0),\quad e_3=(0,0,1),\quad e_4=(-1,-1,-1),\qquad e_{ij}=e_i+e_j.\]
Let $\sigma_{ij}=\R_{\geq0}e_i+\R_{\geq0}e_j$ for $i<j$, and $X=\bigcup_{i<j}\sigma_{ij}$. The fine fan $\Sigma$ splits every $\sigma_{ij}$ at its diagonal ray $e_{ij}$. Give all twelve two-dimensional cones weight one.

\begin{lemma}\label{geometry}
This fan is balanced, and every fine cone is unimodular in its saturated tangent lattice. It is the fine $U_{3,4}$ Bergman fan.
\end{lemma}
\begin{proof}
Any three of the four $e_i$ form a $\Z$-basis. Thus $(e_i,e_j)$ is a saturated two-dimensional basis, and replacing $e_j$ by $e_{ij}$ preserves that property. At a singleton ray $e_i$ choose inward normals $e_j$, $j\ne i$, in the adjacent cones $(e_i,e_{ij})$. Their sum is $-e_i$, hence zero modulo $\Z e_i$. At a pair ray use inward normals $e_i,e_j$; their sum is $e_{ij}$. This proves balancing with the specified saturated lattices and primitive normals.

In $\Z^4/\Z(1,1,1,1)$ the standard vectors map to the $e_i$. A representative of a point of $X$ has two possibly positive coordinates and two zero coordinates; equivalently its minimum coordinate is attained at least twice. The uniform rank-three matroid on four elements has just the full ground set as its circuit. Thus its circuit minimum condition gives precisely this support. Its nonempty proper flats have sizes one and two, and their inclusion chains give the twelve fine cones. This establishes the stated Bergman description directly. Transversally at $e_i$ there is a three-ray fan with its unique positive relation; at $e_{ij}$ the support is locally an affine plane. These explicit properties, and the origin's displayed Bergman fan, are the matroidal and lattice smoothness properties used here. No stronger undefined smoothness hypothesis is claimed.
\end{proof}

\section{Local supports without external convexity dependencies}
\begin{lemma}\label{support}
Suppose a continuous function $f$ on $X$ has an ambient affine local support at every point. Then it is convex on every segment contained in $X$ and satisfies every PCC inequality. If the support equals $f$ along a face, intersection with any nonnegative balanced cycle has nonnegative coefficient there.
\end{lemma}
\begin{proof}
On a segment subtract the chord from $f$. If the difference has a positive maximum, its maximum set is a nonempty closed subset of the open segment. At any maximum point the slope of a local supporting affine function must be zero, by using both directions on the segment. The local support then forces the maximum set to be open. Connectedness contradicts the zero endpoint values. This proves convexity on the segment.

For a PCC centered at $x$, the segment $[x,x_i]$ is contained in its face $\sigma_i$ and hence in $X$. Convexity propagates the supporting slope $\ell$ at $x$ to each endpoint:
\[f(x_i)\geq f(x)+\ell(x_i-x).\]
Summing cancels the linear terms. For an intersection coefficient, choose a support agreeing on $\tau$. Formula \eqref{divisor} becomes
\[(f\cdot c)(\tau)=\sum c(\sigma)(f_\sigma-\ell)(n_{\sigma/\tau})\geq0.\]
Balancing cancels the tangent correction, and each summand is nonnegative by the inward support inequality. The same cancellation proves independence from the tangent lift of an inward normal.
\end{proof}

For these two-dimensional complexes refinement independence can also be proved directly. A new edge inside an affine cell has cancelling opposite normal contributions. An existing bent edge retains its coefficient under subdivision. A new vertex on an affine edge of the resulting one-cycle has cancelling outgoing slopes. Old vertex coefficients are unchanged. Consequently the calculations on our specified complex give the same raw operator on common refinements. We shall also verify explicitly every balance of the first intersection cycle. No general commutativity, analytic comparison, or operator-extension theorem is needed.

\section{The strict-growth obstruction}
Let $\mathcal E=\{\{1,2\},\{3,4\}\}$. In $\sigma_{ij}$ write $x=a e_i+b e_j$, $a,b\geq0$, and define
\begin{align*}
 h(x)&=\max(a,b),\quad\text{on all six cones},\\
 \eta(x)&=\begin{cases}|a-b|,&\{i,j\}\in\mathcal E,\\\max(a,b),&\{i,j\}\notin\mathcal E,\end{cases}\\
 u_\eps(x)&=\begin{cases}(\eps-\min(a,b))_+,&\{i,j\}\in\mathcal E,\\\eps,&\{i,j\}\notin\mathcal E.\end{cases}
\end{align*}
Here $\eps\in\Q_{>0}$. These definitions agree at all common rays and at zero. All three functions are continuous literal PA on finite rational structures, and $0\leq u_\eps\leq\eps$. On $\R^4/\R(1,1,1,1)$, $h$ is the restriction of the ambient convex norm $\max_i z_i-\min_i z_i$.

\begin{theorem}\label{main}
Let $A\geq0$, $B>0$, $C>B$ be real numbers, set $S=A+B$, and put $\Gamma=A\eta+B h$, $U=C u_\eps$. The reference is strictly convex relative to $\Sigma$ and positive at infinity. Its exact envelope is
\begin{equation}\label{Pformula}P_\Gamma(U)=P=\Gamma+B u_\eps\in\PAPC_{\R}(X,\Gamma).\end{equation}
The real-linear extension of the raw finite PA intersection formula gives
\begin{equation}\label{mass}
 \MARpoly(P)=4S^2\delta_0+B(4A+3B)(\delta_{\eps e_{12}}+\delta_{\eps e_{34}}).
\end{equation}
Both reference and endpoint have total raw mass $4A^2+16AB+10B^2$, but
\begin{equation}\label{contact}
 \int_X(P-(\Gamma+U))\MARpoly(P)=-4(C-B)\eps S^2<0.
\end{equation}
If $A,B,C$ are integers, reference, obstacle, and endpoint are literal PA and the endpoint lies in $\PC^{\reg}_{\Z}$. The measure in \eqref{mass} is then exactly the literal raw operator.
\end{theorem}

\subsection{Convexity, strictness, growth, and endpoint domain}
\begin{proof}[Proof of the convexity and domain assertions]
Both $h$ and $\eta$ are convex on each coarse cone. At a point $r e_i$, $r>0$, let $j$ be its exceptional partner and $k,l$ the remaining two indices. The germ of $\eta$ is ambient affine, with linear values $(1,-1,0,0)$ on $(e_i,e_j,e_k,e_l)$. These values sum to zero, so they define an ambient linear form. At zero the support is zero, since $\eta\geq0$. Pair-ray neighborhoods lie in their coarse two-dimensional plane, where the convex formulas have affine supports; interior points have supports too. Lemma \ref{support} proves $\eta$ is PC. The ambient norm formula proves the same for $h$.

The longitudinal and transverse slopes of $\Gamma$ at $r e_i$ are $S$ and $-A,0,0$. The ambient form with values
\[S,\quad -A-B/3,\quad-B/3,\quad-B/3\]
has strictly positive transverse support slack $B/3$ in each incident cone and agrees along the ray. At an exceptional pair ray the convex bend is $2A+B>0$; at the other pair rays it is $S>0$. The average of the two plane gradients gives a strict support on either side. At the vertex $\Gamma\geq B h>0$ off zero gives the strict zero support. Thus every proper fine face has a strict support, and convexity propagates strict local slack along its incident faces to give the active strict Jensen inequality. Conicality and $\Gamma\geq B h$ prove strictly positive recession slope in every nonzero recession direction, so $\Gamma$ is positive at infinity.

On an exceptional coarse cone,
\begin{equation}\label{maxP}P=\max\{\Gamma,\ B\eps+S|a-b|\};\end{equation}
on every other coarse cone $P=B\eps+S\max(a,b)$. Thus $P$ is convex on those cones. At $r e_i$ its germ is ambient affine, with linear values $(S,-S,0,0)$ on $(e_i,e_j,e_k,e_l)$. At zero the germ is $B\eps+S\eta$, which has the constant support $B\eps$. Pair-ray neighborhoods and the new bends in \eqref{maxP} lie in a single plane and have the displayed convex supports. Hence Lemma \ref{support} proves PC and intersection positivity of $P$.

The finite rational structure is explicit. In each exceptional half-cone $a\geq b$, split at $b=\eps$, and similarly with $a,b$ interchanged. Each region has vertices among $0,\eps e_{ij}$ and the appropriate recession generators $e_i,e_{ij}$. Keep the fine cones elsewhere. There are sixteen top cells and exactly the three vertices $0,\eps e_{12},\eps e_{34}$. All coefficients are integral when $A,B$ are integers. Finally $P-\Gamma=B u_\eps$ is bounded and $P\leq\Gamma+C u_\eps$. Therefore it is a competitor, PA, and regularizable in the asserted category. This does not use pair-level regularity.
\end{proof}

\subsection{Envelope maximality against every competitor}
\begin{proof}[Proof of \eqref{Pformula}]
Let $q$ be any competitor in \eqref{envelope}. The rational endpoints $\eps e_{12}$ and $\eps e_{34}=-\eps e_{12}$ have obstacle value $B\eps$. Their midpoint gives $q(0)\leq B\eps$. On a singleton ray the obstacle bound is $q(r e_i)\leq Sr+C\eps$. For rational $R>r$, combine $0$ and $R e_i$ and then let $R\to\infty$. The result is
\begin{equation}\label{raybound}q(r e_i)\leq Sr+B\eps.\end{equation}
The identical argument applies to nonexceptional pair rays, also of reference slope $S$. On an exceptional pair ray, the segment from zero to $\eps e_{ij}$ and the direct obstacle bound give
\[q(r e_{ij})\leq\begin{cases}B\eps,&0\leq r\leq\eps,\\Br,&r\geq\eps.\end{cases}\]
These are rational-endpoint PCC bounds and require no continuity or PA hypothesis on $q$.

Take a rational point of an exceptional cone with $a\geq b$, $d=a-b$. For rational $0<\theta<1$ use
\begin{equation}\label{mix}
 a e_i+b e_j=\theta\frac d\theta e_i+(1-\theta)\frac b{1-\theta}e_{ij}.
\end{equation}
If $b<\eps$, choose $\theta$ small enough that $b/(1-\theta)\leq\eps$. The ray bounds give $q(x)\leq Sd+B\eps=P(x)$. If $b\geq\eps$, they give $q(x)\leq Sd+Bb+\theta B\eps$; letting $\theta\downarrow0$ gives $q(x)\leq Sd+Bb=P(x)$. The diagonal case $d=0$ is already covered, and the other half-cone is identical. On a nonexceptional half-cone both ray bounds are $Sr+B\eps$, so \eqref{mix} gives $q(x)\leq S\max(a,b)+B\eps=P(x)$.

Thus $q\leq P$ at all rational points. For an arbitrary point $x$, choose successively smaller rational simplices in its relative rational face containing $x$, and express $x$ barycentrically in their rational vertices. These combinations are PCCs after rational subdivision. Applying the rational bound to the vertices and using continuity of $P$ gives $q(x)\leq P(x)$. Since $P$ itself is a competitor, equality \eqref{Pformula} follows on all of $X$. The displayed envelope is continuous, so its upper-semicontinuous regularization is the same function. This proves maximality over all PC competitors, not just an ansatz or a separable obstacle class.
\end{proof}

\subsection{Raw masses, factorial check, and the contact integral}
\begin{proof}[Proof of \eqref{mass} and \eqref{contact}]
For a conical PA function on $\Sigma$ write $a_i=f(e_i)$ and $b_{ij}=f(e_{ij})$. The primitive inward normals of Lemma \ref{geometry} give
\begin{equation}\label{fanweights}
 (f\cdot[X])(e_i)=\sum_{j\ne i}b_{ij}-2a_i,\qquad
 (f\cdot[X])(e_{ij})=a_i+a_j-b_{ij}.
\end{equation}
Indeed the transverse slope on $e_j$ is $b_{ij}-a_i$ and $\sum_{j\ne i}e_j=-e_i$; at a pair ray the normals sum to $e_{ij}$. At a vertex the next divisor is the sum of weights times outgoing slopes. Constants contribute nothing.

Near zero, $P=B\eps+S\eta$. Thus the first cycle has singleton weights zero, exceptional pair weights $2S$, and other pair weights $S$. It is balanced since $e_{12}+e_{34}=0$ and the sum of the remaining four pair vectors is zero. The exceptional outgoing slopes are zero and the other pair slopes $S$, yielding raw mass $4S^2$.

At $p=\eps e_{12}$ use the saturated basis $e_1,e_2$ and local coordinates $x,y$. After removing the constant $B\eps$, \eqref{maxP} has gradients
\[(S,-A),\quad(-A,S),\quad(S,-S),\quad(-S,S).\]
The local first cycle and outgoing slopes are
\begin{center}
\begin{tabular}{ccc}\toprule
Primitive direction&First divisor weight&Outgoing slope\\\midrule
$(1,1)$&$2A+B$&$B$\\
$(-1,-1)$&$2S$&$0$\\
$(1,0)$&$B$&$S$\\
$(0,1)$&$B$&$S$\\\bottomrule
\end{tabular}
\end{center}
On the positive diagonal choose inward normals $(1,0),(0,1)$: their slope sum $2S$ minus tangent slope $B$ is $2A+B$. On the negative diagonal the same inward normals have slope sum $2S$ and tangent slope zero. Across each positive axis the opposing normal slope difference is $B$. The balance is
\[(2A+B)(1,1)+2S(-1,-1)+B(1,0)+B(0,1)=0.\]
The second mass is therefore $(2A+B)B+2BS=B(4A+3B)$. At $\eps e_{34}$ the calculation is identical. There are no other vertices, hence no other atoms. The first cycle's only vertex balances are precisely these three; its open edges are straight weighted lines. Thus it is a genuine globally balanced intersection cycle.

The ordered gradient polygon $(S,-S),(S,-A),(-A,S),(-S,S)$ has shoelace area $B(4A+3B)/2$. Its area is the Alexandrov atom: the subdifferential of a maximum of affine forms is the convex hull of the active gradients. Inclusion of that hull follows from the supporting inequalities; exclusion follows by separating a point outside the hull and testing the separating direction. The direct raw computation therefore equals $2!$ times the lattice-normalized area. This proves the needed normalization here without a toric or analytic dependency.

For $\Gamma$, formula \eqref{fanweights} gives singleton weights $B$, exceptional pair weights $2A+B$, and other pair weights $S$. Its sole-vertex mass is
\[4BS+2B(2A+B)+4S^2=4A^2+16AB+10B^2.\]
The endpoint has the same total $4S^2+2B(4A+3B)$. But its obstacle gap is $(B-C)u_\eps$, equal to $(B-C)\eps$ at zero and zero at both other atoms. This proves the exact negative integral \eqref{contact}.
\end{proof}

\begin{remark}\label{simplest}
The choice $A=0,B=1,C=2$ gives $\Gamma=h$, $U=2u_\eps$, $P=h+u_\eps$, with
\[\MA(P)=4\delta_0+3\delta_{\eps e_{12}}+3\delta_{\eps e_{34}},\quad\deg(h)=10,\quad\int_X(P-(h+2u_\eps))\MA(P)=-4\eps.\]
Every displayed function is literal PA and this endpoint is literal regularizable. The reference has strict local supports, positive recession slopes, and positive first divisor weight one at all ten fine rays. Hence positive growth, strict reference convexity in the specified sense, unimodular matroidal fan geometry, and correct total mass still do not force the asserted contact identity. This does not claim that every possible stronger intrinsic smoothness package has been disproved.
\end{remark}

\section{An independently checked literal regularity failure}
\begin{proposition}\label{literal}
For the reference $h$ above, literal pair-level regularity fails. For each integer $n\geq2$, the bounded literal obstacle
\[v_n=\min\{1/n,(1-h)_+\}\]
has exact envelope
\[Q_n=\max\{h,(1-1/n)h+1/n\},\]
and every literal PA PC function $\psi$ satisfies
\[\|\psi-Q_n\|_{L^\infty(X)}\geq\frac1{4n}.\]
\end{proposition}
\begin{proof}
The obstacle has slopes zero or minus those of $h$ and rational break levels. The candidate $Q_n$ is ambient convex and differs boundedly from $h$. On $h\leq1$ its difference from $h$ is $(1-h)/n$, at most both $1/n$ and $1-h$; outside that region it equals the obstacle $h$. Thus it is a competitor.

Every competitor has $q(0)\leq1/n$ and $q(y)\leq1$ when $h(y)=1$. For rational $x$ with $0<h(x)\leq1$, join zero to the rational point $y=x/h(x)$. The PCC inequality gives $q(x)\leq(1-h(x))/n+h(x)$. The cases zero and $h\geq1$ are direct, and rational simplices as in the main proof cover all other points. Thus $Q_n$ is the exact envelope.

On the primitive segment $r e_1$, $0\leq r\leq1$, its slope is $q=1-1/n$. A literal PA convex $\psi$ has nondecreasing integral slopes there. Choose its right-hand slope $k$ at the midpoint and let $\delta$ be its uniform error. If $k\geq1$, its right-half increment is at least $1/2$; comparing with $Q_n$ yields $2\delta\geq(1-q)/2=1/(2n)$. If $k\leq0$, its left-half increment is at most zero, yielding $2\delta\geq q/2\geq1/(2n)$. Thus $\delta\geq1/(4n)$, excluding uniform literal regularization. No literal regularizable MA is assigned to this endpoint. The main endpoint in Remark \ref{simplest}, which is genuinely literal PA, is unaffected.
\end{proof}

\section{Comparison with the original request and failed approaches}
The source's Example 6.24 and complete Claim 6.25 proof were read in the fixed version, but its assertions are not used as grants. Our function $\eta$ is reconstructed by local supports and its masses by \eqref{fanweights}. The explicit replacement of a flat reference by $h$ and the roof $2u_\eps$ gives a strictly positive-growth reference and an actual PA endpoint with a noncontact atom. It is not a special product example. Nevertheless it is one fan obstruction, not necessary and sufficient conditions for all balanced rational polyhedral pairs and actual references with all admissible obstacles. Real regularity for all obstacles on this fan remains unproved here. The literal reference $h$ is outside the pair-level regularity domain by Proposition \ref{literal}; the main failure is still measured at a valid literal endpoint. Original P05.2 is not closed.

Two unsuccessful mechanisms are retained. A full-dimensional ambient contact argument cannot use ambient subgradient volume in place of the singular fan's raw top intersection: the envelope is flat along its exceptional two-sided line but has positive raw origin mass. A small perturbation plus continuity argument in changing reference classes would require common operator domains and local continuity not supplied by merely having different growth references. The direct envelope formula eliminates those missing premises rather than assuming them.

The supplied dossier's printed cross-fan obstacle assigns $+\eps$ and $-\eps$ to the shared origin through its two axes; it is not continuous as printed. It is unused here. Our roof equals $\eps$ at zero on every cone, and is continuous and bounded. Essential control-glyph repairs are fixed by the primary source: the PCC relation is inclusion as a face, and the contact expression uses ordinary grouping parentheses. No other dossier hypothesis is removed or promoted to a grant.

\section{Finite evidence and reproducibility}
The standard-library Python program \texttt{check\_obstruction.py} uses exact fractions, with four parameter tuples in \texttt{obstruction-input.json}. It checks all twelve saturated-cone calculations and all stated balances, masses, degree formulas, and polygon areas. For each tuple it also exhausts a specified set of 1,014 point inequalities and 1,800 midpoint inequalities. Those 4,056 point and 7,200 midpoint checks are exhaustive only for the finite lists. They do not certify a continuum envelope or an analytic theorem; the preceding proofs establish the mathematical statements independently.

\begin{center}\small
\begin{tabular}{ccccc}\toprule
$(A,B,C,\eps)$&Degree&Origin&Each other atom&Contact integral\\\midrule
$(0,1,2,1)$&$10$&$4$&$3$&$-4$\\
$(2,1,2,1)$&$58$&$36$&$11$&$-36$\\
$(1/3,2/5,7/6,3/2)$&$188/45$&$484/225$&$76/75$&$-2783/1125$\\
$(1,1/10,1,1/4)$&$57/10$&$121/25$&$43/100$&$-1089/1000$\\\bottomrule
\end{tabular}
\end{center}
All assertions passed. Programs, input, output, environment details, source retrieval records, source application ledger, full \texttt{argument.md}, and structured notes are retained in the supplied artifact workspace. No installation or resource-heavy compute was used; no supervised compute service was exposed. The runtime's requested model label was not independently selectable, so no model change is claimed. Rerun with
\begin{verbatim}
python check_obstruction.py
python source_provenance.py
pdflatex -interaction=nonstopmode -halt-on-error P05.2-paper.tex
pdflatex -interaction=nonstopmode -halt-on-error P05.2-paper.tex
\end{verbatim}
Execution success is not verification of mathematical correctness. This is an unverified research draft, with candidate status false.

\appendix
\section{Source application ledger and provenance policy}
Current literature was searched before choosing the obstruction. Actual queries are retained in \nolinkurl{execution-requests.md}, and actual response text under \texttt{sources/}. No later resolving primary result was found in those searches; no assertion of exhaustive bibliographic absence follows. The primary version used is
\begin{center}\small
\url{https://arxiv.org/pdf/2603.08664v1}\\
\url{https://arxiv.org/html/2603.08664v1}\\
\url{https://arxiv.org/abs/2603.08664v1}.
\end{center}
The abstract page records submission on 9 March 2026; the PDF is dated 10 March 2026. The web tool reports 62 pages and 4,580 extracted lines. We read complete pertinent units, including the definitions of normals, PA coefficients, raw divisor and PA measure, the full normal-invariance argument, complete refinement Lemma 2.34, complete PA/PC Lemma 3.4, strictness Definition 3.8 and Remark 3.9, envelope Definition 6.2, orthogonality Definition 6.9, complete factorial Proposition 4.12 proof, and complete Example 6.24--Claim 6.25--Remarks 6.26--6.27. The exact intervals and uses are in the separate quote-free \texttt{source-application-ledger.md}. Definition 3.23 is the printed regularizable definition; the dossier's reference to Definition 3.22 is an internal source numbering inconsistency.

Only definitions and conventions are imported. The operator-extension theorem was inspected only in part and is \emph{not} an application dependency. Its full proof, nor a real-scalar repair, is claimed here. The factorial proposition has toric proof dependencies; we do not import those either, since the needed local identity is reconstructed by divisor and polygon calculations. The matroid description and all convexity, envelope, balance, and measure antecedents used by the theorem have proofs above.

The original PDF byte stream was not downloaded: shell curl failed through the existing configured proxy, and no settings were changed. The web-tool PDF and HTML text responses were retained as actual UTF-8 JSON. Byte lengths and SHA-256 hashes in \nolinkurl{evidence/source-provenance.json} apply to these saved files and the actual input, never to an unavailable original PDF. Rendered PDF pages were visually inspected; the returned evidence object did not expose separate screenshot byte streams, so no screenshot-byte provenance is claimed. The separate ledger paraphrases applications and records exact URLs, versions, proof-unit coverage, and limitations without quoting passages.

\begin{thebibliography}{1}
\bibitem{BMPS} A. M. Botero, E. Mazzon, and L. Pille--Schneider,
\emph{Monge--Amp\`ere measures on balanced polyhedral spaces},
arXiv:2603.08664v1, submitted 9 March 2026, manuscript dated 10 March 2026.
\url{https://arxiv.org/pdf/2603.08664v1}.
\end{thebibliography}
\end{document}
END COMPLETE BODY COMPLETE CALLER GRANT A

BEGIN COMPLETE BODY CALLER GRANT A ALL HARMLESS CLARIFICATIONS
{
  "recorded_utc": "2026-10-07T12:15:08.104585+00:00",
  "independent_review_round": 187,
  "source_sha256": "49c87b02c5fd2269eaae85f4d16537d462ddf1413ab80cbefd4deb8ea6ef5aae",
  "exact_reviewed_source_preserved": true,
  "substantial_mathematical_repair": false,
  "clarifications": [
    "The intersection clause of the local-support lemma applies to PA f on a common carrying structure; the segment and Jensen clauses apply to continuous f. Every actual intersection application uses PA f.",
    "For translated cells the tangent space is span(sigma-sigma). The shorthand span(sigma) in the conical note convention applies only to cones; the main manuscript states the correct general convention.",
    "Strictness is the explicitly disclosed active-coefficient local-support convention. No claim of the source literal zero-coefficient strictness wording is made.",
    "Reviewer independently checked mathematical finite rows/counts. Historical environment/retrieval-hash/compile execution claims are provenance observations, not mathematical premises. ROOT separately reproduced finite checks/builds and exact native source compilation."
  ]
}
END COMPLETE BODY CALLER GRANT A ALL HARMLESS CLARIFICATIONS

BEGIN COMPLETE BODY COMPLETE CALLER GRANT B
\documentclass[11pt]{article}
\usepackage[margin=1in]{geometry}
\usepackage{amsmath,amssymb,amsthm}
\usepackage[T1]{fontenc}
\usepackage{hyperref}
\hypersetup{colorlinks=true,linkcolor=blue,urlcolor=blue}
\newtheorem{theorem}{Theorem}
\newtheorem{lemma}[theorem]{Lemma}
\newtheorem{corollary}[theorem]{Corollary}
\newtheorem{remark}[theorem]{Remark}
\newcommand{\R}{\mathbb R}
\newcommand{\Q}{\mathbb Q}
\newcommand{\PC}{\operatorname{PC}}
\newcommand{\relint}{\operatorname{relint}}
\newcommand{\vol}{\operatorname{vol}}
\title{Positive balancing, compact support, and a polyhedral maximum principle\\\large A supporting scope calculation for P05.1 and P05.2}
\author{Research draft}
\date{7 October 2026}
\begin{document}
\maketitle
\begin{abstract}
We give elementary proofs that a nonempty finite positive balanced rational cycle of positive dimension in one real vector space has noncompact support, and that the convex cone generated by a positive balanced fan is its linear span. The latter yields a strong maximum principle for continuous functions satisfying the rational-endpoint polyhedral Jensen inequalities. On compact connected spaces with compatible local balanced charts, these functions are constant. These statements clarify the distinction between a globally embedded compact support, a finite bounded skeleton, a toric compactification, and an abstract compact space with local charts. No regularity theorem or higher-dimensional contact classification is asserted.
\end{abstract}

\section{Exact geometric conventions}
Let $N$ be a lattice, $V=N\otimes\R$, and fix an auxiliary Euclidean inner product on $V$. A finite rational polyhedral complex $\Pi$ is pure of dimension $d$. Its tangent lattices are saturated:
\[N_\sigma=N\cap\operatorname{span}_{\R}(\sigma-\sigma).
\]
For a facet $\tau\prec\sigma$, choose an inward integral vector $n_{\sigma/\tau}$ whose class is primitive in $N_\sigma/N_\tau$. A strictly positive balanced weight $w$ satisfies
\begin{equation}\label{balance}
\sum_{\sigma\succ\tau}w_\sigma n_{\sigma/\tau}\in N_{\tau,\R}.
\end{equation}
Weights may be positive real numbers; rational weights in the fixed BMPS conventions are a special case. The definitions of finite globally embedded space, saturated lattices, inward normals and strictly positive top cycles agree with \cite[Definitions 2.1--2.4, 2.18--2.27]{BMPS}. Only definitions are imported. No source regularization or convexity theorem is a grant.

For a rational affine face $\sigma$, let $a_\sigma>0$ be the Euclidean covolume of $N_\sigma$ in its tangent space, and put $a_\tau=1$ for a zero-dimensional face. Set
\[c_\sigma=w_\sigma a_\sigma.
\]
These auxiliary weights serve an ordinary Euclidean divergence calculation. They are not a replacement for the raw polyhedral intersection weights or a Monge--Amp\`ere measure.

\begin{lemma}\label{height}
Let $\pi_\tau$ denote orthogonal projection onto $N_{\tau,\R}^{\perp}$. If $\nu_{\sigma/\tau}$ is the inward Euclidean unit conormal in the tangent space of $\sigma$, then
\[
 \pi_\tau n_{\sigma/\tau}
   =\frac{a_\sigma}{a_\tau}\nu_{\sigma/\tau},
 \qquad
 \sum_{\sigma\succ\tau}c_\sigma\nu_{\sigma/\tau}=0.
\]
\end{lemma}
\begin{proof}
The saturated rank-$d-1$ sublattice $N_\tau\subset N_\sigma$ has torsion-free rank-one quotient. A basis of $N_\tau$ followed by $n_{\sigma/\tau}$ is therefore a basis of $N_\sigma$. Its parallelotope volume is the base volume $a_\tau$ times the perpendicular height $|\pi_\tau n_{\sigma/\tau}|$. The inward sign gives the first formula. Project \eqref{balance} orthogonally and multiply by $a_\tau$ to obtain the second. Tangential changes of a primitive lift have no effect.
\end{proof}

\begin{lemma}\label{stationary}
For any compactly supported continuously differentiable ambient vector field $Y$,
\begin{equation}\label{stationarity}
 \sum_{\sigma\in\Pi(d)}c_\sigma
       \int_\sigma\operatorname{div}_{\sigma}Y\,d\vol_d=0.
\end{equation}
Here the divergence is the trace of the derivative on the affine tangent space of $\sigma$.
\end{lemma}
\begin{proof}
Apply the ordinary divergence formula to each polyhedron. For unbounded cells, truncate outside the support of $Y$; the added boundary gives zero. Each genuine facet $\tau$ contributes the integral of $Y$ paired with the outward unit conormal, which is $-\nu_{\sigma/\tau}$. Its total coefficient is zero by Lemma~\ref{height}. Lower-dimensional faces have zero facet measure. For $d=1$, the same calculation is the fundamental theorem of calculus on each edge, and the zero-dimensional facet integrals are endpoint values. This proves \eqref{stationarity}. The divergence formula itself follows by triangulation and the one-variable fundamental theorem, so it introduces no polyhedral intersection hypothesis.
\end{proof}

\section{A compact-support obstruction}
\begin{theorem}\label{noncompact}
If $\Pi$ is nonempty, finite, pure of dimension $d\geq1$, and admits strictly positive balanced top weights, then its support $|\Pi|\subset V$ is noncompact.
\end{theorem}
\begin{proof}
If the support were compact, every face would be bounded. Choose a compactly supported vector field equal to $Y(x)=x$ on a neighborhood of the support. On every top face its tangential divergence is $d$. Equation~\eqref{stationarity} would give
\[0=d\sum_{\sigma\in\Pi(d)}c_\sigma\vol_d(\sigma)>0.
\]
The sum is positive because the weights and covolumes are positive and each nonempty top polyhedron has positive relative volume. This is a contradiction.
\end{proof}

\begin{remark}\label{scope}
This theorem concerns the original support in a single $V$. It applies directly to the globally embedded finite spaces of BMPS Definition 2.4 equipped with Definition 2.27's strictly positive cycle. A union of bounded faces inside a noncompact balanced space need not be balanced at its boundary. A toric compactification has additional strata and lies outside this single-vector-space hypothesis. An abstract compact space with local integral-affine charts also lies outside that hypothesis. Consequently no assertion about these other categories follows by naming them compact supports. In particular the theorem supplies no higher-dimensional real envelope/contact classification.
\end{remark}

\section{The cone generated by a positive fan}
\begin{theorem}\label{fan}
Let $\Sigma$ be a nonempty finite rational fan, allowing common lineality, pure of dimension $d\geq1$, with strictly positive balanced weights. If $L$ is the linear span of its support, then
\[\operatorname{cone}(|\Sigma|)=L.
\]
Equivalently, no linear form is nonnegative on the entire support and positive somewhere on it.
\end{theorem}
\begin{proof}
Choose a smooth nonincreasing radial cutoff $\chi(r)$, equal to one near zero, zero for large $r$, and decreasing on a nonempty interval. For any constant vector $b\in V$, apply Lemma~\ref{stationary} to $Y(x)=b\chi(|x|)$. For $x$ in a top cone, its radial vector belongs to that cone's tangent space, and
\[\operatorname{div}_\sigma Y(x)
      =\chi'(|x|)\frac{\langle b,x\rangle}{|x|}.
\]
Polar integration on the $d$-dimensional tangent space gives
\[0=\left(\int_0^\infty\chi'(r)r^{d-1}\,dr\right)
 \sum_{\sigma\in\Sigma(d)}c_\sigma
     \int_{\sigma\cap S(V)}\langle b,\theta\rangle\,dS_{d-1}(\theta).
\]
The radial factor is finite and strictly negative, including when $d=1$, for which the spherical integral is a sum over the directions. Thus the weighted angular vector has barycenter zero.

If a linear form $\ell$ is nonnegative on the support and positive at some point, a top cone containing that point has a relatively open angular subset where $\ell>0$. Its angular measure is positive. All other angular integrals are nonnegative, and all $c_\sigma$ are positive, contradicting the zero barycenter. Hence every such $\ell$ vanishes on the support.

The cone generated by the support is a closed polyhedral cone: each of the finitely many rational cones is finitely generated, with a basis and its negatives added for any lineality. If that cone were a proper subset of $L$, finite-dimensional separation would give a linear form nonnegative on it and nonzero on $L$. It is positive somewhere on the support because the support spans $L$, a contradiction. For completeness, separation of a point from a closed convex cone follows by taking its nearest point: the vector from the outside point to the nearest point pairs nonnegatively with the cone and negatively with the outside point. This proves the equality.
\end{proof}

\begin{corollary}\label{relation}
Choose any finite set of nonzero rational vectors $v_1,\ldots,v_m$ generating all cones of $\Sigma$, including both signs for lineality. There exist positive rational numbers $\lambda_i$ with
\[\sum_{i=1}^m\lambda_i v_i=0.
\]
\end{corollary}
\begin{proof}
Theorem~\ref{fan} puts each $-v_i$ in the cone generated by the $v_j$. Its nonnegative representation can be chosen rational: eliminate dependent active columns until the remaining columns are linearly independent, then solve that rational linear system. Adding the resulting relations $v_i+\sum_j b_{ij}v_j=0$ gives the desired rational relation, with every coefficient at least one.
\end{proof}

\section{A continuous polyhedral maximum principle}
On a finite rational structure, a rational-endpoint polyhedral convex combination is an equality
\[x=\sum_i\alpha_i x_i,\qquad \alpha_i\geq0,\quad\sum_i\alpha_i=1,
\]
where the endpoints $x_i$ are rational and belong to faces $\sigma_i$ containing a face $\tau$ with $x\in\tau$. A continuous function $f$ is PC here if it satisfies the associated Jensen inequality for every such combination and every rational subdivision. These are BMPS Definitions 3.2--3.3 with continuity made an explicit hypothesis. We do not import its cited automatic-continuity theorem.

\begin{remark}\label{rational-pathology}
The printed rational endpoint definition does not ensure continuity. On $\R$ with its usual rational polyhedral structure, put $f(x)=0$ for $x\in\Q$ and $f(x)=-1$ otherwise. Every permitted endpoint has value zero, and every center has value at most zero, so every permitted PCC Jensen inequality holds. Nevertheless $f$ is discontinuous at every point. The source's sentence after Definition 3.3 asserting automatic continuity therefore requires an additional hypothesis or a change of endpoint convention. This example changes neither the definition tested nor the continuous class of the following theorem. It makes no assertion that an envelope of continuous obstacles is discontinuous.
\end{remark}

\begin{theorem}\label{maximum}
On a positive balanced finite rational polyhedral space, a continuous PC function attaining a global maximum is constant on the connected component of each maximum point. The same assertion holds for a space with local rational polyhedral charts and compatible positive balanced weights, provided the function satisfies these local Jensen inequalities. In particular every continuous PC function on a compact connected space of the latter kind is constant.
\end{theorem}
\begin{proof}
In dimension zero every connected component is a point, so the conclusion is immediate. In positive dimension first consider a rational maximum point $x\in\relint(\tau)$. Its local star consists of the cones $C_{\sigma/\tau}$ in the ambient tangent vector space, with their inherited weights. They are balanced: faces containing $\tau$ and their inward primitive normal classes are exactly the corresponding faces and normal classes of the original structure. Their tangent lattices are unchanged. Apply Corollary~\ref{relation} to nonzero rational generators $v_i$ of these cones, including both directions along $\tau$. Choose a rational $\varepsilon>0$ small enough that $z_i=x+\varepsilon v_i$ belongs to an incident face $\sigma_i\supset\tau$.

Let $y$ be any rational point of an incident face $\sigma\supset\tau$. Its displacement is in $C_{\sigma/\tau}$, so write $y-x=\sum_i a_i v_i$ with $a_i\geq0$. Choose $t$ large enough that $t\lambda_i-a_i\geq0$ for every $i$. Then
\[(y-x)+\sum_i\frac{t\lambda_i-a_i}{\varepsilon}(z_i-x)=0.
\]
After normalizing the coefficients, this expresses $x$ as a PCC of $y$ and the $z_i$, with a strictly positive coefficient at $y$. All endpoint values are at most the global maximum $M=f(x)$. Jensen's inequality forces $f(y)=M$. Rational points are dense in the incident faces, so continuity implies that the entire closed star of $\tau$ has value $M$.

For a possibly irrational maximum point $p\in\relint(\tau)$, the restriction of $f$ to $\tau$ is ordinarily convex. Indeed rational-endpoint Jensen inequalities extend to arbitrary endpoints by continuity. A convex function with a maximum at a relative interior point is constant on the whole face: for any $q\in\tau$, express $p$ as a convex combination with positive coefficient at $q$ and a second point in $\tau$ on the other side of $p$, and use the global upper bound $M$. Thus a rational point $x\in\relint(\tau)$ also has value $M$. The preceding argument makes every incident face maximal, giving a neighborhood of $p$ in the maximum set.

The maximum set is therefore open and, by continuity, closed. Its intersection with a connected component containing a maximum point is that entire component. In local charts, the same argument uses only a sufficiently small finite star and the global upper bound; every endpoint used lies in the chart. Compactness supplies a maximum on each compact connected component, proving the last assertion.
\end{proof}

\section{Consequences and limits for the envelope problems}
The compact globally embedded positive-dimensional branch is excluded by Theorem~\ref{noncompact}, independently of the reference or coefficient convention. This does not exclude abstract compact balanced spaces, and Theorem~\ref{maximum} gives a separate, explicitly continuous statement there.

For a compact connected space satisfying Theorem~\ref{maximum}, take a continuous PC reference $\gamma$ and a continuous obstacle $u$. Since $\gamma$ is constant, the envelope over \emph{continuous} PC minorants is the constant
\[\min_X(\gamma+u).
\]
If a finite bounded rational polyhedral cell decomposition compatible with the local charts is given and $\gamma,u$ have literal integral affine slopes and rational constants on a finite rational subdivision, their minimum value is rational: it is attained at a rational vertex of a cell of a common bounded subdivision. The constant envelope is consequently literal PA and has a constant decreasing regularizing sequence. In positive dimension its raw iterated-divisor measure is zero, because intersection with a constant is zero. Its contact integral is zero. These are direct finite-PA assertions and introduce no operator extension. An envelope allowing competitors without an explicit continuity hypothesis requires a separate identification of those competitors with continuous PC functions; that identification is not granted here.

In dimension zero a finite globally embedded space is a finite set of rational points. Every PCC is trivial on its singleton face. A literal PA reference and obstacle therefore have exact envelope $\gamma+u$ on each point, the raw zero-fold measure is the given weight cycle, and the contact gap is identically zero.

Theorems~\ref{noncompact} and \ref{maximum} clarify compact-category boundaries. They do not prove real-PA regularity on noncompact singular spaces, the global realization of local noncontact germs, or a necessary-and-sufficient higher-dimensional contact criterion. In particular they do not close original P05.1 or P05.2. The positive-dimensional real sector remains an original target.

\appendix
\section{Source application and reproducibility}
The sole cited primary version is \cite{BMPS}. Definitions 2.1--2.4 were read in the literal PDF text, lines 222--265. Definitions 2.18--2.27 and the full local-star Lemma 2.24 proof were read in lines 443--527; Definitions 3.2--3.3 were read in lines 880--902. The fixed source requires finite globally embedded complexes and strictly positive top cycles. Its toric compactification is a different space in additional strata. These definitions are paraphrased above; every needed geometric assertion is proved independently. No proof of its Monge--Amp\`ere extension, its orthogonality theorem, or the cited automatic-continuity result was imported. All auxiliary Euclidean choices disappear from the geometric conclusions.

This is an unreviewed supporting manuscript. Compilation and provenance hashes do not certify its mathematics. The exact saved source can be compiled twice using an existing \texttt{pdflatex}; no numerical experiment is needed for the divergence identities or Jensen argument.

\begin{thebibliography}{1}
\bibitem{BMPS} A. M. Botero, E. Mazzon, and L. Pille--Schneider,
\emph{Monge--Amp\`ere measures on balanced polyhedral spaces},
arXiv:2603.08664v1, submitted 9 March 2026.
\url{https://arxiv.org/pdf/2603.08664v1}.
\end{thebibliography}
\end{document}
END COMPLETE BODY COMPLETE CALLER GRANT B

BEGIN COMPLETE BODY CALLER GRANT B ALL HARMLESS CLARIFICATIONS
{
  "recorded_utc": "2026-10-07T12:33:48.345059+00:00",
  "independent_review_round": 188,
  "source_sha256": "796ef33eda780e65164664944d3b6daa46485ce852904d31e9424b6a5284ce01",
  "exact_reviewed_source_preserved": true,
  "substantial_mathematical_repair": false,
  "clarifications": [
    "In abstract local charts, the closed-star conclusion means its portion inside the chart; all endpoints remain inside the chart as already required.",
    "The maximum principle and compact-envelope results require continuous PC competitors. The rational-endpoint counterexample refutes automatic continuity but does not assert a discontinuous envelope.",
    "Rational constant literal-PA compact-envelope claims require the stated finite BOUNDED rational cell decomposition compatible with charts. No extended operator for arbitrary continuous functions on arbitrary abstract spaces is imported."
  ]
}
END COMPLETE BODY CALLER GRANT B ALL HARMLESS CLARIFICATIONS

BEGIN COMPLETE BODY ENTIRE UNCHANGED THIRTEEN-PAGE UNREVIEWED MANUSCRIPT
\documentclass[11pt]{article}
\usepackage[margin=1in]{geometry}
\usepackage[T1]{fontenc}
\usepackage{amsmath,amssymb,amsthm,booktabs}
\usepackage{hyperref}
\hypersetup{colorlinks=true,linkcolor=blue,urlcolor=blue}
\newtheorem{theorem}{Theorem}
\newtheorem{lemma}[theorem]{Lemma}
\newtheorem{proposition}[theorem]{Proposition}
\newtheorem{corollary}[theorem]{Corollary}
\newtheorem{remark}[theorem]{Remark}
\newtheorem{definition}[theorem]{Definition}
\newcommand{\R}{\mathbb R}
\newcommand{\Q}{\mathbb Q}
\newcommand{\Z}{\mathbb Z}
\newcommand{\PC}{\operatorname{PC}}
\newcommand{\PA}{\operatorname{PA}}
\newcommand{\PAPC}{\operatorname{PAPC}}
\newcommand{\MA}{\operatorname{MA}_{\mathrm{poly}}}
\newcommand{\relint}{\operatorname{relint}}
\newcommand{\cone}{\operatorname{cone}}
\newcommand{\spanR}{\operatorname{span}_{\R}}
\title{Continuous completion of rational-endpoint polyhedral convexity\\\large An envelope antecedent for original P05.2}
\author{Research draft}
\date{7 October 2026}
\begin{document}
\maketitle
\begin{abstract}
We retain the printed rational-endpoint definition of polyhedral convexity, including its discontinuous functions. On a finite positive balanced rational polyhedral space, every finite-valued function in that class has a unique continuous representative agreeing at every rational point and dominating it everywhere. No boundedness, continuity, or measurability premise is imposed on the original function. The representative is its upper semicontinuous hull and satisfies the corresponding inequalities even with real endpoints. Consequently, for every bounded continuous obstacle and continuous PC reference, the unrestricted printed envelope is continuous and equals the continuous-competitor envelope. An exact positive-spanning criterion characterizes rational-value continuity at the vertex of a finite rational fan. We also identify the unrestricted compact-chart envelope and a uniform-density obstruction for the unrepaired printed PC class. These results do not give real-PA regularization, a general extended Monge--Ampere operator, or the structural contact classification. Original P05.2 remains open; candidate status is false.
\end{abstract}

\section{Domain, coefficients, and the exact unresolved target}
Let $N$ be a lattice, $V=N\otimes\R$, and $X=|\Pi|\subset V$ the support of a finite rational polyhedral complex. Rational means that all affine constraints have rational coefficients; clearing denominators gives the integral-affine convention in the fixed primary version \cite{BMPS}. Put $X_\Q=X\cap(N\otimes\Q)$. Every nonempty rational face has dense rational points in its relative interior. For translated cells, use
\[N_\sigma=N\cap\spanR(\sigma-\sigma).\]
A normal $n_{\sigma/\tau}\in N_\sigma$ for a facet $\tau\prec\sigma$ projects to the primitive generator of $N_\sigma/N_\tau$ pointing into $\sigma$. A positive balanced top cycle consists of weights $w_\sigma>0$ such that
\begin{equation}\label{balance}
 \sum_{\sigma\succ\tau}w_\sigma n_{\sigma/\tau}\in N_{\tau,\R}.
\end{equation}
The literal source weights are rational. The geometric proofs also allow positive real weights; no real-weight operator extension is inferred.

A rational-endpoint polyhedral convex combination, or PCC, is
\[x=\sum_i\alpha_i x_i,\qquad \alpha_i\geq0,\quad\sum_i\alpha_i=1,\quad x_i\in X_\Q,
\]
with faces $\tau\preceq\sigma_i$ of some rational polyhedral structure on $X$ such that $x\in\tau$ and $x_i\in\sigma_i$. The center and coefficients need not be rational. Write $\PC_q(X)$ for the real-valued functions satisfying every such Jensen inequality. This notation marks the printed definition, rather than changing it. Write $\PC_c(X)=\PC_q(X)\cap C(X)$ and $\PC_q(X,\gamma)=\{q\in\PC_q(X):q-\gamma\text{ is bounded}\}$. A real-endpoint PCC uses the same face constraints but allows arbitrary endpoints in $X$.

The function equal to zero on $\Q$ and minus one elsewhere on $\R$ belongs to $\PC_q$ and is discontinuous everywhere: each permitted endpoint has value zero, and each center has value at most zero. Thus continuity of every member of $\PC_q$ is false. Our theorem concerns a dominating representative, not equality with the original function.

The class $\PA_\Z$ consists of continuous finite piecewise-affine functions with integral tangent slopes and rational constants in rational affine coordinates. The explicitly declared $\PA_\R$ allows arbitrary real affine coefficients on a finite \emph{rational} structure. Set $\PAPC_*:=\PA_*\cap\PC_q$ for $*=\Z,\R$. In each category let $\PC^{\rm reg}_*(X,\gamma)$ mean uniform decreasing limits of $\PAPC_*$ functions with bounded difference from $\gamma$. No general operator on all continuous $\PC_c$ functions is assumed.

For a continuous PC reference $\gamma$ and bounded continuous $u$, the actual printed envelope is
\begin{equation}\label{envelope}
 P_\gamma(u)(x)=\sup\{q(x):q\in\PC_q(X),\ q\leq\gamma+u,\ q\leq\gamma+C_q\text{ on }X\text{ for some }C_q\in\R\}.
\end{equation}
Every bounded obstacle in either PA coefficient category is included. The original problem requires structural necessary and sufficient conditions, all admissible obstacles, genuine membership of these envelopes in the appropriate regularizable operator domain, and the exact contact integral. We resolve the continuity antecedent of \eqref{envelope} on all finite positive balanced spaces. We do not resolve those remaining requirements.

\section{Finite cone geometry with uniform constants}
For a face $\tau\preceq\sigma$, put
\[C_{\sigma/\tau}=\{t(a-b):t\geq0,\ a\in\sigma,\ b\in\tau\}.
\]
For $z\in\relint(\tau)$ this is the tangent cone of $\sigma$ at $z$, including the lineality $N_{\tau,\R}$. This fact and the needed uniform version are proved next.

\begin{lemma}[Uniform rational star geometry]\label{geometry}
Fix a compact set $K\subset\relint(\tau)$. For every $\sigma\succeq\tau$ choose a finite rational generating list for $C_{\sigma/\tau}$, including a rational basis and its negatives for lineality. Let $v_1,\ldots,v_m$ be their union, with zero vectors removed; a generator may carry more than one incident-face assignment. There are constants $r>0$, rational $\varepsilon>0$, and $C>0$, independent of $z\in K$, with the following properties.

For all assigned pairs $(i,\sigma)$, $z+\varepsilon v_i\in\sigma$. If $y\in\sigma$, then $d=y-z\in C_{\sigma/\tau}$ and it has a representation using generators assigned to that cone,
\begin{equation}\label{representation}
 d=\sum_i a_i v_i,\qquad a_i\geq0,\qquad\sum_i a_i\leq C\|d\|.
\end{equation}
If $d$ is rational the $a_i$ may be chosen rational. Conversely, if $d\in C_{\sigma/\tau}$ and $\|d\|<r$, then $z+d\in\sigma$.
\end{lemma}
\begin{proof}
Write $\sigma$ using rational linear equations for its affine hull and inequalities $A_jx\geq b_j$. An inequality is active on all of $\tau$ precisely when it is active at any point of $\relint(\tau)$. All the other inequalities have positive slack on $K$, with a positive common minimum after taking the finite list. Thus its tangent cone consists exactly of tangent vectors satisfying $A_jd\geq0$ at the active inequalities. To verify equality with the displayed definition of $C_{\sigma/\tau}$, one inclusion follows by subtracting $b\in\tau$ from $a\in\sigma$. For the reverse inclusion choose $z\in\relint(\tau)$ and a sufficiently small $t>0$; inactive slack gives $z+td\in\sigma$ and $d=t^{-1}((z+td)-z)$. The common slack also proves the stated uniform radius $r$. Taking $\varepsilon$ positive rational and sufficiently small handles every assigned generator uniformly.

Here is an elementary justification that the cones have finite rational generating lists. A cone given by finitely many rational homogeneous inequalities has rational lineality. Mod out that lineality. In the pointed quotient, choose a rational linear form strictly positive on the cone away from zero (for instance the sum of a defining inequality list after its joint kernel has been removed). Its section at value one is a bounded rational polytope. This polytope is the convex hull of its finitely many vertices: from a point not yet a vertex, move in both directions in the kernel of its active constraints until an additional independent constraint becomes active, and recurse; boundedness supplies both endpoints and the recursion terminates. The vertices solve rational full-rank systems and hence are rational. Lifting their rays and adjoining a basis and its negatives for lineality supplies the list.

For any representation by a given list, eliminate dependent active columns. If $\sum_i b_i v_i=0$ is a nonzero relation among active columns, change its sign to have a positive entry and subtract $t b_i$ from $a_i$, where $t=\min_{b_i>0}a_i/b_i$. This preserves nonnegativity and the vector represented and removes at least one active column. Iteration leaves an independent subset. On any independent subset the unique coefficient vector is a linear inverse of its column map; consequently its $\ell^1$ norm is at most $C_T\|d\|$. There are finitely many subsets, so take their maximum for $C$. For rational $d$ the independent rational system has a rational solution, by Gaussian elimination. The zero vector uses the empty representation. This proves \eqref{representation} without a boundedness assumption on any function.
\end{proof}

\begin{definition}
The star at $\tau$ is positively spanning if the cone generated by $\bigcup_{\sigma\succeq\tau} C_{\sigma/\tau}$ is its linear span. Equivalently, for any generating list as above there are $\lambda_i\in\Q_{>0}$ with
\begin{equation}\label{relation}
 \sum_i\lambda_i v_i=0.
\end{equation}
\end{definition}
\begin{proof}[Proof of the equivalence in the definition]
A positive relation writes each $-v_i$ as a nonnegative combination of the other generators, so their cone is their span. Conversely, if the cone is the span, express each $-v_i$ as a nonnegative combination of the list. The elimination argument in Lemma~\ref{geometry} makes each representation rational. Add the resulting relations $v_i+\sum_j b_{ij}v_j=0$. Every coefficient is then rational and at least one, proving \eqref{relation}.
\end{proof}

\begin{lemma}[Positive balancing implies positive spanning]\label{balanced}
Every star of a finite positive balanced rational complex is positively spanning. The same holds for a positive balanced rational fan with common lineality.
\end{lemma}
\begin{proof}
We reconstruct the relevant geometric result from caller manuscript B rather than import a continuity theorem. The star inherits its top weights. A face $C_{\delta/\tau}$ corresponds to a face $\delta\succeq\tau$ of the original complex, its tangent lattice is $N_\delta$, and its primitive normal classes for adjacent facets are unchanged. This follows from the active-inequality description in Lemma~\ref{geometry}: tangent spaces are the original tangent spaces and inward facet signs agree. Thus the inherited star weights are strictly positive and balanced.

It remains to prove positive spanning for such a fan $\Sigma$ of dimension $d\geq1$. Choose a Euclidean inner product. Let $a_\sigma$ be the covolume of $N_\sigma$ in its tangent space and set $c_\sigma=w_\sigma a_\sigma>0$. For a facet $\delta$, the perpendicular projection of its primitive inward normal has length $a_\sigma/a_\delta$. Indeed a basis of the saturated $N_\delta$ followed by that normal is a basis of $N_\sigma$, and its parallelotope volume is base covolume times perpendicular height. Let $\nu_{\sigma/\delta}$ be the inward unit conormal. Projecting \eqref{balance} gives
\[\sum_{\sigma\succ\delta}c_\sigma\nu_{\sigma/\delta}=0.\]
The ordinary divergence formula therefore yields, for every compactly supported $C^1$ ambient vector field $Y$,
\begin{equation}\label{stationarity}
 \sum_{\sigma\in\Sigma(d)}c_\sigma\int_\sigma \operatorname{div}_\sigma Y\,d\operatorname{vol}_d=0.
\end{equation}
The outward boundary contributions are minus these unit conormals and cancel at each facet. For unbounded cones truncate beyond the support of $Y$, where the new boundary contribution is zero. Lower faces have zero facet measure. In dimension one this is the ordinary fundamental theorem on weighted edges. The divergence formula used here is elementary, obtainable by triangulating polyhedra and integrating derivatives in one variable; it is not a tropical operator.

Take $Y(x)=b\chi(\|x\|)$ for a constant vector $b$, with a smooth radial cutoff equal to one near zero, nonincreasing, zero far out, and strictly decreasing on an interval. Since $x$ lies in the tangent space of any cone containing it,
\[\operatorname{div}_\sigma Y(x)=\chi'(\|x\|)\langle b,x\rangle/\|x\|.\]
Polar integration in each $d$-dimensional tangent space turns \eqref{stationarity} into
\[0=\left(\int_0^\infty\chi'(r)r^{d-1}\,dr\right)
 \sum_{\sigma}c_\sigma\int_{\sigma\cap S(V)}\langle b,\theta\rangle\,dS_{d-1}(\theta).
\]
The first factor is strictly negative. In dimension one the angular integral is the sum over unit directions. If a linear form is nonnegative on the support and positive somewhere, it is positive on a relatively open angular subset of a top cone. That subset has positive angular measure, all other integrals are nonnegative, and every $c_\sigma$ is positive, contradicting the displayed identity. Hence every nonnegative linear form on the support vanishes on its span. The cone generated by the finite support is finitely generated and closed: for a converging sequence of represented vectors, the independent-column elimination in Lemma~\ref{geometry} gives uniformly bounded nonnegative coefficients; a subsequence with one fixed column subset converges to a representation of the limiting vector. If this cone $D$ were proper in its span, choose $y$ in that span outside $D$ and let $p$ be its nearest point in $D$. Existence follows by minimizing distance on a closed bounded portion. Differentiating the squared distance along the segment from $p$ to $z\in D$ gives $\langle p-y,z-p\rangle\geq0$. Taking $z=0,2p$ gives $\langle p-y,p\rangle=0$. Thus $\ell(z)=\langle p-y,z\rangle$ is nonnegative on $D$ while $\ell(y)=-\|p-y\|^2<0$. It is nonzero on the span and hence positive somewhere on the support, contradicting the preceding angular calculation. This proves positive spanning. Dimension zero has only the zero tangent space and needs no generators.
\end{proof}

\section{Two rational Jensen estimates and automatic rational bounds}
Fix a face $\tau$ with positively spanning star, a compact inner set $K\subset\relint(\tau)$, the geometry of Lemma~\ref{geometry}, and a positive relation \eqref{relation}. Put
\[\Lambda=\sum_i\lambda_i,\quad \lambda_{\min}=\min_i\lambda_i,\quad H=\frac{C\Lambda}{\varepsilon\lambda_{\min}},\quad
 L=\frac{C}{\varepsilon}\max\{1,\Lambda/\lambda_{\min}\}.
\]
The zero-star case is an isolated rational point and is omitted from these formulas.

\begin{lemma}[Exact transverse estimates]\label{estimates}
Let $q\in\PC_q(X)$, $z\in K\cap X_\Q$, and $y\in\sigma\cap X_\Q$ for $\sigma\succeq\tau$. Put $d=y-z$ and choose the rational representation \eqref{representation}. Assume $C\|d\|\leq\varepsilon$. All endpoints $z_i=z+\varepsilon v_i$ are rational and lie in their assigned incident faces.

If $m_0\leq q\leq M_0$ at $z,y,z_1,\ldots,z_m$, then
\begin{equation}\label{lipschitz}
 |q(y)-q(z)|\leq (M_0-m_0)L\|y-z\|.
\end{equation}
There is also a lower inequality requiring no lower bound on $q$:
\begin{equation}\label{lower}
 q(y)\geq q(z)+\sum_i b_i(q(z)-q(z_i)),\qquad
 b_i=\frac{t\lambda_i-a_i}{\varepsilon}\geq0,\quad
 t=\max_i\frac{a_i}{\lambda_i},\quad \sum_i b_i\leq H\|d\|.
\end{equation}
\end{lemma}
\begin{proof}
Write $A=\sum_i a_i$. The equality
\[y=(1-A/\varepsilon)z+\sum_i(a_i/\varepsilon)z_i\]
is a PCC with center in $\sigma$: omit indices $a_i=0$ from its endpoint list, so every remaining generator is assigned to $C_{\sigma/\tau}$ and every endpoint lies in $\sigma$. Its coefficients are nonnegative and sum to one. This constructs a valid combination and does not change the printed weak definition for other combinations with zero coefficients. Hence
\begin{equation}\label{upper}
 q(y)-q(z)\leq\sum_i\frac{a_i}{\varepsilon}(q(z_i)-q(z)).
\end{equation}
For the other direction, using the positive relation gives
\[d+\sum_i b_i\varepsilon v_i=d+t\sum_i\lambda_i v_i-\sum_i a_i v_i=0.
\]
Thus $z$ is the PCC of $y$ with unnormalized coefficient one and of the $z_i$ with coefficients $b_i$. Its center lies in $\tau$ and each endpoint lies in a face containing $\tau$, including $y\in\sigma$. Normalizing by $1+\sum b_i$ and rearranging proves \eqref{lower}. Since $t\leq C\|d\|/\lambda_{\min}$,
\[\sum_i b_i=(t\Lambda-A)/\varepsilon\leq H\|d\|.\]
Bounding the value differences in \eqref{upper} and \eqref{lower} by $M_0-m_0$ proves \eqref{lipschitz}. Every invocation has rational endpoints. No continuity of $q$ is used.
\end{proof}

\begin{lemma}[No boundedness premise is needed]\label{bounds}
If every star of $\Pi$ is positively spanning and $q:X\to\R$ belongs to $\PC_q(X)$, then its restriction to $X_\Q$ is locally bounded above and below at every point of $X$, including irrational points.
\end{lemma}
\begin{proof}
Let $p\in\relint(\tau)$ and choose a compact relative neighborhood $K\subset\relint(\tau)$ of $p$. Take the uniform constants and generators above. A sufficiently small neighborhood of $p$ meets only faces containing $\tau$: there are finitely many closed other faces, none containing $p$. Choose $z\in K\cap X_\Q$ sufficiently close to $p$, then a neighborhood $W$ of $p$ sufficiently small, so that $C\|y-z\|\leq\varepsilon$ for all $y\in W$ and every such $y$ belongs to an incident face. The single fixed finite list $z,z_i$ has finite values. Put $M=\max\{q(z),q(z_1),\ldots,q(z_m)\}$. Formula \eqref{upper} gives $q(y)\leq M$ for every rational $y\in W$. Formula \eqref{lower} gives
\[q(y)\geq q(z)-H\|y-z\|(M-q(z)).\]
The right side has a finite uniform lower bound on a smaller bounded $W$. This uses only values at the fixed rational anchor and its rational endpoints. For an isolated zero-dimensional face, take its own finite value. These cases cover $X$.
\end{proof}

\section{The completion theorem, including irrational centers and shared faces}
\begin{lemma}[Rational density in a feasible polyhedron]\label{density}
Let $D$ be a nonempty polyhedron defined by rational equations and inequalities. Every point $a\in D$ is a limit of rational points of $D$ in its minimal face. Indeed, collect all constraints active at $a$, solve their rational affine system by Gaussian elimination, and approximate the coordinates in a rational affine basis of its solution space. All inactive inequalities are strict at $a$ and remain satisfied for close approximants. This also proves density in every rational affine face.
\end{lemma}

\begin{theorem}[Continuous completion of the printed PC class]\label{completion}
Suppose every star of a finite rational complex $\Pi$ is positively spanning. For each finite-valued $q\in\PC_q(X)$ there is a unique $F\in C(X)$ agreeing with $q$ on $X_\Q$. It satisfies all real-endpoint PCC inequalities on every rational polyhedral structure, and
\begin{equation}\label{hull}
 q(x)\leq F(x),\qquad F(x)=q^*(x):=\limsup_{y\to x}q(y).
\end{equation}
In particular $F\in\PC_c(X)$. It is the least continuous majorant of $q$. No local boundedness or measurability assumption on $q$ is required. Conversely, every finite-valued function $q$ agreeing on $X_\Q$ with such an $F$ and satisfying $q\leq F$ belongs to $\PC_q(X)$.

All conclusions apply in every dimension to a finite positive balanced rational polyhedral space.
\end{theorem}
\begin{proof}
Lemma~\ref{bounds} gives local rational two-sided bounds. Fix $p\in\relint(\tau)$ and a smaller compact relative neighborhood $K$ around it. The endpoint lists for all rational $z\in K$ remain in a fixed compact neighborhood: their finitely many translations of $K$ are compact subsets of $X$. A finite cover by the neighborhoods in Lemma~\ref{bounds} provides common bounds $m_0,M_0$ on rational values in these endpoint sets and on a small neighborhood of $K$. Consequently \eqref{lipschitz}, with constants uniform in $z\in K\cap X_\Q$, applies to nearby rational $y$ in every incident face.

First take $y,z\in\relint(\tau)\cap X_\Q$. The same estimate is a local Lipschitz bound there. For any sequence of rational points tending to $p$ within $\relint(\tau)$, the values are Cauchy and their limit is independent of the sequence. This defines a continuous function $F_\tau$ on $\relint(\tau)$ and agrees with $q$ at every rational point of this relative interior. An isolated rational point uses its given value.

Next consider any rational sequence $y_n\to p$ in $X$, potentially lying in different incident faces. Choose rational $z_n\in\relint(\tau)$ with $\|z_n-p\|\leq\|y_n-p\|+1/n$. For large $n$ these belong to $K$, the $y_n$ belong to incident faces, and the estimate just proved gives
\[|q(y_n)-q(z_n)|\leq (M_0-m_0)L\|y_n-z_n\|\longrightarrow0.
\]
Thus \emph{every} rational sequence tending to $p$ has value limit $F_\tau(p)$. This proves compatibility across all shared faces and at irrational centers; it defines $F$ on $X$ by the unique rational limit.

To verify continuity in the full topology, fix $p$ and its bounds and constants. For a rational $y$ near $p$ in an incident face, let rational $z\in\relint(\tau)$ tend to $p$ in \eqref{lipschitz}. We obtain
\[|q(y)-F(p)|\leq (M_0-m_0)L\|y-p\|.
\]
For any real $p'$ sufficiently near $p$, take rational $y\to p'$ within this neighborhood, using the rational-limit property already established at $p'$. The last inequality yields
\[|F(p')-F(p)|\leq (M_0-m_0)L\|p'-p\|.
\]
This is continuity at $p$. We claim no uniform global Lipschitz constant on the noncompact space. Uniqueness follows from density of $X_\Q$.

For domination at an irrational $x\in\relint(\tau)$, choose rational simplices in this relative face containing $x$ whose diameters tend to zero. They exist by enclosing $x$ in small rational coordinate boxes lying in the relative interior and triangulating the boxes; a simplex containing $x$ is enough. Its rational vertices $r_j$ and barycentric coefficients give a PCC with center and endpoints in $\tau$. Therefore
\[q(x)\leq\sum_j\alpha_j q(r_j)=\sum_j\alpha_j F(r_j)\longrightarrow F(x).
\]
At a rational point this is equality. The same construction works in each relative face, including lower-dimensional ones.

It remains to check all PCC inequalities for $F$, with no unproved passage through irrational endpoints. Fix an arbitrary rational carrying structure and an arbitrary real-endpoint PCC $x=\sum_i\alpha_i x_i$ with its faces $\tau\preceq\sigma_i$. Discard zero-coefficient endpoints; the remaining $\alpha_i$ are strictly positive. Write the rational constraints of $\sigma_i$ as $A_ix_i\geq b_i$, including equations as pairs of inequalities, and those of $\tau$ likewise. Introduce perspective variables $t_i=\alpha_i x_i$. The constraints
\begin{equation}\label{perspective}
 \alpha_i\geq0,\quad\sum_i\alpha_i=1,\quad A_i t_i\geq b_i\alpha_i,\quad \sum_i t_i\in\tau
\end{equation}
define a rational polyhedron. The given $(\alpha_i,t_i)$ is a feasible point. Lemma~\ref{density} supplies rational feasible approximants $(\alpha_i^{(n)},t_i^{(n)})$, whose coefficients stay positive for large $n$. Hence
\[x_i^{(n)}=t_i^{(n)}/\alpha_i^{(n)}\in\sigma_i\cap X_\Q,
 \quad x^{(n)}=\sum_i t_i^{(n)}\in\tau\cap X_\Q.
\]
These are actual rational-endpoint PCCs. Applying the original inequalities and using agreement at rational points gives
\[F(x^{(n)})=q(x^{(n)})\leq\sum_i\alpha_i^{(n)}q(x_i^{(n)})
 =\sum_i\alpha_i^{(n)}F(x_i^{(n)}).
\]
Continuity and convergence of the perspective variables give the desired real-endpoint inequality. This covers every structure witnessing any PCC; it does not rely on a locality theorem for the original discontinuous class.

Since $q\leq F$ and $F$ is continuous, $q^*\leq F$. Rational sequences attain the limit $F(x)$, so $q^*\geq F$. If $G\in C(X)$ majorizes $q$, then $G\geq F$ on the dense rational set and hence everywhere, proving the least-majorant assertion. Conversely, for rational endpoints, $q(x)\leq F(x)\leq\sum_i\alpha_i F(x_i)=\sum_i\alpha_i q(x_i)$; this is exactly the printed inequality. Finally Lemma~\ref{balanced} checks positive spanning for the balanced case.
\end{proof}

\begin{proposition}[Exact criterion at the vertex of a fan]\label{fancriterion}
For the support of a finite rational fan, every finite-valued $\PC_q$ function has a rational restriction continuous at the origin if and only if
\[\cone(X)=\spanR(X).
\]
When this condition holds, each such function satisfies $|q(y)-q(0)|\leq C_q\|y\|$ for all sufficiently small rational $y\in X$. This is a criterion at the fan vertex, not a criterion for all the other stars of an unbalanced fan.
\end{proposition}
\begin{proof}
If the fan has lineality, subdivide it by a rational coordinate hyperplane arrangement in its span so that the origin is a vertex; its support and generated cone remain the same. If $\cone(X)$ is its span, take $K=\{0\}$ in Lemmas~\ref{bounds} and \ref{estimates}. The automatic rational bounds use only the star at this vertex, as does \eqref{lipschitz} with $z=0$. They give the asserted estimate without requiring properties of the other stars.

If the generated cone is proper in its span, separate it by a linear form $\ell$ nonnegative on $X$ and positive somewhere. The function
\[q(x)=\begin{cases}0,&\ell(x)=0,\\-1,&\ell(x)>0\end{cases}\]
satisfies even the real-endpoint PCC inequalities. If its center has $\ell=0$, every active endpoint has $\ell=0$; if its center has $\ell>0$, the endpoint average is at least $-1$. Some rational generator $v$ has $\ell(v)>0$. Hence $q(v/n)=-1$ at a rational sequence tending to zero while $q(0)=0$, proving necessity.
\end{proof}

\begin{remark}[A failed strengthening]\label{failed-fan}
The condition at the origin cannot replace the condition at every face in Theorem~\ref{completion}. The unbalanced fan $X=\R_{\geq0}^2\cup\R_{\leq0}^2$ generates $\R^2$, but the star at $(1,0)$ is a half-plane. A concrete finite-valued PC function is $q(x,0)=x$ for $x\geq0$, $q(x,y)=0$ for $x\geq0,y>0$, and $q(x,y)=-x$ on the negative quadrant. Here is a check for every PCC, on any carrying structure. At a negative-quadrant center, $q$ agrees with the ambient linear form $-x$, which it majorizes everywhere, proving Jensen. A positive-quadrant center with $y>0$, or the origin, has value zero and all endpoint values are nonnegative. For a center $(x,0)$ with $x>0$, any endpoint of negative second coordinate is impossible: its segment to the center, contained in its incident convex face, would enter the quadrant $x>0,y<0$ outside $X$. All endpoints therefore have nonnegative second coordinate, and the barycenter equation forces the active ones onto the horizontal axis. There $q=|x|$, giving Jensen. Its rational values jump at $(1,0)$ and cannot have a continuous representative. This diagnostic is outside the positive balanced domain and does not refute Theorem~\ref{completion}.
\end{remark}

\section{The true envelope for every bounded continuous obstacle}
\begin{theorem}[Unrestricted-envelope identification]\label{true-envelope}
Let $X$ satisfy Theorem~\ref{completion}, let $\gamma\in\PC_c(X)$, and let $u\in C_b(X)$. The envelope in \eqref{envelope} is finite, continuous, and satisfies all real-endpoint PCC inequalities. It equals the envelope over continuous PC competitors, and its upper semicontinuous regularization is itself. Moreover
\begin{equation}\label{sandwich}
 \gamma+\inf_Xu\leq P_\gamma(u)\leq\gamma+u\leq\gamma+\sup_Xu.
\end{equation}
For $u,v\in C_b(X)$, $\|P_\gamma(u)-P_\gamma(v)\|_\infty\leq\|u-v\|_\infty$.

In particular the result holds for every obstacle in $\PA_{\Z,b}$ and, separately, $\PA_{\R,b}$ on every finite positive balanced space, including arbitrary nonseparable product obstacles. Positive growth of $\gamma$ is not needed for this continuity result. No PA or regularizable membership of the envelope is asserted.
\end{theorem}
\begin{proof}
The function $\gamma+\inf_Xu$ is a competitor, proving finiteness and the lower bound in \eqref{sandwich}; the other bounds follow from the obstacle. A pointwise supremum of a nonempty family of $\PC_q$ functions with a finite upper bound is $\PC_q$: for each permitted PCC every competitor satisfies $q(x)\leq\sum_i\alpha_i q(x_i)\leq\sum_i\alpha_i P(x_i)$, and taking the supremum at $x$ proves the inequality for $P$.

Apply Theorem~\ref{completion} directly to the finite-valued $P$. Its continuous completion $F$ agrees on rational points and dominates $P$. The continuous obstacle and the upper bound $\gamma+\sup_Xu$ pass from rational points to all points, so $F\leq\gamma+u$ and $F\leq\gamma+\sup_Xu$. Thus $F$ is a competitor in the original unrestricted envelope. Maximality gives $P\geq F$, whence $P=F$ and all the stated continuity assertions.

For completeness, each original competitor $q$ also has a completion $F_q$. Since $q\leq\gamma+u$ and $q\leq\gamma+C_q$ on the dense rational set, continuity gives $F_q\leq\gamma+u$ and $F_q\leq\gamma+C_q$ globally. It is a continuous competitor dominating $q$. This proves equality with the continuous-competitor supremum directly, including its global growth constraint.

Finally set $a=\|u-v\|_\infty$. Adding $a$ to any competitor for $v$ makes it a competitor for $v+a$, and monotonicity in the obstacle gives $P_\gamma(u)\leq P_\gamma(v+a)=P_\gamma(v)+a$. Reverse $u,v$ for the other bound. Maxima, scalar additions, and these suprema preserve $\PC_q$ directly by Jensen; no PA closure assertion is involved.
\end{proof}

\section{Compact chart spaces: unrestricted competitors and a genuine raw endpoint}
The globally embedded positive-dimensional finite compact branch is empty. The proof is short: the divergence cancellation \eqref{stationarity} applies to a finite balanced complex as well as a fan. If its support were compact, choose $Y(x)=x$ near it with compact support. Each top-cell tangential divergence is $d$, giving
\[0=d\sum_\sigma w_\sigma a_\sigma\operatorname{vol}_d(\sigma)>0.
\]
This is a contradiction for $d\geq1$. An abstract compact space with local charts is a different category.

\begin{corollary}[Compact locally balanced charts]\label{compact}
Let $X$ be a compact space with locally embedded rational polyhedral charts, compatible positive balanced weights, and integral-affine lattice-isomorphism transition maps with rational translation. Assume the printed local PCC inequalities define its PC class. Then every continuous PC function is constant on each connected component. For a continuous PC reference $\gamma$ and continuous $u$, the envelope over \emph{all} printed-PC competitors is
\begin{equation}\label{compact-envelope}
 P_\gamma(u)|_D=\min_{x\in D}(\gamma(x)+u(x))
\end{equation}
on each connected component $D$.

If there is a finite bounded rational cell decomposition compatible with these charts and $\gamma,u\in\PA_\Z$, the constants in \eqref{compact-envelope} are rational and the endpoint is literal PA and literal regularizable. If $\gamma,u\in\PA_\R$, it is real PA and real regularizable. In positive dimension its raw iterated-divisor measure and its contact integral are zero. No measure is assigned here to arbitrary continuous endpoints outside these finite PA assertions.
\end{corollary}
\begin{proof}
The completion proof is local: use a small compact portion of a face in a chart and choose all generator endpoints inside it. Rational-affine chart transitions identify dense rational points on overlaps. The completions agree there and hence, by continuity, throughout the overlap. Thus they give a global continuous completion of every printed-PC competitor; the perspective argument gives all real-endpoint local inequalities.

Here is the maximum principle needed for the continuous completion. If a continuous PC function $F$ has maximum $M$ at $p$, choose a local star at the face containing $p$ and a positive relation as above. For any sufficiently close real $y$ in an incident face write $y-p=\sum_i a_i v_i$, set $t=\max_i a_i/\lambda_i$, and use endpoints $p+\varepsilon v_i$. The same normalized combination as in \eqref{lower} is a real-endpoint PCC centered at $p$, with strictly positive coefficient at $y$. Every endpoint value is at most $M$, so Jensen forces $F(y)=M$. The maximum set is therefore open as well as closed, and $F$ is constant on the component of $p$. Local polyhedral neighborhoods are locally connected, so components are open; in a compact space each component is compact and there are finitely many components. A maximum on each component proves the first assertion.

A competitor $q$ has continuous completion $F_q$ below the continuous obstacle, by dense rational comparison. On $D$ it is a constant at most the displayed minimum and majorizes $q$. Conversely the componentwise constants in \eqref{compact-envelope} are continuous PC competitors. This proves the exact unrestricted formula without applying a continuous maximum principle to $q$ itself.

On a finite bounded rational carrying decomposition, each affine obstacle attains its minimum on a cell at a vertex. Its vertices are rational and its literal values there are rational; taking finitely many such values proves rationality of the constant. In the real category the constant may be any real number. Both constants are PA in their stated category. A constant sequence, or addition of decreasing positive rational constants, is a valid decreasing uniform regularization.

For this separate chart category use the recursive raw divisor formula in each chart; the lattice and cycle compatibility identifies the primitive normal classes on overlaps. For the measured endpoint all chart coefficients vanish, so they glue to the global zero cycle without any general operator extension. The raw divisor of a constant $k$ against a balanced cycle $c$ is zero from the actual formula
\begin{equation}\label{raw}
 (k\cdot c)(\tau)=\sum_{\sigma\succ\tau}c(\sigma)k_\sigma(n_{\sigma/\tau})
 -k_\tau\left(\sum_{\sigma\succ\tau}c(\sigma)n_{\sigma/\tau}\right)=0,
\end{equation}
since every linear part is zero. Normals are the saturated primitive inward normals specified above; no additional factorial is inserted into this recursive intersection convention. The first divisor vanishes and so do all further divisors, proving the raw MA and exact contact statements for this finite PA endpoint. This does not extend the operator to general continuous functions.
\end{proof}

In dimension zero, the globally embedded finite rational space is a finite set of rational points. Every PCC is confined to a singleton face. Its exact envelope is $\gamma+u$ pointwise, and the genuine zero-fold measure is the given weighted cycle $[X]$. The gap is identically zero. These claims follow directly from the definitions.

\section{A precise density obstruction in both coefficient categories}
\begin{proposition}[Downward irrational modifications have a fixed gap]\label{gap}
Let $X$ have a positive-dimensional rational cell, and let $\gamma\in\PC_c(X)$. Define
\[q_\gamma(x)=\begin{cases}\gamma(x),&x\in X_\Q,\\\gamma(x)-1,&x\notin X_\Q.\end{cases}\]
Then $q_\gamma\in\PC_q(X)$, $q_\gamma-\gamma$ is bounded, and
\begin{equation}\label{half-gap}
 \inf_{f\in C(X)}\|f-q_\gamma\|_\infty=\frac12.
\end{equation}
Consequently neither $\PAPC_\Z(X,\gamma)$ nor $\PAPC_\R(X,\gamma)$ is uniformly dense in the entire printed class $\PC_q(X,\gamma)$, and that class cannot equal either regularizable class. This conclusion concerns unrestricted-PC density; it is not an all-obstacle endpoint nonregularizability theorem.
\end{proposition}
\begin{proof}
For any rational-endpoint PCC, $q_\gamma(x)\leq\gamma(x)\leq\sum_i\alpha_i\gamma(x_i)=\sum_i\alpha_i q_\gamma(x_i)$. Thus $q_\gamma$ is printed PC. Choose an irrational point $p$ in the relative interior of a positive-dimensional rational cell and rational points $r_n\to p$ in that cell. For a continuous $f$ with error at most $\delta$, $f(r_n)\geq\gamma(r_n)-\delta$ gives $f(p)\geq\gamma(p)-\delta$, whereas comparison at $p$ gives $f(p)\leq\gamma(p)-1+\delta$. Hence $\delta\geq1/2$. The continuous function $\gamma-1/2$ realizes error exactly $1/2$. Every PA function and every uniform limit of PA functions is continuous, so the non-density and non-equality conclusions follow in both coefficient categories.
\end{proof}

The source's Theorem 6.4 relates an all-PA-obstacle endpoint property to uniform density and equality with the entire PC class. Under the literal rational-endpoint reading, the latter two conditions have the independent obstruction in Proposition~\ref{gap}. We therefore do not import that equivalence or define endpoint regularity by equality with all printed PC functions. For the present target the precise antecedent to be checked is
\[P_\gamma(u)\in\PC^{\rm reg}_*(X,\gamma)\quad\text{for every admissible }u\in\PA_{*,b},\]
followed by a genuine operator on those endpoints and the exact contact integral. Theorem~\ref{true-envelope} does not prove that antecedent. Nor does the discontinuity of $q_\gamma$ imply discontinuity or nonregularizability of an envelope of a continuous obstacle: its completion is just $\gamma$, and the exact envelope is continuous by our theorem.

\section{What remains for the original classification}
The new theorem handles the unrestricted-competitor issue for every finite positive balanced space, in arbitrary dimension and with every bounded continuous obstacle. It includes all admissible PA obstacles in each separately fixed coefficient category. It identifies the upper semicontinuous regularization without redefining the printed endpoint convention. Its positive-spanning criterion depends only on local rational geometry; the actual reference enters the global envelope through a continuous lower competitor and the growth upper bound.

This is a completion criterion, not a contact criterion. On noncompact singular spaces it provides neither uniform global PA approximants with the prescribed reference growth nor a genuine extended MA operator at every envelope. Even a finite PA endpoint with positive raw mass need not have contact merely because the reference grows or the cycle is balanced. The accepted caller manuscript A224 gives such a strict-active-support, positive-growth $U_{3,4}$ example, with a genuine literal PA endpoint; that granted obstruction is retained as context, not claimed as new work or as pair-level real regularity. No unaccepted dossier theorem is an application dependency here.

The missing structural classification still includes the higher-dimensional real coefficient regularization/operator domain, a necessary and sufficient raw local contact condition, and its necessity and sufficiency under global endpoint realization with the actual reference and all obstacles. No theorem in this manuscript solves those requirements, and no raw MA is assigned to the merely continuous envelopes of Theorem~\ref{true-envelope}. The compact-chart conclusion is a separately named category and does not manufacture a compact embedded positive-dimensional cycle. Original P05.2 remains unresolved.

Three failed shortcuts are recorded. First, the original rational-endpoint PC functions cannot be declared continuous; only their dominating completions can. Second, positive spanning at a fan origin is not enough for all stars, as Remark~\ref{failed-fan} shows. Third, continuity of the exact envelope does not produce real-PA approximants, operator continuity, or contact; applying an operator extension on that premise would omit its domain hypothesis.

\section{Finite checks, source applications, and reproducibility}
The standard-library exact-fraction program \texttt{check\_star\_estimates.py} checks the two barycentric identities, coefficient nonnegativity, face assignments, and Jensen estimates on fixed rational finite lists for a four-ray star, the fine $U_{3,4}$ star, and a translated trivalent star with a bounded-edge truncation. For each cone it enumerates coefficients $0,1/64,\ldots,8/64$ and tests two ambient convex functions, a norm and that norm plus a linear form. All 1,035 barycentric cases and 2,070 convex-function cases passed. The respective star counts were $(36,72)$, $(972,1944)$, and $(27,54)$; maximal sums of the other coefficients in the lower combination were $3/4$, $9/4$, and $1$. These computations exhaust only the specified finite lists; the proofs above establish the continuum statements independently. Inputs, actual output, environment details, structured notes, source responses, and commands are retained in this workspace. Execution success and PDF compilation do not verify mathematical correctness.

The current primary version used for literal definitions is
\[\text{\url{https://arxiv.org/pdf/2603.08664v1}}.\]
Its abstract page currently lists only v1, submitted 9 March 2026; the manuscript date is 10 March 2026. Searches for the title, arXiv identifier, orthogonality, and a sequel found no resolving primary result in the returned results. This is a retrieval observation, not exhaustive bibliographic absence. The version-of-record BBGS article is \url{https://doi.org/10.1007/s00209-021-02869-6}. We read its endpoint definition, complete Lemma 6.1 and Theorem 6.2 proofs. They use unrestricted real endpoints; the automatic-continuity result is not imported into the printed rational-endpoint class. The geometric positive-spanning result from the accepted B225 grant is independently reconstructed in Lemma~\ref{balanced}. The full preserved caller grants and their supplied harmless clarifications are mathematical inputs, not new source retrievals.

The quote-free source ledger specifies literal URLs, versions, units read, actual applications and exclusions. Essential new claims have complete proofs here, rather than borrowed regularization, PA/PC equivalence, or operator-extension theorems. The shell PDF download failed through the existing configured proxy. No network or runtime settings were changed. Saved source artifacts are actual UTF-8 tool-response JSON, not original PDF bytes. Hashes apply only to files actually retained. No installation or resource-heavy local computation was performed; no operator-provided supervised compute facility was exposed. The requested model label was not independently selectable or verified, so no runtime model change is claimed.

Rerun with the existing tools:
\begin{verbatim}
python check_star_estimates.py
python build_artifacts.py
pdflatex -interaction=nonstopmode -halt-on-error P05.2-paper.tex
pdflatex -interaction=nonstopmode -halt-on-error P05.2-paper.tex
python record_provenance.py
\end{verbatim}
This manuscript is an unverified draft and candidate status is false.

\begin{thebibliography}{2}
\bibitem{BMPS} A. M. Botero, E. Mazzon, L. Pille--Schneider,
\emph{Monge--Ampere measures on balanced polyhedral spaces}, arXiv:2603.08664v1, submitted 9 March 2026, manuscript dated 10 March 2026.
\url{https://arxiv.org/pdf/2603.08664v1}.
\bibitem{BBGS} A. M. Botero, J. I. Burgos Gil, M. Sombra,
\emph{Convex analysis on polyhedral spaces}, Math. Z. 301 (2022), 1631--1674, version of record published 24 January 2022.
\url{https://doi.org/10.1007/s00209-021-02869-6}.
\end{thebibliography}
\end{document}
END COMPLETE BODY ENTIRE UNCHANGED THIRTEEN-PAGE UNREVIEWED MANUSCRIPT

BEGIN COMPLETE BODY ENTIRE NATIVE ARGUMENT; SAME UNREVIEWED MATHEMATICS
# Continuous completion of rational-endpoint polyhedral convexity

Unverified draft. Original P05.2 remains open; candidate=false. This file contains the complete argument, including proofs and limitations, converted from P05.2-paper.tex.

*Abstract.*

We retain the printed rational-endpoint definition of polyhedral convexity, including its discontinuous functions. On a finite positive balanced rational polyhedral space, every finite-valued function in that class has a unique continuous representative agreeing at every rational point and dominating it everywhere. No boundedness, continuity, or measurability premise is imposed on the original function. The representative is its upper semicontinuous hull and satisfies the corresponding inequalities even with real endpoints. Consequently, for every bounded continuous obstacle and continuous PC reference, the unrestricted printed envelope is continuous and equals the continuous-competitor envelope. An exact positive-spanning criterion characterizes rational-value continuity at the vertex of a finite rational fan. We also identify the unrestricted compact-chart envelope and a uniform-density obstruction for the unrepaired printed PC class. These results do not give real-PA regularization, a general extended Monge--Ampere operator, or the structural contact classification. Original P05.2 remains open; candidate status is false.

## Domain, coefficients, and the exact unresolved target

Let $N$ be a lattice, $V=N\otimes{\mathbb{R}}$, and $X=|\Pi|\subset V$ the support of a finite rational polyhedral complex. Rational means that all affine constraints have rational coefficients; clearing denominators gives the integral-affine convention in the fixed primary version [BMPS](https://arxiv.org/pdf/2603.08664v1). Put $X_{\mathbb{Q}}=X\cap(N\otimes{\mathbb{Q}})$. Every nonempty rational face has dense rational points in its relative interior. For translated cells, use

$$
N_\sigma=N\cap\operatorname{span}_{\mathbb R}(\sigma-\sigma).
$$

A normal $n_{\sigma/\tau}\in N_\sigma$ for a facet $\tau\prec\sigma$ projects to the primitive generator of $N_\sigma/N_\tau$ pointing into $\sigma$. A positive balanced top cycle consists of weights $w_\sigma>0$ such that
$$
\tag{1}
 \sum_{\sigma\succ\tau}w_\sigma n_{\sigma/\tau}\in N_{\tau,{\mathbb{R}}}.

$$
The literal source weights are rational. The geometric proofs also allow positive real weights; no real-weight operator extension is inferred.

A rational-endpoint polyhedral convex combination, or PCC, is

$$
x=\sum_i\alpha_i x_i,\qquad \alpha_i\geq0,\quad\sum_i\alpha_i=1,\quad x_i\in X_{\mathbb{Q}},

$$

with faces $\tau\preceq\sigma_i$ of some rational polyhedral structure on $X$ such that $x\in\tau$ and $x_i\in\sigma_i$. The center and coefficients need not be rational. Write $\operatorname{PC}_q(X)$ for the real-valued functions satisfying every such Jensen inequality. This notation marks the printed definition, rather than changing it. Write $\operatorname{PC}_c(X)=\operatorname{PC}_q(X)\cap C(X)$ and $\operatorname{PC}_q(X,\gamma)=\{q\in\operatorname{PC}_q(X):q-\gamma\text{ is bounded}\}$. A real-endpoint PCC uses the same face constraints but allows arbitrary endpoints in $X$.

The function equal to zero on ${\mathbb{Q}}$ and minus one elsewhere on ${\mathbb{R}}$ belongs to $\operatorname{PC}_q$ and is discontinuous everywhere: each permitted endpoint has value zero, and each center has value at most zero. Thus continuity of every member of $\operatorname{PC}_q$ is false. Our theorem concerns a dominating representative, not equality with the original function.

The class $\operatorname{PA}_{\mathbb{Z}}$ consists of continuous finite piecewise-affine functions with integral tangent slopes and rational constants in rational affine coordinates. The explicitly declared $\operatorname{PA}_{\mathbb{R}}$ allows arbitrary real affine coefficients on a finite *rational* structure. Set $\operatorname{PAPC}_*:=\operatorname{PA}_*\cap\operatorname{PC}_q$ for $*={\mathbb{Z}},{\mathbb{R}}$. In each category let $\operatorname{PC}^{\rm reg}_*(X,\gamma)$ mean uniform decreasing limits of $\operatorname{PAPC}_*$ functions with bounded difference from $\gamma$. No general operator on all continuous $\operatorname{PC}_c$ functions is assumed.

For a continuous PC reference $\gamma$ and bounded continuous $u$, the actual printed envelope is
$$
\tag{2}
 P_\gamma(u)(x)=\sup\{q(x):q\in\operatorname{PC}_q(X),\ q\leq\gamma+u,\ q\leq\gamma+C_q\text{ on }X\text{ for some }C_q\in{\mathbb{R}}\}.

$$
Every bounded obstacle in either PA coefficient category is included. The original problem requires structural necessary and sufficient conditions, all admissible obstacles, genuine membership of these envelopes in the appropriate regularizable operator domain, and the exact contact integral. We resolve the continuity antecedent of (2) on all finite positive balanced spaces. We do not resolve those remaining requirements.

## Finite cone geometry with uniform constants

For a face $\tau\preceq\sigma$, put

$$
C_{\sigma/\tau}=\{t(a-b):t\geq0,\ a\in\sigma,\ b\in\tau\}.

$$

For $z\in\operatorname{relint}(\tau)$ this is the tangent cone of $\sigma$ at $z$, including the lineality $N_{\tau,{\mathbb{R}}}$. This fact and the needed uniform version are proved next.

**Lemma 1 (Uniform rational star geometry).**

Fix a compact set $K\subset\operatorname{relint}(\tau)$. For every $\sigma\succeq\tau$ choose a finite rational generating list for $C_{\sigma/\tau}$, including a rational basis and its negatives for lineality. Let $v_1,\ldots,v_m$ be their union, with zero vectors removed; a generator may carry more than one incident-face assignment. There are constants $r>0$, rational $\varepsilon>0$, and $C>0$, independent of $z\in K$, with the following properties.

For all assigned pairs $(i,\sigma)$, $z+\varepsilon v_i\in\sigma$. If $y\in\sigma$, then $d=y-z\in C_{\sigma/\tau}$ and it has a representation using generators assigned to that cone,
$$
\tag{3}
 d=\sum_i a_i v_i,\qquad a_i\geq0,\qquad\sum_i a_i\leq C\|d\|.

$$
If $d$ is rational the $a_i$ may be chosen rational. Conversely, if $d\in C_{\sigma/\tau}$ and $\|d\|<r$, then $z+d\in\sigma$.

*Proof.*

Write $\sigma$ using rational linear equations for its affine hull and inequalities $A_jx\geq b_j$. An inequality is active on all of $\tau$ precisely when it is active at any point of $\operatorname{relint}(\tau)$. All the other inequalities have positive slack on $K$, with a positive common minimum after taking the finite list. Thus its tangent cone consists exactly of tangent vectors satisfying $A_jd\geq0$ at the active inequalities. To verify equality with the displayed definition of $C_{\sigma/\tau}$, one inclusion follows by subtracting $b\in\tau$ from $a\in\sigma$. For the reverse inclusion choose $z\in\operatorname{relint}(\tau)$ and a sufficiently small $t>0$; inactive slack gives $z+td\in\sigma$ and $d=t^{-1}((z+td)-z)$. The common slack also proves the stated uniform radius $r$. Taking $\varepsilon$ positive rational and sufficiently small handles every assigned generator uniformly.

Here is an elementary justification that the cones have finite rational generating lists. A cone given by finitely many rational homogeneous inequalities has rational lineality. Mod out that lineality. In the pointed quotient, choose a rational linear form strictly positive on the cone away from zero (for instance the sum of a defining inequality list after its joint kernel has been removed). Its section at value one is a bounded rational polytope. This polytope is the convex hull of its finitely many vertices: from a point not yet a vertex, move in both directions in the kernel of its active constraints until an additional independent constraint becomes active, and recurse; boundedness supplies both endpoints and the recursion terminates. The vertices solve rational full-rank systems and hence are rational. Lifting their rays and adjoining a basis and its negatives for lineality supplies the list.

For any representation by a given list, eliminate dependent active columns. If $\sum_i b_i v_i=0$ is a nonzero relation among active columns, change its sign to have a positive entry and subtract $t b_i$ from $a_i$, where $t=\min_{b_i>0}a_i/b_i$. This preserves nonnegativity and the vector represented and removes at least one active column. Iteration leaves an independent subset. On any independent subset the unique coefficient vector is a linear inverse of its column map; consequently its $\ell^1$ norm is at most $C_T\|d\|$. There are finitely many subsets, so take their maximum for $C$. For rational $d$ the independent rational system has a rational solution, by Gaussian elimination. The zero vector uses the empty representation. This proves (3) without a boundedness assumption on any function.

∎

**Definition 2.**

The star at $\tau$ is positively spanning if the cone generated by $\bigcup_{\sigma\succeq\tau} C_{\sigma/\tau}$ is its linear span. Equivalently, for any generating list as above there are $\lambda_i\in{\mathbb{Q}}_{>0}$ with
$$
\tag{4}
 \sum_i\lambda_i v_i=0.

$$

*Proof of the equivalence in the definition.*

A positive relation writes each $-v_i$ as a nonnegative combination of the other generators, so their cone is their span. Conversely, if the cone is the span, express each $-v_i$ as a nonnegative combination of the list. The elimination argument in Lemma 1 makes each representation rational. Add the resulting relations $v_i+\sum_j b_{ij}v_j=0$. Every coefficient is then rational and at least one, proving (4).

∎

**Lemma 3 (Positive balancing implies positive spanning).**

Every star of a finite positive balanced rational complex is positively spanning. The same holds for a positive balanced rational fan with common lineality.

*Proof.*

We reconstruct the relevant geometric result from caller manuscript B rather than import a continuity theorem. The star inherits its top weights. A face $C_{\delta/\tau}$ corresponds to a face $\delta\succeq\tau$ of the original complex, its tangent lattice is $N_\delta$, and its primitive normal classes for adjacent facets are unchanged. This follows from the active-inequality description in Lemma 1: tangent spaces are the original tangent spaces and inward facet signs agree. Thus the inherited star weights are strictly positive and balanced.

It remains to prove positive spanning for such a fan $\Sigma$ of dimension $d\geq1$. Choose a Euclidean inner product. Let $a_\sigma$ be the covolume of $N_\sigma$ in its tangent space and set $c_\sigma=w_\sigma a_\sigma>0$. For a facet $\delta$, the perpendicular projection of its primitive inward normal has length $a_\sigma/a_\delta$. Indeed a basis of the saturated $N_\delta$ followed by that normal is a basis of $N_\sigma$, and its parallelotope volume is base covolume times perpendicular height. Let $\nu_{\sigma/\delta}$ be the inward unit conormal. Projecting (1) gives

$$
\sum_{\sigma\succ\delta}c_\sigma\nu_{\sigma/\delta}=0.
$$

The ordinary divergence formula therefore yields, for every compactly supported $C^1$ ambient vector field $Y$,
$$
\tag{5}
 \sum_{\sigma\in\Sigma(d)}c_\sigma\int_\sigma \operatorname{div}_\sigma Y\,d\operatorname{vol}_d=0.

$$
The outward boundary contributions are minus these unit conormals and cancel at each facet. For unbounded cones truncate beyond the support of $Y$, where the new boundary contribution is zero. Lower faces have zero facet measure. In dimension one this is the ordinary fundamental theorem on weighted edges. The divergence formula used here is elementary, obtainable by triangulating polyhedra and integrating derivatives in one variable; it is not a tropical operator.

Take $Y(x)=b\chi(\|x\|)$ for a constant vector $b$, with a smooth radial cutoff equal to one near zero, nonincreasing, zero far out, and strictly decreasing on an interval. Since $x$ lies in the tangent space of any cone containing it,

$$
\operatorname{div}_\sigma Y(x)=\chi'(\|x\|)\langle b,x\rangle/\|x\|.
$$

Polar integration in each $d$-dimensional tangent space turns (5) into

$$
0=\left(\int_0^\infty\chi'(r)r^{d-1}\,dr\right)
 \sum_{\sigma}c_\sigma\int_{\sigma\cap S(V)}\langle b,\theta\rangle\,dS_{d-1}(\theta).

$$

The first factor is strictly negative. In dimension one the angular integral is the sum over unit directions. If a linear form is nonnegative on the support and positive somewhere, it is positive on a relatively open angular subset of a top cone. That subset has positive angular measure, all other integrals are nonnegative, and every $c_\sigma$ is positive, contradicting the displayed identity. Hence every nonnegative linear form on the support vanishes on its span. The cone generated by the finite support is finitely generated and closed: for a converging sequence of represented vectors, the independent-column elimination in Lemma 1 gives uniformly bounded nonnegative coefficients; a subsequence with one fixed column subset converges to a representation of the limiting vector. If this cone $D$ were proper in its span, choose $y$ in that span outside $D$ and let $p$ be its nearest point in $D$. Existence follows by minimizing distance on a closed bounded portion. Differentiating the squared distance along the segment from $p$ to $z\in D$ gives $\langle p-y,z-p\rangle\geq0$. Taking $z=0,2p$ gives $\langle p-y,p\rangle=0$. Thus $\ell(z)=\langle p-y,z\rangle$ is nonnegative on $D$ while $\ell(y)=-\|p-y\|^2<0$. It is nonzero on the span and hence positive somewhere on the support, contradicting the preceding angular calculation. This proves positive spanning. Dimension zero has only the zero tangent space and needs no generators.

∎

## Two rational Jensen estimates and automatic rational bounds

Fix a face $\tau$ with positively spanning star, a compact inner set $K\subset\operatorname{relint}(\tau)$, the geometry of Lemma 1, and a positive relation (4). Put

$$
\Lambda=\sum_i\lambda_i,\quad \lambda_{\min}=\min_i\lambda_i,\quad H=\frac{C\Lambda}{\varepsilon\lambda_{\min}},\quad
 L=\frac{C}{\varepsilon}\max\{1,\Lambda/\lambda_{\min}\}.

$$

The zero-star case is an isolated rational point and is omitted from these formulas.

**Lemma 4 (Exact transverse estimates).**

Let $q\in\operatorname{PC}_q(X)$, $z\in K\cap X_{\mathbb{Q}}$, and $y\in\sigma\cap X_{\mathbb{Q}}$ for $\sigma\succeq\tau$. Put $d=y-z$ and choose the rational representation (3). Assume $C\|d\|\leq\varepsilon$. All endpoints $z_i=z+\varepsilon v_i$ are rational and lie in their assigned incident faces.

If $m_0\leq q\leq M_0$ at $z,y,z_1,\ldots,z_m$, then
$$
\tag{6}
 |q(y)-q(z)|\leq (M_0-m_0)L\|y-z\|.

$$
There is also a lower inequality requiring no lower bound on $q$:
$$
\tag{7}
 q(y)\geq q(z)+\sum_i b_i(q(z)-q(z_i)),\qquad
 b_i=\frac{t\lambda_i-a_i}{\varepsilon}\geq0,\quad
 t=\max_i\frac{a_i}{\lambda_i},\quad \sum_i b_i\leq H\|d\|.

$$

*Proof.*

Write $A=\sum_i a_i$. The equality

$$
y=(1-A/\varepsilon)z+\sum_i(a_i/\varepsilon)z_i
$$

is a PCC with center in $\sigma$: omit indices $a_i=0$ from its endpoint list, so every remaining generator is assigned to $C_{\sigma/\tau}$ and every endpoint lies in $\sigma$. Its coefficients are nonnegative and sum to one. This constructs a valid combination and does not change the printed weak definition for other combinations with zero coefficients. Hence
$$
\tag{8}
 q(y)-q(z)\leq\sum_i\frac{a_i}{\varepsilon}(q(z_i)-q(z)).

$$
For the other direction, using the positive relation gives

$$
d+\sum_i b_i\varepsilon v_i=d+t\sum_i\lambda_i v_i-\sum_i a_i v_i=0.

$$

Thus $z$ is the PCC of $y$ with unnormalized coefficient one and of the $z_i$ with coefficients $b_i$. Its center lies in $\tau$ and each endpoint lies in a face containing $\tau$, including $y\in\sigma$. Normalizing by $1+\sum b_i$ and rearranging proves (7). Since $t\leq C\|d\|/\lambda_{\min}$,

$$
\sum_i b_i=(t\Lambda-A)/\varepsilon\leq H\|d\|.
$$

Bounding the value differences in (8) and (7) by $M_0-m_0$ proves (6). Every invocation has rational endpoints. No continuity of $q$ is used.

∎

**Lemma 5 (No boundedness premise is needed).**

If every star of $\Pi$ is positively spanning and $q:X\to{\mathbb{R}}$ belongs to $\operatorname{PC}_q(X)$, then its restriction to $X_{\mathbb{Q}}$ is locally bounded above and below at every point of $X$, including irrational points.

*Proof.*

Let $p\in\operatorname{relint}(\tau)$ and choose a compact relative neighborhood $K\subset\operatorname{relint}(\tau)$ of $p$. Take the uniform constants and generators above. A sufficiently small neighborhood of $p$ meets only faces containing $\tau$: there are finitely many closed other faces, none containing $p$. Choose $z\in K\cap X_{\mathbb{Q}}$ sufficiently close to $p$, then a neighborhood $W$ of $p$ sufficiently small, so that $C\|y-z\|\leq\varepsilon$ for all $y\in W$ and every such $y$ belongs to an incident face. The single fixed finite list $z,z_i$ has finite values. Put $M=\max\{q(z),q(z_1),\ldots,q(z_m)\}$. Formula (8) gives $q(y)\leq M$ for every rational $y\in W$. Formula (7) gives

$$
q(y)\geq q(z)-H\|y-z\|(M-q(z)).
$$

The right side has a finite uniform lower bound on a smaller bounded $W$. This uses only values at the fixed rational anchor and its rational endpoints. For an isolated zero-dimensional face, take its own finite value. These cases cover $X$.

∎

## The completion theorem, including irrational centers and shared faces

**Lemma 6 (Rational density in a feasible polyhedron).**

Let $D$ be a nonempty polyhedron defined by rational equations and inequalities. Every point $a\in D$ is a limit of rational points of $D$ in its minimal face. Indeed, collect all constraints active at $a$, solve their rational affine system by Gaussian elimination, and approximate the coordinates in a rational affine basis of its solution space. All inactive inequalities are strict at $a$ and remain satisfied for close approximants. This also proves density in every rational affine face.

**Theorem 7 (Continuous completion of the printed PC class).**

Suppose every star of a finite rational complex $\Pi$ is positively spanning. For each finite-valued $q\in\operatorname{PC}_q(X)$ there is a unique $F\in C(X)$ agreeing with $q$ on $X_{\mathbb{Q}}$. It satisfies all real-endpoint PCC inequalities on every rational polyhedral structure, and
$$
\tag{9}
 q(x)\leq F(x),\qquad F(x)=q^*(x):=\limsup_{y\to x}q(y).

$$
In particular $F\in\operatorname{PC}_c(X)$. It is the least continuous majorant of $q$. No local boundedness or measurability assumption on $q$ is required. Conversely, every finite-valued function $q$ agreeing on $X_{\mathbb{Q}}$ with such an $F$ and satisfying $q\leq F$ belongs to $\operatorname{PC}_q(X)$.

All conclusions apply in every dimension to a finite positive balanced rational polyhedral space.

*Proof.*

Lemma 5 gives local rational two-sided bounds. Fix $p\in\operatorname{relint}(\tau)$ and a smaller compact relative neighborhood $K$ around it. The endpoint lists for all rational $z\in K$ remain in a fixed compact neighborhood: their finitely many translations of $K$ are compact subsets of $X$. A finite cover by the neighborhoods in Lemma 5 provides common bounds $m_0,M_0$ on rational values in these endpoint sets and on a small neighborhood of $K$. Consequently (6), with constants uniform in $z\in K\cap X_{\mathbb{Q}}$, applies to nearby rational $y$ in every incident face.

First take $y,z\in\operatorname{relint}(\tau)\cap X_{\mathbb{Q}}$. The same estimate is a local Lipschitz bound there. For any sequence of rational points tending to $p$ within $\operatorname{relint}(\tau)$, the values are Cauchy and their limit is independent of the sequence. This defines a continuous function $F_\tau$ on $\operatorname{relint}(\tau)$ and agrees with $q$ at every rational point of this relative interior. An isolated rational point uses its given value.

Next consider any rational sequence $y_n\to p$ in $X$, potentially lying in different incident faces. Choose rational $z_n\in\operatorname{relint}(\tau)$ with $\|z_n-p\|\leq\|y_n-p\|+1/n$. For large $n$ these belong to $K$, the $y_n$ belong to incident faces, and the estimate just proved gives

$$
|q(y_n)-q(z_n)|\leq (M_0-m_0)L\|y_n-z_n\|\longrightarrow0.

$$

Thus *every* rational sequence tending to $p$ has value limit $F_\tau(p)$. This proves compatibility across all shared faces and at irrational centers; it defines $F$ on $X$ by the unique rational limit.

To verify continuity in the full topology, fix $p$ and its bounds and constants. For a rational $y$ near $p$ in an incident face, let rational $z\in\operatorname{relint}(\tau)$ tend to $p$ in (6). We obtain

$$
|q(y)-F(p)|\leq (M_0-m_0)L\|y-p\|.

$$

For any real $p'$ sufficiently near $p$, take rational $y\to p'$ within this neighborhood, using the rational-limit property already established at $p'$. The last inequality yields

$$
|F(p')-F(p)|\leq (M_0-m_0)L\|p'-p\|.

$$

This is continuity at $p$. We claim no uniform global Lipschitz constant on the noncompact space. Uniqueness follows from density of $X_{\mathbb{Q}}$.

For domination at an irrational $x\in\operatorname{relint}(\tau)$, choose rational simplices in this relative face containing $x$ whose diameters tend to zero. They exist by enclosing $x$ in small rational coordinate boxes lying in the relative interior and triangulating the boxes; a simplex containing $x$ is enough. Its rational vertices $r_j$ and barycentric coefficients give a PCC with center and endpoints in $\tau$. Therefore

$$
q(x)\leq\sum_j\alpha_j q(r_j)=\sum_j\alpha_j F(r_j)\longrightarrow F(x).

$$

At a rational point this is equality. The same construction works in each relative face, including lower-dimensional ones.

It remains to check all PCC inequalities for $F$, with no unproved passage through irrational endpoints. Fix an arbitrary rational carrying structure and an arbitrary real-endpoint PCC $x=\sum_i\alpha_i x_i$ with its faces $\tau\preceq\sigma_i$. Discard zero-coefficient endpoints; the remaining $\alpha_i$ are strictly positive. Write the rational constraints of $\sigma_i$ as $A_ix_i\geq b_i$, including equations as pairs of inequalities, and those of $\tau$ likewise. Introduce perspective variables $t_i=\alpha_i x_i$. The constraints
$$
\tag{10}
 \alpha_i\geq0,\quad\sum_i\alpha_i=1,\quad A_i t_i\geq b_i\alpha_i,\quad \sum_i t_i\in\tau

$$
define a rational polyhedron. The given $(\alpha_i,t_i)$ is a feasible point. Lemma 6 supplies rational feasible approximants $(\alpha_i^{(n)},t_i^{(n)})$, whose coefficients stay positive for large $n$. Hence

$$
x_i^{(n)}=t_i^{(n)}/\alpha_i^{(n)}\in\sigma_i\cap X_{\mathbb{Q}},
 \quad x^{(n)}=\sum_i t_i^{(n)}\in\tau\cap X_{\mathbb{Q}}.

$$

These are actual rational-endpoint PCCs. Applying the original inequalities and using agreement at rational points gives

$$
F(x^{(n)})=q(x^{(n)})\leq\sum_i\alpha_i^{(n)}q(x_i^{(n)})
 =\sum_i\alpha_i^{(n)}F(x_i^{(n)}).

$$

Continuity and convergence of the perspective variables give the desired real-endpoint inequality. This covers every structure witnessing any PCC; it does not rely on a locality theorem for the original discontinuous class.

Since $q\leq F$ and $F$ is continuous, $q^*\leq F$. Rational sequences attain the limit $F(x)$, so $q^*\geq F$. If $G\in C(X)$ majorizes $q$, then $G\geq F$ on the dense rational set and hence everywhere, proving the least-majorant assertion. Conversely, for rational endpoints, $q(x)\leq F(x)\leq\sum_i\alpha_i F(x_i)=\sum_i\alpha_i q(x_i)$; this is exactly the printed inequality. Finally Lemma 3 checks positive spanning for the balanced case.

∎

**Proposition 8 (Exact criterion at the vertex of a fan).**

For the support of a finite rational fan, every finite-valued $\operatorname{PC}_q$ function has a rational restriction continuous at the origin if and only if

$$
\operatorname{cone}(X)=\operatorname{span}_{\mathbb R}(X).

$$

When this condition holds, each such function satisfies $|q(y)-q(0)|\leq C_q\|y\|$ for all sufficiently small rational $y\in X$. This is a criterion at the fan vertex, not a criterion for all the other stars of an unbalanced fan.

*Proof.*

If the fan has lineality, subdivide it by a rational coordinate hyperplane arrangement in its span so that the origin is a vertex; its support and generated cone remain the same. If $\operatorname{cone}(X)$ is its span, take $K=\{0\}$ in Lemmas 5 and 4. The automatic rational bounds use only the star at this vertex, as does (6) with $z=0$. They give the asserted estimate without requiring properties of the other stars.

If the generated cone is proper in its span, separate it by a linear form $\ell$ nonnegative on $X$ and positive somewhere. The function

$$
q(x)=\begin{cases}0,&\ell(x)=0,\\-1,&\ell(x)>0\end{cases}
$$

satisfies even the real-endpoint PCC inequalities. If its center has $\ell=0$, every active endpoint has $\ell=0$; if its center has $\ell>0$, the endpoint average is at least $-1$. Some rational generator $v$ has $\ell(v)>0$. Hence $q(v/n)=-1$ at a rational sequence tending to zero while $q(0)=0$, proving necessity.

∎

**Remark 9 (A failed strengthening).**

The condition at the origin cannot replace the condition at every face in Theorem 7. The unbalanced fan $X={\mathbb{R}}_{\geq0}^2\cup{\mathbb{R}}_{\leq0}^2$ generates ${\mathbb{R}}^2$, but the star at $(1,0)$ is a half-plane. A concrete finite-valued PC function is $q(x,0)=x$ for $x\geq0$, $q(x,y)=0$ for $x\geq0,y>0$, and $q(x,y)=-x$ on the negative quadrant. Here is a check for every PCC, on any carrying structure. At a negative-quadrant center, $q$ agrees with the ambient linear form $-x$, which it majorizes everywhere, proving Jensen. A positive-quadrant center with $y>0$, or the origin, has value zero and all endpoint values are nonnegative. For a center $(x,0)$ with $x>0$, any endpoint of negative second coordinate is impossible: its segment to the center, contained in its incident convex face, would enter the quadrant $x>0,y<0$ outside $X$. All endpoints therefore have nonnegative second coordinate, and the barycenter equation forces the active ones onto the horizontal axis. There $q=|x|$, giving Jensen. Its rational values jump at $(1,0)$ and cannot have a continuous representative. This diagnostic is outside the positive balanced domain and does not refute Theorem 7.

## The true envelope for every bounded continuous obstacle

**Theorem 10 (Unrestricted-envelope identification).**

Let $X$ satisfy Theorem 7, let $\gamma\in\operatorname{PC}_c(X)$, and let $u\in C_b(X)$. The envelope in (2) is finite, continuous, and satisfies all real-endpoint PCC inequalities. It equals the envelope over continuous PC competitors, and its upper semicontinuous regularization is itself. Moreover
$$
\tag{11}
 \gamma+\inf_Xu\leq P_\gamma(u)\leq\gamma+u\leq\gamma+\sup_Xu.

$$
For $u,v\in C_b(X)$, $\|P_\gamma(u)-P_\gamma(v)\|_\infty\leq\|u-v\|_\infty$.

In particular the result holds for every obstacle in $\operatorname{PA}_{{\mathbb{Z}},b}$ and, separately, $\operatorname{PA}_{{\mathbb{R}},b}$ on every finite positive balanced space, including arbitrary nonseparable product obstacles. Positive growth of $\gamma$ is not needed for this continuity result. No PA or regularizable membership of the envelope is asserted.

*Proof.*

The function $\gamma+\inf_Xu$ is a competitor, proving finiteness and the lower bound in (11); the other bounds follow from the obstacle. A pointwise supremum of a nonempty family of $\operatorname{PC}_q$ functions with a finite upper bound is $\operatorname{PC}_q$: for each permitted PCC every competitor satisfies $q(x)\leq\sum_i\alpha_i q(x_i)\leq\sum_i\alpha_i P(x_i)$, and taking the supremum at $x$ proves the inequality for $P$.

Apply Theorem 7 directly to the finite-valued $P$. Its continuous completion $F$ agrees on rational points and dominates $P$. The continuous obstacle and the upper bound $\gamma+\sup_Xu$ pass from rational points to all points, so $F\leq\gamma+u$ and $F\leq\gamma+\sup_Xu$. Thus $F$ is a competitor in the original unrestricted envelope. Maximality gives $P\geq F$, whence $P=F$ and all the stated continuity assertions.

For completeness, each original competitor $q$ also has a completion $F_q$. Since $q\leq\gamma+u$ and $q\leq\gamma+C_q$ on the dense rational set, continuity gives $F_q\leq\gamma+u$ and $F_q\leq\gamma+C_q$ globally. It is a continuous competitor dominating $q$. This proves equality with the continuous-competitor supremum directly, including its global growth constraint.

Finally set $a=\|u-v\|_\infty$. Adding $a$ to any competitor for $v$ makes it a competitor for $v+a$, and monotonicity in the obstacle gives $P_\gamma(u)\leq P_\gamma(v+a)=P_\gamma(v)+a$. Reverse $u,v$ for the other bound. Maxima, scalar additions, and these suprema preserve $\operatorname{PC}_q$ directly by Jensen; no PA closure assertion is involved.

∎

## Compact chart spaces: unrestricted competitors and a genuine raw endpoint

The globally embedded positive-dimensional finite compact branch is empty. The proof is short: the divergence cancellation (5) applies to a finite balanced complex as well as a fan. If its support were compact, choose $Y(x)=x$ near it with compact support. Each top-cell tangential divergence is $d$, giving

$$
0=d\sum_\sigma w_\sigma a_\sigma\operatorname{vol}_d(\sigma)>0.

$$

This is a contradiction for $d\geq1$. An abstract compact space with local charts is a different category.

**Corollary 11 (Compact locally balanced charts).**

Let $X$ be a compact space with locally embedded rational polyhedral charts, compatible positive balanced weights, and integral-affine lattice-isomorphism transition maps with rational translation. Assume the printed local PCC inequalities define its PC class. Then every continuous PC function is constant on each connected component. For a continuous PC reference $\gamma$ and continuous $u$, the envelope over *all* printed-PC competitors is
$$
\tag{12}
 P_\gamma(u)|_D=\min_{x\in D}(\gamma(x)+u(x))

$$
on each connected component $D$.

If there is a finite bounded rational cell decomposition compatible with these charts and $\gamma,u\in\operatorname{PA}_{\mathbb{Z}}$, the constants in (12) are rational and the endpoint is literal PA and literal regularizable. If $\gamma,u\in\operatorname{PA}_{\mathbb{R}}$, it is real PA and real regularizable. In positive dimension its raw iterated-divisor measure and its contact integral are zero. No measure is assigned here to arbitrary continuous endpoints outside these finite PA assertions.

*Proof.*

The completion proof is local: use a small compact portion of a face in a chart and choose all generator endpoints inside it. Rational-affine chart transitions identify dense rational points on overlaps. The completions agree there and hence, by continuity, throughout the overlap. Thus they give a global continuous completion of every printed-PC competitor; the perspective argument gives all real-endpoint local inequalities.

Here is the maximum principle needed for the continuous completion. If a continuous PC function $F$ has maximum $M$ at $p$, choose a local star at the face containing $p$ and a positive relation as above. For any sufficiently close real $y$ in an incident face write $y-p=\sum_i a_i v_i$, set $t=\max_i a_i/\lambda_i$, and use endpoints $p+\varepsilon v_i$. The same normalized combination as in (7) is a real-endpoint PCC centered at $p$, with strictly positive coefficient at $y$. Every endpoint value is at most $M$, so Jensen forces $F(y)=M$. The maximum set is therefore open as well as closed, and $F$ is constant on the component of $p$. Local polyhedral neighborhoods are locally connected, so components are open; in a compact space each component is compact and there are finitely many components. A maximum on each component proves the first assertion.

A competitor $q$ has continuous completion $F_q$ below the continuous obstacle, by dense rational comparison. On $D$ it is a constant at most the displayed minimum and majorizes $q$. Conversely the componentwise constants in (12) are continuous PC competitors. This proves the exact unrestricted formula without applying a continuous maximum principle to $q$ itself.

On a finite bounded rational carrying decomposition, each affine obstacle attains its minimum on a cell at a vertex. Its vertices are rational and its literal values there are rational; taking finitely many such values proves rationality of the constant. In the real category the constant may be any real number. Both constants are PA in their stated category. A constant sequence, or addition of decreasing positive rational constants, is a valid decreasing uniform regularization.

For this separate chart category use the recursive raw divisor formula in each chart; the lattice and cycle compatibility identifies the primitive normal classes on overlaps. For the measured endpoint all chart coefficients vanish, so they glue to the global zero cycle without any general operator extension. The raw divisor of a constant $k$ against a balanced cycle $c$ is zero from the actual formula
$$
\tag{13}
 (k\cdot c)(\tau)=\sum_{\sigma\succ\tau}c(\sigma)k_\sigma(n_{\sigma/\tau})
 -k_\tau\left(\sum_{\sigma\succ\tau}c(\sigma)n_{\sigma/\tau}\right)=0,

$$
since every linear part is zero. Normals are the saturated primitive inward normals specified above; no additional factorial is inserted into this recursive intersection convention. The first divisor vanishes and so do all further divisors, proving the raw MA and exact contact statements for this finite PA endpoint. This does not extend the operator to general continuous functions.

∎

In dimension zero, the globally embedded finite rational space is a finite set of rational points. Every PCC is confined to a singleton face. Its exact envelope is $\gamma+u$ pointwise, and the genuine zero-fold measure is the given weighted cycle $[X]$. The gap is identically zero. These claims follow directly from the definitions.

## A precise density obstruction in both coefficient categories

**Proposition 12 (Downward irrational modifications have a fixed gap).**

Let $X$ have a positive-dimensional rational cell, and let $\gamma\in\operatorname{PC}_c(X)$. Define

$$
q_\gamma(x)=\begin{cases}\gamma(x),&x\in X_{\mathbb{Q}},\\\gamma(x)-1,&x\notin X_{\mathbb{Q}}.\end{cases}
$$

Then $q_\gamma\in\operatorname{PC}_q(X)$, $q_\gamma-\gamma$ is bounded, and
$$
\tag{14}
 \inf_{f\in C(X)}\|f-q_\gamma\|_\infty=\frac12.

$$
Consequently neither $\operatorname{PAPC}_{\mathbb{Z}}(X,\gamma)$ nor $\operatorname{PAPC}_{\mathbb{R}}(X,\gamma)$ is uniformly dense in the entire printed class $\operatorname{PC}_q(X,\gamma)$, and that class cannot equal either regularizable class. This conclusion concerns unrestricted-PC density; it is not an all-obstacle endpoint nonregularizability theorem.

*Proof.*

For any rational-endpoint PCC, $q_\gamma(x)\leq\gamma(x)\leq\sum_i\alpha_i\gamma(x_i)=\sum_i\alpha_i q_\gamma(x_i)$. Thus $q_\gamma$ is printed PC. Choose an irrational point $p$ in the relative interior of a positive-dimensional rational cell and rational points $r_n\to p$ in that cell. For a continuous $f$ with error at most $\delta$, $f(r_n)\geq\gamma(r_n)-\delta$ gives $f(p)\geq\gamma(p)-\delta$, whereas comparison at $p$ gives $f(p)\leq\gamma(p)-1+\delta$. Hence $\delta\geq1/2$. The continuous function $\gamma-1/2$ realizes error exactly $1/2$. Every PA function and every uniform limit of PA functions is continuous, so the non-density and non-equality conclusions follow in both coefficient categories.

∎

The source's Theorem 6.4 relates an all-PA-obstacle endpoint property to uniform density and equality with the entire PC class. Under the literal rational-endpoint reading, the latter two conditions have the independent obstruction in Proposition 12. We therefore do not import that equivalence or define endpoint regularity by equality with all printed PC functions. For the present target the precise antecedent to be checked is

$$
P_\gamma(u)\in\operatorname{PC}^{\rm reg}_*(X,\gamma)\quad\text{for every admissible }u\in\operatorname{PA}_{*,b},
$$

followed by a genuine operator on those endpoints and the exact contact integral. Theorem 10 does not prove that antecedent. Nor does the discontinuity of $q_\gamma$ imply discontinuity or nonregularizability of an envelope of a continuous obstacle: its completion is just $\gamma$, and the exact envelope is continuous by our theorem.

## What remains for the original classification

The new theorem handles the unrestricted-competitor issue for every finite positive balanced space, in arbitrary dimension and with every bounded continuous obstacle. It includes all admissible PA obstacles in each separately fixed coefficient category. It identifies the upper semicontinuous regularization without redefining the printed endpoint convention. Its positive-spanning criterion depends only on local rational geometry; the actual reference enters the global envelope through a continuous lower competitor and the growth upper bound.

This is a completion criterion, not a contact criterion. On noncompact singular spaces it provides neither uniform global PA approximants with the prescribed reference growth nor a genuine extended MA operator at every envelope. Even a finite PA endpoint with positive raw mass need not have contact merely because the reference grows or the cycle is balanced. The accepted caller manuscript A224 gives such a strict-active-support, positive-growth $U_{3,4}$ example, with a genuine literal PA endpoint; that granted obstruction is retained as context, not claimed as new work or as pair-level real regularity. No unaccepted dossier theorem is an application dependency here.

The missing structural classification still includes the higher-dimensional real coefficient regularization/operator domain, a necessary and sufficient raw local contact condition, and its necessity and sufficiency under global endpoint realization with the actual reference and all obstacles. No theorem in this manuscript solves those requirements, and no raw MA is assigned to the merely continuous envelopes of Theorem 10. The compact-chart conclusion is a separately named category and does not manufacture a compact embedded positive-dimensional cycle. Original P05.2 remains unresolved.

Three failed shortcuts are recorded. First, the original rational-endpoint PC functions cannot be declared continuous; only their dominating completions can. Second, positive spanning at a fan origin is not enough for all stars, as Remark 9 shows. Third, continuity of the exact envelope does not produce real-PA approximants, operator continuity, or contact; applying an operator extension on that premise would omit its domain hypothesis.

## Finite checks, source applications, and reproducibility

The standard-library exact-fraction program `check_star_estimates.py` checks the two barycentric identities, coefficient nonnegativity, face assignments, and Jensen estimates on fixed rational finite lists for a four-ray star, the fine $U_{3,4}$ star, and a translated trivalent star with a bounded-edge truncation. For each cone it enumerates coefficients $0,1/64,\ldots,8/64$ and tests two ambient convex functions, a norm and that norm plus a linear form. All 1,035 barycentric cases and 2,070 convex-function cases passed. The respective star counts were $(36,72)$, $(972,1944)$, and $(27,54)$; maximal sums of the other coefficients in the lower combination were $3/4$, $9/4$, and $1$. These computations exhaust only the specified finite lists; the proofs above establish the continuum statements independently. Inputs, actual output, environment details, structured notes, source responses, and commands are retained in this workspace. Execution success and PDF compilation do not verify mathematical correctness.

The current primary version used for literal definitions is

$$
\text{<https://arxiv.org/pdf/2603.08664v1>}.
$$

Its abstract page currently lists only v1, submitted 9 March 2026; the manuscript date is 10 March 2026. Searches for the title, arXiv identifier, orthogonality, and a sequel found no resolving primary result in the returned results. This is a retrieval observation, not exhaustive bibliographic absence. The version-of-record BBGS article is <https://doi.org/10.1007/s00209-021-02869-6>. We read its endpoint definition, complete Lemma 6.1 and Theorem 6.2 proofs. They use unrestricted real endpoints; the automatic-continuity result is not imported into the printed rational-endpoint class. The geometric positive-spanning result from the accepted B225 grant is independently reconstructed in Lemma 3. The full preserved caller grants and their supplied harmless clarifications are mathematical inputs, not new source retrievals.

The quote-free source ledger specifies literal URLs, versions, units read, actual applications and exclusions. Essential new claims have complete proofs here, rather than borrowed regularization, PA/PC equivalence, or operator-extension theorems. The shell PDF download failed through the existing configured proxy. No network or runtime settings were changed. Saved source artifacts are actual UTF-8 tool-response JSON, not original PDF bytes. Hashes apply only to files actually retained. No installation or resource-heavy local computation was performed; no operator-provided supervised compute facility was exposed. The requested model label was not independently selectable or verified, so no runtime model change is claimed.

Rerun with the existing tools:

“`bash
python check_star_estimates.py
python build_artifacts.py
pdflatex -interaction=nonstopmode -halt-on-error P05.2-paper.tex
pdflatex -interaction=nonstopmode -halt-on-error P05.2-paper.tex
python record_provenance.py
“`

This manuscript is an unverified draft and candidate status is false.

Primary references: [BMPS v1](https://arxiv.org/pdf/2603.08664v1); [BBGS version of record](https://doi.org/10.1007/s00209-021-02869-6).
END COMPLETE BODY ENTIRE NATIVE ARGUMENT; SAME UNREVIEWED MATHEMATICS

BEGIN COMPLETE BODY QUOTE-FREE APPLICATION LEDGER; DATA ONLY
# Quote-free source-application ledger

The mathematical arguments in the new manuscript are reconstructed. No automatic-continuity, general regularization, PA/PC equivalence, or Monge–Ampère extension theorem is imported.

| Source and literal version | Complete pertinent unit read | Application and checks | Excluded dependence |
| --- | --- | --- | --- |
| BMPS, https://arxiv.org/pdf/2603.08664v1; arXiv submitted 9 March 2026; manuscript dated 10 March 2026 | Definitions 2.1–2.4, PDF lines 222–265; definitions 2.18–2.27 and complete local-star Lemma 2.24 proof, lines 443–527 | Finite globally embedded rational complexes, saturated tangent lattices, primitive inward normal classes, positive rational balanced top weights. New paper separately proves the uniform star representation and inherited balancing. Positive real weights appear only in the independent geometry proof. | No implication from balancing to an analytic realization. No compact chart space is silently put in the globally embedded category. |
| Same BMPS v1 | Complete PA definitions 2.28–2.30, lines 529–548; divisor Definition 2.31, lines 549–562 | Separate integral-slope/rational-constant category and explicitly declared real coefficients on finite rational cells. The only new measured endpoints are componentwise constants. Their linear parts vanish, so the displayed raw divisor is zero for every prescribed primitive inward normal and weight. | No general PA positivity or balancing of divisors is needed for this constant calculation. No real extended operator is assumed. |
| Same BMPS v1 | Complete rational-endpoint PCC and PC Definitions 3.2–3.3, lines 880–898; diagnostic automatic-continuity assertion at 899–902 | Endpoints remain rational; coefficients and centers remain real. Jensen inequalities are applied to actual rational endpoints in both star estimates. General real endpoints are recovered only for the continuous completion, with the rational perspective-polyhedron proof. | The automatic-continuity claim is not imported. Original functions can retain arbitrary downward modifications away from the rational locus. |
| Same BMPS v1 | Proposition 3.22 and regularizable Definition 3.23, lines 1285–1309 | Regularizable category is declared explicitly as decreasing uniform PA approximation with bounded relative reference. The finite constant endpoint has its own constant regularizing sequence. | The purported equivalence and its compactification/Dini dependencies are not imported. No continuous noncompact endpoint is declared regularizable. |
| Same BMPS v1 | Complete Definition 6.2 and Proposition 6.3 proof, lines 3379–3424; full Theorem 6.4 proof and Definition 6.5, 3425–3441; complete orthogonality Definition 6.9, 3480–3485 | The original unrestricted envelope and one-sided global growth constraint are preserved. Supremum Jensen, nonemptiness, completion, obstacle and growth comparisons, and nonexpansiveness are independently proved. The full printed-PC density statements are tested by an explicit half-unit gap. | No Theorem 6.4 equivalence, PA approximation, or PSH closure is used. Definition 6.9's operator-domain antecedent remains separate from continuity. |
| Same BMPS v1 | Positive-at-infinity Definition 4.15, lines 2564–2568 | The new envelope-continuity theorem does not need growth positivity. The actual reference and growth constraints still occur in every competitor and are passed to the completion. | No Proposition 4.16 boundary result or Theorem 4.13 operator extension is applied or claimed fully audited. |
| BBGS, version of record, 24 January 2022; https://doi.org/10.1007/s00209-021-02869-6; primary HTML https://link.springer.com/article/10.1007/s00209-021-02869-6 | Complete Definition 5.1, HTML lines 973–991; complete Lemma 6.1 and Theorem 6.2 proofs, 1233–1282 | Diagnostic comparison only: endpoints there range over real points, and continuity depends on that convention. The new paper supplies its own finite-generator proof for the rational convention. | Neither theorem is applied. Their intersection-cycle, positivity and classical convex-closure dependencies are not promoted to grants. |
| Caller grant B225, complete accepted body and all supplied harmless clarifications, preserved from input.json | Whole supplied manuscript | Its cone-span, divergence and continuous maximum results motivated the route. Every result actually needed in the new proofs is reconstructed: saturated-covolume projection, divergence cancellation, angular barycenter, positive rational relation, and a maximum principle after real-endpoint completion. | No unrestricted envelope identification or automatic continuity is attributed to the original B225 grant. |
| Caller grant A224, complete accepted body and all supplied harmless clarifications, preserved from input.json | Whole supplied manuscript | Context only in the limitations paragraph: a valid finite PA contact obstruction exists under its explicitly disclosed strict-active-support convention. It is not claimed as a new theorem here. | No real pair-level regularity, general raw-to-extended comparison, or source zero-coefficient strictness follows. No part of the new completion proof depends on A224. |

Actual saved tool responses are in sources/*.json. Those are retained response text, not original PDF streams. The shell curl attempt failed at the existing proxy; no settings were changed. The BBGS author-hosted primary PDF URL was also opened: https://www.maia.ub.edu/~sombra/publications/Convex%20analysis/convex_polyhedral.pdf. The exact version-of-record HTML units above were used for the diagnostic convention check.

The initial web call used the wrong search key and returned an error; the corrected call used system2_search_query. A later tool response for an internal BBGS reference incorrectly resolved to BMPS. That response was not used as evidence about BBGS; literal BBGS URLs were used for the complete units saved in sources/bbgs-complete-units.json and sources/proof-diagnostics.json. Retained outputs are not normalized into fictitious successes.

Current title/identifier/orthogonality/sequel searches returned the BMPS v1 and the primary BBGS article, with no resolving later primary result found. The current arXiv submission history listed only v1. These are retrieval observations, not a proof of exhaustive literature absence.
END COMPLETE BODY QUOTE-FREE APPLICATION LEDGER; DATA ONLY

BEGIN COMPLETE BODY INTERNAL PROOF AUDIT; DATA ONLY
# Proof and domain audit

This is an internal draft audit, not independent acceptance and not a proof certificate produced by execution.

The finite rational cell geometry is proved from active inequalities and finite independent-column elimination. The common coefficient bound works with lineality because a basis and its negatives are included. The same generator endpoint radius is uniform over a compact subset of a relative-face interior.

Positive balancing is applied only after saturated lattices, primitive inward normal classes and positive top weights are specified. Its conversion to Euclidean conormal cancellation uses covolume ratios, not an MA normalization. The angular divergence argument and finite-cone separation reconstruct the positive-spanning result. Auxiliary Euclidean weights are never substituted for raw polyhedral intersection weights.

Both star estimates use actual rational endpoints. In the upper combination all zero a_i terms are omitted so its endpoint faces contain the center face. In the lower combination all endpoints are assigned to incident faces containing the original face, and its y coefficient is strictly positive. This does not redefine weak PC or source zero-coefficient strictness.

The automatic-bounds proof uses a fixed rational anchor chosen near any possibly irrational center, finite endpoint values, and both displayed combinations. It does not assume local boundedness of the original function. Later common bounds cover compact endpoint sets, not arbitrary unbounded regions.

The completion proof first handles rational values within each relative face, then arbitrary rational approaches through incident faces. It proves continuity at every real point by the resulting local estimate, and separately proves domination of original irrational values by shrinking rational simplices. It does not identify q itself with its completion.

The real-endpoint PCC limit uses a rational polyhedron in perspective variables, exact preservation of face constraints, rational density in the active face, and positivity of the retained coefficients. It handles every rational structure witnessing a PCC, with no imported locality theorem for discontinuous functions.

The envelope is a finite printed-PC supremum, bounded below by gamma+inf(u) and above by the continuous obstacle and a uniform growth upper bound. Its completion is a valid original competitor, forcing equality. Every original competitor's own growth bound also passes to its completion. This is all-obstacle continuity for every bounded continuous u, not all-obstacle PA regularization.

The compact extension names a separate category: locally embedded charts with integral-affine lattice isomorphisms and rational translations, compatible positive cycles, and a finite bounded rational decomposition for finite PA assertions. Only the componentwise constant finite PA endpoint is measured; its first raw divisor is exactly zero in every chart, so it glues and iterates to zero. No general operator on arbitrary continuous functions is used.

The entire-class half-unit approximation obstruction is independent of endpoint regularity: q_gamma agrees with gamma on rational points and drops by one elsewhere. It belongs to printed PC but has uniform distance exactly 1/2 from all continuous functions. It does not identify an admissible continuous obstacle with a bad endpoint.

The origin-only positive-span strengthening was rejected. The unbalanced two-quadrant fan has full generated span at zero and a half-plane star at a nonzero boundary point; its explicit PC rational values can jump there. The final vertex criterion is only about rational-value continuity at the fan origin.

Unresolved original axes: structural necessary and sufficient contact conditions in arbitrary dimension; global PA approximation in each fixed coefficient category at every admissible obstacle envelope; a genuine extended MA operator in those domains; and reference-compatible global realization of local contact obstructions or sufficiency. The paper makes none of these missing premises automatic and keeps candidate=false.
END COMPLETE BODY INTERNAL PROOF AUDIT; DATA ONLY

