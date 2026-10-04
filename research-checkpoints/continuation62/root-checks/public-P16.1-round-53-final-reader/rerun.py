#!/usr/bin/env python3
"""Reproduce all artifact operations, preserving each driver's real output."""
import pathlib
import subprocess
import sys

root = pathlib.Path(__file__).resolve().parent
for script, stem in [('prepare_provenance.py','prepare-run'), ('build.py','build-run'), ('verify.py','verify-run')]:
    result = subprocess.run([sys.executable,script],cwd=root,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    (root/(stem+'.stdout.txt')).write_bytes(result.stdout)
    (root/(stem+'.stderr.txt')).write_bytes(result.stderr)
    print(f'{script}: exit {result.returncode}')
    if result.returncode:
        sys.exit(result.returncode)
