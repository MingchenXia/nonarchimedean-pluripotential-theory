# Primary source and dependency ledger

Date: 1 September 2026. This is an author ledger, not an independent audit.

## BFJ: original field and nonreduced SNC models

Boucksom-Favre-Jonsson, Singular semipositive metrics in non-Archimedean
geometry, arXiv:1201.0187v2 (21 January 2014).
Primary landing page: https://arxiv.org/abs/1201.0187v2 .

Exact local sources read:

- /private/tmp/BFJ_singular_1201.0187_audit_20260831.pdf
- /private/tmp/BFJ_singular_1201.0187_audit_20260831.txt

Their exact bytes are pinned in this packet's manifest.

Relevant primary passages read completely:

- Section 1.1 and Definition 1.1, printed page 6: complete DVR, residue
  characteristic zero, residue field NOT required algebraically closed;
  regular SNC support may have positive multiplicities. BFJ additionally
  requires every named intersection to be irreducible. Our construction
  instead works with its explicitly selected connected component and
  writes the global centers, so it does not silently apply that additional
  indexing convention to an arbitrary disconnected intersection.
- Sections 3.1-3.3, printed pages 12-15: monomial embedding, center-face
  correspondence, complete regular local ring and weighted-series formulas
  (3.2)-(3.4), uniqueness by dense independent weights, and continuity.
  The BFJ statement is about vertical dual complexes. The inclusion of
  horizontal boundary parameters in our full-dimensional local cell is
  proved in Section 2 of our note; it is not attributed to an unprinted
  BFJ pair theorem. Properness, but not a polarization, is sufficient for
  this explicitly local argument.
- Theorem 3.15 and its full proof, printed pages 16-19: a simplicial
  projective subdivision gives a NORMAL, VERTICALLY Q-FACTORIAL model;
  regularity is not asserted. The completed-local comparison to toric
  charts in Step 2, including flat base change of blowups, is the relevant
  interface. Our blowups are specifically smooth coordinate-center
  blowups and their new bases are unimodular. Section 3 proves the extra
  regularity instead of upgrading BFJ's conclusion by terminology.
- Corollary 3.17, printed page 19: rational points are divisorial and
  dense in each dual complex. This is consistent with the construction,
  but we do not use mere density to obtain regular subdivisions or walls.
  The terminating extraction algorithm is written separately.

No BFJ model-existence or resolution theorem is used to produce the
original pair; that pair and its full-dimensional stratum are assumed.
There is no use of BFJ psh/Monge-Ampere theory in this packet.

## GRW: comparison only, with its actual hypotheses

Gubler-Rabinoff-Werner, Skeletons and tropicalizations,
arXiv:1404.7044v3 (28 February 2016).
Primary landing page: https://arxiv.org/abs/1404.7044v3 .

Exact local sources read:

- /private/tmp/grw1404.7044v3_p213_residual.pdf
- /private/tmp/grw1404.7044v3_p213_residual.txt

Relevant passages:

- Section 1.1, printed page 1, and Section 2 conventions: K is complete,
  algebraically closed and nontrivially valued throughout that paper.
- Definition 3.1, printed page 8, and Section 3.2, page 9: the model
  charts are strict semistable charts with product of distinct vertical
  coordinates. The statement is not an arbitrary-multiplicity SNC
  theorem over a discrete original field.
- Sections 4.3-4.6, printed pages 12-14, and Proposition 4.10/Corollary
  4.11 on page 14: monomial polyhedra, the order-reversing stratum-face
  correspondence, and dimension(stratum)+dimension(face)=dimension(X).

These passages explain the familiar residual-curve face language. They
are NOT invoked to transfer the new construction from an algebraically
closed field back to K. We explicitly prove the original-field chart
changes and obtain the actual curve as a connected component of a
closed intersection. We neither assume reduced output nor identify
primitive affine metrics or conductances with a unit-weight model.

## New work and nondependencies

The new proof is the following finite construction on the supplied model:

1. The subtraction algorithm realizes a prescribed primitive positive
   ray by regular stratum blowups, with a decreasing integer termination
   measure and a verticality check at every step.
2. Repeated two-component blowups replace b_i by b_i+k_i a while retaining
   the chosen positive ray a.
3. The normalized slice formula contracts a whole all-vertical simplex
   toward P(a); continuity places its actual analytic points inside W.
4. A closed face has a whole smooth proper residual curve and has a
   dense set of independent normal weights.

No L, V, O, P, Q, or R packet is used as a proof dependency. Mention of
the outer-collar problem is an intended application interface only. In
particular, no current theorem and no current pullback is imported.
The author has independently reviewed several such predecessor packets;
that history is not an independent review of the argument authored here.

There is no novelty or priority claim about this elementary toroidal
construction. It is a detailed candidate for the bounded geometric step.
Before freeze, root read the complete draft and requested two explanatory
strengthenings: the direct Rees-chart cotangent regularity check, and the
algebraic independence of zero-weight residual coordinates with old-weight
tail control on final faces. Those clarifications are incorporated in
Section 3. This advisory input is disclosed; no independent verdict is
being attributed to root's author-side review.

## PDF inspection and warnings

The PDF skill was read and used only for source inspection. Complete
rendered pages inspected: BFJ 6,12,14,15,16,17,18 and GRW 1,8,13,14.
The other passages listed above were read in the corresponding complete
text excerpts. The relevant headings, equation numbers and source
hypotheses were preserved in this ledger.

Rendering exited zero. Fontconfig reported three instances of no writable
cache directories; no access escalation or cache-directory alteration was
attempted. All eleven page images were readable and complete on visual
inspection. SOURCE_QA.json records the warning verbatim. The exclusively
owned temporary images are removed after recording their checksums; source
PDFs are unchanged. No PDF artifact was created and no TeX compile is
claimed.
