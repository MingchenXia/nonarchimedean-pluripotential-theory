#!/usr/bin/env python3
"""Rebuild the specified proof/evidence bundle using existing local tools only.

Documentary checks do not verify mathematical correctness. No network, environment
variables, installation, editor operation, or access outside the supplied catalogue.
"""
from __future__ import annotations
import hashlib
import json
import os
from pathlib import Path
import platform
import re
import shutil
import subprocess
import sys

ROOT = Path(__file__).resolve().parent
os.chdir(ROOT)

def digest(data):
    return hashlib.sha256(data).hexdigest()

def write_json(path, value):
    Path(path).write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')

def preserve(path, data):
    p = Path(path)
    if p.exists():
        assert p.read_bytes() == data, f'Exact preservation mismatch: {path}'
    else:
        p.write_bytes(data)

original = Path('input.json').read_bytes()
input_value = json.loads(original.decode('utf-8'))
preserve('input-original.json', original)
preserve('task-original.json', (json.dumps(input_value['task'], ensure_ascii=False, indent=2)+'\n').encode())
preserve('assignment-original.txt', input_value['assignment'].encode('utf-8'))
assert input_value['notes'] == []
catalogue = json.loads(Path('source-catalogue.json').read_text())
for directory in ['sources', 'source-extracts', 'granted', 'logs']:
    Path(directory).mkdir(exist_ok=True)

source_records = []
for source in catalogue['sources']:
    for entry in source['files']:
        local = Path(entry['local_copy'])
        if not local.exists():
            # This is the exact authorized primary path in the supplied catalogue.
            local.write_bytes(Path(entry['authorized_path']).read_bytes())
        data = local.read_bytes()
        assert digest(data) == entry['expected_sha256'], str(local)
        source_records.append({'source': source['id'], 'version': source['version'],
          'url': source['public_source'], 'file': str(local), 'sha256': digest(data),
          'bytes': len(data), 'authorized_path': entry['authorized_path']})

units = []
def make_unit(uid, source, a, b, description, read_status='Retained complete pertinent unit; not a recursively complete source audit.'):
    p = Path(f'sources/{source}-literal_extract.txt')
    data = p.read_bytes()
    lines = data.decode('utf-8').split('\n')
    assert 1 <= a <= b <= len(lines)
    literal = '\n'.join(lines[a-1:b])
    artifact = f'source-extracts/{uid}-{source}-{a}-{b}.txt'
    Path(artifact).write_bytes(literal.encode('utf-8'))
    s = next(x for x in catalogue['sources'] if x['id']==source)
    rec={'id':uid,'source':source,'version':s['version'],'url':s['public_source'],
      'source_file':str(p),'source_text_sha256':digest(data),'inclusive_LF':[a,b],
      'coordinate_rule':"UTF-8 bytes decode; split('\\n'); inclusive one-based",
      'literal':literal,'sha256':digest(literal.encode()),'artifact':artifact,
      'description':description,'reading_limit':read_status}
    units.append(rec)
    return uid

for supplied in catalogue['units']:
    a,b=supplied['inclusive_LF']
    uid=make_unit(supplied['id'],supplied['source'],a,b,supplied['application'],
                  'Catalogue unit retained exactly; retention is not a claim of independent full reading or proof validation.')
    assert units[-1]['literal']==supplied['literal']
    assert units[-1]['sha256']==supplied['sha256']
    assert units[-1]['source_text_sha256']==supplied['source_text_sha256']

extra = {
 'x00':('S1',435,469,'Standing reduced-variety conventions'),
 'x01':('S1',886,900,'Actual canonical metric and section evaluation'),
 'x02':('S1',962,1030,'PL vector lattice, density, and proof'),
 'x03':('S1',1390,1464,'Actual FS/model bundle identification and pertinent proof'),
 'x04':('S1',1692,1729,'Same actual bundle inclusion and PL uniform approximation proof'),
 'x05':('S1',2170,2368,'Genuine definitions, varying-class closure, flattening, pullback and full proof'),
 'x06':('S1',2418,2468,'Genuine approximation and continuous fixed-class closure; complete proofs'),
 'x07':('S1',2494,2541,'Divisorial determination and continuity; full pertinent proofs'),
 'x08':('S1',2754,2887,'General-projective EP equivalence, compactness, and conditional birational onto; proofs'),
 'x09':('S1',2894,2976,'Continuity of envelopes and full pertinent proof'),
 'x10':('S1',2978,3064,'Smooth connected nef EP, compactness, and complete pertinent proof'),
 'x11':('S1',3649,3889,'General-projective extended energy, finite-energy cone and full pertinent proofs'),
 'x12':('S1',3890,4135,'Signed multilinear pairing, genuine raw operator and weighted convergence; proofs'),
 'x13':('S1',4165,4340,'Finite-energy inequalities, strict concavity and scaling; proofs'),
 'x14':('S1',4529,4602,'Unbounded locality and comparison; complete pertinent proofs'),
 'x15':('S1',4674,4962,'Extended and outer energy, uniform derivatives, relative-volume inputs; entire pertinent proofs'),
 'x16':('S1',4970,5035,'Intrinsic dual energy definition and model-test formula; proof'),
 'x17':('S1',5110,5158,'USC duality and both PL variation signs; complete proofs'),
 'x18':('S1',5180,5301,'Bounded-J, target integral continuity, integrability criterion; complete proofs'),
 'x19':('S1',5426,5477,'General equidimensional uniqueness and domination; proofs'),
 'x20':('S1',6092,6146,'Actual general-variety Calabi-Yau theorem and full proof; smooth corollary distinguished'),
 'x21':('S1',6302,6359,'Explicit EP hypothesis and orthogonality theorem; full proof'),
 'x22':('S7',2358,2379,'Actual semiample FS smoothing and full proof'),
 'x23':('S7',2611,2779,'Raw fundamental cycles, continuous measures and base change; full pertinent proofs'),
 'x24':('S7',3125,3202,'Model Deligne pairing induction and cycle multiplicities; complete proofs'),
 'x25':('S2',2697,2755,'New envelope source entire proof; diagnostic only, not an envelope premise'),
}
for uid,(src,a,b,description) in extra.items(): make_unit(uid,src,a,b,description)

# Preserve retrieved Temkin primary transcript; never label it original PDF bytes.
response_files=['temkin_web.json','temkin_find.json','primary_web_0.json']
web_lines={}
for name in response_files:
    value=json.loads(Path('source-extracts',name).read_text())
    if value.get('status')=='fulfilled': value=value['value']
    for item in value.get('content',[]):
        if item.get('type')!='text': continue
        for line in item['text'].split('\n'):
            m=re.match(r'L(\d+)@[^:]+: (.*)',line)
            if m:
                number=int(m.group(1))
                # Multiple source renderings of the same exact public version.
                if number not in web_lines: web_lines[number]=line
transcript='\n'.join(web_lines.get(i,f'L{i}: [not retrieved]') for i in range(2076))
Path('sources/Temkin-v2-rendered-transcript.txt').write_bytes(transcript.encode())
for uid,a,b,desc in [('t00',82,91,'Exact resolution statement'),
 ('t01',421,433,'Finite blowup-sequence definition'),
 ('t02',1526,1551,'Stabilization lemma and proof'),
 ('t03',1693,1886,'Entire pertinent main-theorem proof, including Cartier pullback proof')]:
    assert all(i in web_lines for i in range(a,b+1)),(uid,'incomplete primary retrieval')
    # Native renderer labels start at zero; our saved LF coordinates start at one.
    literal='\n'.join(transcript.split('\n')[a:b+1])
    artifact=f'source-extracts/{uid}-Temkin-rendered-{a+1}-{b+1}.txt'
    Path(artifact).write_bytes(literal.encode())
    units.append({'id':uid,'source':'Temkin','version':'0904.1592v2 (11 December 2011)',
     'url':'https://arxiv.org/pdf/0904.1592v2','source_file':'sources/Temkin-v2-rendered-transcript.txt',
     'source_text_sha256':digest(transcript.encode()),'inclusive_LF':[a+1,b+1],
     'renderer_zero_based_labels':[a,b],'coordinate_rule':"UTF-8 bytes decode; split('\\n'); inclusive one-based on saved rendered transcript, NOT original PDF",
     'literal':literal,'sha256':digest(literal.encode()),'artifact':artifact,'description':desc,
     'reading_limit':'Complete pertinent retrieved unit read; earlier recursively cited algorithms not reconstructed. Original PDF bytes were not downloaded; its checksum is not asserted.'})

def premise(index, statement, ids, quote):
    evidence=[]
    for uid in ids:
        unit=next(x for x in units if x['id']==uid)
        evidence.append({'unit':uid,'url':unit['url'],'version':unit['version'],
         'source_text_sha256':unit['source_text_sha256'],'inclusive_LF':unit['inclusive_LF'],
         'literal':unit['literal'],'sha256':unit['sha256'],'artifact':unit['artifact']})
    assert evidence and all(e['url'].startswith('https://') for e in evidence)
    return {'index':index,'statement':statement,'passages':evidence,'short_pertinent_quote':quote,
     'kind':'External primary mathematical premise; not a native registered support.'}

premises=[
premise(0,'For every Noetherian quasi-excellent generically reduced scheme X over Spec(Q), Temkin 0904.1592v2 Theorem 1.2.1 supplies a finite blowup sequence with regular final scheme, regular centers disjoint from the preimages of the original regular locus, and the stated regular-morphism functoriality. A sequence means a finite composition; the pertinent construction and its stabilization are those in Section 4.3.', ['t00','t01','t02','t03'],'For any noetherian quasi-excellent generically reduced scheme'),
premise(1,'BJ 1801.08229v4 works over algebraically closed trivially valued fields with reduced projective varieties, permitting nonnormal, reducible and unequal-dimensional varieties. Canonical section evaluation at valuation-ring centers gives norms in [0,1] and the trivial reference metric. Rational PL functions form a vector lattice uniformly dense in C0(Xan).', ['x00','x01','x02'],'is reduced, but not necessarily irreducible, nor even equidimensional'),
premise(2,'For an actual ample rational bundle L on a reduced projective variety over an algebraically closed trivially valued field, BJ 2.18, 2.31 and 3.9 identify finite FS potentials with actual same-bundle model metrics, with Hdom(c1(L)) contained in H(L). BJ 3.10 uniformly approximates any genuine PL_R potential in an ample class by Hdom of that class.', ['x03','x04'],'Hdom (L) := Hdom (c1 (L)) ⊂ H(L)'),
premise(3,'On a reduced projective variety over an algebraically closed trivially valued field, BJ 4.3, 4.5-4.7 give zero in every nef psh class, positive addition and scaling, maxima, constants, uniform closure, decreasing varying-class closure for generically finite limits, and genuine pullback when the pullback is generically finite. BJ 4.15-4.16 give decreasing Hdom nets in ample classes and uniform fixed-class approximation of continuous psh potentials, without EP.', ['x05','x06'],'Theorem 4.7.'),
premise(4,'On a reduced projective variety over an algebraically closed trivially valued field, a genuine theta-psh potential is ordered below any USC scalar exactly when that order holds at all BJ divisorial valuations (4.22); for fixed continuous psi, sup(phi-psi) is continuous in the divisorial topology (4.28).', ['x07'],'Theorem 4.22.'),
premise(5,'For an irreducible projective variety over an algebraically closed trivially valued field, BJ 5.11 equates EP with compactness of normalized genuine PSH in the divisorial topology. For ample omega, 5.17 equates EP with continuity of envelopes of every finite continuous obstacle, and the envelope is genuine under EP; envelopes satisfy the sup-norm Lipschitz estimate.', ['x08','x09'],'Theorem 5.11.'),
premise(6,'For a smooth connected projective variety over an algebraically closed trivially valued characteristic-zero field, every nef class has EP and normalized PSH is compact (BJ 5.20-5.21). No ampleness or countability of the nef source class is required.', ['x10'],'Then any θ ∈ Nef(X) has the envelope property.'),
premise(7,'For a projective birational morphism pi:Y->X of projective varieties over an algebraically closed trivially valued field, if theta is approached by target classes theta_m having EP with theta_m-theta ample, BJ 5.13 gives an onto homeomorphic genuine psh pullback at theta. This premise is used only after original-target approaching EP.', ['x08'],'Lemma 5.13.'),
premise(8,'For a reduced projective variety over an algebraically closed trivially valued field and ample numerical classes, BJ 7.1-7.2 extend the actual symmetric intersection pairing by infima of genuine finite Hdom majorants, weakly USC and decreasing-net continuous. BJ 7.7-7.8 give concave translation-equivariant energy, the genuine finite-energy cone, mixed finiteness and normalization energy compatibility. These statements do not require smoothness or EP.', ['x11'],'In this section, X denotes a projective variety'),
premise(9,'For a reduced projective variety over an algebraically closed trivially valued field, BJ 7.14 and 7.18-7.21 extend the signed finite-energy pairing, construct positive genuine mixed Radon measures for genuine nef entries, give their raw intersection mass and model formula with ord_E(t), normalization pushforward, integrability of finite-energy tests, unbounded genuine decreasing-net continuity, and weighted continuity when the limiting psh test is integrable. The defining weighted integral is test-containing pairing minus zero-test pairing.', ['x12'],'Theorem 7.18.'),
premise(10,'For a reduced projective variety over an algebraically closed trivially valued field and ample omega, BJ 8.2-8.8 define outer energy, continuous on decreasing USC nets and equal to genuine energy on psh; under EP it equals energy of the genuine envelope. For fixed real PL f, its expansion at any actual E1 potential is E_down(phi+tf)=E(phi)+t integral(f MA_BJ(phi))+O(t^2), uniformly in phi. Both signed continuous directions follow by uniform PL approximation. No smoothness hypothesis enters these global derivative theorems.', ['x15'],'where the implicit constant in the O is uniform with respect to ϕ.'),
premise(11,'For a reduced projective variety over an algebraically closed trivially valued field and ample omega, BJ 9.1 defines intrinsic dual energy on probability Radon measures by the supremum over genuine E1. BJ 9.9 gives USC outer-energy duality, and 9.11-9.12 identify a genuinely attained E1 maximizer with its actual Monge-Ampere equation, using f and -f and PL density. No inverse-support operator or EP is assumed in this identification.', ['x16','x17'],'and replacing f with −f yields the result.'),
premise(12,'On an irreducible projective variety over an algebraically closed trivially valued field, BJ 9.15-9.16 bound J on dual maximizing nets, and 9.19 gives target L1 convergence for weakly convergent genuine psh nets with eventually bounded J against every finite-dual-energy target. BJ 9.20 says finite intrinsic dual energy is equivalent to integrability of all actual E1 potentials. General finite-energy concavity, I/J and scaling estimates used here are those of 7.28-7.33. No smoothness or support condition is imposed.', ['x13','x18'],'A Radon probability measure µ ∈ M has finite energy iff E 1 ⊂ L1 (µ).'),
premise(13,'On a reduced projective variety over an algebraically closed trivially valued field with ample omega, BJ 7.40-7.44 give genuine unbounded E1 strict-winning Borel locality, mixed open locality and comparison. On an equidimensional projective variety, 10.3-10.6 give equality of genuine MA iff I=0 iff the potential difference is locally constant, and domination of a psh potential by an E1 potential when the inequality holds almost everywhere for its MA. These theorems require neither smoothness nor EP; irreducibility makes the difference one constant.', ['x14','x19'],'Corollary 10.6 (Domination principle).'),
premise(14,'For a reduced projective variety over an algebraically closed trivially valued field and ample omega, BJ 12.8 says EP is equivalent to surjectivity of the genuine E1 Monge-Ampere operator onto all intrinsic finite-dual-energy probability Radon measures. Its EP-to-surjectivity proof obtains an actual normalized psh subnet limit using general EP compactness, bounded J, target integral continuity and energy USC to attain the variational supremum. The smooth 12.9 corollary is a separate statement.', ['x20'],'This proves (i)⇒(ii).'),
premise(15,'For an irreducible projective variety over an algebraically closed trivially valued field, ample omega with EP, and a finite continuous obstacle f, BJ 13.1 gives genuine continuous envelope p and integral((f-p) MA_BJ(p))=0. Its continuous proof uses P(p+t(f-p))=p and the continuous energy derivative. EP is a stated hypothesis.', ['x21'],'and we assume that the envelope property holds for ω'),
premise(16,'For a projective scheme of dimension n over a complete valued field and actual rational semiample bundles, BE 1805.01016v3 7.14 makes FS-limit metrics psh-regularizable on the same bundles. Its 8.3-8.5 construct positive continuous mixed Radon measures of raw fundamental-cycle intersection mass, uniform continuity and complete-field pushforward. The full fundamental cycle includes generic lengths. BE 8.18-8.21 identify model Deligne pairing and vertical intersections, including the zero-dimensional induction and relatively regular section proof. BJ 7.23 identifies this continuous operator with its energy-pairing operator.', ['x22','x23','x24','x12'],'for any complete field extension F/K'),
]
assert [p['index'] for p in premises]==list(range(len(premises)))
write_json('external-premises.json',{'coordinate_rule':"UTF-8 bytes decode; split('\\n'); inclusive one-based",'premises':premises,
 'limits':'Every top-level external premise is indexed and has exact HTTP(S) primary statement/proof evidence. Recursive inputs wholly inside task-granted accepted proofs retain their exact scope as grants, not invented external premises. Source-byte checks do not validate applications.'})
write_json('source-provenance.json',{'sources':source_records,'units':units,
 'temkin_pdf_download':{'url':'https://arxiv.org/pdf/0904.1592v2','command':['curl','--fail','--location','--max-time','25','--output','sources/Temkin-0904.1592v2.pdf','https://arxiv.org/pdf/0904.1592v2'],
 'observed_exit_code':7,'observed_failure':'Failed to connect to proxy port 8080; no original PDF bytes or verified local PDF checksum obtained.',
 'substitute':'Exact version-pinned primary rendered response observations, saved verbatim, with separate transcript/unit hashes.'},
 'epistemic_limit':'Exact retention and compilation are observations. The new applications remain unverified mathematical drafts.'})

write_json('reading-limits.json',{
 'rule':'A retained complete unit is not automatically fully read. Listed readings include proofs where stated; no recursively complete audit is claimed.',
 'independent_reading':{
 'S1':[[435,469],[886,900],[1596,1735],[2220,2368],[2418,2468],[2494,2541],[2754,2889],[2889,2929],[2978,3061],[3649,3935],[3930,4137],[4303,4420],[4500,4650],[4750,5000],[5110,5313],[5375,5508],[6050,6164],[6302,6374]],
 'S7':[[2358,2390],[2390,2440],[2611,2779],[3125,3202]],
 'S2':[[2697,2755]],
 'Temkin_rendered_zero_based':[[82,91],[421,433],[1526,1551],[1693,1886]],
 'granted_complete_mathematical_inputs':['supplied-07.txt','supplied-08.txt','supplied-11.txt','supplied-14.txt','supplied-15.txt','supplied-18.txt (mathematical chain LF12-316)','supplied-19.txt']},
 'partial_limits':'Some initial larger output was truncated; decisive energy, derivative, comparison, attainment and accepted-body segments were reread separately. S3-S6 and S8-S10 catalogue units were preserved and their exact supplied statements used within the compact-contact grant; whole source files were not independently read. BJ FS/density and some longer theorem groups are preserved as complete units while the current independent reading is partial, with the accepted fixed-reference/general-theory grants supplying their proved deductions. Temkin earlier algorithm construction and recursive curve/model/volume background are not newly reconstructed.'})

commands=[]
def run(argv, log_name):
    result=subprocess.run(argv,stdout=subprocess.PIPE,stderr=subprocess.PIPE,check=False)
    Path('logs',log_name+'.stdout.log').write_bytes(result.stdout)
    Path('logs',log_name+'.stderr.log').write_bytes(result.stderr)
    commands.append({'argv':argv,'cwd':str(ROOT),'exit_code':result.returncode,
      'stdout':'logs/'+log_name+'.stdout.log','stderr':'logs/'+log_name+'.stderr.log'})
    assert result.returncode==0, f'{argv[0]} failed; inspect logs/{log_name}.*.log'
    return result

environment={'platform':platform.platform(),'python':sys.version,'python_executable':sys.executable,
 'cwd':str(ROOT),'tools':{},'network_failure':'Shell proxy connection unavailable; read-only primary web tool returned public version-pinned passages.',
 'compute':'No resource-heavy computation performed; no operator supervised compute service exposed.',
 'models_and_workers':'One native configured Codex session only; no subagents or model-switch tools called. No independent verification of host model identity is asserted.'}
for tool in ['pandoc','pdflatex','pdftex','pdftotext']:
    binary=shutil.which(tool)
    environment['tools'][tool]={'path':binary}
    if binary:
        result=run([binary,'-v' if tool=='pdftotext' else '--version'],tool+'-version')
        version_bytes=result.stdout or result.stderr
        environment['tools'][tool]['version']=version_bytes.decode('utf-8',errors='replace').split('\n')[:3]
assert environment['tools']['pandoc']['path'] and environment['tools']['pdflatex']['path'], 'Existing tools are required; do not install replacements.'
run([environment['tools']['pandoc']['path'],'argument.md','--standalone','--from=markdown+tex_math_dollars','--to=latex','--output=P16.1-paper.tex'], 'pandoc-compile')
tex=Path('P16.1-paper.tex').read_text()
# Permit line breaking of literal hash identifiers without changing their characters.
tex=re.sub(r'\\texttt\{([0-9a-f]{64})\}',lambda m:'\\texttt{'+r'\allowbreak{}'.join(m[1][i:i+8] for i in range(0,64,8))+'}',tex)
Path('P16.1-paper.tex').write_text(tex)
for number in [1,2]:
    run([environment['tools']['pdflatex']['path'],'-interaction=nonstopmode','-halt-on-error','-file-line-error','P16.1-paper.tex'],f'pdflatex-pass-{number}')
    shutil.copyfile('P16.1-paper.log',f'logs/pdflatex-pass-{number}.tex.log')
run([environment['tools']['pdftotext']['path'],'-layout','P16.1-paper.pdf','P16.1-paper-pdf-text.txt'],'pdf-extraction')
write_json('environment.json',environment)
write_json('commands.json',commands)

# Note registration is supplied by this fresh run; grants have no native handles.
note_file=Path('canonical-notes.json')
if note_file.exists():
    note_value=json.loads(note_file.read_text())
    assert len(note_value['notes'])<=4
    seen=set()
    for note in note_value['notes']:
        assert note['id'] not in seen
        assert set(note['support'])<=seen, 'Support must be registered earlier local notes only.'
        seen.add(note['id'])
    assert note_value['notes'][-1]['id']=='n4' if note_value['candidate'] else True

status={'id':'P16.1-original-retained-domain','status':'complete-proof-draft',
 'exact_result':'The original reduced irreducible geometrically unibranch projective domain over every algebraically closed trivially valued characteristic-zero field, without countability, with actual ample rational L, genuine E1 raw MA of mass (L^n), every finite-intrinsic-dual-energy positive Radon target of that mass, arbitrary support, an attained variational solution and uniqueness modulo constants; proved relative only to the supplied exact task-granted accepted intermediate mathematical bodies.',
 'proof_file':'argument.md','concrete_gaps':[]}
assert set(status)=={'id','status','exact_result','proof_file','concrete_gaps'}
write_json('status.json',status)

write_json('checks.json',{'input_original_sha256':digest(original),'exact_input_preserved':True,
 'exact_task_value_preserved':json.loads(Path('task-original.json').read_text())==input_value['task'],
 'exact_assignment_bytes_preserved':Path('assignment-original.txt').read_bytes()==input_value['assignment'].encode(),
 'primary_files_verified':len(source_records),'literal_supplied_units_verified':len(catalogue['units']),
 'additional_complete_units_retained':len(extra)+4,'external_premise_indices':list(range(len(premises))),
 'compile_results':[c['exit_code'] for c in commands if 'pdflatex-pass' in c.get('stdout','')],
 'proof_rules':'No finite computation proves the infinite-domain theorem. These are preservation, provenance, schema, support and compile observations only.',
 'canonical_notes_registered':note_file.exists(),'candidate_means':'Complete mathematical proof draft relative to exact supplied accepted grants; not independent verification.'})
run_result={'primary_files':len(source_records),'supplied_units':len(catalogue['units']),
 'external_premises':len(premises),'pdf_bytes':Path('P16.1-paper.pdf').stat().st_size,
 'compile_exit_codes':[c['exit_code'] for c in commands if 'pdflatex-pass' in c.get('stdout','')],
 'mathematical_verification':'unverified proof draft'}
write_json('run-result.json',run_result)
artifacts={}
for p in sorted(ROOT.rglob('*')):
    if p.is_file() and p.name!='artifact-hashes.json':
        artifacts[str(p.relative_to(ROOT))]={'sha256':digest(p.read_bytes()),'bytes':p.stat().st_size}
write_json('artifact-hashes.json',artifacts)
print(json.dumps(run_result,ensure_ascii=False))
