"""Bind the successful R32 rerun with its expected PDF metadata difference.

The original recorder expected byte identity of an execution audit containing
the PDF digest. Preserve that failed assertion and certify only the actual
byte-identical mathematical core, TEX and primary annex.
"""
from pathlib import Path
import datetime, hashlib, json

ROOT = Path('/workspace/research')
check = ROOT / 'root-checks/minimum-reference-zero-volume-P15.2-phase1'
workspace = ROOT / 'campaigns/round-32/P15.2-minimum-reference-full-mass-operator/artifacts/codex-UNkbGs'
copy = check / 'reproduction'
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
failure = check / 'reproduction-v1-assertion-failure.json'
assert not failure.exists()
failure.write_text(json.dumps({
    'recorded_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
    'script': str(ROOT / 'record_minimum_reference_zero_volume_root_read.py'),
    'script_sha256': sha(ROOT / 'record_minimum_reference_zero_volume_root_read.py'),
    'failure': 'Expected byte identity of full argument, but its execution-audit paragraph embeds the newly compiled PDF digest.',
    'both_build_commands_succeeded': True,
    'author_inputs_and_artifacts_not_modified': True,
    'mathematical_proof_repair': False,
}, indent=2) + '\n')
pins = {
    'P15.2-argument.md': '73ce427df484251a2caf8f49a47291ff62bbc4107c322f77701c646a3b483815',
    'P15.2-proof.md': '9a30d5d090fbd19bdc75ac32f330934d13109c6a66e3953ed3a045f2918787b2',
    'P15.2-partial.tex': 'acf53110f1e934c0012e8351a3e518c30f12096d7fe316951efe985a82d66739',
}
for name, pin in pins.items():
    assert sha(workspace / name) == pin
for name in ['P15.2-proof.md', 'P15.2-partial.tex', 'source-annex.md']:
    assert (workspace / name).read_bytes() == (copy / name).read_bytes()
old_pdf, new_pdf = sha(workspace / 'P15.2-partial.pdf'), sha(copy / 'P15.2-partial.pdf')
old_audit, new_audit = (workspace / 'execution-audit.md').read_text(), (copy / 'execution-audit.md').read_text()
assert old_audit.count(old_pdf) == 1 and new_audit == old_audit.replace(old_pdf, new_pdf)
old_arg, new_arg = (workspace / 'P15.2-argument.md').read_text(), (copy / 'P15.2-argument.md').read_text()
assert old_arg.count(old_pdf) == 1 and new_arg == old_arg.replace(old_pdf, new_pdf)
audit = json.loads((copy / 'build-audit.json').read_text())
assert all(c['returncode'] == 0 for c in audit['commands'])
assert audit['pdf_twice_compiled'] and audit['pdf_text_checks']['all_found']
assert (check / 'package_notes.py.stderr.txt').read_text() == ''
record = {
    'completed_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
    'commands': [{'argv': ['python', s], 'cwd': str(copy), 'returncode': 0} for s in ['build.py', 'package_notes.py']],
    'success': True, 'frozen_author_proof_and_TEX_unchanged': True,
    'fresh_generated_mathematical_core_TEX_and_literal_annex_byte_identical': True,
    'fresh_generated_full_argument_byte_identical': False,
    'full_argument_only_difference': 'New PDF digest in execution observation; exact single substitution verified.',
    'author_pdf_sha256': old_pdf, 'copied_pdf_sha256': new_pdf,
    'author_full_argument_sha256': sha(workspace / 'P15.2-argument.md'),
    'copied_proof_sha256': sha(copy / 'P15.2-proof.md'),
    'copied_TEX_sha256': sha(copy / 'P15.2-partial.tex'),
    'copied_full_argument_sha256': sha(copy / 'P15.2-argument.md'),
    'preserved_v1_assertion_failure_sha256': sha(failure),
    'diagnostic_build_only_not_analytic_certification': True,
}
out = check / 'reproduction-result.json'
assert not out.exists()
out.write_text(json.dumps(record, indent=2) + '\n')
print(json.dumps({'atom': 'P15.2', 'reproduction_success': True, 'only_difference': record['full_argument_only_difference']}))
