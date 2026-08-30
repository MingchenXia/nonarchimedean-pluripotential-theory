# Independent exact-source recheck and v2 release audit

Date: 30 August 2026 (Asia/Shanghai)

## Audit target

This recheck concerns the source-only sibling release
`p071_stone_polyhedral_corners_v2_20260830`.  It does not reassess novelty or
priority and is not a production Rethlas verdict.

The principal mathematical bytes are:

- `statement.tex`:
  `b46b8e22fa8b3f8f64dcf8ae24d164b905dbe8d9035e37c3ede23321717cc002`;
- `proof.tex`:
  `37a3b6a12f6ddd2a3038dd926dfe8120d8955756efe64608fbd2a37b33c01efb`.

Direct `cmp -s` comparisons against the v1 files returned exit status zero
for both files.  They were not edited during this recheck.

## Exact-source reconstruction

The PDF present at `/private/tmp/CLD25_1204.6277.pdf` has SHA-256

`5690f999523017d184ab751bb55857ab1637b197d1186ad4fd2edba7e1bda719`.

Its title page identifies Chambert--Loir--Ducros,
*Formes différentielles réelles et courants sur les espaces de Berkovich*,
arXiv:1204.6277v2, dated 25 July 2025.  `pdfinfo` reports 608 unencrypted A4
pages.

The command

```text
pdftotext -layout /private/tmp/CLD25_1204.6277.pdf \
  /private/tmp/CLD25_reextracted_layout_p071_20260830.txt
```

produced a file with SHA-256

`021be260392de1f3240858d4c775da86653518dfab4fd9c4c21a2406081b6c7e`.

The navigation extraction actually used in the audit,
`/private/tmp/CLD25.txt`, has the same SHA-256.  `cmp -s` returned exit
status zero, establishing byte-for-byte equality.  The old v1 PDF hash
`f659...` is therefore neither needed nor retained in the v2 source ledger.

## Source-content checks

The regenerated exact extraction contains the following source obligations:

1. line 2165, CLD §1.8.2: the standing `(Q,R)` convention;
2. CLD §§1.8.3--1.8.10: cells, polyhedra, and parlinear subspaces;
3. lines 2392 and 2473, CLD §§1.9.3--1.9.6: local ambient restriction of
   smooth functions and forms;
4. line 2628, CLD Definition 1.10.1: cellwise positivity;
5. line 7045, CLD Example 6.1.4: induced affine structure on a parlinear
   subspace;
6. line 7069, CLD Definition 6.2.1: smooth forms/functions on an affine
   tropical space;
7. lines 9723 and 9757, CLD Definition 8.1.1 and Lemma 8.1.4: the psh
   hierarchy;
8. lines 11236--11273, CLD §§9.1.1--9.1.4: product structures.

For a convex rational polyhedron, the maximal cell spans
(A=\operatorname{Aff}(P)).  Thus CLD's cellwise positivity condition for
(\mathrm d'\mathrm d''F) is exactly positive semidefiniteness of the
Hessian on (A), including at faces and corners.  The source therefore
supports the compatibility paragraph in the frozen statement and proof.

The legality of the locally constant Stone factor is independently bound to
the verified Stone--Euclidean packet.  Its frozen proof has SHA-256
`9316e1a9df86c73a68ec099d3254e451ceaaac17a15c2a92441ad44961d863f6`,
its independent audit passed, and its production response has SHA-256
`ef9be00d4ed1462f11068a2b99a2c7fbe366af2b3bd180850b6763db541c3d6a`
with verdict `correct`, zero critical errors, and zero gaps.

## Mathematical carry-forward

The v1 hostile audit bound the same statement/proof hashes and found zero
critical mathematical errors and zero proof gaps.  Its report has SHA-256
`1d74c658835a2a9459350bc7e4509b7fbed3686b2c9bde9d31f24465242c3045`.
Since the v2 mathematical bytes are identical, no mathematical finding is
invalidated or enlarged by this source-only repair.

## Independent minimal compilation

The v2 wrapper was compiled in the sibling directory with

```text
latexmk -pdf -interaction=nonstopmode -halt-on-error compile.tex
```

in two resolved passes.  The resulting six-page letter-size PDF has SHA-256

`cb82cad66d8cc7924feccffaf5b22b0ce0a8f30043b9411b2b7a4de89791ae17`.

The final log has SHA-256

`70860c78abdacb0956b1e1d68d5bad1a92366ea6c7f0ffe561dbc80b78e755dc`

and contains no undefined reference, undefined citation, multiply defined
label, overfull box, or TeX error.

## Verdict

**PASS: the exact-source identity is closed, and the source-only v2 sibling
is ready for production submission of its unchanged principal bytes.**

- Principal-byte mismatch: **0**.
- Critical mathematical errors carried from the exact-byte audit: **0**.
- Mathematical proof gaps carried from the exact-byte audit: **0**.
- Exact-source/provenance gaps after recheck: **0**.

The named polyhedral-manifold extension remains subordinate to the explicit
generator-preserving chart hypothesis.  Nonconvex and branched face gluing is
still excluded.  P07.1 is not retired.

No live-book file was edited and no production call was made.
