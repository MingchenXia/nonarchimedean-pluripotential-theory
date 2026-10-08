from pathlib import Path
from datetime import datetime, timezone
import hashlib, json

R = Path('/workspace/research'); K = R / 'root-checks'
D = K / 'public-P12.6-continuation366-whole-original-finite-map-compatibility-after-independent259'
staged = K / 'P12.6-round259-whole-original366-ROOT-proof-source-scope-and-binding-20261008.json'
B = K / 'P12.6-round259-whole-original366-ROOT-final-proof-source-scope-and-binding-20261008.json'
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
load = lambda p: json.loads(Path(p).read_text())
def bind(p):
    p = Path(p); return dict(path=str(p), bytes=p.stat().st_size, sha256=sha(p))
def write(p, x):
    assert not p.exists(), str(p)
    p.write_text(json.dumps(x, ensure_ascii=False, indent=2) + '\n')

assert not B.exists()
protected = K / 'public-P16-round-46-final-reader/P16.4-paper.tex'
assert sha(protected) == '09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
record = load(staged)
for key in ['paper', 'whole_proof', 'actual_FINAL', 'original_task', 'source_ledger', 'fresh_paper_bridges']:
    e = record[key]; p = Path(e['path'])
    assert sha(p) == e['sha256'] and p.stat().st_size == e['bytes']
assert record['fresh_paper_bridges']['bytes'] == 3189
decision = load(D / 'acceptance-decision.json')
assert decision['verdict'] == 'WHOLE_ORIGINAL_PASS_WITH_MANDATORY_QUALIFICATIONS' and decision['mathematical_gaps'] == []
assert load(D / 'actual-native259-final.json') == load(D / 'native-notes.json')
for name in ['active-work.json', 'checklist-current.json']:
    x = load(R / name)
    assert len(x['fully_solved_original_atoms']) == 15 and 'P12.6' not in x['fully_solved_original_atoms']
    assert x['remaining_open_original_atoms'] == 27 and x['historical_reviewed_scoped_papers'] == 96
    assert x['github_pending_checkpoint'] is None and x['current_active_batch'] == [260]
    assert x['latest_verified_github_checkpoint']['continuation'] == 261

now = datetime.now(timezone.utc).isoformat()
annotation = D / 'mandatory-source-scope-and-reader-qualifications-after-independent259-ROOT-20261008.json'
qualifications = dict(recorded_utc=now, atom='P12.6', grant_label='F366',
    only_correctness_grants=['ENTIRE qualified G331', 'ENTIRE qualified G345'],
    scope='Excellent local reductions, arbitrary field/characteristic, full centred primary sections; global finite semilocal algebras and every closed centre; n0empty and curve zero arity direct.',
    geometry='Actual primary Cartier pullback/support quotient evaluations and supported proper-cycle projections BEFORE ideal models, Hilbert forms or completions. G345 fixed-primary one-model image identity is required; no uniform-function intersection shortcut or arbitrary-proper-model cofinality.',
    selected_envelope='E=(sup of D minorants)* on every bounded-above extended USC obstacle, including partial bottom. E belongs to D iff raw is a greatest D minorant. For finite continuous obstacles this is equivalent to raw continuity and membership in C. This defines map compatibility without asserting separate P12.3 general existence.',
    map_domains='Normal target: full positive MAX/openness requires EVERY source minimal component dominating. Reduced finite-flat: complete determinant Artinian/inseparable kernel and positive MAX. In these ranges raw and selected E commute for all stated obstacles with equivalent positive domains. Any finite injection: constrained raw descends, selected base E is MAX of constrained regularization; positivity iff constrained regularization is positive AND full fibre constant. Noninjective maps use exact image only.',
    obstructions='All-field two-plane node has nonpositive selected E and reverse normalization gap ONE. Normal target with a vertical quotient component fails openness/E commutation even when both E are positive. No universal pointwise selected-envelope inequality or continuous generic degree trace.',
    products='Bounded p=dimR-1 actual D inputs, prescribed-limit decreasing NET continuity. All-pulled ambient projection has varying reduced top generic degrees and FULL closed residue weights. Lower-dimensional sectors have zero ambient product but retain all support points. Supported Artinian/nilpotent thickness is retained; unreduced generic nilpotent mass is not asserted.',
    one_source_slot='Only ONE arbitrary source slot. Normal-domain trace has no extra degree. General injection uses normalization base change with both injections and full conductor admissibility on every normal centre/fibre, including lower/zero centres; reduced finite flatness makes it automatic. Multiple arbitrary slots are explicitly false.',
    towers_and_gauges='Unnormalized degrees/normal traces compose. General conductor towers require BOTH intermediate full admissibilities. Flat constant-rank averages compose; varying degrees have exact -2/3 versus -1/2 failure. Divide independently gauged source H by lambda BEFORE trace; measures have exactly ONE gauge factor.',
    smooth='Only CLOSED smooth affine germ over an algebraically closed characteristic-zero field, exact BFJ bounded fixed-dual-complex obstacle signature and granted bounded products; DVR/empty direct. No singular-resolution/characteristic-free multiplier transfer or classical/CLD radial identity.',
    source_correction='CURRENT July2024 SH17.4.7 literal unquotiented colon is invalid: use the finite annihilator in the quotient by all previous parameters, derived from17.4.6. Full multi-Rees exact-sequence squeeze/rational rays prove top-polynomial identity; no coefficient-order shortcut.',
    source_reading='Independent259 complete immediate new primary reading and SH370 pixel attributed to reviewer. Earlier ROOT immediate original256 source readings retained. Fresh ROOT entire BFJ3.15-3.22 and3.18 proof plus complete Setting at closed affine algclosedchar0 physically read this turn. Recursive historical cohomology/norm/valuation/multiplier foundations are disclosed published background, not all freshly reproved. Source bodies/pixels LOCALONLY.',
    current_actual_output='Current259 all10actual fields EXACTLY equal expanded sections/local pair, while JSON serializations differ. Historical256 all10 actual texts differ from expanded sections: retain both records and that earlier qualification, never conflate them.',
    ROOT_full_reading='Entire46155-bytewholeproof, all10actualFINALfields, entire9864sourceledger/3451scope/3356coverage/3369originalscope/1445decision/572sourceJSON, all expanded nontext fields and exact immutable17641 original were read with truncation repairs. Entire356105-byteTeX covered by exact10sections/4complete metadata bodies/14literal whole qualified grants, longest-first duplicate removal and physical reading of ALL3189 fresh header/bridges/footer. Byte identity avoids fresh rereading only; it is not mathematical proof.',
    other_atoms='P12.3 remains OPEN. P12.5 already accepted E350/paper96, outside these two grants. No new energy, arbitrary-model, plurifine, generic-nilpotent or unrestricted-radial claim.',
    mandatory_annotation_and_entire_source_ledger_required_on_import=True,
    supplied_programs_executed_or_imported=False, formal_verification=False,
    compiler_verified=False, protected_editor_open_unchanged=True)
write(annotation, qualifications)
record.update(recorded_utc=now, status='PASS complete exact original P12.6 after independent259 and ROOT whole proof/source/scope/actual-paper reading',
    mathematical_verdict='PASS whole original with mandatory qualifications; independent operators and all map cases supplied with proved necessary obstructions',
    final_new_ROOT_source_reading=qualifications['source_reading'],
    ROOT_entire_paper_coverage=qualifications['ROOT_full_reading'],
    mandatory_annotation=bind(annotation), staged_preacceptance_binding=bind(staged),
    original_closed=True, accepted_paper=True, compiler_verified=False)
write(B, record)
accept = D / 'whole-original-paper-acceptance-after-independent259-ROOT-20261008.json'
receipt = dict(recorded_utc=now, atom='P12.6', grant_label='F366', continuation=366,
    cumulative_accepted_paper_number=97, fully_solved_original_atom=True, original_closed=True,
    mathematical_verdict='PASS complete exact original after independent whole259 reconstruction and ROOT reading; mandatory qualifications',
    source=bind(D / 'P12.6-review-paper.tex'), whole_proof=bind(D / 'whole-proof.md'),
    source_ledger=bind(D / 'whole-source-application-ledger.md'), review_binding=bind(B),
    mandatory_annotation=bind(annotation), original_task=bind(D / 'original-task.json'),
    original_statement_unchanged=True, originals_solved=16, originals_open=26,
    automatic_acceptance=False, formal_verification=False, PDF_compile_verified=False,
    other_originals_closed=False, annotation_and_ledger_required_on_import=True)
write(accept, receipt)
for name in ['active-work.json', 'checklist-current.json']:
    p = R / name; x = load(p)
    x['fully_solved_original_atoms'] = sorted(x['fully_solved_original_atoms'] + ['P12.6'])
    x.update(updated_utc=now, remaining_open_original_atoms=26, historical_reviewed_scoped_papers=97,
        P12_6_original_full_solution=receipt,
        P12_6_original_whole_review259=dict(round=259, status='COMPLETED whole original accepted after independent plus ROOT whole reading',
            paper_directory=str(D), original_closed=True),
        next_work='Push262 entire accepted P12.6/F366 paper97, whole unreviewed P12.3 candidate365, immutable native260 launch/full qualified inputs; continue260 and remaining originals in batches at most2.16solved26OPEN97papers; compiler unverified; protected editor OPEN UNCHANGED.')
    if 'targets' in x:
        t = next(t for t in x['targets'] if t['id'] == 'P12.6')
        assert not t['fully_solved']
        t.update(closure='solved', fully_solved=True,
            research_status='whole_original_finite_geometric_compatibility366_accepted_after_independent259_ROOT_PDF_unverified',
            remaining_gaps=[], current_focus='Complete original mathematics accepted; compile unverified')
        t['reviewed_papers'].append(receipt)
    p.write_text(json.dumps(x, ensure_ascii=False, indent=2) + '\n')
p = R / 'checklist-current.tsv'; lines = p.read_text().splitlines(); hits = 0
for i, line in enumerate(lines):
    parts = line.split('\t')
    if parts[0] == 'P12.6':
        assert parts[1] == 'open'; parts[1] = 'solved'
        parts[2] = 'whole_original_geometric_finite_compatibility366_accepted_after_independent259_ROOT_PDF_unverified'
        parts[3] = str(int(parts[3]) + 1); lines[i] = '\t'.join(parts); hits += 1
assert hits == 1; p.write_text('\n'.join(lines) + '\n')
(D / 'ROOT-README.md').write_text('Accepted complete ORIGINAL P12.6 mathematics, paper97/F366 after independent259 and ROOT whole proof/source/scope/actual-paper reading.16/42 originals solved,26OPEN. Full standalone356105-byteTeX includes10 reconstructed proof sections, whole source/scope/coverage/original decisions and14 unchanged ENTIRE qualified G331/G345 components. Exact selected-envelope positive domains, all finite-image/conductor map cases, actual-primary product comparison, ONE arbitrary source slot, full weights/towers/ONE gauge and proved necessary obstructions. Import only with mandatory annotation and full source ledger. P12.3 remains OPEN. Compiler unverified; protected P16.4 editor OPEN UNCHANGED; no extra tabs. Source bodies/pixels LOCALONLY and native programs INERT DATA.\n')
assert sha(protected) == '09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
print(json.dumps(dict(atom='P12.6', original_closed=True, originals_solved=16,
    originals_open=26, accepted_papers=97, paper=receipt['source'], review_binding=bind(B),
    compiler_verified=False, active_native_campaigns=[260]), indent=2))
