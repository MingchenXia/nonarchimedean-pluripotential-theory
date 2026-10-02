# Appendices D--F quality audit

Date: 2 October 2026. Scope: the three complete appendix sources, under the
sequential whole-book quality programme. This is a direct mathematical,
source, editorial and rendered-page audit. It is not a new independent
solver/verifier verdict or a change to an archived research receipt.

## Architecture and complete scope

Appendix D supplies finite-dimensional convex duality, mixed volume,
Alexandrov measure and the real-current normalization. Appendix E supplies
arbitrary-directed-set topology and the compact semicontinuous envelope and
integration calculus. Appendix F supplies cycle-level intersection theory,
the Cartier/Weil distinction and the separately imported nef numerical
b-class limiting theorem.

All three sources were read completely, including proofs, examples,
warnings, checks and source notes. The final scope contains 2,274 lines,
169 semantic labels, 35 labelled headings and 74 labelled reusable
environments. There are 40 assertions and 40 proofs:

| Appendix | Lines | Labels | Headings | Reusable objects | Assertions/proofs |
|---|---:|---:|---:|---:|---:|
| D | 936 | 65 | 10 | 25 | 14/14 |
| E | 669 | 53 | 13 | 27 | 15/15 |
| F | 669 | 51 | 12 | 22 | 11/11 |

The appendices have no input fragments. The other 119 appendix-closure
files remain unchanged during this unit: 116 match the entry baseline,
and A--C match their completed current-source gate. This includes all
108 appendix input fragments. Frozen statements/proofs, verifier receipts
and the research inventory are preserved.

## Mathematical and exposition repairs

### D: convexity and normalization

- The decreasing-net convexity proof handles the endpoint coefficients
  separately, so it never multiplies infinity by zero.
- Fenchel equality implies the dual subgradient inequality directly from
  the defining supremum, without a hidden closedness assumption.
- The biconjugacy proof constructs a finite affine minorant using relative
  convex continuity and separation. If a later separator is vertical,
  adding a small multiple of the first minorant produces the required
  positive vertical coefficient. Properness of the closed hull is proved.
- Nonnegative conjugate parameters are justified by the negative-tail
  estimate. The single-break example computes both Legendre branches and
  recovers the three branches of the original concave function.
- Convex bodies and all volume measures consistently live in the dual
  lattice space M; support functions live on N. Volume statements require
  positive dimension, and the bilinear AF reformulation requires n >= 2.
- Smooth support functions are homogeneous away from the origin. Their
  Hessians are positive only in tangent directions; the radial eigenvalue
  is zero. Sphere functions are interpreted by homogeneous extension.
- The Alexandrov construction extends the function by infinity outside its
  domain when forming the conjugate. The smooth area-formula argument uses
  local Lipschitz continuity and exhaustion, rather than asserting a
  global Lipschitz bound.
- The polyhedral triangle example displays mass 1/2 for Alexandrov measure
  and mass 1 for the current square. Mixed products use finite convex
  functions on a common domain and the exact convex BT input.
- The dilation remark distinguishes the book's pullback, scaling both
  covector families, from Berndtsson's base-only dilation. The two
  homogeneity degrees differ; the contraction identities agree.
- The zero-volume check specifies the measure being pushed forward.
  Translated first moments require integrability; probability normalization
  requires positive finite mass.

### E: nets and semicontinuity

- Neighborhood nets require no countability assumption. Replacing one by a
  sequence requires an additional selection property.
- The divergent-subnet construction uses an open excluded neighborhood,
  giving a closed complement. Upper regularization likewise uses open
  neighborhoods.
- Pointwise sequential closure characterizes Frechet--Urysohn spaces;
  the weaker sequential closed-set test characterizes sequential spaces.
- The countable-spikes example proves that Choquet selection equates usc
  regularizations without equating pointwise suprema, even on [0,1].
- The lower-semicontinuous integral-minorant formula is explicitly linked
  to its later complete Radon/Urysohn proof. The proof has no dependency
  cycle. Metrizable probability spaces give a sufficient subsequence
  criterion without claiming necessity.
- A two-index calculation shows that a coupled supremum does not decouple
  even for finite families. Integral subtraction is restricted to the
  integrable or well-defined extended-real domain.

The complete subnet, compactness, Dini, Choquet, Radon integration and
Portmanteau proofs were reviewed for tail cofinality, directedness,
semicontinuity, finite mass and extended-real operations.

### F: Cartier operations and limiting products

- Pullback in the projection formula means the pulled-back line bundle's
  first-Chern operator. It is defined when divisor equations vanish on
  the image. The proof iterates the exact line-bundle projection formula,
  rather than pulling back a zero local equation as a Cartier divisor.
- The non-Cartier Weil b-divisor example uses blowups at infinitely many
  distinct closed points. Any proposed finite determination is an
  isomorphism outside finitely many points; blowing up a remaining point
  contradicts its prescribed exceptional coefficient. The argument does
  not require rational points or a general point avoiding an unspecified
  infinite collection.
- Nef descent constructs a curve over a downstairs curve by taking a
  closed point of its generic fibre and then its closure. Its degree is
  finite and positive.
- Numerical transition maps are asserted on smooth models, where the
  Chow projection formula applies. No singular-model numerical
  pushforward is silently introduced.
- The nef b-volume proof specifies a decreasing Cartier approximation.
  The source's approximation theorem, limiting-product existence and
  independence, upper semicontinuity and decreasing-net continuity remain
  distinct exact imports. Arbitrary Weil products and an extra absolute
  intersection factor are not introduced.

## Primary source review

Two freshly downloaded PDFs were title/version checked, read at every
listed page and visually reviewed in ten contact sheets (35 selected
pages). These are witnesses for the cited inputs, not fresh reviews of all
classical books in the bibliography.

| Source witness | Physical pages read and viewed | Imported scope checked |
|---|---|---|
| Berndtsson, arXiv:2501.02896v3 (6 August 2026), 93 pages | 1, 17--18, 21--28, 50--59 | Theorem 4.2 convex BT; Alexandrov normalization; support-function volume and its polarization; Section 7 partial dilation; Theorems 12.3 and 13.3 Lorentz signature and linear kernel/solvability |
| Dang--Favre, arXiv:2007.04549v2, 35 pages | 1--2, 6--8, 11--19 | Smooth projective characteristic-zero model category; weak closure; Theorem 2.1 decreasing nets; Proposition--Definition 3.1; Theorem 3.2 upper semicontinuity and decreasing-net continuity |

The Dang--Favre preprint is the source witness for the bibliography's
published DF20 entry; identity with the published journal PDF is not
asserted. Its third continuity item has a sequences heading but explicitly
states a net in its body; the appendix uses that body. The introduction's
sequence formulation is not substituted for the exact Theorem 2.1 import.
Berndtsson's bilinear form is n! times the appendix's form, as his (12.4)
shows. His Section 7 dilation fixes the auxiliary covectors.

The complete statement and proof of Stacks Tag 02SU (Lemma 42.26.4) were
read for the first-Chern projection formula. Tag 02U9 (Lemma 42.38.4) was
also read in full as a general-Chern corroboration. The earlier search
results 0FBD/0FBC concern localized Chern classes and were not used as
imports. The surrounding 02U4 section is not claimed as a complete review.

The precise classical locators retained include Rockafellar Theorems 10.1,
12.2, 24.5 and 25.5, Schneider Theorems 5.1.7 and 7.3.1, Evans--Gariepy
Theorem 3.8, Willard Chapters 4--5, Kelley Chapter 5, Rudin Theorem 2.14,
and Fulton Proposition 2.3(c). Their foundational roles remain explicit;
no fresh full-book PDF inspection is claimed. Rockafellar's author index
was inspected, but its listed book link returned 404. It is not counted as
a downloaded primary book. The internal Chapter 7 relative-continuity
statement and Chapter 14 convex BT statement were reread.

PDF source SHA-256:

- Berndtsson: d2cb950659b15eb2223ee6cebf7034c6169346277c79a5fb4bd0adbb6a4da034.
- Dang--Favre: a1fd9666bbca63b365053f9c6b240e5c441ddd562787dd905c14445403e0fda6.

## Calculations, navigation and remaining gates

Eight finite calculation families pass 18,225 exact checks: rectangle AF
(4,096), mixed-volume polynomial coefficients (12,288), the single-break
Legendre minimum (1,260), simplex factorial normalization (144), coupled
supremum bounds (256) and their strict example (1), Cartier projection on
one-point surface blowups (90), and the exceptional degree calculation
(90). These are example supplements; they do not certify the general
analytic, net or intersection theorems.

All reusable environments and headings have semantic labels. Inline math
uses the house delimiters; the existing mathematical index entry in F is
retained. The unavailable legacy writing-audit executable is replaced by a
complete direct/scoped source audit, label/heading scans and protected-file
hash comparison. No nonexistent tool run is claimed.

## Full build and rendered gate

The final full latexmk build passes: 4,160 pages and 19,407,769 bytes.
The final PDF SHA-256 is
f5fb5cc118b48afd5d86229756963870d386e012fe62f20ee6e9ddcdb3d08ede.

All 34 appendix pages were visually inspected in nine contact sheets,
with both seams: D physical 3779--3792 (printed 3709--3722), E physical
3793--3802 (printed 3723--3732), F physical 3803--3812 (printed
3733--3742), and seam pages 3778/3813. The blank D terminal page is the
intentional recto-start separator. An overflowing inline triangle formula
was moved to display form. Two short warning boxes now stay together;
the template's ordinary samepage wrapper did not prevent the heading
break, so the final sources use local minipages. All nine sheets were
reviewed again after the final rebuild. The three underfull diagnostics
in F's narrow projection table were checked visually; no clipping,
overflow or layout defect remains in the reviewed scope.

Post-render references pass for 425 inputs and 12,445 labels, with zero
missing inputs, duplicate labels or dangling references. Six checker tests,
the unchanged 42-atom/12-environment inventory, the complete scoped label
and protected-file audit, and git whitespace checks pass. The final log
has zero D--F overfull boxes, unresolved references/citations, missing
glyphs, rerun requests, fatal errors or duplicate PDF destinations.
The inherited class-path warning and eighteen overfull boxes elsewhere
remain for the whole-book pass.

The full review PDF is retained at
/workspace/book-completion-drafts/Appendices_DEF_Final_Review_2026-10-02.pdf.
Local reproducibility artifacts are /tmp/appendices_DEF_verify_20261002.py,
/tmp/appendices_DEF_scope_20261002.json,
/tmp/appendices_DEF_render_20261002/manifest.json and
/tmp/appendices_DEF_primary_20261002/manifest.json. Primary downloads are
in source_material/appendices_audit_20261002/ (ignored by git).

## Current-source hashes and disposition


- appendices/appD_convexity.tex: e709ffdebf3312f8a0fd6cce17aa30ff163403df2ed36ff0b6ff5bd3ff157b29.
- appendices/appE_nets.tex: f889d3398295b60d2556368cddbc28ac9127739b961c47b3265554bcb33357d5.
- appendices/appF_intersection_bdivisors.tex: a30e25bbe184b8899b661affca203a1ffc4a74b7724774b2f4c083608cc16363.

All six programme gates pass for D--F. This is a classical/editorial/source
repair and makes no new research, priority or independent-verifier claim.
The work remains local pending explicit remote-push approval. G--I are the
next active unit; the whole-book goal continues.
