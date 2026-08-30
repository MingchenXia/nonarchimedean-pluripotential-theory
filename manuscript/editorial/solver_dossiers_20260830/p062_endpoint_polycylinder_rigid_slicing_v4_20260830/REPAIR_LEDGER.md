# Repair ledger

1. Preserved frozen v3 byte-for-byte.
2. Renamed the principal labels to v4; mathematical text otherwise retained.
3. Routed the fully open annulus only to
   `prop:p062-arbitrary-field-annulus-v4-source-correct`; endpoint cases remain
   routed only to the verified endpoint proposition.
4. Routed the strict core only to
   `thm:p062-arbitrary-field-polycylinder-v4-source-correct`.
5. Deleted the legacy strict-open fibre-slicing statement and proof from the
   v4 dependency.  Thus the reverse use of CLD Corollary 15.1.2 is absent.
6. Replaced its sole use in the strict polycylinder proof by the stronger
   principal v4 fibre-slicing proposition.  That proof uses CLD Proposition
   15.1.1(b), in the forward local-presentation direction.
7. Materialized the rational-centred/descent and finite-trace/disc exact
   dependencies and their production receipts/responses.
8. Compiled both the principal packet and the active strict dependency; no TeX
   errors or unresolved references remain after the final pass.
