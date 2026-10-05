from pathlib import Path
import re
D=Path('/workspace/research/deliverables/scoped-P15.3-round120')
p=D/'P15.3-argument.md'; text=p.read_text()
a=text.index('## 9.'); b=text.index('## 15.')
section=text[a:b]
pairs={
 'Let M be':r'Let $M$ be', 'on M':r'on $M$', 'on X':r'on $X$', 'curve E':r'curve $E$',
 'no curves, as in Sections 3--4': 'no curves, as in Sections 3--4',
 'form beta of rank1, with beta^2=0':r'form $\beta$ of rank one, with $\beta^2=0$',
 'form gamma on $M$':r'form $\gamma$ on $M$',
 'Let pi:X -> M':r'Let $\pi:X\to M$', 'E^2=-1':r'$E^2=-1$',
 'Fix a>0 with a^2<d':r'Fix $a>0$ with $a^2<d$',
 'any q in E':r'any $q\in E$', 'X superset E superset {q}':r'$X\supset E\supset\{q\}$',
 'epsilon>0':r'$\epsilon>0$', 'H_epsilon':r'$H_\epsilon$',
 'reference0':r'reference zero', 'near q':r'near $q$',
 'pullback of beta':r'pullback of $\beta$', 'pairs to zero with E':r'pairs to zero with $E$',
 'form eta on $M$, let V=integral_M eta^2':r'form $\eta$ on $M$, let $V=\int_M\eta^2$',
 'small r>0':r'small $r>0$', 'O(-E)':r'$\mathcal O(-E)$', 'pi*eta':r'$\pi^*\eta$',
 'near E':r'near $E$', 'small r their':r'small $r$ their',
 'interval0<r<sqrt(V)':r'interval $0<r<\sqrt V$', 'V-r^2':r'$V-r^2$',
 'intersection r with E':r'intersection $r$ with $E$', 'cycles on $X$':r'cycles on $X$',
 'particular Omega':r'particular $\Omega$', 'a epsilon<sqrt(V_epsilon)':r'$a\epsilon<\sqrt{V_\epsilon}$',
 'current S has class pi*[eta]-b{E} with b>=0':r'current $S$ has class $\pi^*[\eta]-b\{E\}$ with $b\geq0$',
 'of K_r for0<r<sqrt(V)':r'of $K_r$ for $0<r<\sqrt V$',
 'r increase to sqrt(V)':r'$r$ increase to $\sqrt V$', 'b<=sqrt(V)':r'$b\leq\sqrt V$',
 'at each r':r'at each $r$', 'divisor E':r'divisor $E$',
 'Set s_epsilon=sqrt(V_epsilon)-a epsilon>0':r'Set $s_\epsilon=\sqrt{V_\epsilon}-a\epsilon>0$',
 'current T whose':r'current $T$ whose', 'Let t=nu(T,E)':r'Let $t=\nu(T,E)$',
 'S=T-t[E]>=0':r'$S=T-t[E]\geq0$',
 'class pi*[eta_epsilon]-(a epsilon+t){E}':r'class $\pi^*[\eta_\epsilon]-(a\epsilon+t)\{E\}$',
 'a epsilon+t<=sqrt(V_epsilon)':r'$a\epsilon+t\leq\sqrt{V_\epsilon}$',
 't<=s_epsilon':r'$t\leq s_\epsilon$', 'current on E':r'current on $E$',
 'along E is0':r'along $E$ is zero', 'intersection with E':r'intersection with $E$',
 'a epsilon+t':r'$a\epsilon+t$', 'mass y at q':r'mass $y$ at $q$',
 'rational t with0<=t<s_epsilon and rational y with0<=y<':r'rational $t$ with $0\leq t<s_\epsilon$ and rational $y$ with $0\leq y<$',
 'restriction to E':r'restriction to $E$', 'On E=P1':r'On $E=\mathbb P^1$',
 'form omega_E':r'form $\omega_E$', 'coefficient y at q':r'coefficient $y$ at $q$',
 'class of F_t':r'class of $F_t$', 'current S in F_t with S|E=R':r'current $S\in F_t$ with $S|_E=R$',
 'delta>0 with F_t-delta{E}':r'$\delta>0$ with $F_t-\delta\{E\}$',
 'Therefore S':r'Therefore $S$', 'pole on E':r'pole on $E$', 'current t[E] gives T=S+t[E]':r'current $t[E]$ gives $T=S+t[E]$',
 'valuation(t,y)':r'valuation $(t,y)$', 't=s_epsilon and y=':r'$t=s_\epsilon$ and $y=$',
 'vertices are(0,0),(s_epsilon,0),(s_epsilon,sqrt(V_epsilon)),(0,a epsilon)':r'vertices are $(0,0)$, $(s_\epsilon,0)$, $(s_\epsilon,\sqrt{V_\epsilon})$, $(0,a\epsilon)$',
 'epsilon^(-1/2)':r'$\epsilon^{-1/2}$', 'dimension is2':r'dimension is two',
 'class pi*[beta] has numerical dimension1':r'class $\pi^*[\beta]$ has numerical dimension one',
 'with Omega':r'with $\Omega$', 'square is0':r'square is zero',
 'epsilon^(-p) and epsilon^(-q)':r'$\epsilon^{-p}$ and $\epsilon^{-q}$',
 'sqrt(2c epsilon)':r'$\sqrt{2c\epsilon}$', 'p,q<=1/2':r'$p,q\leq1/2$',
 'equal1/2':r'equal $1/2$', 'p=1/2 and q<1/2':r'$p=1/2$ and $q<1/2$',
 'q=1/2 and p<1/2':r'$q=1/2$ and $p<1/2$',
 'horizontal interval[0,sqrt(2c)] times{0}':r'horizontal interval $[0,\sqrt{2c}]\times\{0\}$',
 'vertical interval{0} times[0,sqrt(2c)]':r'vertical interval $\{0\}\times[0,\sqrt{2c}]$',
 'greater than1/2':r'greater than $1/2$', 'c=integral beta gamma':r'$c=\int_M\beta\wedge\gamma$',
 'Replacing Omega by b Omega':r'Replacing $\Omega$ by $b\Omega$', 'by sqrt(b)':r'by $\sqrt b$',
 'of gamma and a':r'of $\gamma$ and $a$', 'Fix p in M':r'Fix $p\in M$',
 'pi: X=Bl_p M -> M':r'$\pi:X=\operatorname{Bl}_pM\to M$', 'cutoff chi':r'cutoff $\chi$',
 'form kappa_form':r'form $\kappa$', 'with exceptional E':r'with exceptional $E$',
 'small a>0':r'small $a>0$', 'kappa_form+dd^c u_a':r'$\kappa+dd^c u_a$',
 'dd^c log|z|^2':r'$dd^c\log|z|^2$', 'chi=1':r'$\chi=1$', 'dd^c f':r'$dd^cf$',
 'rational a':r'rational $a$', 'with beta_a a':r'with $\beta_a$ a',
 'chart z_1=w, z_2=wt':r'chart $z_1=w$, $z_2=wt$',
 'a log|w|^2+a log(1+|t|^2)':r'$a\log|w|^2+a\log(1+|t|^2)$',
 'Subtraction of a[E]':r'Subtraction of $a[E]$',
 'pi^*kappa_form+a dd^c log(1+|t|^2)':r'$\pi^*\kappa+a\,dd^c\log(1+|t|^2)$',
 'on E the':r'on $E$ the', 'small a gives':r'small $a$ gives',
 'beta_a is the pullback of kappa_form where pi':r'$\beta_a$ is the pullback of $\kappa$ where $\pi$',
}
# Substitute once using the original longest matching tokens, only outside math.
pattern=re.compile('|'.join(re.escape(k) for k in sorted(pairs,key=len,reverse=True)))
parts=re.split(r'(\$\$[\s\S]*?\$\$|\$[^$]*\$)',section)
section=''.join(s if i%2 else pattern.sub(lambda m:pairs[m.group()],s) for i,s in enumerate(parts))
# Two longer replacements containing tokens expanded above need final cleanup.
section=section.replace('rational t with0<=t<s_epsilon and rational y with0<=y<$a\\epsilon+t$',r'rational $t$ with $0\leq t<s_\epsilon$ and rational $y$ with $0\leq y<a\epsilon+t$')
section=section.replace('$0\\leq y<$'+'$a\\epsilon+t$',r'$0\leq y<a\epsilon+t$')
section=section.replace('$y=$'+'$a\\epsilon+t$',r'$y=a\epsilon+t$')
section=section.replace('form gamma on M',r'form $\gamma$ on $M$')
section=section.replace('    f=chi log(|z_1|^2+|z_2|^2), u_a=a f.',r'$$f=\chi\log(|z_1|^2+|z_2|^2),\qquad u_a=af.$$')
section=section.replace('    pi^*(kappa_form+dd^c u_a)=beta_a+a[E],\n    [beta_a]=kappa_a=pi^*kappa-a[E],                            (3.1)',r'$$\pi^*(\kappa+dd^c u_a)=\beta_a+a[E],\qquad[\beta_a]=\pi^*[\kappa]-a\{E\}.\tag{3}$$')
# Preserve the correct full mathematical phrase if smaller lexical substitutions
# made the originally indented equation ineligible for the previous replacement.
section=re.sub(r'^    pi\^\*\(.*?\n    \[beta_a\].*?\(3\.1\)',lambda m:r'$$\pi^*(\kappa+dd^c u_a)=\beta_a+a[E],\qquad[\beta_a]=\pi^*[\kappa]-a\{E\}.\tag{3}$$',section,flags=re.M)
section=section.replace('This proves (3.1)', 'This proves (3)')
p.write_text(text[:a]+section+text[b:])
print('Typeset the accepted exact-body proof and blowup equations without changing scope.')
