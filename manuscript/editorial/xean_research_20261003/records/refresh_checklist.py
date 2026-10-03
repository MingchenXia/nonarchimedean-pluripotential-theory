"""Refresh the live checklist without changing immutable research checkpoints."""
from pathlib import Path
import datetime
import hashlib
import json

ROOT = Path('/workspace/research')
baseline = json.loads((ROOT/'deliverables/results.json').read_text())
checkpoint_path = ROOT/'deliverables/round-02-update-01/results.json'
checkpoint = json.loads(checkpoint_path.read_text())
active = json.loads((ROOT/'active-work.json').read_text())

paper_map = {}
for paper in baseline['papers']:
    paper_map.setdefault(paper['id'], []).append({
        'scope': paper['reviewed_scope'],
        'source': str(ROOT/'papers'/paper['source']),
        'pdf': str(ROOT/'papers'/paper['pdf']),
        'argument': str(ROOT/'papers'/paper['argument']),
        'review': str(ROOT/'papers'/paper['review']),
        'full_original_atom_solved': False,
    })
for atom in {p['atom'] for p in checkpoint['papers_and_supporting_note']}:
    paper_map[atom] = []
for paper in checkpoint['papers_and_supporting_note']:
    directory = checkpoint_path.parent
    files = paper['files']
    def matching(suffix):
        return str(directory/next(name for name in files if name.endswith(suffix)))
    paper_map[paper['atom']].append({
        'scope': paper['scope'], 'source': matching('.tex'),
        'pdf': matching('.pdf'), 'argument': matching('-argument.md'),
        'review': matching('-review.json'), 'pages': paper['pages'],
        'full_original_atom_solved': False,
    })

round03_path = ROOT/'deliverables/round-03/results.json'
for newer_path in [round03_path, ROOT/'deliverables/round-04/results.json', ROOT/'deliverables/round-05/results.json', ROOT/'deliverables/round-06/results.json', ROOT/'deliverables/round-07/results.json', ROOT/'deliverables/round-08/results.json', ROOT/'deliverables/round-09/results.json', ROOT/'deliverables/round-10/results.json', ROOT/'deliverables/round-11/results.json', ROOT/'deliverables/round-12/results.json']:
    if newer_path.is_file():
        newer = json.loads(newer_path.read_text())
        for paper in newer['papers_and_supporting_note']:
            directory = newer_path.parent
            files = paper['files']
            def matching(suffix):
                return str(directory/next(name for name in files if name.endswith(suffix)))
            paper_map.setdefault(paper['atom'], []).append({
                'scope': paper['scope'], 'source': matching('.tex'),
                'pdf': matching('.pdf'), 'argument': matching('-argument.md'),
                'review': matching('-review.json'), 'pages': paper['pages'],
                'full_original_atom_solved': False,
            })

targets = []
for original in baseline['targets']:
    atom = original['id']
    target = {key: original[key] for key in
              ('id', 'tier', 'title', 'family', 'statement')}
    target['closure'] = 'open'
    target['fully_solved'] = False
    target['research_status'] = ('active' if atom in active['selected_atoms']
                                 else original['research_status'])
    target['reviewed_papers'] = paper_map.get(atom, [])
    target['earlier_remaining_gaps'] = original['remaining_gaps']
    if atom == 'P06.2':
        target['current_focus'] = ('Closed-curve paper audit PASS; '
            'purely inseparable ascent audit PASS and paper published; '
            'intrinsic curve recognition full-evidence PASS read and published, previous INCONCLUSIVE preserved; '
            'restricted quadratic curve-ascent principal PASS read and published, unused broad supplemental cutoff statement caveated; '
            'higher-dimensional restricted quadratic compact-specialization PASS8/10 read and published; first broad cutoff caveat preserved; every-separable-quadratic/all-pure-dimensional compact-specialization PASS22/22 read and published; finite-separable curve draft fully read under exact review; completed-algebraic curve research runs. ')
        target['remaining_full_target'] = ('Arbitrary analytic germs and curve maps, '
            'all required field-extension tests, general scalar-current ascent '
            'and two-sign regularization are not established by cone constancy '
            'or the closed-curve theorem.')
    elif atom == 'P05.2':
        target['current_focus'] = ('Exact cylinder-theorem audit PASS; continued '
            'product-criterion audit PASS and paper published; native research '
            'on ambient-extendible real references received PASS and was published; '
            'extension-free all-real-reference product PASS read and published, earlier input-access INCONCLUSIVE preserved; '
            'nonconical graph-cylinder full exact PASS read and published; Bergman all-real-reference actual PAPC-envelope/full contact-defect PASS0/0 read, bound and published; first missing-book-proof INCONCLUSIVE preserved; arbitrary weighted tree-cylinder PASS0/0 fully read and published; cyclic graph-cylinder native continuation runs.')
        target['remaining_full_target'] = ('The geometric classification of all '
            'admitted pairs in the fixed coefficient conventions remains open.')
    elif atom == 'P21.3':
        target['current_focus'] = 'General continuous-pair case returned to backlog.'
        target['remaining_full_target'] = ('The strict real-PL theorem and supporting '
            'dual reduction do not prove the identity for arbitrary continuous '
            'equal-curvature psh pairs, including the trivially valued scope.')
    targets.append(target)

assert len(targets) == 42
assert len({target['id'] for target in targets}) == 42
assert not any(target['fully_solved'] for target in targets)
for papers in paper_map.values():
    for paper in papers:
        for field in ('source', 'pdf', 'argument', 'review'):
            if not Path(paper[field]).is_file():
                raise FileNotFoundError(paper[field])

payload = {
    'updated_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
    'catalogue_atoms': 42, 'fully_solved_original_atoms': [],
    'active_atoms': active['selected_atoms'],
    'route': 'Xean native Codex', 'model': 'gpt-6.1-sol', 'reasoning': 'xhigh',
    'latest_immutable_checkpoint': active['latest_checkpoint'],
    'checkpoint_results_sha256': hashlib.sha256(checkpoint_path.read_bytes()).hexdigest(),
    'review_limit': baseline['review_limit'],
    'active_work_record': str(ROOT/'active-work.json'),
    'unpublished_drafts': ([] if round03_path.is_file() else [
        {'atom':'P06.2',
         'source':'/workspace/research/campaigns/round-02/P06.2-curve-continuation/artifacts/codex-HTO5Wc/P06.2-partial.tex',
         'pdf':'/workspace/research/campaigns/round-02/P06.2-curve-continuation/artifacts/codex-HTO5Wc/P06.2-partial.pdf',
         'status':'Independent exact-scope PASS read and bound; accepted partial paper awaiting paired publication.'},
        {'atom':'P05.2',
         'source':'/workspace/research/campaigns/round-03/P05.2/artifacts/codex-upitq1/P05.2-partial.tex',
         'pdf':'/workspace/research/campaigns/round-03/P05.2/artifacts/codex-upitq1/build/P05.2-partial.pdf',
         'status':'Full-classification audit INCONCLUSIVE preserved; focused exact-theorem PASS read and bound, awaiting publication.'},
    ]) + [
        {'atom': continuation['atom'],
         'campaign_directory': continuation['directory'],
         'status': continuation['state'],
         'queued_review_directory': continuation['queued_review_directory']}
        for continuation in active.get('continuations', [])
        if not continuation.get('published_results')
    ],
    'targets': targets,
}
(ROOT/'checklist-current.json').write_text(
    json.dumps(payload, ensure_ascii=False, indent=2)+'\n')
rows = ['ID\tClosure\tResearch\tReviewed_papers\tTitle']
rows += ['\t'.join((t['id'], t['closure'], t['research_status'],
                    str(len(t['reviewed_papers'])), t['title'])) for t in targets]
(ROOT/'checklist-current.tsv').write_text('\n'.join(rows)+'\n')
print(json.dumps({'atoms':len(targets), 'fully_solved':0,
                  'active_atoms':active['selected_atoms'],
                  'live_checklist':str(ROOT/'checklist-current.json')}))
