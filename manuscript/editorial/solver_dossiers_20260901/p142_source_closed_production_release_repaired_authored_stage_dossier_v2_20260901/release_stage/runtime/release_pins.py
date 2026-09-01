"""Immutable release pins for the v3.3.3-r5-p142-source-closed-lf-v2 bundle.

This module is part of the trusted runtime code, not a mutable release
manifest.  Both the host service and the MCP independently bind the
canonical pinset digest below before accepting any source bytes.
"""

from __future__ import annotations

import hashlib
import json
from types import MappingProxyType
from typing import Final, Mapping


RELEASE_PINSET_FORMAT: Final = "rethlas-fixed-source-release-pins-v1"
RELEASE_PINSET_SHA256: Final = (
    "0412636c6dee5af057f0093075d85de96809719eb55c185b9409c5b71996decf"
)

_FIXED_SOURCE_RUNTIME_PATHS = {
    "bmps_2603_08664": "sources/bmps_2603.08664.txt",
    "cld_1204_6277": "sources/cld_1204.6277.txt",
    "dxz_2302_02541v3": "sources/dxz_2302.02541v3.txt",
    "ducros_aif_2009": "sources/AIF_2009__59_4_1443_0.txt",
    "berman_0710_4375v2": "sources/berman_0710.4375v2.txt",
    "bc_0911_2923v1": "sources/bc_0911.2923v1.txt",
    "gk_1406_7637": "sources/gk_1406.7637.txt",
    "gk_1509_09079": "sources/gk_1509.09079.txt",
    "stacks_0AY8": "sources/stacks_0AY8.html",
    "stacks_0BXQ": "sources/stacks_0BXQ.html",
    "stacks_01PR": "sources/stacks_01PR.html",
    "stacks_02O1": "sources/stacks_02O1.html",
    "gz_1403_7247": "sources/gz_1403_7247.txt",
    "boucksom_l2": "sources/boucksom_l2.txt",
    "begz_0812_3674v2": "sources/begz_0812_3674v2.txt",
    "bt82_new_capacity": "sources/bt82_new_capacity.txt",
    "km_1102_5596": "sources/km_1102_5596.txt",
    "p148_ch51_dependency_v3": "sources/p148_ch51_dependency_v3.txt",
    "mp_2409_06221v2": "sources/mp_2409.06221v2.txt",
    "darvas_xia_2003_04818": "sources/darvas_xia_2003.04818.txt",
    "del_math0002035": "sources/demailly_ein_lazarsfeld_math0002035.txt",
    "xia_2312_17150v3": "sources/xia_2312.17150v3.txt",
}

_SOURCE_BUNDLE_PINS = {
    "sources/AIF_2009__59_4_1443_0.pdf": {
        "bytes": 1090874,
        "sha256": "bfa8c478551c0e15e43fe5cfeb99211d35ec144ddb1c39b31a73ed2613aa05f0",
    },
    "sources/AIF_2009__59_4_1443_0.txt": {
        "bytes": 309747,
        "sha256": "180642ff21eaec9a16b4eeeb88b96efb127e007acec69057aaa1896e1bc0914a",
    },
    "sources/bmps_2603.08664.pdf": {
        "bytes": 774717,
        "sha256": "5cf7e68ee9113f1dc813f9aefa5f9ca72cba02fc4fa688f1a61e4b7f0d1223e7",
    },
    "sources/bmps_2603.08664.txt": {
        "bytes": 231469,
        "sha256": "f53dbe010f5ce481ebb4ee4954be0aa148729313d68c3fb79c34af1bc6873fea",
    },
    "sources/bc_0911.2923v1.pdf": {
        "bytes": 238010,
        "sha256": "1dca3f1a575a97e98e5fd5dd78063c1d84f61c377ea8c5fef3ba5afc50e6d027",
    },
    "sources/bc_0911.2923v1.txt": {
        "bytes": 69671,
        "sha256": "1d7dfef7bd658066848109de54fb438af00f3403221f2490e7df2e393ce2075e",
    },
    "sources/berman_0710.4375v2.pdf": {
        "bytes": 490866,
        "sha256": "6b1d6a1f595a9353d928d26c13c417fd560d1c63e248d054e4ac5de03d3af7c0",
    },
    "sources/berman_0710.4375v2.txt": {
        "bytes": 117136,
        "sha256": "f2edcf529dce1fb39a711f3e2f56bc942952d75df483835d624de75486e4f53f",
    },
    "sources/cld_1204.6277.pdf": {
        "bytes": 4659053,
        "sha256": "5690f999523017d184ab751bb55857ab1637b197d1186ad4fd2edba7e1bda719",
    },
    "sources/cld_1204.6277.txt": {
        "bytes": 2150944,
        "sha256": "021be260392de1f3240858d4c775da86653518dfab4fd9c4c21a2406081b6c7e",
    },
    "sources/dxz_2302.02541v3.pdf": {
        "bytes": 534767,
        "sha256": "7fede7c413e396008217a4a4c9638776dbdd7cacff90fdd463bf5ae48220246c",
    },
    "sources/dxz_2302.02541v3.txt": {
        "bytes": 141746,
        "sha256": "3234b3366d4aa4e235c5d2581cb131c68b95cdb0b386622302b4707930ea57f9",
    },
    "sources/gk_1406.7637.pdf": {
        "bytes": 1066195,
        "sha256": "62c7e4dfebab75d725f529c6ef78c300856c63fd050a9399e8a86879e569315d",
    },
    "sources/gk_1406.7637.txt": {
        "bytes": 311700,
        "sha256": "be0b9b4afc76b71d652772de6d6e720fe1620149b9470ed903a1de3cb3b470e6",
    },
    "sources/gk_1509.09079.pdf": {
        "bytes": 446717,
        "sha256": "36ce3e8bb8758eb67af4320dd4e23bf65297fb80abea64ce87a160683b300dbd",
    },
    "sources/gk_1509.09079.txt": {
        "bytes": 126873,
        "sha256": "3ce89f11fed97fadd6199a2a1fa6a5be0e34f7c878615a18ea6db4ddfd02e4d5",
    },
    "sources/stacks_01PR.html": {
        "bytes": 48192,
        "sha256": "10e5729facc1f46a826ad3adad02c107aa2d7aec3f87b7650122c46c5d9a59c1",
    },
    "sources/stacks_02O1.html": {
        "bytes": 14863,
        "sha256": "95b2a9b89f899192d71a6ced00b482b5901ab512daa9a63d7d568e424c7adfcb",
    },
    "sources/stacks_0AY8.html": {
        "bytes": 15046,
        "sha256": "b5d4fecb3d75b8f51b93e134bcaafabf3d47810370ad356e79de23907de18d75",
    },
    "sources/stacks_0BXQ.html": {
        "bytes": 25115,
        "sha256": "7fc401b609392d9dc1bf78bdd534a1dc0bf40fcbe6ddc2d97d15795a5b191737",
    },
    "sources/begz_0812_3674v2.pdf": {
        "bytes": 414218,
        "sha256": "43097be8459edfd948929fade34367fa7bbd0fe691d9cba1a4f27a11181214cd",
    },
    "sources/begz_0812_3674v2.txt": {
        "bytes": 163107,
        "sha256": "890173e309165984432e7326d13b7e096662cc805fbc19045a297f12211254c7",
    },
    "sources/boucksom_l2.pdf": {
        "bytes": 552046,
        "sha256": "5e3b9441461c6eab35f546c35087cdec0dd146daa84460a00058750eb5cd0909",
    },
    "sources/boucksom_l2.txt": {
        "bytes": 147498,
        "sha256": "4a3fa01a21b1cc66fe174460732fe80a29914f26279c04d2824223fc7d9ab0a4",
    },
    "sources/bt82_new_capacity.pdf": {
        "bytes": 1560096,
        "sha256": "e75ea91e48c14a9838a800aee25b68ed04169c4372f2ce4b399967b53005b758",
    },
    "sources/bt82_new_capacity.txt": {
        "bytes": 83498,
        "sha256": "716a2e1012a35ab6811873bc9f84d981627b7d6f4d9e6e4c8d48b0b525460d8b",
    },
    "sources/gz_1403_7247.pdf": {
        "bytes": 351472,
        "sha256": "13abbf7960f8c3619f040e28aed9d1e63dac854ab5e92fdf37db3df734ef88aa",
    },
    "sources/gz_1403_7247.txt": {
        "bytes": 104796,
        "sha256": "27b2cde510c3204fe672de367119644dd917f0abe0487af256d43db4a5287f10",
    },
    "sources/km_1102_5596.pdf": {
        "bytes": 194428,
        "sha256": "56f18ebf925b06d8b29fac3388c9be42dfe23d5365b3f10d12ff8f7088319f1e",
    },
    "sources/km_1102_5596.txt": {
        "bytes": 48316,
        "sha256": "fd59393dbbd2c98820bf217b5bd94ec1b786e125c7fa53b00900d56f6bc19cf7",
    },
    "sources/p148_ch51_dependency_v3.txt": {
        "bytes": 34444,
        "sha256": "c2404ea689ed09cf80fb8059145bc74bab123fd39c7e1d3b70f2f37b4c484fce",
    },
    "sources/mp_2409.06221v2.pdf": {
        "bytes": 843381,
        "sha256": "9eb2ea7686a5962ebc11c5eacd23b0cb3dcb081e27ac48292933f291fc82cb23",
    },
    "sources/mp_2409.06221v2.txt": {
        "bytes": 209777,
        "sha256": "724926d161cb3744dd5037e259f098a944a072419176bdc3e02538a657e5c59d",
    },
    "sources/darvas_xia_2003.04818.pdf": {
        "bytes": 1201940,
        "sha256": "a09dc667342b2ffb75ff55de9660c97f4d6238245f3e23ed3992cb2dfab79b61",
    },
    "sources/darvas_xia_2003.04818.txt": {
        "bytes": 182600,
        "sha256": "794c9e34736334b6ba2ff01a257a916b619e9036cb02e2a2e160c494e6c358ed",
    },
    "sources/demailly_ein_lazarsfeld_math0002035.pdf": {
        "bytes": 262219,
        "sha256": "59219defe8729b2cd8db7e05cabec3736832e3bfd5aad4ac1b58390c801337a2",
    },
    "sources/demailly_ein_lazarsfeld_math0002035.txt": {
        "bytes": 61147,
        "sha256": "0ae95d36227cc357a45b42336fdc1c28588be7163d25e160ba9e5a47bf8e81a3",
    },
    "sources/xia_2312.17150v3.pdf": {
        "bytes": 296408,
        "sha256": "773eea71af9f1fff112bf5fcab2b9046b81467df2e37165ee1da3949ff74c6d9",
    },
    "sources/xia_2312.17150v3.txt": {
        "bytes": 73722,
        "sha256": "a39c27332e746fa7f711718542658b1a0cfc526b8922f6f220e159089ac9562d",
    },
}

_TARGET_BUNDLE_PINS = {
    "target/STATEMENT.tex": {
        "bytes": 3518,
        "sha256": "cc3f5fbdc8f4a491ca6121c0c254a20f05a0bfb6da5d91f11d6ae6e406a40bc2",
    },
    "target/PROOF.tex": {
        "bytes": 7938,
        "sha256": "7f2ff066d1213107e5e4e4d6e3653016be3b0b5959205f689fa9131ae16a3dac",
    },
    "target/EXAMPLE.tex": {
        "bytes": 1460,
        "sha256": "7010c2a461de6f2ed1fb7c1f0170c6eaa8aed38b88492ea919f8b0c1eea49f6f",
    },
}

_P142_SOURCE_LOCATORS = {
    "mp_2409_06221v2": (
        (413, 423, "Definition 1.3.1: tropical spectrum of coherent ideals, extended values, and pointwise topology"),
    ),
    "dxz_2302_02541v3": (
        (437, 458, "decreasing relative test curves, finite endpoint, and interior I-maximality"),
        (848, 880, "formula (28): transition map between I-model test-curve components and its pseudoeffective scope"),
        (873, 925, "Definition 3.3: pseudoeffective inverse system, common endpoint, and transition I-envelopes"),
    ),
    "darvas_xia_2003_04818": (
        (1055, 1185, "compact Kähler pseudoeffective setting, Definition 2.12, and Proposition 2.18(ii)"),
    ),
    "del_math0002035": (
        (596, 613, "Theorem 2.6(ii): analytic subadditivity of multiplier ideals"),
    ),
    "xia_2312_17150v3": (
        (628, 647, "formula (3.8): raw multiplier-ideal transform and projective comparison"),
    ),
}

FIXED_SOURCE_RUNTIME_PATHS: Final[Mapping[str, str]] = MappingProxyType(
    _FIXED_SOURCE_RUNTIME_PATHS
)
SOURCE_BUNDLE_PINS: Final[Mapping[str, Mapping[str, int | str]]] = MappingProxyType(
    {
        relative: MappingProxyType(dict(pin))
        for relative, pin in _SOURCE_BUNDLE_PINS.items()
    }
)
TARGET_BUNDLE_PINS: Final[Mapping[str, Mapping[str, int | str]]] = MappingProxyType(
    {
        relative: MappingProxyType(dict(pin))
        for relative, pin in _TARGET_BUNDLE_PINS.items()
    }
)
P142_SOURCE_LOCATORS: Final[Mapping[str, tuple[tuple[int, int, str], ...]]] = (
    MappingProxyType(dict(_P142_SOURCE_LOCATORS))
)


def canonical_pinset_payload() -> dict[str, object]:
    return {
        "format": RELEASE_PINSET_FORMAT,
        "fixed_source_runtime_paths": dict(FIXED_SOURCE_RUNTIME_PATHS),
        "source_bundle_pins": {
            relative: dict(pin) for relative, pin in SOURCE_BUNDLE_PINS.items()
        },
        "target_bundle_pins": {
            relative: dict(pin) for relative, pin in TARGET_BUNDLE_PINS.items()
        },
        "p142_source_locators": {
            source_id: [list(locator) for locator in locators]
            for source_id, locators in P142_SOURCE_LOCATORS.items()
        },
    }


def canonical_pinset_sha256() -> str:
    encoded = json.dumps(
        canonical_pinset_payload(),
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=False,
    ).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


if canonical_pinset_sha256() != RELEASE_PINSET_SHA256:
    raise RuntimeError("release pin constants do not match their immutable digest")
