# Addendum: exact Ch23 revised1 recheck

31 August 2026. Independent reviewer: `/root/p081_weighted_repair_fresh`. This addendum preserves `AUDIT.md` (SHA-256 `feb04a45f2b20bfc62773be8274510cb2f5d3b965777480276d132f528449b5c`) and applies only to the new exact bytes below.

## Outcome

All R1–R3 findings in the earlier audit are resolved in this revision. No remaining substantive mathematical gap was found in the reviewed Ch23 repair, relative to the same stated Ch20/Ch21 and source inputs. This is an independent mathematical recheck, not production verification, full-manuscript acceptance, or authorization to integrate.

The SNC paragraph now fixes the original-field regular semistable subdivision before any BFJ approximation is chosen. It preserves the metric skeleton and retraction while retaining the original vertex set for chording, so both the SNC-only approximation and retraction inputs apply. The nodal Cartier argument and real numerical chording remain as previously audited.

The numerical example now chooses base-residue-field-rational smooth blowup centres, justifying the unit edge weights and integer degree moves. It distinguishes the skeletal contact set from its global analytic preimage and attributes vanishing off contact to total curvature, not to the relative potential's Laplacian. The related corollary now calls ΔP=−c the reference-adjusted curvature equation, not a homogeneous equation.

## Exact reviewed bytes

Directory:

`/private/tmp/nappt_p071_20260827/manuscript/editorial/solver_dossiers_20260831/p081_ch23_curve_consumer_repair_20260831/revised1/`

| File | SHA-256 |
|---|---|
| MANIFEST.json | 413ae8813d17aeb142aceec46447ad71154c6fdb7140d52e1b4677af47184ac4 |
| snc_addendum.tex | 12ff696ae1ce33b61fec9615ea2f2b3402802eca84b4cad31a37aa59174cc53b |
| curve_chord_bridge.tex | ac5d104c5d94191e0546bfab5160c9d54c461b76ecf02b6ba005911ebc9b78c1 |
| patched/ch23_bfj_envelopes.tex | cb9d7c65bdf64b2b52c32483877f13a143b59d07615fc6d5f9ff3ced0d0e2e06 |
| chapter.patch | ab980a9e71452778b9f0f04f007a55044db3bd06db9e25db1ca42bfd76cea1a4 |

The revised bridge and full-copy differences were read completely. The only changes relative to the earlier full copy are the SNC insertion and the four reviewed rational-centre/contact/curvature replacements. The three other original fragments are unchanged through that exact full-copy comparison.

## Mechanical checks and remaining gates

The new read-only `verify_ch23_revised1.mjs` verifies all ten earlier manifest entries and all nine revised1 entries, with zero size/hash mismatches. The full-copy revision is reconstructed in memory and compared exactly. All 178 original labels remain among 179 proposed labels, with no duplicates. The combined chapter patch passes `git apply --check`; it was not applied. The earlier audit bytes and live source are preserved.

No compile, PDF production, source mutation, or Rethlas submission occurred in this recheck. The required production sol/xhigh verification, coordination with the Ch29/Ch31 repair, final rebase, and full-manuscript integration checks remain unresolved gates. No envelope-scope enlargement or inventory-retirement claim follows.
