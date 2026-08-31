# Positive closed currents of bidegree (0,0): qualified assembly and local extension

Date: 1 September 2026. Research author: /root.

Status: NEW assembled research candidate, not a live theorem and not production Rethlas verified. The frozen projective endpoint note was an implication with explicit premises. This sibling supplies the qualified representation import, states the resulting candidate without that premise, and proves two local extensions. Its whole dependency assembly and its new extension arguments require their own independent review. The separate acceptance of individual ingredients is not an acceptance of this manuscript. No priority claim or open-problem retirement is made.

## 1. Proposed statements and the precise research boundary

Let K be a complete discretely valued non-Archimedean field with residue field k of characteristic zero. Its valuation ring is R, pi is a uniformizer, and ell=-log|pi|>0. All analytic spaces, currents, moment maps, and compact supports are over this SAME K.

The main proposed statement is the following. Let Z be a good separated strict boundaryless quasi-smooth K-analytic space, pure of dimension n>=2. On every nonempty connected ordinary open subset W of Z, each positive ordinary CLD current T of bidegree (0,0) satisfying

    d'T=0,   d''T=0

is a unique nonnegative constant multiple of the canonical integration current:

    T=c delta_W,   c>=0.                                      (1.1)

Here and below d' and d'' denote the two ordinary CLD current differentials; in eventual TeX they are written with upright differential d. The word ordinary always refers to the topology and smooth-form structure used for these currents, not merely a formal or G-open cover. No global compactness, paracompactness, algebraizability, or projectivity of Z is proposed as a hypothesis.

We distinguish three proof stages:

1. W is an ordinary open subset of the analytification of a smooth connected PROJECTIVE K-variety. The frozen A/B/C/L/O/Q arguments plus the qualified representation proof below give the proposed result.
2. The projectivity requirement is removed for smooth separated algebraic K-varieties by compactifying small affine algebraic neighborhoods, keeping the given current on the same ordinary open set.
3. A strict quasi-smooth analytic germ is replaced by an ORDINARY open algebraic germ through formal algebraization and the interior theorem. This is not a finite covering, alteration, scalar extension, or pullback of an arbitrary current.

The new conclusions are research candidates until the exact assembled argument is reviewed and the required production gate is met. In particular the already frozen C audit does NOT certify stages 2 or 3.

The immediate proposed Bedford--Taylor consequence concerns only currents of bidegree (0,0): on every ordinary open set U, for continuous psh u and v with equal curvature currents,

    d'd''[u]=d'd''[v],

one has

    d'd''(uT)=d'd''(vT).                                    (1.2)

It does not assert the same for an arbitrary positive closed current of positive bidegree. Thus even acceptance of this entire candidate would not retire the full higher-dimensional P21.3 atom, which includes every 0<=p<=n-1 and singular analytic spaces.

## 2. What is imported, and what is not

The exact file identities are recorded in INPUT_PINS.json when this note is frozen. Abbreviations name specific proof files, not new conventional theorem names.

| Input | Mathematical content used | Dependency boundary |
| --- | --- | --- |
| R | Explicit source-cell coefficient formula, proved in Section 3 below from the CLD source interfaces and the frozen representation proof | Does not assume canonical coefficient propagation, L, O, Q, A, B, or C; does not infer local affine separation |
| L, Sections 2--6 | Finite flat projection of the actual multiplicity hypersurface, proper tropical projection, canonical multiplicity and residue-field degree, one source over independent Gauss radii | Banach division and actual finite-fibre algebra; independent of R; L Section 7 is not needed as a black box |
| O, Sections 2--9 | Whole-model-tube geometry, ordinary-open all-source collars at an independent normal point, compact principal-divisor tests and residual degree factorization | Uses geometric L Sections 2--5; not R, Q, or the whole-tube current theorem of the older V packet |
| Q | Comparison on the FULL inverse image of any connected open target, including arbitrary compact source multipliers | Uses geometric L and R directly; no extension of T to the unreduced whole tube |
| A | Saturated ordinary neighborhoods and actual original-model ample-cut augmentations | BFJ model theory, original-field Bertini and connectedness; geometric part independent of currents |
| B, Sections 2--8 | Stratum incidence and finite controlled chamber chains, allowing a non-pure original skeleton | A's actual geometric modifications; no current premise |
| B, Section 9 | Equality of canonical-normalized coefficients along those chains | O and Q, hence L and R; includes omitted-normal determinant and residue degrees |
| C | Same-X endpoint capture, one identical compact source test, all-moment comparison and all-compact-test coverage | Geometric A/B and the stated L/O/Q/R interfaces |

This table is a directed acyclic dependency scheme: R and geometric L are proved first; O does not use R; Q uses R and geometric L; current B uses O and Q; C then compares the arbitrary original moments. O Section 2 explicitly proves the completed-ring geometry recalled from V. No assertion about a current on the entire V-domain is used. The whole-current conclusion of C is not an input to any earlier row.

The old source-representation statement ends with terminology referring to CLD Definition 7.5.1. Its opening has a local-affine-separation hypothesis stronger than the local differential separation supplied for our analytic spaces. We import ONLY the explicit formula, Radon-measure conclusion and glued calibration actually proved. We do not invoke a subsequent skeletal-current theorem whose other hypotheses have not been checked. This resolves the terminology issue without asserting an implication between the two separation conditions or editing the frozen statement.

## 3. The qualified source representation, with proof

The following proof works over every complete NONTRIVIALLY valued K, not only the discretely valued field of Section 1. Let V be good, separated, paracompact and boundaryless, pure of dimension n>=1, and let F:V->E=R^m be an actual ordinary tropical chart defined on all of V. Let T be positive of bidegree (0,0), separately closed. Write S for the maximal-variation locus of F.

There is a locally finite compact-cell decomposition of S such that F is affine-injective on each cell. After fixing affine coordinates t_C on the affine span of each top cell image and the interleaved positive form eta_C, there are finite b_C>=0 with

    <T,rho F^*alpha>
      = sum_C b_C integral_(F(C))
          (rho composed with (F|C)^(-1)) a_C dt_C,            (3.1)

where alpha restricts to a_C eta_C, rho is ANY ordinary smooth compact source multiplier, and the sum ranges over top-dimensional cells and is finite on its source support. There is no coefficient measure remaining on the lower-dimensional cells. The symbol a_C in this formula is a density function; later we denote the canonical CONSTANT coefficient by m_C to avoid confusing the two.

### 3.1. The source decomposition and coefficient measures

Good separated analytic spaces are locally holomorphically separated, hence locally differentially separated. The ordinary compact cutoffs and smooth density used below follow from CLD 15.2.2--15.2.7. No affine separation is claimed.

The analytic PL structure is G-tropical vertebrated (CLD 12.9.5), and pure dimension gives the tropical-space structure (15.7.1). CLD 5.2.5 makes S closed and pure n-dimensional, with F a piecewise immersion on S. Closedness in paracompact Hausdorff V makes S paracompact. Subordinate a locally finite compact-cell decomposition to compact PL domains on which F is an affine embedding (2.2.12 and 2.2.15). This gives the stated injective cells, not an assumption that V itself is compact.

For every smooth top form omega, positivity and the local order-zero bound give a Radon coefficient measure mu_omega characterized by

    integral rho d mu_omega = <T,rho omega>.                  (3.2)

For positive omega it is positive. For arbitrary omega, pass locally to its symmetric part and express that part as a difference of positive forms on the compact coefficient range; the positive cone has an interior element in the symmetric ambient space (CLD 1.2.13). This does NOT say that strongly positive ambient forms span every intermediate symmetric bidegree. CLD 7.2.8--7.2.11 and smooth density give the signed measures and their agreement on overlaps. Thus we are not treating T itself as a scalar measure on V.

An F-tropical form with max(p,q)=n is strongly supported on S. Wedge products with arbitrary smooth forms and both differentials preserve strong support; restriction to S detects zero for such forms (CLD 5.3.1, 5.3.4 and 5.3.6). An F-based top form therefore vanishes as a germ off S, and its coefficient measure is supported on S. This says nothing about tests based on an unrelated chart.

### 3.2. Lower cells are negligible for every required chart

Let B be the union of the lower-dimensional cells. Local finiteness makes B closed. It is a PL subset of S and therefore of the ambient G-tropical space. For EVERY compact analytic domain A in V and EVERY G-tropical chart H on A, CLD 3.2.8(c)--(d) makes B intersect A a compact PL set of dimension at most n-1, and makes H restrict to a PL map on it. Its image is consequently a finite union of polyhedra of dimension at most n-1. This verifies tropical Hausdorff n-negligibility in the precise all-chart sense of 16.8.3.

CLD 16.8.5 applies to the original positive closed T of bidimension (n,n), since V is boundaryless and the valuation is nontrivial. All its top coefficient measures give B zero mass. Applying the statement to the local positive decompositions above gives zero TOTAL VARIATION on B for signed coefficients. Checking just F(B) would not suffice, and is not the argument.

### 3.3. Localize the source without introducing a closedness error

Fix x in the interior of one top cell C. This interior is open in S. Choose an ordinary neighborhood V_x with S intersect V_x contained in that interior, so F is injective on the whole local source skeleton. Choose a compact smooth cutoff 0<=chi<=1 supported in V_x and equal to one on a neighborhood W_0 of x. Set

    D=supp(d'chi) union supp(d''chi).

The compact set D intersect S does not contain x, and injectivity implies F(x) is not in its image. A sufficiently small Euclidean ball O about F(x) avoids that compact image and has

    Q=O intersect L_C contained in F(S intersect W_0).

Use the same Euclidean structure to choose the ORTHOGONAL affine projection pi:E->L_C. In particular pi(O) is contained in Q, so subsequent coefficient functions are defined where used.

The compactly supported current chi T has pushforward R_0=F_*(chi T) by CLD 7.1.10--7.1.11. For a target primitive beta of type (n-1,n), compactly supported in O, closedness gives

    0=<T,d'(chi F^*beta)>
      =<T,d'chi wedge F^*beta>+<R_0,d'beta>.

The first form vanishes as a germ everywhere: off D its first factor vanishes; off S its second factor vanishes by strong support; on D intersect S the target support is avoided. Hence R_0 is d'-closed on O. The analogous calculation with type (n,n-1) gives d''-closedness. No assertion says that chi T is closed on all of V_x.

### 3.4. Tangentiality and the scalar Euclidean measure

If a target top form alpha restricts to zero on Q, then chi F^*alpha is strongly supported on S and restricts to zero there. It vanishes as a form. Thus R_0 on O factors through restriction to Q; normal coefficients or derivatives are not left over merely because the support lies in L_C.

A compact top form on Q extends to O using pi and a transverse compact cutoff. Tangentiality makes the answer independent of extension. A nonnegative scalar times the positive coordinate top form eta has a positive such extension. The resulting functional is a positive Radon measure nu on Q. Extend coordinate-deleted primitives in the same way. Restriction commutes with d', so closedness yields

    integral partial_i h d nu=0

for every compact smooth h and each affine coordinate. Convolve on relatively compact Euclidean balls. Each mollified density has zero gradient and is constant on a smaller ball. A fixed unit-integral test makes these constants converge; distributional convergence gives nu=b dt there. Overlaps and connectedness of Q give a single finite b>=0 on Q. This is ordinary Euclidean convolution, not convolution on the analytic space or a singular tropical support.

### 3.5. Recover an individual SOURCE measure

Let theta=F^*pi^*eta. Its coefficient measure is supported on S intersect V_x, and

    F_*(chi mu_theta)|Q=b dt.

Put H=S intersect V_x intersect F^(-1)(Q). By the defining inclusion for Q, each point of H has the same F-image as a point of S intersect W_0. Local injectivity forces them to be the same point. Thus H is contained in W_0, chi=1 there, and F|H is a homeomorphism onto Q. Pulling the pushforward equality back through this homeomorphism gives equality of source Radon measures on H, not just their target images.

For omega=F^*alpha with alpha|Q=a eta, strong-support detection gives

    omega=(a composed with pi composed with F) theta

on V_x intersect F^(-1)(O). Orthogonality of pi supplies the domain check. Its source measure is therefore the corresponding density times the recovered measure. This equality can be integrated against every continuous restriction rho|H, in particular every compact smooth SOURCE multiplier. It does not require rho to factor through F on V_x.

Keep the cell coordinates fixed while varying x. On a nonempty overlap the same source measure is represented by the same reference Lebesgue measure, whose open subsets have positive mass. The constants agree. Connectedness of the cell interior gives one b_C.

### 3.6. Assemble and compare with canonical integration

The cell-side measures are Radon locally: only finitely many compact cells meet a compact support, and smooth coefficients are bounded there. They agree with the coefficient measures away from B, vanish off S, and both have zero mass on B. This proves (3.1) everywhere. If the target form is defined only on a neighborhood of F(V), a cutoff equal to one near F(supp rho) reduces its single evaluation to an ambient form without changing the formula.

Constant top-cell volume calibrations glue as in CLD Example 4.5.2; lower faces carry no n-calibration data. This explains the explicit description identity without adding local affine separation to the hypotheses.

Refine to convenient cells for the analytic calibration when needed. The canonical integration current uses the same form of (3.1), with its positive constant calibration coefficient m_C on each top cell. The canonical finite-degree construction is CLD 14.1--14.4; on a boundaryless source the relevant g-cells are convenient (14.1.4(b)). Refinement restricts the already constant b_C unchanged. The ratios b_C/m_C are therefore defined. Nothing in Section 3 identifies ratios on different cells: that is precisely the role of the projective comparison.

## 4. Discharging the projective implication

Assume now the field hypotheses of Section 1 and let X be smooth connected projective over K. Fix a nonempty connected ordinary open W in X^an and T as in (1.1). We check each domain before using Section 3.

The complete coordinate-tube domains in L and O are good, separated, boundaryless and pure-dimensional. L gives a proper tropical projection to an ordinary Euclidean open. A countable compact exhaustion of that open pulls back to a countable compact exhaustion of its full inverse image. The same is true after the connected target-open restriction in Q. These domains are locally compact Hausdorff and sigma-compact, hence paracompact. Their moments are analytic units on the ENTIRE chosen ordinary domain. Section 3 therefore applies exactly there, without a current extension and without a stronger separation premise.

For arbitrary local ordinary moments used to describe compact tests, choose domains {chi>0} with chi a nonnegative compact ordinary cutoff inside the given moment neighborhood. Each is the union of its compact superlevels {chi>=1/j}, and has all other hypotheses of Section 3 by ordinary restriction. This is how C Section 9 satisfies paracompactness; we do not assert it for every arbitrary open U or for W itself. Rational replacement of finitely many moment coordinates is exact at the level of their absolute values on a sufficiently small ordinary neighborhood, as proved in C.

Now apply geometric L, O and Q with the representation established in Section 3. At a maximal model stratum with multiplicities N_0,...,N_n and residue degree d_p, Q gives one normalized coefficient b_p/(N_0 d_p) on every full connected target-open piece. O compares the collar coefficients along a WHOLE proper residual curve by compact principal-divisor tests supported inside W: lambda(p)=c_C d_p. Thus two chambers incident to that curve have the same ratio c_C/N_0 when the omitted normal is fixed. B Section 9 checks the affine determinant when changing the omitted normal; its absolute determinant factor in the coefficient is N_j/N_0, and the canonical coefficient changes from N_0 d_p to N_j d_p. Hence the ratio is independent of this choice. This is not an ordinary count of geometric sheets or a deletion of residue degrees.

A and B construct finite such chamber chains in a saturated neighborhood of a connecting path, on actual higher models of X. They preserve the full endpoint tubes and proper curve witnesses. The boundary indexing qualification of their independent audit is used: components are components of EACH restricted divisor, not connected components of the crossing union.

C Sections 2--5 supply the endpoint interface for any chosen top cell of any rational moment. Choose an independent point, extend the selected rational logarithms locally by global model functions from vertical ideals, and take a common SNC determination. Independence forces the SAME point into a maximal chamber. On an ordinary neighborhood, the original selected moment and the model moment differ by an invertible affine matrix. C Section 7 constructs one compact positive source test on which both descriptions agree, including the squared determinant factor for the two form blocks. Its canonical integral is positive, so it identifies the original ratio b_C/m_C with the model ratio. The finite chain compares any two such ratios, even from different moments with disjoint domains.

Finally C Section 9's finite compact-source partition expresses every ordinary compact top-form test as a finite sum of rational-moment tests on the paracompact domains checked above. Section 3 now gives their actual source formulas and excludes the lower-cell residual, rather than leaving either as a hypothesis. All top ratios have the same value c by the preceding comparison. The canonical formula for those identical tests therefore gives (1.1) on all compact tests.

A nonzero positive reference test exists by A/B's augmentation of a positive vertex in a saturation of any point of W, followed by the positive local calibration of L. Thus c is finite, nonnegative and unique. This proves the projective statement as an ASSEMBLED CANDIDATE from the supplied proofs. Verification of the assembly is a separate obligation from the already frozen conditional C audit.

## 5. Removing projectivity for algebraic spaces in this argument

Let Y be a smooth separated K-variety, pure of dimension n>=2; projectivity or properness of Y is not required. Every point of Y has an affine algebraic neighborhood U. After splitting regular components, take U integral. Embed U as a closed subscheme of affine space and take its integral projective closure P. Then U is an open subscheme of P and is contained in P's regular locus.

In characteristic zero, resolution gives a projective birational morphism P'->P with P' regular, isomorphic over P's regular locus. The precise external resolution input is Temkin, math/0703678v2, Theorem 1.1 together with the definition in its introduction: resolution is a blowup whose center avoids the regular locus. Hence U embeds as the SAME open subscheme of P'. Projectivity of the blowup makes P' projective over K; regular finite type over the perfect field K is smooth. Taking the integral component containing U gives a smooth connected projective compactification of U. We do not claim that an arbitrary smooth nonquasiprojective Y itself has a projective compactification.

Given a point x of an ordinary open W in Y^an, choose a connected ordinary neighborhood H contained in W intersect U^an. Such neighborhoods exist by local path connectedness. Through the open immersion just constructed, H is the same ordinary open subset of (P')^an. Restrict the given T to H and apply the projective statement there. This uses no current on the rest of (P')^an and no pullback through the resolution over its exceptional locus. Canonical integration and the ordinary form structure agree on this identified open set. Thus T|H=c_H delta_H.

If two such neighborhoods overlap, their constants agree. Indeed a nonempty overlap contains a smaller connected ordinary open, where the projective argument supplies a positive compact test of nonzero canonical mass; evaluation on that test identifies the two constants. Consequently these constants define a locally constant nonnegative function on W. It is constant when W is connected. Equality of currents glues on ordinary opens, or follows by a finite smooth partition of any compact test support. This proves (1.1) for all smooth separated algebraic Y, with no extension of T across a compactification boundary.

## 6. An ordinary-local algebraization argument

This section supplies the new analytic extension, not just a proposal to use an alteration. Let Z satisfy Section 1 and x belong to an arbitrary ordinary neighborhood W. Goodness, strictness and boundarylessness allow a strict affinoid neighborhood D of x contained in W with x in its intrinsic analytic interior Int(D). Equivalently, use the relative interior of D in Z and the composition rule, since Z has no boundary. The standard interior facts used here are stated in Temkin, 1010.2235v2, 3.4.2.3 and 4.2.4.1--4.2.4.3. The same facts identify the relative interior of an analytic domain embedding with its topological interior.

Write D=M(B). Choose a pi-torsion-free topologically finite type R-algebra C with C[1/pi]=B, by a strict affinoid presentation and contraction of its defining ideal to R{T_1,...,T_s}. This is an admissible affine formal model. The algebra B is regular because D is quasi-smooth; K has characteristic zero. Thus Spf(C) is rig-regular. Apply Temkin, math/0703678v2, Proposition 3.3.1 with its dense subfield L taken to be K itself. Since R is complete henselian, its proof gives a finite type R-algebra A with pi-adic completion isomorphic to C. This step changes neither K nor the analytic space D.

The generic fibre of that formal completion is the analytic domain D inside (Spec A[1/pi])^an. More explicitly, choose algebraic generators a_1,...,a_s of A over R and its presentation R[T]/I. Completion is R{T}/I R{T}; after inverting pi the resulting affinoid algebra is K{T}/I K{T}. Thus D is the closed unit-polydisc domain |a_i|<=1 in the algebraic analytification, with its actual analytic structure, not merely an injection on points. This is also the affine generic-fibre construction of Temkin 5.2.2.1.

Put Y=Spec A[1/pi]. The image of x lies in the TOPOLOGICAL interior of this domain in Y^an: analytifications are boundaryless, Int(D/Y^an)=Int(D), and the domain-interior theorem identifies the former with topological interior. These statements are checked by the composition rule for affinoid interiors and its local version, not inferred from formal Zariski openness. Hence an ordinary neighborhood of x in Z is isomorphic to an ordinary open subset H of Y^an.

Shrink to a connected such H if necessary. On H, quasi-smoothness of D means H is smooth. It lies in the analytification of the algebraic smooth locus Y_sm. One can check this locally by the same polynomial Jacobian criterion before and after analytification: the ideal describing the nonsmooth locus pulls back to that describing the nonsmooth analytic locus. Equivalently use the usual local smooth-locus compatibility of analytification. H meets only components of the same dimension n; shrink inside that open-and-closed dimension stratum of Y_sm.

Section 5 applies on this smooth algebraic ambient space and to the given current on H. Transport through the analytic ISOMORPHISM identifies the ordinary forms, current differentials and canonical integration, and gives a scalar description on a neighborhood of the original x. No pullback of a current by a finite noninvertible map is involved. In particular the algebraization theorem is not used as a claim that an arbitrary G-domain has become an ordinary neighborhood: the interior argument provides that missing step.

These scalar descriptions agree on overlaps by the same positive-test argument as in Section 5. They give a locally constant scalar on every ordinary open W in Z, and one scalar when W is connected. This proves the proposed analytic statement, conditional only on the validity of the supplied projective assembly and the explicitly identified standard analytic/algebraization interfaces. This NEW proof is not covered by the earlier endpoint audit and must be checked independently before promotion.

## 7. The bidegree-zero Bedford--Taylor consequence

Let U be any ordinary open subset of Z and let T,u,v be as in (1.2). Locally T=c delta with c constant by (1.1). Multiplication of a positive order-zero current by a continuous function is defined by its coefficient measures, so uT=c[u] and vT=c[v] on that neighborhood. Applying the two current differentials gives

    d'd''(uT)=c d'd''[u]=c d'd''[v]=d'd''(vT).

Equality is local and therefore holds on all of U, even when its connected components carry different constants. For continuous psh potentials these are precisely the single-step Bedford--Taylor products under discussion. Positivity or regularization of the difference u-v is not required.

This includes arbitrary ordinary subopens, not just a pair defined on one fixed standard polycylinder. It still concerns ONLY bidegree-zero T. The proof does not identify every continuous zero-curvature function as ordinary smooth, and does not multiply an arbitrary positive-bidegree current by an unsupported nonsmooth differential form.

## 8. Examples, unsatisfied gates, and what remains

For any ordinary connected open subset of affine n-space over K, including one cut out by analytic inequalities rather than an algebraic open, the proposed conclusion is T=c delta. The proof works by restriction to smooth projective space; it does not extend T to the projective boundary.

For a connected smooth analytic space with no given global algebraization, Section 6 would still give the same conclusion through local affinoid algebraizations and ordinary-interior identifications. The algebraic ambient varieties and their compactifications may vary from point to point; the single global scalar comes from uniqueness on overlaps, not a global compactification.

The complete higher-dimensional P21.3 question is not solved by these examples or by (1.1). Its remaining scope includes arbitrary positive-bidegree currents and singular pure analytic spaces, as well as field hypotheses outside this discrete residue-characteristic-zero argument. Neither a general envelope theorem nor equivalence of every non-Archimedean psh definition follows from (1.1).

All new statements in this sibling require independent exact-final mathematical review and production Rethlas verification. No production acceptance has been obtained, and no permission boundary is bypassed. Hash and syntax checks preserve evidence but do not establish correctness. Frozen predecessors remain unchanged; corrections to this note after freeze belong in a sibling or addendum.
