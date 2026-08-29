# Production-verification problem: P06.2 proper full-rank moment factor

Verify the exact proposition, corollary, remarks, and proofs in
`p062_proper_full_rank_moment_statement_20260829.tex` and
`p062_proper_full_rank_moment_proof_20260829.tex` against the primary sources
identified in `p062_proper_full_rank_moment_source_and_hostile_audit_20260829.md`.

The principal result is the constant-calibration proposition.  The
automatic-calibration corollary is logically separate and must be rejected
or narrowed without affecting the principal proposition if any step in its
top-dimensional balancing argument is not supported by the exact CLD
hypotheses.

Audit all of the following.

1. Check the analytic category, pure dimension, strictness, goodness,
   separatedness, pleasantness, and nontrivial valuation hypotheses needed
   for the CLD current calculus and the GJR conclusion.  Confirm that
   boundarylessness is unnecessary for the forward implication and is
   imposed separately for the converse and automatic-calibration
   corollary.
2. Check that the notation means exactly
   `Omega=F(X)=Pi_F=F(Sigma_F^(n))`, not merely
   `F(X) subset Omega`. Check the explicit identity
   `mu_F=(F|Sigma_F^(n))_*mu_Sigma=m|e_1 wedge ... wedge e_n|`.
   Check that properness means exactly that `F^{-1}(C)` is compact in `X`
   for every compact `C subset Omega`.
3. Check local integrability of `h=phi o F` and the definition of `[h]` for
   an arbitrary continuous, not globally bounded, `phi`.
4. For every compactly supported smooth Lagerberg form `gamma` on `Omega`,
   in every bidegree, check that `F^*gamma` is an ordinary CLD-smooth form
   and that its support is compact. No unproved source-side cutoff or
   pullback of an arbitrary current may be inserted.
5. Check the sign convention.  CLD uses `(log|f_i|)`, while the proposition
   uses `(-log|f_i|)`.  Verify differential functoriality, the transported
   calibration, and that no factor `(-1)^n` appears.
6. Check that CLD §7.1.11 defines the proper current pushforward `F_*` and
   that §7.7.8 makes it commute with `d'` and `d''`. In particular,
   distinguish current pushforward from current pullback and from the
   boundary-sensitive current associated to the differential of a form.
7. Check that CLD Proposition 5.10.1(c),(d) applies to the compactly
   supported top form `phi gamma`, whose coefficients are continuous and
   Borel but need not be smooth. Check its Borel-coefficient pullback and
   every equality proving `F_*[phi o F]=m[phi]`, including all
   normalizations.
8. Check that the resulting equality is the standard Euclidean
   distributional identity `d'd''[phi]=0` on all of `Omega`. Check the
   coefficient-distribution interpretation in CLD §1.6.4, the use of CLD
   Proposition 8.3.2 on relatively compact convex balls, and the passage
   from local affinity to one global affine formula using connectedness.
9. Check the terminal recognition: ordinary CLD smoothness; real piecewise
   linearity and GJR harmonicity directly from GJR Definition 7.2 and
   Remark 7.3(5),(6); and classical pluriharmonicity from GR Proposition
   7.2(2),(3). Check the treatment of the arbitrary real constant term using
   nontriviality of the valuation.
10. Audit the automatic-calibration corollary independently.  Verify that
    the explicit pleasantness hypothesis has exactly the sense of CLD
    Definition 14.1.7, that CLD Theorem 6.6.8 applies because the source has
    no boundary, that the canonical calibration is positive and standard,
    and that harmony on a connected open full-dimensional target forces a
    single positive cell weight.  Check local finiteness, the two-sided
    facet assertion, the generic polygonal path, and the transport through
    `-id`.  Do not infer that the analytic moment is proper merely from
    properness of the topological map `F:X->Omega`.
11. Check the conditional converse independently. On boundaryless `X`,
    verify CLD Theorem 16.7.3 for every unit `f_i` and CLD §7.7.4 for the
    constant term. Confirm that the converse is not asserted with boundary.
12. Test the hypotheses against the cross fan, a nonconstant weighted
    interval, a proper map whose image is smaller than the declared target,
    disconnected targets, and nonproper tropicalizations.
13. Preserve the firewall between current positivity and CLD-psh
    membership: CLD Proposition 8.3.1 is one-way for arbitrary continuous
    functions, and the recent P21.3 continuous-CLD-psh curve packets are not
    a converse for arbitrary continuous zero-current functions.
14. Search the cited primary literature for a theorem or counterexample
    resolving the unrestricted higher-dimensional P06.2 problem.  Do not
    infer a general result from this factorized subclass.

Return `correct` only if the proposition has zero mathematical gaps and all
citations support their exact uses.  Report the corollary separately if its
verdict differs.  Do not broaden the result to an arbitrary continuous
function, a lower-rank or singular tropical image, a nonconstant
calibration, a map that is not proper onto its full image, or a space with
boundary in the reverse or automatic-calibration directions.
