# P07.2 omega-one uniform-bound candidate, v2

Status: **frozen research candidate; not production verified; not a
live-book input**.

The mathematical payload is the CLD-specific theorem

\[
\operatorname{Psh}_{X,\omega_1}=\operatorname{Psh}_X,
\qquad
\operatorname{CPsh}_{X,\omega_1}=\operatorname{CPsh}_X
\]

for every affine \(G\)-tropical space \(X\), together with the local
common-countable-rank assertion for a decreasing sequence.  The proof uses
CLD Lemma 8.1.4, CLD Proposition 8.1.11, local compactness, the sheaf axiom,
and regularity of \(\omega_1\).

The v2 payload deliberately makes no theorem about an arbitrary sheaf
hierarchy.  It also makes no finite or fixed countable rank claim and no
first-stage-collapse claim.  See `V1_TO_V2_REPAIR_NOTE.md` for the exact
repair provenance.

`minimal_compile.pdf` is a packaging check only.  Production Rethlas must
verify the exact frozen bytes of `statement.tex` and `proof.tex` before any
live-book integration.
