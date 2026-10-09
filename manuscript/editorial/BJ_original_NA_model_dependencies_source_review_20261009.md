# Original non-Archimedean energy and bounded model-ray dependencies

Date: 9 October 2026. This is a selected primary-source audit. The current
4,667-page book, its two bibliographies and the open LaTeX catalogue are
unchanged by this checkpoint. All work remains in the cloud.

## Editions and actual reading

| Source | Controlling bytes | Actual selected scope |
| --- | --- | --- |
| Boucksom–Jonsson, *Singular semipositive metrics on line bundles on varieties over trivially valued fields* | arXiv:1801.08229v1; 79 physical pages; SHA256 `6ee47fae26082ead2beb6375448c0ba0b9d95ab80439753d2b28a76421ebf5d0` | 1–6, 51–79: 35 pages, 18 individual matching displays. Physical 7–50 remain unread in this round. |
| Boucksom–Jonsson, *A non-Archimedean approach to K-stability* | arXiv:1805.11160v1; 39 physical pages; SHA256 `fa108da4e3f443258662f6615e3b598bb07df946908fda069383b36ec10bde6d` | 1–4, 22–34, 37–39: 20 pages, 11 displays. Physical 5–21 and 35–36 remain unread. |
| Berman, *K-polystability of Q-Fano varieties admitting Kähler–Einstein metrics* | arXiv:1205.6214v3; 41 physical pages; SHA256 `7331584a455a5ae1d53f5dec03f914df75b8835fc29210d0cd37e98122346884` | 1–2, 9–16, 39–41: 13 pages, seven displays. Physical 3–8 and 17–38 remain unread. |

The first preparation selected 55 source/page pairs in 29 views. Reading
revealed that the FS definitions and two original energy proof blocks
needed additional pages. A separate immutable preparation added 13
previously unselected pages in seven views. The combined **68 distinct
source/page pairs and 36 individual views** were actually read as complete
selected text and matching rendered images. No PDF is wholly read. No
preparation, computation, archive or upload creates reading credit.

The 1801 v1 margin says 24 January 2018, while the acquired PDF's internal
first-page date says 12 March 2022. Both are recorded literally. This
date mismatch alone does not identify a different mathematical revision.
The 1805 v1 margin and internal dates say 28 and 30 May 2018. Berman v3
has the 9 June 2015 margin. The later Inventiones 203 (2016), 973–1025,
edition is not byte-certified by reading this 41-page preprint.

All 36 chronological notes and receipts pin the exact PDF, selected text
and image. The original preparation flags remain false; the separate actual
record supplies the reading claim. Supplemental note 6 resolves the
provisional canonical-FS terminology in first-pass note 15. Supplemental
note 7 explicitly withdraws any suggestion that a raw point-jump example
refutes the upper-regularized Theorem 4.16 of this exact 2018 source. The
older notes are retained unchanged rather than silently rewritten.

## The original NA energy chain

BoJ18a defines parts of the theory over arbitrary non-Archimedean fields,
but its continuity, orthogonality, countable regularization and full
Calabi–Yau existence theorems retain **smooth projective X, ample L,
trivially or discretely valued k, and residue characteristic zero**. Its
trivial-valuation arguments descend discrete results through the Gauss
extension. Resolution, SNC models, vanishing and BFJ/BGJKM inputs remain
original dependencies. Reading this selection does not prove a general
BJ22 envelope theorem or repair homogeneous Siu decomposition.

The measure convention is probability MA, and energy has the factor
1/((n+1)V). Constants satisfy E(phi+c)=E(phi)+c. Consequently

    F_mu(phi)=E(phi)-integral(phi-phi_ref) dmu

is invariant under constants for a probability measure. MA uniqueness
is naturally on E1 modulo constants. Compactness is used on a family with
a reference upper bound and an energy lower bound; an I or J bound alone
does not select a representative because both ignore constants.

Theorem 6.9 constructs mixed finite-energy measures by integration by
parts, positivity and density of differences of FS metrics in continuous
functions. Its proof uses Radon integration for **decreasing USC nets**
and approximate monotonicity, not a sequence-only dominated-convergence
argument on an arbitrary Berkovich space. Theorem 6.11's increasing-net
proof replaces mixed measures with FS measures uniformly, then tests
the latter at their finite quasimonomial support. Increasing convergence
does not mean pointwise convergence at every analytic point.

Corollary 6.22 proves a countable decreasing FS regularization for a
finite-energy metric in this exact setup. Its sequence is selected by
energy and reference-MA pairings, with the pointwise conclusion using
model atoms and order. It is not a countable cofinal sequence of all SNC
models. Corollary 6.23's further countable PSH regularization retains the
same field and smoothness assumptions.

The original Lemma 6.17 proof is now read through physical page 76. With
phi_t=t phi+(1-t)psi, differentiation gives

    d/dt J_psi(phi_t)=I(phi_t,psi)/t >= (n+1)J_psi(phi_t)/(n t).

Thus J_psi(phi_t)/t^(1+1/n) is nondecreasing and
J_psi(phi_t)<=t^(1+1/n)J_psi(phi). This rescaling is a potential-energy
estimate; it is different from scaling a graded weight by its degree.

Orthogonality and envelope differentiability in Theorem 6.30 use the
discrete BFJ result and the removal of its technical hypothesis through
BGJKM and Lazarsfeld's appendix. Corollary 6.32 extends differentiation
to E1 obstacles by the actual countable regularization theorem and
decreasing mixed-MA continuity. Its derivative is the scalar
integral f MA(phi). The bound P(phi+tf)>=phi-|t| norm(f)_infinity
keeps the envelope in finite energy for either sign of t.

The variational existence proof maximizes F_mu. It does not minimize it.
Its ordered strictness, normalization and energy topology are required
to identify the limiting metric, rather than only its energy number.

## Printed defects and explicit proof obligations

These are distinctions between literal formulas, omitted arguments and
intended theorems. No intended main theorem in these three sources is
declared disproved.

| Location in BoJ18a | Actual observation and retained consequence |
| --- | --- |
| Lemma 6.24 and its quotient-centering discussion, physical 56 | Literal membership in E1_C fails for the constant family phi_ref+1, even though it converges strongly. A common shift/reference bound is needed. The printed +max centering doubles a constant; the normalized representative subtracts the maximum. |
| Corollary 6.28, physical 57 | The I-zero-to-constant argument needs strong-topology separation, or the earlier I/topology equivalence, rather than the cited measure-pairing continuity alone. |
| Cauchy-net compactness, physical 58 | Cauchy estimates bound a tail; incomparable earlier indices need not all lie in one bounded set. A compactness argument can be localized to the tail. |
| Corollary 6.32, physical 59 | The displayed derivative omits its pairing with f. The lower obstacle bound has the wrong sign; use phi+inf(tf) or the norm bound above. |
| Proposition 7.2, physical 64 | Concavity gives F_MA(phi)(psi)-F_MA(phi)(phi)=-J_phi(psi)<=0. The proof prints +J>=0, which is inconsistent with taking a supremum. The dual value (I-J)(phi) is the intended correct identity. |
| Proposition 7.8, physical 65–66 | In the J-to-infinity argument, t=J^(-1/2) tends to zero and keeps t^2 J bounded. The printed positive exponent does neither. |
| Corollary 7.9, physical 66 | The lower integral bound gives F<=A-J+B sqrt(J), not the printed minus sign. Completing the square gives F<=A+B^2/2-J/2, sufficient coercivity. |
| Proposition 7.10, physical 67 | An ample CL2-L1 does not make C phi2 an L1-PSH metric. A compatible comparison uses CL1-L2 ample and phi2/C, with reference and E1 bookkeeping retained. |
| Proposition 7.24, physical 70 | A sequence of models chosen only by convergence of the dual energy need not be cofinal in the entire model net. Weak convergence of its retracted measures therefore requires an extra argument. One possible route is to control the full net with the already proved ordered I comparison, rather than assert model cofinality. No complete replacement theorem is promoted here. |
| Proposition 7.27, physical 71 | A weak maximizer accumulation argument alone does not yet give the claimed strong convergence. On a normalized bounded energy family, the earlier mu-pairing continuity plus convergence of maximal F values would also give convergence of E; this is an additional step. |

Several lesser proof slips, including repeated potentials in concavity
and quasi-triangle lines, are recorded in the individual notes. The
approximation of arbitrary uniform nets by decreasing nets via added
constants also requires an argument; a uniform net does not automatically
admit the monotone correction asserted in passing. These observations are
kept separate from the finite FS Cauchy–Schwarz estimates actually read.
Those estimates pair differences of potentials with **signed differences
of equal-mass measures**, so constants cancel. They do not imply the
absolute-mean bound disproved for published BBJ21 Lemma A.2.

## The 2018 FS and Dirac-potential conventions

BoJ18b is in the smooth projective, ample, trivially valued
characteristic-zero setting. Its exact physical pages 22–24 define

    Q_2018(phi)=usc sup{positive metrics psi: psi<=phi},
    FS_2018(norm_bullet)=usc sup_m m^(-1)FS(norm_m).

The upper regularization is part of **both definitions**. This differs
from the raw Q notation in the later BJKS1 source. The source proves
Q_2018(phi)=usc P(lsc phi), and for continuous obstacles obtains
Q_2018=P using its restricted continuous-envelope theorem. Its bounded
PSH range consists of metrics regularizable from below, where convergence
means pointwise on quasimonomial points and upper regularization globally.
One cannot infer ordinary pointwise equality everywhere from that phrase.

Powers make the finite-degree obstacles increase along divisibility.
Factorial degrees are genuinely a countable cofinal subset of the positive
integer divisibility index. This says nothing about cofinality of the SNC
model index. The Veronese FS identity includes division by r. A scalar
norm shift exp(c m) corresponds to the metric shift -c.

Lemma 4.15's use of an arbitrary graded subalgebra requires its actual
degree period and semigroup lattice. The elementary example k[x^2,y^2]
has dimension k+1 in degree 2k and zero in odd degrees; an ordinary
all-degree volume limit fails and the ambient lattice overcounts its
leading volume. The saturation line and the invoked Boucksom Okounkov
lemma therefore need their original hypotheses. This source audit supplies
no general replacement semigroup theorem.

For a nonpluripolar point x, Theorem 5.13 constructs its extremal metric
phi_x with MA(phi_x)=delta_x, E(phi_x)=S(x), and J(phi_x)=T(x)-S(x).
The generic point has S=T=0 and phi_x=0. The point's valuation norm
has minimum jumping number zero in **eventually globally generated
degrees**; this need not hold for every small ample degree.

The quasimonomial proof chooses an SNC model containing x and refines it
to a vertex, constructs a barrier, and uses continuous-envelope
orthogonality. The general case first identifies the finite-energy
potential by the retraction net and maximum argument. It then proves
continuity using the explicit estimate

    phi_{x_j} <= phi_x <= phi_{x_j}+epsilon_j,
    epsilon_j=phi_x(x_j) decreasing to zero.

This uniform estimate is the missing justification if the proof is
abbreviated to 'a bounded increasing limit is continuous'. The source's
subsequent FS identification explicitly uses usc. The energy calculation
on physical 32 reverses sup-minus-J; the correct value is S.

Corollary 5.17 correctly states M_ad(phi_x)=A(x)-S(x). Its next
semistability paragraph reverses both signs; the consistent inequality is
A(x)>=S(x). Uniform stability uses (1+epsilon)S<=A. Ratios A/S and
A/T exclude the trivial point with zero denominator, or require a stated
convention. The minimizing-point argument on physical 34 imports
Blum–Jonsson under its stated uncountability hypotheses. Failure of
semistability is delta<1; failure of stability can also occur at delta=1.
Historical regularizability and entropy conjectures in this 2018 text
are not automatically new 2026 catalogue atoms.

## Berman's bounded model-ray input

The actual original BBJ21 base input, Proposition 2.7, is on physical
14–16 of this v3. It treats a normal ample test configuration over the
complex numbers with a locally bounded positive boundary metric. Over
a disc, its envelope proof uses a lower barrier, a global upper bound
on a resolution, upper regularization, time-convexity boundary control
and local Bedford–Taylor homogeneous-MA comparison. The locally bounded
measure does not charge the singular locus. The quasi-PSH compactness
and local Dirichlet results remain external proofs.

The printed barrier is called continuous even for a merely locally
bounded boundary metric, although near the boundary it equals that
metric plus log|tau|. Continuity of this barrier needs continuity of the
datum; the bounded-barrier argument is a separate claim. The full main
Ding-slope and polystability argument on physical 17–38 is unread here.
This selection cannot certify it or arbitrary E1 ray existence.

Berman uses t=-log|tau|^2 and squared Hermitian metric potentials. Its
energy has 1/(n+1), without 1/V, and E(phi+c)-E(phi)=Vc. The normalized
book energy is E/V. The Deligne formula (2.4) on physical 11 omits the
zeroth curvature: a relative n-dimensional fiber needs n+1 factors.
Proposition 2.5's integral has an additional mu factor inconsistent with
its preceding intersection formula. The direct local-weight computation
checks Lemma 2.6's singular Kempf–Ness signs; an orbit section of nonzero
weight has a zero or pole at the origin and need not holomorphically
trivialize the line there as the alternative proof says.

Formula (3.1) on physical 16 prints +log integral exp(-phi) together
with -E/V. A shift phi+c changes this literal expression by -2c,
so it cannot have the claimed KE critical points. The convention
consistent with the preceding KE equation is -E/V-log integral exp(-phi),
up to a reference constant. This diagnoses a displayed sign, not the
intended polystability theorem. A product total space may have a nontrivial
action and a nonconstant flow ray; only a trivial product action gives
the constant ray in Example 2.8.

## Evidence and next book integration

Twelve elementary exact diagnostic families test constants, dual energy,
coercivity scaling, directional obstacle bounds, energy differentiation,
Ding signs, Deligne degree, local weights, adjoint signs, rare spectral
weights and semigroup periods. They do not supply new primary reading,
an independent-model verifier receipt or a new formal mathematical result.
All archived members are byte-checked. Author-written evidence is published
to GitHub; controlling external PDFs and their selected text/image evidence
are retained in a separate cloud archive with precise partial scope.

The next book unit can now use the published BBJ21 Theorems 6.4 and 6.6
as exact source anchors, and the read Finski Corollary 2.12 to explain
the holomorphic input behind fixed-rank Parseval quantization. It must
retain the quotient-by-constants normalization, ordered energy strictness,
the inequality/equality distinction for arbitrary versus maximal rays,
and original restricted envelope dependencies. These are source-attested
explanations and imports, not newly verified general theorems.

Canonical inventory remains 42 active atoms in twelve formal problems,
tiers (0,3,7,15,17). General BJ22 homogeneous Siu and general envelopes
remain OPEN, LPWZ density UNVERIFIED, and the user's Theorem 6.21 proof
warning binding. The last complete ordered whole-book read remains
4 October; later source and book selections are scoped. No fresh complete
book pass, source independence certificate or repair of Theorem 6.21 is
claimed. Incoming author research should be checked at the next GitHub
sync before its integration.
