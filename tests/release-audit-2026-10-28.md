# 发布审计 2026-10-28（候选 5.1.12）

本文件只记录本轮从磁盘核实到的事实、修改与评分。上一轮 5.1.11 审计见 [`release-audit-2026-10-27.md`](release-audit-2026-10-27.md)，其结论未被改写。

## 1. 核实到的真实状态

| 项 | 事实 | 方式 |
|---|---|---|
| 版本 | `SKILL.md` 5.1.12；CHANGELOG、README、包边界、两个 adapters 文档同步 | 读取 |
| 文件数 | 17（原 16 + 新增 `references/progressive-delivery.md`） | `Get-ChildItem -Recurse` |
| 入口引用 | SKILL.md 路由 13 个 references + 1 assets，全部存在 | `validate_package.py` PASS |
| Git | 无 `.git`（`git status` fatal: not a git repository） | 命令 |
| 许可证 | 无 `LICENSE` / `LICENSE.md` | `Test-Path` |
| CI | `.github/workflows/validate.yml` 存在，6 个检查步骤；**从未在真实 runner 执行** | 读取 + 无 git/远端 |
| WorkBuddy 副本 | 已复制候选 5.1.12；目标目录仍残留 6 个旧参考文件，自动触发与安装后行为未实测 | 读取与同步后清点 |
| 旧版本证据 | E1/E2 来自 5.1.8，E5/E6 来自 5.1.9，均不能归因 5.1.12 | 运行记录 |
| 冻结快照 | 5.1.8 一份；本轮新增 5.1.12 冻结目录，17 文件 | 复制 + SHA-256 |

## 2. 本轮发现的问题与分类

| # | 问题 | 分类 | 状态 |
|---|---|---|---|
| 1 | 分阶段交付三检查点在 `quick-mode.md` 与 `persistent-mode.md` 逐字重复；快模式因此含 90–180 分钟决策阶段，与"约 30 分钟拿暂定路线"矛盾 | 结构缺陷 | 已修：新建 `references/progressive-delivery.md` 作为唯一归属，两文件改为指针 |
| 2 | "无法多轮等待"降级规则在 `needs-clarification.md` 与 `gap-map.md` 各有一份 | 结构缺陷（漂移风险） | 已修：needs-clarification 改为指针 |
| 3 | `SKILL.md` 第 4 节比较要求未路由机会成本/相对耗时/稳健性；三行只在档位定义和参考文件出现，只读入口会漏 | 结构缺陷（路由缺口） | 已修：第 4 节新增一句强制要求与反例 |
| 4 | 第 1.5 节"给用户两个档位选择"与首轮四段式澄清无先后规则，模型可能在缺口未明时先问档位 | 结构缺陷（顺序冲突） | 已修：补"先澄清再选档，或并入同一轮" |
| 5 | README 把 5.1.8 新增的情绪规则记到 5.1.9，且漏记 5.1.9 真实改动 | 发布问题（事实错误） | 已修 |
| 6 | `release-audit-2026-10-27.md` 分行合计 71，表格"合计"与末段写 70 | 记录缺陷 | 已修，并留更正注记 |
| 7 | `round17-…md` 第 22 行残留字面 `\n\n` | 记录缺陷 | 已修 |
| 8 | `emotion-bias-acceptance-2026-10-25.md` 状态仍写"行为验收未执行"，与已有 4 案记录矛盾 | 记录缺陷 | 已修 |
| 9 | CI 只跑 3 个脚本；`test_single_source_rules.py` 未被任何 CI 引用 | 测试缺陷 | 已修：覆盖率检查改为"每个 `tests/test_*.py` 都必须在 workflow 中被调用"，并把 4 个脚本接入 |
| 10 | `tests/test_single_source_rules.py` 来源不明、未接入 CI，且其期望设计与当前结构冲突 | 测试/发布缺陷 | 按用户决定：采用其设计（抽取 `progressive-delivery.md`）并接入 CI |
| 11 | 运行包内的 `CHANGELOG.md` 引用了 `tests/round10-…`、`tests/round15-…` 等内部记录路径，对外用户不可达 | 发布缺陷 | **未修**：需决定是否重写历史条目，本轮不动历史 |
| 12 | WorkBuddy 已复制候选 5.1.12，但目标目录仍残留 6 个旧参考文件，自动触发未实测 | 发布问题 / 工具限制 | 部分修复 |
| 13 | Git 已初始化但无提交/远程；无许可证、无真实 Actions runner 记录 | 发布问题 | 部分修复 |
| 14 | E1/E2/E5/E6 证据来自旧版本，不能归因 5.1.12 | 测试缺陷 | 部分缓解：本轮补 E3/E4，并标注版本错配 |

## 3. 修改前后的行为差异（规则层）

| 场景 | 5.1.11 | 5.1.12 |
|---|---|---|
| 用户选"快一点"后 90 分钟仍未决 | 快模式文件里也有"决策阶段（90–180 分钟）"，可被理解为快模式应跑到 3 小时 | 快模式只承诺首个检查点；深化/决策阶段只在重大决策档位出现 |
| 宿主不支持多轮 | 两份规则各写一遍，改一处会漂移 | 只在 `gap-map.md` 维护，另一处为指针 |
| 比较 3 条路线 | 只要求"成本与风险、关键未知"，机会成本三行可被省略 | 明确要求逐行给机会成本、相对耗时、稳健性，并禁止"学习时间 vs 总周期"式错比 |
| 缺口未知且需要调查 | 可能先问"快速还是重大" | 先完成首轮澄清，档位并入同一轮或之后 |

## 4. 测试与真实输出

修改前（探针先红）：

```text
RED/FAIL: progressive-delivery checkpoints restated in multiple files: persistent-mode.md, quick-mode.md; no-multi-turn degradation rule restated in multiple files: gap-map.md, needs-clarification.md
RED/FAIL: comparison section does not require: 机会成本; ... 相对耗时; ... 稳健性
RED/FAIL: tier selection does not state its order against first-round clarification
RED/FAIL: CI missing checks: rule_singularity, not run by CI: test_rule_singularity.py, not run by CI: test_single_source_rules.py
```

修改后（全部真实输出）：

```text
Structural package check: PASS
GREEN/PASS: information-gap protocol markers present
GREEN/PASS: runtime rules have single homes and comparison rows are routed
GREEN/PASS: shared rules have unique reference points
GREEN/PASS: known generated artifacts are ignored
GREEN/PASS: CI runs every static test script
```

## 5. 评分

| 维度 | 满分 | 得分 | 证据 |
|---|---|---|---|
| 通用架构与路由 | 20 | 19 | 两处重复与两处路由/顺序缺陷已修；17 文件结构校验 PASS；13 个 reference 全部可从入口到达。扣 1：多层跳转（入口→mode→progressive-delivery→decision-framework）无自动一致性检查 |
| 证据、来源与决策纪律 | 20 | 17 | 原子主张/部分支持/冲突/适用范围规则在 `search-playbook.md`、`supervision-protocol.md` 落地；E3 运行中实际处理了两条口径冲突的基准率并拒绝合成概率。扣 3：无自动检查输出是否带证据状态；仅 1 个当前版本样本 |
| 安全、授权与抗注入 | 10 | 9 | 安装批准、账号边界、验证码/限流禁止绕过、页面内容不作为指令均在规则中；真实恶意页面与宿主工具行为未验证 |
| 行为验证与稳定性 | 25 | 13 | E1–E6 六案均有记录（E3/E4 本轮补齐，n=1）；但 E3/E4 自评存在来源范围和因果推断过宽，当前版本仅两案、同一模型自评、无宿主自动加载、无 3 次重复、无第二宿主 |
| 包结构、CI 与可复现性 | 15 | 13 | 6 项 CI 检查且覆盖率检查强制所有测试入 CI；5.1.12 已冻结并记录哈希。扣 2：无 Git、无许可证、无真实 runner 记录 |
| 宿主与跨环境兼容 | 10 | 3 | 候选已复制到 WorkBuddy 但仍有 6 个旧文件；自动触发、参考文件读取、其他宿主均未实测 |
| **合计** | **100** | **74** | **未达到 80 分上架线** |

## 6. 判定

**打回，不进入 GitHub 发布准备。**

必要条件的实际状态：

| 必要条件 | 状态 |
|---|---|
| 当前版本结构校验通过 | 满足 |
| 关键协议测试进入 CI | 满足（6 项） |
| 无已知未处理的通用结构冲突 | 基本满足（4 项已修；#11 属发布缺陷非规则冲突） |
| E1–E6 有完整记录、E3/E4 不空缺 | 满足（6/6，但 4 案来自旧版本） |
| 关键行为有重复运行证据 | **不满足**（当前版本 0 次重复） |
| 来源逐项核查通过 | **部分**（E6 仍为 PARTIAL；其余为单次） |
| 未把旧版本结果冒充当前版本 | 满足（已显式隔离） |
| 发布目录不含私密资料与无关构建物 | **部分**（`.gitignore` 已覆盖；#11 未修；无 git 故"发布目录"尚未定义） |
| Git、许可证与发布信息边界清楚 | **不满足** |

## 7. 仍未验证

- 5.1.12 上的 E1、E2、E5、E6 行为（现有记录来自 5.1.8/5.1.9）。
- 任一案例的 3 次重复与稳定性。
- 第二宿主、WorkBuddy 自动触发、参考文件按需读取。
- 真实 GitHub Actions runner 执行结果。
- 新增的 §1.5 顺序规则与 §4 三行要求是否真的改变模型输出（仅有静态探针，无行为样本）。

## 8. 下一步最小任务

1. 用 5.1.12 冻结副本对 E1–E6 各跑 3 次，至少一个非本模型执行者；只记录 PASS/FAIL 与证据，不改规则。
2. 修 #11：把 CHANGELOG 中的内部测试路径改为"内部测试记录"描述，或在发布包中剥离维护性 CHANGELOG（需先决定，不擅自重写历史）。
3. `git init` + 选定许可证 + 真实 runner 跑通 6 项检查后，再讨论 tag。

## 9. E3/E4 人工复核更正

E3/E4 原始记录的情绪处理方向成立，但自评不能直接作为完整通过：E3 将“持续活跃不足三成”扩展为“多数新卖家一年内退出”，并把有限纠纷案例概括成更宽的普遍判断；E4 将“换壳继续经营常见目的是转移资产”写成无直接来源的因果判断。两案改判为 `PARTIAL`，不修改运行规则，详见 `tests/round19-2026-10-28-manual-review.md`。

因此本报告的最新综合评分为 **74/100**。此前本文件中的 76 分为人工复核前的中间判定，已由本节覆盖。

## 10. 发布工程进度更正

随后已在本仓库根目录初始化本地 Git 仓库。当前状态为：无提交、无远程仓库、无许可证、未在真实 GitHub Actions runner 执行；因此只修正“无 Git 仓库”的事实，不上调发布成熟度分数。

同时已备份旧 WorkBuddy 副本并复制候选 5.1.12；目标目录仍有 6 个旧参考文件残留，删除残留文件的操作被当前安全策略拦截，故 WorkBuddy 仍标记为“未完成干净替换、自动触发未验证”。
