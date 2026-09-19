# P14.3 unconditional exact-live production ledger

## Target bytes

The target consists of the exact current statements and proofs of
`prop:mp-psh-decreasing-stability`, `thm:p143-mp-section`, and
`thm:p143-full-kahler-comparison`, materialized by
`materialize_live_packet.py`.  Their per-chunk and packet SHA-256 values are
recorded in `LIVE_CHUNK_HASHES.tsv`.

## Independently verified P14.2 premise

The exact current P14.2 V15 statement packet is supplied as a declared
statement dependency.  Its SHA-256 is
`c2f8fa3841704dc2dacaf8b4d8d633d8129790f74f555cef9b887f769373060b`.
The corresponding exact current proof packet, including the local
quasi-psh-to-psh bounded-perturbation reduction, was independently accepted
by the production verifier with:

- verdict `correct`;
- zero critical errors and zero gaps;
- checked item `pi_4e14dc8a6a26aa190cd191b5`;
- proof digest
  `86de3f3687ce5160d37bcdff4315e93462dc0138939170957425aea4d9e45f7e`;
- context digest
  `8f63b5ed0ca6234e59723fc1abf3b4e0cb64503540a3db5cb0fe573288e981a3`;
- adaptive-context digest
  `54981f00909b54f10102efe4ec4ae01ad764a0141b382959c7af0299eb24280c`.

The immutable receipt is
`../p142_v15_qpsh_repair_production_20260919/VERIFICATION_RUN_RETRY1_20260919/response.json`.
Thus `thm:p142-raw-transform-usc` and
`cor:p142-pseudoeffective-raw-usc` are established premises here, rather
than hypotheses to be reproved inside the P14.3 item.

## Exact current internal premise cards

`PREMISE_STATEMENTS.tex` supplies the exact current statement bytes for all
named internal results used by the three target proofs:

1. compactness and Hausdorffness of the semivaluation spectrum
   (`prop:mp-tropical-compactness`);
2. rational translation stability of the model psh cone
   (`prop:mp-model-psh-stability`), the decreasing-net definition
   (`def:mp-general-psh`), and divisorial finiteness/comparison
   (`thm:mp-psh-divisorial`);
3. the common endpoint and positive-volume recovery interfaces
   (`prop:tna-common-terminal`, `thm:tna-positive-volume`);
4. maximum and decreasing-infimum operations
   (`def:operations-maximum`, `def:operations-infimum`);
5. the constant raw transform, component independence, divisorial
   inversion/order reflection, finite-energy correspondence, dominated
   divisorial comparison, all-point finite-energy comparison, and
   maximum/infimum transform formulas from Chapter 71.

These are declared ancestors of the target item.  Their statements are not
silently inferred from labels.

## Single canonical source-extract family

The proof request supplies exactly one extract for each cited primary source:

- `SOURCE_EXTRACT_MP24.txt`, whole-file SHA-256
  `0445ccf2c4474b6576a8053d0c7c038ffbd72c2ab27bb3d5704b90dd0e5beb62`;
- `SOURCE_EXTRACT_DXZ23.txt`, whole-file SHA-256
  `7d5a061d240096139e6302c2b4da2e9c125a8839730fc90909c1488baa446244`;
- `SOURCE_EXTRACT_XIA23.txt`, whole-file SHA-256
  `c75572e06a2df8cb9dbd76726678a52db5e79587ec568df41f4886e3e4ee8005`.

All three are the immutable files archived in
`../p143_full_kahler_truncation_integration_20260919/`.  No second extract
or second whole-file hash for any of these source filenames is included in
this request.

The MP extract contains the decreasing-net definition, translation
stability, divisorial comparison, and the finite-energy radial interface.
The DXZ extract contains the inverse-system definition, energy formula (43),
and finite-energy correspondence.  The Xia extract contains positive-volume
recovery, divisorial order reflection, maxima, and decreasing infima.

## Scope

The target proves the full raw-transform/MP order isomorphism for a Kähler
class.  It makes no assertion about an unchanged relatively nef MP cone in a
big non-nef class and constructs no normalized energy or Monge--Ampère
operator in a zero-volume class.
