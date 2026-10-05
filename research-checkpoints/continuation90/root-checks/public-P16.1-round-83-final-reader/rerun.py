from pathlib import Path
import json,hashlib,subprocess,sys,re
ROOT=Path(__file__).resolve().parent
EXPECTED='7ecc6bd499117a12eab966d8ef9feefdb9642d4a157bbb7b20870ac7f667ecb1'
def sha(b):return hashlib.sha256(b).hexdigest()
def dump(fn,obj):(ROOT/fn).write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
assert sha((ROOT/'input.json').read_bytes())==EXPECTED
assert (ROOT/'input-original.json').read_bytes()==(ROOT/'input.json').read_bytes()
commands=[]
def run(argv,stem):
 r=subprocess.run(argv,cwd=ROOT,capture_output=True,text=True)
 (ROOT/(stem+'.stdout')).write_text(r.stdout,encoding='utf8')
 (ROOT/(stem+'.stderr')).write_text(r.stderr,encoding='utf8')
 commands.append({'argv':argv,'cwd':str(ROOT),'exit_code':r.returncode,'stdout':stem+'.stdout','stderr':stem+'.stderr'})
 dump('command-log.json',commands)
 if r.returncode:raise SystemExit(f'Failed {argv}; see {stem}.stdout/stderr')
 return r
run(['python3','prepare.py'],'prepare-run')
run(['python3','premise_ledger.py'],'premise-run')
run(['python3','finite_checks.py'],'finite-run')
inp=json.loads((ROOT/'input.json').read_bytes());task=inp['task']
fnames=['n1-trace.md','n2-affine-tools.md','n3-runge-chain.md','n4-disposition.md']
texts=[(ROOT/f).read_text(encoding='utf8') for f in fnames]
head='''---
title: "Original-witness trace and a conditional countable Runge chain"
author: "Unverified mathematical proof draft"
date: "5 October 2026"
geometry: margin=0.85in
fontsize: 10pt
---

Candidate=false. The exact unchanged original P16.1 is not solved. The results below retain every contact and geometric antecedent of the task-granted round77 theorem and precise round80 PASS. The mathematical deductions are drafts; documentary execution does not validate them.

'''
appendix='\n\n# Exact unchanged task and full family\n\n'+task['problem']+'\n\n## Exact completion criterion\n\n'+task['completionCriteria']+'\n'
(ROOT/'P16.1-argument.md').write_text(head+'\n\n'.join(texts)+appendix,encoding='utf8')
run(['pandoc','P16.1-argument.md','--standalone','--from=markdown+tex_math_single_backslash-raw_tex','--to=latex','--include-in-header=paper-header.tex','--output=P16.1-paper.tex'],'pandoc-run')
for i in [1,2]:
 run(['pdflatex','-interaction=nonstopmode','-halt-on-error','P16.1-paper.tex'],f'pdftex-pass-{i}')
 (ROOT/f'build-pass-{i}.log').write_bytes((ROOT/'P16.1-paper.log').read_bytes())
summaries=[
 'Conditional whole-base weak trace reconstructed on the ONE original proper birational witness, using actual strict discs, every canonical positive norm character, and complete-fiber compactness. Smooth geometric witness antecedents remain conditional; no arbitrary-residue-field affine theorem is used.',
 'Proved controlled original-reference approximation for already genuine singular affine FS limits and replaced the false denominator bound by finite normalization and one uniform original-ring multiplier. Reconstructed the countable entropy barrier, Rossi and off-bad-set maximum control without singular EP.',
 'Under the explicitly retained smooth geometric antecedents, reconstructed the full countable-field split-piece, descending-Z, genuine Runge/Hartogs, finite-projection and singular-stratum chain, including gamma=1 and the final empty-Z local-to-global step. This does not give arbitrary-cardinality singular EP.',
 'Delivered a standalone conditional partial proof, exact input and primary evidence, both TeX pass logs, and rerun diagnostics. The genuine general-variety operator and uniqueness remain distinct from singular existence; GEO, resolved-nef fiber descent, singular EP, arbitrary-cardinality descent and normalization/E1 compatibility remain missing. Candidate=false.'
]
details=[
 'For k algebraically closed, trivially valued and characteristic zero, pi:Y->S finite from integral Y to a principal affine open in A^n, the weak trace is an actual original-base AFS limit under GEO. Construct the smooth-base extension first. At every analytic s use all normalized horizontal curves over H(s), lift them relatively to the original witness, construct genuine disc coordinates by contraction, prove strict radial limits including minus infinity, cover the entire finite Gauss fiber, and identify the original nonflat weights by polynomial norm-law equality and complete-field grouping. No fiber length identification or affine theorem over H(s) occurs.',
 'Starting with an actual decreasing AFS sequence v_j->v<=g+B, expanding reference-winning collars yield one genuine bundle and decreasing controlled FS approximation with every original generator. Height-one valuation inequalities give integral h=b^N f^(Nc/q); finite R[h] gives one f^M clearing every h^j, and hull tests followed by j-th roots give exact original-ring bounds. Rational entropy grid roofs give global majorants on all faces including infinity; interval maxima and decreasing generator padding handle real support coefficients and minus-infinity values. Rossi is proved by a compactly modified reference weight; off-bad-set control assumes local regularizability of ORIGINAL u.',
 'Over countable k, indicator traces are locally constant integers only, so one base neighborhood is fixed for every split test. Closed immersion ensures analytic injectivity. Raw positive weights give the split contradiction with a separate gamma=1 case and c times the boundary gap. Descending Z has a genuine componentwise dimension drop. Hartogs begins with a Runge exhaustion by strict polynomial domains with compact controlled closures, then derives the exact coefficient radius over every H(y), including infinity. Finite smooth-stratum projection is proved with secant/tangent avoidance and Nakayama, retaining U=pi^-1(S). Singular induction ends with the required empty-Z global argument. All accepted smooth compactification/domination/resolution gates remain conditional.',
 'The exact original family and arbitrary-cardinality projective geometrically unibranch domain are preserved. BJ supplies raw mass V=(L^n), genuine E1 operator, dual-energy condition E^vee(nu/V)<infinity, uniqueness modulo constants, and actual EP/onto equivalence. The new conditional countable affine chain does not prove resolved-nef fiber-value descent or singular EP, and cannot justify arbitrary-cardinality obstacle descent or normalization through unbounded E1 limits. Documentary checks retain exact primary versions, hashes and LF units, actual HTTP(S) primary premises with nonnegative indices, and separate mathematical limitations.'
]
supports=[[],[],['n1','n2'],['n1','n2','n3']]
pdf_log=(ROOT/'build-pass-2.log').read_text()
pages=re.search(r'Output written on P16\.1-paper\.pdf \((\d+) pages',pdf_log)
obs={'input_bytes':len((ROOT/'input.json').read_bytes()),'input_sha256':EXPECTED,'authorized_files':23,'literal_units':len(json.loads((ROOT/'source-extracts/source-provenance.json').read_text())['units']),'external_premises':len(json.loads((ROOT/'external-premises.json').read_text())['premises']),'finite_cases':json.loads((ROOT/'finite-checks.json').read_text())['total_finite_cases'],'pandoc_exit':commands[-3]['exit_code'],'pdftex_pass_exits':[commands[-2]['exit_code'],commands[-1]['exit_code']],'pdf_pages':int(pages[1]) if pages else None,'tex_sha256':sha((ROOT/'P16.1-paper.tex').read_bytes()),'pdf_sha256':sha((ROOT/'P16.1-paper.pdf').read_bytes()),'initial_build_failures':'Three failed builds retained: unmarked inline math, literal set-difference backslash, and escaped header under disabled raw TeX. Corrected by explicit math delimiters and an external TeX header.','epistemic_status':'Documentary observations, not a correctness verdict.'}
dump('execution-observations.json',obs)
texts[-1]+='\nObserved current rerun: '+json.dumps(obs,ensure_ascii=False)+'.\n'
notes=[{'id':f'n{i+1}','summary':summaries[i],'detailedSummary':details[i],'text':texts[i],'support':supports[i]} for i in range(4)]
dump('canonical-notes.json',{'notes':notes,'candidate':False})
gaps=['GEO smooth ample-boundary compactification/projective birational domination/resolution witnesses remain explicit conditional antecedents.','Resolved-nef fiber constancy and usc descent over every completed residue field, including minus infinity, remain unproved.','Singular countable EP remains unproved; printed Wu envelope proof depends on unresolved fiber descent.','Arbitrary-cardinality finite-data obstacle/competitor descent preserving original nonnormal fibers, references and positive raw masses remains unproved.','Target-side normalization descent and unbounded E1/MA compatibility remain unproved.','The actual singular raw-mass finite-energy existence theorem has not been deduced.']
dump('status.json',{'id':'P16.1','status':'partial','exact_result':'Unverified conditional original-witness whole-base trace and complete countable-field affine Runge/Hartogs/singular-stratum chain, plus controlled original-ring approximation and pole repair; original arbitrary-cardinality singular equation unresolved.','proof_file':'P16.1-argument.md','concrete_gaps':gaps})
checks=[]
checks.append(('exact_input_bytes',(ROOT/'input.json').read_bytes()==(ROOT/'input-original.json').read_bytes()))
checks.append(('exact_task_value',json.loads((ROOT/'task-original.json').read_text())==task))
checks.append(('exact_assignment',(ROOT/'assignment-original.txt').read_text()==inp['assignment']))
prov=json.loads((ROOT/'source-extracts/source-provenance.json').read_text())
for f in prov['files']:checks.append((f['file'],sha((ROOT/f['file']).read_bytes())==f['sha256']))
for u in prov['units']:
 source=next(f['file'] for f in prov['files'] if f['source']==u['source'] and f['file'].endswith('.txt'))
 raw=(ROOT/source).read_bytes();ls=raw.decode('utf8').split('\n');a,b=u['inclusive_one_based_LF']
 checks.append((u['literal_file'],(ROOT/u['literal_file']).read_bytes()=='\n'.join(ls[a-1:b]).encode() and sha(raw)==u['source_sha256']))
ledger=json.loads((ROOT/'external-premises.json').read_text())
assert sorted(p['premise'] for p in ledger['passages'])==list(range(len(ledger['premises'])))
for p in ledger['passages']:
 checks.append((p['id']+' literal',sha((ROOT/p['literal_file']).read_bytes())==p['literal_sha256']))
 checks.append((p['id']+' HTTP(S) indexed premise',p['url'].startswith(('http://','https://')) and 0<=p['premise']<len(ledger['premises'])))
checks.append(('status_exact_keys',set(json.loads((ROOT/'status.json').read_text()))=={'id','status','exact_result','proof_file','concrete_gaps'}))
checks.append(('native_backward_supports',all(set(n['support'])<=set(f'n{j+1}' for j in range(i)) for i,n in enumerate(notes))))
checks.append(('candidate_false',not json.loads((ROOT/'canonical-notes.json').read_text())['candidate']))
checks.append(('both_complete_pass_logs',all((ROOT/f'build-pass-{i}.log').is_file() and (ROOT/f'build-pass-{i}.log').stat().st_size>0 for i in [1,2])))
assert all(v for _,v in checks)
dump('artifact-checks.json',{'checks':checks,'count':len(checks),'all_pass':True,'epistemic_limit':'Artifact consistency only; no independent mathematical review.'})
artifact_names=fnames+['input.json','input-original.json','task-original.json','assignment-original.txt','P16.1-argument.md','P16.1-paper.tex','P16.1-paper.pdf','canonical-notes.json','status.json','external-premises.json','finite-checks.json','artifact-checks.json','build-pass-1.log','build-pass-2.log','environment.json','command-log.json','execution-observations.json','rerun.py','prepare.py','premise_ledger.py','finite_checks.py','format_trace.py','paper-header.tex']
artifact_names+=sorted(p.name for p in ROOT.glob('*-failed-*') if p.is_file())
dump('artifact-hashes.json',[{'file':f,'bytes':(ROOT/f).stat().st_size,'sha256':sha((ROOT/f).read_bytes())} for f in artifact_names])
print(json.dumps({'status':'partial','candidate':False,'artifact_checks':len(checks),**obs},ensure_ascii=False))
