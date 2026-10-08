"""Own artifact binding and retained allowed input snapshots; no supplied binder run."""
import pathlib,json,hashlib,shutil,subprocess,platform,sys,datetime
ROOT=pathlib.Path(__file__).resolve().parent;BASE=ROOT.parents[1]
def sha(b):return hashlib.sha256(b).hexdigest()
inputs=[]
for name in ['mathematical-packet-bindings.json','historical-own-evidence-bindings.json','private-primary-packet-bindings.json']:
    p=BASE/name;b=p.read_bytes();inputs.append({'manifest':name,'path':str(p),'bytes':len(b),'sha256':sha(b)})
    (ROOT/'LOCALONLY'/name).write_bytes(b)
    entries=json.loads(b)
    for i,e in enumerate(entries):
        b=pathlib.Path(e['path']).read_bytes();assert sha(b)==e['sha256'] and len(b)==e['bytes']
        inputs.append({'packet':name,'index':i,'path':e['path'],'bytes':len(b),'sha256':sha(b),'match':True})
        if name!='historical-own-evidence-bindings.json' or i in [0,2,3,4,5,6,9,10,11,12,13,14,15,16,17,18,19,21,22,23,24,25,26,27,28,29,30,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50]:
            d=ROOT/'LOCALONLY'/'bound-input-snapshots'/name.removesuffix('.json');d.mkdir(parents=True,exist_ok=True)
            dest=d/(f'{i:03d}-'+pathlib.Path(e['path']).name)
            # Supplied executable-looking files are saved as DATA only.
            if dest.suffix=='.py':dest=dest.with_name(dest.name+'.DATA.txt')
            dest.write_bytes(b);inputs[-1]['local_snapshot']=str(dest.relative_to(ROOT))
b=(ROOT/'input.json').read_bytes();inputs.append({'path':'input.json','bytes':len(b),'sha256':sha(b),'role':'current original task and assignment'})
(ROOT/'input-bindings.json').write_text(json.dumps(inputs,indent=2)+'\n')
env={'UTC':datetime.datetime.now(datetime.timezone.utc).isoformat(),'python':sys.version,'platform':platform.platform(),'cwd':str(ROOT),'requested_external_execution_configuration':'native gpt-6.1-sol xhigh ONE call; not independently certified or changed','supervised_compute_facility':'none supplied; no resource-heavy work performed'}
for argv in [['pdflatex','--version'],['pdftotext','-v'],['pdfinfo','-v']]:
    p=subprocess.run(argv,capture_output=True,text=True);env[argv[0]]=(p.stdout+p.stderr).split('\n')[0]
(ROOT/'environment.json').write_text(json.dumps(env,indent=2)+'\n')
out=[]
for p in sorted(ROOT.rglob('*')):
    if not p.is_file() or any(x.startswith('.') for x in p.relative_to(ROOT).parts) or p.name=='artifact-bindings.json':continue
    b=p.read_bytes();out.append({'path':str(p.relative_to(ROOT)),'bytes':len(b),'sha256':sha(b),'local_only':p.relative_to(ROOT).parts[0]=='LOCALONLY'})
(ROOT/'artifact-bindings.json').write_text(json.dumps({'candidate':False,'original_P05_1':'OPEN','original_P05_2':'OPEN','self_hash_excluded':True,'files':out,'meaning':'own byte identities; no historical did-read or mathematical-correctness certification'},indent=2)+'\n')
print(json.dumps({'bound_inputs_verified':64,'input_records_including_manifests_and_task':len(inputs),'own_artifacts_bound':len(out),'immutable_input_matches':True},indent=2))
