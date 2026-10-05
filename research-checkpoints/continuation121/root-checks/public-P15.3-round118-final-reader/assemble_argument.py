"""Assemble this fresh proof and the supplied, scoped historical mathematics."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent

APPLICATIONS = [
 {'id':'S1','source':'drwnxz','LF':[[226,263],[314,385],[561,691]],
  'statement':'Smooth complete flags; rational recursive analytic-current valuations; big-class body closure and pseudoeffective intersection.',
  'application':'New torus theorem Section 6 and retained divisorial/product construction.',
  'hypotheses_checked':'X smooth connected compact Kähler surface; fixed globally smooth complete flag; positive perturbation representative beta_X+rho is Kähler. Generators gentle analytic Kähler; rational divisorial coefficient. No recursive restriction of arbitrary nonanalytic potential is asserted.',
  'proof_status':'Published lemma/definition/proofs retained. Uniform collapse is proved here, not supplied by these statements.'},
 {'id':'S2','source':'drwnxz','LF':[[255,263]],
  'statement':'Potential pullback/descent proof uses bounded-above psh removability and equality of canonical representatives off an analytic set.',
  'application':'New Section 4; retained product modification.',
  'hypotheses_checked':'Proper bimeromorphic morphism, smooth compact Kähler source and target; global upper bound. The source standing assumption is big, but this draft reconstructs its proof without bigness.',
  'proof_status':'Nonbig extension proved in the draft; exact classical removability statement is explicitly retained from the published proof.'},
 {'id':'S3','source':'drwnxz','LF':[[338,361],[852,894]],
  'statement':'Partial bodies for gentle analytic Kähler references; divisorial translate identity and analytic realization.',
  'application':'Smooth-reference partial bodies in Section 6; rational divisorial appendix.',
  'hypotheses_checked':'Smooth reference at positive torus levels; every potential bounded above, so zero-type comparison automatic. Appendix D rational, residual smooth semipositive; epsilon makes residual Kähler. No general P-type replacement is used.',
  'proof_status':'Partial identity is reproved in the appendix; no application to arbitrary dense-pole references.'},
 {'id':'S4','source':'drwnxz','LF':[[494,502],[939,963],[1139,1415]],
  'statement':'Volume zero for nonbig classes; class ambient volume formula and its induction proof.',
  'application':'New Section 7 perturbative area; retained big surface mass/area calculation.',
  'hypotheses_checked':'Formula applied only to Kähler/big surface positive levels or the Kähler residual surface in appendix. Nonbig volume is separately proved via a positive test pairing. No lower numerical dimension conclusion from zero ambient volume.',
  'proof_status':'Published theorem used as background. Kähler self-intersection calculation separately proved here.'},
 {'id':'S5','source':'xia','LF':[[67,105],[371,429],[476,494],[1158,1185],[1623,1637],[1824,1840]],
  'statement':'Projective line-bundle multiplier-ideal bodies; ordinary, C, and I distinctions; section volume from I-envelope mass; zero-volume dimension conjecture; eta-dependent Chebyshev question.',
  'application':'Source limitations only; no numerical result applied to nonprojective torus.',
  'hypotheses_checked':'Positive ideal-model/section volume, positive actual input mass, and big class are distinct. Ordinary P-envelope is used as defined. Chebyshev auxiliary datum is a more-singular Kähler-current potential eta.',
  'proof_status':'Definitions and literal statements/proof references retained; Conjecture 5.29 remains conjectural.'},
 {'id':'S6','source':'cao','LF':[[162,279],[281,289],[660,721]],
  'statement':'Global potential representation and quasi-equisingular current products; numerical dimension for line-bundle metrics; projective general-hypersurface reduction.',
  'application':'Uniqueness of positive current from rigidity; constant approximations compute products in Sections 5 and appendix.',
  'hypotheses_checked':'Currents on compact Kähler manifolds; constant analytic approximations verify all three conditions directly. Definition 3 applies to transcendental smooth currents. Definition 4 is not asserted for a nonexistent line bundle. General ample hypersurface argument not applied.',
  'proof_status':'Published potential/product background explicitly retained; equality with actual products established only for the stated smooth/divisorial examples.'},
 {'id':'S7','source':'chpw','LF':[[166,185],[530,577],[915,1096]],
  'statement':'Numerical dimension and lower intrinsic volume for projective real divisors with a positive-volume-subvariety flag; other flags may have smaller dimension.',
  'application':'Source limitation, not a theorem used to prove new collapse or old transcendental dimension.',
  'hypotheses_checked':'Smooth projective variety, real divisor, flag containing positive volume subvariety. They are absent for the torus. All relevant proof bodies are extracted.',
  'proof_status':'Published result retained without any claimed transcendental extension.'},
]

def main():
 frozen=json.loads((ROOT/'input-original.json').read_bytes())
 assignment=frozen['assignment']
 old=assignment.split('## Entire preceding own scoped proof\n',1)[1].split('## Actual correctness review of that scoped proof',1)[0]
 old=old.split('## 6. Reproducible evidence',1)[0].rstrip()
 first='whether the Chebyshev transform is independent of its auxiliary positive form'
 clarification="Xia's section 6.4 (lines 1824–1840) leaves independence of the Chebyshev transform from its auxiliary more-singular Kähler-current potential eta open; the auxiliary datum is not an arbitrary positive form."
 second='The sandwich therefore proves convergence to (2.1) along these paths.'
 assert old.count(first)==0  # That shorthand occurs in the task, not this supplied proof body.
 assert old.count(second)==1
 marker="Xia's source domain is projective and line-bundle based. It is not invoked for the transcendental example below."
 assert old.count(marker)==1
 old=old.replace(marker,marker+'\n\n'+clarification)
 old=old.replace(second,'The sandwich therefore proves convergence to the residual class body along these paths; translating by nu_Y([D]) gives (2.1).')
 (ROOT/'retained-scoped-proof.md').write_text(old+'\n',encoding='utf-8')
 ledger={'coordinate_convention':"one-based inclusive text.split('\\n') entries",'applications':APPLICATIONS,
  'additional_explicit_classical_background':[
   {'statement':'Bedford–Taylor products of bounded potentials are closed, positive, local, and have no pluripolar mass; nonpluripolar products on a small-unbounded-locus domain are their trivial extension.','use':'Supplied divisorial/product/dense-pole appendix only; actual smooth products in the new theorem need only the smooth case.','status':'Classical background retained from the exact inline reviewed proof and its stated premise; no inaccessible book proof or BEGZ cache read.'},
  ],
  'reconstructed_background':['torus integral cohomology/type calculation','Baire existence and properness of each excluded type locus','dense null leaves by Fourier averaging','bounded-above subharmonic Liouville argument','positive-current weak compactness needed for collapse','nonbig descent using the published removability input','contraction of model curves by pushing forward integral integration currents','cohomological degree bound for positive curve currents','Kähler self-intersection computation from gentle resolution','conditional Hausdorff area continuity'],
  'historical_scope':'Complete supplied Sections 1–5 preserved as mathematical appendix, exactly two wording corrections. Historical evidence section not reused as fresh execution evidence. PASS in frozen assignment concerns only that restricted result; no new audit inferred.',
  'wording_corrections':[
   {'before':'Chebyshev shorthand absent from supplied proof body; clarification added after Xia section 5.6 paragraph','after':clarification},
   {'before':second,'after':'The sandwich therefore proves convergence to the residual class body along these paths; translating by nu_Y([D]) gives (2.1).'},
  ]}
 (ROOT/'source-application-ledger.json').write_text(json.dumps(ledger,ensure_ascii=False,indent=2)+'\n')
 prefix=(ROOT/'argument-new.md').read_text()
 appendix='\n# Appendix: complete retained restricted proof\n\nThe following is the supplied mathematical proof, with exactly the two harmless wording corrections recorded in the ledger. Its old documentary section is superseded by Section 9 above. The supplied source-aware PASS is retained in the frozen input as a review of this restricted scope only; it supplies no certification of the new torus theorem or of original closure.\n\n'
 # Demote historical headings, preserving every other mathematical byte after the two corrections.
 displayed='\n'.join('#'+line if line.startswith('#') else line for line in old.split('\n'))
 table='\n\n# Source/application ledger\n\nThe machine-readable ledger is `source-application-ledger.json`. The full literal extracts and their inclusive LF coordinates are `source-extracts/source-provenance.json`.\n\n'
 for app in APPLICATIONS:
  coords='; '.join(f'{a}–{b}' for a,b in app['LF'])
  table+=f"**{app['id']} — {app['source']}, LF {coords}.** {app['statement']}\n\nApplication: {app['application']} Hypotheses: {app['hypotheses_checked']} Status: {app['proof_status']}\n\n"
 table+='Contraction of model curves is proved by pushing forward their integral integration currents. The bounded-potential/nonpluripolar background in the supplied appendix is retained only in its stated scope; no fifth cache or book theorem was read. The torus existence, leaf density, rigidity, nonbig descent, weak compactness argument, valuation uniformity and reference-sensitive area assertions are proved in the main argument.\n'
 (ROOT/'P15.3-argument.md').write_text(prefix+appendix+displayed+'\n'+table)
 status={'id':'P15.3','status':'partial','exact_result':'Dense-null-leaf curve-free transcendental rank-one torus: smooth ordinary P-type zero, numerical/actual/Cao current degree one, but every usual unrescaled analytic-current body on every fixed smooth Kähler model and smooth complete flag tends to a point. Positive smooth perturbation paths have the same limit; perturbative area has explicitly reference-sensitive leading coefficient. Retains the supplied divisorial/product theorem and dense-pole recipe obstruction.','proof_file':'P15.3-argument.md','concrete_gaps':['No general geometric/valuation construction for arbitrary prescribed ordinary P-envelope types.','No general numerical dimension or actual/Cao product theorem for a new lower-dimensional carrier.','No general carrier/scale/flag/modification independence result for any construction evading the explicit usual-valuation and unrescaled-limit axioms.','No impossibility theorem for all richer geometric constructions satisfying the unchanged original task.']}
 (ROOT/'status.json').write_text(json.dumps(status,ensure_ascii=False,indent=2)+'\n')
 print(json.dumps({'argument_bytes':(ROOT/'P15.3-argument.md').stat().st_size,'retained_proof_bytes':(ROOT/'retained-scoped-proof.md').stat().st_size,'applications':len(APPLICATIONS),'status':status['status']},indent=2))

if __name__=='__main__':main()
