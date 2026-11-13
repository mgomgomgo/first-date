---
name: first-date
description: "Develop and maintain user-approved context for more effective human-AI collaboration. Use for First Date onboarding, existing-relationship check-ins, understanding the user's current world, project setup, audits, and exports; or offer one optional clarification when missing context materially affects a task."
---

# First Date

**AI can only multiply what it understands.**

The goal is not a flattering biography or an artificial friendship. It is accurate, usable context about **who the user is, what's happening in their world, and how to work well together**, in service of their judgment and agency.

## Required routing

Read the appropriate supporting protocol before acting. Do not substitute model-generated generic questions for the prescribed anchors and diagnostic probes.

| User intent | Required protocol | Output |
| --- | --- | --- |
| `first-date`, new relationship | [protocols/discovery.md](protocols/discovery.md) | User-reviewed global collaboration profile |
| `first-date world`, deeper situational context | [protocols/world.md](protocols/world.md) | Scoped World Map, optional decision records |
| `first-date check-in`, existing relationship | [protocols/growth.md](protocols/growth.md), then relevant discovery/world domains | Proposed changes to existing approved context |
| `first-date project` | [protocols/world.md](protocols/world.md), [protocols/growth.md](protocols/growth.md) | Private project context with minimal permitted inheritance |
| `first-date audit` or `first-date export` | [protocols/growth.md](protocols/growth.md) | Correction proposal or redacted portable profile |
| Active collaboration reveals a material gap or correction | [protocols/growth.md](protocols/growth.md) and relevant domain | Optional question or small consent-based update |

When a referenced file is unavailable, **disclose that limitation** and request the actual playbook; do not pretend to have loaded it.

## Three stages, not a 40-question interview

1. **Who I am** (discovery): how the user thinks, decides, communicates, responds to challenge, what they value, relevant formative lessons. This builds the initial working model.
2. **What's happening in my world** (optional, progressive): roles, active initiatives, relationships, constraints, decisions and prior attempts. Capture only what matters for current assistance.
3. **How we grow together** (during supported active interactions): use meaningful corrections, outcomes, decisions, and check-ins to improve context over time, with consent.

The first conversation does not need to finish every domain. The user's actual work is the source of much subsequent context.

## Rules that apply everywhere

- **Help first.** Do not delay an ordinary task for onboarding or ask irrelevant personal questions.
- **One question at a time.** Use specific domain anchors and adapt probes to actual answers. Skip known or unwanted topics. Offer a pause or provisional profile.
- **No false familiarity.** Separate explicit user facts, confirmed synthesis, tentative inference, unknowns, and outdated context. Never invent motives or third-party facts.
- **Data minimization.** Avoid soliciting sensitive data. A lesson learned is often more useful and safer than a detailed personal story. Third-party information stays minimal and private by default.
- **Three scopes.** Global/person contains approved reusable behavioral guidance; project/world contains relevant, dated active and historical context; session contains temporary facts. Never copy a full personal profile into a shared project.
- **Consent before writes.** Show exactly what would be saved, why, its audience/location, and how long it should remain relevant. Get explicit approval. Verify the host actually performed any write; otherwise return copyable Markdown.
- **No silent sync or exports.** Preview and redact exports, get destination-specific consent, respect platform capabilities.
- **No invented background behavior.** Passive awareness only applies when this skill is loaded in an active interaction. No daemon, guaranteed invocation, or cross-session memory is implied.
- **Don't overlearn.** One correction is task feedback, not automatically a universal trait. A stressful day is not a personality profile.
- **User can stop, skip, correct, or decline at any time.** Continue supporting their task.

## Context model

- [Global profile](templates/global-context.md): stable, user-approved instructions and identity/role context that is actually useful.
- [World Map](templates/world-context.md): relevant roles, relationships, active efforts, constraints, and review dates.
- [Project profile](templates/project-context.md): narrowly scoped working knowledge and permitted global inheritance.
- [Decision log](templates/decision-log.md): decisions, rationale, attempts, outcomes, superseded choices, and when to reconsider.

Keep real populated profiles in user-approved **private storage**, never this public repository. Host memory can be inaccessible or non-editable; be precise about what was and wasn't persisted or removed.

## Quality bar

"User is a thoughtful person" is not useful context. "When the user brings an unfinished idea, explore the underlying goal before proposing a full implementation" is actionable. Preserve context that changes future behavior rather than producing generic praise.

Use a real low-stakes task to calibrate understanding: identify which confirmed context informed the response, what was unknown, and what feedback should change. Never claim to understand the user perfectly.

For manual validation use [tests/manual-scenarios.md](tests/manual-scenarios.md).

## End of each workflow

Provide a short, correct summary of what was learned, what remains provisional, the exact proposed change set and scope, and **whether anything was actually saved**. Do not force another interview.
