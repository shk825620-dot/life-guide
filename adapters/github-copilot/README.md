# GitHub Copilot 适配

GitHub Copilot 支持把标准 Skill 放入项目的 `.github/skills/life-guide/`、`.claude/skills/life-guide/` 或 `.agents/skills/life-guide/`；个人 Skill 可放在宿主支持的个人技能目录。Copilot 根据 Skill 描述判断相关性，复杂任务才加载详细内容。

项目发布时建议把核心目录复制到 `.github/skills/life-guide/`，并保留全部 references。用一个学习路线、采购比较或法规核查问题分别测试发现和实际加载，不把“目录可放置”当成“自动触发已证明”。

官方说明：<https://docs.github.com/en/copilot/concepts/customizations/agent-skills>

当前状态：路径和说明适配；Copilot 各产品形态的真实发现、自动加载和工具行为未在本项目中验证。
