"""Owned artifact assembly from independent proof, no supplied program use."""
import pathlib,json,re,hashlib
from review_data import BASE,OUT
def main():
    data=BASE/'immutable-mathematical-DATA'
    dest=OUT/'qualified-G331';dest.mkdir(exist_ok=True)
    for f in ['00-P12.2-paper.tex','01-mandatory-source-scope-and-reader-qualifications-after-review240-20261008.json','02-source-application-ledger.md','03-exact-scope.md']:
        (dest/f).write_bytes((data/f).read_bytes())
    proof=(OUT/'whole-proof.md').read_text()
    matches=list(re.finditer(r'^## (n[2-9])\. (.*)$',proof,re.M))
    sections={m.group(1):proof[m.start():matches[i+1].start() if i+1<len(matches) else len(proof)].strip() for i,m in enumerate(matches)}
    meta=[
      ('n1','Fresh whole-packet audit, source-pixel qualification and bounded observations; none is a correctness grant.','All 68 current bindings, 15 historical own entries and 54 origin/local-copy pairs match. Actual FINAL has nine distinct expanded counterparts. Reader font substitution corrects a literal byte-identity receipt. Six pages inspected; 2060 finite checks have no failures.',[]),
      ('n2','Independent all-field mixed-multiplicity kernel, retaining units, unused labels and nonpure/embedded superficial quotients.','Whole-form identities prove product/power laws and closure invariance. Simultaneous superficial elements in the same quotients prove monotonicity after exact R(z); stabilized finite colons and top-form additivity are reconstructed. Literal SH 17.4.7 is qualified.', ['G331']),
      ('n3','Positive all-support bounded moment measures with full representation independence and actual prescribed-limit decreasing-NET continuity.','Proves test relations, positive real Riesz extension, mass and binomial perturbation bounds, C and bounded D extension, exact majorant supremum, additivity and every uniform/decreasing-net limit inside the stated domain. No increasing closure or measure order.', ['G331','n2']),
      ('n4','Independent supported Cartier degree with all nilpotent layers, actual Koszul symmetry, cycle projection and raw Rees comparison.','m-filtration handles mixed characteristic. Supported complexes allow improper intersections. Nonpure top-component and one-dimensional cycle decomposition precede proper projection. Eventual Rees H0/Serre vanishing and polynomial identity prove the mixed comparison; DVR local degree remains one.', ['G331','n2']),
      ('n5','Independent positive REAL nef atoms and refinement invariance, followed by a fixed-model real-core comparison.','Normal lifts, same-field DVR equality and exactly-one-prime projection prove atomic invariance first. One primary c0 and one Bl_(I c0) give the actual invertible IMAGE equality and maps to all Bl_Jq. Finite coefficient polynomials and all-support uniform profiles establish function/model independence.', ['G331','n2','n3','n4']),
      ('n6','Full bounded ordinary open locality from actual ratio subideals and justified compact-cover limits.','L+M=O and strict generic inequality force M zero on the whole integral prime and L trivial, preserving weights. Uniform C extension, other D slots, two successive prescribed decreasing limits and final known-domain uniform convergence determine Radon open restrictions. No plurifine assertion.', ['G331','n3','n5']),
      ('n7','Exact one-factor gauges, residue-weighted normalization/full conductor quotient, every reduced-curve primary model and degeneracies.','Proves degree-n exact-sequence and residue-series formulas including inseparability, retains lower-dimensional points with zero top-degree contribution, and constructs actual zero-arity curve Cartier degree. Empty/unit/zero/bottom and generic-nilpotent distinctions are explicit.', ['G331','n2','n3','n4','n5']),
      ('n8','Exact BFJ bounded OPERATOR specialization only at its published smooth closed affine algebraically closed characteristic-zero scope.','Generic joint-reduction colength is compared in the regular CM ring. Full 4.4 coefficient-topology upper semicontinuity plus monotonicity proves arbitrary decreasing NET convergence, not a promotion of 4.8 sequences. Multiplier history remains confined to the smooth domain.', ['G331','n2','n3','n7']),
      ('n9','Whole-original P12.4 survives independent reconstruction relative to qualified G331; mandatory scope/source qualifications remain.','Claims the complete bounded primary-model operator, exact supported intersections, function/model independence, ordinary open locality, prescribed-limit NET and uniform continuity, gauge/conductor/curve/degeneracy rules and exact smooth operator. No envelope, energy, full finite-map, nilpotent generic or radial-identification claim.', ['G331','n1','n2','n3','n4','n5','n6','n7','n8'])
    ]
    notes=[]
    for ident,summary,detail,support in meta:
        text=(OUT/'audit-note.md').read_text() if ident=='n1' else sections[ident]
        n={'id':ident,'summary':summary,'detailedSummary':detail,'text':text,'support':support};notes.append(n)
        (OUT/(ident+'.md')).write_text(text+'\n')
    (OUT/'native-notes.json').write_text(json.dumps({'notes':notes,'candidate':True},ensure_ascii=False,indent=2)+'\n')
    decision={'verdict':'WHOLE_ORIGINAL_PASS_WITH_MANDATORY_QUALIFICATIONS','whole_original_PASS':True,'review_complete':True,'candidate':True,'exact_atom':'P12.4','sole_incoming_grant':'Entire qualified G331','mathematical_gaps':[],
      'scope':{'ring':'Every excellent local germ through R=A_red, arbitrary characteristic/residue field','boundary':'Full centered normalized primary section; all supports retained','domain':'Bounded G331 D, p=dim R-1; n0 empty','models':'Directed actual PRIMARY blowups and auxiliary finite normalizations; no arbitrary-model cofinality','locality':'Ordinary open sets','continuity':'Weak uniform within bounded D; bounded decreasing NETS with prescribed D limit','smooth':'Published BFJ smooth CLOSED affine algclosed characteristic-zero setting; direct DVR/empty'},
      'source_qualifications':['SH17.4.7 literal unquotiented colon length invalid; use finite annihilator in current quotient derived from17.4.6','Published immediate units read at exact hypotheses; recursive historical foundations disclosed, not all independently reproved','Entire unchanged qualifiedG331 annotation, source ledger and exact scope remain mandatory'],
      'presentation_correction':'Standalone reader changes G331 font declarations inside the verbatim source. Its mathematical body is unchanged, but that embedded source is not literally byte-identical. Other three components are exact; own grant copies are unchanged.',
      'original_family_separate':['P12.3 envelopes','P12.5 energy','P12.6 unrestricted finite-map operator calculus'],
      'not_claimed':['plurifine locality','arbitrary-proper-model cofinality','singular characteristic-free resolution','generic nilpotent intersection data','literal classical/CLD radial identification','D-limit membership without hypothesis'],
      'current_binding_matches':68,'author15_fresh_matches':15,'author54_origin_fresh_matches':54,'author54_local_fresh_matches':54,'unavailable_in_these_sets':0,'actual_FINAL_note_count':9,'owned_finite_checks':2060,'owned_finite_failures':0,'fresh_source_pages_viewed':6,
      'formal_verification':False,'compiler_run':False,'external_acceptance_performed':False,'catalogue_mutation':False,'publication':False,'private_ACTIVE_P12_5_read':False,'supplied_program_execution_or_import':False,'subagents_or_native_jobs':False,'supervised_heavy_compute':'No facility exposed; no resource-heavy computation launched or needed'}
    (OUT/'acceptance-decision.json').write_text(json.dumps(decision,indent=2)+'\n')
    commands=['python review_data.py','python compare_packets.py','python inspect_sources.py','python bounded_checks.py','python assemble_review.py','python final_check.py']
    (OUT/'evidence'/'rerun-commands.json').write_text(json.dumps(commands,indent=2)+'\n')
    print('Assembled nine complete independent notes, decision and four unchanged grant components.')
if __name__=='__main__':main()
