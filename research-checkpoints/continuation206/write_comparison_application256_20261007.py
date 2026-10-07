from pathlib import Path
from datetime import datetime, timezone
import hashlib, json

K = Path('/workspace/research/root-checks')
D = K / 'continuation253-formal-comparison-primary-LOCALONLY'
out = K / 'P16.4-continuation256-rigid-Berkovich-H0-primary-application-working-proof-20261007.json'
assert not out.exists()
def binding(p):
    b=p.read_bytes()
    return {'path':str(p),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()}
record = {
 'recorded_utc':datetime.now(timezone.utc).isoformat(),
 'status':'Unreviewed source application; no additional grant, accepted paper, or original closure',
 'original':'P16.4',
 'source':{'literal_url':'https://www.numdam.org/item/PMIHES_1993__78__5_0.pdf',
           'pdf':binding(D/'Berkovich1993-publisher.pdf'),
           'text':binding(D/'Berkovich1993-publisher.txt')},
 'actual_ROOT_reading':{
   'text_LF_ranges':[[895,1010],[1320,1465]],
   'scope':'Whole Proposition1.3.4, Corollary1.3.5, Proposition1.3.6 and proofs; whole section1.6 including Theorem1.6.1, Lemma1.6.2 and proofs and final coherent cohomology comparison paragraph.',
   'images_visually_read':[{'image':binding(D/'Berkovich1993-primary-page24.png'),'PDF_page_one_based':24,'printed_page':27}, {'image':binding(D/'Berkovich1993-primary-page34.png'),'PDF_page_one_based':34,'printed_page':37}],
   'all_recursive_source_proofs_read':False,
   'higher_cohomology_foundations_not_newly_read':'Tate acyclicity; the recursively used affinoid gluing and refinement foundations; no claim that their entire proofs were reconstructed here.'},
 'application_proof':[
  {'step':'A1','proof':'Restrict this comparison to a complete NONTRIVIALLY valued field K and the actual analytification Y of the original projective variety. For an actual closed projective embedding, intersect Y with the finitely many standard domains where the chosen homogeneous coordinate has maximal absolute value. The corresponding strict affinoid algebras are K<T_1,...,T_m> modulo the dehomogenized ideal. Their analytic domains cover Y; the usual projective analytification is good and Hausdorff. Compactness gives paracompactness. These properties, including the neighborhood property defining goodness, belong to the actual projective analytification, rather than a claim that every finite affinoid cover by itself proves goodness.'},
  {'step':'A2','proof':'Berkovich section1.6 assigns a quasiseparated rigid space Y_0 to a Hausdorff strict analytic space Y by using the same strict affinoid domains and coordinate rings. Lemma1.6.2 identifies rigid admissible covers with analytic quasinets and rigid affinoid opens with strict analytic domains. Theorem1.6.1 makes this correspondence fully faithful; its paracompact part applies to this projective Y. Its final paragraph identifies the G-topos with the rigid topos and the coherent sheaf categories.'},
  {'step':'A3','proof':'Let A be the ORIGINAL algebraic line bundle or its actual tensor power. Its transition functions on the original algebraic trivializing opens pull back to the same analytic functions on all common affinoid refinements. Hence its Berkovich G-coherent sheaf A_G corresponds to the rigid analytification A_0 of that SAME bundle. The identification is natural on restrictions and on original algebraic sections; neither the bundle nor the original field is replaced.'},
  {'step':'A4','proof':'For degree zero, Proposition1.3.4(i) gives A = pi_* A_G on the usual topology of the good Y. Taking global sections yields Gamma(Y,A)=Gamma(Y_G,A_G). The isomorphism of topoi in the final paragraph of section1.6 then gives Gamma(Y_G,A_G)=Gamma(Y_0,A_0). Concretely, sections are compatible tuples of affinoid module elements on a common affinoid cover; the rings, modules, transition functions and overlap equalities are the same. Thus this H0 comparison does not need an additional higher-cohomology vanishing argument. Proposition1.3.6(ii) and the final paragraph also state the all-degree coherent comparison, but only q=0 is used here.'},
  {'step':'A5','proof':'The comparison preserves every original algebraic section under the two analytification maps. The corresponding Berkovich section is therefore the same analytic function in every original trivialization at EVERY analytic point, including nonclassical points. If a separately proved formal/rigid GAGA step algebraizes a rigid section of the actual model bundle, this comparison transports that section to the actual Berkovich section; it does not itself prove the formal GAGA step or equality with any separately constructed germ.'},
  {'step':'A6','proof':'This supplies the immediate original primary text for independent198 premise15 in its complete nontrivially valued, Hausdorff strict, good projective domain. It does not discharge premise14 concerning Raynaud-Gruson flat loci, all recursive Fujiwara-Kato coherent/formal foundations, algebraic/rigid GAGA, existence of the required actual model, positive-genus kernel realization, general prescribed-target attainment, or all-point uniqueness. Trivially valued fields use the already granted T171 theorem; section1.6 is not extended to that domain.'}
 ],
 'material_coercivity_scope':'Finite reference moment alone is insufficient. Any repaired coercivity conclusion must explicitly assume/prove finite U_mu (equivalently the appropriate intrinsic target condition), as in the full independent198 failure and working252 route.',
 'whole_sources_or_images_published':False,
 'no_hot_feedback_to_active_campaigns':True,
 'counts_unchanged':{'original_solved':9,'original_open':33,'accepted_scoped_papers':76}
}
out.write_text(json.dumps(record,indent=2,ensure_ascii=False)+'\n')
print(json.dumps({'output':binding(out),'status':record['status']},indent=2))
