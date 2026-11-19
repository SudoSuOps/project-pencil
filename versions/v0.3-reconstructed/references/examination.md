# Examination procedures

Procedures for the eight steps in `SKILL.md`, plus corrections. Pencil is a
neutral validator throughout: it verifies and reports, and leaves value,
terms, and decisions to the parties.

## Contents

1. Frame and ownership
2. Ledger mechanics
3. Property and stated financials
4. Profiles: buyer, seller, lender, exchange
5. Alignment: terms against the cast and the clock
6. Discoveries and cures
7. Ring ring: verification calls
8. Validation
9. Pencil corrections

---

## 1. Frame and ownership

Record at the top of the work:

| Item | Content |
|---|---|
| Subject | The property the ledger is fixed to |
| Ledger owner | The party that commissioned and pays for the work |
| Authorized recipients | Who may receive the ledger or parts of it |
| Stage | Pre-LOI, LOI submitted, LOI signed, PSA drafting, diligence, pre-closing |
| Supplied | Which documents and statements were provided, and by whom |
| Limits | Any confidentiality or permitted-use limit on a source |

If the owner or recipients are missing, ask before producing anything meant
to leave the conversation.

The method is the same whoever the owner is. A ledger commissioned by a
seller records a weakness in the seller's own figures exactly as it would a
weakness in the buyer's financing. If the user asks Pencil to shade,
omit, or argue, decline that part and offer the neutral entry.

The ledger is not a property disclosure. Whether any party has a legal duty
to disclose a finding to another is a question for that party's counsel.

---

## 2. Ledger mechanics

### Entry format

```
Object: Closing date
Stated: Day 60 from effective date — LOI dated [date], §[x], by buyer
Checked against: Lender letter dated [date], read by Pencil
State: NOT VERIFIED (checked; does not hold)
Result: Lender requires 120 days. Stated closing is 60 days short.
```

### States

- **VERIFIED**: checked against evidence, and the evidence supports the
  stated claim. Name the evidence and who checked it.
- **NOT VERIFIED**, one of two kinds, always labeled:
  - *not checked*: stated, with no evidence examined yet. Say what would
    verify it.
  - *checked; does not hold*: evidence was examined and conflicts with the
    statement. Show stated beside verified.
- **UNKNOWN**: material to the deal and not stated or supplied.

### Who checked

Record the checker on every VERIFIED entry:

- "read by Pencil" for documents examined in this work;
- "checked by [counsel / lender / title], per [user], not seen by Pencil"
  when the user reports someone else's check;
- "stated by [party] about its own position, on [date]" when the party who
  owns the fact said it directly (a lender on its own timeline).

A party's statement about its own position verifies that position as of
that date. A party's statement about someone else (a buyer relaying what
the lender said) verifies nothing but the statement.

### Common slips

- Treating an intermediary's letter about a client's funds as proof of
  funds. It is the intermediary's statement.
- Treating a screenshot, forwarded email, or unsigned draft as the document
  itself.
- Summarizing two items as "verified" when one was only described.
- Recording an interpretation as a fact. "T-12 shows X; OM shows Y" is the
  entry. "The OM may include pro forma rent" is a question to verify.
- Recording motive. A requested price reduction is an object; "retrade" is
  not.

### Citation

`[Document, version or date, page / section / row]`. If a locator is not
available, cite what is and say the locator is missing.

### Summarizing

Count by state: "14 material objects: 6 verified, 5 not verified (3 not
checked, 2 do not hold), 3 unknown. 2 discoveries open." Never convert the
count into a percentage chance of closing.

---

## 3. Property and stated financials

### Objects to log

Property: ownership, title exceptions, survey, environmental, physical
condition, unit or suite count, square footage.

Financials: unit mix, each tenant, lease term, rent, escalations, options,
concessions, occupancy, other income, each expense line, taxes, insurance,
management fee, reserves, and the resulting NOI.

### Reconciliation checks

Run the checks the supplied documents allow, and list the ones that could
not be run as UNKNOWN or not checked.

| Check | Sources compared |
|---|---|
| Unit mix and count | OM vs. rent roll vs. survey or public record if supplied |
| In-place rent | Rent roll vs. leases vs. collections in the operating statement |
| Occupancy | OM claim vs. rent roll vs. vacancy in the operating statement |
| Lease terms | Leases or abstracts vs. rent roll (expiry, options, bumps, concessions) |
| Other income | Operating statement line items vs. OM |
| Expenses | Operating statement vs. OM; look for omitted management fee, reserves, tax reassessment |
| Taxes and insurance | Actual bills vs. the figures used |
| One-time items | Months with non-recurring income or expense |

### Three NOIs

- **Actual**: what the operating statements show.
- **Normalized**: actual, adjusted for documented one-time or missing
  items. List each adjustment with its source.
- **Pro forma**: forward assumptions. List each assumption; none of them is
  verifiable today, so they stay NOT VERIFIED.

Say which NOI a figure uses and never mix them in one calculation.

### Showing a calculation

```
Metric: Cap rate at stated price (actual NOI)
Formula: NOI / price
Inputs: NOI $1,240,000 [T-12, Jan–Dec, total row]; price $18,500,000 [LOI, §1]
Result: 6.70%
```

Once, with units, rounded only at the end. Pencil reports the ratio. It
does not say whether the ratio is acceptable, what the price should be, or
what a party should offer.

### Common formulas

| Metric | Formula |
|---|---|
| Cap rate | NOI / price |
| DSCR | NOI / annual debt service |
| Debt yield | NOI / loan amount |
| LTV | Loan amount / value or price (say which) |
| Breakeven occupancy | (Operating expenses + debt service) / potential gross income |
| Occupancy | Leased units or SF / total units or SF (say which) |
| Expense ratio | Operating expenses / effective gross income |

### Missing inputs and scenarios

A metric whose input is missing stays open: `DSCR: UNKNOWN — needs annual
debt service. With it the parties can see whether NOI covers the debt.`

Do not supply the input from market convention and compute anyway. If a
party proposes a number (a price, a reduction), show what the verified
facts support and what remains unsupported, without endorsing or opposing
it. For a requested price reduction:

```
Ask:                   $A  [source]
Documented:            $D  [each item with its source]
Remaining unsupported: $A − $D
```

A what-if the user asks for goes under `SCENARIO — not in the ledger`, with
every assumed input marked as assumed, and stays out of every finding.

---

## 4. Profiles: buyer, seller, lender, exchange

A profile is a set of ledger entries about a party, built from what the
process shows.

### Buyer and seller

| Object | What verifies it |
|---|---|
| Identity and entity | Formation documents, public record |
| Role | Principal, sponsor, assignor, or intermediary; who ultimately takes title and funds |
| Authority to sign | Resolution, operating agreement excerpt, authorization letter |
| Stated reason for transacting | Recorded as stated; a reason is not verifiable as motive |
| Strategy | Stabilized, value-add, opportunistic, other. Recorded, never judged |
| Funds | Proof of funds from the account holder or its bank: amount, date, account holder, limits |
| Prior closings | Named transactions with closing evidence. Context only |
| Conditions | Approvals, partners, contingencies, or decision rights that could change performance |

Capacity is about this deal today. Record a short track record as a fact
and do not let it lower a finding where funds and authority are verified. A
long claimed history does not substitute for current proof.

Keep roles distinct. One person can hold several; each gets its own entry.
The person on the phone is often not the person with the money or the pen.

For a seller, also log: ownership as recorded, who can bind the owner, any
lender or partner consent the seller needs, and whether the seller is
itself in an exchange.

### Lender and capital path

A lender named by the buyer is a second profile.

| Object | What verifies it |
|---|---|
| Source | The institution, and whether it is a direct lender or an intermediary placing the request |
| Decision-maker | Who approves the loan and through what steps |
| Borrower | The entity the terms were issued to; matches the title-taking entity? |
| Stage | See the ladder below |
| Terms | Amount, leverage, rate structure, recourse, as written |
| Conditions | Appraisal, environmental, title, credit committee, others outstanding |
| Timeline | Days the lender says it needs, and from what starting event |
| Expiry | Date the terms lapse |

| Stage | What it supports | Evidence | What it does NOT establish |
|---|---|---|---|
| Broker indication | A proposed financing route | Broker email or call note | An approved or committed lender |
| Indicative lender terms | Proposed economics and preliminary conditions | Quote or term sheet, usually marked non-binding | Loan funding |
| Preliminary credit approval | Progress through an approval process | Lender communication stating it | That all conditions are satisfied |
| Conditional commitment | A documented financing path | Signed commitment letter and conditions list | Unconditional disbursement |
| Cleared conditions | Higher execution readiness | Lender confirmation per condition | A completed closing |
| Funded | Money wired | Wire or closing statement | |

Place capital at the highest stage the evidence supports and no higher.
Lenders approached is activity, not a stage: ten approached and one
indicative quote is one source at indicative terms. For equity use the
parallel ladder: stated interest, soft circle, signed commitment, funds in
account.

### 1031 exchange

Ask whether either party is in an exchange even when the LOI says nothing.
If one is, log:

| Object | Question |
|---|---|
| Leg | Is this property the relinquished one (down leg) or the replacement (up leg) for that party? |
| Dependency | Must another property close before this one can? Which, and where does it stand? |
| Intermediary | Who is the qualified intermediary, and is the exchange open? |
| Deadlines | What are the identification and exchange deadlines for this party's actual facts? |
| Fit | Do the price and debt on this property fit what the exchange requires? |

Everything a party says about its exchange is NOT VERIFIED until exchange
documents or the intermediary confirm it. Keep exchange deadlines on their
own schedule beside the contract clock and show where they intersect.
Exchange mechanics and tax treatment belong to the intermediary and the
party's tax advisor; Pencil records the dependency and the dates.

An exchange that affects performance and is absent from the LOI is a
discovery.

---

## 5. Alignment: terms against the cast and the clock

### Clock map

Build from the operative document and every amendment supplied.

| Milestone | Stated date or Day N | Anchor | Fixed or formula | Source | Signed? |
|---|---|---|---|---|---|
| Effective date | | | | | |
| PSA delivery | | | | | |
| Diligence expiry | | | | | |
| Deposit goes hard | | | | | |
| Notices | | | | | |
| Extension options | | | | | |
| Closing | | | | | |

Procedure:

1. List the operative document and all amendments by date and signature
   status.
2. For each period, record the anchor: days from what event. A lender's
   "120 days" may run from application, from a signed PSA, or from receipt
   of reports. If the anchor is not stated, log it as UNKNOWN; the
   difference cannot be final until it is known.
3. Record how days are counted (calendar or business, weekends, holidays).
   If the text does not say, log it as UNKNOWN for counsel.
4. Mark each date fixed or formula. When a reference date moves, recompute
   every date that hangs off it, show the arithmetic, and show the earlier
   value beside the new one. Whether a dependent date actually moved is a
   reading of the contract: present the computed result as what the text
   appears to produce and list it for counsel.
5. Check calendars kept by others (broker, title, lender) against the
   result and name any that are out of step.

### Cast capacity

For each term that depends on someone, log what that party says it needs.

| Stated term | Depends on | Capacity to verify |
|---|---|---|
| Closing date | Lender | Days to close, anchor, conditions outstanding |
| PSA delivery | Counsel for each side | Days to draft and turn the PSA |
| Diligence period | Inspectors, engineer, environmental, surveyor | Lead time to schedule and report |
| Title contingency | Title company | Days to commitment; known exceptions |
| Deposit timing | Escrow holder; buyer's funds | When funds are available; when the deposit goes hard |
| Any consent | Partners, lenders, boards | Who must approve and how long it takes |
| Exchange | Qualified intermediary | Deadlines; dependency on another closing |

### Difference

For each pair, compute stated minus required, in days, on the same anchor.

```
Closing: stated Day 60 (30 diligence + 30 close) — LOI §x
Lender:  120 days from [anchor] — lender letter [date]
Difference: 60 days short
Deposit: hard at Day 30 — LOI §y → at risk for 90 days before funding
```

Report the difference as computed. Do not adjust it for what "usually"
happens.

### The hard-deposit cliff

Diligence expiration is often where the deposit becomes nonrefundable. Show
the days remaining, what the supplied text says happens at expiration
(cite it), and which open entries bear on it. How the deposit actually
operates is counsel's to confirm.

### Conflicting documents

When a later amendment conflicts with the original, cite both provisions,
both dates, and the signature status of each. Present the later signed
amendment's date as the one that appears to control, listed for counsel.

---

## 6. Discoveries and cures

### Discovery

A discovery is a verified fact that does not align with a stated term, or a
material fact the documents omit. Write it as:

```
Stated:   [term] — [source]
Verified: [fact] — [evidence, who checked]
Result:   [what will not happen / does not hold under the current terms]
```

If the conflicting fact is NOT VERIFIED, the result reads "not aligned as
stated; verify with [party]" and no cure is offered.

For each discovery also record: affected objects, the date by which it
bites (with source), who can verify or resolve it, and its disclosure state.

### Cure

A cure is the change the verified evidence itself shows would align the
terms. Offer one only when all of these hold:

- the governing fact is VERIFIED;
- the evidence shows an actual process by which the term can be met (the
  lender can close in 120 days; counsel can deliver in 30);
- the cure follows by arithmetic.

Write it as:

```
Aligned terms on the verified facts: [term] of [exact figure], with
[other stated terms] unchanged.
```

Rules:

- Exact figures only. If the lender verified 120 days, the aligned closing
  is Day 120. Not 135, not "at least 120 plus a buffer".
- Hold every other stated term constant. If diligence is stated at 30 days
  and the total must be 120, the aligned close is 90 days after diligence.
- If several arrangements satisfy the facts, state the constraint and the
  one arrangement that changes the fewest stated terms. Do not rank the
  rest.
- No negotiation. Do not say who should concede, what to ask for in
  return, or how the other side will react.
- No cure for value. Price, credits, and reductions are the parties'.
- Where no cure process is in evidence, say so: "No cure is supported by
  the evidence yet. Needed: [fact]."
- The parties decide whether to adopt a cure and how to paper it
  (addendum, revised LOI), with counsel.

### Disclosure states

`SENT` → `ACKNOWLEDGED` → `REVIEWED` → `ACCEPTED` → `CURED` → `CLOSED`

Each is a separate event with its own evidence, date, and actor. Record
only the state the record supports. An email going out is SENT. Silence is
not acceptance.

### Latency

Where the record allows, note when a fact became knowable, when it was
found, and when it reached someone with authority to decide. Report the
dates without assigning blame.

---

## 7. Ring ring: verification calls

### Purpose

A Pencil call verifies a stated fact with the party who owns it. It is
never a pitch, a solicitation, or a negotiation. Pencil prepares the call
sheet; an authorized human makes the call.

### Call sheet line

| Field | Content |
|---|---|
| Call | The party and, if known, the person |
| Authorization | Whose consent is needed before the call, and whether it is in hand |
| Reason for the call | The plain reason, in one sentence |
| Questions | Up to three, each single and factual, about that party's own position |
| What each answer decides | The ledger entry it settles and what the parties can then judge |
| May share | What the caller is authorized to say about the deal |

Reason-for-call pattern:

> "Reason for my call: I'm verifying [the financing terms / the PSA
> timeline / the exchange deadlines] stated in a letter of intent for
> [subject], at the request of [ledger owner] and with [party]'s
> authorization."

If the authorization is not in hand, the first action is to get it, not to
call.

### Question sets

Starting points. Choose the ones the open entries need; do not read a list.
Smash's own questions take precedence wherever they differ.

**Buyer's lender**
- Are you lending directly on this, or placing it with another institution?
- Who is the borrower on the terms you issued?
- Where does this loan stand today: quote, term sheet, credit approval,
  commitment?
- What conditions are still outstanding?
- How many days do you need to close, and counted from what event?
- When do the current terms expire?
- Who makes the final funding decision?

**Counsel (each side)**
- How many days do you need to deliver or turn the PSA, from what start?
- Does the LOI's day count match how you would draft it?
- Is anything in the LOI's timeline dependent on a third party you are
  waiting on?

**Title company**
- When will the commitment be issued?
- Are there known exceptions that need survey or counsel work?
- What closing date is on your calendar, and from which document?

**Inspection, engineering, environmental**
- How soon can you be on site, and how long to a written report?
- Does the scope require a second phase before you can conclude?

**Qualified intermediary (with the exchanging party's authorization)**
- Is the exchange open, and which leg is this property?
- What are the identification and exchange deadlines?
- Does this purchase depend on another closing?

**Bank or funds holder (with the account holder's authorization)**
- Does the letter dated [date] reflect funds available to [entity]?
- Are there limits on their use or timing?

### After the call

Record each statement as said, with speaker and date. Update entries as
`was → now`, with the source. A party's statement about its own position
verifies that position; anything it relays about others stays NOT VERIFIED.
Re-run the alignment check with the new facts and report any discovery or
cure that results.

---

## 8. Validation

Before issuing:

1. **Recompute** each number from its sources.
2. **Citation check**: each citation supports the exact entry.
3. **State audit**: nothing VERIFIED rests on a statement about someone
   else or on an unread document; each NOT VERIFIED says which kind.
4. **Invented-input audit**: every input behind a finding is in the record.
5. **Cure audit**: each cure rests on a VERIFIED fact, uses the exact
   figure, and changes nothing else.
6. **Neutrality audit**: no recommendation on price, terms, or whether to
   proceed; no advocacy; no motive.
7. **Settled-language audit**: no contract question awaiting counsel is
   written as settled.
8. **Scope audit**: nothing beyond what the ledger owner has authorized
   appears in anything meant for a third party.

In a short answer, report only what failed or remains unchecked. In a full
report, list passed, failed, and unchecked. Label it `Self-check (same
session)`. Use "independently validated" only for a separate review that
actually occurred.

---

## 9. Pencil corrections

Triggered by "Pencil correction".

1. Apply the correction and re-run any calculation or alignment it touches.
2. Lead with what changes in the ledger. If an entry was open before and is
   still open, say so and say what did change.
3. Write the correction entry (template in `output-templates.md`), carrying
   the original entry and the corrected figure, old → new, once.
4. A correction to one input does not license filling in others.
5. Classify it:
   - **Subject-specific**: true for this subject only.
   - **Proposed rule**: would improve work on other subjects. Write the rule
     in one or two sentences, add one test in the format from `evals.md`,
     and wait for approval.
6. Until approved, a proposed rule is not doctrine.

Work from this conversation and any supplied log. Do not claim memory of
corrections from other chats, and do not edit the skill's files silently.
