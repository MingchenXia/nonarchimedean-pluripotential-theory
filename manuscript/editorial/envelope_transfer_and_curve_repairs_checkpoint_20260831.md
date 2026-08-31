# Envelope transfer and curve-proof repair checkpoint

31 August 2026. Base: `4ec9fb514e9d33d0f8e1b6d918d6264a104cb676`.
This is research and proof-repair progress, not a release or a general
nontrivially valued envelope theorem. The preceding status-only turn made
no mathematical progress; this continuation inspected current files and
produced the concrete new evidence and candidates below.

## Candidate envelope transfer

The root and p082_independent_reaudit developed an exact weighted-FS
extension argument for a smooth integral projective variety X over an
algebraically closed trivially valued k, an ample L defined over k, and
K=k((t)). For an FS potential in [-M,0], one fixed integer C>=max(1,M)
gives an extension to the actual line bundle p*L tensor q*O(C) on X x P1.
The extension is globally bounded in [-C,1], with uniformly bounded
normalized section weights. Strict Laurent-tail estimates preserve the
potential exactly at every point of the full analytic fibre. Negatively
weighted padding removes central and infinite base loci.

The scaling collar of that full fibre supplies the missing control of
ambient upper-semicontinuous regularization. A product-net argument and
lower truncation then give an envelope-transfer theorem conditional on
the stated trivial-field EP input. The target class is explicitly the
decreasing-FS metric class of Boucksom--Eriksson Definition 7.2.

Frozen candidate:
`solver_dossiers_20260831/p081_uniform_fiber_extension_research_20260831/`.

- Statement SHA256: `4a758e5271862cad16c2242c5a2778c49de3cb4bff4797ff2a5d22ef0b00b503`.
- Proof SHA256: `f1b2014cbc612885421d1df26383f146809a0e621c43c98ea30993bf1f3ad3fa`.
- SHA256SUMS: `97a7c2bacd9aeabd7eafc7ebce32cc4ba253a88c573f4317efd74ba62abda262`.

The root read the complete statement/proof and checked the primary
BJ22 Example 3.9 and Theorem 4.15(iii), the BE v3 Definitions 5.2/7.2
and Lemma 7.4/Corollary 7.5, and the supplied unibranch paper's exact
introductory theorem. This root review is NOT independent: the root
contributed substantive arguments. A genuinely separate review has been
assigned to p081_weighted_repair_fresh. Production Rethlas remains pending.

No arbitrary-field, nonconstant-variety, arbitrary numerical-class,
continuous-obstacle-continuity, or CLD/BFJ-identification claim is made.
No novelty/priority or open-problem retirement is asserted. A separate
nonconstant curve-base extension investigation is ongoing, not an input.

## Chapter 29/31 assembly

The root read both complete first-assembly fragments. The independent
audit found that the reverse positivity implication for real model forms
needed an explicit local-potential argument, not just scalar pushforward
and final nef reflection. Revised2 now uses local real sums of lisse
weights, subharmonicity, scalar pullback, individual upstairs component
degrees, and only then nef reflection. It also includes the nonsplit
degree calculation and the two-edge rational-mass/irrational-slope example.

Frozen revised2 manifest:
`solver_dossiers_20260831/p081_ch29_ch31_weighted_full_scope_isolated_repair_20260831/revised2/MANIFEST.json`,
SHA256 `c36b29ce080d0269955f58f3dd8069561338c75afafe49657c4e2f1e229176ec`.

Independent assembly audit:
`solver_dossiers_20260831/p081_ch29_ch31_assembled_independent_audit_20260831/INDEPENDENT_ASSEMBLY_AUDIT.md`,
SHA256 `59038867a7128f6361620623e42da19a9f64a2cded08d6832bef6cb69cb556c9`.
Its no-gap verdict is bounded by the explicitly accepted inputs and does
not remove downstream, production, or full-manuscript integration gates.

The root also inspected every rendered page of the seven-page weighted
revised1 PDF (SHA256 adeff24075da261d1ff7766d158094273a7d06ec8a823f4c5dad2d0e95a38b4d).
No visible layout defect was found. This does not certify assembled
chapter layout, mathematics, or the complete book.

## Chapter 23 and energy consumers

The old Ch23 model-vs-psh proof enlarged a skeleton after selecting an
approximation on it. The root's isolated repair keeps the skeleton fixed
and uses chi<=chi composed with retraction instead of equality. It
preserves the proof's real-model convention and its 4-epsilon estimate.

A new full-BFJ chord bridge preserves the arbitrary-psh conclusions of
the numerical example and fixed-model discussion. It uses fixed-skeleton
approximation and closed finite vertex inequalities, not an identification
of the rational-model envelope with an all-psh envelope. The refinement
pushforward step is explicitly proved for nonfactoring functions by
zero-total-mass cancellation on each attached graph piece. The root read
Thuillier Proposition 2.2.26 in full to distinguish this argument from
the proposition's narrower pullback identity.

Independent review requested three clarifications, now included in
`solver_dossiers_20260831/p081_ch23_curve_consumer_repair_20260831/revised1/`:
fixed regular SNC subdivision before invoking BFJ inputs; rational blowup
centres in the unit-weight example; and correct analytic contact-set and
reference-adjusted curvature language. All 178 old labels survive, with
one new bridge label. The patch passes git apply --check against the base;
that check is not mathematical verification.

- Ch23 revised1 bridge SHA256: `ac5d104c5d94191e0546bfab5160c9d54c461b76ecf02b6ba005911ebc9b78c1`.
- Full proposed chapter SHA256: `cb9d7c65bdf64b2b52c32483877f13a143b59d07615fc6d5f9ff3ced0d0e2e06`.
- Patch SHA256: `ab980a9e71452778b9f0f04f007a55044db3bd06db9e25db1ca42bfd76cea1a4`.

The downstream audit additionally found missing residue-degree weights
in Ch26/28 energy formulas under nonsplit hypotheses. A degree-two-node
example gives energy -1 where the printed unweighted formula gives -1/2.
A separate weighted repair preserving the original real-form and
connected-curve hypotheses is being authored. Ch20 also has a graph
sentence equating node count with intersection number without residue
degrees; it must be included in the subsequent consistency pass.

## Release boundary

No live chapter was changed in this continuation. No new production
submission was made, and no permission workaround was used. The existing
production approval gate remains unresolved. These proposals must not be
integrated as established mathematics before their required review and
production gates. The existing 3476-page draft is unchanged and retains
its earlier proof warnings; the newly detected downstream defects are
recorded here and in the independent audit, not silently certified.

Inventory remains 51 active atoms in 14 formal problem environments.
The overall book/research goal remains active and far from complete.
