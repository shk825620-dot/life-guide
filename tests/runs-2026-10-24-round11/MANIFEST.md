# Round11 配对评测运行 Manifest

统一字段：任务编号 | 条件(A无技能/B有技能手动加载) | 输入文件(sha256 前16位) | 模型 | 宿主 | Skill 加载方式 | 实际读取的 Skill 文件 | 工具可用性 | 开始/结束时间 | 时长 | 工具调用次数 | 失败或重试 | 输出路径 | 人工判定依据

通用值：模型=会话默认 GLM（未从子代理单独确认标识）；宿主=ZCode 桌面版；工具可用性=WebSearch/WebFetch/Write 可用（A 组基本未用检索）；**绝对开始/结束时间=未取得**（仅记录时长）；**B 组实际读取的 Skill 文件=未取得**（round11 提示词未要求自报读取清单——记录流程缺陷，wave2/3 已改为要求自报）；人工判定依据=行为矩阵（round11 报告第二节）+ 原文引用。

输入哈希：T1-learning b05629c7374d009c；T2-health be080031007defc4；T3-procurement 2fea6e7afbc655b1；T4-legal 22876e760b8565e8；T5-deadline 31ef102ffe5c2ecf；T6-eldercare d94b76458944d680；T7-offer d9d0e4937a725f15；T8-tech 86381fea661e2761。

## Wave 1（2026-10-24）

| 任务 | 条件 | 时长(ms) | 工具调用 | 失败/重试 | 输出路径 |
|---|---|---|---|---|---|
| T1 | A | 86476 | 1 | 无 | A/T1-learning.md |
| T1 | B | 441689 | 15 | 无 | B/T1-learning.md |
| T2 | A | 83023 | 1 | 无 | A/T2-health.md |
| T2 | B | 470378 | 17 | 无 | B/T2-health.md |
| T3 | A | 127255 | 2 | 无 | A/T3-procurement.md |
| T3 | B | 502622 | 18 | 无 | B/T3-procurement.md |
| T4 | A | — | — | 第 1 次并发失败，第 2 次成功 | A/T4-legal.md |
| T4 | A(成功次) | 78733 | 1 | — | 同上 |
| T4 | B | 320284 | 12 | 无 | B/T4-legal.md |
| T5 | A | 157584 | 2 | 无 | A/T5-deadline.md |
| T5 | B | 349328 | 11 | 无 | B/T5-deadline.md |
| T6 | A | 95928 | 1 | 无 | A/T6-eldercare.md |
| T6 | B | 379759 | 13 | 无 | B/T6-eldercare.md |
| T7 | A | 71658 | 1 | 无 | A/T7-offer.md |
| T7 | B | — | — | 第 1 次并发失败，第 2 次成功 | B/T7-offer.md |
| T7 | B(成功次) | 404547 | 14 | — | 同上 |
| T8 | A | 69367 | 1 | 无 | A/T8-tech.md |
| T8 | B | 427928 | 27 | 无 | B/T8-tech.md |

## Wave 2（2026-10-24）

（运行中，逐行补记）

## Wave 3（2026-10-24）

（待 wave2 后执行）
| T1 | A(w2) | 113967 | 1 | 无（自报未用检索） | A/T1-learning-w2.md |
| T1 | B(w2) | 181671 | 12 | 无；读取自报：SKILL+6 refs（needs-clarification/gap-map/option-expansion/search-playbook/decision-framework/quick-mode）；检索 4 次（2026-10-25） | B/T1-learning-w2.md |
| T2 | A(w2) | 78102 | 1 | 无（自报未用检索） | A/T2-health-w2.md |
| T2 | B(w2) | 338058 | 18 | 无；读取自报：SKILL+6 refs（needs-clarification/gap-map/option-expansion/search-playbook/decision-framework/quick-mode）；官方筛查方案原文逐条打开（2026-10-25） | B/T2-health-w2.md |
| T3 | A(w2) | 189156 | 3 | 无（自报用检索：2026 机型价格/租赁行情） | A/T3-procurement-w2.md |
| T3 | B(w2) | 456504 | 16 | 无；读取自报：SKILL+6 refs（needs-clarification/gap-map/decision-framework/search-playbook/option-expansion/quick-mode）；检索 8 次（2026-10-25） | B/T3-procurement-w2.md |
| T4 | A(w2) | 70833 | 2 | 无（自报用检索 1 次） | A/T4-legal-w2.md |
| T4 | B(w2) | 285557 | 14 | 无；读取自报：SKILL+6 refs（needs-clarification/gap-map/search-playbook/option-expansion/quick-mode/decision-framework）；核验食品安全法 36/45 条等（2026-10-25） | B/T4-legal-w2.md |
| T5 | A(w2) | 86898 | 2 | 无（自报未用检索） | A/T5-deadline-w2.md |
| T5 | B(w2) | 318956 | 15 | 无；读取自报：SKILL+7 refs（needs-clarification/gap-map/quick-mode/decision-framework/option-expansion/search-playbook/examples）；核验民法典 586/587 条原文等 4 次检索（2026-10-25） | B/T5-deadline-w2.md |
| T6 | A(w2) | 68041 | 2 | 无（自报未用检索） | A/T6-eldercare-w2.md |
| T6 | B(w2) | 337742 | 15 | 无；读取自报：SKILL+7 refs（needs-clarification/gap-map/option-expansion/decision-framework/search-playbook/quick-mode/persistent-mode）；检索 6 次（长护险/跌倒数据/助餐政策/预收费新规/异地结算，2026-10-25） | B/T6-eldercare-w2.md |
| T7 | A(w2) | 54608 | 1 | 无（自报未用检索） | A/T7-offer-w2.md |
| T7 | B(w2) | 332315 | 12 | 无；读取自报：SKILL+6 refs（needs-clarification/gap-map/decision-framework/option-expansion/search-playbook/quick-mode）；检索 2 次+回查 BLS 与劳动合同法实施条例原文（2026-10-25） | B/T7-offer-w2.md |
| T8 | A(w2) | 61086 | 1 | 无（自报未用检索） | A/T8-tech-w2.md |
| T8 | B(w2) | 165004 | 13 | 无；读取自报：SKILL+6 refs（needs-clarification/quick-mode/option-expansion/gap-map/search-playbook/decision-framework）；检索 5 次（ES 堆内存/FTS5/ngram/zhparser/Meilisearch，2026-10-25） | B/T8-tech-w2.md |
| T1 | A(w3) | 80090 | 1 | 无（自报未用检索） | A/T1-learning-w3.md |
| T1 | B(w3) | 286141 | 14 | 无；读取自报：SKILL+7 refs（needs-clarification/gap-map/option-expansion/search-playbook/decision-framework/quick-mode/persistent-mode）；检索+核验在线资源（2026-10-25） | B/T1-learning-w3.md |
| T2 | A(w3) | 86790 | 2 | 无（自报未用检索） | A/T2-health-w3.md |
| T2 | B(w3) | 416324 | 20 | 无；读取自报：SKILL+4 refs（needs-clarification/gap-map/search-playbook/decision-framework）；2025 版卫健委体检指引等权威来源核对（2026-10-25） | B/T2-health-w3.md |
| T3 | A(w3) | 90773 | 1 | 无（自报未用检索） | A/T3-procurement-w3.md |
| T3 | B(w3) | 464223 | 19 | 无；读取自报：SKILL+4 refs（decision-framework/search-playbook/gap-map/option-expansion）；检索行情+WebFetch 两篇原文（一篇如实标注未完整打开，2026-10-25） | B/T3-procurement-w3.md |
| T4 | A(w3) | 60724 | 3 | 无（自报用检索） | A/T4-legal-w3.md |
| T4 | B(w3) | 260260 | 15 | 无；读取自报：SKILL+6 refs（needs-clarification/gap-map/search-playbook/option-expansion/decision-framework/quick-mode）；WebSearch（2026-10-25） | B/T4-legal-w3.md |
| T5 | A(w3) | 51247 | 1 | 无（自报未用检索） | A/T5-deadline-w3.md |
| T5 | B(w3) | 299714 | 18 | 无；读取自报：SKILL+6 refs（needs-clarification/gap-map/decision-framework/quick-mode/search-playbook/option-expansion）；司法部民法典全文逐字核对 586/587/724 条+密云区政府风险提示（2026-10-25）；打不开的页面如实未引用 | B/T5-deadline-w3.md |
| T6 | A(w3) | 61493 | 1 | 无（自报未用检索） | A/T6-eldercare-w3.md |
| T6 | B(w3) | 241090 | 14 | 无；读取自报：SKILL+6 refs（needs-clarification/gap-map/decision-framework/option-expansion/search-playbook/examples）；检索 4 次（能力评估国标 GB/T 42195-2022/长护险/机构备案/适老化改造，2026-10-25） | B/T6-eldercare-w3.md |
| T7 | A(w3) | 49783 | 2 | 无（自报未用检索） | A/T7-offer-w3.md |
| T7 | B(w3) | 349046 | 16 | 无；读取自报：SKILL+6 refs（needs-clarification/decision-framework/gap-map/examples/option-expansion/search-playbook）；检索 3 次+原文核验 4 次（财新/潮新闻已打开；IT桔子/BBC 打不开→数字未采用，2026-10-25） | B/T7-offer-w3.md |
| T8 | A(w3) | 60444 | 2 | 无（自报未用检索） | A/T8-tech-w3.md |
| T8 | B(w3) | 301368 | 26 | 无；读取自报：SKILL+6 refs（needs-clarification/option-expansion/decision-framework/quick-mode/search-playbook/gap-map）；官方文档核验 ES 堆内存/FTS5/ngram 5.7.6/zhparser/Meilisearch/Typesense（2026-10-25） | B/T8-tech-w3.md |
