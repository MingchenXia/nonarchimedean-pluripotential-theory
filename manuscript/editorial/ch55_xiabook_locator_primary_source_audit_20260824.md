# Chapter 55 XiaBook locator primary-source audit

**Audit date:** 2026-08-24 (Asia/Shanghai)  
**Verdict:** **PASS.  The four locator criticisms in the whole-Chapter 55
Rethlas report, and the two repeated XiaBook locator criticisms in the later
metric-only run, are false positives and are rejected.**  The five restored
live citations (four mathematical uses and one provenance repetition) agree
with both the identified primary PDF and the supplied author source.  No
XiaBook locator repair remains.

## Controlling sources

1. `tmp/pdfs/SGPT_final_20260718_primary.pdf`, *Singularities in Global
   Pluripotential Theory*, 549 pages, 2,373,363 bytes, SHA-256
   `c816eea5f06822021fa8dd75b70f82724ee47e6dcd6830729f5ecc109296b706`.
   `pdfinfo` reports `CreationDate: Sat Jul 18 10:44:19 2026 CST`.  The
   bibliography supplied with the author's paper identifies the 18 July
   2026 source as
   `https://mingchenxia.github.io/Lectures/SGPT_final.pdf`.
2. `/Users/mingchen/Downloads/Mixed_volumes_of_partial_Okounkov_bodies/main.tex`,
   41,905 bytes, SHA-256
   `5746eb011417caecfa876c05c6c74fb548e2ae9d086c1441189bbcad02a96594`.
   This file was inspected read-only and was not modified.

The PDF was checked twice: first by layout-preserving text extraction, then
by direct visual inspection of the rendered source pages.  Printed page
numbers below are the page numbers shown in the book; physical PDF page
numbers include the front matter.

## Locator-by-locator findings

| Ch55 use | Primary-source finding | Author-source cross-check | Verdict |
|---|---|---|---|
| General-valuation Minkowski inclusion at live line 730; repeated in the provenance paragraph at line 1612 | Proposition 10.3.10, printed p. 340 (physical PDF p. 356), states that for another Hermitian big line bundle \((L',h')\), \(\Delta_\nu(L,h)+\Delta_\nu(L',h')\subseteq\Delta_\nu(L\otimes L',h\otimes h')\).  This is precisely the inclusion used in Ch55, in the book's fixed arbitrary rank-\(n\) valuation convention. | `main.tex` lines 181--184 records the same inclusion and cites Propositions 10.3.8 and 10.3.10; the latter is the Minkowski input. | **Correct: Proposition 10.3.10.** |
| Normalized finite-level Hausdorff convergence at live line 889 | Proposition 10.3.4, printed p. 335 (physical PDF p. 351), states \(\Delta_{k,T}(L)\to\Delta_\nu(L)\) in Hausdorff distance for every holomorphic twist \(T\).  Taking the untwisted case and then a divisible subsequence is exactly the Ch55 use. | `main.tex` lines 591--595 cites Proposition 10.3.4 for \(k^{-1}P_{i,k}=\Delta_{\nu,k}(D_i)\to\Delta_\nu(D_i)\), explicitly noting validity along \(k\in p\mathbf Z_{>0}\). | **Correct: Proposition 10.3.4.** |
| Closure of the \(P\)-preorder at live line 920 | Proposition 6.2.5, printed p. 225 (physical PDF p. 241), states that if two nets converge in \(d_S\) and \(\varphi_i\preceq_P\psi_i\) for every index, then \(\varphi\preceq_P\psi\).  Applying it to a constant sequence and a convergent tail is exactly the Ch55 argument. | `main.tex` lines 229--235 makes the same constant-sequence/tail application and cites Proposition 6.2.5. | **Correct: Proposition 6.2.5.** |
| Log-resolution translation formula at live line 1086 | Remark 10.3.1, equation (10.22), printed p. 338 (physical PDF p. 354), displays \(\Delta_\nu(\theta,\varphi)=\Delta_\nu(\pi^*L-D)+\nu(D)\) after resolving analytic singularities.  This is exactly the formula used in Ch55 after naming the residual rational line bundle \(A_i\). | `main.tex` lines 779--782 cites Remark 10.3.1, equation (10.22), and writes the same translated-body identity. | **Correct: Remark 10.3.1, equation (10.22).** |

## Rejection of the false-positive replacements

The locator substitutions introduced in response to the earlier whole-Ch55
Rethlas criticism do not match this identified source snapshot:

| False replacement | Controlling locator |
|---|---|
| Proposition 10.2.10 for Minkowski inclusion | Proposition 10.3.10 |
| Theorem 10.2.4 for finite-level Hausdorff convergence | Proposition 10.3.4 |
| Proposition 6.2.4 for closure of the \(P\)-preorder | Proposition 6.2.5 |
| Remark 10.2.1, equation (10.14), for the log-resolution formula | Remark 10.3.1, equation (10.22) |

The report's criticism is therefore not a mathematical defect in Ch55 and
must not be used as a verification finding for the 18 July 2026 XiaBook
snapshot.  The cause of the report's mismatch cannot be determined from the
report alone; no claim about its internal source or edition is needed for
this conclusion.  Direct inspection of the controlling PDF is decisive.

## Repeated false positives in the corrected-locator metric run

The later response read from
`/private/tmp/rethlas_ch55_xia_metric_corrected_20260824.json` has SHA-256
`b0e341e905aeba72397e773e8d1e9d8df356f2171d7153e27cf244c419d293dc`.
Its raw JSON payload is archived as
`ch55_xia8_8_metric_corrected_locator_false_positive_diagnostic_20260824.json`;
the archive has SHA-256
`31797c82f96f8e06fdd0491736286a26725a2f8fcd6e00a2773a6f2a22d16e9c`
and differs from the 3,686-byte source only by one terminal LF.
It was generated from the already corrected Xia full-context proof digest
`19de77caf613e0ab0f7592f814f07d48befcdb67906a7cde3fbd931e844e2192`.
Nevertheless, it repeats two assertions already contradicted by the
controlling PDF:

1. It says Proposition 6.2.5 concerns continuity of the maximum and directs
   the proof to Proposition 6.2.4.  Printed page 225, visually inspected at
   physical PDF page 241, explicitly states in Proposition 6.2.5 that the
   \(P\)-preorder is closed under simultaneous \(d_S\)-limits.
2. It says the log-resolution formula is equation (10.21) and that equation
   (10.22) changes a smooth reference metric.  Printed page 338, visually
   inspected at physical PDF page 354, explicitly displays the translated
   partial-body formula as Remark 10.3.1, equation (10.22).

These are not close interpretive calls: both proposition/equation numbers
and both statements are printed together on the cited primary pages.  The
second run's two XiaBook findings are therefore repeated locator
hallucinations and must not reverse this audit's verdict.

The same response also complains that the former Schneider pinpoint did not
identify John's theorem.  That is a separate Schneider-source question, not
evidence against any XiaBook locator.  Independent second-edition evidence
now identifies John's theorem as Theorem 10.12.2, page 588, and Blaschke
selection as Theorem 1.8.7, page 63.  The live chapter uses those two exact
locators.  The separate audit is
`manuscript/editorial/ch55_sch14_locator_primary_source_audit_20260824.md`.

Finally, the run reports several internal results as unavailable from its
submitted context.  Those are dependency-coverage gaps rather than
counterexamples to the results: the live book contains the required
\(\mathcal I\)-order monotonicity, diagonal body-volume formula,
\(\mathcal I\)-projection, body invariance, and mass--volume identity.  A
new source-aware metric packet embeds exact live extracts of those premises
before the complete metric-only proof chain.  The line-bundle specialization
is deliberately outside that metric-only packet.

## Live-source and packet consequences

The corrected live chapter has 64,938 bytes and SHA-256
`b2134d6b59f7687f8f5f296023a7d80703122210909032856b965f12f61619ab`.
The four mathematical locators occur inside the contiguous Xia full-context
slice, so that extract must be regenerated.  The five shorter Xia theorem
extracts begin after the four mathematical uses and remain byte-identical.
The provenance repetition lies after all six Xia intervals.  All toric
zero-mass exact intervals start later still and are unaffected.

No Rethlas submission was made in this audit, and no file under Downloads
was changed.
