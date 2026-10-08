from pathlib import Path
from datetime import datetime,timezone
import hashlib,json

R=Path('/workspace/research');K=R/'root-checks'
P=K/'P12.4-continuation342-localized-Cartier-core-comparison-and-bounded-locality-working-proof-20261008.md'
out=K/'P12.4-continuation342-ROOT-whole-working-proof-source-scope-and-binding-20261008.json'
B=R/'primary-data-LOCALONLY/P12.4-local-cartier-intersections-20261008'
D=K/'public-P12.2-continuation331-geometric-primary-model-and-full-conductor-original-candidate'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def entry(p):
    p=Path(p);return dict(path=str(p),bytes=p.stat().st_size,sha256=sha(p))
assert not out.exists()
sources=json.loads((B/'acquisition-records.json').read_text())
assert [e['tag'] for e in sources]==['0BEL','0AG7','01OF','0AYA','02QL']
for e in sources:
    for kind in ['html','text']:
        p=Path(e[kind+'_path']);assert sha(p)==e[kind+'_sha256'] and p.stat().st_size==e[kind+'_bytes']
grant=[D/n for n in ['P12.2-paper.tex','mandatory-source-scope-and-reader-qualifications-after-review240-20261008.json','source-application-ledger.md','exact-scope.md','whole-original-paper-acceptance-after-review240-20261008.json']]
assert sha(grant[0])=='dadc8d064c849b80bbcb55d2c68217cd20a8c3056e3ca10ae729ac7b03537b80'
old=R/'primary-data-LOCALONLY/P12.2-relative-geometry-20261008'
assert sha(K/'public-P16-round-46-final-reader/P16.4-paper.tex')=='09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
for name in ['active-work.json','checklist-current.json']:
    x=json.loads((R/name).read_text());assert len(x['fully_solved_original_atoms'])==13 and x['remaining_open_original_atoms']==29 and x['historical_reviewed_scoped_papers']==93
record=dict(recorded_utc=datetime.now(timezone.utc).isoformat(),atom='P12.4',continuation=342,
    status='UNREVIEWED complete working argument; whole original remains OPEN',proof=entry(P),
    ROOT_whole_proof_physically_read=True,read_chunks='Characters0:15000 and15000:end; amended source-application paragraph physically reread separately.',
    only_qualified_correctness_grant='G331',complete_grant_import_requires_all=[entry(p) for p in grant],
    unreviewed_dependencies=[entry(K/n) for n in ['P12.4-continuation338-bounded-mixed-multiplicity-extension-working-route-20261008.md','P12.4-continuation339-mixed-multiplicity-moment-kernel-and-bounded-measures-working-proof-20261008.md']],
    private_primary_metadata=sources,extra_existing_primary_bindings=[entry(old/'Stacks-0B5S.html'),entry(old/'Stacks-0B5S.txt')],
    whole_immediate_source_units_ROOT_text_read=['Entire0BEL Section33.45 statements and proofs1--13.','Entire0AG7 Lemma30.14.3 statement and proof.','Entire01OF Section31.33 statements and proofs1--14.','Entire0AYA Section42.26 statements and proofs1--4.','Entire02QL Situation42.7.1.','Entireexisting0B5S Section30.16 statements and proofs1--3, including all5parts of30.16.1.','WholeG331 n7/n8 physical reread lines273--368 for fixedc0, ampleness, section generation, actual primary model and divisor evaluation.'],
    source_pixels_freshly_viewed=False,recursive_historical_source_reading_claim=False,primary_bodies_publish=False,
    new_working_arguments=['Supported Euler intersection on actual Cartier thickenings; mixed-characteristic filtration and full symmetry by a supported Koszul complex.','Properbirational/normalization cycle projection without a degree on globalCH0.','PrimaryRees ideals via0AG7+Serre yield raw mixed multiplicity equality.','Independent positive geometric atomic model measure.','Exact divisor identity on ONE fixed primary refinement bridges section-ideal approximations and actual REAL curve-nef intersections.','Raw rational-ideal strict maximum locality via a trivial restricted ratio line bundle.','Full boundedD OPEN locality by uniform approximation, two compact-cover decreasing-net limits and uniform weak continuity insideD.'],
    original_obligations_still_require_whole_independent_judgment=['Completealgebraic338339kernel review247.','Complete342actualgeometriccomparisonandlocalityreview.','Wholeoriginal reconstruction including exact BFJsmooth specialization,gauge,normalization,all-support,topdimension and curve/empty cases.'],
    original_closed=False,paper_accepted=False,new_correctness_grant=False,counts_unchanged=dict(solved=13,open=29,papers=93),
    frozen_active_campaigns_not_given342=[247,248],hot_feedback_sent=False,account_auth_runtime_environment_changed=False,protected_editor_open_unchanged=True)
out.write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(record=str(out),proof_sha256=sha(P),proof_bytes=P.stat().st_size,status=record['status']),indent=2))
