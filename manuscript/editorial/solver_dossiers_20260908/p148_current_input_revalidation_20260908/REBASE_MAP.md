# P14.8 exact live-span rebase map

The frozen v2 candidate locates its three Chapter 51 dependencies by line
range.  The current Chapter 51 file contains an inserted 51-line
`ℐ`-calculus block before the envelope subsection, so all three old
locators fail even though the dependent text itself is unchanged.

| Frozen candidate locator | Current Chapter 51 locator | SHA-256 | Result |
| --- | --- | --- | --- |
| 3240--3288 | 3291--3339 | `54e4d6b864e81429549753d781a3e1c859cb5235a0d138b556196214611dbaa0` | exact |
| 3707--3829 | 3758--3880 | `e8a6762a30b5e890a49fb8a37b2d80463a7ad72ac66eec7badfd5b329e2e65b5` | exact |
| 3898--3917 | 3949--3968 | `047d2f1f25d4c7d9d88b4a3f492d753fa530044170cd902fa667199aada41282` | exact |

Thus the frozen `I`-envelope/projection, polar-Cantor construction, and
all-mass-family dependency blocks are byte-identical to their present live
counterparts.  This is a source-location rebase only: it changes no
candidate byte and says nothing about the separate production-review gate.
