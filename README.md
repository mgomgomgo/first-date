# First Date

**AI can only multiply what it understands.**

Your AI may be incredibly capable. But if it doesn't understand how you think, communicate, make decisions, and what matters to you, you're leaving much of that capability untapped.

**First Date helps your AI get to know you, through a conversation rather than a questionnaire.** No coding required.

## Start your First Date (no installation)

**1.** Open [Claude](https://claude.ai/) or [ChatGPT](https://chatgpt.com/) in a new chat. Other conversational AIs may also work.

**2.** Click the **Copy** icon on the following prompt.

**3.** Paste it into your AI and start talking.

<details open>
<summary><strong>Copy this prompt to begin</strong></summary>

```text
You are running First Date, a user-controlled protocol for building a better working relationship between a person and their AI.

Your purpose is not to collect a biography. It's to understand enough about how I think, communicate, make decisions, and what I'm trying to accomplish that you can collaborate with me more effectively.

Make this feel like a real conversation, not an intake form:
- Start with one thoughtful question about what I want AI to help me accomplish.
- Ask only one question at a time. Listen and adapt each follow-up to what I actually say.
- Explore my working style, decision-making, preferred feedback, goals, and boundaries only when relevant.
- Don't assume that everything I say is a permanent preference. Separate things I've explicitly confirmed from your interpretations.
- Don't ask for sensitive personal information unless I bring it up and it is genuinely relevant. I can skip any question.
- Don't claim to know me already or invent facts. If you have existing memory, be transparent about whether you're using it.

When we've established enough useful context, or I ask to stop:
1. Summarize what you've learned in a concise, editable global context profile, distinguishing confirmed facts from things to verify.
2. Ask me to correct, remove, or approve that profile.
3. Before saving anything, tell me where it would be stored, who or what could access it, and whether that storage would persist into future chats.
4. Save only what I explicitly approve, and only if your platform truly supports the requested storage. Otherwise give me a copyable Markdown profile and instructions for using it.
5. Never add my private information to a public project or automatically share it with another service.

Start the conversation now. Ask me your first question.
```

</details>

That's it. **No ZIP files, extensions, account registration, or technical setup.**

### What happens next?

Your AI should ask a question and build on your answer, one step at a time. You can skip anything. When you're ready to finish, ask it to create a context profile you can review and approve.

**Important:** A conversation alone does not guarantee long-term memory. Different AI tools offer different persistence options, and some may not support global context at all. First Date should explain what's available and give you a reusable Markdown profile when it can't save one. Never paste private profiles into this public GitHub repository.

### Already have an AI relationship?

Start a chat and paste:

```text
Let's do a First Date check-in. Tell me what you currently know about how I think and work, separate confirmed facts from assumptions, and ask one question at a time to fill meaningful gaps. Don't save changes without showing me a proposed update and getting my approval.
```

This prompt asks for a check-in. If you want the **full check-in procedure** without installing anything, copy the longer instructions in [SKILL.md](SKILL.md) as well.

## What makes it different?

Most AI onboarding focuses on the task. First Date focuses on the person behind the task.

- **Conversational by design.** No giant forms or mandatory questions.
- **Global context first.** What the AI learns about you should be reusable across relevant work where your AI supports it.
- **Project-specific context when needed.** Projects should inherit only the minimum approved information.
- **User-owned and inspectable.** Review, correct, withhold, or export your context.
- **Evolving, not one-and-done.** Future check-ins help correct stale assumptions and deepen understanding.

> Understand before assuming. Learn without intruding. Remember with permission. Evolve through experience.

## Want the ongoing experience?

The zero-install prompt starts the conversation. The [full skill](SKILL.md) adds structured workflows for onboarding, project context, check-ins, audits, and exports, plus guidance for optional context clarification during normal collaboration *when your AI platform loads the skill*.

| Approach | Best for | What to expect |
| --- | --- | --- |
| **Copy the prompt** | Anyone trying First Date | Immediate introduction; persistence depends on your AI tool |
| **Install the skill** | People who want repeated use | Host-supported skill invocation and maintenance workflows; storage still depends on the platform |
| **Use the templates** | People who want full control of their data | Portable Markdown for [global context](templates/global-context.md) and [project context](templates/project-context.md) |

See the [skill instructions](SKILL.md) for the full protocol. Native slash commands, automatic loading, and global memory **are not guaranteed** across AI platforms.

## How context is organized

| Layer | Contains | Boundary |
| --- | --- | --- |
| **Global: the person** | Durable communication, decision-making, goals, boundaries | Private and user-controlled |
| **Project: the work** | Conventions, decisions, objectives, constraints | Inherit only relevant approved global context |
| **Session: the moment** | Immediate goal and temporary circumstances | Not promoted without permission |

## For contributors and implementers

- [Protocol specification](SPEC.md)
- [Full skill](SKILL.md)
- [Reusable starter prompt](prompts/first-date.txt)
- [Global profile template](templates/global-context.md)
- [Project profile template](templates/project-context.md)
- [Contributing](CONTRIBUTING.md)

**Status:** v0.1 early prototype. We're validating the conversational experience and cross-platform behavior. Feedback and real-world testing (without sharing personal profiles) are welcome.

MIT licensed. See [LICENSE](LICENSE).
