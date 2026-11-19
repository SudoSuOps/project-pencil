# PencilBot Founding Blueprint

Version 1.0, 19 November 2026. Adopted as the project's founding document
on 2026-11-19 ("we lock it in"). Converted from the original Word file;
the wording is unchanged.

Three points in this blueprint differ from the skill as built and are held
open in `DOCTRINE.md` (open questions 9 to 11) until ruled on. Everything
else here is doctrine.

---

Working concept document • 19 November 2026 • Version 1.0

## CORE THESIS

The Pencil does not broker, negotiate, decide, or pretend to be an expert. It works alongside humans to trace information to its origin, test claims against evidence, preserve uncertainty, and produce a defensible record. The human discovers the color; the Pencil preserves and validates it.

# 1. Why Pencil Exists

The idea emerged from a transaction-first philosophy: a deal cannot be understood from its offering memorandum or spreadsheet alone. The meaningful discovery often happens through calls, clarification, and sustained collaboration. A 30-year dialer understands that “reason for my call” is not a slogan; it is how a missing fact becomes a useful question.

The aim is not a five-minute chatbot verdict. It is a calm, boring, organized participant in a working office, helping humans return to the record as circumstances evolve. Pencil makes the next call more informed, without making that call or substituting for the parties’ judgment.

# 2. The Problem

- Claims circulate without clear source of origin, authority, or custody.

- Offering memoranda, spreadsheets, verbal representations, and model outputs can conflict.

- A plausible AI answer can hide missing evidence, assumptions, or silent revisions.

- Deal teams lose context across calls, chats, documents, and time.

- Confidential information may cross organizational boundaries without adequate controls.

- Existing tools often optimize for speed of answer rather than auditability of discovery.

# 3. What Pencil Is — and Is Not

| Pencil is                                     | Pencil is not                                   |
|-----------------------------------------------|-------------------------------------------------|
| A human-partnered validation instrument       | A broker, negotiator, or investment adviser     |
| A persistent, scoped case record              | A chief of staff or marketing executive         |
| A software-defined role using code and models | A single model or a personality made of weights |
| An evidence and uncertainty tracker           | A superhero bot, autonomous swarm, or coin      |
| A tool that helps ask the next question       | A replacement for professional judgment         |

Identity: calm, methodical, patient, restrained, explicit about uncertainty. Authority: no independent transactional authority. Success: traceable, reproducible findings reviewed by an accountable human.

# 4. The Carfax Analogy — and Its Limit

Carfax is useful because it organizes a vehicle-history record; it does not sell the car or negotiate its price. Pencil applies the same discipline to information in a deal, shipment, system, or AI output. The analogy has a boundary: absence of a reported event does not prove the event never occurred. Likewise, a source document or matching hash does not prove the underlying claim is true.

Pencil should say “not established by the available record” when coverage is incomplete, not “verified clean.”

# 5. Farm-to-Table Provenance: Source to Passport

| Layer     | Question                                     | Required record                                               |
|-----------|----------------------------------------------|---------------------------------------------------------------|
| Origin    | Where did this claim begin?                  | Domain, publisher, person/system, source ID, captured time    |
| Integrity | Has the material changed?                    | Hash, versions, access/change history                         |
| Authority | Is the source competent to assert this?      | Role, permission, credential or official status when relevant |
| Accuracy  | Does independent evidence support the claim? | Cross-checks, calculations, contradictions, limitations       |
| Custody   | Who handled or transmitted it?               | Ingestion, access, transformation, sharing events             |
| Review    | Who accepted the finding and on what scope?  | Reviewer, decision, timestamp, version                        |

A domain is an address, not proof of truth. A hash is evidence of byte integrity, not factual accuracy. “Verified” must always identify what was verified, against which source, at which time, and with what limits.

# 6. The Working Office: Human + Pencil

Pencil operates inside a permissioned virtual office with humans and specialized tools. Meetings, voice, chat, and deal rooms are collaboration channels, not permission to listen to or disclose everything. The human owns the relationship and any external communications. Pencil prepares questions, retrieves authorized evidence, tracks decisions, and flags conflicts.

## The Ring Ring Loop

- Open a scoped assignment with named participants, purpose, confidentiality restrictions, and evidence inventory.

- Human conducts discovery calls or meetings; Pencil participates only when authorized and appropriately disclosed.

- Capture claims with speaker/source attribution and timestamps; mark unconfirmed statements as such.

- Reconcile new claims against documents, calculations, and earlier statements.

- Generate precise follow-up questions; human chooses whether and how to ask them.

- Record replies and new evidence without overwriting history.

- Publish a revised validation status with human review and sign-off.

# 7. Findings: Black, White, and Grey

| Status       | Meaning                                                | Pencil response                                 |
|--------------|--------------------------------------------------------|-------------------------------------------------|
| Supported    | Evidence supports a narrowly stated claim              | Cite scope, evidence, method, date              |
| Contradicted | Evidence materially conflicts with a claim             | Show both sources and quantify discrepancy      |
| Unresolved   | Evidence is missing, ambiguous, stale, or insufficient | Specify missing proof and responsible follow-up |

Grey is not failure. It is an honest boundary. The parties decide how to act on the record. Pencil does not set a price, propose concessions, negotiate, or recommend that a transaction close.

# 8. Validator of Validators

Model-generated findings are provisional. Calculations should be re-run in deterministic code, extracted values checked against their source spans, and high-impact claims subjected to independent review. Agreement between two models is not independent proof if both share the same bad input.

- Source-grounded extraction with page, line, or record pointers.

- Deterministic arithmetic and reconciliation tests with reproducible inputs.

- Independent checker using a different method where feasible.

- Exception queue for conflicts, missing sources, and model uncertainty.

- Human sign-off on material findings and on publication.

- Versioned evaluation sets measuring false verification, missed contradiction, citation accuracy, and unauthorized disclosure.

# 9. The Pencil Passport

The deliverable is a living validation passport, not a generic score or investment recommendation. Every claim receives an ID, source lineage, method, status, uncertainty, reviewer, and revision history. The passport contains a source inventory, finding ledger, exception log, follow-up queue, and exportable evidence index.

## Illustrative CRE assignment — not a real transaction

| Item              | Example finding                                                                      |
|-------------------|--------------------------------------------------------------------------------------|
| Rent roll         | Reconciles to executed leases: supported within reviewed scope                       |
| NOI               | Seller reports \$5.2M; reviewed records indicate \$4.8M: discrepancy of \$400k       |
| Value sensitivity | At an assumed 6% cap rate, \$400k / 0.06 = ~\$6.67M; arithmetic only                 |
| Timeline          | LOI contemplates 60 days; financing indicates 90 days: unresolved execution conflict |
| Environmental     | Report pending: cannot verify environmental status                                   |

The human can call about the financing timeline or environmental documentation. Pencil updates the record when evidence arrives; the parties decide whether and how to proceed.

# 10. Confidentiality and Service Boundaries

- Tenant- and assignment-scoped access; least privilege and explicit information-sharing rules.

- NDA and retention obligations captured at intake; no automatic cross-party disclosure.

- Meeting recording/transcription only with applicable notice, consent, and organizational authorization.

- Encryption, audit logs, secure exports, access revocation, and incident procedures.

- Human approval before outbound communications, external sharing, or final publication.

- Counsel review of service descriptions, compensation structures, licensing exposure, and applicable regulated activities.

“We validate, we do not broker” is the intended service boundary, not an automatic legal conclusion. Actual conduct and compensation must match it.

# 11. Build Architecture

| Component                | Function                                                                 |
|--------------------------|--------------------------------------------------------------------------|
| Pencil identity contract | Stable role, authority limits, voice, escalation rules                   |
| Case & evidence store    | Immutable originals, claim IDs, provenance, versions, custody events     |
| Connectors               | Authorized document, chat, meeting, voice and deal-room ingestion        |
| Deterministic tools      | Parsers, calculators, reconciliation checks, policy checks               |
| Model adapter            | Replaceable model inference for language/extraction/reasoning assistance |
| Validation engine        | Source checks, contradictions, uncertainty, independent tests            |
| Human workspace          | Assignment queue, review, Ring Ring questions, approvals                 |
| Passport publisher       | Versioned reports, evidence links, scope and limitations                 |
| Evaluation harness       | Regression tests, drift checks, permission tests, error analysis         |

The model can change without changing Pencil’s identity. The identity contract alone cannot guarantee behavior; access controls, state machines, testing, and human checkpoints must enforce it.

# 12. Practical Build Sequence

## Phase 0 — Contract and boundaries

Freeze Pencil identity v1, allowed/disallowed actions, claim schema, evidence status taxonomy, and confidentiality threat model. Define measurable acceptance criteria before integration.

## Phase 1 — Text-only proof

One private assignment. Ingest a controlled set of CRE documents, preserve originals and hashes, reconcile rent roll/NOI, generate an exception ledger, and export Passport v0. Human reviews every finding.

## Phase 2 — Ring Ring collaboration

Add human-entered call notes, follow-up queue, attributed revisions, and controlled meeting transcript ingestion. Test whether each new conversation improves the record without erasing prior evidence.

## Phase 3 — Office and voice

Integrate permissioned chat, meeting/voice workflow, role-based rooms, and approval gates. Validate consent, transcript attribution, data isolation, and failure handling before live use.

## Phase 4 — Cross-domain skills

Retain one Pencil identity. Add separate tested validation packs for cold chain custody, infrastructure telemetry, AI answer provenance, and other domains. Domain experts approve domain-specific criteria.

## Phase 5 — Commercial pilot

Offer narrowly scoped paid validation assignments only after legal review and operational testing. Measure turnaround time, source coverage, material errors, customer corrections, repeatability, and human effort.

# 13. Non-Negotiable Acceptance Tests

- No verified status without an attributable source and specified validation method.

- No source modification without an audit event and preserved original.

- No confidential source shown to an unauthorized participant.

- No outbound call, message, or disclosure without human authorization.

- No silent conversion of assumption into fact.

- No unsupported claim that a model is drift-free.

- Every material finding can be reconstructed from stored evidence and calculations.

- Human can override a finding only with a recorded reason and preserved prior version.

# 14. Open Design Decisions

- Canonical claim and evidence schema, including source identity and confidence semantics.

- Whether the first pilot is a CRE asset, an LOI execution timeline, or a controlled synthetic deal room.

- Exact meeting/voice integrations and consent workflow.

- Which data remains on-premises and what external services, if any, are permitted.

- Reviewer roles, separation of duties, and dispute resolution for conflicting findings.

- Passport format, external verification access, and retention schedule.

- Commercial service scope and pricing after counsel review.

# 15. Founding Language

PencilBot.ai — Source-to-Decision Validation.

We do not bring you a buyer. We do not bring you a seller. We do not negotiate your deal. We bring the Pencil. Human experience. Machine intelligence. Independent validation. Black and white where the evidence supports it. Grey where it does not. The decisions remain yours.

The AI does not make the call. The human does not have to work alone.

Ring Ring. Reason for my call? We have the report. We are validating its source.

ONE PENCIL. MANY DOMAINS. EVERY CLAIM ACCOUNTABLE TO ITS ORIGIN.

Document status: Concept and implementation blueprint derived from the November 19, 2026 Pencil discussion. Architecture and service design are proposed, not represented as deployed or independently validated.
