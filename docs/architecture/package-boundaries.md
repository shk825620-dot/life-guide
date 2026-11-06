# 源码、发行包与个人资料边界

## 唯一源

- `skills/life-guide/` 是唯一可发布的 Agent Skills 核心包；修改应落在这里。
- `README.md` 负责面向使用者的项目介绍；`CHANGELOG.md` 只记录可公开、可复核的版本变化。
- `tests/` 保存行为标准和结构检查；测试结果必须另行记录实际宿主、模型、输入和判定，不把静态检查写成行为证明。
- `adapters/<host>/` 记录宿主专属字段、安装和验证要求。适配包不能成为第二份行为规则来源。
- `docs/maintainers/` 保存通用维护方法。个人需求、私有目录、完整会话、一次性返修任务和历史测试证据放入本机 `审查证据/`，不得随公共发行包发布。

## 核心包内容

运行时核心包含：需求澄清、候选扩展、检索核验、工具访问、方案比较、快/深调查，以及按需专题研究角色。每条规则有一个主要维护位置；入口只放启动判据、流程和路由。

个人书籍、个人知识库、宿主私有路径与个人记录不是启用条件。用户提供或宿主授权的资料可以在具体任务中作为补充材料，但不会自动进入公开 Skill。

| 文件 | 归属 | 是否随核心包分发 | 唯一职责 |
|---|---|---:|---|
| skills/life-guide/SKILL.md | 运行入口 | 是 | 首要准则、启动判据、主流程和参考路由 |
| references/capability-check.md | 运行细则 | 是 | 调查前能力预检与降级路径 |
| references/output-contract.md | 运行细则 | 是 | 用户可见答复的最小字段与反馈回流 |
| references/needs-clarification.md | 运行细则 | 是 | 关键缺口识别、先问后研究和进入调查的条件 |
| references/gap-map.md | 运行细则 | 是 | 信息差地图：十类缺口、重要未知三件事、未知管理统一位置 |
| references/option-expansion.md | 运行细则 | 是 | 发现不同路径、参与位置和进入方式 |
| references/search-playbook.md | 运行细则 | 是 | 选择来源、检索、反证、原文核验 |
| references/tool-access.md | 运行细则 | 是 | 按需工具、账号、权限、限流和失败处理 |
| references/supervision-protocol.md | 运行细则 | 是 | 监督与交接：三种运行方式、完成证据、打回清单 |
| references/decision-framework.md | 运行细则 | 是 | 用户目标、现实取舍、风险、可逆性和行动 |
| references/emotion-and-bias.md | 运行细则 | 是 | 情绪压力与认知偏差下的事实/感受分离、外部视角、验证与停止条件 |
| references/progressive-delivery.md | 运行细则 | 是 | 两档共用的分阶段交付：三个检查点、档位用法、记录要求与时长口径 |
| references/quick-mode.md | 运行细则 | 是 | 控制调查深度，不设固定时限或搜索次数 |
| references/persistent-mode.md | 运行细则 | 是 | 复杂调查的阶段路由和收敛，不另建澄清标准 |
| references/research-specialists.md | 可选专题角色 | 是 | 五类真实痛点对应的按需研究任务卡 |
| references/examples.md | 示例 | 是 | 展示关键行为分支；不是实测证据 |
| assets/decision-log.md | 可选模板 | 是 | 用户自愿使用的通用决策记录空白模板 |
| CHANGELOG.md | 维护记录 | 是 | 公开包的版本变化与验证边界 |
| LICENSE | 发布边界 | 是 | MIT 许可证文本 |
| tests/acceptance-cases.md | 测试标准 | 仓库级，不随 Skill 安装 | 13 个冻结行为情形，不代表已经通过 |
| tests/acceptance-cases-4.0.1.md | 新增测试标准 | 仓库级，不随 Skill 安装 | 四项新增行为回归标准；仅资源路线漏检有历史 PARTIAL 基线，其余待目标宿主实测 |
| tests/emotion-bias-acceptance-2026-10-25.md | 新增测试标准 | 仓库级，不随 Skill 安装 | 六类情绪压力与认知偏差案例；当前仅冻结标准，尚未完成真实行为验收 |
| tests/validate_package.py | 静态检查 | 仓库级，不随 Skill 安装 | 检查元数据、路由、版本、已知个人路径和角色结构 |
| tests/acceptance-report-4.0.0.md | 验收记录 | 仓库级，不随 Skill 安装 | 记录实际检查和未验证项 |
| adapters/workbuddy/README.md | 宿主适配 | 仓库级，不随标准包安装 | 说明 WorkBuddy 字段映射与当前未验证状态 |
| docs/maintainers/* | 维护资料 | 仓库级，不随 Skill 安装 | 记录方法来源和贡献/修改纪律 |
| docs/superpowers/specs/* | 设计依据 | 仓库级，不随 Skill 安装 | 保存专题角色的研究依据和设计边界 |
| 审查证据/ | 本机私人档案 | 否；由 .gitignore 排除 | 保存原始用户需求、3.3.0 快照和完整内部审查资料 |

## 标准与宿主适配

核心 `SKILL.md` 采用 Agent Skills 标准字段，版本和展示名放入标准允许的 `metadata` 映射。标准格式只说明包形态，不保证某个模型会触发、读取全部参考文件或拥有搜索/浏览器/子 Agent 工具。

WorkBuddy Open Platform 的字段与标准核心不同，详见 [`adapters/workbuddy/README.md`](../../adapters/workbuddy/README.md)。在生成独立发行物并通过目标宿主导入与实际对话验收前，不同步核心包到用户安装目录，也不声称 WorkBuddy 适配完成。

## 当前状态

- 标准核心候选：`skills/life-guide/`，版本 6.0.6（2026-11-07 更新）。
- 本轮未读取到可核验的 WorkBuddy 安装目录，不能声称已与 6.0.6 源包同步；自动触发与跨宿主行为仍未验证。
- GitHub 发布、作者展示名和目标宿主兼容性：尚未完成；许可证已采用 MIT。
