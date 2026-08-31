# Primary-source ledger

Read-only diagnosis, 1 September 2026. Printed page numbers are used.
This is an interface check, not a fresh audit of every proof in every paper.
No secondary source is relied upon. Current indexing conventions vary:
the report consistently uses bidegree (0,0) for function-like currents
acting on top-degree compact tests.

## CLD25: local exact primary bytes

Antoine Chambert-Loir and Antoine Ducros, *Formes différentielles réelles
et courants sur les espaces de Berkovich*, July 2025 revision.

- PDF: `/private/tmp/CLD25.pdf`, 4,659,053 bytes,
  SHA256 `5690f999523017d184ab751bb55857ab1637b197d1186ad4fd2edba7e1bda719`.
- Text: `/private/tmp/CLD25.txt`, 2,150,944 bytes,
  SHA256 `021be260392de1f3240858d4c775da86653518dfab4fd9c4c21a2406081b6c7e`.
- Test topology: §§3.7.5–3.7.7 p.93; §§6.4.1–6.4.6 pp.146–147.
- Currents and order: §§7.1.1–7.1.3 pp.155–156; Proposition 7.2.9 p.162.
- Measures from T wedged with tests, and bounded source multipliers:
  §7.2.11 and Example 7.2.12 p.163. A bidegree-(0,0) current itself is
  not being identified with a Radon measure on scalar tests.
- Stokes: Proposition 5.11.1; transpose/product calculus §§7.7.1–7.7.7,
  pp.186–188; full-support/injectivity interfaces §§7.3.10–7.3.13 p.168.
- Positive G-extension: Theorem 7.4.4, Proposition 7.4.5, Corollary 7.4.6,
  pp.170–172. Hypotheses: decent, locally differentially separated,
  affined G-tropical space. No closedness assertion for added primitives.
- Harmonic definition/scope: Definition 7.8.2 and Remark 7.8.3 p.190.
- Ordinary CPsh: Definition 8.1.7 pp.196–197; Proposition 8.3.1 p.201;
  Lemmas 8.5.1 and 8.5.5 pp.205–207. Section 8.3 onward assumes the
  level-n tropical space has no boundary. These are the source interfaces
  for the report's direct two-sided CPsh criterion.
- Bedford–Taylor independence: §8.6.1–Definition 8.6.2 pp.207–208;
  Proposition 8.11.1 and Corollary 8.11.2 pp.220–222. Source cautions
  about Corollaries 8.6.7 and 8.11.3 are explicitly recorded in the report.

The analytic setting in the task is boundaryless and is used with its
ordinary CLD calculus; abstract tropical hypotheses are not used to
manufacture new analytic charts. The PDF skill was used for source reading,
not to author a PDF. Selected full-page visual checks are in SOURCE_QA.json.

## Jell: ordinary Poincaré lemma

[A Poincaré lemma for real-valued differential forms on Berkovich spaces,
arXiv:1409.0676v3](https://arxiv.org/pdf/1409.0676v3), 29 July 2016.
Section 4 begins with K algebraically closed and complete and X reduced,
irreducible, separated, finite type. Theorem 4.5 and Corollary 4.6,
pp.18–20, give separate-differential local exactness and the constant-sheaf
resolution in one column. Remark 4.4, p.18, expressly rules out exactness
of the analogous total d-complex. This does not identify top compact
ordinary cohomology with the orientation line of a real 2n-manifold.
No descent of arbitrary currents from the algebraic closure is supplied.

## Jell: ordinary curve cohomology obstruction

[Tropical Hodge numbers of non-Archimedean curves,
arXiv:1706.05895v4](https://arxiv.org/pdf/1706.05895v4), 26 March 2018.
Standing field: algebraically closed, complete, nontrivially valued.
Theorems A/B pp.1–2; Definition 3.3 p.6; Corollaries 3.9/3.11 pp.7–8;
Lemma 4.1 and Theorems 4.2/4.4 pp.8–9. Proper smooth ordinary-form curve
duality has a reduction Pic^0-torsion condition. With residue field C,
positive-genus reduction can produce infinite-dimensional H^{1,1}.
This rules out an unqualified ordinary-top-cohomology-is-R assertion.
It is not itself an original-DVR counterexample, a continuous-dual
calculation, or a positive-current counterexample.

## Jell–Wanner: a genuine but restricted ordinary-open duality

[Poincaré duality for the tropical Dolbeault cohomology of non-archimedean
Mumford curves, arXiv:1612.01889v3](https://arxiv.org/pdf/1612.01889v3),
29 December 2017. K is algebraically closed and complete; the open-domain
result uses nontrivial valuation. Theorem 4.3 pp.17–18 proves ordinary
duality for open subsets of P1-an; Corollary 4.4 p.18 gives the
genus-zero-type-II/Mumford scope. Theorem 3.14 p.16 supplies its
compact-support refinement comparison. This is an actual ordinary-open
result but neither arbitrary higher-dimensional duality nor an
original-field arbitrary-current pullback theorem.

## Jell–Shaw–Smacka: tropical-manifold duality

[Superforms, tropical cohomology, and Poincaré duality,
arXiv:1512.07409v3](https://arxiv.org/pdf/1512.07409v3), header 27 March
2018, manuscript date 13 September 2018. Definition 4.15 p.25 requires
tropical-manifold local charts built from matroidal cycles (with the
specified weights). Theorem 4.33 pp.31–32 proves duality in that setting.
Example 4.13 pp.24–25 has a connected coordinate cross with
H^{0,0}=R but H_c^{1,1}=R². Thus connectedness/full rank alone is not
the tropical-manifold hypothesis. This cross is not asserted to be an
analytic ordinary-current counterexample upstairs.

## Gubler–Jell–Rabinoff: harmonic tropicalizations

[Forms on Berkovich spaces based on harmonic tropicalizations,
arXiv:2111.05741v3](https://arxiv.org/pdf/2111.05741v3), 7 March 2025.
The checked version is v3, not the initially attempted v2 download.
Standing analytic setting: good strict over a complete nontrivially valued
K; §12 uses Hausdorff, pure-dimensional, boundaryless spaces. Exact
locators: Remarks 10.10/10.11 p.64; §10.13, Proposition 10.14 and
Remark 10.15 pp.64–66; Example 11.8 p.70; §§12.1–12.5 pp.71–72;
Theorem 13.1 and Corollary 13.3 pp.73–74. The larger test sheaf,
induced ordinary subspace topology, and derivative distinction are used
only as described in the report. No automatic closed extension is stated
there. The elementary quotient/Hahn–Banach discussion in the report is
the researcher's deduction, not an attributed GJR theorem.

## Gubler–Jell–Rabinoff: weak-form curve duality

[Dolbeault cohomology of graphs and Berkovich curves,
arXiv:2111.05747v1](https://arxiv.org/pdf/2111.05747v1), 10 November 2021.
Section 6.4 p.50 specifies compact rig-smooth strict curves over a
complete nontrivially valued field. Theorem 6.4.1 pp.50–51 is a
form/skeleton description after finite Galois extension. For connected
proper curves, Theorem 6.4.3 p.53 identifies the weak top trace kernel
with d''-boundaries, and Theorem 6.4.5 pp.53–54 gives duality. The proof
descends forms/cohomology, not arbitrary ordinary currents. Properness,
dimension one, and the weak form sheaf must not be discarded.

## Gubler–Künnemann: delta forms/currents

[A tropical approach to non-Archimedean Arakelov geometry,
arXiv:1406.7637v3](https://arxiv.org/pdf/1406.7637v3), 13 September 2016.
The exact title is “geometry”; no v4 was read. Standing K is algebraically
closed, complete, nontrivially valued (pp.4,8). Section 6,
Definitions 6.3/6.4 pp.49–50, uses compact delta-form tests and their
topology for delta-currents. Theorem 0.2 and the cycle/metric constructions
do not classify arbitrary ordinary CLD currents. The introductory
base-change observation about that paper's applications is not authority
to pull back an arbitrary current in the present task.

## Jell: compact-support tropicalization colimit

[Tropical cohomology with integral coefficients for analytic spaces,
arXiv:1909.12633v2](https://arxiv.org/pdf/1909.12633v2), 28 June 2020.
K is complete non-Archimedean; Definition 4.11 p.12 gives condition (†):
normality and a common affine neighbourhood for any two scheme points.
Theorem 5.7 pp.14–15 assumes a fine enough global family and an ordinary
open admitting its tropical chart; Theorem 5.9 p.15 assumes an admissible
global family. These are compact-test/cohomology colimit statements, not
trace-kernel or continuous-dual identifications. The introductory global
embedding scope is expressly stated, and a general ordinary W is not
silently treated as a single proper tropical chart.

## Access and non-use boundaries

Web-reader extraction supplied the remote primary statements and relevant
proof interfaces. Shell downloads failed with DNS resolution errors; no
remote PDF file or SHA is represented as obtained. Remote screenshot
attempts on the Jell curve PDF failed with cache misses. Accordingly this
packet claims no remote PDF visual verification. The source-version pins
are URLs plus displayed arXiv headers, not byte hashes.

Searches were bounded to these primary interfaces and related exact-title
queries. No universal absence-of-literature claim, novelty claim, or
candidate mathematical verdict follows. Existing geometric source-cell,
nearby-wall, residual-functional, and common-moment research is not used
as a theorem input to this source diagnosis.
