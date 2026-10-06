from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, re, shutil, subprocess

R = Path('/workspace/research')
K = R / 'root-checks'
C = R / 'campaigns/round-145/P16.5-original-big-class-relative-floor-closure-and-entire-equation-research-retry1'
W = C / 'artifacts/codex-Caywwc'
D = K / 'public-P16.5-round145-partial-equation-reader'
if D.exists():
    assert not list(D.iterdir()), 'Resume only the empty directory from the failed pre-publication byte assertion.'
else:
    D.mkdir(parents=True, exist_ok=False)
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
canonical = K / 'P16.5-round145-completed-author-result-PUBLIC-20261006.json'
r = json.loads(canonical.read_text())
assert sha(canonical) == 'b234d34ec332483a2f58337bda9e2aa3edf4a2a68e1081212558e2590d9126d1'
assert r['candidate'] is False and len(r['notes']) == 5
f = json.loads((C / 'freeze.json').read_text())
assert sha(C / 'input.json') == f['input_sha256']
assert (W / 'input-original.json').read_bytes() == (W / 'input.json').read_bytes()
decoded = json.loads((C / 'input.json').read_text())
assert json.loads((W / 'input-original.json').read_text()) == decoded
assert json.loads((W / 'task-original.json').read_text()) == decoded['task']
assert (W / 'assignment-original.txt').read_text() == decoded['assignment']
assert len((W / 'P16.5-paper.md').read_text().splitlines()) == 452
assert len((W / 'source-ledger.md').read_text().splitlines()) == 58
for name in ['P16.5-paper.md','P16.5-paper.tex','P16.5-paper.pdf','source-ledger.md']:
    shutil.copyfile(W / name, D / name)
info = subprocess.run(['pdfinfo',str(D / 'P16.5-paper.pdf')],capture_output=True,text=True,check=True).stdout
pages = int(re.search(r'^Pages:\s+(\d+)',info,re.M).group(1))
assert pages == 16
log = (W / 'P16.5-paper.log').read_text()
b = {'recorded_utc':datetime.now(timezone.utc).isoformat(),
    'classification':'Completed native author PARTIAL mathematical paper; no independent acceptance and no original closure.',
    'author':'Xean native Codex gpt-6.1-sol xhigh','candidate':False,'original_closed':False,
    'canonical_author_result':str(canonical),'canonical_sha256':sha(canonical),
    'whole_all_five_canonical_notes_root_read':True,
    'whole_452_line_standalone_argument_root_read':True,
    'whole_58_line_source_application_ledger_root_read':True,
    'whole_standalone_tex_separately_root_read':False,
    'worker_input_original_byte_identical_to_native_worker_input':True,
    'worker_input_sha256':sha(W / 'input.json'),
    'worker_input_decoded_entire_input_equal_to_campaign_input':True,
    'campaign_and_worker_json_serialization_byte_identical':False,
    'decoded_task_preserved':True,'decoded_assignment_preserved':True,'decoded_notes_preserved':True,
    'frozen_input_sha256':f['input_sha256'],'unchanged_original_task':True,
    'pages':pages,'root_reran_unchanged_build':False,
    'overfull':log.count('Overfull'),'warnings':log.count('Warning'),'undefined':log.lower().count('undefined'),
    'independent_review':False,'accepted_count_change':0,'existing_editor_unchanged':True,
    'actual_visual_pages':[],'native_compile_success_observed':False,
    'scope':'Conditional actual relative-floor closure, reconstructed ample divisorial nonnegligibility, conditional section-volume entire energy/operator and finite-model target attainment; separate zero numerical-class quotient equation. Full arbitrary-dimensional arbitrary-support P16.5 remains open.',
    'first_unresolved_foundation':'Relative arbitrary-field multiplier-ideal generation; proposed independent compactification/field-descent repair192 is under review148, not granted to this completed paper.',
    'remaining_equation_bridges':['Actual complete moving-series top and positive-product limits against fixed Cartier classes.',
        'Missing-rank lower energy transfer at fixed original continuous obstacles.',
        'Output/target pole-nullness, negligible discrepancy and finite relative moments/contraction.',
        'Uniform absolute continuous-test approximations and exact weighted identification at all E1 bases.',
        'Entire unbounded supporting planes, strong relative integration, arbitrary-target attainment, strict comparison and all-solution uniqueness.'],
    'file_bindings':[{'name':name,'bytes':(D / name).stat().st_size,'sha256':sha(D / name),'byte_identical_to_completed_native_author':True}
        for name in ['P16.5-paper.md','P16.5-paper.tex','P16.5-paper.pdf','source-ledger.md']]}
assert b['overfull'] == b['warnings'] == b['undefined'] == 0
(D / 'publication-binding.json').write_text(json.dumps(b,indent=2)+'\n')
record = K / 'P16.5-round145-completed-partial-and-original-scope-record-20261006.json'
assert not record.exists()
record.write_text(json.dumps(b,indent=2)+'\n')
for n in [1,8,16]:
    subprocess.run(['pdftoppm','-f',str(n),'-l',str(n),'-scale-to','1500','-png','-singlefile',str(D / 'P16.5-paper.pdf'),str(D / f'page-{n}-LOCALONLY')],capture_output=True,check=True)
for name in ['active-work.json','checklist-current.json']:
    p = R / name
    o = json.loads(p.read_text())
    assert len(o['fully_solved_original_atoms']) == 8 and o['remaining_open_original_atoms'] == 34 and o['historical_reviewed_scoped_papers'] == 56
    o['completed_original_big_research145_full_reader'] = b
    o['original_full_big_equation_research145'].update({'observed_status':'completed','candidate':False,'classification':'Completed original author PARTIAL; original remains open.','completed_scope_record':str(record)})
    p.write_text(json.dumps(o,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'reader':str(D),'pages':pages,'classification':'PARTIAL; unreviewed','whole_argument_and_source_ledger_root_read':True},indent=2))
