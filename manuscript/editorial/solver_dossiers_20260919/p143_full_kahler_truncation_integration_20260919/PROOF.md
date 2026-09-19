# P14.3 full Kähler truncation closure — production proof

## 1. Decreasing stability of the MP cone

Let `H=PL(K) intersect PSH_MP(alpha)`.  For every `j`, choose a decreasing
model net `h_(j,lambda) downarrow phi_j` in `H`.  Let `S` consist of all
`h in H` such that

`h >= phi_j + epsilon`

for some `j>=1` and some positive rational `epsilon`.  Rational translation
shows that `S` is nonempty.

We prove that `S` is downward directed.  Suppose
`h_i >= phi_(j_i)+epsilon_i` for `i=1,2`.  Choose
`j>=max(j_1,j_2)` and a positive rational `delta` with
`4 delta < min(epsilon_1,epsilon_2)`.  For the continuous comparison
function `g=min(h_1,h_2)`, one has `phi_j+4 delta<g` everywhere on compact
`K`.  The open sets

`{h_(j,lambda)+2 delta<g}`

form a directed increasing cover of `K`.  Compactness first gives a finite
subcover, and directedness of the approximating net then gives one index
`lambda` for which the displayed inequality holds on all of `K`.  Therefore

`h=h_(j,lambda)+delta`

belongs to `S` and satisfies `h<=h_1,h_2`.  The minimum `g` was used only as
a continuous comparison function; no closure of the psh cone under minima
is assumed.

Order `S` by reverse pointwise order.  Its identity net is a decreasing net
in `H`.  Every member dominates `phi=inf_j phi_j`, so the net's infimum is at
least `phi`.  Conversely, fix `x in K` and a real `b>phi(x)`.  Choose `j`
with `phi_j(x)<b`, and then choose a positive rational `epsilon` and an index
`lambda` such that `h_(j,lambda)(x)+epsilon<b`.  The function
`h_(j,lambda)+epsilon` belongs to `S` and is smaller than `b` at `x`.
Thus `inf_(h in S) h=phi` pointwise, including where `phi=-infinity`.
Since the limit is not identically minus infinity, the defining MP
decreasing-net completion gives `phi in PSH_MP(alpha)`.

## 2. Finite-energy truncations

Fix a DXZ object `Gamma`, write `c=Gamma_max`, and set
`c_j=max(c,-j)`.  In every Kähler perturbation class `omega+eta`, the
constant object of value `-j` has level zero for `tau<-j`.  The maximum
`Gamma^(j)=Gamma vee (0-j)` dominates that object, while each normalized
model level is at most zero.  Hence

`(Gamma^(j),omega+eta)_tau=0` for `tau<-j`.

Its minus-infinity level therefore has full mass in every perturbation
component, so its DXZ volume equals
`V_alpha=int_X omega^n>0`.  Positive-volume recovery supplies an
unperturbed positive-mass test curve `gamma^(j)` in the class `omega`.
The levelwise recovery formula preserves the zero tail, so
`gamma^(j)_tau=0` for `tau<-j`.  Consequently

`E^0(gamma^(j)) = c_j V_alpha
                  + int_(-j)^(c_j)(M_omega(gamma^(j)_tau)-V_alpha) d tau`

lies in `[-j V_alpha,c_j V_alpha]`, because the integrand lies in
`[-V_alpha,0]`.  Thus `Gamma^(j)` has finite energy.  This proves finite
energy from the actual zero tail of the recovered curve, not from a merely
divisorial lower bound.

## 3. Recovery of the original DXZ object

Maximum is monotone, so `Gamma^(j)` decreases with `j`.  Its endpoints are
`c_j downarrow c`, and hence the decreasing DXZ infimum exists.  At every
positive rational divisorial point `q`, the maximum and infimum formulas give

`T_(inf_j Gamma^(j))(q)
 = inf_j max(T_Gamma(q),-j)
 = T_Gamma(q)`.

The endpoint formula gives the same equality at the trivial semivaluation.
Divisorial injectivity therefore yields

`inf_j Gamma^(j)=Gamma`.

## 4. Positivity of the literal raw transform

Let `phi_j in E^1_MP(alpha)` correspond to `Gamma^(j)` under the
finite-energy bijection.  The established all-point finite-energy comparison
gives

`phi_j=T_(Gamma^(j))`

on all of `K`.  The sequence is decreasing by monotonicity of the raw
transform.  At the trivial semivaluation,

`inf_j phi_j(0)=inf_j c_j=c> -infinity`,

so `phi=inf_j phi_j` is not identically minus infinity.  Section 1 gives
`phi in PSH_MP(alpha)`.  The divisorial maximum formula and the endpoint
formula give `phi=T_Gamma` on the entire rational divisorial locus.

By the assumed P14.2 conclusion, `T_Gamma` is upper semicontinuous.  It is
antitone for ideal order directly from its multiplier-ideal formula.  The
dominated divisorial comparison interface therefore promotes the divisorial
equality to

`phi=T_Gamma`

at every semivaluation.  This proves both the asserted pointwise truncation
formula and that the literal raw transform maps the entire DXZ cone into the
MP cone.

## 5. Isomorphism, order, and energy

Established interface 6 supplies the previously constructed section
`S_alpha` and the identity `T_alpha o S_alpha=id` on the full MP cone.
Since the raw transform is
divisorially injective, `S_alpha o T_alpha=id` on the DXZ cone.  Pointwise
monotonicity of the raw transform and divisorial order reflection show that
both maps preserve and reflect order.  On the finite-energy locus,
divisorial identification and injectivity identify this map with the existing
finite-energy DXZ--MP correspondence, so its energy identity applies.  This
completes the proof.
