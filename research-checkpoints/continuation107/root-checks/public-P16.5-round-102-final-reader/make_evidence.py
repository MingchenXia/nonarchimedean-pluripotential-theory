#!/usr/bin/env python3
"""Build a checked statement-to-literal-passage ledger from retained supplied/public data."""
import hashlib, json, pathlib, re, sys

ROOT = pathlib.Path(__file__).resolve().parent
def sha(b): return hashlib.sha256(b).hexdigest()
def write_json(p, v):
    (ROOT / p).write_text(json.dumps(v, ensure_ascii=False, indent=2) + '\n')
supplied = json.loads((ROOT/'granted/block-02.json').read_text())
assignment = json.loads((ROOT/'input-original.json').read_text())['assignment']
blocks = list(re.finditer(r'BEGIN MATHEMATICAL DATA: ([^\n]+)\n([\s\S]*?)\nEND MATHEMATICAL DATA', assignment))
assert len(blocks) == 5
for i,m in enumerate(blocks):
    assert (ROOT/('granted/block-%02d.txt' % i)).read_text() == m.group(2), i
additional_units = json.loads((ROOT/'granted/block-03.json').read_text())
for expected,literal in additional_units.items():
    b=(ROOT/('supplied-primary-units/'+expected+'.txt')).read_bytes()
    assert b.decode()==literal and sha(b)==expected, expected
sup_units = {u['unit']: u for p in supplied['premises'] for u in p['passages']}
for u in sup_units.values():
    b = (ROOT/u['artifact']).read_bytes()
    assert b.decode() == u['literal'] and sha(b) == u['sha256'], u['unit']

# Keep distinct coordinates: supplied inclusive one-based LF; renderer zero-based labels.
web_lines = {}
web_origins = {}
conflicts = []
for f in sorted((ROOT/'public-primary').glob('*.json')):
    d = json.loads(f.read_text())
    for c in d.get('content', []):
        for part in re.split(r'\n-{20,}\n', c.get('text', '')):
            m = re.search(r'\((https?://[^\s)]+)\)', part)
            if not m: continue
            url = m.group(1)
            for line in part.split('\n'):
                lm = re.match(r'L(\d+)(?:@[^:]+)?: (.*)', line)
                if not lm: continue
                i = int(lm.group(1)); key = (url, i)
                if key in web_lines and web_lines[key] != line:
                    conflicts.append({'url':url,'line':i,'prior':web_lines[key],'later':line})
                web_lines[key] = line
                web_origins[key] = str(f.relative_to(ROOT))

(ROOT/'primary-units').mkdir(exist_ok=True)
versions = {
 'https://arxiv.org/pdf/2206.07183v2': 'arXiv:2206.07183v2; submission 6 September 2023; PDF date 7 September 2023',
 'https://arxiv.org/html/2206.07183v2': 'arXiv:2206.07183v2; submission 6 September 2023; HTML rendering date differs from PDF',
 'https://arxiv.org/pdf/1801.08229v4': 'arXiv:1801.08229v4; 27 March 2022',
 'https://arxiv.org/html/2302.02541v3': 'arXiv:2302.02541v3; 17 July 2024; CMH 100 (2025), 269-322, DOI 10.4171/CMH/586',
 'https://arxiv.org/html/2603.25605v1': 'arXiv:2603.25605v1; 26 March 2026',
 'https://arxiv.org/html/2509.09442v1': 'arXiv:2509.09442v1; 11 September 2025',
}
def web_unit(uid, url, lo, hi, role):
    missing = [i for i in range(lo,hi+1) if (url,i) not in web_lines]
    assert not missing, (uid, missing)
    literal = '\n'.join(web_lines[url,i] for i in range(lo,hi+1))
    artifact = 'primary-units/'+uid+'.txt'
    (ROOT/artifact).write_text(literal)
    return {'unit':uid,'url':url,'version':versions[url],
      'coordinate_rule':'literal public renderer line labels; zero-based inclusive; page labels zero-based when present',
      'inclusive_renderer_lines':[lo,hi],'literal':literal,'sha256':sha(literal.encode()),
      'artifact':artifact,'role':role,
      'response_artifacts':sorted({web_origins[url,i] for i in range(lo,hi+1)})}
def given(uid):
    u=dict(sup_units[uid]); u['coordinate_rule']='supplied UTF-8 decoding and split(\\n); inclusive one-based LF'
    u['source_text_sha256_status']='supplied binding; full text bytes not independently present or rehashed'
    u['role']='supplied literal primary statement and pertinent proof unit'
    return u
records=[]
def add(statement, used_for, passages):
    i=len(records)
    records.append({'index':i,'statement':statement,'used_for':used_for,'passages':passages})

add('BJ 1801.08229v4 defines PSH(theta) by genuine generically finite section maxima on actual rational bundles in classes tending to theta, followed by decreasing nets. It gives sums, finite maxima and decreasing varying-class closure; bounded potentials require nefness. On irreducible projective varieties sup(phi)=phi(v_triv), and genuine potentials are determined and ordered on divisorial valuations. The ground field is algebraically closed and trivially valued.',
 'Original-carrier definitions, factorization, and diagnosis of the invalid constant floor in a nonnef class.',[given(u) for u in ['x00','x01','x02','x05','x06','x07']])
add('Boucksom-Jonsson 2206.07183v2 Theorem A: for smooth irreducible projective X over an algebraically closed trivially valued field, if char(k)=0 or dim(X)<=2, every numerical class has the envelope property. Corollaries 2.1-2.2: PSH(theta) is nonempty exactly for pseudoeffective theta, V_theta=P_theta(0) is genuine, and sup-normalized PSH(theta) is compact in the divisorial topology.',
 'The full big/pseudoeffective psh cone, reference and compactness gates already proved in the literature; no big energy or equation is inferred.',[
 web_unit('BJ-addendum-statement','https://arxiv.org/pdf/2206.07183v2',18,54,'complete retained standing hypotheses and Theorem A; Theorem B remains ample'),
 web_unit('BJ-addendum-proof-A','https://arxiv.org/pdf/2206.07183v2',324,378,'full proof of Theorem A'),
 web_unit('BJ-addendum-consequences','https://arxiv.org/pdf/2206.07183v2',379,405,'complete statements and proofs of Corollaries 2.1-2.3'),
 web_unit('BJ-addendum-base-ideals','https://arxiv.org/html/2206.07183v2',159,208,'same-bundle section envelope and base ideal lemmas with full pertinent proofs'),given('x08')])
add('BJ 1801.08229v4 Lemma 5.13: if a target class theta is approached by theta_m with theta_m-theta ample and every theta_m has EP, birational pullback is an onto homeomorphism of genuine PSH spaces. Theorem 5.11 equates EP and normalized compactness. Theorem 5.20 and Corollary 5.21 give the smooth characteristic-zero nef/ample endpoint.',
 'Only ample target Y is used for the endpoint and its local bounded products; no ampleness of its birational pullback is claimed.',[given('x08'),given('x10')])
add('BJ 1801.08229v4 Theorems 7.14 and 7.18 and Proposition 7.19 define a signed multilinear intersection product for functions in the ambient finite-energy vector space, of mass the numerical top intersection. Positivity is asserted when each numerical class is nef and its potential genuine psh. Bounded psh potentials are in that ambient vector space after addition of a dominating ample class. This is not a positive product for general nonnef classes.',
 'Bounded nef zero-volume example, bounded nef original-carrier local products, and scope warning about big volume versus top intersection.',[given('x11'),given('x12')])
add('BE 1805.01016v3 Theorem 7.14 regularizes genuine psh metrics on actual semiample rational bundles by smooth semipositive metrics. Propositions 8.3, 8.5 and Theorems 8.4, 8.18 give continuous mixed measures, raw intersection mass, intersection/Deligne compatibility and uniform-to-weak continuity. Their model intersection formulas use the actual analytic fundamental cycle.',
 'Continuous same-bundle products on the semiample H of the explicit endpoint; no assertion for arbitrary big unbounded metrics.',[given('x22'),given('x23'),given('x24')])
add('BJ 1801.08229v4 Corollary 4.24: PSH(0) consists of locally constant functions. For irreducible X the functions are constants; its proof uses the Alexander-Taylor bound under arbitrarily small ample classes and divisorial determination.',
 'Only the actual trivial-bundle zero-volume endpoint is claimed.',[given('x07')])
add('Darvas-Xia-Zhang 2302.02541v3 Theorem 3.14 identifies their analytic test-curve PSH space with genuine BJ PSH for pseudoeffective rational bundles on complex projective manifolds. Section 3.4 defines a finite-energy space for big complex classes by test-curve mass integrals; Theorem 3.17 identifies it with I-maximal finite-energy rays. These are not statements of a general original-carrier non-Archimedean MA operator and arbitrary-target inverse equation over every retained field.',
 'Literature scope audit only; its analytic energy is acknowledged, but is not used as a foundation for our endpoint.',[
 web_unit('DXZ-cone-identification','https://arxiv.org/html/2302.02541v3',714,743,'whole map construction and Theorem 3.14 proof'),
 web_unit('DXZ-energy','https://arxiv.org/html/2302.02541v3',774,794,'complete Section 3.4 definitions and Theorem 3.17 deduction')])
add('Dervan-Reboulet 2603.25605v1 works on smooth complex projective varieties with big bundles. Definition 3.4 and Theorem 3.6 solve prescribed finite divisorial probability data on compatible smooth dominant test configurations by a big real total bundle and positive restricted intersection coefficients. Proposition 3.8 and the simplex argument are the stated proof. This is a finite model endpoint, not an arbitrary-support genuine finite-energy original-carrier theorem; source comments about nonuniqueness concern test configurations.',
 'Literature scope audit only; not used to define or prove the local metric operator.',[
 web_unit('DR-field-and-volume','https://arxiv.org/html/2603.25605v1',111,123,'standing complex field, geometric and positivity hypotheses'),
 web_unit('DR-finite-target','https://arxiv.org/html/2603.25605v1',371,402,'full finite-target definitions and Theorem 3.6 statement'),
 web_unit('DR-finite-proof','https://arxiv.org/html/2603.25605v1',411,449,'Proposition 3.8 and complete displayed proof of Theorem 3.6'),
 web_unit('DR-scope-comments','https://arxiv.org/html/2603.25605v1',85,109,'source explicitly distinguishes test configurations from FS metrics')])
add('Mesquita-Piccione-Witt Nystrom 2509.09442v1 formulates its transcendental non-Archimedean Calabi-Yau theorem for a compact Kahler manifold with a Kahler positivity class. Its big model terminology concerns the total degeneration class and does not state the theorem for an arbitrary nonample big generic line bundle.',
 'Literature scope observation only; no theorem from this source is used to deduce our endpoint.',[
 web_unit('MPN-positivity-and-equation','https://arxiv.org/html/2509.09442v1',163,241,'retained positivity definitions and Theorem B statement; no full proof is claimed inspected')])
add('BJ 1801.08229v4 Corollary 4.10 gives genuine convex composition with slopes in [0,1]; Lemma 4.36 makes proper algebraic subsets pluripolar. In the ample domain Lemma 7.47 gives Cap(phi<=-t)<=n/t for sup-zero phi and J(phi)<=1+integral_1^infty t^n Cap(phi<=-t)dt. Corollary 7.49 gives zero pluripolar mass for ample finite-energy mixed products. Our actual point-nullness deduction uses the conservative exponent alpha=1/(n+2), for which the displayed capacity bound is directly integrable; no larger exponent range is needed.',
 'Explicit zero mass at p for every ample finite-energy product and every intrinsic finite-energy target, needed in the actual original-carrier endpoint. Complete source units retained; the conservative deduction is proved in the paper.',[
 web_unit('BJ-convex-composition','https://arxiv.org/pdf/1801.08229v4',3453,3460,'full convex-composition statement and proof'),
 web_unit('BJ-algebraic-pluripolar','https://arxiv.org/pdf/1801.08229v4',3767,3783,'definitions and complete proper-algebraic-subset proof'),
 web_unit('BJ-capacity-null-mass','https://arxiv.org/pdf/1801.08229v4',7016,7112,'complete capacity, finite-energy pole and null pluripolar mass statement/proof units')])

write_json('external-premises.json',{'coordinate_conventions':[
 'indices of premises are consecutive nonnegative zero-based integers',
 'supplied source slices retain their literal inclusive one-based LF coordinates',
 'new HTTP renderer slices retain literal zero-based renderer line and page labels; these are not original-PDF LF coordinates'],
 'premises':records,
 'task_grants':[{'id':'P16.1-ample-only','artifact':'granted/block-00.txt',
 'sha256':sha((ROOT/'granted/block-00.txt').read_bytes()),
 'scope':'Exact supplied theorem on actual ample rational bundles, reduced irreducible geometrically unibranch projective varieties, arbitrary algebraically closed trivially valued characteristic-zero fields. Used on smooth ample Y only.',
 'usage':'Compactness, genuine E1, local mixed raw products, comparison, finite intrinsic dual-energy target condition, attainment, equation and uniqueness. No nonample extension is granted.'}],
 'retrieval_limitations':[
 'Public sources were read through the available HTTP primary-source renderer. No full original PDF binary was returned by that tool.',
 'A local urllib PDF request failed with Operation not permitted. Original-PDF binary checksums are not invented.',
 'Checksums here bind exact retained literal excerpts and response JSON; full-source hashes in supplied data remain supplied metadata, not newly computed evidence.',
 'The addendum PDF identifies v2 as 6 September 2023, paper date 7 September 2023. The HTML rendering shows a different date; the PDF version controls.',
 'Only listed pertinent statement/proof units were inspected; no recursively complete reading of their background citations is claimed.',
 'No supervised compute facility was exposed and no resource-heavy computation was performed.'],
 'renderer_conflicts':conflicts})
checks = {'input_original_identical':(ROOT/'input.json').read_bytes()==(ROOT/'input-original.json').read_bytes(),
 'task_semantically_exact':json.loads((ROOT/'task-original.json').read_text())==json.loads((ROOT/'input.json').read_text())['task'],
 'assignment_exact':(ROOT/'assignment-original.txt').read_text()==json.loads((ROOT/'input.json').read_text())['assignment'],
 'supplied_literal_units_checked':len(sup_units),'external_statement_count':len(records),
 'supplied_blocks_identical_to_input':len(blocks),'additional_hash_keyed_literal_units_checked':len(additional_units),
 'all_indices_consecutive':all(p['index']==i for i,p in enumerate(records)),
 'all_external_statements_bound_to_http':all(p['passages'] and all(u['url'].startswith(('http://','https://')) for u in p['passages']) for p in records),
 'renderer_conflict_count':len(conflicts)}
assert all(checks[k] for k in ['input_original_identical','task_semantically_exact','assignment_exact','all_indices_consecutive','all_external_statements_bound_to_http'])
write_json('evidence-checks.json',checks)
print(json.dumps(checks,sort_keys=True))
