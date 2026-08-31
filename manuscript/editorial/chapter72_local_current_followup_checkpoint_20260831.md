# Chapter 72: local-current comparison follow-up

Date: 31 August 2026.

## Outcome

The current work narrows the bidegree-(0,0) route to P21.3. It does not solve P21.3, the general equivalence of plurisubharmonicity definitions, or the general nontrivially valued envelope problem.

Five components now have fresh independent mathematical reviews: the source description formula, generic common-moment comparison on noncontracted cells, the residual divisor functional on an actual strictly semistable model, the degree-qualified modification/continuous-product transfer diagnostic, and the local multiplicity-tube calculation. Production Rethlas acceptance has not been obtained. No new theorem from this batch has been promoted to the live book, and no open-problem atom has been retired.

The last already-pushed checkpoint at the start of this continuation was 6dacb6866fcd013b8e602b78d52eb784691bb718. The PDF is unchanged at 3,476 pages, SHA-256 c840f3d714ca41841ec7d071902c5a0fcd6f8f5b053027fd06c7c3559bdd3176; it does not contain these new research notes or all recent source-only corrections. No full-book build is claimed.

## 1. Source representation: the formula, not an extra adjective

The exact representation packet remains frozen in

solver_dossiers_20260831/p213_skeletal_packets_20260831/skeletal_representation.

Its statement and proof hashes are respectively
5c06cd6f091e5964a16c07b3efddd2104fed938447605f4f9b19ff8dfea01f1a and
27a344a15fa7d22b2e88c07837aacfca0c978758c5bae5871c5af2d30e47999a.

The fresh audit is

solver_dossiers_20260831/p213_source_skeletal_representation_independent_audit_20260831,

report SHA-256 3f646a1aa73096965cc71e12bcb9ce38f30e2d44d179adda5cb8492721bdcdba,
manifest 739f32df56ec5a39430548ba8c5747eed704911d0c4a871bd95a88a528b07599.

It accepts the displayed source description for compact ordinary source cutoffs, with constant nonnegative top-cell coefficients and no lower-cell residual term. It does not certify the stronger literal local-affine-separation terminology of CLD Definition 7.5.1: the analytic source result establishes differential separation. Eventual exposition must say precisely which description identity was proved.

The review also retains the necessary all-chart nullity condition for lower-dimensional cells, positive-cone decomposition and total-variation nullity, and the affine projection choice in the cutoff argument. A historical pause record, not an invented completed author manifest, supplies the original packet's provenance.

## 2. Common moments: generic source isolation is derived

Candidate:
solver_dossiers_20260831/p213_common_moment_generic_isolation_research_20260831.

Research-note SHA-256
b3ef8bdbae6bce6459fd8b472ace0ed81567d8e465292841fc2331fc421ce079;
manifest 3a80d5a0b68668adeb158bb56bb3689f8f5e63fe18dce0bae4065c4b7e1dd5e0.

Fresh review:
solver_dossiers_20260831/p213_common_moment_generic_isolation_independent_audit_20260831.

Report SHA-256
9ae6e98886763d27abd3c06f258756b182adb69f8a046549efef7cc6c512eb46;
manifest dcffc0fd6bb09f668417735ae5bfa9f1d0f60bd166c2b008d99a113fa458d75f.

For actual moments f and g on the same ordinary source, the combined moment h=(f,g) provides generic ordinary source isolation on a common top cell whenever both coordinate projections have full rank. Thus this source-isolation condition is not merely assumed in that noncontracted situation.

Assuming the representation formula R, comparison of the same pulled-back test form gives b_J=j b_H and a_J=j a_H, where j is the absolute affine determinant and a denotes canonical calibration. The normalized ratio is unchanged. Known CLD geometric ingredients are credited; no priority claim is made.

New h-cells contracted by a projection are genuinely outside this conclusion. Their coefficients do not become known by adjoining units alone.

## 3. A genuine strictly semistable wall, without product splitting

Candidate:
solver_dossiers_20260831/p213_general_snc_wall_residual_functional_research_20260831.

Research-note SHA-256
1c8011863516d8bdc900b3432b270c923126ee36d6600d915f714dc016553ae7;
manifest 2ee5bb8478d7f4cd04b1632af51028c90023cc18323e9db5c8f67deea25d36b8.

Fresh independent review:
solver_dossiers_20260831/p213_general_snc_wall_residual_functional_independent_audit_20260831.

Report SHA-256
a4166d1b73e073cc6e5eefe99c341c43048b2a8f0ad9ea5c7c711e2c58f3ede4;
manifest a0d8d73aa5c19f6580efa035fd9115f3b8feb9176c6a14ff2915b55b45cae867.

The model is integral, proper, regular and strictly semistable over a complete DVR with perfect residue field. Its special fibre is REDUCED. The current is positive and separately d'- and d''-closed of bidegree (0,0), and is defined on the WHOLE tube of a chosen proper residual curve C. The relative dimension may be any n>=2.

The argument constructs actual original-field branch coefficients b_T(p) and proves

\[
 \sum_p\operatorname{ord}_p(f)b_T(p)=0
       \quad(f\in k(C)^\times),\qquad
 b_T(p)=c[\kappa(p):k].
\]

The divisor-functional proof itself does not use R. Only its interpretation as represented source-cell ratios does.

The proof handles nontrivial deformations by bounding the normal radii first and then proving exact leading-term dominance on residual collars. It uses actual Cartier-ideal generators, keeps zero-order bad points, glues ordinary compact cutoffs, and includes the extra simplex term at a further vertical component. No global smoothness of model radii, product neighborhood, residual-current slice or current scalar extension is assumed.

The companion examples distinguish a genuinely nonisotrivial elliptic family from a base-preserving product, component orders from Cartier generators, and fixed-moment tropical balancing from the full arbitrary-current principal-divisor relation. GRW's canonical intersection and corrected-slope statements are not misused as identities for unknown current weights.

## 4. Safe modification transfer and an extension pitfall

Candidate:
solver_dossiers_20260831/p213_zero_extension_derivative_degree_diagnostic_20260831.

Note SHA-256 ecded1c81172a2f42c1d2b00acb2663ee6bc06b4a2929c2ea5b1a3eb634d800c;
manifest 0d18ac6d059e0a61672e962be5c4b59f372e0ba148bd4d0096d1024d911dff7c.

Fresh independent review:
solver_dossiers_20260831/p213_zero_extension_derivative_degree_independent_audit_20260831.

Report SHA-256 daade5bd560e8e92b0ae9aee129273c25f97b255a762429f8e65b6ac2f0d368d;
manifest 1c98af3e5491f8b32558ea149d0da0b239518e0ae05def4026b0e37bb8bdbe53.

The literal unqualified differential-commutation sentence in CLD 7.1.12 fails under its printed definition: on the punctured analytic line the logarithm has zero Hessian, while its unique extension satisfies the Poincare--Lelong formula with a nonzero point mass. The fixed-bidimension extension theorem itself remains valid. This is a bounded source diagnostic, not an official erratum or a rejection of CLD's theory.

The correct dimension-only commutation test uses the OUTPUT bidimension. This still gives a bijection of positive closed-(0,0) cones across a proper modification that is an isomorphism off lower-dimensional analytic exceptional sets.

For a finite continuous u and the transported currents, the safe global formulas are

\[
 \pi_*((u\circ\pi)T_Y)=uT_X,\qquad
 \pi_*\mathrm d'\mathrm d''((u\circ\pi)T_Y)
       =\mathrm d'\mathrm d''(uT_X).
\]

They use coefficient Radon measures and proper pushforward, not an unjustified interchange of Hessian and zero extension. Divisor-borderline removability of the derivative is not proved. The logarithm lacks a finite continuous extension, so it is not a counterexample to P21.3 or to an additional continuous-potential theorem.

The reviewed Chapter 14 paragraph needs a future precise source/wording correction: positive bidimension-(0,0) currents are Radon measures; arbitrary currents of that bidimension need not be. Also distinguish mere pullback vanishing under an intrinsic dimension hypothesis from the stronger ambient-support theorem for closed analytic subsets of sufficiently small dimension. No live Chapter 14 edit is made in this batch.

## 5. Multiplicities: a separately reviewed local calculation

A separate root-authored candidate is frozen at

solver_dossiers_20260831/p213_nonreduced_tube_finite_projection_research_20260831.

Note SHA-256 3001c94985c0d3e60f184ffd9f0e9591775ea026a98cd20ee538005edac11b7a;
manifest d82be02c8b536651f8e9366c407448139c88cf7044158edc419834c515b58fec.

Its fresh independent review is at

solver_dossiers_20260831/p213_nonreduced_tube_finite_projection_independent_audit_20260831.

Report SHA-256 9251b5571386ca23c5e5d6bb5d307559340460a200e8c63a7cffe200d9b54159;
manifest 48bbb80f30fc942f0e945925383814f6e02af7a90148ea56025270b4be1468b0.
The review found no substantive gap within any of the stated scopes.

It studies the actual analytic tube

\[
 x^m\varepsilon(x,z)\prod_jz_j^{a_j}=\pi
\]

with a genuine bounded formal unit epsilon. Its written division argument gives a finite flat projection of degree m, including the whole preimage rather than selected roots. Proper tropical pushforward gives a constant b, and canonical calibration gives m[L:K].

When pi remains a DVR uniformizer and L/K is unramified, rationally independent Gauss radii force ramification index m. This exhausts the entire fibre-algebra dimension and forces one source point. Individual source-cell comparison then remains conditional on R.

This packet does not yet construct a global weighted residual-divisor functional or prove the necessary ordinary-open locality. A separate extension of the vertical-wall proof to nonreduced models is in progress; its status must not be inferred from this local calculation.

## 6. Remaining proof obligations and verification gate

The next geometric steps must retain all of the following distinctions:

1. A log resolution with SNC SUPPORT need not have reduced special fibre; an original-field strict semistable model cannot simply be assumed after blowups.
2. A result for selected vertical components does not automatically cover mixed vertical/horizontal strata of an adapted SNC pair.
3. Transport of T from an ordinary W gives a current only on its actual inverse image, not on every complete residual-curve tube in the model.
4. Finite-moment compatibility on noncontracted cells does not itself give access to all new cells.
5. Results in bidegree (0,0) do not prove the higher-bidegree part of P21.3.

There are still 51 administratively active atoms in 14 problem environments, with tier counts 0/5/12/17/17. This is not a count of 51 untouched literature conjectures: it includes source-covered/project-verification-pending and underspecified entries. No count has decreased in this continuation.

All fresh reviews are scoped AI mathematical reviews, not formal proofs, external peer review, priority determinations or production Rethlas receipts. The previously recorded production submission gate remains unresolved; the original attempt and its single permitted retry timed out during automatic permission review. No alternate endpoint or verifier is used to bypass it, and no live production job is claimed.

The plan is to preserve exact frozen candidates, reviews and qualifications; continue the remaining model/locality calculations; and integrate only after the required production verification. No previously frozen bytes should be overwritten.
