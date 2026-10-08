from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, shutil

R=Path('/workspace/research'); K=R/'root-checks'
C=R/'campaigns/round-267/P16.7-whole373374-nonalgebraization-and-intrinsic-E1'
A=C/'artifacts/codex-XGSLoe'
D=K/'public-P16.7-continuation378-conditional-nonalgebraization-and-divergent-branch-energy-whole-candidate'
P=R/'primary-data-LOCALONLY/P16.7-native267-whole-primary-and-evidence-20261008'
B=K/'P16.7-round267-whole-candidate378-ROOT-proof-source-scope-and-binding-20261008.json'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
load=lambda p:json.loads(Path(p).read_text())
def write(p,x):p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
assert not D.exists() and not P.exists() and not B.exists()
actual=K/'round267-actual-native-final.json'
assert sha(actual)=='c496972c8694f95079f58c0c7d4b04cae784b523b295a8291bbeaea5bcc56665'
j=load(actual); e=load(A/'final-notes.json')
assert not j['candidate'] and not e['candidate'] and len(j['notes'])==len(e['notes'])==5
proof=(A/'proof-companion.md').read_text(); ledger=(A/'source-application-ledger.md').read_text()
assert len(proof)==57732
assert (A/'P16.7-partial-paper.md').read_text()==proof[45:]
assert proof[39989:]==ledger
assert (A/'nonalgebraization-conditional-paper.md').read_text()=='# A conditional constant-meromorphic-field theorem for an analytic torus\n\nUnverified draft. The condition F_L is not discharged.\n\n'+e['notes'][0]['text']+'\n\n'+ledger
comparisons=[]
for x,y in zip(j['notes'],e['notes']):
    assert x['id']==y['id'] and x['text']!=y['text']
    assert y['text'] in proof and (A/f"notes/{y['id']}.md").read_text()==y['text']
    comparisons.append(dict(id=x['id'],actual_text_sha256=hashlib.sha256(x['text'].encode()).hexdigest(),expanded_text_sha256=hashlib.sha256(y['text'].encode()).hexdigest(),actual_DIFFERS_expanded=True,expanded_entire_literal_proof_substring=True,expanded_proof_start_character=proof.index(y['text'])))
assert sha(K/'public-P16-round-46-final-reader/P16.4-paper.tex')=='09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
D.mkdir(); P.mkdir(); shutil.copytree(A/'evidence',P/'native-evidence');shutil.copytree(C/'private-primary-DATA-LOCALONLY',P/'frozen-campaign-private-primary')
for n in ['proof-companion.md','P16.7-partial-paper.md','nonalgebraization-conditional-paper.md','source-application-ledger.md','final-notes.json']:
    shutil.copyfile(A/n,D/n)
shutil.copyfile(actual,D/'actual-settled-native267-FINAL.json');shutil.copyfile(C/'original-task.json',D/'original-task.json')
for n in j['notes']:(D/f"{n['id']}-actual-settled.md").write_text(n['text'])
for n in e['notes']:shutil.copyfile(A/f"notes/{n['id']}.md",D/f"{n['id']}-expanded.md")
for n in ['artifact-bindings.json','build-output.txt','check-output.txt','checks-output.json','commands.json','coverage.json','diagnostics-output.txt','diagnostics.json','environment.json','input-retention-bindings.json','original-verdict.json']:
    shutil.copyfile(A/'evidence'/n,D/n)
Q=D/'native-programs-INERT-DATA';Q.mkdir()
for p in sorted((A/'scripts').glob('*.py')):shutil.copyfile(p,Q/(p.name+'.DATA.txt'))
now=datetime.now(timezone.utc).isoformat()
qual=dict(recorded_utc=now,status='UNREVIEWED complete mathematical draft. No paper acceptance or original closure.',counts=dict(solved=16,open=26,accepted_papers=97),candidate=False,whole_original_solved=False,new_accepted_paper=False,
    actual_FINAL=dict(path=str(actual),sha256=sha(actual),all_five_complete_actual_texts_and_outside_fields_ROOT_physically_read=True,intermediate_messages_excluded=10),
    ROOT_reading=dict(entire_proof_companion_57732_characters_ROOT_physically_read=True,untruncated_overlapping_character_intervals=[[0,19000],[18600,38000],[37600,48500],[48100,57732]],entire_source_ledger_in_that_read=True,all_five_expanded_bodies_physically_read_within_proof=True,all_expanded_outside_fields_ROOT_read=True,entire_coverage_original_verdict_checks_environment_commands_ROOT_read=True,partial_paper_entire_exact_proof_suffix_content_identity=True,conditional_paper_entire_exact_read_header_n1_and_ledger_composition=True,duplicate_content_identity_NOT_new_separate_physical_reading=True),
    actual_expanded_comparisons=comparisons,
    new_scope='For the explicit smooth boundaryless analytic torus and the locally uniform middle-positive bounded class C_theta, full ordinary-local branch tests U_N satisfy E_theta(U_N)=-1/6-N/3, U_N(1,1)=-1/6-N, hence E_theta(U_N)-2U_N(1,1)=1/6+5N/3. The mass-two rigid atom has INFINITE dual energy on this bounded class despite restricted separable dual energy 1/6. Applies to any extension containing these tests and the same energy; no class identification is assumed.',
    other_whole_scope='Entire quotient geometry, conditional constant meromorphic field/nonalgebraization for all separated finite-type algebraic spaces, middle-cone repair, bounded mixed calculus and mass 2, actual off-canonical-skeleton mass-one atom, circle product equations and restricted energy/envelopes retained in full.',
    nonalgebraization_gate='F_L: Picard vanishing of every finite nonzero-width polyannulus. Gruson IV.5 applies to disc/unit-circle factors; printed Van der Put broader restricted-extension claim does not discharge this gate. No unconditional nonalgebraization acceptance.',
    source_qualification=dict(native267_fresh_source_claims='Attributed to native267 in the entire retained source application ledger. Not fresh ROOT primary physical reading.',ROOT_prior_source_coverage='Earlier ROOT374/373 complete applied Van der Put/Gruson/current Stacks and CLD units and viewed pixels retain their precise historical scopes. No current native web/source or new Gruson pixel is credited as ROOT fresh reading.',new_native_primary_pixels_ROOT_viewed=False,new_native_primary_immediate_proofs_ROOT_freshly_read=False,all_primary_bodies_literal_units_and_pixels_LOCALONLY=True,deeper_foundations_not_rebuilt=True),
    original_gaps=['Unconditional F_L or independently proved nonalgebraization','Full intrinsic psh class and bounded-class comparison','Unbounded E1 and full-mass mixed products and decreasing continuity','All-direction envelope orthogonality and suitable compactness','Full first variation and finite-energy measure criterion','Existence and uniqueness for EVERY admissible arbitrary-support measure'],
    original_counterexample=False,other_atoms_counted=[],supplied_or_native_programs_executed_or_imported=False,native_programs_public_INERT_DATA_only=True,finite_computations_DATA_not_analytic_proof=True,compiler='Native standalone paper is Markdown. No TeX/PDF compilation claimed; protected editor remains unchanged.',protected_editor_open_unchanged=True)
write(D/'mandatory-ROOT-whole-proof-source-scope-qualifications-20261008.json',qual)
(D/'README.md').write_text('Whole candidate378 for P16.7\n\nUNREVIEWED. 16/42 original problems solved, 26 OPEN, 97 accepted papers; no increase.\n\nThe complete paper proves an exact branch-energy formula and divergence of the bounded dual energy of a rigid mass-two atom. This removes a false shortcut from restricted separable finiteness to full admissibility. It preserves the full bounded theory and the conditional nonalgebraization proof with its explicit polyannulus Picard gate. Full intrinsic unbounded E1 and all-support existence/uniqueness remain unresolved.\n\nAll five actual FINAL texts and the complete expanded proof and source/scope ledger were physically read. Distinct returned and expanded texts are retained separately. Whole partial and conditional papers are verified exact compositions of that read material, without a false fresh duplicate-reading claim. New native primary reading stays attributed native267; ROOT prior source scopes are preserved. All full primary bodies, source units and pixels remain LOCALONLY. Native programs are inert data and were never run/imported by ROOT. No protected-editor changes or compiled PDF claimed.\n')
binding=dict(recorded_utc=now,round=267,paper=378,atom='P16.7',public_directory=str(D),private_directory=str(P),whole_original_solved=False,new_accepted_paper=False,counts=dict(solved=16,open=26,papers=97),qualified_whole_reading=qual,public_whole_body_bindings=[dict(path=str(p),bytes=p.stat().st_size,sha256=sha(p)) for p in sorted(D.rglob('*')) if p.is_file()],private_retention_bindings=[dict(path=str(p),bytes=p.stat().st_size,sha256=sha(p)) for p in sorted(P.rglob('*')) if p.is_file()]);write(B,binding)
for n in ['active-work.json','checklist-current.json']:
    p=R/n;x=load(p);assert len(x['fully_solved_original_atoms'])==16 and x['remaining_open_original_atoms']==26 and x['historical_reviewed_scoped_papers']==97
    x['native267_complete378']=dict(public_directory=str(D),whole_binding=str(B),whole_binding_sha256=sha(B),actual_FINAL_sha256=sha(actual),candidate=False,original_closed=False,new_accepted_paper=False,independent_whole_reconstruction_pending=True);x['updated_utc']=now;write(p,x)
print(json.dumps(dict(round=267,paper=378,public_files=len(binding['public_whole_body_bindings']),private_files=len(binding['private_retention_bindings']),whole_proof_sha256=sha(A/'proof-companion.md'),binding_sha256=sha(B),candidate=False,solved=16,open=26,papers=97),indent=2))
