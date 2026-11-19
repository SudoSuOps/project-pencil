# Ledger schema and rules

The ledger is a JSON file. `scripts/pencil_ledger.py` validates it, does
the arithmetic, counts it, renders it, and compares runs. This file says
how to fill it in so that the same record always produces the same ledger.

## Contents

1. Division of labor
2. File structure
3. Decision table for state
4. Who checked
5. Keys (fixed vocabulary)
6. Profiles (required entries)
7. Alignments
8. Corrections and history
9. Commands
10. Human review gate

---

## 1. Division of labor

| Step | Done by |
|---|---|
| Read the documents and statements; extract what each one states; cite it | The model |
| Assign a state using the decision table | The model, by rule |
| Check the ledger is well-formed and breaks no rule | Code |
| Day counts, differences, cures, totals, ratios, counts | Code |
| Render the ledger | Code |
| Approve release | A human |

The model never does arithmetic in its head, never words a cure itself, and
never decides a close call by feel. If the decision table does not settle
an entry, the state is UNKNOWN.

## 2. File structure

A complete example is in `assets/example-ledger.json`.

```json
{
  "schema": "pencil-ledger/0.5",
  "subject": "the property",
  "owner": "the commissioning party",
  "recipients": [],
  "stage": "LOI submitted",
  "as_of": "YYYY-MM-DD",
  "profiles": ["loi"],
  "review": {"status": "DRAFT"},
  "entries": [],
  "alignments": []
}
```

Each entry:

```json
{
  "id": "E1",
  "key": "terms.closing",
  "object": "Closing date",
  "stated": {"value": "…", "by": "…", "source": "document, date, section"},
  "evidence": {"source": "…", "checked_by": "pencil", "checker": "Pencil", "seen_by_pencil": true},
  "state": "NOT_VERIFIED",
  "kind": "DOES_NOT_HOLD",
  "result": "one line: what the check showed",
  "needs": null,
  "supersedes": null
}
```

- `stated` is `null` only when nothing was stated (state UNKNOWN).
- `evidence` is `null` when nothing was checked.
- `kind` is set only for NOT_VERIFIED.
- `needs` is required for NOT_CHECKED and UNKNOWN: the fact that would
  settle it, and what that lets the parties decide.
- `omitted_from_documents: true` (optional) marks a material fact that came
  up outside the documents and that the documents do not address, such as
  an exchange the LOI never mentions. It is counted as a discovery.
- `result` states facts. The validator rejects hedges (probably, likely,
  appears, seems, typically), motive or judgment words (retrade, bad faith,
  leverage, shaky), and percentage odds.

## 3. Decision table for state

Apply the first row that fits. Do not weigh, average, or estimate.

| # | Situation | State | Kind |
|---|---|---|---|
| 1 | Nothing was stated or supplied about the object | UNKNOWN | — |
| 2 | Stated; no evidence examined, or the only evidence is relayed from a document Pencil has not seen | NOT_VERIFIED | NOT_CHECKED |
| 3 | Stated; evidence examined; evidence does not address the claim, or is ambiguous | NOT_VERIFIED | NOT_CHECKED |
| 4 | Stated; evidence examined; evidence conflicts with the claim | NOT_VERIFIED | DOES_NOT_HOLD |
| 5 | Stated; evidence examined; evidence matches the claim | VERIFIED | — |

"Matches" is exact: the same date, the same count, the same amount to the
precision stated. Close is not a match. A claim with several parts (a unit
mix, a rent schedule) is VERIFIED only if every part matches; otherwise row
4, with the parts that differ named in the result.

A relayed statement is not evidence. "The buyer says the lender needs 90
days" is row 2 for the lender's timeline.

## 4. Who checked

| `checked_by` | Use when | `seen_by_pencil` |
|---|---|---|
| `pencil` | The document's own text is in the conversation (attached, pasted, or quoted verbatim) and was read | must be `true` |
| `owner_of_fact` | The party who owns the fact stated it itself: its own letter, quoted verbatim, or its own words on a call the user reports directly | `true` if the words are in the conversation |
| `third_party` | A named party other than the requester (counsel, title) checked the document, as reported | `false` unless their written confirmation is in the conversation |
| `relayed` | The requester or anyone else read out or described a document that has not been supplied | must be `false`; state can only be NOT_VERIFIED / NOT_CHECKED |

**The relayed rule.** A figure, date, or term that someone reads out or
describes from a document Pencil has not seen is `relayed`. A relayed item
can never be VERIFIED and can never be marked DOES_NOT_HOLD. It is
NOT_VERIFIED / NOT_CHECKED, "as relayed by [name]", until the document
itself is supplied. The validator enforces this.

- Record what was relayed in `evidence` with `checked_by: "relayed"`,
  checker = the person who relayed it, `seen_by_pencil: false`.
- If the relayed figure differs from what was stated, say so in the result
  as a relayed difference ("As relayed, the rent roll shows 34 of 40
  suites; the OM states 96%"). Arithmetic on relayed figures may be shown,
  labeled as relayed. It is not a discovery and supports no cure.
- `needs` names the document to supply and what having it would let the
  parties decide.
- The same applies to the terms of an LOI, PSA, or letter that the user
  describes instead of pasting. Text pasted or quoted verbatim into the
  conversation has been seen; a description has not.

A party owns the facts about itself: a lender its timeline and conditions,
counsel its turnaround, a consultant its schedule. It does not own facts
about anyone else.

## 5. Keys (fixed vocabulary)

Use these keys so that the same object always has the same name. Add a
qualifier after a colon when there are two of something
(`cast.counsel_timeline:seller`). Use the `x.` prefix only when nothing
fits.

| Prefix | Keys |
|---|---|
| `property.` | ownership, title, survey, environmental, condition, unit_count, square_feet |
| `fin.` | unit_mix, occupancy, rent, other_income, expenses, taxes, insurance, noi, one_time_items, lease_terms, tenants, price_reduction |
| `party.` | buyer_identity, buyer_role, buyer_authority, buyer_funds, buyer_track_record, buyer_strategy, buyer_conditions, seller_identity, seller_authority, seller_consents, seller_conditions |
| `capital.` | source, lender_type, borrower, stage, terms, conditions, timeline, expiry, equity |
| `terms.` | price, diligence, deposit, deposit_hard, psa_delivery, closing, contingencies, extension, day_count, anchor, assignment |
| `cast.` | counsel_timeline, title_timeline, inspection_timeline, environmental_timeline, survey_timeline, calendar |
| `exchange.` | involved, leg, dependency, intermediary, deadlines, fit |

Which key for which fact:

- What the LOI or PSA says about a date or period → `terms.*`.
- How long a party says it needs → `capital.timeline` for the lender,
  `cast.*_timeline` for everyone else.
- Where a loan stands → `capital.stage`.
- Someone else's calendar (title, broker) → `cast.calendar:who`.

One entry per key. Do not split one claim across several entries or log the
same claim twice.

## 6. Profiles (required entries)

A profile is the fixed set of objects that must appear for a kind of work,
in whatever state the record supports. Declare it in `profiles`; the
validator enforces it.

| Profile | Use for | Required keys |
|---|---|---|
| `loi` | Vetting an LOI or PSA clock | terms.anchor, terms.day_count, terms.diligence, terms.deposit_hard, terms.psa_delivery, terms.closing, capital.stage, capital.timeline, party.buyer_funds, party.buyer_authority, exchange.involved |
| `financials` | Checking an OM and its numbers | fin.unit_mix, fin.occupancy, fin.rent, fin.lease_terms, fin.expenses, fin.noi |

If the deal is stated to be all cash, `capital.stage` and
`capital.timeline` still appear: state what was stated and its state.

Beyond the profile, add an entry only when a party stated something
material about that object. Do not add entries for things nobody raised.

## 7. Alignments

Create one alignment for every stated period that has a party's requirement
in days on record.

```json
{
  "id": "A1",
  "key": "terms.closing",
  "term": "Closing",
  "party": "Lender",
  "stated_days": 60,
  "stated_entry": "E1",
  "required_days": 120,
  "required_entry": "E2",
  "anchor_match": "SAME",
  "components": [
    {"name": "Diligence", "days": 30, "adjustable": false},
    {"name": "Close after diligence", "days": 30, "adjustable": true}
  ]
}
```

- `stated_days` and `required_days` are whole days counted from each
  period's own starting event.
- `required_days` is a requirement only when the party says it needs that
  long ("requires", "needs", "takes us", "no sooner than"). An outer figure
  ("within 105 days", "up to", "anticipate by") is not a requirement: the
  party might be faster. Log the alignment with the figure given, leave the
  entry for the stated term at NOT_CHECKED, mark the requirement entry's
  result as an outer figure, and make the next verification the question
  "how many days do you need, counted from [the stated term's event]?"
- `anchor_match`: `SAME` only when both documents name the same starting
  event in the same words or by the same defined term. `DIFFERENT` when
  they name different events. Otherwise `UNKNOWN`.
- `components` break the stated period into its parts. Mark `adjustable:
  true` only on the part the requirement bears on (the closing period when
  the lender's time is the issue). Everything else stays as stated.

The script then decides, by arithmetic:

| Requirement verified? | Anchors | Stated vs. required | Status | Cure |
|---|---|---|---|---|
| No | any | short | NOT_ALIGNED_AS_STATED | none; verify first |
| Yes | DIFFERENT | any | ANCHORS_DIFFER | none |
| Yes | SAME or UNKNOWN | short | NOT_ALIGNED | exact figure; UNKNOWN adds a note for counsel |
| Yes | SAME or UNKNOWN | equal or longer | ALIGNED | none |

A cure is the required figure exactly, with the non-adjustable parts
unchanged. The script cannot add cushion. Copy its cure text as printed.

## 8. Corrections and history

Entries are never edited or deleted after a ledger has been issued. To
correct one, add a new entry with a new id and `supersedes` set to the old
id. Both stay in the file; counts and rendering use the latest. `export`
writes every entry as a hash-chained line for an append-only store.

## 9. Commands

Keep each ledger in the working directory for its subject, in its own file
named for the subject (for example `ledger-100-sample-way.json`). Never
write a ledger inside the skill folder, and never reuse another subject's
file. Call the script by its path in the skill folder.

```
python3 scripts/pencil_ledger.py validate ledger.json    # rules; must print VALID
python3 scripts/pencil_ledger.py render   ledger.json    # the brief ledger, as Markdown (default)
python3 scripts/pencil_ledger.py render   ledger.json --full   # every entry, in tables
python3 scripts/pencil_ledger.py check    ledger.json response.md   # the response carries this ledger's render unchanged
python3 scripts/pencil_ledger.py align    ledger.json    # alignment results as JSON
python3 scripts/pencil_ledger.py count    ledger.json
python3 scripts/pencil_ledger.py hash     ledger.json
python3 scripts/pencil_ledger.py export   ledger.json    # hash-chained JSONL
python3 scripts/pencil_ledger.py drift    a.json b.json c.json
python3 scripts/pencil_ledger.py review   ledger.json --reviewer NAME --date YYYY-MM-DD
python3 scripts/pencil_ledger.py calc add-days 2026-06-01 45
python3 scripts/pencil_ledger.py calc days-between 2026-06-01 2026-08-15
python3 scripts/pencil_ledger.py calc ratio 1240000 18500000
python3 scripts/pencil_ledger.py calc sum-products "24*1450" "24*1850"
```

`render`, `check`, `align`, `count`, `hash`, and `export` refuse an invalid ledger.
Fix every error the validator reports; do not work around one.

## 10. Human review gate

Every ledger starts as `DRAFT` and renders with "Not reviewed by a human.
Not for release." Only the `review` command sets `REVIEWED`, and only with
a named reviewer and a date. Run it only when the human reviewer says they
have reviewed this ledger and gives their name. Never run it on your own
initiative, and never type `REVIEWED` into the file by hand.

The review is tied to the ledger's content by hash. Any change after
review makes the ledger invalid until it is set back to DRAFT and reviewed
again.
