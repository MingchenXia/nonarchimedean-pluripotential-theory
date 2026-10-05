#!/usr/bin/env python3
"""Optional small primary PDF transport probe; not required by offline rerun.py."""
import json, pathlib, sys, urllib.request, hashlib
root=pathlib.Path(__file__).resolve().parent
(root/'logs').mkdir(exist_ok=True)
url='https://arxiv.org/pdf/2206.07183v2'
out={'argv':[sys.executable,'network_probe.py'],'url':url,'purpose':'Record whether original primary PDF bytes are actually available; never invent a PDF hash.'}
try:
    with urllib.request.urlopen(url,timeout=5) as r:
        blob=r.read(2000000)
    if not blob.startswith(b'%PDF-'):raise ValueError('Response is not PDF bytes')
    p=root/'public-primary/BJ-addendum-original.pdf';p.write_bytes(blob)
    out.update(success=True,artifact=str(p.relative_to(root)),bytes=len(blob),sha256=hashlib.sha256(blob).hexdigest())
except Exception as e:
    out.update(success=False,exception_type=type(e).__name__,exception=str(e))
(root/'logs/network-probe.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,sort_keys=True))
