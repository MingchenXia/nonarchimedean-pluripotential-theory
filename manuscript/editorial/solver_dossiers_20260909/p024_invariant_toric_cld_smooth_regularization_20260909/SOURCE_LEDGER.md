# P02.4 invariant split-toric regularization — source ledger

Status: source-scoped positive companion result.  It proves decreasing
ordinary-CLD-smooth regularization only for finite continuous
maximal-compact-torus-invariant psh functions on one open convex chamber of a
split torus.  It does not identify all classical psh functions on that domain
with this invariant class and does not retire P02.4.

## Claim-to-source map

| Step | Source / direct argument | Scope control |
| --- | --- | --- |
| An invariant finite continuous psh potential descends to a finite tropical psh potential | BGJKK25, Theorem 5.3.11, specialized to the trivial toric line bundle and zero reference Green function | The maximal-compact-torus invariance and finiteness assumptions are essential. |
| The descended potential is convex on the dense chamber | Definition 3.1.2 and Proposition 5.2.6 of BGJKK25 | The argument uses an ordinary open convex subset of \(N_{\mathbf R}\), not a toric boundary stratum. |
| Convex functions admit decreasing smooth convex regularizations on an interior ball | The book's \(\Cref{prop:ch09-radial-mollification}\) | A radial kernel gives both domination and monotonicity as the radius decreases. |
| Pullbacks are ordinary CLD-smooth psh | BGJKK25, Proposition 2.3.4 and Remark 5.3.8 | Positivity is preserved by tropical pullback only for the displayed smooth tropical forms. |

Primary source: J. I. Burgos Gil, W. Gubler, P. Jell, and K. Künnemann,
*Pluripotential theory for tropical toric varieties and non-Archimedean
Monge--Ampère equations*, Kyoto J. Math. 65 (2025),
doi:10.1215/21562261-2024-0010.

https://gubler.app.uni-regensburg.de/Publikationen/2102.07392.pdf

## Deliberate boundaries

1. The result begins with finite continuous invariant psh functions; it does
   not promote an arbitrary classical psh function to that class.
2. The approximation is local on a ball compactly contained in the dense
   tropical chamber; no toric-boundary or nonconvex-domain assertion is made.
3. The approximants are CLD-smooth psh, not required to be harmonic,
   semipositive real PL, or locally Fubini--Study.
4. No conclusion is drawn for noninvariant functions or nonsplit toric forms.
