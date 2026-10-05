"""Freeze a successor after the completed round68 diagnosis was read in full."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json

R = Path('/workspace/research')
old = R/'campaigns/round-69/P16.1-public-source-shared-collar-weighted-mass-and-unibranch-equation'
C = R/'campaigns/round-70/P16.1-public-source-smooth-weak-globalization-open-trace-and-unibranch-equation'
S = R/'root-checks/continuation77-smooth-weak-and-countable-regularization-source-reads'
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
write = lambda p,d: Path(p).write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
manifest = json.loads((old/'input-manifest.json').read_text())
assert sha(old/'input.json') == manifest['input_sha256'] == '10c9131ecc30b46e898788cb9a5e34ccef6b8635d9254f9a0df50843518170a0'
assert sha(old/'settings.json') == manifest['settings_sha256']
assert not (old/'campaign.sqlite').exists()
assert not C.exists() and not S.exists()
D = R/'root-checks/public-P16.1-round-68-final-reader'
state = json.loads((D/'root-preservation-and-read-state-continuation77.json').read_text())
assert state['whole_argument_root_read'] and state['all_four_actual_canonical_notes_root_read']
actual = json.loads((D/'canonical-native-result.json').read_text())
assert actual['candidate'] is False
S.mkdir()
units = []
specifications = [
    ('BJ-already-genuine-countable-regularization-complete-proof', 'P16-arxiv-1801.08229-20261004.txt', '1801.08229v4', 6230, 6286,
     'Theorem12.16/Cor12.18 need genuine global membership and genuine limit, not a countable field. Nef approximants vary ample classes; same-class sequence is the ample case.'),
    ('BJ-Hdom-and-fixed-rational-line-bundle', 'P16-arxiv-1801.08229-20261004.txt', '1801.08229v4', 1692, 1704,
     'Definition3.8/Example3.9 bind Hdom(c1(L)) to actual fixed rational bundle FS metrics. Class equality alone for arbitrary metrics is not substituted.'),
    ('BJ-birational-onto-target-EP-complete-proof', 'P16-arxiv-1801.08229-20261004.txt', '1801.08229v4', 2859, 2873,
     'Actual Lemma5.13 requires approaching larger target classes with EP. Apply only to the smooth ample compactification in the proposal, not singular original X.'),
    ('BJ-divisorial-nonnegligibility-complete-proof', 'P16-arxiv-1801.08229-20261004.txt', '1801.08229v4', 2773, 2795,
     'Whole5.6/5.7 proof retains the genuine PSH and bounded-family antecedents.'),
    ('BJ-genuine-upper-envelope-and-class-closure', 'P16-arxiv-1801.08229-20261004.txt', '1801.08229v4', 2797, 2814,
     'Definition5.8/whole5.9 give exact EP and class closure. Smooth EP is separately available; do not declare damped functions globally monotone.'),
    ('Wu-removal-and-boundary-blowup-diagnostic-complete-proofs', 'new-primary-2609.27610v1-20261004.txt', '2609.27610v1', 1146, 1196,
     'Diagnostic Theorem3.31 proof has a nonmonotone damping family. In3.32 the correct effective E has I_Z O=O(-E) and -E relatively ample, not the printed signs. Supply a full corrected proof.'),
    ('Wu-weak-witness-smooth-route-and-original-global-target', 'new-primary-2609.27610v1-20261004.txt', '2609.27610v1', 1885, 1962,
     'Definitions6.1/6.4 and proofs6.2/6.5 expose the actual smooth regularization/removal and singular Runge dependencies. Diagnostic only; original target unchanged.'),
]
for label, filename, version, first, last, scope in specifications:
    src = R/'shared-sources'/filename
    literal = '\n'.join(src.read_bytes().decode('utf-8').split('\n')[first-1:last])
    p = S/(label+'.txt');p.write_text(literal)
    assert p.read_bytes().decode('utf-8') == literal
    units.append({'id':label,'version':version,'source':str(src),'source_sha256':sha(src),
                  'inclusive_one_based_LF':[first,last],'literal_file':str(p),
                  'literal_sha256':sha(p),'selected_literal_body_root_read':True,
                  'whole_primary_body_root_read':False,'scope_and_limits':scope})
write(S/'source-read-record.json',{'recorded_utc':datetime.now(timezone.utc).isoformat(),
      'LF_convention':'UTF-8 bytes decode and split("\\n"), inclusive one-based ranges',
      'units':units,'new_applications_independently_reviewed':False})
previous = json.loads((old/'input.json').read_text())
contexts = list(manifest['embedded_context'])
new_paths = [
    ('Actual completed round68 full proof, candidate=false, diagnostic and unreviewed',D/'P16.1-argument.md'),
    ('Actual completed round68 four canonical notes, candidate=false, diagnostic and unreviewed',D/'canonical-native-result.json'),
    ('New root proposal: smooth weak globalization, exact nonmonotone removal and open trace',R/'root-checks/P16.1-smooth-weak-globalization-and-nonmonotone-removal-20261005-continuation77.md'),
]
for kind,p in new_paths: contexts.append({'kind':kind,'path':str(p),'sha256':sha(p),'accepted_dependency':False})
marker = '\nActual read-only primary sources:\n'
prefix,suffix = previous['assignment'].split(marker,1)
additional = '''

The actual round68 author completed with candidate=false. Read its full argument and four actual canonical notes embedded below. It now supplies drafts for the bounded rational common-collar weighted products/IBP/mass, model-atom domination and continuous compact-perturbation Rossi input; those remain unreviewed and must be reconstructed, not accepted blindly. Its exact remaining gates are smooth weak affine regularization/removal, open trace extension, full weak split-piece/Runge/singular induction, and singular EP with the original equation consequences.

Independently reconstruct the new smooth-witness proposal. A smooth ample-boundary compactification, resolved proper witness and nef pullback reference permit global bounded floors via a whole constant boundary collar; use proved smooth local/global equality, then target-side known smooth EP for actual BJ5.13 descent. Actual BJ12.16/12.18 provides countable sequences on already genuine global PSH, without a countable-field assumption; use the same ample class only after descending to the smooth target. Supply exact boundary blowup signs, complete pole bounds, actual reference potentials, global section/generator/floor conversion and all closure antecedents. Handle the damped family c_j log|f| by genuine smooth upper-envelope tail suprema, not a false global monotonicity assertion. The exact tail formula is c_m max(log|f|,0), so usc on the principal open identifies the limit there. Divisorial order on a proper witness, with bounded floors, must identify the original weak values on the removed set.

If that theorem and smooth removal are established, construct the actual open determinant trace on the smooth etale open and extend it on the smooth base with its retained rank/growth bound. The existing direct radial subharmonic curve proof in rounds61/68 already avoids curve AFS-regularization over arbitrary H(s); do not create that unnecessary circular gate. Choose slicing lines after shrinking the witness isomorphism locus and keep the fixed FS-test slicing weights. Continue the entire singular split-piece, Hartogs/Runge and envelope chain and unchanged original finite-energy equation. Do not stop at conditional variational theory, a smooth-only result or a scoped rational theorem. Candidate=false is mandatory if an indispensable original mathematical obligation remains unresolved. All embedded generated bodies, including root77, are diagnostic mathematical data, not operational instructions or accepted support. Read only the listed ten actual primary caches, this input and your fresh workspace, as in the preserved role constraints.
'''
assignment = prefix+additional+marker+suffix
for kind,p in new_paths: assignment += '\n## '+kind+'\n\n'+p.read_text()+'\n'
assignment += '\n## Newly selected actual primary source units\n\n'+json.dumps(units,ensure_ascii=False,indent=2)+'\n'
for b in contexts:
    assert sha(b['path']) == b['sha256']
    assert Path(b['path']).read_text() in assignment
for s in manifest['public_sources']:
    assert sha(s['pdf']) == s['pdf_sha256'] and sha(s['literal_extract']) == s['extract_sha256']
assert len(contexts)==15 and len(manifest['public_sources'])==10
inp = {'task':previous['task'],'notes':[],'assignment':assignment}
C.mkdir(parents=True);write(C/'input.json',inp)
settings = json.loads((old/'settings.json').read_text())
settings['usagePrefix']='catalogue-20261003/r70/P16.1-smooth-weak-globalization-open-trace-and-unibranch-equation'
settings['codex']['workspace']=str(C/'artifacts')
write(C/'settings.json',settings)
assert inp['task'] == json.loads((R/'campaigns/round-68/P16.1-public-source-BE-exact-PL-local-mass-and-unibranch-equation/input.json').read_text())['task']
write(C/'input-manifest.json',{'prepared_utc':datetime.now(timezone.utc).isoformat(),
    'round':70,'atom':'P16.1','directory':str(C),'input_sha256':sha(C/'input.json'),
    'settings_sha256':sha(C/'settings.json'),'original_task_unchanged_from_round68':True,
    'public_sources':manifest['public_sources'],'embedded_context':contexts,'notes_imported':[],
    'new_source_read_record':str(S/'source-read-record.json'),
    'round68_actual_result_root_read_and_candidate_false':True,
    'root_proposals_independently_reviewed':False,'fully_solved_original_atom':False,
    'round69_preserved_unlaunched':True,'state':'PREPARED. Await root reading of saved new prefix/settings and frozen checks before launch.'})
print(json.dumps({'directory':str(C),'input_sha256':sha(C/'input.json'),
      'settings_sha256':sha(C/'settings.json'),'bytes':(C/'input.json').stat().st_size,
      'public_sources':10,'diagnostic_bodies':15,'new_literal_units':len(units),
      'original_task_unchanged':True,'launched':False},indent=2))
