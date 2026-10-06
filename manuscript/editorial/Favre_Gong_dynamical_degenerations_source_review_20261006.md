# Favre–Gong sequential hybrid dynamics: exact-source review, 6 October 2026

This checkpoint reads the whole of **arXiv:2406.15892v4**, Charles Favre
and Chen Gong, *Non-Archimedean techniques and dynamical degenerations*:
58 physical PDF pages, read as extracted text and actually displayed in
29 sheets. The arXiv submission history dates v4 to **20 June 2026,
03:27:01 UTC**; the PDF's internal date is **23 June 2026**. These are
different dates. Its Peking Mathematical Journal publication metadata
(2025, DOI `10.1007/s42543-025-00100-7`) does not constitute a reading of
the published edition. The diagnostics below concern the exact v4 PDF.

The work adds a useful direction to the book: a single relative projective
line for an arbitrary sequence of rational maps, rather than only a
meromorphic one-parameter family. Resultant-dependent exponents organize
the complex fibres and the nonprincipal Robinson-field fibres. Probability
measures and **rescaled**, intrinsically defined Lyapunov exponents are
the relevant continuity statements.

The main equilibrium-measure and intrinsic Lyapunov-continuity assertions
are **not refuted by this review**. Several literal auxiliary statements
and displayed formulas fail elementary tests, and some proof steps require
additional justification. **A complete repair is not certified.** The
twenty-seven records are not twenty-seven counterexamples to the main
theorems. This checkpoint admits no original result, independent model
call, verification receipt or canonical problem-status change.

## Exact editions and actual reading

| Source | Edition actually read | Actual PDF pages read/displayed | Scope |
|---|---|---|---|
| Favre–Gong | arXiv:2406.15892v4 | 1–58 | Entire PDF, including references |
| Rumely, *The Minimal Resultant Locus* | arXiv:1304.1201v2 | 1–3, 13–14 | Reduction definitions, strong topology, main statement and its concluding proof |
| Luo, *Limits of rational maps, R-trees and barycentric extension* | arXiv:1905.00915v4 | 1–3, 22–23, 28–31 | Scale, degeneration criterion, degree and moduli conclusions |
| Luo, *Trees, length spectra … and Berkovich spaces* | arXiv:1907.06220v2 | 1–2, 16–24 | Robinson field, tree correspondence and meromorphic-family interface |
| Poineau, *Dynamique analytique sur Z. I* | arXiv:2201.08480v5 | 1, 3–6, 13, 38–41 | Good-ring hypotheses, relative measures, potentials and the final continuity proof |

The fresh total is **93 distinct source/page pairs in 48 displayed
sheets**: 58 main pages and 35 selected dependency pages. Only the main
paper was read in its entirety. No full external dependency chain or
published Luo/Rumely/Poineau PDF is certified. The current arXiv version
histories were checked: Rumely v2, 5 April 2013; Luo's first paper v4 and
second paper v2, 15 December 2021; Poineau v5, 11 August 2025.

The main PDF is
`source_material/hybrid_dynamics_next_sources_20261006/Favre_Gong_2406_15892v4.pdf`,
888,615 bytes, SHA-256
`89a46e03bc6a4624859715740991cf7407a62b961b1f207a7c31a6779c35011e`.
The frozen main reading record has SHA-256
`0729b205a82761e0e949d08d04439015ff699598882217226e6ca8b0db6575b6`;
the selected dependency reading record has SHA-256
`c00b6a877f2b10dc6803073dc01470e13db6ee9f06ce208155ea543724b824ff`.
Their manifests pin every displayed image, selected text and source PDF.
Acquisition and keyword-location scans are not counted as reading.

Primary links: [Favre–Gong v4](https://arxiv.org/abs/2406.15892v4),
[Rumely v2](https://arxiv.org/abs/1304.1201v2),
[Luo's first paper v4](https://arxiv.org/abs/1905.00915v4),
[Luo's second paper v2](https://arxiv.org/abs/1907.06220v2),
[Poineau v5](https://arxiv.org/abs/2201.08480v5).

## Source diagnostics and boundaries

**F01 — Resultant scale, pp. 5–6, 29–30.** For the optimized normalized
resultant R_n and C_d=e sup R, the formal definition is
epsilon_n=1/log(C_d/R_n), with 0<epsilon_n<=1. Consequently
R_n^{epsilon_n}=exp(-1) C_d^{epsilon_n}, tending to exp(-1) when
epsilon_n tends to zero. The exponential printed in the proof on p. 30
does not equal this expression. Use the formal definition and the correct
identity to justify the unit resultant. On a principal fibre the
intrinsic exponent is epsilon_n times the usual complex exponent; an
unscaled complex exponent is not what the main theorem transports.

**F02 — Good and potential good reduction, pp. 6, 20–22.** The
single-point Julia criterion in the introduction needs *potential* good
reduction. The later Theorem 2.5 and discussion on p. 22 use that precise
notion. For g(z)=t z^2 with 0<|t|<1, the normalized lift has resultant
norm |t|^2, whereas z↦tz conjugates it to z^2. It has potential good
reduction and a singleton Julia set without good reduction in those
coordinates. Rumely's pp. 1–3, 13–14 explicitly distinguish the notions.

**F03 — Weak topology and path topology, pp. 12, 20.** Path-distance
continuity means the strong topology, not the weak Berkovich topology.
For fixed 0<r<1 and distinct residue classes a_j, points zeta(a_j,r)
converge weakly to the Gauss point while their distance from it remains
-log r. Rumely's main theorem explicitly specifies the strong topology.
The additional word “proper” on p. 20 also needs a topology: bounded
sublevels need not be compact for the strong metric when infinitely
many residue directions are available. Minimum attainment on the
finite fixed-point/pole tree is a different assertion.

**F04 — Trivial valuations and type-3 disks, pp. 11–12.** The finite-chart
list for a trivially valued algebraically closed field omits the
infinity branch, including |P|=R^{deg P} for R>1. For a type-3 disk,
the classical-disk formula must in general use a supremum, not an
attained maximum: |z-a| has seminorm r when r is outside the value
group. The coefficient/Gauss formula remains the appropriate definition.
The actual nonprincipal fields in this application have value group
R_{>0}, so this particular type-3 issue does not occur there.

**F05 — Projective points over an arbitrary ring, pp. 11, 27, 29.** A
general B-valued projective point is an invertible quotient of B^2;
it need not have a globally trivial quotient line. Likewise a general
relative map may require line-bundle data. The unimodular-pair formulas
must retain their trivialization scope. Normalized complex sequences
do give unimodular pairs over A^epsilon as in Lemma 3.12. That concrete
application is not a license for the same coordinate description over
every Banach ring.

**F06 — Subharmonicity on finite graphs, pp. 14–16.** Edgewise
convexity and the full outgoing-branch balance are not equivalent to
convexity on every path through a branch point. For example log|z| is
harmonic near the Gauss point, but along a path from the zero direction
to a neutral residue direction its slopes decrease from 1 to 0.
Furthermore the Laplacian of a restriction to a compact graph has
endpoint terms and can be signed. On U=A^1, u=log|z| has Laplacian
delta_0, while on Gamma=[zeta(0,r),x_G] the outward-slope graph
Laplacian is delta_{zeta(0,r)}-delta_{x_G}. Thus the stated equality
between the projected open-domain Laplacian and the graph-restriction
Laplacian needs boundary terms. Use the standard potential operator,
proper subharmonic functions and explicit boundary data; this diagnostic
does not refute the standard equilibrium construction on pp. 21–22.

**F07 — Ultrafilter bookkeeping, pp. 22–25.** Proposition 3.4(3)
requires a nonprincipal ultrafilter to extract a subsequence with
strictly increasing indices. A principal ultrafilter applied to x_n=n
already shows the unrestricted statement fails. In Theorem 3.8,
x_E is initially 0 on E and 1 on E^c, but the proof subsequently uses
it as the indicator of E. As printed, its putative ultrafilter contains
the empty set and the product-intersection identities fail. Reverse
the indicator convention consistently. Neither issue refutes the
Stone–Čech spectrum theorem.

**F08 — Residue-field representatives, p. 25.** Boundedness along an
ultrafilter is not global boundedness of a representative sequence.
For e=lim_omega epsilon_n>0, coefficients are bounded on an omega-big
set; they may be arbitrarily large outside it. Modifying them on the
thin complement supplies a bounded representative. The assertion that
the complete field equals A^epsilon/ker omega also requires identifying
the quotient norm with the residue norm; closedness of the ideal alone
does not identify those two norms. Keep those representative and norm
steps explicit when using lifts of matrices or points.

**F09 — Spherical-completeness diagonal, p. 26.** Nested closed balls
give non-strict centre inequalities, not the displayed strict ones
without a cofinal/slack argument. More substantially, j_n=min N_n
does not guarantee n∈N_{j_n}, which is needed for the asserted estimate
for alpha_{j_n,n}. A compatible diagonal uses the depth of n in the
decreasing big sets, with uniform bounds and closed-ball limits retained.
Luo's selected Robinson-field proof is corroborating source material,
not a complete certificate for the literal diagonal printed here.

**F10 — Root lifting on big sets, pp. 26–27, 38.** Proposition 3.11
cannot demand a degree-m factor for every coordinate n of an arbitrary
polynomial over A^epsilon. Take P_1=1 and P_n=z for n>=2 and a
nonprincipal omega: P_omega=z has a root, but P_1 has no linear factor.
The conclusion and the Rouché proof apply on an omega-big set, with
arbitrary bounded fillings or modified polynomial data on its complement.
The transfer proof on p. 38 ultimately uses such a big set, so the
literal all-n failure does not itself refute its continuity conclusion.

**F11 — Comparable exponents and representatives, pp. 28–30.** In
Proposition 3.16 the ratio alpha_n=epsilon'_n/epsilon_n need only lie
in a compact interval of R_{>0}, not in (0,1]. For example doubling
epsilon_n where it is at most 1/2 gives alpha_n=2. Comparable positive
ratios still give the needed power homeomorphisms. Remark 3.19 also
needs g_n to represent the same conjugacy classes as f_n; comparable
resultants alone do not conjugate arbitrary rational maps. Keep the
field isomorphisms, power normalization and conjugacy hypotheses separate.

**F12 — Boundary union versus minimum, pp. 18–19.** A local equation
for the union of the two resultant divisors is a product. Its absolute
value is not uniformly comparable to the minimum of the two factors
near their intersection: with both factors of size s, the ratio is s.
With bounded coefficients, power inequalities can replace the claimed
comparability, and the exponent in Lemma 2.4 can absorb this change.
This is a gap in the displayed justification, not a counterexample to
the two-sided power comparison itself. The valued-field extension of
the Łojasiewicz/GAGA argument remains an explicit dependency gate.

**F13 — Optimized moduli resultant, pp. 17–20.** The normalized
resultant on Rat_d is proper and its logarithm has the indicated
psh description. Do not transfer psh to the optimized quotient
function: Remark 2.3 explicitly leaves that unclear. The continuity
proof also relies on lifting convergent quotient classes and on the
appropriate complex/non-Archimedean quotient theory. Poineau's
Fréchet–Urysohn result and Maculan's quotient assertions were not
fully read in this checkpoint. The normalized determinant of a
projective matrix is |ad-bc|/max|entries|^2; it is not the literal
determinant 1 of an unnormalized SL_2 representative.

**F14 — Bounded continuous families need not be compact, p. 33.**
Remark 4.4 fails for the pointwise evaluation topology, as well as
for the compact-open interpretation. Over beta N let h_j be the
continuous indicator of the clopen closure of {n>=j}, and take the
continuous family h_j(omega) delta_infinity. Its mass is at most 1.
Its pointwise limit is 0 on principal points and delta_infinity on
nonprincipal points, which is discontinuous. Any convergent subnet
would have that same limit. Compactness of measures on a *fixed*
compact space is distinct from compactness of continuous families.
The later uniform-potential proof does not require this remark.

**F15 — Proper quasi-model functions on every relevant fibre, pp. 35, 47–49.**
Arbitrary section collections may vanish identically on a fibre. With
a_1=0 and a_n=1 for n>=2, the collection {a z_0,a z_1} gives a
quasi-model function identically -infinity on the first fibre.
Its Laplacian is not the finite signed measure of Lemma 4.6, and
its integral is not finite as claimed in the unrestricted extra
assertion of Theorem 5.8. Require a nonzero collection on each relevant
fibre. Continuous model functions already meet that requirement;
the critical section for a degree-d map over these characteristic-zero
residue fields is also nonzero. Do not conflate this definite auxiliary
counterexample with a failure of equilibrium-measure continuity.

**F16 — General model-function density, pp. 35–37.** The concrete
ring A^epsilon has the unit (2^{-1/epsilon_n}) of constant spectral
norm 1/2. This is the useful property (N) witness. The broader
Remarks 4.11–4.12 are not valid as stated: for an algebraically closed
trivially valued field, its one-point spectrum is vacuously separated
by D(M(B))={0}, while (N) fails. Basepoint-free homogeneous model
functions on its projective line are identically zero, so adjoining
the constant 1 cannot make them dense in all continuous functions.
Poineau's different test class includes rational additive constants
and keeps a good-ring hypothesis. Do not identify the two test classes.

**F17 — Truncation formula in the lattice proof, p. 36.** A difference
max(L,A)-max(L,B) need not equal max(L,A-B). For L=0,A=-1,B=1
the values are -1 and 0. The printed section construction for the
truncated function therefore needs adjustment. Tensoring the P
section with the denominator collection before taking the union
gives max(L+B,A)-B=max(L,A-B). Separation also has to use normalized
homogeneous evaluations, rather than assuming that unequal affine
polynomial values remain unequal after division by the reference norm.
This records the algebraic correction needed for a density proof,
not a certification of all arbitrary-ring claims.

**F18 — Polynomial norm is multiplicative, pp. 39–40.** The
homogeneous map F=(P,Q) has d^2 affine preimages of a generic point.
Thus F_*(cR)=c^{d^2}F_*R; the map called “linear” is not linear and
the estimate ||F_*R||<=C||R|| with C independent of R fails.
For F=(z_0^2,z_1^2), R=c z_0 gives F_*R=c^4 z_0^2. The correct
kind of bound retains the power ||R||^{d^2} and dependence on the
degree/lift. Polynomial degree dl and the logarithmic pushforward
identity are separate assertions. Differences at common logarithmic
zeros are understood by continuous extension/distributions, not
literal subtraction of two -infinity values.

**F19 — Hyperbolic and spherical normalization, pp. 40–41, 46, 51.**
The Euclidean disk |z|<=sqrt(t) has chordal radius sqrt(t/(1+t))
about 0, not sqrt(t). The Fubini–Study probability density transported
by z↦tz is t^2/[pi(t^2+|z|^2)^2] against Euclidean area; the p. 46
factor 1/4 does not integrate to 1. Its outside-disk mass is t/(1+t),
so the needed O(t) estimate survives. The ball metric matching
curvature -1 is 4|dx|^2/(1-|x|^2)^2; omitting 4 prevents the stated
isometry to the upper-half-space metric. Keep exact constants separate
from logarithmic-scale comparability.

**F20 — Canonical-measure potential under a powered norm, p. 42.**
The displayed g_n lacks the normalization needed for homogeneity and
vanishing as epsilon_n tends to zero. In powered homogeneous
coordinates a valid relative potential is
log max(|z_0|,|z_1|) - (epsilon_n/2)
log(|z_0|^{2/epsilon_n}+|z_1|^{2/epsilon_n}). Its absolute value is at
most (epsilon_n/2) log 2. This preserves the Haar/Fubini–Study
Laplacian difference under the powered-field convention and yields
the required uniform vanishing. In the positive-exponent case,
rotation invariance alone does not characterize Haar measure on the
sphere; support on the unit circle is also needed.

**F21 — Reference term under a projective coordinate change, pp. 43–45.**
The disk test's constant is log r, not -r. More importantly,
phi_sigma∘M differs from phi_{M^*sigma} by the reference-norm term
d(log max|z|-log max|Mz|). Pulling back the numerator sections
without that term is not an identity of relative weights. The
continuous correction can be retained in the model-function span;
the p. 44 displayed denominator correctly shows why it is necessary.
This is the same reference-weight distinction kept in Chapter 66.6.

**F22 — Maximum of singular quasi-model functions, p. 49.** Lifting
the common factor Q_omega separately gives Q_{i,n}; it does not give
a common factor Q_n for the coordinate polynomials. Comparing the
remaining factors therefore does not give the comparison of the
original polynomials used in the final inequality. Take P_{1,n}=z,
P_{2,n}=z-a_n with nonzero a_n tending to zero faster than the
powered scale. Both residual factors are 1 after the limiting
common factor z is removed, yet at z=0 one original logarithm is
-infinity and their maximum is finite. Also, a neighbourhood of a
base point cannot be required to avoid the zeros of *every* residual
factor if some of those factors vanish there. A proof using uniform
integrability of a proper single-section majorant and truncations
would address the singular maximum passage, but that passage is
kept as a proof obligation here. No counterexample to the properly
scoped integral-continuity assertion is claimed.

**F23 — The scalar 1/d belongs inside the valued absolute value, p. 50.**
Write J=P_{z_0}Q_{z_1}-P_{z_1}Q_{z_0}. The derivative formula
uses |J/d|, not the numerical real prefactor (1/d)|J|. On C^e the
factor is d^{-e}; on these nonprincipal Robinson fields |d|=1.
For f(z)=z^d, the intrinsic spherical derivative on the unit circle
of C^e is d^e, and on the Gauss point it is 1. The printed formula
instead gives d^{2e-1} and 1/d. Thus the intrinsic Lyapunov values
are e log d and 0 respectively. These exact tests diagnose the
displayed formula; they do not refute continuity of the intrinsically
defined exponents. Over arbitrary characteristic-zero valued fields
one must retain |d| as well; characteristic zero does not imply |d|=1.

**F24 — Scaled equivalence relation in an asymptotic cone, pp. 50–51.**
The zero-distance relation must be lim_omega d_H(x_n,y_n)/r_n=0.
The printed unscaled relation gives a pseudometric rather than the
claimed metric quotient: x_n=(0,1), y_n=(0,exp(sqrt(r_n))) have
unscaled distance tending to infinity and scaled distance tending
to zero. The standard scaled construction and the correspondence
in Luo's selected sections are the relevant objects.

**F25 — Two directions of resultant/Luo-scale comparison, pp. 52–54.**
The proof obtains a degree-d map over the Robinson field and hence
a nonzero resultant. That gives an upper bound for -log R_n/r_L(f_n),
but does not by itself give a strictly positive lower bound; the
residual resultant could have norm 1. The r_L-normalized construction
must also retain a preimage of the base point at nonzero limiting
distance, ruling out good reduction at the Gauss point. Luo's
moduli conclusion on p. 31 of the first paper explicitly rules out
totally invariant points. Keep this additional geometric step when
using a two-sided comparison. A complete repaired proof of Theorem
6.3, including every cited annulus/barycentre dependency, is not certified.

**F26 — Conjugacy directions and pushed smooth measures, p. 54.**
If L_n(y_n)=x_star, then psi(y)=L_omega^{-1}(x_G), and the
corresponding normalized composition is L_omega f_omega M_omega.
The displayed inverses instead match the other convention
L_n(x_star)=y_n. Choose one convention consistently. A nonconstant
rational map also need not push a smooth area measure to a smooth
measure: z↦z^2 has a density singular at the critical value 0.
Non-atomicity and barycentre continuity are the appropriate inputs;
the claimed smoothness equivalence is too strong.

**F27 — Elimination pivot, pp. 54–55.** After dividing the Q
coefficients by c_n, the coefficient killed in Q/c_n-t_n P is
obtained by t_n=b_{k_0,n}/(c_n a_{k_0,n}), not by the printed
a_{k_0,n}/b_{k_0,n}. The latter does not make gamma_{k_0,n}=0
in general. The remaining degree argument depends on that zero.
Read Luo's original normalization as a separate primary source;
do not treat a citation to it as a verification of this printed pivot.

## Dependency boundaries

Rumely's read main theorem specifies the **strong topology**, the
finite tree containing the minimum locus, parity-dependent point/segment
alternatives, and the coordinate-invariant zero minimum for potential
good reduction. Its proof on pp. 13–14 cites earlier lemmas not fully
read here. The printed Proposition 1.8 radius condition on p. 13 uses
the type-I endpoint where it should use the interior point xi; p. 14
uses the intended xi. This is an additional local notation guard,
not a full audit of Rumely's published proof.

Luo's first read paper provides the fixed-degree Lipschitz statement,
the proper degeneration scale, branched-cover conclusion and the
moduli version with no totally invariant point. The selected passages
do not cover the full extremal-length proof or every annulus lemma.
The proof of Theorem 8.12 continues beyond our selected p. 31 and
is not claimed as fully read. Its limiting tree is a **branched**
covering; it is not an everywhere unramified covering of a tree.

Luo's second read paper provides the explicit Robinson field and
affine construction of the tree isometry, and the statement/proof
passage for Theorem 7.3. Local transcription guards remain: on p. 18
the nested-set difference must use the nonempty orientation, and
strict inequalities need not survive an ultralimit; on p. 19 a
moderate root bound can absorb the fixed factor d by lowering, not
raising, the exponent of rho<1. Distinguish the algebraic Puiseux
field from its completion when discussing arbitrary unbounded
denominators. On p. 23 retain multiplicative/logarithmic coefficient
normalization, the domain-correct conjugacy Phi B=F Phi, and
|b|<=1 for affine transformations fixing the Gauss point. These
guards do not refute the established tree correspondence, nor
certify the entire external chain.

Poineau's Definition 2.3 on p. 13 requires a geometric base ring,
a sufficiently unmixed spectrum, and local arc connectedness of
the spectrum and its ultrametric part. A^epsilon has spectrum
beta N, which is totally disconnected and has non-isolated
nonprincipal points; it cannot simply be declared a good ring
under that definition. Theorem A/6.26 is a separate relative-line
continuity theorem for a finite flat polarized degree-d map over
a good base. Its concluding proof on pp. 40–41 uses continuous
relative potentials, dense test functions with locally uniform
Laplacian variation, and the estimate
2 eta + ||rho_n|| M_eta. The density and variation results cited
there are not fully read in this checkpoint. Its auxiliary extension
of the base also needs a valid descent/quotient argument; continuity
of a surjection alone is not a universal descent criterion.
Do not import the optional energy-pairing sign formula without
checking the chosen pairing and Laplacian conventions. The repeated
A^1 symbols in a proof about the compact projective fibre do not
justify an affine probability or properness assertion.

The iteration and rescaling corollaries in Favre–Gong pp. 31–32
are recorded as attributed literature statements, not fully certified
new proofs. Their coordinate changes require bounded normalized
determinants at the chosen scale; invoking Lemma 2.4 alone does
not display every comparison with iterated resultants. No claim
in positive characteristic is promoted from the speculative remark.

## Book admission and preserved state

This is a **source-only** checkpoint. All 425 active manuscript
inputs, both bibliography files, 108 protected inputs, the compiled
book and generated index, 82 preceding frozen manifests and 142
exports are preserved. The current book remains the index-polished
4,417-page PDF, SHA-256
`6659448ecfb0a315839c2d0f60efd6d6169da98a642ece56088f0b3ab320eac2`.
No fresh book build or book-page rereading is claimed. Exact-byte
preservation permits reuse of the preceding reference/inventory gates;
the source-review release gate checks the new records and git diff.

The native catalogue source/PDF and its open editor remain untouched.
The canonical inventory stays at 42 atoms in twelve families with
tier counts (0,3,7,15,17). The general BJ22 Theorem 6.21 Siu/envelope
boundary remains separate and conditional. No original result,
production verifier, historical-receipt extension or problem closure
is asserted.

For the next book integration, retain the arbitrary-sequence Banach
ring construction, the positive resultant scale, intrinsic derivative
normalization and the distinction between weak measure continuity
and tree-metric statements. Use properly scoped source-attested
statements or explicit continuity/uniform-integrability inputs,
with the uniform-potential proof interface visible. Independently
integrate the known K3 symmetric eigen-current normalization from
the preceding Cantat/Filip review, keeping the meromorphic-family
and positive-product hypotheses explicit. Neither route supplies
a general Siu decomposition or envelope-closure theorem.

Fetch both main and work under standing authorization, preserve any
incoming author research, then commit normally and push work. The
matching immutable manifest records the exact editions, actual
reading and preservation evidence. No force push is authorized.
