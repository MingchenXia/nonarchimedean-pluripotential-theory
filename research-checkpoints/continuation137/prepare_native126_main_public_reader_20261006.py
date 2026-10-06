from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, shutil, subprocess
import fitz

R = Path('/workspace/research'); K = R / 'root-checks'
A = R / 'campaigns/round-126/P16.5-original-general-big-relative-operator-and-equation-research/artifacts/codex-8TB2oN'
D = K / 'public-P16.5-round126-main-reader'
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
canonical = K / 'P16.5-round126-actual-native-result-20261006.json'
result = json.loads(canonical.read_text())
assert result['candidate'] is False and len(result['notes']) == 5
assert sha(canonical) == '01e7648de54ead89717c39612357187d8b2c64644d29917c2d9d73a348b1e3b0'
assert sha(A / 'P16.5-argument.md') == 'aa2d427f7fc4895469579a27126e48d7a2e38e5e82fe54279599040059c320cf'
assert json.loads((A / 'status.json').read_text())['status'] == 'PARTIAL'
assert json.loads((A / 'input.json').read_text()) == json.loads((A.parent.parent / 'input.json').read_text())
D.mkdir(exist_ok=False)
for source, destination in [('P16.5-argument.md','P16.5-argument.md'),('P16.5-core.md','P16.5-core.md'),
                            ('status.json','status.json'),('source-application-ledger.json','source-application-ledger.json')]:
    shutil.copyfile(A / source, D / destination)
shutil.copyfile(canonical, D / 'canonical-native-result.json')
commands = [['pandoc','P16.5-argument.md','--standalone','--from=markdown+tex_math_dollars+tex_math_single_backslash','--to=latex','--output=P16.5-paper.tex']]
commands += [['pdflatex','-interaction=nonstopmode','-halt-on-error','-file-line-error','P16.5-paper.tex']] * 2
builds = []
for i, command in enumerate(commands):
    proc = subprocess.run(command, cwd=D, capture_output=True, text=True)
    (D / f'build-{i}.stdout').write_text(proc.stdout)
    (D / f'build-{i}.stderr').write_text(proc.stderr)
    builds.append({'argv':command,'returncode':proc.returncode})
    assert proc.returncode == 0, (i, proc.stdout[-1800:], proc.stderr[-1800:])
pdf = fitz.open(D / 'P16.5-paper.pdf')
pages = len(pdf)
for page in sorted(set([0,pages//2,pages-1])):
    pdf[page].get_pixmap(matrix=fitz.Matrix(1.3,1.3)).save(D / f'layout-page-{page+1}.png')
log = (D / 'P16.5-paper.log').read_text()
binding = {
    'recorded_utc':datetime.now(timezone.utc).isoformat(),'atom':'P16.5','round':126,
    'status':'PARTIAL','candidate':False,'original_closed':False,'independently_accepted':False,
    'whole_actual_canonical_five_notes_root_read':True,'whole_main_mathematical_argument_root_read':True,
    'actual_main_body_root_read_literal_LF_ranges':[[1,90],[91,165],[166,247]],
    'whole_core_root_read':True,'whole_native_source_application_ledger_root_read':True,
    'source_ledger_read_literal_LF_ranges':[[1,370],[371,750],[751,1118]],
    'whole_generated_TEX_separately_root_read':False,'native_paper_appended_source_section_root_read':True,
    'public_main_argument_identical_to_completed_native_main':True,
    'extended_primary_transcripts_private_inputs_logs_databases_uploaded':False,
    'canonical_sha256':sha(canonical),'argument_sha256':sha(D / 'P16.5-argument.md'),
    'core_sha256':sha(D / 'P16.5-core.md'),'source_sha256':sha(D / 'P16.5-paper.tex'),
    'pdf_sha256':sha(D / 'P16.5-paper.pdf'),'PDF_pages':pages,'local_builds':builds,
    'overfull_diagnostics':log.count('Overfull'),'undefined_diagnostics':log.count('Undefined'),
    'actual_visual_pages':[],'native_compiler_success_observed':False,
    'scope':'Unreviewed full-big envelope and signed-domain obstruction; reconstructed all-big surface cone; actual equation only for point blowups of projective space with L=dH+aE, d,a>0; numerical-zero equation and nonconstant zero-volume counterexample. Exact original remains open.',
    'existing_P16_4_editor_modified_or_new_tab_opened':False
}
(D / 'publication-preparation.json').write_text(json.dumps(binding,ensure_ascii=False,indent=2)+'\n')
(D / 'README.md').write_text('This reader preserves the completed native main mathematical argument and canonical PARTIAL result. Its PDF is built from the main argument only. The source ledger provides versioned coordinates and applications; referenced private evidence files and raw transcripts are not part of this public reader. The actual ample grant is publicly available in the round-92 P16.1 reader. No original completion or independent acceptance is claimed. Local compilation checks presentation only.\n')
print(json.dumps({'reader':str(D),'pages':pages,'binding':binding},indent=2))
