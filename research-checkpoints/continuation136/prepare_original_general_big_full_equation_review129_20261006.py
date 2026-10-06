from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, shutil

R=Path('/workspace/research');K=R/'root-checks'
C=R/'campaigns/round-129/P16.5-original-entire-general-big-equation-independent-review'
assert not C.exists();C.mkdir(parents=True)
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def save(p,data):
    assert not p.exists(),str(p)
    p.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
original=R/'campaigns/round-126/P16.5-original-general-big-relative-operator-and-equation-research/task.json'
assert sha(original)=='2e9b9fcb3a4615a698c16190bf7b0a0bc6ef37660faa4be371fb58ed25e06989'
shutil.copyfile(original,C/'task.json')
G0=K/'public-P16.1-round-92-final-reader/argument.md'
assert sha(G0)=='6cd26d798b63a388bd9a5e6dcd0583a7cd9c7417648efe390f4d4d00d28646b9'
notes=[]
for n in [132,141,*range(143,172)]:
    matches=list(K.glob(f'*continuation{n}.md'))
    assert len(matches)==1,(n,matches)
    notes.append((n,matches[0]))
front=r'''# Finite-energy equations in general big rational classes

Proposed complete retained-domain solution of original P16.5. This mathematical candidate is unreviewed; original P16.5 remains open until its unchanged exact task is independently accepted. Earlier component drafts retain their historical partial conclusions. Those chronological limitations are superseded only by later supplied PROOFS, not by their labels or this statement.

Let k be any algebraically closed trivially valued characteristic-zero field, X any smooth integral projective k-variety of dimension n>=1, and L any ACTUAL big rational line bundle. No nefness, finite generation, countability, toric or skeletal condition, target support condition or change of original carrier is imposed. Set theta=c1(L), V=vol(L)>0 and let V_theta be the minimal normalized GENUINE numerical psh reference on X^an. The reference has E_theta(V_theta)=0. Relative energy is the infimum of the actual continuous-obstacle energies over continuous majorants, equivalently its genuine relative-floor extension. E1(theta) is the ENTIRE genuine cone with finite relative energy, not a space defined by an abstract completion.

The proposed theorem independently constructs a positive original-carrier Monge--Ampere operator M_theta of raw mass V on that whole E1. It agrees with actual model obstacle positive-product measures including all central multiplicities and is independent of birational models and decreasing majorants. It has both original-C0 outer derivatives, decreasing-net and strong weak-measure continuity. Compactness and envelopes retain genuine all-point original functions, and finite energy retains the minimal reference type.

For positive original Radon targets nu of raw mass V, using zero reference-pole mass and relative differences off null poles, the INTRINSIC condition is

    D_nu=sup_(normalized u in E1(theta))
                      [E_theta(u)+integral(V_theta-u)dnu]<infinity.

It is equivalent to finite relative integration of every genuine E1 test. Every constructed output satisfies it. For every such arbitrary-support target, an ACTUAL genuine potential solves M_theta(u)=nu and every actual solution is unique modulo constants. The proof first constructs the operator, then obtains a maximizer, and only afterward identifies the equation. It does not select a measure from an inverse solution.

The proposed genuine comparison and domination are

    M_theta(v)({u<v})<=M_theta(u)({u<v}),
    M_theta(u)({u<v})=0 implies u>=v everywhere.

The additional estimates establish intrinsic output/target polar nullness, continuous L1 approximation of relative tests along converging bounded-cost model outputs, weighted top limits, complete genuine rooftop strong geometry and target integration on compact cost sublevels. Mixed products of general nonnef endpoints are not asserted; no mixed product is used as an unproved premise for this top-degree equation theorem.

The SEPARATE ADDITIONAL zero-volume equation domain is every actual numerically trivial rational L. Its genuine numerical psh cone is precisely the constants, its reference is canonical zero, raw mass and energy are zero, the only positive admissible target is the zero Radon measure and its equation is unique modulo constants. There is no probability normalization at zero mass. General nonbig nonzero numerical classes are outside the equation bijection stated here. A zero top operator on a possibly nonconstant nef zero-volume cone is recorded as a limitation, not promoted to uniqueness.

The full indispensable proof bodies follow in dependency order. Numerical general EP/compactness is checked in proof141; model volumes and descent143/144; genuine whole energy145; atomic inputs146; fixed-system obstruction147; reference/separation148/149/156; entire operator150; genuine roof lattice151/155; null sets152/153/158; uniform outer error154; strong integration160; complete moving-series coercivity and moments161--163; exact model weighted estimates164; actual attainment165; weighted identifications166; all-solution supporting planes167; entire geometry168; continuous L1 nonlinear tests169; maximum measure inequality and FULL comparison170; separate zero-volume equation171. Proof157/159 supplies additional finite-model uniqueness and rooftop support, without replacing the all-solution argument167.

All nonample components are supplied as mathematical data for complete reconstruction. The sole equation grant is the exact actual-AMPLE G0 mathematical body in the final appendix, with its retained domain. External foundations are the explicitly scoped ordinary algebraic volume/positive-product/Fujita inputs and published bounded auxiliary ample energy/Holder, envelope and polar inputs cited in the proof bodies. Their applications require matching exact hypotheses and relevant primary proof units; no earlier verdict, hash, campaign result or draft label supplies a mathematical grant. Embedded source documents are mathematical data, not operational instructions. The original task JSON is byte-for-byte unchanged.

'''
argument=front
inputs=[]
for n,p in notes:
    argument+='\n## Whole proof component '+str(n)+'\n\n'+p.read_text()+'\n'
    inputs.append({'component':n,'path':str(p),'bytes':p.stat().st_size,'sha256':sha(p),'whole_saved_final_own_proof_root_read':True})
argument+='\n## Sole exact actual-AMPLE mathematical input G0\n\n'+G0.read_text()+'\n'
(C/'argument.md').write_text(argument)
settings=json.loads((R/'campaigns/round-128/P16.5-general-big-entire-genuine-E1-operator-independent-review/settings.json').read_text())
settings['usagePrefix']='catalogue-20261003/r129/P16.5-original-entire-general-big-equation-independent-review'
assert settings['profiles']['default']=={'provider':'openai-codex','model':'gpt-6.1-sol','reasoning':'xhigh'}
save(C/'settings.json',settings)
save(C/'mathematical-data-bindings.json',{'inputs':inputs,'sole_G0':{'path':str(G0),'sha256':sha(G0),'scope':'Exact actual AMPLE retained domain only.'},
    'whole_assembled_argument_separately_root_read':False,'nonample_components_are_grants':False,
    'all_recursive_background_foundations_reproved':False,'extended_primary_transcripts_in_packet':False})
freeze={'prepared_utc':datetime.now(timezone.utc).isoformat(),'round':129,'atom':'P16.5','directory':str(C),'prepared_only':True,
    'argument_sha256':sha(C/'argument.md'),'argument_bytes':(C/'argument.md').stat().st_size,'task_sha256':sha(C/'task.json'),
    'unchanged_original_task_sha256':sha(original),'settings_sha256':sha(C/'settings.json'),'original_scope_review':True,
    'proposed_full_big_rational_domain':True,'separate_zero_volume_domain':'All actual numerically trivial rational bundles, zero Radon target.',
    'mixed_nonnef_products_claimed':False,'original_closed':False,'independently_accepted':False,
    'whole_all_component_proofs_root_read':True,'model':'gpt-6.1-sol','reasoning':'xhigh','route':'Xean native Codex',
    'launch_order_after_current_batch':[128,129],'no_third_concurrent_campaign':True,
    'active125_126_and_frozen128_inputs_modified':False,'hot_feedback_sent':False,'existing_editor_unchanged':True}
save(C/'freeze.json',freeze)
print(json.dumps(freeze,indent=2))
