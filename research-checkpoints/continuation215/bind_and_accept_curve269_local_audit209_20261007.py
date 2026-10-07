from pathlib import Path
from datetime import datetime, timezone
import csv, hashlib, json, re, shutil, subprocess

R = Path('/workspace/research'); K = R/'root-checks'
C = R/'campaigns/round-209/P16.4-unchanged-all-genus-curve-independent-native-local-source-audit'
A = C/'artifacts/codex-yYuVeX'
D = K/'public-P16.4-continuation269-all-genus-original-field-curve-equation'
S = K/'round209-root-reproduction-LOCALONLY'
E = D/'evidence/independent-local-audit209'
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
digest = lambda b: hashlib.sha256(b).hexdigest()
load = lambda p: json.loads(Path(p).read_text())
write = lambda p, d: Path(p).write_text(json.dumps(d, ensure_ascii=False, indent=2)+'\n')

x = load(K/'round209-settled-inspection-LOCALONLY.json')
assert x['campaign']['status']=='completed' and x['campaign']['error'] is None
registered = x['campaign']['result']
assert registered['kind']=='notes' and registered['candidate'] is False
req = next(z['data']['payload'] for z in x['records'] if z['kind']=='xean.call.request')
msg = next(z['data']['message'] for z in x['records'] if z['kind']=='xean.call.settled')
assert msg['exitCode']==0 and not msg['failed'] and not msg['isCanceled']
finals=[]
for line in msg['stdout'].splitlines():
    z=json.loads(line)
    if z.get('type')=='item.completed' and z.get('item',{}).get('type')=='agent_message':
        try: n=json.loads(z['item']['text'])
        except (ValueError, TypeError): continue
        if isinstance(n,dict) and set(n)=={'notes','candidate'}: finals.append(n)
assert len(finals)==1
n=finals[0]; assert n==load(A/'native-notes.json') and len(n['notes'])==3 and n['candidate'] is False
ids=set()
for p,q in zip(n['notes'],registered['notes']):
    assert all(v in ids for v in p['support']); ids.add(p['id'])
    assert {k:v for k,v in p.items() if k!='text'}=={k:v for k,v in q.items() if k!='text'}
    assert q['text']==p['text']+'\n\nArtifacts: '+str(A)
inp=load(C/'input.json'); prompt=json.loads(req['prompt'])
assert all(prompt[k]==inp[k] for k in ('task','notes','assignment'))
assert {k:v for k,v in prompt.items() if k!='workspace'}==load(A/'input.json')==inp
assert prompt['workspace']==str(A)==req['workspace']
assert (req['model'],req['reasoning'],req['sandbox'],req['shell'],req['webSearch'])==('gpt-6.1-sol','xhigh','workspace-write',True,'disabled')
f=load(C/'freeze.json')
for name,key in [('task.json','task_sha256'),('original-task.json','original_task_sha256'),('input.json','input_sha256'),('settings.json','settings_sha256')]:
    assert sha(C/name)==f[key]
argument=(C/'unchanged-whole-mathematical-argument.md').read_text()
assert sha(C/'unchanged-whole-mathematical-argument.md')==f['unchanged_review_argument_sha256']==f['original_review_argument_sha256']
units=load(C/'unchanged-mathematical-data-bindings.json'); assert len(units)==33
for e in units:
    assert sha(e['source'])==e['sha256'] and Path(e['source']).stat().st_size==e['bytes']
    lo,hi=e['argument_inclusive_lf']; assert argument.splitlines()[lo-1:hi]==Path(e['source']).read_text().splitlines()
blocks={}
for m in re.finditer(r'^BEGIN COMPLETE BODY (.+)\n',inp['assignment'],re.M):
    end=inp['assignment'].index('\nEND COMPLETE BODY '+m[1],m.end()); blocks[m[1]]=inp['assignment'][m.end():end]
b=load(A/'frozen-file-bindings.json'); assert len(b['primary_files'])==62 and len(b['supplied_bodies'])==33
originals=load(C/'private-primary-packet-bindings.json'); bypath={e['path']:e for e in originals}
assert len(bypath)==62
for e in b['primary_files']:
    assert e['path'] in bypath and e['sha256']==bypath[e['path']]['sha256'] and e['bytes']==bypath[e['path']]['bytes']
    assert e['matches'] and sha(e['path'])==e['sha256'] and Path(e['path']).stat().st_size==e['bytes']
for e in b['supplied_bodies']:
    raw=blocks[e['label']].encode(); assert digest(raw)==e['sha256'] and len(raw)==e['bytes']
for e in b['frozen_submission_files']:
    assert sha(e['path'])==e['sha256']==e['after_sha256'] and e['unchanged']
    if e['label']!='five exact native final notes':
        key='WHOLE269 '+e['label']+'; UNREVIEWED NEW MATHEMATICS/DATA'
        assert Path(e['path']).read_bytes().rstrip(b'\n')==blocks[key].encode().rstrip(b'\n')
    else:
        key='WHOLE EXACT DATA '+Path(e['path']).name; assert load(e['path'])==json.loads(blocks[key])
for e in b['before_after_immutable_checks']: assert e['unchanged'] and sha(e['path'])==e['sha256']
report=load(A/'audit-report.json'); apps=load(A/'source-application-audit.json')
assert report['verdict']==apps['verdict']=='PASS' and not report['candidate'] and not report['whole_original_P16_4_solved']
assert report['report']==report['full_quote_free_report'] and n['notes'][1]['text'].startswith(report['report'])
assert report['premises']==report['standalone_external_premises']==apps['premises']
assert len(report['premises'])==26 and [p['index'] for p in report['premises']]==list(range(26))
assert report['accepted_caller_grants']==b['exact_complete_grant_bindings'] and [g['id'] for g in report['accepted_caller_grants']]==list('ODNTQCGM')
for g in report['accepted_caller_grants']:
    for e in g['bodies']:
        raw=blocks[e['label']].encode(); assert len(raw)==e['bytes'] and digest(raw)==e['sha256'] and digest(raw+b'\n')==e['sha256_with_one_terminal_LF']
u={p['id']:p for p in report['per_assertion_and_unnumbered_proof_unit_checks']}; assert len(u)==52
assert list(u)==['U'+str(i).zfill(2) for i in range(52)]
assert [e['equation'] for e in report['equation_coverage']]==list(range(1,27))
for e in report['equation_coverage']: assert e['check_id'] in u and e['status']=='PASS'
pu={p['premise_index']:p for p in apps['independent_primary_units']}; assert len(pu)==26
assert len(apps['applications'])==25
for p in apps['applications']:
    assert p['status']=='PASS' and not p['unresolved_essential_premises'] and p['authored_ledger_not_a_grant']
    assert p['actual_application_hypothesis_and_domain_checks']==[u[k]['independent_check'] for k in p['independently_checked_manuscript_units']]
    assert p['whole_immediate_primary_units']==[pu[k] for k in p['external_premise_indices']]
assert not report['unresolved_essential_premises'] and not report['material_repairs']
quotes=load(A/'source-quotations-LOCALONLY.json'); assert quotes['premises']==report['premises']
coverage=set()
assert len(quotes['passages'])==len(report['passages'])==44
for p,q in zip(quotes['passages'],report['passages']):
    i=p['premise']; coverage.add(i); assert 0<=i<26
    assert p['statement']==report['premises'][i]['statement'] and p['url']==report['premises'][i]['url']
    assert q=={**{k:v for k,v in p.items() if k not in ('quote','transcription')},'quote_LOCALONLY_artifact':'source-quotations-LOCALONLY.json'}
    assert p['path'] in bypath and sha(p['path'])==p['sha256']==bypath[p['path']]['sha256']
    if 'LF_first' in p['location']:
        z=p['location']; assert p['quote']=='\n'.join(Path(p['path']).read_text().split('\n')[z['LF_first']-1:z['LF_last']])
assert coverage==set(range(26))
sourceunits=load(A/'source-units-LOCALONLY.json')['units']; assert len(sourceunits)==35
for e in sourceunits:
    assert e['path'] in bypath and sha(e['path'])==e['sha256']==bypath[e['path']]['sha256']
    assert e['text']=='\n'.join(Path(e['path']).read_text().split('\n')[e['first_LF']-1:e['last_LF']])
for e in pu.values():
    assert e['original_url']==report['premises'][e['premise_index']]['url']
    for z in e['source_files']:
        assert z['path'] in bypath and sha(z['path'])==z['sha256']==bypath[z['path']]['sha256'] and Path(z['path']).stat().st_size==z['bytes']
    for z in e['pixel_evidence_LOCALONLY']: assert sha(z['path'])==z['sha256']
manifest=load(A/'own-artifact-manifest.json'); assert len(manifest['artifacts'])==40
for e in manifest['artifacts']: assert sha(A/e['path'])==e['sha256'] and (A/e['path']).stat().st_size==e['bytes']
repro=load(D/'root-reproduction-binding-20261007.json')
assert repro['whole1105_tex_root_read'] and repro['whole399_argument_separately_root_read'] and repro['whole47_ledger_root_read'] and repro['whole9_scope_root_read'] and repro['whole_five_exact_final_notes_root_read']
assert repro['root_local_build_exit_codes']==[0,0] and not repro['root_local_warnings'] and repro['own_finite_checker_reproduced']
assert sha(D/'P16.4-paper.tex')==repro['source_sha256']=='161e55d2e94807a8248619501e74c932d5f25273250a1c6cbfa66a09cbb83f94'
assert sha(D/'P16.4-paper.pdf')=='c11eb3bce1f2bf43fd526a53ac0a2a1612a4a4deab0511af963c379ff7df23e8'
assert sha(K/'public-P16-round-46-final-reader/P16.4-paper.tex')=='09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
for name in ('active-work.json','checklist-current.json'):
    j=load(R/name); assert len(j['fully_solved_original_atoms'])==9 and j['remaining_open_original_atoms']==33 and j['historical_reviewed_scoped_papers']==78 and j['github_pending_checkpoint'] is None
binding=K/'P16.4-round209-whole-local-source-curve-audit-and-root-binding-20261007.json'
accept=D/'whole-partial-paper-acceptance209-local-source-audit-20261007.json'
clar=D/'harmless-reader-clarifications209-local-source-audit-20261007.json'
assert not any(p.exists() for p in (S,E,binding,accept,clar))
S.mkdir(); shutil.copyfile(A/'audit_checks.py',S/'audit_checks.py')
check=subprocess.run(['python',str(S/'audit_checks.py')],cwd=S,capture_output=True,text=True)
assert check.returncode==0,check.stderr
assert load(S/'independent-finite-checks.json')==load(A/'independent-finite-checks.json')
render_bindings=[]
for line in (A/'independent-reads.jsonl').read_text().splitlines():
    e=json.loads(line)
    if e['kind']!='original_PDF_render': continue
    out=S/Path(e['command'][-1]).name; command=e['command'][:-1]+[str(out)]
    rr=subprocess.run(command,capture_output=True,text=True); assert rr.returncode==0,rr.stderr
    for p in sorted(S.glob(out.name+'*.png')):
        page=int(p.stem.rsplit('-',1)[1])
        if not e['PDF_pages'][0]<=page<=e['PDF_pages'][1]: continue
        original=A/'source-images-LOCALONLY'/p.name
        assert sha(p)==sha(original)
        render_bindings.append(dict(original_pdf=e['path'],original_pdf_sha256=e['sha256'],PDF_pages=e['PDF_pages'],dpi=e['dpi'],image_name=p.name,image_sha256=sha(p),LOCALONLY=True))
assert len({e['image_name'] for e in render_bindings})==18
for e in manifest['artifacts']: assert sha(A/e['path'])==e['sha256']
E.mkdir(parents=True)
for name in ('audit-report.json','source-application-audit.json','frozen-file-bindings.json','own-artifact-manifest.json','independent-finite-checks.json','audit_checks.py','independent-reads.jsonl','independent-review-record.json'):
    shutil.copyfile(A/name,E/name)
shutil.copyfile(S/'independent-finite-checks.json',E/'root-reproduced-finite-checks.json')
(E/'root-checker.stdout.txt').write_text(check.stdout); (E/'root-checker.stderr.txt').write_text(check.stderr)
native=K/'P16.4-round209-exact-native-model-final-independent-local-audit-20261007.json'
canonical=K/'P16.4-round209-actual-registered-native-worker-independent-local-audit-20261007.json'
assert not native.exists() and not canonical.exists(); write(native,n); write(canonical,registered)
now=datetime.now(timezone.utc).isoformat()
scope=('Entire continuation269 curve theorem, ALL genera and ALL original fields: actual original-bundle positive formal pairs; unconditional whole-reduction FS recognition with all-j lifts and same-carrier q0; canonical whole residue field and genuine raw signed/zero CLDv1 curve coefficients; cyclic cofinal finite-graph inverse including nonatomic projected targets and arbitrary support/poles; intrinsic finite-J energy bound and literal FS majorant net BEFORE E1; prescribed-target actual E1 inverse and supporting dual attainment afterward; EVERY E1 solution equal at EVERY analytic point modulo a finite constant; original-field singular invariance BEFORE descent. Raw total deg(L); no probability, factorial or blanket field-degree normalization. Relative to exactly EIGHT complete O/D/N/T/Q/C/G/M grants and ALL clarifications and the independently audited ordinary primary premises.')
gaps=('Original P16.4 remains OPEN for general nontrivially valued n>=2: inverse existence, attained dual and every-solution every-point uniqueness. Curves do not close the all-dimensional original. Complete recursive foundational literature was not freshly reconstructed; disclosed ordinary-source dependency boundaries remain explicit.')
bound=dict(recorded_utc=now,round=209,continuation=269,atom='P16.4',verdict='PASS',review_kind='Independent native Codex worker local-source audit PLUS independent ROOT whole audit/binding/reproduction; NOT canonical Xean research review',canonical_xean_review_role=False,automatic_acceptance=False,operation_id=req['operationId'],model=req['model'],reasoning=req['reasoning'],child_sandbox=req['sandbox'],shell=req['shell'],native_web_search=req['webSearch'],native_final=str(native),native_final_sha256=sha(native),registered_native_notes=str(canonical),registered_native_notes_sha256=sha(canonical),all_three_entire_native_final_notes_root_read=True,registered_notes_equal_exact_final_except_artifact_suffix=True,exact_decoded_native_task_assignment_notes_equal_frozen_input=True,artifact_input_equal_frozen_input=True,frozen_task_sha256=f['task_sha256'],frozen_input_sha256=f['input_sha256'],unchanged_math_argument_sha256=f['unchanged_review_argument_sha256'],all33_entire_math_body_bindings_verified=True,all62_immutable_original_bindings_verified=True,all8_entire_grants_and_all_clarifications_exactly_bound=True,all40_own_artifact_bindings_verified_unchanged=True,whole_report26_premises52_proof_units26_equations25_applications_root_read=True,application_hypothesis_checks_exactly_equal_already_read_whole_units=True,all25_primary_metadata_entries_exactly_equal_canonical_units=True,all44_passage_metadata_valid_bound_zero_based_and_exact_statement=True,all41_text_quotes_exact_original_LF_extractions=True,three_pixel_transcriptions_root_mathematically_checked=True,all35_long_source_units_exact_original_LF_extractions=True,long_sources_and_quotes_and_pixels_remain_LOCALONLY=True,root_independent_rational_graph_checker_reproduced=True,finite_domain_target_tuples=150,attached_tree_pairs=36,finite_checks_not_analytic_certification=True,original_pixels_rerendered_exactly_bound=render_bindings,root_did_not_execute_audit_report_note_or_source_emitters=True,whole_paper_argument_ledger_scope_five_author_notes_root_read=True,root_recursive_foundations_not_all_freshly_read=True,recursive_dependency_boundaries=report['recursive_dependencies_not_all_freshly_reconstructed'],accepted_scope=scope,residual_original_scope=gaps,whole_scoped_paper_accepted=True,new_accepted_scoped_paper=True,original_closed=False,previous207_whole_INCONCLUSIVE_preserved=True,source_unchanged=True,no_active_private_outputs_read=True,no_hot_feedback=True,protected_editor_unchanged_open=True)
write(binding,bound)
a=dict(recorded_utc=now,atom='P16.4',continuation=269,grant_label='S269',independent_review_round=209,verdict='PASS',review_kind=bound['review_kind'],canonical_xean_review_role=False,automatic_acceptance=False,cumulative_accepted_paper_number=79,source=str(D/'P16.4-paper.tex'),source_sha256=sha(D/'P16.4-paper.tex'),source_lf_lines=1105,argument=str(D/'P16.4-argument.md'),argument_sha256=sha(D/'P16.4-argument.md'),pdf=str(D/'P16.4-paper.pdf'),pdf_sha256=sha(D/'P16.4-paper.pdf'),pdf_pages=15,review_binding=str(binding),review_binding_sha256=sha(binding),accepted_scope=scope,only_caller_grants=f['only_mathematical_grants'],all_clarifications_retained=True,whole_source_parallel_argument_ledger_scope_five_exact_notes_root_read=True,whole_independent_report_premises_checks_and_native_notes_root_read=True,local_build_exit_codes=[0,0],local_warnings=[],builtin_compiler_success_claimed=False,builtin_request_tracking_addendum=str(D/'builtin-request-tracking-addendum-after-environment-transition-20261007.json'),root_visual_pages_read=[1,6,9,12,15],all_pdf_pages_visually_root_read=False,fully_solved_original_atoms_count=9,remaining_original_atoms_count=33,original_closed=False,residual_original_scope=gaps,recursive_foundations=report['recursive_dependencies_not_all_freshly_reconstructed'],exact_reviewed_source_preserved=True,protected_editor_unchanged_open=True)
write(accept,a)
write(clar,dict(recorded_utc=now,independent_review_round=209,source_sha256=a['source_sha256'],exact_reviewed_source_preserved=True,substantial_mathematical_repair=False,clarifications=report['harmless_clarifications'],all_previous_caller_clarifications_preserved=True,source_scope_not_enlarged=True))
for name in ('active-work.json','checklist-current.json'):
    p=R/name; j=load(p);j.update(updated_utc=now,historical_reviewed_scoped_papers=79,P16_4_accepted_all_genus_curves209=a,goal_state='9/42 original problems solved;33 open;79 cumulative accepted scoped/supporting papers. All-genus original-field curves accepted after whole independent local-source/ROOT audit; general higher-dimensional P16.4 and higher-dimensional P05.2 classification remain open.',next_work='Continue original P16.4 in nontrivial dimension>=2 with exactly accepted grants including S269 curves. Complete whole210 P05.2 audit when settled. Keep at most two campaigns and regularly verify GitHub pushes.')
    if name=='checklist-current.json':
        for target in j['targets']:
            if target['id']=='P16.4':
                assert not target['fully_solved'] and target['closure']=='open'
                target.update(research_status='all_genus_original_field_curves_accepted_general_higher_dimension_open',current_focus='Whole269 accepted after independent local-source worker209 and ROOT audit. Original nontrivial dimension>=2 equation, attainment and every-point uniqueness remain OPEN.')
    write(p,j)
table=R/'checklist-current.tsv'
with table.open(newline='') as fh: reader=csv.DictReader(fh,delimiter='\t'); columns=reader.fieldnames; rows=list(reader)
for row in rows:
    if row['ID']=='P16.4': row['Research']='all_genus_original_field_curves_accepted_general_higher_dimension_open'
with table.open('w',newline='') as fh: writer=csv.DictWriter(fh,fieldnames=columns,delimiter='\t',lineterminator='\n');writer.writeheader();writer.writerows(rows)
print(json.dumps(dict(accepted_supporting_paper=79,originals_solved=9,originals_open=33,acceptance_record=str(accept),acceptance_sha256=sha(accept),review_binding_sha256=sha(binding),finite_reproduction_exit=check.returncode,unique_original_pixel_bindings=18),indent=2))
