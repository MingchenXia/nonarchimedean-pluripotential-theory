# Isolated full-manuscript syntax review

This directory records a syntax/reference test of proposed curve repairs,
not an accepted book release. The live manuscript and existing PDF must
remain untouched. The scratch build is draft-mode only: no PDF is produced.

Inputs are the current live manuscript and the exact frozen full-chapter
proposals listed by assemble_review.mjs. All literal TeX input dependencies
are copied, including live exact-proof imports. Only source/style/bibliography
assets are used; prior auxiliary files are not inherited. The existing
book.bbl is copied as a bibliography input, because this correction adds
no bibliography entry. Multiple TeX passes and an index pass test the real
book cross-references rather than fragment placeholders.

Mathematical review and production Rethlas gates remain separate. The
presence of an unrepaired passage elsewhere in a copied chapter must not
be mistaken for acceptance. In particular, the pending Ch21 curve-retraction
audit is not resolved by compilation. No problem is retired by this check.
