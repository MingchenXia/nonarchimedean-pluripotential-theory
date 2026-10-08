"""Fresh data-only identity audit. Never imports or executes supplied code."""
import json, pathlib, hashlib, datetime, re

ROOT = pathlib.Path.cwd()
def digest(b): return hashlib.sha256(b).hexdigest()
def read_json(p): return json.loads(p.read_text())
math = read_json(ROOT / 'inputs/mathematical-packet-bindings.json')
def local(i):
    return ROOT / 'inputs/mathematical' / (f'{i:02d}-' + pathlib.Path(math[i]['path']).name)
incoming = read_json(ROOT / 'input.json')
grants = ROOT / 'inputs/grants'; grants.mkdir(exist_ok=True)
paper = local(12).read_bytes()
checks = []
for note in incoming['notes']:
    b = note['text'].encode()
    (grants / (note['id'] + '-qualified.txt')).write_bytes(b)
    (grants / (note['id'] + '-complete-note.json')).write_text(json.dumps(note, ensure_ascii=False, indent=2))
    checks.append({'id':note['id'], 'bytes':len(b), 'sha256':digest(b),
                   'native250_entire_literal_present': b in paper})
# Exact component bytes, removing only a separately declared framing separator.
parts = incoming['notes'][1]['text'].split('===== ENTIRE QUALIFIED B341 COMPONENT: ')[1:]
for i, part in zip(range(5,12), parts):
    heading, content = part.split(' =====\n',1)
    b = local(i).read_bytes()
    raw = content.encode()
    framing = b'\n\n' if raw == b + b'\n\n' else b''
    checks.append({'component':i, 'heading':heading, 'framing_removed_bytes':len(framing),
                   'exact_body_match':raw[:-len(framing)] == b if framing else raw == b})
binding = read_json(local(20))
hist = {}
for key, pathkey in [('own33_current_physical_checks','current_path'),
                     ('author52_origin_and_local104_current_physical_checks','path')]:
    rows = []
    for row in binding[key]:
        p = pathlib.Path(row[pathkey]); r = dict(row)
        r['currently_available'] = p.is_file()
        if p.is_file():
            b = p.read_bytes()
            r.update(current_bytes=len(b), current_sha256=digest(b),
                     exact_current_match=len(b)==row['bytes'] and digest(b)==row['sha256'])
        rows.append(r)
    hist[key] = rows
hist['unavailable_claim_boundary'] = 'Only these explicitly bound current files were audited; no attestation about other historical bytes or old command states.'
(ROOT/'evidence/historical-current-bindings.json').write_text(json.dumps(hist, indent=2))
native = read_json(local(24)); original = read_json(local(21))
a = native['problem'].encode(); b = original['problem'].encode()
scope = {'ROOT_original_keys':list(original), 'native_original_keys':list(native),
         'ROOT_problem_bytes':len(b),'native_problem_bytes':len(a),
         'raw_equal':a==b,'native_has_exact_two_extra_trailing_LF':a==b+b'\n\n',
         'native_problem_txt_exact':local(22).read_bytes()==a,
         'ROOT_problem_sha256':digest(b),'native_problem_sha256':digest(a),
         'augmented_assignment_separate_sha256':digest(local(23).read_bytes())}
expanded = read_json(local(18)); actual = read_json(local(19))
argument = local(13).read_text()
proofmatches=[]
bodymatches=[]
sections=list(re.finditer(r'^# (n\d+)\. ([^\n]+)\n',argument,re.M))
for note in expanded['notes']:
    position=next(i for i,m in enumerate(sections) if m.group(1)==note['id'])
    m=sections[position]
    chunk=argument[m.end():sections[position+1].start() if position+1<len(sections) else len(argument)]
    body=chunk.split('\n\n',1)[-1].strip()
    assert body in note['text']
    bodymatches.append({'id':note['id'],'argument_body_in_expanded':True,
                        'argument_body_chars':len(body),'text_chars':len(note['text'])})
    proofmatches.append({'id':note['id'],'expanded_text_bytes':len(note['text'].encode()),
                         'actual_text_bytes':len(next(n for n in actual['notes'] if n['id']==note['id'])['text'].encode()),
                         'actual_and_expanded_text_equal':note['text']==next(n for n in actual['notes'] if n['id']==note['id'])['text']})
(ROOT/'evidence/expanded-proof-matches.json').write_text(json.dumps(bodymatches,indent=2))
out={'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'grant_checks':checks,
     'scope_identity':scope,'note_field_distinctions':proofmatches,
     'actual_note_count':len(actual['notes']),'expanded_note_count':len(expanded['notes']),
     'all_primary_and_mathematical_bound_inputs':read_json(ROOT/'evidence/input-bindings.json'),
     'historical_summary':{key:{'entries':len(rows),'available':sum(r['currently_available'] for r in rows),
                              'matching':sum(r.get('exact_current_match',False) for r in rows)}
                           for key,rows in hist.items() if isinstance(rows,list)}}
(ROOT/'evidence/review-byte-audit.json').write_text(json.dumps(out,indent=2))
assert all(c.get('exact_body_match', True) for c in checks)
assert all(c.get('native250_entire_literal_present', True) for c in checks)
assert scope['native_has_exact_two_extra_trailing_LF'] and scope['native_problem_txt_exact']
assert all(r['match'] for r in out['all_primary_and_mathematical_bound_inputs'])
assert all(r.get('exact_current_match',False) for k,rows in hist.items() if isinstance(rows,list) for r in rows)
print(json.dumps({'grants':checks,'scope_identity':scope,'historical_summary':out['historical_summary'],
                  'actual_notes':len(actual['notes']),'expanded_notes':len(expanded['notes'])},indent=2))
