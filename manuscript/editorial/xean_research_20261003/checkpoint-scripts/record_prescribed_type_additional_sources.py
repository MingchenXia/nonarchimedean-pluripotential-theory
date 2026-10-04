"""Preserve fresh primary-source authentication and harmless review qualifications."""
from pathlib import Path
import datetime, hashlib, json

ROOT = Path('/workspace/research')
BASE = ROOT / 'shared-sources'
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
units = []
specs = [
    ('DGMS-real-homotopy-1975-stonybrook-20261004', [(1,46),(861,1064)],
     'Compact Kahler hypotheses, complete identities leading to Lemma 5.11, its full printed proof, and real-form Remark 5.14. These bodies were directly read in full; source OCR is retained literally.'),
    ('GZ-intrinsic-capacities-JGA05-20261004', [(1,62),(347,680)],
     'Kahler background and complete selected capacity section, including Proposition 3.6 sublevel estimate, bounded decreasing Proposition 3.7 with full proof, Corollary 3.8 quasicontinuity, and Proposition 3.10 local/global capacity comparison with full printed proof. References inside the source remain standard literature foundations, not newly reconstructed proofs.')]
for stem, ranges, scope in specs:
    provenance = json.loads((BASE / (stem + '-provenance.json')).read_text())
    text = Path(provenance['text_path'])
    assert sha(text) == provenance['text_sha256']
    assert sha(provenance['pdf_path']) == provenance['pdf_sha256']
    lines = text.read_text().split('\n')
    assert len(lines) == provenance['literal_LF_entries']
    for start, end in ranges:
        body = '\n'.join(lines[start-1:end])
        units.append({'id': stem + '-LF' + str(start) + '-' + str(end),
                      'source_provenance': provenance, 'first_LF_entry': start,
                      'last_LF_entry': end, 'literal_body': body,
                      'literal_body_sha256': hashlib.sha256(body.encode()).hexdigest(),
                      'complete_selected_body_directly_read': True, 'scope': scope})
record = {'recorded_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
          'units': units,
          'DGMS_authentication': 'The earlier IAS HTTP403 was preserved. A fresh public Stony Brook author-hosted copy now authenticates Lemma5.11 and its complete printed proof. A smooth real cohomologically zero closed (1,1) form on compact Kahler X is d- and dc-closed and therefore ddc of a smooth real function, with the fixed scalar normalization adjusted.',
          'GZ_qualification': 'Proposition3.7 itself assumes bounded potentials. For general decreasing quasi-psh functions in one fixed smooth background, first choose a dominating Kahler form, use bounded truncations and Proposition3.7, then remove the sublevel set using Proposition3.6. Proposition3.10 compares local and global capacities; Corollary3.8 supplies quasicontinuity. This is the standard foundation used in the reviewed local bounded application.',
          'Vu_qualification': 'Vu2005.13241v3 Theorem3.3 has bounded product factors and possibly unbounded comparison potentials. The reviewed nonpluripolar applications first truncate all local product potentials and then exhaust their simultaneous finite loci. No unbounded-factor strengthening of that theorem is asserted.',
          'cutoff_qualification': 'The strict comparison locus contains the nonzero locus of the cutoff; the closed support can meet its zero boundary. Publication uses nonzero locus where that distinction matters.',
          'scope_change': False, 'substantive_proof_repair': False,
          'frozen_author_and_review_files_modified': False,
          'whole_primary_PDFs_or_texts_for_GitHub': False,
          'review_operations': ['d1fe9a0a-23d5-4624-a3ae-1ac6be40bb3e','f4f996fa-eef0-43a2-bded-bcbfd96cd0b7'],
          'full_original_atoms_solved': []}
path = BASE / 'prescribed-type-additional-primary-read-20261004.json'
assert not path.exists()
path.write_text(json.dumps(record, ensure_ascii=False, indent=2)+'\n')
print(json.dumps({'path': str(path), 'sha256': sha(path), 'units': len(units), 'scope_change': False}))
