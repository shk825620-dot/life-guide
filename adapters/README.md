# Agent Skills 宿主适配状态

核心包是 `skills/life-guide/`，只使用 Agent Skills 标准的 `SKILL.md`、`references/` 和 `assets/`。宿主专属元数据与安装路径放在本目录，避免把一个产品的字段写进所有宿主都要读取的核心包。

| 宿主 | 适配资料 | 自动发现依据 | 当前验证状态 |
|---|---|---|---|
| OpenAI / Codex | `skills/life-guide/agents/openai.yaml`、本表 | 标准 `SKILL.md` 的 `name`/`description`；OpenAI UI 元数据 | 文件格式已检查；真实自动触发未验证 |
| Claude Code / Claude API | [`claude/README.md`](claude/README.md) | `SKILL.md` frontmatter；按宿主安装到技能目录或上传 Skill | 文档适配；真实触发未验证 |
| Gemini CLI | [`gemini-cli/README.md`](gemini-cli/README.md) | `.gemini/skills/` 或 `.agents/skills/` 扫描，按描述自动激活 | 文档适配；真实 `/skills` 与激活未验证 |
| GitHub Copilot | [`github-copilot/README.md`](github-copilot/README.md) | `.github/skills/`、`.claude/skills/` 或 `.agents/skills/` | 文档适配；真实加载未验证 |
| WorkBuddy | [`workbuddy/README.md`](workbuddy/README.md) | WorkBuddy 专属字段与导入流程 | 已复制上一候选 5.1.12；当前标准包为 6.0.0，目标目录仍残留 6 个旧参考文件，自动触发未验证 |

“标准包可移植”只表示目录和 frontmatter 符合开放格式，不表示任何宿主一定会自动触发、读取全部参考文件或提供联网工具。
