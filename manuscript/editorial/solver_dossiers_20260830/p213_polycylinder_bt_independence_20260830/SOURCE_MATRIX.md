# Source and dependency matrix

| Input | Exact use | Scope retained |
|---|---|---|
| Verified P06.2 v3 theorem `thm:p062-arbitrary-field-polycylinder-candidate` | A continuous zero-current function on a standard strict open polycylinder is `c + sum lambda_j log|S_j|`, hence ordinary CLD-smooth with zero smooth Hessian. | Complete nontrivially valued field; strict open standard discs and annuli only. |
| Frozen P06.2 v3 statement/proof SHA-256 `985be85d97b583f72be5cee65988df6f31c1edb49a685121b834df179fa87fda` / `42b592bf8ac26ed46c36928e5e90272225ae6883bd2bfe62d3ff2840f01d46e5` | Exact internal verified dependency. | No endpoint inference. |
| P06.2 v3 production response SHA-256 `c8c951075a574c6a3badde2e2a22942718616cd21da0144cb8a983bc3cac822f` | Production verdict `correct`, zero critical errors, zero gaps. | Dependency only; the present candidate has not been submitted. |
| Chambert--Loir--Ducros, Lemma 8.5.3, reproduced as `lem:ch16-leibniz-closed` and specialized in `cor:ch16-smooth-case` | For smooth `h` and a positive closed current `T`, `d'd''(hT)=d'd''h wedge T`. | Smooth multiplier; positive closed current. |
| Positivity/order-zero multiplication, reproduced as `lem:continuous-times-positive-current` | A continuous function may multiply a positive current, and the operation is linear. | No multiplication by an arbitrary distribution. |
| Sheaf property of CLD currents | Local zero identities glue on an ordinary open cover. | No extension across a boundary or deleted locus. |

No literature statement in the matrix asserts the new bridge in the exact
form printed here.  The candidate is a formal but nontrivial synthesis of
the production-verified P06.2 regularity theorem with the CLD current
Leibniz rule.  It carries no priority claim before independent verification
and literature comparison.

