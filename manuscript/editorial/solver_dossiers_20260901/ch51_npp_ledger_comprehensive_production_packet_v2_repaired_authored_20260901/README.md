# Chapter 51 comprehensive nonpluripolar-ledger production packet v2

Status: **REPAIRED AUTHORED SOURCE-CLOSED PACKET — NOT INDEPENDENTLY
AUDITED, NOT SUBMITTED**.

The target bytes are the exact independently audited Chapter 51 v2 local and
ledger replacements.  BEGZ arXiv:0812.3674v2, Bedford–Taylor 1982, and DDNL
arXiv:1705.05796 are pinned as PDF/text pairs with exact line routes.  The
candidate itself has two exact fixed-source routes.  No runtime stage is
bundled or authorized by this packet.

Each raw `pdftotext -layout` derivative ended in a terminal form-feed without LF.
The bundled text deterministically appends exactly one LF after that
form-feed; `SOURCE_ROUTES.json` binds both the pre-normalization and bundled
hashes.  Lines are addressed one-based using byte `0x0a` as the only
separator; form-feed byte `0x0c` remains content within a line.  Every routed
range and the three critical source anchors have independent byte hashes.

Run `python3 -B check_packet.py` for a read-only check.  This dossier contains
no Rethlas receipt, no final-path smoke, no live edit, no inventory change,
and no git operation.  The independently rejected v1 packet/stage audit is
bundled as immutable repair provenance; its runtime-smoke blocker remains for
a separate repaired release stage.
