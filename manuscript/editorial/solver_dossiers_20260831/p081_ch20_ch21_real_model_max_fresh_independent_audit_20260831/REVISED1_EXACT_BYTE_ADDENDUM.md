# Revised1 exact-byte addendum

31 August 2026. Read together with ORIGINAL_FRESH_INDEPENDENT_AUDIT.md. The original author packet and the original audit findings are preserved.

## Verdict

Revised1 addresses all three required local corrections recorded in the initial review. The fixed-form density, irrational-breakpoint example, truncation, rational minorant proof, and full-PSH maximum proof remain unchanged. No further substantive gap was found within this repair's original BFJ hypotheses. The separate Ch21 curve-retraction and other chapter-wide gates remain.

The inherited Step 1 wording “D is Cartier” is still imprecise when the input model function is rational: use “rational Cartier divisor” or explicitly clear denominators. This audit checks the proof with that rational-divisor convention and does not certify an unproved integralization. Root was notified separately; this note does not modify the frozen revised1 bytes.

This is a fresh independent review of the root-authored density/max mechanism. The auditor's comments about the stale openness denial and locator are ordinary review feedback, not authorship of that mechanism.

## Exact revised inputs

Directory:
/private/tmp/nappt_p071_20260827/manuscript/editorial/solver_dossiers_20260831/p081_ch20_ch21_real_model_max_repair_20260831/revised1/.

- Full Ch20: 180757 bytes; SHA256 `3f2814e440f738708c084ee186a06e0930c0d48db89e80db1f21e7300e373ca2`.
- Full Ch21: 167368 bytes; SHA256 `ae6f71cd7db4c21108fb975e159ccaacf76d7f7251978224f7ac70886168769f`.
- Portable Ch20 cumulative patch: 30978 bytes; SHA256 `5b70d68f29b2a5be0c085a48a71b7f9257c0fcd0934712249bb041cac7a810e5`.
- Portable Ch21 cumulative patch: 4394 bytes; SHA256 `dbd51e8360bc49bcf94eb2bcf89b235b3a9b9d234e35cbbff2a8640cb2f022e1`.
- Author revised1 manifest: 3511 bytes; SHA256 `309f49c60598b88647fffa7b813f80addb3405d21859a46d1d9ac5de8b5ecc14`.

## The four exact text operations

1. The stale denial of openness is replaced by the relative-open-cone argument. Intersecting an open ample cone with the numerical restriction subspace \(V\) gives openness in \(V\). The existence of an ample class in \(V\) also gives nonempty interior for its nef cone. No surjectivity assumption is inserted.
2. The adjacent usage ledger now distinguishes nef-plus-ample, closedness, relative ample-cone openness for divisor rounding, and generic ample-cone openness in the positive-representative construction.
3. The refinement example now assumes neither affine function dominates the other throughout the face. Then both strict comparison regions are nonempty and the maximum cannot be affine on the whole face. The direction of the chord inequality remains correct.
4. The incorrect “Lemma 5.3” source locator becomes §5.2. Direct source inspection identifies its specific input as Lemma 5.7, so the broader section locator is accurate.

There are only two parent-to-revised Ch20 diff hunks (the adjacent first two operations combine) and one Ch21 hunk. No statement's hypothesis is broadened or narrowed by this revision, and none of the new central proof fragments is rewritten.

## Independent assembly and patch checks

VALIDATION.json records independent read-only checks of both stages:

- 19 author-manifest checks, including repeated source-chain entries, with no hash or byte mismatch.
- Original Ch20 labels 209→212, adding only the density lemma, uniform-maximum corollary, and irrational example. Original Ch21 retains all 172 labels.
- Revised1 retains all 212+172=384 labels, with no duplicates.
- Each of the three standalone core fragments occurs exactly once, with exact bytes, in both assembled Ch20 stages.
- The excluded Ch21 curve-retraction subsection up to the next section is unchanged from live source in both stages: 6996 bytes, SHA256 `0c319292e5ae9d50478d19b114383cf1ffb64e6487e5710a05b459690c402cd5`.
- The original saved raw comparison patches exactly match regenerated `git diff --no-index` output. Those absolute/dossier-header patches were not directly apply-checked.
- The revised saved portable patches exactly match regenerated cumulative `diff -u` output using the author-specified a/b live-chapter labels.
- **The actual saved revised portable patches**, without rewriting their bytes or headers, each pass `git apply --check` directly. Neither was applied.

These are cumulative patches from the live chapter files to revised1. In particular, Ch20's patch incorporates the prior weighted/unit-node parent work. It is not an incremental patch to apply after that parent or after the original real-model packet.

The current live files retain their pre-audit hashes: Ch20 `531024045204686aaf0fc12ff0e825bf67367551cd310a26c956740b4d164baa`; Ch21 `477db8e896633bcf5f89c8738e16e0afa8eaac55f36042c1d263b683daed72b3`. No author assembly script was executed; both were read completely. No live chapter, frozen packet, or prior audit was changed. No TeX build or production Rethlas submission was performed by this auditor.
