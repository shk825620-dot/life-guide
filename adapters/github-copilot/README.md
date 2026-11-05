# GitHub Copilot 适配

GitHub Copilot 支持把标准 Skill 放入项目的 `.github/skills/life-guide/`、`.claude/skills/life-guide/` 或 `.agents/skills/life-guide/`；个人 Skill 放在 `~/.copilot/skills/` 或 `~/.agents/skills/`。Copilot 根据 Skill 描述判断相关性，复杂任务才加载详细内容。

项目发布时建议把核心目录复制到 `.github/skills/life-guide/`，并保留全部 references。Copilot CLI 也可用 `gh skill` 从 GitHub 仓库发现和安装技能。

用一个学习路线、采购比较或法规核查问题分别测试发现和实际加载，不把「目录可放置」当成「自动触发已证明」。

官方说明：<https://docs.github.com/en/copilot/concepts/customizations/agent-skills>

当前状态：路径和说明适配；Copilot 各产品形态（App / CLI / cloud agent / IDE）的真实发现、自动加载和工具行为未在本项目中验证。

## 放置位置速查

| 范围 | 路径 |
|---|---|
| 项目级（三选一） | `.github/skills/life-guide/`、`.claude/skills/life-guide/`、`.agents/skills/life-guide/` |
| 个人级 | `~/.copilot/skills/life-guide/` 或 `~/.agents/skills/life-guide/` |
| 云端会话个人技能 | 放在 dotfiles 仓库的 `.copilot/skills/`（不适用于 Actions 会话） |

支持范围随产品形态与版本变化，具体以各形态官方 setup 指南为准，不要假设个人技能在云端代理中一定可用。
