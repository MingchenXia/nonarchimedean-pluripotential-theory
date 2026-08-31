# Revised2 rational-Cartier clarification: exact-byte addendum

31 August 2026. Auditor: p213_skeletal_hostile. This is a separate addendum to the preserved original and revised1 fresh independent review.

## Verdict

The revised2 edit resolves the remaining inherited Cartier-wording issue. It makes explicit the rational-divisor hypothesis already sufficient for the proof and used in the independent mathematical audit. There is no new mathematical hypothesis, rescaling of the input function, or change to the density, maximum, envelope, or PSH conclusions.

Accordingly the bounded real-versus-rational maximum repair has no unresolved issue found in this review, with the operative combination **Ch20 revised1 plus Ch21 revised2**. This is not production verification or a certificate for the whole chapters. The separate Ch21 curve-retraction subsection, Ch24 locality, Ch30 descent, and the newly researched general-SNC length/conductance formulas remain outside the scope. In particular this addendum does not amend or re-prove the old Ch20 nonreduced-length remark.

## Exact frozen author inputs

Author directory:
/private/tmp/nappt_p071_20260827/manuscript/editorial/solver_dossiers_20260831/p081_ch20_ch21_real_model_max_repair_20260831/revised2/.

- Full Ch21: 167387 bytes; SHA256 `81a1928677f59eba2e7eac6461480c5c90cadcccc70c15ea923ebbaeba6e0ed7`.
- Saved portable cumulative patch: 4890 bytes; SHA256 `00ad0bd536bb0e826809eb0ea1f0a02bb09974140d80e4a3db7ae532d24a7a59`.
- Author manifest: 1238 bytes; SHA256 `26460ce52b3d72ef00eb667b33f456055ce50bb2534b1ede79abc5ed7503f06f`.
- Preserved Ch21 revised1 source: 167368 bytes; SHA256 `ae6f71cd7db4c21108fb975e159ccaacf76d7f7251978224f7ac70886168769f`.
- Unchanged Ch20 revised1: 180757 bytes; SHA256 `3f2814e440f738708c084ee186a06e0930c0d48db89e80db1f21e7300e373ca2`.

## Mathematical clarification

At Ch21 lines 769–770, in Step 1 of lem:ch21-model-skeletal-properties, “on which D is Cartier” becomes “on which D is a rational Cartier divisor,” with one line wrap. This is exactly the appropriate input for a rational model function. A sufficiently divisible multiple of a rational Cartier divisor is integral Cartier; the proof later chooses such multiples when obtaining relative global generation. Its divisor-function identity divides by that same multiple, so the original function and reference form remain fixed.

The source interface already independently checked in the parent audit is BFJ §5.2, specifically Lemma 5.7: its determining divisor belongs to the rational vertical Cartier group. Revised2 therefore corrects a literal overstatement without introducing a different argument.

## Exact and mechanical checks

The GATE.md, complete assembly script, author manifest, complete one-hunk diff, and surrounding proof were read. The assembly script was not executed.

All four author-manifest entries match their recorded hashes and byte counts. The old string occurs once. Independently replacing that one string by the manifest's replacement reproduces the entire revised2 chapter exactly. The whole parent-to-revised diff is the single hunk `@@ -766,7 +766,8 @@`. All 172 labels survive, with no new or duplicate label.

The actual saved portable patch equals independently regenerated cumulative `diff -u` output, labelled for the live Chapter21 path. The **saved patch itself, without any header transformation**, passes direct `git apply --check`. It was not applied. It replaces, rather than follows, the earlier cumulative Ch21 patch.

The Ch20 revised1 bytes still match their frozen hash. The previous independent-audit manifest remains unchanged at SHA256 `f054ce87afd1f894621dec516a82d6d8122de0d761dd5b6c107df8bc6e545e80`. Live Ch21 remains 166756 bytes, SHA256 `477db8e896633bcf5f89c8738e16e0afa8eaac55f36042c1d263b683daed72b3`.

No live chapter, frozen author input, or earlier audit artifact was changed. No production call or new TeX build was made.

