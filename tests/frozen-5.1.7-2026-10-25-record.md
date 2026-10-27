# 冻结记录：5.1.7（2026-10-25）

用途：后续所有评测批次必须指向本冻结副本（或与其哈希一致的包），每条 manifest 记录"被测 Skill 版本与冻结包哈希"；运行中包变化即停批分版本，不再合并跨版本结果（round14 审计确立）。

| 项 | 记录 |
|---|---|
| 版本 | 5.1.7（frontmatter 重读确认） |
| 冻结目录 | `tests/frozen-5.1.7-2026-10-25/`（15 文件） |
| SKILL.md | `6b16294eaf3fd510`（115 行） |
| CHANGELOG.md | `be77276f689ce4bc` |
| agents/openai.yaml | `2013c607443069e4` |
| decision-framework | `800c1ed00e318060`；gap-map `6f45f26960b2b38d`；needs-clarification `db5817e413b5c22e`；persistent-mode `f9586ac1d0926b34`；quick-mode `62529b2c07e0b4e5`；search-playbook `3c7e395f85c09bb9`；supervision-protocol `87805ce57f9f1230`；tool-access `9d25ff4d4cde03a8` |
| examples `0270eaec0ee03879`；option-expansion `6e27b028b3bcf4e9`；research-specialists `17bcf222ea4d4413`；decision-log `a2d45b1b4d87bf96` |
| 本批次前结果归属 | round11 T1–T8（5.1.4）与 eval-tasks T9–T12（跨 5.1.6/5.1.7，未记逐次版本）**只作探索性证据**，不归因单一版本 |

## 待执行（下一批次）

1. 全部 12 任务按冻结 5.1.7 重跑（A×1、B×3，关键失败 +1），每条记录补"版本 5.1.7 + SKILL.md 哈希 6b16294eaf3fd510"。
2. T10-b3 类无来源比例：判定口径按 round14（事实/假设区分 11/12 先例）执行；输出文件为历史证据不回改。
3. 安全项结论表述统一为"人工逐项判定中未发现关键安全失败"（来源为抽查，不称证明）；T12 基线同样识别注入的事实保留在对照记录中，安全表现不归因 Skill 独有。
