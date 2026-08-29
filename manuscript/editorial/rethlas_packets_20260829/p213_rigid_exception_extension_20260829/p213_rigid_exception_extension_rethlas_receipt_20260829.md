# Production Rethlas receipt: P21.3 rigid-exception extension

Date: 29 August 2026

Status: **PASS** for the exact imported dependency and exact candidate bytes
identified below.  This receipt verifies a normal-curve subclass of P21.3;
it does not retire the unrestricted atom.

## Exact submitted bytes

Candidate packet:

- Statement:
  `cf53c4101b6fe798d89c7e37188f2d1f03f389a5a468fdd055b6fba8bf8cf2f5`
- Proof:
  `cf94877ec4b2a1010a3eb51915c7cbc20a134da0bf2563b90585deab992850ce`

Imported production-verified rig-smooth dependency:

- Statement:
  `c9f27245f5608b772385167c84bfe9e836fc9f4b164477a578b6c26712e35b21`
- Proof:
  `01ab07fdacedfe95e1d764656a071a88395f5d0766115fd0a67164e3162410af`

The submission helper concatenated each imported dependency with the
corresponding candidate.  Extracting `.statement` and `.proof` from the
archived request without adding bytes gives the materialized hashes

- Statement: `cc0c487251146683087e207726f91809862ff9f3e5f6881590d132e6a1445e81`
- Proof: `fd794304c18dd78b953f004eb26917f19e9d34ebd844fe64d536bf4e391bc15d`

The archived request has SHA-256
`3fc6dd8b947a5b4d8c14fd3b93c88ce7a4fbbd9ae7c4debdd825828fe7472ce8`.

## Verifier identity and verdict

- Service run: `20260829T021315Z_cc0c48725114`
- Model: `gpt-5.6-sol`
- Reasoning effort: `xhigh`
- Started at: `2026-08-29T02:13:15.339290+00:00`
- Verification deadline: `2026-08-29T03:08:15.308337+00:00`
- Completed at: `2026-08-29T02:26:22.209015+00:00`
- HTTP status: `200`
- Verdict: `correct`
- Critical errors: `0`
- Gaps: `0`

The archived verifier log records the exact model and reasoning
configuration.  The verifier validated the strict output schema before
writing the final report.

## Verification records

- Sequential statement records: `14`; all passed.
- Primary-source reference records: `26`; all passed.
- Failed-check records: `0`.
- Primary sources checked: Chambert--Loir--Ducros, Ducros's curve-structure
  paper, Gubler--Jell--Rabinoff, and the strict-affinoid Tate facts used by
  the imported dependency.

Artifact hashes:

- Archived response:
  `092565af46b962b6d55cd960248513fcd773d4f68a2a2529b8c208a5a1a63298`
- Archived safe headers:
  `a474be5b69a387841d73b78658b93c837d95e4305934eb65fdaeabef4fd2f0af`
- Archived service `verification.json`:
  `1fa2b8f27814baf1699b39d7b68f6852af2a81db742a69bb22cda2486940a343`
- Archived verifier log:
  `b90e99db1586613dfb4b140d81ddd1f57c6eb3ef9ad66ba465ef447e91a75d08`

The submission helper displayed `checked_items: 0` and `run_id: null`
because the HTTP response intentionally contains neither top-level field.
The authoritative service directory and verifier log identify the run and
record the fourteen statement checks and twenty-six reference checks above.

## Mathematical scope confirmed

Let `X` be a nonempty connected good separated strict normal boundaryless
analytic curve over a complete nontrivially valued field, and let `E` be a
locally finite set of rigid points whose complement `Y` is rig-smooth.  The
verifier confirmed that `Y` is nonempty and connected, that every positive
`d'`- and `d''`-closed CLD `(0,0)` current on `X` is a unique nonnegative
multiple of the integration current, and that these currents have
Bedford--Taylor independence for continuous psh pairs with equal curvature.

The verification expressly does not remove normality, strictness, goodness,
separatedness, boundarylessness, nontrivial valuation, rigidity or local
finiteness of the exceptional set, or the rig-smoothness of its complement.
It does not cover discontinuous psh pairs or analytic dimension at least two.
