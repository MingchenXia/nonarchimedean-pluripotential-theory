# OT/Bergman and positive-model follow-up audit

Date: 4 October 2026. The active book remains the checked 4,244-page
intermediate-limit edition. This checkpoint adds two fully written
conditional research derivations outside the manuscript. It makes no new
open-problem solution, novel theorem, priority or independent-model verdict
claim.

## Primary-source scope and editions

The cached author-hosted Demailly PDF is *Analytic Methods in Algebraic
Geometry*, **July 2011**, 228 pages. Its SHA-256 is
`6f4682f322d6ae0c0ce3feae4964792c473a3d9051fe01288ef9017ca341d009`.
The fresh text reading covers lines 9400–9995 (596 lines), including the
complete statement and printed proof of Theorem 13.6, Remark 13.7 and
adjacent corollary material. Physical/printed pages 125–131 were rendered
and all seven actually inspected. The applied statement is Section 13.C,
Theorem 13.6 for rank \(r=n\), \(q=0\), with the metric-independent norm
interpretation of Remark 13.7(a). The curvature conditions, small-section
condition and regular zero scheme were checked against the actual page.
This is a scoped reading, not a full fresh reading of the book or a fresh
independent verification of all its analytic imports.

Li's arXiv:2505.11087v1 Proposition 4.2 and the published intermediate-limit
paper's Proposition 6.7 cite the **2012 print edition**, Section 12.C and
Theorem 12.6. That edition's actual pages were not acquired in this
follow-up. The 2011 author manuscript is already a separate bibliography
entry `DemAMAGAuthor2011`; the 2012 print edition is `Dem12`.
The reconstruction states and applies the checked 2011 theorem directly;
it does not authenticate the printed 2012 locator by analogy. A bounded
Crossref title query returned five related Demailly works without the
requested book. This does not prove the book absent from Crossref and
does not authorize substituting a different publication.

The two Li primary files retain their earlier full-source audits.
The point-extension passages were freshly reread: arXiv v1 lines
1340–1475 and the published intermediate paper lines 1553–1650.
Their earlier metadata, acquisition records, complete-reading manifests
and actual-page records are unchanged.

Stacks primary caches were freshly inspected for Tag 0C4K, Lemma 29.38.8
(statement and proof), its proof input Tag 0892, Lemma 29.38.7 (statement
and proof), and the scoped Tag 01OF statements/proofs of Lemmas 31.33.4
and 31.33.13. These are cached primary scheme pages, not a fresh live-page
update check. Chapter 59's existing projective-germ interface explicitly
distinguishes the scheme statements from their analytic application.
The rest of Section 31.33 is not claimed freshly read in full.

## Point-extension reconstruction

The [Bergman derivation](research_dossiers/li_ot_bergman_reconstruction_20261004.md)
assumes a fixed relative embedding of a power of the polarization on a
smooth proper SNC model, a nonvanishing meromorphic volume form on the
punctured family and smooth semipositive potentials of oscillation
\(O(-\log|t|)\). It gives the expected \(CT/l\) logarithmic error uniformly
in \(l,t,z\), for all \(l\) above one fixed degree. The ambient dimension
and the model are fixed; there is no asserted uniformity over every model.

The proof spells out the following inputs that are compressed in the
source application:

- A bounded right inverse to the total-space projective immersion and the
  SNC equation give a lower bound for the **maximum of all projective
  wedges**, divided by the meromorphic volume. Meromorphy of an arbitrary
  single quotient would not give this bound.
- Hyperplane sections through the point are perturbed within that
  linear system. Parametric transversality yields a finite transverse
  zero scheme, while retaining half the chosen Jacobian and bounded
  coefficients. No uniform perturbation radius is asserted or needed.
- The auxiliary embedding degree \(k\) is separated from the reserved
  positive curvature degree \(N=(n+1)k+1\). The two conditions of the
  checked extension theorem then hold with \(\alpha=1\).
- Extension data vanish at the other zeros, so their Jacobians make no
  contribution. The ordinary integral is controlled by the extension
  weight, and restoration of the full tensor weight costs
  \(2N\operatorname{osc}\varphi_t\), independent of \(l\).

The proof includes \(l=N\) and \(n=1\), excludes the rank-zero extension
case, and requires the family to be projective. It preserves the raw
volume measure, squared-norm convention and invariance under scalar
potential shifts. This is an explicit conditional derivation from an
imported extension theorem, not an independent certification of the
general CY hybrid theorem.

## Positive reference on a specified modification

The [model bridge](research_dossiers/li_positive_model_bridge_20261004.md)
starts with a supplied relatively ample projective extension of a power
of \(L\), and a supplied finite sequence of blowups over zero ending in
a smooth SNC total space. The negative exceptional tautological sheaves,
combined by relative ampleness, give a vertical divisor \(G\). A bundle
\(f^*A_0^a\otimes\mathcal O(G)\) is relatively ample for large fixed \(a\).
Its root FS metric is a positive rational extension of \(L\) whose
fibre curvature equals the restriction of a total-space Kähler form.
This supplies the earlier comparison construction's uniform positivity
for that chosen reference.

A **meromorphic** reference identification is retained. Its vertical
divisor coefficients and \(\operatorname{div}(t)=\sum b_iE_i\) show that
the background change is \(O(T)\), preserving the CY oscillation scale.
A nonmeromorphic identification with an essential singularity is outside
the argument. SNC multiplicities are allowed: independent logarithmic
coordinates satisfy \(\sum b_ix_i=1\), and the scalar-profile bound still
applies on the fixed weighted interior. The curvature class and fixed
\(2\pi\)/norm-potential factors are recorded explicitly.

This removes the separate positivity assumption **conditional on the
specified projective blowup model and meromorphic identifications**.
It does not assert that the unmodified pullback of every ample bundle is
uniformly positive. Existence of an appropriate SNC/projective model for
an arbitrary proposed family remains a source/application gate. The
historical metric dossier and its scalar calculation are unchanged.

## Verification and next dependencies

Both complete proof texts were read after writing, including signs,
potential shifts, weighted simplices, compactness, curvature loss and
all constant dependencies. This is the author's self-audit, **not** a
separate model-verifier run. No finite calculation, compilation or novel
receipt was needed or claimed for these book-external Markdown additions.
The 2011 source's \(q>0\) regularity and all underlying analytic imports
are not certified by this \(q=0\) application.

The [manifest](li_ot_and_positive_model_manifest_20261004.json) pins the
current proofs, this audit, checked source bytes, actual-page records and
the historical source/repair manifests. Remaining general-degeneration
gates are the projective/SNC model inputs, chamber geometry and formal
orthogonal-basis existence, convergent section-module/base change,
uniform Skoda and generic-region mass, and hybrid uniform approximation
with identification of the limiting potential. All 42 open-problem
statuses and every active TeX/bibliography input are preserved.
