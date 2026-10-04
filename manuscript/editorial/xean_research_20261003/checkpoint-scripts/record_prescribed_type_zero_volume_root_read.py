"""Bind completed drafts and reproduce them in fresh copies; no theorem acceptance."""
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import datetime, hashlib, json, re, shutil, subprocess

ROOT = Path('/workspace/research')
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
primary_path = ROOT / 'shared-sources/prescribed-type-zero-volume-primary-read-20261004.json'
primary = json.loads(primary_path.read_text())
assert sha(primary_path) == '4c487e9393a34a5a95e3eafa72d672065cac13e9940350b63a93004ae01e11f4'
assert primary['all_selected_complete_bodies_directly_root_read_or_exact_unchanged_prior_read_reused']
proposal = ROOT / 'P15-prescribed-type-zero-volume-proposal-20261004.md'
assert sha(proposal) == '6826da400d0ddc0f3ebde3f15ceaed4afb0f89a950e73ed40ec9228a4ed97d09'

def check_one(spec):
    atom, relative, core_name, expected_main, core_lf, tex_lf = spec
    campaign = ROOT / 'campaigns' / relative
    result = json.loads((campaign / 'run.json').read_text())['campaign']['result']
    workspace = Path(result['workspace'])
    review = Path(str(campaign) + '-review')
    freeze = json.loads((review / 'freeze.json').read_text())
    binding = json.loads((review / 'source-artifact-binding.json').read_text())
    argument = workspace / (atom + '-argument.md')
    core = workspace / core_name
    tex = workspace / (atom + '-partial.tex')
    status = workspace / 'status.json'
    assert sha(argument) == expected_main == freeze['main_argument_sha256']
    assert freeze['declared_proof_sha256'] == expected_main
    assert sha(tex) == freeze['source_tex_sha256']
    assert sha(status) == freeze['source_status_sha256']
    assert sha(review / 'argument.md') == freeze['argument_sha256'] == binding['review_argument_sha256']
    assert sha(review / 'freeze.json') == binding['original_freeze_sha256']
    assert argument.read_text().startswith(core.read_text())
    review_text = (review / 'argument.md').read_text()
    assert argument.read_text() in review_text and proposal.read_text() in review_text
    assert len(core.read_text().split('\n')) == core_lf
    assert len(tex.read_text().split('\n')) == tex_lf
    native_input = json.loads((campaign / 'input.json').read_text())
    assert native_input == json.loads((workspace / 'input.json').read_text())
    assert native_input['notes'] == [] and result['candidate'] is False
    settings = json.loads((review / 'settings.json').read_text())
    assert settings['profiles']['default'] == {'provider': 'openai-codex', 'model': 'gpt-6.1-sol', 'reasoning': 'xhigh'}
    seen = set()
    for note in result['notes']:
        assert set(note) == {'id', 'summary', 'detailedSummary', 'text', 'support'}
        assert note['id'] not in seen and set(note['support']) <= seen
        seen.add(note['id'])
    for unit in primary['primary_units']:
        source = Path(unit['source_text'])
        assert sha(source) == unit['source_text_sha256']
        chunk = b'\n'.join(source.read_bytes().split(b'\n')[unit['first_lf_line']-1:unit['last_lf_line']])
        assert chunk.decode() == unit['body']
        assert hashlib.sha256(chunk).hexdigest() == unit['raw_sha256']
        assert chunk.decode() in argument.read_text() and chunk.decode() in native_input['assignment']
    audit = json.loads((workspace / 'source-audit.json').read_text())
    records = audit if isinstance(audit, list) else audit['source_units']
    sources = []
    for u in records:
        p = Path(u.get('file', u.get('source_path')))
        lo, hi = u.get('lf_start', u.get('first_LF')), u.get('lf_end', u.get('last_LF'))
        chunk = b'\n'.join(p.read_bytes().split(b'\n')[lo-1:hi])
        assert hashlib.sha256(chunk).hexdigest() == u['observed_sha256']
        assert chunk.decode() in argument.read_text()
        if u.get('supplied_sha256'): assert u['supplied_sha256'] == u['observed_sha256']
        if u.get('artifact'): assert (workspace / u['artifact']).read_bytes() == chunk
        sources.append({'source': str(p), 'first_LF': lo, 'last_LF': hi,
                        'raw_sha256': u['observed_sha256'], 'literal_body_rebound': True,
                        'root_read': 'Exact unchanged prior full primary read reused' if u.get('supplied_sha256') else 'Additional full range directly read in this turn (overlaps supplemented by exact prior read)'})
    author_manifest = json.loads((workspace / 'artifact-manifest.json').read_text())
    manifest_files = author_manifest.get('files', author_manifest)
    for name, item in manifest_files.items():
        assert (workspace / name).stat().st_size == item['bytes']
        assert sha(workspace / name) == item['sha256']
    check = ROOT / 'root-checks' / ('prescribed-type-zero-volume-' + atom + '-phase1')
    check.mkdir(exist_ok=False)
    canonical = check / 'canonical-result-record.json'
    canonical.write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
    local_notes = workspace / ('notes.json' if atom == 'P15.1' else 'native-notes.json')
    local = json.loads(local_notes.read_text())
    record = {
        'recorded_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
        'state': 'Completed draft fully read with exact source-body reuse; independent review running; no theorem accepted.',
        'atom': atom, 'main_argument': str(argument), 'main_argument_sha256': sha(argument),
        'new_mathematical_core': str(core), 'new_core_sha256': sha(core),
        'all_new_core_LF_entries_directly_read': core_lf,
        'all_author_TEX_LF_entries_directly_read': tex_lf, 'source_tex_sha256': sha(tex),
        'all_actual_canonical_note_texts_directly_read': sorted(seen),
        'canonical_result_record_sha256': sha(canonical),
        'local_notes_equal_canonical': local == {'notes': result['notes'], 'candidate': result['candidate']},
        'local_notes_not_assumed_canonical': True,
        'review_task_settings_freeze_binding_fully_read': True,
        'review_argument_sha256': sha(review / 'argument.md'),
        'review_freeze_sha256': sha(review / 'freeze.json'),
        'review_binding_sha256': sha(review / 'source-artifact-binding.json'),
        'source_status_sha256': sha(status), 'decoded_original_inputs_equal': True,
        'author_audits_and_all_build_scripts_fully_read': True,
        'all_source_appendix_bodies_bound_to_complete_primary_reads': sources,
        'original_primary_read_record': str(primary_path), 'original_primary_read_record_sha256': sha(primary_path),
        'scoped_standard_foundations': 'BEGZ actual NPP; DDNL pseudoeffective mixed mass; Vu v3 admissible Dirichlet/IBP and relative finite-energy convexity; Vu constant-smooth-relative-current lower semicontinuity; compact Kahler ddc lemma. P15.1 additionally local weighted bounded BT/capacity convergence. Printed half-factor defects preserved and correctly handled in new arguments.',
        'manuscript_conversion_issue': 'P15.2 Condition (*) was parsed as emphasis across two occurrences; publication copy must restore literal stars by two exact cosmetic replacements.' if atom == 'P15.2' else None,
        'all_original_atoms_still_open': True,
    }
    (check / 'complete-read-before-review.json').write_text(json.dumps(record, ensure_ascii=False, indent=2)+'\n')
    copy = check / 'reproduction'
    shutil.copytree(workspace, copy)
    scripts = ['build.py'] if atom == 'P15.1' else ['build.py', 'finalize.py', 'verify_artifacts.py']
    executions = []
    for script in scripts:
        run = subprocess.run(['python', script], cwd=copy, capture_output=True, text=True)
        (check / (script + '.stdout.txt')).write_text(run.stdout)
        (check / (script + '.stderr.txt')).write_text(run.stderr)
        executions.append({'argv': ['python', script], 'cwd': str(copy), 'returncode': run.returncode})
        assert run.returncode == 0, run.stderr
    for p in (argument, core, tex): assert sha(copy / p.name) == sha(p)
    assert sha(argument) == expected_main and sha(tex) == freeze['source_tex_sha256']
    repro = {'completed_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
             'commands': executions, 'success': True, 'frozen_author_proof_and_TEX_unchanged': True,
             'fresh_generated_proof_and_TEX_byte_identical': True,
             'copied_proof_sha256': sha(copy / argument.name), 'copied_TEX_sha256': sha(copy / tex.name),
             'copied_pdf_sha256': sha(copy / (atom + '-partial.pdf')),
             'diagnostic_build_only_not_analytic_certification': True,
             'no_private_native_transcript_or_whole_primary_pdf_uploaded': True}
    (check / 'reproduction-result.json').write_text(json.dumps(repro, indent=2)+'\n')
    print(json.dumps({'atom': atom, 'phase1': str(check), 'reproduction_success': True,
                      'independent_review_pending': True}), flush=True)

specs = [
    ('P15.1', 'round-29/P15.1-prescribed-type-zero-volume-energy', 'P15.1-proof.md', '136df3a9d0718ecd41ae81fef449786b7d080ac7d9b3f66f68bb1c102538d23f', 525, 1148),
    ('P15.2', 'round-30/P15.2-prescribed-type-zero-volume-operator', 'P15.2-main.md', '16c3b97e5184196af0d94ca250d20bf02ddf0540e962145057683653a88319e6', 346, 794),
]
with ThreadPoolExecutor(max_workers=2) as pool:
    list(pool.map(check_one, specs))
