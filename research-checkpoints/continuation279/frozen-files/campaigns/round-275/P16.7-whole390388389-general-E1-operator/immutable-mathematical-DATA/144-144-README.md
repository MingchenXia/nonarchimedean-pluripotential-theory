# Independent P16.7 scoped implementation

Original P16.7 remains unresolved (`candidate=false`). This directory contains an unverified independent scoped mathematical review and new intrinsic branch results on the actual nonalgebraizable analytic surface.

Read `proof-companion.md` or `P16.7-independent-paper.md` for the complete scoped arguments. `P16.7-independent-paper.tex` contains their complete standalone prose encoding and has not been compiled. `source-application-ledger.md` distinguishes fresh reading, retained bodies, historical attribution and unresolved source-retention limits.

The new results identify the second atom of the bounded branch potentials, solve finite nested branch equations, compute the exact restricted dual of the actual finite-depth mass-two Dirac, and construct a restricted unbounded radial domain with genuine full-mass mixed products, energy, comparison, separated compactness and countable branch equations. They do not establish full-class admissibility of that Dirac or the original all-direction arbitrary-support theory.

`actual-final-notes.json` and `final-notes.json` contain the same final note data. `expanded-notes.json` contains the longer complete-proof version; their distinct identities are recorded in `evidence/own-version-identities.json`. Supplied actual and expanded versions are separately identified in `evidence/identities.json`.

Rerun from this directory with Python 3.12 and the standard library:

```
python audit_and_build.py
```

This runs only newly written inert readers/retention checks, exact finite rational diagnostics, schema and lexical checks, and document assembly. It does not execute or import supplied programs or invoke a compiler. Mathematical correctness is not established by execution. Full source bodies remain under `sources-LOCALONLY`; bound mathematical inputs remain under `inputs-LOCALONLY`. Direct raw Conrad--Temkin/Ducros PDF retrieval failed in the sandbox; applied primary retrieval bodies are retained and the limitation is disclosed.

No supervised heavy-compute service was supplied or needed. No editor, tab, catalogue, compiler, publication, authentication, proxy or runtime operation was performed. ROOT retains acceptance and publication.
