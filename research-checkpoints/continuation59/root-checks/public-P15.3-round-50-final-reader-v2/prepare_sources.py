#!/usr/bin/env python3
"""Freeze the four allowed primary extracts and literal, LF-indexed passages."""
from pathlib import Path
import hashlib
import json
import platform
import shutil
import subprocess

ROOT = Path(__file__).resolve().parent
OUT = ROOT / 'source-extracts'
OUT.mkdir(exist_ok=True)
CACHE = Path('/workspace/research/shared-sources')
SOURCES = [
 dict(id='DRWNXZ', version='2309.07584v3', date='5 Jan 2026', title='Transcendental Okounkov bodies',
      pdf_hash='48b82ded9de9d2fee8d2c525129b1f176bbfc87dfa67f7ac4bfe9b23eba94e83',
      text_hash='203fcf50f30ff047be9557db66d9f83473e996ea3cc943f652db0b6bd9da802e',
      passages=[('flag-domain-and-modifications',101,146),('singularity-order-and-pullback-proof',226,263),
                ('divisor-subtraction-and-proof',309,333),('gentle-singularities',338,361),
                ('regularization',398,411),('class-body-definitions-and-proofs',561,715),
                ('lifting-flags-and-proof-bodies',716,850),('partial-bodies-and-proof-bodies',852,966),
                ('volume-theorem-and-entire-section-7-proof',1137,1415)],
      checks=[
        'Applied only on compact Kähler manifolds with a specified globally smooth connected complete flag.',
        'Definition 5.1 requires a Kähler current with gentle analytic singularities. R_epsilon=[D]+beta+epsilon*Omega has these properties for rational smooth D and smooth semipositive beta.',
        'Example 5.3 is used only with residual beta+epsilon*Omega Kähler. The two inclusions are also proved in the argument.',
        'Lemma 3.1 is applied only to positive currents with analytic singularities in a big residual class.',
        'Theorem 7.6 is applied to the Kähler surface class kappa_a, never to infer dimension from zero three-dimensional volume.',
        'Section 2 initially fixes a big class. For Lemma 2.1 the argument reproduces its removable-singularity proof explicitly, thereby checking the same psh pullback bijection in a nonbig pullback class; it is not applied to an arbitrary class on a modification. No independence of arbitrary modified flags is claimed.',
        'The class-level Corollary 7.7 and its proof do not assert a lower-dimensional numerical theorem or retention of a prescribed potential.' ]),
 dict(id='Xia', version='2112.04290v2', date='13 Apr 2024', title='Partial Okounkov bodies and Duistermaat--Heckman measures of non-Archimedean metrics',
      pdf_hash='0847fc4313e630946e8ff122ab2de587185eb9067d6c3efe2a65dfcfc8e72f2f',
      text_hash='d59c0231ec64871b6a21657bcc3a952af8b2e9c975eee07db1d99f0ef4cf7273',
      passages=[('projective-domain-and-introduction-theorems',33,119),('P-C-and-I-definitions-and-proof',371,429),
                ('ideal-volume-and-I-envelope-formula',458,494),('partial-body-construction-and-proof',988,1185),
                ('valuative-singularity-recovery-and-proof',1514,1562),('section-5.6-and-conjecture-5.29',1623,1637)],
      checks=[
        'This source constructs section/multiplier-ideal bodies on projective varieties with line-bundle data. It is audited, not applied to the nonprojective product theorem.',
        'The invariant factors through all multiplier ideals I(k*phi); Proposition 5.8 and section 5.6 preserve this I-invariance.',
        'Theorem 2.19 uses the mass of P[phi]_I, not a general equality with the mass of phi.',
        'At zero actual mass, Proposition 2.10 does not identify C[phi] with P[phi]. They are kept separate.',
        'Section 5.6 defines the limiting body; Conjecture 5.29 states, rather than proves, its dimension equality.',
        'No extension of the conjecture to every flag or to transcendental classes is assumed.' ]),
 dict(id='Cao', version='1210.5692v1', date='21 Oct 2012', title='Numerical dimension and a Kawamata--Viehweg--Nadel-type vanishing theorem on compact Kahler manifolds',
      pdf_hash='17717664b0ae2b154e76e2ecb68c9f63f09dc74be6f25bac7f04b7ee0103b0d6',
      text_hash='1bae7bf39d69c41451507e29d908977cb4599bf0b10216eb8b8295c7ba769fce',
      passages=[('normalization-and-metric-convention',100,128),('definitions-2-3-4-and-independence-proof',162,289),
                ('class-dimension-versus-pair-dimension',1165,1179)],
      checks=[
        'Definition 3 is a cohomological product of general positive currents, computed using absolutely continuous parts of quasi-equisingular analytic approximants.',
        'Definition 4 is worded for a pseudoeffective line bundle and metric; the transcendental example explicitly names its current-product analogue d_Cao instead of claiming a line-bundle application.',
        'For the analytic divisorial current in the theorem, the constant approximation meets every condition of Definition 2, so Definition 3 gives [beta^k].',
        'Equality with actual nonpluripolar products is proved only for this analytic divisorial type using locality and the bounded remainder. No general identification is made.',
        'The cited approximation-independence statement is retained with its actual proof, not replaced with nonpluripolar continuity.' ]),
 dict(id='CHPW', version='1508.03922v5', date='5 Feb 2018 (arXiv header); September 24, 2018 (internal manuscript Date)', title='Okounkov bodies associated to pseudoeffective divisors',
      pdf_hash='8217255c74b4402b6e6a3167db1a6fd8f539056029d82b13556b82828b191a0c',
      text_hash='5ff42d0b3c3c0f0aca4af9fccafdfc96f9e60a30e46cb64fcf9a59b45fcf2c14',
      passages=[('limiting-body-definition',80,105),('theorem-B-and-flag-hypotheses',124,185),
                ('positive-volume-subvarieties-and-proof',532,574),('theorems-3.20-3.22-and-proofs-and-flag-warning',919,1106),
                ('bad-flag-example-4.1',1258,1274)],
      checks=[
        'Theorem B/Corollary 3.22 is for a pseudoeffective real divisor on a smooth projective variety, with a flag containing a positive volume subvariety.',
        'The lower-dimensional mass is augmented restricted volume along that subvariety, not an unrestricted flag-independent number.',
        'Remark 3.24 explicitly allows strict dimension inequality for other flags.',
        'None of these algebraic theorems is applied to the nonprojective transcendental example. Its product formula is proved directly.' ])
]

def sha(b):
    return hashlib.sha256(b).hexdigest()

records = []
for src in SOURCES:
    stem = 'P15.3-arxiv-' + src['version'] + '-20261004'
    pdf = CACHE / (stem + '.pdf')
    txt = CACHE / (stem + '.txt')
    pdf_bytes, txt_bytes = pdf.read_bytes(), txt.read_bytes()
    assert sha(pdf_bytes) == src['pdf_hash']
    assert sha(txt_bytes) == src['text_hash']
    full = txt_bytes.decode('utf-8')
    lines = full.split('\n')  # Required LF convention; never splitlines().
    local = OUT / (src['version'] + '-full.txt')
    local.write_bytes(txt_bytes)
    passages = []
    for label, first, last in src['passages']:
        literal = '\n'.join(lines[first-1:last])
        fragment = OUT / (src['version'] + '--' + label + '.txt')
        fragment.write_bytes(literal.encode('utf-8'))
        passages.append(dict(id=label, first_line=first, last_line=last,
                             first_textflow_page=1+'\n'.join(lines[:first-1]).count('\f'),
                             last_textflow_page=1+'\n'.join(lines[:last]).count('\f'),
                             literal=literal, local_file=str(fragment.relative_to(ROOT)),
                             sha256=sha(literal.encode('utf-8')),
                             content_kind='Literal statement(s) and relevant proof body/bodies; conjecture records have no supplied proof.'))
    records.append(dict(id=src['id'], title=src['title'], exact_arxiv_version=src['version'],
                        printed_date=src['date'], public_source='https://arxiv.org/pdf/'+src['version'],
                        pdf_location=str(pdf), pdf_sha256=sha(pdf_bytes),
                        supplied_extract_location=str(txt), extract_sha256=sha(txt_bytes),
                        byte_identical_local_extract=str(local.relative_to(ROOT)),
                        source_line_count=len(lines), line_number_convention="UTF-8 text.split('\\n'); one-based indexing; trailing empty line counted; form feeds remain inside lines",
                        passages=passages, application_checks=src['checks']))

provenance = dict(scope='Only the four supplied public primary caches were read. No generated proof, private material, or other mathematical source was read.',
                  epistemic_status='Source quotations and application audit; new arguments are unverified mathematical drafts.',
                  page_convention='Textflow pages count literal form-feed separators, independently of printed pagination. Exact locations are the inclusive LF line ranges.',
                  sources=records)
(OUT/'source-provenance.json').write_text(json.dumps(provenance,ensure_ascii=False,indent=2)+'\n')
versions = {}
for command in ['pdflatex','latexmk','python3']:
    result = subprocess.run([command,'--version'],capture_output=True,text=True)
    versions[command] = dict(path=shutil.which(command),returncode=result.returncode,
                             stdout=result.stdout,stderr=result.stderr)
(ROOT/'environment.json').write_text(json.dumps(dict(python=platform.python_version(),os=platform.system(),kernel=platform.release(),tools=versions,
     constraints='No installation, external network, subagents, account/runtime changes, or heavy computation used.'),indent=2)+'\n')
print(json.dumps([dict(id=s['id'],version=s['exact_arxiv_version'],source_line_count=s['source_line_count'],hashes_match=True,passages=len(s['passages'])) for s in records],indent=2))
