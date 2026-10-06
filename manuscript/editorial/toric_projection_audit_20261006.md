# Toric directions, secondary polytopes and finite certificates

**Known finite argument import and direct substitutions.** The controlling
baseline is `cf47c2a29d9afaa6e528df2f5cc723a8a5d0e736`.
Chapter 68.7.2 explains Li--Sheng--Yao,
[*K-unstable Toric Varieties and Secondary Polytopes*, arXiv:2610.05179v1](https://arxiv.org/abs/2610.05179v1),
submitted 4 October 2026 at 12:41:11 UTC. Appendix L.54 records the source
scope. The finite construction is separated from continuum regularity,
the Delzant convergence theorem and general lattice asymptotics.

## Argument and normalization

Let A be a full-dimensional finite marked set in R^n, n at least one,
Q its convex hull, N its cardinality and V_Q its Euclidean volume.
Triangulations may omit marked points. Dividing incident simplex volumes
by (n+1)V_Q gives normalized GKZ vectors g_T of total mass one. Their
convex hull is the secondary polytope Sigma(A). For any nodal vector f,
the minimum of its pairing with this polytope is V_Q^{-1} times the
integral of the lower convex envelope f^vee. A lower regular triangulation
attains this value; any triangulated interpolation is above the envelope.

The unique closest point p_A to the origin satisfies the projection
inequality against every g in Sigma(A). Since all vectors have mass one,
the closest point to the constant barycenter c_A=(1/N,...,1/N) is also p_A.
The support identity and Cauchy--Schwarz give the lower bound
-||p_A-c_A|| for the normalized finite Mabuchi functional. When negative,
the minimizing ray is p_A-c_A, unique up to positive scaling. The
semistability criterion is c_A in Sigma(A), equivalently p_A=c_A.

The proof that p_A itself is convex is included: its lower envelope rho
satisfies 0<=rho<=p_A, and their support minima agree. The projection
inequality, equality of envelope integrals and two norm bounds force
rho=p_A. This uses the finite nonnegative GKZ coordinates, not an
unproved continuum regularity assertion.

All GKZ vectors have the same projection ell_A onto the full affine
subspace because their affine moments are the same normalized integrals
over Q. With Pi the complementary projection, relative semistability
is 0 in Pi Sigma(A), equivalently ell_A in Sigma(A). Absolute
semistability forces ell_A=c_A, but that equality alone is insufficient.
For A={-1,-1/10,0,1/10,1}, Q=[-1,1] and f=|x|, ell_A=c_A while the
finite Mabuchi value is 11/25-1/2=-3/50. Thus the source's extra
Theorem 29 equivalence is not imported; its main closest-point criterion
and Theorem 2 retain their correct scope.

For weights chi_f(s_u,k)=-k f(u), the spectral norm is
k||f||_Euclidean/sqrt(N). The resulting quotient conversion retains
sqrt(N)/k and the sign opposite to jumping numbers. For rho in Sigma(A),
the gap delta=||rho||^2-H_A(rho) is nonnegative and controls
||rho-p_A|| by sqrt(2 delta); zero gap characterizes the minimizer.
A regular lower triangulation gives the linear oracle. Floating-point
optimization is distinguished from an exact rational certificate, which
requires rational input and verified polytope membership. These are
known source arguments and their immediate finite consequences.

Equations (68.23cs)--(68.23cv) record the support identity, projection,
membership criteria and gap. The preceding Yao subsection and following
quantized-limit subsection remain intact. A finite certificate supplies
neither closed-polytope precompactness nor a continuum limit. No general
lattice convergence, piecewise-affinity, rational realization, long-time
Calabi-flow existence or general Siu/closure repair is admitted.

## Primary reading reused

The preceding [source review](toric_secondary_polytopes_source_review_20261006.md)
read and displayed all 49 actual pages of the v1 PDF, including proofs,
appendices and references. Its metadata's 46-page comment does not
describe the actual file. The PDF SHA-256 is
`63215db3cddf557280dad21555cba0b1eb191130ed618b24c24cd8bd409b1a69`;
the full-reading record SHA-256 is
`5e9e3517b0a1114f32a72da018a56ce033835690e6205e75ac7c92845c21f22e`.
The preceding nineteen-page selected dependency record, Székelyhidi
0709.2687v1 and Tate 0908.3073v5, has SHA-256
`2f420581931249e293759b0253b64861eeb6b3a6c18d0410a60dfff9fc0842b4`.
These records and the previously checked Yao input are reused. No fresh
primary pages or new complete dependency-paper reading is claimed.
The exact v1 bibliography entry is added separately from older sources.

The source review's two other diagnostics, a missing sufficiently-large-
level qualifier and an omitted asymptotic remainder, remain source
diagnostics rather than counterexamples to the correctly scoped main
theorem. The external continuum compactness and regularity chain is
not cleared by this finite integration.

## Final validation and PDF review

The final book has **4,388 pages**, 20,391,949 bytes and SHA-256
`0aed46c82e8c59dcd218356d1f8253b513995e74e730728f76ae06e63a6b61e4`.
There are zero TeX errors, package/pdfTeX warnings, missing characters,
overfull boxes, unresolved references/citations or rerun requests.
The 954 nonfatal underfull diagnostics match the baseline.

The post-render reference check finds 425 active inputs and 12,838 unique
labels, with no missing inputs, duplicate labels or dangling references.
There are 372 used bibliography keys among 667 available keys, with
zero bibliography warnings. Six new labels, four new explicit equation
tags and one version-specific bibliography key are added. All 132
Chapter 68 equation numbers are unique. No index entry is added.
All 764 index entries are accepted, zero rejected, with 1,012 index
lines, 763 page groups and 419 valid numeric destinations.

PDF navigation has 21,933 named destinations, 47,016 internal links,
171 external URL links, 2,560 contents entries and six parts, with zero
invalid links, destinations or contents pages. All **37 matching final
PDF pages** were displayed and their full extracted text read in nineteen
sheets: actual 60, 68, 3585--3588, 4151--4153 and 4361--4388. They cover
affected contents, the whole addition and its transitions, provenance
and the following appendix, the complete index and bibliography.
The final review manifest SHA-256 is
`622fe0f8e24ce93be2c88a2e8f7f74bacf7ba99b977b8a4c94b1f1721f621f31`.
This scoped release review is not a fresh rereading of all 4,388 pages.

Historical draft diagnostics remain immutable. The first draft repeated
printed equation numbers; the second repaired printed numbers but still
repeated equation PDF anchors. Explicit tagged display math, following
the repository convention, repairs both in the final build. Final
numbering, navigation and page review use only the corrected PDF.

## Preservation and publication

Only Chapter 68 and Appendix L change among active inputs. All 423 other
active inputs and 108 protected inputs retain their baseline bytes. The
edited files preserve all 34 existing statement/explanatory environments
and twelve proof environments, 46 blocks in total. No formal result
environment is added or relabeled. The other bibliography remains intact.
README and the research programme record the completed integration.

All 57 prior frozen manifests, 52 integrations and five source-only
reviews, and all 112 prior exports retain their bytes. The other 5,029
tracked baseline files are unchanged. The inventory passes with 42 atoms,
twelve families and tier counts 0/3/7/15/17; every complete canonical
status, the open toric candidate and native catalogue source/PDF retains
its bytes. The native editor stays open without compilation or tab change.

The release contains the full PDF, a 37-page review PDF and a source
archive with 641 members. Every member is verified against its saved
source bytes, the CRC is checked, and all 425 active inputs are included.
No fresh isolated archive compilation is claimed. The closure, manifest
and artifact record pin this edition. GitHub synchronization explicitly
fetches main and work and uses the existing work branch and draft PR.

No original result, independent production model call, verification
receipt, canonical solved status or general proof repair is claimed.
Continue with the newly acquired Hermitian bounded-to-smooth paper and
its exact regularity and sign hypotheses before further admission.
