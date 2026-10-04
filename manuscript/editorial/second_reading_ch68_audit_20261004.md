# Chapter 68 renewed second-reading audit

Date: 4 October 2026. Baseline: `d7434ff972287fb9a1ff3fca23f2a9a111f62e8f`.

The complete 1,042-line source `parts/part6/ch68_ytd_bridge.tex` was freshly
read in four consecutive ranges. There are no direct inputs. The source
remains byte-identical; this checkpoint records a renewed mathematical,
source and visual review without unnecessary source changes. It closes only
Chapter 68 in the ordered whole-book rereading.

## Mathematical and expository review

The book retains its explicit literature cutoff of 22 August 2026. Reading
cached sources again on 4 October does not silently move that cutoff or
turn announcements into dependency-audited theorems.

- The analytic package uses raw mass V in mixed products and probability
  measures in entropy. The analytic entropy is half the ordinary relative
  entropy. With squared potentials, E and J double the norm-weight values,
  whereas H, Ricci energy and Mabuchi values do not. The Chen–Tian formula
  is H + Sbar E/2 + R, and R translates by -Sbar c/2. The BDL operator
  convention is converted using u=phi/(2 pi), with its K-energy equal to
  twice the book's M for the same curvature form. First variation against
  all smooth zero-mean variations gives the cscK characterization; extended
  convexity and finite-energy regularity remain precise source imports.
- Normalized polarization powers cancel in DF. Normalized ramified base
  change instead scales M and J, while DF needs the central-fibre correction
  C=V^{-1} sum(1-b_E)(E.L^n). The logarithmic canonical pullback gives
  DF(phi_d)=d DF(phi)+d C(phi)-C(phi_d). Reduced central fibre requires a
  sufficiently divisible degree. The valuation function scales by
  D_d phi(v)=d phi(v/d), rather than pointwise multiplication by d.
- The canonical weak test-configuration E/J slopes use denominator 2s.
  All smooth-ray slope statements imported from BHJ retain their positivity
  assumptions and norm/squared conversion. The weak-ray Mabuchi inequality
  is an assembly result with finite E/R limits and a separate entropy-slope
  inequality explicitly assumed. Ordinary weak-measure entropy lower
  semicontinuity alone does not identify the radial entropy slope with HNA.
- The complete BHJ erratum keeps Sections 1–4, Theorem A and Corollary B
  available while quarantining 5.6, 5.4, C and D–E. No Bergman-level statement
  is silently promoted to full finite-energy coercivity.
- The Fano beta integral stops at the pseudoeffective threshold through
  vanishing volume. The j-integral explicitly ends at that threshold; its
  integrand would stay V afterwards. The projective-line computation gives
  beta=0 and j=2 and lies outside the finite-automorphism scope.
- The normalized model/valuative criterion tests all finite weighted sums of
  divisorial Dirac masses, keeps the measure fixed in the class derivative,
  and uses reduced discrepancy entropy. Testing individual divisors alone
  is a different condition. Chapter 62's repaired normalized model criterion
  is used separately from the implication starting with all raw big models;
  the literal broader equivalence printed in MPWN is not substituted for it.
- The elementary coercivity/minimizer proposition states compactness, lower
  semicontinuity and smoothness assumptions separately. Continuous
  automorphisms require a reduced norm and relative functional. Ordinary
  J-coercivity is not asserted along every automorphism orbit.
- The finite-automorphism Fano equivalence uses the unaffected smooth Ding
  slope and semipositive-model approximation for the forward direction.
  Uniform convergence makes the infimum defining LNA Lipschitz. The converse
  uses BBJ's finite-energy ray compactness, LNA convergence and only the
  inequality ENA(phi_m)>=c. With c<0 and 0<epsilon<1, the resulting
  c>=(1-epsilon)c is impossible. No unjustified equality of energy slopes
  for arbitrary rays is used. Existence, regularity and ordinary uniqueness
  remain separately named variational inputs.
- The 2025 cscK implication begins with stability for every big model and
  passes through normalized models and completed finite-energy coercivity.
  Entropy-preserving approximation of measures and the non-Archimedean
  Calabi–Yau homeomorphism do the completion work. The independent MP
  existence theorem is invoked in unrelative coercive scope. Ordinary ample
  tests are not asserted to imply all-big stability in this theorem.
- BJ26 v2 is dated orientation. Trusiani v2's projective relative YTD,
  entropy regularization and maximal-ray entropy-slope claims are reported
  with their version and dependency boundary. Weighted existence keeps the
  log-concavity hypothesis. These announcements do not prove an arbitrary
  nonprojective compact-Kaehler statement or identify every prescribed
  approximation sequence term by term.
- In the product example, the squared Fubini–Study orbit has E=0,
  J=2s coth(2s)-1, half entropy H=J and Ricci energy R=-J, so M=0.
  Full ordinary entropy would destroy this cancellation. In the nonreduced
  quotient example, the stabilizers allow descent of O(m), the generic
  central action is free, X0=mG, G.L=1 and V=m. The degree-m normalization
  gives J=m/2 and M=0 upstairs; downstairs J=1/2, M=0 and DF=(m-1)/m.
  Thus DF upstairs is zero while m DF downstairs is m-1, exactly illustrating
  the correction rather than contradicting Mabuchi homogeneity.

No new mathematical or layout defect was identified. The source checks
preserve all 75 labels, 42 formal environments and their order, all 42
formal bodies byte for byte, and 32 labelled tagged displays. There are no
legacy inline delimiters, double-dollar displays, placeholders, unlabelled
numbered objects or direct inputs.

## Scoped primary evidence

Nine pinned cached PDFs and 65 selected physical pages were freshly read in
text. All twenty primary contact sheets were actually viewed. The manifest
stores full SHA-256 pins, page lists, text hashes and precise import
boundaries. There was no new source acquisition or exhaustive literature
search in this checkpoint.

| Source | Selected physical pages | Evidence boundary |
| --- | --- | --- |
| BDL, published G&T 21 (2017), 2945–2988 | 1–5, 18–19 | Operator, Chen–Tian formula, Theorem 1.2 statement and full printed Lemma 3.1 proof; Theorem 3.2 starts here but continues outside the selection; full 4.7 convexity proof is not selected. |
| BHJ17, published AIF 67 (2017) | 1, 59, 65–67, 70–72 | Scaling, E/J and full printed 7.14–7.22 interfaces. Earlier intersection/log-canonical pullback and semistable reduction remain imports. |
| BHJ19, published JEMS 21 (2019) | 1, 5–9, 18–22, 26–28 | Half entropy and Deligne normalization; full printed 3.6 and 3.9–3.11 arguments; 4.2 and its printed proof. Ding 4.3 imports Berman; 4.5 read. |
| BHJ erratum, JEMS 24 (2022), 735–736 | 1–2 | Entire note, counterexample and affected/unaffected dependency list. |
| BBJ, arXiv:1509.04561v3, side 8 September 2020 | 1–2, 12, 15–16, 20–23 | Selected complete 2.19/2.20, 4.6, 5.4–5.8 and 5.1 printed arguments; 2.8 and earlier/Appendix B/uniqueness/MMP results remain imports. Cover date is 9 September. |
| MPWN, arXiv:2509.09442v1, 11 September 2025 | 1–3, 13, 32–37 | Raw definitions, reduced entropy, printed 9.1/9.2 arguments and 10.0 interfaces; prior Calabi–Yau and class derivatives remain imports. Printed normalization slips and overly broad raw-model equivalence are not adopted. |
| MP, arXiv:2409.06221v2, 18 September 2025 | 1, 3–4, 51–53 | Theorem A and printed Section 6 argument; Li maximality, preceding mixed slopes and Chen–Cheng remain imports. |
| BJ26, arXiv:2602.10800v2, side 19 May 2026 | 1–3 | Introduction and announcement only; cover 20 May. No newly audited full bridge proof. |
| Trusiani, arXiv:2605.30063v2, 17 August 2026 | 1–6 | Introduction, A/B/C, Corollaries A/B and entropy-slope/appendix announcements. No full Fujita proof or dependency closure claimed. |

The correctly identified BDL published PDF is used. The cached unrelated
`Araujo_Casagrande_2017_unused.pdf` supplies no mathematical evidence.
Historical Chapter 68 calculations (11,733 exact and 58 numerical checks
in 25 families) were not rerun and are not fresh evidence or a new
independent-verifier verdict. Frozen receipts and historical audits remain
unchanged.

## Build and actual visual review

The unchanged source reuses the successful Chapter 60 fourth-stage full
validation. Current book PDF: 4,236 pages, 19,733,185 bytes; SHA-256
`c06b9b2487f7c2f82a4fc8d19fa02eae760368547d3e23cbdbcf24b3f680bc8d`.
The current log has zero TeX errors, package warnings, overfull boxes,
unresolved references/citations or rerun requests; 953 bookwide underfull
boxes remain. All six checker regressions passed in that full validation;
no redundant build or regression rerun is claimed here.

All sixteen chapter physical pages 3531–3546 and seams 3530/3547 were
actually viewed in five contacts. The terminal physical page 3546 is an
intentional blank. Formulas and diagrams fit, theorem proofs retain natural
page breaks and source notes finish normally. Review export:
`/workspace/book-completion-drafts/second-reading/Ch68_Review_2026-10-04.pdf`.
Fresh post-render reference checks pass for 425 inputs and 12,569 labels.
Fresh inventory checks preserve 42 active atoms in twelve families, tiers
(0,3,7,15,17). No open-problem status changes.

A fresh main fetch found no incoming commits. Publication continues through
normal work-branch pushes and the existing draft PR. Chapter 69's complete
1,790-line source and historical quality audit have now been freshly read;
its scoped checks are next. Later chapters and appendices are not marked
complete by this checkpoint. Related-direction and recent-arXiv integration
continues after the whole-book polishing pass.
