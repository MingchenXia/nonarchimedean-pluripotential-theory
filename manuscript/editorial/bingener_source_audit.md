# Bingener and Stein-space source audit

Sources inspected on 14--15 August 2026:

- Jürgen Bingener, *Schemata über Steinschen Algebren*, Schriftenreihe des
  Mathematischen Instituts der Universität Münster, 2. Serie, Heft 10 (1976).
- Mingchen Xia, *Stein spaces*, version of 3 July 2026.

The 1976 paper is the provenance source.  The 2026 notes are a modern,
detailed reconstruction and are used to inspect arguments and hypotheses, not
to displace the original attribution.

## Results relevant to this book

1. Bingener §1 constructs relative analytification over the Stein algebra
   \(A=\Gamma(S,\mathcal O_S)\).  In the reconstruction this is Theorem 5.3.1:
   for an \(A\)-scheme that is *interiorly locally of finite type*, the functor
   of morphisms from complex spaces over \(S\) is representable by
   \(X^{\mathrm{an}}\); the comparison map on local rings is flat and induces
   an isomorphism on completions.
2. Bingener (4.2) compares proper higher direct images:
   \(R^p f_*\mathcal F\) analytifies to
   \(R^p f_*^{\mathrm{an}}\mathcal F^{\mathrm{an}}\).  The reconstruction is
   Theorem 5.4.3 and its consequences, including the relative de Rham
   comparison in Corollary 5.4.11.  Properness and the relevant
   finite-presentation/coherence hypotheses are indispensable.
3. Bingener (5.1) and (5.3) algebraize coherent analytic modules near a Stein
   compactum.  The reconstruction's Theorem 5.4.4 treats an excellent Stein
   compact subset \(K\subset S\), an interiorly separated scheme that is
   interiorly locally of finite type, and coherent modules with proper support.
   Only for an interiorly proper \(X\) does Corollary 5.4.12 remove the explicit
   proper-support restriction.
4. Bingener (7.4) is the relative Riemann existence comparison.  The
   reconstruction's Theorem 5.4.6 gives the equivalence of finite étale covers
   of \(X_K\) with germs of finite étale analytic covers near an excellent
   Stein compactum, for \(X\) interiorly of finite type.
5. Bingener, Aussage 2.8, has a narrower and exact signature: \(X\) is a
   proper \(A\)-scheme of finite presentation and \(K\subset S\) is a Stein
   compactum.  After shrinking, its closed constructible sets \(T_n\) have
   analytification equal to the analytic local-dimension-\(\geq n\) locus,
   while \(T_n\otimes_AA_K\) is the union of the algebraic irreducible
   components of dimension at least \(n\).  It then gives
   \(\dim(X\otimes_AA_K)=\dim(X^{\mathrm{an}}|_U)\) for all sufficiently
   small \(U\).  Bingener's immediately following counterexample
   \(S=\mathbf C\), \(X=\operatorname{Spec}A_z\), \(K=\{0\}\) shows that
   the finiteness hypothesis cannot be deleted.
6. For the singleton \(K=\{p\}\), Xia's Corollary 4.4.5 supplies
   excellence and \(\Gamma(K,\cO)=\cO_{S,p}\).  Theorem 5.3.1 gives
   analytification; Theorem 5.4.4 and Corollaries 5.4.12--5.4.14 give
   coherent algebraization, closed subspaces, and morphisms through their
   graphs.  The removal of the explicit proper-support hypothesis uses the
   properness of the ambient projective space.

## Permitted use in the pluripotential-theory manuscript

These results justify relative analytification, comparison, and algebraization
of coherent/model data over Stein bases when their hypotheses are displayed.
They do not establish semipositivity, envelopes, Bedford--Taylor products,
Monge--Ampère measures, or finite-energy theory.  Any proposed local analogue
of Boucksom--Jonsson may use Bingener to move algebraic data across the
relative analytic interface, but its positivity and potential-theoretic
assertions require separate proofs and Rethlas verification.

Mesquita--Piccione uses this interface essentially in Theorem 2.5.5 and
Proposition 2.5.11, which identify restrictions of invariant vertical
divisorial valuations and transport them across bimeromorphic maps.  In
that proof he invokes the equivalence
between projective schemes over \(\mathcal O_{X,p}\) and germs of analytic
spaces projective over \((X,p)\), and then cites Bingener, Aussage 2.8, for
dimension compatibility after the local Zariski center has become a prime
divisor.  The resulting Theorem 2.5.5 feeds Theorem 2.6.4 (PL functions as
vertical Cartier b-divisors), hence Theorem 2.3.6 (divisorial density), and
then Theorem 3.1.1 (the inverse limit of dual complexes).  Consequently the
MP chapters must expose this input in that order; citing MP alone hides a
genuine dependency.

No result from either source may be quoted merely for an arbitrary analytic
family: the audit must check interior finite presentation, separation,
properness or proper support, and excellence of the Stein compactum at the
point of use.

## Normalization findings at the MP interfaces

- The rational PL space in MP24 Definition 1.4.2 is only a
  \(\mathbf Q\)-vector space. Thus MP24 Proposition 4.1.4(2) preserves
  rational PL functions under rational constant translation; arbitrary real
  translation belongs to the real PL extension.
- MP24 equations (3.2.3)--(3.2.4) construct total discrepancy and give it
  value \(1\) at the trivial valuation. Its Proposition 6.2.2 and Corollary
  6.2.3 fail in that literal normalization, as shown by the constant-ray
  test. The later convention is imported from MPWN25 Definition 2.4.1,
  which subtracts one. The expected repair of the MP24 entropy-slope proof
  has the pending packet `tmp/mp24_discrepancy_shift_rethlas_exact.md`; it is
  not asserted as a theorem or marked `RETHLAS-NEW` in the manuscript.
- MPWN25 Definition 2.4.1 explicitly uses the reduced discrepancy
  \(A_{X\times\mathbf P^1}-1\), confirming the convention needed at the
  MP24--MPWN25 interface. Its Lemma 7.1.5 also requires the coefficient
  \(b_i t_i\) on a central component of multiplicity \(b_i\) to realize the
  vertex value \(t_i\); Chapter 61 retains that normalization.
- MPWN25 Section 2.4.2 prints the scalar coefficient without the factor
  \(n\) that is forced by Definition 1.1.1, equation (9.1.2), and Theorem
  9.1.1. The exact packet `tmp/mpwn_factor_n_rethlas_exact.md` passed
  `gpt-5.6-sol` at `xhigh` scrutiny with verdict `correct` and no gaps.
  The production receipt is
  `Rethlas_isolated_20260813_232740/agents/verification/results/20260814T175959Z_484442fcc393/manifest.json`,
  with report
  `Rethlas_isolated_20260813_232740/agents/verification/results/20260814T175959Z_484442fcc393/verification.json`; the verified blueprint is
  `Rethlas_isolated_20260813_232740/agents/generation/results/open_problems/mpwn_factor_n_exact/blueprint_verified.md`.
  Its proof digest is
  `403ac2a601abe51c1d0b4a8852f52b42004332088236a00be3e8460c80af7527`.
- MPWN25 Theorem 7.1.2 proves facewise convexity and interior continuity but
  its printed boundary argument checks only the finite vertex set before
  invoking Proposition 7.1.4. The repaired Chapter 61 proof uses an explicit
  barycentric chord bound to propagate the divisorial estimate to each whole
  simplex, proves that all its points are non-pluripolar, and bounds the
  `d_infty`-diameter of the whole finite dual complex before applying the
  proposition. The exact packet
  `tmp/mpwn_dual_complex_boundary_rethlas_exact.md` passed `gpt-5.6-sol` at
  `xhigh` scrutiny with verdict `correct` and no gaps. The production receipt
  is
  `Rethlas_isolated_20260813_232740/agents/verification/results/20260814T181019Z_3beefd710782/manifest.json`,
  with report
  `Rethlas_isolated_20260813_232740/agents/verification/results/20260814T181019Z_3beefd710782/verification.json`;
  the verified blueprint is
  `Rethlas_isolated_20260813_232740/agents/generation/results/open_problems/mpwn_dual_complex_boundary_exact/blueprint_verified.md`.
  Its statement digest is
  `3beefd710782d6ed51e115d35c3927535c15399b064cc1499e5d9239f861be54`
  and its proof digest is
  `95c4ddb6a737d81e4feaa7e39862f2518b7d63f43235d060f351f07d7aa85973`.
