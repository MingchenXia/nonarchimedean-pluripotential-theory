from pathlib import Path
from datetime import datetime, timezone
import difflib, hashlib, json, shutil, subprocess
R=Path('/workspace/research');D=R/'deliverables/original-P16.2'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
p=D/'P16.2-core.md';old=p.read_text()
assert sha(p)=='68e80f9af75880ddcc2dca91287671e7b0e8bc147985e0dd72360ed1a9cf722f'
record=D/'publication-set-difference-typography-repair.json'
assert not record.exists()
before_tex_sha=sha(D/'P16.2-paper.tex')
log=D/'P16.2-paper.log'
assert 'Undefined' in log.read_text()
shutil.copyfile(log,D/'local-first-build-error.log')
replacements=[('V=X^an\\P',r'$V=X^{\rm an}\setminus P^{\rm an}$',2),
              ('Y^an\\D',r'$Y^{\rm an}\setminus D^{\rm an}$',1),
              ('Y\\D',r'$Y^{\rm an}\setminus D^{\rm an}$',1)]
text=old
for before,after,n in replacements:
    assert text.count(before)==n,(before,text.count(before),n)
    text=text.replace(before,after)
p.write_text(text)
(D/'P16.2-core.set-difference-typography.patch').write_text(''.join(difflib.unified_diff(
    old.splitlines(True),text.splitlines(True),fromfile='pre-repair/P16.2-core.md',tofile='publication/P16.2-core.md')))
subprocess.run(['pandoc',str(p),'--standalone','--from=markdown+tex_math_dollars',
    '--to=latex','--pdf-engine=xelatex','--output',str(D/'P16.2-paper.tex')],check=True,capture_output=True,text=True)
record.write_text(json.dumps({'recorded_utc':datetime.now(timezone.utc).isoformat(),
    'change':'Put four already defined analytic set differences in proper math mode; raw backslashes had produced undefined TeX commands or the paragraph symbol.',
    'old_core_sha256':hashlib.sha256(old.encode()).hexdigest(),'core_sha256':sha(p),
    'old_tex_sha256':before_tex_sha,'tex_sha256':sha(D/'P16.2-paper.tex'),
    'first_failed_local_build_log_sha256':sha(D/'local-first-build-error.log'),
    'mathematical_content_changed':False,'native_compile_cell1280_pending':True,
    'existing_P16_4_editor_modified_or_new_tab_opened':False},indent=2)+'\n')
print(record.read_text())
