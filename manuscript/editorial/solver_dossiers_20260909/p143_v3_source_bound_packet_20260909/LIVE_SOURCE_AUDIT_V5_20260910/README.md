# P14.3 V5 current exact-live audit

This is a new local integrity audit.  It preserves the historical V4 audit
unchanged and binds the accepted conditional V3 packet to the current live
Chapter 71 theorem/corollary, Chapter 72 scope boundary, and inventory entry.

Run `python3 build_and_check.py` from this directory.  The audit resolves
source ranges from stable content anchors rather than inherited line numbers,
then verifies the current source hashes and the frozen final V3 receipt.  It
does not create a new verifier receipt, discharge P14.2, establish general MP
positivity, or retire P14.3.
