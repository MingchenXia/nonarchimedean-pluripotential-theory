from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,re,shutil,subprocess
R=Path('/workspace/research');K=R/'root-checks'
D=K/'public-P14.8-continuation308-arbitrary-formal-ideal-realization-on-projective-line'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
source=D/'P14.8-paper.tex';digest=sha(source)
old=D/'evidence/pre-representative-repair-20261008/P14.8-paper.tex'
assert sha(old)=='3e8ea22f01ca3574aa4e08ed5ded84fab03a9f9a07e7d72c9c4d67b71e23d92d' and digest!=sha(old)
text=source.read_text()
assert 'The resulting function is subharmonic with curvature' not in text
assert 'take its canonical subharmonic representative' in text and 'upward spikes on null sets' in text
E=D/'evidence/ROOT-representative-repair-build-20261008';assert not E.exists();E.mkdir();(E/'build').mkdir()
shutil.copyfile(source,E/source.name);passes=[]
for n in [1,2]:
 argv=['pdflatex','-no-shell-escape','-interaction=nonstopmode','-halt-on-error','-output-directory=build',source.name]
 result=subprocess.run(argv,cwd=E,capture_output=True,text=True)
 (E/f'pass{n}.stdout.log').write_text(result.stdout);(E/f'pass{n}.stderr.log').write_text(result.stderr)
 log=E/'build/P14.8-paper.log'
 if log.exists():shutil.copyfile(log,E/f'pass{n}.tex.log')
 warnings=[line for line in log.read_text(errors='replace').splitlines() if re.search(r'Warning|Overfull|Underfull|Undefined',line)] if log.exists() else []
 passes.append(dict(pass_number=n,argv=argv,exit_code=result.returncode,warnings=warnings))
 assert result.returncode==0, result.stdout[-3000:]
assert passes[-1]['warnings']==[] and sha(source)==digest and sha(E/source.name)==digest
pdf=E/'build/P14.8-paper.pdf'
info=subprocess.run(['pdfinfo',str(pdf)],capture_output=True,text=True,check=True).stdout;(E/'pdfinfo.txt').write_text(info)
pages=int(re.search(r'^Pages:\s+(\d+)',info,re.M).group(1));shutil.copyfile(pdf,D/'P14.8-paper.pdf')
assert sha(K/'public-P16-round-46-final-reader/P16.4-paper.tex')=='09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
value=dict(recorded_utc=datetime.now(timezone.utc).isoformat(),continuation=308,old_source_sha256=sha(old),repaired_source=str(source),repaired_source_sha256=digest,repaired_source_bytes=source.stat().st_size,repaired_pdf_sha256=sha(D/'P14.8-paper.pdf'),pages=pages,passes=passes,whole_revised_source_ROOT_read=True,repair='Explicit canonical subharmonic representative almost everywhere, with local logarithmic-potential proof and integrability invariance; false pointwise sentence removed',unchanged_native229_verdict='FAIL preserved; audit did not read this new revision',ordinary_reconstruction='Native229 n1/n2 independently prove the representative step and intended same criterion; ROOT inserted it and checked the revised full proof',no_new_accepted_paper=True,no_original_closure_from_this_curve_repair=True,counts=dict(solved=10,open=32,accepted=88),builtin_old_cell90_unverified=True,builtin_revised_cell228_pending=True,historical_ROOT_binding_applies_only_to_pre_repair_source=True,general_P14_8_solved_separately_by309_audit230=True,protected_editor_unchanged_open=True)
record=D/'ROOT-representative-repair-and-build-binding-20261008.json';assert not record.exists();record.write_text(json.dumps(value,indent=2)+'\n')
for name in ['active-work.json','checklist-current.json']:
 p=R/name;x=json.loads(p.read_text());assert x['historical_reviewed_scoped_papers']==88
 x['P14_8_projective_line308_repaired_revision']=value;x['prepared_P1_formal_ideal_audit229'].update(repair_pending=False,repaired_revision_binding=str(record),repaired_revision_binding_sha256=sha(record),unchanged_mathematical_verdict='FAIL retained');p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(source_sha256=digest,pdf_sha256=sha(D/'P14.8-paper.pdf'),pages=pages,final_warnings=[],binding_sha256=sha(record)),indent=2))
