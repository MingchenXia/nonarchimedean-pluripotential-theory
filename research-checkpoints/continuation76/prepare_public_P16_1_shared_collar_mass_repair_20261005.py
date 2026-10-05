"""Freeze new weighted/collar source bindings and prepare an unlaunched successor."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json

R = Path('/workspace/research')
old = R / 'campaigns/round-68/P16.1-public-source-BE-exact-PL-local-mass-and-unibranch-equation'
C = R / 'campaigns/round-69/P16.1-public-source-shared-collar-weighted-mass-and-unibranch-equation'
S = R / 'root-checks/continuation76-BJ-shared-collar-weighted-and-locality-reads'
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
write = lambda p, d: Path(p).write_text(json.dumps(d, ensure_ascii=False, indent=2) + '\n')
m = json.loads((old / 'input-manifest.json').read_text())
assert sha(old/'input.json') == m['input_sha256'] == '7406e003058a7ac99b768f641c352242070284533dd11fba245f15bea04091be'
assert sha(old/'settings.json') == m['settings_sha256']
assert not C.exists() and not S.exists()
src = R / 'shared-sources/P16-arxiv-1801.08229-20261004.txt'
lines = src.read_bytes().decode().split('\n')
S.mkdir()
units = []
for label,first,last,scope in [
    ('BJ-actual-model-signed-measures-and-integration-by-parts',1818,1849,'Whole formulas3.6-3.9 with exact model mass; local extension not supplied by this theorem.'),
    ('BJ-divisorial-order-and-complete-proof',2494,2535,'Whole4.22 proof including4.26. Order against usc functions, not merely injectivity of divisorial evaluations.'),
    ('BJ-general-E1-mixed-measures-and-complete-proof',4003,4057,'Whole7.19. Actual general projective signed products; local analytic applicability is a new bridge.'),
    ('BJ-weighted-decreasing-continuity-and-complete-proofs',4074,4125,'Whole7.21 and7.22. Use actual pairing-minus-reference sign; printed4119-4123 reverses it.'),
    ('BJ-genuine-locality-comparison-and-complete-proofs',4529,4602,'Whole7.40/7.41/7.43/7.44. Replace final7.19iii citation by two legitimate7.21 weighted passages; no EP antecedent.')
]:
    literal = '\n'.join(lines[first-1:last])
    p = S/(label+'.txt');p.write_text(literal)
    assert p.read_bytes().decode() == literal
    units.append({'id':label,'version':'1801.08229v4','source':str(src),'source_sha256':sha(src),
        'inclusive_one_based_LF':[first,last],'literal_file':str(p),'literal_sha256':sha(p),
        'selected_literal_body_root_read':True,'whole_primary_body_root_read':False,'scope_and_limits':scope})
write(S/'source-read-record.json',{'recorded_utc':datetime.now(timezone.utc).isoformat(),
    'LF_convention':'UTF-8 bytes decode and split("\\n"), inclusive one-based ranges',
    'units':units,'new_applications_independently_reviewed':False})
previous = json.loads((old/'input.json').read_text())
p = R/'root-checks/P16.1-shared-collar-independence-and-signed-cutoff-mass-20261005-continuation76.md'
contexts = list(m['embedded_context'])
item = {'kind':'New unreviewed root proposal: shared-collar independence, weighted signed-cutoff mass and explicit divisorial order',
    'path':str(p),'sha256':sha(p),'accepted_dependency':False}
contexts.append(item)
marker = '\nActual read-only primary sources:\n'
prefix,suffix = previous['assignment'].split(marker,1)
additional = '''

Reconstruct the new shared-collar proof proposal independently. For distinct approximation sequences and chart extensions, compare each with a single smaller common collar using its own continuous approximants; then identify the explicit common global limit max(u-h,0). Do not assert equality of unrelated approximant measures or rely on MA monotonicity in the potential. Treat weights through actual BJ7.21 and signed PL cutoffs as the difference of two positive global curvature pairs; pass each term separately. Use actual compact-neighborhood global PL extensions and global model IBP before the bounded limit, then a finite actual global PL partition with sum exactly one to prove the ddc-exact telescoping mass identity. Keep A^r only if the global metric has been divided by A; it is already present for metrics in A theta. Compare relative potentials by adding the same local reference weight g in both collars, then use BJ4.22 globally on the resulting genuine potentials to prove divisorial order. Reconstruct the positive ample-model atom perturbation and comparison argument without a singular Dirac existence theorem. Check restriction, max and positive rational-combination closure, all weighted limits, exact total mass, singular/reduced scope and real-class obligations. If these antecedents are proved, continue the noncircular smooth weak-affine regularization, controlled principal-open damping and weak finite-flat trace reconstruction, then Rossi/Runge/singular EP and the unchanged full original equation. Do not use source5.13 birational onto without target-side envelope hypotheses.

Actual BJ1801.08229v4 source units: LF1818-1849,2494-2535,4003-4057,4074-4125,4529-4602, with complete pertinent proof bodies. The displayed signs at4119-4123 and final locality citation at4585 are checked diagnostically; the correct definitions and BJ7.21 weighted limit must replace the printed shortcuts. All root proposals and earlier generated bodies remain diagnostic and unreviewed, not assumed mathematical support. Return candidate=false and list concrete gates if any indispensable original obligation remains unresolved.
'''
assignment = prefix+additional+marker+suffix
assignment += '\n## '+item['kind']+'\n\n'+p.read_text()+'\n'
assignment += '\n## Exact newly selected read-only source units\n\n'+json.dumps(units,ensure_ascii=False,indent=2)+'\n'
for b in contexts:
    assert sha(b['path'])==b['sha256']
    assert Path(b['path']).read_text() in assignment
for s in m['public_sources']:
    assert sha(s['pdf'])==s['pdf_sha256'] and sha(s['literal_extract'])==s['extract_sha256']
assert len(contexts)==12 and len(m['public_sources'])==10 and previous['notes']==[]
inp={'task':previous['task'],'notes':[],'assignment':assignment}
C.mkdir(parents=True)
write(C/'input.json',inp)
settings=json.loads((old/'settings.json').read_text())
settings['usagePrefix']='catalogue-20261003/r69/P16.1-shared-collar-weighted-mass-and-unibranch-equation'
settings['codex']['workspace']=str(C/'artifacts')
write(C/'settings.json',settings)
manifest={'prepared_utc':datetime.now(timezone.utc).isoformat(),'round':69,'atom':'P16.1','directory':str(C),
    'input_sha256':sha(C/'input.json'),'settings_sha256':sha(C/'settings.json'),
    'original_task_unchanged_from_round68':True,'public_sources':m['public_sources'],
    'embedded_context':contexts,'notes_imported':[],'new_source_read_record':str(S/'source-read-record.json'),
    'root_proposals_independently_reviewed':False,'fully_solved_original_atom':False,
    'state':'PREPARED LOCAL ONLY. Do not launch alongside the current two-item batch. Read round68 actual result first; a later successor may need that new diagnosis.'}
write(C/'input-manifest.json',manifest)
print(json.dumps({'directory':str(C),'input_sha256':manifest['input_sha256'],
    'settings_sha256':manifest['settings_sha256'],'bytes':(C/'input.json').stat().st_size,
    'public_sources':10,'context_bodies':12,'new_literal_units':5,'original_task_unchanged':True,'launched':False},indent=2))
