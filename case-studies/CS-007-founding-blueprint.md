# CS-007 — The founding blueprint against the build

**Date:** 2026-11-19 · **Evidence:** `FOUNDING_BLUEPRINT.md`; no test
runs.

## What happened

Smash wrote the Founding Blueprint from the day's work and adopted it as
the project's founding document. This case study records where the build
stood against it on the day it was adopted.

## Where the build already matched

| Blueprint | Built |
|---|---|
| No broker, no negotiation, no value, no decision | Rulings 11 to 13 |
| Human makes the call; Pencil prepares the questions | The Ring ring call sheet |
| Calculations re-run in deterministic code | The ledger script |
| History never overwritten | Superseded entries are kept |
| Human sign-off before publication | The draft gate and review stamp |
| No silent conversion of assumption into fact | The relayed rule; the validator's hedge check |
| No unsupported claim that a model is drift-free | CS-005 reports drift on four of six cases |
| Passport publisher | The `ledger.pencil` site, as a first cut |

## Where the blueprint and the skill disagree

Held open in `DOCTRINE.md` as questions 9 to 11:

1. **Status words**: Supported / Contradicted / Unresolved against
   Verified / Not verified / Unknown.
2. **Cures**: the exact arithmetic cure of ruling 20 against "does not
   propose concessions".
3. **Arithmetic on an assumed input** shown in the Passport against the
   skill's rule that a what-if never enters the ledger.

## What the blueprint asks for that was not built

- A source inventory: each original stored with an ID, a hash, the capture
  time and who supplied it.
- Authority and custody layers for each claim.
- Source spans: extracted values pointing to a page, line or record.
- The exception log and follow-up queue as their own parts of the
  Passport.
- Human override with a recorded reason and the prior version kept.
- A core identity separated from domain packs. The skill is CRE
  throughout.
- Evaluation metrics for citation accuracy and unauthorized disclosure.

## Position on the blueprint's phases

Partway through Phase 0, with pieces of Phase 1. The identity, the allowed
and disallowed actions, the status rules and a working validator exist.
The claim schema is not frozen, there is no store for original documents,
and nothing has run on a real controlled document set.

## Next

Rule on questions 9 to 11, then freeze the claim schema with the source
inventory in it. The rest of the blueprint depends on that schema.
