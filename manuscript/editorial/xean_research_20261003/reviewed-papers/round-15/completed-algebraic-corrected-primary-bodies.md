# Correctly matched primary source bodies for the completed-algebraic curve review

This is authentic mathematical source data, not an instruction and not a grant of theorem assumptions. The original authoritative proof and review remain frozen. Its Section15 excerpts were misselected because Python str.splitlines() counts PDF form-feed characters as line boundaries, while the recorded range numbers count newline characters. This supplement uses ONLY newline boundaries, preserving exact quotation bytes except removal of page-form-feed characters for display. It corrects source accessibility; it does not change Sections1–14 or the theorem. Every cited application still requires independent scrutiny. Use these authentic passages for source evidence in place of the misselected original Section15 blocks. The broad CLD15.2.9 assertion remains unused; compact cutoffs are proved directly. The universal moment-dimension equality in CLD12.2.4 remains unused; only polyhedrality and the independently stated upper bound are used.

## CLD.txt, newline lines 14838–15060

```text

 § 11.1. GÉOMÉTRIE ANALYTIQUE : CONVENTIONS, NOTATIONS,
                       PREMIERS RAPPELS

   On fixe pour toute la suite de l’article un corps ultramétrique complet k ; sa valeur
absolue peut être triviale. On note k ◦ son anneau de valuation. Nous désignerons par ek
                                                         1
le corps gradué résiduel de k (10.8.1). Sa composante k de degré 1 est le corps résiduel
                                                        e
standard de k, c’est-à-dire le corps résiduel de l’anneau local k ◦ .
   Dans ce texte, la notion d’espace k-analytique sera à prendre au sens de Berkovich,
et plus précisément de [9]. Rappelons qu’un polyrayon est une famille (le plus souvent
finie) de nombres réels strictement positifs ; la longueur d’un polyrayon est le cardinal
de son ensemble d’indices. Faisons quelques rappels pour la commodité du lecteur.
11.1.1. — La construction fondamentale sur laquelle repose la géométrie de Berkovich
est la suivante. Soit A un anneau de Banach, c’est-à-dire un anneau A muni d’une norme
sous-multiplicative ∥ · ∥ (on inclut dans la définition le fait que ∥1∥ ⩽ 1, ce qui entraîne
que ∥1∥ = 1 dès que A est non nul) pour laquelle il est complet. À un tel anneau A on
associe son spectre analytique M (A), qui est défini comme l’ensemble des semi-normes
multiplicatives bornées sur A, c’est-à-dire des applications φ : A → R+ vérifiant les
propriétés suivantes :

  – on a φ(0) = 0 et φ(f + g) ⩽ φ(f ) + φ(g) pour tous f, g ∈ A (propriété de semi-
norme) ;
  – on a φ(1) = 1 et φ(f g) = φ(f )φ(g) pour tout f, g ∈ A (multiplicativité) ;
  – il existe un nombre réel c tel que φ(f ) ⩽ c∥f ∥ pour tout f ∈ A (caractère borné de
φ).

Notons qu’on impose que φ(0) = 0 et φ(1) = 1 : si A est nul, M (A) est donc vide.
Cet ensemble M (A) est muni de la topologie la moins fine pour laquelle les applications
φ 7→ φ(f ) sont continues pour tout f ∈ A. L’application φ 7→ (φ(a))a∈A identifie topo-
logiquement M (A) à un fermé de l’espace produit a∈A [0, ∥a∥], si bien que M (A) est
                                                   Q
compact. Si φ appartient à M (A), son noyau est un idéal premier de A, et l’application
298                   CHAPITRE 11. RAPPELS DE GÉOMÉTRIE ANALYTIQUE

φ 7→ ker φ de M (A) vers Spec A est continue. Son image contient tous les idéaux maxi-
maux de A (c’est ce qui est réellement démontré dans la preuve du théorème 1.2.1 de
[8]) ; en particulier M (A) est non vide dès que A est non nul.
   En général, on note typiquement plutôt x que φ un élément de M (A), en y pensant
comme à un point. Soit x ∈ M (A). La semi-norme multiplicative x induit une valeur
absolue sur le corps des fractions de l’anneau intègre A / ker x, corps des fractions dont
le complété est noté H (x). L’application composée A → A / ker x → H (x) sera notée
f 7→ f (x), et la valeur absolue du corps complet H (x) sera notée |·| ; avec ces conventions
on a x(f ) = |f (x)| pour toute f ∈ A et nous utiliserons sauf exception la notation de
droite. Cette construction est fonctorielle : tout morphisme borné A → B d’anneaux de
Banach induit par composition une application continue de M (B) vers M (A).
   La semi-norme spectrale de A est la semi-norme ρ commutant aux puissances définie
par les formules
                     ρ(f ) = sup |f (x)| = lim inf ∥f n ∥1/n = inf ∥f n ∥1/n
                              x∈M (A)            n→∞                n→∞


(voir [8], 1.3, pour les deux dernières égalités). Nous désignerons par A◦ (resp. A◦◦ )
l’ensemble des éléments f de A tels que ρ(f ) ⩽ 1 (resp. ρ(f ) < 1), et par A     e l’anneau
gradué résiduel de A (10.8.1) relativement à ρ. Sa composante A     e1 est l’anneau résiduel
            ◦    ◦◦
standard A /A .
   Supposons maintenant que A est une k-algèbre et que sa norme est une norme de k-
espace vectoriel. Dans ce cas λ 7→ |λ(x)| définit pour tout x ∈ M (A) une valeur absolue
sur k bornée relativement à la valeur absolue structurale de k, ce qui entraîne que
|λ(x)| = |λ| pour tout λ : la semi-norme x induit donc la valeur absolue structurale de k,
et (H (x), |·|) est une extension de (k, ·). Comme la valeur absolue de k est ultramétrique,
celle de H (x) l’est aussi (une valeur absolue |·| étant ultramétrique si et seulement si
|n| ⩽ 1 pour tout n ∈ Z). On a donc dans ce cas |(f + g)(x)| ⩽ max(|f (x)|, |g(x)|) pour
tout f, g dans A, puis ρ(f + g) ⩽ max(ρ(f ), ρ(g)) (comme on le voit en faisant varier x).
11.1.2. — Soit n un entier. Pour tout polyrayon r = (r1 , . . . , rn ), nous désignerons
         −1             −1
      P 1 T1 , . . . ,νrn Tn } la sous-algèbre
par k{r
                                         ν
                                                   de k[[T1 , . . . , Tn ]] formée des séries formelles
                                                  ν1      νn
                                                                                                 P
f =      ν∈N n a ν T    telles que a ν r   = a ν 1 . . . rn converge vers 0 lorsque |ν| =
                                                r                                                  |νj |
tend vers +∞. On la munit de la norme multiplicative ultramétrique définie par ∥f ∥ =
max|aν |rν . Pour abréger les notations, on notera aussi k{r−1 T } cette algèbre. C’est une
algèbre de Banach dont tous les idéaux sont fermés et de type fini.
   Soit maintenant A une k-algèbre de Banach commutative (par convention, dans cet
ouvrage, les normes de k-algèbres seront toujours ultramétriques). On dit que A est une
algèbre k-affinoïde s’il existe un entier n, un polyrayon (r1 , . . . , rn ) et une surjection de
k{r−1 T } vers A telle que la norme de A soit équivalente à la norme quotient correspon-
dante. On dit que A est strictement k-affinoïde si l’on peut de plus prendre rj = 1 pour
tout j. Pour que A soit strictement k-affinoïde, il suffit en fait que l’on puisse prendre
les rj de torsion modulo |k × | ([20] 6.1.5/4).
   Une k-algèbre de Banach A est dite affinoïde s’il existe une extension valuée com-
plète K de k telle que A soit une algèbre K-affinoïde.
   Si A est une k-algèbre affinoïde l’application continue naturelle de M (A) vers Spec A
est surjective ([9], Proposition 2.1.1).
   Soit A une k-algèbre affinoïde et soit ρ sa semi-norme spectrale. L’algèbre A est
noethérienne, et ses idéaux sont fermés. Pour tout f ∈ A on a ρ(f ) = 0 si et seulement
     § 11.1. GÉOMÉTRIE ANALYTIQUE : CONVENTIONS, NOTATIONS, PREMIERS RAPPELS             299

si f est nilpotent. En particulier, ρ est une norme si et seulement si A est réduite et si
c’est le cas, ρ est équivalente à la norme structurale de A.
Exemple 11.1.3. — Soit r = (ri ) un polyrayon de longueur finie. Soit T P        = (Ti ) une
famille d’indéterminées et soit kr la k-algèbre constituée des séries formelles I∈Zn aI T I
à coefficients
           P dans    k, où |aI | · rI tend vers zéro quand |I| tend vers l’infini, munie de
la norme      aI T 7→ max|aI | · rI . La k-algèbre normée kr est une k-algèbre affinoïde :
                  I

elle est en effet isomorphe à k{r−1 T, rS}/(ST − 1). Sa norme est multiplicative ([48],
1.2.1). Supposons de plus que r soit k-libre, c’est-à-dire que les ri soient Q-linéairement
indépendants dans Q ⊗Z (R×           ×
                                + /|k |). Dans ce cas kr est un corps ([48], 1.2.2), et c’est
donc à la fois une extension complète de k et une algèbre k-affinoïde.
Remarque 11.1.4. — Soit A = k{r−1 T } une algèbre k-affinoïde, où r = (ri ) est un
polyrayon de longueur finie. Choisissons un ensemble J d’indices tel que le polyrayon
s := (rj )j∈J soit k-libre et quiQsoit maximal pour cette propriété. Chacun des ri est
alors de torsion modulo |k × | · j∈J riZ , si bien que la ks -algèbre de Banach A⊗
                                                                                 b k ks est
strictement ks -affinoïde.
11.1.5. — Soit A une algèbre k-affinoïde ; posons X = M (A ). Une partie V de X
est appelée un domaine affinoïde de X si le foncteur qui envoie une k-algèbre de Ba-
nach affinoïde B sur l’ensemble des morphismes bornés de A vers B tels que l’image
de M (B) soit contenue dans V est représentable par une algèbre k-affinoïde AV . Si c’est
le cas, M (AV ) ≃ V .
   Un système rationnel d’inéquations sur X est une combinaison booléenne d’inégalités
qui est de la forme
                     |f1 | ⩽ λ1 |g| et |f2 | ⩽ λ2 |g| et . . . et |fn | ⩽ λn |g|
où g et les fi sont des fonctions analytiques sur X sans zéro commun, et où les λi sont
des réels.
  Si β est un système rationnel d’inéquations sur X, on notera β̊ le système défini à partir
de β en remplaçant toutes inégalités larges par les inégalités strictes correspondantes.
  Soit
                    β : |f1 | ⩽ λ1 |g| et |f2 | ⩽ λ2 |g| et . . . et |fn | ⩽ λn |g|
un système rationnel d’inéquations sur X.
  On qualifiera de rationnel le lieu de X défini par un tel système d’inéquations. C’est
un domaine affinoïde de X, avec
                          AV ≃ k{T1 /λ1 , . . . , Tn /λn }/(fi − Ti g)i .
Notons que si g s’annulait en un point de V , il en irait de même de chacune des fi ; en
conséquence, g|V est inversible.
  Tout point de X possède une base de voisinages rationnels, en particulier une base
de voisinages affinoïdes. Plus précisément, pour tout x ∈ X et tout voisinage ouvert U
de x, il existe un système rationnel d’inéquations β dont le lieu de validité est contenu
dans U , et tel que x satisfasse β̊.
11.1.6. — Le théorème de Gerritzen-Grauert affirme que tout domaine affinoïde de X
est réunion finie de domaines rationnels (pour le cas non strict, voir [47], lemme 2.4 ;
pour une preuve directe, voir aussi [128], théorème 3.1). Il en résulte que si x est un
point de X situé sur un domaine affinoïde V de X, le corps résiduel complété H (x) ne
dépend pas du fait que l’on voie x comme appartenant à V = M (AV ) ou à X = M (A).
300                CHAPITRE 11. RAPPELS DE GÉOMÉTRIE ANALYTIQUE

11.1.7. — À partir des espaces affinoïdes, Berkovich définit dans [9] la catégorie des
espaces k-analytiques par un procédé de recollement un peu délicat qu’il serait trop
long de décrire ici en détail ; nous allons tout de même rappeler quelques faits. Suivant
Berkovich, si X est un espace topologique et si (Xi ) est une famille de parties de X,
nous dirons que les Xi constituent
                           S         un G-recouvrement de X si tout point x de X possède
un voisinage de la forme i∈J Xi où J est fini et où x ∈ Xi pour tout i ∈ J. Si l’on
ne s’astreint à recoller que des espaces strictement affinoïdes, on obtient la classe des
espaces strictement k-analytiques.
   Soit X un espace k-analytique. C’est en particulier un espace topologique dont tout
point possède une base de voisinages compacts (mais X n’est pas nécessairement lo-
calement compact puisqu’un espace topologique localement compact est par définition
séparé, et que ce n’est pas forcément le cas de X). L’espace X possède par ailleurs une
classe distinguée de partie compactes, ses domaines affinoïdes (si X = M (A ), les do-
maines affinoïdes de X sont précisément ceux décrits au 11.1.5 ci-dessus). Un domaine
analytique de X est une partie de X qui est G-recouverte par les domaines affinoïdes
qu’elle contient. Tout domaine affinoïde de X est un domaine analytique de X ; plus
généralement, tout compact de X qui est une union finie de domaines analytiques de
X est un domaine analytique. Et tout ouvert de X (et notamment X lui-même) est un
domaine analytique. En particulier, tout point x de X possède un voisinage compact
qui est une réunion finie de domaines affinoïdes contenant x. Les espaces définis dans [8]
sont ceux qui sont qualifiés de bons dans [9], c’est-à-dire ceux dont tout point admet un
voisinage affinoïde (et donc une base de voisinages affinoïdes.) Tout domaine analytique
de X est une partie localement fermée de X : l’intersection d’une famille finie de do-
maines analytiques est un domaine analytique ; la réunion d’une famille localement finie
de domaines analytiques fermés est un domaine analytique.
   Tout domaine analytique V de X hérite d’une structure canonique d’espace analy-
tique, et d’un morphisme V ,→ X dont l’application sous-jacente est l’inclusion. Tout
morphisme f : Y → X se factorisant ensemblistement par V se factorise en fait unique-
ment par la structure analytique de V .
11.1.8. La G-topologie. — Soit X un espace k-analytique. En plus du site topolo-
gique sur X on définit un second site plus fin, noté XG . Ses objets sont les domaines
analytiques de X, ses flèches sont les inclusions, et ses familles couvrantes sont les G-
recouvrements. La topologie de ce site est appelée la G-topologie de X.
  Comme tout ouvert de X est un domaine analytique et comme tout recouvrement
ouvert est un G-recouvrement, on dispose d’un morphisme de site canonique π : XG →
X. L’unité d’adjonction id → π∗ π ∗ est un isomorphisme ([9], p. 26).
  Le site XG est annelé. Nous noterons OX le faisceau structural de XG . Sauf mention du
contraire, lorsque nous parlerons de faisceaux cohérents sur X, il s’agira plus précisément
de OX -module cohérents sur XG . Précisons que le faisceau OX ainsi que sa restriction
au site topologique usuel de X sont cohérents ([49], lemme 0.1 ; pour la correction d’une
petite erreur dans la preuve, signalée par Jérôme Poineau, voir [52], 1.1.1). Si X = M (A)
alors OX (X) = A.
  Tout morphisme f : Y → X entre espaces analytiques est en particulier un morphisme
de sites annelés : si V est un domaine analytique de Y alors f −1 (V ) est un domaine
analytique de X et l’on dispose d’un morphisme f ∗ : OX (V ) → OY (f −1 (V )). Si X est
un espace k-affinoïde M (A) et si Y est un espace affinoïde M (B) sur une extension de
     § 11.1. GÉOMÉTRIE ANALYTIQUE : CONVENTIONS, NOTATIONS, PREMIERS RAPPELS               301

k, l’application f 7→ f ∗ établit une bijection entre l’ensemble des k-morphismes de Y
vers X et l’ensemble des morphismes bornés de k-algèbres de A vers B.
   Si X = M (A) est un espace k-affinoïde et si M est un A-module de type fini, le
faisceau Mf sur XG associé au préfaisceau V 7→ M ⊗A OX (V ) est cohérent. Le foncteur
M 7→ M f établit une équivalence entre la catégorie des A-modules de type fini et celle
des faisceaux cohérents sur X, de quasi-inverse F 7→ F (X) (cf. [9] ; ce résultat est dû
à Kiehl dans le cas strictement affinoïde).
   Lorsque X est bon, le foncteur π∗ induit une équivalence de catégories entre faisceaux
cohérents sur XG et faisceaux cohérents sur X, et qu’un faisceau cohérent F sur XG est
localement libre si et seulement si c’est le cas de π∗ F ([9], 1.3.4 ; notons que la définition
de faisceau cohérent qu’il utilise dans cette proposition est ad hoc, mais qu’elle coïncide
bien en fait avec la notion usuelle au vu de la cohérence des faisceaux structuraux sur
les deux sites annelés en jeu).
11.1.9. Produits fibrés, extension des scalaires. — La catégorie des espaces k-
analytiques admet des produits fibrés. Si A → B et A → C sont deux morphismes
d’algèbres k-affinoïdes, M (B) ×M (A) M (C) = M (B ⊗     b A C).
   Si L est un extension complète de k on dispose d’un foncteur d’extension des scalaires
X 7→ XL de la catégorie des espaces k-analytiques vers celle des espaces L-analytiques.
Si X = M (A) alors XL = M (A⊗       b k L). En général on dispose d’un morphisme naturel
de sites annelés de XL vers X, qui est surjectif (cf. [48], 0.5).
   Supposons X bon, soit y un point de XL et soit x son image sur X. Le morphisme
naturel de Spec OXL ,y vers Spec OX,x est plat à fibres localement d’intersection complète,
et à fibres géométriquement régulières si L est analytiquement séparable sur k ; c’est le
théorème [52], th. 2.6.5. La notion d’extension analytiquement séparable est définie
dans [49] (définition 1.6). Une extension finie de k est analytiquement séparable si et
seulement si elle est séparable ; si r est un polyrayon de longueur finie et k-libre, kr est
une extension analytiquement séparable de k ; si k est parfait, toute extension complète
de k est analytiquement séparable.
   On définit la catégorie des espaces analytiques au-dessus de k comme la catégorie dont
```

## CLD.txt, newline lines 15287–15355

```text
topologie de V induite par la topologie de Zariski de X, et en général strictement plus
fine.
   Si E est une partie de X et si (Xi ) est un G-recouvrement de X par des domaines
analytiques, alors E est un fermé (resp. un ouvert) de Zariski de X si et seulement si
E ∩ Xi est un fermé (resp. un ouvert) de Zariski de Xi pour tout i ([49], Prop. 4.2.1).
306                  CHAPITRE 11. RAPPELS DE GÉOMÉTRIE ANALYTIQUE

   Une immersion fermée (1) est un morphisme d’espaces k-analytiques f : Y → X se
factorisant par un isomorphisme entre Y et un sous-espace analytique fermé de X. Une
immersion fermée préserve les corps résiduels complétés.
   Un morphisme d’espaces k-analytiques f : Y → X est dit séparé si sa diagonale
δ : Y → Y ×X Y est une immersion fermée, et X est dit séparé si le morphisme structural
de X vers M (k) est séparé. La séparation dans ce sens entraîne la séparation topolo-
gique, mais la réciproque est fausse : le recollement de deux copies du disque unité le
long du domaine affinoïde décrit par l’égalité |T | = 1 est topologiquement séparé car le
domaine de recollement est fermé, mais n’est pas séparé.
11.2.3. Dimension. — On dispose d’une théorie de la dimension en géométrie ana-
lytique, due à Berkovich, au sujet de laquelle on pourra consulter le chapitre 2 de [8], la
fin du paragraphe 1.2 de [9] ou encore l’article [48].
   Soit X un espace k-analytique. Sa dimension (k-analytique) est définie comme suit.
Commençons par le cas affinoïde. Écrivons X = M (A) et choisissons une extension
complète L de k telle que AL := A⊗        b k L soit strictement L-affinoïde. La dimension de
Krull de AL ne dépend alors pas de L ([48], 1.5) et est appelée dimension de X. (Si X est
strictement k-affinoïde sa dimension est donc simplement sa dimension de Krull relative
à sa topologie de Zariski.) On a par construction dim Xred = dim X et dim XL = dim X
pour toute extension complète L de k.
   Si Y est un fermé de Zariski de X, le choix d’une structure de sous-espace analytique
fermé sur Y , c’est-à-dire d’un idéal I de A définissant Y , fait de Y un espace affinoïde
(identifié à M (A/I)). Sa dimension ne dépend pas du choix de I, et nous parlerons donc
de la dimension de Y sans spécifier I.
   Soit X1 , . . . , Xn les fermés de Zariski de X correspondant aux idéaux premiers mini-
maux de A. Si V est un domaine affinoïde de X on a alors dim V = supi,V ∩Xi ̸=∅ dim Xi .
En particulier dim V ⩽ dim X = supi dim Xi . Si x est un point de X on définit dimx X
comme le minimum des dim V où V est un domaine affinoïde de X contenant x ; c’est
aussi supi,x∈Xi dim Xi . Il vient dim X = supi dim Xi = supx∈X dimx X.
   Ne supposons plus X affinoïde. Si x est un point de X, on définit la dimension locale
dimx X de X en x comme le minimum des dim V où V parcourt l’ensemble des domaines
affinoïdes de X contenant x, et l’on pose alors dim X = supx∈X dimx X. Cette définition
est compatible avec la précédente lorsque X est affinoïde. Si V est un domaine analytique
de X on a dimx V = dimx X pour tout x ∈ V , si bien que dim V ⩽ dim X. Si d est un
entier on dit que X est purement de dimension d si dimx X = d pour tout x ∈ X. Si
c’est le cas X est ou bien vide, ou bien de dimension d.
   Pour tout point x de X on pose
(11.2.3.1)
                                                   1
      dk (x) = degtr(H      (x)/k̃) = degtr(H        k 1 ) + dimQ Q ⊗Z (|H (x)× |/|k × |) ,
                                                                                         
                         ^                  ^  (x) /e
où la seconde égalité provient de 10.1.9 ; Berkovich le note d(κ(x)/k) ou d(H (x)/k)
L’intérêt majeur de cet invariant est l’égalité dim(X) = supx∈X dk (x) ([9], Lemma 2.5.2).
   Soit Y un fermé de Zariski de X. Munissons-le d’une structure de sous-espace analy-
tique fermé. La dimension de l’espace analytique correspondant ne dépend que de Y , et
(1)
   Dans l’expression « immersion fermée » ou dans l’expression « sous-espace analytique fermé », l’ad-
jectif « fermé » fait implicitement référence à la topologie de Zariski. Ainsi, en général, un domaine
analytique fermé V de X n’est pas un sous-espace analytique fermé de X, et le morphisme canonique
V ,→ X n’est pas une immersion fermée.
                 § 11.2. TOPOLOGIE DE ZARISKI, THÉORIE DE LA DIMENSION                     307

pas de la structure en question (par exemple au vu de l’égalité ci-dessus, ou par réduc-
tion au cas affinoïde via la description des domaines analytiques de Y ). On pourra donc
parler de la dimension de Y sans spécifier la structure dont on le munit.


Remarque 11.2.4. — Insistons sur le fait que la dimension considérée ici est en fait
une dimension relative au corps de base k, même si nous ne rappelons pas cette dépen-
dance. Considérons par exemple l’algèbre de Banach kr associée à un polyrayon k-libre
(r1 , . . . , rn ) (exemple 11.1.3). C’est une extension complète de k. En tant qu’algèbre kr -
affinoïde elle est stricte, et sa dimension de Krull est nulle. Par conséquent la dimension
```

## CLD.txt, newline lines 15567–15604

```text
compact si l’image réciproque de toute partie compacte est compacte. Comme tout point
possède un voisinage compact, cela revient à dire que f est topologiquement propre et
topologiquement séparé.
  Suivant [9] (1.5.3), un morphisme est dit propre s’il est compact et sans bord.
11.4.4. Morphismes finis. — Soit A une algèbre k-affinoïde. Une A-algèbre de Ba-
nach finie est une A-algèbre de Banach B qui est finie comme A-algèbre, et dont la
norme est équivalente à la norme quotient induite par une présentation finie An → B
du A-module B. Dans ce cas la norme de B est en fait équivalente à la norme quotient
associée à n’importe quelle présentation finie du A-module B (c’est une conséquence de
[8], Prop. 2.1.9). Toute A-algèbre de Banach finie est k-affinoïde (combiner [20], Prop.
6.1.3/4 et [8], Cor. 2.1.8). Le foncteur d’oubli de la norme induit une équivalence de
catégories entre A-algèbres de Banach finies et A-algèbres finies(2) ([8], Prop. 2.1.12).
   Soit f : Y → X un morphisme entre espaces k-analytiques. Si X et Y sont affinoïdes,
on dit que f est fini si f ∗ fait de O(Y ) une O(X)-algèbre de Banach finie ; cela revient
à demander que f soit sans bord ([8], Cor. 2.5.13). En général (si l’on ne suppose plus
X et Y affinoïdes) les assertions suivantes sont équivalentes : ([9], Cor. 1.3.7).
  (i) Il existe un G-recouvrement (Xi ) de X par des domaines affinoïdes tels que pour
tout i, l’image réciproque f −1 (Xi ) soit affinoïde et que le morphisme induit de f −1 (Xi )
vers Xi soit fini
  (ii) Pour tout domaine affinoïde V de X l’image réciproque f −1 (V ) est affinoïde et le
morphisme induit de f −1 (V ) vers V est fini.

  Si |k × | ̸= {1} et si A est strictement k-affinoïde, on déduit de [8], Prop. 2.1.1 et [20], Thm. 6.1.3/1
(2)

que toute A-algèbre de Banach qui est finie comme A-algèbre est une A-algèbre de Banach finie. Par
contre si k est trivialement valué et si 0 < r < s < 1, le morphisme continu naturel de k{T /s} vers
k{T /r} est bijectif (sa source et son but s’identifient tous deux à k[[T ]]) mais sa réciproque n’est pas
bornée, si bien que k{T /s} n’est pas une k{T /r}-algèbre de Banach finie).
312                CHAPITRE 11. RAPPELS DE GÉOMÉTRIE ANALYTIQUE

On dit que f est fini si elles sont satisfaites ; cette définition est compatible avec la
précédente si X et Y sont affinoïdes. Un morphisme fini est sans bord.
  La classe des morphismes finis est stable par composition et changement de base
analytique sur k, et la propriété d’être fini est G-locale au but.
  Soit y un point de Y . On dit que f est fini en y s’il existe un voisinage analytique
U de f (y) dans X et un voisinage analytique V de y dans f −1 (U ) tel que f induise un
morphisme fini de V vers U . Si c’est le cas le point y appartient à Int(Y /X), et si de
```

## CLD.txt, newline lines 16122–16143

```text
  Supposons réciproquement que (X, ^   x) soit l’image réciproque d’un ouvert affine de
P ^ 1 e1 . Il résulte de la preuve du lemme 3.5.1 de [52] qu’il existe un entier n, un
 H (x) /k
point y du polydisque unité D de dimension n et un morphisme sans bord de (X, x) vers
(D, y). Lorsque la valeur absolue de k n’est pas triviale, y possède une base de voisinages
strictement affinoïdes dans D, si bien que (X, x) possède un représentant strictement
affinoïde.
11.7.7. — Supposons que la valeur absolue de k n’est pas triviale. On déduit alors
des résultats rappelés au 11.7.6 que (X, x) est strictement k-analytique si et seulement
   ^
si (X, x) est strict, cf. [52, Lemma 3.5.2]. Mentionnons incidemment que si (X, x) est
                         ^
à la fois bon et strict, (X, x) est à la fois affine et strict, donc est l’image réciproque
d’un ouvert affine de P ^ 1 e1 (10.5.5) ; il découle alors de 11.7.6 que le germe (X, x) est
                        H (x) /k
strictement affinoïde. Autrement dit tout point d’un bon espace strictement k-analytique
admet un voisinage strictement affinoïde ce qui, à notre connaissance, ne figurait pas
jusqu’ici explicitement dans la littérature.
   Notons que l’hypothèse que la valeur absolue de k n’est pas triviale est indispensable
à la validité des énoncés ci-dessus. Supposons en effet que |k × | = {1}, et soit X l’ouvert
de A1k défini par les inégalités 0 < |T | < 1 ; il est sans bord, si bien que pour tout x ∈ X
              ^
```

## CLD.txt, newline lines 3750–3920

```text
3.3.8. — Soit ω une G-forme (resp. une forme) de type (p, q) à coefficients dans G
sur X. Si V est un domaine de X, une G-tropicalisation de ω sur V est la donnée d’une
carte G-tropicale (f : V → E, P ) et d’une forme α ∈ GPp,q (P ) telle que ω = f ∗ α.
  On dira que ω est G-tropicale si elle admet une G-tropicalisation sur X.
  Si V est un domaine de X tel que ω possède une G-tropicalisation sur V , nous dirons
aussi que V G-tropicalise ω.
  Soit V un domaine compact de X qui G-tropicalise ω, et soit (f V → E, P, α) une
G-tropicalisation de ω|V . Comme f (V ) est un sous-espace paralinéaire de E, (f : V →
E, f (V ), α|f (V ) ) est encore une G-tropicalisation de ω|V ; une telle G-tropicalisation sera
simplement notée (f : V → E, α) : lorsque V est compact, l’omission du sous-espace
paralinéaire P signifie qu’il est égal à f (V ).

Remarque 3.3.9. — Soit H une classe de coefficients contenant G . Observons que
les G-formes à coefficients dans G s’identifient à des G-formes à coefficients dans H .
   En effet, le G-préfaisceau Gpfp,q sur XG s’identifie à un sous-G-préfaisceau de Hpfp,q , de
sorte que le G-faisceau GXp,qG sur X s’identifie alors à un sous-G-faisceau de HXp,qG
                                                                                       . Ces
identifications sont compatibles avec les constructions faites dans ce paragraphe.

3.3.10. — Le faisceau GXG := GX0,0G est un faisceau en R-algèbres et les faisceaux GXp,qG
sont des GXG -modules. Leur somme directe GX∗,∗G = p,q GXp,qG est un faisceau en algèbres
                                                   L

bigraduées commutatives : si ω est de type (p, q) et ω ′ de type (p′ , q ′ ), alors
                                                    ′     ′
                                ω ′ ∧ ω = (−1)(p+p )(q+q ) ω ∧ ω ′ .
3.3.11. — Le G-préfaisceau Gpf∗,∗ est naturellement muni d’un opérateur J qui s’étend
au faisceau GX∗,∗G . Ce sont des morphismes d’algèbres. On dit qu’une section ω de GXp,qG
est symétrique si p = q et si Jω = ω.
    Soit H une classe de coefficients telles que les dérivées partielles des fonctions de G
existent et appartiennent à H . On dispose alors d’opérateurs différentiels d′ et d′′ de
Gpf∗,∗ dans Hpf∗,∗ ; ils induisent des opérateurs différentiels de GX∗,∗G dans HX∗,∗
                                                                                  G
                                                                                     , caractérisés
par les relations
                               d′ f ∗ α = f ∗ d′ α, d′′ f ∗ α = f ∗ d′′ α,
                                 § 3.4. NULLITÉ DES G-FORMES                             81

pour toute carte G-tropicale (f : U → E, P ) et toute forme α de type (p, q) à coeffi-
cients dans G sur P . Les différentielles vérifient la règle de Leibniz : si ω et ω ′ sont
respectivement de type (p, q) et (p′ , q ′ ), on a
(3.3.11.1)               d′ (ω ∧ ω ′ ) = d′ ω ∧ ω ′ + (−1)p+q ω ∧ d′ ω ′ ,
et de même pour d′′ (ω ∧ ω ′ ).
   Si G ⊂ C 2 , ces opérateurs vérifient d′ d′ = d′′ d′′ = 0.
3.3.12. — Cette construction est fonctorielle. Plus précisément, si f : Y → X est un
morphisme d’espaces G-tropicaux, on dispose de morphismes de faisceaux
                                     f ∗ : GX∗,∗G → f∗ (GY∗,∗
                                                           G
                                                              )
sur XG qui sont des morphismes d’anneaux gradués, commutent aux dérivations d′ et
d′′ (lorsqu’elles existent) et à l’opérateur J.
   Lorsque le contexte rend évident le morphisme f , on se permettra parfois de noter
ω|Y l’image dans GYp,q G
                         (Y ) d’une G-forme ω ∈ GXp,qG .
3.3.13. — Soit (p, q) un couple d’entiers naturels. Soit Σ une partie paralinéaire de X
et soit j l’inclusion de Σ dans X. C’est un morphisme d’espaces G-tropicaux. On dispose
donc d’un morphisme de faisceaux de FXp,qG dans j∗ FΣp,qG . On notera ω 7→ ω|Σ l’image
d’une forme ω et on dira que c’en est la restriction à Σ.
   Concrètement, cette restriction se calcule de la façon suivante.
   Soit V un domaine de X, soit (f : V → E, P ) une carte G-tropicale sur V , et soit
α ∈ FPp,q (P ). Alors Σ ∩ V est une partie paralinéaire de V , l’application f : Σ ∩ V → E
est paralinéaire et son image est contenue dans P , l’image réciproque f ∗ α de α est
une forme de type (p, q) sur l’espace paralinéaire Σ ∩ V . Par définition de l’ensemble
Fpfp,q (V ) comme limite inductive, la forme f ∗ α ne dépend que de la classe de f ∗ α dans
cet ensemble. Cette construction définit un morphisme de préfaisceaux de FX,pf     p,q
                                                                                       dans
j∗ FΣp,q .
   Par passage aux faisceaux associés, on en déduit le morphisme de restriction de FXp,qG
dans j∗ FΣp,qG .
3.3.14. — Soit f : Y → X un morphisme d’espaces G-tropicaux, soit T une partie
paralinéaires de Y et soit Σ une partie paralinéaire de X telle que f (Σ) ⊂ T. Pour toute
forme ω ∈ FXp,qG (X), on a (f ∗ ω)|T = (f |T )∗ (ω|Σ ).
   Nous appliquerons notamment cette remarque lorsque Y est un domaine de X et
T = Σ ∩ Y , ou bien lorsque Y = X et T est une partie polyédrale de Σ.



                          § 3.4. NULLITÉ DES G-FORMES

Proposition 3.4.1. — Soit X un espace G-tropical compact, soit f : X → E une carte
G-tropicale, soit P un sous-ensemble paralinéaire de E contenant f (X) et soit α ∈
GPp,q (P ). Les assertions suivantes sont équivalentes :
   a) La restriction de α au sous-espace paralinéaire f (X) est nulle ;
   b) La section globale f ∗ α de Gpfp,q est nulle.
Démonstration. — L’hypothèse (1) entraîne que l’image de α dans la carte tropicale
(f, f (X)) est nulle, de sorte que (2) vaut. Supposons que (2) est vérifiée et prouvons (1).
82                          CHAPITRE 3. ESPACES G-TROPICAUX

   On peut remplacer P par f (X). Par définition, il existe une carte G-tropicale g : X →
F , une morphisme affine p : F → E tel que p ◦ g = f , et un sous-espace paralinéaire Q
de F contenant g(X) tels que p(Q) ⊂ P et p∗ α = 0 dans GQp,q (Q). On peut aussi
remplacer Q par g(X) ; on a alors p(Q) = P .
   Le morphisme de Q sur P induit par p possède G-localement des sections. D’après
le corollaire 1.8.5, il existe une décomposition cellulaire (Ci ) de P et, pour tout i, une
section de ptrop sur Ci à valeurs dans Q. Puisque p∗ α = 0, on a donc α|Ci = 0 pour
tout i. Par suite, α = 0.

Corollaire 3.4.2. — Soit X un espace G-tropical compact, soit ω ∈ Gpfp,q (X) et soit
(Xi ) un G-recouvrement de X. Supposons que pour tout i, la restriction de ω à Xi soit
nulle ; alors ω = 0.
Démonstration. — Tout G-recouvrement admet un G-recouvrement plus fin formé de
domaines compacts. Comme X est compact, cela permet de supposer que le recouvre-
ment (Xi ) est formé d’un nombre fini de domaines compacts. Par définition du préfais-
ceau Gpfp,q , il existe une carte G-tropicale f : X → E, un sous-espace paralinéaire P de E
contenant f (X), et une forme α ∈ GPp,q (P ) tels que ω = f ∗ α.
   Il résulte que de la proposition 3.4.1 que α|f (Xi ) = 0 pour tout i. Comme f (X) est la
réunion des f (Xi ), la forme α est nulle sur f (X) (lemme 1.9.2). On a donc ω = f ∗ α =
0.

Remarque 3.4.3. — L’hypothèse que X est compact est cruciale pour le corol-
laire 3.4.2.
   Prenons pour espace G-tropical l’ensemble X = R, muni de la topologie discrète, et
pour carte l’application identique f : R → R. Soit α la forme d′ x sur R. Soit g : X → Rn
une carte qui domine la carte f , et soit p : Rn → R une application affine telle que
f = p ◦ g. Alors, p est surjective, donc p∗ α ̸= 0. Cela prouve que la section f ∗ α de Gpf1,0
n’est pas nulle. En revanche, pour tout t ∈ R, le singleton Vt = {t} est un domaine de X
de tropicalisation Pt = {t} et α|Pt = 0, si bien que α|Vt = 0. Comme ces domaines Vt
forment un G-recouvrement de X, cela montre que le préfaisceau Gpf1,0 n’est pas séparé.
Proposition 3.4.4. — Soit X un espace G-tropical, soit f : X → E une carte G-
tropicale, soit P un sous-espace paralinéaire de E contenant f (X) et soit α ∈ FPp,q (P ).
   Les propriétés suivantes sont équivalentes :
   a) Pour tout domaine compact V de X, la restriction de α au polytope f (V ) est nulle ;
   b) Pour tout domaine compact V de X, la restriction de f ∗ α à V est nulle ;
   c) L’image de f ∗ α dans FXp,qG (X) est nulle.
Démonstration. — D’après la proposition 3.4.1, les assertions (1) et (2) sont équiva-
lentes.
   Supposons (1). Comme X admet un G-recouvrement par des domaines compacts,
l’assertion (3) s’en déduit.
   Supposons (3). Il existe donc un G-recouvrement (Xi ) tel que f ∗ α|Xi = 0 en tant que
section du préfaisceau Fpfp,q . Soit V un domaine compact de X. La restriction de f ∗ α
à Xi ∩ V est nulle pour tout i ; comme la famille (Xi ∩ V ) est un G-recouvrement de V ,
le corollaire 3.4.2 entraîne que f ∗ α|V = 0, d’où l’assertion (2). Cela termine la preuve
de la proposition.
                                § 3.4. NULLITÉ DES G-FORMES                                83

Corollaire 3.4.5. — Soit X un espace G-tropical compact, soit f : X → E une carte
G-tropical et soit P le sous-espace paralinéaire f (X). Soit α ∈ GPp,q (P ), et soit ω la
G-forme f ∗ α. Notons K le support de ω dans X et H celui de α dans f (X). On a
H = f (K).

Démonstration. — Soit x un point de X. Soit Q un voisinage de f (x) dans P qui est
                                             −1
un polytope compact. Le domaine W = ftrop       (Q) de X est un voisinage de x et ω|W =
       ∗
(f |W ) (α|Q ).
   Supposons que x appartienne à K. Le compact K rencontre alors l’intérieur de W , ce
qui entraîne que ω|W ̸= 0, et donc que α|Q ̸= 0. Il s’ensuit que H rencontre Q. Comme
Q peut être choisi arbitrairement petit, f (x) appartient à H, d’où l’inclusion f (K) ⊂ H.
   Réciproquement, supposons que f (x) ∈ H. Par définition de H, la restriction à Q de
la forme α est non nulle. D’après la proposition 3.4.4, la restriction de ω à f −1 (Q) est
non nulle. Par conséquent, f −1 (Q) rencontre K, donc Q = f (f −1 (Q)) rencontre f (K).
Comme Q est un voisinage arbitrairement petit de f (x), celui-ci est adhérent à f (K).
Puisque f (K) est compact, f (x) appartient à f (K).

3.4.6. — À toute carte G-tropicale (f : V → E, P ) sur un domaine V de X et à toute
fonction u sur P , associons la fonction u◦f sur V . On définit ainsi un morphisme de pré-
faisceaux de Fpf0,0 vers le G-faisceau des fonctions sur X. Il découle de la proposition 3.4.4
que le morphisme de FX0,0G dans le G-faisceau des fonctions sur X est injectif, morphisme
par lequel nous identifierons systématiquement une (0, 0)-G-forme à une fonction.
   Une section globale du faisceau GX0,0G est une fonction sur X qui est G-localement de la
forme φ(f1 , . . . , fn ) où les fi sont des fonctions paralinéaires sur X, et où φ appartient
à la classe G . De telles fonctions seront appelées G-localement tropicales de classe G .

Définition 3.4.7. — Soit A la classe des fonctions lisses. Les sections de AX0,0
                                                                              G
                                                                                 sont
appelées fonctions G-lisses sur X.

   Les fonctions G-lisses sont donc les fonctions sur X sont G-localement de la forme
φ(f1 , . . . , fn ) où les fi sont des fonctions paralinéaires et où φ est une fonction de
classe C ∞ .
```

## CLD.txt, newline lines 5289–5314

```text

Lemme 4.4.5. — Soit f : Y → X une immersion par morceaux d’espaces paralinéaires
de niveau n. Soit α une forme-volume à coefficients boréliens sur X. On a l’égalité
(f ∗ α)Bor = f ∗ (αBor ) de mesures de Borel régulières positives sur Y . Si α est localement
intégrable, alors f ∗ α est localement intégrable et l’on a l’égalité (f ∗ α)Rad = f ∗ (αRad ) de
mesures de Radon sur Y .

   Comme f est une immersion par morceaux, l’image inverse de la mesure de Borel
régulière αBor par f est définie G-localement (cf. A.3.13) ; de même pour les mesures de
Radon.
Démonstration. — L’espace Y est G-recouvert par des cellules C telles que f induise un
isomorphisme de C sur son image, laquelle possède une immersion paralinéaire dans Rn .
L’assertion découle alors de la construction de ces mesures.

Lemme 4.4.6. — Soit f : Y → X une immersion par morceaux compacte d’espaces
paralinéaires de niveau n. Soit α une forme-volume à coefficients boréliens sur Y . On
a une inégalité (f∗ α)Bor ⩽ f∗ (αBor ) de mesures de Borel régulières positives sur X, qui
est une égalité si f est injective. Si α est localement intégrable, alors f∗ α est localement
intégrable et l’on a l’égalité (f∗ α)Rad = f∗ (αRad ) de mesures de Radon sur X.

Démonstration. — En raisonnant localement, on se ramène au cas où X est paracom-
pact. Soit (C , D) un couple de décompositions cellulaires qui est adapté à f . Après
restriction à toute cellule D de D, les assertions découlent directement des définitions
des mesures et des images directes.
108    CHAPITRE 4. CALIBRAGES ET INTÉGRATION SUR LES ESPACES PARALINÉAIRES

```

## CLD.txt, newline lines 5449–5483

```text
forme ω sont positifs.
   Les (n, n)-formes localement µ-intégrables forment un sous-faisceau en BXG -module
de BX n,n
        G
          , et l’application ω 7→ ⟨ω, µ⟩ est linéaire.
   On dira enfin que le calibrage µ est localement intégrable si toute forme à coefficients
localement bornés est localement µ-intégrable. Sur une cellule, cela revient à dire que
le calibrage est produit d’un calibrage standard par une fonction localement intégrable.
Les calibrages G-localement constants sont localement intégrables.

Exemple 4.5.7. — Lorsque X est un sous-espace affine de dimension n d’un espace
affine V , ω une forme lisse sur X et µ un vecteur-volume sur X, on retrouve la notion
d’intégrale définie dans le paragraphe 1.5.3 à partir des idées de Lagerberg.
   D’une certaine manière, les constructions de ce chapitre visaient simplement à « G-
faisceautiser » cette formule élémentaire de Lagerberg sur un espace affine.

Proposition 4.5.8. — Soit f : Y → X une immersion par morceaux propre d’espaces
paralinéaire de niveau n.
   a) Pour toute (n, n)-forme ω sur X et tout calibrage µ de Y , on a l’égalité f∗ ⟨f ∗ ω, µ⟩ =
⟨ω, f∗ µ⟩ de formes-volume n-dimensionnelles sur X.
   b) Pour toute (n, n)-forme ω sur Y et tout calibrage µ de X, on a l’égalité ⟨f∗ ω, µ⟩ =
f∗ ⟨ω, f ∗ µ⟩ de formes-volume n-dimensionnelles sur X.

Démonstration. — En raisonnant localement, on se ramène au cas où X est paracom-
pact. Il existe alors un couple (C , D) de décompositions cellulaires qui est adapté à f .
                  § 4.6. CALIBRAGES ET INTÉGRALES DES (n − 1, n)-FORMES                  111

Les assertions indiquées se vérifient alors, cellule par cellule, à partir des constructions
des intégrales et de la définition du calibrage f∗ µ (resp. du calibrage f ∗ µ).



     § 4.6. CALIBRAGES ET INTÉGRALES DES (n − 1, n)-FORMES

4.6.1. — Soit G une classe de coefficients. Soit X un espace paralinéaire de niveau n,
```

## CLD.txt, newline lines 6308–6332

```text
Lemme 5.3.4. — Si la forme ω est G-tropicalisée par une carte G-tropicale f de do-
                (n)
maine X, alors Σf supporte fortement ω.

Démonstration. — Le support de ω est contenu dans l’ensemble des points x ∈ X en
                                                                    (n)
lesquels f est de dimension tropicale ⩾ n qui, par définition, est Σf .
                                                                  (n)
  Soit T un sous-espace paralinéaire fermé de X qui contient Σf . Démontrons que ω|T
est le prolongement par zéro de ω|Σ(n) . Soit C une décomposition cellulaire en f -cellules
                                     f
                             (n)
de T qui est compatible à Σf . Il suffit de prouver que pour toute cellule C de C      telle
                        (n)
que C̊ est disjoint de Σf , on a ω|C = 0.
  Par hypothèse, f est de dimension tropicale < n en tout point de C̊, donc il existe une
cellule D, compacte, d’intérieur non vide, de C̊ telle que dim(f (D)) < n. Comme C est
une f -cellule, on dim(f (C)) = dim(f (C̊)) = dim(f (D)). D’après la proposition 3.4.4, on
a donc ω|C = 0.
                          (n)
  Cela démontre que Σf supporte fortement ω.

Proposition 5.3.5. — Soit n un entier et soit X un espace G-tropical vertébré de
niveau n. Soit (p, q) un couple d’entiers naturels tel que max(p, q) = n et soit ω une
G-forme de type (p, q) sur X. Supposons que X est paracompact, ou que le support de ω
```

## CLD.txt, newline lines 6400–6414

```text
                                      f
composition cellulaire finie en f -cellules.
                                                                         (n)
   Lorsque f est une carte agréable, nous noterons Πf l’ensemble f (Σf ) et l’appellerons
le polyèdre tropical de la carte G-tropicale agréable f . Il est purement de dimension n
                                                               (n)
et l’application f induit une immersion par morceaux de Σf sur Πf .
5.4.4. — Si X est compact, toute carte G-tropicale est agréable et l’on a Πf = f (X)(n)
(proposition 5.2.5).
Proposition 5.4.5. — Soit X un espace G-tropical vertébré de niveau n, soit f : X →
E une carte G-tropicale agréable et soit P un sous-espace paralinéaire P de E. Consi-
dérons la carte G-tropicale fP : f −1 (P ) → E sur le domaine f −1 (P ) (considéré comme
130                      CHAPITRE 5. ESPACES G-TROPICAUX CALIBRÉS

espace G-tropical vertébré de niveau n) déduite de f par restriction. La carte fP est
```

## CLD.txt, newline lines 6753–6812

```text
            = ⟨ω|T , µT ⟩                  d’après (3.3.14)
            = ⟨(ω|Σ )|T , (µΣ )|T ⟩        d’après (3.3.14) et la définition d’un calibrage
            = ⟨ω|Σ , µΣ ⟩|T = ω
                              e |Y
parce que l’accouplement entre (n, n)-formes et calibrages est un morphisme de faisceaux
sur le site XG . Le lemme est ainsi démontré.

Proposition 5.8.3. — Il existe un unique morphisme de faisceaux FXn,n            G
                                                                                    → VXnG
sur XG , noté ω 7→ ω e , qui prolonge l’application définie en (5.8.1) lorsque ω possède
un support fort. Ce morphisme est FX0,0G -linéaire. Si ω est une G-forme positive, la
forme-volume ωe est positive. Si ω est à coefficients dans une classe G , il en va de même
de la forme-volume ωe.
Démonstration. — Compte tenu du lemme 5.8.2, la première assertion résulte de ce que
toute forme sur un domaine paracompact possède un support fort, et que tout domaine
est G-recouvert par ses domaines paracompacts. Les autres propriétés découlent alors
de la construction.

5.8.4. — Explicitons cette construction lorsque ω est tropicale. Soit f : X → E une
carte G-tropicale et soit α une (n, n)-forme sur un sous-espace paralinéaire de E conte-
                                         (n)
nant f (X) telle que ω = f ∗ α. Alors, Σf est un support fort de ω (lemme 5.3.4) et on
                                         (n)
a l’égalité de formes-volume sur Σf            :
                                                ∗
(5.8.4.1)                                ω̃ = ⟨ftrop α, µΣ(n) ⟩.
                                                            f

Si, de plus, la carte G-tropicale f est agréable, la proposition 4.5.8 entraîne alors que
(5.8.4.2)                       ftrop,∗ (ω̃) = ⟨α, f∗ µΣ(n) ⟩ = ⟨α, µΠf ⟩.
                                                        f
                                   § 5.9. MESURES DE BORD                                  137

 5.8.5. — Soit ω une forme de type (n, n) sur XG à coefficients tropicalement boréliens.
 Nous venons de lui associer une forme-volume n-dimensionnelle ω̃. Nous noterons alors
 ωBor la mesure de Borel sur X associée à ω̃ par la construction du §5.7.1.
   Nous dirons que ω est localement intégrable si cette mesure est localement finie, et
 que ω est intégrable si cette mesure est finie. Lorsque ω est localement intégrable, nous
 noterons ωRad la mesure de Radon associée à ω̃ ; on a |ωRad | = ωBor . Lorsque ω est une
 G-forme positive, la mesure ωRad est positive.         R           R
   Si f est une fonction borélienne sur X, on notera X f |ω| et X f ω les intégrales de f
Rcontre les mesures ωBor et ωRad lorsqu’elles existent. Cela définit en particulier l’intégrale
  X
    ω pour toute G-forme de type (n, n) à support compact qui est localement intégrable
(par exemple lisse).
   Les G-formes localement intégrables constituent un sous-espace vectoriel de F n,n (XG )
contenant les G-formes lisses. Les G-formes intégrables en sont un sous-espace vectoriel
qui contient les G-formes lisses à support compact.
5.8.6. — Soit u une fonction localement intégrable sur X et soit ω une G-forme lisse
de type (n, n) sur X. Alors, u est localement intégrable par rapport à la mesure ωBor ,
de sorte que uωRad est une mesure de Radon sur X.
   L’application (u, ω) 7→ uωRad est bilinéaire ; elle induit une application linéaire de
Lloc
   1
     (XG ) ⊗ A n,n (XG ) dans l’ensemble des mesures de Radon sur X. Cette application
se factorise par L1loc (XG ) ⊗ A n,n (XG ). On la notera bien sûr α 7→ αRad .
   Cette construction s’étend en des morphismes de G-faisceaux
                  Lloc,X
                    1
                        G
```

## CLD.txt, newline lines 6934–6977

```text

               § 5.10. INTÉGRALES ET TROPICALISATIONS

  Soit X un espace G-tropical calibré de niveau n.
Proposition 5.10.1. — Soit f : X → E une carte G-tropicale agréable, soit Πf le
polyèdre tropical de la carte f et soit µΠf son calibrage.
  Soit p ∈ {n−1, n} et soit α une (p, n)-forme à coefficients boréliens sur un sous-espace
paralinéaire P de E contenant f (X).
  a) Si p = n, on a l’égalité
                                   ftrop,∗ (f ∗ α)Bor ⩾ ⟨α, µΠf ⟩Bor
                             (n)
de mesures de Borel sur Πf .
  b) Si p = n − 1, on a l’inégalité
                                   ftrop,∗ (f ∗ α)Bor ⩾ ⟨α, µΠf ⟩Bor
                             (n)
de mesures de Borel sur Πf .
  c) La mesure (f ∗ α)Bor est localement finie si et seulement si la forme α|Πf est locale-
ment intégrable sur Πf ; dans ce cas, on a l’égalité
                                   ftrop,∗ (f ∗ α)Rad = ⟨α, µΠf ⟩Rad
de mesures de Radon sur Πf .
   d) En particulier, si α est intégrable sur Πf , la forme f ∗ α est intégrable sur X, on a
l’égalité
                                   Z         Z
                                        ∗
(5.10.1.1)                            f α=       ⟨α, µΠf ⟩
                                        X           Πf

lorsque p = n et l’égalité
                                      Z ∂          Z ∂
                                            ∗
(5.10.1.2)                                  f α=         ⟨α, µΠf ⟩
                                        X           Πf

lorsque p = n − 1.
Démonstration. — Posons ω = f ∗ α. D’après la relation (5.8.4.2) lorsque p = n et la
relation (5.9.4.2) lorsque p = n−1, on a l’égalité (ftrop )∗ (ω̃) = ⟨α, µΠf ⟩ de formes-volume
p-dimensionnelles sur Πf . Le lemme 4.4.6 entraîne alors que f∗ (ω̃Bor ) ⩾ ⟨α, µΠf ⟩Bor .
Loreque p = n, on vérifie, en revenant aux définitions et en utilisant la positivité du
140                   CHAPITRE 5. ESPACES G-TROPICAUX CALIBRÉS

calibrage canonique, que l’on a en fait l’égalité, d’où (1). En appliquant le lemme 4.4.6
aux mesures de Radon correspondantes, on en déduit (2), puis (3) par intégration.

5.10.2. — La formule (5.10.1.1) définit explicitement l’intégrale d’une forme tropicale.
```

## CLD.txt, newline lines 7070–7101

```text


      § 6.2. FORMES LISSES SUR UN ESPACE G-TROPICAL AFFINÉ

  Soit G une classe de coefficients.
Définition 6.2.1. — Soit (p, q) un couple d’entiers naturels. Soit ω une G-forme de
type (p, q) à coefficients dans G sur un domaine V de X.
  On dit que ω est tropicale s’il existe une carte tropicale qui G-tropicalise ω.
  On dit que ω est une forme (de type (p, q) à coefficients dans G ) si pour tout point x
de V , il existe un voisinage ouvert U de x dans V sur lequel ω est tropicale.
  Lorsque G est la classe des fonctions lisses, on parle de forme lisse sur l’espace G-
tropical affiné X. Si de plus p = q = 0, on parle de fonction lisse.
6.2.2. — Les formes lisses forment un sous-G-préfaisceau en R-espaces vectoriels
de AXp,q qui est un faisceau pour la topologie usuelle. Ces faisceaux sont stables par les
opérateurs d′ , d′′ , J et par le produit extérieur.
6.2.3. — Un espace G-tropical affiné (X, LX ) est dit affinement séparé si pour tout
couple (x, y) de points de X avec x ̸= y, il existe une fonction affine f sur X telle que
f (x) ̸= f (y). A fortiori, les fonctions lisses sur X séparent les points. On dira alors que
X est différentiellement séparé.
   Si X est affinement (resp. différentiellement) séparé, il en est de même de tout domaine.
   Un espace G-tropical affiné (X, LX ) est dit localement affinement (resp. différentielle-
ment) séparé si chacun de ses points possède un voisinage affinement (resp. différentiel-
lement) séparé.
   Cela entraîne que le faisceau des fonctions lisses sépare localement les points au sens
du §A.2.2.
Corollaire 6.2.4. — Soit (X, LX ) un espace G-tropical affiné qui est localement dif-
férentiellement séparé. Soit K une partie compacte de X et soit U un voisinage ouvert
de K. Il existe une fonction lisse sur X qui vaut 1 au voisinage de K et dont le support
est compact et contenu dans U .
Démonstration. — C’est une conséquence du corollaire A.2.4.

Théorème 6.2.5 (Stone–Weierstraß). — Soit (X, LX ) un espace G-tropical affiné
```

## CLD.txt, newline lines 8130–8168

```text
forme positive est positive.                             R∂
   On définit aussi le courant [ω]∂ par la formule α 7→ X ω∧α défini à l’aide de l’intégrale
de bord des G-formes. Il est d’ordre 0 et de bidimension (n − p − 1, n − q). Lorsque ω
est une forme lisse, on a [ω]∂ = δX ∂
                                      ∧ ω.
   Il découle de la définition de la topologie des espaces de courants que les applications
ω 7→ [ω] et ω 7→ [ω]∂ sont continues.
7.3.5. — Nous allons maintenant généraliser cette construction aux « G-formes » qui
sont combinaisons linéaires de G-formes usuelles à coefficients dans un anneau de fonc-
tions non nécessairement tropicales.
   Soit V un domaine de X et soit U un voisinage ouvert de V dans X dans lequel V
est fermé. Soit u ∈ L1loc (V ), ω ∈ AXp,q
                                       G
                                          (V ) et α ∈ Acn−p,n−q (U ) ; la G-forme ω ∧ α|V est à
support compact
            R     dans V , de sorte que u est intégrable pour la mesure associée. L’appli-
cation α 7→ V u(ω ∧ α)Rad est un courant d’ordre 0 sur U . La section correspondante de
                              § 7.3. COURANTS D’INTÉGRATION                              165

π ∗ Dp,q (V ) ne dépend pas du choix de U . On définit ainsi un morphisme de G-faisceaux
                                L1loc,X ⊗ AXp,q
                                             G
                                                → π ∗ (Dp,q )X .
Par adjonction, on en déduit un morphisme de faisceaux
                            π∗ (L1loc,X ⊗ AXp,q
                                             G
                                                ) → π∗ π ∗ (Dp,q )X .
Comme l’unité id → π∗ π ∗ est un isomorphisme de foncteurs, on en déduit un morphisme
de faisceaux
                               π∗ (L1loc,X ⊗ AXp,q
                                                G
                                                   ) → (Dp,q )X .
   L’image d’une section ω sera notée [ω]. La notation est cohérente avec le cas des G-
formes lisses ; via l’isomorphisme de la proposition 3.4.11, elle est aussi cohérente avec
les cas des G-formes à coefficients tropicalement boréliens localement bornés. Ce courant
est d’ordre 0 et de bidimension (n − p, n − q).
   Par composition avec l’homomorphisme canonique
                               1
                         π∗ (Lloc,X ⊗ AXp,q
```

## CLD.txt, newline lines 16809–16927

```text
Définition 12.2.1. — Soit X un espace k-analytique ; on appelle moment sur X un
morphisme de X vers un tore.

   Soit f : X → T un moment sur un espace k-analytique X. On désignera par ftrop : X →
Ttrop l’application composée X → T → Ttrop . On dira que l’application ftrop est la
tropicalisation de f ; c’est une application continue.

Remarque 12.2.2. — Si f : T → T ′ est un morphisme affine entre tores, la nota-
                                                                  ′
tion ftrop désigne donc aussi bien l’application induite Ttrop → Ttrop que sa composée
        ′     ′
T → T → Ttrop avec l’application de tropicalisation de T . Cette ambiguïté n’aura, en
pratique, guère de conséquences.

Lemme 12.2.3. — Soit X un espace analytique, soit x un point de X et soit V un
domaine analytique de X contenant x. Soit f : V → Gm une fonction analytique in-
versible. On suppose que X est presque bon en x. Il existe alors un voisinage ouvert U
de x et une fonction analytique inversible g sur U telle que |f − g| < |f | sur U ∩ V ; en
particulier, ftrop et gtrop coïncident sur U ∩ V .
                      § 12.2. MOMENTS, TROPICALISATIONS, POLYÈDRES                         335

Démonstration. — Soit U un voisinage ouvert de x dans X et g ∈ OX (U ) tels que
|f (x) − g(x)| < |f (x)| ; il en existe car κ(x) est dense dans H (x) et |f (x)| > 0. L’en-
semble des points de U ∩ V en lesquels |f − g| < |f | est un voisinage de x dans V ; quitte
à restreindre U , on peut supposer que cette inégalité vaut dans U ∩ V tout entier. Quitte
à restreindre encore U , on peut supposer que g est inversible sur U , d’où le lemme.

Théorème 12.2.4. — Soit X un espace k-analytique compact et soit f : X → T un
moment. Le sous-espace compact ftrop (X) est un polyèdre de Ttrop de dimension dim(X).
   L’assertion a été établie par Berkovich dans le cas où X est G-localement algébrisable,
cf. [11], cor. 6.2.2. Pour le cas général, on pourra se reporter à [46], §3.30, ou à [50],
th. 3.2.
Corollaire 12.2.5. — Soit X un espace k-analytique compact et soit V une partie
fermée de X munie d’une structure faiblement analytique de dimension d. Soit f : X → T
un moment. Alors, ftrop (V ) est une partie paralinéaire de dimension ⩽ d de Ttrop .
Démonstration. — On se ramène immédiatement au cas où il existe un morphisme
g : X → Y et un point y ∈ Y tel que V = g −1 (y). Alors, le produit fibré X ×Y H (y)
permet de considérer V comme un espace H (y)-analytique compact, de dimension ⩽ d,
et f |V : V → TH (y) comme un moment sur cet espace. On donc dim(ftrop (V )) ⩽ d.

Corollaire 12.2.6. — Soit X un espace k-analytique compact de dimension n. Soit
f : X → T un moment. Si X est affinoïde, alors ftrop (∂(X)) est une partie paralinéaire
de dimension ⩽ n − 1 de Ttrop ; en genéral, ftrop (∂(X)) est contenu dans une telle partie
paralinéaire.
Démonstration. — Compte tenu de l’exemple 11.10.2 selon lequel ∂(X) est une partie
faiblement analytique de dimension ⩽ dim(X) − 1, cela résulte du corollaire précédent.
Il s’agit en fait du théorème 3.2 de [50], démontré de la même façon, même si la notion
de structure faiblement analytique n’avait pas été dégagée.

12.2.7. — Soit X un espace k-analytique et f : X → T un moment. Soit x ∈ X. On
appellera degré de transcendance résiduel (gradué) de f en x le degré de transcendance
résiduel torique du point f (x) de T . Si χ1 , . . . , χn est une base de X(T ), ce degré est
le degré de transcendance sur ek du sous-corps gradué de H         ^  (x) engendré par e
                                                                                       k et les
χi^◦ f (x). Si T = Gn et f = (f1 , . . . , fn ), c’est donc le degré de transcendance sur e
                     m                                                                    k du
sous-corps gradué de H ^ (x) engendré par e k et les f]
                                                      i (x).
   Le degré de transcendance résiduel de f en x est majoré à la fois par dk (x) et par n.
Il vaut n si et seulement si f (x) ∈ S(T ).
Proposition 12.2.8. — Soit X un espace k-analytique et soit x un point de X. Soit
f = X → T un moment ; posons ξ = ftrop (x). Notons d le degré de transcendance
résiduel de f en x.
   Il existe un voisinage analytique compact U de x dans X tel que pour pour tout voi-
sinage analytique compact V de x contenu dans U , on ait les propriétés suivantes :
   i) Les germes de polyèdres (ftrop (U ), ξ) et (ftrop (V ), ξ) coïncident ;
   ii) La dimension locale dimξ (ftrop (V )) est majorée par d, et a fortiori par dk (x).
336           CHAPITRE 12. PARTIES SQUELETTIQUES D’UN ESPACE ANALYTIQUE

   iii) Si x ̸∈ ∂(X), alors ftrop (V ) est purement de dimension d en ξ. Si, de plus, d = n,
alors ftrop (V ) est un voisinage de ξ dans Ttrop .
   iv) Si dimξ (ftrop (V )) = n, alors f (x) ∈ S(T ) ; inversement, si f (x) ∈ S(T ) et si de
plus x ∈ / ∂(X), alors dimξ (ftrop (V )) = n.
Démonstration. — L’existence d’un voisinage analytique U vérifiant les i), ii) et iii) est
le théorème 3.4 de [50]. Montrons (iv). Si dimξ (ftrop (V )) = n, il résulte de (ii) que n ⩽ d,
donc que d = n et que f (x) ∈ S(T ). Réciproquement, si f (x) ∈ S(T ) alors d = n et si
de plus x ∈
          / ∂X il résulte de (iii) que dimξ (ftrop (V )) = n.

Remarque 12.2.9. — Soit X un espace k-analytique et soit x ∈ X. Soit f : X → Gnm
un moment. Si V est un voisinage analytique compact de x dans X, il résulte de la
proposition ci-dessus que le germe de ftrop (V ) en x ne dépend pas de V . Nous le noterons
ftrop (X, x).
   La preuve du théorème 3.4 de [50] en donne une description en termes de réduction
de Temkin, que nous allons rappeler ici, en supposant que le germe est (X, x) séparé.
   Le théorème 10.5.7 assure (en reprenant le vocabulaire et les notations de 10.5.6)
l’existence d’un sous-foncteur D de Dn{1} tel que pour tout H ∈ D et tout n-uplet
(h1 , . . . , hn ) d’éléments de H, les assertions suivantes soient équivalentes :
   (i) h ∈ D(H) ;
   (ii) il existe H ′ ∈ DH et une valuation w appartenant à (X,   ^   x) à valeurs dans H ′ telle
que w(f]     i (x)) = hi pour tout i.
Comme le groupe des paramètres est ici {1}, le foncteur D est simplement définiQpar
conjonctions et disjonctions d’inégalités de la forme φ ⩽ 1 où φ est un monôme xri i
à exposants rationnels. L’ensemble D(R×      + ) est alors un cône rationnel, et ftrop (X, x) =
                ×
(ftrop (x) · D(R+ ), ftrop (x)) en notation multiplicative.
                                                      ^
  En particulier, si x est intérieur, c’est-à-dire si (X, x) = P       , ce germe de polytope
                                                                 H
                                                                 ^ (x)/e
                                                                       k

ne dépend que de la classe d’isomorphie de l’extension graduée F de e       k dans H^  (x)
engendrée par les f]
                   i (x), munie de cette famille. Dans ce cas, il est équidimensionnel, de
dimension égale au degré de transcendance (gradué) de F sur e    k.
Définition 12.2.10. — Soit X un espace analytique et soit f : X → T un moment.
Soit x un point de X. On appelle dimension tropicale de f en x la borne inférieure de di-
mensions des polyèdres ftrop (V ), où V est un domaine analytique compact qui contient x.
On la note dimtrop,x (f ).
  Soit d le degré de transcendance résiduel de f en x. D’après le théorème 12.2.4 et la
proposition 12.2.8, on a
(12.2.10.1)                 dimtrop,x (f ) ⩽ d ⩽ dk (x) ⩽ dimx (X),
et dimtrop,x (f ) = d si x ∈
                           / ∂X. Si X est compact, il résulte de la définition que
(12.2.10.2)                   dim(ftrop (X)) = sup dimtrop,x (f ).
                                                x∈X

Proposition 12.2.11. — Soit X un espace analytique, soit x un point de X ∂(X).
```

## CLD.txt, newline lines 18040–18119

```text
      § 12.8. POLYÈDRES CARACTÉRISTIQUES ET DIMENSION
                            TROPICALE

12.8.1. — Soit X un espace k-analytique de niveau n, soit m un entier et soit f =
X → Gm   m un moment sur X. On note (f1 , . . . , fm ) les composantes de f . Pour toute
partie I de {1, . . . , m}, on note qI la projection canonique de Gm      I
                                                                   m sur Gm .
  Rappelons (proposition 12.6.8) que le polyèdre caractéristique de f est une partie
paralinéaire de X et que l’application ftrop |Σf est une immersion par morceaux d’espaces
paralinéaires.
  Le but de ce numéro est de relier la dimension tropicale de ftrop aux propriétés de Σf .
Théorème 12.8.2. — Soit x un point de X.
                                                                    (n)
   a) On a dimtrop,x (f ) ⩽ n, avec égalité si et seulement si x ∈ Σf .
   b) Supposons x ∈ Int(X). Les trois assertions suivantes sont équivalentes : (i) x ∈ Σf ;
                                                        (n)
(ii) f est de dimension tropicale n en x ; (iii) x ∈ Σf .
   c) Si X est compact ou plus généralement si l’application ftrop est topologiquement
                                    (n)
propre, on a ftrop (X)(n) = ftrop (Σf ).
Démonstration. — a) Soit d le degré de transcendance résiduel de f en x. On a
dimtrop,x (f ) ⩽ d ⩽ dimx X ((12.2.10.1)). Comme dimx X ⩽ n, il vient dimtrop,x (f ) ⩽
d ⩽ n.
                                                              (n)
   Supposons que dimtrop,x (f ) = n, et montrons que x ∈ Σf . Puisque dimtrop,x (f ) ⩽
d ⩽ n, on a d = n. Il existe donc un sous-ensemble I de cardinal d de {1, . . . , m}
tels que les f] i (x) soient algébriquement indépendants sur k. ll s’ensuit que x ∈ Σf . Il
                                                             e
reste à vérifier que dimx (Σf ) = n. Soit V un voisinage analytique compact arbitraire
de x dans X et démontrons que dim(Σf ∩ V ) = n. Comme dimtrop,x (f ) = n, on a
dim(ftrop (V )) = n. Soit C une cellule compacte de dimension n de ftrop (V ) et soit
             § 12.8. POLYÈDRES CARACTÉRISTIQUES ET DIMENSION TROPICALE                     357

q : Gm        n
      m → Gm un morphisme de tores tel que la restriction de qtrop à ⟨C⟩ soit injective.
                                                                            (n)
Alors, dim(q ◦ f )trop (V ) = n. D’après le lemme 12.2.13, (q ◦ f )trop (V )sq est contenu dans
(q ◦f )(V ), donc dans (q ◦f )(Σf ∩V ). Comme dim(Σf ∩V ) ⩾ n, il vient dim(Σf ∩V ) = n,
ce qu’il fallait démontrer.
                                          (n)
   Inversement, supposons que x ∈ Σf et montrons que dimtrop,x (f ) = n. Soit V un
                                         (n)                                (n)
voisinage compact de x. Alors, V ∩ Σf est un voisinage de x dans Σf , donc contient
une cellule de dimension n puisque dimx Σf = n par hypothèse. Comme la restriction
               (n)
de ftrop à Σf est une immersion par morceaux, cela prouve que dim(ftrop (V )) ⩾ n,
et donc que dim(ftrop (V )) = n puisque dim V ⩽ n. Comme V est arbitraire, il vient
dimtrop,x (f ) = n.
   b) Faisons l’hypothèse que x ∈ Int(X). Supposons x ∈ Σf . Il existe alors un sous-
ensemble I de {1, . . . , m} tels que les f]   i (x) pour i ∈ I soient algébriquement indépen-
dantes sur k ; par conséquent, d ⩾ n, si bien que d = n puisqu’on sait que d ⩽ n. Et
              e
comme x ∈ Int(X), la dimension tropicale de f en x est égale à d (12.2.10.1), et donc
à n.
   Supposons réciproquement que x est de dimension tropicale n en x. Le point x appar-
                  (n)
tient alors à Σf d’après (a).
   L’implication (iii)⇒(i) est évidente.
   c) Supposons ftrop topologiquement propre. En raisonnant G-localement sur Rm on
                                           (n)
voit que ftrop (X), ftrop (Σf ) et ftrop (Σf ) sont des parties paralinéaires fermées de Rm .
                                                                                           (n)
Comme ftrop induit une immersion par morceaux de Σf sur ftrop (Σf ), l’image ftrop (Σf )
est purement de dimension n et est donc contenue dans ftrop (X)(n) .
                                                                         (n)
  Soit maintenant ξ un point de ftrop (X) qui n’appartient pas à ftrop (Σf ). Soit x un
                                                     (n)
point de X tel que ftrop (x) = ξ ; on a donc x ̸∈ Σf . D’après a), ftrop est de dimension
tropicale < n en x. Comme ftrop est topologiquement propre, il existe un voisinage
                             −1
analytique compact V de ftrop   (ξ) et un voisinage paralinéaire U de ξ dans ftrop (X) tels
      −1
que ftrop (U ) ⊂ V et que dim(ftrop (V )) ⩽ n−1. Puisque U ⊂ ftrop (V ), il est de dimension
au plus n − 1 et ξ n’appartient à ftrop (X)(n) .

Corollaire 12.8.3. — Soit X un espace k-analytique de niveau n et soit f : X → T un
                  (n)                                             (n)
moment. Alors Σf coïncide avec le polyèdre de variation maximale Σftrop de l’application
paralinéaire ftrop (définition 5.2.1).
Démonstration. — C’est l’assertion a) du théorème 12.8.2.
```

## CLD.txt, newline lines 19153–19240

```text
Lemme 13.2.8 (Longueur générique et extension des scalaires)
    Soit X un espace k-analytique et soit K une extension complète de k. Soit F un
faisceau cohérent sur X. Soit Z une composante irréductible de X, soit ℓ la longueur
générique de X le long de Z, soit ℓK la longueur générique de FK le long de ZK , et soit
µ la multiplicité générique de Xred,K le long de ZK . On a alors ℓK = µℓ.
                                                   gen     gen
Démonstration. — Choisissons un point y sur ZK         ⊂ XK    dont on note x l’image sur
X ; par construction, x ∈ Z. L’anneau local OXK,G ,y est artinien car y ∈ XK    gen
                                                                                    , et il est
plat sur OXG ,x (13.1.5) ; ce dernier est donc également artinien, ce qui montre que x
appartient à X gen , et donc à Z gen car x ∈ Z.
   Pour alléger les notations posons A = OXG ,x , B = OXK,G ,y et M = FXG ,x . On note m
l’idéal maximal de A et κ = A/m son corps résiduel. Enfin on pose B ′ = B/mB = κ⊗A B.
Remarquons que κ = OXred,G ,x et B ′ = OXred,K,G ,y (proposition 13.1.9 d ) et c)).
   Par définition de ℓ il existe une filtration

                             {0} = M0 ⊂ M1 ⊂ . . . ⊂ Mℓ = M

du A-module M dont les quotients successifs sont A-isomorphes à κ. Comme B est plat
sur A, cette filtration en induit une

                {0} = B ⊗A M0 ⊂ B ⊗A M1 ⊂ . . . ⊂ B ⊗A Mℓ = B ⊗A M

dans la catégorie des B-modules dont les quotients successifs sont tous B-isomorphes à
B ′ . Il vient
                    ℓK = ℓB (B ⊗A M ) = ℓ · ℓB (B ′ ) = ℓ · ℓB ′ (B ′ ) = ℓµ.
378              CHAPITRE 13. COMPLÉMENTS DE GÉOMÉTRIE ANALYTIQUE

§ 13.3. DEGRÉ ET DEGRÉ CALIBRÉ D’UN MORPHISME QUASI-FINI

13.3.1. — Soit f : Y → X un morphisme d’espaces k-analytiques. Soit y ∈ Y . Si
dimy (f −1 (f (y)) > 0, on pose degy (f ) = +∞. Sinon, le point y est isolé dans sa fibre
f −1 (f (y)), l’anneau local de f −1 (f (y)) en y est une H (f (y))-algèbre de dimension finie
et on note degy (f ) sa dimension.
   Lorsque f est fini et plat en y, cet entier degy (f ) coïncide avec l’entier degy (f ) défini
en 11.6.3.
   Nous dirons que degy (f ) est le degré de f en y.
   Soit V un domaine analytique de Y contenant y et soit U un domaine analytique
de X tel que f (V ) ⊂ U ; soit g : V → U le morphisme déduit de f . Pour tout y ∈ V , on
a degy (f ) = degy (g), car pour tout y ∈ V d’image x ∈ X, les anneaux locaux en y de
f −1 (f (y)) et de g −1 (g(y)) coïncident.
   Soit Z un sous-espace analytique fermé de X contenant x et soit g : Y ×X Z → Z le
morphisme déduit de f par changement de base. Comme les espaces H (x)-analytiques
f −1 (x) et g −1 (x) coïncident, on a degy (f ) = degy (g).
13.3.2. — Soit f : Y → X un morphisme d’espaces k-analytiques. Pour tout x ∈ X,
on définit de le degré de f au-dessus de x comme la somme
                                            X
                               degx (f ) =     degy (f ).
                                              y∈f −1 (x)


Il est fini si et seulement si f −1 (x) est compact et de dimension nulle ; alors f −1 (x) est
un espace analytique fini sur H (x), et degx (f ) = dimH (x) (O(f −1 (x))).
   Lorsque f est globalement fini et plat, cet entier degx (f ) coïncide avec l’entier degx (f )
défini en 11.6.1.

Lemme 13.3.3. — Soit f : Y → X un morphisme d’espaces analytiques. Soit K une
extension valuée complète de k ; notons p : XK → X et q : YK → Y les morphismes de
changement de base, et fK : YK → XK le morphisme déduit de f par changement de
base. Soit xK ∈ p−1 (x).
  a) Pour tout y ∈ Y d’image x = f (y) ∈ X, tout point xK ∈ p−1 (x), on a
                                        X
                         degy (f ) =              degz (fK ).
                                           −1
                                        z∈fK  (xK )∩q −1 (y)


  b) Pour tout x ∈ X et tout point xK ∈ p−1 (x), on a degx (f ) = degxK (fK ).

Démonstration. — Tout se passe dans les fibres f −1 (x) et fibre fK−1 (xK ) = f −1 (x) ×
M (H (xK )). Cela permet de supposer que X = M (k) = {x} et XK = M (K) = {xK }.
  Prouvons l’égalité a). Si dimy (Y ) > 0, il en est de même de dimz (YK ) pour tout
antécédent z de y, si bien que les deux membres de l’égalité sont infinis. Supposons
maintenant dimy (Y ). Alors OY,y est une k-algèbre artinienne et OY,y ⊗k K = z OYK ,z ,
                                                                              Q
où z parcourt l’ensemble des antécédents de y dans YK . L’égalité s’ensuit.
  L’égalité b) s’en déduit en sommant sur tous les points de Y .
               § 13.3. DEGRÉ ET DEGRÉ CALIBRÉ D’UN MORPHISME QUASI-FINI                    379

13.3.4. — Soit A un anneau local artinien et soit M un A-module de longueur finie.
Nous noterons δA (M ) le nombre rationnel ℓA (M )/ℓA (A). Indiquons quelques propriétés
élémentaires de cet invariant.
   Si A est réduit, c’est un corps, on a ℓA (A) = 1 et δA (M ) est donc simplement ℓA (M ),
c’est-à-dire la dimension de M comme A-espace vectoriel.
   Supposons M plat sur A, c’est-à-dire libre comme A-module ; soit r son rang. Comme
M ≃ Ar , ℓA (M ) = rℓA (A), si bien que δA (M ) = r.
   Si M = Ared , alors ℓA (M ) = 1 et δA (M ) = 1/ℓA (A).
   Soit B une A-algèbre finie. Soit κ le corps résiduel de A et λ celui de B. Choisis-
```

## CLD.txt, newline lines 18355–18407

```text
Théorème 12.9.11. — Soit X un espace k-analytique de niveau n. Soit L une exten-
sion complète de k et notons p : XL → X la projection canonique. Soit Σ une partie sque-
lettique de X ; notons ΣL la réunion des polyèdres caractéristiques ΣfL , où f : V → T
parcourt l’ensemble des moments définis sur un domaine analytique V de X tels que
Σf ⊂ Σ.
   L’ensemble ΣL est une partie squelettique de XL et le morphisme p induit une immer-
sion par morceaux surjective de ΣL sur Σ qui préserve la dimension locale.
   De plus, pour tout moment f : V → T tel que Σf ⊂ Σ, on a ΣL ×Σ Σf = ΣfL .

Démonstration. — La première assertion est G-locale sur X ; comme elle est vérifiée
pour l’application ΣfL → Σf , il suffit de démontrer la seconde assertion.
   Soit f : V → T un moment défini sur un domaine analytique V de X. Démontrons
l’égalité PL ×P Σf = ΣfL . Cela revient à démontrer que si g : W → T ′ est un moment et
x ∈ Σf ∩Σg , alors les fibres de ΣfL et ΣgL au-dessus de x coïncident. Quitte à remplacer X
par V ∩ W , on suppose que les moments f et g sont définis sur X.
   Soit x ∈ Σf ∩ Σg . Soit C la complétion d’une clôture algébrique de k et soit M une
extension complète composée de L et C. Considérons le diagramme

                                               XM   →
                                                           σ
                                         q′
                                         →    ←      ←
                                                       →
                                                           ←

                                    XL                  XC
                                         ←             ←
                                         p →
                                                   →   q

                                               X
dans lequel σ est la section de Poineau de l’application XM → XC dont l’existence
résulte de ce que C est algébriquement clos. Comme l’extension C/k contient une sous-
extension algébrique dense, on a ΣfC = q −1 (Σf ). Comme C est algébriquement clos, on
a ΣfM = σ(ΣfC ). Enfin, on a ΣfL = q ′ (ΣfM ). Par suite,
                                  ΣfL = q ′ (σ(q −1 (Σf ))),
donc la fibre de ΣfL au-dessus de x est donnée par la formule
                                   ΣfL ,x = q ′ (σ(q −1 (x)))
dans laquelle Σf n’intervient plus ; cette fibre coïncide donc avec la fibre de ΣgL au-dessus
de x. Cela conclut la démonstration du théorème.
  Le cas des polyèdres caractéristiques et la définition de ΣL entraînent de plus la
caractérisation suivante :

Proposition 12.9.12. — Conservons les notations du théorème 12.9.11.
   a) Si l’extension L/k possède une sous-extension algébrique dense, alors ΣL = p−1 (Σ) ;
   b) Si l’extension L/k est universellement multiplicative, ou si le corps le corps k est
algébriquement clos, on a ΣL = σL (Σ).

Démonstration. — Compte tenu de la seconde assertion du théorème, l’assertion a)
découle de la proposition 12.7.2, et l’assertion b) du corollaire 12.7.5.
                  § 12.9. PARTIES SQUELETTIQUES D’UN ESPACE ANALYTIQUE                         363

Lemme 12.9.13. — Soit X un espace k-analytique de niveau n, soit Σ une partie
```

## CLD.txt, newline lines 20320–20360

```text
                           § 14.2. MOMENTS ET DEGRÉS

Lemme 14.2.1. — Soit X un espace analytique de niveau n, soit f : X → Gnm un
moment. Alors, f est quasi-fini et plat en tout point de Σf .
Démonstration. — Soit x ∈ Σf . On a f (x) ∈ S(Gnm ), donc dk (f (x)) = n. D’après
le lemme 11.5.1, le morphisme f est quasi-fini en x. Comme Gnm est réduit, le théo-
rème 10.3.7 de [52] entraîne que f est plat en x.

Proposition 14.2.2. — Soit X un espace analytique de niveau n, soit f : X → T un
moment sur X et soit C une f -cellule commode de dimension n de X. Soit q : T → Gnm
un morphisme de tores tel que qtrop |ftrop (C) est injectif. Alors le morphisme q ◦ f est de
dimension relative nulle en tout point de C et il existe un unique entier d > 0 tel que ce
morphisme soit fini et plat de degré d en tout point de C̊.
Démonstration. — Soit q : T → Gnm un morphisme de tores tel que qtrop soit injectif sur
ftrop (C). La dimension tropicale de q ◦ f est égale à n en tout point de C, donc C ⊂
(q ◦f )−1 (S(Gnm )) d’après la prop. 12.2.8, (iv). D’après le lemme 11.5.1, le morphisme q ◦f
est de dimension relative nulle en tout point de C.
   Comme C̊ ne rencontre pas ∂(X), il résulte du lemme 11.6.5 que le morphisme q ◦f est
fini et plat en tout point de C̊ ; on a noté degx (q ◦ f ) son degré et il s’agit de démontrer
que l’entier degx (q ◦ f ) est indépendant du point x ∈ C̊.
   Soit D la cellule sq(qtrop (ftrop (C))) de Gnm . Si un point x ∈ Int(X) vérifie q ◦ f (x) ∈ D̊,
                                                                                 (n)
alors q◦f est de dimension tropicale n en x, donc f aussi, si bien que x ∈ Σf . Autrement
dit, on a les inclusions
                                                                (n)
                             C̊ ⊂ (q ◦ f )−1 (D̊) ∩ Int(X) ⊂ Σf .
                                                                        (n)
   Soit maintenant x ∈ C̊. Par hypothèse, C̊ est ouvert dans Σf ; il est donc ouvert
dans (q ◦ f )−1 (D̊) ∩ Int(X). Comme q ◦ f est fini et plat en x, il existe un voisinage
ouvert U de x dans Int(X) et un voisinage ouvert V de q ◦ f (x) dans Gnm tels que
q ◦ f induise un morphisme fini et plat de degré degx (q ◦ f ) de U sur V , et tel que
(q ◦ f )−1 (D̊) ∩ U ⊂ C̊. Un point y ∈ C̊ ∩ U est alors le seul antécédent dans U de
q ◦ f (y) par q ◦ f ; on a donc degy (q ◦ f ) = degx (q ◦ f ) pour tout y ∈ C̊ ∩ U . La
fonction x 7→ degx (q ◦ f ) est localement constante sur l’ensemble C̊ ; comme celui-ci est
connexe, elle est constante.
400           CHAPITRE 14. CALIBRAGE CANONIQUE D’UN ESPACE ANALYTIQUE

Proposition 14.2.3. — Soit X un espace k-analytique paracompact de niveau n et
soit f : X → Gnm un moment. Soit Σ un sous-espace paralinéaire paracompact de Σf .
Il existe une décomposition cellulaire C de Σ en f -cellules telle que pour toute cellule
C ∈ C , l’application x 7→ degx (f ) soit finie et constante sur C̊.
```

## CLD.txt, newline lines 20700–20870

```text
de l’anneau local de (g ′ )−1 (g ′ (y)) en g ′ (y). Considérons X × Gdm comme Gdm,X ; alors
406           CHAPITRE 14. CALIBRAGE CANONIQUE D’UN ESPACE ANALYTIQUE

g ′ (y) s’identifie au point g|Yx (y) de Gdm,H (x) . De même, la fibre (g ′ )−1 (g ′ (y)) s’identifie à
la fibre (g|Yx )−1 (g|Yx (y)). Il en résulte l’égalité degy (g ′ ) = degy (g|Yx ).
                                   ′                                            ′
     Démontrons enfin que degg (y) (f ′ ) = degx (f ). Par définition, degg (y) (f ′ ) est la dimen-
sion sur f ′ (g ′ (y)) = h(y) de l’anneau local de (f ′ )−1 (h(y)) en g ′ (y). Le morphisme f ′
est déduit de f par changement de base. Ainsi, (f ′ )−1 (h(y)) = f −1 (f (x)) ⊗H (f (x))
H (h(y)). L’anneau local de f −1 (f (x)) en x est une algèbre locale artinienne de di-
mension degx (f ) sur H (x). Son produit tensoriel par H (h(y)) est le produit des an-
neaux locaux de (f ′ )−1 (h(y)) en tous les antécédents de x. Pour conclure la démons-
tration de l’égalité voulue, il suffit de démontrer que le point x n’a qu’un seul an-
técédent dans (f ′ )−1 (h(y)). Cela résulte du fait que H (f (x)) est séparablement clos
dans H (h(y)) : le point h(y) appartient à S(Gnm,H (f (x)) ), le corollaire 12.1.8 s’applique
donc.



                        § 14.3. CALIBRAGES CANONIQUES

  Soit X un espace analytique de niveau n.
Proposition 14.3.1. — Soit f : X → T un moment et soit C une f -cellule de dimen-
                                                                                 ′
sion n. Soit q et q ′ des morphismes de tores de T dans Gnm tels que qtrop et qtrop  soient in-
jectifs sur ftrop (C). Soit σq l’unique section affine de qtrop dont l’image contient ftrop (C) ;
on définit σq′ de façon analogue.
   Soit µ un vecteur-volume sur Rn . Pour presque tout x ∈ C, on a l’égalité
(14.3.1.1)                  degx (q ◦ f )σq,∗ (µ) = degx (q ′ ◦ f )σq′ ,∗ (µ)
de vecteurs volumes sur l’espace affine ⟨ftrop (C)⟩.
Démonstration. — Notons Cf = ftrop (C).
  Supposons d’abord que q ′ soit de la forme φ ◦ q, où φ : Gnm → Gnm est un morphisme
surjectif de tores. D’après la proposition 13.3.10, on a
                  degx (q ′ ◦ f ) = degx (φ ◦ q ◦ f ) = degq◦f (x) (φ) degx (q ◦ f ).
Le morphisme φ est fini et plat et pour tout t ∈ S(Gnm ), on a degt (φ) = deg(φ), en vertu
du corollaire 12.1.7. Par suite, on a degx (q ′ ◦ f ) = deg(φ) degx (q ◦ f ) pour tout x ∈ C.
   Par ailleurs, φtrop est une application affine bijective de Rn dans lui-même et l’on a
σq′ = σq ◦φ−1                                                                    →
                                                                                 −
              trop . La valeur absolue du déterminant de l’application linéaire φ trop est égale
au degré de φ. Par suite, φ−1                                                 −1
                                trop applique le vecteur volume µ sur deg(φ) µ, de sorte que
σq′ ,∗ (µ) = deg(φ)−1 σq,∗ (µ). La relation voulue est donc vérifiée dans ce cas particulier.
                               ′
   Supposons ensuite que qtrop    − qtrop soit constante sur Cf . D’après le théorème 14.2.7,
          x                 x ′
on a deg (q ◦ f ) = deg (q ◦ f ) pour tout x ∈ C ∩ Int(X) ; d’autre part, C ∩ ∂(X)
est localement négligeable. De plus, σq et σq′ diffèrent d’une constante, si bien que
σq,∗ (µ) = σq′ ,∗ (µ). Cela prouve la relation voulue dans ce cas.
   Montrons maintenant comment la conjonction de ces deux cas permet d’obtenir le
cas général. Notons ψ l’unique application linéaire de Rn dans lui-même telle que ψ ◦
          ′
qtrop et qtrop diffèrent d’une translation sur Cf . Compte tenu de la convention faite
au paragraphe 12.1.13, l’espace affine ⟨Cf ⟩ est Q-rationnel, si bien que ψ appartient
                                 § 14.3. CALIBRAGES CANONIQUES                                  407

à GLn (Q). Il existe donc deux morphismes de tores φ et φ′ de Gnm dans lui-même tels
que φ′trop ◦ ψ = φtrop . Ainsi, (φ′ ◦ q ′ ◦ f )trop et (φ ◦ q ◦ f )trop diffèrent d’une constante
                       −1
sur C. Posons V = ftrop   (Cf ) ; c’est un domaine analytique fermé de X qui contient C.
                ′  ′
Sur V , on a (φ ◦ q ◦ f )trop = (φ ◦ q ◦ f )trop .
  D’après le premier cas particulier, on a donc presque partout les relations

                     degx (φ ◦ q ◦ f |V )σφ◦q,∗ (µ) = degx (q ◦ f |V )σq,∗ (µ)

et
                   degx (φ′ ◦ q ′ ◦ f |V )σφ′ ◦q′ ,∗ (µ) = degx (q ′ ◦ f |V )σq′ ,∗ (µ).
D’autre part, il résulte du second cas particulier traité que

                degx (φ ◦ q ◦ f |V )σφ◦q,∗ (µ) = degx (φ′ ◦ q ′ ◦ f |V )σφ′ ◦q′ ,∗ (µ).

Comme V est un domaine de X contenant x, on a les égalités de degrés

             degx (q ◦ f |V ) = degx (q ◦ f ) et         degx (q ′ ◦ f |V ) = degx (q ′ ◦ f )

pour tout x ∈ V . Cela conclut la démonstration de la proposition.

14.3.2. — Soit Σ une partie squelettique de X, paracompacte et contenue dans le
polyèdre caractéristique Σf d’un moment f : V → T défini sur un domaine analytique V
de X. Nous allons définir un calibrage µΣ de Σ.
   Soit C une décomposition cellulaire de Σ en f -cellules commodes (lemme 14.1.5).
Soit C une cellule de dimension n appartenant à C . Soit q : T → Gnm un morphisme de
tores tel que qtrop soit injectif sur ftrop (C). D’après la proposition 14.2.2, le morphisme
q ◦f est fini et plat sur C̊ et son degré x 7→ degx (q ◦f ) prend une valeur finie, strictement
positive et constante dC sur C̊. Notons e = |e1 ∧ · · · ∧ en | le vecteur-volume canonique
de Rn , considéré comme un calibrage constant, et posons µC = dC (q ◦ f )∗trop (e) ; c’est
un calibrage standard de la cellule C. Il ne dépend pas du choix de q d’après la propo-
sition 14.3.1. La famille (µC ) définit un calibrage standard de Σ ; on le note µΣ,f,C .
   Vérifions que ce calibrage est indépendant du choix de (V, f, C ).
   Soit V ′ un domaine analytique de X, soit f ′ : V ′ → T ′ un moment tel que Σ ⊂ Σf ′ et
soit C ′ une décomposition cellulaire de Σ en f ′ -cellules commodes. Posons W = V ∩ V ′
et soit g le moment (f, f ′ ) sur W et considérons une décomposition cellulaire D de Σ en
g-cellules commodes qui est adaptée aux décompositions cellulaires C et C ′ .
   Soit D une cellule de dimension n appartenant à D. Soit q : T → Gnm un morphisme
de tores tel que qtrop est injectif sur ftrop (D). Notons aussi p : T × T ′ → T la première
projection.
   Soit C une cellule de C contenant D. Comme D̊ ne rencontre pas ∂(W ), il est contenu
dans Int(W/V ), si bien que q ◦ f |W est fini et plat de degré dC en tout point de D̊. Il
existe aussi un entier dD > 0 tel que (q ◦ p) ◦ g soit fini et plat de degré dD en tout point
de D̊ (proposition 14.2.2). Comme on a (q ◦ p) ◦ g = q ◦ f |W , on a dC = dD . Par ailleurs,
(q ◦ g)∗trop (e) = (q ◦ f )∗trop (e). Par suite, les triplets (V, f, C ) et (W, g, D) induisent le
même calibrage sur D.
   Cela entraîne que le calibrage µΣ,f,C de Σ déduit de (V, f, C ) coïncide avec celui déduit
de (W, g, D) ; par symétrie, il coïncide avec celui déduit de (V ′ , f ′ , C ′ ). Notons-le µΣ .
408          CHAPITRE 14. CALIBRAGE CANONIQUE D’UN ESPACE ANALYTIQUE

14.3.3. — Soit Σ′ un sous-espace paralinéaire de Σ. Soit C ′ une décomposition cellu-
laire de Σ en f -cellules commodes qui raffine C ∩ Σ′ . La description de µΣ′ ,f,C ′ entraîne
alors l’égalité µΣ |Σ′ = µΣ′ .
Lemme 14.3.4. — Soit X un espace analytique de niveau n et soit Σ une partie sque-
lettique de X. Il existe un unique calibrage µΣ de Σ vérifiant la propriété suivante : pour
tout domaine analytique V de X, tout moment f sur V et tout sous-espace paralinéaire Σ′
de Σf ∩ Σ qui est paracompact, on a µΣ |Σ′ = µΣ′ . Ce calibrage µΣ est standard.
Démonstration. — Par définition, l’espace squelettique Σ est G-recouvert par des sous-
espaces paralinéaires Σ′ comme dans l’énoncé. Les calibrages formant un G-faisceau, il
existe au plus un tel calibrage. Pour démontrer son existence, il suffit alors de vérifier
la condition de coïncidence. Or, si Σ′ est Σ′′ sont des sous-espaces paralinéaires de Σ
satisfaisant les conditions de l’énoncé, on a µΣ′ |Σ′ ∩Σ′′ = µΣ′ ∩Σ′′ = µΣ′′ |Σ′ ∩Σ′′ d’après le
paragraphe 14.3.3.

Définition 14.3.5. — Soit X un espace analytique de niveau n, topologiquement sé-
paré, et soit Σ une partie squelettique de X. On appelle calibrage canonique de Σ le
calibrage dont le lemme 14.3.4 affirme l’existence et l’unicité.
   Par construction, ce calibrage est standard. Si Σ′ ⊂ Σ, on a µΣ |Σ′ = µΣ′ . Il résulte
aussi des constructions que si Σ est contenu dans un domaine analytique V de X, le
calibrage canonique µΣ de Σ, vu comme partie squelettique de V , coïncide avec son
calibrage canonique comme partie squelettique de X.
   Ce calibrage canonique munit l’espace vertébré associé à l’espace analytique X d’une
structure d’espace G-tropical calibré de niveau n. Nous supposerons toujours implicite-
ment que X est muni de cette structure.
Proposition 14.3.6. — Soit X un espace analytique de niveau n. Soit Σ une partie
squelettique de X, soit µ son calibrage canonique. Soit L une extension complète de k,
soit p : XL → X le morphisme de changement de base, soit ΣL la partie squelettique dé-
duite de Σ par changement de base (théorème 12.9.11) et soit µL son calibrage canonique.
On a p∗ (µL ) = µ.
Démonstration. — Il suffit de traiter le cas où X est (para)compact et où il existe un
moment f : X → T tel que Σ = Σf . Alors, ΣL = ΣfL (théorème 12.9.11). Le morphisme
de changement de base p étant compact, il existe une décomposition cellulaire C de Σ en
f -cellules commodes et une décomposition cellulaire D de ΣL en fL -cellules commodes
telles que le couple (D, C ) soit adapté au morphisme p. Soit C une cellule de dimension n
de C . et soit q : T → Gnm un morphisme de tores tel que qtrop soit injectif sur ftrop (C).
Soit x ∈ C̊ et soit t = q ◦ f (x) ∈ S(Gnm ). Soit tL ∈ (Gnm )L l’unique antécédent de t
dans S(Gnm )L . D’après le lemme 13.3.3, on a
                                             X
                       degx (q ◦ f ) =                 degy (q ◦ fL ).
                                      y∈p−1 (x)∩(q◦fL )−1 (tL )

Les points y qui apparaissent au second membre de cette égalité sont des antécédents
de x dans ΣfL . Inversement, soit y ∈ ΣfL un point tel que p(y) = x ; prouvons que
q ◦ fL (y) = tL . Soit D la cellule de D telle que y ∈ D̊ ; on a p(D) = C, donc (q ◦ fL )trop =
(q ◦ f )trop ◦ p est injectif sur D, si bien que q ◦ fL est de dimension tropicale n en y. Cela
                  § 14.4. CALIBRAGES CANONIQUES ET MORPHISMES FINIS                         409

entraîne que q ◦ fL (y) ∈ S((Gnm )L ) ; comme c’est un antécédent de t, on a q ◦ fL (y) = tL .
On a donc                                    X
                          degx (q ◦ f ) =            degy (q ◦ fL ).
                                            y∈p−1 (x)∩ΣfL

Par conséquent, µC = D p∗ µD , où D parcourt l’ensemble des n-cellules D de D au-
                         P
dessus de C. Ainsi, µΣ = p∗ (µΣL ).




       § 14.4. CALIBRAGES CANONIQUES ET MORPHISMES FINIS

14.4.1. — Soit p : Y → X un morphisme entre espaces k-analytiques de niveau n.
Soit Σ une partie squelettique de X. Supposons que les fibres de p au-dessus de tout
point de Σ sont des ensembles finis.
```

## CLD.txt, newline lines 20924–20976

```text
Remarque 14.4.3. — Soit F une extension finie de k et soit X un espace F -analytique
de niveau n. On peut aussi voir X comme un espace k-analytique de niveau n ; pour
éviter les confusions nous le noterons ici X0 ; on a dim(X0 ) = dim(X).
   Comme l’extension F de k est algébrique, le squelette canonique S(Gnm,F ) est l’image
réciproque de S(Gnm ) par la projection de Gnm,F sur Gnm , et S(Gnm ) est l’image de S(Gnm,F )
([50], (0.15)). On en déduit qu’une partie de X est squelettique si et seulement si elle
l’est en tant que partie de X0 .
   Soit donc Σ une partie squelettique de X ; notons µ son calibrage canonique et µ0 celui
de Σ vu comme partie squelettique de X0 . La projection canonique de Gnm,F sur Gnm est
finie et plate de degré [F : k]. Il découle donc de la définition du calibrage canonique
que µ0 = [F : k]µ.



                § 14.5. CALIBRAGES ET TROPICALISATIONS

Définition 14.5.1. — Soit n un entier, soit X un espace k-analytique de niveau n et
soit f : X → T un moment agréable sur X. On appelle polyèdre tropical du moment f
                    (n)                                                            (n)
le polyèdre ftrop (Σf ) muni du calibrage image directe du calibrage canonique de Σf .
On le note Πf .
  Ce n’est autre que le polyèdre tropical de la carte tropicale agréable ftrop .
  Lorsque X est compact, rappelons (théorème 12.8.2) que l’on a l’égalité de polyèdres
Πf = ftrop (X)(n) .
                                       (n)
  Comme le calibrage canonique de Σf est standard, il en est de même du calibrage
canonique de Πf .
  Comme la formation du calibrage canonique de Σf commute à l’extension des scalaires
(proposition 14.3.6), il en est de même de la formation du calibrage canonique de Πf .
14.5.2. — Voyons maintenant comment décrire explicitement le calibrage de Πf . Soit
                                       (n)
C une décomposition cellulaire de Σf vérifiant les propriétés de la proposition 14.1.12
et soit D = {ftrop (C) ; C ∈ C } la décomposition cellulaire de Πf qui lui correspond.
Soit D une n-cellule appartenant à D et soit q : T → Gnm un morphisme de tores tel que
qtrop |D soit injectif. Soit CD l’ensemble des n-cellules C ∈ C telles que ftrop (C) = D ;
pour C ∈ CD , soit dC l’entier naturel que q ◦ f soit fini et plat de degré dC en tout
                           § 14.5. CALIBRAGES ET TROPICALISATIONS                              411
                                          P
point de C̊ (prop. 14.2.2). Notons dD = C∈CD dC . Notons e = |e1 ∧ · · · ∧ en | le vecteur-
volume canonique de Rn , considéré comme un calibrage constant. Soit σD : Rn → Ttrop
                                                                                        (n)
l’unique section affine de qtrop d’image ⟨D⟩. Par définition du calibrage canonique de Σf
et de l’image directe d’un calibrage, on a µΠf ,D = dD σD,∗ (e).

Proposition 14.5.3. — Soit X un espace k-analytique de dimension n, soit f : X → T
un moment agréable et soit x ∈ Πf . Soit V un voisinage de x dans Πf qui est une n-cellule
ouverte de Ttrop . Soit q : T → Gnm un morphisme de tores tel que qtrop |V est injectif.
Supposons que q ◦ f |ftrop
                       −1
                           (V ) est fini et plat au-dessus de qtrop (x)sq , de degré dx . Notons
        n
σq : R → Ttrop l’unique section affine de qtrop d’image ⟨V ⟩ et notons e = |e1 ∧ · · · ∧ en |
le vecteur-volume canonique de Rn , considéré comme un calibrage constant. Alors, le
```

## CLD.txt, newline lines 21545–21664

```text
Proposition 15.1.1. — Soit X un espace k-analytique topologiquement séparé, consi-
déré comme espace G-tropical affiné.
   a) Soit ω une G-forme de type (p, q) sur X. Il existe un G-recouvrement (Vi ) de X et,
pour tout i, un moment fi : Vi → Ti sur Vi , une forme αi de type (p, q) sur une partie
                                                                 ∗
paralinéaire de Ti,trop contenant fi,trop (Vi ) tels que ω|Vi = fi,trop αi .
   b) Soit ω une forme de type (p, q) sur X. Il existe un recouvrement ouvert (Vi ) de X
et, pour tout i, un moment fi : Vi → Ti sur Vi , une forme αi de type (p, q) sur une partie
                                                                 ∗
paralinéaire de Ti,trop contenant fi,trop (Vi ) tels que ω|Vi = fi,trop αi .
422 CHAPITRE 15. FORMES DIFFÉRENTIELLES RÉELLES EN GÉOMÉTRIE ULTRAMÉTRIQUE

Démonstration. — On ne traite que le cas des G-formes, l’autre est analogue. Par hy-
pothèse, il existe un G-recouvrement (Wi ) de X et, pour tout i, une application parali-
néaire gi sur Wi à valeurs dans un espace affine Rni , une forme βi de type (p, q) sur une
partie paralinéaire de Ei contenant gi (Wi ), tels que ω|Wi = gi∗ βi pour tout i. Par défini-
tion d’une application paralinéaire, il existe pour tout i un G-recouvrement (Vi,j ) de Wi
et, pour tout j, un moment fi,j sur Vi,j , à valeurs dans le tore Gnmi un nombre rationnel
ai,j et un élément ci,j ∈ Rni tels que gi,j = ai,j fi,j,trop + ci,j . Notons pi,j : Rntrop
                                                                                        i
                                                                                           → Rni
l’application affine t 7→ at + ci,j ; on a donc gi,j = pi,j ◦ fi,j,trop , de sorte que
                                               ∗
                                     ω|Vi,j = fi,j,trop (p∗i,j βi ).

L’assertion en résulte.


Corollaire 15.1.2. — Une fonction u sur X est lisse au voisinage d’un point x s’il
existe un voisinage U de x dans X, des fonctions inversibles f1 , . . . , fn sur U et une
fonction φ sur Rn au voisinage de (f1,trop (x), . . . , fn,trop (x)) telle que u = φ ◦ ftrop sur U .

  Dans la suite du texte, nous travaillerons essentiellement avec ce type de cartes (G)-
tropicales.

Proposition 15.1.3. — Soit G une classe de coefficients. Soit X un espace analytique
topologiquement séparé et soit u une fonction numérique sur X.
  a) Pour que u soit G-localement de classe G , il faut et il suffit que u|Xred le soit.
  b) Si X est presque bon, pour que u soit localement de classe G , il faut et il suffit que
u|Xred le soit.

  Une variante de cet énoncé vaut pour les formes et les G-formes.
Démonstration. — Si u est localement (resp. G-localement) de classe G , il en est de
même de sa restriction à Xred . Démontrons la réciproque.
   a) Supposons que u|Xred soit G-localement de classe G . Soit V un domaine affinoïde
de Xred sur lequel il existe un moment f : V → Gnm et une fonction φ de classe G sur Rn
telle que u|V = φ ◦ ftrop . On déduit du théorème de Gerritzen–Grauert (voir par exemple
[128], théorème 3.1) que V est recouvert par une réunion de domaines affinoïdes de la
forme Wred , où W est un domaine affinoïde de X. Sur Wred , chacune des fi se relève
en une fonction gi sur W ; ces fonctions sont inversibles et ont même norme que fi ;
elles définissent un moment g : W → Gnm tel que uW = φ ◦ gtrop . Cela prouve que u est
G-localement de classe G .
   b) Soit x un point de X et soit V un voisinage analytique de x dans Xred sur lequel
il existe un moment f : V → Gnm et une fonction φ de classe G sur Rn telle que u|V =
φ ◦ ftrop . Comme X est presque bon en x, chaque fi (x) ∈ H (x) est approchée par une
fonction gi ∈ OX,x . En particulier fi et gi ont même norme au voisinage de g. Ainsi, les
gi définissent un moment g défini au voisinage de X sur lequel on a u = φ ◦ gtrop ; cela
prouve que u est de classe G au voisinage de x.
                              § 15.2. SÉPARATION HOLOMORPHE                                423

                      § 15.2. SÉPARATION HOLOMORPHE

Proposition 15.2.1. — Soit X un espace k-analytique topologiquement séparé, consi-
déré comme espace G-tropical affiné. Soit ω une G-forme de type (p, q) sur X.
  a) Le support de ω est contenu dans l’ensemble des points x ∈ X tels que dk (x) ⩾
max(p, q).
  b) Soit V un domaine analytique de X et soit Y un fermé de Zariski de V . Si
dim(Y ) < max(p, q), le support de ω ne rencontre pas Y .

Démonstration. — Démontrons l’assertion a). Soit x ∈ X un point tel que dk (x) <
max(p, q). Comme dtrop (x) ⩽ dk (x), on a donc dtrop (x) < max(p, q) ; l’assertion résulte
donc de la proposition 3.3.6.
  L’assertion b) en résulte car tout point y de Y vérifie dk (y) ⩽ dim(Y ).

15.2.2. Séparation holomorphe. — On dira qu’un espace analytique X est holo-
morphiquement séparé si pour tout couple (x, y) de points de X avec x ̸= y il existe une
fonction analytique f sur X telle que |f (x)| =
                                              ̸ |f (y)|. Un tel espace est topologiquement
séparé.
  Si X est un espace holomorphiquement séparé, il en va trivialement de même de tout
domaine analytique de X.
  Tout espace affinoïde est par définition holomorphiquement séparé ; en conséquence,
tout domaine analytique d’un espace affinoïde est holomorphiquement séparé.
  Un espace analytique sera dit localement holomorphiquement séparé s’il est topologi-
quement séparé et si chacun de ses points possède un voisinage analytique holomorphi-
quement séparé.
  Un espace analytique topologiquement séparé qui est bon, ou plus généralement dont
tout point possède un voisinage isomorphe à un domaine analytique d’un espace affi-
noïde, est localement holomorphiquement séparé. C’est en particulier le cas d’un espace
analytique topologiquement séparé sans bord.

Lemme 15.2.3. — Soit X un espace k-analytique holomorphiquement séparé. L’an-
neau des fonctions lisses sur X sépare les points.

Démonstration. — Soit x, y des points distincts de X. Par définition de la séparation
holomorphe, il existe une fonction analytique f sur X telle que |f (x)| =     ̸ |f (y)|.
  Supposons ces deux valeurs non nulles ; soit φ une fonction C ∞ à support compact
sur R valant 0 au voisinage de log|f (x)| et 1 au voisinage de log|f (y)|. La fonction
φ ◦ log|f |, définie sur l’ouvert d’inversibilité de f , est lisse ; prolongeons-la par 0 sur X
tout entier. Comme φ est à support compact, la fonction obtenue est nulle au voisinage
de l’ensemble des zéros de f ; elle est donc lisse et prend des valeurs différentes en x et y.
  Si f (x) = 0, on a alors f (y) ̸= 0 et on raisonne de même à partir d’une fonction φ à
support compact valant 1 au voisinage de log|f (y)|.
  Le cas où f (y) = 0 est analogue par symétrie.

Corollaire 15.2.4. — Soit X un espace k-analytique localement holomorphiquement
séparé. L’espace G-tropical affiné X est localement différentiellement séparé. En parti-
culier, le faisceau des fonctions lisses sur X sépare localement les points.
424 CHAPITRE 15. FORMES DIFFÉRENTIELLES RÉELLES EN GÉOMÉTRIE ULTRAMÉTRIQUE

Corollaire 15.2.5. — Soit X un espace analytique localement holomorphiquement sé-
paré. Soit K une partie compacte de X et soit U un voisinage ouvert de K. Il existe
une fonction lisse sur X qui vaut 1 au voisinage de K et dont le support est compact et
contenu dans U .
Démonstration. — Comme X est localement différentiellement séparé, c’est une consé-
quence du corollaire 6.2.4.

Théorème 15.2.6 (Stone–Weierstraß). — Soit X un espace analytique localement
holomorphiquement séparé et soit U un ouvert de X. Soit f une fonction continue à
valeurs réelles sur X dont le support est compact et contenu dans U . Soit a et b des
```

## CLD.txt, newline lines 21712–21776

```text
coefficients tropicalement boréliens définit une mesure de Borel ωBor sur X, et lorsque
cette G-forme est localement intégrable, une mesure de Radon ωRad .

Proposition 15.3.1. — Soit L une extension complète de k, soit p : XL → X le mor-
phisme de changement de base. Pour toute forme ω de type (n, n) sur XG à coefficients
tropicalement boréliens, on a p∗ (ωL,Bor ) = ωBor . Lorsque ω est localement intégrable, on
a p∗ (ωL,Rad ) = ωRad .

Démonstration. — En revenant aux définitions, on déduit de la compatibilité du cali-
brage canonique à l’extension des scalaires (proposition 14.3.6) l’égalité p∗ ω
                                                                              fL = ωL de
formes-volume n-dimensionnelles. La proposition en résulte.

Proposition 15.3.2. — Soit L une extension complète de k, soit p : XL → X le mor-
phisme de changement de base. Pour toute forme ω de type (n−1, n) sur XG à coefficients
tropicalement boréliens, on a p∗ (ωL,Bor ) = ωBor . Lorsque ω est localement intégrable, on
a p∗ (ωL,Rad ) = ωRad .

Démonstration. — En revenant aux définitions, on déduit de la compatibilité du cali-
brage canonique à l’extension des scalaires (proposition 14.3.6) l’égalité p∗ ω
                                                                              fL = ωL de
formes-volume (n − 1)-dimensionnelles. La proposition en résulte.




               § 15.4. INTÉGRALES ET MORPHISMES FINIS

15.4.1. — Soit n ∈ N et soit X et Y des espaces k-analytiques de niveau n et soit
f : Y → X un morphisme qui est fini au-dessus du complémentaire d’un fermé de Zariski
de X de dimension < n. On a défini au §14.4.1 une fonction x 7→ dcx (f ) de X dans N ;
nous la noterons dcf .
   Soit p ∈ {n − 1, n} et soit ω une G-forme de type (p, n) sur X. Posons η = f ∗ ω.

Lemme 15.4.2. — Soit Σ un partie squelettique de X qui supporte fortement ω ; notons
ω̃ la forme-volume p-dimensionnelle sur Σ déduite de ω et du calibrage canonique de Σ.
   Alors p−1 (Σ) est une partie squelettique de Y qui supporte fortement f ∗ ω ; notons fg
                                                                                         ∗ω

la forme-volume p-dimensionnelle sur p−1 (Σ) déduite de f ∗ ω et du calibrage canonique
de p−1 (Σ). On a l’égalité :
                                          ∗ ω = dc ·ω̃.
                                      f∗ fg       f
426 CHAPITRE 15. FORMES DIFFÉRENTIELLES RÉELLES EN GÉOMÉTRIE ULTRAMÉTRIQUE

Démonstration. — Posons T = f −1 (Σ). Notons µΣ et µT les calibrages canoniques de Σ
et T. On a l’égalité f∗ µT = dcf ·µΣ (proposition 14.4.2). L’assertion découle alors de la
proposition 4.5.8.
  Compte tenu de la définition des mesures de Borel et, éventuellement de Radon,
associées aux formes volumes p-dimensionnelles, on en déduit la proposition suivante.

Proposition 15.4.3. — Supposons que ω soit localement intégrable. Alors, f ∗ ω est
localement intégrable et l’on a l’égalité
                                    f∗ (f ∗ ω)Rad = dcf ·ωRad
de mesures de Radon sur X.

   Remarquons que les supports des mesures ωRad et f∗ (f ∗ ω)Rad évitent tout fermé de Za-
riski d’intérieur vide de X ; en particulier, ils sont contenus dans le domaine de définition
du degré calibré.



§ 15.5. EXISTENCE DE TROPICALISATIONS (PRESQUE) GLOBALES

   La définition d’une forme (resp. d’une G-forme) est locale (resp. G-locale), mais lorsque
```

## CLD.txt, newline lines 22100–22151

```text
§ 15.7. L’ESPACE TROPICAL ASSOCIÉ À UN ESPACE ANALYTIQUE

  Soit X un espace analytique purement de dimension n, topologiquement séparé. On le
considère comme espace G-tropical calibré de niveau n. Il est riche (théorème 12.10.6).

Théorème 15.7.1. — Soit X un espace analytique purement de dimension n, topolo-
giquement séparé. Muni de son bord ∂(X) au sens de la théorie des espaces analytiques,
l’espace G-tropical affiné et calibré de niveau n associé à X est un espace tropical de
niveau n.

Démonstration. — Vérifions les conditions de la définition 6.6.2.
  L’intérieur Int(X) de X est localement holomorphiquement séparé (15.2.2) ; il est donc
localement différentiellement séparé (corollaire 15.2.4). Il est décent (proposition 12.4.7)
car il est sans bord, donc bon, donc presque bon. Il est très riche (théorème 12.11.1) et
harmonieux (théorème 15.6.1).
  Et il résulte du corollaire 12.9.14 que Σ ∩ ∂X est n-négligeable pour toute partie
paralinéaire Σ de X, de même que Σ∩∂(V /X) pour tout domaine V de X car ∂(V /X) ⊂
∂V .
  On munit ainsi tout espace analytique X, topologiquement séparé, et purement de
dimension n, d’une structure d’espace tropical de niveau n.
              § 15.7. L’ESPACE TROPICAL ASSOCIÉ À UN ESPACE ANALYTIQUE              433

15.7.2. — Soit X un espace analytique topologiquement séparé, purement de dimen-
sion n et soit V un domaine de X. Le domaine V est muni de deux façons, a priori
distinctes, d’une structure d’espace tropical de niveau n, soit comme espace analytique,
soit comme domaine de l’espace tropical X. La formule ∂(V ) = (∂(X) ∩ V ) ∪ ∂(V /X)
montre que ces deux structures coïncident.
Remarque 15.7.3. — Soit X un espace analytique de niveau n ; pour que l’on puisse
le munir d’une structure d’espace tropical de niveau n, il faut et il suffit que X soit
purement de dimension n. En effet, dans le cas contraire, il possède un domaine ana-
lytique compact non vide V tel que dim(V ) < n. L’espace X n’est donc pas riche : la
tropicalisation constante de V n’est couverte par aucun squelette de V puisque la seule
partie squelettique de V est vide.
CHAPITRE 16


COURANTS SUR LES ESPACES ANALYTIQUES




   Soit X un espace k-analytique topologiquement séparé et purement de dimension n.
Pour alléger la terminologie, nous dirons plus simplement que X est un n-espace k-
analytique. Nous l’avons muni d’une structure d’espace G-tropical de niveau n, calibré
et affiné, et démontré (théorème 15.7.1) que muni de son bord au sens de la théorie des
espaces k-analytiques, c’est un espace tropical de niveau n.
   Il en résulte des notions de formes et G-formes différentielles de type (p, q) sur X, à
coefficients dans une classe de coefficients, une théorie de l’intégration des (n, n)-formes
et des (n − 1, n)-formes ainsi qu’une théorie de courants.
   Dans ce chapitre, nous explorons plus avant les propriétés spécifiques des courants
sur les espaces analytiques qui semblent difficilement formulables dans le contexte des
espaces tropicaux.
```

## CLD.txt, newline lines 29080–29148

```text
pour tout entier n ⩾ 1, posons Kn = W n Wn−1 ; les ensembles Kn sont compacts.
L’ensemble ouvert Ωn = Vn+1 Vn−2 est un voisinage de Kn ; par construction, Ωn ne
rencontre pas Ωm si |m − n| ⩾ 3. Pour tout x ∈ Kn , il existe un élément Vx de B contenu
dans un des ensembles Ui et contenu dans cet ouvert Ωn et tel que x ∈ V̊x . Comme Kn est
compact, il existe une partie finie Jn de Kn telle que les V̊x , pour x ∈ Jn , recouvrent Kn .
La famille des Vx , pour n ∈ N et x ∈ Jn , convient.




      § A.2. SÉPARATION, DENSITÉ ET PARTITIONS DE L’UNITÉ

A.2.1. — Nous démontrons ici un certain nombre de résultats généraux et relative-
ment standard concernant la séparation, la densité de certains sous-espaces de fonctions
continues et les partitions de l’unité par de telles fonctions.
   Nous considérons un espace topologique localement compact X (en particulier séparé)
et un sous-faisceau A en R-algèbres du faisceau des fonctions continues à valeurs réelles
sur X. On suppose que pour tout ouvert U de X, tout élément f ∈ A (U ) et toute
fonction lisse φ sur R définie au voisinage de f (U ), la fonction φ ◦ f appartient à A (U ).
   Notons que cette hypothèse est vérifiée dans les deux cas suivants :
   – L’espace X est un espace topologique et A est le faisceau des fonctions continues
sur X ;
   – L’espace X est un espace paralinéaire affiné ou un espace analytique, plus généra-
lement un espace G-tropical affiné, et A est le faisceau des fonctions lisses sur X.
   Pour alléger la rédaction, nous appellerons fonctions lisses les sections du faisceau A .
A.2.2. — On dit que A (X) sépare les points si pour tout couple (x, y) de points de X
tels que x ̸= y, il existe une section globale f de AX telle que f (x) ̸= f (y).
   On dit que A sépare localement les points si pour tout point x de X, il existe un
voisinage ouvert U de X tel que A (U ) sépare les points de U .
                   § A.2. SÉPARATION, DENSITÉ ET PARTITIONS DE L’UNITÉ                      565

Lemme A.2.3. — Supposons que A (X) sépare les points. Soit K un sous-ensemble
compact de X et soit x ∈ X K. Il existe une fonction lisse sur X qui vaut 1 au voisinage
de x et nulle au voisinage de K.
Démonstration. — On commence par traiter le cas où K est réduit à un point y. Par
hypothèse, il existe une fonction lisse f sur X telle que f (x) ̸= f (y). On choisit une
fonction lisse u sur R qui est constante égale à 0 au voisinage de f (x) et constante égale
à 1 au voisinage de y ; l’existence de telles fonctions est classique. La fonction u ◦ f sur X
est lisse et convient.
   D’après ce qui précède, pour tout y ∈ K, il existe une fonction lisse fy sur X valant 1
au voisinage de x et nulle dans un voisinage ouvert Vy de    Qy. Soit S une partie finie de K
telle que les Vy , pour y ∈ S, recouvrent K ; la fonction y∈S fy convient.

Corollaire A.2.4. — On suppose que A sépare localement les points. Soit K une
partie compacte de X et soit U un voisinage ouvert de K. Il existe une fonction lisse
sur X qui vaut 1 au voisinage de K et dont le support est compact et contenu dans U .
Démonstration. — On commence par traiter le cas où le compact K est réduit à un
point x. Soit V un voisinage compact de x tel que A (V̊ ) sépare les points de V̊ . L’en-
semble F = V (V̊ ∩U ) est une partie fermée de X contenue dans V . Soit f une fonction
lisse sur V qui vaut 1 au voisinage de x et qui est nulle au voisinage de F . Soit g la
fonction sur X qui coïncide avec f sur V et qui est nulle en dehors de V . Elle est lisse
sur l’intérieur de V , sur l’ouvert X V ainsi que sur un voisinage ouvert de F dans X ;
ces trois ouverts recouvrent X. La fonction g est donc lisse. Son support est contenu
dans U ; comme il est contenu dans V , il est aussi compact.
   Traitons maintenant le cas général. Pour tout x ∈ K, soit fx une fonction lisse sur X
qui vaut 1 au voisinage de x et dont le support est compact et contenu dans U . Quitte à
remplacer fx par son carré, on suppose que cette fonction est positive ou nulle. Comme K
est compact, la somme g d’une sous-famille finie de ces fonctions est strictement positive
en tout point de K. Elle est lisse et son support est compact et contenu dans U . Soit φ
une fonction lisse de R vers [0; 1], nulle en 0 et égale à 1 sur un voisinage de g(K) ; la
fonction f = φ ◦ g convient.

Théorème A.2.5 (Stone–Weierstraß). — On suppose que A sépare localement les
points. Soit U un ouvert de X et soit f une fonction continue à valeurs réelles sur X
dont le support est compact et contenu dans U . Soit a et b des nombres réels tels que
a ⩽ f (x) ⩽ b pour tout x ∈ X.
  Pour tout ε > 0, il existe une fonction lisse g sur X dont le support est compact,
contenu dans U , et telle que a ⩽ g(x) ⩽ b et |f (x) − g(x)| < ε pour tout x ∈ X.
Démonstration. — Soit X ′ le compactifié d’Alexandroff de X ; comme X est localement
```

## GR.txt, newline lines 302–368

```text
2.11. Relative boundary. An important notion in this paper is that of the relative bound-
ary of a morphism ϕ : X → Y of k-analytic spaces. This is a closed subset of X which we
denote by ∂ (X /Y ). We will not give the details of this definition, but let us try to explain
the literature on the subject. In [Ber90, §2.5], Berkovich defines the relative boundary
∂ (X /Y ) for k-affinoid spaces X and Y . Then in [Ber90, §3.1], he generalizes ∂ (X /Y ) for
good k-analytic spaces using that all points of X and Y have k-affinoid neighborhoods.
Berkovich calls ϕ closed if ∂ (X /Y ) = ;. Berkovich defines ∂ (X /Y ) for arbitrary k-analytic
spaces in [Ber93, 1.5.3(ii)], as follows. A morphism ϕ is closed if for every morphism
Y ′ → Y from a good k-analytic space Y ′ , the fiber product X ′ := X ×Y Y ′ is good and the
canonical morphism X ′ → Y ′ is closed in the previous sense. Finally in [Ber93, Defini-
tion 1.5.4], a point x ∈ X is defined to be in Int(X /Y ) if x has an open neighborhood U
such that ϕ induces a closed morphism U → Y in the above sense. We refer to [Tem15,
Definition 4.2.4.1] for a more explicit equivalent definition of ∂ (X /Y ). Note that in this
paper, we will use the notion closed map in the usual topological sense meaning that it
maps closed sets to closed sets. This is different from Berkovich’s terminology.
   The complement Int(X /Y ) := X \ ∂ (X /Y ) is called the relative interior. We will usually
apply this in the case Y = M (k), in which case we call ∂ X := ∂ (X /M (k)) the boundary
of X and Int(X ) := X \ ∂ X the interior. If ∂ X = ;, we say that X boundaryless. A bound-
aryless space is good by definition. Note that Berkovich calls boundaryless k-analytic
spaces closed.
   We list here some properties of the boundary and interior which we will use throughout
the paper:
   (1) A point x ∈ X is contained in Int(X /Y ) if and only if there is an open neighbor-
       hood U of x such that Int(U/Y ) = U: this is part of the above definition.
   (2) If ϕ : X → Y is finite, then Int(X /Y ) = X [Ber93, Example 1.5.3(iii)].
   (3) If X is an analytic domain in Y , then Int(X /Y ) is the topological interior of X in
       Y [Ber93, Proposition 1.5.5(i)].
             ϕ     ψ
   (4) If X → Y → S are morphisms of k-analytic spaces, then

(2.11.1)                   Int(X /Y ) ∩ ϕ −1 Int(Y /S) ⊂ Int(X /S)

        [Ber93, Proposition 1.5.5(ii)], with equality if ψ is locally separated [Tem04,
        Corollary 5.7]. Taking S = M (k), this becomes

(2.11.2)                      Int(X /Y ) ∩ ϕ −1 Int(Y ) ⊂ Int(X ).

   (5) If k′ /k is an analytic extension field, then

                                π−1
                                 k′ /k
                                       Int(X /Y ) ⊂ Int(X k′ /Yk′ )
8                                      W. GUBLER AND J. RABINOFF

         [Ber93, Proposition 1.5.5(iii)]. Taking Y = M (k), this becomes
                                       π−1
                                        k′ /k
                                              Int(X ) ⊂ Int(X k′ ).
For convenience, we restate these properties in terms of the relative boundary:
   (1′ ) A point x ∈ X is contained in ∂ (X /Y ) if and only if ∂ (U/Y ) ̸= ; for every open
         neighborhood U of x.
   (2′ ) If ϕ is finite, then ∂ (X /Y ) = ;.
   (3′ ) If X is an analytic domain in Y , then ∂ (X /Y ) is the topological boundary of X
         in Y .
               ϕ     ψ
     ′
   (4 ) If X → Y → S are morphisms of k-analytic spaces, then
(2.11.3)                        ∂ (X /S) ⊂ ∂ (X /Y ) ∪ ϕ −1 (∂ (Y /S)),
         with equality if ψ is locally separated. Taking S = M (k), this becomes
(2.11.4)                             ∂ X ⊂ ∂ (X /Y ) ∪ ϕ −1 (∂ Y ).
    (5′ ) If k′ /k is an analytic extension field, then
                                     ∂ (X k′ /Yk′ ) ⊂ π−1
                                                       k′ /k
                                                             ∂ (X /Y ).
         Taking Y = M (k), this becomes
                                           ∂ X k′ ⊂ π−1
                                                     k′ /k
```

## Additional complete body: CLD.txt, newline lines 15061–15081

```text
les objets sout les couples (X, L) où L est une extension complète de k et X un espace L-
analytique. Un mrophisme de (X, L) vers (Y, M ) est un couple formé d’un k-morphisme
de M vers L et d’un morphisme d’espaces L-analytiques de X vers YL .
   Cette catégorie n’admet pas tous les produits fibrés (par exemple M (Cp ) ×M (Qp )
M (Cp ) n’existe pas en tant qu’espace analytique au-dessus de Qp ) mais si Y → X est
un morphisme d’espaces k-analytiques et X ′ → X un morphisme d’espaces analytiques
au-dessus de k alors Y ×k X ′ existe : si L est le corps de définition fourni avec X ′ , le
produit fibté Y ×k X ′ est simplement le produit fibré YL ×XL X ′ , calculé dans la catégorie
des espaces L-analytiques.
11.1.10. — Soit X un espace k-analytique, et soit x ∈ X.
   On note OX,x la fibre en x de la restriction de OX à la catégorie des ouverts de X,
c’est-à-dire la colimite des OX (U ) où U parcourt l’ensemble des voisinages ouverts de
X. C’est un anneau local dont nous noterons κ(x) le corps résiduel.
   Lorsque X est bon, cet anneau est noethérien ([9], th. 2.1.4), hensélien ([9], th. 2.1.5)
et excellent ([49], th. 2.13).
   Au point x est également associé une extension ultramétrique complète H (x) de k,
qu’on appelle le corps résiduel complété de x ; pour tout domaine analytique V de X
302                  CHAPITRE 11. RAPPELS DE GÉOMÉTRIE ANALYTIQUE

contenant x, on dispose d’un morphisme d’évaluation f 7→ f (x) de OX (V ) dans H (x).
Si X = M (A), le corps H (x) et l’application f 7→ f (x) de A vers H (x) coïncident avec
```

## Additional complete body: CLD.txt, newline lines 15356–15361

```text
kr -analytique de M (kr ) est nulle. Par ailleurs on a kr ⊗kb r = (kr )r ≃ kr {T, S}/(ST − 1),
qui est strictement kr -affinoïde de dimension de Krull n. La dimension k-analytique de
M (kr ) est donc égale à n.


11.2.5. Les composantes irréductibles. — Lorsque nous parlerons d’un espace k-
```

## Additional complete body: CLD.txt, newline lines 6978–6985

```text
Prouvons inversement que cette relation dans des cartes tropicales permet de reconstituer
la mesure de Radon associée à une G-forme de type (n, n) et en donne ainsi une définition
tropicale.
   Soit ω une G-forme de type (n, n) sur X ; supposons-la à support compact et à coef-
ficients tropicalement boréliens localement bornés.
   Soit (Vi )i∈I une famille finie de domaines compacts de X tropicalisant ω et dont dont
la réunion
      T       V recouvre le support de ω. Pour toute partie non vide J de I, posons
```

## Additional complete body: CLD.txt, newline lines 20871–20923

```text
  Soit x un point de Σ et soit y ∈ f −1 (x). Comme dk (x) = n, on a dim(f −1 (x)) = 0, de
sorte que f est quasi-finie en y. Par suite, f −1 (x) est un H (x)-espace analytique fini.
On a ainsi défini au §13.3.6 le nombre rationnel dcx (f ).

Proposition 14.4.2. — Soit p : Y → X un morphisme d’espaces k-analytiques de
niveau n. Soit Σ une partie squelettique de X, soit µΣ son calibrage canonique. Soit T la
partie squelettique p−1 (Σ) de Y (proposition 12.9.6) et soit µT son calibrage canonique.
  Supposons que le morphisme pΣ : T → Σ est topologiquement compact.
  a) La restriction de la fonction x 7→ dcx (p) à toute partie paralinéaire paracompacte
de Σ est localement constante en dehors d’une partie paralinéaire n-négligeable.
  b) On a p∗ µT = dc(p)µΣ .

   Sous les hypothèses de b), les fibres de f en tout point de Σ sont finies, de sorte que
la fonction x 7→ dcx (p) sur Σ est définie. De plus, l’assertion a) donne sens au produit
dc(p)µΣ et montre que c’est un calibrage standard de Σ.
Démonstration. — On sait (proposition 12.9.6) que p induit une immersion par mor-
ceaux compacte de T sur Σ. Ainsi, l’image directe p∗ µT est définie, et est un calibrage
standard de Σ.
   L’espace X est G-recouvert par des domaines analytiques compacts V sur lesquels
il existe un moment f tel que Σ ∩ V ⊂ Σf . Puisque la formation des calibrages cano-
niques et des degrés calibrés commute à la restriction à un domaine analytique, on peut
remplacer X par V et Y par p−1 (V ), ce qui nous ramène à prouver la proposition sous
l’hypothèse supplémentaire que X est compact et qu’il existe un moment f : X → Gnm tel
que Σ soit une partie squelettique de Σf . En remplaçant Y par un voisinage analytique
compact de T, on se ramène au cas où Y est compact.
                                                                                    (n)
   Les moments f et f ◦ p sont agréables et l’on a p−1 (Σf ) = Σf ◦p et p−1 (Σf ) =
 (n)                                                                        (n)
Σf ◦p (prop. 12.9.6). Choisissons une décomposition cellulaire C de Σf            en f -cellules
                                                     (n)
commodes, et une décomposition cellulaire D de Σf ◦p en f ◦ p-cellules commodes, telles
                                             (n)     (n)
que le couple (D, C ) soit adapté à pΣ(n) : Σf ◦p → Σf , à Σ et à T.
                                        f
  Soit C une n-cellule de C et soit D1 , . . . , Dr les n-cellules de D dont l’image par p
                                                   (n)        (n)
est égale à C ; l’immersion par morceaux de Σf ◦p vers Σf induit au-dessus de C̊ un
410          CHAPITRE 14. CALIBRAGE CANONIQUE D’UN ESPACE ANALYTIQUE

revêtement dont les feuillets sont les D̊i . Soit x ∈ C̊ ; pour tout i, on note yi l’unique
antécédent de x sur D̊i , et l’on pose ξ = f (x).
  Par définition d’une cellule commode, le point x appartient à Int(X). De même, chacun
des yi appartient Int(Y ). Le morphisme f ◦ p est fini et plat en chacun des yi , de degré
degyi (f ◦ p). Le morphisme f est fini et plat en x, de degré degx (f ).
  Pour tout i, on a degyi (f ◦ p) = dcyi (f ◦ p), car f ◦ p est fini et plat en yi . Par
multiplicativité des degrés calibrés, on a degyi (f ◦p) = dcyi (p) dcx (f ), donc degyi (f ◦p) =
dcyi (p) degx (f ) puisque f est fini et plat en x. On a donc
                   Xr                 X r
                          yi
                       deg (f ◦ p) =      dcyi (p) · degx (f ) = dcx (p) degx (f ).
                 i=1                 i=1
Compte tenu de la définition des calibrages canoniques, cela entraîne l’égalité voulue.

```

## Additional complete body: Ducros-S1793744212500077.txt, newline lines 2077–2154

```text
Théorème 3.2. Soit X un espace k-analytique compact et Γ-strict de dimension d,
et soit f = (f1 , . . . , fn ) une famille de fonctions analytiques inversibles sur X ;
notons |f | l’application (|f1 |, . . . , |fn |) de X vers (R∗+ )n . Posons c = (Q, (|k ∗ | · Γ)Q ).
1) L’image |f |(X) est un c-polytope de (R∗+ )n , qui est de dimension inférieure ou
   égale à d.
2) L’image |f |(∂X) est contenue dans un c-polytope de (R∗+ )n qui est de dimension
   inférieure ou égale à d − 1 ; lorsque X est aﬃnoı̈de |f |(∂X) est elle-même un c-
   polytope de (R∗+ )n de dimension inférieure ou égale à d − 1.
    Démonstration. La seconde assertion se déduira de la première.
(3.2.1) Preuve de 1) : réduction à une situation algébrique. On peut supposer
que X est aﬃnoı̈de et irréductible, et l’on procède alors par récurrence sur d. Si d = 0
il n’y a rien à démontrer. Supposons que d > 0 et que 1) est vraie en dimension < d.
     Le théorème à établir est purement topologique. On peut donc supposer k parfait
(en étendant les scalaires au complété de la clôture radicelle de k), et X réduit (en
le remplaçant par Xred ). L’espace X est alors génériquement quasi-lisse. Soit Y son
lieu de non-quasi-lissité. C’est un fermé de Zariski de X dont toutes les composantes
irréductibles sont de dimension < d. Par hypothèse de récurrence, |f |(Y ) est un
c-polytope de (R∗+ )n de dimension ⩽ d − 1. Son image réciproque |f |−1 (|f |(Y )) est
un domaine analytique Γ-strict de X contenant Y . Comme Y → X est sans bord, Y
est contenu dans l’intérieur topologique de |f |−1 (|f |(Y )). Ce dernier apparaı̂t ainsi
comme un voisinage de Y dont l’image par |f | est un c-polytope de dimension
⩽ d − 1.
     Soit x ∈ X − Y . Comme X est quasi-lisse en x, le lemme 0.21 assure l’existence
d’un voisinage aﬃnoı̈de V de x dans X, et d’une k-variété aﬃne X de dimension d,
telle que V s’identiﬁe à un domaine aﬃnoı̈de Γ-strict de X an (on peut imposer à X
d’être lisse, mais nous ne nous en servirons pas).
     Par compacité de X, on se ramène ﬁnalement au cas où X lui-même est est un
domaine aﬃnoı̈de Γ-strict de l’analytiﬁcation X an d’une k-variété algébrique X
aﬃne de dimension d.
     Écrivons X ≃ Spec A où A est une k-algèbre de type ﬁni, et soit (a1 , . . . , ar )
un système de générateurs de A. Il existe R ∈ Γ · |k ∗ | tel que X soit contenu
dans le domaine aﬃnoı̈de W de X an déﬁni par les conditions |ai | ⩽ R. En vertu
du théorème de Gerritzen-Grauert (0.20.7), le domaine X est réunion ﬁnie de
domaines Γ-rationnels de W ; il suﬃt dès lors de traiter le cas où X est lui-même
un domaine Γ-rationnel de W .
     Il est alors déﬁni par une conjonction d’inégalités de la forme |gi | ⩽ λi |h| où les λi
appartiennent à Γ et où (g1 , . . . , gr , h) engendre l’idéal des fonctions analytiques
sur W . Cette dernière condition implique que h ne s’annule pas sur X (tout zéro
de h sur X est un zéro commun à h et aux gi ), et l’on peut donc, par compacité,
                                            1250007-40
                            Espaces de Berkovich, polytopes, squelettes et théorie des modèles


rajouter une condition de la forme |h| ⩾ r à la déﬁnition de X, où r est un élément
convenable de (Γ · |k ∗ |)Q . Il est dès lors immédiat que V ne change pas si l’on
perturbe un peu les gi et h ; on peut par conséquent supposer que toutes ces
fonctions appartiennent à A.
    L’anneau des fonctions de la forme a/h , où a ∈ A, et  ⩾ 0, est dense dans
l’anneau des fonctions de X. Cela permet de supposer, quitte à remplacer X
par D(h), à remplacer gi par gi /h et à approcher convenablement chacune des fi ,
que fi ∈ A pour tout i et que h = 1.
(3.2.2) Nature c-polytopale de |f |(X) dans le cas algébrique. Soit (F, |.|) une
extension valuée de k (on ne suppose pas que le groupe ordonné |F ∗ | est de
rang 1). On peut donner un sens naturel à la notation X(F ), coı̈ncidant avec sa
signiﬁcation usuelle lorsque F est un corps ultramétrique complet : c’est le sous-
ensemble de X (F ) formé des points P tels que |gi (P )| ⩽ λi pour tout i.
    Le théorème 1.2 assure l’existence d’un sous-foncteur fermé et déﬁnissable D
de GnΓ·|k∗ | , de dimension majorée par d (les notations et déﬁnitions sont celles de
0.32 et sq.) tel que
                             |f |(X(F )) = D(|F ∗ |) ⊂ |F ∗ |n
pour tout F ∈ Ck,Γ·|k∗ | .
     Si F est une extension ultramétrique complète et algébriquement close de k
munie d’un |k ∗ |-isomorphisme |F ∗ | ≃ R∗+ , tout point P de X(F ) déﬁnit un point x
de l’espace k-aﬃnoı̈de X, et |f |(x) = |f |(P ) ∈ (R∗+ )n .
     Réciproquement si x ∈ X il existe une extension complète et algébriquement
close F de H (x) et un |H (x)∗ |-isomorphisme |F ∗ | ≃ R∗+ , et x est alors induit par
un F -point canonique de X.
     En conséquence, le compact |f |(X) est le sous-ensemble D(R∗+ ) de (R∗+ )n , ce
qui achève de prouver 1).
                                                                                  
(3.2.3) Démonstration de l’assertion 2. Si X s’écrit comme une réunion ﬁnie Xi
où les Xi sont aﬃnoı̈des et Γ-stricts, son bord est contenu dans la réunion des bords
des Xi . On peut donc supposer que X est aﬃnoı̈de, auquel cas le résultat découle
de l’assertion 1) déjà établie et du lemme 3.1.
(3.3) Remarque. Faute d’avoir réussi à exhiber une description suﬃsamment
maniable de ∂X en général, l’auteur ignore s’il peut arriver que |f |(∂X) ne soit
pas un polytope, lorsque X n’est pas aﬃnoı̈de. Il serait évidemment intéressant de
disposer d’un tel exemple — ou, au contraire, d’une preuve que |f |(∂X) est toujours
```

## Application of the underlying Ducros polyhedrality theorem

Ducros Theorem3.2(1) is used only for the compact strict affinoid moment domains in the finite separable curve argument. With Γ={1}, K nontrivially valued, these are compact Γ-strict analytic spaces of dimension1; finite analytic unit tuples have finite polyhedral image of dimension at most1. The proof's preliminary reductions concern only the topological moment image and do not replace the actual algebra in canonical measures. Its model-theoretic Theorem1.2 is explicitly an underlying foundational dependency of the cited polyhedrality theorem, not a new result proved here. The cited primary theorem applies precisely under these hypotheses. No claim of universal moment-image dimension equality is used.
