# CS-004 — Rules, not judgment: first drift test

**Date:** 2026-11-19 · **Evidence:** `evidence/round-3-v0.4-drift/`

## The ruling

Pencil does not think like a model and does not drift. It is black and
white, with grey as unknown; closer to math and immutable code. And a
human reviews the ledger before anything is submitted. (DOCTRINE.md 23,
24.)

## What that required

A skill is instructions to a model, and a model is not deterministic.
v0.3 asked for the behavior; it could not enforce it. v0.4 split the work:

- **The model reads**: extracts what each document states, cites it, and
  assigns a state by a five-row decision table.
- **Code decides and computes**: `scripts/pencil_ledger.py` validates the
  ledger, does every day count, difference, cure and count, and renders
  the output. It rejects a "verified" entry without evidence and a named
  checker, hedge words, motive words, percentage odds, and a missing
  required object. It cannot add cushion to a cure.
- **A human releases**: every ledger renders as a draft until a named
  reviewer signs it; the review is tied to the content by hash.

Corrections supersede entries and never delete them. An export command
writes hash-chained lines for an append-only store.

## The drift test

Three holdout cases, three fresh runs each. The script compares the
ledgers field by field: every entry's key and state, and every alignment's
days, difference, status and cure. Wording is ignored. Any difference is
drift.

| Case | First pass | After fixes |
|---|---|---|
| PSA delivery vs. counsel, plus a silent exchange | No drift | not re-run |
| Unit mix, OM vs. rent roll | No drift | not re-run |
| LOI clock vs. lender letter | Drift: one run logged two extra objects | No drift (3 runs) |

## Defects the test found

1. **Extra entries.** One run logged "anchor" and "day count" objects the
   others did not. Both became required for every LOI vetting.
2. **Contradictory rules.** The decision table said figures a user reads
   from a document are "not checked"; the worked sample treated them as
   checked. All three runs resolved it the same way, toward "checked, not
   seen by Pencil". That resolution was written into the schema. It was
   later overturned (CS-005, CS-006).
3. **Ledger and response came apart.** In two runs the response text did
   not match that run's ledger file, because parallel runs wrote to a
   shared file in the skill folder. Each ledger now lives in its own file
   per subject, and a `check` command confirms a response carries its
   ledger's render unchanged.
4. **The test case was wrong.** The lender letter said "within 105 days".
   Every run read that as an outer figure, not a requirement, and stated
   no cure. The rubric had expected a cure. The runs were right and the
   rubric was corrected.

## Limits

- Nine runs, plus three re-runs of one case.
- Drift comparison covers states, numbers and cures. The one-line result
  text in each entry is still written by the model.
