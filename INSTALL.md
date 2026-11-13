# Install First Date

**Install the real skill, not a shortcut prompt.** The skill includes `SKILL.md`, three protocols, and four context templates. The installed skill teaches the assistant the specific discovery questions, World Map, and consent-based learning loop.

## Option A: Personal Claude (claude.ai)

1. Go to the repo's [Actions tab](https://github.com/mgomgomgo/first-date/actions/workflows/validate.yml).
2. Select the latest **successful** "Validate and package First Date" run on `main`.
3. Under **Artifacts**, download `first-date-claude-skill`. GitHub may require sign-in to download Actions artifacts; artifacts also expire after 30 days. If unavailable, follow Option C.
4. Extract the downloaded artifact. Inside it is `first-date.zip`. **Upload that inner ZIP, not the outer artifact archive.**
5. In Claude, open **Customize → Skills → + → Create skill → Upload a skill** and upload `first-date.zip`.
6. Enable the skill, then start a chat: `Run First Date.`

Claude must support custom skills and have the required code-execution/file-creation capability. This installs instructions, not a cross-session personal context database. Confirm any profile storage capability separately.

## Option B: Claude Code / supported coding agents

Requires Node.js and the open skills CLI:

```sh
npx skills add mgomgomgo/first-date -g
```

Select the appropriate supported agent when prompted. Global means available across projects **within that agent**, not shared memory across all AI providers. If autodiscovery misses the root skill, use manual installation in Option C.

## Option C: Manual package build (works from a repo checkout)

Requires Python 3.10 or later; no third-party Python dependencies.

```sh
git clone https://github.com/mgomgomgo/first-date.git
cd first-date
python scripts/package_skill.py
python scripts/validate_skill.py
```

Upload `dist/first-date.zip` to personal Claude. The packaging script includes **exactly** the skill's eight instruction and template files under one `first-date/` folder. No personal context or repository metadata is packaged.

## First-run checks

1. Say `Run First Date` and check it asks the concrete opening anchor from [discovery](protocols/discovery.md), not a generic survey.
2. Say `Run First Date world` and confirm it asks permission before exploring active initiatives.
3. Say `Run First Date check-in` and confirm it uses relevant existing context only if accessible and permitted.
4. Ask where your profile would be stored. It should answer accurately for your AI tool, not promise global memory.
5. Use a real low-stakes task to verify that it applies your approved context and welcomes correction.

For the evaluation rubric, see [test scenarios](tests/manual-scenarios.md). Don't publish personal transcripts or completed profiles in issues.

## What this installation cannot guarantee

- Always-on background monitoring
- Automatic invocation on every platform or every conversation
- Persistent cross-session memory
- Automatic cross-provider synchronization
- Removal of historical provider-held chat records when editing a local profile

The protocol always requires consent for its own context writes, and otherwise supplies copyable Markdown.
