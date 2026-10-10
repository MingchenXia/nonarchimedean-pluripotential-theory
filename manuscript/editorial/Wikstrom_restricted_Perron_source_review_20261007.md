# Globally bounded minorants and pointwise Perron envelopes: exact-source review

Date: 7 October 2026. Baseline and explicitly fetched `origin/work`:
`854e9336b2b78f63f1d5dedf1ad651c7f1a7aaba`; fetched `origin/main`:
`00957114db21b627e97369563032ceda9cea09c7`.

Wikström arXiv:2607.24139v2 distinguishes a restricted pointwise envelope
from its upper semicontinuous regularization. In real potential theory the
restricted subharmonic envelope is already upper semicontinuous. In complex
dimension at least two, a positive pluriharmonic obstacle on a bounded
B-regular Hartogs domain has a restricted plurisubharmonic envelope which
loses every value on an interior analytic disc, despite bounded approximation
off that pluripolar set and a strong pole-valued majorant.

Both main versions were read completely as matching selected text and
individually displayed images: nine controlling v2 pages and eight comparison
v1 pages. Five dependencies contribute 34 further actual source/page pairs.
The total is **51 source/page pairs on 27 sheets**, all fresh, across seven
PDFs: two complete main readings and five partial dependency readings.
Twenty-four exact algebra, sign and quantifier diagnostics accompany the
reading. This is an attributed source audit, not an independent model receipt
or a certificate for every external Dirichlet proof chain.

The 4,480-page book, its active inputs, bibliography, index, canonical
inventory and historical native catalogue/editor are unchanged at this
source-only checkpoint. A checked Appendix H continuation can follow after
its own compilation and actual matching-page review.

## Controlling files and reading scopes

| Primary file | Actual pages read | PDF SHA-256 |
| --- | --- | --- |
| Wikström 2607.24139v2, *Perron envelopes with globally bounded minorants*, 29 September 2026, 12:05:49 UTC | 1--9, complete | `8e7c02d53d3889afd7adc9dc30ececc0f7c020142ee81dd036572f494da5e385` |
| Wikström 2607.24139v1, *Restricted Perron envelopes and quasibounded functions*, 27 July 2026, 08:19:08 UTC | 1--8, complete | `beebade3c756bcae74bd6f14c62df7ecf1dcf445956b8e29b419f5437d45654d` |
| Nilsson, published Math. Z. 301 (2022), 3959--3971, DOI 10.1007/s00209-022-03043-2 | 1--4 of 13 | `4e044740670286b8a302e2c48258e14266244f4c8d0c4e60fa64dd2ca0eeb71d` |
| Nilsson 2109.13625v1, 28 September 2021 | 1--4 of 12 | `dd3687da4ffe05777c1b8b22ef55478e7e008cd34bb4d67fa8bf1c1cdb4525d4` |
| Nilsson--Wikström 2005.09505v1, 19 May 2020 | 1--6 of 13 | `072c5174f8fbe7c83a3ffbaf0362273073e2c83dfd45edba8227367d7bc8b92c` |
| Nilsson 2505.09301v1, 14 May 2025 | 1--3 and 7--12 of 17 | `521b9f0ebacb96cf628c4769c0d8b84eaf36fd1a26871755489e85a2d532976c` |
| Wikström, published Ark. Mat. 39 (2001), 181--200 | 1--3 and 5--12 of 20 | `66f3f0dcdc9be58490a188a5cbe2e30229153470d8a31007ce4421499697a926` |

The 2020 and 2025 arXiv author files are not the related 2021 and 2026
journal layouts. The attempted 2026 Wiley PDF returned HTTP 403. The
Sibony DOI returned an anti-bot HTML page, not the article, and the Ransford
chapter endpoint returned a non-PDF response. These access results are
retained; they authenticate neither article content nor printed locators.
Wikström's published 2001 B-regular/Jensen criteria supply an inspected
alternative for the boundary argument. The disk estimate can be written
directly with circle submeans and reverse Fatou, without an unchecked
Ransford theorem-number claim. Acquisition layout texts remain unchanged;
images control conjugation marks, closure symbols and signs lost by extraction.

## Scoped source records

**W01 — Controlling revision.** v2 Theorems 1.1--1.2, actual 1--2,
are stronger than v1's formulations. v2 gives automatic subharmonicity for
finite-above usc obstacles and every complex dimension n at least two.
Its Proposition 3.4(b) adds a converse for pluriharmonic obstacles. v1
already contains majorant sufficiency; that whole criterion is not new to v2.
The general Jensen inequality is promoted from the old example remark to
a separate v2 proposition. The revised subharmonic proof removes Brelot
resolutivity. v1's incomplete sentence after (2.5) is a literal text defect,
not a counterexample to its intended dominated-convergence step.

**W02 — Subharmonic signature.** v2 Theorem 1.1 uses a connected
domain in real dimension d at least two, an usc obstacle into
[-infinity,+infinity), and globally bounded-above subharmonic minorants.
The empty-family envelope is minus infinity. Each competitor has its own
finite upper bound; there is no common bound fixed for the entire family.
The two-sided bounded version has the same conclusion. Obstacles allowing
plus infinity require the separately stated subharmonic-regularization
hypothesis; it is not automatic in that enlarged class.

**W03 — Envelope versus obstacle.** The conclusion is V=V*, not
V=f for every obstacle. Corollary 2.1, actual 4, recovers an already
subharmonic W from increasing bounded minorants converging to it
quasi-everywhere. The disk Poisson kernel has restricted SH envelope zero,
as Nilsson--Wikström's earlier Example 1.2 shows. This is consistent with
V=V* and prevents a false universal obstacle-recovery statement.

**W04 — Linear proof mechanism.** v2 proof, actual 3--4, uses Choquet
selection and increasing finite maxima, W=V*, harmonic Poisson differences
h_j=P_B[u_j]-P_B[W], and max-pasting of W+h_j with u_j. Boundary integrals
are finite for nontrivial SH functions; truncation and Poisson comparison
exclude an integral of minus infinity which would force an open set of
minus-infinity values. Polar exceptional sets have zero harmonic measure
on the centered sphere. The pasted correction remains globally bounded
above, and preserves a competitor's lower bound when present.

**W05 — Complex correction boundary.** An ordinary real harmonic
Poisson difference in C^n need not be pluriharmonic when n is at least two.
Adding it need not preserve PSH. In one complex variable PSH equals SH.
This identifies the proof's category boundary; no non-Archimedean
harmonic correction or envelope theorem is inferred.

**W06 — Hartogs geometry.** v2 actual 4--6 and Remark 3.6, actual
8--9, use P(w)=(1-|w|²)/|1-w|², Phi=P²+(1-|w|²)^(-1), and
Omega_n={||z||<exp(-Phi(w)), w in D}, z in C^(n-1). The interior
obstacle W=P(w) is finite, positive, smooth and pluriharmonic; its
unboundedness is at a boundary point. The axis H={0}×D is an analytic
disc of codimension n-1. The bounded B-regular domain has cuspidal
boundary points, so globally smooth boundary is not asserted.

**W07 — Higher-dimensional Levi check.** r=log||z||+Phi is smooth
near the side boundary. The complex tangent constraint and the
log-norm Levi form give positivity from Phi_wbarw when the w component
is nonzero, and from the orthogonal z component otherwise. The radial
null direction of log||z|| is excluded by tangency. A product with extra
discs has boundary analytic discs and does not give the same B-regular
construction. The exact derivatives confirm Phi_wbarw>0.

**W08 — Boundary peaks.** On the collapsed boundary circle,
b_zeta=Re(conjugate(zeta)w)-1 is a continuous pluriharmonic peak,
zero at its selected point and strictly negative elsewhere on the closure.
The conjugation is essential and is visible in the PDF. A strong peak
does not mean a strictly positive complex Hessian: this peak has zero
Levi form. Smooth strongly pseudoconvex side points have local negative
PSH peaks which can be pasted with a negative constant.

**W09 — Axis estimate.** Any globally bounded-above PSH u<=W
restricts to a bounded-above SH function on the axis, or minus infinity.
Its boundary limsup is at most zero except at one point. Circle submeans,
the global bound and reverse Fatou give v<=0; a disk automorphism handles
each center. Harmonic measure of the exceptional singleton is zero.
The zero competitor forces V=0 on H.

**W10 — Explicit competitors.** u_epsilon=max(0,P+epsilon log||z||),
extended as zero on H, is PSH and is bounded on both sides. Since
log||z||<-Phi<=-P², it obeys 0<=u_epsilon<=1/(4epsilon).
As epsilon decreases to zero it increases to W off H and remains zero
on H. The finite upper bounds grow with the selected sequence.

**W11 — Exact raw envelope.** v2 Theorem 1.2 and proof give V=W
off H and V=0 on H, while V*=W everywhere by density and continuity.
At (0,0) the values are zero and one. H is pluripolar, so the example
is simultaneously a quasi-everywhere approximation and an everywhere
pointwise failure. No envelope without the global boundedness restriction
is being evaluated by this formula.

**W12 — Quantifiers.** The family allows each competitor its own
global bound. A prescribed common cap gives a different envelope. Local
boundedness of W in the interior does not make it an admissible globally
bounded competitor. A finite-valued obstacle may have an infinite
majorant on an analytic subset.

**W13 — Tameness with poles.** Remark 3.3 gives G=-log||z||>Phi>=W²,
positive plurisuperharmonic, nontrivial and plus infinity exactly on H.
The square identity yields W<=epsilon G+1/(4epsilon) for every epsilon.
Nilsson--Wikström preprint Theorem 3.2, actual 4--5, makes this a tame
example through a superlinear scalar function. Nilsson's published
Lemma 2.1, actual 3/printed 3961, gives the strong-majorant equivalence.
Neither tameness nor nontriviality makes G finite everywhere.

**W14 — Finite-majorant sufficiency.** v2 Proposition 3.4(a), actual
7--8, needs only PSH W and a positive plurisuperharmonic strong majorant.
W-epsilon G is a globally bounded-above admissible PSH competitor.
At points where G is finite, it tends to W, proving V=W there. Pole
points are excluded from that argument; infinite subtraction is handled
as addition of a negative PSH function, without plus-infinity PSH values.

**W15 — Pluriharmonic converse.** Proposition 3.4(b), actual 8,
uses finite pluriharmonic W. From V(p)=W(p), choose increasing bounded
competitors u_k with deficit at p below 2^(-k). Then
G=1+sum(W-u_k) is positive plurisuperharmonic, finite at p and a strong
majorant, since NW<=sum_{k<=N} sup u_k+G. Pluriharmonicity makes
the nonnegative deficits plurisuperharmonic; this converse is not
claimed for arbitrary PSH obstacles.

**W16 — Defect and pole sets.** For pluriharmonic W the defect set
is the intersection of the pole sets of all positive strong majorants.
In the example every such majorant is infinite on H, and the explicit
G has exactly that pole set. Its restriction to H is identically infinite
and supplies no nontrivial disk majorant. Tameness cannot be transferred
to such a subvariety by this restriction argument.

**W17 — Jensen conventions.** v2 Proposition 3.2, actual 6--7,
uses probability measures on the closure tested by globally bounded-above
PSH with usc boundary traces. Published Wikström Definition 1.1,
actual 1--2, matches this convention. Its Theorem 4.1, actual 9--11,
and Corollary 4.3, actual 12/printed 192, give equality with the
continuous-closure Jensen class on B-regular domains. The boundary
support restriction is separate from equality of these classes.

**W18 — One-sided Jensen bound.** The correct general estimate is
V(p)<=lim_M inf_mu integral (f cap M)* dmu, with boundary-supported
Jensen measures. An individual competitor's bound licenses a sufficiently
large truncation. The limit exists by monotonicity, but equality or an
interchange of limit and infimum is not supplied. The fixed axis harmonic
measure has zero integral for every finite truncation of W, so the
example needs no interchange of infimum and limit.

**W19 — Dirichlet distinction.** Remark 3.5, actual 8, explicitly
separates raw-envelope discontinuity from continuity of Dirichlet solutions.
V*=W is already continuous and maximal in the interior. The example
does not refute globally continuous tame Dirichlet solutions, nor assert
finite continuous data on the entire cuspidal boundary.

**W20 — Published Nilsson locators.** The 2022 journal PDF has
Definition 1, Lemma 2.1 and Proposition 2.2 on actual 3, printed 3961,
with the latter proof ending actual 4/3962. The 2021 preprint has
Definition 2.1 on actual 2, Lemma 2.2 and Proposition 2.3 on actual 3--4.
Wikström cites the latter numbering alongside the journal citation.
The correspondence resolves this edition mismatch; book locators must
name the controlling version and cannot silently transfer the numbers.

**W21 — Earlier Poisson obstruction.** Nilsson--Wikström v1 Example
1.2, actual 1, already contains the disk and ball-axis obstruction.
The later Hartogs construction adds tameness and exact off-axis
recovery. Its Theorem 3.1, actual 4, promises only quasi-everywhere
approximation. The adjacent question display literally omits v<=u;
its unrestricted supremum would be infinite. The book retains the
intended obstacle condition, without treating this textual omission
as a refutation of the intended research question.

**W22 — Reversed Edwards inequality.** Nilsson--Wikström v1
Theorem 4.1, actual 6, writes I^F g<=S_F g for arbitrary Borel g.
The Jensen definition immediately gives S_F g<=I^F g; the published
Wikström Theorem 2.1, actual 3/printed 183, has that correct direction.
On X=[0,1], F=C(X), and g equal to one at zero and zero elsewhere,
J_0 consists of the Dirac measure, I g(0)=1 and S g(0)=0.
This checks the literal direction error. It is not a counterexample
to the lower-semicontinuous equality clause or a proof that the later
Dirichlet theorem is false. The general equality chain is not imported.

**W23 — Nilsson 2025 terminology only.** Exact preprint Definition
3.1, actual 7, calls a signed function pluri-quasibounded when a positive
plurisuperharmonic majorant strongly dominates its absolute value. It
says the majorant quasibounds the function; the word strongly in
Wikström's terminology is not quoted as the preprint's exact wording.
The 2026 publication's definition locator remains unchecked. The
positive example satisfies the displayed absolute-value condition directly.

**W24 — Boundary criterion scope.** Original Sibony and Ransford
files were not obtained. The inspected published Wikström Corollary 3.8,
actual 8/188, supplies the boundary Dirac-Jensen criterion. For the
Hartogs geometry, rho=max(log||z||+Phi,|w|²-1) is a continuous negative
PSH exhaustion, zero on the side and collapsed circle; it is finite and
continuous near the axis. The boundary peaks force each boundary
continuous-cone Jensen measure to be Dirac. This is an explicit
elementary reformulation, not a new theorem or original-source reading
claim. External Walsh extension and standard peak inputs remain attributed.

**W25 — Unimported Dirichlet chain.** Nilsson v1 Theorem 3.7, actual
10--12, needs compliant measures, pluri-quasibounded boundary data,
continuity/local bounds off a b-pluripolar set, a Cegrell E minorant,
and comparison/balayage inputs. Literal proof-text issues include the
positive lower bound for negative approximants in Lemma 3.3 on actual 9,
u instead of u' in one comparison conclusion on actual 11, and
max(v,-j) for positive v in the purported negative-PSH truncation there.
The last expression equals v for every j and does not justify that
E-class truncation step. These are retained as source-local defects;
no statement is declared disproved and no 2026 publisher-proof defect
is inferred. Its E-to-D minorant conjecture and measure-class discussion
are preprint-local questions, not authenticated current published status.

**W26 — Final scope.** The fully read controlling v2 argument is
unrefuted by this source/sign/quantifier audit and its exact elementary
diagnostics, with standard SH/PSH inputs kept explicit. No full
unbounded Dirichlet proof chain is certified. No original theorem,
independent production-model call, canonical problem closure, general
non-Archimedean envelope property or repair of BJ22 Theorem 6.21 is added.
The latter remains the user-identified proof gap, not a counterexample
established by this complex-domain construction.

## Preservation and next integration

The frozen record checks all 5,172 tracked baseline hashes except the
two intentional editorial progress updates, all 425 active TeX inputs,
108 protected inputs, 104 preceding frozen manifests and 178 preceding
exports. Both bibliographies, generated book/index and native catalogue
source/PDF are byte-preserved. The canonical inventory remains 42 atoms,
12 tier-zero atoms, with status totals 0/3/7/15/17.

The actual-read sheets and their complete selected texts are pinned
individually; no page is credited from a search snippet or acquisition.
The successful freeze records are immutable. The intended book addition
will present the restricted-family signature, exact Hartogs example,
finite-majorant recovery, pluriharmonic converse and one-sided Jensen
estimate, with a concise provenance account of the edition and proof-text
qualifications. It will preserve prior theorem/equation numbers and the
canonical inventory, and undergo build, navigation and matching-page checks.
