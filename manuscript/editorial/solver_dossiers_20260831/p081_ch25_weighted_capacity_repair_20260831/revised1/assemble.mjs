import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import {fileURLToPath} from 'node:url';
import {spawnSync} from 'node:child_process';
const packet=path.dirname(fileURLToPath(import.meta.url)),parent=path.dirname(packet);
const hash=s=>crypto.createHash('sha256').update(s).digest('hex');
const source=path.join(parent,'patched/ch25_capacity.tex');
const before=fs.readFileSync(source,'utf8');
if(hash(before)!=='bc939ba01e4763debb7d73b4d6681592ea70229a7c42814c8c59384b3b4cb1ce') throw Error('parent changed');
let text=before;const changes=[];
function replace(oldText,newText,note){
 if(text.split(oldText).length!==2)throw Error(`nonunique ${note}`);
 text=text.replace(oldText,newText);changes.push({note,before:hash(oldText),after:hash(newText)});
}
replace(String.raw`is not uniform over divisorial points: on a segment of resistance length
\(\ell\) with \(m_0=m_1=1\), the midpoint has capacity
\(4/\ell\) once \(\ell\geq2\)
(\Cref{prop:ch25-segment-capacities}), which tends to \(0\) as the thickness
of the node grows.  So \Cref{lem:divisorial-positive-capacity} is a
qualitative statement, and every quantitative use of it below is made at one
fixed point.`,String.raw`is not uniform over divisorial points, even for one fixed reference:
\Cref{ex:ch25-fixed-reference-small-capacities} constructs points on
\(\mathbf P^1_K\), with its fixed standard \(\cO(2)\) model form, whose
capacities are \(1/N\).  Thus \Cref{lem:divisorial-positive-capacity}
is qualitative, and every quantitative use of it below is made at one
fixed point.`,'fixed-reference quantifier in preliminary remark');
replace(String.raw`\begin{example}[A nonsplit node changes capacity]`,String.raw`\begin{example}[A non-rational node changes capacity]`,'residue terminology');
replace(String.raw`also \(2\).  The next example shows that the coincidence is an artefact of
the short edge.`,String.raw`also \(2\).  Here both the point and its tube have full capacity \(V\).
It is equality with the total mass, not equality of point and tube
capacities, that the next longer-edge example need not preserve.`,'distinguish full mass from point-tube equality');
const old=String.raw`Two consequences are worth recording.  First, the capacity of a divisorial
point is \emph{not} bounded below uniformly: replacing the four-edge chain
by a chain of unit-weight edges of total resistance length \(\ell\)
and taking \(c=\ell/2\) gives
\(\Capa_\theta(p^{-1}(\{x_{\ell/2}\}))=4/\ell\) as soon as
\(\ell\geq2/m_0\) and \(\ell\geq2/m_1\), which tends to \(0\) as
\(\ell\to\infty\).  Along even integral \(\ell\), the midpoint is the
divisorial vertex of an intermediate component, and the maximizing kink
puts the whole displayed tube mass at that vertex; hence its singleton has
the same capacity \(4/\ell\).  Thus
\Cref{lem:divisorial-positive-capacity} is not
quantitative in any uniform sense, and the caveat in
\Cref{rem:ch25-divisorial-explicit} is real.  Second, a proper closed subset
can already have full capacity: \(\Capa_\theta(p^{-1}([1,3]))=V\) while
\(p^{-1}([1,3])\neq C^{\An}\).
\end{example}
`;
const replacement=String.raw`A proper closed subset can already have full capacity:
\(\Capa_\theta(p^{-1}([1,3]))=V\), although
\(p^{-1}([1,3])\neq C^{\An}\).  The symmetric segment calculation also
gives midpoint capacity \(4/\ell\) for endpoint masses one and total
resistance length \(\ell\geq2\).  Varying such reference data alone
does not prove nonuniformity on a single fixed curve with a fixed form;
the next example supplies that stronger conclusion.
\end{example}

`+fs.readFileSync(path.join(packet,'fixed_reference_example.tex'),'utf8')+'\n';
replace(old,replacement,'replace varying-reference inference by explicit fixed-pair proof');
const oldLabels=[...before.matchAll(/\\label\{([^}]+)\}/g)].map(m=>m[1]);
const newLabels=[...text.matchAll(/\\label\{([^}]+)\}/g)].map(m=>m[1]);
if(oldLabels.some(x=>!newLabels.includes(x)))throw Error('lost label');
const dest=path.join(packet,'patched/ch25_capacity.tex');fs.mkdirSync(path.dirname(dest),{recursive:true});fs.writeFileSync(dest,text,{flag:'wx'});
const live='/private/tmp/nappt_p071_20260827/manuscript/parts/part3/ch25_capacity.tex';
const diff=spawnSync('git',['diff','--no-index','--',live,dest],{encoding:'utf8'});
if(![0,1].includes(diff.status))throw Error(diff.stderr);
fs.writeFileSync(path.join(packet,'chapter.patch'),diff.stdout,{flag:'wx'});
const files=['GATE.md','assemble.mjs','fixed_reference_example.tex','chapter.patch','patched/ch25_capacity.tex'].map(name=>{const b=fs.readFileSync(path.join(packet,name));return {name,bytes:b.length,sha256:hash(b)};});
const manifest={date:'2026-08-31',status:'isolated pending verification',source,sourceSha256:hash(before),oldLabels:oldLabels.length,newLabels:newLabels.length,changes,files};
fs.writeFileSync(path.join(packet,'MANIFEST.json'),JSON.stringify(manifest,null,2)+'\n',{flag:'wx'});
console.log(JSON.stringify(manifest,null,2));
