# Research-question ledger

## Non-Archimedean pluripotential theory monograph

**Snapshot date:** 15 August 2026  
**Research engine for Passes R1--R3:** `gpt-5.6-sol`, `xhigh` reasoning effort  
**Scope:** explicit questions in the two supplied archives; directly relevant
questions in the BFJ, BJ, CLD, Gubler--Künnemann--Jell--Rabinoff,
DXZ/Xia, Mesquita-Piccione, Mesquita-Piccione--Witt Nyström, Bingener,
and local valuative sources; gaps exposed by the planned comparison
theorems.

This is an internal research document, not a list of claims for publication.
It records what has been tried, what is already known, and where a proof
actually stops.

**Controlling delta, 25 August 2026.**  Later exact production runs supersede
the 15 August candidate classifications in five places.  The weighted cross
has both a compact-source obstruction and a proper noncompact analytic
realization, although equality of curvature remains only after pushforward.
The positive-current problem has a verified regular complete-intersection
slice but not a global converse.  The CLD hierarchy collapses at stage one on
tropical toric partial compactifications and on the stated finite-valence
boundaryless tropical curves; unrestricted higher-dimensional, boundary, and
infinite-valence cases remain open.  The real-PL zero-current implication is
also verified on good separated boundaryless strict pure-dimensional spaces,
while the arbitrary continuous higher-dimensional problem remains open.  The
literal ordinary CLD-smooth harmonic approximation variant is disproved on a
smooth curve, while that 25 August gate did not decide ordinary CLD-smooth
psh regularization.  The
exact run identifiers and scope
firewalls appear in the current tables below.

**Controlling delta, 27 August 2026.**  Three later exact gates supersede
additional current-facing entries below.  The canonical cubical
delta-metricity problem is resolved: the product--Gauss criterion shows that
an ample cubical metric in split Raynaud uniformization is ordinary delta if
and only if the residual Raynaud extension is isotrivial, hence answers the
non-isotrivial mixed-reduction case negatively.  On smooth proper algebraic
curves over algebraically closed complete nontrivially valued fields,
continuous current-psh functions admit decreasing ordinary CLD-smooth psh
regularization; this does not contradict the harmonic-approximant
counterexample.  Finally, first-stage collapse holds for every finite
ambient-induced real-affine star, including extended-valued polar branches,
without lattice or balancing hypotheses.  Arbitrary non-toric
positive-sedentarity structures not covered by the toric theorem, nonambient
structures, infinite-valence stars, and higher-dimensional settings remain
open.  The current
literal frontier is fifteen problem environments in Chapter 72 and one in
Chapter 71, split into fifty-five active atoms.  Exact hashes, production
responses, and scope firewalls are recorded in the dated receipts and the
atomic inventory.

---

## 1. Status vocabulary

| Status | Meaning |
|---|---|
| **Published theorem** | Verified in a primary published source, with hypotheses checked |
| **Source-manuscript theorem** | Claimed and proved in a supplied manuscript; audit state is recorded separately, and publication is not implied |
| **Historically resolved** | Posed as open in an older source and subsequently settled |
| **Candidate proposition** | A complete-looking argument was produced in Pass R1; an independent proof audit is still required |
| **Conditional reduction** | A correct implication reduces the problem to a named missing input |
| **Counterexample/no-go** | A proposed formulation is false, subject to checking the cited example |
| **Open after Pass R1** | Literature audit found no solution and the solver pass did not close the main gap |
| **Programme, not proposition** | The wording denotes a family of theories rather than one yes/no statement |
| **VERIFIED (R3)** | Exact signature, independent proof, adversarial audit, boundary tests, and source/novelty separation all passed |
| **CONDITIONAL (R3)** | The implication is valid only after an explicitly displayed additional input or hypothesis |
| **DISPROVED (R3)** | A counterexample or signature obstruction survived the independent audit |
| **OPEN (R3)** | Neither a proof nor a counterexample survived the audit in the stated natural framework |

A candidate proposition is never cited as a theorem in the textbook. Promotion
requires a separate hostile audit, a source audit, and tests on boundary cases.

---

## 2. The envelope property

### EP-1. BJ envelope conjecture on unibranch projective varieties

**Status:** source-manuscript theorem; modular dependency, proof, and source
audits completed for the first draft.

The second supplied archive claims the following full statement.

> Let \(X\) be an integral projective unibranch variety over an algebraically
> closed trivially valued field, and let
> \(\theta\in N^1(X)_\mathbf R\). For every nonempty bounded-above family
> \((\varphi_i)\subset\operatorname{PSH}_X(\theta)\), the usc regularization
> \((\sup_i\varphi_i)^*\) belongs to \(\operatorname{PSH}_X(\theta)\).

This is the stated scope of BJ Conjecture 5.14: arbitrary dimension,
characteristic, and real numerical class, including semivaluations with
proper support where the functions may equal \(-\infty\).

The public 2022 BJ addendum proves a smaller smooth case when the field has
characteristic zero or the dimension is at most two, together with an
ample-class energy result on singular varieties. Thus the supplied proof is a
substantial extension.  It has received a theorem-level modular audit for the
first draft, while its status as a supplied, not yet bibliographically
identified publication is kept visible throughout the book.

**Completed audit decomposition:**

1. circularity check for all regularization/reflection inputs;
2. asymptotic test ideals, subadditivity, fixed twists, and uniform
   \(O(m^{-1})\) class error;
3. determinant norms at inseparable/nonreduced fibres;
4. alteration and Stein-factorization descent;
5. Roberts--Singh additive powers and global homogeneous weight control;
6. Frobenius reflection in positive characteristic;
7. values on nontrivial-support semivaluations and common \(-\infty\) loci;
8. the net/usc passage in the final theorem.

**Book disposition:** replace the obsolete conjecture in the first archive by
the theorem, with a provenance note and the complete audited proof in
Chapters 37--45.

### EP-2. Remove unibranchness

**Status:** false as a general request.

The envelope property for an ample class forces unibranchness in the relevant
BJ setting. The node/cusp contrast will be used to explain sharpness. This is
not sent to the solver queue as if it were a plausible generalization.

---

## 3. Trace and restriction questions from the supplied complex book

### TR-1. Trace Dirichlet problem

**Statement.** For a connected compact Kähler manifold \(X\), a submanifold
\(Y\), a Kähler class \(\alpha\), and a Kähler current
\(S\in\alpha|_Y\), find a Kähler current \(T\in\alpha\) such that
\[
  \operatorname{Tr}_Y(T)\sim_{\mathcal I}S.
\]

**Status:** open after Pass R1 in general; split product/retraction special
case validated by independent Pass R2.

**Validated special case.** Suppose
\(X=Y\times Z\),
\(\alpha=p_Y^*\alpha_Y+p_Z^*\alpha_Z\), and
\(S=\theta_Y+dd^c\psi\in\alpha_Y\) is a Kähler current. If
\(\eta\in\alpha_Z\) is Kähler, then
\[
  T=p_Y^*S+p_Z^*\eta
\]
is a Kähler current in \(\alpha\) and solves the problem on
\(Y\times\{z_0\}\). Indeed, a quasi-equisingular approximation of \(\psi\)
pulls back through the smooth projection, multiplier ideals commute with that
pullback, and restriction recovers the original approximation. Consequently
\[
  \operatorname{Tr}_{Y\times\{z_0\}}(T)
  \sim_{\mathcal I} P_{\alpha_Y}[\psi]_{\mathcal I}
  \sim_{\mathcal I}S.
\]
If \(S\) is \(\mathcal I\)-good, the canonical representative satisfies
\[
  P_{\alpha_Y}[\psi]_{\mathcal I}\sim_P S.
\]
This does not promote \(\operatorname{Tr}_{Y\times\{z_0\}}(T)\) itself to a
\(P\)-class: the sourced trace is defined only up to
\(\mathcal I\)-equivalence.

For a holomorphic retraction \(r:X\to Y\) with section \(i:Y\hookrightarrow
X\), the same conclusion holds under the genuinely necessary splitting
\[
  \alpha=r^*\beta+\gamma,
\]
where \(\gamma\) has a smooth semipositive representative \(\eta\) that is
strictly positive on \(\ker dr\) and satisfies \(i^*\eta=0\). Then
\(T=r^*S+\eta\). A bare retraction does not provide positivity in the fixed
class.

**Main obstruction.** One must extend singularity/multiplier-ideal data inside
a fixed global cohomology class while retaining strict positivity.

### TR-2. Trace on an unibranch complex ambient space

**Status:** open after Pass R1.

The second archive's algebraic envelope theorem does not supply the missing
analytic input. The obstruction is equisingular Demailly-type regularization
and a robust multiplier-ideal formalism on a singular complex ambient space.
The first archive treats the case in which the subspace avoids the singular
locus by passing to an embedded resolution.

### TR-3. Construct a \(P\)-valued refinement of trace

**Status:** book-formulated question; open; the previous claim of an internal
resolution was withdrawn after checking the exact scope of Xia's Proposition
2.12.  A source-scoped Rethlas packet is prepared but was not run.

On
\[
  D_Y=\{\varphi\in\operatorname{QPSH}(X):\nu(\varphi,Y)=0\},
\]
the sourced theorem gives only
\[
  \varphi\sim_{\mathcal I}\psi
  \Longrightarrow
  \operatorname{Tr}_Y(\varphi)\sim_{\mathcal I}
  \operatorname{Tr}_Y(\psi).
\]
Thus trace descends to a well-defined map
\[
  D_Y/{\sim_{\mathcal I}}\longrightarrow
  \operatorname{QPSH}(\widetilde Y)/{\sim_{\mathcal I}}.
\]
Since \(P\)-equivalence implies \(\mathcal I\)-equivalence, the map from
input \(P\)-classes to output \(\mathcal I\)-classes factors as
\[
  D_Y/{\sim_P}\longrightarrow D_Y/{\sim_{\mathcal I}}
  \longrightarrow
  \operatorname{QPSH}(\widetilde Y)/{\sim_{\mathcal I}}.
\]
Neither statement supplies a map with values in \(P\)-classes. The open
refinement is to prove that the trace construction is independent of all
choices up to \(P\)-equivalence, or to construct another canonical
\(P\)-valued restriction with the expected compatibility. Even when a datum
\(S\) is \(\mathcal I\)-good and its canonical envelope
\(P_\alpha[S]_{\mathcal I}\) is \(P\)-equivalent to \(S\), this controls the
canonical representative, not the \(P\)-class of \(\operatorname{Tr}_Y(T)\).

**Packet:** `trace_p_valued_refinement.md`, prepared after the 15 August
source audit; no attempt or verification receipt exists.

### TR-4. Uniform \(L^2\) control in trace extension

**Status:** open after corrected formulation.

At each fixed tensor power, surjectivity between finite-dimensional section
spaces gives a bounded linear right inverse for arbitrary chosen Hilbert
norms. The meaningful question is uniform/asymptotic control in the tensor
power with the natural singular weights. Strong openness alone allows its
auxiliary parameters to deteriorate with the tensor power.

---

## 4. Zero mass and Okounkov bodies

### OK-1. A zero-mass body detecting numerical dimension

**Status:** open in general; toric theorem validated after repair in Pass R2.

**Validated toric theorem.** Let \(X\) be a smooth projective toric variety,
let \(T\) be a torus-invariant positive \((1,1)\)-current in an integral or
rational big toric class, and let \(K=\Delta(T)\) be its Newton/partial
Okounkov body. Then
\[
  \nu_{\mathrm{Cao}}(T)=\dim K.
\]

The original R1 proof through the book's mixed-volume formula had a gap: the
book's mixed volume and Cao's cohomological product are not literally the same
by definition without an approximation bridge. Pass R2 supplied a cleaner
argument. For an ample toric class with polytope \(Q\),
\[
  \Delta(T+\varepsilon\omega_A)=K+\varepsilon Q.
\]
Toric asymptotic Riemann--Roch identifies the section-growth term in Cao's
criterion with \(\operatorname{vol}_n(K+\varepsilon Q)\). If
\(d=\dim K\), elementary convex geometry gives
\[
  c\varepsilon^{n-d}
  \leq \operatorname{vol}_n(K+\varepsilon Q)
  \leq C\varepsilon^{n-d},
\]
and Cao's criterion yields the theorem.

A real transcendental toric class still requires a separately stated
definition and an approximation argument; it is not included for free.

### OK-2. A refined partial body whose volume is actual nonpluripolar mass

**Status:** open if full \(P\)-type data may be used; no-go theorem for
\(\mathcal I\)-invariant constructions validated in Pass R2.

The counterexample is the polar-Cantor potential on
\(\mathbf P^1\) from the first archive. It satisfies
\[
  \varphi\sim_{\mathcal I}0,
  \qquad
  \int(\omega+dd^c\varphi)=0,
  \qquad
  \int\omega=1.
\]
Thus any convex-body assignment determined only by multiplier ideals—or by an
ordinary partial Okounkov body that is \(\mathcal I\)-invariant—would assign
the same body to two potentials having different actual masses.

**Validated conclusion.** No \(\mathcal I\)-equivalence-invariant assignment
of measurable sets can
have Euclidean volume equal to the actual nonpluripolar mass for all
potentials. Convexity is not needed for this obstruction. A viable refinement
must contain genuinely \(P\)-sensitive data; the argument does not rule out a
\(P\)-invariant refined body.

### OK-3. Remove closure in the valuative characterization

**Status:** open in general; one special case and one conditional reduction.

- In the rank-one curve case with a smooth positive current of degree \(d\)
  and flag point \(p\), the full interval is expected to be realized directly
  by currents of the form
  \[
    S_a=a[p]+(1-a/d)T,
    \qquad 0\le a\le d,
  \]
  so closure is unnecessary. The class and normalization require checking.
- An iterated trace-Dirichlet theorem along a smooth flag would remove closure
  inductively: subtract the first-coordinate divisor, lift the desired trace
  from \(Y_1\), and continue along the induced flag.

### OK-4. Maximality of big-line-bundle filtration test curves

**Status:** primary-source conjecture; open at the cutoff.

Darvas--Xia--Zhang state immediately before their Definition 4.4 that it is
unclear whether the filtration test curves constructed in the big case are
already maximal, and conjecture that they are. Definition 4.4 therefore takes
the maximization before forming the Phong--Sturm ray. This is the exact
question; it is narrower than removing every \(P_\theta\)-projection in an
arbitrary big-class construction. Finitely generated filtrations, flag
configurations, semiample big line bundles, and birational pullbacks of ample
data are the first test classes.

### OK-5. Xia's three exact convex-body questions

**Status:** primary-source conjectures/questions; open at the cutoff.

1. Conjecture 5.29 asks whether
   \(\dim\Delta(L,\phi)=\operatorname{nd}(L,\phi)\), including the zero-mass
   limit-body setting.
2. Conjecture 8.8 asks for the non-toric mixed-volume formula, with a
   supremum over rank-\(n\) valuations, for positive-volume Hermitian big
   line bundles.
3. At the end of Section 6.4, Xia asks whether the Chebyshev transform is
   independent of the auxiliary Kähler-current potential
   \(\eta\preceq\varphi\).

The third item must not be confused with the already asserted independence
of the limit partial body from the auxiliary ample divisor \(H\) and Kähler
form \(\omega\) in Section 5.6.

---

## 5. Zero-mass singularity questions

### ZM-1. Is \(\varphi\sim_P P_\theta[\varphi]\) at zero mass?

**Status:** open after Pass R1.

The difficulty is not merely the vanishing of the top mass: \(P\)-equivalence
requires control of all relevant mixed masses/singularity data. No proof or
counterexample survived the first pass.

### ZM-2. Is every zero-mass \(\mathcal I\)-model potential
\(\mathcal I\)-good?

**Status:** open after Pass R1.

The next pass will test divisorial, analytic-singularity, toric, and surface
cases before attempting a general statement.

---

## 6. Non-Kähler and higher-bidegree directions

### NK-1. Extend the book to the non-Kähler setting

**Status:** programme, not proposition.

Work of Boucksom--Guedj--Lu gives important volume and Monge--Ampère progress,
but regularization, energy geometry, trace, and Okounkov constructions do not
transfer as one theorem. The research task must be decomposed construction by
construction and should not be advertised as “solved” by a partial analogue.

### HB-1. Higher-bidegree positive currents

**Status:** programme, not proposition.

For \((p,p)\), \(p>1\), scalar local potentials and strong equisingular
approximation are absent in general. Candidate theories should first be
tested for model currents, products of \((1,1)\)-currents, and toric currents.

---

## 7. BFJ questions over nontrivially valued fields

### BFJ-1. Remove algebraizability in residue characteristic zero

**Status:** historically resolved.

Burgos Gil--Gubler--Jell--Künnemann--Martin remove the algebraizability
restriction in the relevant residue-characteristic-zero Monge--Ampère theorem.
The exact theorem and base-field hypotheses will be checked from the primary
source before incorporation.

### BFJ-2. Mixed and positive characteristic Monge--Ampère

**Status:** partial published progress; open in unrestricted dimension.

Fang--Gubler--Künnemann prove a mixed-characteristic result assuming resolution
and embedded resolution. The unrestricted theorem without these inputs
remains open.

### BFJ-3. Arbitrary nonpluripolar right-hand sides over general fields

**Status:** open after Pass R1.

The original BFJ theorem has a support condition. The BJ finite-energy theorem
over a trivial valuation and the MPWN Kähler theorem do not imply the general
nontrivially valued statement.

### BFJ-3a. The \(\mathcal E^1\) Monge--Ampère operator over an arbitrary field

**Status:** exact primary-source question; open; prepared Rethlas packet not
run.

Pille--Schneider Remark 4.4 observes that the finite-energy class
\(\mathcal E^1(X,L)\) is defined over an arbitrary complete
non-Archimedean field, but that extension of the Monge--Ampère operator to
that class is unclear in general. The source names the discretely valued
characteristic-zero BFJ theory and the trivially valued BJ theory as the
established endpoints. This is an operator-construction question and must be
kept separate from the Banach-base family-continuity Question 4.9.

### BFJ-4. Must a Green function with divisorial pole be model or rational PL?

**Status:** counterexample in the literature.

Boucksom--Jonsson, *Non-Archimedean Green's functions and Zariski
decompositions*, C. R. Math. 362 (2024), Special Issue S1, 5--42,
Theorems A--B, construct a negative answer and also a finite atomic
Monge--Ampère solution supported on a dual complex but invariant under no
retraction attached to any snc model. This is later than the first
Gubler--Jell--Künnemann--Martin toric failure and closes the stronger
single-skeleton regularity expectation negatively.

### BFJ-5. Does every nef non-Archimedean class have a semipositive closed-form
representative?

**Status:** open/unclear in general.

It holds in basic curve, toric, semiample, and model cases. The question needs
a precise ambient cohomology theory before another solver pass.

### BFJ-6. Semiample psh metrics versus Zhang-nef metrics

**Status:** open/expected extension.

The ample equivalence is known. Extending it to the semiample case is expected
to require a descent or relative local Hodge-index theorem. This is narrower
than BFJ-5 and is the more tractable next target.

---

## 8. BJ topology questions

### BJ-1. Strong topology and the exhaustion \(T\) (BJ Question 11.16)

**Status:** disproved globally; positive on strongly compact subsets. The
fixed SNC-dual-complex case remains verified in characteristic zero for
smooth projective \(X\).

The question can be reformulated using
\[
  T(v)=d_\infty(v,v_{\mathrm{triv}}).
\]
Strong convergence implies weak convergence plus convergence of \(T\). The
converse is a nonlinear Radon--Riesz/Kadec--Klee property; mere comparability
of energy and \(T\) does not prove it.  The converse is false already on
\(\mathbf P^n\), for every \(n\ge2\): exceptional valuations \(v_j\) of
blowups at pairwise distinct points of a fixed linear line \(C\) converge
weakly to the line-centred valuation \(v_C\), while
\[
 T(v_j)=T(v_C)=1,
 \qquad d_\infty(v_j,v_C)\ge1.
\]
Here \(v_C=\ord_C\) for \(n=2\), and for \(n\ge3\) it is the exceptional
valuation of the blowup along \(C\).  The equality \(T(v_C)=1\), obtained
from the degree bound for the ideal of a linear line, is what makes this a
counterexample to the exact published premise; the older curve example had
\(T\) drop to zero at the weak limit.  The generalized packet passed guarded
production run `20260825T044839Z_326e2035bbb9`, item
`pi_9e222887262acc5d9fbc740a`, with final `correct`, zero critical errors,
and zero gaps.  The adapted exact-live theorem and proof separately passed
run `20260825T051642Z_049da6197deb`, item
`pi_062d99c623958fae25885125`, with the same clean verdict.

On every strongly compact subset, the answer is positive by the
compact-to-Hausdorff lemma. In particular, if the ground field has
characteristic zero, \(X\) is smooth projective, and
\(\mathcal X\) is a fixed SNC test configuration, BJ Appendix A,
Theorem A.4 makes \(\Delta_{\mathcal X}\) strongly compact; hence weak and
strong topologies coincide there. The same conclusion in arbitrary
characteristic is conditional on an independently sourced strong-compactness
estimate for the embedded dual complex and remains a separate restricted
question in this audit.  The moving centres above escape every one fixed
dual complex, so they do not contradict the positive theorem.

### BJ-2. Global bi-Lipschitz comparison for different ample classes

**Status:** open after Pass R1.

Known results give the same topology, the same bounded sets, and uniform
comparison on bounded regions. They do not provide one global bi-Lipschitz
constant.

### BJ-3. Divisorial versus ordinary K-stability thresholds

**Status:** exact threshold identity still open in this audit (BJ K-stability
II, Conjecture 5.15); it is no longer a missing input for the smooth
projective YTD theorem if one accepts the dated 2026 Trusiani preprint.

The conjecture asserts equality of the divisorial and ordinary stability
thresholds.  Trusiani's Theorem A proves the smooth polarized projective YTD
equivalence by a different dated route, and Corollary A solves the broad
Boucksom--Jonsson entropy-regularization conjecture.  Neither statement, by
its wording alone, identifies every separately normalized threshold in
Conjecture 5.15.  That exact identity remains a source-matching task rather
than being inferred from the existence theorem.

### BJ-4. Entropy convergence of canonical degree-one approximants

**Status:** broad entropy regularization is claimed resolved in Trusiani
arXiv:2605.30063v1, Corollary A; the exact canonical-degree-one formulation
below remains open in this audit until the two approximation sequences are
identified.

For a rational divisorial norm \(\chi\) and its canonical degree-one
approximants \(\chi_d\), the expected statement is
\[
  M(\chi_d)\longrightarrow M(\chi),
\]
equivalently convergence of the entropies of
\(\operatorname{MA}(\chi_d)\). This would imply BJ-3. Trusiani's Corollary A
constructs smooth ample test configurations approximating a dominating snc
big model and explicitly claims the equivariant Boucksom--Jonsson
regularization conjecture.  An existence theorem for some entropy-regularizing
sequence does not formally prove convergence for the separately prescribed
canonical sequence \((\chi_d)\); a term-by-term identification or a direct
citation is still required.

### BJ-5. Uniformly bounded support tests for divisorial stability

**Status:** open after Pass R1.

The question asks whether divisorial stability can be tested on divisorial
measures whose supports have cardinality bounded independently of the
measure. Toric surfaces admit a bound of two; no general bound was found.

---

## 9. Chambert--Loir--Ducros questions

The revised 2025 CLD manuscript remains the status source, but its questions
will be reformulated in the notation and modular architecture of the new book.

### CLD-1. Maximum principle for CLD psh functions

**Status:** historically resolved by Gubler--Rabinoff (2025).

Every CLD-psh function is classically psh: functoriality and scalar extension
reduce the smooth stage to Wanner's curve comparison, and transfinite
induction handles the CLD closure. Gubler--Rabinoff then prove the local
maximum principle for classically psh functions and the Shilov-boundary
maximum principle on affinoids. The interior qualification in the local
theorem remains essential. This resolution concerns the 2025 transfinite CLD
psh sheaf, not an arbitrary continuous function satisfying only
\(d'd''[u]\geq0\).

### CLD-2. Local CLD psh versus global semipositive/BFJ psh

**Status:** exact one-way comparisons and a PL equivalence verified in R3;
the reverse local-to-global arrow remains open in higher dimension.

On a complete nontrivially valued field, for a good strict analytic space and
an \(\mathbf R\)-PL function,

\[
  \text{residue-nef semipositive}
  \quad\Longleftrightarrow\quad
  \text{classically psh}
  \quad\Longleftrightarrow\quad
  \text{revised CLD psh}
\]

on a boundaryless space, and on the relative interior in general.  This is
R3-24.  It is not an identification with CLD-smooth functions and it is not a
BFJ--CLD global comparison theorem.

A global BFJ/BJ psh metric has local classically psh weights: its
Fubini--Study/model approximants are classically psh and the usc pointwise net
limit remains so. Conversely, a local classical psh function carries neither
a polarization nor transition data nor global finite-type approximation.
No theorem reconstructing an arbitrary global BFJ/BJ metric from such local
data was found. The older implication

\[
 d'd''[h]\geq0\text{ for }h\text{ PL}
 \quad\Longrightarrow\quad h\text{ semipositive}
\]

also remains open, because pullback stability of the current predicate is
unknown. It must not be conflated with the functorial transfinite CLD sheaf.

There is nevertheless a verified analytic slice.  If a regular sequence of
length (n-1) cuts out a pure-relative-dimension-one zero fibre (C) in a
good separated boundaryless strict (n)-fold, ambient positivity of
(\mathrm d'\mathrm d''[h]) implies nonnegative pairing of
(\mathrm d'\mathrm d''[h|_C]) against every test obtained by restricting a
nonnegative smooth compactly supported ambient function.  A tightly
supported ambient cutoff therefore detects a nonnegative isolated atom.  The
exact statement passed production run
`20260825T023505Z_66547f68ec32`, `gpt-5.6-sol`/`xhigh`, final `correct`, zero
critical errors, and zero gaps.  It neither extends arbitrary curve tests nor
supplies the residual-degree formula needed for the global converse; a
separate attempted global deduction was rejected for exactly that missing
smooth-curve/descent bridge.

### CLD-3. Independence in Bedford--Taylor products

**Status:** the sufficient criterion is VERIFIED; the unrestricted assertion
for arbitrary positive closed currents is DISPROVED on an abstract calibrated
tropical fan.

Let \(T\) be positive and closed, and let \(u,v\) be continuous psh functions
with \(d'd''u=d'd''v\). Put \(h=u-v\). If there are smooth functions
\(h_j\to h\) locally uniformly with \(d'd''h_j=0\), then formally
\[
 d'd''(hT)=\lim_j d'd''(h_jT)
            =\lim_j d'd''h_j\wedge T=0.
\]
Pass R2 confirmed that uniform convergence gives \(h_jT\to hT\) and that
differentiation is continuous on currents. Thus the displayed implication is
valid. It is only a sufficient criterion: it does not construct the smooth
pluriharmonic approximants.

The cross-fan calculation in CLD-4 gives continuous CLD-psh \(u,v\) with
equal Hessian currents and a positive closed current \(T\) for which
\(d'd''((u-v)T)\ne0\). Hence not every positive closed current is a
Bedford--Taylor current. This does not contradict CLD's recursive product,
which begins with \(\delta_X\) and remains inside the Bedford--Taylor class.

### CLD-4. Distributionally harmonic functions

**Status:** cell-interior result validated; unqualified gluing implication
refuted by Pass R2.

On the relative interior of one tropical cell, the distributional equations
for \(d'd''[u]=0\) force all second distributional derivatives to
vanish, hence \(u\) is almost everywhere affine and has a continuous affine
representative.

Cellwise affine regularity does **not** imply the global Bedford--Taylor
independence without a balancing theorem. On the abstract calibrated cross
fan
\[
 X=\mathbf R_{\ge0}(\pm e_1)\cup
   \mathbf R_{\ge0}(\pm e_2),
\]
put
\[
 u=2|x_1|,\qquad v=|x_1|+|x_2|,\qquad h=u-v.
\]
Both \(u\) and \(v\) are CLD-psh. This requires more than nonnegative outgoing
slopes: for \(\varepsilon_j\downarrow0\), they are the decreasing locally
uniform limits of the restrictions of the smooth convex functions

\[
  2\sqrt{x_1^2+\varepsilon_j},\qquad
  \sqrt{x_1^2+\varepsilon_j}+\sqrt{x_2^2+\varepsilon_j}.
\]

They have the same ambient outgoing slope sum.
Let \(T\) be the closed positive skeletal current of weight \(2\) on each
horizontal ray and \(1\) on each vertical ray. Then
\[
  d'd''(hT)=(2+2-1-1)\delta_0=2\delta_0\ne0.
\]
Thus the obstruction is exactly the change of face-balancing weights under
multiplication by \(T\).

**25 August boundary update:** the counterexample remains an abstract
Bedford--Taylor calculation, but its weighted geometry now has a genuine
analytic realization.  The proper tropicalization of
(V((x-1)(y-1))^{\an}) is exhausted by compact harmonic charts, and the
cycle (2[Y_h]+[Y_v]) gives the desired positive current.  The two curvature
measures are unequal at distinct Gauss points upstairs and become equal only
after proper pushforward.  Thus production run
`20260825T021353Z_058a4390b0fb` realizes the weighted configuration but does
not supply an analytic Bedford--Taylor counterexample.  The literal compact
full-cross chart is ruled out by run
`20260825T024519Z_16376e0d52eb`.

**25 August four-punctured-curve update:** a smooth connected candidate can
put the two curvature measures at the same analytic Gauss point, but it
cannot carry the proposed unequal current weights.  On
\((\mathbf P^1_K\setminus\{a,b,c,d\})^{\mathrm{an}}\), with pairwise
distinct reductions, the real-PL psh potentials satisfy
\(\mathrm d'\mathrm d''[U]=\mathrm d'\mathrm d''[V]=4\delta_q\).
After adjoining the third unit \((z-a)/(z-c)\), however, closedness gives
\((w_a-w_b,w_c-w_d,w_a-w_c)=0\), so all four ray weights are equal and
\((2,2,1,1)\) is impossible.  The exact packet passed guarded production
run `20260825T034743Z_ea6194f07e86`, item
`pi_19c9aad210847a2875a0fe4a`, final `correct`, with zero critical errors
and zero gaps.  This excludes only that concrete smooth-curve construction;
the unrestricted upstairs problem remains open.

**25 August real-PL update:** on a good separated boundaryless strict
pure-dimensional analytic space, a real-PL function with zero CLD
\(\mathrm d'\mathrm d''\)-current is GJR harmonic and classically
pluriharmonic.  The proof
uses rational coefficients of codimension-one calibrated skeletal currents
on common analytic refinements and therefore avoids both current pullback and
target-side boundary separation.  Its repaired exact-live packet passed
production run `20260825T061351Z_655e7f503e5d`, item
`pi_eea98ea0a54108cae4e076be`, final `correct`, with zero critical errors and
zero gaps.  The earlier boundary-separator proof returned final `wrong` in
run `20260825T031243Z_1603e0a83037` and remains quarantined.  This closes the
real-PL subproblem, not the arbitrary continuous higher-dimensional one.
Wanner's published comparison separately gives the continuous implication on
open subsets of smooth proper algebraic curves over algebraically closed
complete nontrivially valued fields.

**25 August harmonic-approximation update:** the literal request for ordinary
CLD-smooth harmonic approximants is false.  The Chapter 19 theta-curve example
is weakly smooth and harmonic but is not even a locally uniform limit of
ordinary CLD-smooth harmonic functions.  Its exact-live proof passed run
`20260825T055907Z_b5c8f0719b60`, item
`pi_d80993bb01a748f0422ae6a5`, final `correct`, with zero critical errors and
zero gaps.  The fixed-support proof uses zero curvature of every approximant;
that run did not decide ordinary CLD-smooth psh regularization.

**27 August ordinary-psh-regularization update:** the continuous
smooth-proper-curve case is now closed positively.  Over an algebraically
closed complete nontrivially valued field, current positivity, Thuillier
subharmonicity, and local decreasing ordinary CLD-smooth psh approximation
coincide for continuous functions on smooth proper algebraic curves.  The
exact statement and proof passed production run
`20260827T090645Z_767cbf81c723`, final `correct`, with zero critical errors
and zero gaps.  The approximants carry positive curvature in fresh tangent
directions, so the harmonic-approximant obstruction above remains valid.
Arbitrary singular curve functions, more general analytic curves, and higher
dimensions are not covered.

### CLD-5. Non-Archimedean Kähler forms and Kodaira theory

**Status:** open after Pass R1; structural warning established.

A definition by pointwise positive top-degree density is too restrictive:
top-degree CLD forms are skeletal, and even Fubini--Study Monge--Ampère
measures may be Dirac. The viable common notion appears to be numerical
ampleness together with positivity on models, but an intrinsic differential
Kodaira theorem remains to be formulated and proved.

### CLD-6. Further explicit questions retained for later passes

1. rational smooth extension from boundaries of rational cells;
2. finite-linear-combination versus distributional harmonicity;
3. collapse at stage one, or at another controlled early stage, of the
   transfinite hierarchy used in CLD's definition of psh functions (cardinal
   stabilization itself is already Lemma 8.1.4; Remark 8.1.6 is literally
   inconsistent if read as denying all stationarity);
4. enlargement of psh functions on abstract tropical spaces;
5. “very richness” of higher-dimensional unit polydiscs;
6. necessity of maximal-rank Abhyankar/Zariski-closed hypotheses;
7. precise Dolbeault/tropical-homology comparison;
8. analytic non-Archimedean Arakelov theory and a theory over
   \(\mathbf Z\).

These are lower priority for the core textbook, but they remain inside the
scoped research corpus because they occur explicitly in the current CLD text.

### CLD-7. Common local singular Monge--Ampère product

**Status:** model and joint bounded core VERIFIED in R3-26; two overbroad
signatures DISPROVED; the remaining natural extensions are OPEN.

For a smooth complex germ, base change to
\(K=\mathbf C((t))\), \(|t|=\mathrm e^{-1}\).  The Gauss extension realizes
the normalized BFJ link \(V_{\mathfrak m}\) as the shell
\(u_{\mathfrak m}=-1\).  If \(T\) is the product of \(n-1\) ideal model potentials,
or rational semipositive model potentials carried by an algebraizable common
log model, the swept measure

\[
  T\wedge \mathrm d'\mathrm d''\max\{u_{\mathfrak m},-1\}
 -\mathbf 1_{\{u_{\mathfrak m}>-1\}}
  T\wedge \mathrm d'\mathrm d''u_{\mathfrak m}
\]

is shell-supported.  On a common log resolution, its atom over \(E\) is

\[
 b_E((-A_1)\cdots(-A_{n-1})\cdot E),
\]

which is exactly the BFJ coefficient.  The proof computes the normalized
blow-up of \((t,\mathfrak m\mathcal O_Y)\) using CLD Theorem 18.5.5 and
Proposition 18.5.8, then compares with BFJ Proposition 4.9.  BFJ Proposition
4.8 and polarization extend the equality to the explicitly defined joint
bounded closure built from ideal/algebraizable model approximants.  The construction is local without renormalization
and satisfies the finite projection formula, with a variable radial factor
when changing the source reference ideal.  This functoriality is unconditional
for ideal inputs and conditional on pullback preserving the stated locus for
rational or bounded inputs.

The hostile source audit does not promote the receipt's unqualified analytic
model wording: polynomialization and admissible formal-model construction
are proved for the ideal locus, while the rational extension is retained only
on algebraizable common log models.  Removing this boundary is an additional
open problem.

Two boundary calculations limit the result.  The ideal
\((x^3,xy,y^2)\) on a twice-blown-up smooth surface produces two unit atoms,
so probability normalization is incompatible with literal restriction.  The
ideals \((y,x^k)\) give full monotone limits charging a polar endpoint while
their nonpluripolar truncations vanish.  Thus an unrestricted unbounded
extension is not uniquely forced.

**Receipt:** statement digest
`923e70de7a01fd5db358b35d509323b33a9bd9d586003bb0498fd8663bc7820a`;
proof digest
`64776c912e47b1c0ac68fa2e26e316f855a72ed6b94dc720f8d25e9d1957112c`;
`gpt-5.6-sol`, `xhigh`, final verdict `correct` with zero gaps.

The open remainder is now precise: arbitrary bounded classical psh functions
outside the joint realization, a capacity/finite-energy rule for polar mass,
rational models on nonalgebraizable analytic modifications, and singular or
nonnormal germs.

### CLD-8. Early collapse of the psh hierarchy

**Status:** verified on tropical toric partial compactifications and every
finite ambient-induced real-affine star; open in the unrestricted scope.

CLD Lemma 8.1.4 proves eventual stabilization by a cardinality argument.
Remark 8.1.6 literally says stationarity is unknown, contradicting that
lemma, but immediately gives the intended analytic content: in complex
geometry stage one suffices, and every non-Archimedean example known there
also lies at stage one. The meaningful question is therefore whether
\(\operatorname{Psh}_{X,1}=\operatorname{Psh}_X\), or whether a finite or
otherwise uniformly controlled early ordinal suffices on natural classes of
affine refined tropical spaces. No second-stage example is known at the
cutoff. Eventual set-theoretic stationarity is not an open problem.

The first natural cases are now closed.  On every tropical toric partial
compactification with the standard Lagerberg smooth structure, the toric psh,
CLD psh, and first-stage CLD psh sheaves coincide.  Stage one also suffices on
a one-dimensional boundaryless affine tropical space locally modeled on a
finite balanced complex with ambient-induced smooth structure.  That earlier
packet passed production run
`20260825T024707Z_d1b8d7eaf79e`, `gpt-5.6-sol`/`xhigh`, final `correct`, zero
critical errors, and zero gaps.

The stronger finite-star theorem removes rationality, weights, balancing,
calibration, harmony, and boundary designation from the abstract model.  For
any finite union of distinct half-open rays in a finite-dimensional real
vector space, with ambient-induced smooth branchwise-convex generators, it
identifies the first stage and the full generated psh sheaf with branchwise
extended-real convexity plus all junction Jensen inequalities and constructs
decreasing smooth approximants on one fixed neighbourhood.  Its exact bytes
passed the direct production endpoint using `gpt-5.6-sol`/`xhigh`, final
`correct`, zero critical errors, and zero gaps; the response is archived
under the local label `20260827T103835Z_c8131b22d800`, and the endpoint
assigned no run or item identifier.  The theorem does not identify arbitrary
positive-sedentarity or nonambient generator sheaves with its model.
Higher-dimensional spaces, such boundary structures, and infinite-valence
stars remain open.

### CLD-9. Local psh metrics versus global psh metrics

**Status:** two primary-source questions in CLD Remark 17.8.10; open.

The first asks whether every continuous locally CLD-psh metric on a
projective variety is globally psh in CLD's uniform smooth-approximation
sense. The second asks whether Corollary 17.8.9 extends to a proper strict
analytic space possessing a formal model with projective special fibre:
every parlinear metric should then be globally dpsh. The second is not
literally the same as the first and must not be replaced by a modern
Fubini--Study definition without a comparison theorem.

### CLD-10. The resolved Gubler--Jell--Rabinoff delta-metricity question

**Status:** resolved.  The formerly bundled cohomology-isomorphism and
semipositive integral-decomposition questions are also resolved in their
literal unrestricted formulations.

The final residual asked whether a canonical metric on a line bundle on an
abelian variety is an ordinary \(\delta\)-metric, with non-isotrivial mixed
reduction as the essential boundary case.  The answer in that residual range
is no.  The product--Gauss criterion proves that a nondegenerate quadratic
weight on an equivariant locally integral-PL map is ordinary delta exactly
when every coordinate of that map is CLD-smooth.  Applied to split Raynaud
uniformization, an ample cubical metric is ordinary delta exactly when the
residual Raynaud extension is isotrivial.  The exact statement and proof
passed production run `20260826T055627Z_b68659fba1be`, item
`pi_75c74fac9a98efc3719b9773`, using `gpt-5.6-sol` at `xhigh`, final
`correct`, zero critical errors, and zero gaps.  The preceding Picard
reduction settles `Pic^0`, separates symmetric and antisymmetric factors, and
shows that the ample symmetric range was the last universal case on a fixed
abelian variety.

The low-residual-dimension theorem uses a common residue model and an
integral B\'ezout splitting of its single degree functional.  Source-aware
exact-current production run `20260824T135721Z_81346238f7dd` returned final `correct`, zero
critical errors, and zero gaps.  It includes all good strict analytic curves,
allows boundary points, and imposes no relation between the coefficient
group and the value group.

In arbitrary residual dimension,
`thm:p09-signed-semipositive-span` proves signed generation by semipositive
integral germs, while
`cor:p09-good-reduction-positive-cone-counterexample` disproves the natural
nonnegative-coefficient version on a good-reduction abelian surface.
Production runs `20260825T130036Z_c1607c25ec38` and
`20260825T130707Z_4c4a1f2c885f`, both with `gpt-5.6-sol` at `xhigh`,
returned final `correct`, zero critical errors, and zero gaps.  Thus the
integral-decomposition atom is retired; the signed statement is not a
semipositivity characterization.

For chronology, Section 1.15 also asks whether
\(\Lambda^{p,q}M_{\mathbf R}\to H^{p,q}(A)\) is always an isomorphism.  The
literal unrestricted answer is no: a good-reduction elliptic curve has
\(M_{\mathbf R}=0\), while GJR Theorem 1.14 gives
\(\dim_{\mathbf R}H^{1,1}(A^{\mathrm{an}})=1\).  The complete proof is
Proposition `prop:ch18-gjr-cohomology-counterexample` in Chapter 18.  Its exact-current
production run `20260824T123617Z_fcddc3abc33d` returned final `correct`, zero
critical errors, and zero gaps.  The counterexample does not decide the
totally degenerate restriction.

### CLD-11. Exact balanced-polyhedral questions and book strengthenings

**Status:** three primary-source questions are open; the two comparison
targets following them are book-formulated; prepared Rethlas packet not run.

Botero--Mazzon--Pille-Schneider ask for higher-dimensional polyhedral
smoothness hypotheses that guarantee regularity and orthogonality, for a
characterization of the polarized Calabi--Yau degenerations whose
tropicalizations have those properties, and, in Remark 6.27, for a
classification of the matroids whose Bergman fans satisfy orthogonality.
These are the exact source questions.  The complete affine calculation in
R3-27 answers none of them in their singular intrinsic scope.

The manuscript's intrinsic singular-fan contact problem and its request for
a recursive calibrated CLD/non-Archimedean comparison theorem are stronger
book-formulated questions.  They are motivated by the source but must not be
attributed to it verbatim.  Likewise, the four-ray cross only disproves the
claim that strict positivity of a reference function by itself forces
orthogonality; it is not a counterexample to every prospective smoothness
package.

---

## 10. Complex/transcendental and YTD questions

### CX-1. The missing Calabi--Yau theorem in MP24

**Status:** historically resolved.

Mesquita-Piccione--Witt Nyström (2025) prove continuity of envelopes,
orthogonality, strong-topology results, a transcendental non-Archimedean
Calabi--Yau theorem, regularity for measures supported on dual complexes, and
uniform K-stability for models implying a unique cscK metric.

### CX-2. General compact Kähler YTD equivalence

**Status:** split by signature at the 15 August 2026 cutoff.  The smooth
polarized projective automorphism-relative uniform statement is claimed by
Trusiani arXiv:2605.30063v1, Theorem A, and Corollary B reports the
equivalence of the standard smooth polarized projective stability
formulations listed there.  The bare comparison among those projective
signatures must therefore not be recycled as an open problem.  Direct
algebraic proofs, equivariant transcendental formulations, the
nonprojective compact-Kähler frontier, and singular-space extensions remain
open in the exact senses below.

Uniform K-stability for models is stronger than the original condition using
the narrower class of test configurations.  The September 2025
Boucksom--Jonsson and Darvas--Zhang preprints and MPWN use different
non-Archimedean, \(K^\beta\), log-discrepancy-model, or model-stability
signatures.  Their comparison maps and normalizations must be proved rather
than identified by vocabulary.  No statement in MPWN is relabelled as the
complete projective or transcendental YTD conjecture.

### CX-3. Current 2026 projective YTD claim

**Status:** recent primary-preprint claim, source boundary checked; not
independently reproved by Pass R3.

Trusiani arXiv:2605.30063v1 (28 May 2026) states: Theorem B for special
Fujita approximations of a big line bundle on a smooth projective variety;
Corollary A for equivariant entropy regularization by smooth ample test
configurations from a dominating snc model; and Theorem A for the
\(\operatorname{Aut}^{\circ}(X,L)\)-uniform YTD equivalence on a smooth
polarized projective variety.  Corollary B reports the corresponding
equivalence of the standard smooth polarized projective signatures,
including the log-discrepancy-model, model, and b-K-polystability
formulations specified in that source.  It does not state the nonprojective
Kähler or singular analytic extension.  The textbook may report these exact
claims with their version/date, but must not silently identify their
normalizations with MP--MPWN, Boucksom--Jonsson weighted, or Darvas--Zhang
objects outside the common scope actually covered by Corollary B.

### CX-3a. Exact post-2025 YTD residual questions

**Status:** primary-source questions and book-separated extension targets;
open; prepared Rethlas packet not run.

Boucksom--Jonsson's section “Questions and further remarks” asks for a direct
algebraic proof of the equivalence between b-K-polystability and uniform
stability, a dimension-dependent bound on the support size of divisorial
test measures, algebraic proofs of equivariance, an extension to polarized
klt pairs, and a nonprojective Kähler extension.  Darvas--Zhang leave the
regularization by test configurations of rays attached to log-discrepancy
models and the equivariant transcendental extension, especially for a
nontrivial group, as residual problems.  Trusiani's Corollary B removes the
undifferentiated smooth projective signature-comparison question but does not
supply those direct algebraic, transcendental, equivariant, or singular
extensions.

The genuinely hybrid compactness and measure-continuity bridge used in the
book is a book-formulated synthesis problem, not a question quoted verbatim
from any one of these sources.  It is recorded separately from the preceding
primary-source questions.

### CX-4. General big-class ample-locus regularity

**Status:** open after literature Pass R1.

For a non-nef big class, the expected smoothness on the ample locus of a
Monge--Ampère solution with smooth positive density remains a live benchmark.
The nef-and-big theorem does not settle this formulation.

### CX-5. Local finiteness of nonpluripolar products beyond the Fujiki class

**Status:** open after literature Pass R1.

This question is directly relevant only to the proposed non-Kähler extension;
it will not be allowed to complicate the main compact-Kähler theory.

### CX-6. Uniform algebraic approximation of supercanonical envelopes

**Status:** open after Pass R1.

When \(K_X+L\) is merely big, the desired uniform approximation is tied to
abundance-type behaviour on restrictions. This enters the book only if the
big-class quantization discussion needs it.

### CX-7. Competing big-class test configurations

**Status:** open comparison programme.

DXZ flag configurations provide one workable notion for a big class. Their
relationship with alternative algebraic or analytic notions of big test
configuration must be stated construction by construction; no universal
equivalence was found.

---

## 11. Historically closed items not to recycle as open problems

1. independence of \(\mathcal I\)-goodness from the background form: solved
   immediately after it is raised in the first archive;
2. uniqueness in the full complex class \(\mathcal E(X,\omega)\): later
   settled;
3. monotonicity of nonpluripolar products in the needed compact-Kähler form:
   proved by Darvas--Di Nezza--Lu;
4. log-concavity of total nonpluripolar masses: proved by
   Darvas--Di Nezza--Lu;
5. existence of smooth weak geodesics between arbitrary smooth endpoints:
   false in general by counterexample;
6. algebraizability in the residue-characteristic-zero BFJ equation: removed
   by later work;
7. the MP24 Calabi--Yau gap: filled by MPWN 2025;
8. eventual set-theoretic stationarity of the CLD transfinite psh hierarchy:
   proved by the cardinal argument in CLD Lemma 8.1.4; only stage-one or
   controlled-early collapse remains open despite the wording of Remark
   8.1.6;
9. the expectation that a divisorial Green function, or every finite atomic
   Monge--Ampère solution supported on a dual complex, must be model/PL or
   factor through an SNC retraction: disproved by Boucksom--Jonsson (2024),
   Theorems A--B;
10. the two local-volume questions for isolated Gorenstein singularities:
    Yuchen Zhang (2014) proves a positive dimension-only lower bound for
    every nonzero BdFF volume, while the implication “volume zero implies the
    existence of a log-canonical \(\mathbf Q\)-boundary” is false in the
    non-\(\mathbf Q\)-Gorenstein setting by the counterexample in that paper;
11. independence of Xia's limit partial Okounkov body from the auxiliary
    ample divisor \(H\) and Kähler form \(\omega\): asserted in Section 5.6;
    this does not answer the separate auxiliary-\(\eta\) question for the
    Chebyshev transform at the end of Section 6.4;
12. the undifferentiated equivalence of the standard smooth polarized
    projective stability signatures listed in Trusiani's Corollary B: a
    dated 2026 preprint claim, not a remaining open item.  Direct algebraic,
    transcendental, equivariant, hybrid, and singular extensions remain open.
13. the unrestricted GJR abelian-cohomology isomorphism question: disproved
    by the good-reduction elliptic curve in Chapter 18, with exact-current run
    `20260824T123617Z_fcddc3abc33d`; the totally degenerate refinement remains
    open;
14. the BFJ generalized-Lelong converse for psh germs at a smooth complex
    point: the exact frozen statement and source-aware proof passed
    `20260824T140127Z_ef8316d19c12`, and an independent hostile audit found no
    defect before Chapter 70 integration.  Primary-ideal weights already
    separate pointwise valuative transforms.  This is a dated book-level
    derivation, not a novelty or priority claim, and the run was not a
    post-integration byte-identity gate.

---

## 12. Ordered Rethlas research queue

All passes below use `gpt-5.6-sol` at `xhigh` effort. Each successful solver
pass is followed by a separately prompted hostile audit.

### Queue A. Proofs already claimed or nearly closed

1. envelope proof audit I: definitions, dependency graph, and circularity;
2. envelope proof audit II: smooth positive-characteristic test ideals;
3. envelope proof audit III: determinant norms, finite descent, alterations;
4. envelope proof audit IV: universal-homeomorphic normalization by
   characteristic;
5. \(P\)-valued trace refinement (open; no theorem promoted);
6. toric zero-mass numerical-dimension theorem;
7. \(\mathcal I\)-invariant refined-body no-go theorem;
8. product/retraction trace Dirichlet proposition;
9. CLD harmonic-reduction lemmas (real-PL zero-current case verified by
   `20260825T061351Z_655e7f503e5d`; arbitrary continuous higher-dimensional
   case remains open; continuous ordinary CLD-smooth psh regularization on
   smooth proper algebraic curves is verified by
   `20260827T090645Z_767cbf81c723`, while arbitrary singular or more general
   curves and higher dimensions remain open; the literal harmonic
   approximation variant is disproved by `20260825T055907Z_b5c8f0719b60`);
10. fixed-dual-complex special case of BJ Question 11.16.

### Queue B. Tractable special cases

1. trace Dirichlet for analytic singularities and split normal bundles;
2. quantitative Ohsawa--Takegoshi estimates uniform in tensor power;
3. closure removal for curves, toric flags, and flags admitting holomorphic
   retractions;
4. big-line-bundle projection removal under finite generation;
5. zero-mass \(P\)-model and \(\mathcal I\)-goodness on toric varieties and
   surfaces;
6. CLD harmonic regularization on tropical manifolds before singular
   polyhedral spaces;
7. local FS-envelope continuity on polystable and smooth tropical charts.

### Queue C. Large structural problems

1. general trace Dirichlet;
2. unibranch complex trace and equisingular regularization;
3. general zero-mass Okounkov construction;
4. unrestricted nontrivially valued Monge--Ampère solvability;
5. reverse local-to-global reconstruction beyond the semipositive/model core;
6. intrinsic non-Archimedean Kähler/Kodaira theory;
7. the residual compact-Kähler YTD bridge: direct algebraic,
   equivariant-transcendental, singular, and hybrid compactness statements
   after the dated 2025--2026 claims;
8. construction-by-construction non-Kähler and higher-bidegree programmes.

Queue C receives serious attacks, but its size is not evidence that a short
model-generated proof should exist.

---

## 13. Promotion checklist for a new theorem

A candidate result can enter the research-frontier chapter or an earlier
thematic chapter only
after all boxes are checked:

- [ ] exact statement and notation fixed;
- [ ] proof written without phrases such as “clearly” at the critical step;
- [ ] every external theorem checked in its primary source;
- [ ] no circular dependency on the target result;
- [ ] zero-mass and \(-\infty\) cases checked;
- [ ] singular/non-normal/non-unibranch examples checked where applicable;
- [ ] positive-characteristic and inseparability issues checked where
      applicable;
- [ ] nets versus sequences checked;
- [ ] divisorial equality versus equality on all semivaluations checked;
- [ ] curve and toric test examples computed;
- [ ] hostile independent audit passed;
- [ ] full Rethlas receipt records the exact signature, independent proof,
      adversarial audit, boundary/counterexample search, source/novelty
      separation, and final verdict;
- [ ] every newly proved statement has a numbered, unnamed heading; a
      parenthetical title is retained only for a literature-established name
      with a primary-source anchor;
- [ ] every theorem, lemma, proposition, and corollary has a complete proof in
      the manuscript, or is explicitly marked as an imported deep theorem
      with an exact primary-source anchor; no proof is silently omitted;
- [ ] there are no exercise sections or exercise environments anywhere in the
      manuscript (open `problem` environments in the research-frontier chapter
      are status statements, not exercises);
- [ ] provenance recorded in the mathematical revision log.

---

## 14. Pass R3 verified disposition

The complete receipts, primary-source links, theorem anchors, and proposed
chapter edits are in
[the R3 verification report](manuscript/editorial/rethlas_r3_report.md).
The statement-by-statement expansion queue required by the no-silent-proof
release rule is maintained in
[the full-proof audit](manuscript/editorial/full_proof_audit.md).
The following table is the release-facing index. A row is not a substitute
for its full receipt.

| Receipt | Question or candidate | R3 disposition |
|---|---|---|
| R3-01 | literal equality of smooth CLD, semipositive PL, current-psh, classical psh, and global BFJ/BJ psh | **DISPROVED** already on a tropical interval and by the local/global signature mismatch |
| R3-02 | semipositive PL versus classical PL psh | **VERIFIED** for complete nontrivially valued \(k\), good strict spaces, and \(\mathbf R\)-PL functions |
| R3-03 | maximum principle for the 2025 CLD psh sheaf | **VERIFIED** as a consequence of the submitted GR-C primary preprint's CLD-to-classical comparison and maximum principles |
| R3-04 | current-psh PL implies semipositive PL | **OPEN** globally; the regular complete-intersection slice against ambient tests is **VERIFIED** by `20260825T023505Z_66547f68ec32`, while the attempted degree--atom completion was rejected |
| R3-05 | curve comparison and regularization | **VERIFIED** with weakly smooth nets in general smooth boundaryless curve scope; ordinary CLD-smooth harmonic approximation is **DISPROVED** by the later exact-live curve construction, while unrestricted ordinary CLD-smooth psh regularization is **OPEN** |
| R3-06 | global BFJ/BJ psh gives local classical weights | **VERIFIED** for the FS/model-net definitions; the reverse arrow is **OPEN** |
| R3-07 | raw local FS envelope | **VERIFIED** for a nonempty pointwise-bounded-above family when the raw supremum is already usc; the unconditional classical-psh, CLD-v2-psh, and continuity conclusions after usc regularization are **DISPROVED** on a reduced strict nodal affinoid curve by `prop:ch15-nodal-local-envelope` and production run `20260825T094005Z_10ac70696f69`; sharp normal/analytically-unibranch classification remains **OPEN** |
| R3-08 | probability-valued local MA sheaf with literal restriction | **DISPROVED** by disjoint opens |
| R3-09 | full local BJ/CLD/GR theory | **OPEN** beyond the R3-26 smooth algebraizable-model and joint bounded comparison, especially for arbitrary classical psh data, nonalgebraizable analytic models, unbounded finite energy, and singular germs |
| R3-10 | MP--DXZ finite-energy comparison | **VERIFIED** for compact Kähler \(X\), Kähler class, fixed initial potential, and \(\mathcal I\)-maximal finite-energy objects |
| R3-11 | unchanged MP signature for a big non-Kähler class | **DISPROVED**; a relatively Kähler class restricts to a Kähler fibre class |
| R3-12 | unchanged MP probability/energy theory at zero volume | **DISPROVED**; the normalization divides by zero |
| R3-13 | reconstruct DXZ from only a tail of large Kähler MP shifts | the formal cofinality argument is **DISPROVED** by the variance; existence and uniqueness of extension for the actual DXZ envelope system remain **OPEN** |
| R3-14 | Bingener/SS comparison | **VERIFIED** for interiorly locally finite-type Stein-algebra schemes: analytification, flat/completion comparison, and interiorly proper direct images; coherent algebraization near an excellent Stein compact also requires interior separation and proper support, while finite étale Riemann existence requires interior finite type; no positivity or MA consequence |
| R3-15 | Berndtsson superforms as a Berkovich comparison theorem | limited Euclidean convex integration **VERIFIED**; the asserted Berkovich comparison is **DISPROVED** as attribution |
| R3-16 | CLD uniform pluriharmonic-approximation criterion | **VERIFIED** for continuous multipliers and order-zero positive closed currents |
| R3-17 | cross-fan obstruction | **VERIFIED** on the abstract calibrated fan; the compact full-cross chart is **DISPROVED**, and the proper noncompact weighted analytic realization is **VERIFIED** by the first two 25 August production runs; a third guarded run excludes the four-punctured smooth-\(\mathbf P^1\) unequal-weight candidate by refined balancing; the unrestricted upstairs-equality problem remains **OPEN** |
| R3-18 | fixed-dual-complex topology | **VERIFIED** for smooth projective \(X\) in characteristic zero; arbitrary characteristic remains **CONDITIONAL/OPEN** |
| R3-19 | \(\mathcal I\)-class trace factorization and split product | **VERIFIED** in the displayed smooth/submanifold and split-class domains; a \(P\)-valued trace refinement is **OPEN** |
| R3-20 | toric Cao dimension formula | **VERIFIED** for integral/rational big toric data after the live Guenancia/toric-count citation and limsup-versus-limit repair; the real transcendental extension remains **OPEN** |
| R3-21 | \(\mathcal I\)-invariant mass-body assignment | **DISPROVED** by the polar-Cantor pair; a \(P\)-sensitive refinement remains **OPEN** |
| R3-22 | singular higher-dimensional CLD/GR Bedford--Taylor products | **OPEN** beyond continuous CLD, Euclidean convex, curve, and model loci |
| R3-23 | harmonic/pluriharmonic comparison | sourced weakly smooth and regular-model cases are **VERIFIED**; the real-PL zero-CLD-current converse is **VERIFIED** by exact-live run `20260825T061351Z_655e7f503e5d`; ordinary CLD-smooth harmonic approximation is **DISPROVED** by `20260825T055907Z_b5c8f0719b60`; continuous ordinary-smooth psh regularization on smooth proper curves is **VERIFIED** by `20260827T090645Z_767cbf81c723`; arbitrary singular curves, higher dimensions, arbitrary continuous zero-current functions, and unrestricted classical pluriharmonicity remain **OPEN** |
| R3-24 | model-semipositive, classical-psh, and revised-CLD-psh real PL functions | **VERIFIED** on complete nontrivially valued fields and good strict boundaryless spaces, or on the relative interior in general; separatedness is needed only for the one-way current consequence |
| R3-26 | swept CLD boundary product versus local BFJ measure | **VERIFIED** for ideal model functions, algebraizable rational-semipositive model functions, and their stated joint bounded closure; the probability-sheaf signature and canonical selection of arbitrary unbounded polar mass by the model comparison alone are **DISPROVED**; nonalgebraizable analytic models and broader psh/singular domains **OPEN** |
| R3-27 | balanced polyhedral regularity, orthogonality, and realization | all-dimensional regularity and orthogonality on the complete affine space (N_{mathbf R}) are **VERIFIED**; strict positivity alone is **DISPROVED** on the singular four-ray cross; analytic comparison is **CONDITIONAL** on recursive calibrated current compatibility; the intrinsic higher-dimensional singular-fan contact problem is **OPEN** |

### Boundary rules fixed by Pass R3

1. Do not identify \(\mathcal I\)-equivalence with \(P\)-equivalence.
2. Do not pass from sequences to nets, or conversely, without a metrizability
   input.
3. Do not call a positive-current predicate functorial unless pullback has
   been proved; this is the obstruction in R3-04.
4. Do not normalize a zero-mass local or global measure to probability
   without adding new reference data.
5. Do not extend a relatively Kähler model theory to a non-Kähler big class
   by changing only the symbol for the class.
6. Do not infer a Berkovich realization from an abstract calibrated tropical
   calculation.
7. Do not use Bingener/SS beyond finite-presentation, excellence,
   separation, and properness/proper-support hypotheses, and do not extract
   positivity from those comparison theorems.
8. Do not promote any new claim without the complete Rethlas receipt above.
   New results receive numbered headings only; descriptive parenthetical
   titles are forbidden unless the name is already established and sourced.
9. Do not leave a theorem, lemma, proposition, or corollary without a complete
   proof unless the statement is visibly marked as imported and carries its
   exact primary-source anchor.  Exercises are forbidden throughout the book;
   research-frontier `problem` environments remain permissible because they
   assert open status rather than assign work to the reader.

---

## 15. Cutoff additions and prioritized Rethlas queue

The full natural frameworks, dates, partial results, and adversarial tasks are
spelled out in Section 7 of the
[R3 verification report](manuscript/editorial/rethlas_r3_report.md).  This is
the compact release-facing index.  `P0` means essential to the unified theory,
`P1` a major extension with a verified core, and `P2` a sharp secondary
question.

The former BFJ generalized-Lelong-converse row has been retired from the
active queue.  In the smooth-germ framework, primary-ideal tests suffice to
force pointwise equality of valuative transforms; production run
`20260824T140127Z_ef8316d19c12` and the independent hostile audit are recorded
above.  Singular and nonnormal germs remain in the separate functorial local-
theory row.

| Priority | Open target and controlling primary source | Concrete next Rethlas task | Live-book status |
|---|---|---|---|
| P0 | Full local CLD/classical/LFS comparison beyond PL; CLD v2 (25 July 2025), GR-PL/GR-C (2025), GJR (2026) | Prove decreasing local-FS regularization or construct a strict higher-dimensional counterexample; audit boundary, scalar extension, and nonmetrizable cases | Chapter 72 proves only the PL core and records the remaining interface |
| P0 | CLD local-to-global psh metrics; CLD Remark 17.8.10 | Treat separately global smooth-psh approximation on projective varieties and the parlinear-dpsh assertion on proper strict spaces with projective formal special fibre | Primary-source questions; Chapter 72 states both exactly |
| P0 | Common singular local MA product; CLD §§8.5--8.7 and Theorem 18.5.5, BFJ08 Propositions 4.6/4.8/4.9, BMPS 2603.08664v1 | R3-26 proves the smooth ideal/algebraizable-model and joint bounded comparison; next remove the analytic-model algebraizability boundary, characterize the closure, and find a capacity/energy rule for polar mass | Chapter 72 proves the Gauss-shell comparison and records the remaining scope |
| P0 | Local FS envelopes and gluing; GR-C Theorem 6.5 and global BJ envelopes | Classify geometric hypotheses, beginning with normal or analytically unibranch domains, under which usc regularization preserves classical psh; then treat CLD-v2 psh for usc obstacles and continuity for continuous finite obstacles separately | The unconditional assertions are disproved by `prop:ch15-nodal-local-envelope` and run `20260825T094005Z_10ac70696f69`; the positive classification is open |
| P0 | MP realization of big/pseudoeffective DXZ data; DXZ (CMH 2025), MP (Adv. Math. 2025), Xia operations | Build a relatively big/nef model category with intersections, envelopes, orthogonality, and exact \(\mathcal I\)-comparison | Chapter 72 records the Kähler comparison and no-go boundaries |
| P0 | Nontrivially valued MA existence and the arbitrary-field \(\mathcal E^1\) operator; BFJ and Pille--Schneider Remark 4.4 | Separate operator construction from solvability; remove one field/singularity/support hypothesis at a time and reconstruct every variational input | Exact source question and broader book programme are separated in Chapter 72 and this ledger |
| Resolved history | BJ global Radon--Riesz, BJ Question 11.16 | Moving-centre valuations on \(\mathbf P^n\), \(n\ge2\), give weak convergence and identical exhaustion value one but a uniform strong gap | Disproved by `thm:ch49-global-radon-riesz-counterexample`; the fixed-SNC-complex positive theorem remains valid |
| P1 | Singular/nonnormal local valuative theory; BFJ08, Bingener 1976, Xia *Stein spaces* (3 July 2026) | Test normalization, conductor, and finite-map descent on nodes, cusps, quotient and inseparable germs | Chapter 72 treats the smooth BFJ endpoint only |
| Resolved history | GJR canonical ordinary \(\delta\)-metricity | The product--Gauss criterion detects ordinary delta-metricity coordinatewise and, for ample cubical metrics, by isotriviality of the residual Raynaud extension | The non-isotrivial mixed-reduction answer is negative by `20260826T055627Z_b68659fba1be`; P09.1 and unrestricted cohomology surjectivity are separately retired |
| P1 | DXZ filtration-test-curve maximality, Xia Conjecture 5.29, and auxiliary-\(\eta\) independence | Start with finitely generated/toric/flag cases; do not recycle the already asserted \(H,\omega\)-independence or the now-proved positive-volume Conjecture 8.8 | The residual source-scoped packets remain open; Conjecture 8.8 is closed in its exact Chapter 55 positive-volume scope by separate exact-current gates |
| P1 | Banach-family MA continuity; Pille-Schneider, JEP 10 (2023), Question 4.9; the Favre--Pille-Schneider endpoint question is retained only as resolved history | Prove FS specialization or produce a non-hybrid jumping base for Question 4.9 | `thm:hybrid-endpoint-continuity-counterexample` disproves both literal Question 3.18/Favre Question 1 and the zero-supremum normalized strengthening; the stronger packet passed production run `20260825T035945Z_070e264c3ef1`, item `pi_db89dd432acabcf33a3f2272`, and the adapted exact-live bytes passed `20260825T043840Z_d77f7f93aeb0`, item `pi_b7f015a6ad5570f431769a71`, both `final/correct`, while Question 4.9 remains open |
| P1 | BMPS higher-dimensional smoothness, Calabi--Yau tropicalizations, and Bergman-fan matroid classification | Test intrinsic contact and orthogonality on singular smooth fans; keep the recursive analytic comparison as a stronger book question | Exact source questions and book strengthenings are separated; R3-27 solves only the complete affine case |
| P1 | Exact post-2025 YTD residuals; BJ 2509.15016v1, Darvas--Zhang 2509.15173v2, Trusiani 2605.30063v1, MPWN25 | Direct algebraic bridge, bounded divisorial support, algebraic equivariance, log-discrepancy-ray regularization, and transcendental/singular/hybrid extensions | Trusiani Corollary B removes the bare smooth-projective signature question; Chapter 72 lists only residuals |
| P1 | Zero-volume relative energy/MA and \(P\)-sensitive bodies; DXZ/Xia/MP | Test first-nonzero-volume-coefficient rescaling for path independence and numerical dimension | Chapter 72 proves the probability and \(\mathcal I\)-body no-go boundaries |
| P2 | Early collapse of the CLD transfinite psh hierarchy; CLD Lemma 8.1.4/Remark 8.1.6 | Extend the verified toric and finite ambient-induced real-affine-star cases to arbitrary non-toric positive-sedentarity or nonambient structures, higher-dimensional spaces, or infinite stars, or exhibit genuine transfinite rank | Eventual stabilization, the toric case, and the finite ambient-induced star case are closed; the latter passed the direct production endpoint and is archived under `20260827T103835Z_c8131b22d800`; Chapter 72 retains the unrestricted residual |
| P2 | Exact canonical BJ approximation and threshold identities after Trusiani 2026 | Identify Trusiani's approximants term by term with the prescribed BJ sequence and normalize every threshold | Earlier chapters provide machinery; Chapter 72 does not identify them |

The live Chapter 72 has 15 open-problem environments.  The book-wide literal
count is 16 because the preceding pseudoeffective MP--DXZ chapter separately
contains the projective-rational full-link problem.  These are
research-status records, not exercises.  The earlier trace-refinement row has
been removed: the complete supplied Darvas--Xia chapter proves the required
input-\(\mathcal I\)/output-\(P\) factorization, so Chapter 72 now records it as
resolved source history.  Splitting compound environments into independently
auditable targets gives 55 active atoms; their exact crosswalk and easy-to-hard
queue are recorded in
`manuscript/editorial/open_problem_atomic_inventory_20260824.md`.  The
production receipts distinguish exact-current gates from frozen
pre-integration gates.  They include the exact-current Chapter 18, 23, 49,
55, and 69 checks; the frozen Chapter 70 generalized-Lelong and real-toric
checks; and the P18 sequence consisting of the original scalar packet, its
exact-current gate, and the stronger normalized packet.  The last of these,
run `20260825T035945Z_070e264c3ef1`, item
`pi_db89dd432acabcf33a3f2272`, controls the theorem that retires the
normalized atom mathematically; the exact adapted live bytes additionally
passed run `20260825T043840Z_d77f7f93aeb0`, item
`pi_b7f015a6ad5570f431769a71`.  The real-toric atom is likewise retired: the current-level
identity is proved in every pseudoeffective real class, while the class-level
reading is disproved.
The remaining source-scoped packets in the table have no
promotable proof receipt unless an individual entry explicitly says
otherwise.
