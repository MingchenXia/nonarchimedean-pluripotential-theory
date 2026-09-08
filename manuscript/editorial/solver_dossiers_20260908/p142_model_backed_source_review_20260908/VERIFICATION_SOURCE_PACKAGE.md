# P14.2 model-backed source-review package — 8 September 2026

## Scope

This package requests an independent sequential review of the frozen P14.2
upper-semicontinuity argument.  It is neither a source-closed production
release nor a retirement record.  In particular, a favorable review cannot
by itself retire P14.2, alter the Chapter 72 inventory, or establish the
separate MP-positivity question P14.3.

The target consists of the exact research-packet statement and proof:

| artifact | SHA-256 |
| --- | --- |
| `statement.tex` | `488868dc2b2d1d62b23864970f8bf36acc0a6c7c85d27eaf66e6a9ed7120c949` |
| `proof.tex` | `bf991c724e138626fbd8fcd4fc6f613d7979f3bf75a3614c569a1ff3c7d21e21` |
| contextual `example.tex` | `7010c2a461de6f2ed1fb7c1f0170c6eaa8aed38b88492ea919f8b0c1eea49f6f` |

The statement and proof are taken verbatim from
`solver_dossiers_20260831/p142_raw_transform_usc_research_20260831`.
The example is contextual material: it tests the infinite ideal-value case
but is not silently made part of the theorem statement.

## Cited primary-source extracts

The submitted proof context includes the source audit, the contextual example,
and these exact normalized text extracts from the independently audited
source-closed release:

| source | SHA-256 |
| --- | --- |
| `mp_2409.06221v2.txt` | `724926d161cb3744dd5037e259f098a944a072419176bdc3e02538a657e5c59d` |
| `dxz_2302.02541v3.txt` | `3234b3366d4aa4e235c5d2581cb131c68b95cdb0b386622302b4707930ea57f9` |
| `xia_2312.17150v3.txt` | `a39c27332e746fa7f711718542658b1a0cfc526b8922f6f220e159089ac9562d` |
| `darvas_xia_2003.04818.txt` | `794c9e34736334b6ba2ff01a257a916b619e9036cb02e2a2e160c494e6c358ed` |
| `demailly_ein_lazarsfeld_math0002035.txt` | `0ae95d36227cc357a45b42336fdc1c28588be7163d25e160ba9e5a47bf8e81a3` |

The original source-closed audit additionally binds the exact locator blocks
used for the spectrum topology, DXZ test curves and transition maps,
multiplier-ideal envelope invariance, multiplier-ideal subadditivity, and the
raw ideal-valuative formula.  This model review retains that delimitation:
it checks the theorem as a proof packet and does not turn a cited source into
an assertion that the source already proves the new all-point result.

## Submission boundary

`VERIFICATION_RUN_20260908/request.json` is the exact submitted request.  A
response and a concise result record may be added only after the verifier
reaches a terminal state.  Until then this package records no verdict.
