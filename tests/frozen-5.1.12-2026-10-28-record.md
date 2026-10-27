# 冻结记录：候选版 5.1.12（2026-10-28）

- 冻结时间：2026-10-28 会话内（E3/E4 行为运行前）。
- 冻结目录：`tests/frozen-5.1.12-2026-10-28/`，由 `skills/life-guide/` 全量复制。
- 冻结时候选版 frontmatter `metadata.version = 5.1.12`；CHANGELOG 最新条目 `[5.1.12] - 2026-10-28`。
- 用途：为本日 E3/E4 行为运行提供被测包归属。运行时模型加载的是同一会话内已通读的候选文件（与冻结副本逐文件同源）；哈希如下，供日后核对是否被替换。

## SHA-256（前 16 位）

```
B39FCE5B155CDF52  CHANGELOG.md
FE5AC9AA42116548  SKILL.md
2013C607443069E4  agents/openai.yaml
A2D45B1B4D87BF96  assets/decision-log.md
9CDEAA203262318A  references/decision-framework.md
912F9143F242D1B2  references/emotion-and-bias.md
0270EAEC0EE03879  references/examples.md
6F45F26960B2B38D  references/gap-map.md
C9EE7F438853C75E  references/needs-clarification.md
6E27B028B3BCF4E9  references/option-expansion.md
5D8B9FA30BF1611A  references/persistent-mode.md
CD0B837D655F85CB  references/progressive-delivery.md
029D64EC939C0058  references/quick-mode.md
17BCF222EA4D4413  references/research-specialists.md
1BF9739FF54C189D  references/search-playbook.md
F03F6382727E418A  references/supervision-protocol.md
9D25FF4D4CDE03A8  references/tool-access.md
```

## 边界

本冻结只锁定文件内容归属，不证明任何行为。会话内曾观察到候选文件在 2026-10-28 00:18–00:22 被并发编辑（SKILL.md §1.5 顺序规则与 CHANGELOG 第 (4) 条同期更新）；本冻结发生在该并发编辑之后，若后续再有编辑，须重新冻结并另立版本归属。
