from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, shutil, subprocess, re
R=Path('/workspace/research'); K=R/'root-checks'
A=Path(json.loads((K/'P05.2-round184-completed-actual-author-result-20261007.json').read_text())['workspace'])
D=K/'public-P05.2-continuation224-strict-growth-obstruction'; assert not D.exists()
sha=lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
D.mkdir(); (D/'evidence').mkdir()
for name in ('P05.2-paper.tex','P05.2-paper.pdf','argument.md','source-application-ledger.md','structured-notes.json','check_obstruction.py','obstruction-input.json','README.md'):
    shutil.copyfile(A/name,D/name)
assert sha(D/'P05.2-paper.tex')==sha(A/'P05.2-paper.tex')
check=subprocess.run(['python','check_obstruction.py'],cwd=D,capture_output=True,text=True,check=True)
(D/'evidence/root-check.stdout').write_text(check.stdout)
assert json.loads((D/'evidence/check-output.json').read_text())['all_assertions_passed']
for i in (1,2):
    p=subprocess.run(['pdflatex','-interaction=nonstopmode','-halt-on-error','P05.2-paper.tex'],cwd=D,capture_output=True,text=True)
    (D/f'evidence/root-latex-pass{i}.stdout').write_text(p.stdout)
    assert p.returncode==0
warnings=re.findall(r'.*(?:Warning|Overfull|Underfull|undefined|^!).*',(D/'P05.2-paper.log').read_text(),re.M); assert not warnings,warnings
record=dict(recorded_utc=datetime.now(timezone.utc).isoformat(),atom='P05.2',continuation=224,native_author_round=184,
    native_workspace=str(A),source_sha256=sha(D/'P05.2-paper.tex'),source_lf_lines=241,source_equal_complete_native_source=True,whole_saved_source_root_read=True,
    whole_argument_and_source_ledger_root_read=True,fresh_clean_local_builds=2,local_warning_count=0,root_finite_check_rerun=True,
    finite_checks_only=True,source_provenance_program_root_rerun=False,pdf_sha256=sha(D/'P05.2-paper.pdf'),pdf_pages=9,
    all_pdf_pages_visually_root_read=False,root_visual_pages_read=[],independent_mathematical_verdict=None,new_accepted_paper=False,original_closed=False,
    protected_editor_unchanged_open=True,no_active_private_output_read=True)
(D/'root-reproduction-binding-20261007.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
