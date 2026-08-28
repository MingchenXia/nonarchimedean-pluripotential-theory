# Annotated primary-literature map

## Non-Archimedean pluripotential theory monograph

**Literature cut-off:** 15 August 2026  
**Policy:** primary papers, books, official journal pages, and author/arXiv
versions are used for mathematical claims. Surveys are used only as reading
guides. Version-sensitive statements are dated.

This map records what each source contributes, its main hypotheses, where it
enters the planned book, and any status warning. It is not a substitute for
the final theorem-provenance table, which will cite exact theorem numbers and
pages after the source freeze.

---

## 1. The four frameworks must remain distinct

### 1.1 BFJ global theory

Over a complete nontrivially valued field, the foundational BFJ construction
defines singular semipositive metrics through algebraic/formal models, SNC
dual complexes, nefness, and monotone approximation. Its Monge--Ampère theory
is global and variational.

### 1.2 BJ trivially valued theory

Over a trivially valued field, BJ use semivaluations, Fubini--Study functions,
homogeneity, filtrations, finite-energy potentials and measures, and strong
topologies. This is not obtained by simply setting the valuation parameter to
zero in every BFJ proof.

### 1.3 CLD local differential theory

CLD define \((p,q)\)-forms, currents, positivity, integration, and local
Bedford--Taylor products through Lagerberg superforms and tropicalizations of
Berkovich spaces. Their approximation-defined local notion of psh is not
silently interchangeable with BFJ/BJ global semipositivity.

### 1.4 Complex/transcendental theory

DXZ/Xia construct non-Archimedean metrics from relative test curves and
geodesic rays, while Mesquita-Piccione constructs an intrinsic tropical
semivaluation space \(X^\beth\) for compact complex spaces. Agreement holds in
specified projective/Kähler/finite-energy regimes and must be proved there.

---

## 2. Foundational analytic and model geometry

### Berkovich

Vladimir Berkovich, *Spectral Theory and Analytic Geometry over
Non-Archimedean Fields*, Mathematical Surveys and Monographs 33, AMS, 1990.

**Contribution.** Banach spectra, affinoid analytic spaces, gluing,
analytification, completed residue fields, compactness and properness.

**Book use.** Chapters 2--5. The graduate exposition will develop only the
portion needed for pluripotential theory, with curves and Gauss points as
continuous examples.

### Zhang semipositive metrics

Shou-Wu Zhang, “Positive line bundles on arithmetic varieties,” *J. Amer.
Math. Soc.* 8 (1995), 187--221.
[DOI](https://doi.org/10.1090/S0894-0347-1995-1254133-6).

**Contribution.** Nef/model and admissible metrics in arithmetic geometry.

**Book use.** Historical and mathematical precursor for model semipositivity
in Chapter 6.

### Gubler--Martin

Walter Gubler and Florent Martin, “On Zhang's semipositive metrics,”
*Documenta Mathematica* 24 (2019), 331--372.
[arXiv](https://arxiv.org/abs/1608.08030).

**Contribution.** Comparison among algebraic, formal, and PL metrics; density
and stability under limits.

**Book use.** Chapter 6 and the normalization of “model,” “formal,” and “PL,”
terms that are often used too loosely.

### Chambert-Loir measures

Antoine Chambert-Loir, “Mesures et équidistribution sur les espaces de
Berkovich,” *J. Reine Angew. Math.* 595 (2006), 215--235.
[arXiv](https://arxiv.org/abs/math/0304023),
[DOI](https://doi.org/10.1515/CRELLE.2006.049).

**Contribution.** Atomic measures attached to semipositive model metrics,
computed from residual intersection numbers.

**Book use.** Chapter 6 introduces the measure before either CLD or BFJ; later
chapters prove that their constructions recover it.

---

## 3. Chambert--Loir--Ducros and local differential theory

### CLD, current version

Antoine Chambert-Loir and Antoine Ducros, “Formes différentielles réelles et
courants sur les espaces de Berkovich,” 608 pp., version 2, 25 July 2025.
[arXiv](https://arxiv.org/abs/1204.6277).

**Contribution.** Lagerberg superforms; positive forms and supercurrents;
polyhedral, parlinear, and tropical spaces; calibrations and integration;
Stokes and Green formulae; tropical intersection; graded reduction; analytic
skeleta and tropicalizations; real differential forms and currents on
Berkovich spaces; Poincaré--Lelong, Bochner--Martinelli, and Levine formulae;
psh functions and Bedford--Taylor products; metrized vector bundles, Chern
currents, formal metrics, relative Monge--Ampère operators; canonical metrics
on abelian varieties.

**Exact anchors to audit.**

- Stokes/Green: Proposition 5.11.1, around PDF p. 140.
- Poincaré--Lelong: Theorem 16.7.3, around PDF p. 460,
  \[
    \delta_{\operatorname{div}(f)}=d'd''[\log|f|].
  \]
- Formal/model Monge--Ampère: Theorem 18.5.5, around PDF pp. 528--529.
- Agreement with the 2006 Chambert--Loir measure: Proposition 18.5.8, around
  PDF p. 531.
- Transfinite psh hierarchy: Definition 8.1.1, Lemma 8.1.4, and Remark
  8.1.6.  Lemma 8.1.4 proves eventual cardinal stabilization; the meaningful
  unresolved issue suggested by Remark 8.1.6 is collapse at stage one, or at
  another controlled early ordinal, rather than eventual stationarity.
- Local versus global psh metrics: Definition 17.8.5, Corollary 17.8.9, and
  Remark 17.8.10.  The remark asks separately whether every continuous
  locally psh metric on a projective variety is globally psh in the uniform
  smooth-approximation sense, and whether the parlinear-dpsh conclusion of
  Corollary 17.8.9 extends to proper strict analytic spaces with a formal
  model having projective special fibre.

**Book use.** Part II supplies the mathematical core but not the source's
expository order. The material is rebuilt concrete-to-invariant and
local-to-global; maximal tropical-space abstraction is moved to appendices
when it is not needed in the proof path.

**Status warning.** The current source is the vastly expanded 2025 revision,
not merely the 2012 draft commonly cited in older bibliographies.  The
literal sentence in Remark 8.1.6 saying stationarity is unknown conflicts
with Lemma 8.1.4; the book records the source wording and asks only the
coherent early-collapse question.

### Mikhalkin--Rau: tropical convention authority

Grigory Mikhalkin and Johannes Rau, *Tropical Geometry*, book manuscript,
version of 16 November 2018.
[PDF](https://www.math.uni-tuebingen.de/user/jora/downloads/main.pdf).

**Contribution.** Max-plus tropical arithmetic; tropical vector spaces and
integer-affine maps; rational polyhedra (where rationality concerns the
linear parts, not the real constants); facets as top-dimensional cells;
weighted refinements and tropical cycles as equivalence classes; tropical
subspaces as positive cycles; stars, stable intersection, divisors of
piecewise integer-affine functions, pushforward, projection formula, tropical
spaces, and tropical curves.

**Book use.** Chapters 10--12 and Appendix G use this source as their
terminology and convention authority. CLD's phrase “integral affine” is
recorded as a synonym for “integer affine.” The analytic valuation coordinates
\(u=-\log|\cdot|\) are the negatives of the max-plus coordinates used in this
reference; every tropical-to-analytic interface displays this max/min sign
translation explicitly.

**Exact anchors.** Sections 1.2--1.3 (max-plus and integer-affine
conventions), 2.1 (rational polyhedra and facets), 4.2 (cycles and weighted
refinements), 4.3 (stable intersection), 4.4 (piecewise integer-affine
functions and divisors), 4.6 and 6.2 (projection and pushforward), and 7.1--7.3
(abstract tropical spaces and morphisms).

### Berndtsson: supercurrents and Riemannian submanifolds

Bo Berndtsson, “Superforms, supercurrents, minimal manifolds and Riemannian
geometry,” *Arnold Mathematical Journal* 5 (2019), 501--532.
[arXiv v2](https://arxiv.org/abs/1805.00379),
[DOI](https://doi.org/10.1007/s40598-019-00130-x).

**Contribution.** A Euclidean scalar product attaches a positive symmetric
supercurrent \([M]_{\mathrm s}\) to a smooth real submanifold. Its derivative
records the second fundamental form, and
\([M]_{\mathrm s}\wedge\beta^{m-1}\) is closed exactly when \(M\) is minimal.
This metric-dependent construction is distinct from lattice-calibrated,
balanced tropical integration.

**Book use.** Chapter 14, routed back to the superform algebra of Chapter 9;
only the minimal/mean-curvature interpretation is used, not a development of
mean-curvature flow.

**Version warning.** Use arXiv v2 (13 June 2019) or the journal version. The
arXiv record states that an incorrect proof in v1, Section 8, was replaced;
the main results were unchanged.

### Berndtsson: supercurrents and convex geometry

Bo Berndtsson, “Superforms, supercurrents and convex geometry,”
arXiv:2501.02896v3, 6 August 2026.
[arXiv v3](https://arxiv.org/abs/2501.02896).

**Contribution.** Convex Bedford--Taylor products and Alexandrov
Monge--Ampère measure; the weakly-null obstruction and the additional
“strong” hypothesis; strongly homogeneous currents built from support
functions; mixed volumes and supercurrent proofs of Alexandrov--Fenchel.

**Book use.** Chapter 14 for positivity and convention warnings, Chapter 16
for the real Bedford--Taylor bridge, Chapter 8 for the toric dictionary, and
the convexity appendix for support functions and mixed volumes.

**Convention warning.** Version 3, Section 2 uses
\(J(dx_i)=-d\xi_i\), \(J(d\xi_i)=dx_i\), \(d^\#=J^{-1}dJ\), and a specified
Berezin sign. These differ from the Lagerberg--CLD conventions of this book
and even from Berndtsson's 2019 paper. Translate Hessians, \(J\), bidegrees,
and integration normalizations explicitly; do not copy formulas verbatim.

### Delta-forms and tropical Arakelov geometry

Walter Gubler and Klaus Künnemann, “A tropical approach to nonarchimedean
Arakelov geometry,” *Algebra & Number Theory* 11 (2017), 77--180.
[DOI](https://doi.org/10.2140/ant.2017.11.77).

**Contribution.** Delta-forms and delta-currents, tropical intersections,
generalized Poincaré--Lelong, Green currents and local heights. Formal metric
wedge products recover Chambert-Loir measures.

**Book use.** Chapter 18, after the reader understands ordinary CLD forms and
why their smooth category does not contain every piecewise-linear curvature
object.

### Positivity and delta-forms

Walter Gubler and Klaus Künnemann, “Positivity properties of metrics and
delta-forms,” *J. Reine Angew. Math.* 752 (2019), 141--177.
[arXiv](https://arxiv.org/abs/1509.09079),
[DOI](https://doi.org/10.1515/crelle-2016-0060).

**Contribution.** Comparison of positive delta-currents, psh metrics, and
Zhang semipositivity for formal metrics.

**Book use.** Chapters 17--19 and the model-core comparison of Chapter 63.

### Poincaré lemma

Philipp Jell, “A Poincaré lemma for real-valued differential forms on
Berkovich spaces,” *Math. Z.* 282 (2016), 1149--1167.
[arXiv](https://arxiv.org/abs/1409.0676),
[DOI](https://doi.org/10.1007/s00209-015-1583-8).

**Contribution.** Cohomological foundations for real differential forms.

**Book use.** Chapter 13 and the later discussion of cohomological limitations.

### Curves: CLD and Thuillier

Veronika Wanner, “Comparison of two notions of subharmonicity on
non-archimedean curves,” *Math. Z.* 293 (2019), 443--474.
[arXiv](https://arxiv.org/abs/1801.04713),
[DOI](https://doi.org/10.1007/s00209-018-2205-z).

**Contribution.** For continuous functions on smooth proper curves, CLD psh
equals Thuillier subharmonicity; includes regularization results in important
curve cases.

**Book use.** Chapters 8, 19, and the dimension-one base case of the local/global
comparison.

### Real versus non-Archimedean Monge--Ampère

Christian Vilsmeier, “A comparison of the real and non-archimedean
Monge--Ampère operator,” *Math. Z.* 297 (2021), 633--668.
[arXiv](https://arxiv.org/abs/1912.06220),
[DOI](https://doi.org/10.1007/s00209-020-02527-3).

**Contribution.** On a skeleton face, the non-Archimedean measure of a convex
metric is a normalized Alexandrov real Monge--Ampère measure.

**Book use.** Toric/skeletal examples and Chapter 64.

### Tropical toric pluripotential theory

José Ignacio Burgos Gil, Walter Gubler, Philipp Jell, and Klaus Künnemann,
“Pluripotential theory for tropical toric varieties and non-Archimedean
Monge--Ampère equations,” *Kyoto J. Math.* 65 (2025), 55--152.
[arXiv](https://arxiv.org/abs/2102.07392),
[DOI](https://doi.org/10.1215/21562261-2024-0010).

**Contribution.** Invariant complex/tropical/non-Archimedean comparison and
invariant Monge--Ampère equations on toric and abelian varieties over arbitrary
fields.

**Book use.** Chapters 8, 19, 31, and the concrete test suite for every
normalization in Part VI.

### Harmonic tropicalizations

Walter Gubler, Philipp Jell, and Joseph Rabinoff, “Forms on Berkovich spaces
based on harmonic tropicalizations,” *Bull. Soc. Math. France* 154 (2026),
135--238.
[arXiv](https://arxiv.org/abs/2111.05741),
[DOI](https://doi.org/10.24033/bsmf.2919).

**Contribution.** Enlarged sheaves of forms based on harmonic
tropicalizations, with improved cohomological behaviour.

**Book use.** Chapter 18. The construction is presented after the defect in
the original sheaf has been made concrete.

**Exact open-question anchors.**  The source leaves three distinct questions:

1. immediately before Proposition 7.5, whether the local finite integral
   decomposition of harmonic functions has a semipositive analogue;
2. in Section 1.15, whether the canonical injection
   \(\Lambda^{p,q}M_{\mathbf R}\to H^{p,q}(A)\) for an abelian variety is an
   isomorphism;
3. in Remark 16.4, whether a canonical metric on a line bundle on an abelian
   variety is an ordinary \(\delta\)-metric.

Section 17 constructs a mixed-reduction abelian threefold whose canonical
tropicalization is not smooth, invalidating the smoothness premise of the
older proposed proof of the third item.  It is a boundary example, not a
negative answer to either abelian-variety question.

### Monge--Ampère measures on balanced polyhedral spaces

Ana María Botero, Enrica Mazzon, and Léonard Pille--Schneider,
“Monge--Ampère measures on balanced polyhedral spaces,”
arXiv:2603.08664v1, submitted 9 March 2026 and manuscript dated 10 March
2026. [arXiv](https://arxiv.org/abs/2603.08664).

**Contribution.** Polyhedral psh functions, compactness, energy, capacity,
Monge--Ampère measures and equations on balanced polyhedral spaces;
regularity and orthogonality in specified smooth or one-dimensional cases;
counterexamples; and a comparison for the stated toric Calabi--Yau
complete-intersection degenerations.

**Exact open questions.** The paper asks for higher-dimensional notions of
polyhedral smoothness that ensure regularity and orthogonality, for a
characterization of the polarized Calabi--Yau degenerations whose
tropicalizations enjoy those properties, and, in Remark 6.27, for a
classification of the matroids whose Bergman fans satisfy orthogonality.

**Book use and attribution boundary.** Chapter 72 records these three source
questions.  Its intrinsic singular-fan contact problem and recursive
calibrated CLD/non-Archimedean comparison problem are stronger
book-formulated targets, not questions attributed verbatim to this paper.
The verified complete-affine calculation and the four-ray-cross boundary do
not settle the source's higher-dimensional singular questions.

### New local psh framework

Walter Gubler and Joseph Rabinoff, “On semipositive piecewise linear functions
in non-archimedean analytic geometry.”
[arXiv](https://arxiv.org/abs/2503.05513).

Walter Gubler and Joseph Rabinoff, “Classically psh and pluriharmonic functions
on Berkovich spaces.”
[arXiv](https://arxiv.org/abs/2506.13548).

**Contribution.** A curve-test local notion, maximum principles, and comparison
with semipositive PL functions.

**Book use.** Chapters 15, 18--19, and the CLD/BFJ bridge. These papers help
produce a clearer modern treatment than following the CLD manuscript
strictly, but their notion is carefully distinguished from CLD's
approximation-defined psh class.

---

## 4. BFJ global theory over a nontrivially valued field

### Singular semipositive metrics

Sébastien Boucksom, Charles Favre, and Mattias Jonsson, “Singular semipositive
metrics in non-Archimedean geometry,” *J. Algebraic Geom.* 25 (2016), 77--139.
[arXiv](https://arxiv.org/abs/1201.0187),
[DOI](https://doi.org/10.1090/jag/656).

**Foundational scope.** Smooth projective \(X\) over a complete discretely
valued field, residue characteristic zero, with an ample line bundle.

**Contribution.** Model functions and closed \((1,1)\)-forms; positivity on
models; SNC dual complexes and retractions; singular psh metrics; compactness
modulo constants; equicontinuity on skeleta; envelopes; decreasing
regularization by semipositive model functions.

**Book use.** Chapters 20--23. Later extensions are never folded backward into
the statement of the original theorem.

### The BFJ Monge--Ampère equation

Sébastien Boucksom, Charles Favre, and Mattias Jonsson, “Solution to a
non-Archimedean Monge--Ampère equation,” *J. Amer. Math. Soc.* 28 (2015),
617--667.
[arXiv](https://arxiv.org/abs/1201.0188),
[DOI](https://doi.org/10.1090/S0894-0347-2014-00806-7).

**Foundational scope.** Smooth projective spaces in the discretely valued,
residue-characteristic-zero framework, with algebraizability over a function
field and a technical support hypothesis for the prescribed measure.

**Contribution.** Mixed Monge--Ampère measures; capacity and quasicontinuity;
locality and comparison; energy and \(\mathcal E^1\); envelope
differentiability and orthogonality; variational existence; continuity for
measures supported on a dual complex.

**Book use.** Chapters 24--29.

### BFJ expository bridge

Boucksom--Favre--Jonsson, “The Non-Archimedean Monge--Ampère Equation,” in
*Nonarchimedean and Tropical Geometry*, Simons Symposia, Springer, 2016,
31--49. [arXiv](https://arxiv.org/abs/1502.05724),
[DOI](https://doi.org/10.1007/978-3-319-30945-3_2).

**Book use.** Reading guide only; proofs are sourced to the primary papers.

### Local valuative pluripotential theory

Sébastien Boucksom, Charles Favre, and Mattias Jonsson, “Valuations and
plurisubharmonic singularities,” *Publ. Res. Inst. Math. Sci.* 44 (2008),
449--494. [DOI](https://doi.org/10.2977/prims/1210167334).

**Contribution.** The normalized valuation link of a smooth complex germ;
exceptional Cartier and Weil b-divisors; primary-ideal functions; formal psh
functions and multiplier-ideal approximation; nef envelopes; local mixed
Monge--Ampère measures; valuative transforms of complex psh germs; relative
types and generalized Lelong numbers.

**Exact unresolved point.** The paper proves that equality of infinitely-near
Lelong numbers, strong multiplier ideals, and relative types are equivalent
and imply equality of generalized Lelong numbers against tame weights.  The
converse implication from all such generalized Lelong numbers is left open.

**Book use.** Chapter 70.  This local theory is not the nontrivially valued
global BFJ theory: its carrier is the centered link
\(v(\mathfrak m)=1\), and its mixed measure has one fewer psh input than the
dimension of the smooth germ.

### Removing algebraizability

José Ignacio Burgos Gil, Walter Gubler, Philipp Jell, Klaus Künnemann, and
Florent Martin, “Differentiability of non-archimedean volumes and
non-archimedean Monge--Ampère equations,” *Algebraic Geometry* 7 (2020),
113--152. [arXiv](https://arxiv.org/abs/1608.01919),
[DOI](https://doi.org/10.14231/AG-2020-005).

**Contribution.** Differentiability and orthogonality remove the BFJ
algebraizability hypothesis in residue characteristic zero.

**Book use.** Chapters 27--29, explicitly as a later extension.

### Envelope continuity and test ideals

Walter Gubler, Philipp Jell, Klaus Künnemann, and Florent Martin,
“Continuity of plurisubharmonic envelopes in non-Archimedean geometry and test
ideals,” *Ann. Inst. Fourier* 69 (2019), 2331--2376.
[arXiv](https://arxiv.org/abs/1712.00980),
[DOI](https://doi.org/10.5802/aif.3296).

**Contribution.** Envelope continuity in residue characteristic zero and for
geometrically defined surfaces in positive characteristic.

**Book use.** Chapter 23 and the test-ideal preparation for Chapter 40.

### Mixed characteristic

Yanbo Fang, Walter Gubler, and Klaus Künnemann, “On the non-Archimedean
Monge--Ampère equation in mixed characteristic,” *Nagoya Math. J.* 259 (2025),
548--561. [arXiv](https://arxiv.org/abs/2203.12282),
[DOI](https://doi.org/10.1017/nmj.2025.8).

**Contribution.** Mixed-characteristic solutions conditional on resolution
and embedded resolution.

**Book use.** Chapter 29 hypothesis atlas.

### Relative and non-Archimedean volumes

Boucksom--Gubler--Martin, “Differentiability of relative volumes over an
arbitrary non-Archimedean field,” *Int. Math. Res. Not.* (2022), 6214--6242.
[arXiv](https://arxiv.org/abs/2004.03847),
[DOI](https://doi.org/10.1093/imrn/rnaa314).

Boucksom--Gubler--Martin, “Non-Archimedean volumes of metrized nef line
bundles,” *Épijournal de Géométrie Algébrique* 5 (2021).
[arXiv](https://arxiv.org/abs/2011.06986),
[DOI](https://doi.org/10.46298/epiga.2021.6908).

**Contribution.** Relative volume, energy, differentiability, and
orthogonality over increasingly general fields.

**Book use.** Chapters 27, 30, and the hypothesis history.

### Local volume of isolated singularities

Yuchen Zhang, “On the volume of isolated singularities,” *Compositio
Mathematica* 150 (2014), 1413--1424.
[arXiv](https://arxiv.org/abs/1301.6121),
[DOI](https://doi.org/10.1112/S0010437X13007847).

**Contribution and resolved status.** For the Boucksom--de Fernex--Favre
local volume, Zhang proves a positive lower bound depending only on the
dimension for every nonzero volume of an isolated Gorenstein singularity.
He also constructs a non-\(\mathbf Q\)-Gorenstein isolated singularity of
volume zero admitting no boundary that makes the pair log canonical.  Thus
the proposed lower-bound direction is true, while the proposed implication
from volume zero to the existence of a log-canonical \(\mathbf Q\)-boundary
is false.

**Book use.** Chapter 72 records both answers as resolved history delimiting
the singular local programme; neither is listed as an open problem.  The PDF
was not present in the local Rethlas reference pack during the 15 August
audit; no newly prepared packet asks Rethlas to prove this resolved result.

### Norms, envelopes, and CLD regularizability

Sébastien Boucksom and Dennis Eriksson, “Spaces of norms, determinant of
cohomology and Fekete points in non-Archimedean geometry,” *Adv. Math.* 378
(2021), 107501. [arXiv](https://arxiv.org/abs/1805.01016),
[DOI](https://doi.org/10.1016/j.aim.2020.107501).

**Contribution.** Norms and Fubini--Study metrics over arbitrary complete
valued fields; relative volume equals energy; envelopes and Fekete points.
Theorem 7.8 identifies continuous psh metrics on ample line bundles with
Zhang-nef metrics; Theorem 7.14 gives CLD-psh regularizability on semiample
bundles; Theorem 8.4 treats the CLD Bedford--Taylor mixed measure.

**Book use.** Chapters 6, 18--19, 23, 30, 33, and the local/global comparison.

### Global pluripotential theory on hybrid spaces

Léonard Pille--Schneider, “Global pluripotential theory on hybrid spaces,”
*J. Éc. polytech. Math.* 10 (2023), 601--658.
[arXiv](https://arxiv.org/abs/2209.04879).

**Contribution.** Global psh metrics over integral Banach rings; canonical
psh extension to hybrid spaces; continuity of hybrid Monge--Ampère measures;
and continuity for canonically polarized degenerations.

**Exact open-question anchors.** Remark 4.4 observes that
\(\mathcal E^1(X,L)\) is defined over an arbitrary complete
non-Archimedean field but that the Monge--Ampère operator on this class is
not known in that generality; it names the discretely valued
characteristic-zero BFJ theory and the trivially valued BJ theory as the
known endpoints.  This is distinct from Question 4.9, which asks for
continuity of fibrewise Monge--Ampère integrals over a general integral
Banach base.  Question 3.18 reproduces Favre's continuity question for the
hybrid extension.  Theorem 4.11 treats the hybrid Monge--Ampère continuity
case, and Theorem 5.1 treats canonically polarized degenerations.

**Book use.** The arbitrary-field operator, Banach-family continuity, and
hybrid-extension continuity are stated as three separate interfaces in the
research corpus; solvability of a Monge--Ampère equation is not conflated
with construction of the operator.

---

## 5. BJ global theory over a trivially valued field

### Global pluripotential theory

Sébastien Boucksom and Mattias Jonsson, “Global pluripotential theory over a
trivially valued field,” *Ann. Fac. Sci. Toulouse* 31 (2022), 647--836.
[arXiv](https://arxiv.org/abs/1801.08229),
[DOI](https://doi.org/10.5802/afst.1705).

**Contribution.** Trivially valued analytification and test configurations;
PL/Fubini--Study functions; psh metrics; energy; envelopes; homogeneity and
b-divisors; finite-energy functions and mixed Monge--Ampère measures;
differentiability; finite-energy measures; strong topologies; valuations of
linear growth; capacity and pluripolar sets; dual complexes and toric theory.

**Book use.** Chapters 32--36 and 46--50.

**Envelope chronology.** Conjecture 5.14 asks for the envelope property on a
unibranch projective variety for every numerical class. Theorem 5.20 supplies
an earlier smooth case under restricted characteristic/dimension and
positivity assumptions.

### Polarized affine cones: model energy

Yueqiao Wu, “Volume and Monge--Ampère energy on polarized affine varieties,”
*Math. Z.* 301 (2022), 781--809.
[arXiv](https://arxiv.org/abs/2106.13395),
[DOI](https://doi.org/10.1007/s00209-021-02935-z).

**Contribution.** Homogeneous finite-type filtrations and their
Fubini--Study functions on the trivially valued analytification of a normal
affine cone with Reeb polarization; the CLD shell product
\[
 (d'd''\varphi_1)\wedge\cdots\wedge(d'd''\varphi_{n-1})
 \wedge d'd''\max\{\varphi_\xi,0\};
\]
support on the analytic link; equality of Monge--Ampère energy with
filtration volume; approximation of irrational Reeb fields by rational ones;
and comparison with global projective Fubini--Study metrics in the
quasi-regular case.

**Exact anchors.** Corollary 5.7 proves finite support on the shell.
Proposition 5.13 gives the unnormalized quasi-regular identity between the
projective CLD/Chambert--Loir product and the shell product; after division by
the common volume it identifies the corresponding probability measures.
Corollary 5.14 compares Fubini--Study energies, and Theorem 5.15 identifies
model energy with filtration volume.

**Book use.** Chapters 63 and 70.  Both the radial reference factor and the
normalizing factor (1/\operatorname{vol}(\xi)) are retained explicitly;
without them the displayed current is not the probability measure on the
link.

### Polarized affine cones: finite energy

Yueqiao Wu, “Some non-Archimedean pluripotential theory on polarized affine
cones,” arXiv:2406.13684v1, 19 June 2024.
[arXiv](https://arxiv.org/abs/2406.13684).

**Contribution.** The compact analytic link
\(X_0=\{v:v(\mathfrak m)=0\}\); continuous psh functions as local-uniform
limits of homogeneous Fubini--Study functions; general psh functions as
decreasing-net limits; density of differences of continuous psh functions;
CLD integration by parts and a local Hodge-index inequality; Monge--Ampère
energy; the finite-energy classes \(\mathcal E^1(\xi)\) and
\(\mathcal M^1(\xi)\); mixed Monge--Ampère products; and the dual
quasi-pseudometrics \(I\) and \(I^\vee\).

**Exact anchors.** Definition 2.6 is the link, Definition 2.9 the
Fubini--Study class, Definition 3.1 the continuous psh class, Theorem 3.5 the
density statement, Definition 5.1 the decreasing-net psh class, Definition
5.9 and Proposition 5.10 the extended energy, Theorem 6.3 the mixed
finite-energy product, and Corollary 7.8 the bi-Lipschitz comparison of
Monge--Ampère measures onto the operator's image.  Corollary 6.6(4) records
recovery of the global BJ finite-energy class and energy for rational Reeb
fields; it is not cited as an identification of the whole BJ theory.

**Exact open questions.** The introduction identifies the missing uniform
differentiability input needed to characterize the image of the
Monge--Ampère operator and to solve the local non-Archimedean Monge--Ampère
equation in full generality.  It reduces the difficulty to comparing
\(\operatorname{PSH}(\xi)\) and \(\operatorname{PSH}(\xi')\) for
nonproportional Reeb fields.  For irrational polarization, a divisorial norm
may map to a genuinely quasimonomial measure.

**Normalization warning.** Wu's analytic link
\(v(\mathfrak m)=0\) normalizes Reeb translation.  The BFJ local link
\(v(\mathfrak m)=1\) normalizes positive scaling of centered valuations.
They are different carriers; the book never identifies them without an
additional comparison construction.

**Book use.** Chapter 70 gives the graduate exposition and the CLD/BJ
interfaces.  Chapter 63 records the precise solid arrows and the missing
BFJ comparison arrow.  The source's two explicit questions remain in the
research boundary rather than being reported as solved.

### BJ addendum

Boucksom--Jonsson, “Addendum to the article ‘Global pluripotential theory over
a trivially valued field’,” *Ann. Fac. Sci. Toulouse* 33 (2024), 405--417.
[arXiv](https://arxiv.org/abs/2206.07183),
[DOI](https://doi.org/10.5802/afst.1775).

**Contribution.** All numerical classes for smooth \(X\) in characteristic
zero or dimension at most two; an ample-class energy identity for singular
\(X\).

**Book use.** Chapter 36, as the last public stage before the supplied full
proof.

### Supplied envelope manuscript

*The Envelope Property for Unibranch Projective Varieties*, user-supplied TeX
archive; author and date fields currently blank.

**Claimed contribution.** Full BJ Conjecture 5.14: every integral projective
unibranch variety, arbitrary characteristic and dimension, all real numerical
classes, arbitrary nonempty bounded-above families.

**Proof mechanisms.** Homogeneous Cartier b-divisors; carrier and birational
reflection; asymptotic test ideals; determinant norms and finite descent;
alterations; universal-homeomorphic normalization via Frobenius or
Roberts--Singh.

**Book use.** Chapters 37--45 after a separate proof audit. Bibliographic
metadata must be supplied before a conventional citation can be finalized.

### K-stability I

Boucksom--Jonsson, “A non-Archimedean approach to K-stability, I: metric
geometry of spaces of test configurations and valuations,” *Ann. Inst.
Fourier* 75 (2025), 829--927.
[arXiv](https://arxiv.org/abs/2107.11221),
[DOI](https://doi.org/10.5802/aif.3668).

**Contribution.** Graded norms and filtrations, \(d_p\)-completions,
divisorial norms, divisorial measures, and valuation metrics.

**Book use.** Chapters 33, 48--50.

### K-stability II

Boucksom--Jonsson, “A non-Archimedean approach to K-stability, II: divisorial
stability and openness,” *J. Reine Angew. Math.* 805 (2023), 1--53.
[arXiv](https://arxiv.org/abs/2206.09492),
[DOI](https://doi.org/10.1515/crelle-2023-0062).

**Contribution.** Beta invariants of divisorial measures, divisorial
stability, openness, and comparison with K-stability.

**Book use.** Chapter 50 and the research ledger. Conjectures on equality of
stability thresholds and entropy convergence of canonical degree-one
approximants remain version-sensitive research items.

### Synthetic finite-energy theory

Boucksom--Jonsson, “Measures of finite energy in pluripotential theory: a
synthetic approach,” *Contemporary Mathematics* 810 (2025), 159--208.
[arXiv](https://arxiv.org/abs/2307.01697),
[DOI](https://doi.org/10.1090/conm/810/16207).

**Contribution.** An axiomatic framework encompassing compact Kähler and
projective Berkovich finite-energy settings.

**Book use.** A synthesis section after the concrete BFJ/BJ/complex
constructions, not as a replacement for them.

### Green functions and failure of PL regularity

Boucksom--Jonsson, “Non-Archimedean Green's functions and Zariski
decompositions,” *C. R. Math.* 362 (2024), Special Issue S1, 5--42.
[arXiv](https://arxiv.org/abs/2304.00144),
[DOI](https://doi.org/10.5802/crmath.579).

**Contribution.** Theorems A--B give a divisorial Green function that is not
\(\mathbf Q\)-PL/model and a finite atomic Monge--Ampère solution supported
on a dual complex that is invariant under no retraction attached to any SNC
model.  This strengthens the earlier toric negative skeleton-factorization
example of Gubler--Jell--Künnemann--Martin: finite skeletal support does not
force the solution to factor through some refinement.

**Book use.** Chapters 29, 49, and 72.  The two expectations are recorded as
disproved, not left as regularity questions.  The PDF was not present in the
local Rethlas reference pack during the 15 August audit, and no solver packet
asks Rethlas to prove either resolved negative result.

---

## 6. Complex pluripotential foundations and rays

### Bedford--Taylor

Eric Bedford and B. A. Taylor, “The Dirichlet problem for a complex
Monge--Ampère equation,” *Invent. Math.* 37 (1976), 1--44.
[DOI](https://doi.org/10.1007/BF01418826).

Bedford--Taylor, “A new capacity for plurisubharmonic functions,” *Acta Math.*
149 (1982), 1--40.
[DOI](https://doi.org/10.1007/BF02392348).

**Contribution.** Local products for locally bounded psh functions, Dirichlet
problems, capacity, quasicontinuity, and pluripolar/negligible sets.

### Guedj--Zeriahi energy

Vincent Guedj and Ahmed Zeriahi, “The weighted Monge--Ampère energy of
quasiplurisubharmonic functions,” *J. Funct. Anal.* 250 (2007), 442--482.
[arXiv](https://arxiv.org/abs/math/0612630),
[DOI](https://doi.org/10.1016/j.jfa.2007.04.018).

**Contribution.** Full-mass and weighted energy classes, including
\(\mathcal E^p\), comparison and range questions.

### BEGZ

Boucksom--Eyssidieux--Guedj--Zeriahi, “Monge--Ampère equations in big
cohomology classes,” *Acta Math.* 205 (2010), 199--262.
[arXiv](https://arxiv.org/abs/0812.3674),
[DOI](https://doi.org/10.1007/s11511-010-0054-7).

**Contribution.** Nonpluripolar products, positive intersections and volumes,
full-mass/weighted-energy classes in big classes, variational existence and
uniqueness, ample-locus regularity, and singular Kähler--Einstein metrics.

**Status warning.** Some conjectural monotonicity and log-concavity statements
are historically resolved by Darvas--Di Nezza--Lu; general non-nef
ample-locus regularity and local finiteness beyond the Fujiki setting remain
live.

### Equilibrium energy and envelopes

Robert Berman and Sébastien Boucksom, “Growth of balls of holomorphic sections
and energy at equilibrium,” *Invent. Math.* 181 (2010), 337--394.
[arXiv](https://arxiv.org/abs/0803.1950),
[DOI](https://doi.org/10.1007/s00222-010-0248-9).

Robert Berman and Jean-Pierre Demailly, “Regularity of plurisubharmonic upper
envelopes in big cohomology classes,” in *Perspectives in Analysis, Geometry,
and Topology*, 2012, 39--66.
[arXiv](https://arxiv.org/abs/0905.1246),
[DOI](https://doi.org/10.1007/978-0-8176-8277-4_3).

**Contribution.** Equilibrium envelopes, differentiability of energy,
regularity, and algebraic approximation questions.

### Variational complex Monge--Ampère

Berman--Boucksom--Guedj--Zeriahi, “A variational approach to complex
Monge--Ampère equations,” *Publ. Math. IHÉS* 117 (2013), 179--245.
[arXiv](https://arxiv.org/abs/0907.4490),
[DOI](https://doi.org/10.1007/s10240-012-0046-6).

**Contribution.** \(\mathcal E^1\), dual energy of measures, coercivity,
variational solutions, weak Kähler--Einstein metrics, and balanced
approximations. It is the closest complex template for BFJ/BJ variational
theory.

### Darvas geometry

Tamás Darvas, “The Mabuchi geometry of finite energy classes,” *Adv. Math.*
285 (2015), 182--219.
[arXiv](https://arxiv.org/abs/1409.2072),
[DOI](https://doi.org/10.1016/j.aim.2015.08.005).

**Contribution.** \(d_1\) and Orlicz--Finsler completions, geodesic metric
structure, and energy/topology equivalences.

### Test curves and geodesic rays

Julius Ross and David Witt Nyström, “Analytic test configurations and geodesic
rays,” *J. Symplectic Geom.* 12 (2014), 125--169.
[arXiv](https://arxiv.org/abs/1101.1612),
[DOI](https://doi.org/10.4310/JSG.2014.v12.n1.a5).

**Contribution.** Test curves of singularity types, maximal envelopes,
Legendre transforms, filtrations, and recovery of Phong--Sturm rays.

**Book use.** Chapter 52, before transcendental non-Archimedean metrics.

### Test configurations and Duistermaat--Heckman measures

Boucksom--Hisamoto--Jonsson, “Uniform K-stability,
Duistermaat--Heckman measures and singularities of pairs,” *Ann. Inst.
Fourier* 67 (2017), 743--841.
[arXiv](https://arxiv.org/abs/1504.06568),
[DOI](https://doi.org/10.5802/aif.3096).

**Contribution.** Test configurations and filtrations,
Duistermaat--Heckman measures, intersection formulas for non-Archimedean
functionals, and uniform K-stability.

### Energy asymptotics and its erratum

Boucksom--Hisamoto--Jonsson, “Uniform K-stability and asymptotics of energy
functionals in Kähler geometry,” *J. Eur. Math. Soc.* 21 (2019), 2905--2944.
[arXiv](https://arxiv.org/abs/1603.01026),
[DOI](https://doi.org/10.4171/JEMS/894).

The [2022 erratum](https://doi.org/10.4171/JEMS/1215) states that the proof of
Theorem 5.6 is incorrect and its assertion is only possibly true. Theorem 5.4,
Theorem C, and Corollaries D--E are affected. Theorem A, Corollary B, and
results through Section 4 are unaffected.

**Book use.** Chapter 65 contains an explicit dependency audit; affected
claims are not repeated as established.

**Source exclusion recorded 23 August 2026.** At the author's request,
Mingchen Xia, “Deligne--Riemann--Roch Theorems I”
(arXiv:1710.09731), is not used anywhere in this book.  All
Deligne-pairing identities and slope computations used here are derived
from independent sources, principally the unaffected Sections 1--4 of the
Boucksom--Hisamoto--Jonsson paper above, or are reduced to intersection
formulas already proved in the book.  No claim may cite the excluded paper
directly or through an intermediate summary.

### Variational YTD in the Fano/log-Fano setting

Robert Berman, Sébastien Boucksom, and Mattias Jonsson, “A variational approach
to the Yau--Tian--Donaldson conjecture,” *J. Amer. Math. Soc.* 34 (2021),
605--652. [arXiv](https://arxiv.org/abs/1509.04561),
[DOI](https://doi.org/10.1090/jams/964).

**Contribution.** Twisted Kähler--Einstein currents, Ding coercivity,
stability thresholds, valuations, psh rays, and finite-energy
non-Archimedean potentials.

**Scope warning.** This is principally the smooth projective ample
Fano/log-Fano Ding theory, not the complete general cscK YTD theorem.

---

## 7. Complex/transcendental non-Archimedean theory

### Relative analytification over Stein algebras

Jürgen Bingener, *Schemata über Steinschen Algebren*, Schriftenreihe des
Mathematischen Instituts der Universität Münster, 2. Serie, Heft 10 (1976),
and Mingchen Xia, *Stein spaces*, version of 3 July 2026.

**Contribution.** Bingener constructs the relative analytification of schemes
of the appropriate finite-presentation type over a Stein algebra, compares
algebraic and analytic local properties and proper direct images, proves an
existence theorem for coherent sheaves near Stein compacta, and establishes a
relative Riemann existence theorem.  Xia's notes give a modern formulation and
fill in the proof details, including the role of excellent Stein compacta and
proper support.

**Book use.** These sources control the relative-algebraic interface in the
complex and hybrid parts.  They are especially relevant when a local analogue
of the global theory is formulated over a Stein base: algebraization or descent
of coherent/model data may be invoked only under the precise proper-support,
finite-presentation, and excellence hypotheses of the comparison and existence
theorems.  Bingener is the provenance source; Xia's notes are the detailed proof
source.  Neither source by itself supplies positivity, envelope, or
Monge--Ampère theorems.

### Darvas--Xia--Zhang

Tamás Darvas, Mingchen Xia, and Kewei Zhang, “A transcendental approach to
non-Archimedean metrics of pseudoeffective classes,” *Comment. Math. Helv.*
100 (2025), 269--322.
[arXiv](https://arxiv.org/abs/2302.02541),
[DOI](https://doi.org/10.4171/CMH/586).

**Contribution.** Relative test curves and non-Archimedean metrics for
pseudoeffective transcendental classes; projective comparison with BJ; finite
energy; flag configurations; approximation and radial Ding invariants.

**Book use.** Chapters 52--57.

**Exact open question.** Immediately before Definition 4.4 the authors state
that, for a big line bundle, it is unclear whether the filtration test curve
is already maximal and conjecture that it is.  Definition 4.4 therefore
maximizes the test curve before taking the Phong--Sturm ray.  The question is
about this specific construction, not the removal of every envelope or
\(P_\theta\)-projection in an arbitrary big-class theory.

### Partial Okounkov bodies

Mingchen Xia, “Partial Okounkov bodies and Duistermaat--Heckman measures of
non-Archimedean metrics,” arXiv:2112.04290v2, 13 April 2024.
[arXiv](https://arxiv.org/abs/2112.04290).

**Contribution.** Partial and limit Okounkov bodies of singular Hermitian big
line bundles, numerical-dimension and mixed-volume questions, Chebyshev
transforms, and Duistermaat--Heckman measures of non-Archimedean metrics.

**Exact source questions and current book status.** Conjecture 5.29 asks
whether \(\dim\Delta(L,\varphi)=\operatorname{nd}(L,\varphi)\).
Conjecture 8.8 asks for the stated non-toric mixed-volume formula with a
supremum over rank-\(n\) valuations.  At the end of Section 6.4 the paper
asks whether the Chebyshev transform is independent of the auxiliary
Kähler-current potential \(\eta\preceq\varphi\).  By contrast, Section 5.6
already asserts that the limit-body definition is independent of the
auxiliary ample divisor \(H\) and Kähler form \(\omega\); that independence
must not be recycled as open.

**Book use.** Conjecture 5.29 and auxiliary-\(\eta\) independence remain in
the source-scoped open-problem corpus.  The author-supplied repaired proof of
Conjecture 8.8, independently audited and verified in Chapter 55, closes its
smooth-projective positive-Cao-volume scope; this does not turn it into a
published result or settle the zero-volume, transcendental, singular-variety,
or attainment extensions.  The \((H,\omega)\)-independence is recorded under
resolved history.

### Xia on operations

Mingchen Xia, “Operations on transcendental non-Archimedean metrics,”
*Contemporary Mathematics* 810 (2025), 271--293.
[arXiv](https://arxiv.org/abs/2312.17150),
[DOI](https://doi.org/10.1090/conm/810/16216).

**Contribution.** Maxima, monotone limits, regularized suprema, rescaling,
addition, and restriction on reduced irreducible unibranch compact Kähler
spaces; equivalence between the algebraic envelope conjecture and bijectivity
of the comparison map.

**Book use.** Chapter 54 for the operations package and as a historical
precursor to the separate trace theorem below.

**Exact trace boundary.** Definition 2.11 and Proposition 2.12 give the
earlier trace construction and its multiplier-ideal dependence.  They must
not be used to truncate the stronger target supplied by the later
Darvas--Xia trace theorem.

### Darvas--Xia on analytic trace

Tamás Darvas and Mingchen Xia, “The trace operator of
quasi-plurisubharmonic functions on compact Kähler manifolds,” 2024.
[arXiv](https://arxiv.org/abs/2403.08259).

**Contribution.** On the natural domain
\(D_Y=\{\varphi:\nu(\varphi,Y)=0\}\), restricted quasi-equisingular
approximants admit a trace.  Every trace is \(\mathcal I\)-good, two choices
are \(P\)-equivalent, and
\(\varphi\preceq_{\mathcal I}\psi\) implies
\(\operatorname{Tr}_Y(\varphi)\preceq_P
\operatorname{Tr}_Y(\psi)\).  Trace is continuous along the sourced
decreasing \(d_S\)-convergent nets.

**Exact quotient map.** The source provides
\[
 D_Y/{\sim_{\mathcal I}}
 \longrightarrow
 \operatorname{QPSH}(\widetilde Y)/{\sim_P}.
\]
Thus the formerly listed request for a \(P\)-valued target is resolved
history, not an open problem.  This does not identify \(P\)- and
\(\mathcal I\)-equivalence for the ambient inputs.

**Book use.** Chapters 51, 54, 67, 69, and 72; the supplied trace chapter of
the author's book is used for the complete proofs and exact net statement.

### Mesquita-Piccione

Pietro Mesquita-Piccione, “A non-Archimedean theory of complex spaces and the
cscK problem,” *Advances in Mathematics* 481 (2025), Paper 110543.
[arXiv](https://arxiv.org/abs/2409.06221),
[DOI](https://doi.org/10.1016/j.aim.2025.110543).

**Contribution.** Tropical spectra and the compact semivaluation space
\(X^\beth\) for complex spaces; density of divisorial points; inverse limits of
dual complexes; log discrepancy; PL/b-divisor and psh finite-energy theories;
complex-to-non-Archimedean rays; entropy and Mabuchi functionals; comparison
with DXZ in the Kähler finite-energy setting; strong K-stability implying a
unique cscK metric.

**Book use.** Chapters 58--60 and the comparison Chapter 63.

### Mesquita-Piccione--Witt Nyström

Pietro Mesquita-Piccione and David Witt Nyström, “A transcendental
non-Archimedean Calabi--Yau theorem with applications to the cscK problem,”
42 pp., submitted 11 September 2025.
[arXiv](https://arxiv.org/abs/2509.09442).

**Contribution.** Weak topology and nonpluripolar points; continuity of
envelopes; orthogonality; strong topologies; transcendental
non-Archimedean Calabi--Yau; measures on dual complexes; regularity;
uniform K-stability for models implying a unique cscK metric; valuative
criterion and beta invariant.

**Book use.** Chapters 61--62.

**Scope warning.** This proves the model-stability implication, not the
ordinary general cscK YTD equivalence in every formulation.

### Current 2026 bridge notes

Sébastien Boucksom and Mattias Jonsson, “From complex to non-Archimedean
geometry: an approach to the YTD conjecture,” version 2, 19 May 2026.
[arXiv](https://arxiv.org/abs/2602.10800).

**Contribution.** Current overview of algebraic, analytic, and
non-Archimedean geometry in the YTD programme.

**Book use.** Orientation and current-status cross-check, not a replacement
for proof sources.

### Post-2025 YTD claims and exact residuals

Sébastien Boucksom and Mattias Jonsson, “On the Yau--Tian--Donaldson
conjecture for weighted cscK metrics,” arXiv:2509.15016v1, 18 September
2025. [arXiv](https://arxiv.org/abs/2509.15016).

Tamás Darvas and Kewei Zhang, “A YTD correspondence for constant scalar
curvature metrics,” arXiv:2509.15173v2, 3 November 2025.
[arXiv](https://arxiv.org/abs/2509.15173).

Antonio Trusiani, “A solution to the Yau--Tian--Donaldson Conjecture through
Special Fujita Approximations,” arXiv:2605.30063v1, 28 May 2026.
[arXiv](https://arxiv.org/abs/2605.30063).

**Dated claims.** Boucksom--Jonsson formulate cscK and weighted-extremal
existence through their non-Archimedean stability theory on polarized
projective manifolds.  Darvas--Zhang state a compact-Kähler correspondence in
their \(K^\beta\) signature and, in the polarized projective case, a
reductivity plus log-discrepancy-model formulation.  Trusiani's Theorem B
states special Fujita approximation, Corollary A states the relevant entropy
regularization, Theorem A states the smooth polarized projective
automorphism-relative uniform YTD theorem, and Corollary B reports the
equivalence of the standard smooth polarized projective stability
formulations listed there.  These are version-one/version-two preprint
claims and are reported with their dates; this map does not independently
reprove them.

**Residual primary-source questions.** Boucksom--Jonsson's “Questions and
further remarks” asks for a direct algebraic proof that b-K-polystability is
equivalent to uniform stability, a dimension-dependent bound on the support
size of divisorial test measures, algebraic proofs of equivariance, an
extension to polarized klt pairs, and a nonprojective Kähler extension.
Darvas--Zhang leave regularization by test configurations of rays attached to
log-discrepancy models and the equivariant transcendental extension,
especially for a nontrivial group, as residual directions.

**Book-formulated residual.** The hybrid compactness and measure-continuity
bridge needed to pass through a degenerating family is the book's synthesis
problem, not a question quoted verbatim from any one of these preprints.
Trusiani's Corollary B means that the undifferentiated comparison of the
standard smooth projective signatures listed there is no longer treated as
open; direct algebraic, transcendental, equivariant, hybrid, and singular
extensions remain separately labelled.

---

## 8. Dependency order for the complex/transcendental bridge

The efficient graduate-level order is

\[
\begin{aligned}
&\text{Bedford--Taylor capacity and products}\\
&\quad\longrightarrow
\text{Guedj--Zeriahi / BEGZ finite-energy theory}\\
&\quad\longrightarrow
\text{Berman--Boucksom / BBGZ variational theory}\\
&\quad\longrightarrow
\text{Darvas }d_1\text{ geometry}\\
&\quad\longrightarrow
\text{Ross--Witt Nyström test curves}\\
&\quad\longrightarrow
\text{DXZ/Xia}\\
&\quad\longrightarrow
\text{Mesquita-Piccione}\\
&\quad\longrightarrow
\text{Mesquita-Piccione--Witt Nyström}.
\end{aligned}
\]

BHJ and BBJ enter in parallel when filtrations, slopes, Ding/Mabuchi
functionals, and K-stability are introduced.

---

## 9. Version and theorem-status warnings to display in the book

1. **CLD:** cite version 2 (25 July 2025), not only “2012.”
2. **BFJ:** retain the original discrete-valuation, residue-characteristic-zero,
   smooth/projective/ample hypotheses at first statement.
3. **BFJ equation:** distinguish the original algebraizability and support
   hypotheses from later removals/partial extensions.
4. **BJ envelope:** public literature reaches the 2024 addendum; the full
   unibranch theorem comes from the supplied manuscript and requires an
   internal proof audit.
5. **BHJ 2019:** display the 2022 erratum and its dependency cone.
6. **Green functions:** divisorial or atomic data do not imply PL/model
   regularity.
7. **Mesquita-Piccione:** use the accepted 2025 journal version and identify
   the exact finite-energy/Kähler comparison scope.
8. **MPWN:** model-stability is stronger than the original narrow
   test-configuration condition.
9. **2025--2026 YTD preprints:** label claims by version and date.  Trusiani
   Corollary B removes the undifferentiated smooth-projective signature
   question in its stated scope; retain only the exact direct-algebraic,
   equivariant, transcendental, hybrid, and singular residuals.
10. **Terminology:** “Pietro M-P” is Pietro Mesquita-Piccione; the bibliography
    will use the author's published hyphenation.

---

## 10. Literature-based open-question corrections

The research ledger contains detailed statuses. The most important
literature corrections are:

- removing BFJ algebraizability in residue characteristic zero is solved;
- the BFJ divisorial Green-function/model-function expectation and the
  stronger single-SNC-skeleton factorization expectation are false by
  Boucksom--Jonsson (2024), Theorems A--B;
- Zhang's two 2014 local-volume questions have opposite resolved answers: the
  dimension-only positive lower bound is true for nonzero isolated
  Gorenstein volume, while volume zero does not force a log-canonical
  boundary in the non-\(\mathbf Q\)-Gorenstein setting;
- the MP24 missing non-Archimedean Calabi--Yau theorem is solved by MPWN;
- BEGZ monotonicity and log-concavity issues used by this book are historical,
  not current;
- arbitrary smooth complex geodesics are known to fail;
- CLD Lemma 8.1.4 already proves eventual cardinal stabilization; only
  stage-one or controlled-early collapse remains open, along with the two
  local/global metric questions of Remark 17.8.10;
- the three Gubler--Jell--Rabinoff questions, the Pille--Schneider arbitrary-
  field \(\mathcal E^1\) operator, DXZ filtration-test-curve maximality,
  Xia Conjecture 5.29 and auxiliary-\(\eta\) independence, and the three
  exact BMPS questions remain source-stated open items; Xia Conjecture 8.8 is
  closed in the Chapter 55 positive-volume scope by the author-supplied
  repaired proof, without a publication claim;
- Xia's limit-body independence from \(H\) and \(\omega\) is already asserted
  in Section 5.6 and is distinct from the Chebyshev auxiliary-\(\eta\)
  question;
- the Darvas--Xia trace theorem already gives a target \(P\)-class from an
  input \(\mathcal I\)-class; the former trace-refinement problem has been
  removed from the active list;
- Trusiani's Corollary B reports the standard smooth polarized projective
  signature equivalences; the post-2025 YTD corpus therefore retains the
  narrower direct-algebraic, support-bound, equivariant, transcendental,
  hybrid, and singular residuals;
- the general nontrivially valued finite-energy/full-measure equation, full
  higher-dimensional local CLD/global BFJ psh comparison, several CLD
  regularization questions, BJ valuation-topology questions, and the general
  compact-Kähler YTD bridge in the exact residual signatures remain
  genuinely delicate;
- the supplied envelope manuscript changes BJ Conjecture 5.14 from an open
  item into a theorem-to-audit.

---

## 11. Source-freeze checklist

Before drafting a chapter, the following must be recorded for every anchor
source:

- [ ] exact title, author spelling, journal, year, DOI, and arXiv version;
- [ ] theorem/definition numbers used;
- [ ] hypotheses copied and translated into the book's convention sheet;
- [ ] errata and later corrections;
- [ ] whether the cited version is published, accepted, preprint, or supplied
      manuscript;
- [ ] notation and normalization differences;
- [ ] dependency on resolution, multiplier ideals, test ideals, alterations,
      envelope continuity, or orthogonality;
- [ ] whether the theorem treats sequences, nets, or arbitrary families;
- [ ] whether values at nontrivial-support semivaluations are included;
- [ ] whether total Monge--Ampère mass is normalized.
