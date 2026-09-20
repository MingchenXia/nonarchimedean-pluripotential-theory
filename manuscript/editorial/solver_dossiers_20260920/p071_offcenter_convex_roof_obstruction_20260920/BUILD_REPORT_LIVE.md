# P07.1 off-centre convex-roof obstruction: live build report

Date: 2026-09-20

## Mathematical and editorial checks

- Local model-backed verification with `gpt-6-astra` at `xhigh` returned
  final `correct`, with `0` critical errors and `0` gaps.
- Checked item: `pi_d4506c7b32b78fce239673a8`.
- Strict exact-current receipt audit against the archived verifier source:
  `PASS`.
- Strict Mingchen-writing audit on the principal statement and proof: `0`
  errors and `0` warnings.
- Principal statement SHA-256:
  `8d97947f837ea1b4c306e44040371ca313c158ae92f37c0f2faa31ea12fd4d70`.
- Principal proof SHA-256:
  `068e16e7e4a07c0865facec516b192893dbbb7ee0a14f89c6b681c553904147a`.
- A complete automatic second reading rechecked the common axis restrictions,
  the two slope-balance laws, all nine Hessians, both ambient barycentre
  coordinates, the five exact function values, and the Jensen defect
  `7169/688`.  No further revision was required.

## Structural checks

- Open-problem inventory audit:
  `PASS_OPEN_PROBLEM_INVENTORY`; `46` active atoms across `14` Chapter 72
  environments, with tiers `T1=0`, `T2=5`, `T3=8`, `T4=16`,
  `T5=17`.
- Build-closure reference audit: `385` files, `11,451` labels, `0`
  multiply defined labels, `0` dangling references, and all per-file
  structure checks clean.
- The final build log contains no unresolved-reference, multiply-defined,
  citation, or rerun warning.
- `git diff --check`: clean.

## Full-book build and visual inspection

- Full clean `latexmk` build: success; all targets are up to date.
- Artifact: `manuscript/book.pdf`, PDF 1.5, letter size, `3,387` pages,
  `17,910,443` bytes.
- Final PDF SHA-256:
  `5e5aecc3215da84d583b3a23246ed9bf2c23be26a5e5f657d1d40f36d04610f5`.
- Final log SHA-256:
  `da556355cc4465675b87559486cbfbf2a296818d66872bbafa7687d90266722b`.
- The new Chapter 16 statement and proof occupy printed pages `831--834`
  (physical PDF pages `899--902`).
- The Chapter 72 status integration occupies printed page `3137`
  (physical PDF page `3205`).
- The Appendix L provenance record occupies printed pages `3288--3289`
  (physical PDF pages `3356--3357`).
- All seven affected physical pages were rendered from the final full-book
  PDF and inspected at source resolution.  Equations, page breaks,
  cross-references, and margins are clear, with no clipping, overlap, or
  malformed glyphs.

## Scope outcome

- The example disproves the unrestricted ambient-barycentric convexity of
  the full generated two-star sheaf, already at the stage-zero generator
  level.
- Hence an ambient convex-roof extension cannot prove sufficiency of the
  mixed double-node conditions.
- The example does not contradict the proved double-node inequality and
  does not settle its sufficiency.  P07.1 therefore remains active, and the
  global active-atom count is unchanged.
