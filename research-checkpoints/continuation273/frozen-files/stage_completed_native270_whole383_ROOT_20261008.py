from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, re, shutil

R=Path('/workspace/research'); K=R/'root-checks'
C=R/'campaigns/round-270/P16.7-whole378-polyannulus-Picard-and-intrinsic-E1'
A=C/'artifacts/codex-PjZjwy'
D=K/'public-P16.7-continuation383-finite-Picard-nonalgebraization-and-constant-branch-energy-whole-candidate'
P=R/'primary-data-LOCALONLY/P16.7-native270-whole-primary-and-evidence-20261008'
B=K/'P16.7-round270-whole-candidate383-ROOT-proof-source-scope-and-binding-20261008.json'
S=R/'primary-data-LOCALONLY/P16.7-period-algebraization-primary-20261008'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
load=lambda p:json.loads(Path(p).read_text())
def write(p,x):p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
assert not D.exists() and not P.exists() and not B.exists()
actual=K/'round270-actual-native-final.json'; assert sha(actual)=='7250b57403edc18d240f08d106f41dcc60d349ba9fa5c768a8c0b8dc7a90ca71'
j=load(actual); e=load(A/'final-notes.json'); assert not j['candidate'] and not e['candidate'] and len(j['notes'])==len(e['notes'])==5
proof=(A/'proof-companion.md').read_text(); paper=(A/'P16.7-standalone-paper.md').read_text(); tex=(A/'P16.7-standalone-paper.tex').read_text(); ledger=(A/'source-application-ledger.md').read_text()
assert len(proof)==66573 and proof=='# Complete own proof companion\n\n'+paper and proof.endswith(ledger)
special={'\\':r'\textbackslash{}','{':r'\{','}':r'\}','$':r'\$','&':r'\&','#':r'\#','%':r'\%','_':r'\_','~':r'\textasciitilde{}','^':r'\textasciicircum{}'}
def esc(s):return ''.join(special.get(c,c) for c in s)
comparisons=[]; sections=[]
for x,y in zip(j['notes'],e['notes']):
    assert x['id']==y['id'] and x['text']!=y['text'] and y['text'] in proof and (A/'notes'/(y['id']+'.md')).read_text()==y['text']
    heading,body=y['text'].split('\n',1); sections.append('\\section{'+esc(heading.removeprefix('# '))+'}\n'+esc(body)+'\n')
    comparisons.append(dict(id=x['id'],actual_text_sha256=hashlib.sha256(x['text'].encode()).hexdigest(),expanded_text_sha256=hashlib.sha256(y['text'].encode()).hexdigest(),actual_DIFFERS_expanded=True,expanded_entire_literal_proof_substring=True))
expected='\n'.join(sections)+'\n\\section{Full source application and reading ledger}\n'+esc(ledger)+'\n\\end{document}\n'
assert tex[tex.index('\\section{n1.'):]==expected
assert sha(K/'public-P16-round-46-final-reader/P16.4-paper.tex')=='09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
D.mkdir(); P.mkdir(); shutil.copytree(A/'inputs-LOCALONLY',P/'native-selected-inputs'); shutil.copytree(A/'sources-LOCALONLY',P/'native-full-source-evidence')
T=P/'entire-frozen-primary-packet'; T.mkdir()
for i,u in enumerate(load(C/'private-primary-packet-bindings.json')):
    p=Path(u['path']); assert p.stat().st_size==u['bytes'] and sha(p)==u['sha256']; shutil.copyfile(p,T/(f'{i:03d}-'+p.name))
for name in ['P16.7-standalone-paper.md','P16.7-standalone-paper.tex','proof-companion.md','final-notes.json','source-application-ledger.md','README.md']:shutil.copyfile(A/name,D/name)
shutil.copytree(A/'evidence',D/'evidence'); shutil.copyfile(actual,D/'actual-settled-native270-FINAL.json'); shutil.copyfile(C/'original-task.json',D/'original-task.json')
for n in j['notes']:(D/(n['id']+'-actual-settled.md')).write_text(n['text'])
for n in e['notes']:shutil.copyfile(A/'notes'/(n['id']+'.md'),D/(n['id']+'-expanded.md'))
Q=D/'native-programs-INERT-DATA'; Q.mkdir()
for p in sorted((A/'scripts').glob('*.py')):shutil.copyfile(p,Q/(p.name+'.DATA.txt'))
vdp=S/'Van-der-Put-Rigid-analytic-spaces-1975-1976.txt'; gr=S/'Gruson-Fibres-vectoriels-polydisque-1968.txt'
assert sha(vdp)=='4a7f66af66a9c4e8950376b533b0701945b7e81459c8b1232f17afc2ca628de7'
assert sha(gr)=='101445a9e73b87bcc6d1fdb1aafce1eaf38b44390ba9c960226e510c3e94da93'
fresh=[]
for p,lo,hi in [(vdp,575,707),(gr,1510,1690)]:
    u=P/(f'ROOT383-fresh-full-{p.stem}-LF{lo}-{hi}-LOCALONLY.txt'); u.write_text('\n'.join(p.read_text().split('\n')[lo-1:hi])+'\n')
    fresh.append(dict(source_path=str(p),source_sha256=sha(p),inclusive_LF_interval=[lo,hi],entire_interval_ROOT_physically_read_untruncated=True,literal_unit_path=str(u),literal_unit_bytes=u.stat().st_size,literal_unit_sha256=sha(u),LOCALONLY=True))
pixel=S/'ROOT383-Van-der-Put-PDF-page10-coherent-descent.png'; assert pixel.is_file()
now=datetime.now(timezone.utc).isoformat()
qual=dict(recorded_utc=now,status='UNREVIEWED complete independent native270 draft; original P16.7 OPEN/candidateFALSE. No acceptance/count increase.',counts=dict(solved=16,open=26,papers=97),whole_original_solved=False,new_accepted_paper=False,
    actual_FINAL=dict(path=str(actual),sha256=sha(actual),all_five_complete_actual_fields_ROOT_physically_read=True,intermediate_messages_excluded=9),actual_expanded_comparisons=comparisons,
    ROOT_whole_reading=dict(entire66573character_companion_ROOT_physically_read=True,untruncated_overlapping_intervals=[[0,18500],[18100,37000],[36600,53000],[52600,66573]],all_five_expanded_bodies_physically_read_within_companion=True,all_expanded_outside_fields_ROOT_read=True,entire21055byte_source_ledger_physically_read_within_companion=True,entire_README_coverage_original_verdict_environment_structural_checks_ROOT_read=True,entire66541byteMD_exact_companion_suffix=True,all_five_complete_proof_bodies_and_ledger_exact_verified_character_encoding_in_entire71651byteTeX=True,TeX_preamble_and_all_three_new_displayed_theorem_statements_ROOT_physically_read=True,duplicate_body_identity_NOT_new_separate_fresh_physical_reading=True),
    new_claims='BaseK C((s)) Pic of every finite product discs/circles/wide annuli with radii in |K*| vanishes: Gruson SK0 ONLY pure disc/circle factors, determinant cancellation, finite rational G-cover hole filling induction. Compatible torus frames/all pole ideals give M(X)=K and exclude EVERY separated finite-type K-algebraic-space algebraization. No arbitrary extension claim. Ordinary generated bounded Ctheta full middle-PSD products/rawmass2; ALL real N branch pencil energy -1/6-a^3N/3, MA convex combination with a^2; normalized constant-energy -2/3 family disproves UNIFORM compactness. Finite bounded dual gives necessary bidisc mass<=const*N^(-2/3), not sufficiency.',
    ROOT_new_primary_reading=fresh,
    ROOT_new_pixel=dict(path=str(pixel),bytes=pixel.stat().st_size,sha256=sha(pixel),PDF_one_based_page=10,printed_page='J7-09',fresh_ROOT_visual_reading=True,scope='Complete2.16 coherent-affinoid statement and immediate descent proof/diagram, source formulas repaired beyond OCR. Explicitly cites Kiehl for deeper descent proof. Earlier displayed existing page11 was printedJ7-10/3.1, not evidence for2.16.',LOCALONLY=True),
    primary_scope='Gruson IV5 entire statement/immediate proof freshly ROOT read with actual disc/circle definitions, SK0 not wider-factor theorem; deeper graded K0/filtered dependencies retain earlier scope, not fabricated new whole proof. Van der Put2.14-2.16.3 whole text freshly ROOT read with missing formulas checked against actual printedJ7-09 source pixel. Other new CT/Ducros/Stacks/CLDv2 readings and four source views attributed native270, historical ROOT primary scope retained exactly. No fullKiehl/CLD608pages/all book or recursive historical source tree fresh reading claim.',
    original_remaining='Intrinsic unbounded all-direction psh/E1 and comparison with Ctheta, genuine full-mass mixed products and decreasing continuity, useful separated weak compactness, arbitrary analytic-obstacle envelopes/orthogonality, full first variation, sufficient finite-energy measure criterion, EVERY admissible arbitrary-support mass-two measure existence and full uniqueness remain OPEN. Rigid atom bounded dual infinite, ineligible as original counterexample. No inverse-construction MA or restricted-S closure.',
    all_full_primary_bodies_literal_units_and_pixels_LOCALONLY=True,supplied_or_native_programs_executed_or_imported=False,native_programs_inert_DATA_only=True,finite_diagnostics_not_universal_analytic_proof=True,no_other_ACTIVE271_mathematical_read_or_feedback=True,
    compiler='Saved standalone source; built-in check follows staging. No successful compilation/PDF/export/install/newtab claimed.',protected_editor_open_unchanged=True)
write(D/'mandatory-ROOT-whole-proof-source-scope-qualifications-20261008.json',qual)
binding=dict(recorded_utc=now,round=270,paper=383,atom='P16.7',public_directory=str(D),private_directory=str(P),whole_original_solved=False,new_accepted_paper=False,counts=dict(solved=16,open=26,papers=97),qualified_whole_reading=qual,public_whole_body_bindings=[dict(path=str(p),bytes=p.stat().st_size,sha256=sha(p)) for p in sorted(D.rglob('*')) if p.is_file()],private_retention_bindings=[dict(path=str(p),bytes=p.stat().st_size,sha256=sha(p)) for p in sorted(P.rglob('*')) if p.is_file()]); write(B,binding)
for name in ['active-work.json','checklist-current.json']:
    p=R/name; x=load(p); assert len(x['fully_solved_original_atoms'])==16 and x['remaining_open_original_atoms']==26 and x['historical_reviewed_scoped_papers']==97
    x['native270_complete383']=dict(public_directory=str(D),whole_binding=str(B),whole_binding_sha256=sha(B),actual_FINAL_sha256=sha(actual),candidate=False,original_closed=False,new_accepted_paper=False,finite_Picard_gate_new_independent_draft=True); x['updated_utc']=now; write(p,x)
print(json.dumps(dict(round=270,paper=383,public_files=len(binding['public_whole_body_bindings']),private_files=len(binding['private_retention_bindings']),whole_TeX_sha256=sha(D/'P16.7-standalone-paper.tex'),whole_proof_sha256=sha(D/'proof-companion.md'),binding_sha256=sha(B),candidate=False,solved=16,open=26,papers=97),indent=2))
