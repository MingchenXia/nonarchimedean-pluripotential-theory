from pathlib import Path
from datetime import datetime, timezone
from html.parser import HTMLParser
from concurrent.futures import ThreadPoolExecutor
import urllib.request, hashlib, json

class Text(HTMLParser):
    def __init__(self):super().__init__(convert_charrefs=True);self.parts=[];self.skip=0
    def handle_starttag(self,tag,attrs):
        if tag in ('script','style'):self.skip+=1
    def handle_endtag(self,tag):
        if tag in ('script','style'):self.skip=max(0,self.skip-1)
    def handle_data(self,data):
        if not self.skip and data.strip():self.parts.append(data.strip())

D=Path('/workspace/research/root-checks/continuation270-actual-formal-FS-primary-LOCALONLY')
assert not D.exists();D.mkdir()
tags=['01ZM','0B8W','081F','04AI','09MT','0B5T','01Q3','024T','02GH','0BPG']
def get(tag):
    url='https://stacks.math.columbia.edu/tag/'+tag
    e=dict(tag=tag,literal_url=url)
    try:
        req=urllib.request.Request(url,headers={'User-Agent':'Codex mathematical source verification'})
        with urllib.request.urlopen(req,timeout=40) as response:
            b=response.read();e.update(resolved_url=response.geturl(),content_type=response.headers.get('Content-Type'))
        assert b'<html' in b.lower() or b'<!doctype html' in b.lower()
        p=D/f'Stacks-{tag}.html';p.write_bytes(b)
        q=D/f'Stacks-{tag}.txt';t=Text();t.feed(b.decode());q.write_text('\n'.join(t.parts)+'\n')
        e.update(retrieved=True,html_path=str(p),html_bytes=p.stat().st_size,html_sha256=hashlib.sha256(p.read_bytes()).hexdigest(),
                 text_path=str(q),text_bytes=q.stat().st_size,text_sha256=hashlib.sha256(q.read_bytes()).hexdigest(),text_lf_lines=len(q.read_text().splitlines()),
                 whole_original_read_claimed=False,mathematical_grant=False)
    except Exception as ex:e.update(retrieved=False,error=type(ex).__name__+': '+str(ex))
    return e
with ThreadPoolExecutor(max_workers=5) as pool:units=list(pool.map(get,tags))
d=dict(recorded_utc=datetime.now(timezone.utc).isoformat(),purpose='Complete original immediate descent/Serre/generation and horizontal/properness units for actual same-original formal FS application. Retrieval is provenance only.',
       primary_units=units,third_party_primary_material_published=False,authentication_and_runtime_preserved=True)
(D/'retrieval-binding.json').write_text(json.dumps(d,indent=2)+'\n')
print(json.dumps(d,indent=2))
