# Case studies

One write-up per test round or design decision, in order. Each says what
was tested, what happened, and what changed as a result. Raw material is in
`evidence/`.

| # | Case study | Date | Outcome |
|---|---|---|---|
| CS-001 | [First acceptance test of v0.1](CS-001-v0.1-acceptance.md) | 2026-11-19 | v0.1 passed its checks; answers ran long and boilerplate |
| CS-002 | [v0.2 against v0.1 and no skill](CS-002-v0.2-three-way.md) | 2026-11-19 | v0.2 had 1 critical error in 30 responses; v0.1 had 3; no skill had 20 |
| CS-003 | [Role correction: the neutral validator](CS-003-neutral-validator.md) | 2026-11-19 | Prospecting, advocacy and verdicts removed; ledger, alignment and exact cures added (v0.3) |
| CS-004 | [Rules, not judgment: first drift test](CS-004-rules-not-judgment.md) | 2026-11-19 | Ledger moved into code (v0.4); first drift test found four defects, all fixed |
| CS-005 | [v0.4 against v0.3](CS-005-v0.4-vs-v0.3.md) | 2026-11-19 | v0.4 did not beat v0.3 on behavior; drift clean on 2 of 6 cases |
| CS-006 | [The relayed rule](CS-006-relayed-rule.md) | 2026-11-19 | Ruling 25 written into the skill and validator (v0.5). Not yet tested |
| CS-007 | [The founding blueprint against the build](CS-007-founding-blueprint.md) | 2026-11-19 | Blueprint adopted; three conflicts with the skill held open; seven items not yet built |
| CS-008 | [The pain point: the unwind period and defendable mode](CS-008-the-unwind-period.md) | 2026-11-19 | The pain is the unwind before a deal, not broken contracts; rulings 38 to 40 recorded; sources for the headline numbers still open |

## How rounds are run

- Every run is a fresh session with no memory of this project.
- The skill under test is given without its `evals.md`, so the cases and
  expected results are not in view.
- From CS-002 on, responses are graded blind by a separate agent per case,
  under neutral IDs. The map from ID to version is in each round's
  `blind-grading-map.json`.
- Results are reported in separate tiers: critical failures, substantive
  checks, format checks, answer length, and (from CS-004) drift.
- All case facts are invented.

## Limits that apply to every round so far

- Graders are AI agents, one per case. No human has reviewed the grades.
- Three runs per case is a small sample.
- All runs used the same model.
