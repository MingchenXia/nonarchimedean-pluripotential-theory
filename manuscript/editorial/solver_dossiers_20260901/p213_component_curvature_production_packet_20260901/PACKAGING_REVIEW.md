# Packaging review: exact restricted production target

Date: 1 September 2026. Packager: /root/p213_skeletal_hostile.
This is an extraction and scope-equivalence review, NOT a new independent mathematical audit or a production receipt.

## 1. Source and prior independent acceptance

Frozen source:
../p213_approachable_component_curvature_research_20260901/RESEARCH_NOTE.md
SHA256 4c5167ee3f51e2c1b0307fedc0c7d351a026f6352a2f89f56fae73b7d0d610f1, 17469 bytes.

Fresh independent audit:
../p213_approachable_component_curvature_fresh_audit_20260901/AUDIT.md
SHA256 d9fb638af49c87197971e9358b47bab77844cb16bbcf6ea4b670029b5eb1dc2e, 32101 bytes.
Its reviewer is /root/p213_general_propagation_fresh_audit; the proof author is /root. The audit expressly accepts (I), Section 4.1 and its one-sided/local-A specialization without scalar classification. Its separate acceptance of (II) is outside this package.

The packager had earlier suggested the positive-common-curvature refinement, and authored a separate later weighted-CPsh research candidate. Accordingly this packaging review is not presented as another independent proof review. The earlier named fresh audit is the independent mathematical review. The later weighted candidate is neither copied nor imported here.

## 2. Character-for-character extraction

PROOF.md is exactly the concatenation of two UTF-8 substrings from the pinned source, with no inserted wrapper and no edited mathematical or boundary sentence:

| Source part | Source lines, inclusive | UTF-8 byte interval, zero-based and end-exclusive | Bytes |
|---|---|---|---:|
| Start at Section 1 heading; stop immediately before "(II) Retain" | 7–22 | [524,2492) | 1968 |
| Start at Section 2 heading; stop immediately before the Section 5 heading | 31–114 | [3577,13804) | 10227 |

All original separator newlines in both intervals remain. Here the Unicode-scalar character intervals equal the byte intervals because these two source substrings and their preceding text are ASCII; EXTRACT_MAP.json records both conventions explicitly. Total extracted proof: 12195 bytes, SHA256 b0d74bf26276199f4e03da2ef18b78698ecf4cda93ede2a576df0a73b3116255.

The first block contains the definition of A, its explicit decreasing-subsequence justification, usual strictness, the statement of (I), and its field-scope disclaimer. The second contains ALL of Sections 2, 3, 4 and 4.1, including the source-nullity input, coefficient pushforward, component support proof, positive common-curvature domination, and sufficient conditions. Section 5 and all of (II) are excluded. The source title/status preamble mentioning classification is also excluded.

The checker reconstructs the exact substrings from the frozen source, compares the concatenation with PROOF.md, and checks the stored byte/character/line boundaries and segment hashes. No lossy whitespace normalization or retyped proof is involved.

## 3. Equivalence of the separately written statement

STATEMENT.md reorganizes, but does not strengthen, the selected source conclusions:

- Its ambient assumptions and definitions reproduce source (I): any complete K, good separated usual-strict boundaryless pure dimension n>=1, actual reduced components and positive generic multiplicities.
- Its first target is exactly source equation (1.1) for both potentials in A.
- Its second target is exactly Section 4.1 for arbitrary continuous CPsh potentials with equal canonical curvature AND the explicit crossing-nullity hypothesis.
- Its one-sided A, ordinary-local A-potential, and zero-curvature sufficient conditions are exactly the last two paragraphs of Section 4.1.
- It excludes the narrower-field scalar-current consequence and any unconditional all-CPsh nullity theorem.

No every-open usual-strict inheritance over a trivially valued field is added. Local source calculus and local A-potentials are used in the same sense as the frozen proof and its independent audit.

## 4. Retained historical language and reference check

The source heading "the two different field scopes" and sentence "Here are the two proposed conclusions" remain in the exact first extract, although only (I) is submitted. They are historical organization, NOT a second target or a missing proof requirement.

The last paragraph of Section 4 compares the new proof with a "preceding frozen classification note". This is a boundary explanation of what analytic nullity adds; no assertion of that classification is used. The current package does not pin or import the classification theorem. The original source ledger and manifest are pinned only to identify provenance; their records of (II) dependencies are not mathematical inputs of this restricted proof.

Section 2 says the m=1 source is used on reduced component spaces; Section 4.1 also applies m=1 to the possibly nonreduced ambient X or retains its positive multiplicities. The original ledger and fresh audit explicitly check this additional ambient use. The sentence in Section 2 is not interpreted as prohibiting the later application, and no source byte is silently corrected.

All mathematical numbered cross-references retained in PROOF.md resolve inside it: (1.1), (3.2)–(3.5), (4.1)–(4.4), and Sections 2–4.1. No proof step refers to the excluded equation (1.2), Section 5, or conclusion (II). No substantive dangling mathematical dependency was found.

## 5. Complete classification-free source boundary

The mathematical inputs are exactly these known interfaces:

1. Ducros's analytic irreducible components, closed analytic unions, G-local finiteness, and dimension drop for proper analytic intersections. In the good setting a compact set is covered by finitely many affinoid neighborhoods, giving finiteness for each compact test.
2. Finite closed immersions, relative boundary, ordinary pullback of smooth forms/functions, topological properness, and positive closed integration.
3. CLD's fundamental-cycle identity delta_X=sum m_i delta_i, including nonreduced generic lengths.
4. Positive-current Radon coefficient measures, local positive test decomposition, compact cutoffs/density, continuous multiplication and proper pushforward.
5. CLD 8.5.5 positivity for the full uniform-closure CPsh sheaf, proved by its least-subsheaf argument; no direct smooth sequence for the arbitrary second potential is assumed.
6. CLD 16.9.4 analytic nullity ONLY for locally approachable continuous potentials. Its weighted estimate is an established source input, not a theorem rederived in this package.

Primary bibliography: Chambert-Loir–Ducros, *Formes differentielles reelles et courants sur les espaces de Berkovich*, https://arxiv.org/abs/1204.6277v2 ; Ducros, *Les espaces de Berkovich sont excellents*, AIF 59 (2009), https://www.numdam.org/article/AIF_2009__59_4_1443_0.pdf . This package does not claim a new primary-source PDF inspection; it preserves the exact independent audit's checked interfaces.

The fresh audit disclosed the CLD 8.4.2 k=n factor-two typo. The extracted proof asserts no such derivative identity and imports the first-stage nullity theorem in its stated scope. This source caveat is retained explicitly here; it is not repaired by silently importing the later full-CPsh candidate. If the production reviewer requires a rederivation of an imported source theorem, that is a further review obligation, not an unstated extra premise satisfied by the packager.

## 6. Service and status

Prepared for root's actual production submission. The intended mathematical payload is STATEMENT.md and PROOF.md, with this packaging/source clarification available as context. The service's supported sequential Markdown three-key response protocol is to be retained by the submitting operator; this package does not specify a new protocol, strict0.2 schema, endpoint, model, or server configuration.

No HTTP request, Rethlas call, service restart/change, git action, live edit or frozen-source edit was performed. The byte checker is read-only. A successful checker result is not a service result. Production acceptance remains pending until an actual receipt reviews these exact statement/proof bytes.

