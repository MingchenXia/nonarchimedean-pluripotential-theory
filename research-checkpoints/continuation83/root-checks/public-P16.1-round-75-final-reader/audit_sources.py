#!/usr/bin/env python3
"""Read only the frozen input, explicitly authorized caches, and this workspace."""
import hashlib, json, pathlib, shutil

ROOT = pathlib.Path(__file__).resolve().parent
def sha(b): return hashlib.sha256(b).hexdigest()
def write(name, obj):
    (ROOT/name).write_text(json.dumps(obj, ensure_ascii=False, indent=2)+'\n')

def main():
    original = (ROOT/'input.json').read_bytes()
    assert (ROOT/'input-original.json').read_bytes() == original
    data = json.loads(original)
    assert json.loads((ROOT/'task-original.json').read_text()) == data['task']
    assert (ROOT/'assignment-original.txt').read_text() == data['assignment']
    descriptors = json.loads((ROOT/'authorized-sources.json').read_text())
    ranges = {
      '1801.08229v4': [
        ('conventions',435,469),('Gauss',724,757),('relative-closure',759,849),
        ('genuine-definition',2173,2250),('majorants',2418,2468),
        ('divisorial-minimum',2494,2535),('birational-error',2550,2616),
        ('onto-antecedent',2859,2881),('continuous-obstacle-EP',2905,2975),
        ('general-variety-operator',3649,3705),('MA-proof',3980,4057),
        ('weighted-proof',4074,4148),('continuous-locality',4510,4551),('target-integrability',5245,5301),
        ('uniqueness-domination',5440,5477),('actual-attainment',6092,6146),
        ('already-genuine-sequences',6195,6265),('EP-orthogonality',6300,6359)],
      '2609.27610v1': [
        ('new-envelope-statement',48,85),('genuine-approximants',399,458),
        ('weak-descent',563,638),('printed-contact',643,707),
        ('printed-growth',762,774),('controlled-approximation',950,1038),
        ('flat-trace',2128,2205),('whole-trace-and-radial',2207,2372),
        ('split-proof',2373,2533),('two-inductions',2534,2692),
        ('envelope-proof',2697,2755)],
      '1204.6277v2': [('continuous-products-proof',10401,10485)],
      '1608.08030v3': [
        ('algebraization-extension',249,287),('actual-PL-and-model-proof',288,385),
        ('field-detection',633,710),('whole-global-nef-proof',729,782)],
      '1801.04713v3': [('continuous-curve-theorem',1090,1128)],
      'tel-00010990v1': [('unit-log-proof',3580,3624),
        ('harmonic-maximum',3730,3741),('subharmonic-definition-and-limits',3783,3820),
        ('maximum-and-locality-proof',3860,3906)],
      '1805.01016v3': [('FS-difference-proof',1989,2043),
        ('genuine-PSH-and-nef-proof',2281,2353),('smooth-FS-regularization',2354,2379),
        ('actual-continuous-operator-proof',2611,2779),('model-Deligne-proof',3125,3202)],
      '2503.05513v1': [('unknown-current-converse',147,164),
        ('local-lifting-proof',489,800),('represented-curve-criterion-proof',803,923)],
      'Published Confluentes Mathematici 4(4) 1250007, DOI10.1142/S1793744212500077':
        [('compact-unit-tropicalization-proof',2077,2155)],
      '2111.05741v3': [('source-introduction',1,100),('represented-positive-current-proof',2540,2589)]
    }
    (ROOT/'sources').mkdir(exist_ok=True)
    (ROOT/'source-extracts').mkdir(exist_ok=True)
    manifest=[]; units=[]; checks=[]
    for i, s in enumerate(descriptors,1):
        rec={'id':f'S{i}','version':s['saved_version'],'public_source':s['public_source'],'files':[]}
        for field,hfield in [('pdf','pdf_sha256'),('literal_extract','extract_sha256'),
                             ('abstract_html','abstract_sha256'),('html','html_sha256')]:
            if field not in s: continue
            p=pathlib.Path(s[field]); b=p.read_bytes(); actual=sha(b)
            assert actual==s[hfield], (p,actual,s[hfield])
            dest=ROOT/'sources'/p.name; shutil.copyfile(p,dest)
            rec['files'].append({'role':field,'authorized_path':str(p),'local_file':str(dest.relative_to(ROOT)),
                                 'sha256':actual,'bytes':len(b)})
            checks.append({'source':f'S{i}','role':field,'hash_match':True})
        text=pathlib.Path(s['literal_extract']).read_bytes().decode('utf-8'); lines=text.split('\n')
        rec.update({'LF_convention':"UTF-8 bytes decode then split('\\n'); inclusive one-based coordinates",
                    'split_entries':len(lines),'whole_body_independently_audited':False})
        for label,a,b in ranges[s['saved_version']]:
            assert 1<=a<=b<=len(lines)
            literal='\n'.join(lines[a-1:b])
            target=pathlib.Path('source-extracts')/f'S{i}-{label}-LF{a}-{b}.txt'
            (ROOT/target).write_bytes(literal.encode('utf-8'))
            units.append({'id':f'S{i}-{label}','version':s['saved_version'],
                          'source_sha256':s['extract_sha256'],'inclusive_one_based_LF':[a,b],
                          'literal_file':str(target),'literal_sha256':sha(literal.encode('utf-8')),
                          'scope':'Literal statement and pertinent proof text. New applications require the paper arguments; no whole-source correctness certification.'})
        manifest.append(rec)
    (ROOT/'embedded-data').mkdir(exist_ok=True)
    ass=data['assignment']
    bindings=[('round72-argument.md','# Round72 complete argument, including genuine operator and CONDITIONAL A-C Runge reconstruction; UNREVIEWED',
              '# Actual round72 four canonical notes and exact unresolved premises; candidate=false'),
              ('round70-argument.md','# Round70 attempted smooth weak upper-growth and trace route; UNREVIEWED, with unresolved metric premises retained',
               '# Root80 conditional fiber constancy and finite-data envelope descent; UNREVIEWED'),
              ('root80.md','# Root80 conditional fiber constancy and finite-data envelope descent; UNREVIEWED',
               '# Root81 geometric fiber, finite normalization, explicit blowup and conditional onto reconstruction; UNREVIEWED')]
    for name,a,b in bindings:
        (ROOT/'embedded-data'/name).write_text(ass[ass.index(a):ass.index(b)])
    root81='# Root81 geometric fiber, finite normalization, explicit blowup and conditional onto reconstruction; UNREVIEWED'
    (ROOT/'embedded-data'/'root81.md').write_text(ass[ass.index(root81):])
    marker='# Actual round72 four canonical notes and exact unresolved premises; candidate=false'
    tail=ass[ass.index(marker)+len(marker):].lstrip()
    oldnotes,end=json.JSONDecoder().raw_decode(tail)
    write('embedded-data/round72-notes.json',oldnotes)
    write('source-extracts/source-provenance.json',{'sources':manifest,'units':units,
          'pinned_primary_file_checks':checks,'live_access_claimed':False,
          'Stacks_pages_independently_accessed':False})
    write('preservation-report.json',{'input_sha256':sha(original),'input_bytes':len(original),
          'input_original_byte_identical':True,'task_value_identical':True,'assignment_string_identical':True,
          'primary_hash_count':len(checks),'literal_unit_count':len(units)})
    print(json.dumps({'input_sha256':sha(original),'primary_hashes':len(checks),'literal_units':len(units)}))
if __name__=='__main__': main()
