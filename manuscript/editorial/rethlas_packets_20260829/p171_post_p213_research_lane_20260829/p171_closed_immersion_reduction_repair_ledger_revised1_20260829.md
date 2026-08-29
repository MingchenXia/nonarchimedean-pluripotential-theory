# Repair ledger: P17.1 closed-immersion finite-level reduction, revised1

Date: 29 August 2026

Status: **FROZEN QUARANTINED CANDIDATE; awaiting independent exact-byte audit;
not yet eligible for production Rethlas; not a live-book input**.

No live chapter, bibliography, open-problem inventory, provenance ledger, or
verified-results ledger was edited.  The original rejected candidate files were
not changed.

## Exact revised1 bytes

~~~text
1f8ff9e26779f422038cdc88c682ac5a7c0d0bcdad7b7f224a4944c069a0b252  p171_closed_immersion_reduction_statement_revised1_20260829.tex
f4f4f54daf31be6f7f3b9114817cf2377e990e7db5c701ced364ebfedb4e7669  p171_closed_immersion_reduction_proof_revised1_20260829.tex
caaaf8ba6088217344e789694dbe29635522dbd4855288eae43cbf1e79de2891  p171_closed_immersion_reduction_compile_revised1_20260829.tex
797822161533bde4e86f6d70cb9f868e77ecb7564b9980726f2e40ce30f52203  p171_closed_immersion_reduction_compile_revised1_20260829.pdf
d48859f1f5bb15d057200276f3eadb76f1262d0fef11492943b58ab5bf9432ee  p171_chen_moriwaki_edition_map_frozen_20260829.md
~~~

These bytes are frozen for the next independent audit.  Any byte change to the
statement or proof requires a new suffix, new hashes, a new compile, and a new
audit before production submission.

## Superseded bytes retained for provenance

~~~text
3ad32111cfa564815c91dfa9aad30070495611b9f59bb677e2d0050820e38dfb  p171_closed_immersion_reduction_statement_20260829.tex
f43c83f12b738b60f26e534989552805d812126bfb3b4a9fdfc177eb9b020e13  p171_closed_immersion_reduction_proof_20260829.tex
~~~

The independent hostile audit of those superseded bytes is
`p171_closed_immersion_reduction_independent_hostile_audit_20260829.md`,
SHA-256
`e2afd69f5f1d12d8ab5953d029eb21950eea95250766e25306b7303302af4877`.

## Repairs made and nothing more

### R1. Restored the exact Pille--Schneider source hypotheses

Revised statement lines 49--54 now say:

- `A` is an integral Banach ring;
- `X/A` is an `n`-dimensional projective scheme;
- in addition, `X` is flat over `A`.

This follows the exact wording split between Pille--Schneider, Definition 4.8,
and Question 4.9.  No reducedness, geometric reducedness, equidimensionality,
or purity hypothesis was silently added: the source says `n`-dimensional and
the fieldwise construction uses the top-dimensional fundamental cycle.  The
repair does not reinterpret `n` as merely the number of supplied line bundles.

### R2. Added the exact definitions and multilinearity anchors

Revised proof lines 59--61 cite Pille--Schneider, Definition 2.15, for the DFS
presentation.  Revised proof lines 76--78 cite Pille--Schneider, Proposition
4.2, for symmetry and multilinearity of the fieldwise Monge--Ampere pairing on
DFS metrics.

### R3. Added the exact Deligne change-of-metric anchor and applicability check

Revised proof lines 87--93 state that the metrics in each expanded summand are
continuous dpsh metrics and cite Boucksom--Eriksson, Theorem 8.16 and formula
(8.9).  That is the direct fieldwise result identifying the difference of two
Deligne-metric weights with the integral of the metric difference.  The
self-contained harness contains the two bibliography entries, using the same
keys as the monograph bibliography: `PS23Hybrid` and `BE21`.

### R4. Froze the Chen--Moriwaki edition map

The separate source map with hash recorded above gives a two-column
concordance.  In particular:

- CM-v1 uses Definition 1.6.3, Example 1.6.4, Definition 1.6.7, Remark
  1.6.8, Theorem 3.8.7, and Proposition 3.9.3;
- CM-later uses Definition 1.6.4, Example 1.6.5, Definition 1.6.9, Remark
  1.6.10, Theorem 3.9.7, and Proposition 3.10.3;
- CM-v1 Proposition 3.9.7 is only the special regular-curve comparison and
  cannot be cited as the broad formula.

The map also records that Chen--Moriwaki is a downstream resultant/metric
comparison source, not an input to this finite reduction.

### R5. Preserved the strict scope firewall

No theorem conclusion was strengthened.  The revised statement still asserts
only a finite signed expansion, with a global finite index set and
closed-immersion defining systems after every complete-residue-field base
change.  Its remark still explicitly denies:

- construction of a relative resultant over an arbitrary Banach base;
- identification with every fundamental-cycle fibre resultant;
- continuous assembly of fieldwise Chow/Deligne norms;
- a solution of Pille--Schneider Question 4.9 or P17.1.

Thus no open-problem atom can be retired on the strength of this packet.

## Primary sources rechecked

~~~text
68d1bf470a78d4021e126ec1d491ad002cb64a1689d06beec3dd3fc9f9dee71e  /private/tmp/PS23Hybrid.pdf
51d02f75a65aa463f8e22393933f5ebef9036e322d720fc632f87759c2b71cb2  /private/tmp/BE_1805.01016.pdf
89828d2fe257736d0a51d8152d47b29ba0da207b61f6e04137fd9f28f89d5b1f  /private/tmp/ChenMoriwaki2103.15646.pdf
4978bf5a6b0b09dbb43a273fe0eba1e2368ce60b9f78730e567f59d605be0b44  /private/tmp/ChenMoriwakiIntersectionAccepted.pdf
~~~

The exact checked anchors are Pille--Schneider Definitions 2.13, 2.15, and
4.8, Proposition 4.2, and Question 4.9; Boucksom--Eriksson Proposition 8.5
and Theorem 8.16, especially formula (8.9); and every item in the frozen
Chen--Moriwaki concordance.

## Compile and visual audit

The revised1 harness was compiled with PDF LaTeX through `latexmk` in nonstop
mode with halt on error.  The final log contains zero warnings, undefined
references, undefined citations, overfull boxes, underfull boxes, multiply
defined labels, emergency stops, and fatal errors.  The result has three A4
pages and empty Author metadata.

All three pages were rendered at 120 dpi and inspected.  There is no clipping,
overlap, missing glyph, black box, or margin defect.  The citations render as
links and the reference list contains exactly the two cited works.

## Independent-audit checklist

Before production submission, an agent independent of this repair should:

1. rehash the exact revised1 statement, proof, harness, source map, and PDF;
2. diff revised1 against the superseded theorem bytes and verify that the only
   mathematical change is the restored source scope plus citation/applicability
   text;
3. recheck the graph/base-change/Segre proof and the exact max identity;
4. check Definition 2.15 for the fixed isomorphism in the DFS presentation;
5. check Proposition 4.2 for the `2^n` signed expansion;
6. check Boucksom--Eriksson Theorem 8.16 and (8.9), including trivially valued
   fields, continuous dpsh hypotheses, and top-cycle generic multiplicities;
7. check that global sections and closed immersions base-change uniformly but
   that no relative continuity is inferred;
8. check every entry of the two-edition Chen--Moriwaki map;
9. compile the exact harness independently and inspect all three rendered
   pages;
10. return a fail-closed PASS/FAIL report with critical-error and gap counts.

Only after an independent PASS should the exact statement/proof pair above be
submitted together to the production gpt-5.6-sol/xhigh Rethlas service.  The
request must describe the theorem as a finite-level reduction and must not ask
the verifier to decide P17.1 itself.  A production result is acceptable only if
it is `final/correct`, the proof digest matches the exact proof hash above, and
both critical-error and gap arrays are empty.
