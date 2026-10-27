# 方法复用核查记录

日期：2026-10-18。用途：记录本轮设计参考了哪些公开做法、采用到什么程度，以及明确不外推什么。外部项目仅作方法来源，不复制其提示词、代码或产品承诺。

## 吸收的做法

- **Agent Skills 标准与官方示例**：一个独立 Skill 目录包含入口、可选 references 和 assets；入口说明何时使用，详细材料按需读取。Anthropic 的公开仓库也提醒：展示用 Skill 的表现可能与实际宿主不同，应在目标环境测试。因此将通用核心设为唯一入口、把细则留在 `references/`，并把 WorkBuddy 元数据隔离在适配说明中。标准格式不能保证所有宿主自动触发或具有相同工具。
- **证据约束的独立判断**：开源项目 I Can't 的公开说明把“压力不是证据”“证据充分时改判”“避免为了反对而产生假阴性”与小型测试放在一起。这里吸收的是可证伪的判断纪律：不因重复要求改变事实结论，也不把“不迎合”变成固定悲观人格。它自己的 README 同样把少量单次探针限定为定向 smoke test，不外推成普遍提升。
- **窄任务委派与主 Agent 综合**：OpenAI 官方编排文档描述了 manager/worker 与 handoff 模式；Anthropic 多 Agent 研究系统分享了具体协调经验。这里仅采用任务边界清楚、彼此独立时才委派、主 Agent 负责关键事实复核和最终综合。角色卡不保证宿主支持独立子 Agent，也不证明多 Agent 一定更好。
- **扩大候选空间**：HBS 的价值链视角和 Tom Ritchey 的形态分析可以帮助发现不同参与位置、维度组合和组合不相容之处。它们提供检查视角，不证明某个小生意有需求，也不意味着每道题都要做产业链或全组合枚举。
- **按影响匹配调查力度**：英国 Green Book 的公共项目评估强调让分析深度与事项相称，并留意乐观偏差。本 Skill 只借鉴比例原则和核查悲观/乐观假设；不把政府投资评估流程直接套到个人选择。
- **外部参照与关键假设**：Kahneman 与 Lovallo 讨论当前计划的“内部视角”会忽略相似情况的既往统计；CIA 的结构化分析手册提供关键假设检查、外部视角与反方分析。对应到本 Skill：只有重要预测和高影响选择才触发；要检查比较类是否真的相似、数据口径和适用边界，缺少可靠基准时不编概率。
- **失败预演**：Gary Klein 的 HBR 方法让参与者假设项目已经失败，再提出可能原因，以便在决策前暴露可修正的问题。本 Skill 将其缩成两三条会改变行动的失败路径、早期信号和验证动作；不把它变成每题固定仪式，也不把方法本身说成成功保证。
- **社交线索与现实行为**：X、小红书和社区内容可帮助发现用户语言、痛点与绕行办法，但帖子热度不等于普遍需求。技能要求继续核查使用、付费、复购、迁移或有成本试点等行为，并保留样本、时间与地区边界；这是证据纪律，不是已验证的市场预测模型。

## 有意不采用

- 不把“敢顶撞”写成无条件反对用户；结论由证据而非人格姿态决定。
- 不让每个问题启动全部角色，不把多 Agent 数量当质量指标。
- 不强制至少列五个商业方案，不把耗材、设备、上游等候选直接包装成商机。
- 不把 GitHub stars、营销榜单或一手来源身份单独当成效果或适配证明。
- 不把单个开源 Skill 的样例或其自报评测当作本项目效果证据。

## 原始来源

- [Agent Skills Specification](https://agentskills.io/specification)
- [Anthropic：Public Agent Skills repository](https://github.com/anthropics/skills)
- [I Can't：evidence-gated anti-sycophancy skill](https://github.com/achen919/Icant)
- [OpenAI：Orchestration and handoffs](https://developers.openai.com/api/docs/guides/agents/orchestration)
- [Anthropic：How we built our multi-agent research system](https://www.anthropic.com/engineering/multi-agent-research-system)
- [Harvard Business School：The Value Chain](https://www.isc.hbs.edu/strategy/business-strategy/Pages/the-value-chain.aspx)
- [Tom Ritchey：General Morphological Analysis](https://swemorph.com/ma.html)
- [UK HM Treasury：The Green Book 2026](https://www.gov.uk/government/publications/the-green-book--2/the-green-book-2026)
- [Kahneman 与 Lovallo：Timid Choices and Bold Forecasts（1993）](https://pubsonline.informs.org/doi/10.1287/mnsc.39.1.17)
- [美国政府：A Tradecraft Primer（关键假设检查、外部视角等）](https://www.cia.gov/resources/csi/static/Tradecraft-Primer-apr09.pdf)
- [Gary Klein：Performing a Project Premortem（HBR，2007）](https://hbr.org/2007/09/performing-a-project-premortem)

这些来源支持方法设计参考，不证明本 Skill 已提高真实用户结果。方法来源与时间敏感的实际事实来源分开处理。
