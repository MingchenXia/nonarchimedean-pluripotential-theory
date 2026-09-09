# P14.8 V7 exact-live integration audit packet

`build_packet.py` materializes this packet from exact source-line ranges at
the current Git revision and writes `RELEASE_PINS.json`.  The proof context
contains the frozen V6 target statement and all live source extracts required
for the limited comparison.  `SHA256SUMS` is an inventory and integrity
manifest for the packet after materialization.  The accepted V7 audit is a
source-and-boundary gate, not the required `gpt-5.6-sol` production gate.
