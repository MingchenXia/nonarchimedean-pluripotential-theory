# Revised1 addendum: exact-byte mathematical and assembly review

Date: 2026-08-31. Reviewer: /root/p082_independent_reaudit.

PASS within the bounded repair scope of ORIGINAL_REVISION_AUDIT.md.
The original report, source matrix, checker and SHA256SUMS.original were
frozen before this addendum. They remain unchanged. The original report's
provenance limitation and gate exclusions apply without modification:
this is not a wholly fresh review of the reviewer's own repair ingredients,
not an audit of every claim in either chapter, and not production acceptance.

## Exact revision

Reviewed directory:
/private/tmp/nappt_p071_20260827/manuscript/editorial/solver_dossiers_20260831/
p081_ch20_ch21_real_model_max_repair_20260831/revised1.

| Artifact | SHA256 |
| --- | --- |
| patched/ch20_model_forms.tex | 3f2814e440f738708c084ee186a06e0930c0d48db89e80db1f21e7300e373ca2 |
| patched/ch21_bfj_psh.tex | ae6f71cd7db4c21108fb975e159ccaacf76d7f7251978224f7ac70886168769f |
| MANIFEST.json | 309f49c60598b88647fffa7b813f80addb3405d21859a46d1d9ac5de8b5ecc14 |
| ch20_model_forms.patch | 5b70d68f29b2a5be0c085a48a71b7f9257c0fcd0934712249bb041cac7a810e5 |
| ch21_bfj_psh.patch | dbd51e8360bc49bcf94eb2bcf89b235b3a9b9d234e35cbbff2a8640cb2f022e1 |

## Four changes checked in full

1. Relative ample-cone openness. The numerical subspace V is not identified
   with the entire special-fibre numerical space. Its ample cone is the
   intersection with that ambient open cone, hence is open in V. Because
   it contains an ample class, the relatively nef cone has nonempty
   interior. This removes the contradictory denial without altering the
   fixed-theta density lemma or adding a hypothesis to it.
2. The cone-usage explanation now distinguishes nef-plus-ample, closedness,
   relative openness for coefficient rounding, and generic openness for
   the positive-representative construction. These are precisely the
   different uses checked in the original audit. Surjectivity of the
   restriction map is unnecessary.
3. Non-affineness of a maximum is now qualified by genuine crossing on a
   face: neither input dominates throughout that face. Under this condition
   the maximum is not affine; the inequality below its vertex interpolant
   has the correct sign. Equal or globally ordered affine inputs are no
   longer incorrectly included in the obstruction.
4. The Ch21 relative-ideal approximation citation now points to BFJ
   Section 5.2, which contains Lemma 5.7 in the exact source version
   listed in SOURCE_MATRIX.md. The old specific Lemma 5.3 locator is gone
   from this sentence. The mathematical approximation text is unchanged.

Thus all three precision notes of the original report are resolved.
There is no new substantive mathematical gap in these four replacements.
All original core conclusions remain as checked: arbitrary real theta for
rational maxima; ample generic class only for fixed-form density and
rational/real envelope-supremum equality; no directedness assertion for the
full real-model obstacle family; and rational replacement in the Ch21
skeletal and full-PSH maximum arguments.

## Exact assembly and preservation checks

The read-only check_revised1.mjs verifies all revised manifest entries,
checks both parent hashes, replays only the four in-memory replacements,
and reproduces both revised chapter files exactly. All three original
core Ch20 proof fragments are still present verbatim, exactly once.
The original-to-revised full diffs were read and contain exactly the
four recorded replacements, with no additional chapter changes.

The complete ordered label lists are unchanged from the original repaired
chapters: Ch20 has 212, Ch21 has 172. All 209 weighted-parent Ch20 labels
and all 172 live-parent Ch21 labels consequently remain present. No new
duplicate label or control byte was found. The replacements introduce
no new environment boundaries; the original balanced environment counts
are therefore unchanged.

Both revised portable patches equal fresh cumulative diffs from the live
chapters with relative a/manuscript/... and b/manuscript/... headers.
Independent git apply --check succeeded for each patch. Neither patch
was applied. The original absolute-path comparison artifacts were not
rewritten. Cumulative Ch20 patch contents still include the inherited
weighted-parent changes, whose independent mathematical gate is separate.

All 13 entries in SHA256SUMS.original passed after the original report
freeze. The final SHA256SUMS binds that frozen manifest and this addendum
to the revised targets. No candidate or live edits, production calls,
compilation, PDF visual-QA, or new-priority claims occurred.
