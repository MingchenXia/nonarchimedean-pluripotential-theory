# Repair ledger: P17.1 closed-immersion finite-level reduction, revised3

Date: 29 August 2026

Status: **FROZEN QUARANTINED CANDIDATE; awaiting independent exact-byte audit;
not submitted to production; not a live-book input**.

No live chapter, bibliography, open-problem inventory, provenance ledger, or
verified-results ledger was edited.

## Exact revised3 bytes

~~~text
11b559989d5d79737c1b2e37e819ec4dc11fbc0baf704a1dd8f3c4427f6ee4ae  p171_closed_immersion_reduction_statement_revised3_20260829.tex
5c5b7561549f4feecadd5677dd54f14f98a02cecf76502e251fdb2ef9219697d  p171_closed_immersion_reduction_proof_revised3_20260829.tex
a36e2cf83a8cf89c1f4dfadcec2bf1d9521bdaa9639f91273c7c9d7b7c4e179f  p171_closed_immersion_reduction_compile_revised3_20260829.tex
0e6bf326b0f25de682d95e96189e4fdeb8b607219d8711faf7c483806276d6c1  p171_closed_immersion_reduction_compile_revised3_20260829.pdf
9409c9cfb44f9195d47b67ced32ffeaf50fd7c1902b96422de0e665616a77a5b  p171_chen_moriwaki_edition_map_frozen_revised3_20260829.md
~~~

These bytes are frozen.  Any byte change requires a new revision suffix,
rehash, compile, independent audit, and production request.

## Rejected revisions retained as provenance

Revised1 was rejected because Pille--Schneider Proposition 4.2 lies in the
paper's non-Archimedean subsection and therefore did not by itself support an
all-complete-field assertion.

Revised2 replaced that source by the mathematically correct
Boucksom--Eriksson extension, but its locator said “the paragraph following
Definition 8.7.”  In the frozen source, Definition 8.7 is followed by Lemma 8.8
and Examples 8.9--8.10; the symmetric multilinear extension paragraph occurs
immediately after Example 8.10.  Revised2 is therefore rejected for one exact
source-locator gap, not a mathematical error.  Its hashes remain:

~~~text
767661c5d31a08f7a04d25b9856e8317062be8ced974a76707a4f9a9cd20c999  statement revised2
ceb947c47a83ea3e7591fc1aa27c2cc9206ccb3359f39f15b3a7f6d9e7b6d208  proof revised2
642c42873b276372fd7b4bb3e905fed3e3a7c251cf226d80a3d3d786a116feca  harness revised2
48dd3b7f12db26be713935d39f9862a87692d5098482989d0ed4a62ffca77b6e  PDF revised2
804e427b6302d92919d7931a17a87455a85674cda07e6420ee686c80961cdc58  map revised2
9b465f64d40696a1b2824b47d83111cabd08a55d49928901ea5981252be4f475  ledger revised2
~~~

## Exact repair from revised2

The revised3 statement is mathematically byte-identical to revised2; only its
first comment identifies the new revision.  In the proof and supporting map,
the words

> paragraph following Definition 8.7

were replaced by

> paragraph following Example 8.10.

Together with Proposition 8.5 and Definition 8.7, that is the exact printed
all-field anchor.  Proposition 8.5 extends the symmetric multi-additive pairing
to continuous psh-regularizable metrics; Definition 8.7 defines continuous
dpsh metrics; and the paragraph after Example 8.10 extends the operator to a
symmetric multilinear signed-measure-valued pairing on continuous dpsh
metrics.  The same Section 8 treats an arbitrary complete valued field; its
non-Archimedean specializations explicitly allow trivial valuation.  The
existing citation to Boucksom--Eriksson Theorem 8.16 and formula (8.9) remains
the exact Deligne change-of-metric anchor.

No other mathematical text changed.  Revised3 retains the exact
Pille--Schneider source hypotheses, does not add purity or reducedness, and
asserts only the finite signed closed-immersion expansion.  It does not
construct relative Chow/resultant data, prove continuity, solve Question 4.9,
or retire P17.1.

## Chen--Moriwaki map

The 12-entry two-edition concordance and the v1 Proposition 3.9.7 firewall are
unchanged and previously passed 12/12 independent checking.  The only revised3
change is the exact Boucksom--Eriksson locator in the final input-summary
paragraph.  The stale revised1/revised2 map hashes must not be attached to a
revised3 verification request.

## Compile and visual check

The exact revised3 harness compiled with PDF LaTeX through `latexmk` in
nonstop mode with halt on error.  Its final log has zero warnings, undefined
references, undefined citations, overfull boxes, underfull boxes, multiply
defined labels, emergency stops, and fatal errors.  The output has three A4
pages and empty Author metadata.  The layout is the same three-page layout
already inspected for revised2 apart from the corrected locator text; no
clipping or margin defect is introduced.

## Independent audit and production gate

An independent auditor must rehash all five frozen revised3 artifacts,
independently compile the exact harness, check that the diff from revised2 is
confined to revision headers and the exact Example 8.10 locator, and return
PASS with zero critical errors and zero gaps.  It must recheck
Boucksom--Eriksson Proposition 8.5, Definition 8.7, the paragraph following
Example 8.10, and Theorem 8.16 (8.9).

Only after that independent PASS may the exact revised3 statement/proof pair be
submitted to the production gpt-5.6-sol/xhigh Rethlas service.  The request
must describe this as a finite-level reduction, not a proposed solution of
P17.1.  A production response is acceptable only if it is `final/correct`, its
proof digest matches the exact revised3 proof hash, and both critical-error and
gap arrays are empty.
