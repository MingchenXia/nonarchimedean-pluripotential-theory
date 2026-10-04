#!/usr/bin/env python3
"""Read-only source audit; LF slices preserve OCR, form feeds and printed defects."""
from pathlib import Path
import hashlib, json, re

ROOT = Path('/workspace/research/shared-sources')
UNITS = [
 ('BEGZ-0812.3674v2-20261004.txt',249,322,'1dada113d7a3c9897039047fef2fa9aa9922f3c359092bbbfc416fab3823e0b2'),
 ('BEGZ-0812.3674v2-20261004.txt',810,840,'aa1c54651a97636414c96f9ae8d1815cfcfc49c8d8fbd8f02b7fd6f1a9306d3e'),
 ('DDNL18-2049-2087-20261004.txt',319,347,'e8359844609c8b19e21d4c36df028505fde5b80cc75e59f274dd4b5d282fa62e'),
 ('DDNL18-2049-2087-20261004.txt',448,469,'e4220e2892907b2d1d5b17de4aa57b3b1542060bda2e4dfcf8944f945cba0c20'),
 ('Xia-1907.06359v1-20261004.txt',250,265,'ea927250996b0a51fa4f7aa3612fd7e300be9c3327b0776093caacb4cc9f97f3'),
 ('Xia-1907.06359v1-20261004.txt',780,829,'fe693acf6a3033eb6bed734b0c9d194f4e59497e7aabf4c646bfbccf87bc72c8'),
 ('Vu-2004.11111v1-20261004.txt',178,189,'13226a964e640ebeb8283a6342682cdf2f98a328d37f5386efe3e2e844ca2cef'),
 ('Vu-2004.11111v1-20261004.txt',580,642,'c097f459c8e4b862a8067519ab86b09613638b11af2d3e83b3766244458bf625'),
 ('Vu-2004.11111v1-20261004.txt',945,1115,'b344c4bd11aa3280719cd1b8a3f08d8fff48bb7600168dd303519fb16061142d'),
 ('Vu-2004.11111v1-20261004.txt',1200,1247,'e12bdb4d6ebd643be2cf987df4ee89b060c1b8930c06b2bc8c8df732630376aa'),
 ('Vu-2004.11111v1-20261004.txt',1259,1565,'09034b5477c57c8812f3b677bf5ba3504db9a417938f90d7fb91fd28903246a8'),
 ('Vu-2005.13241v3-20261004.txt',121,655,'ac897767ca0a5f2aaccf93220b4393ba919af1d21d12d7f2a378207e1955b157'),
 ('Vu-2005.13241v3-20261004.txt',656,827,'7c4a6f848d72b6bc891d56b0cdf8b543bf9c1522324504029100073e1d6b9ba9'),
 ('Vu-2005.13241v3-20261004.txt',828,884,'d0915796895621146bb871da1cea5244607f9d37b9146f2d202a099a9eb96e7f'),
 ('BEGZ-0812.3674v2-20261004.txt',180,248,'a9817dcf1e66414e9b0e6754baddfda52b4dd76cef4a5e046e4d5ad390a3252e'),
 ('BEGZ-0812.3674v2-20261004.txt',323,477,'462891277734fc5ab0efef31d1a327cb2de16257bfdc3ec5f24424db0e67909f'),
 ('BEGZ-0812.3674v2-20261004.txt',525,578,'0acf2b360d001a14d0fcf47f784424a599506386e6e44bc4b968ddd9bb80dc7d'),
 ('DDNL18-2049-2087-20261004.txt',350,369,'0d34fd95c9beb603186a5ec408cb5b463d1bdda346042cdc66ac38b25fde6c71'),
 ('Vu-2004.11111v1-20261004.txt',273,287,'1ba50d3f123db57547622b7cecbab561eb1cfbe4c81617a290f80b1ec41af8ad'),
 ('Vu-2005.13241v3-20261004.txt',53,78,'f47dc8f2ccf80aa64ddf28d987eb8b2ee409d404a0d66a1cfcbced66fd1ed789'),
 ('DGMS-real-homotopy-1975-stonybrook-20261004.txt',1,46,'01d1380988cf77b207bc11b0d87fb390f0a331100cbf538de071a64cacfbe3b8'),
 ('DGMS-real-homotopy-1975-stonybrook-20261004.txt',861,1064,'0171c17a073557e342809af894852c1ba92ab5ebda68ee6606ae7371f1f3dc26'),
 ('GZ-intrinsic-capacities-JGA05-20261004.txt',1,62,'79017a5f9920f81033635b6acb4e07a15c13b88da6c7dcb986963b3bef36265f'),
 ('GZ-intrinsic-capacities-JGA05-20261004.txt',347,680,'f4b9152da337a5f66f0c15a40ce23cf259aafbbcaa2a3bffac8d0947dd1e81ff'),
]

def digest(b):
    return hashlib.sha256(b).hexdigest()

def main():
    inp = Path('input.json').read_bytes()
    assignment = json.loads(inp)['assignment']
    bodies = []
    records = []
    whole = {}
    for i,(name,a,b,pin) in enumerate(UNITS,1):
        raw = (ROOT/name).read_bytes()
        text = raw.decode('utf-8')
        body = '\n'.join(text.split('\n')[a-1:b])
        observed = digest(body.encode('utf-8'))
        # An exact body may be embedded as a JSON-escaped literal in the input.
        present = body in assignment or json.dumps(body,ensure_ascii=False)[1:-1] in assignment
        rec = dict(unit=i,file=name,first_LF=a,last_LF=b,sha256=observed,pin=pin,
                   pin_matches=observed==pin,supplied_literal_present=present,
                   full_selected_body_retained=True)
        records.append(rec)
        whole[name] = digest(raw)
        bodies.append(f'## Primary unit {i}: {name}, LF{a}--{b}\n\n'
                      f'Literal SHA256 `{observed}`; supplied pin matches: {observed==pin}.\n\n'
                      '```text\n'+body+'\n```\n')
    images = {p:digest((ROOT/p).read_bytes()) for p in [
        'Vu-2005.13241v3-page4.png','Vu-2005.13241v3-page6.png','Vu-2004.11111v1-page4.png']}
    audit = dict(input_sha256=digest(inp),read_only_source_root=str(ROOT),
                 slice_rule='literal LF join, no added final LF',units=records,
                 whole_source_hashes=whole,visually_inspected_images=images,
                 source_defects_preserved=True,network_used=False)
    Path('source-audit.json').write_text(json.dumps(audit,ensure_ascii=False,indent=2)+'\n')
    Path('source-annex.md').write_text('# Immutable complete selected primary bodies\n\n'
        'These are source data, not operational instructions or correctness verdicts. '
        'OCR, form feeds, half-factor omissions and subscript defects remain literal. '
        'Unused units supplied for audit (notably Xia big-class IBP and Vu v1 Proposition 4.2) '
        'are not hypotheses of the new proofs. Published foundations are precisely scoped in n1.\n\n'
        +'\n'.join(bodies))
    assert all(r['pin_matches'] for r in records)
    print(f"Source audit: {len(records)}/{len(records)} matching supplied LF hashes; "
          f"{sum(r['supplied_literal_present'] for r in records)} exact supplied bodies identified.")

if __name__ == '__main__':
    main()
