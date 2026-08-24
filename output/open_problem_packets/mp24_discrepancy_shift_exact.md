# Exact verification packet: the discrepancy shift in MP24 entropy

## Statement to verify

Let $X$ be a compact Kähler manifold and let $\alpha$ be a Kähler class.
Write $v_{\mathrm{triv}}$ for the trivial semivaluation and let

\[
 A^{\mathrm{tot}}(v)
 =\sup_{\mathcal X}A_{X\times\mathbf P^1}
       (p_{\mathcal X}(v))
\]

be the function constructed in Mesquita--Piccione, arXiv:2409.06221v2,
equation (3.2.4).  Then the entropy entering the non-Archimedean Mabuchi
functional and its slope inequality must use

\[
 \boxed{A_X^{\mathrm{NA}}=A^{\mathrm{tot}}-1},
\]

not $A^{\mathrm{tot}}$.  Equivalently, MP24 Proposition 6.2.2,
Corollary 6.2.3, and Theorem 6.3.3 are mathematically consistent only when
their operative $A_X$ is interpreted as the reduced discrepancy
$A^{\mathrm{tot}}-1$.

## Exact derivation

1. MP24 equation (3.2.3) gives

\[
 A_{X\times\mathbf P^1}(\sigma(\operatorname{ord}_F))
 =A_X(F)+1.
\]

For the trivial semivaluation, represented on the trivial model by
$X\times\{0\}$, this gives

\[
 A^{\mathrm{tot}}(v_{\mathrm{triv}})=1.
\]

2. The zero potential is represented on the trivial model, whose central
fiber has one component of multiplicity one.  The model Monge--Ampère
formula therefore gives

\[
 \operatorname{MA}_\alpha(0)=\delta_{v_{\mathrm{triv}}}.
\]

Its energy and twisted-energy terms vanish.  Hence the functional obtained
by integrating total discrepancy satisfies

\[
 M_{\alpha,\mathrm{tot}}^{\mathrm{NA}}(0)=1.
\]

3. The maximal complex ray associated to the zero potential is the constant
ray $U_s=0$.  The complex Mabuchi functional is invariant under constants,
so

\[
 \lim_{s\to+\infty}s^{-1}M_\omega(U_s)=0.
\]

Thus the total-discrepancy reading of MP24 Corollary 6.2.3 would give the
false inequality $1\leq0$.

4. In the proof of MP24 Proposition 6.2.2, the PL test function is written
as $A\circ p_{\mathcal X}$, and a compatible smooth ray $U$ is used in
the entropy variational formula.  The proof asserts

\[
 \log\int_X\exp(U_s)\,\mathrm d\mu=O(\log s),
\]

so the logarithmic term divided by $s$ tends to zero.  This normalization
requires the non-Archimedean test function to have value zero at
$v_{\mathrm{triv}}$.  The total function has value one there; its
compatible ray has linear constant part $s$, and the displayed logarithm
has linear term $s$.  Subtracting one from the PL function is exactly the
required normalization.

5. With $A_X^{\mathrm{NA}}=A^{\mathrm{tot}}-1$, one has
$A_X^{\mathrm{NA}}(v_{\mathrm{triv}})=0$, the constant-ray test is correct,
and the entropy proof applies to
$A^{\mathrm{tot}}\circ p_{\mathcal X}-1$.  This is also the convention
explicitly adopted in Mesquita--Piccione--Witt Nyström,
arXiv:2509.09442v1, Definition 2.4.1:

\[
 \operatorname{Ent}(\mu)
 =\int(A_{X\times\mathbf P^1}-1)\,\mathrm d\mu.
\]

## Primary-source locations

- MP24 arXiv:2409.06221v2, PDF p. 31, equation (3.2.1): ordinary log
  discrepancy $A_X(r\operatorname{ord}_F)$.
- MP24 v2, PDF p. 32, equations (3.2.3)--(3.2.4): the Gauss-extension
  identity $A_{X\times\mathbf P^1}(\sigma(\operatorname{ord}_F))
  =A_X(F)+1$, followed by the supremum construction of the function later
  denoted $A$.
- MP24 v2, PDF p. 51, Definition 6.2.1: entropy is printed as
  $H_\alpha(\phi)=\int A_X\,\operatorname{MA}_\alpha(\phi)$, without
  resolving whether $A_X$ is the total function from (3.2.4) or its
  reduced version.
- MP24 v2, PDF pp. 51--52, Proposition 6.2.2 and its proof, especially
  equations (6.2.2)--(6.2.3) and the assertion
  $\log\int_X\exp(U_s)\,\mathrm d\mu=O(\log s)$.
- MP24 v2, PDF p. 52, Corollary 6.2.3, equation (6.2.4): the
  non-Archimedean Mabuchi slope inequality.
- MP24 v2, PDF pp. 52--53, Theorem 6.3.3 and its proof: the contradiction
  uses $M_\alpha(\phi)\leq0$, so the same reduced normalization is
  required.
- MPWN25 arXiv:2509.09442v1, PDF p. 13, Definition 2.4.1: entropy is
  explicitly $\int(A_{X\times\mathbf P^1}-1)\,\mathrm d\mu$.

## Verification status

This is an exact verification input, not a verification receipt.  The
manuscript marker is `% RETHLAS-NEW: mp24-discrepancy-shift-correction`.
The correction must remain described as pending until the designated xhigh
gate returns a receipt for this exact packet.
