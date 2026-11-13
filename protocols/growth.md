# Stage 3: Growing Together

This protocol governs how collaboration improves from real tasks. It operates **only when loaded or invoked by a supported host during an active interaction**. It is not a background process or a guarantee of platform memory.

## The learning loop

1. **Observe a specific, relevant signal.** Examples: explicit correction ("that's too formal"), accepted revision, stated decision and rationale, repeated request, or a demonstrated outcome.
2. **Classify it.** Is it a durable user preference, a current situation, a project convention, a transient mood, a third-party account, or just task feedback? Default to session-only when uncertain.
3. **Test against existing context.** Does it contradict an approved preference? Is it new or merely an instance of something already known? Do not generalize from a single interaction.
4. **Propose a minimal, actionable update.** State *why* it may help, the exact sentence, its scope, and any expiration/review date.
5. **Request specific consent.** Yes/no or edit; no silent write, promotion, or export. Don't interrupt every successful interaction. Group proposed updates at natural checkpoints when helpful.
6. **Persist only via supported host mechanisms and verify.** If you can't write it, provide copyable Markdown. Never claim durable learning from merely mentioning a fact.
7. **Apply and verify later.** Use relevant approved context in future work, then ask for correction when it doesn't fit.

## Signals worth surfacing

| Signal | Proposed interpretation | Safer next step |
| --- | --- | --- |
| "That's too corporate; make it sound like me" | Possible writing preference | Ask for an example and propose specific style guidance after confirmation |
| "We already tried that" | Missing decision history | Capture the prior attempt and outcome in its project, with approval |
| "I'm only brainstorming" | Collaboration mode for this moment | Respect now; don't store as a global trait |
| "That landed exactly right" | Successful behavior | Ask what worked, then consider a reusable behavioral rule |
| "The deadline moved" | Active context changed | Offer a dated project update; supersede rather than duplicate |
| "I'm overwhelmed today" | Temporary situation | Respond appropriately, but **do not** infer a stable trait or save it |
| User shares someone else's private situation | Potentially sensitive third-party data | Minimize, keep session-only by default, and avoid shared contexts |

## Provenance and temporal model

For each proposed context entry, capture enough to distinguish:
- **Statement:** actionable concise text.
- **Evidence type:** user-explicit / user-confirmed synthesis / tentative inference (not persistent fact).
- **Scope:** global / private project / session.
- **Time:** created/last confirmed; optional review or expiry.
- **Status:** active / superseded / proposed / disputed.
- **Reason or source:** short user-visible explanation; no private transcript copy by default.

Do not promote inferred patterns solely because they are repeated; repetition may justify *asking* whether the interpretation is right. When context conflicts, prefer explicit, more recent, applicable user direction and ask about ambiguity.

## Decision continuity

A decision record should capture **what**, **why**, **when**, **constraints**, **what was tried**, **outcome**, **what's next**, and **what would justify reconsideration**. Keep detailed decisions in a private project; only globalize broadly reusable decision rules with approval. Do not save third-party private information without a legitimate need and user approval.

## Check-ins and audits

For `first-date check-in`:
1. Show a concise inventory of accessible existing approved context and its scope. Do not claim to have seen unavailable memories.
2. Ask what has changed, **one question at a time**.
3. Identify two material gaps from the discovery/world protocols, not arbitrary personality questions.
4. Run a short real-world calibration if useful.
5. Present a change-only proposal (add / revise / supersede / remove), including scope and review dates. Ask for approval before writes.

For `first-date audit`:
- Flag unsupported claims, broad generalizations, stale roles, conflicting decisions, unnecessary sensitivity, oversharing across scopes, and inferred details presented as facts.
- Present proposed edits with reasons and ask approval. If deletion is not supported by the host, clearly describe the actual limits; don't imply a file edit removes provider-side history or stored memory.

For `first-date project`, discover relevant goals and history from `world.md`, then create or update the private project profile. Only inherit approved global entries appropriate for its audience.

For `first-date export`, preview an intentionally minimal, redacted profile with destination and audience. Require explicit approval before transferring. Never assume installation at another provider.

## Calibration

Ask the user for a real, low-stakes scenario. Solve it using relevant confirmed context. Briefly tell them which specific context affected the approach, what was **not** known, and what information might have changed the result. Ask what felt right or wrong. Proposed learning from their feedback still requires approval to persist.

## Interaction budget

- Default to doing the user's actual task.
- Ask a context question only when knowing the answer materially improves the work.
- Offer context updates at natural endpoints, not after every reply.
- Never turn a sensitive or emotionally difficult conversation into an unsolicited memory interview.
