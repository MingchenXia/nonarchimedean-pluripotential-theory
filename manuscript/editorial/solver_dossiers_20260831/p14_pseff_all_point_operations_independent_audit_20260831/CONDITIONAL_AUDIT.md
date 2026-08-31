# Independent conditional audit: pseudoeffective all-point realization and operations

Date: 31 August 2026. Reviewer: `/root/p081_weighted_repair_fresh`.

Verdict: **CONDITIONAL PASS for the exact frozen statements and proofs identified below.** I found no unresolved substantive gap in the new deductions, assuming the explicitly named raw-USC, dominated-divisorial, and full Kähler comparison inputs and the cited standard DXZ/MP source interfaces. No candidate revision is required by this audit. This is not a production verdict or a fresh validation of those assumed research inputs.

## Exact bytes and independence disclosure

Candidate directory:

`/private/tmp/nappt_p071_20260827/manuscript/editorial/solver_dossiers_20260831/p14_pseff_all_point_operations_research_20260831/`

| Object | Bytes | SHA-256 |
| --- | ---: | --- |
| `statement.tex` | 3161 | `1ec3db259a1c00302085459a42c2708cec4f3676aa03177a9011552dc474a642` |
| `proof.tex` | 7278 | `52900352bdde0ec57c4ef4c7488d783f29c57b8c4db0beb3df7e3abb884a44fe` |
| `SOURCE_INTERFACE.md` | 2731 | `80a7feb7a167946f1f17221fb1d722953da6eb4e6af25805f2d88d49dcef3130` |
| `MANIFEST.json` | 9571 | `f42fd86160b4a719696d7b0acfec25e741cdfa06c3066a807f9d30a078871add` |

The candidate is root-authored. I did not author its global direct-limit argument, operation proof, or source-interface file and did not edit its bytes. I **did** author the separate dominated-divisorial approximation candidate and its abstract usc-antitone corollary. I also authored the later nef-intersection deduction and previously reviewed the root-authored full Kähler packet conditionally. These contributions are disclosed dependencies, not a basis for independently certifying my own geometric argument here. In this audit, dominated approximation and the full Kähler theorem are assumed propositions; their proofs are not reapproved by this verdict.

The complete current statement, proof, source interface, README, bibliography, syntax wrapper and input ledger were read. All 30 author-manifest entries, including the preserved first layout attempt, and all 11 exact source/research inputs were independently rehashed: zero mismatches. The two principal mathematical files are byte-identical to their first-draft copies. The wrapper diff consists exactly of adding the one-inch geometry setting. The extra source and audit evidence are identified in `SOURCE_INTERFACES.md` and `CHECKS.json`.

## 1. Exact theorem scope

X is a connected compact Kähler manifold. The fixed DXZ input class may be any real pseudoeffective class, including a non-nef or zero-volume one. The MP target of the global statement is explicitly **the union of Kähler-class MP cones as actual functions**. In particular, the statement does not assume MP has already defined a fixed non-nef cone, or identify the DXZ image in such a cone.

The claimed realization retains proper-support semivaluations and possible negative infinite values. It is not a quotient by equality on rational divisorial points. The latter locus is enlarged by the zero valuation o, as in the assumed dominated-density input. The operation formulas at o are justified by the separate finite endpoint formulas; Xia's notation for nonzero divisorial points need not be silently enlarged.

The literal fixed-class statement is an injective order-reflecting map from N(alpha), whose output is MP psh in every Kähler kappa with kappa-alpha Kähler. This is weaker than an intrinsic description of the fixed-class image. The exclusions after the theorem and in the final proof paragraph accurately preserve that distinction.

## 2. Large backgrounds and the ordered direct limit

For any smooth closed representative theta and a fixed Kähler form omega, the eigenvalues of theta relative to omega are bounded on compact X. Choosing M larger than their common upper bound makes M omega-theta Kähler. Thus both the destination class kappa=M[omega] and its difference from alpha are Kähler. A single M handles any finite collection of representatives. This proves the common-upper-class property actually needed for comparison of two direct-limit representatives; no common upper bound for an arbitrary family is assumed.

The same observation identifies the candidate's direct limit over pseudoeffective classes with Xia's construction after equation (3.5). Indeed, for any fixed starting class alpha_0, its classes alpha_0+eta are cofinal upwards: given finitely many classes, a sufficiently large multiple of [omega] is above each of them and above alpha_0 by Kähler differences. Compatibility of the source injections makes the order of the direct limit independent of choices.

On the MP side, a model function determined by a vertical divisor D does not change when its background class is increased. Pullback of a Kähler class is nef; adding it to kappa_X+D preserves relative nefness. Therefore the same decreasing net of PL model functions works in the larger Kähler class. This proves inclusion of MP cones without an unsupported claim about real-model maximum closure or a change of normalization. The union in the statement is consequently a directed union of actual-function cones.

For an arbitrary kappa satisfying the theorem's two positivity conditions, choose a positive form eta representing kappa-alpha and use theta+eta as the displayed target representative. It may not itself be positive, but the standard DXZ change-of-representative identification transports it to a positive representative of kappa. Thus the universal quantifier on kappa is justified, not only the special class M[omega].

## 3. Raw compatibility and representative normalization

The class-inclusion step uses a genuine identity of multiplier ideals in compatible perturbation components. The common finite endpoint is unchanged. Applying any ideal semivaluation, including one assigning infinity to a nonzero ideal, to the same ideals gives the same inner supremum and hence the same raw transform. No topological-density argument enters this step.

For a smooth reference change theta'=theta+ddc h, one first changes a complex potential u to u-h and then takes its normalized I-model envelope in the new representative. Merely subtracting h would generally not produce the normalized model representative. The candidate explicitly calls the identification normalized-envelope based. The multiplier ideals are unchanged by u-h because e^(m h) is locally bounded above and below by positive constants; normalized I-enveloping preserves them by the standard source interface already named in the P14.2 input. The endpoint also remains unchanged. Thus this known cohomological identification preserves the raw function on every ideal semivaluation.

The raw formula is antitone for the coherent-ideal order: increasing v(a) for every ideal increases each inner term and its supremum, and subtraction from finite tau reverses the inequality. Taking the outer supremum preserves the resulting comparison. The inner supremum is nonnegative, giving F_Gamma<=c_Gamma. Its value at o is c_Gamma, so it is never identically negative infinity.

Embedding a fixed object into a Kähler class and applying the assumed full comparison therefore gives literal MP realization in that larger class. Surjectivity of the global map follows by applying the inverse Kähler comparison to any member of the union. For injectivity and order reflection, put the two representatives into a common Kähler class and use the order isomorphism there. This is the correct categorical order test; it does not identify different fixed-class objects merely because the underlying complex potentials happen to share a normalization.

## 4. The two directions of the all-point comparison

The comparison paragraph is valid with a larger Kähler background. Let G be usc, finite above and antitone, and let phi be MP psh in that background with G=phi on D. For each v the **assumed** dominated approximation gives q_lambda<=v and q_lambda->v. Hence G(v)<=phi(q_lambda) for every lambda. Since phi is usc, limsup phi(q_lambda)<=phi(v); equivalently, every strict upper neighbourhood bound for phi(v) eventually bounds phi(q_lambda), proving G(v)<=phi(v). If phi(v)=-infinity, the same argument uses an arbitrary finite upper threshold and forces G(v)=-infinity. No subtraction involving infinities is used.

For the reverse inequality, MP Theorem 4.3.8 applies to phi and the arbitrary usc function G: phi<=G on D implies phi<=G everywhere. G need not already be psh in that background. Merely knowing equality of two arbitrary usc functions on a dense set would not prove the result; the ordered approximation and the MP comparison theorem supply distinct required directions.

This paragraph is logically independent of the desired all-point operation identities. The output DXZ object is first embedded into a larger Kähler class, where its raw function supplies phi. The elementary right-hand side supplies G. The proof never assumes the right-hand side already has the fixed non-nef positivity that is absent from the theorem.

## 5. Source operation types, endpoints, and the printed addition typo

I read Xia v3 Definitions 4.3/4.7/4.9/4.14–4.16, Proposition 4.4, Corollary 4.8, and Lemmas 4.10/4.17 in their compact-Kähler Section 4 setting. They supply existence of the stated operations, their nonzero divisorial values, and their endpoints. Positive scaling in Definition 4.14 uses any real a>0 and changes alpha to a alpha; addition changes the class to alpha+beta. The maximum in the candidate is only asserted for equal input classes, as in the source. Pseudoeffectivity is preserved under positive scaling and addition, so each output is covered by the preceding realization theorem.

The literal display of source Definition 4.16 is not correctly typed: it repeats theta+omega as if both inputs and the output had that same class. `SOURCE_INTERFACE.md` flags and excludes that display. Its replacement construction is correctly typed: at total form theta+theta'+eta, add the positive-system components at theta+eta/2 and theta'+eta/2. Lemma 3.7 supplies the positive-system presentation, and Definition 4.15 supplies positive-curve addition in the sum class. For completeness, different splittings of eta yield the same object: the source divisorial addition identity gives the same sum of input divisorial values and the same endpoint, and the source order/injectivity criterion identifies their images in the common output class. The same argument after a transition proves compatibility of the output components. Thus the cited Lemma 4.17 has a coherent, correctly typed construction behind it; the bad display is not an additional assumption of the candidate.

The surrounding explanatory text of Definition 4.15 also occasionally suppresses the second background when naming a psh space. The input types, the defining envelope's theta+theta' subscript, and Lemma 4.17 make the sum class unambiguous. The candidate uses the correct sum, not that typographical suppression. No fresh full proof audit of Xia's positive-curve operation theorem is claimed here.

## 6. Extended-real operation checks

Translation by finite C, multiplication by a strictly positive finite real number, and finite maximum preserve usc, antitonicity, and a finite upper bound. The endpoint formulas give equality at o, supplementing the source's nonzero divisorial identities. In particular a=0 is excluded, avoiding an undefined product with negative infinity.

For addition, both raw inputs have finite global upper bounds. At a point where both values are finite, the usual two local upper estimates prove upper semicontinuity of the sum. If one input is negative infinity, it has an arbitrarily low local upper bound while the other remains bounded above by its finite endpoint; this proves usc of the sum there as well. Both-negative-infinity causes no new difficulty. No positive infinite value occurs, so the sum is always defined in [-infinity,+infinity). It remains antitone and has finite upper bound c_Gamma+c_Gamma'. Its finite value at o precludes collapse to the identically negative-infinite function.

The output raw function is MP psh in a sufficiently large Kähler background by the first theorem. All hypotheses of the comparison in Section 4 of this audit are now checked for the translated/scaled/added/maximum expression. Therefore the asserted all-point equalities follow. This is not a proof that a finite minimum of psh functions is psh, nor a hidden positivity assumption on arbitrary ideal approximants.

## 7. Decreasing nets and the boundary check

For a decreasing net indexed by a nonempty directed set I and any i_0, the tail I_{>=i_0} is cofinal: for each i there is j>=i,i_0. Monotonicity then implies equality of the infimum over the tail and over all I. Every function on that tail is bounded above by c_{Gamma_i0}. No countability, sequence extraction or total order of I is needed.

The pointwise infimum G is usc because {G<t} is the union of the open sets {F_i<t}, for each finite real t. It is antitone, and its upper bound is finite. The lower endpoint condition gives G(o)=inf_i c_i in R; since a fixed tail supplies an upper bound, the endpoint is not positive infinity either. Definitions 4.9 and Lemma 4.10 produce a nontrivial DXZ output in the original pseudoeffective class with exactly these endpoint and divisorial infimum values. The all-point comparison therefore applies again. No interchange of the raw formula's suprema with the infimum is required.

If inf_i c_i were negative infinity, the source permits a formal negative-infinity symbol, but the theorem deliberately does not claim a nontrivial DXZ output in that case. The hypothesis is neither discarded nor implicitly replaced by a bound only at selected points.

The final truncation diagnostic is valid: in a Kähler class a constant object -j exists, and at a proper-support point with raw value negative infinity the maximum has value -j, decreasing to negative infinity. The example is not used to assert the availability of a constant zero object in every fixed non-nef class.

## 8. Mechanical provenance and remaining gates

The author's preserved final draft log records one underfull bibliography hbox, no error, undefined citation/reference, overfull box, or LaTeX warning. The author already separated the underfull line in BUILD.json. The independently checked label/reference counts are 9/12. No PDF occurs in the packet, and the log has the draftmode marker. I did not rerun the writing build script, create a PDF, or change any candidate, live manuscript, inventory, or frozen dependency.

The first attempt is preserved, including its layout evidence; the current statement and proof are exactly unchanged. The only wrapper change is page geometry. This provenance is compatible with the mathematical audit, but neither a successful draft build nor preservation of labels is mathematical evidence.

No substantive correction is requested. The result remains conditional on the named new inputs and requires production review under the existing gate. It does not characterize the intrinsic image of a fixed non-nef class, prove fixed-class relatively-nef model density, define a class-specific Monge–Ampère measure or energy at zero volume, assert continuity of envelopes, extend increasing supremum identities without regularization, or retire the whole pseudoeffective P14.3 problem.
