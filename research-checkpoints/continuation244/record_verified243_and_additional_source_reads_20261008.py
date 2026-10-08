from pathlib import Path
from datetime import datetime, timezone
import hashlib, json

R=Path('/workspace/research');G=R/'github-checkpoint';K=R/'root-checks'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
M=G/'upload-manifest-continuation243.json';d=json.loads((G/'push-receipt-continuation243.json').read_text());m=json.loads(M.read_text())
assert d['parent_sha']=='79f007ee717f62ced9ae236a278a0157bc34f1f0' and d['commit_sha']=='fe311b244a6dd0a6fc16b669ec93048148acb6aa'
assert d['tree_sha']=='660bb631c93e3689423a820df402112d2c79d8ef' and d['files']==len(m['files'])+1==64
assert d['manifest_sha256']==sha(M)=='70078db81997791606b28c39faf27e69aefa1fe6382b22d866d6a89e25a55bda'
assert not d['force_update'] and all(d[k]for k in('remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified'))
now=datetime.now(timezone.utc).isoformat()
for name in('active-work.json','checklist-current.json'):
    p=R/name;x=json.loads(p.read_text());assert len(x['fully_solved_original_atoms'])==11 and x['remaining_open_original_atoms']==31 and x['historical_reviewed_scoped_papers']==89 and x['github_pending_checkpoint']['continuation']==243
    assert x['fully_solved_original_atoms']==d['fully_solved_original_atoms']
    x.update(github_checkpoint=d,github_pending_checkpoint=None,updated_utc=now);p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
source=R/'primary-data-LOCALONLY/P12.2-conductor-integral-dependence-20261008';book=source/'Swanson-Huneke-author-book.txt';pdf=source/'Swanson-Huneke-author-book.pdf'
assert sha(book)=='9b15169d0c624e89a2b91153690e8a348c8c9f23e412a6cc0e4bde6510d25392'
assert sha(pdf)=='a12705f066aee67648768bc37b58a37c661907dc3918a71974c1441bc551a18b'
p=K/'P12.2-additional-Rees-residue-and-dimension-formula-ROOT-reading-20261008.json';assert not p.exists()
images=[source/f'ROOT-Rees-residue-additional-read-{n}.png'for n in(223,224)]
record=dict(recorded_utc=now,pdf_path=str(pdf),pdf_sha256=sha(pdf),text_path=str(book),text_sha256=sha(book),source_version='Current author-hosted July2024 file, not a byte-identity claim for the 2006 printing',original_url='https://www.math.purdue.edu/~iswanso/book/SwansonHuneke.pdf',whole_primary_units_additionally_ROOT_read=[dict(unit='10.2.2 and 10.2.3 complete immediate proofs, with 10.2.1 context',LF_inclusive=[9230,9360]),dict(unit='10.4.3 complete immediate proof, with 10.4.2 context',LF_inclusive=[9700,9770]),dict(unit='B.2.5 complete proof supplying B.3.2 modification context',LF_inclusive=[19223,19273]),dict(unit='B.3.2 complete statement and immediate source modification explanation; B.3.6/7 context',LF_inclusive=[19272,19324]),dict(unit='B.5.1 complete immediate proof, final continuation included',LF_inclusive=[19438,19482])],primary_PDF_pages_ROOT_visually_read=[dict(one_based_PDF_page=n,printed_page=n-14,image_path=str(q),image_sha256=sha(q),LOCALONLY=True)for n,q in zip((223,224),images)],application_qualifications=['The Rees residue degree equals ht(P)-1 at formally equidimensional local targets; the general formula instead uses the selected minimal component of the completion.','For the excellent domain birational chart used in native236 density, universal catenarity and generic transcendence degree zero give the exact B.3.2 dimension formula; combine it with 10.4.3 and residue-field transcendence-degree additivity.','Integral-closure bars in 10.4.3 were checked in actual primary PDF pixels; text extraction alone was not relied on for those bars.','B.3.2 cites a modification of B.2.5 rather than a separate displayed full proof. The entire immediate B.2.5 proof and the explicit catenarity equality explanation were additionally read.','Recursive book foundations, historical original Rees/Ratliff editions and all463PDF pages are not freshly independently read or reconstructed.'],source_bodies_and_images_excluded_from_publication=True,private_active_native_output_read=False,hot_feedback_sent=False,new_mathematical_grant=False,new_accepted_paper=False,original_closed=False)
p.write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(verified_checkpoint=243,commit_sha=d['commit_sha'],originals_solved=11,originals_open=31,accepted_papers=89,additional_source_read_metadata=str(p),metadata_sha256=sha(p)),indent=2))
