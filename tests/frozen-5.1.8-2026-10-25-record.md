# 冻结记录：5.1.8（2026-10-25）

用途：为情绪与认知偏差验收固定唯一被测包。后续运行必须使用此目录；包内容变化时停止当前批次并按版本分组。5.1.7 冻结副本保持不变。

| 项 | 记录 |
|---|---|
| 版本 | 5.1.8（读取冻结副本 `SKILL.md` frontmatter 确认） |
| 冻结目录 | `tests/frozen-5.1.8-2026-10-25/` |
| 文件数 | 16 |
| 当前候选与冻结副本 | 16/16 文件 SHA-256 完全一致（2026-10-25 独立复核） |
| `SKILL.md` 实际行数 | 77（候选与冻结一致） |

## SHA-256

```text
agents/openai.yaml 2013c607443069e4b2967fee02db46fdeb8db65d6b90cdc76e1e35123a4b7287
assets/decision-log.md a2d45b1b4d87bf967facae02bd55dc6317c128dfc63967a1a92b20b92664f4f0
CHANGELOG.md eaa3cb48cea59f0d07dd68d8153cff73004020dc4e65214078c9ec7a92b40266
references/decision-framework.md 9cdeaa203262318a0ba939c3d33021de4e4426a1e1382ca9710fea19c1408d03
references/emotion-and-bias.md 912f9143f242d1b28d2b6d5a19dd490a4908da6830f7cc066b13e3bc7e6d47c1
references/examples.md 0270eaec0ee038790fb6899885f0c6834e23acb4163ab593068914e72b6d2026
references/gap-map.md 6f45f26960b2b38dddfc6fc2d10acd2095647a5384c94d6c67c7595a0960f5a6
references/needs-clarification.md db5817e413b5c22e5efb6d8c50eb95ad1600f59746ac632c6c13c9b74c48fe41
references/option-expansion.md 6e27b028b3bcf4e99ec60c08f1173bcaf7bb1d146ca5d9e30fe68c4220c8da81
references/persistent-mode.md f9586ac1d0926b34750e86b4c4f042b666b27c7f2581ce30bf4cc3e6f5baa147
references/quick-mode.md 62529b2c07e0b4e59b048134c59bf98c3c8964bb4c75e6a50ac762af622a4cf9
references/research-specialists.md 17bcf222ea4d4413e352abe719197654c1bb29585c5d3267e49c610b592993b4
references/search-playbook.md 3c7e395f85c09bb9e18cb565973387c98fff762a2d910c1410a32d958b863730
references/supervision-protocol.md 87805ce57f9f123074db5005f0669dbf70322877e8e19217abc05bd8b320e74e
references/tool-access.md 9d25ff4d4cde03a87f5985d3eccc4cb83ad85a79a2456c4d81942fbeaad5fbad
SKILL.md deb7a0fa9401d95249a1765848636b0c86ba62effa8e9b661159ec5f45944d01
```

## 复核边界

- 冻结目录存在，当前候选包与冻结包逐文件哈希一致。
- 原验收记录把 `SKILL.md` 写成 116 行；实际候选与冻结均为 77 行，已在独立复核中更正。
- 冻结记录此前未单独落盘；本文件补齐哈希清单，不改变被测包和历史回答。
- 该冻结只证明测试对象固定，不证明情绪偏差行为已经稳定或跨宿主可用。
