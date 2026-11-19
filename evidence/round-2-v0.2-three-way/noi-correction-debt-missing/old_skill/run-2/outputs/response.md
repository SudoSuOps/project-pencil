# DOES IT PENCIL? (corrected) — Hialeah flex

**Short answer:** Holding the same cap rate, the corrected NOI supports about **$22.15M**, not $24.0M. The $22M number is roughly $154K below that. The debt side is still open because there is no lender quote, so the deal cannot be called penciled or not penciled yet.

Audience: Smash and the buy-side team (I am reading "we should go back at $22M" as you being on the buyer's side; tell me if that is wrong) | Decision: whether to re-price, and at what number | Stage: UNKNOWN (LOI or PSA not stated) | Decider: the buyer principal

I do not have the earlier brief in this conversation, so I am working from the two figures as you restated them: $24.0M and $1,560,000.

## Status

- **Examination: INSUFFICIENT EVIDENCE.** The $120K adjustment rests on a relayed bookkeeper statement, the T-12 was not supplied, and the departed tenant's rent has not been tested.
- **Execution readiness: NOT YET DEFENDABLE — EXECUTION.** There is no lender quote, so capital is not on the ladder, and the contract clock is unknown.

## What changed

| Item | Before | After | Tag |
|---|---|---|---|
| NOI basis | $1,560,000 actual T-12 | $1,440,000 normalized | REPORTED (bookkeeper, relayed by you; no document supplied) |
| Adjustment | none | −$120,000 lease termination fee, tenant vacated in March | REPORTED |
| Cap rate at $24.0M | 6.50% | 6.00% | calculated |
| Price at a held 6.50% cap | $24,000,000 | $22,153,846 | calculated; holding the cap is an assumption |

## The math

| Metric | Formula | Inputs | Result |
|---|---|---|---|
| Original cap rate | NOI / price | $1,560,000 / $24,000,000 | 6.50% |
| Normalized NOI | actual − one-time fee | $1,560,000 − $120,000 | $1,440,000 |
| Cap rate at $24.0M, normalized | NOI / price | $1,440,000 / $24,000,000 | 6.00% |
| Value at held cap | NOI / cap rate | $1,440,000 / 6.50% | $22,153,846 |
| Reduction the fee supports | price − value | $24,000,000 − $22,153,846 | $1,846,154 |
| Cap rate at $22.0M, normalized | NOI / price | $1,440,000 / $22,000,000 | 6.55% |

All figures are annual dollars, rounded to the dollar and to two decimals at the end.

**What moves the answer most is the cap rate.** I inferred 6.50% from your two numbers; it is not a checked market fact.

| Cap rate on $1,440,000 | Price |
|---|---|
| 6.00% | $24,000,000 |
| 6.25% | $23,040,000 |
| 6.50% | $22,153,846 |
| 6.75% | $21,333,333 |

## The $22M ask, decomposed

```
Ask (reduction from $24.0M):        $2,000,000   [buyer's analyst, REPORTED]
Explained by the $120K fee at 6.50%: $1,846,154   [calculated, on a REPORTED input]
Modeled exposure:                    none supplied
Remaining to explain:                $153,846     (7.7% of the ask)
```

The analyst's basis for the last $153,846 is not in the record, so it is neither justified nor unjustified yet.

One fact could close it. At a 6.50% cap, $22.0M needs NOI of $1,430,000, which is only $10,000 below the normalized figure. If the T-12 still carries more than $10,000 of rent from the tenant who left in March, and that space has not been re-leased, then $22M is at or above the held cap.

## Open metrics

- **DSCR, debt yield, LTV, cash-on-cash: OPEN.** They need loan amount, rate and amortization, and no lender quote is in.
- **Direction only:** a lender sizing on NOI will be working from 7.7% less income ($120,000 / $1,560,000). Proceeds constrained by DSCR or debt yield would fall in the same proportion, and the equity check would rise. I have not put a dollar figure on that.

## Material exceptions

| Exception | Evidence | Impact | Owner | Possible cure |
|---|---|---|---|---|
| The $120K fee is not documented | Bookkeeper statement, relayed (REPORTED) | The whole re-price rests on it | You, with the seller's side | Get the T-12 line and month, plus the termination agreement or ledger entry |
| The departed tenant's rent may still be in the T-12 | Tenant left in March; T-12 window not stated (UNKNOWN) | NOI could be lower than $1,440,000 | Buyer's analyst | Get the current rent roll, the tenant's rent by month, and the re-leasing status of the space |
| No lender quote | You stated it | Capital is not on the ladder; all debt metrics open | Buyer and lender | Give the lender the normalized NOI now, so the quote is sized on the right number |
| Clock unknown | Not stated | A re-price near diligence expiry or a hard deposit changes the options | You and counsel | Confirm stage and dates from the operative document; contract rights are counsel's call |

## Decision due

The buyer principal decides whether to go back and at what number. Three positions are on the table:

- **$22.15M:** the fee alone, at the held cap. This is the number the record supports today.
- **$22.0M:** needs about $10K more of non-recurring NOI shown, or a stated cap-rate argument.
- **Wait for the lender quote:** re-price once, with debt in hand, instead of twice.

Before choosing, get the fee documented and the vacated space tested. A re-price built on a number the seller's own bookkeeper confirmed is easier to defend than a round number.

## Validation: self-check (same session)

- **Passed:** all six calculations above were recomputed in code, plus $22,000,000 × 6.50% = $1,430,000 and $2,000,000 − $1,846,154 = $153,846.
- **Unchecked:** the T-12 itself, the fee amount and its line item, the T-12 window, the vacated tenant's rent, the rent roll, the original brief, the cap rate against market, and any contract dates.

---

### PENCIL CORRECTION — 2026-11-19 — Hialeah flex

- **Original finding:** $24.0M price on $1,560,000 of T-12 NOI (6.50% cap on actual NOI).
- **Correction (Smash):** $120,000 of the T-12 NOI is a lease termination fee from a tenant that moved out in March. It is non-recurring.
- **Basis:** Seller's bookkeeper confirmation, relayed by Smash (REPORTED; no document supplied).
- **Effect on output:** NOI basis $1,560,000 actual → $1,440,000 normalized. Value at a held 6.50% cap $24,000,000 → $22,153,846. Cap rate at $24.0M 6.50% → 6.00%.
- **Effect on decision or call:** $24.0M is no longer supported at the original cap. A reduction of $1,846,154 is supported by the fee; $153,846 of the $22M ask remains to be explained. Debt metrics stay open until the lender quotes.
- **Classification:** Deal-specific. One proposed rule is below, pending your approval.

**Proposed rule:** When a lease termination fee is removed from NOI, also test whether the departed tenant's rent is still in the T-12 and whether the space has been re-leased. Leave NOI flagged as possibly overstated until that is answered.

**Proposed test:** Input: T-12 NOI includes a termination fee from a tenant who vacated mid-period. | Expected: the fee is removed, and the tenant's remaining rent and re-leasing status are listed as an open check. | Fail if: the brief presents the fee-adjusted NOI as fully normalized without that check.

**Status:** Awaiting approval. Not applied as doctrine.

---

**Work record:** Evidence checked: none (all figures taken from your message) | Calculations run: original cap, normalized NOI, value at held cap, supported reduction, cap at $22M and $24M, cap sensitivity, NOI required for $22M | What changed: NOI basis actual → normalized, supported price $24.0M → $22.15M at held cap | Open checks: fee documentation, vacated tenant's rent and re-leasing, lender quote, contract clock, cap rate support | Next action and owner: request the T-12 line item and termination agreement from the seller's side — Smash
