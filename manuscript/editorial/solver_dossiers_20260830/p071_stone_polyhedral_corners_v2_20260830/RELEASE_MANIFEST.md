# Exact release manifest

Release: `p071_stone_polyhedral_corners_v2_20260830`

Date: 30 August 2026 (Asia/Shanghai)

Status: source provenance repaired; independent exact-source recheck PASS;
production Rethlas not yet called; not a live-book input.

## Principal mathematical bytes

| File | SHA-256 |
|---|---|
| `statement.tex` | `b46b8e22fa8b3f8f64dcf8ae24d164b905dbe8d9035e37c3ede23321717cc002` |
| `proof.tex` | `37a3b6a12f6ddd2a3038dd926dfe8120d8955756efe64608fbd2a37b33c01efb` |

Both files are byte-for-byte identical to v1.  Direct `cmp -s` checks
returned exit status zero.

## Source and audit records

| File | SHA-256 |
|---|---|
| `README.md` | `afa26c495d7abb5e10301ed054421fdcf2b1f4bf4c7b61917b08542832d3d8b7` |
| `SOURCE_AND_OBLIGATION_MATRIX.md` | `9dcb2c8bab8fb47e3cdeebb8821776770fa1929b2712afbc047bddeed94ae1c0` |
| `INDEPENDENT_EXACT_SOURCE_RECHECK_20260830.md` | `3ff43da8dd1044a0144d6f1410ad5b66020ff868c934886c87f3bc38b5c0f974` |

## Minimal build

| File | SHA-256 |
|---|---|
| `compile.tex` | `74e321a96d68abedffebc5d14d267aee313e3fab07c79354d0c1b513ea81485a` |
| `compile.pdf` | `cb82cad66d8cc7924feccffaf5b22b0ce0a8f30043b9411b2b7a4de89791ae17` |
| `compile.log` | `70860c78abdacb0956b1e1d68d5bad1a92366ea6c7f0ffe561dbc80b78e755dc` |

The final PDF has six letter-size pages.  The final log has no undefined
reference or citation, multiply defined label, overfull box, or TeX error.

## External exact-source chain

| Artifact | SHA-256 / result |
|---|---|
| `/private/tmp/CLD25_1204.6277.pdf` | `5690f999523017d184ab751bb55857ab1637b197d1186ad4fd2edba7e1bda719` |
| `/private/tmp/CLD25_reextracted_layout_p071_20260830.txt` | `021be260392de1f3240858d4c775da86653518dfab4fd9c4c21a2406081b6c7e` |
| `/private/tmp/CLD25.txt` | `021be260392de1f3240858d4c775da86653518dfab4fd9c4c21a2406081b6c7e` |
| exact text comparison | `cmp -s` exit status `0` |

The extraction command was `pdftotext -layout`.  The stale v1 PDF
fingerprint is withdrawn and is not part of this release.

## Scope and release decision

The unchanged theorem covers one convex polyhedral chamber with a locally
constant Stone parameter, and generator-preserving chart-local transports of
that model.  It does not prove a nonconvex or branched face-gluing theorem and
does not retire P07.1.

The release has passed exact mathematical-byte audit and exact-source
recheck.  Its next permitted step is production verification of these exact
principal bytes with the source dependencies materialized.  No production
claim is made by this manifest.
