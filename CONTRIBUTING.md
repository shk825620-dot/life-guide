# 贡献指南

感谢你帮忙验证这个技能。当前最需要的不是新功能，而是**真实宿主里的安装与行为证据**。

## 最值得提交的四类报告

| 类型 | 需要附带的证据 |
|---|---|
| 装不上 | 宿主与版本、安装路径、目录结构截图或 `ls` 输出、报错原文 |
| 不触发 / 误触发 | 完整输入原话、是否点名技能、期望是否触发、实际是否加载 |
| 参考文件读不到 | 技能版本与包哈希、实际读取到的文件清单、缺失文件名 |
| 回答不符合预期 | 完整输入、实际输出、你期望的形态、是否联网、模型与宿主 |

**请脱敏**：不要贴私人需求文档、账号凭证、本地私有路径或他人个人信息。

## 修改规则的纪律

1. 先确认当前源包、版本与引用关系，不按旧行号覆盖。
2. 只有同时满足三条才修改通用规则：**跨领域重复出现 + 现有规则未覆盖 + 能定位唯一责任文件**。
3. 单次回答错误、来源漏标、宿主能力不足、模型偶发失误，先归类，不借机堆规则。
4. 行为修改先写通过 / 失败案例，再改规则；改完必须回归。
5. 测试案例、审计报告、个人需求、私有路径不得写进运行包 `skills/life-guide/`。
6. 不把「结构校验通过」「一次运行通过」写成「效果已证明」；提交信息里写明验证范围与未验证项。

详细维护流程见 [`docs/maintainers/CONTRIBUTING.md`](docs/maintainers/CONTRIBUTING.md)。

## 本地检查

```bash
python tests/validate_package.py
python tests/test_information_gap_protocol.py
python tests/test_rule_singularity.py
python tests/test_single_source_rules.py
python tests/test_release_hygiene.py
python tests/test_ci_coverage.py
```

这些只证明结构与文本一致，不证明业务结论正确。

## 发布与身份

发布前必须确认许可证、作者身份与目标宿主验证范围。宿主专属字段放 `adapters/`，不回写标准包。

行为准则见 [`CODE_OF_CONDUCT.md`](CODE_OF_CONDUCT.md)。
