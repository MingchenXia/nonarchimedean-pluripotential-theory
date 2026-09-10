# P03 invariant toric upper-semicontinuous envelope — source ledger

Status: source-scoped positive companion result.  For every
upper-semicontinuous invariant obstacle admitting a finite convex minorant,
it identifies the full continuous invariant-psh minorant envelope on one
toric chamber and proves that it agrees with its invariant real-PL
subenvelope.  It does not identify the unrestricted
local-Fubini--Study/semipositive-real-PL envelope and does not retire a P03
atom.

## Claim-to-source map

| Step | Source / direct argument | Scope control |
| --- | --- | --- |
| Finite convex functions on O correspond to finite continuous invariant psh functions on V | BGJKK25, Theorem 5.3.11, pp. 29--30, specialized to the trivial toric line bundle and zero reference Green function | This is only the maximal-compact-torus-invariant psh class on the inverse image of an ordinary open convex set. |
| The corresponding invariant psh functions are locally psh approximable | BGJKK25, Theorem 5.3.11, pp. 29--30 | The source gives local uniform smooth-psh approximation for finite tropical psh functions. |
| p is finite and convex | Direct supremum argument using one member a_0 of the nonempty competitor family | No compactness or global boundedness of O is used. |
| p is continuous | Direct local chord-slope estimate: on a ball compactly contained in O, a_0 <= p <= phi gives uniform two-sided bounds; finiteness plus upper semicontinuity of phi gives the upper bound | This is the automatic local modulus specific to one convex tropical chamber. |
| The invariant real-PL and invariant continuous-psh envelopes agree | Direct supporting-hyperplane argument for the finite convex envelope p | A global affine support at every point belongs to the real-PL minorant class. |
| The invariant semipositive-real-PL subenvelope agrees as well | BGJKK25, Theorem 5.3.11; \(\Cref{thm:cld-to-classical-psh}\); \(\Cref{thm:gr-pl-comparison}\); and GJR26, Theorem 7.14 | Affine supports are CLD-psh, hence classically psh and semipositive on a good strict domain; GJR's one-way current theorem puts every semipositive competitor back in the psh class on the added good, separated, strict, boundaryless domain.  No pure-dimensionality hypothesis is needed. |
| The full invariant local-FS/semipositive-real-PL competitor union is the same subenvelope | GJR26, Definition 7.8 and (7.9): an LFS function is real PL and semipositive at every point | Thus the first alternative contributes no extra \(S\)-invariant competitors beyond the semipositive real-PL class. |
| The common invariant envelope is CLD-v2 psh, already at the first decreasing stage | \(\Cref{cor:p024-invariant-toric-cld-smooth-regularization}\) applied to \(P^S_Vf=p\circ\operatorname{trop}\) | The upper-semicontinuous obstacle is finite once a finite minorant exists, and the resulting envelope is finite and continuous. |
| The common invariant envelope is classically psh | \(\Cref{thm:cld-to-classical-psh}\) | This is the one-way CLD-v2-to-classical comparison; no converse is used. |

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
4. The first-stage CLD conclusion uses the separate P02.4 invariant-toric
   corollary, and its classical-psh conclusion uses the one-way CLD
   comparison.  They apply to every displayed upper-semicontinuous obstacle
   with a finite convex minorant, and make no statement about noninvariant
   competitors or the book's unrestricted classical-psh or CLD-v2
   classification problems.
5. The exact local-FS/semipositive-real-PL identification is only for the
   invariant subfamily and only on the additional good, separated, strictly
   analytic, boundaryless domain.  It leaves every noninvariant competitor
   outside the conclusion.
