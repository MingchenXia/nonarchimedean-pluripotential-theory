# General-measure parabolic comparison: source audit, 8 October 2026

The controlling source is Bowoo Kang, *A general comparison principle for the pluripotential complex Monge–Ampère flow*, [arXiv:2511.06412v3](https://arxiv.org/abs/2511.06412v3), revised 15 December 2025. The entire 21-page PDF was actually read as complete selected text and eleven individually displayed matching images, with sequential notes. Acquisition, metadata, image preparation and evidence export add no reading credit. No cited foundational proof was recursively inspected in this checkpoint. The dd^c convention is not explicitly stated in the inspected source.

The setting is a bounded strictly pseudoconvex domain, bounded spatial psh potentials locally uniformly Lipschitz in time, a measure dominated by the Monge–Ampère measure of a bounded zero-boundary psh function, and the specified continuous nondecreasing F. The new comparison requires both functions to be locally uniformly time-semiconcave; lateral boundary ordering and an L1(mu) initial trace must not be silently strengthened. The general statement is not a compact singular-space or non-Archimedean flow theorem.

## Controlling exclusions

The printed proof of Lemma 3.6 (physical pages 13–14) uses a signed integral bound on an open U to bound the integral on a time-dependent strict sublevel by A t times its measure in the third inequality of (3.7). That implication is unsupported. The direct logarithmic-well calculation below satisfies all four printed hypotheses and gives positive strict-sublevel mass arbitrarily close to t=0. It includes a smooth positive finite reference measure, a uniform open-set constant, both time-semiconcave functions, smooth matching lateral values and pointwise/L1 initial traces. Twelve exact checks and twelve finite fixtures support the constants; the infinite-family argument, rather than finite fixtures alone, establishes the diagnostic.

Theorem 3.8 explicitly relies on this lemma on page 17. Its final time shift on page 18 additionally changes the actual initial value to u(epsilon0) and lateral value to h1(t+epsilon0)-kappa_F epsilon0 t. The stated old initial ordering and assigned h1(t)-kappa_F epsilon0 t do not follow. The printed epsilon0<S-T has a sign typo, but correcting that typo does not settle the trace issue. Lemma 3.3's proof needs the supersolution's time semiconcavity although its printed signature omits it; the main theorem does supply that condition.

The logarithmic-well example does not satisfy the flow supersolution inequality against Lebesgue measure. It is therefore a diagnostic of the auxiliary lemma, not a disproof of the main comparison theorem. General-measure comparison, its uniqueness consequence and the long-time conclusion remain **UNVERIFIED in this audit**. They are excluded from the book's proved inputs. The explicit stationary barrier computations remain conditional on a valid comparison and stationary-existence input, with a lower/upper slope interval containing every barrier argument. Reference 21 is Kołodziej alone (2000); note 11 corrects the provisional Kołodziej–Nguyen attribution in historical note 10.

These source and diagnostic records leave the active 4,612-page book and native catalogue unchanged. The 42 canonical atoms and twelve formal problem environments retain their statuses; general critical homogeneous BJ22 Siu division/envelopes remain OPEN and LPWZ density remains UNVERIFIED. No original theorem, priority claim, independent gpt-6.1-sol xhigh receipt or GitHub publication is claimed.

## Direct diagnostic and proof

# Diagnostic of Kang v3 Lemma 3.6

This is a direct worked one-dimensional example and an audit artifact, not an independently verified original theorem. It tests the printed auxiliary lemma, not the sub/supersolution comparison theorem. The controlling locator is physical pages 13–14 of arXiv:2511.06412v3, especially the third inequality of (3.7). No flow differential inequalities are claimed for the example.

Take Omega={|z|<1}, T=1/64, mu=ordinary planar Lebesgue measure. All subharmonic functions are locally mu-integrable. This measure is also dominated by dd^c of a suitable positive multiple of |z|^2-1, a bounded zero-boundary subharmonic function, for any fixed positive conventional normalization of dd^c.

For k>=1 set a_k=2^(-k-3), e_k=2^(-k^2-10), r_k=3 exp(-1/e_k), and

    b_k(z)=max{e_k log(|z-a_k|/3), -1},
    b(z)=sum_{k>=1} b_k(z),     |z|<2.

Each term is subharmonic and nonpositive on {|z|<2}. The discs D_k={|z-a_k|<a_k/4} are disjoint: successive center separation is a_k/2, larger than the sum 3a_k/8 of the radii; nonconsecutive separations are larger still. Outside D_k, b_k>=-e_k log(12/a_k). Write

    S=sum e_k log(12/a_k)
      <= (log(96)+2 log(2))/1024 = log(384)/1024 < 1/100.

This uses k^2>=k, sum 2^-k=1 and sum k 2^-k=2. At most one disc contains a given point, so -1-S<=b<=0 throughout {|z|<2}. The decreasing partial sums therefore define a bounded subharmonic function. Also r_k<a_k/4 because e_k log(12/a_k)<=S<1. The function b is harmonic in a common annulus containing the unit circle: all its Riesz circles lie inside {|z|<5/64}, and the series converges locally uniformly there. At z=a_k it is smooth in a sufficiently small neighborhood: the k-th term is constant on {|z-a_k|<r_k}, and the other terms form a locally uniformly convergent harmonic series. At the centers b(a_k)<=-1; at zero b(0)>=-S, so b is bounded but discontinuous near zero.

Use the compactly supported radial C^3 kernel

    chi(w)=(5/pi)(1-|w|^2)^4 for |w|<1, and 0 otherwise.

It is nonnegative and has integral one, second moment m2=1/6, and logarithmic moment integral chi(w) log|w| dA=-137/120. These exact constants are checked separately. C^3 regularity suffices for two time derivatives of the scaled kernel. Set

    u(t,z)=integral chi(w)b(z-sqrt(t)w)dA(w),
    v(t,z)=b(z),       u0=v0=b,       eta(t)=0.

For 0<t<T the convolution only uses {|z|<2}. Radial submean gives u>=b. Both functions are bounded spatially subharmonic potentials. The scaled kernel has bounded first and second time derivatives on every compact positive-time interval, uniformly in z because b is bounded on {|z|<2}; consequently u is locally uniformly time Lipschitz and even locally uniformly time semiconcave. The static v has the same properties. In a common collar of the unit boundary u=v by the radial mean value property of b. Thus the lateral boundary inequality in Lemma 3.6 holds, eta=0 gives (b), and the initial order (d) is equality. Standard subharmonic radial regularization gives pointwise u(t,z)->b(z), in addition to the L1 trace checked below.

The open-set signed-integral hypothesis (c) actually holds here with one constant for every open U compactly contained in Omega. To see its exact bound, Jensen's circle identity gives

    b_k(z)=e_k average_theta log(|z-(a_k+r_k exp(i theta))|/3).

For |q|<1,

    integral_{|z|<1} log|z-q| dA(z)=(pi/2)(|q|^2-1).

Every Riesz-circle point, even after translation by sqrt(t)w, remains inside the unit disc: 5/64+1/8=13/64<1. Averaging the last formula, the radial kernel's first moment vanishes and yields

    integral_Omega [u(t,z)-b(z)] dA(z)
        =(pi/2)m2 t sum e_k=(pi/12)t sum e_k.

The same formula first holds for finite sums and then passes to the infinite sum by bounded/monotone convergence. Since u-b>=0, for every such U

    integral_U u(t) dmu <= integral_U u0 dmu + A t,
    A=(pi/12)sum e_k<infinity.

It remains to test the purported zero strict-sublevel conclusion. Set epsilon_k=a_k/8 and t_k=epsilon_k^2. Each convolution at a_k stays inside D_k, hence the other terms contribute at least -S. Since max{e_k log(|epsilon_k w|/3),-1}>=e_k log(|epsilon_k w|/3),

    u(t_k,a_k)>=-S-e_k[log(3/epsilon_k)+137/120].

For k>=1 the second error is at most (log(384)+137/120)/2048: the sequence 2^-k(log(192)+k log(2)+137/120) is decreasing, and e_k<=2^-k/1024. Therefore

    S+e_k[log(3/epsilon_k)+137/120]
      <= log(384)/1024+(log(384)+137/120)/2048 < 1/100.

Thus u(t_k,a_k)>-1/100 and v(t_k,a_k)<=-1. In particular

    u(t_k,a_k)-v(t_k,a_k)>99/100 > (1+T)/2.

Use the single fixed tolerance epsilon=1/2 in Lemma 3.6. For every k, the point (t_k,a_k) belongs to {v+(t+1)/2<u}. The two functions are continuous on a neighborhood of this point (v is smooth near a_k), so that strict sublevel contains a genuine open time-space neighborhood and has positive dt wedge dmu mass there. As t_k->0, every positive initial time cylinder contains such a neighborhood. Its strict-sublevel mass cannot vanish as the lemma asserts.

All four printed hypotheses of Lemma 3.6 hold, with a finite smooth positive measure, uniform open-set constant A, both time-semiconcave potentials, matching smooth lateral boundary values and pointwise/L1 initial convergence. The missing implication is substantive. The example is not a supersolution: the static b has singular circle Riesz measures and does not satisfy the required parabolic supersolution inequality against Lebesgue measure. It therefore does not disprove Theorems 1.2/3.8, their uniqueness assertion or the convergence claim. Those remain unverified in this audit until a valid replacement argument is supplied.

No insertion into the book, canonical problem-status change, theorem promotion, priority claim or independent gpt-6.1-sol xhigh receipt is made here.
