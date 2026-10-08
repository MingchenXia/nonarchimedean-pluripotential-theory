"""Own read-only binding/coverage analysis. No absent path is opened."""
import pathlib,json,hashlib,re,subprocess,sys
ROOT=pathlib.Path(__file__).resolve().parent
BASE=ROOT.parents[1]
def packet(n):return json.loads((BASE/n).read_bytes())
M=packet('mathematical-packet-bindings.json');E=packet('historical-own-evidence-bindings.json');P=packet('private-primary-packet-bindings.json')
def raw(e):return pathlib.Path(e['path']).read_bytes()
def sha(b):return hashlib.sha256(b).hexdigest()
def save(n,x):(ROOT/n).write_text(json.dumps(x,indent=2)+'\n')
own=[json.loads(s) for s in (ROOT/'own-read-displays.jsonl').read_text().split('\n') if s]
coverage=[]
for i,e in enumerate(M):
    if i in [0,1,2,3,8]:
        name=f'decoded-math-{i}.txt';n=len((ROOT/name).read_text().split('\n'))-1
        rows=[r for r in own if r.get('derived_file')==name]
        kind='JSON entire bytes parsed; all recursive leaves displayed in source order'
    else:
        n=len(raw(e).decode().split('\n'))-bool(raw(e).endswith(b'\n'))
        rows=[r for r in own if r.get('packet')=='m' and r.get('index')==i]
        kind='literal LF complete source displayed'
    seen={j for r in rows for j in range(r['start'],r['end']+1)}
    coverage.append({'index':i,'path':e['path'],'source_sha256':sha(raw(e)),'display_kind':kind,'display_lines':n,'ranges':[[r['start'],r['end']] for r in rows],'missing':sorted(set(range(1,n+1))-seen)})
save('whole-nine-coverage.json',coverage)
loc=ROOT/'LOCALONLY';loc.mkdir(exist_ok=True)
units={'BMPS':[(1,48),(254,301),(418,604),(689,847),(848,885),(886,894),(1005,1029),(1741,1746),(2259,2353)],'BBGS':[(1,38),(196,242),(383,413),(443,598),(604,670),(675,704),(1515,1787),(1876,1897),(1898,2000)]}
prim=[]
for key,rs in units.items():
    i=1 if key=='BMPS' else 3;b=raw(P[i]);lines=b.decode().split('\n')
    for a,z in rs:
        out='\n'.join(lines[a-1:z])+'\n';name=f'{key}-LF{a}-{z}.txt';(loc/name).write_text(out)
        reads=[r for r in own if r.get('packet')=='p' and r.get('index')==i]
        seen={k for r in reads for k in range(r['start'],r['end']+1)}
        prim.append({'source':key,'LF_first':a,'LF_last':z,'excerpt_file':'LOCALONLY/'+name,'sha256':sha(out.encode()),'missing_displays':sorted(set(range(a,z+1))-seen)})
save('primary-unit-coverage.json',prim)
artifact=json.loads(raw(E[9]));inp=json.loads(raw(E[11]));snap=json.loads(raw(E[12]));reads=[json.loads(s) for s in raw(E[16]).decode().split('\n') if s]
report={'author_artifact_metadata_entries':len(artifact['files']),'ROOT_report_verified_artifacts':json.loads(raw(E[35]))['verified_author_artifacts'],'inputs':len(inp),'snapshots':len(snap),'input_digest_equalities':all(x['sha256_actual']==x['sha256_bound'] for x in inp),'snapshot_digest_identities':all(x['sha256_actual']==y['sha256'] and x['bytes_actual']==y['bytes'] for x,y in zip(inp,snap)),'whole_read_log_records':len(reads),'unique_index_chunk_records':len({(x['index'],x['chunk']) for x in reads}),'no_absent_source_or_snapshot_bodies_opened':True,'historical_ROOT_verification_only_for_98_bodies':True,'not_a_did_read_or_universal_operations_certificate':True}
save('historical-metadata-analysis.json',report)
logs={}
for k in [18,19,21,22,23,24,25,26,27,28,29,39,47,48,49,50]:
    b=raw(E[k]);s=b.decode(errors='replace');lines=s.split('\n')
    logs[str(k)]={'path':E[k]['path'],'sha256':sha(b),'relevant_lines':[[i,t] for i,t in enumerate(lines,1) if re.search(r'Warning|Output written|shell|disabled|restricted|source_sha256|exit_code|success|pages',t)]}
save('historical-build-log-findings.json',logs)
tex=raw(M[4]).decode().split('\n');displays=[];proofs=[];start=None
for n,s in enumerate(tex,1):
    if '\\[' in s or '\\begin{align*}' in s:start=n
    if start is not None and ('\\]' in s or '\\end{align*}' in s):
        displays.append({'id':f'eq{len(displays)+1:02d}','first':start,'last':n,'text':'\n'.join(tex[start-1:n]),'verdict':'PASS','basis':'independent reconstruction in reconstructed-proofs.md; scope/hypotheses preserved'});start=None
    if '\\begin{proof}' in s:ps=n
    if '\\end{proof}' in s:proofs.append({'first':ps,'last':n,'verdict':'PASS'})
save('equation-and-proof-inventory.json',{'source_sha256':M[4]['sha256'],'displays':displays,'numbered_environment_proofs':proofs,'remaining_prose_coverage':'complete LF1--461 map in proof-coverage.md; unnumbered arguments separately covered'})
for i in [0,2]:
    b=raw(P[i]);name=P[i]['label']
    out=loc/f'{name}-fresh-pdftotext.txt'
    p=subprocess.run(['pdftotext','-layout',P[i]['path'],str(out)],capture_output=True,timeout=10)
    info=subprocess.run(['pdfinfo',P[i]['path']],capture_output=True,text=True,timeout=10)
    (loc/f'{name}-pdfinfo.txt').write_text(info.stdout)
    save(f'{name}-PDF-text-binding.json',{'argv':['pdftotext','-layout',P[i]['path'],str(out)],'exit_code':p.returncode,'pdf_sha256':sha(b),'fresh_text_sha256':sha(out.read_bytes()) if out.exists() else None,'fresh_extraction_exact_bound_text':out.exists() and out.read_bytes()==raw(P[i+1]),'whole_PDF_visual_read_claim':False,'pages':re.search(r'^Pages:\s+(\d+)',info.stdout,re.M)[1]})
print(json.dumps({'math_bodies':len(coverage),'missing_math_display_lines':sum(len(x['missing']) for x in coverage),'primary_units':len(prim),'missing_primary_display_lines':sum(len(x['missing_displays']) for x in prim),'display_equations':len(displays),'proof_environments':len(proofs),'historical_metadata':report},indent=2))
