# Production Rethlas receipt: P21.3 componentwise rigid exceptions

Date: 29 August 2026

## Frozen candidate bytes

- Candidate statement SHA-256:
  `5b03b18f255625809a863c1079e9d84df146cb06a8c3b752ce08c58c700aeca8`
- Candidate proof SHA-256:
  `3893a89ffd59f7636a7ab160c4746fecd520b328281ac60f0bbd0401dd2d21e5`
- First independent exact-byte audit:
  `PASS`, report SHA-256
  `8c6fdee4b6edcfaaf11e7cb9d60d4712863530014adb14a50d094ec94e18f5ac`
- Second independent exact-byte audit:
  `PASS`, report SHA-256
  `e14e78696d099328f0eb5f662f1c380d968386aa1a80910709c6fd29633f81e4`

The production materialization prepended the exact transitive dependency
closure to these unchanged candidate bytes.  Its SHA-256 digests were:

- materialized statement:
  `2bf673687e935bcdae91550158344647cb1ca1cd4ae0a5040109aeb5fb2f3cbc`;
- materialized proof:
  `a27c40fbb1328b008acab07b871f50a778c34bab2b0f1d05e3a6d9d229839716`.

## Controlling production result

- Service-evidence run: `20260829T061505Z_2bf673687e93`
- Checked item: `pi_ee24d64b88f0c4e60ad1acbd`
- Model: `gpt-5.6-sol`
- Reasoning effort: `xhigh`
- Verification status: `final`
- Verdict: `correct`
- Critical errors: `0`
- Gaps: `0`
- Failed or blocked items: `0`
- Adaptive round: `0`
- Codex return code: `0`
- Service output validation: `validated`

The response proof digest is exactly the materialized proof SHA-256.  The
item-level service report states that the complete, untruncated proof was
checked and that its localization, virtual-annulus, current-classification,
zero-atom, normalization, nilreduction, and Bedford--Taylor arguments are
logically consistent with the stated hypotheses and supported by the cited
external results.  It records no critical error and no proof gap.

The direct HTTP wrapper reports no endpoint-assigned run identifier.  The
service-evidence directory name above is therefore the durable local archive
identifier; no absent identifier is inferred.

## Archived transport and service evidence

- `request.json`:
  `932d6a80311fa9428a648dce2b1b429bd45faa36df303ae0dae3f9d1ad13ff8a`
- `response.json`:
  `20169289938e2f1301caa119801dafc942e2385d7817aa65ad3a822d7708c192`
- `headers.json`:
  `a497241659aff504b186153415e79c19fe12656d43e9d8b6ffadc9ca282b8bff`
- `service_manifest.json`:
  `627817faf1cb897d22545c9fb2b3a1c1191e2ceb8e7ea358bd660fa00e5502f8`
- `service_verification.json`:
  `fc0257c2f8bfc830adab1b691735a0502258d2fa39e402edfcb7f1b16b4f44f1`
- `service_item_log.md`:
  `68c64ee73b639278871588a51e249b3982d25d2a853f497951bf83fcaaffd027`
- `service_item_verification.json`:
  `4d3ced0ffa31cbf9e7a4a6d50768093bc7ef026ceaeb12d8af18ab40186f4deb`
- `service_process_guard.json`:
  `3cf1165efe6b9e1fcdebe573c2c5b2d55dc43e147347e4ae72575024af1020b8`
- `service_process_child_guard.json`:
  `8c568785bed1ba76293d791374ef665a95b349ff160328e55872720d3381cc24`

## Noncontrolling rejected attempt

The earlier materialization with statement hash
`9e819244c341dab4fec3cbab94c7af05494accb4cb16bb961823850d88e88a4a`
and proof hash
`8ab5ea0344357961cd945f3c1b77e8d2004d6ff4a4f292d291e046054d9c72c1`
omitted the transitive canonical-collar bridge.  It returned final `wrong`,
one critical error, and zero gaps.  It is preserved in
`p213_componentwise_rigid_exceptions_rejected_missing_bridge_20260829/`
and is not controlling.  The successful materialization repaired only the
dependency closure: it did not change the candidate theorem or proof bytes.
