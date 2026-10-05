"""Prepare a new original-domain repair from completed58 and three root proposals."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json

R = Path('/workspace/research')
old = R / 'campaigns/round-58/P16.1-public-source-algebraic-collar-trace-and-unibranch-equation'
C = R / 'campaigns/round-61/P16.1-public-source-calibrated-local-BT-and-unibranch-equation'
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
previous = json.loads((old / 'input.json').read_text())
manifest58 = json.loads((old / 'input-manifest.json').read_text())
assert sha(old / 'input.json') == manifest58['input_sha256']
assert sha(old / 'settings.json') == manifest58['settings_sha256']
reader = R / 'root-checks/public-P16.1-round-58-final-reader'
result = json.loads((reader / 'canonical-notes.json').read_text())
assert result['candidate'] is False and len(result['notes']) == 4
read_state = json.loads((reader / 'root-preservation-and-read-state-continuation69.json').read_text())
assert read_state['whole_argument_root_read']
assert read_state['entire_completed_native_result_and_four_notes_root_read']
contexts = manifest58['embedded_context'] + [
    {'kind': 'Completed round58 entire partial argument, unreviewed', 'path': str(reader / 'P16.1-argument.md')},
    {'kind': 'Actual completed round58 four canonical notes, unreviewed', 'path': str(reader / 'canonical-notes.json')}
]
for p in sorted((R / 'root-checks').glob('P16.1-*-20261005-continuation70.md')):
    contexts.append({'kind': 'Unreviewed root proposal: ' + p.stem, 'path': str(p)})
assert len(contexts) == 16
marker = '\nActual read-only primary sources:\n'
prefix, suffix = previous['assignment'].split(marker, 1)
additional = '''

New repair target after the completed round58 partial: independently reconstruct its entire mathematical chain and then close the original P16.1 task. The additional whole argument and four notes are diagnostic data, not accepted dependencies. The three new root proposals specifically target corrected tropical-image local positivity, smooth common bounded-local representation, and domination/globalization. Check every new statement instead of assuming a root proposal is correct.

For curves, prove lisse membership on a common semistable skeleton for finite regular unit log coordinates; handle zeros, identically-zero pulled coordinates, type I/IV neighborhoods and real breakpoints. Corrected relative affine contact supports give nonnegative outgoing slopes after subtracting a harmonic log support, so apply the actual Thuillier/Wanner positive-Laplacian criterion. Pass decreasing limits by Thuillier3.1.8(ii). Verify this removes the extra ambient-convex current-approximation antecedent in round58's radial boundary proof, while retaining Omega's exact field scope, smooth proper compactification when needed, all ramification/Artinian degrees, properness and minus-infinity cases. Local supports alone do not imply an ambient convex extension; the supplied elementary counterexample explains the distinction.

For higher dimensions reconstruct the actual calibrated corner-current formula from CLD's Green and harmonic-balancing proof7.8.4, with correct inward/outgoing signs, positive facet calibrations, test-coordinate refinement, collapsed cells, and finite rational-domain representation of the stated local PL convention. Prove positive curvature from relative contact supports. Check18.8.4/6/8 and17.8.4 exactly:17.8.4 states strict integer PL, whereas18.8.8 is printed for integer PL. Resolve rather than silently identify this distinction. Over k((t)), clear rational constants and use GM's proper nontrivially valued algebraic/formal/PL equivalence, residual central curve degrees and BJ4.19 only on smooth connected characteristic-zero compactifications. For this smooth route, continuous global PSH is sufficient; do not require an unproved singular equivariant PL representation. Uniform genuine model approximation of a continuous global psh metric permits the actual CLD/model mixed-product identification. Do not use CLD8.7.2's uniform-convergence theorem for a noncontinuous decreasing bounded limit.

Complete the corrected common bounded-local representation using a rational negative FS floor and a compact common collar for an entire decreasing tail. Include the actual complete section system, reference difference theta=omega+ddc p, Phi=Psi/A+p and G=v-p+(M+1)/A. One common reference/scale should work for the whole mixed tuple and test. Use the genuine global BJ mixed weighted decreasing continuity to establish local mixed measures, overlap and approximation independence, weighted integrability, local/global compatibility and locality. Reconstruct the partition-of-unity mass and integration-by-parts proof and comparison before using domination; correct the winning-locus measure. No local mixed product or arbitrary weak regularization may be assumed to build its own common representation.

Replace the Dirac-equation antecedent in Wu4.16 with a bounded ample model test having positive actual MA mass at each divisorial point. BJ2.12 and2.33 give an ample test configuration on a model containing that point, so its central intersection weight is positive. Check relative integral closure, exact degree/multiplicity and field/polarization conditions. Then the perturbation phi_t=(1-t)phi+t b, mixed positivity and exact comparison/mass force the desired divisorial inequality. Obtain full local domination only after divisorial determination has been established for this corrected class. Use a decreasing directed net of continuous majorants for an arbitrary usc obstacle on an uncountable-field analytification; do not assume metrizability or an unavailable global sequence. Under the known smooth EP/orthogonality, prove smooth local/global equality and noncircular smooth upper-growth affine regularization by bounded floors and genuine global closure. For weak inputs resolve the witness and use known smooth nef EP and the exact BJ5.13 onto hypotheses; analytic surjectivity identifies the descended values. The principal-open removable extension and controlled original-exhaustion bounds still require an independent proof, not just regularizability on Y_f.

Then reconstruct Rossi's actual arbitrary analytic-neighborhood and split analytic-piece applications, localize the locally constant integer trace to fix gamma, separately handle gamma=1, and complete the Hartogs/Runge induction and weak/global singular identification. A narrower algebraic collar lemma by itself does not validate arbitrary analytic gluing on a singular space. Close actual geometrically unibranch singular EP, arbitrary-cardinality/real-class passages, genuine energy differentiation/comparison, onto normalization and arbitrary-support finite-energy variational existence/uniqueness before declaring candidate=true. If an indispensable gate remains open, preserve the exact original criteria and record a concrete partial theorem and gap in the paper.
'''
assignment = prefix + additional + marker + suffix
for item in contexts[len(manifest58['embedded_context']):]:
    body = Path(item['path']).read_text()
    assignment += '\n## ' + item['kind'] + '\n\n' + body + '\n'
for item in contexts:
    if 'sha256' in item:
        assert sha(item['path']) == item['sha256']
    item['sha256'] = sha(item['path'])
    item['accepted_dependency'] = False
    assert Path(item['path']).read_text() in assignment
sources = manifest58['public_sources']
assert len(sources) == 6
for s in sources:
    assert sha(s['pdf']) == s['pdf_sha256']
    assert sha(s['literal_extract']) == s['extract_sha256']
inp = {'task': previous['task'], 'notes': [], 'assignment': assignment}
assert inp['task'] == previous['task']
C.mkdir(parents=True, exist_ok=False)
(C / 'input.json').write_text(json.dumps(inp, ensure_ascii=False, indent=2) + '\n')
settings = json.loads((old / 'settings.json').read_text())
settings['usagePrefix'] = 'catalogue-20261003/r61/P16.1-calibrated-local-BT-and-unibranch-equation'
settings['codex']['workspace'] = str(C / 'artifacts')
(C / 'settings.json').write_text(json.dumps(settings, indent=2) + '\n')
manifest = {'prepared_utc': datetime.now(timezone.utc).isoformat(), 'round': 61,
    'atom': 'P16.1', 'directory': str(C),
    'input_sha256': sha(C / 'input.json'), 'settings_sha256': sha(C / 'settings.json'),
    'original_task_unchanged_from_round58': True, 'public_sources': sources,
    'embedded_context': contexts, 'notes_imported': [],
    'root_proposals_independently_reviewed': False, 'fully_solved_original_atom': False,
    'state': 'PREPARED LOCAL ONLY; no worker launched. Wait for a free native two-item batch slot.'}
(C / 'input-manifest.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + '\n')
print(json.dumps({'directory': str(C), 'input_sha256': manifest['input_sha256'],
                  'settings_sha256': manifest['settings_sha256'],
                  'bytes': (C / 'input.json').stat().st_size, 'context_bodies': len(contexts),
                  'original_task_unchanged': True, 'launched': False}, indent=2))
