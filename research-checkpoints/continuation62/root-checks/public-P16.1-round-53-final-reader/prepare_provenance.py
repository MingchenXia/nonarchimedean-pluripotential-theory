#!/usr/bin/env python3
"""Preserve and verify the two authorized public caches, with LF-indexed excerpts."""
import hashlib
import json
import pathlib
import shutil

ROOT = pathlib.Path(__file__).resolve().parent
DEST = ROOT / 'source-extracts'
DEST.mkdir(exist_ok=True)

SOURCES = [
    {
        'id': 'BJ', 'version': '1801.08229v4',
        'title': 'Global pluripotential theory over a trivially valued field',
        'authors': ['Sébastien Boucksom', 'Mattias Jonsson'],
        'date': '2022-03-22', 'url': 'https://arxiv.org/pdf/1801.08229v4',
        'files': {
            'pdf': ('/workspace/research/shared-sources/P16-arxiv-1801.08229-20261004.pdf', '8d5975337f4ac88a475929ea6a436ec4a15d08715d5582bc0ba0eb3e07152c52'),
            'extract': ('/workspace/research/shared-sources/P16-arxiv-1801.08229-20261004.txt', '659bb8d2e5335781041f03cdb168bac70126487bc0db394f3dac8cf1e9f076d0'),
            'abstract': ('/workspace/research/shared-sources/P16-arxiv-1801.08229-20261004.html', '680fc70f252a7203bf277dccb65c9fddf4f0725c387d2b41b64d467f087c2304'),
        },
        'ranges': [
            ('version_and_abstract', 1, 24),
            ('ambient_general_variety_conventions', 442, 479),
            ('relative_integral_closure_and_vertical_valuations', 735, 880),
            ('model_psh_class_and_Hdom', 1580, 1729),
            ('model_energy_intersection_and_Hodge_estimates', 1730, 2183),
            ('global_psh_definitions_regularization_and_divisorial_determination', 2184, 2719),
            ('compactness_envelopes_unibranch_necessity_and_smooth_nef_input', 2720, 3075),
            ('finite_energy_pairing_mixed_operator_integrability_comparison', 3650, 4688),
            ('extended_energy_uniform_differentiation_dual_energy_and_bounded_J_integration', 4689, 5318),
            ('measure_quasimetric_uniqueness_domination_and_completeness', 5403, 5690),
            ('Dirac_energy_and_divisorial_convergence', 5730, 5830),
            ('strong_topology_abstract_equivalence_nodal_obstruction_countable_regularization', 6010, 6270),
        ],
        'application_checks': [
            'Conventions explicitly allow reduced nonnormal singular projective varieties; Section 7 reintroduces this general scope. Section 12 assumes irreducibility, not smoothness.',
            'Relative integral closure is finite and preserves the nonnormal generic fiber. Absolute normalization has generic fiber X^nu. Vertical R1 gives the DVRs in the atomic intersection formula.',
            'Theorem 7.18 defines mixed measures by pairing against PL tests, which are uniformly dense. Proposition 7.19 proves model agreement, mass, decreasing continuity, integrability and normalization pushforward. These precede the envelope hypothesis.',
            'Energy normalization is ((omega,varphi)^(n+1))/((n+1)V). MA in Section 7.4 is V^(-1) times the diagonal raw measure. Its differential and translation rule therefore use probability normalization.',
            'Theorem 5.11, rather than the smooth Corollary 5.21, supplies normalized psh compactness after the envelope property is supplied by Wu.',
            'Theorem 8.5 and Corollary 8.6 have the general-variety scope. Applying the PL formula to both f and -f and then uniform approximation proves two-sided differentiation. Envelope property identifies E-downarrow with energy of the actual envelope.',
            'Proposition 9.19 controls integration of unbounded psh potentials against the fixed finite-energy target on bounded-J sets. This is essential to attainment of the maximizing supremum.',
            'Corollaries 10.4 and 10.6 assume equidimensionality, which irreducibility guarantees. They give uniqueness modulo one constant and domination without smoothness.',
            'Theorem 12.8 assumes omega ample and X irreducible. Its envelope-to-surjectivity argument uses bounded J, Proposition 9.19 and energy usc. Theorem 12.9 adds smoothness only as a sufficient envelope case.',
            'Corollary 12.18 supplies countable global regularization without the envelope hypothesis, preventing circularity in matching Wu Definition 2.7 to BJ Definition 4.1.',
            'Lemma 5.13 applied to omega_m=(1+1/m)omega gives genuine psh normalization descent. Degree-one projection formula, (7.5), (7.10), (7.18) then give energy, volume, measure, and dual-energy identities.',
        ],
        'corrected_expressions': [
            {'range': [4117, 4127], 'context': 'Proposition 7.21(ii)', 'correct': 'integral phi0 mu = pairing((omega0,phi0),...) - pairing((omega0,0),...)'},
            {'range': [4944, 4970], 'context': 'Corollary 8.6', 'correct': 'fm-eta_m <= f <= fm+eta_m; energy differences <= |t| eta_m; the upper derivative endpoint is integral fm MA + eta_m'},
            {'range': [5245, 5262], 'context': 'Proposition 9.19', 'correct': '|phi_i-phi| = 2 max(phi_i,phi) - phi_i - phi'},
            {'range': [5266, 5304], 'context': 'Theorem 9.20', 'correct': '-integral phi mu <= A J(phi)^(1/2)+B for sup phi=0; rescaling uses the proven I(t phi,0)<=n t^2 I(phi,0)'},
            {'range': [4601, 4619], 'context': 'Proposition 7.45', 'correct': 'I(phi,psi) = integral (phi-psi)(MA(psi)-MA(phi)), with the globally defined sign'},
            {'range': [6126, 6141], 'context': 'Theorem 12.8 reverse implication', 'correct': 'It suffices to use the uniformly bounded increasing net of model competitors for a continuous obstacle; this avoids assuming arbitrary increasing PSH nets are finite-energy.'},
        ],
        'limits': [
            'No smooth sufficient case is imported as a hypothesis of the abstract equation theorem.',
            'The operator exists on more general varieties, but surjectivity needs the envelope property. Example 12.11 gives actual failure on a multibranch nodal curve.',
            'One constant uniqueness is used only for irreducible X; reducible or disconnected domains have prescribed component masses and locally constant ambiguity.',
        ],
    },
    {
        'id': 'W', 'version': '2609.27610v1',
        'title': 'On the local theory of non-archimedean psh functions',
        'authors': ['Lyuhui Wu'], 'date': '2026-09-23',
        'url': 'https://arxiv.org/pdf/2609.27610v1',
        'files': {
            'pdf': ('/workspace/research/shared-sources/new-primary-2609.27610v1-20261004.pdf', '11808a6c9ede9c0158b27e16700fc180a4ac8df12a4586a7178e1958e8f6bba8'),
            'extract': ('/workspace/research/shared-sources/new-primary-2609.27610v1-20261004.txt', 'c8ffe91a631da67f6d3872a1a06ab8d15755aed2f926cdf326725ca3662cef7d'),
            'abstract': ('/workspace/research/shared-sources/new-primary-2609.27610-20261004.html', 'fb78c30f3021e7683a23b91fc2e967cc7a1f3777eb8f083c20823a73d67b663e'),
        },
        'ranges': [
            ('version_introduction_scope_and_chain', 1, 218),
            ('trivial_models_global_psh_definition_and_FS_equivalence', 231, 512),
            ('connected_geometric_fiber_descent', 551, 638),
            ('local_growth_and_global_extension_lemma', 850, 1035),
            ('local_domination_scope_used_in_section7', 1487, 1511),
            ('Runge_polynomial_hulls_distance_regularization', 1580, 1789),
            ('weak_psh_and_theorems6_3_6_5', 1888, 1960),
            ('strict_supporting_functions_countability_and_Runge_patch', 1961, 2110),
            ('finite_norms_projection_induction_and_complete_theorem6_3_proof', 2111, 2695),
            ('body_theorem7_1_and_complete_countability_removal_proof', 2696, 2750),
            ('APW_bibliography_without_identifiers', 2828, 2835),
        ],
        'application_checks': [
            'The body Theorem 7.1 says geometrically unibranch; Theorem A in the introduction only says normal. The body is the theorem applied.',
            'Theorem 6.5 requires a countable dense subfield, but the second half of Section 7 uses finite PL data, countable subfields, contact measure support, base change and domination to remove that condition.',
            'For the trivial reference of an ample Q-line bundle, take a very ample multiple and the complete-linear-system embedding. The reference metric is then the pullback of the trivial projective-space metric, verifying the reference/model reduction actually needed in Theorem 6.5.',
            'Definition 2.7 and Propositions 2.10-2.11 are compared to BJ Lemma 4.3 and countable regularization Corollary 12.18. The resulting global psh cone is identical, not only a locally defined class.',
            'Theorem 6.3 proof uses smooth-locus regularization, singular-stratum induction via Lemma 6.16 and Proposition 6.14, and Runge distance regularization via Corollary 6.9 and Proposition 5.7. The Section 6.1 strict supporting construction is where countability enters.',
            'Geometric unibranchness provides connected geometric resolution fibers; Proposition 2.24 descends their pullback-class psh envelopes. Irreducibility alone or connectedness alone would not suffice.',
            'For the retained algebraically closed trivially valued domain, the countable subfields can be chosen algebraically closed. This verifies BJ applicability on k1 and k2.',
            'The field reduction is re-derived using genuine BJ model measures and general-variety domination Corollary 10.6, instead of citing a smooth BFJ theorem for a singular k2-variety in Wu Theorem 4.16.',
            'Orthogonality is proved by differentiating energy of the constant envelope along the contact obstacle; field pushforward is checked by model intersections and decreasing continuity.',
            'Ample real numerical classes follow by rational classes approaching from above and BJ Lemma 5.9; no countability assumption is added for real coefficients.',
        ],
        'corrected_expressions': [
            {'range': [576, 592], 'context': 'Lemma 2.25', 'correct': 'Use m phi decreasing for phi<=0, not -m phi.'},
            {'range': [2718, 2749], 'context': 'Section 7', 'correct': 'Competitors are psh model functions below f. Correct typing: psi = r_(k/k2)^* psi2, not psi2 = psi composed with a map in the wrong direction.'},
        ],
        'limits': [
            'This is a v1 preprint, not an independently certified proof. Its exact source theorem is used as an allowed mathematical input.',
            'APW26a/b bibliography entries have no identifiers. Their separate texts were not supplied, accessed or independently verified; Wu Theorem 6.3 and its supplied chain, not the unsupplied APW papers, is the local input.',
            'We verify Theorem 6.5 reference reduction only for the trivial ample line bundle reference needed here. We do not infer the arbitrary semipositive model reference case by asserting that every such metric is an embedding metric.',
            'The proof makes no equation claim for arbitrary valued fields, positive characteristic, nonample classes or nonalgebraizable spaces.',
        ],
    },
]

result = {'line_convention': "one-based inclusive ranges; lines = UTF-8 text split('\\n'); literal_text = '\\n'.join(lines[start-1:end]); CR and form-feed bytes are not normalized", 'sources': []}
for spec in SOURCES:
    record = {key: val for key, val in spec.items() if key not in ('files', 'ranges')}
    record['files'] = {}
    for kind, (cache, expected) in spec['files'].items():
        data = pathlib.Path(cache).read_bytes()
        actual = hashlib.sha256(data).hexdigest()
        if actual != expected:
            raise RuntimeError(f'{kind} source hash mismatch: {cache}: {actual}')
        target = DEST / pathlib.Path(cache).name
        shutil.copyfile(cache, target)
        record['files'][kind] = {'cache_path': cache, 'local_path': str(target.relative_to(ROOT)), 'expected_sha256': expected, 'actual_sha256': actual, 'bytes': len(data)}
    extract = (ROOT / record['files']['extract']['local_path']).read_bytes().decode('utf-8')
    lines = extract.split('\n')
    record['LF_split_line_count'] = len(lines)
    record['excerpts'] = []
    for name, start, end in spec['ranges']:
        assert 1 <= start <= end <= len(lines)
        literal = '\n'.join(lines[start-1:end])
        record['excerpts'].append({'id': name, 'start_line': start, 'end_line': end, 'literal_text': literal, 'literal_sha256': hashlib.sha256(literal.encode('utf-8')).hexdigest()})
    result['sources'].append(record)
(DEST / 'source-provenance.json').write_text(json.dumps(result, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
print(json.dumps({'verified_source_files': 6, 'sources': [{'version': s['version'], 'excerpts': len(s['excerpts']), 'LF_lines': s['LF_split_line_count']} for s in result['sources']]}, indent=2))
