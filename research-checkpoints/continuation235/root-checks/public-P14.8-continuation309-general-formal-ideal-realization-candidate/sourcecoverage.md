# Physical reading and source coverage

Literal LF indexing is `text.split('\n')`, never `splitlines()`. Form feeds are retained in records. Files ending in a newline therefore have one more record than their newline counts. The mathematical binding files used “LF_lines” as newline count in several entries; no source was silently reindexed or changed.

The complete preserved original-task.json was read as all JSON fields, with its problem string decoded into untruncated bounded chunks 1–95, 96–180, and 181–266, and its complete completionCriteria. A first combined tool output was truncated; it is not counted as complete reading. The decoded bounded rereads supply complete semantic coverage and are archived in LOCALONLY/. The complete family-08.txt was read in chunks LF1–90, LF91–180, LF181–255. The complete original atomic JSON was read. The complete working305 body, F0–F4 and every metadata field, was read both as a decoded object and literal bounded ranges LF1–30 and LF31–62. Its production/operational language was not executed.

## DPS original text

Version identity: arXiv math/0006205v2, 10 October 2000. Exactly the two bound private primary files were used. Full source identity is in source-inventory.json and the application ledger. Whole-PDF visual reading and publisher byte identity are expressly **not** claimed.

| Bounded physically read chunk | What it covers |
| --- | --- |
| LF1–70 | Version header, exp(−2φ), curvature convention, introduction context |
| LF360–445 | Immediate preamble, §2.2 definitions, **whole 2.2.1 and 2.2.2**, proof opening and Step 1 opening |
| LF446–505 | Step 1 cover, weighted Hilbert space, kernel formula, all three local estimates and their analytic attribution |
| LF506–565 | Complete local transfer/sketch with Hörmander weight, normalization and norm comparison |
| LF566–625 | Step 1 global gluing/end and changing-cover warning; Step 2 opening and coherent reduction start |
| LF626–685 | Step 2 coherent reduction/conclusion; Step 3 opening through extension norm estimate |
| LF686–735 | Step 3 tensor expansion, dyadic almost decrease, integral limit; Step 4 choice and upper-tail formula |
| LF736–775 | Step 4 envelope, analytic-set continuity and ideal comparison, Richberg finish, **whole Remark 2.2.13** |
| LF2382–2488 | Complete pertinent bibliography entries for De92/GR84/Hör66/Nadel/Nar66/OT87/Richberg and terminal version-print metadata; unrelated entries in those bounded chunks were read as context |

Every literal record LF404–775 is covered. This is checked by the author's range inventory, not merely asserted by a hash. PDF pages 10 and 12 were visually inspected at bounded resolution to check factors, logarithmic terms, and conjugations that the text extraction can lose. Pages 9, 13, and 14 were rendered locally but are not claimed visually read. Formula interpretation and the author's correction remain mathematical arguments, not visual-reading certification.

## Frozen book pertinent units

The complete chapters are not asserted physically read. The following pertinent statement/proof units and actual definitions were read; the program's detailed overlapping ranges are in source-read-log.jsonl/sourcecoverage.json.

- ch51 LF246–360: actual normalization, squared metric convention, all three tests.
- ch51 LF375–444: complete θ-psh definition and current/change-of-representative explanation.
- ch51 LF588–772: the contextual local example, complete compactness proposition/proof, complete Hartogs corollary/proof, complete Choquet corollary/proof. None is accepted merely because the book calls it proved.
- ch51 LF1440–1733: multiplier definition, all threshold arithmetic, complete formal ideal proposition/proof, threshold example, strong openness/valuative statement and all normalization/proof deductions. Integer-vs-real equivalence is not imported.
- ch51 LF1904–2069: analytic-singularity definition and complete rigidity proposition/proof; complete regularization theorem/proof and approximation definition; **complete erroneous qes-preserves-i proposition/proof LF2013–2059** and beginning of the following warning.
- ch51 LF3290–3566: complete I-preorder calculus, envelope definition, complete I-projection theorem including both proof versions, complete canonical reconstruction corollary/proof and explanatory warnings. Canonical recovery is not claimed from these data without independent input validation.
- ch51 LF3861–4098: complete polar Cantor lemma/proof, full example including raw mass/P discussion, complete no-I-mass corollary/proof and following zero-mass consequence. The paper proves a separate direct Cantor obstruction, avoiding the book's capacity import.
- ch71 LF1–105: introductory definitions and complete generic-fiber obstruction proposition/proof.
- ch71 LF144–270: complete ideal-valuative number and I-equivalence propositions/proofs and P/I firewall.
- ch71 LF2310–2352: complete terminal slice corollary/proof and scope explanation. The preceding theorem was not used as a premise.
- ch71 LF2398–2453: complete zero-volume boundary proposition/proof and end of preceding context. No zero-volume mass theorem is imported into the main criterion.

The erroneous frozen body is preserved **byte for byte for its LF unit** in LOCALONLY/ch51-qes-preserves-i-original-body.tex. The inputs remain unchanged. Long quoted source content stays local. The paper gives its own analysis and a corrected conditional formula separately.

## Bibliography boundaries

Complete relevant entries read: Hor66 LF2006–2021; Dem92reg LF2038–2050; DPS01 LF4061–4077; Nad90 LF4965–4981; Nad89 LF2770–2786; OT87 LF5684–5699; GZ15 LF5094–5110; GZ15b LF4504–4520; DEL00 LF4706–4723; Hor90 LF5854–5866. Some read chunks include starts of adjacent unrelated entries; those adjacent fragments are not used. The DPS references supply complete GR84 and Nar66 identities. A bibliography identity is not a full original statement or proof, and no such proof is claimed to have been read.

## Diagnostics and assurance limits

Initial combined original/family output and an overbroad search output produced truncation warnings; bounded rereads corrected the meaningful coverage. The inventory author's first program execution had a syntax error and is preserved in initial-inventory-failure.log; the corrected program checked all eight bound source hashes and the complete required DPS range. This success establishes extraction/integrity facts only. Source coverage, proof correctness, saved notes, and actual final delivery are different claims.
