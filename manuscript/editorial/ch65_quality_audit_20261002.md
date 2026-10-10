# Chapter 65 completion audit

Date: 2 October 2026.

Base: local Chapter 64 commit 97ee2ac.

Scope: parts/part6/ch65_rays_filtrations.tex, under the sequential quality
programme. The whole-book completion goal continues. Independent Chapter 72
research remains paused; frozen releases, receipts and checksum ledgers are
preserved.

## Mathematical and expository review

The entire chapter and all six earlier Chapter 65 unit audits were read.
All seventeen formal assertions were checked with their proofs or precise
imported interfaces. The chapter has thirty labelled reusable environments,
including eight examples, and 108 labels. Its thirteen numbered sections,
two subsections and source note have semantic labels. The introduction
identifies the algebraic, analytic, energy and comparison dependencies.

The checks and repairs include the following:

- The test-configuration filtration uses the actual integer jumps and their
  ceiling extension. Its full equivariant lattice, decreasing sign and
  finite-generation bounds are retained. The converse uses a degree-one
  Veronese Proj, flatness over the parameter ring, normalization and section
  saturation. Uniqueness is asserted for the ample integrally closed model,
  rather than every raw presentation.
- The finite-generator Fubini--Study formula includes proper-support
  semivaluations and rational polarization degrees. The proof of integral
  closure invariance handles infinite ideal values, the graded Gauss
  extension and the section-saturation power argument. The nonnormal P1
  example computes changed weights, changed base ideals, a common metric
  and the persistent odd-weight discrepancy under base change.
- Sup and L2 norms use the fixed smooth positive probability volume form.
  Their uniform polynomial comparison supplies the explicit logarithmic
  error. The worked volume-form example is now a labelled example: its
  beta integral shows strict failure if that error is omitted.
- The filtered test curve is built from regularized tails. Concavity uses
  multiplication in common degrees; maximality is the precise RWN envelope
  input. The closed terminal value is a left limit. The unattained scalar
  and parity examples prevent an all-degree terminal limit from being
  substituted for the tail construction.
- Pointwise concave biconjugacy fixes the Legendre sign, the zero reference,
  and the finite-time ray bounds. Character translation and the factor-two
  radial conversion remain independent operations.
- The weighted Bergman inequality first compares L2 obstacles. Its passage
  to sup obstacles pays the norm error. Two direct inequalities reconstruct
  the RWN Phong--Sturm tail-envelope identity, without commuting a parameter
  supremum with an asymptotic limit. The original traceless generator,
  basis rescaling and time sign are recorded separately. The PS existence
  theorem is a precise imported interface, not a new proof of its entire
  original curvature argument.
- The finite-generation analytic square uses globally generated degree-one
  sections, flag coefficient ideals, inclusion of filtered section spaces,
  and DXZ's exact flag valuation formula. Degree and character translations
  are tracked in both the test curve and ray. BJ divisorial determination
  extends the established equality to all semivaluations. Normalization
  then preserves the closed curve and ray; it need not preserve finite-level
  weights or Bergman potentials. Their compact-time bound is explicitly
  nonuniform on the whole time half-line.
- For each strict interior threshold, a high-slope section times a complete
  residual series supplies an ample subseries and birationality. Resolving
  the base ideal computes partial Monge--Ampere mass. Hisamoto's birational
  Fujita interface and a cofinal factorial degree sequence give the volume
  identity. The finite-cover counterexample keeps the birational hypothesis
  visible; bounded singularities alone do not give the series volume.
- Spectral quantization uses BC's probability normalization, bounded support
  and all moment convergence. Interior tails identify its limit with V^-1
  times the analytic DH measure. The terminal atom is the left-limit mass,
  not the terminal graded series. BHJ's actual polarization degree removes
  the apparent Veronese dilation.
- The capped-weight example computes zero terminal series and a positive
  limiting terminal atom. A new moving-threshold calculation gives finite
  tail zero at tau_m = b - 1/(2m), while the limiting tail tends to 1-b.
  Fixed interior convergence is therefore not used uniformly at the atom.
  The dimension-zero case is treated by scalar Fekete superadditivity.
- Finite-level moment and orthonormal monomial calculations recover the
  complete P1 Bergman ray. The O(d) calculation separates support dilation,
  raw mass d, probability mean d/2 and raw first moment d^2/2.
- Radial energy uses the RWN bounded-ray energy identity and the DH layer
  cake, including the terminal jump. The compactified intersection slope
  uses relative Serre vanishing and Riemann--Roch, without claiming that
  the polarization is ample on the total space.
- The unaffected BHJ19 slope reconstruction now converts the differential
  operator as well as the weights and time: ddc_wt = 2 ddc and
  ddc_wt psi_s = ddc varphi_2s. Every raw curvature occurrence in that proof
  uses ddc_wt; MA_wt is explicitly probability normalized by V. Deligne
  pairing and local SNC estimates are imported only from Sections 1--4.
  The entropy replacement, its logarithmic upper and lower bounds, and
  the Chen--Tian decomposition keep this convention throughout.
- The logarithmic statement retains a rational Weil boundary with K_X+B
  Q-Cartier and the source's subklt and semipositivity hypotheses. Boundary
  terms are raw Deligne pairings, avoiding division by a possibly zero
  restricted volume. When that degree is positive the normalized restricted
  energy formula follows. A new big-nef blowup example has L.E = 0 and
  computes the zero pairing and intersection even though probability MA
  and normalized energy on E are undefined. The big-nef entropy argument
  chooses a smooth positive canonical volume and interprets 0 log 0 as zero.
- The complete P1 inverse Legendre formula has a reusable equation label and
  computes all endpoint values. The comparison table retains every reverse
  condition and loss of finite-level information. Cone identification alone
  is not used to identify nonlinear Monge--Ampere operators.
- The published BHJ erratum ledger precisely quarantines Theorem 5.6,
  Theorem 5.4, Theorem C and Corollaries D--E. The authors leave open whether
  the flawed statement is true, while confirming Theorem A, Corollary B
  and all results through Section 4. No surrogate use or arbitrary weak-ray
  slope extension is inferred.

House inline mathematics is used throughout. Compact formal statements,
the three shorter new/revised examples, the P1 translation block and the
source note are kept together; proofs remain outside statement minipages.

## Direct primary-source interfaces

Nine primary PDFs and 63 selected pages were read and visually inspected.
The source-version record distinguishes fresh published PDFs, cached
published PDFs and Hisamoto's dated preprint. These are direct interface
checks, not an independent verification of every imported deep theorem.

| Source and version | Interfaces checked | Physical PDF pages |
| --- | --- | --- |
| RWN14, freshly retrieved published JSG 12 (2014), 125--169 PDF | Proposition 6.7 and its energy proof, Proposition 6.10, Lemmas 7.4--7.6, Proposition 7.7, Proposition 7.11 and Corollary 7.12 with proofs; Definition 9.1 and full Theorem 9.2 proof | 1, 26--36, 40--42 |
| BC11, freshly retrieved published Compositio Mathematica 147 (2011), 1205--1231 PDF | Definitions 1.1--1.4, full Lemma 1.6 proof, closed concave transform, Theorem 1.11 and Remark 1.12 with proof | 1, 7--11 |
| His13, arXiv:1201.4236v3, 26 November 2012, twelve-page preprint | Theorem 1.3, moving-product Proposition 3.7 and Proposition 4.2 with proofs, Example 3.2 and Remarks 3.8/4.3 | 2, 5--9 |
| PS07, freshly retrieved published JSG 5 (2007), 221--247 PDF | Theorem 1.1's original existence interface; traceless generator and squared radial parameter in Section 2.1; basis rescaling in Section 4.2 | 2--3, 5--6, 17--18 |
| BHJ19, published JEMS 21 (2019), 2905--2944, checked cached PDF | Norm-weight differential convention; Theorem 3.6, Lemma 3.9 and full proof, Lemmas 3.10--3.11 and local estimates; rational boundary definition, Theorem 4.2 and full Section 4.5 proof including its weaker-positivity footnote | 1, 5, 18--23, 26--27 |
| BHJ17, published AIF 67 (2017), 743--841, checked cached PDF | Section 1.2 equivariant lattice proof; Lemmas 2.13--2.14 and Proposition 2.15 proof; probability moments in Corollary 3.4; Proposition 3.12(iii) barycenter proof; Proposition 5.9 filtration proof | 13--14, 28--29, 33, 36--37, 51 |
| BJ22, published AFST 31 (2022), 647--836, checked cached PDF | Proposition 2.30, both clauses of Theorem 2.31, Corollary 2.32; Theorem 4.22 and Corollary 4.23 including divisorial determination proof and decreasing-net argument | 40--42, 70--71 |
| DXZ25, published Geometry & Topology 29 (2025), 269--322, checked cached PDF | Theorem 3.12(i) exact order-reflection interface; Lemma 4.5 and Proposition 4.6 proofs; Definition 4.7, Proposition 4.8 and full Lemma 4.10 proof | 26, 34--37 |
| BHJ erratum, published JEMS 24 (2022), 735--736 | Incorrect reduction claim, counterexample, possible remaining validity, and exact affected/unaffected dependency ledger | 1--2 |

Hisamoto's publisher download returned a landing page, not a published PDF.
The current proof check uses the explicit v3 preprint: Theorem 1.3 maps to
published Theorem 3, Propositions 3.7/4.2 to Propositions 17/19, and Example
3.2 and Remarks 3.8/4.3 to Example 12 and Remarks 18/20. The chapter retains
the published bibliography and locators checked in its earlier unit audit.
No fresh publisher-PDF verification of that article is claimed. Cofinal
factorial degrees in the book replace the insufficient dyadic cofinality
shortcut. The RWN all-degree terminal shortcut is not carried into the
closed-endpoint construction; its printed layer-cake typo is not propagated.

Source SHA-256 values (cached files are not staged):

- RWN: `fe45eb080e0b2f4e18abf35ecf4e80580a49b21be47a26534ac5c1568721d160`.
- BC: `0ed60336258435ffc720b4940c54b714750f5e3af49b92e33c66a02e829c94f2`.
- His: `ebbbb29cd38e0e4fd255a8296e088c5778a2472e033fe49e359fbb4ce8250227`.
- PS: `85236cbbe2084840eb84609fe4ee163597213aa5069e7556e9c431126bff5bfb`.
- BHJ19: `e0042513cdb7e565a4d63b556f478bb588dd85561305e2ce4240aab8b76e0832`.
- BHJ17: `edfd3b1506b49cf42ae85014d731bd9d86af5ed248134397cd562fba70c6f60e`.
- BJ: `50bd6e6782c29088edc96d013a5d49257b0395d9fb398664f1a9859639992948`.
- DXZ: `467778ff37b893681482e43b4d8f1d717e947a34fe61026b2e6bc418e4a1f70e`.
- Erratum: `62efc671a6e837f9166144dc93ab4dfe6fbca52b64ad7dcea11519641097e873`.

## Example supplement

The supplement passes 81,126 exact rational checks and 312 numerical checks
in 33 families. It covers capped-weight multiplicativity, fixed and moving
tails, terminal atoms, moments and character shifts; nonnormal and
normalized monomial weights, finite FS bounds and base-change discrepancies;
flag coefficient ideals against an independent Rees monomial enumeration,
including infinite values and the trivial flag; scalar unattained and
parity endpoints; the custom-volume beta integral and norm error; complete
orthonormal monomials; P1 and O(d) moments and mass conversions; numerical
inverse-Legendre minima and Bergman bounds; operator/time/weight conversion;
and the big-nef exceptional degree. These computations supplement the
worked proofs and examples; they do not test the general imported theorems.

## Build, render and final gates

Three changed-source full builds pass. The final PDF has 4,142 pages
and 19,313,995 bytes. Source SHA-256:
`b64f2ba076040fe26d1b861dc2c510c05a03fcd93f7abcddfbb9b78bbc8030e4`.
PDF SHA-256:
`2facc7a395165016d6b06c0a0c223e8994dd6ff009652d86573363b60bd0adbd`.
There are no unresolved references/citations, missing glyphs, rerun requests
or fatal errors. Chapter 65 has no overfull boxes or LaTeX/package warnings.
Eighteen inherited overfull boxes elsewhere and thirteen duplicate PDF
destinations in Chapter 70 remain recorded for the whole-book pass.

All 34 physical chapter pages 3347--3380 (printed 3277--3310) and adjoining
physical pages 3346 and 3381 were visually checked at detail size. All
seventeen images changed by the second build were reinspected, then all ten
images changed by the last page-boundary repair were reinspected. The other
26 final chapter/seam images match inspected preceding images byte for byte
at the same render resolution. Physical 3380 is intentionally blank. The
long example now begins with its Rees algebra on the same page. No reviewed
layout defect remains.

The post-render scoped check finds seventeen formal assertions, thirty
labelled reusable environments and 108 labels, without duplicate labels,
unlabelled objects, missing proofs, environment imbalance, unfinished
markers or legacy inline delimiters. Project references pass for 425 inputs
and 12,295 unique labels with no missing input or dangling reference; all
six checker tests pass. The inventory remains 42 active atoms in twelve
Chapter 72 environments, tiers (0,3,7,15,17). git diff --check passes. The
unavailable legacy house-audit executable is replaced by the recorded
manual and scoped review, rather than reported as having run.

Frozen releases, receipts and checksum ledgers are unchanged. This direct
editorial/source audit claims no new independent verifier verdict. Chapter
66 is next; the whole-book completion goal continues. Verified commits
remain local pending explicit remote-push approval.
