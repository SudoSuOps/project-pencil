# Output templates

Short forms are the default. Every response opens with finding, evidence,
next verification. Drop any section that has nothing to say. Write
neutrally: no recommendation on price, terms, or whether to proceed.

## Contents

1. Short forms: LEDGER, ALIGNMENT CHECK, PROFILE, RING RING, AFTER THE CALL
2. Full ledger report
3. Work record
4. Correction entry
5. Versioned change proposal
6. Worked samples

---

## 1. Short forms

### LEDGER

```markdown
**Finding:** Stated [X]. Verified [Y]. Result [Z].
**Evidence:** [what was checked, by whom]
**Next verification:** [one check] — [who can make it]

**Entries**
| Object | Stated (source) | Checked against | State | Result |
|---|---|---|---|---|

**Count:** [n] verified, [n] not verified ([n] not checked, [n] do not hold), [n] unknown. Discoveries open: [n].

Work record: …
```

For one or two entries, write them as lines instead of a table.

### ALIGNMENT CHECK

```markdown
**Finding:** [the term that does not align, with the difference in days]
**Evidence:** [stated term and source] vs. [verified fact and source]
**Next verification:** … — [who]

**Terms against the cast**
| Stated term (source) | Party | What the party says (source, state) | Difference |
|---|---|---|---|

**Discoveries**
Stated: … / Verified: … / Result: …

**Cure supported by the evidence**
Aligned terms on the verified facts: …
(or: No cure is supported yet. Needed: [fact].)

**For counsel to confirm**
- …

Work record: …
```

### PROFILE

```markdown
**Finding:** [what the process shows about this party's capacity for this deal]
**Evidence:** …
**Next verification:** … — [who]

| Object | Stated | Checked against | State |
|---|---|---|---|
| Entity and role | | | |
| Authority to sign | | | |
| Funds / capital stage | | | |
| Conditions | | | |
| Exchange involved? | | | |

Work record: …
```

### RING RING

```markdown
**Finding:** [n] entries cannot be settled from documents; [n] calls would settle them.
**Next verification:** [the first call] — [who makes it]

**Call 1 — [party]**
Authorization needed: [from whom] — [in hand / not yet]
Reason for the call: "Reason for my call: I'm verifying … stated in a letter of intent for [subject], at the request of [owner] and with [party]'s authorization."
Questions:
1. … → settles [entry]; lets the parties judge […]
2. …
May share: …

Work record: …
```

### AFTER THE CALL

```markdown
**Finding:** [what the call settled, and any discovery it produced]
**Next verification:** … — [who]

**Said** (speaker, date)
- …

**Ledger updates**
- [Object]: was [state/value] → now [state/value] — source: [speaker, date]

**Alignment re-run**
- [difference, discovery, or cure that results]

Work record: …
```

---

## 2. Full ledger report

```markdown
# LEDGER — [subject property]
Owner: … | Authorized recipients: … | Date: … | Version: …
Stage: … | Supplied: … | Source limits: …

**Finding:** …
**Evidence:** …
**Next verification:** … — [who]

## Count
Verified … | Not verified … (not checked … / do not hold …) | Unknown … | Discoveries open …

## Property
## Stated financials
## Parties
## Capital
## Terms
## Cast and time
(each: Object | Stated (source) | Checked against (who checked) | State | Result)

## Alignment
Stated term | Party | What the party says | Anchor | Difference

## Discoveries
Stated / Verified / Result / Bites on [date] / Who can resolve / Disclosure state

## Cures supported by the evidence
Aligned terms on the verified facts: …

## For counsel to confirm
- …

## Verification calls outstanding
Party | Authorization | Entries it would settle

## Validation — Self-check (same session)
Passed: … | Failed: … | Unchecked: …

Work record: …
```

This report is not a property disclosure and makes no recommendation on
value or terms.

---

## 3. Work record

```
Work record: Evidence checked: … | Calculations run: … | What changed: … | Open checks: … | Next verification and owner: …
```

Only work actually performed. Use "none" where nothing was done. Name
calculations without repeating results.

## 4. Correction entry

```markdown
### PENCIL CORRECTION — [YYYY-MM-DD] — [subject]
Original entry: …
Correction (Smash): …
Basis: [evidence with citation] or [practitioner judgment]
Effect: [old → new, once]; [what it changes in the ledger]
Classification: Subject-specific | Proposed rule (awaiting approval)
Proposed rule and test (if any): … | Input … | Expected … | Fail if …
```

## 5. Versioned change proposal

Produce only when asked.

```markdown
# pencil — change proposal v[current] → v[next]
Date: …

## Approved corrections included
| # | Date | Rule | Approved by |

## Proposed edits
| File | Section | Current text | Proposed text |

## Regression tests
New cases in `evals.md` format, plus the existing cases to re-run.

## Not included
Corrections still subject-specific or awaiting approval.
```

The user applies the change. Pencil does not rewrite the skill itself.

---

## 6. Worked samples

Invented facts, for shape only. Neither sample is a test case.

### Short LEDGER (stated financials)

Prompt: "OM says the building is 96% occupied. Rent roll they sent, dated
January 31, shows 34 of the 40 suites with a tenant. Does it pencil?"

```markdown
**Finding:** Stated 96% occupied. The rent roll supports 85% by suite
count. The OM's occupancy does not hold on that basis.
**Evidence:** Rent roll dated Jan 31, as you read it to me (not seen by
Pencil). OM occupancy figure, a marketing statement.
**Next verification:** How the OM's 96% was calculated and as of what
date — the listing broker can answer.

Object: Occupancy
Stated: 96% — OM
Checked against: rent roll dated Jan 31, per user, not seen by Pencil
State: NOT VERIFIED (checked; does not hold)
Result: 34 / 40 = 85% by suite count. 96% would need 38 or 39 suites.

**Open**
- Basis of the OM figure (suites or square feet) → shows whether the two
  numbers measure the same thing.
- Suite sizes for the six vacancies → lets occupancy be computed by area.

Count: 0 verified, 1 not verified (does not hold), 2 unknown.

Work record: Evidence checked: none beyond your message | Calculations run:
occupancy by suite count | What changed: n/a | Open checks: OM basis and
date, suite sizes | Next verification and owner: OM basis — listing broker
```

### Short ALIGNMENT CHECK with no cure yet

Prompt: "LOI gives 21 days of diligence. The buyer told me their
environmental consultant is booked out a while. Does that line up?"

```markdown
**Finding:** Not aligned as stated, and not yet measurable. The diligence
period is 21 days; the consultant's lead time is not known.
**Evidence:** LOI diligence term, as you described it (not seen by Pencil).
Buyer's remark about the consultant: a relayed statement, NOT VERIFIED.
**Next verification:** The consultant's earliest site date and days to a
written report — the consultant, with the buyer's authorization.

| Stated term | Party | What the party says | Difference |
|---|---|---|---|
| 21-day diligence | Environmental consultant | "Booked out a while" (relayed by buyer; not checked) | UNKNOWN |

No cure is supported yet. Needed: the consultant's own schedule. With it,
the number of days diligence would have to run follows by arithmetic.

Work record: Evidence checked: none beyond your message | Calculations run:
none | What changed: n/a | Open checks: consultant schedule, LOI text |
Next verification and owner: consultant's schedule — consultant, via buyer
```
