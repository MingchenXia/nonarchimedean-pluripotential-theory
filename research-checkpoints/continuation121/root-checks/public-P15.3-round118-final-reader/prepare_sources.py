"""Copy only the four permitted public caches and record literal LF coordinates."""
from pathlib import Path
import hashlib
import json
import shutil

ROOT = Path(__file__).resolve().parent
CACHE = Path('/workspace/research/shared-sources')
SOURCES = [
 ('drwnxz', '2309.07584v3', '48b82ded9de9d2fee8d2c525129b1f176bbfc87dfa67f7ac4bfe9b23eba94e83', '203fcf50f30ff047be9557db66d9f83473e996ea3cc943f652db0b6bd9da802e'),
 ('xia', '2112.04290v2', '0847fc4313e630946e8ff122ab2de587185eb9067d6c3efe2a65dfcfc8e72f2f', 'd59c0231ec64871b6a21657bcc3a952af8b2e9c975eee07db1d99f0ef4cf7273'),
 ('cao', '1210.5692v1', '17717664b0ae2b154e76e2ecb68c9f63f09dc74be6f25bac7f04b7ee0103b0d6', '1bae7bf39d69c41451507e29d908977cb4599bf0b10216eb8b8295c7ba769fce'),
 ('chpw', '1508.03922v5', '8217255c74b4402b6e6a3167db1a6fd8f539056029d82b13556b82828b191a0c', '5ff42d0b3c3c0f0aca4af9fccafdfc96f9e60a30e46cb64fcf9a59b45fcf2c14'),
]
RANGES = {
 'drwnxz': [
  ('version', 1, 20), ('standing_domain_potentials_and_descent', 226, 263),
  ('analytic_singularities_and_subtraction_proof', 271, 333),
  ('gentleness_and_modification_domain', 338, 385),
  ('gentle_regularization', 398, 411),
  ('class_volume_definition', 494, 502),
  ('flag_valuation_realization_and_bodies_with_proofs', 561, 691),
  ('one_dimensional_volume_base_case', 693, 711),
  ('partial_definition_and_divisorial_identity_with_proof', 852, 894),
  ('volume_proof_reduction', 939, 963),
  ('volume_proof_induction', 1139, 1415),
 ],
 'xia': [
  ('version', 1, 14), ('section_ideal_construction_and_positive_volume_domain', 67, 105),
  ('ordinary_C_and_I_envelopes_with_proof', 371, 429),
  ('section_volume_and_I_envelope_mass', 476, 494),
  ('I_invariance_and_proof', 1158, 1185),
  ('zero_volume_limit_and_conjecture', 1623, 1637),
  ('Chebyshev_auxiliary_more_singular_Kahler_potential', 1824, 1840),
 ],
 'cao': [
  ('version', 1, 17), ('current_potentials_approximations_products_and_comparison_proof', 162, 279),
  ('line_bundle_numerical_dimension', 281, 289),
  ('projective_hypersurface_domain_and_restriction_proof', 660, 721),
 ],
 'chpw': [
  ('version_and_internal_date', 1, 65), ('theorem_B', 166, 185),
  ('positive_volume_subvariety_and_ample_construction', 530, 577),
  ('restricted_limit_and_numerical_volume_proofs', 915, 1096),
 ],
}

def sha(raw): return hashlib.sha256(raw).hexdigest()

def main():
 out = ROOT / 'source-extracts'
 out.mkdir(exist_ok=True)
 ledger = {'line_convention': "one-based inclusive coordinates in UTF-8 text.split('\\n'); form feeds retained; terminal empty entry counted", 'sources': []}
 for key, version, pdf_sha, txt_sha in SOURCES:
  rec = {'id': key, 'saved_version': version, 'public_source': 'https://arxiv.org/pdf/' + version, 'files': {}, 'extracts': []}
  for suffix, expected in [('pdf', pdf_sha), ('txt', txt_sha)]:
   src = CACHE / ('P15.3-arxiv-' + version + '-20261004.' + suffix)
   raw = src.read_bytes()
   assert sha(raw) == expected, str(src)
   dest = out / (key + '-' + version + '.' + suffix)
   dest.write_bytes(raw)
   rec['files'][suffix] = {'permitted_cache': str(src), 'local_copy': str(dest.relative_to(ROOT)), 'sha256': sha(raw), 'byte_count': len(raw)}
  lines = (out / (key + '-' + version + '.txt')).read_bytes().decode('utf-8').split('\n')
  rec['LF_split_line_count'] = len(lines)
  for name, start, end in RANGES[key]:
   literal = '\n'.join(lines[start-1:end])
   path = out / (key + '-' + name + '.txt')
   path.write_bytes(literal.encode('utf-8'))
   rec['extracts'].append({'name': name, 'start_LF': start, 'end_LF': end, 'local_file': str(path.relative_to(ROOT)), 'literal_text': literal, 'sha256': sha(literal.encode('utf-8'))})
  ledger['sources'].append(rec)
 (out / 'source-provenance.json').write_text(json.dumps(ledger, ensure_ascii=False, indent=2)+'\n')
 print(json.dumps({'sources': [{'id': s['id'], 'version': s['saved_version'], 'LF_split_line_count': s['LF_split_line_count'], 'extract_ranges': len(s['extracts'])} for s in ledger['sources']], 'hashes_match_supplied': True}, indent=2))

if __name__ == '__main__': main()
