"""Bind completed root reads to immutable final bytes; no model or export."""
from pathlib import Path
import datetime
import difflib
import hashlib
import json

root = Path('/workspace/research/root-checks')
reader = root / 'public-envelope-round-37-final-reader'
preliminary = root / 'public-envelope-round-37-preliminary-reader'
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
stamp = datetime.datetime.now(datetime.timezone.utc).isoformat()
core = reader / 'P03.1-argument.md'
assert sha(core) == 'e196ba45167023649da0b63a51da3d1af6de9a2325fb1ca9bb2bf4cf29d2de79'
assert sha(preliminary / core.name) == '1696846e37a7a6369699c619aa58b333e519ba9f9cf39590fc5adb7f6cfd1870'
canon = json.loads((reader / 'canonical-result.json').read_text())
assert canon['candidate'] is False and [n['id'] for n in canon['notes']] == ['n1','n2','n3']
seen = set()
for n in canon['notes']:
    assert set(n['support']) <= seen
    seen.add(n['id'])
opcodes = [{'operation': tag, 'preliminary_zero_based_half_open': [i,j],
            'final_zero_based_half_open': [k,l]}
           for tag,i,j,k,l in difflib.SequenceMatcher(
               a=(preliminary / core.name).read_text().splitlines(keepends=True),
               b=core.read_text().splitlines(keepends=True), autojunk=False).get_opcodes()]
record = {
    'recorded_utc': stamp,
    'full_argument_read': True,
    'argument_read_units': ['Preliminary LF1-145', 'Preliminary LF146-285', 'Preliminary LF286-408',
                            'Entire final unified diff, including all changed blocks, read untruncated around 11:30 UTC',
                            'Final LF255-368 reread, including entire irreducible pinching, around 11:46 UTC'],
    'final_argument_byte_identical_to_preliminary': False,
    'read_byte_mapping': opcodes,
    'all_actual_canonical_notes_read': True,
    'actual_note_ids': [n['id'] for n in canon['notes']],
    'actual_note_fields_read': ['text', 'summary', 'detailedSummary', 'support'],
    'local_notes_view_not_assumed_identical': True,
    'full_TeX_read': True,
    'TeX_read_units': ['Final LF1-180', 'Final LF181-360', 'Final LF361-end'],
    'full_source_provenance_and_checked_applications_read': True,
    'all_reproduced_helpers_fully_read': True,
    'unexecuted_make_notes_helper_not_claimed_fully_read': True,
    'reproduction_result_sha256': sha(reader / 'reproduction-result.json'),
    'argument_sha256': sha(core),
    'canonical_result_sha256': sha(reader / 'canonical-result.json'),
    'TeX_sha256': sha(reader / 'P03.1-paper.tex'),
    'source_provenance_sha256': sha(reader / 'source-provenance.json'),
    'published_foundations_hypotheses_checked': True,
    'new_application_reconstruction': 'Entire proof reconstructed: perfected/reduced/normalized curve homeomorphisms, anchored directed finite maxima with literal two-sided local boundedness and absolute boundary extension; all analytic extensions and curve tests; full semipositive-real-PL class constancy on actual proper connected boundaryless fibres; finite field extension descent without a rational ground-field section, projective bundles and fibre infima; normal and cusp products; split-branch, irreducible bidisc point-pinching and nonsplit-node open-factor counterexamples. New pinching checked as a bounded strict-affinoid realization, finite birational normalization, conductor and analytic equal-residue germ kernel, seminormality and complete global LFS obstacle estimates. No independent acceptance claimed.',
    'source_original_PDF_visual_checks': ['Thuillier PDF76: exact Proposition3.1.8(iii) locally bounded family',
                                          'Berkovich PDF125/printed128: proper torsion degree-zero connectedness comparison',
                                          'Berkovich PDF66/printed69: Proposition3.5.8 smooth analytification'],
    'relative_boundary_equality_hypothesis': 'Equality in relative boundary composition requires locally separated base-to-field map; the good separated curve bases here satisfy it. Arbitrary scalar projections are not claimed open.',
    'paper_first_page_visual_check': 'Root fresh PDF first page viewed: legible prose and formulae without clipping.',
    'native_editor_verified': False,
    'independent_review_launched': False, 'accepted': False, 'original_atom_closed': False,
    'record_is_read_and_execution_evidence_not_a_proof_certificate': True
}
for filename, data in [
    ('complete-root-read.json', record),
    ('native-request-unresponsive.json', {
        'recorded_utc': stamp, 'source': str(reader / 'P03.1-paper.tex'),
        'source_sha256': sha(reader / 'P03.1-paper.tex'),
        'requested_tools': ['codex_app.open_in_codex', 'codex_app.compile_latex_document'],
        'functions_exec_cell': '1568', 'request_returned_diagnostics': False,
        'cell_terminated': True, 'termination_output': 'Script terminated',
        'native_compilation_verified': False, 'editor_opening_confirmed': False,
        'editor_close_command_invoked': False, 'source_preserved': True,
        'limitation': 'Both requests remained unresponsive; no compiler or handler diagnostics returned. Local TeX reproduction is separately recorded.'
    })]:
    p = reader / filename
    assert not p.exists()
    p.write_text(json.dumps(data, indent=2) + '\n')
    print(filename, sha(p))
