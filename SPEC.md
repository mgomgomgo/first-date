# First Date — Product & Protocol Specification

**Status:** Draft for community review  
**Version:** 0.2.0 (design iteration)  
**Tagline:** **AI can only multiply what it understands.**  
**License:** MIT

## 1. Vision

First Date is an open, portable protocol that helps AI assistants develop an accurate, useful, evolving understanding of the people they work with.

Most AI interactions begin with a task. First Date makes room for understanding the person behind that task. Its goal is to improve human judgment and capability, not replace either.

**Mission:** Turn context from an accidental byproduct of chats into a user-controlled foundation for better AI collaboration.

**Guiding principle:** Understand before assuming. Learn without intruding. Remember with permission. Evolve through experience.

## 2. Problem

AI assistants are powerful but often lack context about users' working styles, priorities, goals, preferences, and constraints. This leads to generic responses, repeated explanations, and poor continuity.

Context exists in fragmented places: chat history, user memory, global instructions, project instructions, and session prompts. More memory alone isn't enough: information may be stale, sensitive, inferred incorrectly, or shared too broadly.

First Date prioritizes **relevant, trustworthy, permissioned context**.

## 3. Scope

### Goals
1. A natural introduction instead of a rigid survey.
2. An editable global user-context profile.
3. Project profiles that inherit only authorized, relevant global details.
4. Explicit invocation and optional context clarification during supported active interactions.
5. Consent-based maintenance, corrections, audits, and exports.
6. Host-agnostic instructions with optional platform-specific adapters.

### Non-goals for v0.1
- Hosted database, account service, or telemetry.
- Background monitoring or guaranteed automatic invocation.
- Guaranteed memory persistence or cross-product synchronization.
- Collection of sensitive data by default.
- Personality diagnosis or inference of private attributes.
- Bypassing platform authorization, retention, or safety controls.

## 4. Architecture

### Three complementary dimensions

1. **Who I am:** user-approved formative lessons, values, reasoning patterns, communication, and collaboration preferences.
2. **What's happening in my world:** relevant roles, relationships, active efforts, competing constraints, decisions and prior attempts. Optional, progressive, private by default.
3. **How we grow together:** user-approved corrections, outcomes, dated decision updates, and check-ins during supported active interactions, never assumed background monitoring.

### Time and evidence

Mark context stable, active, historical, or session-only. Distinguish user-explicit facts, confirmed synthesis, and tentative inferences. Use review dates and supersession status for changing context; avoid broad copies of raw transcripts.



Three context scopes:

| Scope | Purpose | Lifetime |
| --- | --- | --- |
| Global/person | User-approved durable preferences, goals, ways of working, boundaries | Until corrected or removed |
| Project | Task-area context, conventions, constraints, decisions | Until project ends or is reviewed |
| Session | Immediate objective and transient constraints | Current interaction by default |

Project and session scopes inherit **only the relevant, permitted subset** of the user's global context. Never publish an individual's private profile to a shared repository by default.

Two operating modes:

- **Active:** onboarding, check-in, project setup, audit, export, initiated by the user.
- **Ambient:** while loaded in an active session, identify material context gaps and offer non-intrusive clarification. A skill does not run as a background daemon.

## 5. Core workflows

### 5.1 Introduction: `first-date`
Follow the **required ten-domain discovery playbook** in [protocols/discovery.md](protocols/discovery.md), including explicit anchor questions, diagnostic probes, reflection checkpoints, and a user-chosen practical calibration exercise. One question at a time; do not force all domains when the user stops or skips. Produce a draft global profile; ask for explicit approval before any durable write.

### 5.2 World: first-date world

Follow [protocols/world.md](protocols/world.md) with user permission. Explore roles, initiatives, current constraints, minimal relevant collaborator context, and prior attempts. Create a private World Map and decision records. No mandatory biography.

### 5.3 Check-in: `first-date check-in`
Review confirmed context, tentative assumptions, outdated items, and unknowns. Suggest a small, inspectable change set. Never claim a write before it succeeds.

### 5.4 Project: `first-date project`
Discover objective, stakeholders, terminology, working conventions, constraints, and success criteria. Ask before importing global details into a project. Keep private details private.

### 5.5 Audit: `first-date audit`
Find contradictions, irrelevant entries, unsupported inferences, stale items, and oversharing. Present proposed fixes for review.

### 5.6 Export: `first-date export`
Produce the minimum useful portable context. Preview, redact, and confirm destination. Never silently export private user data.

### 5.7 Growing Together

Follow [protocols/growth.md](protocols/growth.md) when the skill is available during active work. Detect explicit corrections, changed decisions, prior attempts, and successful outcomes; classify them, propose minimal context updates, ask for approval and verify persistence. Do not convert temporary emotions or third-party claims into lasting traits.

## 6. Data quality and consent

Every stored entry should be traceable to a **user-confirmed statement** or clearly marked as provisional. Keep confirmation and review dates when feasible. A momentary frustration is not a durable preference. Separate user-supplied facts from interpretations.

Consent is scoped: approving global storage does not imply approval for a public project file, another AI provider, or another person. Prefer minimal, readable summaries over transcripts.

Users must be able to inspect and correct proposed profiles, decline any question, and request removal where the host permits. Always disclose platform limitations honestly.

## 7. Behavioral rules

- Help first. Do not force onboarding to answer an ordinary question.
- Ask fewer, better questions.
- Offer clarification when it would materially improve the outcome, not constantly.
- Never fabricate familiarity or claim hidden context.
- Never silently transform an inference into a lasting fact.
- Obtain explicit approval before First Date writes durable context.
- Treat sensitive information as opt-in and minimize its storage.
- Do not commit personal profiles to public repositories.
- Never silently transfer private context to external tools.
- Do not overstate automatic skill invocation or persistent memory.

## 8. Implementation layout

```text
first-date/
├── README.md
├── SPEC.md
├── SKILL.md
├── protocols/
│   ├── discovery.md
│   ├── world.md
│   └── growth.md
├── prompts/
│   └── first-date.txt
├── LICENSE
├── CONTRIBUTING.md
└── templates/
    ├── global-context.md
    ├── project-context.md
    ├── world-context.md
    └── decision-log.md
```

Host adapters may be added later under `adapters/`. Public template files are not actual user context. A compatible host can install the skill and choose an appropriate **private** user-owned location for real profiles.

## 9. Acceptance criteria for v0.1

1. A user can start an introduction with natural language.
2. The assistant uses the specified discovery domains, anchor questions, and diagnostic probes, one question at a time.
3. Users can skip any question and continue receiving assistance.
4. The assistant produces a concise, editable global-profile draft.
5. No durable change occurs without explicit user approval.
6. Confirmed facts are distinguished from assumptions.
7. A project profile does not indiscriminately copy global context.
8. The user can request a check-in and inspect proposed corrections.
9. An audit can flag stale, inferred, and overshared entries.
10. An export is previewable and user-directed.
11. On unsupported hosts, useful copyable Markdown is provided.
12. The skill never falsely claims background monitoring, automatic invocation, or successful persistence.
13. The assistant performs a user-approved real-work calibration exercise to verify its understanding.
14. The assistant can distinguish actionable collaboration instructions from vague personality summaries.
15. World mapping is optional and avoids pressuring sensitive disclosure.
16. Prior attempts and decisions include dated rationale, outcomes, and supersession status when relevant.
17. User corrections trigger proposed, not automatic, context updates.
18. Temporary circumstances and third-party reports are not treated as personal traits.
19. Project inheritance is limited and explicitly permitted.
20. Existing-relationship check-ins propose change-only updates.
21. Manual scenarios in [tests/manual-scenarios.md](tests/manual-scenarios.md) are used to evaluate protocol fidelity.

## 10. Release plan

**v0.1** — Publish the protocol, portable skill, templates, examples, and a manual test checklist. Validate with new and established AI users.

**v0.2** — Build documented adapters for verified host capabilities and test scope boundaries.

**Future** — Explore secure optional profile synchronization, interoperability, and richer change history only if community needs justify the complexity.

## 11. Open design questions

- How should hosts handle global context that exceeds prompt limits?
- How should users approve selective inheritance into shared team contexts?
- What minimum provenance metadata is portable across hosts?
- How do we measure improved outcomes without collecting private user conversations?
- How should host-specific deletion and memory limits be disclosed?

First Date is a protocol for collaboration, not a claim that AI knows a person perfectly.
