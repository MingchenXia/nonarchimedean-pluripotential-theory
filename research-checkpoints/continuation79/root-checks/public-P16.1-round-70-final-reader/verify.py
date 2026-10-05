#!/usr/bin/env python3
"""Verify preservation/provenance/build facts, not the mathematical claims."""
import hashlib
import json
from pathlib import Path

root=Path(__file__).resolve().parent
checks=[]
def check(label, condition, detail=None):
    checks.append({'check':label,'passed':bool(condition),'detail':detail})
def digest(data):
    return hashlib.sha256(data).hexdigest()

raw=(root/'input.json').read_bytes()
data=json.loads(raw)
check('byte-identical input preservation',(root/'input-original.json').read_bytes()==raw,digest(raw))
check('assignment value preservation',(root/'assignment-original.txt').read_text()==data['assignment'])
check('task value preservation',json.loads((root/'task-original.json').read_text())==data['task'])
status=json.loads((root/'status.json').read_text())
check('exact status schema',set(status)=={'id','status','exact_result','proof_file','concrete_gaps'})
check('partial status and real gaps',status['status']=='partial' and len(status['concrete_gaps'])==4)

provenance=json.loads((root/'source-extracts/source-provenance.json').read_text())
manifest=json.loads((root/'source-manifest.json').read_text())
check('ten exact source manifests',len(provenance['sources'])==10 and provenance['sources']==manifest)
sources={}
for f in provenance['verified_files']:
    local=(root/f['local_file']).read_bytes()
    primary=Path(f['authorized_path']).read_bytes()
    check('primary/local bytes: '+f['local_file'],local==primary)
    check('source hash: '+f['local_file'],digest(local)==f['sha256'])
    check('source byte count: '+f['local_file'],len(local)==f['bytes'])
    if f['kind']=='literal_extract':
        sources[f['source_index']]=local.decode('utf-8').split('\n')
for e in provenance['excerpts']:
    a,b=e['inclusive_one_based_LF']
    lines=sources[e['source_index']]
    literal='\n'.join(lines[a-1:b])
    check('valid inclusive LF range: '+e['id'],1<=a<=b<=len(lines))
    check('literal body: '+e['id'],literal==e['literal'])
    check('literal file: '+e['id'],(root/e['literal_file']).read_bytes()==literal.encode())
    check('literal hash: '+e['id'],digest(literal.encode())==e['literal_sha256'])
    check('version/application/limits: '+e['id'],e['version']==manifest[e['source_index']]['saved_version'] and bool(e['checked_application_and_concrete_limits']) and not e['whole_source_audit'])

result=json.loads((root/'notes.json').read_text())
check('candidate false and note count',result['candidate'] is False and 0<len(result['notes'])<=4)
earlier=set()
for i,note in enumerate(result['notes'],1):
    check('canonical note ID '+str(i),note['id']==f'n{i}')
    check('exact note fields '+note['id'],set(note)=={'id','summary','detailedSummary','text','support'})
    check('earlier-only support '+note['id'],set(note['support'])<=earlier)
    check('nonempty note bodies '+note['id'],all(isinstance(note[k],str) and note[k] for k in ['summary','detailedSummary','text']))
    earlier.add(note['id'])
check('input hash in final note',digest(raw) in result['notes'][-1]['text'])
check('source counts in final note',f"{len(provenance['verified_files'])} verified primary" in result['notes'][-1]['text'] and f"{len(provenance['excerpts'])} literal LF excerpts" in result['notes'][-1]['text'])

build=json.loads((root/'build-results.json').read_text())
check('three successful build stages',build['success'] and len(build['runs'])==3 and all(r['returncode']==0 for r in build['runs']))
check('two distinct TeX runs',[r['stage'] for r in build['runs'][1:]]==['tex-run-1','tex-run-2'])
for r in build['runs']:
    stage=r['stage']
    for suffix in ['stdout','stderr','command.json']:
        check(f'preserved {stage}.{suffix}',(root/'build-logs'/f'{stage}.{suffix}').exists())
    if stage!='pandoc':
        log=(root/'build-logs'/f'{stage}.log').read_text(errors='replace')
        check(f'separate {stage} TeX log','Output written on P16.1-paper.pdf' in log)
        check(f'no TeX error {stage}','! ' not in log)
tex=(root/'P16.1-paper.tex').read_bytes()
pdf=(root/'P16.1-paper.pdf').read_bytes()
check('standalone TeX',b'\\documentclass' in tex and b'\\begin{document}' in tex and b'\\end{document}' in tex)
check('TeX output hash',digest(tex)==build['standalone_tex_sha256'])
check('PDF output hash',digest(pdf)==build['pdf_sha256'])
check('nonempty PDF pages',build['pdf_pages']>0)
argument=(root/'P16.1-argument.md').read_text()
check('explicit partial proof disposition','The unchanged original P16.1 is not solved here.' in argument)
check('complete proof location',status['proof_file']=='P16.1-argument.md' and len(argument)>40000)
finite=json.loads((root/'algebra-checks.json').read_text())
check('exhaustive finite partition domain',finite['partition_grid_exhaustive_count']==369)
check('finite domain count consistency',len(finite['partition_examples'])==369)
check('execution/mathematics distinction','no analytic theorem' in finite['epistemic_status'])
audit=json.loads((root/'mathematical-audit.json').read_text())
check('audit retains original target',audit['original_target_unchanged'] and audit['candidate'] is False)
check('same concrete gaps',audit['concrete_gaps']==status['concrete_gaps'])

warnings={}
for stage in ['tex-run-1','tex-run-2']:
    log=(root/'build-logs'/f'{stage}.log').read_text(errors='replace')
    warnings[stage]={'overfull_boxes':log.count('Overfull \\hbox'),'underfull_boxes':log.count('Underfull \\hbox')}
report={'success':all(c['passed'] for c in checks),'check_count':len(checks),'checks':checks,
 'source_files':len(provenance['verified_files']),'LF_excerpts':len(provenance['excerpts']),
 'pdf_pages':build['pdf_pages'],'typesetting_warnings':warnings,
 'epistemic_status':'File preservation, literal extraction, finite illustration and compilation checks only. These do not verify infinite mathematical claims.'}
(root/'verification.json').write_text(json.dumps(report,indent=2)+'\n')
files=[]
for p in sorted(root.rglob('*')):
    if p.is_file() and p.name!='artifact-manifest.json' and '.git' not in p.parts:
        b=p.read_bytes();files.append({'file':str(p.relative_to(root)),'bytes':len(b),'sha256':digest(b)})
(root/'artifact-manifest.json').write_text(json.dumps({'artifacts':files,'limits':'Hashes identify files; they do not prove mathematics.'},indent=2)+'\n')
print(json.dumps({k:report[k] for k in ['success','check_count','source_files','LF_excerpts','pdf_pages','typesetting_warnings']}))
if not report['success']:
    print(json.dumps([c for c in checks if not c['passed']],indent=2))
    raise SystemExit(1)
