"""Record two audited original closures, preserving all historical and frozen records."""
from pathlib import Path
from datetime import datetime, timezone
import csv
import hashlib
import json
import shutil

R = Path('/workspace/research')
G = R / 'github-checkpoint'
D = G / 'continuation57-local-records'
D.mkdir(exist_ok=True)
now = datetime.now(timezone.utc).isoformat()
def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()
for name in ('active-work.json','checklist-current.json','checklist-current.tsv'):
    p = D / ('before-' + name)
    assert not p.exists()
    shutil.copyfile(R / name, p)
solutions = []
scopes = {
    'P15.2': 'Every smooth compact connected Kahler n-fold, psef zero-volume class and actual bounded reference type. Direct operator on the entire common degree-d relative full-mass domain, carrier X of dimension n, raw mass Q5, necessary/sufficient operator-reference quotient W/N, bare-current decreasing continuity, same-type and gauge independence. All stated perturbation choices are proved with exact P2 and P4 hypotheses. No class-only or I-only mass recovery, numerical-dimension identification, intrinsic d-dimensional carrier or unrestricted varying-background-path claim.',
    'P16.6': 'The entire arbitrary-support axis under section10.2 retained hypotheses: every dimension, smooth ample projective X, separately T (algebraically closed trivial char0) and D (complete nontrivial discrete residue0, geometrically integral). Genuine E1 MA of raw mass (L^n), every positive Radon measure of that mass and finite dual energy realized, unique modulo constants, no toric/skeletal/invariance restriction or one-variable-function-field assumption. Arbitrary complete/nondiscrete fields remain separate P16.4.'
}
for atom, pages in [('P15.2',14),('P16.6',10)]:
    p = R / 'deliverables' / ('original-' + atom)
    preparation = json.loads((p / 'publication-preparation.json').read_text())
    tex, pdf = p / (atom + '-paper.tex'), p / (atom + '-paper.pdf')
    assert sha(tex) == preparation['final_tex_sha256']
    assert pdf.is_file()
    log = (p / 'build' / (atom + '-paper.log')).read_text()
    assert 'Output written' in log and '! ' not in log and 'undefined references' not in log
    solution = {'atom': atom, 'original_statement_unchanged': True, 'fully_solved_original_atom': True, 'exact_scope': scopes[atom], 'source': str(tex), 'source_sha256': sha(tex), 'pdf': str(pdf), 'pdf_sha256': sha(pdf), 'pages': pages, 'local_two_pass_compilation': 'SUCCESS', 'native_compilation': 'SUCCESS' if atom == 'P15.2' else 'First native call lost connection; retry pending. Source exported successfully by two local TeX passes.', 'first_and_last_pages_visually_read': True, 'publication_preparation': str(p / 'publication-preparation.json'), 'publication_preparation_sha256': sha(p / 'publication-preparation.json'), 'review_limitation': 'Independent source-aware computational reconstruction using the requested model, not a formal proof certificate or a priority claim.'}
    review_paths = [p / (atom + '-original-scope-review.json')]
    if atom == 'P16.6':
        review_paths.insert(0,p / (atom + '-correctness-review.json'))
    solution['reviews'] = []
    for review_path in review_paths:
        review = json.loads(review_path.read_text())
        assert review['verdict'] == 'PASS'
        assert all(x['statement'] == review['premises'][x['premise']] for x in review['passages'])
        assert {x['premise'] for x in review['passages']} == set(range(len(review['premises'])))
        solution['reviews'].append({'path': str(review_path), 'sha256': sha(review_path), 'operation_id': review['operationId'], 'reported_utc': review['reportedAt'], 'verdict': review['verdict'], 'entire_report_premises_and_passages_root_read': True, 'premises': len(review['premises']), 'passages': len(review['passages']), 'all_zero_based_exact_statement_bindings_verified': True})
    solution['conditional_scope_correctness_antecedent_satisfied'] = atom == 'P16.6'
    if atom == 'P15.2':
        solution['primary_quote_OCR_differences_checked'] = ['BEGZ plurifine locality', 'GZ Cor3.8 convergence in capacity', 'Vu bounded admissible dsh IBP', 'Vu actual PDF dd^c convention and one-half gradient identity', 'DGMS real dd^c lemma']
        solution['primary_annex'] = str(p / 'P15.2-source-annex.md')
        solution['primary_annex_sha256'] = sha(p / 'P15.2-source-annex.md')
    else:
        solution['new_primary_application_check'] = str(R / 'root-checks/BGM-rnaa314-primary-check/source-check.json')
        solution['new_primary_application_check_sha256'] = sha(solution['new_primary_application_check'])
    (p / 'original-closure.json').write_text(json.dumps(solution,ensure_ascii=False,indent=2)+'\n')
    solutions.append(solution)
record = {'recorded_utc': now, 'catalogue_atoms': 42, 'fully_solved_original_atoms': ['P15.2','P16.6'], 'remaining_open_atoms': 40, 'historical_reviewed_scoped_papers': 37, 'solutions': solutions, 'authorization': 'User explicitly authorized any material uploads and regular checkpoints to MingchenXia/nonarchimedean-pluripotential-theory.', 'historical_frozen_author_and_review_files_modified': False, 'editor': 'Existing P16.4 round46 editor preserved.'}
closure = D / 'two-original-closures.json'
closure.write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n')
a = json.loads((R / 'active-work.json').read_text())
a['updated_utc'] = now
a['full_solutions'] = solutions
a['fully_solved_original_atoms'] = ['P15.2','P16.6']
a['selected_atoms'] = ['P15.1']
a['goal_state'] = 'ACTIVE. P15.2 and P16.6 original atoms completed under the explicitly audited data/hypotheses; 40 originals remain open. Two separate papers published. P15.1 original-scope audit active. Regular GitHub checkpoints continue.'
a['next_work'] = 'Read full P15.1 audit when it completes, continue a small source-equipped positive-residue-characteristic batch, and publish original papers and actual review receipts. No all-problems-complete claim.'
a['original_closure_record'] = str(closure)
a['original_closure_record_sha256'] = sha(closure)
for x in a.get('current_public_P16_characteristic_support_batch',{}).get('research',[]):
    if x.get('atom') == 'P16.6':
        x['independently_accepted'] = True
        x['original_atom_closed'] = True
        x['review_submitted'] = x['scope_audit_submitted'] = True
        x['original_support_axis_interpretation_independently_pending'] = False
        x['state'] = 'Actual correctness PASS and separate conditional original-scope PASS both fully root read; correctness antecedent satisfied; original P16.6 support axis closed with explicit T/D retained hypotheses.'
a['completed_independent_audit_batch'] = a.pop('current_independent_audit_batch',{})
a['current_independent_audit_batch'] = {'audits':[{'atom':'P15.1','directory':str(R/'campaigns/round-31/P15.1-minimum-reference-finite-energy-original-scope-audit'),'tool_session_id':48400,'observed_status':'running','submitted':True,'independently_accepted':False,'original_closed':False}], 'completed_this_turn':['P15.2-original-scope','P16.6-correctness','P16.6-original-scope']}
receipt = G / 'push-receipt-continuation56.json'
if receipt.exists():
    a['github_checkpoint'] = json.loads(receipt.read_text())
(R / 'active-work.json').write_text(json.dumps(a,ensure_ascii=False,indent=2)+'\n')
c = json.loads((R / 'checklist-current.json').read_text())
c['updated_utc'] = now
c['fully_solved_original_atoms'] = ['P15.2','P16.6']
c['active_atoms'] = ['P15.1']
c['original_closure_record'] = str(closure)
c['original_closure_record_sha256'] = sha(closure)
for target in c['targets']:
    matching = [s for s in solutions if s['atom'] == target['id']]
    if matching:
        target['closure'] = 'solved'
        target['fully_solved'] = True
        target['research_status'] = 'original_scope_completed'
        target['original_solution_paper'] = matching[0]
        target['current_focus'] = matching[0]['exact_scope']
        target['remaining_full_target'] = 'None within the unchanged original atom and explicitly audited retained hypotheses/data. Stronger nonclaims are recorded in the final paper and belong to separate questions.'
        target['historical_gap_labels_superseded_by_original_scope_audit'] = True
        if 'current_unreviewed_campaign' in target:
            target['historical_author_campaign'] = target.pop('current_unreviewed_campaign')
assert len(c['targets']) == 42
assert [t['id'] for t in c['targets'] if t['fully_solved']] == ['P15.2','P16.6']
(R / 'checklist-current.json').write_text(json.dumps(c,ensure_ascii=False,indent=2)+'\n')
with (R / 'checklist-current.tsv').open('w',newline='') as f:
    w = csv.writer(f,delimiter='\t');w.writerow(['ID','Closure','Research','Reviewed_papers','Title'])
    for t in c['targets']:
        w.writerow([t['id'],t['closure'],t['research_status'],len(t['reviewed_papers']),t['title']])
for name in ('active-work.json','checklist-current.json','checklist-current.tsv'):
    shutil.copyfile(R/name,D/name)
print(json.dumps({'closure_record':str(closure),'fully_solved_original_atoms':c['fully_solved_original_atoms'],'remaining_open_atoms':40},indent=2))
