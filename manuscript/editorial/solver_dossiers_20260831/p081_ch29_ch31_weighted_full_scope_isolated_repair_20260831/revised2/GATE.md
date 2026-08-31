# Revised2 isolated Ch29/Ch31 candidate — NOT INTEGRATED

Date: 31 August 2026. Live base commit: `4ec9fb514e9d33d0f8e1b6d918d6264a104cb676`.

This is a new child directory of the frozen first assembly. It preserves that assembly, the weighted original/revised1 packet, the pending real-class F packet, and every live manuscript file. The full chapter copies and patches are review candidates only. No mathematical verification status is inferred from draft compilation or exact-byte checks.

## Release gates

1. Exact independent mathematical acceptance of the underlying weighted and real-class F packets at the source hashes recorded in this manifest.
2. Exact independent review of all revised2 chapter mathematics, including the local-real-potential positivity lift, both new examples, the transported labels, and their downstream consumers.
3. Production Rethlas verification with model sol and reasoning xhigh for every new mathematical byte, preserving exact submitted hashes and receipts, as required by the user.
4. Coordinated review of the separate Ch23 consumer repair and any further weighted-energy consumers (including the independently reported Ch26/Ch28 mismatch). This directory does not repair or endorse those chapters.
5. Rebase against the then-current manuscript, recheck all labels and hypotheses across chapters, and compile the actual full manuscript. Only after the preceding gates pass may future integration remove the temporary live reconstruction warnings.

The production permission gate remains unresolved. No production submission, alternative endpoint, credential workaround, or live integration has been attempted. Neither an earlier weighted-packet audit nor a local compile endorses revised2.

## Scope retained

- The equation theorem uses an actual GIVEN proper strictly semistable formal model over the original arbitrary complete nontrivially valued field, a positive-degree line bundle, and a positive target measure of matching mass supported on that finite skeleton.
- The point-reference metric is Thuillier-lisse, not asserted rational formal. An actual model reference on the given model is additional data, not automatic.
- The real-class criterion concerns an actual real closed model form on its determining model and an actual rational model function with the asserted original-skeleton factorization.
- The envelope competitor class remains rational model functions. There is no identification with the real linear span of model functions or the unrestricted all-PSH envelope. Degree zero still requires an actual rational model competitor.
- Conductances are node residue degrees at both endpoints; slopes use natural-log analytic length. Resistance lengths enter estimates only. Real atomic masses need not produce rational slopes; nonatomic limits need not be lisse.
- No nonskeletal-measure continuity, general-envelope theorem, or open-problem retirement is asserted.

## Files and limited checks

The two `ch*_curve_replacement.tex` files are exact fragments of the corresponding full copies under `patched/`. `combined.patch` is against the recorded live base, for future gated integration only. `fragments_from_frozen.patch` exposes only the revision relative to the frozen first assembly; that first assembly has not been overwritten.

`REVISION_LEDGER.md` describes the new mathematics and pedagogy. `MANIFEST.json` records source and output bytes. `VALIDATION.json` records mechanical checks, not mathematical acceptance.

The standalone compile uses `pdflatex -draftmode` with the two fragments, the inherited accepted-input statements, and the bibliography. No revised2 PDF is produced, so no visual-QA result is claimed. This is not a full-manuscript compile.
