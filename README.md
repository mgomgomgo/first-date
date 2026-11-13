# First Date

**AI can only multiply what it understands.**

First Date is an open, portable protocol for helping AI assistants develop a useful, accurate, evolving understanding of the people they work with.

Most AI interactions begin with a task. First Date begins by making room for the person behind that task.

> Understand before assuming. Learn without intruding. Remember with permission. Evolve through experience.

## What it does

- **Introduces you to your AI** through a natural conversation, not a lengthy questionnaire.
- **Builds global context** about how you prefer to think, communicate, work, and collaborate.
- **Creates project context** that inherits only relevant, permitted details from your global profile.
- **Offers optional context clarification** during ordinary work when a significant gap would materially change an answer.
- **Supports check-ins, audits, corrections, and exports** so context stays accurate and in your control.

## Try it

Copy [SKILL.md](SKILL.md) into a supported AI skill location, or paste its instructions into your AI assistant and say:

```text
Run First Date. I'd like to establish the context that will help us work together.
```

For an existing relationship:

```text
Run First Date check-in. Show me what you know, what's inferred, and what needs updating.
```

For a project:

```text
Run First Date project. Help me establish context for this workstream.
```

The exact installation path, automatic skill discovery, and persistence behavior depend on your AI platform. A plain prompt **cannot guarantee** global memory, passive invocation, or cross-session persistence. When those capabilities are unavailable, First Date produces copyable Markdown profiles.

## How context is organized

| Layer | Contains | Default boundary |
| --- | --- | --- |
| Global | Durable preferences, explicitly supplied goals, ways of working | Private, user-controlled |
| Project | Workstream goals, conventions, stakeholders, constraints | Project-scoped; only permitted global context |
| Session | Immediate goal, temporary decisions, short-lived details | Not promoted without approval |

See [global-context template](templates/global-context.md) and [project-context template](templates/project-context.md).

## Ways to use it

| Invocation | Purpose |
| --- | --- |
| `first-date` | Conversational introduction |
| `first-date check-in` | Reconcile and refresh context |
| `first-date project` | Create or refine a project profile |
| `first-date audit` | Identify stale, unsupported or overshared context |
| `first-date export` | Produce an approved, portable profile |

These are **conceptual invocations**, not guaranteed native slash commands on every platform.

## Principles

1. User agency comes first. The assistant supports judgment rather than replacing it.
2. Help with the task before requesting optional context, whenever possible.
3. Never infer a lasting personal fact from a single message.
4. Request explicit approval before writing durable context through this protocol.
5. Keep private profiles out of public repositories.
6. Only share the minimum relevant information across context boundaries.
7. Be transparent about what the host can and cannot remember.

## Project status

**v0.1: early prototype.** The skill and templates are usable as instructions, but cross-platform behavior and storage adapters require validation. See [SPEC.md](SPEC.md) for scope and acceptance criteria.

## Contributing

Feedback, platform adapters, examples, and accessibility improvements are welcome. See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

MIT. See [LICENSE](LICENSE).
