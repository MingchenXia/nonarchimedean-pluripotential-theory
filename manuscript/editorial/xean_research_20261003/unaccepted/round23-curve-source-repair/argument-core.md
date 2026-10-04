# P06.2: source-repair attempt and retained diagnostics

This is an incomplete research record, not a proof of the requested curve theorem.
No substantive new analytic recognition or approximation theorem is claimed.
The status has exact identifier `P06.2` and `proof_file: null`. The original
arbitrary-dimensional atom remains open; no strict analytic counterexample is
constructed. P05.2 has not been investigated here.

## Exact requested gate and where this attempt stops

Let K be complete and nontrivially valued and let X be a good, separated,
strict, boundaryless, pure one-dimensional K-analytic space. Let U be an
ordinary open, let h be finite continuous, and suppose its ordinary CLD Hessian
current D[h] vanishes on U, where D=d'd''. Write C for the completion of an
algebraic closure with its extending valuation and π:U_C→U.
The requested conclusion is the following: for every x∈U_C and every ordinary
neighborhood N of x, there is one compact strict affinoid Y⊂N with x in its
actual ordinary interior, and two sequences u_n^+,u_n^- continuous on this
same Y, ordinary CLD-smooth and psh on its interior, decreasing uniformly to
h∘π and −h∘π respectively. Nilpotents, singularities, imperfect K, positive
characteristic and actual component Artinian lengths must be retained.

An equation is an equation against all compactly supported ordinary smooth
tests, not an a priori curve pullback or a claim that D[h] is a Radon measure.
In dimension one the pairing is ∫hDφ for ordinary scalar tests φ. Canonical
integration uses each component's actual generic length. Two logically
different requirements are (i) the completed-algebraic scalar-current
transport, and (ii) the fixed-neighborhood two-sign ordinary psh
regularization. Neither is declared proved by a preceding verdict.

The elementary calculations below survive scrutiny. They do not complete
the analytic construction. This record does not claim an extra conditional
hypothesis as a solution, does not exchange ordinary opens with G-covers,
and does not infer ordinary smooth approximation from weak smoothness or
an iterated generated hierarchy.

## Canonical input and version checks

The source reader ingests the entire bytes of the round-16, round-17 and
round-21 authoritative arguments and their canonical run.json notes; it
selects `/campaign/result/notes`, with counts 3, 5 and 2. The duplicate
work-result entries do not create additional notes. The argument bodies,
canonical notes, complete controlling review, both book TeX packets and
the selected primary proofs were inspected during this attempt. Machine
ingestion of a full source appendix is not represented as a completed
mathematical audit of every nested citation in that appendix.

The round-16 independent review is retained with its INCONCLUSIVE disposition
and its 23 premises/19 passage checks. There is no override. No round-16,
round-17, round-21 or round-07 theorem is an accepted mathematical premise
here. The round-17 requested filename `proof-core.md` is absent at the given
location; the actual `repair-core.md` exists and was inspected alongside
the authoritative argument. No predecessor file was rewritten or modified.

The fresh causal evidence has SHA-256
`dfc96b12afe112f6eccb35d34417a4199892ded5501305edae0aa15f55c912d3`,
matching the assignment and the supplied manifest. Its official identity
evidence identifies Thuillier tel-00010990v1; the evidence records that the
official unversioned PDF and cached v1 PDF are byte-identical. This run used
the installed cache and made no new network authentication claim. The correct
official DOI for Berkovich (1993) is `10.1007/BF02712916`.

The two CLD text caches differ, but their PDFs have exactly the same bytes,
SHA-256 `5690f999523017d184ab751bb55857ab1637b197d1186ad4fd2edba7e1bda719`.
The differing text hashes are
`64846cb00926267c6238d1afac61b5eaed0a0e3a6349725738f9b1bf163de085`
and `021be260392de1f3240858d4c775da86653518dfab4fd9c4c21a2406081b6c7e`.
This is a text-extraction discrepancy, not evidence for a different PDF or
a mathematical error. LF line coordinates must name the particular cache.

All new extraction uses `split('\n')` or `split(b'\n')`; PDF formfeeds are
not new lines. Raw selected bodies, starts, complete printed endings,
source hashes and selected-body hashes are included below and in
`evidence/source-selections.json`. Printed proof completion does not prove
the applicability of every nested reference. OCR spelling/control bytes
are retained as evidence rather than silently repaired quotations.

## Field-scope repair with an elementary proof

**Lemma.** If A is an algebraically closed non-Archimedean valued field,
its completion C is algebraically closed. If the valuation is nontrivial,
the value group of C is divisible and its logarithm is dense in R. Its
residue field is algebraically closed. These facts do not assert current
transport.

**Proof.** Let F(T)=T^d+Σ_{i<d}c_iT^i∈C[T], d≥1. Choose a real B≥1
bounding every |c_i|. Choose decreasing positive ε_m→0, all less than 1.
By density choose monic polynomials F_m over A with
max_i|c_{m,i}−c_i|≤ε_m^d B^{−(d−1)}. Their coefficients have absolute
values at most B. Every root of every F_m in A has absolute value at
most B: at |z|>B, the leading term strictly dominates all other terms.
Choose a root r_1 of F_1. Given r_m, ultrametricity and the coefficient
bounds give |F_{m+1}(r_m)|≤ε_m^d. Factor F_{m+1} into d linear factors
over A. If all its roots were farther than ε_m from r_m, the product
of those d distances would be greater than ε_m^d, a contradiction.
Choose r_{m+1} with |r_{m+1}−r_m|≤ε_m. Ultrametricity makes (r_m)
Cauchy. Its limit r∈C satisfies F(r)=0 by continuity and convergence
of the coefficients. Induction on degree factors every polynomial
over C. Repeated roots and inseparability cause no problem in this
argument.

To prove residue algebraic closure, lift a monic polynomial over the
residue field to a monic polynomial with coefficients in C^∘. Its
roots in C all have norm at most one by the leading-term argument.
Reducing its linear factorization gives a linear factorization over
the residue field. Divisibility of |C^×| follows by taking n-th roots
in C for each n≥1. Its logarithm contains all rational multiples of
one nonzero number because the valuation is nontrivial. Those
multiples are dense in R. This proves the lemma. ∎

Consequently van der Put's *The class group of a one-dimensional affinoid
space*, Ann. Inst. Fourier 30(4) (1980), 155–164, Theorem 1.1 can be
considered over C. The introductory field convention, printed page 155,
explicitly assumes complete and **algebraically closed**. The theorem
states that every one-dimensional normal connected affinoid space is an
affinoid subspace of a nonsingular complete curve. The affinoid convention
uses a quotient of the unit-radius Tate algebra, hence the strict setting.
The selected proof and its actual final paragraph, including Lemma 1.2,
are embedded below. No arbitrary-K finite-separable algebraization is
deduced from it. This is a scope repair, not a new curve theorem.

Berkovich, *Étale cohomology for non-Archimedean analytic spaces*, Publ.
Math. IHÉS 78 (1993), §1.6, works with a nontrivially valued field and
Hausdorff strict spaces. Theorem 1.6.1 gives full faithfulness into
quasiseparated rigid spaces. Lemma 1.6.2(i) identifies a rigid open
affinoid domain with a strict Berkovich affinoid domain. Its word
"open" describes a rigid domain; it does not put every Berkovich point
in an ordinary interior. The full selected proofs are embedded, including
the end of the theorem proof. The further paracompact equivalence is not
needed for a single affinoid-domain identification. No inference from
"injective on a dense subset" alone is used here.

For an intended actual application one must also identify the intrinsic
analytic interior of an affinoid with its ordinary interior in the
boundaryless ambient curve, using the relative-interior composition
theorem with separated target. That is a separate analytic theorem and
its applicability; it is not supplied by rigid/Berkovich identity evidence.
No new actual-domain application is claimed complete in this record.

## Exact metric-tree calculations

The following are elementary graph facts, not assertions that a curve
neighborhood has already been realized by such a graph.

Let T be a finite connected metric tree with positive edge lengths, B a
nonempty set of boundary vertices, and I=V(T)\B. The Laplacian at a
vertex is the sum of its outgoing edge slopes. Fix b∈B and set
μ(v)=1 for v∈I, μ(b)=−|I|, and μ=0 on B\{b}. Thus Σμ=0.
Root T at b. For an edge with child c and parent p let S_c be the
vertices in the child subtree and put M_c=Σ_{v∈S_c}μ(v). Give that
edge slope M_c in the direction c→p and integrate from ψ(b)=0.
No cycle imposes a period equation, so this defines one continuous
piecewise affine ψ.

At a nonroot vertex c, the outgoing slope towards its parent is M_c
and the outgoing slopes towards its children are −M_d. Hence
Δψ(c)=M_c−Σ_d M_d=μ(c). At b the same identity follows from
Σμ=0. In particular Δψ(v)=1 at every interior vertex. All slopes
are integers. This proves, on the given tree, the positive interior
Laplacian auxiliary function used in rational strictification.

If F is continuous edgewise affine on T and ΔF(v)≥0 at every v∈I,
then H=F+δψ has ΔH(v)≥δ for δ>0. Fix orientations of the edges.
Choose rational slopes q_e differing from the slopes of H by less
than η, integrate them from the same root value, and call the result G.
Rational density gives the choices. Tree path uniqueness gives
||G−H||∞≤Lη, where L is the sum of all edge lengths, and
|ΔG(v)−ΔH(v)|≤deg(v)η. If I is nonempty choose
η<δ/(2 max_{v∈I}deg(v)); then ΔG(v)>δ/2 at every interior vertex.
The total uniform error is bounded by δ||ψ||∞+Lη and can be made
arbitrarily small. When I is empty there is no interior inequality.
This proves the metric-tree rounding calculation, not its analytic
realization by ordinary unit-log germs.

The exact program in `diagnostics/finite_checks.py` enumerates all labelled
trees with 2 through 6 vertices using Prüfer codes, all nonempty boundary
subsets, and specified positive rational edge lengths. It verifies the
displayed Laplacian identity with exact fractions in 85,787 cases on
1,441 trees. This is an exhaustive finite result for that stated finite
domain; the general proof is the subtree calculation above. If the edges
are indexed by k=0,…,n−2 in the Prüfer decoder's output order, their
tested lengths are (k+2)/(k+1). The case count for order n is
n^(n−2)(2^n−1), giving [3, 21, 240, 3875, 81648] for n=2,…,6.

## A retained failed approach: rounding on a fixed cyclic graph

Let a graph have vertices v0,v1,b0,b1. Join v0 to v1 by two separate
edges of lengths 1 and √2, and attach an edge of length 1 from each vi
to bi. The boundary is {b0,b1}. Define the continuous edgewise affine F by

F(v0)=0, F(v1)=1, F(b0)=−1−1/√2, F(b1)=2+1/√2.

At v0 its outgoing slopes are 1,1/√2,−1−1/√2 and sum to zero;
at v1 they are −1,−1/√2,1+1/√2 and also sum to zero. Thus F is
harmonic in the metric-graph sense.

Suppose G is continuous and affine on each of these **same unsubdivided
parallel edges**, with rational slopes q1 and q2 in the direction
v0→v1. Endpoint consistency forces
G(v1)−G(v0)=q1=q2√2. Irrationality of √2 forces q1=q2=0.
For completeness, if √2=a/b in lowest positive integer terms, a²=2b²
makes a even; writing a=2c then makes b even, a contradiction.
Hence G(v0)=G(v1), and the triangle inequality gives
1=|F(v1)−F(v0)|≤2||G−F||∞. In particular no such rational-slope
G approximates F with uniform error less than 1/2.

This disproves the *fixed-edge* independent rational-rounding procedure
on arbitrary graphs. It does not obstruct refinements with new breakpoints,
other approximants, or a genuinely realized local-tree procedure. It is
not an analytic counterexample to P06.2 and is not counted as a solution.
An exact finite check in Q(√2), representing a+b√2 by (a,b), tests slopes
a/b with −6≤a≤6 and 1≤b≤6; it finds only the zero continuous pair.
The irrationality proof, not this finite search, gives the universal result.

## Convex caps and a monotone shift, with all hypotheses visible

Choose a nonnegative even smooth probability kernel ρ supported in
(−1,1) on R, and let ρ_η(t)=η^{-1}ρ(t/η). Set
χ_η=|·|*ρ_η and

m_η(s,t)=(s+t+χ_η(s−t))/2.

Convolution makes χ_η smooth and convex; its derivative is between −1
and 1. Its even kernel has mean zero, so Jensen's inequality gives
χ_η(r)≥|r|, while the one-Lipschitz bound gives χ_η(r)≤|r|+η.
For |r|≥η the sign is constant on the convolution support and the
zero first moment gives χ_η(r)=|r|. The Hessian of m_η is
(χ_η''(s−t)/2) times the positive semidefinite matrix with rows
(1,−1),(−1,1). Its two first partials (1±χ_η')/2 are nonnegative.
Thus m_η is smooth, convex, nondecreasing in both arguments, equals
max(s,t) when |s−t|≥η, and lies between max(s,t) and max(s,t)+η/2.

On a ray t≥0, given c∈R, a>0, r>0 and 0<η<ar, define
k(t)=m_η(c−at,c−ar). It is convex and smooth, equals c−at
for 0≤t≤r−η/a, and equals the constant c−ar for t≥r+η/a.
Relative to the original constant value c its absolute error is at most
ar+η/2. The exact affine and constant intervals provide *open* overlap
regions whenever the containing annular collar has sufficiently large
length. After the constant interval the cap can be continued by that
same constant; restoring c instead would change the construction.
This is an elementary one-variable calculation. To use it on a curve
one must still exhibit an actual whole annular collar, its unit
coordinate, its overlap with the vertex germ, the rest of its disc,
and the ordinary CLD positivity calculation. None of those analytic
inputs follows from this convex calculation alone.

For any fixed compact set Y, suppose (already constructed) continuous
approximants g_n to f satisfy ||g_n−f||∞≤b_n, b_n=4^{-n}. Put
c_n=Σ_{j≥n}(b_j+b_{j+1})=(5/3)b_n and u_n=g_n+c_n. Then
c_n−c_{n+1}=b_n+b_{n+1}, so
u_n−u_{n+1}≥−b_n−b_{n+1}+c_n−c_{n+1}=0.
Also 0≤u_n−f≤(8/3)b_n. Therefore u_n decreases uniformly to f.
Adding constants preserves ordinary smoothness and psh if g_n already
have those properties. The argument applies independently to two signs
on the same Y. It cannot turn approximants on shrinking neighborhoods
into approximants on a common compact set. The diagnostic checks the
two fraction identities exactly for n=1,…,100; the infinite formula
is proved by the geometric-series calculation just given.

## Primary scope checks and the indispensable open applications

**Actual affinoids and model realization.** Thuillier tel-00010990v1,
Theorem 2.3.8 states that a strict rig-smooth affinoid pure of dimension
one becomes the generic fibre of a simply semistable formal curve after
a finite separable field extension. Lemma 2.3.9 gives the harmonic
Dirichlet isomorphism with functions on its Shilov boundary. Their complete
selected proof bodies are embedded. Over C the finite extension is
trivial; van der Put is used only in this algebraically closed setting.
The printed proof of 2.3.8 places the actual boundary on a refined model
and then asserts that the reduction image of the affinoid is an open U
and that the affinoid is the generic fibre of the formal restriction to U.
This attempt has not independently established that formal-open
realization for each chosen neighborhood, followed by the required local
finite-tree neighborhood construction at every kind of analytic point.
Point insertion alone does not establish it. The relevant printed
proof statement is not concealed, but its application is not declared
proved by this dossier.

The published Bosch–Lütkebohmert, *Stable reduction and uniformization
of abelian varieties I*, Math. Ann. 270 (1985), 349–379,
DOI `10.1007/BF01473432`, Theorem 7.1 has the hypotheses: a smooth
geometrically connected **projective** curve over a complete
non-Archimedean field. It gives potential stable reduction for genus
at least 2 and potential semistable reduction for genus at most 1.
The installed scanned statement was checked visually; the machine OCR
misreads its inequalities. Its complete proof route through Lemmas 7.2,
7.3, Proposition 7.4 and preceding results was inspected. For a smooth
proper connected algebraic curve over C, projectivity and geometric
connectedness must be supplied by the standard algebraic curve theorems;
finite extensions of C are trivial. That is the proper-projective
application, not a direct theorem about a singular analytic curve or
about an arbitrary prescribed affinoid formal open. The archival scan
and OCR remain at their supplied local paths; they are not redistributed
as an entire monograph in this dossier.

**Residual principal lifts and every direction.** Thuillier Lemma
2.3.22 identifies a quotient of harmonic germs by real unit-log germs
with Pic^0(C_v)⊗R after a reduction to a proper geometrically connected
residual component. Its proof constructs harmonic slopes on inserted
directions and displays a unit-log/principal-divisor exact sequence.
The latter converse lifting and its use on a *common* actual ordinary
neighborhood need to be checked in the desired construction; printed
exactness is not here substituted for an explicit simultaneous lifting
application. Proposition 2.2.24 and Lemma 2.2.25 give the slope
−ord_p(tilde f) for an already present analytic unit on the stated
semistable formal charts. Lemma 2.2.25 in particular assumes a connected
simply semistable formal curve with a single special-fibre singular
point and a global analytic unit on its generic fibre. These statements
are not arbitrary residue-germ statements on an unconstructed
neighborhood. The construction still needs one actual unit-log germ
with its complete set of slopes, finite exceptional directions, whole
annular tubes in every exceptional direction, and common exact overlap
domains. Approximating an element of H(v) alone does not establish that
entire application chain.

Lemma 2.2.22 explicitly distinguishes two operations: finitely many
type-2 points can become model vertices after finite extension, while
an arbitrary type-3 point in general cannot become such a vertex by
that operation; part (ii) can put type-2 or type-3 points on the
skeleton. Over C finite extensions are trivial. A metric subdivision
at a type-3 point must not be silently called a formal-model vertex.

**Comparison is not ordinary regularization.** Wanner arXiv:1801.04713v3,
Theorem 4.7 and Corollary 4.8 concern ordinary opens of the
analytification of a smooth proper **algebraic** curve over an
algebraically closed complete nontrivially valued field. In Definition
3.16, psh denotes current positivity, not the first ordinary-smooth
decreasing-limit stage. Algebraic very-affine test units are analytic
units; consequently those tests belong to the ordinary analytic test
class. This inclusion has the useful direction from an ordinary
analytic zero equation to Wanner's equation, not the reverse inclusion.
Her Theorem 4.7 has no general ordinary psh regularization conclusion.
The complete selected Lemma 4.6/Theorem 4.7 proofs are embedded so that
the model-function/calibration citations and the construction ending
are visible. Those nested primary applications are not all reproved
in this attempt. A positive-genus vertex cannot be included in an
open annular cap, and a comparison used for smoothing needs a strictly
positive error margin. Correcting those two local features does not
by itself prove all the supporting model-function chain.

The entire book statement/proof was read. It explicitly uses positive
curvature in fresh residue-disc directions, a fixed compact neighborhood,
and exact equality on open overlaps. Its tree rounding, convex caps
and monotone shift have the elementary proofs above. Its remaining
local semistable realization, residual Riemann–Roch movement and actual
unit-germ gluing applications have not been made into a complete
independent proof here. Psh functions cannot be glued by arbitrary
partitions of unity. Ordinary smooth harmonic approximation is a
different assertion and is not claimed.

**Normalization, punctures and nilpotent lengths.** The round-07
recognition argument uses the normalization isomorphism off the
conductor, continuous rigid-puncture removal and a closed-curve
restriction claim. These claims were inspected as fallible proofs,
not reused as theorem grants. An arbitrary finite fibre product can
contain isolated zero-dimensional components; its reduced pure
one-dimensional part must be taken and its surjectivity proved before
invoking a curve theorem. A regular element alone does not prove S_1
for an arbitrary quotient. On a pure nonreduced curve, writing the
integration cycle as Σm_i[C_i] does not by itself separate the zero
current equation into the component equations at intersection points.
At a rigid point an ordinary smooth scalar unit-moment germ is locally
constant: for a unit f and rigid C-point a, the ordinary inequalities
|f−f(a)|<|f(a)| imply |f|=|f(a)|. A finite tuple has a common such
neighborhood. This elementary fact does not imply local constancy of
an arbitrary continuous zero-current h. The missing conductor,
puncture and test-extension chain cannot be discarded on that basis.
No normalization-harmonicity-to-ordinary-zero-current bridge is claimed
proved in this submission.

**Completed-algebraic transport.** The full round-21 argument and both
canonical notes were examined, with the corrected primary bodies rather
than historical formfeed-split excerpts. Its needed obligations include
actual embeddings of finite fields, compact support of exact descended
ordinary forms, preservation of good/strict/boundaryless/pure curve
structure, wild/separable and Frobenius stages, and the scalar top-measure
multiplicities. Its scalar comparison uses no degree factor, whereas a
same-carrier restriction-of-field comparison has a field-degree factor;
interchanging them would be invalid. This run has not reconstructed all
the requisite calibration, compact-form descent and induction
applications into an independent completed-algebraic transport proof.
No use is made of its prior PASS as a mathematical premise. This remains
a separately recorded unmet obligation here, even if a future audit
validates that packet. Nothing here asserts transcendental ascent.

## Audit disposition and rerun

The exact still-unproved claims for this attempt are:

1. the needed ordinary-current transport to C with actual component
   lengths and exact compact tests;
2. the full reduction/normalization/conductor/puncture recognition
   and reverse current bridge on singular or nonreduced curves;
3. actual fixed-affinoid semistable/formal-open and finite-tree
   realization with the prescribed ordinary neighborhood and the
   **actual** Shilov boundary;
4. simultaneous residual-unit lifts, every-direction slope identities,
   whole annular collars and exact ordinary overlap gluing;
5. combining those inputs into two ordinary smooth psh sequences on
   the same fixed compact Y.

These are absent proofs, not proved impossibilities. The finite graph
obstruction is limited to one discarded rounding procedure. There is
no new analytic counterexample. An equation on a strict radial core,
the false non-strict arbitrary-radius extension, a G-cover, or a new
conditional hypothesis does not substitute for the requested target.

Artifacts are `P06.2-argument.md` (this diagnostic dossier plus complete
selected raw proof bodies), `status.json`, `notes.json`, `self-audit.md`,
`research-evidence.md`, `source-evidence.md`, `build-evidence.md`, and
the programs and outputs in `evidence/` and `diagnostics/`. The argument
filename is an access point for the failed attempt, not a nonnull proof
claim. No standalone TeX/PDF is produced because the condition requiring
them—a complete substantive new theorem—has not been met.

Rerun `bash reproduce.sh` in this fresh workspace. It checks immutable
input hashes and canonical notes, re-extracts selected bodies using LF,
runs the exact finite diagnostics, assembles this dossier, and validates
the status/note schema and artifact hashes. It neither changes old
artifacts nor runs a model or mathematical verifier. Execution success,
source authentication, source hashes and self-audit are not mathematical
certification or priority evidence. All computation is small local
Python computation. No supervised heavy-compute facility was supplied;
none was needed or used. No subagent, extra model, network, installation,
external message or authentication/environment modification was used.

# Selected primary proof evidence

The following blocks are directly accessible for review without filesystem
tools. They are source evidence, not replacement proofs for the unmet
applications above. Source identities and literal LF boundaries are explicit.
