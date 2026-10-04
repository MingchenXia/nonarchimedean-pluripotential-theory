from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import subprocess

R = Path('/workspace/research')
md = R / 'root-checks/P16.1-nodal-normalization-obstruction-20261004.md'
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
assert sha(md) == '87b4a86d09b5a64b2391e25ebba6e701a64b5139c8ee753255f63d596590c639'
d = R / 'root-checks/P16.1-nodal-obstruction-paper-20261004'
d.mkdir(exist_ok=False)
paper_md = d / 'P16.1-nodal-obstruction-paper.md'
paper_md.write_text('---\ntitle: A nodal compatibility obstruction for finite-energy equations\nauthor: Local research continuation for P16.1\ndate: 4 October 2026\n---\n' + md.read_text().split('\n',1)[1])
tex = d / 'P16.1-nodal-obstruction-paper.tex'
cmd = ['pandoc', str(paper_md), '--standalone', '--from=markdown+tex_math_dollars',
    '--to=latex', '-V','geometry:margin=1in','-V','fontsize=11pt','-V','colorlinks=true',
    '--output',str(tex)]
run = subprocess.run(cmd,capture_output=True,text=True)
(d / 'pandoc.stdout').write_text(run.stdout)
(d / 'pandoc.stderr').write_text(run.stderr)
assert run.returncode == 0,run.stderr
def bind(p):
    p = Path(p)
    return {'path':str(p),'bytes':p.stat().st_size,'sha256':sha(p)}
units_dir = d / 'source-extracts'
units_dir.mkdir()
specs = [
    ('P16-arxiv-1201.0188-20261004.txt',1829,1875,'Full published curve-current equation and uniqueness argument; finite-energy scope explicitly separated.'),
    ('P16-arxiv-1805.01016-20261004.txt',2620,2708,'Smooth curvature endpoint and full Proposition 8.3, Theorem 8.4 statement; projection formula is a new checked application.'),
    ('P16-arxiv-1805.01016-20261004.txt',3540,3588,'Definition 9.13 and full Proposition 9.14, including normalization and birational energy proof.'),
    ('P16-arxiv-2209.04879-20261004.txt',1932,1997,'Complete valued-field continuous endpoint, mass formula and finite-energy Remark 4.4; no general finite-energy theorem inferred.'),
    ('Thuillier-tel-00010990v1.txt',5793,5905,'Dirichlet Hilbert construction and full Proposition 3.5.2 proof; W1 completion has continuous nonrigid evaluation.'),
    ('Thuillier-tel-00010990v1.txt',6067,6115,'Full Proposition 3.5.9 dual-energy proof and sign; actual PDF pages118-119 also inspected.')]
units = []
for name,lo,hi,scope in specs:
    source = R / 'shared-sources' / name
    literal = source.read_bytes().decode('utf-8').split('\n')
    selected = '\n'.join(literal[lo-1:hi])+'\n'
    p = units_dir / f'{source.stem}-LF-{lo}-{hi}.txt'
    p.write_bytes(selected.encode('utf-8'))
    units.append({'source':bind(source),'LF':[lo,hi],'literal_unit':bind(p),
        'scope_read':scope,'new_application_checked':True})
cache = json.loads((R / 'shared-sources/P16-public-primary-cache-20261004.json').read_text())
pdfs = [bind(s['pdf']) for s in cache['sources'] if s['arxiv_id'] in ('1201.0188','1805.01016','2209.04879')]
pdfs.append(bind(R / 'shared-sources/Thuillier-tel-00010990v1.pdf'))
images = [bind(R / 'shared-sources/P16-Thuillier-energy-primary-pages-20261004' / f'actual-page-{n}.png') for n in (114,118,119)]
data = {'prepared_utc':datetime.now(timezone.utc).isoformat(),
    'origin':'Fresh root proof with public primary mathematical sources and explicit standard algebraic background; not a native-author or independent-review result.',
    'mathematical_source':bind(md),'standalone_paper_markdown':bind(paper_md),'standalone_tex':bind(tex),
    'markdown_body_exactly_preserved_except_title_metadata':paper_md.read_text().split('---\n',2)[2]==md.read_text().split('\n',1)[1],
    'pandoc_command':cmd,'pandoc_returncode':run.returncode,
    'root_entire_markdown_read_LF':[1,130],
    'source_units':units,'actual_public_PDFs':pdfs,'actual_Thuillier_visual_pages':images,
    'new_application_checks':[
        'Actual invertible degree-two ample line bundle glued at the node; displayed matching sections are global and have no common zero.',
        'Fubini-Study reference equality checked at all Berkovich points, including cancellation on |T|=1; raw degree and mass are2.',
        'Continuous metric projection uses model intersection/fundamental class pushforward then uniform endpoint continuity; energy equality alone is not substituted.',
        'Canonical normalized solution computed on all points with unequal two rigid endpoint values that no constant shift repairs.',
        'Segment resistance inequality extended through W1 nonrigid evaluations; energy normalized only for dual condition; exact bound ell and witness upstairs computed.',
        'Downstairs dual energy bounded on the specified monotone completion by continuous birational energy invariance; no unidentified larger cone is asserted.',
        'Finite-energy nonexistence consequence uses exactly three stated metric/energy/locality interfaces and smooth-normalization full raw mass; no global unbounded projection formula assumed.',
        'Multibranch example does not claim an obstruction for the geometrically unibranch range or original catalogue closure.'
    ],
    'standard_algebraic_inputs':['Rational projective nodal cubic and normalization coordinate with preimages0,infinity.','Invertible sheaf conductor gluing with identity fiber map.','Positive degree iff ample on an integral projective curve.'],
    'native_editor_state':'Not yet requested.','standalone_tex_full_read':False,
    'independent_acceptance':False,'original_atoms_closed':[],
    'active_authors_received_feedback':False,'external_export_attempted':False}
assert data['markdown_body_exactly_preserved_except_title_metadata']
(d / 'preparation-binding.json').write_text(json.dumps(data,indent=2)+'\n')
print(json.dumps({'directory':str(d),'tex':bind(tex),'binding':bind(d/'preparation-binding.json')},indent=2))
