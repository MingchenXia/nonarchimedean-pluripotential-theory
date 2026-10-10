# Formula rendering correction to the frozen relative Hessian audit

The inline-math formatting pass in the frozen source audit also changed
parentheses inside two display equations to dollar delimiters. The primary
source notes, exact diagnostic JSON and book TeX fragments preserve the
correct formulas. This addendum supplies the readable equations without
rewriting the already exported and published audit.

For the unit disk, with the source operator, the common-boundary family is

$$
h_\epsilon(s)=-(1-s+\epsilon)^\alpha+\epsilon^\alpha,\qquad
u_\epsilon=\psi+h_\epsilon,\qquad
\psi=s-2,\quad\alpha=\frac34,\quad\epsilon_j=\frac1j.
$$

Its mass and signed relative energy are

$$
\int_D H_1(u_\epsilon)=2+\frac32\epsilon^{-1/4},
$$

$$
E_\psi(u_\epsilon)
=2\int_0^1h_\epsilon(s)\,ds
-\alpha^2\int_0^1s(1-s+\epsilon)^{2\alpha-2}\,ds.
$$

The absolute energy bound remains 11/4, its exact limit remains -53/28,
and the total mass tends to positive infinity. The limit and canonical
truncation conclusions are unchanged. This is a formatting correction,
with zero additional primary-source reading credit and no theorem or
canonical problem status change.
