# P03.3 invariant toric real-PL envelope — source ledger

Status: source-scoped positive narrowing.  It does not identify the full
local-Fubini--Study/semipositive-real-PL envelope and does not retire P03.3.

## Claim-to-source map

| Step | Source / direct argument | Scope control |
| --- | --- | --- |
| Continuous invariant functions descend along tropicalization | BGJKK25, equation (5.5), p. 28 | Applied only to an open inverse image in a split torus. |
| A continuous tropical psh function pulls back to a continuous psh function and is locally psh approximable | BGJKK25, Theorem 5.3.11, pp. 29--30 | Applied to the trivial toric line bundle and zero reference Green function on the ordinary open convex set `O`. |
| `p` is finite and convex | Direct supremum argument using one member `a_0` of the nonempty competitor family | No compactness or global boundedness of `O` is used. |
| `p` is continuous | Direct local chord-slope estimate: on a ball compactly contained in `O`, `a_0 <= p <= phi` gives uniform two-sided bounds | This is the automatic local modulus specific to one convex tropical chamber. |

Primary source: J. I. Burgos Gil, W. Gubler, P. Jell, and K. Künnemann,
*Pluripotential theory for tropical toric varieties and non-Archimedean
Monge--Ampère equations*, Kyoto J. Math. 65 (2025),
doi:10.1215/21562261-2024-0010.

https://gubler.app.uni-regensburg.de/Publikationen/2102.07392.pdf

## Deliberate boundaries

1. `O` is an ordinary open convex subset of the dense tropical vector space;
   no toric boundary stratum or nonconvex tropical domain is included.
2. The raw envelope is only over the displayed invariant toric real-PL
   functions `a o trop`, not over all local-FS or semipositive-real-PL
   minorants on `V`.
3. Nonemptiness is essential to obtain the finite lower bound `a_0 <= p`.
4. The theorem proves a continuous CLD-current psh envelope, but makes no
   statement about the book's unrestricted CLD-v2 classification problem.
