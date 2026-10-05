import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent

def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()

def main():
    original = ROOT / 'input.json'
    data = json.loads(original.read_bytes())
    assignment = data['assignment']
    marker = 'Actual read-only primary sources:'
    tail = assignment.split(marker, 1)[1].lstrip()
    sources, _ = json.JSONDecoder().raw_decode(tail)
    assert len(sources) == 17
    for i, source in enumerate(sources):
        source['audit_id'] = chr(65+i)
    (ROOT/'sources.json').write_text(json.dumps(sources, ensure_ascii=False, indent=2)+'\n')
    dst = ROOT/'source-extracts'
    dst.mkdir(exist_ok=True)
    files = []
    for source in sources:
        for key, hashkey in [('pdf','pdf_sha256'), ('literal_extract','extract_sha256'),
                             ('abstract_html','abstract_sha256'), ('html','html_sha256'),
                             ('fresh_official_versioned_pdf','fresh_official_pdf_sha256')]:
            if key not in source:
                continue
            path = Path(source[key])
            actual = sha(path)
            assert actual == source[hashkey], (source['audit_id'], key, actual)
            files.append({'id':source['audit_id'], 'kind':key, 'path':str(path),
                          'sha256':actual,'bytes':path.stat().st_size,'matches':True})
        raw = Path(source['literal_extract']).read_bytes()
        (dst/(source['audit_id']+'-full.txt')).write_bytes(raw)
    # UTF-8 byte decode followed by split('\n'), with inclusive one-based coordinates.
    selections = {
        'A':[(120,152),(218,286),(344,346),(522,577),(762,784),(937,964),(1237,1268)],
        'C':[(2815,2900),(2980,3064),(3916,3945),(5190,5270),(6084,6148)],
        'D':[(64,184),(282,319),(1010,1041),(2053,2235)],
        'E':[(638,710),(759,777),(950,1012),(1560,1577),(1734,1813),
             (1926,1957),(1968,2039),(2048,2102),(2383,2539),(2635,2691),(2697,2749)]
    }
    applications = {
        'A':'Actual cone definitions and probability energy. Printed tangent sign is replaced by the concave-tangent derivation. No inverse-existence conclusion is imported.',
        'C':'Projective proofs of uniform target integration and EP/onto equivalence are methodological cross-checks. They are not applied to irrational cone classes by analogy.',
        'D':'Only Appendix A finite homogeneous-polynomial inequalities are applied, after constructing the fixed-ray linear polynomial and its Hodge cone. Theorem A concerns measures and supplies no actual potential.',
        'E':'AFS presentation and singular-route diagnostic. Corrected explicit barriers are proved independently. Printed lower-growth Proposition 4.19 and the complete weak Runge/EP chain are not assumed.'
    }
    excerpts = []
    for source in sources:
        sid = source['audit_id']
        lines = Path(source['literal_extract']).read_bytes().decode('utf-8').split('\n')
        for lo, hi in selections.get(sid, []):
            assert 1 <= lo <= hi <= len(lines)
            text = '\n'.join(lines[lo-1:hi])
            name = f'{sid}-LF{lo}-{hi}.txt'
            (dst/name).write_text(text, encoding='utf-8')
            excerpts.append({'id':sid,'version':source['saved_version'], 'file':name,
                             'lf_start':lo,'lf_end':hi,'literal':text,
                             'application_and_limit':applications[sid]})
    # Only embedded documentary data are read: no referenced campaign path is opened.
    headings = [
        ('accepted-P13.1.md','## Accepted P13.1 exact reviewed full comparison and uniform outer differentiation proof'),
        ('accepted-P13.1-notes.json.txt','## Accepted P13.1 actual canonical mathematical notes; operational assertions are documentary'),
        ('accepted-P13.1-review.json.txt','## Exact independent ORIGINAL P13.1 review, actual verdict PASS'),
        ('round71-draft.md','## Actual round71 full finite-target, approximate-solution, I-Cauchy and raw-root envelope draft; UNREVIEWED'),
        ('round71-notes.json.txt','## Actual round71 canonical four notes; candidate=false'),
        ('round70-draft.md','## Actual round70 rational local bridge, smooth weak theorem and finite trace draft; UNREVIEWED'),
        ('round70-notes.json.txt','## Actual round70 canonical four notes; candidate=false'),
        ('root79-proposal.md','## Root79 explicit strict potential, actual poles and full Runge reconstruction proposal; UNREVIEWED')
    ]
    embedded = ROOT/'embedded-data'
    embedded.mkdir(exist_ok=True)
    for i,(name,heading) in enumerate(headings):
        start = assignment.index(heading)
        end = assignment.index(headings[i+1][1],start+len(heading)) if i+1<len(headings) else len(assignment)
        (embedded/name).write_text(assignment[start:end],encoding='utf-8')
    # Preserve literal task-object bytes, rather than only an equivalent reserialization.
    raw = original.read_bytes()
    decoded = raw.decode('utf-8')
    i = decoded.index('"task"') + len('"task"')
    i = decoded.index(':', i)+1
    while decoded[i].isspace(): i+=1
    task, length = json.JSONDecoder().raw_decode(decoded[i:])
    assert task == data['task']
    (ROOT/'task-original.json').write_bytes(decoded[i:i+length].encode('utf-8'))
    assert raw == (ROOT/'input-original.json').read_bytes()
    preservation = {name:{'sha256':sha(ROOT/name),'bytes':(ROOT/name).stat().st_size}
                    for name in ['input.json','input-original.json','assignment-original.txt','task-original.json']}
    (ROOT/'preservation.json').write_text(json.dumps(preservation,indent=2)+'\n')
    report = {'coordinate_convention':"UTF-8 bytes decode; split('\\n'); inclusive one-based LF indices",
              'sources':sources,'verified_files':files,'excerpts':excerpts,
              'scope':'All supplied file hashes checked; selected pertinent proof bodies read. Copies of complete extracts do not imply a whole-source proof review.'}
    (dst/'source-provenance.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'sources':len(sources),'verified_files':len(files),'literal_excerpts':len(excerpts),
                      'input_sha256':sha(original),'input_unchanged':True},indent=2))

if __name__ == '__main__': main()
