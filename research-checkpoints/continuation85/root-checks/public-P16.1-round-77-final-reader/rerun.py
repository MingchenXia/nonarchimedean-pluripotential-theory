#!/usr/bin/env python3
"""Bounded, offline reproduction; no numerical test certifies an analytic proof."""
from pathlib import Path
import hashlib, json, platform, shutil, subprocess, sys
from fractions import Fraction as F
from itertools import product

ROOT = Path(__file__).resolve().parent
def digest(b): return hashlib.sha256(b).hexdigest()
def write_json(p, x):
    (ROOT/p).write_text(json.dumps(x, ensure_ascii=False, indent=2)+'\n')
def command(argv, stem):
    p = subprocess.run(argv, cwd=ROOT, capture_output=True)
    (ROOT/'build-logs'/f'{stem}.stdout').write_bytes(p.stdout)
    (ROOT/'build-logs'/f'{stem}.stderr').write_bytes(p.stderr)
    return {'argv':argv, 'returncode':p.returncode,
            'stdout':f'build-logs/{stem}.stdout','stderr':f'build-logs/{stem}.stderr'}

def main():
    original = (ROOT/'input.json').read_bytes()
    saved = ROOT/'input-original.json'
    if not saved.exists(): saved.write_bytes(original)
    assert saved.read_bytes() == original
    data = json.loads(original)
    write_json('task-original.json', data['task'])
    (ROOT/'assignment-original.txt').write_text(data['assignment'])
    marker = '# Authorized read-only primary sources\n'
    start = data['assignment'].index(marker)+len(marker)
    sources, _ = json.JSONDecoder().raw_decode(data['assignment'][start:])
    for folder in ['sources','source-extracts','build-logs','embedded-data']:
        (ROOT/folder).mkdir(exist_ok=True)
    (ROOT/'embedded-data/assignment-full.txt').write_text(data['assignment'])
    records=[]; texts={}
    for i,s in enumerate(sources,1):
        rec={'id':f'S{i}','version':s['saved_version'], 'title':s.get('title'),
             'public_source':s['public_source'],'files':[]}
        for key in ['pdf','literal_extract','abstract_html','html']:
            if key not in s: continue
            hashkey={'literal_extract':'extract_sha256','abstract_html':'abstract_sha256'}.get(key,key+'_sha256')
            content=Path(s[key]).read_bytes(); actual=digest(content)
            assert actual == s[hashkey], (s[key],actual)
            suffix=Path(s[key]).suffix
            local=Path('sources')/f'S{i}-{key}{suffix}'
            (ROOT/local).write_bytes(content)
            f={'authorized_path':s[key], 'local_copy':str(local), 'sha256':actual,
               'bytes':len(content),'expected_sha256':s[hashkey]}
            if key=='literal_extract':
                text=content.decode('utf-8'); lines=text.split('\n')
                texts[f'S{i}']=(text,lines,str(local),actual)
                f['LF_count']=len(lines); f['coordinate_rule']="UTF-8 bytes decode; split('\\n'); inclusive one-based"
            rec['files'].append(f)
        records.append(rec)
    units=[
      ('S1',435,469,'general reduced-variety conventions'),
      ('S1',759,874,'relative integral closure and vertical DVRs'),
      ('S1',938,1089,'flag ideals, PL lattice, density, actual divisor representation'),
      ('S1',1309,1352,'same-bundle FS generation and span'),
      ('S1',1420,1455,'actual test configuration and ample model'),
      ('S1',1687,1738,'Hdom on a fixed actual bundle'),
      ('S1',1810,1858,'raw model measure and compact-pairing IBP'),
      ('S1',2190,2289,'genuine cone and class closure'),
      ('S1',2414,2462,'regularization and genuine FS membership'),
      ('S1',2488,2541,'divisorial order, minimum usc extension'),
      ('S1',2859,2876,'birational onto with target-side approaching EP'),
      ('S1',2887,2957,'continuity of envelopes; compact-majorant nets'),
      ('S1',2980,3065,'smooth envelope theorem and proof'),
      ('S1',3649,3692,'general projective scope of global pairings'),
      ('S1',3980,4148,'genuine mixed operator, weighted convergence, continuous compatibility'),
      ('S1',4519,4607,'winning-locus locality and comparison'),
      ('S1',4892,4960,'energy differentiation and its limits'),
      ('S1',5230,5304,'target integral continuity and intrinsic energy condition'),
      ('S1',5440,5479,'uniqueness and domination'),
      ('S1',6092,6146,'EP equivalent to actual variational solvability'),
      ('S1',6230,6268,'sequential approximation only after membership'),
      ('S1',6304,6372,'EP assumed for contact orthogonality'),
      ('S2',635,781,'actual local definitions and printed contact/growth conventions'),
      ('S2',1236,1309,'bounded collar product claim and its convergence premises'),
      ('S2',1331,1537,'entire compact IBP, mass, comparison, membership proof'),
      ('S2',1560,1579,'printed smooth growth statement'),
      ('S2',2200,2372,'entire original nonflat trace argument'),
      ('S2',2697,2755,'entire envelope and field-descent argument'),
      ('S3',10432,10449,'CLD convergence is locally uniform and continuous'),
      ('S4',249,295,'formal/algebraic dependency actually cited'),
      ('S4',633,782,'represented-model nef detection and proper residual-curve proof'),
      ('S6',3580,3627,'analytic units are harmonic'),
      ('S6',3730,3741,'harmonic maximum principle'),
      ('S6',3783,3820,'subharmonic logs and decreasing limits'),
      ('S6',3860,3907,'harmonic-test characterization'),
      ('S7',2281,2363,'same-ample-class continuous FS theorem'),
      ('S7',2611,2779,'continuous products and uniform extension'),
      ('S7',3125,3202,'continuous Deligne comparison including proof'),
      ('S8',147,164,'general positive-current converse remains unknown'),
      ('S8',489,800,'entire local curve-lifting theorem and proof'),
      ('S8',803,926,'represented PL curve criteria and entire proofs'),
      ('S9',2077,2155,'compact norm-image theorem and exact algebraic reduction'),
      ('S10',2540,2589,'model positivity and proper residue tests')
    ]
    excerpts=[]
    for j,(sid,first,last,use) in enumerate(units,1):
        _,lines,path,h=texts[sid]; assert 1<=first<=last<=len(lines)
        literal='\n'.join(lines[first-1:last])
        name=f'source-extracts/{j:02d}-{sid}-{first}-{last}.txt'
        (ROOT/name).write_bytes(literal.encode('utf-8'))
        excerpts.append({'id':f'e{j}','source':sid,'source_text_sha256':h,
           'inclusive_LF':[first,last],'literal':literal,'sha256':digest(literal.encode()),
           'artifact':name,'application':use,
           'limit':'Pinned source data; retention and hashes are not independent mathematical validation.'})
    write_json('source-extracts/source-provenance.json',{'sources':records,'units':excerpts})
    checks={}; count=0
    # Exact saturation partition recursion, including the nonlinear-clipping alternatives.
    partition_cases=0
    for xs in product([F(i,4) for i in range(5)],repeat=4):
        partial=F(0); rows=[]
        for x in xs:
            r=min(x,1-partial); rows.append(r); partial+=r
        assert partial==min(F(1),sum(xs))
        assert all(F(0)<=r<=x for r,x in zip(rows,xs))
        if max(xs)==1: assert partial==1
        partition_cases+=1
    checks['partition']={'cases':partition_cases,'result':'pass','domain':'four rational cutoff values in {0,1/4,1/2,3/4,1}'}
    # Support clipping and maximum-penalty exactness, finite rational grid only.
    extension_cases=0
    for e,c,eta in product(range(-4,5),range(1,6),[F(i,4) for i in range(5)]):
        v=max(-c*eta,min(c*eta,e))
        assert abs(v)<=c*eta
        if eta==0: assert v==0
        if eta==1 and abs(e)<=c: assert v==e
        extension_cases+=1
    checks['support_clipping']={'cases':extension_cases,'result':'pass','domain':'E integers -4..4, C integers 1..5, eta in {0,1/4,1/2,3/4,1}'}
    collar_cases=0
    for M,eps,A in product(range(1,5),[F(1,4),F(1,2),F(1)],range(1,50)):
        if A*eps<=2*M+2: continue
        assert -A*eps+M+1<-M
        assert -F(1,2)+M+1>M+F(1,4)
        collar_cases+=1
    checks['collar_inequalities']={'cases':collar_cases,'result':'pass','domain':'M=1..4, eps in {1/4,1/2,1}, A=1..49 satisfying strict margin'}
    shifts=0
    for j in range(1,101):
        eps=F(1,4**j); nxt=eps/4; shift=F(8,3)*eps
        assert shift-shift/4-eps-nxt>0
        shifts+=1
    checks['decreasing_shift']={'cases':shifts,'result':'pass','domain':'j=1..100; epsilon_j=4^-j; B_j=(8/3)epsilon_j'}
    # Nonflat algebra multiplication law; fiber rank is separately proved on paper.
    norm_cases=0
    for x,a,b,c,d in product(range(-2,3),repeat=5):
        assert (a*c+x*b*d)**2-x*(a*d+b*c)**2==(a*a-x*b*b)*(c*c-x*d*d)
        norm_cases+=1
    checks['quadratic_norm']={'cases':norm_cases,'result':'pass','domain':'x,a,b,c,d integers -2..2'}
    count=sum(v['cases'] for v in checks.values())
    write_json('finite-checks.json',{'total_cases':count,'checks':checks,
       'epistemic_limit':'Exhaustive only on declared finite grids. No infinite analytic assertion was numerically validated.'})
    versions={}
    for prog in ['pandoc','pdflatex']:
        p=subprocess.run([prog,'--version'],capture_output=True)
        versions[prog]={'path':shutil.which(prog),'version':p.stdout.decode(errors='replace').split('\n')[0]}
    write_json('environment.json',{'python':sys.version,'platform':platform.platform(),
       'cwd':str(ROOT),'tools':versions,'network_used':False,'installations':False,
       'resource_heavy_compute':False,'supervised_compute_service':'No operator-provided supervised compute service was exposed; none was needed.',
       'model_setting':'Requested operator model setting was not inspected or changed.'})
    commands=[command(['pandoc','P16.1-argument.md','--standalone','--to=latex','--output=P16.1-paper.tex'],'pandoc')]
    for passno in [1,2]:
        commands.append(command(['pdflatex','-interaction=nonstopmode','-halt-on-error','P16.1-paper.tex'],f'pdflatex-pass{passno}'))
        log=ROOT/'P16.1-paper.log'
        if log.exists(): shutil.copyfile(log,ROOT/'build-logs'/f'pdflatex-pass{passno}.log')
    write_json('build-report.json',{'commands':commands,
       'tex_sha256':digest((ROOT/'P16.1-paper.tex').read_bytes()) if (ROOT/'P16.1-paper.tex').exists() else None,
       'pdf_sha256':digest((ROOT/'P16.1-paper.pdf').read_bytes()) if (ROOT/'P16.1-paper.pdf').exists() else None,
       'limit':'Compilation is an observation, not proof validation.'})
    assert all(c['returncode']==0 for c in commands),commands
    write_json('execution-report.json',{'input_bytes':len(original),'input_sha256':digest(original),
       'input_preserved_byte_identically':True,'primary_files_checked':sum(len(s['files']) for s in records),
       'literal_units':len(excerpts),'finite_cases':count,'rerun_command':'python3 rerun.py',
       'all_commands_succeeded':True,'candidate':False})
    print(json.dumps({'preserved_bytes':len(original),'primary_files':sum(len(s['files']) for s in records),
       'literal_units':len(excerpts),'finite_cases':count,'build_returncodes':[c['returncode'] for c in commands]}))

if __name__=='__main__': main()
