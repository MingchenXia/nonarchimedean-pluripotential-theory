from pathlib import Path
import hashlib, json, shutil

ROOT = Path(__file__).resolve().parent
data = json.loads((ROOT / 'input.json').read_bytes())
assignment = data['assignment']
start = assignment.index('[\n  {\n    "arxiv_id"')
end = assignment.index('\n]\n\nNew literal-source', start) + 2
bindings = json.loads(assignment[start:end])
(ROOT / 'source-extracts').mkdir(exist_ok=True)
manifest = json.loads((ROOT / 'source-manifest.json').read_text())
checks = []
for record, binding in zip(manifest, bindings):
    record['public_source'] = binding['public_source']
    record['title'] = binding.get('title', record['id'])
    record['primary_files'] = []
    for kind in ['literal_extract', 'pdf', 'abstract_html', 'html']:
        if kind not in binding:
            continue
        expected = binding.get({'literal_extract': 'extract_sha256', 'pdf': 'pdf_sha256',
                                'abstract_html': 'abstract_sha256', 'html': 'html_sha256'}[kind])
        p = Path(binding[kind]); raw = p.read_bytes()
        actual = hashlib.sha256(raw).hexdigest()
        assert expected == actual, (record['id'], kind, actual, expected)
        suffix = '.txt' if kind == 'literal_extract' else p.suffix
        copy = ROOT / 'sources' / (record['id'] + ('-' + kind if suffix == '.html' else '') + suffix)
        if kind == 'literal_extract':
            copy = ROOT / record['copy']
        copy.write_bytes(raw)
        record['primary_files'].append(dict(kind=kind, source=str(p), copy=str(copy.relative_to(ROOT)),
                                             sha256=actual, bytes=len(raw)))
        checks.append(dict(id=record['id'], kind=kind, sha256=actual, matched=True))

# Complete literal units include statements and their proof bodies. Retention is
# deliberately distinct from accepting a theorem or auditing its dependencies.
units = {
 'BJ': [(435,480,'domain'),(745,865,'relative-closure'),(980,1037,'PL-density'),(1758,1845,'model-positivity'),
        (2360,2550,'divisorial-order'),(2797,2893,'EP-compactness-descent'),
        (2894,3030,'envelopes-and-smooth-EP'),(3649,3945,'energy-pairing'),
        (3971,4155,'mixed-MA-and-weighted-continuity'),(4531,4619,'locality-comparison'),
        (4826,4960,'outer-energy-differentiation'),(4970,5156,'dual-energy-and-maximizers'),
        (5180,5301,'bounded-J-integrals'),(5417,5571,'uniqueness-domination'),
        (5758,5795,'finite-energy-Diracs'),(6080,6158,'conditional-equation'),(6227,6267,'already-genuine-sequences')],
 'Wu': [(645,707,'local-definitions'),(752,797,'growth-definition'),(860,905,'polytopes'),
        (950,1038,'controlled-approximation'),(1532,1730,'Rossi-and-printed-smooth-regularization'),
        (1731,1837,'Hartogs'),(1838,1890,'pole-counting'),(1924,2110,'strict-potential-and-local-hull'),
        (2200,2372,'trace'),(2373,2533,'split-proof'),(2534,2692,'two-inductions'),
        (2694,2747,'EP-and-cardinality'),(567,624,'connected-fiber-descent')],
 'BE': [(1987,2063,'same-class-FS-difference'),(2240,2357,'generated-PSH-and-nef-metrics'),
        (2640,2768,'continuous-mixed-products'),(3125,3177,'Deligne-comparison'),
        (3430,3530,'relative-volume'),(3590,3670,'continuous-psh-energy')],
 'GM': [(270,405,'formal-representation-extension'),(632,695,'nef-model-detection'),
        (727,820,'local-semipositivity')],
 'GR': [(70,164,'scope-and-warning'),(818,941,'curve-test')],
 'GJR': [(2298,2425,'nef-locality-base-change')],
 'Ducros': [(2070,2275,'finite-polyhedral-images')],
 'Thuillier': [(3580,3620,'unit-log-harmonicity'),(3810,3870,'decreasing-subharmonic-functions'),(5322,5380,'slope-positivity')],
 'Wanner': [(105,155,'field-and-curve-domain'),(405,470,'subharmonic-definitions')]
}
units['CLD'] = [(10432,10530,'continuous-current-diagnostic'),(25583,25650,'model-psh-diagnostic'),(27926,28068,'represented-integer-metrics')]
excerpts = []
applications = {
 'BJ': ('Use the stated general-projective genuine operator, exact mass, intrinsic targets, comparison/uniqueness and conditional equation theorems with the corrections detailed in paper Section2.',
        'No new singular EP follows; Theorem12.8 needs EP. Outer differentiation is not unbounded envelope attainment. Source-cited relative-volume inputs outside these caches are not independently reproved.'),
 'Wu': ('Audit diagnostic local definitions, controlled growth, strict-contact/Runge/trace/induction and EP bodies against paper Sections3–9; do not import their conclusions as premises.',
        'Printed lower-growth4.19 has the supplied independently reconstructed counterexample; the repaired upper-growth and final EP theorems are not disproved. Full analytic antecedents remain unproved.'),
 'BE': ('Check exact model-to-FS differences, common-class cancellation, nontrivial-field ample nef approximation and continuous genuine product/energy scope.',
        'Actual model/PL representation and continuous psh membership are prerequisites. 9.15 concerns continuous psh metrics;9.16 assumes envelopes. This supplies no singular EP by itself.'),
 'GM': ('Check formal representation/compact extension and local semipositivity hypotheses for the proposed rational metric bridge.',
        'A strict analytic G-cover and actual fixed-bundle transition cocycle must be constructed first. The combined new bridge remains an explicit gap.'),
 'GR': ('Check represented R-PL curve nef criteria, Proposition5.1 and Corollary5.4, before applying them to the proposed rational bridge.',
        'Remark1.8 does not give arbitrary positive-current pullback or a converse. Actual PL membership is indispensable and not fully reconstructed here.'),
 'GJR': ('Check local represented-model nefness and its scalar-extension/surjective-descent statements for the proposed bridge.',
         'Does not prove the initial local rational metric representation or singular EP.'),
 'Ducros': ('Use compact strict invertible-function image theorem as a proposed representation input; retain the complete proof.',
            'Dimension is at most analytic dimension, not an unconditional equality. Infinite-coordinate charts and a genuine strict domain must precede the application.'),
 'Thuillier': ('Retain analytic-unit harmonicity and subharmonic slope/decreasing bodies needed by the proposed curve bridge.',
               'Curve and field hypotheses must be met after scalar extension; the new all-residue-field trace application is not certified.'),
 'Wanner': ('Check the actual curve/field domain of the subharmonic/current comparison.',
            'A proper algebraic compactification must precede any smooth-proper-curve application; no arbitrary analytic map becomes algebraic.'),
 'CLD': ('Check local-uniform continuous-current limits and represented strict-integer model metric statements.',
         '8.7.2 is locally uniform for continuous inputs, not a bounded-decreasing theorem;17.8.4 is nef-to-psh for already represented strict-integer PL metrics.')
}
for record in manifest:
    lines = (ROOT / record['copy']).read_bytes().decode('utf-8').split('\n')
    for a,b,name in units[record['id']]:
        assert 1 <= a <= b <= len(lines)
        literal = '\n'.join(lines[a-1:b])
        dest = Path('source-extracts') / f"{record['id']}-{a}-{b}-{name}.txt"
        (ROOT / dest).write_bytes(literal.encode('utf-8'))
        excerpts.append(dict(id=record['id']+'-'+name, version=record['version'],
                             source=record['source'], source_sha256=record['sha256'],
                             inclusive_one_based_LF=[a,b], literal_file=str(dest),
                             literal_sha256=hashlib.sha256(literal.encode()).hexdigest(),
                             literal=literal, role='Source statement/proof data; acceptance and application scope are in the paper.',
                             application=applications[record['id']][0], concrete_limits=applications[record['id']][1]))
(ROOT / 'source-manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
(ROOT / 'source-extracts/source-provenance.json').write_text(json.dumps({
 'LF_convention':'UTF-8 bytes decode and split("\\n"); inclusive one-based ranges',
 'sources':manifest,'excerpts':excerpts,
 'limits':'Complete source copies and literal units are retained. No whole-source independent correctness audit is claimed. Wu v1 and all embedded generated proofs are diagnostic until reconstructed.'
},ensure_ascii=False,indent=2)+'\n')
(ROOT / 'source-checks.json').write_text(json.dumps({'checks':checks,'count':len(checks),'excerpts':len(excerpts)},indent=2)+'\n')
print(json.dumps({'matched_primary_hashes':len(checks),'literal_units_retained':len(excerpts)}))
