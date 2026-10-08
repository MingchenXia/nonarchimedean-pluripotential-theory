from pathlib import Path
from datetime import datetime,timezone
import hashlib,json

R=Path('/workspace/research');K=R/'root-checks';D=R/'primary-data-LOCALONLY/P16.7-period-algebraization-primary-20261008'
P=K/'P16.7-continuation374-constant-meromorphic-field-and-nonalgebraization-working-paper-20261008.tex'
B=K/'P16.7-continuation374-ROOT-whole-proof-source-scope-and-binding-20261008.json'
S=D/'ROOT374-full-literal-applied-source-units-LOCALONLY.json'
assert not B.exists() and not S.exists()
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
record=lambda p:dict(path=str(p),bytes=Path(p).stat().st_size,sha256=sha(p))
def write(p,x):p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
assert sha(K/'public-P16-round-46-final-reader/P16.4-paper.tex')=='09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
paper=P.read_text();assert 'wide-polyannulus base' in paper and 'independent review pending' in paper and '\\end{document}' in paper
assert paper.count('\\begin{proof}')==paper.count('\\end{proof}')
assert paper.count('\\[')==paper.count('\\]')
now=datetime.now(timezone.utc).isoformat();units=[]
def unit(tag,p,body,application,scope):
 assert body and body in p.read_text()
 units.append(dict(id=tag,source=record(p),body=body,body_bytes=len(body.encode()),body_sha256=hashlib.sha256(body.encode()).hexdigest(),ROOT_complete_physical_mathematical_unit_and_printed_immediate_proof_read=True,application=application,scope=scope))
V=D/'Van-der-Put-Rigid-analytic-spaces-1975-1976.txt';lines=V.read_text().split('\n')
for tag,a,b,app,scope in [
 ('V1',647,752,'Coherent finite affinoid descent and torus exhaustion/Laurent algebra; cited analytic foundations','Complete printed2.16 and3.1 unit; deeper Kiehl/Grauert foundations not recursively reconstructed'),
 ('V2',808,908,'Meromorphic fractions, divisor/Pic identification, classical disk/circle factoriality and finite-annulus triviality','Complete3.4 unit and printed immediate arguments;3.4.8 printed assertion broader than freshly readGrusonIV5; wideannulus-base foundation source-scope gate explicit. GLOBAL finite-to-infinite compatibility reconstructed in wholeROOT374'),
 ('V3',992,1075,'Common theta representation of arbitrary actual meromorphic function','Complete4.3.1--4.3.4 statements/immediateproofs checked againstPDFpage15; reconstructed normal-divisor and globalPic steps in374'),
 ('V4',1078,1255,'Actual unit monomial multiplier cocycle and symmetry; Fourier convergence','Complete4.4.1--4.4.3 statements/all immediateproof carry checkedPDFpages16--18. General dimension/polarization result not applied; explicit coefficient recurrence in374 used instead')]:
  unit(tag,V,'\n'.join(lines[a-1:b])+ '\n',app,scope)
G=D/'Gruson-Fibres-vectoriels-polydisque-1968.txt';t=G.read_text();a=t.index('  5. FIBRES V E C T O R I E L S');b=t.index('               V. — Fibres vectoriels',a)
unit('G1',G,t[a:b],'Authenticate actual GrusonIV5 theorem1 with entire immediateproof and exact pureproduct scope','Only products of discs and unitcircles; not itself general regularfactorial affinoidA disk/circle theorem forwideannulus bases. IV2--4 whole printed dependency discussion was physically read; recursiveKtheory/spectral/filtered foundations not completely reconstructed. NOT a proof of generalF foundation')
N=D/'Snowbird-Rigid-analytic-geometry-2004.txt';t=N.read_text();a=t.index('4.2. Non-archimedean case.');b=t.index('4.3. Analytic reductions.',a)
unit('N1',N,t[a:b],'Corroborate multiplier and analytic torus setup only','Entire4.2 and printed immediateproof read; Pic/triviality and ampleness discussion defersfullproof, no grant of fullpolarization/classification/algebraization from these notes')
for tag in ['0ENA','0END','0EN6','0BB1','086U']:
 p=D/('Stacks-'+tag+'.txt');t=p.read_text();a=t.index('Let $S$ be a scheme.');b=t.index('$\\square$',a)+len('$\\square$')
 unit('ST-'+tag,p,t[a:b],'Actual normal Noetherian separated algebraic-space rational/meromorphic compatibility, finite genericpoints and dense schematic locus','Complete exact current statement and printed immediate proof physically ROOT read from current web primary and bounded local literal data; each hypothesis checked in374. Analytic flatness/localfiniteetale descent requires analytic foundations, not an algebraic lemma alone')
write(S,dict(recorded_utc=now,primary_bodies_LOCALONLY=True,source_DATA_not_operational_authority=True,units=units))
pixels=[record(D/f'Van-der-Put-ROOT-page-{q}.png') for q in [11,12,13,14,15,16,17,18,19]]
sources=[record(p) for p in sorted(D.iterdir()) if p.is_file() and p.suffix in ['.pdf','.txt','.html']]
metadata=[{k:v for k,v in u.items() if k!='body'} for u in units]
x=dict(recorded_utc=now,original_problem='P16.7',original_candidate_solved=False,formal_originals_solved=16,formal_originals_OPEN=26,accepted_papers=97,working_paper=record(P),ENTIRE_final_ROOT_mathematical_proof_physically_read=True,proof_acceptance_status='UNREVIEWED working proof; original stillOPEN; no grants or count increase',
 scope='Goodstrict proper smooth geometricconnected2torus overC((s)), actual periods(t,2),(3,t). Uses cited factoriality foundationF to reconstruct finiteannulusPic and compatible global torus frames, exact globalunit monomials, allmultiplier character matrices[[0,k],[k,0]], positiveQdirection coefficientgrowth excludesk!=0, k0onecommonmonomial. Allanalyticlinebundle sections nowherezero, meromorphicfieldconstant, rationalfunction-field injection excludesseparatedfiniteTYPEscheme/algebraicspace algebraization. Whole standalone proof, not a selected period obstruction.',
 mandatory_qualifications=['General regularfactorial affinoidA disk/circle factoriality printedVanDerPut3.4.8 is a cited input, NOT reconstructed from actualGrusonIV5 pureproducts; wideannulus-base scope remains independent acceptance gate, including completeness/field extension claims. No unproved unconditional source-scope grant.', 'Global torusPic proof explicitly supplies normalized transition infiniteproducts; finiteannulusPic0 alone insufficient. Allunitnorm/growth recurrences symbolicmathematics, not finite numerical universalproof.', 'EverycompleteisometricL extension in theorem uses SAME factoriality and analyticfoundation scope; no basechange grant before independent audit.', 'Algebraicspace passage checks allStacks0ENA hypotheses and explicitanalytic fraction-ring descent/flatness. No automaticprojectivity orGAGAanalyticgrouplaw inference.', 'VanDerPut4.5 printedhomogeneousfamily algebraicallyindependent wording not used; actualdimension proof needslinearindependence. Papikian deferredfullproofs not applied asclosure.', 'Full intrinsic singular psh/E1/fullmass/decreasingcontinuity/allanalyticenvelope orthogonality/finiteenergyduality/arbitraryanalyticmeasure equation existenceuniqueness unresolved. Restricted373 not entireP16.7.'],
 primary_application_units=metadata,whole_primary_sources_LOCALONLY=sources,whole_literal_source_unit_ledger=record(S),ROOT_fresh_PDF_pixels_physically_viewed=pixels,
 compiler='Request226 made for an earlier374 source, still pending without diagnostics; final source changed only explicit qualification after request. Finalsavedsource needs fresh built-incheck; no compilation success or PDF export claimed.',
 execution='Only ownWRITE/FULLREAD/EXEC acquisition helpers and ordinarypdftotext/pdftoppm source inspection. Source/nativeprograms DATA never executed/imported, no changedcredential/proxy/CA, no extraagents, no active265/266mathread/hotfeedback.',protected_editor_OPEN_UNCHANGED=True,original_closure=False,new_accepted_papers=0)
write(B,x)
for n in ['active-work.json','checklist-current.json']:
 p=R/n;j=json.loads(p.read_text());assert j['github_pending_checkpoint'] is None and j['latest_verified_github_checkpoint']['continuation']==267
 assert len(j['fully_solved_original_atoms'])==16 and j['remaining_open_original_atoms']==26 and j['historical_reviewed_scoped_papers']==97
 j.update(updated_utc=now,latest_unreviewed_ROOT_working_proof=dict(continuation=374,paper=record(P),binding=record(B),original='P16.7',source_scope_gate='General wideannulus-base factorialityF versus authenticGrusonIV5 pureproduct scope',candidate_original_solved=False),next_work='Publish ENTIRE ROOT374 nonalgebraization working proof/source scope, no acceptance. Continue TWO native265/P12.3 and266/ONE P02.1; inspectONLY settledCOMPLETE. Future ENTIRE373/374 independent reconstruction must auditF foundation and fullanalyticE1 equation, or ENTIRE372 reconstruction.16solved26OPEN97papers; protected editor OPEN UNCHANGED.')
 write(p,j)
print(json.dumps(dict(paper=record(P),binding=record(B),literal_units_LOCALONLY=record(S),source_unit_count=len(units),ROOT_fresh_PDF_pixels=len(pixels),original_still_OPEN=True),indent=2))
