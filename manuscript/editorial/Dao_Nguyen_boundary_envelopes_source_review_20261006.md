# Unbounded boundary envelopes and divisor Green functions: exact-source audit

Recorded 6 October 2026. Baseline: afec39f9b76e645c476374c695a3db4595abd61b.
This checkpoint changes no active TeX, bibliography, canonical problem status,
original-result verification tier, native catalogue or general Siu/envelope closure.

## Decision

The two new papers provide a useful complex reference for the book's distinction
between an interior obstacle, boundary data, a divisor singularity and the class
in which uniqueness is sought. They can support attributed exposition in
Appendix H and a connection to Chapter 68. The deformation hypotheses and
remaining questions must accompany that exposition.

The Green-function paper's sectorial inward deformation (SID) yields its
canonical truncation approximation; B-regularity is used subsequently for
continuity. The Dirichlet paper uses a different, potentially outward or
nonnested deformation and a one-sided obstacle condition. These methods are
not interchangeable. Neither gives a general non-Archimedean envelope theorem,
mixed-product continuity, arbitrary ideal-singularity identification or a
repair of Boucksom--Jonsson 2022, Theorem 6.21.

Both new papers have been read in full. Their complete external proof chains
are **not independently certified**. Precise selections from the controlling
older sources have been read, including the original 2001 erratum. Literal
auxiliary errors are distinguished from the new main assertions. No
counterexample to either new main theorem, complete proof repair, original
result promotion or independent-model receipt is claimed.

## Editions and actual reading

Read the full selected text and actually displayed **119 source/page pairs in
62 sheets** across seven exact PDFs: four complete returned PDFs and three
precise selections. Two additional crops repeat already counted pages and add
zero unique pages. Acquiring a PDF or looking up metadata does not count as
reading.

| Source | Acquired layout | Physical pages actually read | Scope |
| --- | --- | --- | --- |
| Huy Hoang Dao, Quang Dieu Nguyen, *Complex Dirichlet problem with unbounded boundary values* | 2610.00914v1, 33 pages; submitted 1 October 2026, 01:46:02 UTC | 1--33 | Complete v1, including references |
| Huy Hoang Dao, Quang Dieu Nguyen, Duc Hieu Tran, *Continuity of pluricomplex Green functions with hypersurface poles on certain B-regular domains* | 2610.00909v1, 35 pages; submitted 1 October 2026, 01:39:03 UTC | 1--35 | Complete v1, including references and affiliation page |
| Finnur Lárusson, Ragnar Sigurdsson, *Plurisubharmonic extremal functions, Lelong numbers and coherent ideal sheaves* | Legacy publisher PDF, Indiana 48 (1999), printed 1513--1534, DOI 10.1512/iumj.1999.48.1767; 22 actual pages | 1, 11--22, printed 1513 and 1523--1534 | Complete displayed Section 3 and references; most of Sections 1--2 unread |
| Same authors, *Erratum* | Legacy publisher PDF, Indiana 50 (2001), DOI 10.1512/iumj.2001.50.2279; one actual page, printed 1705 | 1 | Complete returned erratum; citation metadata 1705--1706 does not create another PDF page |
| Quang Dieu Nguyen, *Continuity of pluricomplex Green functions with poles along a hypersurface* | Published Ark. Mat. 43 (2005), 181--200, DOI 10.1007/BF02383618; 20 pages | 1--20 | Complete publication |
| Barbara Drinovec Drnovšek, Franc Forstnerič, *Disc functionals and Siciak--Zaharyuta extremal functions on singular varieties* | Published Ann. Polon. Math. 106 (2012), 171--191, DOI 10.4064/ap106-0-13; 22-page returned layout | 1--4, 9--14, printed 171--174 and 179--184 | Functional definitions, Lemma 3.2 and complete displayed Theorem 3.1 argument; remaining pages unread |
| N. Q. Dieu, T. V. Long, T. D. Hieu, *Dirichlet problem for plurisubharmonic functions on bounded quasi B-regular domains in Cn* | 2509.12063v1, 23 pages; submitted 15 September 2025, 15:42:44 UTC | 1--3, 6--9 | Definitions and complete displayed Lemmas 2.3 and 2.6; main continuity proof unread |

The 2026 JGA publication corresponding to 2509.12063 is J. Geom. Anal. 36,
article 164, DOI 10.1007/s12220-026-02412-1. Its attempted publisher PDF
request returned an HTML cookie-error page. It has **not** been read or
identified with the preprint. Diagnostics of v1 are not attributed to that
publication.

The older math/9807164v1 PDF was acquired but not read in this checkpoint.
The published 1999 copy was obtained instead. The metadata of DDF's
1109.3947v3 was consulted, but that preprint was not used as the read edition.
The current IUMJ issue pages returned service errors; public legacy publisher
PDF endpoints supplied the two controlling copies.

PDF SHA-256 pins, in the table's order:

- e1eab0c0bdf2369ee514cfed4261e177ca1801282ce7ac90f3dc0db2fcd4efea.
- ebed2c071947b0f7a57d5524eb16215632c125c1bb933f6bca664cbd4ec2517f.
- 601bed29ec31e988ed90f9db6115cd0a255b867c8f97730b0c2e79c6a33f5714.
- ebc482b82c23899feac2392b0a3e397d2c0e407d089aac52e87b5e25b6afffe9.
- b776107a71dda1a42fc636a51123d5536d8417c45f24f603b96c41d267c59c48.
- ad0f59af86d96b1d357f9c870b388df176aebe8bcd03c8145ac21664b7aa9033.
- 979581b6a6fb1ef8fff716ab3ef97c8e0751a73fb4dc2f9ce27181cdf75ecc4b.

Acquisitions, actual-reading flags, displayed images, selected text and
calculation records are separately pinned in the companion manifest.
Initial preparation/acquisition flags remain historical records.

## The Dirichlet paper

**DB01 -- Interior obstacle and maximal envelope.** Theorem 1.1 and its
proof, physical 14--15: the obstacle is extended-real continuous on the
**closed bounded domain**, superharmonic in the ordinary real sense inside,
and not identically +infinity. Its finite lower bound and the submean
inequality give local uniform upper bounds for its PSH minorants. Upper
regularization remains below the obstacle; pasting gives maximality and
vanishing locally bounded top Monge--Ampère mass. Boundary barriers provide
the indicated boundary limits. An arbitrary continuous interior obstacle
does not have this maximality property.

**DB02 -- The divisor identity has a scalar hypothesis.** For a reduced
principal divisor defined by f on a neighborhood of the closure, the obstacle
phi=-log|f| and the residual of the Green function are related by
G_A=log|f|+G_phi off A, with PSH extension of the residual.
Lárusson--Sigurdsson Proposition 3.2, printed 1525--1526, supplies local
divisorial subtraction; their Theorem 3.3, printed 1526--1527, gives the
divisor Riesz functional under its stated Stein ambient hypothesis.
DDF's general-manifold functional interface is a separate source.
The same identity is not supplied for an arbitrary tuple of generators.

**DB03 -- One-sided deformation and moving boundary.** Definition 1.3 and
Theorem 1.4, physical 4--5; proof 15--18: the biholomorphic maps are defined
on a fixed closure neighborhood, approach the identity, and have the
specified real-analytic inverse trajectories. D1 controls the one-sided
obstacle difference near its infinite boundary locus. D2 requires the
moving-boundary cluster S_Phi to avoid that locus and have PSH barriers.
The cluster uses **closed Omega intersect Phi_t(boundary Omega)**.
For the identity deformation it is the entire boundary, not the empty set.
Neighborhood PSH minorants require neighborhood barriers, rather than
merely barriers defined inside Omega.

**DB04 -- Proof mechanism and compactness.** Physical 15--18:
transport the envelope by Phi_t inverse, keep its upper obstacle error
uniform, use subharmonic pullbacks along the inverse trajectory to recover
the center value, then regularize on a compact cut away from the moving
boundary. Strict barrier margins permit a maximum gluing. The selected
cut and its boundary are fixed before the local regularization tolerance.
There is no general assertion that the deformed domains are nested, Runge
or pseudoconvex.

**DB05 -- What convergence says.** Theorem 1.4 gives approximation by
finite continuous minorants, interior continuity and locally uniform
convergence of increasing continuous **whole-boundary** approximations.
Lemma 3.3 and Corollary 3.4, physical 18--19, allow nonmonotone boundary
approximations off the specified neighborhood pluripolar hull.
Proposition 3.6, physical 19--20, instead gives whole-domain convergence
under finite-truncation uniform boundary approximation, or the equivalent
eventual domination/sequential condition. Mere pointwise convergence
is insufficient; Example 5.2, physical 28--29, makes this explicit.

**DB06 -- Boundary hulls are different objects.** Physical 18--19:
the neighborhood pluripolar hull uses PSH functions on connected
neighborhoods of the closure. The quasi-B-regular preprint, physical 7,
uses negative PSH functions only on Omega with upper boundary limit
-infinity. These domains of definition and boundary-limit conventions
must remain distinct.

**DB07 -- Jensen and Hartogs claims keep the ambient category.**
Lemma 3.7 and Proposition 3.8, physical 20--21, use the cone of PSH
functions continuous on the closure and boundary-supported Jensen measures;
the minimizing measures have finite obstacle integral and charge no
infinite boundary locus. Theorem 1.5, physical 5--6 and proof 21,
additionally requires a pseudoconvex ambient U, O(U)-convex closed Omega
and the neighborhood-minorant interface. The Hartogs fiber radius is
exp(-G_phi). An O(U)-hull is not automatically the polynomial hull in Cn.

**DB08 -- Domain variation and uniqueness are separate.**
Corollary 1.8, proof physical 23--24, requires uniform convergence of the
radii exp(-phi_j) on the indicated closed ambient set, inner exhaustion
of every compact subset of Omega, and **outer** cluster control of the
closed varying domains. Example 4.1, physical 22, shows why the latter
cannot be omitted. Theorem 1.9, proof physical 24, concerns lower-bounded
maximal PSH functions below the **same obstacle**, with the indicated
boundary trace and complete pluripolar/barrier assumptions. Adding a
positive Poisson kernel can preserve the extended boundary data while
leaving this class; physical 24--25 explains the obstruction.

**DB09 -- Ideal preservation is stronger than zero-set preservation.**
Lemma 1.11, physical 26, uses holomorphic division for a reduced
principal divisor preserved by the jointly holomorphic deformation.
Proposition 6.1, physical 31, requires a holomorphic matrix identity
F composed with Phi_t=M_t F, with M_t approaching the identity uniformly.
For F=(z1 squared,z2), the map (z1,z2+t z1) preserves the zero set {0},
but its second pullback generator does not belong to that ideal.
This extension concerns obstacles and does not identify all
higher-codimensional Green-function conventions.

**DB10 -- The nonnested example is internally checkable.**
Example 5.1, physical 28: Phi_t=(exp(-t)z1,exp(t)z2) gives ellipsoids
which vary in opposite coordinate directions. For the fixed obstacle
-log|z1| the envelope on the deformed domain is
t-1/2 log(1-exp(-2t)|z2| squared). Its derivative at zero is
(1-2q)/(1-q), q=|z2| squared, and changes sign. The extra t is present
for the **same obstacle**; it is absent from the transported old envelope.

## The Green-function paper

**DB11 -- Boundary-reduced principal divisor.** Definitions and
Theorems 1.3 and 1.7, physical 1--5: f is holomorphic and reduced on a
fixed neighborhood of the **closed** domain. Reducedness is not imposed
only in the interior. The Green class uses Lelong constraints, while
the divisor disc functional counts one-variable intersection orders
with negative logarithmic weights. Normalize the supremum of |f| on
the closure to at most one before using the nonnegative obstacle.

**DB12 -- The full SID signature.** Definition 1.4, physical 3--4:
S(z,tau) is jointly holomorphic near the closure and a full parameter
disk, S_0 is the identity, and for tau in a fixed complex sector its
image of the entire **closed** domain is inside Omega. Displacement
is O(|tau|); depth is bounded below by c|tau| near the boundary
divisor. At every singular boundary divisor point, f(S_tau(p)) is
not identically zero as a function of tau. No fixed center is required.
These conditions are more than a small inward displacement or
zero-locus invariance.

**DB13 -- Geometry supplies examples, with its own assumptions.**
Proposition 2.1, physical 11, uses a biholomorphism on neighborhoods
of both closures and an interior convex center **outside** the divisor.
A real convex segment and a smaller complex sector give the uniform
depth and escape conditions. The Reinhardt criterion, physical 12--14,
retains C1 radial geometry, hyperconvexity, the appropriate
no-boundary-disc B-regularity input and singular escape.
The Kohn--Nirenberg flow example, physical 6--7, is nonconvexifiable;
its B-regularity and holomorphic-support obstruction have external
Sibony/Kohn--Nirenberg inputs, not full proofs certified here.

**DB14 -- Canonical truncation and continuity.** Proposition 1.9 and
Theorem 1.7, physical 8--10 and full proof 29--33:
v_j=P_Omega min(-log|f|,j) increases pointwise to the residual off A;
the upper regularization of its supremum equals the residual on all
Omega. B-regularity then identifies v_j with continuous
Perron--Bremermann envelopes and gives residual continuity **off A**.
Local upper bounds give G_A tending to -infinity at A and hence
extended-real continuity of G_A. Residual continuity on all of A
is not a stated consequence of this proof.

**DB15 -- Moving center, rather than continuity assumed beforehand.**
Lemma 5.5, physical 29, applies the submean inequality to the PSH
pullback along tau -> S_tau(p). For any fixed arc of positive length
inside the allowed sector there are parameters tau_j of prescribed
modulus with residual(S_tau_j(p)) at least residual(p)-o(1).
It neither assumes continuity of the residual nor requires S_tau(p)=p.

**DB16 -- Uniform chart insertion.** Lemmas 5.1--5.4, physical 26--29:
a finite cover of the closed divisor separates compact interior,
regular boundary and singular boundary regions. Weierstrass units and
degrees are fixed uniformly on singular charts; individual roots are
not claimed holomorphic in the base. The insertion circles remain in
a narrower sector. The relative estimate uses
|a| <= |tau|+|tau-a| <= (1+2/kappa)max(|tau-a|,r);
its unit and degree constant is independent of the later truncation
level. The local inverse of S_tau is only used on a neighborhood
of the corresponding interior target point.

**DB17 -- Parameter order in source gluing.** Lemmas 3.1--3.5,
physical 15--23, and main proof 31--32:
fix target contours, their Rouche margins and source arcs first,
then the Cartan pair and harmonic cutoff, and choose the root
distribution integer last. Additive Cousin bounds are independent of
derivatives of the oscillating difference. The final slight radial
shrink restores discs holomorphic near the closed unit disk and its
logarithmic weight change is included in the error budget.
A tolerance chosen before its controlling contour is fixed would
not justify the asserted uniformity.

**DB18 -- Recovering the logarithmic loss.** Main proof, physical
30--33: with s_j=exp(-j), t_j=A0 s_j to the power 1/m_star and
eta_j=j to the power -1/2, the bad arcs have length O(1/j).
Singular relative insertions lose only a fixed constant; regular
relative insertions lose O(log j). The uninsertable regular part
has the same integrable O(log j/j) loss. Finitely many boundary
zeros have integrable logarithmic singularities. Vitali selection,
discarded tails and separated finite arcs are handled before
gluing. Jensen's formula at the moving center supplies the final
residual bound. This is a reading of the displayed argument,
not certification of every external functional theorem.

**DB19 -- The 2001 erratum is controlling.**
The original Theorem 3.9, physical 20--21, printed 1532--1533,
claims the missing comparison residual <= v-star after increasing
bounded boundary truncations. The complete 2001 erratum says
explicitly that this comparison cannot be concluded, the theorem
remains unproved, and the rest of the paper is unaffected.
The alternative candidate is the upper regularization of the
supremum of negative PSH u for which u-log|f| is bounded above
on the **whole domain**, rather than only locally at the divisor.
The erratum does not provide a counterexample. The new SID argument
is a restricted approximation proof, not a claim that the original
general comparison has always been valid.

**DB20 -- The older homogeneous result is complementary.**
Dieu 2005 Theorem 2.2, printed 184--185, proof 189--192, treats
hyperplanes through a common interior point under closure hull,
radial inwardness near the trace and good-barrier assumptions.
Corollary 2.9 includes strongly star-shaped pseudoconvex domains
which need not be B-regular. Its conclusion is continuity of the
residual on all Omega. Radial motion centered at the common
singular pole preserves that pole and fails SID escape there.
It is not a literal special case of the new deformation.

## Dependencies, diagnostics and open directions

**DB21 -- Functional weights and manifold scope.** DDF Theorem 1.1,
printed 172; definitions printed 173--174; Theorem 3.1 and
Lemma 3.2, printed 179--184: the Lelong and reduced Lelong
functional use the nonnegative point weight alpha, with or without
the disc multiplicity. Their envelopes agree in the stated manifold
or locally irreducible scope. The divisor Riesz weight instead is
the zero order of f composed with the disc. The Riesz--Poisson
identity is unambiguous at finite centers; polar extension requires
a convention. The published spray proof preserves its selected
target points exactly during parameter gluing. The new additive
divisor construction controls contours and intersection weights,
rather than literally identifying the two functionals.

**DB22 -- The actual uniqueness comparison.** Quasi-B-regular v1,
Lemma 2.6, physical 8--9: u is quasi upper bounded PSH; the
comparison function is maximal PSH with finite **lower** boundary
limits; the **upper** boundary limits of u are dominated outside
an Omega-pluripolar set. First add epsilon times a negative
boundary-polar PSH witness for upper-bounded u, use a compact
comparison domain, then take epsilon to zero. Upper-bounded
approximants extend the assertion to the specified class. Part (ii)
uses a harmonic comparison function and Omega-polar sets.
The positive Poisson kernel explains why the function-class
condition is essential. The proof is not being attributed to the
unread 2026 publication.

**DB23 -- Literal auxiliary formulas, distinct from main theorems.**
The twelve recorded elementary checks include the following:

- Dieu 2005, Lemma 2.6, printed 187: the example
  -log(|f|+1/j) is not C2 at a simple zero. The stated approximation
  has smooth alternatives such as -1/2 log(|f| squared+1/j).
- Dieu 2005, Corollary 2.11, printed 193: the conformal map is on
  the z1 slice, but the printed coordinate map applies it to z2.
  The intended map is (psi(z1),z2). A C-infinity neighborhood
  extension also does not follow merely from the printed C3
  boundary hypothesis; that assertion is not imported.
- Dieu 2005, Proposition 3.2 proof, printed 196: the printed
  peak base (Mw+1)/2 is not normalized to one at w=M for
  arbitrary M. The normalized base (1+w/M)/2 has the needed
  property. The unique-maximum representing-measure argument
  remains distinct from this normalization problem.
- DDF 2012, Lemma 3.2, printed 180--181: the displayed slash
  phase theta0+j/2k pi does not give the standard kth-root
  spacing. The required phases are theta0+2 pi j/k.
  The root-cell and winding argument uses equidistribution.
- Quasi-B-regular v1, Remark 2.5(a), physical 8:
  (-log|z|) to the power alpha, 0<alpha<1, is not PSH on
  the ball. Off zero its radial Laplacian is
  alpha(alpha-1)r to the power -2 times (-log r) to the
  power alpha-2, which is negative. It also takes
  +infinity on the interior coordinate axis.
- An interior obstacle |z| squared on the disk has PSH
  envelope |z| squared; its constant boundary datum has
  Perron envelope one. The continuous-obstacle and
  boundary-envelope terminology on v1 physical 3 therefore
  requires the relevant superharmonic hypothesis.

These checks establish only the displayed local facts. They do
not show that either new main theorem is false or that every
printed older proof is repaired. The source-only record does not
promote the checks into original mathematical results.

**DB24 -- Open directions and book relevance.** The new Green
paper's explicit questions, physical 33--34, ask for continuity on
arbitrary bounded B-regular domains, continuity and canonical
approximation on arbitrary C2 strongly pseudoconvex domains even
without convexifiability/SID, a stable higher-codimensional
ideal-disc insertion mechanism, and geometric criteria for SID.
The quasi-B-regular preprint, physical 6, asks about replacing
a strong plurisuperharmonic majorant by an ordinary one.

These are literature-attested complex directions, not new
canonical atoms in Chapter 72. They may be explained beside the
book's local comparison and boundary discussion. Identifying
complex divisor subtraction with a non-Archimedean residual
Siu decomposition, passing scalar root weights to arbitrary
ideals, or deriving non-Archimedean envelope closure requires
additional theorems. BJ22 Theorem 6.21 remains under the book's
existing conditional treatment.

## Verification and preservation

The calculation record has twelve passed elementary checks. A first
symbolic attempt stopped before writing its record because a real-log
power identity lacked the positive-radius branch needed by the example;
the recorded v2 checks it after r=exp(-y), y>0. An initial detail crop
used coordinates outside the smaller publisher page and was completed
using relative page coordinates; the prepared full pages were preserved.
Neither failed preparation is reported as completed verification.

All 425 active source inputs, both bibliography files, 108 protected
inputs, the generated 4,443-page book and index, the native catalogue,
92 prior frozen manifests and 160 prior exports are preserved.
No manuscript compilation or new book-page reading is claimed by this
source-only checkpoint. The preserved preceding build's successful
compilation and review are not extended to future edits.

The canonical inventory remains 42 active atoms in twelve formal
problem environments, with tiers (0,3,7,15,17). No original proof
promotion, independent model call, Xean run or verification receipt
is produced. The user-authorized normal GitHub work-branch push
will publish this review and its exact companion evidence manifest.

