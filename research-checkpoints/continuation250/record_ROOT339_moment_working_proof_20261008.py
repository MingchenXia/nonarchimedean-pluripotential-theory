from pathlib import Path
from datetime import datetime, timezone
import hashlib, json

R=Path('/workspace/research'); K=R/'root-checks'
P=K/'P12.4-continuation339-mixed-multiplicity-moment-kernel-and-bounded-measures-working-proof-20261008.md'
route=K/'P12.4-continuation338-bounded-mixed-multiplicity-extension-working-route-20261008.md'
book=R/'primary-data-LOCALONLY/P12.2-conductor-integral-dependence-20261008'
D=K/'public-P12.2-continuation331-geometric-primary-model-and-full-conductor-original-candidate'
out=K/'P12.4-continuation339-ROOT-working-proof-source-scope-and-binding-20261008.json'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def entry(p):
    return dict(path=str(p),bytes=Path(p).stat().st_size,sha256=sha(p))
assert not out.exists()
lines=(book/'Swanson-Huneke-author-book.txt').read_text().split('\n')
units=[]
for a,b,role in [
    (16040,16165,'Complete17.2.1,17.2.2 statement/proof and17.2.4 statement/proof: simultaneous superficial choice with prime avoidance.'),
    (16308,16383,'Complete17.4.2 polynomial statement/proof and leading coefficient context.'),
    (16360,16575,'Complete17.4.3--8 immediate statements/proofs, mixed additivity and superficial reduction.'),
    (16575,16645,'Complete17.4.9 continuation/proof; beginning17.5.1.'),
    (16645,16830,'Complete17.5.1--5 continuation/statements/proofs, ending before17.6.')]:
    units.append(dict(LF_begin=a,LF_end=b,whole_immediate_unit_read=True,
        source_unit_sha256=hashlib.sha256('\n'.join(lines[a-1:b]).encode()).hexdigest(),role=role))
grant=[D/'P12.2-paper.tex',D/'mandatory-source-scope-and-reader-qualifications-after-review240-20261008.json',
    D/'source-application-ledger.md',D/'exact-scope.md',D/'whole-original-paper-acceptance-after-review240-20261008.json']
assert sha(grant[0])=='dadc8d064c849b80bbcb55d2c68217cd20a8c3056e3ca10ae729ac7b03537b80'
x=dict(recorded_utc=datetime.now(timezone.utc).isoformat(),atom='P12.4',continuation=339,
    status='UNREVIEWED algebraic moment working proof; original OPEN',proof=entry(P),route_dependency=entry(route),
    ROOT_whole_proof_physically_read=True,read_chunks='Characters0:12000 and12000:end; full route338 previously read. Entire339 reread after independent245.',
    only_qualified_correctness_grant='G331',complete_grant_import_requires_all=[entry(p) for p in grant],
    route338_is_unreviewed_local_argument_not_correctness_grant=True,
    private_primary_bindings=[entry(book/'Swanson-Huneke-author-book.pdf'),entry(book/'Swanson-Huneke-author-book.txt')],
    current_complete_ROOT_text_units=units,source_pixels_freshly_viewed=False,source_bodies_and_extracts_and_pixels_publish=False,
    source_hypotheses='Current July2024 author Swanson-Huneke; actual Noetherian local mixed-polynomial and superficial-element statements, arbitrary residue field via exact length-preserving R[t]_mR[t]. Historical Hilbert-Serre/Artin-Rees/Samuel foundations disclosed, not recursively freshly proved.',
    monotonicity_proof='Same simultaneous superficial elements for both compared families, same quotients until one-dimensional ordinary Samuel inequality. No inference of individual multivariate coefficients solely from polynomial domination.',
    results=['Primary powers/products and integral-closure invariance of mixed multiplicities.',
        'Positive rational ideal-difference moments depend on full geometric input FUNCTIONS, not ideal representatives; unique Radon representation.',
        'Uniform C and bounded actual-D extension, representation independence and bounded decreasing-net weak continuity via full route338.',
        'Exact arity n-1, gauge mu_b=T_*(v_a(b)mu_a), and finite normalization residue-weighted top-dimensional pushforward.',
        'Explicit zero-arity reduced-curve algebraic reference measure.'],
    essential_missing_original_obligations=['Actual Cartier intersection comparison for all negative curve-nef REAL primary-model presentations.','Locality on open subsets for bounded geometric potentials.'],
    no_nilpotent_intersection_or_unbounded_energy_or_full_finite_map_operator_claim=True,
    frozen_active_campaign246_not_given339=True,hot_feedback_sent=False,new_correctness_grant=False,
    original_closed=False,paper_accepted=False,counts_unchanged=dict(solved=13,open=29,papers=93),
    protected_editor_open_unchanged=True)
assert sha(K/'public-P16-round-46-final-reader/P16.4-paper.tex')=='09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
out.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(record=str(out),proof_sha256=sha(P),status=x['status']),indent=2))
