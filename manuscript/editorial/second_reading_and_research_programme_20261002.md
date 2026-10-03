# Second reading and sequential research programme

Date: 2 October 2026. User-authorized continuation after completion of the
editorial second draft in commit `f0d7942`.

## Objective and controlling instructions

Read the entire book again from the beginning and polish its coherence and
readability. Resume attempts on the active open problems one by one using
[Xean](https://github.com/chaoxu/xean) and `gpt-6.1-sol` at `xhigh` reasoning.
This instruction initially superseded the previous pause on independent
research. Subsequent user steering suspends Xean setup and requires all
current execution to remain in the cloud. The active work is the complete
book rereading and polishing pass; the prepared research queue remains
historical preparation, with no new solved status.
The earlier completion manifest, source ledger, PDF, source package, audits,
and verifier receipts remain records of that completed edition.

## Reading pass

Read Chapters 1--72 in order, then Appendices A--N, and finish by reconciling
the preface, conventions, and six part introductions with the revised body.
For each unit, check the roadmap against its actual content, dependencies
against preceding definitions, notation and normalization at every interface,
and the continuity of examples and arguments. Repair ambiguous prose,
unnecessary repetition, unsupported scope, and misleading reading routes.
Retain precise proofs, source boundaries, and extended-real/net conventions.
Read active input fragments with the chapter using them; identify reuse of
unchanged proof/source evidence without calling that a fresh independent audit.

Compile and inspect the changed pages before closing each verified unit.
Repeat the reference and relevant scope checks after rendering. Chapter
checkpoints are milestones; the goal is the complete rereading pass.

Current reading position: Chapters 1--19 pass the new source, build,
reference, and rendered-page gates; see the
[Chapter 1 audit](second_reading_ch01_audit_20261002.md),
[Chapter 2 audit](second_reading_ch02_audit_20261002.md),
[Chapter 3 audit](second_reading_ch03_audit_20261002.md),
[Chapter 4 audit](second_reading_ch04_audit_20261002.md),
[Chapter 5 audit](second_reading_ch05_audit_20261002.md),
[Chapter 6 audit](second_reading_ch06_audit_20261002.md),
[Chapter 7 audit](second_reading_ch07_audit_20261002.md),
[Chapter 8 audit](second_reading_ch08_audit_20261002.md),
[Chapter 9 audit](second_reading_ch09_audit_20261002.md),
[Chapter 10 audit](second_reading_ch10_audit_20261002.md),
[Chapter 11 audit](second_reading_ch11_audit_20261002.md),
[Chapter 12 audit](second_reading_ch12_audit_20261002.md),
[Chapter 13 audit](second_reading_ch13_audit_20261002.md),
[Chapter 14 audit](second_reading_ch14_audit_20261002.md),
[Chapter 15 audit](second_reading_ch15_audit_20261003.md),
[Chapter 16 audit](second_reading_ch16_audit_20261003.md),
[Chapter 17 audit](second_reading_ch17_audit_20261003.md),
[Chapter 18 audit](second_reading_ch18_audit_20261003.md), and
[Chapter 19 audit](second_reading_ch19_audit_20261003.md).
Chapter 16's original 5,753-line source and all 83 direct inputs were freshly
read. Its product construction, proof interfaces, examples, harmonic
compatibility and source scopes were repaired; all 274 chapter pages and two
seams passed visual review. All original input bytes are preserved; four
reader copies repair typography, the empty finite-set case and pagination.
Chapter 15's earlier real-coefficient
LFS descent correction and affected Chapter 72 scopes are also recorded in the
[3 October correction audit](ch15_lfs_descent_scope_correction_audit_20261003.md).
Chapter 17's original 4,813-line main source and all seven inputs were
freshly read. Metric classes, residual constructions, curvature and formal
comparison, polar extensions and detection scopes were repaired. All 88
chapter physical pages and two seams passed visual review; the seven input
files remain byte-identical.
Chapter 18's original 4,527-line main source and all nine inputs were freshly
read. Polyhedral corner formulas, measure proofs, positivity, harmonic charts,
curve tests and model comparisons were reconciled with their source and base
field hypotheses. All 92 chapter physical pages and two seams passed visual
review; all nine input files remain byte-identical.
Chapter 19's original 4,479-line main source and all four inputs were freshly
read. Toric approximation and support, abelian harmonic products and relative
fibre currents, the BFJ common locus and singular limitations were reconciled
with their exact source and field hypotheses. All 74 chapter physical pages
and both seams passed visual review; all four input files remain
byte-identical. Chapter 20 is next. No later chapter is marked reread.

The user's standalone catalogue is complete: [LaTeX source](../../output/open_problems_catalogue_2026-10-02.tex),
[85-page PDF](../../output/open_problems_catalogue_2026-10-02.pdf), and
[audit](open_problem_catalogue_audit_20261002.md). All 42 active items in
twelve families retain their exact scopes, known cases, obstructions,
completion criteria and references. Its general literature cutoff is
24 August, targeted updates reach 19 September, and dated verification and
supplied-source integrations reach 26 September. It claims no new literature
search or solution. The source compiles in the built-in editor; all 85 pages
and the final internal navigation were checked.

The first repairs distinguish affine analytification from a compact affinoid
spectrum, state integrality where the valuation cone has one trivial vertex,
retain boundedness/energy conditions for filtration constructions, and replace
an unrestricted comparison promise by the book's proved domains. The reader's
guide now includes Chapters 70--72 and avoids sending complex readers through
Chapters 60--62 twice. Examples and formal theorem/proof environments remain
unchanged.

## Sequential problem queue

Use the exact ordered identifiers in
[the active inventory](open_problem_atomic_inventory_20260824.md): 42 atoms
in twelve formal problem environments, tier totals (0, 3, 7, 15, 17).
Begin with P02.1, then P02.2, P02.3, P02.4, and continue in inventory order.
Work on one problem campaign at a time. A serious unsuccessful attack remains
an open problem; partial progress is recorded with its exact scope and does
not retire the atom or satisfy the full problem's completion criteria.

For each campaign, freeze the task, completion criteria, settings, source
revision, and runtime version. Preserve mathematical notes and failed routes.
Separate exploration, source checking, requirements, reconstruction, and
independent adversarial review. The requested `gpt-6.1-sol`/`xhigh` applies
to new campaign profiles and research calls; historical model names and
settings remain unchanged.

Xean acceptance alone does not promote a new theorem into the manuscript.
Keep candidates outside the active TeX closure until the repository's
[verification protocol](rethlas_verification_protocol.md), primary-source
locator checks, boundary tests, receipt requirements, and integration audit
are satisfied. Never convert a failed, conditional, or unrun attempt into
a solved status.

## Runtime and current execution state

Xean source checkout: `/workspace/xean`, commit
`548fbf5b40dea325aa0d762ee091b1ab84a0c88a` (3.0.0 candidate).
Pinned runtime: Bun 1.4.2 in `/workspace/tool-runtimes/bun-v1.4.2/`.
Frozen dependency installation succeeds. CLI version and help succeed;
the deterministic kernel smoke returns completed/result 25.
The pinned Pi catalog contains the requested `openai/gpt-6.1-sol` model.

The latest user instruction is to ignore the Xean setup issue and continue
execution exclusively in the cloud. Xean setup and local-machine startup
are suspended. The earlier subscription investigation is retained as
infrastructure history: Codex is ChatGPT-subscription authenticated, but its
native model smoke failed before inference on the read-only managed state
path, and Pi roles do not automatically inherit native CLI login. No
API-key substitution or further local-machine setup is being pursued.
The authorized whole-book reading and polishing pass continues in the cloud.

P02.1 has been initialized with frozen task and settings, zero admitted model
calls, and no generated mathematical notes. No Xean mathematical campaign
has yet run, and no new problem is solved.

GitHub default-branch publication remains pending the previously requested
explicit approval. This continuation grants no new push approval.
