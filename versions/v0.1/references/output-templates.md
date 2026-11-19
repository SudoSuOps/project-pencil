# Output templates

Use the template that fits the request. Combine sections when useful. Drop a
section only when it has nothing to say, and never fill a section with
unsupported content to make it look complete.

## Contents

1. DEAL COLOR
2. REASON FOR MY CALL
3. DOES IT PENCIL?
4. AFTER THE CALL
5. Work record
6. Correction entry
7. Versioned change proposal
8. Worked sample

---

## 1. DEAL COLOR

```markdown
# DEAL COLOR — [party or deal name]
Audience: … | Decision: … | Stage: … | Disclosure scope: … | Decider: …

## Who and why
- [Role] [Name/entity] — [what they are doing here] — TAG [citation]

## Authority
- Who can sign: … — TAG
- Who takes title: … — TAG

## Capital
- Equity source: … — TAG
- Debt source and stage: … — TAG

## Timing and dependencies
- …

## Supported facts
- VERIFIED: … [citation]

## Material gaps
- UNKNOWN / REPORTED items that could change the next move

## Next evidence to request
1. …

## Questions (up to three)
1. …

Work record: …
```

## 2. REASON FOR MY CALL

```markdown
# REASON FOR MY CALL — [who is being called]
Audience: …
Purpose: …
Call type: Exploratory | Mandate-backed (state the evidence for a mandate)
Permitted disclosure: … | Not to be disclosed: …

## Color behind the call
- Verified: … [source]
- Unresolved material facts: …
- Relevant strengths: …
- Material weaknesses: …

## Opening
"Ring ring. [Name], [caller] with [firm]. Reason for my call: …"

## Two questions worth asking
1. …
2. …

## Do not imply
- [buyer / mandate / offer / funding source / financing approval / market
  fact / seller motivation or willingness / established relationship] — not
  supported by the record

## Sources
- [Document or call note, date, locator]

## Post-call findings
(Fill in after the call, or use AFTER THE CALL.)
- Statement — speaker — REPORTED — verification task

Work record: …
```

Keep the opening to what the record supports. An honest exploratory opening
("I'm calling to learn whether…") is a complete deliverable.

## 3. DOES IT PENCIL?

```markdown
# DOES IT PENCIL? — [deal]
Audience: … | Decision due: … | Decider: …

## Status
Examination: [DEFENDABLE — EXAMINATION | INSUFFICIENT EVIDENCE] — why
Execution readiness: [DEFENDABLE WITH CONDITIONS | NOT YET DEFENDABLE —
EXECUTION | not examined] — why

## Underwriting result
[Pencils / does not pencil / open] on [actual | normalized | pro forma]
assumptions. One or two sentences.

## Execution assessment
Separate from underwriting. State of capital, clock, and exceptions.

## The math
Metric | Formula | Inputs (with source) | Result
What moves the answer: …
Open metrics: …

## Capital vs. clock
Capital stage: … [evidence]
Clock map: milestone | date | source | status
Gaps: …

## Material exceptions
Exception | Severity and why | Evidence | Impact | Owner | Dependency |
Deadline | Possible cure | Cost/time | Disclosure state

## Decision due
What the authorized human has to decide, by when, and what is needed first.

## Validation — Self-check (same session)
Passed: … | Failed: … | Unchecked: …

Work record: …
```

## 4. AFTER THE CALL

```markdown
# AFTER THE CALL — [counterparty], [date]

## Attributed statements
- [Speaker] said: "…" / paraphrase — VERIFIED as said; assertion REPORTED

## Changes to the deal record
- [Field]: was … → now … (TAG) — source of change: [speaker, date]

## New exceptions
- … (add to the exception ledger)

## Verification tasks
- [Claim] — evidence needed — owner — due

## Next action
- … — owner — date
```

## 5. Work record

One line or a five-row list at the end of every substantive brief:

```
Evidence checked: … | Calculations run: … | What changed: … | Open checks: … | Next action and owner: …
```

Only work actually performed. Use "none" where nothing was done.

## 6. Correction entry

```markdown
### PENCIL CORRECTION — [YYYY-MM-DD] — [deal]
Original finding: …
Correction (Smash): …
Basis: [evidence with citation] or [practitioner judgment]
Effect on output: before … → after …
Effect on decision or call: …
Classification: Deal-specific | Proposed rule (pending approval)

Proposed rule (if any): …
Proposed test: Input … | Expected … | Fail if …
Status: Awaiting approval
```

## 7. Versioned change proposal

Produce only when asked.

```markdown
# pencil — change proposal v[current] → v[next]
Date: …

## Approved corrections included
| # | Date | Rule | Approved by |

## Proposed edits
| File | Section | Current text | Proposed text |

## Regression tests
New fixtures in `evals.md` format, plus the existing fixtures to re-run.

## Not included
Corrections still deal-specific or awaiting approval.
```

The user applies the change. PencilBot does not rewrite the skill itself.

---

## 8. Worked sample

Fixture 5 from `evals.md`. All facts below are fixture facts supplied in the
prompt, not real deal data.

Prompt: "Buyer came back after diligence asking for $2.5M off. We have their
roof bid at $410K and the HVAC replacement estimate at $190K. Does the ask
hold up?"

```markdown
# DOES IT PENCIL? — Price reduction request
Audience: Seller's broker | Decision due: response to buyer's ask (deadline
UNKNOWN) | Decider: seller

## Status
Examination: INSUFFICIENT EVIDENCE — the $600K rests on documents described
but not supplied, and the $1.9M balance has no support in the record.
Execution readiness: not examined (capital and clock were outside this
request).

## Execution assessment
The buyer's ask is larger than the costs documented so far. $600,000 of the
$2,500,000 is supported by supplied estimates. $1,900,000 (76% of the ask)
has no support in the record.

## The math
| Line | Amount | Source | Tag |
|---|---|---|---|
| Ask | $2,500,000 | Buyer request, as relayed by user | REPORTED |
| Roof | $410,000 | Roof bid, as described by user | REPORTED (bid not supplied for review) |
| HVAC | $190,000 | HVAC estimate, as described by user | REPORTED (estimate not supplied for review) |
| Documented costs | $600,000 | $410,000 + $190,000 | |
| Modeled exposure | none | No model supplied | |
| Remaining to explain | $1,900,000 | $2,500,000 − $600,000 | |

Share of ask documented: 24%. Share unexplained: 76%.

## Material exceptions
| Exception | Evidence | Impact | Owner | Possible cure |
|---|---|---|---|---|
| $1.9M of the ask is unsupported | No bid, report, or model for it in the record | Price | Buyer to support; seller to decide | Request itemization and backup for the balance |
| Bids not yet reviewed | User described them; documents not supplied | The $600K is itself REPORTED | User | Supply both documents so scope and totals can be checked |
| Response deadline unknown | Not stated | Clock | User / counsel | Confirm where the request sits against the diligence and deposit dates in the PSA |

Why the buyer is asking for the remaining $1.9M is not in the record. No
motive is assigned.

## Decision due
Seller decides whether to grant, counter, or decline. Before that: ask the
buyer to itemize the balance, and confirm the contractual deadline.

## Validation — Self-check (same session)
Passed: $410,000 + $190,000 = $600,000; $2,500,000 − $600,000 = $1,900,000;
600 / 2,500 = 24%.
Unchecked: bid contents, scope overlap between roof and HVAC, PSA dates.

Work record: Evidence checked: none (figures taken from user's message) |
Calculations run: documented total, remaining to explain, shares of ask |
What changed: n/a (first pass) | Open checks: bid documents, PSA clock,
buyer's support for balance | Next action and owner: request itemized
backup from buyer — seller's broker
```
