"""Own report assembly and integrity checks; executes no supplied program."""
import hashlib,json,pathlib,re

OWN=pathlib.Path(__file__).resolve().parent
BASE=pathlib.Path('/workspace/research/campaigns/round-215/P05.2-unchanged-all-continuous-affine-arrangement-independent-native-local-source-audit')
def load(p): return json.loads(pathlib.Path(p).read_text())
def save(name,data): (OWN/name).write_text(json.dumps(data,indent=2,ensure_ascii=False)+'\n')
math=load(BASE/'mathematical-packet-bindings.json')
history=load(BASE/'historical-own-evidence-bindings.json')
primary=load(BASE/'private-primary-packet-bindings.json')
binding=load(OWN/'frozen-file-bindings.json')
for row in binding:
    raw=pathlib.Path(row['path']).read_bytes()
    assert len(raw)==row['bytes'] and hashlib.sha256(raw).hexdigest()==row['sha256']

summaries=[
 ('Five whole grants and primary applications pass with explicit scope; no extra ROOT grant or automatic acceptance.',
  'A224/B225/R230/S262/S272 and every clarification are the only theorem premises. All 27 mathematical bodies were read. Raw primitive/unit-normal calibration and whole original BBGS/BMPS application units were checked. Recursive granted foundations, literal/abstract distinctions and Native210 evidence limits remain explicit.'),
 ('Affine duality, global same-reference rational-geometry REAL PA approximation and finite raw contact pass.',
  'Continuous printed PC equals ordinary full-plane convexity with legal incidences and rational-face density. Boundary dual continuity, exact rec generators, finite rational primal samples with real heights, closed epigraph generation, global conjugate error, rational projected faces and actual decreasing extraction are reconstructed. Finite unrestricted envelopes and saturated flat-lineality raw zero are checked.'),
 ('Legal finite trees and existing-domain measure limits prove all-C_b affine contact under the stated grants.',
  'Bellman infima and monotone fixed points equal the actual envelope; near-optimal trees have compact proper-height tails. SAME-reference DC auxiliaries give supported signed-TV bounds and mixed telescoping for two already completed tuples. Independent endpoint membership and fixed-C moments precede weak/contact limits; compact PA approximation is local only.'),
 ('Primitive determinant and positive subcycle obstruction yield the exact affine-arrangement iff disjoint sector.',
  'All primitive quotient indices, repeated-factor zero and d! surviving orders give c 2^d d! |det A|. Effective balanced residual and a legal rational transverse flat PCC meet S272 actual-reference jet/roof hypotheses. Separated components give componentwise actual envelopes, synchronized global approximation and raw locality. General singular/literal/abstract cases remain separate.'),
 ('Overall INCONCLUSIVE: scoped mathematics PASS; historical universal action claims remain unverified. Original OPEN, candidate=false.',
  'All four exact FINAL notes differ from saved prose; registered result appends only its bound artifact suffix. All 77 bindings, 26 author artifacts, 20 normalization positions and semantic parent/child equality pass. Own finite output is byte-equal and unchanged TeX converts exactly and builds twice; first-pass warnings are preserved. These facts do not prove historical read/no-operation assertions or complete original P05.2.')]
supports=[[],['n1'],['n1','n2'],['n1','n2','n3'],['n1','n2','n3','n4']]
notes=[{'id':f'n{i+1}','summary':s,'detailedSummary':d,'text':(OWN/f'note-n{i+1}.txt').read_text().strip(),'support':supports[i]} for i,(s,d) in enumerate(summaries)]
for i,n in enumerate(notes):assert all(x in [m['id'] for m in notes[:i]] for x in n['support'])
save('native-notes.json',{'notes':notes,'candidate':False})

readlog=[json.loads(l) for l in (OWN/'read-log.jsonl').read_text().splitlines()]
body_coverage=[]
for i,e in enumerate(math):
    lines=pathlib.Path(e['path']).read_text().splitlines();seen=set();ranges=[]
    for r in readlog:
        if r['packet']=='math' and r['index']==i:
            seen.update(range(r['start'],r['end']+1));ranges.append([r['start'],r['end']])
    missing=sorted(set(range(1,len(lines)+1))-seen);assert not missing
    body_coverage.append({'index':i,'file':pathlib.Path(e['path']).name,'whole_lines':len(lines),'returned_ranges':ranges,'missing_returned_lines':missing,'reviewed_whole_body':True,'status':'grant' if e['grant'] else 'DATA','read_flag_is_not_mathematical_proof':True})

grants=[
 {'id':'A224','indices':[0,1],'use':'fan-specific context only; no general classification inferred'},
 {'id':'B225','indices':[2,3],'use':'embedded support/maximum principle and distinction from abstract compact charts'},
 {'id':'R230','indices':[4,5],'use':'continuous completion and unrestricted-envelope identification, real endpoints, bounded-reference sandwich; no density premise'},
 {'id':'S262','indices':[6,7,8,9],'source_DATA_indices':[10,11],'use':'finite raw foundations, corrected continuity scopes, separate graph and literal results'},
 {'id':'S272','indices':[12,13,14,15],'source_DATA_indices':[16,17],'use':'actual-real-reference genuine mixed completion, same-reference compact-test auxiliaries, all-tuple fixed-C moment and rational jet/roof'}]
assert len(grants)==5
sections=[
 (1,43,'Title/abstract and exact limited claims',['n1','n2','n3','n4']),
 (44,105,'Definitions, raw formula, actual domain, five grants, granted moment and exclusions',['n1']),
 (106,157,'Covolumes, primitive conversion, whole original applications, positivity, symmetry, IBP and mass',['n1']),
 (158,250,'PC versus full-plane convexity, support duality, real max reference, rec cones and boundary conjugate continuity',['n2']),
 (251,348,'Global primal roof construction, exact conjugate, projected rational faces, decreasing extraction and unrestricted finite envelope',['n2']),
 (349,396,'Noncontact strict floor, flat PCC, full-plane rational lineality, saturated recursion/refinement and finite contact',['n2']),
 (397,447,'Legal-tree Bellman fixed point and actual envelope, finite real splits, near-optimal trees and proper-height tail estimate',['n3']),
 (448,487,'Supported signed-TV DC bounds, finite mixed telescoping, two completed tuples, fixed-C moment before weak limit',['n3']),
 (488,526,'Local-only compact rational PA obstacle approximation, independently completed endpoints and bounded contact tails',['n2','n3']),
 (527,606,'Primitive determinant all dimensions, repeated factors, positive complete subcycle/residual, actual-reference jet and roof witness',['n4']),
 (607,664,'Rational arrangement intersections, explicit residual, positive component separation, all incidence and actual envelope componentwise, global synchronized approximation and raw locality',['n4']),
 (665,744,'Literal, zero-dimensional, abstract/general-singular scope, non-PA example, finite and build evidence and source ledger',['n1','n4','n5'])]
units=[]
tex=pathlib.Path(math[22]['path']).read_text().splitlines()
starts=[]
for j,l in enumerate(tex,1):
    m=re.search(r'\\begin\{(lemma|theorem|proposition|corollary)\}.*?\\label\{([^}]+)\}',l)
    if m: starts.append((j,m.group(1),m.group(2)))
for k,(start,kind,label) in enumerate(starts):
    proof_end=next(j+1 for j in range(start-1,len(tex)) if tex[j].strip()=='\\end{proof}')
    ids=['n2'] if start<397 else ['n3'] if start<527 else ['n4']
    units.append({'number':k+1,'kind':kind,'label':label,'LF_statement_and_proof':[start,proof_end],'verdict':'PASS','reasoning_notes':ids})
assert len(units)==12
equations=[]
for j,l in enumerate(tex,1):
    if '\\label{' in l and not re.search(r'\\begin\{(?:lemma|theorem|proposition|corollary)\}',l):
        equations.append({'LF':j,'labels':re.findall(r'\\label\{([^}]+)\}',l),'verdict':'PASS','reasoning_notes':next(n for a,b,_,n in sections if a<=j<=b)})
coverage={'kind':'own whole-proof coverage, not automated theorem validation','exact_grant_group_count':5,'grant_groups':grants,'body_coverage':body_coverage,'paper_sections':[{'LF':[a,b],'claims':t,'verdict':'PASS','reasoning_notes':n} for a,b,t,n in sections],'numbered_statement_proofs':units,'numbered_equations':equations,'unnumbered_claims':'Every LF is assigned above; support, incidence/density, recession, graph-face geometry, envelope, locality, limit, sources and scope have explicit reasoning in n1-n5. Displayed formulas without labels are included in their whole section.','parallel_argument':{'file':math[23]['path'],'LF':[1,700],'reviewed_whole':True,'source_to_markdown_bytes_equal':True,'reverse_equivalence_claimed':False,'reasoning_notes':['n1','n2','n3','n4','n5']},'NEW_ledger_scope':{'indices':[24,25],'reviewed_whole':True,'reasoning_notes':['n1','n4','n5']},'exact_FINAL':[{'id':'n1','mathematical_verdict':'PASS','historical_read_flags':'INCONCLUSIVE as past-action evidence','own_reasoning':['n1','n5']},{'id':'n2','mathematical_verdict':'PASS','own_reasoning':['n2','n3']},{'id':'n3','mathematical_verdict':'PASS','own_reasoning':['n4']},{'id':'n4','finite_build_conversion_verdict':'PASS','historical_universal_action_verdict':'INCONCLUSIVE','own_reasoning':['n5']}],'old_ROOT_DATA':[{'index':18,'used_as_premise':False,'not_needed':'joint-cone/max/cap closure'},{'index':19,'used_as_premise':False,'not_needed':'stronger intrinsic actual-height bound'},{'index':20,'used_as_premise':False,'needed_claims_freshly_reconstructed_in':'n3'},{'index':21,'used_as_premise':False,'not_needed':'compact strictification'}],'excluded':['ROOT283','ROOT284','ROOT285','unbound campaigns','analytic MA replacement','literal general all-PA density'],'candidate':False}
save('premise-and-wholeproof-coverage.json',coverage)

apps=[]
def app(source,unit,ranges,use,limitations='Finite granted foundations retain their recursive dependencies; no general analytic replacement.'):
    e=primary[1 if source=='BMPS' else 3]
    apps.append({'source':source,'short_units':unit,'literal_LF_ranges':ranges,'version':e['version'],'URL':e['literal_url'],'text_path':e['path'],'text_sha256':e['sha256'],'application_and_checked_domain':use,'limitations':limitations,'whole_immediate_units_read':True,'verdict':'PASS within stated application','reasoning_note':'n1'})
app('BMPS',['D2.1-2.4'],[[254,301]],'Finite rational complexes, saturated lattice tangents and common rational refinements; no inference about abstract glued compact spaces.')
app('BMPS',['D2.18-2.31','L2.24','R2.33','L2.34','L2.35-exclusion'],[[418,638]],'Primitive raw divisor and refinement conventions; supports calibration and distinguishes integral/real slopes.','L2.35 delegates an AR10 ingredient; broad product/density conclusions from that delegation are excluded.')
app('BMPS',['D3.1-3.5','L3.4','P3.7','D3.8','R3.9'],[[691,852]],'Printed rational-endpoint PC and PA support criterion; the latter is used through authorized finite grants.','L3.4 arbitrary-center insertion as a rational vertex is not justified at irrational centers and is explicitly excluded. R230 perspective density and S272 all-face support replace that passage. Automatic continuity of arbitrary rational-endpoint functions is excluded. Strict convexity is not generalized into a classification.')
app('BMPS',['P3.22','D3.23'],[[1005,1029]],'Uniform/decreasing completed domain distinction; new affine approximation establishes its own domain antecedents.','No source assertion of all-PC density or merely local limits is imported; compactification proof dependencies are not freshly proved.')
app('BMPS',['D4.4-4.7','L4.6','P4.8','L4.9','L4.11'],[[1354,1503]],'Finite mixed signed divisor symmetry and bounded primitive-edge IBP, calibrated to the raw saturated recursion.','No appended factorial; real/signed conversion supplied in n1. Source recursion dependencies remain disclosed.')
app('BMPS',['D4.15'],[[1741,1746]],'Positive recession growth only, checked for actual finite REAL PA reference.','No automatic regularization follows from positive growth.')
app('BMPS',['D6.2','P6.3','T6.4','R6.6','C6.7-6.8','D6.9'],[[2259,2353]],'Unrestricted envelope and scope language; affine hull/contact proof is independently reconstructed rather than inferred from a broad source affine claim.','Broad PA density, literal complete-affine claim and normalization shortcuts are excluded; no general singular all-obstacle theorem is cited.')
app('BBGS',['D2.1-2.3'],[[196,250]],'Quasi-embedding domain; x -> (x,1) satisfies its hyperplane requirement with unchanged tangent metric.')
app('BBGS',['D2.14-2.15','D3.1-3.9','P3.12'],[[379,598]],'Real Euclidean weights, negative unit-normal product and whole refinement proof; calibrated via saturated lattice covolumes to raw D_f.')
app('BBGS',['P3.15','L3.18','P3.19'],[[599,714]],'Whole codimension-two commutation and preservation of balancing for REAL and signed/zero cycles in all dimensions.','P3.19 references 3.12 at commutation; actual equality is in the whole 3.15 proof. This source-reference correction is disclosed, not a new theorem.')
app('BBGS',['D5.1'],[[1515,1555]],'Real-endpoint concavity/convexity domain examined to prevent importing it into the rational-endpoint printed class.','This automatic continuity route is excluded for arbitrary printed-PC functions.')
app('BBGS',['L6.1','T6.2'],[[1913,1992]],'Whole immediate regularity proof read for domain comparison, not used as a rational-PC continuity theorem.','R230 is the authorized continuous-completion premise; downward irrational modifications show why the endpoint distinction matters.')
source={'kind':'quote-free original application metadata and own reasoning','sources':[dict(e) for e in primary],'applications':apps,'raw_conversion':'B_{-f}(a c)(tau)=a_tau D_f c(tau) with covolume a_sigma and primitive normal projection (a_sigma/a_tau) nu; holds through signed/zero recursion dimensions. Full reasoning: own n1.','recursive_foundations_not_freshly_reconstructed':['Internal proofs underlying the five whole caller grants','Positive-functional Radon representation in granted completion','Source compactification/regularization foundations outside the new argument','Delegated AR10 results (excluded from applications)'],'long_source_material':'LOCALONLY only','web_used':False,'candidate':False}
save('source-application-audit.json',source)

finite=load(OWN/'finite-output.json');build=load(OWN/'build-output.json');comparison=load(OWN/'historical-comparison.json')
assert (OWN/'finite-output.json').read_bytes()==pathlib.Path(history[13]['path']).read_bytes()
assert build['source_unchanged'] and build['source_to_markdown_exact']
assert [x['exit_code'] for x in build['commands'] if x['argv'][0]=='pdflatex' and '-no-shell-escape' in x['argv']]==[0,0]
report={'task':'Independent entire unchanged continuation282 local worker audit','overall_verdict':'INCONCLUSIVE','mathematical_reconstruction_verdict':'PASS','conditional_on_exactly_five_whole_grants':True,'source_application_verdict':'PASS within explicitly checked domains','finite_build_conversion_verdict':'PASS','historical_execution_verdict':'INCONCLUSIVE only for universal past-action/read assertions; supplied file identity, finite/build/normalization outputs verified','decisive_reason':'No remaining scoped mathematical gap identified. Historical complete own artifact files lack a full action transcript establishing every asserted past read and no-operation claim. Those assertions are not analytic premises.','ordinary_premises_and_complete_reasoning':notes,'coverage':coverage,'source_audit':source,'historical_comparison':comparison,'finite_evidence':finite,'build_evidence':build,'original_status':'OPEN','candidate':False,'automatic_acceptance':False,'proof_modified':False,'operator_configuration':{'operator_certification':'supported Xean native Codex gpt-6.1-sol xhigh, one provider call, as supplied','independently_verified_runtime_backend':False,'nested_provider_or_agents':False,'network':False,'heavy_computation':False,'supervised_compute_required':False,'supplied_programs_executed':False,'protected_editor_action':False},'retained_original_gaps':['general singular all-obstacle genuine completed domain','general singular non-PA contact sufficiency','full necessary-and-sufficient structural classification over all spaces/refinements','abstract compact/glued setting outside embedded affine sector','literal coefficient category remains separate with exact granted noncompact exclusions; no excluded endpoint receives a measure'],'reproducibility_commands':['python verify_inputs.py','python finite_check.py','python build_own.py','python assemble_audit.py']}
save('audit-report.json',report)

# Artifact manifest excludes itself, and includes all own texts/programs/logs/inputs.
manifest=[]
for p in sorted(OWN.rglob('*')):
    if p.is_file() and p.name!='own-artifact-manifest.json':
        raw=p.read_bytes();manifest.append({'file':str(p.relative_to(OWN)),'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest(),'LOCALONLY':p.relative_to(OWN).parts[0]=='LOCALONLY'})
save('own-artifact-manifest.json',manifest)
print(json.dumps({'overall':'INCONCLUSIVE','mathematics':'PASS','grant_groups':len(grants),'whole_math_bodies':len(body_coverage),'numbered_proofs':len(units),'finite_output_exact':True,'notes':len(notes),'original':'OPEN','candidate':False}))
