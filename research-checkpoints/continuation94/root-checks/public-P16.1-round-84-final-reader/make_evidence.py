#!/usr/bin/env python3
"""Document primary inputs; LF coordinates always use bytes.decode().split('\n')."""
import hashlib, json, re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
OUT = ROOT / 'source-extracts'
OUT.mkdir(exist_ok=True)
# Only our generated literal units/snapshots are regenerated; primary inputs stay untouched.
for path in OUT.glob('e[0-9][0-9][0-9]-*.txt'): path.unlink()
for path in (ROOT/'sources').glob('web-e[0-9][0-9][0-9].txt'): path.unlink()
def sha(b): return hashlib.sha256(b).hexdigest()
def dump(path, x): (ROOT/path).write_text(json.dumps(x, ensure_ascii=False, indent=2)+'\n', encoding='utf8')
files = json.loads((ROOT/'source-files.json').read_text())
by_source = {x['source']:x for x in files if x['path'].endswith('literal_extract.txt')}
units, seen = [], {}

def local(source, first, last, use):
    rec=by_source[source]; path=ROOT/rec['path']; data=path.read_bytes()
    lines=data.decode('utf8').split('\n')
    assert 1<=first<=last<=len(lines)
    body='\n'.join(lines[first-1:last]); key=(rec['path'],first,last)
    if key in seen: return seen[key]
    uid=f'e{len(units)+1:03d}'; artifact=f'source-extracts/{uid}-{source}-{first}-{last}.txt'
    (ROOT/artifact).write_bytes(body.encode('utf8'))
    unit={'id':uid,'source':source,'version':rec['version'],'url':rec['url'],
          'source_file':rec['path'],'source_text_sha256':sha(data),
          'inclusive_LF':[first,last],'literal':body,'sha256':sha(body.encode('utf8')),
          'artifact':artifact,'application':use,'limit':'Literal primary input; combined application is an unverified draft.'}
    units.append(unit);seen[key]=uid;return uid

def web(filename, urlpart, use, required=None):
    obj=json.loads((ROOT/filename).read_bytes())
    text='\n'.join(c.get('text','') for c in obj.get('content',[]) if c.get('type')=='text')
    blocks=re.split(r'\n-{20,}\n',text)
    hits=[]
    for b in blocks:
        m=re.search(r'\((https?://[^\s)]+)\)',b)
        if not m or urlpart not in m.group(1): continue
        if required and required not in b: continue
        if not re.search(r'^L\d+(?:@P[^:]+)?:',b,re.M): continue
        hits.append(b)
    assert hits, (filename,urlpart,required)
    # Preserve every matching returned unit, not a paraphrase or reconstructed PDF.
    body='\n\n'.join(hits); url=re.search(r'\((https?://[^\s)]+)\)',hits[0]).group(1)
    key=(filename,urlpart,required)
    if key in seen:return seen[key]
    uid=f'e{len(units)+1:03d}'; sourcefile=f'sources/web-{uid}.txt'
    (ROOT/sourcefile).write_bytes(body.encode('utf8'))
    lines=body.encode('utf8').decode('utf8').split('\n')
    # Whole tool-returned statement/proof block is literal, including rendering labels.
    artifact=f'source-extracts/{uid}-web-1-{len(lines)}.txt'
    (ROOT/artifact).write_bytes(body.encode('utf8'))
    version=(re.search(r'(\d{4}\.\d{4,5}v\d+|alg-geom/\d+v\d+)',url) or [None])[0]
    if 'alg-geom/9508005' in url:
        version='alg-geom/9508005v2, 16 August 1995; exact abstract version history in evidence/versions-and-flat.json; introductory chapter only'
    if version is None:version='Public primary snapshot retrieved 2026-10-05; see rendered header and version evidence'
    units.append({'id':uid,'source':'public-primary','version':version,'url':url,
        'source_file':sourcefile,'source_text_sha256':sha(body.encode('utf8')),
        'inclusive_LF':[1,len(lines)],'literal':body,'sha256':sha(body.encode('utf8')),
        'artifact':artifact,'retrieval_file':filename,'application':use,
        'limit':'Hash and LF coordinates concern this exact web-rendered UTF8 snapshot, not downloaded PDF bytes. Any cross-referenced source theorem remains an external premise.'})
    seen[key]=uid;return uid

premises=[]; passages=[]
def add(statement, sections, loc=(), webs=(), limitation='Source theorem used within its stated hypotheses; no independent proof certificate.'):
    idx=len(premises); refs=[]
    for source,a,b,use in loc:refs.append(local(source,a,b,use))
    for args in webs: refs.append(web(*args))
    assert refs
    premises.append({'index':idx,'statement':statement,'used_in_sections':sections,'evidence_units':refs,'limit':limitation})
    for uid in refs:
        u=next(x for x in units if x['id']==uid)
        nonempty=[s for s in u['literal'].split('\n') if s.strip()]
        # A short exact quote locates a literal unit; it does not replace that unit.
        quote=next((s for s in nonempty if any(t in s for t in ['Theorem','Lemma','Proposition','Corollary','Definition','Fact'])),nonempty[0])
        passages.append({'id':f'p{idx}-{uid}','premise':idx,'statement':statement,'url':u['url'],
            'quote':quote[:160],'unit':uid,'inclusive_LF':u['inclusive_LF'],'coverage':'Full literal unit retained in provenance; quote is only a locator.'})

add('BJ uses reduced possibly nonnormal projective varieties over algebraically closed trivially valued fields. Definition 4.1 uses a decreasing net of generically finite FS functions on varying rational bundles, whose numerical classes converge; bounded limits have finite semiample approximants. Theorem 4.5 gives varying-class decreasing closure.',[1,3,7,10,12], [('S1',435,469,'General-variety conventions'),('S1',2173,2297,'Actual definition and flattening-of-nets proof')])
add('For a projective finite-presentation flat family and a finitely presented flat sheaf, Euler characteristics are locally constant; generic flatness and generic geometric integrality permit shrinking a finite-type integral field-of-definition base. These apply separately to a fixed curve and fixed line bundle.',[2,3],webs=[('evidence/stable-proof.json','tag/0B9T','Euler-characteristic constancy','Lemma 36.32.2'),('evidence/spread-proof.json','tag/052A','Generic flatness','Lemma'),('evidence/spread-proof.json','tag/0574','Geometrically reduced generic fiber spreads to dense open','37.26.4'),('evidence/irreducible-fibers.json','tag/0553','Geometrically irreducible generic fiber spreads to dense open','37.27.5')])
add('BE Lemma 4.5 supplies finite presentation for algebraic models over valuation rings. Proposition 5.13 extends a projective morphism on a flat schematic graph model and identifies pulled model metrics. Theorem 4.20 gives finite relative integral closure for nontrivially valued discretely valued or algebraically closed complete K, and reduced special fiber in the algebraically closed case; Remark 4.21 excludes arbitrary densely valued K.',[3], [('S7',1510,1565,'Model definition and finite presentation'),('S7',1710,1788,'Exact closure hypotheses and proof'),('S7',1930,1995,'Model metric pullback and graph proof')])
add('Temkin defines multipointed curves as flat finitely presented schemes with pure one-dimensional fibers. A multipointed curve over integral qcqs S with semistable generic fiber has a stable modification after generically etale alteration. Stable modification morphisms are projective. Proposition 4.5.1 proves the valuation-ring application for separably closed valued fields of finite height.',[3],webs=[('evidence/definitions-and-fibers.json','0707.3953','Exact curve definitions','L61@'),('evidence/stable-find.json','0707.3953','Existence theorem and finite-height case','Theorem 1.5'),('evidence/stable-proof.json','0707.3953','Projectivity and actual valuation-ring gluing proof','Theorem 1.1')])
add('BPR identifies semistable vertex sets and semistable formal models of a smooth proper curve over complete algebraically closed nontrivially valued K; enlarging finite type II vertex sets gives dominating refinements. This permits removal of loops while preserving the already constructed graph morphism.',[3],webs=[('evidence/bpr-refinement-unit.json','1404.0279','Formal-model refinement and full correspondence proof','Theorem 4.11'),('evidence/bpr-detail.json','1404.0279','Finite vertex refinements','Proposition 3.13'),('evidence/web1.json','1404.0279','Standing field hypotheses','algebraically closed')])
add('BE continuous psh-regularizable metrics on projective schemes define symmetric raw mixed Radon measures with fundamental-cycle multiplicities and intersection mass. Real PL/model metrics are dpsh, and reduced-special-fiber models give finite Shilov-support coefficients equal to component intersections. FS metrics admit smooth semipositive uniform regularization.',[4,9], [('S7',2360,2470,'PSH regularization on semiample bundles'),('S7',2629,2783,'Cycles, extension, dpsh, exact finite model support')])
add('Wanner assumes K algebraically closed, complete and nontrivially valued and works on smooth proper algebraic curves. Model curvature agrees with Thuillier ddc in 3.27-3.28. Theorem 4.7, with its proof, makes every finite continuous CLD-psh function on an ordinary open Thuillier-subharmonic.',[4,5], [('S5',123,173,'Standing field hypotheses'),('S5',735,821,'Model curvature identities'),('S5',1096,1622,'Full continuous-current converse proof')])
add('Thuillier 3.3.7 gives local Green functions zero on affinoid boundary with interior ddc=-delta and global proper-curve functions with ddc(g_xy)=delta_y-delta_x. Proposition 3.1.11 is the subharmonic maximum principle, and 3.1.12 is its harmonic comparison formulation.',[5], [('S6',3862,3905,'Maximum and comparison'),('S6',4800,4902,'Both Green signs and proofs')])
add('Stacks 0AY8: a proper map to normal integral S from reduced X, every generic point dominating, whose generic fiber has global functions equal to the generic field, has geometrically connected fibers and pushforward O=O. Stacks 0GIQ identifies finite normalization of an integral geometrically unibranch scheme as a universal homeomorphism.',[3,6],webs=[('evidence/web1.json','tag/0AY8','All six Stein-factor hypotheses and proof','Lemma'),('evidence/web1.json','tag/0GIQ','Normalization universal homeomorphism and proof','Lemma')])
add('Stacks Bertini 0FD6 gives smooth general hyperplane sections for the generated bundle and immersion hypotheses; 0FD9 gives connected ample divisors when depth at closed points is at least two. Characteristic-zero resolution by finite smooth-center blowups is used for projective components, retaining projectivity.',[1,6],webs=[('evidence/geometry.json','tag/0FD6','Bertini smoothness and proof','Lemma'),('evidence/geometry.json','tag/0FD9','Connected hyperplane sections and proof','Lemma'),('evidence/resolution-units.json','9508005','Bierstone-Milman resolution statement and precise scope','Theorem 1.6'),('evidence/resolution-bm.json','9508005','Resolution setting in introductory chapter','characteristic zero'),('evidence/versions-and-flat.json','9508005','Exact v2 version history and first-chapter limit','this version, v2')],limitation='Bierstone-Milman public alg-geom/9508005v2 is the introductory chapter, with theorem statement and explanation; the complete chapter-4 proof was not retrieved or reproved. This standard geometric theorem is an explicit external input, not task-granted unconditional witness construction.')
add('A complete real-valued field norm extends uniquely to algebraic extensions (Temkin Fact 2.2.2); an algebraic extension embeds over its base into an algebraically closed field (Stacks 09GU). Complete algebraically closed valued extensions are available for curve tests. BJ Remark 1.9 supplies a continuous section of analytic projection for non-Archimedean field extensions, hence surjectivity.',[3,6,9], [('S1',738,758,'Analytic projection section'),('S9',2127,2155,'Use of complete algebraically closed residue-field extensions')],webs=[('evidence/model-and-flat.json','Temkin-lecture-notes','Unique norm extension','Fact 2.2.2'),('evidence/finite-descent-units.json','tag/09GU','Embedding algebraic extensions','Lemma')])
add('BJ 4.3 identifies constant potentials in nef classes; Theorem 4.7 supplies finite maxima, sums, pullback and closure. PSH topology is pointwise convergence on the divisorial valuations; sup is continuous; 4.22 proves divisorial order. Corollary 12.18(ii), with its 12.16 proof, supplies a decreasing sequence of finite rational FS functions in varying ample bundles for an already genuine nef-class potential, independently of target EP. No same-bundle regularization on pi*L is asserted.',[6,7,10,12], [('S1',2224,2239,'Constants in nef classes'),('S1',2298,2351,'Basic PSH operations'),('S1',2481,2551,'Actual topology and divisorial order proof'),('S1',6228,6268,'Full varying-bundle countable regularization proof')])
add('BJ 5.11 equates EP with compactness of normalized PSH. Smooth connected characteristic-zero projective varieties have EP for every nef class by 5.20, and compact normalized PSH by 5.21. No birational onto statement is supplied before approaching target EP.',[7,13], [('S1',2810,2858,'Compactness equivalence with proof'),('S1',2977,3070,'Smooth nef EP proof and compactness')])
add('Finite-presentation schemes, morphisms and finite equality data descend along filtered affine qcqs inverse systems (Stacks 01ZM); finitely presented modules and vector bundles descend too (01ZR). Relative ampleness of a line bundle is fpqc local on the base (0D3C).', [2,8],webs=[('evidence/finite-descent-units.json','tag/01ZM','Finite schemes maps and equalities, full standard proof','Lemma'),('evidence/finite-descent-units.json','tag/01ZR','Modules and vector bundles','Lemma'),('evidence/versions-and-flat.json','tag/0D3C','Fpqc ampleness with proof','Lemma')])
add('Over a perfect field a normal variety is geometrically normal (Stacks 0BXT). Noetherian flat local depth and dimension formulas with regular fibers, and descent/ascent of regularity, apply to finite-type models under characteristic-zero field extension. BJ 1.13 and 1.15 characterize relative integral closure by vertical R1 and special-fiber S1, preserving the specified nonnormal generic fiber.',[8], [('S1',758,855,'Relative closure, vertical criterion and complete proof')],webs=[('evidence/stable-proof.json','tag/0BXT','Geometric normality','Lemma'),('evidence/versions-and-flat.json','tag/0337','Flat depth formula','Lemma'),('evidence/versions-and-flat.json','tag/031E','Flat regular-fiber regularity and dimension','Lemma'),('evidence/spread-proof.json','tag/00OF','Descent of regularity','Lemma')])
add('BJ 2.2 gives rational PL lattice density; Definition 3.8 and Example 3.9 identify Hdom(c1(L)) with actual ample models of L dominating the trivial model. Theorem 4.15(iii) supplies decreasing Hdom majorant NETS for every ample-class genuine potential, without needing EP.',[8,10], [('S1',938,1040,'PL density proof'),('S1',1692,1729,'Finite Hdom actual-bundle representation'),('S1',2408,2494,'Regularization theorem and full net proof')])
add('BE 8.3(iv) has raw complete-field pushforward invariance with the analytic fundamental cycle; 8.4-8.5 uniquely extend it under uniform metric convergence. BJ 4.16 provides uniform FS approximation of continuous genuine ample-class potentials, and 7.23 identifies the actual continuous measures with CLD/BE on general reduced projective X.',[9,10], [('S7',2629,2750,'Complete-field invariance proof and unique extension'),('S1',2425,2443,'Uniform FS approximation'),('S1',4125,4150,'Genuine continuous compatibility')])
add('BJ Theorem 13.1 orthogonality is conditional on EP and uses differentiation of genuine envelope energy; Corollary 10.6 is genuine finite-energy domination and does not require EP or an inverse Dirac equation.',[10,13], [('S1',6304,6372,'Orthogonality proof under explicit EP'),('S1',5442,5490,'Domination proof')])
add('BJ 5.17 equates ample EP with continuity/genuine membership of envelopes of all continuous obstacles; the envelope is supnorm-Lipschitz. Lemma 5.9 and Theorem 4.5 give approaching-class closure. These are applied after finite feasible-competitor bounds, not assumed on a singular target.',[10], [('S1',2781,2820,'Approaching EP lemma'),('S1',2905,2977,'Envelope continuity reformulation and Lipschitz estimates')])
add('BJ 5.13 gives birational pullback homeomorphism only when the TARGET class is the limit of strictly larger target classes with EP. It is used after target ample EP, with an explicit conductor/Rees blowup presentation of normalization.',[11], [('S1',2859,2876,'Exact target-side antecedent and proof')])
add('BJ 7.2 gives normalization pullback equality for mixed energy pairings. Theorem 7.18 and Proposition 7.19 define genuine signed mixed finite-energy Radon measures, positivity, raw intersection mass, actual central-cycle formula, decreasing continuity and normalization pushforward identity (7.18), on the general reduced projective variety.',[12,13], [('S1',3649,3745,'General scope and normalization pairing'),('S1',3970,4075,'Genuine operator, raw mass, cycle and normalization proofs')])
add('BJ energy is the normalized mixed pairing with denominator (n+1)V, extended by decreasing limits; E1 means energy greater than minus infinity. The strong E1 topology refines the weak topology by continuity of this energy, so equality of energy and common valuations transports both.',[12], [('S1',3800,3948,'Energy and finite-energy definitions and properties'),('S1',6073,6094,'Strong E1 topology')])
add('BJ 9.1 defines dual energy for probability measures. Theorem 9.20 on irreducible general X equates finite dual energy with integrability of every genuine E1 potential. Proposition 9.19 supplies L1 continuity on bounded-energy weakly compact sets.',[12,13], [('S1',4973,5060,'Dual energy definition'),('S1',5245,5301,'Integrability equivalence and L1 theorem proofs')])
add('BJ 8.3 identifies outer decreasing energy with envelope energy under EP; Theorem 8.5 gives the uniform PL-test derivative of genuine energy and Corollary 8.6 gives the continuous-test derivative, on general varieties.',[13], [('S1',4756,4966,'Outer energy and differentiation statement/proof')])
add('BJ Theorem 12.8 equates ample EP with onto genuine finite-energy MA on irreducible general X. Its proof uses actual compactness, bounded-energy control, integral continuity, energy usc, attainment and outer energy differentiation. No smooth-only corollary replaces it.',[13], [('S1',5131,5200,'Bounded-energy estimates'),('S1',6090,6246,'Actual equivalence and complete variational argument')])
add('BJ 7.40-7.44 gives genuine finite-energy winning-locus locality and comparison; Corollary 10.4 gives uniqueness modulo a real constant on irreducible X through actual E1 estimates and divisorial order, without EP.',[13], [('S1',4519,4610,'Finite-energy locality and comparison'),('S1',5412,5484,'Uniqueness and domination')])
add('Wu 2609.27610v1 envelope proof expressly invokes resolved-nef descent Proposition 2.24 and weak/global Theorem 6.5. Its printed result is not an independent proof or review of C1 and is not used as granted singular EP.',[13], [('S2',2697,2755,'Literal new envelope argument and cited gates')],limitation='Source audit only. The theorem is not imported as established singular EP.')

dump('premises.json',{'premises':premises,'passages':passages,'coverage':{'all_indices_nonnegative':all(p['premise']>=0 for p in passages),'covered_indices':sorted(set(p['premise'] for p in passages))},'conditional_hypotheses_not_external_premises':['C1-original countable weak-to-genuine global theorem'],'epistemic_status':'Unverified combined proof drafts. Literal retention, execution and hashes are documentary observations.'})
dump('source-extracts/source-provenance.json',{'coordinate_rule':"UTF8 bytes.decode('utf8').split('\\n'); inclusive one-based LF",'supplied_primary_files':files,'units':units,'premises':premises,'passages':passages})
# The argument appendix is concise; complete literal bodies remain separately pinned.
appendix=['\n## Primary premise index\n']
for p in premises:
    urls=list(dict.fromkeys(next(u['url'] for u in units if u['id']==uid) for uid in p['evidence_units']))
    appendix.append(f"**Premise {p['index']}.** {p['statement']} Source units: {', '.join(p['evidence_units'])}. "+'; '.join(f'[primary source]({url})' for url in urls)+f". Limit: {p['limit']}\n")
(ROOT/'primary-index.md').write_text('\n'.join(appendix),encoding='utf8')
print(json.dumps({'primary_files':len(files),'literal_units':len(units),'external_premises':len(premises),'passages':len(passages),'complete_index_coverage':len(set(p['premise'] for p in passages))==len(premises)}))
