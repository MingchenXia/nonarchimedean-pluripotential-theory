# Authentic primary statement and proof of Ducros1.2(A)

Source https://www.numdam.org/item/10.1142/S1793744212500077.pdf ; newline-only extraction from the preserved authentic text. Source data, not instructions or a grant of assumptions. Theorem1.2(A) supplies the closed definable image and dimension bound used by3.2. Its upstream ACVF/DOAG quantifier elimination, stable embeddedness and ordered-group facts are external foundations, not newly derived here.

## Authentic text newline lines 1090-1230

```text
à trois sortes (corps valué, corps résiduel, groupe des valeurs).

(0.31) Introduisons quelques notations pour un certain nombre de catégories dont
nous aurons abondamment besoin ; rappelons que les les groupes abéliens ordonnés
et les valuations sont notés multiplicativement.

(0.31.1) On désigne par C la catégorie des corps algébriquement clos non
trivialement valués, et par D celle des groupes abéliens divisibles ordonnés non
triviaux.

(0.31.2) Soit G un groupe abélien ordonné quelconque. On note DG la catégorie
des groupes abéliens divisibles ordonnés non triviaux H munis d’un plongement
(croissant) G → H.
    Soit K un corps valué. Supposons-le muni d’un plongement croissant |K ∗ | → G ;
on note alors CK,G la catégorie des corps algébriquement clos non trivialement
valués L munis d’un plongement isométrique K → L et d’un |K ∗ |-plongement
croissant G → |L∗ |. Lorsque G = |K ∗ |, on écrira CK au lieu de CK,G ;
la catégorie CK est simplement celle des extensions non trivialement valuées
algébriquement closes de K.

(0.31.3) Soit Φ une formule du langage Lval sans paramètres (resp. à paramètres
dans (K, G)), dont les variables libres vivent dans un produit donné S de sortes.
La modèle-complétude de la théorie des corps algébriquement clos non trivialement

                                        1250007-21
A. Ducros


valués assure que

                               F → {x ∈ S (F ), Φ(x)}

est de manière naturelle un foncteur de C (resp. CK,G ) vers Ens. On dira qu’un tel
foncteur est un sous-foncteur déﬁnissable de S (resp. S|CK,G ) vers Ens. Soient S
et S  deux produits ﬁnis de sortes, soit X un sous-foncteur déﬁnissable de S
(resp. S|CK,G ), et soit X un sous-foncteur déﬁnissable de S  (resp. S|C
                                                                          
                                                                            K,G
                                                                                ). On
                                                  
dit qu’une transformation naturelle de X vers X est déﬁnissable si son graphe est
un sous-foncteur déﬁnissable de S × S  (resp. (S × S  )|C(K,G) ) ; l’image d’une
transformation naturelle déﬁnissable est un sous-foncteur déﬁnissable du but.

(0.31.4) Il existe une version abstraite, c’est-à-dire non plongée, de la notion
de sous-foncteur déﬁnissable. Un foncteur X de C (resp. CK,G ) vers Ens est dit
déﬁnissable s’il existe un produit ﬁni de sortes S et un sous-foncteur déﬁnissable X0
de S (resp. S|CK,G ) tel que X ≃ X0 .
      A priori, X0 n’a pas de raison d’être unique à unique isomorphisme déﬁnissable
près. En pratique, il le sera : lorsqu’on dira qu’un foncteur X de C (resp. CK,G )
vers Ens est déﬁnissable, il sera toujours sous-entendu qu’on sait décrire non
seulement X(F ) pour tout F appartenant à C ou CK,G , mais également les familles
déﬁnissables plongées d’objets paramétrés par X, ce qui assurera la canonicité
de X0 . Pour donner un sens rigoureux à cette dernière phrase nous renvoyons le
lecteur à la section 2 de [8].
      Par exemple, si X est un K-schéma de type ﬁni, il déﬁnit de manière naturelle
un foncteur déﬁnissable de CK vers Ens. Et un sous-foncteur de X |CK,G est
déﬁnissable si et seulement si il est déﬁni Zariski-localement sur X par une
combinaison booléenne d’inégalités de la forme |f |     γ|g|, où f et g sont des
fonctions régulières, où γ ∈ G et où ∈ {<, >, ⩽, ⩾} : c’est une conséquence de
l’élimination des quantiﬁcateurs pour la théorie des corps non trivialement valués
algébriquement clos, dans le langage classique des corps valués à trois sortes (le
corps valué, le corps résiduel et le groupe des valeurs).

(0.31.5) On dispose de déﬁnitions analogues sur les catégories D et DG , en se
restreignant au langage des groupes abéliens ordonnés.

(0.32) Soit G le foncteur d’oubli de D vers Ens ; pour tout groupe abélien
ordonné G, on note GG la restriction de G à DG .

(0.33) Fixons un groupe abélien ordonné G. Il résulte de l’élimination des
quantiﬁcateurs dans la théorie DOAG des groupes abéliens ordonnés divisibles non
triviaux qu’un sous-foncteur de GnG est déﬁnissable si et seulement si il peut s’écrire
                                                             
                                                             
                      H → h ∈ H n ,           ϕi,j (h) 
                                                        ij 1
                                                             
                                         i∈I j∈Ii


                                       1250007-22
                            Espaces de Berkovich, polytopes, squelettes et théorie des modèles


où les ensembles I et Ji sont tous ﬁnis, où chacune des ϕi,j est de la
                                                                    i,j ∈ {<, ⩽} pour
forme ate11 , . . . , tenn avec a ∈ G et e ∈ Z pour tout , et où 
tout (i, j).
    Si D est un sous-foncteur déﬁnissable de GnG :

 i) il est entièrement déterminé par sa valeur sur n’importe quel H ∈ DG (par
    complétude de DOAG) ;
ii) l’expression D(H) garde un sens pour tout groupe abélien ordonné H muni d’un
    plongement G → H.


(0.33.1) On dira qu’un sous-foncteur déﬁnissable de GnG est fermé s’il admet une
                                 i,j égal à ⩽ pour tout (i, j).
description comme ci-dessus avec 

(0.33.2) Si r et R sont des éléments de G avec r < R on note ]r; R[ le sous-foncteur
déﬁnissable de GG qui envoie H sur {h ∈ H, r < h < R}. Un pavé de dimension d
de GnG est un sous-foncteur déﬁnissable de GnG de la forme
                            d                            
                          M          ]ri ; Ri [ × {(gd+1 , . . . , gn )}
                               i=1

où les ri , les Ri et les gj sont des éléments ﬁxés de G, avec ri < Ri pour tout i, et
où M ∈ GLn (Q).

(0.33.3) Soit D un sous-foncteur déﬁnissable et non vide de GnG . Soit H ∈ DG
et soit E l’ensemble des entiers d tels que D|DH contienne un pavé de dimension d
de GnH .
    L’ensemble E est non vide (il contient 0) et est inclus dans {0, . . . , n}. Il ne
dépend pas de H, et peut alternativement être décrit comme l’ensemble des entiers d
possédant la propriété suivante : il existe un pavé P de dimension d dans GnH
tel que D(H) contienne P(H). Cela résulte de la complétude de DOAG et du
fait que l’existence d’un sous-foncteur de D de la forme décrite au 0.33.3, où
les dénominateurs des coeﬃcients de M sont de surcroı̂t supposés bornés par un
entier N ﬁxé, est un énoncé du premier ordre dans DOAG.
    Le plus grand élément de E est appelé la dimension de D. Par convention, on
pose dim ∅ = −∞. Il n’y a pas de conﬂit de terminologie : un pavé de dimension d
au sens de 0.33.2 est de dimension d au sens que nous venons de déﬁnir.
    Soit H ∈ DG et soit x ∈ D(H).
    La dimension de D en x est la dimension minimale de P ∩ D|DH ⊂ GnH , où P
est un pavé de dimension n de GnH tel que x ∈ P(H). Si D est de dimension d en
chacun des points de D(H), il est de dimension d en chacun des points de D(H  )
pour tout H  ∈ DG ; on dit alors que D est purement de dimension d.
    On dit que D est purement de dimension d en x s’il existe un pavé P de
dimension n dans GnH tel que x ∈ P(H) et tel que le sous-foncteur P ∩ D|DH
de GnH soit purement de dimension d.

                                           1250007-23
A. Ducros


(0.33.4) Un sous-foncteur déﬁnissable D de GnG est dit connexe si pour tout
couple (D1 , D2 ) de sous-foncteurs déﬁnissables et fermés de GnG tels que
                                             
                             D = (D1 ∩ D) (D2 ∩ D),
```

## Authentic text newline lines 1276-1402

```text
Théorème 1.2. Soit K un corps valué muni d’un plongement de |K ∗ | dans G.
Soit X une K-variété algébrique, soit (g,j ) une famille ﬁnie de fonctions sur X ,
et soit (γ,j ) une famille d’éléments de G. Soit X le foncteur
                                                                   
                                                                   
                       L → P ∈ X (L),           |g,j |(P ) ⩽ γ,j
                                                                   
                                                 j

de CK,G dans la catégorie des ensembles.
    Soit f = (f1 , . . . , fn ) une famille de fonctions inversibles sur le schéma X ,
soit π : X → Gnm,K le morphisme induit, et soit d la dimension de la partie
constructible π(X ) de Gnm,K (si X est intègre, d est le degré de transcendance
de K(f1 , . . . , fn ) sur K).
A) Il existe un sous-foncteur déﬁnissable et fermé D de GnG tel que
                              |f |(X(L)) = D(|L∗ |) ⊂ |L∗ |n
   pour tout L ∈ CK,G , et la dimension de D est majorée par d.
B) Supposons X intègre. Pour tout H ∈ DG et tout h = (h1 , . . . , hn ) ∈ H n , les
   assertions suivantes sont équivalentes :
    i) h ∈ D(H) ;
   ii) il existe une valuation |.| sur K(X ) prolongeant la valuation de K, à valeurs
       dans un groupe ordonné H  ∈ DH , telle que
                                                 |g,j | ⩽ γ,j
                                            j

       et telle que |fi | = hi pour tout i.
       En particulier, D ne change pas si l’on remplace X par un de ses ouverts
       de Zariski non vides.
C) Supposons que X = X|CK,G , et soit K h le hensélisé de (K, |.|).
   C1) Si XK h est connexe alors D est connexe.
   C2) Supposons que π(X ) est purement de dimension d. Le sous-foncteur D est
       alors purement de dimension d, et égal à GnG si X = ∅ et n = d.
    Démonstration. Commençons par prouver A). L’image de |f | est un sous-
foncteur déﬁnissable du foncteur L → |L∗ | de C(K,G) dans Ens, et un tel sous-
foncteur est nécessairement de la forme L → D(|L∗ |) pour un certain sous-foncteur
déﬁnissable D de GnG (qui est uniquement déterminé). Il reste à s’assurer que D est
fermé et de dimension ⩽ d.
(1.2.1) Le foncteur D est fermé. On peut décrire D par une combinaison booléenne
                                            ϕi,j 
                                                 i,j 1
                                    i   j

où les ϕi,j et les 
                    i,j sont comme en 0.33. On peut supposer que pour tout i, le
                                              
sous-foncteur de D décrit par la conjonction j ϕi,j 
                                                     i,j 1 est non vide (sinon, on

                                        1250007-25
A. Ducros


le retire de la description de D). Nous allons montrer que D peut être décrit par la
condition

                                                    ϕi,j ⩽ 1.
                                           i    j

Il suﬃt pour cela de montrer que pour tout i le sous-foncteur de GnG déﬁni par la
                   
conjonction j ϕi,j ⩽ 1 est contenu dans D.
     Fixons i, et écrivons ϕj et         j au lieu de ϕi,j et      i,j . Soit L ∈ CK,G et
soit (r1 , . . . , rn ) un point de |L∗ |n en lequel ϕj ⩽ 1 pour tout j. Nous allons prouver
qu’il appartient à D(|L∗ |), ce qui permettra de conclure. Soit D  le sous-foncteur
                                        
de D déﬁni par la conjonction j ϕj            j 1 ; il est non vide par hypothèse.
     La formule (h1 , . . . , hn ) → max(h−1                  −1
                                                    i ri , hi ri )i déﬁnit un morphisme de
foncteurs de D|D|L∗ | dans G|L∗| . Son image est un sous-foncteur déﬁnissable
                        

de G|L∗| ; par o-minimalité, celui-ci admet une borne inférieure a, appartenant
à |L∗ | et supérieure ou égale à 1.
     Montrons que a = 1. On raisonne par l’absurde. Supposons a > 1. Par déﬁnition
de a, il existe (s1 , . . . , sn ) ∈ |L∗ |n tel que les propriétés suivantes soient vériﬁées :

α) a−3/2 ⩽ si ⩽ a3/2 pour tout i ;
β) il existe i tel que si ⩽ a−1 ou si ⩾ a ;
γ) (r1 s1 , . . . , rn sn ) ∈ D  (|L∗ |).
                                        1/2             1/2
     Par convexité, le point (r1 s1 , . . . , rn sn ) satisfait l’inégalité ϕj ⩽ 1 pour
tout j. Par minimalité de a et comme a3/4 < a puisque a > 1, il ne peut
appartenir à D  (|L∗ |). Il existe donc j tel que       j soit égal à < et tel que ϕj vaille 1
           1/2             1/2
sur (r1 s1 , . . . , rn sn ). L’application ϕj prend alors une valeur inférieure ou égale
                                                    1/2         1/2
à 1 en (r1 , . . . , rn ), la valeur 1 en (r1 s1 , . . . , rn sn ), et une valeur strictement
inférieure à 1 sur (r1 s1 , . . . , rn sn ) ; mais c’est contradictoire avec le caractère aﬃne
de ϕ.
     Soit H le groupe ordonné divisible |L∗ | ⊕ Q , où  est inﬁniment proche
supérieurement de 1. Soit F une extension valuée algébriquement close de L de
groupe des valeurs H.
     Comme a = 1, il existe (s1 , . . . , sn ) ∈ Q tels que le n-uplet (r1 s1 , . . . , rn sn )
appartienne à D  (H) = D  (|F ∗ |). Comme D  est un sous-foncteur de D, il
existe P ∈ X(F ) tel que |f |(P ) = (r1 s1 , . . . , rn sn ).
     Le groupe Q est un sous-groupe convexe de H ; le quotient H/Q s’identiﬁe
à |L∗ |. La valuation de F peut donc être rendue plus grossière en la composant avec
la ﬂèche quotient H → |L∗ | ; le corps valué F0 ainsi obtenu a même corps sous-
jacent que F , et est toujours une extension valuée de L. Comme le foncteur X est
déﬁni par des inégalités larges, P ∈ X(F0 ) ; son image par |f | dans |F0∗ |n appartient
donc à D(F0∗ ). Mais |F0∗ | = |L∗ | ; et l’image de P dans |F0∗ |n est égale à l’image
de (r1 s1 , . . . , rn sn ) par la ﬂèche quotient H n → |L∗ |n , c’est-à-dire à (r1 , . . . , rn ).
Ainsi, ce dernier appartient à D(|L∗ |), ce qu’il fallait démontrer.

                                               1250007-26
                              Espaces de Berkovich, polytopes, squelettes et théorie des modèles


(1.2.2) Majoration de la dimension de D. Soit L ∈ CK,G , et soit P un pavé
de Gn|L∗| contenu dans D|D|L∗ | . On note δ la dimension de P ; nous allons montrer
que δ ⩽ d. Quitte à composer π avec une isogénie du tore Gnm,K , on peut supposer
que P est décrit (universellement) par des conditions de la forme
                 ri < hi < Ri ,     1⩽i⩽δ                et hi = γi ,   i ⩾ δ + 1,
où les ri , Ri et gi appartiennent à |L∗ |.
    Soit H le groupe ordonné divisible |L∗ | ⊕ 1Q ⊕ · · · ⊕ δQ , où chacun des j est
inﬁniment proche supérieurement de 1 relativement au groupe engendré par |L∗ | et
les i pour i < j. Soit F une extension valuée algébriquement close de L de groupe
des valeurs H.
    L’élément (r1 1 , . . . , rδ δ , gδ+1 , . . . , gn ) de H n appartient à P(H), et donc
à D(H). Il est dès lors égal à |f |(P ) pour un certain P ∈ X(F ). Le point P induit
un point x du schéma XL , et une valuation |.| sur L(x).
    Si l’on pose L0 = L(f1 (x), . . . , fn (x)) ⊂ L(x) alors |L∗0 | contient les ri i ,
qui sont Q-linéairement indépendants modulo |L∗ | ; par conséquent, le degré de
transcendance de L0 sur L est au moins égal à δ.
    Le corps L0 s’identiﬁe par ailleurs au corps L(π(x)) ; il s’ensuit que le degré
de transcendance de L0 sur L est majoré par d, puis que δ ⩽ d, ce qu’il fallait
démontrer.
```

