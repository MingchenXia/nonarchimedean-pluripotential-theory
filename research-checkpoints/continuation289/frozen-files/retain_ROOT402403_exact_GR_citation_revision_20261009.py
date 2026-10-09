from pathlib import Path
from datetime import datetime,timezone
import hashlib,json
R=Path('/workspace/research');K=R/'root-checks';G=R/'github-checkpoint'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
load=lambda p:json.loads(p.read_text())
write=lambda p,x:p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
P402=K/'P16.7-continuation402-bounded-atomic-tests-and-Shilov-point-lower-bounds-working-paper-20261009.tex'
P403=K/'P16.7-continuation403-generated-uniqueness-by-two-actual-Gauss-fibres-working-paper-20261009.tex'
S=R/'campaigns/round-267/P16.7-whole373374-nonalgebraization-and-intrinsic-E1/private-primary-DATA-LOCALONLY/004-004-CLD-literal_extract.txt'
T=R/'primary-data-LOCALONLY/P16.7-classical-PSH-Shilov-GR-v2-primary-20261009/GR2506.13548v2-full-LOCALONLY.txt'
assert sha(S)=='64846cb00926267c6238d1afac61b5eaed0a0e3a6349725738f9b1bf163de085' and sha(T)=='3a221b86116604c950db07e4c60ab184701f0624deebabd92502e5c81871436b'
old='stages. The published smooth CLD-to-classical bridge is GRv2\nTheorem1.2. Its Proposition4.2 gives sheafiness and decreasing-net'
new='stages. The published smooth CLD-to-classical bridge is the\nunnumbered statement and argument in GRv2 Section1.2.\nIts Proposition4.2 gives sheafiness and decreasing-net'
prior=[]
for number,p in [(402,P402),(403,P403)]:
    frozen=G/'continuation288-publication-records/frozen-files/root-checks'/p.name
    before=frozen.read_text();after=p.read_text();assert before.count(old)==1 and after==before.replace(old,new)
    prior.append(dict(paper=number,before_sha256=sha(frozen),after_sha256=sha(p),only_change='Correct GR smooth-recognition source designation to unnumbered Section1.2',actual_recompile_kind='success',mathematical_claim_changed=False))
q402=K/'ROOT402-fresh-primary-application-and-compilation-scope-20261009.json';q403=K/'ROOT403-fresh-primary-application-and-compilation-scope-20261009.json'
a=load(q402);b=load(q403);unit_checks=[]
for e in a['source_units']:
    carrier=Path(e['source']);parts=carrier.read_bytes().split(b'\n');exact=b'\n'.join(parts[e['LF_start']-1:e['LF_end']])+b'\n'
    unit=Path(e['path']);assert exact==unit.read_bytes() and sha(unit)==e['sha256'];unit_checks.append(dict(path=str(unit),literal_newline_only_identity=True))
for e in b['fresh_applied_source_units']:
    lo,hi=e['literal_LF'];parts=S.read_bytes().split(b'\n');exact=b'\n'.join(parts[lo-1:hi])+b'\n'
    unit=Path(e['local_unit_path']);assert exact==unit.read_bytes() and sha(unit)==e['sha256'];unit_checks.append(dict(path=str(unit),literal_newline_only_identity=True))
unit=R/'primary-data-LOCALONLY/P16.7-ROOT403-two-actual-Gauss-fibres-source-20261009/GR-v2-Section1.2-LF96-112-LOCALONLY.txt'
assert not unit.exists();unit.write_bytes(b'\n'.join(T.read_bytes().split(b'\n')[95:112])+b'\n')
body=P402.read_text();body=body[body.index('\\section{The actual analytic object'):body.index('\\end{document}')]
assert P403.read_text().count(body)==1
appendix=dict(source_path=str(P402),source_sha256=sha(P402),body_bytes=len(body.encode()),body_sha256=hashlib.sha256(body.encode()).hexdigest(),exact_identity=True,second_independent_source_reading=False)
now=datetime.now(timezone.utc).isoformat();Q=K/'ROOT402403-GR-source-designation-only-revision-20261009.json'
rec=dict(recorded_utc=now,revisions=prior,whole_GR_Section1_2_statement_and_immediate_argument_ROOT_physically_read=True,GR_source_sha256=sha(T),local_GR_literal_unit=dict(path=str(unit),LF=[96,112],sha256=sha(unit),bytes=unit.stat().st_size,LOCALONLY=True),all_16_retained_literal_units_newline_only_identity=unit_checks,original_checkpoint288_frozen_sources_unchanged=True,actual_built_in_recompilations_both_success=True,accepted=False,original_closed=False,UNREVIEWED=True,protected_editor_OPEN_UNCHANGED=True)
write(Q,rec)
a.update(recorded_utc=now,source_designation_revision=dict(path=str(Q),sha256=sha(Q)),compiler=dict(path=str(P402),kind='success',actual_recompile_observed=True,mathematical_certification=False))
b.update(recorded_utc=now,paper=dict(path=str(P403),bytes=P403.stat().st_size,sha256=sha(P403)),exact_ROOT402_appendix_whole_body=appendix,source_designation_revision=dict(path=str(Q),sha256=sha(Q)),compiler=dict(path=str(P403),kind='success',actual_recompile_observed=True,mathematical_certification=False))
write(q402,a);write(q403,b)
for number,p,q in [(402,P402,q402),(403,P403,q403)]:
    binding=K/f'P16.7-continuation{number}-ROOT-whole-paper-source-scope-and-binding-20261009.json'
    v=load(binding);v.update(recorded_utc=now,source_scope=dict(path=str(q),sha256=sha(q)),compiler=load(q)['compiler'],source_designation_revision=dict(path=str(Q),sha256=sha(Q)))
    v['whole_paper' if number==402 else 'paper']=dict(path=str(p),bytes=p.stat().st_size,sha256=sha(p))
    if number==403:v['exact_ROOT402_appendix']=appendix
    write(binding,v)
assert sha(K/'public-P16-round-46-final-reader/P16.4-paper.tex')=='09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
for name in ['active-work.json','checklist-current.json']:
    p=R/name;x=load(p);assert x['github_pending_checkpoint'] is None and x['current_active_batch']==[] and x['latest_verified_github_checkpoint']['continuation']==288
    assert len(x['fully_solved_original_atoms'])==16 and x['remaining_open_original_atoms']==26 and x['historical_reviewed_scoped_papers']==97
    x.update(updated_utc=now,ROOT402403_GR_source_designation_revision=dict(record=str(Q),sha256=sha(Q),paper402_sha256=sha(P402),paper403_sha256=sha(P403),compiled=True,UNREVIEWED=True))
    x['ROOT403_generated_pointwise_uniqueness_working_proof']['sha256']=sha(P403)
    write(p,x)
print(json.dumps(dict(revision=str(Q),papers=prior,newline_units_verified=len(unit_checks),both_compiled=True,original_closed=False,accepted=False),indent=2))
