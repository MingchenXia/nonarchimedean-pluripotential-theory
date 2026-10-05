from pathlib import Path
import hashlib,json
ROOT=Path(__file__).resolve().parent;sha=lambda b:hashlib.sha256(b).hexdigest()
checks=[]
def check(name,test):
 assert test,name; checks.append(name)
b=(ROOT/'input.json').read_bytes();orig=(ROOT/'input-original.json').read_bytes();x=json.loads(b);s=b.decode('utf-8')
check('input byte identical',b==orig)
check('input SHA256 unchanged',sha(b)=='c900a151274149ec0a060d8b965bc770e06adb6320c244fb162be200814ca602')
check('assignment decoded string exact',(ROOT/'assignment-original.txt').read_text()==x['assignment'])
start=s.index(':',s.index('"task"'))+1
while s[start].isspace():start+=1
_,end=json.JSONDecoder().raw_decode(s,start)
check('task literal UTF8 span exact',(ROOT/'task-original.json').read_bytes()==s[start:end].encode('utf-8'))
pres={'input_bytes':len(b),'input_sha256':sha(b),'input_original_sha256':sha(orig),'byte_identical':True,'task_literal_bytes':len(s[start:end].encode('utf-8')),'task_sha256':sha((ROOT/'task-original.json').read_bytes()),'assignment_utf8_bytes':len(x['assignment'].encode()),'assignment_sha256':sha(x['assignment'].encode())}
(ROOT/'preservation.json').write_text(json.dumps(pres,indent=2)+'\n')
status=json.loads((ROOT/'status.json').read_text());check('exact status keys',set(status)=={'id','status','exact_result','proof_file','concrete_gaps'})
check('partial status',status['status']=='partial' and len(status['concrete_gaps'])>0)
notes=json.loads((ROOT/'canonical-notes.json').read_text());check('four local notes candidate false',len(notes['notes'])==4 and notes['candidate'] is False)
seen=set();external={'supplied:P13.1/n1','supplied:P13.1/n3','supplied:round73/n1','supplied:round73/n2'}
for note in notes['notes']:
 check('note schema '+note['id'],set(note)=={'id','summary','detailedSummary','text','support'})
 check('backward support '+note['id'],all(z in seen|external for z in note['support']))
 seen.add(note['id'])
pr=json.loads((ROOT/'source-extracts'/'source-provenance.json').read_text())
check('17 sources,42 files,13 LF units',pr['source_count']==17 and len(pr['files'])==42 and len(pr['literal_units'])==13)
for f in pr['files']:
 check('source copy '+f['copy'],sha((ROOT/f['copy']).read_bytes())==f['sha256'])
for u in pr['literal_units']:
 check('literal '+u['id'],sha((ROOT/'source-extracts'/u['file']).read_bytes())==u['excerpt_sha256'])
 check('literal body '+u['id'],(ROOT/'source-extracts'/u['file']).read_text()==u['literal'])
fc=json.loads((ROOT/'finite-checks.json').read_text());check('finite declared cases',fc['total']==22277 and fc['status']=='all finite cases passed')
build=json.loads((ROOT/'build-report.json').read_text())
check('three zero-return build commands',len(build['commands'])==3 and all(z['returncode']==0 for z in build['commands']))
for label in ('tex-pass-1','tex-pass-2'):
 check('retained log '+label,(ROOT/'build-logs'/f'{label}.log').stat().st_size>0)
for n,details in build['artifacts'].items():check('build artifact '+n,sha((ROOT/n).read_bytes())==details['sha256'])
check('PDF header',(ROOT/'P13.2-paper.pdf').read_bytes().startswith(b'%PDF-'))
report={'status':'all artifact checks passed','check_count':len(checks),'checks':checks,'limits':'Artifact and finite execution checks only; no mathematical correctness certification or original completion.'}
(ROOT/'validation-report.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps({'status':report['status'],'check_count':len(checks)}))
