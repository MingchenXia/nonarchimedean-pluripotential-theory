from pathlib import Path
from datetime import datetime,timezone
import hashlib,json

R=Path('/workspace/research');K=R/'root-checks';W=K/'P12.3-continuation355-excellent-normal-surfaces-primary-model-nef-projection-and-continuous-envelopes-working-proof-20261008.md'
B=K/'P12.3-continuation355-ROOT-whole-working-proof-source-scope-and-binding-20261008.json'
P=R/'primary-data-LOCALONLY/P12.3-normal-surface-geometric-envelopes-20261008'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
assert not B.exists()
source=[]
for e in json.loads((P/'acquisition-records.json').read_text()):
    for kind in ['html','text']:
        p=Path(e[kind+'_path']);assert p.stat().st_size==e[kind+'_bytes'] and sha(p)==e[kind+'_sha256'];source.append(dict(path=str(p),bytes=p.stat().st_size,sha256=sha(p),source_url=e['url'],LOCALONLY=True))
old=next((R/'campaigns/round-255').iterdir());rel=next(e for e in json.loads((old/'private-primary-packet-bindings.json').read_text()) if Path(e['path']).name=='Stacks-0D2N.txt')
assert sha(rel['path'])==rel['sha256'];source.append(rel)
assert sha(K/'public-P16-round-46-final-reader/P16.4-paper.tex')=='09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
now=datetime.now(timezone.utc).isoformat();proof=dict(path=str(W),bytes=W.stat().st_size,sha256=sha(W))
record=dict(recorded_utc=now,continuation=355,atom='P12.3',status='ENTIRE new working proof UNREVIEWED; originalOPEN and no acceptedpaper',proof=proof,ROOT_whole_reading='Entire current savedproof physically read by fullcat without truncation. Whole immediate primary statements/proofs0BGJ0BGP0AY80B5Y0AX7 andexisting0D2N freshlyread; no newsourcepixels orrecursivecompleteLipmanproofclaim.',only_correctness_prerequisite='ENTIRE qualifiedG331 geometriccone/PRIMARYcomparison/fullsection topology, finiteMAX/scaling/uniformclosure anddenseideal-differencelattice withwholemandatorysource/scope',new_theorem='All excellent NORMAL LOCAL SURFACES, arbitrary/imperfect/mixedcharacteristic andeveryprimarygauge: finitecontinuous obstacles havegreatestC/Dminorant inC. BoundedaboveextendedUSC obstacles havegreatestDminorants viaoneactualC-net; all decreasingUSCobstaclenets stable.',new_proof='ResolveFINITEchosenprimarymodels byprojective normalizedblowups; actualconnectedclosedcurveintersectionmatrixnegative definite fromreferencevectorb andexplicitquadraticidentity; positiveintegralboundaryample=>usedregularmodelACTUALprimaryBl_I. Nefpushforwardandprincipal-submatrixnegativity givefinitevertexprojectiondominatingEVERY C andboundedDcompetitoratFULLsupports. CompactcoordinateMAXstablepolytopegreatestnefvectorcomputesFULL envelope; wholedenseprofileuniformapprox coversALLcontinuousobstacles. NoSNC/retractionsneeded.',private_primary_metadata=source,published_background='Exact0BGPtwo-dimensionalLipman conditions checkedviaexcellence; finite normalization/projectiveblowups/Steinconnectedness/curvepositive-degreeampleness/fibrewise relativeampleness. RecursiveLipmanrational-singularity/desingularizationfoundations, propercoherence, relativeSerre generation andCartierdegreeprojection remainordinarypublishedinputs, notfreshlyreproved.',scope='Onlydimension<=2 normaldomains; arbitrarynormaldimension>=3 remainsOPEN. Nohigherdimnefpushforward/allmodelcofinality, universalnon-normalconductorcommutation, CLD/classicalrecognition, literalradialidentity, sourceacceptanceorcompilerPDFclaim.',source_bodies_pixels_LOCALONLY=True,original_closed=False,accepted_paper=False,protected_editor_open_unchanged=True,no_extra_jobs_or_supplied_programs=True)
B.write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n')
for name in ['active-work.json','checklist-current.json']:
    p=R/name;x=json.loads(p.read_text());assert len(x['fully_solved_original_atoms'])==15 and x['remaining_open_original_atoms']==27 and x['historical_reviewed_scoped_papers']==96 and x['github_pending_checkpoint'] is None
    x.update(updated_utc=now,P12_3_ROOT355=dict(proof=proof,binding=str(B),status=record['status']),next_work='ReadENTIRE completed254255math/source/scopebeforeacceptance. Freeze new355normalSURFACEmatrix/PRIMARYproof forindependentnewnative, plus356specifiedregularizedfinite-mapcalculus toaddress255residual.15solved27OPEN96papers,currentlynoactivecalls,verifiedGitHub257,compile1010pending,protectededitorOPENUNCHANGED.')
    p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(ROOT355=proof,binding=str(B),primary_metadata=len(source),counts_unchanged=True),indent=2))
