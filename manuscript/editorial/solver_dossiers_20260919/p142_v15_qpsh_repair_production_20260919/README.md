# P14.2 V15 exact-current quasi-psh repair

Date: 19 September 2026.

This dossier materializes the exact current Chapter 71 statement and proof of
the P14.2 upper-semicontinuity theorem and its pseudoeffective corollary.  The
V15 proof repairs the sole mathematical gap found by the later combined audit
of V14: locally, each quasi-psh level is written as a psh function plus a
smooth term; bounded smooth perturbations leave multiplier ideals unchanged,
so DEL00 subadditivity applies to the psh part.

`materialize_live_packet.py` extracts the exact current target chunks, the
statement and proof of the perturbation-independent transform, and the exact
statement of the five one-curve transform conclusions.  Per-chunk and packet
hashes are recorded in `LIVE_CHUNK_HASHES.tsv`.  The immutable V14 source
extract family is supplied from the sibling V14 dossier.

The first V15 run returned `wrong`, with zero critical errors and one gap:
the exact five one-curve conclusions used by the perturbation-independent
transform proof were absent.  `ADDITIONAL_PREMISE_STATEMENT.tex` supplies
that exact statement without changing the target proof.  The retry returned
final `correct`, zero critical errors, and zero gaps for item
`pi_4e14dc8a6a26aa190cd191b5`.

The accepted retry is the exact-current production gate that retires P14.2.
The earlier V14 pass is retained only as superseded review history.
