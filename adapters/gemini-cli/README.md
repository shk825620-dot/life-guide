# Gemini CLI 适配

Gemini CLI 支持标准 `SKILL.md`，可安装到用户级 `~/.gemini/skills/`，或项目级 `.gemini/skills/`；`.agents/skills/` 是兼容别的 Agent 工具的别名。安装后使用 `/skills list` 查看，必要时用 `/skills reload` 刷新。

Windows 项目级示例：

```powershell
New-Item -ItemType Directory -Force -Path ".gemini\skills\life-guide"
Copy-Item -Recurse "skills\life-guide\*" ".gemini\skills\life-guide\"
```

不要只复制 `SKILL.md`，否则 references 无法按需读取。当前状态：文档适配；Gemini CLI 的发现、确认和自动激活未在本项目中验证。

官方说明：<https://geminicli.com/docs/cli/tutorials/skills-getting-started/>
