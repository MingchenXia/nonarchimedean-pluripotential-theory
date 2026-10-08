# P12.3 whole reconstruction artifacts

The complete proof core is [whole-proof.md](whole-proof.md). The standalone [P12.3-paper.md](P12.3-paper.md) includes all qualified incoming grant bodies. P12.3-paper.tex is the same full mathematical core, uncompiled. Every new proof body is also n1.md--n14.md. Native notes are expanded proof-bearing notes; actual-FINAL.json records the separately emitted final notes and candidate decision.

Original P12.3 remains incomplete. See exact-scope.md, whole-proof-coverage.md, original-scope-and-noncircularity.md, whole-source-application-ledger.md and acceptance-decision.json. The new finite-correction theorem is n12; the exact uniform correction criterion is n11; the residual attempt is n13.

Local rerun (standard library, bounded diagnostics; no compiler/network):

    python audit_inputs.py
    python audit_coverage.py
    python finite_diagnostics.py
    python reconstruct.py
    python write_docs.py
    python prepare_final.py
    python final_audit.py

All input bytes, diagnostics, commands/output/environment and own files are retained. Inputs/primary-LOCALONLY and source images are private and local only. No supplied script is run, and no publication is authorized or performed by these commands. Hash/support audits do not establish mathematical correctness.
