# Build and execution evidence

The substantive analytic theorem is incomplete. Therefore no standalone
P06.2-partial.tex or twice-compiled PDF is generated: those deliverables
were required only for a complete substantive new theorem. status.json
has exactly five keys, id P06.2, status incomplete and proof_file null.
P06.2-argument.md is an accessible diagnostic dossier, not a proof claim.

Rerun from this fresh directory with bash reproduce.sh. The commands are:

    python prepare_evidence.py > evidence/extraction-output.json
    python diagnostics/finite_checks.py > diagnostics/output.json
    python assemble_and_validate.py > evidence/validation-output.json

Environment details are in evidence/environment.json. Only Python's
standard library is used. The diagnostics use exact Fraction arithmetic.
They enumerate 1,441 labelled trees, 85,787 nonempty-boundary assignments,
2,209 bounded rational slope pairs and 100 tail-shift identities.
The written proofs distinguish these finite results from universal claims.

The assembly step embeds the exact selected primary bodies and checks the
five-key status, null proof pointer, note dependency order, negative
candidate value, source selection hashes and finite diagnostic counts.
It hashes the retained new artifacts. These are reproducibility/schema
checks, not a mathematical verifier. The original input inventory is
rechecked on every extraction run to detect predecessor mutations.
