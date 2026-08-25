# P03 nodal local-envelope counterexample

## Disposition

The unrestricted local-envelope assertions are false, even for a continuous
real-valued obstacle on a reduced strict affinoid curve.  On

\[
U=\mathcal M\bigl(K\langle x,y\rangle/(xy)\bigr)
\]

the obstacle in `prop:ch15-nodal-local-envelope` has a raw local-FS/
semipositive-real-PL envelope equal to zero on the punctured `x`-branch and
to a negative constant on the entire `y`-branch.  Upper-semicontinuous
regularization changes only the value at the node.  The resulting function
is discontinuous and is neither classically psh nor CLD-v2 psh.

This disproves the three unconditional universal assertions.  It does not
classify envelopes on normal or analytically unibranch domains, so the three
P03 classification atoms remain open.

## Construction

Choose `varpi` with `r=|varpi|<1` and put `a=-log r`.  Write
`A=V(y)`, `B=V(x)`, and let `o` be their common origin.  The continuous
obstacle is zero on `A` and

\[
-a\min\{r^{-1}|y|,1\}
\]

on `B`.  For every positive integer `m`, the function

\[
h_m=\max\{m^{-1}\log|x|,-a\}
\]

is a finite real-PL function: the apparent pole is confined to
`|x|\le r^m`, where the displayed maximum is the constant `-a`.  Pullback to
the normalization, the logarithm/maximum rules, finite-surjective descent,
and the PL/classical comparison prove semipositivity, including at the node.
The functions `h_m` are admissible, are identically `-a` on `B`, and tend to
zero pointwise on `A\setminus\{o\}`.

On the closed `y`-disc `D_r`, the `r`-Gauss point is its unique Shilov point.
Every admissible competitor is classically psh.  The affinoid maximum
principle therefore bounds it above by its value at that point, hence by
`-a`, throughout `D_r`; the obstacle gives the same bound outside `D_r`.
This determines the raw envelope exactly.

Points on the punctured `x`-branch converge to the node, so usc
regularization assigns value zero there.  Its restriction to `D_r` then has
an interior maximum zero at the node while its Shilov value is `-a`,
contradicting the affinoid maximum principle.  The CLD-v2 conclusion fails
because CLD-v2 psh functions are classically psh.  A sequence on the other
branch proves discontinuity.

## Adversarial checks

- “Locally Fubini--Study” is used only for the positive source class; no
  arbitrary signed maximum expression is admitted.
- The functions `h_m` are admitted as semipositive real-PL competitors; they
  are not asserted to be locally Fubini--Study.
- The disc `D_r` is strict because `r=|varpi|`, and restriction is analytic
  pullback.
- The singleton Shilov boundary is proved directly from the Gauss norm.
- Gubler--Rabinoff Theorem 6.4, not Theorem 6.5, supplies the affinoid
  maximum principle.
- The counterexample exploits reducibility at a node; it proves no positive
  or negative classification in the analytically unibranch setting.

## Primary inputs

The proof uses Gubler--Rabinoff, Proposition 3.5(2), (4), and (8),
Proposition 4.2, Section 4.1.2, Theorem 4.3, Theorem 6.4, and the
CLD-to-classical implication recalled in Section 1.2.  These sources do not
themselves state an envelope theorem.  The book-level construction carries
no novelty or priority claim.

## Production verification

- Run: `20260825T094005Z_10ac70696f69`
- Item: `pi_31f95353b7e94f3cb98b09b6`
- Model / reasoning: `gpt-5.6-sol` / `xhigh`
- Verdict: `final/correct`
- Critical errors / gaps: `0 / 0`
- Exact statement SHA-256:
  `10ac70696f69b1ed18ae1522c0b065fe9240d8f921b9db258201c9e8a7b509e1`
- Exact proof SHA-256:
  `21fc22e5b1f3b3084f29df412a57485131e46ca160cf168db18da8a3e2559fc7`

The exact statement and proof remain byte-identical to the live Chapter 15
slices recorded in the corresponding integration receipt.
