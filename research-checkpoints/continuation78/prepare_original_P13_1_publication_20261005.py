"""Preserve the exact accepted proof and make only the auditor's lexical clarifications."""
from pathlib import Path
from datetime import datetime, timezone
import difflib
import hashlib
import json
import shutil
import subprocess

R=Path('/workspace/research')
reader=R/'root-checks/public-P13.1-round-63-final-reader'
Q=R/'campaigns/round-63/P13.1-public-source-eleven-body-semigroup-and-uniform-differentiation-original-review'
P=R/'root-checks/P13.1-round63-actual-original-review-20261005.json'
D=R/'deliverables/original-P13.1'
assert not D.exists()
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
write=lambda p,d:Path(p).write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
review=json.loads(P.read_text());task=json.loads((Q/'task.json').read_text())
assert review['verdict']=='PASS' and len(review['premises'])==24 and len(review['passages'])==55
covered=set();bindings=[]
for i,p in enumerate(review['passages']):
    assert p['id']==review['operationId']+'/'+str(i)
    assert p['statement']==review['premises'][p['premise']]
    if p['url']=='urn:xean:task':assert p['quote'] in task['problem']+'\n'+task['completionCriteria']
    else:assert p['url'].startswith('https://')
    covered.add(p['premise']);bindings.append({'id':p['id'],'premise':p['premise'],'statement_exact':True,'url':p['url']})
assert covered==set(range(24))
assert sha(reader/'P13.1-argument.md')=='de75b9ae55fbeb63c605505a328ed306c321a8e674331827cde51f5cfad76609'
assert sha(Q/'argument.md')=='da9bd31729e4396ca78c77700ec11280653d71e4895701a496625647fc96dfe5'
D.mkdir(parents=True)
shutil.copyfile(P,D/'P13.1-original-scope-review.json')
shutil.copyfile(reader/'P13.1-argument.md',D/'P13.1-reviewed-argument.md')
shutil.copyfile(reader/'P13.1-paper.tex',D/'P13.1-reviewed-paper.tex')
shutil.copyfile(reader/'actual-canonical-notes.json',D/'P13.1-reviewed-canonical-notes.json')
shutil.copyfile(reader/'sources.json',D/'sources.json')
shutil.copytree(reader/'source-extracts',D/'source-extracts')
shutil.copyfile(Q/'task.json',D/'P13.1-original-review-task.json')
sources=json.loads((reader/'source-extracts/source-provenance.json').read_text())
for s in sources['sources']:
    for f in s['files']:assert sha(f['path'])==f['sha256']==f['expected_sha256']
assert len(sources['excerpts'])==63
for e in sources['excerpts']:
    # Author provenance uses source IDs and LF coordinates; its frozen reader
    # already reproduces all bodies. Reproduce again using that exact schema.
    s=next(s for s in sources['sources'] if s['id']==e['source'])
    f=next(f for f in s['files'] if f['kind']=='literal_extract')
    literal='\n'.join(Path(f['path']).read_bytes().decode('utf-8').split('\n')[e['lf_start']-1:e['lf_end']])
    assert literal==e['literal_statement_and_proof_body']
    assert sha(D/e['artifact'])==e['sha256']
old=(reader/'P13.1-argument.md').read_text()
body=old
def once(before,after):
    global body
    assert body.count(before)==1, before
    body=body.replace(before,after,1)
once('author: "Public-source reconstruction; unverified draft"','author: "Research manuscript"')
once('The following is the result claimed by this draft.','The following is the main result.')
once('Mathematical statements in this document remain unverified draft claims; execution is not a correctness or novelty verdict.',
     'The complete original P13.1 proof received an independent source-aware computational reconstruction with verdict PASS on 5 October 2026. This is not a formal proof certificate or a priority claim; the exact review and source bindings accompany the paper.')
once('Let homogeneous algebra generators $g_i$ (redundant elements are allowed)',
     'Let nonconstant homogeneous algebra generators $g_i$ of positive Reeb degree (redundant elements are allowed)')
assert body.count(',qquad')==2
body=body.replace(',qquad', ',\\qquad')
once('Products after clearing rational logarithmic exponents give positive sums of FS functions, with slopes added; maxima concatenate lists.',
     'Finite power/product constructions clear rational logarithmic coefficients and give positive sums of FS functions, with slopes added; real coefficients are obtained through the stated CPSH uniform closure. Maxima concatenate lists.')
once('Applying (35)--(38) to that norm gives',
     'For this application of the counting argument, the included witness triples already generate the full group lattice, so the conductor proof does not require the original strict bottom-weight margin again. Applying (35)--(38) to that norm gives')
marker='## 15. Execution and reproducibility'
assert body.count(marker)==1
body=body.split(marker,1)[0]+'''## 15. Scope and verification

The theorem solves original P13.1 on its normal-cone domain. The independent
original-scope review returned PASS on 5 October 2026, after reconstructing the
mathematical dependency chain. Its 24 premises and 55 evidence passages are
preserved with the exact reviewed proof. The publication applies only the
reviewer's three wording clarifications and corrects two missing LaTeX
backslashes; the theorem, estimates, hypotheses and proof dependencies are
unchanged. P13.2 remains a separate open image and existence problem.

The evidence annex preserves 63 literal primary statement/proof units and all
source versions, application limits and hash bindings. Compilation and finite
arithmetic diagnostics are execution checks, not proofs of the mathematical
claims or certificates of novelty. The computational review is not a formal
proof certificate or a peer-review verdict.

## References

'''
for s in sources['sources']:
    body+='['+s['id']+'] '+s['title']+'. '+s['version']+'. <'+s['public_source']+'>.\n\n'
(D/'P13.1-argument.md').write_text(body)
(D/'publication-only-clarifications.patch').write_text(''.join(difflib.unified_diff(
    old.splitlines(keepends=True),body.splitlines(keepends=True),
    fromfile='exact-reviewed-argument',tofile='publication-argument')))
build=D/'build';build.mkdir()
commands=[]
for label,command in [
    ('pandoc',['pandoc','P13.1-argument.md','--standalone','--to=latex','--output=P13.1-paper.tex']),
    ('tex-pass-1',['pdflatex','-interaction=nonstopmode','-halt-on-error','-output-directory=build','P13.1-paper.tex']),
    ('tex-pass-2',['pdflatex','-interaction=nonstopmode','-halt-on-error','-output-directory=build','P13.1-paper.tex']),
    ('pdfinfo',['pdfinfo','build/P13.1-paper.pdf'])
]:
    proc=subprocess.run(command,cwd=D,capture_output=True,text=True)
    (build/(label+'.stdout.txt')).write_text(proc.stdout)
    (build/(label+'.stderr.txt')).write_text(proc.stderr)
    if label.startswith('tex') and (build/'P13.1-paper.log').exists():
        shutil.copyfile(build/'P13.1-paper.log',build/(label+'.log'))
    commands.append({'command':command,'returncode':proc.returncode,
                     'stdout':'build/'+label+'.stdout.txt','stderr':'build/'+label+'.stderr.txt'})
    if proc.returncode:raise RuntimeError(label+' failed; source and diagnostics preserved')
shutil.copyfile(build/'P13.1-paper.pdf',D/'P13.1-paper.pdf')
pdfinfo=(build/'pdfinfo.stdout.txt').read_text()
pages=int(next(line.split(':',1)[1].strip() for line in pdfinfo.splitlines() if line.startswith('Pages:')))
scope='Every normal good affine cone over an algebraically closed trivially valued characteristic-zero field; all nonproportional and irrational Reeb fields. Actual H/CPSH/PSH order transport and normalized onto E1 comparison with exp(plus/minus(2n+1)delta) energy bounds. On compact Reeb sets, the canonical outer extension agrees with every actual PSH energy and has a potential-independent quadratic remainder for the fixed dense direction lattice, and uniform derivative for each fixed continuous direction given by the genuine probability MA. No singular envelope premise, general unbounded moving-field measure limit, or P13.2 existence claim.'
closure={'atom':'P13.1','fully_solved_original_atom':True,'original_statement_unchanged':True,
    'exact_scope':scope,'source':str(D/'P13.1-paper.tex'),'source_sha256':sha(D/'P13.1-paper.tex'),
    'pdf':str(D/'P13.1-paper.pdf'),'pdf_sha256':sha(D/'P13.1-paper.pdf'),'pages':pages,
    'argument':str(D/'P13.1-argument.md'),'argument_sha256':sha(D/'P13.1-argument.md'),
    'local_two_pass_compilation':'SUCCESS','native_compilation':'NOT_YET_REQUESTED_FOR_PUBLICATION_SOURCE',
    'first_and_last_pages_visually_read':False,
    'review':str(D/'P13.1-original-scope-review.json'),'review_sha256':sha(P),
    'verdict':review['verdict'],'reported_utc':review['reportedAt'],'operation_id':review['operationId'],
    'entire_report_premises_and_passages_root_read':True,
    'all_zero_based_exact_statement_bindings_verified':True,'premises':24,'passages':55,
    'reviewed_argument_sha256':sha(reader/'P13.1-argument.md'),
    'original_review_packet_sha256':sha(Q/'argument.md'),
    'publication_changes':'Three explicit harmless wording clarifications and two missing qquad backslashes; metadata/references and verification section edited. No mathematical change.',
    'primary_literal_units':63,'primary_sources':11,
    'review_limit':'Source-aware computational reconstruction by the requested native model, not a formal proof certificate, peer-review verdict or priority claim.'}
write(D/'original-closure.json',closure)
write(D/'publication-preparation.json',{'prepared_utc':datetime.now(timezone.utc).isoformat(),
      'commands':commands,'original_closure':closure,'passage_bindings':bindings,
      'whole_review_report_premises_and_passages_root_read':True,'whole_reviewed_argument_root_read':True,
      'whole_publication_tex_root_read':False,'all_literal_bindings_reproduced':True,
      'editor':'Existing P16.4 editor remains open and unchanged; no tab opened.'})
now=datetime.now(timezone.utc).isoformat()
a=json.loads((R/'active-work.json').read_text());c=json.loads((R/'checklist-current.json').read_text())
assert len(c['targets'])==42 and sum(len(t['reviewed_papers']) for t in c['targets'])==40
t=next(t for t in c['targets'] if t['id']=='P13.1');assert t['fully_solved'] is False
t.update({'closure':'solved','fully_solved':True,'research_status':'original_scope_completed',
          'current_focus':scope,'original_solution_paper':closure,
          'historical_gap_labels_superseded_by_original_scope_audit':True,'remaining_full_target':[]})
a['full_solutions'].append(closure)
solved=['P13.1','P15.1','P15.2','P16.6']
a['fully_solved_original_atoms']=solved;c['fully_solved_original_atoms']=solved
a['goal_state']='4/42 unchanged original problems solved;38 remain open;40 historical reviewed scoped papers. Continue until the original goal is fulfilled.'
a['updated_utc']=now;c['updated_utc']=now
a['P13.1_round63_actual_original_review']={'actual_result':str(P),'sha256':sha(P),
    'verdict':'PASS','entire_result_root_read':True,'premises':24,'passages':55,
    'original_closed':True,'publication':str(D),'publication_source_native_compile':'NOT_YET_REQUESTED'}
receipt=json.loads((R/'github-checkpoint/push-receipt-continuation77.json').read_text())
assert receipt['remote_ref_verified'] and receipt['all_file_blob_bindings_verified_remote']
a['github_checkpoint']=receipt;c['latest_verified_github_checkpoint']=receipt
a['github_pending_checkpoint']='Next checkpoint: exact accepted original P13.1 review and clarified standalone paper, four original closures and P13.2 successor. Checkpoint77 retains its historical three-closure snapshot.'
for front,data in [('active-work.json',a),('checklist-current.json',c)]:write(R/front,data)
lines=['ID\tClosure\tResearch\tReviewed_papers\tTitle']
for target in c['targets']:
    fields=[target['id'],target['closure'],target['research_status'],str(len(target['reviewed_papers'])),target['title']]
    lines.append('\t'.join(str(v).replace('\t',' ').replace('\n',' ') for v in fields))
(R/'checklist-current.tsv').write_text('\n'.join(lines)+'\n')
print(json.dumps({'publication':str(D),'pages':pages,'source_sha256':closure['source_sha256'],
      'pdf_sha256':closure['pdf_sha256'],'fully_solved_original_atoms':solved,
      'remaining_open_atoms':38,'historical_reviewed_scoped_papers':40},indent=2))
