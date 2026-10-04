"""Artifact integrity and reproducibility checks, not mathematical verification."""
from pathlib import Path
import json,hashlib,subprocess
root=Path(__file__).resolve().parent
checks={}
inp=json.loads((root/'input.json').read_text());task=json.loads((root/'task.json').read_text())
checks['original_task_unchanged']=task==inp['task']
checks['assignment_unchanged']=(root/'assignment.txt').read_text()==inp['assignment']+'\n'
checks['original_scope_unchanged']=(root/'original-scope.txt').read_text()==inp['task']['problem']+'\n\n'+inp['task']['completionCriteria']+'\n'
status=json.loads((root/'status.json').read_text())
checks['exact_five_status_keys']=set(status)=={'id','status','exact_result','proof_file','concrete_gaps'}
checks['partial_not_original_atom_closure']=status['id']=='P05.2' and status['status']=='partial'
checks['proof_file_exists']=status['proof_file']=='P05.2-argument.md' and (root/status['proof_file']).exists()
hashes=json.loads((root/'source-hashes.json').read_text())
checks['sources_unchanged_and_exact_snapshots']=all((root/r['file']).read_bytes()==Path(r['origin']).read_bytes() and hashlib.sha256((root/r['file']).read_bytes()).hexdigest()==r['sha256'] for r in hashes)
checks['all_canonical_notes_preserved']=len(json.loads((root/'sources/canonical-two-graph-notes.json').read_text()))==3 and len(json.loads((root/'sources/canonical-cylinder-notes.json').read_text()))==2
checks['all_selected_primary_bodies_present_in_fresh_PDF_extraction']=all(y['exact_body_present_in_fresh_extraction'] for x in json.loads((root/'source-authentication.json').read_text()) for y in x['selected_body_checks'])
ar=(root/'sources/Allermann-Rau-0709.3705.txt').read_text()
bmps=(root/'sources/BMPS2603.08664v1-from-pdf.txt').read_text()
checks['primary_version_and_date_identifiers']='arXiv:0709.3705v3' in ar and '20 Jan 2009' in ar and 'arXiv:2603.08664v1' in bmps and 'Date: March 10, 2026.' in bmps
checks['exact_finite_diagnostics_passed']=json.loads((root/'diagnostic-output.json').read_text())['all_assertions_passed']
b=json.loads((root/'build-evidence.json').read_text());checks['two_successful_final_compilations']=b['two_successful_compilations']
checks['PDF_matches_build_record']=hashlib.sha256((root/'P05.2-partial.pdf').read_bytes()).hexdigest()==b['pdf_sha256']
log=(root/'P05.2-partial.log').read_text()
checks['final_log_no_glyph_math_or_overfull_warnings']=all(x not in log for x in ['Missing character','Overfull','Undefined control sequence','! Missing'])
r=subprocess.run(['pdfinfo','P05.2-partial.pdf'],capture_output=True,text=True,cwd=root)
(root/'pdfinfo.txt').write_text(r.stdout+r.stderr)
checks['pdfinfo_success']=r.returncode==0
notes=json.loads((root/'result-notes.json').read_text())
checks['canonical_note_schema']=not notes['candidate'] and all(set(n)=={'id','summary','detailedSummary','text','support'} for n in notes['notes']) and [n['id'] for n in notes['notes']]==['n1','n2','n3']
all_pass=all(checks.values())
evidence={'checks':checks,'all_passed':all_pass,'interpretation':'Artifact, source and finite-program checks only. No mathematical verification or priority certification.'}
(root/'checks.json').write_text(json.dumps(evidence,indent=2)+'\n')
artifacts=[]
for p in sorted(root.iterdir()):
 if p.is_file() and p.name not in ['artifact-hashes.json']:
  artifacts.append({'file':p.name,'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()})
(root/'artifact-hashes.json').write_text(json.dumps(artifacts,indent=2)+'\n')
print(json.dumps(evidence,indent=2))
if not all_pass:raise SystemExit(1)
