# P09.1 live-integration receipt — 25 August 2026

## Scope and mathematical disposition

This receipt controls the live integration of two complementary results about
the semipositive analogue of the local finite integral decomposition of
harmonic PL functions.

1. Every PL germ with coefficients in (mathbf Z), or in a divisible
   additive subgroup of (mathbf R), is a finite signed combination of
   semipositive integral PL germs, over an arbitrary good strict analytic
   germ and in arbitrary residual dimension.
2. The corresponding nonnegative-cone assertion is false.  An irrational
   extremal nef ray gives a general residual-surface obstruction, and the
   constant good-reduction surface (E\times E) over (mathbf C((t)))
   gives an explicit example for
   (Lambda=mathbf Q+mathbf Q\sqrt2).

Together these results settle the unrestricted P09.1 atom.  They do not settle
ordinary delta-metricity of canonical cubical metrics, which remains P09.2.
No novelty or priority claim is made.

## Controlling production verifications

| result | run | item | verifier | outcome |
|---|---|---|---|---|
| signed semipositive span | `20260825T130036Z_c1607c25ec38` | `pi_c3231d0fe67b2ad1d3a08ee0` | `gpt-5.6-sol`, `xhigh` | final `correct`; 1/1 checked; 0 critical errors; 0 gaps |
| positive-cone obstruction and example | `20260825T130707Z_4c4a1f2c885f` | `pi_bdb5349d5b3e403fdc08ef87` | `gpt-5.6-sol`, `xhigh` | final `correct`; 1/1 checked; 0 critical errors; 0 gaps |

The exact packet hashes are:

| file | SHA-256 |
|---|---|
| `p09_signed_semipositive_span_statement_exact_20260825.tex` | `c1607c25ec38a4e2b9f50c3fd681e532ae4e1e1efbb9155a76de758c06d5fc79` |
| `p09_signed_semipositive_span_source_aware_proof_exact_20260825.tex` | `ca91bcee1ee0b821523e377128e4989431240cbf1cc6b90d887d6787f5dd6214` |
| `p09_signed_semipositive_span_source_aware_request_20260825.json` | `1fb301bfadeba0cbf42db331565d26999c74223fe1a3d0260fe1fc73d59c4e19` |
| `p09_signed_semipositive_span_source_aware_response_20260825.json` | `11addb5d8f8cd1ad716e64299290aa14dad89745a631c52fb0ef857110e72b2e` |
| `p09_signed_semipositive_span_source_aware_headers_20260825.json` | `f5ca8db6c4dec0c74025d0b30d1051364f4e74e8b09bdf12e07e444559535c95` |
| `p09_positive_cone_counterexample_statement_exact_20260825.tex` | `4c4a1f2c885f00ba1b5e9398909589f85e6298277c78dfd1039fd75c31a1c9b1` |
| `p09_positive_cone_counterexample_source_aware_proof_exact_20260825.tex` | `fb6aec4b8055d924dc4a42cbf702bb474272ce165f69ed5572471dfb45e2f403` |
| `p09_positive_cone_counterexample_source_aware_request_20260825.json` | `ef392e5f6a029a08325eaffd8c56c26432fac0b68ce7925cc6fb462e0609a780` |
| `p09_positive_cone_counterexample_source_aware_response_20260825.json` | `029bde00645d242a23d738833af7e9396517d24aaccb68b1f16d5f790f0f5e00` |
| `p09_positive_cone_counterexample_source_aware_headers_20260825.json` | `a7030869d242d1686d6caa47ed0f2c4f1d57c4bf89dac4a4a4c57f3d7f98728c` |

The copied aggregate and item artifacts are preserved under
`p09_signed_semipositive_span_run_20260825/` and
`p09_positive_cone_counterexample_run_20260825/`.  Their controlling item
verification hashes are respectively
`a7cc951e4ee346f880fbb288d126ec1ceab51b7d2765f63f27425db758b3d8c9`
and
`bd54c08aebb32054d84764a4ffe65673140a1118e0f58589ab8a72c595f49c37`;
the aggregate-manifest hashes are respectively
`91d33c0c584c6e2dafb03b5939a0f8122286762b7877187e594d82e0c7aaf0d2`
and
`07f433e25a395fd963e218612f3a9c4a7319d3e4ccd235aa42cda63ef30df261`.

## Exact live-byte integration

`parts/part2/ch18_delta_forms.tex` inputs, without transcription, the
following four frozen files:

- signed statement,
- signed source-aware proof,
- positive-cone statement,
- positive-cone source-aware proof.

Their environments are balanced, their labels are globally unique, all
internal references and citations resolve, and no preamble or nested include
command occurs.  The production-source closure therefore has 105 files.  Its
ledger is `editorial/current_source_closure_20260825.sha256`, whose SHA-256
is
`01a38c76ca1788cc0ecb7ca870142818381910ae050b35755d72ad715af7cb55`.
The dated 101-file release ledger was not modified.

The live narrative, research ledger, atomic inventory, theorem provenance,
Appendix L, Chapter 72, and public open-problem packet all distinguish the
signed theorem from the failed positive-cone characterization.  P09.1 was
removed from the active inventory.  The resulting live inventory has 57
atoms:

[
T1=0,qquad T2=8,qquad T3=15,qquad T4=17,qquad T5=17.
]

There remain 17 formal `problem` environments: one in Chapter 71 and
sixteen in Chapter 72.

## Build and static gates

The converged command

```sh
cd manuscript
latexmk -pdf -interaction=nonstopmode -halt-on-error book.tex
```

produced `book.pdf` with 3,133 pages and 15,112,387 bytes.

- PDF SHA-256:
  `86308e8040a37a0e842820674cf91fe0d53ceddc76a867c35a0e6c8eb2729b96`.
- Log SHA-256:
  `b976f35c93b9b974273017634ffa2cba5a5b9cb7694f56d64b1f39c7aa4ed84a`.
- No TeX error, undefined control sequence, fatal or emergency stop,
  undefined reference or citation, multiply defined label, duplicate
  destination, or overfull box was found.
- There is no exercise environment and no optional name on a theorem, lemma,
  proposition, corollary, or claim.
- The author field is empty and the acknowledgements have no body text.
- `git diff --check` passed.

Rendered visual inspection passed for the signed statement on printed page
822, the positive-cone statement and proof on printed pages 825 and 829, the
Chapter 72 status record on printed pages 2888--2889, and the Appendix L
provenance entries on printed page 3042.  No clipping, overlap, malformed
link, or unreadable display was observed.

This receipt records verification and integration only; it does not assert
publication, novelty, or priority.
