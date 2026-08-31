# Primary-source interface

The source was independently read in the supplied text and exact local PDF, and its public arXiv version was opened independently: [Boucksom–Favre–Jonsson, arXiv:1201.0187v2](https://arxiv.org/pdf/1201.0187v2).

Exact local files:

- /private/tmp/BFJ_singular_1201.0187_audit_20260831.pdf — 768011 bytes; SHA256 `8b684713055b9147de0d3379ad925c58f031bafe10a77e769a2791cdaa128270`.
- /private/tmp/BFJ_singular_1201.0187_audit_20260831.txt — 175006 bytes; SHA256 `df3fa71656240742234907514956389d2f2533e20bb89cd877bd235a922e5f1f`.

The PDF skill was read completely. Public-reader screenshots failed with a cache miss; this was not a permission rejection. The exact supplied local PDF was then rendered with Poppler and pages 6, 9, 15, 16, 23, 24, 25, 32, and 33 were inspected visually. No source PDF was modified. Scratch images are not output artifacts.

Source routing and scope, in under 200 words:

- §1.1, p6: complete DVR, normalized valuation, residue characteristic zero, without requiring algebraically closed residue field.
- §2.4, p9: smooth **connected** projective analytic space and normal projective models.
- Proposition 3.12 and the piecewise-affine part of Corollary 3.13, pp15–16: ideal/monomial formulas give the rational affine pieces used to exclude irrational breakpoints. Only that part is used here.
- Definition 5.1 discussion, p23: semipositivity is independent of determination and ampleness is open on a fixed model.
- Proposition 5.2, p23: a sufficiently high model carries a positive representative; its proof explicitly uses a real vertical divisor.
- Lemma 5.7, p24: rational psh model functions admit uniform relative-ideal approximation. This is the intended Ch21 input.
- Proposition 5.8, pp24–25: rational potentials are max-stable at a real form, via rational perturbation and ideal generation.
- §7 opening and Proposition 7.4, pp32–33: ample generic class; finite maxima in the full PSH class.

The new fixed-form rational-density proof is audited as an explicit argument, not falsely attributed as the literal statement of one of these source propositions. The source's real divisor in Proposition 5.2 is kept real until the repair's own ample-cone rounding step. The source statements do not themselves prove the manuscript's every other model-consistency or curve-retraction claim.

The Ch05 rational piecewise-affine interface was also read at prop:skeleton-model-pa. Its file is frozen in the audit manifest: 151486 bytes; SHA256 `76c47909486f66289199e54369ecb5ba0c8bc4018efa205f534d1e44e25d318d`. The irrational example is independently supported by the source monomial/ideal formulas, not by an assumption that arbitrary real breakpoints have algebraic realizations.

