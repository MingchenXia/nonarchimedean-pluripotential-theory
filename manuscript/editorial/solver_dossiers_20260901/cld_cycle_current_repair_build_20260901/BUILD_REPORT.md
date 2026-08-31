# Chapter 14 cycle-current corrections and whole-book build

Date: 1 September 2026.
Source comparison base: db8918d5a533c5a29336d97f70b500540dd9484f.

## Scope and mathematical review

This build makes six content corrections, followed by one display-layout correction, in Chapter 14. It does not promote a new research theorem or retire a Chapter 72 problem.

The Tate-curve example now distinguishes the pushforward of skeleton length measure, a current acting on functions, from the integration current of the analytic curve, which acts on top-degree forms. Explicit Gauss norms describe the skeleton and an annulus in an off-skeleton open disc supplies a nonzero test form disjoint from it. The two summary tables use the same corrected terminology.

The projective-line example distinguishes finite analytic zero-cycles from arbitrary Dirac currents and from the fundamental integration current. An explicit tropical branch with a compactly supported test form explains why a one-point model skeleton does not determine the integration functional.

The fundamental-cycle theorem retains its statement. Its proof now keeps the nonreduced components and uses CLD's reduction calibration factor, including the reciprocal generic Artinian length, before applying the integration formula. It no longer discards the generic nonreduced structure.

The fibre-integral warning now gives the explicit square-zero thickening of a nonempty smooth space. The reduction map has reduced point fibres but is nowhere flat, and the factor of two in the fundamental current explains exactly why the proposed fibre identity fails. This is an explanation of the counterexample already indicated in CLD 16.5.6, not a newly solved conjecture.

Root checked the actual primary CLD text, the complete candidate changes and the complete audit reports. Separate audit packets preserve the cycle-source corrections, the Tate-measure correction and the exact final integration check. The reviewer independently checked root's added thickening argument; root checked the reviewer's drafted corrections. This division of labour is recorded rather than describing an author's self-check as an independent review.

The exact final audit addendum has SHA256 c269b07471a3fd17b1ecfcc0a7eeccbbd291fdf2b993dcbe16dedad9d27cc8f4. Its checker reconstructed the final source from the recorded parent inputs and passed. The final Chapter 14 source is 165265 bytes, SHA256 0ffe13c44ced54ed77d6bfb1e16679cc5682368d1ca6207c2d7d1fc0f4480870. All 102 label definitions and 22 existing eqref calls are preserved in order. New internal references use cref/Cref. The Chapter 72 source, atomic inventory and book.tex are unchanged from the comparison base; author and acknowledgements remain blank.

## Build history and final result

The first complete build, in /private/tmp/nappt_cld_cycle_repair_20260901_ATOrHB, completed successfully but exposed an 18.87pt overfull inline formula. The interval test-function condition was moved to an unnumbered display. Two intermediate source snapshots, ending UcmAWt and PiU366, were retained but not compiled. The final snapshot also includes the explicitly nonempty smooth-space hypothesis in the thickening example.

The final exclusive 216-file build is /private/tmp/nappt_cld_cycle_repair_20260901_4TqAnG. The latexmk command with pdf, nonstopmode and halt-on-error completed with exit code zero. Both the live inputs and build-tree inputs are checked against the complete source snapshot before publication.

The final PDF has 3478 pages and 16618597 bytes, with SHA256 4061c4de8e6af169dea215831e7405cf7a4ef7d637c09928a3b7d964c7c35dfb. The author metadata is empty. The title is unchanged and has no subtitle.

There are no TeX errors, undefined references or citations, multiply defined labels, missing characters, overfull boxes or BibTeX warnings/errors. The 1018 underfull notices and existing svmono class-name notice remain. This does not certify the entire book's mathematical correctness or claim a warning-free build.

Following the PDF skill, root rendered and visually read all fourteen final physical pages 633-639, 641-643 and 652-655, corresponding to printed pages 565-571, 573-575 and 584-587. The review covers every changed passage and the adjacent transitions. No clipped text, overlapping equations, unreadable formulas or broken references were found in this scoped check. The final QA record pins the inspected image bytes.

## Recoverable publication

The finalizer validates all source, PDF, log and rendering identities before replacing the stable current PDF. It first preserves the former 3476-page current PDF, SHA256 dd0aba9532b258b83af57a84c42d6209f1f9c90f9ba9511e3e2cca442530fc00, as a separately named backup ending before_cycle_current_repair_20260901.pdf.

The output remains output/pdf/Non-Archimedean_Pluripotential_Theory_current.pdf. The older release and manuscript/book.pdf are untouched. Generated PDFs, temporary build trees and reference copies remain outside Git; the source snapshot and QA records are versioned.

Production Rethlas work on the separate component-curvature and full-CPsh research packets is tracked separately. Its status is not evidence for these known-source corrections, and these corrections are not evidence that the wider P21.3 research problem is solved.

