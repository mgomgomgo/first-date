# First Date: personal Claude pre-test

**Do not share your completed profile or conversation transcript publicly.** Record ratings and sanitized observations only.

## Before you start

- Download the [real First Date skill ZIP](https://github.com/mgomgomgo/first-date/releases/download/v0.2.0-pretest.1/first-date.zip).
- Install it via Claude's **Customize → Skills → + → Create skill → Upload a skill**.
- Enable the skill and open a normal new chat outside a project.
- Decide whether to let Claude use its existing memory. If you request a fresh start, note that a new chat may still access provider memory. Don't treat it as a perfectly isolated baseline.

## Test A: First Date

Say: **Run First Date.**

Look for:
1. A specific question about a time you wanted better help, not a generic "tell me about yourself."
2. One question per turn and follow-ups that build on your answers.
3. Exploration of meaningful reasoning, principles, communication, challenge, and boundaries.
4. A checkpoint or option to pause; not a forced ten-question interrogation.
5. A brief practical demonstration of understanding using your own low-stakes scenario.
6. A draft of useful behavioral context, with explicit approval before any actual save.

Try saying **"I'd rather not discuss that"** once. It should move on without guilt or invented assumptions.

## Test B: Your world

Say: **Run First Date world.**

Look for:
- The AI asks permission to map what's relevant.
- It asks about active initiatives, history, what you've already tried, and real constraints.
- It minimizes third-party details and asks where context should belong (global, project, or session).
- It doesn't turn the session into an exhaustive biography.

## Test C: Growing Together

Offer a simple writing or decision task. Correct the AI's first approach (for example: "That sounds too formal"). Then ask **"What did you learn from that correction?"**

Look for:
- It states the specific behavior that should change.
- It doesn't claim a lifelong personality trait from one correction.
- It asks before saving any durable preference.
- It tells you whether anything was actually persisted.
- In a new chat, test if the approved context is accessible. If not, note the provider/storage limitation.

## Test D: Returning-user check-in

Say: **Run First Date check-in.**

Look for:
- It distinguishes context it can actually access from guesses.
- It identifies gaps rather than repeating every onboarding question.
- It proposes inspectable changes with timestamps/scopes.
- It can correct or supersede a dated decision.

## Scorecard

Rate each 1–5, where 1 = poor and 5 = excellent.

| Area | Score |
| --- | --- |
| Questions were specific and revealing | _/5 |
| Conversation felt adaptive and human, not scripted | _/5 |
| AI understood how I think, not just what I said | _/5 |
| AI understood relevant constraints and history | _/5 |
| Practical calibration changed the work meaningfully | _/5 |
| Context boundaries and consent were respected | _/5 |
| Saved context was usable in a new chat (if supported) | _/5 |

### Sanitized feedback

- What worked:
- Where the AI missed your meaning:
- Which question felt unnecessary:
- What important context was never discovered:
- Did it actually use the installed skill? How did you verify?
- What platform and available memory/storage options did you test?

## Known limits

Automated GitHub checks validate skill files and ZIP structure, **not** live conversational fidelity or persistence. This field test is the next validation step.
