> Historical implementation checkpoint: the follow-up below adds 21 individual 4414 revision studies, bringing the current note count to 348. Current counts are in `data/physical_upgrade_metrics.json` and the manifest.

# Physical evidence upgrade — 2026-11-07

Branch: `research/anchor-physical-evidence-upgrade`. Starting commit: `9accf749eb876706e114101e3ce47d04f841fc19`. Changes are local; no push or publication is authorized.

## Implementation

Seven source-bounded physical studies cover five anchors, separate original/rebuild 2910, and Team 27. They add 24 mechanism records, 20 explicit input/output contracts, 21 deterministic annotated views, five inspected Citrus CAD renders and one inspected Team RUSH overview thumbnail. The thumbnail is not a video frame or internal mechanism detail. Read the exact remaining gaps below.

Canonical research is in `data/physical_studies.jsonl` and `data/mechanism_interfaces.jsonl`. Detailed notes, parameters and source-image metadata remain authoritative under `data/`. Generated Markdown, context documents, normalized tables, research SQL, reader and agent outputs are rebuilt from them. The new build step is `scripts/build_physical_studies.py`, followed by `scripts/rebuild_database.py` and `scripts/build_agent_and_reader.py`.

The new `physical_mechanism` search kind returns construction, editorial operating sequence, whole-robot packaging, exact figure IDs, source notes and transfer limits together. `mechanism_interface` exposes unresolved spatial, velocity, electrical, control and service contracts. `compare-interfaces` rejects piece mismatches and prohibited historical hardware, and keeps unverified matches unresolved.

## Changed research files

- [Authoritative physical studies](../data/physical_studies.jsonl), [interface contracts](../data/mechanism_interfaces.jsonl), [coverage states](../data/evidence_coverage.jsonl), and [image audit](../data/image_evidence_audit.jsonl).
- [Original BLITZ](physical/physical-2026-2910-original.md) and [RE-BLITZ](physical/physical-2026-2910-rebuild.md), kept separate.
- [Limestone](physical/physical-2026-1678.md), [Doppler](physical/physical-2024-1690.md), [AURELIA](physical/physical-2025-1323.md), [Toploader](physical/physical-2026-604.md), and [Team RUSH partial reconstruction](physical/physical-2026-27.md).
- [Rebuild script](../scripts/build_physical_studies.py), [compatibility screening](../scripts/interface_compatibility.py), and [relationship / retrieval validation](../scripts/validate_physical_studies.py).
- [Measured retrieval examples](../data/physical_retrieval_examples.json), [cohort coverage](../data/cohort_coverage.jsonl), and [1323 investigations](../data/cohort_research_attempts.jsonl).

## Before / after

The figures below are rebuilt in `data/physical_upgrade_metrics.json`; the starting checkpoint is `data/physical_upgrade_baseline.json`.

| Metric | Before | After |
|---|---:|---:|
| Robot dossiers | 141 | 141 |
| Technical notes | 303 | 327 |
| Parameters | 136 | 159 |
| Robot-years with parameters | 34 | 37 |
| Source image associations | 569 | 575 |
| Editorial drawings | 0 | 21 |
| Dossiers without any image | 50 | 49 |
| Dossiers with exactly one technical note | 97 | 94 |
| Notes without explicit image links | 128 | 126 |
| New explicit mechanism coverage assessments | 0 | 24 |
| Structured interface ports | 0 | 20 |

Editorial drawings are counted separately from source evidence. A thumbnail does not establish internal construction. Descriptions in legacy dossiers remain available, but evidence dimensions are marked unassessed until explicitly reviewed.

## Consequential findings

- RE-BLITZ's apparent internal roller shapes include stationary backing supports after active rollers were removed. The team reports worse consistency/throughput with those extra contacts. The new physical study prevents copying them as extra powered feed stages.
- Citrus's later official page specifies a 3.5-inch aluminum drum; the retained interview account describes steel. Both source snapshots remain visible with an explicit unresolved revision conflict. Neither material is silently applied to the entire season.
- Citrus's mixed floor contacts use different diameters and reductions. Under the usual reduction convention, their nominal surface-speed factors agree (`1 / 1.5 = 2 / 3`). This is an analytical consistency check, not a measured fuel-speed or loaded-flow result.
- The AURELIA handoff now distinguishes donor detection from receiver capture, with team-reported Banner/CANdi locations. Receiving a sensor event does not establish the exact mechanical overlap or safe timeout.
- Toploader's bucket segmentation, removable battery-access panel and overhead turret support are coupled packaging choices. A fixed-launcher adaptation can borrow rotating capture but remains an unvalidated outlet/support redesign under 1833's no-turret constraint.

## Cohort integrity and research gaps

The original ranked cohort has 125 slots, of which 106 have provisional dossiers; all 19 exclusions were recomputed. Nineteen lower-ranked substitutions remain. Three 604 supplements and thirteen curated 2018/2019 studies retain separate labels. See `data/cohort_coverage.jsonl`.

New investigations of 2026–1323 and 2022–1323 are recorded in `data/cohort_research_attempts.jsonl`. Team season/media pages and public code discovery did not supply enough new primary construction detail to promote either slot into a dossier. Observer discussions and another team's imitation are leads, not proof of 1323 construction. This is a retrieval result, not a claim no publication exists.

## Specific missing interfaces

| Study | Missing evidence | Effect on future design |
|---|---|---|
| BLITZ original | Two-intake merge cross-section and support | Cannot claim a drop-in merge or certify simultaneous streams |
| RE-BLITZ | Exact feeder gap, loaded wall sweep and battery route | Width-preserving architecture is supported; fabrication dimensions remain conditional |
| Limestone | Full J-path section, hood-range compression and conflicting drum snapshot | Must inspect exact revision before selecting material or spacing |
| Doppler | Final deflector detail, moving note-contact overlap and battery service | Guard function and low architecture transfer; exact handoff/guard shape cannot be copied |
| AURELIA | Donor/receiver overlap, complete wire routing and suspended load geometry | Direct handoff and shared-joint climb require further assembly evidence |
| Toploader | Tube clearances, queue forces and fixed-outlet adaptation | Historical turret is ineligible; serializer transfer is conditional |
| Team RUSH | Internal inspected figures and compression definition | Thumbnail supports exterior only; internal drawing remains explicitly partial |

## Verification and retrieval examples

The research and agent SQLite databases passed integrity and foreign-key checks. The new validator passed 1,761 evidence/relationship/retrieval checks; the existing agent validator passed 24,229 checks (see current JSON for the exact count). Reader logic passed 34 checks. A real Chromium render was attempted but blocked by this runtime’s socket permission; browser layout is not claimed verified. The deterministic drawings were inspected as images. All 596 local images decode; external destination states are tracked separately, with untested links kept untested.

The Team 27 public video download attempt reached a sign-in/bot confirmation requirement and was stopped. No internal video frame was reviewed. The supplied overview thumbnail is explicitly distinguished from mechanism-detail evidence.


Checks and exact retrieval results are recorded in `PHYSICAL_UPGRADE_VALIDATION.json` and `data/physical_retrieval_examples.json`. Syntax and byte checks do not prove mechanical completeness or model quality.

Try these commands, then read the linked source figures and complete packets:

```sh
python scripts/query_agent.py search backing --robot 2026-2910 --kind physical_mechanism
python scripts/query_agent.py search floor --robot 2026-1678 --kind physical_mechanism
python scripts/query_agent.py search handoff --robot 2025-1323 --kind physical_mechanism
python scripts/query_agent.py search column --robot 2026-604 --kind physical_mechanism
python scripts/query_agent.py search restraint --robot 2026-27 --kind physical_mechanism
```

The next agent has richer connected evidence; its design quality has not been benchmarked. Push, merge or publication requires owner approval after review.

## 4414 revision follow-up

The original 21 labeled revision images were retained, but the five broad notes did not provide individual revision records. The binder mechanism gallery also truncated attached images after four. This made the history difficult to find and exposed only part of it in that view.

The fix adds ten rotor and eleven shooter records, each with its original image, a visible-construction account, a comparison to the previous gallery ordinal, a separate engineering interpretation and explicit unknowns. All 21 originals were inspected at their available resolution. The live team binder was checked through its last rotor and shooter slider values. Its gallery does not explain each revision's rationale or outcomes, so those are not invented.

[Read the revision history](2026-4414_REVISION_HISTORY.md), [authoritative records](../data/mechanism_revisions.jsonl), [known-label coverage audit](../data/revision_coverage.jsonl), and [validation](../REVISION_VALIDATION.json). Search `--kind mechanism_revision`, for example `RotorV10` or `ShooterV11`, then load the complete 2026–4414 packet. Rotor and shooter ordinals are independent; no automatic matched configuration or event installation is asserted.

The image cap is removed for every robot. The label audit also flags shared historical version figures for 2018–2898 and 2018–971, without claiming that their existing studies vanished or fabricating additional version interpretations.

Follow-up checks passed: individual revision retrieval and SQL relationships; all 596 pre-correction image byte hashes; all 327 prior technical-note IDs, 159 parameter IDs and 141 robot IDs; 35 reader logic checks; existing agent and physical checks. Browser verification of the public binder is distinct from the offline reader's logic checks. No push, merge or publication was performed.
