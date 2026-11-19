# Journal

What happened, in order. One entry per working day. Detail lives in the
case studies and `DOCTRINE.md`.

## 2026-11-19

1. **v0.1 built** from the original spec and two discovery documents: a
   transaction examiner with four reference files.
2. **First acceptance test** (CS-001). v0.1 passed 36 of 36 checks against
   27 of 36 with no skill. Answers ran long.
3. **v0.2 built and tested** against v0.1 and no skill, 90 responses
   (CS-002). One critical error in 30 for v0.2, 3 for v0.1, 20 for no
   skill.
4. **Role corrected** (CS-003). Pencil does not prospect, represent, price
   or negotiate. It is a neutral validator and the ledger is the product.
   v0.3 built.
5. **Rules, not judgment** (CS-004). Pencil does not drift; a human
   reviews before release. v0.4 moved the ledger into code with a
   validator and a review gate. First drift test found four defects.
6. **v0.4 tested against v0.3**, 36 responses (CS-005). v0.4 did not win
   on behavior. Drift clean on two of six cases; numbers and cures never
   differed.
7. **The relayed rule** (CS-006, ruling 25). Something read out from a
   document Pencil has not seen is never verified. Written into v0.5 and
   its validator. Not yet tested.
8. **Repositories created.** `project-pencil` for the skill, doctrine,
   case studies and evidence. `ledger.pencil` for the gated ledger site
   for `ledger.pencilbot.ai`: built and tested locally, not deployed.
9. **Founding Blueprint adopted** (CS-007). Rulings 26 to 37. Three points
   where it differs from the skill are held open.
10. **Testnet framing.** This work is the Pencil testnet. One principle,
    the integrity of the Pencil and its role in an assignment; domains
    interchangeable; CRE the voice. Doctrine split into core and CRE pack.
11. **Pencil as a service** (ruling 38). Flat fee, never commission.
12. **The pain point** (CS-008, rulings 39 and 40). The unwind period and
    defendable mode.

13. **The NDA question.** A model cannot sign an NDA; the company signs
    and is accountable, and every processor must be covered, or the
    document never leaves. Ruling 41: the Pencil gets a vault. Two more
    pain points recorded: confidential documents leaving the NDA, and
    talking about a deal under NDA. `PAIN_POINTS.md` started.
14. **The unknown** added as market pain point 8: nobody is counting how
    many AI tools receive confidential documents in the cloud. Sources
    recorded with it.

### Open at the end of the day

- Rulings needed: status words, cures, assumed-input arithmetic, relayed
  third-party checks, reported calls (questions 1, 2, 9, 10, 11).
- Smash to supply: his first-meeting seller questions and his lender
  questions (questions 7, 15); real unwinds, anonymized (CS-008).
- To build: v0.5 fixes from CS-005, then test against v0.4; the claim
  schema with a source inventory; per-ledger access on the site.
- To do in Cloudflare: connect `ledger.pencil` to Pages and set up Access.
- To check: visibility of both repositories.
