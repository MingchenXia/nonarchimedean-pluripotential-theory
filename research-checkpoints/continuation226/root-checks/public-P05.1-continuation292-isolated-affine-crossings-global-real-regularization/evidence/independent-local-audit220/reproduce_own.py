"""Own, bounded reproduction; never imports or runs supplied orchestration."""
from pathlib import Path
import hashlib, json, platform, re, shutil, subprocess, sys
BASE=Path('/workspace/research/campaigns/round-220/P05.1-unchanged-isolated-affine-crossings-whole-independent-native-local-source-audit')
NAMES={'m':'mathematical-packet-bindings.json','h':'historical-own-evidence-bindings.json','p':'private-primary-packet-bindings.json'}

def bound(k, i):
    return Path(json.loads((BASE/NAMES[k]).read_text())[i]['path'])
def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def put(p, v):
    Path(p).write_text(json.dumps(v, indent=2, ensure_ascii=False)+'\n')

dest=Path('own-reproduction')
dest.mkdir(exist_ok=False)
(dest/'logs').mkdir()
source=bound('m',19).read_text()
unsafe=re.findall(r'\\(?:input|include|write18|openin|openout|read|filecontents|directlua|catcode)\b',source)
assert not unsafe, unsafe
# The checker and its 477-byte input were inspected in full before this copy.
for k,i,name in [('m',19,'P05.1-paper.tex'),('h',17,'check_certificates.py'),('h',15,'certificate-input.json')]:
    shutil.copyfile(bound(k,i),dest/name)
    assert sha(dest/name)==sha(bound(k,i))

record={'source_sha256':sha(dest/'P05.1-paper.tex'),'source_LF':source.count('\n'),
        'python':sys.version,'platform':platform.platform(),'commands':[],
        'network_used':False,'subagents_used':False,'supplied_orchestration_executed':False,
        'supervised_heavy_compute_facility_exposed':False,'heavy_compute_needed':False}
def run(args, log):
    p=subprocess.run(args,cwd=dest,capture_output=True,text=True)
    (dest/'logs'/log).write_text(p.stdout+p.stderr)
    record['commands'].append({'argv':args,'exit_code':p.returncode,'log':'own-reproduction/logs/'+log})
    assert p.returncode==0,(args,p.returncode)
    return p

run([sys.executable,'check_certificates.py'],'checks.log')
record['finite_output_byte_equal']= (dest/'certificate-output.json').read_bytes()==bound('h',16).read_bytes()
assert record['finite_output_byte_equal']
for i in (1,2):
    run(['pdflatex','-no-shell-escape','-interaction=nonstopmode','-halt-on-error','P05.1-paper.tex'],f'build-pass-{i}.stdout.log')
    shutil.copyfile(dest/'P05.1-paper.log',dest/'logs'/f'build-pass-{i}.log')
p=run(['pandoc','-s','-f','latex','-t','markdown','--wrap=none','P05.1-paper.tex'],'pandoc.log')
(dest/'argument.md').write_text(p.stdout)
# Retain diagnostics without duplicating the whole argument in a log.
(dest/'logs'/'pandoc.log').write_text(p.stderr)
record['markdown_byte_equal']= (dest/'argument.md').read_bytes()==bound('m',20).read_bytes()
assert record['markdown_byte_equal']
record['markdown_sha256']=sha(dest/'argument.md')
record['source_unchanged']=sha(dest/'P05.1-paper.tex')==sha(bound('m',19))
record['diagnostics']=[[line for line in (dest/'logs'/f'build-pass-{i}.log').read_text().splitlines()
  if any(t in line for t in ('Warning','Overfull','Underfull','undefined','Error'))] for i in (1,2)]
assert not record['diagnostics'][1]
info=run(['pdfinfo','P05.1-paper.pdf'],'pdfinfo.txt').stdout
record['pdf_pages']=int(re.search(r'^Pages:\s+(\d+)',info,re.M).group(1))
assert record['pdf_pages']==17
record['pdf_sha256']=sha(dest/'P05.1-paper.pdf')
record['versions']={}
for prog,args in [('pdflatex',['pdflatex','--version']),('pandoc',['pandoc','--version']),('pdfinfo',['pdfinfo','-v'])]:
    p=run(args,prog+'-version.txt')
    record['versions'][prog]=(p.stdout+p.stderr).splitlines()[0]

f=json.loads(bound('m',23).read_text()); expanded=json.loads(bound('h',6).read_text())
registered=json.loads(bound('h',40).read_text())
record['exact_FINAL_sha256']=sha(bound('m',23))
record['six_exact_notes']=len(f['notes'])==6 and not f['candidate']
record['saved_native_byte_equal']=bound('m',23).read_bytes()==bound('h',28).read_bytes()==bound('h',39).read_bytes()
record['expanded_distinct']=bound('h',6).read_bytes()!=bound('m',23).read_bytes()
record['expanded_note_lengths']=[len(n['text']) for n in expanded['notes']]
record['exact_note_lengths']=[len(n['text']) for n in f['notes']]
workspace=registered['workspace']
record['registered_only_artifacts_suffix']=registered['candidate']==f['candidate'] and len(registered['notes'])==len(f['notes']) and all(
  x.keys()==y.keys() and all(y[key]==(x[key]+'\n\nArtifacts: '+workspace if key=='text' else x[key]) for key in x)
  for x,y in zip(f['notes'],registered['notes']))
record['parent_child_input_semantically_equal']=json.loads(bound('h',25).read_text())==json.loads(bound('h',61).read_text())
for key in ['six_exact_notes','saved_native_byte_equal','expanded_distinct','registered_only_artifacts_suffix','parent_child_input_semantically_equal','source_unchanged']:
    assert record[key], key
record['historical_initial_GFM_distinct']=bound('h',51).read_bytes()!=bound('m',20).read_bytes()
record['literal_qquad_retained']='sum_i w_i=0,qquad' in source
put('reproduction-evidence.json',record)
print(json.dumps({k:record[k] for k in ['source_sha256','finite_output_byte_equal','markdown_byte_equal','source_unchanged','pdf_pages','diagnostics','saved_native_byte_equal','expanded_distinct','registered_only_artifacts_suffix','parent_child_input_semantically_equal','literal_qquad_retained']},indent=2))
