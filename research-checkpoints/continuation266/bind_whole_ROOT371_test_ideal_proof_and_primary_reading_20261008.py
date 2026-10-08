from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,shutil

R=Path('/workspace/research');K=R/'root-checks';D=R/'primary-data-LOCALONLY/P12.3-test-ideal-uniform-approximation-20261008'
P=K/'P12.3-continuation371-test-ideal-uniform-approximation-on-smooth-primary-models-working-paper-20261008.tex'
B=K/'P12.3-continuation371-ROOT-whole-proof-source-scope-and-binding-20261008.json'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def bound(p):return dict(path=str(p),bytes=p.stat().st_size,sha256=sha(p))
def write(p,x):p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
assert not B.exists() and sha(P)=='152b79a85a21a0fc70011d758982d7c85366ca9f69a239369609e9302f750506'
assert sha(K/'public-P16-round-46-final-reader/P16.4-paper.tex')=='09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
G=R/'shared-sources/P16-completion-envelopes-arxiv-1712.00980-20261004.txt'
assert sha(G)=='2cfdf8ae09038a52e9e84b2cf58ac301002e37f5c9c24896cbe1717d694f5b51'
M=D/'Mustata-non-nef-locus-public.txt';assert sha(M)=='2c19d7f09ee3f20248ab2ac8b73fcbc52a1e158db11501e53497c90a786f473b'
Q=R/'primary-data-LOCALONLY/P12.2-relative-geometry-20261008/Keeler-ample-filters-corrected-v5.txt'
sources=[]
for name,text in [('GJKM',G),('Mustata',M),('Keeler',Q)]:
 for p in [text.with_suffix('.pdf'),text]:
  assert p.is_file();dest=D/(name+'-whole-primary'+p.suffix)
  if dest.exists():assert dest.read_bytes()==p.read_bytes()
  else:shutil.copyfile(p,dest)
  sources.append(dict(id=name,**bound(dest),origin=str(p)))
units=[]
def unit(id,body,scope,application,reading):
 units.append(dict(id=id,literal_complete_immediate_unit=body,unit_sha256=hashlib.sha256(body.encode()).hexdigest(),unit_bytes=len(body.encode()),exact_source_scope=scope,application=application,ROOT_physical_reading=reading,recursive_background_disclosed=True))
s=G.read_text();a=s.index('4. Asymptotic test ideals',4000);z=s.index('5. Descent for model functions',a)
unit('GJKM-whole-Section4',s[a:z],'Perfect field of positive characteristic, smooth integral finite-type variety; Theorem4.6 projective over finite-type affine k-base with ample globally generated H, nonzero sections, E-lambdaD NEF','ROOT371 asymptotic ideals b_m subset t_m and t_ml subset t_m^l; UG at D=C,E=mC,lambda=m,zero nef difference, fixed H negative effective ample primary divisor; entire4.6 proof read, not analyticSections7--9 imported','Retained authentic full text printed whole Section4 after repairing initial ToC extraction; duplicate historical excerpts not called fresh source reading')
s=M.read_text();a=s.index('3. Asymptotic test ideals');b=s.index('4. A uniform global generation result',a);z=s.index('5. Applications to asymptotic test ideals',b)
unit('Mustata-whole-Section3',s[a:b],'Section3 explicitly says perfect k suffices for smooth-variety test-ideal construction; full Proposition3.1(i)--(iv) and immediate proof,3.2--3.3 statements/proofs read','Underlying asymptotic ideal containment/subadditivity applied via exact GJKMperfect-field statement; 3.2/3.3 are read background, not needed for the uniform estimate','Fresh public arXiv1109.3825v2 authentic title30April2012, full text printed0:21000/20500:36500, full Section3 included; no PDFpixel reading claim')
unit('Mustata-whole-Section4',s[b:z],'Smooth PROJECTIVE variety over ALGEBRAICALLY CLOSED positive-characteristic field; Theorem4.1 and ENTIRE proof plus4.2','Source proof of trace surjection/Frobenius projection/CM regularity/finitely many rational rounding twists/Fujita; used ONLY as background to GJKM4.6 published generalization to finite-type affine base/perfect k, not directly extrapolated','Fresh full Section4 whole immediate proof physically read in20500:36500 output, no truncated proof')
l=Q.read_text().split('\n')
for id,a,z in [('Keeler-1.5-statement-with-context',78,135),('Keeler-1.5-whole-immediate-proof',1220,1269),('Keeler-entire-erratum',1780,len(l))]:
 unit(id,'\n'.join(l[a-1:z])+'\n','Noetherian affine base, projective scheme, ample invertible sheaf, uniform vanishing for ALL nef invertible sheaves; corrected v5 with entire erratum','GJKM4.6 uniform-generation proof and one fixed ample Serre twist. ErratumE2.5 validates1.5 reduction via finite faithfully flat base change; no perfect/smooth base assumption added','Entire stated LF windows printed separately in one bounded nontruncated result, whole erratum1780:end read; not a whole-Keeler/PDFpixel claim')
private=D/'ROOT371-full-literal-applied-source-units-LOCALONLY.json';write(private,dict(recorded_utc=datetime.now(timezone.utc).isoformat(),sources=sources,units=units))
public=[{k:v for k,v in u.items() if k!='literal_complete_immediate_unit'} for u in units]
now=datetime.now(timezone.utc).isoformat()
write(B,dict(recorded_utc=now,atom='P12.3',whole_working_paper=bound(P),status='WHOLE unreviewed ROOT proof; future independent reconstruction pending; no correctness grant',
 ROOT_entire_paper_physically_read=True,ROOT_paper_reading='Initial whole source0:14500/14000:end plus full FINAL17741byteTex printed entirely after proper-J and source-qualification repairs; no truncated final proof',
 whole_primary_sources=sources,whole_immediate_applied_unit_metadata=public,whole_literal_primary_ledger_LOCALONLY=bound(private),
 theorem='Normal CLOSED affine algebraic germ over perfect characteristicp>0 field dim>=2; FIXED ACTUAL smooth primary blowup principalizing gauge and carrying Cartier obstacle. Actual section ideals pointwise raw envelope via fullsupport normal Cartier orders and rational-primary-density; asymptotic test ideals +UG produce actual primary profiles g_m <=P(f_C)<=g_m+c v(J)/m on ENTIRE normalized boundary. Uniform convergence givesC before anyD/energy recognition.',
 extension='ALL finite continuous obstacles ONLY IF (SM): every finiteprimaryideal collection/gauge admits ACTUAL smooth primary common blowup on one shrunk normal affine neighbourhood. Signed-profile density plus nonexpansivity. SM not proved; CP3/unconditional positivechar excellent extension NOT claimed.',
 source_scope='GJKM4.6 is algebraic on smoothY/perfectk/projectivefinite-typeaffinebase; no use of discrete-field analytic equation endpoint. Mustata3 explicitly perfect; Mustata4.1 PROJECTIVEalgclosed scope kept, GJKM supplies generalization. Keelercorrected1.5 and ENTIREerratum checked; BMS ordinary subadditivity/CM/Serre/coherent/Hartogs recursive foundations disclosed, not freshly recursively reconstructed.',
 only_existing_grants=['ENTIRE qualified G331 with every mandatory actualmodel/Keelererratum/SHfinitequotientcolon/support/gauge/class annotation'],
 current_compilation='Built-in compiler requested cell146 against this frozen source; no diagnostic/success at binding. Separate370 compiler cell125 remains pending. No source changed after146 request, no tabs/exportPDF.',
 original_closed=False,new_accepted_paper=False,formal_solved=16,formal_OPEN=26,accepted_papers=97,formal_verification=False,compiler_success=False,
 source_documents_and_programs_DATA=True,supplied_programs_executed_or_imported=False,primary_bodies_pixels_LOCALONLY=True,other_ACTIVE_math_read_or_supplied=False,hot_feedback_sent=False,held_until_future_independent_reconstruction=True,protected_editor_open_unchanged=True))
for n in ['active-work.json','checklist-current.json']:
 p=R/n;x=json.loads(p.read_text());assert len(x['fully_solved_original_atoms'])==16 and x['remaining_open_original_atoms']==26 and x['historical_reviewed_scoped_papers']==97
 x.update(updated_utc=now,ROOT371_unreviewed_test_ideal_uniform_approximation=dict(whole_paper=bound(P),whole_proof_source_scope_binding=bound(B),original_closed=False,new_accepted_paper=False,held_until_future_independent_reconstruction=True,no_ACTIVE_feedback=True));write(p,x)
print(json.dumps(dict(whole_paper=bound(P),whole_binding=bound(B),fresh_primary_units=len(units),sources=len(sources),literal_primary_ledger_LOCALONLY=bound(private),original_closed=False,new_accepted_paper=False),indent=2))
