# Triangular hyperfields, metric inequalities and Lorentzian signatures

Date: 8 October 2026. Source-only checkpoint before book integration.
Preservation baseline: `27c459491c52a4b4f08ffa04363374d0a0dcb3d7`.

Baker, Huh, Kummer and Lorscheid, *Lorentzian polynomials and matroids
over triangular hyperfields, Part 2: Analytic aspects*, exact
arXiv:2607.15375v2, revised 18 August 2026, has been read in full:
88 physical pages, complete selected text and 44 individually displayed
matching images, with sequential notes. Four dependency PDFs were read
in the exact partial scopes below. The combined checkpoint contains
**135 distinct exact-source/page pairs and 68 matching images**: one
whole paper and four partial readings. A further focused reread of four
already counted primary pages resolves a support-boundary convention;
it adds zero distinct pages. Acquisition, searches, prepared views and
repository inventories receive no mathematical reading credit.

This is an attributed source audit. The principal analytic containments
and the sharp five-element result survive the scoped checks with the
qualifications below. Some subsidiary statements and one appendix proof
must not be imported as written. There is no original theorem promotion,
independent-model verification receipt, canonical open-problem solution,
or exhaustive certification of current open status.

## Exact sources and reading scopes

| Controlling source | Physical pages actually read | PDF SHA-256 |
| --- | --- | --- |
| Analytic aspects, 2607.15375v2, 88 pages | All 1–88 | `a6c9e52b2843ff25289cef8b07915cb62406e138029695b1d027d884b2f0828e` |
| Topological aspects, 2508.02907v3, 10 October 2025, 82 pages | 1–2, 32–41; twelve pages | `2200c81f9b621df24f68d3ab7b175f7ad2d57dd5e51cabc8165f278610ebe3a5` |
| Representation theory for polymatroids, 2507.14718v2, 17 September 2025, 90 pages | 1–2, 17–20, 35–40; twelve pages | `ecd94bd6b76d16de46f701f4b31c03160eb3eebd7aea9c5c60053e5c024c5dad` |
| Faver et al., Glasgow Math. J. 56 (2014), 519–535, DOI 10.1017/S0017089513000438; published seventeen-page PDF | 1, 5–9; six pages | `62eeedd6b314351778a0b1466723b7c9f833ede85fae0116c1eb676daa91e32c` |
| Brändén–Huh, Annals 192 (2020), 821–891; published 71-page PDF | 14–16, 25–27, 30–37, 44–46; seventeen pages | `ecfc011bb4c755d6e1e802fbdcbff6eed4c6f907cb2968fedee6e68f5be71ff8` |

The reading notes preserve the actual sequential observations, including
issues subsequently resolved. The manifest records source, selected-text,
image and note hashes. No earlier reading of other papers is counted as
fresh reading here.

## Coefficients, support and weak relations

**TH01 — Normalization.** Definition 2.23 of Part 2, Part 1 pages 32,
38–39, and the published BH normalization proof all use
`f_rho=sum rho(alpha) x^alpha/alpha!`. The operator
`N_t(x^alpha)=x^alpha/(alpha!)^t` therefore gives
`N_t f_rho=sum rho(alpha) x^alpha/(alpha!)^(t+1)`.
This extra factorial is essential outside squarefree support. A
homeomorphism of projective spaces is not an equality of these
coefficient maps.

**TH02 — Fixed support.** A weak representation has support exactly the
given nonempty M-convex set J: coefficients are positive on J and zero
outside it. The common multi-index and repeated indices must obey
`delta^-_J<=alpha` and the coordinatewise upper bound `delta^+_J`.
The vector formulation and strong definition are cleared at Representation
Definition 4.3, pages 35–36, and the near-idempotent discussion on 39–40.
For finite positive q, a null sum means the q-th roots of its nonnegative
summands are side lengths of a polygon. Three terms give the triangle
inequalities. At q=0 the maximum is attained at least twice; at q=infinity
every sum with at least three nonzero terms is admissible, whereas two
nonzero terms must be equal.

**TH03 — Standalone binary omission.** Part 2 Lemma 5.4's unqualified
nonnegative-coefficient iff must retain the exact-full-support assumption
from the surrounding representation space. The zero function or
`[1,0,0,1]` satisfies the local adjacent inequalities but is not a
representation of the full binary simplex. With all coefficients
positive, the relation computation and Proposition 5.5 are valid:
weakness is `a_(k-1)a_(k+1)<=2^q a_k^2`, and the exponential polynomial
is Lorentzian iff `(a_k)` is log-concave. For t>0 the sufficient bound is
`t min_k log_2((k+1)(d-k+1)/(k(d-k)))`. At t=0 no positive q works
uniformly on the full binary degree-d simplex. This is not a
counterexample to the fixed-support main theorem.

## Analytic containments

**TH04 — The upper inclusion is compatible with exponential coefficients.**
Part 2 Theorem 3.1/Proposition 3.7 prove `L_J subset N R^w_J(T_2)`;
they do not assume that inverse normalization preserves Lorentzianity.
After derivative and positive diagonal rescaling, inverse normalization
multiplies each diagonal Hessian coefficient by
`lambda_i=(alpha_i+2)/(alpha_i+1)<=2`, leaving off-diagonals fixed.
Distinct quartets use the zero-diagonal four-by-four determinant; single
and paired repeats use the original Lorentzian minor inequalities plus
those bounds. General t gives the upper parameter `2 max(1,t)`.

**TH05 — The rank-two lower bound.** Positive zero-diagonal matrices are
normalized by positive diagonal congruence so the distinguished first
row is one. Three-term relations through that point make
`d_ij=B_ij^(1/q)` a metric on the remaining n-1 points. The remaining
quartets are precisely Ptolemy inequalities. Published Faver et al.
Theorem 3.6 is on physical page 8 / printed 526 and uses STRICT
`0<=p<log_2(1+1/(m-1))` for m points. It supplies affine independence
strictly below the bound. Part 2 reaches the endpoint by closure, where
zero eigenvalues are permitted. Thus the lower bound is
`log_2(1+1/(n-2))`; the endpoint is not an independent-embedding theorem.
The older inputs used within Faver's proof are attributed rather than
recursively recertified here.

**TH06 — General supports and the exceptional square.** Part 1
Theorem 4.7, fully selected on 34–35, forces each two-class coefficient
block to have rank one before the small-class uniform shortcut. This
also handles only two parallel classes; positivity alone would not.
Only active-variable class weights are uniquely determined; unused
variables have immaterial unconstrained weights. Weighted copies in
Part 2 produce a uniform rank-two representation, then compression
gives diagonal factor `theta_i=((alpha_i+1)/(alpha_i+2))^t` for t>0.
Three/four lifted indices in the same fibre give coincident products
and are automatically admissible; they must not be passed to an
inadmissible downstairs quartet. Copies with two elements chosen in a
basis are not parallel matroid elements.

Part 2 defines V(K) using off-diagonal terms only, whereas Part 1
includes present squares. The support `K={2e_i}` therefore gives empty
V(K) in Part 2's simplification as printed. Its Hessian is an immediate
positive rank-one case, to be separated before the weighted-copy
argument. This omission is not a disproof of Theorem 5.1. The imported
general sandwich retains t>0, nonempty exact support, and permits
degenerate quadratic derivatives.

**TH07 — The minor-quantifier issue.** Part 2 Remark 5.7 claims
`q(N)>=q(M)` for every minor N of M, justified by representation and
Lorentzian descent. Descent only controls representations of N that
extend from M; it does not quantify over all weak representations of N.
The printed reason is insufficient. Uniform-size monotonicity can be
treated separately by duplicating an element and using the actual
relations. The general lower bound can be obtained from rank-two
contractions without importing an arbitrary-minor assertion.

An independently implemented finite diagnostic for PG(2,3) enumerates
its thirteen F_3 points, 234 bases, and two-term weak Plücker equalities.
The equality matrix has rank 221 modulo the prime 1,000,003; its exact
annihilation of the thirteen element-incidence columns gives an upper
bound 221 over Q, and the incidence matrix has rank thirteen modulo
that prime. Thus the rank statement is an exact integer certificate,
not a floating-point fit. A contraction with four chosen parallel-class
representatives gives U_2,4. The inferred objection to the threshold
claim remains an **UNVERIFIED original candidate**, pending the
required separate model receipt. Neither this candidate nor arbitrary
minor monotonicity is promoted into book theorem typography.

## Sharp small cases and operations

**TH08 — The four- and five-element bounds.** The complete proofs of
Part 2 Sections 6–7 were read. For four elements, the zero-diagonal
determinant is the quadratic expression in the three opposite-edge
products, yielding q(4)=2. For five elements, normalization identifies
the question with four-point Ptolemaic metrics. The Gram proof of the
sharp exponent `log_2 3` explicitly checks its determinant-concavity
endpoints: collinear configurations, a centre with three leaves,
attached tails, and tight Ptolemy via inversion. Zero/coincident
endpoints are taken by limits. The example with one distance two and
all other distances one gives sum-zero quadratic form
`2(2^q-3)`, so the exponent is optimal. BH Proposition 3.25 handles
smaller positive parameters by normalized coefficient powering;
its published statement/proof reduction is read on physical 45.

Two-block matrices with within-block entry a and cross-block entry one
have eigenvalue -a with multiplicity n-2. Their remaining two eigenvalues
come from the displayed two-by-two quotient; two are positive exactly
when `a^2(r-1)(s-1)>rs`. Balancing block sizes gives the even upper
bound `2 log_2(n/(n-2))` and odd upper bound
`log_2((n+1)/(n-3))`, hence q(n) has order 1/n. Sharpness for all n>=6
is a source-era conjecture, not a certified addition to the open catalogue.

**TH09 — Weak and strong are not aggregation invariants.** Part 2
Proposition 8.2 uses `a_k=2^(k choose 2)`; a strong degree-d relation
would demand `2^(d-1)<=d^c`, contradicting any fixed c for large d.
Representation Proposition 4.8 and its full proof on 38–39 clear the
uniform U_(d,2d) lift. These particular polynomials are not asserted
Lorentzian.

Part 2 Propositions 8.4/8.5 give explicit six-variable cubics that fail
even weak relations after identifying two variables. All thirty
three-term squarefree relations, and all fifteen nontrivial strong
four-term relations in the strong example, were separately enumerated.
The weak output would require
`1+2^q<=2^(1+q/2)`; the difference is the positive square
`(2^(q/2)-1)^2`. The strong example fails for 1<=q<=2, including its
endpoint 10>9. These contrast with BH Theorem 2.10, which preserves
Lorentzianity under every nonnegative linear substitution.

## Trees and strictness

**TH10 — Elementary tree proof.** The full appendix was read. Its
edge-coordinate embedding sends a leaf to the sum of the square roots
of the positive edge lengths along its root path. Squared Euclidean
distance equals tree distance. Distinct leaves have private positive
pendant coordinates, giving affine independence and strict conditional
negative definiteness on sum-zero vectors. A positive all-ones Rayleigh
quotient gives inertia (1,n-1). Extending leaves to equal root height
writes a tree metric as an ultrametric plus `c_i+c_j`; the exponential
matrix is positively diagonally congruent to that for the ultrametric.
This proves the exponential statement independently of Appendix proof six.

**TH11 — Two appendix exclusions.** Appendix A.7 calls the canonical
metric-graph measure a probability measure. The standard canonical
measure can have negative vertex masses, for example at the centre
of a three-leaf star. Its mass-one signed version may still support
the linear energy argument. No positive-probability assertion or
fresh Baker–Rumely dependency reading is imported here.

Appendix A.8's proof six asserts squared complex Plücker absolute
values lie in a STRICT Lorentzian stratum and treats its logarithm as
closed. The cited Part 1 Theorem 5.1 explicitly has a non-strict target
and boundary conclusions. For real columns `(1,0),(1,1),(1,2),(1,3)`,
squared Plücker coordinates form the positive off-diagonal matrix
`A_ij=(i-j)^2` of rank three, with nonzero kernel `(-1,3,-3,1)`.
Adding epsilon to every off-diagonal entry gives strict matrices
converging to this singular matrix: on sum-zero vectors the quadratic
form is `-2(sum i c_i)^2-epsilon sum c_i^2`. Both printed strictness
inputs therefore fail as stated. A closed non-strict limit argument
does not prove nondegeneracy. This appendix proof is excluded; the
elementary tree proof above remains available.

## Evidence and preservation

Seven exact diagnostic groups passed in the corrected second helper:
the four-element determinant; normalization/support fixtures;
PG(2,3) equality rank and minor data; exhaustive weak/strong cubic
relations; the squared-Plücker kernel and strict-limit fixture;
the four-cycle negative-type obstruction; and the canonical-measure
wording boundary, whose external formula still needs a source check.
These are finite diagnostics, not an independent model receipt.
The first helper passed its algebraic assertions but failed to serialize
a SymPy zero; its written candidate certificate is preserved separately.
The failed run is not relabeled successful. A separate receipt-freeze
helper initially required one exact prose phrase despite equivalent
earlier read attestations; that administrative failure is preserved too.

The author-linked Lean repository `icarm/FourPointPtolemaic` is pinned
at `1564ff7909a3adc980bf2a7e0efa5ced88c1383b`. Its README and nine-file
inventory were inspected; Lean/lake are unavailable in this cloud
environment. No Lean source-proof reading, installation, execution or
formal-check success is claimed.

The 4,560-page baseline book, all historical formal statements/proofs,
425 active inputs, 108 protected inputs, 138 frozen prior records,
215 earlier exports, and the existing native catalogue are preserved
at this source-only checkpoint. The canonical inventory remains
42 atoms in twelve problem environments. General BJ22 critical
homogeneous Siu division/envelope closure remains OPEN; the LPWZ
density candidate remains UNVERIFIED.
