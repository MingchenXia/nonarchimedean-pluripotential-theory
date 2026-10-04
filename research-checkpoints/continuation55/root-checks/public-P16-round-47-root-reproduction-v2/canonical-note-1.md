ID: n1

SUMMARY:
Exact-source audit: saved BFJ 1201.0188v1 retains function-field algebraizability and SNC support; BE 1805.01016v3 reports a descent/resolution-restricted characteristic-p envelope result. All ten source hashes verified.

DETAILED SUMMARY:
The original proof uses cofinal regular SNC models, skeleton equicontinuity, multiplier-ideal positivity and envelope regularization, followed by locality and algebraizability-dependent orthogonality. The saved 1201.0188 is actual v1. Its algebraizability concerns descent of X to a one-variable function field with completion K; L need not descend. BE's reported positive-characteristic envelope result instead assumes descent of (X,L) and resolution in dimension n+d. These statements do not establish the full positive-residue-characteristic finite-energy equation.

SUPPORT:
[]

TEXT:
The audit used only input.json, the ten listed public caches and fresh workspace artifacts.

BFJ 1201.0187v2 assumes complete discrete valuation, residue characteristic zero, smooth projective X and ample L. Its banner is 21 January 2014; its internal manuscript date is 22 October 2018. SNC cofinality enters the original psh definition and retractions. Sections 5–8 also use multiplier ideals for positivity, toroidal equicontinuity for normalized compactness, and subadditivity/global generation/vanishing for envelope regularization. Resolution alone does not replace these ideal-theoretic uses.

The actual saved 1201.0188v1 has banner 30 December 2011. Theorem A requires smooth projective X over complete discretely valued K of residue characteristic zero, ample L, and positive Radon μ of mass (L^n) supported on an SNC dual complex. X must satisfy X=Y_K for smooth projective Y over a one-variable function field F whose completion is K. The statement does not require L to descend. Appendix A uses this algebraizability for orthogonality through compactification and big-line-bundle decompositions. This saved theorem cannot be treated as a later arbitrary-support theorem.

1805.01016v3 is Boucksom–Eriksson, Spaces of norms, determinant of cohomology and Fekete points in non-Archimedean geometry. Theorem 9.15 identifies relative volume with relative MA energy for continuous psh metrics on semiample Q-line bundles on geometrically reduced projective varieties over any complete valued field. Smooth X and ample L meet these hypotheses. Section 7.30 still labels unrestricted envelope continuity conjectural. Its reported discrete characteristic-p case assumes descent of (X,L) to a function field of transcendence degree d and resolution in dimension n+d, replacing multiplier ideals with test ideals. The cited GJKM paper is not supplied, so its exact stronger resolution formulation is not independently asserted here. This report gives neither a mixed-characteristic conclusion nor an unbounded equation theorem in this draft.

Pille–Schneider 2209.04879v2, Remark 4.4, distinguishes defining E1 from extending MA to E1. Section 1.2 expressly assumes equicharacteristic zero; the shorter wording “characteristic zero” in the remark does not establish a mixed-characteristic endpoint.

Execution evidence: source_audit.py reported 10 verified sources, 20 matching PDF/text SHA256 values, six matching abstract hashes, byte_identical_input=true and 52 literal extracts. The actual 1201.0188v1 PDF SHA256 is 4c29d91987477baf9baa4dfdd0b901ae1cd8910746012fd6285ab9a90bbf3f3a. input.json and input-original.json both have SHA256 b25c64ae0b33d0f726371bae85dff3802a464ea4e786375ad8b558f03215a1f8. assignment-original.txt and task-original.json preserve the decoded assignment/task.

Artifacts: source_audit.py, source-audit-output.json and source-extracts/source-provenance.json, alongside copied PDFs and regenerated PDF text. Provenance includes literal published proof extracts, versions/hashes, line/page locations and application checks. Rerun: python3 source_audit.py. Hash agreement establishes artifact identity, not mathematical correctness.

Artifacts: /workspace/research/campaigns/round-47/P16.3-public-source-positive-residue-characteristic/artifacts/codex-69HHDl
