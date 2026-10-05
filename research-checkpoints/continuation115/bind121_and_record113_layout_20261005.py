from pathlib import Path
from datetime import datetime, timezone
import hashlib, json

R=Path('/workspace/research');K=R/'root-checks'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def save(p,v):
    assert not p.exists(),str(p)
    p.write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')
note=K/'P16-prescribed-divisorial-references-as-intrinsic-original-model-envelopes-20261005-continuation121.md'
sources=[K/'public-P16.5-round112-final-reader/P16.5-paper.md',
         K/'public-P16.2-round113-final-reader/P16.2-paper.md',
         K/'P16.5-effective-divisorial-zero-volume-prescribed-type-equations-20261005-continuation118.md',
         K/'P16.2-entire-divisor-cone-by-normalized-ample-finite-suprema-20261005-continuation120.md']
binding=K/'P16-continuation121-intrinsic-model-reference-binding.json'
save(binding,{'recorded_utc':datetime.now(timezone.utc).isoformat(),
    'note':str(note),'note_sha256':sha(note),'entire_saved_note_root_read':True,
    'sources':[{'path':str(p),'sha256':sha(p)} for p in sources],
    'independent_review_performed':False,'original_closed':False,
    'only_exact_actual_ample_G0_granted':True,
    'native114_115_private_outputs_read_or_used':False,'hot_feedback_sent':False,
    'whole_primary_works_root_read':False,'original_counts_incremented':False})
P=K/'public-P16.2-round113-final-reader';L=K/'P16.2-round113-root-layout-read'
save(L/'root-layout-observation.json',{
    'recorded_utc':datetime.now(timezone.utc).isoformat(),
    'paper_PDF':str(P/'P16.2-paper.pdf'),'paper_PDF_sha256':sha(P/'P16.2-paper.pdf'),
    'actual_PDF_pages':17,'actual_PDF_bytes':153263,
    'pages_rendered_and_root_visually_read':[1,17],
    'images':[{'path':str(L/f'page-{n}.png'),'sha256':sha(L/f'page-{n}.png')} for n in [1,17]],
    'readable_first_and_last_page':True,'all_pages_visually_read':False,
    'entire478_LF_source_paper_previously_root_read':True,
    'candidate':False,'original_closed':False,
    'existing_PDF_rendered_only':True,'new_PDF_compiled':False,
    'editor':'/workspace/research/root-checks/public-P16-round-46-final-reader/P16.4-paper.tex',
    'editor_modified_replaced_or_new_tab_opened':False})
for name in ['active-work.json','checklist-current.json']:
    p=R/name;data=json.loads(p.read_text());assert len(data['fully_solved_original_atoms'])==6
    data['updated_utc']=datetime.now(timezone.utc).isoformat()
    data['continuation121_unreviewed_model_reference']={
        'binding':str(binding),'sha256':sha(binding),'original_closed':False,
        'frozen_reviews114_115_modified':False}
    p.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'binding':str(binding),'binding_sha256':sha(binding),
    'layout_observation':str(L/'root-layout-observation.json'),
    'original_count':6,'original_count_incremented':False},indent=2))
