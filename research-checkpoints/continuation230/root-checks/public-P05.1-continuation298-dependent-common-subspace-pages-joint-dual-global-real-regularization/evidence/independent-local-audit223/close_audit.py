"""Own final metadata checks and source-metadata clarification; no external commands."""
import hashlib
import json
from pathlib import Path

updates = {
    'audit-report.md': [
        ('FAIL narrowly at an unused source-unit label.', 'FAIL narrowly at source metadata: an unused unit label and older whole-proof range endpoints.'),
        ('this does not invalidate the mathematical proof.', 'older grant ledgers also call LF604–667 the whole BBGS3.15 proof, whose ending is670. NEW298 correctly includes670. These metadata errors do not invalidate the mathematical proof.')],
    'independent-reconstruction.md': [
        ('fails narrowly at the unused BMPS Proposition 4.16 label described in source-application-audit.md.', 'fails narrowly at the unused BMPS Proposition 4.16 label and older BBGS3.15 range endpoints described in source-application-audit.md.')],
    'whole-proof-coverage.md': [
        ('FAILS narrowly at an unused unit label.', 'FAILS narrowly at an unused unit label and older BBGS3.15 whole-proof range endpoints.')],
}
for name,pairs in updates.items():
    text = Path(name).read_text()
    for old,new in pairs:
        if old in text:
            text=text.replace(old,new)
        else:
            assert new in text
    Path(name).write_text(text)

payload=json.loads(Path('native-notes.json').read_text())
raw_ibp_old='Z(e)(b(v)−b(w))(c(w)−c(v))/L_e'
raw_ibp_new='Z(e)(b(v)−b(w))(c(w)−c(v))/lambda_e, with w−v=lambda_e n_e/v and n_e/v primitive saturated'
reconstruction=Path('independent-reconstruction.md').read_text()
reconstruction=reconstruction.replace(raw_ibp_old,raw_ibp_new)
Path('independent-reconstruction.md').write_text(reconstruction)
for note in payload['notes']:
    if note['id']=='n1':
        note['text']=note['text'].replace('For a rational feasible point, impose active inequalities as equalities.',
            'For any real feasible point in a rational polyhedron, impose its active inequalities as equalities.')
        note['text']=note['text'].replace(
            'polynomial uniqueness and elementary convex secants.',
            'polynomial uniqueness and elementary convex secants; for the lattice steps, the Euclidean algorithm and saturated-subgroup extension to a lattice basis.')
        note['text']=note['text'].replace(
            'the sum of nonnegative defining forms has a bounded section at one.',
            'the sum of nonnegative defining forms has a bounded section at one. Add both signs of a basis of the removed lineality; a zero quotient needs no section.')
        note['text']=note['text'].replace(
            'Homogenization gives pointed polyhedron vertex-hull plus recession generation.',
            'Homogenization gives pointed polyhedron vertex-hull plus recession generation: positive-height extreme rays normalize to vertices, since a nontrivial affine decomposition would split the ray; zero-height rays are recession generators. The height equation makes the positive-height coefficients sum to one.')
    if note['id']=='n2':
        note['summary']='Essential source/raw applications PASS under exactly six whole grants. Source-metadata FAIL: unused BMPS unit label and older BBGS3.15 whole-proof range endpoints; no mathematical counterexample.'
        endpoint_detail=' Older whole-proof604–667 citations omit the actual670 ending; NEW298 and this audit include it. This is a metadata limitation, not evidence that past PDF readers omitted the ending.'
        if endpoint_detail not in note['detailedSummary']:
            note['detailedSummary'] += endpoint_detail
        old='At rational v∈H choose rational a∈L_2\\L_1 and its two-sided line.'
        new='In the crossing sector, with an actual second page, at rational v∈H choose rational a∈L_2\\L_1 and its two-sided line.'
        if old in note['text']:
            note['text']=note['text'].replace(old,new)
        endpoint_text='\n\nSource-range verdict for older whole-proof citations604–667: FAIL as exact endpoint metadata, since LF668–670 contains the final equality and closing proof sentence. This does not establish a historical failure to inspect a rendered full page. NEW298 correctly identifies the ending670; my604–704 display included it. The essential commutation application was checked against the entire original unit.'
        if endpoint_text not in note['text']:
            note['text'] += endpoint_text
        note['text']=note['text'].replace(raw_ibp_old,raw_ibp_new)
        denominator_detail='\n\nFor the rational-row jump, write the actual row as m/N. A unimodular integer basis sends m to(G,0,...,0), so the ORIGINAL row becomes(g,0,...,0) with g=G/N, and its actual two-sided jump is2g. Denominator clearing is undone; the rational heights/determinants and actual scalar factors are retained. A repeated row restricts to zero on its own kernel. For singular rows the common rational lineality gives a carrier with no zero-dimensional faces, so the top product vanishes; subdivision invariance excludes artificial atoms on finer carriers. No extra normalization is introduced.'
        if denominator_detail not in note['text']:
            note['text'] += denominator_detail
    if note['id']=='n4':
        note['text']=note['text'].replace(
            'FAILS narrowly because an explicitly unused BMPS Proposition4.16 is labelled Definition4.16.',
            'FAILS narrowly because an explicitly unused BMPS Proposition4.16 is labelled Definition4.16 and older grant ledgers cite604–667 as the whole BBGS3.15 proof although its ending is670. NEW298 correctly includes670.')
        note['text']=note['text'].replace('frozen-verification.json and three frozen manifest snapshots;',
            'frozen-verification.json/final-bound-source-verification.json and three frozen manifest snapshots;')
payload['candidate']=False
assert set(payload)=={'notes','candidate'}
assert len(payload['notes'])==4
for i,note in enumerate(payload['notes']):
    assert set(note)=={'id','summary','detailedSummary','text','support'}
    assert note['id']==f'n{i+1}'
    assert all(ref in [n['id'] for n in payload['notes'][:i]] for ref in note['support'])
Path('native-notes.json').write_text(json.dumps(payload,indent=2,ensure_ascii=False)+'\n')

verified=[]
for manifest in ['frozen-mathematical-packet-bindings.json',
                 'frozen-historical-own-evidence-bindings.json',
                 'frozen-private-primary-packet-bindings.json']:
    rows=json.loads(Path(manifest).read_text())
    for i,row in enumerate(rows):
        data=Path(row['path']).read_bytes()
        actual=hashlib.sha256(data).hexdigest()
        assert len(data)==row['bytes'] and actual==row['sha256'],(manifest,i)
        verified.append(dict(manifest=manifest,index=i,bytes=len(data),sha256=actual))
assert len(verified)==159
Path('final-bound-source-verification.json').write_text(json.dumps(verified,indent=2)+'\n')

bindings=[]
own_paths=list(Path('.').iterdir())+list(Path('LOCALONLY').iterdir())
for path in sorted(own_paths):
    if path.is_file() and path.name!='artifact-bindings.json':
        data=path.read_bytes()
        bindings.append(dict(filename=str(path),bytes=len(data),sha256=hashlib.sha256(data).hexdigest()))
Path('artifact-bindings.json').write_text(json.dumps(bindings,indent=2)+'\n')
print(json.dumps(dict(frozen_entries_unchanged=len(verified),notes=len(payload['notes']),
                     own_artifacts=len(bindings),candidate=payload['candidate'])))
