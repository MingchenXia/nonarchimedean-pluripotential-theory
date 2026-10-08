from pathlib import Path
from datetime import datetime, timezone
import hashlib,json
R=Path('/workspace/research');K=R/'root-checks';G=R/'github-checkpoint'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def write(p,x):Path(p).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
receipt=G/'push-receipt-continuation245.json';x=json.loads(receipt.read_text())
assert x['commit_sha']=='cad9792fb7df5fc81ed452198e46eeadc15c88d6' and x['tree_sha']=='943917793e2ab873b1cdedf61e104e1f6fcf22a2'
assert x['manifest_sha256']==sha(G/'upload-manifest-continuation245.json')=='d8f88f8a8225e4028785f7140f72d2b0fb93ec1544f209897956035762f991a2'
assert not x['force_update'] and all(x[k]for k in ('remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified'))
assert sha(K/'public-P16-round-46-final-reader/P16.4-paper.tex')=='09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
now=datetime.now(timezone.utc).isoformat()
for name in ('active-work.json','checklist-current.json'):
    p=R/name;y=json.loads(p.read_text());assert y['github_pending_checkpoint']['continuation']==245 and len(y['fully_solved_original_atoms'])==11 and y['remaining_open_original_atoms']==31 and y['historical_reviewed_scoped_papers']==89
    y.update(updated_utc=now,latest_verified_github_checkpoint=dict(continuation=245,commit=x['commit_sha'],tree=x['tree_sha'],receipt=str(receipt),receipt_sha256=sha(receipt),receipt_reported_utc=x['verified_utc'],ROOT_observed_completed_utc=now,remote_ref_verified=True,all_file_blob_bindings_verified_remote=True,independent_native_git_tree_verified=True,force_update=False),github_pending_checkpoint=None,next_work='Continue independent entire-original P12.2review240 and P05.2review241; ROOT read complete actual reports and current exact source applications before acceptance; max2 native campaigns. Verified GitHub245.11 solved31 OPEN89 accepted.');write(p,y)
rows=(R/'checklist-current.tsv').read_text().splitlines()
for i,line in enumerate(rows[1:],start=1):
    parts=line.split('\t')
    if parts[0]=='P05.2':parts[2]='whole_original_candidate239_14p_ROOT_read_independent_review241_running_original_open'
    elif parts[0]=='P12.2':parts[2]='whole_original_candidate238_23p_ROOT_read_independent_review240_running_original_open'
    elif parts[0]=='P19.2':parts[2]='joint_entropy_partial_accepted_original_general_approximation_open_prior169170_original_scope_INCONCLUSIVE'
    rows[i]='\t'.join(parts)
(R/'checklist-current.tsv').write_text('\n'.join(rows)+'\n')
C=next((R/'campaigns/round-239').iterdir());primary=json.loads((C/'private-primary-packet-bindings.json').read_text());pdf=next(e for e in primary if e['label']=='BBGS' and e['format']=='pdf');txt=next(e for e in primary if e['label']=='BBGS' and e['format']=='txt')
assert sha(pdf['path'])==pdf['sha256'] and sha(txt['path'])==txt['sha256']
p=K/'P05.2-additional-BBGS-real-signed-recursion-and-normalization-ROOT-reading-20261008.json';assert not p.exists()
write(p,dict(recorded_utc=now,source_url=pdf['literal_url'],source_version=pdf['version'],pdf_path=pdf['path'],pdf_sha256=pdf['sha256'],text_path=txt['path'],text_sha256=txt['sha256'],complete_immediate_units_ROOT_reread=[dict(literal_LF_inclusive=[379,532],units='2.14/2.15 quasiembedding and Euclidean setting,3.1--3.9 real/signed weights and negative inward unit-normal product'),dict(literal_LF_inclusive=[533,674],units='Entire3.12 subdivision/restriction proof and entire3.15 commutation proof ending670; next context included'),dict(literal_LF_inclusive=[675,718],units='Entire3.18 immediate proof and entire3.19 balancing proof and homomorphism continuation')],current_application='Native239 n2 full signed/zero primitive recursion: x->(x,1), saturated facet-basis primitive height covol(Nsigma)/covol(Ntau), weights covol(Nsigma)*primitiveweight, factor -p cancels source negative-normal sign, repeated every dimension.',qualifications=['Arbitrary real weights and signed/zero intermediate weights are the literal source domain.','Primitive balancing and Euclidean unit-normal balancing are related by the covolume factors; normals are not silently relabeled.','Source3.19 product commutation cites3.12 but the needed already-complete argument is3.15; explicit corrected application retained.','The finite polynomial contains raw mixed-order factorial naturally, with no appended normalization.','Selected complete text proof units are ROOT-read; no fresh whole44-page visual or recursive historical attestation.','This independent reading adds no caller Note, accepted paper, original closure or correctness grant.'],primary_bodies_and_excerpts_not_publicly_copied=True,active240241_inputs_unchanged=True,hot_feedback_sent=False,new_accepted_paper=False,original_closed=False))
print(json.dumps(dict(recorded_verified_checkpoint=245,commit=x['commit_sha'],counts=dict(solved=11,open=31,accepted_papers=89),pending_checkpoint=None,new_primary_reading_metadata=str(p)),indent=2))
