from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as Q
from itertools import combinations
import csv,hashlib,json,re,shutil,subprocess

R=Path('/workspace/research');K=R/'root-checks'
C=R/'campaigns/round-210/P05.2-unchanged-arbitrary-reference-independent-native-local-source-audit'
A=C/'artifacts/codex-Dpre3U'
B=R/'campaigns/round-206/P05.2-original-classification-after-all-continuous-graph-and-arbitrary-reference-route/artifacts/codex-Go7KPX'
D=K/'public-P05.2-continuation272-arbitrary-real-reference-completion-and-flat-jet-contact'
S=K/'round210-root-reproduction-LOCALONLY';E=D/'evidence/independent-local-audit210'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
digest=lambda b:hashlib.sha256(b).hexdigest()
load=lambda p:json.loads(Path(p).read_text())
write=lambda p,d:Path(p).write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
x=load(K/'round210-settled-inspection-LOCALONLY.json');assert x['campaign']['status']=='completed' and x['campaign']['error'] is None
registered=x['campaign']['result'];assert registered['kind']=='notes' and registered['candidate'] is False
req=next(z['data']['payload'] for z in x['records'] if z['kind']=='xean.call.request')
msg=next(z['data']['message'] for z in x['records'] if z['kind']=='xean.call.settled')
assert msg['exitCode']==0 and not msg['failed'] and not msg['isCanceled']
finals=[]
for line in msg['stdout'].splitlines():
    z=json.loads(line)
    if z.get('type')=='item.completed' and z.get('item',{}).get('type')=='agent_message':
        try:n=json.loads(z['item']['text'])
        except (ValueError,TypeError):continue
        if isinstance(n,dict) and set(n)=={'notes','candidate'}:finals.append(n)
assert len(finals)==1;n=finals[0];assert len(n['notes'])==3 and n['candidate'] is False
saved=load(A/'native-notes.json');assert saved!=n
ids=set();note_differences=[]
for p,q,sv in zip(n['notes'],registered['notes'],saved['notes']):
    assert all(v in ids for v in p['support']);ids.add(p['id'])
    assert {k:v for k,v in p.items() if k!='text'}=={k:v for k,v in q.items() if k!='text'}
    assert q['text']==p['text']+'\n\nArtifacts: '+str(A)
    note_differences.append(dict(id=p['id'],different_saved_fields=[k for k in p if p[k]!=sv.get(k)],exact_FINAL_text_length=len(p['text']),saved_text_length=len(sv['text']),saved_draft_used_as_mathematical_grant=False))
inp=load(C/'input.json');prompt=json.loads(req['prompt'])
assert all(prompt[k]==inp[k] for k in ('task','notes','assignment'))
assert {k:v for k,v in prompt.items() if k!='workspace'}==load(A/'input.json')==inp and prompt['workspace']==str(A)
assert (req['model'],req['reasoning'],req['sandbox'],req['shell'],req['webSearch'])==('gpt-6.1-sol','xhigh','workspace-write',True,'disabled')
f=load(C/'freeze.json')
for name,key in [('task.json','task_sha256'),('original-task.json','original_task_sha256'),('input.json','input_sha256'),('settings.json','settings_sha256')]:assert sha(C/name)==f[key]
argument=(C/'unchanged-whole-mathematical-argument.md').read_text()
assert sha(C/'unchanged-whole-mathematical-argument.md')==f['unchanged_review_argument_sha256']==f['original_review_argument_sha256']
units=load(C/'unchanged-mathematical-data-bindings.json');assert len(units)==30
for e in units:
    assert sha(e['source'])==e['sha256'] and Path(e['source']).stat().st_size==e['bytes']
    lo,hi=e['argument_inclusive_lf'];assert argument.splitlines()[lo-1:hi]==Path(e['source']).read_text().splitlines()
blocks=[(m[1],m[2]) for m in re.finditer(r'^BEGIN COMPLETE BODY (.*?)\n(.*?)^END COMPLETE BODY \1$',inp['assignment'],re.M|re.S)]
assert len(blocks)==30
binds=load(A/'frozen-file-bindings.json');report=load(A/'audit-report.json');apps=load(A/'source-application-audit.json')
assert report['verdict']=='INCONCLUSIVE' and report['mathematical_sector_verdict'].startswith('PASS') and not report['candidate'] and not report['canonical_acceptance'] and not report['original_closed']
assert report['all_30_body_bindings']==binds['body_bindings']
for e,(label,text) in zip(binds['body_bindings'],blocks):
    assert e['name']==label and e['sha256']==digest(text.encode()) and e['utf8_bytes']==len(text.encode())
assert binds['grant_names']==['A224','B225','R230','S262']
originals=load(C/'private-primary-packet-bindings.json');assert len(originals)==4;by={e['path']:e for e in originals}
for e in originals:assert sha(e['path'])==e['sha256'] and Path(e['path']).stat().st_size==e['bytes']
assert report['premises']==apps['premises'] and len(report['premises'])==12
assert len(report['unit_checks'])==13 and [p['number'] for p in report['unit_checks']]==list(range(1,14)) and all(p['status']=='PASS' for p in report['unit_checks'])
assert len(report['unnumbered_checks'])==32 and len(report['final_note_checks'])==5
assert len(report['display_equation_check_index'])==22 and len(report['paragraph_and_display_coverage_index'])==67
assert not apps['unresolved_essential_mathematical_premises']
quotes=load(A/'source-quotations-LOCALONLY.json');assert quotes['premises']==report['premises'] and len(quotes['passages'])==len(apps['applications'])==22
coverage=set();primary_units=[]
for p,q in zip(quotes['passages'],apps['applications']):
    assert {k:v for k,v in p.items() if k not in ['quote','quote_sha256','LOCALONLY','independent_original_read']}==q
    i=p['premise'];assert 0<=i<12 and p['statement']==report['premises'][i];coverage.add(i)
    assert p['path'] in by and sha(p['path'])==p['sha256']==by[p['path']]['sha256']
    assert p['PDF_path'] in by and sha(p['PDF_path'])==p['PDF_sha256']==by[p['PDF_path']]['sha256']
    text=Path(p['path']).read_text();lo,hi=p['character_range'];assert p['quote']==text[lo:hi] and p['quote_sha256']==digest(p['quote'].encode())
    lf_start=text[:lo].count('\n')+1;lf_end=text[:hi-1].count('\n')+1
    assert p['LF_range']==[lf_start,lf_end]
    primary_units.append(dict(id=p['id'],premise=i,original_url=p['originalURL'],version=p['version'],path=p['path'],sha256=p['sha256'],LF_range=p['LF_range'],character_range=p['character_range'],whole_unit=p['unit'],actual_application=p['actual_application']))
assert coverage==set(range(12))
manifest=load(A/'audit-artifact-hashes.json');assert len(manifest['artifacts'])==14
for e in manifest['artifacts']:assert sha(A/e['file'])==e['sha256'] and (A/e['file']).stat().st_size==e['bytes']
assert report['independent_finite_result']==load(A/'audit-finite-output.json')
repro=load(D/'root-reproduction-binding-20261007.json');visual=load(D/'root-visual-and-builtin-request-scope-addendum-20261007.json')
for k in ['whole1016_tex_root_read','whole290_argument_separately_root_read','whole47_ledger_root_read','whole13_material_changes_root_read','whole_five_exact_final_notes_root_read','own_finite_checker_reproduced','whole_pandoc_tex_to_markdown_and_normalization_reproduced','all73_native_artifact_hashes_valid']:assert repro[k]
assert repro['root_local_build_exit_codes']==[0,0] and not repro['root_local_warnings']
assert sha(D/'P05.2-paper.tex')==repro['source_sha256']=='c2d53239c96a751dc62c5e3c35a7b5828d99e1a6fe8336bdfc157ec9577d1f70'
assert sha(D/'argument.md')==repro['argument_sha256'] and sha(D/'P05.2-paper.pdf')==repro['root_pdf_sha256']
assert visual['root_actual_visual_read_pages']==[1,8,9,14] and not visual['all_pdf_pages_visually_read']
oldmanifest=load(B/'evidence/artifact-manifest.json');assert len(oldmanifest)==73
for e in oldmanifest:assert sha(B/e['path'])==e['sha256'] and (B/e['path']).stat().st_size==e['bytes']
assert (D/'evidence/certificate-output.json').read_bytes()==(B/'evidence/certificate-output.json').read_bytes()
assert sha(D/'check_certificates.py')==sha(B/'check_certificates.py') and sha(D/'certificate-input.json')==sha(B/'certificate-input.json')
data=load(D/'certificate-input.json');es=[(1,0,0),(0,1,0),(0,0,1),(-1,-1,-1)];pairs=list(combinations(range(4),2));sample_cases=[]
for i,j in pairs:
    for a in data['collar_coordinates']:
        for b in data['collar_coordinates']:
            xyz=tuple(Q(a)*es[i][k]+Q(b)*es[j][k] for k in range(3));rho=max(map(abs,xyz))
            if Q(1,8)<=rho<Q(1,4):
                hv=max(Q(a),Q(b));ev=abs(Q(a)-Q(b)) if (i,j) in [(0,1),(2,3)] else hv
                assert hv<=2*rho and ev<=2*rho and Q(1,512)+Q(1,64)*ev<Q(1,16)*rho
                sample_cases.append(dict(coarse_cone=[i+1,j+1],a=a,b=b,point=[str(z) for z in xyz]))
assert len(sample_cases)==load(D/'evidence/certificate-output.json')['U34']['collar_cases']==291
assert sha(K/'public-P16-round-46-final-reader/P16.4-paper.tex')=='09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
for name in ['active-work.json','checklist-current.json']:
    j=load(R/name);assert len(j['fully_solved_original_atoms'])==9 and j['remaining_open_original_atoms']==33 and j['historical_reviewed_scoped_papers']==79 and j['github_pending_checkpoint'] is None
binding=K/'P05.2-round210-whole-local-source-audit-INCONCLUSIVE-and-ROOT-mathematical-binding-20261007.json'
accept=D/'whole-mathematical-paper-acceptance-after-audit210-20261007.json'
clar=D/'harmless-reader-clarifications-after-audit210-20261007.json'
assert not any(p.exists() for p in [S,E,binding,accept,clar])
S.mkdir();shutil.copyfile(A/'audit_finite.py',S/'audit_finite.py')
check=subprocess.run(['python','audit_finite.py'],cwd=S,capture_output=True,text=True);assert check.returncode==0,check.stderr
assert load(S/'audit-finite-output.json')==report['independent_finite_result']
pixels=[]
for command in manifest['render_commands']:
    result=subprocess.run(command,cwd=S,capture_output=True,text=True);assert result.returncode==0,result.stderr
    p=S/(command[-1]+'.png');assert sha(p)==sha(A/p.name)
    pixels.append(dict(file=p.name,sha256=sha(p),original_path=command[-2],original_sha256=sha(command[-2]),PDF_page=int(command[2]),LOCALONLY=True))
for e in manifest['artifacts']:assert sha(A/e['file'])==e['sha256']
E.mkdir(parents=True)
for name in ['audit-report.json','source-application-audit.json','frozen-file-bindings.json','audit-artifact-hashes.json','audit-analysis.json','audit_finite.py','audit-finite-output.json','audit-read-log.jsonl','audit-execution.json']:shutil.copyfile(A/name,E/name)
shutil.copyfile(S/'audit-finite-output.json',E/'root-reproduced-finite-output.json')
(E/'root-checker.stdout.txt').write_text(check.stdout);(E/'root-checker.stderr.txt').write_text(check.stderr)
write(E/'root-reconstructed-historical291-labelled-collar-cases.json',dict(cases=sample_cases,count=291,distinct_spatial_points_claimed=False,generated_from_actual_bound_original_program_and_input=True,not_a_continuum_proof=True))
native=K/'P05.2-round210-exact-native-model-final-independent-local-INCONCLUSIVE-audit-20261007.json'
canonical=K/'P05.2-round210-actual-registered-native-worker-independent-local-INCONCLUSIVE-audit-20261007.json'
assert not native.exists() and not canonical.exists();write(native,n);write(canonical,registered)
now=datetime.now(timezone.utc).isoformat()
scope=('ENTIRE continuation272 mathematical sector, all13 numbered results and unnumbered proofs: all-face rational coefficient cone; exact rational positive reference component and DISTINCT positive convex decomposition of actual real reference; genuine actual-reference raw mixed completion, exact mass/height bounds for EVERYcompleted fixed-Ctuple, global vague uniformity and ordinary weak/net continuity, weak/BL uniformity ONLY eachfixedC; arbitrary-reference common rational-summand gluing of flat positive-mass jets; necessary/sufficient contact criterion ONLY in finite-PA measured sector, quantified over EVERYrationalpoint and EVERYfinite rational starrefinement; correct plane/U34 raw constants and stated conditional contact stability. Exactly FOURwhole A224/B225/R230/S262 grants with ALLclarifications. No ALLcontinuousPC domain membership, nonPA contact sufficiency or complete structural classification is imported.')
gaps='Original P05.2 remains OPEN: higher-dimensional ALL-obstacle regularization/domain membership, contact sufficiency for nonPA endpoints, and complete structural treatment of all rational refinements. Historical execution observations are not mathematical grants; native210 overall whole-evidence INCONCLUSIVE is preserved.'
bound=dict(recorded_utc=now,round=210,continuation=272,atom='P05.2',native_whole_evidence_verdict='INCONCLUSIVE',native_mathematical_sector_verdict=report['mathematical_sector_verdict'],ROOT_mathematical_verdict='PASS after whole proof/source/application review and independent binding/reproduction',canonical_xean_review_role=False,automatic_acceptance=False,operation_id=req['operationId'],model=req['model'],reasoning=req['reasoning'],native_final=str(native),native_final_sha256=sha(native),registered_native_notes=str(canonical),registered_native_notes_sha256=sha(canonical),registered_notes_match_exact_final_except_artifact_suffix=True,all_three_exact_native_final_notes_root_read=True,saved_draft_notes_differ_and_not_substituted=note_differences,exact_decoded_native_task_assignment_equal_frozen_inputs=True,all30_whole_body_bindings_verified=True,all4_entire_grants_and_all_clarifications_bound=True,all4_immutable_primary_bindings_verified=True,all14_own_artifact_hashes_verified_unchanged=True,whole_report13_proof_units32_unnumbered_checks5_final_note_checks12_premises22_applications_and22_equation_checks_root_read=True,all22_long_original_unit_quotes_exact_character_and_literalLF_bindings=True,actual_source_units=primary_units,root_original_pixel_pages_actually_read_and_rerendered=pixels,root_reproduced_independent_exact_finite_checker=True,finite_checks_not_continuum_certification=True,native_unresolved_evidence_preserved=report['unresolved_evidence'],ROOT_additional_evidence=dict(actual_original73_artifact_byte_bindings_verified=True,actual_original_checker_and_input_present_and_exactly_bound=True,actual_291_labelled_cases_reconstructed_and_inequalities_checked=True,previous_root_whole_original_checker_reproduction_output_matches_author=True,previous_root_full_conversion_normalization_and_two_clean_builds_reproduced=True,historical_execution_flags_not_relabelled_as_independent_native_certification=True),source_or_report_note_emitters_executed=False,long_originals_quotes_and_pixels_remain_LOCALONLY=True,whole1016_tex290_argument47_ledger13_material_changes_and5_author_FINAL_root_read=True,root_recursive_foundations_not_all_freshly_reconstructed=True,recursive_scope_boundaries=apps['unresolved_recursive_foundations'],source_preserved=True,whole_mathematical_sector_accepted=True,whole_historical_evidence_PASS_claimed=False,original_closed=False,accepted_scope=scope,residual_original_scope=gaps,no_active_private_outputs_read=True,no_hot_feedback=True,protected_editor_unchanged_open=True)
write(binding,bound)
a=dict(recorded_utc=now,atom='P05.2',continuation=272,grant_label='S272',independent_native_audit_round=210,native_whole_evidence_verdict='INCONCLUSIVE',ROOT_mathematical_verdict='PASS',acceptance_basis='Whole ROOT mathematical audit plus independently bound native local-source reconstruction and ROOT finite/historical-artifact reproduction; no native verdict relabeling',canonical_xean_review_role=False,automatic_acceptance=False,cumulative_accepted_paper_number=80,source=str(D/'P05.2-paper.tex'),source_sha256=sha(D/'P05.2-paper.tex'),source_lf_lines=1016,argument=str(D/'argument.md'),argument_sha256=sha(D/'argument.md'),pdf=str(D/'P05.2-paper.pdf'),pdf_sha256=sha(D/'P05.2-paper.pdf'),pdf_pages=14,review_binding=str(binding),review_binding_sha256=sha(binding),accepted_scope=scope,only_caller_grants=['A224','B225','R230','S262'],all_clarifications_retained=True,exact_reviewed_source_preserved=True,whole_mathematical_source_argument_ledger_material_five_author_and_three_auditor_exact_notes_root_read=True,local_build_exit_codes=[0,0],local_warnings=[],builtin_compiler_success_claimed=False,builtin_request_tracking_addendum=str(D/'builtin-request-tracking-addendum-after-environment-transition-20261007.json'),root_visual_pages_read=[1,8,9,14],all_pdf_pages_visually_root_read=False,originals_solved=9,originals_open=33,original_closed=False,residual_original_scope=gaps,protected_editor_unchanged_open=True)
write(accept,a)
write(clar,dict(recorded_utc=now,source_sha256=a['source_sha256'],exact_reviewed_source_preserved=True,substantial_mathematical_repair=False,clarifications=report['harmless_clarifications']+['Historical291 count is labelled cone/coordinate cases; distinct spatial points are not claimed.','All old/native execution/hash observations remain DATA. Native210 overall evidence INCONCLUSIVE is preserved; only the whole mathematical sector is accepted after ROOT audit.'],all_prior_caller_clarifications_preserved=True,all_obstacle_domain_membership_and_nonPA_contact_sufficiency_remain_open=True))
for name in ['active-work.json','checklist-current.json']:
    p=R/name;j=load(p);j.update(updated_utc=now,historical_reviewed_scoped_papers=80,P05_2_accepted_arbitrary_reference_mathematics_after210=a,goal_state='9/42 original problems solved;33 open;80 cumulative accepted scoped/supporting mathematical papers. S269 all-genus curves and S272 arbitrary-reference mixed completion/finitePA contact are accepted; both general originals remain open.',next_work='Continue original211 general higherdim P16.4. Start originalP05.2 full all-obstacle/domain/contact/structural classification with FIVEwhole A/B/R/S262/S272 grants and ALLclarifications; ROOT276/277/278 are working data to prove, not new grants. At most two61xhigh campaigns and regular verified pushes.')
    j['P05_2_local_audit210_scope'].update(ROOT_binding_in_progress=False,ROOT_mathematical_sector_accepted=True,new_accepted_scoped_paper_number=80,native_whole_evidence_verdict_preserved='INCONCLUSIVE',original_closed=False)
    if name=='checklist-current.json':
        for target in j['targets']:
            if target['id']=='P05.2':
                assert not target['fully_solved'] and target['closure']=='open'
                target.update(research_status='arbitrary_real_reference_completion_and_finitePA_contact_accepted_full_classification_open',current_focus='Whole mathematical272 accepted by ROOT after complete local-source210 reconstruction/binding; nativewholeevidence INCONCLUSIVE retained. Higherdim all-obstacle/nonPA/fullstructural classification OPEN.')
    write(p,j)
table=R/'checklist-current.tsv'
with table.open(newline='') as fh:reader=csv.DictReader(fh,delimiter='\t');columns=reader.fieldnames;rows=list(reader)
for row in rows:
    if row['ID']=='P05.2':row['Research']='arbitrary_real_reference_completion_and_finitePA_contact_accepted_full_classification_open'
with table.open('w',newline='') as fh:writer=csv.DictWriter(fh,fieldnames=columns,delimiter='\t',lineterminator='\n');writer.writeheader();writer.writerows(rows)
print(json.dumps(dict(accepted_mathematical_supporting_paper=80,native_whole_evidence_verdict='INCONCLUSIVE',ROOT_mathematical_verdict='PASS',acceptance_sha256=sha(accept),review_binding_sha256=sha(binding),originals_solved=9,originals_open=33,independent_finite_exit=check.returncode,actual_historical_labelled_collar_cases=291),indent=2))
