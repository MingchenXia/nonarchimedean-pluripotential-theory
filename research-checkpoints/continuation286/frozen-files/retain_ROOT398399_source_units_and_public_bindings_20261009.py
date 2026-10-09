from pathlib import Path
from datetime import datetime, timezone
import hashlib, json
R=Path('/workspace/research'); K=R/'root-checks'
D=R/'campaigns/round-267/P16.7-whole373374-nonalgebraization-and-intrinsic-E1/private-primary-DATA-LOCALONLY'
U=R/'primary-data-LOCALONLY/P16.7-ROOT398-rational-domains-and-PH-source-20261009'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def entry(p):
    p=Path(p); return dict(path=str(p),bytes=p.stat().st_size,sha256=sha(p))
def write(p,x): p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
sources={
 'CLD':D/'004-004-CLD-literal_extract.txt',
 'Van-der-Put':D/'051-Van-der-Put-Rigid-analytic-spaces-1975-1976.txt',
 'Papikian':D/'026-Snowbird-Rigid-analytic-geometry-2004.txt',
 'GR':R/'primary-data-LOCALONLY/P16.7-classical-PSH-Shilov-GR-v2-primary-20261009/GR2506.13548v2-full-LOCALONLY.txt'}
assert sha(sources['CLD'])=='64846cb00926267c6238d1afac61b5eaed0a0e3a6349725738f9b1bf163de085'
units=[
 ('CLD',7872,7889,'proper current pushforward definition; full immediate passage', [399]),
 ('CLD',7983,8020,'scalar Radon-current recognition; entire7.2.8 statement and immediate proof',[398,399]),
 ('CLD',9427,9431,'restriction and proper push commute with both differentials; whole7.7.8',[399]),
 ('CLD',10249,10609,'whole immediate continuous products/dpsh units8.5--8.8;8.6.7 read but NOT premise',[398,399]),
 ('CLD',16501,16525,'torus Gauss point norm and analytic carrier12.1.2',[399]),
 ('CLD',16577,16595,'whole canonical Gauss section12.1.5',[399]),
 ('CLD',16650,16709,'whole12.1.8 scalar extension Gauss section statement and immediate proof; application only(a)',[399]),
 ('CLD',20924,20935,'whole14.4.3 finite-ground-field calibration factor and immediate proof',[399]),
 ('CLD',21710,21743,'whole15.3.1--2 base-change integration statements and immediate proofs; application15.3.1',[399]),
 ('CLD',22158,22170,'whole16.1.1 integration-current base change and immediate proof',[399]),
 ('CLD',23458,23671,'whole16.7.3 Poincare--Lelong statement and immediate proof; freshly ROOT read for396397398',[398,399]),
 ('Van-der-Put',1,100,'field and completed Tate series definitions; bounded text reading; not whole-source read',[398,399]),
 ('Van-der-Put',128,151,'finite residue statement1.6 and immediate reference to1.2; no entire deeper proof claimed',[399]),
 ('Van-der-Put',261,360,'whole2.1--2.2 rational presentation and immediate universal-property proof; actual pixels05--06 repair OCR',[398,399]),
 ('Papikian',1,68,'complete nonarchimedean field setup; erroneous ring-inequality OCR not premise',[398,399]),
 ('Papikian',198,310,'Tate series/rational presentation and3.2(d) finite residue statement; corroboration, no full immediate proof printed',[398,399]),
 ('GR',1833,1945,'whole7.1--7.6 immediate statements/proofs;7.8 read but NOT premise;398 classical PH criterion only',[398])]
unit_records=[]
for key,a,b,scope,papers in units:
    full=sources[key].read_bytes().splitlines(keepends=True)
    assert 1<=a<=b<=len(full)
    p=U/f'{key}-literal-LF{a}-{b}-LOCALONLY.txt'
    body=b''.join(full[a-1:b]).decode('utf-8'); p.write_text(body)
    assert p.read_text()==body
    unit_records.append(dict(**entry(p),source=entry(sources[key]),literal_LF_first=a,literal_LF_last=b,scope=scope,papers=papers,ROOT_physically_read_untruncated=True,all_deeper_recursive_proofs_freshly_read=False,upload=False))
pixels=[U/f'Van-der-Put-original-page-{n:02}.png' for n in [3,5,6]]
assert all(p.exists() for p in pixels)
pdfs=[D/'050-Van-der-Put-Rigid-analytic-spaces-1975-1976.pdf',D/'025-Snowbird-Rigid-analytic-geometry-2004.pdf']
assert all(p.exists() for p in pdfs)
now=datetime.now(timezone.utc).isoformat()
private=dict(recorded_utc=now,full_text_sources={k:entry(p) for k,p in sources.items()},full_PDF_sources=[entry(p) for p in pdfs],literal_units=unit_records,actual_pixels=[dict(**entry(p),original_PDF_page=n,ROOT_actual_pixels_viewed=True,upload=False) for n,p in zip([3,5,6],pixels)],all_primary_bodies_units_pixels_LOCALONLY=True)
write(U/'ROOT-whole-source-unit-and-pixel-retention-LOCALONLY.json',private)
public=dict(recorded_utc=now,public=True,full_sources=[entry(p) for p in sources.values()]+[entry(p) for p in pdfs],units=unit_records,actual_pixel_metadata=private['actual_pixels'],source_bodies_embedded=False,qualified_reading='All listed applied statements and immediate available proof passages physically read untruncated in ROOT. Primary proof bounds do not assert fresh whole recursive source audits. Van-der-Put actual pixels03,05,06 viewed; Papikian statements corroborate without printed whole proofs. Current399 needs no classical all-curve/all-extension recognition assumption.',original_P16_7_closed=False,accepted=False,solved=16,remaining_open=26,accepted_scoped_papers=97)
B=K/'ROOT398399-fresh-primary-application-and-compilation-scope-20261009.json'
for n in [398,399]:
    label={398:'local-analytic-divisor-tests-and-pluriharmonic-defects',399:'bounded-continuous-uniqueness-by-coordinate-curves'}[n]
    p=K/f'P16.7-continuation{n}-{label}-working-paper-20261009.tex'
    compiler=dict(path=str(p),kind='success',message='Current saved source compiled successfully with the built-in desktop editor compiler; ROOT observed explicit success after whole current source read.')
    record=dict(recorded_utc=now,paper=n,whole_paper=entry(p),ROOT_whole_current_mathematical_body_physically_read_untruncated=True,compiler=compiler,source_application_record=str(B),status='UNREVIEWED',accepted=False,original_closed=False,scope=('Local analytic principal divisor-current annihilation and sufficient classical PH criterion' if n==398 else 'Actual bounded continuous MA uniqueness modulo constants on the specified torus quotient; coordinate curves, finite Galois signed Radon descent and bounded Gauss-ray Liouville'),remaining='Full unbounded generated finite-energy intrinsic recognition, compactness, envelopes, orthogonality, arbitrary-support equation existence and full-domain uniqueness',incoming_grants=[],new_material_sent_to_active_native278279=False,protected_editor_OPEN_UNCHANGED=True)
    write(K/f'P16.7-continuation{n}-ROOT-whole-paper-source-scope-and-binding-20261009.json',record)
public['papers']=[entry(K/f'P16.7-continuation{n}-ROOT-whole-paper-source-scope-and-binding-20261009.json') for n in [398,399]]
assert sha(K/'public-P16-round-46-final-reader/P16.4-paper.tex')=='09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
write(B,public)
for name in ['active-work.json','checklist-current.json']:
    p=R/name; x=json.loads(p.read_text()); assert x['github_pending_checkpoint'] is None
    assert len(x['fully_solved_original_atoms'])==16 and x['remaining_open_original_atoms']==26 and x['historical_reviewed_scoped_papers']==97
    x.update(updated_utc=now,ROOT398399_working_papers=dict(record=str(B),paper_bindings=public['papers'],UNREVIEWED=True,original_closed=False,accepted=False,source_bodies_LOCALONLY=True,protected_editor_OPEN_UNCHANGED=True),next_work='Publish286 whole398399 and qualified source/compiler metadata. Native278279 independent at mostTWO. Bounded uniqueness working proof exists; full unbounded/compactness/existence remain OPEN. No active-math inspection or hot feedback; no countchange.')
    write(p,x)
print(json.dumps(dict(papers=[398,399],public_binding=str(B),private_units=len(unit_records),actual_pixels=3,compiled=True,original_closed=False,accepted=False),indent=2))
