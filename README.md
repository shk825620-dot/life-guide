# 减少信息差（life-guide）

> 让 AI 在给建议之前，先查出你没考虑到的那几个选项、代价和证据。

life-guide 是一个 Agent Skills 通用技能。面对「推荐什么、怎么开始、选哪条路、这个说法可信吗」这类问题，它让 AI 先识别会改变答案的关键条件，再调查现成工具、不同路线和适用规则，最后给出有来源、有取舍、有下一步的判断。

## 为什么不只是再问一次 AI

AI 让“得到一个答案”变得很快，但真正有价值的信息，往往藏在答案背后的检索路径里：知道去哪里找、该用什么关键词、怎样从二手线索追到原始来源。`life-guide` 把这条路径组织起来：用搜索引擎找入口，用官方文档、法规、源码和统计定事实，用 Reddit、X、微博、小红书观察真实讨论与失败信号，用 YouTube 看具体操作和版本差异，最后把关键结论回查到能支撑它的来源。

它不承诺一次列尽所有选项，也不把热度当证据；它要做的是让用户看见原本没进入视野的路线，并知道哪些已经核实、哪些仍未知、下一步怎样用最低成本验证。

**适合**：个性化推荐、多方案比较、现成工具调查、规则与例外核查、来源可靠性判断、重大或难撤回的决定。

**不适合**：单个事实、纯写作 / 翻译 / 润色、不需要情境判断的问题——这些会直接回答，不启动完整流程。

## 30 秒看懂它做什么

输入：**「我想做点小生意，但只想到奶茶店，你有什么建议？」**

| | 没有技能时常见回答 | 加载本技能后的预期形态 |
|---|---|---|
| 起点 | 直接比较奶茶、咖啡、服装店的优劣 | 先确认目标、预算、地区、可投入时间等会改变答案的条件 |
| 候选 | 在既有店型里重排 | 额外调查原料耗材、设备、配送、维修、流通等不同参与位置 |
| 证据 | 经验性判断，无出处 | 关键事实给来源与查询日期，查不到就写「未核实」 |
| 收尾 | 「可以考虑加盟」 | 给主推荐 + 备选 + 机会成本 + 最低成本验证 + 停止条件 |

以上是**行为形态示意**，不是实时市场调查，也不代表这些方向已被证明有需求或适合每个人。更完整的回应示例见 [`skills/life-guide/references/examples.md`](skills/life-guide/references/examples.md)。

## 安装（约 3 分钟）

**通用要求：复制整个 `life-guide/` 目录，不要只复制 `SKILL.md`**——参考文件按需读取，缺了规则就不可达。标准源包在 [`skills/life-guide/`](skills/life-guide/)，也可使用发布页的上传 zip（解压后顶层即 `life-guide/`）。

| 平台 | 放置位置 / 导入方式 | 如何确认已识别 |
|---|---|---|
| Claude Code | 项目 `.claude/skills/life-guide/`，或用户 `~/.claude/skills/life-guide/` | `/skills` 查看 |
| OpenAI Codex | `.agents/skills/life-guide/` | `$life-guide` 显式调用 |
| Gemini CLI | `.gemini/skills/life-guide/`，或 `gemini skills install <路径>` | `/skills list`（工作区需先 `/trust`；新增后 `/skills reload`） |
| GitHub Copilot | 项目 `.github/skills/life-guide/`（也认 `.claude/skills`、`.agents/skills`）；个人 `~/.copilot/skills/` | 提问后观察是否加载；可用 `gh skill` 安装 |
| WorkBuddy 本地 | 技能目录下的 `life-guide/` | 技能清单中出现名称与描述 |
| WorkBuddy 开放平台 | **需专用宿主包**，见 [`adapters/workbuddy/`](adapters/workbuddy/)（字段要求不同，未实测上传） | 以上架审核结果为准 |
| 豆包 / 扣子 | 内容映射，不是标准包直装，见 [`adapters/`](adapters/) | 未实测 |

Windows 示例（Git Bash，Claude Code 项目级）：

```bash
mkdir -p .claude/skills
cp -r /path/to/skills/life-guide .claude/skills/
ls .claude/skills/life-guide/SKILL.md
```

**装好后用两道题自验**：

1. 问「巴黎在哪个国家」→ 应直接回答，**不应**追问职业目标或启动调查。
2. 问「我想做点小生意，但只想到奶茶店」→ 应先复述已知、指出关键缺口并按优先级提问，**不应**直接给一份店型推荐。

两题都符合，说明加载与边界生效；不符合请按 [`CONTRIBUTING.md`](CONTRIBUTING.md) 提交宿主、版本、输入与实际输出。

## 验证边界（请先读这一段再决定是否采用）

- **结构校验通过 ≠ 效果已证明。** 结构检查与静态 CI 只证明包结构、引用与规则文本一致。
- 当前版本已完成结构和本地行为验收；**自动触发、跨宿主、跨模型和真实用户效果仍未验证**。各平台状态见 [`adapters/`](adapters/)，未实测的一律标注未验证。
- 历史行为证据来自 5.x 批次：12 次有技能运行、119/120 行为格通过，但该批次**跨版本、单宿主（ZCode）、单模型（GLM）、手动加载、人工判定**，不能外推到当前版本或其他宿主。
- 各平台状态逐项见 [`adapters/`](adapters/)：文档适配与已实测分开标注，未实测的一律写未验证。
- 本技能可能建议联网检索或读取参考资料；工具安装、账号登录与外部写入需你明确批准，技能本身不承诺「无病毒」「不封号」。

## A/B 证据与文档

- 有 / 无技能的对照证据与边界：[`docs/ab-evidence.md`](docs/ab-evidence.md)
- 发布计划与发布后观察指标：[`docs/release-plan.md`](docs/release-plan.md)
- 行为验收用例与运行记录：[`tests/`](tests/)（含评测协议、冻结基线与 A/B 原始输出）
- 包边界与维护规则：[`docs/architecture/package-boundaries.md`](docs/architecture/package-boundaries.md)

## 贡献

欢迎提交「装不上 / 不触发 / 参考文件读不到 / 回答不符合预期」四类报告，请附宿主、版本、输入与实际输出。修改规则的纪律见 [`CONTRIBUTING.md`](CONTRIBUTING.md)。

## License

MIT，见 [`LICENSE`](LICENSE)（技能包内也附带同一份许可证）。
