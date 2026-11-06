# life-guide — Reduce Information Gaps

[中文文档](README.zh-CN.md)

> Help an AI find the options, costs, and evidence that were missing from the first answer.

`life-guide` is a general Agent Skill for context-dependent recommendations and decisions. For questions such as “what should I choose?”, “how should I start?”, “which route is better?”, or “can this claim be trusted?”, it first identifies the conditions that could change the answer. It then investigates existing tools, alternative routes, applicable rules, and supporting evidence before giving a conclusion with trade-offs and a next step.

## Why this is more than asking an AI one more time

AI makes getting an answer fast. The valuable information is often in the search path behind that answer: knowing where to look, what keywords to use, and how to trace a secondary lead back to a primary source. `life-guide` organizes that path. Search engines find entry points. Official documentation, laws, source code, and statistics establish facts. Reddit, X, Weibo, and Xiaohongshu surface real discussions and failure signals. YouTube can show practical operations and version differences. Key claims are then traced back to sources that support them.

The skill does not promise to list every possible option or treat popularity as evidence. It helps users see routes that were outside their initial view, distinguish verified facts from unknowns, and choose a low-cost next step.

**Good fit:** personalized recommendations, multi-option comparisons, tool research, rules and exception checks, source reliability checks, and important or hard-to-reverse decisions.

**Not a good fit:** simple facts, pure writing or translation, polishing, and questions that do not depend on the user's situation. Those should be answered directly without starting the full process.

## Understand it in 30 seconds

Input: **“I want to start a small business, but I can only think of opening a bubble tea shop. What should I do?”**

| | A common answer without the skill | Expected shape with `life-guide` |
|---|---|---|
| Starting point | Compare bubble tea, coffee, and clothing stores | Ask for the conditions that could change the answer, such as goal, budget, location, and available time |
| Candidate space | Reorder the shop types already mentioned | Investigate ingredients, equipment, delivery, maintenance, distribution, upstream suppliers, and other participation points |
| Evidence | Experience-based advice without sources | Give sources and query dates for decision-changing facts, or mark them as unverified |
| Ending | “You could consider a franchise” | Give a main route, alternatives, opportunity costs, a low-cost validation step, and stop conditions |

This is a **behavior illustration**, not a live market study. It does not prove that any route has demand or fits every user. A longer response example is in [`skills/life-guide/references/examples.md`](skills/life-guide/references/examples.md).

## Installation

**Copy the entire `life-guide/` directory, not only `SKILL.md`.** Reference files are loaded as needed. If they are missing, some rules cannot be reached. The standard package is in [`skills/life-guide/`](skills/life-guide/). A release ZIP is also available, with `life-guide/` as its top-level directory after extraction.

| Platform | Location or import method | How to check discovery |
|---|---|---|
| Claude Code | Project `.claude/skills/life-guide/`, or user `~/.claude/skills/life-guide/` | Check `/skills` |
| OpenAI Codex | `.agents/skills/life-guide/` | Invoke `$life-guide` explicitly |
| Gemini CLI | `.gemini/skills/life-guide/`, or `gemini skills install <path>` | Run `/skills list`; trust the workspace first and reload skills after adding |
| GitHub Copilot | Project `.github/skills/life-guide/` and supported `.claude/skills` or `.agents/skills`; user `~/.copilot/skills/` | Ask a question and observe loading; `gh skill` may also be available |
| WorkBuddy local | `life-guide/` inside the host skill directory | Check the skill list for the name and description |
| WorkBuddy hosted platform | Requires a host-specific package. See [`adapters/workbuddy/`](adapters/workbuddy/) | Follow the host's review result |
| Doubao / Coze | Content mapping, not direct installation of the standard package. See [`adapters/`](adapters/) | Not verified |

Windows example for a project-level Claude Code installation using Git Bash:

```bash
mkdir -p .claude/skills
cp -r /path/to/skills/life-guide .claude/skills/
ls .claude/skills/life-guide/SKILL.md
```

After installation, try these two boundary checks:

1. Ask “Which country is Paris in?” The skill should answer directly without asking about career goals or starting an investigation.
2. Ask “I want to start a small business, but I can only think of a bubble tea shop.” The skill should restate what is known, identify key gaps, and ask prioritized questions instead of immediately returning a shop-type ranking.

If both behaviors match, discovery and boundaries are working in that host. If they do not, submit the host, version, input, and actual output according to [`CONTRIBUTING.md`](CONTRIBUTING.md).

## Verification boundary

- **Structural checks do not prove outcome quality.** Static checks only verify package structure, references, and rule consistency.
- The current version has local structural and behavior records. Automatic triggering, cross-host behavior, cross-model behavior, and real-user outcomes remain unverified. Platform status is listed in [`adapters/`](adapters/), and untested items are labeled as unverified.
- Historical behavior records come from 5.x batches. They used one host, one model, manual loading, and human judgment across versions, so they cannot be generalized to the current version or every host.
- Tool installation, account login, and external writes require explicit user approval. The skill does not promise that a tool is virus-free or immune from account restrictions.

## Evidence and maintenance documents

- With/without-skill comparison and boundaries: [`docs/ab-evidence.md`](docs/ab-evidence.md)
- Release plan and post-release observations: [`docs/release-plan.md`](docs/release-plan.md)
- Behavior cases and run records: [`tests/`](tests/)
- Package boundaries and maintenance rules: [`docs/architecture/package-boundaries.md`](docs/architecture/package-boundaries.md)

## Contributing

Reports about installation failures, missing triggers, unreadable reference files, or unexpected answers are welcome. Include the host, version, input, and actual output. Rule-change discipline is documented in [`CONTRIBUTING.md`](CONTRIBUTING.md).

## Language

Chinese documentation is available in [`README.zh-CN.md`](README.zh-CN.md).

## License

MIT. See [`LICENSE`](LICENSE). The skill package includes the same license file.
