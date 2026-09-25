# Independent review scope

Review the exact theorem and corollary in `STATEMENT_LIVE.tex` against the
proof in `PROOF_LIVE.tex` and the dependency excerpts supplied in the
verification packet.

In particular, check:

1. whether `(a o f)^* <= a^* o f` is used with the correct hypotheses;
2. whether the live inputs really make both `p_g` and `h_g` subharmonic;
3. whether `p_g <= h_g <= q_g` implies the stated strict-locus splitting;
4. whether equality off the closure of `B_g` is enough for the local and
   sheaf subharmonicity conclusion;
5. whether the all-extensions curve-test witness is separated under the
   source convention, so that it lies in the theorem's stated class;
6. whether any conclusion silently assumes analyticity of the canonical
   retraction or a removability theorem.

Return a verdict and enumerate every critical error or proof gap.
