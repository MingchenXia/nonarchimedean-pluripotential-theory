from pathlib import Path
from datetime import datetime,timezone
import hashlib,json

root=Path(__file__).resolve().parent
R=Path('/workspace/research')
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
dictionary=R/'campaigns/round-99/P16.1-original-self-contained-full-review/primary-literal-body-dictionary.json'
d=json.loads(dictionary.read_text())
specs=[
 ('Temkin-theorem1-2-1','8e04c8c70067b9241eac60096b1d40f71432c02710482d42b86cda7b4327d64f',[82,91]),
 ('Temkin-finite-stabilization4-1-3','0e83f63e3296a2fe2043512f2317647039a7010757aec51315752e217ac4c9d0',[1526,1551]),
 ('Temkin-main-proof1-2-1','33518fa382ca7543017cd847eec37abbc72a2fa03d9ace110dfc9b0942b4cf24',[1693,1886])]
units=[]
for label,key,lines in specs:
    body=d[key]
    target=root/(label+'.literal.txt')
    assert not target.exists()
    target.write_text(body)
    assert sha(target)==key
    units.append({'path':str(target),'sha256':key,'dictionary':str(dictionary),
      'dictionary_sha256':sha(dictionary),'inclusive_zero_based_renderer_lines':lines,
      'url':'https://arxiv.org/pdf/0904.1592v2','version':'v2,11 December2011',
      'entire_selected_body_root_read':True,'whole_primary_root_read':False})
source=R/'shared-sources/Temkin-0904.1592v2-20261005.txt'
target=root/'Temkin-actual-finite-blowup-definitions.literal.txt'
assert not target.exists()
target.write_text('\n'.join(source.read_text().split('\n')[449:508])+'\n')
units.append({'path':str(target),'sha256':sha(target),'source':str(source),'source_sha256':sha(source),
 'inclusive_one_based_LF':[450,508],'extraction_rule':'split LF, inclusive range, one trailing LF',
 'url':'https://arxiv.org/pdf/0904.1592v2','entire_selected_body_root_read':True,'whole_primary_root_read':False})
note=R/'root-checks/P16.2-projective-modification-and-all-field-resolution-audit-20261005-continuation112.md'
binding=root/'binding.json'
assert not binding.exists()
binding.write_text(json.dumps({'recorded_utc':datetime.now(timezone.utc).isoformat(),
 'note':str(note),'note_sha256':sha(note),'entire_saved_note_root_read':True,
 'independent_review_performed':False,'original_closed':False,'units':units,
 'actual_Temkin_pdf':{'path':str(R/'shared-sources/Temkin-0904.1592v2-20261005.pdf'),
                     'sha256':sha(R/'shared-sources/Temkin-0904.1592v2-20261005.pdf')},
 'new_Stacks_response':{'path':str(root/'Stacks-primary-web-response.json'),
                       'sha256':sha(root/'Stacks-primary-web-response.json'),
                       'urls':['https://stacks.math.columbia.edu/tag/07QW',
                               'https://stacks.math.columbia.edu/tag/07QU',
                               'https://stacks.math.columbia.edu/tag/0B8X'],
                       'entire_three_printed_mathematical_statement_and_proof_units_root_read':True},
 '07QU_localization_omitted_proof_not_read_and_not_used':True,
 'recursive_resolution_and_Stacks_cross_references_not_all_read':True,
 'active108_109_private_outputs_read_or_used':False,'hot_feedback_sent':False},indent=2)+'\n')
print(json.dumps({'binding':str(binding),'sha256':sha(binding),'units':len(units)}))
