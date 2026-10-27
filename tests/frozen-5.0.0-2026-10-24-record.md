# 冻结记录：单根因验证轮被测副本 5.0.0（2026-10-24 第二轮）

总指挥命令范围：只验证一个根因（"标出未知但不推导分支后果"），不扩张范围；验证完成前不修改技能正文、版本号、description、README 或参考文件。

## 冻结信息（本轮全部重新读取核实）

| 项 | 记录 |
|---|---|
| 被测版本 | **5.0.0**（`SKILL.md` frontmatter `metadata.version`，本轮重新读取确认） |
| 冻结目录 | `tests/frozen-5.0.0-2026-10-24/`（14 个文件，sha256 见下表） |
| 宿主 | ZCode 桌面版（本会话） |
| 模型 | 会话默认模型 GLM-5.3-Flash；子 Agent 使用宿主默认模型设定，**未从子 Agent 内部单独确认具体标识** |
| 加载方式 | **手动加载候选内容**：被测子 Agent 先读冻结副本 `SKILL.md`，再按其指示读同目录 `references/`。非自动触发、非安装实测 |
| 提示词 | 见 `runs-2026-10-24-round2/inputs/`，逐字照录总指挥命令。**注意：本轮第一轮提示词不含"请实际使用检索工具"句（与 10-22/10-24 前轮不同），核验行为必须来自技能本身，不得由提示词触发** |
| 工具与来源记录 | 各运行文件由被测 Agent 自行写入其回答全文；其检索行为与来源标注在回答内，逐字保存不加工 |
| Computer Use | 本会话重试仍不可用（错误原文："Computer Use is unavailable for this node_repl session"），WorkBuddy 应用内触发验证本轮无法执行，如实记录 |
| 历史记录关系 | 此前各轮报告（10-18/10-22/10-24 第一轮）仅作历史参考；本轮未重新读取的内容一律标"未核实"，不引用旧报告充当当前证据 |

## 文件清单与 sha256（前 16 位）

| 文件 | sha256 |
|---|---|
| `SKILL.md` | `81a706fc4f9ab709` |
| `CHANGELOG.md` | `c024a96b7ee9f65c` |
| `references/decision-framework.md` | `fea5f13598017cc7` |
| `references/examples.md` | `0270eaec0ee03879` |
| `references/gap-map.md` | `45db2c910c269997` |
| `references/needs-clarification.md` | `bbbc12965834ddeb` |
| `references/option-expansion.md` | `6e27b028b3bcf4e9` |
| `references/persistent-mode.md` | `063fce90defd0f60` |
| `references/quick-mode.md` | `ab57df86d5c2a4fa` |
| `references/research-specialists.md` | `17bcf222ea4d4413` |
| `references/search-playbook.md` | `3681d4329a4eb846` |
| `references/supervision-protocol.md` | `43320b79fd196086` |
| `references/tool-access.md` | `b3617ad480077333` |
| `assets/decision-log.md` | `a2d45b1b4d87bf96` |
