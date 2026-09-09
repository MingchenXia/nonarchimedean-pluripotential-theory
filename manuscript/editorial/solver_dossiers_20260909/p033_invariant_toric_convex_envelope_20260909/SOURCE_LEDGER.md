# P03.3 invariant toric psh envelope — source ledger

Status: source-scoped positive companion result.  It identifies the full
continuous invariant-psh minorant envelope on one toric chamber, and proves
that it agrees with its invariant real-PL subenvelope.  It does not identify
the unrestricted local-Fubini--Study/semipositive-real-PL envelope and does
not retire P03.3.

## Claim-to-source map

| Step | Source / direct argument | Scope control |
| --- | --- | --- |
| Finite convex functions on O correspond to finite continuous invariant psh functions on V | BGJKK25, Theorem 5.3.11, pp. 29--30, specialized to the trivial toric line bundle and zero reference Green function | This is only the maximal-compact-torus-invariant psh class on the inverse image of an ordinary open convex set. |
| The corresponding invariant psh functions are locally psh approximable | BGJKK25, Theorem 5.3.11, pp. 29--30 | The source gives local uniform smooth-psh approximation for finite tropical psh functions. |
| p is finite and convex | Direct supremum argument using one member a_0 of the nonempty competitor family | No compactness or global boundedness of O is used. |
| p is continuous | Direct local chord-slope estimate: on a ball compactly contained in O, a_0 <= p <= phi gives uniform two-sided bounds | This is the automatic local modulus specific to one convex tropical chamber. |
| The invariant real-PL and invariant continuous-psh envelopes agree | Direct supporting-hyperplane argument for the finite convex envelope p | A global affine support at every point belongs to the real-PL minorant class. |
| The invariant semipositive-real-PL subenvelope agrees as well | Theorem 5.3.11 of BGJKK25 makes tropical affine supports psh; the book's P01 comparison turns positive Hessian current into real-PL semipositivity | Requires the added good, separated, strict, boundaryless, pure-dimensional hypotheses. |
| The full invariant local-FS/semipositive-real-PL competitor union is the same subenvelope | GJR26, Definition 7.8 and (7.9): an LFS function is real PL and semipositive at every point | Thus the first alternative contributes no extra \(S\)-invariant competitors beyond the semipositive real-PL class. |

Primary source: J. I. Burgos Gil, W. Gubler, P. Jell, and K. Künnemann,
*Pluripotential theory for tropical toric varieties and non-Archimedean
Monge--Ampère equations*, Kyoto J. Math. 65 (2025),
doi:10.1215/21562261-2024-0010.

https://gubler.app.uni-regensburg.de/Publikationen/2102.07392.pdf

Local-Fubini--Study source: W. Gubler, P. Jell, and J. Rabinoff,
*Forms on Berkovich spaces based on harmonic tropicalizations*, Bull. Soc.
Math. France 154 (2026), Definition 7.8 and (7.9),
doi:10.24033/bsmf.2919.

https://smf.emath.fr/system/files/filepdf/GUBLER_JELL_RABINOFF.pdf

## Deliberate boundaries

1. `O` is an ordinary open convex subset of the dense tropical vector space;
   no toric boundary stratum or nonconvex tropical domain is included.
2. The full raw envelope is only over finite continuous invariant psh
   functions; its agreement with the displayed invariant toric real-PL
   subenvelope does not identify either with the local-FS/semipositive-real-PL
   competitor union without \(S\)-invariance.
3. Nonemptiness is essential to obtain the finite lower bound `a_0 <= p`.
4. The theorem proves a continuous CLD-current psh envelope, but makes no
   statement about the book's unrestricted CLD-v2 classification problem.
5. The exact local-FS/semipositive-real-PL identification is only for the
   invariant subfamily and only on the additional strict, boundaryless
   domain.  It leaves every noninvariant competitor outside the conclusion.
