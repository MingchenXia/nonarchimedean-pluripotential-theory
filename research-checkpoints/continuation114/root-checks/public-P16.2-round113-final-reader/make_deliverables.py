#!/usr/bin/env python3
"""Generate the precise premise register, status, and canonical draft notes."""
import hashlib
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent
BJ = 'https://arxiv.org/pdf/1801.08229v4'
BE = 'https://arxiv.org/pdf/1805.01016v3'
CLD = 'https://arxiv.org/pdf/1204.6277v2'
TEMKIN = 'https://arxiv.org/pdf/0904.1592v2'
WU = 'https://arxiv.org/pdf/2609.27610v1'


def dump(name, value):
    (ROOT/name).write_text(json.dumps(value, ensure_ascii=False, indent=2)+'\n')


def main():
    records = {u['id']: u for u in json.loads((ROOT/'evidence/units-index.json').read_text())}
    premises = []

    def add(identifier, kind, claim, scope, application, units=(), urls=(), extra=(), reading='Pertinent supplied printed statement/proof units checked; cited background proofs not all read.'):
        literals=[]
        for unit in units:
            record=records[unit]
            contents=(ROOT/record['file']).read_text()
            literals.append({
                'unit_id':unit, 'file':record['file'], 'sha256':record['sha256'],
                'local_inclusive_one_based_LF':[1,len(contents.splitlines())],
                'original_metadata':record['metadata'],
            })
        for filename in extra:
            p=ROOT/filename
            literals.append({
                'file':filename,'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),
                'local_inclusive_one_based_LF':[1,len(p.read_text().splitlines())],
                'original_coordinates':'Renderer coordinates retained literally when present; otherwise supplied packet.',
            })
        premises.append({
            'index':len(premises),'id':identifier,'kind':kind,'exact_premise':claim,
            'retained_scope':scope,'new_application_in_paper':application,
            'primary_urls':list(urls),'literal_evidence':literals,'reading_scope':reading,
            'whole_primary_work_read':False,'all_recursively_cited_proofs_read':False,
            'historical_paths_opened':False,
        })

    add('G0','sole task grant',
        'Exactly the supplied actual-ample equation theorem: genuine ample cones, divisorial principles, envelopes, compactness, energy, genuine mixed products with mass, weighted decreasing limits, comparison, dual-energy characterization, all continuous derivatives, attained equation and uniqueness.',
        'Algebraically closed trivially valued characteristic-zero field of arbitrary cardinality; geometrically unibranch integral projective variety; actual ample rational line bundle. Applied only on smooth projective Y and actual ample A or H.',
        'Sections 1, 2.2, 5--9. No nonample closure or new nonprojective local bridge is granted.',
        extra=['evidence/packet-00.txt'],reading='Exact supplied theorem body retained and read as the task grant, not independent certification of all its recursively cited premises.')
    add('Chow','published algebraic theorem',
        'Chow lemma gives a proper birational quasi-projective refinement of the proper integral carrier; a proper immersion into projective space is closed.',
        'Separated finite-type proper integral k-variety, no cardinality restriction.',
        'Section 3.1 takes the reduced closure of the common dense open and obtains integral projective Z.',
        ['existing42-32','existing42-33'],['https://stacks.math.columbia.edu/tag/0200','https://stacks.math.columbia.edu/tag/0201'])
    add('Temkin-resolution','published algebraic theorem',
        'Temkin v2 Theorem 1.2.1 gives a finite regular-final blowup sequence for Noetherian quasi-excellent generically reduced schemes over Spec(Q).',
        'A finite-type scheme over any characteristic-zero field is over Spec(Q); finite type over Q is not assumed.',
        'Section 3.1 applies this to projective integral Z; blowup charts stay integral and the finite composition stays projective.',
        ['additional-06','additional-07','additional-08','additional-09'],[TEMKIN],
        reading='The statement, finite-sequence definitions, stabilization lemma and pertinent main proof read. Earlier desingularization algorithms and all recursive proofs not read.')
    add('excellent-and-smooth','published algebraic theorems',
        'Fields and their finite-type algebras are excellent (07QW). On reduced locally algebraic schemes over a perfect field, regularity equals smoothness (0B8X).',
        'Finite type over any retained k; characteristic zero makes k perfect.',
        'Section 3.1 verifies the exact hypotheses of Temkin and regular-to-smooth conversion.',
        urls=['https://stacks.math.columbia.edu/tag/07QW','https://stacks.math.columbia.edu/tag/0B8X'],extra=['evidence/packet-16.txt'],
        reading='Both pertinent printed proofs read. The localization proof explicitly omitted in 07QU is not used; recursive algebra proofs not all read.')
    add('normal-birational-sections','published algebraic theorem',
        'For a proper morphism with normal integral base, reduced source whose generic components dominate, and generic H0 equal to the base function field, f_*O=O and geometric fibers are connected (0AY8).',
        'Y integral, X smooth normal integral, pi proper birational.',
        'Section 3.1 glues the actual pulled frames to prove the actual section identity for every original integral bundle.',
        ['existing42-34','additional-13'],['https://stacks.math.columbia.edu/tag/0AY8'])
    add('factoriality','published algebraic theorem',
        'Regular local rings are UFDs (0AG0), hence smooth X is locally factorial.',
        'Smooth integral original X over k.',
        'Section 3.2 turns the pushed hyperplane Weil divisor into an actual Cartier divisor; Section 5 uses normal section division separately.',
        urls=['https://stacks.math.columbia.edu/tag/0AG0'],extra=['evidence/public-stacks_new.txt'],reading='Newly retrieved primary statement and printed proof checked; recursive proof bodies not all read.')
    add('ample-growth','published algebraic theorems',
        'Sufficiently positive ample twists are globally generated (01Q3); higher cohomology of ample twists vanishes (0B5T); Euler characteristics are polynomials of degree at most coherent-support dimension (0BEM).',
        'Projective finite-type schemes, including nonreduced hyperplane T.',
        'Section 3.3 injects F^m|T into N^m using a regular section and derives O(m^(n-1)) without smooth or reduced T. Section 3.2 uses positive leading growth of a very ample bundle.',
        ['existing42-20','existing42-21','existing42-22'],['https://stacks.math.columbia.edu/tag/01Q3','https://stacks.math.columbia.edu/tag/0B5T','https://stacks.math.columbia.edu/tag/0BEM'])
    add('quasifinite-birational','published algebraic theorem',
        'A proper birational morphism over a normal base is an isomorphism near the image of a point where it is quasi-finite (0BFP).',
        'pi:Y to smooth normal original X.',
        'Section 3.4 excludes isolated zero-dimensional components in whole bad geometric fibers; antiample restrictions then force their inclusion in D.',
        ['existing42-35'],['https://stacks.math.columbia.edu/tag/0BFP'])
    add('Berkovich-functor','published analytic theorems',
        'Berkovich 1993 2.6.1 gives analytification, ground-field/product compatibility; 2.6.7 transfers separatedness; 2.6.8 identifies analytic images by valuation extension.',
        'Schemes locally of finite type over the specified analytic base; applied over the complete trivially valued k.',
        'Section 4 proves compactness by bounded seminorm domains, proper analytic surjectivity, all-point center compatibility and quotient descent.',
        ['additional-00'],['https://www.numdam.org/item/PMIHES_1993__78__5_0/'],
        reading='The complete pertinent printed statements/proofs 2.6.1, 2.6.7 and 2.6.8 read; necessary intervening printed proof units retained. Cross-referenced omitted proof of 2.6.9 not used.')
    add('canonical-section-values','published definition with direct application',
        'BJ 1.24 identifies the continuous canonical trivial metric by valuation-ring centers and unit frames; actual section evaluation is nonnegative order and multiplicative.',
        'The printed BJ carrier is projective; the proper smooth original-carrier construction is proved directly here.',
        'Section 4.1 verifies original metric continuity from a finite closed center-domain cover and compatibility under actual pullback.',
        ['whole68-47','additional-10'],[BJ])
    add('single-FS-definition','published definition and section arithmetic',
        'The numerical PSH definition is one decreasing net of generically finite real FS maxima in actual rational bundles with numerical classes tending to theta; products of sections add logarithms and generating-family zero maxima embed actual bundles.',
        'Smooth projective Y, arbitrary retained k. Definition only: no varying-class nested closure theorem.',
        'Sections 5.1--5.3 prove rounding, common ample embeddings, finite-polytope homogeneous projection, ray decomposition, literal divisor division and compactness of divided quotients directly.',
        ['existing42-00','existing42-01','whole68-51','whole68-00'],[BJ],
        reading='Definition and pertinent arithmetic/division proof units checked. False Lemma 4.6 and its nonample dependent conclusions are not premises.')
    add('ample-divisorial-envelope','actual-ample consequence of G0 with primary proof check',
        'Ample genuine potentials are determined at all points by divisorial values and satisfy the usc obstacle principle; bounded-above ample families have a genuine usc envelope preserving their divisorial supremum values.',
        'Actual ample H or A on projective Y only.',
        'Sections 5.1--5.3 reduce every numerical function to one such ample cone before invoking this. It proves the all-point fixed-divisor cone, not a general nonample envelope theorem.',
        ['additional-01','whole68-54','existing42-07'],[BJ],
        reading='Pertinent determination and ample divisorial-nonnegligibility proof units checked; use restricted to the G0 ample scope.')
    add('capacity-background','actual-ample consequence of G0; repaired estimate',
        'Ample signed integration by parts, zero-potential generic Dirac measure, concavity and strict locality. Capacity is defined as the supremum of genuine bounded probability products.',
        'Actual ample A and normalized genuine potentials on Y.',
        'Section 6 reconstructs Cap{a<=-s}<=n/s and J(max(z,-s))<=1+integral t^n Cap{z<=-t}dt. The explicit pole with exponent 1/(n+2) is E1. The printed missing factor and oversized exponent interval are not granted.',
        ['whole68-62','existing42-38'],[BJ],extra=['evidence/public-bj_capacity_body.txt'])
    add('BE-continuous-product','published analytic theorems',
        'BE v3 7.14 gives smooth semipositive approximation of actual finite FS metrics. 8.3--8.6 define raw local/global products and uniform convergence for continuous psh-regularizable metrics; 8.18 matches model Deligne pairings.',
        'Actual bundles on projective schemes over complete valued fields, including trivially valued fields. Continuous endpoint scope only.',
        'Section 8.2 compares each finite section stage, on projective Y and compact original isomorphic frame neighborhoods, with the actual local metric intersection product.',
        ['existing42-14','existing42-15','whole68-37','whole68-67'],[BE],
        reading='The pertinent statements and printed approximation/uniform-continuity proof units checked. These are not a bounded discontinuous or unbounded local bridge.')
    add('CLD-frame-units','published local analytic statements',
        'CLD v2 18.1.2 supplies the local frame transformation for smooth line-bundle curvature; 8.8.5 and the local pluriharmonic/unit identities give zero Hessian and invariance under logarithms of analytic units.',
        'At finite continuous/smooth stages on original frame neighborhoods off P.',
        'Sections 8.2--8.3 retain the plus sign lambda=psi+h_A+log|f| and pass the finite unit identities through global-section decreasing product limits.',
        ['existing42-17','existing42-19'],[CLD])
    add('ample-mixed-limits','actual-ample consequence of G0 with primary proof check',
        'Raw positive mixed Radon products have fixed intersection mass, integrate E1 tests, satisfy genuine mixed locality and comparison, and converge along unbounded decreasing nets and integrable weighted limits.',
        'Actual ample A and genuine E1 entries on Y only.',
        'Sections 6--9 prove exceptional zero mass before target selection and transport exact raw and weighted products; the weighted test identity retains its correct sign.',
        ['whole68-58','whole68-64','existing42-13'],[BJ])
    add('standard-topology-and-norms','standard published background with explicit application proofs',
        'Tychonoff compactness, compact Hausdorff normality and positive-functional Riesz representation; unique extension of a complete-field norm to a finite field extension; proper valuative criterion.',
        'Arbitrary compact Hausdorff, possibly nonmetrizable spaces and complete residue fields.',
        'Sections 4 and 7 construct compact center domains, quotient descent, Radon inversion without selections, uniqueness, and weak continuity at zero-exceptional limits.',
        ['additional-00','whole68-58'],['https://www.numdam.org/item/PMIHES_1993__78__5_0/',BJ],
        reading='Published statements treated as standard background; all primary proof bodies not separately retrieved. Every new application and zero-exceptional assertion is proved in the paper.')
    add('toric-properness','published primary theorem used only for a test',
        'A toric scheme from a finite fan is separated and of finite presentation. A complete fan gives properness, by the orbit/star/DVR character extension proof.',
        'Rohrer dissertation IV 1.2.1 and IV 1.3.11--1.3.12 over any field.',
        'Section 11 reconstructs the chart cover and repairs the star-completeness application using a relative-interior point.',
        ['additional-02','additional-03','additional-04'],['https://fredrohrer.ch/wp-content/uploads/2020/06/diss.pdf'],
        reading='Selected orbit/properness and star statement/proof units checked; finite-presentation/separatedness proof cross-references not all read. Not a premise of the whole-domain polar construction.')
    add('Miyake-Oda-test','published example, not a domain restriction',
        'Fujino--Sato Example 4.4 records the seven-ray ten-cone classical smooth complete nonprojective threefold.',
        'Its integral fan defines the carrier over every retained field.',
        'Section 11 proves unimodular chart smoothness, complete support, and three wall-degree expressions summing to zero, excluding an ample original bundle.',
        ['additional-05'],['https://www.math.kyoto-u.ac.jp/~fujino/wSato.pdf'])
    add('ample-proper-projective','published algebraic theorem',
        'A proper finite-type scheme with an ample line bundle is projective (Stacks 0B5N).',
        'Original proper carrier over k.',
        'Sections 1 and 11 exclude retaining an ample original datum and verify genuine nonprojectivity of the test.',
        urls=['https://stacks.math.columbia.edu/tag/0B5N'],extra=['evidence/public-stacks_new.txt'])
    add('false-flattening','diagnostic counterexample; not a premise',
        'General BJ v4 Lemma 4.6 is false in its varying-family extended-valued scope; common poles invalidate strict shifts.',
        'Compact convergent sequence plus an isolated point, families stable under constants.',
        'Section 2.1 supplies a complete counterexample and excludes this lemma and unproved dependent nonample closure from the reconstruction.',
        ['additional-11','whole68-07'],[BJ],extra=['evidence/packet-02.txt'],
        reading='Counterexample reconstructed; preserved supplied FAIL report is diagnostic mathematical data, not an operational instruction or a theorem disproving equations.')
    add('local-collar-L','MISSING MATHEMATICAL PREMISE',
        'For the actual raw weights psi+h_A+log|f| off P, equivalently the genuine A metric in frame e_A/f under division by s_D, prove agreement with the exact bounded discontinuous local contact/collar construction and divided global-section limits, its integrable weighted form and its relative-floor E1 nonpluripolar extension.',
        'Only the required local approximation category for the constructed retained original metrics; no arbitrary unrelated local psh class or choice independence for M.',
        'Section 10. Without this bridge the pretarget pairing equation is not the exact requested genuine original-carrier MA theorem.',
        ['whole68-22','whole68-23'],[WU],extra=['evidence/public-wu_collar.txt'],
        reading='Pertinent primary local definitions, Proposition 3.28 and Theorem 4.2 proofs inspected; collar references and sequence/globalization scope require repair. No new local theorem is granted.')
    dump('external-premises.json',premises)

    gap = (
        'Local bridge L: on compact original frame neighborhoods off the saturated polar image, '
        'identify the local contact/collar intersection product for the constructed bounded, possibly '
        'discontinuous raw weights with the divided global-section decreasing limit; prove independence '
        'of the required local approximants, collars and compatible frames, including integrable weighted '
        'limits, and identify its relative-floor finite-energy nonpluripolar extension. '
        'Until this is proved, the transported pairing and its attained equation are not asserted '
        'to be the exact genuine original-carrier Monge--Ampere operator and equation required by P16.2.'
    )
    status = {
        'id':'P16.2',
        'status':'partial; candidate=false',
        'exact_result':(
            'Unverified standalone proof reconstruction on every smooth integral proper positive-dimensional '
            'X over every algebraically closed trivially valued characteristic-zero field and any actual big '
            'rational L: retained polar data, actual original-section metrics, repaired fixed-divisor cone, '
            'finite energy, a pretarget raw Radon pairing of mass A^n with comparison, intrinsic target '
            'integrability, all original continuous energy variations and an attained pairing equation unique '
            'modulo constants. Genuine local MA identification remains conditional on L.'
        ),
        'proof_file':'P16.2-paper.md',
        'concrete_gaps':[gap],
    }
    dump('status.json',status)

    notes = [
        {
            'id':'n1',
            'summary':'The false extended-valued flattening lemma remains excluded. Direct single-net and actual-ample arguments repair the fixed-divisor cone; divided FS quotients need not decrease.',
            'detailedSummary':(
                'On arbitrary-cardinality algebraically closed trivially valued characteristic-zero fields, '
                'the reconstruction uses only one defining numerical FS net and the actual-ample G0 grant. '
                'It proves rational rounding within that net, an embedding into a fixed actual ample bundle, '
                'finite-polytope homogeneous projection, raywise homogeneous decomposition, literal divisor '
                'division and ample-compactness convergence of nonmonotone quotients. On smooth projective Y '
                'with actual B=A+D it obtains {v numerical B-psh: v<=sigma_D+C for some C}=sigma_D+PSH(Y,A) '
                'at all analytic points. This repairs cone foundations only; it does not establish the new local operator.'
            ),
            'text':(
                'The mathematical proof draft is in P16.2-paper.md, Sections 2 and 5, also rendered as '
                'P16.2-paper.tex and P16.2-paper.pdf. Rerun all preservation, diagnostics and document builds '
                'with python3 rerun.py. Primary literal units and exact scope restrictions are in '
                'external-premises.json and evidence/units-index.json.\n\n'
                'Counterexample proof: let K be an isolated q plus p_j converging to p_infinity. '
                'F_a consists of f(q)=c, f(p_a)=-infinity and f=c-m elsewhere, m positive integer. '
                'These extended-continuous families are stable under constants. For each fixed a the net '
                'm increasing gives g(q)=0 and g=-infinity elsewhere, so g lies in each limiting family '
                'of parameter 1/a. A decreasing original-family net cannot change its label after any '
                'term from F_a: later values at p_a must stay -infinity, which only F_a permits. '
                'Its parameters therefore cannot tend to zero. This disproves the general BJ Lemma 4.6, '
                'not an equation theorem. Strict shifts at a common pole and the associated strictly '
                'negative exponential difference are invalid.\n\n'
                'Safe fixed-A flattening uses finite continuous inner FS functions. A small positive '
                'shift below two finite upper functions remains strictly smaller even at a limiting '
                'pole; compactness of the negative open sets provides a common inner index. This is '
                'done before adding sigma_D. Rational coefficient rounding within a single original '
                'net instead uses non-strict inequalities phi_i<=f_i,delta<=phi_i+delta and '
                'g_i,delta=f_i,delta+delta. Choose 2delta_new<=min(delta_old) to get a directed '
                'decreasing g-net without any strict pole argument.\n\n'
                'For rational coefficients lambda_j with max lambda_j>=0, the homogeneous projection '
                'has the formula inf_{r>=0} max_j(x_j+r lambda_j) = '
                'max_{vertices w of {w>=0,sum w=1,w.lambda>=0}} sum w_j x_j. '
                'The vertices are nonnegative-slope unit vectors and rational zero-slope two-branch '
                'mixtures. Breakpoint convexity proves the formula; replacing -infinity entries by '
                'finite floors and commuting infima handles every base-locus point. Clearing denominators '
                'gives actual section monomials in the same bundle. One-dimensional supporting lines '
                'then reconstruct every genuine potential from its homogeneous components.\n\n'
                'For homogeneous h<=sigma_D, compactness of {sigma_D=-1} yields FS approximants '
                'h_i<=t_i sigma_D with t_i increasing to 1. Prime-divisor orders allow actual global '
                'section division by s_(degree*t_i D), using normality. The quotients are realized '
                'after arbitrarily small numerical corrections in a fixed actual ample A cone. '
                'Normalized ample compactness, followed by divisorial determination in a common '
                'ample cone, gives h=sigma_D+r at every point. Homogeneous decomposition and ample '
                'envelopes give the entire reference-dominated cone. No varying-class nested '
                'closure is invoked. On P1, h_i=(1-i^-2)sigma decreases, but subtracting '
                't_i sigma, t_i=1-i^-1, gives (i^-1-i^-2)sigma, increasing wherever sigma<0. '
                'Thus quotient monotonicity is explicitly not assumed.\n\n'
                'The exact-arithmetic diagnostic output diagnostics-output.json matches 5,616 '
                'three-branch cases with slopes {-1,0,1}, values {-2,-1,0,1,2,-infinity}. '
                'This finite grid supports checking the implementation, not the mathematical '
                'generalization. All claims are unverified proof drafts relative to the actual-ample grant.'
            ),
            'support':[],
        },
        {
            'id':'n2',
            'summary':'Retained polar data and genuine original-section metrics are reconstructed for every smooth integral proper carrier and every actual big rational L, with whole bad-fiber saturation and arbitrary field cardinality.',
            'detailedSummary':(
                'The argument first obtains smooth projective Y by Chow and the exact characteristic-zero '
                'Temkin theorem, proves actual section descent over normal X, and constructs a big original '
                'Cartier bundle. For any specified big L, a hyperplane restriction growth argument gives '
                'pi*L=A+D. Every bad geometric fiber is wholly inside D because its positive-dimensional '
                'components carry an antiample restriction. P=pi|D| is saturated, and Y minus D is isomorphic '
                'to X minus P. Canonical original metrics are constructed using compatible valuative centers; '
                'sigma_D+psi descends all-point, including -infinity poles. Multiplication by the actual '
                'divisor section converts one finite fixed-A FS net into an actual decreasing original-L '
                'section net. The reference-dominated original section cone is therefore bijective and '
                'divisorially homeomorphic to the genuine ample cone. Its compactness and finite energy '
                'are constructed without projectivity of the original carrier.'
            ),
            'text':(
                'P16.2-paper.md Sections 3--6 contain the complete draft arguments, with source scopes '
                'and literal evidence in external-premises.json. TeX and PDF versions have the same '
                'problem ID; rerun with python3 rerun.py.\n\n'
                'Fix any algebraically closed trivially valued characteristic-zero k, of arbitrary '
                'cardinality, and any smooth integral proper X of dimension n>0. Chow gives an integral '
                'projective birational refinement. Temkin v2 Theorem 1.2.1 applies because it is '
                'Noetherian quasi-excellent generically reduced and over Spec Q; finite type over Q is '
                'not required. Its finite blowup sequence remains integral and projective, and the '
                'regular final Y is smooth over perfect k. The normal-base theorem gives pi_*O_Y=O_X '
                'and literal H0(Y,p pi*L)=H0(X,pL). A very ample hyperplane H on Y avoiding the finite '
                'exceptional primes pushes to an effective Cartier B on smooth X; pi*B=H+E with '
                'effective exceptional E, and multiplication by s_E injects the positive degree-n '
                'section growth of H into that of B. Thus big actual original bundles exist.\n\n'
                'For any chosen big rational L, let F=q pi*L integral. A very ample hyperplane '
                'T on Y need not be reduced: on T choose ample N with N-F|T globally generated '
                'and a section avoiding all associated points. Its powers inject F^m|T into N^m. '
                'Serre vanishing and the coherent Euler polynomial give h0(T,F^m|T)=O(m^(n-1)). '
                'Hence positive limsup degree-n growth of F supplies a section of mF-M for a '
                'very ample M, yielding pi*L=A+D with A=M/(qm), D effective rational. The datum '
                'retains the actual isomorphism, and its raw mass is A^n; no choice independence '
                'or unrestricted minimal-class volume is claimed.\n\n'
                'On a bad geometric fiber, the normal-base quasi-finite birational theorem excludes '
                'zero-dimensional components. On every integral reduced component pi*L is trivial, '
                'so D restricts to -A. A nonzero antiample section would inject unbounded ample '
                'section growth into H0(O), impossible. Thus all components, and the whole bad '
                'fiber, lie in |D|. With P=pi(|D|), pi^-1(P)=|D| and Y minus |D| is isomorphic to X minus P. '
                'This uses saturation of entire fibers, not just exceptional divisors.\n\n'
                'Proper valuation-ring centers and their uniqueness give compatible canonical '
                'trivial metrics on all actual original bundles. Compactness is proved using a '
                'finite affine center-domain cover and Tychonoff, without metrizability. Analytic '
                'surjectivity and compact-to-Hausdorff closed quotient descent show that '
                'sigma_D+psi, for genuine A-psh psi, descends to an actual usc metric u. On '
                'P its value is -infinity, and elsewhere the fiber is singleton. Clear all '
                'degrees in a finite fixed-A approximating net, multiply every section by '
                's_(pD), and use literal section descent. This produces actual original '
                'section maxima u_alpha decreasing to u at every analytic point, including '
                'the common poles. With tau=F(0), n1 gives '
                '{original section-psh u: u<=tau+C}=F(PSH(Y,A)). '
                'Divisorial order cancellation and ample determination give a genuine quotient, '
                'normalized compactness and E_M(u)=E_A(Q(u)).\n\n'
                'The classical Miyake--Oda fan is checked as a test over every retained field, '
                'not as a domain restriction: its ten maximal charts are unimodular A3 charts, '
                'the complete-fan DVR proof gives properness, and the three wall degrees '
                'a1+a6-a2-a5, a2+a7-a3-a6, a3+a5-a1-a7 sum to zero. No ample original bundle '
                'can have positive degree on all three proper curves. The small determinant '
                'and coefficient checks are diagnostics only. Genuine local MA identification '
                'is not a conclusion of this geometric and cone reconstruction.'
            ),
            'support':['n1'],
        },
        {
            'id':'n3',
            'summary':'A pretarget pairing has raw mass A^n, intrinsic target integrability and an attained unique equation with all original continuous variations. P16.2 remains incomplete: the local contact/collar bridge for bounded discontinuous and finite-energy products is unproved.',
            'detailedSummary':(
                'Before any target, the retained genuine quotient gives positive mixed Radon pairings '
                'p_*M_A. A reconstructed capacity estimate supplies an actual E1 pole on all D, proving '
                'zero exceptional mass and target exclusion. Fiber-max relative potentials q_u are '
                'actual original usc functions; their dual energy is finite exactly when every '
                'finite-energy q_u is integrable. Unique zero-exceptional Radon inversion identifies '
                'this with the ample target class and gives actual attainment, comparison and uniqueness '
                'modulo constants. Minorant and all-original-continuous-majorant energies agree, and '
                'their two-sided derivative includes every f in C(Xan). Divided global-section local '
                'products converge even to bounded discontinuous floors, and their relative-floor '
                'mixed nonpluripolar and weighted limits recover the pairing. This does not yet '
                'identify the full required local contact/collar construction. The exact remaining '
                'statement L is recorded, and candidate is false.'
            ),
            'text':(
                'The deliverable is the standalone P16.2-paper.md, P16.2-paper.tex and P16.2-paper.pdf, '
                'with status.json, external-premises.json, 18 preserved supplied blocks, 124 literal '
                'primary units, and retained new public responses. Run python3 rerun.py. Exact argv, '
                'environment versions, stdout/stderr and artifact hashes are retained; document '
                'compilation and finite diagnostics are not mathematical certification.\n\n'
                'In the notation and domain of n2, let Q(u) be the genuine A quotient. Define the '
                'pretarget symmetric pairing as p_*M_A(Q(u1),...,Q(un)); it is positive Radon '
                'of exact raw mass V=A^n before any target is selected. To prove zero mass '
                'on D, take a normalized A-section logarithm a vanishing along D and '
                'w=1-(1-a)^(1/(n+2)). Convex slopes in [0,1] and ample envelopes give genuine '
                'membership. Signed integration by parts proves Cap{a<=-s}<=n/s. For bounded '
                'floors z_s, strict locality, fixed masses and mixed positivity give '
                'J(z_s)<=1+integral_1^infinity t^n Cap{z<=-t}dt. The factor t^n is essential. '
                'For w its integrand is O(t^-2), so w is genuinely E1 and is -infinity on '
                'all D. Every ample mixed E1 product integrates w, hence gives D zero mass.\n\n'
                'Define q_u(x)=max_{p(y)=x} Q(u)(y), attained on the compact fiber, with '
                'upper semicontinuity proved by closed images of superlevel sets. Off P it '
                'equals u-tau; on P it is a canonical retained relative value, never '
                '-infinity-(-infinity). For mass-V Radon mu set '
                'D_M(mu)=sup_{u in E1_M}(E_M(u)-integral q_u dmu). Finiteness forces '
                'every q_u integrable, and q_F(w) excludes P. The positive-functional '
                'construction integral g(jx)dmu on X minus P, followed by Riesz, gives the '
                'unique Radon inverse nu with zero D mass; compact bump functions prove '
                'that assertion and weak lifting continuity. D_M(mu)=E_A^vee(nu). By '
                'G0 it is finite iff every finite-energy q_u is integrable. No imposed '
                'skeletal support or arbitrary fiber selection occurs.\n\n'
                'For all original f in C(Xan), cancel finite sigma at divisorial '
                'function-field points and apply actual-ample usc determination to obtain '
                'F(eta)<=u+t f iff eta<=Q(u)+t p*f. The genuine-minorant energy is '
                'E_A(P_A(Q(u)+t p*f)). The infimum over ALL original continuous relative '
                'majorants q_u+t f<=b is identical: decreasing all b, compact ample '
                'envelopes and singleton divisorial fibers determine the same limit. '
                'Thus both derivative signs give the raw integral of f against the '
                'pairing. Ample attainment and the actual section map give an attained '
                'original finite-energy maximizer; both derivative signs give its '
                'pairing equation. Zero-exceptional Radon inversion and G0 give '
                'uniqueness modulo one constant, and comparison transports on strict '
                'sets outside P. These are actual pairing results, conditional as a '
                'genuine P16.2 local Monge--Ampere theory.\n\n'
                'Local progress: in a frame off P, the literal raw weight is '
                'lambda=psi+h_A+log|f_D|, with a PLUS unit logarithm. Finite actual '
                'original-section products agree with the finite ample products by '
                'continuous local intersection theory. For finite fixed-A nets '
                'decreasing globally to bounded genuine psi, G0 gives convergence on '
                'compact original frame neighborhoods even for discontinuous endpoints. '
                'It gives germ independence in this divided global-section category, '
                'and finite-stage analytic-unit frame identities pass through its '
                'decreasing limits. The relative floors max(u,tau-j), not absolute '
                'original floors, correspond to max(psi,-j). Mixed locality and E1 '
                'integrability recover their unbounded nonpluripolar restrictions and '
                'weighted limits with mass V.\n\n'
                'Exact unresolved lemma L: prove that the local rational contact '
                'approximants and actual ample collars of the required original local '
                'intersection construction, on compact original frame neighborhoods '
                'off P, give these same bounded, possibly discontinuous products '
                'independently of contact nets, collar realizations and compatible '
                'frames; include their integrable weighted limits and identify their '
                'relative-floor finite-energy nonpluripolar extension. The missing '
                'step is product comparison with the actual ample local construction. '
                'Division by s_D maps the original frame e_L to the actual A frame '
                'e_A/f_D, isometrically. A direct audit in that frame could avoid '
                'globalization of local contact families, which need not be '
                'globally decreasing fixed-A nets. Neither route is completed here. '
                'A continuous uniform-convergence '
                'theorem does not prove this. The primary collar identity must '
                'retain Phi=p+Psi/a and lambda=a Phi+a h0+M+1; omission of p or '
                'a zero-branch maximum asserted negative is invalid. No stronger '
                'arbitrary-local-psh or retained-choice-independence theorem is '
                'introduced as a gate. No counterexample to L or P16.2 is claimed. '
                'The exact original task remains unproved; candidate=false.'
            ),
            'support':['n1','n2'],
        },
    ]
    dump('notes.json',{'notes':notes,'candidate':False})
    dump('input-binding.json',{
        'file':'input.json','sha256':hashlib.sha256((ROOT/'input.json').read_bytes()).hexdigest(),
        'supplied_notes':[], 'preservation':'Input file was not edited; all extractions come solely from its assignment and task fields.',
    })
    print(json.dumps({'premises':len(premises),'notes':len(notes),'candidate':False,'status_keys':list(status)},indent=2))


if __name__ == '__main__':
    main()
