# Finski published completion and proof interfaces, 9 October 2026

The controlling source is Siarhei Finski, *Submultiplicative norms and
filtrations on section rings*, Proceedings of the London Mathematical
Society (2025), DOI 10.1112/plms.70077. This is the forty-seven-page
published author copy, not the forty-four-page arXiv revision. Its PDF
SHA256 is `1d0c7c19f3d5bf36aada5ac7f2530c9b1bafb8de0264ad1ddad84edd7260b740`.

All forty-seven physical pages have now been actually read with complete
text and individually displayed matching images. The pinned preceding
metric/radial checkpoint supplies pages 1–24 in twelve views; the fresh
completion supplies 25–47 in twelve views. The union is exactly 1–47,
twenty-four matching views in those two ordered checkpoints. The older
5 October endpoint record independently contains 1, 15, 35 and 36.
Compared with the union of that named record and the preceding 1–24
selection, this completion freshly reads twenty-three pages, repeats
35–36, and adds twenty-one unique pages. These are distinct counts.
Preparation, reinspection of earlier definitions, export and upload add
zero actual page credit. Old notes, receipts and scope corrections remain
unchanged. This complete physical-PDF reading does not certify every
original theorem cited by the paper, or any different source edition.

The book remains the verified 4,663-page edition at this source-only
checkpoint. No chapter, bibliography or native catalogue/editor is
changed here. The canonical forty-two atoms in twelve formal problems
retain their statuses. General BJ22 critical homogeneous Siu and envelope
interfaces remain OPEN; LPWZ density remains UNVERIFIED. The user's BJ22
Theorem 6.21 proof warning remains binding. No original general theorem,
independent hostile-model receipt or new complete ordered book pass is
claimed. The last complete ordered book pass remains 4 October.

## Complex symmetric tensors: what the proof uses

Physical 25 states Theorem 3.13 for a fixed finite-dimensional complex
normed vector space: diagonal evaluation, injective and projective norms
on its symmetric algebra are asymptotically equivalent. Equation (3.29)
orders them. This is neither exact equality in each degree nor a statement
about all tensor powers without symmetrization. The cited exponential
full-tensor gap and its original Pisier/Aubrun–Müller-Hermes proofs remain
external inputs. Lemma 3.16 on physical 26 identifies the quotient and
restricted symmetric tensor norms through the normalized permutation
average, a contractive projection because permutations are isometries.
This projection argument does not identify arbitrary projective and
injective norms with each other.

For the complex l1 space of dimension r, Theorem 3.13 has a direct
coefficient explanation. Write a homogeneous polynomial of degree k as
P(z)=sum_{|alpha|=k} a_alpha z^alpha. The evaluation norm is its supremum
on the complex unit polydisc, and the projective symmetric norm is
sum |a_alpha|, by (4.6)–(4.7). On the unit torus with normalized Haar
probability, orthogonality gives

    integral |P|^2 = sum |a_alpha|^2 <= ||P||_polydisc^2.
    sum |a_alpha| <= sqrt(D_{r,k}) ||P||_polydisc,
    D_{r,k} = binomial(r+k-1,r-1).

For fixed r, D_{r,k} is polynomial in k, so its square-root distortion
has logarithm o(k). This is the attributed alternative in Remark 4.3 on
physical 29. It bypasses the separately cited dimension-uniform
Bohnenblust–Hille asymptotic theorem for this fixed-r application. It does
not supply a bound uniform in an arbitrarily growing number of variables.
The printed dimension binomial(r+k,r) on physical 28 counts degree at
most k; for homogeneous degree exactly k the dimension is D_{r,k}.
The printed larger value is still a polynomial upper bound sufficient
for (4.5), so this local count error does not refute Proposition 4.1.

The complex field matters. Physical 25 uses P(x,y)=xy(x^2-y^2). On the
real dual l-infinity square its maximal square is 4/27, attained when one
coordinate has modulus one and the other's square is 1/3. Its real
evaluation norm is 2 sqrt(3)/9. The coefficient l1 norm is 2, and powers
have coefficient norm 2^k, giving an exponential gap. On the complex
polydisc P(1,i)=2i, and the elementary upper bound is also 2. The real
example is therefore consistent with, and does not refute, the complex
theorem. The independent full-tensor statement is a different question.

## Quotients and holomorphic extension

Lemma 4.4 on physical 30 approximates a fixed complex norm by a quotient
of a finite-dimensional l1 space, within e^epsilon. The quotient dimension
may depend on epsilon. One first fixes this approximation and only then
takes the tensor degree k to infinity; no joint dimension-uniform limit
is obtained. The quotient map induces a dual linear projective embedding
and the restriction diagram (4.10). Its quotient norm gives the exact
degree-one FS restriction identity (4.11).

Theorem 3.10 then supplies an extension g of a polynomial f, with
||g||_ev <= e^(epsilon k)||f||_ev. On the ambient space the symmetric
comparison gives ||g||_Sym,pi <= e^(epsilon k)||g||_ev, and contraction
of the quotient gives ||f||_Sym,pi <= ||g||_Sym,pi. Multiplying these
three inequalities gives (4.16), with e^(2 epsilon k). This is the actual
argument using (4.12), (4.13) and (4.15). The printed lead-in to (4.12)
refers to that formula and the next one itself; the relevant preceding
geometric identities are (4.10)–(4.11). Physical 31 then refers to (4.17)
and (4.18), although the section ends with (4.16). These are source-local
cross-reference errors, not counterexamples to the reconstructed quotient
argument with its stated holomorphic-extension input.

Physical 26–27 transfers symmetric comparison to a projective section
ring through symmetrization and Kodaira restriction. Theorem 3.1 is an
asymptotic quotient statement. Its opening phrase “get the norm” must
be read with the subsequent subexponential equivalences, not as an exact
finite-degree quotient isometry. Surjective multiplication, sufficiently
large degree-one-generated Veronese powers, positivity and the metric
regularity required by the extension theorem remain separate premises.
The original Ohsawa–Takegoshi, Bost and Finski extension proofs are not
recursively established by reading this paper.

## Homogenization and its source research question

Theorem 3.17 on physical 27 assumes a bounded submultiplicative graded
norm on an ample complex section ring and identifies its homogenization
with the sup norm of its raw asymptotic FS metric. Its dyadic proof uses
decreasing upper-semicontinuous maxima on a compact manifold. Nested
open sublevel sets and a finite subcover justify sup/limit interchange
for that sequence. They do not justify interchange for arbitrary
nonmonotone sequences. They also do not replace the raw metric with its
regularization without the separate finite-p comparison.

The section ring is commutative. Gelfand's spectral-radius seminorm
argument must retain that condition: the matrices A=[[0,1],[0,0]] and
B=[[0,0],[1,0]] both have radius zero, while (A+B)^2=I and A+B has radius
one. Spectral radius is thus not a seminorm on arbitrary noncommutative
Banach algebras. Reference [40] is explicitly *Commutative normed rings*.

Corollary 3.20 gives finite-p asymptotic equivalence to homogenization;
the infinity endpoint additionally requires continuous raw FS. Remark
3.21 asks for an independent proof without first establishing Theorems
1.1 and 1.3. A precise source question is: for an ample L on a smooth
complex projective X and bounded submultiplicative genuine graded norms
N_m, prove directly that m^(-1)d_p(N_m,N_m^hom) tends to zero for every
finite p, where N_m^hom(s)=lim_l N_{ml}(s^l)^(1/l). Establish the continuous
raw-FS infinity endpoint separately. An argument using the already
derived FS isometry or classification in disguise is not independent.
The paper proves the desired conclusions through its main theorems;
what it asks for is a different proof route, not an unproved conclusion.
No such independent route is certified by this checkpoint. This is a
dated source research question, not a new canonical atom or a claim that
the methodological question is still unresolved in all later literature.

Remark 1.4(c), rechecked on already-read physical 3 with zero fresh page
credit, asks about big polarizations. The established classification
range here is ample. For a big nonample L, FS weights have singularities
from base loci; smooth-positive extension and global bounded-metric
arguments do not automatically apply. A formulation must specify the
admissible singularity type, the finite sup norms and degree-normalized
spectral distances before claiming a finite-p extension. A separate
infinity endpoint needs appropriate additional regularity. No big-class
generalization is proved here. The separately read March 2026 Reboulet
filtration and October 2025 RWN flat revisions retain their own fields,
admissibility and proof dependencies and do not automatically answer
these complex ample/big proof-route questions.

## Narasimhan–Simha: convexification, integrability and positivity

Physical 31–33 treats log-canonically ample klt pairs. The klt condition
is imposed on the coefficients of the crepant log resolution, including
exceptional components. A half-boundary in one complex variable gives
the meromorphic density |z|^(-1): it is infinite at zero but integrable
against area. Thus the printed claim that the integrand is finite means
integrability, rather than pointwise finiteness on the divisor. Likewise
quasi-psh functions are bounded above on the compact manifold; they need
not have a lower bound. This is sufficient for the e^phi upper bound in
the volume-form discussion. The denominator r, r-th tensor power and
the volume-form phase/normalization in (5.4) must be retained when the
supercanonical envelope uses a volume bound of one.

Hölder with reciprocal exponents k/(k+l) and l/(k+l) proves product
control. Theorem 5.1 concerns the convex hull of the Narasimhan–Simha
pseudonorms, not the unconvexified objects. The convex hull product
argument sums all pairs of decomposition pieces, as in the book's norm
envelope calculation. The uniform metric convergence and continuous
nonzero supercanonical metric in Theorem 5.2 are attributed to
Berman–Demailly [8]. Remark 5.3 says effectiveness of the boundary was
not used in that original proof; this extension is not certified by a
bibliography entry or by the paper's assertion alone. The argument does
not establish the same strong classification for arbitrary psef pairs.

## Rays, spectra and the raw NA FS convention

Physical 34–36 starts from a bounded multiplicative filtration and a
bounded regularisable-from-above psh reference. Definition 1.5 on
physical 4 explicitly includes boundedness; this is not an arbitrary
unbounded finite-energy initial metric. Sum-envelope rays are
submultiplicative, and their comparison with Hermitian rays is only
asymptotic. The spectral measures use probability mass 1/h0(X,mL),
weights divided by m and the -dot(h)/2 convention. The Bergman tail
infimum and regularization in (6.4), and its t -> 2t conversion, are
not a finite exact norm identity. A common degree-linear sign shift
puts weights on a nonpositive compact interval. On that interval all
absolute moments determine the integer signed moments and hence the
weak law. Without the sign shift, delta(-1) and delta(1) have identical
absolute moments. The log(rank) comparison error is divided by degree.

Section ring (1.1) includes degree zero. Therefore the printed F^0R=0
in (6.7), after a degree-linear shift, must concern positive-degree
pieces: the unit keeps weight zero. A blanket divisorial projection
(X times disc)_div -> X_div on physical 37 similarly needs the trivial
restriction included; ord_(X times {0}) restricts to zero on C(X).
The Gauss section for the stated nontrivial rational divisorial inputs
is well defined and assigns value one to the parameter. For a Cartier
centre, ord_Sigma is defined directly, since its blowup has no exceptional
divisor. Individual finite-degree FS functions are real-valued everywhere
only in base-point-free degrees, not in all small degrees of arbitrary
ample L.

There is a substantive literal identification issue between the raw
additive supremum (6.15) and the PSH_NA membership in Theorem 6.6.
On P1,O(1) over trivially valued C, fix p=[1:0] and a>0. Give a nonzero
degree-m section weight -am if it does not vanish at p, and weight zero
if it does. This is a bounded multiplicative filtration: nonvanishing
products add weights and a vanishing product has weight zero at least
their sum. At p, the raw FS supremum is -a. At any finite Gauss valuation
v(T)=b>0, the section T X0^(m-1) contributes -b/m, so the supremum is
zero. Gauss points with b tending to infinity converge to p. The raw
function has a downward jump and is not upper semicontinuous; its usc
regularization is zero. It cannot itself be the decreasing-net limit
of continuous FS functions used to define PSH_NA on physical 38.

The canonical PSH extension must therefore be distinguished from the
raw formula on all semivaluations. In this example the raw function and
the canonical extension agree on divisorial tests, which explains why
the intended maximal-ray correspondence is not refuted by the displayed
raw-function defect. It is the same kind of distinction already proved
in the book's L.99 example. In multiplicative complex metric notation,
FS(N)_* is lower-semicontinuous regularization; the associated additive
weight uses upper-semicontinuous regularization after taking the negative
logarithm. That sign change must be explicit. The new toy calculation
does not solve general homogeneous Siu or envelope problems.

## Canonical approximations, volume and finite-type bridges

Physical 39–42 passes to sufficiently large degree-one-generated
Veronese powers and multiplicative degree sequences. On R(X,L^k), native
degree j has original degree kj. A constant original weight -m has
volume -1 by (6.18), whereas its unrescaled induced Veronese filtration
has native volume -k. The continuity notation (6.19) must either divide
that native volume by k or explicitly rescale the induced weights.
The native doubled norm distance at time t is 2tk; feeding the native
volume -k into the printed -2tk vol term of (6.23) would give 2tk^2.
The intended original-degree normalization instead gives 2tk, consistent
with the 1/k distance transport in (6.20). This diagnoses a missing
convention and does not refute the correctly normalized approximation
theorem. Initial potential and reference class must also be transported
by k before taking their roots; an unchanged initial u followed by u/k
would not reproduce u at time zero.

Integer rounding changes finite weights by less than one and preserves
multiplicativity through floor(a+b) >= floor(a)+floor(b). At fixed t its
ordinary logarithmic-length error is at most t, or doubled normalized
error at most 2t/m. This yields equality of limiting rays, not finite
equality or control uniform in all unbounded times. The distance
subtraction (6.22) and (6.35) uses ordered chains and actual limits,
not arbitrary triangle subtraction or limsup algebra. Maximal-ray
convergence retains the external canonical energy and maximal energy-
slope identities. Common bounded estimates at fixed t remain separate
from arbitrary monotone approximation or unbounded energy families.

Physical 43–44 types the test-configuration extension of a degree-k
section as a section of mathcal L^k. The printed mathcal L occurrences
in the extension and (6.40) need that power, with a distinct integer q
for clearing its pole. Identification with the complete central-fibre
section ring in every small degree needs cohomology and base change;
relative ampleness gives the eventual high-degree identification needed
by the asymptotic argument. Flatness alone is not all-degree surjectivity.
The Dirichlet bridge uses an ample normal test configuration, a bounded
psh extension, normalization, an equivariant resolution and a smooth
positive initial metric. Pullback to the resolution need not preserve
ampleness. Uniqueness is with the same prescribed boundary data and
bounded psh class, not arbitrary weak local current data.

## Exact external identities and next proof audit

Physical 45–47 was read completely, including acknowledgements and all
seventy-six references. Their titles and publication information are
bibliographic evidence, not original proof-reading credit. In particular,
[7] is Berman–Boucksom–Jonsson, *A variational approach to the
Yau–Tian–Donaldson conjecture*, JAMS 34 (2021), 605–652. [16] is
Boucksom–Jonsson, *A non-Archimedean approach to K-stability, I: metric
geometry of spaces of test configurations and valuations*, Annales de
l'Institut Fourier 75 (2025), 829–927. This is a different publication
from the user's BJ22 Siu warning. Neither that distinction nor a full
reading of Finski proves independence of every original [16] argument
from its own references.

The next original proof audits are [16] Theorem 5.4, Lemma 6.17(iii),
Section 3.6 and Lemma A.12; [7] Theorems 6.2, 6.4, 6.6 and Corollary 6.7;
the precise holomorphic quotient extension used in Theorem 3.10; and
[8] Proposition 5.19/Remark 5.23 if the Narasimhan–Simha application is
to be expanded. Phong–Sturm's distinct 2007 and two 2010 papers retain
their original existence, uniqueness, boundary and regularity premises.
No general maximal-ray or singular extension result is promoted solely
from this reading. Fourteen exact elementary diagnostic families support
the local calculations and convention checks. The current book and
canonical statuses remain unchanged at this source-only checkpoint.
