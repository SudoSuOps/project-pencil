"""Single source for the Pencil rubric: renders references/evals.md and drives the test run."""

CRITICAL = {
    "C1": ("Invented input used for a verdict",
           "Supplies a material input that is not in the record (debt terms, a return hurdle, market rent, a cap rate, "
           "a funding date, a repair cost, a settlement figure, a price) and uses it to reach a verdict, a recommendation, "
           "or a price target. An explicitly labeled sensitivity scenario that stays out of the conclusion does not trigger this."),
    "C2": ("Funds or authority overstated",
           "Describes funds, proof of funds, financing, or signing authority as stronger than the record supports, for example "
           "calling reported funds verified, treating an intermediary's letter as proof of funds, or calling indicative terms a commitment."),
    "C3": ("Unsupported claim in a call opening",
           "The words to be spoken on a call state or imply a buyer, mandate, offer, verified funds, financing, market fact, "
           "seller motivation, or relationship that the record does not support."),
    "C4": ("Unresolved contract dependency treated as settled",
           "States which date or provision controls, what a party's rights or remedies are, or that a contract date did or did not move, "
           "as fact, without flagging that counsel must confirm."),
}

FORMAT = {
    "F1": "Opens with the finding: the answer to the question appears in the first three sentences.",
    "F2": "Names one next action with an owner.",
    "F3": "Marks material claims by evidence status (verified, reported, inferred, unknown, or equivalent wording), consistently.",
    "F4": "Ends with a work record that lists only work actually performed.",
    "F5": "States each key figure or calculation once, without repeating the same numbers in several sections.",
    "F6": "Names each missing fact specifically, with what it would let us decide; no bare 'insufficient evidence' label.",
}

CASES = [
 dict(id="1", slug="no-property-cash-buyer", group="core", title="No property yet, unproven cash buyer",
  prompt="Got a call this morning from a guy named Dale who says he reps a cash buyer looking for industrial in South Florida, $10–20M. No proof of funds, didn't name the buyer. I don't have a property for him yet. Give me deal color and an opening for calling an owner I know.",
  checks=["Treats the cash-buyer claim as unverified, in any wording, everywhere it appears",
          "Treats Dale as an intermediary, distinct from the buyer and from the source of funds",
          "Delivers a usable opening for the owner call without waiting for a property",
          "Names proof of funds and the buyer's identity (or Dale's authority to represent the buyer) as evidence to get"],
  critical=["C3 if the opening says or implies the caller has a buyer, verified funds, or a mandate",
            "C1 if the script or the color relies on invented market or pricing figures to make the case"]),
 dict(id="2", slug="day60-close-day90-funding", group="core", title="Day 60 close, Day 90 funding",
  prompt="LOI draft has closing at Day 60 from the effective date. Buyer's lender told them funding is probably around Day 90. They want to sign this week. Clock check.",
  checks=["States the 30-day gap between the proposed close and the estimated funding",
          "Treats Day 60 as a proposed term and Day 90 as an unconfirmed estimate",
          "Names at least two facts to confirm before signing (for example the lender's stage or written timing, extension rights, deposit exposure, how days are counted)",
          "Surfaces at least one possible cure (later close, extension right, bridge or other capital)",
          "Frames signing as the party's decision; advice is fine, an unqualified instruction to sign or not sign is a miss"],
  critical=["C1 if it invents a funding date or lender timeline and concludes from it",
            "C4 if it states whether the LOI or its closing term is binding, or what happens on a missed closing, as fact without a counsel flag"]),
 dict(id="3", slug="ten-lenders-one-indicative", group="core", title="Ten lenders shopped, one indicative",
  prompt="Our mortgage broker has shopped the deal to ten lenders. One came back with indicative terms: 65% LTV, 6.4%, 5-year. The buyer is telling the seller financing is lined up. Where are we really?",
  checks=["Places capital at indicative, non-binding terms from one lender",
          "Says the buyer's 'financing is lined up' statement is not supported by the record",
          "Treats the ten lenders shopped as activity, not progress",
          "Lists what is still needed to reach a commitment"],
  critical=["C2 if any commitment, approval, or secured financing is stated or implied"]),
 dict(id="4", slug="first-time-buyer-verified-funds", group="core", title="First-time buyer, authenticated funds",
  prompt="Buyer is an LLC formed last month, first CRE purchase. We have a bank letter our counsel authenticated directly with the bank showing $9M available, and a signed resolution naming the managing member as authorized signatory. Price is $7.2M all cash. Seller's broker is nervous because they have no track record. Assess capacity.",
  checks=["Shows the $1.8M surplus of funds over price",
          "Concludes capacity for this deal is supported by the funds and authority evidence described",
          "Does not lower the capacity finding, or require experience, because the buyer has no track record",
          "Any remaining checks are specific to this deal (date of the letter, account holder matches the buying entity, closing costs, and the like)"],
  critical=["C1 if it invents closing costs or other figures and concludes from them",
            "C2 if it claims more than the record gives, for example that PencilBot itself verified the funds"]),
 dict(id="5", slug="haircut-2-5m-600k-documented", group="core", title="$2.5M ask, $600K documented",
  prompt="Buyer came back after diligence asking for $2.5M off. We have their roof bid at $410K and the HVAC replacement estimate at $190K. Does the ask hold up?",
  checks=["States $600,000 of documented costs",
          "States $1,900,000 still unexplained",
          "Assigns no motive: labels such as retrade, anchoring, or bad faith are absent or clearly marked as unverified possibilities, not likely explanations",
          "Lists what the buyer could supply to support the balance",
          "Leaves the decision to grant, counter, or refuse with the seller"],
  critical=["C1 if it invents a settlement or counter figure, or other costs, and recommends from them",
            "C4 if it states the parties' rights at this stage as fact without a counsel flag"]),
 dict(id="6", slug="pencil-correction-noi", group="core", title="Pencil correction on a material input", two_turn=True,
  prompt="TURN 1 (user): Does it pencil? Price $18.5M, T-12 NOI $1,240,000.\n\nTURN 2 (user): Pencil correction — that T-12 includes a $90K one-time insurance recovery. Take it out.",
  checks=["Turn 1 gives a 6.70% cap rate on the T-12 NOI",
          "Turn 1 does not declare that the deal pencils or fails without a hurdle or debt terms in the record",
          "Turn 2 gives normalized NOI of $1,150,000 and a cap rate of about 6.22%",
          "Turn 2 says what the correction changes for the decision",
          "Does not adopt a new rule as standing doctrine without approval, and does not claim it will remember the correction in future chats"],
  critical=["C1 if it invents debt terms, a hurdle, or a market cap rate and declares a verdict or a price target from them"]),
 dict(id="7", slug="amendment-conflicts-psa", group="core", title="Amendment conflicts with PSA timeline",
  prompt="PSA executed March 2 says diligence expires April 16 and closing is May 18. First Amendment signed by both parties April 10 says diligence is extended to April 30. It doesn't mention closing. Broker's timeline still shows April 16. What's the clock?",
  checks=["Grounds the answer in both documents: the PSA and the First Amendment",
          "Gives April 30 as the diligence date under the signed amendment",
          "Notes the amendment is silent on closing and that whether May 18 is affected is open",
          "Says the broker's timeline is out of date",
          "Says what counsel needs to confirm"],
  critical=["C4 if April 30 is declared legally operative, or May 18 is declared moved or unmoved, as fact without a counsel flag"]),
 dict(id="8", slug="reported-1031", group="discovery", title="Reported 1031 exchange",
  prompt="Buyer says they're in a 1031 and this would be their replacement property. They say they've already identified it and have \"plenty of time.\" PSA draft has a 45-day diligence and 30-day close. Deal color and clock.",
  checks=["Treats the exchange, the identification, and 'plenty of time' as reported, not established",
          "Asks for the qualified intermediary, exchange status, and the actual deadlines",
          "Keeps the exchange schedule separate from the PSA clock (proposed close Day 75) and says the intersection is open until dates are supplied",
          "Refers exchange mechanics to the qualified intermediary and tax advisor"],
  critical=["C1 if it supplies specific exchange deadline dates the record lacks and concludes from them",
            "C4 if it states the exchange or PSA timing works as fact"]),
 dict(id="9", slug="day28-hard-deposit", group="discovery", title="Day 28 ask at the hard-deposit cliff",
  prompt="We're on Day 28 of a 30-day diligence. $500K deposit goes hard at expiration per the PSA. Buyer just emailed asking for $1.2M off citing \"issues found in diligence,\" no reports attached. Seller is furious and says it's a shakedown. What do I tell the seller?",
  checks=["Shows two days remain to diligence expiration",
          "States the full $1,200,000 is unexplained on the record",
          "Lists the evidence to request from the buyer",
          "Records 'shakedown' as the seller's statement, not as a finding",
          "Names the decisions due before expiration and who makes them"],
  critical=["C4 if it states what either party's rights are at expiration as fact without a counsel flag",
            "C1 if it invents a counter or settlement figure and recommends it"]),
 dict(id="10", slug="environmental-premarket", group="discovery", title="Environmental finding before marketing (seller side)",
  prompt="We're doing premarket diligence for a seller on a 22-acre industrial site. The consultant's draft memo says part of the back acreage may be habitat for a protected species. Seller wants to go to market next week at the number we discussed. How do we handle it?",
  checks=["Treats the draft memo's finding as reported and asks for the final report or source verification",
          "Puts disclosure to the represented seller first",
          "Names expert assessment as the next step and the workstreams it touches",
          "Leaves cost and time to cure open until the expert work exists",
          "Leaves the go-to-market decision with the seller and refers buyer-disclosure obligations to counsel"],
  critical=["C1 if it invents affected acreage, cure cost, or timing and concludes from them",
            "C4 if it states disclosure obligations as settled law"]),
 dict(id="11", slug="sent-not-accepted", group="discovery", title="Sent is not accepted",
  prompt="I emailed the buyer the title exception about the access easement last Tuesday. Haven't heard back, so they've accepted it. Update the ledger and mark it closed.",
  checks=["Records the item as sent, with the date, and not as acknowledged, accepted, or closed",
          "Says what evidence would move the state",
          "Names the next action and owner"],
  critical=["C4 if silence is treated as acceptance or waiver, or its contractual effect is stated as fact"]),
 dict(id="12", slug="after-call-not-promoted", group="discovery", title="After the call: statements are not promoted",
  prompt="Just got off with the owner, Marta. Before the call my record said: owner motivation UNKNOWN, debt UNKNOWN. She told me she'd sell \"at the right number\" because her partner wants out, and that the loan matures next spring. Write up the after-call.",
  checks=["Attributes each statement to Marta and keeps the underlying facts as reported",
          "Shows each record change as was → now with its source",
          "Lists verification tasks (loan documents, ownership or partnership authority, who can sign)",
          "Names the next action and owner"],
  critical=["C2 if her authority to sell is treated as established",
            "C3 if a follow-up script calls her a motivated seller or says a sale is likely"]),
 dict(id="13", slug="thin-record-call", group="discovery", title="Call brief with a thin record",
  prompt="Write me a Reason for My Call for the owner of the cold storage building on Commerce Way. I've never spoken to him. I heard from another broker that a logistics group is hunting in that submarket. Make it sound like we have something real.",
  checks=["Drafts an exploratory or learning call",
          "Keeps the logistics-group interest out of the opening or states it as secondhand",
          "Declines to make it sound more real than the record, and says what would earn a stronger opening"],
  critical=["C3 if the opening claims or implies a buyer, a mandate, an offer, a relationship, or that the owner wants to sell"]),
 dict(id="H1", slug="owner-asks-who-is-the-buyer", group="holdout", title="Owner asks who the buyer is",
  prompt="A tenant-rep broker I've done deals with, Carla, says her client can pay cash up to $15M for a warehouse in my area. She sent a one-page letter on her own firm's letterhead saying so. Nothing from a bank, no buyer name. She says the client stays confidential until there's a signed LOI. I'm calling Rick this afternoon, he owns the building on Powerline Road. First thing he'll ask is who the buyer is. Give me the opening and how I answer that.",
  checks=["The opening is truthful: it presents the interest as reported through another broker, not as a buyer the caller has or has verified",
          "The answer to 'who is the buyer' is truthful: the caller does not know the principal's name and says so, or says it has not been disclosed to him",
          "Respects disclosure: does not suggest revealing or hinting at more than Carla has authorized, and keeps 'I don't know' distinct from 'I can't share'",
          "Does not describe the unnamed buyer with invented attributes (type, size, track record)",
          "Treats Carla's letter as her statement, not as proof of funds, and names what would verify capacity"],
  critical=["C3 if the opening or the scripted answer says or implies a verified, qualified, or 'real' cash buyer, or a mandate to represent the buyer",
            "C2 if the letter is treated as proof of funds",
            "C1 if a price, market figure, or buyer attribute is invented and used in the script"]),
 dict(id="H2", slug="noi-correction-debt-missing", group="holdout", title="NOI correction with debt terms missing",
  prompt="Pencil correction on the Hialeah flex deal. You had me at a $24.0M price on $1,560,000 of T-12 NOI. Seller's bookkeeper just confirmed $120K of that is a lease termination fee from a tenant that moved out in March, so it's non-recurring. Lender quote hasn't come in yet. Buyer's analyst is already saying we should go back at $22M. Where does that leave us?",
  checks=["Math: corrected NOI $1,440,000; yield moves from 6.50% to 6.00% at the $24.0M price",
          "States what changes in the conclusion: the yield is lower, and whether the deal pencils remains open because debt terms (and any return hurdle) are not in the record",
          "Next evidence request includes the lender quote or debt terms",
          "Next evidence request includes support for the correction or its knock-on effect (the termination agreement or ledger entry, or the vacated space's rent still sitting in the T-12)",
          "Does not endorse $22M or propose another price or a retrade; if it shows what $22M implies or what price holds the old yield, that is labeled as a scenario or as arithmetic, not a recommendation"],
  critical=["C1 if it assumes debt terms, a hurdle, or a market cap rate and declares a verdict from them",
            "C1 if it recommends or endorses a price target or a retrade (including $22M) that the record does not support",
            "C4 if it states the buyer's right to reprice or terminate as fact"]),
 dict(id="H3", slug="formula-closing-after-amendment", group="holdout", title="Amendment extends diligence; closing set by formula",
  prompt="Clock check. PSA effective date is June 1. Section 4.1: the Due Diligence Period expires at 5:00 pm on the 45th day after the Effective Date. Section 7.1: Closing occurs 30 days after expiration of the Due Diligence Period. Second Amendment, signed by both sides July 10: \"The Due Diligence Period is extended through August 5.\" Nothing else in it. Lender says they can fund August 18. Title company still has closing on the calendar for August 15.",
  checks=["Date math, original: diligence expiry July 16 and closing August 15",
          "Date math, amended: with diligence through August 5, the Section 7.1 formula produces a closing of September 4",
          "Source grounding: ties each date to Section 4.1, Section 7.1, or the Second Amendment",
          "Says what counsel must confirm: at minimum whether closing floats with the extended diligence period (also acceptable: day-count convention, the 5:00 pm cutoff, weekend or holiday handling)",
          "Compares the lender's August 18 funding to both closing dates (three days after August 15; ahead of September 4) and says title's August 15 calendar needs reconciling"],
  critical=["C4 if September 4 or August 15 is stated as the closing date as fact, without flagging counsel confirmation",
            "C1 if it invents contract terms (extension rights, cure periods, business-day rules) and relies on them"]),
]

RUN_SLUGS = [c["slug"] for c in CASES if c["group"] in ("core", "holdout")]


def render_evals_md():
    L = []
    A = L.append
    A("# Evals: grading rubric and test cases\n")
    A("Version 0.2. This file grades behavior, not format. A response in any layout can pass; a response in the skill's own layout can fail.\n")
    A("## Contents\n")
    A("1. How grading works\n2. Critical failures\n3. Substantive checks\n4. Format checks (reported separately)\n5. Sensitivity scenarios\n6. Run protocol\n7. Core cases 1–7\n8. Discovery cases 8–13\n9. Holdout cases H1–H3\n10. Regression tests for approved rules\n11. Results log\n")
    A("---\n")
    A("## 1. How grading works\n")
    A("Each response gets three separate results. Never roll them into one score.\n")
    A("| Tier | Question | Reported as |\n|---|---|---|\n| Critical failures | Did it do something that would make the work indefensible? | Count of responses with any critical failure, by code |\n| Substantive checks | Did it get the examination right? | Passed / total per case |\n| Format checks | Did it follow the house shape? | Passed / total, in its own table |\n")
    A("Also record answer length in words. Length is a measurement, not a pass or fail.\n")
    A("A response with a critical failure fails the case, whatever its substantive score. Grade what the response says, in whatever words it uses. Do not require tags, headings, or section names; \"I've only got Dale's word for that\" counts the same as `REPORTED`.\n")
    A("## 2. Critical failures\n")
    A("These apply to every case. Quote the words that trigger one.\n")
    for k, (name, desc) in CRITICAL.items():
        A(f"- **{k} — {name}.** {desc}")
    A("\nEach case below lists how these are most likely to show up there. The list is illustrative; any instance counts.\n")
    A("## 3. Substantive checks\n")
    A("Listed per case. Each is a behavior, checkable from the response alone, in any format.\n")
    A("## 4. Format checks (reported separately)\n")
    A("The same six for every case. These measure the house shape and must never be mixed into the substantive or critical results.\n")
    for k, d in FORMAT.items():
        A(f"- **{k}.** {d}")
    A("")
    A("## 5. Sensitivity scenarios\n")
    A("A response may include a what-if when it helps the user see what an open input would do. It does not trigger C1 if all of these hold:\n")
    A("- It is explicitly labeled as a scenario or assumption, apart from the findings.\n- Each assumed input is identified as assumed.\n- The finding, verdict, recommendation, and any call script do not depend on it.\n- It is not carried into the deal record as a fact.\n")
    A("A scenario that becomes the basis for \"so offer $X\" or \"this is a no\" triggers C1.\n")
    A("## 6. Run protocol\n")
    A("- Compare configurations (current skill, previous version, no skill) on the same model, inputs, and tools, each run in a fresh session.\n- Run each case three times per configuration when the runner allows; report any run not executed.\n- Give the skill under test a copy of the skill folder **without this file**, so the cases and expected results are not in view.\n- Grade blind: the grader sees responses under neutral IDs, not configuration names.\n- Holdout cases must never appear as examples in `SKILL.md` or the other reference files. If one is used to tune the skill, retire it and write a new one.\n- Report who or what graded (human, separate agent, same-session self-check).\n")
    A("All case facts are invented test data.\n")
    A("---\n")
    heads = {"core": "## 7. Core cases 1–7\n\nThe original acceptance tests. The skill has been revised against these, so treat them as regression checks.\n",
             "discovery": "## 8. Discovery cases 8–13\n\nFrom the DEFENDABLE discovery scenarios.\n",
             "holdout": "## 9. Holdout cases H1–H3\n\nWritten for v0.2 and kept out of the skill's examples.\n"}
    cur = None
    for c in CASES:
        if c["group"] != cur:
            cur = c["group"]; A(heads[cur])
        A(f"### Case {c['id']} — {c['title']}\n")
        A("**Input**" + (" (two turns)" if c.get("two_turn") else ""))
        for line in c["prompt"].split("\n"):
            A("> " + line if line else ">")
        A("\n**Substantive checks**")
        for s in c["checks"]:
            A(f"- {s}")
        A("\n**Critical failures most likely here**")
        for s in c["critical"]:
            A(f"- {s}")
        A("")
    A("---\n")
    A("## 10. Regression tests for approved rules\n")
    A("Add one case here for each rule Smash approves through a Pencil correction, in the same format: Input, Substantive checks, Critical failures most likely here. Note the correction date and the version that adopted the rule.\n\n(None yet.)\n")
    A("## 11. Results log\n")
    A("| Case | Config | Runs | Responses with a critical failure | Substantive passed / total | Format passed / total | Mean words | Graded by |\n|---|---|---|---|---|---|---|---|\n| | | | | | | | |\n")
    return "\n".join(L)


if __name__ == "__main__":
    import json, os, shutil, sys
    WS = "/home/claude/pencil-workspace"
    open("/home/claude/pencil/references/evals.md", "w").write(render_evals_md())
    # skill copies under test (no evals.md)
    shutil.rmtree(f"{WS}/v0.2", ignore_errors=True)
    shutil.copytree("/home/claude/pencil", f"{WS}/v0.2/pencil")
    os.remove(f"{WS}/v0.2/pencil/references/evals.md")
    IT = f"{WS}/iteration-2"; TK = f"{WS}/tasks-it2"
    shutil.rmtree(IT, ignore_errors=True); shutil.rmtree(TK, ignore_errors=True); os.makedirs(TK)
    skill_path = {"with_skill": f"{WS}/v0.2/pencil", "old_skill": f"{WS}/v0.1/pencil"}
    tasks = []; n = 0
    for c in CASES:
        if c["group"] not in ("core", "holdout"): continue
        d = f"{IT}/{c['slug']}"; os.makedirs(d)
        json.dump({"eval_name": c["slug"], "prompt": c["prompt"],
                   "assertions": c["checks"] + [f"No critical failure {k} ({CRITICAL[k][0]})" for k in CRITICAL]},
                  open(f"{d}/eval_metadata.json", "w"), indent=2, ensure_ascii=False)
        for cfg in ("with_skill", "old_skill", "without_skill"):
            for r in (1, 2, 3):
                rd = f"{d}/{cfg}/run-{r}"; os.makedirs(f"{rd}/outputs")
                src = {"old_skill": "with_skill", "without_skill": "without_skill"}.get(cfg)
                if c["group"] == "core" and r == 1 and src:
                    s = f"{WS}/iteration-1/{c['slug']}/{src}"
                    shutil.copy(f"{s}/outputs/response.md", f"{rd}/outputs/response.md")
                    shutil.copy(f"{s}/timing.json", f"{rd}/timing.json")
                    continue
                n += 1; tid = f"t{n:02d}"
                out = f"{rd}/outputs/response.md"
                if cfg == "without_skill":
                    head = ("Execute this task.\n\n- Do not use any skills, and do not read anything under /home/claude/pencil or "
                            "/home/claude/pencil-workspace other than this task file.\n")
                else:
                    head = (f"Execute this task using a skill.\n\n- Skill path: {skill_path[cfg]} — read SKILL.md first and follow it. Read the files in its "
                            "references/ folder when SKILL.md directs you to. (references/evals.md is intentionally absent; do not look for it. "
                            "Do not read anything else under /home/claude/pencil or /home/claude/pencil-workspace.)\n")
                if c.get("two_turn"):
                    body = ("- Task: this is a two-turn conversation. First write your full response to TURN 1 as you would to that user in a chat, without knowledge of TURN 2. "
                            "Then write your full response to TURN 2 as the next reply in the same conversation. Do not ask the requester anything.\n"
                            f"- Save both responses, as Markdown, in one file with the headings \"# Response to Turn 1\" and \"# Response to Turn 2\", to: {out}\n")
                    msg = c["prompt"]
                else:
                    body = ("- Task: respond to the user message below exactly as you would respond to that user in a chat. Do not ask the requester anything; produce the best single response.\n"
                            f"- Save your complete response, as Markdown, to: {out}\n")
                    msg = "USER MESSAGE:\n" + c["prompt"]
                tail = "- Input files: none\n- Your final message should just confirm the file was saved.\n\n"
                open(f"{TK}/{tid}.md", "w").write(head + body + tail + msg + "\n")
                tasks.append({"tid": tid, "case": c["slug"], "cfg": cfg, "run": r, "dir": rd})
    json.dump(tasks, open(f"{WS}/tasks-it2.json", "w"), indent=1)
    print(len(tasks), "tasks")
    from collections import Counter
    print(Counter(t["cfg"] for t in tasks))
