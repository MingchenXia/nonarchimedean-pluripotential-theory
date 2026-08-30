# Current-source build: four T2 scope reductions

Date: 30 August 2026 (Asia/Shanghai).

This record supersedes `current_source_build_p071_infinite_star_20260830.md`
as the controlling current-source build.  It does not rewrite any dated
release archive.

## Mathematical gates

Four exact statement/proof pairs were integrated in this milestone only after
independent source-aware audit and production Rethlas verification with
`gpt-5.6-sol` at `xhigh`.  Every production verdict was `correct`, with zero
critical errors and zero gaps.

| Atom narrowed | Verified scope | Statement SHA-256 | Proof SHA-256 | Production run |
|---|---|---|---|---|
| P03.1 | perfected unibranch analytic curves | `e30033eea96e7d59310a1e67402dc73dbdc1a9463b7ab14fc6f28e271ea0397f` | `59535602b2f29c7c34bb4b4df79be1e2f72c0fa4fa61f1467b3e1c75723a1c71` | `20260829T233220Z_e30033eea96e` |
| P06.1 | finite constant-group quotients of separated strict affinoid sources | `e1daa4b3e3efd64fcc8f0ce05b9c1d5d6cb69b28686b939b48535fc56b0ccc07` | `a6c24d1686c726dc72aebe55a1e83eb8d4fe1ed4025d4a8d7166da59123ce30e` | `20260829T235341Z_e1daa4b3e3ef` |
| P06.2 | strict open and closed polydiscs over an algebraically closed complete nontrivially valued field | `017f3da108ae737e4bbc1d490d6988faf76ce643b4cb52104aae53c4dcda75d6` | `3763bf9a7e4b1f47602544ad2c3248d9b8abd7b9d34109e3c14259e422393bbd` | `20260830T001728Z_017f3da108ae` |
| P07.1 | fixed-core flattening of iterated first-stage approximation rows | `b29ccabac98982c239fcedcc34a701c9a9bb98ca95710d6ed7fbaa3f0f96e4d9` | `7677ba46620cc4cef8a74d502cdf9fde344e045b04bbc66a4274a5c20b1838c2` | `20260829T234341Z_b29ccabac989` |

The P06.2 packet has an exact-byte hostile-audit SHA-256 of
`2419e2c7abb2c07b5ee1ffc4feae40fc6e54c0a784a716f4db71abc73b03ba8c`.
Its archived request, response, and headers have respective SHA-256 values
`7ac08a78130251f6153f21e5fe4e191e2fe8c93562e235b8ed4e8f69dd86bd8e`,
`416af3bce60e90de51898e9f95b5addbfd1d99f47a396df65bb03a6af14304b5`,
and `a15e345955c74239824ad2585ec60d0364a07279c4ea9de902ce208ef7b06843`.
The corresponding service-side verification record explicitly logs the same
model, scrutiny, theorem bytes, proof bytes, and final verdict.

None of these theorems is promoted beyond its displayed hypotheses.  In
particular, the strict-polydisc theorem does not supply arbitrary-ground-field
descent or uniformization of an arbitrary analytic germ; the other three
results likewise leave the residual scopes stated in Chapter 72 untouched.

## Converged whole-book build

Starting from base commit
`528722d114554db5cd1cb8dcd8478c3e8210b470`, the integrated source was built
with

```text
latexmk -pdf -interaction=nonstopmode -halt-on-error book.tex
```

The build converged.  A literal final-log scan found:

- LaTeX errors, fatal errors, emergency stops, and undefined control
  sequences: 0;
- undefined references and citations: 0;
- multiply defined labels and duplicate PDF destinations: 0;
- overfull horizontal or vertical boxes: 0.

The title is `Non-Archimedean Pluripotential Theory`, and the PDF metadata
author field is blank.

## Current PDF and source closure

- pages: 3,364;
- bytes: 16,136,713;
- SHA-256: `6ed7643a080343f54336432ecc3be6666f11cef095aa16f52b4fe9968cac7319`.

The 173-entry live-source closure is
`editorial/current_source_closure_p062_20260830.sha256`.  Every entry passed
`shasum -a 256 -c`; the closure file itself has SHA-256
`c2e38b8e793afed2b7b5f41e2d8efa2ea472f7df9834766fc34a1e2538962903`.

## Rendered audit

The following physical PDF pages were rendered at 144 dpi and individually
inspected:

- 712--716: the perfected-unibranch-curve theorem and proof;
- 753--755: the fixed-core proposition, proof, and scope firewall;
- 1021--1027: the strict-polydisc statement, complete proof, and scope
  firewall;
- 1053--1056: Chapter 18 comparison table and exact provenance;
- 3158--3163 and 3166--3171: the Chapter 72 P06.1, P06.2, and P07.1 status
  records.

No clipping, overlap, margin intrusion, malformed display, or redundant proof
heading remains in those ranges.  The exact verified packet bytes were not
changed by the local presentation wrappers.

## Inventory consequence

Each theorem removes a blanket residual subcase but none retires its whole
atom.  The active inventory therefore remains 53 atomic questions in 14
formal problem environments, with tier distribution `(0,5,14,17,17)`.

No novelty or priority claim is made.
