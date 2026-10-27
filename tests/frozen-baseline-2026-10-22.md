# 冻结记录：被测候选副本 4.0.4

冻结时间：2026-10-22 23:11（+0800）。冻结目录：`tests/frozen-4.0.4-2026-10-22/`。
用途：作为本轮"修改前"基线的唯一被测副本；后续任何修改都不改动本目录，以便同条件复跑。

| 项 | 记录 |
|---|---|
| 候选 Skill 版本 | 4.0.4（`SKILL.md` frontmatter `metadata.version`） |
| 仓库候选包路径 | 仓库根下标准源包目录 `skills/life-guide/`（不写本机绝对路径） |
| WorkBuddy 安装副本版本 | 3.3.0，**未同步、未覆盖** |
| 宿主 | WorkBuddy 本机会话 |
| 模型 | **未知**（无法从子 Agent 输出确认具体模型标识） |
| 加载方式 | **手动加载候选内容**：被测子 Agent 先读冻结副本的 `SKILL.md`，再按其指示读同目录 `references/`。**不是自动触发，不是安装后测试** |
| 与历史运行的关系 | 本轮新运行**不能**证明 2026-10-18 旧运行的根因；旧运行完整原始输出与工具记录缺失，未以摘录补造 |

## 文件清单与 sha256（前 16 位）

| 文件 | sha256 |
|---|---|
| `SKILL.md` | `63f4fc8884d42e65` |
| `CHANGELOG.md` | `93654af15601d52a` |
| `references/decision-framework.md` | `8b4a67ee763f1b0b` |
| `references/examples.md` | `0270eaec0ee03879` |
| `references/needs-clarification.md` | `08b10f03ca4251bc` |
| `references/option-expansion.md` | `6e27b028b3bcf4e9` |
| `references/persistent-mode.md` | `063fce90defd0f60` |
| `references/quick-mode.md` | `ab57df86d5c2a4fa` |
| `references/research-specialists.md` | `17bcf222ea4d4413` |
| `references/search-playbook.md` | `c952b27ac691c4f3` |
| `references/tool-access.md` | `b3617ad480077333` |
| `assets/decision-log.md` | `a2d45b1b4d87bf96` |
