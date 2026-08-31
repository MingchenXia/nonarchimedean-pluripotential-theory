# Direct source checks for the conditional operations audit

The exact primary text inputs already listed and rehashed in the candidate are:

- Xia Operations v3 local text `/Users/mingchen/Projects/Yethlas/tmp/pdfs/xia23operations.txt`, 73721 bytes, SHA-256 `c75572e06a2df8cb9dbd76726678a52db5e79587ec568df41f4886e3e4ee8005`.
- MP v2 local text `/private/tmp/mp24.txt`, 209776 bytes, SHA-256 `0445ccf2c4474b6576a8053d0c7c038ffbd72c2ab27bb3d5704b90dd0e5beb62`.

I read the following primary interfaces directly, not solely the author's paraphrases:

| Source | Precise interface |
| --- | --- |
| [Xia v3 §3.2](https://arxiv.org/html/2312.17150v3#S3.SS2) | Definition 3.2 prime curves versus positive-mass curves; Definition 3.5 inverse-system transitions and finite common endpoint; Lemma 3.7 equivalence of presentations; equation (3.5) full-space injections and following QPSH direct limit, explicitly independent of starting theta. |
| Xia v3 opening of §4 and §4.1 | Compact Kähler scope is restated; the preceding projective comparison subsection is not a standing restriction. Definition 4.1 and Lemma 4.2 give order and divisorial reflection. |
| Xia v3 §§4.2–4.4 | Proposition 4.4 gives translation and endpoint. Corollary 4.8 gives maximum and endpoint. Definition 4.9 requires finite lower endpoint for a decreasing-net infimum; Lemma 4.10 gives its divisorial and endpoint values. |
| [Xia v3 §4.6](https://arxiv.org/html/2312.17150v3#S4.SS6) | Definition 4.14 allows every real positive scaling parameter and scales the class. Definitions 4.15/4.16 supply addition, with the latter's repeated-background typo explicitly excluded. Lemma 4.17 states the sum/scaling numerical and endpoint formulas. The type-correct half-perturbation interpretation is detailed in the audit. |
| [MP v2 §4](https://arxiv.org/html/2409.06221v2#S4) | Definition 4.1.2 relative nefness of a PL model, Definition 4.3.1 decreasing model completion, and Theorem 4.3.8 comparison of a psh function with an arbitrary usc function. Only Kähler-class MP cones are used. |

The HTML sources were opened on 31 August 2026; the local texts gave the exact formulas when HTML layout was abbreviated. No new PDF was generated or visually reviewed.

For representative changes, the standard cohomological identification is explicitly stated on p. 3 of the introduction of DXZ arXiv:2302.02541v3. That local source `/private/tmp/dxz23.txt` has 141745 bytes and SHA-256 `7d5a061d240096139e6302c2b4da2e9c125a8839730fc90909c1488baa446244`. It was read directly in the preceding nef-source check and the same interface was checked against the current proof. Smooth shifts preserve ideals by local boundedness, and normalized I-enveloping is the already named mass-free transition input of the assumed P14.2 packet. This audit does not replace that input with a positive-unperturbed-mass assumption.

The new research inputs are **assumed**: P14.2 raw USC, P14.3 dominated-divisorial approximation, and the full Kähler order comparison. Their exact files are included in the candidate's 11-entry input ledger and verified in `CHECKS.json`. The reviewer authored the dominated-divisorial premise; this audit explicitly does not self-certify it. The independent status of that premise comes only from its separate reviewer, not this report.

Source statements of the ordinary operation theory are treated as inputs. This is not a new independent proof of every theorem in Xia or MP, and no statement is attributed to those papers as already giving the present all-semivaluation conclusion.
