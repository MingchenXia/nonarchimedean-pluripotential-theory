# Second reading and sequential research programme

Date: 2 October 2026. User-authorized continuation after completion of the
editorial second draft in commit `f0d7942`.

## Objective and controlling instructions

Read the entire book again from the beginning and polish its coherence and
readability. Resume attempts on the active open problems one by one using
[Xean](https://github.com/chaoxu/xean) and `gpt-6.1-sol` at `xhigh` reasoning.
This instruction supersedes the previous pause on independent research.
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

Current reading position: Chapters 1 and 2 pass the new source, build,
reference, and rendered-page gates; see the
[Chapter 1 audit](second_reading_ch01_audit_20261002.md)
and [Chapter 2 audit](second_reading_ch02_audit_20261002.md).
Chapter 3 source reading is complete and its editorial repairs are next.
No later chapter is marked reread.

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

The user now explicitly requests the local Codex subscription for execution.
The installed Codex CLI is confirmed logged in through ChatGPT, rather than
an API key. Its model smoke fails before inference because its managed state
path is read-only, and this cloud chat has no attached local app terminal.
Xean's Pi roles do not automatically inherit native CLI login. Supported
subscription integration is being investigated; no API-key substitution is
assumed. These are infrastructure states, not mathematical failures or
verifier findings. The reading pass continues independently.
P02.1 has been initialized with frozen task and settings, zero admitted model
calls, and no generated mathematical notes. No Xean mathematical campaign
has yet run, and no new problem is solved.

GitHub default-branch publication remains pending the previously requested
explicit approval. This continuation grants no new push approval.
