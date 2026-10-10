# Chapter 5: second reading audit

Date: 2 October 2026. The complete original 3,271-line active source,
`parts/part1/ch05_skeleta.tex`, was reread from beginning to end. It has no
active input fragments. The repaired source has 3,349 lines, preserves all
74 original labels and adds one classical helper label.

The face-compatibility proof now works through weighted monomial ideals,
rather than substituting units into a power series that need not converge
after localization. The helper proves contraction of these ideals from the
positive-coordinate localization: the completed quotient has a finite
parameter-adic filtration whose graded pieces are free over the
zero-coordinate power-series ring; multiplication by an element outside the
parameter prime is injective on each piece. Faithful flatness then gives
contraction in the original local ring. Threshold membership identifies the
face valuation with the minimum projected weight. The Newton-boundary and
minorant arguments use this same helper, with no circular dependence.

The helper reorganizes a classical saturation argument already used in the
chapter. It is not an original research claim or a new independent verifier
verdict. The exact finite checks in
`tools/second_reading_ch05_examples_20261002.py` pass: 24 weighted quotients,
48 injective multipliers outside the parameter prime, 24 excluded nilpotent
multipliers, ten truncation witnesses, and the cancellation witness
`w+(z-w)=z`. These illustrate why the original zero-weight series argument
was insufficient; the general proof remains the filtration argument.

The chapter now separates a proper compact analytification from its local
charts, a model skeleton from an essential skeleton, and model piecewise
affine functions from limits of potentials and measures. SNC charts are
taken at the generic stratum, and the weight-one convention explicitly
rescales the absolute value. Curve cycles and chain examples have their
stated scope. Annuli come from formal node charts; attached open-disc
descriptions are made over a completed algebraic closure. Local
contractibility and deformation claims retain the cited polystable
hypotheses, and the equicharacteristic proof is distinguished from the
characteristic-free formulation.

Other repairs distinguish cellwise convexity from global nefness and graph
subharmonicity, rational from real piecewise affine functions, and an
interior ideal-function atom from endpoint terms supplied by the
polarization. Skeletal continuity is checked on regular algebraic
functions and their quotients. The Hesse example uses formal coordinates
and the displayed rational point; the split elliptic-cycle length and the
effects of nodal versus smooth blowups are explicit. Retraction fibers are
described on the whole relevant cell. The dictionary records nonunique
representations and the reference-form hypotheses for positivity.

Of 84 original formal environments, 65 remain byte-identical and nineteen
change; the classical helper and its proof add two. Earlier source/proof
gates are reused for unchanged imports. Direct semantic, dependency,
delimiter and structural checks replace the unavailable legacy scoped-writing
executable. All edited proof and example contexts were rechecked.

The full book builds to 4,170 pages, 19,472,176 bytes, with zero TeX errors,
LaTeX/package warnings, overfull boxes, unresolved references/citations and
rerun requests. It has 865 nonfatal underfull boxes. All physical Chapter 5
pages 179--226 and seams 178/227 were visually inspected across thirteen
contact sheets. The helper's unnamed heading and the final dictionary
placement were repaired and their changed sheets rereviewed. All thirteen
final bitmaps match that reviewed layout exactly. No clipping, collision or
detached reviewed heading remains. Post-render references pass for 425
active inputs and 12,564 unique labels; the inventory remains 42 atoms in
twelve families with tiers (0,3,7,15,17).

Exact hashes, environment scope and example receipts are in
[the manifest](second_reading_ch05_manifest_20261002.json). The selected
review PDF is
`/workspace/book-completion-drafts/second-reading/Ch05_Review_2026-10-02.pdf`.
Chapter 5 passes this reading gate. The complete-book goal continues in
the cloud.
