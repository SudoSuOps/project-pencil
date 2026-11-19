#!/usr/bin/env python3
"""Pencil ledger tools.

Deterministic validation, alignment arithmetic, counting, rendering, hashing,
human-review gating, append-only export, and drift comparison for a Pencil
ledger (JSON). Standard library only. The same ledger file always produces
the same output.

Usage:
  pencil_ledger.py validate LEDGER.json
  pencil_ledger.py align    LEDGER.json
  pencil_ledger.py count    LEDGER.json
  pencil_ledger.py render   LEDGER.json [--full]
  pencil_ledger.py check    LEDGER.json RESPONSE.md
  pencil_ledger.py hash     LEDGER.json
  pencil_ledger.py review   LEDGER.json --reviewer NAME --date YYYY-MM-DD
  pencil_ledger.py export   LEDGER.json
  pencil_ledger.py drift    A.json B.json [C.json ...]
  pencil_ledger.py calc add-days YYYY-MM-DD N
  pencil_ledger.py calc days-between YYYY-MM-DD YYYY-MM-DD
  pencil_ledger.py calc ratio NUMERATOR DENOMINATOR
  pencil_ledger.py calc sum-products "QTY*AMOUNT" ["QTY*AMOUNT" ...]
"""
import argparse
import datetime as dt
import hashlib
import json
import re
import sys

SCHEMA = "pencil-ledger/0.4"
STATES = ("VERIFIED", "NOT_VERIFIED", "UNKNOWN")
KINDS = ("NOT_CHECKED", "DOES_NOT_HOLD")
CHECKED_BY = ("pencil", "third_party", "owner_of_fact")
ANCHOR_MATCH = ("SAME", "DIFFERENT", "UNKNOWN")
REVIEW = ("DRAFT", "REVIEWED")

CATEGORY = {
    "property": "Property", "fin": "Stated financials", "party": "Parties",
    "capital": "Capital", "terms": "Terms", "cast": "Cast and time",
    "exchange": "Exchange", "x": "Other",
}
VOCAB = {
    "property": ["ownership", "title", "survey", "environmental", "condition", "unit_count", "square_feet"],
    "fin": ["unit_mix", "occupancy", "rent", "other_income", "expenses", "taxes", "insurance", "noi",
            "one_time_items", "lease_terms", "tenants", "price_reduction"],
    "party": ["buyer_identity", "buyer_role", "buyer_authority", "buyer_funds", "buyer_track_record",
              "buyer_strategy", "buyer_conditions", "seller_identity", "seller_authority",
              "seller_consents", "seller_conditions"],
    "capital": ["source", "lender_type", "borrower", "stage", "terms", "conditions", "timeline", "expiry", "equity"],
    "terms": ["price", "diligence", "deposit", "deposit_hard", "psa_delivery", "closing", "contingencies",
              "extension", "day_count", "anchor", "assignment"],
    "cast": ["counsel_timeline", "title_timeline", "inspection_timeline", "environmental_timeline",
             "survey_timeline", "calendar"],
    "exchange": ["involved", "leg", "dependency", "intermediary", "deadlines", "fit"],
}
# Words that signal judgment instead of a checked fact. Not allowed in a result line.
HEDGES = ["probably", "likely", "unlikely", "appears", "seems", "presumably", "typically",
          "usually", "perhaps", "maybe", "i think", "in my view"]
MOTIVE = ["retrade", "re-trade", "bad faith", "shakedown", "anchoring", "leverage", "motivated",
          "shaky", "good deal", "bad deal"]
# Required objects per kind of work. Every key must have an entry, in whatever state the record supports.
PROFILES = {
    "loi": ["terms.anchor", "terms.day_count", "terms.diligence", "terms.deposit_hard", "terms.psa_delivery",
            "terms.closing", "capital.stage", "capital.timeline", "party.buyer_funds", "party.buyer_authority",
            "exchange.involved"],
    "financials": ["fin.unit_mix", "fin.occupancy", "fin.rent", "fin.lease_terms", "fin.expenses", "fin.noi"],
}
KEY_RE = re.compile(r"^([a-z]+)\.([a-z0-9_]+)(:[a-z0-9_\-]+)?$")


# ---------- helpers ----------

def load(path):
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def canon(obj):
    return json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=False)


def sha(text):
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def content_hash(led):
    core = {k: led.get(k) for k in ("schema", "subject", "owner", "recipients", "stage", "as_of", "profiles", "entries", "alignments")}
    return sha(canon(core))


def active_entries(led):
    superseded = {e.get("supersedes") for e in led.get("entries", []) if e.get("supersedes")}
    return [e for e in led.get("entries", []) if e.get("id") not in superseded]


def nonempty(v):
    return isinstance(v, str) and v.strip() != ""


# ---------- validation ----------

def validate(led):
    """Return (errors, warnings). Errors make the ledger unusable."""
    E, W = [], []
    if led.get("schema") != SCHEMA:
        E.append(f"schema must be '{SCHEMA}'")
    for f in ("subject", "owner", "as_of"):
        if not nonempty(led.get(f)):
            E.append(f"'{f}' is required")
    if not isinstance(led.get("recipients"), list):
        E.append("'recipients' must be a list (may be empty)")
    try:
        dt.date.fromisoformat(str(led.get("as_of")))
    except ValueError:
        E.append("'as_of' must be YYYY-MM-DD")

    rev = led.get("review") or {}
    if rev.get("status") not in REVIEW:
        E.append("review.status must be DRAFT or REVIEWED")
    elif rev.get("status") == "REVIEWED":
        if not nonempty(rev.get("reviewer")) or not nonempty(rev.get("date")):
            E.append("REVIEWED requires review.reviewer and review.date")
        if rev.get("hash") != content_hash(led):
            E.append("ledger changed since human review; set review.status back to DRAFT and have it reviewed again")

    entries = led.get("entries")
    if not isinstance(entries, list) or not entries:
        E.append("'entries' must be a non-empty list")
        entries = []
    ids = [e.get("id") for e in entries]
    if len(set(ids)) != len(ids):
        E.append("entry ids must be unique")
    idset = set(ids)

    for e in entries:
        tag = f"entry {e.get('id', '?')}"
        if not nonempty(e.get("id")):
            E.append("every entry needs an id")
        m = KEY_RE.match(str(e.get("key", "")))
        if not m:
            E.append(f"{tag}: key must look like 'terms.closing' or 'cast.counsel_timeline:seller'")
        else:
            prefix, name = m.group(1), m.group(2)
            if prefix not in CATEGORY:
                E.append(f"{tag}: unknown key prefix '{prefix}'")
            elif prefix != "x" and name not in VOCAB[prefix]:
                W.append(f"{tag}: key '{e['key']}' is outside the fixed vocabulary; use an existing key or the 'x.' prefix")
        if not nonempty(e.get("object")):
            E.append(f"{tag}: 'object' is required")
        state = e.get("state")
        if state not in STATES:
            E.append(f"{tag}: state must be one of {', '.join(STATES)}")
        stated, ev = e.get("stated"), e.get("evidence")
        if stated is not None:
            if not nonempty(stated.get("value")) or not nonempty(stated.get("source")):
                E.append(f"{tag}: stated needs 'value' and 'source'")
        if ev is not None:
            if not nonempty(ev.get("source")):
                E.append(f"{tag}: evidence needs 'source'")
            if ev.get("checked_by") not in CHECKED_BY:
                E.append(f"{tag}: evidence.checked_by must be one of {', '.join(CHECKED_BY)}")
            if not nonempty(ev.get("checker")):
                E.append(f"{tag}: evidence needs 'checker' (who did the checking)")
            if not isinstance(ev.get("seen_by_pencil"), bool):
                E.append(f"{tag}: evidence.seen_by_pencil must be true or false")
            if ev.get("checked_by") == "pencil" and ev.get("seen_by_pencil") is not True:
                E.append(f"{tag}: checked_by 'pencil' requires seen_by_pencil true; a document that was only described was not checked by Pencil")
        if state == "VERIFIED":
            if stated is None:
                E.append(f"{tag}: VERIFIED needs a stated claim to verify")
            if ev is None:
                E.append(f"{tag}: VERIFIED needs evidence")
            if e.get("kind") is not None:
                E.append(f"{tag}: 'kind' applies only to NOT_VERIFIED")
        elif state == "NOT_VERIFIED":
            if e.get("kind") not in KINDS:
                E.append(f"{tag}: NOT_VERIFIED needs kind NOT_CHECKED or DOES_NOT_HOLD")
            if stated is None:
                E.append(f"{tag}: NOT_VERIFIED needs a stated claim; if nothing was stated, the state is UNKNOWN")
            if e.get("kind") == "DOES_NOT_HOLD" and ev is None:
                E.append(f"{tag}: DOES_NOT_HOLD needs the evidence that contradicts the statement")
            if e.get("kind") == "NOT_CHECKED" and not nonempty(e.get("needs")):
                E.append(f"{tag}: NOT_CHECKED needs 'needs': what would verify it and what that lets the parties decide")
        elif state == "UNKNOWN":
            if not nonempty(e.get("needs")):
                E.append(f"{tag}: UNKNOWN needs 'needs': the missing fact and what it lets the parties decide")
            if e.get("kind") is not None:
                E.append(f"{tag}: 'kind' applies only to NOT_VERIFIED")
        if not nonempty(e.get("result")):
            E.append(f"{tag}: 'result' is required (one line: what the check showed)")
        else:
            low = e["result"].lower()
            for w in HEDGES:
                if re.search(r"\b" + re.escape(w) + r"\b", low):
                    E.append(f"{tag}: result uses '{w}'. State what was checked; if it is not settled, the state is UNKNOWN")
            for w in MOTIVE:
                if re.search(r"\b" + re.escape(w) + r"\b", low):
                    E.append(f"{tag}: result uses '{w}'. The ledger records what was stated and verified, not motive or judgment")
            if re.search(r"\d+\s*%\s*(chance|probab|likel|odds)", low):
                E.append(f"{tag}: result states a percentage probability; report counts, not odds")
        sup = e.get("supersedes")
        if sup is not None and sup not in idset:
            E.append(f"{tag}: supersedes '{sup}', which is not in the ledger. Superseded entries are kept, never deleted")

    profiles = led.get("profiles", [])
    if not isinstance(profiles, list) or any(p not in PROFILES for p in profiles):
        E.append(f"'profiles' must be a list drawn from: {', '.join(PROFILES)}")
    else:
        have = {str(e.get("key", "")).split(":")[0] for e in active_entries(led)}
        for p in profiles:
            for k in PROFILES[p]:
                if k not in have:
                    E.append(f"profile '{p}' requires an entry for {k}; if nothing was stated or supplied, log it as UNKNOWN")

    for a in led.get("alignments", []) or []:
        tag = f"alignment {a.get('id', '?')}"
        for f in ("id", "key", "term", "party"):
            if not nonempty(a.get(f)):
                E.append(f"{tag}: '{f}' is required")
        for f in ("stated_days", "required_days"):
            if not isinstance(a.get(f), int) or isinstance(a.get(f), bool) or a.get(f) < 0:
                E.append(f"{tag}: '{f}' must be a whole number of days")
        for f in ("stated_entry", "required_entry"):
            if a.get(f) not in idset:
                E.append(f"{tag}: '{f}' must be the id of a ledger entry")
        if a.get("anchor_match") not in ANCHOR_MATCH:
            E.append(f"{tag}: anchor_match must be SAME, DIFFERENT, or UNKNOWN")
        comps = a.get("components") or []
        for c in comps:
            if not nonempty(c.get("name")) or not isinstance(c.get("days"), int) or not isinstance(c.get("adjustable"), bool):
                E.append(f"{tag}: each component needs name, whole-number days, and adjustable true/false")
        if comps and all(isinstance(c.get("days"), int) for c in comps) and isinstance(a.get("stated_days"), int):
            if sum(c["days"] for c in comps) != a["stated_days"]:
                E.append(f"{tag}: components must add up to stated_days")
    return E, W


# ---------- alignment ----------

def compute_alignment(a, by_id):
    """Pure arithmetic. No cushion, no rounding, no preference."""
    req = by_id.get(a["required_entry"], {})
    stated_days, required_days = a["stated_days"], a["required_days"]
    diff = stated_days - required_days
    out = {"id": a["id"], "key": a["key"], "term": a["term"], "party": a["party"],
           "stated_days": stated_days, "required_days": required_days,
           "difference_days": diff, "anchor_match": a["anchor_match"],
           "required_state": req.get("state"), "cure": None, "cure_text": None, "notes": []}
    if req.get("state") != "VERIFIED":
        out["status"] = "NOT_ALIGNED_AS_STATED" if diff < 0 else "ALIGNED_AS_STATED"
        out["notes"].append(f"{a['party']}'s requirement is not verified; verify it with {a['party']} before any cure is stated")
        return out
    if a["anchor_match"] == "DIFFERENT":
        out["status"] = "ANCHORS_DIFFER"
        out["notes"].append("the two periods run from different events; they cannot be compared until both are restated from the same event")
        return out
    if diff >= 0:
        out["status"] = "ALIGNED"
    else:
        out["status"] = "NOT_ALIGNED"
        comps = a.get("components") or []
        adjustable = [c for c in comps if c["adjustable"]]
        fixed_sum = sum(c["days"] for c in comps if not c["adjustable"])
        if not comps:
            out["cure"] = {"total_days": required_days}
            out["cure_text"] = f"{a['term']} at {required_days} days, other stated terms unchanged."
        elif len(adjustable) == 1 and required_days - fixed_sum >= 0:
            new = required_days - fixed_sum
            c = adjustable[0]
            out["cure"] = {"total_days": required_days, "component": c["name"], "from_days": c["days"], "to_days": new}
            kept = ", ".join(f"{x['name']} {x['days']} days as stated" for x in comps if not x["adjustable"])
            out["cure_text"] = (f"{kept + ', then ' if kept else ''}{c['name']} {new} days, for {required_days} days in total.")
        else:
            out["cure"] = {"total_days": required_days}
            out["cure_text"] = (f"Constraint: {a['term']} no earlier than Day {required_days}. "
                                "More than one arrangement satisfies it; the parties choose.")
    if a["anchor_match"] == "UNKNOWN":
        out["notes"].append("whether both periods run from the same event is not confirmed; for counsel")
    return out


def alignments(led):
    by_id = {e["id"]: e for e in led.get("entries", [])}
    return [compute_alignment(a, by_id) for a in led.get("alignments", []) or []]


# ---------- counts ----------

def counts(led):
    act = active_entries(led)
    al = alignments(led)
    disc = {e["key"] for e in act if e.get("kind") == "DOES_NOT_HOLD"}
    disc |= {e["key"] for e in act if e.get("omitted_from_documents") is True}
    disc |= {a["key"] for a in al if a["status"] == "NOT_ALIGNED"}
    return {
        "objects": len(act),
        "verified": sum(1 for e in act if e["state"] == "VERIFIED"),
        "not_verified": sum(1 for e in act if e["state"] == "NOT_VERIFIED"),
        "not_checked": sum(1 for e in act if e.get("kind") == "NOT_CHECKED"),
        "does_not_hold": sum(1 for e in act if e.get("kind") == "DOES_NOT_HOLD"),
        "unknown": sum(1 for e in act if e["state"] == "UNKNOWN"),
        "discoveries": len(disc),
        "superseded": len(led.get("entries", [])) - len(act),
    }


# ---------- rendering ----------

def state_label(e):
    if e["state"] == "NOT_VERIFIED":
        return "NOT VERIFIED (" + ("not checked" if e["kind"] == "NOT_CHECKED" else "checked; does not hold") + ")"
    return e["state"]


def checked_label(ev):
    if ev is None:
        return "—"
    who = {"pencil": f"read by {ev['checker']}",
           "third_party": f"checked by {ev['checker']}" + ("" if ev["seen_by_pencil"] else ", not seen by Pencil"),
           "owner_of_fact": f"stated by {ev['checker']} about its own position"}[ev["checked_by"]]
    return f"{ev['source']} ({who})"


def cell(s):
    return str(s).replace("|", "\\|").replace("\n", " ")


def render(led, full=False):
    c, al, rev = counts(led), alignments(led), led["review"]
    L = []
    L.append(f"# LEDGER — {led['subject']}")
    L.append(f"Owner: {led['owner']} | Authorized recipients: {', '.join(led['recipients']) or 'none named'} | "
             f"As of: {led['as_of']}" + (f" | Stage: {led['stage']}" if led.get("stage") else ""))
    if rev["status"] == "REVIEWED":
        L.append(f"Review: REVIEWED by {rev['reviewer']} on {rev['date']}")
    else:
        L.append("Review: DRAFT. Not reviewed by a human. Not for release.")
    L.append("")
    L.append("## Count")
    L.append(f"{c['objects']} objects: {c['verified']} verified, {c['not_verified']} not verified "
             f"({c['not_checked']} not checked, {c['does_not_hold']} do not hold), {c['unknown']} unknown. "
             f"Discoveries open: {c['discoveries']}.")
    L.append("")

    disc_entries = [e for e in active_entries(led) if e.get("kind") == "DOES_NOT_HOLD" or e.get("omitted_from_documents") is True]
    short = [a for a in al if a["status"] in ("NOT_ALIGNED", "NOT_ALIGNED_AS_STATED", "ANCHORS_DIFFER")]
    if disc_entries or short:
        L.append("## Discoveries")
        for e in disc_entries:
            st = e["stated"]
            if e.get("omitted_from_documents") is True and e.get("kind") != "DOES_NOT_HOLD":
                L.append(f"- **{e['object']}** — not addressed in the documents. Stated: {st['value']} [{st['source']}]. "
                         f"State: {state_label(e)}. Result: {e['result']}")
            else:
                L.append(f"- **{e['object']}** — Stated: {st['value']} [{st['source']}]. "
                         f"Verified: {checked_label(e['evidence'])}. Result: {e['result']}")
        L.append("")
    if al:
        L.append("## Alignment")
        L.append("| Term | Stated (days) | Party | Party requires (days) | Difference | Status |")
        L.append("|---|---|---|---|---|---|")
        for a in al:
            d = a["difference_days"]
            dtext = "0" if d == 0 else (f"{-d} short" if d < 0 else f"{d} to spare")
            L.append(f"| {cell(a['term'])} | {a['stated_days']} | {cell(a['party'])} | {a['required_days']} "
                     f"({'verified' if a['required_state'] == 'VERIFIED' else 'not verified'}) | {dtext} | {a['status'].replace('_', ' ')} |")
        for a in al:
            for n in a["notes"]:
                L.append(f"- {a['term']}: {n}.")
        L.append("")
        cures = [a for a in al if a["cure_text"]]
        L.append("## Cures supported by the evidence")
        if cures:
            for a in cures:
                L.append(f"- {a['term']}: aligned terms on the verified facts: {a['cure_text']}")
        else:
            L.append("- None. A cure is stated only when the governing fact is verified and the terms do not align.")
        L.append("")

    groups = {}
    for e in active_entries(led):
        groups.setdefault(e["key"].split(".")[0], []).append(e)
    if full:
        L.append("## Entries")
    else:
        ver = [e for e in active_entries(led) if e["state"] == "VERIFIED"]
        if ver:
            L.append("## Verified")
            for e in ver:
                L.append(f"- {e['object']}: {e['result']} [{checked_label(e['evidence'])}]")
            L.append("")
    for prefix in CATEGORY:
        if not full or prefix not in groups:
            continue
        L.append(f"### {CATEGORY[prefix]}")
        L.append("| Object | Stated (source) | Checked against | State | Result |")
        L.append("|---|---|---|---|---|")
        for e in groups[prefix]:
            st = e.get("stated")
            stated = f"{st['value']} [{st['source']}]" if st else "—"
            L.append(f"| {cell(e['object'])} | {cell(stated)} | {cell(checked_label(e.get('evidence')))} | {state_label(e)} | {cell(e['result'])} |")
        L.append("")

    opens = [e for e in active_entries(led) if e["state"] != "VERIFIED" and nonempty(e.get("needs"))]
    if opens:
        L.append("## Open: what would settle each")
        for e in opens:
            L.append(f"- {e['object']}: {e['needs']}")
        L.append("")
    if c["superseded"]:
        L.append(f"Superseded entries retained in the ledger file: {c['superseded']}.")
    L.append("This ledger is not a property disclosure and makes no recommendation on value or terms.")
    L.append(f"Ledger hash: {content_hash(led)[:16]}")
    return "\n".join(L)


# ---------- drift ----------

def fingerprint(led):
    """The facts of a ledger, without its wording."""
    fp = {"entries": {}, "alignments": {}}
    for e in active_entries(led):
        fp["entries"][e["key"]] = [e["state"], e.get("kind")]
    for a in alignments(led):
        cure = a["cure"] or {}
        # A period logged whole and the same period logged as one adjustable part are the same fact.
        part = cure.get("to_days") if cure.get("to_days") != cure.get("total_days") else None
        fp["alignments"][a["key"]] = [a["stated_days"], a["required_days"], a["difference_days"], a["status"],
                                      cure.get("total_days"), part]
    return fp


def drift(paths):
    fps = [(p, fingerprint(load(p))) for p in paths]
    base_p, base = fps[0]
    diffs = []
    for p, fp in fps[1:]:
        for section in ("entries", "alignments"):
            keys = sorted(set(base[section]) | set(fp[section]))
            for k in keys:
                a, b = base[section].get(k), fp[section].get(k)
                if a != b:
                    diffs.append(f"{'entry' if section == 'entries' else 'alignment'} {k}: {base_p} has {a}; {p} has {b}")
    return diffs


# ---------- CLI ----------

def main():
    ap = argparse.ArgumentParser(description="Pencil ledger tools")
    sub = ap.add_subparsers(dest="cmd", required=True)
    for name in ("validate", "align", "count", "hash", "export"):
        sub.add_parser(name).add_argument("ledger")
    rn = sub.add_parser("render"); rn.add_argument("ledger"); rn.add_argument("--full", action="store_true")
    ck = sub.add_parser("check"); ck.add_argument("ledger"); ck.add_argument("response")
    r = sub.add_parser("review")
    r.add_argument("ledger"); r.add_argument("--reviewer", required=True); r.add_argument("--date", required=True)
    d = sub.add_parser("drift"); d.add_argument("ledgers", nargs="+")
    c = sub.add_parser("calc"); c.add_argument("op", choices=["add-days", "days-between", "ratio", "sum-products"]); c.add_argument("args", nargs="+")
    a = ap.parse_args()

    if a.cmd == "calc":
        if a.op == "add-days":
            print((dt.date.fromisoformat(a.args[0]) + dt.timedelta(days=int(a.args[1]))).isoformat())
        elif a.op == "days-between":
            print((dt.date.fromisoformat(a.args[1]) - dt.date.fromisoformat(a.args[0])).days)
        elif a.op == "ratio":
            n, m = float(a.args[0]), float(a.args[1])
            print(f"{n / m * 100:.2f}%")
        else:
            total = 0.0
            for term in a.args:
                q, amt = term.split("*")
                total += float(q) * float(amt)
            print(f"{total:,.2f}")
        return 0

    if a.cmd == "drift":
        if len(a.ledgers) < 2:
            print("drift needs at least two ledgers"); return 2
        for p in a.ledgers:
            errs, _ = validate(load(p))
            if errs:
                print(f"INVALID {p}: " + "; ".join(errs)); return 2
        diffs = drift(a.ledgers)
        if diffs:
            print(f"DRIFT: {len(diffs)} difference(s) across {len(a.ledgers)} ledgers")
            for x in diffs:
                print(" - " + x)
            return 1
        print(f"NO DRIFT: {len(a.ledgers)} ledgers agree on every state, number, and cure")
        return 0

    led = load(a.ledger)
    if a.cmd == "review":
        led["review"] = {"status": "DRAFT"}
        errs, _ = validate(led)
        if errs:
            print("Cannot mark reviewed; ledger is invalid:"); [print(" - " + e) for e in errs]; return 2
        led["review"] = {"status": "REVIEWED", "reviewer": a.reviewer, "date": a.date, "hash": content_hash(led)}
        with open(a.ledger, "w", encoding="utf-8") as f:
            json.dump(led, f, indent=2, ensure_ascii=False)
        print(f"REVIEWED by {a.reviewer} on {a.date}. Hash {content_hash(led)[:16]}"); return 0

    errs, warns = validate(led)
    if a.cmd == "validate":
        for w in warns:
            print("WARNING: " + w)
        if errs:
            print(f"INVALID: {len(errs)} error(s)"); [print(" - " + e) for e in errs]; return 2
        print("VALID"); return 0
    if errs:
        print(f"INVALID: {len(errs)} error(s). Fix the ledger before using it."); [print(" - " + e) for e in errs]; return 2
    if a.cmd == "align":
        print(json.dumps(alignments(led), indent=2, ensure_ascii=False))
    elif a.cmd == "count":
        print(json.dumps(counts(led), indent=2))
    elif a.cmd == "render":
        print(render(led, full=a.full))
    elif a.cmd == "check":
        text = open(a.response, encoding="utf-8").read()
        want = [l for l in render(led).split("\n") if l.strip()]
        want_full = [l for l in render(led, full=True).split("\n") if l.strip()]
        missing = min(([l for l in w if l not in text] for w in (want, want_full)), key=len)
        if missing:
            print(f"MISMATCH: {len(missing)} rendered line(s) are not in the response. The response was not rendered from this ledger, or was altered.")
            for l in missing[:5]:
                print(" - " + l[:160])
            return 1
        print("MATCH: the response contains this ledger's render unchanged")
    elif a.cmd == "hash":
        print(content_hash(led))
    elif a.cmd == "export":
        prev = "0" * 64
        for i, e in enumerate(led["entries"], 1):
            rec = {"seq": i, "subject": led["subject"], "owner": led["owner"], "as_of": led["as_of"], "entry": e}
            h = sha(prev + canon(rec))
            print(json.dumps({**rec, "prev_hash": prev, "hash": h}, ensure_ascii=False, sort_keys=True))
            prev = h
    return 0


if __name__ == "__main__":
    sys.exit(main())
