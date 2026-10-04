"""Freeze root reads and reproduce immutable rounds 31/32 in fresh copies.

This records exact scoped proof reads; it does not accept a theorem or close an
original problem. Source ranges reuse the complete primary reads recorded in
the preceding work, including the additional DGMS/GZ authentication.
"""
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import ast, datetime, hashlib, json, re, shutil, subprocess

ROOT = Path('/workspace/research')
SRC = ROOT / 'shared-sources'
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
digest = lambda b: hashlib.sha256(b).hexdigest()
primary = SRC / 'prescribed-type-zero-volume-primary-read-20261004.json'
additional = SRC / 'prescribed-type-additional-primary-read-20261004.json'
assert sha(primary) == '4c487e9393a34a5a95e3eafa72d672065cac13e9940350b63a93004ae01e11f4'
assert sha(additional) == '4b9fbaf4614ec85e3115091cd7d301d3b5f76063ea75cd94e3f4fe93a973e707'
evidence = ROOT / 'P15-minimum-reference-full-evidence-20261004.md'
assert sha(evidence) == '36e1e7369f5bd19e0ba0793809fd3faa4a75e7fc7f2d9cf912de5e8ef291b029'
whole_pins = {
    'BEGZ-0812.3674v2-20261004.txt': '9d52c95247fd7f69194c84df01ef54b4cd98b6e4e35b4f3851f90f04c98a71b0',
    'Xia-1907.06359v1-20261004.txt': '2c88015e60b6da6557c874e25ffad28dc1a6fbe193c4e44c66a244e6cb9f1576',
    'DDNL18-2049-2087-20261004.txt': 'e893fc77346a1608fbfee3006b37c960b1239dbd767d5952d48e13acac3b27e6',
    'Vu-2004.11111v1-20261004.txt': '8c3a83dd2479d61238a68034165be86bdcd610cd364dd21dc6d929b5b011f6a6',
    'Vu-2005.13241v3-20261004.txt': '672cf50a987b46375dc40d6f75baabdaac4634a70bee9f6c99d328ecea1cbb31',
    'DGMS-real-homotopy-1975-stonybrook-20261004.txt': '5481d97fdb0ae210d2affed7f7906f55f9c5c8f2f129197f05a5a035a2028db4',
    'GZ-intrinsic-capacities-JGA05-20261004.txt': '510152dd9c77adde026b0eea3cb3cf007301bc06c7b06046baf39d70ed8f8190',
}
for name, pin in whole_pins.items():
    assert sha(SRC / name) == pin
# The immutable source-audit program's literal list is independently read above.
unit_program = ROOT / 'campaigns/round-31/P15.1-minimum-reference-finite-energy/artifacts/codex-7YBaVo/verify_sources.py'
assert sha(unit_program) == 'aa4b47794fe4212b089c1ca1abfad3e695b2ac30358288c68e51b7d55b4ccd31'
unit_node = next(n for n in ast.parse(unit_program.read_text()).body
                 if isinstance(n, ast.Assign) and any(isinstance(t, ast.Name) and t.id == 'UNITS' for t in n.targets))
units = ast.literal_eval(unit_node.value)
assert len(units) == 24

SPECS = [
    {'round': 31, 'atom': 'P15.1', 'name': 'P15.1-minimum-reference-finite-energy', 'input': 'input.json',
     'input_sha256': 'd908fbc0f6a6f7e747e8d6cea764655501cad2bae927a55cd26209ada5e98f5d',
     'proof': 'f5c7023e427b629962273bddb9644b71de7b9545b574b4062386fb149042be36',
     'tex': '7806e70e013dc5dce55ea2add346fe37c57fd6550f9a7241ddfeae7ff1aff37e', 'tex_lf': 1286,
     'core_files': [('n1.md', 149, 'c487f8aa42bad921ff92d6bfa6e623da95ce55672c193d60b2f65fd7e315bcff'),
                    ('n2.md', 172, '44b0e29a754268d731f08343ef8bd75bdec80ddbc25bd30aa7aaa139b6edff22'),
                    ('n3.md', 132, '2b8b5691ad0733b14fd90b4c2af657967e3d77020584c021e2d3a5edd7c0b46c'),
                    ('n4.md', 86, 'a0da70fe17c7070247cccac2d657449325eb743f0ef5c9e3e73376fbd1ea3509')],
     'scripts': ['build.py'], 'all_read_scripts': ['build.py', 'verify_sources.py', 'coefficient_check.py', 'native_note_texts.py']},
    {'round': 32, 'atom': 'P15.2', 'name': 'P15.2-minimum-reference-full-mass-operator', 'input': 'input-v2.json',
     'input_sha256': '3e43e731e0b49f76334a54a73d6bcd8231e6acbab77431226d443526f0cc7397',
     'proof': '73ce427df484251a2caf8f49a47291ff62bbc4107c322f77701c646a3b483815',
     'tex': 'acf53110f1e934c0012e8351a3e518c30f12096d7fe316951efe985a82d66739', 'tex_lf': 881,
     'core_files': [('P15.2-proof.md', 335, '9a30d5d090fbd19bdc75ac32f330934d13109c6a66e3953ed3a045f2918787b2')],
     'scripts': ['build.py', 'package_notes.py'], 'all_read_scripts': ['build.py', 'package_notes.py', 'checks.py', 'verify_sources.py']},
]

def check_one(spec):
    atom = spec['atom']
    campaign = ROOT / 'campaigns' / f"round-{spec['round']}" / spec['name']
    result = json.loads((campaign / 'run.json').read_text())['campaign']['result']
    workspace = Path(result['workspace'])
    review = Path(str(campaign) + '-review')
    freeze = json.loads((review / 'freeze.json').read_text())
    binding = json.loads((review / 'source-artifact-binding.json').read_text())
    argument = workspace / (atom + '-argument.md')
    tex = workspace / (atom + '-partial.tex')
    assert sha(argument) == spec['proof'] == freeze['main_argument_sha256'] == freeze['declared_proof_sha256']
    assert sha(tex) == spec['tex'] == freeze['source_tex_sha256']
    assert sha(workspace / 'status.json') == freeze['source_status_sha256']
    assert sha(review / 'freeze.json') == binding['original_freeze_sha256']
    assert sha(review / 'argument.md') == freeze['argument_sha256'] == binding['review_argument_sha256']
    assert argument.read_text() in (review / 'argument.md').read_text()
    assert evidence.read_text() in (review / 'argument.md').read_text()
    assert len(tex.read_text().split('\n')) == spec['tex_lf']
    core_records = []
    for name, lines, pin in spec['core_files']:
        p = workspace / name
        assert sha(p) == pin and len(p.read_text().split('\n')) == lines
        assert p.read_text() in argument.read_text()
        core_records.append({'path': str(p), 'sha256': pin, 'all_LF_entries_directly_read': lines})
    if spec['round'] == 31:
        assert argument.read_bytes() == (workspace / 'proof-body.md').read_bytes() + b'\n\n' + (workspace / 'source-annex.md').read_bytes()
        t = ast.parse((workspace / 'native_note_texts.py').read_text())
        assert len(t.body) == 2 and isinstance(t.body[0], ast.Expr)
        assert isinstance(t.body[0].value, ast.Constant) and isinstance(t.body[0].value.value, str)
        a = t.body[1]
        assert isinstance(a, ast.Assign) and len(a.targets) == 1 and isinstance(a.targets[0], ast.Name) and a.targets[0].id == 'TEXTS'
        texts = ast.literal_eval(a.value)
        assert [s + '\n\nArtifacts: ' + str(workspace) for s in texts] == [n['text'] for n in result['notes']]
    else:
        assert argument.read_bytes() == (workspace / 'P15.2-proof.md').read_bytes() + b'\n\n' + (workspace / 'execution-audit.md').read_bytes() + b'\n\n' + (workspace / 'source-annex.md').read_bytes()
    selected = campaign / spec['input']
    assert sha(selected) == spec['input_sha256']
    native_input = json.loads(selected.read_text())
    assert native_input == json.loads((workspace / 'input.json').read_text())
    assert native_input['notes'] == [] and result['candidate'] is False
    settings = json.loads((review / 'settings.json').read_text())
    assert settings['profiles']['default'] == {'provider': 'openai-codex', 'model': 'gpt-6.1-sol', 'reasoning': 'xhigh'}
    seen = set()
    for note in result['notes']:
        assert set(note) == {'id', 'summary', 'detailedSummary', 'text', 'support'}
        assert note['id'] not in seen and set(note['support']) <= seen
        seen.add(note['id'])
    source_records = []
    for name, lo, hi, pin in units:
        raw = b'\n'.join((SRC / name).read_bytes().split(b'\n')[lo-1:hi])
        assert digest(raw) == pin and raw.decode() in argument.read_text()
        assignment = native_input['assignment']
        assert raw.decode() in assignment or json.dumps(raw.decode(), ensure_ascii=False)[1:-1] in assignment
        source_records.append({'file': name, 'first_LF': lo, 'last_LF': hi, 'raw_sha256': pin,
                               'whole_text_sha256': whole_pins[name], 'literal_body_rebound': True,
                               'root_read': 'Exact unchanged complete primary body read in preceding work reused; all new applications directly read in current core.'})
    if spec['round'] == 32:
        quotes = re.findall(r'```text\n(.*?)\n```', native_input['assignment'], re.S)
        archive = json.loads((workspace / 'supplied-quotation-archive.json').read_text())
        assert len(quotes) == len(archive) == 36
        assert all(q == a['text'] and digest(q.encode()) == a['sha256'] for q, a in zip(quotes, archive))
    check = ROOT / 'root-checks' / ('minimum-reference-zero-volume-' + atom + '-phase1')
    check.mkdir(exist_ok=False)
    canonical = check / 'canonical-result-record.json'
    canonical.write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
    local = json.loads((workspace / 'notes.json').read_text())
    record = {
        'recorded_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
        'state': 'Complete scoped author proof and actual canonical notes read; independent review running. No theorem accepted.',
        'atom': atom, 'round': spec['round'], 'main_argument': str(argument), 'main_argument_sha256': sha(argument),
        'all_new_mathematical_core_files_fully_directly_read': core_records,
        'all_author_TEX_LF_entries_directly_read': spec['tex_lf'], 'source_tex_sha256': sha(tex),
        'all_actual_canonical_note_texts_summaries_support_fully_directly_read': sorted(seen),
        'canonical_result_record_sha256': sha(canonical),
        'local_notes_equal_canonical': local == {'notes': result['notes'], 'candidate': result['candidate']},
        'local_notes_not_assumed_canonical': True,
        'native_note_data_module_pure_literal_list_bound_with_artifact_suffix': spec['round'] == 31,
        'review_task_settings_freeze_binding_fully_read': True,
        'review_argument_sha256': sha(review / 'argument.md'), 'review_freeze_sha256': sha(review / 'freeze.json'),
        'review_binding_sha256': sha(review / 'source-artifact-binding.json'),
        'source_status_sha256': sha(workspace / 'status.json'), 'selected_input': str(selected),
        'selected_input_sha256': sha(selected), 'decoded_selected_input_equal_to_worker_input': True,
        'author_audits_and_build_scripts_fully_read': {s: sha(workspace / s) for s in spec['all_read_scripts']},
        'all_24_source_appendix_bodies_bound_to_complete_primary_reads': source_records,
        'primary_read_records': {str(primary): sha(primary), str(additional): sha(additional)},
        'full_dependency_evidence_sha256': sha(evidence),
        'standard_foundations': 'BEGZ actual NPP; DDNL pseudoeffective mixed mass and bounded weighted convergence; Vu v3 relative convexity and correctly normalized bounded admissible IBP; Vu constant-relative-current lower semicontinuity; DGMS compact Kahler ddc lemma; GZ bounded decreasing capacity theorem with sublevel and local/global extensions. New uses are fully proved and read.',
        'manuscript_conversion_issue': 'P15.2 Condition (*) emphasis markers must be restored in a fresh publication copy.' if spec['round'] == 32 else None,
        'full_original_atoms_solved': [], 'original_scope_audit_pending': True,
    }
    (check / 'complete-read-before-review.json').write_text(json.dumps(record, ensure_ascii=False, indent=2) + '\n')
    copy = check / 'reproduction'
    shutil.copytree(workspace, copy)
    executions = []
    for script in spec['scripts']:
        run = subprocess.run(['python', script], cwd=copy, capture_output=True, text=True)
        (check / (script + '.stdout.txt')).write_text(run.stdout)
        (check / (script + '.stderr.txt')).write_text(run.stderr)
        executions.append({'argv': ['python', script], 'cwd': str(copy), 'returncode': run.returncode})
        assert run.returncode == 0, run.stderr
    for p in [argument, tex] + [workspace / x[0] for x in spec['core_files']]:
        assert sha(copy / p.name) == sha(p)
    assert sha(argument) == spec['proof'] and sha(tex) == spec['tex']
    repro = {'completed_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(), 'commands': executions,
             'success': True, 'frozen_author_proof_and_TEX_unchanged': True,
             'fresh_generated_proof_and_TEX_byte_identical': True,
             'copied_proof_sha256': sha(copy / argument.name), 'copied_TEX_sha256': sha(copy / tex.name),
             'copied_pdf_sha256': sha(copy / (atom + '-partial.pdf')),
             'diagnostic_build_only_not_analytic_certification': True}
    (check / 'reproduction-result.json').write_text(json.dumps(repro, indent=2) + '\n')
    print(json.dumps({'atom': atom, 'phase1': str(check), 'reproduction_success': True, 'independent_review_pending': True}), flush=True)

if __name__ == '__main__':
    with ThreadPoolExecutor(max_workers=2) as pool:
        list(pool.map(check_one, SPECS))
