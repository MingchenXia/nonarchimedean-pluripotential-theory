# P14.3 full Kähler truncation integration

This dossier freezes the 19 September 2026 candidate that closes the
remaining Kähler-class image direction of P14.3, conditional on the already
stated P14.2 upper-semicontinuity conclusion.  It contains the new MP
decreasing-stability lemma and the DXZ truncation argument used in the live
Chapter 60/71 integration.

The live-book rendering is frozen in `STATEMENT.md` and `PROOF.md`.
`VERIFICATION_PROOF.txt` is the same mathematical proof without Markdown
headings, so the verifier treats the packet as one synthetic item after the
source extracts are prepended.  `SOURCE_AUDIT.md` records the primary-source
interfaces and the boundary of the claim.  The verifier run and its exact
request, response, headers, hashes, and verdict will be archived here before
any Chapter 72 retirement or problem count change.

The result is not an unconditional proof of P14.2, and it is not a theorem
for a big non-nef or zero-volume class.  Its conclusion is the full DXZ--MP
order isomorphism in a Kähler class, with the finite-energy correspondence as
its finite-energy restriction.

`VERIFICATION_RUN_20260919` and `VERIFICATION_RUN_V2_20260919` are HTTP 422
pre-dispatch failures: respectively, source text preceded a structured proof
item and the full source files exceeded the per-item context budget.  Neither
failure launched a model.  `VERIFICATION_RUN_V3_20260919` uses exact cited
source ranges and is the production mathematical run.

That V3 run checked the new truncation argument but returned `wrong` with
one dependency-closure gap: the packet used the already verified full-cone
MP section without listing it among the established interfaces.  The live
Chapter 71 proof already cites that theorem.  V4 makes this premise explicit
as interface 6 and changes no truncation deduction.
