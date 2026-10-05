"""Publish unchanged reviewed partial mathematics and freeze unreviewed public drafts."""
from pathlib import Path
from datetime import datetime, timezone
import csv
import hashlib
import json
import shutil
import subprocess

R = Path('/workspace/research')
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
write = lambda p, d: Path(p).write_text(json.dumps(d, ensure_ascii=False, indent=2)+'\n')
now = datetime.now(timezone.utc).isoformat()
Q = R/'campaigns/round-76/P13.2-public-source-same-partial-theorem-and-valid-evidence-mathematical-review'
N = R/'root-checks/P13.2-round76-actual-same-scope-partial-mathematical-review-20261005.json'
assert sha(N) == 'f3be9b36ea393a2e9f561c208f4718e2cdaf7a86cb1f6d458f12eb2ca91ab3c0'
j = json.loads(N.read_text())
assert j == json.loads((Q/'run.json').read_text())['campaign']['result']
assert j['verdict'] == 'PASS' and len(j['premises']) == 6 and len(j['passages']) == 17
freeze = json.loads((Q/'freeze.json').read_text())
for name, key in [('task.json','task_sha256'),('argument.md','argument_sha256'),('settings.json','settings_sha256')]:
    assert sha(Q/name) == freeze[key]
assert (Q/'task.json').read_bytes() == (R/'campaigns/round-74/P13.2-public-source-fixed-ray-polynomial-and-uniform-target-mathematical-review/task.json').read_bytes()
coverage = {i:[] for i in range(6)}
for i, p in enumerate(j['passages']):
    assert p['id'] == j['operationId']+'/'+str(i)
    assert type(p['premise']) is int and 0 <= p['premise'] < 6
    assert p['statement'] == j['premises'][p['premise']] and p['quote'].strip()
    assert p['url'] in {'https://arxiv.org/pdf/2307.01697v1','https://arxiv.org/pdf/2609.27610v1'}
    coverage[p['premise']].append(i)
assert all(coverage.values())
V = R/'root-checks/public-P13.2-round-73-final-reader'
P = R/'deliverables/scoped-P13.2-round73'
assert not P.exists()
expected = {'P13.2-argument.md':'1945efebae76fcc4b540d36d1058c5fb40a04668b32aea28c8ecd03ba36367ee',
    'P13.2-paper.tex':'73aecd43569e1250c7477ffd7d2be1254a9ef7b3c5a52893a7dfb9a475b01730',
    'P13.2-paper.pdf':'d0be5d9f777f14eb1db5f936ea94ae4b78315d096c16469182ab01fd66f32cdd'}
for name, h in expected.items(): assert sha(V/name) == h
build = json.loads((V/'build-report.json').read_text())
assert all(x['returncode'] == 0 for x in build['commands'])
P.mkdir()
for name in [*expected,'canonical-notes.json','build-report.json','root-preservation-and-read-state-continuation81.json']:
    shutil.copyfile(V/name,P/name)
shutil.copyfile(N,P/'P13.2-correctness-review.json')
U = P/'independent-review-inputs'; U.mkdir()
for name in ['task.json','argument.md','settings.json','freeze.json']: shutil.copyfile(Q/name,U/name)
scope = 'Fixed-Reeb intrinsic finite-dual-energy target criterion; genuine fixed-ray polynomial and uniform signed target estimate; approximate Monge–Ampere measures and I-Cauchy dual maximizers. General finite-energy realization and original P13.2 remain open.'
pub = {'published_utc':now,'atom':'P13.2','author_round':73,'independent_review_round':76,'scope':scope,
    'independently_reviewed_partial_theorem':True,'fully_solved_original_atom':False,
    'original_remaining_gaps':['Actual finite-energy I-limit realization or an independently proved envelope theorem','Unconditional existence for every original finite-energy target and actual operator surjectivity'],
    'review':str(P/'P13.2-correctness-review.json'),'review_sha256':sha(N),'verdict':'PASS',
    'operation_id':j['operationId'],'reported_utc':j['reportedAt'],
    'entire_report_premises_and_passages_root_read':True,'premises':6,'passages':17,
    'exact_zero_based_binding_coverage':coverage,'task_sha256':freeze['task_sha256'],
    'argument_packet_sha256':freeze['argument_sha256'],'mathematical_task_unchanged_from_round74':True,
    'previous_round74_verdict_preserved':'INCONCLUSIVE','author_original_candidate':False,
    'whole_author_argument_root_read':True,'whole_tex_root_read':False,
    'source':str(P/'P13.2-paper.tex'),'source_sha256':sha(P/'P13.2-paper.tex'),
    'pdf':str(P/'P13.2-paper.pdf'),'pdf_sha256':sha(P/'P13.2-paper.pdf'),'pages':11,
    'author_paper_and_argument_bytes_unchanged':True,'local_two_pass_return_codes':[0,0],
    'native_compile':'Not checked for this copy; prior native handler unavailable. No native success asserted.',
    'limits':'Independent source-aware mathematical reconstruction by the requested model. No formal certificate, novelty claim, or original-problem closure inferred from a partial PASS.'}
write(P/'publication-preparation.json',pub)
(P/'README.md').write_text('# P13.2: independently reviewed partial results\n\n'+scope+'\n\nThe unchanged 11-page paper is accompanied by the actual round76 PASS, all six external premises and seventeen passages, and the exact frozen review inputs. Round74 INCONCLUSIVE is preserved in its historical reader. The paper retains its original unverified-draft author label; the independent verdict applies only to the task and claims specified in the review. Four original problems remain solved; this publication adds one scoped paper, not an original solution.\n')

C = R/'campaigns/round-75/P16.1-public-source-actual-metric-collars-and-whole-base-trace-equation'
A = R/'root-checks/P16.1-round75-actual-result-20261005.json'
assert sha(A) == 'b4d0366dc744bb13027b3cbf3f1b1cbae707d7da5ed522f377da974cb3e59b40'
actual = json.loads(A.read_text()); assert actual == json.loads((C/'run.json').read_text())['campaign']['result']
assert actual['candidate'] is False and [n['id'] for n in actual['notes']] == ['n1','n2','n3','n4']
W = Path(actual['workspace']); D = R/'root-checks/public-P16.1-round-75-final-reader'; assert not D.exists()
native = json.loads((W/'input.json').read_text()); assert native == json.loads((C/'input.json').read_text())
assert (W/'input.json').read_bytes() == (W/'input-original.json').read_bytes()
assert json.loads((W/'task-original.json').read_text()) == native['task']
assert (W/'assignment-original.txt').read_text() == native['assignment']
assert sha(W/'P16.1-argument.md') == 'eb6c9631b1f3c630bc3f502e5231ea1ad0f944f34b3a153596e513c1d1a95365'
prov = json.loads((W/'source-extracts/source-provenance.json').read_text())
assert len(prov['sources']) == 10 and len(prov['units']) == 50
primary=[]; texts={}
for s in prov['sources']:
    for f in s['files']:
        assert sha(f['authorized_path']) == f['sha256'] == sha(W/f['local_file'])
        primary.append({'source_id':s['id'],**f})
        if f['role'] == 'literal_extract': texts[s['id']] = Path(f['authorized_path'])
for u in prov['units']:
    source = texts[u['id'].split('-')[0]]; first,last=u['inclusive_one_based_LF']
    assert sha(source) == u['source_sha256']
    assert (W/u['literal_file']).read_bytes().decode() == '\n'.join(source.read_bytes().decode().split('\n')[first-1:last])
    assert sha(W/u['literal_file']) == u['literal_sha256']
assert len(primary) == 23
b=json.loads((W/'build-report.json').read_text()); assert all(x['returncode']==0 for x in b['commands'])
for name,h in b['artifacts'].items(): assert sha(W/name) == h
info=subprocess.run(['pdfinfo',str(W/'P16.1-paper.pdf')],capture_output=True,text=True,check=True).stdout
assert 'Pages:           14' in info
D.mkdir(); files=[]
for p in sorted(W.rglob('*')):
    if not p.is_file(): continue
    rel=p.relative_to(W); assert not p.is_symlink()
    assert not any(x in {'.git','.codex','.aws','.env','auth.json','run.json','campaign.sqlite','review.sqlite'} for x in rel.parts)
    assert p.suffix not in {'.sqlite','.jsonl'}
    target=D/rel; target.parent.mkdir(parents=True,exist_ok=True); shutil.copyfile(p,target)
    assert sha(p)==sha(target); files.append({'file':str(rel),'sha256':sha(p),'bytes':p.stat().st_size})
shutil.copyfile(A,D/'canonical-native-result.json')
write(D/'root-preservation-and-read-state-continuation83.json',{'recorded_utc':now,'atom':'P16.1','round':75,
    'candidate':False,'original_closed':False,'native_workspace':str(W),'actual_result_sha256':sha(A),
    'entire_actual_four_notes_root_read':True,'whole_argument_root_read':True,
    'argument_read_ranges':[[1,125],[126,245],[246,337]],'argument_sha256':sha(D/'P16.1-argument.md'),
    'bounded_collar_proof_whole_root_read':True,'whole_tex_root_read':False,
    'all_literal_bodies_root_read':False,'whole_primary_bodies_root_read':False,
    'primary_file_bindings':primary,'literal_units':prov['units'],'preserved_author_files':files,
    'author_two_pass_compilation':'SUCCESS','pdf_pages':14,'new_mathematics_independently_reviewed':False,
    'limits':'Actual representation, bounded collars and canonical determinant drafts remain unreviewed; Gate B, singular EP and actual equation existence remain open.'})

F=R/'root-checks/P16.1-fixed-bundle-rational-metric-and-exact-Gauss-cutoff-20261005-continuation83.md'
assert sha(F)=='8d8c07aacd95907405349f42624d9d98a648ea4daabe262a7955f4df96e564c1'
S=R/'root-checks/continuation83-fixed-bundle-metric-source-reads'; assert not S.exists(); S.mkdir(); units=[]
specs=[
 ('GM1608.08030v3-20261004-continuation66.txt','1608.08030v3',[(89,135),(270,399),(632,698),(731,782)],'Already represented original-bundle PL metric; ordinary point neighborhoods test nefness. Algebraization cites GK17, whose full dependency is not independently reconstructed.'),
 ('GR2503.05513v1-20261005-continuation72.txt','2503.05513v1',[(818,934)],'Curve criterion applies after actual PL representation; unrestricted positive-current converse is not assumed.'),
 ('GJR2111.05741v3-20261005-continuation72.txt','2111.05741v3',[(2298,2425)],'Semipositivity is not a G-sheaf; use ordinary neighborhoods and retain entire residual-curve tests.'),
 ('P16-arxiv-1805.01016-20261004.txt','1805.01016v3',[(2252,2357)],'Same original ample class and nontrivially valued extension; no EP or arbitrary continuous weak-metric rational approximation asserted.'),
 ('Ducros-published-1250007-20261005-continuation72.txt','Published DOI10.1142/S1793744212500077',[(2077,2150)],'Theorem3.2 compact finite-unit log image and pertinent proof; not a claim of having read all Theorem3.4.'),
 ('Thuillier-tel-00010990v1.txt','tel-00010990v1',[(3720,3824),(3830,3945)],'Previously whole-read root80 local harmonic tests, decreasing limits and strong maximum principle. Actual curve pullback supplied; no current converse.')]
for name,version,ranges,limit in specs:
    source=R/'shared-sources'/name
    for first,last in ranges:
        q=S/(name.removesuffix('.txt')+f'-LF{first}-{last}.txt')
        q.write_bytes('\n'.join(source.read_bytes().decode().split('\n')[first-1:last]).encode())
        units.append({'source':str(source),'source_sha256':sha(source),'version':version,
            'inclusive_one_based_LF':[first,last],'literal_file':str(q),'literal_sha256':sha(q),
            'whole_literal_body_root_read':True,'application_and_limit':limit})
write(S/'source-read-record.json',{'recorded_utc':now,'proposal':str(F),'proposal_sha256':sha(F),
    'whole_saved_proposal_root_read':True,'proposal_read_ranges':[[1,50],[51,75]],'units':units,
    'LF_convention':'UTF-8 bytes decode and split("\\n"), inclusive one-based ranges',
    'whole_primary_bodies_root_read':False,'accepted_dependency':False,'original_closed':False,
    'new_mathematics_independently_reviewed':False,'hot_feedback_sent':False,
    'limits':'Only an already supplied continuous rational PL weight is treated. Arbitrary weak-metric rational approximation, common collars, local-global membership, EP and existence require further proof.'})

a=json.loads((R/'active-work.json').read_text()); c=json.loads((R/'checklist-current.json').read_text())
assert sum(len(t['reviewed_papers']) for t in c['targets'])==40
solved=['P13.1','P15.1','P15.2','P16.6']; assert sorted(t['id'] for t in c['targets'] if t['fully_solved'])==solved
entry={k:pub[k] for k in ['scope','source','source_sha256','pdf','pdf_sha256','pages','review','review_sha256','verdict','operation_id','reported_utc','premises','passages']}
entry.update({'argument':str(P/'P13.2-argument.md'),'publication_preparation':str(P/'publication-preparation.json'),
    'publication_preparation_sha256':sha(P/'publication-preparation.json'),'all_zero_based_exact_statement_bindings_verified':True,'full_original_atom_solved':False})
t=next(t for t in c['targets'] if t['id']=='P13.2'); t['reviewed_papers'].append(entry)
t['research_status']='fixed_Reeb_target_and_signed_estimate_reviewed_partial_original_realization_open'
t['current_focus']='Actual finite-energy realization or independently reconstructed normal-cone envelope theorem; round73 partial accepted by actual round76 review.'
t['current_reviewed_partial_round73']=entry
u=next(t for t in c['targets'] if t['id']=='P16.1'); u['research_status']='actual_metric_collars_and_canonical_trace_unreviewed_original_gate_B_and_EP_open'
u['current_focus']='Compact signed PL integration by parts, bounded-local mass/comparison and smooth weak globalization; round75 actual partial completed.'
assert sum(len(t['reviewed_papers']) for t in c['targets'])==41
c['historical_reviewed_scoped_papers']=41; c['updated_utc']=now
a['updated_utc']=now; a['P13.2_round73_reviewed_partial']=entry
a['goal_state']='4/42 unchanged original problems solved;38 remain open;41 historical reviewed scoped papers. Continue until the original goal is fulfilled.'
a['completed_actual_round75_author']={'reader':str(D),'candidate':False,'whole_argument_and_all_notes_root_read':True,'original_closed':False}
a['continuation83_unreviewed_root_proposal']={'path':str(F),'sha256':sha(F),'source_read_record':str(S/'source-read-record.json'),'source_read_record_sha256':sha(S/'source-read-record.json'),'accepted_dependency':False}
write(R/'active-work.json',a); write(R/'checklist-current.json',c)
with (R/'checklist-current.tsv').open('w',newline='') as h:
    w=csv.writer(h,delimiter='\t'); w.writerow(['ID','Closure','Research','Reviewed_papers','Title'])
    for t in c['targets']: w.writerow([t['id'],t['closure'],t['research_status'],len(t['reviewed_papers']),t['title']])
print(json.dumps({'publication':str(P),'review':'PASS','originals_solved':4,'scoped_papers':41,
    'P16_reader':str(D),'preserved_author_files':len(files),'root83_literal_units':len(units)},indent=2))
