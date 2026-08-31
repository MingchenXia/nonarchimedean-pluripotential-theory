# Sources, dependencies, and the exact verification boundary

Date: 1 September 2026. Author: /root.

## Primary sources read for this argument

1. Boucksom--Favre--Jonsson, *Singular semipositive metrics in non-Archimedean geometry*, arXiv:1201.0187v2. Root read Section 1.1 (original DVR, residue characteristic zero, vertical SNC resolutions), Section 2.4 (projective models with the same generic variety and common domination), Section 2.5 and Proposition 2.2 (vertical ideals and model functions), Corollary 2.3 (uniform density), Lemma 3.5(ii) and Proposition 3.6(iii) (determined-divisor equality and retention of old skeleta), and the full local monomial construction in Section 3.3. Root checked the primary PDF text directly, as well as the pinned local text. The normalization ell=1 in that source is replaced by ell=v(pi)>0 throughout this note. The sign of the truncated function is derived from I O=O(-E), not from a remembered sign convention.
2. Berkovich, *Smooth p-adic analytic spaces are locally contractible*, Invent. Math. 137 (1999), 1--84, DOI 10.1007/s002229900914. Root read the primary author PDF's definition of local contractibility and Section 9 scope/Theorem 9.1. It applies to the strict analytification of a smooth variety over the nontrivially valued original field and its ordinary opens. Here it supplies a path in W; no map used inside its proof is applied to the unknown current.
3. Chambert-Loir--Ducros, *Formes differentielles reelles et courants sur les espaces de Berkovich*, July 2025 revision, local text CLD25.txt. Root read Lemma 12.2.3 and its entire proof (local text lines 16808--16824), the preceding strict-perturbation observation, Section 12.9/Lemma 12.9.2 (lines 18120--18170), and the complete cutoff/partition statements and proofs 15.2.5--15.2.9 with the preceding locally holomorphically separated hypothesis (lines 21550--21640). The algebraic rational replacement is separately justified by density of Frac(A/ker(x)) in H(x), exactly as in the earlier capture note. The analytic functions are not asserted equal, only their tropicalizations and their resulting ordinary pullback forms on the strict-approximation neighborhood. Compact-set cutoffs do not require global paracompactness; the new note explicitly supplies sigma-compact smaller domains when R requires them.
4. For the geometric companions root also checked Stacks Section 33.47, Situation 33.47.2 and Lemma 33.47.3 (tag 0FD4), and the full statement/proof of Lemma 33.48.3 (tag 0FD9). Their use belongs to the separately authored ample-cut geometry, not to the new local-logarithm construction.

Primary links: [BFJ exact arXiv version](https://arxiv.org/pdf/1201.0187v2), [Berkovich author PDF](https://www.wisdom.weizmann.ac.il/~/vova/Inven_1999_137_contra.pdf), [CLD source](https://arxiv.org/abs/1204.6277), [Stacks Bertini](https://stacks.math.columbia.edu/tag/0FD4), [Stacks connected ample divisor](https://stacks.math.columbia.edu/tag/0FD9).

The primary PDF web text was inspected, not newly rendered. No PDF visual QA is claimed for this research dossier.

## Fixed local source identities

- BFJ PDF `/private/tmp/BFJ_singular_1201.0187_audit_20260831.pdf`: 768011 bytes; SHA256 `8b684713055b9147de0d3379ad925c58f031bafe10a77e769a2791cdaa128270`.
- BFJ extracted text `/private/tmp/BFJ_singular_1201.0187_audit_20260831.txt`: 175006 bytes; SHA256 `df3fa71656240742234907514956389d2f2533e20bb89cd877bd235a922e5f1f`.
- CLD extracted text `/private/tmp/CLD25.txt`: 2150944 bytes; SHA256 `021be260392de1f3240858d4c775da86653518dfab4fd9c4c21a2406081b6c7e`.

No local byte identity is invented for the Berkovich web PDF or the Stacks pages. The URLs, exact theorem identifiers and inspected scopes identify those sources.

## Research premises remain conditional

The new geometric endpoint construction, Sections 2--5, does not use the current premises L/O/Q/R. It uses the primary BFJ model framework and the elementary proofs written there.

The later coefficient and whole-current conclusions require the following separate research inputs. Their manifest identities are pinned by the accompanying freeze/check script; naming or hashing a file does not prove its mathematical contents.

- `p213_saturated_open_model_propagation_research_20260901`: separately authored by /root/p082_independent_reaudit. Exact note SHA256 `a77fe9f80d2da71d1c9c81163955808736b38508f49da76f0cf8ad8d81fdbefc`; manifest `0b3abe46b75019f87f2e8a7206ccd6b98f729ff9c59caacdc9bfac4665f4be91`. Supplies full ordinary superlevel saturation on all higher determinations, original-field vertical star augmentation and preservation of old chamber/curve witnesses. Root read its complete proof and source ledger. The boundary components are indexed separately for each component restriction; connectedness of the entire crossing boundary is not an indexing convention.
- `p213_stratum_incidence_controlled_chambers_research_20260901`: separately authored by /root/p213_skeletal_hostile. Exact frozen note SHA256 `30d3d66a465dd51e488fa7f4b440aa2d083fc1640bd331fa61a1472acab5df34`; manifest `a250bf5f9e2473433cb078fd58261d0fab401446cf1b6546e761faa75565dcd3`. Supplies the closed proper-stratum incidence graph, positive-vertex retraction, finite parent-before-child assembly, actual-subdivision preservation and degree-accurate current overlap. Root read the complete draft and the final corrected source/argument passages before pinning this version. Its current application uses n>=2, the scope of O; its pure geometric parts may have a wider range.
- L: `../../solver_dossiers_20260831/p213_nonreduced_tube_finite_projection_research_20260831/RESEARCH_NOTE.md`, SHA256 `3001c94985c0d3e60f184ffd9f0e9591775ea026a98cd20ee538005edac11b7a`. On the actual analytic hypersurface, finite proper projection, independent-radius single source and canonical multiplicity/residue degree are used. Root reread its exact analytic statement. L itself does not identify an arbitrary model tube with that hypersurface. Root authored L earlier; that fact is disclosed, not an independent acceptance of it here.
- O: `../../solver_dossiers_20260831/p213_ordinary_open_outer_collar_research_20260831/RESEARCH_NOTE.md`, SHA256 `f629a77106d023763c7b99626c1ec1f8f449164f3749de475bf18bb0661e1d5b`. Root reread Sections 1--4, including the completed-ring/formal-tube interface in Section 2 that precedes applying L; the new note repeats its maximal-point algebraic check. The finite compact principal-divisor tests on whole proper residual curves remain supported in W; the model/saturation construction does not replace that analytic proof.
- Q: `../p213_proper_target_open_comparison_20260901/RESEARCH_NOTE.md`, SHA256 `35d4ae59a167025ef595aa50a45101619ed1aef586be39abebca1486c62857ec`. Root read this entire source during the present turn. It compares q-based tests with arbitrary compact ordinary source multipliers on a full inverse image of a connected target open. It does NOT already assert equality for all other moments. Root authored Q earlier; the new endpoint comparison in Section 7 is a separate argument, not a relabeling of Q's scope.
- Displayed R: `../../solver_dossiers_20260831/p213_skeletal_packets_20260831/skeletal_representation/statement.tex`, SHA256 `5c06cd6f091e5964a16c07b3efddd2104fed938447605f4f9b19ff8dfea01f1a`. Root read the complete statement. ONLY the displayed source-cell representation with constant coefficients, arbitrary compact smooth source multipliers, locally finite compact cells and no lower-cell residual is assumed. The full source-representation proof and its rejected stronger source-separation wording are not accepted by this note.

## Related work that is not used as a hidden same-X input

Root reread the earlier `p213_maximal_rank_source_cell_capture_research_20260901/RESEARCH_NOTE.md` (SHA256 `4cc25ff627af56aca05c8733e3e5bff65aea21015abe35e49726f9966bb1b384`) and `p213_source_cell_residual_curve_access_v2_20260901/RESEARCH_NOTE.md` (SHA256 `177d7ea0e2f5fd1cde5e9539b4cd88ce90623a1ee78202f9050b08cb00130d96`). They explain the previously unresolved generic-birational-model interface and the finite-leading-term and rational-replacement mechanisms.

The new proof does NOT identify their generic Y with X or assume their access models share the same generic fibre. It replaces that part by vertical truncation ideals and applies model theory directly to X. The earlier methods are acknowledged as background; the new complete proofs of the needed elementary steps are included.

## Exact nonclaims

- Independent review of the two geometric companions is not independent review of this newly authored endpoint proof.
- Neither kind of independent model review is production Rethlas verification, formal certification, or a novelty/priority decision.
- The conditional equality T=c delta_W is not a proof of its unverified source representation premise R. Without R, Sections 7--9 do not give the asserted arbitrary-source and all-top-form comparisons.
- No live theorem is promoted, no open item is retired, and no claim of a general envelope-property solution is made by this dossier.
