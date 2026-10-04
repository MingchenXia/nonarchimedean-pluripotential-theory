ID: n2

SUMMARY:
All arbitrary classical psh targets on saturated products of a permitted curve with proper projective fibres have decreasing ordinary smooth psh approximants. This does not establish regularization of nonsaturated higher-dimensional sheaf germs.

DETAILED SUMMARY:
Under n1’s smooth curve hypotheses, every classical psh function defined on the entire saturated domain U×P^m analytification is constant on each proper fibre. A rational section identifies it with a subharmonic target on U, so n1’s ordinary smooth sequence pulls back on a fixed saturated neighborhood. The starting target need not be continuous, finite, or torus invariant. The conclusion depends on having whole proper fibres in the domain of definition; it does not cover arbitrary targets initially defined on smaller nonsaturated charts.

SUPPORT:
["n1"]

TEXT:
Let K and the smooth proper curve C satisfy n1, let U⊂C^an be ordinary open, and let X=U×_K(P^m_K)^an with m≥1 and projection p. For every arbitrary classical psh u defined on all of this saturated X, each z∈U has an ordinary neighborhood V such that u|p^(−1)(V) is a decreasing limit of finite ordinary CLD-smooth psh functions on that one fixed ordinary open.

Proof. The fibre over z is (P^m_H(z))^an. GR v2 Proposition 4.2(5,6) makes the restriction of u classical psh there. This fibre is compact, connected, and boundaryless. If the restriction is not identically −∞, upper semicontinuity and compactness give a finite attained maximum M. Its maximum locus is nonempty and closed. GR Theorem 6.1 applies at every point of this locus because the entire fibre is an analytic interior; the locus is therefore open. Connectedness implies that u is constant on the fibre. The identically −∞ case is already constant.

Choose a rational point o of P^m and its section s:U→X. The function w=u∘s is classical psh by analytic pullback, hence subharmonic on the curve, and fibre constancy proves the actual equality u=w∘p, including −∞ values. Apply n1 to w at z. Pull its terms w_j back to w_j∘p on p^(−1)(V). Ordinary smoothness and positive d′d″ forms follow from the proved ordinary chart pullback argument. The same quantitative gaps and pointwise convergence are preserved. In the identically −∞ case use constants −j. The products are boundaryless, so the smooth currents are positive as well.

Each term is globally given by the projection formula. Ordinary chart overlaps therefore agree, and after every analytic extension the formula is exactly w_j,L∘p_L. This proves the asserted scalar compatibility without choosing new approximants over the extension.

Scope. This treats all targets on the specified saturated domains and permits noninvariant, discontinuous, or −∞-valued targets. A target on a nonsaturated affine chart need not extend to whole proper fibres. The fibre maximum argument cannot be applied to it, and no such extension theorem was proved. Consequently this result does not establish the original higher-dimensional local sheaf characterization.

The full proof and this limitation appear in P02.4-argument.md and P02.4-paper.tex; the maximum-principle source proof and exact application checks are retained in source-extracts/source-provenance.json. Rerun commands are python3 verify_sources.py and python3 build_and_check.py from the supplied workspace.

Artifacts: /workspace/research/campaigns/round-44/P02.4-public-source-decreasing-ordinary-smooth/artifacts/codex-QKCSac
