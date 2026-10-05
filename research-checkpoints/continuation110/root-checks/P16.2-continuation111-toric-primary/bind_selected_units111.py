from pathlib import Path
from datetime import datetime, timezone
import hashlib, json

root = Path(__file__).resolve().parent
research = Path('/workspace/research')
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
note = research/'root-checks/P16.2-proper-nonprojective-toric-test-and-source-audit-20261005-continuation111.md'
specs = [
    ('Rohrer-orbit-cover-and-properness', 'Rohrer-dissertation.txt', 9829, 10228,
     'https://fredrohrer.ch/wp-content/uploads/2020/06/diss.pdf',
     ['IV1.3.1--1.3.9', 'IV1.3.11', 'IV1.3.12']),
    ('Rohrer-star-fan-and-completeness', 'Rohrer-dissertation.txt', 4035, 4145,
     'https://fredrohrer.ch/wp-content/uploads/2020/06/diss.pdf', ['II2.2.5--2.2.7']),
    ('Rohrer-separatedness-finite-presentation-statement', 'Rohrer-dissertation.txt', 9780, 9792,
     'https://fredrohrer.ch/wp-content/uploads/2020/06/diss.pdf', ['IV1.2.1']),
    ('Fujino-Sato-example4-4-and-continuation', 'Fujino-Sato-wSato.txt', 212, 247,
     'https://www.math.kyoto-u.ac.jp/~fujino/wSato.pdf', ['Example4.4']),
]
units=[]
for label, source, first, last, url, statements in specs:
    p=root/source
    lines=p.read_text().split('\n')
    assert last <= len(lines)
    target=root/(label+'.literal.txt')
    assert not target.exists()
    target.write_text('\n'.join(lines[first-1:last])+'\n')
    units.append({'path':str(target), 'sha256':sha(target), 'source':str(p),
                  'source_sha256':sha(p), 'inclusive_one_based_LF':[first,last],
                  'extraction_rule':'split on LF, select inclusive range, add one trailing LF',
                  'url':url, 'statements':statements,
                  'entire_selected_unit_root_read_before_binding':True,
                  'whole_primary_root_read':False})
binding=root/'binding.json'
assert not binding.exists()
binding.write_text(json.dumps({'recorded_utc':datetime.now(timezone.utc).isoformat(),
    'note':str(note), 'note_sha256':sha(note), 'entire_saved_note_root_read':True,
    'independent_review_performed':False, 'original_closed':False,
    'units':units, 'downloaded_primary_bindings':json.loads((root/'retrieval-manifest.json').read_text()),
    'Fujino_pdf_page4_minus_signs_visually_read':True,
    'Fujino_page4_image':{'path':str(root/'Fujino-Sato-page4.png'),'sha256':sha(root/'Fujino-Sato-page4.png')},
    'source_foundational_cross_references_not_read_in_full':True,
    'dissertation_IV1_2_1_printed_proof_cross_references_not_read':True,
    'Rohrer1207_0605v2_properness_is_cross_reference_not_printed_proof':True,
    'active108_109_private_outputs_read_or_used':False,
    'hot_feedback_sent':False},indent=2)+'\n')
print(json.dumps({'binding':str(binding),'sha256':sha(binding),'units':len(units)}))
