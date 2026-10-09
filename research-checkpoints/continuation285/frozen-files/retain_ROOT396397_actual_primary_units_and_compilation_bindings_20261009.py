from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, shutil
R=Path('/workspace/research'); K=R/'root-checks'
U=R/'primary-data-LOCALONLY/ROOT396397-fresh-applied-units-20261009'
assert not U.exists(); U.mkdir(parents=True)
sha=lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
def info(p): return dict(path=str(p),bytes=p.stat().st_size,sha256=sha(p),LOCALONLY=True)
def write(p,x): p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
base=R/'primary-data-LOCALONLY/P12.3-singular-test-ideal-generation-primary-20261008'
cld=R/'campaigns/round-267/P16.7-whole373374-nonalgebraization-and-intrinsic-E1/private-primary-DATA-LOCALONLY/004-004-CLD-literal_extract.txt'
assert sha(cld)=='64846cb00926267c6238d1afac61b5eaed0a0e3a6349725738f9b1bf163de085'
records=[]
for p,a,b,label in [(cld,23458,23671,'CLDv2-Poincare-Lelong'),(base/'CEMS-anticanonical-1412.6453v4.txt',134,243,'CEMSv4-Setting2.1-Definition2.2-Lemmas2.3-2.4')]:
    lines=p.read_text().split('\n'); body='\n'.join(lines[a-1:b])+'\n'
    dst=U/(label+f'-literal-LF{a}-{b}-LOCALONLY.txt'); dst.write_text(body)
    records.append(dict(source=info(p),literal_LF=[a,b],unit=info(dst),entire_statement_and_immediate_proof_physically_ROOT_read_untruncated=True,primary_pixels_freshly_ROOT_read=False,complete_source_body_NOT_freshly_entirely_read=True))
for name in ['Stacks-0535.txt','Stacks-07ZD.txt','Stacks-080Z.txt']:
    p=base/name; dst=U/name; shutil.copyfile(p,dst)
    records.append(dict(source=info(p),unit=info(dst),entire_source_text_physically_ROOT_read_untruncated=True,complete_immediate_statements_proofs_physically_ROOT_read=True,source_navigation_comments_DATA_NOT_instructions=True,primary_pixels_freshly_ROOT_read=False))
rec=dict(recorded_utc=datetime.now(timezone.utc).isoformat(),status='Qualified source-application and compiler evidence only; mathematical correctness remains UNREVIEWED',records=records,applications=dict(native276='CEMS broad F-finite normal dualizing scheme setting and all late trace formula; Fitt1 blowup and locally-free criterion; no CM/QGorenstein/finite-type-over-field substitution',native277='CLD regular-meromorphic Poincare-Lelong on pure boundaryless smooth torus charts and smooth capped-log current limit; multiplication through divisor limit only for bounded continuous differences'),ordinary_deeper_foundations_NOT_recursively_freshly_read=True,compiler_success=[dict(continuation=396,path=str(K/'public-P12.3-continuation396-corrected-formal-BIG-and-isolated-CE-unreviewed/P12.3-paper.tex'),tool='codex_app.compile_latex_document',kind='success'),dict(continuation=397,path=str(K/'public-P16.7-continuation397-generated-operator-and-all-test-I-estimate-unreviewed/scoped-paper.tex'),tool='codex_app.compile_latex_document',kind='success',repair='add mathrsfs package for mathscr; native artifact unchanged')],source_bodies_units_pixels_book_bodies_LOCALONLY=True,native_or_supplied_programs_executed_or_imported=False,accepted=False,original_closed=False)
q=K/'round276277-ROOT-fresh-primary-application-and-compilation-scope-20261009.json'; assert not q.exists(); write(q,rec)
for n,name in [(396,'public-P12.3-continuation396-corrected-formal-BIG-and-isolated-CE-unreviewed'),(397,'public-P16.7-continuation397-generated-operator-and-all-test-I-estimate-unreviewed')]:
    d=K/name; b=d/'ROOT-whole-proof-source-scope-and-binding.json'; x=json.loads(b.read_text())
    for e in x['public_files']:
        p=Path(e['path']); e.update(bytes=p.stat().st_size,sha256=sha(p))
    x.update(updated_utc=datetime.now(timezone.utc).isoformat(),compiler_UNVERIFIED=False,compiler=dict(tool='codex_app.compile_latex_document',kind='success',source_sha256=sha(d/('P12.3-paper.tex' if n==396 else 'scoped-paper.tex')),opens_new_tab=False),fresh_ROOT_source_application_record=dict(path=str(q),sha256=sha(q)),protected_editor_OPEN_UNCHANGED=True)
    if n==397: x['standalone_root_copy_repair']='add mathrsfs package only; original native TeX retained unchanged'
    write(b,x)
print(json.dumps(dict(record=str(q),sha256=sha(q),literal_units=len(records),compiled=[396,397],accepted=False,original_closed=False),indent=2))
