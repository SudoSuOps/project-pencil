# Evidence

Raw material for each test round. Case studies in `../case-studies/` cite
these folders.

| Folder | Round | Layout |
|---|---|---|
| `round-1-v0.1-acceptance/` | CS-001 | `<case>/with_skill` (v0.1) and `<case>/without_skill` |
| `round-2-v0.2-three-way/` | CS-002 | `<case>/with_skill` (v0.2), `old_skill` (v0.1), `without_skill`, each with `run-1..3` |
| `round-3-v0.4-drift/` | CS-004 | `first-pass/` and `rerun-after-fixes/`, each `<case>/run-1..3` |
| `round-4-v0.4-vs-v0.3/` | CS-005 | `<case>/with_skill` (v0.4), `old_skill` (v0.3), each with `run-1..3` |

In each run folder:

- `response.md`: the response as written.
- `ledger.json`: the ledger file (v0.4 runs only).
- `grading.json`: the grade. `expectations` holds substantive checks and
  critical-failure checks; `format_checks` is separate.
- `timing.json`: tokens and duration.

Each case folder has `eval_metadata.json` with the prompt and the checks.
`results.json` holds one row per response. `blind-grading-map.json` maps
the neutral IDs the graders saw to version and run.

All case facts are invented. Some no-skill responses cite web sources they
looked up themselves; those figures are not part of any case.
