#!/usr/bin/env python3
"""Bind the exact used premises to preserved literal bodies, not other workers."""
import hashlib,json,pathlib,re
ROOT=pathlib.Path(__file__).resolve().parent
def sha(p): return hashlib.sha256((ROOT/p).read_bytes()).hexdigest()
units=json.loads((ROOT/'primary-units/manifest.json').read_text())
dictionary=json.loads((ROOT/'primary-dictionary/manifest.json').read_text())
def unit(i):
    r=units[i]; p=r['artifact']; m=r['supplied_metadata']
    return {'artifact':p,'sha256':sha(p),'local_inclusive_LF':[1,len((ROOT/p).read_text().split('\n'))],
            'literal_supplied_coordinates':{k:v for k,v in m.items() if k in
             ['inclusive_LF','inclusive_one_based_LF','inclusive_renderer_lines','coordinate_rule',
              'version','url','source_sha256','source_text_sha256','sha256','source_text_sha256_status']},
            'supplied_metadata_preserved_in':'primary-units/manifest.json',
            'full_source_bytes_independently_available':False}
def dunit(i):
    r=dictionary[i];p=r['artifact']
    return {'artifact':p,'sha256':sha(p),'local_inclusive_LF':[1,len((ROOT/p).read_text().split('\n'))],
            'literal_supplied_binding':r['binding'],
            'binding_matches_preserved_body':r['binding_matches_preserved_body'],
            'original_source_LF':'not supplied for this dictionary record; not invented',
            'full_source_bytes_independently_available':False}
def public_piece(source,artifact,a,b,url):
    r=json.loads((ROOT/source).read_text()); t='\n'.join(c.get('text','') for c in r['content'])
    lines=[]
    for s in t.splitlines():
        m=re.match(r'L(\d+)(?:@[^:]+)?:',s)
        if m and a<=int(m.group(1))<=b: lines.append(s)
    assert len(lines)==b-a+1,(artifact,len(lines),a,b)
    p=ROOT/artifact;p.parent.mkdir(exist_ok=True);p.write_text('\n'.join(lines)+'\n')
    return {'artifact':artifact,'sha256':sha(artifact),'local_inclusive_LF':[1,len(lines)],
            'literal_renderer_coordinates':[a,b],'coordinate_rule':'zero-based inclusive literal renderer labels',
            'url':url,'version':'public primary page retrieved 5 October 2026; immutable response saved',
            'response_artifact':source,'response_sha256':sha(source),'binary_source_hash':None}
pub=[public_piece('public-primary/associated-primes-response.json','public-primary/associated-primes-body.txt',20,61,
                   'https://stacks.math.columbia.edu/tag/00L9'),
     public_piece('public-primary/prime-filtration-response.json','public-primary/prime-filtration-body.txt',22,30,
                   'https://stacks.math.columbia.edu/tag/00L0')]
records=[]
def add(i,statement,url,version,u=(),d=(),extra=()):
    records.append({'id':f'E{i}','statement':statement,'url':url,'version':version,
                    'pertinent_statement_and_proof_bodies':[unit(j) for j in u]+[dunit(j) for j in d]+list(extra),
                    'read_scope':'complete pertinent mathematical statement/proof units; no full-source or recursively complete proof-reading claim',
                    'mathematical_role':'external published premise; documentary hashes do not prove it'})
BJ='https://arxiv.org/pdf/1801.08229v4'; BJv='arXiv:1801.08229v4, March 2022'
add(0,'On projective varieties over algebraically closed trivially valued fields, BJ Definition 4.1 and Theorems 4.5, 4.7, 4.15 define genuine generically finite psh cones from varying-class FS limits, prove genuine decreasing varying-class closure, positive sums/scaling, constants in nef classes, finite maxima, and the stated finite approximations. For the actual ample A, fixed-bundle conversion is supplied in G0. No energy construction for a nonample class is part of this premise.',BJ,BJv,u=[0,2],d=[51,52])
add(1,'BJ 4.12 and 4.22--4.25: on projective varieties, genuine psh potentials have the stated maximum principle, are finite divisorially, and an inequality from a genuine psh function to an usc obstacle holds everywhere iff it holds divisorially. Genuine functions are divisorially determined. On connected X the zero numerical class psh cone is precisely the finite constants.',BJ,BJv,u=[3,4])
add(2,'BJ 6.15--6.17 and 6.23--6.25: genuine homogeneous psh functions have decreasing homogeneous FS approximation in varying rational classes tending to the given class; each genuine psh function has its pointwise homogeneous Legendre decomposition on every analytic point. No divided-net monotonicity conclusion is included.',BJ,BJv,u=[8,10])
add(3,'BJ 2.23: on normal projective X, a generically finite FS function on an actual Q-line bundle dominated up to a constant by an effective Q-Cartier divisor potential admits actual section division and a genuine FS quotient in the actual subtracted bundle.',BJ,BJv,u=[1])
add(4,'BJ 5.6 and 5.11: divisorial points are nonnegligible, so usc regularization of bounded-above genuine psh suprema changes no divisorial value. For irreducible projective X, EP is equivalent to normalized genuine psh compactness in the divisorial topology. Here normalized ample compactness itself is also G0.',BJ,BJv,u=[7,28])
add(5,'BJ+ Theorem A and Corollaries 2.1--2.3: if X is smooth irreducible projective over algebraically closed trivial k and char(k)=0 or dim(X)<=2, every numerical class has EP; PSH(theta) is nonempty exactly for pseudoeffective theta, its V_theta=P_theta(0) is genuine, normalized PSH(theta) is compact, and Siu division holds for effective Q-Cartier divisors. Theorem B still assumes ample omega and is excluded as a nonample energy premise. Only characteristic zero is retained here.',
    'https://arxiv.org/pdf/2206.07183v2','arXiv:2206.07183v2; submission 6 September 2023; PDF date 7 September 2023',u=[24,25,26,27])
add(6,'BJ 4.36, 5.3 and 13.2: on projective varieties, proper algebraic closed subsets are pluripolar, pluripolar sets are negligible, and under the standing ample envelope property every finite-dual-energy positive probability measure assigns zero mass to negligible Borel sets. Output finite dual energy and arbitrary retained field cardinality are supplied in G0; no inverse equation is required for the zero-mass lemma.',BJ,BJv,u=[5,6,12])
add(7,'BE 7.14 gives decreasing smooth semipositive regularization for psh metrics on actual semiample Q-line bundles on geometrically reduced projective schemes over complete non-Archimedean fields, including trivial fields. BE 8.3--8.5 give original-fundamental-cycle mixed smooth measures, raw intersection mass and their unique uniform-to-weak extension for continuous psh-regularizable metrics on projective schemes. BE 8.18 proves model Deligne-pairing compatibility, and BJ 7.23 identifies the continuous BJ operator with the local metric product. BE 7.8 assumes nontrivial valuation and is not used.',
    'https://arxiv.org/pdf/1805.01016v3','arXiv:1805.01016v3',u=[14,15],d=[14,37])
add(8,'CLD 18.1.2 and 18.1.6 on boundaryless analytic spaces: the curvature in an invertible local frame is dd^c(-log norm(frame)); logarithms of analytic units are smooth harmonic, and the local Poincare--Lelong proof gives the corresponding frame identity. CLD 8.8.5 proves harmonic-addition invariance for continuous local dpsh products with a positive closed current. These are continuous/local premises; no arbitrary unbounded nonample product is assumed.',
    'https://arxiv.org/pdf/1204.6277v2','arXiv:1204.6277v2',u=[17,19])
add(9,'Stacks Proposition 28.27.13(7), Lemma 30.16.1(4) and Lemma 33.45.1: positive ample twists globally generate finite-type quasi-coherent sheaves on quasi-compact quasi-separated schemes; on proper Noetherian schemes over a Noetherian affine base ample twists of coherent sheaves have vanishing higher cohomology for all sufficiently large powers; on a proper scheme over a field Euler characteristic of invertible twists of a coherent sheaf is a numerical polynomial of total degree at most its support dimension. These apply to the nonreduced projective Cartier scheme H. Bigness growth is the definition stated in paper (2.1).',
    'https://stacks.math.columbia.edu/tag/01Q3','supplied primary page bodies retrieved 5 October 2026; tags 01Q3, 0B5T, 0BEM',u=[20,21,22])
add(10,'Stacks 10.63.9 (00LD): over a Noetherian ring, zero divisors on a module are exactly the union of its associated primes. Stacks 10.63.5 and 10.62.1 imply finitely many associated primes for a finite module. On a Noetherian scheme a line-bundle section is regular iff it does not vanish at associated points (31.16.1, 0B3Q). Its printed proof is omitted; paper Section 3 supplies its reduction to the primary zero-divisor proof. Finiteness extends over a finite affine cover of a coherent sheaf.',
    'https://stacks.math.columbia.edu/tag/00LD','public primary responses retrieved 5 October 2026; supplied 0B3Q body same date',u=[23],extra=pub)
grant={'id':'G0','status':'task-granted exact mathematical premise, not external publication or historical audit',
       'exact_domain':'Reduced irreducible geometrically unibranch projective varieties over every algebraically closed trivially valued characteristic-zero field, with an actual ample rational line bundle. Used here only on original smooth X with actual ample A.',
       'exact_result':'The full genuine actual-ample energy, mixed/raw operator, mass, decreasing/weighted limits, EP/compactness, comparison/domination, all continuous two-sided outer derivatives, intrinsic dual-energy criterion, coercivity/target L1 continuity, actual attained equation and uniqueness modulo constants stated in the supplied Theorem 1.',
       'complete_supplied_body':{'artifact':'preserved/block-00.md','sha256':sha('preserved/block-00.md')},
       'proof_source_dictionary':'primary-dictionary/manifest.json',
       'historical_audit':'preserved/block-01.json; documentary only',
       'excluded':'No big/nonample conclusion and no incomplete102 endpoint are granted.'}
ledger={'grant':grant,'external_premises':records,'new_proofs':'P16.5-paper.md Sections 3--11',
        'unused_supplied_notes':'All four historical block-04 notes are preserved as data. None is a logical support: their reused mathematical claims are proved again or bound to published primary bodies.',
        'binary_source_hash_policy':'Only preserved body/response hashes are computed. No arXiv binary was acquired or hashed. Supplied whole-source hash strings remain documentary supplied bindings.'}
(ROOT/'external-premises.json').write_text(json.dumps(ledger,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'external_premises':len(records),'task_grants':1,'public_primary_units':len(pub)}))
