# P14.8 v3 current-source rebase

## Scope

P14.8 v3 repairs the Cantor initial-index calculation.  The matching live
Chapter 51 correction changes the frozen v2 Cantor excerpt, while its
`I`-envelope/projection and all-mass excerpts remain byte-identical to the
current manuscript.  This dossier binds the v3 candidate to those current
source inputs without modifying the immutable v2 candidate or any further
live text.

The source map is:

| v2 frozen locator | current locator | status |
| --- | --- | --- |
| 3240--3288 | 3291--3339 | exact v2 bytes |
| 3707--3829 | 3758--3882 | exact v3 Cantor bytes |
| 3898--3917 | 3951--3970 | exact v2 bytes |

The v3 proof postimage has SHA-256
`94e6efde9dc8e14bb90ae8b63a3cfa0b0f53b024210e570e29b0b67bd450b47b`.
The patch from the v2 proof is preserved in
`../p148_cantor_index_repair_20260908/V2_TO_V3.patch`.

This is a current-source alignment record only.  It is not a new independent
mathematical audit, a source-complete production verdict, live integration,
or P14.8 retirement evidence.
