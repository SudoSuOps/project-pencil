# Output templates

Short forms are the default. Use the full decision brief when the user asks
for it or the deal has multiple material dependencies (see `SKILL.md`).
Every response opens with finding, evidence, next action. Drop any section
that has nothing to say.

## Contents

1. Short forms: DEAL COLOR, REASON FOR MY CALL, DOES IT PENCIL?, AFTER THE CALL
2. Full decision brief
3. Work record
4. Correction entry
5. Versioned change proposal
6. Worked samples

---

## 1. Short forms

### DEAL COLOR

```markdown
**Finding:** [who this is and how far the record supports them]
**Evidence:** [what it rests on, tagged]
**Next action:** [one action] — [owner]

**Can say out loud**
- [claim the record supports today]

**Verify first**
- [fact] → [what it would let us decide]

**Questions** (0–3, only if the answer changes the next move)

Work record: …
```

### REASON FOR MY CALL

```markdown
**Finding:** [the call the record supports: specific / exploratory / learning]
**Evidence:** [what earns it, tagged]
**Next action:** [one action] — [owner]

**Opening**
"[Name], [caller] with [firm]. Reason for my call: …"

**If they ask "[the obvious pushback]"**
"[truthful answer; 'I don't know' kept distinct from 'I can't share']"

**Two questions worth asking**
1. …
2. …

**Not yet**
- [claim the record does not support; do not say or imply it]

Work record: …
```

### DOES IT PENCIL?

```markdown
**Finding:** [underwriting result on which NOI] / [execution picture], stated separately
**Evidence:** [inputs and their tags]
**Next action:** [one action] — [owner]

**Math** (once)
[Metric] = [formula] = [inputs with source] = [result]

**Open**
- [missing fact] → [what it would let us decide]

**Decision due:** [what, by when, who decides]

Work record: …
```

### AFTER THE CALL

```markdown
**Finding:** [what the call changed, in one line]
**Next action:** [one action] — [owner]

**Said** (attributed; enters as REPORTED)
- [Speaker]: …

**Record changes**
- [Field]: was … → now … (TAG) — source: [speaker, date]

**Verify**
- [claim] — evidence needed — owner

**New exceptions**
- …

Work record: …
```

---

## 2. Full decision brief

```markdown
# DOES IT PENCIL? — [deal]

**Finding:** …
**Evidence:** …
**Next action:** … — [owner]

Audience: … | Decision due: … | Decider: … | Disclosure scope: …

## Status
Examination: DEFENDABLE — EXAMINATION, or OPEN — [missing fact] → [what it
would decide]
Execution readiness: DEFENDABLE WITH CONDITIONS | NOT YET DEFENDABLE —
EXECUTION | not examined — why

## Parties and authority
Role | Name/entity | Claim | Tag | Source

## The math
Metric | Formula | Inputs (with source) | Result
What moves the answer: …
Open metrics: [metric] — needs [input]

## Capital vs. clock
Capital stage: … [evidence]; what it does not establish: …
Milestone | Date | Fixed or formula | Source | Status
Gaps: …

## Material exceptions
Exception | Severity and why | Evidence | Impact | Owner | Dependency |
Deadline | Possible cure | Cost/time | Disclosure state

## For counsel to confirm
- …

## Decision due
What the authorized human has to decide, by when, and what is needed first.

## Scenarios (optional)
SCENARIO — not in the deal record. Assumed: … Result: …

## Validation — Self-check (same session)
Passed: … | Failed: … | Unchecked: …

Work record: …
```

---

## 3. Work record

One line at the end of every substantive response:

```
Work record: Evidence checked: … | Calculations run: … | What changed: … | Open checks: … | Next action and owner: …
```

Only work actually performed. Use "none" where nothing was done. Name
calculations without repeating their results.

## 4. Correction entry

The entry carries the corrected calculation, once.

```markdown
### PENCIL CORRECTION — [YYYY-MM-DD] — [deal]
Original finding: …
Correction (Smash): …
Basis: [evidence with citation] or [practitioner judgment]
Effect: [old → new, the calculation once]; [what it changes in the decision or call]
Classification: Deal-specific | Proposed rule (awaiting approval)
Proposed rule and test (if any): … | Input … | Expected … | Fail if …
```

Lead the response with what the correction changes, then give the entry.

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
Corrections still deal-specific or awaiting approval.
```

The user applies the change. PencilBot does not rewrite the skill itself.

---

## 6. Worked samples

Invented facts, for shape only. Neither sample is a test case.

### Short DOES IT PENCIL? (reconciliation)

Prompt: "OM says the building is 96% occupied. I pulled the rent roll they
sent, dated January 31: 34 of the 40 suites show a tenant. Does the OM hold
up?"

```markdown
**Finding:** No. The rent roll supports 85% occupancy by suite count, not
the OM's 96%.
**Evidence:** Rent roll dated Jan 31, as you read it to me: 34 of 40 suites
leased (REPORTED; I have not seen the document). OM figure: 96% (REPORTED,
marketing document).
**Next action:** Ask the listing broker how 96% was calculated and as of
what date — you.

**Math**
34 / 40 = 85%. The OM's 96% would need 38 or 39 suites leased by count.

**Open**
- Whether the OM measures by square feet rather than suites → could explain
  part of the gap if the six vacant suites are small.
- Date of the OM's figure → tells us whether tenants left after it was
  written.
- Suite sizes for the six vacancies → lets us compute occupancy by area and
  the rent at stake.

Work record: Evidence checked: none beyond your message | Calculations run:
occupancy by suite count | What changed: n/a | Open checks: OM basis and
date, suite sizes | Next action and owner: question to listing broker — you
```

### Short DEAL COLOR with the line drawn

Prompt: "A property manager I know says the owner of the Dixie Highway
strip center 'has to sell by year-end' because of a partnership dispute. I
haven't talked to the owner. Color?"

```markdown
**Finding:** You have a secondhand account of seller pressure and nothing
from the owner. That supports a learning call, not a pitch.
**Evidence:** Property manager's statement to you (VERIFIED as said;
content REPORTED, secondhand). Owner's intent, the dispute, and any
deadline: UNKNOWN.
**Next action:** Call the owner to ask about their plans for the property —
you.

**Can say out loud**
- You work that corridor and wanted to introduce yourself and ask about
  their plans.

**Verify first**
- Who owns it and who can sign → tells us whether one call reaches a
  decision-maker.
- Whether a sale is being considered at all → decides if there is an
  assignment to pursue.

**Not yet**
- That they have to sell, that there is a dispute, or any deadline. Raising
  it would also expose the property manager.

Work record: Evidence checked: none beyond your message | Calculations run:
none | What changed: n/a | Open checks: ownership, authority, intent | Next
action and owner: introductory call — you
```
