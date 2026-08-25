# Remaining source questions from Gubler--Jell--Rabinoff

The unrestricted cohomological item formerly numbered 2 is **closed
negatively**.  A Rethlas generation run using `gpt-5.6-sol` at `xhigh`
returned `final/correct`, with zero critical errors and zero gaps, for the
good-reduction elliptic-curve counterexample.  The exact-current integrated
production run is `20260824T123617Z_fcddc3abc33d`; its source-aware proof
digest is
`99d7583f90ebf7dcb56a40dcc04463ffcb0c04ee4c1c711e0acafacdc85dbe2c`,
and its receipt is
`manuscript/editorial/rethlas_receipts_20260824/ch18_gjr_cohomology_counterexample_exact_current_receipt.md`.
The two unrestricted questions below are stated in Gubler--Jell--Rabinoff,
arXiv:2111.05741v3.  The first now has the complete positive-cone solution in
residual dimension at most one; its higher-dimensional remainder stays open.

Treat the following independently.

1. Immediately before Proposition 7.5 the authors ask whether its local
   finite integral-decomposition characterization of harmonic
   \(\Lambda\)-PL functions has a semipositive analogue.  Formulate the exact
   analogue for \(\Lambda=\mathbf Z\) or a divisible subgroup containing
   \(1\), and determine whether a semipositive \(\Lambda\)-PL function is
   locally a finite \(\Lambda\)-linear combination of integral semipositive PL
   functions with the coefficient/sign conditions actually needed for
   semipositivity.  Chapter 18 proves that the answer is affirmative when
   \(\operatorname{trdeg}_{\widetilde K}
   \widetilde{\mathscr H(x)}\leq1\): the coefficients can be taken in
   \(\Lambda_{\geq0}\), and all but at most
   one integral summand are harmonic.  Exact-current Rethlas run
   `20260824T135721Z_81346238f7dd` returned `final/correct`, zero critical
   errors, and zero gaps.  Do not extrapolate this one-degree argument to a
   higher-dimensional, possibly nonpolyhedral nef cone.
2. Remark 16.4 retracts an argument in earlier work that assumed the canonical
   tropicalization of every abelian variety is smooth.  Is a canonical metric
   on a line bundle on an abelian variety nevertheless an ordinary
   \(\delta\)-metric, rather than only an object in the enlarged weakly smooth
   formalism?

For item 1, do not confuse an arbitrary real linear decomposition with a
positive-cone decomposition.  For item 2, account for the mixed-reduction
abelian threefold in Section 17 whose canonical tropicalization is not smooth.
Weak smoothness is not ordinary CLD smoothness.  Return known special cases,
conditional reductions, counterexamples, and open remainders separately.

For chronology, the deleted item asked whether
\(\Lambda^{p,q}M_{\mathbf R}\hookrightarrow H^{p,q}(A)\) is always an
isomorphism.  If \(A\) is a good-reduction elliptic curve, then \(M=0\), while
Gubler--Jell--Rabinoff Theorem 1.14 gives
\(\dim H^{1,1}(A^{\mathrm{an}})=1\).  Hence the unrestricted answer is no.
The totally degenerate restriction is not settled by this counterexample.
