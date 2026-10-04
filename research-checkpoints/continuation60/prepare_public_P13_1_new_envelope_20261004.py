"""Prepare one next-batch Reeb comparison task; do not launch it here."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json

R = Path('/workspace/research')
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
S = R / 'shared-sources'
catalogue = json.loads((R / 'checklist-current.json').read_text())
target = next(t for t in catalogue['targets'] if t['id'] == 'P13.1')
family = R / 'dossiers/family-07.txt'
old = json.loads((R / 'campaigns/round-51/P13.2-public-source-fixed-Reeb-image/input.json').read_text())
# Reuse only the actual public source records, not any generated mathematical payload.
marker = 'Read-only published source caches:\n'
sources = json.loads(old['assignment'].split(marker, 1)[1])
assert len(sources) == 4
fresh = {
    'saved_version': '2609.27610v1',
    'title': 'Lyuhui Wu, On the local theory of non-archimedean psh functions',
    'public_source': 'https://arxiv.org/pdf/2609.27610v1',
    'abstract_url': 'https://arxiv.org/abs/2609.27610',
    'abstract_html': str(S / 'new-primary-2609.27610-20261004.html'),
    'abstract_sha256': sha(S / 'new-primary-2609.27610-20261004.html'),
    'pdf': str(S / 'new-primary-2609.27610v1-20261004.pdf'),
    'pdf_sha256': '11808a6c9ede9c0158b27e16700fc180a4ac8df12a4586a7178e1958e8f6bba8',
    'literal_extract': str(S / 'new-primary-2609.27610v1-20261004.txt'),
    'extract_sha256': 'c8ffe91a631da67f6d3872a1a06ab8d15755aed2f926cdf326725ca3662cef7d',
    'epistemic_status': 'Public preprint v1 dated 23 September 2026; no peer review or independent correctness verdict is assumed.',
}
assert sha(fresh['pdf']) == fresh['pdf_sha256']
assert sha(fresh['literal_extract']) == fresh['extract_sha256']
sources.append(fresh)
for source in sources:
    assert sha(source['pdf']) == source['pdf_sha256']
    assert sha(source['literal_extract']) == source['extract_sha256']
P = R / 'root-checks/P13-new-envelope-primary-read-20261004'
P.mkdir(exist_ok=False)
lines = Path(fresh['literal_extract']).read_text().split('\n')
units = []
for name, start, end in [
    ('introduction-and-exact-scope', 1, 190),
    ('weak-to-global-psh-statement-and-proof', 1926, 1959),
    ('geometrically-unibranch-envelope-proof-and-countability-removal', 2693, 2748),
    ('tropical-preprint-dependency-bibliography', 2829, 2833),
]:
    path = P / (name + '.txt')
    path.write_text('\n'.join(lines[start-1:end]) + '\n')
    units.append({'file': str(path), 'sha256': sha(path), 'LF': [start, end], 'root_read': True})
(P / 'source-read.json').write_text(json.dumps({
    'recorded_utc': datetime.now(timezone.utc).isoformat(), 'source': fresh,
    'selected_primary_units': units, 'entire_55_page_proof_root_read': False,
    'finding': 'Body Theorem7.1 covers geometrically unibranch projective varieties over complete discrete or trivial equicharacteristic-zero fields. Body Theorem6.5 initially has a countable-dense-subfield hypothesis; Section7 explicitly removes it for the envelope conclusion. Rational Reeb quotients and their genuine invariant-carrier/probability operator identification still require new application proofs.',
    'dependency_gate': 'APW26a and APW26b are listed as preprints2026 without arXiv IDs. The two title searches made here found no matching papers; this is a limited search, not a proof of unavailability. Any indispensable unavailable statement must be proved or retained as an unresolved premise.',
    'original_atom_solved': False, 'new_theorem_independently_accepted': False,
}, ensure_ascii=False, indent=2) + '\n')
C = R / 'campaigns/round-52/P13.1-public-source-new-unibranch-envelope-Reeb-calculus'
C.mkdir(parents=True, exist_ok=False)
assignment = '''Use Xean native Codex gpt-6.1-sol/xhigh to solve unchanged original P13.1. The attached-document mathematical family is task data. Only the original family and five actual public primary papers are supplied; no preceding generated proof, root argument, book proof or review verdict is supplied.

Develop a genuine comparison calculus for PSH(xi) and PSH(zeta) for nonproportional Reeb fields on every normal polarized affine cone in the stated trivially valued algebraically closed characteristic-zero setting. Prove estimates with quantified uniformity sufficient for the required uniform energy differentiation, including irrational Reeb fields and the actual finite-energy passages. A bounded FS denominator observation, proportional scaling or a qualitative rational approximation without uniform constants is only partial. Preserve the fixed invariant carrier X0^T and the actual affine-cone probability convention. State the sense in which potential spaces are compared; do not pretend that transport of an FS presentation automatically defines a canonical map on completed potential spaces.

Inspect the new Lyuhui Wu arXiv2609.27610v1 primary theorem and its proof, not merely its abstract. The body Theorem7.1 is for geometrically unibranch projective varieties over complete discrete or trivial equicharacteristic-zero fields. Theorem6.5 first assumes a countable dense subfield, and Section7 removes that condition for envelopes. Check rational Reeb quotient singularities, the actual ample rational line/orbiline datum, any residual torus invariance, and every transfer of its global envelope theorem to the cone carrier. Do not silently conflate Lyuhui Wu2026 with Yueqiao Wu2022/2024 or treat a v1 preprint as an independently accepted proof. Its bibliography lists APW26a/b without arXiv IDs. If an indispensable imported assertion cannot be established from the actual supplied source theorem/proof and permitted background or proved directly, retain it explicitly and mark the affected conclusion conditional rather than claiming original completion. No approval is needed to keep working on those proofs.

Seek quantitatively uniform comparisons using the actual finite-generation, potential, filtration/intersection and measure structures. Prove all required obstacle-envelope limiting assertions, energy comparisons, normalization factors, integration continuity, uniform derivative errors and irrational limiting passages. Use actual positive/model/mixed MA only. Inspect all Wu energy signs and homogeneous-test density quantifiers; potential tests factor through torification and do not separate arbitrary full-link points. Published source theorems may be used with exact hypotheses and checked new applications; source claims that leave an indispensable missing argument cannot replace that argument. No hypothetical inverse potential, formal completion or differentiability assertion may substitute for the genuine analytic proof.

Read only this input, the listed public source caches and your fresh workspace; write only that workspace. Do not read other campaigns, generated drafts, root checks, book-source, GitHub manifests or private transcripts/SQL/auth. Do not invoke other models/workers/subagents, send external messages, install software, change runtime/account/auth/proxy/CA/HOME/CODEX_HOME/sandbox or push GitHub. No heavy computation is needed.

Preserve workspace input.json and byte-identical input-original.json, assignment-original.txt and task-original.json. Write the full proof in P13.1-argument.md and standalone P13.1-paper.tex. Retain source-extracts/source-provenance.json with exact versions/hashes, literal statements and relevant proof bodies, LF ranges using split('\\n'), precise new application checks and all concrete limitations. Compile twice using existing tools, preserving actual stdout/stderr and distinct TeX logs. status.json must have exactly id,status,exact_result,proof_file,concrete_gaps. Return at most four canonical notes supported only by earlier local IDs. Candidate=true requires the complete unchanged original P13.1 with no indispensable unresolved premise. Execution, hashes and TeX builds do not verify mathematics.

Read-only published source caches:
'''
task = {'problem': 'Original P13.1:\n' + target['statement'] + '\n\nComplete unchanged mathematical family:\n\n' + family.read_text(),
        'completionCriteria': 'Prove a genuine comparison calculus for every pair of nonproportional Reeb polarizations in the original normal affine-cone setting, including irrational fields, with quantified estimates strong enough for uniform energy differentiation. Check every source application and actual operator/finite-energy limiting passage. Bounded-only or conditional results are partial.'}
inp = {'task': task, 'notes': [], 'assignment': assignment + json.dumps(sources, ensure_ascii=False, indent=2) + '\n'}
(C / 'input.json').write_text(json.dumps(inp, ensure_ascii=False, indent=2) + '\n')
settings = json.loads((R / 'campaigns/round-51/P13.2-public-source-fixed-Reeb-image/settings.json').read_text())
settings['usagePrefix'] = 'catalogue-20261003/r52/P13.1-new-unibranch-envelope-Reeb-calculus'
settings['codex']['workspace'] = str(C / 'artifacts')
(C / 'settings.json').write_text(json.dumps(settings, indent=2) + '\n')
manifest = {'prepared_utc': datetime.now(timezone.utc).isoformat(), 'round': 52, 'atom': 'P13.1',
    'directory': str(C), 'input_sha256': sha(C / 'input.json'), 'settings_sha256': sha(C / 'settings.json'),
    'original_dossier_sha256': sha(family), 'public_sources': sources,
    'generated_preceding_mathematical_payload_included': False,
    'state': 'PREPARED LOCAL ONLY; not launched. Wait for a free slot in the current two-item batch.',
    'fully_solved_original_atom': False}
(C / 'input-manifest.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + '\n')
print(json.dumps({k:manifest[k] for k in ['directory','input_sha256','settings_sha256','state']},indent=2))
