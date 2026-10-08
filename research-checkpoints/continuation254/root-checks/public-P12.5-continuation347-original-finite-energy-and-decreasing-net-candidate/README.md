# Rerun

Run from this directory:

```sh
python prepare.py
python exact_diagnostics.py
python build_delivery.py
python final_audit.py
```

All helpers are newly owned. `prepare.py` reads only explicitly bound bytes and input.json, never supplied executable code. `build_delivery.py` uses local pandoc to generate **TeX source only**, with complete qualified grants embedded verbatim. No PDF compiler is run; ROOT retains compilation and acceptance. `final_audit.py` checks artifact/hash/support consistency, not mathematical correctness. Primary data stay LOCALONLY.

The final native-notes JSON has the whole proof bodies, summaries and explicit supports. Argument.md is the full new proof; P12.5-paper.tex is its standalone TeX with grant and ledger appendices. The first finite diagnostic failure is retained and explained in n9. The corrected finite arithmetic checks do not certify the universal mathematical claims.
