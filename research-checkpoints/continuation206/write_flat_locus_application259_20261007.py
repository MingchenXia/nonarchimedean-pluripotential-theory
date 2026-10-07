from pathlib import Path
from datetime import datetime, timezone
import hashlib,json

K=Path('/workspace/research/root-checks');D=K/'continuation258-flat-locus-primary-LOCALONLY'
out=K/'P16.4-continuation259-Raynaud-Gruson-flat-locus-primary-application-working-proof-20261007.json'
assert not out.exists()
def bind(p):
 b=p.read_bytes();return {'path':str(p),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()}
record={
 'recorded_utc':datetime.now(timezone.utc).isoformat(),
 'status':'Unreviewed immediate-primary application; no mathematical acceptance or new grant',
 'original':'P16.4',
 'source':{'literal_url':'https://gdz.sub.uni-goettingen.de/download/pdf/PPN356556735_0013/PPN356556735_0013.pdf','original_article':'M. Raynaud and L. Gruson, Criteres de platitude et de projectivite, Inventiones Mathematicae13 (1971),1-89','whole_journal_pdf':bind(D/'Inventiones1971-volume13-original.pdf'),'retrieval_metadata':bind(D/'retrieval-binding.json'),'ordinary_pdftotext_has_no_article_text':True},
 'actual_ROOT_reading':{
   'printed_pages_visually_read':[23,24,25,26],
   'PDF_pages_one_based':[30,31,32,33],
   'visual_images':[bind(D/f'RG1971-primary-PDFpage{p}.png') for p in [30,31,32,33]],
   'whole_immediate_units':'Entire section3.4, including3.4.0, Theorem3.4.1 and proof, Cor3.4.2, Prop3.4.3 and proof, Lemmas3.4.4/5 and proofs, Theorem3.4.6 and proof, Cor3.4.7 and all remarks.',
   'OCR_used_only_as_a_navigation_and_reading_aid':True,
   'OCR_primary_mathematics_verified_in_actual_images':True,
   'entire_recursive_foundations_read':False,
   'remaining_recursive_dependencies':'Section2.6 finite-presentation flat approximation; section1.2.3 devissage; section3.1-3.3 purity/projectivity and EGA weak-assassin lemmas are cited by the immediate proof and not all newly reconstructed here.',
   'FK_actual_application_text':{'path':str(K/'continuation236-formal-algebraization-primary-LOCALONLY/Fujiwara-Kato2017-v5.txt'),'LF_range':[11385,11495],'scope':'Whole0.9.2.1 statement/0.9.2.2-4 and full two-step proof0.9.2.1, including original RG use on V/aV.'}},
 'working_application_proof':[
  {'step':'A1','proof':'The original RG3.4.6 concerns a locally finitely presented scheme morphism f:X->S and a finite-type O_X-module M. It additionally requires the WEAK associated-point set Ass(S) to be locally finite. It concludes the S-flat locus U is OPEN and M|U is finitely presented. Finite type alone or generic flatness alone does not remove the Ass(S) condition. Its full printed proof first builds a finitely presented S-flat approximation N->M inducing an isomorphism at the chosen flat point using3.4.2/2.6, then restricts to a neighborhood where the finite weak-assassin set of N consists of generalizations of that point. The map is surjective there; its kernel has no weak associated points and is zero. Earlier3.4.3 supplies the finite-assassin transfer. These are ordinary source dependencies, not new grants.'},
  {'step':'A2','proof':'For the actual complete rank-one valued field C and V=C-circle, the scheme Spec(V) is integral; its weak associated-point set is just the generic point, since the annihilator of every nonzero element is zero. This checks the locally finite condition if RG is applied over V itself. However this alone is NOT the actual FK0.9.2.1 application: FK first applies it over the quotient V/aV.'},
  {'step':'A3','proof':'For 0<|a|<1, Spec(V/aV) has ONE point. Every element b of the maximal ideal of V has a positive power whose norm is at most |a|, so b belongs to the radical of aV; units do not. Thus radical(aV)=m_V and the only prime of V/aV is m_V/aV. The weak-assassin set is this one point (the annihilator of1 is0 and its radical is that maximal ideal). It is finite despite the possible non-Noetherian quotient and unbounded nilpotence of its nilradical. No uniform nilpotence exponent is asserted.'},
  {'step':'A4','proof':'Let A=V<T_1,...,T_m> and let M be an a-torsion-free finite A-module as in FK0.9.2.1. Rank one implies V-flatness: any nonzero b in V dominates some a^N in divisibility, so b-torsion would imply a-torsion. A torsion-free module over a valuation ring is flat. Hence M/aM is flat over V/aV. Restricted series reduce to polynomials modulo a, so A/aA=(V/aV)[T_1,...,T_m] is finitely presented over V/aV, and M/aM is a finite module over it. RG3.4.6 now applies at EVERYpoint of Spec(A/aA); its conclusion makes M/aM finitely presented over A/aA. The flatness premise is flatness over V/aV, not a claim that an arbitrary such M/aM is flat over A/aA.'},
  {'step':'A5','proof':'This verifies the ACTUAL immediate Raynaud-Gruson use in the rank-one part of FK0.9.2.1. FK proceeds through its earlier saturated-kernel and complete-module lemmas to finite presentation of M; those remain separate foundations. In higher-height valuation rings FK has an additional localization step, but the original retained complete real-valued field gives rank one here. The original Cor3.4.7 also states finite-type flat algebras over integral domains are finitely presented; it is not a replacement theorem about every finite module over a non-Noetherian ring.'},
  {'step':'A6','proof':'The source and exact-domain check provide the immediate original theorem/proof evidence missing for independent198 premise14. Combined with working256 they address those TWO immediate-source gaps as unreviewed source applications. They do not turn whole250 into a grant, repair its material missing finite-U target hypothesis, establish the entire recursive formal GAGA proof, build every required polarized actual curve model, prove general prescribed-target attainment, or prove every-solution all-point uniqueness. A future independent review must check the completed actual route in full.'}
 ],
 'full_third_party_primary_or_images_published':False,
 'no_hot_feedback_to_active200201':True,
 'counts_unchanged':{'original_solved':9,'original_open':33,'accepted_scoped_papers':76}
}
out.write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n');print(json.dumps(bind(out),indent=2))
