# CS-006 — The relayed rule

**Date:** 2026-11-19 · **Evidence:** none yet. This rule has not been
tested.

## The ruling

A figure, date, or term read to Pencil from a document it has not seen can
never be verified and can never be marked as not holding. It stays "not
checked, as relayed by [name]" until the document itself is supplied.
(DOCTRINE.md 25.)

## Why

In CS-005, all three v0.4 critical failures came from a looser rule: a
figure the user read aloud counted as the document's content, labeled "not
seen by Pencil". Under a black-and-white standard, the word "verified"
cannot sit on something Pencil has not seen.

## What changed (v0.5, in development)

- **Schema.** New evidence source `relayed`. Text pasted or quoted verbatim
  has been seen; a description has not.
- **Validator.** An entry whose evidence is relayed is rejected if its
  state is VERIFIED or its kind is DOES_NOT_HOLD.
- **Rendering.** Relayed evidence prints as "as relayed by [name];
  document not seen by Pencil".
- **Differences.** A relayed difference may be reported and its arithmetic
  shown, labeled as relayed. It is not a discovery and supports no cure.
- **Rubric.** The overstatement failure now names this case. Holdout H6
  (unit mix, OM against rent roll) was rewritten: with both documents
  relayed, nothing is verified and nothing is marked as not holding.

## Consequence to expect

Ledgers built from a conversation alone will show few verified entries.
That is the intended reading: Pencil needs the documents.

## Not yet decided

Two neighbouring cases are open (DOCTRINE.md, Open questions 1 and 2): a
third party's check that reaches Pencil only as the user's report, and a
verification call the caller reports afterwards. The skill currently lets
both count, labeled. Neither is covered by this ruling.

## To test

Run v0.5 on the six CS-005 cases, with H6 in its rewritten form, and
compare critical failures and drift against CS-005.
