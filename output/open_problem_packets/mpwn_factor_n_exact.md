# Exact verification packet: the factor $n$ in the MPWN Mabuchi coefficient

## Statement to verify

Let $X$ be a compact Kähler manifold of complex dimension $n$, let
$\alpha$ be a Kähler class, and put $V=\alpha^n$.  Normalize the
non-Archimedean Monge--Ampère energy by

\[
 E_A(\phi)=\frac{1}{(n+1)V}(A,\phi)^{n+1}.
\]

If the non-Archimedean Mabuchi functional is written

\[
 M_A(\phi)=sE_A(\phi)+E_A^{K_X}(\phi)+H_A(\phi),
\]

and is required to agree, on a big model $(\mathcal X,A+D)$, with
\(V^{-1}M^{\mathrm{NA}}(\mathcal X,A+D)\), where

\[
 \mathrm{DF}(\mathcal X,A+D)
 =K_{\mathcal X/\mathbf P^1}\cdot\langle(A+D)^n\rangle
 -\frac{n\alpha^{n-1}\cdot K_X}{(n+1)V}
   \langle(A+D)^{n+1}\rangle,
\]

then the coefficient is necessarily

\[
 \boxed{s=-nV^{-1}\alpha^{n-1}\cdot K_X}.
\]

Thus the formula $s=-V^{-1}\alpha^{n-1}\cdot K_X$ printed in
Mesquita-Piccione--Witt Nyström, arXiv:2509.09442v1, Section 2.4.2,
is missing the factor $n$ relative to that paper's own Donaldson--Futaki
normalization and Theorem 9.1.1.

## Derivation

For a big model, the positive-product energy identity is

\[
 E_A(P_A(f_D))
 =\frac{1}{(n+1)V}\langle(A+D)^{n+1}\rangle.
\]

Consequently the contribution of $sE_A$ to
\(VM_A(P_A(f_D))\) is

\[
 VsE_A(P_A(f_D))
 =\frac{s}{n+1}\langle(A+D)^{n+1}\rangle.
\]

The twisted-energy and entropy terms contribute to the
$\langle(A+D)^n\rangle$-part of the model Mabuchi invariant and do
not contribute another multiple of
$\langle(A+D)^{n+1}\rangle$.  Agreement with the displayed
Donaldson--Futaki coefficient therefore forces

\[
 \frac{s}{n+1}
 =-\frac{n\alpha^{n-1}\cdot K_X}{(n+1)V},
\]

and hence $s=-nV^{-1}\alpha^{n-1}\cdot K_X$.

The same value is the usual cohomological average scalar curvature when
\(\mathrm{Scal}(\omega)=\operatorname{tr}_{\omega}\mathrm{Ric}(\omega)\):

\[
 \frac{\int_X\mathrm{Scal}(\omega)\,\omega^n}
      {\int_X\omega^n}
 =-n\frac{K_X\cdot\alpha^{n-1}}{\alpha^n}.
\]

## Source locations

- MPWN25 arXiv:2509.09442v1, PDF pp. 1--2, Definition 1.1.1 and the
  displayed formula immediately after the definition: the coefficient of
  $\langle(A+D)^{n+1}\rangle$ in $\mathrm{DF}$ is
  $-n\alpha^{n-1}\cdot K_X/((n+1)\alpha^n)$.
- MPWN25 v1, PDF p. 11, Section 2.3.1, the unnumbered display immediately
  after Lemma 2.3.1:
  $E_A(\phi)=V^{-1}(A,\phi)^{n+1}/(n+1)$.
- MPWN25 v1, PDF p. 13, Section 2.4.2, the two displays defining $M_A$ and
  $s$: $M_A=sE_A+E_A^{K_X}+H_A$ and the printed
  $s=-V^{-1}\alpha^{n-1}\cdot K_X$.
- MPWN25 v1, PDF p. 31, beginning of Section 9.1, repeats both the
  Donaldson--Futaki coefficient containing $n$ and the printed definition
  of $s$ without $n$, making the inconsistency visible on one page.
- MPWN25 v1, PDF p. 31, Theorem 9.1.1:
  $M_A(P_A(f_D))=V^{-1}M^{\mathrm{na}}(\mathcal X,A+D)$.
- MPWN25 v1, equation (9.1.2) on PDF p. 32:
  $E_A(P_A(f_D))=V^{-1}\langle(A+D)^{n+1}\rangle/(n+1)$.
- MPWN25 v1, proof of Theorem 9.1.1 on PDF pp. 33--34: the first displayed
  expansion has coefficient $s/(n+1)$ in front of
  $\langle(A+D)^{n+1}\rangle$, and the proof then identifies the result
  with $V^{-1}M^{\mathrm{na}}$.  Comparing with the Section 9.1 definition
  forces the boxed value.

## Verification status

This is an exact verification input, not a verification receipt.  The
manuscript marker is `% RETHLAS-NEW: mpwn-factor-n-correction`.  The claim
must remain described as pending until the designated xhigh gate returns a
receipt for this exact packet.
