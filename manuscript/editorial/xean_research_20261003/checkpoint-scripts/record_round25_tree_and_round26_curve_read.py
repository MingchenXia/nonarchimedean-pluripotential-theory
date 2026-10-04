"""Record exact completed reading and immutable review/source bindings."""
from pathlib import Path
import datetime, hashlib, json

r = Path('/workspace/research')
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
now = datetime.datetime.now(datetime.timezone.utc).isoformat()
def save(p, value):
    assert not p.exists(), p
    p.write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n')

tree = r/'campaigns/round-25/P06.2-specified-semistable-tree-regularization'
w = tree/'artifacts/codex-luvloj'
d = r/'campaigns/round-25/P06.2-specified-semistable-tree-regularization-review'
prior = r/'root-checks/specified-tree-regularization-phase2/root-complete-read-before-review.json'
read = json.loads(prior.read_text())
for name, key in [('P06.2-argument.md','main_argument_sha256'), ('P06.2-partial.tex','source_tex_sha256'), ('status.json','source_status_sha256')]:
    assert sha(w/name) == read[key]
selections = json.loads((w/'evidence/source-selections.json').read_text())
assert len(selections) == 17
for u in selections:
    origin = Path(u['source'])
    assert sha(origin) == u['source_sha256']
    body = b'\n'.join(origin.read_bytes().split(b'\n')[u['first_lf_line']-1:u['last_lf_line']])
    assert (w/u['local_selection']).read_bytes() == body
    assert sha(w/u['local_selection']) == u['body_sha256']
for u in json.loads((w/'evidence/source-inventory.json').read_text()):
    assert sha(Path(u['original_path'])) == u['sha256']
native = json.loads((tree/'run.json').read_text())['campaign']['result']
assert native['candidate'] is False and [n['id'] for n in native['notes']] == ['n1','n2','n3']
root = r/'root-checks/specified-tree-regularization-phase3'
root.mkdir(exist_ok=False)
save(root/'canonical-result-record.json', {'source_run_sha256':sha(tree/'run.json'),'result':native})
f = json.loads((d/'freeze.json').read_text())
b = json.loads((d/'source-artifact-binding.json').read_text())
j = json.loads((d/'run.json').read_text())
review = j['campaign']['result']
assert j['campaign']['status'] == 'completed' and review['verdict'] == 'PASS'
assert len(review['premises']) == 16 and len(review['passages']) == 26
for p in review['passages']:
    assert isinstance(p['premise'],int) and 0 <= p['premise'] < len(review['premises'])
    assert p['statement'] == review['premises'][p['premise']]
assert sha(d/'argument.md') == f['argument_sha256'] == b['review_argument_sha256']
assert sha(d/'freeze.json') == b['original_freeze_sha256']
for key, hk in [('main_argument','main_argument_sha256'),('source_tex','source_tex_sha256'),('declared_proof_file','declared_proof_sha256')]:
    assert sha(Path(b[key])) == b[hk] == f[hk]
assert sha(w/'status.json') == f['source_status_sha256'] == b['source_status_sha256']
record = {'checked_utc':now,'source_workspace':str(w),'previous_complete_read_record':str(prior),
 'previous_complete_read_record_sha256':sha(prior),'main_argument_sha256':sha(w/'P06.2-argument.md'),
 'full_new_core_directly_read_LF':[1,759],'all_17_selected_primary_bodies_fully_directly_read':True,
 'all_source_origins_and_LF_bodies_rebound':True,'all_three_canonical_native_notes_fully_read':True,
 'canonical_native_result_record':str(root/'canonical-result-record.json'),
 'canonical_native_notes_distinct_from_author_local_notes':True,
 'audits_and_all_source_build_scripts_fully_read':True,
 'fresh_copy_reproduction_record':str(r/'root-checks/specified-tree-regularization-phase2/fresh-reproduction-result.json'),
 'scope':'Supplied actual connected rig-smooth strict affinoid over algebraically closed complete nontrivially valued C, supplied simply semistable TREE/model/retraction, supplied real edge-affine harmonic factorization. Both signs ordinary smooth psh on entire actual IntZ, continuous uniformly decreasing on all Z.',
 'full_original_atom_solved':False,'standard_foundations':'Precisely scoped published foundations and new applications; not a local reproof of BGR/EGA/Hartshorne.'}
save(root/'root-complete-read-record.json',record)
save(d/'root-draft-read-record.json',record)
att = {'read_utc':now,'verdict':'PASS','premise_count':16,'passage_count':26,
 'full_report_read':True,'all_premises_read':True,'all_passages_read':True,
 'passage_premise_zero_based_exact_statement_checks':True,
 'root_full_main_and_all_canonical_notes_read':True,'publish_exact_scope':True,
 'run_sha256':sha(d/'run.json'),'argument_sha256':sha(d/'argument.md'),'freeze_sha256':sha(d/'freeze.json'),
 'source_artifact_binding_sha256':sha(d/'source-artifact-binding.json'),
 'root_read_record_sha256':sha(d/'root-draft-read-record.json'),'full_original_atom_solved':False,
 'governing_report':review['report'],
 'editorial_corrections_only':'Hartshorne IV Example1.3.3; I Corollary6.10 following Theorem6.9; residual divisor/orders, not normalized function, are independent of scalar. Formal-etale standard references clarified without changing the proof.',
 'limit':'Same-model review is not formal verification or priority certification.'}
save(d/'review-read-attestation.json',att)
save(root/'canonical-review-result.json',{'source_run_sha256':sha(d/'run.json'),'result':review})

campaign = r/'campaigns/round-26/P06.2-arbitrary-field-curve-recognition-integration-v2'
w = campaign/'artifacts/codex-V8ZFSU'
d = r/'campaigns/round-26/P06.2-arbitrary-field-curve-recognition-integration-v2-review'
root = r/'root-checks/arbitrary-field-curve-integration-phase1'
root.mkdir(exist_ok=False)
native = json.loads((campaign/'run.json').read_text())['campaign']['result']
assert native['candidate'] is False and [n['id'] for n in native['notes']] == ['n1','n2','n3']
save(root/'canonical-result-record.json',{'source_run_sha256':sha(campaign/'run.json'),'result':native})
manifest = json.loads((w/'sources/manifest.json').read_text())
assert len(manifest) == 23
for m in manifest:
    p = w/m['artifact']; origin = Path(m['read_only_origin'])
    assert p.read_bytes() == origin.read_bytes() and sha(p) == m['sha256']
units = json.loads((w/'sources/primary-units.json').read_text())
assert len(units) == 16
main = (w/'P06.2-argument.md').read_text()
assert len(main.split('\n')) == 1232
for u in units:
    body = b'\n'.join((w/'sources'/u['source']).read_bytes().split(b'\n')[u['first_lf_line']-1:u['last_lf_line']])
    assert (w/u['artifact']).read_bytes() == body and sha(w/u['artifact']) == u['body_sha256']
    assert body.decode() in main
incoming = json.loads((campaign/'input.json').read_text())
support = {}
for note in incoming['notes']:
    nid = note['id']; body = (w/f'sources/{nid}-argument.md').read_text()
    assert body in note['text'] and note['text'] in (d/'argument.md').read_text()
    assert note['imported'] and note['verified'] and not note['accepted'] and not note['candidate']
    receipt = json.loads((w/f'sources/{nid}-review.json').read_text())
    assert receipt['result']['verdict'] == 'PASS'
    for p in receipt['result']['passages']:
        assert p['statement'] == receipt['result']['premises'][p['premise']]
    support[nid] = {'argument_sha256':sha(w/f'sources/{nid}-argument.md'),
                   'review_receipt_sha256':sha(w/f'sources/{nid}-review.json'),
                   'exact_prior_scope':receipt['precise_scope'],
                   'full_previous_root_read_reused_unchanged':True}
f = json.loads((d/'freeze.json').read_text());b = json.loads((d/'source-artifact-binding.json').read_text())
assert sha(d/'argument.md') == f['argument_sha256'] == b['review_argument_sha256']
assert sha(d/'freeze.json') == b['original_freeze_sha256']
for key,hk in [('main_argument','main_argument_sha256'),('source_tex','source_tex_sha256'),('declared_proof_file','declared_proof_sha256')]:
    assert sha(Path(b[key])) == b[hk] == f[hk]
assert sha(w/'status.json') == f['source_status_sha256'] == b['source_status_sha256']
record = {'checked_utc':now,'source_workspace':str(w),'main_argument_sha256':sha(w/'P06.2-argument.md'),
 'full_new_main_directly_read_LF_ranges':[[1,300],[301,622],[623,961],[962,1232]],
 'all_three_actual_canonical_native_notes_fully_read':True,'canonical_native_result_record':str(root/'canonical-result-record.json'),
 'all_16_selected_primary_bodies_fully_directly_read':True,'all_23_source_support_copies_rebound_to_unchanged_origins':True,
 'all_16_raw_LF_bodies_and_main_embeddings_exact':True,
 'audits_status_and_source_build_scripts_fully_read':True,
 'known_support_full_body_reuse':support,
 'n701_authoritative_main_sha256':sha(w/'sources/n701-argument.md'),
 'n701_distinct_published_wrapper_sha256':sha(w/'sources/n701-published-review-wrapper.md'),
 'review_binding_sha256':sha(d/'source-artifact-binding.json'),
 'independent_review_verdict_read':False,'publication_allowed':False,'full_original_atom_solved':False,
 'scope':'Recognition only on actual good separated strict boundaryless PURECURVES over arbitrary complete nontrivial K. All extensions/all curve-map quantifiers obtained after recognized harmonic-function descent. No arbitrary transcendental-current ascent or ordinary two-sign smoothing theorem.'}
save(root/'root-complete-read-before-review.json',record)
print(json.dumps({'tree_review':'PASS16/26','tree_attestation_sha256':sha(r/'campaigns/round-25/P06.2-specified-semistable-tree-regularization-review/review-read-attestation.json'),
 'curve_read_record_sha256':sha(root/'root-complete-read-before-review.json'),'full_original_atoms_solved':0},indent=2))
