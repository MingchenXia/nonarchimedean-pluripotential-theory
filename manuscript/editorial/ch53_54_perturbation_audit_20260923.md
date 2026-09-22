# Chapters 53--54: order reflection and positive mass under perturbation

Audit date: 23 September 2026.

## Mathematical repair

The proof that the order can be checked at one Kähler perturbation
previously used only monotonicity of the transition. That proves one
direction and does not recover order in the smaller background.
Lemma 53.1.2 now proves order reflection and injectivity: the I-envelope
preserves multiplier ideals, and the I-preorder is independent of the
background. Its candidate characterization recovers pointwise order
between normalized I-model representatives in either background.
For two unrelated perturbations, descend to a common smaller form
using reflection and then project to the second form using monotonicity.
The proof includes terminal parameters and the closed endpoints.

Proposition 54.3.1 supplies the missing positive-mass prerequisite for
decreasing inverse-system limits. At a common interior parameter, take
the infima u and v of the components in theta+omega and theta+omega/2.
Normalized compact zero sets prevent either infimum from collapsing.
Decreasing-net compactness gives psh limits; the envelope sandwich
shows that u is I-model. Compatibility gives u >= v, whence

    M_(theta+omega)(u) >= M_(theta+omega)(v)
                       >= 2^(-n) integral_X omega^n > 0.

The last inequality uses the positive mixed terms of the nonpluripolar
binomial expansion and its purely smooth term. It is proved directly,
without assuming decreasing continuity of mass. Only after obtaining
positive mass is the decreasing-envelope theorem applied. The
transition formula now displays its source and target backgrounds.
The result has the asserted terminal parameter and is the greatest
lower bound in the inverse limit.

The lower bound depends on omega and tends to zero under shrinking
perturbations. It does not assert positivity in the unperturbed class.
The fixed-class mass-collapse example from the preceding Chapter 52
audit remains valid; its members cannot be the components of a
decreasing compatible family with the stated common terminal bound.

The same audit found an incorrect countability assertion in Chapter 51.
For fixed omega_0, the forms omega_0/m are cofinal for the reversed
Kähler order, by compactness of X. Chapters 51, 53 and 54 now
distinguish this cofinal sequence from a countable subfamily supplied
by Choquet's lemma for an arbitrary index set of metrics.
The trace reminder retains its additional convergence and domain
hypotheses; the trace theorem itself is unchanged.

## Exact source versions

The author's supplied lecture files were read without modification:
chapter_comp.tex, chapter_envelopes.tex, chapter_testcurve.tex and
chapter_NApotential.tex.
Corollary 6.1.3 and Proposition 6.1.3 on printed page 199 of the
[public final lectures](https://mingchenxia.github.io/Lectures/SGPT_final.pdf)
give precisely the I-envelope candidate characterization and order
equivalence used above. Physical page 215 was rendered and inspected.
The existing Chapter 51 I-projection, compactness and nonpluripolar
mass inputs are retained as cited prerequisites.

For [Operations on transcendental non-Archimedean metrics, version 3](https://arxiv.org/abs/2312.17150v3),
dated 22 October 2024, the checked locators are:

- Proposition 2.8, pages 5--6: decreasing I-envelope compatibility,
  explicitly requiring positive mass of the limiting potential.
- Definition 4.1 and Lemma 4.2, page 13: the order on inverse systems.
- Definition 4.9 and Lemma 4.10, page 15: decreasing infimum, terminal
  parameter and greatest-lower-bound properties.
- Definition 4.20, page 18, and Section 4.8, pages 20--21: the existing
  trace definition and functoriality locators. These locator checks
  do not constitute a new proof audit of the trace theorem.

Source pages 5, 6 and 15 were rendered and inspected. The arXiv
history and the author's homepage were checked: the author warns
that the published volume contains an earlier version. A separate
XiaOperationsV3 bibliography entry now identifies the actual source
of the Chapter 54 numbered citations. The published Xia23Operations
entry is preserved; its locators are not silently identified with v3.
The source note also corrects the description of the supplied
operations material, which consists of sections in the lecture
chapters rather than a separate supplied operations chapter.

## Validation and preservation

The second mathematical pass checked both directions of the order
comparison, normalization and noncollapse for nets, the background
of each psh potential, positive mass before envelope interchange,
the common terminal interval and endpoint convention, and the
quantifiers in the cofinality assertion.
The general singularity-metric theorem remains a precise imported
input; no new research-frontier result or production verifier gate
is claimed.

The final full build succeeds with 3,931 pages and 18,668,128 bytes.
There are no unresolved references or citations and no horizontal or
vertical overflows. The pre-existing class-name warning remains.
The 389-file TeX closure has 11,526 unique labels, no missing inputs,
duplicate labels, dangling references or structural defects.
The active research inventory is unchanged: 46 atoms in 14 environments,
with tiers (0,5,8,16,17).

The actual edited blocks pass the strict writing audit with zero errors
and zero warnings. The scope excludes unchanged legacy optional titles
and inline delimiters. Final physical pages 3128, 3136, 3207--3209,
3217--3218, 3220--3222, 3227 and 3930 were rendered and checked.
The decreasing-infimum definition starts with its formulas on one page.
Later statement and section boundaries were checked after tightening
the proof. Unchanged final raster pages were compared byte for byte
with the already inspected renderings.

PDF SHA-256: 01c5bf01449663b172ca093e057a52e8ecee2ae2b53fd6c30c228207c1609a12

Edited chapter SHA-256 values:

- ch51_complex_prerequisites.tex: 829d6d72530cda573f80cdde61ee3c72e41959600632774ae6a6b2402330e356
- ch53_transcendental_metrics.tex: 61478a274093b37f1da563fd1d52abaf8bc012de6a0eeab80f01fba1da195c8a
- ch54_operations_trace.tex: 96d6b19b3261d1647338669c62fc167cdefb3ecf9269a9427e382969d68ceab3

Primary-source PDF SHA-256 values:

- nappt-sgpt-final-20260923.pdf: c816eea5f06822021fa8dd75b70f82724ee47e6dcd6830729f5ecc109296b706
- nappt-operations-v3.pdf: 773eea71af9f1fff112bf5fcab2b9046b81467df2e37165ee1da3949ff74c6d9

Read-only supplied source SHA-256 values:

- chapter_comp.tex: c8cb2b9c6cbcc9a1b6965f23802eaed6891fcc23b965163a37a227e53497f7cb
- chapter_envelopes.tex: 9b3757bb28b898c90361f2928dbbff1b580a0c674a2f6e009823658126ec969b
- chapter_testcurve.tex: b39e18f7e00c84916d791b54d8040bf6a2ad9a923f2c8e3497170ca2da7594d0
- chapter_NApotential.tex: 81dc584fdf60b7907551f6d2b1493fb740594bf94b27b2092ffd8df7f53516d1

Only the three named chapters, the new bibliography entry and
editorial progress records were changed. The author-supplied
CURVE_PSH.tex remains byte-identical to its recovered copy.
Frozen proof packets, production verifier records, research-atom
classifications and dated release artifacts were preserved.
The current PDF is an ignored local build artifact.
This receipt records local mathematical, source, style, build and
visual checks, not independent-agent or production Rethlas verification.

The next bounded unit is the Chapter 54 volume-continuity argument:
separate the monotone family index, the initial-level limit and the
Kähler perturbation; check the uniform error estimate and the
failure of decreasing continuity of total inverse-system volume.
