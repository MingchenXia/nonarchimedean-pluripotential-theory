#!/usr/bin/env python3
"""Reassemble review access from immutable sources, using LF coordinates only."""
from pathlib import Path
import hashlib
import json

ROOT = Path(__file__).resolve().parent


def sha(b):
    return hashlib.sha256(b).hexdigest()


inventory = json.loads((ROOT / 'evidence/source-inventory.json').read_text())
sources = {Path(x['file']).name: x for x in inventory}
selections = [
    ('vdp-boundary-check', 'van-der-Put-AIF-1980-30-4-155.txt', 42, 221,
     'Field convention and full Theorem 1.1 proof including Lemma 1.2; used only to check the boundary-identity ambient hypothesis.', True, True),
    ('berkovich-boundary-domain-check', 'Berkovich-PMIHES-1993-78-5.txt', 1335, 1438,
     'Full Theorem 1.6.1 and Lemma 1.6.2 proofs. Domain comparison only, followed separately by Thuillier ordinary boundary/interior identification.', True, True),
    ('thu-residue', 'Thuillier-tel-00010990v1.txt', 1222, 1360,
     'Definition of H(x); full Propositions 2.1.1 and 2.1.2 proofs.', True, True),
    ('thu-boundary', 'Thuillier-tel-00010990v1.txt', 1535, 1602,
     'Full Proposition 2.1.10 proof; curve convention and Proposition 2.1.12 statement. The latter has no separate printed proof here.', False, True),
    ('thu-components', 'Thuillier-tel-00010990v1.txt', 1604, 1638,
     'Full Lemma 2.1.13 proof and Remark 2.1.14; ordinary reduction fibres.', True, True),
    ('thu-standard-annulus-unit', 'Thuillier-tel-00010990v1.txt', 2079, 2148,
     'Full Lemma 2.2.1 proof and following Newton-polygon remark.', True, True),
    ('thu-supplied-skeleton', 'Thuillier-tel-00010990v1.txt', 2318, 2695,
     'Full Theorem 2.2.10 construction/proof through Lemmas 2.2.11--14 and Propositions 2.2.15--20; includes calibration definition.', True, True),
    ('thu-type2-cuts', 'Thuillier-tel-00010990v1.txt', 2791, 2856,
     'Full Lemma 2.2.22 proof. Only actual type-2 cuts are used in the new construction.', True, True),
    ('thu-223-to-227', 'Thuillier-tel-00010990v1.txt', 2858, 3227,
     'Full Propositions 2.2.23, 2.2.24, Lemma 2.2.25, Propositions 2.2.26 and 2.2.27. Only 24--26 are essential here; 23 and 27 were inspected as requested.', True, True),
    ('thu-residual-exact-sequence-not-used', 'Thuillier-tel-00010990v1.txt', 3623, 3700,
     'Context and full Lemma 2.3.22 proof. Inspected but not used to grant unit lifting or a common ordinary star.', True, False),
    ('cld-stokes-green', 'CLD-1204.6277v2.txt', 6992, 7018,
     'Full Proposition 5.11.1 proof, including compact intersection of supports.', True, True),
    ('cld-positive-integration', 'CLD-1204.6277v2.txt', 8089, 8129,
     'Complete definition and sign arguments in 7.3.1--7.3.4 for calibrated integration currents.', True, True),
    ('cld-smooth-psh-current', 'CLD-1204.6277v2.txt', 9991, 10018,
     'Full Proposition 8.3.1 proof; smooth-function/current identification. No nonsmooth converse is used.', True, True),
    ('cld-ordinary-unit-charts', 'CLD-1204.6277v2.txt', 21480, 21512,
     'Full Proposition 15.1.1 proof and Corollary 15.1.2. Ordinary-open clause (b) is retained.', True, True),
    ('cld-harmony', 'CLD-1204.6277v2.txt', 21869, 21971,
     'Full Theorem 15.6.1 and Lemma 15.6.2 proofs for the analytic interior.', True, True),
    ('gjr-actual-weights', 'GJR-2111.05741v3.txt', 3919, 3953,
     'Definitions/scope 15.1--15.2, including actual edge weights and boundary. This is not a printed theorem proof unit.', False, True),
    ('gjr-smooth-versus-weak-not-used', 'GJR-2111.05741v3.txt', 4064, 4076,
     'Remark 15.10, inspected for the smooth/weak distinction; no germ exactness is imported.', False, False),
]
blocks = []
manifest = []
for sid, name, first, last, desc, full, used in selections:
    meta = sources[name]
    data = Path(meta['original_path']).read_bytes()
    assert sha(data) == meta['sha256'], name
    # Formfeeds and every other PDF control byte remain within LF lines.
    lines = data.split(b'\n')
    body = b'\n'.join(lines[first-1:last])
    out = ROOT / 'sources' / (sid + '.txt')
    out.write_bytes(body)
    m = dict(id=sid, source=meta['original_path'], source_sha256=sha(data),
             first_lf_line=first, last_lf_line=last,
             body_sha256=sha(body), local_selection=str(out.relative_to(ROOT)),
             description=desc, selection_is_full_printed_proof_unit=full,
             used_as_foundation=used, nested_citations_are_not_reproved=True)
    manifest.append(m)
    blocks.append('\n## ' + sid + '\n\n' + desc + '\n\n'
                  + f"Source `{m['source']}`; SHA-256 `{m['source_sha256']}`. "
                  + f"Inclusive literal LF lines {first}--{last}; body SHA-256 `{m['body_sha256']}`. "
                  + 'OCR/control bytes are retained. Printed proof units remain external foundations, '
                  + 'not certification of the new applications.\n\n```text\n'
                  + body.decode('utf-8') + '\n```\n')
(ROOT / 'evidence/source-selections.json').write_text(json.dumps(manifest, indent=2) + '\n')

intro = '''# P06.2: specified semistable-tree ordinary regularization

This is the authoritative, self-contained author draft. Status: **partial**;
candidate: **false**. The claimed conditional theorem concerns a supplied
actual connected rig-smooth strict affinoid over an algebraically closed
complete nontrivially valued field, its supplied simply semistable model
with metric-tree skeleton, and a supplied real harmonic skeletal function.
It gives ordinary CLD-smooth decreasing psh approximants for both signs on
the entire actual analytic interior, continuous on the affinoid, hence on
every SAME supplied compact strict affinoid Y inside that interior.

The original task and completion criteria remain exactly in `input.json`.
Original P06.2 and its all-curve gate remain open. P05.2 is untouched.
The proof does not infer factorization, a tree, a model, or harmonicity from
a continuous current equation. It does not use completed-current transport,
normalization, nilpotents, Wanner recognition, the book's claimed theorem,
a prior PASS, or an old note as a mathematical theorem grant.

The new proof includes an exact residual divisor construction, a quotient of
GLOBAL analytic functions realizing that residual function, finite exceptional
directions, an explicit common ORDINARY open star, correct one-node slope
applications, full annular-fibre equalities, all-direction control, caps
excluding their vertex with a strict error margin and new plateau, exact
ordinary-open overlap gluing, and calibrated positivity against every
nonnegative compact ordinary test. Both sequences use the entire fixed Z.
Old tree/cap/tail diagnostics are reproved as supporting calculations and
are not presented as new analytic results.

All used new supporting proofs appear below in the complete standalone TeX
body, followed by complete selected primary bodies. The TeX body is readable
source, not an inaccessible external proof pointer. Three standard printed
foundations (BGR affinoid algebra facts, the étale Jacobian criterion in EGA,
and Hartshorne Riemann--Roch) are stated exactly, cited, and applied in that
body. Their archival books were not installed here, are not redistributed,
and have no claimed local source hash. The analytic Newton application and
every NEW application are proved directly. Installed Thuillier, CLD, GJR, van der Put and Berkovich
body hashes and exact LF coordinates follow; a definition or a scope statement
is explicitly distinguished from a complete proof unit.

The draft is not independently verified. Author audit, source identities,
structural checks and two successful TeX builds do not establish mathematical
correctness. `bash reproduce.sh` rebuilds selected-body access, two PDF passes,
and integrity/schema evidence using small local operations only. All new
files remain in this fresh workspace; old files are read only.

# Complete new argument and standalone paper source

```tex
'''
paper = (ROOT / 'P06.2-partial.tex').read_text()
(ROOT / 'P06.2-argument.md').write_text(intro + paper + '\n```\n\n# Selected primary bodies\n' + ''.join(blocks))
# Retain only selected units, not copies of entire archival monographs.
for name in sources:
    copied = ROOT / 'sources' / name
    if copied.exists():
        copied.unlink()
print(json.dumps(dict(selected_units=len(manifest),
                      authoritative_bytes=(ROOT / 'P06.2-argument.md').stat().st_size,
                      lf_coordinates_only=True)))
