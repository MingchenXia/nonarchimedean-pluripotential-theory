from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, shutil, subprocess

R = Path('/workspace/research'); K = R/'root-checks'
C = R/'campaigns/round-213/P05.2-original-all-obstacle-after-lossless-input-normalization'
A = C/'artifacts/codex-BatEk6'
D = K/'public-P05.2-continuation282-all-continuous-affine-spaces-and-affine-arrangements'
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
def write(p, v):
    Path(p).write_text(json.dumps(v, ensure_ascii=False, indent=2)+'\n')

assert not D.exists()
final = K/'P05.2-round213-exact-native-model-final-unreviewed-original-continuation282-20261007.json'
native = json.loads(final.read_text())
saved = json.loads((A/'native-notes.json').read_text())
inspection = json.loads((K/'round213-settled-inspection-LOCALONLY.json').read_text())
registered = inspection['campaign']['result']
assert inspection['campaign']['status']=='completed'
assert not native['candidate'] and not saved['candidate'] and not registered['candidate']
assert len(native['notes'])==len(saved['notes'])==len(registered['notes'])==4
differences=[]
for n, s, r in zip(native['notes'], saved['notes'], registered['notes']):
    for key in ['id','summary','detailedSummary','support']: assert n[key]==r[key]
    assert r['text']==n['text']+'\n\nArtifacts: '+str(A)
    differences.append(dict(id=n['id'],different_fields=[key for key in n if n[key]!=s[key]]))
assert all(row['different_fields'] for row in differences)
bindings=[]
for name in ['mathematical-packet-bindings.json','private-primary-packet-bindings.json']:
    for e in json.loads((C/name).read_text()):
        assert sha(e['path'])==e['sha256'] and Path(e['path']).stat().st_size==e['bytes']
        bindings.append(e)
assert len(bindings)==26
manifest=json.loads((A/'artifact-manifest.json').read_text())
for e in manifest:
    assert sha(A/e['file'])==e['sha256'] and (A/e['file']).stat().st_size==e['bytes']
parent_input=json.loads((C/'input.json').read_text()); child_input=json.loads((A/'input.json').read_text())
input_equal=parent_input==child_input
assert input_equal
D.mkdir(); E=D/'evidence'; E.mkdir(); S=E/'root-reproduction'; S.mkdir()
for e in manifest:
    if e['file'].endswith(('.aux','.out','.log','.pdf')) and e['file'].startswith('P05.2-paper.'): continue
    shutil.copyfile(A/e['file'],D/e['file'])
shutil.copyfile(A/'artifact-manifest.json',D/'artifact-manifest.json')
shutil.copyfile(final,E/'exact-native-final.json')
write(E/'registered-native-worker-result.json',registered)
shutil.copyfile(A/'check_continuation282.py',S/'check_continuation282.py')
shutil.copyfile(A/'certificate-input.json',S/'certificate-input.json')
runs=[]
def run(argv,cwd,stem):
    p=subprocess.run(argv,cwd=cwd,capture_output=True,text=True)
    stdout=S/(stem+'.stdout.txt'); stderr=S/(stem+'.stderr.txt')
    stdout.write_text(p.stdout);stderr.write_text(p.stderr)
    runs.append(dict(argv=argv,cwd=str(cwd),exit_code=p.returncode,stdout=str(stdout),stderr=str(stderr)))
    assert p.returncode==0
run(['python',str(S/'check_continuation282.py')],S,'finite-checks')
assert (S/'certificate-output.json').read_bytes()==(A/'certificate-output.json').read_bytes()
run(['pandoc','-f','latex','-t','markdown',str(D/'P05.2-paper.tex'),'-o',str(S/'argument.md')],S,'source-to-markdown')
argument_equal=(S/'argument.md').read_bytes()==(D/'argument.md').read_bytes()
assert argument_equal
for i in [1,2]:
    run(['pdflatex','-no-shell-escape','-interaction=nonstopmode','-halt-on-error','P05.2-paper.tex'],D,f'local-pass{i}')
diagnostics=[l for l in (D/'P05.2-paper.log').read_text(errors='replace').splitlines() if any(w in l for w in ['Warning:','Overfull','Underfull','! '])]
assert not diagnostics
info=subprocess.run(['pdfinfo',str(D/'P05.2-paper.pdf')],capture_output=True,text=True,check=True).stdout
pages=int(next(l for l in info.splitlines() if l.startswith('Pages:')).split(':')[1]);assert pages==11
editor=K/'public-P16-round-46-final-reader/P16.4-paper.tex'
assert sha(editor)=='09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
record=dict(recorded_utc=datetime.now(timezone.utc).isoformat(),atom='P05.2',continuation=282,author_round=213,
    source=str(D/'P05.2-paper.tex'),source_sha256=sha(D/'P05.2-paper.tex'),source_LF_lines=(D/'P05.2-paper.tex').read_bytes().count(b'\n'),
    argument=str(D/'argument.md'),argument_sha256=sha(D/'argument.md'),pdf=str(D/'P05.2-paper.pdf'),pdf_sha256=sha(D/'P05.2-paper.pdf'),pdf_pages=pages,
    entire_source_argument_ledger_scope_and_four_exact_FINAL_and_four_saved_draft_notes_ROOT_read=True,
    exact_FINAL_differs_from_saved_notes=True,saved_note_differences=differences,registered_exact_FINAL_plus_artifacts_suffix_checked=True,
    parent_and_author_input_json_semantically_equal=input_equal,author_input_byte_equal=(C/'input.json').read_bytes()==(A/'input.json').read_bytes(),
    all_22_math_and_4_primary_hashes_and_sizes_match=True,all_four_whole_primaries_ROOT_read_claimed=False,
    all_author_manifest_hashes_and_sizes_match=True,finite_checker_ROOT_read_before_copied_execution=True,
    finite_output_exact=True,finite_checks_certify_continuum=False,latex_to_markdown_exact=argument_equal,markdown_to_latex_reversibility_claimed=False,
    root_commands=runs,local_build_exit_codes=[0,0],local_diagnostics=diagnostics,builtin_compile_not_yet_requested=True,
    mathematical_acceptance=False,original_closed=False,protected_editor_unchanged_open=True,
    scope='UNREVIEWED all-C_b affine full-space theorem with actual real references; affine-arrangement iff disjoint, positive plane-subcycle/transverse-line obstruction. General singular/abstract classification remains open.')
write(D/'root-reproduction-binding-20261008.json',record)
(D/'README.md').write_text('Unreviewed continuation282: all-continuous affine contact and affine arrangements\n\nOriginal P05.2 remains open. The paper proposes genuine global real regularization for all relative continuous convex functions on complete rational affine spaces, all bounded-obstacle contact, and an affine-arrangement classification by pairwise disjointness. General singular/abstract spaces remain outside this sector. ROOT read the whole paper, argument, ledger, scope, actual four-note FINAL and separate four-note saved draft. Saved notes differ from actual FINAL; the exact FINAL and registered result are preserved separately. Whole independent mathematical audit is required. ROOT reproduced the finite arithmetic, exact source-to-Markdown conversion and two clean local builds; these acts imply no mathematical acceptance. Existing protected editor stays open unchanged.\n')
print(json.dumps({k:record[k] for k in ['source','source_sha256','argument_sha256','pdf_sha256','pdf_pages','mathematical_acceptance','original_closed']},indent=2))
