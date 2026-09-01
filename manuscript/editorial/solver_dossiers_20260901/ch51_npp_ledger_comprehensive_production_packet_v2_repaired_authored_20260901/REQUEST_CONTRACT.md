# Exact source-closed production request contract

This packet is prepared for `gpt-5.6-sol` at `xhigh`.  It has not been
submitted.

The request target is the ordered pair `STATEMENT.tex`, `PROOF.tex`.
`STATEMENT.tex` is byte-identical to the audited
`LOCAL_CONSTRUCTION_REPLACEMENT.tex`; `PROOF.tex` is byte-identical to the
audited `LEDGER_REPLACEMENT.tex`.  The apparently unusual split is
intentional: the first field contains the exact local setup and auxiliary
construction on which the theorem depends, while the second contains the
exact theorem statement followed by its proof.  Reformatting, extracting a
new theorem statement, or silently moving preliminary arguments between the
fields would change the production target and is forbidden.

The verifier must audit the two fields in order as one source-closed target.
The independent audit is evidence that this target is ready to be submitted;
it is not a substitute for the verifier's mathematical work.

The proof has one deliberately imported substantive result: unrestricted
monotonicity of total mixed nonpluripolar masses in `PROOF.tex` lines
317–327 is DDNL Theorem 1.1.  The verifier must check the orientation and the
`p<n` specialization against fixed source `ddnl_1705_05796`, lines 62–65 and
74–86.  It must not demand that the packet reprove DDNL, and it must not
credit DDNL with the remaining arguments.

The following material is supplied in the target and must be verified
line-by-line as an internal proof: the local mass definition; admissible
exhaustions; both potential-choice mass inequalities; the common-exhaustion
current; the capacity proof of no pluripolar charge; positive-cone
multilinearity and both local-finiteness directions; compact-Kähler
finiteness; closedness; pullback from local psh potentials; and the
modification pushforward formula.  BEGZ and Bedford–Taylor are fixed for
source comparison, but citations to them do not replace checking these
supplied deductions.

The exact external and candidate routes are frozen in `SOURCE_ROUTES.json`.
For each external text, the route records the raw extraction hash and the
bundled normalization: one LF byte appended after its terminal form-feed.
The raw extraction command for all three PDFs is exactly
`pdftotext -layout`.  Line addressing is one-based and LF-only: byte `0x0a`
is the sole separator, byte `0x0c` remains content within a line, and the
terminal LF terminates the last addressed line without creating another one.
No form-feed-aware or parallel runtime line-number domain is permitted.
Each contracted external range is bound by the SHA-256 of its exact inclusive
line bytes, with an LF after every selected line.  In particular, the
verifier must recover BEGZ Definition 1.1 at LF line 211,
Bedford--Taylor Theorem 6.9 at LF line 1107, and DDNL Theorem 1.1 at LF
line 81 with the exact anchor-line hashes in `SOURCE_ROUTES.json`.
This normalization changes no routed line content or LF-only line number.

No runtime stage is bundled.  The independent hostile audit rejected the v1
runtime sibling because its final-path smoke runner was already known to
fail.  Repairing and independently auditing that runtime is a separate gate;
this packet does not claim to satisfy it and must not be installed or smoked
on its own.
No live Chapter 51 file, Chapter 72 inventory, or production result is part of
this packet.
