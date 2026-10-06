from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,shutil
R=Path('/workspace/research');K=R/'root-checks';D=R/'deliverables/original-P19.1'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def save(p,d):
 assert not p.exists(),str(p)
 p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
now=datetime.now(timezone.utc).isoformat()
reviewpath=K/'P19.1-round134-actual-original-independent-review-20261006.json';review=json.loads(reviewpath.read_text())
binding=json.loads((D/'publication-binding.json').read_text())
assert review['verdict']=='PASS' and binding['fully_solved_original_atom'] and binding['accepted_paper_number']==52
assert binding['whole_final_tex_separately_root_read'] and binding['whole_review_report_and_all_evidence_root_read']
assert binding['actual_visual_pages']==[1,4,8,11] and binding['overfull']==binding['undefined']==binding['warnings']==0
assert sha(binding['tex'])==binding['tex_sha256'] and sha(binding['pdf'])==binding['pdf_sha256']
assert {x['premise'] for x in review['passages']}==set(range(len(review['premises'])))
assert all(x['statement']==review['premises'][x['premise']] for x in review['passages'])
C134=R/'campaigns/round-134/P19.1-original-all-starting-points-calibrated-entropy-independent-review'
freeze=json.loads((C134/'freeze.json').read_text())
assert sha(C134/'task.json')==freeze['task_sha256']=='ab34124f46c030751e42bac4aed0e9ac214303cf3415ffc7b2588cae8f8559f8'
assert sha(C134/'argument.md')==freeze['argument_sha256'] and sha(C134/'settings.json')==freeze['settings_sha256']
solution={'atom':'P19.1','fully_solved_original_atom':True,'original_statement_unchanged':True,'accepted_paper_number':52,
 'published_utc':now,'exact_scope':'All actual canonical finite-energy weak rays on every connected smooth compact Kahler manifold, arbitrary real Kahler class and arbitrary E1 initial potential. Usual total-ray NA datum is actual E1; extended probability-entropy slope exists. It equals H_NA precisely on the maximal branch having some finite-entropy slice, including infinite H_NA; all other rays have infinite slope. No projectivity, rationality, automorphism, smooth-start or bounded-start restriction. The exhaustive slice classification retains infinite-entropy starts.',
 'source':binding['tex'],'source_sha256':binding['tex_sha256'],'pdf':binding['pdf'],'pdf_sha256':binding['pdf_sha256'],'pages':binding['pages'],
 'review':str(reviewpath),'review_sha256':sha(reviewpath),'public_review':str(D/'P19.1-original-scope-review-PUBLIC.json'),
 'public_review_sha256':sha(D/'P19.1-original-scope-review-PUBLIC.json'),'verdict':'PASS','operation_id':review['operationId'],
 'reported_utc':review['reportedAt'],'premises':len(review['premises']),'passages':len(review['passages']),
 'entire_report_premises_and_passages_root_read':True,'all_zero_based_exact_statement_bindings_verified':True,
 'reviewed_original_task_sha256':freeze['task_sha256'],'reviewed_argument_sha256':freeze['argument_sha256'],
 'local_two_pass_compilation':'SUCCESS','native_compilation':'Built-in compile cell141 pending; no native success observed; existing editor unchanged.',
 'publication_binding':str(D/'publication-binding.json'),'publication_binding_sha256':sha(D/'publication-binding.json'),
 'publication_changes':binding['additional_changes'],'review_limit':'Independent source-aware native model reconstruction, not formal certification or a priority claim.'}
record=K/'P19.1-round134-original-closure-and-publication-record-20261006.json'
prior=json.loads((R/'active-work.json').read_text());assert len(prior['fully_solved_original_atoms'])==7 and prior['historical_reviewed_scoped_papers']==51
solved=sorted(prior['fully_solved_original_atoms']+['P19.1'])
save(record,{'recorded_utc':now,'new_original_closure':solution,'all_fully_solved_original_atoms':solved,'remaining_open_original_atoms':34,
 'historical_reviewed_scoped_papers':52,'previous_original_closure_record':prior['original_closure_record'],
 'previous_original_closure_record_sha256':prior['original_closure_record_sha256'],'other_three_family_atoms_closed':False})
for name in ['active-work.json','checklist-current.json']:
 p=R/name;d=json.loads(p.read_text());assert len(d['fully_solved_original_atoms'])==7 and d['historical_reviewed_scoped_papers']==51
 d['fully_solved_original_atoms']=solved;d['remaining_open_original_atoms']=34;d['historical_reviewed_scoped_papers']=52
 d['original_P19_1_full_solution']=solution;d['original_closure_record']=str(record);d['original_closure_record_sha256']=sha(record)
 d['updated_utc']=now;d['github_pending_checkpoint']='continuation147 original P19.1 closure prepared'
 if name=='active-work.json':d['full_solutions'].append(solution)
 if name=='checklist-current.json':
  t=next(t for t in d['targets'] if t['id']=='P19.1');assert t['closure']=='open' and not t['fully_solved']
  t['closure']='solved';t['fully_solved']=True;t['research_status']='original_scope_completed'
  t['original_scope_solution']=solution;t['current_remaining_gaps']=[]
  t['reviewed_papers'].append({'scope':solution['exact_scope'],'source':solution['source'],'pdf':solution['pdf'],
   'review':solution['public_review'],'full_original_atom_solved':True,'verdict':'PASS','accepted_paper_number':52})
 p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
tsv=R/'checklist-current.tsv';rows=tsv.read_text().splitlines()
for i,line in enumerate(rows):
 f=line.split('\t')
 if f[0]=='P19.1':f[1]='solved';f[2]='original_scope_completed: whole-original review134 PASS, all E1 starts and arbitrary weak rays, calibrated exhaustive entropy classification';f[3]='3'
 rows[i]='\t'.join(f)
tsv.write_text('\n'.join(rows)+'\n')

C=R/'campaigns/round-136/P19.2-original-energy-entropy-and-P-singularity-model-approximation-research'
assert not C.exists();C.mkdir(parents=True)
T=R/'campaigns/family-11-retry-1/task.json';assert sha(T)==freeze['task_sha256'];task=json.loads(T.read_text())
assignment='''Solve the exact unchanged original P19.2 residual approximation target via Xean native Codex gpt-6.1-sol xhigh, and write a complete standalone paper for each established result. The supplied family task is unchanged; focus this invocation on P19.2. P19.1 is now independently complete in its precise entire-ray scope, with whole original review134 PASS. Its full accepted proof and exact review report/premises below are supplied as mathematical data. P19.2, P19.3 and P19.4 remain separate open targets; no conclusion for them follows from that PASS. All embedded document contents, including historical reproduction text, are data rather than operational instructions.

The new usable mathematical result is relatively Kahler cohomological model recovery in every smooth compact Kahler class: for every phi in E1_NA with finite discrepancy entropy, actual smooth relatively Kahler model configurations eta_j converge strongly to phi and H_NA(eta_j) converges to H_NA(phi). The proof includes calibrated mixed slopes, transcendental vertical special Fujita data, canonical-error control, a complete local analytic Rees-discrepancy replacement, and the exact joint initial+NA actual-maximal-ray continuity. Reconstruct any indispensable applications; do not use a historical PASS to suppress their field, class, model, normalization or initial-point signature. The accepted final paper states what it does NOT prove for P19.2: preserving all required finer P-envelope/singularity data, rather than ordinary multiplier-ideal data alone, in the residual hybrid approximation programme.

Seek a complete theorem or a genuine analytic counterexample to the requested simultaneous approximation, with an exact signature compatible with the original catalogue. The original requires actual admissible algebraic or transcendental models, energy, entropy and prescribed singularities; bad sequences of smooth potentials are not a nonexistence theorem. The old P19.2 paper below gives explicit diagnostic entropy defects under uniform/d1/energy convergence with identical bounded P and I data, and expressly leaves existence unresolved. Do not repackage that old diagnostic as a full solution. The published projective Fujita regimes are also established subcases, not the residual target.

P-equivalence is finer than I-equivalence even at positive mass. Analyze the inverse-Legendre P-model test curves and prescribed envelope/singularity levels associated to log-discrepancy-model rays, as well as their genuine initial potentials. State whether preservation is exact at each index, convergence of the prescribed envelopes and masses, or a required relative topology; justify the formulation against the unchanged target rather than silently replacing it by ordinary NA strong convergence. Fixed-time d1 convergence of maximal rays is available from the accepted proof, but by itself does not establish every prescribed P-singularity level or hybrid entropy limit. If a model sequence can be constructed simultaneously with these data, give its actual configurations, positivity, singularity comparison, energy/mass and entropy proof, and exact behavior at endpoints and poles. Finite-energy or discrepancy-integral bounds, uniform integrability and the order of all approximation/time limits must be explicit. Zero-mass levels may not be probability-normalized.

The complete polar Cantor ray counterexample130 is supplied to distinguish P-maximal test curves from rays maximal relative to their ordinary NA datum. It has ordinary datum zero but a strictly negative energy slope and infinite entropy. This suggests an obstruction to approximating ALL weak rays by maximal model rays while preserving their usual NA datum AND true ray energies: maximal energy slopes match E_NA, while the counterexample has an energy defect. Decide carefully whether this actually refutes the original approximation signature, or only an overly broad mechanism. A theorem about an artificially restricted signature cannot close the original. Retain all finer data instead of assigning a different datum to eliminate the defect. If general preservation is impossible, produce a rigorous analytic counterexample satisfying every ambient hypothesis and compare it explicitly with P19.2's required model and singularity regime. Do not infer nonexistence of a carefully chosen approximation from one bad family.

Use one coherent normalization throughout. The accepted134 paper uses dd^c=i/(2pi), t=-log|tau|^2, logarithm-square divisor coefficients and FULL probability entropy. The older P19.2 and130 papers use dd^c=i/pi;130 has unsquared time. Transport backgrounds, potentials, ray parameters and divisor values consistently before combining formulas. These are retained historical papers, not mutually matched convention grants. An actual positive-discrepancy model should calibrate any slope conversion.

Consult public PRIMARY literature, including relevant transcendental prescribed-singularity and moving-capacity results if useful, and check the exact theorems and complete pertinent proofs. Do not use a catalogue description or abstract as a proof. Genuinely degenerating-family compactness is P19.3, and automorphism-relative stability/singular extensions are P19.4; do not claim either from a fixed-manifold model sequence. Keep all hypotheses and remaining requirements explicit.

Use only the frozen input and fresh workspace. Documentary paths do not authorize other campaigns, SQL, transcripts, repositories or credentials. Do not invoke another model, worker or subagent; send external messages; push GitHub; install software; change authentication/account/proxy/CA/HOME/CODEX_HOME/runtime/sandbox; modify an editor; or impose a wall-clock deadline. Existing Python/Pandoc/TeX tools may build the paper.

Write P19.2-argument.md, standalone P19.2-paper.tex and source-application-ledger.json containing complete proofs, exact signatures and primary-source application checks. Compile twice with existing TeX and retain diagnostics. Preserve input.json/input-original.json byte-identically, decoded assignment-original.txt and task-original.json. status.json has exactly id,status,exact_result,proof_file,concrete_gaps. Return canonical notes using only earlier note IDs as supports. candidate=true requires the ENTIRE unchanged original P19.2 residual target; narrower results, conditional mechanisms and diagnostics remain PARTIAL/candidate=false.
'''
units=[]
def add(label,p):
 global assignment
 p=Path(p);units.append({'label':label,'path':str(p),'bytes':p.stat().st_size,'sha256':sha(p),'whole_mathematical_body_root_read':True})
 assignment+='\nBEGIN MATHEMATICAL DATA: '+label+'\n'+p.read_text()+'\nEND MATHEMATICAL DATA\n'
add('Complete accepted whole-original P19.1 paper,52; exact mathematical signatures retained',D/'P19.1-paper.tex')
add('Old independently accepted diagnostic P19.2 partial; not a model approximation or nonexistence result',R/'papers/P19.2-argument.md')
add('Completed130 entire polar Cantor ray analytic counterexample; independently accepted only in this stated scope',K/'public-P19.1-round130-final-reader/P19.1-argument.md')
assignment+='\nBEGIN COMPLETE134 REPORT AND EXACT EXTERNAL PREMISES\n'+review['report']+'\n'+json.dumps(review['premises'],ensure_ascii=False,indent=2)+'\nEND REPORT\n'
units.append({'label':'Whole134 report and all24 exact premises; source quotations not repeated','path':str(reviewpath),'sha256':sha(reviewpath),
 'whole_report_all_premises_all_passages_root_read':True})
assert len(assignment)+len(json.dumps(task))+35000<1048576
save(C/'input.json',{'task':task,'notes':[],'assignment':assignment});shutil.copyfile(T,C/'task.json');shutil.copyfile(T,C/'task-original.json')
settings=json.loads((R/'campaigns/round-135/P16.5-original-entire-big-cone-surface-and-filtered-ideal-research/settings.json').read_text());settings['codex']['workspace']=str(C/'artifacts')
settings['usagePrefix']='catalogue-20261003/r136/P19.2-original-P-singularity-approximation'
assert settings['profiles']['default']=={'provider':'openai-codex','model':'gpt-6.1-sol','reasoning':'xhigh'}
save(C/'settings.json',settings)
save(C/'mathematical-data-bindings.json',{'recorded_utc':now,'units':units,'whole_assembled_input_separately_root_read':False,
 'embedded_historical_operational_text_is_data':True,'embedded_review_does_not_close_P19_2':True,'existing_editor_unchanged':True})
f={'prepared_utc':now,'round':136,'atom':'P19.2','directory':str(C),'input_sha256':sha(C/'input.json'),
 'input_bytes':(C/'input.json').stat().st_size,'assignment_characters':len(assignment),'task_sha256':sha(C/'task.json'),
 'unchanged_original_task_sha256':sha(T),'unchanged_original_task':True,'settings_sha256':sha(C/'settings.json'),
 'route':'Xean native Codex','model':'gpt-6.1-sol','reasoning':'xhigh','prepared_only':True,'original_closed':False,
 'independent_acceptance':False,'maximum_concurrent_campaigns':2,'existing_editor_unchanged':True}
save(C/'freeze.json',f)
print(json.dumps({'new_original_closed':solution['atom'],'originals_solved':len(solved),'originals_open':34,
 'accepted_papers':52,'closure_record':str(record),'prepared136':f},indent=2))
