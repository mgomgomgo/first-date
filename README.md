# First Date

**AI can only multiply what it understands.**

Your AI may be incredibly capable. But if it doesn't understand how you think, communicate, make decisions, and what matters to you, you're leaving much of that capability untapped.

**First Date helps your AI get to know you, through a conversation rather than a questionnaire.** No coding required.

## Start with the actual protocol

**First Date is a structured discovery protocol, not a generic "get to know me" prompt.** It uses ten specific discovery domains, thoughtful follow-ups, checkpoints, and a practical exercise to test whether your AI actually understands how to collaborate with you.

**[Read the complete discovery protocol](protocols/discovery.md)** to see the exact questions and flow.

### First Date, after installation

Once the full skill is installed and its supporting files are available, simply say:

```text
Run First Date.
```

Or use the [explicit invocation prompt](prompts/first-date.txt), which requires the installed protocol and will **not** pretend a short prompt is equivalent to the real skill.

### Want to preview it without installing?

Open [the discovery protocol](protocols/discovery.md) and copy its **entire contents** into your AI, followed by: `Run First Date using the protocol above.`

This is a **manual demonstration** of the same structured interview, but it doesn't install persistent behavior or guarantee memory across sessions. We are improving packaging to make the full experience easier to install.

### Already have a relationship with your AI?

Install the skill and say `Run First Date check-in`. The protocol checks existing context for unverified assumptions, identifies the least-understood relevant domains, and calibrates against a real working example. It does not need to reinterview you from scratch.

## What makes it different?

Most AI onboarding focuses on the task. First Date focuses on the person behind the task.

- **Conversational by design.** No giant forms or mandatory questions.
- **Global context first.** What the AI learns about you should be reusable across relevant work where your AI supports it.
- **Project-specific context when needed.** Projects should inherit only the minimum approved information.
- **User-owned and inspectable.** Review, correct, withhold, or export your context.
- **Evolving, not one-and-done.** Future check-ins help correct stale assumptions and deepen understanding.

> Understand before assuming. Learn without intruding. Remember with permission. Evolve through experience.

## Install the full skill (recommended)

This installs the **actual First Date protocol**, including its skill instructions and context templates, rather than just a standalone prompt.

### Personal Claude (claude.ai)

1. Download the packaged First Date skill ZIP from a project release **when published**. A release asset is not available yet; until then, create a ZIP containing a `first-date/` folder with [SKILL.md](SKILL.md) and the [templates](templates/) folder.
2. In Claude, open **Customize → Skills → + → Create skill → Upload a skill**.
3. Upload the ZIP and enable First Date.
4. Start a chat and say: **"Run First Date."**

Claude requires code execution to be enabled for Skills. Installation is persistent within Claude's supported skill settings, but this does not automatically guarantee durable storage of the resulting personal profile.

### Claude Code / supported coding agents

From your terminal (requires Node.js and the community skills CLI):

```sh
npx skills add mgomgomgo/first-date -g
```

Choose your agent when prompted. The `-g` flag installs globally rather than only in the current project. Confirm the agent discovers First Date after installation. This is a community installer, not a built-in feature of all chat apps.

### Other AI tools

Installation, invocation, and persistent memory are host-specific. See [SKILL.md](SKILL.md) for the portable protocol; do not assume every AI can automatically fetch or execute a GitHub repository.

## Want the ongoing experience?

The manual protocol preview can demonstrate the conversation, but does not install ongoing behavior. The [full skill](SKILL.md) adds structured workflows for onboarding, project context, check-ins, audits, and exports, plus guidance for optional context clarification during normal collaboration *when your AI platform loads the skill*.

| Approach | Best for | What to expect |
| --- | --- | --- |
| **Copy the full discovery protocol** | Anyone evaluating the conversation style | Structured manual demo; no installed behavior or persistence guarantee |
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
- [Required discovery questions and calibration](protocols/discovery.md)
- [Installed skill invocation prompt](prompts/first-date.txt)
- [Global profile template](templates/global-context.md)
- [Project profile template](templates/project-context.md)
- [Contributing](CONTRIBUTING.md)

**Status:** v0.1 early prototype. We're validating the conversational experience and cross-platform behavior. Feedback and real-world testing (without sharing personal profiles) are welcome.

MIT licensed. See [LICENSE](LICENSE).
