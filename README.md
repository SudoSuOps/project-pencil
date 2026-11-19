# Project Pencil

Pencil is a neutral third-party validator for commercial real estate
transactions. It keeps a defendable ledger of the transactional objects
tied to a subject property and marks each one **verified**, **not
verified**, or **unknown**. The parties make their own decisions from that
ledger.

Pencil does not prospect, represent a side, set value, or negotiate terms.

This repository is the project record: the skill, every earlier version,
the case studies from each test round, and the raw evidence behind them.

**Status: in development. Not released.** The current skill is v0.5 (in
development). Its newest rule has not been tested yet. See
[case-studies/](case-studies/README.md).

## Layout

| Path | What it holds |
|---|---|
| `skill/pencil/` | The current skill (v0.5, in development): `SKILL.md`, reference files, the ledger script, an example ledger |
| `versions/` | Snapshots of v0.1, v0.2, v0.3 (reconstructed), and v0.4 |
| `DOCTRINE.md` | The rulings that define what Pencil is, in the order they were made, and the questions still open |
| `case-studies/` | One write-up per test round or design decision: what was tested, what happened, what changed |
| `evidence/` | Raw material for each round: every response, ledger file, grade, and timing |
| `tools/` | The rubric source that renders `references/evals.md` |

## How Pencil works (v0.5)

- **The model reads.** It extracts what each document states and cites it.
- **Code decides and computes.** `skill/pencil/scripts/pencil_ledger.py`
  validates the ledger against the rules, does the day counts, differences
  and cures, and renders the output. Same ledger file, same output.
- **A human releases.** Every ledger is a draft until a named person has
  reviewed it. A change after review voids the review.

A cure is offered only as exact arithmetic from a verified fact. Stated a
30-day diligence and 30-day close; lender verified at 120 days; the aligned
terms are 30-day diligence as stated, then a 90-day close. No cushion.

## Running the ledger script

```
python3 skill/pencil/scripts/pencil_ledger.py validate skill/pencil/assets/example-ledger.json
python3 skill/pencil/scripts/pencil_ledger.py render   skill/pencil/assets/example-ledger.json
```

Python 3, standard library only. Commands and the ledger format are in
`skill/pencil/references/ledger-schema.md`.

## Test data

Every case in this repository uses invented facts. No real deal, party, or
document appears here.
