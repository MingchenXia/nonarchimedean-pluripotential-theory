# P07.1 double-node support-plane reduction: live build report

Date: 2026-09-20

## Mathematical and editorial checks

- Local model-backed verification with `gpt-6-astra` at `xhigh` returned
  final `correct`, with `0` critical errors and `0` gaps.
- Checked item: `pi_34acd32abc0bfae9990b71d7`.
- Strict exact-current receipt audit against the independently inspected
  verifier source: `PASS`.
- Strict Mingchen-writing audit on the principal statement and proof: `0`
  errors and `0` warnings.
- Principal statement SHA-256:
  `12b983557fd9a0da9665170a5423275412230b334cd003cbe8559f7b3344a1d9`.
- Principal proof SHA-256:
  `ec523a5fbe05d10ddc5d905eb80da4f2ba89c02c3282f16373fe6ed3fa95b573`.
- The automatic second reading rechecked the moment--barycentre
  equivalence, the extreme-point support bound, the collarwise convex
  envelope, compactness of the dual feasible set, the nested-intersection
  passage to the open chart, and affine independence of the sharp
  five-point configuration.  It found and removed one stray plus sign
  between two convex-envelope constraints.  The corrected exact bytes were
  then reverified; no further revision was required.

## Structural checks

- Open-problem inventory audit: `PASS_OPEN_PROBLEM_INVENTORY`; `46` active
  atoms across `14` Chapter 72 environments, with tiers `T1=0`, `T2=5`,
  `T3=8`, `T4=16`, `T5=17`.
- Build-closure reference audit: `387` files, `11,456` labels, `0`
  multiply defined labels, `0` dangling references, and all per-file
  structure checks clean.
- The final build log contains no unresolved-reference, citation,
  multiply-defined-label, or rerun warning.
- No box warning occurs while the new principal statement or proof is read.
- `git diff --check`: clean.

## Full-book build and visual inspection

- Full `latexmk` build: success; all targets are up to date.
- Artifact: `manuscript/book.pdf`, PDF 1.5, letter size, `3,391` pages,
  `17,925,182` bytes.
- Final PDF SHA-256:
  `5d6a2768cc1eb05c208eda6b5d9c115fba0ad665a6ffda5e52793b904044610d`.
- Final log SHA-256:
  `5e3c9816add6bb6f8a27f4057d92347abb096b3367d42500d542d6162c8e8975`.
- The new Chapter 16 statement and proof occupy printed pages `831--834`
  (physical PDF pages `899--902`); physical page `903` was also checked for
  the transition to the following proposition.
- The Chapter 72 status integration occupies printed page `3141`
  (physical PDF page `3209`).
- The Appendix L provenance record occupies printed pages `3292--3293`
  (physical PDF pages `3360--3361`).
- All eight affected physical pages were rendered from the final full-book
  PDF and inspected at source resolution.  Equations, page breaks,
  headings, cross-references, and margins are clear, with no clipping,
  overlap, duplicated wording, stray operator, or malformed glyph.

## Scope outcome

- The complete finite balanced double-node Jensen family has support rank
  five and is equivalent to one ambient affine minorant touching at the
  double node.
- The bound five is sharp for balanced-barycentre representation.
- This removes infinite atomic support as the residual local mechanism but
  does not prove sufficiency for the generated sheaf.  P07.1 therefore
  remains active, and the global active-atom count is unchanged.
