# P21.3 auxiliary obstructions: bounded independent exact-byte audit

Date: 2026-08-31. Reviewer: p082_independent_reaudit. Author of the reviewed note: p213_skeletal_hostile.

## Verdict and limits

PASS for exactly the three fully stated claims in OBSTRUCTION_NOTE.md Sections 3, 4, and 6, and for their stated separation from the open scalar-rigidity target and full P21.3. No substantive mathematical gap was found in this bounded scope.

This is not an audit of the conditional source-representation assertion in Section 2, the earlier skeletal/cross packets or Section 5, nor a proof of scalar rigidity. No conclusion that all compatible calibration families are canonical is obtained. There is no production verification, live integration, inventory retirement, or new-priority claim.

The reviewer has previously worked on non-Archimedean curve and Gauss-fibre questions in this project, but did not author these three claims. Their displayed proofs were checked afresh, without assuming the conditional source-representation packet. The parent's preliminary mathematical assessment was not used as acceptance evidence.

## Exact input binding

All paths below are relative to the worktree `/private/tmp/nappt_p071_20260827`, except the two explicitly absolute primary-source paths. The candidate directory is `manuscript/editorial/solver_dossiers_20260831/p213_calibrated_chart_rigidity_research_20260831`.

| Input | SHA-256 |
| --- | --- |
| Candidate OBSTRUCTION_NOTE.md | b27c56591db85bfef79e8e34b47637a06bd7df8f9d065b46b5303c64cfd61b86 |
| Candidate MANIFEST.json | a27d1042cf1426de4c28146994a84dac816fa6ec88992cbfd4bfc9c28cc5ec4b |
| Candidate TARGET.tex | 6598bf384d2033a2a01d0f4309f8119a3c1272c6c6f23fa46f194ad34e7a9f27 |
| Candidate SOURCE_INTERFACE.md | 5c4fca9dd3b996b98bdf1678f5b63a63d4091d0ccd6bb921f27e9f62e29b80b5 |
| Candidate VALIDATION.json | ef15cd155630012bdb8585a2579e8f7f6d265315b9f2495263ddfbde966cb335 |
| manuscript/parts/part6/ch72_major_open_problems.tex | 6e671da09d50cc7becd553d319a0cbce0fe6c3622ac77a491550411a32c69b8c |
| manuscript/editorial/open_problem_atomic_inventory_20260824.md | 227b7fc73c50c4f17e17b5efb9231a595cb9585463299ff77feaa30e96ef06d6 |
| /private/tmp/CLD25.pdf | 5690f999523017d184ab751bb55857ab1637b197d1186ad4fd2edba7e1bda719 |
| /private/tmp/CLD25_20260830.txt | 24920a1f4c8bd4944c83d89c8747c95b0206ae0754053eb0ed4d3de95e0f7727 |

The note, target, and source interface were read completely. A read-only Node check recomputed the manifest hash and all 15 recorded file sizes and SHA-256 values: 15/15 matched. Checking hashes of the earlier packets is preservation verification, not mathematical endorsement of those packets.

## Section 3: no common dominating positive Radon measure

PASS. The example uses the actual canonical integration current on the smooth algebraic analytification `(A1_K x Gm_K)^an`, for `K=C((pi))`, `|pi|=exp(-1)`. This space is connected, strict, good, separated and boundaryless, of pure dimension two. Boundarylessness is asserted for the ambient analytification, not for the compact affinoid domains inside it.

The displayed Q and Q_a are compact strict affinoid domains; their endpoint radii belong to the value group. For distinct constants a,b, `|a-b|=1`, while membership in both Q_a and Q_b would force `|a-b|<=exp(-1)`. Thus the uncountable family is genuinely disjoint. Also Q_a lies in Q, including for a=0.

The support of chi lies in a compact rectangle strictly inside the open tropical box. Its inverse image is contained in a compact polyannulus inside the ordinary open chart. Consequently extension of the top form by zero is smooth; no assertion about smooth extension through a nonzero boundary value is being used. The ordered product `d'u wedge d''u wedge d'v wedge d''v` has the positive, interleaved CLD sign. Since `(x-a,z)` are actual torus coordinates, the coordinate lattice has weight one and the integral is exactly the positive Lebesgue integral of chi.

The coefficient-measure step is valid on this ambient space. Good and separated imply locally holomorphically separated; CLD 15.2.4 then gives local differential separation, the hypothesis in CLD 7.2.8 and 7.2.11. A positive current wedged with the positive top form produces a positive bidimension-zero current and hence its positive Radon measure, supported on Q_a. The formula involving rho is initially read for smooth test functions and then for continuous compactly supported functions through the unique order-zero extension. Choosing a smooth cutoff equal to one near the support identifies its mass with the positive top-form integral.

If all these measures were absolutely continuous with respect to a single positive Radon measure sigma, each Q_a would have positive sigma-mass. Since Q is compact, sigma(Q) is finite. For each integer j>0 there can be only finitely many disjoint Q_a with mass at least 1/j; their countable union contains every positive-mass Q_a. This contradicts uncountability. No countability or metrizability of X was assumed.

This rules out the proposed common-Radon-dominator shortcut on the displayed whole surface. It does not assert failure on every sufficiently small ordinary neighborhood and, because the current is delta_X itself, is not a counterexample to rigidity or Bedford--Taylor independence.

## Section 4: finite etale degree versus ordinary sheets

PASS. The algebraic torus map `(x,z)->(x^m,z)` is finite free of rank m, with basis `1,x,...,x^(m-1)` over the target ring. Its derivative `m x^(m-1)` is a unit because the characteristic is zero and x is invertible. Thus its analytification is finite etale of degree m; both analytic surfaces have the required strict/good/boundaryless properties.

At the downstairs unit Gauss point eta, the completed residue field has residue field `C(ybar,zbar)`. The reduction of `T^m-y` is irreducible: apply Eisenstein in `C(zbar)[ybar]` at ybar, then pass to its fraction field. If the original monic polynomial factored over H(eta), all roots in an algebraic closure would have norm one. The coefficients of each monic factor, being elementary symmetric functions of roots, would be integral. Reduction would preserve both positive factor degrees and contradict irreducibility. There is no assumption that K is algebraically closed.

The analytic fibre is therefore the Berkovich spectrum of a degree-m field extension of the complete field H(eta), a single point by uniqueness of the extended non-Archimedean absolute value. Substitution of monomials shows that the upstairs unit Gauss point maps to eta. Its residue extension `C(xbar,zbar)/C(xbar^m,zbar)` has degree m. Hence the fibre has one ordinary point, not m points, and cannot admit m disjoint ordinary neighborhoods each mapping isomorphically over a common neighborhood of eta.

The degree/sign consistency check also passes: tropical pullback under `diag(m,1)` contributes m twice, once in each differential grading, while Lebesgue change of variables contributes 1/m. The net factor is m. The argument does not invalidate degree-weighted pushforward or etale-site statements and does not establish source disintegration.

## Section 6: positive divisor functionals on a proper regular curve

PASS in the exact arbitrary-field scope. A closed point q has finite positive degree `[kappa(q):k]`; it need not be rational. On a regular integral curve all divisors are Cartier. The degree convention is over k, with `chi(O(D))=deg_k(D)+chi(O_C)`. For clarity, its extension from effective divisors to arbitrary integral divisors follows by writing D as a difference of effective divisors and using the degree change under tensoring with their invertible sheaves.

Choose H=Nq with `deg_k(H)+chi(O_C)>0`. This H is fixed as n varies over all integers. For any degree-zero A, proper coherent cohomology and vanishing above dimension one give `h0(O(H+nA))>=chi(O(H+nA))>0`. Integrality turns a nonzero section into a nonzero rational section with an effective zero divisor D_n linearly equivalent to H+nA. It follows that `lambda(H)+n lambda(A)>=0` for every positive and negative integer n. Finite-valuedness therefore forces lambda(A)=0.

The degree-weighted difference `(deg_k q)p-(deg_k p)q` now shows that the ratio `lambda(p)/deg_k p` is independent of the closed point p. Finite additivity on divisors and positivity give the asserted nonnegative multiple of degree. Neither vanishing of H1 nor a uniform very-ampleness assertion is required. The proof does not use geometric connectedness, algebraic closedness, a genus formula with constant field tacitly equal to k, or torsion of Picard-zero classes.

This is an established algebraic mechanism, not a claimed new theorem about analytic currents. No analytic realization of such a functional is supplied by the lemma.

## Primary-source and visual checks

| Source/version directly checked | Exact interface used | Scope retained |
| --- | --- | --- |
| Chambert--Loir--Ducros, arXiv:1204.6277v2, dated 25 July 2025; local PDF/text above | 1.2.4; 1.5.1--1.5.2, printed pp.23,33 | Interleaved positive top-form sign and determinant factor; not a theorem about all source calibrations |
| Same CLD source | 7.2.8--7.2.11, printed pp.161--163; 15.2.2--15.2.4, p.423 | Positive coefficient measures and the local-separation hypothesis for good separated analytic spaces |
| [Stacks, Degrees on curves, Definition 33.44.1 and Lemma 33.44.7](https://stacks.math.columbia.edu/tag/0AYQ), read 2026-08-31 | Euler-characteristic definition and line-bundle tensor additivity | Proper curves over any field, with degree measured over that field |
| [Stacks, Lemma 33.44.9](https://stacks.math.columbia.edu/tag/0AYY), read 2026-08-31 | Effective Cartier divisor degree and Euler-characteristic change | No smoothness or geometric-connectedness requirement; regularity in the audited claim ensures Cartier divisors |

The finite-Gauss-fibre calculation was independently checked directly, using elementary Eisenstein reduction, finite free algebra and the standard uniqueness of valuation extension for a finite extension of a complete non-Archimedean field. It is not attributed to an unchecked CLD disintegration theorem.

Using the PDF skill, the complete CLD pages 23, 33, 161, 162, 163 and 423 were rendered and visually inspected. The wedge order, integration sign footnote, coefficient-measure hypotheses and local-separation bridge match the extracted text. No candidate PDF was created or compiled; visual inspection is source verification, not proof verification by compilation.

## Separation from the targets and final status

The displayed live Chapter 72 problem at lines 3150--3168 permits any complete non-Archimedean field, includes every bidegree `(p,p)` for `0<=p<=n-1`, and does not impose quasi-smoothness. It asks about equality of Bedford--Taylor products for actual continuous psh pairs on every ordinary open subset.

TARGET.tex instead asks scalar rigidity only for connected quasi-smooth spaces over a nontrivially valued field and bidegree zero. Even a proof of that target would address only part of P21.3. The three auxiliary results audited here do not prove even that smaller target. For a scalar current the displayed Hessian-independence implication is immediate by linearity, but no argument in these three sections makes an arbitrary current scalar.

The section-2 source-representation premise, the section-5 cross-refinement packet and the missing analytic residual-curve interface remain outside this verdict. Hash preservation must not promote them to accepted dependencies. P21.3 and the scalar-rigidity target remain open in this packet. Only this report and its checksum file are newly authored; candidate and live files are unchanged.
