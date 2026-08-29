# Repair ledger: P17.1 closed-immersion finite-level reduction, revised2

Date: 29 August 2026

Status: **FROZEN QUARANTINED CANDIDATE; awaiting independent exact-byte audit;
not submitted to production; not a live-book input**.

No live chapter, bibliography, open-problem inventory, provenance ledger, or
verified-results ledger was edited.

## Exact revised2 bytes

~~~text
767661c5d31a08f7a04d25b9856e8317062be8ced974a76707a4f9a9cd20c999  p171_closed_immersion_reduction_statement_revised2_20260829.tex
ceb947c47a83ea3e7591fc1aa27c2cc9206ccb3359f39f15b3a7f6d9e7b6d208  p171_closed_immersion_reduction_proof_revised2_20260829.tex
642c42873b276372fd7b4bb3e905fed3e3a7c251cf226d80a3d3d786a116feca  p171_closed_immersion_reduction_compile_revised2_20260829.tex
48dd3b7f12db26be713935d39f9862a87692d5098482989d0ed4a62ffca77b6e  p171_closed_immersion_reduction_compile_revised2_20260829.pdf
804e427b6302d92919d7931a17a87455a85674cda07e6420ee686c80961cdc58  p171_chen_moriwaki_edition_map_frozen_revised2_20260829.md
~~~

These bytes are frozen.  Any byte change requires a new revision suffix,
rehash, compile, independent audit, and production request.

## Revised1 rejection retained as provenance

The independent revised1 audit returned FAIL with:

- critical mathematical errors: 0;
- source/numbering factual errors: 0;
- source-scope gaps: 1;
- hash, algebra, scope, compile, and layout defects: 0.

The sole gap was that revised1 cited Pille--Schneider Proposition 4.2 for the
expansion over every complete residue field, while the proposition is located
after the paper's explicit assumption that the field is non-Archimedean.
Revised1 remains immutable rejected provenance.  Its exact hashes were:

~~~text
1f8ff9e26779f422038cdc88c682ac5a7c0d0bcdad7b7f224a4944c069a0b252  statement revised1
f4f4f54daf31be6f7f3b9114817cf2377e990e7db5c701ced364ebfedb4e7669  proof revised1
caaaf8ba6088217344e789694dbe29635522dbd4855288eae43cbf1e79de2891  harness revised1
d48859f1f5bb15d057200276f3eadb76f1262d0fef11492943b58ab5bf9432ee  supporting map revised1
797822161533bde4e86f6d70cb9f868e77ecb7564b9980726f2e40ce30f52203  PDF revised1
~~~

## Exact repair from revised1

The revised2 statement is mathematically byte-identical to revised1; only its
first comment identifies the new revision.  In the proof, besides the matching
comment change, revised1 lines 76--78 were replaced by the all-field anchor:

> symmetry and multilinearity on continuous dpsh metrics over every complete
> valued field follow from Boucksom--Eriksson, Proposition 8.5, Definition 8.7,
> and the paragraph following Definition 8.7.

Boucksom--Eriksson Proposition 8.5 extends the symmetric multi-additive pairing
to continuous psh-regularizable metrics; Definition 8.7 introduces continuous
dpsh metrics; its following paragraph extends the operator to a symmetric
multilinear signed-measure-valued pairing on them.  This section is stated for a
complete valued field, and the paper later explicitly includes possibly
trivially valued non-Archimedean fields.  The existing citation to Theorem 8.16
and formula (8.9) remains the correct all-field Deligne change-of-metric anchor.

No other mathematical text changed.  In particular, revised2 retains:

- the exact Pille--Schneider source scope: integral Banach `A`, an
  `n`-dimensional projective `A`-scheme `X`, and the additional flatness of
  Question 4.9;
- no added reducedness, geometric reducedness, equidimensionality, or purity;
- the same graph/base-change/Segre closed-immersion proof;
- the same exact tropical maximum identity;
- the same `2^n` signed MA expansion and `2^{n+1}` individual Deligne weights;
- the same global finite index set after every complete-residue-field base
  change;
- the explicit denial of any relative-resultant construction, continuous
  metric assembly, solution of Question 4.9, or retirement of P17.1.

## Revised2 Chen--Moriwaki map

The 12-entry concordance and the v1 Proposition 3.9.7 firewall are unchanged
and independently passed 12/12 in the revised1 audit.  Only the final
input-summary paragraph was updated: revised2 identifies the all-field
multilinearity source as Boucksom--Eriksson Proposition 8.5, Definition 8.7,
and its following paragraph, and records Pille--Schneider Proposition 4.2 only
as the corresponding non-Archimedean statement.  The revised2 map hash is
listed with the frozen bytes above; the stale revised1 map must not be attached
to a revised2 verification request.

## Compile and visual check

The exact revised2 harness compiled with PDF LaTeX through `latexmk` in
nonstop mode with halt on error.  Its final log has zero warnings, undefined
references, undefined citations, overfull boxes, underfull boxes, multiply
defined labels, emergency stops, and fatal errors.  The output has three A4
pages and empty Author metadata.

All three pages were rendered at 120 dpi and inspected.  There is no clipping,
overlap, missing glyph, black box, or margin defect; both source citations and
the two-item reference list render correctly.

## Independent audit and production gate

An independent auditor must rehash all five frozen revised2 artifacts,
independently compile the exact harness, check that the diff from revised1 is
confined to the all-field source repair and revision headers, and return
PASS with zero critical errors and zero gaps.  It must in particular recheck
the scope of Boucksom--Eriksson Proposition 8.5, Definition 8.7 and its
following paragraph, and Theorem 8.16 (8.9).

Only after that independent PASS may the exact revised2 statement/proof pair be
submitted to the production gpt-5.6-sol/xhigh Rethlas service.  The request
must describe this as a finite-level reduction, not a proposed solution of
P17.1.  A production response is acceptable only if it is `final/correct`, its
proof digest matches the exact revised2 proof hash, and both critical-error and
gap arrays are empty.
