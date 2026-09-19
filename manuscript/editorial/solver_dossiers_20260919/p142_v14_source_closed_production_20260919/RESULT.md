# Production result

The 19 September 2026 source-closed production request returned HTTP 200 with:

- verification status: `final`;
- verdict: `correct`;
- checked item: `pi_786d6710873ea471db69e4e0`;
- critical errors: 0;
- gaps: 0;
- item disposition: `verified`;
- final expansion round: 0;
- expanded proofs: none.

The response binds the combined exact proof and source extracts by:

| field | SHA-256 |
| --- | --- |
| proof digest | `76e91218db89f4ec02063ebc0521f712bc335a2c0cf5acaf6ee7d92810df13f2` |
| context digest | `f1d02098b342bd4b5a09bf99c6b5cda9f92156c6477445e762c9ecadbeb2648f` |
| adaptive-context digest | `81e245298cfed0e1b5cc2bdb110816fc25b3b824a59ece5b88163c970b91b54f` |
| item-context digest | `2386c58f56c7f278bc12d177f518f6611b232251d921ffdd66e71c4b5d3a1eb0` |

The request statement has SHA-256
`cc3f5fbdc8f4a491ca6121c0c254a20f05a0bfb6da5d91f11d6ae6e406a40bc2`,
which is the V14 target hash.  This result is now historical: a later combined
exact-live audit identified the omitted local bounded-perturbation reduction
from quasi-psh to psh weights before DEL00 subadditivity.  The repaired
exact-current V15 production receipt in
`../p142_v15_qpsh_repair_production_20260919/` is the superseding basis for
retiring P14.2 and for discharging the former P14.3 premise.  P14.4--P14.6 and
P14.8 remain outside both results.
