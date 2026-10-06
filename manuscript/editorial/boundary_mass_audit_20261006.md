# Boundary barriers, local mass and fixed interior buffers

**Known qualitative source mechanism and scoped explanation.** The
baseline is `8199363dd1ef41e5fb368916114426fd45529641`. Chapter 68.9.7
explains local boundary control; Appendix L.58 records exact sources
and retained quantitative gates. The earlier logarithmic ample-locus
paragraph now states its fixed positive interior buffers and starting
iteration radius. No original result or complete repaired external
quantitative proof is admitted.

## Mathematics and scope

Nguyen's published Theorems A and B consider a bounded strictly
pseudoconvex domain with smooth strictly plurisubharmonic defining
function, a positive measure dominated by the Monge--Ampere measure of
a Hölder plurisubharmonic zero-boundary subsolution, and continuous or
Hölder prescribed boundary values. Neither the prescribed measure nor
the subsolution's Monge--Ampere measure must have finite total mass.
The conclusion is the ordinary unique continuous Dirichlet solution,
with positive Hölder regularity for Hölder boundary values. The common
positive normalization of ddc can be rescaled; no compact Hermitian
total-mass identity is introduced.

The homogeneous boundary envelope and the envelope plus subsolution
bound the solution on both sides. Their common positive Hölder exponent
may be lower than the original boundary exponent. These actual barriers
control the collar and justify gluing a shifted ball-average maximum
to the solution. Boundary values alone would not justify this gluing
for an arbitrary bounded plurisubharmonic function. The homogeneous
Monge--Ampere envelope is maximal, not generally pluriharmonic in
dimension greater than one.

For a bounded subharmonic potential the defining-function argument
bounds the Laplacian mass on Omega_delta by C/delta. The Jensen error
is integrated on Omega_2delta with trace mass measured on Omega_delta:
the sampled balls must stay in the larger region. This gives an
O(delta) error; the remaining collar also has volume O(delta). An
O(delta^2) estimate with global mass instead requires finite total
Laplacian mass. The regions and finiteness assumptions are stated
before the estimates are used.

The collar extension phi_epsilon=max(phi-epsilon,A rho/epsilon) can
have growing mixed masses. The normalized family
epsilon phi_epsilon=max(epsilon phi-epsilon^2,A rho) has uniform
Hölder and supremum bounds. Applying exponential capacity domination
to that family and undoing n-homogeneity keeps the epsilon^(-n)
prefactor. A crude unnormalized Hölder bound alone would not justify
a uniform exponential constant. The source's localized stability and
weighted transfer yield positive exponents and a balance between the
barrier error and delta^(a2 a3)/epsilon^(2n+1). The book explains this
qualitative balance without asserting sharp numerical regularity.

Near the boundary, conversion from mean error to oscillation uses the
already available boundary modulus. Without boundary control, fixed
nested interior neighborhoods K compactly contained in U0 compactly
contained in U1 are chosen first. A dominating smooth local background
makes the potential subharmonic and adds only an O(delta^2) error.
The nested-ball iteration is stopped at a positive radius below the
fixed buffer; boundedness controls its initial oscillation. For the
logarithmic modulus the contraction is made explicit in equation
68.23di. The final constant may depend on the buffer and initial
modulus value. A finite coordinate cover gives the fixed-compact
consequence. The literal stronger boundary-free shrinking-collar
assertion in the cited modulus note is not used.

The Benali--Zeriahi erratum has a different signature: finite
prescribed measure, a bounded strongly m-pseudoconvex domain, and a
Hölder zero-boundary subsolution in E_m^0 with finite total Hessian
mass. Smooth boundary data permit the corrected global mixed-mass
argument; arbitrary Hölder data require the power-difference argument
and local trace mass. The original Proposition 2.20's displayed
capacity recursion gives an extinction scale proportional to
c(0)^((tau-1)/m), whereas the next printed expression uses
c(0)^(tau-1). The erratum still invokes that proposition. Its printed
numerical exponent is therefore not certified here. This diagnoses
the displayed derivation, not a counterexample to the qualitative
Hölder theorem or a complete repair of its quantitative proof.

These local and fixed-compact inputs do not supply uniform second-order
estimates for unknown-dependent auxiliary densities, identify geodesic
velocity with a spectral measure, or repair the general non-Archimedean
Siu decomposition or closure claim. The BJ22 Theorem 6.21 proof issue
retains its established scope, distinct from a theorem counterexample.

## Primary reading reused

The preceding [boundary source review](Hessian_boundary_erratum_source_review_20261006.md)
fully read and displayed all four exact PDFs, 77 physical pages in
39 sheets. Four identically hashed Zeriahi pages were previously read;
73 pages were fresh, comprising 68 research and five publisher pages.
This integration reuses that record and claims zero fresh primary pages.

- Nguyen, *On the Hölder continuous subsolution problem for the complex
  Monge--Ampère equation, II*, Analysis & PDE 13(2) (2020), 435--453,
  DOI `10.2140/apde.2020.13.435`: all 22 actual pages; actual 1 is the
  publisher cover, 2--20 research, 21--22 publisher matter.
  PDF SHA-256:
  `c3b57a3b4eaa0b3f2abbae6085d54c21e6226bc34005edcfa6be471e149d1a5d`.
- Benali--Zeriahi, *The Hölder continuous subsolution theorem for
  complex Hessian equations*, JEP 7 (2020), 981--1007,
  DOI `10.5802/jep.133`: all 28 actual pages, cover 1 and research
  2--28. Proposition 2.20 is on actual 14--15.
  PDF SHA-256:
  `791646c992aa972d1bd12a75ccb7910ab40ac153ba9b77d0364303c033c59e74`.
- Its explicit erratum, JEP 8 (2021), 779--789,
  DOI `10.5802/jep.157`, published online 22 March 2021: all twelve
  actual pages, cover 1 and research 2--12. Corrected Theorem B' is
  on actual 3, boundary-dependent mixed mass on 4--5,
  power differences on 6--9, regularization on 10--12.
  PDF SHA-256:
  `1ef038b5d22de71df875ad28c2140c8ba9c54dd41c8f3cfe937e8fe043d1321e`.
- Zeriahi, *Remarks on the modulus of continuity of subharmonic
  functions*, [2007.08399v1](https://arxiv.org/abs/2007.08399v1):
  all fifteen actual pages. Primary v1 submission metadata is
  16 July 2020 at 15:20:28 UTC; the acquired PDF internally prints
  27 November 2024. No 2024 submission is inferred. Actual 9--12
  repeat the identical earlier file; Theorem 3.2 and Lemma 3.3 and
  their nested-ball proof retain their separate boundary scopes.
  PDF SHA-256:
  `8c55994b7b24f944cb5070669e2af5e7f2d995367b115934e30281d65e4ab16f`.

The full reading record has SHA-256
`d3175b7e15e7bd531bbaf8420071c1626a54adeff37d65ddc5bd3983ce8b3c44`;
the frozen source-review manifest has SHA-256
`6de8d2f4b6543fb8016ffbd1e9a6e0409219a9aeaf57ec5cdb630fc4d2a2b042`.
Fourteen exact diagnostics distinguish false literal assertions,
repairable formulas and cleared objections. No main qualitative PDE
theorem counterexample or exact numerical stability repair is claimed.
Three publication-specific bibliography entries are added.

## Final validation and PDF review

The final v2 book has **4,401 pages**, 20,453,590 bytes and SHA-256
`efd8bca72071fb90847fe563164c99eafc8ce9d68fd4aba2f8719ae61214463b`.
TeX errors, package/pdfTeX warnings, missing glyphs, overfull boxes,
unresolved references/citations and rerun requests are zero. The 954
nonfatal underfull diagnostics equal the preceding count. Both builds
succeeded: v1 had 4,403 pages and only fourteen pages were actually
reviewed before the new provenance conclusion was shortened to avoid
an orphaned paragraph. Its partial scope is frozen separately. The
final source, build and PDF gates are v2; v1 views are not claimed as
final-v2 reading.

References contain 425 active inputs and 12,862 unique labels, with
zero missing inputs, duplicate labels or dangling references. There
are 384 cited entries among 679 unique bibliography keys and zero
bibliography warnings. Six labels and four explicit equation tags
are new; all 148 Chapter 68 equation numbers are unique. No index
entry is added. The index accepts 764 entries, rejects zero, and
has 1,012 lines, 763 page groups and 419 valid numeric destinations.
Navigation has 21,982 named destinations, 47,079 internal links,
171 external URL links, 2,568 contents entries and six parts;
invalid internal links and destinations are zero.

All **42 matching final-v2 physical PDF pages** were displayed and
their complete extracted text read in 21 sheets: actual 61, 68,
3617--3619, 3624--3627, 4162--4165 and 4373--4401. They cover the
affected contents, fixed-buffer clarification, new boundary discussion
and neighboring transitions, provenance and following appendix, and
complete final index and bibliography. View-manifest SHA-256:
`11b2a46596e9905d004380e7d9c3f149f86a8b305ef0d67a0a864b945b980374`.
Final reading-record SHA-256:
`0e6eb186c00825536d6ad7aa6ed512f76240cc8e850beaa66577fb5fda09d9f7`.
This checkpoint does not claim a new reading of all 4,401 pages.
Existing bibliography accent/spacing and duplicate-edition questions
are retained for a separate usage-aware polish; no such cleanup is
claimed by this integration.

## Preservation and publication

Chapter 68 and Appendix L are the only changed active inputs. All 423
others and all 108 protected inputs retain baseline bytes. The edited
files preserve 34 existing statement/explanatory blocks and twelve
proof blocks, 46 in total, with no new formal environment. The
non-Archimedean bibliography is unchanged. README and the research
programme record the completed integration.

All 72 prior frozen manifests, 56 integrations and sixteen source
reviews, and all 124 prior exports retain their bytes. Apart from
the five changed baseline paths, the other 5,066 tracked baseline
files are unchanged. The canonical inventory passes with 42 atoms,
twelve families and tier counts 0/3/7/15/17. Complete status rows,
the inactive toric candidate and native catalogue source and PDF
retain their bytes. The native editor remains open without editing,
recompilation or tab change.

The release comprises the full PDF, a 42-page review PDF and a source
archive with 678 byte-verified members and passing CRC. All 425 active
inputs and both bibliographies are included, with inherited support,
current provenance and four preceding dependency source-review pairs.
Ignored primary caches and the current external artifact record are
excluded. No fresh isolated archive compilation is claimed. The
integration manifest, closure and artifact record pin the edition.
Main and work were explicitly fetched before publication on work and
the existing draft PR; no incoming author changes were found. Routine
GitHub synchronization follows standing user authorization and retains
platform permission checks.

No original result, independent production model call, verification
receipt, canonical solved status or general Siu/closure repair is added.
Continue with the fifteen-page Wang tau-invariant preprint and its
relationship to metric-graph Green functions and energy. Only primary
metadata and the abstract have been read so far; neither its claimed
uniform bound nor its claimed cubic counterexample is admitted here.
