"""Own paragraph and whole-body coverage locators, not a proof verifier."""
import hashlib
import json
from pathlib import Path

root = Path(__file__).resolve().parent
rows = json.loads((root / 'frozen-bindings-verified.json').read_text())
requests = [json.loads(s) for s in (root / 'reader-ranges.jsonl').read_text().split('\n') if s]
parallel = {7: 6, 13: 12, 19: 18}
grant_bodies = {0, 2, 4, 6, 7, 12, 13, 18, 19}
grant_annotations = {1, 3, 5, 8, 9, 14, 15, 22, 23, 24}
whole = []
for r in rows:
    if r['kind'] != 'math':
        continue
    index = r['index']
    if index in parallel:
        d = json.loads((root / f'delta-math-{index:02}.json').read_text())
        method = {'type': 'lossless_already-read_token_dictionary_plus_all_literal_tokens',
                  'base_index': parallel[index], 'token_count': d['whole_tokens'],
                  'exact_referenced_tokens': d['exact_referenced_tokens'],
                  'literal_tokens': d['literal_tokens'],
                  'original_whitespace_reconstruction': d['byte_exact_reconstruction']}
    else:
        spans = [[s['start'], s['end']] for s in requests if s['kind'] == 'math'
                 and s['index'] == index and s['coordinate'] == 'byte']
        method = {'type': 'bounded_direct_display', 'requested_spans': spans,
                  'display_attestation': 'Whole displayed content read; initial truncations repaired separately in evidence report'}
    whole.append({'index': index, 'filename': Path(r['path']).name,
                  'bytes': r['actual_bytes'], 'sha256': r['actual_sha256'],
                  'literal_LF': r['actual_LF'], 'method': method,
                  'role': ('qualified_whole_grant_body' if index in grant_bodies else
                           'bound_grant_qualification_or_acceptance_data' if index in grant_annotations else
                           'source_ledger_or_material_scope_DATA_not_an_additional_grant' if index < 25 else
                           'unreviewed_data_under_audit')})

source = (root / 'reproduction' / 'argument.md').read_text()
section = 'front matter'
paragraphs = []
position = 0
for number, text in enumerate(source.split('\n\n'), 1):
    if text.startswith('# '):
        section = text.split('\n', 1)[0][2:]
    if section.startswith(('Scope', 'Quote-free')):
        treatment = 'source-application-ledger.md and reconstructed-proof.md: Qualified envelope and operator consequences'
    elif section.startswith('Reproducibility'):
        treatment = 'evidence-report.md and whole-proof-coverage.md'
    else:
        treatment = 'reconstructed-proof.md: ' + section
    start = source.count('\n', 0, position) + 1
    end = start + text.count('\n')
    paragraphs.append({'block': number, 'section': section, 'LF_start': start,
                       'LF_end': end, 'sha256': hashlib.sha256(text.encode()).hexdigest(),
                       'first_text': text[:180], 'treatment': treatment,
                       'claim_check': 'See explicit subclaim table and independent proof; locator itself is not mathematical evidence'})
    position += len(text) + 2
actual_row = next(r for r in rows if r['kind'] == 'math' and r['index'] == 32)
actual = json.loads(Path(actual_row['path']).read_text())
assert len(whole) == 33 and len(paragraphs) == 102 and len(actual['notes']) == 6
result = {'status': 'Independent manual proof coverage with exact machine locators',
          'whole_mathematical_bodies': whole,
          'new306_parallel_argument_blocks': paragraphs,
          'actual_FINAL_notes': [{'id': n['id'], 'summary': n['summary'],
                                 'text_sha256': hashlib.sha256(n['text'].encode()).hexdigest(),
                                 'support': n['support']} for n in actual['notes']],
          'saved_expansions_distinct': True,
          'mathematical_verdict': 'PASS within unchanged scoped hypotheses',
          'source_application_verdict': 'PASS for current essential applications; historical FAIL retained',
          'evidence_verdict': 'PASS for supplied bounded artifacts and own reproduction; universal past history INCONCLUSIVE',
          'candidate': False, 'original_P05_1': 'OPEN', 'original_P05_2': 'OPEN'}
(root / 'whole-proof-coverage.json').write_text(json.dumps(result, indent=2, ensure_ascii=False) + '\n')
print('whole bodies', len(whole), 'paragraphs', len(paragraphs), 'actual FINAL notes', len(actual['notes']))
