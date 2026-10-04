"""Refresh the live checklist without changing immutable research checkpoints."""
from pathlib import Path
import datetime
import hashlib
import json
import re

ROOT = Path('/workspace/research')
baseline = json.loads((ROOT/'deliverables/results.json').read_text())
checkpoint_path = ROOT/'deliverables/round-02-update-01/results.json'
checkpoint = json.loads(checkpoint_path.read_text())
active = json.loads((ROOT/'active-work.json').read_text())
round_match = re.search(r'reviewed-papers-round-(\d+)\.zip$', active['latest_checkpoint'])
latest_results_path = (ROOT/'deliverables'/('round-'+round_match[1])/'results.json'
                       if round_match else checkpoint_path)
assert latest_results_path.is_file()

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
for newer_path in [round03_path, ROOT/'deliverables/round-04/results.json', ROOT/'deliverables/round-05/results.json', ROOT/'deliverables/round-06/results.json', ROOT/'deliverables/round-07/results.json', ROOT/'deliverables/round-08/results.json', ROOT/'deliverables/round-09/results.json', ROOT/'deliverables/round-10/results.json', ROOT/'deliverables/round-11/results.json', ROOT/'deliverables/round-12/results.json', ROOT/'deliverables/round-13/results.json', ROOT/'deliverables/round-14/results.json', ROOT/'deliverables/round-15/results.json', ROOT/'deliverables/round-16/results.json', ROOT/'deliverables/round-17/results.json', ROOT/'deliverables/round-18/results.json', ROOT/'deliverables/round-19/results.json', ROOT/'deliverables/round-20/results.json', ROOT/'deliverables/round-21/results.json', ROOT/'deliverables/round-22/results.json', ROOT/'deliverables/round-23/results.json', ROOT/'deliverables/round-24/results.json', ROOT/'deliverables/round-25/results.json', ROOT/'deliverables/round-26/results.json', ROOT/'deliverables/round-27/results.json', ROOT/'deliverables/round-28/results.json']:
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
            'higher-dimensional restricted quadratic compact-specialization PASS8/10 read and published; first broad cutoff caveat preserved; every-separable-quadratic/all-pure-dimensional compact-specialization PASS22/22 read and published; every-finite-separable curve exact partial PASS12/12 fully read and published; completed-algebraic pure curve ascent/compact scalar-test finite-stage descent corrected-source PASS26/35 fully read/bound and published20 pages, original PASS21/27 and source excerpt defect preserved; arbitrary-field curve recognition INCONCLUSIVE26/28 fully read/bound: missing imported proof chains and local corrections; proof/source repair completed incomplete, unaccepted; two-sign ordinary-psh curve exact review INCONCLUSIVE23/19 read/bound unaccepted; recognition source-proof repair completed incomplete with concrete foundational gaps and no recognition theorem; finite-Galois ALL-pure-dimensional complementary-test ordinary current-transport exact PASS27/40 fully read/bound and published12pages, with nilpotents/allcomponents/wild extensions retained; classical recognition and ordinary two-sign regularization remain open. Completed-algebraic ALL-dimensional current-transport and ALL-bidegree exact compact-test descent PASS23/32 fully read/bound and published13pages; all33primary bodies retained with exact prior-read reuse disclosed, arbitrary algebraic valued M/K and its completion, all components/nilpotents/Artinian lengths included. Fresh official Thuillier/Berkovich source authentication and selected complete primary proofs prepared. Round23 full-curve ordinary two-sign source/scope repair completed INCOMPLETE with null proof pointer; no independent theorem review admitted and no analytic theorem accepted. All three canonical notes and full core read; finite diagnostics independently rerun without analytic inference. Round25 specified actual semistable TREE conditional regularization exactPASS16/26 fully read and bound, published10pages with nativeSUCCESS and2cleanPDFexports: sequences on whole actualIntZ, continuous/uniformdecreasing on Z; arbitrary residualgenus, same suppliedY. All3canonicalnotes/fullnewproof/all17selectedprimarybodies fullyread; sourcebindings checked and freshcopiedreproduction byteidentical. Suppliedtree theorem accepted. Model/tree/factorization remain suppliedinputs, no originalcompletion. Round26v2 recognition-only all-K PURE-curve integration exactPASS43/75 fullyread/bound andpublished10pages, nativeSUCCESS/2cleanexports/firstpagevisual; allnewproof/all3canonicalnotes/all16primarybodies and23sourcebindings fullychecked with full exact reviewed transport/ALGClrecognition gates and GR harmonic-function descent. All actual good separated strict boundarylessPUREcurves overANYcomplete nontrivialK nowrecognized, including singularities/nilpotents/imperfectK/allcharacteristics/allanalyticextensions andallcurve maps. Stronger first-stage ordinary-smooth psh construction remains separate. Initial wrapper/main binding preparation failure preserved without native admission. Original arbitrary-dimensional recognition stays open. ')
        target['remaining_full_target'] = ('Beyond the proved actual pure-curve scope and displayed products, arbitrary higher-dimensional analytic germs still need recognition with all extension-field/curve-map quantifiers. General transcendental-current ascent and ordinary two-sign regularization are separate unproved constructions; intrinsic recognition on pure curves is now established over every complete nontrivial field.')
    elif atom == 'P05.2':
        target['current_focus'] = ('Exact cylinder-theorem audit PASS; continued '
            'product-criterion audit PASS and paper published; native research '
            'on ambient-extendible real references received PASS and was published; '
            'extension-free all-real-reference product PASS read and published, earlier input-access INCONCLUSIVE preserved; '
            'nonconical graph-cylinder full exact PASS read and published; Bergman all-real-reference actual PAPC-envelope/full contact-defect PASS0/0 read, bound and published; first missing-book-proof INCONCLUSIVE preserved; arbitrary weighted tree-cylinder PASS0/0 fully read and published; every finite graph cylinder including cycles PASS0/0 fully read/bound and published15 pages; restricted cyclic triangle-square/certificate PASS0/0 fully read/bound and published10pages; actual cyclic triangle-square negative contact PASS0/0 fully read/bound and published8pages: actualPAPC/regularizable rawenvelope, completeintegral-8 and independently reconstructed finite totalmass46; universal graph-product characterization PASS0/0 fully read/bound and published14pages, iffonefactorunbranched; fixed rational-reference graph-product theorem exact PASS0/0 fully read/bound and published16pages; every prescribed rational reference on two branched graphs has nonnegative compact obstacle and full integral-8epsilon^2ab with unchanged asymptotic reference; each prescribed REAL-reference graph-product exact theorem PASS0/0 fully read/bound and published19pages via finite rational PC cone and exact positive-growth convex decomposition; every fixed real reference on two branched rank-one-relation graphs admits full negative contact with unchanged infinity. Arbitrary-balanced-pair classification remains open. Arbitrary TWO finite-graph product classification removing rank-one hypothesis exact PASS0/0 fully read/bound and published25pages: criterion both local relation cones rank one and at least one unbranched factor, each fixed real reference; higher-relation exact PAPC/raw/regularizable compact obstruction with COMPLETE negative integral and unchanged infinity. Two local PDF exports clean; native compiler SUCCESS on unchanged final source, separately bound addendum preserves earlier pending checkpoint. Any-finite-number graph-product partial classification exactPASS0/0 fully read/bound and published28pages. Every factor localrelationcone rankone and atmostONEbranchedfactor iff full regularizable rational-domain actualPAPC envelope/contact for EACHfixedREALreference and ALLboundedREALPAobstacles. Both failures have complete negative integrals with all d-stage orders/weights retained and unchangedinfinity. Fullmain/canonical3notes and19source snapshots/12selectedbodies checked; exact4localrecursive diagnostics in dimensions3/5 rerun fromfreshcopy. NativeSUCCESS on unchangedsource,2cleanlocalexports. Originalarbitrarybalancedcarriersopen.')
        target['remaining_full_target'] = ('The geometric classification of all '
            'admitted pairs in the fixed coefficient conventions remains open.')
    elif atom in ('P15.1','P15.2'):
        target['current_focus'] = ('Supplied-fibration bounded relative zero-volume operator and unnormalized energy exact partial theorems independently PASS and fully root read/bound, published as separate 11-page and 12-page papers with native compiler SUCCESS and two clean PDF exports each. Includes critical/dimension-jumping fibres, non-descending perturbations and uniform convergence without an epsilon-relative rate. Every auxiliary Kahler class after explicit transverse calibration, and smoothly converging nondegenerate paths. Energy cocycle/shift/concavity/monotonicity and stated bounded variation laws; optional continuous descent requires connected fibres. Original general pseudoeffective problem open. Next small batch remains ONLY P15.1/P15.2, investigating actual prescribed-type mixed products and energy; future general extension remains unverified until fresh native research and review.')
        target['remaining_full_target'] = ('General pseudoeffective zero-volume scope, retained prescribed singularity types and minimum reference choices remain open. Supplied fibration/bounded-potential hypotheses, if proved, give a special scope only.')
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
    'checkpoint_results_path': str(latest_results_path),
    'checkpoint_results_sha256': hashlib.sha256(latest_results_path.read_bytes()).hexdigest(),
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
