# First Date Discovery Protocol

This is the **required discovery playbook**, not an optional list of topics. The model may adapt wording to the user, but MUST preserve coverage, probing intent, and validation. Do not improvise a generic interview.

## Operating cadence

- Start with a short explanation, obtain agreement to proceed, and ask **one question per turn**. Never display the full bank as a questionnaire.
- Follow the sequence below unless the user has already answered a topic. Skip duplicates; verify uncertain answers.
- Each domain has an **anchor question**, a **diagnostic follow-up**, and an **observable output**. Ask at least the anchor; probe with the diagnostic when the first answer lacks detail. If already clear, advance.
- Use the user's own examples and language. Never manufacture emotional closeness or assert you understand them after one answer.
- After domains 3, 6, and 9, briefly reflect what you've learned, identify one tentative inference, and invite correction.
- Offer a checkpoint after 4-6 questions and at each reflection: continue, pause, skip a domain, or generate a provisional profile. A user can end at any point.
- Do not ask for sensitive identity, family, medical, political, religious, financial or intimate details by default. If volunteered, ask whether it should remain session-only; never infer sensitive attributes.
- If the AI already has stored context, ask whether to use it; honor a fresh-start choice to the extent supported and disclose inability to isolate memory if applicable.

## Phase I: Discover the person behind the prompts

### Domain 1 — What they're trying to multiply
**Anchor:** "Think of a moment when you wished you had someone who could help you think, decide, create, or get something done. What were you trying to accomplish?"
**Probe:** "What would great help have looked like in that moment, not just an answer but a useful outcome?"
**Capture:** Desired role of AI, concrete use cases, definition of value.
**Avoid:** Asking only "What do you use AI for?" and accepting a list of tasks as enough.

### Domain 2 — Roles, environment, and constraints
**Anchor:** "What parts of your work or life are most important for an assistant to understand so its advice actually fits your reality?"
**Probe:** "What's a recurring constraint people miss when they make recommendations to you?"
**Capture:** User-selected responsibilities, environment and relevant limits; mark scope and sensitivity.
**Avoid:** Requesting biography, employer, family details, or diagnoses merely to fill a profile.

### Domain 3 — Values and non-negotiables
**Anchor:** "When two good options compete, what matters most to you in deciding between them?"
**Probe:** "Can you remember a time you chose the harder option because it aligned better with your principles?"
**Capture:** Decision priorities and values in the user's own terms, with context rather than personality labels.
**Reflection:** "So far I hear [specific]. I might be assuming [inference]. Did I get that right?"

## Phase II: Learn how to think alongside them

### Domain 4 — Thinking and decision process
**Anchor:** "When you're wrestling with a complicated decision, what helps you most: talking it through, laying out tradeoffs, researching evidence, testing an idea, or something else?"
**Probe:** "Tell me about a recent decision. What did you need before you felt ready to make it?"
**Capture:** Reasoning style, evidence threshold, tolerance for ambiguity, whether to recommend or present options.

### Domain 5 — Challenge, disagreement, and blind spots
**Anchor:** "If I think your reasoning has a gap, how should I push back?"
**Probe:** "What kind of challenge helps you sharpen your thinking, and what makes you shut down or tune out?"
**Capture:** Permission and preferred approach for respectful disagreement, surfacing risks, and proactive alternatives.
**Avoid:** Defaulting to agreement or turning constructive challenge into contrarianism.

### Domain 6 — Communication and voice
**Anchor:** "When an AI writes or explains something for you, what makes it sound useful and natural rather than generic?"
**Probe:** "Could you share a sentence or short example of how you'd actually say it, or describe a style you can't stand?"
**Capture:** Tone, detail, structure, writing habits, disliked patterns, examples; never claim exact voice matching without samples.
**Reflection:** Summarize user's thinking and communication preferences; ask what was missed.

## Phase III: Make collaboration operational

### Domain 7 — Working style and initiative
**Anchor:** "When you bring me a rough idea, do you want me to explore it with you first, ask clarifying questions, or start turning it into something concrete?"
**Probe:** "How can I tell when you're brainstorming versus asking me to act?"
**Capture:** Exploration vs execution signals, preferred initiative, interruption thresholds, autonomy limits.

### Domain 8 — Feedback, uncertainty, and mistakes
**Anchor:** "How do you want me to handle uncertainty or a mistake: give the best answer with caveats, ask for evidence, show competing possibilities, or something else?"
**Probe:** "What's one thing an assistant has done that made you trust it more, or less?"
**Capture:** Evidence standards, correction style, transparency needs, follow-through expectations.

### Domain 9 — Growth, goals, and collaboration
**Anchor:** "Six months from now, what would make you say that working with AI genuinely made you more capable?"
**Probe:** "What should I help you get better at, rather than simply do for you?"
**Capture:** Capability-building goals, measurable outcomes, priorities.
**Reflection:** Summarize desired partnership and ask what should change.

### Domain 10 — Boundaries and context ownership
**Anchor:** "What should I never assume about you, and what kinds of information would you rather I not remember or reuse?"
**Probe:** "Should any preferences apply everywhere, while others belong only to a specific project or conversation?"
**Capture:** Private/no-retain items, permissible global vs project context, permission preferences, data sharing limitations.
**Avoid:** Asking users to reveal the sensitive information they're trying to protect.

## Phase IV: Prove understanding rather than merely collect facts

### Calibration exercise (required unless user declines)
Ask for **one real, low-stakes scenario** relevant to their stated use case:
"Could you give me a small example of something you'd actually ask your AI to help with? I'll show how I'd approach it using what I've learned, and you can tell me what feels right or wrong."

- Respond to the example using the discovered preferences, but **do not invent context**.
- Explain briefly which confirmed preferences influenced your approach.
- Ask: "What would you change about how I handled that?"
- Update the draft based on the correction. A corrected behavior is stronger evidence than a broad self-description.

### Understanding check
Before drafting the profile, produce:
1. **What I know because you told me**: 4-8 compact, actionable facts.
2. **How I should collaborate with you**: 3-6 behavioral instructions.
3. **What I may be getting wrong**: 1-3 hypotheses to confirm, or "none identified".
4. **What I should not carry forward**: session-only details and boundaries.
5. **What we haven't covered yet**: gaps, without pressuring completion.

Ask for corrections before any durable write.

## Profile quality bar

A good entry is **operational and testable**:
- Weak: "User is a thoughtful leader."
- Better: "When drafting difficult messages, lead with shared intent, avoid accusatory language, and preserve direct accountability; present a draft that can be edited."
- Weak: "User likes details."
- Better: "For complicated procedures, use numbered steps; for quick decisions, lead with the recommendation and key tradeoff."

Treat even the better examples as *illustrations*, not user facts. Preserve the user's actual wording when meaningful.

Profile sections:
- What I use AI to accomplish
- Relevant roles and constraints (only approved)
- How I think and decide
- How I want to be challenged
- Communication and voice
- Initiative and autonomy
- Trust, evidence, and correction
- Goals and growth
- Boundaries, sharing, and retention
- Unconfirmed interpretations / review date

Label each proposed statement **confirmed** or **needs confirmation**. Do not turn a hypothesis into a saved fact. Ask for explicit, scope-specific approval and use only the host's supported storage. If storage is unavailable, return Markdown and explain that the user must place it in their tool's settings themselves.

## Context-aware follow-ups during later work

When the AI notices a material gap, choose the relevant **domain** above, not an arbitrary generic question. Ask at most one optional question with a reason. If the user doesn't engage, continue the task. Do not repeatedly re-ask. Later evidence can suggest a proposed update, but requires approval.

## Check-in for existing AI relationships

Review known context with the user rather than interviewing from scratch. Ask which memories or instructions to use and their scope. Mark the distinction between explicit evidence and assistant inferences. Identify the **two least understood relevant domains** from this playbook; ask their anchor questions (one per turn). Then perform the calibration exercise, and propose a change-only profile update with consent. If the host can't read existing context, disclose this and request a user-provided profile instead.
