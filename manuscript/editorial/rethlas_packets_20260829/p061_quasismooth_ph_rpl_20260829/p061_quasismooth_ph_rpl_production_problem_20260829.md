# P06.1 production problem: quasi-smooth pluriharmonic regularity

Date: 29 August 2026

Status: exact quarantined candidate for a production Rethlas audit. Nothing
in this directory is included by the live manuscript, and no novelty or
priority claim is made.

## Exact files to verify byte for byte

- p061_quasismooth_ph_rpl_statement_20260829.tex
- p061_quasismooth_ph_rpl_source_aware_proof_20260829.tex

## Verification request

Audit the exact lemma, theorem, proposition, and proofs against the primary
sources in p061_quasismooth_ph_rpl_primary_source_ledger_20260829.md.
Return a final verdict of correct only if there are zero critical errors and
zero proof gaps. In particular, check all of the following.

1. The target conclusion is real piecewise linearity, $\mathbf R$-PL,
   exactly as in Gubler--Rabinoff, Proposition 7.8. The packet does not
   silently strengthen this to integral PL.
2. The presheaf
   $\mathscr P$ is legitimately defined on every, including globally
   nongood, object of the rigid $\acute{e}$tale site as compatible
   $\mathbf R$-PL sections on its strict affinoid G-domains. Its pullbacks
   are supplied by Gubler--Jell--Rabinoff, Lemma 5.4, and its rigid/G-site
   sheaf condition is supplied by their Section 5.2(4). De Jong--van der
   Put, Section 2.1, identifies the sheaf categories for their special and
   the usual strong rigid G-topologies.
3. De Jong--van der Put, Proposition 3.2.2, has exactly the two conditions
   used: G-sheafiness and the equalizer for every surjective finite
   $\acute{e}$tale morphism of affinoids.
4. In the equalizer proof, for two Berkovich points $y_1,y_2$ over $x$, the
   algebra
   $\mathscr H(y_1)\widehat\otimes_{\mathscr H(x)}\mathscr H(y_2)$ is
   given a bounded multiplicative seminorm by embedding both finite
   separable residue-field extensions in one finite complete valued
   extension. Uniqueness of the extension of the absolute value makes both
   embeddings isometric, so the resulting seminorm restricts to the two
   prescribed point norms. Thus it has a Berkovich point mapping to the
   ordered pair, and compatibility on the fibre square really implies fibre
   constancy.
5. A finite surjection of Berkovich affinoid spaces is a continuous
   surjection from a compact space to a Hausdorff space and hence is a
   quotient map. This proves continuity of the descended function before
   Gubler--Jell--Rabinoff, Proposition 5.11, is invoked.
6. The proof never claims that an arbitrary quasi-$\acute{e}$tale map is
   finite flat or can be refined source-by-source into finite-flat maps onto
   target affinoid domains. Finite flat descent is used only in the finite
   $\acute{e}$tale equalizer demanded by the de Jong--van der Put criterion.
7. Temkin, Corollary 3.3.2, rather than merely Theorem 3.4.1, supplies a
   finite field extension and an actual rigid $\acute{e}$tale covering whose
   affinoid source possesses a strictly semistable affine formal model. This
   is precisely the model hypothesis of Gubler--Rabinoff, Proposition 7.8.
8. Classical pluriharmonicity survives the finite ground-field extension
   and the possibly boundary-bearing quasi-$\acute{e}$tale Berkovich
   pullback by the exact directions of Gubler--Rabinoff,
   Proposition 7.2(6),(7).
9. Real PL descends from $L$ to $K$ by the published
   Gubler--Jell--Rabinoff, Corollary 5.12. The coefficient group
   $\mathbf R$ is divisible as required.
10. Goodness permits localization to strict affinoid neighbourhoods, so
    Temkin's quasicompact and quasiseparated hypotheses are local. The
    theorem consequently needs no global quasicompactness, separatedness,
    or boundarylessness.
11. The final harmonicity assertion follows only after real PL is proved:
    Gubler--Rabinoff, Theorem 4.3, makes both signs semipositive, and
    Gubler--Jell--Rabinoff, Definition 7.2, then applies.
12. On the semistable annulus, the irrational-slope example is classically
    pluriharmonic but cannot be $\mathbf Q$-PL. Check the unit/vector-space
    argument; the finite affinoid subcover extracted from a hypothetical
    admissible PL cover; the Baire argument producing a nondegenerate
    skeletal subinterval in one chart; and the local integral-slope theorem
    for analytic units on a quasi-smooth curve, which makes the slope of a
    finite $\mathbf Q$-linear combination rational on a smaller interval.
13. The theorem is not promoted to singular spaces of dimension at least
    two. A proper generically finite alteration is not covered by the
    finite-flat norm descent theorem.

## Required verdict format

State one of correct, minor fix, or major fix; list every critical error and
every proof gap separately; and give explicit source locations for any
disputed imported claim. Treat a missing descent bridge, a lost strictness
hypothesis, or an unproved change from a rigid $\acute{e}$tale cover to a
finite-flat cover as a critical error.

## Source boundary

The new assembly is the $\acute{e}$tale-sheaf descent of real PL functions
followed by Temkin uniformization. The imported results are limited to those
itemized in the source ledger. The unrestricted singular case remains open,
and the packet claims neither a counterexample to the real-PL statement nor
a descent theorem through arbitrary alterations.
