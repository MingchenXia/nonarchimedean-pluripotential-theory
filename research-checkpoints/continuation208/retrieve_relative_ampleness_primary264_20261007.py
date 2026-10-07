from pathlib import Path
from datetime import datetime, timezone
import hashlib,json,urllib.request
from html.parser import HTMLParser

class PrimaryText(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True); self.parts=[]; self.skip=0
    def handle_starttag(self,tag,attrs):
        if tag in ('script','style'): self.skip+=1
    def handle_endtag(self,tag):
        if tag in ('script','style'): self.skip=max(0,self.skip-1)
    def handle_data(self,data):
        if not self.skip and data.strip(): self.parts.append(data.strip())

D=Path('/workspace/research/root-checks/continuation264-relative-ampleness-primary-LOCALONLY')
assert not D.exists(); D.mkdir()
out=dict(recorded_utc=datetime.now(timezone.utc).isoformat(),purpose='Original Stacks immediate proper-fiber ampleness units and proper field-curve degree criterion; retrieval alone does not certify reading or an application.',primary_units=[],full_primary_published=False,no_auth_or_runtime_change=True)
for tag in ['0D2S','0D2N','0AYQ','0B5X']:
    url='https://stacks.math.columbia.edu/tag/'+tag
    e=dict(tag=tag,literal_url=url)
    try:
        req=urllib.request.Request(url,headers={'User-Agent':'Codex mathematical primary-source reading'})
        with urllib.request.urlopen(req,timeout=40) as response:
            data=response.read();e.update(resolved_url=response.geturl(),content_type=response.headers.get('Content-Type'))
        assert b'<html' in data.lower() or b'<!doctype html' in data.lower()
        html=D/('Stacks-'+tag+'.html');html.write_bytes(data)
        parser=PrimaryText(); parser.feed(data.decode('utf-8'))
        txt=D/('Stacks-'+tag+'.txt');txt.write_text('\n'.join(parser.parts)+'\n')
        e.update(retrieved=True,html_path=str(html),html_bytes=len(data),html_sha256=hashlib.sha256(data).hexdigest(),text_path=str(txt),text_bytes=txt.stat().st_size,text_sha256=hashlib.sha256(txt.read_bytes()).hexdigest(),text_lf_lines=len(txt.read_text().splitlines()),whole_unit_read_claimed=False)
    except Exception as ex:
        e.update(retrieved=False,error=type(ex).__name__+': '+str(ex))
    out['primary_units'].append(e)
(D/'retrieval-binding.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
