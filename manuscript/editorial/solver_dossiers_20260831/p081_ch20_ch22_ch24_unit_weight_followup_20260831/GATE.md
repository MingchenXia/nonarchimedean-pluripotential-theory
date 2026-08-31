# Unit-weight numerical examples and the weighted sign convention

31 August 2026. Isolated follow-up, not a live-book change.

The general Ch20 curve formula remains the residue-weighted formula in
the frozen parent `p081_ch20_weighted_intersection_repair_20260831`.
This follow-up fixes a different numerical example in that chapter and
its Ch22/Ch24 consumers: a single closed node does not imply intersection
degree one. The examples now explicitly choose a residue-rational node.
No general theorem is restricted to rational nodes. Their displayed
numbers, labels, and equation references remain unchanged.

The Ch24 sign audit now calls the general outgoing-slope sum
residue-degree-weighted. The two-vertex numerical example and its mixed
pairing consumer explicitly have unit residue weight. For a closed node
of residue degree c instead, the intersection matrix and the Dirichlet
quadratic form are multiplied by c; that is already the general Ch20
identity, not a new existence or envelope theorem.

Assembly starts with the exact frozen proposed Ch20 copy and the live
Ch22/Ch24 sources. Each replacement must match once, and the manifest
records both the live bases and the frozen input. The combined patch is
against the live book and includes the parent Ch20 correction. Do not
apply both Ch20 patches cumulatively: use the full proposed Ch20 here.

This packet does not repair Ch25 or certify all of Ch22/Ch24. It does not
change the active open-problem count, authorize integration, or replace
the independent and production verification gates. No PDF is produced.
