# Tau, tropical moments and uniform positivity: source review

**Source-only checkpoint.** The clean baseline is
`f933e24f21e3a1da54280a82a2fd7eea81a022d1`. Ruihua Wang's
*Uniform positivity of the tau invariant*,
[2610.04994v1](https://arxiv.org/abs/2610.04994v1), was submitted
4 October 2026 at 06:29:10 UTC. Its complete fifteen-page PDF was read
as extracted text and displayed as original page images, including
all proofs and references. Ninety-three dependency pages were also
read and displayed. No active TeX, original result, verification
receipt or canonical status changes at this checkpoint.

## Conclusions and mathematical signature

For a finite connected metrized graph with positive edge lengths,
effective resistance is the minimum of sum L_e j_e^2 over unit flows.
The tau invariant is one quarter of the Dirichlet energy of r(p, -).
Subdivision makes the base point a model vertex. Write ell for total
edge length, b for total bridge length, and

    F_e = 1 - r(u_e,v_e)/L_e,
    A = sum L_e F_e^2,
    B_p = sum (r(p,u_e)-r(p,v_e))^2/L_e.

Then tau=A/12+B_p/4. The tropical Jacobian is the integral cycle
lattice in ker(partial), with inner product sum L_e x_e y_e. Its
full tropical moment I is the average squared norm on a centered
Voronoi cell, with no factor one half. De Jong--Shokrieh's identity
is I=ell/8-tau/2. All three quantities ell, tau and I scale linearly
with edge lengths. A tree has tau=ell/4 and I=0; a circle has
tau=ell/12 and I=ell/12. The circle's Euclidean Jacobian circumference
is sqrt(ell), distinct from its graph circumference ell.

Wang's Theorem 1.1 gives tau >= c_-(ell-b)+b/4, where c_- is the
unique root in (0,1/12) of

    c_-(1-4c_-)^2 = 4/(27 pi^2 e^2),
    c_- = 0.0020654439458672232... .

The proof combines an attributed dual-lattice moment bound, a
cographic matroid partition and Holder's inequality. The lattice
bound is I >= (1/(2 pi e)) sum 1/||y_i||^2 for independent vectors
in the dual lattice. Principal-minor conditions on the coordinate
covariance matrix come from its periodized density being at most
one. The LDL pivots need not individually exceed one: decreasing
weights and Abel summation control their logarithms. Independent
dual coordinates give a surjective torus map even without a
primitive integer image. These two apparent objections are cleared.

After bridge contraction and two-edge-cut reduction, the relevant
coordinate matroid has rank |S|-c(G minus S)+1. Its independent sets
are those with connected edge complement. Minimum cut degree three
gives Edmonds' rank condition for three independent subsets. This is
a cographic partition, not a partition into ordinary forests.
Contraction of one edge in a two-edge cut transfers its length to
the other and **retains every created loop**; the cycle lattice and
its metric are preserved. Bridge contraction removes length b and
decreases tau by b/4.

Put R=sum L_e/F_e and t=tau/ell after the reduction. The lattice
bound gives R<=6 pi e I, while Holder gives ell^3<=A R^2. Together
with tau>=A/12, these imply
t(1-4t)^2>=4/(27 pi^2 e^2). The scalar function is increasing on
(0,1/12). If t>=1/12 the desired bound is already true; no upper
assumption t<=1/12 on every graph is needed.

Theorem 1.3 constructs simple cubic graphs Gamma_M, M>=3, with
6M^2 vertices, 9M^2 edges and total length 15M^2. A periodic
hexagonal graph is expanded by unit triangles and length-three
connectors. Triangle--star reduction, edge transitivity on the
base graph and Foster's trace identity give

    beta_M = (M^2+1)/(3M^2),
    F_connector = 9 beta_M/11,
    F_triangle = 1/3 + beta_M/11,
    tau(Gamma_M)/ell(Gamma_M) --> 59/7260 < 1/108.

Length-preserving vertex transitivity makes the resistance correction
equal to tr(Q^+)/n, bounded after normalization by the vertex
diameter divided by 2ell. The diameter bound 8M+5 makes that term
vanish. The source gives finite counterexamples for M>=300. Exact
rational checks verify the gap 1/108-59/7260=37/32670 and the finite
M=300 upper bound. Independent numerical networks at M=3,4,5
reproduce both Foster coefficients, their trace, the base-point
tau formula and the transitive formula, with coefficient errors
below 7e-15. These finite computations are diagnostics; the
all-M argument is the paper's proof, not a new result of this project.

The optimal universal normalized tau constant remains open; the
source bounds place it between c_- and 59/7260. This is an additional
related research direction, not a resolution or addition to the
existing 42-atom canonical catalogue.

## Height and sign interfaces

Remark 4.5 applies to a smooth projective geometrically connected
curve of genus at least two over a number field, with semistable
reduction. The local graph is the geometric dual graph of its minimal
regular model, with unit edge lengths. The finite-place contribution
uses (1/[k:Q]) sum I(Jac(Gamma_v)) log N(v); archimedean terms remain.
In the primary height paper, Theorem A has coefficient 2/[k:Q] and
Theorem B identifies its local invariant with **half** the tropical
moment. These factors cancel, confirming Wang's coefficient.
The local valuation is normalized by v(uniformizer)=1; the
arithmetic log N(v) weight is separate. Unread height antecedents
are not certified by this check.

Chapter 8 uses outgoing slopes and a negative-semidefinite vertex
Laplacian. The electrical papers use incoming slopes and the positive
conductance matrix Q=partial D^(-1) partial^T. Thus Q is the negative
of the book's vertex operator. Resistance, Dirichlet energy and tau
remain positive. Any integration must state this sign conversion
before displaying matrix formulas.

## Fourteen diagnostics and retained source corrections

The frozen machine-readable diagnostics distinguish literal source
defects, corrected conventions and cleared objections. They do not
claim a counterexample to Wang's main conclusions or the final
tropical moment identity.

1. Moments Example 4.6, actual p.11: its endpoint resistance
   interpolation requires the source point outside the open edge.
   On a unit segment with p=q=1/2 the literal formula gives 1/2,
   instead of zero. Subdivision at q repairs the scope used later.
2. Moments Theorem 5.4 proof, actual p.14: the sum over f prints
   ell(e) in the denominator; it should be ell(f), as in the
   statement. A two-edge path of lengths 1 and 2 distinguishes them.
3. Moments Definition 5.2(ii), actual pp.12--14, and the zero-diagonal
   Z calculation on pp.17--18: the auxiliary incident-edge sum
   must exclude f=e. A single unit edge gives literal t=1 but
   the theorem's expression zero. With t_0=sum over f different
   from e, AZ delta_e=t_0; including e adds
   P(e)(delta_u+delta_v). Later diagonal terms are already separate.
4. Cinkir's discrete matrix formula uses an optimal simple model;
   Wang states simplicity in the transitive specialization.
5. The tau/moment two-edge-cut reduction retains loops, unlike the
   moments paper's resistance-only contraction convention.
6. The half-moment height normalization and arithmetic weight pass.
7. The LDL pivot objection is cleared by weighted Abel summation.
8. The nonprimitive dual-image objection is cleared by torus
   surjectivity and Haar pushforward.
9. The cographic rank and Edmonds partition conditions pass.
10. The root branch, Holder constants and bridge correction pass.
11. The cubic construction, triangle--star identity, Foster
    coefficients, limit and finite rational inequalities pass the
    targeted independent computations above.
12. Baker--Rumely v2, actual p.37, has a June 2005 footnote claiming
    the stronger 1/108 value had been proved. That historical
    footnote is not an independent proof here and is not imported
    as the current universal bound. Its 2007 publication PDF is unread.
13. Rayleigh Remark 5.3, actual p.9, incorrectly equates Q^+ to the
    uncentered average of grounded inverses. For one unit edge,
    their average is I/2 but Q^+=(1/4)[[1,-1],[-1,1]]. The corrected
    formula sandwiches the average between H=Id-11^T/n on both
    sides. The uncentered average is a generalized inverse and
    gives the same zero-mass pairing, as Proposition 5.2 permits.
14. Rayleigh Theorem 8.2, actual pp.18--19, needs the discrete measures
    supported outside the contracted open edge. On Gamma=[0,2],
    contract e=[0,1] and take nu=delta_(1/4)-delta_(3/4). The quotient
    remains a nondegenerate segment and its pushed-forward energy is
    zero; the literal rank-one expression gives 1/4. The proof cannot
    make e a single model edge while making its interior charges
    model vertices. Subdivision and successive contractions handle
    arbitrary interior charges. Wang uses Theorem 7.8, which is
    independent of Theorem 8.2; moments uses vertex-supported charges.

These defects in auxiliary source statements must not be promoted
to general claims that the main tau proof or tropical moment identity
is false. Conversely, the known final identities do not make the
literal incorrect auxiliary statements correct. Complete further
tiling, volume and height antecedents remain outside this audit.

## Exact primary reading

All sources below were freshly read for the listed physical pages.
Publisher metadata and unread editions are distinguished from the
actual PDF acquired. The dependency total is 93 physical pages in
48 displayed sheets; Wang adds fifteen in eight sheets, for **108
physical pages and 56 sheets**. Dependency sheet 34 was reread after
a truncated tool response; only the complete repeat is counted.

| Exact edition | Physical pages read | Reading scope | PDF SHA-256 |
| --- | --- | --- | --- |
| Wang, 2610.04994v1 | 1--15 | Complete PDF | `946d24046c6e5c76792ebd2cf88fc6b04cbf968728c37805342d19cef67c023f` |
| de Jong--Shokrieh, Tropical moments, CJM 75(4) (2023), 1045--1075, DOI 10.4153/S0008414X22000220 | 1--31 | Complete publisher PDF | `be9f583c9c78ed5cdbfc828858f1a71aac612e4f67430007450c4c34950a97cf` |
| Cinkir, 0902.3401v3, 17 December 2009, 07:33:12 UTC | 1--13 | Complete preprint; published 2011 PDF unread | `30b56e64d71915aa2680f593bc059bcd360e50928fc5c58f5a4e7685e37c798b` |
| Edmonds, NBS 69B(1--2) (1965), 67--72 | 1--6 | Complete NIST publisher PDF; scanned formulas checked visually | `864357675b91b552e899a2ccee434a4a28d04749b2ff629dc4bfd49d317a4440` |
| Baker--Rumely, math/0407427v2, 27 July 2005, 18:49:23 UTC | 1, 36--39, 43--47 | Selected ten of 47; other 37 and published 2007 PDF unread | `2f2f4cdeb472e0c6203644624a1f30c4b2ef7a0809322366d82b699a58dd0e4c` |
| de Jong--Shokrieh, Rayleigh, RMJM 52(4) (2022), 1403--1422, DOI 10.1216/rmj.2022.52.1403 | 1--20 | Complete publisher PDF supplied by NSF PAR | `df6e609bfd06af2af053e80b380a907cb2bfbf02ef0c0fc2d20fcca8bd8761bd` |
| de Jong--Shokrieh, Heights, Compositio 158 (2022), 1--32, DOI 10.1112/S0010437X21007661 | 1--7, 23--24, 30--33 | Selected thirteen of 33, including publisher cover; other twenty unread | `7f5abfa3aa3a8ceb4752094c6a72a68fa4390fe0599f4e1ec5647e2fa29c9f9c` |

Wang's full-reading record has SHA-256
`1b399ab4647c9aac749fd2d32c261d91aa79fbc6cdb415e6bd1c9e7e4bc7a20c`.
The dependency-reading record has SHA-256
`e0ab56dd7dd65986584bf6b3717e2db26f35c5b1a27b93b108efae8e240bfe49`.
The final diagnostic record has SHA-256
`47d26c775f9da559d8a849a61299e6cc6a64eb19a0e391af6ef6cad7b390d31a`.
Its preceding v1 remains frozen; v2 only chooses a nondegenerate
quotient graph for diagnostic 14 and repeats no network computation.

## Preservation and next integration

All 425 active inputs, 108 protected inputs, 73 prior frozen manifests
(57 integrations and sixteen source reviews), 127 prior exports,
the 4,401-page book and fourteen generated project files retain
their bytes. Only README and the research programme change among
the 5,075 baseline tracked files; the other 5,073 are preserved.
The inventory remains 42 atoms in twelve families with tier counts
0/3/7/15/17. General non-Archimedean Siu/closure remains conditional
at the existing BJ22 proof boundary. The open native catalogue
source, PDF and editor are unchanged, with no new native compile.

The next scoped book step is the connection between Chapter 8's
graph Green functions, resistance energy, full tropical moments and
the attributed new positivity result, with Appendix L provenance.
The positive electrical matrix sign, loop retention, cographic
partition and height half-factor must be explicit. This checkpoint
does not certify the full unread dependency chain or admit an
original theorem. No new independent production model call or
verification receipt is claimed. Routine fetch and work-branch push
follow standing user authorization and retain platform checks.
