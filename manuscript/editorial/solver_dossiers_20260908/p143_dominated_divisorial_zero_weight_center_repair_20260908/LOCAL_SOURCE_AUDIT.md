# P14.3 v3 local source-alignment audit

## Verdict

**PASS for local citation alignment; not an independent mathematical or
production verdict.**

This audit checks that the prepared v3 review packet names the repaired
claim and that the citations it invokes occur in the durable local source
copies.  It does not validate every deduction, authorize external
submission, or retire P14.3.

## Exact reviewed inputs

| Input | SHA-256 |
| --- | --- |
| `VERIFICATION_STATEMENT.md` | `376312e9ff2a51f8ca379bd170f7dfe40bb45831b257eff9ec570ed4bffe96b7` |
| `VERIFICATION_PROOF.md` | `ea1064b8856bc47457359e339b019996d6de85e8c196c63f182c1c003ff327b3` |
| v3 proof postimage | `1392f87e1ef47a1dde1c8b17ee7e264ed4a1b926e031ea35a9fb711e91f83d87` |
| MP24 local source text | `0445ccf2c4474b6576a8053d0c7c038ffbd72c2ab27bb3d5704b90dd0e5beb62` |
| DXZ23 local source text | `7d5a061d240096139e6302c2b4da2e9c125a8839730fc90909c1488baa446244` |

The first two files are a v3 review rendering.  The displayed postimage hash
is the exact patched TeX proof recorded in `VALIDATION.md`; `V2_TO_V3.patch`
replays from the fixed v2 postimage to that byte sequence.

## Local source checks

The verified local copies are:

- `manuscript/editorial/solver_dossiers_20260901/p142_source_closed_production_release_repaired_authored_stage_dossier_v2_20260901/source_augmentation/mp_2409.06221v2.txt`;
- `manuscript/editorial/solver_dossiers_20260901/p142_source_closed_production_release_repaired_authored_stage_dossier_v2_20260901/source_augmentation/dxz_2302.02541v3.txt`.

Exact-marker checks locate the required results at these lines:

| Source result | Local line |
| --- | ---: |
| MP24, Lemma 2.1.1 | 552 |
| MP24, Remark 2.3.2 | 735 |
| MP24, Proposition 2.3.4 | 799 |
| MP24, Remark 2.3.5 | 877 |
| MP24, Theorem 2.3.6 | 889 |
| MP24, Theorem 4.3.8 | 2234 |
| MP24, Theorems 5.1.4 and 5.1.7 | 2452 and 2501 |
| DXZ23, Theorem 3.17 | 1322 |

These results provide the stated interfaces: central ideals, birational
divisorial invariance, rational monomial divisoriality, ordinary divisorial
density, the MP comparison principle, and the finite-energy correspondence.
The direct v3 argument from `Z subset W subset B_i` to
`O_Y(-B_i) subset I_Z` is a deduction inside the candidate, not a claim that
any cited source proves P14.3 outright.  The raw-transform upper
semicontinuity is retained solely as the stated P14.2 hypothesis.

## Production boundary

No model-backed verification was run for v3.  A prior v2 local
source-alignment audit does not certify this changed postimage.  The v3
packet is prepared so that one explicitly authorized, reproducible external
review can inspect the exact current argument.  Until then P14.3 remains
open and Chapter 72's count and status remain unchanged.
