# Siu dependencies in the Cartier and numerical b-divisor criteria

Date: 4 October 2026. Baseline: `5d1b995`.
This is a source and dependency correction following the author's warning
about BJ22 Theorem 6.21. The critical division assertion on arbitrary
normal varieties remains unresolved. No new division proof, theorem
counterexample, open-problem solution or production-model receipt is claimed.

## The two dependencies and the retained smooth regime

BJ22 Theorem 6.35's inverse Cartier criterion removes an effective divisor
using Theorem 6.21. Ample-class envelopes alone are the hypothesis printed
in the original statement; its given proof additionally needs that division
step. Chapter 35 now displays critical division on the particular normal
variety `X` as an assumption, alongside ample-class envelopes. Its forward
implication and semiample criterion remain independent of both inputs.
The early dependency paragraph, semiample/nef warning and chapter dictionary
now record the same boundary as the theorem and its proof.

In the smooth characteristic-zero subsection, the required instance on `X`
has an independent source: Proposition 17 of BJGreen24, using the all-class
envelope property proved by Theorem A of the 2024 BJ22 addendum. The cited
division instance concerns effective rational Cartier divisors. It is not
an assertion of `(SD)_k` for every normal variety over the same field.

The numerical-correspondence proof formerly cited BJ22 Corollary 6.22 for
homogeneous compactness. That corollary's proof itself invokes Theorem 6.21.
The updated proof instead uses independent all-class envelopes and BJ22
Theorem 5.11(ii), the normalized compactness equivalence. This matters
because the buffered class `theta+omega` need not be ample. Homogeneous
functions are normalized; their closedness follows from divisorial
homogeneity under rational scaling, determination, and orbit monotonicity
to extend to positive real scaling. Irrational rescalings are not silently
treated as divisorial tests. Thus the established smooth
characteristic-zero correspondence and its monotone approximation retain
their scope, without assuming division on all normal varieties.
Appendix F's separately imported Dang--Favre intersection construction
is unchanged.

## Exact primary-source scope

The cached published BJ22 text was freshly read at lines 4260--4415 and
4548--4848, including the full Cartier-criterion and numerical-correspondence
proofs and their compactness/division references. Seven selected actual
pages, 95--101 (printed 740--746), were viewed in four contact sheets.
The actual page 99 displays the critical-division invocation; page 101
displays the Corollary 6.22 invocation. The section/Cartier dictionary
antecedents are visible in the adjoining pages. This is a targeted source
check, not a new whole-paper audit.

BJGreen24's standing scope and complete Proposition 17 proof were reread
at lines 575--715. The addendum's introduction was reread at lines 1--85;
its independent Theorem A proof and consequences retain the earlier
source audit. The previous same-byte actual views of Green page 13 and
addendum pages 10--11 are explicitly reused. The companion manifest pins
these PDFs, extracted text and dated actual-view receipts. No fresh
verification of every cited antecedent is inferred.

## Verification and artifacts

The final full build, source preservation, reference/inventory checks,
navigation and scoped actual-page review are recorded in the companion
manifest. Historical Siu, cyclic-model and literature checkpoints retain
their original sources, checks and dated artifacts. The 86-page standalone
catalogue and all 42 active problem statuses are unchanged.

Only the Chapter 35 TeX input changes. The source comparison distinguishes
the explicit hypothesis correction and the two modified proofs from
unchanged formal environments; the fixed strict-division statement and
proof are preserved byte for byte. There are no new formal environments
or labels. The surrounding source commentary and dictionary are corrected
to match the displayed assumptions.

The final PDF has 4,253 pages. The active closure contains 425 TeX inputs
and 12,591 unique labels; 424 inputs and all 108 protected Appendix M--N
inputs are byte unchanged. Chapter 35 has 111 formal environments, of
which 108 are unchanged and three are modified (the conditional criterion
and the two affected proofs). The full build has no TeX errors, unresolved
references or citations, package warnings, overfull boxes or rerun requests;
954 underfull boxes remain. The index and bibliography have no rejected
entries or warnings, and the internal navigation checks pass. The source
checker and the independent open-problem inventory check both pass.

Fifty selected final physical pages were actually viewed in 13 contact
sheets: the scoped contents, affected Chapter 35 passages and seams,
retained strict-division warning, and complete index and references. No
layout defect was found on those pages. This is not a fresh visual review
of all 4,253 pages. After the final wording clarification, four changed
pages were freshly viewed and 46 same-byte actual views were explicitly
reused from the preceding full scoped review. The seven newly viewed BJ22 source pages and the
explicitly reused Green/addendum views have separate dated receipts.
The [manifest](bj22_siu_bdivisor_followup_manifest_20261004.json),
[source ledger](bj22_siu_bdivisor_followup_source_closure_20261004.sha256)
and [artifact record](bj22_siu_bdivisor_followup_artifacts_20261004.json)
pin the scope and bytes of this checkpoint. The source archive is checked
against the current workspace; it is not independently compiled from the
archive, and font portability is not claimed.

The first shell build lacked the already installed newtx package search
path, and a subsequent attempt used the system font map. The successful
build restores `TEXMFHOME=/workspace/.texlive`,
`TEXMFVAR=/workspace/.texlive/texmf-var` and the configured local TeX
configuration. No new installation or manuscript font substitution was
needed. Actual-page review of an intermediate build found the dictionary's
remaining omission; it was corrected before the final review.
