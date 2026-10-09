from pathlib import Path
from datetime import datetime,timezone
import ast,hashlib,json,shutil
R=Path('/workspace/research');K=R/'root-checks'
C=R/'campaigns/round-286/P12.3-whole410-general-excellent-envelope-residual'
A=C/'artifacts/codex-lgLyRK'
D=K/'public-P12.3-continuation413-algebraic-field-and-Frobenius-root-envelope-descent-unreviewed'
OLD=K/'public-P12.3-continuation410-finite-smooth-quotient-continuous-envelopes-unreviewed'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
load=lambda p:json.loads(Path(p).read_text())
write=lambda p,x:Path(p).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
assert not D.exists()
rawpath=K/'round286-raw-native-actual-FINAL.json'
assert sha(rawpath)=='8dc923d36fd115d795aab12bf1221a79ddf18307fe8acd3ef07766f39e31a585'
raw=load(rawpath);notes=load(A/'notes.json');incoming=load(C/'input.json')
assert raw==notes and raw['candidate'] is False and len(raw['notes'])==5
assert incoming==load(A/'input.json') and [n['id'] for n in incoming['notes']]==['G331']
known={'G331'};pairs=[]
for n in raw['notes']:
    assert set(n)=={'id','summary','detailedSummary','text','support'} and set(n['support'])<=known
    assert n['text']==(A/(n['id']+'.txt')).read_text()
    known.add(n['id']);p=A/(n['id']+'.tex')
    pairs.append(dict(id=n['id'],all_five_actual_fields_ROOT_physically_read=True,distinct_entire_expanded_TeX_ROOT_physically_read=True,expanded_bytes=p.stat().st_size,expanded_sha256=sha(p),actual_and_expanded_NOT_claimed_identical=True))
task=incoming['task'];assert task==load(A/'original-task.json')
assert task['problem']==(A/'original-problem.txt').read_text() and task['completionCriteria']==(A/'original-completion-criteria.txt').read_text()
grant=incoming['notes'][0]['text'];assert grant==(A/'retained/G331-qualified.txt').read_text()
assert grant==load(R/'campaigns/round-284/P12.3-whole408-canonical-filtration-and-general-envelope-residual/input.json')['notes'][0]['text']
assert len(grant.encode())==93375
for a,b in [('000-P12.3-quotient-envelopes.tex','P12.3-quotient-envelopes.tex'),('015-proof-companion.md','proof-companion.md'),('014-original-residual.md','original-residual.md')]:
    assert (A/'retained'/a).read_bytes()==(OLD/b).read_bytes()
assert (A/'original-residual.md').read_bytes()==(OLD/'original-residual.md').read_bytes()
# Native programs are inert DATA. Inspect only one literal preamble; never execute/import them.
values=[]
for node in ast.walk(ast.parse((A/'assemble_delivery.py').read_text())):
    if isinstance(node,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='preamble' for t in node.targets):
        assert isinstance(node.value,ast.Constant) and isinstance(node.value.value,str);values.append(node.value.value)
assert len(values)==1
escape={'\\':r'\textbackslash{}','{':r'\{','}':r'\}','#':r'\#','$':r'\$','%':r'\%','&':r'\&','_':r'\_','^':r'\textasciicircum{}','~':r'\textasciitilde{}','<':r'\textless{}','>':r'\textgreater{}'}
def tex(s):return ''.join(escape.get(c,c) for c in s)
sections=[(A/f'n{i}.tex').read_text() for i in range(1,6)]
paper=values[0]+'\n'.join(sections)
for name,title in [('source-application-reading-ledger.md','Exact source, application and reading ledger'),('scoped-verdict.md','Separate scoped verdict'),('original-residual.md','Byte-unchanged incoming original residual')]:
    paper+='\n\\section*{'+title+'}\n'+'\n\n'.join(tex(p) for p in (A/name).read_text().split('\n\n'))+'\n'
assert '\\end{QualifiedGrantDATA}' not in grant
paper+='\n\\section*{ENTIRE qualified G331, with every source and scope annotation}\n\\begin{QualifiedGrantDATA}\n'+grant+'\n\\end{QualifiedGrantDATA}\n'
paper+='\n\\section*{Exact unchanged original task DATA}\n\\begin{QualifiedGrantDATA}\n'+json.dumps(task,ensure_ascii=True,indent=2)+'\n\\end{QualifiedGrantDATA}\n\\end{document}\n'
assert paper==(A/'P12.3-algebraic-descent-envelopes.tex').read_text()
companion='# ENTIRE proof companion; actual notes and expanded expositions are separate\n\n'
for note,expansion in zip(raw['notes'],sections):
    companion+='## Actual five-field note '+note['id']+'\n\n'+json.dumps(note,ensure_ascii=False,indent=2)+'\n\n'
    companion+='## ENTIRE distinct expanded TeX '+note['id']+'\n\n'+expansion+'\n'
for name in ['source-application-reading-ledger.md','scoped-verdict.md','original-residual.md','retained/G331-qualified.txt','original-task.json','original-problem.txt','original-completion-criteria.txt']:
    companion+='\n## ENTIRE '+name+'\n\n'+(A/name).read_text()+'\n'
for name in ['013-notes.json','016-raw-native-actual-FINAL.json','005-final-n1.txt','006-final-n2.txt','007-final-n3.txt','008-final-n4.txt','009-n1.tex','010-n2.tex','011-n3.tex','012-n4.tex','018-source-application-reading-ledger.md','017-scoped-verdict.md','014-original-residual.md','000-P12.3-quotient-envelopes.tex','015-proof-companion.md']:
    companion+='\n## ENTIRE retained current DATA '+name+'; retention is not inherited reading\n\n'+(A/'retained'/name).read_text()+'\n'
assert companion==(A/'proof-companion.md').read_text()
cap=load(K/'round286-terminal-actual-final-ROOT-retention-20261009.json')
assert cap['public_status']['status']=='completed' and cap['public_status']['calls']['unsettled']==0 and cap['campaign_result']['candidate'] is False
tails=[]
for n,c in zip(raw['notes'],cap['campaign_result']['notes']):
    assert all(n[k]==c[k] for k in ['id','summary','detailedSummary','support']) and c['text'].startswith(n['text']);tails.append(dict(id=n['id'],tail=c['text'][len(n['text']):]))
for name in ['active-work.json','checklist-current.json']:
    x=load(R/name);assert x['current_active_batch']==[287] and x['github_pending_checkpoint'] is None and x['latest_verified_github_checkpoint']['continuation']==296
    assert len(x['fully_solved_original_atoms'])==16 and x['remaining_open_original_atoms']==26 and x['historical_reviewed_scoped_papers']==97
assert sha(K/'public-P16-round-46-final-reader/P16.4-paper.tex')=='09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
U=R/'primary-data-LOCALONLY/P12.3-ROOT413-algebraic-field-root-descent-source-20261009';assert not U.exists();U.mkdir()
primary=[]
for p in [R/'primary-data-LOCALONLY/P12.3-ROOT408-integral-closure-criterion-source-20261009'/n for n in ['SH-1.1.5-whole-statement-and-proof.txt','SH-6.8.1-4-whole-statements-and-proofs.txt']]+sorted((R/'primary-data-LOCALONLY/P12.3-ROOT410-smooth-envelope-estimate-source-20261009').glob('BFJ-*.txt')):
    q=U/p.name;shutil.copyfile(p,q);assert sha(p)==sha(q)
    primary.append(dict(path=str(q),bytes=q.stat().st_size,sha256=sha(q),ROOT_fresh_immediate_unit_physically_read=True,partial_neighbor_units_not_applied=True,LOCALONLY=True))
assert len(primary)==8
pixels=[]
for number in [153,154]:
    p=A/f'LOCALONLY/SH-formula-{number}.png';q=U/p.name;shutil.copyfile(p,q)
    pixels.append(dict(path=str(q),bytes=q.stat().st_size,sha256=sha(q),ROOT_actual_formula_pixels_viewed=True,LOCALONLY=True))
programs=[A/n for n in ['audit_data.py','assemble_delivery.py','check_delivery.py','finite_checks.py']]
now=datetime.now(timezone.utc).isoformat();D.mkdir()
for name in ['P12.3-algebraic-descent-envelopes.tex','proof-companion.md','notes.json','source-application-reading-ledger.md','scoped-verdict.md','original-residual.md']:
    shutil.copyfile(A/name,D/name)
for i in range(1,6):
    for suffix in ['.txt','.tex']:shutil.copyfile(A/f'n{i}{suffix}',D/f'n{i}{suffix}')
shutil.copyfile(rawpath,D/'raw-native-actual-FINAL.json')
shutil.copyfile(K/'round286-terminal-actual-final-ROOT-retention-20261009.json',D/'terminal-actual-FINAL-retention.json')
audit=dict(recorded_utc=now,paper=413,round=286,UNREVIEWED=True,accepted=False,original_closed=False,actual_expanded_pairs=pairs,all_unique_current_proofs_preamble_ledger_verdict_residual_ROOT_physically_read=True,whole_standalone_and_companion_component_identity_verified=True,repeated_retention_not_an_extra_independent_historical_audit=True,incoming_correctness_grants=['ENTIRE qualified G331 with all annotations unchanged; reused qualified grant not a new independent whole recursive audit'],ROOT_fresh_primary_units=primary,ROOT_actual_formula_pixels=pixels,native_programs_physically_read_only_as_DATA=[dict(path=str(p),bytes=p.stat().st_size,sha256=sha(p)) for p in programs],native_or_supplied_programs_executed_or_imported=False,terminal_tails=tails,new_complete_scoped_proofs=['All-support separable coefficient-field inverse-limit boundary and full profinite orbits','Trace-dual coefficient extraction proves actual invariant primary ideal descent without dividing by group order','Every canonical degree and raw compatible envelope commute with the separable coefficient extension; uniform bounds and FG equivalence retain exact scope','Geometric finite smooth quotients at rational points over ANY characteristic-zero field have every continuous signed envelope, using BFJ only over algebraic closure','Finite S^q subset R and specified Noetherian infinite-root extensions identify every semivaluation, rational primary profile, C/D cone and all-obstacle envelope','Geometrically normal/integral rational-point finite-type imperfect-field perfection reduces CE to its perfect/algebraic closure; positive-characteristic source CE remains conditional'],named_deeper_foundations_not_recursively_reproved=['Qualified G331 geometric model and full-support trace foundations','Excellent/Nagata finite normalization, ideal-integrality background named in complete SH immediate units','Smooth characteristic-zero Hironaka/multiplier-subadditivity/Izumi/thinness foundations named in the complete applied BFJ units','Separable Galois extension/profinite compactness and ordinary faithful-flat Noetherian finite-type ring foundations at the explicit geometric rational-point hypotheses'],unresolved=['Arbitrary normal nonisolated excellent germs beyond geometric finite smooth quotients','General positive-characteristic CE source theorem and mixed-characteristic higher-dimensional envelopes','A qualifying normal continuous-obstacle failure or unrestricted conductor envelope commutation','Fresh complete inherited historical405/401/392/B341/E350 recursive source audit'],compiler_pending=True,primary_bodies_pixels_books_LOCALONLY=True,counts=dict(solved=16,open=26,accepted_scoped_papers=97),protected_editor_OPEN_UNCHANGED=True)
write(D/'ROOT-whole-serialization-source-application-and-scope-audit.json',audit)
(D/'ROOT-review-scope.txt').write_text('Whole working paper413 UNREVIEWED, original P12.3 OPEN. All five actual notes including every field and all five distinct expanded TeX proofs, entire unique ledger/verdict/residual and preamble were ROOT physically read. Whole formal and companion components reconstruct exactly; duplicated grant/history retention is not a new independent recursive historical audit. All four native programs physically read only as DATA, never executed/imported. Complete immediate SH/BFJ units and actual SH formula pixels were ROOT read/viewed with partial unused neighboring units excluded; named deeper foundations retain their stated limits.\n\nNew complete scoped proofs give exact EVERY-degree separable coefficient-field canonical descent, full profinite fibre orbits, and every continuous signed envelope on geometric finite smooth quotient rational-point germs over ANY characteristic-zero field. Frobenius-root maps preserve ALL semivaluations, actual primary positivity, C/D and raw envelopes for all obstacles at the explicit finite or Noetherian infinite-root hypotheses. Positive-characteristic source CE remains conditional; mixed characteristic and arbitrary excellent normal singularities beyond the source class OPEN. Counts16solved26OPEN97accepted unchanged. Compiler pending. Primary bodies/pixels/books LOCALONLY; protected P16.4 editor OPEN UNCHANGED.\n')
B=D/'ROOT-whole-proof-source-scope-and-binding.json'
write(B,dict(recorded_utc=now,paper=413,round=286,whole_paper=dict(path=str(D/'P12.3-algebraic-descent-envelopes.tex'),bytes=len(paper.encode()),sha256=sha(D/'P12.3-algebraic-descent-envelopes.tex')),public_files=[dict(path=str(p),bytes=p.stat().st_size,sha256=sha(p)) for p in sorted(D.iterdir()) if p.is_file()],UNREVIEWED=True,accepted=False,original_closed=False,compiler=dict(kind='pending'),counts=audit['counts'],primary_bodies_not_published=True,protected_editor_OPEN_UNCHANGED=True))
for name in ['active-work.json','checklist-current.json']:
    p=R/name;x=load(p);x.update(updated_utc=now,native286_whole_unreviewed_paper413=dict(directory=str(D),binding=str(B),sha256=sha(B)),next_work='Compile whole413 P12.3 field/root descent, freeze288 unchanged original general envelope residual with whole413 and sole qualified G331. Native287 continues universal P16.7 variational representation/existence. Verify regular NONFORCE297; at mostTWO, no hot feedback; counts/editor unchanged.');write(p,x)
print(json.dumps(dict(paper=413,directory=str(D),whole_source_bytes=len(paper.encode()),whole_source_sha256=sha(D/'P12.3-algebraic-descent-envelopes.tex'),whole_companion_bytes=len(companion.encode()),fresh_primary_units=len(primary),formula_pixels=len(pixels),terminal_tails=tails,compiler='pending',original_closed=False),indent=2))
