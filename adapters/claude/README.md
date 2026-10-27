# Claude 适配

Claude Code 支持把标准 Skill 放入项目 `.claude/skills/life-guide/` 或用户技能目录；Claude API 需要通过其 Skills 能力上传或挂载目录。Claude 根据 `SKILL.md` 的 `name` 和 `description` 判断是否相关，参考文件按需读取。

建议安装：复制 `skills/life-guide/` 整个目录，保留 `SKILL.md`、`references/`、`assets/` 和 `agents/`。先在目标环境查看 Skill 是否被发现，再用一个需要比较路线的真实问题测试自动触发。

官方说明：<https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview>

当前状态：目录结构适配；Claude Code/API 的真实加载、自动触发和工具可用性未在本项目中验证。
