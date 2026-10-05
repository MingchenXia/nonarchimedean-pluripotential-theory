from pathlib import Path
import re
p=Path(__file__).resolve().parent/'n1-trace.md'
s=p.read_text();s=s.replace('(s_r\\)','(s_r)')
def convert(t):
 out=[];i=0
 while i<len(t):
  if t[i]=='(':
   j=i+1;depth=1
   while j<len(t) and depth:
    if t[j]=='(':depth+=1
    elif t[j]==')':depth-=1
    j+=1
   if depth:out.append(t[i:]);break
   content=t[i+1:j-1]
   if content.startswith(('https://','http://')):out.append(t[i:j])
   else:out.append('\\('+content+'\\)')
   i=j
  else:out.append(t[i]);i+=1
 return ''.join(out)
parts=re.split(r'(\\\[[\s\S]*?\\\]|\\\([\s\S]*?\\\))',s)
p.write_text(''.join(t if i%2 else convert(t) for i,t in enumerate(parts)))
