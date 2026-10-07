from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, shutil, subprocess, re
R=Path('/workspace/research'); K=R/'root-checks'; A=Path(json.loads((K/'P16.4-round186-completed-actual-author-result-20261007.json').read_text())['workspace'])
D=K/'public-P16.4-continuation227-genus-zero-equation'; assert not D.exists()
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
D.mkdir(); (D/'evidence').mkdir()
for name in ('P16.4-paper.tex','P16.4-paper.pdf','P16.4-argument.md','source-application-ledger.json','source-application-ledger.md','notes.json','finite_checks.py','environment.json','build-diagnostics.json'):
    shutil.copyfile(A/name,D/name)
assert sha(D/'P16.4-paper.tex')==sha(A/'P16.4-paper.tex')
p=subprocess.run(['python','finite_checks.py'],cwd=D,capture_output=True,text=True,check=True); (D/'evidence/root-finite-check.stdout').write_text(p.stdout); result=json.loads(p.stdout); assert result['status'].startswith('PASS')
(D/'evidence/root-finite-check.json').write_text(json.dumps(result,indent=2)+'\n')
for i in (1,2):
    p=subprocess.run(['pdflatex','-no-shell-escape','-interaction=nonstopmode','-halt-on-error','P16.4-paper.tex'],cwd=D,capture_output=True)
    (D/f'evidence/root-latex-pass{i}.stdout').write_bytes(p.stdout); assert p.returncode==0
warnings=re.findall(r'.*(?:Warning|Overfull|Underfull|undefined|^!).*',(D/'P16.4-paper.log').read_text(),re.M)
b=dict(recorded_utc=datetime.now(timezone.utc).isoformat(),atom='P16.4',continuation=227,native_author_round=186,native_workspace=str(A),source_sha256=sha(D/'P16.4-paper.tex'),source_lf_lines=851,source_equal_complete_native_source=True,whole_saved_source_root_read=True,whole_four_notes_root_read=True,whole_source_application_json_ledger_root_read=True,whole_native_argument_separately_root_read=False,fresh_final_local_builds=2,local_warnings=warnings,root_finite_check_rerun=True,finite_checks_only=True,pdf_sha256=sha(D/'P16.4-paper.pdf'),pdf_pages=11,all_pdf_pages_visually_root_read=False,root_visual_pages_read=[],independent_mathematical_verdict=None,new_accepted_paper=False,original_closed=False,protected_editor_unchanged_open=True,no_active_private_output_read=True)
(D/'root-reproduction-binding-20261007.json').write_text(json.dumps(b,indent=2)+'\n');print(json.dumps(b,indent=2))
