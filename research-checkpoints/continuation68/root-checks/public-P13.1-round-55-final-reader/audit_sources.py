"""Read only the eight supplied caches; write literal LF-indexed excerpts locally."""
from pathlib import Path
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parent
inp = (ROOT / 'input.json').read_bytes()
data = json.loads(inp)
assert (ROOT / 'input-original.json').read_bytes() == inp
raw = inp.decode('utf-8')
m = re.search(r'"task"\s*:\s*', raw)
task, end = json.JSONDecoder().raw_decode(raw, m.end())
assert task == data['task']
(ROOT / 'task-original.json').write_bytes(raw[m.end():end].encode('utf-8'))
assert (ROOT / 'assignment-original.txt').read_text() == data['assignment']
manifest = json.loads(data['assignment'].split('Read-only published source caches:\n', 1)[1])

spec = [
 ('A', [(169,217),(218,246),(277,331),(344,398),(522,615),
        (762,805),(930,959),(977,1061),(1130,1144)],
  'Orbit action and H/CPSH/PSH definitions used. The probability/translation rule is used; '
  'Theorem 5.15 of B is not used. No cross-Reeb finite-energy conclusion is inferred.'),
 ('B', [(181,217),(379,469),(470,527),(589,671),(674,757),
        (889,948),(1198,1239),(1239,1274),(1275,1372)],
  'Corollary 3.13 is applied only to explicitly nonnegative, multiplicative, linearly bounded '
  'shifted filtrations. Lemma 3.16 and the complete Proposition 5.13/Corollary 5.14/'
  'Theorem 5.15 bodies are audited; the E=S conclusion is not used.'),
 ('C', [(4690,4823),(4841,4966)],
  'Projective E-downarrow and differentiation are inspected as a target. '
  'No affine-cone application is claimed. Both signs and the continuous-approximation '
  'argument must be handled in any future application.'),
 ('D', [(246,319),(1029,1096),(1348,1387),(1650,1680)],
  'Synthetic results require a common linear form/positivity setup and orthogonality. '
  'The nonlinear orbit map does not verify these axioms; no application is claimed.'),
 ('E', [(388,440),(476,520),(567,614),(692,729),(743,790),(792,860),
        (950,995),(1331,1339),(1488,1576),(1885,1959),(2635,2747)],
  'The upper-growth convention u<=g+O(1) is recorded. Proposition 4.19 uses '
  'Lemma 3.25(1), whose hypothesis already includes regularizability. No '
  'noncircular replacement or singular envelope application is claimed. '
  'Countability removal and global reference conventions are retained in excerpts.'),
 ('F', [(525,533),(1222,1276)],
  'Theorem 4.13 has the smooth projective standing hypothesis. '
  'It is not applied to arbitrary normal Reeb quotients.'),
 ('G', [(585,610),(6179,6211),(7095,7121),(9797,9863),
        (10401,10489),(10595,10689),
        (22100,22131),(26410,26457)],
  'The cited 8.7.2 is a Proposition. It requires local uniform convergence of '
  'continuous potentials and positive closed currents; it does not give '
  'unbounded decreasing-net tail control. Definition 8.1.7 and Proposition '
  '8.1.9 verify CPSH membership; 6.2.4 and 6.2.6 supply cutoff and density. '
  '15.7.1 permits separated '
  'pure-dimensional singular analytic spaces with the stated boundary structure. '
  '18.3.3(b) retains the calibrated finite-degree factor.'),
 ('H', [(365,425),(945,997),(1022,1059),(1249,1316),(1317,1369),
        (1854,1875),(2141,2175),(2260,2313),(2317,2349),(2372,2435)],
  'The assignment calls 5.9 a Theorem; this cache labels it Proposition 5.9. '
  '2.15, 3.12(iii), 5.9 and Section 7 yield the signed degree-wise '
  'mean/intersection energy for actual projective test configurations. '
  'They do not by themselves verify an arbitrary cone CLD radial/Veronese bridge.'),
]

dest = ROOT / 'source-extracts'
dest.mkdir(exist_ok=True)
out = {'line_convention': "one-based inclusive LF ranges, bytes decoded as UTF-8 then split('\\n'); no universal-newline conversion",
       'sources': [], 'preservation': {}}
def sha(b): return hashlib.sha256(b).hexdigest()
for source, (sid, ranges, check) in zip(manifest, spec, strict=True):
    record = dict(source)
    record['id'] = sid
    record['hash_checks'] = {}
    for field in ('pdf', 'literal_extract', 'abstract_html'):
        if field in source:
            b = Path(source[field]).read_bytes()
            key = {'pdf':'pdf_sha256', 'literal_extract':'extract_sha256',
                   'abstract_html':'abstract_sha256'}[field]
            actual = sha(b)
            assert actual == source[key], (sid, field, actual, source[key])
            record['hash_checks'][field] = {'actual_sha256':actual, 'bytes':len(b), 'matches_supplied':True}
    b = Path(source['literal_extract']).read_bytes()
    lines = b.decode('utf-8').split('\n')
    record['split_LF_line_count'] = len(lines)
    record['application_check'] = check
    record['excerpts'] = []
    for a, z in ranges:
        assert 1 <= a <= z <= len(lines)
        literal = '\n'.join(lines[a-1:z])
        fname = f'{sid}-{source["saved_version"]}-L{a}-L{z}.txt'
        (dest / fname).write_bytes(literal.encode('utf-8'))
        record['excerpts'].append({'first_line':a, 'last_line':z,
                                  'file':f'source-extracts/{fname}',
                                  'sha256':sha(literal.encode('utf-8')),
                                  'literal':literal})
    out['sources'].append(record)
for fname in ('input.json','input-original.json','assignment-original.txt','task-original.json'):
    out['preservation'][fname] = sha((ROOT / fname).read_bytes())
out['concrete_limits'] = [
    'No general equality between a signed cutoff mean and the genuine affine-cone CLD energy is proved.',
    'No moving-MA uniform tail estimate, E1 preservation, or strong-topology continuity is proved.',
    'No singular projective envelope theorem is used in the proved comparison.',
    'No affine-cone extended-energy uniform differentiation theorem is proved.',
    'Literal extraction artifacts are retained; source corrections in the argument are explicit, not silently substituted.',
]
(dest / 'source-provenance.json').write_text(json.dumps(out, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
print(json.dumps({'verified_sources':len(out['sources']),
                  'literal_excerpts':sum(len(s['excerpts']) for s in out['sources']),
                  'input_original_byte_identical':True,
                  'provenance':'source-extracts/source-provenance.json'},indent=2))
