# Source matrix

Date: 30 August 2026

This matrix records only claims actually used by the exact staged proof.
URLs point to primary author or publisher copies. The local PDF is inside the
same manuscript snapshot.

| ID | Proof use | Exact source locator | Scope check |
|---|---|---|---|
| S1 | Definition of real-PL by a G-cover of unit-log expressions | Gubler–Jell–Rabinoff, Definition 5.1, [official SMF PDF](https://smf.emath.fr/system/files/filepdf/GUBLER_JELL_RABINOFF.pdf), pp. 170–171 | Coefficient group is $\mathbf R$; the candidate does not replace a G-domain by an ordinary neighborhood. |
| S2 | Restriction and G-sheaf properties for real-PL | Gubler–Jell–Rabinoff, §5.2(3),(4), same official PDF, p. 171 | Used to localize and glue; no finite-flat descent is inferred. |
| S3 | Scalar descent of real-PL | Gubler–Jell–Rabinoff, Corollary 5.12, same official PDF, pp. 176–177 | Applies because $U$ is good strict, $L/K$ is finite algebraic and complete, and $\mathbf R$ is divisible. |
| S4 | Definition of GJR harmonicity | Gubler–Jell–Rabinoff, Definition 7.2, same official PDF, p. 187 | Harmonicity is concluded only after real-PL and semipositivity of both signs are known. |
| S5 | Classical pluriharmonic scalar extension and pullback | Gubler–Rabinoff, Proposition 7.2(6),(7), [arXiv primary PDF](https://arxiv.org/pdf/2506.13548v2), pp. 34–35 | Clause (6) handles $L/K$; only the forward arbitrary-pullback direction of clause (7) is used. |
| S6 | Classical psh iff semipositive for R-PL | Gubler–Rabinoff, Theorem 4.3, same arXiv PDF, pp. 22–23 | Hypotheses exactly match a good strict space over a nontrivially valued field. |
| S7 | Local primary copy for S5–S6 | `manuscript/editorial/rethlas_packets_20260830/p031_perfected_unibranch_curve_envelope_20260830/sources/Gubler_Rabinoff_2506.13548v2.pdf`; SHA-256 `83ca9a19394f44bb2e4e1aa316de95938f311acd53a00fe250fa0f605184b726` | Exact v2 bytes audited locally. |
| S8 | Rational refinement of affinoid domains | Temkin, *A new proof of the Gerritzen–Grauert theorem*, Theorem 1.1 and the stated affinoid-domain consequence in the introduction, [author PDF](https://math.huji.ac.il/~temkin/papers/Gerritzen_Grauert.pdf); classical locator BGR 7.3.5/1 | Used only after taking a finite strict-affinoid subcover of an affinoid G-cover. |
| S9 | Affinoid fibre product and finite pullback | Temkin, *Introduction to Berkovich analytic spaces*, Fact 4.1.16 and Definition 4.2.5, [author lecture PDF](https://berkovich-2010.imj-prg.fr/lecture-notes/Temkin-lecture-notes.pdf) | The candidate additionally proves that the finite tensor product is already complete and proves the $q$-power calculation elementwise. |
| S10 | Quasi-smooth PH implies R-PL and GJR harmonic | Production-verified live `thm:p061-quasismooth-ph-rpl`; packet and exact hashes in `DEPENDENCY_LEDGER.md`, D1 | Applied only to an affinoid analytic domain of $\mathbf A^r\times\mathbf G_m^{n-r}$. |
| S11 | Real-PL descent through finite constant-group quotients | Production-verified live `prop:p061-finite-group-rpl-descent-candidate`; packet and exact hashes in `DEPENDENCY_LEDGER.md`, D2 | Applied only after adjoining the missing prime-to-$p$ roots of unity and verifying the restricted affinoid invariant algebra with the Reynolds projector. |

## Internally proved claims

No external source is needed for the following steps because the exact proof
contains the complete argument:

- saturation and splitting of $N\cap\operatorname{span}_{\mathbf R}\sigma$;
- the non-full-dimensional decomposition
  $X_{\sigma,N'}\simeq\mathbf A^r\times\mathbf G_m^{n-r}$;
- finiteness and diagonalizable invariant algebra of the lattice cover;
- the canonical $p$-primary/prime-to-$p$ lattice factorization;
- existence of the finite roots-of-unity splitting field;
- $B^q\subseteq A$, radiciality, and universal pointwise uniqueness;
- preservation of $D^q\subseteq C$ under finite affinoid and rational base
  change;
- descent of rational inequalities and analytic units by $q$-th powers;
- Reynolds-projector compatibility for the split constant factor.
