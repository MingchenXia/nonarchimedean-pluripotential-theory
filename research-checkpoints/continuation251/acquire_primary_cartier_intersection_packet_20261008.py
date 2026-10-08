from pathlib import Path
from datetime import datetime,timezone
from concurrent.futures import ThreadPoolExecutor
from html.parser import HTMLParser
import hashlib,json,urllib.request

P=Path('/workspace/research/primary-data-LOCALONLY/P12.4-local-cartier-intersections-20261008')
assert not P.exists();P.mkdir(parents=True)
class Visible(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True);self.skip=0;self.parts=[]
    def handle_starttag(self,tag,attrs):
        if tag in ['script','style']:self.skip+=1
        elif not self.skip and tag in ['p','div','li','h1','h2','h3','h4','br','tr']:self.parts.append('\n')
    def handle_endtag(self,tag):
        if tag in ['script','style'] and self.skip:self.skip-=1
        elif not self.skip and tag in ['p','div','li','h1','h2','h3','h4','tr']:self.parts.append('\n')
    def handle_data(self,data):
        if not self.skip:self.parts.append(data)
def fetch(tag):
    url='https://stacks.math.columbia.edu/tag/'+tag
    with urllib.request.urlopen(url,timeout=30) as response:
        assert response.status==200
        data=response.read();headers=dict(response.headers)
    html_path=P/(tag+'.html');html_path.write_bytes(data)
    parser=Visible();parser.feed(data.decode('utf-8'));parser.close()
    text='\n'.join(line.strip() for line in ''.join(parser.parts).split('\n') if line.strip())+'\n'
    text_path=P/(tag+'.txt');text_path.write_text(text)
    return dict(tag=tag,url=url,acquired_utc=datetime.now(timezone.utc).isoformat(),
        html_path=str(html_path),html_bytes=len(data),html_sha256=hashlib.sha256(data).hexdigest(),
        text_path=str(text_path),text_bytes=text_path.stat().st_size,text_sha256=hashlib.sha256(text_path.read_bytes()).hexdigest(),
        headers={k:v for k,v in headers.items() if k.lower() in ['content-type','last-modified','etag']},
        reading_or_correctness_claim=False,source_body_publish=False)
tags=['0BEL','0AG7','01OF','0AYA','02QL']
with ThreadPoolExecutor(max_workers=3) as pool:records=list(pool.map(fetch,tags))
(P/'acquisition-records.json').write_text(json.dumps(records,indent=2)+'\n')
print(json.dumps(dict(directory=str(P),sources=[dict(tag=e['tag'],html_bytes=e['html_bytes'],text_bytes=e['text_bytes']) for e in records],source_bodies_publish=False),indent=2))
