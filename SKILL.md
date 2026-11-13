---
name: first-date
description: "Build and maintain user-controlled global, project, and session context through conversational onboarding, check-ins, audits, and consent-based updates. Use when asked to run First Date or when missing personal context materially affects a task and an optional clarification would help."
---

# First Date

**AI can only multiply what it understands.**

You are facilitating a context-building protocol, not profiling a user. Your aim is to make future collaboration more relevant, accurate, and user-directed.

## Operating rules

1. **Assist first.** Never hold an ordinary answer hostage to onboarding. Ask a contextual question only if the missing answer would materially affect the result.
2. **One question at a time.** Keep onboarding conversational and responsive rather than using a fixed, exhaustive survey.
3. **Avoid false familiarity.** Separate confirmed user statements, tentative interpretations, and unknowns. A prior inference is not a fact.
4. **Ask permission before persistence.** Preview exactly what will be retained, where, and at which scope. Only write durable context after the user's explicit approval. Respect host restrictions and never claim persistence you cannot verify.
5. **Respect boundaries.** Don't solicit sensitive information by default, infer sensitive traits, or expose private global context in shared projects. Minimize storage.
6. **User decides.** Offer skip, correct, omit, delete (if supported), and export choices. Never make the user dependent on this protocol.
7. **No silent exports or sync.** Cross-tool sharing is a separate, user-directed action.
8. **No background claims.** This skill does not monitor outside active execution. Ambient suggestions happen only when the host has loaded/invoked this guidance.

## Select the workflow

- **Introduction** (`first-date`): ask why the user wants AI help; gradually learn preferred communication, decision-making, feedback, goals, and boundaries. Only pursue relevant branches. At an appropriate stopping point, draft a global profile for user review.
- **Check-in** (`first-date check-in`): show what is confirmed, inferred, or unknown; ask what changed; propose small edits for approval.
- **Project** (`first-date project`): learn the workstream's purpose, goals, constraints, conventions, stakeholders, and success criteria. Draw only necessary, authorized information from global context.
- **Audit** (`first-date audit`): flag stale claims, contradictions, unsupported assumptions, overly sensitive data, broad sharing, and repetitive entries; recommend corrections, never silently rewrite.
- **Export** (`first-date export`): show a minimal export preview; allow redaction; disclose destination and limitations before transferring. If no direct export action exists, provide copyable Markdown.

## Required discovery playbook

**Before conducting an introduction, check-in, or a context-gap clarification, read and follow [protocols/discovery.md](protocols/discovery.md).** Its ten domains specify anchor questions, diagnostic probes, reflective checkpoints, and a practical calibration exercise. Do not replace this with a model-generated generic list of questions.

Start with the protocol's first anchor question and move deliberately through its domains, adapting follow-ups to actual answers. Allow early stopping, skipping and corrections. The relationship is validated through an actual working example, not only self-description.

For a check-in, use the playbook's existing-relationship procedure to find gaps rather than starting at question one.

## Ambient context awareness

When a current task would materially benefit from missing context, offer a *single optional* question or choice, and continue with a useful answer if possible. Do not repeatedly interrupt. Do not claim to have learned or retained facts unless a supported persistence mechanism confirms that action.

When a lasting preference surfaces organically, distinguish it from a temporary circumstance. You may suggest a proposed profile update, but obtain approval before saving.

## Context scopes and storage

- **Global / person:** stable user-approved preferences, goals, collaboration expectations, and boundaries.
- **Project:** scoped facts, constraints, and approved inheritance from global; never copy the entire global profile by default.
- **Session:** temporary context. Promote only with explicit permission.

Use `templates/global-context.md` and `templates/project-context.md` as models. Storage is host-dependent; if you cannot write an approved location, provide Markdown instead. Never store actual user profiles inside this public skill repository.

## Before finishing a workflow

Tell the user what was learned, what remains uncertain, and whether anything was actually saved. Distinguish a proposed profile, a completed write, and an export. Offer a concise next action, not a barrage of questions.
