# Exact release manifest

Release: `p071_unbranched_polyhedral_complex_local_collapse_candidate_20260830`

Date: 30 August 2026 (Asia/Shanghai)

Status: **quarantined local theorem; independent exact-byte PASS; no
production submission; not a live-book input**.

## Principal mathematical bytes

| File | SHA-256 |
|---|---|
| `statement.tex` | `2bc8574fecdc46ecafc1e41f24608c6db60cb9e48f696204ef503a83bed0625e` |
| `proof.tex` | `ab3348d8d0dc31c4c661e1358f8b70894eff83890a3c6d6abc412810dea4ca30` |

The theorem is a local chart-transport consequence of the already
production-verified one-convex-polyhedron result.  It proves first-stage
collapse and one fixed-chart-neighbourhood decreasing approximation on a
finite face-to-face complex whose **complete generator germs** admit
generator-preserving convex developments.

## Companion records

| File | SHA-256 |
|---|---|
| `SOURCE_AND_OBLIGATION_MATRIX.md` | `915ec96b4c1bc8f191429f2ba75425a447b223c721121ef2510e8b396be1a619` |
| `EDGE_CASES_AND_OBSTRUCTIONS.md` | `27646456fe2a37d333afdab36e659ad4e06d0749eeedb9949c64737cc52098b3` |
| `README.md` | `fc95b3043d78e9961c275734c565b9d4d5fba67a92808ecdcb6827a780159dce` |

The independent final re-audit is deliberately stored in the sibling
directory
`p071_unbranched_polyhedral_complex_final_exact_reaudit_20260830`:

| Artifact | SHA-256 / verdict |
|---|---|
| `INDEPENDENT_EXACT_BYTE_REAUDIT_20260830.md` | `1f0abda081c5ddcd0eaf9ac11a895af2e6b1b6eaace2fadebd9cb8281a4fd4e2`; **PASS**, zero critical errors, zero proof gaps, zero definition/type gaps, zero source gaps |

The earlier hostile counterexample report on pre-repair bytes remains in a
separate sibling and is superseded for release verdict purposes.  Its only
formal blocker (the untyped generator datum) was repaired before the final
re-audit.

## Minimal build

| File | SHA-256 |
|---|---|
| `compile.tex` | `2bf7e9befecaa62da75f435d0ba8a3816a558cc2918ddf2e1e13ff83a6e71e24` |
| `compile.pdf` | `88608202d9e55759d52608f5203856d03d58399c4376569e8d06a0daac4f444c` |
| `compile.log` | `edf854fe00a81eb9d60fae1449a2212421b5ef8d42f448dae94d7d6b3f7ba01c` |

The final build has four letter-size pages.  The final log has no undefined
reference or citation, multiply defined label, overfull/underfull box,
warning, or TeX error.  An independent clean compile is separately pinned
in the final audit.

## Dependency identities

The exact model theorem remains:

- statement:
  `b46b8e22fa8b3f8f64dcf8ae24d164b905dbe8d9035e37c3ede23321717cc002`;
- proof:
  `37a3b6a12f6ddd2a3038dd926dfe8120d8955756efe64608fbd2a37b33c01efb`;
- production response:
  `c5871408ef86be152ecd6e169eaae05f590feef00e5487d37f185780951d5285`,
  verdict `correct`, zero critical errors and zero gaps.

The exact CLD PDF and layout extraction remain
`5690f999523017d184ab751bb55857ab1637b197d1186ad4fd2edba7e1bda719`
and
`021be260392de1f3240858d4c775da86653518dfab4fd9c4c21a2406081b6c7e`.
CLD Remark 1.9.15 and Definition 1.10.1 support the embedding-dependence and
cellwise-positivity firewall.

## Release decision and firewall

The strongest safely proved statement in this search is the local
generator-convex theorem.  The following stronger assertions were rejected:

- face-to-face plus codimension-one nonbranching is not sufficient;
- agreement on a common face does not supply cross-face Jensen inequalities;
- independent chamberwise smooth approximants are not shown to glue into a
  monotone sequence;
- loop monodromy does not obstruct the local sheaf result, but no single
  global sequence is proved;
- branched links, singular lower links, nonconvex complete germs without a
  generator-preserving development, and merely cellwise-positive generator
  sheaves remain outside the theorem.

Accordingly, this dossier narrows but does not retire unrestricted P07.1.
No production call or live-manuscript edit was made.
