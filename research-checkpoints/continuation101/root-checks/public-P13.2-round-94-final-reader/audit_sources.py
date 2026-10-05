#!/usr/bin/env python3
"""Pin supplied primary bytes and literal LF units; no mathematical validation."""
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
def digest(data):
    return hashlib.sha256(data).hexdigest()

def main():
    original = (ROOT / 'input-original.json').read_bytes()
    assert original == (ROOT / 'input.json').read_bytes()
    obj = json.loads(original)
    assert (ROOT / 'assignment-original.txt').read_bytes() == obj['assignment'].encode('utf8')
    assert json.loads((ROOT / 'task-original.json').read_bytes()) == obj['task']
    preserved = json.loads((ROOT / 'preservation.json').read_text())
    for filename, record in preserved.items():
        data=(ROOT/filename).read_bytes()
        assert len(data)==record['bytes'] and digest(data)==record['sha256'], filename
    assert preserved['task-original.json']['sha256']=='4420d5c79db2fc178119e3f4331df3c2745d4f5be9fb27395659762c55407648'
    catalogue = json.loads((ROOT / 'source-catalogue.json').read_text())
    sources = []
    for rec in catalogue['files']:
        if rec['id'] not in {'A','C','E','I','J'} or rec['kind'] not in {'pdf','literal_extract'}:
            continue
        data = (ROOT / rec['copy']).read_bytes()
        assert len(data) == rec['bytes'] and digest(data) == rec['sha256'], rec['copy']
        sources.append(rec)
    texts = {r['id']: r for r in sources if r['kind'] == 'literal_extract'}
    # Every endpoint is inclusive and one-based after UTF-8 byte decode / split('\n').
    ranges = {
        'A': [(277,346),(762,805)],
        'C': [(1400,1464),(1680,1738),(2170,2328),(2408,2494),
              (2513,2550),(2797,2858),(2894,2978),(2980,3064),
              (3650,3735),(3780,3844),(3971,4148),(4149,4183),(4740,4787),
              (4880,4970),(5090,5302),(5439,5478),(6305,6359)],
        'E': [(2695,2790)],
        'I': [(325,440),(446,512),(550,633),(637,790)],
        'J': [(2357,2379),(2628,2749),(3120,3163)],
    }
    excerpt_dir = ROOT / 'source-extracts'
    excerpt_dir.mkdir(exist_ok=True)
    units = []
    for sid, spans in ranges.items():
        rec = texts[sid]
        lines = (ROOT / rec['copy']).read_bytes().decode('utf8').split('\n')
        for lo, hi in spans:
            assert 1 <= lo <= hi <= len(lines)
            literal = '\n'.join(lines[lo-1:hi])
            name = f'{sid}-LF{lo}-{hi}.txt'
            data = literal.encode('utf8')
            (excerpt_dir / name).write_bytes(data)
            units.append({'id': f'{sid}:{lo}-{hi}', 'source':sid,
                'version':rec['version'], 'source_sha256':rec['sha256'],
                'coordinate_rule': "UTF-8 bytes decode, split('\\n'); inclusive one-based LF",
                'inclusive_one_based_LF':[lo,hi], 'file':f'source-extracts/{name}',
                'sha256':digest(data), 'literal':literal})
    observation = json.loads((ROOT / 'stacks-primary-observation.json').read_bytes())
    raw = '\n'.join(c['text'] for c in observation['content'] if c['type']=='text')
    stacks_data = raw.encode('utf8')
    stacks_file = ROOT / 'sources/Stacks-0BQ3-0BPZ-rendered.txt'
    stacks_file.write_bytes(stacks_data)
    lines = stacks_data.decode('utf8').split('\n')
    for tag, needle, count in [('0BQ3','L24: ',2),('0BPZ','L24: ',1)]:
        start = next(i for i,line in enumerate(lines) if tag in line and 'https://' in line)
        at = next(i for i in range(start,len(lines)) if lines[i].startswith(needle))
        literal = '\n'.join(lines[at:at+count])
        name = f'Stacks-{tag}-LF{at+1}-{at+count}.txt'
        data = literal.encode('utf8')
        (excerpt_dir/name).write_bytes(data)
        units.append({'id':tag,'source':tag,'version':'live primary observation retained locally',
          'primary_url':f'https://stacks.math.columbia.edu/tag/{tag}',
          'source_sha256':digest(stacks_data),
          'coordinate_rule': "UTF-8 bytes decode, split('\\n'); inclusive one-based LF in retained rendered text",
          'inclusive_one_based_LF':[at+1,at+count],
          'original_zero_based_rendered_lines':[24,23+count],
          'file':f'source-extracts/{name}','sha256':digest(data),'literal':literal})
    provenance = {'sources':sources,'literal_units':units,
      'scope':'Literal statements and pertinent proof bodies only; no whole-paper or recursive-proof reading claim.',
      'mathematical_validation':False}
    (ROOT/'source-provenance.json').write_text(json.dumps(provenance,ensure_ascii=False,indent=2)+'\n')
    premises = [
      ('Same actual ample rational bundle regularization: Hdom(L) is contained in H(L); ample PSH has decreasing Hdom majorants, and CPSH is its uniform closure.',
       'C', ['C:1680-1738','C:2408-2494'], 'Hdom (L) := Hdom (c1 (L)) ⊂ H(L)'),
      ('On a reduced projective variety, supremum against each fixed continuous obstacle is continuous in the divisorial topology on PSH.',
       'C',['C:2513-2550'],'Proposition 4.28.'),
      ('On an irreducible projective variety, the envelope property implies compactness of normalized actual PSH, for arbitrary nets and ground-field cardinality.',
       'C',['C:2797-2858'],'Theorem 5.11.'),
      ('For ample classes on a reduced projective variety, actual energy is increasing, upper semicontinuous and continuous along decreasing nets; finite energy is defined on actual PSH.',
       'C',['C:3650-3735','C:3780-3844'],'Proposition 7.7.'),
      ('General-projective genuine mixed E1 measures have intersection mass and decreasing-net continuity; E1 tests are integrable, and simultaneous decreasing integrable tests have weakly convergent weighted measures.',
       'C',['C:3971-4148'],'Proposition 7.21.'),
      ('On a projective variety with an ample class, a divisorially converging actual PSH net with eventually bounded J converges in L1 of every finite-dual-energy probability. This assertion assumes neither EP nor smoothness nor inverse existence.',
       'C',['C:5090-5302'],'Proposition 9.19.'),
      ('On a reduced irreducible projective variety with ample class, finite dual energy of a Radon probability is equivalent to integrability of every actual E1 potential.',
       'C',['C:5090-5302'],'Theorem 9.20.'),
      ('A normal scheme is geometrically unibranch: each local ring is a normal domain, and the local definition applies at every point.',
       '0BQ3',['0BQ3','0BPZ'],'A normal scheme is geometrically unibranch.'),
      ('A local ring is geometrically unibranch when its reduction is a domain, its integral closure in that fraction field is local, and the residue extension is purely inseparable.',
       '0BPZ',['0BPZ'],'the residue field'),
      ('BGM Lemma 3.2 and its differentiability proof have geometrically reduced projective scope over arbitrary complete non-Archimedean fields. The estimate has no envelope-continuity assumption; Section 3.2 adds that assumption separately.',
       'I',['I:325-440','I:446-512','I:550-633','I:637-790'],'Lemma 3.2.'),
      ('On a compact space, a decreasing outer net of decreasing limits of continuous functions from a family stable under constants is a single decreasing limit from that family. Its limit may take minus infinity; minimum closure is unnecessary.',
       'C',['C:2170-2328'],'Lemma 4.6.'),
      ('For an irreducible projective variety with ample class, EP is equivalent to continuity of the envelope of every continuous obstacle; these continuous envelopes are genuine potentials.',
       'C',['C:2894-2978'],'Lemma 5.17.'),
      ('On a smooth connected projective variety over an algebraically closed trivially valued characteristic-zero field, every nef class has EP and its normalized genuine PSH class is compact. This is used only on the smooth source in the recalled established envelope proof route.',
       'C',['C:2980-3064'],'Theorem 5.20.'),
      ('On an equidimensional projective variety with ample class, u in actual PSH and v in actual E1 satisfy u<=v everywhere if u<=v almost everywhere for MA(v). No EP or inverse existence is assumed.',
       'C',['C:5439-5478'],'Corollary 10.6'),
      ('Under target EP on an irreducible projective variety, a continuous obstacle f has continuous genuine envelope psi=P(f) and integral (f-psi) MA(psi)=0.',
       'C',['C:6305-6359'],'Theorem 13.1.'),
      ('On a projective scheme over a complete non-Archimedean field, possibly trivially valued, fixed-bundle psh metrics on a semiample rational bundle are decreasing smooth-semipositive limits on that same bundle, uniformly if continuous; regularized FS permits real weights.',
       'J',['J:2357-2379'],'Theorem 7.14.'),
      ('Smooth mixed Monge-Ampere measures including the analytic fundamental cycle commute with complete field-extension pushforward. They extend uniquely to continuous fixed-bundle psh-regularizable tuples, continuously for uniform metric convergence, with positive intersection mass.',
       'J',['J:2628-2749'],'Proposition 8.3.'),
      ('Model Deligne pairings equal their metric pairings on projective non-Archimedean schemes including the dimension-zero case; on continuous ample-class psh potentials the BE/CLD operator agrees with the BJ energy-pairing operator.',
       'J',['J:3120-3163','C:3971-4148'],'Theorem 8.18.'),
      ('Actual cone FS functions are primary finite homogeneous maxima; CPSH is their local uniform closure, and genuine PSH consists of nontrivial pointwise decreasing CPSH-net limits.',
       'A',['A:277-346','A:762-805'],'Definition 2.9.'),
    ]
    urls={'A':'https://arxiv.org/pdf/2406.13684v1',
          'C':'https://arxiv.org/pdf/1801.08229v4','I':'https://arxiv.org/pdf/2004.03847v1',
          'J':'https://arxiv.org/pdf/1805.01016v3',
          '0BQ3':'https://stacks.math.columbia.edu/tag/0BQ3',
          '0BPZ':'https://stacks.math.columbia.edu/tag/0BPZ'}
    passages=[]
    for i,(statement,sid,ids,quote) in enumerate(premises):
        for uid in ids:
            unit=next(u for u in units if u['id']==uid)
            # A pertinent complete body is retained, rather than a headline-only citation.
            passages.append({'id':len(passages),'premise':i,'statement':statement,
              'url':urls[unit['source']] if unit['source'] in urls else urls[sid],
              'literal_unit':uid,'quote':quote if quote in unit['literal'] else unit['literal'],
              'proof_body':unit['literal']})
    assert {p['premise'] for p in passages}==set(range(len(premises)))
    assert all(p['premise']>=0 and p['url'].startswith('https://') for p in passages)
    evidence={'premises':[p[0] for p in premises], 'passages':passages,
      'task_granted_background_not_external_premises':[
        'Established projective envelope theorem EP_U, with discharged countable antecedent and accepted arbitrary-cardinality reduction.',
        'Fixed-Reeb and cross-Reeb cone calculus, calibrated continuous rational correspondence, genuine outer differentiation, intrinsic integrability criterion and midpoint calculus, within supplied scopes.'],
      'documentary_only':True}
    (ROOT/'external-premises.json').write_text(json.dumps(evidence,ensure_ascii=False,indent=2)+'\n')
    result={'input_sha256':digest(original),'preserved_input':True,
       'primary_files_hash_verified':len(sources),'literal_units':len(units),
       'external_premises':len(premises),'passages':len(passages),
       'nonnegative_complete_HTTP_coverage':True,'mathematical_acceptance':False}
    (ROOT/'source-audit-output.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))

if __name__=='__main__':
    main()
