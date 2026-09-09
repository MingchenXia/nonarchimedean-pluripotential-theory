# P14.2 V7 exact-live binding

This is a local reproducibility audit for the frozen P14.2 V6 source-stage
candidate. It authenticates that candidate's complete manifest and read-only
release tree, then proves that its statement, proof, and example are exact
current Chapter 71 excerpts.

Run `python3 check_exact_live_binding.py` for a read-only audit. Add
`--run-tests` to replay the 179-test candidate suite. Only `--materialize`
regenerates the pinned context and audit manifest.

The audit does not substitute for independent hostile review, a final-path
smoke, or production verification; P14.2 remains open.
