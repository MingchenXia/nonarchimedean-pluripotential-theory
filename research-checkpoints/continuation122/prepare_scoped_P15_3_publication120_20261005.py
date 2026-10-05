from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, re

R = Path('/workspace/research'); K = R / 'root-checks'
W = R / 'campaigns/round-118/P15.3-original-general-P-type-and-numerical-carrier-research/artifacts/codex-J4wN53'
D = R / 'deliverables/scoped-P15.3-round120'
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
review_path = K / 'P15.3-round120-actual-scoped-independent-review-20261005.json'
assert sha(review_path) == '066f08ead04b8404c592256c8781ad26d9da8131b0efb6144cf77ddf34051f2b'
review = json.loads(review_path.read_text())
assert review['verdict'] == 'PASS' and len(review['premises']) == 10 and len(review['passages']) == 12
for p in review['passages']:
    assert p['statement'] == review['premises'][p['premise']]
    assert p['url'].startswith('https://')
assert sha(W / 'P15.3-argument.md') == 'dde8e2c968e0e29199f58473ac65effa70ae05a81d1662f4f28db71db6db664e'
assert not D.exists(); D.mkdir(parents=True)

def save(name, obj):
    (D / name).write_text(json.dumps(obj, ensure_ascii=False, indent=2) + '\n')

lines = (W / 'P15.3-argument.md').read_text().split('\n')
main = '\n'.join(lines[4:154])
main = main.replace(lines[26], 'The following source audit fixes the versions and application domains. Inclusive LF coordinates refer to one-based entries of the version-bound extraction split at literal newline characters. The independent review additionally checked the primary removability and representative-uniqueness statements in Demailly\'s June 21, 2012 notes, and the Demailly--Paun and Deng inputs used below. Complete selected printed proofs were checked; recursively cited foundations and entire works were not exhaustively verified.')
main = main.replace('Their induction proof is retained in the extracts, including', 'The selected induction proof was checked in the version-bound extraction, including')
main = main.replace('The appendix\'s bounded-potential products use the classical Bedford–Taylor/nonpluripolar rules explicitly stated there; no new theorem about arbitrary unbounded potentials is imported from them.', 'Demailly\'s Theorem I.5.24 gives removability; Theorems I.4.18 and I.5.5 give canonical-representative uniqueness. No new theorem about arbitrary unbounded products is imported.')
main = main.replace("exactly as reconstructed in the appendix's local calculation", 'as reconstructed in Section 14')
main = main.replace("This reconstruction validates the proposed torus obstruction with those exact axioms.", 'This proves the torus obstruction under those exact axioms.')
main += '\n\nThe remaining general obligations are a genuine construction for arbitrary prescribed ordinary P-types, an actual dimensional carrier and numerical invariant, and all asserted model, perturbation and reference-scale independence. These scoped counterexamples do not exclude richer constructions.\n'

note = K / 'P15.3-exact-exceptional-flag-trapezoid-and-rescaling-draft-20261005-continuation129.md'
exact = note.read_text().split('## 1. Actual geometric data and explicit imported inputs', 1)[1]
exact = '## 9. Actual geometric data and explicit imported inputs' + exact
for old, new in [(2, 10), (3, 11), (4, 12), (5, 13)]:
    exact = exact.replace(f'## {old}. ', f'## {new}. ')
exact = exact.replace('proposal128', 'Sections 3--4')
exact = exact.replace('extends a positive analytic curve current in the restriction of a Kähler surface class to an analytic Kähler current in that surface class', 'extends a Kähler curve current with finitely many logarithmic poles and smooth local remainders in the restriction of a Kähler surface class to a Kähler current in that surface class')
start = exact.index('I read Demailly--Paun')
end = exact.index('\n\n## 10.', start)
exact = exact[:start] + 'The version-bound source audit checked Demailly--Paun\'s complete main statement and printed proof, and Deng\'s complete Proposition 4.16 and its extension proof. Deng\'s nonbig numerical-dimension-one statement retains a positive-degree curve hypothesis. No such curve exists on the torus, and the pullback of beta pairs to zero with E. Complete selected proofs retain their published background inputs; whole-work and recursive-foundation verification are not claimed.' + exact[end:]
exact = exact.replace('This local argument is also the blowup construction used in the reviewed round50 proof.', 'Section 14 supplies the complete local blowup construction.')
exact = exact.replace('Section2', 'Section 10').replace('Section2', 'Section 10')
exact = exact.replace('I propose the exact formula', 'The exact body is')
old = 'Near q, the two rational coefficients y and delta have a common positive denominator; the local maximum is equivalent up to O(1) to the logarithm of a holomorphic ideal.'
new = r'''Use the convention $dd^c=i\partial\bar\partial/(2\pi)$ fixed in Section 1, with $\log|z|^2$ as the unit divisor potential. Translating Deng's logarithm convention preserves all rational pole coefficients. For $y>0$, choose rational $r>0$ and positive integers $m,n$ with $y=mr$ and $\delta=nr$. In local coordinates with $E=\{z_2=0\}$, the maximum of the two potentials equals

$$r\log\big((|z_1|^2+|z_2|^2)^m+|z_2|^{2n}\big)+O(1).$$

The first summand is a sum of squared holomorphic monomials, so this is the logarithm of an actual ideal with rational coefficient. For $y=0$ the local extension is bounded instead. The class coefficient $a\epsilon$ need not be rational.'''
assert old in exact; exact = exact.replace(old, new)
exact = exact.replace('This proves(1), subject to independent checking of the two explicit imported analytic applications.', 'The two explicit imported analytic applications satisfy their stated hypotheses, proving (1).')
start = exact.index('This calculation would refine')
exact = exact[:start] + 'The exact body and asymptotics refine the torus obstruction on one genuine exceptional flag. They treat smooth P-type zero and an actual rank-one transcendental nef class. The arbitrary P-sensitive lower-dimensional construction of original P15.3 remains open. No universal impossibility theorem is claimed.\n'

blowup = '\n'.join(lines[255:265])
blowup = blowup.replace('S_hat', 'X').replace('S ->', 'M ->').replace(' S,', ' M,')
blowup_intro = '## 14. Actual local Kähler blowup construction\n\nLet $M$ be a smooth compact Kähler surface with actual Kähler form kappa_form. The following construction proves the small positive exceptional subtraction used in Sections 5 and 10.\n\n'

intro = '''# Dense null leaves, collapsing valuation bodies, and an exact exceptional trapezoid

We construct a curve-free compact Kähler torus carrying a nonzero rank-one transcendental nef form with numerical dimension one. Its genuine potentials are constant on every smooth Kähler modification, and every fixed smooth-flag current-valuation body collapses to a point under unrescaled positive perturbation. On a one-point blowup we compute the genuine positive-level body exactly and classify its scalar and diagonal rescaling limits. The scalar square-root rescaling gives a two-dimensional triangle; coordinate choices can instead produce intervals.

These are two scoped results for smooth ordinary P-type zero. They passed independent Xean native Codex reconstruction (gpt-6.1-sol, xhigh), operation 0eb5014e-6254-4201-ac38-0457743f9403, reported 5 October 2026. The verification is a source-aware mathematical review, not a formal proof certificate or a priority claim. Original P15.3, which asks for an arbitrary P-sensitive lower-dimensional theory, remains open.

'''
body = intro + main + '\n' + exact + '\n' + blowup_intro + blowup + '\n\n## 15. Primary references and application ledger\n\n'
for i, premise in enumerate(review['premises']):
    urls = list(dict.fromkeys(p['url'] for p in review['passages'] if p['premise'] == i))
    body += f'{i+1}. {premise} Primary source: ' + ', '.join(urls) + '\n\n'
(D / 'P15.3-argument.md').write_text(body)
(D / 'P15.3-correctness-review.json').write_bytes(review_path.read_bytes())
save('author-source-provenance.json', {
    'prepared_utc': datetime.now(timezone.utc).isoformat(), 'original_closed': False,
    'whole_native118_source': {'path': str(W / 'P15.3-argument.md'), 'sha256': sha(W / 'P15.3-argument.md'), 'selected_literal_LF': [[5,154],[256,265]]},
    'exact_body129': {'path': str(note), 'sha256': sha(note)},
    'canonical_review': {'path': str(review_path), 'sha256': sha(review_path), 'verdict': review['verdict'], 'operation_id': review['operationId']},
    'changes': ['Combine only the two accepted scoped proof units and indispensable local blowup calculation.', 'Update historical drafting and provenance text, omit separate historical product/dense-pole appendix.', 'Apply the two harmless Deng input/normalization clarifications explicitly stated by actual review120.', 'No new mathematical theorem or broader closure imported.'],
    'existing_P16_4_editor_modified_or_replaced_or_new_tab_opened': False})
save('source-application-ledger.json', [{'premise_index':i,'statement':p,'actual_review_passages':[x for x in review['passages'] if x['premise']==i]} for i,p in enumerate(review['premises'])])

# Reuse the already read local converter, then make its presentation accept
# multiline mathematical displays and explicit section numbers.
builder = (W / 'build_paper.py').read_text()
builder = builder.replace(r'\author{Unverified research draft}', r'\author{Scoped research paper}')
builder = builder.replace("command={1:'section',2:'subsection',3:'subsubsection'}.get(len(head.group(1)),'paragraph')", "command={1:'section*',2:'section*',3:'subsection*'}.get(len(head.group(1)),'paragraph')")
old = """  if l.startswith('$$'):
   assert l.endswith('$$') and len(l)>4
   out.append(r'\\['+l[2:-2]+r'\\]');i+=1;continue"""
new = """  if l.startswith('$$'):
   formula=l[2:];i+=1
   while not formula.endswith('$$'):
    assert i<len(lines), 'Unclosed display'
    formula+='\\n'+lines[i];i+=1
   out.append(r'\\['+formula[:-2]+r'\\]');continue"""
assert old in builder; builder = builder.replace(old, new)
# Ordinary primary URLs are breakable and clickable in the PDF.
builder = builder.replace("r'`[^`]*`|\\*\\*[^*]*\\*\\*|\\$[^$]*\\$'", "r'https://[^\\s,]+|`[^`]*`|\\*\\*[^*]*\\*\\*|\\$[^$]*\\$'")
builder = builder.replace("if token.startswith('`'):", "if token.startswith('https://'):parts.append(r'\\url{'+token+'}')\n  elif token.startswith('`'):")
(D / 'build_paper.py').write_text(builder)
print(json.dumps({'directory':str(D),'argument_bytes':(D/'P15.3-argument.md').stat().st_size,'review':'PASS','original_closed':False},indent=2))
